"""Offline tests for scripts/collection_stages.py (synthetic ManaBox exports)."""
import csv
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import build_inventory as bi  # noqa: E402
import collection_stages as cs  # noqa: E402

HEADER = ("Binder Name,Binder Type,Name,Set code,Set name,Collector number,Foil,Rarity,Quantity,ManaBox ID,Scryfall ID,"
          "Purchase price,Misprint,Altered,Signed,Condition,Language,Proxy,Purchase price currency,Added").split(",")


def mrow(name, sid, qty=1, lang="en", foil="normal", binder=None, proxy="false", set_code="tst", number="1",
         set_name="Test Set", cond="near_mint"):
    return {"Binder Name": binder or ("Español" if lang == "es" else "Inglés"), "Binder Type": "binder", "Name": name,
            "Set code": set_code, "Set name": set_name, "Collector number": number, "Foil": foil, "Rarity": "rare",
            "Quantity": str(qty), "ManaBox ID": "1", "Scryfall ID": sid, "Purchase price": "0", "Misprint": "false",
            "Altered": "false", "Signed": "false", "Condition": cond, "Language": lang, "Proxy": proxy,
            "Purchase price currency": "USD", "Added": "2026-10-30T00:00:00.000Z"}


def write_csv(path, rows):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(rows)


EZIO = [
    mrow("Ezio Auditore da Firenze", "s-ezio", proxy="true", set_code="acr", number="1"),
    mrow("Sol Ring", "s-sol", foil="foil", set_code="cmm", number="410"),
    mrow("Forest", "s-forest", qty=2, lang="es", set_code="tla", number="290"),
    mrow("Assassin Token", "s-tok", set_code="tac", number="3", set_name="Assassin's Creed Tokens"),
]
AZULA = EZIO + [mrow("Sol Ring", "s-sol", set_code="cmm", number="410"), mrow("Arcane Signet", "s-signet")]


def stage_rows(**by_stage):
    return [(stage, [dict((k.lower(), v) for k, v in r.items()) for r in rows]) for stage, rows in by_stage.items()]


def test_stage_files_picks_the_newest_per_stage_and_ignores_old_exports():
    with tempfile.TemporaryDirectory() as tmp:
        for name in ("ManaBox_Collection_2026-10-18.csv", "ManaBox_Collection_2026-10-30_ezio.csv",
                     "ManaBox_Collection_2026-11-02_ezio.csv", "ManaBox_Collection_2026-11-03_azula.csv",
                     "ManaBox_Collection_2026-11-03_other.csv"):
            (Path(tmp) / name).write_text("x", encoding="utf-8")
        got = {stage: p.name for stage, p in cs.stage_files(Path(tmp)).items()}
        assert got == {"ezio": "ManaBox_Collection_2026-11-02_ezio.csv", "azula": "ManaBox_Collection_2026-11-03_azula.csv"}


def test_latest_collection_csv_prefers_the_later_stage_of_the_same_day():
    with tempfile.TemporaryDirectory() as tmp:
        for name in ("ManaBox_Collection_2026-10-18.csv", "ManaBox_Collection_2026-11-03_toph.csv",
                     "ManaBox_Collection_2026-11-03_azula.csv", "ManaBox_Collection_2026-11-03_ezio.csv"):
            (Path(tmp) / name).write_text("x", encoding="utf-8")
        assert bi.latest_collection_csv(Path(tmp)).name == "ManaBox_Collection_2026-11-03_toph.csv"
        (Path(tmp) / "ManaBox_Collection_2026-11-04.csv").write_text("x", encoding="utf-8")
        assert bi.latest_collection_csv(Path(tmp)).name == "ManaBox_Collection_2026-11-04.csv"
        assert bi.latest_collection_csv(Path(tmp) / "nowhere") is None


def test_new_rows_belong_to_the_stage_and_the_earlier_cards_stay():
    split = cs.split_stages(stage_rows(ezio=EZIO, azula=AZULA))
    ezio, azula = split["holdings"]["ezio"], split["holdings"]["azula"]
    assert sum(ezio.values()) == 5 and sum(azula.values()) == 2  # ezio: proxy, foil Sol Ring, 2 Forest, 1 token
    names = sorted(split["details"][k]["name"] for k in azula)
    assert names == ["Arcane Signet", "Sol Ring"]
    foil_sol = [k for k in ezio if k[0] == "s-sol"]
    assert len(foil_sol) == 1 and foil_sol[0][1] == "foil"  # the foil copy stays with Ezio, the normal one is new
    assert split["removed"] == [] and split["problems"] == []


