# Phase 2: commander of the Spanish deck (2026-11-01)

Opus 5.5 high. This chooses the commander only; the deck is not built here. Method: `.claude/skills/commander-deckbuilding`
steps 1 to 3 and 7, `archetypes.json`, `references/archetypes.md`, and the owner lessons in
`docs/research/phase2-owner-lessons-20261031.md`.

**Inputs.** `data/model/phase2/spanish-candidates.md/.json` (21 owned legends with a Spanish copy). The Spanish pool of each
candidate came from `build_pools.pool(..., 'es')` over `data/cache/collection_owned.json` and the Scryfall bulk. Pool sizes
checked against the candidates table: Kilo has 191 entries (149 nonland), Jhoira 134 (111), Arbaaz Mir and Alibou 123 (98),
Ezio, Blade of Vengeance 141 (119). EDHREC rows come from `data/cache/edhrec/<slug>.cards.json` and are used as a prior only.

**How the counts were made.** Each function was tagged by hand from the Oracle text. A full piece counts 1. A piece counts
0.5 when it is a one-shot effect in a support line, conditional, a single 1-damage ping, or a cantrip-like effect (skill 3.4).
A card counts as **free** when at least one Spanish copy sits in no deck. A card whose Spanish copies are all in Toph, Azula
or Ezio is listed under conflicts and left out of the counts.

**Spanish basics.** None of them sits in a deck: the three decks hold English basics. Island 11 (ACR 303 ×8, EOE 269 ×2,
EOE 270), Plains 14, Mountain 15, Swamp 10, Forest 1 (TLA 286).

**Bracket 3.** A live Scryfall `is:gamechanger` search (53 cards, 2026-11-01) found **no Game Changer in any of the 21
Spanish pools**. No pool has mass land denial or extra turns. The infinite-combo check (Commander Spellbook) is left for the
build.

## 1. Shortlist and ranking

| Rank | Commander | Id | MV | Plan in one line | Consistency verdict | Lands, scenario A |
|---|---|---|---|---|---|---|
| **1** | **Kilo, Apogee Mind** | URW | 3 | Kilo taps every turn to proliferate a board of growing rocks, charge engines and +1/+1 artifact creatures. It closes with Lux Artillery or Darksteel Reactor, or with an animated flying or trampling alpha strike. | Every gate function is well above its minimum. Ramp is 1 under (9 of 10). Commander protection is 2.5 of 3. | Works |
| 2 | Jhoira, Weatherlight Captain | UR | 4 | Cast historic spells and draw a card for each; close with the same counter artifacts. | Ramp is 3 under (9 of 12); only 1 wipe; the counter closers are slower without Kilo or white. It is the Kilo deck minus white and minus its engine. | Works |
| 3 | Ezio, Blade of Vengeance | UB | 5 | Assassins connect and draw. | Haste 0.5 of 4, team evasion 0, protection 2 of 6, 9 free Assassins. It repeats the losses of the Ezio games (L3) and duplicates the theme of the Ezio deck. | Works, tight |
| 4 | Arbaaz Mir | RW | 2 | Each nontoken historic permanent pings each opponent. | Draw 3.5 of 10, protection 0. Its only Spanish copy sits in Toph. | Works |
| 5 | Alibou, Ancient Witness | RW | 5 | Artifact creatures attack with haste; Alibou shoots one target. | Draw 3.5 of 10, protection 0, and a single-target route. | Works |

**Revised 2026-11-02.** Inspirit, Flagship Vessel was missing from the input. It can be a commander: `is:commander` returns it,
because a legendary Spacecraft with power and toughness is allowed. It enters at **rank 2** (section 2.6), so Jhoira, Ezio,
Blade of Vengeance, Arbaaz Mir and Alibou each move down one place. Adrestia (colorless, Spanish pool of 53) is dropped:
its colorless identity rules out every colored card and every Spanish basic, so its pool is 53 cards with no plan and too
few lands.

