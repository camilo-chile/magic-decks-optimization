#!/usr/bin/env python3
"""Function profile of a deck from Scryfall's community oracle tags (Tagger), for the Phase 2 consistency gate.

Run it with the "Run Python File" button (no arguments). It calls the public Scryfall search API (`otag:<slug>`), with a
relevant User-Agent, an Accept header and a pause between requests (Scryfall FAQ: under 10 requests per second), once per tag
in FUNCTION_TAGS, and caches the oracle IDs of each tag in data/cache/oracle-tags.json (untracked, regenerable). Then it
counts, for each deck in decks/scanned/ (the physical decks), how many cards carry each tag and writes
decks/reports/function-profile.md. A tag whose slug the API does not know is cached as missing and shown as "n/a".

Why (prior art, docs/research/phase2-consistency-survey-20261031.md): no tool that a script may use measures the function
mix of a list: EDHREC and Archidekt bar automated use, Moxfield has no API, and a regex over Oracle text misses cards. The
Tagger tags are community-made and imperfect (a tag can include a card that only does the function in a corner case), so
the profile is a cross-check next to the builder's own tags, never the gate by itself.
"""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402

ROOT = la.ROOT
CACHE_PATH = ROOT / "data" / "cache" / "oracle-tags.json"
SCANNED_DIR = ROOT / "decks" / "scanned"
REPORT_PATH = ROOT / "decks" / "reports" / "function-profile.md"
API = "https://api.scryfall.com/cards/search"
HEADERS = {"User-Agent": "mazos-magic-personal/1.0 (camiloy.94@gmail.com)", "Accept": "application/json"}
PAUSE = 0.6  # seconds between requests: Scryfall asks for under 10 per second but answered 429 to 4 per second on the search
#              endpoint (2026-10-31); a 429 stops the run, never a retry loop
# Slugs probed on 2026-10-31 (each returned cards); some are parents of others, so counts overlap on purpose.
FUNCTION_TAGS = ("ramp", "mana-rock", "mana-dork", "draw", "card-advantage", "removal", "spot-removal", "creature-removal",
                 "board-wipe", "tutor", "reanimate", "recursion", "blink", "bounce", "protection", "protects-creature",
                 "evasion", "gives-evasion", "sacrifice-outlet", "mill-self", "discard-outlet", "counterspell",
                 "extra-combat", "anthem", "gives-haste", "win-condition")


class RateLimited(Exception):
    """Scryfall answered HTTP 429: stop, keep what is cached, and run again a few minutes later."""


def get_json(url):
    """One GET of a Scryfall URL as JSON; None on a 404 (the tag slug does not exist); RateLimited on a 429."""
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=60) as response:
            return json.load(response)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        if err.code == 429:
            raise RateLimited(url) from err
        raise


def oracle_id(card):
    """The oracle ID of a card object (on the faces for reversible cards)."""
    return card.get("oracle_id") or next((f["oracle_id"] for f in card.get("card_faces") or [] if f.get("oracle_id")), None)


def fetch_tag(slug, get=get_json, sleep=time.sleep):
    """The sorted oracle IDs that carry `otag:<slug>`, or None when the slug does not exist."""
    url = f"{API}?{urllib.parse.urlencode({'q': 'otag:' + slug, 'unique': 'cards'})}"
    ids = set()
    while url:
        page = get(url)
        if page is None:
            return None
        ids.update(i for i in (oracle_id(c) for c in page.get("data", [])) if i)
        url = page.get("next_page") if page.get("has_more") else None
        sleep(PAUSE)
    return sorted(ids)


def build_cache(slugs=FUNCTION_TAGS, get=get_json, sleep=time.sleep, existing=None, save=None):
    """{"fetched": date, "tags": {slug: [oracle ids] or None}}.

    Tags already in `existing` (fetched the same day) are kept; `save(cache)` is called after every tag, so a run that is
    stopped by a 429 loses nothing and the next run continues where it stopped."""
    today = date.today().isoformat()
    cache = {"fetched": today, "tags": {}}
    if existing and existing.get("fetched") == today:
        cache["tags"].update(existing.get("tags") or {})
    for slug in slugs:
        if slug in cache["tags"]:
            continue
        cache["tags"][slug] = fetch_tag(slug, get, sleep)
        if save:
            save(cache)
    return cache


def profile(oracle_ids_with_copies, cache, slugs=FUNCTION_TAGS):
    """{slug: number of copies carrying the tag} for [(oracle id, copies)]; None for a tag missing from the cache."""
    out = {}
    for slug in slugs:
        ids = (cache.get("tags") or {}).get(slug)
        carriers = None if ids is None else set(ids)
        out[slug] = None if carriers is None else sum(n for oid, n in oracle_ids_with_copies if oid in carriers)
    return out


def deck_oracle_ids(path, index):
    """([(oracle id, copies)], [unknown names]) of a decklist, the commander included."""
    commanders, main, _ = la.parse_decklist(Path(path).read_text(encoding="utf-8"))
    found, unknown = [], []
    for entry in commanders + main:
        card = index.get(la.normalize(entry["name"])) or index.get(la.normalize(entry["name"].split(" // ")[0]))
        if card is None:
            unknown.append(entry["name"])
        else:
            found.append((card["oracle_id"], entry["qty"]))
    return found, unknown


def profile_markdown(profiles, cache):
    decks = list(profiles)
    lines = [f"# Function profile from Scryfall oracle tags (generated by scripts/function_tags.py, tags read {cache['fetched']})",
             "", "Copies in the 100 cards that carry each tag. Tags are community-made and overlap (a parent tag includes its "
             "children); use them as a cross-check next to the builder's own tags.", "",
             "| Tag | " + " | ".join(decks) + " |", "|---|" + "---|" * len(decks)]
    for slug in FUNCTION_TAGS:
        cells = ["n/a" if profiles[d][slug] is None else str(profiles[d][slug]) for d in decks]
        lines.append(f"| {slug} | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main():
    print(f"Fetching {len(FUNCTION_TAGS)} oracle tags from Scryfall (a minute or two)...")
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = json.loads(CACHE_PATH.read_text(encoding="utf-8")) if CACHE_PATH.exists() else None

    def save(data):
        CACHE_PATH.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    try:
        cache = build_cache(existing=existing, save=save)
    except RateLimited as err:
        print(f"Scryfall answered 429 ({err}). Wait a few minutes and run again: finished tags are kept.")
        sys.exit(3)
    print("tag counts:", {k: (None if v is None else len(v)) for k, v in cache["tags"].items()})
    bulk = la.latest_bulk()
    if bulk is None:
        print("No oracle bulk file in data/cache/: no deck profile written.")
        return
    index = la.build_index(list(la.iter_cards(bulk)))
    profiles = {}
    for path in sorted(SCANNED_DIR.glob("*.txt")):
        found, unknown = deck_oracle_ids(path, index)
        profiles[path.stem] = profile(found, cache)
        if unknown:
            print(f"{path.stem}: unknown names {unknown}")
    if profiles:
        REPORT_PATH.write_text(profile_markdown(profiles, cache), encoding="utf-8")
        print(profile_markdown(profiles, cache))


if __name__ == "__main__":
    main()
