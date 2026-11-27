"""Build the `playbook` dataset of the dashboard: the deck pages of the four current decks.

Reads `data/model/dashboard/cards-<deck>.json` (written by scripts/dashboard_cards.py: the 100 cards with the printed name of
the owner's copy, role, mana cost and type line) and, when it exists, the hand-written guide
`data/model/dashboard/guide-<deck>.json`:

  {"sections": [{"title": ..., "text": ...}],            the plan of play, in order
   "combos":   [{"title": ..., "meta": ..., "text": ...}], Commander Salt combos, steps one per line
   "cards":    {"<English card name>": "how to use it in this deck"}}

A guide must cover every card of the list (English names, basics included) and nothing else, or the script stops: a
stale guide never reaches the page. `guide-<deck>.json` is the Spanish guide; an optional `guide-<deck>.en.json` with the
same shape is its English translation (combo requirement lines start with "Needs:"). The page shows a language selector
once both exist; the card rows keep the printed name of the owner's copy in both languages. Without a guide a card row
shows its mana cost and type line, and the page says the guide is pending. Writes `data/model/dashboard/playbook.json`.
No network, no arguments.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "data" / "model" / "dashboard"
DECKS = {"toph": "Toph", "azula": "Azula", "ezio": "Ezio", "kilo": "Kilo"}
LANGS = {"es": "", "en": ".en"}  # language -> guide file suffix; Spanish is the source, English its translation
PENDING = ("Guía en preparación", "La guía de juego de esta lista (plan, combos y cómo usar cada carta) se escribe en el "
           "próximo paso. Por ahora cada carta muestra su costo y su tipo.")


def read_guide(path, cards, es_guide=None):
    """The guide at `path`, checked against the list and, for a translation, against the Spanish guide's shape."""
    if not path.exists():
        return None
    guide = json.loads(path.read_text(encoding="utf-8"))
    names = {c["name_en"] for c in cards}
    extra, missing = set(guide["cards"]) - names, names - set(guide["cards"])
    if extra or missing:
        sys.exit(f"{path.name} does not match the list: missing {sorted(missing)[:8]}, extra {sorted(extra)[:8]}")
    if es_guide is not None:
        for part in ("sections", "combos"):
            if len(guide.get(part, [])) != len(es_guide.get(part, [])):
                sys.exit(f"{path.name}: {len(guide.get(part, []))} {part}, the Spanish guide has {len(es_guide.get(part, []))}")
        empty = [k for k, v in guide["cards"].items() if not str(v).strip()]
        if empty:
            sys.exit(f"{path.name}: empty card rows {empty[:8]}")
    return guide


def add_rows(rows, key, deck, cards, guide, lang):
    sections = guide["sections"] if guide else [{"title": PENDING[0], "text": PENDING[1]}]
    for i, s in enumerate(sections, 1):
        rows.append({"id": f"{key}-section-{i}-{lang}", "deck": deck, "kind": "section", "lang": lang, "order": i, "name": "",
                     "role": "", "qty": None, "title": s["title"], "meta": "", "text": s["text"]})
    for i, c in enumerate((guide or {}).get("combos", []), 1):
        rows.append({"id": f"{key}-combo-{i}-{lang}", "deck": deck, "kind": "combo", "lang": lang, "order": i, "name": "",
                     "role": "", "qty": None, "title": c["title"], "meta": c.get("meta", ""), "text": c["text"]})
    for c in cards:
        facts = " · ".join(x for x in (c["mana_cost"], c["type_line"]) if x)
        text = guide["cards"][c["name_en"]] if guide else facts
        rows.append({"id": f"{key}-card-{c['order']}-{lang}", "deck": deck, "kind": "card", "lang": lang, "order": c["order"],
                     "name": c["name"], "role": c["role"], "qty": c["qty"], "title": "",
                     "meta": facts + (" · " + c["set"] + " " + str(c["number"]) if c.get("set") else ""), "text": text})


def main():
    rows = []
    for key, deck in DECKS.items():
        cards = json.loads((DIR / f"cards-{key}.json").read_text(encoding="utf-8"))["rows"]
        es_guide = read_guide(DIR / f"guide-{key}.json", cards)
        add_rows(rows, key, deck, cards, es_guide, "es")
        en_guide = read_guide(DIR / f"guide-{key}{LANGS['en']}.json", cards, es_guide) if es_guide else None
        if en_guide:
            add_rows(rows, key, deck, cards, en_guide, "en")
        print(f"{deck}: {sum(c['qty'] for c in cards)} cards, guide {'es' if es_guide else 'pending'}"
              f"{' + en' if en_guide else ''}", flush=True)
    (DIR / "playbook.json").write_text(json.dumps({"rows": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"playbook.json: {len(rows)} rows")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
