# Ezio Auditore da Firenze: collection-only optimization (Phase 2 step 11.1, iteration 3, 2026-11-15)

**Owner swap (2026-11-15, after the Salt diagnosis `decks/reports/salt-diagnosis-20261115.md`).** Eivor, Wolf-Kissed out, Magister Sphinx in (EN, 2X2 247, the free copy). Iter 3 read 4.6 on Commander Salt with no combo line (structural ceiling "no clear win path"); with Sphinx it reads 6.5, bracket 3, the floor. Real power near equal: Sphinx is a second life setter for route 1 and a flier, Eivor was a {B}{B} trampler through freerunning. Plan file updated (route 1 gains Sphinx; route 2 keeps Arno, Bayek, Rally); bracket PASS, gate PASS (2 warnings), 100 copies covered. Eivor goes back to the Spanish binder.

**Fix round (step 11.3, 2026-11-15, the lead on Opus 5.5 high; review `decks/reports/collection-review-ezio-auditore-da-firenze-20261115.md`, verdict FIX).** Applied ranks 1 and 2:

| Out | In | Reason |
|---|---|---|
| Adéwalé, Breaker of Chains | Ravenloft Adventurer (ES, the only copy, Spanish binder) | The initiative is an engine that pays more with three opponents (a land, counters, 5 life loss, a Treasure, a card); every opposing creature death becomes a hit counter, so Etrata, the Silencer's "three hit counters" clause becomes a real kill; a 3/4 Assassin for 4. Adéwalé's Vehicle clause was dead (no Vehicles). |
| Combustion Man | Ghostly Prison (EN, English binder) | A must-have in the primer: only 3 deterrents stayed up while the board is tapped (32 % to have one by turn 5); now 4 (41 %). |

Rank 3 applied on the owner's word (2026-11-15, "whatever makes the deck strongest"; he found Secret Tunnel ideal for Ezio): the tenth Swamp out, Secret Tunnel in (a free copy; two Assassins unblockable each turn; {B}{B} on turn 3 from 78 % to 75 %).

Lead's decisions: Arbaaz Mir stays claimed from Toph (here one of two closers that skip combat; Toph has six other pingers).
Drannith Magistrate is not claimed (no Game Changer role here; revisit if Toph drops it). The Magister Sphinx line stays
out (real power cost near zero; if Commander Salt falls under 6.5, Sphinx comes back for Eivor).

Honest counts (review corrections, no card change): team evasion 2 of 6 real (the pool has no team-evasion card), haste 3
plus Queen Marchesa's, tapped lands 5 by R10 (no free untapped dual left), draw 9 by tag. Five colors ready on turn 7 in
about 66 % of games. Real power after the fix: 7.2 to 7.7 (builder), against 7.0 to 7.5 for the deck as built on
2026-11-09. Confidence medium-low.

Builder notes under `docs/proposals/collection-optimization-brief-20261114.md`: the collection is frozen, so there are no
purchases, no loans and no purchase proposals. Bilingual deck (English copy when both languages are free), proxy commander.
Files: `ezio-auditore-da-firenze.txt` (100 cards), `.plan.json`, this file. Start point: the deck as built on 2026-11-09.

