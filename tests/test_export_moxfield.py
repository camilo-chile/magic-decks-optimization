"""Offline tests for scripts/export_moxfield.py."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
spec = importlib.util.spec_from_file_location("export_moxfield", SCRIPTS / "export_moxfield.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_commander_first_printings_finishes_and_name_only_rest():
    deck = "// Commander\n1 Ezio Auditore da Firenze\n\n// Main\n1 Sol Ring\n2 Swamp\n"
    assigned = {"cards": [
        {"name": "Sol Ring", "qty": 1, "picks": [{"set": "cmm", "number": "400", "foil": "foil", "qty": 1}]},
        {"name": "Ezio Auditore da Firenze", "qty": 1, "picks": []},
        {"name": "Swamp", "qty": 2, "picks": [{"set": "acr", "number": "105", "foil": "normal", "qty": 1}]},
        {"name": "Eagle Vision", "qty": 1, "picks": [{"set": "", "number": "", "foil": "", "qty": 1}]},
    ]}
    text = mod.export("x", deck, assigned)
    assert text.splitlines()[:2] == ["// Commander", "1 Ezio Auditore da Firenze"]
    assert "1 Sol Ring (CMM) 400 *F*" in text
    assert "1 Swamp (ACR) 105" in text and "\n1 Swamp\n" in text
    assert "// Main" not in text
    assert "\n1 Eagle Vision\n" in text and "()" not in text  # a loan has no printing: by name only


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
