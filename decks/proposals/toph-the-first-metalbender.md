# Toph, the First Metalbender: purchase ladder (Phase 8 step 2, round 3, 2026-10-19)

Ladder: `decks/proposals/toph-the-first-metalbender.ladder.txt` (base + 34 swaps). Checked with
`python -I -X utf8 scripts/ladder.py decks/proposals/toph-the-first-metalbender.ladder.txt`: all 35 steps valid
(0 INVALID; 100 cards, no reversible cards, Layer A floor 3 at target 3, 1-2 Game Changers, 0 extra-turn cards,
every purchase with stock > 0). Layer A notes, all review-only: Bumi + Ashaya (two-card, 10 mana, floor 3),
Toph + The Stasis Coffin (lock note), hub Toph Hardheaded Teacher, Springheart Nantuko template variants.
Prices: `merged-20261019T0300Z.json` (a hint; stock is verified in Phase 9). Control copies: round 1 in
`decks/proposals/round1/`, round 2 in `decks/proposals/round2/`.

## Round 3
Measured round 2 on Commander Salt 2026.4195 (`decks/reports/round2-measured-20261018.md`): free base 7.1 (cap -0.27
"wincon combos with no tutors"), 10,590 CLP 6.9 (cap -1.18 after the Coating combo arrived with no tutor),
24,610 CLP 6.9 (cap -0.50 and "too slow for its pieces"), 146,240 CLP 7.5 ("too slow", capped major). A mana base of
52 % to 93 % added little. Round 3 attacks those two caps and keeps the free base exactly as measured.

What changed and why:
| Change | Target |
|---|---|
| Free base unchanged (the measured 7.1 list) | keeps the floor of the curve |
| A tutor right after each new combo piece: Reckless Handling (step 2, finds Coating, Torque, Zuran Orb), Brightglass Gearhulk (9, finds Zuran Orb and Sylvan Safekeeper or Chalice), Chord of Calling (10, any creature: Ashaya, Bumi, loopers, Nantuko, Cobra) | cap "wincon combos with no tutors" |
| More tutors up the ladder: Imperial Recruiter (22, Nantuko, Cobra, Safekeeper, Earth Kingdom General), Inventors' Fair (26, a land that finds an artifact and returns with Toph's earthbend), Gamble (31, Game Changer, any card), Formidable Speaker (32, any creature), Green Sun's Zenith (33). End: 10 tutors with Seismic Sense and Crop Rotation | same cap |
| Cheap speed for the slowest cards: Everflowing Chalice, Talisman of Impulse, Sakura-Tribe Elder, Lotus Cobra in; Moraug (6), Titania (5), Awakening of Vitu-Ghazi (5), Bumi Eclectic Earthbender (5), The Earth King (4), Solemn (4) out. Average mana value 2.53 to 2.30 by 24,152 CLP (round 2 went up to 2.77) | "too slow for its pieces" |
| The fastest line bought early: Toph + Springheart Nantuko + Lotus Cobra or Tireless Provisioner (3 cards, 2-mana pieces) by 45,752 CLP | "too slow for its pieces" and more win lines |
| Goblin Bombardment (step 8): Ashaya + Bombardment + Blind Bandit or Earth Kingdom General wins on the spot | one reliable win path that needs no extra payoff |
| Dropped from round 2 as slow or low value per CLP: Felidar Retreat, Avenger, Spitfire Lagac, Koth, Survey Mechan, All-Fates Scroll, Evolution Sage, Scute Swarm, Heroic Intervention, Toph Greatest Earthbender, Inspiring Call, Generous Gift; 6 of round 2's 12 land purchases (Rockfall Vale, Karplusan Forest, Overgrown Farmland, Brushland, Stomping Ground, Sacred Foundry) replaced by cheaper ones (Game Trail, Fortified Village, Rugged Prairie, Furycalm Snarl, Razorverge Thicket) or Inventors' Fair, all after the tutors | lands did not move Toph's power; cheap ones stay for Manabase Quality |

