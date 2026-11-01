"""Offline tests for scripts/plan_density.py (a synthetic 100-card list, plan and archetype profile, schema of 2026-11-01)."""
import copy
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


def base(minimum):
    return {"min": minimum, "target": minimum + 2, "why": "toy", "source": "toy"}


def fn(minimum, tier="gate", needed_by="early", **extra):
    return {"min": minimum, "target": minimum + 2, "tier": tier, "needed_by": needed_by, "why": "toy", "source": "toy", **extra}


BOARDS = {"through_wide_board": fn(10), "through_big_creatures": fn(10)}
ARCHS = {
    "toy": {"name": "Toy", "land_band": [36, 38],
            "base": {"ramp": base(10), "draw": base(8), "removal": base(8), "wipe": base(2), "protection": base(3)},
            "functions": {"enabler": fn(10), "payoff": fn(6, needed_by="late"), "haste": fn(4, tier="support"), **BOARDS}},
    "toy_source": {"name": "Toy source", "land_band": [37, 40],
                   "base": {"ramp": base(12), "draw": base(8), "removal": base(8), "wipe": base(1), "protection": base(5)},
                   "functions": {"enabler": fn(12, if_commander_is_source={"needed_by": "late", "min": 6, "target": 8}),
                                 "payoff": fn(6, needed_by="late"), "theme_share": fn(32, tier="support", unit="share"), **BOARDS}},
    "toy_modifier": {"name": "Toy modifier", "land_band": [34, 37],
                     "base": {t: base(1) for t in pd.BASE_TAGS},
                     "functions": {"members": fn(25, if_secondary_modifier={"min": 16, "target": 20, "tier": "support"}), **BOARDS}},
}
META = {"commander_dependence": {"applies_to": "text", "engine": {"min": 5, "target": 7}, "value": {"min": 2, "target": 3}}}


def good_plan():
    tags = {n: tag for tag, group in GROUPS.items() for n in group}
    return {
        "plan": "Enablers feed payoffs", "backup": "Ramp into the same payoffs", "archetype": "toy",
        "win_routes": {
            "combat route": {"cards": ["Payoff 12", "Payoff 13"], "axis": "combat", "vs_three": "one player per hit, three hits"},
            "alt route": {"cards": ["The Commander", "Payoff 14", "Payoff 15"], "axis": "alternate",
                          "vs_three": "a table-wide effect"}},
        "functions": {
            "enabler": {"cards": GROUPS["engine"][:10], "needed_by": "early"},
            "payoff": {"cards": GROUPS["payoff"][:6], "needed_by": "late"},
            "through_wide_board": GROUPS["engine"][10:] + GROUPS["payoff"][6:11],
            "through_big_creatures": GROUPS["removal"] + GROUPS["wipe"]},
        "support": {"haste": GROUPS["ramp"][:4]},
        "tags": tags}


def read(text):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "d.txt"
        path.write_text(text, encoding="utf-8")
        return pd.read_list(path)


def check(plan, text=TEXT, archetypes=ARCHS):
    cards, shown, commanders, library = read(text)
    return pd.check(cards, shown, commanders, library, plan, archetypes=archetypes, meta=META)


def failed(result, *fragments):
    return any(all(f in line for f in fragments) for line in result["fail"])


def warned(result, *fragments):
    return any(all(f in line for f in fragments) for line in result["warn"])


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
    assert result["support"] == {"haste": {"pieces": 4, "min": 4, "reported": True}}


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
    plan["tags"]["Draw 1"] = ["draw", "removal"]
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


def test_the_two_reference_board_functions_are_required_and_always_judged_early():
    plan = good_plan()
    del plan["functions"]["through_wide_board"]
    assert failed(check(plan), "required function through_wide_board is not declared")
    plan = good_plan()  # declaring the boards late would let 6 pieces pass: they are judged early (10)
    plan["functions"]["through_wide_board"] = {"cards": GROUPS["engine"][10:] + GROUPS["payoff"][6:7], "needed_by": "late"}
    result = check(plan)
    assert failed(result, "through_wide_board: the reference boards are judged early")
    assert failed(result, "function through_wide_board (early): 6 pieces (minimum 10)")


