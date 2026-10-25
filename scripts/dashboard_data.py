#!/usr/bin/env python3
"""Phase 8 step 4: the datasets of the budget dashboard (an Artifact of the Dashboard type).

Run it with the "Run Python File" button (no arguments, no network). It reads `decks/proposals/measured.json` and writes
JSON row files into `data/model/dashboard/`, which are uploaded to the dashboard as its datasets:

  lists.json  every measured list that can be on a chart (status: offered, dominated by a cheaper list, replaced, variant;
              plus, for reference only, "older" round-2 lists without a saved list and the owner's own lists, "start").
              The "offered" lists of a deck come from every round, so the chart's line is the best power at each spend
  plans.json  the plan of each budget: one row per budget (the deck pages read the 200,000 CLP row, the statistics its list ids)
  decks.json  one row per deck: measured numbers plus the hand-written status of deck-notes.json

`scripts/deck_stats.py` writes the statistics datasets next to them. The deck pages (plan of play, Commander Salt combos
with steps, how to play each of the 100 cards) are written by hand in `playbook-<deck>.json` and `guide.json` (combos only)
and turned into the `playbook` dataset by `scripts/dashboard_playbook.py`; `scripts/dashboard_cards.py` fetches the card
images. `deck-notes.json` is written by hand and only read here. The plans come from `scripts/optimize_budget.py` (highest sum of
powers, no parity rule); this script adds nothing to them. Alexios, Deimos of Kosmos was replaced by Ezio Auditore da
Firenze: his round-2 lists stay on the charts (status "replaced") so the owner sees where he ended, and a variant list (the
black-core Ezio test) is charted as its own series; neither ever enters a plan.
"""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEASURED = ROOT / "decks" / "proposals" / "measured.json"
OUT_DIR = ROOT / "data" / "model" / "dashboard"
SHORT = {"ezio-auditore-da-firenze": "Ezio", "fire-lord-azula": "Azula", "toph-the-first-metalbender": "Toph",
         "alexios-deimos-of-kosmos": "Alexios"}
VARIANT_NAME = {"bcore": "black-core"}
TABLE_ORDER = ["Ezio", "Azula", "Toph"]  # the column order of "What each budget buys"
REPLACED = {"alexios-deimos-of-kosmos"}  # measured, shown, never planned

spec = importlib.util.spec_from_file_location("optimize_budget", Path(__file__).resolve().parent / "optimize_budget.py")
ob = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ob)


def step_of(label):
    return int(label.rsplit("step", 1)[1].split("-")[0])


def variant_of(label):
    """'round4-bcore-step26' -> 'bcore'; 'round4-step26' -> ''."""
    parts = label.split("-")
    return parts[1] if len(parts) == 3 else ""


def round_of(label):
    return int(label.split("-")[0].replace("round", ""))


def list_id(deck, label):
    variant = variant_of(label)
    return f"{SHORT[deck].lower()}{'-' + variant if variant else ''}-r{round_of(label)}-{step_of(label)}"


def series_name(deck, label):
    variant = variant_of(label)
    return SHORT[deck] + (f" {VARIANT_NAME.get(variant, variant)}" if variant else "")


def list_name(label):
    step = step_of(label)
    variant = variant_of(label)
    base = f"R{round_of(label)} step {step}" + (" (free base)" if step == 0 else "")
    return f"{VARIANT_NAME.get(variant, variant).capitalize()} {base}" if variant else base


def charted(measured, plans=()):
    """[(deck slug, label, entry, status)] for every measured list that appears on a chart. A list is offered when it is on
    its deck's frontier or when some plan row uses it."""
    frontier = ob.load_points(measured)
    offered = {(deck, p["label"]) for deck, pts in frontier.items() for p in pts}
    offered |= {(deck, point["label"]) for row in plans for deck, point in (row.get("decks") or {}).items()}
    out = []
    for key, entry in measured["lists"].items():
        deck, label = key.split("/", 1)
        if entry.get("power") is None:
            continue
        if deck in REPLACED:
            out.append((deck, label, entry, "replaced"))
        elif entry.get("variant"):
            out.append((deck, label, entry, "variant"))
        elif entry.get("eligible", (entry.get("round") or 0) >= ob.MIN_ROUND):
            out.append((deck, label, entry, "offered" if (deck, label) in offered else "dominated"))
    return out


def older(measured):
    """[(deck slug, label, entry, status)] of the lists shown for reference only, never offered: the owner's own lists
    ("start") and the round-2 lists whose exact list was not saved ("older"). Round 1 holds reversible cards: never charted."""
    out = []
    for key, entry in measured["lists"].items():
        deck, label = key.split("/", 1)
        if entry.get("power") is None or deck in REPLACED or entry.get("variant"):
            continue
        if label == "owner-list":
            out.append((deck, label, entry, "start"))
        elif entry.get("round") == 2 and not entry.get("eligible"):
            out.append((deck, label, entry, "older"))
    return out


