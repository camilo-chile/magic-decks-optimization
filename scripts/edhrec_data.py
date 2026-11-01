#!/usr/bin/env python3
"""EDHREC data per commander, as a prior for the Phase 2 deck builders (owner decision 2026-10-31: EDHREC may be used).

Run it with the "Run Python File" button (no arguments). It reads the commanders of decks/phase2.json (and, when
data/model/phase2/legends.json exists, the owned commander candidates with a Spanish copy), downloads each commander's
EDHREC page as JSON (https://json.edhrec.com/pages/commanders/<slug>.json) with a pause between requests, and writes
  data/cache/edhrec/<slug>.json        the raw page (untracked, regenerable)
  data/cache/edhrec/<slug>.cards.json  one row per card: list (EDHREC section), synergy, num_decks, potential_decks,
                                       inclusion (num_decks / potential_decks)
scripts/build_pools.py adds these numbers to the pool cards. They say what the EDHREC community plays with that commander
and how much more than in other decks of its colors (synergy); popularity is not quality, so they are a prior for the
builder, never a reason by themselves.
"""
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402

ROOT = la.ROOT
CONFIG_PATH = ROOT / "decks" / "phase2.json"
LEGENDS_PATH = ROOT / "data" / "model" / "phase2" / "legends.json"
CACHE_DIR = ROOT / "data" / "cache" / "edhrec"
URL = "https://json.edhrec.com/pages/commanders/{slug}.json"
HEADERS = {"User-Agent": "mazos-magic-personal/1.0 (camiloy.94@gmail.com)", "Accept": "application/json"}
PAUSE = 1.0  # seconds between requests


def edhrec_slug(name):
    """EDHREC's page slug of a card name: the front face, accents removed, lower case, words joined by hyphens."""
    front = name.split(" // ")[0]
    plain = unicodedata.normalize("NFKD", front).encode("ascii", "ignore").decode("ascii").lower()
    plain = plain.replace("'", "").replace("’", "")
    return re.sub(r"[^a-z0-9]+", "-", plain).strip("-")


def get_json(url):
    """The JSON of a URL, or None on a 404; other HTTP errors (a 429 included) are raised so the run stops."""
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=60) as response:
            return json.load(response)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def flatten(page):
    """One row per card of a commander page: {"name", "list", "synergy", "num_decks", "potential_decks", "inclusion"}.

    A card that appears in several sections keeps the first one (the sections run from "New Cards" and "Top Cards" down)."""
    rows, seen = [], set()
    lists = (((page or {}).get("container") or {}).get("json_dict") or {}).get("cardlists") or []
    for section in lists:
        for view in section.get("cardviews") or []:
            name = view.get("name")
            if not name or name in seen:
                continue
            seen.add(name)
            decks, potential = view.get("num_decks"), view.get("potential_decks")
            rows.append({"name": name, "list": section.get("header"), "synergy": view.get("synergy"),
                         "num_decks": decks, "potential_decks": potential,
                         "inclusion": round(decks / potential, 4) if decks and potential else None})
    return rows


def commander_names(config, legends=None):
    """The commanders to read: the decks' commanders, then the owned candidates with a Spanish copy."""
    import build_pools  # noqa: E402  (imported here so the tests of this module stay light)
    names = [n for n in (build_pools.commander_of(d["slug"], config) for d in config.get("decks", [])) if n]
    for row in legends or []:
        if row.get("spanish_copies") and row["name"] not in names:
            names.append(row["name"])
    return names


def fetch_all(names, cache_dir=CACHE_DIR, get=get_json, sleep=time.sleep):
    """Download and flatten every commander page; returns {name: number of cards, or "not on EDHREC"}."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    done = {}
    for name in names:
        slug = edhrec_slug(name)
        page = get(URL.format(slug=slug))
        sleep(PAUSE)
        if page is None:
            done[name] = "not on EDHREC"
            continue
        (cache_dir / f"{slug}.json").write_text(json.dumps(page, ensure_ascii=False), encoding="utf-8")
        rows = flatten(page)
        (cache_dir / f"{slug}.cards.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
        done[name] = len(rows)
    return done


def load_cards(name, cache_dir=CACHE_DIR):
    """{normalized card name: row} for a commander, or {} when its page was not downloaded."""
    path = cache_dir / f"{edhrec_slug(name)}.cards.json"
    if not path.exists():
        return {}
    return {la.normalize(r["name"]): r for r in json.loads(path.read_text(encoding="utf-8"))}


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    legends = json.loads(LEGENDS_PATH.read_text(encoding="utf-8")) if LEGENDS_PATH.exists() else []
    names = commander_names(config, legends)
    print(f"Reading {len(names)} commander pages from EDHREC, one per {PAUSE:.0f} s...")
    for name, result in fetch_all(names).items():
        print(f"  {name}: {result}")


if __name__ == "__main__":
    main()
