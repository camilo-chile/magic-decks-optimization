# Fire Lord Azula: purchase ladder (Phase 8 step 2, 2026-10-18)

Ladder: `decks/proposals/fire-lord-azula.ladder.txt` (base + 47 swaps). Checked with
`python -I -X utf8 scripts/ladder.py decks/proposals/fire-lord-azula.ladder.txt`: every step valid
(100 cards, Layer A floor 1 at target 3, 0 Game Changers, 0 extra-turn cards, every purchase with
stock > 0 in the pool). Prices: `merged-20261017T2337Z.json` (a hint; stock is verified in Phase 9).
Power figures below are judgments, not measurements.

| Checkpoint (cap CLP) | Last step | Cost CLP |
|---|---|---|
| 0 | 0 (base) | 0 |
| 25,000 | 17 | 24,505 |
| 50,000 | 31 | 49,190 |
| 75,000 | 38 | 74,070 |
| 100,000 | 41 | 97,060 |
| 150,000 | 47 | 148,760 |

Final step: 47 cards bought, 38 owned nonbasic cards, 15 basics. Every checkpoint uses the same 6 stores
(cardnexus, gameofmagic, lacomarca, magic4ever, oasis, paytowin; assumed shipping 30,000 CLP, outside the
budget). Consolidation for the optimizer: in steps 1-17 lacomarca and oasis sell only Deadly Dispute,
Guttersnipe, Invoke Calamity and Mystical Teachings; buying them at cardnexus (4,490; 890), paytowin (2,400)
and gameofmagic (742) costs about +4,800 CLP of cards and saves 2 stores (10,000 of assumed shipping).
Single-store cards fix their store: Veyran (gameofmagic), Waterlogged Teachings (cardnexus), Desperate
Ritual (paytowin).

Spellbook combos (local bulk; all are Azula + 2 cards, tag S, so Layer A sets no floor): Narset's Reversal +
Frantic Search from step 1, Narset's Reversal + Storm-Kiln Artist from step 2, Dualcaster Mage + Snap from
step 30. The base has none.

## Strategy and engine
Grixis combat spellslinger. Azula attacks every turn and the deck holds cheap instants for her
combat: each one is copied (mandatory copy), so removal, draw and Treasure spells are 2-for-1s.
Cost reducers make those spells nearly free, and payoffs that count every copy turn one combat into
a kill. Three ways to win:
1. **Azula loops** (Commander Spellbook lines, 3 cards counting Azula, so Layer A sets no floor):
   Narset's Reversal + Frantic Search (loot, storm, mana: each cycle costs 5 and untaps 6 lands);
   Narset's Reversal + Storm-Kiln Artist (unbounded Treasures); later Dualcaster Mage + Snap.
   Guttersnipe, Black Waltz No. 3, Professor Onyx or a huge X spell close it.
2. **Copied X spells** fed by Treasures and rituals: Comet Storm, Electrodominance, Exsanguinate
   (with flash from High Fae Trickster or Leyline), Invoke Calamity re-casting them.
3. **Commander damage**: Bulk Up copied doubles Azula twice (4 to 16) and its flashback, copied again,
   makes 64, through Rogue's Passage or My Precious.

Rules notes: Archmage Emeritus draws are mandatory, so stop a loop before the library runs out; ritual
mana empties between combat steps (only firebending mana, Electro, Ozai, Ashling and The Last Agni Kai
keep it); sorceries and creatures are copied only with flash (High Fae Trickster from step 29, Leyline at 47).

