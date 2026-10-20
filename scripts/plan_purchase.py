#!/usr/bin/env python3
"""Phase 10 step 2: the purchase order of a plan, the cards that matter most and have no alternative first. No network, one report.

Run it with the "Run Python File" button (no arguments: the newest stock check in data/stock/ and the stores the owner chose on
2026-10-19) or pass them: `python scripts/plan_purchase.py data/stock/20261019T1542Z.json cardnexus,gameofmagic,...`.

Owner rules (2026-10-19): stock comes first, every extra store is one more order that can fail, and the order matters: he goes to
store 1, puts everything in the cart and pays at once, then store 2, and so on, with no check in between. So every card is bought
where the stock check saw it in stock at the lowest live price among the chosen stores. A card needing several copies is split
across stores when one store shows fewer copies than needed (found 2026-10-19: La Comarca had one Dualcaster Mage, not two). Each
purchase line is classified:

  A (secure first)  no second store inside the set, or the store's shown quantity is no more than the copies bought (one other
                    buyer empties it), or more than one copy is bought where the store shows no quantity
  B                 another store inside the set can fill it and the quantity is comfortable

A card of a win line (CORE: the pieces of the Spellbook lines and the tutors that reach them) weighs extra when it is at risk. The
stores are ordered by the weight of their lines at risk, heaviest first: a line with no second store weighs 10 plus its value in
thousands of CLP, plus 8 for a CORE card; a line with a fallback weighs 1 (thin stock) or 2 (quantity not shown) plus the price
difference of the fallback in thousands of CLP, plus 4 for a CORE card. The last column tells what to do when a line is not there:
the fallback store when it comes LATER in the order (add it to that cart, the price difference is shown), otherwise "tell me".

Writes decks/reports/purchase-order-<budget>.md; when data/model/optional-<budget>.json exists (scripts/plan_optional.py: the real
Ezio commander card and the missing tokens) its lines are added as an optional section outside the budget.
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
MODEL_DIR = ROOT / "data" / "model"
DEFAULT_STORES = ("cardnexus", "gameofmagic", "lacomarca", "magic4ever", "oasis", "paytowin")
WEIGHT = {"thin stock": 1, "quantity not shown": 2}  # a line with no second store weighs 10, see risk_weight
# Pieces of the win lines of the final lists (Layer A / Spellbook flagged combos and the engines that find them).
CORE = {"Etrata, the Silencer", "Magister Sphinx", "Dualcaster Mage", "Helm of the Host", "Godo, Bandit Warlord", "Venser, Shaper Savant",
        "Return the Favor", "Strionic Resonator", "Lithoform Engine", "Intruder Alarm", "Deadeye Navigator", "Starfall Invocation",
        "Ember Island Production", "Solve the Equation", "Reckless Handling", "Loyal Inventor", "Entomb", "Etrata, Deadly Fugitive"}


def allocate(card, stores):
    """([(store, price, copies, shown quantity)], copies still missing, every offer in the set cheapest first)."""
    offers = sorted(((r["price_clp"], r["store"], r["quantity"]) for r in card["records"]
                     if r["status"] == "in_stock" and r["price_clp"] is not None and r["store"] in stores
                     and (r["quantity"] is None or r["quantity"] > 0)), key=lambda o: (o[0], o[1]))
    need, plan = card["qty"], []
    for price, store, shown in offers:
        if need == 0:
            break
        take = need if shown is None else min(need, shown)
        plan.append((store, price, take, shown))
        need -= take
    return plan, need, offers


def rows_for(stock, stores):
    """([{card, take, total, decks, store, unit, stock_shown, fallback, reasons, core}], [cards not covered in the set])."""
    rows, uncovered = [], []
    for card in stock["cards"]:
        plan, missing, offers = allocate(card, stores)
        if missing or not plan:
            uncovered.append(f"{card['name']} ({card['qty'] - missing} of {card['qty']} copies in stock)" if plan else card["name"])
            continue
        used = {p[0] for p in plan}
        for store, price, take, shown in plan:
            spare = [o for o in offers if o[1] not in used and (o[2] is None or o[2] >= take)]
            reasons = []
            if not spare:
                reasons.append("single source")
            if shown is not None and shown <= take:
                reasons.append("thin stock")
            if take > 1 and shown is None:
                reasons.append("quantity not shown")
            rows.append({"card": card["name"], "take": take, "total": card["qty"], "decks": "+".join(sorted(card["decks"])), "store": store,
                         "unit": price, "stock_shown": shown, "reasons": reasons, "core": card["name"] in CORE,
                         "fallback": {"store": spare[0][1], "unit": spare[0][0]} if spare else None})
    return rows, uncovered


def risk_weight(row):
    """How much a failure of this line would hurt: 0 for a B line."""
    if not row["reasons"]:
        return 0.0
    if row["fallback"] is None:
        return 10 + row["unit"] * row["take"] / 1000 + (8 if row["core"] else 0)
    delta = max((row["fallback"]["unit"] - row["unit"]) * row["take"], 0)
    return sum(WEIGHT.get(x, 0) for x in row["reasons"]) + delta / 1000 + (4 if row["core"] else 0)


def order_penalty(rows, order):
    """What the failures of the A lines that have a fallback would cost for this order of stores: the price difference in thousands
    of CLP, plus 5 when the fallback store has already been paid (a second parcel from it). A line with no fallback costs the same
    in every order, so it does not count here."""
    position = {store: i for i, store in enumerate(order)}
    penalty = 0.0
    for r in rows:
        if r["reasons"] and r["fallback"] is not None:
            penalty += max((r["fallback"]["unit"] - r["unit"]) * r["take"], 0) / 1000
            penalty += 0 if position[r["fallback"]["store"]] > position[r["store"]] else 5
    return penalty


def store_order(rows):
    """The order of the stores, with the risk weight and the value of each. Store 1 is the critical one (owner rule, 2026-10-19): the
    store whose win-line (CORE) lines at risk weigh most, so a failure shows before the rest is paid; the other stores follow in the
    order that repairs failures best (a failed line falls back to a store that comes later, so no store is paid twice), and among
    equal orders the heaviest risk first."""
    weight, core, value = {}, {}, {}
    for r in rows:
        weight[r["store"]] = weight.get(r["store"], 0) + risk_weight(r)
        core[r["store"]] = core.get(r["store"], 0) + (risk_weight(r) if r["core"] else 0)
        value[r["store"]] = value.get(r["store"], 0) + r["unit"] * r["take"]
    first = max(weight, key=lambda s: (core[s], weight[s], s))
    rest = sorted(s for s in weight if s != first)
    best = min(itertools.permutations(rest), key=lambda o: (round(order_penalty(rows, (first,) + o), 3), [-weight[s] for s in o]))
    return [first] + list(best), weight, value


def when_missing(row, order):
    fb = row["fallback"]
    if fb is None:
        return "no alternative: tell me" if row["core"] else "no alternative: skip it and tell me"
    delta = (fb["unit"] - row["unit"]) * row["take"]
    if order.index(fb["store"]) > order.index(row["store"]):
        return f"add it in {fb['store']} (store {order.index(fb['store']) + 1}), {fb['unit']:,} each ({delta:+,})"
    return f"{fb['store']} (already bought) {fb['unit']:,} each ({delta:+,}): tell me"


def render(stock, path, stores, rows, uncovered, optional=None):
    order, weight, value = store_order(rows)
    total = sum(value.values())
    lines = [f"# Purchase order of the {stock['budget']:,} CLP plan ({path.stem})", "",
             f"From the live stock check `{path.name}` (`scripts/plan_purchase.py`), {len(stores)} stores chosen by the owner's rules of 2026-10-19: "
             "stock first, fewer stores, the cards that matter most and have no alternative first. Live prices of the stock check, with the "
             "quantities the product pages print.", "",
             f"{sum(r['take'] for r in rows)} copies of {len({r['card'] for r in rows})} distinct cards; total {total:,} CLP; shipping assumed "
             f"{am.shipping_clp(order):,} CLP (outside the budget).", ""]
    if uncovered:
        lines += ["**Not covered inside these stores (needs a decision):** " + "; ".join(uncovered), ""]
    lines += ["## How to buy", "",
              "Store by store in this order: put every line in the cart and pay at once. When a line is not there, the last column says what to do.", "",
              "| Order | Store | Lines | A lines | Subtotal CLP |", "|---|---|---|---|---|"]
    for i, store in enumerate(order, 1):
        mine = [r for r in rows if r["store"] == store]
        lines.append(f"| {i} | {store} | {len(mine)} | {sum(1 for r in mine if r['reasons'])} | {value[store]:,} |")
    for i, store in enumerate(order, 1):
        mine = sorted((r for r in rows if r["store"] == store), key=lambda r: (-risk_weight(r), -r["unit"] * r["take"], r["card"]))
        lines += ["", f"## {i}. {store} ({value[store]:,} CLP)", "",
                  "| Class | Card | Qty | Unit CLP | Line CLP | Stock shown | Why | If it is not there |", "|---|---|---|---|---|---|---|---|"]
        for r in mine:
            qty = str(r["take"]) if r["take"] == r["total"] else f"{r['take']} of {r['total']}"
            lines.append(f"| {'A' if r['reasons'] else 'B'}{' core' if r['core'] and r['reasons'] else ''} | {r['card']} | {qty} | {r['unit']:,} | "
                         f"{r['unit'] * r['take']:,} | {r['stock_shown'] if r['stock_shown'] is not None else '?'} | "
                         f"{', '.join(r['reasons']) or '-'} | {when_missing(r, order)} |")
        lines.append(f"| | **Total** | **{sum(r['take'] for r in mine)}** | | **{value[store]:,}** | | | {len(mine)} lines |")
    if optional:
        lines += ["", "## Optional, outside the budget (only in the stores above, add them if you want)", ""]
        lines += optional
    return "\n".join(lines) + "\n"


def optional_lines(budget, order):
    """The lines of data/model/optional-<budget>.json (plan_optional.py), or None."""
    path = MODEL_DIR / f"optional-{budget}.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    lines = ["| Store | Item | Qty | Unit CLP | Stock shown | Note |", "|---|---|---|---|---|---|"]
    cheapest = {}
    for item in data["items"]:  # one line per item: its cheapest store (the owner adds it where he is already buying)
        if item["name"] not in cheapest or item["unit_clp"] < cheapest[item["name"]]["unit_clp"]:
            cheapest[item["name"]] = item
    for item in sorted(cheapest.values(), key=lambda i: (order.index(i["store"]) if i["store"] in order else 99, i["name"])):
        lines.append(f"| {item['store']} (store {order.index(item['store']) + 1 if item['store'] in order else '-'}) | {item['name']} | {item['qty']} | "
                     f"{item['unit_clp']:,} | {item['stock_shown'] if item['stock_shown'] is not None else '?'} | {item['note']} |")
    for text in data.get("notes", []):
        lines.append(f"\n{text}")
    return lines


def main(argv):
    path = Path(argv[0]) if argv else sorted(STOCK_DIR.glob("*.json"))[-1]
    stores = tuple(argv[1].split(",")) if len(argv) > 1 else DEFAULT_STORES
    stock = json.loads(path.read_text(encoding="utf-8"))
    rows, uncovered = rows_for(stock, stores)
    order = store_order(rows)[0]
    text = render(stock, path, stores, rows, uncovered, optional_lines(stock["budget"], order))
    out = ROOT / "decks" / "reports" / f"purchase-order-{stock['budget']}.md"
    out.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