### Dropped (16)
| Commander | Reason |
|---|---|
| Ezio, Brash Novice (RW) | A self-voltron 1/1. The pool has about 9 equipment and no hexproof or indestructible pieces in RW, while voltron needs 8 to 10 protection. Only 4 EDHREC cards with synergy ≥ 0.2 are owned. There is no plan. |
| Adéwalé, Breaker of Chains (UB) | Lesson L7 names its vehicle clause as dead: the Spanish pool has 3 vehicles and 0 Pirates. Its Assassin part is the Ezio, Blade of Vengeance pool, which is ranked above. |
| Tekuthal (U) | Mono-blue. The Spanish lands are 11 Islands plus 14 nonbasics, colorless utility included, so about 25 sources fail scenario A. Its proliferate package is a subset of Kilo's, and Tekuthal itself goes into the Kilo 99. |
| Katara, Emry, Teo, Evie Frye (U) | Mono-blue land count as above. Evie's only Spanish copy sits in Ezio. With 86 nonland cards a deck would take almost the whole pool, so there is no plan. Emry has no self-mill; Teo has about 12 flyers. |
| Aang, Master Piandao, Momo (W) | Mono-white: 14 Plains plus 14 nonbasics give about 28 sources. The pool has 2 white Lessons, about 9 equipment and few Allies. No density for any of their clauses. |
| Zuko, Exiled Prince (R) | Mono-red: 15 Mountains plus 13 nonbasics give about 28 sources. 63 nonland cards and no plan beyond firebending mana. |
| Lo and Li, Koh (B) | Mono-black: 10 Swamps plus 12 nonbasics give about 22 sources. Lo and Li have no Lessons or Nobles in the black pool. Koh has 67 nonland cards. |
| Titania, Nature's Force (G) | 1 Spanish Forest, and its plan is Forests. Impossible in A. |
| Eivor, Wolf-Kissed (GRW) | 24 green nonland cards, 1 Forest, and almost no green land (Kyoshi Village; both Fortified Villages sit in decks). Few Sagas, no self-mill plan, 0 high-synergy cards owned. |
| Arixmethes (GU) | 21 green nonland cards and 1 Forest. It needs many spells cast to wake. Green fails in A. |

## 2. Candidates

### 2.1 Kilo, Apogee Mind (rank 1)

**Reading.** {U}{R}{W} 3/3 legendary artifact creature, with haste. "Whenever Kilo becomes tapped, proliferate."
- *Rewards:* becoming tapped, through any of these:
  - attacking;
  - crewing, stationing, improvise or convoke (Kilo is an artifact creature);
  - waterbend, which taps creatures and artifacts and is often instant speed;
  - being untapped and tapped again.
- *Fuel:* permanents that carry counters (charge or +1/+1 on your side, stun on theirs), plus tap events.
- *Window:* any time it is tapped. Waterbend costs let it proliferate on opponents' turns.
- *Win:* Kilo deals no damage by itself. It multiplies counters, which turn into mana (Chalice, Cornucopia, Autogenerator), cards (Insight Engine, Etched Oracle), threats (Titan Forge, Golem Foundry, Hangarback) and two finishers that need no combat: Lux Artillery (30 counters means 10 damage to each opponent every end step) and Darksteel Reactor.
- *Dies to:* any removal; it is a 3/3 attacker. It never has to attack, though: crew, station and waterbend tap it at home.
- *Dependence:* **enabler** [J]. The 99 holds 9 more proliferate pieces and the counters keep growing without Kilo, only slower. Recast costs 5 and then 7, and haste gives the trigger the same turn. Protection floor 3 to 4.
- *Dead clauses:* none.

**Rules points to verify.**
1. Tapping Kilo to station triggers it. *Confirmed* (ruling 2025-07-25).
2. Tapping it for crew, improvise, convoke or waterbend triggers it too. *Not checked against a ruling*; the general rule is that a permanent tapped to pay a cost "becomes tapped". If it fails, only the tap-outlets line drops; attacking still works.
3. Proliferate may add to opponents' permanents, so stun counters can be extended. *Confirmed* (ruling 2025-07-25).
4. Lux Artillery counts counters of any kind among your artifacts and creatures. *Oracle text* says "counters" (rulings 2023-02-04).

**Plan.** Kilo taps every turn, by attacking with haste or at home through crew, station or waterbend, and proliferates the
counters on rocks, charge engines and +1/+1 artifact creatures. Those counters become mana, cards and threats. The deck
closes with Lux Artillery dealing 10 to each opponent every end step, or with Darksteel Reactor.
**Backup.** The same countered artifacts attack in the air (Cyberdrive Awakener gives artifact creatures flying and turns
noncreature artifacts into 4/4s) or with trample and haste (Depthshaker Titan). Titan Forge 9/9s and Threefold Thunderhulk
gnomes also attack.
**Archetype.** Hybrid: `plus_one_counters` (primary, the proliferate cue, counted for all counter kinds) with `artifacts` as
its fuel. Land band 36 to 37 (rule of thumb 31 + 3 colors + MV 3 = 37; 9 rocks).

