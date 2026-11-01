"""Offline tests for scripts/edhrec_data.py (a fake EDHREC: no network)."""
import json
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import edhrec_data as ed  # noqa: E402

PAGE = {"container": {"json_dict": {"cardlists": [
    {"header": "Top Cards", "cardviews": [{"name": "Eagle Vision", "synergy": 0.42, "num_decks": 900, "potential_decks": 1000},
                                          {"name": "Sol Ring", "synergy": -0.01, "num_decks": 950, "potential_decks": 1000}]},
    {"header": "Creatures", "cardviews": [{"name": "Eagle Vision", "synergy": 0.42, "num_decks": 900, "potential_decks": 1000},
                                          {"name": "Odd Card", "synergy": 0.1, "num_decks": 0, "potential_decks": 0}]}]}}}


def test_slugs_follow_edhrec_page_names():
    assert ed.edhrec_slug("Toph, the First Metalbender") == "toph-the-first-metalbender"
    assert ed.edhrec_slug("Adéwalé, Breaker of Chains") == "adewale-breaker-of-chains"
    assert ed.edhrec_slug("Ezio Auditore da Firenze") == "ezio-auditore-da-firenze"
    assert ed.edhrec_slug("Kaya's Ghostform // Back") == "kayas-ghostform"


def test_flatten_keeps_one_row_per_card_with_inclusion():
    rows = ed.flatten(PAGE)
    assert [r["name"] for r in rows] == ["Eagle Vision", "Sol Ring", "Odd Card"]
    assert rows[0] == {"name": "Eagle Vision", "list": "Top Cards", "synergy": 0.42, "num_decks": 900,
                       "potential_decks": 1000, "inclusion": 0.9}
    assert rows[2]["inclusion"] is None and ed.flatten(None) == []


def test_fetch_all_writes_the_cache_pauses_and_marks_missing_pages():
    calls, pauses = [], []

    def get(url):
        calls.append(url)
        return PAGE if "ezio" in url else None

    with tempfile.TemporaryDirectory() as tmp:
        done = ed.fetch_all(["Ezio Auditore da Firenze", "Nobody Known"], Path(tmp), get, pauses.append)
        assert done == {"Ezio Auditore da Firenze": 3, "Nobody Known": "not on EDHREC"}
        assert calls[0].endswith("/commanders/ezio-auditore-da-firenze.json") and pauses == [ed.PAUSE, ed.PAUSE]
        cards = ed.load_cards("Ezio Auditore da Firenze", Path(tmp))
        assert cards["eagle vision"]["inclusion"] == 0.9 and ed.load_cards("Nobody Known", Path(tmp)) == {}
        assert json.loads((Path(tmp) / "ezio-auditore-da-firenze.json").read_text(encoding="utf-8")) == PAGE


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
