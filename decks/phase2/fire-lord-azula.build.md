# Fire Lord Azula: Phase 2 build notes (round 3, 2026-11-02)

Upgrade of the Phase 1 list he plays today (`decks/scanned/fire-lord-azula.txt`, Salt 8.4), checked against his original list
(`data/raw/Azula.txt`). Pool: `data/model/phase2/pool-fire-lord-azula.json`. Language policy `both`. Every card checked against
`data/model/phase2/assignment.json`: all new cards are free copies; Pull from Tomorrow and Hidden Footblade are Azula's;
Overpowering Attack is an accepted loan; Soul-Guide Lantern is a purchase and Run Amok stands in for it in the physical list.
- Round 3 applies the adversarial review `decks/reports/review-fire-lord-azula.md` (verdict FIX, blocking item B1: real draw
  about 9 of 12) and the owner context of 2026-11-02 (maximize power; Salt second objective, stay at 7.5 or more).
- Gate: `decks/reports/consistency-fire-lord-azula.md` PASS (0 failures, 2 WARNs with reasons in section 9).
- Bracket: `scripts/check_phase2_bracket.py` PASS (floor 3, 0 Game Changers; live Scryfall `is:gamechanger` search, 53 cards,
  none in the list). Spellbook flags one line, Godo + Helm of the Host, classed late (R11).

## 1. Commander reading and rules points

Fire Lord Azula {1}{U}{B}{R}, 4/4. Firebending 2: when she attacks, add {R}{R} that lasts until end of combat. Whenever you cast
a spell while she is attacking, copy it (new targets allowed; a copied permanent spell becomes a token).
- Rewards: spells cast in HER combat window (declare attackers to end of combat). Fuel: instants and flash cards in hand when
  she attacks, and mana in that window. Each cast spends a card; the hand empties fastest of his decks (owner): draw is the
  first need after the window itself.
- Window mana: {R}{R} per attack; Zuko, Exiled Prince adds {R}{R}{R} and Azula, On the Hunt {R}{R} when they attack beside her;
  Fire Nation Palace adds firebending 4. Keepers (Horizon Stone, Electro, Ozai) hold the rest. Every extra combat (Overpowering
  Attack, Godo) is a new firebending trigger and a new window.
- Wins: copied burn (Comet Storm with two kicks hits all three opponents twice), copied draw and removal as two-for-ones,
  commander damage pumped by copied tricks, Helm of the Host copies of her, extra combats.
- Dies to: targeted removal, wipes, BLOCKS by bigger creatures (owner: opponents block when they think he cannot pump), the
  crack-back while tapped, and any "spells only at sorcery speed" effect (shuts the window).
- Dependence: ATTACK ENGINE (protection 6 to 8). A block does not stop the copies but can kill her: the deck makes a block a
  losing trade with copied tricks after blocks, first strike, trample, hexproof and copied removal on the blocker.
- Copies are not cast: Electro's {R} and Thermo-Alchemist's untap trigger only on the original; magecraft (Archmage, Storm-Kiln)
  says "cast or copy" and triggers twice. A spell cast "without paying its mana cost" (Torrential Gearhulk, Electrodominance) has
  X = 0: never recast Comet Storm or Pull from Tomorrow that way.