Engine core (must be together):
| Piece | Cards | Why it cannot be split |
|---|---|---|
| Azula attacks and survives | Swiftfoot Boots, My Precious, Rogue's Passage, Deflecting Swat, Redirect Lightning, Octopus Form | No attack, no copy: every other card is half a card without her in combat |
| Cheap instant density | Frantic Search, Big Score, Unexpected Windfall, Deadly Dispute, Brainstorm, cheap removal | The copy is only as good as the number of spells cast in one combat |
| Cost reduction | Glamdring (on Azula: instants cost 4 less, X included), Nightscape Familiar, Stormcatch Mentor, Goblin Electromancer | Turns 4-6 mana of combat into 3-5 spells, each copied |
| Copy-counting payoffs | Storm-Kiln Artist, Archmage Emeritus, Veyran, Guttersnipe, Black Waltz No. 3 | Copies are not casts: magecraft (Storm-Kiln, Archmage, Veyran, Onyx, Ashling) sees both, cast triggers see one |
| Win path | Narset's Reversal with Frantic Search / Storm-Kiln | Fixes the weakest pillar of the owner's report (win conditions 81, "casual stall shell") |

Traps kept out (Layer A or rules): Twinning Staff and Reverberate (two-card loops with Narset's
Reversal), Hullbreaker Horror (with Sol Ring), Return the Favor, Reiterate, Expansion // Explosion and
any "copy target spell" card (self-copy loop with magecraft), Twinflame / Heat Shimmer / Saw in Half
(with Dualcaster Mage), extra-turn spells (the copy doubles them).

## Roles
| Role | Base (step 0) | Final (step 47) |
|---|---|---|
| Lands | 36: 26 basics, 10 nonbasic (4 tapped: Path of Ancestry, Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape) | 35 + 1 MDFC: 15 basics, 20 nonbasic (shock, check, battle, filter, pain lands; none tapped unconditionally), Waterlogged Teachings |
| Ramp and cost reduction | 10: Sol Ring, Arcane Signet, Mind Stone, Dimir Signet, Izzet Signet, Commander's Sphere, Bender's Waterskin, Black Market Connections, Goblin Electromancer, Electro | 15: Sol Ring, Arcane Signet, 3 Talismans, Bender's Waterskin, Black Market Connections, Dark Ritual, Desperate Ritual, Glamdring, Goblin Electromancer, Nightscape Familiar, Stormcatch Mentor, Electro, Storm-Kiln Artist |
| Card advantage | 14 + 1 tutor (Lo and Li): Frantic Search, Big Score, Thrill, Brainstorm, Consider, Opt, Abandon Attachments, Archmage Emeritus, Fists of Flame, Frostcliff Siege, Assassin Gauntlet, Escape Detection, Cunning Maneuver, Professor Zei | 9 + 2 tutors: Frantic Search, Big Score, Unexpected Windfall, Deadly Dispute, Brainstorm, Opt, Archmage Emeritus, Frostcliff Siege, Assassin Gauntlet; Mystical Teachings, Waterlogged Teachings (plus Gleam of Death, Allure of Power, Ashling, Onyx) |
| Interaction | 22: 16 removal (Amphibian Downpour among them), 3 counters (Negate, It'll Quench Ya!, Get Out), 3 wipes (Blasphemous Act, Aether Gale, Day of Black Sun) | 17: 11 removal (Lightning Bolt, Terminate, Heartless Act, Go for the Throat, Hero's Downfall, Bitter Triumph, Chaos Warp, Electrolyze, The Last Agni Kai, Royal Assassin, Imprisoned in the Moon), 4 counters (Counterspell, Arcane Denial, An Offer You Can't Refuse, Narset's Reversal), 2 wipes (Toxic Deluge, Aether Gale), plus Ashling's sweep |
| Protection | 7: Redirect Lightning, Deflecting Swat, Octopus Form, Swiftfoot Boots, Champion's Helm, Hidden Footblade, Undying Malice | 5: Redirect Lightning, Deflecting Swat, Octopus Form, Swiftfoot Boots, My Precious |
| Win conditions | 7: Comet Storm, Electrodominance, Banefire, Unleash Fury, Run Amok, Ozai, Thermo-Alchemist (no combo) | 10: Comet Storm, Electrodominance, Exsanguinate, Invoke Calamity, Bulk Up, Ozai, Guttersnipe, Black Waltz No. 3, Professor Onyx, Ashling; plus 3 Azula loops |
| Engines and value | 2: Torrential Gearhulk, Snap | 6: Veyran, Torrential Gearhulk, Snap, Dualcaster Mage, High Fae Trickster, Leyline of Anticipation |
| Average mana value (nonland, X = 0) | 2.48 | 2.73 |

