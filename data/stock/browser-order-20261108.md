# Browser stock and price read, purchase order, 2026-11-08

UTC: Part 1 started 2026-11-08T18:27Z; Part 2 ended about 18:37Z. Source: live Shopify JSON from inside the owner's Chrome (fetch from a store tab). Prices in CLP. Stock is the `available` flag of each variant; the Shopify .js endpoint gives no quantity.

## Part 1, names (scripts/browser_shopify_lookup.js)

| Store | Names searched | Names found in file | Names with no available variant |
|---|---|---|---|
| Game of Magic Singles (`data/prices/browser-gameofmagic-20261108-order.psv`) | 16 | 16 | none |
| PayToWin (`data/prices/browser-paytowin-20261108-order.psv`) | 12 | 12 | none |

Checksum (same hash function on the page copy and on the text written to the file, h = (h*31 + charCode) % 1000003): GoM 23 lines, length 2572, hash 730782; PayToWin 27 lines, length 2855, hash 613635. Both match.

## Part 2a, PayToWin full-art Mountains

Eight full-art Mountain products found (suggest + .js). Edge of Eternities: only Borderless printings found, no full-art one.

| Store | Line | Product title | Variant | Price CLP | Available | Evidence |
|---|---|---|---|---|---|---|
| PayToWin | Mountain full art | Mountain (268) (Full Art) [Battle for Zendikar] | Lightly Played Spanish | 900 | yes | .js variants |
| PayToWin | Mountain full art | Mountain (275) - Full Art [Duskmourn: House of Horror] | Lightly Played | 900 | yes | .js variants |
| PayToWin | Mountain full art | Mountain (265) (Full-Art) [Wilds of Eldraine] | Lightly Played | 900 | yes | .js variants |
| PayToWin | Mountain full art | Mountain (265) (Full-Art) [Phyrexia: All Will Be One] | Lightly Played Foil | 900 | yes | .js variants |
| PayToWin | Mountain full art | Mountain (265) (Full Art) [Battle for Zendikar] | Near Mint | 975 | yes | .js variants |
| PayToWin | Mountain full art | Mountain (266) (Full Art) [Battle for Zendikar] | Near Mint | 975 | yes | .js variants |
| PayToWin | Mountain full art | Mountain (267) (Full Art) [Battle for Zendikar] | Near Mint | 975 | yes | .js variants |
| PayToWin | Mountain full art | Mountain (269) (Full Art) [Battle for Zendikar] | Near Mint | 975 | yes | .js variants |

Other NM and LP variants of these products (not in the table): BZR 268 Near Mint Foil 1300; BZR 265 Lightly Played Foil 1800; WOE 265 Near Mint Spanish 975; Duskmourn 275 Near Mint 975 and Lightly Played Foil 900; Phyrexia 265 Near Mint 975 and Near Mint Foil 975. Moderately Played copies at 825 (BZR 265, 267, 268) are not NM or LP and are not listed.

## Part 2b, tokens

The store descriptions give the type line, the keywords and the rules text. They never give power/toughness or colour, so P/T and colour are NOT proven for any token. Status below: "keyword match" means type and keywords match, P/T unproven.