| Function | Tier | Min | Target | Spanish free (weighted) | Main pieces | Reason |
|---|---|---|---|---|---|---|
| counter_sources | gate, early | 12 | 18 | **28** | Repeatable: Insight Engine, Coretapper, Steel Overseer, Hangarback Walker, Crystalline Crawler, Gavel of the Righteous, Golem Foundry, Titan Forge, Lux Cannon, Long-Range Sensor, Empowered Autogenerator, Darksteel Reactor, Inspirit, Uthros Research Craft, Kappa Cannoneer, Katara, Mindless Automaton, Chrome Host Seedshark, Assassin Den, Boar-q-pine. Enter with counters: Everflowing Chalice, Pentad Prism, Astral Cornucopia, Etched Oracle, Threefold Thunderhulk, Patrolling Peacemaker | Kilo only multiplies; the 99 must place the counters. A single source making too few counters is a named trap. |
| counter_payoffs | gate, late | 6 | 8 | **18** | Lux Artillery, Darksteel Reactor, Titan Forge, Golem Foundry, Insight Engine, Etched Oracle, Mindless Automaton, Lux Cannon, Gavel, Empowered Autogenerator, Astral Cornucopia, Everflowing Chalice, Long-Range Sensor, Hangarback, Inspirit, Steel Overseer, Threefold Thunderhulk | Payoffs that grow with proliferate count as payoff and fuel. |
| through_wide_board | gate, early | 10 | 12 | **29** (11 team-level) | Team-level: Lux Artillery, Darksteel Reactor, Reckless Fireweaver, Cyberdrive Awakener, Depthshaker Titan, Organic Extinction (one-sided against nonartifact creatures), Chain Reaction, Fumigate, Hangarback thopters, Kappa Cannoneer, Inspirit at 8+. Plus flyers (Thrummingbird, Tekuthal, Thought Monitor, Seedshark, Cat-Owl, Inspiring Overseer) and flying equipment (Cobbled Wings, Hookblade, Glider Staff) | Board 1, eight chump blockers, is beaten without combat (Lux Artillery, Reactor, Fireweaver) or over it (team flying, trample). |
| through_big_creatures | gate, early | 10 | 12 | **25** | Swords (1 free copy), Chaos Warp, Dispatch (metalcraft is easy here), Firebending Lesson, Misthios's Fury, Bumi Bash, Sandbenders' Storm, Detained by Legionnaires, Lux Cannon, Watery Grasp, Barrels of Blasting Jelly, Meteor Sword, Airbending Lesson, Tranquilize and Rowdy Snowballers (stun counters that Kilo extends), North Pole Patrol, Titan Forge 9/9s, flyers | Board 2 is answered by removal, stun locks and size. |
| counter_doublers (proliferate) | support | 4 | 7 | **7** + Kilo | Repeatable: Surge Conductor, Thrummingbird, Patrolling Peacemaker, Tekuthal (proliferates twice), Karn's Bastion. One-shot at 0.5: Tezzeret's Gambit, Experimental Augury, Ripples of Potential, Deepglow Skate | Keeps the counters climbing when Kilo is removed. |
| tap_outlets (Kilo-specific) | support | 4 | 6 | **16** | Crew: Brute Suit, Ovalchase Dragster, Adrestia. Station: Inspirit, Uthros. Improvise: Kappa Cannoneer, Universal Surveillance, Organic Extinction. Convoke: Astral Wingspan. Waterbend: Katara, Flexible Waterbender, Geyser Leaper, North Pole Patrol, Waterbending Lesson, Watery Grasp. Untap: Cat-Owl, North Pole Patrol | [J] Lets Kilo trigger without attacking into Board 2, and more than once a turn. |
| Ramp (timed, turn 3 or earlier) | base | 10 | 12 | **9** ✗ (−1) | Sol Ring, Arcane Signet, Commander's Sphere, Everflowing Chalice, Pentad Prism, Astral Cornucopia (X=1), Solar Array. At 0.5: Etherium Sculptor, Enthusiastic Mechanaut, Cloud Key, Burnished Hart | Three of the rocks grow with every proliferate (L5: Chalice is good in a proliferate deck), which partly offsets the missing piece. |
| Draw (nets cards) | base | 10 | 12 | **15.5** | Insight Engine, Etched Oracle, Mindless Automaton, Divination, Thirst for Knowledge, Tezzeret's Gambit, Pull from Tomorrow, Universal Surveillance, Waterbending Lesson, Thought Monitor, Uthros, Katara, Jhoira (in the 99), Inspiring Overseer. At 0.5: Escarpment Fortress, Coastal Piracy, Forecasting Fortune Teller | |
| Removal (spot) | base | 6 | 8 | **15.5** | see through_big_creatures | More than needed: the builder keeps 7 to 8 and spends the rest on closers. |
| Wipes | base | 1 | 2 | **4** | Organic Extinction (one-sided here), Chain Reaction, Fumigate, Planar Cleansing | |
| Commander protection | base (enabler) | 3 | 4 | **2.5** ✗ (−0.5) | Inspirit at 8+ (other artifacts gain hexproof and indestructible; Kilo is an artifact), Swan Song, Ripples of Potential at 0.5 | Ripples phases out only the permanents that received a counter. Kilo has one only after Inspirit's combat counter, Keen-Eyed Raven or Momo, so it is conditional. |
| wipe_insurance | support | 2 | 3 | **6** | Inspirit, Wake the Past, Hangarback, Resourceful Defense, Emry, Buried Ruin (land), Darksteel Reactor (indestructible) | |
| Defense while tapped | support | 4 | 6 | **6** | Towering Viewpoint, Escarpment Fortress, Assassin Den, Brute Suit (vigilance), Flexible Waterbender, Knowledge Seeker | |
| Graveyard hate | base | 1 | 1 | **1** | Soul-Guide Lantern (1 free Spanish copy) | |

