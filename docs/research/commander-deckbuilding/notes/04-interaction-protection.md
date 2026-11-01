# Interaction, Protection and Resilience in Commander (Multiplayer)

Research note, 2026-10-31. Scope: Commander in 3 to 4 player pods, Bracket 3 decks. Key questions: removal, board wipes, protection, resilience and recovery, and the two reference boards.

**Method and limits.** 7 web searches and 8 WebFetch calls (15 tool calls; 2 fetches returned HTTP 403). All pages read 2026-10-31. WebFetch returns a model-written extraction, not verbatim text, so every figure below comes from an extraction and has not been re-checked on the page. Re-read the cited page before a figure goes into a builder prompt. Quotations: one, from S3, under 15 words. Excluded by the owner's rules: EDHREC (its article URLs appeared in search results; not opened, and its search summaries were discarded), forum threads and retailer or listicle pages. No 60-card evidence was gathered.

## Sources

| ID | Source | Author | Date | URL | Status and use |
|---|---|---|---|---|---|
| S1 | How Many Board Wipes Should You Really Play in Commander? (Draftsim) | A.L. Walser | 2025-07-11 | https://draftsim.com/edh-how-many-board-wipes/ | Read (extraction). Wipe counts, one-sided wipes, protection against wipes, rebuilding. |
| S2 | How Much Removal Should You Really Play in Commander? (Draftsim) | A.L. Walser | 2024-02-22 | https://draftsim.com/edh-how-much-removal/ | Read (extraction). Removal counts and mix, multiplayer. |
| S3 | Targeted Removal In Commander (Star City Games) | Bennie Smith | 2017-06-16 | https://articles.starcitygames.com/?p=3787 | Read (extraction); no paywall in this fetch. The same title is also indexed under a /premium/ path. Multiplayer removal, commanders, sweepers. |
| S4 | How Many Targeted Removal Spells for EDH Decks? (Nerd Leagues) | DonSpider | 2026-07-04 | https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks | Read (extraction). Totals, spot removal versus wipes, targets. |
| S5 | Building a Commander Deck - Part Two: Structure (Cardsphere blog) | Andy Zupke | 2021-02-26 | https://blog.cardsphere.com/?p=1420 | Read (extraction). Structure counts, protection, recursion. Text and recap disagree. |
| S6 | MTG Head Designer Mark Rosewater Says Commander Staple Was A Mistake (Draftsim) | Herko Kerghans | 2025-06-03 | https://draftsim.com/mtg-head-designer-lightning-greaves/ | Read (extraction). Lightning Greaves and Swiftfoot Boots. Designer remark reported second-hand. |
| S7 | You should be playing more board wipes (Card Kingdom blog) | not shown | not shown | https://blog.cardkingdom.com/you-should-be-playing-more-board-wipes/ | FAILED: HTTP 403. Nothing used. |
| S8 | Swiftfoot Boots or Lightning Greaves, which is better (Card Kingdom blog) | not shown | not shown | https://blog.cardkingdom.com/swiftfoot-boots-or-lightning-greaves-which-is-better/ | FAILED: HTTP 403. Nothing used. |
| S9 | The Other 99 Board Wipes (Cardmarket Insight) | not shown | not shown | https://cardmarket.com/en/Insight/Articles/The-Other-99-Board-Wipes | Search result only; not opened; not used. |
| S10 | Sheldon Menery author index (Star City Games) | Sheldon Menery | n/a | https://articles.starcitygames.com/author/sheldon-menery/ | Index page only; no article read. |

## 1. Removal: how many, which mix, multiplayer

