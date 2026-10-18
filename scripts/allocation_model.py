#!/usr/bin/env python3
"""Phase 8, step 1: the data model of the allocation (library; no network, nothing is written here).

What it knows how to do, all offline:
  - read the merged price offers (data/prices/merged-*.json, Phase 7) and the owned-card inventory
    (data/cache/collection_inventory.json, Phase 1), both keyed by Scryfall oracle ID so that a card
    spelled differently in a list, a store or the collection is still one card;
  - read a decklist (Phase 4 candidates, the owner's lists, or a list proposed in step 2);
  - price a list: owned copies first (an owned copy costs 0 and one physical copy sits in one deck,
    decision D5), then the cheapest available English or Spanish offer (the Spanish copy wins a tie,
    owner rule 2026-10-17), basic lands free (the owner holds 233), cards without stock reported;
  - report the shipping the cheapest-per-card purchase would need (5,000 CLP per store, outside the
    budget, decision of 2026-10-16) and which locked cards a set of lists covers.

Prices are a hint, never stock evidence (Phase 9 verifies). Power is never computed here: it is the
Commander Salt score of a list, read by hand (docs/power-scale.md).
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402
import read_store_prices as rsp  # noqa: E402

ROOT = la.ROOT
PRICES_DIR = rsp.OUT_DIR
INVENTORY_PATH = ROOT / "data" / "cache" / "collection_inventory.json"
LOCKED_PATH = ROOT / "decks" / "locked.txt"
CANDIDATES_DIR = ROOT / "decks" / "candidates"
SHIPPING_PER_STORE_CLP = 5000
USABLE_LANGUAGES = ("en", "es")
BASIC_NAMES = {"plains", "island", "swamp", "mountain", "forest", "wastes"}
META_LINE_RE = re.compile(r"^\d+\.\s+(.+?)\s+(\d+)\s*$")


def is_basic(name):
    """True for the basic lands (including the snow-covered ones): the owner holds plenty, cost 0."""
    n = la.normalize(name)
    if n.startswith("snow-covered "):
        n = n.split(" ", 1)[1]
    return n in BASIC_NAMES


def latest_merged():
    """The newest data/prices/merged-*.json, or None."""
    files = sorted(PRICES_DIR.glob("merged-*.json"))
    return files[-1] if files else None


def load_offers(index, path=None):
    """Available offers by oracle ID: (by_oid, unresolved card names, file name, as-of time)."""
    path = Path(path) if path else latest_merged()
    data = json.loads(path.read_text(encoding="utf-8"))
    by_oid, unresolved = {}, set()
    for offer in data["offers"]:
        if not offer.get("available"):
            continue
        card = index.get(la.normalize(offer["card"]))
        if card is None:
            unresolved.add(offer["card"])
            continue
        by_oid.setdefault(card["oracle_id"], []).append(offer)
    return by_oid, sorted(unresolved), path.name, data.get("as_of_utc")


def best_offer(offers):
    """The cheapest offer, the Spanish copy winning a tie (rsp.offer_rank), or None."""
    return min(offers, key=rsp.offer_rank) if offers else None


def load_owned(path=None):
    """Owned copies by oracle ID: {oid: {"name", "usable"}}; usable counts English and Spanish copies only."""
    data = json.loads(Path(path or INVENTORY_PATH).read_text(encoding="utf-8"))
    owned = {}
    for card in data["cards"]:
        usable = sum(n for lang, n in card["by_language"].items() if lang in USABLE_LANGUAGES)
        owned[card["oracle_id"]] = {"name": card["name"], "usable": usable, "copies": card["copies"]}
    return owned


def read_list(text, index):
    """A decklist as {"cards": Counter oid -> qty, "names": {oid: name}, "commanders": [oid], "unresolved": [...]}."""
    commanders, main, bad = la.parse_decklist(text)
    out = {"cards": Counter(), "names": {}, "commanders": [], "unresolved": list(bad)}
    for role, entries in (("commander", commanders), ("main", main)):
        for entry in entries:
            card = index.get(la.normalize(entry["name"]))
            if card is None:
                out["unresolved"].append(entry["name"])
                continue
            oid = card["oracle_id"]
            out["cards"][oid] += entry["qty"]
            out["names"][oid] = card["name"]
            if role == "commander":
                out["commanders"].append(oid)
    return out


def read_meta_picks(text, index):
    """The Upgrades-tab picks of a meta-staples file: [(oid, name, percent of decks)]; unknown names skipped."""
    picks = []
    for line in text.splitlines():
        match = META_LINE_RE.match(line.strip())
        card = index.get(la.normalize(match.group(1))) if match else None
        if card is not None:
            picks.append((card["oracle_id"], card["name"], int(match.group(2))))
    return picks


def read_locked(index):
    """The oracle IDs of the 32 must-keep cards of decks/locked.txt."""
    oids = []
    for raw in LOCKED_PATH.read_text(encoding="utf-8").splitlines():
        match = la.LINE_RE.match(raw.strip())
        card = index.get(la.normalize(match.group(2))) if match else None
        if card is not None:
            oids.append(card["oracle_id"])
    return oids


def price_list(listing, owned, offers_by_oid, claimed=None):
    """Cost of one list. `claimed` (Counter oid -> copies) holds the owned copies other decks already use;
    it is updated in place, so pricing the 3 decks in turn shares each physical copy once.

    Returns {"cost_clp", "owned": [names], "to_buy": [{name, qty, unit_clp, store, language, finish, url}],
    "no_stock": [names], "basics": count, "stores": [ids]}."""
    claimed = claimed if claimed is not None else Counter()
    result = {"cost_clp": 0, "owned": [], "to_buy": [], "no_stock": [], "basics": 0, "stores": []}
    for oid, qty in sorted(listing["cards"].items(), key=lambda kv: listing["names"][kv[0]]):
        name = listing["names"][oid]
        if is_basic(name):
            result["basics"] += qty
            continue
        have = max(owned.get(oid, {}).get("usable", 0) - claimed[oid], 0)
        use = min(qty, have)
        claimed[oid] += use
        if use:
            result["owned"].append(name)
        need = qty - use
        if not need:
            continue
        offer = best_offer(offers_by_oid.get(oid, []))
        if offer is None:
            result["no_stock"].append(name)
            continue
        result["to_buy"].append({"name": name, "qty": need, "unit_clp": offer["price_clp"],
                                 "store": offer["store"], "language": offer["language"],
                                 "finish": offer["finish"], "url": offer.get("url", "")})
        result["cost_clp"] += need * offer["price_clp"]
    result["stores"] = sorted({b["store"] for b in result["to_buy"]})
    return result


def shipping_clp(stores):
    """Assumed shipping for the stores used (outside the budget)."""
    return SHIPPING_PER_STORE_CLP * len(set(stores))


def locked_coverage(lists, locked_oids):
    """Which locked cards the given lists cover: {"missing": [oids in no list], "copies_needed": Counter}."""
    needed = Counter()
    for listing in lists:
        for oid in locked_oids:
            if listing["cards"].get(oid):
                needed[oid] += 1
    return {"missing": [oid for oid in locked_oids if not needed[oid]], "copies_needed": needed}


def fits_identity(card, identity):
    """True when the card's color identity is inside the deck's identity (a set of color letters)."""
    return set(card.get("color_identity") or []) <= set(identity)
