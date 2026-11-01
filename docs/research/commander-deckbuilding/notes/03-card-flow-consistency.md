# Card Advantage, Tutors and Consistency in Commander: Card-Flow Notes

**Scope.** Commander, 99-card library, casual Bracket 3 pods of 3 to 4 players. 60-card material appears only as labeled complement.
**Labels.** Citations are IDs; the tables give title, author, date and URL. Fetched pages were read 2026-10-31. "Snippet" means a search-result summary I did not open: direction only, not evidence. "Computed" means my own hypergeometric arithmetic, not a source claim.
**Method.** 22 search or fetch calls (12 searches, 10 fetches), above the 15-call guideline, to cover five questions. Six pages were read and three failed. Fetch results are model summaries, not rendered text. Checks: S1's counts sum to 75, leaving 24 slots, as S1 states; S1's ramp odds reproduce; its land odds do not (Conflict 3). Forbidden domains were filtered out of searches and never opened.

## Sources

### Read (fetched 2026-10-31)

| ID | Title | Author | Date | URL |
|---|---|---|---|---|
| S1 | The Power of a Deckbuilding Checklist (Commander Quickie) | Tomer Abramovici, MTG Goldfish | 2020-03-11 | https://www.mtggoldfish.com/articles/the-power-of-a-deckbuilding-checklist-commander-quickie |
| S2 | How Much Card Draw Should You Really Play in Commander? | Kendra Snead, Draftsim | 2024-03-14; updated 2025-01-17 | https://draftsim.com/edh-how-much-card-draw/ |
| S3 | Mechanical Engineering: Call it a Draw? | "Commander Mechanic" (byline as read), Commander's Herald | 2021-07-01 | https://commandersherald.com/mechanical-engineering-4-call-it-a-draw/ |
| S4 | Building For Synergy In Commander | Erik Tiernan, Star City Games | 2016-05-16 | https://articles.starcitygames.com/articles/building-for-synergy-in-commander/ |
| S5 | 9 Critical Tips for Building a Better Commander Deck | A.L. Walser, Draftsim | 2026-06-05 | https://draftsim.com/edh-deck-tips/ |
| S6 | The 15 Worst Mistakes Players Make in Commander | Timothy Zaccagnino, Draftsim | 2025-05-19; updated 2025-06-19 | https://draftsim.com/mtg-commander-mistakes/ |

### Failed (not used as evidence)

| ID | Title | Author | Status | URL |
|---|---|---|---|---|
| F1 | How Many Sources Do You Need to Consistently Cast Your Spells? A 2022 Update | Frank Karsten, ChannelFireball | Redirects to TCGplayer; the fetch returned only the site name. Search summary gives a 2025-02-13 update date (unverified). | https://www.channelfireball.com/article/How-Many-Sources-Do-You-Need-to-Consistently-Cast-Your-Spells-A-2022-Update/dc23a7d2-0a16-4c0b-ad36-586fcca03ad8/ |
| F2 | The Importance of Math to "Doing the Thing" In Commander | Card Kingdom Blog | HTTP 403 | https://blog.cardkingdom.com/the-importance-of-math-to-doing-the-thing-in-commander/ |
| F3 | Spellslinger Commander Deck Building Guide | Card Kingdom Blog | HTTP 403 | https://blog.cardkingdom.com/spellslinger-commander-deck-building-guide/ |

### Snippets (summaries or titles only; unverified)

