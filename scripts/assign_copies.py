#!/usr/bin/env python3
"""Phase 2: give each deck its own physical copies from the collection, and write the pull list.

Run it with the "Run Python File" button (no arguments). No network. It reads
  - data/cache/collection_inventory.json (from scripts/build_inventory.py: every owned copy with its language, printing
    and binder; tokens apart),
  - decks/phase2.json (the 4 decks, the language policy of each and the path of its decklist), and
  - the decklists named there (`decks/phase2/<slug>.txt`, the same text format as decks/<slug>.txt),
and writes data/model/phase2/assignment.json and decks/reports/pull-list-<date>.md.

Rules (owner, 2026-10-26, Phase 2): the collection is the only source (no purchases); a physical copy sits in one
deck (decision D5), so the decks share the collection and a card wanted by two decks needs two copies; a deck with
languages "both" takes the ENGLISH copy when the card is owned in both languages and the Spanish copy when only that
exists (owner rule 2026-10-21); a deck with languages "es" takes Spanish copies only. Decks with a restriction are served
first (the Spanish-only deck keeps its Spanish copies), then the others in the order of the config. Among the copies of
the allowed language the better condition goes first, then the non-foil one. A commander that is a proxy (inventory
`commander_ok`, or a deck marked `proxy_commander` in the config, as Ezio's since the Standard cards are not scanned)
needs no copy. Basic lands come from the same pool, by name. Nothing is hidden: a card the collection
cannot give is listed as missing and a card used by two decks is listed as shared.
"""
import json
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402

ROOT = la.ROOT
INVENTORY_PATH = ROOT / "data" / "cache" / "collection_inventory.json"
CONFIG_PATH = ROOT / "decks" / "phase2.json"
OUT_JSON = ROOT / "data" / "model" / "phase2" / "assignment.json"
REPORTS_DIR = ROOT / "decks" / "reports"
CONDITION_RANK = {"mint": 0, "near_mint": 0, "excellent": 1, "lightly_played": 2, "good": 3, "": 4}
BASIC_NAMES = {"plains", "island", "swamp", "mountain", "forest", "wastes"}


def language_order(policy):
    """The languages a deck may use, best first: "both" is English then Spanish, "es" Spanish only, "en" English only."""
    return {"both": ["en", "es"], "es": ["es"], "en": ["en"]}[policy]


def is_basic(name):
    """True for the basic lands (snow-covered ones included): they are taken by name from the pool."""
    n = la.normalize(name)
    if n.startswith("snow-covered "):
        n = n.split(" ", 1)[1]
    return n in BASIC_NAMES


def supply_by_oid(inventory):
    """{oracle id: {"name", "pool": [printing dicts with a mutable "left"], "commander_ok"}} from the inventory."""
    supply = {}
    for card in inventory["cards"]:
        pool = [dict(p, left=int(p["quantity"])) for p in card["printings"]]
        supply[card["oracle_id"]] = {"name": card["name"], "pool": pool}
    for card in inventory.get("commander_ok", []):
        supply.setdefault(card["oracle_id"], {"name": card["name"], "pool": []})["commander_ok"] = True
    return supply


def pick_order(printing, languages):
    """Sort key: language (best first), then condition, then non-foil, then set and number (a stable order)."""
    return (languages.index(printing["language"]), CONDITION_RANK.get(printing.get("condition", ""), 5),
            printing.get("foil", "normal") not in ("", "normal"), printing.get("set", ""), str(printing.get("number", "")))


def take(entry, qty, languages):
    """Take up to `qty` copies of the allowed languages from one card's pool: [(printing, n)] and the count taken."""
    picks, got = [], 0
    usable = [p for p in entry["pool"] if p["language"] in languages and p["left"] > 0]
    for printing in sorted(usable, key=lambda p: pick_order(p, languages)):
        n = min(qty - got, printing["left"])
        if n:
            printing["left"] -= n
            picks.append((printing, n))
            got += n
        if got == qty:
            break
    return picks, got


def allocate(decks, inventory):
    """Assign copies to the decks. `decks` is [{"slug", "languages", "cards": {oid: (name, qty)}, "commanders": [oid]}].

    Returns {"decks": {slug: {...}}, "shared": [{"name", "decks"}]}; each deck has "cards" (name, qty, picks),
    "missing" (name, needed, given, language_note) and "proxy_commanders"."""
    supply = supply_by_oid(inventory)
    order = sorted(range(len(decks)), key=lambda i: (decks[i]["languages"] == "both", i))  # restricted decks first
    result, users = {}, defaultdict(list)
    for i in order:
        deck = decks[i]
        languages = language_order(deck["languages"])
        out = {"languages": deck["languages"], "cards": [], "missing": [], "proxy_commanders": []}
        for oid, (name, qty) in sorted(deck["cards"].items(), key=lambda kv: kv[1][0].casefold()):
            entry = supply.get(oid, {"name": name, "pool": []})
            picks, got = take(entry, qty, languages)
            if got < qty and oid in deck["commanders"] and (entry.get("commander_ok") or deck.get("proxy_commander")):
                out["proxy_commanders"].append(name)
                got = qty
            if got:
                users[oid].append(deck["slug"])
            out["cards"].append({
                "name": name, "oracle_id": oid, "qty": qty, "given": got,
                "picks": [{"language": p["language"], "set": p.get("set", ""), "number": p.get("number", ""),
                           "foil": p.get("foil", ""), "condition": p.get("condition", ""),
                           "binder": p.get("binder", ""), "qty": n} for p, n in picks]})
            if got < qty:
                owned_other = sum(p["left"] for p in entry["pool"] if p["language"] not in languages)
                note = f"{owned_other} copy(ies) only in a language this deck does not take" if owned_other else ""
                out["missing"].append({"name": name, "needed": qty, "given": got, "note": note})
        result[deck["slug"]] = out
    shared = [{"name": supply.get(oid, {}).get("name") or oid, "decks": sorted(set(slugs))}
              for oid, slugs in users.items() if len(set(slugs)) > 1 and not is_basic(supply.get(oid, {}).get("name", ""))]
    return {"decks": result, "shared": sorted(shared, key=lambda s: s["name"].casefold())}


