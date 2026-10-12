#!/usr/bin/env python3
"""Speed-risk flag: a Monte Carlo goldfish that says how often a deck could threaten lethal
before its own turn 7 (power-scale: qualitative, five levels).

Run it with the "Run Python File" button (no arguments). It needs no network. For every deck
with a decks/<slug>.cards.json (written by scripts/layer_a.py) it plays TRIALS games against
nobody and writes decks/<slug>.speed_risk.json with the level, the simulated frequency and the
model's limits.

The model is deliberately simple and leans fast (it ignores colors, removal, counterspells and
blockers), because the flag feeds a bracket gate: a fast estimate errs on the safe side.
  - Library, 7-card hand, one mulligan if the hand has fewer than 2 or more than 5 lands, one
    draw per turn (turn 1 included, as in multiplayer), one land drop per turn.
  - Mana: lands, mana rocks and mana creatures (summoning sick unless hasty), rituals, land
    ramp, simple draw spells, tutors (they fetch the missing piece of the nearest combo).
  - Damage: creatures hit one opponent for their power the turn after they arrive (or at once
    with haste). A threat is 40 damage to one opponent or 21 commander damage.
  - Combos: every Commander Spellbook variant fully inside the deck whose features win the game
    (win or lose-the-game, infinite damage, infinite turns) is a threat once all its pieces are
    in hand or in play and the mana covers the pieces still to cast and `manaValueNeeded`.
Bands of the simulated frequency (power-scale, user decision 2026-10-11): 0-10% very low,
10-20% low, 20-30% medium, 30-40% high, 40% or more very high. `high` or `very high` fails the
bracket-fit review. The number is an order of magnitude, never an exact percentage.
"""
import json
import random
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402

DECKS = la.DECKS
TRIALS = 20000
SEED = 20261012
HORIZON = 6           # turns the deck gets before its own turn 7
LIFE = 40
COMMANDER_LETHAL = 21
BANDS = [(0.10, "very low"), (0.20, "low"), (0.30, "medium"), (0.40, "high")]
HASTE_LINE = "(^|\n)haste\\b"  # the card's own keyword line, not "has haste" given to others
REQUIRED_FACT_KEYS =("quantity", "role", "power", "keywords", "oracle_id", "mana_value")
NUMBERS = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

TAP_ADD_RE = re.compile(r"\{t\}[^.\n]*?:\s*add ((?:\{[^}]+\}\s*)+)", re.I)
ADD_RE = re.compile(r"\badd ((?:\{[^}]+\}\s*)+)", re.I)
ADD_WORDS_RE = re.compile(r"\badd (one|two|three) mana", re.I)
DRAW_RE = re.compile(r"\bdraws? (a|an|one|two|three|four|five|\d+) cards?", re.I)
ETB_DRAW_RE = re.compile(r"when [^.\n]*enters[^.\n]*, [^.\n]*\bdraw", re.I)
LAND_RAMP_RE = re.compile(
    r"search your library for (?:up to )?(a|an|one|two|three) [^.]*?land cards?[^.]*?onto the battlefield", re.I)
TUTOR_RE = re.compile(r"search your library for (?:a|an|one|up to one) (?![^.]*\blands?\b)[^.]*\bcard", re.I)
DECISIVE_RE = la.DECISIVE_RE


def band(p):
    """The qualitative level of a simulated frequency."""
    for upper, name in BANDS:
        if p < upper:
            return name
    return "very high"


def _count(match):
    return len(re.findall(r"\{[^}]+\}", match.group(1)))


def model_card(fact):
    """Reduce one card-facts entry to the few numbers the goldfish uses."""
    text = fact.get("oracle_text") or ""
    types = fact.get("type_line") or ""
    low = text.lower()
    spell = "Instant" in types or "Sorcery" in types
    card = {
        "name": fact["name"], "oid": fact.get("oracle_id"),
        "cmc": int(fact.get("mana_value") or 0),
        "land": "Land" in types, "creature": "Creature" in types, "spell": spell,
        "power": 0,
        "haste": bool(re.search(HASTE_LINE, low)) or "Haste" in (fact.get("keywords") or []),
        "mana": 0, "tapped": False, "gain": 0, "ramp": 0, "draw": 0, "tutor": False,
    }
    power = fact.get("power")
    if card["creature"] and isinstance(power, str) and power.isdigit():
        card["power"] = int(power)
    if card["land"]:
        match = TAP_ADD_RE.search(text)
        card["mana"] = _count(match) if match else (1 if fact.get("produced_mana") else 0)
        card["tapped"] = ("enters tapped" in low or "enters the battlefield tapped" in low) and "unless" not in low
        return card
    if spell:
        match = ADD_RE.search(text)
        words = ADD_WORDS_RE.search(text)
        if match:
            card["gain"] = _count(match)
        elif words:
            card["gain"] = NUMBERS[words.group(1).lower()]
    else:
        match = TAP_ADD_RE.search(text)
        if match:
            card["mana"] = min(_count(match), 4)
    ramp = LAND_RAMP_RE.search(text)
    if ramp:
        card["ramp"] = NUMBERS.get(ramp.group(1).lower(), 1)
    draw = DRAW_RE.search(text)
    if draw and (spell or ETB_DRAW_RE.search(text)):
        token = draw.group(1).lower()
        card["draw"] = int(token) if token.isdigit() else NUMBERS[token]
    card["tutor"] = bool(TUTOR_RE.search(text)) and not ramp
    return card


