"""Golden tests of Layer A on the real decks and the real card database.

They need data that is not in git (the Scryfall bulk file, the Spellbook slim file and the
owner's deck exports), so every test is skipped, with a message, when something is missing.
Expected values are the outcomes the project recorded on 2026-10-12.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("layer_a", SCRIPTS / "layer_a.py")
la = importlib.util.module_from_spec(spec)
spec.loader.exec_module(la)

TOPH = ROOT / "data" / "raw" / "Toph.txt"
AZULA = ROOT / "data" / "raw" / "Azula.txt"
ALEXIOS = ROOT / "evals" / "anchors" / "alexios-deimos-of-kosmos.reference.txt"
_cache = {}


def environment():
    """(index, spellbook, hazards) or None when the local data is missing."""
    if "env" not in _cache:
        bulk = la.latest_bulk()
        if bulk is None or not la.SPELLBOOK_SLIM.exists():
            _cache["env"] = None
        else:
            _cache["env"] = (la.build_index(list(la.iter_cards(bulk))), la.load_spellbook(),
                             la.load_hazards())
    return _cache["env"]


def analyze(path, slug, text=None, target=None):
    index, spellbook, hazards = environment()
    commanders, main, bad = la.parse_decklist(text if text is not None else path.read_text(encoding="utf-8-sig"))
    assert not bad, bad
    target = target or la.TARGET_BRACKET.get(slug, la.DEFAULT_TARGET)
    return la.analyze(commanders, main, index, slug, spellbook, hazards, target)[0]


def swapped(path, remove, add):
    """The deck text with the `remove` card names replaced by the `add` names."""
    text = path.read_text(encoding="utf-8-sig")
    for out, new in zip(remove, add):
        assert f"1 {out}\n" in text + "\n", out
        text = text.replace(f"1 {out}\n", f"1 {new}\n", 1)
    return text


def skip_if_missing(*paths):
    if environment() is None or any(not p.exists() for p in paths):
        print("   skipped: local data missing")
        return True
    return False


def test_toph_current_list_is_floor_3_with_late_bumi_ashaya_and_two_review_locks():
    if skip_if_missing(TOPH):
        return
    r = analyze(TOPH, "toph-the-first-metalbender")
    assert r["recognized_cards"] == 100 and not r["rejected"]
    assert r["floor"] == 3 and r["floor_ok_so_far"] and r["target_bracket"] == 3
    assert r["checks"]["game_changers"]["cards"] == ["Crop Rotation"]
    rows = {tuple(sorted(x["cards"])): x for x in r["spellbook"]["included_flagged"]}
    bumi = rows[("Ashaya, Soul of the Wild", "Bumi, Unleashed")]
    assert bumi["floor"] == 3 and bumi["kind"].endswith("late")
    locks = [x for x in rows.values() if x["kind"].startswith("review")]
    assert {"Mindslaver", "The Stasis Coffin"} == {c for x in locks for c in x["cards"]} - {
        "Toph, the First Metalbender"}


def test_azula_current_list_is_floor_1_with_nothing_flagged():
    if skip_if_missing(AZULA):
        return
    r = analyze(AZULA, "fire-lord-azula")
    assert r["recognized_cards"] == 100 and r["floor"] == 1 and r["floor_ok_so_far"]
    assert r["spellbook"]["included_flagged"] == [] and r["review_items"] == 0


def test_alexios_reference_is_floor_3_from_exactly_three_game_changers():
    if skip_if_missing(ALEXIOS):
        return
    r = analyze(ALEXIOS, "alexios-deimos-of-kosmos")
    assert r["recognized_cards"] == 100 and not r["rejected"] and r["floor"] == 3
    assert r["checks"]["game_changers"]["cards"] == ["Ancient Tomb", "Jeska's Will", "The One Ring"]
    assert r["spellbook"]["included_flagged"] == []
    assert not [h for h in r.get("curated_hazards", []) if not h["review_only"]]


def test_four_extra_turn_cards_make_the_reference_floor_4():
    if skip_if_missing(ALEXIOS):
        return
    text = swapped(ALEXIOS, ["Mind Stone", "Thought Vessel", "Arcane Signet", "Thran Dynamo"],
                   ["Final Fortune", "Last Chance", "Warrior's Oath", "Magistrate's Scepter"])
    r = analyze(ALEXIOS, "alexios-deimos-of-kosmos", text)
    assert r["checks"]["extra_turns"]["count"] == 4 and r["floor"] == 4 and not r["floor_ok_so_far"]


def test_blood_moon_makes_the_reference_floor_4_through_mass_land_denial():
    if skip_if_missing(ALEXIOS):
        return
    text = swapped(ALEXIOS, ["Mind Stone"], ["Blood Moon"])
    r = analyze(ALEXIOS, "alexios-deimos-of-kosmos", text)
    assert "Blood Moon" in r["checks"]["mass_land_denial"]["cards"] and r["floor"] == 4


def test_a_fourth_game_changer_is_floor_4_and_target_4_accepts_it():
    if skip_if_missing(ALEXIOS):
        return
    text = swapped(ALEXIOS, ["Mind Stone"], ["Mana Vault"])
    r3 = analyze(ALEXIOS, "alexios-deimos-of-kosmos", text)
    assert r3["floor"] == 4 and not r3["floor_ok_so_far"]
    r4 = analyze(ALEXIOS, "alexios-deimos-of-kosmos", text, target=4)
    assert r4["floor_ok_so_far"]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
