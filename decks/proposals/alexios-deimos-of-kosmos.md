# Alexios, Deimos of Kosmos: purchase ladder, round 2 (Phase 8 step 2, 2026-10-18)

Ladder: `decks/proposals/alexios-deimos-of-kosmos.ladder.txt` (free base + 48 swaps). Control: `decks/proposals/round1/`.
Checked with `python -I -X utf8 scripts/ladder.py decks/proposals/alexios-deimos-of-kosmos.ladder.txt`: all 49 steps
valid (100 cards, no reversible card, Layer A floor 1 at steps 0-1 and 3 from step 2 at target 3, 0 Game Changers until
the last step and 1 there (Gamble), 0 extra-turn cards, every purchase with stock > 0). Prices:
`merged-20261017T2337Z.json` (a hint; stock is verified in Phase 9). Power figures are judgments, not measurements.

## Round 2
| Change | Why |
|---|---|
| Shatterskull Smashing out | Modal double-faced: forbidden (it made round-1 steps 44-47 invalid) |
| Myriad Landscape and Spinerock Knoll out; Scavenger Grounds, The Mycosynth Gardens, Geier Reach Sanitarium in; War Room moved to the first 25,000 | Azula's measurements: Manabase Quality moved power more than anything (+1.4 for 7,000 CLP of untapped lands). Mono-red has no duals, so the lesson here is no tapped lands and cheap untapped utility lands early. Every land in every step is now untapped |
| Abrade, Champion's Helm, Mind Stone out of the whole ladder | Azula's round-2 ladder holds its only copy up to its steps 21-24 (about 25,000 CLP): a conflict at the budget mixes the optimizer will try |
| Labyrinth Adversary, Combustion Man, Secret Tunnel no longer kept | Not mandatory any more; weaker than the cards that replace them |
| Meteor Sword, Burnished Hart, Foundry Inspector, Haunted Cloak kept to the end | Free owned cards nobody else uses; Meteor Sword is removal when Godo or Gilgamesh put it onto the battlefield |
| Combo first: Helm and Godo are now steps 1-2; Akki (second line) moved from round-1 step 35 to step 22 (inside 50,000) | Azula's first 25,000 bought +1.2 with a combo at step 1; Salt caps "wincon combos with no tutors", so Reckless Handling (step 6) follows |
| Pyretic Ritual added (step 47) | Fast mana; in 3 of 4 measured lists |

| Cards | Left | Entered |
|---|---|---|
| Base | Abrade, Champion's Helm, Commander's Sphere, Mind Stone, Secret Tunnel | Meteor Sword, Hidden Blade, Furnace Host Charger, Ran and Shaw, 1 Mountain |
| Final | Abrade, Champion's Helm, Mind Stone, Combustion Man, Labyrinth Adversary, Myriad Landscape, Spinerock Knoll, Shatterskull Smashing | Meteor Sword, Burnished Hart, Foundry Inspector, Haunted Cloak, Pyretic Ritual, Scavenger Grounds, The Mycosynth Gardens, Geier Reach Sanitarium |

| Checkpoint (cap CLP) | Step | Cost CLP | Expected power, round 2 | Round-1 expectation (step, cost) |
|---|---|---|---|---|
| 0 | 0 | 0 | 4.6-5.2 | 4.4-5.1 |
| 25,000 | 19 | 24,822 | 5.9-6.5 | 5.8-6.4 (13, 24,910) |
| 50,000 | 25 | 49,932 | 6.3-6.9 | 6.2-6.8 (25, 49,422) |
| 75,000 | 35 | 74,362 | 6.6-7.1 | none given (34, 73,922) |
| 100,000 | 39 | 97,602 | 6.8-7.3 | 6.6-7.1 (38, 94,962) |
| 150,000 | 44 | 146,852 | 7.0-7.5 | none given (round-1 step 44 is now invalid) |
| 200,000 | 48 | 197,392 | 7.2-7.7 | 6.9-7.4 (47, 199,562; now invalid) |
Reasoning: Azula's ladder measured 4.9 / 6.1 / 6.6 / 7.4 at 0 / 25k / 50k / 149k against judgments that were right low
and conservative high, so the top bands moved up. Shaded about 0.2 below Azula at equal spend: Alexios is a weaker
commander (community average 5.4 against 7.8) and the first combo needs 11 mana. In favour: this manabase has no
tapped land at any step. Measure steps 19 and 25 first; they decide whether Alexios clears 6.1 inside 50,000.