| # | Token | Store | Line | Product title | Variant | Price CLP | Available | Evidence | Match |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Elephant 3/3 green | GoM | Tarkir: Dragonstorm | Elephant // Treasure Double-Sided Token [Tarkir: Dragonstorm Tokens] | Near Mint (Elephant face) | 570 | yes (Foil also 570) | desc: Token Creature, Elephant, no abilities | keyword match, P/T unproven |
| 1 | Elephant 3/3 green | GoM | Magic Player Rewards 2001 | Elephant Token [Magic Player Rewards 2001] | Near Mint | 123400 | yes | desc: Token Creature, Elephant, no abilities | keyword match, P/T unproven, price far too high |
| 1 | Elephant 3/3 green | PayToWin | Double Masters | Elephant // Wurm (029) Double-Sided Token [Double Masters Tokens] | Lightly Played Foil | 4300 | yes | desc: Elephant face no abilities; Wurm face Deathtouch | keyword match, P/T unproven; number (029) is not the T2XM 14 requested; foil only |
| 1 | Elephant 3/3 green | PayToWin | Magic Player Rewards 2002 | Elephant Token [Magic Player Rewards 2002] | Near Mint | 91900 | yes | desc: Elephant, no abilities | keyword match, P/T unproven, price far too high |
| 2 | Assassin 1/1 black deathtouch haste | GoM | Conspiracy: Take the Crown | Assassin Token [Conspiracy: Take the Crown Tokens] | (all variants) | - | no | desc: Assassin, Deathtouch, haste | exact keywords, but sold out: Sin stock |
| 2 | Assassin 1/1 black deathtouch haste | PayToWin | - | no Assassin with deathtouch and haste found in search | - | - | - | - | Sin stock |
| 3 | Assassin 1/1 black menace | GoM | Assassin's Creed | Assassin Token [Assassin's Creed Tokens] | Near Mint | 570 | yes | desc: Assassin, Menace | keyword match, P/T unproven |
| 3 | Assassin 1/1 black menace | PayToWin | - | no Assassin with menace found | - | - | - | - | Sin stock |
| 4 | Beast 4/4 green vanilla | GoM | - | no vanilla Beast in search; Beast tokens found all have abilities (Innistrad MH, Duskmourn, Secrets of Strixhaven) | - | - | - | - | Sin stock (no vanilla match) |
| 4 | Beast 4/4 green vanilla | PayToWin | Magic Player Rewards 2004 | Beast Token [Magic Player Rewards 2004] | Lightly Played | 8300 | yes (MP 7600) | desc: Beast, no abilities | vanilla type, P/T unproven |
| 4 | Beast 4/4 green vanilla | PayToWin | Amonkhet | Beast Token ESPAÑOL [Amonkhet Tokens] | Moderately Played only | 825 | yes | desc: Beast, no abilities | vanilla type, P/T unproven, not NM or LP |
| 5 | Bird 2/2 blue flying | GoM | Ravnica Remastered | Bird Token [Ravnica Remastered Tokens] | Near Mint | 570 | yes | desc: Bird, Flying | keyword match, P/T and colour unproven |
| 5 | Bird 2/2 blue flying | GoM | Dominaria United | Bird Token (002) [Dominaria United Tokens] | Near Mint | 570 | yes | desc: Bird, Flying | keyword match, P/T and colour unproven |
| 5 | Bird 2/2 blue flying | GoM | Outlaws of Thunder Junction | Bird Token [Outlaws of Thunder Junction Tokens] | Near Mint | 570 | yes | desc: Bird, Flying | keyword match, P/T and colour unproven |
| 5 | Bird 2/2 blue flying | PayToWin | Return to Ravnica | Bird Token [Return to Ravnica Tokens] | Near Mint | 975 | yes (LP 900) | desc: Bird, Flying | keyword match, P/T and colour unproven |

## Names with no available variant

None. All 16 GoM names and all 12 PayToWin names have at least one available variant in the file.

## Notes

- Token queries: PayToWin ran 12 queries (elephant token, assassin token, beast token, bird token, elephant wurm token, elephant 3/3 token, beast 4/4 token, beast edge of eternities, bird flying token, assassin deathtouch haste token, assassin menace token, queen marchesa assassin token). Game of Magic Singles ran the same 12 queries, and two checks (conspiracy take the crown assassin token, edge of eternities commander beast token). Quantity of copies cannot be read from the store JSON; "Two copies needed" for the Elephant is not verified.
- Read-only. Nothing added to a cart, no sign-in, no form.
- Requests: no HTTP 429 seen in any Part 2 request (0 fails in each job); no line marked UNVERIFIED.
