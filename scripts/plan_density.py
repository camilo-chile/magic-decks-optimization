#!/usr/bin/env python3
"""Phase 2 consistency gate (owner, 2026-10-30; revised after the Opus review of 2026-10-31).

Does a list have ONE plan with enough pieces of every function it relies on, and a way through the boards a 3 to 4 player pod
produces? Run it with the "Run Python File" button (no arguments). No network. For every `decks/phase2/<slug>.plan.json` it
reads the decklist `decks/phase2/<slug>.txt` next to it and writes `decks/reports/consistency-<slug>.md`.

The plan file is written by the deck builder from the Oracle texts and attacked by a reviewer (docs/research/
phase2-gate-review-20261031.md):
  {"plan": "one sentence", "backup": "one sentence or empty",
   "win_routes": {"route": {"cards": [...], "axis": "combat|noncombat|alternate", "vs_three": "how it beats 3 opponents"}},
   "functions": {"name": {"cards": [...], "needed_by": "early|late"}, "other": [cards]},   # a bare list means early
   "tutors": {"tutor card": ["function it can fetch for", ...]},
   "tags": {"card": "engine|payoff|backup|ramp|draw|removal|wipe|tutor|protection|land|orphan"  # or ["primary", "second"]},
   "bad_when_drawn": {"card": "early|late|never"}}
Basic lands need no tag. The commander needs none and counts as a guaranteed piece of any function that lists it. The two
functions in GATE["required_functions"] (a way through a wide board of small blockers and through bigger creatures) must be
declared. FAIL means the list is not ready for Commander Salt; WARN is a reminder. Thresholds: the 8x8 package size and the
base counts are sourced (docs/research/phase2-consistency-survey-20261031.md), the rest is judgment and marked in GATE.
"""
import json
import sys
from collections import Counter
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402
from assign_copies import is_basic  # noqa: E402

ROOT = la.ROOT
PLANS_DIR = ROOT / "decks" / "phase2"
REPORTS_DIR = ROOT / "decks" / "reports"
TAGS = ("engine", "payoff", "backup", "ramp", "draw", "removal", "wipe", "tutor", "protection", "land", "orphan")
PLAN_TAGS = ("engine", "payoff", "backup")
AXES = ("combat", "noncombat", "alternate")
TIMINGS = ("early", "late")
BAD_WHEN = ("early", "late", "never")
GATE = {
    "max_orphans": 3,  # declared orphans plus every plan card that sits in no function and no route (judgment)
    # Cards seen by turn T are 7 + T in a multiplayer game (no player skips the first draw; Comprehensive Rules 103.8c,
    # recalled, not re-read). Early functions are needed by turn 5 (12 cards), late ones by turn 13 (20 cards).
    "function_classes": {"early": {"min": 10, "seen": 12}, "late": {"min": 6, "seen": 20}},  # judgment, from the odds table
    "required_functions": ("through_wide_board", "through_big_creatures"),  # reference boards of the pod (judgment)
    "min_win_routes": 2,         # disjoint, one of them not a combat route (judgment)
    "seen_report": (7, 12, 16, 20),
    # Warnings only. Survey 2026-10-31: ramp 8 to 13 (10 asked), draw 10 (flag under 8), removal 8 to 10, wipes 2 to 3,
    # lands 36 to 38. Protection has no source: a judgment.
    "base_min": {"ramp": 10, "draw": 8, "removal": 8, "wipe": 2, "protection": 3},
    "land_band": (36, 38),
    "max_bad_when_drawn": 12,    # judgment
}


def odds_at_least_one(pieces, seen, library=99):
    """Chance that at least one of `pieces` specific cards is among `seen` cards drawn from `library` cards."""
    if pieces <= 0:
        return 0.0
    if library - pieces < seen:
        return 1.0
    return 1 - comb(library - pieces, seen) / comb(library, seen)


def front(name):
    return la.normalize(name.split(" // ")[0])


def read_list(path):
    """({front name: copies in the 99}, {front name: display}, commander front names, library size) of a decklist."""
    commanders, main, _ = la.parse_decklist(Path(path).read_text(encoding="utf-8"))
    cards = Counter()
    shown = {}
    for entry in main:
        cards[front(entry["name"])] += entry["qty"]
        shown.setdefault(front(entry["name"]), entry["name"])
    return cards, shown, {front(e["name"]) for e in commanders}, sum(cards.values())


def as_function(value):
    """A function entry as {"cards": [...], "needed_by": "early"}; a bare list means an early function."""
    if isinstance(value, dict):
        return {"cards": list(value.get("cards") or []), "needed_by": value.get("needed_by") or "early"}
    return {"cards": list(value or []), "needed_by": "early"}