def test_the_commander_counts_as_a_guaranteed_piece_and_the_report_shows_the_pieces_without_it():
    plan = good_plan()
    plan["functions"]["closer"] = {"cards": GROUPS["payoff"][:5], "needed_by": "late"}
    assert failed(check(plan), "function closer (late): 5 pieces")
    plan["functions"]["closer"]["cards"] = ["The Commander"] + GROUPS["payoff"][:5]
    result = check(plan)
    closer = result["functions"]["closer"]
    assert not failed(result, "function closer") and closer["guaranteed"]
    assert closer["pieces"] == 6 and closer["odds"][7] == 1.0
    assert closer["without_commander"] == 5 and closer["odds_without"][7] < 1.0
    assert warned(result, "function closer", "only with the commander", "5 pieces without it")


def test_tutors_count_only_when_they_carry_the_tutor_tag():
    plan = good_plan()
    plan["functions"]["closer"] = {"cards": GROUPS["payoff"][:5], "needed_by": "late"}
    plan["tutors"] = {"Draw 1": ["closer"]}  # tagged draw only: naming a rock or a draw spell here proves nothing
    result = check(plan)
    assert failed(result, "tutor Draw 1 must carry the tag 'tutor'") and failed(result, "function closer (late): 5 pieces")
    plan["tags"]["Draw 1"] = ["draw", "tutor"]
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


def test_a_route_that_rests_on_one_card_warns_unless_it_is_the_commander():
    plan = good_plan()
    plan["win_routes"]["combat route"]["cards"] = ["Payoff 12"]
    assert warned(check(plan), "win route 'combat route' rests on a single card")
    plan["win_routes"]["alt route"]["cards"] = ["The Commander"]
    assert not warned(check(plan), "win route 'alt route'")


def test_untagged_and_unknown_tags_fail_and_tags_for_absent_cards_and_the_commander_warn():
    plan = good_plan()
    del plan["tags"]["Removal 1"]
    plan["tags"]["Removal 2"] = "sweeper"
    plan["tags"]["Not In The Deck"] = "ramp"
    plan["tags"]["The Commander"] = "engine"
    result = check(plan)
    assert failed(result, "1 cards without a tag: Removal 1") and failed(result, "unknown tags ['sweeper']")
    assert warned(result, "not in the list: not in the deck") and warned(result, "the commander needs no tag")


def test_base_counts_under_the_profile_only_warn_and_no_plan_fails():
    plan = good_plan()
    plan["plan"], plan["backup"] = "", ""
    for n in names("Ramp", 5):
        plan["tags"][n] = "draw"
    result = check(plan)
    assert failed(result, "no primary plan")
    assert warned(result, "no backup plan") and warned(result, "5 ramp cards, the toy profile asks for 10 or more")
    assert not failed(result, "ramp")


def test_a_second_tag_counts_in_the_base_functions():
    plan = good_plan()
    for n in names("Draw", 3):
        plan["tags"][n] = ["draw", "removal"]  # removal as a second role: 8 + 3 spot answers
    plan["tags"]["Removal 1"] = ["wipe", "protection"]
    result = check(plan)
    assert result["base_counts"]["removal"] == 10 and result["base_counts"]["protection"] == 4
    assert result["base_counts"]["wipe"] == 3 and result["tags"]["removal"] == 7  # the tag table still shows primary tags


def test_lands_outside_the_profile_band_warn_and_bad_when_drawn_counts_only_early_and_late():
    cards, shown, commanders, library = read(TEXT.replace("26 Forest", "19 Forest"))
    result = pd.check(cards, shown, commanders, library, good_plan(), archetypes=ARCHS, meta=META)
    assert warned(result, "29 lands, the toy profile asks for 36 to 38") and result["fail"] == []
    plan = good_plan()
    plan["bad_when_drawn"] = {n: "early" for n in names("Enabler", 13)}
    result = check(plan)
    assert warned(result, "13 cards are bad when drawn") and result["bad_when_drawn"] == {"early": 13}
    plan["bad_when_drawn"] = {n: "never" for n in names("Enabler", 13)}  # marking every card, as the skill asks, is not a warning
    result = check(plan)
    assert not warned(result, "bad when drawn") and result["bad_when_drawn"] == {}
    plan["bad_when_drawn"] = {"Enabler 1": "sometimes"}
    assert failed(check(plan), "bad_when_drawn must be one of", "enabler 1")