**Result in one paragraph.** 14 cards change. The plan stays (Assassin tempo, Ezio's kill, Ramses as the table win), and the
changes fix what the reading and a mana simulation showed: too few black sources for {B}{B} on turn 3, a five-color payment
that is payable in only about half the games by turn 7, single-color removal against a pod commander with protection from
monocolored, a noncombat route that rested on a 4-mana planeswalker, and too few big Assassins to make freerunning pay. Six of
the ten cards the owner missed in Ezio come back (Royal Assassin, Mortify, Utter End, The Revelations of Ezio, Commander's
Sphere, Evie Frye with Jacob), and Merciless Harlequin leaves.

**Checks (run 2026-11-15 on this list).**
- `python scripts/check_phase2_bracket.py decks/phase2/ezio-auditore-da-firenze.txt`: **PASS** (floor 1, target 3, Game
  Changers 0, no extra turns, no land denial, no reversible card, Spellbook 0 variants inside the list). The live Scryfall
  search `is:gamechanger` (53 cards, read 2026-11-15) names no card of the list.
- `python scripts/plan_density.py`: **PASS**, 0 failures, 1 warning (team_evasion 3 of 6; reason in 3.3).
- 100 cards (1 + 99), counted by script: 36 lands, 63 nonland cards, average mana value 2.794, 28 cards at MV 2 or less.

---

## 1. Profile

### Commander reading (Oracle and rulings, Scryfall API, re-read 2026-11-15)
Ezio Auditore da Firenze, {1}{B}, 3/2 menace, Human Assassin, identity WUBRG. (1) Assassin spells I cast have freerunning
{B}{B}: once an Assassin or my commander has dealt combat damage to a player this turn, they cost {B}{B}. (2) When Ezio deals
combat damage to a player who then has 10 or less life, I may pay {W}{U}{B}{R}{G}; that player loses the game.
- **Rewards:** combat damage to a player, by any Assassin (cost reduction) and by Ezio himself (the kill).
- **Fuel:** attackers that connect every turn from turn 3. **Window:** my combat, then my second main phase.
- **Kill:** one player per trigger, and only with five colors at once. Ramses turns it into a table win.
- **Dies to:** spot removal (he is the visible threat), wipes, a wall of chump blockers, attack taxes.
- **Dependence:** attack engine for the kill; the cost reduction survives his death (any Assassin hit). Protection class 6 to 10.
- **Cost:** 2, so the tax is light (4, then 6). The real mana problem is color: {B}{B} on turn 3 and {W}{U}{B}{R}{G} late.
- **What freerunning does to the mana:** the 24 Assassin creatures carry 45 colored pips (W 8, U 11, B 15, R 10, G 1), all
  paid as {B}{B} after a hit. The other 39 spells carry W 8, U 10, B 13, R 2, G 1. The deck is black with a blue and white
  splash; red and green are there for the payment, Terminate, Hidden Footblade and Assassin's Trophy.

### Rules points to verify
| Point | Status | What falls if wrong |
|---|---|---|
| Ezio's life check happens when his trigger resolves, after all combat damage | Ruling 2024-07-05, verified | Slasher + Ezio same-combat kill |
| Freerunning stays on for the rest of the turn | Ruling 2024-07-05, verified | Second-main-phase pattern |
| Ramses wins on ANY cause of loss if an Assassin of mine attacked that player this turn | Ruling 2022-09-09, verified | Route 1 as a table win |
| A creature that ENTERS attacking did not "attack"; attacking a planeswalker does not count | Rulings 2022-09-09, verified | Altaïr's token copies never satisfy Ramses: declare a real Assassin attacker at every opponent |
| I order Slasher's trigger before Ezio's (a player at 26 or less dies to both connecting unpumped) | Trigger-ordering rule; not ruling-checked | The 26-life line (the 10-life kill stays) |
| Jacob Frye's copy may be cast for {B}{B} | Derived: the ruling says the copy's costs are paid; no ruling on alternative costs | Jacob recasts at full cost |
| Evie's unblockable is a reflexive trigger with its target chosen on the discard | Ruling 2024-07-05, verified | None |
| Waterbend may tap summoning-sick creatures and any artifact; a rock tapped for mana cannot be tapped again | Rulings 2025-10-02, verified | Waterbender Ascension costs real mana |
| Arbaaz Mir counts nontoken permanents only (copies from Jacob and Altaïr are tokens); a legendary land entering counts | Oracle text | Ping count |
| Brotherhood Headquarters cannot pay {W}{U}{B}{R}{G} (a payment during a trigger is neither a spell nor an activated ability) | Card text; play review 2026-10-26 | Payment math (the simulation already excludes it) |
| Imp's Mischief can point a counterspell at itself | Ruling 2004-10-04, verified | It protects against removal only |
| Royal Assassin kills an attacker during an opponent's combat ({T} ability, needs one turn on the battlefield) | Oracle text | It kills only on my turn |
| The Revelations of Ezio, chapter II, puts a counter on every attacking Assassin, Slasher included (it then no longer returns) | Oracle text | Keep Slasher home that turn |
| Combustion Man: the opponent chooses damage or destruction | Oracle text | Never counted as guaranteed damage |

### Plan (one sentence)
Ezio on turn 2, cheap evasive Assassins connect from turn 3 so every Assassin costs {B}{B} and the hits draw cards; lords,
double strike, a 7/6 trampler and Combustion Man push one player after another to 10 or less, where Ezio's {W}{U}{B}{R}{G}
trigger removes them; with Ramses on the battlefield the first elimination wins the game; Arbaaz Mir and Shao Jun damage every
opponent without combat; an attack tax, Royal Assassin, deathtouch and vigilance hold the crack-back.

### Backup (same pieces)
Without Ezio or Ramses the same Assassins keep connecting under Arno, Bayek and Rally the Peasants and kill by plain damage;
Arbaaz Mir, Shao Jun and Combustion Man add damage that ignores blockers; five recursion cards rebuild after a wipe.

### Speed (goldfish, section 5)
Ezio on turn 2 in 95.5 % of games, first hit turn 3, {B}{B} ready on turn 3 in 80 %. First elimination turn 7 (median of five
games: 6, 6, 7, 10, 10). With Ramses on the battlefield that elimination is the game: two of the five games won on turn 6.

### Win lines (chosen before the cards, R26 and R28)
| Route | Closers | Needs | Reached by | Each piece alone | Fails to |
|---|---|---|---|---|---|
| 1. Ezio's elimination, made a table win by Ramses | Ramses, Unstoppable Slasher | Ezio + a connect + a player at 10 or less (26 with Slasher) + five colors; or any kill by damage with Ramses out | Ramses: itself, Diabolic Tutor, Entomb with one of six recursion cards, Adéwalé's dig (6.5 %), Eivor's mill | Ramses a 4/4 deathtouch lord; Slasher a deathtouch body that returns once | Ezio or Ramses removed (damage still kills), a counter (recursion), no fifth color (damage route) |
| 2. Assassin team beatdown | Arno, Bayek, Rally the Peasants, Eivor Wolf-Kissed, Combustion Man | Four to six attackers and one multiplier | 5 closers + 22 attackers | Arno a deathtouch lord, Bayek a double striker, Rally an instant, Eivor a 7/6 trampler, Combustion Man removal or burn on each attack | A wipe (Hakoda, Mana Leak, Get Out, rebuild) |
| 3. Noncombat damage to each opponent | Arbaaz Mir, Shao Jun | 40 historic cards; 17 artifacts | Diabolic Tutor | Arbaaz a 2-mana Assassin; Shao Jun a 3/3 that flies on my turn | A creature wipe; both are small bodies |

No failure point is shared by all three: Ezio dead leaves routes 2 and 3; a wipe is met by Hakoda, two counters and the
rebuild; a counter on Ramses leaves routes 2 and 3; only the recursion of route 1 uses the graveyard; artifact removal costs
route 3 some darts only.

### How it beats three opponents
Ramses makes one elimination a win. Without him the team spreads 15 to 30 damage a turn, Arbaaz and Shao Jun lower all three
at once, and Ezio's trigger then removes a player per turn for five mana instead of ten damage. On the kill turn attack EVERY
opponent with at least one Assassin that was declared as an attacker.

### What it fears
A wipe on turns 5 to 7 (63 % that the table has seen one by turn 8); removal on Ezio before a second Assassin is out; a
missing fifth color (section 3.2); attack taxes; a fast combo. Answers are in section 4.

---

## 2. The puzzle: every card, how to use it here

### Commander
- **Ezio Auditore da Firenze.** Turn 2, always. Attack from turn 3; cast Assassins after the hit. Give him flying (Glider,
  Enter the Avatar State), unblockable (Evie, Waterbender Ascension) or trample (Cloak) for the kill. Partners: Ramses, Slasher.

### Connectors: cheap Assassins that switch freerunning on (6)
- **Hookblade Veteran.** Turn 1. It flies on turn 2, so a 4- or 5-drop can come down for {B}{B} on turn 2. Bad late (1/2).
- **Basim Ibn Ishaq.** Cast any historic spell before combat (38 others in the list, and Ezio): a card, and Basim is unblockable.
- **Brotherhood Spy.** A 2/3 unblockable on my turn while a legendary Assassin is out (20 in the list, plus Ezio).
- **Desmond Miles.** Menace, grows with each Assassin on the battlefield and in the graveyard (23 others); its surveil
  stocks the graveyard for Jacob, Altaïr and The Revelations.
- **Ratonhnhaké꞉ton.** Hexproof and unblockable until its first hit: a sure connect, and a 1/1 menace Assassin token. Its
  Equipment return is rarely live (5 Equipment, and only from the graveyard).
- **Etrata, the Silencer.** Unblockable removal: each hit exiles that player's best creature, then she shuffles away. Attack
  a player with no creatures to keep her. Her three-counter kill is a dead clause here (no blink, no copier).

### Engines: cards from hits (11)
- **Ezio, Blade of Vengeance.** A card per Assassin hit and a 5/5 deathtouch wall. The best {B}{B} play on turn 3 or 4.
- **Coastal Piracy.** The owner's proven draw: a card per creature that connects. Turn 4 or 5, before the wide attacks.
- **Black Market Connections.** Every first main phase: a Treasure (the fifth color), a card, or a 3/2 changeling (an Assassin).
- **Waterbender Ascension** (new). Turn 2 or 3. From the fourth hit, every hit draws. Its waterbend {4} (tap rocks, Equipment
  or summoning-sick creatures) makes Ezio unblockable on the kill turn.
- **Evie Frye** (new). Enters, puts Jacob in hand. {1}, tap: loot; discarding a creature card makes Ezio unblockable and
  feeds Jacob, Altaïr, Desmond and The Revelations. Keep her home: she is a 2/1.
- **Jacob Frye.** Fetches Evie. Each Assassin hit recasts a copy of an Assassin, Eagle Vision or Restart Sequence from the
  graveyard (25 targets). Bad with an empty graveyard.
- **Etrata, Deadly Fugitive.** Each Assassin hit cloaks the top card of that player's library as my 2/2 with ward {2}; a
  1/4 deathtouch blocker that stays home.
- **Queen Marchesa.** Haste, deathtouch, the monarch. Cast her when Propaganda or deathtouch blockers can keep the crown.
- **Layla Hassan.** On entering and on each Assassin hit, a historic card back to hand: a dead legend, an Equipment, the Saga.
- **Adéwalé, Breaker of Chains.** {B}{B} after a hit: a 4/1 and the best Assassin of the top six (81 % to hit, 23 other
  Assassins). Dead clause, named: Vehicles (none in the list).
- **Eagle Vision.** Draw three for {1}{U} after a hit (the owner's proven role-player). Bad before the first hit.

### Payoffs and closers (11)
- **Ramses, Assassin Lord.** One elimination wins the game. Cast him the turn BEFORE the kill, behind ward or Boots.
- **Unstoppable Slasher.** Halves a player's life on a hit; with Ezio on the same player at 26 or less, both connect and the
  player is gone. Returns once when it dies. Keep it home on chapter II of The Revelations.
- **Arno Dorian.** +2/+0 to every other Assassin; deathtouch. Face down for {3} with ward {2} into open removal.
- **Bayek of Siwa.** Historic attackers (20 other legendary creatures, Thopteryx and Ezio) have double strike on my turn: double damage,
  double hit triggers.
- **Rally the Peasants.** Instant +2/+0 for the team, again with flashback. Hold it for the alpha or a bad block.
- **Eivor, Wolf-Kissed** (new). A 7/6 trampler for {B}{B}; tramples over a chump. Each hit mills seven: a land onto the
  battlefield and Assassins into the graveyard for Jacob, Altaïr, Restart Sequence and Layla. Dead before the first hit
  (six mana in three colors); its Saga clause is nearly dead (one Saga).
- **Combustion Man** (new). A 4/6 for {B}{B}. Each attack: name any opponent's best permanent; they lose it or take his power
  in damage. Aim at the player nearest 10.
- **Arbaaz Mir** (new, from Toph). Turn 2 to 4. Every legend, artifact and Saga that enters is 1 damage to EACH opponent and
  1 life. Sequence the cheap artifacts after him.
- **Shao Jun.** Flies on my turn; tap two untapped artifacts for 1 to each opponent, as often as I can. Tapped Equipment
  still works, so tap Equipment first and only the rocks whose mana is not needed.
- **Aya of Alexandria.** Menace, lifelink; each legendary creature that connects makes a 1/1 menace Assassin.
- **Altaïr Ibn-La'Ahad.** Each attack brings back attacking copies of the Assassins in my graveyard. The copies never count
  for Ramses (they enter attacking). Bad with an empty graveyard.

### Attack enablers (5)
- **Swiftfoot Boots.** Hexproof and haste on Ezio or Ramses; equip {1}.
- **Hidden Footblade.** Flash: haste for a recast Ezio, first strike in a combat.
- **Haunted Cloak.** Haste, vigilance, trample: Ezio attacks, tramples over a chump and still blocks.
- **Mechanical Glider.** One mana, attaches itself: Ezio or a connector flies.
- **Assassin Gauntlet.** Taps one opponent's whole board before combat (the kill target, or Royal Assassin's victim); loots.

### Defense while tapped (2 + bodies)
- **Propaganda.** Turn 3 or 4 when two opponents have boards (a proven role-player).
- **Royal Assassin** (new). Kills a tapped creature each turn: an attacker in their combat, or anything that attacked since
  its controller's last untap. Nobody attacks into it; it also takes a removal spell that would have hit Ezio.

### Interaction (9 + the Saga)
- **Swords to Plowshares**, **Infernal Grasp**, **Terminate**: the cheap instant kills.
- **Assassin's Trophy**: any permanent. **Mortify** (new): creature or enchantment, two colors. **Utter End** (new): exile
  any nonland permanent, two colors. With Terminate these four hit a commander with protection from monocolored.
- **Mana Leak**, **Get Out**: hold them for the wipe or the combo piece; Get Out also returns Ezio and Ramses to hand.
- **Mephitic Vapors**: -1/-1 to all, against the 1/1 chump board. It kills my Evie, Royal Assassin and Adéwalé too.
- **The Revelations of Ezio** (new). I: kill a creature that attacked last round. II: a counter on each attacking Assassin.
  III: an Assassin back from the graveyard. Layla returns the Saga itself.

### Protection (5, plus Boots)
- **Gold-Forged Thopteryx.** Ward {2} on Ezio, Ramses and 20 more legends; a flying lifelink blocker.
- **Hakoda, Selfless Commander.** A 3/5 vigilance blocker; sacrifice it (no mana) for team indestructible. Dead clause, named:
  Ally spells from the library (no other Ally).
- **Haystack.** {2}: phase Ezio or Ramses out of removal or a wipe, every turn.
- **Enter the Avatar State.** One mana: hexproof against removal, or flying for the kill.
- **Imp's Mischief** (new). Two mana in the main color: the removal spell aimed at Ezio hits their creature, or a
  counterspell targets the Mischief. Costs life equal to the spell's mana value.
- (Boots above; Mana Leak and Get Out double as protection.)

### Tutors and recursion (3)
- **Diabolic Tutor.** Ramses first; then Slasher, Chromatic Lantern for the payment, or the answer.
- **Entomb.** Ramses into the graveyard when Restart Sequence, Layla, Jacob, Altaïr or The Revelations is at hand.
- **Restart Sequence.** {1}{B} after a hit: Ramses, Ezio Blade or Eivor back.

### Mana (10 rocks + 36 lands)
- **Sol Ring**; **Arcane Signet**, **Fellwar Stone**, **Talisman of Progress**, **Orzhov Signet**, **Golgari Signet**,
  **Rakdos Signet** (turn 3 or 4, after Ezio; each is also a Basim trigger, an Arbaaz ping and a dart for Shao Jun).
- **Chromatic Lantern** (every land pays the five colors), **Commander's Sphere** (new; any color, a card when it is no longer
  needed), **Bender's Waterskin** (any color; one mana on each opponent's turn for a one-mana instant after tapping out).
