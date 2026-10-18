"""Offline tests for the pure helpers of scripts/check_list.py (no network, no caches)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("check_list", SCRIPTS / "check_list.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_cap_is_read_from_the_file_name():
    assert mod.cap_from_name("toph_cap20000.txt") == 20000
    assert mod.cap_from_name("azula_CAP80000_v2.txt") == 80000
    assert mod.cap_from_name("alexios.txt") is None


def test_cap_status_says_within_or_over():
    assert mod.cap_status(18000, 20000) == "within the cap of 20,000 CLP (+2,000 CLP left)"
    assert mod.cap_status(21500, 20000).startswith("OVER the cap of 20,000 CLP (-1,500")
    assert mod.cap_status(5, None) == "no cap in the file name"


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
