"""Offline tests for scripts/build_inventory.py (synthetic index and rows)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("build_inventory", SCRIPTS / "build_inventory.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
la = mod.la


def card(name, oid):
    return {"name": name, "oracle_id": oid, "cmc": 1}


INDEX = la.build_index([
    card("Sol Ring", "o-sol"), card("Arcane Signet", "o-signet"),
    {"name": "Fire // Ice", "oracle_id": "o-fire", "cmc": 2,
     "card_faces": [{"name": "Fire"}, {"name": "Ice"}]},
])


def row(name, qty=1, lang="en", binder="Toph", btype="deck", cond="near_mint", proxy="false", foil="normal"):
    return {"name": name, "quantity": str(qty), "language": lang, "binder name": binder,
            "binder type": btype, "condition": cond, "proxy": proxy, "foil": foil,
            "set code": "tst", "collector number": "1", "scryfall id": "sid"}


def test_copies_are_summed_per_oracle_id_with_language_and_places():
    inv = mod.build_inventory([row("Sol Ring"), row("Sol Ring", 2, lang="es", binder="Box", btype="binder"),
                               row("Arcane Signet")], INDEX)
    sol = next(c for c in inv["cards"] if c["name"] == "Sol Ring")
    assert sol["copies"] == 3 and sol["by_language"] == {"en": 1, "es": 2}
    assert sol["places"] == {"deck:Toph": 1, "binder:Box": 2}
    assert sol["in_project_deck"] == {"toph-the-first-metalbender": 1}
    assert inv["unique_cards"] == 2 and inv["owned_copies"] == 4 and inv["problems"] == {}


def test_front_face_names_resolve():
    inv = mod.build_inventory([row("Ice")], INDEX)
    assert inv["cards"][0]["oracle_id"] == "o-fire"


def test_proxies_unknown_names_languages_and_conditions_are_reported_not_counted_or_hidden():
    inv = mod.build_inventory([
        row("Sol Ring", proxy="true"), row("Nonexistent Card"), row("Arcane Signet", lang="de"),
        row("Fire // Ice", cond="heavily_played")], INDEX)
    p = inv["problems"]
    assert len(p["proxies"]) == 1 and len(p["unknown_names"]) == 1
    assert len(p["languages_other_than_en_es"]) == 1 and len(p["worse_than_lightly_played"]) == 1
    assert inv["owned_copies"] == 2  # the proxy and the unknown name are not owned cards


def test_reserved_binders_mark_their_copies():
    inv = mod.build_inventory([row("Sol Ring", 1, binder="Modern", btype="deck"),
                               row("Sol Ring", 1, binder="Box", btype="binder")], INDEX, {"modern"})
    sol = inv["cards"][0]
    assert sol["copies"] == 2 and sol["reserved_copies"] == 1


def test_reserved_binder_creatures_and_proxies_may_only_be_commanders():
    index = la.build_index([
        {"name": "Ezio", "oracle_id": "o-ezio", "type_line": "Legendary Creature", "cmc": 2},
        {"name": "Sword", "oracle_id": "o-sword", "type_line": "Artifact — Equipment", "cmc": 3},
        card("Sol Ring", "o-sol")])
    inv = mod.build_inventory([
        row("Ezio", binder="Std", btype="binder"), row("Sword", binder="Std", btype="binder"),
        row("Sol Ring", proxy="true", binder="Std", btype="binder"), row("Sol Ring", binder="Box", btype="binder")],
        index, {"std"})
    ok = {c["name"]: c["sources"] for c in inv["commander_ok"]}
    assert ok == {"Ezio": ["reserved:Std"], "Sol Ring": ["proxy:Std"]}  # the reserved sword is not a creature
    ezio = next(c for c in inv["cards"] if c["name"] == "Ezio")
    assert ezio["reserved_copies"] == 1 and ezio["reserved_by_language"] == {"en": 1}
    sol = next(c for c in inv["cards"] if c["name"] == "Sol Ring")
    assert sol["copies"] == 1  # the proxy is not an owned copy


def test_tokens_and_emblems_are_listed_apart_never_as_cards_or_unknown_names():
    token = dict(row("Treasure", 2, binder="Inglés", btype="binder"), **{"set name": "Lost Caverns of Ixalan Tokens"})
    emblem = dict(row("Wrenn Emblem", 1, lang="es", binder="Español", btype="binder"), **{"set name": "Modern Horizons Emblems"})
    inv = mod.build_inventory([token, emblem, row("Sol Ring", binder="Inglés", btype="binder")], INDEX)
    assert inv["unique_cards"] == 1 and inv["token_copies"] == 3 and inv["problems"] == {}
    assert [(t["name"], t["quantity"], t["language"], t["binders"]) for t in inv["tokens"]] == [
        ("Treasure", 2, "en", ["Inglés"]), ("Wrenn Emblem", 1, "es", ["Español"])]
    assert "tokens and emblems (not cards): 3 copies in 2 printings" in mod.summary(inv)


def test_printings_say_which_binder_holds_each_copy():
    inv = mod.build_inventory([row("Sol Ring", binder="Español", btype="binder", lang="es")], INDEX)
    assert (inv["cards"][0]["printings"][0]["binder"], inv["cards"][0]["printings"][0]["binder_type"]) == ("Español", "binder")


def test_a_card_in_the_binder_of_the_other_language_is_a_scan_error_that_is_reported():
    inv = mod.build_inventory([row("Sol Ring", lang="en", binder="Español", btype="binder"),
                               row("Arcane Signet", lang="es", binder="English Cards", btype="binder"),
                               row("Sol Ring", lang="en", binder="Box", btype="binder")], INDEX)
    assert len(inv["problems"]["language_binder_mismatch"]) == 2  # a binder with another name promises no language
    assert mod.binder_language("Spanish Cards") == "es" and mod.binder_language("Inglés") == "en"
    assert mod.binder_language("Toph") is None


def test_summary_mentions_problems_and_reserved_state():
    inv = mod.build_inventory([row("Nonexistent Card")], INDEX)
    text = mod.summary(inv)
    assert "PROBLEM unknown_names" in text and "cards allowed as commander only: 0" in text


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
