"""Offline tests for scripts/validate_deck_export.py (no network: every run uses offline=True)."""
import argparse
import contextlib
import importlib.util
import io
import json
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("validate_deck_export", SCRIPTS / "validate_deck_export.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

HEADER = ("Binder Name,Binder Type,Name,Set code,Set name,Collector number,Foil,Rarity,Quantity,"
          "ManaBox ID,Scryfall ID,Purchase price,Misprint,Altered,Signed,Condition,Language,Proxy,"
          "Purchase price currency,Added")


def csv_row(binder, btype, name, set_code, num, qty=1, lang="en", foil="normal"):
    return (f"{binder},{btype},{name},{set_code},Set,{num},{foil},rare,{qty},1,sid,0,false,false,false,"
            f"near_mint,{lang},false,USD,2026-10-12")


def deck_text(n_filler=98, commander_num="1"):
    lines = ["// COMMANDER", f"1 Test Commander (tst) {commander_num}", ""]
    lines += [f"1 Filler {i:03d} (tst) {i + 10}" for i in range(n_filler)]
    lines += ["1 Mountain (tst) 300 *F*"]
    return "\n".join(lines) + "\n"


def csv_text(n_filler=98, extra=()):
    rows = [csv_row("Test", "deck", "Test Commander", "tst", "1")]
    rows += [csv_row("Test", "deck", f"Filler {i:03d}", "tst", str(i + 10),
                     lang="es" if i == 0 else "en") for i in range(n_filler)]
    rows += [csv_row("Test", "deck", "Mountain", "tst", "300", foil="foil")]
    rows += list(extra)
    return HEADER + "\n" + "\n".join(rows) + "\n"


def run(deck, csv, deck_name="Test"):
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        (folder / "deck.txt").write_text(deck, encoding="utf-8")
        (folder / "c.csv").write_text(csv, encoding="utf-8")
        args = argparse.Namespace(deck=str(folder / "deck.txt"), csv=str(folder / "c.csv"),
                                  deck_name=deck_name, offline=True, out=str(folder / "out.json"))
        with contextlib.redirect_stdout(io.StringIO()):
            problems = mod.validate(args)
        report = json.loads((folder / "out.json").read_text(encoding="utf-8"))
    return problems, report


def test_basic_land_and_front_face_helpers():
    assert mod.is_basic("Mountain") and mod.is_basic("Snow-Covered Island") and mod.is_basic("Wastes")
    assert not mod.is_basic("Command Tower")
    assert mod.front("Fire // Ice") == "fire"


def test_a_matching_deck_and_csv_has_no_problems_and_counts_languages():
    problems, report = run(deck_text(), csv_text())
    assert problems == [], problems
    assert report["total_cards"] == 100 and report["commanders"] == ["Test Commander"]
    assert report["spanish_copies"] == 1 and report["english_copies"] == 99
    assert report["csv_foil"] == {"normal": 99, "foil": 1}  # the *F* marker did not break parsing
    assert report["mode"] == "offline"


def test_wrong_totals_unparsed_lines_and_singleton_are_reported():
    problems, _ = run(deck_text(n_filler=97), csv_text(n_filler=97))
    assert any("total is 99" in p for p in problems)
    text = deck_text() + "this is not a card line\n1 Filler 000 (tst) 99\n"
    problems, _ = run(text, csv_text())
    assert any("unparsed" in p for p in problems)
    assert any("singleton" in p for p in problems)


def test_text_and_csv_must_list_the_same_printings():
    other = csv_text().replace("tst,Set,12,", "tst,Set,9999,", 1)
    problems, _ = run(deck_text(), other)
    assert any("text and CSV differ" in p for p in problems), problems


def test_a_binder_with_the_deck_name_does_not_merge_into_the_deck():
    extra = [csv_row("Test", "binder", "Extra Card", "tst", "777")]
    problems, report = run(deck_text(), csv_text(extra=extra))
    assert problems == [], problems
    assert report["csv_deck_rows"] == 100
    assert report["binders_in_csv"]["binder:Test"] == 1


def test_languages_other_than_english_and_spanish_are_a_problem():
    german = csv_text().replace(",en,false,USD", ",de,false,USD", 1)
    problems, _ = run(deck_text(), german)
    assert any("languages other than en/es" in p for p in problems), problems


def test_missing_deck_rows_point_to_the_binder_names():
    problems, report = run(deck_text(), csv_text(), deck_name="Nope")
    assert any("no CSV rows" in p for p in problems)
    assert "deck:Test" in report["binders_in_csv"]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
