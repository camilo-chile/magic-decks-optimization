#!/usr/bin/env python3
"""Phase 2: which deck holds each physical card, from the staged scans (owner decision, 2026-10-30).

Run it with the "Run Python File" button (no arguments). No network. The owner scans one deck at a time into the two
binders (Spanish, English) and exports a full CSV of both binders after each stage, in this order: ezio, azula, toph,
rest. File names: data/collection/ManaBox_Collection_<YYYY-MM-DD>_<stage>.csv. Every export is cumulative, so the rows
that are new against the previous export are the cards of that stage's deck ("rest" is the free collection).

A physical row is identified by its exact data: Scryfall printing, finish, language, condition, binder, proxy, misprint,
altered and signed. A row removed or changed between two exports is reported, never guessed at: the new rows always
belong to the new stage.

Writes
  data/cache/collection_owned.json  every owned row with its stage and deck (untracked, regenerable)
  decks/scanned/<slug>.txt          the deck as scanned, `1 Name (SET) 123 *F*` per printing (ManaBox / Moxfield text)
  decks/scanned/<slug>.csv          the same with language, condition, binder, proxy, Scryfall ID, and the deck's tokens
  decks/reports/scan-stages.md      stages, problems, and each scanned deck against its planned list
"""
import csv
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_inventory as bi  # noqa: E402  (CSV reader, token and binder rules, stage names)
import layer_a as la  # noqa: E402

ROOT = la.ROOT
COLLECTION_DIR = bi.COLLECTION_DIR
STAGES = bi.STAGES
STAGE_DECK = {stage: bi.PROJECT_DECKS.get(stage) for stage in STAGES}
CONFIG_PATH = ROOT / "decks" / "phase2.json"
OUT_PATH = ROOT / "data" / "cache" / "collection_owned.json"
SCANNED_DIR = ROOT / "decks" / "scanned"
REPORT_PATH = ROOT / "decks" / "reports" / "scan-stages.md"
KEY_FIELDS = ("scryfall id", "foil", "language", "condition", "binder name", "proxy", "misprint", "altered", "signed")
DETAIL_FIELDS = ("name", "set code", "set name", "collector number", "rarity", "binder name", "binder type")
FINISH_MARK = {"foil": " *F*", "etched": " *E*"}
DECK_SIZE = 100


def stage_files(directory=COLLECTION_DIR):
    """{stage: newest export of that stage}; exports without a stage suffix (the old collection) are ignored."""
    found = {}
    for path in sorted(Path(directory).glob("ManaBox_Collection_*_*.csv")):
        m = bi.STAGE_FILE_RE.match(path.name)
        if m and m.group(2) in STAGES:
            found[m.group(2)] = path  # sorted by name, so the latest date of a stage wins
    return found


def row_key(row):
    """The exact identity of a physical row (lower-cased text, so ManaBox spelling changes do not matter)."""
    return tuple((row.get(field) or "").strip().lower() for field in KEY_FIELDS)


def quantity(row):
    try:
        return max(int(float(row.get("quantity") or 1)), 0)
    except ValueError:
        return 1


def count_rows(rows):
    """(Counter {key: copies}, {key: descriptive fields}) for the rows of one export."""
    counts, details = Counter(), {}
    for row in rows:
        key = row_key(row)
        counts[key] += quantity(row)
        if key not in details:
            info = {field: (row.get(field) or "").strip() for field in DETAIL_FIELDS}
            info["token"] = bi.is_token_row(row)
            details[key] = info
    return counts, details


