#!/usr/bin/env python3
"""Layer A, offline part: deterministic gate and card-facts file for Commander decklists.

Run it with the "Run Python File" button (no arguments). It needs no network: it reads the
Scryfall oracle bulk file that collect_research_data.py cached under data/cache/ and writes,
for every deck it finds,

  decks/<slug>.layer_a.json   floor, flags, rejections and provenance of each check
  decks/<slug>.cards.json     card facts (oracle text, type line, mana value, identity)

Decks read, in order (the first existing file per commander wins):
  decks/<slug>.txt            reference or final list, `1 Card Name` per line
  data/raw/Toph.txt           the owner's current Toph deck (ManaBox export), Toph only

What this part checks (docs/power-scale.md, Layer A): name resolution, 100 cards, singleton,
Commander legality, color identity, Game Changers, extra-turn cards and mass land denial by
card text. Spellbook combos, the own combo detector and the speed-risk flag are separate
steps; the report lists them under `pending_checks`, so a result here is never a final
eligibility answer.
"""
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from collect_research_data import COMMANDERS, iter_cards  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "cache"
DECKS = ROOT / "decks"
FALLBACK_DECKS = {"toph-the-first-metalbender": ROOT / "data" / "raw" / "Toph.txt"}
RULES_AS_OF = "2026-02-09"  # Wizards Brackets update the snapshot is pinned to (beta)

LINE_RE = re.compile(r"^(\d+)\s+(.+?)(?:\s+\(([A-Za-z0-9]+)\)\s+(\S+))?\s*$")
BASIC_TYPE = "Basic Land"

# Wizards' examples of mass land denial (Brackets announcement, 2025-02-11): "four or more
# lands per player" destroyed, exiled, bounced, kept tapped or changed in what they produce.
WIZARDS_MLD_EXAMPLES = {"armageddon", "ruination", "sunder", "winter orb", "blood moon"}
MLD_PATTERNS = [
    re.compile(r"destroy (all|each) (other )?(nonbasic |basic )?lands?"),
    re.compile(r"exile (all|each) (other )?(nonbasic |basic )?lands?"),
    re.compile(r"return (all|each) (other )?(nonbasic |basic )?lands?"),
    re.compile(r"sacrifices? (all|each|x|four|five|six|seven) [^.\n]*lands"),
    re.compile(r"nonbasic lands are mountains"),
]
EXTRA_TURN_GRANT_RE = re.compile(
    r"takes? (an |another )?(extra|additional) turns?|(extra|additional) turn after this one"
)
EXTRA_TURN_FORBID_RE = re.compile(r"can't take (an )?(extra|additional) turns?")
TUTOR_RE = re.compile(r"search your library for (?![^.\n]*\b(basic|land|lands)\b)")

# Commander text that multiplies a flagged card (power-scale: commander effects row).
COMMANDER_MULTIPLIERS = {
    "fire lord azula": "copies every spell cast while she attacks, so one extra-turn spell "
    "gives two extra turns; counted as 1 card with a review note (power-scale v0.6)",
}


def normalize(name):
    """Lower-case a card name and unify apostrophes so lookups are forgiving."""
    return name.replace("’", "'").strip().casefold()


def build_index(cards):
    """Map normalized full names and face names to the card object."""
    index = {}
    for card in cards:
        name = card.get("name") or ""
        index.setdefault(normalize(name), card)
    for card in cards:  # faces second so a full name always wins over a face name
        for face in card.get("card_faces") or []:
            if face.get("name"):
                index.setdefault(normalize(face["name"]), card)
    return index


def parse_decklist(text):
    """Return (commanders, main, bad_lines). Entries: {qty, name, set, num}."""
    commanders, main, bad = [], [], []
    section = "MAIN"
    for raw in text.splitlines():
        line = raw.strip().lstrip("﻿")
        if not line:
            if section.startswith("COMMANDER"):
                section = "MAIN"  # ManaBox ends the commander block with a blank line
            continue
        if line.startswith("//"):
            section = line[2:].strip().upper() or "MAIN"
            continue
        m = LINE_RE.match(line)
        if not m:
            bad.append(line)
            continue
        entry = {"qty": int(m.group(1)), "name": m.group(2).strip(),
                 "set": (m.group(3) or "").lower(), "num": m.group(4) or ""}
        (commanders if section.startswith("COMMANDER") else main).append(entry)
    return commanders, main, bad


def card_text(card):
    """Oracle text of a card, joining the faces of multi-faced cards."""
    parts = [card.get("oracle_text") or ""]
    parts += [f.get("oracle_text") or "" for f in card.get("card_faces") or []]
    return "\n".join(p for p in parts if p)