| ID | Item | Note | URL |
|---|---|---|---|
| SN1 | Commander's Herald, The Top Ten cEDH Card Advantage Engines | Title only; cEDH, complementary | https://commandersherald.com/the-top-ten-cedh-card-advantage-engines/ |
| SN2 | Star City Games, Letting Go Of Tutors In Commander | Singleton structure tempts tutor overload | https://articles.starcitygames.com/articles/letting-go-of-tutors-in-commander/ |
| SN3 | Commander's Herald, Tutors Make Commander a Worse Format | Opinion: heavy tutoring is repetitive | https://commandersherald.com/tutors-make-commander-a-worse-format/ |
| SN4 | Wizards, Introducing Commander Brackets Beta; Card Kingdom, Brackets and Game Changers Update | Bracket tutor rules; outside scope | https://magic.wizards.com/en/news/announcements/introducing-commander-brackets-beta ; https://blog.cardkingdom.com/commander-brackets-game-changers-update/ |
| SN5 | Card Kingdom, Leveraging Virtual Card Advantage in Commander | Multiplayer-dilution claim; exact article unclear | https://blog.cardkingdom.com/leveraging-virtual-card-advantage-in-commander/ |
| SN6 | Draftsim, 5 Important Draft Tips for Commander Drafts; Card Kingdom, Best Tutor Packages for Budget Commander Decks | Draft priorities; one or two narrow tutors | https://draftsim.com/mtg-commander-draft-guide/ ; https://blog.cardkingdom.com/best-tutor-packages-budget-commander-decks/ |
| SN7 | TCGplayer, Enchantment Auras, Nadu and Pure Control Commander guides | Cheap tutors draw less pushback; Trinket Mage; control leans on card advantage | https://www.tcgplayer.com/content/article/How-to-Build-an-Enchantment-Auras-Commander-Deck-in-MTG/108517cc-7d9f-4000-a1b0-e68718ec45f1/ ; https://www.tcgplayer.com/content/article/Commander-MTG-Deck-Guide-Nadu-Winged-Wisdom/6dd54b01-9ff1-4a49-a14c-6672f41e5153/ ; https://www.tcgplayer.com/content/article/What-Does-a-Pure-Control-Deck-in-Commander-Look-Like/4bd8ed0a-7b22-48d3-a4a0-6b6c98fc0aca/ |
| SN8 | Commander's Herald, The Best Card Draw in Blue; The Best Card Draw in White | Do not count cantrips as draw | https://commandersherald.com/the-best-card-draw-in-blue/ ; https://commandersherald.com/the-best-card-draw-in-white/ |
| SN9 | Games Learning Society, "What is the 8 by 8 rule MTG?" and "rule of 8 in Commander deck building" | Domain not on the named list; not fetched | https://www.gameslearningsociety.org/wiki/what-is-the-8-by-8-rule-mtg/ ; https://www.gameslearningsociety.org/what-is-the-rule-of-8-in-commander-deck-building/ |
| SN10 | Proxy King; MTG EDH; CommanDollar (Tumblr) | Not on the named list; Proxy King and Tumblr: titles only | https://proxyking.biz/mtg-commander-consistency-without-tutors-redundancy-selection-and-density/ ; https://mtgedh.com/commander-redundant-effects/ ; https://commandollar.tumblr.com/post/146129269579/8x8-deckbuilding-theory |
| SN11 | Draftsim, Kiki-Jiki combos; Draftsim, Nekusar guide | Overlapping combo pieces: a plus, or a clash with the singleton spirit | https://draftsim.com/kiki-jiki-combos-mtg/ ; https://draftsim.com/nekusar-edh-deck/ |

## 1. Card draw: how many, which kinds, how the count changes

### Takeaway
Three sources (S1, S2, S3) put the baseline at 10 effective draw spells for a 99-card list. S5 (2026) implies 15 as the default, and the sources disagree on how the commander changes the count (Conflict 1). Experts rank draw by yield: multi-card and repeatable sources first, with conditional, plan-tied draw accepted but ranked lower (S2).

