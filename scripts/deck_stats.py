#!/usr/bin/env python3
"""Phase 8 step 5: statistics of the measured lists (ManaBox-style charts and Commander Salt insights) for the dashboard.

Run it with the "Run Python File" button (no arguments, no network). It reads every list of `decks/measured/<deck>/*.txt`
(the exact 100-card lists scored on Commander Salt, hash-checked against `decks/proposals/measured.json`), the card facts of
the newest Scryfall bulk in `data/cache/` and the Salt numbers of `measured.json`, and writes row files into
`data/model/dashboard/`:

  liststats.json   one row per list: cost, power, Salt, Manabase Quality, average mana value, lands, tapped lands, roles
                   (ramp, draw, removal, counterspells, sweepers, tutors, protection), Salt's ceiling and pillars
  mv.json          mana value curve by color group (nonland cards, the commander included, as ManaBox shows it)
  pips.json        colored mana symbols in the mana costs, per color
  production.json  cards that make each color, lands apart from the rest (restricted to the commander's colors)
  types.json       card types (a card counts once per type)
  subtypes.json    the ten most common creature types
  odds.json        chance of having at least one source of each color among the cards seen by turn 3, 5 and 7 (on the
                   play, 99-card library), and of having every color of the deck at once

The role counts read the rules text, so they are heuristics: they rank lists against each other, they are not a rules check.
"""
import gzip
import json
import math
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEASURED_JSON = ROOT / "decks" / "proposals" / "measured.json"
LISTS_DIR = ROOT / "decks" / "measured"
CACHE = ROOT / "data" / "cache"
OUT_DIR = ROOT / "data" / "model" / "dashboard"
COLORS = ["W", "U", "B", "R", "G"]
COLOR_NAME = {"W": "White", "U": "Blue", "B": "Black", "R": "Red", "G": "Green", "C": "Colorless", "M": "Multicolor"}
SHORT = {"ezio-auditore-da-firenze": "ezio", "fire-lord-azula": "azula", "toph-the-first-metalbender": "toph",
         "alexios-deimos-of-kosmos": "alexios"}
DECK_NAME = {"ezio": "Ezio", "azula": "Azula", "toph": "Toph", "alexios": "Alexios"}
VARIANT_NAME = {"bcore": "black-core"}
TYPES = ["Creature", "Instant", "Sorcery", "Enchantment", "Artifact", "Planeswalker", "Land", "Battle"]
TURNS = [3, 5, 7]
SAMPLES = 6000
FACE_FIELDS = ("mana_cost", "colors", "type_line", "oracle_text")
SKIP_LAYOUTS = {"art_series", "token", "double_faced_token", "emblem", "vanguard", "scheme", "planar"}  # same names, not the cards


def front(name):
    return name.split(" // ")[0].strip()


def parse_list(text):
    """([commander names], [(quantity, name)]) of a list in our `// Commander` / `// Main` format."""
    commanders, entries, section = [], [], None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("//"):
            section = line[2:].strip().lower()
            continue
        match = re.match(r"^(\d+)\s+(.+?)\s*$", line)
        if not match:
            continue
        qty, name = int(match.group(1)), front(match.group(2))
        (commanders if section == "commander" else entries).append(name if section == "commander" else (qty, name))
    return commanders, entries


def load_cards(names):
    """{lower front-face name: card facts} for the wanted names, read from the newest Scryfall oracle bulk."""
    path = sorted(CACHE.glob("oracle-cards-*.jsonl.gz"))[-1]
    wanted, cards = {n.lower() for n in names}, {}
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            obj = json.loads(line)
            key = front(obj["name"]).lower()
            if key not in wanted or key in cards or obj.get("layout") in SKIP_LAYOUTS:
                continue
            face = (obj.get("card_faces") or [{}])[0]
            card = {"name": front(obj["name"]), "cmc": obj.get("cmc", 0.0), "produced_mana": obj.get("produced_mana") or [],
                    "color_identity": obj.get("color_identity") or []}
            for field in FACE_FIELDS:
                value = obj.get(field)
                card[field] = value if value not in (None, "") else face.get(field, "")
            cards[key] = card
    return cards


def type_set(card):
    head = card["type_line"].split(" // ")[0].split("—")[0]
    return {t for t in TYPES if t in head}


def subtypes(card):
    parts = card["type_line"].split(" // ")[0].split("—")
    return parts[1].split() if len(parts) > 1 and "Creature" in parts[0] else []


def pip_colors(mana_cost):
    """Colors of each mana symbol of a cost; a hybrid or Phyrexian symbol counts once for each color it shows."""
    out = []
    for symbol in re.findall(r"\{([^}]+)\}", mana_cost or ""):
        out += [c for c in COLORS if c in symbol.split("/")]
    return out


def land_entry(card):
    """tapped, conditional or untapped, read from the rules text of a land."""
    text = card["oracle_text"].lower()
    for sentence in re.split(r"[.\n]", text):
        if "tapped" in sentence and "enters" in sentence:
            return "conditional" if re.search(r"unless|if you|you may pay|if a player|if an opponent", sentence) else "tapped"
    return "untapped"