- **Lands:** Command Tower, Exotic Orchard, Path of Ancestry, Brotherhood Headquarters (pays {B}{B}, never the kill), Abstergo
  Entertainment (filter and graveyard hate on demand), Concealed Courtyard, Isolated Chapel, Drowned Catacomb, Sunken Hollow,
  Dragonskull Summit, Smoldering Marsh, Woodland Cemetery, Woodland Chasm (new), Battlefield Forge, Sulfur Falls, Hinterland
  Harbor, Prairie Stream, Glacial Fortress (new); 10 Swamp, 3 Island, 3 Plains, 1 Mountain, 1 Forest.

---

## 3. Curve and ratios

| MV | Count | Cards |
|---|---|---|
| 1 | 7 | Sol Ring, Hookblade Veteran, Hidden Footblade, Mechanical Glider, Swords, Enter the Avatar State, Entomb |
| 2 | 21 | 6 rocks, Basim, Desmond, Spy, Evie, Arbaaz, Thopteryx, Boots, Haystack, Waterbender Ascension, Grasp, Trophy, Terminate, Mana Leak, Get Out, Imp's Mischief |
| 3 | 19 | Lantern, Waterskin, Sphere, Jacob, Slasher, Royal Assassin, Ratonhnhaké꞉ton, Shao Jun, Altaïr, Etrata DF, Adéwalé, BMC, Propaganda, Revelations, Cloak, Gauntlet, Mortify, Rally, Vapors |
| 4 | 11 | Ramses, Arno, Queen, Etrata S, Aya, Layla, Hakoda, Coastal Piracy, Utter End, Restart Sequence, Diabolic Tutor |
| 5 | 4 | Ezio Blade, Bayek, Combustion Man, Eagle Vision |
| 6 | 1 | Eivor, Wolf-Kissed |

26 creatures (24 Assassins, plus Thopteryx and Hakoda), 17 artifacts, 5 Equipment, 22 legendary cards, 40 historic cards.
Ten Assassins cost 4 or more: the cards freerunning really discounts (8 before). Toughness 2 or less: 8 of 27 creatures with
Ezio (30 %, under a third).

### 3.1 Profile table (combat_attackers with alternate_kill as second plan)
| Function | Tier | Min | Target | Actual | Needed by | Reason for THIS deck |
|---|---|---|---|---|---|---|
| attackers | gate | 12 | 16 | 21 + Ezio + tutor | early | The fuel: 96 % to hold one by turn 5 without Ezio |
| through_wide_board | gate | 10 | 12 | 16 + tutor (about 14 weighted) | early | 6 fliers or unblockables, Glider, Evie, Ascension, Gauntlet, Vapors, trample (Eivor, Cloak), noncombat (Arbaaz, Combustion Man); half weight for the one-shots |
| through_big_creatures | gate | 10 | 12 | 15 + tutor | early | 6 instant answers, Royal Assassin, Etrata, 5 deathtouch attackers, Combustion Man, the Saga |
| condition_enablers | gate | 10 | 12 | 16 + Ezio + 2 tutors (about 13 weighted) | early | 8 team-wide (Arbaaz, Shao Jun, Arno, Bayek, Ramses, Rally, Aya, Altaïr), the rest single-target at half |
| team_finishers | gate | 6 | 8 | 6 + Diabolic Tutor | late | Ramses, Arno, Bayek, Rally, Shao Jun, Arbaaz. At the minimum: the pool has no overrun or extra combat left |
| haste | support | 4 | 6 | 4 | early | Boots, Footblade, Cloak, Queen. Not promoted: freerunning works from any Assassin hit, so a turn without Ezio is not dead |
| team_evasion | support | 6 | 8 | **3 (WARN)** | early | Gauntlet, Vapors, Ascension. Reason in 3.3 |
| defense_while_tapped | support | 4 | 6 | 6 | early | Propaganda, Royal Assassin, Etrata DF, Hakoda, Cloak, Thopteryx |
| combat_draw | support | 4 | 6 | 7 | early | Ezio Blade, Coastal, Etrata DF, Ascension, Eagle Vision, Jacob, Gauntlet |
| wipe_insurance | support | 2 | 3 | 10 | late | Hakoda, Haystack, Get Out, Mana Leak; rebuild: Restart, Layla, Jacob, Altaïr, Slasher, the Saga |
| payment_enablers | support | 6 | 8 | 10 | early | Tower, Orchard, Path, Arcane Signet, Fellwar, Lantern, Waterskin, Sphere, BMC, Abstergo |