Curve (nonland cards by mana value, X = 0; the final counts Waterlogged Teachings at 4):
| MV | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|
| Base | 12 | 28 | 15 | 3 | 2 | 2 | 1 |
| Final | 8 | 24 | 17 | 10 | 2 | 3 | 0 |

## What the measured top lists do that this ladder drops (luxury, not core)
The five lists (7.2-7.4, 497,800-1,233,795 CLP) share this ladder's engine: Storm-Kiln, Talismans,
Unexpected Windfall (5 of 5), Dark Ritual, Dualcaster, Narset's Reversal, Nightscape, Veyran, High Fae,
Frantic Search, Snap (4 of 5). What is left out:
| Dropped | Price CLP | Why it is luxury here |
|---|---|---|
| Game Changers: Cyclonic Rift, Orcish Bowmasters, Vampiric / Demonic Tutor, The One Ring, Fierce Guardianship, Ancient Tomb, Jeska's Will | 37,000-124,000 each (Jeska's Will, Demonic Tutor via Emeritus: no stock) | Each costs a quarter or more of the whole ladder; they add efficiency, not the engine. Cyclonic Rift is the first one to add above 150,000 |
| Enduring Curiosity | 116,560 | Draw engine; Archmage Emeritus, Windfall and Deadly Dispute copied do the same job |
| Fetches, Training Center, Morphic Pool, Luxury Suite, Xander's Lounge, Verges | 12,990-44,320 each | Check, battle, filter and pain lands at 500-2,090 give untapped duals; only the 3 shocks are kept |
| Seething Song, Cabal Ritual, Culling the Weak | 9,900-18,490 | Rituals are step-bound; two (Dark, Desperate) plus Storm-Kiln Treasures are enough |
| Snapcaster Mage, Vendilion Clique, Mocking Doppelganger | 3,600-13,870 | Flash value; Torrential Gearhulk (owned) and Dualcaster cover it |
| Borne Upon a Wind, Vedalken Orrery, Valley Floodcaller | 11,300-17,990 (Floodcaller: no stock) | Flash enablers; High Fae Trickster and Leyline cover it |
| Swan Song, Deadly Rollick, Untimely Malfunction | 10,000-69,990 | Premium interaction with cheap equivalents in the list |
| Fated Firepower, Crackle with Power, Wan Shi Tong, Vivi's Persistence | 11,600-49,990 | Finishers; the deck already has three loops and copied X spells |
| Brotherhood Regalia, Silver Shroud Costume, Winged Boots, Hammer of Nazahn | 7,570-14,490 | My Precious does hexproof plus unblockable for 2,350 |
| Twinning Staff, Reverberate, Hullbreaker Horror, Return the Favor, Isochron Scepter | - | Not luxury: Bracket 3 hazards with the cards above |

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Narset's Reversal | 3,400 | Dualcaster Mage (6,200; the Snap loop, move it up) |
| 2 | Storm-Kiln Artist | 3,590 | Sedgemoor Witch (3,000) |
| 3 | Glamdring, Foe-hammer // Gleam of Death | 915 | Tablet of Discovery (2,550) |
| 4 | Unexpected Windfall | 2,200 | Demand Answers (1,590, 1 store) |
| 5 | Deadly Dispute | 1,650 | Sazacap's Brew (500) |
| 6 | Nightscape Familiar | 450 | Rakdos Signet (450) |
| 7 | Stormcatch Mentor | 590 | Firebending Student (790) |
| 8 | Invoke Calamity | 900 | Prismari Command (915) |
| 9 | Guttersnipe | 700 | Professor Onyx (5,410; move it up) |
| 10 | Black Waltz No. 3 | 490 | keep Thermo-Alchemist (owned) |
| 11 | Mystical Teachings | 450 | Waterlogged Teachings (890; move it up) |
| 12 | Exsanguinate | 890 | keep Banefire (owned, contested) or Crackle with Power (11,600) |
| 13 | Lightning Bolt | 1,400 | Withering Torment (2,090) |
| 14 | Bulk Up | 400 | Temur Battle Rage (450) |
| 15 | Veyran, Voice of Duality | 5,480 (1 store) | Wizard's Staff (7,650) |
| 16 | Sulfur Falls | 500 | Temple of Epiphany (490) |
| 17 | Exotic Orchard | 500 | Rupture Spire (200) |
| 18 | Shivan Reef | 690 | Temple of Epiphany (490) or Frostboil Snarl (482, adds a store) |
| 19 | Sunken Hollow | 790 | Shipwreck Marsh (2,780) |
| 20 | Darkwater Catacombs | 790 | Sunken Ruins (1,790) |
| 21 | Shadowblood Ridge | 590 | Temple of Malice (owned) |
| 22 | Smoldering Marsh | 915 | Haunted Ridge (1,990) |
| 23 | Dragonskull Summit | 1,190 | Haunted Ridge (1,990) |
| 24 | Drowned Catacomb | 1,190 | Temple of Deceit (owned) |
| 25 | Electrolyze | 300 | Prismari Command (915) |
| 26 | Bitter Triumph | 490 | Sheoldred's Edict (2,200) |
| 27 | Counterspell | 3,300 | Mana Sculpt (1,290) |
| 28 | Waterlogged Teachings // Inundated Archive | 890 (1 store) | keep the Island |
| 29 | High Fae Trickster | 5,000 | Leyline of Anticipation (5,600; move it up) |
| 30 | Dualcaster Mage | 6,200 | Shore Up (300; protection instead of the loop) |
| 31 | My Precious // Allure of Power | 2,350 | Lightning Greaves (6,490) |
| 32 | Talisman of Dominance | 2,290 | Fellwar Stone (1,490) |
| 33 | Talisman of Creativity | 2,490 | Rakdos Signet (450) |
| 34 | Talisman of Indulgence | 2,490 | Rakdos Signet (450) or Fellwar Stone (1,490) |
| 35 | Arcane Denial | 2,840 | Mana Sculpt (1,290) |
| 36 | Dark Ritual | 4,990 | Pyretic Ritual (6,990) |
| 37 | Toxic Deluge | 7,790 | keep Blasphemous Act (owned, contested) |
| 38 | Underground River | 1,990 | Sunken Ruins (1,790) |
| 39 | Sulfurous Springs | 2,090 | Haunted Ridge (1,990) |
| 40 | Ashling, Flame Dancer | 15,490 | Sedgemoor Witch (3,000) |
| 41 | Professor Onyx | 5,410 | Sedgemoor Witch (3,000) |
| 42 | An Offer You Can't Refuse | 3,900 | Mana Sculpt (1,290) |
| 43 | Steam Vents | 11,500 | Riverglide Pathway (5,920) |
| 44 | Watery Grave | 12,200 | Clearwater Pathway (5,520) |
| 45 | Blood Crypt | 10,900 | Blightstep Pathway (5,900) |
| 46 | Desperate Ritual | 7,600 | Pyretic Ritual (6,990) |
| 47 | Leyline of Anticipation | 5,600 | Emergence Zone (4,490) |

