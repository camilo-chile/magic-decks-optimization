# Fire Lord Azula: purchase ladder, round 3 (Phase 8 step 2, 2026-10-19)

Ladder: `decks/proposals/fire-lord-azula.ladder.txt` (base + 59 swaps, up to 199,262 CLP). Controls:
`decks/proposals/round1/`, `decks/proposals/round2/`. Checked with
`python -I -X utf8 scripts/ladder.py decks/proposals/fire-lord-azula.ladder.txt`: 0 INVALID; every step 100 cards,
Layer A floor 1 (steps 0-37) or 3 (steps 38-59: flagged late two-card combo Dualcaster Mage + Ember Island
Production, 8 mana), 0 Game Changers, 0 extra-turn cards, 0 reversible cards, every purchase with stock > 0.
Prices `merged-20261019T0300Z` (a hint; stock is verified in Phase 9). Power is not estimated here: the Commander
Salt measurement replaces it.

## Round 3
What the measurements showed (`decks/reports/round2-measured-20261018.md`):
- Azula's power follows Salt's Manabase Quality: round-2 step 24 scored 5.5 at 32 %, the same list with 9 cheap
  untapped duals 6.9 at 70 % (+1.4 for 7,155 CLP). Tapped lands hurt.
- Spells moved power little: round-1 base to round-2 step 24 (48,905 CLP of spells, same tapped mana base) +0.6.
- Toph calibrates the lands: a free base with no tapped lands and 29 basics measured 52 %; 9 cheap duals 68-69 %
  (about +1.9 % each); 3 shocks on top 93 % (about +8 % each).

What changed against round 2, and why:
- **Free base**: the 4 tapped lands (Path of Ancestry, Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape) become
  basics. No tapped land is left at any step.
- **Lands first**: steps 1-9 are exactly the measured 70 % land set; 4 more always-untapped duals (Frostboil Snarl,
  Underground River, Sulfurous Springs, Sunken Ruins) come before 25,000; the 3 slow lands and the first shock before
  50,000; all 3 shocks before 100,000. Per CLP the model from the measurements ranks cheap duals first, shocks second,
  spells third.
- **Spells by value per CLP between the lands**: the cheap structural pieces first (Narset's Reversal loop, Glamdring,
  two reducers, Mystical Teachings as the tutor Salt asks for, Storm-Kiln), then the cheap payoffs and draw; the
  expensive spells (Talismans, High Fae, Dark Ritual, Onyx, Toxic Deluge, Ashling) move after 100,000.
- **New cheap cards priced from the wishlist**: Infernal Grasp (700), Kolaghan's Command (900), Fact or Fiction (300),
  Mana Leak (490), Ertai Resurrected (900), Anger of the Gods (800), Solve the Equation (5,390, second tutor).
- **Dropped**: Imperial Recruiter, Reliquary Tower (colorless land), Electrolyze and Bitter Triumph (replaced by
  better new cards).

| List | Left (round 2 to round 3) | Entered |
|---|---|---|
| Base (step 0) | Path of Ancestry, Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape | 2 Island, 1 Swamp, 1 Mountain |
| Round-2 final (146,840) vs round-3 150k (148,712) | Imperial Recruiter, Snapcaster Mage, Leyline, Desperate Ritual, Reliquary Tower, Electrolyze, Bitter Triumph, 3 Island, 3 Swamp, 1 Mountain | Blood Crypt, Steam Vents, Watery Grave, Frostboil Snarl, Sunken Ruins, Haunted Ridge, Shipwreck Marsh, Stormcarved Coast, Infernal Grasp, Kolaghan's Command, Fact or Fiction, Mana Leak, Ertai Resurrected, Anger of the Gods |
| 200k (step 59) vs 150k | Consider, Heartless Act, Go for the Throat, Hero's Downfall, Shadowblood Ridge, 1 Mountain | Leyline, Solve the Equation, Snapcaster Mage, Desperate Ritual, Luxury Suite, Graven Cairns |

