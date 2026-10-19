"""Offline tests for scripts/deck_stats.py (no network, no files written)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
spec = importlib.util.spec_from_file_location("deck_stats", SCRIPTS / "deck_stats.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def card(name, type_line, mana_cost="", cmc=0.0, colors=(), produced=(), text="", identity=()):
    return {"name": name, "type_line": type_line, "mana_cost": mana_cost, "cmc": cmc, "colors": list(colors),
            "produced_mana": list(produced), "oracle_text": text, "color_identity": list(identity)}


CARDS = {c["name"].lower(): c for c in [
    card("Boss", "Legendary Creature — Human Assassin", "{1}{B}", 2.0, "B", text="Menace", identity="B"),
    card("Swamp", "Basic Land — Swamp", produced="B", text="({T}: Add {B}.)", identity="B"),
    card("Dual", "Land", produced="BR", text="This land enters tapped.\n{T}: Add {B} or {R}."),
    card("Check", "Land", produced="BR", text="This land enters tapped unless you control a Swamp or a Mountain.\n{T}: Add {B} or {R}."),
    card("Tower", "Land", produced="WUBRG", text="{T}: Add one mana of any color in your commander's color identity."),
    card("Rock", "Artifact", "{2}", 2.0, produced="C", text="{T}: Add {C}."),
    card("Hybrid", "Instant", "{B/R}{B/R}", 2.0, "BR", text="Destroy target creature."),
    card("Gold", "Artifact Creature — Construct", "{1}{B}{R}", 3.0, "BR", text="Draw a card."),
    card("Wrath", "Sorcery", "{2}{B}{B}", 4.0, "B", text="Destroy all creatures."),
    card("Seeker", "Sorcery", "{1}{B}", 2.0, "B", text="Search your library for a card, put it into your hand, then shuffle."),
    card("Growth", "Sorcery", "{1}{G}", 2.0, "G", text="Search your library for a basic land card, put it onto the battlefield tapped."),
]}


def test_parse_list_reads_commander_and_main_and_front_faces():
    commanders, entries = mod.parse_list("// Commander\n1 Boss\n\n// Main\n1 Rock\n2 Swamp\n1 Bonecrusher Giant // Stomp\n")
    assert commanders == ["Boss"] and entries == [(1, "Rock"), (2, "Swamp"), (1, "Bonecrusher Giant")]


def test_pips_count_each_color_of_a_hybrid_symbol_and_curve_groups_colors():
    stats = mod.compute(["Boss"], [(1, "Hybrid"), (1, "Gold"), (1, "Rock"), (2, "Swamp")], CARDS)
    assert stats["pips"]["B"] == 1 + 2 + 1 and stats["pips"]["R"] == 2 + 1  # Boss {B}, Hybrid {B/R}{B/R}, Gold {B}{R}
    assert stats["curve"][("2", "B")] == 1 and stats["curve"][("2", "M")] == 1 and stats["curve"][("2", "C")] == 1
    assert stats["curve"][("3", "M")] == 1 and stats["nonland"] == 4 and stats["avg_mv"] == 2.25


def test_production_is_limited_to_the_commander_colors_and_lands_stay_apart_from_rocks():
    stats = mod.compute(["Boss"], [(1, "Dual"), (1, "Tower"), (1, "Rock"), (1, "Swamp")], CARDS)
    assert stats["identity"] == ["B"]
    assert stats["production"]["B"] == {"lands": 3, "other": 0}  # Dual, Tower, Swamp: only black counts for a black commander
    assert stats["production"]["C"] == {"lands": 0, "other": 1}


def test_land_entry_tells_tapped_from_conditional_and_untapped():
    assert mod.land_entry(CARDS["dual"]) == "tapped" and mod.land_entry(CARDS["check"]) == "conditional"
    assert mod.land_entry(CARDS["swamp"]) == "untapped" and mod.land_entry(CARDS["tower"]) == "untapped"


def test_roles_read_the_rules_text_and_types_count_once_per_type():
    assert mod.roles(CARDS["rock"]) == {"ramp"} and mod.roles(CARDS["hybrid"]) == {"removal"}
    assert mod.roles(CARDS["gold"]) == {"draw"} and mod.roles(CARDS["wrath"]) == {"sweeper"}
    assert mod.roles(CARDS["seeker"]) == {"tutor"} and mod.roles(CARDS["growth"]) == {"ramp"}  # a land search is ramp, not a tutor
    assert mod.type_set(CARDS["gold"]) == {"Artifact", "Creature"} and mod.subtypes(CARDS["boss"]) == ["Human", "Assassin"]


def test_odds_use_the_hypergeometric_law_and_grow_with_the_turn():
    assert mod.hypergeom_at_least_one(99, 0, 10) == 0.0 and mod.hypergeom_at_least_one(99, 99, 10) == 1.0
    stats = mod.compute(["Boss"], [(1, "Dual")] * 1 + [(1, "Rock")] + [(2, "Swamp")], CARDS)
    chances = {(o["color"], o["turn"]): o["chance"] for o in stats["odds"]}
    assert chances[("B", 3)] <= chances[("B", 5)] <= chances[("B", 7)]


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
