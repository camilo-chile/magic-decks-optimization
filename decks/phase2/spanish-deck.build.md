# Kilo, Apogee Mind: the Spanish deck (Phase 2 build, 2026-11-02, round 3)

Opus 5.5 high, `commander-deckbuilding` skill. New deck, 100 % Spanish copies (basics included), built from
`data/model/phase2/pool-spanish-deck.json` (191 entries). Base: the Spanish "Counter Intelligence" precon (Edge of Eternities
Commander, EOC): 58 of the 76 EOC entries in the pool are in the list; the 18 left out are in the cut log. Starting analysis:
`docs/research/phase2-spanish-commander-20261101.md` sections 2.1, 2.6 and 3b; the profile below was re-derived.

**History.**
- Round 2 (`decks/phase2/owner-decisions.md`, second round): Kilo gave up Swords to Plowshares (to Ezio), Pull from Tomorrow
  (to Azula) and Battlefield Forge (to Toph), replaced by Tranquilize, Katara, Bending Prodigy and Path of Ancestry; Kilo
  keeps Swan Song, Insight Engine, Thirst for Knowledge, Soul-Guide Lantern, Commander's Sphere, Spire of Industry, Glacial
  Fortress, Mystic Monastery and Radiant Summit.
- Round 3 (adversarial review `decks/reports/review-spanish-deck.md`: PASS for the list, FIX for the purchases; owner
  decisions of 2026-11-02): Relic of Legends and Freed from the Real have no Spanish stock at Game of Magic Singles, so their
  line moves to an optional upgrade path (section 8); the purchases are re-ranked with the live stock the reviewer read.
  Mana improved with owned Spanish cards (I-1): The Mycosynth Gardens → a fifth Mountain, Golem Foundry → Barrels of Blasting
  Jelly, Detained by Legionnaires → Chromatic Star. Plan-file fixes M-1 (North Pole Patrol out of `counter_doublers`) and M-3
  (Katara and Astral Cornucopia bad early, Etherium Sculptor bad late). The plan sentence now says that the noncombat route
  rests on two cards with no tutor and that the combat route is co-primary (I-3).
- Salt: the second objective. Owner floor: Kilo must score at least the Salt power of the Spanish Counter Intelligence precon
  + 0.1 (measured in step 3). Every round-3 swap should raise or keep Salt: better mana (Manabase Quality), two cheap artifacts
  in place of a 3-mana engine and an Aura, and the purchases add a rock, an untapped tri-color land and commander protection.

**Checks on this list** (2026-11-02): `python scripts/plan_density.py` **PASS**, 2 WARN (ramp 9 of 10; counter_doublers
reaches 10 only with Kilo; reasons in section 9). `python scripts/check_phase2_bracket.py decks/phase2/spanish-deck.txt`
**PASS** (floor 1, 0 Game Changers, no extra turns, no mass land denial, 0 Spellbook combos inside). The optional upgrade
list (section 8, all purchases plus Freed and Relic) was checked with the same script in the scratchpad: **PASS**, floor 1,
one combo (Kilo + Freed from the Real + Relic of Legends, "Infinite proliferate"). The pool and every purchase candidate were
checked against the LIVE Scryfall `is:gamechanger` search (53 cards, 2026-11-02): none is a Game Changer. Copies: every card
has a free Spanish copy; Barrels of Blasting Jelly (TLA 254) and Chromatic Star (TSR 263) are in no other deck's list and
not in `data/model/phase2/assignment.json`; Kilo uses 5 of 15 Spanish Mountains.

## 1. Commander reading and rules points to verify

Oracle (Scryfall, 2026-11-02): Kilo, Apogee Mind {U}{R}{W}, Legendary Artifact Creature, Robot Artificer, 3/3, Haste.
"Whenever Kilo becomes tapped, proliferate."

| Question | Answer |
|---|---|
| Rewards | Kilo becoming tapped, by ANY means: attacking (haste, so the turn it lands), station, crew, improvise, convoke, a waterbend cost, any later re-tap after an untap. Each tap is one proliferate. |
| Fuel | Permanents that already carry counters (charge on rocks and engines, +1/+1 on artifact creatures, stun on opposing creatures). Kilo adds nothing to a permanent without a counter, so the 99 must PLACE counters (sources) and then CONVERT them (payoffs). Second fuel: tap events, one per untap cycle unless untappers. |
| Window | Any time it becomes tapped: my combat (attack), my main phase (station, sorcery speed), any time I have priority (crew, waterbend, improvise). Crew and waterbend let Kilo stay untapped as a blocker through the opponents' turns and tap at the last end step. |
| How it wins | It does not. It multiplies counters that become mana (Chalice, Prism, Cornucopia, Autogenerator, Crawler), cards (Insight Engine, Etched Oracle, Automaton, Sensor), threats (Titan Forge, Hangarback, Thunderhulk, Kappa) and two finishers that need no combat: Lux Artillery (10 to EACH opponent per end step at 30 counters) and Darksteel Reactor (wins at 20). |
| How it dies | Any creature or artifact removal (3/3 body), creature and artifact wipes, blockers if it attacks. It never has to attack. |
| Dependence | **Enabler, close to engine** (the reviewer reads it between the two). Without Kilo the 99 has 8 cards that proliferate by themselves (4 one-shots), so counter growth drops from "+1 on every countered permanent per tap" to "+1 per source". Cheap recast (5, then 7) with haste softens it. Protection floor 3 (enabler), aimed at 4 to 5: 4 tags now, 5 with Swiftfoot Boots. |
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
   Use: never grow opponents' counters except stun counters (Tranquilize).
