#!/usr/bin/env python3
"""Validate a ManaBox deck text export and its collection CSV.

Offline checks always run: format, counts, singleton, basic lands, the language, foil and
condition of every copy, and whether the text and the CSV list the same printings.
Online checks resolve every printing through Scryfall and are skipped with --offline.

Run it with the "Run Python File" button (no arguments): it reads the defaults below and
writes a report to data/validation/ (a .json and a .txt with the same name). Arguments
override the defaults:
  python scripts/validate_deck_export.py [DECK.txt] [--csv FILE.csv] [--deck-name NAME]
                                         [--offline] [--out REPORT.json]
"""
import argparse
import csv
import json
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
DEFAULT_CSV = RAW / "ManaBox_Collection.csv"
DEFAULT_RUNS = [(RAW / "Toph.txt", "Toph"), (RAW / "Azula.txt", "Azula")]
OUT_DIR = ROOT / "data" / "validation"

LINE_RE = re.compile(r"^(\d+)\s+(.+?)\s+\(([A-Za-z0-9]+)\)\s+(\S+)(?:\s+\*[A-Za-z]\*)?\s*$")  # ManaBox marks foils with *F*
BASICS = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}
BAD_LAYOUTS = {"token", "double_faced_token", "emblem", "art_series"}
API = "https://api.scryfall.com"
HEADERS = {"User-Agent": "magic-decks-optimization/0.1", "Accept": "application/json"}


def is_basic(name):
    """True for basic lands (including snow-covered ones)."""
    return name in BASICS or (name.startswith("Snow-Covered ") and name[13:] in BASICS)


def parse_deck(path):
    """Return (commanders, mainboard, unparsed). Entries are dicts."""
    commanders, mainboard, bad = [], [], []
    section = "MAIN"
    with open(path, encoding="utf-8-sig") as fh:
        for raw in fh:
            line = raw.strip()
            if not line:
                # ManaBox ends the commander block with a blank line and no new header.
                if section.startswith("COMMANDER"):
                    section = "MAIN"
                continue
            if line.startswith("//"):
                section = line[2:].strip().upper() or "MAIN"
                continue
            m = LINE_RE.match(line)
            if not m:
                bad.append(line)
                continue
            entry = {
                "qty": int(m.group(1)),
                "name": m.group(2),
                "set": m.group(3).lower(),
                "num": m.group(4),
            }
            (commanders if section.startswith("COMMANDER") else mainboard).append(entry)
    return commanders, mainboard, bad


