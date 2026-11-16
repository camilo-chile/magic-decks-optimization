# Collection review: Ezio Auditore da Firenze (Phase 2 step 11.2, iteration 3, 2026-11-15)

Reviewer: independent adversarial champion review, under `docs/proposals/collection-optimization-brief-20261114.md`
("What the reviewer writes"). List under review: `decks/phase2/ezio-auditore-da-firenze.txt` with its `.plan.json` and
`.build.md` (builder Fable 5.2 high, 2026-11-15). Start point: `git show HEAD:decks/phase2/ezio-auditore-da-firenze.txt`.
Frozen collection only: no purchases, loans or exchanges. Pool: `data/model/phase2/pool-ezio-auditore-da-firenze.json`
(`held_by` reflects the decks as built at HEAD, so every card this build cut shows as held by Ezio and returns to a binder).

**Verdict: FIX.** No blocking item. Two card changes (ranked 1 and 2) and one optional one (3), plus corrections to the
notes and plan file that change no card. The plan is right and the build is the best collection-only Ezio list so far.

---

## 1. Independent reading (written before opening the plan file and the build notes)

**Commander (Oracle, project cache, checked against the build's quote).** Ezio Auditore da Firenze, {1}{B}, 3/2 menace, Human
Assassin, identity WUBRG. (1) Assassin spells I cast have freerunning {B}{B}: once an Assassin or my commander has dealt
combat damage to a player this turn, an Assassin costs {B}{B}. (2) When Ezio deals combat damage to a player, I may pay
{W}{U}{B}{R}{G} if that player has 10 or less life; that player then loses. The "if" sits inside the effect, not right
after the trigger condition, so it is checked on resolution, after all combat damage and earlier triggers.
- **Archetype:** combat_attackers, with alternate_kill as the secondary plan. **Fuel:** Assassins that connect every turn
  from turn 3. **Dependence:** attack engine for the kill. The cost cut is a static ability that needs Ezio on the
  battlefield but works after ANY Assassin connects, so Ezio does more than attack. Protection class 6 to 10.
- **How it wins:** one player per Ezio trigger, at five colors at once. Ramses ("whenever a player loses the game, if
  they were attacked this turn by an Assassin you controlled, you win") makes the first elimination a table win.
  Unstoppable Slasher halves a player's life; with Ezio in the same combat, a player at 26 or less dies (Slasher's trigger
  resolves first, then Ezio's check). Bayek, Arno, Ramses and Rally the Peasants scale the damage of the whole team.
- **Rules points:** Brotherhood Headquarters' colored mana can NOT pay the {W}{U}{B}{R}{G} (that is neither a spell nor an
  activated ability). Altaïr's tokens enter attacking and do not "attack", but a token copy of Ramses made by Altaïr is a
  Ramses on the battlefield during combat damage, so it still turns a kill into a win. Haste matters after a recast at 4
  and 6 mana.
- **Haste in the list:** Swiftfoot Boots, Hidden Footblade, Haunted Cloak (3 repeatable), plus Queen Marchesa and Eivor
  for themselves. There is no team haste.
- **Evasion for Ezio himself** (Board 1): Mechanical Glider, Enter the Avatar State, Evie Frye, Waterbender Ascension,
  Haunted Cloak (trample over one chump), Assassin Gauntlet (taps one opponent's board once). Menace alone fails.
- **Recount by Oracle:** 24 Assassins, 27 creatures with Ezio, 20 legendary Assassins in the 99, 22 historic creatures,
  40 historic cards, 17 artifacts. 8 spot answers (Swords, Infernal Grasp, Assassin's Trophy, Terminate, Mortify, Utter End,
  Mana Leak, Get Out) plus Royal Assassin, the Saga, Etrata and Combustion Man. 1 wipe (Mephitic Vapors). Commander
  protection 8 (Boots, Thopteryx, Haystack, Avatar State, Imp's Mischief, Get Out, Mana Leak, Hakoda). Draw that nets cards:
  Ezio Blade, Coastal Piracy, BMC, Basim, Ascension, Queen's monarch, Eagle Vision, Evie (once), Adéwalé (once) = 9
  (Etrata DF's cloak is board, not cards in hand). Tutors: Diabolic Tutor, and Entomb (needs a recursion card).
- **Mana:** 36 lands, 10 rocks plus BMC; average MV 2.79; curve 7 / 22 / 19 / 11 / 4 / 1 (MV 1 to 6, Ezio included).
  Colored sources by land and rock: B 30, U 18, W 18, R 14, G 13. Always tapped: Path, Woodland Chasm; the three battle
  lands are tapped on turns 1 and 2 and usually on turn 3.
- **How it loses.** (1) *Wipe:* 24 small Assassins die together; answers are Hakoda (destroy, damage, -X/-X up to 5),
  Haystack and Get Out (one or two creatures), then a 4-mana Ezio and five recursion cards. (2) *Wide 1/1 chump board:* the
  small evasive bodies hit for 1 to 3 each; Ezio himself needs one of six enablers; Mephitic Vapors and Gauntlet clear or tap
  the board. (3) *Two bigger creatures:* five deathtouch bodies, Royal Assassin and eight answers handle them; Ezio (3/2)
  cannot attack into them alone. (4) *The table:* three opponents at 40 is 120 life. Without Ramses (37 % to have Ramses,
  Diabolic Tutor or Entomb in the first 14 cards) the deck must kill three times.

---

## 2. Differences with the builder

| # | Point | Builder | Reviewer recount | Effect |
|---|---|---|---|---|
| D1 | team_evasion support line | 3 (Gauntlet, Vapors, Waterbender Ascension) | **2**: the Ascension's waterbend makes ONE target unblockable (single target, repeatable) | WARN stays; the notes say single-target evasion is not counted, then count one |
| D2 | haste | 4 | **3 repeatable for Ezio** (Boots, Footblade, Cloak); Queen Marchesa gives haste only to herself | At the support line only by counting Queen |
| D3 | Tapped lands (R10) | "2 of 3 allowed" | **5 by R10's own definition**: R10 counts a conditional land as tapped unless its condition holds on turns 1 to 3 in most games. The battle lands (Sunken Hollow, Smoldering Marsh, Prairie Stream) need two basics: never on turns 1 and 2, about a quarter of the time on turn 3 | The pool has no free untapped dual left, so no card fix; the note is wrong |
| D4 | Draw by tag | 10 | **9**: Etrata, Deadly Fugitive's cloak makes a face-down 2/2 from an opponent's library, not a card in hand | The builder already says about 9 weighted; fix the tag |
| D5 | "Bleeding Effect gives flying only if a flier is in the graveyard (4 fliers in 99)" | 4 | **1** (Gold-Forged Thopteryx). Hookblade Veteran's and Shao Jun's flying are static "during your turn" abilities that work only on the battlefield | It strengthens the builder's case against Bleeding Effect |
| D6 | Get Out "held for the wipe" | counter | It counters only CREATURE or ENCHANTMENT spells: never a sorcery wipe. Against a wipe it bounces two of my creatures | Guide wording |
| D7 | WUBRG on turn 7 | 58.8 % (69.8 % with draw engines) | **66 %** in my own model (no extra draws; BMC Treasures kept; greedy rock casts), 73 % on turn 8, 82 % on turn 10; see 4.3 | Same reading: about one game in three has no kill on turn 7 |
| D8 | Ravenloft Adventurer | not mentioned anywhere (not even in "considered and left out") | The strongest free card the build missed (finding I1) | Change 1 |
| D9 | Ghostly Prison | out: "defense is at 6" | The primer lists it as an owned must-have; the real always-on deterrents are 3 | Change 2 |

Agreements (checked): 100 cards; 36 lands; average MV 2.794; 28 cards at MV 2 or less; 40 historic, 17 artifacts, 20
legendary Assassins, 22 historic creatures, 8 creatures with toughness 2 or less (30 %); Ezio on turn 2 in 95 % (my model
95.4 %); {B}{B} on turn 3 in about 78 to 80 % (mine 78.2 %); the opening-hand keep rate (mine: 69 % keep the first seven,
the same as the builder's 70.2 %); the Slasher + Ezio 26-life line; Secret Tunnel's mana cost (builder 2.6 points of {B}{B}
on turn 3, mine 3.0).

---

## 3. Findings

### BLOCKING
None. Rules, gate, card count and copies all hold (section 6).

### IMPORTANT

**I1. The best free Assassin for this plan is in the binder: Ravenloft Adventurer.**
- *Failure.* Adéwalé's slot buys a 4/1 (it dies to every ping and to Mephitic Vapors, which the deck casts itself) and one
  dig, with a dead Vehicle clause. Etrata, the Silencer carries a dead third-hit-counter clause, which the builder names.
- *Evidence (Oracle).* Ravenloft Adventurer, {3}{B}, 3/4 Human Rogue Assassin: "When this creature enters, you take the
  initiative. If a creature an opponent controls would die, instead exile it and put a hit counter on it." It is an
  Assassin, so it costs {B}{B} after a hit. Free: 1 Spanish copy.
  - *Initiative* (rulings 2022-06-10) is the table-scaling engine R16 asks for. First room: a basic land card to hand. That
    nets a card, as Adéwalé does, and it finds the Forest or Mountain the payment lacks (the list holds one of each). Then
    two +1/+1 counters or scry 2, then Trap! (a player loses 5 life, toward Ezio's 10) or a Treasure (the fifth color), then
    a card or a 4/1. The deck retakes the initiative with any Assassin hit on the holder. Propaganda (and Ghostly Prison,
    change 2) tax the players who come to steal it.
  - *Hit counters:* every nontoken creature of an opponent that dies to Royal Assassin, the Saga, the five deathtouch
    bodies, Mortify, Infernal Grasp or Terminate is exiled with a hit counter. Etrata's text counts any exiled card that
    player owns with a hit counter. Ruling 2018-10-05: tokens do not count, and her ability does nothing if the player has
    no creature. So the dead clause becomes a live elimination, and with Ramses a table win.
  - *Against Board 1 (L8):* sacrificed chump blockers are exiled instead of dying, so death triggers stop.
  - *Toughness:* 4, against Adéwalé's 1.
- *Cost.* Adéwalé's dig (about 81 % to take an Assassin; 6.5 % Ramses). Legendary Assassins go from 20 to 19, which is
  plenty for Spy, Bayek, Basim, Arbaaz and Thopteryx.
- *Fix.* Change 1 (section 8). Scratch gate PASS, bracket PASS.
- *Sourcing.* The initiative and hit-counter rules are Oracle and rulings; R16 is from the addendum; the value judgment
  is [J]. EDHREC lists it for no Ezio deck (a prior only; skill step 13).

**I2. Defense while tapped is thinner than the count says. Ghostly Prison, a primer must-have, sits free.**
- *Failure.* The owner's lesson L3: Ezio was "wide open after attacking". The support line reads 6, but two of the six are
  weak (Haunted Cloak gives vigilance to one creature; Thopteryx is a 1/3). The always-on deterrents are Propaganda, Royal
  Assassin and Etrata, Deadly Fugitive: 3 cards, so 32 % to hold one by turn 5 (12 cards seen).
- *Evidence.* Ghostly Prison, {2}{W}: the Propaganda tax, and the two stack (4 per attacker). The Ezio primer
  (`commanders/ezio-auditore-da-firenze-primers-20261108.md`, must-haves owned) and notes/12 C2 (attack taxes) back it. The
  slot comes from Combustion Man ({3}{R}{R}): the opponent chooses between losing a permanent and taking 4, so he picks the
  cheaper loss; the natural cost needs RR from 14 red sources; and he has no evasion.
- *Counts after the swap:* through_big_creatures 15 to 14, through_wide_board 16 to 15, condition_enablers 17 to 16, route 2
  closers 5 to 4, deterrents 3 to 4 (41 % by turn 5).
- *Fix.* Change 2. Scratch gate PASS.
- *Sourcing.* L3 and the primer are sourced; that Combustion Man is the weakest slot is [J].

### MINOR

**M1. The team_evasion WARN is true, but the count and part of its wording are wrong (D1, D5).**
- *Pool verified.* The only team-wide evasion in the whole pool:
  - Bleeding Effect (2 free English): flying only while a creature card with printed flying is in my graveyard. That is
    Thopteryx alone in this list, so it is a two-card setup with Entomb.
  - Cyberdrive Awakener: Kilo's, artifact creatures only.
- *Nearest pieces:* Secret Tunnel (two Assassins, repeatable, 1 free English), Rogue's Passage (one creature, 1 free) and
  Labyrinth Adversary (one blocker).
- *The builder's statement holds;* the real count is 2 of 6.
- *Fix.* Remove the Ascension from `support.team_evasion` (keep it in `through_wide_board`), write "2 of 6", and point to
  change 3. [Oracle]

**M2. Haste is 3 repeatable pieces, not 4 (D2).** Not a gate issue (support line). The promotion test does not apply:
freerunning works after any Assassin connects. With Boots or Cloak already on the battlefield, a recast Ezio gets haste for
the equip cost. P(any of the 3 by turn 7) = 37 %. The pool's only other repeatable haste is Boros Guildmage (not an
Assassin). Fix: write 3 plus Queen herself. [Oracle; skill S-3.1]

**M3. The R10 tapped-land count is 5, not 2 (D3).**
- No card fix: every free dual left is tapped (temples, Thriving lands, tri-lands).
- My model gives Jungle Shrine for a Swamp +2.3 points of WUBRG on turn 7 at -2.8 of {B}{B} on turn 3: a wash.
- Fix: correct the note. [R10]

**M4. Etrata DF is tagged draw (D4).** Re-tag it engine only. Draw becomes 9 by tag (Ravenloft's first room keeps the
count where Adéwalé had it). The base floor of 10 is reached only with Ravenloft tagged draw at full weight: say so.
[skill S-5]

**M5. Get Out's wording (D6).** In the guide: "against a wipe, bounce Ezio and Ramses in response; it counters only
creature or enchantment spells". Its R20 counter credit is real only against creature or enchantment combo pieces. [Oracle]

**M6. The Salt fallback names a slot that change 1 removes.**
- Build notes, section 7, item (4): "Magister Sphinx for Adéwalé" if Commander Salt falls under 6.5.
- After change 1, write "Magister Sphinx for Eivor" (both are top-end bodies).
- See decision (c).

**M7. Secret Tunnel was cut for 2.6 to 3.0 points of {B}{B} on turn 3; the trade is close.**
- It is the only repeatable pool card that makes TWO Assassins unblockable: Slasher and Ezio past any board, for the
  26-life kill.
- Change 3, optional: the owner chooses between turn-3 tempo and Board 1 reliability.

---

## 4. Knowledge audit

### 4.1 Sources and whether the list meets them
| # | Source | What it demands of this deck | Met? |
|---|---|---|---|
| 1 | **Skill + `archetypes.json`** (combat_attackers + alternate_kill) | One plan; profile by fuel; draw that nets cards (10); modal cards in one function per state; haste, team evasion, protection, defense while tapped; both boards; two disjoint routes, one not combat | **Mostly.** Gate PASS; routes disjoint (Ramses+Slasher / Arno, Bayek, Rally, Eivor, Combustion Man / Arbaaz, Shao Jun). Draw nets 9, not 10 (M4). Team evasion 2 of 6 (M1, pool-limited). Haste 3 + Queen (M2). Modal cards: Get Out counted in one function per state (removal or protection), fine; Mephitic Vapors once as a wipe |
| 2 | **Champion addendum (41 items)** | See 4.2 | 37 met, 3 not met with a written reason (R10 miscounted, R18 and R34 pool-limited), 1 partly (R16) |
| 3 | **Mana study** (`notes/02`, `notes/13`, skill mana-and-ramp) | Karsten 99-card rows; gold cards +1; partial weights; tapped lands 4 to 6 with a payoff; five-color decks 38 to 40 lands (notes/02 S1, Playgroup); colorless utility lands are a mistake in 4 to 5 colors (notes/06 S2); joint colors from probability E2 | **Met at the edge.** B 30 raw / 27.5 weighted against 28 for {B}{B} on turn 3. U 18 against 19 (Mana Leak) and 26 (Coastal Piracy {2}{U}{U}): short but a mid-game color. W 18, R 14, G 13: splash rows (late 12 to 16). 36 lands sits under notes/02's 38 to 40 for five colors, defended by the lean-low rule (average MV 2.79 < 2.8, 13 cheap rocks and draw): at the edge. Colorless lands: Abstergo (filter and the only graveyard hate) and Headquarters (pays {B}{B}), both justified. Joint five colors: 4.3 |
| 4 | **Notes 01 to 12** | 01 templates bend; 03 cantrips are not draw, tutors toward the finisher; 04 two-for-ones, layered protection, 2+ commander answers; 05/12 single-target kills are backups, menace fails against tokens, attack taxes; 06 haste, wipe recovery; 08/09 fit over popularity; 11 engines without enablers rot | Met: Diabolic Tutor targets Ramses; protection in six layers; commander answers exile (Swords, Utter End, Etrata); evasion counted without menace; recursion 6. The notes/12 C2 attack-tax line is under-used (I2) |
| 5 | **Ezio studies and primers** | Ramses line 1; setters; B4 lists: 33 lands, about 10 protection, Royal Assassin 55 %, Lantern 61 %, Rogue's Passage; owned must-haves include **Ghostly Prison**, Viewpoint Synchronization, Loyal Inventor, Rogue's Passage, Magister Sphinx; traps: kill alone, menace, conditional removal, slow Saga, colorless lands | Ramses central; Royal Assassin, Lantern, Saga (owner's call) in; 8 protection. **Ghostly Prison missed** (I2). Viewpoint Synchronization and Inventor out with reasons (green 13 sources; the Inventor's target was the Sphinx), acceptable. Rogue's Passage and Secret Tunnel out: see change 3 |
| 6 | **Owner's lessons, play review, gate review (f)** | See section 5 | L3 thin (I2, M1, M2); the rest met |
| 7 | **Final review 2026-11-08 and `decks/measured/`** | Ramses access thin; Feed the Swarm and Hookblade weakest; Etrata is not a closer; iteration 1 lost to mini-combos, no haste, chump boards, an open board, colorless lands | Feed the Swarm and Hookblade gone, Diabolic Tutor in, Etrata tagged removal. Ramses access 37 % by turn 7, said plainly. The iteration-1 combos stay out. The "open board" failure is only partly closed (I2) |
| 8 | **Owner's card review** | A verdict with a reason of weight per card | Every verdict is well reasoned; table 4.4 |
| 9 | **Dead clauses** | Count what each clause needs | 4.5 |
| 10 | **Strategy rule** (haste, team evasion, protection, defense while tapped) | All four filled | Protection 8 met; haste 3 (M2); team evasion 2, pool-limited (M1); defense 6 nominal, 3 always-on (I2) |
| 11 | **Multiple copies** | No idle staple that improves the deck | 4.6 |

### 4.2 Champion addendum, item by item
Met (written in the build notes and checked here): 1 one plan; 2 cards alone; 3 redundancy (22 attackers, 9 draw); 4
multi-role (about 28 of 63); 5 commander-centric (0 cards blank without Ezio); 6, 7 land count and sources; 8 total sources
46, lands 78 %; 9 fast mana (Sol Ring, Arcane Signet, Fellwar, Talisman, Signets; no Mox Amber owned); 11 window costs
(payment simulated); 12 curve 2.79; 13 tax arithmetic; 14 B4 lands (36 justified); 15 card-flow budget; 17 development first
(Basim, Evie, Ascension at 2); 19 answers (8 spot, 6 at MV 2 or less, 8 instants, 3 artifact and 4 enchantment answers;
Utter End over 3 mana with a reason); 20 counters (2 plus a redirect); 21 one-sided wipe only; 22 graveyard hate (Abstergo);
23 layered protection; 24 win-turn shield (Avatar State, Imp's Mischief, Get Out, Mana Leak, Haystack's activation); 25
answer types; 26 to 28 routes and failure points; 29 what the table holds; 31 politics; 32 rebuild 8; 33 mulligan (91 %
with the free redo); 35 efficiency; 36 R36 cards (the owned ones sit in Azula and Toph); 37 combos; 38, 39 tests and gauntlet;
40 cut log; 41 real games over a score.

Not met or partly: **10 tapped lands** (5 by R10's definition, M3; pool-limited). **16 table-scaling draw** (partly:
Coastal Piracy, Ezio Blade, the monarch; Ravenloft's initiative adds the strongest one, I1). **18 tutors** (4 access cards to
Ramses, not 10; no non-Game-Changer creature tutor is owned; stated by the builder). **30 archenemy** (at least 2 always-on
deterrents: met with 3, raised to 4 by change 2). **34 Game Changers** (0 of 3; see decision (b)).

### 4.3 The five-color payment (judged)
My own Monte Carlo (scratch, 20,000 games, two seeds agree within 0.5 points):
- Its rules: real enter-tapped conditions, the free mulligan, multiplayer draw on turn 1, greedy land and rock play, Exotic
  Orchard and Fellwar giving each color with 80 %, Headquarters never paying, and Signets and Abstergo as filters.
- It counts no extra cards from the draw engines.

| Turn | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|
| {W}{U}{B}{R}{G} payable (this list) | 45 % | 58 % | 66 % | 73 % | 78 % | 82 % |

Swaps tested, effect on turn 7:
- Woodland Chasm to Jungle Shrine: 0. A Swamp to Jungle Shrine: +2.3, but {B}{B} on turn 3 -2.8.
- A Swamp to Evolving Wilds: +1.5.
- A 37th land (Jungle Shrine for a spell): +2.3.
- Commander's Sphere to Talisman of Conviction: -1.5. Cutting any Signet: -2.4.
- Secret Tunnel for a Swamp: 0 (but {B}{B} on turn 3 -3.0).

**Judgment.**
- The builder's 59 to 70 % is right; my 66 % sits inside it.
- It is the ceiling of this collection: no fetch, shock or tri-color land is free, and no free land or rock moves it by
  more than about 2.5 points.
- The ten rocks are correct for a 2-mana commander only because of this payment, and each any-color rock is worth about
  2 points.
- Two consequences, both already in the guide:
  - The kill is a bonus from turn 8 in a third of games; the real route is damage plus Ramses.
  - On the kill turn the precombat spending competes with the payment: Glider equip 2, the Ascension's waterbend 4 (which
    taps rocks), Rogue's Passage or Tunnel 4. A Board 1 kill needs about 9 sources.
- Ravenloft's first room (a basic Forest or Mountain to hand) and its Treasure room add a little here.

### 4.4 The owner's card review (each verdict judged)
| Card | Builder | Judgment |
|---|---|---|
| Merciless Harlequin | OUT | Right: a 2/1 that nets one card; Evie does that and more |
| Royal Assassin | IN | Right: a repeatable answer and a deterrent (L3); bait for removal meant for Ezio |
| Mortify | IN | Right: instant, two colors against the pod's protection-from-monocolored commander, hits enchantments |
| Utter End | IN | Right, with the R19 exception written (exile anything, two colors) |
| The Revelations of Ezio | IN | Right on the owner's games: the pod leaves tapped attackers on my turn; III rebuilds; Layla returns the Saga |
| Commander's Sphere | IN | Right: about 2 points of payment (4.3) and a card when spare |
| Evie Frye + Jacob Frye | IN, both | Right: each fetches the other; the loot feeds Jacob, Altaïr and Desmond; Evie's unblockable is a repeatable enabler for Ezio's kill |
| Lydia Frye | OUT | Reason of weight: her evasion beats Board 2 but fails Board 1 (the owner's loss); slot pressure. She is the first creature in if a slot opens |
| Deadeye Navigator | OUT | Right: 6 mana, never discounted, a blink package of 7 partners at {1}{U} each (L7) |
| Return the Favor | OUT | Right: Azula's single copy; {R}{R} on 14 red sources |
| Tome of Legends | OUT, not contested | Acceptable: one card a turn in both decks (both commanders attack); it was Azula's side of the BMC exchange |
| Mana Leak | IN | Right |

### 4.5 Dead clauses (counted)
| Card | Clause | What it needs | Count in list | Verdict |
|---|---|---|---|---|
| Adéwalé | Vehicle return | Vehicles | 0 | Dead; leaves with change 1 |
| Hakoda | Ally spells from the top | Allies | 0 (Hakoda alone) | Dead; the card stays for its free team indestructible |
| Etrata, the Silencer | 3 hit counters | Other hit-counter sources | 0 today; **live with Ravenloft** (every opposing creature death) | Fixed by change 1 |
| Ratonhnhaké꞉ton | Return Equipment from graveyard | Equipment cards in my graveyard | 5 Equipment, rarely there | Weak; the card's evasion carries it |
| Eivor, Wolf-Kissed | Saga onto battlefield | Sagas | 1 | Nearly dead; the land clause (36 lands) is live, the mill feeds recursion |
| Waterbender Ascension | Quest counters; waterbend {4} | Creature hits; artifacts or creatures to tap | Main action; 17 artifacts | Live |
| Combustion Man | Opponent chooses | Nothing | - | Live but the opponent's choice; leaves with change 2 |
| Imp's Mischief | Redirect a single-target spell | An opposing targeted spell | - | Live; costs life equal to its mana value |
| Arbaaz Mir | Nontoken historic entering | Legends, artifacts, Sagas | 39 nonland historic permanents (37 after the changes) and each Ezio recast | Live |
| Shao Jun | Tap two artifacts | Artifacts | 17 | Live |
| Basim / Bayek / Spy / Thopteryx | Historic or legendary | Legends | 38 historic spells / 22 historic creatures / 20 legendary Assassins / 22 legends (minus 1 to 2 after the changes) | Live |

No equipment-matters, Vehicle-matters or blink payoff is played. No package of 1 to 3 cards was found outside the plan.

### 4.6 Multiple copies (whole collection) and the free pool
- **Free copies of strong staples that Ezio does not play:** Fatal Push (3 English), Murder (4), Hero's Downfall (1),
  Brainstorm, Ponder, Opt, Consider (1 each), Mystical Teachings (1), Evolving Wilds (4), Rogue's Passage (1), Secret
  Tunnel (1 free plus the copy this build returns).
- **None beats the current answers.** Fatal Push is conditional (a primer trap). Murder and Hero's Downfall are 3-mana,
  one-color copies of Mortify's job. Cantrips are fuel, not draw.
- **The free cards that would improve the list are the two in changes 1 and 2**, and Secret Tunnel (change 3).
- **Weighed and left out:**
  - Thorn of the Black Rose (a second monarch; Ghostly Prison defends better).
  - Bleeding Effect (M1).
  - Loyal Inventor (it would find Chromatic Lantern, but costs a slot that a body uses better).
  - Boros Guildmage (repeatable haste, but not an Assassin, R/W).
  - Assassin Initiate (a 1/1).
  - Darkblade Agent (needs a surveil each turn).
  - Shay Cormac (strips protection, a 1/1).
  - Jungle Shrine (4.3).

---

## 5. Lessons checklist (L1 to L10)
| Lesson | Status | Cards |
|---|---|---|
| L1 one plan | Covered | Gate PASS, one plan + backup on the same pieces, 0 orphans |
| L2 ratios by strategy | Covered | 10 rocks for the payment; attack lines sized |
| L3 connect, live, hurry, defend | **Partly** | Connect: 22 attackers, 6 Ezio evasion enablers; live: 8 protection; hurry: haste 3 + Queen (M2); defend: 3 always-on deterrents (Propaganda, Royal Assassin, Etrata DF), raised to 4 by Ghostly Prison (I2); team evasion 2, pool-limited (M1) |
| L4 dependence | Covered | Attack engine, protection 8 in six layers |
| L5 card by curve | Covered | Rocks judged by the payment, not by rating |
| L6 proven role-players | Covered | Eagle Vision, Propaganda, Coastal Piracy in |
| L7 dead clauses, mini-combos | Covered | Named (4.5); Etrata's clause made live by change 1; no two-card package |
| L8 two boards | Covered | Board 1: Veteran, Basim, Spy, Shao Jun, Ratonhnhaké꞉ton, Etrata, Glider, Avatar State, Evie, Ascension, Gauntlet, Vapors, Eivor, Cloak, Arbaaz, Shao Jun's pings. Board 2: 8 answers, Royal Assassin, the Saga, five deathtouch bodies |
| L9 Salt is not the measure | Covered | Salt named only as a risk |
| L10 guide says how to use | Covered | Section 2 of the build notes (fix the Get Out line, M5) |

---

## 6. Rules checklist
| Check | Result |
|---|---|
| `python scripts/check_phase2_bracket.py decks/phase2/ezio-auditore-da-firenze.txt` | **PASS** (floor 1, target 3, Game Changers 0, review items 0); run 2026-11-15 on the REAL list, so `decks/reports/bracket-ezio-auditore-da-firenze.md` is the real report (the scratch variants wrote to the scratchpad only) |
| `python scripts/plan_density.py` | **PASS**, 0 failures, 1 warning (team_evasion 3 of 6); the other decks unchanged (Azula PASS 5 warnings, Kilo PASS, Toph PASS) |
| Card count | 100 (1 + 99), counted by script; 36 lands, 63 nonland |
| Game Changers (live Scryfall `is:gamechanger`, 53 cards, read 2026-11-15) | 0 in the list. Owned: Drannith Magistrate and Crop Rotation (Toph), Narset (Azula) |
| Mass land denial, extra turns, early two-card infinite | None; Spellbook 0 lines inside the list (Ezio + Magister Sphinx left) |
| Reversible cards | None |
| Copies | Every card has a copy in Ezio or a binder, except Arbaaz Mir (the one claim, from Toph, decision (a)) |
| Language | Bilingual: English where both are free. Spanish only where no English copy is free (Evie, Arbaaz, Eivor, Utter End, the Saga, and the carried-over Spanish cards); correct against `free_by_language` |
| Loans, purchases, exchanges | None (frozen collection) |
| Scarce copies named | Yes, build notes section 7 (shared with Azula and Toph; no new conflict). Changes 1 to 3 use free copies only |

Scratch checks of the reviewer's list (scratchpad copies, reports written there):
| Variant | Gate | Bracket |
|---|---|---|
| Changes 1 + 2 | PASS (1 warning, team_evasion) | PASS, 0 Game Changers |
| Changes 1 + 2 + 3 | PASS (1 warning) | PASS, 0 Game Changers |

---

## 7. Decisions (a) to (c)

**(a) Arbaaz Mir claimed from Toph (Spanish, single copy): agree, it adds more in Ezio. [J]**
- **In Ezio:**
  - One of only two noncombat closers.
  - An Assassin: lords, freerunning, Spy, Bayek, Ramses' condition.
  - 39 nonland historic permanents plus every Ezio recast: about 1 to 2 damage to EACH opponent a turn from turn 3, which
    pushes all three toward Ezio's 10.
- **In Toph** (its own notes):
  - One of seven drain closers (Sabotender, Tannuk, Valakut Exploration, Ragost, Goblin Bombardment, Legion Guildmage).
  - Its loop-B kill also works with the landfall pingers.
  - Its written fallback is Fire Nation Archers (owned).
- **Verdict:** Toph loses a redundant pinger; Ezio loses a whole route if it goes back.

**(b) Drannith Magistrate: do not claim it now. The empty Game Changer slots are correct for this collection. [J, R34]**
- **R34 ranks the slots by marginal wins for THIS plan:** a tutor or route card, a win-turn shield, a scaling engine, fast
  mana, a reset. Drannith is none of them.
- **It competes with the deck's best turns.** On turn 2 it competes with Ezio; on turn 3 it costs the {B}{B} Assassin after
  the first hit; cast later, the opposing commanders are already out.
- **Its weaknesses here:**
  - It is a 1/3 that is not an Assassin: no freerunning, no lord, no Spy or Bayek credit.
  - It turns the table against the deck that is already the visible attacker (R30). The builder wrote this, and it holds.
- **The other owned Game Changers do nothing here:**
  - Crop Rotation is green land tutoring.
  - Narset's -2 finds noncreature cards in a creature deck, and she is Azula's.
- **No free Game Changer exists in the pool.**
- **Revisit:** if Toph's own optimization drops Drannith (its plan file tags it "orphan" today), Ezio may take it for Imp's
  Mischief, with the gate re-run. It is not worth contesting.

**(c) Ezio + Magister Sphinx dropped: real power cost near zero; a Commander Salt risk. [J]**
- **Real power.** Sphinx costs {4}{W}{U}{B} and is not an Assassin, so freerunning never discounts it. With Roshan gone it
  is castable only at 7 natural mana, about turn 8 or later in this 36-land base, and the kill then needs {W}{U}{B}{R}{G}
  more (12 mana in one turn, or a turn of warning). Unstoppable Slasher does the setter job at {B}{B} (a player at 26 or
  less dies to Slasher + Ezio). Eivor is a better top end in real games.
- **Salt.** Ezio + Sphinx was the list's only Spellbook line, and the last measured Ezio list was 6.6 (2026-11-07, another
  list) against a 6.5 floor. So Salt may read this list lower.
- **Recommendation:** consistency first. Do not re-add it now. If the next Salt measure is under 6.5, the first swap to
  try is Magister Sphinx for Eivor (M6), gate re-run.

---

## 8. Change list (FIX), ranked

| Rank | OUT (to binder) | IN (language, source copy) | Reason | Expected impact |
|---|---|---|---|---|
| 1 | Adéwalé, Breaker of Chains | **Ravenloft Adventurer** (Spanish, the only copy, free in the Spanish binder) | I1: initiative (table-scaling R16: a land card at once, then counters, 5 life loss or a Treasure, a card); every opposing creature death becomes a hit counter, so Etrata's elimination is live (a table win with Ramses); sacrificed chump blockers are exiled; a 3/4 for {B}{B} | +0.1 real power [J]; draw by tag unchanged; legendary Assassins 20 to 19 |
| 2 | Combustion Man | **Ghostly Prison** (English, free in the English binder) | I2: L3 (open board after attacking), primer must-have, notes/12 C2; doubles Propaganda's tax and protects the initiative; Combustion Man's choice belongs to the opponent and his natural cost needs RR from 14 sources | +0.1 real power in 4-player pods [J]; always-on deterrents 3 to 4 (41 % by turn 5); route 2 closers 5 to 4 |
| 3 (optional, owner's choice) | 1 Swamp (the tenth) | **Secret Tunnel** (English, free; the copy this build returned) | M7: the only repeatable pool card that makes two Assassins unblockable (Slasher + Ezio: the 26-life kill past any board, the owner's Board 1 loss) | {B}{B} on turn 3 78 to 75 %; payment unchanged; Board 1 reliability up from turn 6 |

**Plan file for the changes (scratch-verified PASS).**
- Change 1: Ravenloft replaces Adéwalé in `attackers`; tags `["engine","draw"]`, bad when drawn `never`.
- Change 2: remove Combustion Man from every function, the support lines and route 2; Ghostly Prison goes into
  `support.defense_while_tapped`, tag `engine` (as Propaganda), `never`.
- Change 3: Secret Tunnel goes into `through_wide_board`, tag `land`.

**Notes to correct (no card change):**
- M1: team_evasion is 2 of 6; remove the Ascension from the support line; Bleeding Effect has 1 flier, not 4.
- M2: haste is 3 + Queen herself.
- M3: tapped lands are 5 by R10.
- M4: Etrata DF is not draw; draw is 9 by tag plus Ravenloft.
- M5: Get Out's wording.
- M6: the Salt fallback becomes Sphinx for Eivor.
- New guide lines:
  - Ravenloft: cast it when Propaganda or Ghostly Prison is out, or when you can retake the initiative by an Assassin hit;
    take Secret Entrance's basic in the color the payment lacks; aim Trap! at the player nearest 10; kill creatures, then
    send Etrata at that player.
  - Ghostly Prison: turn 3 or 4, before the first wide attack.

**Copies after the changes.** All from binders; no new conflict:
- Ravenloft Adventurer: the single Spanish copy.
- Ghostly Prison: the single English copy.
- Secret Tunnel: an English copy; Toph holds another.

Adéwalé, Combustion Man and, with change 3, one Swamp go back to the binders.

---

## 9. Real power and the multiplayer check

**Estimates** (1 to 10; confidence medium-low, no games and no Salt in this step):
| List | Estimate |
|---|---|
| Builder's estimate for this list | 7.2 to 7.7 |
| Reviewer, this list as built | 7.1 to 7.6 |
| Reviewer, with changes 1 and 2 | 7.2 to 7.7 |

**Against three opponents.**
- With Ramses (37 % by turn 7, more with the draw engines), one elimination wins: Ezio's trigger, Slasher + Ezio at 26,
  plain damage, or, with change 1, Etrata's third hit counter.
- Without Ramses, eliminations come one by one, while Arbaaz and Shao Jun lower all three.

**What the pod does to it.**
| Pod action | Effect | Answer in the list |
|---|---|---|
| Spot removal (about 2.3 by turn 8) | Hits Ezio or Ramses | Ezio recasts for 4; Ramses has Boots, ward, Haystack, Imp's Mischief and Get Out, and comes back by Restart, Layla, Jacob or Altaïr |
| A wipe (63 % by turn 8) | Costs two turns | Hakoda before; Get Out and Haystack during; eight rebuild pieces after |
| Graveyard hate | Costs only the recursion | The routes do not depend on it |
| Attack taxes | The deck goes wide on cheap bodies | Trophy, Mortify and Utter End answer the enchantment |

**Single points of failure.**
- No single removal ends the plan.
- The only one-of whose loss costs a whole capability is Ramses (the table win). His second access is Diabolic Tutor; the
  third is Entomb with a recursion card.
- An opponent's Drannith Magistrate would stop Ezio recasts from the command zone: keep Utter End, Mortify or Terminate
  for it.

---

## 10. Gaps not closed
- **No ruling read for:**
  - Jacob Frye's copy cast at the freerunning cost.
  - Whether hit counters from Ravenloft count for Etrata's loss check. The Oracle text counts "exiled cards with hit
    counters" with no source restriction; the 2018 rulings only exclude tokens.
- **My mana model is a scratch model:** greedy play, Orchard and Fellwar at 80 %, no draw engines. Its absolute numbers
  are an estimate; the swap deltas are the reliable part.
- **Web read 2026-11-15 (priors only):**
  - Scryfall API: `https://api.scryfall.com/cards/search?q=is:gamechanger` (53 cards) and the rulings of Etrata, the
    Silencer and Ravenloft Adventurer.
  - EDHREC JSON: `https://json.edhrec.com/pages/commanders/ezio-auditore-da-firenze.json` and `/optimized.json`. Ravenloft
    Adventurer and Ghostly Prison are not in Ezio's lists; Adéwalé is in 14 % of the Bracket 4 lists, Combustion Man in
    13 %, Rogue's Passage in 49 %, Secret Tunnel in 10 %.
- **Initiative's real value at this pod is untested:** it invites attacks on its holder. Changes 1 and 2 are meant
  together.
