# Fire Lord Azula: purchase ladder, round 2 (Phase 8 step 2, 2026-10-18)

Ladder: `decks/proposals/fire-lord-azula.ladder.txt` (base + 46 swaps). Control: `decks/proposals/round1/`.
Checked with `python -I -X utf8 scripts/ladder.py decks/proposals/fire-lord-azula.ladder.txt`: 0 INVALID,
every step 100 cards, Layer A floor 1 (steps 0-17) or 3 (steps 18-46: flagged late two-card combo Dualcaster
Mage + Ember Island Production, 8 mana), 0 Game Changers, 0 extra-turn cards, 0 reversible cards, every
purchase with stock > 0. Prices `merged-20261017T2337Z.json` (a hint; stock is verified in Phase 9). Power
figures are judgments unless marked "measured".

## Round 2
What changed against round 1, and why:
- **No locked cards.** Kept only the former locked cards that earn a slot (table below); the base takes 6 better
  owned cards instead (Murder, Ultimate Price, Ponder, Deny Entry, Redirect, Ember Island Production).
- **No reversible cards.** Waterlogged Teachings left (steps 28+ of round 1 are now INVALID). No other card in
  either round was reversible (Glamdring and My Precious are adventures).
- **Ember Island Production (owned) + Dualcaster Mage** is a Spellbook two-card loop at 8 mana (Layer A floor 3,
  "late"): with Dualcaster the deck has 4 loops, one of them without Azula. Dualcaster moved from step 30 to 18.
  Ember Island Production also copies Azula as a non-legendary token: two attacking Azulas copy every spell twice.
- **Reordered by measured power per CLP.** Steps 1-17 bought +1.2 (measured), steps 18-31 only +0.5, steps 32-47
  +0.8 for 100,000. So the same 15-card core stays first; Electrolyze and Bitter Triumph replace the 2 lands of round-1 step 17;
  Talismans, Arcane Denial, Dark Ritual, Toxic Deluge, Onyx and An Offer move ahead of the lands; the 9 cheap
  duals move to 73,000-81,000; the 3 shocks (34,600) leave for Imperial Recruiter, Snapcaster Mage and Reliquary
  Tower (tutor and flash value over manabase polish).

| List | Left (round 1 to round 2) | Entered |
|---|---|---|
| Base (step 0) | Royal Assassin, Frostcliff Siege, Assassin Gauntlet, Hidden Footblade, Cunning Maneuver, Run Amok | Murder, Ultimate Price, Ponder, Deny Entry, Redirect, Ember Island Production |
| Final step | Ozai, Royal Assassin, Frostcliff Siege, Assassin Gauntlet, Waterlogged Teachings, Steam Vents, Watery Grave, Blood Crypt | Ember Island Production, Imperial Recruiter, Snapcaster Mage, Reliquary Tower, Consider, Island, Swamp, Mountain |

| Checkpoint | Step | Cost CLP | Expected power (judgment) | Measured round 1 at similar cost |
|---|---|---|---|---|
| 0 | 0 | 0 | 5.0-5.3 | 4.9 (step 0) |
| 25,000 | 17 | 24,295 | 6.1-6.4 | 6.1 (step 17, 24,505) |
| 50,000 | 24 | 48,905 | 6.7-7.0 | 6.6 (step 31, 49,190) |
| 75,000 | 31 | 74,345 | 7.0-7.2 | not measured (between 6.6 and 7.4) |
| 100,000 | 42 | 97,780 | 7.1-7.3 | not measured |
| 150,000 | 46 | 146,840 | 7.4-7.6 | 7.4 (step 47, 148,760) |

Every checkpoint uses 6 stores (cardnexus, gameofmagic, lacomarca, magic4ever, oasis, paytowin; assumed
shipping 30,000, outside the budget). Consolidation: in steps 1-17 lacomarca and oasis sell only Deadly Dispute,
Guttersnipe, Invoke Calamity and Mystical Teachings; buying them at cardnexus (4,490; 890), paytowin (2,400) and
gameofmagic (742) adds about 4,800 CLP of cards and drops 2 stores. Single-store cards: Veyran (gameofmagic),
Desperate Ritual (paytowin), Demand Answers (fallback only).