Fit check, each card once: 36 lands + 10 rocks + 26 creatures + 5 enchantments + 6 other artifacts + 16 instants and
sorceries = 99. Every gate minimum is met inside those slots; no function needed a card that serves nothing else.

Base floors by tag (gate): ramp 11 (min 10), draw 10 (10), spot removal 12 (6), wipes 1 (1), protection 8 (6).
- **Ramp, honest timing:** turn 2 is Ezio's, so only Sol Ring is cast earlier; the six 2-mana rocks come on turns 3 and 4
  next to a {B}{B} Assassin, the three 3-mana rocks on turn 4 or later. They are counted because they pay the five-color
  kill, and each is also a historic spell (Basim, Arbaaz) and a dart (Shao Jun). Karsten's model gives a 2-mana commander
  no rocks at all; the payment is why this deck keeps ten.
- **Draw, honest weight:** 10 by tag, about 9 at full weight (Evie nets one card once; Queen's monarch and the Ascension
  are conditional). Jacob and Layla are recursion and are not counted. Selection on top: Evie's loot, Desmond's surveil.
- **Answers:** 8 spot answers plus Royal Assassin, Etrata, Combustion Man and the Saga against 27 closing cards.

### 3.2 Mana (the study: notes/02, notes/13, references mana-and-ramp and probability)
**Lands and rocks.** 36 lands (was 35) and 10 rocks: 46 sources, lands 78 % (R8: 46 or more, lands two thirds or more). The
band is 36 to 38; 36 because the average MV is 2.79, 28 cards cost 2 or less and freerunning pays for the top end. Karsten's
formula (31.42 + 3.13 x 2.79 - 0.28 x 13 cheap rocks and draw) gives 36.5.

**Colored sources** (raw; Karsten weight in brackets: rocks 0.75, Orchard 0.75, Fellwar 0.5):
| Color | Lands | Rocks | Total (weighted) | Pips, all | Pips outside the Assassins | Karsten row and need | Verdict |
|---|---|---|---|---|---|---|---|
| B | 22 | 8 | 30 (27.5) | 28 | 13 | Ezio {1}{B}: 19. {B}{B} on turn 3: 28 | Met for Ezio, at the line for {B}{B} |
| U | 12 | 6 | 18 (16.0) | 21 | 10 | Mana Leak {1}{U}: 19. Coastal Piracy {2}{U}{U}: 26 | Short: blue is a mid-game color here |
| W | 11 | 7 | 18 (15.8) | 16 | 8 | Swords {W}, Thopteryx: 19 on curve; 16 from turn 4 | Met from turn 4 |
| R | 8 | 6 | 14 (12.0) | 12 | 2 | Terminate, Footblade: 15 to 16 late | A splash, with the payment |
| G | 7 | 6 | 13 (11.0) | 2 | 1 | Assassin's Trophy; payment only: 12 to 15 | A splash, the scarcest payment color |

**Untapped lands (R10).** Always tapped: Path of Ancestry and Woodland Chasm (2 of the 3 allowed). Conditional: three
battle lands (two basics needed; 18 basics), six check lands (their types sit on 10 Swamps and the typed duals), Concealed
Courtyard (untapped turns 1 to 3). No colorless land except Abstergo (filter and the only graveyard hate) and Headquarters
(black for every Assassin). Secret Tunnel left for a colored land.

**Odds, computed** (scratch simulation, 40,000 games, real enter-tapped rules, free mulligan, greedy land choice, Orchard
and Fellwar giving each color 80 % of the time, Headquarters never paying the kill; second figure = one extra card on 60 %
of the turns from turn 4, for the draw engines):
| Event | Deck as built today (35 lands) | This list |
|---|---|---|
| Ezio cast on turn 2, with his color | 94.6 % | **95.5 %** |
| Ezio cast by turn 3 | 97.9 % | **98.5 %** |
| {B}{B} available on turn 3 | 75.7 % | **79.8 %** |
| Ezio on turn 2 AND {B}{B} on turn 3 | 73.6 % | **77.7 %** |
| {B}{B} by turn 4 | 91.8 % | 94.4 % |
| Blue on turn 3 / white on turn 3 | 67 % / 70 % | 68.5 % / 68.9 % |
| {2}{U}{U} on turn 5 (Coastal Piracy) | 58 % | 64 % / 67.5 % |
| {W}{U}{B}{R}{G} payable on turn 6 | 43.9 % | 49.5 % / 58.6 % |
| ... on turn 7 | 52.8 % | **58.8 % / 69.8 %** |
| ... on turn 8 | 60.2 % | **66.1 % / 78.2 %** |
| ... on turn 8 with 2 mana to spare | 44.7 % | 51.0 % / 70.2 % |
| Three lands on turn 3 / four on turn 4 | 88.7 % / 71.7 % | 89.8 % / 73.8 % |

Reading: Ezio is on time in 19 games of 20. The five colors are NOT there in three to four games of ten on turn 7: this is
the deck's real limit with this collection (no fetch lands, shock lands or Triomes). What was done: one more land, a tenth
rock that makes any color (each any-color source adds 2 to 4 points; a Signet adds less), Woodland Chasm for green, no
colorless land. What the guide does: play for damage, treat the trigger as a bonus, fetch Chromatic Lantern with the tutor
when the kill is the plan, keep BMC Treasures. Hands: 2 to 4 lands in seven is 74.0 %, 93.3 % with the free mulligan (exact).

### 3.3 WARN reasons and dead clauses
- **team_evasion 3 of 6.** The pool has no team-evasion card for this deck: Cover of Darkness went back to the Standard
  binder when the loans closed, Turnabout and Aether Gale are single copies in Azula, and Bleeding Effect gives flying only
  if a flier is already in the graveyard (4 fliers in 99). Board 1 is carried by through_wide_board at 16: six evasive
  Assassins, three ways to make Ezio himself evasive, Gauntlet, Vapors, two tramplers and three noncombat sources. Not
  relabelled: single-target evasion is not counted as team evasion.
- **Dead or weak clauses, counted:** Adéwalé (Vehicles 0); Hakoda (Allies 0); Eivor (Sagas 1; lands 36); Ratonhnhaké꞉ton
  (Equipment 5, graveyard only); Etrata the Silencer (third counter). Live counts for the rest: Basim 38 historic spells
  and Ezio; Arbaaz 40 historic cards; Bayek 22 historic creatures; Shao Jun 17 artifacts; Spy 21 legendary Assassins;
  Jacob 25 targets; Altaïr and the Saga 23 Assassins; Layla 40; Thopteryx 23 legends; Path of Ancestry 25 creatures sharing a type. No equipment-matters
  card, no blink payoff, no Vehicle payoff is played.

---

## 4. Interaction plan and protection plan

- **What the table holds by turn 8:** about 2.3 spot removal, 0.9 wipes and 0.45 counters across three opponents. One removal
  will hit Ezio; a wipe comes in two games of three.