def roles(card):
    text = card["oracle_text"].lower()
    nonland = "Land" not in type_set(card)
    found = set()
    if nonland and (card["produced_mana"] or re.search(r"search your library for (a|up to \w+) (basic )?(land|\w+) cards?[^.]*onto the battlefield", text)
                    or re.search(r"search your library for (a|up to \w+) basic land", text)):
        found.add("ramp")
    if re.search(r"\bdraws? (a|two|three|four|\d+|x) cards?\b|\bdraw a card\b", text):
        found.add("draw")
    if re.search(r"(destroy|exile) target|deals? (\d+|x) damage to (any target|target)|target creature gets -\d", text):
        found.add("removal")
    if re.search(r"counter target", text):
        found.add("counter")
    if re.search(r"(destroy|exile) all|each creature|all creatures", text):
        found.add("sweeper")
    if re.search(r"search your library for", text) and not re.search(r"search your library for (a|up to \w+) (basic )?(\w+ )?lands?\b|search your library for (a|an|up to \w+) (basic )?\w+ card[^.]*(basic land|land card)", text):
        found.add("tutor")
    if re.search(r"hexproof|indestructible|protection from", text):
        found.add("protection")
    return found


def hypergeom_at_least_one(population, successes, draws):
    if successes <= 0:
        return 0.0
    if draws >= population:
        return 1.0
    return 1.0 - math.comb(population - successes, draws) / math.comb(population, draws)


def compute(commanders, entries, cards, seed=7):
    """Statistics of one list. `cards` maps lower front-face names to card facts (see load_cards)."""
    deck = [(qty, cards[name.lower()]) for qty, name in entries]
    cmd = [cards[name.lower()] for name in commanders]
    identity = sorted({c for card in cmd for c in card["color_identity"]}, key=COLORS.index)
    everything = [(1, card) for card in cmd] + deck
    nonland = [(q, c) for q, c in everything if "Land" not in type_set(c)]
    lands = [(q, c) for q, c in everything if "Land" in type_set(c)]
    curve = {}
    for qty, card in nonland:
        colors = [c for c in card["colors"] if c in COLORS] if isinstance(card["colors"], list) else []
        group = "C" if not colors else (colors[0] if len(colors) == 1 else "M")
        bucket = "7+" if card["cmc"] >= 7 else str(int(card["cmc"]))
        curve[(bucket, group)] = curve.get((bucket, group), 0) + qty
    pips = {c: 0 for c in COLORS}
    for qty, card in nonland:
        for color in pip_colors(card["mana_cost"]):
            pips[color] += qty
    production = {c: {"lands": 0, "other": 0} for c in COLORS + ["C"]}
    sources = []  # (quantity, mask) of the cards of the 99 that make mana of the deck's colors
    for qty, card in deck:
        made = [c for c in card["produced_mana"] if c in identity or c == "C"]
        if not made:
            continue
        kind = "lands" if "Land" in type_set(card) else "other"
        for color in made:
            production[color][kind] += qty
        mask = sum(1 << COLORS.index(c) for c in made if c in COLORS)
        sources += [mask] * qty
    types = {t: 0 for t in TYPES}
    subs = {}
    for qty, card in everything:
        for t in type_set(card):
            types[t] += qty
        for s in subtypes(card):
            subs[s] = subs.get(s, 0) + qty
    role_counts = {r: 0 for r in ["ramp", "draw", "removal", "counter", "sweeper", "tutor", "protection"]}
    for qty, card in deck:
        for r in roles(card):
            role_counts[r] += qty
    tapped = {"tapped": 0, "conditional": 0, "untapped": 0}
    for qty, card in lands:
        tapped[land_entry(card)] += qty
    total_mv = sum(q * c["cmc"] for q, c in nonland)
    population = sum(q for q, _ in deck)
    needed = [c for c in identity if pips[c] > 0]
    odds = []
    rng = random.Random(seed)
    library = [0] * (population - len(sources)) + sources
    need_mask = sum(1 << COLORS.index(c) for c in needed)
    for turn in TURNS:
        draws = min(7 + turn - 1, population)
        for color in identity:
            k = sum(1 for m in sources if m & (1 << COLORS.index(color)))
            odds.append({"color": color, "turn": turn, "chance": hypergeom_at_least_one(population, k, draws)})
        hits = 0
        for _ in range(SAMPLES):
            seen = 0
            for m in rng.sample(library, draws):
                seen |= m
            hits += (seen & need_mask) == need_mask
        odds.append({"color": "all", "turn": turn, "chance": hits / SAMPLES})
    return {"identity": identity, "curve": curve, "pips": pips, "production": production, "types": types, "subtypes": subs,
            "roles": role_counts, "tapped": tapped,
            "avg_mv": round(total_mv / max(sum(q for q, _ in nonland), 1), 2),
            "lands": sum(q for q, _ in lands), "nonland": sum(q for q, _ in nonland), "odds": odds}


