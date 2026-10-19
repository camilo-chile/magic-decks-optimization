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


def test_parity_beats_a_higher_weakest_deck_and_the_leader_is_lowered_when_needed():
    pts = {"a": [{"label": "a0", "cost": 0, "power": 7.1}, {"label": "a1", "cost": 50_000, "power": 7.9}],
           "b": [{"label": "b0", "cost": 0, "power": 6.0}, {"label": "b1", "cost": 60_000, "power": 6.8}]}
    row = mod.best_for_budget(pts, 100_000)
    # a1 + b1 costs 110,000 (over budget); a0 + b1 is at parity? 7.1 - 6.8 = 0.3 no; a0 + b0 gap 1.1 no;
    # a1 + b0 gap 1.9 no: nothing is at parity, so the best weakest deck wins and parity is reported false
    assert not row["parity"] and row["decks"]["b"]["label"] == "b1" and row["decks"]["a"]["label"] == "a0"
    pts["a"].append({"label": "a05", "cost": 10_000, "power": 6.9})
    row = mod.best_for_budget(pts, 100_000)
    assert row["parity"] and row["gap"] == 0.1 and row["min_power"] == 6.8 and row["cost"] == 70_000


def test_budget_is_never_exceeded_and_no_fit_is_reported():
    pts = mod.load_points(MEASURED)
    for budget in mod.BUDGETS:
        row = mod.best_for_budget(pts, budget)
        assert row["cost"] <= budget and row["unspent"] == budget - row["cost"]
    assert mod.best_for_budget({"a": [{"label": "x", "cost": 500_000, "power": 7.0}]}, 100_000) is None
    assert mod.curve({"a": [{"label": "x", "cost": 500_000, "power": 7.0}]})[0]["decks"] is None


def test_more_budget_never_lowers_the_weakest_deck():
    pts = mod.load_points(MEASURED)
    weakest = [mod.best_for_budget(pts, b)["min_power"] for b in mod.BUDGETS]
    assert weakest == sorted(weakest)


def test_render_lists_every_budget_and_flags_parity():
    pts = mod.load_points(MEASURED)
    text = mod.render(mod.curve(pts), pts, "2026.4195", "2026-10-19")
    assert text.count("| 100,000 |") == 1 and text.count("| 300,000 |") == 1 and "Weakest" in text


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