def read_csv(path, deck_name):
    """Return (rows of the deck, all binder names). Headers are matched by name."""
    with open(path, encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        reader.fieldnames = [h.strip().lower() for h in reader.fieldnames or []]
        rows = list(reader)
    binders = Counter()
    deck_rows = []
    for r in rows:
        bname = (r.get("binder name") or "").strip()
        btype = (r.get("binder type") or "").strip().lower()
        binders[(btype, bname)] += int(r.get("quantity") or 1)
        if deck_name is None or bname.lower() == deck_name.lower():
            if btype == "deck":  # a binder with the same name must not merge into the deck
                deck_rows.append(r)
    return deck_rows, binders


def scryfall_collection(identifiers):
    import requests

    found, missing = {}, []
    for i in range(0, len(identifiers), 75):
        chunk = identifiers[i : i + 75]
        resp = requests.post(
            f"{API}/cards/collection",
            headers=HEADERS,
            json={"identifiers": chunk},
            timeout=30,
        )
        resp.raise_for_status()
        body = resp.json()
        for card in body.get("data", []):
            found[(card["set"], card["collector_number"])] = card
        missing += body.get("not_found", [])
        time.sleep(0.6)
    return found, missing


def spanish_record_exists(set_code, num):
    import requests

    resp = requests.get(f"{API}/cards/{set_code}/{num}/es", headers=HEADERS, timeout=30)
    time.sleep(0.15)
    return resp.status_code == 200


def front(name):
    return name.split(" // ")[0].strip().lower()


def validate(args):
    """Validate one deck export: prints the report, writes it and returns the problem list."""
    report, problems = {}, []
    commanders, main_cards, bad = parse_deck(args.deck)
    entries = commanders + main_cards
    total = sum(e["qty"] for e in entries)
    report["entry_lines"] = len(entries)
    report["total_cards"] = total
    report["commanders"] = [e["name"] for e in commanders]
    if bad:
        problems.append(f"{len(bad)} unparsed lines: {bad[:3]}")
    if total != 100:
        problems.append(f"total is {total}, expected 100")
    if len(commanders) != 1 or commanders[0]["qty"] != 1:
        problems.append("expected exactly one commander line under // COMMANDER")
    dup = [n for n, c in Counter(e["name"] for e in entries if not is_basic(e["name"])).items() if c > 1]
    over = [e["name"] for e in entries if not is_basic(e["name"]) and e["qty"] > 1]
    if dup or over:
        problems.append(f"singleton violated: {sorted(set(dup + over))}")
    report["basic_lands"] = sum(e["qty"] for e in entries if is_basic(e["name"]))

    # CSV: language per copy and agreement with the text export.
    if args.csv:
        deck_rows, binders = read_csv(args.csv, args.deck_name)
        report["binders_in_csv"] = {f"{t}:{n}": q for (t, n), q in binders.items()}
        langs = Counter()
        csv_prints = Counter()
        for r in deck_rows:
            q = int(r.get("quantity") or 1)
            langs[(r.get("language") or "?").strip().lower()] += q
            csv_prints[((r.get("set code") or "").strip().lower(), (r.get("collector number") or "").strip())] += q
        report["csv_deck_rows"] = len(deck_rows)
        report["csv_deck_total"] = sum(csv_prints.values())
        report["languages"] = dict(langs)
        txt_prints = Counter()
        for e in entries:
            txt_prints[(e["set"], e["num"])] += e["qty"]
        if not deck_rows:
            problems.append("no CSV rows for that deck; check --deck-name against binders_in_csv")
        elif csv_prints != txt_prints:
            only_txt = sorted((txt_prints - csv_prints).keys())
            only_csv = sorted((csv_prints - txt_prints).keys())
            problems.append(f"text and CSV differ. only in text: {only_txt[:5]}; only in CSV: {only_csv[:5]}")
        report["spanish_copies"] = langs.get("es", 0)
        report["english_copies"] = langs.get("en", 0)
        report["spanish_cards"] = sorted(
            f"{r.get('name')} ({(r.get('set code') or '').strip()} {(r.get('collector number') or '').strip()})"
            for r in deck_rows
            if (r.get("language") or "").strip().lower() == "es"
        )
        for col in ("foil", "condition", "proxy", "misprint", "altered", "signed"):
            report[f"csv_{col}"] = dict(Counter((r.get(col) or "?").strip().lower() for r in deck_rows))
        if langs.keys() - {"en", "es"}:
            problems.append(f"languages other than en/es: {dict(langs)}")

    # Scryfall: resolve every printing.
    if not args.offline:
        try:
            import requests  # noqa: F401  (checked early for a clear message)
        except ImportError:
            print("The 'requests' package is missing in this environment. Run once:")
            print("  pip install -r requirements.txt")
            print("or run this script with --offline.")
            sys.exit(2)
        ids = [{"set": e["set"], "collector_number": e["num"]} for e in entries]
        found, missing = scryfall_collection(ids)
        if missing:
            problems.append(f"{len(missing)} printings not found on Scryfall: {missing[:5]}")
        cmd_card = found.get((commanders[0]["set"], commanders[0]["num"])) if commanders else None
        cmd_ci = set(cmd_card["color_identity"]) if cmd_card else None
        gc, illegal, outside, wrong_name, odd = [], [], [], [], []
        for e in entries:
            card = found.get((e["set"], e["num"]))
            if not card:
                continue
            if front(card["name"]) != front(e["name"]):
                wrong_name.append(f'{e["name"]} -> {card["name"]}')
            if card["legalities"].get("commander") != "legal":
                illegal.append(f'{card["name"]}: {card["legalities"].get("commander")}')
            if cmd_ci is not None and not set(card["color_identity"]) <= cmd_ci:
                outside.append(card["name"])
            if card.get("game_changer"):
                gc.append(card["name"])
            if card.get("layout") in BAD_LAYOUTS or card.get("set_type") == "memorabilia" or card.get("oversized"):
                odd.append(card["name"])
        report["game_changers"] = gc
        for label, items in (
            ("name does not match its set/number", wrong_name),
            ("not Commander-legal", illegal),
            ("outside the commander's color identity", outside),
            ("token, oversized or memorabilia", odd),
        ):
            if items:
                problems.append(f"{label}: {items}")
        if args.csv and report.get("spanish_copies"):
            no_es = []
            for r in deck_rows:
                if (r.get("language") or "").strip().lower() == "es":
                    s = (r.get("set code") or "").strip().lower()
                    n = (r.get("collector number") or "").strip()
                    if not spanish_record_exists(s, n):
                        no_es.append(f"{r.get('name')} ({s} {n})")
            report["spanish_rows_without_scryfall_es_record"] = no_es

    report["problems"] = problems
    report["mode"] = "offline" if args.offline else "online"
    report["run_at_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    text = json.dumps(report, indent=2, ensure_ascii=False)
    print(text)
    print("\nRESULT:", "PROBLEMS FOUND" if problems else "OK")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    if args.out:
        json_path = Path(args.out)
    else:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        json_path = OUT_DIR / f"{Path(args.deck).stem}-{stamp}.json"
    json_path.write_text(text, encoding="utf-8")
    json_path.with_suffix(".txt").write_text(
        text + "\n\nRESULT: " + ("PROBLEMS FOUND" if problems else "OK") + "\n", encoding="utf-8"
    )
    print(f"Report written to {json_path} (and .txt)")
    return problems


def main():
    """With no arguments, validate every deck in DEFAULT_RUNS against the shared collection CSV."""
    ap = argparse.ArgumentParser()
    ap.add_argument("deck", nargs="?")
    ap.add_argument("--csv", default=str(DEFAULT_CSV))
    ap.add_argument("--deck-name")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--out")
    args = ap.parse_args()

    if args.deck:
        runs = [(args.deck, args.deck_name or Path(args.deck).stem)]
    else:
        runs = [(str(path), name) for path, name in DEFAULT_RUNS if Path(path).exists()]
    if not runs:
        print("No deck files found; expected the defaults listed in DEFAULT_RUNS.")
        sys.exit(2)
    failed = []
    for deck, name in runs:
        print(f"\n===== {name}: {deck}")
        run_args = argparse.Namespace(deck=deck, csv=args.csv, deck_name=name,
                                      offline=args.offline, out=args.out if len(runs) == 1 else None)
        if validate(run_args):
            failed.append(name)
    print("\nSUMMARY:", "problems in " + ", ".join(failed) if failed else "all decks OK")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
