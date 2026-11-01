#!/usr/bin/env python3
"""Bracket check (Layer A) for the Phase 2 lists in decks/phase2/.

Run it with the "Run Python File" button (no arguments) to check every decks/phase2/<slug>.txt, or pass files:
`python scripts/check_phase2_bracket.py decks/phase2/<slug>.txt`. No network. It reuses scripts/layer_a.py (the Scryfall bulk
file, Commander Spellbook and the curated hazards in data/) and checks each list against Bracket 3: 100 cards, singleton,
Commander legality, color identity, Game Changers, extra-turn cards, mass land denial and flagged combos. It writes
`decks/reports/bracket-<slug>.md` and prints the verdict; a REJECT line or a floor above 3 means the list is not ready.
Reversible cards (transform, modal double-faced, meld and flip layouts) are reported as well: the owner never plays them.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_list as cl  # noqa: E402
import layer_a as la  # noqa: E402

ROOT = la.ROOT
PLANS_DIR = ROOT / "decks" / "phase2"
REPORTS_DIR = ROOT / "decks" / "reports"
TARGET = 3


def verdict(report):
    """'PASS' when the list has no rejection and its floor is within the target bracket, else 'FAIL'."""
    return "PASS" if report["floor_ok_so_far"] and not report["rejected"] else "FAIL"


def report_markdown(slug, report, reversible=()):
    checks = report["checks"]
    lines = [f"# Bracket check: {slug} ({verdict(report)})", "",
             f"Target Bracket {report['target_bracket']}; floor found {report['floor']}; "
             f"{report['total_cards']} cards, {report['recognized_cards']} recognized.", "",
             f"- Game Changers ({checks['game_changers']['count']}): {', '.join(checks['game_changers']['cards']) or 'none'}",
             f"- Extra-turn cards ({checks['extra_turns']['count']}): {', '.join(checks['extra_turns']['cards']) or 'none'}",
             f"- Mass land denial: {', '.join(checks['mass_land_denial']['cards']) or 'none'}",
             f"- Reversible cards (never allowed): {', '.join(reversible) or 'none'}"]
    spellbook = report.get("spellbook")
    if spellbook:
        lines += ["", f"## Spellbook: {spellbook['included_total']} variants inside the list, "
                      f"{len(spellbook['included_flagged'])} flagged, {spellbook['almost_included_total']} one card away", ""]
        lines += [f"- floor {r['floor']} [{r['kind']}] {r['cards']} (tag {r['bracket_tag']})" for r in spellbook["included_flagged"][:20]]
    for row in report.get("curated_hazards", []):
        lines.append(f"- HAZARD floor {row['floor']}: {row['hazard']}: {row['reason']}")
    lines += ["", "## Rejections", ""] + ([f"- {r}" for r in report["reasons"]] or ["- none"])
    lines += ["", "## Notes to read", ""] + ([f"- {n}" for n in report["review_notes"]] or ["- none"])
    return "\n".join(lines) + "\n"


def check_file(path, index, spellbook, hazards, reports_dir=REPORTS_DIR):
    """Analyze one list; write the report; return (slug, report, reversible card names)."""
    path = Path(path)
    commanders, main_cards, bad = la.parse_decklist(path.read_text(encoding="utf-8-sig"))
    slug = path.stem
    report, _ = la.analyze(commanders, main_cards, index, slug, spellbook, hazards, TARGET)
    if bad:
        report["reasons"].append(f"{len(bad)} unparsed lines: {bad[:3]}")
        report["rejected"] = True
        report["floor_ok_so_far"] = False
    reversible = []
    for entry in main_cards + commanders:
        card = index.get(la.normalize(entry["name"])) or index.get(la.normalize(entry["name"].split(" // ")[0]))
        if card is not None and cl.needs_flipping(card):
            reversible.append(card["name"])
    if reversible:
        report["reasons"].append("reversible cards: " + "; ".join(sorted(set(reversible))))
        report["rejected"] = True
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / f"bracket-{slug}.md").write_text(report_markdown(slug, report, sorted(set(reversible))), encoding="utf-8")
    return slug, report, sorted(set(reversible))


def main(argv=None):
    files = [Path(a) for a in (argv if argv is not None else sys.argv[1:]) if not a.startswith("--")]
    files = files or sorted(PLANS_DIR.glob("*.txt"))
    if not files:
        print("No decks/phase2/<slug>.txt lists yet.")
        return 0
    bulk = la.latest_bulk()
    if bulk is None:
        print("No oracle bulk file in data/cache/. Run scripts/collect_research_data.py first.")
        return 2
    index = la.build_index(list(la.iter_cards(bulk)))
    spellbook = la.load_spellbook() if la.SPELLBOOK_SLIM.exists() else None
    hazards = la.load_hazards()
    failed = False
    for path in files:
        slug, report, _ = check_file(path, index, spellbook, hazards)
        print(f"{slug}: {verdict(report)} (floor {report['floor']}, target {TARGET}, "
              f"game changers {report['checks']['game_changers']['count']}, review items {report['review_items']})")
        for reason in report["reasons"]:
            print("  REJECT", reason)
        failed = failed or verdict(report) == "FAIL"
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