4. Lux Artillery counts counters of any kind among MY artifacts and creatures (charge on rocks and Spacecraft, +1/+1,
   Incubator counters); it checks as the end step begins and again on resolution. **Confirmed** (Oracle; ruling 2023-02-04).
5. Airbending my own Kilo in response to removal: the owner may cast it from exile for {2} (Airbending Lesson ruling
   2025-10-02). Commander tax counts only casts from the command zone (CR 903.8, **recalled, not re-read**). If wrong, the
   save still works but costs the tax.
6. Inspirit at 8+: "other artifacts you control have hexproof and indestructible" covers Kilo (an artifact). **Oracle text.**
7. Cyberdrive Awakener's animated noncreature artifacts may attack that turn if they have been under my control since the
   turn began (summoning-sickness rule CR 302.6, **not checked against a ruling**; Scryfall lists none). If wrong, the combat
   route loses the animated rocks and keeps the flying artifact creatures.
8. Proliferate grows only permanents that already have that counter: never cast Everflowing Chalice for 0, never spend the
   last counter of Pentad Prism or Astral Cornucopia unless the mana wins the game. **Oracle text of proliferate.**
9. Lux Artillery gives artifact creature spells sunburst: Kilo recast from the command zone with three colors enters with
   three +1/+1 counters (and Ripples can then phase it out). **Oracle text.**
10. Barrels of Blasting Jelly's "{1}: Add one mana of any color" converts one mana into any color once a turn without losing
    mana, so three lands of two colors plus Barrels cast Kilo. **Oracle text.**
11. Optional path only (section 8): tapping Kilo for the cost of Relic of Legends' second ability makes it "become tapped";
    that ability does not tap Relic, so with Freed from the Real's `{U}: untap` it loops. Commander Spellbook lists Kilo +
    Freed from the Real + Relic of Legends as "Infinite proliferate" (variant 4222-4549-6702). **Oracle text and Spellbook; no
    card ruling read.**

## 2. Plan and backup

- **Plan.** Kilo becomes tapped every turn (a haste attack, or at home by station, crew, waterbend and improvise) and
  proliferates the counters that about 23 rocks, engines and artifact creatures place; those counters become mana, cards and
  threats. The deck closes through whichever route it draws. The noncombat route is Lux Artillery (10 to each opponent every
  end step at 30 counters) or Darksteel Reactor (20 charge counters): **two cards with no tutor in the Spanish pool** (one of
  them by turn 9 in about 30 % of games, about 40 % counting Long-Range Sensor's Discover 4, which can hit either; Emry, Buried
  Ruin and Phyrexian Metamorph recover or copy them once drawn). The combat route below is co-primary and closes most games.
- **Backup, co-primary (same pieces).** The countered artifact board attacks: Cyberdrive Awakener (every noncreature artifact a
  4/4 flyer this turn, every artifact creature flying), Depthshaker Titan (trample, haste, melee), Titan Forge 9/9s and
  Thunderhulk Gnomes; Kappa Cannoneer and Uthros at 12+ add evasive damage. All six closers of both routes: about 66 % to
  see one by turn 9, 75 % by turn 13 (no extra draw; the draw engines raise it).
- **No tutor available.** The Spanish pool has no artifact tutor (checked: no Fabricate, Whir of Invention, Trophy Mage-type
  card). Fabricate (Spanish, 9,800) and Whir of Invention (no stock) exceed or miss this iteration; they are the first
  candidates for the next one (section 8).
