# Kilo, Apogee Mind: the Spanish deck (Phase 2 build, 2026-11-02)

Opus 5.5 high, `commander-deckbuilding` skill. New deck, 100 % Spanish copies (basics included), built from
`data/model/phase2/pool-spanish-deck.json` (191 entries). Base: the Spanish "Counter Intelligence" precon (Edge of Eternities
Commander, EOC): 63 of the 76 EOC entries in the pool are in the list; the 13 left out are in the cut log. Starting analysis:
`docs/research/phase2-spanish-commander-20261101.md` sections 2.1, 2.6 and 3b; the profile below was re-derived.

Checks run on this list: `python scripts/plan_density.py` gives **PASS** with one WARN (ramp 9 of 10, reason in section 9);
`python scripts/check_phase2_bracket.py decks/phase2/spanish-deck.txt` gives **PASS** (0 Game Changers, no extra turns, no mass
land denial, Commander Spellbook: 0 combos inside the list). The pool was also checked against the LIVE Scryfall
`is:gamechanger` search (53 cards, 2026-11-02): no card of the pool is a Game Changer. Every card has a free Spanish copy
(script check of `printings[].deck == "free"`); the copies wanted by other decks' lists are in section 7.

## 1. Commander reading and rules points to verify

Oracle (Scryfall, 2026-11-02): Kilo, Apogee Mind {U}{R}{W}, Legendary Artifact Creature, Robot Artificer, 3/3, Haste.
"Whenever Kilo becomes tapped, proliferate."

| Question | Answer |
|---|---|
| Rewards | Kilo becoming tapped, by ANY means: attacking (haste, so the turn it lands), station, crew, improvise, convoke, a waterbend cost, any later re-tap after an untap. Each tap is one proliferate. |
| Fuel | Permanents that already carry counters (charge on rocks and engines, +1/+1 on artifact creatures, stun on opposing creatures). Kilo adds nothing to a permanent without a counter, so the 99 must PLACE counters (sources) and then CONVERT them (payoffs). Second fuel: tap events, one per untap cycle unless untappers. |
| Window | Any time it becomes tapped: my combat (attack), my main phase (station, sorcery speed), any time I have priority (crew, waterbend, improvise). Crew and waterbend let Kilo stay untapped as a blocker through the opponents' turns and tap at the last end step. |
| How it wins | It does not. It multiplies counters that become mana (Chalice, Prism, Cornucopia, Autogenerator, Crawler), cards (Insight Engine, Etched Oracle, Automaton, Sensor), threats (Titan Forge, Golem Foundry, Hangarback, Thunderhulk) and two finishers that need no combat: Lux Artillery (10 to EACH opponent per end step at 30 counters) and Darksteel Reactor (wins at 20). |
| How it dies | Any creature or artifact removal (3/3 body), creature and artifact wipes, blockers if it attacks. It never has to attack. |
| Dependence | **Enabler**. The 99 holds 10 more proliferate pieces and the counter sources keep placing counters without Kilo, only slower. Protection floor 3, target 4 (meta.commander_dependence). Recast 5 then 7, with haste, so a recast proliferates at once. |
| Cost | MV 3, three colors: wants a 2-mana rock or three colored lands on turn 3; recast is cheap. |
| Dead clauses | None on Kilo. |

**Rules points to verify**
1. Tapping Kilo to station triggers it, and the proliferate resolves before the station ability. **Confirmed** (Kilo ruling
   2025-07-25). So the first station of a Spacecraft gets no proliferate (it has no counter yet); every later one does.
2. Tapping Kilo for crew, improvise, convoke or a waterbend cost triggers it. Waterbend: **confirmed** that any untapped
   artifact or creature may be tapped to pay, summoning sick or not (Waterbending Lesson rulings 2025-10-02). Crew, improvise:
   follows the general rule that a permanent tapped to pay a cost "becomes tapped"; **no card ruling read**. If wrong, the
   tap-outlet line (section 3) shrinks to station and waterbend; attacking still works.
3. Proliferate may choose any permanent or player with counters, including opponents', or none. **Confirmed** (Kilo rulings).
   Use: never grow opponents' counters except stun counters from Sandbenders-type earthbend lands (mine) or opposing stuns.
4. Lux Artillery counts counters of any kind among MY artifacts and creatures (charge on rocks and Spacecraft, +1/+1,
   Incubator counters); it checks as the end step begins and again on resolution. **Confirmed** (Oracle; ruling 2023-02-04).
   Lands with counters (an earthbended land is a creature, so it counts while animated) and opponents' permanents do not count.
5. Airbending my own Kilo in response to removal: the owner may cast it from exile for {2} (Airbending Lesson ruling
   2025-10-02). Commander tax counts only casts from the command zone (CR 903.8, **recalled, not re-read**). If wrong, the
   save still works but costs the tax.
