# Cards to put back or buy at the next purchase

Cards a Phase 2 deck uses without owning them for real: loans from the owner's Standard decks (binder "Assassin's Creed")
and proxies. Each one is bought at the next purchase: a lent card goes back to the Standard deck, a real card replaces the
proxy. The entries are declared in `decks/phase2.json` (`borrowed`, with `restock: true`), so the pools and the pull list
know about them.

**Closed (owner, 2026-11-14): no more purchases.** The purchase of 2026-11-09 replaced every loan (Eagle Vision, Bayek of
Siwa, Layla Hassan, Unstoppable Slasher, Hidden Footblade, plus the new Basim Ibn Ishaq and Aya of Alexandria); the lent copies
went back to the Standard decks. Cover of Darkness, Achilles Davenport and Overpowering Attack left the lists in the final
rebuild and went back unreplaced. The history of this table is in version control.

| Card | Printing | Language | Used by | Why | Since | Status |
|---|---|---|---|---|---|---|
| Ezio Auditore da Firenze | ACR 25 (the proxy's printing) | English | Ezio (commander) | The deck plays a proxy | 2026-10-31 | Stays a proxy: no more purchases (his friends allow proxy commanders) |

## Rule for every purchase (owner, 2026-10-31)
When a purchase is planned at a store, check that store's live stock of every card in this table. Each card in stock is
added to the purchase order of that store (exact printing when the store has it, otherwise the closest printing in English or
Spanish, and the owner says which). The stock check follows the usual evidence rules (`check-stock` skill,
`scripts/verify_stock.py`). When a card is bought, mark it "Bought <date>, <store>" here; when it is back in the Standard
deck or replaces the proxy, remove the row and its `borrowed` entry.
