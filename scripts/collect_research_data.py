#!/usr/bin/env python3
"""Download the Scryfall oracle bulk file that Layer A and the allocation model read.

Run it with the "Run Python File" button (no arguments). It needs internet and downloads about
25 MB, unless that exact version is already cached. It writes only under data/cache/ (ignored by version control):

  oracle-cards-<timestamp>.json[l][.gz]  raw Scryfall bulk file (one card per oracle ID)
  collect_manifest.json                  what was fetched, when, counts and a checksum
  collect_progress.log                   progress with ETA

Also holds the small helpers shared with layer_a.py and collect_spellbook_bulk.py (log, eta_text,
open_text, iter_cards, sha256_of). The Phase 3 research pools and the per-commander Spellbook
queries were removed on 2026-10-18 with the closing of that phase.
Prices are not collected here: every price in this project comes from the Chilean stores.
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
HEADERS = {"User-Agent": "magic-decks-optimization/0.1", "Accept": "application/json"}
DOWNLOAD_HEADERS = {"User-Agent": "magic-decks-optimization/0.1", "Accept": "*/*"}

COMMANDERS = {
    "alexios-deimos-of-kosmos": "Alexios, Deimos of Kosmos",
    "toph-the-first-metalbender": "Toph, the First Metalbender",
    "fire-lord-azula": "Fire Lord Azula",
}


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


def main():
    """Download the oracle bulk file and record it in the manifest (keeping the other entries)."""
    try:
        import requests
    except ImportError:
        print("The 'requests' package is missing in this environment. Run once:")
        print("  pip install -r requirements.txt")
        sys.exit(2)

    CACHE.mkdir(parents=True, exist_ok=True)
    started = time.time()
    log("=== collect_research_data start ===")
    manifest_path = CACHE / "collect_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    manifest["run_at_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    bulk_path, bulk_meta = download_bulk(requests)
    bulk_meta["sha256"] = sha256_of(bulk_path)
    bulk_meta["cards_total"] = sum(1 for _ in iter_cards(bulk_path))
    manifest["scryfall"] = bulk_meta
    log(f"{bulk_meta['cards_total']} oracle cards in {bulk_path.name}")

    manifest["elapsed_seconds"] = round(time.time() - started, 1)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    log(f"=== done in {manifest['elapsed_seconds']} s; manifest: data/cache/collect_manifest.json ===")


if __name__ == "__main__":
    main()