def check(cards, shown, commanders, library, plan, gate=GATE):
    """The gate result: fail and warn lists, tag counts, functions, routes, orphans and the plan share."""
    fail, warn = [], []
    if not str(plan.get("plan") or "").strip():
        fail.append("no primary plan declared")
    if not str(plan.get("backup") or "").strip():
        warn.append("no backup plan declared (allowed, but say so on purpose)")

    def known(name):
        return name in cards or name in commanders

    # tags: one primary tag per card, a second one allowed
    tags = {}
    for name, value in (plan.get("tags") or {}).items():
        tags[front(name)] = [value] if isinstance(value, str) else list(value)
    bad = sorted({t for ts in tags.values() for t in ts if t not in TAGS})
    if bad:
        fail.append(f"unknown tags {bad}; use {list(TAGS)}")
    missing = [shown[n] for n in sorted(cards) if n not in tags and not is_basic(shown[n])]
    if missing:
        fail.append(f"{len(missing)} cards without a tag: " + "; ".join(missing))
    extra = sorted(n for n in tags if not known(n))
    if extra:
        warn.append("tags for cards that are not in the list: " + "; ".join(extra))
    if any(n in commanders for n in tags):
        warn.append("the commander needs no tag (it is always available); remove it from the tags")
    primary = {n: ts[0] for n, ts in tags.items() if ts}
    counts = Counter()
    for name, qty in cards.items():
        counts["land" if is_basic(shown[name]) and name not in primary else primary.get(name, "untagged")] += qty

    # functions, with the commander and the tutors counted as pieces
    functions, covered = {}, set()
    tutors = {front(t): [str(f) for f in fs] for t, fs in (plan.get("tutors") or {}).items()}
    for tutor in tutors:
        if tutor not in cards:
            fail.append(f"tutor not in the list: {tutor}")
    declared = {name: as_function(value) for name, value in (plan.get("functions") or {}).items()}
    for required in gate["required_functions"]:
        if required not in declared:
            fail.append(f"required function {required} is not declared (a way through that board must exist)")
    for fn, info in declared.items():
        if info["needed_by"] not in TIMINGS:
            fail.append(f"function {fn}: needed_by must be one of {list(TIMINGS)}")
            continue
        klass = gate["function_classes"][info["needed_by"]]
        wanted = {front(n) for n in info["cards"]}
        absent = sorted(n for n in wanted if not known(n))
        if absent:
            fail.append(f"function {fn}: not in the list: " + "; ".join(absent))
        pieces = {n: cards[n] for n in wanted if n in cards}
        for tutor, fns in tutors.items():
            if fn in fns and tutor in cards and tutor not in pieces:
                pieces[tutor] = cards[tutor]
        guaranteed = any(n in commanders for n in wanted)
        effective = sum(pieces.values()) + (1 if guaranteed else 0)
        odds = {s: (1.0 if guaranteed else odds_at_least_one(effective, s, library)) for s in gate["seen_report"]}
        functions[fn] = {"pieces": effective, "needed_by": info["needed_by"], "guaranteed": guaranteed, "odds": odds,
                         "judged_at": klass["seen"]}
        covered |= set(pieces) | (wanted & set(cards))
        if effective < klass["min"]:
            fail.append(f"function {fn} ({info['needed_by']}): {effective} pieces (minimum {klass['min']}); "
                        f"add pieces, or drop the function together with the cards that exist for it")

    # win routes
    routes = {}
    for name, value in (plan.get("win_routes") or {}).items():
        spec = value if isinstance(value, dict) else {"cards": value}
        routes[name] = {"cards": {front(c) for c in spec.get("cards") or []}, "axis": spec.get("axis"),
                        "vs_three": str(spec.get("vs_three") or "").strip()}
    if len(routes) < gate["min_win_routes"]:
        fail.append(f"{len(routes)} win routes (minimum {gate['min_win_routes']})")
    for name, route in routes.items():
        if not route["cards"]:
            fail.append(f"win route {name!r} names no card")
        absent = sorted(n for n in route["cards"] if not known(n))
        if absent:
            fail.append(f"win route {name!r}: not in the list: " + "; ".join(absent))
        if route["axis"] not in AXES:
            fail.append(f"win route {name!r}: axis must be one of {list(AXES)}")
        if not route["vs_three"]:
            fail.append(f"win route {name!r}: say how it beats three opponents, not one")
        covered |= route["cards"] & set(cards)
    if routes and all(r["axis"] == "combat" for r in routes.values()):
        fail.append("every win route needs combat damage: one route must not (noncombat or alternate)")
    names = list(routes)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            shared = sorted(routes[a]["cards"] & routes[b]["cards"])
            if shared:
                fail.append(f"win routes {a!r} and {b!r} are not independent: they share " + "; ".join(shared))

    # orphans: declared, plus every plan card that serves no function and no route
    covered |= set(tutors)
    declared_orphans = sorted(shown[n] for n in cards if "orphan" in tags.get(n, []))
    uncovered = sorted(shown[n] for n in cards if primary.get(n) in PLAN_TAGS and n not in covered)
    orphans = sorted(set(declared_orphans) | set(uncovered))
    if len(orphans) > gate["max_orphans"]:
        fail.append(f"{len(orphans)} orphan cards (maximum {gate['max_orphans']}): " + "; ".join(orphans)
                    + (f" (of them {len(uncovered)} are plan cards in no function and no route)" if uncovered else ""))

    # base health and timing
    for tag, minimum in gate["base_min"].items():
        if counts[tag] < minimum:
            warn.append(f"base: {counts[tag]} {tag} cards, the templates ask for {minimum} or more")
    low, high = gate["land_band"]
    if not low <= counts["land"] <= high:
        warn.append(f"base: {counts['land']} lands, the templates ask for {low} to {high}")
    bad_when = {front(n): v for n, v in (plan.get("bad_when_drawn") or {}).items()}
    wrong = sorted(n for n, v in bad_when.items() if v not in BAD_WHEN)
    if wrong:
        fail.append(f"bad_when_drawn must be one of {list(BAD_WHEN)}: " + "; ".join(wrong))
    if len(bad_when) > gate["max_bad_when_drawn"]:
        warn.append(f"{len(bad_when)} cards are bad when drawn at some point (maximum {gate['max_bad_when_drawn']}): "
                    "cut some or add what they need")
    nonland = library - counts["land"]
    plan_cards = sum(counts[t] for t in PLAN_TAGS)
    return {"fail": fail, "warn": warn, "tags": counts, "functions": functions,
            "routes": {k: {"cards": sorted(v["cards"]), "axis": v["axis"], "vs_three": v["vs_three"]} for k, v in routes.items()},
            "orphans": orphans, "uncovered": uncovered, "library": library, "plan_share": (plan_cards, nonland),
            "bad_when_drawn": dict(Counter(bad_when.values()))}


