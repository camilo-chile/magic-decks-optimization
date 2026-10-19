#!/usr/bin/env python3
"""Phase 10 step 1: which stores to buy from, from the live stock check of `scripts/verify_stock.py`. No network.

Run it with the "Run Python File" button (no arguments: the newest stock check in data/stock/) or pass a file:
`python scripts/plan_stores.py data/stock/20261019T1234Z.json`. For every subset of the stores it works out the cheapest way
to buy every card that has a verified offer inside the subset (only the offers the stock check saw in stock, at their live
price; an offer whose shown quantity is below the copies needed does not count), and prints the best subset of each size:
cards cost, assumed shipping (5,000 CLP per store, outside the budget) and the total with shipping. Cards with no offer in
stock anywhere are listed apart (they need a swap in the deck). The owner picks the number of stores: the cheapest cards are
rarely the fewest parcels.

Writes decks/reports/stores-<budget>-<stamp>.md next to the stock report.
"""
import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allocation_model as am  # noqa: E402
import layer_a as la  # noqa: E402

ROOT = la.ROOT
STOCK_DIR = ROOT / "data" / "stock"


def card_options(card):
    """{store: unit price} of the offers in stock that cover the copies the plan buys."""
    options = {}
    for rec in card["records"]:
        if rec["status"] != "in_stock" or rec["price_clp"] is None:
            continue
        if rec["quantity"] is not None and rec["quantity"] < card["qty"]:
            continue
        if rec["store"] not in options or rec["price_clp"] < options[rec["store"]]:
            options[rec["store"]] = rec["price_clp"]
    return options


def shown_quantity(card):
    """{store: quantity the store shows, or None when it shows none} of the in-stock offers."""
    return {r["store"]: r["quantity"] for r in card["records"] if r["status"] == "in_stock"}


def best_subsets(cards):
    """{number of stores: {"cost", "stores", "pick", "single", "unverified"}}: the cheapest subset of that size that covers
    every card. `single` counts the cards with one store only inside the subset (no second source if its stock fails);
    `unverified` the cards that need more than one copy and are bought where the store shows no quantity."""
    options = {c["name"]: card_options(c) for c in cards}
    shown = {c["name"]: shown_quantity(c) for c in cards}
    stores = sorted({s for o in options.values() for s in o})
    best = {}
    for size in range(1, len(stores) + 1):
        for subset in itertools.combinations(stores, size):
            cost, pick, single, unverified, feasible = 0, {}, 0, 0, True
            for card in cards:
                inside = {s: p for s, p in options[card["name"]].items() if s in subset}
                if not inside:
                    feasible = False
                    break
                store = min(inside, key=lambda s: (inside[s], s))
                pick[card["name"]] = store
                cost += inside[store] * card["qty"]
                single += len(inside) == 1
                unverified += card["qty"] > 1 and shown[card["name"]].get(store) is None
            if feasible and (size not in best or cost < best[size]["cost"]):
                best[size] = {"cost": cost, "stores": subset, "pick": pick, "single": single, "unverified": unverified}
    return best


def render(stock, path, covered, uncovered, best):
    lines = [f"# Stores for the {stock['budget']:,} CLP plan ({path.stem})", "",
             f"From the live stock check `{path.name}` (`scripts/plan_stores.py`): the cheapest purchase inside each number of stores, "
             "every card bought where it was seen in stock now. Shipping is assumed at "
             f"{am.SHIPPING_PER_STORE_CLP:,} CLP per store and is outside the budget.", ""]
    if uncovered:
        lines += ["**No offer in stock anywhere (a swap is needed):** " + ", ".join(c["name"] for c in uncovered), ""]
    if not best:
        return "\n".join(lines) + "\nNo subset of stores covers the cards.\n"
    floor = min(v["cost"] for v in best.values())
    lowest = min(best, key=lambda n: best[n]["cost"] + am.shipping_clp(best[n]["stores"]))
    lines += [f"Cards covered: {len(covered)} of {len(stock['cards'])}. Owner decision (2026-10-19): no limit on the number of stores; the "
              "choice weighs the cards plus the shipping and keeps every card in stock, with a second source where the price is close.", "",
              "| Stores | Cards CLP | More than the cheapest | Shipping | Total with shipping | Cards with one source | Copies with no quantity shown | Which |",
              "|---|---|---|---|---|---|---|---|"]
    for size, row in sorted(best.items()):
        ship = am.shipping_clp(row["stores"])
        mark = " (lowest total)" if size == lowest else ""
        lines.append(f"| {size}{mark} | {row['cost']:,} | {row['cost'] - floor:+,} | {ship:,} | {row['cost'] + ship:,} | {row['single']} | "
                     f"{row['unverified']} | {', '.join(row['stores'])} |")
    return "\n".join(lines) + "\n"


def main(argv):
    path = Path(argv[0]) if argv else sorted(STOCK_DIR.glob("*.json"))[-1]
    stock = json.loads(path.read_text(encoding="utf-8"))
    uncovered = [c for c in stock["cards"] if not card_options(c)]
    covered = [c for c in stock["cards"] if card_options(c)]
    best = best_subsets(covered)
    text = render(stock, path, covered, uncovered, best)
    out = ROOT / "decks" / "reports" / f"stores-{stock['budget']}-{path.stem}.md"
    out.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
