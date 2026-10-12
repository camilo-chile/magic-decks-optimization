# Y = 9 reference list v2: Alexios, Deimos of Kosmos (builder round 2, 2026-10-12)

Phase 4 anchor candidate ("Y = 9 reference"). Built under the user decision "power first" (2026-10-12): only
Wizards' official Bracket 3 conditions and Commander legality limit the list; the project's own power-lowering
caps (2 Game Changers, one multiplier, no extra combats, no fast mana, speed below high) are gone. No price,
stock or ownership was considered. Rules snapshot: Wizards update of 2026-02-09 (as in `docs/power-scale.md`);
card data: Scryfall oracle bulk `oracle-cards-20261011210156`; Spellbook: local slim bulk of 2026-10-12;
Comprehensive Rules and rulings: local files of 2026-10-12.

**Plan.** Alexios attacks on every player's turn (4 attacks per round, 8 with Genji Glove). Every Equipment
trigger of mine fires on each attack (rules check R1 chain: Equipment stays attached and its controller does
not change). The list is built so that (1) Hammer of Nazahn makes every Equipment free, (2) 19 colorless
Equipment turn each hit into cards, mana, removal and counters, (3) protection from all five colors plus
hexproof plus indestructible keeps Alexios alive, (4) double strike, damage doubling and Kediss turn hits into
a table-wide kill, and (5) tutors, backup threats and sweepers cover the case where Alexios is answered.

Key numbers: 36 lands, 63 nonland cards (36 artifacts, 19 Equipment, 14 instants and sorceries), 3 Game
Changers, 0 extra-turn cards, average nonland mana value 3.03 (X = 0, Blasphemous Act = 9), 33 red sources.

## (a) Non-land cards (63), in importance order

Roles use the allowed tags. "Hit" means Alexios dealing combat damage to a player on any turn.

