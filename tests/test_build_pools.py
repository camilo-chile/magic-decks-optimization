"""Offline tests for scripts/build_pools.py (synthetic oracle cards and owned rows)."""
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import build_pools as bp  # noqa: E402
import layer_a as la  # noqa: E402


def oracle(name, oid, identity="", type_line="Artifact", legal="legal", layout="normal", text="", gc=False):
    return {"name": name, "oracle_id": oid, "color_identity": list(identity), "type_line": type_line, "cmc": 2,
            "mana_cost": "{2}", "oracle_text": text, "legalities": {"commander": legal}, "layout": layout,
            "game_changer": gc}


CARDS = [
    oracle("Sol Ring", "o-sol", "", "Artifact"),
    oracle("Counterspell", "o-counter", "U", "Instant"),
    oracle("Lightning Bolt", "o-bolt", "R", "Instant"),
    oracle("Banned Thing", "o-ban", "", "Artifact", legal="banned"),
    oracle("Flip Walker", "o-flip", "U", "Creature", layout="transform"),
    oracle("Blue Hero", "o-hero", "U", "Legendary Creature — Human"),
    oracle("Red Hero", "o-redhero", "R", "Legendary Creature — Human"),
    oracle("Forest", "o-forest", "G", "Basic Land — Forest"),
    oracle("Odd Card", "o-odd", "", "Sorcery"),
]
INDEX = la.build_index(CARDS)
BY_OID = {c["oracle_id"]: c for c in CARDS}


def row(name, lang="en", qty=1, deck=None, token=False, proxy=False, set_="tst", number="1", finish="normal"):
    return {"name": name, "language": lang, "quantity": qty, "deck": deck, "token": token, "proxy": proxy, "set": set_,
            "number": number, "finish": finish, "condition": "near_mint"}


RECORDS = [row("Sol Ring", "en", deck="a"), row("Sol Ring", "es"), row("Counterspell", "es", deck="a"),
           row("Lightning Bolt", "en"), row("Banned Thing"), row("Flip Walker", "es"), row("Blue Hero", "es"),
           row("Red Hero", "en", proxy=True), row("Forest", "es", 3), row("Treasure", token=True),
           row("Unknown Card"), row("Odd Card", "es")]


def owned():
    return bp.owned_cards(RECORDS, INDEX)


def test_owned_cards_sum_copies_by_language_and_deck_and_skip_tokens_and_proxies():
    have, unknown = owned()
    assert unknown == ["Unknown Card"]
    sol = have["o-sol"]
    assert sol["copies"] == 2 and dict(sol["by_language"]) == {"en": 1, "es": 1} and dict(sol["by_deck"]) == {"a": 1, "free": 1}
    assert "o-redhero" not in have and have["o-forest"]["copies"] == 3


def test_a_pool_keeps_only_legal_unflipped_cards_inside_the_identity():
    have, _ = owned()
    names = [c["name"] for c in bp.pool({"U"}, have, BY_OID)]
    assert names == ["Blue Hero", "Counterspell", "Odd Card", "Sol Ring"]  # not Bolt, Forest, Banned Thing or Flip Walker
    sol = [c for c in bp.pool({"U"}, have, BY_OID) if c["name"] == "Sol Ring"][0]
    assert sol["copies"] == 2 and sol["held_by"] == {"a": 1, "free": 1} and len(sol["printings"]) == 2


def test_a_language_pool_counts_only_that_language_and_the_commander_is_excluded():
    have, _ = owned()
    entries = bp.pool({"U"}, have, BY_OID, "es", exclude={"o-hero"})
    assert [c["name"] for c in entries] == ["Counterspell", "Odd Card", "Sol Ring"]
    assert [c["copies"] for c in entries] == [1, 1, 1] and all(p["language"] == "es" for c in entries for p in c["printings"])


def test_legends_rank_by_the_spanish_only_pool_and_list_the_other_ones_last():
    have, _ = owned()
    rows = bp.legends(have, BY_OID)
    assert [r["name"] for r in rows] == ["Blue Hero"]  # the Red Hero is a proxy row, so it is not owned as a card
    assert rows[0]["pool_es"] == 3 and rows[0]["pool_any"] == 3 and rows[0]["spanish_copies"] == 1
    assert "| Blue Hero | U | 1 | 3 | 3 |" in bp.legends_markdown(rows)


def test_commander_of_reads_the_planned_list():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "d.txt").write_text("// Commander\n1 Blue Hero\n\n// Main\n1 Sol Ring\n", encoding="utf-8")
        config = {"decks": [{"slug": "d", "list": "d.txt"}, {"slug": "e", "list": "missing.txt"}]}
        assert bp.commander_of("d", config, root) == "Blue Hero" and bp.commander_of("e", config, root) is None


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
