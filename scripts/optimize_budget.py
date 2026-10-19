#!/usr/bin/env python3
"""Phase 8 step 3: the budget curve.

Run it with the "Run Python File" button (no arguments, no network). For every budget from 100,000 to 300,000 CLP
in steps of 50,000 it picks one MEASURED list per deck from `decks/proposals/measured.json` so that

  1. the three decks sit at parity (max power - min power <= 0.2), when any combination within the budget allows it;
  2. the weakest deck is as strong as possible, then the sum of the powers, then the lowest total cost.

Only lists measured on Commander Salt feed it (owner rule, 2026-10-18: the agents' power judgments ran 0.3 to 2.1 points
too high). A measured entry is eligible when it carries `"eligible": true`, or, when it says nothing, when its `round` is
at least MIN_ROUND (round-1 lists contain reversible cards and are not valid). A dearer list that measured no higher than a
cheaper one of the same deck is never chosen. Costs are card totals from `scripts/ladder.py` (shipping is outside the
budget). The chosen lists still go through stock verification (Phase 9) and a final Salt measurement (Phase 11).

Writes:
  data/model/budget-curve.json   the choice per budget (read by the dashboard)
  decks/reports/budget-curve.md  the same as a table
"""
import itertools
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEASURED = ROOT / "decks" / "proposals" / "measured.json"
OUT_JSON = ROOT / "data" / "model" / "budget-curve.json"
OUT_MD = ROOT / "decks" / "reports" / "budget-curve.md"
BUDGETS = list(range(100_000, 300_001, 50_000))
PARITY = 0.2
FRIEND_POWER = 6.1  # the friend's Krenko deck on Commander Salt
MIN_ROUND = 3


def frontier(points):
    """Cheapest first; keeps a point only when it measured higher than every cheaper one."""
    kept, best = [], None
    for point in sorted(points, key=lambda p: (p["cost"], -p["power"])):
        if best is None or point["power"] > best:
            kept.append(point)
            best = point["power"]
    return kept


def load_points(measured, min_round=MIN_ROUND):
    """{deck slug: frontier of its eligible measured lists}."""
    by_deck = {}
    for key, entry in measured.get("lists", {}).items():
        deck, label = key.split("/", 1)
        if entry.get("power") is None or not entry.get("eligible", (entry.get("round") or 0) >= min_round):
            continue
        by_deck.setdefault(deck, []).append({"label": label, "cost": entry["cost_clp"], "power": entry["power"],
                                             "bracket": entry.get("bracket")})
    return {deck: frontier(points) for deck, points in by_deck.items()}


def best_for_budget(points, budget, parity=PARITY):
    """The best combination of one list per deck within the budget, or None when no combination fits."""
    decks = sorted(points)
    best = None
    for combo in itertools.product(*(points[deck] for deck in decks)):
        cost = sum(p["cost"] for p in combo)
        if cost > budget:
            continue
        powers = [p["power"] for p in combo]
        gap = round(max(powers) - min(powers), 2)
        key = (gap <= parity + 1e-9, min(powers), round(sum(powers), 2), -cost)
        if best is None or key > best[0]:
            best = (key, dict(zip(decks, combo)), cost, gap)
    if best is None:
        return None
    _, chosen, cost, gap = best
    powers = [p["power"] for p in chosen.values()]
    return {"budget": budget, "decks": chosen, "cost": cost, "unspent": budget - cost, "min_power": min(powers),
            "gap": gap, "parity": gap <= parity + 1e-9, "above_friend": min(powers) > FRIEND_POWER}


def curve(points, budgets=BUDGETS):
    return [best_for_budget(points, budget) or {"budget": budget, "decks": None} for budget in budgets]


def render(rows, points, version, scored_on):
    decks = sorted(points)
    lines = ["# Budget curve (measured points only)", "",
             f"Generated {date.today().isoformat()} by `scripts/optimize_budget.py` from `decks/proposals/measured.json` "
             f"(Commander Salt {version}, measured {scored_on}). One measured list per deck; parity = within {PARITY} "
             f"power points; the friend's deck is {FRIEND_POWER}. Costs are cards only (shipping outside the budget).", "",
             "| Budget | " + " | ".join(decks) + " | Total | Unspent | Weakest | Gap | Parity | All > 6.1 |",
             "|---|" + "---|" * (len(decks) + 6)]
    for row in rows:
        if not row.get("decks"):
            lines.append(f"| {row['budget']:,} | " + " | ".join("-" for _ in decks) + " | no list fits | - | - | - | - | - |")
            continue
        cells = [f"{row['decks'][d]['label']} ({row['decks'][d]['cost']:,}; {row['decks'][d]['power']})" for d in decks]
        lines.append(f"| {row['budget']:,} | " + " | ".join(cells)
                     + f" | {row['cost']:,} | {row['unspent']:,} | {row['min_power']} | {row['gap']} | "
                     + f"{'yes' if row['parity'] else 'NO'} | {'yes' if row['above_friend'] else 'no'} |")
    lines += ["", "Measured points used per deck (cost CLP; power):", ""]
    for deck in decks:
        lines.append(f"- {deck}: " + ", ".join(f"{p['label']} ({p['cost']:,}; {p['power']})" for p in points[deck]))
    return "\n".join(lines) + "\n"


def main():
    measured = json.loads(MEASURED.read_text(encoding="utf-8"))
    points = load_points(measured)
    if len(points) < 3:
        print(f"Only {len(points)} deck(s) have eligible measured lists: {sorted(points)}. Nothing written.")
        sys.exit(2)
    rows = curve(points)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps({"scoring_version": measured.get("scoring_version"), "parity": PARITY,
                                    "points": points, "curve": rows}, indent=1, ensure_ascii=False), encoding="utf-8")
    OUT_MD.write_text(render(rows, points, measured.get("scoring_version"), measured.get("scored_on")), encoding="utf-8")
    print(OUT_MD.read_text(encoding="utf-8"))
    print(f"Wrote {OUT_JSON.relative_to(ROOT)} and {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
