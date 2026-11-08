# Purchase plan, Phase 2 step 7.1 (2026-11-08, with the owner's answers of 2026-11-08)

Planner: Opus 5.5 high. One purchase order for the four decks (Azula, Toph, Ezio, Kilo) in the three stores of the iteration
(`decks/phase2.json` `iteration.stores`: Game of Magic Singles, PayToWin, Rivendel El Concilio). Nothing is bought here. The
owner's answers of 2026-11-08 (`decks/phase2/owner-decisions.md`) are applied:
- over-cap buys under about 3,000 CLP in the three stores are pre-approved;
- Arcane Denial is out, and there is no 4th store;
- Ezio buys an English Swords to Plowshares and his Spanish copy goes to Kilo;
- the Standard decks' replacements take any printing or language, the cheapest in stock.

Every price is a reading, never stock evidence: **every line needs a live stock check within 24 hours of buying (step 7.4).**

Sources (reading time, UTC):
- GoM = `data/prices/browser-gameofmagic-20261107-wishlist.psv` (2026-11-07 22:01)
- P2W = `data/prices/browser-paytowin-20261107-wishlist.psv` (2026-11-07 22:10)
- RIV = `data/prices/rivendel-20261108.psv` (2026-11-08 03:56; stock counts printed by the store)
- OC = the lead's over-cap script read of 2026-11-07/08 (scratchpad `overcap/result.txt`, **not saved in `data/prices/`**):
  the source of Narset at GoM 1,440 and Muddle the Mixture at P2W 3,000, so both are among the first lines to verify live.
- SCRY = `data/prices/scry-survey-*.psv` (scry.cl, stale cache): used only to know which store might have a card.

## 1. Summary per deck

| Deck | Inside the cap | Approved over-cap | Deck total | Swaps (in for out) | Salt (now, then expected) |
|---|---|---|---|---|---|
| Fire Lord Azula | 1,440 | 0 | **1,440** | Narset, Parter of Veils for Malcolm, the Eyes; Soul-Guide Lantern (his OWNED free Spanish EOC 143, review fix) for Dimir Locket. Talisman of Creativity DROPPED (owner, 2026-11-08): Bender's Waterskin stays | 7.2, then 7.3 measured (v2, exactly this list) |
| Toph, the First Metalbender | 2,970 | 1,440 | **4,410** | Wood Elves for Bender's Waterskin; Cultivate for Chromatic Lantern; Generous Gift for Fateful Absence (moved inside the shared cap after the DROPs); *Myriad Landscape for a Forest* | 7.0, then 7.0 measured (v2 with the first two, v3 with all four) |
| Ezio Auditore da Firenze | 570 | 3,675 | **4,245** | Golgari Signet for Deathcap Cultivator; Mind Stone and Soul-Guide Lantern DROPPED (owner, 2026-11-08): Boros Locket and Hookblade stay; *Battlefield Forge for Clifftop Retreat; Rogue's Passage for Rumble Arena; Llanowar Wastes for Jungle Shrine*; Swords to Plowshares English DRC for his Spanish FRC copy (same card); Command Tower bought Spanish C17 for his Spanish PIP copy (same card, section B) | 6.6, then **6.7 measured** (v3, with Mind Stone and the Lantern; not re-measured without them) |
| Shared cap (Azula, Toph, Ezio) | **4,980 of 5,000** | 5,115 | 10,095 | | |
| Kilo, Apogee Mind (Spanish only) | **6,800 of 7,000** | 8,100 | **14,900** | Meticulous Excavation for Chromatic Star; Volt Charge for Firebending Lesson; Prophetic Prism for Etherium Sculptor; Generous Gift for Brute Suit; Talisman of Conviction for Inspiring Overseer; Relic of Legends for Hangarback Walker; *Swords to Plowshares (Ezio's Spanish FRC 37) for Thrummingbird; Muddle the Mixture for Chain Reaction; Battlefield Forge for Path of Ancestry*; Swiftfoot Boots for Ovalchase Dragster and Command Tower (Ezio's Spanish copy) for a Mountain (both section B) | 3.8, then **4.6 measured** (v3, 2026-11-08; the Spellbook combo Meticulous Excavation + Lux Artillery + Crystalline Crawler, 1034-1350-2060), floor 4.5 met |
| **All four** | **11,780** | **13,215** | **24,995** | | |