def test_a_removed_row_leaves_its_stage_and_an_edited_row_is_flagged():
    edited = [dict(r) for r in AZULA]
    edited[0] = mrow("Ezio Auditore da Firenze", "s-ezio", proxy="true", set_code="acr", number="1", cond="played")
    edited = [r for r in edited if r["Name"] != "Forest"]
    split = cs.split_stages(stage_rows(ezio=EZIO, azula=edited))
    removed = {split["details"][r["key"]]["name"]: r for r in split["removed"]}
    assert set(removed) == {"Ezio Auditore da Firenze", "Forest"} and removed["Forest"]["quantity"] == 2
    assert removed["Ezio Auditore da Firenze"]["printing_added_again"] and not removed["Forest"]["printing_added_again"]
    assert sum(split["holdings"]["ezio"].values()) == 2  # proxy and both Forests left the Ezio stage
    total = sum(sum(c.values()) for c in split["holdings"].values())
    assert total == sum(cs.quantity({"quantity": r["Quantity"]}) for r in edited)  # holdings always match the last export


def test_a_missing_earlier_stage_is_reported():
    split = cs.split_stages(stage_rows(toph=EZIO))
    assert split["problems"] and "earlier stage(s) ezio, azula missing" in split["problems"][0]


def test_scan_problems_flag_language_binder_mismatch_and_bad_language():
    rows = [mrow("Sol Ring", "s1", lang="es", binder="Inglés"), mrow("Forest", "s2", lang="fr", binder="Otros"),
            mrow("Island", "s3", cond="damaged")]
    records = cs.owned_records(cs.split_stages(stage_rows(ezio=rows)))
    problems = cs.scan_problems(records)
    assert any("language/binder mismatch" in p and "Sol Ring" in p for p in problems)
    assert any("'fr' is not en or es" in p for p in problems)
    assert any("unusual condition 'damaged'" in p for p in problems)


def test_deck_text_has_one_commander_finish_marks_no_tokens_and_parses_back():
    records = cs.owned_records(cs.split_stages(stage_rows(ezio=EZIO + [mrow("Ezio Auditore da Firenze", "s-ezio2")])))
    text = cs.deck_text(records, {"ezio auditore da firenze"})
    commanders, main, bad = cs.la.parse_decklist(text)
    assert not bad and [c["name"] for c in commanders] == ["Ezio Auditore da Firenze"] and commanders[0]["set"] == "acr"
    assert "1 Sol Ring (CMM) 410 *F*" in text and "2 Forest (TLA) 290" in text and "Token" not in text
    assert [e["name"] for e in main].count("Ezio Auditore da Firenze") == 1  # the second copy stays in the main deck


def test_run_writes_the_deck_files_and_compares_with_the_planned_list():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        write_csv(root / "ManaBox_Collection_2026-10-30_ezio.csv", EZIO + [mrow("Arcane Signet", "s-signet")])
        (root / "plan.txt").write_text("// Commander\n1 Ezio Auditore da Firenze\n\n// Main\n1 Sol Ring\n1 Forest\n"
                                       "1 Mana Crypt\n", encoding="utf-8")
        config = {"decks": [{"slug": "ezio-auditore-da-firenze", "list": str(root / "plan.txt")}]}
        result = cs.run(cs.stage_files(root), config, root / "scanned", "2026-10-30")
        deck = result["deck_reports"][0]
        assert deck["facts"] == {"cards": 5, "tokens": 1, "proxies": 1, "finish": {"foil": 1, "normal": 4},
                                 "language": {"en": 3, "es": 2}, "condition": {"near_mint": 5}}
        assert deck["only_plan"] == [("Mana Crypt", 1, 0)] and deck["only_scan"] == [("Arcane Signet", 0, 1)]
        assert deck["differ"] == [("Forest", 1, 2)]
        assert any("5 cards scanned, a Commander deck has 100" in p for p in result["problems"])
        txt = (root / "scanned" / "ezio-auditore-da-firenze.txt").read_text(encoding="utf-8")
        detail = list(csv.DictReader(open(root / "scanned" / "ezio-auditore-da-firenze.csv", encoding="utf-8")))
        assert txt.startswith("// Commander\n1 Ezio Auditore da Firenze (ACR) 1") and len(detail) == 5
        assert sorted(r["kind"] for r in detail).count("token") == 1 and "| ezio |" in result["report"]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