All checkpoints use the same 6 stores as Azula (cardnexus, gameofmagic, lacomarca, magic4ever, oasis, paytowin;
assumed shipping 30,000 CLP, outside the budget). Single-store cards: Beamtown Beatstick (lacomarca), Koth
(magic4ever), Jeska (paytowin). Oasis sells only Reckless Handling, Tyrite Sanctum and Brotherhood Regalia here
(cardnexus: +7,970 CLP in total).

## Strategy and engine
Alexios is a free, self-propelled clock: every player controls it on their own turn, it must attack, it never attacks
the owner and it grows +1/+1 each upkeep. Equipment and Auras stay on it when it changes hands and their triggers stay
the owner's (rules check R1, R3, R6). So the deck suits it up on the owner's turn and collects 4 attacks per round of
Treasures, lands and cards, while damage multipliers turn each hit into lethal commander damage to some opponent. Helm
of the Host adds Alexios copies (non-legendary; they never attack the owner) and the combo finish.

| Piece | Cards | Why they must be together |
|---|---|---|
| Alexios connects and survives | Swiftfoot Boots, Darksteel Plate, Tyrite Sanctum, Brotherhood Regalia, Return the Favor, Rogue's Passage | Every engine card is blank without the attack; indestructible matters because the opponent controlling Alexios can target it on their own turn |
| Attack payoffs (every turn) | Shiny Impetus, Beamtown Beatstick, Mask of Memory, The Spear of Leonidas, Sword of the Animist, Infiltration Lens | 4 attacks a round: about 4 Treasures, 4 lands and 8 looted cards |
| Multipliers | Two-Handed Axe, Spear / Lizard Blades (double strike), Genji Glove, Kediss, Jeska | Commander damage counts whoever controls Alexios: 7 power with Axe and double strike is 28 in one hit |
| Combo and tutors | Helm, Godo, Akki Battle Squad, Sword of Hearth and Home, Anger; Reckless Handling, Gilgamesh, Gamble | Godo and Gilgamesh put Equipment straight onto the battlefield |
| Discard synergy | Mask, Spear, Faithless Looting, Windfall, Geier Reach -> Inti, Anger | Discards become impulse draws and bin Anger (team haste) |

Combo lines Layer A allows (Spellbook bulk; all late, floor 3, or three cards) and what each costs:
| Line | Pieces bought | Cost CLP | From step |
|---|---|---|---|
| Godo + Helm of the Host (two cards, 10 MV): Godo puts Helm onto the battlefield, equip 5; each hasty Godo token's first attack untaps and adds a combat, Helm makes a new token each combat | Helm 7,490, Godo 1,590 | 9,080 | 2 |
| Akki Battle Squad + Helm (two cards, 10 MV): each Akki token's once-per-turn trigger is new | Akki 5,840 | +5,840 | 22 |
| Akki + Sword of Hearth and Home (two cards, 9 MV): Alexios (modified by counters) hits, the Sword blinks Akki, its trigger resets | Sword 15,990 | +15,990 | 44 |
| Godo + Sword of Hearth and Home + Anger (three cards): the Sword blinks Godo, Anger gives it haste, its "first time" resets | Anger 590 (step 11) | +590 | 44 |
Tutors for the pieces: Godo's own ETB, Reckless Handling (step 6), Gilgamesh (24), Gamble (48). Without the combo:
Overpowering Attack, Genji Glove, Akki's extra combat and Chandra's Ignition close games.

Rules notes: Helm, Kediss, Inti's attack trigger and Overpowering Attack work only on the owner's turn; Genji Glove
also gives the active opponent an extra combat on their turn; Swiftfoot Boots' hexproof stops the owner targeting
Alexios on opponents' turns (Rogue's Passage, Towering Viewpoint); Jeska's 0 on the owner's turn lasts a full round.
Traps kept out: Sword of Fire and Ice and Sword of War and Peace (protection from red knocks off Impetus, Beatstick,
Axe, Spear, Lizard Blades), Aggravated Assault, Kiki-Jiki, Combat Celebrant (Bracket 4 loops), Reaver Cleaver and
Sticky Fingers (they pay the opponent), Errantry (attack-alone breaks the Godo line), Hanweir Battlements (meld).

