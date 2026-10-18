#!/usr/bin/env python3
"""Phase 7: merge the price readings into one offers file for the optimizer. Offline, no network.

Run it with the "Run Python File" button (no arguments). It reads, under data/prices/:
  <stamp>.json                  the script runs of scripts/read_store_prices.py (per store and card the newest
                                run read without error wins, so a partial run adds cards to the earlier ones)
  browser-<store>-<date>[-wishlist].psv
                                readings of Shopify stores taken by hand in the owner's browser
                                (the Shopify stores answer HTTP 429 to scripts): per card the cheapest
                                available variant for English, Spanish and, when neither exists, foil; per
                                store and card the newest file wins, so a short file adds cards to the earlier ones
and writes data/prices/merged-<UTC stamp>.json (same offer schema as the script) and
.summary.txt with per-store coverage, cards with no offer and the cheapest offer per card.

For a store present in both sources the browser file wins (it is the fresher, more complete one).
`available` is a price-phase hint: stock is verified in Phase 9.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import read_store_prices as rsp  # noqa: E402

OUT_DIR = rsp.OUT_DIR
BUCKET_FINISH_HINT = {"nen": "English", "nes": "Spanish", "f": "foil"}


def browser_offers(store, best, targets, fetched_at):
    """Offers from a browser reading: `best` maps a normalized card name to {bucket: [title, handle, variant, price]}."""
    out = []
    for key, buckets in best.items():
        if key not in targets:
            continue
        for _bucket, (title, handle, variant, price) in buckets.items():
            if rsp.ART_CARD_RE.search(title):
                continue
            language, condition, finish, inferred = rsp.classify(f"{title} {variant}")
            if language not in rsp.ACCEPTED_LANGUAGES or condition not in rsp.ACCEPTED_CONDITIONS:
                continue
            price = int(float(price))
            if price <= 0:
                continue
            out.append({
                "store": store["id"], "card": targets[key], "match": "exact", "set_hint": "",
                "language": language, "condition": condition, "finish": finish, "inferred": inferred,
                "price_clp": price, "available": True, "quantity": None, "title": title, "variant": variant,
                "url": f"{store['base']}/products/{handle}", "fetched_at": fetched_at, "source": "browser",
            })
    return out


def parse_psv(path, targets, store):
    """Offers from a browser reading saved as pipe-separated lines (see docs/research/phase7-handoff-2026-10-17.md).

    Header: `#STORE <id> fetched_at=<UTC> ... FORMAT ...`; lines: key|bucket|handle|variant|price|title_suffix.
    The title is rebuilt as the card name plus the suffix, then classified like any other offer."""
    best, fetched_at, products_seen = {}, "", None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("#STORE"):
            for token in raw.split():
                if token.startswith("fetched_at="):
                    fetched_at = token.split("=", 1)[1]
                if token.startswith("seen="):
                    products_seen = int(token.split("=", 1)[1])
            continue
        parts = raw.split("|")
        if len(parts) < 6:
            continue
        key, bucket, handle, variant, price = parts[:5]
        suffix = "|".join(parts[5:])
        if key not in targets:
            continue
        title = f"{targets[key]} {suffix}".strip()
        best.setdefault(key, {})[bucket] = [title, handle, variant, price]
    return browser_offers(store, best, targets, fetched_at or "unknown"), products_seen


def merge_script_runs(run_paths):
    """Offers and per-store stats from several script runs, oldest first: a later run replaces the offers of a
    card in a store only when that store was read without error in it, so each store keeps, per card, its newest
    good reading and a partial run (a few new cards) adds to the earlier ones."""
    offers, stats = [], {}
    for run in run_paths:
        data = json.loads(run.read_text(encoding="utf-8"))
        for sid, st in data.get("store_stats", {}).items():
            if "error" in st:
                stats.setdefault(sid, {"source": "script", "run": run.name, **st})
                continue
            fresh = [o for o in data["offers"] if o["store"] == sid]
            read_cards = {o["card"] for o in fresh}
            offers = [o for o in offers if o["store"] != sid or o["card"] not in read_cards]
            for offer in fresh:
                offer.setdefault("source", "script")
                offers.append(offer)
            stats[sid] = {"source": "script", "run": run.name, **st}
        print(f"Script run {run.name}: {len(data['offers'])} offers")
    return offers, stats


def merge_browser_files(paths, targets, store):
    """(offers, products_seen of the newest file) from the browser readings of one store, oldest first: a later
    file replaces the offers of the cards it has; the cards only an earlier file has keep that reading."""
    per_card, seen = {}, None
    for path in paths:
        got, seen_now = parse_psv(path, targets, store)
        fresh = {}
        for offer in got:
            fresh.setdefault(offer["card"], []).append(offer)
        per_card.update(fresh)
        seen = seen_now or seen
    return [o for offers in per_card.values() for o in offers], seen


def main():
    """Merge the newest script run with every browser reading and write the merged files."""
    targets = rsp.targets_from_repo()
    stores = {s["id"]: s for s in rsp.STORES}
    offers, stats = merge_script_runs(sorted(OUT_DIR.glob("2*.json")))
    if not offers:
        print("No script run found under data/prices/ (run scripts/read_store_prices.py first).")
    browser_files = {}
    for path in sorted(OUT_DIR.glob("browser-*.psv")):
        browser_files.setdefault(path.name.split("-")[1], []).append(path)  # sorted by name: oldest date first
    for sid, paths in browser_files.items():
        store = stores[sid]
        offers = [o for o in offers if o["store"] != sid]  # the browser readings replace the script's
        got, seen = merge_browser_files(paths, targets, store)
        offers += got
        stats[sid] = {"source": "browser", "file": paths[-1].name, "files": [p.name for p in paths],
                      "products_seen": seen, "offers": len(got)}
        print(f"Browser readings {', '.join(p.name for p in paths)}: {len(got)} offers")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    result = {"as_of_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "note": "Price-phase evidence only: `available` is a hint, stock is verified in Phase 9.",
              "cards_requested": sorted(targets.values()), "store_stats": stats, "offers": offers}
    (OUT_DIR / f"merged-{stamp}.json").write_text(json.dumps(result, indent=1, ensure_ascii=False),
                                                  encoding="utf-8")
    (OUT_DIR / f"merged-{stamp}.summary.txt").write_text(rsp.summarize(targets, offers, stats),
                                                         encoding="utf-8")
    print(f"Wrote data/prices/merged-{stamp}.json and .summary.txt ({len(offers)} offers)")


if __name__ == "__main__":
    main()
