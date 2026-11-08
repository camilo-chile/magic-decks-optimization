#!/usr/bin/env python3
"""Phase 2: write each deck as Moxfield "Paste in List" text with the exact printing of every physical copy.

Run it with the "Run Python File" button (no arguments). It reads the decks of decks/phase2.json, their lists in
decks/phase2/<slug>.txt (for the commander) and the copies each deck was given in data/model/phase2/assignment.json
(scripts/assign_copies.py), and writes decks/phase2/moxfield/<slug>.txt:

    // Commander
    1 Toph, the First Metalbender (TLA) 123
    1 Sol Ring (CMM) 400 *F*
    ...

Format from docs/research/moxfield-import-test-20261031.md: `AMOUNT CARDNAME (SETCODE) NUMBER *F*` (etched `*E*`), no
`// Main` header (Moxfield read it as a card). A card with no physical copy (a proxy commander, a loan) is written by
name only. Moxfield cannot store language or condition: those stay in the assignment and the pull list.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "decks" / "phase2.json"
ASSIGNMENT = ROOT / "data" / "model" / "phase2" / "assignment.json"
OUT_DIR = ROOT / "decks" / "phase2" / "moxfield"
FINISH = {"foil": " *F*", "etched": " *E*"}


def commanders_of(text):
    """Names under the `// Commander` header of a decklist."""
    names, inside = [], False
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("//"):
            inside = line.lower().startswith("// commander")
            continue
        if inside and line:
            names.append(line.split(" ", 1)[1].split(" (")[0].strip())
    return names


def card_lines(card):
    """Moxfield lines of one assigned card: one line per printing, the rest by name."""
    lines, given = [], 0
    for pick in card.get("picks", []):
        if not pick.get("set") or not pick.get("number"):  # a loan or an owed card has no scanned printing: by name
            continue
        qty = pick.get("qty", 1)
        given += qty
        lines.append(f"{qty} {card['name']} ({pick['set'].upper()}) {pick['number']}{FINISH.get(pick.get('foil'), '')}")
    if card["qty"] > given:
        lines.append(f"{card['qty'] - given} {card['name']}")
    return lines


def export(slug, deck_text, assigned):
    commanders = set(commanders_of(deck_text))
    head, body = [], []
    for card in assigned["cards"]:
        (head if card["name"] in commanders else body).extend(card_lines(card))
    return "\n".join(["// Commander", *head, "", *body]) + "\n"


def main():
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    assignment = json.loads(ASSIGNMENT.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for deck in config["decks"]:
        slug = deck["slug"]
        deck_text = (ROOT / "decks" / "phase2" / f"{slug}.txt").read_text(encoding="utf-8-sig")
        text = export(slug, deck_text, assignment["decks"][slug])
        total = sum(int(line.split(" ", 1)[0]) for line in text.splitlines() if line[:1].isdigit())
        (OUT_DIR / f"{slug}.txt").write_text(text, encoding="utf-8")
        print(f"{slug}: {total} cards -> decks/phase2/moxfield/{slug}.txt")
        if total != 100:
            print(f"  WARNING: {slug} has {total} cards, not 100")
    return 0


if __name__ == "__main__":
    sys.exit(main())
