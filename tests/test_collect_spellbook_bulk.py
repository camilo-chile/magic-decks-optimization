"""Offline tests for the pure logic of scripts/collect_spellbook_bulk.py (no network)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("collect_spellbook_bulk", SCRIPTS / "collect_spellbook_bulk.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_slim_variant_keeps_the_fields_layer_a_needs():
    variant = {
        "id": "1-2",
        "bracketTag": "R",
        "identity": "WU",
        "status": "OK",
        "spoiler": False,
        "manaNeeded": "{2}{U}",
        "manaValueNeeded": 3,
        "legalities": {"commander": True, "brawl": False},
        "uses": [
            {"card": {"id": 1, "oracleId": "oid-a", "name": "Card A", "imageUriFrontPng": "x"},
             "quantity": 1, "mustBeCommander": True},
            {"card": {"id": 2, "oracleId": "oid-b", "name": "Card B"}},
        ],
        "requires": [{"template": {"name": "Sacrifice outlet"}}],
        "produces": [{"feature": {"name": "Infinite turns"}, "quantity": 1}, {"feature": {}}],
        "description": "long text that must not be copied",
    }
    out = mod.slim_variant(variant)
    assert out["id"] == "1-2" and out["bracket_tag"] == "R" and out["commander_legal"] is True
    assert [c["oracle_id"] for c in out["cards"]] == ["oid-a", "oid-b"]
    assert out["cards"][0]["must_be_commander"] is True and out["cards"][1]["quantity"] == 1
    assert out["requires"] == ["Sacrifice outlet"]
    assert out["features"] == ["Infinite turns"]
    assert out["mana_value_needed"] == 3 and "description" not in out


def test_read_bulk_streams_variants_from_gzip_and_plain_json():
    import gzip
    import json
    import tempfile

    doc = {"timestamp": "2026-10-10T03:11:56+00:00", "version": "7.1.9",
           "variants": [{"id": "a", "uses": []}, {"id": "b", "uses": [{"card": {"oracleId": "x"}}]}],
           "aliases": [{"id": "z", "variant": None}]}
    raw = json.dumps(doc, indent=1)
    with tempfile.TemporaryDirectory() as tmp:
        plain = Path(tmp) / "plain.json.gz"  # wrong extension on purpose: bytes decide
        plain.write_text(raw, encoding="utf-8")
        packed = Path(tmp) / "packed.json.gz"
        with gzip.open(packed, "wt", encoding="utf-8") as fh:
            fh.write(raw)
        for path in (plain, packed):
            meta, variants = mod.read_bulk(path)
            assert meta == {"timestamp": "2026-10-10T03:11:56+00:00", "version": "7.1.9"}
            assert [v["id"] for v in variants] == ["a", "b"]


def test_slim_variant_tolerates_missing_parts():
    out = mod.slim_variant({"id": "x"})
    assert out["cards"] == [] and out["requires"] == [] and out["features"] == []
    assert out["commander_legal"] is None and out["spoiler"] is False


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
