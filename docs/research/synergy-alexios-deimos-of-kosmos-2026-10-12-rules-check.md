Model ID: claude-sonnet-5-5

# Rules check: synergy report for Alexios, Deimos of Kosmos (2026-10-12)

Independent check of `synergy-alexios-deimos-of-kosmos-2026-10-11.md` (revised 2026-10-12) against the official Wizards rulings on disk. Phase 3 (synergy research), rules sub-check. The original report was not edited.

| Input | Value |
|---|---|
| Rulings file | `data/cache/rulings_pool.jsonl`, 68,266 lines. The source `rulings-20261012090033.jsonl.gz` has the sha256 recorded in the manifest (checked: match). Scryfall file date 2026-10-12T09:00:33Z |
| Pool | `pool_alexios-deimos-of-kosmos.jsonl` (oracle text). Not used: network, `data/raw/`, Comprehensive Rules text (absent) |
| Coverage | Commander (6 rulings) and the 15 `core` cards read in full; rulings of all 220 candidates and ~165 hazard/combo names read; whole file keyword-searched for general mechanics |
| Absence check | Sol Ring, Sword of the Animist and Mountain have 0 rulings in the raw bulk file as well (checked by oracle_id), so the gap is real, not a filter artifact |
| Labels | CONFIRMED = a ruling or the oracle text says it. "(inference)" = follows from a ruling about a similar card. CR numbers cited from memory are marked unverified |

## 1. Verdict table

### 1a. Commander section and weaknesses

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| C1 | Must attack each combat; each player controls it on their turn; counter and haste at every upkeep | CONFIRMED | Oracle; Alexios 2024-07-05: attacks if able, "tapped" means no attack |
| C2 | Can never attack you, but can attack your planeswalkers (Chandra, Jeska, Ugin) | CONFIRMED | Alexios 2024-07-05: "Alexios can attack planeswalkers its owner controls and battles its owner protects." |
| C3 | The active opponent picks the target | CONFIRMED (inference) | Shiny Impetus 2023-06-30 (goad): the creature's controller chooses which opponent it attacks |
| C4 | Counters stay when control changes | CONFIRMED (inference) | Mark of Mutiny 2017-11-17: the counter "remains on the creature after the control-changing effect ends" |
| C5 | Can't be sacrificed, edicts miss | CONFIRMED | Alexios 2024-07-05 (3 rulings): with other creatures you must sacrifice one of those. Assault Suit 2014-11-07 same wording |
| C6 | Opponents stop the forced attack by tapping it for a cost (crew, convoke) | PARTLY | Alexios 2024-07-05 confirms "tapped = doesn't attack" and "isn't forced to pay" attack costs. Crew and convoke are not in the rulings (CR 702.122 / 702.51, unverified). Attack taxes are not mentioned in the report (section 2) |
| C7 | Removal sends it to the command zone, loses counters and auras, tax rises | PARTLY | Sanctum of Eternity 2019-08-23 (tax); Inalla 2017-08-25 (zone change = new object). "Owner may choose" is CR 903.9, no ruling in the file |
| C8 | Never blocks for you | CONFIRMED (oracle) | An opponent controls it on every turn but yours, and it is tapped after attacking |
| C9 | Granted abilities and lifelink help whoever controls it | CONFIRMED | Cloak and Dagger 2008-04-01; Armory Automaton 2016-11-08; Grafted Exoskeleton 2011-01-01 (lifelink pays "its controller") |
| C10 | Hexproof or shroud gear stops your targeting on opponents' turns (Rogue's Passage, Magnetic Theft) | CONFIRMED | Champion's Helm 2011-09-22: you are "an opponent of the controller", so you can't target it. Rogue's Passage and Magnetic Theft target the creature |
| C11 | Same list includes **Bolt Bend** | CONTRADICTED | Bolt Bend (oracle) targets a spell or ability, not Alexios; Bolt Bend 2024-11-08: its target "doesn't have to be" a creature you control. Its limit is the discount, which needs you to control a 4-power creature (your turn only) |
| C12 | Ward makes you pay | CONFIRMED | Ward is relative to the creature's controller (oracle reminder text); Leather Armor 2021-07-23 |

