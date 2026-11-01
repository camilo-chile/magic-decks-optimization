# Ratio gaps: Karsten, Command Zone template, strategy counts, outcome data, mulligans (note 13)

Status: complete 2026-10-31 (all five targets; gaps listed at the end). Fills the gaps listed in `../skill-coverage.md` section 4 (items 2, 4, 5, 6, 7)
and the "[J]" counts of `.claude/skills/commander-deckbuilding/archetypes.json`.

Tags: **[Primary]** the author's own article or data; **[Data]** counted or simulated; **[Convention]** repeated across
sources; **[Opinion]** one author; **[Snippet]** search summary only, unverified.

Sources table at the end of the note.

## 1. Karsten: lands, colored sources, hypergeometric tables (target 1)

Access: tcgplayer.com article pages render by JavaScript (WebFetch sees only "TCGplayer"); the full text comes from the
site's own content API `https://infinite-api.tcgplayer.com/content/article/<uuid>/?source=infinite-content` (JSON, field
`body`; author field `frank-karsten`). Read 2026-10-31 in full. ChannelFireball's old URL answers 404.

### K1. "What's an Optimal Mana Curve and Land/Ramp Count for Commander?" [Primary, Data: simulation]
Frank Karsten, TCGplayer Infinite, 2022-07-15 (K1 in the table).
- Model: 99 cards = 1- to 6-drops (blank permanents), Sol Ring, N Arcane-Signet-like rocks, lands, plus the commander as
  a free spell. Criterion: expected compounded mana spent on the battlefield over the first 7 turns (six-drops count 6.2;
  rocks count 0). Goldfish (no interaction), no draw spells, no colors, no tapped lands. Monte Carlo + local search,
  stop at more than 200,000 simulations for the best deck. Free mulligan and draw on turn 1 for the starting player are
  modelled (CR 103.4c, 800.7 as he cites them). Game length 7 turns, justified by five Game Knights episodes where the
  first player lost by turn 8 or 9.
- Mulligan policy he used (useful for target 5): keep a first 7 with 3, 4 or 5 lands and no more than 5 lands + Signets
  combined, or any hand with Sol Ring and 1 to 5 lands; the second 7 (free mulligan) also keeps 2-landers; at 6 or 5
  keep 2 to 4 lands or 1 land + Sol Ring; at 4 always keep. He says the policy "need not be optimal".
- Results (99 cards; commander MV in the first column):

| Commander MV | 1 | 2 | 3 | 4 | 5 | 6 | Rocks | Lands |
|---|---|---|---|---|---|---|---|---|
| 2 | 9 | 0 | 20 | 14 | 9 | 4 | Sol Ring + 0 | 42 |
| 3 | 8 | 19 | 0 | 16 | 10 | 3 | Sol Ring + 0 | 42 |
| 4 | 6 | 12 | 13 | 0 | 13 | 8 | Sol Ring + 7 | 39 |
| 5 | 6 | 12 | 10 | 13 | 0 | 10 | Sol Ring + 8 | 39 |
| 6 | 6 | 12 | 10 | 14 | 9 | 0 | Sol Ring + 9 | 38 |

- Rules he draws: bulk of the curve at 2, 3 and 4; zero spells at the commander's MV in the pure model (real decks should
  not go to exactly zero, but run fewer); rocks pay off only with a 4+ MV commander; "Commander decks with fewer than 38
  lands and more than nine mana rocks may be better off by cutting a mana rock and adding a land".
- His general advice (quoted in short): start with **42 lands plus a Sol Ring**, cut **one land per 2 or 3 extra rocks**,
  **one per 3 or 4 cheap cantrips**, **one per 3 or 4 mana dorks**; for medium-power midrange decks "try not to go below
  37 lands". Ramp spells like Cultivate count as a rock plus a three-drop.
- Many draw spells or mana sinks: you may run one fewer five-drop and/or one fewer six-drop than the table. In his model
  the optimizer never kept Divination-type draw (the model has no synergies to dig for); he says real decks value draw more.
- Near-optimal is flat: a nearby deck scored 99.96 % of optimal; big shifts (six lands for six three-drops) about 98 %.
- He quotes the EDHREC typical land count as 36 (from a Magic Data Science article) and calls it too low.
- Reliability: high for what it models (author is the field's reference for this math; code public); low for casual
  interaction-heavy pods (goldfish, no draw, 7-turn horizon). It does not model landfall or extra land drops.

### K2. "How Many Lands Do You Need in Your Deck? An Updated Analysis" [Primary, Data: regression]
Frank Karsten, TCGplayer Infinite, 2022-07-29.
- Data: **95,143 60-card decks** with more wins than losses on MTG Melee and Magic Online, 2020-07-01 to 2022-07-01
  (dataset on Kaggle). **Not Commander decks**: earlier notes (notes/02 S2, S12, S13) that call it "95,000 winning
  Commander decks" are wrong.
- 60-card fit: lands = 19.59 + 1.90 x avg MV - 0.28 x cheap draw-or-ramp + 0.27 x companion; R-squared 0.395, RMSE 2.75.
- 99-card port: lands = 99/60 x (19.59 + 1.90 x avg MV + 0.27) - 0.28 x cheap - 1.35 = **31.42 + 3.13 x avg MV -
  0.28 x cheap**. The -1.35 calibrates the port to K1's 42-land optimum (43.35 by scaling, minus free mulligan and
  turn-one draw); he calls it "an imprecise back-of-the-envelope estimate".