def rows_for(deck_short, label, stats, meta):
    step = int(label.rsplit("step", 1)[1].split("-")[0])
    parts = label.split("-")
    variant = parts[1] if len(parts) == 3 else ""  # 'round4-bcore-step26' is a variant list of the deck
    round_no = int(parts[0].replace("round", ""))
    list_id = f"{deck_short}{'-' + variant if variant else ''}-r{round_no}-{step}"
    deck = DECK_NAME[deck_short] + (f" {VARIANT_NAME.get(variant, variant)}" if variant else "")
    out = {"mv": [], "pips": [], "production": [], "types": [], "subtypes": [], "odds": []}
    for (bucket, group), count in sorted(stats["curve"].items()):
        out["mv"].append({"id": f"{list_id}-{bucket}-{group}", "list_id": list_id, "deck": deck, "mv": bucket,
                          "color": COLOR_NAME[group], "count": count})
    total_pips = sum(stats["pips"].values()) or 1
    for color, count in stats["pips"].items():
        if color in stats["identity"]:
            out["pips"].append({"id": f"{list_id}-{color}", "list_id": list_id, "deck": deck, "color": COLOR_NAME[color],
                                "pips": count, "share_pct": round(100 * count / total_pips)})
    for color, kinds in stats["production"].items():
        if color in stats["identity"] or color == "C":
            out["production"].append({"id": f"{list_id}-{color}", "list_id": list_id, "deck": deck, "color": COLOR_NAME[color],
                                      "lands": kinds["lands"], "other": kinds["other"], "total": kinds["lands"] + kinds["other"]})
    for kind, count in stats["types"].items():
        if count:
            out["types"].append({"id": f"{list_id}-{kind}", "list_id": list_id, "deck": deck, "type": kind, "count": count})
    for sub, count in sorted(stats["subtypes"].items(), key=lambda kv: (-kv[1], kv[0]))[:10]:
        out["subtypes"].append({"id": f"{list_id}-{sub}", "list_id": list_id, "deck": deck, "subtype": sub, "count": count})
    for item in stats["odds"]:
        name = "All colors" if item["color"] == "all" else COLOR_NAME[item["color"]]
        out["odds"].append({"id": f"{list_id}-{item['color']}-{item['turn']}", "list_id": list_id, "deck": deck, "color": name,
                            "turn": item["turn"], "chance_pct": round(100 * item["chance"])})
    pillars = meta.get("salt_pillars") or {}
    row = {"id": list_id, "deck": deck, "list": f"R{round_no} step {step}", "label": label, "wotc_bracket": meta.get("wotc_bracket"), "bracket": meta.get("bracket"),
           "cost_clp": meta["cost_clp"], "power": meta["power"], "salt": meta.get("salt"),
           "manabase_pct": meta.get("manabase_quality_pct"), "avg_mv": stats["avg_mv"], "lands": stats["lands"],
           "nonland": stats["nonland"], "tapped_lands": stats["tapped"]["tapped"],
           "conditional_lands": stats["tapped"]["conditional"], "colors": len(stats["identity"]),
           "ceiling_pts": meta.get("salt_ceiling_pts"), "ceiling": meta.get("salt_ceiling"),
           "consistency": pillars.get("consistency"), "efficiency": pillars.get("efficiency"),
           "interaction": pillars.get("interaction"), "wincons": pillars.get("wincons"), **stats["roles"]}
    return list_id, row, out


def main():
    measured = json.loads(MEASURED_JSON.read_text(encoding="utf-8"))["lists"]
    parsed = {}
    names = set()
    for path in sorted(LISTS_DIR.glob("*/*.txt")):
        commanders, entries = parse_list(path.read_text(encoding="utf-8"))
        parsed[(path.parent.name, path.stem)] = (commanders, entries)
        names |= set(commanders) | {n for _, n in entries}
    cards = load_cards(names)
    missing = sorted(n for n in names if n.lower() not in cards)
    if missing:
        print(f"Cards not found in the Scryfall bulk ({len(missing)}): {missing[:10]}")
    liststats, files = [], {k: [] for k in ("mv", "pips", "production", "types", "subtypes", "odds")}
    for (slug, label), (commanders, entries) in sorted(parsed.items()):
        meta = measured.get(f"{slug}/{label}")
        if meta is None or meta.get("power") is None:
            print(f"No measured entry for {slug}/{label}: skipped")
            continue
        if any(n.lower() not in cards for n in commanders) or any(n.lower() not in cards for _, n in entries):
            print(f"{slug}/{label}: skipped (cards missing)")
            continue
        stats = compute(commanders, entries, cards)
        _, row, out = rows_for(SHORT[slug], label, stats, meta)
        liststats.append(row)
        for key in files:
            files[key] += out[key]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    files["liststats"] = liststats
    for name, rows in files.items():
        (OUT_DIR / f"{name}.json").write_text(json.dumps({"rows": rows}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"{name}.json: {len(rows)} rows")
    print(f"Wrote {OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
