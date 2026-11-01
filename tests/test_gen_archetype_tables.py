"""Offline tests for scripts/gen_archetype_tables.py (the skill's archetypes.md tables must match archetypes.json)."""
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import gen_archetype_tables as gen  # noqa: E402

ARCH = {"name": "Toy", "land_band": [36, 38], "land_why": "toy lands", "curve": {"avg_mv": [2.8, 3.2], "creature_count": [20, 25], "why": "toy curve"},
        "base": {t: {"min": 1, "target": 2, "why": f"toy {t}"} for t in gen.BASE_LABELS},
        "functions": {"later": {"min": 3, "target": 4, "tier": "support", "needed_by": "late", "why": "toy support", "counts_inside": "first"},
                      "first": {"min": 10, "target": 12, "tier": "gate", "needed_by": "early", "why": "toy gate",
                                "if_commander_is_source": {"needed_by": "late", "min": 6, "target": 8}}}}


def test_a_table_lists_lands_base_floors_then_gate_before_support_functions():
    lines = gen.table(ARCH).split("\n")
    assert lines[2].startswith("| Lands | band | 36 | 38 |") and lines[3].startswith("| Ramp | base | 1 | 2 |")
    first, later = [i for i, ln in enumerate(lines) if "`first`" in ln or "`later`" in ln]
    assert "`first`" in lines[first] and "`later`" in lines[later]
    assert "If the commander is the source: late, 6 to 8." in lines[first] and "Cards go inside `first`." in lines[later]
    assert lines[-1].startswith("**Curve** 2.8 to 3.2") and "**Creatures** 20 to 25" in lines[-1]


def test_regenerate_rewrites_marked_blocks_only_and_reports_slugs_without_markers():
    text = "intro\n<!-- BEGIN table:toy -->\nSTALE\n<!-- END table:toy -->\nprose stays\n"
    new, missing = gen.regenerate(text, {"toy": ARCH, "other": ARCH})
    assert missing == ["other"] and new.startswith("intro\n<!-- BEGIN table:toy -->\n| Function |") and new.endswith("prose stays\n")
    assert "STALE" not in new and gen.regenerate(new, {"toy": ARCH})[0] == new  # idempotent


def test_the_real_tables_match_archetypes_json():
    archetypes = json.loads(gen.JSON_PATH.read_text(encoding="utf-8"))["archetypes"]
    old = gen.MD_PATH.read_text(encoding="utf-8")
    new, missing = gen.regenerate(old, archetypes)
    assert missing == [], f"no table block for {missing}"
    assert new == old, "references/archetypes.md is out of date: run scripts/gen_archetype_tables.py"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
