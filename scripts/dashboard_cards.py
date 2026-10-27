"""Fetch the card facts and small images of the three final lists for the dashboard's deck pages.

Reads the final measured lists (the 200,000 CLP plan: Toph R3 step 21, Azula R4 step 27, Ezio R5 step 40), asks the
Scryfall API for each card (name, mana cost, type line, oracle text, small image) and writes, under data/cache/
(untracked, regenerable):

  cards-facts.json                 per deck: the facts of every nonbasic card, for writing the function notes
  dashboard-images/img-<deck>.json rows {name, url, big} where url is a data: URL (JPEG, 146x204), the only image form
                                   the dashboard allows, and big is the number of the large-image file that holds the card
  dashboard-images/imgbig-<deck>-<n>.json
                                   rows {name, url} with the large image (JPEG, 488x680) that opens when a thumbnail is
                                   clicked; the cards of one deck are split in BIG_CHUNKS files because a dataset may not
                                   exceed 8 MB (about 80 KB per card)

The images of lands are skipped (the deck pages list lands as text). Scryfall asks for about 10 requests per second at
most; this script waits 0.15 s between calls. Run it from the VS Code "Run Python File" button; no arguments.
"""
import base64
import json
import math
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "cache"
LISTS = {
    "toph": "decks/measured/toph-the-first-metalbender/round3-step21.txt",
    "azula": "decks/measured/fire-lord-azula/round4-step27.txt",
    "ezio": "decks/measured/ezio-auditore-da-firenze/round5-step40.txt",
}
BASIC = {"Plains", "Island", "Swamp", "Mountain", "Forest"}
BIG_CHUNKS = 2
HEADERS = {"User-Agent": "mazos-magic/1.0", "Accept": "application/json"}


def read_list(path):
    commander, main, section = [], [], None
    for line in (ROOT / path).read_text(encoding="utf-8").splitlines():
        if line.startswith("//"):
            section = line.strip()
            continue
        m = re.match(r"^(\d+)\s+(.+?)\s*$", line.strip())
        if m and m.group(2) not in BASIC:
            (commander if section == "// Commander" else main).append(m.group(2))
    return commander, main


def get(url, binary=False):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            return data if binary else json.loads(data)
        except Exception as e:  # noqa: BLE001 - retry any network error, then fail loudly
            if attempt == 4:
                raise
            time.sleep(2 + attempt * 3)
            print("retry", url[:80], e, file=sys.stderr)


def collect(names):
    """Scryfall /cards/collection by front-face name, 75 per request."""
    found = {}
    for i in range(0, len(names), 75):
        chunk = names[i:i + 75]
        body = json.dumps({"identifiers": [{"name": n.split(" // ")[0]} for n in chunk]}).encode()
        req = urllib.request.Request("https://api.scryfall.com/cards/collection", data=body,
                                     headers={**HEADERS, "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.load(r)
        for c in res["data"]:
            found[c["name"].split(" // ")[0].lower()] = c
        if res.get("not_found"):
            print("NOT FOUND:", res["not_found"], file=sys.stderr)
        time.sleep(0.15)
    return found


def facts_of(card):
    faces = card.get("card_faces") or [card]
    return {
        "name": card["name"],
        "mana_cost": " // ".join(f.get("mana_cost", "") for f in faces) if card.get("card_faces") else card.get("mana_cost", ""),
        "type_line": card["type_line"],
        "oracle_text": "\n//\n".join(f.get("oracle_text", "") for f in faces),
        "small": (card.get("image_uris") or faces[0].get("image_uris") or {}).get("small"),
    }


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / "dashboard-images").mkdir(exist_ok=True)
    allnames = sorted({n for p in LISTS.values() for part in read_list(p) for n in part})
    found = collect(allnames)
    facts, image_cache, big_cache = {}, {}, {}
    for deck, path in LISTS.items():
        commander, main_cards = read_list(path)
        rows, images, bigs = [], [], []
        for name in commander + main_cards:
            card = found.get(name.split(" // ")[0].lower())
            if not card:
                continue
            f = facts_of(card)
            f["commander"] = name in commander
            f["land"] = "Land" in f["type_line"]
            rows.append(f)
            if f["land"] or not f["small"]:
                continue
            if f["small"] not in image_cache:
                image_cache[f["small"]] = base64.b64encode(get(f["small"], binary=True)).decode()
                time.sleep(0.15)
            big_url = f["small"].replace("/small/", "/normal/")
            if big_url not in big_cache:
                big_cache[big_url] = base64.b64encode(get(big_url, binary=True)).decode()
                time.sleep(0.15)
            images.append({"name": f["name"], "url": "data:image/jpeg;base64," + image_cache[f["small"]]})
            bigs.append({"name": f["name"], "url": "data:image/jpeg;base64," + big_cache[big_url]})
        per_chunk = math.ceil(len(bigs) / BIG_CHUNKS)
        for i, img in enumerate(images):
            img["big"] = i // per_chunk
        for k in range(BIG_CHUNKS):
            big_out = CACHE / "dashboard-images" / f"imgbig-{deck}-{k}.json"
            big_out.write_text(json.dumps({"rows": bigs[k * per_chunk:(k + 1) * per_chunk]}, ensure_ascii=False), encoding="utf-8")
            if big_out.stat().st_size > 7.5e6:
                sys.exit(f"{big_out.name} is {big_out.stat().st_size / 1e6:.2f} MB: raise BIG_CHUNKS (a dataset may not exceed 8 MB)")
            print("  ", big_out.name, round(big_out.stat().st_size / 1e6, 2), "MB")
        facts[deck] = rows
        out = CACHE / "dashboard-images" / f"img-{deck}.json"
        out.write_text(json.dumps({"rows": images}, ensure_ascii=False), encoding="utf-8")
        print(deck, len(rows), "cards,", len(images), "images,", round(out.stat().st_size / 1e6, 2), "MB")
    (CACHE / "cards-facts.json").write_text(json.dumps(facts, ensure_ascii=False, indent=1), encoding="utf-8")
    print("facts written:", CACHE / "cards-facts.json")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
