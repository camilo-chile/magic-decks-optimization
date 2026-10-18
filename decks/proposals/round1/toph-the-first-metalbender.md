# Toph, the First Metalbender: purchase ladder (Phase 8 step 2, 2026-10-18)

Ladder: `decks/proposals/toph-the-first-metalbender.ladder.txt` (base + 27 swaps). Checked with
`python -I -X utf8 scripts/ladder.py decks/proposals/toph-the-first-metalbender.ladder.txt`: all 28 steps valid
(100 cards, Layer A floor 3 at target 3, 1 Game Changer (Crop Rotation, owned), 0 extra-turn cards, every
purchase with stock > 0 in the pool). Layer A notes on every step, all review-only: Bumi + Ashaya (two-card,
late, floor 3), Toph + Mindslaver and Toph + The Stasis Coffin (floor 1, lock/control), hub Toph Hardheaded
Teacher. Prices: `merged-20261017T2337Z.json` (a hint; stock is verified in Phase 9). Power figures below are
judgments, not measurements.

| Checkpoint (cap CLP) | Last step | Cost CLP | Stores |
|---|---|---|---|
| 0 | 0 (base) | 0 | none |
| 10,000 | 15 | 9,750 | cardnexus, magic4ever, paytowin |
| 25,000 | 21 | 24,120 | + oasis |
| 30,000 | 25 | 29,760 | + gameofmagic |
| 40,000 | 26 | 37,560 | 5 stores |
| final | 27 | 40,080 | 5 stores |

Consolidation for the optimizer: oasis sells only Liquimetal Torque, Overgrown Farmland and Reckless
Handling here; at paytowin (3,200) and cardnexus (2,390; 690) they cost +1,000 CLP and drop a store.
Karplusan Forest is the only card that needs gameofmagic (or lacomarca, 2,100); Brushland is 2,590 at
cardnexus. All five stores are already in the Azula plan, so a joint purchase adds no shipping.

Data fault found: the pool prices **Savannah** at 450 CLP (lacomarca, 2 stores), but every offer behind it is
"Savannah Lions" (a `loose` title match in the merged prices). Not used here; fix the matcher before trusting it.

## Strategy and engine
Metal landfall with three combo finishes. Toph makes every nontoken artifact a land, so each rock, bauble
or equipment that enters is a landfall trigger and, with a lands-tap engine, also a mana source. Landfall
pingers turn the cheap artifacts into damage, earthbend counters turn into cards, and three infinite lines
(all allowed by Layer A) close the game. The plan is the same at every step; purchases add redundancy,
untapped mana and better payoffs, never a second strategy.