def card_facts(card):
    """The facts a judge may see: no prices, no Game Changer flag, no intent."""
    faces = card.get("card_faces") or []
    return {
        "name": card.get("name"),
        "oracle_id": card.get("oracle_id"),
        "mana_cost": card.get("mana_cost") or (faces[0].get("mana_cost") if faces else ""),
        "mana_value": card.get("cmc"),
        "type_line": card.get("type_line"),
        "oracle_text": card_text(card),
        "color_identity": card.get("color_identity") or [],
    }


def singleton_limit(card):
    """How many copies a deck may hold of this card (basic lands and 'any number' cards)."""
    text = card_text(card).lower()
    if BASIC_TYPE in (card.get("type_line") or "") or "any number of cards named" in text:
        return None
    m = re.search(r"up to (\w+) cards named", text)
    words = {"seven": 7, "nine": 9}
    if m:
        return words.get(m.group(1), int(m.group(1)) if m.group(1).isdigit() else 1)
    return 1


def mld_reason(card):
    """Why a card is flagged as mass land denial, or None. Heuristic and over-inclusive."""
    if normalize(card.get("name") or "") in WIZARDS_MLD_EXAMPLES:
        return "Wizards example of mass land denial"
    text = card_text(card).lower()
    for pattern in MLD_PATTERNS:
        if pattern.search(text):
            return f"oracle text matches /{pattern.pattern}/"
    return None


def is_extra_turn_card(card):
    """True when the text gives an extra turn; cards that only skip or forbid them are not."""
    text = EXTRA_TURN_FORBID_RE.sub("", card_text(card).lower())
    return bool(EXTRA_TURN_GRANT_RE.search(text))


def analyze(commander_entries, main_entries, index, slug=None):
    """Run the offline checks. Returns (report dict, list of card facts)."""
    reasons, flags, notes = [], [], []
    entries = [("commander", e) for e in commander_entries] + [("main", e) for e in main_entries]

    resolved, unresolved = [], []
    for role, entry in entries:
        card = index.get(normalize(entry["name"]))
        if card is None:
            unresolved.append(entry["name"])
        else:
            resolved.append((role, entry, card))
    total = sum(e["qty"] for _, e in entries)
    recognized = sum(e["qty"] for _, e, _ in resolved)

    if unresolved:
        reasons.append(f"STOP: {len(unresolved)} names not recognized as English card names: {unresolved[:10]}")
    if not commander_entries:
        reasons.append("STOP: no commander (expected a '// Commander' section); Layer A cannot run "
                       "without it (Spellbook would count it as an ordinary card)")
    if total != 100:
        reasons.append(f"deck has {total} cards, expected 100")
    if recognized != total:
        reasons.append(f"recognized {recognized} of {total} cards")

    commanders = [c for r, _, c in resolved if r == "commander"]
    identity = set()
    for c in commanders:
        identity |= set(c.get("color_identity") or [])
    if commanders and not any(
        "Legendary" in (c.get("type_line") or "") or "can be your commander" in card_text(c).lower()
        for c in commanders
    ):
        reasons.append("the commander is not a legendary creature nor 'can be your commander'")

    counts = Counter()
    for _, entry, card in resolved:
        counts[card.get("oracle_id") or card.get("name")] += entry["qty"]
    by_id = {(c.get("oracle_id") or c.get("name")): c for _, _, c in resolved}
    singleton_bad = []
    for key, qty in counts.items():
        limit = singleton_limit(by_id[key])
        if limit is not None and qty > limit:
            singleton_bad.append(f"{by_id[key]['name']} x{qty}")
    if singleton_bad:
        reasons.append(f"singleton violated: {singleton_bad}")

    illegal = sorted({
        f"{c['name']} ({(c.get('legalities') or {}).get('commander')})"
        for _, _, c in resolved
        if (c.get("legalities") or {}).get("commander") != "legal"
    })
    if illegal:
        reasons.append(f"not Commander-legal (banned or not legal): {illegal}")
    outside = sorted({c["name"] for r, _, c in resolved
                      if r == "main" and not set(c.get("color_identity") or []) <= identity})
    if outside and commanders:
        reasons.append(f"outside the commander's color identity: {outside}")

    # Game Changers: the commander counts.
    gc_names = sorted({c["name"] for _, _, c in resolved if c.get("game_changer")})
    gc_floor = 4 if len(gc_names) >= 4 else 3 if gc_names else 1

    # Extra turns.
    et_names = sorted({c["name"] for _, _, c in resolved if is_extra_turn_card(c)})
    et_floor = 2 if et_names else 1
    if len(et_names) >= 2:
        reasons.append(f"policy reject: {len(et_names)} extra-turn cards {et_names} "
                       "(power-scale: 2 or more cards)")
    mult = [COMMANDER_MULTIPLIERS[normalize(c["name"])] for c in commanders
            if normalize(c["name"]) in COMMANDER_MULTIPLIERS]
    if et_names and mult:
        notes.append(f"extra-turn card(s) {et_names} with a commander that multiplies them: {mult[0]}")
    if et_names:
        flags.append({"flag": "extra_turn", "cards": et_names, "provenance": "curated (oracle text)"})

    # Mass land denial.
    mld = {}
    for _, _, c in resolved:
        why = mld_reason(c)
        if why:
            mld[c["name"]] = why
    mld_floor = 4 if mld else 1
    if mld:
        flags.append({"flag": "mass_land_denial", "cards": mld, "provenance": "heuristic, over-inclusive"})

    floor = max(gc_floor, et_floor, mld_floor)
    nonland = [c for _, e, c in resolved if "Land" not in (c.get("type_line") or "")
               for _ in range(e["qty"])]
    tutors = sorted({c["name"] for _, _, c in resolved if TUTOR_RE.search(card_text(c).lower())})

    report = {
        "slug": slug,
        "rules_as_of": RULES_AS_OF,
        "beta": True,
        "commanders": [c["name"] for c in commanders],
        "total_cards": total,
        "recognized_cards": recognized,
        "unresolved": unresolved,
        "floor": floor,
        "rejected": bool(reasons),
        "reasons": reasons,
        "flags": flags,
        "review_notes": notes,
        "checks": {
            "game_changers": {"count": len(gc_names), "cards": gc_names, "floor": gc_floor,
                              "provenance": "official (Scryfall game_changer)"},
            "extra_turns": {"count": len(et_names), "cards": et_names, "floor": et_floor,
                            "provenance": "curated (oracle text); count policy v0.6"},
            "mass_land_denial": {"cards": mld, "floor": mld_floor,
                                 "provenance": "heuristic, over-inclusive"},
        },
        "descriptive": {
            "tutors": tutors,
            "land_cards": total - len(nonland),
            "average_mana_value_nonland": round(sum(c.get("cmc") or 0 for c in nonland) / len(nonland), 2)
            if nonland else None,
        },
        "pending_checks": [
            "Commander Spellbook estimate-bracket and find-my-combos (step 2.3)",
            "own combo detector: full Spellbook bulk match and curated hazards (step 2.4)",
            "speed-risk flag from the Monte Carlo script (step 2.6)",
        ],
        "complete": False,
    }
    facts = sorted((card_facts(by_id[k]) for k in counts), key=lambda f: f["name"])
    return report, facts


