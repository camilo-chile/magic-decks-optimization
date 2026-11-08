# Kilo, Apogee Mind: the Spanish deck (Phase 2 build, 2026-11-08, step 6 second pass)

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
- Step 4 (2026-11-07; round-3 re-review in `decks/reports/review-spanish-deck.md`, owner decisions of 2026-11-07, the new power
  target of SKILL.md principle 7). The 100-card list is unchanged: no unused owned Spanish card beats the weakest slots, so
  every upgrade is a purchase swap (section 8), and the list keeps the owned stand-ins so it plays today and
  `assign_copies.py` stays clean (it has no notion of planned purchases). Applied: R3-1 (purchases re-ranked over three stores:
  Game of Magic Singles, PayToWin, Tienda La Comarca; Prophetic Prism and Volt Charge in), R3-2 (Barrels of Blasting Jelly now
  tagged `removal` first; Chromatic Star keeps `engine` because its job in the deck is cheap artifact fuel for Surge
  Conductor, Fireweaver, Jhoira and Uthros, and the plan schema has no utility tag), R3-3 (the copy text below is corrected).
- **Competitive pass (principle 7).** Every slot was re-checked against Bracket 4 and 5 options the deck can actually get:
  - **Game Changers: 0 used, 3 slots open.** The owned Spanish pool has none (live Scryfall `is:gamechanger`, 53 cards,
    2026-11-07). In Kilo's colors the best fits are: Narset, Parter of Veils (Kilo proliferates its loyalty, so its −2 digs for
    Lux Artillery or Darksteel Reactor every turn, and it shuts off opponents' extra draws), Teferi's Protection, Enlightened
    Tutor (finds Lux, Reactor or Inspirit), Gifts Ungiven (a tutor toward route 1), Smothering Tithe, Rhystic Study, Cyclonic
    Rift. Live read 2026-11-07: **Narset has no Spanish copy in stock** in the three stores (PayToWin and Game of Magic
    Singles: English only, every Spanish variant unavailable; La Comarca: English NM 1,850); Gifts Ungiven in Spanish is at
    PayToWin for 9,100 (HP) or 10,000 (MP), over the cap; the rest cost roughly 15,000 to 60,000 CLP. So all three slots stay
    open this iteration; Narset in Spanish is the first wish for the next one, then Teferi's Protection and Enlightened Tutor.
  - **Tutors toward the win lines:** none ownable in Spanish this iteration (Fabricate only as a 9,800 Spanish foil, Whir of
    Invention out of stock, Gifts over the cap). Long-Range Sensor's Discover 4 remains route 1's only extra access.
  - **Cheap interaction and low curve:** Volt Charge (1 mana cheaper than kicked Firebending, instant, removal plus
    proliferate) and Prophetic Prism (fixing plus a card) are the buyable upgrades; the curve already averages 3.15 with 7
    one-drops and 11 two-drops.
  - **Fast mana that is not a Game Changer:** Sol Ring is in; Mana Crypt is banned; the remaining fast rocks (Mana Vault,
    Grim Monolith, Chrome Mox) are Game Changers and far over the cap.

