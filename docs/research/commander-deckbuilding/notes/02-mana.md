# Mana in Commander decks: lands, colored sources, ramp, mana retention

Status: read 2026-10-31. Scope: Commander (100 cards with the commander, singleton, 40 life, pods of 3 to 4). 60-card figures are labelled as complementary evidence.

Method: 8 searches and 7 fetch attempts (15 calls). Five pages were read (S1 to S5); two failed (S6, S7). The rest are search summaries and are labelled. Numbers come from WebFetch summaries or search summaries, not copied text, so re-check any number before it drives a decision. EDHREC was not opened, quoted or cited (owner rule).

## Sources

| ID | Source | Author, date | How read | URL |
|---|---|---|---|---|
| S1 | Playgroup.gg, "How Many Lands Should a Commander Deck Run? (2026)" | Author not stated; "Updated 31 Oct 2026"; no original date | Fetched 2026-10-31 | https://playgroup.gg/commander/how-many-lands |
| S2 | ScrollVault, "Commander Land Count: 3.75M Games of Data" | Author and date not stated | Fetched 2026-10-31 | https://scrollvault.net/guides/commander-land-count-data.html |
| S3 | Playgroup.gg, "Does a Turn-1 Sol Ring Win the Game? Win Rates by Pod" | Author and date not stated; data 26 Mar to 7 Sep 2026 | Fetched 2026-10-31 | https://playgroup.gg/commander/turn-1-sol-ring |
| S4 | Draftsim, A.L. Walser, "The 54 Best Ramp Cards in Magic Ranked" | Published and updated 3 Jul 2026 (per page) | Fetched 2026-10-31 | https://draftsim.com/ramp-mtg/ |
| S5 | ScrollVault, "MTG Manabase Guide: Frank Karsten Math 2026" | Author and date not stated | Fetched 2026-10-31 | https://scrollvault.net/guides/mana-bases.html |
| S6 | TCGplayer article, title from URL slug "What's an Optimal Mana Curve and Land/Ramp Count for Commander" (linked as Karsten's by S1) | Author and date unconfirmed | FAILED: site name only, no article text (2026-10-31) | https://www.tcgplayer.com/content/article/What-s-an-Optimal-Mana-Curve-and-Land-Ramp-Count-for-Commander/e22caad1-b04b-4f8a-951b-a41e9f08da14/ |
| S7 | Scryfall JSON search for Kruphix, Upwelling, Fire Lord Azula, Everflowing Chalice, Omnath, Horizon Stone | Scryfall | FAILED: HTTP 403 (2026-10-31) | https://api.scryfall.com/cards/search |
| S8 | Scryfall, "Horizon Stone" (CMR #694); MTG Assist rulings | Ruling dated 10 Nov 2020 (per summary) | Search summary | https://scryfall.com/card/cmr/694/horizon-stone ; https://www.mtgassist.com/cards/Commander-Legends/Horizon-Stone/rulings/ |
| S9 | Q&A and wiki on Kruphix, Omnath, Upwelling, Mana Pool (TappedOut, Magic Judge Tumblr, Mana Pool wiki) | Community answers, mostly 2014 to 2018 (per summary); forum-type | Search summary only | https://tappedout.net/mtg-questions/how-will-kruphix-and-omnath-work/ ; https://www.tumblr.com/magicjudge/169784474126/if-you-have-mono-green-omnath-out-and-a-kruphix ; https://mtg-archive.fandom.com/wiki/Mana_Pool |
| S10 | Scryfall TLA #220, "Fire Lord Azula"; Draftsim EDH guide | Not read | Search summary | https://scryfall.com/card/tla/220/fire-lord-azula ; https://draftsim.com/fire-lord-azula-edh-deck/ |
| S11 | GitHub pull requests of a Claude skill repository citing Karsten's colored-source numbers | Not read; secondary | Search summary | https://github.com/reakaleek/mtg-commander-deck-builder-skills/pull/22 |
| S12 | Getwarsplay, "How Many Lands in a Commander Deck? (36-38 + Formula)" | Author and date not stated | Search summary | https://www.getwarsplay.com/blogs/news/how-many-lands-in-a-commander-deck-mtg |
| S13 | Moxgate, "How Many Lands in a Commander Deck" | Author and date not stated | Search summary | https://www.moxgate.com/guides/play-better/lands-in-commander/ |
| S14 | DeckSummon, "How Many Lands in a Commander Deck? The Complete Guide" | Author and date not stated | Search summary | https://decksummon.com/blog/how-many-lands-commander-deck |
| S15 | RateMyDecks, "How Many Lands Should a Commander Deck Play?" | Author and date not stated | Search summary | https://ratemydecks.com/en/blog/how-many-lands-commander |
| S16 | MTG Master, "How Many Lands in a Commander Deck?" | Author and date not stated | Search summary | https://mtgmaster.app/commander-guides/how-many-lands-commander-deck |

Inline [S#] links point to the URL in this table.

## 1. Land count for a 100-card Commander deck

### Takeaway
Sources agree on a band, not on one number: about 36 to 40 lands for midrange, battlecruiser or landfall decks, and 29 to 31 for cEDH speed. A Karsten-attributed formula, not verified against his article, adds about 3.1 lands per point of average mana value and removes about 0.28 land per cheap ramp or draw spell.

### Cited findings
- Karsten-attributed formula, from search summaries whose source page was not identified (the result set included [S12](https://www.getwarsplay.com/blogs/news/how-many-lands-in-a-commander-deck-mtg) and [S13](https://www.moxgate.com/guides/play-better/lands-in-commander/)): lands = 31.42 + 3.13 x average mana value of nonland cards - 0.28 per cheap ramp or draw spell, from more than 95,000 winning decks. [S2](https://scrollvault.net/guides/commander-land-count-data.html) cites 95,143 winning decklists. Unverified: the primary ([S6](https://www.tcgplayer.com/content/article/What-s-an-Optimal-Mana-Curve-and-Land-Ramp-Count-for-Commander/e22caad1-b04b-4f8a-951b-a41e9f08da14/)) failed.
- Playgroup's tracked data (173,016 opening hands): 89% of kept openers had 2 to 4 lands, averaging 2.96 lands. No formula is given ([S1](https://playgroup.gg/commander/how-many-lands)).
- Playgroup's bands: typical casual deck 38 to 42; most casual 38 to 40; high average mana value 40 to 44; low curve with card draw 36 to 38; five colors leaning on fixing 38 to 40. Its heavy-ramp and landfall figure differs between table (38 to 42) and FAQ (40 or more) ([S1](https://playgroup.gg/commander/how-many-lands)).
- ScrollVault simulation: 3.75 million modelled games; metric is the share of games where a spell is castable on its matching turn. Not modelled: fetch lands, mulligan choices, draw effects and tutors, opposing interaction ([S2](https://scrollvault.net/guides/commander-land-count-data.html)). Recommended counts: cEDH turbo (MV 1.8, 12 fast mana) 29 to 31; combo (MV 2.5, 10 rocks) 33 to 35; midrange (MV 3.0, 10 mixed ramp) 36 to 37; battlecruiser (MV 3.5, 8 rocks and ramp) 38 to 40; landfall (MV 3.0, 6 land-ramp pieces) 38 to 40.
- Same simulation, midrange with four rocks, 29 vs 37 lands: three-drop on turn 3 95.2% vs 97.2%; five-drop on turn 5 88.4% vs 95.6%; six-drop on turn 6 75.1% vs 90.3% ([S2](https://scrollvault.net/guides/commander-land-count-data.html)).
- Search summaries: Getwarsplay 36 to 38 baseline, 38 to 40 for six-plus-mana or landfall decks ([S12](https://www.getwarsplay.com/blogs/news/how-many-lands-in-a-commander-deck-mtg)); DeckSummon 37 ([S14](https://decksummon.com/blog/how-many-lands-commander-deck)); RateMyDecks adds 2 to 4 lands at 0 to 5 ramp pieces and subtracts 2 at 11 to 15 ([S15](https://ratemydecks.com/en/blog/how-many-lands-commander)); MTG Master allows a ramp-based cut of one or two lands ([S16](https://mtgmaster.app/commander-guides/how-many-lands-commander-deck)).
- Draftsim advises newcomers to include roughly ten ramp cards, depending on curve and speed. It gives no land count ([S4](https://draftsim.com/ramp-mtg/)).

### Inferences
- The formula as reported, computed here (check the arithmetic): cEDH (MV 1.8, ramp 12) 33.7; combo (2.5, 10) 36.4; midrange (3.0, 10) 38.0; battlecruiser (3.5, 8) 40.1; landfall (3.0, 6) 39.1. Sources count ramp differently, so this is not a like-for-like check.
- Under this formula one ramp piece replaces about 0.28 of a land. The one-for-one rule some builders use is not in any source read here.
- S2's text says its formula gives 38 for midrange and "matches" its results, but its table says 36 to 37. Use 36 to 38 until the primary is read.
- Playgroup's "peak at about 42" is a property of the opening-hand window: 7 x L / 99 is about 3 at L = 42, which maximises the chance of a 2 to 4 land opener. It is not a consistency target.
- S2 has no opposing interaction and no pod size. Neither source measures consistency in a 3 to 4 player pod.
- Owner signal (not sourced): S2's landfall preset uses 38 to 40 lands with six land-ramp pieces, fewer ramp pieces than its midrange preset, and does not model landfall triggers. It neither confirms nor refutes the owner's lesson.

### Gaps
- Karsten's article could not be read: formula coefficients, the 2022 date and the 95,143 count are unverified.
- No land counts by color count beyond Playgroup's band; no landfall count beyond S2's preset.

## 2. Colored sources, tapped lands, utility and colorless lands

### Takeaway
One ScrollVault page ([S5](https://scrollvault.net/guides/mana-bases.html)) gives every colored-source target found, crediting Karsten without a link. Its 60-card entries reproduce a 90% target on the draw. Its 99-card entries do not, at the turns it gives. No targets exist for four or five colors, and no source prices tapped or colorless lands in Commander.

### Cited findings
- 99-card targets ([S5](https://scrollvault.net/guides/mana-bases.html)): single pip on turn 1, 19 sources (untapped status not stated); double pip on turn 2, 30 sources.
- 60-card targets ([S5](https://scrollvault.net/guides/mana-bases.html)): single pip on turn 1, 14 untapped; single pip on turn 2 on the draw, 13; double pip on turn 2, 21; triple pip on turn 3, 23.
- Karsten's 60-card consistency rule, as S5 summarises it: about 89 plus mana value in percent (90% at MV 1, 96% at MV 7). S5 says not to scale it to Commander. One sentence credits Karsten's hypergeometric research: "The numbers here come from Frank Karsten's hypergeometric probability research." No link is given.
- A search summary cites 26 sources for a 99-card double pip by turn 4 ([S11](https://github.com/reakaleek/mtg-commander-deck-builder-skills/pull/22)). S5 does not list it.
- S5 worked example, not advice: 12 duals plus 6 Plains and 6 Swamps in a 24-land build gives 18 sources of each color ([S5](https://scrollvault.net/guides/mana-bases.html)).
- Tapped lands ([S5](https://scrollvault.net/guides/mana-bases.html)): a tapped land costs one mana on the turn it enters. Tolerances: 0 to 2 in competitive 60-card decks; 4 to 6 in Commander (uncited). Each needs a payoff such as scry or a third color. Untapped sources early, tapped sources later.
- Other lands ([S5](https://scrollvault.net/guides/mana-bases.html)): shock lands cost 2 life or enter tapped; fast lands stay untapped with two or fewer other lands; pain lands cost 1 life per colored tap; fetch lands are the strongest fixers.
- Utility lands ([S5](https://scrollvault.net/guides/mana-bases.html)): Castle Locthwain, Mutavault and Field of Ruin make one color or none, give no colored-source credit, and go in last. S5 calls Command Tower both a utility land and a universal fixer.
- Colorless lands: Field of Ruin and Mutavault add no colored sources; no colorless weight is stated ([S5](https://scrollvault.net/guides/mana-bases.html)).
- The Commander FAQ that S5 cites counts rocks and dorks as colored sources and recommends at least ten rocks ([S5](https://scrollvault.net/guides/mana-bases.html)).
- S5 credits Karsten with modal double-faced land weights (about 0.74 untapped, 0.38 tapped). The project rule "No reversible cards" (CLAUDE.md) excludes modal DFCs, so these do not apply.

### Inferences
- Reproduction check, computed here, not from a source. Assumptions: singleton 99 (or 60) cards, no mulligan, no fetch or ramp, untapped sources, hypergeometric. Cards seen by turn T: 6 + T on the play, 7 + T on the draw. Single pip needs one source; double pip needs two.

| Deck | Target | Sources | Turn, play or draw | Chance |
|---|---|---|---|---|
| 60 | single pip (S5) | 14 | 1, draw | 89.8% (play 86.1%) |
| 60 | single pip (S5) | 13 | 2, draw | 90.8% |
| 60 | double pip (S5) | 21 | 2, draw | 89.8% |
| 99 | single pip (S5) | 19 | 1, draw | 83.1% (play 78.7%) |
| 99 | single pip | 24 | 1, draw | 90.1% |
| 99 | single pip | 19 | 3, draw | 89.4% |
| 99 | double pip (S5) | 30 | 2, draw | 82.2% (play 76.2%) |
| 99 | double pip | 36 | 2, draw | 90.6% |
| 99 | double pip | 30 | 4, draw | 90.5% |
| 99 | double pip (S11) | 26 | 4, draw | 84.4% |

- The 60-card entries reproduce 90% on the draw, and S5 states that assumption for its 13-source entry. The 99-card 19 and 30 fall short of 90% on their stated turns under the same assumptions. They reach 90% only at turn 3 (19) or turn 4 (30), or under a lower target or a mulligan rule. No source says which. Both stay unverified.
- For 90% on turn 1 on the draw, a 99-card deck needs about 24 sources of one color under these assumptions, not 19.
- The same method answers four- and five-color questions. No source gives targets for them.
- Tapped-land cost in Commander: the qualitative cost is sourced; the 4 to 6 tolerance is not. A quantified cost needs a model with tapped-land logic, which S2 lacks.

### Gaps
- Four- and five-color targets; colorless-land cost; quantified tapped-land cost; Karsten's consistency target and mulligan assumptions (the primary failed).
- A search summary gave partial weights (0.75 per color for Arcane Signet on spells costing three or more; 0.5 per color for Llanowar Elves on two or more). The page was not identified, so these are not used.

## 3. Ramp: types, counts by strategy, rocks, early and late

### Takeaway
Ramp comes in eleven forms ([S4](https://draftsim.com/ramp-mtg/)). About ten pieces is the generic count ([S4](https://draftsim.com/ramp-mtg/)); S2's midrange and combo presets use ten, and its landfall preset uses six land-ramp pieces. Sol Ring is the only card that the Playgroup page reports as surviving correction in a 143-card screen, and its edge is smaller in four-player games ([S3](https://playgroup.gg/commander/turn-1-sol-ring)). Editorial rankings put Arcane Signet high ([S4](https://draftsim.com/ramp-mtg/)), but its measured effect does not survive correction ([S3](https://playgroup.gg/commander/turn-1-sol-ring)). No source ranks Everflowing Chalice.

### Cited findings
- Forms ([S4](https://draftsim.com/ramp-mtg/)): land ramp (Cultivate, Rampant Growth); mana creatures (Llanowar Elves, Bugenhagen); rocks (Mind Stone, Basalt Monolith); treasure makers; extra land drops (Exploration); land recursion (Crucible of Worlds); one-shot bursts (Dark Ritual); cost reducers (Honest Rutstein); Eldrazi token makers; mana doublers (Mirari's Wake); temporary mana (firebending, no card named).
- Rock ranks ([S4](https://draftsim.com/ramp-mtg/), editorial, July 2026): Sol Ring #1, the most-played Commander card; Arcane Signet #27, the "premier" two-mana artifact, weaker in two-color decks and valued in three-plus-color decks for cheap fixing; Signets grouped with Talismans at #28, Talismans stronger; Mind Stone #44, valued late because it can become cards. Everflowing Chalice: not stated.
- Sol Ring on turn 1 ([S3](https://playgroup.gg/commander/turn-1-sol-ring); Playgroup Live; base dataset 27,329 games; data 26 Mar to 7 Sep 2026): turn-1 casters' win rate vs others: 2 players 62.2% vs 49.5% (+12.7 points); 3 players 41.1% vs 33.2% (+7.9); 4 players 28.7% vs 25.0% (+3.7; 95% CI +1.5 to +6.0).
- Randomised check, opening seven with vs without Sol Ring: +11.2, +7.1 and +2.2 points for 2, 3 and 4 players (4-player CI -0.1 to +4.7); pooled +7.0 (CI +5.6 to +8.5). Shuffle check passed (p = 0.92) ([S3](https://playgroup.gg/commander/turn-1-sol-ring)).
- Control screen of 143 cards, each in at least 6,000 decks: average effect -0.04 points; only Sol Ring survives correction. Command Tower (q = 0.99), Rhystic Study (q = 0.99) and Mind Stone (q = 0.78) do not. Arcane Signet: randomised +2.56 points (CI +1.0 to +4.1), q = 0.058 ([S3](https://playgroup.gg/commander/turn-1-sol-ring)).
- Early versus late ([S4](https://draftsim.com/ramp-mtg/)): Llanowar Elves and Birds are strong turn-one plays, Birds also fixing. Burgeoning is strong from an opener but weak to a late draw. Utopia Sprawl needs many Forests. Rampant Growth remains viable.
- Ramp that does more ([S4](https://draftsim.com/ramp-mtg/)): Worldsoul's Rage (removal, then a late mana outlet); Sakura-Tribe Elder (blocker, sacrificed later); Malevolent Rumble (graveyard stocking plus an early four-drop); Icetill Explorer (land recursion, extra land drops, self-mill); Relic of Sauron (needs a Grixis commander); Sowing Mycospawn (ramp and land destruction).
- Archetype counts in S2 (Section 1): cEDH 12 fast mana; combo 10 rocks; midrange 10 mixed; battlecruiser 8; landfall 6 land-ramp. S5 reports the Commander FAQ's "10 or more rocks" ([S5](https://scrollvault.net/guides/mana-bases.html)).

### Inferences
- Pod size changes the value of a turn-one Sol Ring. Its edge shrinks from +12.7 points in duels to +3.7 in four-player games, and the four-player randomised check is not significant ([S3](https://playgroup.gg/commander/turn-1-sol-ring)). Duel numbers overstate the benefit in 3 to 4 player pods (inference).
- Editorial rank and measured effect disagree on Arcane Signet ([S4](https://draftsim.com/ramp-mtg/) vs [S3](https://playgroup.gg/commander/turn-1-sol-ring)). Do not read ranks as measured power.
- S2 is the only source with ramp counts by strategy. Its landfall preset has fewer ramp pieces than its midrange preset and still recommends 38 to 40 lands. It counts only land ramp and does not model landfall triggers.
- Owner signal (not sourced): a Chalice that entered with two counters and was cast on turn 5 lost the turn. Its output depends on the counters it enters with (card text not read here). No source ranks or times Chalice, so the lesson stays unverified.

### Gaps
- Chalice ranking and its proliferate versus aggro use; ramp counts by strategy from a primary source; the cost of late ramp beyond Burgeoning.
- Command Beacon's rock list, Card Kingdom, MTGGoldfish, Star City Games and Commander's Herald: not read.

## 4. Mana retention and temporary mana

### Takeaway
Unspent mana drains at the end of each step and phase (baseline in summaries of [S8](https://scryfall.com/card/cmr/694/horizon-stone) and [S9](https://tappedout.net/mtg-questions/how-will-kruphix-and-omnath-work/); not checked against the Comprehensive Rules). Horizon Stone and Kruphix turn drained mana colorless; Omnath keeps green; Upwelling keeps all mana. Fire Lord Azula's firebending mana lasts through combat and is gone at the postcombat main phase, per a summary that matches the owner's description ([S10](https://scryfall.com/card/tla/220/fire-lord-azula)). Scryfall returned 403, so all card text here is summary-level.

### Cited findings
- Horizon Stone (Commander Legends, five-mana artifact per summary; [S8](https://scryfall.com/card/cmr/694/horizon-stone)): under a 10 Nov 2020 ruling, unspent mana that would drain stays and becomes colorless, so it pays generic costs only. Spending limits still apply. If the Stone leaves play, held mana lasts only through the current step or phase.
- Kruphix (assumed to be Kruphix, God of Horizons): a replacement effect that makes draining mana colorless ([S9](https://tappedout.net/mtg-questions/how-will-kruphix-and-omnath-work/) summary; unverified).
- Upwelling: stops pools draining at step and phase boundaries for every player; the wording may have changed ([S9](https://mtg-archive.fandom.com/wiki/Mana_Pool) summary; unverified).
- Omnath, Locus of Mana: green mana does not drain, and Omnath gets +1/+1 per green mana in the pool. The summary says its text came from a listing ([S9](https://tappedout.net/mtg-questions/how-will-kruphix-and-omnath-work/) summary).
- Kruphix with Omnath: a judge answer from 2014 to 2018 treats Omnath's retention as a static rule change, outside Kruphix's replacement ([S9](https://www.tumblr.com/magicjudge/169784474126/if-you-have-mono-green-omnath-out-and-a-kruphix) summary; unverified).
- Fire Lord Azula ([S10](https://scryfall.com/card/tla/220/fire-lord-azula) summary): firebending 2 adds two red mana per attack; the mana does not drain through combat, and the summary says it expires when the postcombat main phase begins. The official rulings were not read.
- Draftsim lists temporary mana as a ramp form, naming no card ([S4](https://draftsim.com/ramp-mtg/)).

### Inferences
- The retention effects keep different things. Colorless conversion keeps quantity but not color, so it pays generic costs only. Upwelling keeps color. Omnath keeps green only.
- For Azula, the summary implies firebending mana is spendable during combat only. A deck that wants it in its second main phase needs a retention effect. Confirm on the ruling.
- Owner signal (not sourced): the Horizon Stone lesson fits this profile, since retention helps only when the deck produces mana it cannot spend. No source measures how often that happens.
- "Locus of Mana" matched only Omnath, Locus of Mana in this pass.

### Gaps
- Card text for Kruphix, Upwelling, Omnath and Azula (the Scryfall search failed); the firebending rulings; how decks sequence temporary mana; any data on the value of retention cards.

## 5. Mana sinks, flood and screw insurance, curve on turns 1 to 4

### Takeaway
Not covered. No page read deals with mana sinks, flood or screw insurance, or a turn 1 to 4 curve. Related points: turn-one accelerants ([S4](https://draftsim.com/ramp-mtg/)), early tapped lands in 60-card decks ([S5](https://scrollvault.net/guides/mana-bases.html)) and Playgroup's calculator outputs ([S1](https://playgroup.gg/commander/how-many-lands)).

### Cited findings
- A turn-one Elf or Bird is a strong play; the author suggests loading up on one-drop accelerants alongside strong three-drops ([S4](https://draftsim.com/ramp-mtg/)).
- Three or more early tapped lands in an aggressive 60-card build are called fatal against fast decks ([S5](https://scrollvault.net/guides/mana-bases.html)).
- Playgroup's calculator outputs, not advice: keepable openers (2 to 4 lands) and flood risk (5 or more lands) ([S1](https://playgroup.gg/commander/how-many-lands)).

### Inferences
- S2 shows what extra lands buy: with four rocks, a six-drop on turn 6 is castable 75% of the time at 29 lands and 90% at 37. That is top-end castability, not flood insurance (inference).

### Gaps
- Mana sinks, flood and screw insurance, and the turn 1 to 4 curve: no source read. Suggested next pass: one source on sinks and flood insurance (Draftsim or Commander's Herald) and one on curve.

## Conflicts between sources

1. Midrange land count: S1 gives 38 to 40 for typical casual decks; S2's table gives 36 to 37 while its text says the formula gives 38; search summaries give 36 to 38 (S12) and 37 (S14). Unresolved.
2. Karsten's study: S13 says 41 lands; S1 says 42. The primary (S6) could not be read. Unresolved.
3. Ramp versus land count: the formula's 0.28 land per piece against the one-for-one rule, which is not in any source read. Unresolved.
4. 99-card colored targets: S5 gives 19 (turn 1) and 30 (turn 2); S11 adds 26 (turn 4). None reaches 90% at the stated turn under plain draws (Section 2 table). The turn labels may be off. Unresolved.
5. Arcane Signet: S4 ranks it top-tier; S3 finds +2.56 points with a CI above zero that does not survive correction (q = 0.058). Opinion against measurement; not resolvable here.
6. Sol Ring in four-player games: S3's turn-1 comparison has a CI above zero (+1.5 to +6.0); its randomised check has a CI spanning zero (-0.1 to +4.7). Same data, different checks.
7. Heavy ramp and landfall in S1: table 38 to 42; FAQ 40 or more.
8. Command Tower: utility land and universal fixer in the same source (S5).
9. Firebending timing: the owner says the mana empties at end of combat; the S10 summary says it lasts until the postcombat main phase begins. Same window; the ruling was not read.
10. A second formula (19.59 + 1.90 x MV) appears in one search summary and seems to be the 60-card version. Not used.

## Gaps

- Failed reads: the Karsten article (S6) returned no text; the Scryfall search (S7) returned 403. Card texts for Kruphix, Upwelling, Omnath, Azula and Horizon Stone are summary-level.
- Missing topics: four- and five-color targets; colorless-land cost; quantified tapped-land cost; Everflowing Chalice; mana sinks; flood and screw insurance; the turn 1 to 4 curve; ramp counts by strategy from a primary source; the value of retention cards.
- Not read: Card Kingdom, MTGGoldfish, Star City Games, Commander's Herald, Wizards of the Coast articles, ChannelFireball, other TCGplayer articles, Command Beacon.
- EDHREC: a search result on mana rocks came from edhrec.com. It was not opened, quoted or used, per the owner's rule. S2 says part of its inputs come from EDHREC data, so its outputs may carry that data.
- Owner lessons: the Chalice lesson has no source; the Horizon Stone lesson has card-text summaries but no frequency data; the landfall lesson is neither confirmed nor refuted by S2.
- Next pass (about 8 calls): Karsten's article by another route; the Comprehensive Rules on mana pools; Oracle text for the retention cards; Command Beacon's rock list; sources on sinks, flood insurance and curve.
