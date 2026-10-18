#!/usr/bin/env python3
"""Phase 8, step 1: price every measured list and build the card pool for the deck-building step.

Run it with the "Run Python File" button (no arguments). No network. It reads the Scryfall and
Spellbook caches, the merged prices (data/prices/merged-*.json), the inventory
(data/cache/collection_inventory.json) and decks/candidates/, and writes under data/model/:
  candidate-costs.json / .md   one row per measured list (the 13 candidates and the owner's 2 lists):
                               Commander Salt power, Layer A result, cards owned, cards to buy, cost in CLP
                               (cheapest offer per card, owned copies free), cards with no stock, the shipping
                               the purchase would need, and the locked cards the list already holds
  pool-<slug>.json             per deck, every card the expert may use: the candidates' cards, the Upgrades
                               picks and the owner's own cards that fit the color identity, each with owned
                               copies, cheapest offer and number of stores with stock

Cost is a hint: stock and price are verified in Phase 9. Power is the site's score of that exact list;
a list changed in the next step has no power until it is scored on Commander Salt.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allocation_model as am  # noqa: E402
import layer_a as la  # noqa: E402

ROOT = la.ROOT
OUT_DIR = ROOT / "data" / "model"
SCORES = am.CANDIDATES_DIR / "scores.json"
OWNER_LISTS = {"toph-the-first-metalbender": ROOT / "data" / "raw" / "Toph.txt",
               "fire-lord-azula": ROOT / "data" / "raw" / "Azula.txt"}


def layer_a_row(path, slug, index, spellbook, hazards):
    """Layer A summary of one list file."""
    commanders, main_cards, bad = la.parse_decklist(path.read_text(encoding="utf-8-sig"))
    report, _ = la.analyze(commanders, main_cards, index, slug, spellbook, hazards,
                           la.TARGET_BRACKET.get(slug, la.DEFAULT_TARGET))
    if bad:
        report["reasons"].append(f"{len(bad)} unparsed lines")
    return {"floor": report["floor"], "ok": report["floor_ok_so_far"] and not bad,
            "game_changers": len(report["checks"]["game_changers"]["cards"]),
            "reasons": report["reasons"][:2]}


def money(clp):
    """CLP with thousands separators."""
    return f"{clp:,}".replace(",", ".")


def main():
    bulk = la.latest_bulk()
    if bulk is None or am.latest_merged() is None or not am.INVENTORY_PATH.exists():
        print("Missing the Scryfall bulk, the merged prices or the inventory (Phases 1 and 7 first).")
        sys.exit(2)
    print(f"Reading {bulk.name} ...", flush=True)
    cards = list(la.iter_cards(bulk))
    index = la.build_index(cards)
    spellbook = la.load_spellbook() if la.SPELLBOOK_SLIM.exists() else None
    hazards = la.load_hazards()
    offers, unresolved, merged_name, offers_as_of = am.load_offers(index)
    owned = am.load_owned()
    locked = am.read_locked(index)
    scores = json.loads(SCORES.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    rows, listings, identity = [], {}, {}
    sources = [(p.parent.name, p.name, p, scores["lists"].get(f"{p.parent.name}/{p.stem}", {}))
               for p in sorted(am.CANDIDATES_DIR.glob("*/*.txt"))]
    sources += [(slug, p.name, p, scores["owner_lists"][slug]) for slug, p in OWNER_LISTS.items() if p.exists()]
    for slug, fname, path, score in sources:
        listing = am.read_list(path.read_text(encoding="utf-8-sig"), index)
        if listing["commanders"]:
            commander = index_card(cards, listing["commanders"][0])
            identity[slug] = set(commander.get("color_identity") or [])
        priced = am.price_list(listing, owned, offers)  # each list priced on its own, owned copies all free
        gate = layer_a_row(path, slug, index, spellbook, hazards)
        held = [listing["names"][o] for o in locked if listing["cards"].get(o)]
        rows.append({"slug": slug, "file": fname, "owner_list": path.parent.name == "raw", **score,
                     "layer_a": gate, "cards": sum(listing["cards"].values()), "basics": priced["basics"],
                     "owned_n": len(priced["owned"]), "to_buy_n": len(priced["to_buy"]),
                     "cost_clp": priced["cost_clp"], "stores": priced["stores"],
                     "shipping_clp": am.shipping_clp(priced["stores"]), "no_stock": priced["no_stock"],
                     "unresolved": listing["unresolved"], "locked_held": held, "to_buy": priced["to_buy"]})
        listings[(slug, fname)] = listing

    for slug, ident in identity.items():
        pool = build_pool(slug, ident, listings, cards, index, owned, offers, locked)
        (OUT_DIR / f"pool-{slug}.json").write_text(json.dumps(pool, indent=1, ensure_ascii=False), encoding="utf-8")

    stamp = {"as_of_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "bulk_file": bulk.name,
             "merged_prices": merged_name, "prices_as_of": offers_as_of, "scoring_version": scores["scoring_version"],
             "offer_cards_not_in_bulk": unresolved}
    (OUT_DIR / "candidate-costs.json").write_text(json.dumps({**stamp, "lists": rows}, indent=1, ensure_ascii=False),
                                                  encoding="utf-8")
    (OUT_DIR / "candidate-costs.md").write_text(render_table(rows, stamp), encoding="utf-8")
    print(f"Wrote {OUT_DIR}/candidate-costs.json, .md and {len(identity)} pool files")


def index_card(cards, oid):
    """The Scryfall card object of an oracle ID."""
    for card in cards:
        if card.get("oracle_id") == oid:
            return card
    return {}


def build_pool(slug, identity, listings, cards, index, owned, offers, locked):
    """Every card the expert may use for one deck, with owned copies, cheapest offer and stores with stock."""
    members = {}
    for (lslug, fname), listing in listings.items():
        if lslug != slug:
            continue
        for oid in listing["names"]:
            members.setdefault(oid, {"lists": []})["lists"].append(fname.removesuffix(".txt"))
    meta_path = am.CANDIDATES_DIR / slug / "meta-staples-bracket3.md"
    if meta_path.exists():
        for oid, _, pct in am.read_meta_picks(meta_path.read_text(encoding="utf-8"), index):
            members.setdefault(oid, {"lists": []})["meta_pct"] = pct
    by_oid = {c.get("oracle_id"): c for c in cards}
    for oid in owned:
        card = by_oid.get(oid)
        if card and am.fits_identity(card, identity):
            members.setdefault(oid, {"lists": []})["owned_fit"] = True
    out = []
    for oid, info in members.items():
        card = by_oid.get(oid)
        if card is None or not am.fits_identity(card, identity):
            continue
        if (card.get("legalities") or {}).get("commander") != "legal":
            continue
        best = am.best_offer(offers.get(oid, []))
        out.append({"name": card["name"], "oracle_id": oid, "type": card.get("type_line"), "cmc": card.get("cmc"),
                    "game_changer": bool(card.get("game_changer")), "locked": oid in locked,
                    "owned_usable": owned.get(oid, {}).get("usable", 0), "basic": am.is_basic(card["name"]),
                    "best_offer": ({"clp": best["price_clp"], "store": best["store"], "language": best["language"],
                                    "finish": best["finish"]} if best else None),
                    "stores_with_stock": len({o["store"] for o in offers.get(oid, [])}),
                    **{k: v for k, v in info.items() if k != "lists" or v}})
    out.sort(key=lambda c: c["name"])
    return {"slug": slug, "color_identity": sorted(identity), "cards": out}


def render_table(rows, stamp):
    """The markdown summary: one table per commander."""
    lines = ["# Candidate costs (Phase 8, step 1)", "",
             f"Generated {stamp['as_of_utc']} from prices `{stamp['merged_prices']}` (read {stamp['prices_as_of']}), "
             f"bulk `{stamp['bulk_file']}`, Commander Salt scoring {stamp['scoring_version']}. Cost = cheapest offer per "
             "card for the cards the owner does not have (owned copies free, each list priced on its own, so cards "
             "shared by two decks are counted in both); shipping is 5,000 CLP per store, outside the cost. "
             "Prices are a hint: stock is verified in Phase 9.", ""]
    for slug in dict.fromkeys(r["slug"] for r in rows):
        lines += [f"## {slug}", "", "| List | Power | Layer A | Owned | To buy | Cost CLP | Stores | No stock | Locked held |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for r in (x for x in rows if x["slug"] == slug):
            gate = r["layer_a"]
            label = ("OK" if gate["ok"] else "NO") + f" (floor {gate['floor']})"
            name = "owner's list" if r["owner_list"] else r["file"].removesuffix(".txt")
            lines.append(f"| {name} | {r.get('power', '?')} | {label} | {r['owned_n']} | {r['to_buy_n']} | "
                         f"{money(r['cost_clp'])} | {len(r['stores'])} | {len(r['no_stock'])} | "
                         f"{len(r['locked_held'])} |")
        lines.append("")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
