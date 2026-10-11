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


def card(name, identity, commander="legal", layout="normal", **extra):
    base = {
        "id": name,
        "name": name,
        "color_identity": identity,
        "legalities": {"commander": commander},
        "layout": layout,
        "oversized": False,
    }
    base.update(extra)
    return base


def test_is_pool_card_filters_legality_layout_and_oversized():
    assert mod.is_pool_card(card("Sol Ring", []))
    assert not mod.is_pool_card(card("Banned Card", [], commander="banned"))
    assert not mod.is_pool_card(card("Not Legal", [], commander="not_legal"))
    assert not mod.is_pool_card(card("Goblin Token", ["R"], layout="token"))
    assert not mod.is_pool_card(card("Giant Card", [], oversized=True))


def test_build_pool_uses_color_identity_subset():
    cards = [
        mod.trim(card("Colorless", [])),
        mod.trim(card("Red", ["R"])),
        mod.trim(card("Red-Green", ["R", "G"])),
        mod.trim(card("Blue", ["U"])),
    ]
    names = {c["name"] for c in mod.build_pool(cards, ["R"])}
    assert names == {"Colorless", "Red"}
    names = {c["name"] for c in mod.build_pool(cards, ["R", "G", "W"])}
    assert names == {"Colorless", "Red", "Red-Green"}


def test_trim_keeps_faces_and_drops_prices():
    raw = card(
        "Front // Back",
        ["R"],
        prices={"usd": "1.00"},
        image_uris={"small": "x"},
        card_faces=[
            {"name": "Front", "mana_cost": "{R}", "type_line": "Creature", "oracle_text": "a", "x": 1},
            {"name": "Back", "mana_cost": "", "type_line": "Land", "oracle_text": "b"},
        ],
    )
    out = mod.trim(raw)
    assert "prices" not in out and "image_uris" not in out
    assert [f["name"] for f in out["card_faces"]] == ["Front", "Back"]
    assert "x" not in out["card_faces"][0]


def test_iter_cards_reads_jsonl_gzip_and_array():
    cards = [card("A", []), card("B", ["R"])]
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


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
