#!/usr/bin/env python3
"""Regenerate the function tables of the skill's references/archetypes.md from archetypes.json (they are twins).

Run it with the "Run Python File" button (no arguments) after editing archetypes.json: it rewrites every block between
`<!-- BEGIN table:<slug> -->` and `<!-- END table:<slug> -->` in
.claude/skills/commander-deckbuilding/references/archetypes.md and leaves the prose alone. `--check` writes nothing and exits
with 1 when the tables are out of date (tests/test_gen_archetype_tables.py runs the same comparison). No network.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / ".claude" / "skills" / "commander-deckbuilding"
JSON_PATH = SKILL / "archetypes.json"
MD_PATH = SKILL / "references" / "archetypes.md"
BASE_LABELS = {"ramp": "Ramp", "draw": "Draw (nets cards)", "removal": "Removal (spot answers)", "wipe": "Wipes",
               "protection": "Commander protection"}


def alt_note(f):
    out = []
    for key, label in (("if_commander_is_payoff", "payoff"), ("if_commander_is_source", "source")):
        if key in f:
            a = f[key]
            out.append(f"If the commander is the {label}: {a['needed_by']}, {a['min']} to {a['target']}.")
    if "if_secondary_modifier" in f:
        a = f["if_secondary_modifier"]
        out.append(f"As a secondary modifier: {a['min']} to {a['target']} ({a['tier']}).")
    if "counts_inside" in f:
        out.append(f"Cards go inside `{f['counts_inside']}`.")
    if "unit" in f:
        out.append(f"Unit: {f['unit']}; ceiling {f.get('ceiling')}.")
    return " ".join(out)


def table(archetype):
    """The markdown table (lands, base floors, gate functions, support lines) and the curve line of one archetype."""
    rows = ["| Function | Tier | Min | Target | Needed by | Reason |", "|---|---|---|---|---|---|"]
    low, high = archetype["land_band"]
    rows.append(f"| Lands | band | {low} | {high} | | {archetype['land_why']} |")
    for key, label in BASE_LABELS.items():
        b = archetype["base"][key]
        rows.append(f"| {label} | base | {b['min']} | {b['target']} | | {b['why']} |")
    functions = archetype["functions"].items()
    for name, f in [x for x in functions if x[1]["tier"] == "gate"] + [x for x in functions if x[1]["tier"] == "support"]:
        tail = alt_note(f)
        rows.append(f"| `{name}` | {f['tier']} | {f['min']} | {f['target']} | {f['needed_by']} | {f['why']}{(' ' + tail) if tail else ''} |")
    c = archetype["curve"]
    rows += ["", f"**Curve** {c['avg_mv'][0]} to {c['avg_mv'][1]} (average MV of nonland cards). **Creatures** "
                 f"{c['creature_count'][0]} to {c['creature_count'][1]}. {c['why']}"]
    return "\n".join(rows)


def block(slug, archetype):
    return f"<!-- BEGIN table:{slug} -->\n{table(archetype)}\n<!-- END table:{slug} -->"


def regenerate(text, archetypes):
    """(new text, [slugs with no marker block in the text]) with every marked table rebuilt from the JSON."""
    missing = []
    for slug, archetype in archetypes.items():
        pattern = re.compile(rf"<!-- BEGIN table:{re.escape(slug)} -->.*?<!-- END table:{re.escape(slug)} -->", re.S)
        if not pattern.search(text):
            missing.append(slug)
            continue
        text = pattern.sub(lambda m: block(slug, archetype), text, count=1)
    return text, missing


def main(argv=None):
    check = "--check" in (argv if argv is not None else sys.argv[1:])
    archetypes = json.loads(JSON_PATH.read_text(encoding="utf-8"))["archetypes"]
    old = MD_PATH.read_text(encoding="utf-8")
    new, missing = regenerate(old, archetypes)
    for slug in missing:
        print(f"no table block for {slug} in {MD_PATH.name}: add the BEGIN/END markers where its table goes")
    if check:
        print("tables out of date" if new != old else "tables match archetypes.json")
        return 1 if new != old or missing else 0
    if new != old:
        MD_PATH.write_text(new, encoding="utf-8")
        print(f"{MD_PATH.name} updated")
    else:
        print(f"{MD_PATH.name} already matches archetypes.json")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
