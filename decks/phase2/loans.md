# Loan candidates from the owner's Standard decks

Cards of his Standard decks (binder "Assassin's Creed", not scanned) that a Commander deck may borrow (owner, 2026-10-31). A loan
becomes a row of `decks/phase2/restock.md` and a `borrowed` entry of the deck in `decks/phase2.json`.

## Rules (they hold in every iteration)
1. A loan card goes to ONE deck only, never to two or more decks.
2. Two classes, read from the stores of the CURRENT iteration (`decks/phase2.json` `iteration.stores`) when the loans are
   decided:
   - AUTOMATIC: at least one of those stores has it in stock and the replacement costs under 5,000 CLP. It may be lent.
   - TO EVALUATE: the replacement costs 5,000 CLP or more, OR none of those stores has it in stock (the replacement must wait for
     a restock). A builder may propose it only with a written justification of why the deck needs it, the replacement situation
     (the price, or "no stock: wait for a restock" with any reference price known) and the fallback card it would play
     instead. The owner accepts or rejects each one, weighing the replacement cost or the wait against that need.
3. Until the owner accepts a TO EVALUATE card, the list is built with its fallback card, and the proposal is listed apart.
4. A candidate that is also in his collection is taken from the collection and needs no replacement.
5. Replacements are bought following `decks/phase2/restock.md` (when a purchase is planned in a store, the cards of that table
   in stock there are added to the order).
6. The purchase budget of an iteration (`iteration.purchase_budget_clp`) is for buying cards for the decks; it is not a loan
   limit.

## Candidates (names checked against Scryfall on 2026-10-31; the owner's spelling in parentheses when it differed)
| Card | Colors | Note |
|---|---|---|
| Eivor, Battle-Ready ("Eivor, lista para la batalla") | RW | |
| Hidden Footblade | R | He thinks it is in his collection |
| Aya of Alexandria | RW | |
| Senu, Keen-Eyed Protector | W | |
| Mjölnir, Storm Hammer ("Mjolnir") | R | |
| Split Up | W | |
| Overpowering Attack | R | |
| Enchanter's Bane ("Ruina del encantador") | R | |
| Bayek of Siwa | RW | |
| Layla Hassan | W | |
| The Spear of Leonidas | R | |
| Kassandra, Eagle Bearer | RW | |
| Bureau Headmaster ("Directora de la casa") | RW | |
| Feed the Swarm ("Alimentar al enjambre") | B | |
| Eagle Vision | U | Lent to Ezio (2026-10-31) |
| Viewpoint Synchronization | G | |
| Assassin Initiate | B | |
| Hullcarver ("Hullcaver"; {B} artifact creature Robot Assassin 1/1 with deathtouch) | B | In the collection per the owner: taken from there, no replacement needed |
| Achilles Davenport ("Aquiles Davenport") | UB | |
| Vincent, Vengeful Atoner | R | |
| Massacre Girl, Known Killer | B | |
| Basim Ibn Ishaq | UB | |
| Funeral Room // Awakening Hall | B | A Room (one-faced split card), allowed |
| Unstoppable Slasher | B | |
| Cover of Darkness | B | |
| Ballad of the Black Flag | U | |
| Propaganda | U | He also owns 2 copies outside the Standard decks (2026-10-18 export): those go first |
| Hidden Blade | C | |
| Ratonhnhaké꞉ton ("Ratonhnhake:ton") | WUB | |

Stock and prices in the stores of iteration 2: `decks/reports/loan-candidates-gom-20261031.md` (read 2026-10-31).
