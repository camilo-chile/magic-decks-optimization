"""Offline tests for scripts/check_phase2_bracket.py (synthetic oracle cards, no bulk file)."""
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import check_phase2_bracket as cb  # noqa: E402
import layer_a as la  # noqa: E402


def card(name, identity=("R",), type_line="Artifact", text="", gc=False, layout="normal"):
    return {"name": name, "oracle_id": f"id-{name}", "type_line": type_line, "oracle_text": text, "cmc": 2,
            "color_identity": list(identity), "game_changer": gc, "legalities": {"commander": "legal"}, "mana_cost": "{1}",
            "layout": layout, "prices": {"usd": "1.00"}}


COMMANDER = card("Test Commander", type_line="Legendary Creature - Human")
FILLERS = [card(f"Filler {i:03d}") for i in range(99)]


def write_list(directory, extra=None):
    """A 100-card list: the commander plus 99 fillers, one of them replaced by `extra` cards when given."""
    names = [c["name"] for c in FILLERS]
    if extra:
        names = [c["name"] for c in extra] + names[len(extra):]
    text = "// Commander\n1 Test Commander\n\n" + "".join(f"1 {n}\n" for n in names)
    path = Path(directory) / "demo.txt"
    path.write_text(text, encoding="utf-8")
    return path


def run(extra=None):
    cards = [COMMANDER] + FILLERS + list(extra or [])
    index = la.build_index(cards)
    with tempfile.TemporaryDirectory() as tmp:
        path = write_list(tmp, extra)
        slug, report, reversible = cb.check_file(path, index, None, None, Path(tmp) / "reports")
        text = (Path(tmp) / "reports" / "bracket-demo.md").read_text(encoding="utf-8")
    return slug, report, reversible, text


def test_a_clean_bracket_3_list_passes_and_the_report_is_written():
    slug, report, reversible, text = run()
    assert slug == "demo" and cb.verdict(report) == "PASS" and reversible == []
    assert text.startswith("# Bracket check: demo (PASS)") and "- Game Changers (0): none" in text


def test_a_reversible_card_rejects_the_list():
    flipper = card("Flip Walker", type_line="Creature", layout="transform")
    slug, report, reversible, text = run([flipper])
    assert cb.verdict(report) == "FAIL" and reversible == ["Flip Walker"]
    assert "reversible cards: Flip Walker" in report["reasons"] and "(FAIL)" in text.splitlines()[0]


def test_game_changers_are_reported_by_name():
    changer = card("Big Changer", gc=True)
    slug, report, reversible, text = run([changer])
    assert report["checks"]["game_changers"]["cards"] == ["Big Changer"] and "- Game Changers (1): Big Changer" in text


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
