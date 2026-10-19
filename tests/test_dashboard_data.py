"""Offline tests for scripts/dashboard_data.py (no network, no files written)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
spec = importlib.util.spec_from_file_location("dashboard_data", SCRIPTS / "dashboard_data.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

T, A, E, X = ("toph-the-first-metalbender", "fire-lord-azula", "ezio-auditore-da-firenze", "alexios-deimos-of-kosmos")


def entry(cost, power, **extra):
    return {"cost_clp": cost, "power": power, "salt": 50.0, "bracket": "3", **extra}


MEASURED = {"lists": {
    f"{T}/round3-step0": entry(0, 7.1, round=3), f"{T}/round3-step21": entry(49_000, 7.4, round=3),
    f"{T}/round3-step30": entry(97_000, 7.5, round=3), f"{T}/round3-step32": entry(149_000, 7.4, round=3),
    f"{A}/round3-step34": entry(49_000, 7.1, round=3), f"{A}/round1-step9": entry(10_000, 5.0, round=1),
    f"{E}/round3-step39": entry(46_000, 7.0, round=3),
    f"{X}/round2-step19": entry(25_000, 4.1, round=2), f"{X}/round2-step48": entry(197_000, 6.8, round=2),
    f"{E}/round4-bcore-step26": entry(49_000, 5.3, round=4, variant="bcore"),
}}


def test_lists_mark_offered_dominated_and_replaced_and_leave_out_unusable_rounds():
    rows = {r["id"]: r for r in mod.lists_rows(MEASURED)}
    assert rows["toph-r3-30"]["status"] == "offered" and rows["toph-r3-32"]["status"] == "dominated"
    assert rows["alexios-r2-19"]["status"] == "replaced" and rows["alexios-r2-48"]["status"] == "replaced"
    assert "azula-r1-9" not in rows  # round 1 holds reversible cards: never charted
    black = rows["ezio-bcore-r4-26"]  # a variant test list: charted as its own series, never offered
    assert black["status"] == "variant" and black["deck"] == "Ezio black-core" and black["list"] == "Black-core R4 step 26"


def test_plans_buys_and_jumps_follow_the_optimizer_and_alexios_never_enters_a_plan():
    points = mod.ob.load_points(MEASURED)
    assert X not in points
    rows = mod.ob.curve(points, budgets=[100_000, 150_000])
    plans = mod.plan_rows(rows)
    assert [p["id"] for p in plans] == ["100000", "150000"]
    assert plans[1]["toph_cell"] == "R3 step 21 (49,000 CLP)" and plans[1]["powers"] == "7.0 / 7.1 / 7.4"
    assert plans[1]["toph_id"] == "toph-r3-21"
    jumps = {j["id"]: j["change"] for j in mod.jump_rows(rows)}
    assert jumps["150000-toph"] == 0.3 and jumps["150000-total"] == 0.3 and jumps["150000-ezio"] == 0.0
    buys = mod.buy_rows(MEASURED)
    assert {b["deck"] for b in buys} == {"Toph", "Alexios"}  # Azula and Ezio have a single point here
    assert [b["status"] for b in buys if b["deck"] == "Alexios"] == ["replaced"]
    assert buys[0]["rank"] == 1 and buys[0]["per_10k"] >= buys[-1]["per_10k"]


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