- **Archetype.** Hybrid: `plus_one_counters` primary (Kilo's proliferate cue; counted for all counter kinds), `artifacts`
  secondary with role `plan`, because every counter lives on an artifact and the deck reads the artifact count (metalcraft,
  improvise, affinity, Surge Conductor, Inspirit's protection, Cyberdrive).

## 3. Profile table

Odds are "at least one by 12 cards seen" (turn 5) for early, "by 20 cards" (turn 13) for late, without Kilo unless said
(consistency report). Weighted counts follow `meta.weights` (one-shot in a support line 0.5, conditional 0.5).

| Function | Tier | Min | Target | Actual | Reason |
|---|---|---|---|---|---|
| counter_sources | gate, early | 12 | 18 | **23** (97 %) | Kilo only multiplies, so the 99 must place counters; repeatable sources first (Coretapper, Steel Overseer, Insight Engine, Inspirit, Uthros, Crawler, Autogenerator, Lux Cannon, Titan Forge, Sensor, Seedshark, Kappa, Hangarback, Reactor), then enter-with-counters pieces. Every source is also a rock, draw engine, removal or body. Kilo is NOT a source. |
| counter_payoffs | gate, late | 6 | 8 | **15** (97 %) | Each payoff grows with proliferate (mana rocks, draw engines, token makers, removal, finishers). |
| counter_doublers (proliferate) | support promoted to gate, early | 10 (class) | 12 | **10** with Kilo, 9 without (WARN) | Promoted because the plan's growth is proliferate; Kilo guarantees it every turn it lives. North Pole Patrol removed (it untaps Kilo, it does not proliferate: review M-1). Pieces: Kilo, Surge Conductor, Thrummingbird, Patrolling Peacemaker, Karn's Bastion, Tekuthal (doubles), Tezzeret's Gambit, Experimental Augury, Ripples, Deepglow Skate. The pool has no other proliferate card. Weighted without Kilo about 6.5 (4 repeatable, Tekuthal, 4 one-shots at half): above the profile's support min 4, under its target 7. |
| kilo_tap_outlets | custom, late | 6 | 8 | **11** with Kilo, 10 without (91 %) | [J] Lets Kilo trigger without attacking into big blockers, at instant speed, and twice a round with North Pole Patrol. Weighted: repeatable Inspirit, Uthros, Brute Suit, Ovalchase Dragster, North Pole Patrol, Katara = 6, one-shots Waterbending Lesson, Kappa, Universal Surveillance, Organic Extinction = 2, total 8 plus Kilo's own attack. |
| artifact_density | gate, early | 20 | 25 | **44** with Kilo (37 artifact spells + 6 artifact lands) | Metalcraft (Dispatch) from turn 3, improvise and affinity costs, Inspirit protection, Cyberdrive animation, Surge Conductor triggers (Barrels and Chromatic Star are cheap entries). |
| artifact_payoffs | gate, early | 10 | 12 | **18** (92 %) | Surge Conductor, Fireweaver, Uthros, Jhoira, Kappa, Cyberdrive, Thought Monitor, 2 cost reducers, Emry, Inspirit, Steel Overseer, Depthshaker, Dispatch, Universal Surveillance, Organic Extinction, Lux Artillery, Seedshark. |
| through_wide_board | gate, early | 10 | 12 | **16** (90 %) | Team level 7: Lux Artillery, Reactor, Fireweaver (scales), Cyberdrive, Depthshaker (trample), Organic Extinction, Fumigate. Flyers and unblockables 9 (Hangarback Thopters, Kappa, Thrummingbird, Tekuthal, Thought Monitor, Inspiring Overseer, Mechanaut, Seedshark, Inspirit at 8+): they count, but none closes alone (review M-2). |
| through_big_creatures | gate, early | 10 | 12 | **16** (90 %) | Spot answers: Tranquilize (three stun counters Kilo keeps topping up), Dispatch, Chaos Warp, Airbending Lesson, Sandbenders' Storm, Firebending Lesson kicked, Barrels of Blasting Jelly ({5}: 5 damage), Lux Cannon (repeatable); North Pole Patrol taps; the two noncombat finishers, Cyberdrive flying, Kappa unblockable, Titan Forge 9/9s, two wipes. |
| evasion | support | 4 | 6 | 9 | Inside through_wide_board. |
| wipe_insurance | support | 2 | 3 | 7 | Inspirit 8+, Darksteel Reactor (indestructible), Hangarback, Emry, Swan Song, Ripples, Buried Ruin; plus 3 indestructible Bridges; every noncreature artifact survives creature wipes with its counters. |
| Ramp | base | 10 | 12 | **9 tags (WARN); about 5 timed** | Timed (review I-2): castable by turn 2 and helping Kilo: Sol Ring, Arcane Signet, Chalice, Prism; Sculptor and Mechanaut at half (they discount artifacts, not Kilo). Cornucopia, Sphere, Solar Array are turn-4 plays. Fixing (not counted as ramp): Barrels of Blasting Jelly, Chromatic Star, Spire, Orchard. Fix: purchase 1 (Talisman). |
| Draw (nets cards) | base | 10 | 12 | **13** | Insight Engine, Uthros, Sensor (half), Etched Oracle, Automaton, Gambit, Thirst, Katara (repeatable, half), Universal Surveillance, Waterbending Lesson, Thought Monitor, Jhoira, Inspiring Overseer. |
| Removal (spot) | base | 6 | 8 | **8** + Soul-Guide Lantern (graveyard answer, tagged removal) | Tranquilize, Dispatch, Chaos Warp, Airbending Lesson, Firebending Lesson, Sandbenders' Storm, Barrels (late), Lux Cannon. Answers to opposing commanders: Chaos Warp (tuck), Tranquilize (stun kept up by proliferate), Dispatch (exile), Lux Cannon. |
| Wipes | base | 2 (hybrid takes the higher) | 2 | **2** | Fumigate, Organic Extinction; both near one-sided here (noncreature artifacts survive; Organic spares artifact creatures; Inspirit 8+ makes Fumigate one-sided). |
| Commander protection | base, enabler | 3 | 4 | **4 tags, about 3.25 weighted** | Swan Song 1 (spells only), Airbending Lesson 1 (exile and recast for {2}), Ripples 0.75 (needs a counter on Kilo), Inspirit 0.5 (needs 8). Swiftfoot Boots (extra purchase) makes 5 tags, about 4.25. |
| Graveyard hate | base | 1 | 1 | 1 | Soul-Guide Lantern. |
| Lands | band 36 to 37 | | | **37** | Rule of thumb 31 + 3 colors + MV 3 = 37; timed ramp about 5, so the top of the band. |
| Curve | avg MV band 2.6 to 3.1 | | | **3.15** | MV 0: 3, 1: 7, 2: 11, 3: 19, 4: 14, 5: 2, 6: 2, 7+: 4. Thought Monitor (affinity) and Organic Extinction (improvise) cost less in practice. |
| Creatures | 15 to 28 | | | 26 in the 99 | Plus 2 Vehicles and 2 Spacecraft. |

**Card-flow budget (turns 4 to 8).** Spend: about one card a turn. Gain: natural draw 1, plus Insight Engine (1, 2, 3... per
activation, faster with proliferate), Uthros and Jhoira (1 per artifact spell), Sensor (1 per 2 counters), Katara (1 per
round), Oracle and Automaton bursts; Chromatic Star replaces itself. Holds.

**Counter rate.** Turn 4: 2 to 4 countered permanents, a Kilo trigger adds 2 to 4 counters, sources add 2 to 3. Turn 6: 5 to
7 countered permanents, about 7 to 10 new counters a turn. Lux Artillery's 30 counters arrive around turns 8 to 10 [J, not
simulated]; Darksteel Reactor alone needs about 7 turns after it lands, 3 to 4 with Tekuthal or Deepglow Skate.

**Dead clauses named.** Thrummingbird's proliferate needs combat damage (weak late); Airbending Lesson lets the opponent
recast the permanent for {2} (best on tokens or expensive permanents); Depthshaker's "sacrifice the animated artifacts"
clause is used only on spare artifacts; Barrels' damage clause costs {5} (a late use). No vehicle, equipment or partner
clause lacks its cards (2 vehicles crewed by Kilo; Swiftfoot Boots, if bought, is the only equipment and equips Kilo).

## 4. The list by function: how to use each card

**Commander.** Kilo, Apogee Mind: cast on turn 3 (turn 2 off Sol Ring); attack with haste only into an empty or small
board; otherwise tap it at home (station Inspirit or Uthros, crew Brute Suit or Ovalchase Dragster at the last opponent's
end step, pay waterbend or improvise with it). Every tap is a proliferate: choose only your permanents (and opposing stuns).
Mulligan a seven that cannot make all three colors by turn 4 (review I-1).

**Ramp and fixing (9 + 2)**
- Sol Ring: turn 1; makes a turn-2 Kilo possible; later pays Insight Engine, Titan Forge, Karn's Bastion. Never bad.
- Arcane Signet: turn 2; fixes all three colors for Kilo on turn 3.
- Everflowing Chalice: turn 2 with one kick, never for 0; each proliferate adds a counter, so it is +1 colorless mana a turn. Late, kick it two or three times as an artifact entry for Surge Conductor and Fireweaver.
- Pentad Prism: turn 2 with two colors; spend counters for a big turn but keep one so proliferate and Coretapper refill it.
- Astral Cornucopia: X=1 on turn 4 after Kilo (X=2 on turn 6); grows into a many-mana fountain for Universal Surveillance, Insight Engine and Katara. Bad early (never instead of Kilo).
- Commander's Sphere: turn 3 or 4 fixing; sacrifice it for a card in response to artifact removal or when mana no longer matters.
- Solar Array: turn 3 or 4; tap it for the next artifact spell so that spell gets sunburst (more counters on Etched Oracle, Crawler, Hangarback; charge counters on rocks, which Lux Artillery counts).
- Etherium Sculptor: turn 2; 37 artifact spells cost 1 less (not Kilo); later a station or crew body. Bad late.
- Enthusiastic Mechanaut: turn 2; same discount and a 2/2 flyer that chips and blocks flyers.
- Barrels of Blasting Jelly: turn 1 or 2; from then on {1} turns one mana into the color Kilo is missing (once a turn, no loss), so it is a fixer for turn 3; an artifact entry for Surge Conductor and Fireweaver; late, {5} and sacrifice it for 5 damage to a creature.
- Chromatic Star: turn 1 or 2; pay {1} and sacrifice it for the missing color on Kilo's turn, and draw a card when it goes to the graveyard from the battlefield (a cheap artifact entry and exit for Surge Conductor, Fireweaver, Jhoira and Uthros). Bad never: it replaces itself.

**Counter engines and sources**
- Coretapper: turn 2; each turn a charge counter on the best target (Prism or Chalice early for mana; Reactor, Titan Forge, Lux Cannon, Sensor later); sacrifice it in response to removal for two counters.
- Steel Overseer: turn 2 or 3; tap it every turn for +1/+1 on every artifact creature, Kilo included (that enables Ripples on Kilo). Keep it home; dies to pings.
- Hangarback Walker: X=1 on turn 2, or large late; pump it with {1},T; proliferate grows it; let it die into flying Thopters (Board 1, Fireweaver pings).
- Insight Engine: turn 3 or 4; activate at an opponent's end step after Kilo grew it on your turn: it draws 2, 4, 6. The main draw engine; protect it.
- Uthros Research Craft: turn 3 or 4; station it with Kilo (proliferate first, then 3 counters) to reach 3+ at once; a card per artifact spell; 12+ is a big flyer.
- Inspirit, Flagship Vessel: turn 4 or 5; station it with Kilo every turn (proliferate, then +3) to 8 in about two turns; each combat put two charge counters on Reactor, Titan Forge or Lux Cannon, or a +1/+1 on Kilo; at 8+ every other artifact, Kilo included, has hexproof and indestructible. The best card of the 99. Bad only before turn 4.
- Long-Range Sensor: turn 3 to 5; Kilo's attack gives a counter and the proliferate another; Coretapper and Inspirit feed it without attacks; Discover 4 at sorcery speed can hit Lux Artillery or the Reactor (the route's only extra access).
- Crystalline Crawler: cast with three colors (three counters, six with Lux); tap it every turn for a counter; remove counters for any color in a big turn.
- Empowered Autogenerator: turn 4 or 5 (enters tapped); every tap adds a counter then that much mana; with proliferate it gives 5 to 10 mana by turn 8 for X spells, Titan Forge and Karn's Bastion.
- Etched Oracle: cast with three colors; one proliferate makes it "draw three"; refill and repeat.
- Mindless Automaton: discard extra lands late for counters; remove two to draw; proliferate turns it into a draw engine.
- Patrolling Peacemaker: a 2/2 with counters that proliferates whenever an opponent targets another player or their stuff, which happens every round in a 4-player pod.
- Kappa Cannoneer: improvise it by tapping Kilo (proliferate) and rocks; ward 4; every artifact entry grows it and makes it unblockable, a clock that Board 2 cannot block.
- Chrome Host Seedshark: turn 3; every noncreature spell makes an Incubator with X +1/+1 counters (Lux counts them, proliferate grows them; pay {2} to make an artifact creature for Cyberdrive or station). 2/4 flying blocker.
- Lux Cannon (removal): tap each turn for a counter; with Kilo it fires every second turn: destroy any permanent.

