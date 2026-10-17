"""Offline tests for scripts/merge_prices.py (no network)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("merge_prices", SCRIPTS / "merge_prices.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

STORE = {"id": "paytowin", "base": "https://www.paytowin.cl"}
TARGETS = {"sol ring": "Sol Ring", "gollum, riddle master": "Gollum, Riddle Master"}


def test_browser_offers_classify_and_filter():
    best = {
        "sol ring": {"nen": ["Sol Ring [Commander Legends]", "sol-ring-cmr", "Near Mint", 2490],
                     "nes": ["Sol Ring [Commander Legends]", "sol-ring-cmr", "Lightly Played Spanish", 2200],
                     "f": ["Sol Ring [Commander Legends]", "sol-ring-cmr", "Near Mint Foil", 9000]},
        "gollum, riddle master": {"nen": ["Gollum, Riddle Master Regular Foil (ingles) 277", "gollum", "Default Title", 108240]},
        "not a target": {"nen": ["X", "x", "Near Mint", 100]},
        "sol ring ": {},
        "bad": {},
    }
    got = mod.browser_offers(STORE, best, TARGETS, "2026-10-17T00:00:00Z")
    rows = sorted((o["card"], o["language"], o["condition"], o["finish"], o["price_clp"]) for o in got)
    assert rows == [("Gollum, Riddle Master", "en", "NM", "foil", 108240),
                    ("Sol Ring", "en", "NM", "foil", 9000), ("Sol Ring", "en", "NM", "nonfoil", 2490),
                    ("Sol Ring", "es", "LP", "nonfoil", 2200)]
    assert all(o["source"] == "browser" and o["available"] and o["store"] == "paytowin" for o in got)
    assert got[0]["url"].startswith("https://www.paytowin.cl/products/")


def test_parse_psv_rebuilds_offers_and_keeps_pipes_in_the_suffix():
    import tempfile
    lines = ["#STORE paytowin fetched_at=2026-10-17T05:00:00Z source=browser pages=2 seen=500 cards=2 lines=3 FORMAT x",
             "sol ring|nen|sol-ring-cmr|Near Mint|2490|[Commander Legends]",
             "sol ring|nes|sol-ring-cmr|Near Mint Español|2200|[Commander Legends]",
             "gollum, riddle master|f|gollum|Default Title|108240|Regular Foil (ingles) 277",
             "unknown card|nen|x|Near Mint|100|"]
    text = "\n".join(lines) + "\n"
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "browser-paytowin-20261017.psv"
        path.write_text(text, encoding="utf-8")
        got, seen = mod.parse_psv(path, TARGETS, STORE)
    assert seen == 500 and len(got) == 3
    assert sorted((o["language"], o["finish"], o["price_clp"]) for o in got) == [
        ("en", "foil", 108240), ("en", "nonfoil", 2490), ("es", "nonfoil", 2200)]
    assert got[0]["fetched_at"] == "2026-10-17T05:00:00Z"


def test_merge_script_runs_keeps_each_stores_newest_good_reading():
    import json
    import tempfile

    def offer(store, price):
        return {"store": store, "card": "Sol Ring", "price_clp": price, "available": True}

    old = {"store_stats": {"a": {"offers": 1}, "b": {"offers": 1}}, "offers": [offer("a", 100), offer("b", 200)]}
    new = {"store_stats": {"b": {"error": "HTTP 429"}, "c": {"offers": 1}, "a": {"offers": 1}},
           "offers": [offer("a", 90), offer("c", 300)]}
    with tempfile.TemporaryDirectory() as tmp:
        paths = []
        for name, data in (("20261017T0100Z.json", old), ("20261018T0100Z.json", new)):
            path = Path(tmp) / name
            path.write_text(json.dumps(data), encoding="utf-8")
            paths.append(path)
        offers, stats = mod.merge_script_runs(paths)
    assert sorted((o["store"], o["price_clp"]) for o in offers) == [("a", 90), ("b", 200), ("c", 300)]
    assert stats["b"]["run"] == "20261017T0100Z.json" and "error" not in stats["b"]
    assert stats["a"]["run"] == "20261018T0100Z.json"


def test_script_reads_only_the_stores_not_yet_read():
    enabled = sorted(s["id"] for s in mod.rsp.STORES if s["enabled"])
    assert enabled == ["afkstore", "lacomarca", "piedrabruja"]


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
