"""Offline tests for scripts/assign_copies.py (synthetic inventory and decks)."""
import importlib.util
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("assign_copies", SCRIPTS / "assign_copies.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
la = mod.la


def printing(lang, qty=1, binder=None, cond="near_mint", foil="normal", set_="tst", number="1"):
    return {"set": set_, "number": number, "language": lang, "foil": foil, "condition": cond, "quantity": qty,
            "scryfall_id": "sid", "binder": binder or ("Español" if lang == "es" else "Inglés"), "binder_type": "binder"}


def card(name, oid, *printings):
    return {"oracle_id": oid, "name": name, "copies": sum(p["quantity"] for p in printings), "printings": list(printings)}


def deck(slug, languages, cards, commanders=()):
    return {"slug": slug, "languages": languages, "cards": cards, "commanders": list(commanders)}


INV = {"cards": [
    card("Sol Ring", "o-sol", printing("en"), printing("es")),
    card("Arcane Signet", "o-signet", printing("es", 2)),
    card("Counterspell", "o-counter", printing("en")),
    card("Island", "o-island", printing("en", 5, binder="Inglés"), printing("es", 3, binder="Español")),
], "commander_ok": [{"oracle_id": "o-ezio", "name": "Ezio", "sources": ["proxy:Standard"]}]}


def picks(result, slug, name):
    return next(c for c in result["decks"][slug]["cards"] if c["name"] == name)["picks"]


def test_a_bilingual_deck_takes_the_english_copy_and_falls_back_to_spanish_only_when_that_is_all_there_is():
    res = mod.allocate([deck("a", "both", {"o-sol": ("Sol Ring", 1), "o-signet": ("Arcane Signet", 1)})], INV)
    assert [p["language"] for p in picks(res, "a", "Sol Ring")] == ["en"]
    assert [p["language"] for p in picks(res, "a", "Arcane Signet")] == ["es"]
    assert res["decks"]["a"]["missing"] == []


def test_the_spanish_only_deck_takes_spanish_copies_only_and_is_served_first():
    decks = [deck("bilingual", "both", {"o-sol": ("Sol Ring", 2)}), deck("spanish", "es", {"o-sol": ("Sol Ring", 1)})]
    res = mod.allocate(decks, INV)
    assert [p["language"] for p in picks(res, "spanish", "Sol Ring")] == ["es"]
    assert [p["language"] for p in picks(res, "bilingual", "Sol Ring")] == ["en"]  # the Spanish copy was already taken
    assert res["decks"]["bilingual"]["missing"] == [{"name": "Sol Ring", "needed": 2, "given": 1, "note": ""}]
    assert res["shared"] == [{"name": "Sol Ring", "decks": ["bilingual", "spanish"]}]


def test_a_card_owned_only_in_the_other_language_is_missing_with_a_note():
    res = mod.allocate([deck("spanish", "es", {"o-counter": ("Counterspell", 1)})], INV)
    assert res["decks"]["spanish"]["missing"] == [
        {"name": "Counterspell", "needed": 1, "given": 0, "note": "1 copy(ies) only in a language this deck does not take"}]


def test_one_physical_copy_serves_one_deck_only():
    res = mod.allocate([deck("a", "both", {"o-counter": ("Counterspell", 1)}), deck("b", "both", {"o-counter": ("Counterspell", 1)})], INV)
    assert res["decks"]["a"]["missing"] == [] and res["decks"]["b"]["missing"][0]["given"] == 0


def test_better_condition_then_non_foil_goes_first():
    inv = {"cards": [card("Sol Ring", "o-sol", printing("en", cond="lightly_played", number="1"),
                          printing("en", cond="near_mint", foil="foil", number="2"), printing("en", cond="near_mint", number="3"))]}
    res = mod.allocate([deck("a", "both", {"o-sol": ("Sol Ring", 2)})], inv)
    assert [(p["number"], p["foil"]) for p in picks(res, "a", "Sol Ring")] == [("3", "normal"), ("2", "foil")]


def test_basic_lands_come_from_the_pool_by_name_across_binders():
    res = mod.allocate([deck("a", "both", {"o-island": ("Island", 7)})], INV)
    assert sorted((p["language"], p["qty"]) for p in picks(res, "a", "Island")) == [("en", 5), ("es", 2)]


def test_a_proxy_commander_needs_no_copy_and_other_proxies_do_not_count():
    res = mod.allocate([deck("e", "both", {"o-ezio": ("Ezio", 1)}, commanders=["o-ezio"])], INV)
    assert res["decks"]["e"]["proxy_commanders"] == ["Ezio"] and res["decks"]["e"]["missing"] == []
    res = mod.allocate([deck("e", "both", {"o-ezio": ("Ezio", 1)})], INV)  # not as the commander: a copy is needed
    assert res["decks"]["e"]["missing"][0]["name"] == "Ezio"
    marked = dict(deck("e", "both", {"o-new": ("New Commander", 1)}, commanders=["o-new"]), proxy_commander=True)
    assert mod.allocate([marked], INV)["decks"]["e"]["proxy_commanders"] == ["New Commander"]  # the config marks the deck


def test_read_deck_resolves_names_and_reports_unknown_cards_and_missing_files():
    index = la.build_index([{"name": "Sol Ring", "oracle_id": "o-sol"}, {"name": "Ezio", "oracle_id": "o-ezio"}])
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "d.txt").write_text("// Commander\n1 Ezio\n\n// Main\n1 Sol Ring\n1 Nonexistent\n", encoding="utf-8")
        got, problems = mod.read_deck({"slug": "d", "list": "d.txt", "languages": "es"}, index, root)
        assert got["cards"] == {"o-ezio": ("Ezio", 1), "o-sol": ("Sol Ring", 1)} and got["commanders"] == ["o-ezio"]
        assert got["languages"] == "es" and problems == ["d: unknown card 'Nonexistent'"]
        none, problems = mod.read_deck({"slug": "x", "list": "x.txt"}, index, root)
        assert none is None and "no list yet" in problems[0]


def test_pull_list_names_the_binder_for_each_copy_and_the_shared_cards():
    config = {"decks": [{"slug": "a", "name": "A", "languages": "both"}, {"slug": "s", "name": "S", "languages": "es"}]}
    decks = [deck("a", "both", {"o-sol": ("Sol Ring", 1)}), deck("s", "es", {"o-sol": ("Sol Ring", 1)})]
    text = mod.pull_list_markdown(config, mod.allocate(decks, INV), {"a": 1, "s": 1}, [], "2026-10-26")
    assert "## Take out of the binder Inglés" in text and "## Take out of the binder Español" in text
    assert "- Sol Ring: a, s" in text and "| Sol Ring | TST 1 | en |" in text


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