**Proliferate (7 + Karn's Bastion, Patrolling Peacemaker)**
- Surge Conductor: turn 3; every nontoken artifact entering (rocks, artifact lands, Barrels, Star) proliferates. Play it before a chain of cheap artifacts.
- Thrummingbird: turn 2 while boards are empty; proliferates when it connects. Bad late.
- Tekuthal, Inquiry Dominus: doubles every proliferate (Kilo's trigger counts twice); a 3/5 flying blocker; remove three counters to give it an indestructible counter before a wipe.
- Tezzeret's Gambit: draw two and proliferate; pay 2 life for {U/P} if blue is short; best when Kilo is off the table or to push the Reactor.
- Experimental Augury: at an opponent's end step: dig three for a finisher and proliferate.
- Ripples of Potential: hold it for removal or a wipe: proliferate, then phase out everything that got a counter (Kilo with a +1/+1, Insight Engine, Lux Artillery, Reactor).
- Deepglow Skate: late; doubles every kind of counter on chosen permanents: Reactor 10 to 20 wins, Lux Artillery's count jumps. Bad early.

**Finishers (win routes)**
- Lux Artillery: cast when about 15 counters are out, or earlier so artifact creature spells (Kilo recast too) get sunburst; at 30 counters it deals 10 to each opponent every end step. Bad early.
- Darksteel Reactor: cast turns 4 to 6; indestructible; feed it with Coretapper, Inspirit and proliferate; 20 wins. Hold Swan Song or Ripples for the exile or bounce aimed at it.
- Reckless Fireweaver: turn 2 or 3; 1 to each opponent per artifact entry (rocks, Barrels, Star, Thopters, Gnomes, Incubators); chip damage that makes Lux's 10 lethal a turn earlier.
- Cyberdrive Awakener: cast in the main phase of the kill turn; every noncreature artifact you had since the turn began becomes a 4/4 flyer and attacks with the flying artifact creatures. Bad early.
- Depthshaker Titan: late; animate only spare noncreature artifacts (they are sacrificed) or none; every artifact creature gets trample, haste and melee. Bad early.
- Threefold Thunderhulk: late; Gnomes equal to its power on entering and on each attack (six with Lux); sacrifice spare artifacts to grow it. Bad early.
- Titan Forge: activate {3},T on spare turns; proliferate fills it; three counters make a 9/9 that blocks Board 2 and attacks.

**Card draw (7 + the draw engines above)**
- Thirst for Knowledge: instant; discard one artifact (a spare rock late, or Lux/Reactor for Emry and Buried Ruin).
- Katara, Bending Prodigy: at an opponent's end step pay waterbend {6} by tapping Kilo (proliferate) and the artifacts you did not use: a card each round at instant speed; if Katara is tapped at your end step she grows. Bad early (few artifacts to tap).
- Universal Surveillance: improvise with Kilo (proliferate), rocks and artifact lands; X of 4 to 6 on turn 6 or later.
- Waterbending Lesson: draw three; pay waterbend {2} by tapping Kilo (proliferate) and an artifact to keep every card.
- Thought Monitor: affinity makes it 2 to 4 mana for a 2/2 flyer and two cards. Bad early.
- Jhoira, Weatherlight Captain: turn 4; every artifact or legendary spell draws; cast it before a chain of cheap artifacts.
- Inspiring Overseer: turn 3; a card and a 2/1 flyer (station fuel, chump blocker against Board 2). Stand-in for the Talisman.

**Removal (7 spot + Lux Cannon + graveyard)**
- Tranquilize: on the biggest Board 2 creature or an opposing commander: three stun counters, and every Kilo trigger adds another, so it never untaps while Kilo lives. Sorcery: cast it before the attack.
- Dispatch: from turn 3 (three artifacts) it exiles for one mana; before that it taps an attacker.
- Chaos Warp: any permanent, commanders included (tuck); the answer to enchantments.
- Airbending Lesson: instant: exile a nonland permanent and draw; or exile your own Kilo in response to removal and recast it for {2} with haste.
- Firebending Lesson: 2 damage to a utility creature early; kicked, 5 damage late.
- Sandbenders' Storm: instant: destroy a creature with power 4 or more (Board 2); or earthbend 3 for a land with counters that proliferate grows and that returns when it dies.
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
- Ovalchase Dragster: crew 1 with Kilo (proliferate); a 6/1 trample haste attacker when a lane is open; flies with Cyberdrive. Bad against pingers. Stand-in for Swiftfoot Boots.

**Lands (37)**
- Untapped duals: Adarkar Wastes, Shivan Reef (pain lands); Sulfur Falls, Glacial Fortress, Clifftop Retreat (check lands: play after a basic); Radiant Summit (untapped with two basics); Rugged Prairie, Cascade Bluffs, Skycloud Expanse (filters: need another colored mana, so count them as colorless until then).
- Any color: Exotic Orchard (depends on opponents), Spire of Industry (with an artifact, 1 life).
- Utility colorless: Karn's Bastion ({4},T proliferate, also on opponents' turns), Buried Ruin (return Lux or Reactor).
- Artifact lands: Ancient Den, Great Furnace, Seat of the Synod (untapped; metalcraft, improvise, Surge Conductor); Silverbluff, Razortide, Rustvale Bridge (tapped, indestructible artifacts).
- Mystic Monastery, Path of Ancestry: tapped tri-color lands; play them on turn 1 or a turn with spare mana.
- Basics: 7 Island, 4 Plains, 5 Mountain (all Spanish; the fifth Mountain is the stand-in for Command Tower).

## 5. Cut log

New deck: no current list and no proven role-player for this commander (lesson L6 names cards of the other decks). The
precon is the starting point; these are the EOC cards in the pool that are NOT in the list, the cards cut in rounds 2 and 3,
and the main non-precon cards considered.

| Card | Function it served | Count after the cut (min) | Replacement and reason |
|---|---|---|---|
| Golem Foundry (EOC, round 3) | counter source, artifact payoff | sources 23 (12), artifact payoffs 18 (10) | Barrels of Blasting Jelly: the mana fix Kilo needs on turn 3 (simulation in section 11), plus late removal; Foundry was the weakest engine and its Freed-line role is gone this iteration. |
| Detained by Legionnaires (round 3) | spot removal, commander answer | removal 8 (6), through_big 16 (10) | Chromatic Star (fixing and a card); Detained falls to bounce and sacrifice; commander answers left: Chaos Warp, Tranquilize, Dispatch, Lux Cannon. |
| The Mycosynth Gardens (EOC, round 3) | any-color land for {1} | lands 37 | A fifth Mountain: red is a short color, and the Mountain also turns on Clifftop Retreat, Sulfur Falls and Radiant Summit (review M-4). |
| Swords to Plowshares (round 2) | spot removal | removal 8 (6) | Given to Ezio; Tranquilize. |
| Pull from Tomorrow (round 2) | draw | draw 13 (10) | Given to Azula; Katara, Bending Prodigy. |
| Battlefield Forge (round 2) | untapped R/W land | lands 37 | Given to Toph; Path of Ancestry. |
| Wake the Past (EOC) | wipe insurance (7 MV) | wipe_insurance 7 (2) | Emry, Buried Ruin, Inspirit cover it. First card back if artifact wipes show up in the pod. |
| Resourceful Defense (EOC) | wipe insurance; moves counters to the Reactor | 7 (2) | Does nothing on the turn it lands. Second card back. |
| Moxite Refinery (EOC) | moves counters, sorcery speed | sources 23 (12) | Narrow; Coretapper does the feeding. |
| Gavel of the Righteous (EOC) | counter source, equipment | sources 23 (12) | Little value on Kilo. |
| Alibou, Ancient Witness (EOC) | haste for artifact creatures, single-target damage | through_big 16 (10) | 5 MV, single target; Depthshaker gives the same haste. |
| Angel of the Ruins (EOC) | artifact/enchantment removal, 7 MV | removal 8 (6) | Chaos Warp and Lux Cannon do it cheaper. |
| Cloud Key (EOC) | cost reducer | ramp 9 (10, WARN) | A turn-3-to-4 play like Sphere, with less output. |
| Command Tower (EOC) | land | lands 37 | All three copies are in Toph, Azula and Ezio; conditional purchase 2. |
| Temple of Enlightenment, Irrigated Farmland, Lonely Sandbar, Secluded Steppe, Evolving Wilds (EOC) | tapped lands | lands 37 | Already 5 tapped lands; untapped lands and basics preferred. |
| Chain Reaction, Planar Cleansing | wipes | wipes 2 (2) | Hit my own board. |
| Rowdy Snowballers | stun | through_big 16 (10) | One stun counter; Tranquilize gives three. |
| Divination, Geyser Leaper, Forecasting Fortune Teller | draw | draw 13 (10) | Weaker than the 13 kept. |
| Cat-Owl, Flexible Waterbender, Adrestia, Astral Wingspan | Kilo tap outlets | 11 (6) | Brute Suit, Dragster, Patrol and Katara do it cheaper. |
| Burnished Hart | land ramp at turn 4+ | ramp 9 | Too slow. |
| Equipment and Assassin cards (Hookblade, Cobbled Wings, Glider Staff, Headsplitter, Brotherhood Spy...) | evasion, other plans | evasion 9 (4) | A second package (L1, L7). |
| Buried Ruin → Plains (tested, not done) | | | +1 point of turn-3 Kilo (inside the noise), but Buried Ruin is one of the two recovery pieces of the noncombat route. Kept. |

## 6. Loans

None. The loan candidates are English cards of his Standard decks; a 100 % Spanish deck cannot play them.

## 7. Scarce copies (resolved by the lead, round 2)

| Card | Copies (ES) | Other deck | Goes to | Kilo's list |
|---|---|---|---|---|
| Swan Song, Insight Engine, Thirst for Knowledge | 1 each | Azula (and Ezio for Swan Song) | **Kilo** | kept |
| Soul-Guide Lantern | 2: one in Toph, one free | Azula | **Toph and Kilo**; Azula's is a separate purchase | kept |
| Commander's Sphere, Spire of Industry, Glacial Fortress, Mystic Monastery, Radiant Summit | 1 each | Ezio | **Kilo** | kept |
| Swords to Plowshares / Pull from Tomorrow / Battlefield Forge | | Ezio / Azula / Toph | the other deck | replaced (Tranquilize, Katara, Path of Ancestry) |
| Command Tower | 3, in Toph, Azula and Ezio | | those three | Kilo buys one if a Spanish copy is in stock |

Round-3 additions (Barrels of Blasting Jelly, Chromatic Star, a fifth Spanish Mountain) are wanted by no other deck. No
conflict: Sol Ring, Arcane Signet, Exotic Orchard, Sulfur Falls, Clifftop Retreat, Rugged Prairie, Shivan Reef, Cascade
Bluffs, Chaos Warp, Sandbenders' Storm, Path of Ancestry (separate physical copies in the assignment).

## 8. Purchases (Game of Magic Singles, Spanish copies; Kilo's own cap 5,000 CLP; Boots outside it)

Live stock and prices as read by the reviewer on 2026-11-02 (product `.js` variant data, `decks/reports/review-spanish-deck.md`
section 3b); re-verify within 24 hours of buying. The list holds each purchase's owned stand-in, so it is playable today.

| Rank | Card (Spanish) | Stock and price (2026-11-02) | Need | Replaces (stand-in now in the list) | Fallback |
|---|---|---|---|---|---|
| extra (outside the cap, owner-approved) | Swiftfoot Boots | **in stock**, 3,280 (The Brothers' War Retro Artifacts, schematic, NM ES) | Commander protection 4 to 5 tags (about 3.25 to 4.25 weighted); hexproof, equip {1} does not tap Kilo | Ovalchase Dragster (tap outlets 11 to 10, min 6) | none in stock (Pemmin's Aura out of stock); keep Dragster |
| 1 | Talisman of Conviction | **in stock**, 1,500 (Tarkir: Dragonstorm Commander, NM ES) | Turn-2 rock that makes R or W, Kilo's two short colors; ramp 9 to 10 (WARN closed; about 6 timed) | Inspiring Overseer (draw 13 to 12, min 10) | another Spanish 2-mana rock in stock at buying time (Talisman of Progress or Creativity, a Boros, Azorius or Izzet Signet, Fellwar Stone, Mind Stone), stock not read; else keep Inspiring Overseer |
| 2 | Command Tower | **not confirmed**: Spanish AFC (570), ZNC (1,000) and DFC (1,000) unavailable; English copies in stock (not allowed for this deck); about 25 printings unread (HTTP 429) | Untapped tri-color land | the fifth Mountain | keep the Mountain |
| 3 | A second Spanish 2-mana rock (same candidates as rank 1's fallback) | stock not read | Timed ramp about 6 to 7; Kilo on turn 3 more often | Etherium Sculptor (bad late, discounts artifacts only) | keep Sculptor |

**Inside the 5,000 cap:** Talisman 1,500 + Command Tower 570 to 1,000 = 2,070 to 2,500; about 2,500 left for rank 3 if a
Spanish rock is in stock (prices of 700 to 1,500 are usual for these), or for the next iteration's tutor (Fabricate 9,800
Spanish foil, Whir of Invention out of stock: both over the cap now). **Outside:** Swiftfoot Boots 3,280. Kilo on turn 3
(simulation, section 11): 82.9 % now, 84.2 % with the Talisman, 85.5 % with the Talisman and Command Tower.

**Out this iteration (review B-1):** Relic of Legends (no copy in any of 7 products), Freed from the Real (no Spanish copy;
cheapest printing 5,200 English Damaged, unavailable; only a 28,800 English foil in stock), Springleaf Drum and Pemmin's Aura
(no stock).

**Optional upgrade path (only if a second store is added, owner 2026-11-02: it must stock Hidden Footblade and Overpowering
Attack; then Freed from the Real and Relic of Legends are bought there in Spanish).**
- Relic of Legends replaces Brute Suit (a better tap outlet: it taps Kilo for mana at instant speed, and it is a rock).
- Freed from the Real replaces Firebending Lesson (removal 8 to 7, min 6). Alone with Kilo: `{U}: tap` and `{U}: untap` give an
  extra proliferate for {U}{U} at instant speed, as often as mana allows.
- The line (late, three cards with the commander, Bracket 3 legal, owner's rule welcomes it): tap Kilo for Relic's second
  ability (one blue mana; Kilo proliferates), pay that {U} to Freed's untap, repeat: infinite proliferate at instant speed. With
  Pentad Prism or Crystalline Crawler holding a counter, each loop also nets mana. It wins with a card the deck already plays:
  Darksteel Reactor with a counter (20 counters: the game is won), Etched Oracle plus the infinite mana from Prism or Crawler
  ("target player draws three" on each opponent until they draw from an empty library), Lux Artillery (30 counters at once,
  10 to each opponent per end step), or an infinite-size unblockable Kappa Cannoneer. Do not grow Insight Engine past your own
  library.
- Checked in the scratchpad: the list with Boots, Talisman, Command Tower, Relic and Freed passes `check_phase2_bracket.py`
  (floor 1, 0 Game Changers; Spellbook: one combo, Kilo + Freed from the Real + Relic of Legends, "Infinite proliferate").
- After the path: tap outlets 11, ramp 11 tags, protection 5, removal 7 spot.

## 9. WARN reasons and dead clauses

- **Ramp 9 of 10 (WARN), about 5 timed.** The Spanish pool has no further turn-1-to-2 rock (Mind Stone's Spanish copy is in
  Azula). Mitigation: Chalice, Prism and Cornucopia gain mana with every proliferate and Coretapper charges them; Crawler and
  Autogenerator add late mana; Barrels and Chromatic Star fix colors (not counted as ramp). Fix: purchase 1 (Talisman of
  Conviction, in stock), then rank 3.
- **counter_doublers reaches 10 only with Kilo (WARN).** Correct after removing North Pole Patrol (review M-1): it untaps Kilo,
  it does not proliferate. The pool has no other proliferate card; Kilo is the guaranteed piece, and the 9 others (about 6.5
  weighted) are above the profile's support min 4. No purchase cut takes a card from this function.
- Commander protection meets the floor by tags (4) but is about 3.25 weighted; Swiftfoot Boots (extra) brings it to 5.
- Bad when drawn: 10 early (Thunderhulk, Depthshaker, Cyberdrive, Organic Extinction, Deepglow Skate, Lux Artillery, Kappa,
  Thought Monitor, Katara, Astral Cornucopia), 2 late (Thrummingbird, Etherium Sculptor): 12, at the warning line.
- Dead clauses: section 3.

## 10. The two reference boards

- **Board 1, eight or more 1/1 chump blockers that can be sacrificed.** Kilo never needs to attack into them: station, crew
  and waterbend keep the proliferate going. Win through: Lux Artillery (10 to each opponent per end step, no combat), Darksteel
  Reactor, Fireweaver chip damage; Cyberdrive Awakener turns the rocks into 4/4 flyers over the goblins; Organic Extinction
  and Fumigate clear them. The nine small flyers count but none closes alone. Risk: pingers kill Coretapper, Steel Overseer,
  Thrummingbird and Sculptor; the important engines are noncreature artifacts (Insight Engine, Lux, Reactor, Titan Forge,
  Autogenerator, Lux Cannon).
- **Board 2, two or more creatures bigger than ours.** Do not attack with Kilo; tap it at home. Answers: 7 spot removal plus
  Lux Cannon every second turn and Barrels late; Tranquilize keeps one tapped for good while Kilo lives; North Pole Patrol taps
  one each round; Titan Forge 9/9s and Tekuthal 3/5 block; Kappa Cannoneer is unblockable after each artifact entry; the route
  1 finishers ignore blockers. The real cost here is speed if neither noncombat finisher shows up.
- **One sweeper turn.** A creature wipe leaves every noncreature artifact and its counters: recast Kilo for 5 with haste and
  proliferate at once. An artifact wipe: Inspirit at 8+, the Reactor and the Bridges are indestructible; Swan Song counters a
  sorcery wipe; Ripples phases out the countered permanents; Emry and Buried Ruin rebuild.
- **Toughness.** Closers are big (Cyberdrive 4/4 and 4/4 rocks, Depthshaker 5/5, Titan 9/9s, Thunderhulk); about 12 of the 26
  creatures have toughness 2 or less, all engines kept at home, covered by Steel Overseer, proliferate on +1/+1 counters and
  Inspirit's indestructibility.

## 11. Mana

- **Simulation** (scratchpad `sim_kilo.py`, 4,000 games per point, 7 + T cards, no mulligan, best land order, check lands and
  Radiant Summit by condition, filters and Skycloud consuming another land's mana, Spire with an artifact, Exotic Orchard right
  in half the games, Sol Ring turn 1, 2-mana rocks turn 2, Barrels and Chromatic Star converting one mana). Kilo castable on
  turn 3, all games / games with 3+ lands:

  | List | Turn 3 | Turn 4 (4+ lands) |
  |---|---|---|
  | Round 2 list | 64.8 % / 77.4 % (the reviewer's model: 76.4 %) | 90.5 % |
  | Mycosynth → Mountain | 66.6 % / 79.5 % | 89.6 % |
  | + Golem Foundry → Barrels | 68.4 % / 81.3 % | 90.9 % |
  | **+ Detained → Chromatic Star (this list)** | **69.8 % / 82.9 %** | **91.8 %** |
  | + Talisman of Conviction (purchase 1) | 72.2 % / 84.2 % | about 92 % |
  | + Command Tower for the fifth Mountain (purchase 2) | 73.0 % / 85.5 % | about 92 % |

  Tested and rejected (within noise or a worse trade): Exotic Orchard → Plains (82.2 %), Rustvale Bridge → Plains (82.0 %),
  Path of Ancestry → Mountain (80.4 %), Skycloud Expanse → Plains (80.7 %), Buried Ruin → Plains (84.0 %, costs route 1's
  recursion). Karsten's target for a gold three-drop (about 92 % on turn 3) is out of reach of the Spanish pool: no more
  untapped tri-color or R/W sources are owned. The deck reaches about 92 % on turn 4. Guide: mulligan a hand that cannot make
  all three colors by turn 4.
- **Unconditional land sources:** U 16, W 13, R 14 (filters, Skycloud, Spire and Orchard counted apart; review I-1); plus
  Arcane Signet and Pentad Prism (any), Barrels and Chromatic Star (convert one mana), Commander's Sphere and Solar Array
  (turn 4).
- **Tapped lands:** 5 always (Mystic Monastery, Path of Ancestry, three Bridges); check lands and Radiant Summit usually
  untapped from turn 2 (16 basics).
- **Curve:** section 3. Turn 2 plays: 11 two-drops plus Chalice and Hangarback; turn 3: Kilo first.
- **Keepable hand:** 37 lands give 2 to 4 lands in 7 about 75 % per look, about 93 % with the free first mulligan.

## 12. Open questions for the owner

Answered in rounds 2 and 3 (scarce copies, Freed from the Real, Boots as an extra, one store, the Salt floor, the second-store
condition). Still open:
1. Rank 3 (a second Spanish 2-mana rock): should the lead read the Spanish stock of Talisman of Progress and Creativity, the
   three Signets, Fellwar Stone and Mind Stone at Game of Magic Singles, to spend the rest of Kilo's 5,000?