### Findings
- **Baseline.** S1's checklist runs 10 card-draw cards and calls itself a flexible guide [S1]. S2 sets 10 as the minimum for any Commander deck [S2]. S3 sets 10 for a commander that neither draws nor provides card advantage, and says the count depends on synergy, reliability and card-advantage need [S3].
- **Rationale.** S3 expects a player seldom needs to draw before about a tenth of the library is seen (a seven-card hand plus three turn-start draws), so ten spells keep a refill available [S3].
- **Commander effect.** S2 gives 15 to 20 for a commander built around drawing cards (examples: Jolrael, Morska) [S2]. S5 says a card-advantage commander may need 10 draw pieces instead of 15 [S5].
- **Curve and opponents.** S2: a low curve still needs 10 or more; a high curve, and opponents who regularly outdraw the table, call for more draw. No numbers given [S2].
- **Definitions.** Card draw is any effect that draws, including X spells, activated abilities, cantrips and draw-on-enter. Card advantage is a net gain: instant and sorcery cantrips net no card, while permanent cantrips that replace themselves do. Scry and surveil do not draw; S2 calls scry "virtual advantage"; looting is not addressed. Tutors are one-for-one, and Vampiric and Worldly Tutor are card disadvantage [S2].
- **Engines versus burst.** Repeatable sources (Throne of Eldraine, Emmessi Tome) give recurring draw without a sacrifice; one-shot sacrifice draw (Hedron Archive, Selesnya Locket, Dreamstone Hedron) gives several cards once [S2]. S2 ranks multi-card sources first, then cantrips and draw-on-enter, and says every type stays useful [S2].
- **Conditional and combat-tied draw.** S2 names a combat-tied category (Pride of Hull Clade draws when a high-toughness creature connects) and conditional X spells that pay off mid to late game. Symmetrical draw is not covered [S2].
- **Multiplayer.** Opponent-triggered draw is much stronger in multiplayer: repeatable, no upkeep, several cards per turn cycle. Wheel effects hand opponents card advantage [S3]. A Card Kingdom summary says the other three seats together pull about three cards per one of yours; the article is unclear, so unverified [SN5].
- **Selection and signs.** Extra draw lets you choose the best seven, and card quality counts as card advantage [S3]. S6 lists card selection as a fix for running out of action late, and an empty hand by turn 6 as a sign of too little draw [S6]. S2 says the mana base should keep pace with draw, with no number [S2]. With light tutoring run 10 or more draw spells; with heavy tutoring the best 5 are enough [S1].
- **By strategy.** No fetched source gives a number for spellslinger, go-wide, voltron, landfall, control or symmetrical draw. Snippets only: a Card Kingdom spellslinger summary (F3, not read) says spellslinger needs a critical mass of instants and sorceries, since each creature, enchantment or artifact means fewer instant and sorcery draws; a TCGplayer summary says control leans on card advantage [SN7]; a Commander's Herald summary says not to count cantrips as draw [SN8].

### Inferences
- Use 10 effective draw pieces as the floor for a 99-card list, then adjust for commander and curve. S5 conflicts with S2 on the commander effect; treat that part as open (Conflict 1).
- Conditional, plan-tied draw counts as a draw piece at a lower weight than repeatable multi-card draw. S2 supports the ranking but gives no weight. The owner's Eagle Vision lesson (a cheap draw tied to combat that a score-driven builder dropped) fits S2's combat-tied category.
- Scry and looting are card selection under S2's definitions, not draw. They find the cards the plan needs rather than meeting the draw count [S3, S6].
- The owner's observation that instant-heavy decks empty their hand fastest is consistent with S2's advice that higher curves need more draw and with S6's empty-hand sign. No fetched source says it about instants, so it is unverified.

### Gaps
- No source quantifies draw by strategy (spellslinger, go-wide, voltron, landfall, control) or symmetrical draw. Looting has no source.
- F1 and F2 (Karsten and Card Kingdom probability math) were not read.

## 2. Tutors: role, number, targets

### Takeaway
Tutors substitute for redundancy: each finds one card, so a list can cut backups [S1]. The fetched sources give small counts (two on a budget [S1]; a small handful, suggested by S2) and do not separate tutoring for the engine from tutoring for the win. Tutors are not card advantage [S2], so they sit outside the draw count.

### Findings
- S1: two flexible tutors on a budget, more at higher budgets (its no-limit example is ten). Tutors let you cut weaker cards and fetch the best card when needed; locating key cards is the minimum [S1].
- S1: each card drawn is another chance at the card you need, so draw substitutes for pricey tutors [S1].
- S2 suggests a small handful of tutors, not a fixed number. S5 and S6 do not state tutor counts [S2, S5, S6].
- Scope of S1: budget casual or semi-competitive decks that finish around turns 8 to 12. It says cEDH decks, which aim for turn-3 wins, typically run about 30 lands, 16 to 20 ramp and many more tutors. That is complementary evidence for cEDH only [S1].
- Archetype (snippets): cheap, low-impact tutors draw less pushback [SN7]; one or two narrow tutors can be worth it without a combo plan [SN6]; Trinket Mage and Green Sun's Zenith keep combo pieces accessible [SN7].
- Opinion (snippets): the singleton structure tempts tutor overload, since each tutor takes a slot another card could use [SN2]; heavy tutoring makes games repetitive [SN3].
- Brackets (snippet): Wizards' Bracket 1 keeps tutors to a minimum, and an October 2025 change reportedly dropped a tutor restriction and routes the strongest tutors through Game Changers [SN4]. Unverified and outside this note; the bracket researcher must check the official page.