def older_row(deck, label, entry, status):
    """A reference row. Labels such as 'round2-step24-plus-9-duals' keep their tail so that two lists never share an id."""
    short = SHORT[deck].lower()
    if status == "start":
        ident, name, step, rnd = f"{short}-owner", "Owner's list", None, "Start"
    else:
        tail = label.split("-")[2:]
        ident = list_id(deck, label) + ("-" + "-".join(tail) if tail else "")
        name = list_name(label) + (" " + " ".join(tail) if tail else "")
        step, rnd = step_of(label), f"R{round_of(label)}"
    return {"id": ident, "deck": SHORT[deck], "list": name, "round": rnd, "step": step, "cost_clp": entry["cost_clp"],
            "power": entry["power"], "salt": entry.get("salt"), "manabase_pct": entry.get("manabase_quality_pct"),
            "bracket": entry.get("bracket"), "wotc_bracket": entry.get("wotc_bracket"), "status": status}


def lists_rows(measured, plans=()):
    rows = [{"id": list_id(deck, label), "deck": series_name(deck, label), "list": list_name(label),
             "round": f"R{round_of(label)}", "step": step_of(label), "cost_clp": entry["cost_clp"], "power": entry["power"],
             "salt": entry.get("salt"), "manabase_pct": entry.get("manabase_quality_pct"), "bracket": entry.get("bracket"),
             "wotc_bracket": entry.get("wotc_bracket"), "status": status}
            for deck, label, entry, status in charted(measured, plans)]
    rows += [older_row(*item) for item in older(measured)]
    return sorted(rows, key=lambda r: (r["deck"], r["cost_clp"]))


def plan_rows(rows):
    out = []
    for row in rows:
        if not row.get("decks"):
            continue
        cells = {}
        for deck, point in row["decks"].items():
            name = SHORT[deck].lower()
            cells.update({f"{name}_list": list_name(point["label"]), f"{name}_cost": point["cost"],
                          f"{name}_power": point["power"],
                          f"{name}_cell": f"{list_name(point['label'])} ({point['cost']:,} CLP)",
                          f"{name}_id": list_id(deck, point["label"])})
        powers = " / ".join(f"{row['decks'][d]['power']:.1f}" for d in sorted(row["decks"], key=lambda d: TABLE_ORDER.index(SHORT[d])))
        out.append({"id": str(row["budget"]), "budget_clp": row["budget"], **cells, "powers": powers,
                    "total_cost_clp": row["cost"], "shared_extra_clp": row.get("shared_extra", 0),
                    "unspent_clp": row["unspent"], "sum_power": row["sum_power"],
                    "weakest": row["min_power"], "gap": row["gap"]})
    return out


def deck_rows(measured, plan_rows_, notes):
    plan = next((r for r in plan_rows_ if r["budget"] == 150_000 and r.get("decks")), None)
    out = []
    for slug, short in SHORT.items():
        entries = [e for k, e in measured["lists"].items()
                   if k.startswith(slug + "/") and e.get("power") is not None and not e.get("variant")]
        top = max((e["power"] for e in entries), default=None)
        cheapest = min((e["cost_clp"] for e in entries if e["power"] == top), default=None)
        chosen = plan["decks"].get(slug) if plan else None
        note = notes.get(short, {})
        out.append({"id": short.lower(), "deck": short, "commander": note.get("commander"), "colors": note.get("colors"),
                    "role": note.get("role"), "best_power": top, "best_cost_clp": cheapest,
                    "lists_measured": len(entries),
                    "pick_list": list_name(chosen["label"]) if chosen else None,
                    "pick_cost_clp": chosen["cost"] if chosen else None,
                    "pick_power": chosen["power"] if chosen else None,
                    "status": note.get("status"), "next_step": note.get("next_step"),
                    "progress_pct": note.get("progress_pct")})
    return out


def main():
    measured = json.loads(MEASURED.read_text(encoding="utf-8"))
    _, rows = ob.plan(measured)  # joint costs: an owned card two decks play is bought again for the second deck
    notes_path = OUT_DIR / "deck-notes.json"
    notes = json.loads(notes_path.read_text(encoding="utf-8")) if notes_path.exists() else {}
    files = {"lists": lists_rows(measured, rows), "plans": plan_rows(rows), "decks": deck_rows(measured, rows, notes)}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, data in files.items():
        (OUT_DIR / f"{name}.json").write_text(json.dumps({"rows": data}, indent=1, ensure_ascii=False) + "\n",
                                              encoding="utf-8")
        print(f"{name}.json: {len(data)} rows")
    print(f"Wrote {OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
