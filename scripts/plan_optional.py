#!/usr/bin/env python3
"""Phase 11 step 1 (optional items, outside the budget): the real Ezio commander card and the tokens the final decks create that the
owner lacks, in the stores of the purchase plan only. Network, read-only, slow on purpose (one request per 2.5 s per Shopify store).

Run it with the "Run Python File" button (no arguments: the 200,000 CLP plan) or pass a budget. It follows the rule of CLAUDE.md
(owner, 2026-10-16; the owner asked for the step to be done at once on 2026-10-19): survey the existing token data first (Scryfall's own
card-to-token relations, `all_parts`, are the existing list: nothing is rebuilt), list the tokens the three final lists create, take
away the ones the owner holds (the "Tokens" binder of the newest collection export, by name), and look up only the gap in the stores of
the plan (never a new store). Each item is offered, never added by itself: `scripts/plan_purchase.py` shows them as an optional section.

Writes data/model/optional-<budget>.json (items, candidates seen, token facts). Stock is read from the stores' product lists
(availability and price); the owner sees the quantity in the cart.
"""
import csv
import gzip
import json
import re
import sys
import threading
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402
import read_store_prices as rsp  # noqa: E402

ROOT = la.ROOT
COLLECTION_DIR = ROOT / "data" / "collection"
LISTS = {"Toph": "toph-the-first-metalbender", "Azula": "fire-lord-azula", "Ezio": "ezio-auditore-da-firenze"}
STORES = ("paytowin", "gameofmagic", "lacomarca", "magic4ever", "oasis", "cardnexus")
KINDS = {s["id"]: s for s in rsp.STORES}
SHOPIFY_INTERVAL_S = 2.5
UA = rsp.USER_AGENT
LANGS = {"en", "es"}


def final_lists(budget):
    """{deck: path of its list in the plan} from data/model/budget-curve.json."""
    curve = json.loads((ROOT / "data" / "model" / "budget-curve.json").read_text(encoding="utf-8"))["curve"]
    row = next(r for r in curve if r["budget"] == budget and r.get("decks"))
    return {short: ROOT / "decks" / "measured" / slug / f"{row['decks'][slug]['label']}.txt" for short, slug in LISTS.items()}


def tokens_of(paths):
    """{(token name, type line): {"cards": [...], "id": scryfall id of the token}} from Scryfall's all_parts of every card of the lists."""
    names = {}
    for deck, path in paths.items():
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^(\d+)\s+(.+?)\s*$", line.strip())
            if match:
                names.setdefault(match.group(2).split(" // ")[0].lower(), set()).add(deck)
    bulk = sorted((ROOT / "data" / "cache").glob("oracle-cards-*.jsonl.gz"))[-1]
    found = {}
    with gzip.open(bulk, "rt", encoding="utf-8") as handle:
        for line in handle:
            obj = json.loads(line)
            key = obj["name"].split(" // ")[0].lower()
            if key in names and obj.get("layout") not in ("art_series", "token", "double_faced_token", "emblem"):
                found.setdefault(key, obj)
    tokens = defaultdict(lambda: {"cards": [], "id": None})
    for key, card in found.items():
        for part in card.get("all_parts") or []:
            if part.get("component") == "token":
                entry = tokens[(part["name"], part["type_line"])]
                entry["cards"].append(f"{card['name']} ({'+'.join(sorted(names[key]))})")
                entry["id"] = entry["id"] or part["id"]
    return dict(tokens)


def owned_tokens():
    """{lower token name: copies} of the Tokens binder of the newest collection export."""
    newest = sorted(COLLECTION_DIR.glob("ManaBox_Collection_*.csv"))[-1]
    owned = defaultdict(int)
    for row in csv.DictReader(open(newest, encoding="utf-8-sig")):
        if row["Binder Name"].lower().startswith("token"):
            owned[row["Name"].split(" // ")[0].lower()] += int(row["Quantity"])
    return dict(owned)


def token_facts(requests, token_id):
    """P/T, colors and rules of the exact token Scryfall relates to the cards (one API request)."""
    data = requests.get(f"https://api.scryfall.com/cards/{token_id}", headers={"User-Agent": UA, "Accept": "application/json"}, timeout=30).json()
    time.sleep(0.15)
    pt = f"{data.get('power')}/{data.get('toughness')}" if data.get("power") is not None else ""
    colors = "".join(data.get("colors") or []) or "colorless"
    return " ".join(x for x in (pt, colors, (data.get("oracle_text") or "").replace("\n", " ")) if x)


def wanted(title, name, token):
    """True when a store title is the card we look for: the name as a word, and `token` for a token."""
    norm = title.lower()
    if not token:
        return norm.startswith(name.lower())
    if re.search(r"chinese|japanese|french|german|italian|portuguese|korean|russian|phyrexian|japon|franc|alem", norm):
        return False  # other languages are never bought
    # the token's own name first ("Beast Token [..]", "Treasure // Clue Double-Sided Token [..]"), not "Human Citizen" nor a set name
    return "token" in norm and re.match(r"^(?:spanish\s+)?" + re.escape(name.lower()) + r"\s*(?:token\b|//|\[|\()", norm) is not None


