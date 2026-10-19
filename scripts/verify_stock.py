#!/usr/bin/env python3
"""Phase 9 step 2: live stock check of the offers in a buy list. Network, read-only.

Run it with the "Run Python File" button (no arguments: the buy list of the 150,000 CLP plan) or pass a budget:
`python scripts/verify_stock.py 200000`. It reads `data/model/buylist-<budget>.json` (from `scripts/plan_buylist.py`) and, for
every card, asks each of its top offers' store for the raw data of that one product page, one request at a time per store
(at most one per second to the same host, a clear User-Agent, no sign-in, no cart, no form):

  Shopify stores        <product url>.js  (variants with price in cents and `available`)
  CardNexus (WooCommerce) /wp-json/wc/store/v1/products?slug=<slug>  (`is_in_stock`, price, "N disponibles")
  Magic4Ever            its public search API, the variant with the offer's SKU (stock and price)

Evidence per offer: what the store answered now (UTC time), the live price, the stock quantity when the store shows one
(only CardNexus and Magic4Ever do; Shopify says only available or not), and a status: `in_stock`, `out_of_stock`,
`variant_not_found`, `error`. The verdict per card needs the copies the plan buys: `verified` when an offer is in stock and its
quantity (when shown) covers them, `quantity_unverified` when it is in stock but the store does not show how many and the plan
needs more than one, `no_stock` when none is in stock. A live price more than 5 % above the price the plan used is flagged
(the skill's rule: a price that moved more than 5 % triggers re-optimization).

Writes data/stock/<YYYYMMDDTHHMMZ>.json (every record) and decks/reports/stock-<budget>-<stamp>.md. Stock is perishable: the
purchase needs a check within 24 hours (Phase 11).
"""
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402
import read_store_prices as rsp  # noqa: E402

ROOT = la.ROOT
DEFAULT_BUDGET = 150_000
OFFERS_CHECKED = 3  # the cheapest three offers of each card (one per store)
PRICE_DRIFT = 0.05
KINDS = {s["id"]: s for s in rsp.STORES}


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def record(card, offer, status, **extra):
    base = {"card": card, "store": offer["store"], "url": offer["url"], "title": offer.get("title"), "variant": offer.get("variant"),
            "language": offer["language"], "condition": offer.get("condition"), "finish": offer["finish"],
            "plan_price_clp": offer["price_clp"], "status": status, "checked_at": now_utc(),
            "price_clp": None, "quantity": None, "evidence": ""}
    base.update(extra)
    return base


def shopify_status(card, offer, product):
    """The record of a Shopify product (`.js` JSON): the variant is the one the offer names by its title."""
    variant = next((v for v in product.get("variants", []) if v.get("title") == offer.get("variant")), None)
    if variant is None:
        return record(card, offer, "variant_not_found", evidence=f"variants: {[v.get('title') for v in product.get('variants', [])][:6]}")
    price = int(variant["price"]) // 100
    return record(card, offer, "in_stock" if variant.get("available") else "out_of_stock", price_clp=price,
                  evidence=f"Shopify product JSON: variant '{variant['title']}' available={variant.get('available')}, price {price:,}")


def woo_status(card, offer, products):
    if not products:
        return record(card, offer, "variant_not_found", evidence="Store API returned no product for the slug")
    product = products[0]
    prices = product.get("prices") or {}
    price = int(prices.get("price") or 0) // (10 ** int(prices.get("currency_minor_unit") or 0))
    text = (product.get("stock_availability") or {}).get("text") or ""
    qty = re.search(r"(\d+)\s+disponible", text)
    in_stock = bool(product.get("is_in_stock")) and bool(product.get("is_purchasable"))
    return record(card, offer, "in_stock" if in_stock else "out_of_stock", price_clp=price, quantity=int(qty.group(1)) if qty else None,
                  evidence=f"WooCommerce Store API: is_in_stock={product.get('is_in_stock')}, is_purchasable={product.get('is_purchasable')}, "
                           f"'{text}', price {price:,}")


def magic4ever_status(card, offer, cards):
    for found in cards:
        for variant in found.get("variants") or []:
            if variant.get("sku") == offer.get("variant"):
                stock = int(variant.get("stock") or 0)
                price = int(variant.get("priceClp") or 0)
                return record(card, offer, "in_stock" if stock > 0 else "out_of_stock", price_clp=price, quantity=stock,
                              evidence=f"Magic4Ever API: SKU {variant['sku']} stock {stock}, price {price:,}")
    return record(card, offer, "variant_not_found", evidence=f"SKU {offer.get('variant')} not in the search answer")


def check_offer(requests, throttle, card, offer):
    """One offer's record; a network or format problem is an `error` record, never an exception."""
    kind = KINDS[offer["store"]]["kind"]
    try:
        if kind == "shopify":
            data, _ = rsp.get_json(requests, throttle, offer["url"] + ".js")
            return shopify_status(card, offer, data)
        if kind == "woocommerce":
            slug = urlparse(offer["url"]).path.strip("/").split("/")[-1]
            data, _ = rsp.get_json(requests, throttle, f"{KINDS[offer['store']]['base']}/wp-json/wc/store/v1/products", {"slug": slug})
            return woo_status(card, offer, data)
        name = re.sub(r"\s*\([^)]*\)\s*$", "", offer.get("title") or card)
        data, _ = rsp.get_json(requests, throttle, KINDS[offer["store"]]["api"], {"q": name, "limit": 100, "offset": 0, "withVariants": 1})
        return magic4ever_status(card, offer, data.get("cards") or [])
    except Exception as exc:  # noqa: BLE001 - a failed request must not stop the other checks
        return record(card, offer, "error", evidence=f"{type(exc).__name__}: {exc}"[:200])