| # | Card | Role | Why it is in |
|---|---|---|---|
| 1 | The One Ring | draw | GC. Protection from everything for a turn on cast, then 1, 2, 3 cards per tap; indestructible. Tap it 3 or 4 times at most (upkeep life loss grows); Jitte and Wurmcoil pay the life back. |
| 2 | Jeska's Will | ramp | GC. Both modes while I control Alexios (ruling 2026-03-20: any commander counts): R for each card in an opponent's hand plus 3 impulse cards. Alexios and a full gear package in one turn. |
| 3 | Sword of Fire and Ice | equipment-engine | Each hit: 2 damage to any target and a card for me (the Equipment's controller), every turn. +2/+2, protection from red and blue (branch pivot, section c). |
| 4 | Hammer of Nazahn | protection | Every Equipment that enters attaches to a creature I control for free (Alexios, on my turn); +2/+0 and indestructible (survives destroy wipes). Removes the equip-cost bottleneck. |
| 5 | Sol Ring | ramp | Alexios on turn 2 with two lands; pays equips. |
| 6 | Umezawa's Jitte | equipment-engine | Two counters per hit on every turn; counters are repeatable -1/-1 removal, +2/+2 or 2 life (offsets Tomb and Ring). Its abilities stay mine. |
| 7 | Genji Glove | extra-combat | Double strike plus a second combat on every turn (untaps Alexios after the first combat). Doubles every Sword trigger twice over and gives 8 attacks per round. Cast 5, free to attach with Hammer. |
| 8 | Inquisitor's Flail | multiplier | Doubles all combat damage Alexios deals, on every turn; stacks with double strike (x4). Ruling 2011-09-22: also doubles damage dealt to it, harmless at high toughness. Colorless, so no pro-red conflict. |
| 9 | Commander's Plate | protection | +3/+3 and protection from W/U/B/G; cast for {1}, equip commander {3}. With Sword of Fire and Ice it is protection from all five colors. |
| 10 | Swiftfoot Boots | protection | Haste and hexproof, equip {1}. Hexproof is relative to the current controller: when an opponent holds Alexios, the other opponents cannot target it. |
| 11 | Sword of the Animist | equipment-engine | A basic Mountain on every attack of every turn (4 per round, 8 with Genji Glove): ramp, thinning, feeds Castle Embereth and Lonely Mountain. Tutorable by Maximus. |
| 12 | Sword of Feast and Famine | equipment-engine | Each hit: victim discards and I untap all lands (instant-speed mana on opponents' turns; also untaps Animist's tapped lands). Its Spellbook partners are excluded (section e). |
| 13 | Mask of Memory | equipment-engine | Draw 2, discard 1 per hit; equip {1}. Tutorable by Maximus. |
| 14 | Kediss, Emberclaw Familiar | finisher | On my turn the damage of Alexios's hit is copied to each other opponent (ruling 2020-11-10: not combat damage, not commander damage). With doubling a single swing can be lethal to the table. Two mana; no partner in the list. |
| 15 | Fireshrieker | multiplier | Double strike for {3} and equip {2}: redundancy for Glove, doubles every Sword and Jitte trigger. |
| 16 | Sword of Truth and Justice | equipment-engine | Each hit: a +1/+1 counter and proliferate. Alexios gains 1 (2 on my turn), Jitte gains 1, other counters grow. Protection from white and blue. |
| 17 | Buster Sword | equipment-engine | +3/+2; each hit: draw, then cast a spell from hand free (mana value up to the damage dealt, usually 5+ with Alexios; any turn). |
| 18 | Arcane Signet | ramp | Two-mana rock that always makes red. |
| 19 | Maximus, Knight Apparent | tutor | Body that tutors a 2-mana Equipment: Jitte, Mask, Animist, Boots or Flail. |
| 20 | Reckless Handling | tutor | Two-mana tutor for any artifact (Hammer, Glove, any Sword). The random discard is the cost; 2 damage to each opponent if an artifact is discarded. |
| 21 | Goblin Engineer | tutor | Puts any artifact into the graveyard; {R}, tap, sacrifice an artifact returns one of mana value 3 or less (every Sword, Jitte, Fireshrieker, Plate), which Hammer attaches. Also recursion after artifact removal. |
| 22 | Mystic Forge | draw | Casts artifact and colorless spells from the top of the library (more than a third of the deck qualifies); pay 1 life to bin a dead top card. Ruling 2019-07-12: no lands. |
| 23 | Thorin, Mountain-king | other | ETB attaches any number of my Equipment to Alexios in one go (re-equip after a recast) and Alexios then deals damage equal to its power to a creature. Caveat in (c): red source, so it cannot target an Alexios that already wears Sword of Fire and Ice. |
| 24 | Sword of Hearth and Home | equipment-engine | Each hit: an untapped basic land and a blink of a creature I own with an ETB (Inferno Titan, Fury, Engineer, Maximus, Godo, Thorin, Pyromancer, Solemn). Never target Alexios (it would reset). Combo-adjacent: see (h). |
| 25 | Argentum Armor | equipment-engine | +6/+6; each attack destroys a permanent of my choice (the trigger is Armor's, so it works on opponents' turns): up to 8 per round with Glove. Also my answer to attack-tax enchantments. Policy: never target lands. |
| 26 | Chaos Warp | interaction | Instant answer to any permanent (taxes, planeswalkers, artifacts). |
| 27 | Lightning Bolt | interaction | One-mana instant; also the best recast target of Sword of Once and Future. |
| 28 | Fiery Confluence | wipe | Flexible: three 1-damage sweeps, 6 damage to each opponent, or up to 3 artifacts destroyed. Red damage does not hurt a pro-red Alexios. |
| 29 | Darksteel Plate | protection | Second indestructible source in case Hammer is not out or is exiled. |
| 30 | Silent Arbiter | other | Only one creature can attack each combat; Alexios's "attacks each combat if able" makes it the only attacker (CR 508.1c-d), so nobody can attack me. Also at most one blocker per combat against Alexios. Lock-ish: see (h). |
| 31 | Foundry Inspector | other | Artifact spells cost {1} less; 36 of my 63 nonland cards are artifacts. A body to carry gear. |
| 32 | Goldspan Dragon | finisher | Haste flier that makes Treasures; second threat and gear carrier if Alexios is answered. |
| 33 | Glorybringer | finisher | Haste flier; exert for 4 damage to a creature every other turn; second threat. |
| 34 | Mind Stone | ramp | Two-mana rock that cashes in for a card late. |
| 35 | Thought Vessel | ramp | Two-mana rock; no maximum hand size for the draw engines. |
| 36 | Solemn Simulacrum | ramp | Land plus a card; an artifact body; blink target of Hearth and Home. |
| 37 | Outpost Siege | draw | Khans: an extra card at each of my upkeeps. Dragons mode not needed. |
| 38 | Pip-Boy 3000 | equipment-engine | Each attack: loot, a +1/+1 counter or untap two lands (a cost-1 engine, mana for instants on opponents' turns). Also a chapter III target of Urza's Saga. |
| 39 | Galvanic Blast | interaction | One mana, 4 damage with three artifacts (36 artifacts). Instant. Recast target of Sword of Once and Future. |
| 40 | Blasphemous Act | wipe | Usually 3 to 5 mana; 13 damage. Alexios survives only with pro-red (Sword of Fire and Ice), indestructible (Hammer of Nazahn, Darksteel Plate) or toughness 14+ from counters; Plate's toughness alone (7) does not save it. |
| 41 | Abrade | interaction | Instant: 3 damage or destroy an artifact. |
| 42 | Rebel Salvo | interaction | Affinity for Equipment: usually {R}; 5 damage to a creature or planeswalker at instant speed. |
| 43 | Tome of Legends | draw | Page counter on every Alexios attack under any controller (ruling 2019-10-04); one draw per round for {1}. |
| 44 | Seasoned Pyromancer | other | Filters dead cards and makes Elemental bodies; blink target. |
| 45 | Godo, Bandit Warlord | tutor | Six mana: an Equipment from the library straight onto the battlefield (Hammer attaches it). With Hearth and Home every hit fetches another. |
| 46 | Inferno Titan | finisher | Repeatable 3 damage divided on ETB and attack; blink target. |
| 47 | Wurmcoil Engine | finisher | Colorless lifelink and deathtouch body that leaves two 3/3 tokens when it dies; the life buffer for Tomb and Ring. |
| 48 | Fury | interaction | Free evoke or a 5-mana double striker; 4 damage divided on ETB; blink target. |
| 49 | Bonehoard Dracosaur | finisher | Flying first striker that exiles two cards each upkeep and makes Treasures or Dinosaurs: a threat and an engine. |
| 50 | Furious Rise | draw | A card at each of my end steps while Alexios (power 4+) is mine. |
| 51 | Mizzium Mortars | interaction | Spot removal for 4 damage or a one-sided overload sweep. |
| 52 | Anger of the Gods | wipe | 3 damage to each creature, exile; Alexios survives. |
| 53 | Thran Dynamo | ramp | Three colorless mana pays equips and big sinks. |
| 54 | Fire Diamond | ramp | Red source that cannot be color-blanked (unlike Fellwar Stone). |
| 55 | Everflowing Chalice | ramp | Scalable rock: 2 mana for 1, 4 for 2. |
| 56 | Comet Storm | interaction | Instant X burn split among many targets; late finisher. |
| 57 | Masterwork of Ingenuity | equipment-engine | One mana: a second copy of the best Sword or Mask on the battlefield (not Jitte, Animist or Hammer: legend rule). |
| 58 | Sword of Once and Future | equipment-engine | Each hit: surveil 2 and a free cast of a 2-or-less instant or sorcery from the graveyard (Bolt, Galvanic Blast, Abrade, Mortars, Reckless Handling). |
| 59 | Light Up the Stage | draw | {R} after Alexios hits on my turn: two cards. |
| 60 | Wild Magic Surge | interaction | Instant {R}{R}: destroy any opposing permanent (random replacement of the same type). Second answer to enchantments. |
| 61 | Jhoira's Familiar | other | Historic spells cost {1} less (artifacts and legendaries: Alexios recasts, Hammer, Jitte, Maximus, Godo, Kediss); flying carrier. |
| 62 | Kaldra Compleat | equipment-engine | Added after the review (reviewer suggestion G1, replaces Walking Ballista): living weapon, +5/+5 with first strike, trample, indestructible and haste; Hammer of Nazahn attaches it to Alexios for free when it enters. Colorless, so it coexists with pro-red. |
| 63 | Wayfarer's Bauble | ramp | One-mana early ramp and thinning (Mountains for Animist). |

Role counts: ramp 10, equipment-engine 12, draw 6, interaction 9, finisher 6, other 6, protection 4, tutor 4,
wipe 3, multiplier 2, extra-combat 1 (63). Alexios is the 100th card. Ancient Tomb (a GC land) is not ranked.

### Consistency plan (what makes the list steady, with numbers)

| Concern | What the list does |
|---|---|
| Mana | 36 lands plus 9 mana artifacts (Sol Ring, Signet, Mind Stone, Vessel, Diamond, Chalice, Bauble, Dynamo, Solemn) plus Jeska's Will; Animist and Hearth and Home add lands on every hit. |
| Redundancy of engines | 5 Swords + Jitte + Mask + Buster + Pip-Boy + Armor + Animist as hit triggers (11 pieces, plus Masterwork as a copy); 2 double-strike sources (Glove, Fireshrieker) plus Flail as a separate doubler; 2 indestructible sources (Hammer, Darksteel Plate); protection from all five colors from Sword of Fire and Ice + Plate, or from three Swords. |
| Finding the key pieces | Maximus, Engineer, Reckless Handling, Godo, Urza's Saga (fetches Sol Ring, Plate, Pip-Boy, Masterwork, Chalice, Bauble), Inventors' Fair, Mystic Forge, Outpost Siege. |
| Interaction | 9 spot answers and 3 sweepers, plus Jitte, Swords, Thorin, Titan, Fury. Artifact-capable: Abrade, Chaos Warp, Wild Magic Surge, Fiery Confluence, Armor. Enchantment-capable: Chaos Warp, Wild Magic Surge, Armor. |
| Opponents' sweepers | Hammer and Darksteel Plate (indestructible), Plate and Swords (protection), backup threats in the air and Wurmcoil's tokens. |
| Alexios removed | Command Beacon (back to hand, no tax), Jhoira's Familiar ({1} off the tax), Thorin (re-attach everything), Godo and Engineer (rebuild), Goldspan, Glorybringer, Dracosaur, Titan, Wurmcoil. |
| Attack taxes (Propaganda, Ghostly Prison, Archangel of Tithes style) | Alexios is not forced to pay (Alexios ruling 2024-07-05), so the plan is removal: Chaos Warp, Wild Magic Surge, Argentum Armor, Fiery Confluence/Abrade/Galvanic Blast/Bolt for artifacts and creatures; and choosing an untaxed opponent as the target on my turn. |
| Opposing attackers | Silent Arbiter (nobody else attacks), sweepers, Jitte and Wurmcoil life; goad was left out because it conflicts with Arbiter (CR 508.1d). |
| Dead draws | Pip-Boy and Seasoned Pyromancer loot, Valakut Awakening, Mask discard, Mystic Forge exile. |

## (b) Lands (36 land cards)

| Group | Cards | # | Why |
|---|---|---|---|
| Basic | Mountain | 25 | Red base; Animist, Hearth and Home, Solemn and Bauble fetch basics; Castle Embereth wants a Mountain |
| Colorless utility | Ancient Tomb, Inventors' Fair, Urza's Saga, Command Beacon, Bonders' Enclave | 5 | Tomb: GC fast mana. Fair: late artifact tutor. Saga: constructs and a free Sol Ring or Plate. Beacon: commander insurance. Enclave: draw sink (Alexios is power 4+ on my turn) |
| Red utility | Castle Embereth, Sokenzan, Crucible of Defiance, The Lonely Mountain | 3 | Untapped red sources with a use; Lonely Mountain is a Mountain and enters untapped with any Equipment |
| Modal DFC (counted as lands) | Shatterskull Smashing, Valakut Awakening, Pinnacle Monk | 3 | Land early (pay 3 life for untapped on two of them), removal, hand filter or a 5-drop that returns a sweeper late |

Count justification (hypergeometric over 99 cards, on the play):
- Rule of thumb used by the first draft: 31 + 3 x average mana value - 0.28 x (ramp + cheap draw) =
  31 + 9.15 - 0.28 x 16 = 35.7, so 36.
- 36 lands + 9 mana artifacts = 45 mana sources. Opening 7: expected 2.55 lands, P(2 to 4 lands) = 74%,
  P(0 or 1 land) = 20% (a free mulligan covers it). P(at least 4 mana sources by turn 4, 10 cards) =
  75.6% (35 lands: 73.4%; 37 lands: 77.7%). P(at least 8 lands in 14 cards, the flood case) = 7.6%, and
  the flood is cushioned by sinks (equip, Armor, Pip-Boy, Enclave, Fair, Ballista, Forge) and 3 MDFC.
- Red sources: 25 Mountain + 3 red utility + 3 MDFC = 31 lands, plus Signet and Fire Diamond = 33.
  P(at least 1 red source by turn 2, 8 cards) = 96.6%; P(at least 2 by turn 4) = 90.8%; by turn 6 95.6%.
  Demand: 10 nonland cards need RR (Goldspan, Glorybringer, Fury, Dracosaur, Titan, Pyromancer, Confluence, Anger,
  Comet Storm, Wild Magic Surge) plus 2 modal fronts (Shatterskull Smashing, Pinnacle Monk) and Mortars overload needs RRR; 17 more cards need one R; 36 are colorless.
- Only 5 lands are colorless-only; the colorless rocks (Sol Ring, Mind Stone, Vessel, Dynamo, Chalice) pay
  the generic costs that the gear needs.
- Left out of the base: fetch lands and Command Tower (a Mountain at best), Mishra's Workshop (GC, artifact
  mana only), Strip Mine / Ghost Quarter / Demolition Field (single-land destruction, not needed, intent risk),
  Rogue's Passage and Maze of Ith (Plate, Swords and Arbiter already cover blocks and attacks), War Room
  (cut for a Mountain: Enclave is the draw sink), Myriad Landscape (tapped, colorless), Spinerock Knoll.

## (c) Branch decision: protection from red

**Branch chosen: PRO-RED (kept).** Sword of Fire and Ice and the other protection-from-red Swords are in; the
list has no red Aura, no red Equipment and no red spell that must target Alexios.

| Fact | Source |
|---|---|
| Equipment with the stated quality becomes unattached from a protected permanent (state-based action) | CR 702.16d, 704.5n |
| Protected permanents cannot be targeted by sources with the quality; damage from them is prevented; creatures of that color cannot block them | CR 702.16b; Sword rulings 2019-06-14 |
| Equipment is colorless in this list: all 19 pieces have no color (checked against the pool) | pool file |

Why this branch:
1. Sword of Fire and Ice is the best hit-trigger Sword for this plan (2 damage plus a card, every turn, all
   mine). Dropping it to keep red gear would lose it for Embercleave, Mjolnir Hammer of Thor, Two-Handed Axe,
   Komainu, Spear of Leonidas, Lizard Blades, Hard-Won Jitte, Shiny Impetus: the colorless set (Glove,
   Fireshrieker, Flail, Plate) replaces all of their effects.
2. Free upside: red creatures cannot block it, red removal cannot target it, and my own red sweepers (Blasphemous
   Act, Anger of the Gods, Fiery Confluence, Mortars overload) deal no damage to it.
3. Whole-list coherence: Spectacular Showdown (red, targets Alexios, cast-first rule) was cut; double strike comes
   from Glove and Fireshrieker, both colorless. Thorin is the only red card whose text requires targeting a creature I control:
   if Sword of Fire and Ice is already attached, Thorin cannot target Alexios (red source vs protection). Use
   Thorin after a recast (no Sword attached yet), or cast it before equipping the Sword.
4. Protection stack: Sword of Fire and Ice (R, U) + Sword of Feast and Famine (B, G) + Sword of Truth and
   Justice (W, U) or Plate (W, U, B, G) = all five colors; Boots add hexproof; Hammer and Darksteel Plate add
   indestructible. Only colorless sources that do not target and do not destroy can touch Alexios.
5. Fillers must never include red Auras or red Equipment (see slot-ranking note).

## (d) Game Changers used: 3 (Ancient Tomb, Jeska's Will, The One Ring)

The commander is not one. All three slots are used because each improves the deck.

| Card | Why |
|---|---|
| The One Ring | Best draw engine in the pool plus a turn of protection; indestructible. |
| Jeska's Will | Both modes while Alexios is mine: a turn-3 explosion of mana and cards. |
| Ancient Tomb | Two mana from a land: Alexios on turn 2 with Sol Ring, pays equips; 2 damage per tap is paid back by Jitte, Wurmcoil and Arbiter (no combat damage taken). |

Not used (12 more in the pool): Mana Vault, Grim Monolith, Chrome Mox, Mox Diamond (fast mana: a 4th slot
is not allowed; Mana Vault was the closest), Gamble (one-card tutor with a random discard; the list already
has 4 tutors plus Saga and Fair), Mishra's Workshop (artifact mana only, no help for Alexios or equip
costs), Lion's Eye Diamond and Underworld Breach (combo engines), Field of the Dead, Panoptic Mirror,
The Tabernacle and Glacial Chasm (locks).