def decisive_combos(facts, spellbook):
    """List of (frozenset of oracle IDs, mana value needed) for the winning variants in the deck."""
    if spellbook is None:
        return []
    deck_oids = {f["oracle_id"] for f in facts if f.get("oracle_id")}
    commander_oids = {f["oracle_id"] for f in facts if f.get("role") == "commander"}
    included, _ = la.match_spellbook(spellbook, deck_oids, commander_oids)
    combos = []
    for variant in included:
        if any(DECISIVE_RE.search(name) for name in variant["features"]) and not variant["requires"]:
            combos.append((variant["_oids"], int(variant.get("mana_value_needed") or 0)))
    return combos


def build_deck(facts):
    """Return (library cards, commander card) from a card-facts list with quantities."""
    library, commander = [], None
    for fact in facts:
        card = model_card(fact)
        if fact.get("role") == "commander":
            commander = card
            continue
        library += [card] * int(fact.get("quantity") or 1)
    return library, commander


def play_game(library_cards, commander, combos, rng):
    """One goldfish game. Returns the turn on which a threat appeared, or None."""
    library = list(library_cards)
    rng.shuffle(library)
    hand = [library.pop() for _ in range(min(7, len(library)))]
    lands = sum(c["land"] for c in hand)
    if lands < 2 or lands > 5:  # one mulligan: redraw 7 and bottom one card
        library += hand
        rng.shuffle(library)
        hand = [library.pop() for _ in range(min(7, len(library)))]
        lands = sum(c["land"] for c in hand)
        drop = max((c for c in hand if c["land"]), key=lambda c: 0, default=None) if lands > 3 else \
            max((c for c in hand if not c["land"]), key=lambda c: c["cmc"], default=None)
        if drop is not None:
            hand.remove(drop)
            library.insert(0, drop)

    field = []  # entries: {"card": card, "turn": turn it arrived}
    commander_casts, commander_on_field = 0, None
    damage = commander_damage = 0

    def tutor_target():
        """The library card that completes the combo with most pieces already available."""
        zone = {c["oid"] for c in hand} | {f["card"]["oid"] for f in field}
        if commander is not None:
            zone.add(commander["oid"])
        best, best_have = None, 0
        for pieces, _ in combos:
            have = len(pieces & zone)
            if have > best_have and have < len(pieces):
                missing = pieces - zone
                for card in library:
                    if card["oid"] in missing:
                        best, best_have = card, have
                        break
        return best

    def combo_ready(mana):
        zone = {c["oid"]: c for c in hand}
        for f in field:
            zone[f["card"]["oid"]] = None  # already in play: costs nothing more
        if commander is not None:
            zone[commander["oid"]] = None if commander_on_field else \
                {"cmc": commander["cmc"] + 2 * commander_casts}
        for pieces, needed in combos:
            if all(oid in zone for oid in pieces):
                uncast = sum((zone[oid]["cmc"] if zone[oid] is not None else 0) for oid in pieces)
                if max(needed, uncast) <= mana:
                    return True
        return False

    for turn in range(1, HORIZON + 1):
        if library:
            hand.append(library.pop())
        land = next((c for c in hand if c["land"] and not c["tapped"]), None) or \
            next((c for c in hand if c["land"]), None)
        if land is not None:
            hand.remove(land)
            field.append({"card": land, "turn": turn})

        mana = 0
        for f in field:
            c = f["card"]
            if c["land"]:
                mana += 0 if (c["tapped"] and f["turn"] == turn) else c["mana"]
            elif c["mana"] and (f["turn"] < turn or c["haste"] or not c["creature"]):
                mana += c["mana"]

        guard = 0
        while guard < 30:
            guard += 1
            if combo_ready(mana):
                return turn
            options = []
            for c in hand:
                if c["land"] or c["cmc"] > mana:
                    continue
                if c["gain"] > c["cmc"] or c["mana"] or c["ramp"]:
                    rank = 0
                elif c["draw"]:
                    rank = 1
                elif c["tutor"]:
                    rank = 2
                elif c["creature"] and c["power"] > 0:
                    rank = 3
                else:
                    continue
                order = c["cmc"] if rank < 3 else -c["power"]
                options.append((rank, order, c["cmc"], id(c), c, False))
            if commander is not None and commander_on_field is None:
                cost = commander["cmc"] + 2 * commander_casts
                if cost <= mana and (commander["power"] > 0 or combos):
                    options.append((3, -commander["power"], cost, 0, commander, True))
            if not options:
                break
            options.sort(key=lambda o: o[:4])
            _, _, cost, _, card, is_commander = options[0]
            mana -= cost
            if is_commander:
                commander_casts += 1
                commander_on_field = {"card": card, "turn": turn}
                field.append(commander_on_field)
                continue
            hand.remove(card)
            if card["spell"]:
                mana += card["gain"]
            else:
                field.append({"card": card, "turn": turn})
                if card["mana"] and (card["haste"] or not card["creature"]):
                    mana += card["mana"]
            # Land ramp, draw and tutor work the same whether the card is a spell or a permanent
            # with an enters-the-battlefield effect.
            for _ in range(card["ramp"]):
                found = next((c for c in library if c["land"]), None)
                if found is not None:
                    library.remove(found)
                    field.append({"card": dict(found, tapped=True), "turn": turn})
            for _ in range(card["draw"]):
                if library:
                    hand.append(library.pop())
            if card["tutor"]:
                target = tutor_target()
                if target is not None:
                    library.remove(target)
                    hand.append(target)

        for f in field:
            c = f["card"]
            if c["creature"] and c["power"] > 0 and (f["turn"] < turn or c["haste"]):
                damage += c["power"]
                if commander is not None and c is commander:
                    commander_damage += c["power"]
        if damage >= LIFE or commander_damage >= COMMANDER_LETHAL:
            return turn
    return None