- **Spot answers (R19):** 8, all instants: Swords, Grasp, Trophy, Terminate, Mana Leak, Get Out at MV 2 or less; Mortify at
  3; Utter End at 4. Utter End is over the 3-mana line on purpose: it is the exile answer to anything, and one of four
  two-color answers the pod needs. Artifacts: Trophy, Utter End, Combustion Man. Enchantments: Trophy, Mortify, Utter End,
  Get Out. Spend them on what wins next turn, on the blocker in the way of the kill, on an attack tax.
- **Repeatable answers:** Royal Assassin, Etrata the Silencer, Combustion Man, the Saga.
- **Opposing commanders:** Swords, Utter End and Etrata exile; Royal Assassin kills each recast that attacks. Against
  protection from monocolored: Trophy, Terminate, Mortify, Utter End, and the two-color deathtouch creatures (Ramses, Arno,
  Queen, Ezio Blade, Etrata DF) block and kill it; Ezio himself (black only) cannot block or damage it.
- **Graveyard hate:** Abstergo Entertainment, on demand (it also empties my graveyard: use it last).
- **Commander protection (8, class 6 to 10), layered:** hexproof (Boots, Enter the Avatar State), ward (Thopteryx), phasing
  (Haystack), redirect (Imp's Mischief), counters (Mana Leak, Get Out), bounce (Get Out), indestructible (Hakoda).
- **Win-turn shield (R24, 3 or more at MV 2 or less):** Imp's Mischief, Enter the Avatar State, Get Out, Mana Leak,
  Haystack's activation, Boots already on Ezio; Waterskin gives one mana on their turns. Sequence: Ramses the turn before;
  on the kill turn make Ezio evasive, keep two mana up, attack every opponent, pay the five colors.
- **Wipes (R32):** commit what wins in two turns, keep one Assassin in hand when two opponents can wipe. Before: Hakoda.
  During: Mana Leak, Get Out, Haystack. After: Ezio for 4, Restart Sequence, Layla, Jacob, Altaïr, Slasher, the Saga, Eagle Vision.
- **Archenemy (R30):** always-on deterrents are Propaganda, Royal Assassin and Etrata DF; never show lethal one turn early.
- **Game Changers (R34): 0 of 3.** The collection holds three: Drannith Magistrate and Crop Rotation (Toph) and Narset
  (Azula). Crop Rotation and Narset do nothing here. Drannith was weighed as a claim: it is strong, but it is a lock with
  no function in the plan that turns three players against the deck that is already the visible attacker (R30, notes/12
  C6), and Toph plays it. Left out; the lead may overrule (it would replace Adéwalé).
- **R36, non-Game-Changer power cards:** in: Swords, Fellwar, Sol Ring, Signets and Talisman, Imp's Mischief. Not available:
  Deflecting Swat, Swan Song, Spell Pierce, Snap (Azula, final), Path to Exile and Redirect Lightning (Toph; not claimed, see 7).

---

## 5. Mulligan, play pattern and tests

**Keep:** 2 to 4 lands with a black source, and a plan piece or a rock (Ezio is always the turn-2 play). Five lands with two
plays. **Ship:** 0 or 1 land (one land with Sol Ring and black is a keep), 6 or more lands, no black source, answers only.
**Keep almost any land-good hand with:** Hookblade Veteran, Basim, Brotherhood Spy, Sol Ring, Ramses, Ezio Blade, Coastal
Piracy, Black Market Connections, Arbaaz Mir, Waterbender Ascension.

**Turns 1 to 5.** T1 a tapped land, or Sol Ring, Veteran. T2 Ezio. T3 attack; after the hit the best Assassin for {B}{B}
(Ezio Blade, Ramses at a slow table, Arno, Eivor), one spare mana for Glider or a held Swords. T4 two {B}{B} Assassins, or
one and a rock or an engine (Coastal Piracy, BMC, Ascension). T5 Propaganda or Royal Assassin if the board is tapped out;
keep two mana up from here.
**Turns 6 to 9.** Pick the target (nearest to 10, or the combo player). Slasher and Ezio on the same player; Gauntlet or
Vapors for the blockers; Rally for the last points. Ramses the turn before.
**Late.** Arbaaz, Shao Jun and Combustion Man finish; Restart, Layla, Jacob and the Saga rebuild; Eagle Vision refills.

**20 opening hands** (seed 20261115, checklist applied by script): 17 keep the first seven, **19 of 20 with the free
mulligan (95 %)**. Ships: one hand with no black source, two one-landers (one stays a one-lander after the mulligan). Large
sample, 50,000 hands, same checklist: 70.2 % keep, **91.0 % with the free mulligan**.

**Goldfish, 5 kept hands (seed 11), one opponent targeted:**
1. Swamp, Swamp, BMC, Layla, Altaïr, Restart, Swords: Ezio T2, hit T3 and Layla, T4 Altaïr and Shao Jun, T5 BMC, T6
   Gauntlet; the target is at 6 on T6 with no white, red or green for the kill; dead to damage T7.
2. Rally, Ratonhnhaké꞉ton, Island, Grasp, Sphere, Utter End, Swamp: two lands and no third until turn 6. Ezio T2 and
   alone until Ezio Blade on T6; elimination about T10. The two-land keep that fails.
3. Courtyard, Swamp, Waterskin, Avatar State, Diabolic Tutor, Ascension, Ezio Blade: Ezio T2, Ramses for {B}{B} T3, Ezio
   Blade T4, Bayek T5; T6 double strike for 34 on a player at 16: **win on turn 6** through Ramses.
4. Desmond, Island, Sphere, BMC, Swamp, Swamp, Restart: Ezio T2, Queen T3 and Entomb for Ramses, Restart Sequence returns
   Ramses T4, 16 damage T5 and T6: **win on turn 6**.
5. Swamp, Swamp, Grasp, Hakoda, Coastal, Eagle Vision, Mischief: Ezio T2, Eagle Vision T4, Coastal and Arbaaz T5, Royal
   Assassin T6; few attackers; elimination about T10.
Record: Ezio on turn 2 in 5 of 5, first hit turn 3 in 5 of 5, eliminations T6, T6, T7, T10, T10 (median 7).

**Disrupted.** (a) Ezio killed on his first attack (game 1): no hit, BMC on T3, Ezio again on T4 for 4, hit on T5 with two
Assassins after it; one to two turns lost. With Veteran, Spy or Basim out, nothing is lost. (b) Wipe after my turn 5 (game
4), no shield in hand: Ezio for 4 with Boots attacks at once on T6, Combustion Man after the hit, threat again on T8; two
turns lost. (c) Ramses countered on T3 (game 3): Restart Sequence returns him on T5; the win moves from T6 to T7.

**Reference boards.** Board 1, eight 1/1 chump blockers: Veteran, Basim, Spy, Shao Jun, Ratonhnhaké꞉ton and Etrata go over or
past them; Glider, Avatar State, Evie and the Ascension do it for Ezio; Gauntlet taps them; Vapors kills them all; Eivor and
a Cloaked attacker trample; Arbaaz, Shao Jun and Combustion Man ignore them. Their sacrifice outlet kills my 8 creatures of
toughness 2 or less: Ramses' +1/+1 and Hakoda cover them. Board 2, two bigger creatures: six instant answers, Royal
Assassin, the Saga, Etrata's exile, five deathtouch attackers, Etrata DF and Hakoda as blockers, fliers and unblockables.

**Gauntlet (R39).** (1) Fast combo: Mana Leak, Get Out, six instant kills, Trophy and Utter End for the piece, and the
turn-7 clock aimed at that player; a protected all-spell combo is the worst case (two counters only). (2) Stax and taxes:
28 cards at MV 2 or less; Trophy, Mortify, Utter End, Combustion Man; under a Propaganda, attack with two and let Arbaaz and
Shao Jun work. (3) Go-wide: Board 1. (4) Big creatures: Board 2. (5) Control: ward, Boots, Haystack, Imp's Mischief and two
counters for the engine, Hakoda for the wipe, cheap threats and five recursion cards after it; hold one threat.

**Final cut pass (the 10 weakest, each against the best card left out).** Hookblade Veteran (Aven Heartstabber: a turn
slower), Adéwalé (Lydia Frye, Petty Larceny: the draw floor), Mechanical Glider (Hookblade: dearer), Mephitic Vapors (Ritual
of Soot: kills my own), Rakdos Signet (Talisman of Conviction: no black), Golgari Signet (the green of the payment), Mana
Leak (It'll Quench Ya!: weaker), Enter the Avatar State (Undying Malice: no evasion), Altaïr (Lydia Frye), Utter End
(Kolaghan's Command: cannot hit the protected commander). All ten stay.

---

## 6. The owner's cards (review of 2026-11-14)

Ezio is five colors, so every card of the review gets a verdict.
| Card | Verdict | Reason |
|---|---|---|
| Merciless Harlequin | **OUT** (he is right) | A 2/1 that draws one card. Evie Frye takes the slot: also a cheap Assassin that nets a card (Jacob), and then loots and makes Ezio unblockable every turn |
| Evie Frye with Jacob Frye | **IN, both** | Either one fetches the other. Evie's discards feed Jacob's recasts, Altaïr, Desmond and the Saga, and her unblockable is the cheapest repeatable way to land Ezio's kill |
| Royal Assassin | **IN** | A deterrent that also kills: it covers the open board after an attack (his lesson L3) and takes a removal spell meant for Ezio. In for Loyal Inventor |
| Mortify | **IN** | Instant, two colors, also enchantments. In for Feed the Swarm (sorcery, one color, costs life) |
| Utter End | **IN** | Exile, any nonland permanent, two colors. In for Chaos Warp (one color, and red is the fourth color here) |
| The Revelations of Ezio | **IN** | A kill, a counter on each attacker and an Assassin back, for three mana; the pod always has a tapped attacker; Layla returns the Saga. In for Bitter Triumph, the ninth one-for-one answer |
| Commander's Sphere | **IN** | An any-color rock is worth 2 to 4 points on the five-color payment (3.2); a card when it is spare. Added as the tenth rock |
| Mana Leak | **IN** (stays) | The counter held for the wipe or the combo piece |
| Lydia Frye | **OUT** | Her job is an evasive Assassin. Brotherhood Spy, Hookblade Veteran, Shao Jun and Etrata do it against any blocker, and her evasion fails against exactly the 1/1 board that beat him (L3, L8). Her surveil is selection, which Evie gives with an unblockable on top. First creature in if a slot opens (for Adéwalé, at the cost of the draw floor) |
| Deadeye Navigator | **OUT** | Six real mana in a deck that pays {B}{B}: it is not an Assassin, so freerunning never discounts it. Blink partners counted: Adéwalé, Layla, Queen, Arbaaz, Ratonhnhaké꞉ton, Etrata, Slasher (7 of 26), each blink {1}{U} more. Haystack does the protection job for 2 mana from turn 2 and also dodges wipes; Layla, Jacob and Restart Sequence re-use Assassins for {B}{B} |
| Return the Favor | **OUT** | One copy, in Azula, where every copy is doubled. Here {R}{R} is the problem: red has 14 sources (two red by turn 7 in about half the games). Imp's Mischief does the redirect from the main color |
| Tome of Legends | **OUT, not contested** | Comparison: in both decks it is about one card a turn for {1} while the commander attacks. Ezio got Black Market Connections back from Azula, and the Tome is what Azula took for it; taking both would leave her with neither, and she spends cards faster. Ezio keeps 10 draw pieces; Waterbender Ascension is the new continuous one |
| Waterbending Lesson | **OUT** | Four real mana at sorcery speed for three cards; Eagle Vision does it for {1}{U} |
| Mystical Teachings | **OUT** | Four mana to find a one- or two-mana instant in a deck that taps out; Diabolic Tutor finds Ramses for the same four |
| Torrential Gearhulk | **OUT** | Azula's only copy and her best card; six mana, and Ezio's 12 instants are mostly one- and two-mana answers |
| Frostcliff Siege | **OUT, not contested** | Azula's only copy and her proven draw. Here Coastal Piracy, Ezio Blade and the Ascension draw on hits |
| Aether Gale | **OUT** | Azula's only copy; five real mana. Gauntlet and Vapors open the board for three |
| Imprisoned in the Moon | **OUT** | Azula's only copy. Swords, Utter End and Etrata exile a commander; Royal Assassin kills each recast |
| Hardened Scales, Inscription of Abundance, The Stasis Coffin, Alibou | **OUT** | Toph's cards: no counters plan here, 13 green sources, the Coffin protects the player and not the board, one artifact creature |

---

## 7. Copies

**Claimed from another deck (1).**
| Card | Copies | Holder today | Why it adds more here | What that deck loses |
|---|---|---|---|---|
| Arbaaz Mir | 1 (Spanish) | Toph (not yet optimized) | Here it is the best of only two noncombat closers, an Assassin (lords, freerunning, Ramses), and 40 of 99 cards trigger it; it lowers all three players toward Ezio's 10. In Toph it is one of seven drain closers and does not see land entries | One pinger and the short kill of its loop B; its notes name Fire Nation Archers as the fallback |

**Not claimed, on purpose.** Drannith Magistrate (Toph; section 4). Path to Exile (Toph's Spanish copy; Ezio has six instant
kills and Toph few). Make a Stand (Toph's only wipe insurance; Ezio has Hakoda). Relic of Legends (Kilo's combo piece).
Nothing is contested with Azula.

**Free copies taken** (binder): Royal Assassin (3 EN free), Combustion Man (2 EN), Mortify (4 EN), Imp's Mischief (1 EN),
Waterbender Ascension (1 EN), Commander's Sphere (1 EN; Kilo keeps the Spanish one), Woodland Chasm (1 EN), Glacial Fortress
(1 EN; Kilo keeps the Spanish one), a tenth Swamp (22 EN free), Evie Frye (1 ES), Eivor Wolf-Kissed (1 ES), Utter End (1 ES),
The Revelations of Ezio (2 ES).

**Cards whose copies run short** (one copy per deck that wants it; no new conflict): with Azula: Swiftfoot Boots, Hidden
Footblade, Propaganda, Mana Leak, Terminate (2 each), Bender's Waterskin (3), Drowned Catacomb, Dragonskull Summit, Sunken
Hollow, Smoldering Marsh (2 each), Sulfur Falls (3). With Toph: Haystack, Battlefield Forge (2 each), Swords (3, all used),
Sol Ring (4, all used). With Kilo: Swords, Sol Ring. Single copies only Ezio plays: Black Market Connections, Diabolic
Tutor, Infernal Grasp, Fellwar Stone, the Signets, Get Out, Hakoda and every Assassin legend.

**Freed for the later decks:** Kolaghan's Command, Bitter Triumph, Chaos Warp, Feed the Swarm, Loyal Inventor, Magister
Sphinx, Roshan, Lion Vulture, Kaya, Hookblade, Cobbled Wings, Merciless Harlequin, Secret Tunnel, Clifftop Retreat (Spanish).

**Language, where it is not English** (no English copy owned or free). New: Evie Frye, Arbaaz Mir, Eivor Wolf-Kissed, Utter
End, The Revelations of Ezio. As today: Hookblade Veteran, Brotherhood Spy, Orzhov Signet, Ezio Blade of Vengeance, Assassin
Gauntlet, Restart Sequence, Swords to Plowshares (BLC 109, pinned), Exotic Orchard, Brotherhood Headquarters, Isolated
Chapel, Woodland Cemetery, Hinterland Harbor. Everything else is English.

**For the lead.** (1) The Arbaaz Mir claim. (2) New pins are not needed; the tenth Swamp is any free English one. (3) No new
token: the new cards make none; Kaya leaves. (4) If Commander Salt falls under the 6.5 floor: the list no longer holds a
Spellbook line (Ezio + Magister Sphinx left); the first swaps to try are Magister Sphinx for Adéwalé and Loyal Inventor for
Mechanical Glider, both free again, gate re-run. (5) `plan_density.py` regenerates all four consistency reports on every run; this build changed only Ezio's files.

---

## 8. Changes against the deck as built today (14 out, 14 in)

| OUT (to the binder) | Job it did | IN | From | Why |
|---|---|---|---|---|
| Merciless Harlequin | cantrip body | Evie Frye | Spanish binder | Section 6 |
| Kaya, Ghost Assassin | noncombat closer | Arbaaz Mir | Toph's deck (Spanish) | 1 to each opponent on 40 cards, for 2 mana, on an Assassin; Kaya was a 4-mana planeswalker behind a tapped board |
| Lion Vulture | draw engine at 4 | Waterbender Ascension | English binder | Draws on hits for 2 mana, survives creature wipes, and makes Ezio unblockable |
| Roshan, Hidden Magister | made non-Assassins cheap | Combustion Man | English binder | With Sphinx, Inventor and Vulture gone only two creatures are not Assassins; a 4/6 that removes or burns on every attack uses {B}{B} better |
| Magister Sphinx | life setter, 7 mana | Eivor, Wolf-Kissed | Spanish binder | Castable only through Roshan or Entomb; Slasher keeps the setter job. A 7/6 trampler for {B}{B} hits from turn 4 and fills the graveyard |
| Loyal Inventor | artifact tutor | Royal Assassin | English binder | Its target was the Sphinx. Section 6 |
| Feed the Swarm | removal | Mortify | English binder | Section 6 |
| Chaos Warp | removal | Utter End | Spanish binder | Section 6 |
| Bitter Triumph | removal | The Revelations of Ezio | Spanish binder | Section 6 |
| Cobbled Wings | flying for Ezio | Imp's Mischief | English binder | Evie and the Ascension now make Ezio evasive; protection goes from 7 to 8 with a 2-mana black redirect |
| Hookblade | flying for Ezio | Commander's Sphere | English binder | The weakest Equipment (2026-11-08 review); the tenth rock for the payment |
| Kolaghan's Command | flexible answer | Swamp (tenth) | English binder | The 36th land; artifact answers stay at three |
| Secret Tunnel | evasion land | Woodland Chasm | English binder | The colorless land cost 2.6 points of {B}{B} on turn 3; Chasm is black and green and a Swamp Forest for the check lands |
| Clifftop Retreat | red-white land | Glacial Fortress | English binder | Blue has 10 pips outside the Assassins, red 2: blue on turn 3 +2.5 points, Coastal Piracy on turn 5 +2.8 |

Function counts after the cuts: spot answers 8 (min 6), wipes 1, protection 8, draw 10, ramp 11, team finishers 6 + tutor,
noncombat closers 2, evasion for Ezio 7 (Glider, Avatar State, Evie, Ascension, Gauntlet, Cloak, Vapors), tutors 2.

**Considered and left out** (the card that keeps the slot): Lydia Frye, Deadeye Navigator, Tome of Legends, Return the Favor
(section 6); Drannith Magistrate (section 4); Ghostly Prison (Royal Assassin: a deterrent that kills; defense is at 6);
Haytham Kenway (a fourth 4-mana card at full price; his exile ends when he dies); Petty Larceny (Adéwalé: a body and an
Assassin card); Rooftop Bypass and Bleeding Effect (need a board or a stocked graveyard first); Viewpoint Synchronization and
Hunter's Bow (green at 13 sources); Sokka, Lateral Strategist (not an Assassin, 3 real mana); Hidden Blade (a trick; evasion
was the need); Aven Heartstabber, Nekrataal, Thorn of the Black Rose, Winter Soldier (5 Equipment: the dead clause again);
Rogue's Passage (a colorless land again); Energybending (about 2 points on the payment for a whole slot); Thriving Moor (a third tapped land for 1.8
points); Talisman of Conviction (no black); Undying Malice, Octopus Form (protection is at 8); Auditore Ambush.

---

## 9. Real power (1-10: 4 precon, 6 upgraded, 7-8 high power, 9-10 cEDH)

| List | Estimate | Confidence |
|---|---|---|
| Deck as built today (2026-11-09) | 7.0 to 7.5 (the 2026-11-08 review's figure) | medium-low |
| **This list** | **7.2 to 7.7** | medium-low (no games; Salt not measured in this step) |

Why up, about +0.2: {B}{B} on turn 3 goes from 76 to 80 % and the kill payment from 53 to 59 % on turn 7 (same simulation);
ten Assassins that freerunning discounts instead of eight; a noncombat source that hits all three players from turn 2;
answers that work against the pod's protected commander; Royal Assassin and a second redirect for the turns the board is
tapped; no 7-mana card and no card that needed Roshan. Why not higher: one real tutor for Ramses (Ramses, the tutor or
Entomb in 37 % of games by turn 7, 53 % by turn 10 with the draw engines); the five colors missing in three games of ten on
turn 7; team evasion at 3; no Game Changer, no fast mana beyond Sol Ring. Commander Salt may read this list slightly lower
than today's (its one Spellbook line and an artifact tutor left); the swaps for that case are in section 7.

---

## 10. Knowledge used

| Source | What it demands of this deck | How the list answers |
|---|---|---|
| **Skill, steps 1 to 3 and `archetypes.json`** (combat_attackers + alternate_kill, hybrid rule) | Read the commander; one plan; profile by fuel; both gate profiles under their names | Section 1; profile table 3.1; five gate functions and six support lines declared; fit check |
| Skill steps 4 to 8 | Lands by band, colored sources by pip, layered protection, two boards, attack lines before safety | 36 lands, source table and simulation (3.2); 8 protection in six layers; boards in 5; haste 4, defense 6, evasion for Ezio 7 |
| Skill steps 9 to 15, references (evaluation, role-players, card-flow, win-routes, plan-file, probability, tools) | Bridge cards judged with the commander out; proven role-players stay; dead clauses named; cuts logged; honest tags; EDHREC only a prior | Lantern, Sphere and Waterskin kept as payment bridges; Eagle Vision, Coastal Piracy and Propaganda stay; dead clauses counted (3.3); cut log (8); recursion not tagged as draw; no pick rests on inclusion |
| **Champion addendum, items 1 to 3** (one plan, cards work alone, redundancy) | One plan with a backup on the same pieces | Section 1; 0 plan cards outside a function; no two-card package |
| 4 multi-role (R4) | Count cards with two jobs | About 28 of 63 (Arbaaz, Shao Jun, Combustion Man, Royal Assassin, Evie, the Ascension, Cloak, the rocks as historic spells) |
| 5 commander-centric (R5) | 12 or fewer cards blank without the commander | 0: freerunning needs any Assassin hit. 12 cards need a hit that turn (ten big Assassins, Eagle Vision, Restart) |
| 6, 7 lands and sources | Land count from curve; Karsten's table | 3.2 |
| 8 total sources (R8) | 46 or more, lands two thirds | 36 + 10 = 46, lands 78 % |
| 9 fast mana (R9) | Sol Ring, Signet, Fellwar, Talismans before 3-mana rocks | All owned ones in; Mox Amber and rituals are not owned |
| 10 tapped lands (R10) | At most 3 always tapped | 2 |
| 11 window costs | Count the sources at the payment step, joint colors | Payment simulated: 59 to 70 % on turn 7; the guide treats the kill as a bonus |
| 12, 13 curve, tax | Low curve; recast arithmetic | 2.79; Ezio costs 4 on the first recast, haste from four cards |
| 14 (R14) | Bracket 4 lists run 33 lands | 36: this base is slower than fetch-and-shock bases and needs the colors |
| 15 engines and budget | Card flow through turns 4 to 8 | Spend 1 to 2 a turn; gain 1 + engines (9 repeatable) |
| 16 scaling draw (R16) | Two or more pieces that scale with the table | Coastal Piracy, Ezio Blade, the Ascension, Etrata DF, the monarch |
| 17 development first (R17) | Early draw at 2 mana or engines | Basim, Evie, the Ascension at 2; Eagle Vision at {1}{U} |
| 18 tutors (R18) | 10 access cards to the primary route | Not met, said plainly: Ramses has about 4 (itself, Diabolic Tutor, Entomb, the dig). The route is a board engine that also wins by damage; the Game Changer tutors are not owned |
| 19 answers (R19) | 8 spot, 5 at MV 2 or less, 5 instants, 2 per permanent type | 8, 6, 8; artifacts 3, enchantments 4; one exception written (Utter End) |
| 20 counters (R20) | 2 to 4 for a deck that taps out | Mana Leak, Get Out, plus Imp's Mischief |
| 21 wipes (R21) | Only asymmetric | Mephitic Vapors |
| 22, 23 | Graveyard hate; layered protection | Abstergo; section 4 |
| 24 win-turn shield (R24) | 3 or more at MV 2 or less | 5 named |
| 25 | Answers across types | Section 4 |
| 26 to 28 routes | Scored routes; no shared failure point | Table in section 1 |
| 29 to 31 threat, archenemy, politics | Deterrents; do not draw the table early | Three always-on deterrents; Drannith left out for this reason |
| 32 wipe recovery (R32) | 4 or more rebuild pieces | 8 |
| 33 mulligan (R33) | Checklist, 85 % keeps | 91 % (50,000 hands), 19 of 20 |
| 34 Game Changers (R34) | Fill the slots by marginal wins | 0 of 3 with the reason per owned card (section 4) |
| 35, 36 efficiency, power cards | Cheapest card that does the job; R36 list | 28 cards at MV 2 or less; R36 in section 4 |
| 37 combos | Legal ones welcome | None in the list; Slasher + Ezio is a kill line, not a loop |
| 38, 39 tests, gauntlet | Hands, goldfish, disrupted, five opponents | Section 5 |
| 40, 41 cut log, real games first | Function-based cuts; the owner's games outrank a score | Section 8; six of his ten cards back; Salt named only as a risk |
| **Mana study, notes/02 and notes/13** | Karsten: 42 lands minus rocks and cheap cards, no rocks for a 2-mana commander, sources per pip, gold +1, partial weights; Command Zone 38; Bracket 3 median 36; no Commander number for four or five colors | 36 lands by the formula (36.5); rocks kept for the payment only, said so; weighted sources per color; the missing five-color target was computed by simulation instead |
| notes/01 foundations | Templates bend; one plan | Profile by fuel, not template |
| notes/03 card flow | Draw floor 10; cantrips and recursion are not draw; tutors for the finisher | 10 by tag, 9 weighted, said; the tutor fetches Ramses |
| notes/04 interaction | Two-for-one answers in pods; neutralize commanders; protection layers | Royal Assassin, the Saga, Etrata, Combustion Man; exile answers; six layers |
| notes/05 and notes/12 multiplayer and combat | Single-target kills are backups; menace fails against tokens; defense for attackers; do not become the target | Ramses and three team-wide sources; evasion counted without menace; defense 6; no lock piece |
| notes/06 combat archetypes | Haste, evasion ranking, wipe recovery | Haste 4; unblockable and flying first; Hakoda and recursion |
| notes/07, 10 engines | Not this archetype | Only the timed-ramp rule used |
| notes/08, 09 evaluation and EDHREC | Fit over popularity; averages are behaviour | Combustion Man (16 % of lists) and Eivor (20 %) in on fit; Lydia (62 %) out on function |
| notes/11 community | Engines without enablers rot; griefer cards unite the table | Dead-clause counts; Drannith out |
| **Primers** (`commanders/ezio-auditore-da-firenze*.md`) | Ramses as line 1; setters; Bracket 4 lists run 33 lands, about 10 protection, Royal Assassin 55 %, Lantern 61 %; traps: the kill alone, menace, conditional removal, slow Saga, colorless lands | Ramses central; Slasher as setter; Royal Assassin and Lantern in; no conditional removal; one colorless land less. Against the primer: the Saga is in, on the owner's games and Draftsim's own reading |
| **Owner's lessons L1 to L10** | One plan; ratios by strategy; attackers connect, live, hurry and defend; proven cards stay; no dead clauses; two boards; Salt is not the measure; guide says how to use | Gate PASS; section 3; haste 4, protection 8, defense 6; Eagle Vision, Coastal Piracy, Propaganda in; 3.3; section 5; section 2 |
| **Play reviews 2026-10-26** | He lost with Salt 7.7 to mini-combos, no haste, chump boards, an open board; cast Assassins after combat; Headquarters cannot pay the kill | No package; the misplay rules are in section 2 and 5 |
| **Gate review, section (f)** | Declare short functions; name dead clauses; both boards; one noncombat route; bad-when-drawn honest | team_evasion and team_finishers reported at their real numbers; 12 cards marked bad early or late |
| **Final review 2026-11-08** | Ramses access is thin; Hookblade and Feed the Swarm weakest; Etrata is not a closer | Access stated at 37 %; both cards replaced as it proposed (Mortify); Etrata tagged engine and removal |
| **Iteration-1 lists** (`decks/measured/`, round 3 to 5) | Learn, not copy: Deadeye, Dualcaster, Intruder Alarm, Winter Soldier, colorless lands lost games; Royal Assassin, Lydia, Revelations, Mortify, Utter End were in them | The combos stay out; four of those five return on their own function |
| **Owner's card review** | A verdict per card | Section 6 |
| **Web, read 2026-11-15** | Priors and rulings | EDHREC JSON: `https://json.edhrec.com/pages/commanders/ezio-auditore-da-firenze.json`, the same path with `/upgraded.json`, `/optimized.json`, `/cedh.json`, `/assassins.json`, and `https://json.edhrec.com/pages/average-decks/ezio-auditore-da-firenze/optimized.json` and `/upgraded.json` (Royal Assassin 54 %, Arbaaz 41 %, Evie 38 % of Bracket 4 lists; Drannith 19 % of cEDH lists). Archidekt: `https://archidekt.com/api/decks/v3/?name=Ezio&commanderName=Ezio%20Auditore%20da%20Firenze&orderBy=-viewCount`, decks 10311292 and 8614155 (Bracket 4), 8330777, 11149864 (with a primer: Slasher and Ramses as the kill). Draftsim guide `https://draftsim.com/ezio-auditore-edh-deck/` (plays Arbaaz, Evie, Jacob, Royal Assassin, The Revelations; "the mana base skews heavily black"). Scryfall API: Oracle and rulings of 12 cards, and `https://api.scryfall.com/cards/search?q=is:gamechanger` (53 cards) |
| **Gaps not closed** | | Reddit answered 403; Moxfield's search ignores the query; the EDHREC "Fire and Ice" article page gave no text this time (the 2026-10-31 study read it). No rulings exist for Slasher's ordering with Ezio or for Jacob's copy at the freerunning cost. No source gives five-color source targets: the simulation is a scratch model (greedy land choice, Orchard and Fellwar at 80 %), not a measured result |

### Self-review (skill step 15)
1. One sentence; every plan card sits in a function, a support line or a route (gate: 0 outside).
2. Early functions hold 15 to 22 pieces; team_finishers sits at its minimum of 6 and is said so.
3. Fuel: six connectors at MV 1 to 3 besides Ezio; nine repeatable engines.
4. 36 lands; Ezio on turn 2 in 95.5 %; turns 2 and 3 have plays in every kept hand.
5. Attack engine, protection 8 in six layers, wipe insurance 10.
6. Both boards named; routes: three, disjoint, one noncombat, each with its answer to three opponents.
7. Haste 4, team evasion 3 (WARN, reason), defense 6, toughness 2 or less 30 %.
8. Bracket 3: 0 Game Changers (live list), no land denial, no extra turns, no infinite line.
9. Cuts logged with function, count and replacement; proven role-players all in.

### Open questions for the owner
1. Arbaaz Mir comes from Toph: agreed?
2. Lydia Frye and Deadeye Navigator stay out (section 6): if Lydia is wanted, she replaces Adéwalé.
3. Drannith Magistrate was left out to keep the table off the deck: a call for his pod.