6. Inspirit at 8+: "other artifacts you control have hexproof and indestructible" covers Kilo (an artifact). **Oracle text.**
7. Cyberdrive Awakener's animated noncreature artifacts may attack that turn if they have been under my control since the
   turn began (summoning-sickness rule CR 302.6, **not checked against a ruling**; Scryfall lists none). If wrong, R2 loses
   the animated rocks and keeps the flying artifact creatures.
8. Proliferate grows only permanents that already have that counter: never cast Everflowing Chalice for 0, never spend the
   last counter of Pentad Prism or Astral Cornucopia unless the mana wins the game. **Oracle text of proliferate.**
9. Lux Artillery gives artifact creature spells sunburst: Kilo recast from the command zone with three colors enters with
   three +1/+1 counters (and Ripples can then phase it out). **Oracle text.**

## 2. Plan and backup

- **Plan.** Kilo becomes tapped every turn (a haste attack, or at home by station, crew, waterbend and improvise) and
  proliferates the counters that about 24 rocks, engines and artifact creatures place; those counters become mana, cards and
  threats, and the deck closes WITHOUT combat through Lux Artillery (10 to each opponent every end step at 30 counters) or
  Darksteel Reactor (20 charge counters), with Reckless Fireweaver pinging each opponent on every artifact entry.
- **Backup.** The same countered artifact board attacks: Cyberdrive Awakener (every noncreature artifact a 4/4 flyer this
  turn, every artifact creature flying), Depthshaker Titan (trample, haste, melee), Titan Forge 9/9s and Thunderhulk Gnomes.
  It reuses the plan's pieces; no separate package.
