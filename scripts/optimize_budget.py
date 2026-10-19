#!/usr/bin/env python3
"""Phase 8 step 3: the budget curve.

Run it with the "Run Python File" button (no arguments, no network). For every budget from 100,000 to 300,000 CLP
in steps of 50,000 it picks one MEASURED list per deck from `decks/proposals/measured.json` so that

  1. the sum of the three powers is as high as possible (every CLP goes where it buys the most power),
  2. then the weakest deck is as strong as possible,
  3. then the total cost is as low as possible.

Owner decision (2026-10-19): the parity rule of the first goal (decks within 0.2 power points of each other) is dropped;
each deck gets the most power its money buys, whatever the others score. The gap between decks is still reported.

Only lists measured on Commander Salt feed it (owner rule, 2026-10-18: the agents' power judgments ran 0.3 to 2.1 points
too high). A measured entry is eligible when it carries `"eligible": true`, or, when it says nothing, when its `round` is
at least MIN_ROUND (round-1 lists contain reversible cards and are not valid; round 2 is superseded by round 3). A dearer
list that measured no higher than a cheaper one of the same deck is never chosen (in the best buys; the plan itself
considers every eligible list). Costs are card totals from `scripts/ladder.py` (shipping is outside the budget). The chosen
lists still go through stock verification (Phase 9) and a final Salt measurement (Phase 11).

Shared copies (found 2026-10-19): a card the owner has in one copy and two decks play can sit in only one deck, so the
second deck buys it (Entomb alone costs 22,400 CLP). The cost of a combination is therefore the joint cost of its three
lists, each owned copy used once, priced from the saved lists in `decks/measured/` with the newest merged prices, the
owned inventory and the cheapest English or Spanish offer; the "alone" cost of a list (measured.json) is only its own price.
When the lists or the caches are missing, the plain sum of the alone costs is used and the output says so.

Writes:
  data/model/budget-curve.json   the choice per budget and the best buys (read by the dashboard data script)
  decks/reports/budget-curve.md  the same as tables
"""
import itertools
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
MEASURED = ROOT / "decks" / "proposals" / "measured.json"
LISTS_DIR = ROOT / "decks" / "measured"
OUT_JSON = ROOT / "data" / "model" / "budget-curve.json"
OUT_MD = ROOT / "decks" / "reports" / "budget-curve.md"
BUDGETS = list(range(100_000, 300_001, 50_000))
TARGET_POWER = 7.0  # owner decision 2026-10-19 (it was the friend's 6.1)
MIN_ROUND = 3
MIN_STEP = 5_000  # best buys: lists closer in cost than this are alternatives, not a purchase


def frontier(points):
    """Cheapest first; keeps a point only when it measured higher than every cheaper one."""
    kept, best = [], None
    for point in sorted(points, key=lambda p: (p["cost"], -p["power"])):
        if best is None or point["power"] > best:
            kept.append(point)
            best = point["power"]
    return kept


def load_points(measured, min_round=MIN_ROUND, keep_all=False):
    """{deck slug: frontier of its eligible measured lists}; every eligible list when `keep_all` (the plan search)."""
    by_deck = {}
    for key, entry in measured.get("lists", {}).items():
        deck, label = key.split("/", 1)
        if entry.get("power") is None or entry.get("variant") or not entry.get("eligible", (entry.get("round") or 0) >= min_round):
            continue  # a `variant` entry (such as a black-core test list) is measured and charted, never planned
        by_deck.setdefault(deck, []).append({"label": label, "cost": entry["cost_clp"], "power": entry["power"],
                                             "bracket": entry.get("bracket")})
    return {deck: (sorted(points, key=lambda p: (p["cost"], -p["power"])) if keep_all else frontier(points))
            for deck, points in by_deck.items()}


