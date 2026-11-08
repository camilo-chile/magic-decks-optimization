#!/usr/bin/env python3
"""Phase 2 step 7.5: live stock and price of every line of the purchase order, read from the stores themselves.

Run it with the "Run Python File" button (no arguments). It reads the store tables of the purchase plan
(decks/reports/purchase-plan-<date>.md, the newest; struck rows `~~...~~` and owed cards at price 0 are skipped) and asks each
store, one request at a time with a pause, for that card's product data:

  Shopify (Game of Magic Singles, PayToWin)  /search/suggest.json, then /products/<handle>.js (variants: price, available)
                                             and the product page for the quantity the theme prints
  Jumpseller (Rivendel El Concilio)          the search page, then the product page's variant JSON (price, stock, language)

For each line it lists every in-stock English or Spanish variant whose title starts with the card name, and gives a status:
`ok` (a variant in the planned language is in stock, enough copies when the quantity is shown), `other_language` (only the
other language is in stock), `price_up` (the cheapest planned-language copy costs more than 5 % over the plan), `no_stock`, or
`error`. Progress with an ETA on the console and in data/stock/order-<stamp>.progress.log. Writes data/stock/order-<YYYYMMDDTHHMMZ>.json and decks/reports/stock-order-<YYYYMMDDTHHMMZ>.md. Read-only: no cart,
no sign-in, no form. Evidence for the purchase only within 24 hours.
"""
import json
import re
import sys
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote_plus

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from read_store_prices import Progress  # noqa: E402  (console + log file lines with an ETA)

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "decks" / "reports"
STOCK_DIR = ROOT / "data" / "stock"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
PAUSE_S = 1.5
PRICE_DRIFT = 0.05
# Stores whose product JSON answers HTTP 429 (Retry-After 60) to any script, found 2026-11-08: they are read in the owner's
# browser with scripts/browser_shopify_lookup.js instead, and this script marks their lines "read_in_browser".
BROWSER_STORES = {"Game of Magic Singles", "PayToWin"}
STORES = {
    "Game of Magic Singles": ("shopify", "https://gameofmagicsingles.cl"),
    "PayToWin": ("shopify", "https://www.paytowin.cl"),
    "Rivendel El Concilio": ("jumpseller", "https://www.rivendelelconcilio.cl"),
}
SPANISH = re.compile(r"espa[nñ]ol|spanish|\bes\b|\(es\)", re.I)
OTHER_LANG = re.compile(r"japon|japan|ital|german|alem|french|franc|portug|chin|korea|russ", re.I)
BAD_CONDITION = re.compile(r"\b(hp|heavily|damaged|dmg|mp|moderately|poor)\b", re.I)