def report_markdown(slug, plan, result, gate=GATE):
    status = "FAIL" if result["fail"] else "PASS"
    lines = [f"# Consistency gate: {slug} ({status})", "",
             f"Plan: {plan.get('plan') or '(none)'}", f"Backup: {plan.get('backup') or '(none)'}", "",
             "## Failures", ""] + ([f"- {f}" for f in result["fail"]] or ["- none"]) + ["", "## Warnings", ""]
    lines += [f"- {w}" for w in result["warn"]] or ["- none"]
    seen = gate["seen_report"]
    lines += ["", "## Functions", "", "Pieces count the commander (guaranteed) and the tutors that can fetch for the function.", "",
              "| Function | Needed by | Pieces | " + " | ".join(f"P(1+ in {s} cards)" for s in seen) + " |",
              "|---|---|---|" + "---|" * len(seen)]
    for fn, info in result["functions"].items():
        lines.append(f"| {fn} | {info['needed_by']} (judged at {info['judged_at']} cards) | {info['pieces']} | "
                     + " | ".join(f"{info['odds'][s]:.0%}" for s in seen) + " |")
    plan_cards, nonland = result["plan_share"]
    lines += ["", "## Tags", ""]
    if nonland:
        lines += [f"Plan cards (engine, payoff, backup): {plan_cards} of {nonland} non-land cards ({plan_cards / nonland:.0%}). "
                  f"Plan cards in no function and no route: {len(result['uncovered'])}"
                  + (f" ({'; '.join(result['uncovered'])})" if result["uncovered"] else "") + ".", ""]
    lines += ["| Tag | Cards |", "|---|---|"] + [f"| {tag} | {n} |" for tag, n in sorted(result["tags"].items())]
    lines += ["", "## Win routes", ""]
    for name, route in result["routes"].items():
        lines.append(f"- {name} ({route['axis']}): {', '.join(route['cards'])}. Against three opponents: {route['vs_three'] or '(missing)'}")
    if result["bad_when_drawn"]:
        lines += ["", f"Cards bad when drawn: {result['bad_when_drawn']}"]
    return "\n".join(lines) + "\n"


def run_plan(plan_path, reports_dir=REPORTS_DIR):
    """Check one plan file against the decklist next to it; write the report; return (slug, result)."""
    plan_path = Path(plan_path)
    slug = plan_path.name[: -len(".plan.json")]
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    cards, shown, commanders, library = read_list(plan_path.with_name(slug + ".txt"))
    result = check(cards, shown, commanders, library, plan)
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / f"consistency-{slug}.md").write_text(report_markdown(slug, plan, result), encoding="utf-8")
    return slug, result


def main():
    plans = sorted(PLANS_DIR.glob("*.plan.json"))
    if not plans:
        print("No decks/phase2/<slug>.plan.json yet: the deck builder writes one with each list.")
        return
    for path in plans:
        slug, result = run_plan(path)
        print(f"{slug}: {'FAIL' if result['fail'] else 'PASS'} ({len(result['fail'])} failures, {len(result['warn'])} warnings)")
        for line in result["fail"]:
            print("  FAIL", line)


if __name__ == "__main__":
    main()
