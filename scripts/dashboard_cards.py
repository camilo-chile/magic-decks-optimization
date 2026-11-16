"""Card facts and images of the four current decks (iteration 3) for the dashboard's deck pages.

Reads `decks/phase2.json` (the decks), `decks/phase2/<slug>.txt` (the lists), `data/model/phase2/assignment.json` (the
physical copy each deck holds: set, number, language) and `decks/phase2/<slug>.plan.json` (the role tags). For every card
it asks Scryfall for that exact printing in that language (`/cards/<set>/<number>/<lang>`), so a Spanish copy shows its
real printed Spanish name, type line and image; when Scryfall has no record in that language it falls back to the English
one and says so. Writes:

  data/model/dashboard/cards-<deck>.json   rows {order, name, name_en, qty, role, lang, set, number, mana_cost,
                                            type_line, commander}: what the deck page lists (the guide text is added by
                                            scripts/dashboard_playbook.py)
  data/cache/dashboard-images/img-<deck>.json, imgbig-<deck>-<n>.json
                                           rows {name, url[, big]} with data: URLs (small 146x204 and large 488x680 JPEG,
                                           the only image form the dashboard allows); lands get no image

Responses and images are cached in `data/cache/dashboard-cards/` so a rerun is fast. Scryfall asks for at most about 10
requests per second; this script waits 0.12 s between calls. Run it with the VS Code "Run Python File" button; no
arguments. It prints its progress with an ETA and logs it to `data/cache/dashboard-cards/progress.log`.
"""
import base64
import hashlib
import json
import math
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "decks" / "phase2.json"
ASSIGNMENT = ROOT / "data" / "model" / "phase2" / "assignment.json"
OUT = ROOT / "data" / "model" / "dashboard"
CACHE = ROOT / "data" / "cache" / "dashboard-cards"
IMAGES = ROOT / "data" / "cache" / "dashboard-images"
SHORT = {"fire-lord-azula": "azula", "ezio-auditore-da-firenze": "ezio", "toph-the-first-metalbender": "toph", "spanish-deck": "kilo"}
BASIC = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}
ROLE = {"payoff": "win", "backup": "win", "engine": "engine", "orphan": "engine", "tutor": "tutor", "draw": "draw",
        "ramp": "mana", "removal": "removal", "wipe": "removal", "protection": "defense", "land": "land"}
BIG_CHUNKS = 2
HEADERS = {"User-Agent": "mazos-magic/1.0", "Accept": "application/json"}
LOG = CACHE / "progress.log"


def log(text):
    line = f"{datetime.now(timezone.utc).strftime('%H:%M:%S')} {text}"
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def fetch(url, binary=False):
    """GET with a disk cache; None on 404."""
    key = hashlib.sha1(url.encode()).hexdigest()[:20]
    path = CACHE / (key + (".bin" if binary else ".json"))
    if path.exists():
        data = path.read_bytes()
        return data if binary else json.loads(data)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=60) as response:
                data = response.read()
            time.sleep(0.12)
            path.write_bytes(data)
            return data if binary else json.loads(data)
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return None
            if attempt == 4:
                raise
        except Exception:  # noqa: BLE001 - retry any network error, then fail loudly
            if attempt == 4:
                raise
        time.sleep(2 + attempt * 3)


