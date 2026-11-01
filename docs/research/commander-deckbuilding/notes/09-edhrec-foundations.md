# Commander deckbuilding: EDHREC and The Command Zone, foundations

Researcher notes, read 2026-10-31. Scope: Commander only. Access: owner-authorized (decision of 2026-10-31). About 36 HTTP requests were made with curl, in short batches with pauses between requests. No CAPTCHA, login or bot wall was bypassed; one JSON path answered 403 AccessDenied and was not pursued. The 2025 Command Zone episodes were reachable only through EDHREC's mirrors. WebSearch was used only to find URLs; its summaries are not cited. "Undated" means no date appeared on the page.

## Sources

| ID | Title | Author (as shown) | Date | URL |
|---|---|---|---|---|
| S1 | The Command Zone 658: Commander Deckbuilding Template for the New Era (show notes, EDHREC mirror) | EDHREC account "contentadmin"; hosts per S4 | 2025-02-18 | https://edhrec.com/articles/the-command-zone-commander-deckbuilding-template-for-the-new-era-the-command-zone-658-mtg-edh-magic-gathering |
| S2 | The Command Zone 659: The Problem with Deckbuilding Templates (show notes, EDHREC mirror) | contentadmin | 2025-02-26 | https://edhrec.com/articles/the-command-zone-the-problem-with-deckbuilding-templates-the-command-zone-659-mtg-edh-magic-gathering |
| S3 | The Command Zone #151: The Commander Deck Building Template (show notes, WordPress) | TCZ (no byline in the REST data) | 2017-03-21 | https://commandzone.com/2017/03/21/commander-deck-building-template-151/ |
| S4 | The Command Zone home page (site description, JSON-LD) | TCZ | read 2026-10-31 | https://commandzone.com/ |
| S5 | Superior Numbers - Land Counts | Dana Roach (slug dana-roach) | 2019-02-20 | https://edhrec.com/articles/superior-numbers-land-counts |
| S6 | Superior Numbers - Exotic Orchard | Dana Roach | 2018-09-07 | https://edhrec.com/articles/superior-numbers-exotic-orchard |
| S7 | From Synergy to Lift: The Math Behind EDHREC's New Era of Recommendations | slug juliam (full name not verified) | 2025-12-15 | https://edhrec.com/articles/from-synergy-to-lift-the-math-behind-edhrecs-new-era |
| S8 | Commander Philosophy - The Difference Between Synergy and Exploiting | slug alexwicker | 2025-05-01 | https://edhrec.com/articles/commander-philosophy-the-difference-between-synergy-and-exploiting |
| S9 | Frequently Asked Questions | EDHREC | undated | https://edhrec.com/faq |
| S10 | EDHREC Guide to Commander Brackets | Cooper Gottfried | page date 2025-09-22; text cites a 2025-10-22 update | https://edhrec.com/guides/edhrec-guide-to-commander-brackets |
| S11 | WOTC Introduces New Bracket System for Commander | Matt Morgan | 2025-02-11 | https://edhrec.com/articles/wotc-introduces-new-bracket-system-for-edh |
| S12 | Wizards of the Coast Commander Brackets Update for October 2025 | Matt Morgan | 2025-10-22 | https://edhrec.com/articles/wizards-of-the-coast-commander-brackets-update-for-october-2025 |
| S13 | Commander Ban List Update - Feb 9, 2026 | Matt Morgan | 2026-02-09 | https://edhrec.com/articles/commander-ban-list-update-feb-9-2026 |
| S14 | Should the Bracket System Move Out of Beta? | Levi Perry (slug leviperry) | 2026-09-03 | https://edhrec.com/articles/should-the-bracket-system-move-out-of-beta |
| S15 | Building Combos for Casual Commander | Levi Perry | 2026-07-14 | https://edhrec.com/articles/building-combos-for-casual-commander |
| S16 | Should You Run More Removal in Commander? | Cas Hinds (slug cashinds) | 2025-09-08 | https://edhrec.com/articles/should-you-run-more-removal-in-commander |
| S17 | EDHREC Guide to Upgrading Your Commander Deck | Cooper Gottfried | page date 2025-10-13 | https://edhrec.com/guides/edhrec-guide-to-upgrading-your-commander-deck |
| S18 | Digital Deckbuilding: The How-to Guide to Building a Commander Deck Using EDHREC, Archidekt and Commander Spellbook | John Sherwood | 2024-04-17 | https://edhrec.com/articles/digital-deckbuilding-the-how-to-guide-to-building-a-commander-deck-using-edhrec-archidekt-and-commander-spellbook |
| S19 | Different Approaches To Building a Commander Deck | Cas Hinds | 2025-09-01 | https://edhrec.com/articles/different-approaches-to-building-a-commander-deck |
| S20 | EDHREC JSON endpoints and average-deck page (section 6 lists each URL) | EDHREC | read 2026-10-31 | https://json.edhrec.com/ ; https://edhrec.com/average-decks/atraxa-praetors-voice |

