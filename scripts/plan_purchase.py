#!/usr/bin/env python3
"""Phase 10 step 2: the purchase order of a plan, riskiest cards first. No network, writes one report.

Run it with the "Run Python File" button (no arguments: the newest stock check in data/stock/ and the stores the owner chose on
2026-10-19) or pass them: `python scripts/plan_purchase.py data/stock/20261019T1542Z.json cardnexus,gameofmagic,...`.

Owner rules (2026-10-19): stock comes first, every extra store is one more order that can fail, and the order of the purchase matters:
the cards with low stock or in a single store are secured first. So every card is bought where the stock check saw it in stock at the
lowest live price among the chosen stores (an offer whose shown quantity is below the copies needed does not count), and classified:

  A (secure first)  no second store inside the chosen set, or the store's shown quantity is no more than the copies needed (one other
                    buyer empties it), or the plan needs more than one copy and the store does not show its quantity
  B                 two or more stores inside the set and a comfortable quantity

The stores are ordered by the weight of their cards at risk, heaviest first. A card with no second store weighs 10 plus its value in
thousands of CLP (a failure there means re-planning); a card with a fallback weighs 1 (thin stock) or 2 (quantity not shown) plus the
price difference of the fallback in thousands of CLP (what a failure would cost). Inside a store the A cards come first. Use: put the A cards of every store in its cart first (a cart shows quantity limits without paying), and only
when every cart holds what the plan needs, pay in this order. A failed card has its fallback store (inside the set) with the price
difference; with no fallback the plan is re-optimized before anything else is paid.

Writes decks/reports/purchase-order-<budget>.md.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allocation_model as am  # noqa: E402
import layer_a as la  # noqa: E402

ROOT = la.ROOT
STOCK_DIR = ROOT / "data" / "stock"
DEFAULT_STORES = ("cardnexus", "gameofmagic", "lacomarca", "magic4ever", "oasis", "paytowin")
WEIGHT = {"thin stock": 1, "quantity not shown": 2}  # a card with no second store weighs 10, see risk_weight


def rows_for(stock, stores):
    """[{card, qty, store, unit, fallback, reasons, stock_shown}] for every card with an offer in the chosen stores, and the
    cards with none."""
    rows, uncovered = [], []
    for card in stock["cards"]:
        options = sorted(((r["price_clp"], r["store"], r["quantity"]) for r in card["records"]
                          if r["status"] == "in_stock" and r["price_clp"] is not None and r["store"] in stores
                          and (r["quantity"] is None or r["quantity"] >= card["qty"])), key=lambda o: (o[0], o[1]))
        if not options:
            uncovered.append(card["name"])
            continue
        (price, store, shown), others = options[0], options[1:]
        reasons = []
        if not others:
            reasons.append("single source")
        if shown is not None and shown <= card["qty"]:
            reasons.append("thin stock")
        if card["qty"] > 1 and shown is None:
            reasons.append("quantity not shown")
        rows.append({"card": card["name"], "qty": card["qty"], "decks": "+".join(sorted(card["decks"])), "store": store, "unit": price,
                     "stock_shown": shown, "fallback": {"store": others[0][1], "unit": others[0][0]} if others else None,
                     "reasons": reasons})
    return rows, uncovered


def risk_weight(row):
    """How much a failure of this card would hurt: 0 for a B card."""
    if not row["reasons"]:
        return 0.0
    if row["fallback"] is None:
        return 10 + row["unit"] * row["qty"] / 1000
    delta = max((row["fallback"]["unit"] - row["unit"]) * row["qty"], 0)
    return sum(WEIGHT.get(x, 0) for x in row["reasons"]) + delta / 1000


def store_order(rows):
    """The stores, heaviest risk first (ties: the dearer store first, it has more to lose)."""
    weight, value = {}, {}
    for r in rows:
        weight[r["store"]] = weight.get(r["store"], 0) + risk_weight(r)
        value[r["store"]] = value.get(r["store"], 0) + r["unit"] * r["qty"]
    return sorted(weight, key=lambda s: (-weight[s], -value[s], s)), weight, value


def render(stock, path, stores, rows, uncovered):
    order, weight, value = store_order(rows)
    total = sum(value.values())
    lines = [f"# Purchase order of the {stock['budget']:,} CLP plan ({path.stem})", "",
             f"From the live stock check `{path.name}` (`scripts/plan_purchase.py`), {len(stores)} stores chosen by the owner's rules of 2026-10-19: "
             "stock first, fewer stores, the cards at risk are secured first. Live prices of the stock check; the plan priced them a few hours earlier.", "",
             f"{sum(r['qty'] for r in rows)} copies of {len(rows)} distinct cards; total {total:,} CLP; shipping assumed "
             f"{am.shipping_clp(order):,} CLP (outside the budget).", ""]
    if uncovered:
        lines += ["**No offer inside these stores:** " + ", ".join(uncovered), ""]
    lines += ["## How to buy", "",
              "1. Fill every cart first, the A cards of each store first. A cart shows the quantity limit of a card without paying: where it "
              "says fewer than the plan needs, stop and tell me.",
              "2. Pay store by store in the order below (the riskiest first). If a card of a store fails when you pay, use its fallback (the price "
              "difference is in the table); a card with no fallback means stop and re-plan before paying anything else.", "",
              "| Order | Store | Cards | A cards | Subtotal CLP |", "|---|---|---|---|---|"]
    for i, store in enumerate(order, 1):
        mine = [r for r in rows if r["store"] == store]
        lines.append(f"| {i} | {store} | {len(mine)} | {sum(1 for r in mine if r['reasons'])} | {value[store]:,} |")
    for i, store in enumerate(order, 1):
        mine = sorted((r for r in rows if r["store"] == store), key=lambda r: (not r["reasons"], -r["unit"] * r["qty"], r["card"]))
        lines += ["", f"## {i}. {store} ({value[store]:,} CLP)", "",
                  "| Class | Card | Qty | Unit CLP | Stock shown | Why | Fallback inside the set |", "|---|---|---|---|---|---|---|"]
        for r in mine:
            fb = r["fallback"]
            fallback = f"{fb['store']} {fb['unit']:,} ({(fb['unit'] - r['unit']) * r['qty']:+,})" if fb else "none"
            lines.append(f"| {'A' if r['reasons'] else 'B'} | {r['card']} | {r['qty']} | {r['unit']:,} | "
                         f"{r['stock_shown'] if r['stock_shown'] is not None else '?'} | {', '.join(r['reasons']) or '-'} | {fallback} |")
    return "\n".join(lines) + "\n"


def main(argv):
    path = Path(argv[0]) if argv else sorted(STOCK_DIR.glob("*.json"))[-1]
    stores = tuple(argv[1].split(",")) if len(argv) > 1 else DEFAULT_STORES
    stock = json.loads(path.read_text(encoding="utf-8"))
    rows, uncovered = rows_for(stock, stores)
    text = render(stock, path, stores, rows, uncovered)
    out = ROOT / "decks" / "reports" / f"purchase-order-{stock['budget']}.md"
    out.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
