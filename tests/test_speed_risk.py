"""Offline tests for scripts/speed_risk.py (no network, small synthetic decks)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("speed_risk", SCRIPTS / "speed_risk.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def fact(name, type_line="Creature - Human", text="", cmc=2, power="2", quantity=1,
         role="main", oid=None, produced=()):
    return {"name": name, "oracle_id": oid or f"oid-{name}", "mana_cost": "", "mana_value": cmc,
            "type_line": type_line, "oracle_text": text, "color_identity": [], "power": power,
            "toughness": "2", "produced_mana": list(produced), "keywords": [],
            "quantity": quantity, "role": role}


def vanilla_deck(commander=None, extra=()):
    facts = [fact("Mountain", "Basic Land - Mountain", "({T}: Add {R}.)", 0, None, 36, produced=["R"])]
    facts += list(extra)
    used = sum(f["quantity"] for f in facts)
    filler = 99 - used
    facts += [fact(f"Bear {i}", power="2") for i in range(filler)]
    facts.append(commander or fact("Plain Commander", cmc=3, power="3", role="commander"))
    return facts


def test_band_thresholds():
    assert [mod.band(p) for p in (0.0, 0.099, 0.10, 0.25, 0.30, 0.399, 0.40, 0.9)] == [
        "very low", "very low", "low", "medium", "high", "high", "very high", "very high"]


def test_model_card_reads_the_numbers_the_goldfish_uses():
    sol = mod.model_card(fact("Sol Ring", "Artifact", "{T}: Add {C}{C}.", 1, None))
    assert sol["mana"] == 2 and not sol["land"]
    ritual = mod.model_card(fact("Dark Ritual", "Instant", "Add {B}{B}{B}.", 1, None))
    assert ritual["gain"] == 3 and ritual["spell"]
    ramp = mod.model_card(fact(
        "Rampant Growth", "Sorcery",
        "Search your library for a basic land card, put that card onto the battlefield tapped, "
        "then shuffle.", 2, None))
    assert ramp["ramp"] == 1 and not ramp["tutor"]
    divination = mod.model_card(fact("Divination", "Sorcery", "Draw two cards.", 3, None))
    assert divination["draw"] == 2
    tutor = mod.model_card(fact("Demonic Tutor", "Sorcery",
                                "Search your library for a card, put that card into your hand.", 2, None))
    assert tutor["tutor"] and tutor["ramp"] == 0
    haste = mod.model_card(fact("Hasty", text="Haste", power="4"))
    assert haste["haste"] and haste["power"] == 4
    tapped = mod.model_card(fact("Tapland", "Land", "Tapland enters tapped.\n{T}: Add {G}.", 0, None))
    assert tapped["tapped"] and tapped["mana"] == 1
    star = mod.model_card(fact("Star", power="*"))
    assert star["power"] == 0


def test_a_deck_of_bears_and_lands_is_very_low():
    result = mod.simulate(vanilla_deck(), trials=1500)
    assert result["level"] == "very low" and result["frequency"] == 0.0
    assert result["library_cards"] == 99 and result["commander"] == "Plain Commander"


def test_a_hasty_big_commander_threatens_by_commander_damage():
    commander = fact("Hasty Giant", cmc=3, power="7", text="Haste", role="commander")
    result = mod.simulate(vanilla_deck(commander), trials=1500)
    assert result["level"] == "very high" and result["frequency"] > 0.6


def test_combos_raise_the_frequency_and_the_same_seed_repeats():
    extra, combos = [], []
    for i in range(20):  # 20 disjoint two-card combos of one-mana pieces
        a = fact(f"Piece A{i}", "Artifact", "", 1, None, oid=f"a{i}")
        b = fact(f"Piece B{i}", "Artifact", "", 1, None, oid=f"b{i}")
        extra += [a, b]
        combos.append((frozenset({f"a{i}", f"b{i}"}), 2))
    facts = vanilla_deck(None, extra)
    base = mod.simulate(vanilla_deck(None, extra), trials=3000, seed=7)
    original = mod.decisive_combos
    mod.decisive_combos = lambda f, s: combos
    try:
        with_combos = mod.simulate(facts, trials=3000, seed=7)
        again = mod.simulate(facts, trials=3000, seed=7)
    finally:
        mod.decisive_combos = original
    assert base["frequency"] == 0.0
    assert with_combos["frequency"] > 0.05
    assert with_combos == again
    assert with_combos["decisive_combos_in_deck"] == 20


def test_decisive_combos_use_features_templates_and_deck_membership():
    variants = [
        {"id": "v1", "cards": [{"oracle_id": "x", "name": "X", "must_be_commander": False},
                               {"oracle_id": "y", "name": "Y", "must_be_commander": False}],
         "requires": [], "features": ["Infinite damage"], "mana_value_needed": 3,
         "commander_legal": True},
        {"id": "v2", "cards": [{"oracle_id": "x", "name": "X", "must_be_commander": False},
                               {"oracle_id": "z", "name": "Z", "must_be_commander": False}],
         "requires": [], "features": ["Infinite creature ETB"], "mana_value_needed": 2,
         "commander_legal": True},
        {"id": "v3", "cards": [{"oracle_id": "x", "name": "X", "must_be_commander": False}],
         "requires": ["Persist Creature"], "features": ["Win the game"], "mana_value_needed": 1,
         "commander_legal": True},
    ]
    sb = mod.la.index_variants(variants)
    facts = [fact("X", oid="x"), fact("Y", oid="y"), fact("Z", oid="z")]
    combos = mod.decisive_combos(facts, sb)
    assert combos == [(frozenset({"x", "y"}), 3)]
    assert mod.decisive_combos(facts, None) == []


def test_enters_the_battlefield_ramp_on_a_creature_is_applied():
    ramp_text = ("When Ramp Bear enters the battlefield, search your library for a basic land card, "
                 "put it onto the battlefield tapped, then shuffle.")
    commander = fact("Big Hasty", cmc=5, power="21", text="Haste", role="commander")

    def deck_with(text):
        facts = [fact("Forest", "Basic Land - Forest", "({T}: Add {G}.)", 0, None, 40, produced=["G"])]
        facts += [fact(f"Bear {i}", text=text, power="0" if not text else "1") for i in range(58)]
        facts.append(commander)
        return facts

    plain = mod.simulate(deck_with(""), trials=3000, seed=3)
    ramped = mod.simulate(deck_with(ramp_text), trials=3000, seed=3)
    assert mod.model_card(fact("Ramp Bear", text=ramp_text, power="1"))["ramp"] == 1
    assert ramped["frequency"] > plain["frequency"] + 0.02


def test_a_commander_every_player_takes_over_and_grows_is_a_clock_by_itself():
    text = ("Trample\nAlexios attacks each combat if able, can't be sacrificed, and can't attack its owner.\n"
            "At the beginning of each player's upkeep, that player gains control of Alexios, untaps it, "
            "and puts a +1/+1 counter on it. It gains haste until end of turn.")
    rotating = fact("Rotator", cmc=4, power="4", text=text, role="commander")
    plain = fact("Plain Four", cmc=4, power="4", text="Trample", role="commander")

    def deck(commander):
        facts = [fact("Mountain", "Basic Land - Mountain", "({T}: Add {R}.)", 0, None, 40, produced=["R"])]
        facts += [fact(f"Blank {i}", "Artifact", "", 9, None) for i in range(59)]
        facts.append(commander)
        return facts

    assert mod.model_card(rotating)["rotates"] and mod.model_card(rotating)["grows"]
    assert not mod.model_card(plain)["rotates"]
    clock = mod.simulate(deck(rotating), trials=3000, seed=11)
    alone = mod.simulate(deck(plain), trials=3000, seed=11)
    assert alone["frequency"] == 0.0  # 4 power, own turn only: 8 damage by turn 6
    assert clock["frequency"] > 0.5 and clock["level"] == "very high"
    # Cast on turn 4 it needs 21 by the opponent turns after turn 5 (the 4 attacks are worth
    # 5/2 + 7/2 = 6 in round one and 8 + 9/2 + 11/2 = 16 in round two).
    assert clock["cumulative_by_turn"]["4"] == 0.0


def test_main_skips_a_stale_card_facts_file():
    import contextlib
    import io
    import json
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        stale = [{"name": "Sol Ring", "oracle_id": "x", "mana_value": 1, "type_line": "Artifact",
                  "oracle_text": "", "color_identity": []}]  # no quantity, role, power or keywords
        (folder / "old-deck.cards.json").write_text(json.dumps(stale), encoding="utf-8")
        old = mod.DECKS
        mod.DECKS = folder
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                mod.main()
        finally:
            mod.DECKS = old
        assert "SKIPPED" in out.getvalue()
        assert not list(folder.glob("*.speed_risk.json"))


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
