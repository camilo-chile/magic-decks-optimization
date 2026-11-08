#!/usr/bin/env python3
"""Phase 2: the exact tokens and emblems the four decks make, against the tokens the owner has.

Run it with the "Run Python File" button (no arguments). For every card of decks/phase2/moxfield/<slug>-after-purchases.txt
(the lists he will play after the purchase) it takes the Scryfall oracle data (data/cache/oracle-cards-*.jsonl.gz, `all_parts`:
components `token`, and `combo_piece` whose type line is an Emblem) and reads each token's own Scryfall card (name, type line,
power/toughness, colors, rules text). The tokens he owns are the rows of the newest data/collection/ManaBox_Collection_*.csv
whose set is a token set (code starting with "T" and the set name ending in "Tokens"); each is read from Scryfall by its ID.
A token counts as owned only when name, type line, P/T, colors and rules text all match (one face of a double-faced token is
enough). Progress with an ETA on the console and in data/model/phase2/tokens.progress.log. Writes decks/reports/tokens-<date>.md and data/model/phase2/tokens.json.
"""
import csv
import gzip
import json
import re
import sys
import time
from datetime import date
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from read_store_prices import Progress  # noqa: E402  (console + log file lines with an ETA)

ROOT = Path(__file__).resolve().parent.parent
DECKS = ["fire-lord-azula", "toph-the-first-metalbender", "ezio-auditore-da-firenze", "spanish-deck"]
LABEL = {"fire-lord-azula": "Azula", "toph-the-first-metalbender": "Toph", "ezio-auditore-da-firenze": "Ezio",
         "spanish-deck": "Kilo"}
UA = "mazos-magic-token-check/1.0 (personal, read-only)"
_cache = {}


def scryfall(card_id):
    if card_id not in _cache:
        time.sleep(0.12)
        resp = requests.get(f"https://api.scryfall.com/cards/{card_id}", headers={"User-Agent": UA, "Accept": "application/json"},
                            timeout=60)
        resp.raise_for_status()
        _cache[card_id] = resp.json()
    return _cache[card_id]


def faces(card):
    return card.get("card_faces") or [card]


def spec(face):
    """What makes two tokens the same token: name, type line, P/T, colors, rules text."""
    colors = "".join(sorted(face.get("colors") or []))
    return (face.get("name", ""), face.get("type_line", ""), face.get("power", ""), face.get("toughness", ""), colors,
            re.sub(r"\s+", " ", face.get("oracle_text", "")).strip())


def deck_names(slug):
    names = []
    text = (ROOT / "decks" / "phase2" / "moxfield" / f"{slug}-after-purchases.txt").read_text(encoding="utf-8")
    for line in text.splitlines():
        m = re.match(r"(\d+)\s+(.+?)(\s+\([A-Za-z0-9]+\).*)?$", line.strip())
        if m:
            names.append(m.group(2).strip())
    return names


def oracle_index():
    path = sorted((ROOT / "data" / "cache").glob("oracle-cards-*.jsonl.gz"))[-1]
    index = {}
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            card = json.loads(line)
            if card.get("layout") in ("token", "double_faced_token", "emblem", "art_series"):
                continue
            index.setdefault(card["name"].lower(), card)
            for face in card.get("card_faces") or []:
                index.setdefault(face["name"].lower(), card)
    return index


def owned_tokens():
    path = sorted((ROOT / "data" / "collection").glob("ManaBox_Collection_*.csv"))[-1]
    owned = {}
    with open(path, encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            if not (row["Set code"].upper().startswith("T") and row["Set name"].endswith("Tokens")):
                continue
            card = scryfall(row["Scryfall ID"])
            label = f"{row['Name']} ({row['Set code']} {row['Collector number']}, {row['Binder Name']})"
            for face in faces(card):
                owned.setdefault(spec(face), []).append((label, int(row["Quantity"])))
    return owned, path.name


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    progress = Progress(ROOT / "data" / "model" / "phase2" / "tokens.progress.log")
    started = time.time()
    progress.log("reading the Scryfall oracle cache")
    index = oracle_index()
    progress.log("reading the owned tokens (Scryfall, one card per token row)")
    owned, csv_name = owned_tokens()
    needs = {}
    for done, slug in enumerate(DECKS):
        progress.log(f"deck {done + 1}/{len(DECKS)}: {LABEL[slug]}  {Progress.eta(done, len(DECKS), started)}")
        for name in deck_names(slug):
            card = index.get(name.lower())
            if not card:
                progress.log(f"not in the oracle cache: {name}")
                continue
            for part in card.get("all_parts") or []:
                is_emblem = "Emblem" in part.get("type_line", "")
                if part.get("component") != "token" and not (part.get("component") == "combo_piece" and is_emblem):
                    continue
                token = scryfall(part["id"])
                specs = [spec(f) for f in faces(token)]
                key = specs[0] if len(specs) == 1 else next((s for s in specs if s[0] == part["name"].split(" // ")[0]), specs[0])
                entry = needs.setdefault(key, {"token": key, "made_by": {}, "scryfall": token.get("scryfall_uri", "")})
                entry["made_by"].setdefault(LABEL[slug], set()).add(name)
    rows = []
    for key, entry in needs.items():
        have = owned.get(key, [])
        rows.append({"name": key[0], "type_line": key[1], "pt": f"{key[2]}/{key[3]}" if key[2] or key[3] else "",
                     "colors": key[4] or "C", "text": key[5], "owned": sum(q for _, q in have),
                     "owned_rows": [label for label, _ in have],
                     "made_by": {deck: sorted(cards) for deck, cards in entry["made_by"].items()}, "scryfall": entry["scryfall"]})
    rows.sort(key=lambda r: (r["owned"] > 0, r["name"]))
    out_json = ROOT / "data" / "model" / "phase2" / "tokens.json"
    out_json.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    md = [f"# Tokens and emblems of the four decks after purchases ({date.today().isoformat()})", "",
          f"Lists: decks/phase2/moxfield/<slug>-after-purchases.txt. Owned tokens: token-set rows of `{csv_name}`, matched by "
          "name, type line, P/T, colors and rules text (Scryfall).", "",
          "| Token | Type | P/T | Colors | Owned | Made by |", "|---|---|---|---|---|---|"]
    for r in rows:
        made = "; ".join(f"{d}: {', '.join(c)}" for d, c in r["made_by"].items())
        md.append(f"| {r['name']} | {r['type_line']} | {r['pt']} | {r['colors']} | {r['owned'] or '**0**'} | {made} |")
    missing = [r for r in rows if not r["owned"]]
    md += ["", f"{len(rows)} distinct tokens/emblems, {len(missing)} not owned."]
    out_md = ROOT / "decks" / "reports" / f"tokens-{date.today().strftime('%Y%m%d')}.md"
    out_md.write_text("\n".join(md) + "\n", encoding="utf-8")
    progress.log(f"{len(rows)} tokens, {len(missing)} missing -> {out_md.relative_to(ROOT).as_posix()}")
    for r in missing:
        progress.log(f"  MISSING: {r['name']} {r['pt']} {r['colors']} | {r['made_by']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