def verdict(qty_needed, records):
    """verified / quantity_unverified / no_stock for one card from its offer records."""
    live = [r for r in records if r["status"] == "in_stock"]
    if not live:
        return "no_stock"
    if any(r["quantity"] is None and qty_needed == 1 or r["quantity"] is not None and r["quantity"] >= qty_needed for r in live):
        return "verified"
    return "quantity_unverified"


def drifted(rec):
    return rec["price_clp"] is not None and rec["price_clp"] > rec["plan_price_clp"] * (1 + PRICE_DRIFT)


def render(budget, stamp, plan, results):
    lines = [f"# Stock check of the {budget:,} CLP plan ({stamp})", "",
             f"Read live by `scripts/verify_stock.py` from each store's own product data (the cheapest {OFFERS_CHECKED} offers of every card of "
             f"`data/model/buylist-{budget}.json`, built from `{plan['prices']}`). Stock is perishable: Phase 11 repeats the check within "
             "24 hours of the purchase.", ""]
    counts = {}
    for card in results:
        counts[card["verdict"]] = counts.get(card["verdict"], 0) + 1
    lines.append("Cards: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + f" (of {len(results)}).")
    errors = sum(1 for c in results for r in c["records"] if r["status"] == "error")
    moved = [(c["name"], r) for c in results for r in c["records"] if drifted(r) and r["status"] == "in_stock"]
    lines += [f"Offers read: {sum(len(c['records']) for c in results)}; errors {errors}; live prices more than 5 % above the plan's: {len(moved)}.", ""]
    bad = [c for c in results if c["verdict"] != "verified"]
    if bad:
        lines += ["## Cards that need attention", "", "| Card | Qty | Verdict | Offers (store: status, live price, quantity) |", "|---|---|---|---|"]
        for c in bad:
            offers = "; ".join(f"{r['store']}: {r['status']}, {r['price_clp'] if r['price_clp'] is not None else '-'}, "
                               f"{r['quantity'] if r['quantity'] is not None else '?'}" for r in c["records"])
            lines.append(f"| {c['name']} | {c['qty']} | {c['verdict']} | {offers} |")
        lines.append("")
    if moved:
        lines += ["## Prices that moved more than 5 %", "", "| Card | Store | Plan | Live |", "|---|---|---|---|"]
        lines += [f"| {n} | {r['store']} | {r['plan_price_clp']:,} | {r['price_clp']:,} |" for n, r in moved]
        lines.append("")
    lines += ["## Every card", "", "| Card | Qty | Verdict | In stock at (live price) |", "|---|---|---|---|"]
    for c in results:
        live = "; ".join(f"{r['store']} {r['price_clp']:,}" + (f" (x{r['quantity']})" if r["quantity"] is not None else "")
                         for r in c["records"] if r["status"] == "in_stock")
        lines.append(f"| {c['name']} | {c['qty']} | {c['verdict']} | {live or '-'} |")
    return "\n".join(lines) + "\n"


def main(argv):
    import requests
    budget = int(argv[0]) if argv else DEFAULT_BUDGET
    plan_path = ROOT / "data" / "model" / f"buylist-{budget}.json"
    if not plan_path.exists():
        sys.exit(f"{plan_path.relative_to(ROOT)} is missing: run scripts/plan_buylist.py {budget} first.")
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    jobs = {}  # store -> [(card, offer)]
    for card in plan["cards"]:
        for offer in card["offers"][:OFFERS_CHECKED]:
            jobs.setdefault(offer["store"], []).append((card["name"], offer))
    total = sum(len(v) for v in jobs.values())
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    print(f"{total} offers of {len(plan['cards'])} cards in {len(jobs)} stores; one request per second per store.", flush=True)
    started = time.time()

    def run_store(store):
        throttle = rsp.Throttle()
        out = []
        for i, (card, offer) in enumerate(jobs[store], 1):
            out.append(check_offer(requests, throttle, card, offer))
            if i % 10 == 0 or i == len(jobs[store]):
                print(f"  {store}: {i}/{len(jobs[store])} ({time.time() - started:.0f} s)", flush=True)
        return out

    with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
        records = [r for part in pool.map(run_store, sorted(jobs)) for r in part]
    by_card = {}
    for rec in records:
        by_card.setdefault(rec["card"], []).append(rec)
    results = []
    for card in plan["cards"]:
        recs = sorted(by_card.get(card["name"], []), key=lambda r: r["plan_price_clp"])
        results.append({"name": card["name"], "qty": card["qty"], "decks": card["decks"], "verdict": verdict(card["qty"], recs), "records": recs})
    out_json = ROOT / "data" / "stock" / f"{stamp}.json"
    out_md = ROOT / "decks" / "reports" / f"stock-{budget}-{stamp}.md"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps({"budget": budget, "checked_at": now_utc(), "buylist": plan_path.name, "prices": plan["prices"],
                                    "cards": results}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    out_md.write_text(render(budget, stamp, plan, results), encoding="utf-8")
    print(render(budget, stamp, plan, results))
    print(f"Wrote {out_json.relative_to(ROOT)} and {out_md.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
