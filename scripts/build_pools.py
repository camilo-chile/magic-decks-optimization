#!/usr/bin/env python3
"""Phase 2 pools: every owned card that fits a commander's color identity, and the owned commander candidates.

Run it with the "Run Python File" button (no arguments). No network. It reads
  - data/cache/collection_owned.json (scripts/collection_stages.py: every owned row with its exact printing, language and
    the deck that holds it now), and
  - the Scryfall oracle bulk file in data/cache/ (identity, legality, layout, Oracle text),
and writes into data/model/phase2/
  - pool-<slug>.json for the commander of each scanned deck (Toph, Azula, Ezio): every owned card legal in that identity,
    with Oracle text, copies by language, the decks that hold them now and the exact printings;
  - legends.json and legends.md: the owned legendary creatures (and cards that can be a commander) with the size of the
    pool each would have from Spanish copies only and from any language, for choosing the commander of the Spanish deck.

The whole collection is available to every deck (a card sitting in a deck now can move to another one); "held_by" only says
where it is today. Cards that must be turned over (reversible layouts) and cards not legal in Commander are left out.
Tokens and proxy rows are not cards of a pool. Names that Scryfall does not know are listed as problems.
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allocation_model as am  # noqa: E402
import check_list as cl  # noqa: E402
import layer_a as la  # noqa: E402

ROOT = la.ROOT
OWNED_PATH = ROOT / "data" / "cache" / "collection_owned.json"
CONFIG_PATH = ROOT / "decks" / "phase2.json"
OUT_DIR = ROOT / "data" / "model" / "phase2"
LEGENDS_SHOWN = 80


def face_text(card, field):
    """A text field of a card; a two-faced card joins the text of both faces with ' // '."""
    if card.get(field):
        return card[field]
    return " // ".join(face.get(field) or "" for face in card.get("card_faces") or [])


def resolve(name, index):
    """The Scryfall card of a ManaBox name (full name, then the front face), or None."""
    return index.get(la.normalize(name)) or index.get(la.normalize(name.split(" // ")[0]))


def owned_cards(records, index):
    """({oracle id: {"copies", "by_language", "by_deck", "printings"}}, [unknown names]) from the owned rows.

    Tokens and proxy rows are not counted; "by_deck" uses the deck slug, or "free" for the rest of the collection."""
    owned, unknown = {}, []
    for r in records:
        if r["token"] or r["proxy"]:
            continue
        card = resolve(r["name"], index)
        if card is None:
            unknown.append(r["name"])
            continue
        entry = owned.setdefault(card["oracle_id"], {"copies": 0, "by_language": Counter(), "by_deck": Counter(),
                                                      "printings": []})
        entry["copies"] += r["quantity"]
        entry["by_language"][r["language"]] += r["quantity"]
        entry["by_deck"][r["deck"] or "free"] += r["quantity"]
        entry["printings"].append({"set": r["set"], "number": r["number"], "finish": r["finish"], "language": r["language"],
                                   "condition": r["condition"], "quantity": r["quantity"], "deck": r["deck"] or "free"})
    return owned, sorted(set(unknown))


def usable(card):
    """Legal in Commander and not a card that must be turned over."""
    return (card.get("legalities") or {}).get("commander") == "legal" and not cl.needs_flipping(card)


def pool(identity, owned, by_oid, language=None, exclude=()):
    """Entries for every owned, usable card inside `identity`; with a language only copies of that language count."""
    out = []
    for oid, have in owned.items():
        card = by_oid.get(oid)
        if card is None or oid in exclude or not usable(card) or not am.fits_identity(card, identity):
            continue
        copies = have["by_language"][language] if language else have["copies"]
        if copies <= 0:
            continue
        out.append({"name": card["name"], "oracle_id": oid, "type": card.get("type_line"), "cmc": card.get("cmc"),
                    "mana_cost": face_text(card, "mana_cost"), "oracle_text": face_text(card, "oracle_text"),
                    "color_identity": sorted(card.get("color_identity") or []),
                    "game_changer": bool(card.get("game_changer")), "basic": am.is_basic(card["name"]),
                    "copies": copies, "by_language": dict(have["by_language"]), "held_by": dict(have["by_deck"]),
                    "printings": [p for p in have["printings"] if not language or p["language"] == language]})
    out.sort(key=lambda c: c["name"])
    return out


def can_be_commander(card):
    type_line = card.get("type_line") or ""
    return ("Legendary" in type_line and "Creature" in type_line) or "can be your commander" in face_text(card, "oracle_text")


def legends(owned, by_oid):
    """One row per owned commander candidate with the size of its pool from Spanish copies and from any language."""
    rows = []
    for oid, have in owned.items():
        card = by_oid.get(oid)
        if card is None or not usable(card) or not can_be_commander(card):
            continue
        identity = set(card.get("color_identity") or [])
        rows.append({"name": card["name"], "oracle_id": oid, "color_identity": "".join(sorted(identity)) or "C",
                     "type": card.get("type_line"), "copies": have["copies"], "spanish_copies": have["by_language"]["es"],
                     "pool_es": len(pool(identity, owned, by_oid, "es", exclude={oid})),
                     "pool_any": len(pool(identity, owned, by_oid, None, exclude={oid})),
                     "held_by": dict(have["by_deck"])})
    rows.sort(key=lambda r: (r["spanish_copies"] == 0, -r["pool_es"], r["name"]))
    return rows


def legends_markdown(rows, shown=LEGENDS_SHOWN):
    lines = ["# Owned commander candidates (generated by scripts/build_pools.py)", "",
             "Sorted by the size of the pool a Spanish-only deck would have. Only candidates with a Spanish copy can lead "
             "the Spanish deck; the others are listed for the bilingual decks.", "",
             "| Commander | Identity | Spanish copies | Pool, Spanish only | Pool, any language | Held by now |",
             "|---|---|---|---|---|---|"]
    for r in rows[:shown]:
        held = ", ".join(f"{k} {v}" for k, v in sorted(r["held_by"].items()))
        lines.append(f"| {r['name']} | {r['color_identity']} | {r['spanish_copies']} | {r['pool_es']} | {r['pool_any']} | {held} |")
    if len(rows) > shown:
        lines.append(f"\n{len(rows) - shown} more candidates are in legends.json.")
    return "\n".join(lines) + "\n"


def commander_of(slug, config, root=ROOT):
    """The commander name of a deck from its planned list, or None."""
    for deck in config.get("decks", []):
        if deck["slug"] == slug and deck.get("list") and (root / deck["list"]).exists():
            commanders, _, _ = la.parse_decklist((root / deck["list"]).read_text(encoding="utf-8"))
            return commanders[0]["name"] if commanders else None
    return None


def main():
    if not OWNED_PATH.exists():
        print("Run scripts/collection_stages.py first (data/cache/collection_owned.json is missing).")
        sys.exit(2)
    bulk = la.latest_bulk()
    if bulk is None:
        print("No oracle bulk file in data/cache/. Run scripts/collect_research_data.py first.")
        sys.exit(2)
    cards = list(la.iter_cards(bulk))
    index = la.build_index(cards)
    by_oid = {c.get("oracle_id"): c for c in cards}
    records = json.loads(OWNED_PATH.read_text(encoding="utf-8"))["cards"]
    owned, unknown = owned_cards(records, index)
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for deck in config["decks"]:
        name = commander_of(deck["slug"], config)
        commander = resolve(name, index) if name else None
        if commander is None:
            print(f"{deck['slug']}: no commander yet, no pool written")
            continue
        language = "es" if deck.get("languages") == "es" else None
        entries = pool(set(commander.get("color_identity") or []), owned, by_oid, language, exclude={commander["oracle_id"]})
        data = {"slug": deck["slug"], "commander": commander["name"], "language_policy": deck.get("languages"),
                "color_identity": sorted(commander.get("color_identity") or []), "cards": entries}
        (OUT_DIR / f"pool-{deck['slug']}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"{deck['slug']}: {len(entries)} owned cards fit {''.join(data['color_identity']) or 'C'}")
    rows = legends(owned, by_oid)
    (OUT_DIR / "legends.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT_DIR / "legends.md").write_text(legends_markdown(rows), encoding="utf-8")
    print(f"{len(rows)} commander candidates in legends.md; unknown names: {unknown or 'none'}")


if __name__ == "__main__":
    main()