## 1. The Command Zone template and the 2025 "new era"

**Takeaway.** The 2025 template is published as show notes that name its categories and say it sets ideal ratios for ramp, card draw and disruption. The notes contain no numbers, so the exact counts are a gap.

Cited findings
- TCZ 658 (2025-02-18) presents a revised template that sets ratios for ramp, card draw, disruption and similar categories, based on the hosts' deckbuilding experience [S1].
- The 658 timestamps list the template's parts in order: Lands, Card Advantage, Ramp, Targeted Disruption, Mass Disruption, Using Categories, the Commander Deckbuilding Template, Plan Cards, Mana Curve, a Commander Curve Template, and a closing section on complications [S1].
- TCZ 659 (2025-02-26) calls the new template over-simplified rather than wrong. It argues that a template is a starting point, not paint-by-numbers, and that bending or breaking its rules is often correct [S2].
- The 659 timestamps give one exceptions segment per category: Ramp (00:15), Card Advantage (00:34), Targeted Disruption (00:50), Mass Disruption (01:05) and Lands (01:10). Two later segments cover the magic number and the math. The notes give no number for either [S2].
- The 658 notes link the material behind the template: TCZ 379 (the earlier template, whose URL is not in the page), TCZ 453 (mana curve), TCZ 455 (lands), TCZ 596 (playtesting), TCZ 656 (cards in the 99), a land-count analysis by Frank Karsten, and two mana calculators. I read only the titles [S1].
- The 2017 template episode (TCZ 151) frames building each deck from a basic template and links episodes on card advantage and mana bases. Its notes contain no counts [S3].
- The hosts are Jimmy Wong and Josh Lee Kwai [S4].

How they adjust by strategy. The sources name the mechanism (a ratio per category, then exceptions per category) but give no table by strategy or by bracket [S1, S2].

Inference. A builder can cite the categories and the existence of exceptions from TCZ. Any numeric ratio must come from another source and be labelled as such.

Gaps. The 2025 numbers; the content of the magic-number segment; the numbers of the 379 template; transcripts. The first wave's 403 on the template page was not retried; the 2025 notes were read through the EDHREC mirror.

## 2. EDHREC data: averages, what they measure, and their limits

**Takeaway.** EDHREC's averages are the average of the decks in its sample, by power label or by theme. They show what popular lists contain, not what is best. Measured functional averages (ramp, draw, removal, wipes) are not published; the figures for those come from authors' rules of thumb.

### 2.1 The 2019 land study
- EDHREC's average deck in its 2019 database ran "just over 29" lands and about 4.15 mana rocks. Decks added in the previous year averaged 31 lands [S5].
- A test of 100 goldfished random decks: 26% missed the turn-3 land drop and had no mana source by turn 3; a further 21% missed the drop but could cast a mana source [S5].
- The cEDH decks cited average 1.68 to 2.04 mana value, against a 3-or-more average in the database, and run fewer lands [S5].
- EDHREC writer Nate Burgess's rule of thumb, as quoted: lands = 31 + the number of colours in the commander's colour identity + the commander's mana value, with zero-cost rocks counted as lands [S5].
- The author judges the average too low outside tuned cEDH. He also states that preconstructed Commander decks average over 37 lands; no source is given for that figure (unverified) [S5].
- Landfall and other themed decks may run fewer rocks and more land-ramp spells, according to the author's reasoning and one example [S5].