Checkpoints to measure (no power numbers: the measurement replaces them):
| Cap CLP | Step | Cost CLP | Stores | Tutors in the list | Main additions |
|---|---|---|---|---|---|
| 0 | 0 | 0 | none | Seismic Sense, Crop Rotation | the measured 7.1 base |
| 25,000 | 11 | 24,152 | cardnexus, gameofmagic, magic4ever, oasis, paytowin | + Reckless Handling, Brightglass Gearhulk, Chord of Calling | Coating line, Bombardment, Lantern, Chalice, Talisman, Sakura-Tribe Elder |
| 50,000 | 21 | 49,142 | same 5 | same 5 | Lotus Cobra, Springheart Nantuko, Tireless Provisioner (fast line), 6 cheap duals |
| 75,000 | 23 | 73,842 | same 5 | + Imperial Recruiter | Sylvan Safekeeper (outlet and protection) |
| 100,000 | 30 | 97,537 | same 5 | + Inventors' Fair | Torque, Kutzil, 4 duals |
| 150,000 | 32 | 148,907 | + lacomarca (Gamble) | + Gamble (Game Changer 2 of 3), Formidable Speaker | - |
| 200,000 | 34 | 195,007 | same 6 | + Green Sun's Zenith | Temple Garden |

Consolidation: oasis sells Reckless Handling, Everflowing Chalice and Liquimetal Torque (Reckless Handling is 690 at
cardnexus); gameofmagic sells Talisman of Impulse, Goblin Bombardment, Brightglass Gearhulk, Razorverge Thicket and
Inventors' Fair. All six stores are in the Azula plan already.

## Strategy and engine
Metal landfall with tutored combo finishes. Toph makes every nontoken artifact a land, so each rock or bauble is a
landfall trigger and, with Great Divide Guide, Wrenn or Chromatic Lantern, a mana source. Landfall pingers (Tannuk,
Sabotender, Arbaaz Mir, Ragost, Valakut Exploration) and earthbend counters (Terrasymbiosis, Hardened Scales, Toph
Hardheaded Teacher) carry the fair game; ten tutors find one of four infinite lines.

Combo lines (Spellbook variants in the local bulk: 5 on the base, 7 at step 11, 13 at step 21, 16 from step 30):
| Line | Cards | From | Result | Tutors that reach it | Layer A |
|---|---|---|---|---|---|
| A | Toph + Bumi, Unleashed + Liquimetal Coating (Torque from step 24) | step 1 | Bumi becomes an artifact, so a land: each time he connects all lands untap and he attacks again in the extra combat; Rogue's Passage untaps every combat. Infinite combats | Reckless Handling, Inventors' Fair, Gamble (Coating); Chord, Seismic Sense, Speaker, GSZ (Bumi) | 3 cards with the commander: no floor |
| B | Ashaya + Bumi, Unleashed | base | Ashaya makes every nontoken creature a land: infinite combats with the team | Chord, Seismic Sense, Speaker, GSZ, Gamble | two-card, 10 mana: floor 3 (late) |
| C | Ashaya + Zuran Orb, Goblin Bombardment (step 8) or Sylvan Safekeeper (step 23) + Toph the Blind Bandit or Earth Kingdom General | base | The creature is a land, earthbends itself as it enters, is sacrificed and returns: infinite enters, landfall and deaths. Bombardment wins by itself; with the Orb or Safekeeper any pinger or Valakut Exploration wins | Gearhulk and Reckless Handling (Zuran Orb), Gearhulk and Recruiter (Safekeeper), Chord, Recruiter (General) | 3 cards: no floor |
| E | Toph + Springheart Nantuko + Lotus Cobra or Tireless Provisioner | step 13 | Infinite landfall (Spellbook tag S): lethal with any pinger | Recruiter, Chord, Seismic Sense, Speaker, GSZ | 3 cards with the commander: no floor |
| D | Toph + The Stasis Coffin | base | Protection from everything on every opponent's turn for {2} | - | review note only |

Rules notes: Bumi must deal combat damage in the first combat (no summoning sickness); Coating lasts until end of turn.
Ashaya's creatures are still summoning sick for {T} abilities. Chord of Calling can be convoked by earthbended land
creatures. Gamble discards a card at random after the search: cast it with a full hand or as the last card.
Gearhulk puts the two cards into the hand, not onto the battlefield.