## Strategy and engine
Grixis combat spellslinger. Azula attacks every turn; cheap instants cast in her combat are copied (mandatory),
so removal, draw and Treasure spells are 2-for-1s. Cost reducers make them nearly free; payoffs that count every
copy turn one combat into a kill. Ways to win:
1. **Loops** (Commander Spellbook, local bulk): Azula + Narset's Reversal + Frantic Search (step 1), Azula +
   Narset's Reversal + Storm-Kiln Artist (step 2), Azula + Snap + Dualcaster Mage and Dualcaster Mage + Ember
   Island Production (step 18). Guttersnipe, Black Waltz No. 3, Onyx or a huge X spell close them. Tutors for
   them: Mystical Teachings (copied: both halves), Imperial Recruiter (Dualcaster, Storm-Kiln).
2. **Copied X spells** fed by Treasures and rituals: Comet Storm, Electrodominance, Exsanguinate (flash from High
   Fae Trickster or Leyline), Invoke Calamity re-casting them.
3. **Commander damage**: Bulk Up copied takes Azula from 4 to 16; its copied flashback makes 64.

Rules notes: Archmage Emeritus draws are mandatory (stop a loop before decking); ritual mana empties between
combat steps (only firebending mana, Electro, Ashling and The Last Agni Kai keep it); sorceries and creatures are
copied only with flash (High Fae from step 23, Leyline from step 39).

| Engine piece | Cards | Why it cannot be split |
|---|---|---|
| Azula attacks and survives | Swiftfoot Boots, My Precious, Rogue's Passage, Deflecting Swat, Redirect Lightning, Octopus Form | No attack, no copy |
| Cheap instant density | Frantic Search, Big Score, Unexpected Windfall, Deadly Dispute, Brainstorm, Opt, Consider, cheap removal | The copy is only as good as the spells cast in one combat |
| Cost reduction | Glamdring on Azula (instants cost 4 less, X included), Nightscape Familiar, Stormcatch Mentor, Goblin Electromancer | 3-6 spells per combat instead of 2 |
| Copy-counting payoffs | Storm-Kiln Artist, Archmage Emeritus, Veyran, Guttersnipe, Black Waltz No. 3 | Magecraft sees cast and copy; Veyran doubles both |
| Win path | the four loops above | Fixes the weakest pillar of the owner's report |