def read_deck(spec, index, root=ROOT):
    """Read one deck of the config into the shape `allocate` takes; returns (deck, problems)."""
    path = root / spec["list"]
    deck = {"slug": spec["slug"], "languages": spec.get("languages", "both"), "cards": {}, "commanders": [],
            "proxy_commander": bool(spec.get("proxy_commander"))}
    problems = []
    if not path.exists():
        return None, [f"{spec['slug']}: no list yet ({spec['list']})"]
    commanders, main, bad = la.parse_decklist(path.read_text(encoding="utf-8"))
    problems += [f"{spec['slug']}: could not read the line {b!r}" for b in bad]
    for role, entries in (("commander", commanders), ("main", main)):
        for entry in entries:
            card = index.get(la.normalize(entry["name"]))
            if card is None:
                problems.append(f"{spec['slug']}: unknown card {entry['name']!r}")
                continue
            oid = card["oracle_id"]
            name, have = deck["cards"].get(oid, (card["name"], 0))
            deck["cards"][oid] = (name, have + entry["qty"])
            if role == "commander":
                deck["commanders"].append(oid)
    return deck, problems


def pull_list_markdown(config, assignment, sizes, problems, today):
    """The owner's pull list: per deck and per binder, what to take out and where it goes."""
    lines = [f"# Pull list, Phase 2 ({today})", "",
             "One physical copy sits in one deck. Language rule: bilingual decks take the English copy when both exist; "
             "the Spanish-only deck takes Spanish copies only.", ""]
    for p in problems:
        lines.append(f"- PROBLEM: {p}")
    if problems:
        lines.append("")
    by_binder = defaultdict(list)
    for spec in config["decks"]:
        slug = spec["slug"]
        res = assignment["decks"].get(slug)
        if res is None:
            continue
        missing = sum(m["needed"] - m["given"] for m in res["missing"])
        lines += [f"## {spec.get('name', slug)} ({spec['languages']}): {sizes.get(slug, 0)} cards, {missing} not covered", ""]
        if res["proxy_commanders"]:
            lines.append(f"Commander as a proxy (no copy needed): {', '.join(res['proxy_commanders'])}")
            lines.append("")
        if res["missing"]:
            lines += ["Not covered by the collection:", "", "| Card | Needed | Given | Note |", "|---|---|---|---|"]
            lines += [f"| {m['name']} | {m['needed']} | {m['given']} | {m['note']} |" for m in res["missing"]]
            lines.append("")
        langs = Counter()
        for card in res["cards"]:
            for pick in card["picks"]:
                langs[pick["language"]] += pick["qty"]
                by_binder[pick["binder"] or "(no binder)"].append((spec.get("name", slug), card["name"], pick))
        lines += [f"Copies by language: {dict(langs)}", ""]
    lines += ["## Shared cards (two decks use the same card, each with its own copy)", ""]
    lines += [f"- {s['name']}: {', '.join(s['decks'])}" for s in assignment["shared"]] or ["- none"]
    lines.append("")
    for binder in sorted(by_binder):
        lines += [f"## Take out of the binder {binder}", "", "| Card | Set # | Language | Finish | Copies | For deck |", "|---|---|---|---|---|---|"]
        rows = sorted(by_binder[binder], key=lambda r: (r[1].casefold(), r[0]))
        lines += [f"| {c} | {p['set'].upper()} {p['number']} | {p['language']} | {p['foil']} | {p['qty']} | {d} |" for d, c, p in rows]
        lines.append("")
    return "\n".join(lines)


def main():
    """Read the inventory, the config and the lists; write the assignment and the pull list."""
    if not INVENTORY_PATH.exists():
        print("No data/cache/collection_inventory.json: run scripts/build_inventory.py first.")
        sys.exit(2)
    bulk = la.latest_bulk()
    if bulk is None:
        print("No oracle bulk file in data/cache/. Run scripts/collect_research_data.py first.")
        sys.exit(2)
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    index = la.build_index(list(la.iter_cards(bulk)))
    inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
    decks, problems, sizes = [], [], {}
    for spec in config["decks"]:
        deck, probs = read_deck(spec, index)
        problems += probs
        if deck is not None:
            decks.append(deck)
            sizes[deck["slug"]] = sum(q for _, q in deck["cards"].values())
    for slug, size in sizes.items():
        if size != 100:
            problems.append(f"{slug}: the list has {size} cards, not 100")
    assignment = allocate(decks, inventory)
    today = date.today().isoformat()
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(dict(assignment, problems=problems), indent=1, ensure_ascii=False), encoding="utf-8")
    report = REPORTS_DIR / f"pull-list-{today}.md"
    report.write_text(pull_list_markdown(config, assignment, sizes, problems, today), encoding="utf-8")
    for spec in config["decks"]:
        res = assignment["decks"].get(spec["slug"])
        if res:
            print(f"{spec['slug']}: {sum(c['given'] for c in res['cards'])} of {sizes[spec['slug']]} copies covered, "
                  f"{len(res['missing'])} cards missing")
    for p in problems:
        print("PROBLEM:", p)
    print(f"wrote {OUT_JSON.relative_to(ROOT)} and {report.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
