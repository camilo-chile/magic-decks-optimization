#!/usr/bin/env python3
"""Phase 9 step 1: the buy list of one budget plan, with the offers that could fill it. No network, writes two files.

Run it with the "Run Python File" button (no arguments: the plan of 150,000 CLP, the budget the owner picked on 2026-10-19)
or pass a budget: `python scripts/plan_buylist.py 200000`. It reads the plan of that budget in `data/model/budget-curve.json`
(written by `scripts/optimize_budget.py`), the exact lists in `decks/measured/`, the newest merged prices and the owned
inventory, and prices the three lists together: every owned copy is used once, so a card two decks play is bought again for
the second deck. For each card to buy it keeps the quantity, the decks that need it and up to four offers (cheapest first, at
most one per store): store, price, language, finish, the stock quantity the price reading saw, the URL and the reading time.

Writes data/model/buylist-<budget>.json and decks/reports/buylist-<budget>.md (the cards by store, the total, the assumed
shipping, the cards with a single source or a thin stock). The stock here is a hint of the price reading, never evidence:
the stock check of Phase 9 reads the stores again, and Phase 11 repeats it within 24 hours of the purchase.
"""
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allocation_model as am  # noqa: E402
import layer_a as la  # noqa: E402
import read_store_prices as rsp  # noqa: E402

ROOT = la.ROOT
CURVE = ROOT / "data" / "model" / "budget-curve.json"
LISTS_DIR = ROOT / "decks" / "measured"
DEFAULT_BUDGET = 150_000
OFFERS_KEPT = 4
STALE_HOURS = 24
SHORT = {"ezio-auditore-da-firenze": "Ezio", "fire-lord-azula": "Azula", "toph-the-first-metalbender": "Toph"}


def aggregate(priced_by_deck):
    """{card name: {"qty", "decks": {deck: qty}, "price_clp"...}} from the per-deck `to_buy` lists of `am.price_list`."""
    cards = {}
    for deck, priced in priced_by_deck.items():
        for buy in priced["to_buy"]:
            entry = cards.setdefault(buy["name"], {"name": buy["name"], "qty": 0, "decks": {}})
            entry["qty"] += buy["qty"]
            entry["decks"][deck] = entry["decks"].get(deck, 0) + buy["qty"]
    return cards


def is_stale(read_at, as_of, hours=STALE_HOURS):
    """True when the offer was read more than `hours` before the price reading's own time (`as_of`): the merge keeps the
    newest reading per store and card, so an offer can be days old (the Camera of Ezio's list was 2 days old, and sold out)."""
    if not read_at or not as_of:
        return True
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    return (datetime.strptime(as_of, fmt) - datetime.strptime(read_at, fmt)).total_seconds() > hours * 3600


def offer_view(offer):
    return {"store": offer["store"], "price_clp": offer["price_clp"], "language": offer["language"], "finish": offer["finish"],
            "condition": offer.get("condition"), "stock_hint": offer.get("quantity"), "title": offer.get("title"),
            "url": offer.get("url"), "variant": offer.get("variant"), "read_at": offer.get("fetched_at")}


def offers_for(offers, kept=OFFERS_KEPT):
    """The cheapest offers, at most one per store, best first (the Spanish copy wins a tie)."""
    seen, out = set(), []
    for offer in sorted(offers, key=rsp.offer_rank):
        if offer["store"] in seen:
            continue
        seen.add(offer["store"])
        out.append(offer_view(offer))
        if len(out) == kept:
            break
    return out