Engine core (must be together):
| Piece | Cards | Why it cannot be split |
|---|---|---|
| Artifacts as lands | Toph; 17-20 cheap artifacts (Sol Ring, Arcane Signet, Bender's Waterskin, Wayfarer's Bauble, Heaped Harvest, Zuran Orb, Hunter's Bow, The Stasis Coffin, Mindslaver, later Liquimetal Coating/Torque, Soul-Guide Lantern, All-Fates Scroll, Survey Mechan) | Each artifact is an extra land drop: the fuel of every payoff |
| Lands tap for any color | Great Divide Guide, Wrenn and Realmbreaker, Chromatic Lantern (step 2) | Without them a bauble is only a landfall trigger; with them every artifact is also a rock |
| Landfall and artifact payoffs | Tannuk, Sabotender, Arbaaz Mir (artifacts are historic), Valakut Exploration; Koth and Spitfire Lagac (steps 4-5); Felidar Retreat, Tireless Provisioner, Avenger, Evolution Sage, Lotus Cobra later | With Annie Joins Up, the legendary Tannuk, Arbaaz and Koth trigger twice: one cheap artifact deals up to 8 to each opponent |
| Earthbend counters to cards | Toph's end-step earthbend 2, Terrasymbiosis, Hardened Scales, Toph Hardheaded Teacher, Haru, Seismic Tutelage, Bitter Work | Terrasymbiosis draws 2-3 each turn from Toph alone; Annie doubles Toph's earthbend |
| Win lines | Ashaya, Bumi Unleashed, Zuran Orb, Liquimetal Coating (step 1), three earthbend-on-enter creatures, Seismic Sense to find them | Fixes the owner's report: one win line, redundancy 0.60 |

Combo lines (Spellbook variants found in the local bulk: 6 on the base, 8 on the final step; the owner's list has 3):
| Line | Cards | From | Result | Layer A |
|---|---|---|---|---|
| A | Toph + Bumi, Unleashed + Liquimetal Coating (Liquimetal Torque from step 17) | step 1 | Coating makes Bumi an artifact, so a land; each time he connects, all lands (Bumi included) untap and he attacks again in the extra combat, where only land creatures may attack. Rogue's Passage and Secret Tunnel untap every combat too, so he is unblockable each time. Infinite combats | 3 cards with the commander: no floor |
| B | Ashaya + Bumi, Unleashed | base | Ashaya makes every nontoken creature a land: infinite combats with the whole team | two-card, 10 mana: floor 3 (late) |
| C | Ashaya + Zuran Orb + Toph, the Blind Bandit (or Earth Kingdom General, or Bumi, Eclectic Earthbender) | base | The creature is a land, earthbends itself as it enters, is sacrificed to the Orb and returns: infinite enters, landfall, deaths and life. Lethal with any pinger (Tannuk, Sabotender, Koth, Lagac; Arbaaz with the legendary loopers) or with Valakut Exploration; infinite tokens or Treasures with Felidar Retreat, Tireless Provisioner, Avenger, Lotus Cobra | 3 cards: no floor |
| C' | Ashaya + Zuran Orb + Haru + any other Ally (Great Divide Guide, The Earth King, Toph...) | base | Same loop through Haru's earthbend 1 (derived from oracle text; not in Spellbook) | 4 cards: no floor |
| D | Toph + The Stasis Coffin; Toph + Mindslaver | base | Earthbend the artifact at end step, use and sacrifice or exile it, it returns: protection from everything on every opponents' turn for {2}; control of one opponent's next turn each round for {4} | review notes only (floor 1) |

Rules notes: Bumi must deal combat damage in the first combat (no summoning sickness); Coating's effect lasts
until end of turn, so one activation covers every extra combat. Ashaya's creatures are still summoning sick
for {T} abilities. Mana empties between steps: pay Rogue's Passage in each beginning-of-combat step from the
lands Bumi untapped. Zuran Orb is optional, so loop C stops whenever the player wants. Planar Outburst is
one-sided here: earthbended lands are lands, and with Ashaya every nontoken creature of ours is a land. Toph's
single end-step earthbend is shared by the Coffin, Mindslaver and the fetch or sacrifice-to-draw lands;
Annie gives a second one.

## Roles
| Role | Base (step 0) | Final (step 27, 40,080 CLP) |
|---|---|---|
| Lands | 35: 17 basics, 18 nonbasic (11 enter tapped: Jungle Shrine, 3 Bridges, 4 fetches, Kyoshi Village, Omashu City, Sun-Blessed Peak) | 35: 12 basics, 23 nonbasic (6 tapped: Jungle Shrine, 3 Bridges, Cabaretti Courtyard, Evolving Wilds) |
| Ramp | 18: Sol Ring, Arcane Signet, Selesnya Signet, Boros Locket, Bender's Waterskin, Barrels of Blasting Jelly, Wayfarer's Bauble, Heaped Harvest, Solemn, Raucous Audience, Great Divide Guide, Wrenn, Rampant Growth, Shared Roots, Harrow, Cycle of Renewal, Roiling Regrowth, Earthbender Ascension | 17: Sol Ring, Arcane Signet, All-Fates Scroll, Bender's Waterskin, Chromatic Lantern, Liquimetal Torque, Wayfarer's Bauble, Heaped Harvest, Solemn, Lotus Cobra, Tireless Provisioner, Great Divide Guide, Wrenn, Rampant Growth, Harrow, Cycle of Renewal, Earthbender Ascension |
| Card advantage | 12 + 2 tutors: Terrasymbiosis, Tireless Tracker, Bitter Work, Tannuk, Valakut Exploration, Chromatic Star, Ichor Wellspring, Nutrient Block, Elsewhere Flask, Mycosynth Wellspring, True Ancestry, Wrenn (-2); Seismic Sense, Crop Rotation | 11 + 3 tutors: Terrasymbiosis, Tireless Tracker, Bitter Work, Tannuk, Valakut Exploration, Soul-Guide Lantern, All-Fates Scroll, Survey Mechan, Inspiring Call, Evolution Sage (feeds Terrasymbiosis), Wrenn; Seismic Sense, Crop Rotation, Reckless Handling |
| Interaction | 13 + 1 wipe: Swords, Path, Beast Within, Trapped in the Screen, Rocky Rebuke, Master's Rebuke, Hunter's Bow, Hardlight Containment, Inscription of Abundance, Haywire Mite, Origin of Metalbending, Collective Resistance, Annie Joins Up; Planar Outburst | 12 + 1 wipe + graveyard hate: Swords, Path, Beast Within, Trapped in the Screen, Stroke of Midnight, Generous Gift, Rocky Rebuke, Hunter's Bow, Hardlight Containment, Inscription, Collective Resistance, Annie; Planar Outburst; Soul-Guide Lantern |
| Protection | 3: Redirect Lightning, The Stasis Coffin, Haystack (plus modes of Collective Resistance and Origin of Metalbending) | 4: Redirect Lightning, The Stasis Coffin, Haystack, Inspiring Call (plus Collective Resistance) |
| Win conditions | 4 Spellbook infinite lines (B, C x3) plus C', pingers Tannuk, Sabotender, Arbaaz Mir, Valakut Exploration; Moraug, Titania, Seismic Tutelage; Mindslaver lock | 6 Spellbook infinite lines (A x2, B, C x3) plus C', pingers Tannuk, Sabotender, Arbaaz, Koth, Spitfire Lagac, Valakut Exploration; Avenger, Felidar Retreat, Survey Mechan; Mindslaver lock |
| Average mana value (nonland) | 2.58 | 2.78 |

Curve (nonland cards by mana value; the owner's list for comparison):
| MV | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|---|
| Base | 1 | 13 | 20 | 17 | 6 | 5 | 2 | 0 |
| Final | 1 | 10 | 15 | 23 | 9 | 4 | 1 | 1 |
| Owner's list (6.5, avg 3.37) | 0 | 11 | 10 | 15 | 11 | 9 | 4 | 3 |

## What was dropped or replaced, and why
Owner's current list (6.5, average mana value 3.37, 1 rock, 3 Spellbook lines of which 1 wins):
| Dropped | Why |
|---|---|
| Deflecting Swat | Its only copy is in the Azula ladder; Redirect Lightning stays |
| Banefire, Blasphemous Act, Hour of Revelation | Red or WWW cards the other decks want more; Planar Outburst is one-sided here and the pingers replace X burn |
| Omnath Locus of Rage, Titania Nature's Force, Meteor Sword, Karn's Sylex, Elemental Teachings, Awakening of Vitu-Ghazi | 5-7 mana; the list's curve (3.37) was its efficiency problem |
| Aang Air Nomad, Appa Steadfast Guardian, Avatar Destiny, The Boulder, The Cave of Two Lovers, Blossoming Tortoise, Druid Class, Stocking the Pantry, Horrid Vigor, Rockalanche, Airbender's Reversal, Sandbenders' Storm, Darksteel Citadel, Urza's Cave | Low card quality or off-plan; replaced by Sol Ring, Arcane Signet, 4 rocks, Zuran Orb (3 new Spellbook lines), Seismic Sense, Sabotender, Valakut Exploration, Great Divide Guide and cheap removal |
| Kept from it | Mindslaver, The Stasis Coffin, Crop Rotation, Toph Hardheaded Teacher, every locked card |

Measured top lists (7.2-7.4, 206,000-1,330,000 CLP) share this engine (Bumi + Liquimetal, Zuran Orb, Chromatic
Lantern, Lotus Cobra, Tireless Provisioner, landfall pingers, Annie, Great Divide Guide). Left out:
| Dropped | Price CLP | Why it is luxury here |
|---|---|---|
| Yavimaya, Jetmir's Garden, shocks, fetches, Lotus Field, Urborg, Taiga, Plateau | 2,980-329,000 | Cheap untapped duals (500-2,520) fix colors; Lantern, Guide and Wrenn already make every artifact tap for any color, Yavimaya's job here |
| Toph Greatest Earthbender, Toph Earthbending Master, Avatar Kyoshi, Earthbending Student, Badgermole Cub, Mossborn Hydra, The Ozolith, Ouroboroid, The Earth Crystal | 15,000-78,000 | Earthbend payoffs; the owned Bumis, Blind Bandit, Earth King and Hardened Scales cover the role |
| Springheart Nantuko (with Lotus Cobra and Toph, a fourth infinite line) | 10,400 | First buy above 40,000 |
| Sylvan Safekeeper | 10,000 (1 store) | Second outlet for loop C; Zuran Orb is enough |
| Field of the Dead (Game Changer), Heroic Intervention, Boros Charm, Lightning Greaves, Earthshape | 5,700-27,990 | Protection or value at a quarter of the budget each; The Stasis Coffin, Haystack and Inspiring Call cover it |
| Birds, Dryad, Scute Swarm, Prismatic Omen, Urza's Bauble, Tormod's Crypt, Three Visits, Nature's Lore | 1,560-10,600 | Ramp and artifact variants; Lantern, Cobra and Provisioner do the job |
| Mycosynth Lattice; bounce lands for the Teacher loop | - | Not luxury: Lattice is mass land denial with Vandalblast; the Teacher loop needs a bounce land and a 0-mana artifact, both kept out |

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Liquimetal Coating | 490 | Liquimetal Torque (2,830; move step 17 up) |
| 2 | Chromatic Lantern | 600 | Prismatic Omen (4,200; artifacts become every basic land type) |
| 3 | Soul-Guide Lantern | 590 | Tormod's Crypt (1,560) |
| 4 | Koth, the Geomancer | 300 (1 store) | Rampaging Baloths (690) |
| 5 | Spitfire Lagac | 200 | Weather Maker (500; landfall counters become 3 damage) |
| 6 | Exotic Orchard | 500 | Path of Ancestry (owned, 3 copies) |
| 7 | Clifftop Retreat | 500 | Raucous Carnival (owned) |
| 8 | Stroke of Midnight | 300 | Chaos Warp (790, a third copy) |
| 9 | All-Fates Scroll | 350 | Weather Maker (500) |
| 10 | Survey Mechan | 300 | keep Ichor Wellspring (owned) |
| 11 | Canopy Vista | 590 | Overgrown Farmland (1,820; move up) |
| 12 | Cinder Glade | 790 | Rockfall Vale (1,190; move up) |
| 13 | Battlefield Forge | 590 | Raucous Carnival (owned) or Rupture Spire (200) |
| 14 | Generous Gift | 1,560 | Wild Magic Surge (1,440) |
| 15 | Felidar Retreat | 2,090 | Rampaging Baloths (690) |
| 16 | Tireless Provisioner | 3,400 | Nissa, Worldsoul Speaker (490) |
| 17 | Liquimetal Torque | 2,830 | Reckless Handling (630; move up, finds Coating) |
| 18 | Avenger of Zendikar | 2,760 | keep Moraug (owned) |
| 19 | Evolution Sage | 3,300 (1 store) | Loading Zone (2,400) |
| 20 | Inspiring Call | 890 | Harmonize (300) |
| 21 | Rockfall Vale | 1,190 | keep the Mountain |
| 22 | Fabled Passage | 1,590 | Myriad Landscape (1,440) |
| 23 | Overgrown Farmland | 1,820 | keep the Plains |
| 24 | Karplusan Forest | 1,600 | keep the Forest |
| 25 | Reckless Handling | 630 | Brightglass Gearhulk (6,920; finds Zuran Orb and another 0-1 mana card) |
| 26 | Lotus Cobra | 7,800 | Birds of Paradise (7,500) |
| 27 | Brushland | 2,520 | keep the Forest |

## The three swaps that matter most
| Swap | CLP | What the deck loses without it |
|---|---|---|
| Liquimetal Coating (step 1) | 490 | The cheapest win line: Toph + Bumi + Coating is 7 mana over two turns with no Ashaya; without it every infinite needs the 5-mana Ashaya |
| Chromatic Lantern (step 2) | 600 | Every artifact becomes a mana source of any color: the ramp and fixing the 10/100 manabase lacks |
| Felidar Retreat (step 15) | 2,090 | The landfall engine that turns cheap artifacts into a board or team counters (draws with Terrasymbiosis, scales with Hardened Scales) and lets loop C win without a pinger |

## Owned cards another deck may also want
Checked against `fire-lord-azula.ladder.txt` and the Alexios draft in `decks/proposals/` (in progress).
| Card | Copies owned | Also in | Substitute here (CLP) |
|---|---|---|---|
| Sol Ring | 2 | Azula ladder (all steps), Alexios draft (base) | buy a third (1,900) |
| Arcane Signet | 2 | Azula ladder, Alexios draft | buy one (890) or Fellwar Stone (1,490) |
| Rogue's Passage (locked) | 2 | Azula ladder, Alexios draft | Secret Tunnel already makes Toph and Bumi (both Human Ally) unblockable; or buy one (742) |
| Command Tower | 2 | Azula ladder | one copy left for Toph; the Alexios draft does not use it |
| Redirect Lightning (locked) | 2 | Azula ladder; 2 measured Alexios lists | Angelic Intervention or Enter the Avatar State (owned) |
| Bender's Waterskin (locked) | 3 | Azula ladder, Alexios draft | the third copy is Toph's |
| Secret Tunnel (locked) | 3 | Alexios draft (base) | enough copies |
| Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape | 2, 3, 2 | Azula base | enough copies |
| Avoided on purpose (only copy elsewhere) | | | Mind Stone (Azula, Alexios) -> Selesnya Signet; Commander's Sphere, Mishra's Bauble, Abstergo Entertainment, Reckless Fireweaver (Alexios) -> Boros Locket, Chromatic Star, a Forest, none; Chaos Warp and Swiftfoot Boots (both copies elsewhere) -> Trapped in the Screen, Haystack; Deflecting Swat (Azula) |

If the owner wants each deck to keep its own Sol Ring, Arcane Signet and Rogue's Passage, the extra copies
cost 3,532 CLP in total (1,900 + 890 + 742), outside this ladder's numbers.

## Expected Commander Salt power (judgment, not a measurement)
| Point | Expected band | Reasoning |
|---|---|---|
| Base (0 CLP) | 6.6-7.0 (focused) | Same commander core as the owner's 6.5 list, but average mana value 2.58 instead of 3.37, Sol Ring and 5 rocks instead of 1, six Spellbook combos with four winning lines instead of one, 13 interaction pieces and a wipe, a creature tutor. Risk: the cheap baubles may score low one by one, and the manabase is still mostly basics and tapped lands |
| Step 15 (9,750) | 7.0-7.3 | Adds the cheapest win line (Coating), Lantern, graveyard hate, two pingers, five untapped duals, two flexible removal spells and Felidar Retreat |
| Final, step 27 (40,080) | 7.2-7.6 | Adds five high-meta Toph cards (Provisioner, Torque, Avenger, Evolution Sage, Lotus Cobra) and ten untapped duals. The measured 7.2-7.4 lists share this engine but cost 206,000-1,330,000 CLP; this one lacks their shocks, fetches and Yavimaya, which is where the remaining gap is |

The friend's 6.1 should be passed by the base. Most uncertain number: how much Commander Salt rewards the
cheap duals (manabase score) against one more synergy card; measuring steps 15 and 21 would show it.

## Free locked cards (red or colorless), ranked by fit
| Rank | Card | In the final? | Why |
|---|---|---|---|
| 1 | The Stasis Coffin | yes | Toph earthbends it at end step: protection from everything on every opponent's turn for {2} |
| 2 | Rogue's Passage | yes | Untaps in every Bumi combat: the combo's unblockable source |
| 3 | Secret Tunnel | yes | An earthbended Tunnel is an unblockable land creature; it also makes Toph and Bumi unblockable together |
| 4 | Redirect Lightning | yes | Protects Ashaya, Bumi or Toph for one red mana |
| 5 | Bender's Waterskin | yes | Any-color rock (a land under Toph) that untaps on each opponent's turn: pays the Coffin and instants |
| 6 | Mindslaver | yes | A real loop with Toph (one opponent's turn per round for {4}); no other ladder holds it. Late (6 + 4 mana) and the saltiest play pattern: if the owner prefers, swap it for Selesnya Signet (owned) |
| 7 | Swiftfoot Boots | no | Both copies are in the other decks; Haystack and the Coffin cover it |
| 8 | Deflecting Swat | no | Azula's only copy |
| 9 | Hidden Footblade | no | Haste for a recast creature; in the Azula and Alexios ladders |
| 10 | Labyrinth Adversary | no | 4-mana attacker; in the Alexios draft |
| 11 | Combustion Man | no | 5-mana attacker with no landfall synergy; in the Alexios draft |
| 12 | Electro, Assaulting Battery | no | Instant-and-sorcery payoff; this deck casts few |
| 13 | Horizon Stone | no | 5 mana for mana retention no deck needs; it is in no ladder, so the lock rule needs a home or the owner's drop |

All 10 Toph-only locked cards are in every step (Ashaya, Annie Joins Up, The Earth King, Terrasymbiosis,
Bumi Unleashed, Arbaaz Mir, Heaped Harvest, Seismic Tutelage, Wrenn and Realmbreaker, Inscription of Abundance).

## Wishlist (not in the pool, so not priced; do not build on them)
| Card | Role | Would replace | Why |
|---|---|---|---|
| Goblin Bombardment | combo outlet and win | Survey Mechan | Ashaya + Bombardment + Blind Bandit is lethal by itself (each sacrifice pings 1) |
| Ashnod's Altar | combo outlet, mana | Earthbender Ascension | Loop C then makes infinite colorless mana |
| Skullclamp | card advantage | Bitter Work | Earthbend-1 lands (Haru, Teacher), Plants and Cats die to draw 2 |
| Green Sun's Zenith | tutor | Reckless Handling | Finds Ashaya, Bumi, a looper or a pinger; no random discard |
| Chord of Calling | tutor | Crop Rotation | Instant creature tutor convoked by land creatures; frees the only Game Changer |
| Eternal Witness | recursion | True Ancestry (base) | Returns a combo piece on a body |
| Sakura-Tribe Elder | ramp | Rampant Growth | Blocks, then a basic onto the battlefield (landfall) |
| Wood Elves | ramp | Raucous Audience (base) | Untapped Forest (a shock or Canopy Vista) and a body |
| Talisman of Impulse | ramp | Boros Locket (base) | Untapped 2-mana R/G rock |
| Everflowing Chalice | ramp, landfall | Wayfarer's Bauble | 0-mana landfall trigger or a 2-mana rock |
| Mox Amber | ramp, landfall | Chromatic Star (base) | 0-mana artifact that taps for Toph's colors |
| Nature's Claim | interaction | Collective Resistance | 1-mana artifact or enchantment answer |
| Fateful Absence | interaction | Trapped in the Screen | 2-mana instant creature or planeswalker removal |
| Get Lost | interaction | Rocky Rebuke | 2-mana removal that also hits enchantments and planeswalkers |
| Skyclave Apparition | interaction | Hardlight Containment | Removal on a body that survives the aura being destroyed |
| Tamiyo's Safekeeping | protection | Haystack | 1-mana hexproof and indestructible for Ashaya or Bumi |
| Flawless Maneuver | protection | Inspiring Call | Free team indestructible with Toph out |
| Scavenging Ooze | graveyard hate | Soul-Guide Lantern | Repeatable exile on a growing body |
| Gavony Township | land, counters | Rumble Arena | Counters on every creature: Terrasymbiosis draws, land creatures grow |
| Kessig Wolf Run | land, finisher | Jungle Shrine | Mana sink with trample for a land creature |
| Boseiju, Who Endures | land, removal | Thornglint Bridge | Removal from a land slot |
| Craterhoof Behemoth | finisher | Avenger of Zendikar | One-turn kill with Plants, Cats and land creatures |
