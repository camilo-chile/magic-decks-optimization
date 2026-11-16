"""Build the `playbook` dataset of the dashboard: the deck pages of the four current decks.

Reads `data/model/dashboard/cards-<deck>.json` (written by scripts/dashboard_cards.py: the 100 cards with the printed name of
the owner's copy, role, mana cost and type line) and, when it exists, the hand-written guide
`data/model/dashboard/guide-<deck>.json`:

  {"sections": [{"title": ..., "text": ...}],            the plan of play, in order
   "combos":   [{"title": ..., "meta": ..., "text": ...}], Commander Salt combos, steps one per line
   "cards":    {"<English card name>": "how to use it in this deck"}}

A guide must cover every card of the list (English names, basics included) and nothing else, or the script stops: a
stale guide never reaches the page. Without a guide a card row shows its mana cost and type line, and the page says the
guide is pending. Writes `data/model/dashboard/playbook.json`. No network, no arguments.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "data" / "model" / "dashboard"
DECKS = {"toph": "Toph", "azula": "Azula", "ezio": "Ezio", "kilo": "Kilo"}
PENDING = ("Guía en preparación", "La guía de juego de esta lista (plan, combos y cómo usar cada carta) se escribe en el "
           "próximo paso. Por ahora cada carta muestra su costo y su tipo.")


def main():
    rows = []
    for key, deck in DECKS.items():
        cards = json.loads((DIR / f"cards-{key}.json").read_text(encoding="utf-8"))["rows"]
        guide_path = DIR / f"guide-{key}.json"
        guide = json.loads(guide_path.read_text(encoding="utf-8")) if guide_path.exists() else None
        if guide:
            names = {c["name_en"] for c in cards}
            extra, missing = set(guide["cards"]) - names, names - set(guide["cards"])
            if extra or missing:
                sys.exit(f"{guide_path.name} does not match the list: missing {sorted(missing)[:8]}, extra {sorted(extra)[:8]}")
        sections = guide["sections"] if guide else [{"title": PENDING[0], "text": PENDING[1]}]
        for i, s in enumerate(sections, 1):
            rows.append({"id": f"{key}-section-{i}-es", "deck": deck, "kind": "section", "lang": "es", "order": i, "name": "",
                         "role": "", "qty": None, "title": s["title"], "meta": "", "text": s["text"]})
        for i, c in enumerate((guide or {}).get("combos", []), 1):
            rows.append({"id": f"{key}-combo-{i}-es", "deck": deck, "kind": "combo", "lang": "es", "order": i, "name": "",
                         "role": "", "qty": None, "title": c["title"], "meta": c.get("meta", ""), "text": c["text"]})
        for c in cards:
            facts = " · ".join(x for x in (c["mana_cost"], c["type_line"]) if x)
            text = guide["cards"][c["name_en"]] if guide else facts
            rows.append({"id": f"{key}-card-{c['order']}-es", "deck": deck, "kind": "card", "lang": "es", "order": c["order"],
                         "name": c["name"], "role": c["role"], "qty": c["qty"], "title": "",
                         "meta": facts + (" · " + c["set"] + " " + str(c["number"]) if c.get("set") else ""), "text": text})
        print(f"{deck}: {sum(c['qty'] for c in cards)} cards, guide {'yes' if guide else 'pending'}", flush=True)
    (DIR / "playbook.json").write_text(json.dumps({"rows": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"playbook.json: {len(rows)} rows")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