### 1b. Rules readings R1 to R8

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| R1 | Equipment stays attached on control change; its own triggers ("you draw") belong to the Equipment's controller | **CONFIRMED** | Pact Weapon 2022-06-10: "if an opponent gains control of the equipped creature without gaining control of Pact Weapon and attacks with it, you will draw a card"; same ruling: still attached, you still control it. Armory Automaton 2016-11-08 (an Equipment ability that says "you" refers to the Equipment's controller). Mass Mutiny 2012-06-01, Cloak and Dagger 2008-04-01, Champion's Helm 2011-09-22 |
| R2 | A quoted granted ability belongs to whoever controls the creature | **CONFIRMED** | Cloak and Dagger 2008-04-01: "Only the creature's controller can activate any activated abilities the Equipment grants" and "you" in them is that player. Armory Automaton 2016-11-08. Splinter Twin 2010-06-15 ("That creature's controller ... can activate it"). The six named cards are all quoted grants (oracle). Backgrounds: same rule by analogy, no Background-specific ruling |
| R3 | "Enchant creature you control" Auras fall off when an opponent gains control; plain "Enchant creature" stay | **CONFIRMED** | Inferno Fist 2014-07-18 (put into the graveyard as a state-based action); Krovikan Plague 2004-10-04; Aura Finesse 2010-06-15 ("an opponent controls the creature"). Oracle: Inferno Fist is "Enchant creature you control", Shiny Impetus and Sound of Drums are "Enchant creature". See N1 for a different way they fall off |
| R4 | Commander damage counted per commander, whoever controls it | **CONFIRMED** | Tahngarth 2019-08-23: "It doesn't matter who controls the commander as it deals damage." Aethersnatch 2015-11-04 |
| R5 | Token created "tapped and attacking" under a non-active player enters tapped, not attacking | **CONFIRMED** | Crafty Cutpurse 2018-01-19: "created tapped but not attacking". Andúril 2023-06-16: opponent-controlled equipped creature: "the Spirits would not enter the battlefield attacking". Captain's Claws has the same wording (inference) |
| R6 | "Your commander" triggers (Tome of Legends) fire while an opponent controls Alexios | **CONFIRMED** | Tome of Legends 2019-10-04: "if another player controls your commander, you'll still put a page counter on Tome of Legends if it attacks." |
| R7 | Previous player still controls Alexios at each upkeep, so granted "your upkeep" triggers never fire | NOT COVERED | No ruling on trigger timing or on Homeward Path (only ownership, 2011-09-22). Logic is the standard trigger rule (CR 603.2 / 603.3a, unverified); no ruling contradicts it |
| R8 | Legend rule kills copies; non-legendary copies only from Helm, Tempestra, Delina, Hall of Mirrors; Mirror Box, Mirror Gallery, Hall of Echoes switch it off; Kiki-Jiki can't target | **CONFIRMED** | Splinter Twin 2013-07-01 ("put either the original creature or the token into the graveyard"); Blade of Selves 2015-11-04 ("you'll choose one of them to remain"); Helm of the Host 2018-04-27 (token "isn't legendary"); Mirror Box 2022-02-18. Oracle for Tempestra, Delina, Hall of Mirrors, Kiki-Jiki ("nonlegendary"), Mirror Gallery, Hall of Echoes |