def split_stages(stage_rows):
    """stage_rows: [(stage, rows)] in stage order -> {"holdings": {stage: Counter}, "details", "removed", "problems"}.

    holdings[stage] are the copies that are new in that export. A copy that disappears from a later export is taken
    away from the most recent stage that held it and listed in "removed" (with a flag when the same Scryfall printing
    was added in that same export, which is how an edited row looks)."""
    holdings, details, removed, problems = {}, {}, [], []
    names = [stage for stage, _ in stage_rows]
    for i, stage in enumerate(STAGES):
        missing = [s for s in STAGES[:i] if s not in names]
        if stage in names and missing:
            problems.append(f"stage {stage} found but earlier stage(s) {', '.join(missing)} missing: "
                            f"their cards are counted in {stage}")
    previous = Counter()
    for stage, rows in stage_rows:
        current, info = count_rows(rows)
        for key, value in info.items():
            details.setdefault(key, value)
        added, gone = current - previous, previous - current
        added_ids = {key[0] for key in added}
        for key, qty in sorted(gone.items()):
            left = qty
            for earlier in reversed(list(holdings)):
                take = min(left, holdings[earlier][key])
                if take:
                    holdings[earlier][key] -= take
                    left -= take
                if not left:
                    break
            removed.append({"stage": stage, "key": key, "quantity": qty, "printing_added_again": key[0] in added_ids})
        holdings[stage] = added
        previous = current
    for stage in holdings:
        holdings[stage] = +holdings[stage]  # drop the zero entries
    return {"holdings": holdings, "details": details, "removed": removed, "problems": problems}


def owned_records(split):
    """One record per distinct physical row: stage, deck, copies, and the exact data as scanned."""
    out = []
    for stage, counter in split["holdings"].items():
        for key, qty in counter.items():
            info = split["details"][key]
            out.append({
                "stage": stage, "deck": STAGE_DECK[stage], "quantity": qty, "token": info["token"],
                "name": info["name"], "set": info["set code"].upper(), "set_name": info["set name"],
                "number": info["collector number"], "rarity": info["rarity"],
                "scryfall_id": key[0], "finish": key[1] or "normal", "language": key[2], "condition": key[3],
                "binder": info["binder name"], "binder_type": info["binder type"],
                "proxy": bi.truthy(key[5]), "misprint": bi.truthy(key[6]), "altered": bi.truthy(key[7]),
                "signed": bi.truthy(key[8]),
            })
    out.sort(key=lambda r: (r["token"], r["name"].casefold(), r["set"], r["number"], r["finish"], r["language"]))
    return out


def scan_problems(records):
    """Scan errors worth a second look: a language that does not match its binder, an unexpected language or condition."""
    problems = []
    for r in records:
        where = f"{r['name']} ({r['set']} {r['number']}, {r['language']}, {r['finish']}) in binder {r['binder']!r}"
        promised = bi.binder_language(r["binder"])
        if promised and r["language"] and promised != r["language"]:
            problems.append(f"language/binder mismatch: {where} is stage {r['stage']}")
        elif r["language"] not in bi.LANGUAGES_OK:
            problems.append(f"language {r['language']!r} is not en or es: {where}")
        if r["condition"] not in bi.CONDITIONS_OK:
            problems.append(f"unusual condition {r['condition']!r}: {where}")
    return problems


def front(name):
    """Normalized front-face name, so "A // B" matches a decklist that writes only "A"."""
    return la.normalize(name.split(" // ")[0])


def read_plan(path):
    """(Counter {front name: copies}, {front name: display}, commander front names, bad lines) of a planned decklist."""
    commanders, main, bad = la.parse_decklist(Path(path).read_text(encoding="utf-8"))
    plan, shown = Counter(), {}
    for entry in commanders + main:
        plan[front(entry["name"])] += entry["qty"]
        shown.setdefault(front(entry["name"]), entry["name"])
    return plan, shown, {front(e["name"]) for e in commanders}, bad


