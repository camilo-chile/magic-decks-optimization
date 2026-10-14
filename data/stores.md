# Store allowlist

Source: the owner, 2026-10-11. Chilean specialist shops only; all prices in CLP; never
marketplaces or private sellers. `check-stock` and the stock verifier may visit only these
domains. Price reading of the catalogs is allowed from Phase 7 (owner, 2026-10-14: read as much
as needed); stock verification stays in Phases 9-11. The order is the owner's preference; the first three have
given him good experiences and are the default choice.

| Pref | Store | Domain | Entry URL given by the owner | Shipping rule | Payment fees | Checked |
|---|---|---|---|---|---|---|
| 1 | PayToWin | paytowin.cl | https://www.paytowin.cl/ | unknown | unknown | not yet |
| 2 | Magic4Ever | magic4ever.cl | https://www.magic4ever.cl/buscador_avanzado | unknown | unknown | not yet |
| 3 | CardNexus | cardnexus.cl | https://cardnexus.cl/product-category/singles-magic/ | unknown | unknown | not yet |
| 4 | Game of Magic Singles | gameofmagicsingles.cl | https://gameofmagicsingles.cl/collections/mtg-todas-las-singles | unknown | unknown | not yet |
| 5 | Cartas Magic Sur | cartasmagicsur.cl | https://www.cartasmagicsur.cl/catalogo | unknown | unknown | not yet |
| 6 | Tienda La Comarca | tiendalacomarca.cl | https://www.tiendalacomarca.cl/collections/magic-the-gathering-singles | unknown | unknown | not yet |
| 7 | Oasis Games | oasisgames.cl | https://www.oasisgames.cl/collections/mtg-singles-instock | unknown | unknown | not yet |

## Store selection rule (owner's criterion, left to the optimizer)
- Fewer stores is better because each store adds shipping. There is no fixed cap: shipping
  is a fixed cost per store inside the optimizer, which finds the best point between the
  number of stores, shipping and the stock of each card.
- The preference order breaks ties and is the default: use stores 1-3 unless adding a
  further store lowers the total checkout cost or is the only way to get a card.
- Phase 7 fills the shipping rule (free-shipping threshold, price, region), payment fees and
  the date checked for every store used, from the stores' own pages.
