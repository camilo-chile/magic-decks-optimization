# Card evaluation, playtesting, iteration and prior-art tools for Commander decks

Research note 08 of `docs/research/commander-deckbuilding/`. All sources read 2026-10-31 (the publication date is given where the page shows one). Status: partial.

## Status and method

- Scope: Commander, casual pods, Bracket 3 context. cEDH material is labelled [cEDH]. Other formats are not used.
- Sources: 27 web sources (S1 to S27): 7 fetched, 2 blocked or unreadable, 18 from search-result summaries only. One local project record (P1), read by grep.
- Caveat: fetched pages and search results reach this note as summaries written by a model, not verbatim text. Quotes and numbers need a check against the page before an AI builder relies on them.
- Owner rules applied: EDHREC, Archidekt and Moxfield were not opened or queried. Several EDHREC URLs appeared in search results; none was opened or used. Reddit and forums are not cited. At most one quote per source, under 15 words.
- Tool budget: 20 web calls, above the skill guideline of about 15. The extra calls went to licence checks and two playtest sources.

Read codes: F = fetched (WebFetch summary); S = search-result summary only, page not opened; X = blocked or unreadable.

## Sources

| ID | Source | Author | Date | Read | URL |
|---|---|---|---|---|---|
| S1 | Commander mulligan rules (Draftsim) | Herko Kerghans | 2026-03-09 | F | https://draftsim.com/mtg-commander-mulligan-rules/ |
| S2 | "Stop Evaluating Cards in a Vacuum" (Commander's Herald) | Kristen Emily | 2021-06-23 | F | https://commandersherald.com/stop-evaluating-cards-in-a-vacuum/ |
| S3 | "How many lands in a Commander deck" (CoolStuffInc) | Cas Hinds | 2026-04-27 | F | https://www.coolstuffinc.com/a/how-many-lands-in-a-commander-deck-04272026 |
| S4 | Commander mana bases column (CoolStuffInc) | Mark Wischkaemper | 2022-07-26 | S | https://coolstuffinc.com/a/markwischkaemper-07262022-commander-mana-bases-how-many-lands-should-you-run |
| S5 | Karsten land-drop article, third-party PDF copy | Frank Karsten | 2017-05 (from URL path, unconfirmed) | X (PDF text not decodable; summary only) | https://www.orkerhulen.dk/onewebmedia/How%20Many%20Lands%20Do%20You%20Need%20to%20Consistently%20Hit%20Your%20Land%20Drops.pdf |
| S6 | 40-card deck number of lands (Draftsim) | not read | last updated 2024-06-25 | S | https://draftsim.com/mtg-40-card-deck-number-of-lands/ |
| S7 | Mulligan (mtg.wiki) | wiki, no byline | not shown | S | https://mtg.wiki/page/Mulligan |
| S8 | Can 1v1 Commander testing be worth it (Card Kingdom blog) | not read | not shown | X (HTTP 403); summary only | https://blog.cardkingdom.com/can-1v1-commander-testing-be-worth-it/ |
| S9 | Quit Playing With Yourself (TopDeck newsletter) | Talion (per summary) | not shown | S | https://newsletter.topdeck.gg/p/quit-playing-with-yourself |
| S10 | Anatomy of a playtest game (EDHLab blog) | not read | not shown | S | https://blog.edhlab.gg/anatomy-of-a-playtest-game |
| S11 | "What we learned after 50 games of Commander" (MTGGoldfish) | not read | not shown | S (used only as a warning) | https://www.mtggoldfish.com/articles/what-we-learned-after-50-games-of-commander-commander-clash-s16-stats |
| S12 | The Rise of Compact Combos (Nerd Leagues) | Time (byline only) | 2026-06-22 | F | https://www.nerdleagues.com/blog/the-rise-of-compact-combos |
| S13 | cEDH combo guide series (Nerd Leagues) | not read | series; entries dated 2026-06-22 and 2026-07-01 per summary | S | https://www.nerdleagues.com/blog/series/cedh-combo-guide |
| S14 | Mechanical Engineering: Always Cut From The Top (Commander's Herald; title presumed, the summary does not name it) | not shown | 2022-02 per summary | S | https://commandersherald.com/mechanical-engineering-always-cut-from-the-top/ |
| S15 | Dead Cards (Casual Planeswalker wiki) | not shown | not shown | S | https://casualplaneswalker.com/wiki/dead-cards/ |
| S16 | Pet cards and cut order (Card Kingdom blog, post 30299) | not shown | not shown | S | https://blog.cardkingdom.com/?p=30299 |
| S17 | Finding Synergy in Commander (Medium) | Medium handle gorostiagamanuel | not shown | S | https://medium.com/@gorostiagamanuel/building-for-synergy-7589a6fa5f2f |
| S18 | Forge repository page | Card Forge project | latest commit not shown | F | https://github.com/Card-Forge/forge |
| S19 | XMage repository page | XMage project | latest commit not shown | F | https://github.com/magefree/mage |
| S20 | Commander Spellbook backend repository page | Space Cow Media | latest commit not shown | F | https://github.com/SpaceCowMedia/commander-spellbook-backend |
| S21 | MTG MCP server listings (as3k, bmurdock, dccoder, ericraio, artillect, cryppadotta, others) | individual maintainers | not shown | S | https://glama.ai/mcp/servers/as3k/scryfall-mcp ; https://lobehub.com/en/mcp/bmurdock-scryfall-mcp ; https://hub.docker.com/r/dccoder/mtg-mcp ; https://mcpservers.org/servers/ericraio/mtg-mcp ; https://glama.ai/mcp/servers/@artillect/mtg-mcp-servers |
| S22 | GitHub MTG deck-builder repositories (s-bridges, cschladetsch, texodus, EskoSalaka, svarozhych, IristormDesign) | repository owners | last push 2022 (cschladetsch) and 2024 (svarozhych) per listings; others not shown | S | https://www.github.com/s-bridges/MTG_Deck_Builder ; https://awesome.ecosyste.ms/projects/github.com%2Fcschladetsch%2Fmtg-library ; https://github.com/texodus/mtg-perspective ; https://www.github.com/EskoSalaka/mtg-deckbuilder ; https://awesome.ecosyste.ms/projects/github.com%2Fsvarozhych%2Fcard-deck-mtg ; https://github.com/IristormDesign/mtg-deck-builder |
| S23 | EDH power calculator (digitalkw) | not shown | not shown | S | https://digitalkw.com/en/edh-power-calculator/ |
| S24 | "How the Salt Score Works" (Scrollvault; not Commander Salt) | not shown | not shown | S (title only, page not opened) | https://scrollvault.net/methodology/salt-score.html |
| S25 | Mana Base Calculator (Scrollvault) | not shown | not shown | S (self-reported claims) | https://scrollvault.net/tools/manabase/ |
| S26 | Fundamentals tag page (Modern Nexus) | not shown | not shown | S (weak source) | https://modernnexus.com/tag/fundamentals/ |
| S27 | Playgroup research page | not shown | not shown | S | https://playgroup.gg/research |
| P1 | Prior-art audit, project record (grep only) | project | 2026-10-13 | local | docs/research/audit-prior-art-2026-10-13.md |

Not used (listed only):
- EDHREC pages in results (mulligan guide, synergy FAQ, playtesting, cEDH, interaction guides). Not opened. The only EDHREC figure mentioned is an attribution inside S3, reported as an attribution and not checked.
- Archidekt and Moxfield: not touched. P1 line 8 records the same exclusion.
- Forums (TappedOut, MTGNexus, MTGSalvation, deckstats) and Reddit (r/EDH, r/lrcast, r/CompetitiveEDH): appeared in results, not cited.
- StarCityGames "Let's Talk Mulligans" and the Commander Rules Committee site (mtgcommander.net): appeared in results, not opened.

## 1. Card evaluation for a specific deck

### Takeaway
The one read source that addresses this question (S2, 2021) judges a card by its job inside one list: fit, role, replacement options and mana, then playtest. No source read quantifies stand-alone value against synergy breadth, scaling with pod size, the last ten slots, or high floor against high ceiling.

### Cited findings
- The Commander's Herald article says to judge a card by its fit in the specific deck, not by raw power or popularity alone. It advises sketching how each card interacts with the list, testing swaps, and closes with one line: "Get out there, play the deck, and take notes." [S2]
- Criteria it uses: synergy (the main test: a recursion-and-payoffs card valued through its deck); role (a creature rejected because it conflicts with the deck's reanimation plan); replacement candidates (each card compared with named alternatives); mana (a four-drop judged to undercut stronger ramp and to suit high-curve decks poorly); scaling (indirect only: card advantage is better in longer games); stand-alone value (conceded as real, but not decisive). [S2]
- The same article recommends EDHREC filters as a tool. Those parts are not used here. [S2]
- Cutting favourites is hard. Weigh each card against the deck's main goal; when unsure, playtest the extra cards and cut what performs. Sanctioned Commander decks are exactly 100 cards, so an oversized list is only a test tool. [S14, summary]
- Dead cards: a deck with six or seven spells costing 7 or more mana can leave many stuck in hand, since few are cast in a game. [S14, summary]
- Multiplayer setup, longer games and the singleton rule create dead-card problems. A card can alternate between dead and live over an extended game. [S15, summary]
- Pet cards: one blog argues that a few pet cards keep a list from feeling predictable. Its cut order (list every candidate, trim the most-played or strongest staples first to make room for underplayed picks) is ambiguous in the summary. [S16, summary]
- Synergy hunting: scan every part of a card (rules text, mana cost, types, stats) for hooks that other cards reference; implicit synergy means cards that work with a commander without sharing its wording. [S17, summary; personal Medium post, low authority]
- Land count, a mana-efficiency input: a 2026 column gives a 43-land baseline for Commander, adapted by Rebell Lily from Frank Karsten's 60-card math. Lily's range is 36 to 46, and she counts about 40 when land-cycling, modal and MDFC lands are included. The author's own usual count is about 37. For efficient cEDH builds he gives 26 to 30, citing one cEDH TV example of about 26 to 27 whose method is not described. [S3]
- The same column says current Commander decks run fewer lands, citing an average of about 36 (range 33 to 38) attributed to EDHREC. Not checked, not used. [S3]
- A 2022 column (summary only) equates 24 lands in a 60-card deck with 40 in Commander, and reports 99.8 % for the first two land drops and 63.8 % for the fifth. Unverified. [S4]

### Inferences
- The sources read agree on the method: value is set inside the list (role, replacement, playtest), not by a power or popularity score. That is the same direction as the owner's consistency rule. This reading is mine, not a source's claim.
- The 2026 land column mixes a cEDH anecdote, an EDHREC-attributed average and unsourced opinion. Treat it as a secondary summary, not a measurement.
- The owner's two heavy losses with Ezio (project context, not external evidence) match the dead-card pattern in S14 and S15. They are not used as evidence here.

## 2. Playtesting

### Takeaway
Sources agree on three points: solo goldfishing answers narrow questions, loose goldfishing misleads, and the step from solo tests to multiplayer games is unmeasured. No source found gives a number of test games that yields a useful signal in Commander.

### Cited findings
- London mulligan procedure (S1): each player draws seven and keeps or mulligans in turn order. A mulliganing player shuffles the hand back and draws a new hand of the same size, repeated until everyone keeps. Each counted mulligan puts one card on the bottom of the library. In pods of three or more the first mulligan is exempt from the bottom step; after three mulligans a pod player bottoms two, a 1v1 player three. The article reports pod mulligans as capped at eight. [S1]
- Official status: S1 says not stated and gives no Comprehensive Rules number. [S1]
- 1v1: the first mulligan counts, and the first player skips the first draw. Duel Commander's first mulligan is not free. Brawl, a 1v1 format, gives a free first mulligan, which the article itself calls inconsistent. [S1]
- mtg.wiki (summary only) reports that the Commander Rules Committee's informal guidance backs free mulligans even in two-player games, and suggests setting rejected hands apart instead of reshuffling them. This conflicts with S1 on Duel Commander. [S7, summary]
- Search summaries cite the multiplayer exemption as CR 103.4c (via an EDHREC article, excluded) and as CR 103.5e (origin unclear). Neither was read in primary text. [S7, summary; search results]
- Volume: one author reports roughly 50 logged full playtest games. That is one person's tally, not a benchmark. [S10, summary]
- Solo goldfishing: acceptable for narrow questions such as turn-two consistency. Loose goldfishing lets a shaky opener slip through, makes misses easy to forget, and keeps the wins in memory. [S9, summary; author Talion per summary]
- Sequence: test solo until the deck works and the pilot is competent, then play other people. [S26, summary; tag page, weak]
- 1v1 games accumulate results quickly, according to the Card Kingdom search summary. The page returned HTTP 403 when opened, so this rests on the summary alone. [S8]
- Lands by turn N: the only numeric framework found is Karsten-style land-drop math for 60-card decks. The 2017 PDF copy (S5) could not be read. A search summary of it reports 26 lands on the play for targets of 90 % on land three and 75 % on land four. Unverified. [S5, summary]
- A calculator site says its hypergeometric math follows Karsten, and that its Commander simulations cover 3.75 million games. Self-reported, not checked. [S25, summary]
- A Draftsim guide credits Karsten with 19 lands for over 80 % odds of a fifth land drop on time, in 40-card decks. Not Commander; unverified. [S6, summary]
- An MTGGoldfish article titled "50 games" covers season statistics, not playtesting. [S11, summary]
- Mulligan variant: S7 (summary) describes setting rejected hands apart instead of reshuffling them, which changes the opening-hand distribution. Not verified against a rules text. [S7, summary]

### Inferences
- Lands by turn N can be computed without playing. For a fixed 100-card list and a stated mulligan rule, a script can count the hypergeometric outcomes. Under the project policy that is deterministic work for a script. The sources do not define "engine online by turn N"; the project must define it itself.
- With 10 games, 5 wins gives a 95 % Wilson interval of about 24 % to 76 % (own calculation, not sourced). Ten games cannot rank two close lists. Game logs (what the card did, and when) carry more signal than the win rate.
- The free pod mulligan changes opening hands in multiplayer. Playtest logs should record the mulligan rule used, and pod results should be kept apart from 1v1 results.

## 3. Iterating from real games

### Takeaway
Thin sourcing. The sources read advise: play the deck, take notes, test swaps, and playtest extra cards before cutting. No source found covers postmortem templates, how many games are needed before a card judgment, or how to separate a bad card from a bad draw.

### Cited findings
- "Get out there, play the deck, and take notes." [S2]
- Playtest the extra cards and cut based on what performs. [S14, summary]
- Test changes in real games, and judge each card by whether it advances the deck's plan. Stated as a common thread of several search summaries. [S14, S16, summary]
- Sanctioned decks are exactly 100 cards, so a larger test list is for testing only. [S14, summary]

### Inferences
- The loop the sources support is: play, log, change one card, retest. For each weak card a log should record whether it was drawn, whether it could be cast by the turn it mattered, and whether it did anything. That separates a bad card from a bad draw. This is my inference; no source gives this method.
- After a few games, decide on mechanism (did the card act when drawn), not on the game result.

## 4. cEDH lessons (labelled cEDH)

### Takeaway
One fetched cEDH source (Nerd Leagues, 2026-06-22) argues that cEDH is decided by compact, resilient combo lines with tutor reach and cheap mana. Its general principles transfer more easily than its cEDH-only claims. Its mana totals look inconsistent with printed costs (unverified).

### Cited findings
- [cEDH] A small set of combo packages ends most cEDH games. The article attributes this to compactness: few cards, little mana, and fewer chances for opponents to interact. [S12]
- [General, per article] Compact packages need little support, are easy to find with tutors, fit the deck's plan and assemble quickly. [S12]
- [General, per article; no data given] A two-card line assembles more often than a four-card line and needs fewer tutors and slots. [S12]
- [General, per article] Resilience: redundancy, tutor access, protection, graveyard recovery, and pieces that keep value apart from the combo. The article's thesis: "Speed matters, but resilience wins." [S12]
- [General, per article] Several tutor types reaching the same piece add consistency. Count cards that act as extra copies of a piece. [S12]
- [cEDH] Disruption is always present: removal, counters, stax and anti-combo cards. [S12]
- [General, unsourced in article] A 3-to-4 mana combo beats an 8-to-10 mana one that reaches the same outcome. [S12]
- Conflict: the article gives 3 mana for its two-card line and 9 mana for its four-card line. From printed costs as I recall them, the two-card line is 4 mana (two cards at 2 each) and the four-card line is about 10. Unverified; check on Scryfall before reuse. [S12; own recall]
- A cEDH combo guide series exists (summary only). Not read. [S13, summary]

### Inferences
- Most likely to transfer to Bracket 3 pods: redundancy and tutor reach for the few functions a plan needs. That matches the owner's consistency gate, which asks for enough pieces per function. Least likely to transfer: cEDH speed, and always-present counters and stax in a pod with mixed decks. No source tests either transfer; this is inference.

## 5. Prior-art tools that build or evaluate Commander decks

### Takeaway
Few tools here judge deck quality. Most are deck managers, lookup servers, rules engines or calculators whose methods were not read. Commander Spellbook (MIT backend, combo data) and XMage (MIT, multiplayer AI) are the most concrete candidates. Forge is GPL-3.0. No external Commander Salt page surfaced, so its method is unverified here.

### Tools

| Tool | What it encodes | Licence | Activity | Reuse note | Read |
|---|---|---|---|---|---|
| Commander Spellbook backend | Combo database, wiki and engine; REST API; TS/JS client on npm | MIT on repo page; LICENSE text not read; data terms not stated | 3,574 commits; no release or date shown | The project already uses Spellbook bulk data locally (P1). Check data terms before redistribution. | F (S20) |
| XMage | Rules engine: two-player and multiplayer games including Commander (up to 10 players); AI players for games and deck building | MIT on repo page; LICENSE text not read | 2.4k stars, 976 forks; no commit date shown | Possible AI-played test sandbox; multiplayer AI quality not measured here | F (S19) |
| Forge | Unofficial rules engine with AI opponents; Commander listed as an AI format; multiplayer support not stated | GPL-3.0 | 2.9k stars, 1.2k forks; no commit date shown | Copyleft: using its code would bind the project to GPL-3.0. Use as a separate tool was not analysed. | F (S18) |
| MTG MCP servers (as3k, bmurdock, dccoder, ericraio, artillect, cryppadotta, others) | Scryfall lookups; deck managers (drawing, mulligans, sideboards); one listing claims deck analysis, brackets and combo detection | not checked | not checked | Listings only; none described as encoding Commander evaluation. Check each repo. | S (S21) |
| GitHub deck builders (s-bridges, cschladetsch, texodus, EskoSalaka, svarozhych, IristormDesign) | Collection and deck management; no evaluation described | MIT for s-bridges and cschladetsch per listings; others not shown | cschladetsch last push 2022; svarozhych 2024 | Not knowledge sources | S (S22) |
| digitalkw EDH power calculator | One rough estimate from ramp, interaction, tutors, combo density and curve averages (listing description) | not shown | not shown | Weights unknown | S (S23) |
| Scrollvault Salt Score and Mana Base Calculator | Salt Score page is not Commander Salt: per summary, a frustration gauge tied to table annoyance. The mana calculator claims hypergeometric math and 3.75 million simulated games. | not shown | not shown | Self-reported; pages not opened | S (S24, S25) |
| playgroup.gg | Elo-style comparison against a deck catalog, plus a Salty Score from opponent votes (summary) | not shown | not shown | Not opened | S (S27) |
| Commander Salt (the project's power measure) | No external page surfaced in this search | n/a | n/a | The project records it in its own docs (docs/proposals/commandersalt-adoption.md). Method not verified here. | none |

### Inferences
- No open-source project found encodes expert Commander card-evaluation judgement. The closest reusable knowledge is Spellbook's combo data.
- The functions the owner's consistency gate checks (recursion, evasion, answers to big or wide boards, enablers) are not named in any tool listing or summary read here. A project-specific check must cover them.
- An AI-player engine (XMage or Forge) could serve as a playtest sandbox. Its multiplayer play quality would need a test before the project depends on it.

## Conflicts between sources

1. Free mulligan in 1v1 formats: S1 says Duel Commander's first mulligan is not free. S7 (summary) says the Commander Rules Committee's informal guidance backs free mulligans even in two-player games. Not reconciled; the committee's own text was not read.
2. Rules number of the multiplayer exemption: search summaries give CR 103.4c and CR 103.5e. Neither was read in primary text. The 103.4c attribution comes from an excluded EDHREC article.
3. Commander land counts: S3 gives a 43-land baseline (range 36 to 46) and says current decks run about 36. S4 (summary) gives 40 for Commander by translating 24 lands in 60 cards. S3's author gives 26 to 30 for cEDH. S5 (summary) gives 26 lands for 60-card targets, which are not comparable to 100-card decks. The baselines differ (60-card versus 100-card; cEDH versus casual; EDHREC-attributed average). Not reconciled.
4. Example mana totals: S12 gives 3 and 9. Printed costs as recalled give 4 and about 10. Unresolved until checked on Scryfall.
5. Cut order: S14 (summary) says playtest extra cards before cutting. S16 (summary) says trim the most-played or strongest staples first. The S16 summary is unclear. Not reconciled.
6. Value of 1v1 volume: S8 (summary) favours quick 1v1 volume. S9 (summary) warns that loose solo play misleads. No source read measures the transfer from 1v1 to pods.
7. Game-count headlines: S10 (one author's roughly 50 playtests) and S11 (season statistics titled "50 games") are not comparable, and neither is a benchmark.

## Gaps

- Card evaluation: the last ten slots (none found; the likely sources were EDHREC pages, excluded); stand-alone value versus synergy breadth as a method (none); scaling with pod size (only an indirect remark in S2); win-more, high floor against high ceiling, conditional text, and "does it do something by itself" (not searched).
- Playtesting: number of games or sample size for a useful signal (none); a source or definition for "engine online by turn N" (none); sample-hand analysis method (none); the official mulligan text and the Commander Rules Committee text (not read; a StarCityGames article on mulligans appeared but was not opened); transfer from 1v1 to pods (the Card Kingdom page returned HTTP 403).
- Iteration: postmortem and logging formats (none); bad card versus bad draw (none); signals after a few games (none beyond the inference above).
- cEDH: one article read; interaction density not quantified; the cEDH guide series not read.
- Prior art: Commander Salt's method and licence (no external page); licences and maintenance of the MCP servers and GitHub builders (not checked); Forge's multiplayer support (not stated); academic work on Magic deck building and LLM skills for Commander builders (not searched).
- Land math: Karsten's primary article (PDF unreadable); S4 and S5 figures unverified; S3's EDHREC-attributed average unchecked (EDHREC excluded).
- Excluded sources: several EDHREC pages that probably cover the synergy score, the last-slot question and mulligan practice were excluded by the owner's rule. This is a known gap, not a finding. Revisit only if the owner changes the rule.
- Method: fetched pages and search results are model summaries. Verify the two quotes (S2, S12) and every number against the page before the knowledge base relies on them.