def simulate(facts, spellbook=None, trials=TRIALS, seed=SEED, progress=None):
    """Run the trials. Returns a dict with the per-turn cumulative frequency and the level."""
    library, commander = build_deck(facts)
    combos = decisive_combos(facts, spellbook)
    rng = random.Random(seed)
    by_turn = [0] * (HORIZON + 1)
    started = time.time()
    for i in range(1, trials + 1):
        turn = play_game(library, commander, combos, rng)
        if turn is not None:
            by_turn[turn] += 1
        if progress and i % max(trials // 10, 1) == 0:
            elapsed = time.time() - started
            progress(i, trials, elapsed, elapsed / i * (trials - i))
    cumulative, total = {}, 0
    for turn in range(1, HORIZON + 1):
        total += by_turn[turn]
        cumulative[str(turn)] = round(total / trials, 4)
    p = total / trials
    return {
        "trials": trials, "seed": seed, "horizon_turn": HORIZON,
        "frequency": round(p, 4), "level": band(p),
        "cumulative_by_turn": cumulative,
        "decisive_combos_in_deck": len(combos),
        "library_cards": len(library), "commander": commander["name"] if commander else None,
    }


def main():
    """Simulate every deck with a card-facts file and write its speed-risk file."""
    paths = sorted(DECKS.glob("*.cards.json"))
    if not paths:
        print("No decks/<slug>.cards.json found. Run scripts/layer_a.py first.")
        sys.exit(2)
    spellbook = la.load_spellbook() if la.SPELLBOOK_SLIM.exists() else None
    if spellbook is None:
        print("Spellbook slim file missing: combos are not modelled (run collect_spellbook_bulk.py).")
    for path in paths:
        slug = path.name[: -len(".cards.json")]
        facts = json.loads(path.read_text(encoding="utf-8"))
        missing = [k for k in REQUIRED_FACT_KEYS if not facts or any(k not in f for f in facts)]
        if missing or not any(f.get("role") == "commander" for f in facts):
            print(f"== {slug}: SKIPPED. {path.name} is out of date (missing {missing or ['a commander']}); "
                  "run scripts/layer_a.py again to regenerate it.")
            continue
        print(f"== {slug}: {TRIALS} games ...", flush=True)

        def progress(done, total, elapsed, eta):
            print(f"   {done}/{total} games, {elapsed:.0f} s elapsed, ETA {eta:.0f} s", flush=True)

        result = simulate(facts, spellbook, progress=progress)
        result.update({
            "slug": slug,
            "run_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "fails_bracket_fit_review": result["level"] in ("high", "very high"),
            "note": "Order of magnitude from a simplified goldfish (no colors, removal or blockers). "
                    "It never changes Layer A's floor; it feeds the bracket-fit review.",
        })
        out = DECKS / f"{slug}.speed_risk.json"
        out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"   level: {result['level']} ({result['frequency']:.1%} of games by turn {HORIZON}); "
              f"decisive combos in the deck: {result['decisive_combos_in_deck']}")
        print(f"   cumulative by turn: {result['cumulative_by_turn']}")
        print(f"   wrote decks/{slug}.speed_risk.json\n")


if __name__ == "__main__":
    main()
