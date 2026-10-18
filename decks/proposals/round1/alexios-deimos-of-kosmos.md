# Alexios, Deimos of Kosmos: purchase ladder (Phase 8 step 2, 2026-10-18)

Ladder: `decks/proposals/alexios-deimos-of-kosmos.ladder.txt` (free base + 47 swaps). Checked with
`python -I -X utf8 scripts/ladder.py decks/proposals/alexios-deimos-of-kosmos.ladder.txt`: every step valid
(100 cards, Layer A floor 1 for steps 0-8 and 3 from step 9 at target 3, 0 Game Changers until step 47 and 1
(Gamble) there, 0 extra-turn cards, every purchase with stock > 0 in the pool). Prices: `merged-20261017T2337Z.json`
(a hint; stock is verified in Phase 9). Power figures below are judgments, not measurements.

| Checkpoint (cap CLP) | Last step | Cost CLP | Stores |
|---|---|---|---|
| 0 | 0 (base) | 0 | 0 |
| 25,000 | 13 | 24,910 | 5 (cardnexus, lacomarca, magic4ever, oasis, paytowin) |
| 50,000 | 25 | 49,422 | 6 (+ gameofmagic) |
| 75,000 | 34 | 73,922 | 6 |
| 100,000 | 38 | 94,962 | 6 |
| 150,000 | 44 | 145,372 | 6 |
| 200,000 | 47 | 199,562 | 6 |

Final step: 47 cards bought, 27 owned cards plus the commander, 25 Mountains. The 6 stores are the same 6 as the Azula
ladder (assumed shipping 30,000 CLP, outside the budget). Single-store cards fix their store: Beamtown Beatstick
(lacomarca), Koth (magic4ever), Jeska (paytowin). Consolidation: oasis sells only Reckless Handling, Tyrite Sanctum
and Brotherhood Regalia here; cardnexus has them for +7,970 CLP in total, so dropping oasis pays only if Azula
also leaves it.

## Strategy and engine
Alexios is a free, self-propelled clock: every player controls it on their own turn, it must attack, it can
never attack the owner, and it grows +1/+1 at every upkeep. Equipment and Auras stay on it when it changes
hands and their triggers stay the owner's (rules check R1, R3, R6 confirmed). So the deck suits it up on the
owner's turn and collects 4 attacks per round of Treasures, lands and cards, while damage multipliers turn
those attacks into lethal commander damage to whichever opponent it hits. The Helm of the Host package adds an
army of Alexios copies (non-legendary, they never attack the owner either) and the combo finish.

| Piece | Cards | Why they must be together |
|---|---|---|
| Alexios connects and survives | Swiftfoot Boots, Champion's Helm, Darksteel Plate, Tyrite Sanctum (indestructible counter), Brotherhood Regalia, Return the Favor, Rogue's Passage | Every engine card is blank without Alexios attacking; indestructible matters because the opponent who controls Alexios can target it on their own turn (hexproof and ward do not stop them) |
| Attack payoffs (every player's turn) | Shiny Impetus, Sword of the Animist, Beamtown Beatstick, Mask of Memory, Infiltration Lens, The Spear of Leonidas | 4 attacks per round: about 4 Treasures, 4 lands and 8 looted cards per round from three cheap pieces |
| Damage multipliers | Two-Handed Axe, Lizard Blades / Spear (double strike), Genji Glove, Kediss, Jeska | Commander damage counts whoever controls Alexios (R4): a 7-power Alexios with Axe and double strike deals 28 in one hit |
| Combo and tutors | Helm of the Host, Godo, Akki Battle Squad, Sword of Hearth and Home, Anger; Reckless Handling, Gilgamesh, Gamble | Godo puts Helm (or the Sword) straight onto the battlefield; Gilgamesh does the same from the top six |
| Discard synergy | Mask of Memory, Spear (Revelation), Faithless Looting, Unexpected Windfall -> Inti, Anger | Mask's discards become Inti impulse draws and bin Anger (team haste) |

Combo lines Layer A allows (Spellbook bulk, local; all late, floor 3, or three cards):
1. **Godo + Helm of the Host** (two cards, 10 MV, floor 3, from step 9): Godo enters and puts Helm onto the
   battlefield; equip Helm to Godo (5); each combat a hasty Godo token attacks for the first time, untaps and adds
   a combat; Helm triggers again at that combat's start: unbounded combats and tokens on the owner's turn.
2. **Akki Battle Squad + Helm of the Host** (two cards, 10 MV, floor 3, from step 34): each Akki token's
   once-per-turn trigger is new, so every combat adds another.
3. **Akki Battle Squad + Sword of Hearth and Home** (two cards, 9 MV, floor 3, from step 45): Alexios is
   modified (counters), carries the Sword, hits, blinks Akki, Akki's trigger resets: one more combat per hit.
4. **Godo + Sword of Hearth and Home + Anger** (three cards, no floor, from step 45): the Sword blinks Godo, Anger
   gives the new Godo haste, it re-tutors an Equipment and its "first time" trigger resets.
Without the combo: Overpowering Attack (extra combat for 3 after Alexios connects), Genji Glove, Akki's extra
combat, and Chandra's Ignition (Alexios's power to every other creature and every opponent) close games.

