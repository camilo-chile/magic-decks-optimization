# Kilo, Apogee Mind: the Spanish deck (final rebuild, step 7.7, 2026-11-09)

Opus 5.5 high, champion build procedure (`docs/research/commander-deckbuilding/champion-addendum-20261108.md` section 3),
rebuilt FROM SCRATCH under `docs/proposals/final-rebuild-brief-20261108.md`. 100 % Spanish copies (basics included), pool
`data/model/phase2/pool-spanish-deck.json`, priority 4: Ezio, Azula and Toph are final and keep their copies (section 8).
The previous version (step 6, Salt 4.6 after purchases) stays in version control.

**Fix round (2026-11-09, review `decks/reports/final-review-spanish-deck-20261108.md`, verdict FIX):** Brute Suit ->
Strionic Resonator, Katara -> Lithoform Engine, Fumigate -> Starfall Invocation (all owned Spanish, played by no final
deck); notes corrected (one untapper: Kilo taps at most twice a round; Cyberdrive paid from lands; the Excavation loop needs
Surge Conductor as its fourth piece); Prologue kept as a to-read buy with the plan change written (section 6); Command
Tower bought Spanish for Kilo directly; checklist items 18, 21, 31, 40 answered (section 5).

**Checks (2026-11-09, after the fix round):**
- `python scripts/check_phase2_bracket.py decks/phase2/spanish-deck.txt`: **PASS**, floor 1, 0 Game Changers, no extra turns,
  no mass land denial, no reversible card; Spellbook: 1 variant inside the list, 0 flagged.
- `scripts/plan_density.py` (run on this plan only, `run_plan`): **PASS**, 0 failures, 1 WARN (section 3, reason given).
- 100 cards (1 + 99), all Spanish copies; 37 lands, 62 nonland, average MV 2.89.

## 0. Key findings of the rebuild

