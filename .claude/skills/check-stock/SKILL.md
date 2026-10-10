---
name: check-stock
description: Verify real, purchasable stock and current price of Magic cards in Chilean online stores. Use before any card is added to a purchase list.
argument-hint: [card-list-file]
---

Verify stock for the cards in $ARGUMENTS. A card is "in stock" only with positive evidence.

Method, in this order:
1. Store data endpoints (for example a Shopify store's product JSON, a WooCommerce store
   API). Check the exact variant's availability field and price.
2. A rendered page in the real browser (Claude in Chrome, via the `stock-verifier`
   agent): the add-to-cart control is enabled and no sold-out badge is present.
3. If neither works, mark the card UNVERIFIED. Never infer stock from search snippets,
   cached pages or static HTML text: a past chat recommended cards showing "stock [0]".

Record per card: store, URL, exact printing/condition, price in CLP, available yes/no,
and the UTC timestamp. Reject wrong printings and foil/non-foil mismatches.

Output a table and a JSON file at `data/stock/<date>.json`. Stock is perishable: results
older than the current work session must be re-verified before buying.

Read-only: never add to cart, sign in, or buy.