### Inferences
- Count tutors on their own line: they cut redundancy [S1] and add no card advantage [S2].
- Tutoring for the win versus the engine (inference from S1's roles; no source states it). A tutor is most useful for the single payoff or finisher, which S1 separates as its I-Win card. An engine (repeatable draw or mana) should come from cards already in the list, so the plan does not depend on one tutor. S5's advice to carry several finishers supports more than one win route [S5].
- The tutor count should follow the plan's win routes, not a fixed total (inference). S1's two-tutor budget is a floor, not a target.

### Gaps
- No source separates engine tutoring from win tutoring or gives tutor targets per plan. Bracket tutor rules rest on unverified snippets.

## 3. Redundancy and probability

### Takeaway
Named-source practice sets a number per function and backs up key effects and finishers [S1, S5]. The readable probability evidence is thin: S1's ramp odds reproduce, its land odds do not. The "rule of 8" and "8x8" heuristics have no named-domain source. In a singleton 99-card deck, eight distinct cards for one function are seen by turn 3 on the draw in about 59% of games (computed), so every-game coverage needs more cards seen, not only more backups.

### Findings
- **Ramp odds.** S1: 14 ramp cards give 80% odds of casting one by turn 3 without mulligans; 20 give 90% [S1]. Computed: 79.9% and 90.8% with 10 cards seen (seven-card hand plus three draws); with 9 cards seen (on the play), 76.2% and 88.1%. So S1's "by turn 3" must count 10 cards.
- **Land odds.** S1: 36 lands are roughly the floor for 90% three-plus lands by turn 3 and 74% four-plus by turn 4; 39 to 40 lands give 80% four-plus by turn 4 (Muldrotha example). S1 says its land math assumes older mulligan rules and no scry [S1]. Computed without mulligans: 78.0% (three-plus by turn 3, 10 cards), 62.1% (four-plus by turn 4, 11 cards), and 72.6% at 40 lands. Not reproduced (Conflict 3).
- **Checklist.** 37 lands, 13 ramp, 10 draw, 6 targeted removal, 3 board wipes, 2 recursion, 2 tutors, 1 graveyard hate and 1 I-Win card; the remaining 24 slots are theme cards [S1]. S1 applies the same redundancy logic to graveyard hate, board wipes and removal as to tutors [S1].
- **Backups and finishers.** S5 recommends backups for the commander's key effect (Panharmonicon as a backup for Elesh Norn's trigger, in its example), protection for a commander that is the main route, and several big finishers, since one counterspell can stop a lone win condition. It names Thassa's Oracle with Demonic Consultation as finishers that can close games about as well as Craterhoof Behemoth [S5].
- **Packages.** S4 (2016; examples from two decks) describes cheap artifacts, deathtouch pingers, retrace spells, flash enablers and double-spell enablers that set off one trigger. It does not name redundancy as a term [S4].
- **Non-named heuristics (snippets, unverified).** An 8x8 framework: eight effect categories, eight cards each, plus 35 lands [SN9]. A "rule of 8": eight copies make a card reasonably likely in the opening hand, which is 60-card logic [SN9]. Two to four backups for support roles, five to eight for regular roles and eight to twelve for plan-critical functions [SN10]. A named-domain search for "8x8" found no 8x8 article.

### Computed (our arithmetic, not a source)
Setup: 99-card library; no mulligans, scry or extra draws. Seen cards: on the play, by turn T = 7 + (T − 1); on the draw, 7 + T. P(at least one of k distinct cards) = 1 − C(99 − k, n) / C(99, n), with n the seen cards.

| k distinct cards | T3 play (9 seen) | T3 draw (10) | T5 play (11) | T5 draw (12) | T7 play (13) | T7 draw (14) |
|---|---|---|---|---|---|---|
| 1 | 9.1% | 10.1% | 11.1% | 12.1% | 13.1% | 14.1% |
| 2 | 17.4% | 19.3% | 21.1% | 22.9% | 24.7% | 26.4% |
| 3 | 25.1% | 27.6% | 30.0% | 32.4% | 34.8% | 37.0% |
| 4 | 32.1% | 35.1% | 38.1% | 40.9% | 43.6% | 46.2% |
| 6 | 44.4% | 48.1% | 51.6% | 54.9% | 58.0% | 61.0% |
| 8 | 54.7% | 58.7% | 62.5% | 65.9% | 69.0% | 71.9% |
| 10 | 63.3% | 67.4% | 71.0% | 74.3% | 77.3% | 79.9% |
| 12 | 70.4% | 74.3% | 77.8% | 80.8% | 83.5% | 85.8% |

