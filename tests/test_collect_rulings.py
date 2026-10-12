"""Offline tests for the pure logic of scripts/collect_rulings.py (no network)."""
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))  # collect_rulings imports collect_research_data by name
spec = importlib.util.spec_from_file_location("collect_rulings", SCRIPTS / "collect_rulings.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def ruling(oracle_id, comment, source="wotc", date="2024-01-01"):
    return {"object": "ruling", "oracle_id": oracle_id, "source": source,
            "published_at": date, "comment": comment}


def test_load_pool_names_reads_every_pool_file():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "pool_a.jsonl").write_text(
            json.dumps({"oracle_id": "id-1", "name": "Sol Ring"}) + "\n"
            + json.dumps({"oracle_id": "id-2", "name": "Mox Amber"}) + "\n", encoding="utf-8")
        (tmp / "pool_b.jsonl").write_text(
            json.dumps({"oracle_id": "id-2", "name": "Mox Amber"}) + "\n"
            + json.dumps({"oracle_id": None, "name": "No Id"}) + "\n\n", encoding="utf-8")
        (tmp / "spellbook_a.json").write_text("{}", encoding="utf-8")  # not a pool file
        assert mod.load_pool_names(tmp) == {"id-1": "Sol Ring", "id-2": "Mox Amber"}


def test_filter_rulings_keeps_only_pool_cards_and_adds_names():
    names = {"id-1": "Sol Ring"}
    rulings = [ruling("id-1", "A"), ruling("id-9", "B"), ruling("id-1", "C"), {"comment": "no id"}]
    kept, total = mod.filter_rulings(iter(rulings), names)
    assert total == 4
    assert [r["comment"] for r in kept] == ["A", "C"]
    assert kept[0] == {"name": "Sol Ring", "oracle_id": "id-1", "source": "wotc",
                       "published_at": "2024-01-01", "comment": "A"}


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
