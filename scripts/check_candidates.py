#!/usr/bin/env python3
"""Run Layer A on every candidate list under decks/candidates/<slug>/*.txt.

Run it with the "Run Python File" button (no arguments). It needs no network: it reads the
Scryfall oracle bulk and the Spellbook slim file cached under data/cache/ and writes
decks/candidates/gate-report.json (one entry per list: floor, Game Changers, rejection reasons,
flagged combos, review notes) and prints a compact table.

A candidate is a real public list copied by hand from a Commander Salt deck page (Export list),
see decks/candidates/README.md for where each one came from and its site score. The gate is the
same Layer A as for the owner's decks, at target Bracket 3 (docs/power-scale.md).
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402

ROOT = la.ROOT
CANDIDATES = ROOT / "decks" / "candidates"
DEFAULT_OUT = CANDIDATES / "gate-report.json"


def main(out_path=None):
    """Gate every candidate list and write the report; exit 1 if any list could not be read."""
    out_path = Path(out_path) if out_path else DEFAULT_OUT
    bulk = la.latest_bulk()
    if bulk is None:
        print("No oracle bulk file in data/cache/. Run scripts/collect_research_data.py first.")
        sys.exit(2)
    files = sorted(CANDIDATES.glob("*/*.txt"))
    if not files:
        print("No candidate lists found under decks/candidates/<slug>/*.txt.")
        sys.exit(2)
    print(f"Reading {bulk.name} ...", flush=True)
    index = la.build_index(list(la.iter_cards(bulk)))
    spellbook = la.load_spellbook() if la.SPELLBOOK_SLIM.exists() else None
    hazards = la.load_hazards()
    rows = []
    unreadable = False
    for path in files:
        slug = path.parent.name
        try:
            text = path.read_text(encoding="utf-8-sig")
            commanders, main_cards, bad = la.parse_decklist(text)
            target = la.TARGET_BRACKET.get(slug, la.DEFAULT_TARGET)
            report, _ = la.analyze(commanders, main_cards, index, slug, spellbook, hazards, target)
        except Exception as exc:  # keep going: one bad file must not hide the others
            unreadable = True
            rows.append({"slug": slug, "file": path.name, "error": f"{type(exc).__name__}: {exc}"})
            continue
        if bad:
            report["reasons"].append(f"{len(bad)} unparsed lines: {bad[:3]}")
            report["rejected"] = True
            report["floor_ok_so_far"] = False
        sb = report.get("spellbook") or {}
        rows.append({
            "slug": slug,
            "file": path.name,
            "total_cards": report["total_cards"],
            "floor": report["floor"],
            "rejected": report["rejected"],
            "floor_ok_so_far": report["floor_ok_so_far"],
            "reasons": report["reasons"],
            "game_changers": report["checks"]["game_changers"]["cards"],
            "extra_turn_cards": report["checks"]["extra_turns"]["count"],
            "mass_land_denial": list(report["checks"]["mass_land_denial"]["cards"]),
            "flagged_combos": [
                {"floor": r["floor"], "kind": r["kind"], "cards": r["cards"]}
                for r in sb.get("included_flagged", [])
            ],
            "curated_hazards": [
                {"floor": r["floor"], "hazard": r["hazard"]} for r in report.get("curated_hazards", [])
            ],
            "review_notes": report["review_notes"],
        })
        status = "OK " if report["floor_ok_so_far"] else "NO "
        print(f"{status} {slug[:28]:<28} {path.name:<14} floor {report['floor']} "
              f"GC {len(report['checks']['game_changers']['cards'])} "
              f"flagged {len(sb.get('included_flagged', []))}"
              + (f"  STOP: {report['reasons'][0]}" if report["reasons"] else ""))
    out_path.write_text(json.dumps({
        "as_of_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "bulk_file": bulk.name,
        "rules_snapshot": la.RULES_AS_OF,
        "target_bracket": la.DEFAULT_TARGET,
        "lists": rows,
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {out_path}")
    sys.exit(1 if unreadable else 0)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