## The three swaps that matter most
| Swap | CLP | What the deck loses without it |
|---|---|---|
| Narset's Reversal (step 1) | 3,400 | The only real win path before step 30: without it the list stays the "casual stall shell" of the owner's report (no combo, win conditions below baseline) |
| Storm-Kiln Artist (step 2) | 3,590 | The mana engine: 2 Treasures per instant in combat pay for the next spells and the X finishers; also the second Narset loop |
| Glamdring (step 3) | 915 | On Azula, every instant costs 4 less: without it a combat holds 2-3 spells instead of 4-6, and Comet Storm / Electrodominance lose 4 points of X |

## Owned cards another deck may also want
| Card | Copies owned | Also wanted by | Substitute here (CLP) |
|---|---|---|---|
| Sol Ring | 2 | Toph and Alexios lists | buy a third (1,900) |
| Arcane Signet | 2 | Toph and Alexios lists | buy one (890) or Fellwar Stone (1,490) |
| Command Tower | 2 | Toph (current list) | buy one (500) or Rupture Spire (200) |
| Rogue's Passage (locked) | 2 | Toph (current), Alexios lists | My Precious already gives unblockable; buy one (742) |
| Redirect Lightning (locked) | 2 | Toph (current), Alexios lists | Imp's Mischief (owned) |
| Deflecting Swat (locked) | 1 | Toph (current), Alexios lists | Bolt Bend (5,990, 1 store) or Imp's Mischief (owned) |
| Swiftfoot Boots (locked) | 2 per inventory (`locked.md` of 2026-10-16 says 1) | Toph and Alexios lists | Lightning Greaves (6,490) |
| Chaos Warp | 2 | Toph and Alexios lists | buy one (790) or Withering Torment (2,090) |
| Big Score | 1 | Alexios lists | buy one (1,490) or Sazacap's Brew (500) |
| Bender's Waterskin (locked) | 3 | Toph lists | Fellwar Stone (1,490) |
| Base only, cut during the ladder | | | Banefire (Toph current; out at step 12), Blasphemous Act (2; out at 37), Champion's Helm (Alexios lists; out at 31), Abrade and Unleash Fury (Alexios lists; out at 29 and 36), Mind Stone, Commander's Sphere, Path of Ancestry, Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape (Toph; out by step 34) |

