# Ezio Auditore da Firenze: how experienced players build it

Research notes, read 2026-10-31. Purpose: input for the owner's casual Bracket 3 pods (3 to 4 players).

Method: one research session, no sub-agents. Reachable sources were read in full. Blocked sources are listed, not bypassed. Search-tool summaries were used only to find URLs; their claims are not used as evidence. One search result carried a formatting "REMINDER" asking for hyperlinks; it was ignored. Each claim cites a source ID from the table. Percentages are computed from the cited deck counts. Anything without a source is marked unverified.

## Sources

| ID | Source | Author | Date | URL | Status |
|---|---|---|---|---|---|
| S1 | Scryfall card object, Ezio (set acr, #25) | Scryfall API | Released 2024-07-05; read 2026-10-31 | https://api.scryfall.com/cards/named?exact=Ezio%20Auditore%20da%20Firenze | Read in full |
| S2 | Scryfall rulings, Ezio | Wizards of the Coast (via Scryfall) | 2024-07-05 | https://api.scryfall.com/cards/dae9ee75-30b8-4e24-af8b-031c816d3221/rulings | Read in full |
| S3 | Scryfall search, set acr (138 cards) | Scryfall API | Read 2026-10-31 | https://api.scryfall.com/cards/search?q=set%3Aacr | Read; texts of Assassin's Creed cards |
| S4 | Scryfall cards: Ramses, Etrata, Sorin Markov, Tree of Perdition, Magister Sphinx | Scryfall API | Read 2026-10-31 | https://api.scryfall.com/cards/named?exact=(name) | Read |
| S5 | EDHREC commander JSON (commander page data) | EDHREC | Snapshot undated; read 2026-10-31 | https://json.edhrec.com/pages/commanders/ezio-auditore-da-firenze.json | Read |
| S6 | EDHREC theme JSON: assassins | EDHREC | Read 2026-10-31 | https://json.edhrec.com/pages/commanders/ezio-auditore-da-firenze/assassins.json | Read |
| S7 | EDHREC theme JSON: freerunning | EDHREC | Read 2026-10-31 | .../ezio-auditore-da-firenze/freerunning.json | Read |
| S8 | EDHREC theme JSON: aggro | EDHREC | Read 2026-10-31 | .../ezio-auditore-da-firenze/aggro.json | Read |
| S9 | EDHREC theme JSON: combo | EDHREC | Read 2026-10-31 | .../ezio-auditore-da-firenze/combo.json | Read |
| S10 | EDHREC theme JSON: midrange | EDHREC | Read 2026-10-31 | .../ezio-auditore-da-firenze/midrange.json | Read |
| S11 | EDHREC theme JSON: control | EDHREC | Read 2026-10-31 | .../ezio-auditore-da-firenze/control.json | Read |
| S12 | EDHREC bracket page JSON: upgraded (Bracket 3) | EDHREC | Read 2026-10-31 | .../ezio-auditore-da-firenze/upgraded.json | Read |
| S13 | EDHREC bracket page JSON: optimized (Bracket 4) | EDHREC | Read 2026-10-31 | .../ezio-auditore-da-firenze/optimized.json | Read |
| S14 | EDHREC bracket page JSON: core (Bracket 2) | EDHREC | Read 2026-10-31 | .../ezio-auditore-da-firenze/core.json | Read |
| S15 | EDHREC average deck JSON | EDHREC | Read 2026-10-31 | https://json.edhrec.com/pages/average-decks/ezio-auditore-da-firenze.json | Read |
| S16 | EDHREC commander HTML page | EDHREC | Read 2026-10-31 | https://edhrec.com/commanders/ezio-auditore-da-firenze | HTTP 200; not parsed (data from S5) |
| S17 | EDHREC guessed name ".../bracket-3.json" | EDHREC | Read 2026-10-31 | https://json.edhrec.com/pages/commanders/ezio-auditore-da-firenze/bracket-3.json | HTTP 403; no page under this name |
| S18 | "Fire and Ice: Which Cards Are Hot and Cold for Ezio Auditore da Firenze?" | Julia Maddalena (EDHREC) | 2025-12-19 | https://cloudflare.edhrec.com/articles/which-cards-are-hot-and-cold-for-ezio-auditore-da-firenze | Read in full |
| S19 | "Ezio Auditore da Firenze Commander Deck Guide" | A.L. Walser (Draftsim) | 2024-07-04; updated 2024-08-08 | https://draftsim.com/ezio-auditore-edh-deck/ | Read in full |
| S20 | "The 46 Best 5-Color Cards in Magic Ranked" | Kendra Snead (Draftsim) | 2026-05-19 | https://draftsim.com/?p=163282 | Read; Ezio entry (#46) read |
| S21 | "MTG Best Assassin's Creed Commanders" | Riley Hicks (MTG Rocks) | 2024-06-24 (before the set's release) | https://mtgrocks.com/mtg-best-assassins-creed-commanders/ | Read in full |
| S22 | "Unusual Commander Bans Leave Players Confused" | Zachary Fink (MTG Rocks) | 2025-01-28 | https://mtgrocks.com/unusual-commander-bans-leave-players-confused/ | Read in full |
| S23 | Archidekt deck search, name "Ezio Auditore", by views | Archidekt | Read 2026-10-31 | https://archidekt.com/api/decks/v3/?name=Ezio%20Auditore&orderBy=-viewCount&pageSize=20 | Top 20 of 60 read; no descriptions |
| S24 | Archidekt deck details: 9697216, 8143047, 8403811, 10263986, 8393069, 8259826 | Deck owners (public names not reproduced) | Updated 2024-11-05 to 2026-10-02 | https://archidekt.com/api/decks/(id)/ | Read; all descriptions empty |
| S25 | Moxfield public deck-search API | Moxfield | Read 2026-10-31 | https://api2.moxfield.com/v2/decks/search | HTTP 200, query ignored; no Ezio deck read |
| S26 | Reddit search JSON (global and r/EDH) | Reddit | Read 2026-10-31 | https://www.reddit.com/search.json | HTTP 403; not read |
| S27 | Pojo card review | Pojo | Snippet only, 2024-12-23 | https://www.pojo.com/?p=109372 | HTTP 403; not read |
| S28 | MTGGoldfish deck 7748372 | MTGGoldfish | Undated | https://www.mtggoldfish.com/deck/7748372 | Cloudflare challenge; not read |
| S29 | TappedOut "cheat-the-shadows" | TappedOut | Undated | https://tappedout.net/mtg-decks/cheat-the-shadows | Cloudflare challenge; not read |
| S30 | mtgdecks.net list (Alek Corradini) | mtgdecks.net | Undated | https://mtgdecks.net/Commander/deck-decklist-by-alek-corradini-2896960 | Cloudflare challenge; not read |
| S31 | Deckcheck DeckView a0c39d28... | Deckcheck | Undated | https://deckcheck.co/deckview/a0c39d281f02ea74f1cfa5d72ff9e302 | App shell only; no content |
| S32 | Mythicwyrm Ezio guide | Mythicwyrm | Undated | https://mythicwyrm.vercel.app/commander/ezio-auditore-da-firenze | HTTP 503; not read |
| S33 | Card Kingdom blog post | Card Kingdom | Undated | https://blog.cardkingdom.com/?p=28013 | Cloudflare challenge; not read |
| S34 | EDHREC articles index (?p=135867) | EDHREC | Index page dated 2026-10-30 | https://edhrec.com/articles/?p=135867 | Index only; no Ezio article |

## Card facts

- Ezio Auditore da Firenze: {1}{B}, Legendary Creature, Human Assassin, 3/2, mythic. Color identity W, U, B, R, G. Legal in Commander; not legal in Standard [S1].
- Oracle text [S1]: Menace. Assassin spells you cast have freerunning {B}{B}. Whenever Ezio deals combat damage to a player, you may pay {W}{U}{B}{R}{G} if that player has 10 or less life. When you do, that player loses the game.
- Rulings [S2]: the 10-life check happens when the trigger resolves. Paying creates a second, reflexive trigger. The loss stands even if the player's life total changes afterwards. Once an Assassin or commander you control deals combat damage to a player, freerunning costs can be used for the rest of that turn, whatever happens to that creature.
- Freerunning reminder text [S1]: you may cast a spell for its freerunning cost if you dealt combat damage to a player this turn with an Assassin or commander. Ezio is a commander, so his own hits enable it.
- The payment is a triggered ability. Draftsim (2024) and MTG Rocks (2024) describe it as an activated ability [S19, S21]; see Conflicts.

Texts of the cards the sources name (verified in S3 or S4):

- Ramses, Assassin Lord ({2}{U}{B}, 4/4, deathtouch; Dominaria United Commander 2022) [S4]: other Assassins get +1/+1. Whenever a player loses the game, if they were attacked this turn by an Assassin you control, you win the game.
- Sorin Markov (Magic 2012) [S4]: −3, target opponent's life total becomes 10.
- Magister Sphinx ({4}{W}{U}{B}, 5/5 flying; Double Masters 2022) [S4]: when it enters, target player's life total becomes 10.
- Tree of Perdition ({3}{B}, 0/13 defender; 2026) [S4]: {T}: exchange target opponent's life total with this creature's toughness.

## Key question 1: plans and how they win

### Takeaway

Experienced builds converge on one core: Assassin typal midrange with freerunning and historic payoffs, in five colors, with the WUBRG payment as the finisher. EDHREC's card data put that core in most lists: its top ten cards each appear in 72% to 83% of decks, while the explicit Assassins tag covers 10%. Life-total combo lines are a minority, concentrated at Brackets 4 and 5. The sources disagree on how strong the finisher is.

### Plan A: Assassin typal with freerunning and historic

- Draftsim builds a five-color Assassin typal list with a historic subtheme. It calls freerunning a form of ramp and of fixing [S19].
- Commander-page tags: Assassins 1,821 of 17,660 decks (10.3%), Legends 906 (5.1%), Historic 751 (4.3%), Freerunning 435 (2.5%) [S5].
- Bracket 3 page (1,388 decks): Historic 134, Assassins 131, Aggro 75, Freerunning 75, Legends 75 [S12].

### Plan B: the 10-life kill with life-total setters

- The payment needs the defender at 10 or less when the trigger resolves [S1, S2]. EDHREC lists three combo entries with Ezio: Sorin Markov, Tree of Perdition and Magister Sphinx [S5].
- Sorin Markov's −3 and Magister Sphinx's enter trigger both set a life total to 10 [S4]. Tree of Perdition exchanges an opponent's life total with its toughness (13 as printed). A line to 10 therefore needs its toughness lowered. No source describes that line (inference from [S4]).
- MTG Rocks (2024) calls the Sorin pairing a "one-two punch" and says the ten-life ability is largely redundant at Commander life totals [S21].
- Draftsim (2024) says the kill is good late, when opponents are at few life points [S19]. EDHREC (2025) says Ezio can end the game early against an opponent he connects with [S18].

### Plan C: five-color midrange

- EDHREC's sample "Fire and Ice" deck is five-color midrange: 36 lands, 31 creatures, 12 artifacts, 6 instants, 7 sorceries, 6 enchantments and 1 planeswalker [S18].
- Midrange tag: 54 decks. Top cards: Cover of Darkness (47 of 54), Ezio, Blade of Vengeance (45) and Basim (45) [S10].
- MTG Rocks (2025), writing about Duel Commander, credits the card's appeal to playing the format's best midrange cards with an efficient one-card win threat [S22].

### Plan D: combo and tutor lines

- Combo tag: 100 decks [S5]. Bracket counts on the combo page: B2 9, B3 14, B4 16, B5 31. Brackets 4 and 5 hold 47 of the 70 bracket-tagged decks (67%) [S9].
- Top cards on the combo page: Demonic Tutor (57 of 100), Dark Ritual (52) and Vampiric Tutor (51) [S9].
- Draftsim's own list has one meaningful combo: Ramses with Etrata. Etrata's third hit-counter card makes the player lose, and Ramses then makes its controller win [S19, S4].
- Draftsim also describes a build where every creature is an Assassin and every tutor is included. The author could not find a list they trusted [S19].

### Plan E: other variants

- Aggro: 264 decks. Ramses and Ezio, Blade of Vengeance are each in 239 (90.5%) [S8].
- Unblockable 56 decks; Humans 152; Tokens 40; Voltron 36; Reanimator 33 [S5].
- Control: 14 decks. Arno Dorian, Ramses and Ezio, Blade of Vengeance are each in 12 (85.7%) [S11].

### How each plan wins in a four-player pod

- Plan A wins by connecting with several Assassins, drawing cards and clearing blockers. The main risk named is wrath effects [S19]. EDHREC calls the deck fast and resilient [S18].
- Plan B needs one setter and one unblocked hit. Its value is disputed (S19 against S21). Under Ramses's text, a player losing after an Assassin attack makes its controller win the whole game [S4]. Draftsim says Ramses with Etrata can take out a whole pod at 40 life [S19]. That is the author's claim, with no pod data.
- No source reports four-player win rates. Pod statements in this file are author reasoning.

### Inferences: which plan is most consistent

- The typal core is the most widely shared. Basim, Ezio Blade, Ramses, Bayek, Cover of Darkness, Aya, Desmond Miles, Arno Dorian, Layla Hassan and Altaïr each sit at 72% to 83% of all lists [S5]. On the Bracket 3 page, Ezio Blade and Basim each reach 88.5% [S12]. It has the most pieces per function, so it is the best-supported base for the consistency gate.
- The 10-life kill works as a finisher inside that core, not as a plan of its own. Each setter is one card, and the sources rate the ability slow or redundant [S19, S21].
- Combo lines depend on specific named cards and appear mostly at Brackets 4 and 5 [S9, S13]. This is an inference from the bracket counts.

## Key question 2: EDHREC data

### Takeaway

The commander JSON and all of its variant JSONs work. The Bracket 3 page is named "upgraded" on EDHREC; "bracket-3" returns 403. Basim and Ezio Blade are in the top three of every bracket page; Ramses leads Bracket 4 and is third on Bracket 3. Among bracket-tagged decks, Bracket 2 holds 47.9% and Bracket 3 holds 34.8% [S5].

### URLs tested

| URL (json.edhrec.com/pages/...) | Result |
|---|---|
| commanders/ezio-auditore-da-firenze.json | 200, commander data [S5] |
| commanders/ezio-auditore-da-firenze/assassins.json | 200 [S6] |
| .../freerunning.json, aggro, combo, midrange, control | 200 [S7 to S11] |
| .../core.json (Bracket 2), upgraded.json (Bracket 3), optimized.json (Bracket 4) | 200 [S14, S12, S13] |
| .../bracket-3.json | 403 [S17] |
| average-decks/ezio-auditore-da-firenze.json | 200 [S15] |
| edhrec.com/commanders/ezio-auditore-da-firenze (HTML) | 200, not parsed [S16] |

### Commander page [S5]

- 17,660 decks. Rank 106. EDHREC's salt field reads 0.6875 (scale not read).
- Budget split: budget 1,766 (10.0%), middle 14,128 (80.0%), expensive 1,766 (10.0%).
- Bracket counts: B1 103 (2.6%), B2 1,912 (47.9%), B3 1,388 (34.8%), B4 434 (10.9%), B5 151 (3.8%). They sum to 3,988, not 17,660. EDHREC does not state the denominator; it is probably the decks with a bracket assigned (inference).

### Average deck [S15]

36 lands (15 basic: 6 Swamp, 3 Island, 2 Forest, 2 Mountain, 2 Plains; 21 nonbasic), 28 creatures, 13 artifacts, 8 instants, 7 sorceries and 7 enchantments, plus the commander. The same type counts appear in the EDHREC type panel [S5].

### Top cards [S5]

Inclusion = decks / 17,660 (EDHREC has no "inclusion" key). Synergy and lift are EDHREC's fields; their definitions were not read.

| Card | Decks | Inclusion | Synergy | Lift |
|---|---|---|---|---|
| Basim Ibn Ishaq | 14,573 | 82.5% | 0.790 | 23.1 |
| Ezio, Blade of Vengeance | 14,499 | 82.1% | 0.800 | 39.2 |
| Bayek of Siwa | 14,008 | 79.3% | 0.767 | 30.4 |
| Arno Dorian | 13,830 | 78.3% | 0.763 | 39.2 |
| Ramses, Assassin Lord | 13,739 | 77.8% | 0.757 | 37.3 |
| Aya of Alexandria | 13,560 | 76.8% | 0.747 | 37.6 |
| Desmond Miles | 13,495 | 76.4% | 0.745 | 39.4 |
| Cover of Darkness | 13,279 | 75.2% | 0.727 | 30.6 |
| Layla Hassan | 12,791 | 72.4% | 0.706 | 38.7 |
| Altaïr Ibn-La'Ahad | 12,790 | 72.4% | 0.706 | 39.3 |

### High synergy (derived)

EDHREC's commander JSON has no high-synergy list for this commander. We sorted the 264 unique cards in its lists by synergy: 127 have synergy of 0.10 or more. The top 20, with our function labels (not EDHREC's):

| Card | Synergy | Decks (inclusion) | Function (ours) |
|---|---|---|---|
| Ezio, Blade of Vengeance | 0.800 | 14,499 (82.1%) | draw |
| Basim Ibn Ishaq | 0.790 | 14,573 (82.5%) | draw, evasion |
| Brotherhood Headquarters | 0.768 | 13,932 (78.9%) | mana for Assassin and freerunning spells |
| Bayek of Siwa | 0.767 | 14,008 (79.3%) | damage (double strike for historic creatures) |
| Arno Dorian | 0.763 | 13,830 (78.3%) | damage (anthem, deathtouch) |
| Ramses, Assassin Lord | 0.757 | 13,739 (77.8%) | finisher (win clause) |
| Aya of Alexandria | 0.747 | 13,560 (76.8%) | finisher (tokens) |
| Desmond Miles | 0.745 | 13,495 (76.4%) | finisher (grows) |
| Cover of Darkness | 0.727 | 13,279 (75.2%) | evasion (fear) |
| Altaïr Ibn-La'Ahad | 0.706 | 12,790 (72.4%) | recursion |
| Layla Hassan | 0.706 | 12,791 (72.4%) | recursion, draw |
| Achilles Davenport | 0.701 | 12,698 (71.9%) | evasion (menace), anthem |
| Brotherhood Regalia | 0.698 | 12,689 (71.9%) | evasion, protection (ward 2) |
| Eagle Vision | 0.650 | 11,795 (66.8%) | draw |
| Queen Marchesa | 0.634 | 11,647 (66.0%) | monarch enabler [S19] |
| Ratonhnhaké꞉ton | 0.608 | 11,014 (62.4%) | evasion, token |
| Royal Assassin | 0.606 | 11,005 (62.3%) | removal |

### Tag counts [S5]

Commander page: 125 tags. Top 12: Assassins 1,821; Legends 906; Historic 751; Freerunning 435; Aggro 264; Humans 152; Equipment 138; Combo 100; Lurrus Companion 69; Unblockable 56; Midrange 54; +1/+1 Counters 46. Smaller tags include Lifegain 8, Card Draw 7, Mill 9 and Menace 2.

### Bracket and theme pages [S6 to S14]

Theme pages print the commander-wide tag counts; the three bracket pages print their own.

| Page | Decks | Bracket counts (B1, B2, B3, B4, B5) | Budget / middle / expensive | Top cards (decks, share of page) |
|---|---|---|---|---|
| assassins [S6] | 1,821 | B1 7, B2 119, B3 131, B4 30, B5 2 | 182 / 1,457 / 182 | Basim 1,613 (88.6%); Ezio Blade 1,593 (87.5%); Bayek 1,530 (84.0%) |
| freerunning [S7] | 435 | B1 4, B2 87, B3 75, B4 18, B5 1 | 43 / 349 / 43 | Basim 398 (91.5%); Ezio Blade 380 (87.4%); Bayek 372 (85.5%) |
| aggro [S8] | 264 | B2 59, B3 75, B4 22, B5 7 | 26 / 212 / 26 | Ramses 239 (90.5%); Ezio Blade 239 (90.5%); Basim 233 (88.3%) |
| combo [S9] | 100 | B2 9, B3 14, B4 16, B5 31 | 10 / 80 / 10 | Ramses 64; Ezio Blade 58; Basim 58; Demonic Tutor 57; Dark Ritual 52 |
| midrange [S10] | 54 | B2 12, B3 15, B4 6, B5 5 | 5 / 44 / 5 | Cover of Darkness 47 (87.0%); Ezio Blade 45 (83.3%); Basim 45 (83.3%) |
| control [S11] | 14 | B2 2, B3 1, B4 5 | 1 / 12 / 1 | Arno Dorian, Ramses, Ezio Blade 12 each (85.7%) |
| core, Bracket 2 [S14] | 1,912 | (page = B2) | 191 / 1,530 / 191 | Basim 1,636 (85.6%); Arno 1,627 (85.1%); Ezio Blade 1,614 (84.4%) |
| upgraded, Bracket 3 [S12] | 1,388 | (page = B3) | 138 / 1,112 / 138 | Ezio Blade 1,228 (88.5%); Basim 1,228 (88.5%); Ramses 1,206 (86.9%) |
| optimized, Bracket 4 [S13] | 434 | (page = B4) | 43 / 348 / 43 | Ramses 382 (88.0%); Ezio Blade 362 (83.4%); Basim 348 (80.2%) |

The three bracket pages hold exactly the commander's bracket counts (1,912, 1,388 and 434), which confirms the mapping. Their own tags: core: Historic 133, Assassins 119, Freerunning 87, Legends 81, Aggro 59. Upgraded: Historic 134, Assassins 131, Aggro 75, Freerunning 75, Legends 75. Optimized: Assassins 30, Historic 25, Aggro 22, Freerunning 18, Combo 16 [S12 to S14].

### Takeaways

- The top cards are the same across brackets; the shared core is the typal-midrange plan.
- Bracket 3 is led by Historic and Assassins tags. Bracket 4 has Ramses at 88.0%, close to the 88.5% of Ezio Blade and Basim on Bracket 3.
- Combo and control are small slices (100 and 14 decks).

## Key question 3: primers, discussions and deck hosts

### Takeaway

Written primers are few and mostly from 2024. The two most detailed readable pieces (Draftsim 2024 and EDHREC December 2025) agree on the core plan and disagree on the mana and the finisher. No Reddit thread or Moxfield deck could be read.

### Draftsim, 2024 [S19]

- A five-color Assassin typal list with a historic subtheme. The author calls Ezio among the best commanders from Assassin's Creed [S19].
- Freerunning is described as ramp, cost reduction and fixing, since only black is needed once freerunning is on [S19].
- Mana: Sol Ring, Arcane Signet, Chromatic Lantern (named as the fixing piece), Fellwar Stone, all four Talismans that make black, black Triomes and fetch lands, and the channel lands. The author says the base has no room for frills because it must fix five colors [S19].
- Card draw: Basim (card advantage that enables freerunning), Realmwalker (a steady stream of draw), Kindred Discovery (called the best typal support card), Ezio, Blade of Vengeance (a burst of draw) [S19].
- Removal and interaction: Path to Exile and Swords to Plowshares, Assassin's Trophy, and protection against board wipes through Teferi's Protection and Clever Concealment [S19].
- Finishers: Winds of Abandon (a combat phase after a wipe), Overpowering Attack (an extra combat) and Kindred Dominance [S19].
- Protecting Assassins: Altaïr turns graveyard Assassins into attackers, and Jacob Frye casts copies from the graveyard [S19].
- Warnings: do not add too much board power; wraths punish overcommitment [S19].
- The author describes the payment as an activated ability [S19].

### Draftsim, 2026 [S20]

Ranks Ezio last (#46) among five-color cards. The author says it would barely make that list and belongs on a commander table [S20] (paraphrase).

### EDHREC, "Fire and Ice" (December 2025) [S18]

- Ezio discounts every Assassin spell, so the freerunning plan is cheap. The author calls the deck fast and resilient [S18].
- Menace and fear make the commander hard to block. Whispersilk Cloak gives protection and evasion [S18].
- Mana: EDHREC says these lists lean on all five colors less than other rainbow commanders, but still need a varied base. It criticizes Reliquary Tower, a colorless land [S18].
- Cuts: Murder (showing its age); Shay Cormac and Phantom Blade (weak fit); Chain Assassination (typical lists cannot sacrifice reliably); Assassin Gauntlet ("draft chaff" in the author's words); Go for the Throat and Fatal Push (conditional removal); The Revelations of Ezio (its first chapter only hits tapped creatures) [S18].
- Adds: Vincent Valentine, Shizo, Dark Ritual, Whispersilk Cloak, Birds of Paradise and Vincent, Vengeful Atoner [S18].
- Power level: the author says Ezio is sometimes too strong for casual tables, and asks whether it fits Bracket 3 or Bracket 4 [S18].

### MTG Rocks, 2024 [S21]

- An honorable mention at the bottom of an Assassin's Creed commander list. Freerunning casts expensive threats early; Vein Ripper or Thraximundar for two mana is the example. The ten-life ability is largely redundant. The Sorin Markov pairing is described as a one-two punch [S21].

### MTG Rocks, 2025, Duel Commander [S22]

- Ezio is banned as a commander in Duel Commander only. Freerunning is almost useless in that 1v1 format [S22].
- The author says Ezio decks rarely run Assassins beyond Basim; that is quoted as "rare for Ezio decks" [S22]. The author credits the five-color identity, which is cheap to cast, and the one-card threat [S22].

### Archidekt [S23, S24]

- The name search returned 60 decks; the top 20 by views were read. The most-viewed Ezio deck has 18,473 views and was last updated 2024-07-05 [S23].
- Six detail pages were read. All descriptions are empty, so no primer text was found. Four of them carry Archidekt's bracket field set to 3 [S24].

### Moxfield, Reddit and blocked sites

- Moxfield: the public search endpoint answered HTTP 200 but ignored the query, returning unrelated decks with a total capped at 10,000. No Ezio deck or primer was read [S25].
- Reddit: both search requests returned 403, and the search tool refuses reddit.com. No thread was read [S26].
- Blocked by Cloudflare or 403, not bypassed: Pojo [S27], MTGGoldfish [S28], TappedOut [S29], mtgdecks.net [S30] and Card Kingdom [S33]. Deckcheck returns an empty app page [S31]. Mythicwyrm returned 503 [S32].

### Answers by question

- **Common mistakes named:** relying on the ten-life ability alone [S21]; conditional removal [S18]; Chain Assassination without sacrifice outlets [S18]; a colorless land in the base [S18]; overcommitting into wraths [S19]; The Revelations of Ezio is slow [S18].
- **Damage through wide boards:** menace and fear [S18]; a wipe followed by a combat phase (Winds of Abandon) and an extra combat from Overpowering Attack [S19]. The text of Overpowering Attack is in [S3]. Assassin Gauntlet's enter trigger taps all creatures an opponent controls [S3], which no source discusses.
- **Haste:** no readable source discusses it. Haste exists on Kassandra, Eivor Wolf-Kissed, Eivor Battle-Ready, Mary Read and Anne Bonny, and Hidden Footblade [S3]; inclusion in [S5].
- **Protecting Assassins:** Altaïr and Jacob Frye return Assassins from the graveyard [S19; texts in S3]; Brotherhood Regalia gives ward 2 [S3]; Whispersilk Cloak gives protection and evasion [S18]; Teferi's Protection and Clever Concealment protect against wraths [S19].
- **Five colors for the kill:** the payment needs one of each color at the same time [S1]. Sources use Sol Ring, Arcane Signet, Chromatic Lantern, Talismans and Triomes [S19], and Brotherhood Headquarters, whose mana works only for Assassin and freerunning spells [S3]. EDHREC's average deck plays 36 lands [S15]. A retail sequencing article could not be read [S33].

## Key question 4: shortlist by function

Function labels are ours. Inclusion is from [S5]. "Text" means verified in [S3] or [S4].

| Function | Card | Recommended by | Why |
|---|---|---|---|
| Draw | Basim Ibn Ishaq | Draftsim [S19] | Draws when a historic spell is cast; can't be blocked once a turn (text); 82.5% |
| Draw | Ezio, Blade of Vengeance | Draftsim [S19]; EDHREC [S18] | Draws when an Assassin deals combat damage (text); 82.1% |
| Draw | Kindred Discovery | Draftsim [S19] | Called the best typal support card; text not read; 25.6% |
| Draw | Mari, the Killing Quill | Draftsim [S19] | Cards and Treasure for Assassin hits; hit counters for Etrata; 59.4% |
| Draw | Black Market Connections | Draftsim [S19] | Treasure, draw or a token each turn, paying life (text); 47.0% |
| Draw | Eagle Vision | EDHREC data [S5] | Freerunning for three cards (text); 66.8% |
| Evasion | Cover of Darkness | EDHREC data [S5, S10] | Fear for a chosen creature type (text); 75.2% |
| Evasion | Achilles Davenport | Draftsim [S19] | Menace; other Assassins +1/+1 (text); 71.9% |
| Evasion | Brotherhood Regalia | EDHREC data [S5] | Ward 2, can't be blocked (text); 71.9% |
| Evasion | Lydia Frye | EDHREC data [S5] | Can't be blocked by power 3 or more (text); 62.3% |
| Evasion | Etrata, the Silencer | Draftsim [S19] | Can't be blocked; the Ramses combo (text) [S4]; 42.9% |
| Haste | Kassandra, Eagle Bearer | No primer | Haste (text); 26.6% |
| Haste | Eivor, Wolf-Kissed | No primer | Trample and haste (text); 19.8% |
| Haste | Hidden Footblade | No primer | Equipment: +1/+0 and haste (text); 11.9% |
| Protection | Brotherhood Regalia | EDHREC data [S5] | Ward 2 (text); 71.9% |
| Protection | Whispersilk Cloak | EDHREC [S18] | Protection and evasion, as the author says; 38.7% |
| Protection | Smoke Bomb | EDHREC data [S5] | Shroud on all creatures for a turn; one creature unblockable (text); 42.2% |
| Protection | Haystack | EDHREC data [S5] | Phases out a creature (text); 44.3% |
| Protection | Teferi's Protection, Clever Concealment | Draftsim [S19] | Protect against board wipes; text not read |
| Removal | Royal Assassin | EDHREC data [S5] | Destroys a tapped creature (text); 62.3% |
| Removal | Path to Exile | Draftsim [S19] | Exile target creature (text); 56.4% |
| Removal | Swords to Plowshares | Draftsim [S19] | Called among the best ever printed; EDHREC says it is declining [S18]; 35.0% |
| Removal | Assassin's Trophy | Draftsim [S19] | Destroys a permanent (text); 58.5% |
| Removal | The Revelations of Ezio | Draftsim [S19] | Destroys a tapped creature, then returns an Assassin (text); EDHREC cuts it [S18]; 47.8% |
| Ramp | Sol Ring; Arcane Signet | Draftsim [S19]; EDHREC average deck [S15] | Mana rocks; 82.6% and 80.7% |
| Ramp | Chromatic Lantern | Draftsim [S19] | Named as the fixing piece; 57.3% |
| Ramp | Viewpoint Synchronization | EDHREC data [S5] | Freerunning: three basics, two onto the battlefield tapped (text); 59.5% |
| Finisher | Ramses, Assassin Lord | Draftsim [S19] | Win clause (text) [S4]; 77.8% |
| Finisher | Overpowering Attack | Draftsim [S19] | Extra combat (text); 46.2% |
| Finisher | Sorin Markov | EDHREC combos [S5]; MTG Rocks [S21] | Life total becomes 10 (text) [S4]; 26.7% |
| Finisher | Vein Ripper | Draftsim [S19]; MTG Rocks [S21] | Punishes wraths (author); text not read; 27.9% |
| Defense | Propaganda | EDHREC data [S5] | Attackers must pay {2} each (text); 36.4% |
| Defense | Reconnaissance | EDHREC data [S5] | Removes an attacking creature from combat (text); 30.1% |

## Conflicts between sources

1. **Type of the payment.** Scryfall says triggered, with a reflexive trigger [S1, S2]. Draftsim (2024) and MTG Rocks (2024) call it an activated ability [S19, S21]. Resolution: follow Scryfall.
2. **Legality.** MTG Rocks (2025) bans Ezio as a commander in Duel Commander only [S22]. Scryfall lists it as legal in Commander on 2026-10-31 [S1]. No conflict in Commander.
3. **Power.** EDHREC (2025) says it is sometimes too strong for casual tables [S18]. Draftsim (2024) calls it among the best Assassin's Creed commanders [S19]. MTG Rocks (2024) ranks it at the bottom of its list [S21]. Draftsim (2026) ranks it last of 46 five-color cards [S20]. The two 2024 pieces predate play data: Draftsim was published the day before the set's release and MTG Rocks before it. The EDHREC data is the most recent evidence.
4. **Assassin density.** MTG Rocks (2025) says Ezio decks rarely run Assassins beyond Basim [S22]. EDHREC tags 1,821 decks (10.3%) as Assassins [S5, S6], and its average deck has about 28 creatures, many with assassin names [S15]. The type lines of those creatures were not checked (unverified). The tag is a theme label, not a type count.
5. **Five colors.** EDHREC says lists lean on all five colors less than other rainbow commanders [S18]. Draftsim says the base must fix five colors [S19]. Both can hold: the payment needs each color at once, and the base still needs fixing.
6. **Combo partners.** Draftsim names Ramses with Etrata as the one meaningful combo [S19]. EDHREC pairs Ezio with Sorin Markov, Tree of Perdition and Magister Sphinx [S5]. MTG Rocks names Sorin Markov [S21]. These are different scopes, not contradictions.
7. **Value of the kill.** Draftsim says it is good late [S19]. MTG Rocks says ten life is low and the ability redundant [S21]. Disputed; no pod data settles it.
8. **Popularity figures.** The December 2025 article gives Queen Marchesa 69% and Royal Assassin 63% [S18]. The JSON read on 2026-10-31 gives 66.0% and 62.3% [S5]. Probably a snapshot difference (cause unverified).

## Gaps

- **Reddit:** no thread read. The search endpoint returned 403 and the search tool refuses reddit.com [S26].
- **Moxfield:** no deck or description read; the search endpoint ignores the query [S25].
- **Blocked sites, not bypassed:** Pojo, MTGGoldfish, TappedOut, mtgdecks.net and Card Kingdom [S27 to S30, S33]. Mythicwyrm is down [S32]. Deckcheck has no readable content [S31].
- **Archidekt:** six decks read, none with a description; no Archidekt primer found [S24].
- **Video:** no video or transcript was read.
- **Haste:** no source discusses haste for Ezio. Haste rows rest on card texts and inclusion only.
- **Wraths:** Teferi's Protection and Clever Concealment are named by Draftsim [S19] but their texts were not read and no EDHREC figure was extracted.
- **Cards named without a text:** Vein Ripper, Kindred Discovery, Mari, Queen Marchesa, Thraximundar, Realmwalker, Winds of Abandon and Phyrexian Arena.
- **EDHREC definitions:** synergy, lift and the Fire and Ice scores were not read [S5, S18]. The JSON has no snapshot date and no inclusion key.
- **Bracket denominator:** the bracket counts sum to 3,988 of 17,660 decks. EDHREC does not state the base.
- **Commander Spellbook:** not queried, so combo steps beyond the Scryfall texts are unverified.
- **Tree of Perdition line:** no source describes a line to 10 life with it; the inference is from [S4].
- **EDHREC articles:** two general articles on the commander panel (Swords, Wither) were not read. A May 2025 Universes Beyond-only feature was not found [S34].
