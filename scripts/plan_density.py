#!/usr/bin/env python3
"""Phase 2 consistency gate (owner, 2026-10-30; revised after the Opus review of 2026-10-31).

Does a list have ONE plan with enough pieces of every function it relies on, and a way through the boards a 3 to 4 player pod
produces? Run it with the "Run Python File" button (no arguments). No network. For every `decks/phase2/<slug>.plan.json` it
reads the decklist `decks/phase2/<slug>.txt` next to it and writes `decks/reports/consistency-<slug>.md`.

The plan file is written by the deck builder from the Oracle texts and attacked by a reviewer (docs/research/
phase2-gate-review-20261031.md):
  {"plan": "one sentence", "backup": "one sentence or empty",
   "archetype": "slug of .claude/skills/commander-deckbuilding/archetypes.json, or 'custom'", "secondary": "optional slug",
   "secondary_role": "plan|modifier", "commander_dependence": "engine|attack_engine|enabler|value", "commander_mv": 4,
   "win_routes": {"route": {"cards": [...], "axis": "combat|noncombat|alternate", "vs_three": "how it beats 3 opponents"}},
   "functions": {"name": {"cards": [...], "needed_by": "early|late"}, "other": [cards]},   # a bare list means early
   "support": {"profile support line": [cards]},          # reported against the profile, WARN when under its minimum
   "tutors": {"tutor card": ["function it can fetch for", ...]},   # each tutor must also carry the tag "tutor"
   "tags": {"card": "engine|payoff|backup|ramp|draw|removal|wipe|tutor|protection|land|orphan"  # or ["primary", "second"]},
   "bad_when_drawn": {"card": "early|late|never"}}
Basic lands need no tag. The commander needs none and counts as a guaranteed piece of any function that lists it; the report
also gives the pieces and odds without it. The two functions in GATE["required_functions"] (a way through a wide board of
small blockers and through bigger creatures) must be declared and are always judged early. FAIL means the list is not ready
for Commander Salt; WARN is a reminder. Thresholds: the 8x8 package size and the base counts are sourced
(docs/research/phase2-consistency-survey-20261031.md), the rest is judgment and marked in GATE.

Archetype profiles (revision of 2026-11-01): the plan names its archetype in archetypes.json and the gate applies THAT
profile instead of one template. Every `gate` function of the profile must be declared with at least the larger of the
class minimum (10 early, 6 late) and the profile minimum; `needed_by` may be later than the profile says only through the
profile's own commander alternative (the commander is the payoff or the source); the land band and the five base floors
(ramp, draw, removal, wipe, protection) are the profile's, protection follows `commander_dependence`, ramp rises by 2 for a
commander of mana value 4 or more. `support` lines are reported, never failed. A hybrid takes the higher minimum of every
shared function and the overlap of the land bands (SKILL.md, archetypes.json meta.hybrid). `custom` keeps the generic
GATE floors below and asks the reviewer to check the profile by hand.
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
ARCHETYPES_PATH = ROOT / ".claude" / "skills" / "commander-deckbuilding" / "archetypes.json"
PLANS_DIR = ROOT / "decks" / "phase2"
REPORTS_DIR = ROOT / "decks" / "reports"
TAGS = ("engine", "payoff", "backup", "ramp", "draw", "removal", "wipe", "tutor", "protection", "land", "orphan")
PLAN_TAGS = ("engine", "payoff", "backup")
AXES = ("combat", "noncombat", "alternate")
TIMINGS = ("early", "late")
BAD_WHEN = ("early", "late", "never")  # "never" is allowed in the file but is not counted: only early and late are bad
BASE_TAGS = ("ramp", "draw", "removal", "wipe", "protection")
SECONDARY_ROLES = ("plan", "modifier")
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


def load_archetypes(path=ARCHETYPES_PATH):
    """(archetypes by slug, meta) from archetypes.json, or ({}, {}) when the file is missing."""
    path = Path(path)
    if not path.exists():
        return {}, {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("archetypes") or {}, data.get("meta") or {}


def profile_function(spec):
    """The enforced part of a profile function: min, tier, needed_by and the commander alternative (or None)."""
    alt = spec.get("if_commander_is_payoff") or spec.get("if_commander_is_source")
    return {"min": spec["min"], "tier": spec["tier"], "needed_by": spec["needed_by"], "alt": alt}


def resolve_profile(archetypes, name, secondary=None, role="plan"):
    """One profile from a primary archetype and an optional secondary (archetypes.json meta.hybrid).

    The land band is the primary's, or the overlap when the bands overlap; shared functions and base floors take the higher
    minimum; secondary-only functions keep their minimum, except a secondary that is only a modifier, whose functions become
    support lines (with the profile's `if_secondary_modifier` numbers when it has them). A function with a `unit` is not a
    card count and is not enforced."""
    first = archetypes[name]
    profile = {"name": name, "secondary": secondary, "land_band": tuple(first["land_band"]),
               "base": {t: first["base"][t]["min"] for t in BASE_TAGS},
               "functions": {n: profile_function(f) for n, f in first["functions"].items() if "unit" not in f}}
    if secondary:
        other = archetypes[secondary]
        low, high = max(profile["land_band"][0], other["land_band"][0]), min(profile["land_band"][1], other["land_band"][1])
        if low <= high:
            profile["land_band"] = (low, high)
        for tag in BASE_TAGS:
            profile["base"][tag] = max(profile["base"][tag], other["base"][tag]["min"])
        for n, f in other["functions"].items():
            if "unit" in f:
                continue
            if n in profile["functions"]:
                mine = profile["functions"][n]
                mine["min"] = max(mine["min"], f["min"])
                mine["alt"] = mine["alt"] or profile_function(f)["alt"]
                if f["tier"] == "gate":
                    mine["tier"] = "gate"
            else:
                added = profile_function(f)
                if role == "modifier":
                    added["tier"] = "support"
                    added["min"] = (f.get("if_secondary_modifier") or {}).get("min", added["min"])
                profile["functions"][n] = added
    return profile


def check(cards, shown, commanders, library, plan, gate=GATE, archetypes=None, meta=None):
    """The gate result: fail and warn lists, tag counts, functions, routes, orphans and the plan share.

    `archetypes` and `meta` default to archetypes.json."""
    if archetypes is None:
        archetypes, meta = load_archetypes()
    meta = meta or {}
    fail, warn = [], []
    if not str(plan.get("plan") or "").strip():
        fail.append("no primary plan declared")
    if not str(plan.get("backup") or "").strip():
        warn.append("no backup plan declared (allowed, but say so on purpose)")

    def known(name):
        return name in cards or name in commanders

    # the archetype profile: land band, base floors and the functions the plan must declare
    profile, base_min, land_band = None, dict(gate["base_min"]), gate["land_band"]
    name, secondary = plan.get("archetype"), plan.get("secondary")
    role = plan.get("secondary_role") or "plan"
    if not name:
        fail.append("no archetype declared: name one of archetypes.json, or 'custom' (a deck with no profile is judged by the "
                    "generic template, which does not fit every commander)")
    elif name == "custom":
        warn.append("archetype 'custom': the generic floors apply; the reviewer checks the profile by hand")
    elif name not in archetypes:
        fail.append(f"unknown archetype {name!r}; use one of {sorted(archetypes)} or 'custom'")
    elif secondary and secondary not in archetypes:
        fail.append(f"unknown secondary archetype {secondary!r}")
    elif role not in SECONDARY_ROLES:
        fail.append(f"secondary_role must be one of {list(SECONDARY_ROLES)}")
    else:
        profile = resolve_profile(archetypes, name, secondary, role)
        base_min, land_band = dict(profile["base"]), profile["land_band"]
    dependence = plan.get("commander_dependence")
    if dependence:
        classes = {k: v for k, v in (meta.get("commander_dependence") or {}).items() if isinstance(v, dict) and "min" in v}
        if dependence in classes:
            base_min["protection"] = classes[dependence]["min"]  # the class of the real commander overrides the profile
        else:
            fail.append(f"commander_dependence must be one of {list(classes)}")
    if int(plan.get("commander_mv") or 0) >= 4:
        base_min["ramp"] += 2  # meta.ramp_commander_rule

    # tags: one primary tag per card, a second one allowed
    tags = {}
    for tag_name, value in (plan.get("tags") or {}).items():
        tags[front(tag_name)] = [value] if isinstance(value, str) else list(value)
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
    counts, base_counts = Counter(), Counter()
    for card_name, qty in cards.items():
        counts["land" if is_basic(shown[card_name]) and card_name not in primary else primary.get(card_name, "untagged")] += qty
        for tag in set(tags.get(card_name, [])) & set(BASE_TAGS):
            base_counts[tag] += qty  # a multi-role card counts in every base function it is tagged for

    # functions, with the commander and the tutors counted as pieces
    functions, covered = {}, set()
    tutors = {front(t): [str(f) for f in fs] for t, fs in (plan.get("tutors") or {}).items()}
    for tutor in tutors:
        if tutor not in cards:
            fail.append(f"tutor not in the list: {tutor}")
        elif "tutor" not in tags.get(tutor, []):
            fail.append(f"tutor {shown[tutor]} must carry the tag 'tutor' (a tutor is a card that searches, not any card named here)")
    declared = {fn: as_function(value) for fn, value in (plan.get("functions") or {}).items()}
    for required in gate["required_functions"]:
        if required not in declared:
            fail.append(f"required function {required} is not declared (a way through that board must exist)")
    pfuncs = profile["functions"] if profile else {}
    for fn, spec in pfuncs.items():
        if spec["tier"] == "gate" and fn not in declared and fn not in gate["required_functions"]:
            fail.append(f"profile function {fn} (gate, minimum {spec['min']}) is not declared in the plan; declare it with its "
                        f"cards, or drop it together with the cards that exist for it")
    for fn, info in declared.items():
        if info["needed_by"] not in TIMINGS:
            fail.append(f"function {fn}: needed_by must be one of {list(TIMINGS)}")
            continue
        wanted = {front(n) for n in info["cards"]}
        guaranteed = any(n in commanders for n in wanted)
        timing, profile_min = info["needed_by"], 0
        if fn in gate["required_functions"] and timing != "early":
            fail.append(f"function {fn}: the reference boards are judged early (needed_by early, not {timing})")
            timing = "early"
        spec = pfuncs.get(fn)
        if spec and spec["tier"] == "gate":
            profile_min, expected = spec["min"], spec["needed_by"]
            if spec["alt"] and guaranteed:  # the commander is the payoff or the source: the others are backups
                profile_min, expected = spec["alt"]["min"], spec["alt"]["needed_by"]
            if expected == "early" and timing == "late":
                fail.append(f"function {fn}: the {profile['name']} profile needs it early (needed_by early, not late)")
                timing = "early"
        klass = gate["function_classes"][timing]
        required = max(klass["min"], profile_min)
        absent = sorted(n for n in wanted if not known(n))
        if absent:
            fail.append(f"function {fn}: not in the list: " + "; ".join(absent))
        pieces = {n: cards[n] for n in wanted if n in cards}
        for tutor, fns in tutors.items():
            if fn in fns and tutor in cards and "tutor" in tags.get(tutor, []) and tutor not in pieces:
                pieces[tutor] = cards[tutor]
        without = sum(pieces.values())
        effective = without + (1 if guaranteed else 0)
        odds = {s: (1.0 if guaranteed else odds_at_least_one(effective, s, library)) for s in gate["seen_report"]}
        odds_without = {s: odds_at_least_one(without, s, library) for s in gate["seen_report"]}
        functions[fn] = {"pieces": effective, "without_commander": without, "needed_by": timing, "guaranteed": guaranteed,
                         "odds": odds, "odds_without": odds_without, "judged_at": klass["seen"], "required": required}
        covered |= set(pieces) | (wanted & set(cards))
        if effective < required:
            note = f", the {profile['name']} profile asks {profile_min}" if profile_min > klass["min"] else ""
            fail.append(f"function {fn} ({timing}): {effective} pieces (minimum {required}){note}; "
                        f"add pieces, or drop the function together with the cards that exist for it")
        elif guaranteed and without < required:
            warn.append(f"function {fn}: reaches its minimum of {required} only with the commander ({without} pieces without "
                        f"it); if the commander is removed the function fails")

    # support lines of the profile: reported against its minimum, never failed
    support = {}
    for fn, spec in pfuncs.items():
        if spec["tier"] != "support" or fn in declared:
            continue
        value = (plan.get("support") or {}).get(fn)
        wanted = {front(n) for n in (value.get("cards") if isinstance(value, dict) else value) or []}
        absent = sorted(n for n in wanted if not known(n))
        if absent:
            fail.append(f"support line {fn}: not in the list: " + "; ".join(absent))
        pieces = sum(cards[n] for n in wanted if n in cards)
        support[fn] = {"pieces": pieces, "min": spec["min"], "reported": value is not None}
        covered |= wanted & set(cards)
        if value is None:
            warn.append(f"support line {fn} (profile minimum {spec['min']}) is not reported in the plan 'support' block")
        elif pieces < spec["min"]:
            warn.append(f"support line {fn}: {pieces} pieces, the {profile['name']} profile asks {spec['min']}; write the reason "
                        f"in the profile table or promote the line to a declared function")

    # win routes
    routes = {}
    for route_name, value in (plan.get("win_routes") or {}).items():
        spec = value if isinstance(value, dict) else {"cards": value}
        routes[route_name] = {"cards": {front(c) for c in spec.get("cards") or []}, "axis": spec.get("axis"),
                              "vs_three": str(spec.get("vs_three") or "").strip()}
    if len(routes) < gate["min_win_routes"]:
        fail.append(f"{len(routes)} win routes (minimum {gate['min_win_routes']})")
    for route_name, route in routes.items():
        if not route["cards"]:
            fail.append(f"win route {route_name!r} names no card")
        absent = sorted(n for n in route["cards"] if not known(n))
        if absent:
            fail.append(f"win route {route_name!r}: not in the list: " + "; ".join(absent))
        if route["axis"] not in AXES:
            fail.append(f"win route {route_name!r}: axis must be one of {list(AXES)}")
        if not route["vs_three"]:
            fail.append(f"win route {route_name!r}: say how it beats three opponents, not one")
        in_list = sum(cards[n] for n in route["cards"] if n in cards)
        if route["cards"] and in_list < 2 and not route["cards"] & commanders:
            warn.append(f"win route {route_name!r} rests on a single card: one removal spell turns the route off")
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
    source = f"the {profile['name']} profile" if profile else "the templates"
    for tag, minimum in base_min.items():
        if base_counts[tag] < minimum:
            warn.append(f"base: {base_counts[tag]} {tag} cards, {source} asks for {minimum} or more")
    low, high = land_band
    if not low <= counts["land"] <= high:
        warn.append(f"base: {counts['land']} lands, {source} asks for {low} to {high}")
    bad_when = {front(n): v for n, v in (plan.get("bad_when_drawn") or {}).items()}
    wrong = sorted(n for n, v in bad_when.items() if v not in BAD_WHEN)
    if wrong:
        fail.append(f"bad_when_drawn must be one of {list(BAD_WHEN)}: " + "; ".join(wrong))
    counted_bad = {n: v for n, v in bad_when.items() if v in ("early", "late")}
    if len(counted_bad) > gate["max_bad_when_drawn"]:
        warn.append(f"{len(counted_bad)} cards are bad when drawn at some point (maximum {gate['max_bad_when_drawn']}): "
                    "cut some or add what they need")
    nonland = library - counts["land"]
    plan_cards = sum(counts[t] for t in PLAN_TAGS)
    return {"fail": fail, "warn": warn, "tags": counts, "base_counts": base_counts, "functions": functions,
            "support": support, "archetype": name, "secondary": secondary,
            "routes": {k: {"cards": sorted(v["cards"]), "axis": v["axis"], "vs_three": v["vs_three"]} for k, v in routes.items()},
            "orphans": orphans, "uncovered": uncovered, "library": library, "plan_share": (plan_cards, nonland),
            "bad_when_drawn": dict(Counter(counted_bad.values()))}


def report_markdown(slug, plan, result, gate=GATE):
    status = "FAIL" if result["fail"] else "PASS"
    archetype = result["archetype"] or "(none)"
    if result["secondary"]:
        archetype += f" + {result['secondary']} ({plan.get('secondary_role') or 'plan'})"
    lines = [f"# Consistency gate: {slug} ({status})", "",
             f"Plan: {plan.get('plan') or '(none)'}", f"Backup: {plan.get('backup') or '(none)'}", f"Archetype: {archetype}", "",
             "## Failures", ""] + ([f"- {f}" for f in result["fail"]] or ["- none"]) + ["", "## Warnings", ""]
    lines += [f"- {w}" for w in result["warn"]] or ["- none"]
    seen = gate["seen_report"]
    lines += ["", "## Functions", "",
              "Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the "
              "commander, and a function the commander guarantees says so.", "",
              "| Function | Needed by | Required | Pieces | Without commander | " + " | ".join(f"P(1+ in {s} cards)" for s in seen) + " |",
              "|---|---|---|---|---|" + "---|" * len(seen)]
    for fn, info in result["functions"].items():
        mark = " (commander guaranteed)" if info["guaranteed"] else ""
        lines.append(f"| {fn} | {info['needed_by']} (judged at {info['judged_at']} cards) | {info['required']} | {info['pieces']} | "
                     f"{info['without_commander']}{mark} | " + " | ".join(f"{info['odds_without'][s]:.0%}" for s in seen) + " |")
    if result["support"]:
        lines += ["", "## Support lines", "", "| Line | Pieces | Profile minimum | Reported |", "|---|---|---|---|"]
        for fn, info in result["support"].items():
            lines.append(f"| {fn} | {info['pieces']} | {info['min']} | {'yes' if info['reported'] else 'no'} |")
    plan_cards, nonland = result["plan_share"]
    lines += ["", "## Tags", ""]
    if nonland:
        lines += [f"Plan cards (engine, payoff, backup): {plan_cards} of {nonland} non-land cards ({plan_cards / nonland:.0%}). "
                  f"Plan cards in no function and no route: {len(result['uncovered'])}"
                  + (f" ({'; '.join(result['uncovered'])})" if result["uncovered"] else "") + ".", ""]
    lines += ["| Tag | Cards (primary tag) |", "|---|---|"] + [f"| {tag} | {n} |" for tag, n in sorted(result["tags"].items())]
    base = result["base_counts"]
    lines += ["", "Base functions, counting second tags too: " + ", ".join(f"{t} {base[t]}" for t in BASE_TAGS) + "."]
    lines += ["", "## Win routes", ""]
    for name, route in result["routes"].items():
        lines.append(f"- {name} ({route['axis']}): {', '.join(route['cards'])}. Against three opponents: {route['vs_three'] or '(missing)'}")
    if result["bad_when_drawn"]:
        lines += ["", f"Cards bad when drawn (early and late only): {result['bad_when_drawn']}"]
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
