# Phase 7 handoff (2026-10-17): where the price reading stands

Written so a fresh context can continue without the chat history.

## State
| Store | Method | Status |
|---|---|---|
| 2 Magic4Ever | `scripts/read_store_prices.py` (own API) | Done in the run of 2026-10-17 (`data/prices/20261017T0331Z.json`): 2,244 offers |
| 3 CardNexus | same script (WooCommerce Store API) | Done in that run: 3,205 offers |
| 4 Game of Magic | browser reading | Done: `data/prices/browser-gameofmagic-20261017.psv` (71 pages, 17,559 products, 365 cards, 428 lines) |
| 1 PayToWin, 7 Oasis | browser reading | **Next** (owner agreed 2026-10-17: PayToWin and Oasis first) |
| 6 La Comarca, 8 Piedra Bruja, 9 AFK Store | script retry later (slow), browser only if it fails | Pending |

The 6 Shopify stores answered HTTP 429 to the Python client (see `store-recon-2026-10-16.md`). The script is
not disguised as a browser. The owner's browser reads them without 429.

## Procedure per Shopify store (about 35k tokens each; ask the owner before each batch)
1. `mcp__claude-in-chrome__tabs_context_mcp`, open a tab, navigate to the store home.
2. Set `window.name` to the target names (lower case, `|` separated). Get them with
   `python -I -X utf8 -c "import sys; sys.path.insert(0,'scripts'); import read_store_prices as r; print('|'.join(sorted(r.targets_from_repo())))"`
   (626 names today). `window.name` survives navigation, so one tab serves all stores in turn.
3. Run `scripts/browser_shopify_reader.js` with the store's collection path (the file lists them).
4. Poll `window.__cr` (state, page, seen); each javascript_tool call times out after 45 s.
5. When `state` is `done`, build lines in the page and put them in the body with a `<pre>`, then read with
   `get_page_text` (javascript_tool output is truncated at about 3.5k characters, get_page_text is not):
   `key|bucket|handle|variant|price|title_suffix` where bucket is `nen` (English), `nes` (Spanish) or `f`
   (foil, kept only when the card has no non-foil bucket) and `title_suffix` is the title after the card name.
6. Write the lines to `data/prices/browser-<storeid>-<YYYYMMDD>.psv` with a first line
   `#STORE <id> fetched_at=<UTC> source=browser pages=N seen=N cards=N lines=N FORMAT key|bucket|handle|variant|price|title_suffix`.
   Store ids: paytowin, gameofmagic, lacomarca, oasis, piedrabruja, afkstore.
7. The owner (or Claude, offline) runs `scripts/merge_prices.py`: it merges the newest script run with every
   `browser-*.psv` into `data/prices/merged-<stamp>.json` and `.summary.txt`.

## Data-quality lessons (already handled in the code)
- Art cards ("Art Card", "Art Series") are not the playable card: excluded (`ART_CARD_RE`).
- Titles or variants in Japanese, French, etc. are excluded, and the browser reader must skip them before
  bucketing, otherwise a cheap foreign printing hides the real English price.
- Any printing is allowed (decision D6): the cheapest available variant per card wins.
- Owner rule 2026-10-17: at the same price, prefer the Spanish copy over the English one
  (`offer_rank` in `scripts/read_store_prices.py`; the optimizer must apply the same tie-break).
- Shipping is assumed 5,000 CLP per store and stays outside the budget.

## Next phases
Phase 8 needs the merged offers (and `data/cache/collection_inventory.json` after the owner scans the loose
collection and runs `scripts/build_inventory.py`): PuLP optimizer, budget curve, Artifact dashboard.
