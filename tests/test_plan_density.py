"""Offline tests for scripts/plan_density.py (a synthetic 100-card list and plan, schema of 2026-10-31)."""
import json
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import plan_density as pd  # noqa: E402


def names(prefix, n):
    return [f"{prefix} {i}" for i in range(1, n + 1)]


GROUPS = {"engine": names("Enabler", 15), "payoff": names("Payoff", 15), "ramp": names("Ramp", 10),
          "draw": names("Draw", 10), "removal": names("Removal", 8), "wipe": names("Wipe", 2),
          "protection": names("Guard", 3), "land": names("Land", 10)}  # 73 cards plus 26 Forest = 99, 36 lands
TEXT = "// Commander\n1 The Commander\n\n" + "".join(f"1 {n}\n" for g in GROUPS.values() for n in g) + "26 Forest\n"


def good_plan():
    tags = {n: tag for tag, group in GROUPS.items() for n in group}
    return {
        "plan": "Enablers feed payoffs", "backup": "Ramp into the same payoffs",
        "win_routes": {
            "combat route": {"cards": ["Payoff 12", "Payoff 13"], "axis": "combat", "vs_three": "one player per hit, three hits"},
            "alt route": {"cards": ["The Commander", "Payoff 14", "Payoff 15"], "axis": "alternate",
                          "vs_three": "a table-wide effect"}},
        "functions": {
            "enabler": {"cards": GROUPS["engine"][:10], "needed_by": "early"},
            "payoff": {"cards": GROUPS["payoff"][:6], "needed_by": "late"},
            "through_wide_board": GROUPS["engine"][10:] + GROUPS["payoff"][6:11],
            "through_big_creatures": GROUPS["removal"] + GROUPS["wipe"]},
        "tags": tags}


def read(text):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "d.txt"
        path.write_text(text, encoding="utf-8")
        return pd.read_list(path)


def check(plan, text=TEXT):
    cards, shown, commanders, library = read(text)
    return pd.check(cards, shown, commanders, library, plan)


def failed(result, *fragments):
    return any(all(f in line for f in fragments) for line in result["fail"])


def test_odds_match_the_hypergeometric_values():
    assert round(pd.odds_at_least_one(2, 15) * 100) == 28 and round(pd.odds_at_least_one(4, 15) * 100) == 49
    assert round(pd.odds_at_least_one(8, 15) * 100) == 75 and round(pd.odds_at_least_one(12, 15) * 100) == 88
    assert pd.odds_at_least_one(0, 15) == 0.0 and pd.odds_at_least_one(90, 15) == 1.0


def test_the_list_has_99_in_the_library_and_a_good_plan_passes_with_basics_untagged():
    cards, shown, commanders, library = read(TEXT)
    assert library == 99 and commanders == {"the commander"}
    result = check(good_plan())
    assert result["fail"] == [] and result["warn"] == []
    assert result["tags"]["land"] == 36 and result["plan_share"] == (30, 63) and result["uncovered"] == []
    assert result["functions"]["enabler"]["pieces"] == 10 and result["functions"]["payoff"]["needed_by"] == "late"


def test_a_plan_card_in_no_function_and_no_route_counts_as_an_orphan():
    plan = good_plan()
    plan["win_routes"]["combat route"]["cards"] = ["Payoff 12"]
    plan["win_routes"]["alt route"]["cards"] = ["The Commander"]  # Payoff 13, 14 and 15 are now in no route
    assert check(plan)["fail"] == [] and len(check(plan)["uncovered"]) == 3
    plan["functions"]["through_wide_board"].remove("Enabler 15")  # the fourth one
    result = check(plan)
    assert failed(result, "4 orphan cards", "Enabler 15", "4 are plan cards in no function and no route")


def test_declared_orphans_count_too_and_a_second_tag_is_allowed():
    plan = good_plan()
    for n in names("Draw", 4):
        plan["tags"][n] = "orphan"
    assert failed(check(plan), "4 orphan cards", "Draw 1")
    plan = good_plan()
    plan["tags"]["Draw 1"] = ["draw", "tutor"]
    assert check(plan)["fail"] == []


def test_functions_need_10_early_or_6_late_pieces_and_every_card_must_be_in_the_list():
    plan = good_plan()
    plan["functions"]["enabler"]["cards"] = GROUPS["engine"][:9]
    plan["functions"]["payoff"]["cards"] = GROUPS["payoff"][:5]
    plan["functions"]["vehicles"] = {"cards": ["Ghost Vehicle"], "needed_by": "late"}
    result = check(plan)
    assert failed(result, "function enabler (early): 9 pieces (minimum 10)")
    assert failed(result, "function payoff (late): 5 pieces (minimum 6)")
    assert failed(result, "function vehicles: not in the list: ghost vehicle")
    plan["functions"]["bad_timing"] = {"cards": GROUPS["engine"][:10], "needed_by": "someday"}
    assert failed(check(plan), "needed_by must be one of")