def search_shopify(requests, throttle, base, query):
    """[{title, price_clp, available, url}] of a Shopify store's suggest results."""
    throttle.wait()
    resp = requests.get(base + "/search/suggest.json", params={"q": query, "resources[type]": "product", "resources[limit]": 10},
                        headers={"User-Agent": UA}, timeout=30)
    if resp.status_code == 429:
        time.sleep(int(resp.headers.get("Retry-After") or 30))
        return search_shopify(requests, throttle, base, query)
    products = (resp.json().get("resources", {}).get("results", {}) or {}).get("products", []) if resp.status_code == 200 else []
    return [{"title": p["title"], "price_clp": int(float(p["price"])), "available": bool(p["available"]),
             "url": base + p["url"].split("?")[0]} for p in products]


def search_store(requests, store, query, token):
    """Candidates of one store for one query: [{title, price_clp, available, stock_shown, url}]."""
    kind, base = KINDS[store]["kind"], KINDS[store]["base"]
    if kind == "shopify":
        return [dict(c, stock_shown=None) for c in search_shopify(requests, THROTTLES[store], base, query)]
    THROTTLES[store].wait()
    if kind == "woocommerce":
        data = requests.get(f"{base}/wp-json/wc/store/v1/products", params={"search": query, "per_page": 20}, headers={"User-Agent": UA}, timeout=30).json()
        out = []
        for p in data:
            prices = p.get("prices") or {}
            text = (p.get("stock_availability") or {}).get("text") or ""
            qty = re.search(r"(\d+)\s+disponible", text)
            out.append({"title": p["name"], "price_clp": int(prices.get("price") or 0) // (10 ** int(prices.get("currency_minor_unit") or 0)),
                        "available": bool(p.get("is_in_stock")) and bool(p.get("is_purchasable")), "stock_shown": int(qty.group(1)) if qty else None,
                        "url": p.get("permalink")})
        return out
    data = requests.get(KINDS[store]["api"], params={"q": query, "limit": 40, "offset": 0, "withVariants": 1}, headers={"User-Agent": UA}, timeout=30).json()
    out = []
    for card in data.get("cards") or []:
        for v in card.get("variants") or []:
            if int(v.get("stock") or 0) > 0 and (v.get("language") or "").lower() in LANGS:
                out.append({"title": card["name"], "price_clp": int(v.get("priceClp") or 0), "available": True, "stock_shown": int(v["stock"]),
                            "url": v.get("productUrl") or card.get("productUrl")})
    return out


THROTTLES = {}


def look_up(requests, store, query, name, token):
    """The cheapest available candidate of one store for one item, with every title seen (for the owner's eyes)."""
    try:
        seen = search_store(requests, store, query, token)
    except Exception as exc:  # noqa: BLE001 - one failed search must not stop the others
        return {"store": store, "error": f"{type(exc).__name__}: {exc}"[:120], "best": None, "seen": []}
    good = sorted((c for c in seen if wanted(c["title"], name, token) and c["available"] and c["price_clp"] > 0), key=lambda c: c["price_clp"])
    return {"store": store, "best": good[0] if good else None, "seen": [c["title"] for c in seen if wanted(c["title"], name, token)][:4]}


def main(argv):
    import requests
    budget = int(argv[0]) if argv else 200_000
    tokens = tokens_of(final_lists(budget))
    owned = owned_tokens()
    gap = {key: v for key, v in tokens.items() if key[0].lower() not in owned}
    have = sorted(key[0] for key in tokens if key[0].lower() in owned)
    print(f"{len(tokens)} token kinds created; owned by name: {have}; gap: {sorted(k[0] for k in gap)}", flush=True)
    for key, entry in gap.items():
        entry["facts"] = token_facts(requests, entry["id"])
    for store in STORES:
        THROTTLES[store] = rsp.Throttle(SHOPIFY_INTERVAL_S if KINDS[store]["kind"] == "shopify" else rsp.MIN_INTERVAL_S)
    jobs = [("Ezio Auditore da Firenze", "Ezio Auditore da Firenze", False)] + [(f"{name} token", name, True) for (name, _), _ in gap.items()]

    def run_store(store):
        return [(item, look_up(requests, store, query, name, token)) for item, (query, name, token) in ((j[1], j) for j in jobs)]

    with ThreadPoolExecutor(max_workers=len(STORES)) as pool:
        per_store = list(pool.map(run_store, STORES))
    items, candidates = [], defaultdict(list)
    for results in per_store:
        for item, res in results:
            candidates[item].append(res)
            if res["best"]:
                best = res["best"]
                items.append({"store": res["store"], "name": item if item.startswith("Ezio") else f"{item} (token)", "qty": 1, "unit_clp": best["price_clp"],
                              "stock_shown": best["stock_shown"], "title": best["title"], "url": best["url"], "note": best["title"]})
    notes = [f"Tokens the three lists create that you already own: {', '.join(have) or 'none'}. Missing: "
             + "; ".join(f"{k[0]} ({v['facts']}; made by {', '.join(v['cards'][:3])})" for k, v in sorted(gap.items())) + "."]
    out = ROOT / "data" / "model" / f"optional-{budget}.json"
    out.write_text(json.dumps({"budget": budget, "items": items, "candidates": candidates, "notes": notes}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    cheapest = defaultdict(list)
    for it in items:
        cheapest[it["name"]].append((it["unit_clp"], it["store"], it["title"]))
    for name, offers in sorted(cheapest.items()):
        print(name, sorted(offers)[:3])
    print("without stock in the plan stores:", sorted(set(k for (n, _), _ in gap.items() for k in [f"{n} (token)"]) - set(cheapest) | ({"Ezio Auditore da Firenze"} - set(cheapest))))
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
