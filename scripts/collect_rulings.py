#!/usr/bin/env python3
"""Collect the official Scryfall rulings for the cards the research works with.

Run it with the "Run Python File" button (no arguments), after collect_research_data.py.
It needs internet and takes well under a minute. It writes only under data/cache/
(git-ignored):

  rulings-<timestamp>.jsonl.gz raw Scryfall bulk file of all rulings (one object per ruling)
  rulings_pool.jsonl           the rulings of every card in the three commander pools, each
                               line: name, oracle_id, source, published_at, comment
  collect_manifest.json        gets a "rulings" entry (file, date, counts, checksum)
  collect_progress.log         shared progress log

Source: the Scryfall bulk-data endpoint (type "rulings"). Rulings are official Wizards
clarifications reprinted by Scryfall; they are the evidence for rules readings in the
synergy reports.
"""
import json
import sys
import time
from datetime import datetime, timezone

from collect_research_data import CACHE, download_bulk, iter_cards, log, sha256_of

RULING_FIELDS = ("oracle_id", "source", "published_at", "comment")


def load_pool_names(cache_dir):
    """Map oracle_id -> card name over every pool_<slug>.jsonl in the cache directory."""
    names = {}
    for path in sorted(cache_dir.glob("pool_*.jsonl")):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    card = json.loads(line)
                    if card.get("oracle_id"):
                        names[card["oracle_id"]] = card.get("name")
    return names


def filter_rulings(rulings, names):
    """Keep the rulings whose oracle_id is in names; add the card name. Returns (kept, total)."""
    kept, total = [], 0
    for ruling in rulings:
        total += 1
        oracle_id = ruling.get("oracle_id")
        if oracle_id in names:
            out = {"name": names[oracle_id]}
            out.update({key: ruling.get(key) for key in RULING_FIELDS})
            kept.append(out)
    return kept, total


def main():
    """Download the rulings bulk file, filter it to the pools and update the manifest."""
    try:
        import requests
    except ImportError:
        print("The 'requests' package is missing in this environment. Run once:")
        print("  pip install -r requirements.txt")
        sys.exit(2)

    started = time.time()
    log("=== collect_rulings start ===")
    names = load_pool_names(CACHE)
    if not names:
        log("!! no pool_*.jsonl files in data/cache/; run collect_research_data.py first")
        sys.exit(1)
    log(f"{len(names)} distinct cards across the commander pools")

    bulk_path, bulk_meta = download_bulk(requests, "rulings")
    bulk_meta["sha256"] = sha256_of(bulk_path)

    log("reading the rulings bulk file")
    kept, total = filter_rulings(iter_cards(bulk_path), names)
    out_path = CACHE / "rulings_pool.jsonl"
    with open(out_path, "w", encoding="utf-8") as fh:
        for ruling in kept:
            fh.write(json.dumps(ruling, ensure_ascii=False) + "\n")
    cards_with_rulings = len({r["oracle_id"] for r in kept})
    bulk_meta.update(
        rulings_total=total,
        rulings_kept=len(kept),
        pool_cards=len(names),
        pool_cards_with_rulings=cards_with_rulings,
        pool_file=out_path.name,
        run_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    )
    log(f"{total} rulings in the bulk file; kept {len(kept)} for {cards_with_rulings} "
        f"of the {len(names)} pool cards")

    manifest_path = CACHE / "collect_manifest.json"
    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["rulings"] = bulk_meta
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    log(f"=== done in {round(time.time() - started, 1)} s; "
        f"output: data/cache/{out_path.name}, manifest updated ===")


if __name__ == "__main__":
    main()
