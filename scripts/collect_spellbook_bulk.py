#!/usr/bin/env python3
"""Download the Commander Spellbook bulk file and cut it down for local combo matching.

Run it with the "Run Python File" button (no arguments). It needs internet and downloads
about 30 MB once. It writes only under data/cache/ (git-ignored):

  spellbook-variants-<YYYYMMDD>.json.gz   the raw bulk file (kept for its checksum)
  spellbook_variants_slim.jsonl.gz        gzipped JSON Lines, one variant per line, with the
                                          fields Layer A uses: id, bracket tag, cards (oracle
                                          IDs), template requirements, produced features,
                                          mana needed, identity, Commander legality
  collect_manifest.json                   gets a "spellbook_bulk" entry (date, version,
                                          counts, checksum)
  collect_progress.log                    shared progress log

Source: https://json.commanderspellbook.com/variants.json.gz. The API documentation
(OpenAPI description, version 7.1.9, read 2026-10-12) asks clients not to export the whole
dataset through the API and to read this file locally instead, on their own schedule. Credit:
combo data by Commander Spellbook, https://commanderspellbook.com
"""
import gzip
import json
import re
import sys
import time
from datetime import datetime, timezone

from collect_research_data import CACHE, eta_text, log, open_text, sha256_of

URL = "https://json.commanderspellbook.com/variants.json.gz"
USER_AGENT = ("magic-decks-optimization/0.1 (personal project, "
              "github.com/camilo-chile/magic-decks-optimization)")
SLIM_NAME = "spellbook_variants_slim.jsonl.gz"
WHITESPACE_AND_COMMA = " \t\r\n,"


def slim_variant(variant):
    """The fields Layer A needs from one variant, in a small flat shape."""
    cards = []
    for use in variant.get("uses") or []:
        card = use.get("card") or {}
        cards.append({
            "oracle_id": card.get("oracleId"),
            "name": card.get("name"),
            "quantity": use.get("quantity") or 1,
            "must_be_commander": bool(use.get("mustBeCommander")),
        })
    requires = []
    for req in variant.get("requires") or []:
        template = req.get("template") or {}
        requires.append(template.get("name") or template.get("scryfallQuery") or "?")
    features = [(p.get("feature") or {}).get("name") for p in variant.get("produces") or []]
    return {
        "id": variant.get("id"),
        "bracket_tag": variant.get("bracketTag"),
        "identity": variant.get("identity"),
        "cards": cards,
        "requires": requires,
        "features": [f for f in features if f],
        "mana_needed": variant.get("manaNeeded"),
        "mana_value_needed": variant.get("manaValueNeeded"),
        "commander_legal": (variant.get("legalities") or {}).get("commander"),
        "status": variant.get("status"),
        "spoiler": bool(variant.get("spoiler")),
    }


def download(requests, dest):
    """Stream the bulk file to dest as the server stores it (raw bytes, never decoded)."""
    tmp = dest.with_suffix(dest.suffix + ".part")
    started = time.time()
    with requests.get(URL, headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
                      stream=True, timeout=60) as resp:
        resp.raise_for_status()
        total = int(resp.headers.get("Content-Length") or 0)
        log(f"server sent Content-Length {total / 1e6:.1f} MB, "
            f"Content-Encoding {resp.headers.get('Content-Encoding')!r}")
        done, last = 0, time.time()
        with open(tmp, "wb") as fh:
            # resp.raw with decode_content=False keeps the .gz file's own bytes even when
            # the server also labels the response as gzip-encoded.
            for chunk in resp.raw.stream(1 << 20, decode_content=False):
                fh.write(chunk)
                done += len(chunk)
                if time.time() - last > 3:
                    log(f"download {done / 1e6:.1f}/{total / 1e6:.1f} MB  "
                        f"{eta_text(done, total, started)}")
                    last = time.time()
    tmp.replace(dest)
    return dest.stat().st_size


def iter_array(text, pos):
    """Yield the objects of a JSON array one at a time, starting just after its '['."""
    decoder = json.JSONDecoder()
    size = len(text)
    while True:
        while pos < size and text[pos] in WHITESPACE_AND_COMMA:
            pos += 1
        if pos >= size or text[pos] == "]":
            return
        obj, pos = decoder.raw_decode(text, pos)
        yield obj


def read_bulk(path):
    """Return (meta, variants iterator) for the bulk file, gzipped or plain JSON.

    The text is read once (about 700 MB uncompressed) but the variants are parsed one at a
    time, so memory stays near the size of the text instead of several times it.
    """
    with open_text(path) as fh:
        text = fh.read()
    head = text[:2000]
    meta = {}
    for key in ("timestamp", "version"):
        match = re.search(r'"' + key + r'"\s*:\s*"([^"]*)"', head)
        meta[key] = match.group(1) if match else None
    start = text.find('"variants"')
    if start < 0:
        return meta, iter(())
    return meta, iter_array(text, text.index("[", start) + 1)


def main():
    """Download, slim, write the manifest entry."""
    try:
        import requests
    except ImportError:
        print("The 'requests' package is missing in this environment. Run once:")
        print("  pip install -r requirements.txt")
        sys.exit(2)

    started = time.time()
    CACHE.mkdir(parents=True, exist_ok=True)
    log("=== collect_spellbook_bulk start ===")
    dest = CACHE / f"spellbook-variants-{datetime.now(timezone.utc).strftime('%Y%m%d')}.json.gz"
    size = download(requests, dest)
    log(f"downloaded {size / 1e6:.1f} MB to {dest.name}")

    with open(dest, "rb") as fh:
        magic = fh.read(2)
    log("file is " + ("gzip" if magic == b"\x1f\x8b" else "plain JSON (not gzip)"))

    log("reading and slimming the variants (about a minute)")
    meta, variants = read_bulk(dest)
    slim_path = CACHE / SLIM_NAME
    count, t0 = 0, time.time()
    with gzip.open(slim_path, "wt", encoding="utf-8") as fh:
        for variant in variants:
            fh.write(json.dumps(slim_variant(variant), ensure_ascii=False) + "\n")
            count += 1
            if count % 20000 == 0:
                log(f"  {count} variants slimmed ({time.time() - t0:.0f} s)")
    if count == 0:
        log("!! the bulk file has no variants; stopping")
        sys.exit(1)
    log(f"{count} variants written to {slim_path.name}")

    manifest_path = CACHE / "collect_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    manifest["spellbook_bulk"] = {
        "uri": URL,
        "file": dest.name,
        "slim_file": slim_path.name,
        "built_at": meta.get("timestamp"),
        "version": meta.get("version"),
        "variants": count,
        "sha256": sha256_of(dest),
        "run_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    log(f"=== done in {round(time.time() - started, 1)} s; manifest updated ===")


if __name__ == "__main__":
    main()