def make_joint_cost(candidates):
    """cost({deck: point}) -> CLP of the three lists together, every owned copy used once, or None (with a note) when
    the saved lists, the prices, the inventory or the Scryfall bulk are not there."""
    sys.path.insert(0, str(SCRIPTS))
    import allocation_model as am  # noqa: E402
    import layer_a as la  # noqa: E402
    bulk = la.latest_bulk()
    if bulk is None or am.latest_merged() is None or not am.INVENTORY_PATH.exists():
        print("Note: the Scryfall bulk, the merged prices or the inventory are missing: costs are the plain sum of the lists.")
        return None
    index = la.build_index(list(la.iter_cards(bulk)))
    offers = am.load_offers(index)[0]
    owned = am.load_owned()
    listings = {}
    for deck, points in candidates.items():
        for point in points:
            path = LISTS_DIR / deck / f"{point['label']}.txt"
            if not path.exists():
                print(f"Note: {path.relative_to(ROOT)} is missing: costs are the plain sum of the lists.")
                return None
            listings[(deck, point["label"])] = am.read_list(path.read_text(encoding="utf-8-sig"), index)

    def cost(combo):
        claimed = Counter()
        return sum(am.price_list(listings[(deck, point["label"])], owned, offers, claimed)["cost_clp"]
                   for deck, point in sorted(combo.items()))
    return cost


def best_for_budget(points, budget, joint=None):
    """The best combination of one list per deck within the budget, or None when no combination fits. `joint` (see
    make_joint_cost) prices a combination with the owned copies shared once; without it the costs are simply added."""
    decks = sorted(points)
    best = None
    for combo in itertools.product(*(points[deck] for deck in decks)):
        chosen = dict(zip(decks, combo))
        cost = joint(chosen) if joint else sum(p["cost"] for p in combo)
        if cost > budget:
            continue
        powers = [p["power"] for p in combo]
        key = (round(sum(powers), 2), min(powers), -cost)
        if best is None or key > best[0]:
            best = (key, chosen, cost)
    if best is None:
        return None
    _, chosen, cost = best
    powers = [p["power"] for p in chosen.values()]
    alone = sum(p["cost"] for p in chosen.values())
    return {"budget": budget, "decks": chosen, "cost": cost, "unspent": budget - cost, "min_power": min(powers),
            "shared_extra": cost - alone, "sum_power": round(sum(powers), 2), "gap": round(max(powers) - min(powers), 2),
            "reaches_target": min(powers) >= TARGET_POWER}


def curve(points, budgets=BUDGETS, joint=None):
    return [best_for_budget(points, budget, joint) or {"budget": budget, "decks": None} for budget in budgets]


def plan(measured):
    """(frontier points per deck, the plan rows): the plan searches every eligible list with joint costs."""
    candidates = load_points(measured, keep_all=True)
    joint = make_joint_cost(candidates) if len(candidates) >= 3 else None
    return {deck: frontier(points) for deck, points in candidates.items()}, curve(candidates, joint=joint)


def jumps(rows):
    """Power change of every deck from one budget to the next, {deck: [(budget, change)]} (the first budget has none)."""
    out = {}
    for before, after in zip(rows, rows[1:]):
        if not before.get("decks") or not after.get("decks"):
            continue
        for deck, point in after["decks"].items():
            out.setdefault(deck, []).append((after["budget"], round(point["power"] - before["decks"][deck]["power"], 2)))
    return out


def best_buys(points, min_step=MIN_STEP):
    """Every step from one point of a deck's frontier to the next, best power per CLP first (cost > 0 only).
    A point less than `min_step` CLP below the next one is merged into it: two lists that cost nearly the same are
    alternatives (often of different rounds), not a purchase."""
    steps = []
    for deck, frontier_pts in points.items():
        pts = [p for i, p in enumerate(frontier_pts)
               if i + 1 == len(frontier_pts) or frontier_pts[i + 1]["cost"] - p["cost"] >= min_step]
        for before, after in zip(pts, pts[1:]):
            extra = after["cost"] - before["cost"]
            if extra <= 0:
                continue
            gain = round(after["power"] - before["power"], 2)
            steps.append({"deck": deck, "from": before["label"], "to": after["label"], "from_cost": before["cost"],
                          "to_cost": after["cost"], "extra_cost": extra, "gain": gain,
                          "per_10k": round(gain / extra * 10_000, 3)})
    return sorted(steps, key=lambda s: (-s["per_10k"], s["extra_cost"]))