**Win routes.** Both routes beat three opponents.
- **R1, noncombat:** Lux Artillery and Darksteel Reactor. Lux Artillery hits every opponent for 10 each end step, so four
  end steps kill a full table. The Reactor is an alternate win.
- **R2, combat:** Cyberdrive Awakener, Depthshaker Titan, Titan Forge, Threefold Thunderhulk. These are team-wide flying or
  trampling alpha strikes.
- R1 rests on two cards. It is backed by Reckless Fireweaver (chip damage), recursion (Buried Ruin, Emry, Wake the Past)
  and Long-Range Sensor (Discover 4 can hit either finisher, both mana value 4).

**Fit check.** Adding the minimums once each, with multi-role cards counted once: sources and payoffs together come to about
14 distinct cards, then proliferate +4, ramp +6, draw +6, removal +5, wipe +1, protection +2, wide +3 and tap outlets +2.
The total is about 43, against 63 nonland slots at 36 lands, which leaves about 20 slots of slack. One plan, no second package.

**Gaps.** Ramp is 1 piece short, and commander protection is half a piece short (2.5 of 3). Being an enabler with a cheap
recast and haste softens the protection gap, but it is the first thing to fix. Route R1 has two finishers and no artifact
tutor. Graveyard hate is a single piece.

**Conflicts with the other decks.** None of these is required, and every one has a free replacement in the pool:

| Card | Where the Spanish copies are | Kilo's use | Free replacement in the pool |
|---|---|---|---|
| Command Tower | Spanish copies in Ezio and Toph; the English copy in Azula | land | 38 free nonbasic lands |
| Mind Stone | Azula | ramp | Commander's Sphere, Solar Array |
| Negate | Azula | protection | Swan Song, Ripples |
| Fateful Absence | Ezio and Toph | removal | more than 15 removal pieces |
| Path to Exile | Toph | removal | as above |
| Planar Outburst | Toph | wipe | Organic Extinction |
| Starfall Invocation | Ezio | wipe | Fumigate |
| Aether Gale | Azula | wipe | Chain Reaction |
| Strionic Resonator, Lithoform Engine | Ezio | trigger copy | not needed |
| Helm of the Host, Torrential Gearhulk | Azula | not on plan | none needed |
| Arbaaz Mir | Toph | ping | Reckless Fireweaver |
| Goblin Bombardment | Spanish copy in Toph; English copy in Azula | not on plan | none needed |

Free single Spanish copies whose second copy sits in a deck: Swords to Plowshares, Clifftop Retreat, Rugged Prairie,
Soul-Guide Lantern, Assassin Gauntlet, Coastal Piracy, Exotic Orchard (2 free), Brotherhood Headquarters (3 free).

**Lands.**
- **A:** works. 40 Spanish basics in its colors (Island 11, Plains 14, Mountain 15), all free, plus 38 free nonbasics.
- The best untapped ones: Adarkar Wastes, Battlefield Forge, Shivan Reef, Sulfur Falls, Glacial Fortress, Clifftop Retreat,
  Rugged Prairie, Cascade Bluffs, Skycloud Expanse, Exotic Orchard, Spire of Industry, The Mycosynth Gardens, Karn's Bastion
  (proliferate), Buried Ruin, Ancient Den, Great Furnace and Seat of the Synod.
- The tapped tri-land and duals worth playing: Mystic Monastery, the three Temples, and the three indestructible Bridges.
- 36 to 37 lands with about 16 basics fit easily.
- **B:** brings nothing that matters.

**What a few purchases would fix** (Spanish copies only; inside the shared 10,000 CLP; stock and prices **not checked**):
- **Springleaf Drum, Paradise Mantle or Relic of Legends.** Each is a bridge card that does two jobs: it is ramp, and it lets
  Kilo tap itself at instant speed (Relic of Legends: "Tap an untapped legendary creature you control"). That closes the ramp
  gap and adds a proliferate every turn without attacking. They are cheap commons or uncommons.
- **A Signet or Talisman** (Azorius, Izzet or Boros) for ramp.
- **Swiftfoot Boots or Lightning Greaves** to bring commander protection to its floor of 3.
- Note: Freed from the Real or Pemmin's Aura plus a mana ability on Kilo is an infinite proliferate (Kilo plus two cards).
  Under Bracket 3 that is a late three-card line, so it is allowed. The builder decides if it is organic; it is not proposed here.