def test_the_two_reference_board_functions_are_required():
    plan = good_plan()
    del plan["functions"]["through_wide_board"]
    assert failed(check(plan), "required function through_wide_board is not declared")


def test_the_commander_counts_as_a_guaranteed_piece():
    plan = good_plan()
    plan["functions"]["closer"] = {"cards": GROUPS["payoff"][:5], "needed_by": "late"}
    assert failed(check(plan), "function closer (late): 5 pieces")
    plan["functions"]["closer"]["cards"] = ["The Commander"] + GROUPS["payoff"][:5]
    result = check(plan)
    assert not failed(result, "function closer") and result["functions"]["closer"]["guaranteed"]
    assert result["functions"]["closer"]["pieces"] == 6 and result["functions"]["closer"]["odds"][7] == 1.0


def test_tutors_count_as_pieces_of_the_functions_they_can_fetch_for():
    plan = good_plan()
    plan["functions"]["closer"] = {"cards": GROUPS["payoff"][:5], "needed_by": "late"}
    plan["tutors"] = {"Draw 1": ["closer"]}
    result = check(plan)
    assert not failed(result, "function closer") and result["functions"]["closer"]["pieces"] == 6
    plan["tutors"] = {"Not A Card": ["closer"]}
    assert failed(check(plan), "tutor not in the list: not a card")


def test_win_routes_are_validated_and_one_must_not_need_combat():
    plan = good_plan()
    plan["win_routes"] = {"one": {"cards": ["Payoff 12"], "axis": "combat", "vs_three": "x"}}
    assert failed(check(plan), "1 win routes (minimum 2)")
    plan["win_routes"] = {"a": {"cards": [], "axis": "combat", "vs_three": "x"},
                          "b": {"cards": ["Ghost"], "axis": "magic", "vs_three": ""}}
    result = check(plan)
    assert failed(result, "win route 'a' names no card") and failed(result, "win route 'b': not in the list: ghost")
    assert failed(result, "axis must be one of") and failed(result, "say how it beats three opponents")
    plan["win_routes"] = {"a": {"cards": ["Payoff 12"], "axis": "combat", "vs_three": "x"},
                          "b": {"cards": ["Payoff 13"], "axis": "combat", "vs_three": "y"}}
    assert failed(check(plan), "every win route needs combat damage")
    plan["win_routes"]["b"] = {"cards": ["Payoff 12", "Payoff 13"], "axis": "noncombat", "vs_three": "y"}
    assert failed(check(plan), "not independent", "payoff 12")


def test_untagged_and_unknown_tags_fail_and_tags_for_absent_cards_and_the_commander_warn():
    plan = good_plan()
    del plan["tags"]["Removal 1"]
    plan["tags"]["Removal 2"] = "sweeper"
    plan["tags"]["Not In The Deck"] = "ramp"
    plan["tags"]["The Commander"] = "engine"
    result = check(plan)
    assert failed(result, "1 cards without a tag: Removal 1") and failed(result, "unknown tags ['sweeper']")
    assert any("not in the list: not in the deck" in w for w in result["warn"])
    assert any("the commander needs no tag" in w for w in result["warn"])


def test_base_counts_under_the_templates_only_warn_and_no_plan_fails():
    plan = good_plan()
    plan["plan"], plan["backup"] = "", ""
    for n in names("Ramp", 5):
        plan["tags"][n] = "draw"
    result = check(plan)
    assert failed(result, "no primary plan")
    assert any("no backup plan" in w for w in result["warn"]) and any("5 ramp cards" in w for w in result["warn"])
    assert not failed(result, "ramp")


def test_lands_outside_the_template_band_warn_and_bad_when_drawn_is_capped():
    cards, shown, commanders, library = read(TEXT.replace("26 Forest", "19 Forest"))
    result = pd.check(cards, shown, commanders, library, good_plan())
    assert any("29 lands, the templates ask for 36 to 38" in w for w in result["warn"]) and result["fail"] == []
    plan = good_plan()
    plan["bad_when_drawn"] = {n: "early" for n in names("Enabler", 13)}
    result = check(plan)
    assert any("13 cards are bad when drawn" in w for w in result["warn"]) and result["bad_when_drawn"] == {"early": 13}
    plan["bad_when_drawn"] = {"Enabler 1": "sometimes"}
    assert failed(check(plan), "bad_when_drawn must be one of", "enabler 1")


def test_run_plan_writes_the_report_next_to_the_decklist_slug():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "demo.txt").write_text(TEXT, encoding="utf-8")
        (root / "demo.plan.json").write_text(json.dumps(good_plan()), encoding="utf-8")
        slug, result = pd.run_plan(root / "demo.plan.json", root / "reports")
        text = (root / "reports" / "consistency-demo.md").read_text(encoding="utf-8")
        assert slug == "demo" and not result["fail"] and text.startswith("# Consistency gate: demo (PASS)")
        assert "| enabler | early (judged at 12 cards) | 10 |" in text and "| payoff | late (judged at 20 cards) | 6 |" in text
        assert "- alt route (alternate): " in text and "Against three opponents: a table-wide effect" in text


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