Rules points to verify:
| # | Point | Status | What falls if wrong |
|---|---|---|---|
| R1 | Horizon Stone keeps firebending mana: firebending (ruling 2025-10-02) is "until end of combat, you don't lose this mana as steps end"; at end of combat it would be lost, and Horizon Stone replaces the loss (it becomes colorless). Horizon Stone ruling (2020-11-10): unspent mana is retained across steps, phases and turns. | Confirmed by both rulings; no joint ruling. | Horizon Stone as the window keeper. |
| R2 | With Horizon Stone, mana made in the last opponent's end step survives into my turn as colorless: lands tap twice per cycle for generic costs (X, equip, Zuko's {3}). | Confirmed by the same ruling. | X size. |
| R3 | Copies trigger magecraft; Electro and Thermo-Alchemist see only the cast. | Confirmed (Oracle, Azula ruling). | Draw and treasure per combat. |
| R4 | A copy skips additional costs, keeps X and kicker: copied Big Score and Thrill draw without a discard. | Confirmed (Azula rulings). | Half-weight draw pieces. |
| R5 | Copied permanent spells resolve as tokens: Dualcaster and Gearhulk give two ETBs. | Confirmed (ruling). | Payoff value. |
| R6 | Fire Nation Palace on Azula: two firebending instances trigger separately. | Confirmed (Azula ruling). | Big-turn mana. |
| R7 | Day of Black Sun X=0 destroys every created token (MV 0). | Rules knowledge, not checked. | Board 1 answer. |
| R8 | A Helm token of Azula has her trigger; two Azulas copy each spell twice. | Rules knowledge, not checked. | Combat route scaling. |
| R9 | Electrodominance's free cast ignores timing and is copied while she attacks; it has X = 0 if the card has X. | Rules knowledge, not checked. | Electrodominance value. |
| R10 | Deflecting Swat is free while I control a commander. | Confirmed (Oracle). | Free protection. |
| R11 | **Godo + Helm of the Host is a late line.** Godo ({5}{R}) puts Helm onto the battlefield; equip {5} at sorcery speed; then a hasty Godo token every combat: unlimited combats. 11 mana over at least two main phases. Floor: turn 4 (Sol Ring turn 1, a 2-mana rock turn 2, Godo turn 3, equip turn 4), about 5 % of games by turn 6 (reviewer's odds); typical turn 7 to 9; Godo is not tutorable (Teachings and Solve find instants and sorceries only). Combats, not extra turns. It does not win by itself: it wins with Azula vigilant (Haunted Cloak) so each combat is a new window, plus a keeper. Script and Spellbook: "two-card combo, late". | Confirmed late by the script; floor corrected per review I4. | If judged early, cut Godo; Helm stays. |
| R12 | Overpowering Attack's freerunning {2}{R} is legal once Azula (a commander) dealt combat damage to a player this turn; in a main phase it untaps the attackers and adds a combat and a main phase. Not an extra turn. If she was blocked it costs {3}{R}{R}. | Oracle. | Its cheap cost. |
| R13 | Zuko, Exiled Prince's {3} activation is payable with firebending {R} (generic cost) in the window; the exiled card is playable this turn, and an instant cast from it while Azula attacks is copied. | Rules knowledge (mana of any color pays generic), not checked in a ruling. | Zuko as a window converter. |

## 2. Plan and backup

- **Plan.** Azula attacks every turn (haste and hexproof from equipment, counters and redirects behind her); while she attacks
  she copies every instant and flash spell cast with her firebending mana and the cost reducers, so each draw, removal, burn and
  pump spell is a two-for-one; Horizon Stone, Electro and Ozai keep the leftover window mana; she closes against all three
  opponents with copied multi-target X burn (Comet Storm, Electrodominance) and with combat: herself, Helm of the Host copies,
  extra combats (Overpowering Attack, Godo) and Ozai, while copied pump tricks make blocking her a losing trade.
- **Backup** (same pieces): Thermo-Alchemist pings every opponent on each instant; Comet Storm and Electrodominance cast uncopied
  with Horizon Stone's stored mana (Mystical Teachings and Solve the Equation find them); Archmage, Storm-Kiln and BMC keep cards
  and mana flowing; Ozai attacks with haste.
- Archetype: `spellslinger` + `combat_attackers` as `modifier`: the combat profile supplies the window's support lines; its fuel
  function `attackers` (12) is a beatdown plan the commander does not need (her trigger needs ONE attacker and does not need to
  connect, `win-routes.md` 4). Worked pattern "window-limited payoff + attackers" of `references/archetypes.md`.

## 3. Profile table

| Function | Tier | Min | Target | Actual | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 36 | 36 | Overlap of the two bands; X spells, Horizon Stone, equips and three colors for a 4-MV gold commander. 6 Island, 6 Mountain, 5 Swamp (one Island moved to Mountain: red has 33 pips, review M6). |
| Ramp (by turn 3) | base | 12 | 12 | 11 (WARN) | Section 9. Sol Ring, Arcane/Izzet/Dimir Signet, Mind Stone, Dimir Locket, Bender's Waterskin, Goblin Electromancer, Stormcatch Mentor, Nightscape Familiar + Black Market Connections. Glamdring no longer counted (review M9). |
| Draw (nets cards) | base | 12 | 18 | 16 tags; about 12.5 weighted alone, about 15 while Azula attacks | Full: Archmage Emeritus, Black Market Connections, Fact or Fiction, Pull from Tomorrow, Gleam of Death, Waterbending Lesson (draw 3; tap artifacts to waterbend), Zuko, Exiled Prince ({3}: a card a turn, paid by firebending in the window). 0.75: Azula On the Hunt, Malcolm (a Clue on the second spell each turn; Azula's turns meet it). Half alone, a full card when copied: Big Score, Thrill, Abandon Attachments, Frostcliff Siege (Jeskai), Dimir Locket (late). Tricks with draw as SECOND tag, half each when copied: Fists of Flame, Blazing Crescendo, Cunning Maneuver. 90 % to see a draw piece by turn 5; 71 % two by turn 7; five repeatable engines (Archmage, BMC, Zuko, Malcolm, Azula OtH) 51 % by turn 6. |
| Spot removal | base | 8 | 10 | 8 + 2 counters (second tag) | Terminate, Hero's Downfall, Go for the Throat, Chaos Warp, Abrade, Lightning Strike, Snap, Amphibian Downpour; Narset's Reversal, Negate. Copied in the window, each answers two permanents. X burn doubles as removal. |
| Wipes | base | 2 | 3 | 2 | Day of Black Sun (X=0 kills tokens) and Ritual of Soot; both spare Azula. Ritual also kills Thermo, Electro, Dualcaster, Electromancer, Stormcatch, Nightscape, Malcolm: a reset, cast only when they are absent or worth losing (review M4). |
| Commander protection | base (attack_engine) | 6 | 8 | 7 | Swiftfoot Boots, Champion's Helm, Octopus Form (hexproof); Deflecting Swat, Narset's Reversal (redirect or return); Negate (counter); Undying Malice (death return). 61 % by turn 5. Redirect Lightning went for draw (section 5). |
| spell_density | gate | 30 | 36 | 30 | Instants and flash only: 26 instants + Dualcaster, Gearhulk, Amphibian Downpour, Hidden Footblade. At the minimum: the slots went to draw that works without Azula (Zuko, Malcolm, Waterbending Lesson, Solve). 3+ by turn 5 about 75 %. |
| spell_payoffs | gate (commander payoff, late 6) | 6 | 8 | 8 + 3 tutors | Azula, Archmage, Storm-Kiln, Dualcaster, Electro, Gearhulk, Helm, Narset's Reversal; tutors Teachings, Solve, Godo. |
| through_wide_board | gate | 10 | 12 | 11 + 2 tutors | Comet Storm, Electrodominance, Thermo-Alchemist, Day of Black Sun, Ritual of Soot, Rogue's Passage, Haunted Cloak, Frostcliff Siege, Ozai, Electro, Malcolm (fliers). |
| through_big_creatures | gate | 10 | 12 | 14 + 2 tutors | Terminate, Hero's Downfall, Go for the Throat, Chaos Warp, Amphibian Downpour, Snap, Lightning Strike, Electrodominance, Comet Storm, Rogue's Passage; pump after blocks: Fists of Flame, Run Amok, Blazing Crescendo, Cunning Maneuver. Day of Black Sun removed from this line (review M3: X high enough kills Azula). |
| window_mana (declared, bridge) | declared late | 6 | 8 | 10 | One verb: more mana usable INSIDE Azula's window. Adds in combat: Fire Nation Palace, Azula OtH, Zuko (firebending), Ozai (firebending 4), Electro ({R} per cast), Storm-Kiln and Big Score (treasure), Frantic Search and Snap (untap lands, twice copied). Brings stored mana in: Horizon Stone (R2: lands tapped in the last opponent's end step). Of these, keepers that also save the leftover after combat: Horizon Stone, Electro, Ozai (3; review I3). |
| Make blocks bad (owner) | judgment | 8 | 10 | 16 | Cast after blocks, copied: Fists of Flame (trample, +1/+0 per card drawn), Run Amok (+3/+3 trample, +6/+6 copied), Blazing Crescendo and Cunning Maneuver (+6/+2 copied), Unleash Fury, Octopus Form; removal on the blocker (Terminate, Hero's Downfall, Go for the Throat, Lightning Strike, Snap, Chaos Warp, Abrade, Amphibian Downpour, each copied onto a second creature); static: Champion's Helm 6/6, Haunted Cloak trample, Hidden Footblade first strike, Rogue's Passage. |
| haste | support | 4 | 6 | 4 | Swiftfoot Boots, Haunted Cloak, Hidden Footblade, Frostcliff Siege (Temur). The promotion test says promote (attack-only, MV 4); the pool has no other haste giver for her (only steal effects), so the line stays support and protection sits near target (review M1: reason corrected). Equipment stays after she dies, so the recast is hasty for the equip cost. 41 % to see one by turn 5; the first cast needs none. |
| team_evasion | support | 6 | 8 | 7 | Rogue's Passage, Haunted Cloak, Frostcliff Siege, Ozai, Fists of Flame, Run Amok, Malcolm. |
| defense_while_tapped | support | 4 | 6 | 5 listed, about 4 weighted | Propaganda, Haunted Cloak (vigilance), Thermo-Alchemist (0/3 defender), Octopus Form (one-shot untap), Bender's Waterskin (instant mana on their turns). |
| combat_draw | support | 4 | 6 | 7 | Archmage, Azula OtH, Frostcliff (Jeskai), Zuko, Fists, Blazing Crescendo, Cunning Maneuver. |
| wipe_insurance | support | 2 | 3 | 2 | Undying Malice, Negate; equipment, Helm, BMC, Horizon Stone, Propaganda survive wipes. |
| attackers | support (modifier) | 12 | 16 | 6 (WARN) | Section 9. |
| cost_reducers | support | 2 | 4 | 4 | Goblin Electromancer, Stormcatch Mentor, Nightscape Familiar, Glamdring. |
| Graveyard hate | floor | 1 | 1 | 0 now, 1 after the purchase | Soul-Guide Lantern to buy (lead's ruling); Run Amok plays meanwhile. |
| Answers to commanders | floor | 2 | 3 | 2 | Amphibian Downpour (neutralize, no tax reset), Chaos Warp. Imprisoned in the Moon cut (section 5). |
| Tutors | info | | | 3 | Mystical Teachings (instant or flash), Solve the Equation (instant or sorcery: Comet Storm, Overpowering Attack), Godo (Helm). |

Fit check (each card once): ramp 10 + draw 12 + removal 8 + wipes 2 + protection 6 + payoffs outside those 5 + route closers
outside payoffs 5 + haste/defense pieces in no other line 3 + tutors 3 + Horizon Stone 1 = 55 of 63; 36 + 55 = 91 of 99.

Answers versus closers (review M10): answers 12 (8 spot, 2 counters, 2 wipes) against about 11 damage-dealing closers (Azula,
Comet Storm, Electrodominance, Thermo, Ozai, Unleash Fury, Godo, Helm, Overpowering Attack, Azula OtH, Zuko) plus the engines.
Round 3 cut two answers (The Last Agni Kai, Imprisoned in the Moon) and added no answer: the balance improved.

Salt (second objective; Phase 1 list 8.4, owner floor 7.5). Round 3 moves toward what Salt rewards: a third tutor back (Solve),
four net-draw cards (Zuko, Malcolm, Waterbending Lesson, Abandon), the late Godo + Helm combo, an extra-combat spell; it lost two
cheap answers and one protection spell. Expected neutral to slightly lower than 8.4 and well above 7.5; to be measured on
Moxfield/Salt with exact printings. First Salt-raising swaps if the measure disappoints, all owned and gate-safe: Fatal Push for
Abandon Attachments (density stays 30, removal 9, draw about 12) and Mana Leak for Cunning Maneuver.

## 4. The list by function (how to use each card; when it is bad to draw)

Commander: **Fire Lord Azula**. Cast turn 3 to 4; equip Boots or Cloak before attacking; attack every turn; cast instants in
the declare blockers step, after blocks are known. Keep two mana and a trick open when attacking into the opponent who blocks:
the copied trick wins the fight, and the "in between" opponent stops blocking once he sees it.

**Ramp (10)**
- Sol Ring: turn 1; with a Signet, Azula on turn 3. Weak late.
- Arcane Signet: turn 2, fixes the third color. Weak late.
- Izzet Signet: turn 2; {U}{R} for the double pips. Weak late.
- Dimir Signet: turn 2; {U}{B} for Hero's Downfall and Day of Black Sun. Weak late.
- Mind Stone: turn 2; late, crack it for a card.
- Dimir Locket: turn 3 when no 2-drop rock came; late, sacrifice for two cards. Bad on a turn Azula is castable.
- Bender's Waterskin: turn 3; untaps on each opponent's turn: instant mana for counters and Pull.
- Goblin Electromancer: turn 2; instants in the window cost 1 less. Dies to pings.
- Stormcatch Mentor: turn 2; same discount, hasty prowess body.
- Nightscape Familiar: turn 2; blue and red spells (Azula too) cost 1 less; regenerates to block.

**Draw (12 primary; Frostcliff and three tricks carry draw as a second tag)**
- Archmage Emeritus: in her window each instant draws two. Cast it with protection open; bad as the lone creature against a pinger.
- Black Market Connections: turn 3; draw plus Treasure each turn; the 3/2 only as a blocker.
- Fact or Fiction: end of the last opponent's turn, or in the window (two piles twice).
- Pull from Tomorrow: end of the last opponent's turn with all lands (Horizon Stone keeps the rest); copied in the window, 2X cards. Never recast for free (X = 0). Bad on turns 2 to 3.
- Big Score: in the window the copy draws two and makes two Treasures without a discard.
- Thrill of Possibility: in the window, discard one, draw four. Alone a loot.
- Abandon Attachments: cheap rummage; copied, one more card. Bin extra lands.
- Waterbending Lesson: main phase, tap rocks and creatures to waterbend {2}: draw three, keep all. A refill after a wipe.
- Zuko, Exiled Prince: attack with Azula: his firebending 3 and her 2 pay {3} once or twice: exile the top card and play it now; an instant played that way is copied. Out of combat a mana sink for Horizon Stone's stored mana. 4/3 body; bad into bigger untapped blockers (keep him home then and use the ability).
- Malcolm, the Eyes: turn 2 flier with haste; a Clue on your second spell each turn (your own turns and theirs); crack Clues with stored mana. Flies over Board 1.
- Glamdring // Gleam of Death: Gleam first (mill six, take every instant and sorcery), Glamdring later on Azula: her spells cost up to 4 less (6 with Champion's Helm).
- Azula, On the Hunt: second attacker with firebending 2 and a Clue each attack. Bad into bigger untapped creatures.

**Combat tricks (4; draw as second tag on three)**
- Fists of Flame: after blocks: draw (two copied) and trample with +1/+0 per card drawn this turn, twice: the blocker dies and the rest tramples over. Alone a cantrip.
- Blazing Crescendo: after blocks: +6/+2 copied and a card per copy to play until your next turn.
- Cunning Maneuver: after blocks: +6/+2 copied and a Clue per copy.
- Run Amok: on an attacking Azula after blocks: +6/+6 and trample copied. Stand-in for Soul-Guide Lantern until it is bought.

**Spell payoffs and engines (8 incl. Horizon Stone)**
- Storm-Kiln Artist: two Treasures per spell in the window. Fragile early.
- Dualcaster Mage: flash in the window: three copies of one instant. Out of combat, copy their removal at your target.
- Electro, Assaulting Battery: keeps red mana, adds {R} per instant cast; leaving, pays X to burn a player.
- Torrential Gearhulk: flash in the window: two Gearhulks recast two instants (never an X spell), each copied. Bad before turn 6.
- Helm of the Host: equip Azula: a hasty Azula token every combat (every spell copied twice). On Godo late: unlimited combats (R11). Bad early.
- Godo, Bandit Warlord: turn 6 to 7: puts Helm onto the battlefield; his attack gives an extra combat (Azula with Haunted Cloak's vigilance attacks again). Hidden Footblade gives him haste. Bad before turn 6.
- Overpowering Attack (loan): after Azula connected, {2}{R} in main phase 2: untap the attackers, extra combat and main phase: a second window. Bad when she cannot connect.
- Horizon Stone (proven role-player, bridge): keeps unspent mana as colorless (R1, R2): pays X, equips, Zuko and Clues. Bad on turn 5 with no Azula.

**Commander protection (7)**
- Swiftfoot Boots: hexproof and haste for a recast.
- Champion's Helm: hexproof on a legendary, +2/+2 (6/6 Azula wins most blocks).
- Octopus Form: hexproof in response to removal, +1/+1 in a fight, or untap her after damage as a blocker.
- Deflecting Swat: free with a commander out: send the removal to their creature.
- Narset's Reversal: against an instant or sorcery aimed at Azula: return it and keep a copy.
- Negate: counters removal spells and wipes; hold {1}{U} after a big attack.
- Undying Malice: in response to destroy or a wipe: she returns with a counter, no tax.

**Removal (8)**
- Terminate, Hero's Downfall, Go for the Throat: kill the blocker after blocks; the copy kills a second creature.
- Chaos Warp: any permanent, the commander answer; copied, two.
- Abrade: 3 damage or kill an artifact. Weak late against big bodies.
- Lightning Strike: 3 (6 copied) to a blocker or a player at low life.
- Snap: bounce a blocker or a token; untaps two lands (four copied).
- Amphibian Downpour: flash in the window: storm plus copy make several creatures (or a commander) vanilla 1/1 frogs.

**Wipes (2)**
- Day of Black Sun: X=0 for {B}{B} kills every token; X=3 spares Azula and the 4-MV engines.
- Ritual of Soot: kills everything at MV 3 or less, including your small creatures: a reset, not a routine play.

**Finishers (5)**
- Comet Storm: two kicks name all three opponents; copied, 2X each. Early, X=2 to 3 removal.
- Electrodominance: X and a free spell from hand; copied, twice.
- Ozai, the Phoenix King: haste 7/7 trample, firebending 4; keeps mana as red; flies and is indestructible with six floating. Bad before turn 6.
- Unleash Fury: on an unblocked or trampling Azula: copied, power x4: 16 (24 with Champion's Helm).
- Thermo-Alchemist: turn 2; pings every opponent per instant cast; blocks small attackers.

**Haste, defense, tutors (6)**
- Propaganda (proven role-player): turn 3; each attacker costs {2}; they hit the others while Azula is tapped.
- Haunted Cloak: equip {1}: vigilance (she still blocks, and attacks again in extra combats), trample, haste.
- Hidden Footblade: {R} flash: cast after blocks for first strike; haste on a recast.
- Mystical Teachings: end of an opponent's turn, the instant the game needs; copied, two.
- Solve the Equation: main phase: Comet Storm to kill, Overpowering Attack for a second window, or the answer you lack.
- Frantic Search: in the window it untaps three lands (six copied) and loots.

**Lands (36)**: 6 Island, 6 Mountain, 5 Swamp; Command Tower, Exotic Orchard; check and reveal lands (Drowned Catacomb,
Dragonskull Summit, Sulfur Falls, Choked Estuary, Foreboding Ruins, Frostboil Snarl); Smoldering Marsh and Sunken Hollow;
pain lands (Shivan Reef, Sulfurous Springs, Underground River); filter lands (Cascade Bluffs, Sunken Ruins, Darkwater Catacombs,
Shadowblood Ridge); Fire Nation Palace (firebending 4 on the big turn); Rogue's Passage (Azula unblockable for {4}).

## 5. Cut log

Proven role-players (Horizon Stone, Propaganda) are both IN.

Round 1 (against the Phase 1 list he plays):
| Card out | Function it served | Count after (min) | Replacement | Reason |
|---|---|---|---|---|
| Ember Island Production | none (combo with Dualcaster) | n/a | Pull from Tomorrow | L7 mini-combo; dead alone. |
| Entomb | none | n/a | Thrill of Possibility | No reanimation; orphan. |
| Goblin Bombardment | noncombat damage | burn route 3 | Thermo-Alchemist | No fodder; Thermo hits all three. |
| Lo and Li, Twin Tutors | tutor | tutors 3 | Azula, On the Hunt | 5-mana 2/2 at sorcery speed; its best target is in the list. |
| Reckless Handling | artifact tutor | tutors 3 | Horizon Stone | Random discard; Godo fetches Helm. |
| Banefire | finisher | burn route 3 | Unleash Fury | Single target, sorcery speed. |
| Mana Leak | counter | protection 7 (6) | (later rounds) | Bad late. |
| Consider, Opt, Ponder | cantrips | density 30 (30) | draw that nets cards | Cantrips, not draw. |
| Heartless Act | removal | 8 (8) | Hidden Footblade | Haste was under min. |
| Fatal Push | removal | 8 (8) | Haunted Cloak | Bad late; Cloak gives haste, vigilance, trample. |
| Ultimate Price | removal | 8 (8) | Propaganda | Misses multicolored commanders; proven role-player. |
| Aether Gale | one-sided bounce | wipes 2 (2) | Dimir Locket | 5-mana sorcery outside the window. |
| Canyon Slough | land | 36 | Smoldering Marsh | Always tapped (the assignment plays the English LTC Marsh; the owed Spanish one goes to Ezio). |

Round 2 (owner decisions and the lead's scarce-copy ruling): Brainstorm out for Godo (owner); Swan Song, Insight Engine and
Thirst for Knowledge to Kilo; Lion Vulture out (owner: slow; Coastal Piracy not chosen because it needs combat damage to a
player, the thing Azula lacks, and Ezio keeps the copy); Abandon Attachments out for Fists of Flame; Overpowering Attack in as a
loan; Blazing Crescendo and Cunning Maneuver in as tricks; Redirect Lightning back for Swan Song.

Round 3 (review B1, I1, M3, M6, M7, M9; owner: maximize power, Salt at 7.5 or more):
| Card out | Function it served | Count after (min) | Replacement | Reason |
|---|---|---|---|---|
| Expedite | haste (one-shot), cantrip | haste 4 (4) | Zuko, Exiled Prince | The weakest haste piece (one-shot, half weight); Zuko turns window mana into cards (review B1 bridge card; in his original list, cut by Phase 1 with no reason). Expedite is now free for Ezio. |
| The Last Agni Kai | removal, keeper | removal 8 (8); window_mana 10 (6) | Waterbending Lesson | Its copy makes Azula fight twice and can kill her (review); the keeper role stays with Horizon Stone, Electro, Ozai. Waterbending Lesson is a full draw-three. |
| Redirect Lightning | protection | protection 7 (6) | Malcolm, the Eyes | Protection near target with cheaper layers (Swat free, Octopus Form {U}); Malcolm adds a Clue engine and a hasty flier (Board 1). |
| Loyal Inventor | tutor (artifact to top), vigilant body | tutors 3; defense 5 (4) | Solve the Equation | Its Assassin clause is dead, so it tutors to the top (a skipped draw, review M5); Godo now fetches Helm. Solve finds Comet Storm (route access from 2 to 4 cards: 51 % by turn 9, 60 % by turn 13, review I1) or Overpowering Attack, and adds the tutor Salt rewards. Chosen over Nightscape Familiar to keep ramp at 11. |
| Imprisoned in the Moon | removal, answer to commanders | removal 8 (8); answers to commanders 2 (2) | Abandon Attachments | The only non-instant removal; cutting it keeps spell density at 30 (Abandon is an instant) while adding draw. Commanders are still answered by Amphibian Downpour and Chaos Warp. |
| Soul-Guide Lantern (to buy) | graveyard hate | 0 until bought (1) | Run Amok (stand-in) | Not owned: the physical deck plays Run Amok until the Lantern is bought and scanned (review M7). |
| 7th Island | blue source | blue 18 | 6th Mountain | Red has 33 pips against blue 22 (review M6); red sources 18. |

Original-list cards reconsidered: Zuko, Exiled Prince, Malcolm and Run Amok are back; still out: Coastal Piracy (needs combat
damage to a player), Fire Nation Attacks (5-mana tokens: a creature plan), It'll Quench Ya (soft counter), Zuko's Exile (5 mana),
Firebender Ascension (copies attack triggers: only Azula's firebending, 4 counters needed), Combustion Man, Koh, Cruel
Administrator (creature plan), Royal Assassin (sorcery-speed tapper), Labyrinth Adversary (4-drop, one blocker per attack),
Commander's Sphere (Kilo's).

## 6. Loans

- **Overpowering Attack**: accepted (2026-11-02), declared in `decks/phase2.json` `borrowed`; no stock at Game of Magic Singles,
  the replacement waits for a restock (`decks/phase2/restock.md`). The owner allows a second store only for Hidden Footblade
  and Overpowering Attack: if one has it, buying it returns the loan.
- Propaganda and Hidden Footblade are his own free copies.

## 7. Scarce copies (lead's ruling of 2026-11-02, applied)

| Card | Ruling | Effect on Azula |
|---|---|---|
| Swan Song, Insight Engine, Thirst for Knowledge | Kilo | Out since round 2. |
| Soul-Guide Lantern | Toph and Kilo keep the owned copies; one is bought for Azula | Purchase rank 1; Run Amok meanwhile. |
| Pull from Tomorrow, Hidden Footblade | Azula | In. |
| Command Tower | Toph, Azula, Ezio (Azula gets the Spanish EOC copy per the assignment) | In. |
| Expedite | Freed by round 3 | Available to Ezio. |
| Loyal Inventor, Redirect Lightning, Imprisoned in the Moon, The Last Agni Kai | Freed by round 3 | Available to other decks. |

## 8. Purchase wishes (Game of Magic Singles; Toph, Azula and Ezio share 5,000 CLP; the lead verifies live stock)

Ranked by impact on Azula's consistency and power. Each row names what plays until it arrives.

| Rank | Card | Need and power effect | Price hint | Fallback (plays meanwhile) |
|---|---|---|---|---|
| 1 | Soul-Guide Lantern | The deck's only graveyard answer (lead's ruling) | No GoM reading; usually among the cheapest | Run Amok |
| 2 | Arcane Denial | Cheap counter for ANY spell (creature removal, wipes, the sorcery-speed lock effects that shut her window): protection 7 to 8 and cheap interaction, a Salt driver | 2,840 CLP NM (GoM reading 2026-10-17, old) | Cunning Maneuver |
| 3 | Swan Song | One-mana counter for removal and sorcery wipes: protection and wipe insurance | No GoM reading | Abandon Attachments |
| 4 | Talisman of Dominance (or Indulgence, Creativity), normal printing | The 12th ramp piece at MV 2: clears the ramp WARN and raises Salt's mana score | Only reading is a 12,840 CLP borderless foil (above the share): buy only a normal printing under about 1,500 CLP | Dimir Locket stays; the Talisman replaces Abandon Attachments |

A purchase that would clearly raise power beyond these: none in the share; Lightning Greaves-type haste with shroud would block
her own Octopus Form and Champion's Helm targeting, so it is not proposed.

## 9. WARN reasons and dead clauses

- **Ramp 11 of 12**: ten pieces castable by turn 3 plus Black Market Connections; the window itself pays for the instants
  (firebending {R}{R}, Zuko, Azula OtH, Palace, treasures), and Horizon Stone doubles land mana from midgame. The twelfth slot went
  to draw, the owner's first need for this deck. Purchase 4 restores 12.
- **attackers 6 of 12** (support line of the modifier): Azula's trigger needs one attacker, herself. Beside her: Azula OtH, Ozai,
  Electro, Godo, Zuko, Malcolm, plus a Helm token of Azula every combat. Twelve creatures would replace window spells.
- Dead clauses: Glamdring's discount needs an equipped creature (Azula); Frostcliff Siege's modes are exclusive; BMC's
  Shapeshifter is only a blocker; Ozai's flying needs six floating mana; Godo's untap clause names Samurai (none: only his extra
  combat counts); Overpowering Attack's discount needs Azula's combat damage; Waterbending Lesson's discard is avoided by tapping
  artifacts or creatures.

## 10. Reference boards

- **Board 1: eight sacrificeable 1/1s.** Day of Black Sun X=0 or Ritual of Soot clears them; Comet Storm copied hits all three
  players; Thermo-Alchemist pings past them; Malcolm and Electro fly; Rogue's Passage, Haunted Cloak, Frostcliff, Fists of Flame
  or Run Amok trample put Azula's damage through a chump. Chumps do not stop the copies. Risk: pingers kill the 2-toughness
  engines.
- **Board 2: two creatures bigger than Azula.** If one blocks: a copied trick (Run Amok +6/+6 trample, Blazing Crescendo or
  Cunning Maneuver +6/+2, Fists of Flame) wins the fight, or Terminate on the blocker and its copy on the second. Amphibian
  Downpour neutralizes; Snap copied bounces both; Electrodominance and Comet Storm for X; Champion's Helm 6/6; Rogue's Passage skips
  them.
- **One sweeper turn:** equipment, Helm, Horizon Stone, BMC, Propaganda, Glamdring survive; Azula returns with Undying Malice or
  is recast with haste from the equipment on the table; Negate counters the sorcery wipe; Waterbending Lesson refills; Ozai with
  six floating mana is indestructible.

## 11. Mana

- Colored sources (lands): blue 18 (6 Island + 12 nonbasic), black 18 (5 Swamp + 13), red 18 (6 Mountain + 12); rocks: Arcane
  Signet, Bender's Waterskin (any), Izzet Signet (U R), Dimir Signet and Dimir Locket (U B). Karsten for a gold 4-drop with one
  pip of each: 17 per color: met. Pips: red 33, blue 22, black 14; red double pips are paid mostly by firebending in the window.
- Tapped lands: none always tapped. Conditional: Smoldering Marsh, Sunken Hollow, Fire Nation Palace, three check lands, three
  reveal lands; four filter lands need one mana of input.
- Curve (X at 0): MV1 4, MV2 29, MV3 15, MV4 10, MV5 2, MV6 3; average 2.78.
- Odds (99 cards, no mulligan): 2 to 4 lands in 7 cards 74 % per look, about 93 % with the free redo; 4 lands by turn 4 62 %;
  a draw piece by turn 5 90 %; a protection piece by turn 5 61 %; a haste piece by turn 5 41 %.

## 12. Open questions for the owner

Answered: Godo + Helm (in, late, R11); Overpowering Attack (loan in); Lion Vulture (out); blocks (16 punishers, section 3).
1. After a few games: does the blocking opponent still kill Azula in combat? If yes, Mechanical Glider (flying, owned) goes in for
   Abandon Attachments.
2. Salt measure of this list (exact printings): if it lands under 8, the first swaps are Fatal Push for Abandon Attachments and
   Mana Leak for Cunning Maneuver (section 3).
3. Purchases 2 to 4 (section 8): which fit in the shared 5,000 CLP after the Lantern?