### 2.2 Current averages by power label, one commander (JSON)
Atraxa, Praetors' Voice, EDHREC sample, read 2026-10-31. Each row is the average deck for that label, not a recommended build [S20].

| Label | Creature | Instant | Sorcery | Artifact | Enchant. | Planeswalker | Lands (basic / nonbasic) | Mana curve: cards at 0/1/2/3/4/5/6/7 |
|---|---|---|---|---|---|---|---|---|
| All (default) | 24 | 10 | 8 | 9 | 7 | 5 | 36 (13 / 23) | 1/8/18/16/10/6/3/1 |
| Exhibition (1) | 26 | 8 | 8 | 10 | 7 | 4 | 36 (16 / 20) | 1/8/21/16/9/5/2/1 |
| Core (2) | 27 | 9 | 9 | 9 | 7 | 3 | 35 (13 / 22) | 1/7/20/17/9/5/3/1 |
| Upgraded (3) | 24 | 9 | 9 | 9 | 7 | 6 | 35 (11 / 24) | 1/7/18/16/10/6/4/1 |
| Optimized (4) | 21 | 11 | 8 | 9 | 7 | 7 | 36 (10 / 26) | 2/9/17/15/10/5/4/1 |
| cEDH (5) | 21 | 15 | 8 | 9 | 7 | 5 | 34 (9 / 25) | 3/15/16/14/8/4/3/1 |
| Budget | 27 | 9 | 9 | 9 | 6 | 2 | 37 (20 / 17) | 1/6/22/17/9/5/2/1 |
| Expensive | 21 | 12 | 8 | 10 | 7 | 7 | 34 (4 / 30) | 2/11/16/15/10/5/4/1 |

Checks on these numbers (our arithmetic on the JSON):
- In all nine averages checked (these eight, plus the Edward Kenway ramp average in 2.4), type counts plus lands total 99. With the commander that is 100, so the commander appears to be excluded from the counts (inference).
- The mana-curve total differs from the non-land total by one in six of the nine averages. The cause is not stated; rounding is a hypothesis.
- Lands do not fall with power: 36, 35, 35, 36, 34 across labels 1 to 5; budget is 37 and expensive is 34.
- Cheap spells and instants rise with power: one-drops 8 to 15 and instants 8 to 15 from Exhibition to cEDH. Planeswalkers vary from 2 to 7 with no trend.

### 2.3 Functional counts: authors' rules of thumb, not measured averages
The EDHREC upgrade guide [S17] gives these rules of thumb:
- Ramp: about 10. Big-mana commanders may need up to 15, and the author has seen up to 20. Low-curve creature decks need less. His personal minimum is seven.
- Removal: about 10. Aggressive decks can run 5 to 7; a long-game deck (the example is Shorikai) 15 or more.
- Card advantage: 12 or more.
- Board wipes: two is usually enough. Decks with few permanents may want more; one-sided wipes suit decks that commit to the battlefield.
- Graveyard hate: at least one piece.
- Worked example: the author revises EDHREC's average list for a +1/+1 counters deck (Hamza). He cuts three ramp spells, saying the list does not need 15 more ramp pieces; it has five removal pieces, which he expands; and he says it already has 12 card-advantage pieces [S17]. These are his readings of one list.

No source read gives measured averages of ramp, draw, removal or wipe counts per deck.

### 2.4 By colour count and by archetype
- No averages by colour count were retrieved. The only colour-count link is the rule of thumb in 2.1 [S5].
- One theme average was read: ramp for Edward Kenway [S20]. It shows 35 lands, 28 creatures, 6 instants, 4 sorceries, 20 artifacts, 6 enchantments and no planeswalkers. Its bracket_counts sum to 16 decks, so the sample is small (inference).
- EDHREC's developers define themes by tuning counts, not by a formula; the FAQ says so [S9]. Theme averages inherit that uncertainty.

