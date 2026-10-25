"""Build the `playbook` dataset of the dashboard from the hand-written deck guides.

Reads data/model/dashboard/playbook-<deck>.json (per deck: `sections`, the plan of play, and `cards`, one row per card
with its role and how to play it, each text keyed by language) and the `combo` rows of guide.json (the Commander Salt top
combos with their steps), and writes data/model/dashboard/playbook.json, a flat table of rows
  {id, deck, kind, lang, order, name, role, qty, title, meta, text}
with kind = section | card | combo. The dashboard page shows only the languages that exist in the rows.

Also checks that every deck guide covers exactly 100 cards (nonbasic rows plus the quantities of the basic-land rows) and
that every card of the final list has a row. Run from the VS Code "Run Python File" button; no arguments.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "data" / "model" / "dashboard"
DECKS = {
    "Toph": ("playbook-toph.json", "decks/measured/toph-the-first-metalbender/round3-step21.txt"),
    "Azula": ("playbook-azula.json", "decks/measured/fire-lord-azula/round4-step27.txt"),
    "Ezio": ("playbook-ezio.json", "decks/measured/ezio-auditore-da-firenze/round5-step40.txt"),
}
ROLES = {"commander", "engine", "mana", "draw", "tutor", "win", "removal", "defense", "land"}
BASIC = {"Plains", "Island", "Swamp", "Mountain", "Forest"}


def list_cards(path):
    out = {}
    for line in (ROOT / path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\d+)\s+(.+?)\s*$", line.strip())
        if m:
            out[m.group(2)] = int(m.group(1))
    return out


def main():
    rows = []
    for deck, (fname, list_path) in DECKS.items():
        guide = json.loads((DIR / fname).read_text(encoding="utf-8"))
        assert guide["deck"] == deck, (fname, guide["deck"])
        final = list_cards(list_path)
        have = {}
        for i, c in enumerate(guide["cards"], 1):
            assert c["role"] in ROLES, (deck, c["name"], c["role"])
            have[c["name"]] = c.get("qty", 1)
            for lang, text in c["play"].items():
                rows.append({"id": f"{deck.lower()}-card-{i}-{lang}", "deck": deck, "kind": "card", "lang": lang, "order": i,
                             "name": c["name"], "role": c["role"], "qty": c.get("qty", 1), "title": "", "meta": "", "text": text})
        missing = sorted(set(final) - set(have))
        extra = sorted(set(have) - set(final))
        total = sum(have.values())
        assert not missing and not extra and total == 100 and all(have[n] == final[n] for n in final), (deck, missing, extra, total)
        for s in guide["sections"]:
            for lang, text in s["text"].items():
                rows.append({"id": f"{deck.lower()}-{s['id']}-{lang}", "deck": deck, "kind": "section", "lang": lang, "order": s["order"],
                             "name": "", "role": "", "qty": "", "title": s["title"][lang], "meta": "", "text": text})
        print(deck, "ok:", len(guide["cards"]), "rows,", total, "cards,", len(guide["sections"]), "sections")
    for r in json.loads((DIR / "guide.json").read_text(encoding="utf-8"))["rows"]:
        if r.get("kind") == "combo":
            rows.append({"id": r["id"], "deck": r["deck"], "kind": "combo", "lang": r["lang"], "order": r["order"], "name": "", "role": "",
                         "qty": "", "title": r["title"], "meta": r["meta"], "text": r["text"]})
    (DIR / "playbook.json").write_text(json.dumps({"rows": rows}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("playbook.json:", len(rows), "rows")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