### 2.2 Jhoira, Weatherlight Captain (rank 2)

**Reading.** {2}{U}{R} 3/3. "Whenever you cast a historic spell, draw a card."
- *Rewards:* casting artifacts, legendaries and Sagas.
- *Fuel:* 55 free historic cards.
- *Win:* none of its own; the 99 must close.
- *Dies to:* anything; it has no protection.
- *Dependence:* value engine (the draw); protection class 2 to 3.
- *Rules points:* the draw resolves even if the spell is countered (ruling 2020-08-07). Lands and permanents put onto the
  battlefield without being cast do not trigger it. Both are confirmed.

**Plan.** Cast a stream of cheap artifacts and draw a card for each. Close with Lux Artillery or Darksteel Reactor, using the
blue proliferate, or with Reckless Fireweaver pings.
**Backup.** A Cyberdrive or Depthshaker alpha strike, plus Titan Forge.
**Archetype.** `artifacts`; the commander is the payoff.

| Function | Min | Free | Notes |
|---|---|---|---|
| artifact_density (historic) | 20 | 55 | ✓ |
| artifact_payoffs (late; the commander is the payoff) | 6 | about 10 | Uthros, Fireweaver, Golem Foundry, Kappa Cannoneer, Surge Conductor, Thought Monitor, Emry, cost reducers |
| through_wide_board | 10 | 19.5 (9 team-level) | Lux Artillery is slower here: sunburst gives at most 2 counters, and it has 5 proliferate pieces with no Kilo |
| through_big_creatures | 10 | 17 | ✓ |
| Ramp (MV 4: floor 12) | 12 | **9** ✗ (−3) | |
| Draw | 10 | 13 + Jhoira | ✓ |
| Removal | 6 | 9.5 | ✓, but without the white answers |
| Wipes | 2 | **1** ✗ | Chain Reaction only; Aether Gale sits in Azula |
| Commander protection (value class) | 2 | 1.5 ✗ | Swan Song, Ripples at 0.5 (it needs a counter on Jhoira); Negate sits in Azula |
| wipe_insurance | 2 | 3 | |

**Gaps.** Ramp is 3 short for a 4-drop and there is one wipe. The counter finishers are fed by 5 proliferate pieces where
Kilo's deck has 9 plus Kilo. The draw engine is a 3/3 with no protection. The UR pool is a subset of Kilo's; Kilo can play
Jhoira in its 99 and keep the white removal and wipes.
**Conflicts.** Mind Stone, Negate, Aether Gale, Narset's Reversal and Torrential Gearhulk (Azula); Strionic Resonator and
Lithoform Engine (Ezio); Command Tower.
**Lands.** A works: Island 11 and Mountain 15, plus 20 free nonbasics (Shivan Reef, Sulfur Falls, Cascade Bluffs, Silverbluff
Bridge, Temple of Epiphany, Airship Engine Room, Great Furnace, Seat of the Synod and others). B is not needed.
**Purchases.** About three cheap rocks, at least one Izzet Signet or Talisman, and one wipe. That is most of the shared budget.

### 2.3 Ezio, Blade of Vengeance (rank 3)

**Reading.** {3}{U}{B} 5/5 with deathtouch. "Whenever an Assassin you control deals combat damage to a player, draw a card."
- *Fuel:* Assassins that connect.
- *Dependence:* attack engine for the draw. Protection class 6 to 10. Haste needs a promotion test; it stays support,
  because the commander costs 5.

**Plan.** Evasive Assassins connect every turn and draw. Ezio's deathtouch holds the ground.
**Archetype.** `combat_attackers` with typal Assassin as a secondary modifier.

| Function | Min | Free | Notes |
|---|---|---|---|
| attackers | 12 | about 12 | Hookblade Veteran, Brotherhood Spy (unblockable while Ezio is out), Assassin Initiate, Hired Blade, Merciless Harlequin, Poison-Blade Mentor, Ambushers, Patriarch, Adéwalé, plus non-Assassin flyers |
| Assassin members (secondary) | 16 | **9** ✗ | Evie Frye and Ravenloft Adventurer sit in Ezio |
| haste | 4 | **0.5** ✗ | Only the Ovalchase Dragster vehicle. This is lesson L3. |
| team_evasion | 4 | **0** ✗ | Rooftop Bypass makes menace tokens, which fail against Board 1 |
| through_wide_board | 10 | about 8 at team level | Rags//Riches, Decree of Pain, single flyers |
| Ramp (MV 5) | 12 | **9.5** ✗ | |
| Draw / Removal / Wipes | 10 / 6 / 1 | 16 / 10.5 / 2 | ✓ |
| Commander protection (attack engine) | 6 | **2** ✗ | |

