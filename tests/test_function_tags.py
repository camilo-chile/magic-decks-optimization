"""Offline tests for scripts/function_tags.py (a fake Scryfall: no network)."""
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import function_tags as ft  # noqa: E402
import layer_a as la  # noqa: E402


def fake_get(pages):
    """pages: {url fragment: [page dicts]}; a page list is served in order through next_page markers."""
    state = {"calls": []}

    def get(url):
        state["calls"].append(url)
        for key, seq in pages.items():
            if key in url:
                if "page=2" in url:
                    return seq[1]
                return seq[0]
        return None
    get.state = state
    return get


def test_fetch_tag_follows_pages_collects_oracle_ids_and_pauses_between_requests():
    pages = {"otag%3Aramp": [
        {"has_more": True, "next_page": "https://api.scryfall.com/cards/search?q=otag%3Aramp&page=2",
         "data": [{"oracle_id": "o1"}, {"oracle_id": "o2"}]},
        {"has_more": False, "data": [{"oracle_id": "o2"}, {"card_faces": [{"oracle_id": "o3"}]}]}]}
    pauses = []
    get = fake_get(pages)
    assert ft.fetch_tag("ramp", get, pauses.append) == ["o1", "o2", "o3"]
    assert len(get.state["calls"]) == 2 and pauses == [ft.PAUSE, ft.PAUSE]
    assert "otag%3Aramp" in get.state["calls"][0] and "unique=cards" in get.state["calls"][0]


def test_an_unknown_slug_is_cached_as_missing_not_as_an_empty_tag():
    get = fake_get({"otag%3Aramp": [{"has_more": False, "data": [{"oracle_id": "o1"}]}]})
    cache = ft.build_cache(("ramp", "nonsense"), get, lambda s: None)
    assert cache["tags"] == {"ramp": ["o1"], "nonsense": None}


def test_a_cache_of_the_same_day_is_resumed_and_a_429_keeps_the_finished_tags():
    from datetime import date
    today = date.today().isoformat()
    get = fake_get({"otag%3Adraw": [{"has_more": False, "data": [{"oracle_id": "o2"}]}]})
    saved = []
    cache = ft.build_cache(("ramp", "draw"), get, lambda s: None, {"fetched": today, "tags": {"ramp": ["o1"]}},
                           lambda c: saved.append(dict(c["tags"])))
    assert cache["tags"] == {"ramp": ["o1"], "draw": ["o2"]} and len(get.state["calls"]) == 1
    assert saved == [{"ramp": ["o1"], "draw": ["o2"]}]
    stale = ft.build_cache(("draw",), get, lambda s: None, {"fetched": "2020-01-01", "tags": {"draw": ["old"]}})
    assert stale["tags"] == {"draw": ["o2"]}

    def limited(url):
        if "otag%3Adraw" in url:
            raise ft.RateLimited(url)
        return {"has_more": False, "data": [{"oracle_id": "o1"}]}

    kept = []
    try:
        ft.build_cache(("ramp", "draw", "tutor"), limited, lambda s: None, None, lambda c: kept.append(dict(c["tags"])))
        raise AssertionError("the 429 must stop the run")
    except ft.RateLimited:
        pass
    assert kept == [{"ramp": ["o1"]}]


def test_profile_counts_copies_and_marks_missing_tags():
    cache = {"fetched": "2026-10-31", "tags": {"ramp": ["o1", "o2"], "draw": ["o3"], "tutor": None}}
    got = ft.profile([("o1", 1), ("o2", 4), ("o3", 2), ("o9", 5)], cache, ("ramp", "draw", "tutor", "blink"))
    assert got == {"ramp": 5, "draw": 2, "tutor": None, "blink": None}


def test_deck_oracle_ids_resolves_names_and_reports_unknown_ones():
    index = la.build_index([{"name": "Sol Ring", "oracle_id": "o-sol"}, {"name": "Ezio", "oracle_id": "o-ezio"}])
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "d.txt"
        path.write_text("// Commander\n1 Ezio (ACR) 25\n\n2 Sol Ring (CMM) 410 *F*\n1 Nobody\n", encoding="utf-8")
        found, unknown = ft.deck_oracle_ids(path, index)
    assert found == [("o-ezio", 1), ("o-sol", 2)] and unknown == ["Nobody"]


def test_profile_markdown_has_one_column_per_deck_and_n_a_for_missing_tags():
    cache = {"fetched": "2026-10-31", "tags": {}}
    text = ft.profile_markdown({"a": {s: 1 for s in ft.FUNCTION_TAGS}, "b": {s: None for s in ft.FUNCTION_TAGS}}, cache)
    assert "| Tag | a | b |" in text and "| ramp | 1 | n/a |" in text and "tags read 2026-10-31" in text


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