- Seen cards for 80%: 33 (k=4), 23 (k=6), 18 (k=8), 15 (k=10), 12 (k=12); for 90%: 43, 31, 24, 20, 17. On the draw these are turns 26, 16, 11, 8, 5 (80%) and 36, 24, 17, 13, 10 (90%).
- Commander analogue of "eight copies in the opening hand": 8 distinct cards among the opening seven, 45.6%. Complement only, 60-card deck: four copies in the opening seven, 39.9%; eight copies, 65.4%.

### Inferences
- For a function needed by turn 7 on the draw in about 80% of games, the table says about 10 distinct cards (79.9%); eight give 71.9%. Eight backups are not an every-game guarantee by mid-game.
- The other lever is more cards seen: draw and tutors raise the seen count for every function at once. This is the mechanism behind S1's draw-for-tutor substitution.
- Commander is singleton, so 60-card "copies" logic does not carry over. Count distinct cards per function and per turn.
- State the assumption behind any "by turn N" claim: 9 versus 10 cards seen moves the ramp odds by about 3 points.

### Gaps
- No named-domain source for 8x8 or for the rule of 8 in singleton decks.
- F1 and F2 were not read. The F2 summary's figure (about 77% for at least two of 25 theme cards by turn 3) is unverified; computed under the same assumptions it is 77.65% (Conflict 5).
- A non-named article (Proxy King, "consistency without tutors") may cover this question; it was not fetched.

## 4. Raising the floor: quality, synergy, combos

### Takeaway
Named sources back one focused plan, on-plan cards with more than one job, efficient interaction and a low curve. S4 (2016) and S5 (2026) support synergy over staples. No source quantifies the trade-off; S1, S5 and S6 do not frame card quality versus quantity as a principle.

### Findings
- S4: each card should push the plan; widely played staples are the most damaging to a theme; fit can outweigh efficiency (a token deck favored two on-theme answers over Naturalize). A commander that neither anchors nor supports the plan leaves the deck clunky. Off-plan answers stay when the deck needs them to survive; answers that also advance the plan are preferred [S4].
- S5: prioritize cards with several jobs; a single-role card must excel at its one job. Judge removal by diversity, efficiency and relevancy. Board wipes are weak for enjoyment, so run one only as a finisher. Value alone seldom ends games [S5].
- S6: re-check older staples against today's faster Commander; high-cost cards with no board impact deserve scrutiny; keep efficient removal in every deck; symmetrical sweepers hurt creature-heavy plans; keep the curve low and pair expensive additions with costed swaps [S6].
- S1: one I-Win card, a finisher that ends the game the turn it is cast with little setup. A finisher that is easy to disrupt stalls [S1].
- S3: card quality counts as card advantage, and extra draw lets you select [S3].
- Snippet: in multiplayer pods, conventional draft priorities such as curve and removal should yield to card depth [SN6].

### Inferences
- A synergy card earns its slot when it does its plan's job and something useful alone (S5's one-job test). A card that is dead alone fails that test. This fits the owner's dead mini-combo lesson, but no source states it as a rule.
- A two-card combo can be one finisher among several [S5], not the only route; S1 names the same risk for a finisher that is easy to disrupt.
- Keep a staple when it does two jobs [S5] or is interaction the deck needs to survive [S4, S6]; cut it when it only does a generic job outside the plan [S4, S5].

### Gaps
- No source quantifies synergy against staples or the cost of dead pieces. Two-card combos versus engines have only S5's finisher examples.

## 5. Diagnosing and fixing an inconsistent deck

### Takeaway
The fetched diagnostics are short [S6]: one-land hands point to too few lands, an empty hand by turn 6 to too little draw, running dry late to too little action or selection, and a repeated unexplained problem to the list itself. The fixes named: add lands rather than cut them; cut cards outside the one plan; group the list by function to expose gaps; add backups for the key effect and a second finisher.

### Findings
- S6: mistakes usually show across several games; have trusted players review the list; discuss pivotal turns; name each mistake and plan a fix [S6].
- S6: add lands rather than cut them; use utility lands and card advantage against flood; target about 36 or more when swapping. When a color keeps failing, swap colorless lands for colored sources; 4- and 5-color decks should probably skip them [S6].
- S1: a checklist of counts exposes gaps before playtesting; cutting mana is a trap, since it makes strong cards less likely to be cast [S1].
- S5: group the 99 by function (ramp, card draw, countermagic and so on) to expose off-theme cards, surplus effects and gaps. Center the deck on one main plan; subthemes are fine if they support the core; if unsure, try several strategies and keep the one that holds up [S5].
- S5: ramp adds to land drops rather than replacing them; a turn-2 Signet only helps if the third land drop arrives [S5].