Review of 2026-11-08 (`decks/reports/purchase-review-20261108.md`): factual fixes applied here (owned Soul-Guide Lantern for
Azula, Spanish Command Tower and Spanish full-art Mountains at the same price, the Elephant token line, stale Salt figures and
statements). Owner, 2026-11-08: the three DROPs (Talisman of Creativity, Mind Stone, Ezio's Soul-Guide Lantern) and the Chaos
Warp stock line are APPLIED (a card with no real gain is not bought).

*Italics* = approved over-cap. [J] = my judgment; expert estimates ran 0.3 to 2.1 points high in Phase 1, so only measured
scores count. Kilo's Swords costs nothing in Kilo's own list (it is Ezio's Spanish copy), but the English copy Ezio buys
(2,500) is charged to Kilo's over-cap, as the owner asked.

Bracket check of the four after-purchase lists (the `scripts/check_phase2_bracket.py` logic, reports written to the
scratchpad): all **PASS**, 100 of 100 cards recognized in each. Game Changers: Azula 1 (Narset), Toph 2 (Crop Rotation,
Drannith Magistrate), Ezio 0, Kilo 0. The flagged combos are all late: Godo + Helm of the Host (Azula), Bumi + Ashaya (Toph),
Ezio + Magister Sphinx (Ezio); Toph + The Stasis Coffin is a review item. Kilo has floor 1 and keeps the Excavation line
inside the list.

### Judgment on the swaps (the owner asked for reasons where a cut was not named or a deck could weaken)
- **Ezio, Soul-Guide Lantern for Hookblade** (cut chosen by me). Salt prints "no graveyard interaction" for Ezio, and the
  Lantern is an artifact that Loyal Inventor and Reckless Handling can find. Hookblade's job was flying for Ezio alone on
  my turn. Rogue's Passage now gives Ezio a repeatable unblockable from a land slot, so the kill still connects through a
  board. The builder had already named Hookblade as a cut (for Brotherhood Regalia). Ezio-only evasion stays covered:
  Rogue's Passage, Glider Staff, Secret Tunnel, Cover of Darkness, Angelic Intervention.
- **Ezio, Llanowar Wastes for Jungle Shrine** (the builder's pairing). A tapped land becomes an untapped one, with {B}{G}
  for freerunning and the kill's thinnest color. Red and white lose one source each. Battlefield Forge (in for Clifftop
  Retreat, same colors), Command Tower, Exotic Orchard, Path of Ancestry and Chromatic Lantern still cover them.
- **Ezio, three land swaps**: the deck stays at 36 lands with fewer tapped lands. Correction (review): Rumble Arena is NOT
  colorless for the kill: `{1}, {T}: Add one mana of any color`, a payment_enablers piece (8 to 7). After the three land
  swaps and Boros Locket out, the lands make W 11, U 12, B 12, R 10, G 7 (were 13, 13, 12, 12, 8).
- **Kilo, Muddle the Mixture for Chain Reaction** (the builder named Chain Reaction three times as the cut for a counter).
  The wipes drop from 3 to 2 (Fumigate, Organic Extinction), which is still the gate's base minimum of 2. Kilo gains a
  2-mana counter for the combo turn (Swan Song is its only other one), and the transmute finds MV-2 cards such as Talisman
  of Conviction or Pentad Prism. Muddle reads exactly 3,000; the coordinator named it, so it is included.
- **Kilo, Swords to Plowshares for Thrummingbird.** Kilo gets the best 1-mana answer (interaction is its lowest Salt
  pillar, 84/140). Thrummingbird was a 2-drop proliferator that is bad late. The proliferate pieces drop from 7 to 6, and
  Relic of Legends (an instant Kilo tap, so one more proliferate) offsets it.
- **Kilo, Battlefield Forge for Path of Ancestry**: an untapped {R}/{W} land for a tapped one (Salt's tapped-land penalty
  for Kilo is -0.38).
- **Kilo, Relic of Legends for Hangarback Walker** (step 7.1 choice, unchanged). It spends the money that the unbuyable
  Voltaic Construct frees and fills the slot the builder reserved for it. It also clears the ramp WARN (9 of 10) and adds
  an instant Kilo tap. No combo is lost, and the functions that lose Hangarback keep wide margins: counter_sources 21 of
  12, counter_payoffs 15 of 6. Correction (review): after ALL Kilo swaps through_wide_board is 12 of 10 (Hangarback,
  Thrummingbird, Inspiring Overseer and Chain Reaction all leave it), wipes 2 of 2, counter_doublers 9 + Kilo of 10.
- **Toph, Myriad Landscape for one Forest (ACR 110).** Myriad fetches two basics of one type, normally two Forests: one card
  brings three land entries, and 10 Forests stay for it to find. A Plains or a Mountain would have cost a white or red
  source.
- **Toph, Generous Gift for Fateful Absence** (the builder's pairing). Both are 2-mana instants. The Gift also answers
  artifacts, enchantments and lands, which Salt's lowest pillar for Toph (Interaction) asks for. It gives the opponent a
  3/3 Elephant token instead of a Clue.
- No two approved proposals compete for one slot: each has its own named cut.

### Left out, and why
| Proposal | Why |
|---|---|
| Arcane Denial | Owner, 2026-11-08: out (in none of the three stores; no 4th store) |
| Spanish Swords to Plowshares for Kilo | Owner, 2026-11-08: Ezio buys an English copy and gives Kilo his Spanish one |
| Lightning Greaves (Ezio, P2W 9,900) | Over the pre-approval limit of about 3,000 |
| Eladamri's Call (Toph, GoM 25,080 foil) | Over the limit |
| Game Changer tutors and the other dear cards (Mystical Tutor, Smothering Tithe, Teferi's Protection, Enlightened, Vampiric and Demonic Tutor, Bloodletter, Wound Reflection, Brotherhood Regalia, Tezzeret) | Over the limit, and most are outside the three stores |
| Notion Thief (CardNexus 2,790), Counterspell ES (CardNexus 4,090) | Not in the three stores |
| Voltaic Construct, Sorin Markov, Aura of Dominion | No stock read anywhere |

## 2. The order, store by store

Section labels: **A-cap** upgrade inside a cap; **A-over** approved over-cap; **B-loan** loan replacement
(`decks/phase2/restock.md`; any printing or language, the cheapest in stock); **B-extra** separate deck extra the owner decided;
**B-stock**; **B-basics**; **B-token**; **owed**.

### Store 1: Game of Magic Singles (GoM)

| # | Card | Deck (out) | Lang | Printing, variant | CLP | Read | Section | Fallback |
|---|---|---|---|---|---|---|---|---|
| 1 | Narset, Parter of Veils | Azula (Malcolm, the Eyes) | EN | not read (OC: EN nonfoil) | 1,440 | 2026-11-07, OC (**verify first**) | A-cap | No copy under 13,000 in the three stores (RIV: one Spanish prerelease foil). If gone, Malcolm stays |
| ~~2~~ | ~~Soul-Guide Lantern~~ | Azula (Dimir Locket) | | **Removed by the review**: he owns a FREE Spanish copy (EOC 143, Spanish Cards binder; Toph left it in step 6, no deck holds it). Azula takes it | 0 | | | |
| 3 | Wood Elves | Toph (Bender's Waterskin) | EN | HOB 142, NM | 570 | 2026-11-07 | A-cap | P2W 900 LP (7ED) |
| 4 | Golgari Signet | Ezio (Deathcap Cultivator) | EN | BLC 272, NM | 570 | 2026-11-07 | A-cap | P2W 900 LP |
| ~~5~~ | ~~Mind Stone~~ | Ezio (Boros Locket) | | **Dropped** (owner, 2026-11-08: no real gain; Boros Locket stays) | 0 | | | |
| 6 | Talisman of Conviction | Kilo (Inspiring Overseer) | **ES** | TDC 329, NM Español | 1,500 | 2026-11-07 | A-cap | None in Spanish: Inspiring Overseer stays |
| 7 | Battlefield Forge | Ezio (Clifftop Retreat) | EN | M3C 321, NM | 915 | 2026-11-07 | A-over | P2W 2,400 LP |
| 8 | Llanowar Wastes | Ezio (Jungle Shrine) | EN | C20 286, LP | 1,320 | 2026-11-07 | A-over | P2W 2,400 LP |
| ~~9~~ | ~~Soul-Guide Lantern~~ | Ezio (Hookblade) | | **Dropped** (owner, 2026-11-08: graveyard hate already covered by Abstergo Entertainment; Hookblade stays) | 0 | | | |
| 10 | Swords to Plowshares | Ezio (his Spanish FRC 37 moves to Kilo, for Thrummingbird); charged to Kilo's over-cap | EN | DRC 37, NM | 2,500 | 2026-11-07 | A-over | P2W 2,600 EN NM (BBD) |
| 11 | Eagle Vision | Loan to Ezio | EN | ACR, NM | 742 | 2026-11-07 | B-loan | P2W 1,560 |
| 12 | Bayek of Siwa | Loan to Ezio | EN | ACR Showcase, NM | 2,320 | 2026-11-07 | B-loan | P2W 2,600 |
| 13 | Layla Hassan | Loan to Ezio | EN | ACR Showcase, NM | 915 | 2026-11-07 | B-loan | P2W 2,600 |
| 14 | Unstoppable Slasher | Loan to Ezio | EN | DSK 294, NM | 5,560 | 2026-11-07 | B-loan | P2W 6,000 |
| 15 | Achilles Davenport | Loan to Ezio | ES | ACR 294, NM | 8,680 | 2026-11-07 | B-loan | none in the three stores |
| 16 | Commander's Sphere | Stock (Ezio gave his to Kilo) | EN | DMC, NM | 570 | 2026-11-07 | B-stock (recommended) | P2W 900 LP |
| 17 | Glacial Fortress | Stock (Ezio gave his to Kilo) | EN | DRC, NM | 915 | 2026-11-07 | B-stock (recommended) | P2W 2,400 LP |
| 18 | Radiant Summit | Stock (Ezio gave his to Kilo) | EN | EOC, NM | 915 | 2026-11-07 | B-stock (recommended) | none |
| ~~19~~ | ~~Chaos Warp~~ | Stock | | **Removed** (owner, 2026-11-08: he owns 2 free copies, SOC 239 EN and FIC 291 ES) | 0 | | | |
| 20 | Exotic Orchard | Stock (multicolor staple) | EN | AFC, NM | 915 | 2026-11-07 | B-stock (recommended) | P2W 2,400 LP |
| 21 | Spire of Industry | Stock | EN | MKC, NM | 1,420 | 2026-11-07 | B-stock (optional) | P2W 2,400 LP |
| 22 | Smoldering Marsh | Owed by the store (counts as owned, `pending_owned`) | ES | MSC, NM | 0 | `decks/phase2.json` | owed | Ask for it at payment; scan it on arrival and clear `pending_owned` |

### Store 2: PayToWin (P2W)

| # | Card | Deck (out) | Lang | Printing, variant | CLP | Read | Section | Fallback |
|---|---|---|---|---|---|---|---|---|
| 1 | Cultivate | Toph (Chromatic Lantern) | EN | C17 147, LP | 900 | 2026-11-07 | A-cap | GoM 1,200 NM |
| 2 | Generous Gift | Kilo (Brute Suit) | **ES** | WOC 68, NM Spanish | 2,100 | 2026-11-07 | A-cap | None in Spanish: Brute Suit stays |
| ~~3~~ | ~~Talisman of Creativity~~ | Azula (Bender's Waterskin) | | **Dropped** (owner, 2026-11-08: no real gain; Waterskin stays) | 0 | | | |
| 4 | Rogue's Passage | Ezio (Rumble Arena) | EN | CMM 426, LP | 1,440 | 2026-11-07 | A-over | none in GoM or RIV: Rumble Arena stays |
| 5 | Myriad Landscape | Toph (one Forest ACR 110) | EN | KHC 115, LP | 1,440 | 2026-11-07 | A-over | none: the Forest stays |
| 6 | Generous Gift | Toph (Fateful Absence) | EN | CMM 624 borderless, NM | 1,500 | 2026-11-07 | A-cap (inside the shared cap after the DROPs) | GoM 2,000 NM (MOC) |
| 7 | Muddle the Mixture | Kilo (Chain Reaction) | **ES** | printing not read | 3,000 | 2026-11-07, OC (**verify**) | A-over | none in Spanish in GoM or RIV: Chain Reaction stays |
| 8 | Battlefield Forge | Kilo (Path of Ancestry) | **ES** | BRO 257, NM Spanish | 2,600 | 2026-11-07 | A-over | none in Spanish: Path stays |
| 9 | Cover of Darkness | Loan to Ezio | EN | ACR, NM | 10,500 | 2026-11-07 | B-loan | GoM 10,760 LP foil |
| 10 | Hidden Footblade | Loan to Ezio | EN | ACR 34, LP | 1,440 | 2026-11-07 | B-loan | P2W 1,560 NM foil |
| 11 | Overpowering Attack | Loan to Azula | EN | ACR 37, LP foil (the cheapest) | 1,440 | 2026-11-07 | B-loan | P2W 1,560 NM |
| 12 | Swiftfoot Boots | Kilo (Ovalchase Dragster), owner's extra | **ES** | C14 275, LP Spanish | 2,200 | 2026-11-07 | B-extra | GoM 3,280 ES |
| 13 | Command Tower | Ezio (his Spanish PIP 259 goes to Kilo for a Mountain) | **ES** (review fix: same price as EN CMR 350, Spanish wins; the builder's own pick) | C17 242, LP Spanish | 900 | 2026-11-07 | B-extra | P2W 900 EN CMR 350 LP; GoM 1,200 EN |
| 14 | Mountain, full art, x3 | Free full-art basics (3 short of 10) | **ES** (review fix: same price as the EN DSK, Spanish wins) | BFZ 268 full art, LP Spanish, all three the same printing | 2,700 (3 x 900) | 2026-11-07 | B-basics | If fewer than 3 Spanish BFZ 268: 3 x DSK 275 full art EN LP at 900 (one printing). No Edge of Eternities full-art Mountain was read in the three stores |
| 15 | Elephant token (3/3 green) x2 | For the two Generous Gifts (Toph, Kilo); not in his collection's tokens | any | Elephant // Wurm double-sided token, Double Masters tokens (Elephant face = Scryfall T2XM 14, 3/3 green, no abilities: matches the Generous Gift token TMSC 28) | about 4,400 (2 x 2,200, search "from" price read 2026-11-08; variant price and quantity NOT read: HTTP 429) | 2026-11-08, search only | B-token | "Sin stock" if not 2 in stock. GoM's Elephant // Treasure (TDM tokens) is a 5/5 Elephant: wrong token |
| 16 | Arcane Signet | Stock (staple of all four decks) | EN | NEC, NM | 975 | 2026-11-07 | B-stock (recommended) | GoM 1,000 ES |
| 17 | Beast Within | Stock | EN | LCC, LP | 1,440 | 2026-11-07 | B-stock (optional) | none |
| 18 | Fellwar Stone | Stock | EN | ECC, NM | 1,560 | 2026-11-07 | B-stock (optional) | none |
| 19 | Pull from Tomorrow | Stock (Kilo gave his to Azula) | ES (same price as EN) | AKH, LP | 2,400 | 2026-11-07 | B-stock (optional) | none |

### Store 3: Rivendel El Concilio (RIV)

| # | Card | Deck (out) | Lang | Printing, variant | CLP | Read | Section | Fallback |
|---|---|---|---|---|---|---|---|---|
| 1 | Meticulous Excavation | Kilo (Chromatic Star) | **ES** | BRO 16, 16 in stock | 300 | 2026-11-08 | A-cap | No other Spanish copy in the three stores: without it Chromatic Star stays and Kilo has no combo |
| 2 | Volt Charge | Kilo (Firebending Lesson) | **ES** | ONE 155, 14 in stock | 200 | 2026-11-08 | A-cap | GoM 400 ES |
| 3 | Prophetic Prism | Kilo (Etherium Sculptor) | **ES** | ONE 238, 6 in stock | 200 | 2026-11-08 | A-cap | RIV WOE 249 (3); GoM 400 ES |
| 4 | Relic of Legends | Kilo (Hangarback Walker) | **ES** | DMU 236, 3 in stock | 2,500 | 2026-11-08 | A-cap | Hangarback Walker stays |
| 5 | Thirst for Knowledge | Stock (Kilo has the Spanish copy; Azula wanted one) | ES | CMR 103, 2 in stock | 300 | 2026-11-08 | B-stock (recommended) | RIV 400 ES (9) |
| 6 | Mystic Monastery | Stock (Ezio gave his to Kilo) | ES | TDM 262, 3 in stock | 600 | 2026-11-08 | B-stock (recommended) | GoM 742 EN |

The RIV printings come from its product paths, whose numbers match Scryfall collector numbers. Read the set name on the
product page at step 7.4.

Tokens (Scryfall `all_parts`, read 2026-11-08, for every card in this plan): only Generous Gift makes a token (a 3/3 green
Elephant for the controller of the destroyed permanent). His Tokens binder has none. No other bought card makes tokens or
emblems.

No spare Swords to Plowshares is recommended: Kilo, Ezio and Toph (his Spanish EOC 45) each have a copy; Azula plays none.
(Review correction: Toph does play one.)

## 3. Totals (CLP)

| Block | GoM | P2W | RIV | Total |
|---|---|---|---|---|
| A inside cap, shared 5,000 (Azula 1,440, Toph 2,970, Ezio 570) | 2,580 | 2,400 | 0 | **4,980** |
| A inside cap, Kilo 7,000 | 1,500 | 2,100 | 3,200 | **6,800** |
| A approved over-cap, Azula | 0 | 0 | 0 | **0** |
| A approved over-cap, Toph (Myriad Landscape) | 0 | 1,440 | 0 | **1,440** |
| A approved over-cap, Ezio (Battlefield Forge, Llanowar Wastes, Rogue's Passage) | 2,235 | 1,440 | 0 | **3,675** |
| A approved over-cap, Kilo (Swords for Ezio's swap, Muddle, Forge) | 2,500 | 5,600 | 0 | **8,100** |
| **Section A** | 8,815 | 12,980 | 3,200 | **24,995** |
| B loans (8) | 18,217 | 13,380 | 0 | 31,597 |
| B extras (Swiftfoot Boots ES, Command Tower ES) | 0 | 3,100 | 0 | 3,100 |
| B basics (3 full-art Mountains) | 0 | 2,700 | 0 | 2,700 |
| B stock, recommended (7; Chaos Warp removed) | 3,315 | 975 | 900 | 5,190 |
| B tokens (2 Elephants; not in the totals until the variant price is read) | | about 4,400 | | about 4,400 |
| Owed (Smoldering Marsh) | 0 | | | 0 |
| **Section B** | 21,532 | 20,155 | 900 | **42,587** |
| **Cards** | **30,347** | **33,135** | **4,100** | **67,582** |
| Shipping (assumed 5,000 per store, outside every budget) | 5,000 | 5,000 | 5,000 | **15,000** |
| **Grand total** | **35,347** | **38,135** | **9,100** | **82,582** |
| Grand total with the 2 Elephant tokens at the search price | 35,347 | 42,535 | 9,100 | about 86,982 |
| B stock, optional (4, not in the totals): Spire of Industry, Beast Within, Fellwar Stone, Pull from Tomorrow | 1,420 | 5,400 | 0 | 6,820 |

Section B by type: loans 31,597 (Cover of Darkness and Achilles Davenport are 61 % of it); extras 3,100; basics 2,700;
recommended stock 5,190; tokens about 4,400 (search price, to read).

## 4. Lines once planned at Tienda La Comarca (replaced by Rivendel El Concilio on 2026-11-08)

| Card (deck) | La Comarca plan | Now |
|---|---|---|
| Relic of Legends (Kilo) | 2,600 ES | RIV 2,500 ES |
| Meticulous Excavation (Kilo) | price to read | RIV 300 ES |
| Narset (Azula, fallback) | 1,850 EN | GoM 1,440 main line; **no fallback under 13,000 in the three stores** |
| Soul-Guide Lantern (Azula) | 700 | GoM 742 |
| Wood Elves (Toph, alternative) | 450 | GoM 570 |
| Talisman of Creativity (Azula) | 3,350 ES | P2W 2,100 EN |
| Muddle the Mixture (Kilo) | 3,350 ES | P2W 3,000 ES |
| Arcane Denial (all) | 3,950 | **Out** (owner, 2026-11-08) |
| Tezzeret the Seeker (Kilo) | 34,800 ES foil | **Out** (over the limit, not in the three stores) |

## 5. Step 7.4 checklist (live stock within 24 hours of buying)
- Every line: all readings are, or will be, over 24 hours old when he buys (RIV's turns 24 hours old at 2026-11-09 03:56 UTC).
- First, the lines from the unsaved OC read: Narset (GoM) and Muddle the Mixture ES (P2W).
- Lines with one source and no fallback card: Meticulous Excavation, Talisman of Conviction ES, Generous Gift ES, Muddle ES,
  Battlefield Forge ES, Rogue's Passage, Myriad Landscape, Achilles Davenport. If one fails, its
  stand-in stays in the list (column "Fallback").
- Quantities: no Soul-Guide Lantern to buy (Azula takes his owned copy; Ezio's was dropped); 3 copies of one full-art Mountain printing
  at P2W (Spanish BFZ 268 first); 2 Elephant // Wurm tokens at P2W (variant price and quantity unread).
- Muddle the Mixture: pre-approval is "under about 3,000"; if the live price is over 3,000, ask the owner.
- Smoldering Marsh: confirm GoM includes it in this order.

## 6. Open questions for the owner
1. Stock cards: the owner approved the recommended ones; Chaos Warp removed (7 left, 5,190). Any of the 4 optional (6,820)?

## 7. After-purchase lists (Moxfield paste format)

Built from `decks/phase2/moxfield/<slug>.txt` (exact owned printings) with every swap in section 1: 100 cards each, "//
Commander" header, bought cards with set and number where the store's printing is known (Narset and Muddle by name):
- `decks/phase2/moxfield/fire-lord-azula-after-purchases.txt`
- `decks/phase2/moxfield/toph-the-first-metalbender-after-purchases.txt`
- `decks/phase2/moxfield/ezio-auditore-da-firenze-after-purchases.txt`: Smoldering Marsh written as (MSC) 266, Scryfall's
  regular MSC number; the base file now lists it by name only. Confirm the number when the card arrives. The proxy
  commander stays: the real Ezio waits for the normal printing.
- `decks/phase2/moxfield/spanish-deck-after-purchases.txt`: every card a Spanish copy (the bought ones, plus Ezio's Spanish
  Swords to Plowshares FRC 37 and Command Tower PIP 259).

Moxfield's paste format holds set, number and foil, not language: set the Spanish cards' language by hand after the import.
The deck files `decks/phase2/<slug>.txt`, `.plan.json` and `.build.md` were not edited. When the cards arrive and are
scanned: update `decks/phase2/restock.md` (bought rows marked) and clear the `borrowed` and `pending_owned` entries.