## Roles
| Role | Base (step 0) | Final (step 48) |
|---|---|---|
| Lands | 36 untapped: 33 Mountain, Rogue's Passage, Buried Ruin, Abstergo Entertainment | 35 untapped: 25 Mountain, Rogue's Passage, Buried Ruin, Abstergo, Castle Embereth, Scavenger Grounds, War Room, The Mycosynth Gardens, Tyrite Sanctum, Geier Reach Sanitarium, Sokenzan |
| Ramp | 7: Sol Ring, Arcane Signet, Bender's Waterskin, Pristine Talisman, Burnished Hart, Foundry Inspector, Barrels of Blasting Jelly | 14: Sol Ring, Arcane Signet, Fellwar Stone, Thought Vessel, Bender's Waterskin, Burnished Hart, Foundry Inspector, Freya Crescent, Koth, Sword of the Animist, Shiny Impetus, Beamtown Beatstick, Mana Geyser, Pyretic Ritual |
| Card advantage | 12 weak: Faithless Looting, Wrenn's Resolve, Cathartic Reunion, Zuko Exiled Prince, Blazing Crescendo, Neonate's Rush, Solstice Revelations, Energybending, Brainstone, Mishra's Bauble, Yuyan Archers, Fire Nation Raider | 11 + 4 tutors: Mask, Spear, Infiltration Lens, Unexpected Windfall, Magus of the Wheel, Count on Luck, Inti, Faithless Looting, Wrenn's Resolve, Zuko Exiled Prince, Solstice Revelations; Reckless Handling, Gilgamesh, Godo, Gamble |
| Interaction | 14: Chaos Warp, Misthios's Fury, Lava Coil, Explosive Shot, Lightning Strike, Firebending Lesson, Bumi Bash, Command the Storm, Zuko's Exile, Zuko's Offense, Glassworks, Origin of the Hidden Ones, Combustion Man, Blasphemous Act | 13: Lightning Bolt, Wild Magic Surge, Chaos Warp, Misthios's Fury, Lava Coil, Explosive Shot, Zuko's Exile, Vandalblast, Pyroblast, Untimely Malfunction, Meteor Sword, 2 wipes (Chandra's Ignition, Blasphemous Act); plus Scavenger Grounds |
| Protection | 8 weak Equipment (Swiftfoot Boots, Haunted Cloak, Hidden Footblade, Hidden Blade, Mechanical Glider, Cobbled Wings, Kitesail, Quick-Draw Katana) | 6: Swiftfoot Boots, Darksteel Plate, Brotherhood Regalia, Return the Favor, Haunted Cloak, Hidden Footblade (plus Tyrite Sanctum) |
| Win conditions | Alexios with pumps (Turn Inside Out, Cunning Maneuver, Iroh, Tunnel of Hate, Most Valuable Slayer, Ty Lee, Labyrinth Adversary); no combo | 10: Helm, Akki, Sword of Hearth and Home, Anger (4 combo lines with Godo), Two-Handed Axe, Lizard Blades, Genji Glove, Kediss, Jeska, Overpowering Attack |
| Defense and politics | Towering Viewpoint, Treetop Freedom Fighters, Kyoshi Battle Fan, Headsplitter, Fire Nation Attacks, Zuko Avatar Hunter, Loyal Fire Sage, Fire Nation Archers, Reckless Fireweaver | 6: Agitator Ant, Disrupt Decorum, Towering Viewpoint, Zuko Avatar Hunter, Fire Nation Archers, Reckless Fireweaver |
| Average mana value (nonland, X = 0) | 3.02 | 2.94 |

Curve (nonland cards by mana value, X = 0; Rooms at their combined value):
| MV | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|---|
| Base | 1 | 11 | 20 | 12 | 7 | 6 | 2 | 4 |
| Final | 0 | 10 | 21 | 16 | 6 | 6 | 3 | 2 |