def normalize(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def language_of(text):
    if OTHER_LANG.search(text):
        return "other"
    return "es" if SPANISH.search(text) else "en"


def parse_plan(text):
    """Order lines (store, card, qty, planned language, planned price) from the plan's `### Store N: <name>` tables."""
    lines, store = [], None
    for row in text.splitlines():
        head = re.match(r"###\s+Store\s+\d+:\s+(.+?)\s*(\(|$)", row)
        if head:
            store = head.group(1).strip()
            continue
        if row.startswith("## "):
            store = None
        if not store or store not in STORES or not re.match(r"\|\s*\d+\s*\|", row) or "~~" in row:
            continue
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        name = re.sub(r"\*|,?\s*full art", "", cells[1]).strip()
        qty = 1
        times = re.search(r"\s+x(\d+)$", name)
        if times:
            qty, name = int(times.group(1)), name[:times.start()].strip()
        name = re.sub(r"\s*\(.*\)$", "", name).strip().rstrip(",")
        price = re.search(r"([\d,]+)", cells[5].split("(")[0].replace(".", ","))
        planned = int(price.group(1).replace(",", "")) if price else 0
        if planned == 0:
            continue  # owed card, nothing to buy
        lang = "es" if "ES" in cells[3].replace("*", "").split() or cells[3].replace("*", "").startswith("ES") else (
            "any" if cells[3].lower().startswith("any") else "en")
        lines.append({"store": store, "card": name, "qty": qty, "language": lang, "planned_clp": planned,
                      "unit_planned": round(planned / qty), "printing": cells[4], "use": cells[2]})
    return lines


class Client:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": UA, "Accept-Language": "es-CL,es;q=0.9,en;q=0.8"})
        self.last = 0.0

    def get(self, url):
        for attempt in range(4):
            wait = PAUSE_S - (time.time() - self.last)
            if wait > 0:
                time.sleep(wait)
            self.last = time.time()
            resp = self.session.get(url, timeout=60)
            if resp.status_code == 429:
                time.sleep(int(resp.headers.get("Retry-After") or 20) + 5 * attempt)
                continue
            return resp
        return resp


def title_matches(title, card):
    t, c = normalize(title), normalize(card)
    if c.endswith(" token"):  # a token line: "Elephant token" matches "Elephant // Wurm Token" and the like
        return t.startswith(c[:-6] + " ") and "token" in t
    return t == c or t.startswith(c + " ")


def query_of(card):
    return card[:-6] if card.lower().endswith(" token") else card


def shopify_variants(client, base, card):
    resp = client.get(f"{base}/search/suggest.json?q={quote_plus(query_of(card))}&resources[type]=product&resources[limit]=10")
    resp.raise_for_status()
    products = resp.json().get("resources", {}).get("results", {}).get("products", [])
    out = []
    for prod in products:
        if not title_matches(prod.get("title", ""), card):
            continue
        handle = prod["handle"]
        data = client.get(f"{base}/products/{handle}.js").json()
        page = None
        for var in data.get("variants", []):
            text = f"{data.get('title', '')} {var.get('title', '')}"
            if not var.get("available") or BAD_CONDITION.search(var.get("title", "")):
                continue
            if page is None:
                page = client.get(f"{base}/products/{handle}").text
            qty = None
            block = re.search(r'"%s"\s*:\s*\{[^{}]{0,400}?"inventory_quantity"\s*:\s*(-?\d+)' % var["id"], page)
            if block:
                qty = max(int(block.group(1)), 0)
            out.append({"title": data.get("title"), "variant": var.get("title"), "language": language_of(text),
                        "price_clp": int(var["price"]) // 100, "quantity": qty, "url": f"{base}/products/{handle}"})
    return out


def jumpseller_variants(client, base, card):
    html = client.get(f"{base}/search?q={quote_plus(query_of(card))}").text
    paths = []
    for path in re.findall(r'href="(/[a-z0-9\-]+)"', html):
        slug = re.sub(r"-\d+$", "", path.strip("/")).replace("-", " ")
        if (normalize(slug) == normalize(card)) and path not in paths:
            paths.append(path)
    out = []
    for path in paths[:6]:
        page = client.get(base + path).text
        found = re.search(r"product: '(\[.*?\])'", page)
        title = re.search(r"<title>(.*?)</title>", page, re.S)
        if not found:
            continue
        for item in json.loads(found.group(1)):
            var = item["variant"]
            names = " ".join(v["value"]["name"] for v in item.get("values", []))
            if var.get("stock", 0) <= 0 and not var.get("stock_unlimited"):
                continue
            out.append({"title": (title.group(1).strip() if title else path), "variant": names,
                        "language": language_of(names) if names else "en", "price_clp": int(item["price"]),
                        "quantity": var.get("stock"), "url": base + path})
    return out


def status_of(line, variants):
    usable = [v for v in variants if v["language"] in ("en", "es")]
    if not usable:
        return "no_stock", None
    wanted = usable if line["language"] == "any" else [v for v in usable if v["language"] == line["language"]]
    if not wanted:
        if line["language"] == "es" and "Kilo" in line["use"]:
            return "no_stock_spanish", min(usable, key=lambda v: v["price_clp"])
        return "other_language", min(usable, key=lambda v: v["price_clp"])
    enough = [v for v in wanted if v["quantity"] is None or v["quantity"] >= line["qty"]]
    best = min(enough or wanted, key=lambda v: v["price_clp"])
    if not enough:
        return "too_few", best
    if best["price_clp"] > line["unit_planned"] * (1 + PRICE_DRIFT):
        return "price_up", best
    return "ok", best


def main():
    plan_path = sorted(REPORTS.glob("purchase-plan-*.md"))[-1]
    lines = parse_plan(plan_path.read_text(encoding="utf-8"))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    client = Client()
    STOCK_DIR.mkdir(parents=True, exist_ok=True)
    progress = Progress(STOCK_DIR / f"order-{stamp}.progress.log")
    started = time.time()
    progress.log(f"{len(lines)} order lines from {plan_path.name}")
    for i, line in enumerate(lines, 1):
        kind, base = STORES[line["store"]]
        if line["store"] in BROWSER_STORES:
            line["variants"], line["status"], line["best"] = [], "read_in_browser", None
            continue
        try:
            variants = (shopify_variants if kind == "shopify" else jumpseller_variants)(client, base, line["card"])
            line["variants"] = variants
            line["status"], line["best"] = status_of(line, variants)
        except Exception as exc:  # noqa: BLE001
            line["variants"], line["status"], line["best"] = [], "error", None
            line["error"] = repr(exc)[:200]
        line["checked_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
        progress.log(f"[{i}/{len(lines)}] {line['store']}: {line['card']} -> {line['status']}  "
                     f"{Progress.eta(i, len(lines), started)}")
    (STOCK_DIR / f"order-{stamp}.json").write_text(json.dumps(lines, ensure_ascii=False, indent=1), encoding="utf-8")
    out = [f"# Live stock of the purchase order ({stamp})", "",
           f"Source: `{plan_path.relative_to(ROOT).as_posix()}`, {len(lines)} lines. Read-only, from the stores' own product data.",
           "Valid for the purchase within 24 hours.", "",
           "| Store | Card | Qty | Lang | Planned | Live (best) | Qty shown | Status | Variant | URL |", "|---|---|---|---|---|---|---|---|---|---|"]
    for line in lines:
        best = line.get("best") or {}
        out.append(f"| {line['store']} | {line['card']} | {line['qty']} | {line['language']} | {line['unit_planned']:,} | "
                   f"{best.get('price_clp', '-') if not best else format(best['price_clp'], ',')} | {best.get('quantity', '-')} | "
                   f"**{line['status']}** | {best.get('variant', '') or ''} ({best.get('language', '')}) | {best.get('url', '')} |")
    counts = {}
    for line in lines:
        counts[line["status"]] = counts.get(line["status"], 0) + 1
    out += ["", "Counts: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())), ""]
    report = REPORTS / f"stock-order-{stamp}.md"
    report.write_text("\n".join(out), encoding="utf-8")
    progress.log(f"Counts: {counts} -> {report.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