## (e) Cards considered and left out

### Official-condition reasons (Bracket 3 text or Commander legality)

| Card(s) | Reason |
|---|---|
| Mana Vault, Grim Monolith, Chrome Mox, Mox Diamond, Gamble, Mishra's Workshop, Lion's Eye Diamond, Underworld Breach, Field of the Dead, Panoptic Mirror, Tabernacle, Glacial Chasm | Game Changers beyond the 3 allowed (4+ sets floor 4) |
| Dockside Extortionist, Mana Crypt, Jeweled Lotus | Banned in Commander (lookup: legal "banned") |
| Blood Moon, Magus of the Moon, Ruination, Armageddon family, Winter Orb, Static Orb, Tangle Wire, Smokestack, Worldslayer, Worldfire, Keldon Firebombers and the rest of the mass-land-denial name list in `data/hazards.json` | Mass land denial (floor 4) |
| Aggravated Assault, Hellkite Charger, Najeela, Neheb the Eternal | Early two-card infinite combats with Sword of Feast and Famine or alone (Spellbook, one card away) |
| Akki Battle Squad | Two-card infinite combats with Sword of Hearth and Home (Spellbook tag S, mana value 0) |
| Helm of the Host, Rionya Fire Dancer | Two-card infinite combats with Godo (Spellbook tag S, mana value 0); Helm is also a hub with ten partners (curated hazard) |
| Kiki-Jiki, Splinter Twin, Zealous Conscripts, Dualcaster Mage + Twinflame / Heat Shimmer, Basalt Monolith + Rings / Forsaken Monument, Metalworker + Staff of Domination | Classic early two-card infinites (hazard list) |
| Grafted Exoskeleton | Infect partner of Kediss: "each opponent loses" (Spellbook, tag S) |
| Mycosynth Lattice (with Vandalblast), Blood Clock, Umbilicus, Obelisk of Undoing (with The One Ring), Reiterate (with Jeska's Will), Worldfire (with Outpost Siege), Repercussion, Expedited Inheritance, Fall of Cair Andros, Toralf (with Blasphemous Act) | One card away from a floor-4 or lock variant of a card in the list; never add |
| Global haste and untap enablers (Fervor, Mass Hysteria, Rising of the Day, The Fire Crystal, Tannuk, Purphoros Bronze-Blooded, Urabrask the Hidden, Anger the Incarnation, Hammer of Purphoros, Lavaleaper, Cyclops of Eternal Fury, Kratos, Tuktuk Rubblefort, Gimli's Reckless Might, Barbarian Class, Smellerbee) | Each makes a three-card infinite loop with Godo and Sword of Hearth and Home (Spellbook tag E): allowed by the text, but excluded so the pair stays a finite engine |
| Sensei's Divining Top | Three-card infinite draw with Mystic Forge and Foundry Inspector or Jhoira's Familiar (Spellbook tag E) |

### Just weaker or conflicting with the plan (not official conditions)

| Card(s) | Reason |
|---|---|
| Embercleave, Mjolnir Hammer of Thor, Two-Handed Axe, Komainu Battle Armor, The Spear of Leonidas, Lizard Blades, Hard-Won Jitte, Twin Blades, Shiny Impetus, The Sound of Drums, Spectacular Showdown | Red permanents or spells that cannot attach or target under protection from red (c); colorless double strike and doubling replace them |
| Torbran, Fiery Emancipation, Gratuitous Violence, Angrath's Marauders, Furnace of Rath, Dictate of the Twin Gods, Twinflame Tyrant | Further multipliers: RRR or sorcery speed, or symmetric (they double the opponents' attacks on me); Flail plus double strike already quadruples |
| Relentless Assault, Seize the Day, Full Throttle, Karlach, Moraug, Overpowering Attack | Extra combats weaker than Glove (a permanent, every turn); redundant, sorcery speed, Moraug is main-phase only |
| Chandra Torch of Defiance, Ugin the Ineffable, Tezzeret Cruel Captain, Jeska Thrice Reborn | Planeswalkers give an opponent who holds Alexios a free target that avoids hitting a friend and dodges Sword triggers (Alexios can attack its owner's planeswalkers, ruling 2024-07-05) |
| Court of Embereth, Emberwilde Captain, Crimson Fleet Commodore | Monarch is lost to the first creature that hits me; my only blockers are Arbiter and sweepers |
| Disrupt Decorum, Vengeful Ancestor, Rite of the Raging Storm, wheels | Goad lets an opponent choose a goaded creature as the single attacker under Silent Arbiter (CR 508.1d); wheels help opponents |
| Gonti's Aether Heart, Magistrate's Scepter, Timesifter, Final Fortune, Last Chance, Warrior's Oath, Rise of the Eldrazi | Extra turns are allowed in low quantities (0 used). Aether Heart (6 mana, 8 energy) was the closest; weaker than the cards it would replace and slow; the others lose the game or cost 12 |
| Terror of the Peaks, Trumpeting Carnosaur, Etali, Hellkite Tyrant, Atsushi, Scourge of Valkas | Fewer ETB creatures than Terror needs; Carnosaur and Etali are slower than the finishers already in |
| Armory Automaton, Brass Squire, Kazuul's Toll Collector | Thorin does the mass attach and removes a creature |
| Mithril Coat, Lightning Greaves, Whispersilk Cloak | Mithril attaches only on my turn (flash is useless); shroud blocks Hammer, Thorin and my own equips |
| Blade of Selves | Myriad copies of Alexios would be controlled by the opponent holding it (granted ability) |
| Skullclamp, Idol of Oblivion | No fodder or token makers in the list |
| Mox Opal, Mox Amber, Lotus Petal, Hedron Archive, Worn Powerstone, Fellwar Stone, Commander's Sphere, Prismatic Lens | Weaker ramp than the 10 chosen (Fellwar cannot make red if no opponent has a red land) |
| Vandalblast, Untimely Malfunction, Flame Slash, Thundering Rebuke, Delayed Blast Fireball, Storm's Wrath, Chain Reaction | Weaker or narrower than the kept interaction (Confluence and Abrade cover artifacts, Salvo and Mortars cover creatures) |
| Star of Extinction | Destroys a land per cast and 20 damage to everything; the kept sweepers do the job without land destruction |
| Glamdring, Armory of Iroas, Sword of Hours | Buster Sword does the free cast better; counters come from Pip-Boy and Truth and Justice |
| Strip Mine, Ghost Quarter, Demolition Field, Sundering Eruption | Single-land destruction does not help the plan and invites the intent critique |
| Ugin Eye of the Storms, Kozilek Butcher of Truth | Pricey colorless 7 to 10 drops with no better role than Wurmcoil and Titan |
| Assault Suit, Worldslayer, The Dominion Bracelet, Mindslaver, Tempestra Dame of Games | Rules traps from the rules check (cannot attack my planeswalkers / destroys the carrier / opponent control / permanent non-legendary copy) |

## (f) Last gate output (reference.txt, verbatim)

```text
bulk: oracle-cards-20261011210156.jsonl.gz
cards 100, recognized 100, floor 3, rejected False, floor_ok_so_far True
game changers: 3 -> ['Ancient Tomb', "Jeska's Will", 'The One Ring']
extra-turn cards: 0; mass land denial: {}
Spellbook: 0 variants inside the deck, 0 flagged, 97 one card away
HAZARD floor 3: stax-and-lock-names: Taxes, tap-downs, attack locks and spell locks: Wizards says a Stax-style lock deck should bracket up; review note, not a floor
descriptive: {'tutors': ['Goblin Engineer', 'Godo, Bandit Warlord', "Inventors' Fair", 'Maximus, Knight Apparent', 'Reckless Handling', "Urza's Saga"], 'land_cards': 36, 'average_mana_value_nonland': 3.05}
speed risk: very high (83.1% by turn 6); cumulative {'1': 0.0, '2': 0.0001, '3': 0.0712, '4': 0.3025, '5': 0.6602, '6': 0.8311}; decisive combos 0
```

Reading it: the only HAZARD row is review-only (Silent Arbiter on the stax list) and does not change the
floor; floor 3 comes only from the three Game Changers. The speed flag is reported only; the Monte Carlo
does not model equipment, so it understates the list.

Extra checks run with the same code (read-only, all offline):
- Lookup (oracle text, legality, Game Changer flag) of the commander, the 63 nonland cards, the 11 nonbasic
  lands (75 names) and the 141 fillers: all found, all legal, color identity R or colorless only; exactly 3
  Game Changer flags (Ancient Tomb, Jeska's Will, The One Ring).
- Superset check: the 100-card list plus all 141 fillers (241 cards, size rejection ignored): 0 Spellbook
  variants inside the deck, 0 flagged, 0 floor-4 hazards, floor 3, extra-turn 0, mass land denial none.
- Official conditions by hand: extra turns 0; mass land denial none (Argentum Armor, Chaos Warp and Wild Magic
  Surge can hit a land, policy is never to; no card is aimed at lands); no two-card combo in Spellbook
  (0 variants name Alexios or are inside the list); one-card-away table in (h) item 3.
- Why 97 "one card away": 34 of them have all missing cards in the R or colorless pool and are listed in (h);
  the rest need off-color cards.

## (g) Comparison with the previous draft (`evals/anchors/...reference-draft.txt`)

Same land count (36) and Mountain count (25). 25 cards differ (22 nonland, 3 land); 50 non-Mountain cards stay.

| Left (25) | Reason |
|---|---|
| Spectacular Showdown | Red, targets Alexios, conflicts with protection from red; double strike now from Glove and Fireshrieker |
| Chandra Torch of Defiance, Ugin the Ineffable | Planeswalkers are an attack-target liability here |
| Court of Embereth | Monarch is unsafe without blockers |
| Disrupt Decorum, Vengeful Ancestor | Goad conflicts with Silent Arbiter |
| Armory Automaton | Thorin covers mass attach and removal |
| Deflecting Swat | Protection stack makes it nearly dead; works on my turn only |
| Glamdring | Buster Sword is strictly better for free casts |
| Big Score, Unexpected Windfall, Endless Atlas, Dragon's Hoard, Commander's Sphere, Fellwar Stone, Sceptre of Eternal Glory | Weaker than Mystic Forge, Foundry Inspector, Chalice, Diamond, Bauble and the new engines |
| Terror of the Peaks, Trumpeting Carnosaur | Replaced by Dracosaur, Godo and the engines |
| Delayed Blast Fireball, Flame Slash, Vandalblast, Untimely Malfunction | Replaced by Galvanic Blast, Rebel Salvo, Fiery Confluence's artifact mode and Abrade |
| Rogue's Passage, War Room, Myriad Landscape | Plate, Swords and Arbiter cover blocks; Mountains for red consistency; Landscape is tapped and colorless |

| Entered (25) | Why |
|---|---|
| Ancient Tomb | Third Game Changer slot used (fast mana) |
| Genji Glove, Fireshrieker, Inquisitor's Flail | Extra combat, double strike and damage doubling now allowed |
| Kediss | Table-wide hit on my turn |
| Sword of Truth and Justice, Sword of Hearth and Home, Sword of Once and Future | More hit-trigger Swords (counters, ramp and blink, free recasts) |
| Masterwork of Ingenuity | A second Sword for {1} |
| Darksteel Plate | Second indestructible source |
| Thorin, Godo | Mass re-equip with removal; equipment onto the battlefield |
| Mystic Forge, Foundry Inspector, Jhoira's Familiar | Artifact-deck card flow and cost reduction |
| Silent Arbiter | Nobody else can attack me |
| Galvanic Blast, Rebel Salvo | Cheap efficient removal that scales with artifacts and Equipment |
| Bonehoard Dracosaur | Threat plus engine |
| Walking Ballista | Mana sink and reach |
| Fire Diamond, Everflowing Chalice, Wayfarer's Bauble | Red-safe and early ramp |
| Urza's Saga, Pinnacle Monk // Mystic Peak | Tutor land; land with a late spell side |

## (h) Open doubts

1. **Speed.** The flag says very high (83.1% by turn 6) and the Monte Carlo ignores all gear. With Sol Ring,
   turn 2 Alexios is possible; Glove, Fireshrieker, Flail and Kediss can make one swing lethal to the table
   around turn 4 to 5. Allowed by the official text; the bracket-fit review should say how it reads.
2. **Protection stack and lock feel.** Swords plus Plate plus Boots plus Hammer plus Arbiter is a heavy
   package; if the review calls it too much, drop in this order: Silent Arbiter, Darksteel Plate, Swiftfoot
   Boots, Sword of Once and Future. All have fillers.
3. **Godo + Sword of Hearth and Home.** Spellbook lists 16 three-card infinite loops that need a third card
   that grants haste or untaps (one card away, tag E; names in (e)); Akki Battle Squad is a two-card infinite
   with the Sword alone. Nothing in the list completes them. Never add those cards, and treat the pair as the
   first thing to cut if a stricter reading is wanted.
4. **One card away (never add):** Aggravated Assault, Hellkite Charger, Najeela (Sword of Feast and Famine);
   Akki Battle Squad (Hearth and Home); Helm of the Host, Rionya (Godo); Blood Clock, Umbilicus, Obelisk of
   Undoing (The One Ring); Grafted Exoskeleton (Kediss); Reiterate (Jeska's Will); Worldfire (Outpost Siege);
   Repercussion, Expedited Inheritance, Fall of Cair Andros, Toralf (Blasphemous Act); Sensei's Divining Top
   (Mystic Forge with Inspector or Familiar); Crown of Flames and similar storm-count cards (Goldspan).
5. **Argentum Armor** can destroy any permanent on every attack. Policy: never lands. A reviewer may read it as
   repeated land destruction; it is rank 25 and easy to cut.
6. **Silent Arbiter** is on the review-only stax list. It also stops my other attackers while Alexios is out and
   can be turned off by goad. It is the only card that makes the table unable to hit me.
7. **Life.** Ancient Tomb (2 per tap), The One Ring (burden counters) and Mystic Forge cost life; Jitte,
   Wurmcoil and Arbiter pay it back. A reviewer may see this as a risk; it is optional play.
8. **Genji Glove on opponents' turns** gives the active opponent an extra combat phase too: their other
   untapped creatures could attack me in it. Arbiter closes this; without Arbiter it is a mild downside.
9. **Planeswalker policy** rests on Alexios's ruling that it can attack its owner's planeswalkers; it is a
   judgment that the soak outweighs Chandra's value, not a ruling.
10. **Rules readings used and not tested by a specific ruling.** Silent Arbiter and Genji Glove have no
    rulings on file (CR 508.1c-d read from the local rules file); Hearth and Home never targets Alexios;
    the Alexios counter placement by Truth and Justice on opponents' turns depends on proliferate choosing
    permanents controlled by others (ruling 2023-02-04).
11. **Game Changer flags** come from the 2026-10-11 bulk file; `docs/power-scale.md` says the 2026-10-12
    announcement did not change Commander. Re-check before freezing.
12. **Ranking is judgment, not data.** No community inclusion rates were used. The weakest slots are role
    coverage: Wayfarer's Bauble, Walking Ballista, Jhoira's Familiar, Wild Magic Surge, Light Up the Stage.

## (i) Review response (independent review, Haiku 5.5 at xhigh, 2026-10-12)
Verdict PASS WITH FIXES, 0 blockers, 0 high, 2 medium, 13 low. All fixes applied here.

| Finding | Decision |
|---|---|
| F-01 Argentum Armor and "mass land denial" | Kept. Wizards' definition needs four or more lands per player regularly destroyed; this is one chosen target per attack. Deck rule: target threats, never lands (the user's choice at the table) |
| F-02 Blasphemous Act survival wording | Fixed (row 40) |
| F-03 Boots as the haste piece of an Ardenn loop | Ardenn is white and cannot be added; noted: never add Ardenn, Intrepid Archaeologist |
| F-04 Filler name | `Vance's Blasting Cannons // Spitfire Bastion` in slot-ranking.json |
| F-05 to F-13 | Wording fixed (Thorin, Hammer, Animist, Wurmcoil, Buster Sword, MV 3.03, RR count 12, Toralf is not Commander-legal) |
| F-14 `gate.py lookup` cp1252 crash | Tooling only; run with `python -I -X utf8` |
| G1 Kaldra Compleat for Walking Ballista | Accepted and applied; gate re-run, floor 3, no flags |
| G2 Batterskull | Rejected: lifelink on Alexios pays whoever controls it (rules check C9), so it would feed the opponent on their turn |
| G3 Hellrider | Not applied: 1 damage per attack on my turn only, weaker than the card it would replace |

Design note for the owner: Silent Arbiter lets only one creature attack each combat; while Alexios
is on the battlefield (forced to attack) it also stops Goldspan, Glorybringer and the other hasty
finishers from attacking on my turn. They remain insurance for when Alexios is gone and a defence
against swarms. If the owner prefers them attacking, Arbiter is the first card to swap out.
