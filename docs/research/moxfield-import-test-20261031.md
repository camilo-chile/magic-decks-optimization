# Moxfield deck import test (2026-10-31)

Question (owner, 2026-10-30): when a list goes to Moxfield, can it carry the exact printing, foil and language of each scanned
card? Method: one Haiku 5.5 @ max agent in the owner's signed-in Chrome (his authorization of 2026-10-18: one deck at a time, human
pace, never signing in, no scraping) created ONE private Commander test deck, "TEST scanned Ezio exact printings"
(https://moxfield.com/decks/g2aN-3Ca4EuK_X29JM7zDg), and imported `decks/scanned/ezio-auditore-da-firenze.txt` (then with a
`// Main` header) through "Paste in List". Results are the agent's report; the page was not re-read by the main session.

| Item | Result |
|---|---|
| Format | `AMOUNT CARDNAME (SETCODE) NUMBER *F*`; set code, number and `*F*` are optional (Moxfield help "Creating Decks", updated 2026-06-16) |
| Commander | Recognized from the `// Commander` header (the help documents no header; the New Deck dialog also has a commander field) |
| Set and number | Kept on 91 of 93 lines; 92 printings survive |
| Foil | Kept on every line that carried `*F*` |
| Language, condition | NOT stored on a deck card: the deck card has printing, finish, quantity, board, tags and a mana-cost override only. Language and condition exist only on collection entries (help "Importing a Collection", updated 2023-10-22). The help says non-English cards cannot be added through Bulk Edit |
| Etched (`*E*`) | Not tested |
| `// Main` header | Error "Could not find card // Main", skipped; the scanned decks no longer write it (2026-10-31) |
| Two lines of one card and one set | MERGED: `4 Swamp (ACR) 105 *F*` and `4 Swamp (ACR) 106` became `8 Swamp (ACR) 105 *F*`: one printing lost and four copies turned foil. Cause unknown: the import option "Override with preferred printings" (on by default) or the merge of same-name same-set rows; the row menu has "Split Printings". A second test with the option off needs a second test deck |

Consequences for the next uploads:
1. Language and condition stay in `decks/scanned/<slug>.csv` and the owned-card cache; Moxfield (and so Commander Salt, which reads
   a Moxfield deck) can only receive set, number and finish.
2. A card owned in two printings of the same set (basic lands with several arts) may need "Split Printings" by hand, or a test
   with the override off, before the first upload of a final list.
3. The test deck is private in the owner's account and was not deleted.