def latest_bulk():
    """The newest oracle bulk file in the cache, or None."""
    files = sorted(CACHE.glob("oracle-cards-*.json*"))
    return files[-1] if files else None


def deck_sources():
    """(slug, path) of every deck found, in commander order."""
    found = []
    for slug in COMMANDERS:
        for path in (DECKS / f"{slug}.txt", FALLBACK_DECKS.get(slug)):
            if path and path.exists():
                found.append((slug, path))
                break
    return found


def main():
    """Resolve every found deck against the bulk file and write its two output files."""
    bulk = latest_bulk()
    if bulk is None:
        print("No oracle bulk file in data/cache/. Run scripts/collect_research_data.py first.")
        sys.exit(2)
    sources = deck_sources()
    if not sources:
        print("No decks found (decks/<slug>.txt or data/raw/Toph.txt).")
        sys.exit(2)
    print(f"Reading {bulk.name} ...", flush=True)
    index = build_index(list(iter_cards(bulk)))
    print(f"{len(index)} card and face names indexed.\n")

    DECKS.mkdir(exist_ok=True)
    failed = False
    for slug, path in sources:
        text = path.read_text(encoding="utf-8-sig")
        commanders, main_cards, bad = parse_decklist(text)
        report, facts = analyze(commanders, main_cards, index, slug)
        if bad:
            report["reasons"].append(f"{len(bad)} unparsed lines: {bad[:3]}")
            report["rejected"] = True
        report["source"] = str(path.relative_to(ROOT)).replace("\\", "/")
        report["bulk_file"] = bulk.name
        report["run_at_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        (DECKS / f"{slug}.layer_a.json").write_text(
            json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        (DECKS / f"{slug}.cards.json").write_text(
            json.dumps(facts, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"== {slug}  ({report['source']})")
        print(f"   cards {report['total_cards']}, recognized {report['recognized_cards']}, "
              f"floor {report['floor']}, game changers {report['checks']['game_changers']['count']}, "
              f"extra-turn cards {report['checks']['extra_turns']['count']}, "
              f"mass land denial {len(report['checks']['mass_land_denial']['cards'])}")
        for reason in report["reasons"]:
            print(f"   REJECT/STOP: {reason}")
        for note in report["review_notes"]:
            print(f"   note: {note}")
        failed = failed or report["rejected"]
        print(f"   wrote decks/{slug}.layer_a.json and decks/{slug}.cards.json\n")
    print("RESULT:", "PROBLEMS FOUND (see above)" if failed else "OK (offline checks only; "
          "Spellbook, combo detector and speed flag are still pending)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