| Checkpoint | Step | Cost CLP | Lands (basics / bought duals / shocks) | Manabase Quality estimate |
|---|---|---|---|---|
| 0 | 0 | 0 | 30 / 0 / 0, 0 tapped | about 50 % (Toph's like base: 52 %) |
| 25,000 | 23 | 24,882 | 17 / 13 / 0 | 74-78 % (measured 70 % at step 9, 21 basics) |
| 50,000 | 34 | 49,592 | 14 / 15 / 1 | 83-87 % |
| 75,000 | 39 | 74,472 | 13 / 15 / 2 | 87-90 % |
| 100,000 | 44 | 98,862 | 11 / 16 / 3 | 91-95 % (Toph: 93 % with 3 shocks) |
| 150,000 | 53 | 148,712 | 11 / 16 / 3 | 91-95 % |
| 200,000 | 59 | 199,262 | 10 / 17 / 3 (Luxury Suite for Shadowblood Ridge) | 93-96 % |

Ranking rationale against the measured points (no absolute numbers):
- **25,000** ranks above round-1 step 17 (6.1, MQ 53 %): same core engine (loop, Storm-Kiln, Glamdring, reducers,
  tutor, two burn payoffs) on a mana base above the measured 70 %.
- **50,000** should beat the 6.9 @ 56,060 floor: a higher Manabase Quality (13 more untapped duals and a shock against
  9 duals) and the round-1 core plus Infernal Grasp, Kolaghan's Command and Fact or Fiction; it lacks Talismans, High
  Fae, Counterspell, Arcane Denial and Dualcaster, which the measurements suggest moved little.
- **75,000-100,000**: the remaining shocks (the Toph jump to 93 %), Veyran, Dualcaster (fourth loop, the first one
  without Azula), Counterspell, My Precious.
- **150,000** ranks against round-1 step 47 (7.4 @ 148,760): the same lands plus four more untapped duals (Frostboil
  Snarl, Sunken Ruins, Haunted Ridge, Shipwreck Marsh, Stormcarved Coast in for Waterlogged and four basics) and the
  same spell core; round 1 had Desperate Ritual, Leyline, Electrolyze, Bitter Triumph and four former locked cards
  where round 3 has Infernal Grasp, Kolaghan's Command, Fact or Fiction, Mana Leak, Ertai, Anger of the Gods,
  Consider and Ember Island Production.
- **200,000**: a second tutor, Snapcaster, Leyline, Desperate Ritual and the last land upgrades; low power per CLP.

Stores: 7 at every checkpoint from 25,000 because Frostboil Snarl is cheapest at piedrabruja (482); cardnexus sells it
for 490, so the optimizer can drop that store for 8 CLP. Single-store cards: Veyran (gameofmagic), Desperate Ritual
(paytowin), Demand Answers (fallback only).

## Strategy and engine
Grixis combat spellslinger. Azula attacks every turn; cheap instants cast in her combat are copied (mandatory), so
removal, draw and Treasure spells are 2-for-1s. Cost reducers make them nearly free; payoffs that count every copy turn
one combat into a kill. Wins:
1. **Loops** (Commander Spellbook, local bulk): Azula + Narset's Reversal + Frantic Search (step 10), Azula +
   Narset's Reversal + Storm-Kiln Artist (step 16), Azula + Snap + Dualcaster Mage and Dualcaster Mage + Ember Island
   Production (step 38). Guttersnipe, Black Waltz No. 3, Onyx or a huge X spell close them. Tutors: Mystical
   Teachings (step 14; copied, both halves), Solve the Equation (step 55).
2. **Copied X spells** fed by Treasures and rituals: Comet Storm, Electrodominance, Exsanguinate, Invoke Calamity.
3. **Commander damage**: Bulk Up copied takes Azula from 4 to 16; its copied flashback makes 64.

Rules notes: Archmage Emeritus draws are mandatory (stop a loop before decking); ritual mana empties between combat
steps (firebending mana, Electro, Ashling and The Last Agni Kai keep it); sorceries and creatures are copied only with
flash (High Fae from step 48, Leyline from step 54). Ember Island Production can also copy Azula as a non-legendary
token: two attacking Azulas copy every spell twice.

Kept out (Layer A or rules): Twinning Staff, Reverberate, Increasing Vengeance, Return the Favor (two-card loops with
Narset's Reversal); Hullbreaker Horror (with Sol Ring); Intruder Alarm with the owned Joo Dee or Xerex Strobe-Knight
(early two-card infinites); Reiterate, Expansion // Explosion (self-copy loop); Twinflame, Heat Shimmer, Saw in Half
(with Dualcaster); extra-turn spells; every tapped land.

## Roles
| Role | Base (step 0) | 25,000 (step 23) | 200,000 (step 59) |
|---|---|---|---|
| Lands | 36: 30 basics, Command Tower, Cascade Bluffs, Choked Estuary, Foreboding Ruins, Fire Nation Palace, Rogue's Passage | 36: 17 basics, the 6 owned, 13 bought duals | 36: 10 basics, the 6 owned, 17 duals, 3 shocks |
| Ramp and cost reduction | 10: Sol Ring, Arcane Signet, Mind Stone, Dimir Signet, Izzet Signet, Commander's Sphere, Bender's Waterskin, Black Market Connections, Goblin Electromancer, Electro | 13: base minus Commander's Sphere, plus Glamdring, Nightscape Familiar, Stormcatch Mentor, Storm-Kiln Artist | 15: Sol Ring, Arcane Signet, 3 Talismans, Bender's Waterskin, Black Market Connections, Dark Ritual, Desperate Ritual, Glamdring, Goblin Electromancer, Nightscape Familiar, Stormcatch Mentor, Electro, Storm-Kiln Artist |
| Card advantage | 12 | 11 (Fact or Fiction in) | 8: Frantic Search, Big Score, Brainstorm, Opt, Archmage Emeritus, Fact or Fiction, Deadly Dispute, Unexpected Windfall |
| Tutors | Lo and Li | Mystical Teachings | Mystical Teachings, Solve the Equation |
| Interaction | 17 removal, 4 counters, 3 wipes | 15 removal, 3 counters (Narset's Reversal, Mana Leak, Negate), 3 wipes | 7 removal (Terminate, Chaos Warp, The Last Agni Kai, Imprisoned in the Moon, Infernal Grasp, Lightning Bolt, Kolaghan's Command), Ertai, 5 counters (Narset's Reversal, Mana Leak, Counterspell, Arcane Denial, An Offer You Can't Refuse), 3 wipes (Anger of the Gods, Toxic Deluge, Aether Gale) |
| Protection | 7 | 7 | 5: Swiftfoot Boots, Deflecting Swat, Redirect Lightning, Octopus Form, My Precious |
| Win conditions | 6, no loop | 7 + 2 loops (Guttersnipe, Black Waltz No. 3 in) | 9 + 4 loops: Comet Storm, Electrodominance, Guttersnipe, Black Waltz No. 3, Invoke Calamity, Exsanguinate, Bulk Up, Professor Onyx, Ashling |
| Engines and value | Torrential Gearhulk, Snap, Ember Island Production | same | + Veyran, Dualcaster Mage, High Fae Trickster, Leyline, Snapcaster Mage, Ertai |
| Average mana value (nonland, X = 0) | 2.51 | 2.59 | 2.73 |

| MV | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|
| Base | 12 | 28 | 14 | 3 | 3 | 2 | 1 |
| 25,000 | 11 | 27 | 13 | 7 | 2 | 2 | 1 |
| 200,000 | 8 | 24 | 15 | 11 | 3 | 2 | 0 |

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Exotic Orchard | 500 | move up Stormcarved Coast (3,750) |
| 2 | Sulfur Falls | 500 | move up Stormcarved Coast (3,750) |
| 3 | Shadowblood Ridge | 590 | move up Graven Cairns (5,690) |
| 4 | Shivan Reef | 690 | move up Stormcarved Coast (3,750) |
| 5 | Sunken Hollow | 790 | move up Shipwreck Marsh (2,780) |
| 6 | Darkwater Catacombs | 790 | move up Sunken Ruins (1,790) |
| 7 | Smoldering Marsh | 915 | move up Haunted Ridge (1,990) |
| 8 | Dragonskull Summit | 1,190 | move up Haunted Ridge (1,990) |
| 9 | Drowned Catacomb | 1,190 | move up Shipwreck Marsh (2,780) |
| 10 | Narset's Reversal | 3,400 | move up Dualcaster Mage (6,200) |
| 11 | Glamdring, Foe-hammer // Gleam of Death | 915 | Tablet of Discovery (2,500) |
| 12 | Nightscape Familiar | 450 | Baral, Chief of Compliance (4,200) |
| 13 | Stormcatch Mentor | 590 | Firebending Student (790) |
| 14 | Mystical Teachings | 450 | move up Solve the Equation (5,390) |
| 15 | Frostboil Snarl | 482 | same card at cardnexus (490) |
| 16 | Storm-Kiln Artist | 3,590 | Sedgemoor Witch (3,000) |
| 17 | Underground River | 1,990 | move up Shipwreck Marsh (2,780) |
| 18 | Sulfurous Springs | 2,090 | move up Haunted Ridge (1,990) |
| 19 | Sunken Ruins | 1,790 | move up Shipwreck Marsh (2,780) |
| 20 | Guttersnipe | 700 | Kessig Flamebreather (7,440) |
| 21 | Black Waltz No. 3 | 490 | Sedgemoor Witch (3,000) |
| 22 | Fact or Fiction | 300 | Commence the Endgame (500) |
| 23 | Mana Leak | 490 | Mana Sculpt (1,290) |
| 24 | Deadly Dispute | 1,650 | Sazacap's Brew (500) |
| 25 | Unexpected Windfall | 2,200 | Demand Answers (1,590, 1 store) |
| 26 | Invoke Calamity | 900 | Prismari Command (915) |
| 27 | Infernal Grasp | 700 | Bitter Triumph (490) |
| 28 | Lightning Bolt | 1,400 | Electrolyze (300) |
| 29 | Kolaghan's Command | 900 | Prismari Command (915) |
| 30 | Exsanguinate | 890 | keep Banefire (owned) |
| 31 | Bulk Up | 400 | Temur Battle Rage (450) |
| 32 | Haunted Ridge | 1,990 | Graven Cairns (5,690) |
| 33 | Shipwreck Marsh | 2,780 | keep the Island |
| 34 | Blood Crypt | 10,900 | Luxury Suite (12,990) |
| 35 | Ertai Resurrected | 900 | Venser, Shaper Savant (990) |
| 36 | Veyran, Voice of Duality | 5,480 (1 store) | Wizard's Staff (7,150) |
| 37 | Steam Vents | 11,500 | Training Center (21,410) or keep the Island |
| 38 | Dualcaster Mage | 6,200 | Shore Up (300; no loop) |
| 39 | Anger of the Gods | 800 | keep Blasphemous Act (owned) |
| 40 | Watery Grave | 12,200 | keep the Swamp (Morphic Pool 30,140 is the premium option) |
| 41 | Counterspell | 3,300 | Mana Sculpt (1,290) |
| 42 | Stormcarved Coast | 3,750 | keep the Island |
| 43 | My Precious // Allure of Power | 2,350 | Lightning Greaves (6,490) |
| 44 | Arcane Denial | 2,840 | Tishana's Tidebinder (3,320) |
| 45-47 | Talismans of Dominance, Creativity, Indulgence | 2,290-2,490 | Fellwar Stone (1,490) or Everflowing Chalice (500) |
| 48 | High Fae Trickster | 5,000 | move up Leyline of Anticipation (5,600) |
| 49 | Dark Ritual | 4,990 | Pyretic Ritual (6,990) |
| 50 | Professor Onyx | 5,410 | Sedgemoor Witch (3,000) |
| 51 | Toxic Deluge | 7,790 | Massacre Girl (2,090) |
| 52 | Ashling, Flame Dancer | 15,490 | Sedgemoor Witch (3,000) |
| 53 | An Offer You Can't Refuse | 3,900 | Mana Sculpt (1,290) |
| 54 | Leyline of Anticipation | 5,600 | Emergence Zone (4,490) |
| 55 | Solve the Equation | 5,390 | Merchant Scroll (7,850) |
| 56 | Luxury Suite | 12,990 | keep Shadowblood Ridge |
| 57 | Snapcaster Mage | 13,870 | Venser, Shaper Savant (990) |
| 58 | Graven Cairns | 5,690 | keep the Mountain |
| 59 | Desperate Ritual | 7,600 (1 store) | Pyretic Ritual (6,990) |

## The three swaps that matter most
| Swap | CLP | What the deck loses without it |
|---|---|---|
| Steps 1-9, the nine cheap duals | 7,155 | The measured +1.4 power (Manabase Quality 32 % to 70 %); nothing else bought moved Azula as much |
| Narset's Reversal (step 10) | 3,400 | The win path and bracket 3 until step 38 (no loop means the "casual stall shell" pattern again) |
| Blood Crypt (step 34) | 10,900 | The first premium land; on Toph the three shocks were worth 25 points of Manabase Quality |

## Owned cards another deck may also want
From the current Toph and Alexios ladders in `decks/proposals/`:
| Card | Copies owned | Decks that use it | Conflict | Substitute here (CLP) |
|---|---|---|---|---|
| Sol Ring | 2 | Toph, Alexios, Azula | yes (3 for 2) | buy a third (1,900) |
| Arcane Signet | 2 | Toph, Alexios, Azula | yes | buy one (890) or Everflowing Chalice (500) |
| Rogue's Passage | 2 | Toph, Alexios, Azula | yes | a basic (also helps Manabase Quality); My Precious covers it from step 43 |
| Bender's Waterskin | 3 | Toph, Alexios, Azula | no | - |
| Command Tower, Redirect Lightning | 2 each | Toph, Azula | no | - |
| Swiftfoot Boots, Chaos Warp, Blasphemous Act, Firebending Lesson, Lightning Strike | 2 each | Alexios, Azula | no | - |

## Wishlist (not in the pool; only lands that could raise Manabase Quality further, plus one engine)
| Card | Role | Would replace | Why |
|---|---|---|---|
| Spirebluff Canal | land | Stormcarved Coast | U/R fast land: untapped in the first turns |
| Darkslick Shores | land | Shipwreck Marsh | U/B fast land |
| Blackcleave Cliffs | land | Haunted Ridge | B/R fast land |
| Fiery Islet | land | a basic Island | U/R horizon land: always untapped, cycles late |
| Tainted Isle | land | a basic Island | U/B, untapped; colored with a Swamp |
| Tainted Peak | land | a basic Mountain | B/R, untapped; colored with a Swamp |
| Underground Sea | land | Watery Grave's basic slot | premium U/B dual (price first: likely far above budget) |
| Badlands | land | a basic Swamp | premium B/R dual (same caveat) |
| Multiversal Passage | land | a basic | untapped (2 life) land of any one basic type |
| Archmage of Runes | reducer / draw | Goblin Electromancer | reduces instants and sorceries and draws on each cast |