def test_a_plan_needs_an_archetype_and_custom_keeps_the_generic_floors():
    plan = good_plan()
    del plan["archetype"]
    assert failed(check(plan), "no archetype declared")
    plan["archetype"] = "nope"
    assert failed(check(plan), "unknown archetype 'nope'")
    plan["archetype"] = "toy"
    plan["secondary"] = "nope"
    assert failed(check(plan), "unknown secondary archetype 'nope'")
    plan = good_plan()
    plan["archetype"], plan["support"] = "custom", {}
    result = check(plan)
    assert not result["fail"] and warned(result, "archetype 'custom'") and result["support"] == {}


def test_the_profile_minimum_is_enforced_when_it_is_above_the_class_minimum():
    plan = good_plan()
    plan["archetype"] = "toy_source"
    plan["functions"]["enabler"]["cards"] = GROUPS["engine"][:11]  # the class asks 10, the profile asks 12
    plan["functions"]["theme_share"] = ["x"]  # a function that does not exist in the profile is not enforced (and unknown cards fail)
    result = check(plan)
    assert failed(result, "function enabler (early): 11 pieces (minimum 12), the toy_source profile asks 12")
    plan["functions"]["enabler"]["cards"] = GROUPS["engine"][:12]
    assert not failed(check(plan), "function enabler")


def test_a_gate_function_of_the_profile_must_be_declared_and_a_support_line_may_not_replace_it():
    plan = good_plan()
    del plan["functions"]["payoff"]
    assert failed(check(plan), "profile function payoff (gate, minimum 6) is not declared")
    assert not failed(check(plan), "profile function haste") and not failed(check(plan), "profile function through")


def test_a_profile_that_needs_a_function_early_does_not_accept_it_late():
    plan = good_plan()
    plan["functions"]["enabler"] = {"cards": GROUPS["engine"][:10], "needed_by": "late"}
    result = check(plan)
    assert failed(result, "function enabler: the toy profile needs it early") and result["functions"]["enabler"]["needed_by"] == "early"


def test_the_commander_alternative_lets_a_source_function_be_judged_late_with_six_pieces():
    plan = good_plan()
    plan["archetype"] = "toy_source"
    plan["commander_dependence"] = "engine"
    plan["functions"]["enabler"] = {"cards": ["The Commander"] + GROUPS["engine"][:5], "needed_by": "late"}
    plan["tags"].update({n: "ramp" for n in GROUPS["ramp"]})
    result = check(plan)
    assert not failed(result, "function enabler") and result["functions"]["enabler"]["required"] == 6
    plan["functions"]["enabler"]["cards"] = GROUPS["engine"][:6]  # without the commander in it, the full early minimum applies
    assert failed(check(plan), "function enabler: the toy_source profile needs it early")


def test_support_lines_are_reported_and_only_warn():
    plan = good_plan()
    plan["support"] = {"haste": GROUPS["ramp"][:3]}
    result = check(plan)
    assert result["fail"] == [] and warned(result, "support line haste: 3 pieces, the toy profile asks 4")
    del plan["support"]
    result = check(plan)
    assert result["fail"] == [] and warned(result, "support line haste", "is not reported")
    plan["support"] = {"haste": ["Ghost"]}
    assert failed(check(plan), "support line haste: not in the list: ghost")


def test_the_commander_dependence_and_the_commander_cost_move_the_base_floors():
    plan = good_plan()
    plan["commander_dependence"] = "engine"  # protection 5 instead of the profile's 3
    assert warned(check(plan), "3 protection cards, the toy profile asks for 5 or more")
    plan["commander_dependence"] = "value"
    assert not warned(check(plan), "protection")
    plan["commander_dependence"] = "sidekick"
    assert failed(check(plan), "commander_dependence must be one of")
    plan = good_plan()
    plan["commander_mv"] = 5
    assert warned(check(plan), "10 ramp cards, the toy profile asks for 12 or more")


