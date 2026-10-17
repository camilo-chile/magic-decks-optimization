#!/usr/bin/env python3
"""Phase 7: read prices (CLP) and stock flags of the candidate cards from the stores' public catalogs.

Run it with the "Run Python File" button (no arguments). It needs the `requests` package and the
network; it reads only public catalog feeds (Shopify `products.json`, the WooCommerce Store API),
one request per second at most, with a clear User-Agent, and stops a store on repeated HTTP 429.
It never signs in, never touches a cart or a checkout. Terms of service were not read (owner's
instruction, 2026-10-16); the pace is deliberately gentle.

Cards read: every card of decks/candidates/<slug>/*.txt, of the meta-staples-bracket3.md files and of
decks/locked.txt (names in English), minus basic lands. Offers kept: English or Spanish, near mint or
lightly played, any finish (decision D6), price above 0. Out-of-stock variants are kept with
`available: false`. The `available` flag is a price-phase hint, never stock evidence (Phase 9 verifies).

Writes, next to each other under data/prices/:
  <YYYYMMDDTHHMMZ>.json            every kept offer with its evidence (store, URL, title, variant, fetch time)
  <YYYYMMDDTHHMMZ>.summary.txt     per store counts, cards with no offer, cheapest offer per card
  <YYYYMMDDTHHMMZ>.progress.log    progress with ETA (this run can take 20 minutes or more)
"""
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402

ROOT = la.ROOT
OUT_DIR = ROOT / "data" / "prices"
USER_AGENT = "mazos-magic-price-reader/1.0 (personal, read-only, at most 1 request per second)"
MIN_INTERVAL_S = 1.0
MAX_429 = 3
SHOPIFY_PAGE = 250
WOO_PAGE = 100
MAX_PAGES = 500  # guard against a feed that never ends

# Stores with a public machine-readable catalog (docs/research/store-recon-2026-10-16.md).
# Magic4Ever (pref 2, Jumpseller) loads its search results from its own public API
# (mantenedor.magic4ever.cl/api/public/search, found in the browser on 2026-10-17): per variant
# language, finish, condition grade, stock quantity and price in CLP.
STORES = [
    {"id": "paytowin", "pref": 1, "name": "PayToWin", "kind": "shopify",
     "base": "https://www.paytowin.cl", "collection": "mtg-singles-instock", "enabled": True},
    {"id": "magic4ever", "pref": 2, "name": "Magic4Ever", "kind": "magic4ever",
     "base": "https://www.magic4ever.cl", "api": "https://mantenedor.magic4ever.cl/api/public/search",
     "enabled": True},
    {"id": "cardnexus", "pref": 3, "name": "CardNexus", "kind": "woocommerce",
     "base": "https://cardnexus.cl", "enabled": True},
    {"id": "gameofmagic", "pref": 4, "name": "Game of Magic Singles", "kind": "shopify",
     "base": "https://gameofmagicsingles.cl", "collection": "mtg-todas-las-singles", "enabled": True},
    {"id": "lacomarca", "pref": 6, "name": "Tienda La Comarca", "kind": "shopify",
     "base": "https://www.tiendalacomarca.cl", "collection": "magic-the-gathering-singles", "enabled": True},
    {"id": "oasis", "pref": 7, "name": "Oasis Games", "kind": "shopify",
     "base": "https://www.oasisgames.cl", "collection": "mtg-singles-instock", "enabled": True},
    {"id": "piedrabruja", "pref": 8, "name": "Piedra Bruja", "kind": "shopify",
     "base": "https://piedrabruja.cl", "collection": "single-mtg", "enabled": True},
    {"id": "afkstore", "pref": 9, "name": "AFK Store", "kind": "shopify",
     "base": "https://www.afkstore.cl", "collection": "singles-mtg", "enabled": True},
]
# Already read on 2026-10-17 (Magic4Ever and CardNexus by this script, PayToWin, Game of Magic and Oasis
# in the owner's browser, see docs/research/phase7-handoff-2026-10-17.md): not requested again.
# scripts/merge_prices.py keeps the newest reading of each store. Remove an id here to refresh it.
ALREADY_READ = {"paytowin", "magic4ever", "cardnexus", "gameofmagic", "oasis"}
for _store in STORES:
    _store["enabled"] = _store["id"] not in ALREADY_READ