- **Step 6 (2026-11-07, after Commander Salt: 3.9, Bracket 2; precon 3.8; `decks/reports/salt-spanish-deck-20261107.md`).** Salt's diagnosis was "control without a finisher", no tutors, 2 wipes, light counterspells, 6 tapped lands. Owner standard: consistent, robust and as powerful as possible, with a clear way to close; Salt floor 4.5. Changes:
  - **Closer:** Darksteel Reactor becomes a fast, compact win instead of a 7-turn clock: Resourceful Defense (in for Depthshaker Titan) moves every counter of one permanent onto it at instant speed, and Moxite Refinery (in for Mindless Automaton) turns any counters into charge counters on it. Both were precon cards I had cut; with Kilo proliferating 5 to 10 permanents a turn, the Reactor reaches 20 one to two turns after it lands.
  - **Interaction:** Chain Reaction (in for Threefold Thunderhulk) is the third wipe (the answer to Board 1's chump wall); the purchases add Volt Charge and Generous Gift.
  - **Tapped lands:** kept. Replacing a Bridge with a basic costs Kilo 1 to 2 points on turn 3 (simulation); the fix is Battlefield Forge (over the cap) and Command Tower.
  - **Infinite line:** Spellbook lists Kilo + Aura of Dominion + Pentad Prism or Crystalline Crawler (both owned): the best closer for this deck, but Aura of Dominion and Sinking Feeling (the Relic partner) have no Spanish copy in stock in the three stores, so it is the first over-cap wish (section 8).

- **Step 6, second pass (2026-11-08; `decks/reports/salt-spanish-deck-v2-20261107.md`).** The funnel list scored 3.8 on Salt owned and after purchases (Win conditions 91/200, "control without a finisher", combos: none): Salt does not see the Reactor funnel. New Salt floor 4.0, cap 7,000 CLP. A search of the local Spellbook cache found two lines completed by one cheap Spanish card each, reusing cards already in the list: **Meticulous Excavation + Lux Artillery + Crystalline Crawler** (infinite mana and artifact entries; Reckless Fireweaver or Surge Conductor turns it into a win) and **Voltaic Construct + Cyberdrive Awakener + a rock** (infinite mana on the Cyberdrive turn). They replace Relic of Legends in the cap (section 8). The 100-card list file is unchanged (owned stand-ins); no owned Spanish card adds a combo or more interaction. Filigree Sages was rejected (an early two-card infinite, floor 4).

**Checks on this list** (2026-11-07): `python scripts/plan_density.py` **PASS** (step 6), 2 WARN (ramp 9 of 10; counter_doublers
reaches 10 only with Kilo; both reasons in section 9, and Volt Charge clears the second); base counts ramp 9, draw 12, removal 9, wipe 3, protection 4. `python scripts/check_phase2_bracket.py
decks/phase2/spanish-deck.txt` **PASS** (floor 1, 0 Game Changers, no extra turns, no mass land denial, 0 Spellbook combos
inside). `python scripts/assign_copies.py`: spanish-deck 100 of 100 copies covered, 0 missing, 0 problems (the four decks all
100 of 100); the 12 "shared" names involving Kilo (Sol Ring, Arcane Signet, Exotic Orchard, Sulfur Falls, Clifftop Retreat,
Rugged Prairie, Shivan Reef, Cascade Bluffs, Chaos Warp, Path of Ancestry, Waterbending Lesson, Soul-Guide Lantern) each have
separate physical copies. Barrels of Blasting Jelly (TLA 254, ES), Chromatic Star (TSR 263, ES) and the 5 Mountains (ACR 305,
ES) are assigned to Kilo in `data/model/phase2/assignment.json` (the round-3 note said otherwise; corrected). The optional
upgrade list of round 3 (with Freed from the Real and Relic of Legends) passed the same bracket script in the scratchpad (floor
1, one combo: Kilo + Freed from the Real + Relic of Legends, "Infinite proliferate"); Freed is still not buyable in Spanish.

## 1. Commander reading and rules points to verify

Oracle (Scryfall, 2026-11-02): Kilo, Apogee Mind {U}{R}{W}, Legendary Artifact Creature, Robot Artificer, 3/3, Haste.
"Whenever Kilo becomes tapped, proliferate."

| Question | Answer |
|---|---|
| Rewards | Kilo becoming tapped, by ANY means: attacking (haste, so the turn it lands), station, crew, improvise, convoke, a waterbend cost, any later re-tap after an untap. Each tap is one proliferate. |
| Fuel | Permanents that already carry counters (charge on rocks and engines, +1/+1 on artifact creatures, stun on opposing creatures). Kilo adds nothing to a permanent without a counter, so the 99 must PLACE counters (sources) and then CONVERT them (payoffs). Second fuel: tap events, one per untap cycle unless untappers. |
| Window | Any time it becomes tapped: my combat (attack), my main phase (station, sorcery speed), any time I have priority (crew, waterbend, improvise). Crew and waterbend let Kilo stay untapped as a blocker through the opponents' turns and tap at the last end step. |
| How it wins | It does not. It multiplies counters that become mana (Chalice, Prism, Cornucopia, Autogenerator, Crawler), cards (Insight Engine, Etched Oracle, Sensor), threats (Titan Forge, Hangarback, Kappa) and two finishers that need no combat: Darksteel Reactor (wins at 20; Resourceful Defense and Moxite Refinery funnel counters onto it) and Lux Artillery (10 to EACH opponent per end step at 30 counters). |
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
- **Main closer (step 6): the Darksteel Reactor funnel.** Darksteel Reactor (indestructible) gains a charge counter each upkeep, one per Kilo
  trigger (two with Tekuthal), two per combat from Inspirit and one per Coretapper tap; Resourceful Defense ({4}{W}, instant
  speed) moves every counter of one permanent onto it, and Moxite Refinery (sorcery) converts X counters of any kind into X charge
  counters on it. Typical win: Reactor on turn 5 or 6, 20 counters by turn 7 or 8. Lux Artillery (30 counters, 10 to each
  opponent per end step) is the second noncombat route.
- **Backup (same pieces).** The countered artifact board attacks: Cyberdrive Awakener (every noncreature artifact a
  4/4 flyer this turn, every artifact creature flying), Titan Forge 9/9s and an unblockable Kappa Cannoneer; Uthros at 12+ adds evasive damage. All six closers of both routes: about 66 % to
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
| artifact_payoffs | gate, early | 10 | 12 | **17** (91 %) | Surge Conductor, Fireweaver, Uthros, Jhoira, Kappa, Cyberdrive, Thought Monitor, 2 cost reducers, Emry, Inspirit, Steel Overseer, Dispatch, Universal Surveillance, Organic Extinction, Lux Artillery, Seedshark. |
| through_wide_board | gate, early | 10 | 12 | **16** (90 %) | Team level 7: Lux Artillery, Reactor, Fireweaver (scales), Cyberdrive, Chain Reaction, Organic Extinction, Fumigate. Flyers and unblockables 9 (Hangarback Thopters, Kappa, Thrummingbird, Tekuthal, Thought Monitor, Inspiring Overseer, Mechanaut, Seedshark, Inspirit at 8+): they count, but none closes alone (review M-2). |
| through_big_creatures | gate, early | 10 | 12 | **16** (90 %) | Spot answers: Tranquilize (three stun counters Kilo keeps topping up), Dispatch, Chaos Warp, Airbending Lesson, Sandbenders' Storm, Firebending Lesson kicked, Barrels of Blasting Jelly ({5}: 5 damage), Lux Cannon (repeatable); North Pole Patrol taps; the two noncombat finishers, Cyberdrive flying, Kappa unblockable, Titan Forge 9/9s, two wipes. |
| evasion | support | 4 | 6 | 9 | Inside through_wide_board. |
| wipe_insurance | support | 2 | 3 | 7 | Inspirit 8+, Darksteel Reactor (indestructible), Hangarback, Emry, Swan Song, Ripples, Buried Ruin; plus 3 indestructible Bridges; every noncreature artifact survives creature wipes with its counters. |
| Ramp | base | 10 | 12 | **9 tags (WARN); about 5 timed** | Timed (review I-2): castable by turn 2 and helping Kilo: Sol Ring, Arcane Signet, Chalice, Prism; Sculptor and Mechanaut at half (they discount artifacts, not Kilo). Cornucopia, Sphere, Solar Array are turn-4 plays. Fixing (not counted as ramp): Barrels of Blasting Jelly, Chromatic Star, Spire, Orchard. Fix: purchase 4 (Talisman of Conviction; fallback Relic of Legends). |
| Draw (nets cards) | base | 10 | 12 | **12** | Insight Engine, Uthros, Sensor (half), Etched Oracle, Gambit, Thirst, Katara (repeatable, half), Universal Surveillance, Waterbending Lesson, Thought Monitor, Jhoira, Inspiring Overseer. |
| Removal (spot) | base | 6 | 8 | **8** + Soul-Guide Lantern (graveyard answer, tagged removal) | Tranquilize, Dispatch, Chaos Warp, Airbending Lesson, Firebending Lesson, Sandbenders' Storm, Barrels (late), Lux Cannon. Answers to opposing commanders: Chaos Warp (tuck), Tranquilize (stun kept up by proliferate), Dispatch (exile), Lux Cannon. |
| Wipes | base | 2 (hybrid takes the higher) | 2 | **2** | Fumigate, Organic Extinction; both near one-sided here (noncreature artifacts survive; Organic spares artifact creatures; Inspirit 8+ makes Fumigate one-sided). |
| Commander protection | base, enabler | 3 | 4 | **4 tags, about 3.25 weighted** | Swan Song 1 (spells only), Airbending Lesson 1 (exile and recast for {2}), Ripples 0.75 (needs a counter on Kilo), Inspirit 0.5 (needs 8). Swiftfoot Boots (extra purchase) makes 5 tags, about 4.25. |
| Graveyard hate | base | 1 | 1 | 1 | Soul-Guide Lantern. |
| Lands | band 36 to 37 | | | **37** | Rule of thumb 31 + 3 colors + MV 3 = 37; timed ramp about 5, so the top of the band. |
| Curve | avg MV band 2.6 to 3.1 | | | **3.15** | MV 0: 3, 1: 7, 2: 11, 3: 19, 4: 14, 5: 2, 6: 2, 7+: 4. Thought Monitor (affinity) and Organic Extinction (improvise) cost less in practice. |
| Creatures | 15 to 28 | | | 26 in the 99 | Plus 2 Vehicles and 2 Spacecraft. |

**Card-flow budget (turns 4 to 8).** Spend: about one card a turn. Gain: natural draw 1, plus Insight Engine (1, 2, 3... per
activation, faster with proliferate), Uthros and Jhoira (1 per artifact spell), Sensor (1 per 2 counters), Katara (1 per
round), Oracle bursts; Chromatic Star replaces itself. Holds.

**Counter rate.** Turn 4: 2 to 4 countered permanents, a Kilo trigger adds 2 to 4 counters, sources add 2 to 3. Turn 6: 5 to
7 countered permanents, about 7 to 10 new counters a turn. Lux Artillery's 30 counters arrive around turns 8 to 10 [J, not
simulated]; Darksteel Reactor alone needs about 7 turns after it lands, 3 to 4 with Tekuthal or Deepglow Skate.

