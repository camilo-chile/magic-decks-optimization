"""Offline tests for the pure helpers of scripts/price_candidates.py (no network, no caches)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("price_candidates", SCRIPTS / "price_candidates.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_face_text_reads_a_one_faced_card():
    assert mod.face_text({"oracle_text": "Draw a card."}, "oracle_text") == "Draw a card."


def test_face_text_joins_the_faces_of_a_two_faced_card():
    card = {"card_faces": [{"oracle_text": "Front.", "mana_cost": "{1}{R}"}, {"oracle_text": "Back.", "mana_cost": ""}]}
    assert mod.face_text(card, "oracle_text") == "Front. // Back."
    assert mod.face_text(card, "mana_cost") == "{1}{R} // "


def test_face_text_of_a_card_without_the_field_is_empty():
    assert mod.face_text({"name": "Island"}, "oracle_text") == ""


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
