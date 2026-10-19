# Fire Lord Azula: purchase ladder, round 4 (Phase 8 step 2, 2026-10-19)

Ladder: `decks/proposals/fire-lord-azula.ladder.txt` (base + 44 swaps, up to 147,811 CLP). Checked with
`python -I -X utf8 scripts/ladder.py decks/proposals/fire-lord-azula.ladder.txt`: 0 INVALID; every step 100 cards,
Layer A floor 1 (steps 0-17) or 3 (steps 18-44: flagged late two-card lines), 0 Game Changers, 0 extra-turn cards,
0 reversible cards, every purchase with stock > 0. Prices from the refreshed pool (a hint; stock is verified in Phase 9).
No absolute power numbers: the Commander Salt measurement replaces them.

## Round 4: what changed and why
Round 3 measured flat: 7.1 from 49,592 to 98,862 CLP and 7.2 at 148,712, with Salt's ceiling text "wincon combos with
no tutors" (cap -0.21 to -0.35) or "sparse slow combo package". Manabase Quality was already 95-120 %, and 50,000 CLP of
staples (shocks, Talismans, Veyran, Onyx, Ashling, Toxic Deluge, counters) did not move the score. Toph broke the same
plateau by going from 5 to 16 legal Spellbook variants and from 2 to 10 tutors.

So round 4 keeps the cheap mana base and the core engine, and spends the rest on **win lines and tutors**:
- **Lands**: the 13 cheap untapped duals of the round-3 25k list (13,506 CLP) come first; no shocks, no slow lands.
- **Win lines**: 0 variants at 15k, 3 at 25k, 5 at 35k, 6 at 50k, 9 at 75k, 13 at 100k, 19 at 150k (local Spellbook bulk,
  every one checked inside the list). They are built on hubs that serve several lines: Dualcaster Mage (3 lines),
  Narset's Reversal (2), Helm of the Host and Sword of Hearth and Home (5), Etrata's trigger copiers (3), Aggravated
  Assault (6).
- **Tutors**: 3 owned in the free base (Loyal Inventor, Entomb, Lo and Li), then Mystical Teachings, Reckless
  Handling, Godo, Solve the Equation, Imperial Recruiter: 8 card tutors at 150k, each pointed at a line.
- **Free base**: the owned tutors Loyal Inventor and Entomb, Ritual of Soot instead of Blasphemous Act (mana value 4,
  not 9; spares Azula) and Frostcliff Siege (a piece of a Godo line) replace Escape Detection, Fists of Flame,
  Blasphemous Act and Redirect.
- **Dropped against round 3**: Blood Crypt, Steam Vents, Watery Grave, Haunted Ridge, Shipwreck Marsh, Stormcarved
  Coast, Talismans, Veyran, Professor Onyx, Ashling, Toxic Deluge, Counterspell, Arcane Denial, An Offer You Can't
  Refuse, High Fae Trickster, Leyline, My Precious, Ertai, Kolaghan's Command, Exsanguinate, Bulk Up, Dark and
  Desperate Ritual, Anger of the Gods, Invoke Calamity and the 200k extras: measured or likely plateau spend.
- Trade-off: the combo pieces are heavier, so the average mana value rises from 2.43 to 2.78; the Efficiency pillar
  was already 4x its baseline, the Wincons pillar only 1.1x.

