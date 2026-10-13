#!/usr/bin/env python3
"""Owned-card inventory: ManaBox collection CSV -> one record per card (oracle ID).

Run it with the "Run Python File" button (no arguments). No network. It reads
data/raw/ManaBox_Collection.csv (every binder and deck of the export) and the Scryfall oracle
bulk file cached under data/cache/, and writes data/cache/collection_inventory.json plus a
short text summary next to it. Phases 7 and 8 read that file: an owned copy costs 0, and one
physical copy can sit in only one deck (decision D5).

Per card: total copies, copies by language, the printings (set, number, language, finish,
condition) and the places (binder or deck name and type). Problems are listed, never hidden:
names the bulk file does not know, proxies, languages other than English or Spanish, and
conditions worse than lightly played (decision D6).

RESERVED_BINDERS (decision O3, closed 2026-10-12): the owner's other decks are out of scope, so
nothing is reserved and the set stays empty. The mechanism remains: names listed there mark their
cards `reserved` and the 3 project decks would never use them.
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "raw" / "ManaBox_Collection.csv"
OUT_PATH = ROOT / "data" / "cache" / "collection_inventory.json"
RESERVED_BINDERS = set()  # O3 closed: no other decks are considered
PROJECT_DECKS = {"toph": "toph-the-first-metalbender", "azula": "fire-lord-azula"}
LANGUAGES_OK = {"en", "es"}
CONDITIONS_OK = {"near_mint", "mint", "excellent", "lightly_played", "good", ""}  # ManaBox spellings vary


def read_rows(path):
    """The rows of a ManaBox CSV as dicts with lower-case header names."""
    with open(path, encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        reader.fieldnames = [h.strip().lower() for h in reader.fieldnames or []]
        return list(reader)


def truthy(value):
    return str(value or "").strip().lower() in ("true", "1", "yes")


def build_inventory(rows, index, reserved=frozenset()):
    """Aggregate CSV rows into the inventory dict. `index` is layer_a.build_index(...)."""
    reserved = {r.strip().lower() for r in reserved}
    cards = {}
    problems = defaultdict(list)
    totals = Counter()
    for r in rows:
        qty = int(r.get("quantity") or 1)
        name = (r.get("name") or "").strip()
        binder = (r.get("binder name") or "").strip()
        btype = (r.get("binder type") or "").strip().lower()
        lang = (r.get("language") or "").strip().lower()
        cond = (r.get("condition") or "").strip().lower().replace(" ", "_")
        totals["rows"] += 1
        totals["copies"] += qty
        if truthy(r.get("proxy")):
            problems["proxies"].append(f"{name} x{qty} ({binder})")
            continue  # no proxies (D6): never counted as owned
        card = index.get(la.normalize(name))
        if card is None:
            problems["unknown_names"].append(f"{name} x{qty} ({binder})")
            continue
        if lang not in LANGUAGES_OK:
            problems["languages_other_than_en_es"].append(f"{name} [{lang or '?'}] x{qty} ({binder})")
        if cond not in CONDITIONS_OK:
            problems["worse_than_lightly_played"].append(f"{name} [{cond}] x{qty} ({binder})")
        key = card.get("oracle_id") or card["name"]
        entry = cards.setdefault(key, {
            "oracle_id": card.get("oracle_id"), "name": card["name"], "copies": 0,
            "by_language": Counter(), "printings": [], "places": Counter(),
            "reserved_copies": 0, "in_project_deck": Counter(),
        })
        entry["copies"] += qty
        entry["by_language"][lang or "?"] += qty
        entry["places"][f"{btype}:{binder}"] += qty
        entry["printings"].append({
            "set": (r.get("set code") or "").strip().lower(),
            "number": (r.get("collector number") or "").strip(),
            "language": lang, "foil": (r.get("foil") or "").strip().lower(),
            "condition": cond, "quantity": qty, "scryfall_id": (r.get("scryfall id") or "").strip(),
        })
        if binder.lower() in reserved:
            entry["reserved_copies"] += qty
        if btype == "deck" and binder.lower() in PROJECT_DECKS:
            entry["in_project_deck"][PROJECT_DECKS[binder.lower()]] += qty
    out_cards = []
    for entry in sorted(cards.values(), key=lambda e: e["name"].casefold()):
        entry["by_language"] = dict(entry["by_language"])
        entry["places"] = dict(entry["places"])
        entry["in_project_deck"] = dict(entry["in_project_deck"])
        out_cards.append(entry)
    return {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "reserved_binders": sorted(reserved),
        "rows": totals["rows"], "copies_in_csv": totals["copies"],
        "unique_cards": len(out_cards), "owned_copies": sum(c["copies"] for c in out_cards),
        "problems": {k: v for k, v in problems.items()},
        "cards": out_cards,
    }


def summary(inv):
    """A short human-readable summary."""
    langs = Counter()
    for c in inv["cards"]:
        langs.update(c["by_language"])
    lines = [
        f"rows {inv['rows']}, copies in the CSV {inv['copies_in_csv']}",
        f"owned copies counted {inv['owned_copies']} of {inv['unique_cards']} unique cards "
        f"(by language: {dict(langs)})",
        f"reserved binders: {inv['reserved_binders'] or 'none (decision O3: no other decks)'}",
    ]
    for kind, items in inv["problems"].items():
        lines.append(f"PROBLEM {kind}: {len(items)} e.g. {items[:3]}")
    if not inv["problems"]:
        lines.append("no problems")
    return "\n".join(lines)


def main():
    """Read the collection CSV and write the inventory file."""
    if not CSV_PATH.exists():
        print(f"Missing {CSV_PATH}. Export the collection from ManaBox into data/raw/ first.")
        sys.exit(2)
    bulk = la.latest_bulk()
    if bulk is None:
        print("No oracle bulk file in data/cache/. Run scripts/collect_research_data.py first.")
        sys.exit(2)
    index = la.build_index(list(la.iter_cards(bulk)))
    inv = build_inventory(read_rows(CSV_PATH), index, RESERVED_BINDERS)
    inv["bulk_file"] = bulk.name
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(inv, indent=1, ensure_ascii=False), encoding="utf-8")
    text = summary(inv)
    OUT_PATH.with_suffix(".txt").write_text(text + "\n", encoding="utf-8")
    print(text)
    print(f"wrote {OUT_PATH.relative_to(ROOT)} (and .txt)")


if __name__ == "__main__":
    main()