## What the measured lists do that this ladder drops (luxury, not core)
The four lists (7.2-8.9; the two passing Layer A cost 790,862 and 1,064,470) share this engine: Sword of the Animist,
Beamtown Beatstick, Kediss, Brotherhood Regalia, War Room (4 of 4), Helm, Godo, Mask, Mana Geyser, Jeska, Return the
Favor, Vandalblast, Wild Magic Surge, Pyroblast, Untimely Malfunction, Chandra's Ignition, Pyretic Ritual, Gamble (3 of 4).
| Dropped | Price CLP | Why it is luxury here |
|---|---|---|
| Sword of Feast and Famine (4 of 4) | 41,800 | Untap lands and discard per hit; a fifth of the budget for one card. First card above 200,000 |
| Professional Face-Breaker (4 of 4) | 12,100 (1 store) | Treasures only on the owner's turn; Impetus and Beatstick pay every turn |
| Commander's Plate, Mithril Coat, Hammer of Nazahn | 14,490-40,100 | Darksteel Plate, Tyrite Sanctum and Boots cover protection for 10,190 |
| Buster Sword, Mjölnir Hammer of Thor, Thor, Thorin, Swords of Wealth and Power, Light and Shadow | 12,500-58,990 | Axe, Lizard Blades, Genji, Kediss and Jeska do it for 28,660 |
| Fast mana: Ancient Tomb (GC), Lotus Petal, Mox Opal, City of Traitors, Seething Song, Rite of Flame, Ruby Medallion | 8,090-252,000 | Pyretic Ritual and Mana Geyser are kept; each of these costs more than an engine piece |
| Red fetch lands (Wooded Foothills 26,990, Bloodstained Mire 27,990, Arid Mesa 32,880), Cavern of Souls, Urza's Saga, Nykthos, Valakut the Molten Pinnacle, Command Beacon, Inventors' Fair | 11,100-55,500 | Untapped utility lands at 490-3,360 first. Open question for a measurement: whether Salt's Manabase Quality rewards fetches in a mono-color deck; if so, one Wooded Foothills is the next land to test |
| Tibalt's Trickery, Red Elemental Blast | 19,300 / 7,190 | Pyroblast is kept |
| Silent Arbiter, Defense Grid, Stranglehold, Crawlspace | 8,120-15,490 | Stax review names or pure defense |
| Aggravated Assault, Kiki-Jiki, Combat Celebrant, Twinflame Tyrant, Furnace of Rath | - | Not luxury: Bracket 4 loops or symmetric doublers |

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Helm of the Host | 7,490 | Akki Battle Squad + Sword of Hearth and Home (21,830; the line without Helm) |
| 2 | Godo, Bandit Warlord | 1,590 | Akki Battle Squad (5,840; move it up) |
| 3 | Shiny Impetus | 300 | Prized Statue (400, 1 store) |
| 4 | Mask of Memory | 890 | Rogue's Gloves (1,440, 1 store) |
| 5 | Beamtown Beatstick | 1,150 (1 store) | Trailblazer's Boots (3,400) |
| 6 | Reckless Handling | 630 | Tamiyo's Journal (2,400, 1 store) |
| 7 | Lightning Bolt | 1,400 | Fateful Showdown (500) |
| 8 | Wild Magic Surge | 1,440 | keep Bumi Bash (owned) |
| 9 | Return the Favor | 1,250 | Bolt Bend (5,990, 1 store) |
| 10 | Two-Handed Axe // Sweeping Cleave | 1,700 | Lizard Blades (3,000; move it up) |
| 11 | Anger | 590 | keep Expedite (owned) |
| 12 | Count on Luck | 490 | Experimental Synthesizer (650) |
| 13 | Koth, the Geomancer | 300 (1 store) | Spitfire Lagac (200) |
| 14 | Agitator Ant | 590 | Komainu Battle Armor (5,000) |
| 15 | Castle Embereth | 500 | Volatile Fault (490) |
| 16 | Freya Crescent | 742 | Iron Myr (1,200) |
| 17 | Scavenger Grounds | 490 | Demolition Field (742) |
| 18 | War Room | 2,390 | Baxter Building (490) |
| 19 | The Mycosynth Gardens | 890 | Volatile Fault (490) |
| 20 | The Spear of Leonidas | 2,490 | Lizard Blades (3,000) |
| 21 | Sword of the Animist | 5,890 | no equal; move Mana Geyser up |
| 22 | Akki Battle Squad | 5,840 | Grim Reaper's Sprint (11,600, 1 store; no combo) |
| 23 | Kediss, Emberclaw Familiar | 6,800 | Spectacular Showdown (4,000; afkstore only, adds a store) |
| 24 | Gilgamesh, Master-at-Arms | 2,600 | Raubahn, Bull of Ala Mhigo (1,000; free attach, not a tutor) |
| 25 | Fellwar Stone | 1,490 | Cursed Mirror (490) |
| 26 | Unexpected Windfall | 2,200 | Seize the Spoils (250) |
| 27 | Tyrite Sanctum | 2,710 | keep the Mountain |
| 28 | Geier Reach Sanitarium | 950 | Volatile Fault (490) |
| 29 | Overpowering Attack | 2,100 | keep Ticket Booth // Tunnel of Hate (owned) |
| 30 | Magus of the Wheel | 2,250 | Reforge the Soul (7,080) |
| 31 | Vandalblast | 3,840 | keep Firebending Lesson (owned) |
| 32 | Mana Geyser | 2,090 | Blazing Firesinger // Seething Song (690, 1 store) |
| 33 | Inti, Seneschal of the Sun | 2,990 | Seize the Spoils (250) |
| 34 | Infiltration Lens | 2,300 | Rogue's Gloves (1,440, 1 store) |
| 35 | Lizard Blades | 3,000 | Spectacular Showdown (4,000, afkstore) |
| 36 | Jeska, Thrice Reborn | 7,200 (1 store) | Spectacular Showdown (4,000, afkstore) |
| 37 | Darksteel Plate | 7,480 | Lightning Greaves (6,490; equip it last) |
| 38 | Pyroblast | 5,200 | Red Elemental Blast (7,190) |
| 39 | Sokenzan, Crucible of Defiance | 3,360 | Mines of Moria (4,600) |
| 40 | Thought Vessel | 2,900 | Cursed Mirror (490) |
| 41 | Untimely Malfunction | 10,000 | Red Elemental Blast (7,190) |
| 42 | Chandra's Ignition | 10,400 | Delayed Blast Fireball (15,000) |
| 43 | Brotherhood Regalia | 9,960 | Trailblazer's Boots (3,400) |
| 44 | Sword of Hearth and Home | 15,990 | Professional Face-Breaker (12,100, 1 store; no combo) |
| 45 | Genji Glove | 9,960 | Spectacular Showdown (4,000, afkstore) |
| 46 | Disrupt Decorum | 5,390 | Komainu Battle Armor (5,000) |
| 47 | Pyretic Ritual | 6,990 | Desperate Ritual (7,600, 1 store) |
| 48 | Gamble | 28,200 | Inventors' Fair (14,280) or Tamiyo's Journal (2,400) |

