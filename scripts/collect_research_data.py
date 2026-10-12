#!/usr/bin/env python3
"""Collect the raw data Phase 3 (synergy research) works from.

Run it with the "Run Python File" button (no arguments). It needs internet and takes a few
minutes at most. It writes only under data/cache/ (git-ignored):

  oracle-cards-<timestamp>.json[l][.gz]  raw Scryfall bulk file (one card per oracle ID)
  pool_<slug>.jsonl                      Commander-legal cards inside each commander's
                                         color identity, trimmed to the fields research needs
  spellbook_<slug>.json                  every Commander Spellbook combo that uses the
                                         commander, raw
  collect_manifest.json                  what was fetched, when, counts and a checksum
  collect_progress.log                   progress with ETA

Sources are the Scryfall bulk-data endpoint and the Commander Spellbook REST API only.
Prices are not collected: every price in this project comes from the Chilean stores.
"""
import gzip
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "cache"
LOG_PATH = CACHE / "collect_progress.log"

SCRYFALL = "https://api.scryfall.com"
SPELLBOOK = "https://backend.commanderspellbook.com"
HEADERS = {"User-Agent": "magic-decks-optimization/0.1", "Accept": "application/json"}
DOWNLOAD_HEADERS = {"User-Agent": "magic-decks-optimization/0.1", "Accept": "*/*"}

COMMANDERS = {
    "alexios-deimos-of-kosmos": "Alexios, Deimos of Kosmos",
    "toph-the-first-metalbender": "Toph, the First Metalbender",
    "fire-lord-azula": "Fire Lord Azula",
}
EXCLUDED_LAYOUTS = {
    "token",
    "double_faced_token",
    "emblem",
    "art_series",
    "vanguard",
    "scheme",
    "planar",
    "augment",
    "host",
}
KEEP_FIELDS = [
    "id",
    "oracle_id",
    "name",
    "mana_cost",
    "cmc",
    "type_line",
    "oracle_text",
    "colors",
    "color_identity",
    "keywords",
    "produced_mana",
    "layout",
    "game_changer",
    "edhrec_rank",
    "power",
    "toughness",
    "loyalty",
]
FACE_FIELDS = ("name", "mana_cost", "type_line", "oracle_text")