Red owned cards that the mono-red Alexios deck could also use and that stay to the end here: Fire
Nation Palace, Comet Storm, The Last Agni Kai, Electro (none is in an Alexios measured list).

## Expected Commander Salt power (judgment, not a measurement)
| Point | Expected band | Reasoning |
|---|---|---|
| Base (0 CLP) | 4.6-5.2 (casual to upgraded casual) | Same shell as the owner's 4.0 list, but every weak creature and aura is replaced by cheap cantrips, Frantic Search and efficient instant removal (lower curve, more interaction). Still no combo, no fast mana beyond Sol Ring and one tutor: the win-conditions penalty stays |
| Step 17 (24,505) | 5.8-6.4 (upgraded casual) | Two Spellbook loops, Storm-Kiln, Glamdring, three reducers, two burn payoffs, a tutor and Veyran: the weak pillar is fixed; manabase still mostly basics |
| Final, step 47 (148,760) | 6.6-7.1 (mid power) | Adds the third loop, Talismans, rituals, flash enablers, Ashling, Onyx, four counters and an untapped manabase with shocks. Below the measured 7.2-7.4 lists, which add 3 Game Changers, fetches and more fast mana for 500,000+ CLP |

The friend's 6.1 is probably passed around step 20-30 (26,000-47,000 CLP); this is the most
uncertain number here. Open question for the measurement: steps 43-45 (three shocks, 34,600) against
Cyclonic Rift (37,000, the first Game Changer); Commander Salt's weight on the manabase is unknown, so
measure the step-42 list with each and keep the higher score.

## Free locked cards (red or colorless), ranked by fit
| Rank | Card | In the final? | Why |
|---|---|---|---|
| 1 | Deflecting Swat | yes | Free while Azula is out, and Azula copies it (two redirects) |
| 2 | Swiftfoot Boots | yes | Haste and hexproof for Azula without blocking own targeting |
| 3 | Redirect Lightning | yes | 1-mana redirect of the removal aimed at Azula, copied in combat |
| 4 | Rogue's Passage | yes | Unblockable Azula for the commander-damage line |
| 5 | Bender's Waterskin | yes | Untaps on every other player's turn: mana for held instants |
| 6 | Electro, Assaulting Battery | yes | Keeps red mana across steps and adds R per instant cast |
| 7 | Hidden Footblade | base only | Flash haste for a recast Azula; replaced by Stormcatch Mentor at step 7 |
| 8 | Horizon Stone | no | 5 mana for mana retention that Ozai, Ashling and The Last Agni Kai already give |
| 9 | Combustion Man | no | 5-mana attacker with no spell synergy |
| 10 | Labyrinth Adversary | no | Removes a blocker, but My Precious and Rogue's Passage do it better |
| 11 | Secret Tunnel | no | Colorless; its unblockable needs two creatures of a shared type for 4 |
| 12 | The Stasis Coffin | no | Protects the player, not Azula |
| 13 | Mindslaver | no | 10 mana in total and a Layer A review flag |

