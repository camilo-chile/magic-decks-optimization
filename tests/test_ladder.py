"""Offline tests for the pure helpers of scripts/ladder.py (no network, no caches)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("ladder", SCRIPTS / "ladder.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TEXT = """// Commander
1 Alexios, Deimos of Kosmos

// Base
1 Sol Ring
4 Mountain

// Ladder
+ Lightning Bolt | - Mountain | cheap burn
+ Mana Crypt | - Sol Ring
"""


def test_split_ladder_reads_base_and_swaps():
    head, swaps = mod.split_ladder(TEXT)
    assert "Sol Ring" in head and "Lightning Bolt" not in head
    assert [(s["add"], s["drop"], s["why"]) for s in swaps] == [
        ("Lightning Bolt", "Mountain", "cheap burn"), ("Mana Crypt", "Sol Ring", "")]


def test_a_bad_swap_line_is_an_error():
    try:
        mod.split_ladder("// Base\n1 A\n// Ladder\nswap A for B\n")
    except ValueError as exc:
        assert "not a swap line" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_swaps_apply_in_order_and_basics_count_down():
    head, swaps = mod.split_ladder(TEXT)
    commanders, state = mod.base_state(head)
    state = mod.apply_swap(state, swaps[0]["add"], swaps[0]["drop"])
    assert state["mountain"][1] == 3 and state["lightning bolt"][1] == 1
    state = mod.apply_swap(state, swaps[1]["add"], swaps[1]["drop"])
    assert "sol ring" not in state and state["mana crypt"][1] == 1
    text = mod.render(commanders, state)
    assert text.startswith("// Commander\n1 Alexios, Deimos of Kosmos") and "3 Mountain" in text


def test_removing_a_card_that_is_not_there_is_an_error():
    _, state = mod.base_state("// Main\n1 Sol Ring\n")
    try:
        mod.apply_swap(state, "Mana Crypt", "Island")
    except ValueError as exc:
        assert "cannot remove" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_checkpoints_pick_the_last_valid_step_under_each_cap():
    steps = [{"valid": True, "cost": 0}, {"valid": True, "cost": 20000}, {"valid": False, "cost": 30000},
             {"valid": True, "cost": 45000}, {"valid": True, "cost": 120000}]
    assert mod.pick_checkpoints(steps, (0, 25000, 50000, 100000, 200000)) == {
        0: 0, 25000: 1, 50000: 3, 100000: 3, 200000: 4}
    assert mod.pick_checkpoints([{"valid": True, "cost": 500}], (0,)) == {0: None}


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