Rules notes: Helm, Kediss, Inti's attack trigger, Labyrinth Adversary and Overpowering Attack work only on the
owner's turn; Genji Glove gives the active opponent an extra combat on their turn too (only their untapped
creatures can join); Swiftfoot Boots' hexproof also stops the owner targeting Alexios on opponents' turns
(Rogue's Passage, Towering Viewpoint); Jeska's 0 is used on the owner's turn and lasts through every opponent's
turn. Traps kept out: Sword of Fire and Ice and Sword of War and Peace (protection from red knocks off Shiny
Impetus and stops Beatstick, Axe, Spear and Lizard Blades), Aggravated Assault (early two-card loops with
Sword of Feast and Famine, Neheb, Magda: floor 4), Kiki-Jiki, Combat Celebrant, Reaver Cleaver and Sticky
Fingers (they pay the opponent), Errantry (attack-alone stops Godo's combo).

## Roles
| Role | Base (step 0) | Final (step 47) |
|---|---|---|
| Lands | 36 untapped: 32 Mountain, Rogue's Passage, Buried Ruin, Abstergo Entertainment, Secret Tunnel | 35: 25 Mountain, Rogue's Passage, Buried Ruin, Abstergo, War Room, Castle Embereth, Tyrite Sanctum, Sokenzan, Spinerock Knoll (tapped), Myriad Landscape (tapped), Shatterskull Smashing (MDFC) |
| Ramp | 8: Sol Ring, Arcane Signet, Mind Stone, Commander's Sphere, Bender's Waterskin, Pristine Talisman, Burnished Hart, Foundry Inspector | 12: Sol Ring, Arcane Signet, Mind Stone, Fellwar Stone, Thought Vessel, Bender's Waterskin, Freya Crescent, Koth, Sword of the Animist, Shiny Impetus, Beamtown Beatstick, Mana Geyser |
| Card advantage | 11 weak: Faithless Looting, Wrenn's Resolve, Cathartic Reunion, Zuko Exiled Prince, Blazing Crescendo, Neonate's Rush, Solstice Revelations, Energybending, Brainstone, Mishra's Bauble, Yuyan Archers (plus Clues) | 11 + 4 tutors: Mask of Memory, Spear, Infiltration Lens, Unexpected Windfall, Magus of the Wheel, Count on Luck, Inti, Faithless Looting, Wrenn's Resolve, Zuko Exiled Prince, Solstice Revelations; Reckless Handling, Gilgamesh, Godo, Gamble (plus War Room) |
| Interaction | 15: 13 removal (Chaos Warp, Abrade, Misthios's Fury, Lava Coil, Explosive Shot, Zuko's Offense, Lightning Strike, Firebending Lesson, Bumi Bash, Command the Storm, Zuko's Exile, Glassworks, Origin of the Hidden Ones), Combustion Man, Blasphemous Act | 13 + MDFC: Lightning Bolt, Wild Magic Surge, Chaos Warp, Abrade, Misthios's Fury, Lava Coil, Explosive Shot, Zuko's Exile, Vandalblast, Pyroblast, Untimely Malfunction, 2 wipes (Chandra's Ignition, Blasphemous Act); Shatterskull, Combustion Man |
| Protection | 8 weak Equipment (Swiftfoot Boots, Champion's Helm, Haunted Cloak, Hidden Footblade, Mechanical Glider, Cobbled Wings, Kitesail, Quick-Draw Katana) | 6: Swiftfoot Boots, Champion's Helm, Darksteel Plate, Brotherhood Regalia, Return the Favor, Hidden Footblade (plus Tyrite Sanctum) |
| Win conditions | Alexios commander damage with pumps (Turn Inside Out, Cunning Maneuver, Iroh, Tunnel of Hate, Most Valuable Slayer, Ty Lee, Labyrinth Adversary); pings (Fire Nation Archers, Reckless Fireweaver); no combo | 10: Helm, Akki, Sword of Hearth and Home, Anger (4 combo lines with Godo), Two-Handed Axe, Lizard Blades, Genji Glove, Kediss, Jeska, Overpowering Attack; plus Chandra's Ignition, Reckless Fireweaver and Koth pings |
| Defense and politics | Towering Viewpoint, Treetop Freedom Fighters, Kyoshi Battle Fan, Headsplitter, Fire Nation Attacks, Zuko Avatar Hunter, Loyal Fire Sage, Fire Nation Raider | Agitator Ant, Disrupt Decorum, Towering Viewpoint, Zuko Avatar Hunter (a 2/2 per red spell), Fire Nation Archers, Labyrinth Adversary, Koth (reach) |
| Average mana value (nonland, X = 0) | 2.86 | 2.91 |

Curve (nonland cards by mana value, X = 0; Rooms counted at their combined value):
| MV | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|---|
| Base | 1 | 11 | 21 | 14 | 7 | 5 | 1 | 3 |
| Final | 0 | 10 | 22 | 14 | 7 | 7 | 3 | 1 |

## What the measured lists do that this ladder drops (luxury, not core)
The four lists (7.2-8.9; the two passing Layer A cost 790,862 and 1,064,470) share this ladder's engine: Sword of
the Animist, Beamtown Beatstick, Kediss, Brotherhood Regalia, War Room (4 of 4), Helm, Godo, Mask, Mana Geyser,
Jeska, Return the Favor, Vandalblast, Wild Magic Surge, Pyroblast, Untimely Malfunction, Chandra's Ignition, Gamble
(3 of 4). 59 of the final's 74 nonbasic cards are in at least one measured list.
| Dropped | Price CLP | Why it is luxury here |
|---|---|---|
| Sword of Feast and Famine (4 of 4) | 41,800 | Untap lands and discard per hit; a fifth of the budget for one card. Animist, Impetus and Beatstick already make the mana. First card to add above 200,000 |
| Professional Face-Breaker (4 of 4) | 12,100 (1 store) | Treasures only on the owner's turn; Impetus and Beatstick pay on every turn. Second card above 200,000 |
| Commander's Plate, Mithril Coat, Hammer of Nazahn | 40,100 / 31,700 / 14,490 | Protection: Darksteel Plate, Tyrite Sanctum's indestructible counter, Champion's Helm and Boots do it for 10,190 |
| Buster Sword, Mjölnir, Hammer of Thor, Thor, Thorin, Sword of Wealth and Power, Sword of Light and Shadow | 12,500-58,990 | Value or doubling; Two-Handed Axe, Lizard Blades, Genji Glove, Kediss and Jeska do the job for 28,660 |
| Fast mana: Ancient Tomb (GC), Lotus Petal, Mox Opal, City of Traitors, Pyretic Ritual, Seething Song, Rite of Flame, Ruby Medallion | 6,990-252,000 | Speed Commander Salt rewards, but each costs more than a whole engine piece; Mana Geyser and Treasures cover it |
| Cavern of Souls, Urza's Saga, Nykthos, Talon Gates, Valakut the Molten Pinnacle, Shinka, The Lonely Mountain, Witch's Clinic, Command Beacon, Inventors' Fair, Arena of Glory, Valakut Awakening | 9,700-55,500 | Utility lands; Mountains plus War Room, Tyrite, Sokenzan, Castle and Shatterskull. Valakut (17,930, landfall with Animist) is the best of them |
| Tibalt's Trickery, Red Elemental Blast | 19,300 / 7,190 | Extra counters; Pyroblast is kept |
| Silent Arbiter, Defense Grid, Stranglehold, Crawlspace | 8,120-15,490 | Stax names (Layer A review notes) or pure defense |
| Aggravated Assault, Kiki-Jiki, Combat Celebrant, Twinflame Tyrant, Furnace of Rath, Magda, Neheb | - | Not luxury: Bracket 4 loops (Assault with Sword of Feast and Famine, Neheb, Magda; Kiki-Jiki with Helm or Akki), or symmetric doublers |

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Shiny Impetus | 300 | Errantry (200, 1 store; skip it once Godo is in) |
| 2 | Mask of Memory | 890 | Rogue's Gloves (1,440, 1 store) |
| 3 | Beamtown Beatstick | 1,150 (1 store) | Trailblazer's Boots (3,400) |
| 4 | Koth, the Geomancer | 300 (1 store) | Spitfire Lagac (200) |
| 5 | Count on Luck | 490 | Experimental Synthesizer (650) |
| 6 | Reckless Handling | 630 | Tamiyo's Journal (2,400, 1 store) |
| 7 | Sword of the Animist | 5,890 | no equal; move Mana Geyser and Myriad Landscape up |
| 8 | Helm of the Host | 7,490 | Akki Battle Squad + Sword of Hearth and Home (21,830, the other two-card line); move them up |
| 9 | Godo, Bandit Warlord | 1,590 | Akki Battle Squad (5,840; Helm partner, move up) |
| 10 | Two-Handed Axe // Sweeping Cleave | 1,700 | Lizard Blades (3,000; move up) |
| 11 | Lightning Bolt | 1,400 | Fateful Showdown (500) |
| 12 | The Spear of Leonidas | 2,490 | Lizard Blades (3,000) |
| 13 | Anger | 590 | Hanweir Battlements (2,320) |
| 14 | Return the Favor | 1,250 | Bolt Bend (5,990, 1 store) or the owned Redirect Lightning (contested) |
| 15 | Wild Magic Surge | 1,440 | keep Bumi Bash (owned) |
| 16 | Agitator Ant | 590 | Komainu Battle Armor (5,000) |
| 17 | Castle Embereth | 500 | keep the Mountain |
| 18 | Freya Crescent | 742 | Iron Myr (1,200) |
| 19 | Unexpected Windfall | 2,200 | Seize the Spoils (250) |
| 20 | Gilgamesh, Master-at-Arms | 2,600 | Raubahn, Bull of Ala Mhigo (1,000; free attach, not a tutor) |
| 21 | Fellwar Stone | 1,490 | Cursed Mirror (490) |
| 22 | Mana Geyser | 2,090 | Blazing Firesinger // Seething Song (690, 1 store) |
| 23 | Overpowering Attack | 2,100 | keep Ticket Booth // Tunnel of Hate (owned) |
| 24 | Kediss, Emberclaw Familiar | 6,800 | Spectacular Showdown (4,000; afkstore only, adds a store) |
| 25 | Tyrite Sanctum | 2,710 | keep the Mountain |
| 26 | Magus of the Wheel | 2,250 | Reforge the Soul (7,080) |
| 27 | War Room | 2,390 | Baxter Building (490) |
| 28 | Vandalblast | 3,840 | keep Firebending Lesson (owned) |
| 29 | Spinerock Knoll | 550 | Forgotten Cave (300) |
| 30 | Myriad Landscape | 1,440 | Fabled Passage (1,590) |
| 31 | Thought Vessel | 2,900 | Cursed Mirror (490) |
| 32 | Inti, Seneschal of the Sun | 2,990 | Seize the Spoils (250) |
| 33 | Infiltration Lens | 2,300 | Rogue's Gloves (1,440, 1 store) |
| 34 | Akki Battle Squad | 5,840 | Grim Reaper's Sprint (11,600, 1 store; no combo) |
| 35 | Jeska, Thrice Reborn | 7,200 (1 store) | Spectacular Showdown (4,000, afkstore) |
| 36 | Lizard Blades | 3,000 | Spectacular Showdown (4,000, afkstore) |
| 37 | Darksteel Plate | 7,480 | Lightning Greaves (6,490; equip it last, its shroud blocks later equips) |
| 38 | Sokenzan, Crucible of Defiance | 3,360 | Hanweir Battlements (2,320) |
| 39 | Pyroblast | 5,200 | Red Elemental Blast (7,190) |
| 40 | Disrupt Decorum | 5,390 | Komainu Battle Armor (5,000) |
| 41 | Genji Glove | 9,960 | Spectacular Showdown (4,000, afkstore) |
| 42 | Chandra's Ignition | 10,400 | Delayed Blast Fireball (15,000) |
| 43 | Brotherhood Regalia | 9,960 | Trailblazer's Boots (3,400) |
| 44 | Shatterskull Smashing | 9,500 | Sundering Eruption // Volcanic Fissure (6,100) |
| 45 | Sword of Hearth and Home | 15,990 | Professional Face-Breaker (12,100, 1 store; no combo) |
| 46 | Untimely Malfunction | 10,000 | Red Elemental Blast (7,190) |
| 47 | Gamble | 28,200 | Tamiyo's Journal (2,400) or Professional Face-Breaker (12,100) plus Command Beacon (11,100) |

## The three swaps that matter most
| Swap | CLP | What the deck loses without it |
|---|---|---|
| Helm of the Host (step 8, with Godo at 9: 9,080 together) | 7,490 | The only win path before step 34 that Commander Salt can see as a combo (the base has none), and the Alexios-copy army; without it the deck is a single-threat voltron that dies to one removal spell |
| Sword of the Animist (step 7) | 5,890 | A land on each of 4 attacks per round: the ramp that pays Helm's equip 5, Godo and Genji; with Koth each one is also a ping to every opponent and an extra R |
| Mask of Memory (step 2) | 890 | The card engine: 2 cards per hit on every player's turn; mono-red has no other repeatable draw this cheap, and its discards feed Inti and Anger |

## Owned cards another deck may also want
Read from the three ladders as written on 2026-10-18 (Azula 47 swaps, Toph 27 swaps, this one 47).
| Card | Copies owned | Held by the other ladders | Substitute here (CLP) |
|---|---|---|---|
| Sol Ring | 2 | Azula and Toph, every step | buy a third (1,900): no substitute |
| Arcane Signet | 2 | Azula and Toph, every step | buy a third (890) or Iron Myr (1,200) |
| Rogue's Passage (locked) | 2 | Azula and Toph, every step | buy a third (742) |
| Mind Stone | 1 | Azula steps 0-33 | buy one (650) while Azula is below step 34 |
| Champion's Helm | 1 | Azula steps 0-30 | no offer in the pool; Lightning Greaves (6,490) |
| Abrade | 1 | Azula steps 0-28 | buy one (200) |
| Hidden Footblade (locked) | 1 | Azula steps 0-6 | buy one (300) |
| Bender's Waterskin (locked) | 3 | Azula and Toph, every step | none needed: the third copy is this deck's |
| Chaos Warp, Swiftfoot Boots (locked) | 2 each | Azula, every step (Toph none) | none needed |
| Blasphemous Act | 2 | Azula steps 0-36 (Toph none) | none needed |
| Base only, cut during the ladder | | Commander's Sphere (Azula 0-2), Cunning Maneuver, Firebending Lesson, Lightning Strike (2 copies each), Kyoshi Battle Fan, Barrels, Secret Tunnel (3 or 4 copies) | none needed |
So the "free" base costs 3,532 CLP of third copies (Sol Ring, Arcane Signet, Rogue's Passage) once the three
decks are built together, plus up to 1,150 (Mind Stone, Abrade, Hidden Footblade) and a Champion's Helm substitute
while Azula sits below its step 34.
Avoided on purpose: one-copy cards in the Azula final (Deflecting Swat, Big Score, Fire Nation Palace, Comet Storm,
The Last Agni Kai, Electro) or in every Toph step (Sabotender, Valakut Exploration; Elsewhere Flask at Toph steps
0-3), and Toph's current Moraug, Solemn Simulacrum, Banefire, Meteor Sword, Wayfarer's Bauble. Redirect Lightning
(2 copies, Azula final and Toph current) is not used: Return the Favor replaces it.

## Expected Commander Salt power (judgment, not a measurement)
| Point | Expected band | Reasoning |
|---|---|---|
| Base (0 CLP) | 4.4-5.1 (casual) | The commander is the whole clock; the 99 is cheap removal, weak Equipment and filler draw, no combo, no tutor, two-mana rocks only. Below the community 5.4 |
| Step 13 (24,910) | 5.8-6.4 (upgraded casual) | Impetus, Animist, Beatstick and Mask make each attack pay 4 times a round; a Spellbook combo with a tutor; Axe and Spear double the clock |
| Step 25 (49,422) | 6.2-6.8 | Gilgamesh, Windfall, Magus, Kediss, Overpowering Attack, more interaction: the friend's 6.1 is probably passed here (the most uncertain number) |
| Step 38 (94,962) | 6.6-7.1 (mid power) | Second combo line, Jeska, Lizard Blades, Darksteel Plate, Inti and Lens: redundancy in every pillar |
| Final, step 47 (199,562) | 6.9-7.4 | Four combo lines, Genji, Ignition, Regalia, a GC tutor. Below the measured 7.5 list (790,862), which adds Sword of Feast and Famine, Sword of Fire and Ice, Commander's Plate, Mithril Coat, Buster Sword, Jeska's Will and premium lands |
Measure steps 13, 25 and 47 first; if step 13 already clears 6.1, the order of steps 14-25 matters little.

## Free locked cards (red or colorless), ranked by fit
| Rank | Card | In the final? | Why |
|---|---|---|---|
| 1 | Swiftfoot Boots | yes | Haste and hexproof for Alexios, equip 1 |
| 2 | Rogue's Passage | yes | Unblockable Alexios on any turn |
| 3 | Bender's Waterskin | yes | Mana on every player's turn for Passage, War Room and Archers |
| 4 | Hidden Footblade | yes | Flash haste for a recast Alexios; an Equipment for Godo, Gilgamesh and Misthios's Fury |
| 5 | Labyrinth Adversary | yes | Owner-turn attack trigger stops a blocker |
| 6 | Combustion Man | yes | Removal on attack (owner's turn) or 5 damage |
| 7 | Redirect Lightning | no | Good protection, but both copies are wanted by Azula and Toph; Return the Favor does it |
| 8 | Secret Tunnel | base only (out at 27) | Colorless; unblockable for Alexios plus another Human for 4 |
| 9 | The Stasis Coffin | no | Protects the owner, who has no blockers; Toph uses it |
| 10 | Deflecting Swat | no | Free only on the owner's turn; Azula copies it |
| 11 | Electro, Assaulting Battery | no | Few instants here |
| 12 | Horizon Stone | no | Mana retention the deck does not need |
| 13 | Mindslaver | no | 6 + 2 mana and a Layer A review flag |

## Wishlist (not priced in the pool; do not build on them)
| Card | Role | Would replace | Why |
|---|---|---|---|
| Jeska's Will (GC; pool, no offer) | ramp / draw | Mana Geyser | Both modes while the owner controls Alexios: mana plus 3 impulse cards for 3 |
| Brass Squire (pool, no offer) | equip | Freya Crescent | Free attach of any Equipment on the owner's turn; 3 of 4 lists |
| Pip-Boy 3000 (pool, no offer) | value per attack | Infiltration Lens | Loot, untap two lands or a counter on every attack, any turn |
| The Sound of Drums (pool, no offer) | multiplier | Lizard Blades | Aura that stays: doubles combat damage on every player's turn |
| Wheel of Fortune (pool, no offer) | refill | Magus of the Wheel | Same wheel, cheaper to cast and harder to answer |
| Maximus, Knight Apparent (pool, no offer) | tutor | Gamble | Finds Animist, Mask or Beatstick on a body, no Game Changer slot |
| Goldvein Pick | ramp | Fellwar Stone | Treasure per hit for equip 1, any turn |
| Prying Blade | ramp | Thought Vessel | Treasure per hit, any turn |
| Bitterthorn, Nissa's Animus | ramp | Solstice Revelations | Second Sword of the Animist |
| Tome of Legends | draw | Count on Luck | Page counter on every Alexios attack under any controller |
| Embercleave | multiplier | Lizard Blades | Flash double strike and trample, cheap with attackers |
| Umezawa's Jitte | removal / pump | Explosive Shot | Two counters per hit, every turn |
| Argentum Armor | removal | Zuko's Exile | Destroys a permanent on every Alexios attack, every turn |
| Fury | removal | Lava Coil | Free evoke removal split across creatures |
| Fiery Confluence | removal / wipe | Blasphemous Act | Flexible wipe that spares a grown Alexios, or burn, or artifacts |
| Anger of the Gods | wipe | Blasphemous Act (contested) | 3-damage exile sweep that Alexios survives |
| Trumpeting Carnosaur | value / removal | Combustion Man | Discover 5 on cast, removal from hand |
| Seasoned Pyromancer | draw | Zuko, Exiled Prince | Filters dead cards into tokens |
| Outpost Siege | draw | Wrenn's Resolve | An extra card every upkeep for the whole game |
| Moonsilver Spear | defense | Towering Viewpoint | An untapped 4/4 Angel for the owner on every Alexios attack |
| Rite of the Raging Storm | politics | Reckless Fireweaver | Each opponent's 5/1 cannot attack the owner, like Alexios |
| Vengeful Ancestor | politics | Disrupt Decorum | Repeatable goad that punishes the goaded |
| Grafted Wargear | pump | Fire Nation Archers | +3/+2 for equip 0; its sacrifice clause cannot hit Alexios |
| Lavaspur Boots | protection | Hidden Footblade (locked, keep it if no other deck takes it) | Haste and ward 1 for equip 1 |
| Goldspan Dragon | ramp / threat | Fire Nation Archers | Hasty flyer, Treasures on attack and when targeted |