- **Archetype.** Hybrid: `plus_one_counters` primary (Kilo's proliferate cue; counted for all counter kinds), `artifacts`
  secondary with role `plan`, because every counter lives on an artifact and the deck's mechanics read the artifact count
  (metalcraft, improvise, affinity, Surge Conductor, Inspirit's protection, Cyberdrive). 15 of the 19 artifact payoffs are
  also pieces of a primary function (rule: at least half).

## 3. Profile table

Odds are "at least one by 12 cards seen" (turn 5) for early, "by 20 cards" (turn 13) for late, without Kilo unless said
(consistency report). Weighted counts follow `meta.weights` (one-shot in a support line 0.5, conditional 0.5).

| Function | Tier | Min | Target | Actual | Reason |
|---|---|---|---|---|---|
| counter_sources | gate, early | 12 | 18 | **24** (97 %) | Kilo only multiplies, so the 99 must place counters; repeatable sources first (Coretapper, Steel Overseer, Insight Engine, Inspirit, Uthros, Crawler, Autogenerator, Lux Cannon, Titan Forge, Golem Foundry, Sensor, Seedshark, Kappa, Hangarback, Reactor), then enter-with-counters pieces. Above target on purpose: every source is also a rock, draw engine, removal or body, so none is a one-job card. Kilo is NOT a source. |
| counter_payoffs | gate, late | 6 | 8 | **16** (98 %) | Each payoff grows with proliferate (mana rocks, draw engines, token makers, removal, finishers); most are also sources. |
| counter_doublers (proliferate) | support promoted to gate, early | 10 (class) | 12 | **11** with Kilo, 10 without (74 %) | Promoted because the plan's growth is proliferate; Kilo guarantees it every turn it lives. Weighted WITHOUT Kilo: repeatable Surge Conductor, Peacemaker, Tekuthal (doubles), Karn's Bastion, Thrummingbird, North Pole Patrol (needs Kilo) = 6 at full weight minus Patrol, one-shots Gambit, Augury, Ripples, Skate at 0.5 = 2, total about 7 = the profile's support target 7. |
| kilo_tap_outlets | custom, late | 6 | 8 | **10** with Kilo, 9 without (88 %) | [J] Lets Kilo trigger without attacking into big blockers, at instant speed, and twice a round with North Pole Patrol. Late because early boards are small and Kilo's haste attack works by itself. Weighted: repeatable Inspirit, Uthros, Brute Suit, Ovalchase Dragster, North Pole Patrol = 5, one-shots Waterbending Lesson, Kappa, Universal Surveillance, Organic Extinction = 2, total 7 plus Kilo's own attack. |
| artifact_density | gate, early | 20 | 25 | **43** with Kilo (36 artifact spells + 6 artifact lands) | Metalcraft (Dispatch) from turn 3, improvise and affinity costs, Inspirit protection, Cyberdrive animation. |
| artifact_payoffs | gate, early | 10 | 12 | **19** (93 %) | Surge Conductor, Fireweaver, Golem Foundry, Uthros, Jhoira, Kappa, Cyberdrive, Thought Monitor, 2 cost reducers, Emry, Inspirit, Steel Overseer, Depthshaker, Dispatch, Universal Surveillance, Organic Extinction, Lux Artillery, Seedshark. |
| through_wide_board | gate, early | 10 | 12 | **16** (90 %) | Team level 7: Lux Artillery, Reactor, Fireweaver (scales), Cyberdrive, Depthshaker (trample), Organic Extinction, Fumigate; flyers and unblockables 9: Hangarback Thopters, Kappa, Thrummingbird, Tekuthal, Thought Monitor, Inspiring Overseer, Mechanaut, Seedshark, Inspirit at 8+. |
| through_big_creatures | gate, early | 10 | 12 | **16** (90 %) | 8 spot answers (Swords, Dispatch, Chaos Warp, Airbending Lesson, Sandbenders' Storm, Detained, Firebending Lesson kicked, Lux Cannon repeatable), North Pole Patrol taps, the two noncombat finishers, Cyberdrive flying, Kappa unblockable, Titan Forge 9/9s, two wipes. |
| evasion | support | 4 | 6 | 9 | Inside through_wide_board. |
| wipe_insurance | support | 2 | 3 | 7 | Inspirit 8+ (indestructible artifacts), Darksteel Reactor (indestructible), Hangarback (Thopters), Emry, Swan Song, Ripples, Buried Ruin; plus 3 indestructible Bridges, and every noncreature artifact survives creature wipes with its counters. |
| Ramp (timed) | base | 10 | 12 | **9** (WARN) | 6 cast by turn 2 (Sol Ring, Arcane Signet, Chalice, Prism, Sculptor, Mechanaut); 3 at turn 3 to 4 (Cornucopia, Sphere, Solar Array) kept for their second job. Reason in section 9. |
| Draw (nets cards) | base | 10 | 12 | **13** | Insight Engine, Uthros, Sensor, Etched Oracle, Automaton, Gambit, Thirst, Pull, Universal Surveillance, Waterbending Lesson, Thought Monitor, Jhoira, Inspiring Overseer. |
| Removal (spot) | base | 6 | 8 | **8** + Soul-Guide Lantern (graveyard answer, tagged removal) | Answers to opposing commanders: Swords, Chaos Warp (tuck), Detained (pacifism), Dispatch, Lux Cannon. |
| Wipes | base | 2 (hybrid takes the higher) | 2 | **2** | Fumigate, Organic Extinction; both near one-sided here (noncreature artifacts survive; Organic spares artifact creatures; Inspirit 8+ makes Fumigate one-sided). |
| Commander protection | base, enabler | 3 | 4 | **4 tags, about 3.25 weighted** | Swan Song 1 (spells only), Airbending Lesson 1 (exile and recast for {2}), Ripples 0.75 (needs a counter on Kilo: Steel Overseer, Inspirit's +1/+1, Lux sunburst), Inspirit 0.5 (needs 8). Purchase proposal 2 adds Swiftfoot Boots. |
| Graveyard hate | base | 1 | 1 | 1 | Soul-Guide Lantern (scarce, section 7). |
| Lands | band 36 to 37 (overlap of 36-38 and 35-37) | | | **37** | Rule of thumb 31 + 3 colors + MV 3 = 37; average MV 3.16 with only 9 ramp pieces, so the top of the band. |
| Curve | avg MV band 2.6 to 3.1 | | | **3.16** | Slightly above: 4 cards at 7 (Thunderhulk, Depthshaker, Thought Monitor with affinity, Organic Extinction with improvise at 10) cost less in practice; two cost reducers. |
| Creatures | 15 to 28 (artifacts, the stricter band) | | | 25 in the 99 | Plus 2 Vehicles and 2 Spacecraft. |

**Fit check** (mins, each card once): sources 12 + payoffs 0 extra (all payoffs here are also sources or finishers) +
proliferate 10 + artifact payoffs about 4 not already counted + wide/big about 6 not already counted + ramp 10 + draw 6 not
already counted + removal 6 + wipes 2 + protection 2 = about 58, against 62 non-land slots. One plan, no second package.

**Card-flow budget (turns 4 to 8).** Spend: about one card a turn (a source or a payoff). Gain: natural draw 1, plus Insight
Engine (1, 2, 3... per activation, faster with proliferate), Uthros (1 per artifact spell), Jhoira (1 per artifact spell),
Sensor (1 per 2 counters), Oracle and Automaton bursts. With two of these out the hand grows; with none, the instants (Thirst,
Pull, Gambit, Lesson) cover the gap. Holds.

**Counter rate.** Turn 4: 2 to 4 countered permanents, a Kilo trigger adds 2 to 4 counters, sources add 2 to 3. Turn 6: 5 to
7 countered permanents, about 7 to 10 new counters a turn (more with Tekuthal or a second tap via North Pole Patrol or crew).
Lux Artillery's 30 counters arrive around turns 8 to 10 [J, not simulated]; Darksteel Reactor alone needs about 7 turns
after it lands, 3 to 4 with Tekuthal or Deepglow Skate.

**Dead clauses named.** Thrummingbird's proliferate needs combat damage (weak late); Airbending Lesson lets the opponent
recast the permanent for {2} (best on tokens, which cease to exist, or on expensive permanents); Detained by Legionnaires
falls to bounce and sacrifice; Depthshaker's "sacrifice the animated artifacts" clause is used only on spare artifacts;
Golem Foundry's counters come only from artifact spells and proliferate. No vehicle, equipment or partner clause lacks its
cards (2 vehicles, 0 equipment, crewed by Kilo itself).

## 4. The list by function: how to use each card

**Commander.** Kilo, Apogee Mind: cast on turn 3 (turn 2 off Sol Ring); attack with haste only into an empty or small
board; otherwise tap it at home (station Inspirit or Uthros, crew Brute Suit or Ovalchase Dragster at the last opponent's
end step, pay waterbend or improvise with it). Every tap is a proliferate: choose only your permanents (and opposing stuns).

**Ramp (9)**
- Sol Ring: turn 1; makes a turn-2 Kilo possible; later pays Insight Engine, Titan Forge, Karn's Bastion. Never bad.
- Arcane Signet: turn 2; fixes all three colors for Kilo on turn 3.
- Everflowing Chalice: turn 2 with one kick, never for 0; each proliferate adds a counter, so it is +1 colorless mana a turn. Late, kick it two or three times as an artifact entry for Surge Conductor and Fireweaver.
- Pentad Prism: turn 2 with two colors; spend counters for a big turn but keep one so proliferate and Coretapper refill it.
- Astral Cornucopia: X=1 on turn 3 or 4 only after Kilo is down (X=2 on turn 6); grows into a many-mana fountain for Pull from Tomorrow and Universal Surveillance. Bad as a turn-3 play instead of Kilo.
- Commander's Sphere: turn 3 or 4 fixing; sacrifice it for a card in response to artifact removal or when mana no longer matters.
- Solar Array: turn 3 or 4; tap it for the next artifact spell so that spell gets sunburst (more counters on Etched Oracle, Crawler, Hangarback; charge counters on rocks, which Lux Artillery counts).
- Etherium Sculptor: turn 2; 36 artifact spells cost 1 less; later a station or crew body. Weak late (a 1/2).
- Enthusiastic Mechanaut: turn 2; same discount and a 2/2 flyer that chips and blocks flyers.

**Counter engines and sources (17 + finishers below)**
- Coretapper: turn 2; each turn a charge counter on the best target (Prism or Chalice early for mana; Reactor, Titan Forge, Lux Cannon, Sensor later); sacrifice it in response to removal for two counters.
- Steel Overseer: turn 2 or 3; tap it every turn for +1/+1 on every artifact creature, Kilo included (that enables Ripples on Kilo). Keep it home; dies to pings.
- Hangarback Walker: X=1 on turn 2, or large late; pump it with {1},T; proliferate grows it; let it die into flying Thopters (Board 1, Fireweaver pings).
- Insight Engine: turn 3 or 4; activate at an opponent's end step after Kilo grew it on your turn: it draws 2, 4, 6. The main draw engine; protect it.
- Uthros Research Craft: turn 3 or 4; station it with Kilo (proliferate first, then 3 counters) to reach 3+ at once; a card per artifact spell; 12+ is a big flyer.
- Inspirit, Flagship Vessel: turn 4 or 5; station it with Kilo every turn (proliferate, then +3) to 8 in about two turns; each combat put two charge counters on Reactor, Titan Forge or Lux Cannon, or a +1/+1 on Kilo; at 8+ every other artifact, Kilo included, has hexproof and indestructible. The best card of the 99. Bad only before turn 4.
- Long-Range Sensor: turn 3 to 5; Kilo's attack gives a counter and the proliferate another; Coretapper and Inspirit feed it without attacks; Discover 4 at sorcery speed finds Lux Artillery, Reactor, Insight Engine or a removal spell.
- Golem Foundry: a counter per artifact spell plus proliferate; cash three for a 3/3 Golem (station fuel, blocker, Fireweaver ping). The weakest engine; first cut if a purchase arrives.
- Crystalline Crawler: cast with three colors (three counters, six with Lux); tap it every turn for a counter; remove counters for any color in a big turn.
- Empowered Autogenerator: turn 4 or 5 (enters tapped); every tap adds a counter then that much mana; with proliferate it gives 5 to 10 mana by turn 8 for X spells, Titan Forge and Karn's Bastion.
- Etched Oracle: cast with three colors; one proliferate makes it "draw three"; refill and repeat.
- Mindless Automaton: discard extra lands late for counters; remove two to draw; proliferate turns it into a draw engine.
- Patrolling Peacemaker: a 2/2 with counters that proliferates whenever an opponent targets another player or their stuff, which happens every round in a 4-player pod: free proliferates in opponents' turns.
- Kappa Cannoneer: improvise it by tapping Kilo (proliferate) and rocks; ward 4; every artifact entry grows it and makes it unblockable, a clock that Board 2 cannot block.
- Chrome Host Seedshark: turn 3; every noncreature spell (most of the deck) makes an Incubator with X +1/+1 counters (Lux counts them, proliferate grows them; pay {2} to turn one into an artifact creature for Cyberdrive or station). 2/4 flying blocker.
- Lux Cannon (removal): tap each turn for a counter; with Kilo it fires every second turn: destroy any permanent (a Board 2 creature, an opposing commander, an enchantment).

**Proliferate (7 + Karn's Bastion, North Pole Patrol, Patrolling Peacemaker)**
- Surge Conductor: turn 3; every nontoken artifact entering (rocks, artifact lands too) proliferates. Play it before a chain of cheap artifacts.
- Thrummingbird: turn 2 while boards are empty; proliferates when it connects. Bad late.
- Tekuthal, Inquiry Dominus: doubles every proliferate (Kilo's trigger counts twice); a 3/5 flying blocker; remove three counters to give it an indestructible counter before a wipe.
- Tezzeret's Gambit: draw two and proliferate; pay 2 life for {U/P} if blue is short; best when Kilo is off the table or to push the Reactor.
- Experimental Augury: at an opponent's end step: dig three for a finisher and proliferate.
- Ripples of Potential: hold it for removal or a wipe: proliferate, then phase out everything that got a counter (Kilo with a +1/+1, Insight Engine, Lux Artillery, Reactor).
- Deepglow Skate: late; doubles every kind of counter on chosen permanents: Reactor 10 to 20 wins, Lux Artillery's count jumps. Bad early.

**Finishers (win routes)**
- Lux Artillery: cast when about 15 counters are out, or earlier so artifact creature spells (Kilo recast too) get sunburst; at 30 counters it deals 10 to each opponent every end step. Bad early.
- Darksteel Reactor: cast turns 4 to 6; indestructible; feed it with Coretapper, Inspirit and proliferate; 20 wins. Hold Swan Song or Ripples for the exile or bounce aimed at it.
- Reckless Fireweaver: turn 2 or 3; 1 to each opponent per artifact entry (rocks, Golems, Thopters, Gnomes, Incubators); chip damage that makes Lux's 10 lethal a turn earlier.
- Cyberdrive Awakener: cast in the main phase of the kill turn; every noncreature artifact you had since the turn began becomes a 4/4 flyer and attacks with the flying artifact creatures. Bad early.
- Depthshaker Titan: late; animate only spare noncreature artifacts (they are sacrificed) or none; every artifact creature gets trample, haste and melee. Bad early.
- Threefold Thunderhulk: late; Gnomes equal to its power on entering and on each attack (six with Lux); sacrifice spare artifacts to grow it. Bad early.
- Titan Forge: activate {3},T on spare turns; proliferate fills it; three counters make a 9/9 that blocks Board 2 and attacks.

**Card draw (7 + the draw engines above)**
- Thirst for Knowledge: instant; discard one artifact (a spare rock late, or Lux/Reactor for Emry and Buried Ruin).
- Pull from Tomorrow: at an opponent's end step with Autogenerator or Cornucopia mana.
- Universal Surveillance: improvise with Kilo (proliferate), rocks and artifact lands; X of 4 to 6 on turn 6 or later.
- Waterbending Lesson: draw three; pay waterbend {2} by tapping Kilo (proliferate) and an artifact to keep every card.
- Thought Monitor: affinity makes it 2 to 4 mana for a 2/2 flyer and two cards. Bad early.
- Jhoira, Weatherlight Captain: turn 4; every artifact or legendary spell draws; cast it before a chain of cheap artifacts.
- Inspiring Overseer: turn 3; a card and a 2/1 flyer (station fuel, chump blocker against Board 2).

**Removal (8 spot + graveyard)**
- Swords to Plowshares: the cheapest exile for a Board 2 creature or an opposing commander.
- Dispatch: from turn 3 (three artifacts) it exiles for one mana; before that it taps an attacker.
- Chaos Warp: any permanent, commanders included (tuck); the answer to enchantments.
- Airbending Lesson: instant: exile a nonland permanent and draw; or exile your own Kilo in response to removal and recast it for {2} with haste.
- Firebending Lesson: 2 damage to a utility creature early; kicked, 5 damage late.
- Sandbenders' Storm: instant: destroy a creature with power 4 or more (Board 2); or earthbend 3 for a land with counters that proliferate grows and that returns when it dies.
- Detained by Legionnaires: on an opposing commander (it stays on the table, so no recast) or a Board 2 attacker.
- Soul-Guide Lantern: on entering exile a reanimation target; later sacrifice it to exile each opponent's graveyard, or for a card.

**Wipes (2)**
- Fumigate: when behind on board; your noncreature artifacts keep their counters; with Inspirit at 8+ your artifact creatures are indestructible, so it is one-sided. Recast Kilo after.
- Organic Extinction: improvise with Kilo and artifacts (often 4 to 6 mana from hand); kills only nonartifact creatures, so almost all of yours survive. Bad early.

**Protection (1 + Airbending Lesson, Ripples, Inspirit)**
- Swan Song: keep {U} up for the removal or wipe spell aimed at Kilo, Insight Engine, Lux Artillery or the Reactor.

**Utility (5)**
- Emry, Lurker of the Loch: affinity makes it 0 to 1 mana; mill four, then tap each turn to recast an artifact from the graveyard (Lux, Reactor, a rock after removal; Kilo too if you left it there, with no tax).
- Phyrexian Metamorph: copy Lux Artillery (a second 10 to each opponent), Insight Engine, Autogenerator or Surge Conductor, or an opponent's best artifact or creature; pay 2 life if blue is short.
- North Pole Patrol: untap Kilo after its attack or station and tap it again (crew, waterbend) for a second proliferate; its waterbend {3} (tap Kilo to pay) taps an attacker on an opponent's turn or a blocker on yours.
- Brute Suit: crew 1 with Kilo at the last opponent's end step: Kilo blocked all round and still proliferates; a 4/3 vigilance body.
- Ovalchase Dragster: crew 1 with Kilo (proliferate); a 6/1 trample haste attacker when a lane is open; flies with Cyberdrive. Bad against pingers.

**Lands (37)**
- Untapped duals: Adarkar Wastes, Battlefield Forge, Shivan Reef (pain lands, any time); Sulfur Falls, Glacial Fortress, Clifftop Retreat (check lands: play after a basic); Radiant Summit (untapped with two basics); Rugged Prairie, Cascade Bluffs, Skycloud Expanse (filters: turn one colored mana into two).
- Any color: Exotic Orchard (depends on opponents), Spire of Industry (with an artifact, 1 life), The Mycosynth Gardens ({1} for any color; late, copy a rock or Lux Artillery).
- Utility colorless: Karn's Bastion ({4},T proliferate, also on opponents' turns), Buried Ruin (return Lux or Reactor).
- Artifact lands: Ancient Den, Great Furnace, Seat of the Synod (untapped; count for metalcraft, improvise, Surge Conductor); Silverbluff, Razortide, Rustvale Bridge (tapped, indestructible artifacts).
- Mystic Monastery: tapped tri-land; play it on turn 1 or a turn with spare mana.
- Basics: 7 Island, 4 Plains, 4 Mountain (all Spanish).

## 5. Cut log

New deck: no current list and no proven role-player for this commander (lesson L6 names cards of the other decks). The
precon is the starting point; these are the EOC cards in the pool that are NOT in the list, and the main non-precon cards
considered.

| Card | Function it served | Count after the cut (min) | Replacement and reason |
|---|---|---|---|
| Wake the Past (EOC) | wipe insurance (mass artifact return, 7 MV) | wipe_insurance 7 (2) | Emry, Buried Ruin, Inspirit already cover it; a 7-mana sorcery is the 5th card at 7. First card back if artifact wipes show up in the pod. |
| Resourceful Defense (EOC) | wipe insurance; moves counters to the Reactor | 7 (2) | Golem Foundry kept for bodies; Defense does nothing on the turn it lands. Second card back. |
| Moxite Refinery (EOC) | moves counters (to Reactor or Titan Forge), sorcery speed | sources 24 (12) | Narrow; costs {2} plus a tap per use; Coretapper does the feeding. |
| Gavel of the Righteous (EOC) | counter source, equipment | sources 24 (12) | The only equipment would be an orphan clause (L7); Kilo gains little from +X/+X. |
| Alibou, Ancient Witness (EOC) | haste for artifact creatures, single-target damage | through_big 16 (10) | 5 MV, single target; Depthshaker gives haste to the same board. |
| Angel of the Ruins (EOC) | artifact/enchantment removal, 7 MV flyer | removal 8 (6) | Chaos Warp and Lux Cannon answer artifacts and enchantments for less. |
| Cloud Key (EOC) | cost reducer (ramp at turn 3 to 4) | ramp 9 (10, WARN) | Same turn as Sphere and Solar Array with less output; fallback if Commander's Sphere goes to Ezio (section 7). |
| Command Tower (EOC) | land | lands 37 (36) | Both Spanish copies sit in Toph and Ezio (section 7); purchase proposal 4. |
| Temple of Enlightenment, Irrigated Farmland, Lonely Sandbar, Secluded Steppe, Evolving Wilds (EOC) | tapped lands | lands 37 | 4 tapped lands already (Monastery, three Bridges, which are also indestructible artifacts); untapped duals preferred. Temple is the fallback for Glacial Fortress. |
| Chain Reaction | third wipe vs Board 1 | wipes 2 (2) | Kills Kilo and my engines too; Fumigate and Organic Extinction are near one-sided here. |
| Planar Cleansing | wipe | 2 (2) | Destroys my own artifacts: anti-synergy. |
| Tranquilize, Rowdy Snowballers | stun (Kilo extends it) | through_big 16 (10) | Temporary; fallback for Swords (section 7). |
| Divination, Geyser Leaper, Katara, Forecasting Fortune Teller | draw | draw 13 (10) | Weaker than the 13 kept; fallbacks for Thirst, Pull and Insight Engine (section 7). |
| Cat-Owl, Flexible Waterbender, Adrestia, Astral Wingspan | Kilo tap outlets | kilo_tap_outlets 10 (6) | Brute Suit, Dragster and North Pole Patrol do the same job cheaper. |
| Burnished Hart, Chromatic Star, Barrels of Blasting Jelly | mana | ramp 9 (10) | Not turn 1 to 3 ramp (Hart pays off on turn 4+, Star and Barrels only filter). |
| Equipment and Assassin cards (Hookblade, Cobbled Wings, Glider Staff, Headsplitter, Brotherhood Spy...) | evasion, other plans | evasion 9 (4) | A second package with no support in this plan (L1, L7). |

## 6. Loans

None. The loan candidates are English cards of his Standard decks; a 100 % Spanish deck cannot play them. No loan proposals.

## 7. Scarce copies

Cards of this list whose Spanish copies are also wanted by another deck's current list (`decks/phase2/<slug>.txt`, in
progress) or held by it, with fewer copies than decks. Every one has only Spanish copies (no English copy for the bilingual
decks to take). For `scripts/assign_copies.py` and the lead.

| Card | Copies (ES) and where | Also wanted by | Deck where it adds most (reason) | Kilo plays instead if it loses it |
|---|---|---|---|---|
| Insight Engine | 1, free | Azula | **Kilo**: proliferate grows its counters, so each activation draws 2, 4, 6 instead of 1, 2, 3 | Divination |
| Swan Song | 1, free | Azula, Ezio | **Kilo**: the only counterspell a Spanish deck can play (Negate's Spanish copy sits in Azula) and one of its 4 commander-protection pieces; the bilingual decks have English counterspells to choose from | Resourceful Defense (wipe insurance only; commander protection falls to about 2.25 weighted, so Swiftfoot Boots becomes the first purchase) |
| Soul-Guide Lantern | 2: one in Toph, one free | Azula | **Kilo**: its only graveyard answer in the Spanish pool | none in the pool (graveyard hate 0, open question) |
| Swords to Plowshares | 2: one in Toph, one free | Ezio | **Ezio** if he is short of answers to Board 2 (a combat deck must clear blockers); Kilo has 8 spot answers plus Lux Cannon | Tranquilize |
| Thirst for Knowledge | 1, free | Azula | **Kilo**: the artifact-discard clause is free here (36 artifacts), in Azula it usually costs two cards | Geyser Leaper |
| Pull from Tomorrow | 1, free | Azula | **Azula**: instant X draw for the deck that empties its hand fastest (L2); Kilo keeps Universal Surveillance as its X draw | Forecasting Fortune Teller |
| Commander's Sphere | 1, free | Ezio | **Kilo** if Ezio has English rocks (Kilo is short of ramp, 9 of 10); otherwise Ezio | Cloud Key |
| Glacial Fortress | 1, free | Ezio | Either; Kilo has 21 other nonbasics | Temple of Enlightenment |
| Radiant Summit | 1, free | Ezio | Either | Temple of Triumph |
| Spire of Industry | 1, free | Ezio | **Kilo** (always active with 42 artifacts) | Island |
| Battlefield Forge | 1, free | Toph | Either | Stone Quarry |

No conflict: Sol Ring, Arcane Signet, Exotic Orchard, Sulfur Falls, Clifftop Retreat, Rugged Prairie, Shivan Reef, Cascade
Bluffs, Chaos Warp, Sandbenders' Storm (each other deck holds its own copy or takes an English one). Basics: Kilo uses 7 of
11 Spanish Islands, 4 of 14 Plains, 4 of 15 Mountains, none in another deck.

## 8. Purchase proposals (Game of Magic Singles, Spanish copies, cap 5,000 CLP for this deck)

Stock not verified. Price hints come from the browser readings of 2026-10-17 to 2026-10-19 (`data/prices/browser-gameofmagic-*.psv`),
are stale and are not stock evidence. Nothing here is in the list. Ranked by impact:

| Rank | Card (Spanish) | Need | Price hint | Plays instead of |
|---|---|---|---|---|
| 1 | Relic of Legends (fallback: Springleaf Drum) | Closes the ramp WARN (turn 2 rock) AND taps Kilo at instant speed every round for mana: Kilo blocks through the opponents' turns, proliferates at the last end step, untaps and attacks or stations again, two triggers per round with no other card | not read | Golem Foundry |
| 2 | Swiftfoot Boots | Commander protection about 3.25 to 4.25 weighted; hexproof against the spot removal the table holds (about 2.3 by turn 8); equip 1 does not tap Kilo | 3,200 (FIC, NM ES, 2026-10-17) | Inspiring Overseer |
| 3 | Talisman of Conviction (or of Progress or Creativity, whichever is in Spanish stock) | Ramp 9 to 10 at turn 2 | 1,500 (TDC, NM ES, 2026-10-19) | Ovalchase Dragster |
| 4 | Command Tower | Mana fixing; also ends the Spanish Command Tower question (Toph and Ezio keep theirs) | 570 (AFC, NM ES, 2026-10-17) | 1 Plains |

Within 5,000: ranks 1 + 2 if Relic costs 1,800 or less; otherwise 2 + 3 (about 4,700), or 1 + 3 + 4. The lead verifies stock and decides.

## 9. WARN reasons and dead clauses

- **Ramp 9 of 10 (WARN).** The Spanish pool has no tenth turn-1-to-3 rock (Mind Stone's Spanish copy is in Azula; Burnished
  Hart, Cloud Key, Chromatic Star and Barrels are not ramp by the timed test). Mitigation: Kilo costs 3; three of the rocks
  (Chalice, Prism, Cornucopia) gain mana with every proliferate and Coretapper charges them, so from turn 4 they give more
  than one mana each; Crawler and Autogenerator add late mana; two cost reducers cut the 36 artifact spells. Fix: purchase 1
  or 3.
- Commander protection meets the floor by tags (4) but is about 3.25 weighted; purchase 2.
- `counter_doublers` and `kilo_tap_outlets` reach their declared minimums with Kilo; without Kilo they are at 10 and 9 raw,
  about 7 weighted each (section 3).
- Dead clauses: section 3.

## 10. The two reference boards

- **Board 1, eight or more 1/1 chump blockers that can be sacrificed.** Kilo never needs to attack into them: station, crew
  and waterbend keep the proliferate going. Win through: Lux Artillery (10 to each opponent per end step, no combat), Darksteel
  Reactor, Fireweaver chip damage; Cyberdrive Awakener turns the rocks into 4/4 flyers over the goblins; Organic Extinction
  and Fumigate clear them (near one-sided here). Risk: a sacrifice deck often has pingers; Coretapper, Steel Overseer,
  Thrummingbird and Sculptor die to them. Steel Overseer and proliferate grow the +1/+1 creatures, and the important engines
  are noncreature artifacts (Insight Engine, Lux, Reactor, Titan Forge, Autogenerator, Lux Cannon).
- **Board 2, two or more creatures bigger than ours.** Do not attack with Kilo; tap it at home. Answers: 8 spot removal
  plus Lux Cannon every second turn; North Pole Patrol taps one each round; Titan Forge 9/9s and Tekuthal 3/5 block;
  Kappa Cannoneer is unblockable after each artifact entry; the route 1 finishers ignore blockers.
- **One sweeper turn.** A creature wipe leaves every noncreature artifact and its counters (rocks, Insight Engine, Lux,
  Reactor, Titan Forge, Inspirit below 8, Uthros below 12): recast Kilo for 5 with haste and proliferate at once. An artifact
  wipe: Inspirit at 8+ and the Reactor and Bridges are indestructible; Swan Song counters a sorcery wipe; Ripples phases out
  the countered permanents; Emry and Buried Ruin rebuild.
- **Toughness.** Closers are big (Cyberdrive 4/4 and 4/4 rocks, Depthshaker 5/5, Titan 9/9s, Thunderhulk); 12 of the 25
  creatures have toughness 2 or less (counting the counters they enter with), all engines kept at home, covered by Steel Overseer, proliferate on +1/+1 counters and
  Inspirit's indestructibility.

## 11. Mana

- **Colored sources (lands, then partial).** Blue 17 lands + Orchard, Spire, Gardens + Signet, Prism = about 20.5; White 15
  + same = about 18.5; Red 15 + same = about 18.5. Kilo ({U}{R}{W} on turn 3, a gold card) needs about 17 per color at 37
  lands (Karsten 2C row 18 + 1 for gold, scaled 37/41): met for all three. Tekuthal ({2}{U}{U}) wants about 23 blue on
  curve (short, cast it a turn later); Fumigate and Organic Extinction (WW) are late plays.
- **Tapped lands:** 4 always (Mystic Monastery, three Bridges); 3 check lands and Radiant Summit usually untapped from turn 2.
- **Curve (non-land 62):** MV 0: 3 (X cards), 1: 6, 2: 12, 3: 19, 4: 14, 5: 2, 6: 2, 7+: 4. Average 3.16. Plays on turn 2:
  12 two-drops plus Chalice and Hangarback; turn 3: Kilo first.
- **Keepable hand:** 37 lands give 2 to 4 lands in 7 about 75 % per look, about 93 % with the free first mulligan
  (`probability.md` C). A 2-mana rock by turn 2: 6 pieces, 48 % by 10 cards.

## 12. Open questions for the owner

1. Scarce copies (section 7): Insight Engine, Swan Song and Soul-Guide Lantern matter most to Kilo; Pull from Tomorrow and
   Swords to Plowshares can go to Azula and Ezio. Do you agree?
2. Purchases (section 8): Relic of Legends (or Springleaf Drum) and Swiftfoot Boots first? The lead checks live stock.
3. If Soul-Guide Lantern goes to Azula, the Spanish deck has no graveyard answer: accept that, or buy a Spanish one?
4. A late three-card infinite (Kilo plus an untap effect such as Freed from the Real) is allowed by Bracket 3 but is not in the
   pool and not proposed; the deck wins through its organic routes. Do you want it on a future purchase list?