BASICS = {"plains", "island", "swamp", "mountain", "forest", "wastes", "snow-covered plains",
          "snow-covered island", "snow-covered swamp", "snow-covered mountain", "snow-covered forest"}
META_LINE_RE = re.compile(r"^\d+\.\s+(.+?)\s+\d+\s*$")
OTHER_LANGUAGES_RE = re.compile(
    r"\b(french|francés|frances|german|alemán|aleman|italian|italiano|portuguese|portugués|portugues|"
    r"japanese|japonés|japones|korean|coreano|chinese|chino|russian|ruso|phyrexian|fran[cç]ais|deutsch)\b",
    re.I)
SPANISH_RE = re.compile(r"español|espanol|spanish|\(es\)", re.I)
ENGLISH_RE = re.compile(r"ingl[eé]s|english|\(en\)", re.I)
CONDITIONS = [("DMG", r"damaged|\bdmg\b"), ("HP", r"heavily played|\bhp\b"),
              ("MP", r"moderately played|\bmp\b"), ("LP", r"lightly played|\blp\b"),
              ("NM", r"near mint|\bnm\b|\bmint\b")]
FOIL_RE = re.compile(r"(?<!non-)(?<!non )(?<!no )\bfoil\b", re.I)
ETCHED_RE = re.compile(r"\betched\b", re.I)
FINISH_WORDS = {"regular", "foil", "borderless", "showcase", "extended", "etched", "retro", "full",
                "art", "promo", "surge", "serialized", "normal", "non-foil", "nonfoil"}
ART_CARD_RE = re.compile(r"\bart (card|series)\b", re.I)  # art cards are not the playable card
ACCEPTED_LANGUAGES = {"en", "es"}
ACCEPTED_CONDITIONS = {"NM", "LP"}


# ---------------------------------------------------------------- card list

