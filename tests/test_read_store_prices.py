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
    assert 400 < len(targets) < 800


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