| Checkpoint | Step | Cost CLP | Spellbook variants | Card tutors | Avg MV | What the swaps since the previous checkpoint buy |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 3 | 2.43 | free base: owned tutors, no tapped lands |
| 15,000 | 15 | 14,406 | 0 | 4 | 2.48 | 13 cheap untapped duals (Manabase Quality), Mystical Teachings, Nightscape Familiar |
| 25,000 | 18 | 24,921 | 3 | 4 | 2.48 | Narset's Reversal, Glamdring, Dualcaster Mage: lines 1-3 |
| 35,000 | 24 | 34,721 | 5 | 5 | 2.54 | Goblin Bombardment, Storm-Kiln Artist: lines 4-5; Stormcatch Mentor, Reckless Handling, Fact or Fiction, Mana Leak |
| 50,000 | 27 | 49,191 | 6 | 7 | 2.60 | Godo + Helm of the Host: line 6; Solve the Equation |
| 75,000 | 35 | 74,041 | 9 | 7 | 2.75 | Etrata, Strionic Resonator, Peter Parker's Camera, Lithoform Engine: lines 7-9; Windfall, Deadly Dispute, Black Waltz, Guttersnipe |
| 100,000 | 40 | 98,561 | 13 | 7 | 2.81 | Akki Battle Squad, Sword of Hearth and Home, Anger: lines 10-13; Infernal Grasp, Lightning Bolt |
| 150,000 | 44 | 147,811 | 19 | 8 | 2.78 | Aggravated Assault, Firebending Student, Sozin's Comet: lines 14-19; Imperial Recruiter |

Ranking rationale: each checkpoint keeps the land set that measured 95 %+ and adds what Salt said was missing. 25k and
35k should rank above round 3's 25k (same lands and core, but 3-5 lines and a tutor instead of 2 lines and "sparse"). 50k
to 150k replace the staples that measured flat with 6 to 19 lines and 7-8 tutors, which is what lifted Toph without a
ceiling. The largest uncertainty is whether Salt rewards the slow lines (Godo, Akki, Aggravated Assault) or flags them
"too slow for their pieces".

## Strategy and engine
Grixis combat spellslinger with a combo spine. Azula attacks every turn and copies every spell cast in her combat;
cheap draw and removal plus cost reducers (Glamdring on Azula, Nightscape Familiar, Stormcatch Mentor, Goblin
Electromancer) and Storm-Kiln Treasures fuel it. The deck wins through loops that tutors can find: instant loops
during Azula's combat, Dualcaster loops that need no commander, and infinite-combat lines that also give Azula a new
copy window every combat.

## Win lines
Layer A: every line is a Commander Spellbook variant from the local bulk. Lines with Azula count her as a card (3
cards, no floor). Two-card lines without her are "late" (8-10 mana; floor 3 with a note). No early two-card line, no
hazard from `data/hazards.json`.
| # | Line (exact cards) | From step | Tutors that reach it | Layer A |
|---|---|---|---|---|
| 1 | Azula + Narset's Reversal + Frantic Search | 16 | Mystical Teachings, Solve the Equation (both pieces) | 3 cards with Azula |
| 2 | Azula + Snap + Dualcaster Mage | 18 | Mystical Teachings (Dualcaster, Snap), Solve the Equation (Snap), Imperial Recruiter (Dualcaster) | 3 cards with Azula |
| 3 | Dualcaster Mage + Ember Island Production | 18 | Imperial Recruiter, Mystical Teachings (Dualcaster); Solve the Equation (Ember Island) | two cards, 8 mana: floor 3 note |
| 4 | Goblin Bombardment + Dualcaster Mage + Undying Malice | 19 | Mystical Teachings / Solve the Equation (Undying Malice), Imperial Recruiter (Dualcaster) | 3 cards |
| 5 | Azula + Narset's Reversal + Storm-Kiln Artist | 20 | Mystical Teachings, Solve the Equation (Narset's Reversal), Imperial Recruiter (Storm-Kiln) | 3 cards with Azula |
| 6 | Godo, Bandit Warlord + Helm of the Host | 26 | Godo fetches Helm on entering; Loyal Inventor, Reckless Handling (Helm) | two cards, 10 mana: floor 3 note |
| 7 | Etrata, the Silencer + Strionic Resonator + Peter Parker's Camera | 30 | Loyal Inventor, Reckless Handling (the artifacts) | 3 cards |
| 8 | Etrata + Lithoform Engine + Peter Parker's Camera | 31 | same | 3 cards |
| 9 | Etrata + Strionic Resonator + Lithoform Engine | 31 | same | 3 cards |
| 10 | Akki Battle Squad + Helm of the Host | 36 | Godo, Loyal Inventor, Reckless Handling (Helm) | two cards, 10 mana: floor 3 note |
| 11 | Godo + Sword of Hearth and Home + Frostcliff Siege | 37 | Godo fetches the Sword | 3 cards |
| 12 | Godo + Sword of Hearth and Home + Anger | 38 | Godo fetches the Sword | 3 cards |
| 13 | Akki Battle Squad + Sword of Hearth and Home | 37 | Godo, Loyal Inventor, Reckless Handling (Sword) | two cards, 9 mana: floor 3 note |
| 14-16 | Firebending Student + Aggravated Assault + Electro / The Last Agni Kai / Ozai | 42 | Imperial Recruiter (Student), Lo and Li (Ozai), Mystical Teachings and Solve the Equation (The Last Agni Kai) | 3 cards each |
| 17-19 | Sozin's Comet + Aggravated Assault + Electro / The Last Agni Kai / Ozai | 43 | Solve the Equation (Sozin's Comet, The Last Agni Kai), Lo and Li (Ozai) | 3 cards each |