**Gaps.** No haste, no team evasion and weak protection: the exact functions the Ezio deck lost games without.
**Conflicts.** Ezio holds Evie Frye, Ravenloft Adventurer, Restart Sequence, Strionic Resonator, Lithoform Engine, and one of
the Spanish copies of The Revelations of Ezio, Assassin Gauntlet and Brotherhood Headquarters. Azula holds Choked Estuary,
Darkwater Catacombs, Nightscape Familiar, Ultimate Price, Aether Gale and Negate. It would be a second Assassin attack deck
competing with the Ezio deck's optimization for the same cards.
**Lands.** A works but is tight: Island 11 and Swamp 10, plus 17 free nonbasics, 6 of them tapped. B (English or bought
basics) would replace the tapped ones.
**Purchases.** Haste and team evasion for Assassins cannot be bought within 10,000 CLP in enough quantity.

### 2.4 Arbaaz Mir (rank 4)

**Reading.** {R}{W} 2/2. "Whenever Arbaaz Mir or another nontoken historic permanent you control enters, Arbaaz Mir deals 1
damage to each opponent and you gain 1 life."
- *Fuel:* 52 free historic permanents.
- *Win:* 1 damage to each opponent per historic permanent, so killing three opponents takes about 40 historic entries.
  That is chip damage, not a route. The closers have to come from elsewhere: Lux Artillery (with only Surge Conductor,
  Patrolling Peacemaker and Karn's Bastion to proliferate in RW), Darksteel Reactor, Wake the Past (a burst of returns,
  each one a ping), Reckless Fireweaver doubling the pings from artifacts.
- *Archetype:* fits no profile; closest is a drain on each entry.

| Function | Min | Free |
|---|---|---|
| Draw | 10 | **3.5** ✗✗ |
| Commander protection (enabler) | 3 | **0** ✗ |
| Ramp | 10 | 8 ✗ |
| Removal / Wipes | 6 / 1 | 13 / 4 ✓ |

**Gaps.** RW has almost no card draw in Spanish. The hand empties by turn 6 (skill step 5).
**Conflicts.** **The commander itself:** its only Spanish copy (no English copy) sits in Toph.
**Lands.** A works (Plains 14 and Mountain 15, plus 22 free nonbasics).

### 2.5 Alibou, Ancient Witness (rank 5)

**Reading.** {3}{R}{W} 4/5. Other artifact creatures have haste. When artifact creatures attack, Alibou deals X damage to any
target, where X is the number of tapped artifacts.
- *Dependence:* attack engine.
- *Win:* one target per attack, so it kills one player at a time. That is a backup route only.
- *Rules point:* if no artifacts are tapped when the trigger resolves, it deals no damage (ruling 2021-04-16, confirmed).

| Function | Min | Free |
|---|---|---|
| attackers (artifact creatures and vehicles) | 12 | 14 (vehicles need crew) |
| haste | 4 | met by the commander |
| Draw | 10 | **3.5** ✗✗ |
| Commander protection (attack engine) | 6 | **0** ✗✗ |
| through_wide_board | 10 | Organic Extinction, Chain Reaction, Fumigate, flyers; Alibou hits one blocker |

**Gaps.** Card draw, protection, and a route that reaches the whole table.
**Conflicts.** Arbaaz Mir (Toph), Command Tower.
**Lands.** A works.

### 2.6 Inspirit, Flagship Vessel (added 2026-11-02, rank 2)

**Reading.** {U}{R}{W} legendary artifact Spacecraft, 5/5, with Station: "Tap another creature you control: put charge
counters equal to its power on this Spacecraft. Station only as a sorcery. It's an artifact creature at 8+." Its two
levels:
- **1+:** at the beginning of combat on your turn, put a +1/+1 counter or two charge counters on up to one *other* target
  artifact.
- **8+:** flying; other artifacts you control have hexproof and indestructible.

What it means for a deck:
- *Rewards:* creature power spent on station, and artifacts that use counters.
- *Fuel:* untapped creatures to tap at sorcery speed, about 8 power in total.
- *Window:* my main phase for station; my beginning of combat for the counter.
- *Win:* at 8+ it is a 5/5 flyer dealing commander damage, one player at a time (21 each), which makes it a backup route
  only. Otherwise it wins through the 99.
- *Dies to:* artifact removal, bounce, and wipes of artifacts or of nonland permanents, at any level. Creature removal can
  only hit it at 8+. Its 8+ protection covers **other** artifacts, never itself.
- *Dependence:* enabler. Plan its protection at 3 to 4.

