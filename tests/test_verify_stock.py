"""Offline tests for scripts/plan_buylist.py and scripts/verify_stock.py (no network, no files written)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


pb, vs = load("plan_buylist"), load("verify_stock")


def offer(store, price, language="en", variant="Near Mint", url="https://s.cl/products/x", **extra):
    return {"store": store, "price_clp": price, "language": language, "finish": "nonfoil", "condition": "NM", "title": "X",
            "variant": variant, "url": url, "fetched_at": "2026-10-19T10:00:00Z", **extra}


def test_buy_lists_add_the_copies_every_deck_buys_and_offers_keep_one_per_store_cheapest_first():
    priced = {"Azula": {"to_buy": [{"name": "Entomb", "qty": 1}, {"name": "Sol Ring", "qty": 1}]},
              "Ezio": {"to_buy": [{"name": "Sol Ring", "qty": 1}]}}
    cards = pb.aggregate(priced)
    assert cards["Sol Ring"]["qty"] == 2 and cards["Sol Ring"]["decks"] == {"Azula": 1, "Ezio": 1} and cards["Entomb"]["qty"] == 1
    picked = pb.offers_for([offer("b", 900), offer("a", 700, language="en"), offer("a", 700, language="es"), offer("c", 800)], kept=2)
    assert [(o["store"], o["price_clp"], o["language"]) for o in picked] == [("a", 700, "es"), ("c", 800, "en")]


def test_an_offer_read_more_than_a_day_before_the_price_reading_is_stale():
    assert pb.is_stale("2026-10-17T20:00:00Z", "2026-10-19T10:13:44Z") and not pb.is_stale("2026-10-19T09:56:00Z", "2026-10-19T10:13:44Z")
    assert pb.is_stale(None, "2026-10-19T10:13:44Z")


def test_shopify_variant_is_found_by_title_and_price_is_in_cents():
    product = {"variants": [{"title": "Near Mint", "price": 2240000, "available": True},
                            {"title": "Lightly Played", "price": 2070000, "available": False}]}
    rec = vs.shopify_status("Entomb", offer("paytowin", 22400), product)
    assert rec["status"] == "in_stock" and rec["price_clp"] == 22400
    assert vs.shopify_status("Entomb", offer("paytowin", 20700, variant="Lightly Played"), product)["status"] == "out_of_stock"
    assert vs.shopify_status("Entomb", offer("paytowin", 1, variant="Near Mint Foil"), product)["status"] == "variant_not_found"


def test_woocommerce_and_magic4ever_read_the_quantity_the_store_shows():
    woo = [{"is_in_stock": True, "is_purchasable": True, "prices": {"price": "22990", "currency_minor_unit": 0},
            "stock_availability": {"text": "3 disponibles"}}]
    rec = vs.woo_status("Entomb", offer("cardnexus", 22990), woo)
    assert rec["status"] == "in_stock" and rec["quantity"] == 3 and rec["price_clp"] == 22990
    assert vs.woo_status("Entomb", offer("cardnexus", 1), [])["status"] == "variant_not_found"
    cards = [{"variants": [{"sku": "A-1", "stock": 0, "priceClp": 500}, {"sku": "B-2", "stock": 2, "priceClp": 650}]}]
    assert vs.magic4ever_status("X", offer("magic4ever", 650, variant="B-2"), cards)["quantity"] == 2
    assert vs.magic4ever_status("X", offer("magic4ever", 500, variant="A-1"), cards)["status"] == "out_of_stock"
    assert vs.magic4ever_status("X", offer("magic4ever", 1, variant="Z-9"), cards)["status"] == "variant_not_found"


def test_verdict_needs_the_copies_the_plan_buys_and_a_price_rise_over_5_percent_is_flagged():
    def rec(status, qty=None, price=100, plan=100):
        return {"status": status, "quantity": qty, "price_clp": price, "plan_price_clp": plan}
    assert vs.verdict(1, [rec("in_stock")]) == "verified" and vs.verdict(2, [rec("in_stock", qty=2)]) == "verified"
    assert vs.verdict(2, [rec("in_stock")]) == "quantity_unverified" and vs.verdict(2, [rec("in_stock", qty=1)]) == "quantity_unverified"
    assert vs.verdict(1, [rec("out_of_stock"), rec("error")]) == "no_stock"
    assert vs.drifted(rec("in_stock", price=106)) and not vs.drifted(rec("in_stock", price=105)) and not vs.drifted(rec("error", price=None))


def test_store_subsets_cover_every_card_with_stock_and_fewer_stores_cost_more():
    ps = load("plan_stores")

    def card(name, qty, *offers):
        return {"name": name, "qty": qty, "records": [{"status": s, "store": st, "price_clp": p, "quantity": q} for st, p, s, q in offers]}
    cards = [card("A", 1, ("x", 100, "in_stock", None), ("y", 150, "in_stock", None)),
             card("B", 2, ("y", 200, "in_stock", 2), ("z", 90, "in_stock", 1)),  # z shows 1 copy only: it cannot cover the 2 needed
             card("C", 1, ("x", 50, "out_of_stock", None), ("z", 60, "in_stock", None))]
    assert ps.card_options(cards[1]) == {"y": 200}
    best = ps.best_subsets(cards)
    assert 1 not in best  # no single store sells B and C
    assert best[2]["cost"] == 150 + 400 + 60 and best[2]["stores"] == ("y", "z") and best[2]["pick"] == {"A": "y", "B": "y", "C": "z"}
    assert best[2]["single"] == 3 and best[2]["unverified"] == 0  # inside (y, z) every card has one source; B shows its quantity
    assert best[3]["cost"] == 100 + 400 + 60 and best[3]["stores"] == ("x", "y", "z") and best[3]["single"] == 2


def test_purchase_order_secures_single_source_and_costly_fallbacks_first():
    pp = load("plan_purchase")

    def card(name, qty, *offers):
        return {"name": name, "qty": qty, "decks": {"Ezio": qty},
                "records": [{"status": "in_stock", "store": s, "price_clp": p, "quantity": q} for s, p, q in offers]}
    stock = {"budget": 1, "cards": [
        card("Single", 1, ("a", 2400, None)),                                   # no second store: weighs 10 + 2.4
        card("Costly", 2, ("b", 6200, None), ("a", 17400, None)),              # quantity not shown, fallback +22,400: 2 + 22.4
        card("Plain", 1, ("c", 500, 9), ("a", 600, 9)),                         # comfortable, two stores: class B
        card("Thin", 1, ("c", 490, 1), ("b", 600, 5)),                          # one copy shown, fallback +110: 1 + 0.11
        card("Elsewhere", 1, ("z", 100, 3))]}                                   # only in a store outside the set
    rows, uncovered = pp.rows_for(stock, ("a", "b", "c"))
    by = {r["card"]: r for r in rows}
    assert uncovered == ["Elsewhere"] and by["Single"]["reasons"] == ["single source"] and by["Plain"]["reasons"] == []
    assert by["Costly"]["reasons"] == ["quantity not shown"] and by["Thin"]["reasons"] == ["thin stock"]
    assert round(pp.risk_weight(by["Costly"]), 1) == 24.4 and round(pp.risk_weight(by["Single"]), 1) == 12.4 and pp.risk_weight(by["Plain"]) == 0
    order, weight, value = pp.store_order(rows)
    assert order == ["b", "a", "c"] and value["b"] == 12400  # b holds the costly fallback risk, a the single source, c only a thin card


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