### Takeaway
Totals run about 8 to 12 pieces: S2 sets a floor of 8 to 10 removal spells, S4 counts 8 to 12 including board wipes ([S2](https://draftsim.com/edh-how-much-removal/), [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)). Three to five spot answers are reserved for threats that must be answered. In multiplayer a one-for-one trade with one opponent leaves you and that opponent behind the players who spent nothing (S2 works the four-player case), so the sources favor two-for-one answers, edicts that hit everyone, and removal chosen for its role in the plan. S3 says removal should play a supporting role in the deck ([S3](https://articles.starcitygames.com/?p=3787)).

### Cited findings
- Floor of 8 to 10 removal spells (more is fine) inside a 15 to 20 card interaction package. The author calls this a personal baseline, not split by archetype. [S2](https://draftsim.com/edh-how-much-removal/)
- Total of 8 to 12 removal and interaction pieces including board wipes and other interaction; spot removal 5 to 8 as the starting point; board wipes 2 to 4. [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- Three to five spot removal spells are described as essential for threats that cannot be left unanswered. [S2](https://draftsim.com/edh-how-much-removal/); [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- About 1 to 2 removal spells ready for key moments, without letting removal dominate the hand. This is a hand-level suggestion, not a deck count. [S3](https://articles.starcitygames.com/?p=3787)
- Two or three removal spells seen per game is a drawing goal, not a deck count. [S2](https://draftsim.com/edh-how-much-removal/)
- Removing one player's creature can leave you a card down while uninvolved players spend nothing, so the author advises using removal sparingly. [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- In a four-player pod a one-for-one trade with one opponent leaves you and that player behind the two who spent nothing. [S2](https://draftsim.com/edh-how-much-removal/)
- Single-target answers cannot carry a multiplayer game: several opponents, each with several threats, drain them. The article's line is: "You can't rely on spot removal to solve your problems." [S3](https://articles.starcitygames.com/?p=3787)
- Cheap spot removal (Swords to Plowshares, Path to Exile, Nature's Claim) is top tier one-on-one and often costs less mana than the threat it answers. In multiplayer the sources prefer 2-for-1 value: Chandra, Torch of Defiance, and creatures whose enter-the-battlefield trigger removes a permanent, such as Nekrataal and Skyclave Apparition. [S2](https://draftsim.com/edh-how-much-removal/); [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- Aim removal at the commander, a combo piece, a card-draw engine, a sacrifice outlet, or whatever stops the deck from working, not at every creature. [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- Combo decks use removal defensively, to stop the one card that would stop their plan. [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- Spread answers across permanent types; creature-only removal leaves gaps against artifact, enchantment and other noncreature threats. [S2](https://draftsim.com/edh-how-much-removal/); [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- Edicts are niche but excellent against decks that rely on one creature; edicts that hit every player (Plaguecrafter, Tithing Blade) fit multiplayer. [S2](https://draftsim.com/edh-how-much-removal/)
- Bounce is weaker in Commander: it costs a card for a short swing, and high life totals blunt it. [S2](https://draftsim.com/edh-how-much-removal/)
- Targeted discard is a poor fit. Discard that hits every player suits reactive decks holding counterspells. [S2](https://draftsim.com/edh-how-much-removal/); [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- Counterspells deny a spell its value but cannot touch a permanent already in play. One source says to balance them against removal; another counts them as removal. [S2](https://draftsim.com/edh-how-much-removal/); [S5](https://blog.cardsphere.com/?p=1420)
- Commanders return to the command zone, so destroying one is often temporary. The author prefers neutralizing it, with effects such as Prison Term or Song of the Dryads. [S3](https://articles.starcitygames.com/?p=3787)
- Mass removal punishes the whole table and can push everyone to gang up on you; target the one permanent that actually threatens you. [S3](https://articles.starcitygames.com/?p=3787)
- Removal can be a bargaining chip, such as agreeing to spare someone's commander. [S2](https://draftsim.com/edh-how-much-removal/)
- Targeted artifact or enchantment removal can break a combo without sweeping up the other permanents (the article's example is Paradox Engine). [S3](https://articles.starcitygames.com/?p=3787)

### Inferences (ours, not sourced)
- The owner's game (about 20 one-for-one removal spells, no damage through) fits three sourced points: a single-target answer cannot carry a multiplayer game ([S3](https://articles.starcitygames.com/?p=3787)); one-for-one trades lose ground against several opponents ([S2](https://draftsim.com/edh-how-much-removal/), [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)); and combat wins still need finishers beyond creatures, with at least 3 finishers in the text of [S5](https://blog.cardsphere.com/?p=1420). The missing piece in that game was probably the damage plan, not the removal count.
- Two or more large creatures per opponent in a three-opponent pod means six or more threats. The sources give 3 to 5 must-answer spot removal spells per deck, so such a pod needs answers that do two jobs, or blockers, rather than a larger one-for-one count. This scaling is our inference from the sourced numbers.

### Gaps
- No source splits removal counts by pod size (3 or 4 players) or by the number of big threats per opponent.
- Instant-speed removal: only counterspell timing is covered ([S2](https://draftsim.com/edh-how-much-removal/)). No source treats instant-speed removal as a category.
- Flexible "destroy target permanent" effects: not singled out in [S2](https://draftsim.com/edh-how-much-removal/).
- Removal that clears blockers for a combat plan: [S2](https://draftsim.com/edh-how-much-removal/) says it does not discuss this; its only related point is that aggressive decks should use spot removal selectively.
- No outcome data: none of the sources read shows whether heavier removal wins more games.
- The [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks) extraction flagged an apparent slip (a targeted-discard example that names Swords to Plowshares, a creature removal spell). Not checked on the page.

## 2. Board wipes: how many, one-sided or symmetric, creature decks, surviving wipes

### Takeaway
The newest figure is 3 to 5 wipes for most decks ([S1](https://draftsim.com/edh-how-many-board-wipes/), 2025). Other sources give 2 to 4 ([S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)), no more than 3 ([S5](https://blog.cardsphere.com/?p=1420)), and 1 to 2 ([S2](https://draftsim.com/edh-how-much-removal/), 2024, same author as S1). Creature-based decks run fewer; control and non-creature decks run more. Sources prefer one-sided and synergy wipes, because a symmetric wipe also hits your own board.

### Cited findings
- Most decks: about 3 to 5 wipes. Creature-based decks run fewer, control decks more, and about 10 wipes is too many for most decks. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- The article's examples: a slow combo deck without many creatures might run 3 to 4 wipes beyond one, and a token aggro deck used two. These are examples, not rules. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- The 2024 article by the same author: one or two wipes for most decks; non-creature strategies can run more, with no number given. [S2](https://draftsim.com/edh-how-much-removal/)
- Board wipes 2 to 4 within an 8 to 12 total. [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- No more than 3 mass removal; the rest are targeted and split between creatures and artifacts or enchantments; creature-heavy decks should use fewer creature-killing effects. [S5](https://blog.cardsphere.com/?p=1420)
- One-sided wipes (hit only opposing permanents) should be added whenever possible, except in control or combo decks indifferent to their own board. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- Being hit by one-sided wipes such as Plague Wind, Winds of Abandon or Ruinous Ultimatum is often game-losing. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- Synergy wipes act as one-sided wipes within your own deck. A conditional wipe the deck never triggers works the same way (the article's example: The Battle of Bywater in a white deck of small creatures). The article says every wipe should aim for this type. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- In multiplayer a Damnation-style wipe usually costs opponents more cards than it costs you, even if you keep some creatures, because each opponent has a board. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- Token decks take a hit from Wrath of God even when an opponent casts it. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- Stacking several wipes works against creature strategies. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- Sorcery-speed wipes let opponents rebuild first; instant-speed wipes let you rebuild at once. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- Sweepers alone: repeated sweeps stall the game and bore players; sweepers also hit harmless permanents such as signets; a hand of only sweepers struggles against an early creature. [S3](https://articles.starcitygames.com/?p=3787)
- Wraths do not keep commanders away, since commanders return to the command zone. [S3](https://articles.starcitygames.com/?p=3787)
- Bounce wipes: returned creatures lose their enter-the-battlefield value (Eternal Witness and Baleful Strix are the examples). Bouncing an opposing commander lets its owner recast it from hand without commander tax. A bounce wipe needs a tempo plan; wheel effects (Windfall, Timetwister) help by getting rid of the returned cards. Terminus, which puts creatures at the bottom of libraries, is treated as better than bounce. [S1](https://draftsim.com/edh-how-many-board-wipes/)

### Protection against wipes (all from [S1](https://draftsim.com/edh-how-many-board-wipes/))
- Indestructible, often granted by protection spells, blanks destruction wipes such as Wrath of God. Destruction wipes are still worth running in decks that lack other removal.
- Exile wipes (Sunfall, Farewell) get past standard protection; only phasing (Teferi's Protection, Clever Concealment) stops them.
- Mass bounce gets past indestructible and protection. Sacrifice effects get past indestructible.
- -X/-X wipes get past indestructible; only phasing stops them.
- Damage-based wipes are the kind that protection effects such as Akroma's Will and Brave the Elements stop.
- Modal wipes such as Final Showdown can double as protection.

### Inferences
- Wipe resistance needs more than one mechanism: indestructible covers destruction wipes, phasing covers exile and -X/-X, and mass bounce or sacrifice need a board that can rebuild (from the list in S1).
- A deck that attacks with creatures should run few symmetric wipes and lean on one-sided or synergy wipes. S1 and S5 point the same way.
- Against a wide token board, a symmetric wipe costs the opponent many cards (S1's multiplayer logic), but it also clears your own tokens. The trade favors a deck that does not depend on its own board.

### Gaps
- No source gives a wipe count for 3 or 4 player pods.
- Overextending before a wipe: no read source covers it. Heroic Intervention is not mentioned in any read source.
- Card Kingdom's board-wipe article ([S7](https://blog.cardkingdom.com/you-should-be-playing-more-board-wipes/)) returned HTTP 403. A search summary attributed a count of three or four to Card Kingdom; that is unverified and not used.
- Cardmarket's article on wipes and card advantage ([S9](https://cardmarket.com/en/Insight/Articles/The-Other-99-Board-Wipes)) was listed, not opened.
- No number for rebuild cards after a wipe.

## 3. Protection: commander protection, equipment, counts

### Takeaway
One source gives a protection count: [S5](https://blog.cardsphere.com/?p=1420) (2021) says 5 to 7 in its text and 5 in its recap, and that protection varies more across decks than ramp, draw or removal. Commander-dependent decks need more protection for the commander. Lightning Greaves and Swiftfoot Boots stop targeting only; shroud also stops the controller, hexproof does not ([S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)). No read source gives a reliable count of commander-protection pieces.

### Cited findings
- Protection is treated as a fourth core category beside ramp, draw and removal: about 5 to 7 per deck in the text, 5 in the recap. Its count varies more across decks than the others. [S5](https://blog.cardsphere.com/?p=1420)
- Decks that depend on their commander need more protection for it; decks vulnerable to specific cards need defenses against those cards. Counterspells can double as protection. [S5](https://blog.cardsphere.com/?p=1420)
- Protection covers effects that keep opponents from shutting your plan down. [S5](https://blog.cardsphere.com/?p=1420)
- Lightning Greaves: equip cost zero; grants haste and shroud. Shroud stops targeting by anyone, including the creature's own controller. [S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)
- Swiftfoot Boots: equip cost not stated in S6 (non-zero); grants haste and hexproof. Hexproof does not stop the controller from targeting. [S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)
- S6 calls hexproof arguably the stronger protection, and says Greaves' strength comes from the haste-and-shroud pairing rather than from the zero cost alone. [S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)
- S6 reports that Mark Rosewater called Greaves' zero equip cost an error, and that zero-cost abilities cause design problems. The article reports this from a blog post, so it is second-hand. [S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)
- S6 gives a usage rank: Greaves is fifth in EDH usage, and only Boots is more popular in Commander. The article gives no date or source for the usage data, and the scope of the ranking is unclear. [S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)
- S6 says the equipment niche is largely confined to Commander variants. [S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)
- Protection spells often grant indestructible, which blanks destruction wipes; they do not stop exile, -X/-X, mass bounce or sacrifice. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- Commanders come back eventually, so destroying one is often temporary; the author prefers neutralizing it. [S3](https://articles.starcitygames.com/?p=3787)

### Inferences
- Shroud and hexproof stop targeted effects only. Edicts, sacrifice and non-targeted wipes are not stopped. This is rules reasoning, not sourced here; S6 does not address these effects.
- S6 notes that shroud also stops the controller from targeting. For a deck that targets its own creatures, that favors Boots (inference from S6's stated facts).
- A commander-dependent deck needs protection against destruction wipes (indestructible, [S1](https://draftsim.com/edh-how-many-board-wipes/)), against targeted removal (shroud or hexproof, [S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)), and some answer to exile and -X/-X effects (phasing, [S1](https://draftsim.com/edh-how-many-board-wipes/)). How many pieces that takes is open: S5 gives 5 to 7 for the whole deck.

### Gaps
- One protection count source ([S5](https://blog.cardsphere.com/?p=1420), 2021), with an internal discrepancy; no protection counts split by commander dependence.
- Card Kingdom's equipment article ([S8](https://blog.cardkingdom.com/swiftfoot-boots-or-lightning-greaves-which-is-better/)) returned HTTP 403. Search summaries attributed to Card Kingdom and others a split between Greaves and Boots by commander type; unverified, not used.
- Two Card Kingdom protection guides were listed but not opened: https://blog.cardkingdom.com/how-to-choose-a-protection-spell-for-commander and https://blog.cardkingdom.com/choosing-the-right-protection-for-your-commander/.
- Sacrifice-and-return tricks: no read source covers them.
- Equipment cannot attach to planeswalker commanders: rules knowledge, not checked in this session (unverified here).
- Boots' actual equip cost is not in S6.

## 4. Resilience and recovery: recursion, card advantage, graveyard hate, stax, combo

### Takeaway
The structure numbers come from one source ([S5](https://blog.cardsphere.com/?p=1420), 2021): about 10 card draw, 2 to 3 graveyard recursion effects kept apart from draw, 10 to 12 ramp, 37 to 38 lands. Rebuilding depends on timing and exile: instant-speed wipes let you rebuild at once ([S1](https://draftsim.com/edh-how-many-board-wipes/)), exile largely prevents recursion of destroyed cards ([S1](https://draftsim.com/edh-how-many-board-wipes/)), and commanders return from wraths ([S3](https://articles.starcitygames.com/?p=3787)). No read source gives counts for stax, graveyard hate or combo protection.

### Cited findings
- Card draw about 10, called standard. One draw per turn is not enough in Commander; a commander that draws cards on its own lets a deck run less. [S5](https://blog.cardsphere.com/?p=1420)
- Graveyard recursion 2 to 3 per deck, counted apart from draw, because the graveyard may be empty early or hit by graveyard hate; graveyard-based strategies would run more. [S5](https://blog.cardsphere.com/?p=1420)
- Mana sources about 48 to 50 (37 to 38 lands, 10 to 12 ramp), the author's structure. [S5](https://blog.cardsphere.com/?p=1420)
- Destruction lets opponents recur cards from the graveyard with effects such as Regrowth or Reanimate; exile largely prevents this, with Riftsweeper as a technical exception. [S1](https://draftsim.com/edh-how-many-board-wipes/)
- S3 favors exile for non-commander cards, because creatures in graveyards are often usable by other decks. [S3](https://articles.starcitygames.com/?p=3787)
- Sorcery-speed wipes give opponents time to rebuild; instant-speed wipes let you rebuild immediately; stacked wipes can drag games out. [S1](https://draftsim.com/edh-how-many-board-wipes/); [S5](https://blog.cardsphere.com/?p=1420)
- Commanders return from wraths. [S3](https://articles.starcitygames.com/?p=3787)

### Inferences
- The S5 structure gives 2 to 3 recursion effects and about 10 draw. A deck that runs 3 to 5 wipes ([S1](https://draftsim.com/edh-how-many-board-wipes/)) needs more replacement than that baseline; the two sources imply a tension a builder must resolve.
- Exile-based answers double as protection against recursion ([S1](https://draftsim.com/edh-how-many-board-wipes/), [S3](https://articles.starcitygames.com/?p=3787)). If the deck itself plays recursion, the same exile effects also remove its own targets (inference).

### Gaps
- Playing against stax: no source read.
- Graveyard hate: no count, and no counter-strategy from a read source.
- Playing against combo: [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks) says combo decks use removal defensively; no count of protection against combo.
- Card advantage after a wipe: S1 gives no number; no rebuild count from any source.
- Listed but not read: Card Kingdom's recursion article (https://blog.cardkingdom.com/the-power-of-recursion-whats-yours-is-mine/) and Hipsters of the Coast, 2019 (https://www.hipstersofthecoast.com/2019/08/the-power-of-recursion-commander-2019-spoilers/).
- Sheldon Menery, suggested as a source: only index pages came up ([S10](https://articles.starcitygames.com/author/sheldon-menery/)); no article read.

## 5. The two reference boards

### Takeaway
Sources give little direct guidance for either board. The usable points: edicts suit single-creature threats ([S2](https://draftsim.com/edh-how-much-removal/)); sacrifice outlets are removal targets ([S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)); wipes hit tokens too ([S1](https://draftsim.com/edh-how-many-board-wipes/)); must-answer threats need 3 to 5 spot answers ([S2](https://draftsim.com/edh-how-much-removal/), [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)). The owner's observations are signal, not proof; the table below maps them.

### Cited findings
- Edicts: niche but excellent against builds that rely on one creature. [S2](https://draftsim.com/edh-how-much-removal/)
- Aim removal at a sacrifice outlet, among other key permanents. [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)
- Token decks take a hit even from a wrath an opponent casts ([S1](https://draftsim.com/edh-how-many-board-wipes/)); in multiplayer a symmetric wipe usually costs opponents more cards than you ([S1](https://draftsim.com/edh-how-many-board-wipes/)).
- Creature-light decks need ways to handle large attacks; combat-based decks still need finishers. [S5](https://blog.cardsphere.com/?p=1420)
- Aggressive decks should use spot removal selectively on specific threats, keep enough efficient creatures to pressure opponents, and avoid symmetric wraths. [S2](https://draftsim.com/edh-how-much-removal/)

### Owner's observations mapped (signal, not proof)

| Owner observation | What the read sources say | Status |
|---|---|---|
| Fragile "paper" creatures died to everything | Indestructible from protection blanks destruction wipes; exile, -X/-X and sacrifice get past it ([S1](https://draftsim.com/edh-how-many-board-wipes/)). Nothing on creature durability. | Partly sourced; inference |
| Opponent with 8 or more 1/1 goblins sacrificed two to kill attackers | Target sacrifice outlets ([S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)); wipes hit tokens ([S1](https://draftsim.com/edh-how-many-board-wipes/)). Edict advice is framed around single-creature builds ([S2](https://draftsim.com/edh-how-much-removal/)), so edicts are weak against wide boards. | Inference |
| Opponents with two or more big creatures | 3 to 5 must-answer spot removal ([S2](https://draftsim.com/edh-how-much-removal/), [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)); two-for-one answers preferred (same sources). No per-opponent count. | Numbers sourced; scaling is inference |
| About 20 one-for-one removal spells, no damage through | Removal is a supporting role ([S3](https://articles.starcitygames.com/?p=3787)); one-for-one trades lose in multiplayer ([S2](https://draftsim.com/edh-how-much-removal/), [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks)); combat needs finishers beyond creatures ([S5](https://blog.cardsphere.com/?p=1420)). | Inference from sourced points |
| Commander that attacks needs protection | Commander-dependent decks need more protection ([S5](https://blog.cardsphere.com/?p=1420)); Greaves and Boots stop targeting only ([S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)). | Partly sourced |
| Decks that rarely attack need different protection | Protection against wipes depends on wipe type ([S1](https://draftsim.com/edh-how-many-board-wipes/)); protection keeps the plan running ([S5](https://blog.cardsphere.com/?p=1420)). | Inference |

### Gaps
- No source on fragile combat creatures, or on how often pods hold two or more big creatures.
- No source on sacrifice-based chump boards beyond the single S4 point.
- No Commander's Herald or Wizards of the Coast article was read.

## Conflicts between sources

1. **Wipe counts.** [S1](https://draftsim.com/edh-how-many-board-wipes/) (2025) gives 3 to 5 for most decks; [S2](https://draftsim.com/edh-how-much-removal/) (2024), by the same author, gives 1 to 2; [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks) gives 2 to 4; [S5](https://blog.cardsphere.com/?p=1420) gives no more than 3. The two Draftsim figures differ and neither extraction explains the change. S1 is the newest and most detailed. Across the five sources the range is 1 to 5.
2. **Removal totals use different definitions.** [S2](https://draftsim.com/edh-how-much-removal/) counts 8 to 10 removal inside a 15 to 20 interaction package and gives wipes a separate 1 to 2; it does not say whether the 8 to 10 includes wipes. [S4](https://www.nerdleagues.com/blog/how-many-targeted-removal-spells-for-edh-decks) counts 8 to 12 including wipes and other interaction. [S5](https://blog.cardsphere.com/?p=1420) counts about 10 removal, also counts counterspells as removal, and does not say whether the 10 includes wipes. The totals are not directly comparable.
3. **Internal discrepancy in S5.** Protection is 5 to 7 in the text and 5 in the recap; finishers are at least 3 in the text and 3 to 5 in the recap. The extraction flagged this; not checked on the page.
4. **Equipment popularity.** [S6](https://draftsim.com/mtg-head-designer-lightning-greaves/)'s usage claim is ambiguous in scope. Search summaries (unverified, not used) disagree on whether Greaves or Boots is more popular and on which commander suits which equipment. No read source settles it.
5. **Multiplayer wipes.** [S1](https://draftsim.com/edh-how-many-board-wipes/) says a symmetric wipe usually costs opponents more cards than it costs you; [S3](https://articles.starcitygames.com/?p=3787) says mass removal pushes the table to gang up on you. These are different costs (cards versus politics), not a contradiction; a builder should weigh both.
6. **Hand-level and per-game figures are not deck counts.** The 1 to 2 removal "ready" in [S3](https://articles.starcitygames.com/?p=3787) and the 2 to 3 removal seen per game in [S2](https://draftsim.com/edh-how-much-removal/) must not be compared with deck totals.

## Gaps (overall)
- Owner-excluded: EDHREC (no content used) and forum threads. Figures from those sources are absent by design.
- Not read: Commander's Herald (no article surfaced in search), Wizards of the Coast, Command Zone, MTGGoldfish, TCGplayer. Card Kingdom blocked on both target pages; three of its pages were listed only.
- No 60-card evidence gathered.
- No outcome data: nothing read shows whether more removal or more wipes wins more games.
- No sourced figures for stax, graveyard hate, combo protection, sacrifice-and-return, overextension or Heroic Intervention.
- No pod-size split (3 versus 4 players).
- One protection count source ([S5](https://blog.cardsphere.com/?p=1420), 2021).
- No read source covers the Bracket rules that the project targets.
- All figures come from WebFetch extractions, not verbatim page text. S3 (2017) and S5 (2021) are older, and their card references may predate later sets; this was not checked.
- S9 and S10 were listed but not read as articles.