1. **The step-6 "combo" does not work in Kilo's colors.** Commander Spellbook's Crawler + Lux Artillery + Meticulous
   Excavation line (variant 1034-1350-2060, the combo Salt credited at 4.6) needs Crystalline Crawler cast with FOUR colors
   (8 counters for a {2}{W} + {4} loop). Kilo's identity is three colors, and mana outside it becomes colorless, so Crawler
   enters with 6 counters and the loop loses one mana per turn. It works only with **Surge Conductor** on the battlefield
   (its proliferate on Crawler's entry makes 7) and gains a mana with Tekuthal. The line is kept as a four-card late loop,
   described honestly.
2. **No infinite-proliferate line is buyable in Spanish under 3,000.** Freed from the Real (no Spanish copy in the stores),
   Pemmin's Aura (7.3 USD), Paradise Mantle (8.3 USD) and Aura of Dominion (no stock) are out. I found a cheaper Spellbook
   line, **Kilo + Sinking Feeling + Relic of Legends** (variant 1491-4549-6702; Kilo needs one +1/+1 counter, which Inspirit,
   Steel Overseer or Lux Artillery give), with Sinking Feeling at 0.20 USD. Live read: Game of Magic lists its only printing
   (Shadowmoor) sold out, Rivendel has none, and scry.cl shows no offer in any Chilean store. So it is NOT in the list; it is
   the first card to add the day a Spanish copy appears (section 6).
3. **The fair engine gets a fast table-wide finisher**: Prologue to Phyresis puts one poison counter on each opponent, and
   this deck proliferates 3 to 6 times a turn cycle, so all three opponents die to poison together.
4. **Budget falls from 22,300 to about 15,600 all-in**, with no token to buy: Generous Gift (2,100 + a 4,300 Elephant token),
   Muddle the Mixture (3,100, over the 3,000 line), Swiftfoot Boots, Battlefield Forge and Prophetic Prism are dropped.

## 1. Profile

**Commander reading.** Kilo {U}{R}{W}, 3/3 legendary artifact creature, haste: "Whenever Kilo becomes tapped, proliferate."
- Rewards: Kilo becoming tapped by ANY means (attack, crew, station, waterbend, improvise, Relic of Legends' "tap an untapped
  legendary creature"). Fuel: permanents (and players) that already carry counters. Window: any time Kilo can be tapped,
  including opponents' end steps.
- How it wins: it does not; it multiplies counters. Dependence: **enabler** (the 99 has 11 other proliferate sources and
  three finishers that work without him, at about half speed). MV 3 with haste: cheap to recast (5, 7).
- Dead clauses: none. Rules points (rulings checked in the step-6 notes, unchanged): tapping for station or crew triggers it
  (Kilo ruling 2025-07-25); waterbend may tap summoning-sick artifacts and creatures (Waterbending Lesson ruling); proliferate
  may choose players (poison) and opposing permanents (stun counters), never forced. New point: Relic of Legends' second
  ability taps Kilo as a cost, so it "becomes tapped" (Spellbook 1491-4549-6702 uses exactly this; no card ruling read).

**Plan (one sentence).** Kilo is tapped once or twice per round (Relic, waterbend, North Pole Patrol's untap: his only
untapper), Strionic Resonator and Lithoform Engine copy his trigger, and he proliferates the counters that about 20
rocks, engines and creatures place; Surge Conductor, Flux Channeler, Tekuthal and eight proliferate spells multiply the same
counters into mana, cards and threats, and the first noncombat finisher reached closes against the whole table.

**Backup.** The same countered artifact board attacks: Cyberdrive Awakener (every noncreature artifact a 4/4, artifact
creatures fly) and Titan Forge 9/9s, after Lux Artillery and Fireweaver have softened the table.

**Speed (goldfish, section 5).** Kilo on turn 3 in most games with 3+ lands (the step-6 mana simulation gave 86 % for a similar base with the same
buys; not re-run for this base, which trades three tapped Bridges for basics); engine online turns 4 to 5; first
lethal threat to the table turns 7 to 9 (Prologue plus proliferate, Reactor funnel); a real kill turns 8 to 11.

**Win routes, scored (R26) and failure points (R28).**

| Route | Closers (cards) | Mana on the win turn | Access | Alone? | Fails to |
|---|---|---|---|---|---|
| Darksteel Reactor funnel (alternate win) | Reactor + Resourceful Defense / Moxite Refinery / Deepglow Skate | 0 to 5 | Reactor 1 card + Long-Range Sensor (discover 4), Emry, Buried Ruin | Reactor grows alone (upkeep) | exile or bounce of the Reactor (indestructible to destroy), artifact counterspell |
| Poison (alternate) | Prologue to Phyresis | 2 (instant), then proliferates | 1 card + Experimental Augury, Long-Range Sensor | Prologue cantrips | a counterspell on Prologue; nothing after it resolves (counters on players) |
| Lux Artillery burn | Lux Artillery, Reckless Fireweaver, Meticulous Excavation (loop) | 0 (end step) | Lux 1 card + Metamorph copy, Sensor, Emry | Lux counts every counter | artifact removal, a long clock (10 per turn) |
| Artifact alpha strike (combat) | Cyberdrive Awakener, Titan Forge | 6 | 2 cards | Titan Forge makes 9/9 blockers | a wipe in response, fog, flyers |

No failure point is shared by all routes: commander dead (Reactor upkeep, Lux and poison through Surge Conductor, Flux and
spells still work); a wipe (Reactor indestructible, poison counters stay on players, noncreature artifacts survive creature
wipes); a counterspell (four separate closers); graveyard exile (no route uses the graveyard; Emry and Buried Ruin are
extras); artifact removal (poison is an instant on players); enchantment removal (only Resourceful Defense). At least one
route works with Kilo dead (all three noncombat ones).

**How it beats three opponents.** Every closer hits the table at once: 20 charge counters win the game, poison grows on
all three opponents with each proliferate, Lux deals 10 to each opponent. No single-target kill.

**What it fears.** Artifact wipes (Vandalblast, Bane of Progress): engines and mana go together. Answers: Negate,
Counterspell, Ripples of Potential (phase out the countered permanents), Inspirit at 8+ (indestructible artifacts), the
Reactor (indestructible) and poison already on players. Fast combo that wins on turns 5 to 6: section 4. Graveyard decks:
one Soul-Guide Lantern.

## 2. The puzzle: each card's role, how to use it, and its main synergies

**Mana (11).** Lands + lasting ramp = 37 + 9 = 46 (R8), lands 80 %.
- Sol Ring: turn 1; Kilo on turn 2. Never bad.
- Arcane Signet: turn 2; fixes all three colors for Kilo.
- Talisman of Conviction (buy): turn 2 R/W rock; pairs with the blue-heavy lands.
- Everflowing Chalice: kick once on turn 2; every proliferate adds a mana a turn; Coretapper target. Never cast for 0.
- Pentad Prism: turn 2 with two colors; spend counters on a big turn, keep one so proliferate refills it.
- Relic of Legends (buy): turn 3 to 4 rock; at an opponent's end step tap Kilo (or Tekuthal, Jhoira, Emry) for mana:
  an extra proliferate each round at instant speed while Kilo stayed home as a blocker. With North Pole Patrol: two.
- Commander's Sphere: turn 3 to 4 fixer; sacrifice it for a card in response to artifact removal.
- Astral Cornucopia: X=1 on turn 4 after Kilo, X=2 later; grows one mana per proliferate. Bad early.
- Crystalline Crawler: cast with three colors (six counters with Lux); taps for a counter every turn; burst mana; the loop
  piece with Excavation.
- Barrels of Blasting Jelly: turn 1 fixer ({1}: any color once a turn); late {5}: 5 damage to a creature.
- Chromatic Star: turn 1 fixer that replaces itself; a cheap artifact entry for Surge Conductor, Fireweaver, Jhoira, Uthros.

**Counter engines (12).**
- Inspirit, Flagship Vessel: turn 4; station it with a spare creature (or Kilo: proliferate first); each combat +1/+1 on Kilo
  or two charge counters on the Reactor or Lux Cannon; at 8+ every other artifact, Kilo included, is hexproof and
  indestructible. Trophy Mage target.
- Uthros Research Craft: station to 3+; a card per artifact spell. Trophy Mage target.
- Insight Engine: activate at an opponent's end step after proliferates: draws 2, 4, 6. Trophy Mage target.
- Coretapper: a charge counter each turn on Chalice/Prism early, Reactor/Lux Cannon/Sensor later; sacrifice in response to
  removal for two. Tribute Mage target.
- Steel Overseer: +1/+1 on every artifact creature each turn (Kilo, Crawler, Oracle, Peacemaker). Tribute Mage target.
- Surge Conductor: every nontoken artifact entry proliferates (rocks, artifact lands, Star, Barrels): cast it before a chain
  of cheap artifacts; the piece that makes the Excavation loop work.
- Tekuthal, Inquiry Dominus: doubles every proliferate (poison +2 per Kilo tap); a 3/5 flying blocker; indestructible counter
  before a wipe.
- Flux Channeler (buy, to read): every noncreature spell proliferates (about 40 of them); with Prologue each rock is a
  poison counter on every opponent.
- Long-Range Sensor: attacks or Coretapper/Inspirit charge it; discover 4 at sorcery speed: the extra access to Reactor,
  Lux and Prologue.
- Etched Oracle: three counters (six with Lux); proliferate refills it to draw three again.
- Patrolling Peacemaker: proliferates whenever an opponent targets another player's things: several times a round in a pod.
- Chrome Host Seedshark: every noncreature spell makes an Incubator with that many counters (Lux counts them; transform for
  {2} into a body that crews or stations). 2/4 flying blocker.

**Kilo tap and untap outlets, and trigger copiers (3 + Relic, station, improvise).**
- North Pole Patrol: untap Kilo after his first tap, then tap him again (Relic, crew, waterbend): a second proliferate; or
  waterbend {3} (tap Kilo to pay) to tap an attacker on an opponent's turn.
- Strionic Resonator (owned, fix round): {2},T: copy Kilo's proliferate at instant speed (a third proliferate per round),
  Lux Artillery's end-step trigger (20 to each opponent), Deepglow Skate's trigger (the Reactor x4), Surge Conductor, the
  Reactor's upkeep, Jhoira or Uthros draws. Tribute Mage target.
- Lithoform Engine (owned, fix round): {2},T copies Kilo's or Lux's trigger; {3},T copies Prologue (one more poison each and a
  card), Thirst or Universal Surveillance; {4},T copies the Reactor, Lux or Deepglow as they are cast. Trophy Mage cannot
  find it (MV 4).

**Finishers and funnels (9).**
- Darksteel Reactor: cast turns 4 to 6; fed by upkeep, every proliferate, Coretapper and Inspirit; 20 wins. Hold Negate,
  Counterspell or Ripples for the exile or bounce aimed at it.
- Lux Artillery: cast when about 15 counters are out, or before Kilo's recast (Kilo enters with three +1/+1 counters);
  30 counters: 10 to each opponent per end step.
- Prologue to Phyresis (buy, to read): cast at an opponent's end step once Kilo or Surge Conductor is out, ideally with
  Tekuthal: 1 poison each, then 2 to 4 more per turn cycle. Cantrip; never hold it past turn 6.
- Reckless Fireweaver: 1 to each opponent per artifact entry; with the Excavation loop, infinite.
- Cyberdrive Awakener: the kill turn of the backup; pay its 6 mana from LANDS (rocks tapped for mana cannot attack), in the
  main phase with 8+ untapped noncreature artifacts.
- Deepglow Skate: double the Reactor (10 to 20 wins), Lux's count, Insight Engine and the rocks. Bad early.
- Titan Forge: {3},T on spare turns; three counters make a 9/9 that blocks Board 2 and attacks.
- Resourceful Defense: {4}{W} at an opponent's end step moves Inspirit's or Crawler's counters onto the Reactor; when removal
  hits a countered permanent, its counters move to the Reactor.
- Moxite Refinery: sorcery-speed funnel ({2}, X counters into X charge counters on the Reactor or +1/+1 on Kilo).
- Meticulous Excavation (buy): with Lux + Crawler + Surge Conductor, the infinite entry/proliferate loop; otherwise return a
  Trophy or Tribute Mage, Thought Monitor or Deepglow Skate to reuse it, or save Kilo from removal on my turn (no tax).

**Proliferate and card flow (11).**
- Tezzeret's Gambit: draw two and proliferate; pay 2 life for the {U/P} when short.
- Experimental Augury: at an opponent's end step dig three for a finisher, proliferate.
- Contentious Plan (buy): two mana, proliferate and draw.
- Volt Charge (buy): instant 3 damage and proliferate (counted with removal).
- Thirst for Knowledge: instant draw three; discard a spare artifact (or Lux/Reactor for Emry and Buried Ruin).
- Waterbending Lesson: draw three; waterbend {2} by tapping Kilo (proliferate) and an artifact.
- Universal Surveillance: improvise with Kilo (proliferate) and rocks; X of 4 to 6 late.
- Jhoira, Weatherlight Captain: a card per artifact or legendary spell; cast before a chain of cheap artifacts.
- Thought Monitor: affinity makes it 1 to 3 mana: two cards and a 2/2 flyer.
- Trophy Mage (buy, to read): finds Relic of Legends (extra Kilo tap), Insight Engine, Surge Conductor, Inspirit or Uthros.
- Tribute Mage (buy, to read): finds Pentad Prism or Talisman early, Steel Overseer, Coretapper or Moxite Refinery later.

**Interaction (14).**
- Swords to Plowshares (Ezio's Spanish copy): any big creature or commander, instant, 1 mana.
- Dispatch: metalcraft from turn 3: exile for {W}.
- Fateful Absence: instant creature or planeswalker removal (its Clue goes to the opponent: owned token).
- Chaos Warp: anything, commanders included (tuck); the answer to enchantments.
- Airbending Lesson: instant exile of a nonland permanent and a card; or save my own Kilo and recast him for {2}.
- Volt Charge: see above.
- Tranquilize: three stun counters that Kilo keeps topping up; for a commander or the biggest blocker.
- Lux Cannon: tap each turn; with proliferate it destroys any permanent every second turn.
- Counterspell (buy, to read) and Negate (buy): keep {U}{U} or {1}{U} up on the turn I go for the win or against a wipe.
- Organic Extinction: improvise with Kilo and artifacts; kills only nonartifact creatures (almost one-sided).
- Starfall Invocation (owned, fix round; replaces Fumigate): when behind on board; promise the gift and get back my best
  destroyed creature (Surge Conductor, Tekuthal or Steel Overseer); noncreature artifacts and their counters survive; recast
  Kilo for 5 with haste.
- Ripples of Potential: in response to a wipe or removal: proliferate, then phase out everything that got a counter.
- Soul-Guide Lantern: the graveyard answer; otherwise a card.

**Recursion and copy (2).** Emry (recast Lux, Reactor, Relic or Kilo from the graveyard; affinity makes it 0 to 1 mana);
Phyrexian Metamorph (a second Lux Artillery, Insight Engine or Surge Conductor, or the opponent's best artifact).

**Lands (37).** Command Tower (bought Spanish at PayToWin), untapped duals Adarkar Wastes, Shivan Reef, Sulfur Falls, Glacial
Fortress, Clifftop Retreat, Radiant Summit; filters Rugged Prairie, Cascade Bluffs; Exotic Orchard, Spire of Industry;
artifact lands Seat of the Synod, Ancient Den, Great Furnace (metalcraft, improvise, Surge Conductor); Karn's Bastion
(proliferate sink, also on opponents' turns), Buried Ruin (return the Reactor or Lux), Mystic Monastery (the only
always-tapped land); 9 Island, 6 Plains, 5 Mountain.

**Synergy count (R4).** 47 of 62 nonland cards sit in two or more declared functions or routes, or carry two base tags
(counted from the plan file). **Commander-centric count (R5):** cards nearly blank without Kilo: North Pole
Patrol's untap mode and Relic's second ability: 2 of 62 (limit 12).

## 3. Curve and ratios

| MV | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|---|
| Cards | 2 | 7 | 15 | 23 | 10 | 2 | 1 | 2 |

Average MV 2.89 (Thought Monitor and Organic Extinction cost far less with affinity and improvise). Types: 33 artifacts,
20 creatures, 12 instants, 7 sorceries, 2 enchantments, 37 lands.

| Function | Min | Count | Reason |
|---|---|---|---|
| Lands | band 36 to 38 | 37 | Three colors, MV-3 gold commander, many 3- and 4-drops and mana sinks (Insight Engine, Titan Forge, Strionic, Lithoform, Bastion) |
| Lands + lasting ramp (R8) | 46 | 46 | 9 rocks; Coretapper and proliferate grow Chalice, Prism and Cornucopia |
| Always-tapped lands (R10) | at most 3 | 1 | The three Bridges left; check lands enter untapped with 20 basics |
| counter_sources (gate) | 12 | 21 | Kilo only multiplies, so the 99 must place counters |
| counter_doublers (promoted to gate) | 10 | 15 (14 without Kilo) | The plan grows by proliferate; the commander guarantees one per turn |
| counter_payoffs (gate, late) | 6 | 15 | Rocks, draw engines, finishers |
| kilo_tap_outlets (custom, late) | 6 | 9 | Kilo triggers without attacking into big boards, at instant speed |
| artifact_density / payoffs | 20 / 10 | 34 / 17 | Metalcraft, improvise, affinity, Surge Conductor, Inspirit |
| Through a wide board / big creatures | 10 / 10 | 11 / 15 | Three noncombat closers, flyers, one-sided wipe; ten answers |
| Draw (second tags) | 10 | 16 | Spends one card a turn, gains two to three from turn 5 |
| Spot answers (R19) | 8, 5 at MV<=2, 5 instants | 12; 6 at MV<=2; 8 instants | Swords, Dispatch, Fateful, Tranquilize, Counterspell, Negate at MV<=2 |
| Counterspells (R20) | 2 to 4 (engine deck) | 2 + Ripples | The deck taps out for artifacts; counters protect the win turn |
| Wipes (R21) | 1 to 2 | 2 | Organic Extinction one-sided; Starfall Invocation returns my best creature and leaves noncreature artifacts |
| Commander protection (enabler) | 3 to 4 | 5 | Airbending Lesson, Ripples, Inspirit 8+, Counterspell, Negate |
| Win-turn shield (R24) | 3 at MV<=2 | 3 | Counterspell, Negate, Ripples (plus Airbending at 3) |
| Rebuild pieces (R32) | 4 | 6 | Kilo with haste, Emry, Buried Ruin, Resourceful Defense, Ripples, the indestructible Reactor |
| Tutors (R18) | | 2 + Sensor | Trophy and Tribute Mage find engines; the finishers rely on redundancy (6 closers) and dig |
| Graveyard hate | 1 | 1 | Soul-Guide Lantern |

**WARN reason.** "Poison route rests on a single card": true, and accepted. Prologue costs one card and ends the game
through every other proliferate; it is an instant (cast it at an end step into open mana only after the counter is gone),
the counters stay on players once it resolves, and three other closers do not need it. Access: Experimental Augury, Long-Range
Sensor, Thirst, Waterbending Lesson, Universal Surveillance, Insight Engine. No second poison seeder under 3,000 in Spanish
was found that is not a dead card alone.

## 4. Interaction plan and protection plan

- **Answers kept for**: commanders and engines that beat me (Swords, Chaos Warp, Airbending); combo pieces at instant speed
  (Swords, Dispatch, Fateful, Volt Charge, Chaos Warp, Airbending: six answers castable on an opponent's turn that stop a
  creature combo or lethal attack); artifacts and enchantments (Chaos Warp, Airbending, Lux Cannon; Negate on the spell).
- **Stack**: Counterspell and Negate protect the Reactor turn or stop a wipe; Negate is also the answer to an opposing combo
  spell (Thassa's Oracle lines are creatures: Counterspell).
- **Protection of Kilo (enabler, 3 to 4)**: Airbending Lesson (exile and recast for {2}), Ripples (needs a counter on Kilo:
  Inspirit or Steel Overseer gives one), Inspirit at 8+, the two counters. Kilo is cheap to recast; protect the engines and
  the Reactor first.
- **Win-turn shield (R24)**: keep {U}{U} for Counterspell or {1}{U} for Negate or Ripples on the turn the Reactor reaches
  20, Prologue resolves, or Cyberdrive attacks. Bait with Volt Charge or a draw spell first.
- **Threat posture (R30)**: Kilo stays home and taps at instant speed (Relic, North Pole Patrol's waterbend), so the deck shows little
  until the closer; never cast the Reactor or Lux the turn before you can protect it.

## 5. Mulligan, play pattern and test pass

**Keep checklist (R33).** Keep 2 to 4 lands (3+ when there is no 1- or 2-mana rock) with a play by turn 3 and a plan piece.
Ship 0 to 1 landers, 6+ landers, no play before turn 4, and hands that cannot make all three colors by turn 4. Keep almost
any land-good hand with: Sol Ring, Arcane Signet, Talisman, Pentad Prism, Surge Conductor, Inspirit, Insight Engine.

**20 seeded hands** (scratch script, list above, seeds 1 to 20): 12 keeps on the first seven, 16 with the free mulligan.
20,000-hand sample: 56.1 % keep, **80.8 % with the free mulligan** under the house rule above (it also ships 5-landers); under R33's own ship list (5-landers kept) the reviewer's
recount gives **85.3 %**, on target. House rule: 2-land hands only with a
1-2 mana rock). Under R33's 85 % target; the shortfall is 2-land hands with a fixer (Barrels, Chromatic Star) and a
2-drop, which a pilot keeps in practice. A 38th land or a fourth cheap rock moved it only to 82-83 % in the same test, so the
list stays at 37 lands.

**Goldfish (seeds 101 to 105, 7 + T cards).**
- G1: Kilo turn 3; only Chalice for counters; Waterbending Lesson turn 4; no closer by turn 10 (Deepglow without a target):
  a flood game, kill after turn 10.
- G2: Kilo turn 3 (Barrels fixes white); Seedshark turn 4, Thought Monitor turn 5, Reactor turn 6; Reactor at 20 around
  turn 10, turn 9 with Moxite Refinery.
- G3: Pentad Prism turn 2, Kilo turn 3, Etched Oracle turn 4: card advantage, no closer seen by turn 10 (kill turn 11+).
- G4: no white source until turn 10: Kilo stuck. Prologue turn 4, Tekuthal turn 5, poison grows only through Augury (+2):
  the hand should have been shipped by the color rule (two colors).
- G5: one land: ship.
- Summary: Kilo on turn 3 in 3 of 4 keeps; the plan is online by turns 4 to 5; the first lethal threat comes turns 7 to 9
  when a closer is drawn. Weakness: finisher access (6 closers + dig), not mana.

**Disrupted goldfish (R38).**
- (a) Kilo removed the first time he taps: recast for 5 next turn with haste and tap at once; Surge Conductor, Flux,
  Tekuthal and the spells keep 1 to 3 proliferates a turn meanwhile. One turn lost.
- (b) Creature wipe on turn 6: noncreature artifacts and their counters stay (Reactor, Insight Engine, Lux, rocks); Ripples
  first if held; Kilo back for 5 with haste. Threatens again in one turn. An artifact wipe costs 2 to 3 turns.
- (c) First win attempt countered (the Reactor): Emry or Buried Ruin brings it back, or switch to Prologue or Lux. Two turns.

**Play pattern.** Turns 1 to 5: rock or fixer turn 1 to 2, Kilo turn 3, then an engine a turn (Surge Conductor, Insight
Engine, Inspirit, Coretapper); tap Kilo at home unless the lane is empty. Turns 6 to 9: Prologue at an end step, the Reactor
or Lux, hold two mana for Negate or Counterspell; Kilo taps at most twice a round (Relic and North Pole Patrol's untap); Strionic and Lithoform copy the trigger for a
third and fourth proliferate. Late: Deepglow
Skate on the Reactor (copied by Strionic: x4), Cyberdrive alpha cast from land mana, Excavation loop (needs Surge
Conductor as its fourth piece). Commit what wins in two turns; keep one threat in hand when two
opponents can wipe.

**Gauntlet (R39).**
1. Fast combo (turns 5 to 7): Counterspell, Negate, Swords, Dispatch, Fateful Absence, Volt Charge, Chaos Warp at instant
   speed; Soul-Guide Lantern against graveyard combos. Weak to a turn-4 win through two counters.
2. Stax and taxes: cheap threats (Kilo 3, rocks 1 to 2); Chaos Warp, Airbending and Lux Cannon for the artifact or
   enchantment; poison and the Reactor ignore attack taxes.
3. Go-wide tokens (Board 1): never attack into it; Organic Extinction, Starfall Invocation, Lux, Reactor, poison, flyers.
4. Big creatures (Board 2): eight spot answers plus Lux Cannon, Tranquilize kept by proliferate, North Pole Patrol taps one,
   Tekuthal and Titan Forge block; the noncombat closers ignore them.
5. Control with counters and wipes: instant-speed threats (Prologue, Relic taps, Resourceful Defense, Insight Engine at end
   step), four different closers, rebuild pieces; Negate and Counterspell back up the key turn.

**Final cut pass (10 weakest nonland), redone in the fix round against the FINAL Ezio, Azula and Toph lists (item 40).** The
first pass used the pool's stale `held_by` (2026-11-02) and missed three free Spanish cards no final deck plays. Swaps made:
Brute Suit -> Strionic Resonator, Katara -> Lithoform Engine, Fumigate -> Starfall Invocation. Remaining weakest: Commander's
Sphere, Chromatic Star, Astral Cornucopia, Titan Forge, Meticulous Excavation, Thought Monitor, Deepglow Skate. Best unplayed
candidates and why they lose here: Sinking Feeling (no stock), Swiftfoot Boots (2,100 for hexproof on a cheap commander),
Energy Refractor (300, no mana gain), Kappa Cannoneer (6-mana single-target threat), Hangarback Walker (needs a Thopter token
not owned), Keen-Eyed Raven (kept for the day Sinking Feeling appears), Brute Suit and Katara (now out). No further swap won.

**Politics (item 31).** Fateful Absence's Clue and Starfall's gift card go to the opponent who is NOT the current leader (a
small deal that buys a turn). Patrolling Peacemaker is a visible deterrent: say so when an opponent targets another player.
Chaos Warp, Swords and Tranquilize are offered as table answers to the archenemy's threat before they are spent on mine.
Kilo stays untapped at home as a 3/3 blocker until the end step, so the deck rarely looks like the archenemy before the win
turn; never cast the Reactor or Prologue the turn before the shield (Negate, Counterspell, Ripples) is up.

**Checklist items left from the review.**
- 18 (tutors to the finisher): not fixable within the rules today. No tutor reaching an MV-4 artifact or Prologue is owned in
  Spanish or read under 3,000 (Fabricate 5.76 USD, Whir of Invention 5.43 USD, Muddle 3,100 and MV 2 only, Mystical
  Teachings unread). Mitigation: six closers, Strionic and Lithoform copying the closers, Long-Range Sensor, Augury. The lead's
  browser read of Fabricate and Whir at GoM and PTW (review F9) is the one open path.
- 21 (asymmetric wipes): fixed. Organic Extinction (nonartifact creatures only) and Starfall Invocation (my best creature
  back) replace the symmetric Fumigate.
- 31 (politics): fixed in the guide above (no list change, no cost).
- 40 (cut process): fixed; the cut pass was redone above with the fresh pool.

## 6. BUY

Stores: Game of Magic Singles (GoM), PayToWin (PTW), Rivendel El Concilio (Riv). Spanish only, any condition better than
Damaged, every card under 3,000. Rivendel prices were read live by script on 2026-11-08/09; GoM and PTW prices come from
the 2026-11-08 order reads (`data/prices/browser-*-20261108-order.psv`); "to read" rows have no store reading (GoM and PTW
answered HTTP 429 to scripts on 2026-11-09) and carry a Scryfall USD hint. The lead checks live stock before buying.

| # | Card | Store | Price (CLP) | Lang | Gain | Plays until it arrives |
|---|---|---|---|---|---|---|
| 1 | Negate | Riv | 300 (4 in stock) | ES | Win-turn shield and wipe answer; Azula holds the owned copy | Firebending Lesson |
| 2 | Volt Charge | Riv | 200 (14) | ES | Instant answer + proliferate | Misthios's Fury |
| 3 | Contentious Plan | Riv | 300 (1) | ES | 2-mana proliferate + card | Divination |
| 4 | Meticulous Excavation | Riv | 300 (16) | ES | Lux + Crawler + Surge Conductor loop; ETB reuse; Salt-visible combo | Golem Foundry |
| 5 | Relic of Legends | Riv | 2,500 (3) | ES | Rock + instant Kilo tap: one more proliferate per round | Ovalchase Dragster |
| 6 | Talisman of Conviction | GoM | 1,500 (read 2026-11-08) | ES | Turn-2 rock, Kilo on turn 3 | Etherium Sculptor |
| 7 | Command Tower | PTW | 900 (read 2026-11-08, C17 LP Spanish) | ES | Untapped any-color land; bought Spanish for Kilo directly, Ezio keeps its own copy (review F6) | a 7th Plains |
| 8 | Swords to Plowshares (English, for Ezio; Ezio's Spanish copy comes to Kilo) | GoM | 2,500 (read 2026-11-08) | EN | Best 1-mana instant answer | Detained by Legionnaires |
| 9 | Prologue to Phyresis | PTW or GoM | to read: NO stock evidence (0.52 USD; GoM's only ONE listing 342 CLP was sold out; none at Riv) | ES | The poison route: all three opponents at once | Kappa Cannoneer |
| 10 | Counterspell | GoM or PTW | to read (2.23 USD, about 2,500) | ES | Hard counter for the win turn | Sandbenders' Storm |
| 11 | Flux Channeler | GoM or PTW | to read (2.59 USD, about 2,600; skip if 3,000 or more) | ES | Proliferate on every noncreature spell | Thrummingbird |
| 12 | Tribute Mage | GoM or PTW | to read (1.01 USD, about 1,000) | ES | Tutor: Prism/Talisman early, Overseer/Coretapper/Moxite later | Enthusiastic Mechanaut |
| 13 | Trophy Mage | GoM or PTW | to read (0.57 USD, about 600) | ES | Tutor: Relic, Insight Engine, Surge Conductor, Inspirit | Inspiring Overseer |

Ranked by gain per CLP: 1, 2, 3, 9, 13, 6, 7, 12, 4, 5, 8, 10, 11. Rivendel evidence saved in
`data/prices/rivendel-kilo-20261109.psv` (Contentious Plan has one copy: first line of the Rivendel cart).

**If no Spanish Prologue to Phyresis exists in the three stores:** Kappa Cannoneer keeps the slot, the plan file drops the
"Poison through proliferate" route (three routes remain: Reactor funnel, Lux Artillery burn, artifact alpha strike; the gate
still needs two disjoint ones), the plan sentence loses the poison finisher, Lithoform's {3} mode copies Thirst or Universal
Surveillance instead, and the real-power estimate falls by about 0.2 (no table-wide clock that ignores life totals). The
lead makes this change with the order, not before, so the list plays the card if it is found. Every stand-in is an owned free Spanish copy, so the list
plays today. Thirst for Knowledge is NOT a Kilo buy: Kilo keeps its owned copy and Azula takes the copy bought at Rivendel
(Azula notes, section 8).

**Fix round (2026-11-09):** Strionic Resonator, Lithoform Engine and Starfall Invocation are owned Spanish copies: 0 CLP.
Command Tower is bought Spanish for Kilo directly (review F6), same 900; Ezio needs no Command Tower buy.

**Dropped from the old order (22,300):** Generous Gift 2,100 + Elephant token 4,300 (Volt Charge, Swords, Chaos Warp and
Airbending do the job), Muddle the Mixture 3,100 (over the 3,000 line; it could not reach the MV-3 pieces anyway), Battlefield
Forge 2,600 (Toph keeps the owned Spanish copy; a basic does most of the job), Swiftfoot Boots 2,100, Prophetic Prism 200.

**Watch list (add when a Spanish copy under 3,000 appears):** Sinking Feeling (with Relic of Legends: infinite proliferate,
0.20 USD; cut Commander's Sphere), Pemmin's Aura / Freed from the Real (same line), Walking Ballista, Narset, Parter of
Veils (a Game Changer worth its slot; Spanish only at 13,000).

**Game Changer slots (R34): 0 of 3 used.** No Game Changer is owned in Spanish, and the cheapest ones in Kilo's colors cost
more than 3,000 in Spanish (live Scryfall `is:gamechanger id<=wur`, 33 cards on 2026-11-08: Narset 0.92 USD but Spanish only
at 13,000; Gifts Ungiven, Farewell, Underworld Breach 4 to 5 USD; Drannith 9.85; the rest 15 USD and up). Gain if the cap
allowed: Narset (digs four cards a turn with proliferated loyalty and stops opposing extra draws) first, then Enlightened
Tutor, Teferi's Protection.

**R36 non-GC high-power cards considered:** Swords (in), Counterspell (in), Swan Song (Azula holds the only copy), Mana Drain,
Force of Negation, Fierce-type free spells, Esper Sentinel, Mystic Remora (all over 3,000 in Spanish), Path to Exile (Toph
holds the only copy), Walking Ballista (5.47 USD), Freed from the Real (no Spanish copy), Fellwar Stone and Mind Stone (no
Spanish stock read), Lotus Petal and Mox Amber (price; Mox Amber has only 6 legends).

## 7. Loans and their replacements

None. The loan candidates are English cards of his Standard decks; a 100 % Spanish deck cannot play them. The two English
card bought for Ezio (English Swords) is not a loan: it frees Ezio's Spanish copy and is booked to Kilo.

## 8. Scarce copies

Read against the FINAL Ezio, Azula and Toph lists (2026-11-09), with a dry run of `scripts/assign_copies.py`'s allocation in
the order Ezio, Azula, Toph (nothing written).

| Card | Spanish copies | Held by | Kilo |
|---|---|---|---|
| Swords to Plowshares | 2 | Toph 1, Ezio 1 | Ezio plays a bought English copy (2,500, booked here); Ezio's Spanish copy comes to Kilo |
| Command Tower | 2 (+1 EN) | Azula EN, Toph ES, Ezio ES | Kilo buys its own Spanish copy at PayToWin (900); no card moves |
| Strionic Resonator, Lithoform Engine, Starfall Invocation | 1 ES each | no final deck plays them (the pool's `held_by` of 2026-11-02 is stale) | in Kilo (fix round) |
| Path to Exile | 1 | Toph | **Gives way.** Kilo plays Swords and Fateful Absence instead |
| Arbaaz Mir | 1 | Toph | **Gives way.** Reckless Fireweaver does the per-artifact ping |
| Planar Outburst | 1 | Toph | **Gives way.** Starfall Invocation and Organic Extinction |
| Fateful Absence | 2 | Toph 1 | The second copy is free: in Kilo |
| Battlefield Forge | 1 | Toph (Ezio buys its own) | **Gives way**; a basic instead (no buy) |
| Swan Song, Negate, Mind Stone, Thirst for Knowledge | 1 each | Azula | Swan Song and Mind Stone given way; Negate bought (300); Thirst: Kilo keeps the owned copy, Azula takes the bought one |
| Chaos Warp | 2 | Toph 1 | One free: in Kilo |
| Clifftop Retreat, Rugged Prairie, Exotic Orchard | 3 / 2 / 5 | Ezio, Toph | 1 / 1 / 2 free: in Kilo |
| Sol Ring, Arcane Signet, Everflowing Chalice, Sulfur Falls, Shivan Reef, Cascade Bluffs | 1 each | the other decks play English copies | in Kilo |
| Basics | 11 Island, 14 Plains, 15 Mountain (ES) | the other decks take English basics first | 9 / 6 / 5 in Kilo |

No claim on another deck's copy is made.

## 9. Comparison with the current list and the iteration-1 list

**Against the current list after purchases** (`moxfield/spanish-deck-after-purchases.txt`, Salt 4.6, real power 4.8-5.3):

| Out | Why | In | Why |
|---|---|---|---|
| Swan Song | Azula took the only copy | Counterspell (buy) | Hard counter for the win turn |
| Generous Gift | 2,100 + a 4,300 Elephant token | Fateful Absence (free copy) | 2-mana instant answer, owned |
| Muddle the Mixture | 3,100, over the 3,000 line; cannot reach the MV-3 pieces | Trophy Mage (buy) | Finds Relic, Insight Engine, Surge Conductor, Inspirit |
| Swiftfoot Boots | 2,100 to protect a 3-mana commander | Negate (buy, 300) | Protects the win turn and stops wipes |
| Sandbenders' Storm | 4-mana answer | Prologue to Phyresis (buy) | The poison route |
| Kappa Cannoneer | 6-mana single-target threat | Flux Channeler (buy) | Proliferate on every noncreature spell |
| Empowered Autogenerator | Slow 4-mana rock that enters tapped | Tribute Mage (buy) | Finds Prism, Talisman, Overseer, Coretapper or Moxite |
| Solar Array | 3-mana rock competing with Kilo | Contentious Plan (buy) | 2-mana proliferate and card |
| Enthusiastic Mechanaut | Discount, 2/2 flyer | Strionic Resonator (fix round) | Copies Kilo's, Lux's and Deepglow's triggers |
| Katara (fix round) | {6} waterbend for one card | Lithoform Engine | Copies triggers and spells (Prologue, Lux, Reactor) |
| Fumigate (fix round) | Symmetric; kills my engines | Starfall Invocation | Same wipe; the gift returns my best creature |
| Prophetic Prism | Filter only | Chromatic Star | 1-mana fixer that replaces itself |
| Battlefield Forge, Silverbluff, Razortide, Rustvale Bridge, Skycloud Expanse | Forge stays with Toph; three always-tapped Bridges (R10); a filter | 5 basics (Island +2, Plains +2, Mountain +1) | Always-tapped lands 4 to 1; untapped colors on turns 1 to 3 |

In short: the list keeps the step-6 engine (Inspirit, Uthros, Insight Engine, Surge Conductor, Tekuthal, Reactor, Lux,
funnels) and changes the edges: +2 tutors, +2 proliferate sources (Flux Channeler, Contentious Plan), +1 route (poison), +1 counterspell net (Swan
Song went to Azula; Counterspell and Negate in), 3 fewer always-tapped lands, the Elephant token gone, and the honest note on the
Excavation loop.

**Against iteration 1** (the Counter Intelligence precon, Salt 3.8, real power 4.0-4.5): the precon's 11 tapped lands and 6
cards at MV 7+ are gone (1 and 2 here), Kilo replaces Inspirit as commander (Inspirit is in the 99), the noncombat finishers
replace a combat-only plan, interaction rises from 9 tag-counted to 12 spot answers with 6 at MV 2 or less.

## 10. Real-power estimate

| List | Salt | Real power (1-10) |
|---|---|---|
| Precon (iteration 1) | 3.8 | 4.0-4.5 |
| Current after purchases | 4.6 | 4.8-5.3 |
| **This list (all buys arrive)** | not measured (expect 4.5-5.0: Salt still sees one combo, more interaction, fewer tapped lands) | **5.6-6.1** after the fix round (5.4-5.9 before it), confidence medium-low |
| This list with the to-read buys replaced by their stand-ins | | 5.3-5.7 |

Why higher: a third table-wide finisher that is fast (poison), two more proliferate engines, one more Kilo tap per round
(Relic + North Pole Patrol), cheaper instant interaction and a real win-turn shield, two tutors, cleaner mana. Why not more:
no infinite line is buyable in Spanish, no Game Changer, the finishers have no direct tutor. The biggest upgrade left is
Sinking Feeling (an infinite with Relic of Legends) the day a Spanish copy is in stock.

## 11. Total spend (Kilo's envelope: 18,000; hard cap 20,000)

| Item | CLP |
|---|---|
| Rivendel: Negate 300, Volt Charge 200, Contentious Plan 300, Meticulous Excavation 300, Relic of Legends 2,500 | 3,600 |
| Game of Magic: Talisman of Conviction 1,500; Swords EN for Ezio 2,500 | 4,000 |
| PayToWin: Command Tower (Spanish, for Kilo) 900 | 900 |
| **Confirmed subtotal** | **8,500** |
| To read (hints): Prologue ~400, Trophy Mage ~600, Tribute Mage ~1,000, Counterspell ~2,500, Flux Channeler ~2,600 | ~7,100 |
| Loans | 0 |
| Tokens (Golem 9/9, Incubator, Clue all owned; no Elephant, no Bird) | 0 |
| **All-in** | **about 15,600** (2,400 under the envelope; 22,300 before) |

If a to-read card costs more than its hint, drop in this order: Flux Channeler, Counterspell, Tribute Mage (each has an owned
stand-in). Shipping is counted in the brief's shared line, not here.