Payoffs that make the loops lethal: Guttersnipe, Black Waltz No. 3, Goblin Bombardment, Comet Storm and
Electrodominance (copied X), infinite combats. Rules notes: Archmage Emeritus draws are mandatory (stop a loop before
decking); Etrata's lines need the opponent to control creatures to exile.

## Roles
| Role | Base (step 0) | 150,000 (step 44) |
|---|---|---|
| Lands | 36: 30 basics, Command Tower, Cascade Bluffs, Choked Estuary, Foreboding Ruins, Fire Nation Palace, Rogue's Passage | 36: 17 basics, the 6 owned, 13 cheap untapped duals |
| Ramp and cost reduction | 10: Sol Ring, Arcane Signet, Mind Stone, Dimir Signet, Izzet Signet, Commander's Sphere, Bender's Waterskin, Black Market Connections, Goblin Electromancer, Electro | 10: Sol Ring, Arcane Signet, Bender's Waterskin, Black Market Connections, Goblin Electromancer, Electro, Nightscape Familiar, Stormcatch Mentor, Glamdring, Storm-Kiln Artist |
| Card advantage | 10: Frantic Search, Big Score, Thrill, Brainstorm, Consider, Opt, Ponder, Abandon Attachments, Archmage Emeritus, Professor Zei | 9: Frantic Search, Big Score, Brainstorm, Consider, Opt, Archmage Emeritus, Fact or Fiction, Unexpected Windfall, Deadly Dispute |
| Tutors | 3: Loyal Inventor, Entomb, Lo and Li | 8: those 3, Mystical Teachings, Reckless Handling, Solve the Equation, Imperial Recruiter, Godo |
| Interaction | 24: 17 removal, 4 counters (Negate, It'll Quench Ya!, Get Out, Deny Entry), 3 wipes (Ritual of Soot, Aether Gale, Day of Black Sun) | 10: Terminate, Chaos Warp, The Last Agni Kai, Imprisoned in the Moon, Fatal Push, Infernal Grasp, Lightning Bolt, Ritual of Soot, Narset's Reversal, Mana Leak (plus Goblin Bombardment) |
| Protection | 6: Swiftfoot Boots, Deflecting Swat, Redirect Lightning, Octopus Form, Champion's Helm, Undying Malice | 5: the same minus Champion's Helm |
| Win lines and pieces | 0 lines; finishers Comet Storm, Electrodominance, Banefire, Unleash Fury, Ozai, Thermo-Alchemist; Snap, Ember Island Production, Frostcliff Siege, Torrential Gearhulk | 19 lines: Dualcaster Mage, Goblin Bombardment, Snap, Ember Island Production, Helm of the Host, Etrata, Strionic Resonator, Peter Parker's Camera, Lithoform Engine, Akki Battle Squad, Sword of Hearth and Home, Anger, Frostcliff Siege, Aggravated Assault, Firebending Student, Sozin's Comet, Ozai; payoffs Guttersnipe, Black Waltz No. 3, Comet Storm, Electrodominance |
| Average mana value (nonland) | 2.43 | 2.78 |

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Exotic Orchard | 500 | Stormcarved Coast (3,750) |
| 2 | Sulfur Falls | 500 | Stormcarved Coast (3,750) |
| 3 | Shadowblood Ridge | 590 | Graven Cairns (5,690) |
| 4 | Shivan Reef | 690 | Stormcarved Coast (3,750) |
| 5 | Sunken Hollow | 790 | Shipwreck Marsh (2,780) |
| 6 | Darkwater Catacombs | 790 | Shipwreck Marsh (2,780) |
| 7 | Smoldering Marsh | 915 | Haunted Ridge (1,990) |
| 8 | Dragonskull Summit | 1,190 | Haunted Ridge (1,990) |
| 9 | Drowned Catacomb | 1,190 | Shipwreck Marsh (2,780) |
| 10 | Frostboil Snarl | 481 | same card at cardnexus (about 490; also drops a store) |
| 11 | Underground River | 1,990 | Shipwreck Marsh (2,780) |
| 12 | Sulfurous Springs | 2,090 | Haunted Ridge (1,990) |
| 13 | Sunken Ruins | 1,790 | Shipwreck Marsh (2,780) |
| 14 | Mystical Teachings | 450 | Solve the Equation (5,390; move it up) |
| 15 | Nightscape Familiar | 450 | Baral, Chief of Compliance (4,200) |
| 16 | Narset's Reversal | 3,400 | none in the pool (lines 1 and 5 lost); move Godo + Helm up |
| 17 | Glamdring, Foe-hammer // Gleam of Death | 915 | Tablet of Discovery (2,500) |
| 18 | Dualcaster Mage | 6,200 | none in the pool (lines 2-4 lost); move Godo + Helm up |
| 19 | Goblin Bombardment | 4,200 | none (line 4 lost); keep Thermo-Alchemist |
| 20 | Storm-Kiln Artist | 3,590 | Sedgemoor Witch (3,000; no line) |
| 21 | Stormcatch Mentor | 590 | Firebending Student (790; move it up) |
| 22 | Reckless Handling | 630 | keep Abandon Attachments (Loyal Inventor still finds artifacts) |
| 23 | Fact or Fiction | 300 | Commence the Endgame (500) |
| 24 | Mana Leak | 490 | Mana Sculpt (1,290) |
| 25 | Godo, Bandit Warlord | 1,590 | Akki Battle Squad (5,840; move it up for line 10) |
| 26 | Helm of the Host | 7,490 | Sword of Hearth and Home (15,990; move it up) |
| 27 | Solve the Equation | 5,390 | Merchant Scroll (7,850) |
| 28 | Etrata, the Silencer | 2,400 (1 store) | none (lines 7-9 lost); keep the copiers for Azula's trigger |
| 29 | Strionic Resonator | 7,800 | line 8 still stands without it; keep Abrade |
| 30 | Peter Parker's Camera | 2,600 (1 store) | line 9 still stands without it |
| 31 | Lithoform Engine | 6,960 | line 7 still stands without it; keep Banefire |
| 32 | Unexpected Windfall | 2,200 | Demand Answers (1,590, 1 store) |
| 33 | Deadly Dispute | 1,700 | Sazacap's Brew (500) |
| 34 | Black Waltz No. 3 | 490 | Sedgemoor Witch (3,000) |
| 35 | Guttersnipe | 700 | Kessig Flamebreather (7,440) |
| 36 | Akki Battle Squad | 5,840 | Kiki-Jiki, Mirror Breaker (18,500; Kiki + Helm) |
| 37 | Sword of Hearth and Home | 15,990 | none (lines 11-13 lost); keep Heartless Act |
| 38 | Anger | 590 | line 11 (Frostcliff Siege) still stands |
| 39 | Infernal Grasp | 700 | Bitter Triumph (490) |
| 40 | Lightning Bolt | 1,400 | Electrolyze (300) |
| 41 | Aggravated Assault | 29,440 | none (lines 14-19 lost); Diabolic Intent (19,580) as a tutor instead |
| 42 | Firebending Student | 790 | lines 17-19 (Sozin's Comet) still stand |
| 43 | Sozin's Comet | 4,320 | lines 14-16 (Student) still stand |
| 44 | Imperial Recruiter | 14,700 | Diabolic Intent (19,580) or Grim Tutor (28,990) |

## The three swaps that matter most
| Swap | CLP | What the deck loses without it |
|---|---|---|
| Steps 1-13, the cheap untapped duals | 13,506 | The measured mana-base lever (Manabase Quality 32 % to 95 %+) |
| Dualcaster Mage (step 18) | 6,200 | Three of the first five lines, all with owned partners (Snap, Ember Island Production, Undying Malice) |
| Godo + Helm of the Host (steps 25-26) | 9,080 | The self-tutoring infinite-combat hub that the Akki and Sword lines (10-13) build on |

## Owned cards another deck may also want
From the current Toph, Alexios and Ezio ladders in `decks/proposals/`:
| Card | Copies owned | Other decks that use it | Conflict | Substitute here (CLP) |
|---|---|---|---|---|
| Sol Ring | 2 | Toph, Alexios, Ezio | yes | buy one (1,900) |
| Arcane Signet | 2 | Toph, Alexios, Ezio | yes | buy one (890) or Everflowing Chalice (500) |
| Command Tower | 2 | Toph, Ezio | yes (3 for 2) | buy one (500) |
| Loyal Inventor | 1 | Ezio (an Assassin deck, it puts the artifact in hand there) | yes | Reckless Handling is already in from step 22; Trinket Mage or Tribute Mage (wishlist) |
| Entomb | 1 | Ezio | yes | drop it (it only counts as a tutor here) or buy one (22,400: not worth it) |
| Chaos Warp | 2 | Alexios, Ezio | yes (3 for 2) | buy one (790) |
| Swiftfoot Boots | 2 | Alexios, Ezio | yes (3 for 2) | Lightning Greaves (6,490) |
| Rogue's Passage | 2 | Alexios, Toph | yes (3 for 2) | a basic land |
| Bender's Waterskin | 3 | Toph, Alexios, Ezio | yes (4 for 3) | Fellwar Stone (1,490) |
| Terminate, Redirect Lightning | 2 each | one other deck each | no | - |
| Base only: Fatal Push, It'll Quench Ya!, Murder, Firebending Lesson, Lightning Strike | 2-4 each | Ezio or Alexios | no | - |

## Wishlist (not priced in the pool; for a later pass)
| Card | Role | Would replace | Why |
|---|---|---|---|
| Muddle the Mixture | tutor / counter | Mana Leak | transmute finds any 2-drop: Narset's Reversal, Snap, Goblin Bombardment |
| Drift of Phantasms | tutor | Stormcatch Mentor | transmute finds any 3-drop: Dualcaster Mage, Frantic Search, Sword of Hearth and Home, Aggravated Assault |
| Dimir Infiltrator | tutor | Consider | transmute finds a 2-drop; an unblockable body otherwise |
| Personal Tutor | tutor | Opt | finds Sozin's Comet, Solve the Equation or Ember Island Production |
| Trinket Mage | tutor | Loyal Inventor (if Ezio takes it) | finds Peter Parker's Camera or Sol Ring |
| Tribute Mage | tutor | Loyal Inventor (if Ezio takes it) | finds Strionic Resonator or Glamdring |
| Mystical Tutor | tutor (Game Changer) | Opt | 1-mana instant tutor for every instant piece |
| Hellkite Charger | win line | Akki Battle Squad | two more lines with Firebending Student (extra combats); hasty flyer |
| Tawnos, Urza's Apprentice | win line | Peter Parker's Camera | 2-mana copier: three more Etrata lines |
| Abstruse Archaic | win line | Lithoform Engine | copier: three more Etrata lines |
| Naru Meha, Master Wizard | win line | Fact or Fiction | flash spell copier: two lines with Ember Island Production |
| Leyline Tyrant | win line | Black Waltz No. 3 | keeps red mana: two more Aggravated Assault lines |
| Shallow Grave | win line | Undying Malice backup | another Goblin Bombardment + Dualcaster line |
