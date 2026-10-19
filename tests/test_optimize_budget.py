"""Offline tests for scripts/optimize_budget.py (no network, no files written)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
spec = importlib.util.spec_from_file_location("optimize_budget", SCRIPTS / "optimize_budget.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def entry(cost, power, **extra):
    return {"cost_clp": cost, "power": power, "bracket": "3", **extra}


MEASURED = {"lists": {
    "a/s0": entry(0, 7.1, round=3), "a/s1": entry(30_000, 7.0, round=3), "a/s2": entry(100_000, 7.5, round=3),
    "b/s0": entry(0, 4.9, round=3), "b/s1": entry(25_000, 6.1, round=3), "b/s2": entry(56_000, 6.9, round=3),
    "b/s3": entry(150_000, 7.4, round=3), "b/old": entry(49_000, 6.6, round=1),
    "c/s0": entry(0, 4.1, round=3), "c/s1": entry(40_000, 5.9, round=3), "c/s2": entry(100_000, 6.8, round=3),
    "c/legacy": entry(10_000, 7.9, eligible=True),
}}


def test_only_eligible_lists_and_a_dearer_list_that_measured_no_higher_is_dropped():
    pts = mod.load_points(MEASURED)
    assert [p["label"] for p in pts["a"]] == ["s0", "s2"]  # s1 costs more and measured lower than s0
    assert "old" not in [p["label"] for p in pts["b"]]     # round 1 is not eligible
    assert pts["c"][1]["label"] == "legacy"                # eligible by flag, cheapest list that reaches 7.9


def test_variant_entries_are_measured_but_never_planned():
    measured = {"lists": {"a/s0": entry(0, 7.0, round=3), "a/s1": entry(10_000, 7.9, round=3, variant="bcore")}}
    assert [p["label"] for p in mod.load_points(measured)["a"]] == ["s0"]


def test_the_highest_sum_wins_even_when_one_deck_runs_far_ahead():
    pts = {"a": [{"label": "a0", "cost": 0, "power": 7.1}, {"label": "a1", "cost": 50_000, "power": 7.4}],
           "b": [{"label": "b0", "cost": 0, "power": 7.0}, {"label": "b1", "cost": 60_000, "power": 7.1}]}
    row = mod.best_for_budget(pts, 60_000)
    # a1 + b0 = 14.4 beats a0 + b1 = 14.2: the money goes where it buys more power, the gap (0.4) is only reported
    assert row["decks"]["a"]["label"] == "a1" and row["decks"]["b"]["label"] == "b0"
    assert row["sum_power"] == 14.4 and row["gap"] == 0.4 and row["cost"] == 50_000 and row["min_power"] == 7.0


def test_ties_prefer_the_stronger_weakest_deck_then_the_lower_cost():
    pts = {"a": [{"label": "a0", "cost": 0, "power": 7.0}, {"label": "a1", "cost": 10_000, "power": 7.2}],
           "b": [{"label": "b0", "cost": 0, "power": 6.8}, {"label": "b1", "cost": 20_000, "power": 7.0}]}
    # a1 + b0 and a0 + b1 both sum to 14.0 and 14.2? a1+b0 = 14.0, a0+b1 = 14.0: the weakest deck decides (6.8 vs 7.0)
    row = mod.best_for_budget(pts, 25_000)
    assert row["decks"]["a"]["label"] == "a0" and row["decks"]["b"]["label"] == "b1"
    cheap = {"a": [{"label": "a0", "cost": 0, "power": 7.0}], "b": [{"label": "b0", "cost": 0, "power": 7.0}]}
    assert mod.best_for_budget(cheap, 50_000)["cost"] == 0


def test_budget_is_never_exceeded_and_no_fit_is_reported():
    pts = mod.load_points(MEASURED)
    for budget in mod.BUDGETS:
        row = mod.best_for_budget(pts, budget)
        assert row["cost"] <= budget and row["unspent"] == budget - row["cost"]
    assert mod.best_for_budget({"a": [{"label": "x", "cost": 500_000, "power": 7.0}]}, 100_000) is None
    assert mod.curve({"a": [{"label": "x", "cost": 500_000, "power": 7.0}]})[0]["decks"] is None


def test_more_budget_never_lowers_the_total_power():
    pts = mod.load_points(MEASURED)
    sums = [mod.best_for_budget(pts, b)["sum_power"] for b in mod.BUDGETS]
    assert sums == sorted(sums)


def test_jumps_follow_the_budget_steps():
    pts = {"a": [{"label": "a0", "cost": 0, "power": 7.1}, {"label": "a1", "cost": 50_000, "power": 7.4}],
           "b": [{"label": "b0", "cost": 0, "power": 7.0}, {"label": "b1", "cost": 60_000, "power": 7.1}]}
    rows = mod.curve(pts, budgets=[50_000, 60_000, 110_000])
    assert mod.jumps(rows) == {"a": [(60_000, 0.0), (110_000, 0.0)], "b": [(60_000, 0.0), (110_000, 0.1)]}


def test_best_buys_rank_power_per_clp_and_skip_free_steps():
    pts = {"a": [{"label": "a0", "cost": 0, "power": 7.0}, {"label": "a1", "cost": 20_000, "power": 7.2},
                 {"label": "a2", "cost": 120_000, "power": 7.5}],
           "b": [{"label": "b0", "cost": 10_000, "power": 6.0}, {"label": "b1", "cost": 30_000, "power": 7.0}]}
    buys = mod.best_buys(pts)
    assert [(s["deck"], s["to"]) for s in buys] == [("b", "b1"), ("a", "a1"), ("a", "a2")]
    assert buys[0]["per_10k"] == 0.5 and buys[1]["per_10k"] == 0.1 and buys[2]["extra_cost"] == 100_000


def test_best_buys_merge_lists_that_cost_nearly_the_same():
    pts = {"a": [{"label": "r4s31", "cost": 24_751, "power": 5.8}, {"label": "r3s24", "cost": 24_827, "power": 6.4},
                 {"label": "r4s39", "cost": 48_951, "power": 7.4}]}
    assert [(s["from"], s["to"]) for s in mod.best_buys(pts)] == [("r3s24", "r4s39")]


def test_render_lists_every_budget_and_the_best_buys():
    pts = mod.load_points(MEASURED)
    text = mod.render(mod.curve(pts), pts, "2026.4195", "2026-10-19")
    rows = [line for line in text.splitlines() if line.startswith("| 100,000 |") or line.startswith("| 300,000 |")]
    assert len(rows) == 2 and "Weakest" in text
    assert "Best buys first" in text and "parity" in text.lower()  # the header says the rule is gone


if __name__ == "__main__":
    failed = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("ok", name)
            except Exception as exc:  # noqa: BLE001
                failed += 1
                print("FAIL", name, repr(exc))
    sys.exit(1 if failed else 0)