- Worked number in his own TL;DR: at average MV 3, "start with 40 or 41 lands and cut one land for every three or four
  cheap card draw or mana ramp spells". (Computed: 31.42 + 9.39 = 40.8; with 10 cheap spells 38.0.)
- "Cheap" = mana value **two or less** (draw: Oracle text with draw a card/two/three, creatures only with an ETB;
  "look ... library ... your hand" selection; one-mana cycling. Ramp: "add" mana, land search without sacrifice, etc.).
  Average MV = nonland cards (whether the commander is included is not stated).
- Adjust per card: efficient and reliable ramp/draw (one-mana cantrips, rocks, land search) cut a land per 2 or 3; fragile
  or inefficient ones (two-mana cantrips, dorks) one per 4 or 5.
- Reliability: the 60-card regression is high-quality data; the 99-card port is a calibration of one simulation, not
  Commander data.

### K3. "How Many Sources Do You Need to Consistently Cast Your Spells? A 2022 Update" [Primary, Data: simulation]
Frank Karsten, TCGplayer Infinite, 2022-08-02 (uuid dc23a7d2-0a16-4c0b-ad36-586fcca03ad8).
- Definition of "consistent": at least **89 + M %** to have N colored sources by turn M **on the play, conditional on
  having drawn at least M lands by turn M**, after a London mulligan policy. The 99-card deck is assumed to hold
  **41 lands**. Commander: free mulligan and draw on turn 1 included. Mulligan policy in this model: mulligan a free 7
  with 0, 1, 2, 6 or 7 lands; a regular 7 with 0, 1, 6 or 7; bottom toward 3 lands.
- **99-card table** (colored sources of that color; C = one colored pip; read at turn = MV):

| Cost | 99 | Cost | 99 | Cost | 99 |
|---|---|---|---|---|---|
| C | 19 | 1CC | 28 | 4CC | 22 |
| 1C | 19 | 2CC | 26 | 5CC | 20 |
| 2C | 18 | 3CC | 23 | CCC | 36 |
| 3C | 16 | CC | 30 | 1CCC | 33 |
| 4C | 15 | 2CCC | 30 | 3CCC | 28 |
| 5C | 14 | 4CCC | 26 | 1CCCC | 36 |
|  |  |  |  | CCCC | 39 |

- Gold cards: take each color's need from the table, then add **one** to each requirement (and to the combined
  either-color count).
- Partial sources (for spells of MV 2+ or 3+ as stated): fragile dorks **0.5** per color (MV 2+); rocks like Signets
  **0.75** per color (MV 3+); two-mana land ramp castable on turn 2 **0.75** (MV 3+); three-mana ramp (Cultivate type)
  **0.5** (MV 5+); one-shot Treasure **0.25** each (MV 3+); cheap cantrips about the land share of the deck, rounded
  down; cheap scry 1 in a 99 with 30 sources of that color **0.2**, scry 2 **0.3**; only the first 10 draw effects count;
  Exotic Orchard **0.75** of any color, Fellwar Stone **0.5** with unknown opponents; Fabled Passage-type fetch in a 3+
  color deck **2/3** of each color; fetches that find duals count full.
- Turn 1 counts only untapped sources; from turn 2 all sources count. Tapped-land tolerance is given **only for 60
  cards**: up to 3 in aggro with one-drops, up to 9 in midrange/control without one-drops. No Commander number.
- Off-band land counts: scale by share (for example 18/25 of lands blue); 60-card tables at 20/25/30 lands show the need
  moves by about 2 to 5 sources.
- Reliability: high (primary, simulation code public).

### Resolution of the notes/02 conflict (19 and 30 "fail to reproduce")
notes/02 tested the 99-card 19 and 30 unconditionally (no mulligan, not conditioned on land drops) and got 83 % and 82 %.
K3's figures are **conditional on having M lands by turn M, on the play, with mulligans**. That condition removes the
land-screw games, so the same source counts give 90 % and 91 %. The 19 and 30 are correct under K3's definition. The
unconditional computed table in notes/02 answers a different, stricter question (color and land count together).

