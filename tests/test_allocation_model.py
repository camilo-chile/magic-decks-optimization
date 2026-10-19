"""Offline tests for scripts/allocation_model.py (no network, synthetic cards)."""
import importlib.util
import sys
from collections import Counter
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("allocation_model", SCRIPTS / "allocation_model.py")
am = importlib.util.module_from_spec(spec)
spec.loader.exec_module(am)

CARDS = [{"name": n, "oracle_id": f"id-{n}", "color_identity": ci}
         for n, ci in (("Sol Ring", []), ("Gamble", ["R"]), ("Mountain", []), ("Counterspell", ["U"]),
                       ("Snow-Covered Forest", ["G"]), ("Nowhere Card", []))]
INDEX = am.la.build_index(CARDS)


def offer(card, price, store="a", language="en", finish="nonfoil"):
    return {"card": card, "price_clp": price, "store": store, "language": language, "finish": finish,
            "available": True, "url": f"https://{store}/{card}"}


def listing(text):
    return am.read_list(text, INDEX)


def test_is_basic_includes_snow_covered_basics():
    assert am.is_basic("Mountain") and am.is_basic("Snow-Covered Forest") and not am.is_basic("Sol Ring")


def test_price_list_owned_first_basics_free_and_cheapest_offer():
    deck = listing("// Commander\n1 Sol Ring\n\n// Main\n1 Gamble\n5 Mountain\n1 Counterspell\n")
    owned = {"id-Sol Ring": {"name": "Sol Ring", "usable": 1}}
    offers = {"id-Gamble": [offer("Gamble", 900, "a"), offer("Gamble", 800, "b")],
              "id-Counterspell": [offer("Counterspell", 3000, "a")]}
    got = am.price_list(deck, owned, offers)
    assert got["owned"] == ["Sol Ring"] and got["basics"] == 5
    assert got["cost_clp"] == 3800 and got["stores"] == ["a", "b"]
    assert {b["name"]: b["store"] for b in got["to_buy"]} == {"Gamble": "b", "Counterspell": "a"}
    assert am.shipping_clp(got["stores"]) == 10000


def test_one_physical_copy_serves_one_deck_only():
    deck = listing("// Commander\n1 Sol Ring\n\n// Main\n1 Gamble\n")
    owned = {"id-Gamble": {"name": "Gamble", "usable": 1}}
    offers = {"id-Gamble": [offer("Gamble", 800)], "id-Sol Ring": [offer("Sol Ring", 2000)]}
    claimed = Counter()
    first = am.price_list(deck, owned, offers, claimed)
    second = am.price_list(deck, owned, offers, claimed)
    assert first["cost_clp"] == 2000 and "Gamble" in first["owned"]
    assert second["cost_clp"] == 2800 and "Gamble" not in second["owned"]


def test_no_stock_is_reported_not_priced_and_spanish_wins_a_tie():
    deck = listing("// Commander\n1 Sol Ring\n\n// Main\n1 Gamble\n1 Nowhere Card\n")
    offers = {"id-Gamble": [offer("Gamble", 800, "a", "en"), offer("Gamble", 800, "b", "es")]}
    got = am.price_list(deck, {}, offers)
    assert got["no_stock"] == ["Nowhere Card", "Sol Ring"]
    assert got["to_buy"][0]["language"] == "es" and got["cost_clp"] == 800


def test_unowned_japanese_copies_do_not_count_as_usable(tmp_path=None):
    import json
    import tempfile
    inv = {"cards": [{"oracle_id": "x", "name": "X", "copies": 2, "by_language": {"en": 1, "ja": 1}}]}
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "inv.json"
        path.write_text(json.dumps(inv), encoding="utf-8")
        assert am.load_owned(path)["x"]["usable"] == 1


