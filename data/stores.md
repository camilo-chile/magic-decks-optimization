# Store allowlist

Source: the owner, 2026-10-11. Chilean specialist shops only; all prices in CLP; never
marketplaces or private sellers. `check-stock` and the stock verifier may visit only these
domains. Price reading of the catalogs is allowed from Phase 7 (owner, 2026-10-14: read as much
as needed); stock verification stays in Phases 9-11. The order is the owner's preference; the first three have
given him good experiences and are the default choice.

| Pref | Store | Domain | Entry URL given by the owner | Shipping rule | Payment fees | Checked |
|---|---|---|---|---|---|---|
| 1 | PayToWin | paytowin.cl | https://www.paytowin.cl/ | Shopify; Chilexpress for regions; price shown at checkout | unknown | 2026-10-16 (recon) |
| 2 | Magic4Ever | magic4ever.cl | https://www.magic4ever.cl/buscador_avanzado | Jumpseller; Starken; free pickup Santiago Centro; price at checkout | unknown | 2026-10-16 (recon) |
| 3 | CardNexus | cardnexus.cl | https://cardnexus.cl/product-category/singles-magic/ | WooCommerce; free shipping over $100.000; courier Blue | unknown | 2026-10-16 (recon) |
| 4 | Game of Magic Singles | gameofmagicsingles.cl | https://gameofmagicsingles.cl/collections/mtg-todas-las-singles | Shopify; Chilexpress; price at checkout | unknown | 2026-10-16 (recon) |
| 6 | Tienda La Comarca | tiendalacomarca.cl | https://www.tiendalacomarca.cl/collections/magic-the-gathering-singles | Shopify; Bluexpress; same-day express in RM; price at checkout | unknown | 2026-10-16 (recon) |
| 7 | Oasis Games | oasisgames.cl | https://www.oasisgames.cl/collections/mtg-singles-instock | Shopify; Chilexpress, Correos, Starken; price at checkout | unknown | 2026-10-16 (recon) |
| 8 | Piedra Bruja | piedrabruja.cl | https://piedrabruja.cl/collections/single-mtg | Shopify; shipping price at checkout (assumed 5,000 CLP, outside the budget) | unknown | 2026-10-16 (recon); added by the owner, he knows the store |
| 9 | AFK Store | afkstore.cl | https://www.afkstore.cl/collections/singles-mtg | Shopify; shipping price at checkout (assumed 5,000 CLP, outside the budget) | unknown | 2026-10-16 (recon); added by the owner, he knows the store |

## Store selection rule (owner's criterion, left to the optimizer)
- Shipping is outside the budget (owner, 2026-10-16): assumed 5,000 CLP per store, reported
  separately. Fewer stores is still better as a tie-break. At most 10 stores: the owner's 6
  (below) are the preferred ones; up to 4 more only with excellent reputation evidence and a public
  JSON stock feed, and only with his OK.
- The preference order breaks ties and is the default: use stores 1-3 unless adding a
  further store lowers the total checkout cost or is the only way to get a card.
- Added 2026-10-16 by the owner: Piedra Bruja and AFK Store (public Shopify JSON). Ineko Card Shop was rejected by the owner (domain). 8 of the 10 allowed slots are taken (6 original + 2).
- Platform and catalog findings: `docs/research/store-recon-2026-10-16.md`. Shipping prices are shown only at checkout
  (except CardNexus, free over $100.000), so the owner reads them there.
- Removed by the owner on 2026-10-16: Cartas Magic Sur (no machine-readable catalog; its quick order needs a login). Candidate additions are listed in `docs/research/store-recon-2026-10-16.md`.
- Phase 7 fills the shipping rule (free-shipping threshold, price, region), payment fees and
  the date checked for every store used, from the stores' own pages.
