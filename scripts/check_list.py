#!/usr/bin/env python3
"""Phase 8: check proposed decklists against every constraint at once. Read-only: it prints, writes nothing.

Run it with the "Run Python File" button (no arguments) to check every decks/proposals/*.txt, or pass
the files: `python scripts/check_list.py decks/proposals/toph_cap20000.txt [more files] [--alone] [--brief]`
(`--brief` lists only the 8 priciest purchases, to save reading time).
No network. It reads the Scryfall and Spellbook caches, the merged prices (data/prices/merged-*.json),
the inventory (data/cache/collection_inventory.json) and decks/locked.txt.

A list is a ManaBox-style text file (`// Commander`, `1 Card Name` lines, basics as `5 Mountain`). For each
list it reports:
  - Layer A at the deck's target bracket (floor, Game Changers, flagged combos, review notes, rejections:
    100 cards, singleton, Commander legality, color identity, unknown names);
  - cost: owned copies free, the cheapest available English or Spanish offer for the rest (the Spanish copy
    wins a tie), cards with no stock anywhere, the stores used and the assumed shipping (5,000 CLP per store,
    outside the budget);
  - reversible cards: any card that must be taken out of its sleeve and turned over or around (transform,
    modal double-faced, meld and flip cards) is not allowed (owner rule, 2026-10-18); adventure, split and
    similar one-faced cards are fine;
  - the locked cards the list holds and those that fit its color identity but are missing (printed only when
    decks/locked.txt has cards; it has been empty since 2026-10-18).
A cap is read from the file name (`..._cap20000.txt`) and compared with the cost. When several files are
checked together they share the owned copies in the order given (one physical copy sits in one deck, D5),
so the second deck pays for a card the first one used; `--alone` prices each list as if it were the only one.
Prices are a hint: stock is verified in Phase 9. Power is not computed: it is the Commander Salt score of the
exact list, read by hand.
"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allocation_model as am  # noqa: E402
import layer_a as la  # noqa: E402

ROOT = la.ROOT
PROPOSALS = ROOT / "decks" / "proposals"
CAP_RE = re.compile(r"_cap(\d+)", re.I)
# Scryfall layouts of cards with two physical faces or a rotated half: the owner does not want to take a card
# out of its sleeve to turn it over (2026-10-18). Adventure, split, prepare and similar layouts are one face.
FLIP_LAYOUTS = {"transform", "modal_dfc", "meld", "flip", "reversible_card", "double_faced_token"}


def cap_from_name(name):
    """The budget cap in CLP written in a file name like `toph_cap20000.txt`, or None."""
    match = CAP_RE.search(name)
    return int(match.group(1)) if match else None


def cap_status(cost, cap):
    """One line comparing the cost with the cap."""
    if cap is None:
        return "no cap in the file name"
    return f"{'within' if cost <= cap else 'OVER'} the cap of {cap:,} CLP ({cap - cost:+,} CLP left)"


def needs_flipping(card):
    """True for a card that must be taken out of its sleeve and turned over or around (owner rule 2026-10-18)."""
    return card.get("layout") in FLIP_LAYOUTS


def build_context():
    """Everything the checks read (None when a cache is missing): index, card objects, offers, owned."""
    bulk = la.latest_bulk()
    if bulk is None or am.latest_merged() is None or not am.INVENTORY_PATH.exists():
        return None
    cards = list(la.iter_cards(bulk))
    index = la.build_index(cards)
    offers, _, merged_name, _ = am.load_offers(index)
    return {"index": index, "by_oid": {c.get("oracle_id"): c for c in cards}, "offers": offers,
            "owned": am.load_owned(), "locked": am.read_locked(index), "hazards": la.load_hazards(),
            "spellbook": la.load_spellbook() if la.SPELLBOOK_SLIM.exists() else None,
            "banner": f"prices {merged_name}; bulk {bulk.name}"}


def check_one(path, ctx, claimed, brief=False):
    """Report lines and a verdict dict for one list file."""
    return check_text(path.name, path.read_text(encoding="utf-8-sig"), ctx, claimed, brief)


def check_text(name, text, ctx, claimed, brief=False):
    """Report lines and a verdict dict for a list given as text; `name` carries the cap (`..._cap20000`).
    In brief mode only the 8 priciest purchases are listed."""
    listing = am.read_list(text, ctx["index"])
    commanders, main_cards, bad = la.parse_decklist(text)
    slug = next((s for s, n in la.COMMANDERS.items()
                 if any(la.normalize(e["name"]) == la.normalize(n) for e in commanders)), None)
    target = la.TARGET_BRACKET.get(slug, la.DEFAULT_TARGET)
    report, _ = la.analyze(commanders, main_cards, ctx["index"], slug, ctx["spellbook"], ctx["hazards"], target)
    priced = am.price_list(listing, ctx["owned"], ctx["offers"], claimed)
    cap = cap_from_name(name)
    sb = report.get("spellbook") or {}
    flippers = sorted(listing["names"].get(oid, oid) for oid in set(listing["cards"]) | set(listing["commanders"])
                      if needs_flipping(ctx["by_oid"].get(oid, {})))
    identity = set()
    for oid in listing["commanders"]:
        identity |= set(ctx["by_oid"][oid].get("color_identity") or [])
    held = [listing["names"][o] for o in ctx["locked"] if listing["cards"].get(o)]
    missing_fit = [ctx["by_oid"][o]["name"] for o in ctx["locked"]
                   if not listing["cards"].get(o) and am.fits_identity(ctx["by_oid"][o], identity)]
    shipping = am.shipping_clp(priced["stores"])
    ok_layer = report["floor_ok_so_far"] and not bad
    ok = ok_layer and not priced["no_stock"] and not flippers and (cap is None or priced["cost_clp"] <= cap)
    lines = [f"=== {name}  ({slug or 'commander not recognized'}, target Bracket {target})",
             f"Layer A: floor {report['floor']}, {'OK' if ok_layer else 'NOT OK'}; "
             f"{sum(listing['cards'].values())} cards; Game Changers {len(report['checks']['game_changers']['cards'])} "
             f"{report['checks']['game_changers']['cards']}; extra-turn cards {report['checks']['extra_turns']['count']}"]
    lines += [f"  reason: {r}" for r in report["reasons"]]
    lines += [f"  unparsed line: {b}" for b in bad]
    lines += [f"  flagged combo (floor {r['floor']}): {r['cards']}" for r in sb.get("included_flagged", [])]
    lines += [f"  curated hazard (floor {r['floor']}): {r['hazard']}" for r in report.get("curated_hazards", [])]
    lines += [f"  review: {n}" for n in report["review_notes"]]
    lines += [f"Cost: {priced['cost_clp']:,} CLP for {len(priced['to_buy'])} cards to buy; "
              f"{len(priced['owned'])} owned cards used; {priced['basics']} basic lands; "
              f"stores {priced['stores']}, shipping {shipping:,} CLP (outside the budget)",
              f"Cap: {cap_status(priced['cost_clp'], cap)}"]
    lines += [f"  NO STOCK anywhere: {', '.join(priced['no_stock'])}"] if priced["no_stock"] else []
    lines += [f"  REVERSIBLE (must be taken out of the sleeve and turned over, not allowed): {', '.join(flippers)}"] \
        if flippers else []
    buys = sorted(priced["to_buy"], key=lambda b: -b["unit_clp"] * b["qty"])
    if brief and len(buys) > 8:
        lines.append(f"  ({len(buys) - 8} cheaper purchases not listed in --brief mode)")
    for buy in buys[:8] if brief else buys:
        lines.append(f"  buy {buy['qty']} x {buy['name']}: {buy['unit_clp']:,} CLP at {buy['store']} "
                     f"({buy['language']}, {buy['finish']})")
    if ctx["locked"]:  # the lock list is empty since 2026-10-18; nothing is printed while it is
        lines.append(f"Locked cards held ({len(held)}): {', '.join(held) or 'none'}")
        lines.append(f"Locked cards that fit this identity but are not in the list ({len(missing_fit)}): "
                     f"{', '.join(missing_fit) or 'none'}")
    lines.append(f"VERDICT: {'ELIGIBLE (before the Commander Salt score and the stock check)' if ok else 'NOT ELIGIBLE'}")
    return lines, {"file": name, "ok": ok, "ok_layer": ok_layer, "floor": report["floor"], "cost": priced["cost_clp"],
                   "no_stock": priced["no_stock"], "reversible": flippers, "held": held,
                   "reasons": report["reasons"]}


def main(argv):
    """Check the given lists (default: every decks/proposals/*.txt) and print the reports."""
    alone = "--alone" in argv
    brief = "--brief" in argv
    files = [Path(a) for a in argv if not a.startswith("--")] or sorted(PROPOSALS.glob("*.txt"))
    if not files:
        print("No lists to check: pass files or put them in decks/proposals/*.txt")
        return 2
    ctx = build_context()
    if ctx is None:
        print("Missing the Scryfall bulk, the merged prices or the inventory (Phases 1 and 7 first).")
        return 2
    print(ctx["banner"] + "\n")
    claimed, verdicts = Counter(), []
    for path in files:
        lines, verdict = check_one(path, ctx, Counter() if alone else claimed, brief)
        print("\n".join(lines) + "\n")
        verdicts.append(verdict)
    if len(verdicts) > 1:
        total = sum(v["cost"] for v in verdicts)
        print(f"Together: {total:,} CLP (owned copies shared once); eligible: "
              f"{sum(v['ok'] for v in verdicts)} of {len(verdicts)}")
    return 0 if all(v["ok"] for v in verdicts) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