**Rules points to verify.**
1. A legendary Spacecraft with printed power and toughness may be a commander. Scryfall `is:commander` returns it
   (coordinator, 2026-11-02) and the card is Commander-legal. The current Comprehensive Rules text was **not read**.
2. Below 8 counters it is not a creature. It cannot attack, block, or be hit by creature-only removal and wipes, and it
   deals no commander damage. It is cast from the command zone as an artifact spell, with the normal commander tax. This
   follows the general rules; **not checked** against a ruling (Scryfall lists none for Inspirit).
3. If it leaves the battlefield, its charge counters are lost and a recast starts again at 0. This is the general rule
   that counters do not survive a zone change; **not checked** against a ruling.
4. On the turn it reaches 8 it can attack only if it has been under your control since that turn began (summoning
   sickness). So casting it and stationing it to 8 on the same turn does not let it attack. General rule; **not checked**.
5. Tapping Kilo to station triggers Kilo's proliferate, and the proliferate resolves first. *Confirmed* (Kilo ruling
   2025-07-25). Proliferate also adds charge counters to Inspirit.

**Plan.** Station Inspirit to 8 by turns 5 to 6. Its 1+ ability feeds a counter each combat to the artifact engines. At 8+
it makes the artifact board hexproof and indestructible while the same counter engines grow. It closes with Lux Artillery
or Darksteel Reactor. Inspirit's own charge counters count toward Lux Artillery's 30.
**Backup.** The same alpha strikes as Kilo's (Cyberdrive Awakener, Depthshaker Titan, Titan Forge), plus Inspirit's 5/5
flying commander damage.
**Profile.** Same hybrid and same land band as Kilo (36 to 37). The pool is the same: Inspirit leaves the 99 and Kilo
enters it.

| Function | Min | Free in the 99 (weighted) | Compared with Kilo's deck |
|---|---|---|---|
| counter_sources | 12, or 6 late because the commander is a source | 27 + the commander (1 counter or 2 charge a turn, guaranteed) | The guaranteed adder is fixed at 1 to 2 counters a turn. Kilo's proliferate adds one counter to every permanent that has one, about 4 to 8 per trigger by turn 6. |
| counter_payoffs | 6 | 17 | Same |
| proliferate (support) | 4 | 8 (Kilo is now one of the 99) | Nothing guaranteed. Kilo is seen by turn 5 in about 12 % of games (1 card in 99, 12 cards seen). |
| through_wide / through_big | 10 / 10 | 28 / 25, plus Inspirit as a flyer at 8+ | Same |
| Ramp / Draw / Removal / Wipes | 10 / 10 / 6 / 1 | 9 ✗ / 15.5 / 15.5 / 4 | Same (ramp 1 short) |
| Commander protection (enabler) | 3 | **2** ✗ | Swan Song, plus Ripples of Potential at full weight here (Inspirit always carries counters, so Ripples can phase it out). Nothing in the pool gives an artifact hexproof or indestructible except Inspirit itself, and Negate sits in Azula. |
| wipe_insurance | 2 | 5 + the commander (guaranteed once at 8+) | **Better**: indestructible artifacts are guaranteed instead of a 1-in-99 draw |
| station fuel (new support line) [J] | 4 creatures of power ≥ 2 by turn 4 | 38 free creatures of power 2 or more, mostly 2-power utility at 2 to 3 mana | The commander has its own fuel line. |
| Defense while tapped | 4 | 6 | **Worse**: station taps creatures at sorcery speed, so the creatures used to station cannot also attack or block that turn cycle |

**Both boards and the routes.** Same as Kilo. The commander adds only a single-target 5/5 flying commander-damage backup.
**Fit.** Same arithmetic as Kilo, about 43 of 63 nonland slots.
**Lands.** A works (same 40 basics and 38 nonbasics). B is not needed.
**Conflicts.** Same as Kilo (section 2.1).
**Purchases.** Swiftfoot Boots or Lightning Greaves protect a Kilo, not a noncreature Inspirit. Inspirit's own protection
would need instant counterspells or blink, which the shared budget barely covers.

**Head to head.**

