# Cards to put back or buy at the next purchase

Cards a Phase 2 deck uses without owning them for real: loans from the owner's Standard decks (binder "Assassin's Creed")
and proxies. Each one is bought at the next purchase: a lent card goes back to the Standard deck, a real card replaces the
proxy. The entries are declared in `decks/phase2.json` (`borrowed`, with `restock: true`), so the pools and the pull list
know about them.

| Card | Printing | Language | Used by | Why | Since | Status |
|---|---|---|---|---|---|---|
| Eagle Vision | ACR 17, normal, near mint | English | Ezio | Lent from his Standard deck | 2026-10-31 | To buy at the next purchase |
| Ezio Auditore da Firenze | ACR 25, normal (the printing of the proxy; the owner may choose another) | English | Ezio (commander) | The deck plays a proxy | 2026-10-31 | To buy at the next purchase |
| Bayek of Siwa | ACR, the owner's Standard copy (printing to read when he takes it out) | English | Ezio | Automatic loan (in stock at Game of Magic Singles, about 915 CLP on 2026-10-31) | 2026-11-02 | To buy at the next purchase |
| Layla Hassan | ACR, the owner's Standard copy (printing to read when he takes it out) | English | Ezio | Automatic loan (in stock at Game of Magic Singles, about 915 CLP on 2026-10-31) | 2026-11-02 | To buy at the next purchase |
| Cover of Darkness | The owner's Standard copy | English | Ezio | Loan to evaluate, accepted 2026-11-02 (10,360 CLP, the store's only copy is an LP foil) | 2026-11-02 | To buy at the next purchase |
| Unstoppable Slasher | The owner's Standard copy | English | Ezio | Loan to evaluate, accepted 2026-11-02 (about 5,560 CLP, in stock on 2026-10-31) | 2026-11-02 | To buy at the next purchase |
| Achilles Davenport | The owner's Standard copy | English | Ezio | Loan to evaluate, accepted 2026-11-02 (about 8,680 CLP for a Spanish copy, in stock on 2026-10-31) | 2026-11-02 | To buy at the next purchase |
| Hidden Footblade | The owner's Standard copy | English | Ezio | Loan to evaluate, accepted 2026-11-02 (no stock at Game of Magic Singles on 2026-10-31) | 2026-11-02 | Waits for a restock (or a second store) |
| Overpowering Attack | The owner's Standard copy | English | Azula | Loan to evaluate, accepted 2026-11-02 (no stock at Game of Magic Singles on 2026-10-31) | 2026-11-02 | Waits for a restock |

## Rule for every purchase (owner, 2026-10-31)
When a purchase is planned at a store, check that store's live stock of every card in this table. Each card in stock is
added to the purchase order of that store (exact printing when the store has it, otherwise the closest printing in English or
Spanish, and the owner says which). The stock check follows the usual evidence rules (`check-stock` skill,
`scripts/verify_stock.py`). When a card is bought, mark it "Bought <date>, <store>" here; when it is back in the Standard
deck or replaces the proxy, remove the row and its `borrowed` entry.
