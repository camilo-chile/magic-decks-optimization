# Toph, the First Metalbender: purchase ladder (Phase 8 step 2, round 2, 2026-10-18)

Ladder: `decks/proposals/toph-the-first-metalbender.ladder.txt` (base + 36 swaps). Checked with
`python -I -X utf8 scripts/ladder.py decks/proposals/toph-the-first-metalbender.ladder.txt`: all 37 steps valid
(100 cards, no reversible cards, Layer A floor 3 at target 3, 1 Game Changer (Crop Rotation, owned), 0 extra-turn
cards, every purchase with stock > 0). Layer A notes, all review-only: Bumi + Ashaya (two-card, 10 mana, floor 3),
Toph + The Stasis Coffin (lock note, floor 1), hub Toph Hardheaded Teacher, Springheart Nantuko template variants.
Prices: `merged-20261017T2337Z.json` with loose title matches rejected (a hint; stock is verified in Phase 9).
Round 1 is kept read-only in `decks/proposals/round1/`.

## Round 2
What changed and why:
- **Manabase first** (the Azula measurements: nine cheap untapped duals moved a list from 5.5 to 6.9 on Commander
  Salt; the owner's Toph list, with 8 tapped lands, has Manabase Quality 10). The free base now holds no land that
  enters tapped: fetches, Bridges, tapped duals and Jungle Shrine left for basics, and Secret Tunnel (colorless)
  for a Forest. The first ten purchases are Liquimetal Coating and the nine cheap untapped duals (10,590 CLP);
  three shocks follow at 50,000-90,000.
- **No card is mandatory.** Mindslaver (6 + 4 mana, a lock Salt scores 0 as a win) and Seismic Tutelage left;
  Ragost, Deft Gastronaut (owned: every artifact becomes a Food it sacrifices for 3 damage to each opponent) and
  Awakening of Vitu-Ghazi (owned: instant 9/9 that draws 9 with Terrasymbiosis) entered. The other formerly locked
  cards stayed on merit.
- **Tutors for the combos** (Salt caps win lines with no tutor): Reckless Handling moved to step 16 and Brightglass
  Gearhulk (finds Zuran Orb and Sylvan Safekeeper or Sol Ring) was added at step 28.
- **Extended to 146,240 CLP** because real power is still there: Kutzil (protects the combo turn), Springheart
  Nantuko (two more three-card lines with Toph), Scute Swarm, Sylvan Safekeeper, Heroic Intervention, Toph Greatest
  Earthbender, three shocks. It stops there: fetches, Yavimaya, battlebond lands and the Game Changers (Field of the
  Dead, Enlightened Tutor, The One Ring) add little that the list does not already do for 9,000-124,000 each.
- No reversible card was in round 1; round-1 prices are unchanged.

| List | Left | Entered |
|---|---|---|
| Base (0 CLP) | Mindslaver, Seismic Tutelage, Secret Tunnel, Jungle Shrine, Cabaretti Courtyard, Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape, Kyoshi Village, Omashu City, Sun-Blessed Peak, 3 Bridges | Ragost, Awakening of Vitu-Ghazi, 8 Forest, 3 Mountain, 1 Plains |
| Final (round 1 at 40,080 vs round 2 at 146,240) | the same lands and Mindslaver, Seismic Tutelage, plus Fabled Passage, Bitter Work, The Earth King, Earthbender Ascension, Haystack, Collective Resistance, Trapped in the Screen | Ragost, Kutzil, Brightglass Gearhulk, Springheart Nantuko, Scute Swarm, Sylvan Safekeeper, Heroic Intervention, Toph Greatest Earthbender, Temple Garden, Stomping Ground, Sacred Foundry, 2 Forest, 2 Mountain, 1 Plains |

Checkpoints and expected Commander Salt power (judgment, not a measurement; reasoning below):
| Cap CLP | Step | Cost CLP | Stores | Expected power |
|---|---|---|---|---|
| 0 | 0 (base) | 0 | none | 7.0 (6.8-7.3) |
| (10,000) | 9 (10 at 10,590: all nine duals) | 8,070 | cardnexus, gameofmagic, magic4ever, oasis | 7.5 (7.2-7.8) |
| 25,000 | 22 | 24,610 | + paytowin | 7.8 (7.5-8.0) |
| 50,000 | 28 | 49,110 | same 5 | 7.9 (7.6-8.1) |
| 75,000 | 30 | 66,100 | same 5 | 8.0 (7.7-8.2) |
| 100,000 | 33 | 98,900 | same 5 | 8.0 (7.7-8.3) |
| 150,000 | 36 (end) | 146,240 | + lacomarca (Heroic Intervention) | 8.1 (7.8-8.4) |

Consolidation: gameofmagic sells Karplusan Forest and Brightglass Gearhulk; oasis sells Overgrown Farmland, Reckless
Handling and Liquimetal Torque (at cardnexus 2,390 and 690 and at paytowin 3,200: +1,000 CLP drops oasis); lacomarca
only Heroic Intervention (16,000 at afkstore, 17,990 at cardnexus). All six stores are in the Azula plan already.
The 75,000 checkpoint stops at 66,100 because every next purchase costs about 10,000.

## Strategy and engine
Metal landfall with several combo finishes. Toph makes every nontoken artifact a land, so each rock, bauble or
equipment that enters is a landfall trigger and, with a lands-tap engine, also a mana source. Landfall pingers turn
the cheap artifacts into damage, earthbend counters turn into cards, and infinite lines that Layer A allows close the
game. Every purchase adds mana quality, redundancy or a better payoff to the same plan.

Engine core (must be together):
| Piece | Cards | Why it cannot be split |
|---|---|---|
| Artifacts as lands | Toph; 16-19 artifacts (Sol Ring, Arcane Signet, Bender's Waterskin, Wayfarer's Bauble, Heaped Harvest, Zuran Orb, Hunter's Bow, The Stasis Coffin, Solemn; bought: Coating, Torque, Lantern, Soul-Guide Lantern, All-Fates Scroll, Survey Mechan, Brightglass Gearhulk) | Each artifact is an extra land drop: the fuel of every payoff |
| Lands tap for any color | Great Divide Guide, Wrenn and Realmbreaker, Chromatic Lantern (step 11) | With them every artifact is also a rock |
| Landfall and artifact payoffs | Tannuk, Sabotender, Arbaaz Mir, Ragost, Valakut Exploration; bought: Koth, Spitfire Lagac, Felidar Retreat, Tireless Provisioner, Evolution Sage, Avenger, Lotus Cobra, Springheart Nantuko, Scute Swarm | With Annie Joins Up the legendary Tannuk, Arbaaz and Koth trigger twice: one cheap artifact deals up to 8 to each opponent |
| Earthbend counters to cards | Toph's end-step earthbend 2, Terrasymbiosis, Hardened Scales, Toph Hardheaded Teacher, Haru, Awakening; Toph Greatest Earthbender (step 36) gives land creatures double strike | Terrasymbiosis draws 2-3 each turn from Toph alone; Annie doubles Toph's earthbend |
| Win lines, tutors and protection | Ashaya, Bumi Unleashed, Zuran Orb, 3 earthbend-on-enter creatures, Seismic Sense, Crop Rotation; bought: Coating (step 1), Reckless Handling (16), Kutzil (21), Brightglass Gearhulk (28), Sylvan Safekeeper (34), Heroic Intervention (35) | The owner's list had one win line (redundancy 0.60); the end has 11 winning Spellbook lines, 4 tutors and protection for the combo turn |

Combo lines (Spellbook variants in the local bulk: 5 on the base, 6 at step 22, 7 at step 28, 13 at step 33, 16 at the end; the owner's list has 3):
| Line | Cards | From | Result | Layer A |
|---|---|---|---|---|
| A | Toph + Bumi, Unleashed + Liquimetal Coating (Liquimetal Torque from step 23) | step 1 | Coating makes Bumi an artifact, so a land; each time he connects all lands (Bumi included) untap and he attacks again in the extra combat, where only land creatures may. Rogue's Passage untaps every combat, so he is unblockable each time. Infinite combats | 3 cards with the commander: no floor |
| B | Ashaya + Bumi, Unleashed | base | Ashaya makes every nontoken creature a land: infinite combats with the whole team | two-card, 10 mana: floor 3 (late) |
| C | Ashaya + Zuran Orb (or Sylvan Safekeeper from step 34) + Toph the Blind Bandit, Earth Kingdom General or Bumi Eclectic Earthbender | base | The creature is a land, earthbends itself as it enters, is sacrificed and returns: infinite enters, landfall and deaths. Lethal with any pinger or Valakut Exploration; infinite tokens, Treasures or mana with Felidar, Provisioner, Avenger, Cobra, Scute Swarm | 3 cards: no floor |
| C' | Ashaya + Zuran Orb + Haru + any other Ally | base | Same loop through Haru's earthbend 1 (derived from oracle text; not in Spellbook) | 4 cards: no floor |
| E | Toph + Springheart Nantuko + Lotus Cobra or Tireless Provisioner | step 31 | Infinite landfall (Spellbook tag S) | 3 cards with the commander: no floor |
| D | Toph + The Stasis Coffin | base | Earthbend the Coffin at end step, exile it for {2}: protection from everything on every opponent's turn | review note only |

Rules notes: Bumi must deal combat damage in the first combat (no summoning sickness); Coating's effect lasts until
end of turn. Ashaya's creatures are still summoning sick for {T} abilities. Pay Rogue's Passage in each
beginning-of-combat step from the lands Bumi untapped. The Zuran Orb and Safekeeper sacrifices are optional, so
loop C stops at will. Planar Outburst is one-sided here (earthbended lands are lands; with Ashaya all our nontoken
creatures are). Ragost's damage is an activated ability, so Annie does not double it.

## Roles
| Role | Base (step 0) | Final (step 36, 146,240 CLP) |
|---|---|---|
| Lands | 35: 29 basics (16 Forest, 7 Mountain, 6 Plains), 6 nonbasic (Command Tower, Rootbound Crag, Sunpetal Grove, Ba Sing Se, Rumble Arena, Rogue's Passage); none enters tapped unconditionally | 35: 17 basics (8 Forest, 5 Mountain, 4 Plains), 18 nonbasic: 12 untapped duals (3 shocks, 3 painlands, 6 check, slow or typed duals), Command Tower, Exotic Orchard, Ba Sing Se, Rumble Arena, Rogue's Passage |
| Ramp | 18: Sol Ring, Arcane Signet, Selesnya Signet, Boros Locket, Bender's Waterskin, Barrels, Wayfarer's Bauble, Heaped Harvest, Solemn, Raucous Audience, Great Divide Guide, Wrenn, Rampant Growth, Shared Roots, Harrow, Cycle of Renewal, Roiling Regrowth, Earthbender Ascension | 16: Sol Ring, Arcane Signet, All-Fates Scroll, Bender's Waterskin, Chromatic Lantern, Liquimetal Torque, Wayfarer's Bauble, Heaped Harvest, Solemn, Lotus Cobra, Tireless Provisioner, Great Divide Guide, Wrenn, Rampant Growth, Harrow, Cycle of Renewal |
| Card advantage | 13 + 2 tutors: Terrasymbiosis, Tireless Tracker, Bitter Work, Tannuk, Valakut Exploration, Awakening of Vitu-Ghazi, Chromatic Star, Ichor Wellspring, Nutrient Block, Elsewhere Flask, Mycosynth Wellspring, True Ancestry, Wrenn; Seismic Sense, Crop Rotation | 11 + 4 tutors: Terrasymbiosis, Tireless Tracker, Tannuk, Valakut Exploration, Kutzil, Soul-Guide Lantern, All-Fates Scroll, Survey Mechan, Inspiring Call, Evolution Sage (feeds Terrasymbiosis), Wrenn; Seismic Sense, Crop Rotation, Reckless Handling, Brightglass Gearhulk |
| Interaction | 13 + 1 wipe: Swords, Path, Beast Within, Trapped in the Screen, Rocky Rebuke, Master's Rebuke, Hunter's Bow, Hardlight Containment, Inscription of Abundance, Haywire Mite, Origin of Metalbending, Collective Resistance, Annie Joins Up; Planar Outburst | 10 + 1 wipe + graveyard hate: Swords, Path, Beast Within, Stroke of Midnight, Generous Gift, Rocky Rebuke, Hunter's Bow, Hardlight Containment, Inscription, Annie; Planar Outburst; Soul-Guide Lantern |
| Protection | 3: Redirect Lightning, The Stasis Coffin, Haystack | 6: Redirect Lightning, The Stasis Coffin, Inspiring Call, Kutzil, Sylvan Safekeeper, Heroic Intervention |
| Win conditions | 4 Spellbook lines (B, C x3) plus C'; pingers Tannuk, Sabotender, Arbaaz, Ragost, Valakut Exploration; Moraug, Titania, Awakening | 11 winning Spellbook lines (A x2, B, C x6, E x2) plus C'; pingers Tannuk, Sabotender, Arbaaz, Koth, Spitfire Lagac, Ragost, Valakut Exploration; Avenger, Scute Swarm, Felidar, Toph Greatest Earthbender |
| Average mana value (nonland) | 2.53 | 2.69 |

Curve (nonland cards by mana value):
| MV | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|---|
| Base | 1 | 13 | 21 | 17 | 5 | 6 | 1 | 0 |
| Step 22 (24,610) | 1 | 10 | 15 | 23 | 8 | 6 | 1 | 0 |
| Final | 1 | 11 | 16 | 22 | 9 | 4 | 0 | 1 |
| Owner's list (6.5, avg 3.37) | 0 | 11 | 10 | 15 | 11 | 9 | 4 | 3 |

## What was dropped or replaced, and why
Owner's current list (6.5, average mana value 3.37, 1 rock, 8 tapped lands, Manabase Quality 10):
| Dropped | Why |
|---|---|
| Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape, Cabaretti Courtyard, Jungle Shrine, 3 Bridges, Urza's Cave, Darksteel Citadel | Tapped or colorless lands: the measured cause of the low manabase score |
| Mindslaver | 6 + 4 mana; Salt scores the Toph loop 0 as a win; the saltiest play pattern for a casual pod |
| Deflecting Swat | Its only copy is in the Azula ladder; Redirect Lightning stays |
| Banefire, Blasphemous Act, Hour of Revelation | Red or WWW cards the other decks want more; Planar Outburst is one-sided here and the pingers replace X burn |
| Omnath Locus of Rage, Titania Nature's Force, Meteor Sword, Karn's Sylex, Elemental Teachings | 5-7 mana; the list's curve (3.37) was its efficiency problem |
| Aang Air Nomad, Appa, Avatar Destiny, The Boulder, The Cave of Two Lovers, Blossoming Tortoise, Druid Class, Stocking the Pantry, Horrid Vigor, Rockalanche, Airbender's Reversal, Sandbenders' Storm, Seismic Tutelage | Low card quality or off-plan; replaced by Sol Ring, Arcane Signet, 4 rocks, Zuran Orb (3 new Spellbook lines), Ragost, Seismic Sense, Sabotender, Valakut Exploration, Great Divide Guide and cheap removal |

Measured top lists (7.2-7.4, 206,000-1,330,000 CLP) share this engine (Bumi + Liquimetal, Zuran Orb, Lantern, Cobra,
Provisioner, Safekeeper, Nantuko, pingers, Annie, Great Divide Guide). Left out:
| Dropped | Price CLP | Why it is luxury here |
|---|---|---|
| Fetches, Yavimaya, Jetmir's Garden (tapped), battlebond lands, Lotus Field (tapped), Urborg, Taiga, Plateau | 2,980-329,000 | Twelve untapped duals already cover every color pair; Lantern, Guide and Wrenn make every artifact tap for any color, Yavimaya's job here |
| Toph Earthbending Master, Avatar Kyoshi, Earthbending Student, Badgermole Cub, Mossborn Hydra, The Ozolith, Ouroboroid, The Earth Crystal | 15,000-78,000 | Earthbend payoffs the owned Bumis, Blind Bandit and Hardened Scales cover; Toph Greatest Earthbender is the one bought |
| Field of the Dead, Enlightened Tutor, Gamble, The One Ring, Ancient Tomb (Game Changers) | 27,990-124,000 | One GC slot is used (Crop Rotation); each is a large share of a checkpoint for an effect Felidar, Scute or the four tutors already give |
| Dryad, Birds, Prismatic Omen, Three Visits, Nature's Lore, Urza's Bauble, Tormod's Crypt | 1,560-9,880 | Ramp and artifact variants; Lantern, Cobra and Provisioner do the job |
| Boros Charm, Lightning Greaves, Earthshape | 5,700-8,720 | Protection already 6 deep |
| Mycosynth Lattice; bounce lands for the Teacher loop | - | Not luxury: Lattice is mass land denial with Vandalblast; the Teacher loop needs a bounce land and a 0-mana artifact, both kept out |

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Liquimetal Coating | 490 | Liquimetal Torque (2,830; move step 23 up) |
| 2 | Exotic Orchard | 500 | Spire Garden (9,090) or keep the Forest |
| 3 | Clifftop Retreat | 500 | Sacred Foundry (11,800; move up) or Sunbillow Verge (10,000) |
| 4 | Canopy Vista | 590 | Bountiful Promenade (9,500) |
| 5 | Battlefield Forge | 590 | Spectator Seating (16,490) or keep the Mountain |
| 6 | Cinder Glade | 790 | Thornspire Verge (6,200) |
| 7 | Rockfall Vale | 1,190 | Spire Garden (9,090) |
| 8 | Karplusan Forest | 1,600 (gameofmagic; lacomarca 2,100) | Stomping Ground (9,090; move up) |
| 9 | Overgrown Farmland | 1,820 | Hushwood Verge (9,900) |
| 10 | Brushland | 2,520 | Temple Garden (7,900; move up) |
| 11 | Chromatic Lantern | 600 | Prismatic Omen (4,200; artifacts become every basic land type) |
| 12 | Koth, the Geomancer | 300 (1 store) | Rampaging Baloths (690) |
| 13 | Spitfire Lagac | 200 | Weather Maker (500; landfall counters become 3 damage) |
| 14 | Soul-Guide Lantern | 590 | Tormod's Crypt (1,560) |
| 15 | Stroke of Midnight | 300 | Chaos Warp (790, a third copy) |
| 16 | Reckless Handling | 630 | Expedition Map (1,400; finds Rogue's Passage or a dual) |
| 17 | Felidar Retreat | 2,090 | Rampaging Baloths (690) |
| 18 | Survey Mechan | 300 | keep Ichor Wellspring (owned) |
| 19 | All-Fates Scroll | 350 | Weather Maker (500) |
| 20 | Tireless Provisioner | 3,400 | Nissa, Worldsoul Speaker (490) |
| 21 | Kutzil, Malamet Exemplar | 3,700 (1 store) | Lightning Greaves (6,490) |
| 22 | Generous Gift | 1,560 | Wild Magic Surge (1,440) |
| 23 | Liquimetal Torque | 2,830 | Brightglass Gearhulk (6,920; move up) |
| 24 | Evolution Sage | 3,300 (1 store) | Loading Zone (2,400) |
| 25 | Avenger of Zendikar | 2,760 | keep Moraug (owned) |
| 26 | Inspiring Call | 890 | Harmonize (300) |
| 27 | Lotus Cobra | 7,800 | Birds of Paradise (7,500) |
| 28 | Brightglass Gearhulk | 6,920 | Imperial Recruiter (14,700; finds Blind Bandit, Haru, Safekeeper, Cobra) |
| 29 | Temple Garden | 7,900 | Bountiful Promenade (9,500) |
| 30 | Stomping Ground | 9,090 | Spire Garden (9,090) |
| 31 | Springheart Nantuko | 10,400 | move Scute Swarm up; keep Bitter Work |
| 32 | Sacred Foundry | 11,800 | Sunbillow Verge (10,000) |
| 33 | Scute Swarm | 10,600 | Rampaging Baloths (690) |
| 34 | Sylvan Safekeeper | 10,000 (1 store) | Lightning Greaves (6,490) |
| 35 | Heroic Intervention | 15,350 | Boros Charm (5,700) |
| 36 | Toph, Greatest Earthbender | 21,990 (1 store) | The Earth Crystal (15,000) |

## The three swaps that matter most
| Swap | CLP | What the deck loses without it |
|---|---|---|
| The nine cheap untapped duals (steps 2-10) | 10,100 | The largest measured lever on Commander Salt (Azula: +1.4 for 7,155 CLP of duals); without them the base's manabase is 29 basics and 3 duals |
| Liquimetal Coating (step 1) | 490 | The cheapest win line: Toph + Bumi + Coating is 7 mana over two turns with no Ashaya; without it every infinite before step 31 needs the 5-mana Ashaya |
| Chromatic Lantern (step 11) | 600 | Every artifact becomes a mana source of any color: ramp and fixing for a deck that runs 16-19 artifacts |

## Owned cards another deck may also want
Checked against the current `fire-lord-azula.ladder.txt` and `alexios-deimos-of-kosmos.ladder.txt`.
| Card | Copies owned | Also in | Substitute here (CLP) |
|---|---|---|---|
| Sol Ring | 2 | Azula, Alexios | buy a third (1,900) |
| Arcane Signet | 2 | Azula, Alexios | buy a third (890) or Fellwar Stone (1,490) |
| Rogue's Passage | 2 | Azula, Alexios | buy a third (742); or Secret Tunnel (owned, 3 copies; colorless land) |
| Command Tower | 2 | Azula | one copy left for Toph |
| Redirect Lightning | 2 | Azula | one copy left for Toph; else Angelic Intervention (owned) |
| Bender's Waterskin | 3 | Azula, Alexios | the third copy is Toph's |
| Barrels of Blasting Jelly | 3 | Alexios | enough copies (base only here) |
| Avoided on purpose (only copy elsewhere) | | | Mind Stone, Commander's Sphere, Mishra's Bauble, Abstergo Entertainment, Reckless Fireweaver, Deflecting Swat; Chaos Warp and Swiftfoot Boots (both copies elsewhere) |

Third copies of Sol Ring, Arcane Signet and Rogue's Passage cost 3,532 CLP in total, outside this ladder's numbers.
The base no longer uses Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape or Secret Tunnel.

## Expected Commander Salt power (judgment, not a measurement)
Anchors: the owner's list 6.5 with Manabase Quality 10; the measured top Toph lists 7.2-7.4; Azula (same method):
base +0.9 over the owner's list, +1.2 for the first ~25,000 CLP, 7.4 at 148,760 (judged 6.6-7.1), and the controlled
test (+1.4 for nine cheap duals, Manabase Quality 32% to 70%).
| Point | Expected | Reasoning |
|---|---|---|
| Base | 7.0 (6.8-7.3) | Same core as the 6.5 list with average mana value 2.53 instead of 3.37, Sol Ring and 5 rocks instead of 1, 4 winning Spellbook lines instead of 1, 13 interaction pieces, and no tapped land (the owner's list had 8). The manabase is still mostly basics, so the score stays well under its ceiling |
| 10,590 (step 10) | 7.5 (7.2-7.8) | The nine duals: the Azula test says this alone is worth about a point when the manabase starts low; Toph starts higher on the other pillars, so less is left to gain |
| 24,610 (step 22) | 7.8 (7.5-8.0) | Coating line, Lantern, four pingers, Felidar, Provisioner, Kutzil, graveyard hate, a tutor, two removal spells |
| 49,110 (step 28) | 7.9 (7.6-8.1) | Torque, Sage, Avenger, Lotus Cobra, a second tutor |
| 66,100 (step 30) | 8.0 (7.7-8.2) | Two shocks |
| 98,900 (step 33) | 8.0 (7.7-8.3) | Nantuko lines, the third shock, Scute Swarm |
| 146,240 (step 36) | 8.1 (7.8-8.4) | Safekeeper, Heroic Intervention, Toph Greatest Earthbender: the smallest gain per CLP |

Watch Commander Salt's bracket mark: near 8 power it may show "3*" or suggest 4 even though Layer A stays at floor 3
on every step. The most uncertain points: how far the base's basics-only manabase scores, and whether anything after
step 28 adds more than +0.2 (measuring steps 0, 10, 22 and 28 would settle the front of the curve).

## Formerly locked cards
The lock list is empty, so every card was judged on merit. Kept: Ashaya, Bumi Unleashed, Annie Joins Up,
Terrasymbiosis, Arbaaz Mir, Wrenn and Realmbreaker, Heaped Harvest, Inscription of Abundance, The Stasis Coffin,
Redirect Lightning, Rogue's Passage, Bender's Waterskin (all steps); The Earth King (until step 33). Left out:
Mindslaver, Seismic Tutelage, Secret Tunnel, Deflecting Swat, Swiftfoot Boots, Hidden Footblade, Labyrinth Adversary,
Combustion Man, Electro, Horizon Stone.

## Wishlist (not in the pool, so not priced; do not build on them)
Starred: the 12 whose price matters most. Eight are cheap untapped duals in Toph's colors (the measured biggest
lever; each would replace a basic early, or a 9,000-11,800 shock late), four are cheap tutors, engines or protection.
Pathways are left out: they are modal double-faced (reversible).
| Card | Role | Would replace | Why |
|---|---|---|---|
| Inspiring Vantage * | land | a Mountain early, or Sacred Foundry (11,800) | R/W fastland: untapped in the first turns |
| Copperline Gorge * | land | a Forest early, or Stomping Ground (9,090) | R/G fastland |
| Razorverge Thicket * | land | a Forest early, or Temple Garden (7,900) | G/W fastland |
| Furycalm Snarl * | land | a Mountain | R/W dual, untapped with a Mountain or Plains in hand |
| Game Trail * | land | a Forest | R/G dual, untapped with a Mountain or Forest in hand |
| Fortified Village * | land | a Forest | G/W dual, untapped with a Forest or Plains in hand |
| Sundown Pass * | land | a Plains | R/W slow land; R/W is the thinnest color pair |
| Rugged Prairie * | land | a Plains | R/W filter land |
| Wooded Bastion | land | a Forest | G/W filter land |
| Goblin Bombardment * | combo outlet and win | Survey Mechan | Ashaya + Bombardment + Blind Bandit is lethal by itself (each sacrifice pings 1) |
| Ashnod's Altar | combo outlet, mana | Harrow | Loop C then makes infinite colorless mana |
| Skullclamp * | card advantage | Rocky Rebuke | Earthbend-1 lands (Haru, Teacher), Plants, Insects and Cats die to draw 2 |
| Green Sun's Zenith * | tutor | Reckless Handling | Finds Ashaya, Bumi, a looper or a pinger; no random discard |
| Chord of Calling | tutor | Crop Rotation | Instant creature tutor convoked by land creatures; frees the only Game Changer |
| Eternal Witness | recursion | True Ancestry (base) | Returns a combo piece on a body |
| Sakura-Tribe Elder | ramp | Rampant Growth | Blocks, then a basic onto the battlefield (landfall) |
| Wood Elves | ramp | Raucous Audience (base) | Untapped Forest (a shock or Canopy Vista) and a body |
| Talisman of Impulse | ramp | Boros Locket (base) | Untapped 2-mana R/G rock |
| Everflowing Chalice | ramp, landfall | Wayfarer's Bauble | 0-mana landfall trigger or a 2-mana rock |
| Mox Amber | ramp, landfall | Chromatic Star (base) | 0-mana artifact that taps for Toph's colors |
| Nature's Claim | interaction | Hardlight Containment | 1-mana artifact or enchantment answer |
| Fateful Absence | interaction | Rocky Rebuke | 2-mana instant creature or planeswalker removal |
| Get Lost | interaction | Inscription of Abundance | 2-mana removal that also hits enchantments and planeswalkers |
| Skyclave Apparition | interaction | Hardlight Containment | Removal on a body |
| Tamiyo's Safekeeping | protection | Redirect Lightning | 1-mana hexproof and indestructible for Ashaya or Bumi |
| Flawless Maneuver * | protection | Heroic Intervention (15,350) | Free team indestructible with Toph out; would make step 35 much cheaper |
| Scavenging Ooze | graveyard hate | Soul-Guide Lantern | Repeatable exile on a growing body |
| Gavony Township | land, counters | Rumble Arena | Counters on every creature: Terrasymbiosis draws, land creatures grow |
| Boseiju, Who Endures | land, removal | a Forest | Removal from an untapped land slot |
| Craterhoof Behemoth | finisher | Avenger of Zendikar | One-turn kill with Plants, Cats, Insects and land creatures |