### 1c. Interaction claims, hazards and combos

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| X1 | Sword of Fire and Ice: 2 damage and a card on every hit, every turn | CONFIRMED | R1 chain (section 3); Sword of Fire and Ice 2020-08-07 |
| X2 | Sword of the Animist / Bitterthorn: a land on every attack, every player's turn | CONFIRMED (inference) | No rulings on the cards; Armory Automaton 2016-11-08 and Pact Weapon 2022-06-10 (attack triggers of Equipment) |
| X3 | Shiny Impetus: Treasure for you on every attack | CONFIRMED | Shiny Impetus 2020-04-17: "causes you to create a Treasure token, not the attacking creature's controller" |
| X4 | Sword of Truth and Justice: counter on your creature on opponents' turns, proliferate adds 1 to Alexios (2 on your turn) | CONFIRMED | Proliferate 2023-02-04: "any permanent that has a counter, including ones controlled by opponents". Karn's Bastion same |
| X5 | Sword of Feast and Famine: instant-speed mana on opponents' turns | CONFIRMED | 2020-08-07: you can tap lands "while the triggered ability is on the stack" (unspent mana lost at end of damage step) |
| X6 | Sword of Forge and Frontier best on your turn; Buster Sword, Glamdring, Sword of Once and Future cast free spells on opponents' turns | CONFIRMED | Forge and Frontier 2023-02-04 ("on an opponent's turn ... instants, mostly"); Buster Sword 2025-06-06, Glamdring 2023-06-16, Once and Future 2023-04-14 (timing restrictions ignored) |
| X7 | Andúril / Captain's Claws tokens tapped; Moonsilver Spear Angel untapped, a real blocker | CONFIRMED | Andúril 2023-06-16; oracle (Spear: "create a 4/4 white Angel", no "tapped"). The Angel can block only attackers that hit you or your planeswalkers |
| X8 | Jeska's Will: both modes while you control Alexios; Will of the Jeskai same | CONFIRMED | Jeska's Will 2026-03-20: "controlling any commander will satisfy its condition" |
| X9 | Deflecting Swat, Bolt Bend, Not of This World work only on your turn | CONFIRMED | Deflecting Swat 2020-04-17 (control a commander); Bolt Bend 2024-11-08; Not of This World 2010-06-15 (checks the target's current controller and power) |
| X10 | Kediss: your turn, the hit is copied to each other opponent | CONFIRMED | Kediss 2020-11-10 ("any commander you control"). Missed detail: the copy "isn't combat damage" and "isn't tracked with combat damage dealt by commanders" |
| X11 | Dictate, Furnace, Bitter Feud, Curse of Bloodletting apply to any source; Twinflame Tyrant, Fiery Emancipation only sources you control | CONFIRMED | Dictate 2014-04-26 ("doesn't matter who controls the source"); Curse of Bloodletting 2011-01-22; Twinflame Tyrant 2024-11-08 + oracle ("a source you control") |
| X12 | "Symmetric doublers are lopsided here because Alexios's damage always goes to opponents" | PARTLY | Same Dictate ruling: all sources double, also opponents' attacks on you. True only for Alexios's own damage |
| X13 | Tempestra copy "can't be removed" by its sacrifice clause; Delina copies are temporary | CONFIRMED (inference) | Alexios 2024-07-05 (can't be sacrificed) + Tempestra 2026-01-27 ("copies exactly what was printed"). Delina's clause is "exile", which works (Delina 2021-07-23). Consequence missed (R-change 7) |
| X14 | Grafted Wargear's sacrifice clause can't hit Alexios | CONFIRMED | Alexios 2024-07-05; Grafted Wargear 2004-12-01 (needs control) |
| X15 | Monastery Raid / Overpowering Attack freerunning after Alexios connects; Light Up the Stage spectacle | CONFIRMED | Monastery Raid 2024-07-05 ("commander you control"; your turn only, both are sorceries); Light Up the Stage 2024-01-12 (damage = life loss) |
| X16 | Furious Rise, Bonders' Enclave count Alexios on your turn | CONFIRMED | Furious Rise 2020-06-23; Bonders' Enclave 2020-04-17 |
| X17 | Greaves / Whispersilk shroud blocks your later equips | CONFIRMED | Lightning Greaves 2020-08-07 ("or target it with anything else") |
| X18 | Mithril Coat "flash, auto-attaches to a legendary creature" listed as protection | PARTLY | Oracle: "target legendary creature you control". Flashed on an opponent's turn it has no legal target. Same for Hammer of Nazahn, Embercleave, Mjölnir Storm Hammer, Vibranium |
| X19 | Extra combats make Alexios attack again; Genji Glove untaps only Alexios, Hexplate all attackers | CONFIRMED | Relentless Assault 2025-09-19 ("must attack again if it can"); oracle of Genji Glove and Hexplate Wallbreaker |
| X20 | Sanctum of Eternity saves Alexios "on your turn"; Command Beacon rescues from tax | CONFIRMED | Oracle ("Activate only during your turn", "commander you own"); Command Beacon 2015-11-04 |
| X21 | Argentum Armor destroys a permanent on every attack | CONFIRMED | Argentum Armor 2011-01-01 (resolves in declare attackers; mandatory, may target your own permanent) |
| X22 | Worldslayer "on a creature that attacks every turn wipes the board every turn" | PARTLY | Worldslayer 2011-09-22: "The equipped creature is also destroyed." Every turn only if the carrier is indestructible (Mithril Coat, Hammer of Nazahn, Darksteel Plate, Kaldra Compleat are all candidates) |
| X23 | Speed table: each multiplier doubles the hit "on every turn" | PARTLY | Oracle: Death Kiss triggers on a creature "an opponent controls" (opponents' turns only); Kediss needs a commander "you control" (your turn only, not a multiplier of one hit) |
| X24 | Mindslaver, The Dominion Bracelet: opponent control, review flag | CONFIRMED | Mindslaver 2024-04-12; Dominion Bracelet 2025-07-25 (cost reduced by power: Alexios makes it near free). Supports a hard exclude (R-change 9) |
| X25 | Kediss + Grafted Exoskeleton wins (combo 8) | CONFIRMED | Exoskeleton 2011-01-01: infect applies "to any damage, not just combat damage"; Kediss ruling above |
| X26 | Combos 2, 3: Aggravated Assault loops | CONFIRMED | Aggravated Assault 2004-10-04 (several activations per turn); Neheb 2017-07-14 (later main phases are postcombat, triggers each) |
| X27 | Bloodthirster / Raphael + Helm work from text (open question 3) | CONFIRMED (oracle) | Helm of the Host 2018-04-27: token isn't legendary, gains haste; Helm triggers at each combat's beginning, so each fresh copy re-triggers "first time" / "already attacked" clauses |
| X28 | Tome of Legends is a core draw engine | PARTLY | Rule confirmed (R6) but oracle: `{1}, {T}`, remove a counter: draw one card. One draw per round, counters pile up |
| X29 | Blasphemous Act: Alexios survives at 14+ toughness | CONFIRMED | Oracle (13 damage); Blasphemous Act 2020-11-10 (cost) |
| X30 | "How it is usually played" and community patterns | NOT COVERED | Not a rules claim; rulings cannot settle it |
| X31 | Bracket policy statements (tutors, land denial, Game Changers, class rules) | NOT COVERED | Policy, not rulings |

### 1d. Claim implied by the primary build

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| N1 | Sword of Fire and Ice, Shiny Impetus and Spectacular Showdown (all `core`) work together on Alexios | **CONTRADICTED** | Sword of Fire and Ice gives protection from red. Sword of Truth and Justice 2019-06-14: protection means "can't be the target of spells of that color ... can't be enchanted or equipped by Auras or Equipment of that color". Aura Finesse 2010-06-15 uses exactly this case (red Aura, protection from red). Shiny Impetus and The Sound of Drums are red Auras: they go to the graveyard when the Sword attaches; Spectacular Showdown (red) can no longer target Alexios |

## 2. Required report changes, by severity

1. **HIGH. Protection-from-color conflicts (N1).**
   - Pro-red Swords: Sword of Fire and Ice (core), War and Peace, Forge and Frontier, Sinew and Steel. Pro instants and sorceries: Sword of Wealth and Power.
   - Red Auras that can't stay: Shiny Impetus (core), The Sound of Drums.
   - Red Equipment that can't attach (same definition; the state-based action for Equipment is CR 704.5n, unverified): The Spear of Leonidas, Komainu Battle Armor, Lizard Blades, Embercleave, Two-Handed Axe, Mjölnir, Hammer of Thor.
   - Red sources that can't target Alexios: Spectacular Showdown (cast it before the Sword), Magnetic Theft, Jeska's 0 ability.
   - Upside: your own red sweepers (Blasphemous Act and others) deal no damage to a pro-red Alexios.
   - Change: split archetype A into a pro-red branch (no red Auras or red Equipment) and a branch without those Swords, and say so in the core list and the combo table.
2. **HIGH. Section 1 rules table and open question 4.** Replace "Unverified" with CONFIRMED plus the citations above for R1, R2, R3, R4, R5, R6; keep R7 as "logic only, no ruling"; add rulings for R8. Delete the sentence that rulings could not be fetched and close open question 4.
3. **MEDIUM. Double strike doubles every combat-damage trigger.** Warren Instigator 2009-10-01 ("its triggered ability will thus trigger twice"), Michiko Konda 2005-06-01. With Spectacular Showdown (core), Leyline Axe, Fireshrieker, Lizard Blades, Embercleave or the Spear's Bull Rush, each Sword, Mask, Jitte, Quietus Spike, Goldvein Pick trigger fires twice per combat (Quietus Spike halves twice). Add to section 7 and to the multiplier note; the "roughly doubles the damage" line understates the engine.
4. **MEDIUM. Remove Bolt Bend from the hexproof weakness list (C11).** Add: its discount and the Deflecting Swat free cast need you to control Alexios, so they are your-turn tools.
5. **MEDIUM. Attack costs are a speed brake.** Alexios 2024-07-05: if there is a cost to attack, the controller "isn't forced to pay" and does not attack. Add attack taxes (Ghostly Prison, Propaganda, Archangel of Tithes style) to the real-game brakes and to the Monte Carlo opponent model. They also stop the 4-attacks-per-round assumption.
6. **MEDIUM. Protection removes chump blocks.** Commander's Plate (core) gives protection from white, blue, black, green: those creatures can't block Alexios (2019-06-14 definition). With Sword of Fire and Ice only colorless creatures can block. The "chump blocks" brake in section 7 and the Infiltration Lens value (draws only when blocked) must be revised; the speed-risk estimate goes up.
7. **MEDIUM. Tempestra.** Its "sacrifice at the next end step" cannot happen to a copy of Alexios (copied text), so every activation leaves a permanent non-legendary Alexios that is also passed around. Treat it like Helm of the Host in the speed table, not as a temporary copy; keep it out of the primary build until Phase 4 decides.
8. **LOW. Mithril Coat and similar (X18).** State "your turn only" for the attach trigger; the flash save only works while you control Alexios.
9. **LOW. Worldslayer (X22) and The Dominion Bracelet (X24).** Worldslayer destroys its carrier too; the board wipe each combat needs indestructible gear that the deck wants. The Bracelet's granted ability is the controller's: an opponent holding Alexios can use a near-free "control a player's turn". Make both hard excludes and say why.
10. **LOW. Speed table wording (X23).** Death Kiss: opponents' turns only. Kediss: your turn only, and its copied damage is not combat damage and not commander damage (Kediss 2020-11-10). Fiery Emancipation and Twinflame Tyrant: your turn only.
11. **LOW. Illustration of 110 damage (section 3 below).** State the assumptions: all damage to players, none to planeswalkers or battles, no taxes, no removal.
12. **LOW. Symmetric doublers (X12).** Reword: lopsided only for Alexios's own damage; opponents' attacks on you double too.
13. **LOW. Alexios rulings not in the report.** 2024-07-05: if its controller leaves the game it returns to the controlling player who most recently controlled it; if its owner leaves, it leaves; it may attack battles its owner protects.
14. **LOW. Counter and board accelerators missing from the speed table (oracle, no ruling needed).** Sword of Hours, Armory of Iroas, Pip-Boy 3000 and Sword of Truth and Justice add counters on every attack, Moonsilver Spear makes a 4/4 flier on every attack, Sword of Body and Mind mills 10 per hit. The 110-damage figure uses only the upkeep counters.
15. **LOW. Smaller wording.**
    - Sticky Fingers' "When enchanted creature dies, draw a card" is the Aura's own trigger (yours); only the Treasure grant goes to the opponent.
    - Vengeful Ancestor pings the controller of any goaded creature, so Shiny Impetus or Showdown goad on Alexios also pings you on your turn.

## 3. The two load-bearing checks

### R1 chain: equipment triggers on every turn

| Link | Needed fact | Source |
|---|---|---|
| 1 | Equip targets "a creature you control", sorcery speed: you can equip only on your turn, which is when you control Alexios | Blackblade Reforged 2018-04-27 |
| 2 | Equipment stays attached when the creature changes controller | Pact Weapon 2022-06-10; Champion's Helm 2011-09-22 |
| 3 | You keep controlling the Equipment | Mass Mutiny 2012-06-01; Cloak and Dagger 2008-04-01 |
| 4 | "Whenever equipped creature attacks / deals combat damage" fires on any player's turn if attached at declaration | Armory Automaton 2016-11-08; Andúril 2023-06-16; Forge and Frontier 2023-02-04 |
| 5 | The trigger is controlled by the Equipment's controller | Pact Weapon 2022-06-10; Armory Automaton 2016-11-08 |
| 6 | Quoted grants are NOT yours (cards on the R2 list) | Cloak and Dagger 2008-04-01 |

Result: the chain holds, every link has a ruling. Break points: pro-red colors (N1), shroud gear blocks equips (X17), artifact removal, Alexios leaving play, and attack taxes or taps that cancel the attack (C6, change 5).

### "110 damage before turn 7"

- Arithmetic checked: cast on your turn 4, 11 upkeeps before your turn 7 (3 + 1 + 3 + 1 + 3), power 5 to 15, sum 110 (`sum(range(5,16))`), pigeonhole `ceil(110/3) = 37`.
- Rules support: R4 (commander damage counted for each of the three opponents whoever controlled Alexios) and C1 (haste each upkeep, so every upkeep is an attack).
- Not guaranteed by the rulings: the controller of Alexios may attack a planeswalker or battle instead of a player (Alexios 2024-07-05), and attack costs or taps cancel attacks. So 110 is an upper bound on damage to players, and "at least 37 to one opponent" holds only if all of it hits the three players.
- It excludes Kediss's copies (not commander damage) and all equipment, counters and multipliers (change 3, 14).

## 4. Rulings the report missed

| Card | Ruling | Effect |
|---|---|---|
| Alexios | 2024-07-05 attack costs, controller leaves, owner leaves, battles | Changes 5 and 13 |
| Commander's Plate (core) | 2020-11-10: no commander colors = protection from each color; protection definition via Sword rulings 2019-06-14 | Can't be blocked by protected colors (change 6) |
| Shiny Impetus (core) | 2023-06-30 goad rulings: a goaded creature that changes controller must attack again; "being goaded isn't an ability" | No change; goad from Impetus is redundant with "can't attack its owner" |
| Rogue's Passage (core) | 2018-12-07: after blockers are declared the ability does not unblock | Activate in the declare attackers step, before blocks |
| Spectacular Showdown (core) | 2024-01-12 overload rulings only | Overload ignores hexproof and protection, but the single-target mode does not (N1) |
| Tome of Legends (core) | 2019-10-04 | R6; draw capped by `{T}` (X28) |
| Sol Ring, Sword of the Animist, Mountain | no rulings | Nothing to add |

## 5. Questions the rulings could not answer

1. R7: when exactly a granted "at the beginning of your upkeep" trigger is checked relative to Alexios's own trigger (CR 603.2, 603.3a); no ruling.
2. Jeska, Thrice Reborn 0 ability: does "until your next turn" tripling persist after an opponent takes control of the creature (CR 611.2c, 614)? Not in the Jeska rulings; the report's claim is plausible but unverified.
3. Crew and convoke taps on a creature that must attack (CR 702.122, 702.51): only the generic "tapped" ruling exists.
4. Whether a non-controller can pay "Exile The Dominion Bracelet" for a granted ability (cost-payment rule, CR 118.x): unverified.
5. Assault Suit's "until end of turn" control against Alexios's permanent control effect (layer 2 timestamps): no ruling; both effects name the same player, so likely harmless.
6. Backgrounds: no ruling that the granted ability's controller is the creature's controller (only the Equipment and Aura cases).
7. Bracket policy and Game Changer flags (2026-10-12 announcement): outside rulings.
