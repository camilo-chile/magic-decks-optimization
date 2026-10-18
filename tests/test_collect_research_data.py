"""Offline tests for the pure logic of scripts/collect_research_data.py (no network)."""
import gzip
import importlib.util
import json
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "collect_research_data.py"
spec = importlib.util.spec_from_file_location("collect_research_data", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_iter_cards_reads_jsonl_gzip_and_array():
    cards = [{"name": "A"}, {"name": "B"}]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        jsonl = tmp / "cards.jsonl"
        jsonl.write_text("\n".join(json.dumps(c) for c in cards) + "\n", encoding="utf-8")
        gz = tmp / "cards.jsonl.gz"
        with gzip.open(gz, "wt", encoding="utf-8") as fh:
            fh.write(jsonl.read_text(encoding="utf-8"))
        array = tmp / "cards.json"
        array.write_text(json.dumps(cards), encoding="utf-8")
        # A gzip file with a misleading extension must still be detected by its bytes.
        disguised = tmp / "plain.jsonl.gz"
        disguised.write_text(jsonl.read_text(encoding="utf-8"), encoding="utf-8")
        for path in (jsonl, gz, array, disguised):
            assert [c["name"] for c in mod.iter_cards(path)] == ["A", "B"], path.name


def test_eta_text_handles_zero_progress():
    assert mod.eta_text(0, 10, 0) == "ETA ?"


def test_sha256_of_matches_a_known_digest():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "x.txt"
        path.write_bytes(b"abc")
        assert mod.sha256_of(path) == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