def test_a_hybrid_takes_the_higher_minimums_the_band_overlap_and_demotes_a_modifier():
    both = pd.resolve_profile(ARCHS, "toy", "toy_source")
    assert both["land_band"] == (37, 38) and both["base"]["ramp"] == 12 and both["base"]["protection"] == 5
    assert both["functions"]["enabler"]["min"] == 12 and both["functions"]["enabler"]["alt"]["min"] == 6
    assert "theme_share" not in both["functions"]  # a share is not a card count
    apart = pd.resolve_profile(ARCHS, "toy", "toy_modifier")
    assert apart["land_band"] == (36, 37) and apart["functions"]["members"]["tier"] == "gate" and apart["functions"]["members"]["min"] == 25
    modifier = pd.resolve_profile(ARCHS, "toy", "toy_modifier", "modifier")
    assert modifier["functions"]["members"] == {"min": 16, "tier": "support", "needed_by": "early", "alt": None}
    plan = good_plan()
    plan["secondary"], plan["secondary_role"] = "toy_modifier", "modifier"
    plan["support"]["members"] = names("Enabler", 15) + ["Payoff 1"]
    result = check(plan)
    assert result["fail"] == [] and result["support"]["members"]["pieces"] == 16
    plan["secondary_role"] = "sometimes"
    assert failed(check(plan), "secondary_role must be one of")


def test_every_profile_in_the_real_archetypes_file_is_readable_and_its_gate_functions_meet_the_classes():
    archetypes, meta = pd.load_archetypes()
    assert len(archetypes) >= 15 and "commander_dependence" in meta
    for slug, spec in archetypes.items():
        profile = pd.resolve_profile(archetypes, slug)
        assert set(profile["base"]) == set(pd.BASE_TAGS) and profile["land_band"][0] <= profile["land_band"][1], slug
        for required in pd.GATE["required_functions"]:
            assert profile["functions"][required]["needed_by"] == "early" and profile["functions"][required]["min"] >= 10, slug
        for name, f in profile["functions"].items():
            floor = pd.GATE["function_classes"][f["needed_by"]]["min"]
            if f["tier"] == "gate":
                assert f["min"] >= floor, (slug, name)
            if f["alt"]:
                assert f["alt"]["min"] >= pd.GATE["function_classes"][f["alt"]["needed_by"]]["min"], (slug, name)
    resolved = pd.resolve_profile(archetypes, "combat_attackers", "spellslinger")
    assert resolved["functions"]["spell_density"]["min"] >= 28 and "attackers" in resolved["functions"]


def test_run_plan_writes_the_report_next_to_the_decklist_slug():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "demo.txt").write_text(TEXT, encoding="utf-8")
        plan = good_plan()
        plan["archetype"] = "custom"  # run_plan reads the real archetypes file, which has no toy profile
        plan["support"] = {}
        (root / "demo.plan.json").write_text(json.dumps(plan), encoding="utf-8")
        slug, result = pd.run_plan(root / "demo.plan.json", root / "reports")
        text = (root / "reports" / "consistency-demo.md").read_text(encoding="utf-8")
        assert slug == "demo" and not result["fail"] and text.startswith("# Consistency gate: demo (PASS)")
        assert "Archetype: custom" in text
        assert "| enabler | early (judged at 12 cards) | 10 | 10 | 10 |" in text
        assert "| payoff | late (judged at 20 cards) | 6 | 6 | 6 |" in text
        assert "- alt route (alternate): " in text and "Against three opponents: a table-wide effect" in text
        assert "(commander guaranteed)" not in text


def test_the_report_marks_a_function_the_commander_guarantees():
    plan = good_plan()
    plan["functions"]["closer"] = {"cards": ["The Commander"] + GROUPS["payoff"][:5], "needed_by": "late"}
    text = pd.report_markdown("demo", plan, check(plan))
    assert "5 (commander guaranteed)" in text and "Archetype: toy" in text and "## Support lines" in text


if __name__ == "__main__":
    for name, fn_ in list(globals().items()):
        if name.startswith("test_") and callable(fn_):
            fn_()
            print("ok", name)