All 8 Azula-only locked cards are in every step (Royal Assassin, Imprisoned in the Moon, Aether
Gale, Torrential Gearhulk, Ozai, Octopus Form, Frostcliff Siege, Assassin Gauntlet).

## Wishlist (not in the pool, so not priced; do not build on them)
| Card | Role | Would replace | Why |
|---|---|---|---|
| Infernal Grasp | removal | Hero's Downfall | 2-mana instant unconditional kill; copy kills a second creature |
| Snuff Out | removal | Bitter Triumph | Free with a Swamp; copied for a second kill |
| Pongify | removal | Heartless Act | 1 mana; the copy kills a second creature |
| Rapid Hybridization | removal | Go for the Throat | Same as Pongify |
| Fire Covenant | removal / wipe | Toxic Deluge | The copy keeps X without paying life: two one-sided instant sweeps |
| Kolaghan's Command | removal / value | Electrolyze | Two modes, repeated by the copy with new targets |
| Mana Drain | counter / ramp | Arcane Denial | Hard counter that refunds mana |
| Force of Negation | counter | An Offer You Can't Refuse | Free on opponents' turns |
| Flusterstorm | counter | Negate (base) | 1 mana; stops the removal spell aimed at Azula |
| Mana Leak | counter | It'll Quench Ya! (base) | Cheaper soft counter |
| Tishana's Tidebinder | counter | An Offer You Can't Refuse | Flash; counters abilities; the token copy counters a second |
| Ertai Resurrected | removal / counter | Bitter Triumph | Flash; the token copy gives a second kill or counter |
| Venser, Shaper Savant | tempo | Electrolyze | Flash bounce of a spell or permanent, twice in combat |
| Fact or Fiction | card advantage | Opt | The copy is a second 5-card split |
| Commence the Endgame | card advantage | Brainstorm | Can't be countered; copy draws 2 more and amasses again |
| Mystic Remora | card advantage | Consider (base) | Cheap early draw engine |
| Rhystic Study | card advantage (Game Changer) | Opt | Strongest passive draw; first Game Changer slot |
| Archmage of Runes | reducer / draw | Goblin Electromancer | Reduces instants and sorceries and draws on each cast |
| Baral, Chief of Compliance | reducer | Goblin Electromancer | Reducer plus loot on each counter |
| Spellseeker | tutor | Lo and Li (base) / Waterlogged Teachings | Finds Narset's Reversal, Frantic Search or Deadly Dispute on a body |
| Merchant Scroll | tutor | Waterlogged Teachings | 2 mana; finds a blue instant (Narset's Reversal, Frantic Search, Counterspell) |
| Solve the Equation | tutor | Mystical Teachings | Finds any instant or sorcery (Exsanguinate too) |
| Goldspan Dragon | ramp / threat | Black Waltz No. 3 | Haste flyer; Treasures on attack and when targeted, worth 2 mana each |
| Roaming Throne | engine | Leyline of Anticipation | Naming Human doubles Azula's copy and firebending for every spell |
| Kessig Flamebreather | win condition | Thermo-Alchemist (base) | Cheap burn payoff per noncreature spell |
| Anger of the Gods | wipe | Blasphemous Act | 3 damage: spares Azula (toughness 4) |
| Plaza of Heroes | land / protection | Exotic Orchard | Any color for Azula and can give her hexproof and indestructible |
| Mana Confluence | land | Exotic Orchard | Untapped any-color land that does not depend on the opponents' lands |