**Dead clauses named.** Thrummingbird's proliferate needs combat damage (weak late); Airbending Lesson lets the opponent
recast the permanent for {2} (best on tokens or expensive permanents); Chain Reaction hits my own creatures too (cast it when
the opponents' boards are wider than mine); Barrels' damage clause costs {5} (a late use). No vehicle, equipment or partner
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
- Etherium Sculptor: turn 2; 37 artifact spells cost 1 less (not Kilo); later a station or crew body. Bad late. Stand-in for Prophetic Prism (purchase 2).
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
- Moxite Refinery: from turn 2 it is a converter; on the closing turn pay {2} and tap it to move X counters from Crystalline Crawler, Hangarback, Etched Oracle, an Incubator or a spent rock onto Darksteel Reactor as charge counters (sorcery speed). Early it can also move charge counters onto Pentad Prism or Lux Cannon.
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
- Resourceful Defense: cast it once Darksteel Reactor or Lux Artillery is on the table; {4}{W} at an opponent's end step moves every counter of one permanent (Inspirit, Uthros, Autogenerator, Titan Forge, a rock) onto the Reactor; when removal or a wipe hits a countered permanent, its counters move onto the Reactor or another engine. The deck's main closing piece next to the Reactor.
- Titan Forge: activate {3},T on spare turns; proliferate fills it; three counters make a 9/9 that blocks Board 2 and attacks.

**Card draw (7 + the draw engines above)**
- Thirst for Knowledge: instant; discard one artifact (a spare rock late, or Lux/Reactor for Emry and Buried Ruin).
- Katara, Bending Prodigy: at an opponent's end step pay waterbend {6} by tapping Kilo (proliferate) and the artifacts you did not use: a card each round at instant speed; if Katara is tapped at your end step she grows. Bad early (few artifacts to tap).
- Universal Surveillance: improvise with Kilo (proliferate), rocks and artifact lands; X of 4 to 6 on turn 6 or later.
- Waterbending Lesson: draw three; pay waterbend {2} by tapping Kilo (proliferate) and an artifact to keep every card.
- Thought Monitor: affinity makes it 2 to 4 mana for a 2/2 flyer and two cards. Bad early.
- Jhoira, Weatherlight Captain: turn 4; every artifact or legendary spell draws; cast it before a chain of cheap artifacts.
- Inspiring Overseer: turn 3; a card and a 2/1 flyer (station fuel, chump blocker against Board 2). Stand-in for Talisman of Conviction (purchase 4).

**Removal (7 spot + Lux Cannon + graveyard)**
- Tranquilize: on the biggest Board 2 creature or an opposing commander: three stun counters, and every Kilo trigger adds another, so it never untaps while Kilo lives. Sorcery: cast it before the attack.
- Dispatch: from turn 3 (three artifacts) it exiles for one mana; before that it taps an attacker.
- Chaos Warp: any permanent, commanders included (tuck); the answer to enchantments.
- Airbending Lesson: instant: exile a nonland permanent and draw; or exile your own Kilo in response to removal and recast it for {2} with haste.
- Firebending Lesson: 2 damage to a utility creature early; kicked, 5 damage late. Stand-in for Volt Charge (purchase 1).
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
- Ovalchase Dragster: crew 1 with Kilo (proliferate); a 6/1 trample haste attacker when a lane is open; flies with Cyberdrive. Bad against pingers. Stand-in for Swiftfoot Boots (extra).

**Lands (37)**
- Untapped duals: Adarkar Wastes, Shivan Reef (pain lands); Sulfur Falls, Glacial Fortress, Clifftop Retreat (check lands: play after a basic); Radiant Summit (untapped with two basics); Rugged Prairie, Cascade Bluffs, Skycloud Expanse (filters: need another colored mana, so count them as colorless until then).
- Any color: Exotic Orchard (depends on opponents), Spire of Industry (with an artifact, 1 life).
- Utility colorless: Karn's Bastion ({4},T proliferate, also on opponents' turns), Buried Ruin (return Lux or Reactor).
- Artifact lands: Ancient Den, Great Furnace, Seat of the Synod (untapped; metalcraft, improvise, Surge Conductor); Silverbluff, Razortide, Rustvale Bridge (tapped, indestructible artifacts).
- Mystic Monastery, Path of Ancestry: tapped tri-color lands; play them on turn 1 or a turn with spare mana.
- Basics: 7 Island, 4 Plains, 5 Mountain (all Spanish; the fifth Mountain is the stand-in for Command Tower, purchase 3).

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
| Threefold Thunderhulk (step 6) | combat closer, counter source | sources 22 (12) | 7 MV, bad early; Chain Reaction (third wipe) takes the slot; the combat route keeps Cyberdrive, Titan Forge and Kappa. |
| Depthshaker Titan (step 6) | combat closer (trample, haste) | through_wide 16 (10) | 7 MV, bad early; Resourceful Defense (Reactor funnel) takes the slot. |
| Mindless Automaton (step 6) | counter source, draw | draw 12 (10) | Slow; Moxite Refinery (Reactor funnel) takes the slot. |
| Gavel of the Righteous (EOC) | counter source, equipment | sources 23 (12) | Little value on Kilo. |
| Alibou, Ancient Witness (EOC) | haste for artifact creatures, single-target damage | through_big 16 (10) | 5 MV, single target; Cyberdrive covers that board haste. |
| Angel of the Ruins (EOC) | artifact/enchantment removal, 7 MV | removal 8 (6) | Chaos Warp and Lux Cannon do it cheaper. |
| Cloud Key (EOC) | cost reducer | ramp 9 (10, WARN) | A turn-3-to-4 play like Sphere, with less output. |
| Command Tower (EOC) | land | lands 37 | All three copies are in Toph, Azula and Ezio; purchase 3 (PayToWin copy for Ezio, his Spanish copy to Kilo). |
| Temple of Enlightenment, Irrigated Farmland, Lonely Sandbar, Secluded Steppe, Evolving Wilds (EOC) | tapped lands | lands 37 | Already 5 tapped lands; untapped lands and basics preferred. |
| Planar Cleansing | wipe | wipes 3 (2) | Destroys my own artifacts. |
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
| Command Tower | 3, in Toph, Azula and Ezio | | those three | owner 2026-11-07: a PayToWin copy (900, counted in Kilo's cap) goes to Ezio and Ezio's Spanish copy moves to Kilo when it arrives; the list keeps the fifth Mountain until then |

Round-3 additions (Barrels of Blasting Jelly, Chromatic Star, a fifth Spanish Mountain) are wanted by no other deck. No
conflict: Sol Ring, Arcane Signet, Exotic Orchard, Sulfur Falls, Clifftop Retreat, Rugged Prairie, Shivan Reef, Cascade
Bluffs, Chaos Warp, Sandbenders' Storm, Path of Ancestry (separate physical copies in the assignment).

## 8. Purchases (stores: Game of Magic Singles, PayToWin, Tienda La Comarca; Spanish copies; Kilo's cap 7,000 CLP)

Sources: the live readings of 2026-11-07 (`data/prices/browser-gameofmagic-20261107-wishlist.psv`,
`data/prices/browser-paytowin-20261107-wishlist.psv`, the La Comarca rows of `data/prices/20261107T2140Z.json`) and the lead's
script reads of over-cap cards (2026-11-07, nine stores). A card outside those reads is **price to read**: the lead reads it
by script; its USD price (Scryfall, 2026-11-07) is a hint only. Re-verify stock within 24 hours of buying. The list file keeps
each stand-in until the card arrives (`assign_copies.py` has no notion of purchases).

### Why the closer changes (step 6, second pass)
Commander Salt scored the Reactor funnel list 3.8 owned and 3.8 after purchases ("control without a finisher", combos: none):
Salt credits combos it finds in Commander Spellbook, not counter funnels. I searched the local Spellbook cache
(`data/cache/spellbook_variants_slim.jsonl.gz`) for every variant inside {U}{R}{W} whose cards are owned Spanish copies plus
the planned buys, with one card missing. Two lines are completed by ONE cheap Spanish card and reuse cards the deck already plays:

| Line | Pieces (owned in **bold**) | Spellbook | What it does |
|---|---|---|---|
| **A, the main closer** | Meticulous Excavation + **Lux Artillery** + **Crystalline Crawler** | 1034-1350-2060, "Infinite artifact ETB, infinite colored mana" | With Lux Artillery out, Crawler cast with four colors enters with 8 counters (converge 4 + sunburst 4); remove them for 8 mana of any color, pay {2}{W} to return Crawler with Excavation, recast it for 4: +1 mana per loop, infinite mana and infinite artifact entries during your turn. **Win:** each entry makes **Reckless Fireweaver** deal 1 to each opponent (infinite damage to the whole table); or **Surge Conductor** proliferates on each entry (infinite proliferate: **Darksteel Reactor** wins); or the infinite mana goes into **Etched Oracle** (each opponent draws out). Late, three cards plus a payoff the deck already plays. |
| B, the second line | Voltaic Construct + **Cyberdrive Awakener** + **Empowered Autogenerator** / **Astral Cornucopia** / **Everflowing Chalice** | 198-1978-2734, 1978-2593-2734, 1978-2734-4563 | On the Cyberdrive turn the rocks are artifact creatures, so Voltaic Construct ({2}: untap target artifact creature) untaps a rock that taps for 3 or more: infinite mana; it also untaps the animated Lux Cannon (destroy every opposing permanent), Insight Engine (draw) or Titan Forge (9/9s). Late (Cyberdrive costs 6). |

Both pass the bracket check (scratchpad run of the full post-purchase list: PASS, floor 1, 0 Game Changers, Spellbook: 4
variants inside the list, none flagged). Rejected: **Filigree Sages** (Spellbook pairs it with Astral Cornucopia or Empowered
Autogenerator as a TWO-card infinite: the bracket check gives floor 4, an early two-card infinite, so it breaks a Bracket 3
rule). Not buyable in Spanish: Aura of Dominion (none in nine stores), Freed from the Real, Pemmin's Aura, Sinking Feeling, so
Relic of Legends completes no combo.

### Inside the cap (re-ranked; the owner's approved 7,000 list had Relic of Legends instead of ranks 1 and 5)

| Rank | Card (Spanish) | Store, price | Need it fills | Replaces (stand-in now) | Fallback |
|---|---|---|---|---|---|
| 1 | **Meticulous Excavation** | price to read (0.18 USD; Spanish printing: The Brothers' War) | Completes line A with owned Lux Artillery and Crystalline Crawler: the closer Salt can see; also returns a threatened permanent to hand in response to removal (my turn only) | Chromatic Star | Relic of Legends (La Comarca 2,600): no combo, but ramp and an instant Kilo tap |
| 2 | Volt Charge | Game of Magic Singles, 400 (ONE, NM ES) | Instant removal plus proliferate; clears the `counter_doublers` WARN | Firebending Lesson | keep Firebending |
| 3 | Generous Gift | PayToWin, 2,100 (WOC, NM ES) | Instant answer to any permanent (interaction is Salt's lowest pillar) | Brute Suit | keep Brute Suit |
| 4 | Prophetic Prism | Game of Magic Singles, 400 (ONE, NM ES); PayToWin 900 (ROE, LP ES) | Fixing every turn plus a card | Etherium Sculptor | the PayToWin copy |
| 5 | **Voltaic Construct** | price to read (2.50 USD; Spanish printing: Darksteel) | Completes line B with owned Cyberdrive Awakener and rocks | Hangarback Walker | Muddle the Mixture (PayToWin 3,000, ES): a counterspell whose transmute finds an MV-2 card (Pentad Prism, Moxite Refinery, Volt Charge), if the cap allows; else keep Hangarback Walker |
| 6 | Talisman of Conviction | Game of Magic Singles, 1,500 (TDC; verify Spanish at purchase) | Turn-2 R/W rock; Kilo on turn 3 | Inspiring Overseer | keep Inspiring Overseer |

**Total inside the cap:** 400 + 2,100 + 400 + 1,500 = 4,400 CLP verified, plus Meticulous Excavation and Voltaic Construct at
their read prices (hints: about 200 and 2,400 CLP), about **7,000**. If the reads come in higher, drop rank 6 (the Talisman)
before rank 5. **Why Relic of Legends leaves the cap:** its four Kilo combos all need an Aura (Freed from the Real, Pemmin's
Aura, Sinking Feeling) that no chosen store has in Spanish; alone it is a 3-mana rock. Excavation and Voltaic Construct turn
cards the deck already plays into two Spellbook combos for about the same money.

**Separate lines (outside the cap):** Command Tower (PayToWin 900, C17 LP ES; owner's plan: that copy to Ezio, Ezio's Spanish
copy to Kilo) for the fifth Mountain; Swiftfoot Boots (PayToWin 2,200, C14 LP ES) for Ovalchase Dragster.

**The post-purchase list** = this list with Meticulous Excavation for Chromatic Star, Volt Charge for Firebending Lesson,
Generous Gift for Brute Suit, Prophetic Prism for Etherium Sculptor, Voltaic Construct for Hangarback Walker, Talisman of
Conviction for Inspiring Overseer, Swiftfoot Boots for Ovalchase Dragster and Command Tower for the fifth Mountain. Checked in
the scratchpad (`kb-both.txt`): 100 cards; bracket PASS, floor 1, 0 Game Changers; Spellbook 4 combos inside, 0 flagged.
**Measure this version on Commander Salt.**

### Strong buys that do NOT fit the cap (price and expected gain)

| Card (Spanish) | Price | Expected gain | Would replace |
|---|---|---|---|
| Eternity Vessel | price to read (15 USD; Spanish: Zendikar) | Spellbook "win the game" with **Darksteel Reactor** + **Resourceful Defense** (1870-4153-4873): the Vessel enters with charge counters equal to your life (30 to 40), Resourceful Defense (or Moxite Refinery) moves them onto the Reactor: instant win. Alone it also puts Lux Artillery over 30 counters at once. A third Salt-visible combo, all other pieces owned | Titan Forge |
| Dawnsire, Sunstar Dreadnought | price to read (12 USD; Spanish: Edge of Eternities) | Spellbook "win the game" with Darksteel Reactor + Resourceful Defense (4153-4873-6758); a Spacecraft Kilo stations | Deepglow Skate |
| Muddle the Mixture | PayToWin 3,000 (ES); La Comarca 3,350 | Counterspell plus a tutor for MV-2 cards (Pentad Prism, Moxite Refinery, Volt Charge); raises interaction | Hangarback Walker (if Voltaic Construct is not bought) or Chain Reaction |
| Relic of Legends | La Comarca 2,600 (DMU, NM ES) | Ramp and an instant Kilo tap; a combo only with an Aura none of the stores has in Spanish | Brute Suit |
| Arcane Denial | La Comarca 3,950 (WOC, NM ES) | A 2-mana hard counter to protect the combo turn | Chain Reaction |
| Counterspell | only CardNexus, 4,090 ES (not a chosen store) | Same | Chain Reaction |
| Battlefield Forge | PayToWin 2,600 (BRO, NM ES) | Untapped R/W land; one fewer tapped land | Path of Ancestry |
| Tezzeret the Seeker | La Comarca 34,800 (Spanish foil only) | Untaps Kilo, −X puts the Reactor or Lux onto the battlefield | Titan Forge |
| Enlightened Tutor (Game Changer) | 40,990 or more | Finds Meticulous Excavation, Lux, Crawler or the Reactor for {W}: the tutor line A lacks | Thrummingbird |
| Teferi's Protection (Game Changer) | 47,990 or more | Protects the combo turn from any answer or wipe | Ripples of Potential |
| Narset, Parter of Veils / Aura of Dominion | no Spanish copy in any store read | Narset: digs for the combo pieces each turn; Aura of Dominion: Kilo + Pentad Prism or Crawler, a second infinite | |

**If the cap grows:** Eternity Vessel first (a third combo whose other pieces are all in the list), then Muddle the Mixture
and Arcane Denial (protect the combo turn), then Battlefield Forge.

**Optional upgrade path (Freed from the Real + Relic of Legends)** stays a note: Freed has no Spanish copy in the stores.

## 9. WARN reasons and dead clauses

- **Ramp 9 of 10 (WARN), about 5 timed.** The Spanish pool has no further turn-1-to-2 rock (Mind Stone's Spanish copy is in
  Azula). Mitigation: Chalice, Prism and Cornucopia gain mana with every proliferate and Coretapper charges them; Crawler and
  Autogenerator add late mana; Barrels and Chromatic Star fix colors (not counted as ramp). Fix: purchase 4 (Talisman of
  Conviction; fallback Relic of Legends). The tag count stays 9 after the buys because Etherium Sculptor (tagged ramp) leaves
  for Prophetic Prism; timed ramp rises to about 6.
- **counter_doublers reaches 10 only with Kilo (WARN).** Correct after removing North Pole Patrol (review M-1): it untaps Kilo,
  it does not proliferate. The owned pool has no other proliferate card; Kilo is the guaranteed piece, and the 9 others (about
  6.5 weighted) are above the profile's support min 4. Purchase 1 (Volt Charge, 400) clears it: 10 without Kilo. No purchase
  cut takes a card from this function.
- Commander protection meets the floor by tags (4) but is about 3.25 weighted; Swiftfoot Boots (extra) brings it to 5.
- Bad when drawn: 8 early (Cyberdrive, Organic Extinction, Deepglow Skate, Lux Artillery, Kappa,
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
- **Toughness.** Closers ignore toughness (the Reactor, Lux Artillery) or are big (Cyberdrive 4/4 and 4/4 rocks, Titan 9/9s); about 12 of the 26
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
  | + Talisman of Conviction (round 3 model) | 72.2 % / 84.2 % | about 92 % |
  | + Command Tower for the fifth Mountain (round 3 model) | 73.0 % / 85.5 % | about 92 % |
  | Step 4 re-run (5,000 games, Prophetic Prism as a 2-mana converter): this list | 69.5 % / 82.6 % | |
  | + Prophetic Prism and Volt Charge (purchases 1 and 2) | 70.8 % / 84.1 % | |
  | + Talisman of Conviction (purchase 4) | 72.9 % / 85.3 % | |
  | + Command Tower for the fifth Mountain (purchase 3): all buys | 73.8 % / **86.4 %** | |

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

Answered through step 6. Still open:
1. Inside the 7,000 cap I replaced Relic of Legends (2,600, no Spanish combo partner in the stores) with Meticulous Excavation
   and Voltaic Construct (two Spellbook combos with cards already in the list). Accept? Their Spanish prices are to be read.
2. Eternity Vessel (price to read, about 15 USD) would add a third, instant-win combo (with Darksteel Reactor and Resourceful
   Defense, both in the list). Extend the cap for it?