def build(budget):
    curve = json.loads(CURVE.read_text(encoding="utf-8"))
    row = next((r for r in curve["curve"] if r["budget"] == budget and r.get("decks")), None)
    if row is None:
        sys.exit(f"No plan for {budget:,} CLP in {CURVE.relative_to(ROOT)}: run scripts/optimize_budget.py first.")
    index = la.build_index(list(la.iter_cards(la.latest_bulk())))
    offers_by_oid, _, merged_name, as_of = am.load_offers(index)
    owned = am.load_owned()
    claimed, priced_by_deck, listings = Counter(), {}, {}
    for deck, point in sorted(row["decks"].items()):
        path = LISTS_DIR / deck / f"{point['label']}.txt"
        listing = am.read_list(path.read_text(encoding="utf-8-sig"), index)
        listings[deck] = listing
        priced_by_deck[SHORT[deck]] = am.price_list(listing, owned, offers_by_oid, claimed)
    cards = aggregate(priced_by_deck)
    oid_by_name = {name: oid for listing in listings.values() for oid, name in listing["names"].items()}
    for name, card in cards.items():
        card["offers"] = offers_for(offers_by_oid.get(oid_by_name[name], []))
        cheapest = card["offers"][0]
        card["unit_clp"], card["line_clp"] = cheapest["price_clp"], cheapest["price_clp"] * card["qty"]
        card["single_source"] = len(card["offers"]) == 1
        card["thin_stock"] = any(isinstance(o["stock_hint"], int) and o["stock_hint"] < card["qty"] for o in card["offers"][:1])
        card["stale"] = is_stale(cheapest.get("read_at"), as_of)
    no_stock = sorted(n for p in priced_by_deck.values() for n in p["no_stock"])
    total = sum(c["line_clp"] for c in cards.values())
    stores = {}
    for card in cards.values():
        entry = stores.setdefault(card["offers"][0]["store"], {"cards": 0, "subtotal_clp": 0})
        entry["cards"] += 1
        entry["subtotal_clp"] += card["line_clp"]
    return {"budget": budget, "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "prices": merged_name,
            "prices_as_of": as_of, "lists": {SHORT[d]: p["label"] for d, p in row["decks"].items()},
            "plan_total_clp": row["cost"], "total_clp": total, "cards": sorted(cards.values(), key=lambda c: -c["line_clp"]),
            "no_stock": no_stock, "stores": stores, "shipping_clp": am.shipping_clp(stores), "owned_used": {
                d: len(p["owned"]) for d, p in priced_by_deck.items()}}


def render(plan):
    lines = [f"# Buy list of the {plan['budget']:,} CLP plan", "",
             f"Built {plan['built_at']} by `scripts/plan_buylist.py` from `{plan['prices']}` (prices read {plan['prices_as_of']}). "
             "Lists: " + ", ".join(f"{d} {label}" for d, label in plan["lists"].items()) + ". The three lists together, every owned "
             "copy used once; the stock is the price reading's hint, not evidence (Phase 9 reads the stores again).", "",
             f"Cards to buy: {len(plan['cards'])}; cheapest-offer total {plan['total_clp']:,} CLP (plan total "
             f"{plan['plan_total_clp']:,}); stores {len(plan['stores'])}, assumed shipping {plan['shipping_clp']:,} CLP (outside the budget).",
             ""]
    if plan["no_stock"]:
        lines += [f"**No stock anywhere:** {', '.join(plan['no_stock'])}", ""]
    lines += ["| Store | Cards | Subtotal CLP |", "|---|---|---|"]
    lines += [f"| {s} | {v['cards']} | {v['subtotal_clp']:,} |" for s, v in sorted(plan["stores"].items(), key=lambda kv: -kv[1]["subtotal_clp"])]
    lines += ["", "| Card | Qty | Decks | Cheapest | Other offers | Risk |", "|---|---|---|---|---|---|"]
    for c in plan["cards"]:
        first, rest = c["offers"][0], c["offers"][1:]
        risk = ", ".join(r for r, on in (("single source", c["single_source"]), ("thin stock", c["thin_stock"]),
                                         ("reading over 24 h old", c["stale"])) if on) or "-"
        others = "; ".join(f"{o['store']} {o['price_clp']:,} ({o['language']})" for o in rest) or "-"
        lines.append(f"| {c['name']} | {c['qty']} | {'+'.join(sorted(c['decks']))} | {first['store']} {first['price_clp']:,} "
                     f"({first['language']}, stock {first['stock_hint']}) | {others} | {risk} |")
    return "\n".join(lines) + "\n"


def main(argv):
    budget = int(argv[0]) if argv else DEFAULT_BUDGET
    plan = build(budget)
    out_json = ROOT / "data" / "model" / f"buylist-{budget}.json"
    out_md = ROOT / "decks" / "reports" / f"buylist-{budget}.md"
    out_json.write_text(json.dumps(plan, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    out_md.write_text(render(plan), encoding="utf-8")
    print(render(plan))
    print(f"Wrote {out_json.relative_to(ROOT)} and {out_md.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