## The three swaps that matter most
| Swap | CLP | What the deck loses without it |
|---|---|---|
| Helm of the Host (step 1, with Godo at 2) | 7,490 (9,080 with Godo) | The only combo before step 22 and the Alexios-copy army; without it the deck is a single-threat voltron that dies to one removal spell, and Salt sees no win line |
| Mask of Memory (step 4) | 890 | The card engine: 2 cards per hit on every player's turn; its discards feed Inti and Anger |
| Shiny Impetus (step 3) | 300 | About 4 Treasures a round from the first turn Alexios attacks: the mana for equip costs and the 11-mana combo |

## Shared owned cards
Read from the current ladders (Azula round 2: 46 swaps; Toph: 27 swaps).
| Card | Copies owned | Held by the other ladders | Here |
|---|---|---|---|
| Sol Ring | 2 | Azula and Toph, every step | every step: needs a third copy (1,900) |
| Arcane Signet | 2 | Azula and Toph, every step | every step: third copy (890) |
| Rogue's Passage | 2 | Azula and Toph, every step | every step: third copy (742) |
| Bender's Waterskin | 3 | Azula and Toph, every step | the third copy is this deck's |
| Chaos Warp, Swiftfoot Boots | 2 each | Azula, every step | the second copy is this deck's |
| Blasphemous Act | 2 | Azula steps 0-26 | the second copy is this deck's |
| Lightning Strike, Firebending Lesson | 2 each | Azula, low steps | base only (out at steps 38 and 31) |
| Barrels of Blasting Jelly | 3 | Toph step 0 | base only (out at step 25) |
Third copies for the three cards: 3,532 CLP. Avoided on purpose (one copy held elsewhere): Abrade, Champion's Helm,
Mind Stone (Azula to steps 21-24), Banefire, Unleash Fury, Lightning Axe, Thermo-Alchemist (Azula low steps), Deflecting
Swat, Big Score, Comet Storm, Electro, Electrodominance, Fire Nation Palace, The Last Agni Kai (Azula, every step),
Sabotender, Valakut Exploration, Solemn Simulacrum, The Stasis Coffin, Wayfarer's Bauble (Toph, every step), Moraug
(Toph steps 0-17), Elsewhere Flask (Toph 0-3), Redirect Lightning (both copies held).

