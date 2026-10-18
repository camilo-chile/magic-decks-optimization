# Moxfield hosting validation: the owner's two lists re-scored, 2026-10-18

Purpose: prove that a list hosted on the owner's Moxfield account (unlisted, created by Claude in his signed-in
Chrome, owner decision 2026-10-18) gets the same Commander Salt score as the earlier ManaBox links, and that Salt
scores exactly the text we pasted. Site scoring version: 2026.4195 (changelog of 2026-09-29, still the latest on
2026-10-18).

| Deck | Moxfield link | Salt page | Bracket | Power | Salt | Earlier (ManaBox, 2026-10-13/16) |
|---|---|---|---|---|---|---|
| Toph - owner list | `moxfield.com/decks/x2velZ9UMkyVgzyhCZ9rXw` | `details/deck/57eb4a9c05ba878d33f816e7d7ebf902` | 3 (upgraded) | **6.5** | 72.4 | 6.5, 72.4 (same) |
| Azula - owner list | `moxfield.com/decks/sDsdVt3HG0iI0zi0THvaSA` | `details/deck/b2b652820d0679a1d2713a477fed2023` | 2 (core) | **4.0** | 33.6 | 4.0, 33.8 |

Both pages now show "by camilochile" (the ManaBox pages stay "unknown author").

## Accuracy control (the protocol for every list from now on)
1. Paste plain `N Card Name` lines (set codes dropped, basics merged) in Moxfield's "Paste in List" with the
   commander picked in the dialog; the deck must show 100 cards and raise no unrecognized-name warning.
2. Submit the Moxfield link to Commander Salt; read bracket, power and salt from the deck page.
3. Press the page's "Export list" (copies the cards it scored) and compare, in a browser script and in Python, the
   SHA-256 of the sorted lines with the list file. Toph: `e6f7594574b315d1` on both sides (83 lines);
   Azula: `ea3404de6c192df1` on both sides (77 lines). The Salt export of the old ManaBox page of Azula has the same
   hash: the two Azula measurements scored the very same list.

## Finding
The power and the bracket of an identical list are stable across hosts and dates (6.5 and 4.0 twice). The salt
rating of the identical Azula list moved by 0.2 (33.8 then 33.6) with the same scoring version: do not read salt
differences below about 1 as real. Parity is judged on power, so this does not affect the plan.