### 2.5 The average of popular decks versus best practice
- EDHREC's FAQ says its statistics are computed from decklists on popular deck-building websites [S9]. An average describes those decks.
- The lift article says most decks in its calculations are not built optimally, and that the metrics describe average deckbuilder behaviour, not quality [S7].
- The 2019 land article treats the average as below best practice [S5]. The 2025 upgrade guide calls the average list "by no means bad", but improvable [S17].
- The 2018 Exotic Orchard article describes a "precon effect": precon decklists entered into deck tools feed EDHREC's suggestions and reinforce the same cards. The article counts 31,793 decks for Exotic Orchard at that time [S6]. Nothing in the pages read corrects this bias.

## 3. Fundamentals, consistency and card evaluation

**Takeaway.** EDHREC's fundamentals are rules of thumb. Its consistency arguments are qualitative. Its card-evaluation guidance says that synergy and popularity are not power.

### 3.1 The upgrade guide's template
- Four "vegetables" of deck building: ramp, removal and card advantage in every deck, with board wipes and graveyard hate [S17].
- Card advantage is presented as the easiest way to make a list feel more consistent [S17].

### 3.2 Consistency
- Removal article: singleton Commander has no four-ofs, which in other formats give consistency, so more distinct removal pieces are needed. The author says he has no statistic on whether more removal wins and asks for one. His advice: check with the pod, and consider being the threat instead [S16].
- Combos: consistency in assembling a combo's pieces matters more than the combo's raw power. Tutor-heavy lists find their pieces more reliably than lists that rely on natural draws (author's argument) [S15]. Organic combos use cards the deck wants anyway (for example Gravecrawler with Phyrexian Altar in a Zombie deck); inorganic combos are added for the win [S15].
- A Bracket 3 deck should show a cohesive plan across its groups of cards, not a set of loose parts [S10].

### 3.3 Card evaluation
- Synergy is not power. EDHREC's example: Path to Exile has −1% synergy in Ur-Dragon decks, and a card that is popular in a colour identity is not thereby a good choice [S8].
- Colloquially, synergy means fit with the deck's theme. The author treats Game Changer status of cards like Urza as a question of playstyle, not of synergy alone [S8].
- Mechanic-first building is, by the author's account, "the most popular building type" [S19].

### 3.4 Workflow
- Digital deckbuilding (2024): choose a commander from EDHREC's rankings and tags, then export the average deck to Archidekt as a starting list [S18].

### 3.5 Owner's lessons, checked against these sources

| Lesson | What the sources say | Status |
|---|---|---|
| Landfall needs far more ramp | Landfall decks may run fewer rocks and more land-ramp spells [S5]; no total counts | Partly supported; total unverified |
| Instants decks need the most draw | No draw-by-instant guidance; the guide gives only 12+ card advantage [S17] | Gap |
| Attackers need haste, team evasion, protection and defence | Not in the pages read; the guide says aggressive decks need cheap refills and fewer removal spells [S17] | Gap |
| Mixed plans lose to focused plans | Cohesive-plan requirement [S10]; combo consistency [S15] | Supported as author opinion |
| Score-driven builders cut role-players | Popularity and synergy are not power [S8]; minimum counts for removal and card advantage [S17] | Consistent with EDHREC; not tested |

## 4. Brackets, 2025 and 2026

**Takeaway.** EDHREC's summaries of WotC's bracket system agree on the five brackets, the turn expectations and the restriction tiers. The Bracket 3 Game Changer limit and the combo rule should be checked against WotC's own text, which I did not read.

### 4.1 Launch, 2025-02-11 [S11] (EDHREC's summary of WotC's announcement)
- Five brackets: Exhibition (1), Core (2), Upgraded (3), Optimized (4), cEDH (5).
- Bracket 1: no Game Changers; no intentional two-card infinite combos, mass land denial or extra-turn cards; tutors sparse.
- Bracket 2: no Game Changers; no intentional two-card infinite combos or mass land denial; extra turns only in low quantity; tutors sparse. EDHREC's framing: the average precon sits at Core.
- Bracket 3: up to three Game Changers; no intentional early-game two-card infinite combos; extra turns in low quantity; no mass land denial.
- Brackets 4 and 5: no restrictions beyond the banned list.

### 4.2 Update, 2025-10-22 [S12] (EDHREC's summary of WotC's update, by Matt Morgan)
- Turn expectations: at least nine turns (Bracket 1), eight (2), six (3) and four (4); cEDH games can end on any turn.
- Precons are no longer tied to Bracket 2 [S12, S13].
- Some iconic cards were removed from the Game Changers list. The subtitle says so; the cards are not named in the part read [S12].
- WotC's panel acknowledged that some heuristics were unclear, such as "no early-game combos" and the limit on tutors [S12].
- Expected cards: Bracket 3 Game Changers should be value engines or game-enders; Bracket 4 fast mana, resource engines, free disruption and tutors [S12].
- The author's view: six turns for Bracket 3 is optimistic; four for Bracket 4 is close [S12].

### 4.3 EDHREC's bracket guide (text cites the 2025-10-22 update) [S10]
- Same five brackets and turn expectations (9, 8, 6 and 4; cEDH none).
- Restrictions shown: Brackets 1 and 2 bar two-card combos (game-enders, lockouts, infinites); Brackets 4 and 5 have no restrictions beyond the banned list. The guide gives no Game Changer number for Bracket 3. A search of its text and HTML for "up to three" and "three Game Changers" found nothing; my paragraph filter drops short bullets, but the search does not.
- Examples: one commander (Lumra) built once per bracket. The Bracket 3 build runs 46 lands (27 basics) and three Game Changers. The Bracket 4 build cites 21 combos and the Bracket 5 build 29, per Commander Spellbook. These are illustrative lists, not averages [S10].
- The author suggests most players start at Bracket 2 or 3 (opinion) [S10].

### 4.4 2026 changes and status
- 2026-02-09 [S13]: Biorhythm unbanned; Lutri, the Spellchaser unbanned but banned as a companion. A separate article by Gavin Verhey (WotC's Commander Format Panel head) adds one Game Changer, Farewell, per EDHREC's report; the WotC article itself was not read. The article quotes Verhey saying that precons were decoupled from Bracket 2 in the last update.
- 2026-07-14 [S15]: the author reads Bracket 3 as allowing two-card infinite combos after turn six, and Brackets 4 and 5 as allowing combos. He notes that no bracket mentions combos of three or more cards. These are his readings, not official text.
- 2026-09-03 [S14]: the bracket system is still in beta; the last update was October 2025. The author concludes it is not ready to leave beta. Problems named: a wide spread inside each bracket (a low-floor deck and a high-ceiling deck), turn expectations that work as conversation rather than rules, Voltron and Stax decks, and a Game Changers list "as of February 2026" [S14].
- EDHREC's April 2026 Bracket combo vote appears only in a search summary; not read.

## 5. Reading EDHREC synergy, inclusion and lift

**Takeaway.** Inclusion, synergy and lift measure how often cards run together, relative to the decks that could run them. None of them measures quality.

- Potential decks: EDHREC compares decks that include both cards with potential decks, the decks that could include both. A potential deck must be able to run both cards: the commander, colour identity and the dates when each card was previewed are considered. Active filters (budget, bracket, tag) narrow potential decks too [S9].
- Synergy (the older metric): the share of the commander's decks that run a card, minus the share of decks in the commander's colour identity that run it. EDHREC's example: a card in 81% of Ur-Dragon decks and 11% of five-colour decks has 70% synergy [S8]. Synergy is asymmetric and ranges from −100% to +100% [S7].
- Lift (from December 2025): the probability of two cards appearing together, divided by the product of their individual probabilities. 1 means independence; above 1 means they appear together more often than chance. Lift is symmetric [S7].
- Ubiquitous cards (all basics, Swords to Plowshares, Arcane Signet, Sol Ring and Command Tower, each in more than half of candidate decks) distorted synergy; lift keeps them near 1. The median lift across card pairs is 1.58 [S7].
- Commander pages still used synergy in December 2025 because of their many filters, which EDHREC was still optimising [S7].
- EDHREC's own limits: most decks in the data are not built optimally, so the metrics show average behaviour, not quality [S7]. Synergy does not show how powerful a card is [S8]. The statistics can also shape what players build [S7].
- Our check on the JSON: the Atraxa commander page carries both fields. Sol Ring: lift 0.979, synergy −0.018, in 39,153 decks [S20]. Tekuthal, Inquiry Dominus: 30,816 of 46,056 potential decks, which is 66.9% (our arithmetic), with synergy 0.270 [S20].
- Practical reading: a high inclusion with low synergy means a staple that many decks run. High synergy means the card is unusually common in that commander's decks compared with its colour identity. Neither says the card is good [S8, S9].

## 6. EDHREC JSON: URLs that work, fields and examples

Endpoints tested on 2026-10-31 [S20]:

| URL | Result | Content |
|---|---|---|
| json.edhrec.com/pages/commanders/atraxa-praetors-voice.json | 200, 131,158 B | commander page: counts, bracket, budget and tag counts, cardlists, panels |
| json.edhrec.com/pages/average-decks/atraxa-praetors-voice.json | 200, 62,830 B | average deck: counts, deck.cards, cardlists |
| json.edhrec.com/pages/average-decks/atraxa-praetors-voice/{exhibition, core, upgraded, optimized, cedh, expensive, budget}.json | 200 for all seven | power-label and budget variants |
| json.edhrec.com/pages/commanders/atraxa-praetors-voice/upgraded.json | 200, 119,582 B | commander page, Upgraded variant |
| json.edhrec.com/pages/average-decks/edward-kenway/ramp.json | 200, 39,177 B | theme variant (tag ramp) |
| json.edhrec.com/pages/commanders/edward-kenway/ramp.json | 200, 105,217 B | commander page, ramp variant |
| json.edhrec.com/pages/themes/landfall.json | 403 AccessDenied (XML) | not pursued |
| json.edhrec.com/pages/average-decks/atraxa-praetors-voice-upgraded.json | 403 AccessDenied (XML) | wrong path shape |
| edhrec.com/average-decks/atraxa-praetors-voice | 200, HTML 444,131 B | HTML average-deck page; not parsed |

Fields (examples from the Atraxa commander JSON unless stated):
- Card-type counts at top level (creature, instant, sorcery, artifact, enchantment, battle, planeswalker, land, basic, nonbasic), plus similar (similar commanders). Example: creature 24. The top-level counts equal the average-deck counts.
- bracket_counts: {"1":154,"2":3167,"3":4099,"4":2572,"5":191}, summing to 10,183. The unit is not stated; read as decks per bracket (inference). Bracket 3 is 40% of the total.
- budget_counts: {"budget":4605,"middle":36846,"expensive":4605}, summing to 46,056, about 10/80/10 (observed; EDHREC's definition is not stated).
- tag_counts: a list of {count, slug, value}, for example {"count":3638,"slug":"infect","value":"Infect"}; read as decks with the tag (inference).
- savedate_counts: counts per calendar date over 730 dates (inference: decks saved that day).
- panels.mana_curve: the average deck's non-land cards by mana value, for example {"0":1,"1":8,"2":18,"3":16,"4":10,"5":6,"6":3,"7":1}.
- panels.articles: EDHREC articles about the commander, with date, author and excerpt.
- container.json_dict.cardlists: 11 lists tagged newcards, topcards, creatures, instants, sorceries, utilityartifacts, enchantments, planeswalkers, utilitylands, manaartifacts and lands. Each cardview has name, slug, url, synergy, lift, num_decks, potential_decks and trend_zscore. List lengths run from 5 to 50, which suggests caps (unverified).
- container.json_dict.card.num_decks: 46,056 decks run this commander.
- Average-deck JSON: deck.cards holds, by type, the [name, quantity] pairs of one 100-card average list (basics carry quantities), and eight cardlists with a label such as a count and a basic name. I did not copy the list.
- Functional tags (ramp, draw, removal, wipes) are not exposed as counts. The only lists are type-like tags (manaartifacts, utilitylands, lands). Functional counts would need our own tagging (inference).

Use: take counts by label from these files; use cardviews for inclusion (num_decks over potential_decks) and lift; do not treat an average deck as a target [S7, S9, S17].

## 7. Conflicts between sources

1. Land baseline. The 2019 average of 29 lands [S5] and the 2026 averages of 34 to 37 for Atraxa [S20] differ in year, sample and scope. They do not show a trend.
2. Ramp by strategy. The 2019 note says landfall decks run fewer rocks and more land ramp [S5]. The owner's lesson says landfall needs far more ramp. No EDHREC source gives a landfall total.
3. Early-game combos. The 2025 text bars "early game" two-card infinite combos at Bracket 3 [S11]. A 2026 author reads that as allowed after turn six [S15]. The guide does not define early game [S10]. Unresolved.
4. Turn expectations. WotC's six-turn figure for Bracket 3 [S12] versus EDHREC authors who call it optimistic [S12, S14]. A rule versus an opinion; not a factual conflict.
5. Precons and Core. The 2025 launch framed the average precon as Core [S11]. The October 2025 update removed that tie [S12, S13]. The later statement supersedes.
6. Game Changers at Bracket 3. The three-card limit comes from the 2025 launch text [S11]. A search summary attributed it to the guide; the guide does not state it [S10]. Game Changers changed in October 2025 and February 2026 [S12, S13]; the current list was not read.
7. Lift scale. The lift article says it displays log-lift (0 = independence), yet it treats 1 as independence and reports a median of 1.58 [S7]. The JSON values (Sol Ring 0.979; Sanctum Lurker 1.68) fit the ratio scale [S20]. Unresolved.
8. Synergy or lift on commander pages. The article says commander pages still used synergy in December 2025 [S7]; the JSON carries both fields [S20]. Which one a page shows is unverified.
9. Mana-curve totals. They differ from non-land totals in six of nine averages [S20]. Internal inconsistency; cause unknown.
10. Land figures across EDHREC pages: 29 (2019) [S5]; "40, give or take five" in one aside [S16], which is unsourced and seems to describe lands in general; 36 (Atraxa) [S20]; 35 (Edward Kenway ramp) [S20]. Different definitions; none is a rule.
11. Search summaries versus pages. Two claims in search summaries were not borne out by the pages read: that the TCZ 658 notes set proportions (they name categories only) [S1], and that the guide sets Bracket 3 Game Changer limits [S10]. I cite only pages I read.
12. Guide date. Page metadata says 2025-09-22; the text cites 2025-10-22 [S10]. Both are recorded.

## 8. Gaps

- The Command Zone numbers: the 2025 ratios (ramp, draw, disruption, lands, curve) are not in any text reached. Needed: the episode audio or video, a transcript, or the Patreon (not accessed). The 379 template is not located. Frank Karsten's land analysis, cited by S1, was not read.
- Measured functional averages (ramp, draw, removal, wipes per deck) by commander, strategy or bracket: none found. EDHREC gives rules of thumb only [S17].
- Averages by colour count: none retrieved.
- Averages by bracket for more than one commander: only Atraxa and one ramp theme.
- Sample sizes for average decks: not shown, except bracket_counts.
- Consistency metrics (chance of finding a piece, mulligan rates): none in the pages read. Guidance for attackers (haste, evasion, protection, defence) and for instant-heavy decks' draw: none in the pages read.
- WotC's own bracket text and the Game Changers lists of 2025 and 2026: not read; EDHREC summaries only.
- Unread EDHREC leads: "Commander Games Feel Fast These Days" (cited by S16); "Is Optimization Ruining Commander Deck Building?"; "How Modular Deckbuilding Works in Commander"; "Building a Commander Deck With Banned and Restricted Cards"; the April 2026 combo vote; the October 2025 article on brackets that "have updated"; and the updated card-type distribution article that S5's editor's note links (link not captured).
- Theme JSON pages: /pages/themes/<theme>.json is not confirmed (landfall returned 403). Tag-page JSON was not tested.
- Other sources: Archidekt, Moxfield and Reddit were not used, so EDHREC's averages are not cross-checked.