def targets_from_repo():
    """normalized front-face name -> display name, for every candidate, meta pick and locked card."""
    names = {}

    def add(raw):
        raw = raw.strip()
        key = la.normalize(raw.split(" // ")[0])
        if key and key not in BASICS:
            names.setdefault(key, raw.split(" // ")[0].strip())

    for path in sorted((ROOT / "decks" / "candidates").glob("*/*.txt")):
        commanders, deck, _ = la.parse_decklist(path.read_text(encoding="utf-8-sig"))
        for entry in commanders + deck:
            add(entry["name"])
    for path in sorted((ROOT / "decks" / "candidates").glob("*/meta-staples-bracket3.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            match = META_LINE_RE.match(line.strip())
            if match:
                add(match.group(1))
    locked = ROOT / "decks" / "locked.txt"
    if locked.exists():
        _, deck, _ = la.parse_decklist(locked.read_text(encoding="utf-8-sig"))
        for entry in deck:
            add(entry["name"])
    return names


# ---------------------------------------------------------------- parsing

def classify(text):
    """(language, condition, finish, inferred) from the words of a title and variant."""
    inferred = []
    if OTHER_LANGUAGES_RE.search(text):
        language = "other"
    elif SPANISH_RE.search(text):
        language = "es"
    elif ENGLISH_RE.search(text):
        language = "en"
    else:
        language = "en"
        inferred.append("language")
    condition = None
    for code, pattern in CONDITIONS:
        if re.search(pattern, text, re.I):
            condition = code
            break
    if condition is None:
        condition = "NM"
        inferred.append("condition")
    if ETCHED_RE.search(text):
        finish = "etched"
    elif FOIL_RE.search(text) and not re.search(r"non[- ]?foil|no foil", text, re.I):
        finish = "foil"
    else:
        finish = "nonfoil"
    return language, condition, finish, inferred


def match_title(title, targets):
    """Match a product title to a target card. Returns (display name, quality, set hint) or None.

    The longest word prefix of the title that is a target name wins. Quality `exact` when what follows is
    empty, a bracket, a parenthesis, a `//`, a dash or a finish word; otherwise `loose`.
    """
    clean = re.sub(r"^(french|german|italian|spanish|portuguese|japanese|korean|russian|chinese)\s+",
                   "", title.strip(), flags=re.I)
    words = clean.split(" ")
    for cut in range(min(len(words), 9), 0, -1):
        prefix = " ".join(words[:cut])
        key = la.normalize(prefix)
        if key in targets:
            rest = clean[len(prefix):].strip()
            first = rest.split(" ")[0].lower() if rest else ""
            exact = (not rest or rest[0] in "[(-—" or rest.startswith("//")
                     or first.strip("(") in FINISH_WORDS or first.isdigit())
            hint = re.search(r"\[([^\]]+)\]", rest)
            return targets[key], "exact" if exact else "loose", (hint.group(1) if hint else "")
    return None


def shopify_offers(product, store, targets, fetched_at):
    """Offers from one Shopify product (one per variant that passes the filters)."""
    if ART_CARD_RE.search(product.get("title") or ""):
        return []
    hit = match_title(product.get("title") or "", targets)
    if not hit:
        return []
    card, quality, set_hint = hit
    out = []
    for variant in product.get("variants") or []:
        text = " ".join([product.get("title") or "", variant.get("title") or ""])
        language, condition, finish, inferred = classify(text)
        try:
            price = int(float(variant.get("price") or 0))
        except ValueError:
            continue
        if price <= 0 or language not in ACCEPTED_LANGUAGES or condition not in ACCEPTED_CONDITIONS:
            continue
        out.append({
            "store": store["id"], "card": card, "match": quality, "set_hint": set_hint,
            "language": language, "condition": condition, "finish": finish,
            "inferred": inferred, "price_clp": price, "available": bool(variant.get("available")),
            "quantity": None, "title": product.get("title"), "variant": variant.get("title"),
            "url": f"{store['base']}/products/{product.get('handle')}", "fetched_at": fetched_at,
        })
    return out


def woo_offers(product, store, targets, fetched_at):
    """Offers from one WooCommerce Store API product: purchasable listings only (`cn-child-*`)."""
    key = la.normalize((product.get("name") or "").split(" // ")[0])
    if key not in targets or not product.get("is_purchasable") or ART_CARD_RE.search(product.get("name") or ""):
        return []
    prices = product.get("prices") or {}
    try:
        price = int(prices.get("price") or 0) // (10 ** int(prices.get("currency_minor_unit") or 0))
    except ValueError:
        return []
    attrs = {a.get("name", "").lower(): " ".join(t.get("name", "") for t in a.get("terms", []))
             for a in product.get("attributes") or []}
    language, condition, finish, inferred = classify(
        " ".join([attrs.get("idioma", ""), attrs.get("pa_condicion", ""), attrs.get("foil", "")]))
    if price <= 0 or language not in ACCEPTED_LANGUAGES or condition not in ACCEPTED_CONDITIONS:
        return []
    text = (product.get("stock_availability") or {}).get("text") or ""
    qty = re.search(r"(\d+)\s+disponible", text)
    return [{
        "store": store["id"], "card": targets[key], "match": "exact", "set_hint": "",
        "language": language, "condition": condition, "finish": finish, "inferred": inferred,
        "price_clp": price, "available": bool(product.get("is_in_stock")),
        "quantity": int(qty.group(1)) if qty else None,
        "title": product.get("name"), "variant": attrs.get("idioma", "") + "/" + attrs.get("pa_condicion", ""),
        "url": product.get("permalink"), "fetched_at": fetched_at,
    }]


def magic4ever_offers(card, store, targets, fetched_at):
    """Offers from one Magic4Ever search card (its variants carry language, finish, grade, stock, price)."""
    if ART_CARD_RE.search(card.get("name") or ""):
        return []
    base_name = re.sub(r"\s*\([^)]*\)\s*$", "", card.get("name") or "").split(" // ")[0]
    key = la.normalize(base_name)
    if key not in targets:
        return []
    out = []
    for variant in card.get("variants") or []:
        language = (variant.get("language") or "").lower()
        condition = (variant.get("conditionGrade") or "").upper()
        price = int(variant.get("priceClp") or 0)
        if price <= 0 or language not in ACCEPTED_LANGUAGES or condition not in ACCEPTED_CONDITIONS:
            continue
        stock = int(variant.get("stock") or 0)
        out.append({
            "store": store["id"], "card": targets[key], "match": "exact",
            "set_hint": card.get("setName") or "", "language": language, "condition": condition,
            "finish": "foil" if variant.get("finish") == "foil" else variant.get("finish") or "nonfoil",
            "inferred": [], "price_clp": price, "available": stock > 0, "quantity": stock,
            "title": card.get("name"), "variant": variant.get("sku"),
            "url": variant.get("productUrl") or card.get("productUrl"), "fetched_at": fetched_at,
        })
    return out


# ---------------------------------------------------------------- network

class Progress:
    """Prints and logs progress lines with an ETA."""

    def __init__(self, log_path):
        self.log_path = log_path
        self.start = time.time()

    def log(self, message):
        line = f"{datetime.now().strftime('%H:%M:%S')}  {message}"
        print(line, flush=True)
        with open(self.log_path, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")

    @staticmethod
    def eta(done, total, started):
        if done <= 0 or total <= 0:
            return "ETA ?"
        remaining = (time.time() - started) / done * max(total - done, 0)
        return f"ETA {int(remaining // 60)}m{int(remaining % 60):02d}s"


class Throttle:
    def __init__(self, interval=MIN_INTERVAL_S):
        self.interval, self.last = interval, 0.0

    def wait(self):
        gap = self.interval - (time.time() - self.last)
        if gap > 0:
            time.sleep(gap)
        self.last = time.time()


def get_json(requests, throttle, url, params=None, progress=None):
    """GET JSON with throttling; honors Retry-After on 429; raises after MAX_429 of them."""
    rate_limited = 0
    while True:
        throttle.wait()
        resp = requests.get(url, params=params, headers={"User-Agent": USER_AGENT,
                                                         "Accept": "application/json"}, timeout=60)
        if resp.status_code == 429:
            rate_limited += 1
            if rate_limited >= MAX_429:
                raise RuntimeError("HTTP 429 three times: stopping this store")
            wait = int(resp.headers.get("Retry-After") or 30)
            if progress:
                progress.log(f"  429 from {url}: waiting {wait}s")
            time.sleep(wait)
            continue
        resp.raise_for_status()
        return resp.json(), resp


def read_shopify(requests, throttle, store, targets, progress):
    """Page through the collection feed; return (offers, stats)."""
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    base = f"{store['base']}/collections/{store['collection']}"
    total = 0
    try:
        data, _ = get_json(requests, throttle, base + ".json", progress=progress)
        total = int((data.get("collection") or {}).get("products_count") or 0)
    except Exception as exc:  # the count is only for the ETA
        progress.log(f"  no product count ({exc}); ETA unknown")
    pages_expected = (total + SHOPIFY_PAGE - 1) // SHOPIFY_PAGE if total else 0
    offers, seen, started, truncated = [], 0, time.time(), False
    for page in range(1, MAX_PAGES + 1):
        try:
            data, _ = get_json(requests, throttle, base + "/products.json",
                               {"limit": SHOPIFY_PAGE, "page": page}, progress)
        except Exception as exc:
            # Shopify lists at most 100 pages of 250: page 101 answers HTTP 400. The default order can be
            # price-descending, so the cheap tail may be missing: flag the reading as truncated.
            status = getattr(getattr(exc, "response", None), "status_code", None)
            if status == 400 and page > 1:
                truncated = True
                progress.log(f"  {store['name']}: HTTP 400 at page {page}: listing cap reached, reading truncated")
                break
            raise
        products = data.get("products") or []
        if not products:
            break
        seen += len(products)
        for product in products:
            offers += shopify_offers(product, store, targets, fetched_at)
        progress.log(f"  {store['name']}: page {page}" + (f"/{pages_expected}" if pages_expected else "")
                     + f", {seen} products read, {len(offers)} offers kept, "
                     + (Progress.eta(page, pages_expected, started) if pages_expected else "ETA ?"))
        if len(products) < SHOPIFY_PAGE:
            break
    return offers, {"products_read": seen, "products_count_reported": total, "offers": len(offers),
                    "truncated": truncated}


def read_woocommerce(requests, throttle, store, targets, progress):
    """One search per card (the catalog is large); keep purchasable exact-name listings."""
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    url = f"{store['base']}/wp-json/wc/store/v1/products"
    offers, seen_ids, started = [], set(), time.time()
    names = sorted(targets.values())
    for i, name in enumerate(names, 1):
        for page in range(1, 30):
            data, _ = get_json(requests, throttle, url,
                               {"search": name, "per_page": WOO_PAGE, "page": page}, progress)
            for product in data:
                if product.get("id") in seen_ids:
                    continue
                seen_ids.add(product.get("id"))
                offers += woo_offers(product, store, targets, fetched_at)
            if len(data) < WOO_PAGE:
                break
        if i % 20 == 0 or i == len(names):
            progress.log(f"  {store['name']}: {i}/{len(names)} cards searched, {len(offers)} offers kept, "
                         + Progress.eta(i, len(names), started))
    return offers, {"cards_searched": len(names), "offers": len(offers)}


def read_magic4ever(requests, throttle, store, targets, progress):
    """One search per card against the store's own public API; keep exact-name cards."""
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    offers, started = [], time.time()
    names = sorted(targets.values())
    for i, name in enumerate(names, 1):
        offset = 0
        while True:
            data, _ = get_json(requests, throttle, store["api"],
                               {"q": name, "limit": 100, "offset": offset, "withVariants": 1}, progress)
            cards = data.get("cards") or []
            for card in cards:
                offers += magic4ever_offers(card, store, targets, fetched_at)
            offset += len(cards)
            if not cards or offset >= int(data.get("total") or 0):
                break
        if i % 20 == 0 or i == len(names):
            progress.log(f"  {store['name']}: {i}/{len(names)} cards searched, {len(offers)} offers kept, "
                         + Progress.eta(i, len(names), started))
    return offers, {"cards_searched": len(names), "offers": len(offers)}


READERS = {"shopify": read_shopify, "woocommerce": read_woocommerce, "magic4ever": read_magic4ever}


# ---------------------------------------------------------------- output

def offer_rank(offer):
    """Sort key for the best offer: cheapest first; at the same price Spanish before English (owner, 2026-10-17)."""
    return (offer["price_clp"], 0 if offer["language"] == "es" else 1)


def summarize(targets, offers, store_stats):
    """Text summary: stats per store, cards with no available offer, cheapest available offer per card."""
    lines = ["Stores"]
    for sid, stats in store_stats.items():
        lines.append(f"  {sid}: {stats}")
        if stats.get("truncated"):
            lines.append("    WARNING: the listing hit Shopify's 100-page cap; the cheapest products may be missing")
    by_card = {}
    for offer in offers:
        by_card.setdefault(offer["card"], []).append(offer)
    missing = sorted(name for name in targets.values()
                     if not any(o["available"] for o in by_card.get(name, [])))
    lines += ["", f"Cards requested: {len(targets)}; with at least one available offer: "
                  f"{len(targets) - len(missing)}; with none: {len(missing)}", ""]
    lines.append("Cards with no available offer (English or Spanish, NM or LP):")
    lines += [f"  {name}" for name in missing]
    lines += ["", "Cheapest available offer per card (any finish):"]
    for name in sorted(by_card):
        live = [o for o in by_card[name] if o["available"]]
        if live:
            best = min(live, key=offer_rank)
            lines.append(f"  {name}: {best['price_clp']} CLP at {best['store']} "
                         f"({best['language']}, {best['condition']}, {best['finish']}, match {best['match']})")
    return "\n".join(lines) + "\n"


def main():
    try:
        import requests
    except ImportError:
        print("The 'requests' package is missing in this environment. Run once:\n  pip install requests")
        sys.exit(2)
    targets = targets_from_repo()
    if not targets:
        print("No cards found under decks/candidates/ or decks/locked.txt.")
        sys.exit(2)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    progress = Progress(OUT_DIR / f"{stamp}.progress.log")
    progress.log(f"{len(targets)} cards to price; stores: "
                 + ", ".join(s["name"] for s in STORES if s["enabled"]))
    throttle, offers, store_stats = Throttle(), [], {}
    active = [s for s in STORES if s["enabled"]]
    for n, store in enumerate(active, 1):
        progress.log(f"Store {n}/{len(active)}: {store['name']} ({store['kind']})")
        try:
            got, stats = READERS[store["kind"]](requests, throttle, store, targets, progress)
            offers += got
            store_stats[store["id"]] = stats
        except Exception as exc:  # one failing store must not lose the others
            store_stats[store["id"]] = {"error": f"{type(exc).__name__}: {exc}"}
            progress.log(f"  FAILED {store['name']}: {exc}")
    result = {"as_of_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "note": "Price-phase evidence only: `available` is a hint, stock is verified in Phase 9.",
              "cards_requested": sorted(targets.values()), "store_stats": store_stats, "offers": offers}
    (OUT_DIR / f"{stamp}.json").write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT_DIR / f"{stamp}.summary.txt").write_text(summarize(targets, offers, store_stats), encoding="utf-8")
    progress.log(f"Done: {len(offers)} offers. Wrote data/prices/{stamp}.json and .summary.txt")
    failed = [s for s, v in store_stats.items() if "error" in v]
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