## Wishlist (not priced in the pool; do not build on them). * = the 12 whose price matters most
| Card | Role | Would replace | Why |
|---|---|---|---|
| * Jeska's Will (GC; pool, no offer) | ramp / draw | Mana Geyser | Both modes while the owner controls Alexios: mana plus 3 impulse cards for 3 |
| * Brass Squire (pool, no offer) | equip | Freya Crescent | Free attach on the owner's turn; 3 of 4 lists |
| * Pip-Boy 3000 (pool, no offer) | value per attack | Infiltration Lens | Loot, untap two lands or a counter on every attack, any turn; 3 of 4 lists |
| * The Sound of Drums (pool, no offer) | multiplier | Lizard Blades | Aura that stays: doubles combat damage every turn; 3 of 4 lists |
| * Maximus, Knight Apparent (pool, no offer) | tutor | Gamble | Finds Animist, Mask or Beatstick on a body, no Game Changer slot |
| Wheel of Fortune (pool, no offer) | refill | Magus of the Wheel | Same wheel, harder to answer |
| * Goldvein Pick | ramp | Fellwar Stone | Treasure per hit for equip 1, any turn |
| Prying Blade | ramp | Thought Vessel | Treasure per hit, any turn |
| * Bitterthorn, Nissa's Animus | ramp | Solstice Revelations | A second Sword of the Animist |
| * Prismatic Vista | land | a Mountain | Untapped-for-1-life fetch of a Mountain: tests whether Salt's Manabase Quality rewards fetches, far cheaper than Wooded Foothills |
| Tome of Legends | draw | Count on Luck | Page counter on every Alexios attack under any controller |
| * Embercleave | multiplier | Lizard Blades | Flash double strike and trample |
| Umezawa's Jitte | removal / pump | Explosive Shot | Two counters per hit, every turn |
| Argentum Armor | removal | Zuko's Exile | Destroys a permanent on every Alexios attack |
| * Fury | removal | Lava Coil | Free evoke removal split across creatures |
| * Fiery Confluence | removal / wipe | Blasphemous Act | Flexible wipe that spares a grown Alexios, or burn, or artifacts |
| * Anger of the Gods | wipe | Blasphemous Act | 3-damage exile sweep Alexios survives (round 1 priced a wrong match; needs a real price) |
| Trumpeting Carnosaur | value / removal | Meteor Sword | Discover 5 on cast, removal from hand |
| Seasoned Pyromancer | draw | Zuko, Exiled Prince | Filters dead cards into tokens |
| Outpost Siege | draw | Wrenn's Resolve | An extra card every upkeep |
| Moonsilver Spear | defense | Towering Viewpoint | An untapped 4/4 Angel for the owner on every attack |
| Rite of the Raging Storm | politics | Reckless Fireweaver | Each opponent's 5/1 cannot attack the owner |
| Vengeful Ancestor | politics | Disrupt Decorum | Repeatable goad that punishes the goaded |
| Grafted Wargear | pump | Fire Nation Archers | +3/+2 for equip 0; its sacrifice clause cannot hit Alexios |
| Lavaspur Boots | protection | Hidden Footblade | Haste and ward 1 for equip 1 |
| Goldspan Dragon | ramp / threat | Zuko, Avatar Hunter | Hasty flyer, Treasures on attack and when targeted |
