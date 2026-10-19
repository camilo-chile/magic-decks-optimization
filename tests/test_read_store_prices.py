"""Offline tests for the pure logic of scripts/read_store_prices.py (no network)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("read_store_prices", SCRIPTS / "read_store_prices.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TARGETS = {n.casefold(): n for n in ["Sol Ring", "Molten Gatekeeper", "Wooded Foothills", "Sam, Loyal Attendant",
                                       "Gollum, Riddle Master", "Nykthos, Shrine to Nyx", "Lulu, Stern Guardian",
                                       "Valakut Awakening"]}
SHOP = {"id": "s", "base": "https://shop.example"}
WHEN = "2026-10-16T00:00:00Z"


def variants(*rows):
    return [{"title": t, "price": p, "available": a} for t, p, a in rows]


def test_classify_language_condition_finish():
    assert mod.classify("Near Mint Español")[:3] == ("es", "NM", "nonfoil")
    assert mod.classify("Lightly Played Foil")[:3] == ("en", "LP", "foil")
    assert mod.classify("Near Mint / English / Foil")[:3] == ("en", "NM", "foil")
    assert mod.classify("Regular Foil (ingles)")[:3] == ("en", "NM", "foil")
    assert mod.classify("Non-Foil Heavily Played")[:3] == ("en", "HP", "nonfoil")
    assert mod.classify("FRENCH Wooded Foothills Near Mint")[0] == "other"
    assert mod.classify("Etched Near Mint")[2] == "etched"
    assert mod.classify("Ingles")[3] == ["condition"]  # condition inferred
    assert mod.classify("")[3] == ["language", "condition"]


def test_match_title_formats_seen_in_the_stores():
    m = mod.match_title
    assert m("Molten Gatekeeper [Modern Horizons 3]", TARGETS) == ("Molten Gatekeeper", "exact", "Modern Horizons 3")
    assert m("Sam, Loyal Attendant (Showcase Scrolls) [LTC - 476]", TARGETS)[:2] == ("Sam, Loyal Attendant", "exact")
    assert m("Gollum, Riddle Master Regular Foil (ingles) 277", TARGETS)[:2] == ("Gollum, Riddle Master", "exact")
    assert m("Nykthos, Shrine to Nyx Regular (español) 223", TARGETS)[:2] == ("Nykthos, Shrine to Nyx", "exact")
    assert m("Lulu, Stern Guardian (Borderless) (Chocobo Track Foil) R0467", TARGETS)[:2] == ("Lulu, Stern Guardian", "exact")
    assert m("FRENCH Wooded Foothills [Onslaught]", TARGETS)[0] == "Wooded Foothills"
    assert m("Valakut Awakening // Valakut Stoneforge [Zendikar Rising]", TARGETS)[:2] == ("Valakut Awakening", "exact")
    assert m("Sol Ring Token Deluxe Edition", TARGETS)[1] == "loose"
    assert m("Completely Different Card [Set]", TARGETS) is None


def test_shopify_offers_filter_language_condition_and_keep_stock_flag():
    product = {"title": "Molten Gatekeeper [Modern Horizons 3]", "handle": "molten-gatekeeper-mh3",
               "variants": variants(("Near Mint", "570", True), ("Lightly Played", "513", False),
                                    ("Moderately Played", "456", True), ("Damaged", "342", True),
                                    ("Near Mint Foil", "1880", True), ("Near Mint Español", "600", True),
                                    ("Near Mint French", "300", True), ("Near Mint", "0", True))}
    offers = mod.shopify_offers(product, SHOP, TARGETS, WHEN)
    got = [(o["language"], o["condition"], o["finish"], o["price_clp"], o["available"]) for o in offers]
    assert got == [("en", "NM", "nonfoil", 570, True), ("en", "LP", "nonfoil", 513, False),
                   ("en", "NM", "foil", 1880, True), ("es", "NM", "nonfoil", 600, True)]
    assert offers[0]["url"] == "https://shop.example/products/molten-gatekeeper-mh3"
    assert mod.shopify_offers({"title": "Other [Set]", "variants": []}, SHOP, TARGETS, WHEN) == []


def test_art_cards_are_not_offers():
    art = {"title": "Sol Ring Art Card [Commander Masters Art Series]", "handle": "a",
           "variants": variants(("Near Mint", "570", True))}
    assert mod.shopify_offers(art, SHOP, TARGETS, WHEN) == []
    assert mod.woo_offers(woo(name="Sol Ring Art Card"), SHOP, TARGETS, WHEN) == []
    assert mod.magic4ever_offers({"name": "Sol Ring Art Series", "variants": [
        {"language": "en", "conditionGrade": "NM", "stock": 1, "priceClp": 500, "finish": "nonfoil"}]}, SHOP, TARGETS, WHEN) == []


def test_shopify_offers_language_in_the_product_title():
    product = {"title": "Nykthos, Shrine to Nyx Regular (español) 223", "handle": "n",
               "variants": variants(("Default Title", "73797", True))}
    (offer,) = mod.shopify_offers(product, SHOP, TARGETS, WHEN)
    assert (offer["language"], offer["finish"], offer["condition"], offer["inferred"]) == ("es", "nonfoil", "NM", ["condition"])
    french = {"title": "FRENCH Wooded Foothills [Onslaught]", "handle": "w",
              "variants": variants(("Heavily Played Foil", "593610", True), ("Near Mint", "500000", True))}
    assert mod.shopify_offers(french, SHOP, TARGETS, WHEN) == []  # French printing: not accepted


def woo(**kw):
    base = {"id": 1, "name": "Sol Ring", "is_purchasable": True, "is_in_stock": True,
            "permalink": "https://cardnexus.cl/product/cn-child-x/",
            "prices": {"price": "2790", "currency_code": "CLP", "currency_minor_unit": 0},
            "stock_availability": {"text": "2 disponibles"},
            "attributes": [{"name": "idioma", "terms": [{"name": "Inglés"}]},
                           {"name": "pa_condicion", "terms": [{"name": "NM"}]},
                           {"name": "Foil", "terms": [{"name": "No Foil"}]}]}
    base.update(kw)
    return base


def test_woocommerce_offers_use_purchasable_listings_only():
    (offer,) = mod.woo_offers(woo(), SHOP, TARGETS, WHEN)
    assert (offer["price_clp"], offer["quantity"], offer["available"], offer["finish"], offer["language"]) == (2790, 2, True, "nonfoil", "en")
    assert mod.woo_offers(woo(is_purchasable=False), SHOP, TARGETS, WHEN) == []  # catalog entry, not a listing
    assert mod.woo_offers(woo(prices={"price": "0", "currency_minor_unit": 0}), SHOP, TARGETS, WHEN) == []
    assert mod.woo_offers(woo(name="Unknown Card"), SHOP, TARGETS, WHEN) == []
    sold_out = mod.woo_offers(woo(is_in_stock=False, stock_availability={"text": "Agotado"}), SHOP, TARGETS, WHEN)[0]
    assert sold_out["available"] is False and sold_out["quantity"] is None
    foil = woo(attributes=[{"name": "idioma", "terms": [{"name": "Español"}]},
                           {"name": "pa_condicion", "terms": [{"name": "LP"}]},
                           {"name": "Foil", "terms": [{"name": "Foil"}]}])
    got = mod.woo_offers(foil, SHOP, TARGETS, WHEN)[0]
    assert (got["language"], got["condition"], got["finish"]) == ("es", "LP", "foil")


def test_magic4ever_offers_from_its_public_api():
    card = {"name": "Sol Ring (Surge Foil)", "setName": "Warhammer 40,000 Commander", "productUrl": "https://m/x",
            "variants": [
                {"language": "en", "finish": "foil", "conditionGrade": "NM", "stock": 3, "priceClp": 13000,
                 "sku": "A", "productUrl": "https://m/a"},
                {"language": "es", "finish": "nonfoil", "conditionGrade": "LP", "stock": 0, "priceClp": 1900, "sku": "B"},
                {"language": "en", "finish": "nonfoil", "conditionGrade": "MP", "stock": 2, "priceClp": 900, "sku": "C"},
                {"language": "fr", "finish": "nonfoil", "conditionGrade": "NM", "stock": 2, "priceClp": 900, "sku": "D"},
                {"language": "en", "finish": "nonfoil", "conditionGrade": "NM", "stock": 2, "priceClp": 0, "sku": "E"}]}
    got = mod.magic4ever_offers(card, SHOP, TARGETS, WHEN)
    assert [(o["language"], o["condition"], o["finish"], o["price_clp"], o["available"], o["quantity"]) for o in got] == [
        ("en", "NM", "foil", 13000, True, 3), ("es", "LP", "nonfoil", 1900, False, 0)]
    assert got[0]["card"] == "Sol Ring" and got[0]["url"] == "https://m/a" and got[1]["url"] == "https://m/x"
    assert mod.magic4ever_offers({"name": "Sol Ringleader", "variants": card["variants"]}, SHOP, TARGETS, WHEN) == []


def test_targets_from_repo_cover_candidates_picks_and_locked_without_basics():
    targets = mod.targets_from_repo()
    assert "sol ring" in targets and "mountain" not in targets and "forest" not in targets
    assert "mindslaver" in targets  # locked list
    assert "frantic search" in targets  # Azula meta pick
    assert "valakut awakening" in targets  # double-faced name reduced to its front face
    assert 400 < len(targets) < 1500  # 916 with the Ezio targets (2026-10-19)


def test_same_price_prefers_spanish_over_english():
    def offer(lang, price, store):
        return {"card": "Sol Ring", "store": store, "price_clp": price, "available": True, "language": lang,
                "condition": "NM", "finish": "nonfoil", "match": "exact"}
    targets = {"sol ring": "Sol Ring"}
    tie = [offer("en", 2000, "a"), offer("es", 2000, "b")]
    assert "at b (es" in mod.summarize(targets, tie, {})
    cheaper_english = [offer("en", 1900, "a"), offer("es", 2000, "b")]
    assert "1900 CLP at a (en" in mod.summarize(targets, cheaper_english, {})


def test_summary_lists_missing_cards_and_cheapest_offer():
    targets = {"sol ring": "Sol Ring", "mox amber": "Mox Amber"}
    offers = [{"card": "Sol Ring", "store": "a", "price_clp": 3000, "available": True, "language": "en",
               "condition": "NM", "finish": "nonfoil", "match": "exact"},
              {"card": "Sol Ring", "store": "b", "price_clp": 2500, "available": True, "language": "en",
               "condition": "LP", "finish": "nonfoil", "match": "exact"},
              {"card": "Mox Amber", "store": "a", "price_clp": 9000, "available": False, "language": "en",
               "condition": "NM", "finish": "nonfoil", "match": "exact"}]
    text = mod.summarize(targets, offers, {"a": {"offers": 2}})
    assert "with none: 1" in text and "  Mox Amber\n" in text
    assert "Sol Ring: 2500 CLP at b" in text


def test_wishlist_names_come_from_the_wishlist_table_only():
    text = ("## Roles\n| Card | x |\n|---|---|\n| Sol Ring | y |\n\n"
            "## Wishlist (not in the pool)\n| Card | Role |\n|---|---|\n| Infernal Grasp | removal |\n"
            "| Jeska's Will (GC; pool, no offer) | ramp |\n\n## Other\n| Pongify | x |\n")
    assert mod.wishlist_names(text) == ["Infernal Grasp", "Jeska's Will"]


def test_wishlist_names_drop_the_markdown_marks_of_the_experts():
    text = ("## Wishlist\n| Card | Role |\n|---|---|\n| **Fact or Fiction** | draw |\n| * Embercleave | win |\n"
            "| Copperline Gorge * | land |\n| `Mana Drain` (GC) | counter |\n")
    assert mod.wishlist_names(text) == ["Fact or Fiction", "Embercleave", "Copperline Gorge", "Mana Drain"]


def test_ladder_cards_stay_targets_even_when_no_wishlist_names_them():
    text = "\n".join(["// Commander", "1 Toph, the First Metalbender", "", "// Base", "33 Forest", "1 Sol Ring", "",
                      "// Ladder", "+ Talisman of Impulse | - Titania, Protector of Argoth | rock",
                      "+ Lotus Cobra | - Harrow | speed"])
    assert mod.ladder_names(text) == ["Toph, the First Metalbender", "Forest", "Sol Ring", "Talisman of Impulse",
                                      "Lotus Cobra"]
    targets = mod.targets_from_repo()
    assert "talisman of impulse" in targets and "sakura-tribe elder" in targets  # both came from round-2 wishlists only


def test_extra_targets_of_a_deck_without_a_candidate_list_are_read():
    import tempfile
    old = mod.ROOT
    try:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "decks" / "candidates" / "new-deck"
            folder.mkdir(parents=True)
            (folder / "extra-targets.txt").write_text(
                "# comment\nBayek of Siwa\n\n  Mari, the Killing Quill\nIsland\n", encoding="utf-8")
            mod.ROOT = Path(tmp)
            got = mod.targets_from_repo()
    finally:
        mod.ROOT = old
    assert sorted(got.values()) == ["Bayek of Siwa", "Mari, the Killing Quill"]  # a basic land is never a target


def test_new_names_are_the_targets_the_newest_run_did_not_request():
    import json
    import tempfile
    old = mod.OUT_DIR
    try:
        with tempfile.TemporaryDirectory() as tmp:
            mod.OUT_DIR = Path(tmp)
            targets = {"sol ring": "Sol Ring", "opt": "Opt"}
            assert mod.new_names(targets) == targets  # no run yet
            # a merged file lists the repo's targets at merge time: it must not hide the new names
            (Path(tmp) / "merged-20261018T0000Z.json").write_text(
                json.dumps({"cards_requested": ["Sol Ring", "Opt"]}), encoding="utf-8")
            assert mod.new_names(targets) == targets
            (Path(tmp) / "20261017T0000Z.json").write_text(
                json.dumps({"cards_requested": ["Sol Ring"]}), encoding="utf-8")
            assert mod.new_names(targets) == {"opt": "Opt"}
    finally:
        mod.OUT_DIR = old


def test_stores_are_read_in_parallel_in_store_order_and_a_failure_stays_in_its_store():
    import tempfile
    import time
    seen_throttles = []

    def slow(requests, throttle, store, targets, progress):
        seen_throttles.append(throttle)
        time.sleep(0.3)  # the first store finishes last: the output must still follow the store order
        progress.log(f"  {store['name']}: working")
        return [{"card": "Sol Ring", "store": store["id"]}], {"offers": 1}

    def fast(requests, throttle, store, targets, progress):
        seen_throttles.append(throttle)
        return [{"card": "Opt", "store": store["id"]}], {"offers": 1}

    def broken(requests, throttle, store, targets, progress):
        raise RuntimeError("HTTP 429 three times: stopping this store")

    stores = [{"id": "a", "name": "A", "kind": "slow"}, {"id": "b", "name": "B", "kind": "broken"},
              {"id": "c", "name": "C", "kind": "fast"}]
    old = mod.READERS
    try:
        mod.READERS = {"slow": slow, "fast": fast, "broken": broken}
        with tempfile.TemporaryDirectory() as tmp:
            progress = mod.Progress(Path(tmp) / "run.progress.log")
            started = time.time()
            offers, stats = mod.read_all_stores(None, stores, {}, {}, progress)
            elapsed = time.time() - started
            assert [o["store"] for o in offers] == ["a", "c"]
            assert list(stats) == ["a", "b", "c"]
            assert stats["b"]["error"].startswith("RuntimeError") and "offers" in stats["a"]
            assert len({id(t) for t in seen_throttles}) == 2  # one throttle per store, never shared
            assert elapsed < 0.29 + 0.3  # parallel: the slow store did not wait for the others
            assert "FAILED B" in (Path(tmp) / "run.progress.log").read_text(encoding="utf-8")
    finally:
        mod.READERS = old


def test_shopify_stores_are_read_one_after_another_beside_the_other_stores():
    import tempfile
    import threading
    import time
    spans = {}

    def shop(requests, throttle, store, targets, progress):
        spans[store["id"]] = [time.time(), None, threading.get_ident()]
        time.sleep(0.2)
        spans[store["id"]][1] = time.time()
        return [], {"offers": 0}

    def card(requests, throttle, store, targets, progress):
        assert targets == {"opt": "Opt"}  # the per-card store searches only the fresh names
        spans[store["id"]] = [time.time(), None, threading.get_ident()]
        time.sleep(0.2)
        spans[store["id"]][1] = time.time()
        return [], {"offers": 0}

    stores = [{"id": "s1", "name": "S1", "kind": "shop"}, {"id": "c1", "name": "C1", "kind": "card"},
              {"id": "s2", "name": "S2", "kind": "shopify"}, {"id": "s3", "name": "S3", "kind": "shopify"}]
    old = mod.READERS
    try:
        mod.READERS = {"shop": shop, "shopify": shop, "card": card}
        with tempfile.TemporaryDirectory() as tmp:
            progress = mod.Progress(Path(tmp) / "run.progress.log")
            mod.read_all_stores(None, stores, {"sol ring": "Sol Ring", "opt": "Opt"}, {"opt": "Opt"}, progress)
    finally:
        mod.READERS = old
    assert spans["s2"][1] <= spans["s3"][0] + 0.01  # the second Shopify store started after the first one ended
    assert spans["s2"][2] == spans["s3"][2]          # in the same thread
    assert spans["c1"][2] != spans["s2"][2]          # the per-card store runs beside them
    assert spans["c1"][0] < spans["s2"][1]


def test_progress_log_keeps_every_line_whole_when_threads_log_together():
    import tempfile
    import threading
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "run.progress.log"
        progress = mod.Progress(path)
        threads = [threading.Thread(target=lambda n=n: [progress.log(f"store {n} line {i}") for i in range(50)])
                   for n in range(6)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        lines = path.read_text(encoding="utf-8").splitlines()
        assert len(lines) == 300 and all(" store " in line and " line " in line for line in lines)


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