## Roles
| Role | Base (step 0) | End (step 34, 195,007 CLP) |
|---|---|---|
| Lands | 35: 29 basics, 6 nonbasic (Command Tower, Rootbound Crag, Sunpetal Grove, Ba Sing Se, Rumble Arena, Rogue's Passage) | 35: 17 basics, 18 nonbasic: the six, 10 bought duals or filter lands (Game Trail, Fortified Village, Rugged Prairie, Furycalm Snarl, Clifftop Retreat, Canopy Vista, Cinder Glade, Battlefield Forge, Razorverge Thicket, Temple Garden), Exotic Orchard, Inventors' Fair |
| Tutors | 2: Seismic Sense, Crop Rotation | 10: Seismic Sense, Crop Rotation, Reckless Handling, Brightglass Gearhulk, Chord of Calling, Imperial Recruiter, Inventors' Fair, Gamble, Formidable Speaker, Green Sun's Zenith |
| Ramp and speed | 18 (Sol Ring, Arcane Signet, 3 more rocks, Barrels, Bauble, Heaped Harvest, Solemn, Raucous Audience, Great Divide Guide, Wrenn, 6 land spells) | 19: Sol Ring, Arcane Signet, Everflowing Chalice, Talisman of Impulse, Selesnya Signet, Boros Locket, Bender's Waterskin, Chromatic Lantern, Wayfarer's Bauble, Heaped Harvest, Sakura-Tribe Elder, Lotus Cobra, Tireless Provisioner, Great Divide Guide, Wrenn, Rampant Growth, Harrow, Cycle of Renewal, Earthbender Ascension |
| Combo pieces | Ashaya, Bumi Unleashed, Zuran Orb, Blind Bandit, Earth Kingdom General, Bumi Eclectic, Haru | Ashaya, Bumi, Zuran Orb, Goblin Bombardment, Sylvan Safekeeper, Coating, Torque, Blind Bandit, Earth Kingdom General, Haru, Springheart Nantuko, Lotus Cobra, Provisioner |
| Card advantage and payoffs | Terrasymbiosis, Tracker, Bitter Work, Tannuk, Valakut Exploration, Awakening, 5 cantrip artifacts, True Ancestry, Wrenn | Terrasymbiosis, Tracker, Tannuk, Valakut Exploration, Nutrient Block, Soul-Guide Lantern, Wrenn; pingers Sabotender, Arbaaz, Ragost |
| Interaction | 13 + Planar Outburst | 10 + Planar Outburst: Swords, Path, Beast Within, Fateful Absence, Stroke of Midnight, Rocky Rebuke, Hunter's Bow, Hardlight Containment, Inscription, Annie; Soul-Guide Lantern (graveyard) |
| Protection | Redirect Lightning, The Stasis Coffin, Haystack | Redirect Lightning, The Stasis Coffin, Kutzil, Sylvan Safekeeper |
| Average mana value (nonland) | 2.53 | 2.31 |

Curve (nonland cards by mana value):
| MV | 0 | 1 | 2 | 3 | 4 | 5 | 6+ |
|---|---|---|---|---|---|---|---|
| Base | 1 | 13 | 21 | 17 | 5 | 6 | 1 |
| Step 11 (24,152) | 2 | 12 | 25 | 18 | 4 | 3 | 0 |
| End | 2 | 14 | 20 | 21 | 4 | 3 | 0 |

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Liquimetal Coating | 490 | Liquimetal Torque (2,830; move step 24 up) |
| 2 | Reckless Handling | 630 | Inventors' Fair (14,280; move up) |
| 3 | Everflowing Chalice | 500 | Mind Stone (650) |
| 4 | Talisman of Impulse | 742 | Gruul Signet (700) |
| 5 | Sakura-Tribe Elder | 890 | Wood Elves (300) |
| 6 | Chromatic Lantern | 600 | Prismatic Omen (4,200) |
| 7 | Fateful Absence | 490 | Generous Gift (1,560) |
| 8 | Goblin Bombardment | 4,200 | move Sylvan Safekeeper (10,000) up |
| 9 | Brightglass Gearhulk | 6,920 | Imperial Recruiter (14,700; move up) |
| 10 | Chord of Calling | 8,100 | Formidable Speaker (23,320; move up) |
| 11 | Soul-Guide Lantern | 590 | Scavenging Ooze (490) |
| 12 | Lotus Cobra | 7,800 | Birds of Paradise (7,500); line E then runs on Provisioner |
| 13 | Springheart Nantuko | 10,400 | Scute Swarm (10,600; a threat, not a combo) |
| 14 | Tireless Provisioner | 3,400 | Nissa, Worldsoul Speaker (490) |
| 15 | Stroke of Midnight | 300 | Generous Gift (1,560) |
| 16 | Game Trail | 500 | Cinder Glade (790) |
| 17 | Fortified Village | 500 | Canopy Vista (590) |
| 18 | Rugged Prairie | 500 | Battlefield Forge (590) |
| 19 | Furycalm Snarl | 590 | Sundown Pass (4,280) |
| 20 | Exotic Orchard | 500 | keep the Forest |
| 21 | Clifftop Retreat | 500 | Sundown Pass (4,280) |
| 22 | Imperial Recruiter | 14,700 | Formidable Speaker (23,320) |
| 23 | Sylvan Safekeeper | 10,000 (1 store) | Lightning Greaves (6,490); Bombardment and the Orb remain outlets |
| 24 | Liquimetal Torque | 2,830 | keep Shared Roots |
| 25 | Kutzil, Malamet Exemplar | 3,700 (1 store) | Lightning Greaves (6,490) |
| 26 | Inventors' Fair | 14,280 | Tezzeret, Cruel Captain (29,990) or keep the Forest |
| 27 | Canopy Vista | 590 | Overgrown Farmland (1,820) |
| 28 | Cinder Glade | 790 | Rockfall Vale (1,190) |
| 29 | Battlefield Forge | 590 | Sundown Pass (4,280) |
| 30 | Razorverge Thicket | 915 | Brushland (2,520) |
| 31 | Gamble | 28,050 | Enlightened Tutor (38,480) |
| 32 | Formidable Speaker | 23,320 | Green Sun's Zenith (move step 33 up) |
| 33 | Green Sun's Zenith | 38,200 | Enlightened Tutor (38,480) |
| 34 | Temple Garden | 7,900 | Bountiful Promenade (9,500) |

## The three swaps that matter most
| Swap | CLP | Why |
|---|---|---|
| Reckless Handling (step 2) | 630 | The first tutor for the combo pieces: round 2's cap jumped to -1.18 when the Coating line came with no tutor |
| Chord of Calling (step 10) | 8,100 | Instant tutor that reaches a piece of every line (Ashaya, Bumi, loopers, later Nantuko and Cobra) |
| Springheart Nantuko (step 13) | 10,400 | The fastest win line (two 2-mana pieces with Toph): the answer to "too slow for its pieces" |

## Owned cards another deck may also want
Unchanged from round 2 (the base is the same list).
| Card | Copies owned | Also in | Substitute here (CLP) |
|---|---|---|---|
| Sol Ring | 2 | Azula, Alexios | buy a third (1,900) |
| Arcane Signet | 2 | Azula, Alexios | buy a third (890) |
| Rogue's Passage | 2 | Azula, Alexios | buy a third (742) |
| Command Tower | 2 | Azula | one copy left for Toph |
| Redirect Lightning | 2 | Azula | one copy left for Toph |
| Bender's Waterskin | 3 | Azula, Alexios | the third copy is Toph's |
| Barrels of Blasting Jelly | 3 | Alexios | enough copies (base only here) |

Third copies of Sol Ring, Arcane Signet and Rogue's Passage cost 3,532 CLP in total, outside this ladder's numbers.

## What the owner's list and the top lists do that this one does not
Owner's list (6.5): tapped lands, 5-7 mana cards (Omnath, Titania Nature's Force, Meteor Sword), Mindslaver, one win line
and no tutor beyond Crop Rotation. Measured top lists (7.2-7.4): the same engine plus shocks, fetches, Yavimaya and
expensive earthbend payoffs; this ladder spends on tutors and speed instead, the two caps Salt measured on Toph.