### Inferences
- A possible order (ours, not a source's ranking): (1) mana counts first, since S6's first sign is a mulligan of one-land hands; (2) cut second and third plans and off-theme cards [S4, S5]; (3) add draw or selection where hands empty [S2, S6]; (4) add backups for the key effect and a second finisher [S5]. Lower the curve when hands fill with 4-plus drops [S6]; add ramp when key cards are expensive [S1].
- The owner's failure pattern (several plans with one to three support cards each) is covered by S5's single-plan rule; no fetched source names it as a failure mode.

### Gaps
- No numeric diagnostic threshold beyond S6's 36-land target and its empty-hand sign. No formal audit method; S5's function grouping is the nearest.

## Conflicts between sources

1. **Baseline and the commander effect.** S1, S2 (minimum) and S3 (no card-advantage commander) say 10; S5 implies 15. S2 and S5, both Draftsim (2024 and 2026), point in opposite directions: S2 says a draw-built commander needs 15 to 20, while S5 says a card-advantage commander can drop from 15 to 10. Neither reconciles them.
2. **Land count.** S1: 37 with a 36 floor. S6: 36 target, 38 as the author's usual. S5: about 40, including 3 to 5 modal double-faced cards or landcyclers. S5 flags 30 as a possible mistake, and S6 calls 33 undersized. Range: 36 to 40. Modal double-faced cards are banned in this project (reversible cards), so only the landcycler part of S5 transfers.
3. **Land odds (S1) versus recomputation.** Ramp odds reproduce; land odds do not: 78.0% against 90%, 62.1% against 74%, and 72.6% at 40 lands against 80% at 39 to 40. S1's stated mulligan assumption may explain the gap, but no model is given. Use S1's land numbers only after F1 is read.
4. **Tutors and redundancy.** S1 says tutors reduce redundant cards; opinion snippets say heavy tutoring is repetitive or tempting [SN2, SN3]. A disagreement about value, not a data conflict.
5. **Redundancy heuristics.** Snippets give 8 per category [SN9], 2 to 4, 5 to 8 and 8 to 12 backups by role [SN10], and an eight-copy rule that is 60-card logic [SN9]. Computed: eight distinct cards reach 58.7% by turn 3 on the draw and 71.9% by turn 7. The F2 summary's 77% for at least two of 25 theme cards by turn 3 matches the computed 77.65% on the draw (10 seen), so the magnitude is consistent, though the summary itself is unverified. Eight is not an every-game count before mid-game.
6. **Singleton overlap.** Draftsim's Kiki-Jiki summary treats overlapping combo pieces as a plus; its Nekusar summary says they can clash with the singleton spirit [SN11]. Opinion.
7. **Scry and looting.** S2 says scry is not draw and does not address looting; S3 and S6 value selection. A classification gap, not a numeric conflict.
8. **Bracket tutor rules.** Snippets describe a Bracket 1 tutor minimum and an October 2025 change [SN4]. Not checked here.

## Gaps (consolidated)

1. F1 (Karsten, Commander source math) could not be read: the redirect returned no body. Karsten is the main primary source missing for question 3. A second Karsten summary (Verge Lands) does not define its event, so it is not used.
2. F2 and F3 (Card Kingdom) returned HTTP 403; their summaries are not evidence.
3. No named-domain source for: 8x8; the rule of 8 in singleton decks; draw counts by strategy; engine versus win tutoring; looting counts; the dead-alone piece rule; numeric diagnostic thresholds. The cEDH engines article (SN1, complementary) was not read.
4. Snippet-only sources are unverified. S1 (2020), S3 (2021) and S4 (2016) predate the current Bracket system and card pool, so their counts may be dated.
5. Bracket rules are outside this note; the bracket researcher should check Wizards' current page.
6. Non-named domains (Games Learning Society, Proxy King, MTG EDH, a Tumblr post) were not fetched under the named-source rule; the owner can add them to the list if wanted.
7. Method limit: 22 calls, above the 15-call guideline; fetched pages are model summaries, not rendered text.
