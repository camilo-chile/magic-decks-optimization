# Store reconnaissance, Phase 7 step 0 (2026-10-16)

Read by hand in the owner's Chrome, one store at a time, read-only (no sign-in, no cart, no forms
other than a public search). The owner told Claude to skip the terms of service (2026-10-16), so
none were read; robots.txt was read only for the first Shopify store. All prices are CLP.

| Pref | Store | Platform | Machine-readable catalog | Price format | Stock signal | Native decklist tool | Shipping (published) |
|---|---|---|---|---|---|---|---|
| 1 | PayToWin | Shopify | `/collections/mtg-singles-instock/products.json` (public, 30 per page) | variant price in CLP, integer string | `available` true/false per variant (no quantity); the "instock" collection still lists sold-out variants | "Arma tu mazo" (`#decklist` on the home page), not tested | Chilexpress for regions, an external delivery company inside Santiago; no prices published |
| 2 | Magic4Ever | Jumpseller | **its own public API** `https://mantenedor.magic4ever.cl/api/public/search?q=<name>&limit=100&offset=0&withVariants=1` (found in the browser network log on 2026-10-17; the HTML page loads its results from it) | per variant `priceClp`, `language` (en/es), `finish`, `conditionGrade` (NM seen), `sku` | **exact stock quantity** per variant (`stock`) | none seen; server-rendered search `resultados_busqueda_avanzada?q=<name>` returns every printing (Sol Ring: 38 results) | Starken to all Chile; free pickup in Santiago Centro; no prices published |
| 3 | CardNexus | WooCommerce | WooCommerce Store API `/wp-json/wc/store/v1/products` (public) | `prices.price` with `currency_code` CLP, minor unit 0 | `is_in_stock` boolean | none seen | Free shipping over $100.000; courier Blue; otherwise no price published |
| 4 | Game of Magic Singles | Shopify | `/products.json` and `/collections/mtg-todas-las-singles/products.json` (public); about 205 product sitemaps | CLP integer string | `available` per variant; variants are conditions (NM, LP, MP, HP, Damaged), Foil and "Español" | `/pages/multi-card-search` (BinderPOS: paste a decklist, filter by condition and printing) | Chilexpress; the cost is chosen at checkout; ships the same day if ordered before noon |
| 5 | Cartas Magic Sur | custom React site on a Supabase backend | none verified (the catalog is a client app) | page shows price in CLP | "Agotado / Sin stock" on the card page; pages are `/carta/<set>-<number>-<slug>?finish=Foil` | "Pedido rápido" exists but needs a login: not used | Chilexpress, Shippit, Starken; free pickup at 2 stores in Santiago; no prices published |
| 6 | Tienda La Comarca | Shopify | `/collections/magic-the-gathering-singles/products.json` (public) | CLP integer string | `available`; variants carry Condition / Language / Printing options | none seen | Bluexpress (priority insured, 1-3 working days in RM) and same-day express delivery in RM; no prices published |
| 7 | Oasis Games | Shopify | `/collections/mtg-singles-instock/products.json` (public) | CLP integer string | `available`; variants include "Spanish" versions; some titles carry a language prefix (for example "FRENCH Wooded Foothills") | none seen | Chilexpress, Correos de Chile or Starken; dispatch in 24 to 72 working hours; no prices published |

## Findings
- 5 of 7 stores (1, 3, 4, 6, 7) publish a public JSON catalog (4 Shopify, 1 WooCommerce); all give price
  in CLP and an in-stock boolean per variant. None gives a stock quantity.
- Store 2 (Jumpseller): its HTML search results load by script, but the page calls the store's own public API (above), which returns JSON with price, language, finish, condition and exact stock per variant. Card names carry suffixes such as "(Surge Foil)" or "(Borderless)".
- Store 5 has no verified machine-readable source; its pages are per card and read one at a time.
- No store publishes shipping prices; they appear at checkout (the owner does that step) except
  CardNexus: free over $100.000.
- Shopify stores publish an agent policy in `/agents.md` (identify agent requests, back off on 429,
  no scripted checkout). A reader script should send a clear User-Agent, throttle and stop on 429.
- Shopify's `products.json` serves 30 products per page by default; the full singles catalog of store 4
  is on the order of tens of thousands of products.
- **Script run of 2026-10-17:** Magic4Ever (626 searches, 2,244 offers) and CardNexus (3,205 offers) worked. All
  6 Shopify stores answered HTTP 429 to the Python client (PayToWin after 4 pages, the rest from the first
  request) and stayed blocked for 30+ minutes. The same collection feeds read from the owner's browser
  (Claude in Chrome, by hand, 1.2 s between pages) returned 200 on every page. The script is not disguised as a
  browser. The Shopify stores are therefore read in the browser and merged by `scripts/merge_prices.py`.
- marketplace.scry.cl lists CardNexus with 0 stock while CardNexus's own API shows stock: aggregators
  are not a source.

## Update 2026-10-16 (later): owner decisions and candidate extra stores
- Cartas Magic Sur removed from the list. Shipping assumed 5,000 CLP per store and outside the budget.
- Up to 4 extra stores allowed, only with excellent reputation evidence and a public JSON stock feed,
  and the owner's OK. Web search is US-only and found no reviews of Chilean store reputations.

| Candidate | Platform and feed (checked with WebFetch, 2026-10-16) | Reputation evidence found |
|---|---|---|
| Ineko Card Shop (inekosingles.com, Iquique) | WooCommerce Store API public: price CLP, `is_in_stock` | Scry profile "Ineko Card Shop": 100% positive, 25 reviews, 27 sales, 16,858 cards (same business by name, not confirmed) |
| Piedra Bruja (piedrabruja.cl) | Shopify `collections/single-mtg/products.json`: price integer, `available` | none found |
| AFK Store (afkstore.cl) | Shopify `collections/singles-mtg/products.json` | none found |
| Bloodmoon Games (bloodmoongames.cl) | no JSON (both `/products.json` and the WooCommerce API are 404) | none found; dropped |
| mtgoasis.cl | appears to be Oasis Games' other domain (store 7) | not a new store |

Scry's directory (50 stores with 94-100% positive reviews) lists marketplace sellers, not stores with their
own site: not used. tcgmatch.cl is a marketplace: excluded.
