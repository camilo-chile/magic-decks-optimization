"""Offline tests for scripts/backup_collection.py (no network)."""
import importlib.util
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
spec = importlib.util.spec_from_file_location("backup_collection", SCRIPTS / "backup_collection.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

ROWS = [
    {"binder name": "Spanish Cards", "binder type": "binder", "quantity": "2", "language": "es"},
    {"binder name": "English Cards", "binder type": "binder", "quantity": "3", "language": "en"},
    {"binder name": "Toph", "binder type": "deck", "quantity": "1", "language": "es"},
]
EXPECTED = {"total": 6, "binders": {"Spanish Cards": 2, "English Cards": 3}}


def test_counts_and_checks_pass_on_a_consistent_export():
    counts = mod.count_collection(ROWS)
    assert counts["total"] == 6 and counts["by_language"] == {"es": 3, "en": 3}
    checks = mod.check_collection(counts, EXPECTED)
    assert all(ok for ok, _ in checks), checks


def test_checks_flag_a_wrong_language_and_a_missing_copy():
    rows = ROWS + [{"binder name": "English Cards", "binder type": "binder", "quantity": "1", "language": "es"}]
    checks = mod.check_collection(mod.count_collection(rows), EXPECTED)
    bad = [text for ok, text in checks if not ok]
    assert any("total copies 7" in t for t in bad) and any("not marked English: 1" in t for t in bad)


def test_verify_folder_detects_changed_missing_and_extra_files():
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        (folder / "a.csv").write_text("one", encoding="utf-8")
        (folder / "b.txt").write_text("two", encoding="utf-8")
        mod.write_sums(folder, ["a.csv", "b.txt"])
        assert mod.verify_folder(folder) == []
        (folder / "a.csv").write_text("changed", encoding="utf-8")
        (folder / "b.txt").unlink()
        (folder / "c.txt").write_text("new", encoding="utf-8")
        problems = mod.verify_folder(folder)
    assert "DIFFERENT: a.csv" in problems and "missing: b.txt" in problems and "not in the list: c.txt" in problems


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