def compare_to_plan(records, plan, shown):
    """Differences between the scanned deck (tokens left out) and the planned list: three lists of (name, plan, scan)."""
    scanned, scanned_shown = Counter(), {}
    for r in records:
        if not r["token"]:
            scanned[front(r["name"])] += r["quantity"]
            scanned_shown.setdefault(front(r["name"]), r["name"])
    only_plan = [(shown[n], plan[n], 0) for n in sorted(plan) if n not in scanned]
    only_scan = [(scanned_shown[n], 0, scanned[n]) for n in sorted(scanned) if n not in plan]
    differ = [(shown[n], plan[n], scanned[n]) for n in sorted(plan) if n in scanned and plan[n] != scanned[n]]
    return only_plan, only_scan, differ


def printing_line(rec, qty):
    tail = f" ({rec['set']}) {rec['number']}" if rec["set"] and rec["number"] else ""
    return f"{qty} {rec['name']}{tail}{FINISH_MARK.get(rec['finish'], '')}"


def deck_text(records, commander_names):
    """The scanned deck as plain text: a `// Commander` block, a blank line, then one line per printing and finish.

    There is no `// Main` header on purpose: Moxfield reads it as a card it cannot find (tested 2026-10-31). The commander
    is one copy of the card named in the plan (the proxy first); tokens are not part of the deck."""
    cards = [dict(r) for r in records if not r["token"]]
    commander = None
    for pick in sorted((r for r in cards if front(r["name"]) in commander_names), key=lambda r: not r["proxy"]):
        commander = dict(pick, quantity=1)
        pick["quantity"] -= 1
        break
    grouped = Counter()
    sample = {}
    for r in cards:
        if r["quantity"] > 0:
            key = (r["name"], r["set"], r["number"], r["finish"])
            grouped[key] += r["quantity"]
            sample.setdefault(key, r)
    lines = []
    if commander:
        lines += ["// Commander", printing_line(commander, 1), ""]  # the blank line ends the commander block
    lines += [printing_line(sample[key], grouped[key]) for key in sorted(grouped, key=lambda k: (k[0].casefold(),) + k[1:])]
    return "\n".join(lines) + "\n"


def write_detail_csv(path, records):
    fields = ["kind", "quantity", "name", "set", "number", "finish", "language", "condition", "binder", "proxy",
              "scryfall_id"]
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for r in records:
            row = {k: r.get(k, "") for k in fields}
            row["kind"] = "token" if r["token"] else "card"
            row["proxy"] = "true" if r["proxy"] else "false"
            writer.writerow(row)


def deck_facts(records):
    """Copies by finish, language and condition, tokens and proxies counted apart."""
    cards = [r for r in records if not r["token"]]

    def by(field):
        totals = Counter()
        for r in cards:
            totals[r[field] or "none"] += r["quantity"]
        return dict(sorted(totals.items()))

    return {"cards": sum(r["quantity"] for r in cards), "tokens": sum(r["quantity"] for r in records if r["token"]),
            "proxies": sum(r["quantity"] for r in cards if r["proxy"]),
            "finish": by("finish"), "language": by("language"), "condition": by("condition")}


def report_markdown(stages, problems, deck_reports, today):
    lines = [f"# Scan stages (generated by scripts/collection_stages.py on {today})", "",
             "| Stage | Deck | File | Rows | Copies | New copies | Tokens | Proxies |", "|---|---|---|---|---|---|---|---|"]
    for s in stages:
        lines.append(f"| {s['stage']} | {s['deck'] or 'free collection'} | {s['file']} | {s['rows']} | {s['copies']} | "
                     f"{s['new_copies']} | {s['tokens']} | {s['proxies']} |")
    lines += ["", "## Problems", ""]
    lines += [f"- {p}" for p in problems] or ["- none"]
    for d in deck_reports:
        facts = d["facts"]
        lines += ["", f"## {d['deck']}: scanned against the planned list", "",
                  f"- Cards: {facts['cards']} (a Commander deck has {DECK_SIZE}); tokens: {facts['tokens']}; "
                  f"proxies: {facts['proxies']}",
                  f"- Finish: {facts['finish']}; language: {facts['language']}; condition: {facts['condition']}"]
        if d["plan"] is None:
            lines.append("- No planned list found to compare with.")
            continue
        for title, rows in (("Only in the planned list (not scanned)", d["only_plan"]),
                            ("Only in the scan (not in the planned list)", d["only_scan"]),
                            ("Different number of copies (plan, scan)", d["differ"])):
            lines.append(f"- {title}: " + ("none" if not rows else "; ".join(
                f"{n} ({p}, {s})" if title.startswith("Different") else n for n, p, s in rows)))
    return "\n".join(lines) + "\n"