Kept out (Layer A or rules): Twinning Staff, Reverberate, Increasing Vengeance, Return the Favor (two-card loops
with Narset's Reversal); Hullbreaker Horror (with Sol Ring); Intruder Alarm with Joo Dee or Xerex Strobe-Knight
(both owned: early two-card infinites); Reiterate, Expansion // Explosion (self-copy loop); Twinflame, Heat
Shimmer, Saw in Half (with Dualcaster); extra-turn spells.

## Roles
| Role | Base (step 0) | Final (step 46) |
|---|---|---|
| Lands | 36: 26 basics, 10 nonbasic (4 tapped: Path of Ancestry, Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape) | 36: 18 basics, 18 nonbasic (check, battle, filter, pain lands, Exotic Orchard, Reliquary Tower; none tapped unconditionally) |
| Ramp and cost reduction | 10: Sol Ring, Arcane Signet, Mind Stone, Dimir Signet, Izzet Signet, Commander's Sphere, Bender's Waterskin, Black Market Connections, Goblin Electromancer, Electro | 15: Sol Ring, Arcane Signet, 3 Talismans, Bender's Waterskin, Black Market Connections, Dark Ritual, Desperate Ritual, Glamdring, Goblin Electromancer, Nightscape Familiar, Stormcatch Mentor, Electro, Storm-Kiln Artist |
| Card advantage | 12: Frantic Search, Big Score, Thrill, Brainstorm, Consider, Opt, Ponder, Abandon Attachments, Archmage Emeritus, Escape Detection, Fists of Flame, Professor Zei | 8: Frantic Search, Big Score, Unexpected Windfall, Deadly Dispute, Brainstorm, Consider, Opt, Archmage Emeritus (plus Gleam of Death, Allure of Power, Ashling's loot, Onyx) |
| Tutors | 1: Lo and Li | 2: Mystical Teachings, Imperial Recruiter |
| Interaction | 24: 17 removal (Terminate, Heartless Act, Go for the Throat, Fatal Push, Ultimate Price, Hero's Downfall, Murder, Deadly Derision, Chaos Warp, Lightning Axe, Abrade, Lightning Strike, The Last Agni Kai, Firebending Lesson, Roku's Mastery, Amphibian Downpour, Imprisoned in the Moon), 4 counters (Negate, It'll Quench Ya!, Get Out, Deny Entry), 3 wipes (Blasphemous Act, Aether Gale, Day of Black Sun) | 16: 10 removal (Lightning Bolt, Terminate, Heartless Act, Go for the Throat, Hero's Downfall, Bitter Triumph, Chaos Warp, Electrolyze, The Last Agni Kai, Imprisoned in the Moon), 4 counters (Narset's Reversal, Counterspell, Arcane Denial, An Offer You Can't Refuse), 2 wipes (Toxic Deluge, Aether Gale), plus Ashling's sweep |
| Protection | 7: Swiftfoot Boots, Deflecting Swat, Redirect Lightning, Octopus Form, Champion's Helm, Undying Malice, Redirect | 5: Swiftfoot Boots, Deflecting Swat, Redirect Lightning, Octopus Form, My Precious |
| Win conditions | 6: Comet Storm, Electrodominance, Banefire, Unleash Fury, Ozai, Thermo-Alchemist (no loop) | 9 + 4 loops: Comet Storm, Electrodominance, Exsanguinate, Invoke Calamity, Bulk Up, Guttersnipe, Black Waltz No. 3, Professor Onyx, Ashling |
| Engines and value | 3: Torrential Gearhulk, Snap, Ember Island Production | 8: Veyran, Torrential Gearhulk, Snap, Ember Island Production, Dualcaster Mage, High Fae Trickster, Leyline of Anticipation, Snapcaster Mage |
| Average mana value (nonland, X = 0) | 2.51 | 2.65 |

| MV | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|
| Base | 12 | 28 | 14 | 3 | 3 | 2 | 1 |
| Final | 9 | 25 | 15 | 9 | 3 | 2 | 0 |

## Former locked cards: kept only where they earn the slot
| Card | Round 2 | Why |
|---|---|---|
| Deflecting Swat | every step | Free while Azula is out; copied, it redirects two spells |
| Swiftfoot Boots | every step | Haste and hexproof without blocking own targeting |
| Redirect Lightning | every step | 1-mana redirect of removal aimed at Azula |
| Rogue's Passage | every step | Unblockable Azula for commander damage |
| Torrential Gearhulk | every step | Flash; the token copy re-casts a second instant |
| Octopus Form | every step | 1-mana hexproof and untap |
| Imprisoned in the Moon | every step | Answers any creature, commander or utility land |
| Aether Gale | every step | Bounces 6 permanents; 12 when copied with flash |
| Bender's Waterskin | every step | Mana on every opponent's turn for held instants |
| Electro, Assaulting Battery | every step | Keeps red mana; R per instant cast |
| Ozai, the Phoenix King | steps 0-42 | Firebending 4 and mana retention, but a 6-drop; Ashling replaces it |
| Royal Assassin, Frostcliff Siege, Assassin Gauntlet, Hidden Footblade | dropped | Creature or aura effects with little spell synergy; owned instants do more |
| Horizon Stone, Combustion Man, Labyrinth Adversary, Secret Tunnel, The Stasis Coffin, Mindslaver | dropped | No fit (as in round 1) |

## What the measured top lists do that this ladder drops (luxury, not core)
| Dropped | Price CLP | Why it is luxury here |
|---|---|---|
| Game Changers: Cyclonic Rift, Orcish Bowmasters, Vampiric / Demonic Tutor, The One Ring, Fierce Guardianship, Ancient Tomb, Gamble | 28,200-124,000 each | Each costs a fifth or more of the ladder; round 1 reached 7.4 with none. Cyclonic Rift or Gamble is the first candidate above 150,000 |
| Enduring Curiosity | 116,560 | Archmage, Windfall and Deadly Dispute copied do the job |
| Shocks, fetches, Training Center, Morphic Pool, Luxury Suite, Xander's Lounge, Verges | 10,900-44,320 each | Check, battle, filter and pain lands at 500-2,090 give untapped duals |
| Seething Song, Cabal Ritual, Culling the Weak | 9,900-18,490 | Two rituals plus Storm-Kiln Treasures are enough |
| Borne Upon a Wind, Vedalken Orrery, Valley Floodcaller | 11,300-17,990 (Floodcaller: no stock) | High Fae Trickster and Leyline give flash |
| Swan Song, Deadly Rollick, Untimely Malfunction, Fated Firepower, Crackle with Power, Wan Shi Tong, Vivi's Persistence | 10,000-69,990 | Premium versions of roles already filled |
| Brotherhood Regalia, Silver Shroud Costume, Winged Boots, Hammer of Nazahn | 7,570-14,490 | My Precious gives hexproof and unblockable for 2,350 |
| Twinning Staff, Reverberate, Hullbreaker Horror, Return the Favor, Isochron Scepter, Waterlogged Teachings | - | Not luxury: Bracket 3 hazards here, or reversible |

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Narset's Reversal | 3,400 | Dualcaster Mage (6,200; move it up: two loops with owned cards) |
| 2 | Storm-Kiln Artist | 3,590 | Sedgemoor Witch (3,000) |
| 3 | Glamdring, Foe-hammer // Gleam of Death | 915 | Tablet of Discovery (2,550) |
| 4 | Nightscape Familiar | 450 | Rakdos Signet (450) |
| 5 | Stormcatch Mentor | 590 | Firebending Student (790) |
| 6 | Unexpected Windfall | 2,200 | Demand Answers (1,590, 1 store) |
| 7 | Deadly Dispute | 1,650 | Sazacap's Brew (500) |
| 8 | Invoke Calamity | 900 | Prismari Command (915) |
| 9 | Guttersnipe | 700 | Professor Onyx (5,410; move it up) |
| 10 | Black Waltz No. 3 | 490 | Sedgemoor Witch (3,000) |
| 11 | Mystical Teachings | 450 | keep Lo and Li (owned) |
| 12 | Lightning Bolt | 1,400 | Withering Torment (2,090) |
| 13 | Veyran, Voice of Duality | 5,480 (1 store) | Wizard's Staff (7,650) |
| 14 | Exsanguinate | 890 | keep Banefire (owned) |
| 15 | Bulk Up | 400 | Temur Battle Rage (450) |
| 16 | Electrolyze | 300 | Prismari Command (915) |
| 17 | Bitter Triumph | 490 | Sheoldred's Edict (2,200) |
| 18 | Dualcaster Mage | 6,200 | Shore Up (300; no loop) |
| 19 | Counterspell | 3,300 | Mana Sculpt (1,290) |
| 20 | Talisman of Dominance | 2,290 | Fellwar Stone (1,490) |
| 21 | Talisman of Creativity | 2,490 | Rakdos Signet (450) |
| 22 | Talisman of Indulgence | 2,490 | Rakdos Signet (450) or Fellwar Stone (1,490) |
| 23 | High Fae Trickster | 5,000 | Leyline of Anticipation (5,600; move it up) |
| 24 | Arcane Denial | 2,840 | Mana Sculpt (1,290) |
| 25 | My Precious // Allure of Power | 2,350 | Lightning Greaves (6,490) |
| 26 | Dark Ritual | 4,990 | Pyretic Ritual (6,990) |
| 27 | Toxic Deluge | 7,790 | keep Blasphemous Act (owned) |
| 28 | Professor Onyx | 5,410 | Sedgemoor Witch (3,000) |
| 29 | An Offer You Can't Refuse | 3,900 | Mana Sculpt (1,290) |
| 30 | Sulfur Falls | 500 | Temple of Epiphany (490) |
| 31 | Exotic Orchard | 500 | Rupture Spire (200) |
| 32 | Shivan Reef | 690 | Temple of Epiphany (490) |
| 33 | Sunken Hollow | 790 | Shipwreck Marsh (2,780) |
| 34 | Darkwater Catacombs | 790 | Sunken Ruins (1,790) |
| 35 | Shadowblood Ridge | 590 | Temple of Malice (owned) |
| 36 | Smoldering Marsh | 915 | Haunted Ridge (1,990) |
| 37 | Dragonskull Summit | 1,190 | Haunted Ridge (1,990) |
| 38 | Drowned Catacomb | 1,190 | Temple of Deceit (owned) |
| 39 | Leyline of Anticipation | 5,600 | Emergence Zone (4,490) |
| 40 | Desperate Ritual | 7,600 (1 store) | Pyretic Ritual (6,990) |
| 41 | Underground River | 1,990 | Sunken Ruins (1,790) |
| 42 | Sulfurous Springs | 2,090 | Haunted Ridge (1,990) |
| 43 | Ashling, Flame Dancer | 15,490 | Sedgemoor Witch (3,000) |
| 44 | Imperial Recruiter | 14,700 | keep Ponder (owned) |
| 45 | Snapcaster Mage | 13,870 | keep Amphibian Downpour (owned) |
| 46 | Reliquary Tower | 5,000 | keep the Island |

## The three swaps that matter most
| Swap | CLP | What the deck loses without it |
|---|---|---|
| Narset's Reversal (step 1) | 3,400 | The win path until step 18: without it the list is the "casual stall shell" again (bracket 2, no loop) |
| Storm-Kiln Artist (step 2) | 3,590 | The mana engine (2 Treasures per instant in combat) and the second loop |
| Glamdring (step 3) | 915 | On Azula every instant costs 4 less: 4-6 spells per combat instead of 2-3, and 4 more points of X |

## Owned cards another deck may also want
From the current Toph and Alexios ladders in `decks/proposals/`:
| Card | Copies owned | Decks that use it | Conflict | Substitute here (CLP) |
|---|---|---|---|---|
| Sol Ring | 2 | Toph, Alexios, Azula | yes (3 for 2) | buy a third (1,900) |
| Arcane Signet | 2 | Toph, Alexios, Azula | yes | buy one (890) or Fellwar Stone (1,490) |
| Rogue's Passage | 2 | Toph, Alexios, Azula | yes | buy one (742); My Precious covers it from step 25 |
| Mind Stone | 1 | Alexios, Azula (steps 0-21) | yes | Rakdos Signet (450) |
| Commander's Sphere | 1 | Alexios, Azula (steps 0-2) | yes | Rakdos Signet (450) |
| Champion's Helm | 1 | Alexios, Azula (steps 0-24) | yes | Shore Up (300) |
| Abrade | 1 | Alexios, Azula (steps 0-22) | yes | Electrolyze (300) |
| Bender's Waterskin | 3 | Toph, Alexios, Azula | no | - |
| Command Tower, Redirect Lightning, Evolving Wilds, Vibrant Cityscape | 2 each | Toph, Azula | no | - |
| Swiftfoot Boots, Chaos Warp, Blasphemous Act, Firebending Lesson, Lightning Strike | 2 each | Alexios, Azula | no | - |
| Deflecting Swat, Big Score | 1 each | only Azula now | no | Bolt Bend (5,990) / Sazacap's Brew (500) if another deck takes them |

## Expected Commander Salt power (judgment; calibrated on the round-1 measurements)
| Checkpoint | Expected | Reasoning |
|---|---|---|
| 0 | 5.0-5.3 | Round-1 base measured 4.9; six weak creature and aura slots become efficient owned instants and a combo half. Still bracket 2 (no loop, one tutor) |
| 25,000 | 6.1-6.4 | The measured round-1 core (6.1 at 24,505) with cheap removal and finishers instead of 2 lands, on a better base |
| 50,000 | 6.7-7.0 | Four loops (Dualcaster), Talismans, High Fae, two hard counters; round 1 spent this band on lands and got +0.5 |
| 75,000 | 7.0-7.2 | My Precious, Dark Ritual, Toxic Deluge, Onyx, An Offer: the spells that round 1 bought only after 50,000 |
| 100,000 | 7.1-7.3 | Untapped manabase, Leyline, Desperate Ritual |
| 150,000 | 7.4-7.6 | Ashling, a second tutor and Snapcaster on top; round 1 measured 7.4 here with shocks instead |

Watch the bracket star: Layer A floor is 3 from step 18 (flagged late combo); Salt marked round-1 steps 17-47 as 3*.

## Wishlist (not in the pool, so not priced; do not build on them)
**Bold** = the 12 whose price matters most (likely to enter the first 50,000-75,000 if cheap).
| Card | Role | Would replace | Why |
|---|---|---|---|
| **Infernal Grasp** | removal | Hero's Downfall | 2-mana instant unconditional kill; copy kills a second creature |
| **Snuff Out** | removal | Bitter Triumph | Free with a Swamp; copied for a second kill |
| **Pongify** | removal | Heartless Act | 1 mana; the copy kills a second creature |
| **Rapid Hybridization** | removal | Go for the Throat | Same as Pongify |
| **Fire Covenant** | removal / wipe | Toxic Deluge | The copy keeps X without paying life: two one-sided instant sweeps |
| **Kolaghan's Command** | removal / value | Electrolyze | Two modes, repeated by the copy with new targets |
| **Spellseeker** | tutor | Imperial Recruiter | Finds Narset's Reversal, Frantic Search or Deadly Dispute on a 3-drop body |
| **Merchant Scroll** | tutor | Mystical Teachings | 2 mana; finds a blue instant (Narset's Reversal, Frantic Search, Counterspell) |
| **Solve the Equation** | tutor | Imperial Recruiter | Finds any instant or sorcery, Exsanguinate included |
| **Archmage of Runes** | reducer / draw | Goblin Electromancer | Reduces instants and sorceries and draws on each cast |
| **Fact or Fiction** | card advantage | Consider | The copy is a second 5-card split |
| **Roaming Throne** | engine | Leyline of Anticipation | Naming Human doubles Azula's copy and firebending for every spell |
| Mana Drain | counter / ramp | Arcane Denial | Hard counter that refunds mana |
| Force of Negation | counter | An Offer You Can't Refuse | Free on opponents' turns |
| Flusterstorm | counter | Negate (base) | 1 mana; stops the removal spell aimed at Azula |
| Mana Leak | counter | It'll Quench Ya! (base) | Cheaper soft counter |
| Tishana's Tidebinder | counter | An Offer You Can't Refuse | Flash; counters abilities; the token copy counters a second |
| Ertai Resurrected | removal / counter | Bitter Triumph | Flash; the token copy gives a second kill or counter |
| Venser, Shaper Savant | tempo | Electrolyze | Flash bounce of a spell or permanent, twice in combat |
| Commence the Endgame | card advantage | Brainstorm | Can't be countered; copy draws 2 more and amasses again |
| Mystic Remora | card advantage | Ponder (base) | Cheap early draw engine |
| Rhystic Study | card advantage (Game Changer) | Opt | Strongest passive draw; first Game Changer slot |
| Baral, Chief of Compliance | reducer | Goblin Electromancer | Reducer plus loot on each counter |
| Goldspan Dragon | ramp / threat | Black Waltz No. 3 | Haste flyer; Treasures worth 2 mana |
| Kessig Flamebreather | win condition | Thermo-Alchemist (base) | Cheap burn payoff per noncreature spell |
| Anger of the Gods | wipe | Blasphemous Act (base) | 3 damage spares Azula (the pool had a wrong price for it) |
| Plaza of Heroes | land / protection | Exotic Orchard | Any color for Azula; can give her hexproof and indestructible |
| Mana Confluence | land | Exotic Orchard | Untapped any-color land |
