# Ezio Auditore da Firenze: final rebuild from scratch, budget-adjusted (Phase 2 step 7.7, 2026-11-08)

Builder: champion rebuild under `docs/proposals/final-rebuild-brief-20261108.md` (CORRECTED budget section), the skill
`.claude/skills/commander-deckbuilding/SKILL.md` (Champion standard), `docs/research/commander-deckbuilding/champion-addendum-20261108.md`
(R4 to R39) and the primers `commanders/ezio-auditore-da-firenze*.md`. Bilingual deck (English copy when owned in both), proxy
commander. Files: `ezio-auditore-da-firenze.txt` (the 100 cards to PLAY, buys included), `.plan.json`, this file.

**Budget frame (owner, corrected 2026-11-08):** Ezio's envelope is **34,000 CLP all-in** (upgrades + loan replacements + tokens
+ extras); every bought card under 3,000 CLP from Game of Magic Singles, PayToWin or Rivendel; loan replacements follow the loan
rules (automatic under 5,000, to evaluate at 5,000 or more). A first version of this rebuild assumed "no cap" (217,547 CLP with
Cyclonic Rift, Teferi's Protection, Mari, Lightning Greaves, Brotherhood Regalia, Diabolic Intent, Counterspell); that version is
void and every one of those cards is out. **This list (after the review's fix round): 29,707 CLP all-in (section 11), 4,293 under the envelope.**

**Fix round (review `decks/reports/final-review-ezio-auditore-da-firenze-20261108.md`, verdict FIX, applied 2026-11-08):**
F1 Eivor, Battle-Ready out, Kaya, Ghost Assassin in, until the owner accepts Eivor's 5,400 replacement (`loans.md` rule 3); Eivor
is a pending loan proposal and comes back in Kaya's slot when accepted, or on its own if a copy under 5,000 is read live.
F2 Ramses fallback corrected: Rooftop Assassin failed the gate; the exact fallback is in section 6. F3 Reckless Handling out,
Diabolic Tutor in (any card, so Ramses). F4 Rogue's Passage out, ninth Swamp in (saves 1,440). F5 Kitesail out, Cobbled Wings
(owned, equip {1}) in. F6 Etrata the Silencer is no longer a route closer: she shuffles herself away after each hit, so the
third-hit-counter kill is not a line without Mari; she is removal on an unblockable body. F7 guide: on the kill turn attack
EVERY opponent with at least one Assassin, so Ramses covers whoever falls. All fixes applied; none kept back.

**Checks (run 2026-11-08 on this list):**
- `python scripts/check_phase2_bracket.py decks/phase2/ezio-auditore-da-firenze.txt`: **PASS** (floor 3, target 3; Game Changers
  0, checked against the live Scryfall `is:gamechanger` list of 53 cards; no extra turns, no land denial, no reversible card;
  Spellbook finds one line, Ezio + Magister Sphinx, "commander plus one card, late").
- `python scripts/plan_density.py`: **PASS**, 0 failures, 2 warnings, reasons in section 3: team_evasion 3 of 6; 35 lands against
  the 36-38 band. Report `decks/reports/consistency-ezio-auditore-da-firenze.md`.
- 100 cards (1 commander + 99), counted by script; average MV of the 64 nonland cards 2.797; 29 cards at MV 2 or less.
- Tree of Perdition was rejected in drafting (Ezio + Tree is flagged "early", floor 4, by the bracket script).

---

## 1. The profile

### Commander reading (Oracle and rulings)
Ezio Auditore da Firenze, {1}{B}, 3/2 menace Human Assassin, identity WUBRG. (1) Assassin spells I cast have freerunning {B}{B}:
once an Assassin or a commander of mine deals combat damage to a player, any Assassin spell costs {B}{B} for the rest of the turn.
(2) When Ezio deals combat damage to a player at 10 life or less, I may pay {W}{U}{B}{R}{G}; that player loses.
- Fuel: attacks that connect early and every turn; window: my combat, then the second main phase (Assassins cast after the hit).
- Dependence: **attack engine** for the kill; freerunning works from ANY Assassin hit, so the cost reduction survives Ezio's death.
  Protection class 6 to 10.
- Cost 2: tax is cheap (4, then 6); haste after a recast comes from Swiftfoot Boots, Hidden Footblade, Haunted Cloak.
- Dead clauses: none. The kill removes one player per trigger: Ramses or repetition makes it a table win.

**Rules points to verify**
| Point | Status | What falls if wrong |
|---|---|---|
| Ezio's life check happens when the trigger resolves, after all combat damage | Ezio ruling 2024-07-05, verified (study S2) | Slasher + Ezio same-combat kill |
| Freerunning lasts the rest of the turn after the hit | Ezio and Restart Sequence rulings, verified | Second-main-phase pattern |
| Slasher's and Ezio's triggers fire on the same damage; I order Slasher's to resolve first | Basic trigger ordering; not ruling-checked | Slasher + Ezio at 21-25 life |
| Ramses wins when the losing player "was attacked this turn by an Assassin you controlled": true for Ezio's trigger and combat damage; for Kaya's drain or Shao Jun's pings only if an Assassin attacked that player that turn | Oracle reading; no Ramses ruling read | Route 1 as a TABLE win (each elimination still removes one player) |
| Shao Jun taps artifacts as a cost; a tapped Equipment keeps working | Rules for tapped permanents, well known | Route 3 |
| Etrata shuffles herself into the library after each hit, so a three-counter kill needs counters from elsewhere (not in this list) | Oracle; Etrata rulings 2018-10-05 | Etrata is removal, not a closer |
| Brotherhood Headquarters cannot pay Ezio's {W}{U}{B}{R}{G} | Card text; play review 2026-10-26 | Payment math |
| Jacob Frye's copy of a freerunning card can be cast for the freerunning cost | Derived, unverified by a ruling (play review) | One draw line |
| Hakoda's sacrifice gives indestructible at instant speed (no mana) | Oracle (an activated ability with no timing limit) | Wipe insurance |

### Plan (one sentence)
Assassin evasion tempo with a table-ending kill: cheap evasive Assassins and Ezio connect from turn 2 or 3, every hit makes
Assassin spells cost {B}{B} and draws cards, and Ramses turns the FIRST elimination (Ezio's {W}{U}{B}{R}{G} trigger, Etrata's
or damage focused on one player) into a win of the whole game, while Shao Jun and Kaya damage every opponent without combat.

### Backup (same pieces)
Without Ezio or Ramses the same evasive Assassins keep connecting under Arno and Bayek with Rally the Peasants, and Shao
Jun and Kaya turn the Equipment, the rocks and loyalty into damage to each opponent every turn.

### Speed (goldfish, section 10)
Ezio turn 2 in most hands; first hit and first freerunning turn 3; first elimination turn 7 (6-8). With Ramses out that
elimination is the game; without him the table falls turn 9-10.

### Win lines (chosen before the cards, R26 and R28)
| Route | Closers | Win turn | Mana | Access (10+, R18) | Each piece alone | Fails to |
|---|---|---|---|---|---|---|
| 1. Ezio eliminations, made a table win by Ramses | Ramses, Magister Sphinx, Unstoppable Slasher | Ezio + Ramses + a setter or enough damage (3 cards with the commander) | 5 for the payment | To Ramses: Ramses, Diabolic Tutor, Adéwalé (about 7 % per dig), Entomb + Restart/Layla/Jacob/Altaïr; to a setter: Sphinx, Slasher, Loyal Inventor (Sphinx) = about 8 cards, under R18's 10 (the brief's money limit; Demonic or Vampiric would fix it) | Ramses a 4/4 deathtouch lord; Slasher a deathtouch halver that returns; Sphinx a 5/5 flier | Ezio or Ramses removed (damage still kills one player), a counter (recursion) |
| 2. Assassin team beatdown | Arno Dorian, Bayek of Siwa, Rally the Peasants | 4-6 attackers + one multiplier | the turn's mana | 3 closers + 24 attackers | Arno a deathtouch lord, Bayek a double striker, Rally an instant +2/+0 twice | a wipe (Hakoda, Get Out, rebuild) |
| 3. Damage to each opponent without combat | Kaya, Ghost Assassin (Eivor when its loan is accepted), Shao Jun | Shao Jun + 2 untapped artifacts per point; Kaya -1 for 2 each | 3 / 4 | 2 closers + Diabolic Tutor + 7 Equipment + 9 rocks | Shao Jun a 3/3 that flies on my turn; Kaya blinks a creature or makes each opponent discard | a creature wipe (Kaya survives it), artifact wipe (rare) |

No failure point is shared by all three: Ezio dead leaves routes 2 and 3; a wipe is met by Hakoda, Get Out
and the rebuild pieces; a counter on Ramses leaves routes 2 and 3; only route 1's recursion uses the graveyard.

### How it beats three opponents
Ramses: any of the deck's single-player eliminations ends the game for all three. Without him, route 2 spreads 15-30 evasive
damage a turn over the table and route 3 hits every opponent at once (Shao Jun 1 per two artifacts, several times a turn; Kaya 2 per
-1; Eivor, once accepted, 7 per attack with seven Equipment). On the kill turn attack every opponent with at least one Assassin.

### What it fears
Wipes on turns 5-7 (63 % that one appears by turn 8, skill S-6); flying or reach deathtouch blockers; black and artifact chump
boards (no Cover of Darkness now); attack taxes; fast combo before turn 6. Answers: Hakoda, Get Out, Mana Leak, ward (Thopteryx)
and hexproof (Boots, Enter the Avatar State), ten spot answers, Mephitic Vapors, the noncombat route.

---

## 2. The puzzle: every card, its job and its main partners

### Commander
- **Ezio Auditore da Firenze**: turn 2; attack from turn 3 with menace, later with Hookblade or Cobbled Wings for flying; pay {W}{U}{B}{R}{G} on a player at 10 or less. Partners: Ramses, Slasher, Sphinx, Boots.

### Connectors: cheap evasive Assassins that switch freerunning on (6)
- **Hookblade Veteran**: turn 1; flies on turn 2 so a 4-5 MV Assassin costs {B}{B} on turn 2-3. Bad late (1/2).
- **Basim Ibn Ishaq** (loan): every historic spell (legend, artifact, Equipment) draws and makes Basim unblockable; cast a rock or
  Equipment before combat.
- **Brotherhood Spy**: unblockable 2/3 on my turn while I control a legendary Assassin (Ezio counts).
- **Desmond Miles**: menace 2-drop that grows with every Assassin on board and in the yard; surveil feeds Jacob and Altaïr.
- **Ratonhnhaké꞉ton**: hexproof and unblockable until its first hit; each hit makes an Assassin token and returns an Equipment.
- **Gold-Forged Thopteryx**: ward {2} on every legend I control (20, Ezio and Ramses included); flier that blocks fliers.

### Engines: card flow on hits (10)
- **Ezio, Blade of Vengeance**: a card per Assassin hit; 5/5 deathtouch wall. Freerunning target turn 3-4.
- **Etrata, Deadly Fugitive**: each Assassin hit cloaks the opponent's top card as my 2/2 ward creature; 1/4 deathtouch blocker.
- **Coastal Piracy**: a card per creature hit on an opponent; turn 4, before the big attacks.
- **Black Market Connections**: Treasure (payment colors), card or a 3/2 changeling (an Assassin) each first main phase.
- **Lion Vulture**: flier that draws and grows at every end step in which an opponent lost life (nearly every turn).
- **Jacob Frye**: on each Assassin hit, recast a copy of an Assassin or freerunning card from my yard (Eagle Vision for {1}{U},
  Restart Sequence, a dead Ramses for {B}{B}).
- **Merciless Harlequin**: body + card for {1}{B} after a hit.
- **Queen Marchesa**: haste deathtouch 3/3 and the monarch; drop it when the board can defend the crown.
- **Eagle Vision** (loan): draw three for {1}{U} after a hit (owner's proven role-player).
- **Layla Hassan** (loan): on entry and every Assassin hit, a historic card (Ramses, Sphinx, an Equipment) from yard to hand.

### Payoffs, closers and diggers (12)
- **Ramses, Assassin Lord** (buy): one elimination wins the game; lord +1/+1; deathtouch. Cast it the turn BEFORE the kill,
  behind Thopteryx's ward.
- **Arno Dorian**: +2/+0 to every other Assassin, deathtouch; disguise as a 2/2 ward body for 3 into open removal.
- **Bayek of Siwa** (loan): legendary attackers have double strike on my turn.
- **Rally the Peasants**: instant +2/+0 to the team, flashback for a second swing; also a combat trick against blocks.
- **Aya of Alexandria** (loan): menace lifelink; each historic creature hit makes an Assassin token.
- **Unstoppable Slasher** (loan): halves a player's life on a hit and returns once when it dies; with Ezio on the same player at
  25 or less: halve, then Ezio's check.
- **Etrata, the Silencer** (removal, not a closer): unblockable; each hit exiles that player's best creature, then she shuffles into my library; the third counter makes
  them lose. Attack a player with no creatures to keep her.
- **Magister Sphinx**: sets one opponent to 10; Roshan makes it {B}{B} after a hit.
- **Kaya, Ghost Assassin** (holds Eivor's slot until its loan is accepted): -1 drains 2 from each opponent (route 3); 0 blinks
  Ezio or Ramses out of a removal spell's way until my upkeep (sorcery speed, so before passing); -2 a card for me, one less for each
  opponent. Eivor, Battle-Ready (loan, pending): haste, vigilance, Equipment count to each opponent per attack.
- **Shao Jun**: flier on my turn; tap two artifacts (Equipment keep working) for 1 to each opponent, repeatedly.
- **Altaïr Ibn-La'Ahad** (buy): each attack brings back attacking copies of Assassins from my yard.
- **Adéwalé, Breaker of Chains**: reveal six, take an Assassin (23 in the list): a 2-for-1 for {B}{B} after a hit that digs for
  Ramses. Its Vehicle clause is dead (no Vehicles), named here.
- **Roshan, Hidden Magister**: every creature is an Assassin: Sphinx, Thopteryx, Lion Vulture, Inventor and Hakoda cost {B}{B}
  after a hit and take the lord buffs.

### Equipment and attack enablers (8)
- **Swiftfoot Boots**: hexproof + haste on Ezio or Ramses.
- **Hidden Footblade** (loan): flash, haste for a fresh attacker, first strike in a combat.
- **Haunted Cloak**: vigilance, trample, haste: a lord or Ramses attacks and still blocks.
- **Hookblade**, **Cobbled Wings** (equip {1}), **Mechanical Glider**: flying for Ezio or a connector (Glider costs 1 and attaches itself).
- **Assassin Gauntlet**: taps one opponent's whole board before combat (the elimination target); loots on hits.
- **Propaganda**: attack tax that protects the tapped board (a proven role-player in his Azula list).

### Interaction (11)
- **Swords to Plowshares**: 1-mana instant exile.
- **Infernal Grasp**, **Bitter Triumph**, **Terminate**: 2-mana instant kills.
- **Assassin's Trophy**: any permanent; **Chaos Warp**: any permanent, instant; **Kolaghan's Command**: artifact + regrowth or 2
  damage; **Feed the Swarm**: creature or enchantment (sorcery).
- **Mana Leak**, **Get Out**: early counter / the win-turn counter; Get Out also returns Ezio and Ramses to hand in response to a
  wipe or removal.
- **Mephitic Vapors**: -1/-1 to all: kills a board of 1/1 chump blockers while my Assassins survive.

### Protection (3, plus Boots, Thopteryx, Get Out)
- **Hakoda, Selfless Commander**: a 3/5 vigilance blocker; sacrifice it (no mana, instant speed) for team indestructible against
  a wipe or a combat.
- **Haystack**: {2}: phase out Ezio or Ramses in response to removal or a wipe, every turn.
- **Enter the Avatar State**: 1-mana hexproof plus flying on the kill turn.

### Tutors and recursion (4)
- **Loyal Inventor**: an artifact to hand: Sphinx, Boots, an Equipment. Vigilance blocker.
- **Diabolic Tutor** (buy): any card to hand for 4 (Ramses first; Sphinx or an answer when Ramses is out). Was: Reckless Handling: an artifact to hand; random discard; 2 to each opponent if it bins an
  artifact. Bad late.
- **Entomb**: instant; Ramses or Sphinx to the yard for Restart, Layla, Jacob or Altaïr.
- **Restart Sequence**: {1}{B} after a hit: Ramses, Sphinx or Ezio Blade back.

### Mana (9 rocks + 35 lands)
- **Sol Ring**, **Arcane Signet**, **Fellwar Stone** (buy), **Talisman of Progress** (buy), **Golgari Signet**, **Rakdos
  Signet**, **Orzhov Signet** (buy): turn 1-2 mana and fixing; **Chromatic Lantern** (every land taps for any color: the payment),
  **Bender's Waterskin** (any color, untaps each opponent's turn).
- Lands: Command Tower, Exotic Orchard, Path of Ancestry, Brotherhood Headquarters, Secret Tunnel, Abstergo
  Entertainment (filter and graveyard hate), Concealed Courtyard, Isolated Chapel, Drowned Catacomb, Sunken Hollow, Dragonskull
  Summit, Smoldering Marsh, Woodland Cemetery, Battlefield Forge, Sulfur Falls, Hinterland Harbor, Prairie Stream, Clifftop
  Retreat; 9 Swamp, 3 Island, 3 Plains, 1 Mountain, 1 Forest.

---

## 3. Curve, functions and ratios

| MV | Count | Cards |
|---|---|---|
| 1 | 7 | Sol Ring, Hookblade Veteran, Hidden Footblade, Mechanical Glider, Swords, Enter the Avatar State, Entomb |
| 2 | 21 | 5 rocks, Basim, Desmond, Spy, Thopteryx, Boots, Haystack, Hookblade, Cobbled Wings, Feed the Swarm, Grasp, Bitter Triumph, Trophy, Terminate, Mana Leak, Get Out |
| 3 | 19 | Lantern, Waterskin, BMC, Shao Jun, Ratonhnhaké꞉ton, Etrata DF, Slasher, Altaïr, Inventor, Harlequin, Jacob, Adéwalé, Haunted Cloak, Gauntlet, Rally, Propaganda, K-Command, Chaos Warp, Vapors |
| 4 | 13 | Diabolic Tutor, Kaya, Ramses, Arno, Queen, Etrata S, Aya, Layla, Roshan, Lion Vulture, Hakoda, Coastal Piracy, Restart Sequence (Assassins {B}{B} after a hit) |
| 5 | 3 | Ezio Blade, Bayek, Eagle Vision ({B}{B} / {1}{U} after a hit) |
| 7 | 1 | Magister Sphinx |

27 creatures (22 Assassins; Roshan makes the other 5 Assassins); 19 artifacts, 7 Equipment, 20 legends. Toughness 2 or less:
7 of 27 creatures with Ezio (26 %, under a third).

### Function profile (combat_attackers + alternate_kill as plan)
| Function | Tier | Min | Target | Actual | Needed by | Reason |
|---|---|---|---|---|---|---|
| attackers | gate | 12 | 16 | 24 (23 without Ezio) | early | 22 Assassins plus fliers; the fuel |
| through_wide_board | gate | 10 | 12 | 19 | early | 9 evasive or flying creatures, 3 flying Equipment, Gauntlet, Vapors, Tunnel, Enter the Avatar State, Kaya's drain, Diabolic Tutor |
| through_big_creatures | gate | 10 | 12 | 15 | early | 7 spot answers + deathtouch (Ramses, Arno, Queen, Slasher, Ezio Blade) + Etrata's exile + Diabolic Tutor |
| condition_enablers | gate | 10 | 12 | 20 | early | Damage sources and multipliers toward 10; Sphinx sets one |
| team_finishers | gate | 6 | 8 | 7 | late | Ramses (game), Kaya, Shao Jun, Arno, Bayek, Rally, Diabolic Tutor |
| haste | support | 4 | 6 | 4 | early | Boots, Footblade, Haunted Cloak, Queen. Not promoted: freerunning works from any Assassin hit, so a turn without Ezio is not a dead turn |
| team_evasion | support | 6 | 8 | **3** (WARN) | early | Gauntlet, Secret Tunnel, Vapors. Reason below |
| defense_while_tapped | support | 4 | 6 | 7 | early | Propaganda, Haunted Cloak (vigilance), Inventor, Thopteryx, Etrata DF, Ramses, Hakoda |
| combat_draw | support | 4 | 6 | 7 | early | Ezio Blade, Coastal Piracy, Etrata DF, Jacob, Eagle Vision, Gauntlet, Lion Vulture |
| wipe_insurance | support | 2 | 3 | 8 | late | Hakoda, Haystack, Get Out, Restart, Layla, Jacob, Altaïr, Slasher |
| payment_enablers | support | 6 | 8 | 9 | early | Tower, Orchard, Path of Ancestry, Arcane Signet, Fellwar, Lantern, Waterskin, BMC Treasure, Abstergo |

**WARN team_evasion 3 of 6 (reason):** the only owned team-evasion card was Cover of Darkness, a loan whose replacement costs
10,600 (31 % of the envelope); the stores have no other team-evasion card under 3,000. Board 1 is still carried by 20
through_wide_board pieces: nine creatures that fly or are unblockable, three flying Equipment, Gauntlet (one opponent's whole board
tapped), Mephitic Vapors (kills every 1/1), Secret Tunnel, and the noncombat route (Shao Jun, Kaya) that
never meets a blocker. Cover of Darkness is the first card to add when money frees up (section 6).

**WARN 35 lands (reason):** the lean-low rule holds: average MV 2.797 (< 2.8) with 29 cards at MV 2 or less and 9 rocks;
freerunning makes every 4-5 MV Assassin cost {B}{B} after turn 3. Bracket 4 average lists of this commander run 33 lands (primer
E1). P(2-4 lands in 7) 73 %, 93 % with the free mulligan.

### Ratios
| Item | Count | Why for THIS deck |
|---|---|---|
| Lands + lasting ramp (R8) | 35 + 9 = 44 (+ BMC Treasure) | Two under 46, accepted for freerunning; lands 80 % of sources |
| Ramp | 10 (9 rocks + BMC) | Profile min 10 met; 7 at MV 2 or less |
| Draw | 11 counted | Hit-based draw counts full: the deck connects with unblockables every turn |
| Spot answers | 10 (+ Etrata S) | R19: 8 at MV 2 or less, 9 instants; artifacts: Trophy, Chaos Warp, K-Command; enchantments: Trophy, Chaos Warp, Feed the Swarm, Get Out |
| Wipes | 1 (Mephitic Vapors, one-sided) | A creature deck does not run symmetric wipes |
| Commander protection | 7 | Boots, Thopteryx (ward), Haystack, Hakoda, Get Out, Mana Leak, Enter the Avatar State (attack engine 6-10) |
| Tutors | Diabolic Tutor (buy), Loyal Inventor, Entomb, Adéwalé (dig) | Diabolic Intent and the GC tutors exceed the 3,000 limit |
| Tapped lands (R10) | 1 always (Path of Ancestry); 3 need two basics (Sunken Hollow, Smoldering Marsh, Prairie Stream) | The check lands read 8 Swamps and the typed duals |
| Colored sources (lands + rocks) | B 27, W 19, U 18, R 16, G 13 | Pips B 27, U 21, W 15, R 12, G 1 |

---

## 4. Interaction plan and protection plan

- **What the table holds by turn 8** (skill S-6): about 2.3 spot removal, 0.9 wipes, 0.45 counters across three opponents.
  Protect Ezio and Ramses against spot removal first (Thopteryx ward, Boots, Haystack, Enter the Avatar State), then hold one wipe
  answer from turn 6 (Hakoda on the board, Get Out or Mana Leak in hand).
- **Spot answers**: (1) whatever wins next turn, (2) a flying or deathtouch blocker in the way of the kill, (3) an attack tax
  (Trophy, Chaos Warp, Feed the Swarm). Never a small value creature: the swarm goes around it.
- **Win-turn shield (R24, 3+ at MV 2 or free)**: Mana Leak, Get Out, Enter the Avatar State, Haystack (activation 2), Boots already
  on Ezio. Sequence: Ramses the turn before; on the kill turn equip a flier, keep {U}{U} or {W} up, attack, pay the five colors
  with Lantern or the any-color lands. Bait a counter with Coastal Piracy or a lord first.
- **Archenemy (R30)**: never show a lethal board one turn before the shield is ready; Propaganda and deathtouch make the
  crack-back expensive.
- **Wipes (R32)**: commit what wins in two turns, keep one Assassin in hand when two opponents can wipe. Rebuild: Ezio (2),
  Restart, Layla, Jacob, Altaïr, Slasher, Ratonhnhaké꞉ton (Equipment back), Eagle Vision; Hakoda before it, Get Out during it.
- **Graveyard hate**: Abstergo Entertainment. **Opposing commanders**: Swords, Chaos Warp, Etrata exile or shuffle them away.

---

## 5. Mulligan and play pattern

**Keep:** 2-4 lands with a black source; a 1-2 MV rock or two plays at MV 3 or less; a plan piece (connector, engine, lord,
Equipment) or a rock. Ezio is always the turn-2 play.
**Ship:** 0-1 land; 5+ lands with no play; no black source by turn 2; interaction-only hands.
**Keep almost any land-good hand with:** Hookblade Veteran, Basim, Brotherhood Spy, Sol Ring, Swiftfoot Boots, Ramses, Coastal
Piracy, Black Market Connections, Adéwalé.

**Turns 1-5:** T1 land + Sol Ring, Hookblade Veteran or Mechanical Glider. T2 Ezio. T3 attack with Ezio and the connector; after
the hit cast the best 4-5 MV Assassin for {B}{B} (Ramses first at a slow table; Arno, Etrata S or Ezio Blade otherwise). T4-5
engines (Coastal Piracy, BMC, Lion Vulture), Thopteryx before Ramses; keep 2 mana up from turn 5.
**Turns 6-9:** choose the elimination target (nearest to 10, or the combo player): Slasher + Ezio on that player, Sphinx, Etrata,
Gauntlet to tap their board, Rally for the extra damage. Ramses on board turns it into the win.
**Kill turn:** attack every opponent with at least one Assassin (Ramses only covers players an Assassin attacked).
**Late:** Shao Jun and Kaya finish every opponent; Restart, Layla, Jacob rebuild; Eagle Vision and Coastal refill.

---

## 6. BUY (ranked by gain per CLP, all under 3,000)

Price hints: highest variant price on the store's product search, 2026-11-08 (Shopify `price_max`, about Near Mint; product JSON
answered HTTP 429, so the variant is **to read** live); Rivendel by script with quantity. Gain is judgment [J], estimated points
of win rate in a 4-player pod, only to rank.

### New buys
| # | Card | Store (printing, stock 2026-11-08) | Price hint | Lang | Gain [J] | Gain per 10k | Plays until it arrives |
|---|---|---|---|---|---|---|---|
| 1 | Ramses, Assassin Lord | PayToWin, Dominaria United Commander (in stock; variants 1,600-3,500) | **2,990 cap: buy only a variant UNDER 3,000** (the NM regular showed 3,500) | EN | +6: one elimination ends the game; lord; deathtouch | 20 | Rooftop Assassin (owned) |
| 2 | Talisman of Progress | Game of Magic, FINAL FANTASY Commander (in stock) | 1,500 | EN | +0.7: untapped W/U turn 2 | 4.7 | Dimir Locket (owned) |
| 3 | Fellwar Stone | PayToWin, Lorwyn Eclipsed Commander (in stock) | 1,560 | EN | +0.7: 2-mana any-color rock | 4.5 | Boros Locket (owned) |
| 4 | Orzhov Signet | Game of Magic, Tarkir Dragonstorm Commander (in stock) | 1,240 | EN | +0.5 | 4.0 | Everflowing Chalice (owned) |
| 5 | Altaïr Ibn-La'Ahad | Game of Magic, Assassin's Creed (in stock) | 2,080 | EN | +0.7: attacking copies of dead Assassins | 3.4 | Lydia Frye (owned) |
| 6 | Diabolic Tutor | PayToWin, four printings available (product range 1,200-7,400, per the review); **to read: buy only a variant UNDER 3,000** (2,990 cap) | 2,990 | EN or ES | +0.8: a second card that finds Ramses (doubles access to the table win) | 2.7 | Reckless Handling (owned) |

Ramses is NOT a loan candidate (it is not in his Standard binder, `decks/phase2/loans.md`), so it can only be a normal buy and
must cost under 3,000. **Exact fallback (review F2):** if no Ramses under 3,000 is in stock at the live read, the slot plays
**Fire Nation's Conquest** (owned; team +1/+0, a team finisher) while Kaya holds Eivor's slot, or **Kaya, Ghost Assassin** once
Eivor is in; NOT Rooftop Assassin, which fails the gate (team_finishers 5 of 6). Route 1 then stays a
one-player-per-elimination route; the gate passes either way (Ramses is one of four closers).

### Kept from the current purchase order for Ezio
| Card | Store | Price | Note |
|---|---|---|---|
| Golgari Signet | Game of Magic | 570 | rock, black + green for the payment |
| Battlefield Forge | Game of Magic | 915 | untapped R/W |
| Dropped (review F4): Rogue's Passage | PayToWin | -1,440 | a colorless land whose 4-mana activation competes with the 5-color payment; ninth Swamp instead |
| Assassin token 1/1 black menace (TACR 4) | Game of Magic | 570 | Ratonhnhaké꞉ton and Aya |
| Dropped: Llanowar Wastes | Game of Magic | -1,320 | replaced by an 8th Swamp; green comes from 13 sources already |

Booked to Kilo in the order, unchanged: Swords to Plowshares EN (2,500; Ezio plays it, the Spanish copy goes to Kilo) and Command
Tower (900; Ezio's Spanish copy goes to Kilo, the bought copy to Ezio: buying the English LP at the same 900 is better).
Tokens: Queen Marchesa's 1/1 deathtouch haste Assassin had no stock (use a marker); BMC's Shapeshifter and Treasures are owned
(they move with BMC); Copy tokens owned.

### Not bought (gain per CLP or the 3,000 rule), with what would come first if money frees up
Cover of Darkness loan (10,600; team fear, the proven role-player: first in line), Achilles Davenport loan (8,680), Mari (7,200),
Lightning Greaves (7,200), Brotherhood Regalia (12,200), Whispersilk Cloak (3,640), Counterspell (4,400 NM), Path to Exile (2,600
at PayToWin: Feed the Swarm and the owned removal do the job), Diabolic Intent (21,120), every Game Changer (section 12).

---

## 7. Loans and their replacements (rules `decks/phase2/loans.md`)

| Card | Status | Replacement | Class | Gain [J] per 10k | Decision |
|---|---|---|---|---|---|
| Eagle Vision | lent 2026-10-31 | Game of Magic 742 | automatic | high (draw 3 for 2) | keep |
| Bayek of Siwa | accepted 2026-11-02 | Game of Magic 2,320 | automatic | +1.5 → 6.5 | keep |
| Layla Hassan | accepted 2026-11-02 | Game of Magic 915 | automatic | +0.8 → 8.7 | keep |
| Hidden Footblade | accepted 2026-11-02 | PayToWin 1,440 | evaluate (accepted) | +0.6 → 4.2 (haste now that Greaves is out) | keep |
| Unstoppable Slasher | accepted 2026-11-02 | Game of Magic 5,560 | evaluate (accepted) | +1.5 → 2.7 (halving + Ezio kill, deathtouch, returns) | keep |
| **Basim Ibn Ishaq** | NEW | Game of Magic 3,400 (in stock) | **automatic** | +2 → 5.9 | keep |
| **Aya of Alexandria** | NEW | Game of Magic 915 (in stock) | **automatic** | +0.8 → 8.7 | keep |
| **Eivor, Battle-Ready** | NEW, **pending proposal, not in the list** | PayToWin 5,400 NM (variants 3,100-5,400; Game of Magic sold out) | **to evaluate** at 5,400 (automatic if an LP under 5,000 is read; then it enters in Kaya's slot). Need: the only closer that hits all three opponents at once without combat (7 Equipment = 7 to each per attack, haste, vigilance). Fallback until accepted: Kaya, Ghost Assassin (owned; -1 drains each opponent 2) | +1.5 → 2.8 | keep |
| Achilles Davenport | accepted 2026-11-02 | Game of Magic 8,680 | evaluate | +1.2 → 1.4 | **drop**: Arno (owned) is the stronger lord; Rally the Peasants (owned) covers the team pump; Adéwalé (owned) takes the slot and digs for Ramses |
| Cover of Darkness | accepted 2026-11-02 | PayToWin 10,600 | evaluate | +1.5 → 1.4 | **drop** (proven role-player: the reason is for the owner to review): 31 % of the envelope for one card; fear fails against black and artifact blockers; 20 other ways through a wide board remain. To keep it, the owner would drop Eivor + Altaïr + Orzhov Signet (8,720) and go 1,880 over the envelope, or also drop Slasher |

Ratonhnhaké꞉ton and Propaganda use free English copies (no loan). New `borrowed` / restock entries for the lead: Basim, Aya,
Eivor only once accepted; Achilles and Cover of Darkness go back to his Standard decks (remove their restock rows).

---

## 8. Scarce copies

| Card | Copies | Claim | Reason and what the other deck loses |
|---|---|---|---|
| Black Market Connections | 1 EN, held by Azula's current list | **Ezio claims it** (priority 1; Azula not yet rebuilt) | Here it is ramp (Treasure for the payment), draw and an Assassin body every turn. Azula loses it; no copy under 3,000 in the stores |
| Hakoda, Selfless Commander | 1 EN, in Toph's current list (pool: free) | **Ezio claims it** | Free wipe insurance on a 3/5 body; Toph not yet rebuilt; Toph's builder may want it back for its own wipe insurance (lead resolves) |
| Chaos Warp | 4 (2 EN free, 1 EN Azula, 1 ES Kilo) | Ezio takes a free English copy | No conflict |
| Command Tower | 3 (1 EN Azula, 2 ES Ezio and Toph) | Ezio keeps one copy | Kilo needs Spanish: Ezio's Spanish copy goes to Kilo, Ezio takes the bought copy (prefer the English LP, 900) |
| Swords to Plowshares | 2 ES | Ezio plays the bought English copy | The Spanish copy goes to Kilo |
| Haystack | 2 EN (Toph 1, free 1) | Ezio takes the free copy | No conflict |
| Deflecting Swat | 1 EN, Azula | not claimed | Azula's free-spell plan needs it more |
| Spanish-only cards played here | Brotherhood Spy, Hookblade Veteran, Hookblade, Merciless Harlequin, Restart Sequence, Assassin Gauntlet, Ezio Blade, Isolated Chapel, Woodland Cemetery, Hinterland Harbor, Clifftop Retreat (Ezio's copy), Exotic Orchard, Brotherhood Headquarters | no Kilo conflict | Clifftop and Orchard have spare Spanish copies for Kilo |

---

## 9. Comparison with the current list (after purchases) and iteration 1

Current list `decks/phase2/moxfield/ezio-auditore-da-firenze-after-purchases.txt` (Salt 6.6, real power 6.6-7.1): 19 out, 18 in,
plus one Swamp.
| Out | Function | In | Why |
|---|---|---|---|
| Cover of Darkness (loan 10,600) | team evasion | Rally the Peasants (owned) | Budget (section 7); Rally closes route 2 |
| Achilles Davenport (loan 8,680) | lord | Adéwalé (owned) | Budget; Arno stays as lord; Adéwalé digs for Ramses |
| Haytham Kenway | removal body | Basim (loan) | Unblockable draw engine at 2 |
| Thorn of the Black Rose | monarch | Aya (loan) | The monarch is stolen in a pod; Aya makes Assassins from hits |
| The Revelations of Ezio | slow saga | Ramses (buy) | The table kill |
| Lydia Frye, Evie Frye | connectors | Hookblade Veteran, Altaïr (buy) | Turn-2 freerunning; recursion in combat |
| Mortify, Utter End | 3-4 MV answers | Bitter Triumph, Feed the Swarm | Cheaper; Chaos Warp covers any permanent |
| What Must Be Done | symmetric wipe / recursion | Hakoda | A board deck should not wipe its own board; Hakoda saves it |
| Angelic Intervention | single protection | Chaos Warp | Protection count still 7; another instant answer to any permanent |
| Ghostly Prison | attack tax | Black Market Connections | One tax is enough with deathtouch and vigilance |
| Boros Guildmage | haste | Cobbled Wings | Haste 4 without it; flying for equip {1} |
| Glider Staff | evasion | Mechanical Glider | 1 mana instead of 3 |
| Boros Locket | 3-mana rock | Fellwar Stone, Talisman of Progress, Orzhov Signet (buys) | 2-mana rocks (R9) |
| Abandoned Campground, Raucous Carnival, Llanowar Wastes | lands | Clifftop Retreat, Swamp | R10 tapped lands; budget |

Iteration 1 (`decks/measured/ezio-auditore-da-firenze/round5-step40.txt`, Salt 7.7, lost two games): 45 names kept. Gone: the
Etrata copiers, Dualcaster + Ember Island, Intruder Alarm, Deadeye, Nekrataal, Venser, Winter Soldier, Ravenloft Adventurer, the
colorless and tapped lands. The owner's losses named the fixes: haste (5 now), ways past chump boards (20), fragile creatures
(ward, deathtouch, Hakoda), open while tapped (Propaganda, vigilance, deathtouch), finishing more than one player (Ramses, Kaya,
Shao Jun).

---

## 10. Test pass (R33, R38, R39) and the reference boards

**20 opening hands** (seeded shuffle, seed 20261108, section 5 checklist applied strictly by script): 11 of 20 keep the first
seven, **19 of 20 with the free mulligan (95 %)**. Ships: six one-landers, one five-lander, two hands with lands and only
answers (a human would keep one of them: Ezio on turn 2). Theory: 2-4 lands 73 %, 93 % with the free redo.

**Goldfish (seed 7, the kept hands, one opponent targeted; run before the fix round, so games 2 and 4 show Eivor where Kaya now plays: Kaya on T4-5 adds 2 to each opponent per turn instead of Eivor's attack, about the same elimination turn):**
1. Swamp, Swamp, Orchard, Golgari Signet, Etrata S, Haunted Cloak, Feed the Swarm: Ezio T2, first hit T3 and Etrata for {B}{B},
   Layla T4, Thopteryx + Cloak T5; target at 9 on T7, Ezio's trigger removes them (T7).
2. Island, Swamp, Dragonskull, Eivor, Haunted Cloak, Swords, Eagle Vision: Ezio T2, hit T3 + Lantern, Sol Ring + Eivor T4 (haste),
   Eagle Vision for {1}{U} T5; elimination T7.
3. Feed the Swarm, Etrata DF, Drowned Catacomb, Swamp, Hookblade, Aya, Coastal Piracy: Ezio T2, hit T3 and Aya for {B}{B} (no
   white yet for Hookblade), Coastal T5; elimination T7.
4. Eivor, Hinterland Harbor, Golgari Signet, Harlequin, Woodland Cemetery, Smoldering Marsh, Layla: three lands that enter
   tapped; Ezio + Hookblade Veteran T3, first hit T4; elimination T8.
5. Rally, Harlequin, Altaïr, Drowned Catacomb, Brotherhood Headquarters, Plains, Trophy: Ezio T2 (Headquarters pays him), hit T3 and
   Altaïr for {B}{B}, Coastal T5; elimination T7.
Record: Ezio on turn 2 in 4 of 5, first hit turn 3 in 4 of 5, first elimination turn 7-8 (median 7). With Ramses that is the game.

**Disrupted:** (a) Ezio removed the first time he attacks: recast turn 4 with Boots (haste) while Spy/Basim keep freerunning on;
one turn lost. (b) Wipe on turn 6: Hakoda's sacrifice or Get Out keeps the core; otherwise Ezio (4), Restart and Layla threaten
again turn 8. (c) Ramses countered: Restart Sequence or Jacob recast it; routes 2 and 3 keep the pressure; one turn lost.

**Gauntlet (R39):** (1) fast combo: Mana Leak, Get Out, seven instant creature answers, Chaos Warp, Trophy, and the turn-7 clock
(eliminate the combo player first); a protected all-spell combo is the worst case. (2) Stax and taxes: 29 cards at MV 2 or less;
Trophy, Chaos Warp, K-Command, Feed the Swarm answer artifacts and enchantments; under Propaganda attack with the unblockables only
and let Shao Jun ping. (3) Go-wide: Mephitic Vapors, nine evasive creatures, flying Equipment, Gauntlet, Shao Jun and Kaya.
(4) Big creatures: seven spot answers, deathtouch (Ramses, Arno, Queen, Slasher, Ezio Blade), unblockables, Etrata's exile.
(5) Control: Thopteryx ward, Boots, Haystack, Mana Leak and Get Out against the answers, Hakoda against the wipe, cheap threats and
recursion after it; hold one threat in hand.

**Reference boards (gate):** Board 1, eight 1/1 chump blockers: Basim, Spy, Ratonhnhaké꞉ton, Etrata S (unblockable), Hookblade
Veteran, Shao Jun, Thopteryx, Lion Vulture, Sphinx (fliers), Hookblade, Cobbled Wings, Glider, Enter the Avatar State, Gauntlet,
Vapors, Secret Tunnel, Shao Jun and Kaya without combat. Board 2, two bigger creatures: Swords, Grasp, Bitter
Triumph, Terminate, Trophy, Chaos Warp, Feed the Swarm, deathtouch attackers, unblockables, Etrata's exile.

**Final cut pass (10 weakest, before the review):** Reckless Handling (later replaced by Diabolic Tutor), Mana Leak, Kitesail (later Cobbled Wings), Hookblade, Haystack, Merciless Harlequin, Mephitic Vapors,
Hookblade Veteran, Rakdos Signet, Lion Vulture: each kept against the best affordable alternatives (Smoke Bomb 742, Thraximundar
2,600, Unclaimed Territory 742, Anguished Unmaking 2,600, Path to Exile 2,600, Fatal Push, Murder, Royal Assassin, Lydia Frye,
Ghostly Prison, all owned or under 3,000) because the envelope has 443 left and none wins its slot by enough to buy.

---

## 11. Total spend of the deck against the 34,000 envelope (CLP, price hints)

| Block | Lines | CLP |
|---|---|---|
| New buys (each under 3,000) | Ramses 2,990 (cap), Diabolic Tutor 2,990 (cap, to read), Altaïr 2,080, Fellwar Stone 1,560, Talisman of Progress 1,500, Orzhov Signet 1,240 | 12,360 |
| Kept upgrade lines from the order | Golgari Signet 570, Battlefield Forge 915 (Rogue's Passage 1,440 and Llanowar Wastes 1,320 dropped) | 1,485 |
| Loan replacements kept | Eagle Vision 742, Bayek 2,320, Layla 915, Hidden Footblade 1,440, Unstoppable Slasher 5,560 | 10,977 |
| New loan replacements | Basim 3,400, Aya 915 (Eivor 5,400 pending, not counted) | 4,315 |
| Tokens | Assassin token 570 | 570 |
| **All-in total** | | **29,707** |
| Envelope | | 34,000 (4,293 left; with Eivor accepted at 5,400: 35,107, 1,107 over, so accept it only at an LP under 4,293 or with the lead's rebalance) |
| Before the rebuild | | 35,072 |

Upgrades (non-loan) come to 13,845: above Ezio's share of the 10,000 shared with Azula and Toph; every card is under 3,000 and the
deck stays inside its all-in envelope, which the lead set to hold the 90,000 target. If Ramses or Diabolic Tutor is
cheaper than its cap, the total drops. Not counted here (booked to Kilo): Swords EN 2,500, Command Tower 900.

---

## 12. Real-power estimate (1-10: 4 precon, 6 upgraded, 7-8 high power, 9-10 cEDH)

| List | Estimate | Confidence |
|---|---|---|
| Current list after purchases | 6.6-7.1 | medium-low |
| **This list with Ramses and Diabolic Tutor (after the fix round)** | **7.0-7.5** | medium-low (no games, not yet on Commander Salt) |
| This list if no Ramses under 3,000 is found (Fire Nation's Conquest in the slot) | 6.8-7.2 | medium-low |

Why up: Ramses makes one elimination a win; Basim, BMC, Lion Vulture and Coastal Piracy give cheap repeatable draw; ramp 10;
8 answers at MV 2 or less; a real noncombat route; Hakoda and Haystack against wipes and removal. Why not higher: no Game Changers,
no fast mana beyond Sol Ring, owned tutors only, team evasion thin without Cover of Darkness, five-color payment, the kill needs a
combat hit. Commander Salt guess (secondary): 6.8-7.3.

---

## 13. Game Changer slots (R34) and R36

**0 used.** The three slots may only take owned or affordable cards. Owned: Drannith Magistrate and Crop Rotation; affordable
under 3,000: Narset, Parter of Veils (the store's copy is already in Azula's order) and Braids, Cabal Minion (about 1 USD, store price not read). Drannith was tried and cut: an
off-plan stax piece with no function in this list that draws the table's hate; Crop Rotation and Braids do nothing here; Narset
digs only noncreature cards in a creature deck. Every Game Changer that fits the plan (Cyclonic Rift, Teferi's Protection, Fierce
Guardianship, Demonic, Vampiric, Enlightened Tutor) costs 26,000 to 130,000. Leaving the slots empty is the budget champion's
choice: no affordable Game Changer beats the card it would replace.

Non-GC high-power cards (R36): taken: Swords, Fellwar Stone, Talismans/Signets. Not taken: Path, Counterspell, Deadly Rollick,
Flawless Maneuver, Mox Amber, Lotus Petal, Dark Ritual, Esper Sentinel, Mystic Remora, Grand Abolisher, Deflecting Swat (Azula's),
Swan Song (Kilo's only copy): over 3,000, held by another deck, or no better than the owned card in the slot.

---

## 14. Self-review (skill S-15)
1. One-sentence plan; every engine, payoff and backup card is in a function, support line or route (gate: 0 outside).
2. Gate functions above min; early functions 15-24 pieces.
3. Fuel: 6 connectors at MV 1-2 plus flying Equipment; freerunning from turn 3; card flow +1 to +3 a turn from turn 4.
4. 35 lands with the lean-low reason; sources fit the pips; plays on turns 1-3 in most hands.
5. Attack engine, protection 7, layered (ward, hexproof, phasing, indestructible, counters, bounce).
6. Both boards: section 10.
7. Three disjoint routes, one noncombat, each beating three opponents.
8. Haste 5, team evasion 3 (WARN with reason), defense 8, toughness 2 or less 26 %.
9. Bracket 3: 0 Game Changers, no land denial, no extra turns, no early two-card infinite (script PASS).
10. Cuts logged with function and replacement (section 9); proven role-players: Eagle Vision and Propaganda kept, Cover of
    Darkness cut for budget with the reason for the owner (section 7); rules points listed with status.