def read_list(path):
    commanders, entries, section = [], [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("//"):
            section = line[2:].strip().lower()
            continue
        match = re.match(r"^(\d+)\s+(.+?)\s*$", line)
        if match:
            (commanders if section == "commander" else entries).append((int(match.group(1)), match.group(2)))
    return commanders, entries


def face(card, field):
    faces = card.get("card_faces") or []
    value = card.get(field)
    if value:
        return value
    return " // ".join(f.get(field, "") for f in faces if f.get(field))


def card_facts(name, pick):
    """(Scryfall card in the copy's language or English, language used)."""
    if pick:
        lang = pick["language"]
        base = f"https://api.scryfall.com/cards/{pick['set'].lower()}/{pick['number']}"
        card = fetch(base + ("/" + lang if lang != "en" else ""))
        if card:
            return card, lang
        card = fetch(base)
        if card:
            return card, "en"
    return fetch("https://api.scryfall.com/cards/named?exact=" + urllib.request.quote(name.split(" // ")[0])), "en"


def spanish_name(name):
    """(printed Spanish name, printed type line) from any Spanish printing of the card, or None."""
    query = urllib.request.quote(f'!"{name.split(" // ")[0]}" lang:es')
    found = fetch(f"https://api.scryfall.com/cards/search?q={query}&unique=prints")
    for card in (found or {}).get("data", []):
        if card.get("printed_name"):
            return card["printed_name"], card.get("printed_type_line")
    return None


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    IMAGES.mkdir(parents=True, exist_ok=True)
    LOG.write_text("", encoding="utf-8")
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    assignment = json.loads(ASSIGNMENT.read_text(encoding="utf-8"))["decks"]
    decks = [d for d in config["decks"] if d["slug"] in SHORT]
    jobs = []
    for deck in decks:
        commanders, entries = read_list(ROOT / "decks" / "phase2" / f"{deck['slug']}.txt")
        jobs.append((deck, commanders, entries))
    total = sum(len(c) + len(e) for _, c, e in jobs)
    started, done = time.time(), 0
    for deck, commanders, entries in jobs:
        slug, short = deck["slug"], SHORT[deck["slug"]]
        picks = {c["name"]: c["picks"] for c in assignment[slug]["cards"]}
        tags = json.loads((ROOT / "decks" / "phase2" / f"{slug}.plan.json").read_text(encoding="utf-8"))["tags"]
        rows, smalls, bigs = [], [], []
        for order, (qty, name, is_commander) in enumerate([(q, n, True) for q, n in commanders] + [(q, n, False) for q, n in entries], 1):
            done += 1
            pick = (picks.get(name) or [None])[0]
            card, lang = card_facts(name, pick)
            if card is None:
                log(f"{short}: {name} not found on Scryfall")
                continue
            shown = card.get("printed_name") if lang != "en" and card.get("printed_name") else name
            type_line = card.get("printed_type_line") if lang != "en" and card.get("printed_type_line") else face(card, "type_line")
            if pick and lang != pick["language"]:
                other = spanish_name(name) if pick["language"] == "es" else None
                if other:
                    shown, type_line, lang = other[0], other[1] or type_line, "es"
                    log(f"{short}: {name}: no Spanish record of this printing; Spanish name from another printing ({shown})")
                else:
                    log(f"{short}: {name} has no {pick['language']} record on Scryfall; English shown")
            tag = tags.get(name)
            tag = tag[0] if isinstance(tag, list) else tag
            land = "Land" in face(card, "type_line")
            role = "commander" if is_commander else ("land" if land or name in BASIC else ROLE.get(tag, "engine"))
            rows.append({"order": order, "name": shown, "name_en": name, "qty": qty, "role": role, "lang": lang,
                         "set": (pick or {}).get("set", card.get("set", "")).upper(), "number": (pick or {}).get("number", card.get("collector_number", "")),
                         "mana_cost": face(card, "mana_cost"), "type_line": type_line, "commander": is_commander})
            uris = card.get("image_uris") or ((card.get("card_faces") or [{}])[0].get("image_uris") or {})
            if not land and uris.get("small"):
                small = base64.b64encode(fetch(uris["small"], binary=True)).decode()
                big = base64.b64encode(fetch(uris["normal"], binary=True)).decode()
                smalls.append({"name": shown, "url": "data:image/jpeg;base64," + small})
                bigs.append({"name": shown, "url": "data:image/jpeg;base64," + big})
            if done % 20 == 0 or done == total:
                rate = (time.time() - started) / done
                log(f"{done}/{total} cards ({100 * done // total} %), ETA {int(rate * (total - done))} s")
        per_chunk = max(1, math.ceil(len(bigs) / BIG_CHUNKS))
        for i, img in enumerate(smalls):
            img["big"] = i // per_chunk
        for k in range(BIG_CHUNKS):
            path = IMAGES / f"imgbig-{short}-{k}.json"
            path.write_text(json.dumps({"rows": bigs[k * per_chunk:(k + 1) * per_chunk]}, ensure_ascii=False), encoding="utf-8")
            if path.stat().st_size > 7.5e6:
                sys.exit(f"{path.name} is {path.stat().st_size / 1e6:.2f} MB: raise BIG_CHUNKS (a dataset may not exceed 8 MB)")
        (IMAGES / f"img-{short}.json").write_text(json.dumps({"rows": smalls}, ensure_ascii=False), encoding="utf-8")
        (OUT / f"cards-{short}.json").write_text(json.dumps({"rows": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        log(f"{short}: {sum(r['qty'] for r in rows)} cards, {len(smalls)} images, "
            f"{sum(1 for r in rows if r['lang'] == 'es')} rows in Spanish")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
