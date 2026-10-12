"""Offline golden tests for scripts/layer_a.py (no network, no bulk file)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("layer_a", SCRIPTS / "layer_a.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def card(name, identity=(), type_line="Artifact", text="", cmc=1, gc=False,
         legal="legal", faces=None, oracle_id=None):
    out = {
        "name": name,
        "oracle_id": oracle_id or f"id-{name}",
        "type_line": type_line,
        "oracle_text": text,
        "cmc": cmc,
        "color_identity": list(identity),
        "game_changer": gc,
        "legalities": {"commander": legal},
        "mana_cost": "{1}",
        "prices": {"usd": "1.00"},
    }
    if faces:
        out["card_faces"] = faces
        out["oracle_text"] = None
    return out


COMMANDER = card("Test Commander", ["R"], "Legendary Creature - Human", cmc=3)
BASIC = card("Mountain", ["R"], "Basic Land - Mountain", cmc=0, oracle_id="id-mountain")


def deck(extra_cards=(), commander=COMMANDER, fillers=None):
    """Return (cards, commander entries, main entries) with exactly 100 cards by default."""
    extra = list(extra_cards)
    n_fill = 99 - len(extra) if fillers is None else fillers
    cards = [commander, BASIC] + extra
    main = [{"qty": 1, "name": c["name"], "set": "", "num": ""} for c in extra]
    for i in range(max(n_fill, 0)):
        filler = card(f"Filler {i:03d}", ["R"], "Artifact", cmc=2)
        cards.append(filler)
        main.append({"qty": 1, "name": filler["name"], "set": "", "num": ""})
    return cards, [{"qty": 1, "name": commander["name"], "set": "", "num": ""}], main


def run(extra_cards=(), commander=COMMANDER, fillers=None, slug=None):
    cards, cmd, main = deck(extra_cards, commander, fillers)
    return mod.analyze(cmd, main, mod.build_index(cards), slug)[0]


def gcs(n):
    return [card(f"GC {i}", ["R"], gc=True) for i in range(n)]


def test_clean_deck_has_floor_1_and_is_not_rejected():
    r = run()
    assert r["total_cards"] == 100 and r["recognized_cards"] == 100
    assert not r["rejected"] and r["floor"] == 1 and r["reasons"] == []
    assert r["complete"] is False and r["pending_checks"]


def test_game_changer_floors_0_3_4_and_commander_counts():
    assert run(gcs(0))["floor"] == 1
    assert run(gcs(3))["floor"] == 3
    assert run(gcs(4))["floor"] == 4
    gc_commander = card("GC Commander", ["R"], "Legendary Creature - Human", gc=True)
    r = run(gcs(3), commander=gc_commander)
    assert r["checks"]["game_changers"]["count"] == 4 and r["floor"] == 4


def test_extra_turn_cards_one_floor_2_up_to_three_allowed_four_is_floor_4():
    def turn(i):
        return card(f"Turn Spell {i}", ["R"], "Sorcery", "Target player takes an extra turn after this one.")
    assert run([turn(1)])["floor"] == 2
    r3 = run([turn(1), turn(2), turn(3)])
    assert not r3["rejected"] and r3["floor"] == 2
    assert any("low quantities" in n for n in r3["review_notes"])
    r4 = run([turn(1), turn(2), turn(3), turn(4)])
    assert not r4["rejected"] and r4["floor"] == 4 and not r4["floor_ok_so_far"]


def test_cards_that_only_skip_or_forbid_extra_turns_are_not_counted():
    pendant = card("Gerrard's Hourglass Pendant", [], "Artifact",
                   "If a player would begin an extra turn, that player skips that turn instead.")
    hold = card("Stranglehold", ["R"], "Enchantment", "Your opponents can't take extra turns.")
    nexus = card("Ugin's Nexus", [], "Legendary Artifact",
                 "If a player would begin an extra turn, that player skips that turn instead.\n"
                 "If Ugin's Nexus would be put into a graveyard from the battlefield, instead exile "
                 "it and take an extra turn after this one.")
    r = run([pendant, hold, nexus])
    assert r["checks"]["extra_turns"]["cards"] == ["Ugin's Nexus"]


def test_azula_with_one_extra_turn_card_is_floor_2_with_a_review_note():
    azula = card("Fire Lord Azula", ["U", "B", "R"], "Legendary Creature - Human Noble", cmc=4)
    et = card("Final Fortune", ["R"], "Instant", "Take an extra turn after this one.")
    r = run([et], commander=azula)
    assert not r["rejected"] and r["floor"] == 2
    assert any("multiplies" in n for n in r["review_notes"])


def test_mass_land_denial_flags_floor_4():
    armageddon = card("Armageddon", ["W"], "Sorcery", "Destroy all lands.")
    r = run([armageddon])
    assert r["floor"] == 4 and "Armageddon" in r["checks"]["mass_land_denial"]["cards"]
    blood_moon = card("Blood Moon", ["R"], "Enchantment", "Nonbasic lands are Mountains.")
    assert run([blood_moon])["floor"] == 4
    stone_rain = card("Stone Rain", ["R"], "Sorcery", "Destroy target land.")
    assert run([stone_rain])["floor"] == 1


def test_singleton_basics_and_any_number_cards():
    cards, cmd, main = deck([], fillers=98)
    main.append({"qty": 1, "name": "Mountain", "set": "", "num": ""})
    main[0]["qty"] = 2  # a duplicated non-basic filler
    r = mod.analyze(cmd, main, mod.build_index(cards))[0]
    assert any("singleton" in x for x in r["reasons"])
    cards, cmd, main = deck([], fillers=0)
    main.append({"qty": 99, "name": "Mountain", "set": "", "num": ""})
    r = mod.analyze(cmd, main, mod.build_index(cards))[0]
    assert r["total_cards"] == 100 and not r["rejected"]
    rats = card("Relentless Rats", ["B"], "Creature", "A deck can have any number of cards named Relentless Rats.")
    cards, cmd, main = deck([rats], fillers=0)
    main[0]["qty"] = 5
    main.append({"qty": 94, "name": "Mountain", "set": "", "num": ""})
    r = mod.analyze(cmd, main, mod.build_index(cards + [BASIC]))[0]
    assert not any("singleton" in x for x in r["reasons"])


def test_card_count_banned_and_color_identity():
    assert any("expected 100" in x for x in run(fillers=98)["reasons"])
    banned = card("Banned Card", ["R"], legal="banned")
    assert any("not Commander-legal" in x for x in run([banned])["reasons"])
    reckoner = card("Boros Reckoner", ["R", "W"], "Creature - Elemental")
    r = run([reckoner])
    assert r["rejected"] and any("color identity" in x for x in r["reasons"])
    javelin = card("Flame Javelin", ["R"], "Instant")
    assert not run([javelin])["rejected"]


def test_front_face_names_resolve_and_count_as_game_changer():
    tergrid = card("Tergrid, God of Fright // Tergrid's Lantern", ["B"], "Legendary Creature - God",
                   gc=True, faces=[
                       {"name": "Tergrid, God of Fright", "oracle_text": "Menace", "mana_cost": "{3}{B}{B}"},
                       {"name": "Tergrid's Lantern", "oracle_text": "Target player loses 3 life.",
                        "mana_cost": ""}])
    cards, cmd, main = deck([], fillers=98)
    cards.append(tergrid)
    main.append({"qty": 1, "name": "Tergrid, God of Fright", "set": "", "num": ""})
    index = mod.build_index(cards)
    r, facts = mod.analyze(cmd, main, index)
    assert r["recognized_cards"] == 100 and r["checks"]["game_changers"]["cards"] == [tergrid["name"]]
    assert any(f["name"] == tergrid["name"] and "Menace" in f["oracle_text"] for f in facts)


def test_spanish_and_unknown_names_fail_loudly():
    cards, cmd, main = deck([], fillers=98)
    main.append({"qty": 1, "name": "Anillo Solar", "set": "", "num": ""})
    r = mod.analyze(cmd, main, mod.build_index(cards))[0]
    assert r["rejected"] and r["unresolved"] == ["Anillo Solar"]
    assert any(x.startswith("STOP") for x in r["reasons"])


def test_commander_omitted_is_caught():
    cards, _, main = deck()
    r = mod.analyze([], main, mod.build_index(cards))[0]
    assert r["rejected"] and any("no commander" in x for x in r["reasons"])


def test_card_facts_hide_prices_and_game_changer_flag():
    r, facts = mod.analyze(*deck()[1:], mod.build_index(deck()[0]))
    assert facts and all(set(f) == {"name", "oracle_id", "mana_cost", "mana_value", "type_line",
                                    "oracle_text", "color_identity", "power", "toughness",
                                    "produced_mana", "keywords", "quantity", "role"} for f in facts)
    assert sum(f["quantity"] for f in facts) == 100
    assert [f["role"] for f in facts].count("commander") == 1


def test_parse_decklist_handles_plain_manabox_and_commander_block():
    text = ("// Commander\n1 Toph, the First Metalbender (TLA) 247\n\n"
            "1 Sol Ring\n1 Aang, Air Nomad (TLE) 265\n1 Archmage Emeritus (STX) 377 *F*\n"
            "3 Mountain\nnot a card line\n")
    commanders, main, bad = mod.parse_decklist(text)
    assert [c["name"] for c in commanders] == ["Toph, the First Metalbender"]
    assert commanders[0]["set"] == "tla" and commanders[0]["num"] == "247"
    assert [(m["qty"], m["name"]) for m in main] == [
        (1, "Sol Ring"), (1, "Aang, Air Nomad"), (1, "Archmage Emeritus"), (3, "Mountain")]
    assert bad == ["not a card line"]


def variant(vid, cards, features=(), tag="E", requires=(), mana_value=0, legal=True, commander_card=None):
    """A slim Spellbook variant over the given card dicts."""
    return {
        "id": vid,
        "bracket_tag": tag,
        "identity": "R",
        "cards": [{"oracle_id": c["oracle_id"], "name": c["name"], "quantity": 1,
                   "must_be_commander": commander_card is not None and c is commander_card}
                  for c in cards],
        "requires": list(requires),
        "features": list(features),
        "mana_needed": "",
        "mana_value_needed": mana_value,
        "commander_legal": legal,
        "status": "OK",
        "spoiler": False,
    }


def run_sb(extra_cards, variants, commander=COMMANDER, hazards=None, slug=None):
    cards, cmd, main = deck(extra_cards, commander)
    sb = mod.index_variants(variants)
    return mod.analyze(cmd, main, mod.build_index(cards), slug, sb, hazards)[0]


def test_classify_features_maps_spellbook_names_to_categories():
    cats = mod.classify_features(["Infinite turns", "Mass Land Denial", "Lock",
                                  "You control your opponents on each of their turns",
                                  "Target opponent skips all their future turns"])
    assert cats == {"infinite_turns", "mass_land_denial", "lock", "control_all_opponents", "skip_turns"}
    assert mod.classify_features(["You control one opponent on each of their turns"]) == {"control_some_opponents"}
    assert mod.classify_features(["Infinite creature ETB", "Skip your draw steps"]) == set()


def test_early_commander_plus_one_card_infinite_is_floor_4_and_late_is_3():
    a = card("Mindslaver", [], "Artifact")
    early = variant("v1", [COMMANDER, a], ["Infinite mana"], tag="R", mana_value=5, commander_card=COMMANDER)
    r = run_sb([a], [early])
    assert r["floor"] == 4 and not r["floor_ok_so_far"]
    assert r["spellbook"]["included_flagged"][0]["kind"].startswith("commander plus one card, early")
    late = variant("v2", [COMMANDER, a], ["Infinite mana"], tag="E", mana_value=10, commander_card=COMMANDER)
    assert run_sb([a], [late])["floor"] == 3


def test_a_lock_with_the_commander_is_a_review_note_not_a_floor():
    a = card("Mindslaver", [], "Artifact")
    r = run_sb([a], [variant("v1", [COMMANDER, a], ["Lock"], tag="E", mana_value=5, commander_card=COMMANDER)])
    assert r["floor"] == 1 and r["spellbook"]["included_flagged"][0]["kind"].startswith("review")


def test_target_bracket_four_accepts_a_floor_four_deck():
    ruination = card("Ruination", ["R"], "Sorcery", "Destroy all nonbasic lands.")
    cards, cmd, main = deck([ruination])
    index = mod.build_index(cards)
    assert not mod.analyze(cmd, main, index)[0]["floor_ok_so_far"]
    r4 = mod.analyze(cmd, main, index, target=4)[0]
    assert r4["floor"] == 4 and r4["floor_ok_so_far"] and r4["target_bracket"] == 4


def test_two_card_combo_floor_3_slow_and_4_early():
    a, b = card("Piece A", ["R"]), card("Piece B", ["R"])
    assert run_sb([a, b], [variant("v1", [a, b], ["Infinite mana"], mana_value=9)])["floor"] == 3
    assert run_sb([a, b], [variant("v1", [a, b], ["Infinite mana"], mana_value=3)])["floor"] == 4
    assert run_sb([a, b], [variant("v1", [a, b], ["Infinite mana"], mana_value=6)])["floor"] == 4
    seven = run_sb([a, b], [variant("v1", [a, b], ["Infinite mana"], mana_value=7)])
    assert seven["floor"] == 3 and "borderline" in seven["spellbook"]["included_flagged"][0]["kind"]


def test_a_finite_two_card_combo_is_not_an_infinite_combo():
    a, b = card("Value A", ["R"]), card("Value B", ["R"])
    r = run_sb([a, b], [variant("v1", [a, b], ["Draw a card each turn"], mana_value=2)])
    assert r["floor"] == 1


def test_three_card_combos_only_matter_through_their_features():
    a, b, c = card("A3", ["R"]), card("B3", ["R"]), card("C3", ["R"])
    plain = variant("v1", [a, b, c], ["Infinite creature ETB"], mana_value=4)
    assert run_sb([a, b, c], [plain])["floor"] == 1
    turns = variant("v2", [a, b, c], ["Infinite turns"], mana_value=4)
    assert run_sb([a, b, c], [turns])["floor"] == 4
    mld = variant("v3", [a, b, c], ["Mass Land Denial"], mana_value=4)
    assert run_sb([a, b, c], [mld])["floor"] == 4
    lock = variant("v4", [a, b, c], ["Lock"], mana_value=4)
    r = run_sb([a, b, c], [lock])
    assert r["floor"] == 1 and r["spellbook"]["included_flagged"][0]["kind"].startswith("review")


def test_template_requirements_make_a_variant_review_only():
    a, b = card("T1", ["R"]), card("T2", ["R"])
    r = run_sb([a, b], [variant("v1", [a, b], ["Infinite turns"], requires=["Persist Creature"])])
    assert r["floor"] == 1
    assert r["spellbook"]["included_flagged"][0]["kind"].startswith("review: template")


def test_must_be_commander_and_legality_are_enforced():
    a = card("Mindslaver", [], "Artifact")
    other = card("Other Commander", ["R"], "Legendary Creature - Human")
    wrong = variant("v1", [other, a], ["Lock"], commander_card=other)
    assert run_sb([a, other], [wrong])["floor"] == 1  # `other` is in the main deck, not the commander
    banned = variant("v2", [COMMANDER, a], ["Lock"], legal=False, commander_card=COMMANDER)
    assert run_sb([a], [banned])["floor"] == 1


def test_almost_included_lists_floor_4_variants_one_card_away():
    a, missing = card("Have It", ["R"]), card("Missing Piece", ["R"])
    v = variant("v1", [a, missing, COMMANDER], ["Infinite turns"], commander_card=COMMANDER)
    r = run_sb([a], [v])
    assert r["spellbook"]["almost_included_total"] == 1
    assert r["spellbook"]["almost_included_floor_4_features"][0]["missing"] == ["Missing Piece"]


def test_curated_hazards_match_by_commander_and_groups():
    emeria, omen = card("Emeria Shepherd", ["W"]), card("Prismatic Omen", ["G"])
    hazards = [
        {"id": "h1", "commander": "toph-the-first-metalbender", "all": ["Emeria Shepherd"],
         "any": [["Prismatic Omen", "Dryad of the Ilysian Grove"]], "floor": 4, "reason": "loop"},
        {"id": "h2", "commander": "*", "all": ["Emeria Shepherd"], "any": [], "floor": 3,
         "review_only": True, "reason": "note"},
    ]
    r = run_sb([emeria, omen], [], hazards=hazards, slug="toph-the-first-metalbender")
    assert r["floor"] == 4 and {h["hazard"] for h in r["curated_hazards"]} == {"h1", "h2"}
    assert "Dryad of the Ilysian Grove" in r["unresolved_hazard_names"]
    other = run_sb([emeria, omen], [], hazards=hazards, slug="fire-lord-azula")
    assert other["floor"] == 1 and [h["hazard"] for h in other["curated_hazards"]] == ["h2"]
    assert run_sb([emeria], [], hazards=hazards, slug="toph-the-first-metalbender")["floor"] == 1


def test_hazards_file_is_well_formed():
    hazards = mod.load_hazards()
    assert hazards, "data/hazards.json is missing or empty"
    ids = [h["id"] for h in hazards]
    assert len(ids) == len(set(ids))
    for h in hazards:
        assert h["commander"] == "*" or h["commander"] in mod.COMMANDERS, h["id"]
        assert h["floor"] in (3, 4) and h.get("reason") and h.get("source"), h["id"]
        groups = [[n] for n in h["all"]] + h["any"]
        assert groups and all(g and all(isinstance(n, str) and n for n in g) for g in groups), h["id"]


def test_pending_checks_shrink_when_spellbook_and_hazards_are_loaded():
    assert len(run()["pending_checks"]) == 3
    r = run_sb([], [], hazards=[])
    assert r["pending_checks"] == ["speed-risk flag from the Monte Carlo script (step 2.6)"]



def test_plural_extra_turn_counts_are_detected():
    stretch = card("Time Stretch", ["R"], "Sorcery", "Target player takes two extra turns after this one.")
    warp = card("Time Warp", ["R"], "Sorcery", "Target player takes an extra turn after this one.")
    r = run([stretch, warp])
    assert r["checks"]["extra_turns"]["count"] == 2 and not r["rejected"]


def test_extra_turn_card_that_returns_itself_gets_a_chain_note():
    nexus = card("Nexus of Fate", ["U"], "Instant",
                 "Take an extra turn after this one. If Nexus of Fate would be put into a graveyard "
                 "from anywhere, reveal Nexus of Fate and shuffle it into its owner's library instead.")
    r = run([nexus])
    assert any("chain candidate" in n for n in r["review_notes"])


def test_snow_basics_and_numbered_named_limits():
    snow = card("Snow-Covered Mountain", ["R"], "Basic Snow Land - Mountain", cmc=0, oracle_id="id-snow")
    hawk = card("Squadron Hawk", ["W"], "Creature - Bird",
                "A deck can have up to three cards named Squadron Hawk.")
    cards, cmd, main = deck([hawk], fillers=0)
    main[0]["qty"] = 3
    main.append({"qty": 96, "name": "Snow-Covered Mountain", "set": "", "num": ""})
    r = mod.analyze(cmd, main, mod.build_index(cards + [snow]))[0]
    assert not any("singleton" in x for x in r["reasons"]), r["reasons"]
    main[0]["qty"] = 4
    main[1]["qty"] = 95
    r = mod.analyze(cmd, main, mod.build_index(cards + [snow]))[0]
    assert any("singleton" in x for x in r["reasons"])


def test_template_variant_with_a_decisive_feature_is_review_not_dropped():
    a, b = card("T1", ["R"]), card("T2", ["R"])
    v = variant("v1", [a, b], ["Win the game"], tag="S", requires=["Card That Gives Lifelink"])
    r = run_sb([a, b], [v])
    row = r["spellbook"]["included_flagged"][0]
    assert r["floor"] == 1 and row["floor"] == 1 and row["kind"].startswith("review: template")
    assert r["review_items"] == 1


def test_commander_plus_two_cards_is_a_three_card_combo_and_sets_no_floor():
    a, b = card("C2a", ["R"]), card("C2b", ["R"])
    v = variant("v1", [COMMANDER, a, b], ["Infinite creature ETB"], mana_value=4, commander_card=COMMANDER)
    assert run_sb([a, b], [v])["floor"] == 1
    turns = variant("v2", [COMMANDER, a, b], ["Infinite turns"], mana_value=4, commander_card=COMMANDER)
    assert run_sb([a, b], [turns])["floor"] == 4


def test_spellbook_tag_disagreement_is_listed_for_review():
    a, b, c = card("R3a", ["R"]), card("R3b", ["R"]), card("R3c", ["R"])
    v = variant("v1", [a, b, c], ["Infinite card draw"], tag="R")
    r = run_sb([a, b, c], [v])
    row = r["spellbook"]["included_flagged"][0]
    assert r["floor"] == 1 and "tag R" in row["tag_note"] and r["review_items"] == 1


def test_mass_land_denial_heuristic_false_positives_and_misses():
    splendid = card("Splendid Reclamation", ["G"], "Sorcery",
                    "Return all land cards from your graveyard to the battlefield tapped.")
    balance = card("Gaea's Balance", ["G"], "Sorcery",
                   "As an additional cost to cast this spell, sacrifice five lands.")
    assert mod.mld_reason(splendid) is None and mod.mld_reason(balance) is None
    choke = card("Choke", ["G"], "Enchantment", "Islands don't untap during their controllers' untap steps.")
    stench = card("Stench of Evil", ["B"], "Sorcery", "Destroy all Plains.")
    wipe = card("Devastation", ["R"], "Sorcery", "Destroy all creatures and lands.")
    each = card("Brawl Sweep", ["R"], "Sorcery", "Each player sacrifices four lands.")
    for c in (choke, stench, wipe, each):
        assert mod.mld_reason(c), c["name"]


def test_foil_marker_without_a_set_and_non_creature_commander():
    text = "// Commander" + chr(10) + "1 Test Commander" + chr(10) + chr(10) + "1 Sol Ring *F*" + chr(10)
    commanders, main, bad = mod.parse_decklist(text)
    assert [m["name"] for m in main] == ["Sol Ring"] and not bad
    artifact = card("Legendary Relic", [], "Legendary Artifact")
    r = run([], commander=artifact)
    assert any("commander is not" in x for x in r["reasons"])


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