def run(files, config, scanned_dir, today):
    """Compute everything from {stage: csv path}; write the deck files into scanned_dir; return the results."""
    stage_rows = [(stage, bi.read_rows(files[stage])) for stage in STAGES if stage in files]
    split = split_stages(stage_rows)
    records = owned_records(split)
    problems = list(split["problems"]) + scan_problems(records)
    for item in split["removed"]:
        info = split["details"][item["key"]]
        extra = " (the same printing was added again: an edited row?)" if item["printing_added_again"] else ""
        problems.append(f"removed in stage {item['stage']}: {item['quantity']} x {info['name']} "
                        f"({item['key'][1] or 'normal'}, {item['key'][2]}){extra}")
    stages = []
    for stage, rows in stage_rows:
        mine = [r for r in records if r["stage"] == stage]
        stages.append({"stage": stage, "deck": STAGE_DECK[stage], "file": files[stage].name, "rows": len(rows),
                       "copies": sum(quantity(r) for r in rows), "new_copies": sum(r["quantity"] for r in mine),
                       "tokens": sum(r["quantity"] for r in mine if r["token"]),
                       "proxies": sum(r["quantity"] for r in mine if r["proxy"] and not r["token"])})
    plans = {d["slug"]: d.get("list") for d in config.get("decks", [])}
    deck_reports = []
    for stage, _ in stage_rows:
        slug = STAGE_DECK[stage]
        if not slug:
            continue
        mine = [r for r in records if r["stage"] == stage]
        plan_path = ROOT / plans[slug] if plans.get(slug) else None
        report = {"deck": slug, "facts": deck_facts(mine), "plan": None}
        commanders = set()
        if plan_path and plan_path.exists():
            plan, shown, commanders, bad = read_plan(plan_path)
            report["plan"] = sum(plan.values())
            report["only_plan"], report["only_scan"], report["differ"] = compare_to_plan(mine, plan, shown)
            problems += [f"{slug}: unreadable line in the planned list: {line}" for line in bad]
        if report["facts"]["cards"] != DECK_SIZE:
            problems.append(f"{slug}: {report['facts']['cards']} cards scanned, a Commander deck has {DECK_SIZE}")
        scanned_dir.mkdir(parents=True, exist_ok=True)
        (scanned_dir / f"{slug}.txt").write_text(deck_text(mine, commanders), encoding="utf-8")
        write_detail_csv(scanned_dir / f"{slug}.csv", mine)
        deck_reports.append(report)
    return {"stages": stages, "problems": problems, "records": records, "deck_reports": deck_reports,
            "removed": split["removed"], "details": split["details"], "report": report_markdown(
                stages, problems, deck_reports, today)}


def main():
    files = stage_files()
    if not files:
        print("No data/collection/ManaBox_Collection_<YYYY-MM-DD>_<stage>.csv found "
              f"(stages: {', '.join(STAGES)}). Export the collection from ManaBox after each stage and save it there.")
        sys.exit(2)
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    result = run(files, config, SCANNED_DIR, date.today().isoformat())
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(result["report"], encoding="utf-8")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps({
        "generated": date.today().isoformat(), "stages": result["stages"], "problems": result["problems"],
        "cards": result["records"]}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(result["report"])
    print(f"wrote {REPORT_PATH.relative_to(ROOT)}, {OUT_PATH.relative_to(ROOT)} and decks/scanned/")


if __name__ == "__main__":
    main()
