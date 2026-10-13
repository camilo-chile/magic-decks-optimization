"""Offline tests for scripts/build_ablation_ladder.py (no network, no bulk file)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("build_ablation_ladder", SCRIPTS / "build_ablation_ladder.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

LIST = """// Commander
1 Test Commander

1 Alpha
1 Beta
1 Gamma
1 Delta
25 Mountain
"""
RANKING = [
    {"name": "Alpha", "role": "ramp", "importance_rank": 1},
    {"name": "Beta", "role": "draw", "importance_rank": 2},
    {"name": "Gamma", "role": "ramp", "importance_rank": 3},
    {"name": "Delta", "role": "interaction", "importance_rank": 4},
]
FILLERS = {"ramp": ["Weak Rock", "Weak Ring", "Beta"], "draw": ["Weak Draw"],
           "other": ["Weak Other"]}


def parts():
    return mod.split_list(LIST)


def test_pairs_follow_rank_and_roles_with_fallback_to_other():
    commander_lines, main = parts()
    pairs = mod.walk(RANKING, FILLERS, [n for _, n in main], 4)
    assert pairs == [("Alpha", "Weak Rock", "ramp"), ("Beta", "Weak Draw", "draw"),
                     ("Gamma", "Weak Ring", "ramp"), ("Delta", "Weak Other", "interaction")]
    assert commander_lines == ["1 Test Commander"]


def test_a_filler_already_in_the_list_is_skipped():
    _, main = parts()
    fillers = {"ramp": ["Beta", "Weak Rock"], "draw": ["Weak Draw"], "other": ["X", "Y"]}
    pairs = mod.walk(RANKING, fillers, [n for _, n in main], 3)
    assert pairs[0] == ("Alpha", "Weak Rock", "ramp")  # "Beta" is in the list, so it is not a filler
    assert pairs[2] == ("Gamma", "X", "ramp")


def test_rungs_are_nested_and_lands_never_change():
    commander_lines, main = parts()
    rungs = mod.ladder(commander_lines, main, RANKING, FILLERS, k_values=(1, 2, 4))
    outs = {k: {o for o, _, _ in pairs} for k, (_, pairs) in rungs.items()}
    assert outs[1] < outs[2] < outs[4]
    text2 = rungs[2][0]
    assert "Weak Rock" in text2 and "Weak Draw" in text2 and "Gamma" in text2
    assert "25 Mountain" in text2 and "1 Test Commander" in text2
    assert "Alpha" not in text2 and "Beta" not in text2


def test_running_out_of_fillers_is_an_error():
    _, main = parts()
    try:
        mod.walk(RANKING, {"ramp": ["Weak Rock"]}, [n for _, n in main], 4)
    except ValueError as err:
        assert "no unused filler" in str(err)
    else:
        raise AssertionError("expected ValueError")


def test_the_rungs_are_the_five_agreed_values_of_k():
    assert mod.K_VALUES == (2, 4, 6, 10, 20)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
