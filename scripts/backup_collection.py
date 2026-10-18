#!/usr/bin/env python3
"""Phase 1: back up and verify the owner's ManaBox collection export. No network, nothing is deleted.

Run it with the "Run Python File" button (no arguments). It reads data/raw/ManaBox_Collection.csv and:
  1. counts the cards (rows, copies, copies per binder or deck, per language) and compares them with
     what the ManaBox app showed on 2026-10-17 (EXPECTED below, from the owner's screenshot);
  2. copies every file of data/raw/ into data/raw/backups/<UTC stamp>/, writes SHA256SUMS.txt, marks the
     copies read-only and re-reads each copy to prove the hashes match;
  3. writes REPORT.txt next to them.
To check a copy kept somewhere else (USB drive, cloud folder), put its folder in VERIFY_FOLDER and run
it again: it only re-checks that folder's SHA256SUMS.txt and says OK or lists what differs.

data/raw/ is git-ignored (private): this backup is NOT in git. Copy the backup folder elsewhere yourself.
"""
import csv
import hashlib
import os
import shutil
import stat
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
BACKUPS = RAW / "backups"
CSV_NAME = "ManaBox_Collection.csv"
VERIFY_FOLDER = ""  # e.g. r"E:\backup\collection-20261017T2300Z"; empty = make a new backup

# What the ManaBox app showed on 2026-10-17 (owner's screenshot): the four binders and the total.
EXPECTED = {"total": 1364, "binders": {"Lands": 293, "Tokens": 27, "English Cards": 691, "Spanish Cards": 153}}


def sha256(path):
    """SHA-256 of a file, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_rows(path):
    """Rows of a ManaBox CSV as dicts with lower-case header names."""
    with open(path, encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        reader.fieldnames = [h.strip().lower() for h in reader.fieldnames or []]
        return list(reader)


def count_collection(rows):
    """Copies per (binder type, binder name), per language, per (binder name, language) and the total."""
    by_binder, by_language, by_binder_language = Counter(), Counter(), Counter()
    total = 0
    for row in rows:
        qty = int(row.get("quantity") or 1)
        btype = (row.get("binder type") or "").strip().lower()
        binder = (row.get("binder name") or "").strip()
        language = (row.get("language") or "").strip().lower()
        by_binder[(btype, binder)] += qty
        by_language[language] += qty
        by_binder_language[(binder, language)] += qty
        total += qty
    return {"total": total, "rows": len(rows), "by_binder": by_binder, "by_language": by_language,
            "by_binder_language": by_binder_language}


def check_collection(counts, expected=EXPECTED):
    """Report lines: each is (ok, text). Compares with the app's numbers and checks the language binders."""
    out = [(counts["total"] == expected["total"],
            f"total copies {counts['total']} (the app showed {expected['total']})")]
    in_binders = 0
    for name, want in expected["binders"].items():
        got = sum(n for (btype, binder), n in counts["by_binder"].items() if binder == name)
        in_binders += got
        out.append((got == want, f"binder '{name}': {got} copies (the app showed {want})"))
    decks = sum(n for (btype, _), n in counts["by_binder"].items() if btype == "deck")
    rest = counts["total"] - in_binders
    out.append((rest == decks, f"outside the 4 binders: {rest} copies, of which in decks: {decks}"))
    wrong_en = sum(n for (binder, lang), n in counts["by_binder_language"].items()
                   if binder == "English Cards" and lang != "en")
    wrong_es = sum(n for (binder, lang), n in counts["by_binder_language"].items()
                   if binder == "Spanish Cards" and lang != "es")
    out.append((wrong_en == 0, f"'English Cards' copies not marked English: {wrong_en}"))
    out.append((wrong_es == 0, f"'Spanish Cards' copies not marked Spanish: {wrong_es}"))
    return out


def write_sums(folder, names):
    """SHA256SUMS.txt for the given file names in a folder."""
    lines = [f"{sha256(folder / n)}  {n}" for n in sorted(names)]
    (folder / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return lines


def verify_folder(folder):
    """Problems found when re-hashing the files a folder's SHA256SUMS.txt lists (empty list = all good)."""
    sums = folder / "SHA256SUMS.txt"
    if not sums.exists():
        return ["SHA256SUMS.txt is missing"]
    problems, listed = [], set()
    for line in sums.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, name = line.split("  ", 1)
        listed.add(name)
        path = folder / name
        if not path.exists():
            problems.append(f"missing: {name}")
        elif sha256(path) != digest:
            problems.append(f"DIFFERENT: {name}")
    extra = {p.name for p in folder.iterdir() if p.is_file()} - listed - {"SHA256SUMS.txt", "REPORT.txt"}
    problems += [f"not in the list: {n}" for n in sorted(extra)]
    return problems


def main():
    if VERIFY_FOLDER:
        problems = verify_folder(Path(VERIFY_FOLDER))
        print("VERIFIED: every file matches its hash." if not problems else "PROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(1 if problems else 0)
    csv_path = RAW / CSV_NAME
    if not csv_path.exists():
        print(f"{CSV_NAME} not found in data/raw/. Export it from ManaBox first.")
        sys.exit(2)
    counts = count_collection(read_rows(csv_path))
    report = [f"Collection export read: {counts['rows']} rows, {counts['total']} copies",
              "Per language: " + ", ".join(f"{k or '?'}={v}" for k, v in sorted(counts["by_language"].items())),
              "Per binder or deck: " + ", ".join(f"{b} ({t})={n}" for (t, b), n in sorted(counts["by_binder"].items()))]
    checks = check_collection(counts)
    report += [("OK       " if ok else "MISMATCH ") + text for ok, text in checks]
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    folder = BACKUPS / f"collection-{stamp}"
    folder.mkdir(parents=True)
    names = [p.name for p in RAW.iterdir() if p.is_file()]
    for name in names:
        shutil.copy2(RAW / name, folder / name)
    write_sums(folder, names)
    problems = verify_folder(folder)
    for name in names:  # read-only copies: an accidental edit or delete needs a deliberate extra step
        os.chmod(folder / name, stat.S_IREAD)
    report.append(f"Backup: {len(names)} files copied to data/raw/backups/collection-{stamp}/")
    report.append("Hash re-check of the copies: " + ("OK" if not problems else "PROBLEMS " + "; ".join(problems)))
    text = "\n".join(report) + "\n"
    (folder / "REPORT.txt").write_text(text, encoding="utf-8")
    print(text)
    sys.exit(1 if problems or not all(ok for ok, _ in checks) else 0)


if __name__ == "__main__":
    main()