| Point | Kilo as commander (Inspirit in the 99) | Inspirit as commander (Kilo in the 99) |
|---|---|---|
| Engine every game | Proliferate from turn 3, haste, every turn. It scales with the board, and the waterbend outlets make it repeatable. | 1 counter, or 2 charge, on one artifact a turn from about turn 4. Protection only at 8+, around turns 5 to 7. |
| Turns invested | None: Kilo works on the turn it is cast. | About 8 power of creature taps over 2 to 3 sorcery-speed turns. Those creatures do not attack or block that turn. |
| After removal | Recast for 5, with haste, and proliferate at once. Nothing is lost. | Recast for 5 and station again from 0; the 2 to 3 turns invested are lost. It cannot protect itself. |
| Removal that hits it | Creature and artifact removal | Artifact removal, nonland-permanent removal and bounce before 8+; everything after |
| Wipe insurance | 6 pieces in the 99; Inspirit is one card in 99 | Guaranteed at 8+: Inspirit's strongest point |
| The other legend in the 99 | Inspirit, if drawn: Kilo stations it with 3 power plus a proliferate, so it reaches 8 in about 2 turns. Strong. | Kilo, if drawn (about 12 % by turn 5): a good extra proliferate source |
| Speed toward Lux Artillery's 30 counters | Fast; the counters grow faster the more permanents carry them | Slower; about 8 to 10 from station plus about 2 a turn, unless Kilo is drawn |
| Commander protection after cheap purchases | 2.5 now; 3.5 with Greaves or Boots | 2 now, with no cheap artifact-only fix in the pool |

**Verdict.** Kilo stays first. The deck's plan is to multiply counters, and only Kilo makes the multiplier certain and
immediate in every game. Inspirit as commander makes wipe insurance certain, but Kilo's deck already has 6 such pieces.
The price is a slow, removable investment and a commander that cannot protect itself. Inspirit beats Jhoira as the
runner-up: it has the same complete pool, including the white removal and wipes, plus a guaranteed counter source and
late protection. It is the best card in Kilo's 99.

## 3. Recommendation

**Choose Kilo, Apogee Mind.** The runner-up is Jhoira, Weatherlight Captain.

Why Kilo:
1. **One plan, densely supported.** Every gate function is two to three times its minimum (sources 28, payoffs 18, wide 29,
   big 25), so the builder chooses quality instead of filling slots. This is the only candidate where that is true.
2. **Consistency.** The commander costs 3 and has haste, so it can be recast quickly. Nine more proliferate pieces keep the
   plan going without it. Sixteen tap outlets let it trigger without attacking into big blockers, which removes the
   failure mode of the Ezio games: a fragile attacker that must connect.
3. **Both reference boards and two disjoint routes.** One route needs no combat and hits each opponent (Lux Artillery,
   Darksteel Reactor); the other is a team-wide air or trample alpha strike.
4. **Mana works in scenario A** with only free Spanish cards: 40 basics and 38 nonbasics.
5. **Broad synergy, few mini-combos (L1, L7).** Almost every counter card does something by itself (a rock, a draw engine, a
   body) and grows with every proliferate.
6. **No card has to be taken from Toph, Azula or Ezio.**
7. It is the owner's precon base, and his Spanish collection holds 92 of EDHREC's Kilo cards. That is a prior, not the reason.

Why Jhoira is second: the same artifacts, with a real draw engine, but ramp 3 short, one wipe, no protection and slower
finishers. Every strength it has is available to Kilo, which can play Jhoira in its 99.

### 3b. Revised recommendation (2026-11-02, after Inspirit was added)
**Choose Kilo, Apogee Mind.** The runner-up is now **Inspirit, Flagship Vessel**; Jhoira drops to third.

Kilo's engine works from the turn it is cast, every game, and it scales with the board. Inspirit needs 2 to 3 turns of
sorcery-speed creature taps, loses them to any artifact removal or bounce, and never protects itself. Its one advantage,
guaranteed wipe insurance, covers a function Kilo's deck already meets with 6 pieces. Inspirit is the first card for Kilo's
99, where Kilo stations it to 8 in about two turns.

## 4. Open questions for the owner

1. **Commander:** do you accept Kilo, Apogee Mind for the Spanish deck, so that "Counter Intelligence" becomes its base?
   Inspirit goes in the 99 (section 2.6). Or do you prefer Inspirit as commander, accepting a slower start in exchange for
   guaranteed artifact protection once it is stationed?
2. **Basics (scenario A or B):** Kilo does not need B, since 40 Spanish basics in its colors are free. Should the pending
   decision still be recorded, for the record and for future iterations?
3. **Purchases from the shared 10,000 CLP:** may the Spanish deck use part of it? The suggested lines, about 2,000 to 3,000
   CLP if stock exists, are one or two of Springleaf Drum, Paradise Mantle and Relic of Legends (ramp, and they let Kilo tap
   at instant speed), plus Swiftfoot Boots or Lightning Greaves (protection 2.5 to 3.5). Stock and prices are not checked
   yet.
4. **Command Tower:** the three copies (2 Spanish, 1 English) sit in Toph, Ezio and Azula. Should Kilo get one Spanish copy?
   If so, a bilingual deck would play a different land. Without it, Kilo uses Exotic Orchard and the tri-land.
5. **Infinite lines:** if a later purchase brings Freed from the Real or Pemmin's Aura, Kilo can proliferate without limit
   with a mana ability. Bracket 3 allows it as a late three-card line. Do you want it, or should the deck win by its organic
   routes only?