def log(message):
    """Print a timestamped line and append it to the progress log."""
    line = f"{datetime.now().strftime('%H:%M:%S')}  {message}"
    print(line, flush=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def eta_text(done, total, started):
    """Remaining time as text, from the average rate so far."""
    if done <= 0 or total <= 0:
        return "ETA ?"
    remaining = (time.time() - started) / done * max(total - done, 0)
    return f"ETA {int(remaining // 60)}m{int(remaining % 60):02d}s"


def trim(card):
    """Keep only the fields the research needs (no prices, no images)."""
    out = {key: card.get(key) for key in KEEP_FIELDS}
    faces = card.get("card_faces")
    if faces:
        out["card_faces"] = [{k: face.get(k) for k in FACE_FIELDS} for face in faces]
    return out


def is_pool_card(card):
    """Commander-legal, a real game card (not a token, emblem or oversized card)."""
    if (card.get("legalities") or {}).get("commander") != "legal":
        return False
    if card.get("layout") in EXCLUDED_LAYOUTS:
        return False
    return not card.get("oversized")


def build_pool(legal_cards, identity):
    """Cards whose color identity fits inside the commander's."""
    allowed = set(identity)
    return [c for c in legal_cards if set(c.get("color_identity") or []) <= allowed]


def open_text(path):
    """Open a file as text, gunzipping when the bytes say it is gzip (not the extension)."""
    with open(path, "rb") as fh:
        magic = fh.read(2)
    if magic == b"\x1f\x8b":
        return gzip.open(path, "rt", encoding="utf-8")
    return open(path, encoding="utf-8")


def iter_cards(path):
    """Yield cards from a Scryfall bulk file, JSON Lines or one JSON array."""
    with open_text(path) as fh:
        first = fh.readline()
        if first.lstrip().startswith("["):
            yield from json.loads(first + fh.read())
            return
        if first.strip():
            yield json.loads(first)
        for line in fh:
            if line.strip():
                yield json.loads(line)


def sha256_of(path):
    """SHA-256 of a file, read in blocks."""
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def download_bulk(requests, bulk_type="oracle_cards"):
    """Download a Scryfall bulk file (default oracle_cards) unless this exact version is cached."""
    resp = requests.get(f"{SCRYFALL}/bulk-data", headers=HEADERS, timeout=30)
    resp.raise_for_status()
    entry = next(e for e in resp.json()["data"] if e.get("type") == bulk_type)
    uri = entry.get("jsonl_download_uri") or entry.get("download_uri")
    dest = CACHE / Path(urlparse(uri).path).name
    meta = {"updated_at": entry.get("updated_at"), "uri": uri, "file": dest.name}
    if dest.exists() and dest.stat().st_size > 1_000_000:
        log(f"bulk file already cached: {dest.name}")
        return dest, meta
    log(f"downloading {uri}")
    tmp = dest.with_suffix(dest.suffix + ".part")
    started = time.time()
    with requests.get(uri, headers=DOWNLOAD_HEADERS, stream=True, timeout=60) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length") or 0)
        done, last = 0, time.time()
        with open(tmp, "wb") as fh:
            for chunk in r.iter_content(1 << 20):
                fh.write(chunk)
                done += len(chunk)
                if time.time() - last > 3:
                    log(f"download {done / 1e6:.1f}/{total / 1e6:.1f} MB  {eta_text(done, total, started)}")
                    last = time.time()
    tmp.replace(dest)
    log(f"downloaded {dest.stat().st_size / 1e6:.1f} MB")
    return dest, meta


def fetch_spellbook(requests, card_name):
    """All Commander Spellbook variants that use the card, paged. Returns (variants, count, query)."""
    for query in (f'card="{card_name}"', f'card:"{card_name}"'):
        url, params = f"{SPELLBOOK}/variants/", {"q": query, "limit": 100}
        variants, count, started, page = [], None, time.time(), 0
        while url:
            for _ in range(4):
                resp = requests.get(url, params=params, headers=HEADERS, timeout=60)
                if resp.status_code == 429:
                    log("Spellbook rate limit (429); waiting 30 s")
                    time.sleep(30)
                    continue
                break
            if resp.status_code == 400 and page == 0:
                log(f"query {query!r} rejected (400); trying the next syntax")
                break
            resp.raise_for_status()
            body = resp.json()
            count = body.get("count", count)
            variants += body.get("results", [])
            page += 1
            if count:
                total_pages = -(-count // 100)
                log(f"  {card_name}: page {page}/{total_pages}, {len(variants)} variants  "
                    f"{eta_text(page, total_pages, started)}")
            else:  # the API only reports a count on request; progress has no total then
                log(f"  {card_name}: page {page}, {len(variants)} variants")
            url, params = body.get("next"), None
            time.sleep(1.0)
            if page > 200:
                raise RuntimeError("more than 200 pages; stopping")
        else:
            return variants, count, query
    return [], None, None


def main():
    """Download, filter and save the research inputs; write the manifest."""
    try:
        import requests
    except ImportError:
        print("The 'requests' package is missing in this environment. Run once:")
        print("  pip install -r requirements.txt")
        sys.exit(2)

    CACHE.mkdir(parents=True, exist_ok=True)
    started = time.time()
    log("=== collect_research_data start ===")
    manifest = {"run_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}

    bulk_path, bulk_meta = download_bulk(requests)
    bulk_meta["sha256"] = sha256_of(bulk_path)

    log("reading the bulk file")
    legal, by_name, total_cards = [], {}, 0
    for card in iter_cards(bulk_path):
        total_cards += 1
        if card.get("name") in COMMANDERS.values():
            by_name[card["name"]] = card
        if is_pool_card(card):
            legal.append(trim(card))
    bulk_meta["cards_total"] = total_cards
    bulk_meta["cards_commander_legal"] = len(legal)
    manifest["scryfall"] = bulk_meta
    log(f"{total_cards} oracle cards, {len(legal)} Commander-legal game cards")

    manifest["commanders"] = {}
    for slug, name in COMMANDERS.items():
        entry = {"name": name}
        card = by_name.get(name)
        if card is None:
            entry["error"] = "commander not found in the bulk file"
            manifest["commanders"][slug] = entry
            log(f"!! {name}: not found in the bulk file")
            continue
        identity = card.get("color_identity") or []
        entry["color_identity"] = identity
        pool = build_pool(legal, identity)
        pool_path = CACHE / f"pool_{slug}.jsonl"
        with open(pool_path, "w", encoding="utf-8") as fh:
            for c in pool:
                fh.write(json.dumps(c, ensure_ascii=False) + "\n")
        entry["pool_cards"] = len(pool)
        entry["pool_game_changers"] = sorted(c["name"] for c in pool if c.get("game_changer"))
        entry["pool_file"] = pool_path.name
        log(f"{name}: identity {''.join(identity) or 'colorless'}, pool {len(pool)} cards, "
            f"{len(entry['pool_game_changers'])} Game Changers")

        try:
            variants, count, query = fetch_spellbook(requests, name)
            if query is None:
                raise RuntimeError("both Spellbook query syntaxes were rejected (HTTP 400)")
            sb_path = CACHE / f"spellbook_{slug}.json"
            sb_path.write_text(
                json.dumps({"commander": name, "query": query, "count": count, "variants": variants},
                           ensure_ascii=False),
                encoding="utf-8",
            )
            entry.update(spellbook_variants=len(variants), spellbook_count=count,
                         spellbook_query=query, spellbook_file=sb_path.name)
            log(f"{name}: {len(variants)} Spellbook variants (API count {count})")
        except Exception as exc:  # keep going; the manifest records the failure
            entry["spellbook_error"] = f"{type(exc).__name__}: {exc}"
            log(f"!! {name}: Spellbook failed: {exc}")
        manifest["commanders"][slug] = entry

    manifest["elapsed_seconds"] = round(time.time() - started, 1)
    (CACHE / "collect_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    log(f"=== done in {manifest['elapsed_seconds']} s; manifest: data/cache/collect_manifest.json ===")


if __name__ == "__main__":
    main()