### Correction to earlier notes
- notes/02 inferred "formula gives 38 for midrange (MV 3.0, ramp 10)": arithmetic right, but its ramp count must be MV 2 or
  less only (Cultivate and Kodama's Reach do not count); with Signets/Talismans/Sol Ring/Arcane Signet as the cheap ramp it
  holds.

## 2. The Command Zone template (target 2)

The episodes themselves (video/audio) were not transcribed; the EDHREC show notes carry chapters but no numbers
(notes/09, notes/11). Numbers below come from two independent written summaries that agree, plus one 2022 article for
the older template. Reddit (r/magicTCG thread on the new template) answered HTTP 403 (bot wall; not bypassed).

### CZ-new: episode 658 "Commander Deckbuilding Template for the New Era" (2025-02-18)
Summaries: Alan W Smith, "Notes on Commander Deck Building Templates for the New Era", January 2026
(https://www.alanwsmith.com/en/38/z9/2w/vi/) and そういちろう, note.com translation-summary, 2025-08-04
(https://note.com/black777cat/n/n588a5c571b7d). A third, Farseek blog (search summary only), gives the same six numbers.

| Category | Count | What counts / how to adjust (per the note.com summary) |
|---|---|---|
| Lands | **38** | Start at 38. One-mana basic landcyclers count as tapped lands; MDFCs as lands (project bans MDFCs). "With 38 lands, 3+ lands in the opening 7 about 55 %" |
| Card advantage | **12** | Cards that net two or more cards (cantrips do not count); repeatable draw, big one-shot draw, impulse draw, self-mill in graveyard decks |
| Ramp | **10** | **12 if the commander costs 4 or more**; rituals do not count; too much ramp at the cost of lands is counterproductive. 10 pieces: about 63 % to have one by turn 2 (Smith: 54 % in the opener, 63 % by turn 2; with 12: 61 % and 70 %) |
| Targeted disruption | **12** | Creature removal, counterspells, bounce, phasing, tappers, land destruction, targeted graveyard hate; about 70 % to have one by turn 2 |
| Mass disruption | **6** | Wipes plus mass effects (graveyard wipes such as Bojuka Bog, Propaganda-type effects, artifact/enchantment sweepers); mix the roles |
| Plan cards | **about 30** | Enablers, payoffs, enhancers |

- Total 108: cards overlap categories on purpose.
- Average curve they give (two summaries, slight differences): 1 MV 9; 2 MV 18 (peak); 3 MV 14 to 15; 4 MV 10;
  5 MV 4 to 5; 6+ MV 3 to 5. Five-plus only for game-defining cards; six-mana permanents avoided unless the deck reanimates.
- Commander role: payoff commander, run many enablers; enabler commander, run more high-impact payoffs and protect the
  commander; enhancer commander, run as many enablers as possible.
- Reliability: medium-high. Two independent summaries agree on all six numbers; the episode itself was not heard.
- Note the shift from the old template: lands up (35-38 to 38), wipes become "mass disruption" 6 (wider), removal becomes
  "targeted disruption" 12 (counters and graveyard hate included), draw becomes "card advantage" 12.

### CZ-659: "The Problem with Deckbuilding Templates" (2025-02-26)
Show notes only (https://edhrec.com/articles/the-command-zone-the-problem-with-deckbuilding-templates-the-command-zone-659-mtg-edh-magic-gathering):
chapters "Exceptions for Ramp / Card Advantage / Targeted Disruption / Mass Disruption / Lands", "What's the Magic
Number?". The text holds no numbers; the episode is the hosts' own statement that the template must bend by strategy.
Not transcribed (gap).

### CZ-old: the earlier template as quoted in 2022
Benjamin Nicol, "Solve the Equation: How to Tell if a Strategy Has Enough Support Using Deck Templates", EDHREC,
2022-09-13 (https://edhrec.com/articles/solve-the-equation-how-to-tell-if-a-strategy-has-enough-support-using-deck-templates).
- Ramp **10-12**; card draw **10**; removal **10-12**; board wipes **3-4**; lands **35-38**; standalone **25**;
  enhancers **10-12**; enablers **7-8**.
- Method: count each synergy category against the suggested range before building; a theme with 16 eligible lands was
  "not a substantial amount of support" and needed enablers; the sub-theme (landfall, three extra-land-drop cards) must
  support the main theme.
- Reliability: medium (secondary quote of the template by an EDHREC writer; matches other secondary quotes).
- Useful as a sourced anchor for plan-part sizes: **enablers 7-8 and enhancers 10-12** inside about 30 to 45 plan cards.

## 3. Counts per strategy (target 3)

### E1. EDHREC Bracket-3 average decks, counted by function [Data, computed here]
Source: `https://json.edhrec.com/pages/average-decks/<slug>/upgraded.json` ("Upgraded" = Bracket 3 average deck),
fetched 2026-10-31 with 1.5 s pauses, 54 commanders (two answered 403 and were skipped: storm-kiln-artist,
rabbit-battery). Seven to eight archetypal commanders per archetype, chosen by me as well-known examples (list in the
script). Counting: Scryfall oracle bulk 2026-10-11 (Oracle text, keywords) plus the Scryfall Tagger tags cached in
`data/cache/oracle-tags.json` (2026-10-31). Script: scratchpad `scripts/avg_profile.py` (not in the repo); output
`avg_profile.json`. All 54 decks matched 99/99 cards to Oracle.

Caveats (read before using): an average deck is the most-included card per slot across many lists, not a real list,
and it shows community **behaviour, not quality** (notes/09). Tagger tags are broad ("ramp" includes extra land drops
and land tutors; "draw" includes cantrips; "protection" includes equipment and blink). Regex counts miss wordings and
can double-count. Treat every number as a range anchor, not a target.

Median (min to max) per archetype, cards in the 99:

| Count | Landfall | Spellsl. | Combat | Tokens | Voltron | Aristocr. | Counters |
|---|---|---|---|---|---|---|---|
| lands | 39.5 (38-46) | 35 (34-36) | 35.5 (34-37) | 35 (35-36) | 35 (34-36) | 35.5 (34-36) | 35 (34-37) |
| avg MV nonland | 3.22 | 2.52 | 3.16 | 3.05 | 2.48 | 2.77 | 2.79 |
| creatures | 25.5 | 13 (10-17) | 30.5 (27-46) | 26 | 17 (14-23) | 32.5 | 29.5 |
| instants + sorceries | 20.5 | **36 (31-43)** | 16 | 19 | 13.5 | 16 | 15.5 |
| ramp (Tagger, broad) | 28.5 (22-37) | 13 (7-17) | 13.5 (8-21) | 17 | 10 (3-15) | 17 | 20 |
| draw (Tagger, incl. cantrips) | 8 (5-11) | **21 (15-27)** | 7 (2-10) | 11 | 7 | 10 | 9.5 |
| card advantage (Tagger) | 12 | 25 (20-29) | 8.5 | 11 | 9 | 11 | 13 |
| removal (Tagger) | 5.5 | 11 | 10.5 | 10 | 8.5 | 14.5 | 6.5 |
| board wipes | 1 | 3 | 2.5 | 2 | 2 | 2 | 1 |
| counterspells | 0.5 | 5 (2-12) | 0 | 0 | 0 | 0 | 0 |
| protection (Tagger, broad) | 2 | 1 | 10 (2-15) | 4 | **15.5 (10-20)** | 1.5 | 4 |
| gives haste (Tagger) | 1 | 1 | **4 (0-8)** | 1 | 2 (1-4) | 0.5 | 1.5 |
| creatures with haste | 0 | 1 | 2 (0-6) | 1 | 0 | 0.5 | 0.5 |
| gives evasion (Tagger) | 0 | 0 | 3 (0-6) | 2 | **5.5 (2-12)** | 0.5 | 1.5 |
| team evasion (regex) | 1 | 0 | 1.5 (0-4) | 1 | 0 | 0 | 0.5 |
| evasive creatures | 2.5 | 2 | **12 (7-26)** | 2 | 1 | 4 | 6 |
| vigilance creatures | 0 | 0 | 4 (1-5) | 1 | 2 | 1 | 0 |
| attack taxes / fogs / goad | 0 | 0 | 0 (0-1) | 0 | 0 (0-1) | 0 | 0 |
| extra land drops (regex) | **7 (3-10)** | 0 | 0 | 0 | 0 | 0 | 0 |
| land recursion (regex) | **6 (2-11)** | 0 | 0 | 0 | 0 | 0 | 0 |
| lands onto battlefield (regex) | **16 (11-20)** | 1 | 3 | 4 | 3 | 5.5 | 6 |
| landfall payoffs (regex) | **11.5 (5-21)** | 0 | 0 | 2 | 0 | 0.5 | 1 |
| spell-cast payoffs (regex) | 0 | **8 (3-15)** | 0 | 0 | 0 | 0 | 0 |
| cost reducers (regex) | 0 | 3 (1-8) | 0 | 0 | 1.5 | 0 | 0 |
| token makers (regex) | 8.5 | 8 | 8 | **32 (13-35)** | 2 | 17 | 7 |
| team pump "creatures you control get +" | 0 | 0 | 2 | 4 (0-6) | 0 | 0 | 0 |
| anthem (Tagger) | 0 | 0 | 1.5 | 6 (1-14) | 0 | 0 | 0 |
| death payoffs (regex) | 1 | 0 | 0 | 0 | 0 | **7 (2-13)** | 0 |
| sacrifice outlets (Tagger) | 6.5 | 0 | 1.5 | 2 | 0 | **18 (14-25)** | 0 |
| +1/+1 counter cards (regex) | 3.5 | 0 | 4 | 5 | 0.5 | 4.5 | **20.5 (3-46)** |
| doublers / proliferate (regex) | 1 | 0 | 0 | 3 | 0 | 1 | **11 (0-25)** |
| recursion (Tagger) | 8 | 2 | 1 | 0 | 3 | 5.5 (2-13) | 2 |

Commanders: landfall Tatyova, Omnath Locus of Rage, Lord Windgrace, Aesi, Titania Protector of Argoth, Omnath Locus of
Creation, Lumra, Moraug; spellslinger Talrand, Mizzix, Veyran, Kalamax, Niv-Mizzet Parun, Kykar, Lier; combat Isshin,
Aurelia, Kaalia, Winota, Najeela, Saskia, Gishath, Edgar Markov; tokens Rhys, Adrix and Nev, Jetmir, Chatterfang, Krenko
Mob Boss, Jinnie Fay, Brimaz; voltron Uril, Sram, Light-Paws, Rafiq, Wyleth, Syr Gwyn, Sigarda Host of Herons, Kemba;
aristocrats Teysa Karlov, Judith, Prossh, Korvold, Meren, Mazirek, Elas il-Kor, Savra; counters Atraxa Praetors' Voice,
Ezuri Claw of Progress, Marath, Ghave, Zegana, Hamza, Pir, Bello.

Per-commander detail worth keeping:
- Landfall (lands, extra land drops, land recursion, lands onto battlefield, landfall payoffs): Tatyova 39/10/5/20/13;
  Omnath Rage 39/7/7/14/12; Windgrace 40/7/11/13/13; Aesi 40/8/2/17/11; Titania 40/5/8/15/7; Omnath Creation 38/9/7/17/21;
  Lumra 46/4/5/17/10; Moraug 39/3/2/11/5. Extra-land-drop check on Tatyova's list: Aesi, Azusa, Dryad of the Ilysian
  Grove, Icetill Explorer, Oracle of Mul Daya, Wayward Swordtooth, Druid Class, Exploration, Explore.
- Spellslinger (I/S, Tagger draw, cost reducers, spell payoffs, copy): Talrand 40/23/4/3/0; Mizzix 43/21/4/8/4; Veyran
  36/21/3/15/4; Kalamax 39/15/3/10/11; Niv-Mizzet Parun 33/27/3/7/1; Kykar 31/20/1/11/0; Lier 36/23/8/4/2.
- Combat (gives haste + haste creatures; evasive creatures; vigilance creatures): Isshin 5+6 / 8 / 4; Aurelia 4+1 / 17 / 5;
  Kaalia 4+1 / 26 / 4; Winota 2+3 / 14 / 3; Najeela 5+4 / 7 / 3; Saskia 8+3 / 8 / 5; Gishath 3+0 / 14 / 4; Edgar 0+1 / 10 / 1.
  Kaalia's haste sources by tag: Lightning Greaves, Swiftfoot Boots, Dragon Tempest, Windcrag Siege.

### W. Written guides with counts (lower reliability)
- Voltron, Ian Flores, Rate My Decks, "Voltron Commander", updated 2026-06-21
  (https://www.ratemydecks.com/en/blog/voltron-commander-guide) [Opinion]: equipment and auras "at least 15-20";
  protection spells "8-10"; ramp 8-12; draw 8-12; removal 8-10. No haste or evasion count.
- Voltron, DonSpider, Nerd Leagues, 2026-07-02 (https://www.nerdleagues.com/blog/how-to-build-a-winning-voltron-edh-deck)
  [Opinion]: mana rocks 8-12; no other counts. Power math: 7 power needs three hits, 11 two, 21 one.
- Voltron search summaries (unverified, sites of unknown authorship: grimdeck, krakenthemeta, tcgcustom, gamertagmythras)
  [Snippet]: equipment 12-18, or 10-12 equipment plus 4-6 auras, or 18-24 total; evasion sources 6-8; both haste-and-
  protection equipment.
- Spellslinger, Nick Price, EDHREC "Guide to Spellslinger in Commander", 2026-04-08
  (https://edhrec.com/articles/edhrec-guide-to-spellslinger-in-commander/) [Opinion]: no counts; its sample list runs
  34 lands, 38 instants and sorceries, 20 creatures, 3 rocks, 2 counterspells.
- Spellslinger search summaries [Snippet]: Draftsim Kalamax list (updated 2025-09-22) 35 instants + 5 sorceries, 13
  creatures; Card Kingdom (page 403) author's extreme Talrand list 52 instants and sorceries and the rule "critical mass".
- Landfall search summaries [Snippet; blogs of unknown authorship: mulligo, krakenthemeta, playgroup]: 38-40, 39-42,
  40-42, 40-44 lands; "ramp supplements lands, it does not replace them"; no extra-land-drop count.

Reading:
- **Landfall** behaviour supports the profile's land band and its land-entry lines, and runs **more** extra land drops
  (median 7) and land recursion (median 6) than the profile's [J] 4 to 6 and 2 to 4. Lands onto the battlefield (16)
  sits above the [J] land_entries 10 to 14.
- **Spellslinger** decks run about 36 instants/sorceries (profile [J] 28 to 32) and far more draw than any other
  archetype (Tagger draw 21 incl. cantrips; card advantage 25) on 34 to 36 lands with average MV 2.5.
- **Combat**: about 5 haste sources total (gives haste median 4 plus creatures with haste), many evasive creatures
  (median 12), little team-wide evasion (median 1.5 by regex, gives-evasion tag 3), and almost **no** defense while
  tapped beyond about 4 vigilance creatures (taxes, fogs, goad 0). Community lists do not do what the profile's
  defense_while_tapped line asks; that line stays a judgment call driven by the owner's lessons.
- **Voltron**: protection is the biggest line (Tagger 15.5, includes equipment), evasion granting 5.5, haste granting 2.
- **Aristocrats**: sacrifice outlets 18 (Tagger is broad: any "sacrifice a creature:" text), death payoffs 7, token makers 17.
- **Counters**: counter cards 20.5, doublers/proliferate 11.
- **Tokens**: token makers 32 (regex, any "create ... token" text, includes Treasure), anthem/pump 4 to 6.

## 4. Data linking ratios to results (target 4)

- **Opening-hand lands vs win rate** [Data, observational], Playgroup.gg "How Many Lands Should a Commander Deck Run?",
  updated 2026-10-31 (https://playgroup.gg/commander/how-many-lands), 173,016 opening hands from tracked games:

| Lands in opener | Hands | Win rate duel | Win rate 4-6 players |
|---|---|---|---|
| 0 | 473 | 33 % | 17 % |
| 1 | 8,194 | 46 % | 25 % |
| 2 | 47,419 | 49 % | 28 % |
| 3 | 69,927 | 51 % | 28 % |
| 4 | 36,804 | 52 % | 29 % |
| 5 | 8,942 | 50 % | 28 % |
| 6 | 1,070 | 42 % | 24 % |
| 7 | 187 | 49 % | 26 % |

  In pods, 2 to 5 lands sit within one point of each other (28 to 29 %); 0 to 1 and 6 lose 4 to 11 points. The page
  calls it "Directional, not a verdict"; opener lands confound deck build, mulligans, skill. Same page: 89 % of kept
  openers had 2 to 4 lands, average 2.96 lands; average game 8.76 rounds (median 9) over 1,591,235 finished games.
- **No measured deck-level land count vs win rate** was found (Playgroup gives none; Karsten has none for Commander:
  "especially for Commander it's hard to find data on a deck's performance", K2).
- Playgroup ramp pages (search summary, https://playgroup.gg/commander/ramp/green) report per-card win-rate lift as a
  Mantel-Haenszel pooled difference against decks of the same commander, published only when the 95 % CI is above zero:
  Bloom Tender +3.8, Delighted Halfling +2.0, Farseek +0.1 points [Snippet]. With notes/02 S3 (only Sol Ring survives
  correction in a 143-card screen), card-level ramp lifts are small.
- Karsten K1's game-length check: in five Game Knights episodes the first player lost by turn 8 or 9; Playgroup's
  measured 8.76 rounds agrees. A 7-turn curve horizon is therefore a reasonable model for casual pods.
- 17lands-type data for Commander: none found. Commander Spellbook publishes combo counts, not ratio outcomes (notes/08).

## 5. Mulligan guidance (target 5)

- Rules basis as Karsten cites them (K1, K3): CR 103.4c, the first mulligan in multiplayer is free; CR 800.7, the
  starting player draws on turn 1 in multiplayer. (Earlier notes cite 103.8c for the draw; Karsten's 2022 numbering is
  800.7. Re-check the current CR before quoting either.)
- Measured [Data, Playgroup, as in section 4]: 65 % of games no mulligan, 24 % one, 8 % two, 3 % three or more (1,591,235
  games); 89 % of kept hands have 2 to 4 lands.
- Karsten's modelled policies [Primary]:
  - K1 (curve model): keep the first 7 with 3 to 5 lands (and at most 5 lands + rocks), or Sol Ring with 1 to 5 lands;
    after the free mulligan also keep 2 lands; at 6 or 5 cards keep 2 to 4 lands or 1 land + Sol Ring; always keep 4.
  - K3 (color model): mulligan a free 7 with 0, 1, 2, 6 or 7 lands; a regular 7 with 0, 1, 6, 7; bottom toward 3 lands.
  - Both say the policy is reasonable, not optimal, and should depend on the deck.
- Per-commander snapshots on Playgroup (search summary, small samples) show win rate falling after one mulligan (for
  example 24.8 % to 22.2 % over 1,196 games for one commander) [Snippet].
- Computed here (hypergeometric, 99 cards, 7 cards): chance of 2 to 4 lands is 74.0 % at 36 lands, 75.5 % at 38, 76.4 %
  at 40; with one free retry 93.3 %, 94.0 %, 94.4 %. Chance of 3+ lands: 50.1 % at 36, 54.8 % at 38, 59.4 % at 40
  (the Command Zone's "about 55 % at 38" reproduces). Chance of 0 to 1 lands: 20.1 % at 36, 17.1 % at 38, 14.4 % at 40.
- Takeaway for building: a deck that wants to keep only 3+ land hands (landfall, big mana) needs about 40 lands to make
  that keep more likely than not in one look; the free mulligan covers most of the gap at 36 to 38 for 2-land keeps.

## 6. [J] counts: sourced range now available

"E1" = the Bracket-3 average-deck counts of section 3 (behaviour, not quality; regex and Tagger caveats apply).
Suggested values are my proposal for the skill owner to review; archetypes.json was not edited.

| Profile.function | Current [J] min-target | Sourced range now | Suggested |
|---|---|---|---|
| landfall.land_entries | 10-14 | E1 lands onto battlefield 16 (11-20) | min 12, target 16 |
| landfall.extra_land_drops | 4-6 | E1 7 (3-10); CZ-old example sub-theme 3 | min 5, target 7 |
| landfall.land_recursion | 2-4 | E1 6 (2-11) | min 3, target 5 |
| landfall.landfall_payoffs | 10-12 | E1 11.5 (5-21) | keep 10-12 |
| landfall.mana_sinks | 3-4 | still no source (K1: many sinks allow one fewer 5- or 6-drop, qualitative) | keep 3-4 |
| landfall land band | 38-40 (sourced) | E1 39.5 (38-46); K1 start 42; K2 at MV 3.2 with few cheap spells about 41 | keep 38-40, lean 40 |
| spellslinger.spell_density | 28-32 | E1 36 (31-43); EDHREC sample 38; Draftsim Kalamax 40 [Snippet] | min 30, target 36 |
| spellslinger.spell_payoffs | 10-12 | E1 regex 8 (3-15), undercounts | keep 10-12 (gate), note community 8 |
| spellslinger.draw (partly sourced) | 12-15 | E1 Tagger draw 21 (15-27, incl. cantrips), card advantage 25 | min 12, target 18 |
| spellslinger curve | 2.5-3.0 | E1 2.52 (2.37-3.12) | keep |
| spellslinger cost reducers | none | E1 3 (1-8) | add support line 2-4 |
| go_wide.token_makers | 12-15 | E1 regex 32 (13-35, Treasure included) | min 15, target 20 |
| go_wide.token_payoffs | 6-8 | E1 anthem tag 6 (1-14), team pump 4 (0-6) | keep 6-8 |
| go_wide.wipe_insurance | 3-4 | still no source (E1 protection tag 4, broad) | keep 3-4 |
| go_wide curve | 2.6-3.1 | E1 3.05 (2.58-3.59) | 2.7-3.2 |
| voltron.equipment_auras | 10-15 | Rate My Decks 15-20; snippets 12-18, 18-24 | min 12, target 16 |
| voltron.evasion | 6-8 | E1 gives-evasion 5.5 (2-12); snippet 6-8 | keep 6-8 |
| voltron.haste | 2-3 | E1 gives-haste 2 (1-4) | keep 2-3 |
| voltron protection (profile line) | per dependence | Rate My Decks 8-10 protection spells; E1 Tagger 15.5 (broad) | engine min 6, target 8-10 |
| voltron curve | 2.3-3.0 | E1 2.48 (2.08-2.81) | keep |
| combat.attackers | 12-16 | E1 evasive creatures 12 (7-26), creatures 30.5 | keep 12-16 |
| combat.haste | 4-6 | E1 gives haste 4 + hasty creatures 2, total about 5 (1-11) | keep 4-6, target 6 |
| combat.team_evasion | 6-8 | E1 team regex 1.5 (0-4), gives-evasion 3 (0-6): community runs fewer | still no source for 6-8; keep as owner-lesson [J] or min 4 |
| combat.defense_while_tapped | 4-6 | E1 vigilance creatures 4 (1-5); taxes, fogs, goad 0 | partly: vigilance about 4; rest still no source; keep |
| combat.combat_draw | 4-6 | still no source | keep |
| counters.counter_sources | 10-14 | E1 20.5 (3-46) | min 12, target 18 |
| counters.counter_doublers | 3-5 | E1 doublers + proliferate 11 (0-25) | min 4, target 7 |
| counters.counter_payoffs | 6-8 | still no source | keep |
| counters.evasion | 4-6 | E1 evasive creatures 6 (2-13) | keep |
| counters curve | 2.8-3.2 | E1 2.79 (2.47-3.69) | 2.7-3.1 |
| aristocrats.wipe | 2-3 | E1 2 (0-5) | keep |
| aristocrats.fodder | 12-15 | E1 token makers 17 (4-24), creatures 32.5 | min 14, target 18 |
| aristocrats.death_payoffs | 10-12 | E1 regex 7 (2-13), undercounts | keep 10 (gate); community about 7-8 |
| aristocrats.recursion | 6-8 | E1 Tagger recursion 5.5 (2-13) | keep 6-8 |
| aristocrats curve | 2.6-3.1 | E1 2.77 (2.4-2.89) | keep |
| meta.commander_dependence protection (engine 5-8, enabler 3-4, value 2-3) | [J] | Rate My Decks voltron 8-10; E1 combat Tagger 10, voltron 15.5 (broad) | engine 6-10 for attack-based engines; others still no source |
| reanimator (wipe, fillers, reanimation, non-graveyard threats, curve) | [J] | still no source | keep |
| blink (etb creatures, blink effects, curve) | [J] | still no source | keep |
| artifacts (protection, density, payoffs, lands, curve) | [J] | still no source | keep |
| enchantments (density, payoffs, lands, curve) | [J] | still no source | keep |
| typal (lords_payoffs, curve) | [J] | still no source | keep |
| control_stax_lite.counterspells | 4-6 | E1 spellslinger counterspells 5 (2-12) as the nearest | keep 4-6 |
| control_stax_lite land_why, curve | [J] | still no source | keep |
| pillowfort.attack_deterrents | 10-12 | E1: taxes and fogs about 0 in every archetype sampled (not a pillowfort sample) | still no source |
| pillowfort curve | [J] | still no source | keep |
| big_mana.big_threats | 8-10 | K1 table: 4 to 10 six-drops by commander MV (6.2 value each) | keep 8-10 |

Generic numbers the skill should also reflect (sourced now):
- Lands: K1 start at 42 + Sol Ring, minus one per 2-3 extra rocks, per 3-4 cheap cantrips, per 3-4 dorks; floor 37 for
  midrange; K2 formula 31.42 + 3.13 x avg MV - 0.28 x cheap (MV 2 or less) draw/ramp. CZ-new 38. E1 community 34-36
  outside landfall. Karsten calls 36 too low; community plays 35.
- Ramp: CZ-new 10, **12 when the commander costs 4+**; K1 rocks pay off only with a 4+ MV commander (7 to 9 Signet-type
  rocks plus Sol Ring for MV 4 to 6 commanders, none for MV 2 to 3).
- Curve: K1 bulk at 2 to 4, fewer cards at the commander's MV; CZ-new 9/18/14-15/10/4-5/3-5.
- Colored sources: K3 99-card table (section 1), gold +1, partial-source weights.

## Sources
| ID | Title | Author | Date | How read | URL |
|---|---|---|---|---|---|
| K1 | What's an Optimal Mana Curve and Land/Ramp Count for Commander? | Frank Karsten | 2022-07-15 | Full text via TCGplayer content API | https://www.tcgplayer.com/content/article/What-s-an-Optimal-Mana-Curve-and-Land-Ramp-Count-for-Commander/e22caad1-b04b-4f8a-951b-a41e9f08da14/ |
| K2 | How Many Lands Do You Need in Your Deck? An Updated Analysis | Frank Karsten | 2022-07-29 | Full text via API | https://www.tcgplayer.com/content/article/How-Many-Lands-Do-You-Need-in-Your-Deck-An-Updated-Analysis/cd1c1a24-d439-4a8e-b369-b936edb0b38a/ |
| K3 | How Many Sources Do You Need to Consistently Cast Your Spells? A 2022 Update | Frank Karsten | 2022-08-02 | Full text via API (uuid dc23a7d2-0a16-4c0b-ad36-586fcca03ad8) | https://library-of-leng.com/articles/tcgplayer-dc23a7d2-0a16-4c0b-ad36-586fcca03ad8 (index page); API https://infinite-api.tcgplayer.com/content/article/dc23a7d2-0a16-4c0b-ad36-586fcca03ad8/?source=infinite-content |
| CZ-new | The Command Zone 658 summaries | Alan W Smith; そういちろう (note.com) | 2026-01; 2025-08-04 | Fetched | https://www.alanwsmith.com/en/38/z9/2w/vi/ ; https://note.com/black777cat/n/n588a5c571b7d |
| CZ-659 | The Problem with Deckbuilding Templates (show notes) | The Command Zone | 2025-02-26 | Fetched (chapters only) | https://edhrec.com/articles/the-command-zone-the-problem-with-deckbuilding-templates-the-command-zone-659-mtg-edh-magic-gathering |
| CZ-old | Solve the Equation | Benjamin Nicol (EDHREC) | 2022-09-13 | Fetched | https://edhrec.com/articles/solve-the-equation-how-to-tell-if-a-strategy-has-enough-support-using-deck-templates |
| E1 | EDHREC average decks, Upgraded (Bracket 3), 54 commanders | EDHREC data | fetched 2026-10-31 | JSON, counted here | https://json.edhrec.com/pages/average-decks/<slug>/upgraded.json |
| PG | How Many Lands Should a Commander Deck Run? (2026) | Playgroup.gg (no author) | updated 2026-10-31 | Fetched | https://playgroup.gg/commander/how-many-lands |
| W1 | Voltron Commander guide | Ian Flores (Rate My Decks) | 2026-06-21 | Fetched | https://www.ratemydecks.com/en/blog/voltron-commander-guide |
| W2 | How to Build a Winning Voltron EDH Deck | DonSpider (Nerd Leagues) | 2026-07-02 | Fetched | https://www.nerdleagues.com/blog/how-to-build-a-winning-voltron-edh-deck |
| W3 | EDHREC Guide to Spellslinger in Commander | Nick Price | 2026-04-08 | Fetched | https://edhrec.com/articles/edhrec-guide-to-spellslinger-in-commander/ |
| X | Reddit r/magicTCG thread on the new CZ template; Card Kingdom blog; ChannelFireball old URL | - | - | Blocked: Reddit 403 (bot wall, not bypassed), Card Kingdom 403, CFB 404 | - |

## Remaining gaps
- The Command Zone 658/659 audio not transcribed: per-strategy exceptions (659 chapters) unknown.
- Reddit and Card Kingdom unread (403).
- No source counts team evasion, defense while tapped, combat draw, wipe insurance, mana sinks, counters payoffs; the
  community average decks run almost no attack taxes or fogs in any archetype sampled.
- No deck-level outcome data for any ratio (only opener-level land data).
- Archetypes not sampled in E1: reanimator, blink, artifacts, enchantments, typal, control, pillowfort, big mana.