def render(rows, points, version, scored_on):
    decks = sorted(points)
    lines = ["# Budget curve (measured points only)", "",
             f"Generated {date.today().isoformat()} by `scripts/optimize_budget.py` from `decks/proposals/measured.json` "
             f"(Commander Salt {version}, measured {scored_on}). One measured list per deck, the highest sum of powers "
             f"within the budget (no parity rule since 2026-10-19); every deck should reach {TARGET_POWER}. Costs are cards "
             "only (shipping outside the budget). The list costs are each list alone; \"Total\" is the three lists together "
             "with every owned copy used once, and \"Shared copies\" is what the decks pay on top of the alone costs because "
             "a card the owner has once is played by two decks.", "",
             "| Budget | " + " | ".join(decks) + " | Total | Shared copies | Unspent | Sum | Weakest | Gap | All >= 7.0 |",
             "|---|" + "---|" * (len(decks) + 7)]
    for row in rows:
        if not row.get("decks"):
            lines.append(f"| {row['budget']:,} | " + " | ".join("-" for _ in decks) + " | no list fits | - | - | - | - | - | - |")
            continue
        cells = [f"{row['decks'][d]['label']} ({row['decks'][d]['cost']:,}; {row['decks'][d]['power']})" for d in decks]
        lines.append(f"| {row['budget']:,} | " + " | ".join(cells)
                     + f" | {row['cost']:,} | {row.get('shared_extra', 0):,} | {row['unspent']:,} | {row['sum_power']} | "
                     + f"{row['min_power']} | {row['gap']} | "
                     + f"{'yes' if row['reaches_target'] else 'no'} |")
    lines += ["", "Power change of each deck from one budget to the next:", ""]
    for deck, steps in sorted(jumps(rows).items()):
        lines.append(f"- {deck}: " + ", ".join(f"{b:,}: {d:+.1f}" for b, d in steps))
    lines += ["", "Best buys first (power gained per 10,000 CLP between two measured points of the same deck):", "",
              "| Deck | From | To | Extra CLP | Power | Per 10,000 CLP |", "|---|---|---|---|---|---|"]
    for s in best_buys(points):
        lines.append(f"| {s['deck']} | {s['from']} ({s['from_cost']:,}) | {s['to']} ({s['to_cost']:,}) | "
                     f"{s['extra_cost']:,} | {s['gain']:+.1f} | {s['per_10k']:+.2f} |")
    lines += ["", "Measured points used per deck (cost CLP; power):", ""]
    for deck in decks:
        lines.append(f"- {deck}: " + ", ".join(f"{p['label']} ({p['cost']:,}; {p['power']})" for p in points[deck]))
    return "\n".join(lines) + "\n"


def main():
    measured = json.loads(MEASURED.read_text(encoding="utf-8"))
    points, rows = plan(measured)
    if len(points) < 3:
        print(f"Only {len(points)} deck(s) have eligible measured lists: {sorted(points)}. Nothing written.")
        sys.exit(2)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps({"scoring_version": measured.get("scoring_version"), "points": points, "curve": rows,
                                    "best_buys": best_buys(points)}, indent=1, ensure_ascii=False), encoding="utf-8")
    OUT_MD.write_text(render(rows, points, measured.get("scoring_version"), measured.get("scored_on")), encoding="utf-8")
    print(OUT_MD.read_text(encoding="utf-8"))
    print(f"Wrote {OUT_JSON.relative_to(ROOT)} and {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