## Wishlist (not in the pool, so not priced)
Cheaper or faster ways to fill the two caps; each would replace a costly purchase late in the ladder.
| Card | Role | Would replace | Why |
|---|---|---|---|
| Eladamri's Call | tutor | Formidable Speaker (23,320) | 2-mana instant tutor for any creature |
| Worldly Tutor | tutor (Game Changer) | Gamble (28,050) | 1-mana creature tutor; no random discard |
| Summoner's Pact | tutor | Green Sun's Zenith (38,200) | Free green creature tutor on the combo turn |
| Finale of Devastation | tutor | Green Sun's Zenith (38,200) | Any creature to the battlefield |
| Natural Order | tutor (Game Changer) | Gamble (28,050) | Sacrifice a land creature to put Ashaya onto the battlefield |
| Survival of the Fittest | tutor (Game Changer) | Imperial Recruiter (14,700) | Repeatable creature tutor for every line |
| Llanowar Elves | speed | Selesnya Signet | 1-mana ramp |
| Elvish Mystic | speed | Boros Locket | 1-mana ramp |
| Fyndhorn Elves | speed | Earthbender Ascension | 1-mana ramp |
| Arbor Elf | speed | Rampant Growth | 1-mana ramp that untaps a Forest |
| Elvish Spirit Guide | speed | Harrow | Free green mana on the combo turn |
| Talisman of Unity | speed | Boros Locket | 2-mana G/W rock |
| Talisman of Conviction | speed | Selesnya Signet | 2-mana R/W rock |
| Ashnod's Altar | combo outlet, mana | Zuran Orb | Loop C makes infinite colorless mana; free outlet |