def test_reserved_binder_copies_are_not_usable_but_a_commander_may_come_from_there():
    import json
    import tempfile
    inv = {"cards": [
        {"oracle_id": "id-Gamble", "name": "Gamble", "copies": 2, "by_language": {"en": 2},
         "reserved_by_language": {"en": 1}},
        {"oracle_id": "id-Sol Ring", "name": "Sol Ring", "copies": 1, "by_language": {"en": 1},
         "reserved_by_language": {"en": 1}}],
        "commander_ok": [{"oracle_id": "id-Sol Ring", "name": "Sol Ring", "sources": ["reserved:Std"]},
                         {"oracle_id": "id-Counterspell", "name": "Counterspell", "sources": ["proxy:Std"]}]}
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "inv.json"
        path.write_text(json.dumps(inv), encoding="utf-8")
        owned = am.load_owned(path)
    assert owned["id-Gamble"]["usable"] == 1 and owned["id-Sol Ring"]["usable"] == 0
    assert owned["id-Counterspell"] == {"name": "Counterspell", "usable": 0, "copies": 0, "commander_ok": True}
    as_commander = am.price_list(listing("// Commander\n1 Counterspell\n\n// Main\n1 Sol Ring\n"), owned,
                                 {"id-Sol Ring": [offer("Sol Ring", 2000)]})
    assert as_commander["cost_clp"] == 2000  # the commander is free, the reserved Sol Ring in the 99 is bought
    assert any("Counterspell (commander" in name for name in as_commander["owned"])
    in_the_99 = am.price_list(listing("// Commander\n1 Gamble\n\n// Main\n1 Counterspell\n"), owned,
                              {"id-Counterspell": [offer("Counterspell", 3000)]})
    assert in_the_99["cost_clp"] == 3000  # a proxy or reserved card is never free outside the commander slot


def test_meta_picks_and_identity():
    picks = am.read_meta_picks("1. Sol Ring 90\n2. Unknown Thing 50\n3. Gamble 40\n", INDEX)
    assert [(n, p) for _, n, p in picks] == [("Sol Ring", 90), ("Gamble", 40)]
    assert am.fits_identity(CARDS[1], {"R", "G"}) and not am.fits_identity(CARDS[3], {"R", "G"})


def test_the_locked_list_may_be_empty_and_coverage_reports_the_missing_cards():
    import tempfile
    old = am.LOCKED_PATH
    try:
        with tempfile.TemporaryDirectory() as tmp:
            am.LOCKED_PATH = Path(tmp) / "locked.txt"
            assert am.read_locked(INDEX) == []  # no file
            am.LOCKED_PATH.write_text("# empty on purpose\n// Commander\n", encoding="utf-8")
            assert am.read_locked(INDEX) == []  # comments only
            am.LOCKED_PATH.write_text("1 Sol Ring\n1 Unknown Thing\n", encoding="utf-8")
            assert am.read_locked(INDEX) == ["id-Sol Ring"]
    finally:
        am.LOCKED_PATH = old
    a, b = listing("// Commander\n1 Sol Ring\n"), listing("// Commander\n1 Gamble\n")
    cover = am.locked_coverage([a, b], ["id-Sol Ring", "id-Gamble", "id-Counterspell"])
    assert cover["missing"] == ["id-Counterspell"] and cover["copies_needed"]["id-Sol Ring"] == 1


def test_a_loose_title_match_must_still_be_the_same_card():
    def offer(card, title, match="loose"):
        return {"card": card, "title": title, "match": match}
    assert not am.is_the_card(offer("Savannah", "Savannah Lions [DMR - 24]", "exact"))  # even a reader's "exact" does not make it the card
    assert not am.is_the_card(offer("Savannah", "Savannah Lions (Retro)", "exact"))
    assert am.is_the_card(offer("Sol Ring", "Sol Ring Regular Foil (ingles) 277", "exact"))
    assert am.is_the_card(offer("Pyroblast", "Pyroblast - 1998 Brian Selden (ICE) (SB) [WCD - 1998]", "exact"))
    assert not am.is_the_card(offer("Savannah", "Savannah Lions [DMR - 24]"))
    assert not am.is_the_card(offer("Bedlam", "Bedlam Reveler (Borderless) [INR - 312]"))
    assert not am.is_the_card(offer("Anger", "Anger of the Gods [TSR - 339]"))
    assert not am.is_the_card(offer("Earth Rumble", "Earth Rumble Wrestlers Regular Foil (ingles) 218"))
    assert am.is_the_card(offer("Comet Storm", "Comet Storm M411"))
    assert am.is_the_card(offer("Anticipate", "Anticipate P12"))
    assert not am.is_the_card(offer("Anger", "Anger of the Gods R112"))
    assert am.is_the_card(offer("Ozai, the Phoenix King", "Ozai, the Phoenix King M335"))
    assert am.is_the_card(offer("Anger", "Anger [TSR - 339]"))
    assert am.is_the_card(offer("Waterlogged Teachings // Inundated Archive", "Waterlogged Teachings R12"))


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
