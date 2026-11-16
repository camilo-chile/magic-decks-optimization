# Kilo, Apogee Mind: the Spanish deck (collection-only optimization, step 13.1, 2026-11-15)

**Fix round (step 13.3, 2026-11-15, the lead on Opus 5.5 high; review `decks/reports/collection-review-spanish-deck-20261115.md`, verdict FIX).** Owner decision: Azula, Toph and Ezio are rebuilt and FROZEN, so Kilo takes no copy from them.

| Out | In | Reason |
|---|---|---|
| Swan Song (Azula's copy, not taken) | Titan Forge (already Kilo's) | Owner's decision; the builder's own fallback. Cost: 2 cheap win-turn shield pieces (Negate, Ripples of Potential) where 3 are wanted, and one counterspell; no free Spanish card fills it. |
| Contentious Plan | Empowered Autogenerator (free Spanish copy) | Grows into 5 to 8 mana a turn; its charge counters can be moved onto Darksteel Reactor. Left out with no reason. |
| Thrummingbird | Hangarback Walker (free Spanish copy) | Counters, an artifact creature and wipe insurance; the missing Thopter token is a token to list, not a reason to cut the card. |

Not applied: the optional Karn's Bastion -> ninth Island swap (+1.1 points to cast Kilo on turn 3). Karn's Bastion is a
repeatable proliferate in a proliferate deck, and Kilo is already castable on turn 3 in about 81 % of games.
Confirmed by the review: the Commander rules of 2026-11-06 (section 903) do not turn off-color mana into colorless, so Lux
Artillery + Crystalline Crawler + Meticulous Excavation is a real three-card infinite (infinite mana; a fourth card such as
Reckless Fireweaver kills), allowed in Bracket 3. Open gap: no tutor reaches Darksteel Reactor or Lux Artillery (one of
them in hand or play in 38 % of games by 21 cards seen). Real power: 5.6 to 6.0 (builder), against 5.1 to 5.5 for the
deck as built. Confidence medium-low.

Fable 5.2 high, under `docs/proposals/collection-optimization-brief-20261114.md`: no purchases, no loans, the collection
frozen as scanned on 2026-11-13. 100 % Spanish copies (basics included), pool `data/model/phase2/pool-spanish-deck.json`
(197 cards; checked against the 322 Spanish rows of `ManaBox_Collection_2026-11-13_purchase.csv`: nothing legal is missing).
The previous version (final rebuild of 2026-11-09, built with 99 cards) is in version control.

**Checks (2026-11-15):**
- 100 cards (1 + 99): 37 lands, 62 nonland, average mana value 2.95. Every card has enough Spanish copies (script over the pool).
- `python scripts/check_phase2_bracket.py decks/phase2/spanish-deck.txt`: **PASS** (floor 1, 0 Game Changers, no extra turns,
  no mass land denial, no reversible card; Spellbook: 1 variant inside the list, 0 flagged).
- `scripts/plan_density.py` (run on this plan only, `run_plan`, so no other deck's report is touched): **PASS**, 0 failures,
  **0 warnings**.

## 0. Three findings that changed the list

1. **Any-color mana is not limited to Kilo's colors.** The 2026-11-09 notes and their review said "mana outside the identity
   becomes colorless", so Crystalline Crawler could never be cast with four colors. That rule left the game in 2016: the
   Comprehensive Rules in force (effective 2026-11-06, section 903, read today) have no such rule, Crawler's own ruling
   (2016-11-08) pays {W}{U}{B}{R}{G}, and Commander Spellbook lists the loop for a mono-white identity. Only Arcane Signet,
   Command Tower, Commander's Sphere and Path of Ancestry are tied to the identity by their own text. Ten cards here make
   black or green mana: Pentad Prism, Relic of Legends, Solar Array, Crystalline Crawler, Astral Cornucopia, Barrels of
   Blasting Jelly, Chromatic Star, Spire of Industry, The Mycosynth Gardens and (if an opponent has those lands) Exotic Orchard.
   - So **Lux Artillery + Crystalline Crawler + Meticulous Excavation is a real three-card infinite** (section 1). It
     needed Surge Conductor as a fourth card only under the wrong rule.
   - Sunburst and converge reach four or five: Etched Oracle draws three the turn it lands, Crawler enters with four
     counters (eight with Lux Artillery).
2. **The mana lost one game in ten to colors.** A color-aware simulation (section 3) gave the deck as built 78.5 % to cast
   Kilo on turn 3, 86.4 % by turn 4 and 90.1 % by turn 5. Path of Ancestry, Rustvale Bridge and The Mycosynth Gardens (for
   Buried Ruin and two basics) raise that to 80.9 %, 90.3 % and 93.4 %, at a cost of 0.12 more "tapped land only" turns a game.
3. **Solar Array was left in the binder.** It is the Talisman's replacement and far more: every artifact cast after tapping
   it enters with one counter per color spent (Reactor with four charge counters, Lux Cannon ready to fire, Insight Engine
   drawing four on its first activation, Chalice kicked twice with six counters).

## 1. Profile

**Commander reading.** Kilo {U}{R}{W}, 3/3 legendary artifact creature, haste: "Whenever Kilo becomes tapped, proliferate."
- Rewards: becoming tapped by ANY means: attacking, Relic of Legends ("tap an untapped legendary creature"), station,
  waterbend, improvise. Fuel: permanents that already carry counters. Window: any time he can be tapped.
- How it wins: it does not; it multiplies. Dependence: **enabler** (13 other proliferate pieces; every closer works without
  him). Mana value 3 with haste: recast for 5, then 7, and he taps the same turn.
- Dead clauses: none on Kilo.

**Rules points to verify.**

| # | Point | Evidence | If wrong |
|---|---|---|---|
| R1 | Tapping Kilo to station triggers him, and the proliferate resolves before the station counters land | Kilo ruling 2025-07-25 | Station still gives the charge counters |
| R2 | Waterbend and Relic may tap a summoning-sick Kilo | North Pole Patrol ruling 2025-10-02; Relic ruling 2022-09-09 | He taps a turn later |
| R3 | Any-color sources make black and green mana in this deck | CR 2026-11-06 section 903 (no conversion rule); Crawler ruling 2016-11-08 | The loop needs Surge Conductor again; sunburst caps at three |
| R4 | Each instance of sunburst counts separately (Lux Artillery + Solar Array + printed sunburst) | Lux Artillery ruling 2023-02-04; Solar Array ruling 2025-07-25 | Fewer counters, no route falls |
| R5 | A cost reduction cannot be ignored to spend more colors | Crawler ruling 2016-11-08 | Enthusiastic Mechanaut takes one counter off sunburst cards: true, see section 2 |
| R6 | The Mycosynth Gardens copies only printed values; a copied X is 0 | Gardens rulings 2023-02-04 | Never copy Chalice, Prism or Cornucopia |
| R7 | Lux Artillery checks 30 counters when the end step begins and again on resolution | Lux Artillery ruling 2023-02-04 | Do not spend Crawler's counters in the end step |
| R8 | Meticulous Excavation only on my turn; a commander returned to hand is recast without tax | Oracle text; tax applies only to casts from the command zone (rules knowledge, not re-read) | Kilo is recast with tax |

**Plan (one sentence).** Kilo is tapped once or twice a round at home (Relic of Legends, station, waterbend; North Pole
Patrol is his only untapper) and Strionic Resonator and Lithoform Engine copy the trigger, so he proliferates the counters
that about 20 rocks, engines and creatures place and that Solar Array and Lux Artillery multiply on entry; the counters
become mana, cards and removal, and the first noncombat finisher reached closes against the whole table.

**Backup.** The same artifact board attacks: Steel Overseer and proliferate grow the artifact creatures, Cyberdrive
Awakener gives one flying alpha strike, Kappa Cannoneer is unblockable, Alibou shoots X at any target on every attack.

**Speed (goldfish, section 5).** Kilo on turn 3 in about 4 of 5 kept hands; engine online turns 4 to 6; first lethal
threat turns 8 to 10; a real kill turns 10 to 12, turn 8 when Solar Array meets the Reactor and a funnel.

**Win routes, scored (R26) and failure points (R28).**

| Route | Closers | Cards / mana on the win turn | Access | Alone? | Fails to |
|---|---|---|---|---|---|
| Darksteel Reactor funnel (alternate) | Reactor + Moxite Refinery, Resourceful Defense or Deepglow Skate | 2 cards; 2 to 5 mana | Reactor 1 card + dig (11 draw pieces, Long-Range Sensor, Emry's mill) | Reactor grows alone | exile or bounce of the Reactor, a counterspell |
| Lux Artillery burn | Lux Artillery, Reckless Fireweaver | 1 card; 0 mana (end step) | Lux + Phyrexian Metamorph and The Mycosynth Gardens as second copies | Lux gives sunburst from the turn it lands | artifact removal, a long clock when not copied |
| Crawler loop (inside the Lux route) | Lux Artillery + Crystalline Crawler + Meticulous Excavation | 3 cards; 7 mana counting Crawler's counters | no tutor; Metamorph can be either artifact | Lux and Crawler are core cards; Excavation is the narrow one | removal in response to the bounce, a counterspell on Crawler |
| Artifact alpha and Alibou (combat) | Cyberdrive Awakener, Kappa Cannoneer, Alibou | 1 card; 6 from lands | 3 cards | Cannoneer and Alibou are threats alone | a fog, a wipe in response, flying blockers |

No failure point is shared by every route. Commander dead: all four still work. A creature wipe: the Reactor, Lux and the
rocks stay. An artifact wipe: section 4. A counterspell: three separate closers plus two counters of my own. Graveyard
exile: no route uses the graveyard. Enchantment removal: only the loop and one funnel.

**How it beats three opponents.** 20 charge counters win outright; Lux Artillery deals 10 to each opponent; Fireweaver pings
each opponent; the loop ends the game on the spot with Fireweaver, Surge Conductor (Reactor to 20), Jhoira, Uthros, Thought
Monitor, Trophy Mage or Etched Oracle on the battlefield or in hand. The single-target pieces (Cannoneer, Alibou) are backups.

**What it fears.** (1) Artifact wipes: Vandalblast, Farewell, Austere Command. (2) Never finding a table-wide closer: only
the Reactor and Lux Artillery are, and nothing in the Spanish pool tutors a mana value 4 artifact (38 % to hold one of the two
in 21 cards, 77 % to hold one of the six closers). (3) Fast combo on turns 5 to 6. (4) Colors: 7 % of games still lack one
on turn 5.

## 2. The puzzle: each card, how to use it, and what it works with

**Mana and fixing (12).** Lands + lasting ramp = 37 + 9 = 46 (R8), lands 80 %.
- Sol Ring: turn 1. Never bad.
- Arcane Signet: turn 2; all three colors for Kilo.
- Everflowing Chalice: kick once on turn 2; every proliferate is one more mana a turn. With Solar Array, kick twice.
- Pentad Prism: turn 2 with two colors; keep one counter so proliferate refills it; its mana can be black or green for
  Crawler and Oracle.
- Relic of Legends: tap Kilo for mana at an opponent's end step: a proliferate each round while he stays home as a blocker.
  Also taps Tekuthal, Jhoira, Emry and Alibou (five legendary creatures and Kilo).
- Commander's Sphere: turn 4 fixer for all three colors; sacrifice it for a card in response to removal.
- Solar Array (new): tap it for the first artifact of the turn, and pay that artifact with as many colors as possible.
  Best targets: Reactor, Lux Cannon, Insight Engine, Chalice, Cornucopia, Uthros (online at once), Inspirit. Trophy Mage target.
- Astral Cornucopia: X=1 on turn 4 after Kilo, or X=1 through Solar Array for four counters. Bad early.
- Crystalline Crawler: cast with four colors when an off-color source is out; taps for a counter each turn; burst mana;
  the loop piece.
- Barrels of Blasting Jelly: turn 1; turns one mana into any color each turn (Kilo on turn 3, a fourth color later); it is
  always untapped for improvise and waterbend; late {5}: 5 damage to a creature. A fixer, not ramp.
- Chromatic Star: turn 1 fixer that replaces itself; with Emry it returns every turn (a card, a Conductor proliferate, a
  Fireweaver ping, a Jhoira or Uthros draw for one mana). The two fixers are worth 3.2 points of turn-3 Kilo together (simulation).
- Enthusiastic Mechanaut: turn 2; 33 artifact spells cost {1} less; a 2/2 flyer that charges Long-Range Sensor and triggers
  Alibou safely. Honest minus (R5): with it out, sunburst cards get one color less and the loop nets no mana (still unlimited
  entries). Do not cast it while holding Crawler and Lux.

**Counter engines (13).**
- Inspirit, Flagship Vessel: station it with Kilo (proliferate first, then three charge counters); each combat a +1/+1
  counter on Kilo or two charge counters on the Reactor; at 8+ every other artifact is hexproof and indestructible.
- Uthros Research Craft: station to 3 (one Kilo tap), then a card per artifact spell.
- Insight Engine: activate at an opponent's end step after the proliferates: 2, 4, 6 cards. Lithoform copies the activation.
- Coretapper: a charge counter a turn (Chalice and Prism early, Reactor, Lux Cannon and Sensor later; on Kilo himself so
  Ripples can phase him out).
- Steel Overseer: +1/+1 on every artifact creature each turn (12 of them and Kilo); the backup route's engine.
- Surge Conductor: a proliferate for every nontoken artifact that enters, artifact lands included. Trophy Mage target.
- Tekuthal, Inquiry Dominus: doubles every proliferate; 3/5 flying blocker; pay its ability before a wipe.
- Thrummingbird: turn 2; early proliferates on Chalice and Prism are permanent mana. Bad late.
- Long-Range Sensor: any attacker charges it (Mechanaut, Thrummingbird, Kilo); with two proliferates a turn it discovers 4
  every turn for {1}.
- Etched Oracle: with four colors it draws three for {1} at once; with Lux Artillery it keeps four counters and a body.
- Patrolling Peacemaker: proliferates whenever an opponent targets another player's things; say so at the table.
- Chrome Host Seedshark: each of the 41 noncreature spells leaves an Incubator with that many counters (Lux counts them,
  Fireweaver pings on each, improvise and waterbend tap them). 2/4 flying blocker.
- North Pole Patrol: untap Kilo after his first tap and tap him again, or untap Insight Engine, Lux Cannon or Sol Ring;
  waterbend {3} (tapping Kilo) taps an attacker.

**Copies (3).**
- Strionic Resonator: {2}: Kilo's proliferate, Lux Artillery's end step (20 each), Deepglow Skate (x4), Alibou's shot,
  the Reactor's upkeep.
- Lithoform Engine: the same for {2}, plus Insight Engine's or Lux Cannon's activation; {4} copies Lux Artillery as it is cast.
- Phyrexian Metamorph: a second Lux Artillery, Surge Conductor or Insight Engine; as Crawler it loops too.

**Finishers and funnels (10).**
- Darksteel Reactor: cast it through Solar Array when possible; then feed it. Hold Swan Song, Negate or Ripples for the
  exile or bounce aimed at it.
- Lux Artillery: cast it early when artifact creatures follow (each enters with a counter per color; a recast Kilo is a 6/6);
  the 30 arrive by themselves.
- Reckless Fireweaver: turn 2; 15 to 20 damage to each opponent over a game; the kill of the loop.
- Meticulous Excavation: the loop; otherwise {2}{W} on my turn re-buys Trophy Mage, Thought Monitor, Deepglow Skate,
  Etched Oracle or a small Chalice, or saves Kilo without tax. Bad early; the narrowest card of the list (section 3).
- Cyberdrive Awakener: pay it from lands; main phase with 8+ untapped noncreature artifacts (artifact lands count).
- Kappa Cannoneer: tap Kilo and idle artifacts for improvise; ward {4}; unblockable on every artifact entry. One player
  at a time: a backup, and a blocker.
- Alibou, Ancient Witness (new): tap the rocks for spells first, then attack with any artifact creature: X damage to any
  target and scry X, X = tapped artifacts (4 to 8). Shoot the blocker before Kilo's attack is blocked. Gives haste to Cannoneer
  and to everything Cyberdrive animates.
- Deepglow Skate: Reactor 10 to 20, Lux's count, Insight Engine, Chalice. Bad early.
- Moxite Refinery: sorcery speed; Inspirit's or Crawler's counters become charge counters on the Reactor, or on Insight
  Engine (draw that many) or Lux Cannon.
- Resourceful Defense: {4}{W} at instant speed moves charge counters onto the Reactor; when an artifact wipe resolves, every
  counter of the destroyed artifacts moves to the indestructible Reactor.

**Card flow (9).**
- Tezzeret's Gambit: two cards and a proliferate; pay 2 life when short of blue.
- Experimental Augury, Contentious Plan: two-mana proliferates that replace themselves; turn 2 with Chalice or Prism out.
- Thirst for Knowledge: instant; discard a spare rock (or Reactor/Lux for Emry).
- Waterbending Lesson: tap Kilo and one artifact for the waterbend: three cards, a proliferate, no discard.
- Universal Surveillance: late: {U}{U}{U} from any-color rocks, X from idle artifacts and Kilo. Bad early.
- Jhoira, Weatherlight Captain: a card per artifact or legendary spell (about 36 of them).
- Thought Monitor: 1 to 3 mana with affinity: two cards and a flying artifact body.
- Trophy Mage: nine targets: Insight Engine (cards), Surge Conductor, Solar Array, Relic of Legends (Kilo's tap), Inspirit
  (protection), Uthros, Sensor, Peacemaker, Sphere.
- Emry, Lurker of the Loch: 1 mana with affinity; recasts Star or Lantern each turn, and a destroyed or discarded finisher.

**Interaction (14).** Section 4.
- Swords to Plowshares, Dispatch (metalcraft from turn 3), Fateful Absence: instant creature answers at 1, 1 and 2.
- Chaos Warp: anything; the answer to enchantments. Airbending Lesson: exile and a card, or save my own Kilo for {2}.
- Volt Charge: 3 damage and a proliferate at instant speed.
- Tranquilize: three stun counters that Kilo keeps topped up: a commander neutralized without changing zone.
- Lux Cannon: through Solar Array it destroys a permanent the turn it lands; then every second turn.
- Swan Song (contested, section 7), Negate: the win-turn shield and the answer to artifact wipes.
- Ripples of Potential: in response to a wipe: proliferate, then phase out everything that got a counter.
- Organic Extinction (improvise; spares my artifact creatures), Starfall Invocation (promise the gift, get Tekuthal back).
- Soul-Guide Lantern: the graveyard answer; otherwise a card.

**Lands (37).** Command Tower; untapped duals Adarkar Wastes, Shivan Reef, Sulfur Falls, Glacial Fortress, Clifftop Retreat,
Radiant Summit; filters Rugged Prairie, Cascade Bluffs; Exotic Orchard, Spire of Industry; artifact lands Seat of the
Synod, Ancient Den, Great Furnace and Rustvale Bridge (new, tapped, indestructible); Karn's Bastion; The Mycosynth Gardens
(new: {1},{T} any color; late it becomes a second Lux Artillery for {4}, a Surge Conductor, an Insight Engine or a Sol Ring);
Mystic Monastery and Path of Ancestry (new) as tapped three-color lands; 8 Island, 6 Plains, 4 Mountain.

**Synergy count (R4).** 44 of 62 nonland cards sit in two or more plan functions or routes, or in one with a second base tag.
**Commander-centric count (R5):** nothing is blank without Kilo (Relic taps five other legends, Patrol untaps engines): 0 of 12.

**Dead clauses and what each conditional card needs (owner's lesson L7, counted in the list).**

| Card | Needs | In the list |
|---|---|---|
| Dispatch, Thought Monitor, Emry, improvise x3, Cyberdrive | artifacts | 33 artifact spells + 4 artifact lands + Kilo |
| Waterbending Lesson, North Pole Patrol | artifacts or creatures to tap | 46 cards (33 artifacts, 4 artifact lands, 9 other creatures) + Kilo |
| Trophy Mage | artifacts of mana value 3 | 9 |
| Relic of Legends (second ability) | legendary creatures | 5 + Kilo |
| Jhoira | historic spells | 36 |
| Steel Overseer, Alibou, Lux Artillery's sunburst | artifact creatures | 12 + Kilo |
| Coretapper, Moxite Refinery, Resourceful Defense | charge-counter users | 9 |
| Deepglow Skate, Tekuthal, Ripples, every proliferate | counters | 19 sources |
| Etched Oracle and Crawler at four colors | black or green mana | 10 sources |
| Meticulous Excavation's loop | Lux Artillery and Crawler | 2 cards + Metamorph (either) + Gardens (Lux): thin, named |
| Path of Ancestry's scry | creatures sharing Robot or Artificer | 5: a dead clause; the land is played for three colors |
| Chrome Host Seedshark | noncreature spells | 41 |

## 3. Curve and ratios

| MV | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|---|
| Cards | 2 | 8 | 15 | 19 | 11 | 3 | 2 | 2 |

Average 2.95 (Thought Monitor, Emry, Kappa Cannoneer and Organic Extinction cost far less in play). Types: 33 artifacts,
21 creatures, 11 instants, 7 sorceries, 2 enchantments, 37 lands (4 artifact lands).

| Function | Min | Count | Reason |
|---|---|---|---|
| Lands | band 36 to 37 (counters + artifacts) | 37 | Karsten: 31.42 + 3.13 x 2.95 - 0.28 x 10 cheap pieces = 37.9; three colors and many sinks |
| Lands + lasting ramp (R8) | 46 | 46 | 9 rocks; four of them grow with proliferate |
| Ramp by tag / cast by turn 3 | 10 | 12 / 5 | Sol Ring, Signet, Chalice, Prism, Mechanaut by turn 3; the pool has no other 2-mana rock in Spanish. Kilo costs 3, so Karsten asks for no rocks at all; the rocks here are fuel |
| Always-tapped lands (R10) | at most 3 | 3 | Monastery, Path, Rustvale: each brings colors the basics cannot |
| counter_sources (gate, early) | 12 | 19 + Trophy Mage | Kilo only multiplies |
| counter_doublers (promoted to gate) | 10 | 13 + Kilo + Trophy Mage | 8 repeatable, 6 one-shot (11 weighted) |
| counter_payoffs (gate, late) | 6 | 15 | |
| kilo_tap_outlets (custom, late) | 6 | 8 + Kilo + Trophy Mage | 4 repeatable: Relic, Inspirit, Uthros, Patrol |
| artifact_density / payoffs | 20 / 10 | 37 + Kilo / 21 | |
| Through a wide board / big creatures | 10 / 10 | 13 / 15 | Fireweaver counts half; Volt Charge is not counted against big creatures |
| Draw that nets cards | 10 | 10 | Uthros, Insight Engine, Sensor, Oracle, Gambit, Thirst, Lesson, Surveillance, Jhoira, Monitor. Augury, Plan, Star and Sphere are not counted |
| Spot answers (R19) | 8; 5 at MV<=2; 5 instants | 10; 6; 8 | plus Alibou, Patrol and Barrels as second roles; Lantern is graveyard hate, not counted |
| Counterspells (R20) | 2 to 4 (tap-out engine deck) | 2 | Swan Song, Negate |
| Wipes (R21) | 2 | 2 | both spare most of my board |
| Commander protection (enabler) | 3 | 5 | Airbending Lesson, Ripples, Inspirit, Swan Song, Negate |
| Win-turn shield (R24) | 3 at MV<=2 | 3 | Swan Song, Negate, Ripples |
| Rebuild (R32) | 4 | 6 | Kilo with haste, Emry, Resourceful Defense, Ripples, the Reactor, Inspirit at 8+ |
| Tutors (R18) | 10 access cards | 1 tutor | NOT met: section 10 |
| Graveyard hate | 1 | 1 | |

**Fit check.** The minimums, each card counted once: counter sources 12, doublers +8 (the rest are shared), ramp +6 (four
rocks are sources), draw +6, removal +6, wipes +2, protection +1, closers +6 = about 47 of the 62 nonland slots; lands 37.
It fits, with no second package.

**Mana in detail.**
- Pips: blue 30 on 27 cards, white 14 on 12, red 9 on 9. Kilo and Inspirit need all three.
- Colored land sources (Exotic Orchard at 0.75): **blue 18.75, white 17.75, red 16.75**. Rocks add Signet, Sphere, Prism,
  Relic and Solar Array (about +2.5 each by Karsten's weights): about 21, 20 and 19.
- Karsten's 99-card table (41 lands; scaled by 37/41): a gold three-drop asks 19 of each color (17 scaled): met. Tekuthal
  ({2}{U}{U}) asks 26 (23.5): short by two, so he is a turn-5 card. Starfall ({3}{W}{W}) asks 23 (21): at the line.
  Universal Surveillance ({U}{U}{U}) is a late card paid by any-color rocks.
- Untapped: 34 lands never enter tapped by their own text; Sulfur Falls, Glacial Fortress and Clifftop Retreat need a basic
  type (18 basics and Radiant Summit), Radiant Summit needs two basics, Spire of Industry needs an artifact for colors.
- **Kilo on time, with colors** (my simulation, 60,000 games, Exotic Orchard gives each color 80 % of the time):

| Model | Turn 3 | By turn 4 | By turn 5 |
|---|---|---|---|
| This list: free mulligan, rocks and fixers, best land order (upper bound) | **80.9 %** | **90.3 %** | **93.4 %** |
| Deck as built, same model | 78.5 % | 86.4 % | 90.1 % |
| This list: lands only, any 2 to 5 land hand, simple land order (lower bound) | 60.9 % | 72.4 % | 79.2 % |
| Deck as built, same model | 59.3 % | 67.3 % | 73.7 % |

- Cost of the two extra tapped lands: 0.21 turns a game where the only land to play is tapped, against 0.09; average
  untapped land mana on turns 2 to 6 falls by 0.00 to 0.04. Five tapped lands would add about 1 to 2 points by turn 5 for
  0.15 more such turns a game: refused (R10).
- Keepable: 63.4 % on the first seven (3 to 5 lands, or 2 with a rock or fixer of mana value 2 or less), **92.8 % with the
  free mulligan** (second seven: any 2 to 5 lands).

**WARN reasons.** None raised. Two notes the gate does not see: timed ramp is 5, and the Crawler loop inside the Lux route
is three specific cards with no tutor (about 2 to 3 % of games by turn 10): it is a bonus, never the plan.

## 4. Interaction plan and protection plan

- **Answers kept for**: commanders and engines that beat me (Swords, Chaos Warp, Tranquilize); combo pieces at instant speed
  (Swords, Dispatch, Fateful Absence, Volt Charge, Chaos Warp, Airbending Lesson: six on an opponent's turn); artifacts and
  enchantments (Chaos Warp, Airbending Lesson, Lux Cannon; Negate and Swan Song on the stack); a repeatable shot from Alibou.
- **Stack**: Swan Song ({U}) and Negate stop the wipe (Vandalblast, Farewell, Austere Command and Cyclonic Rift are all
  sorceries or instants) and protect the Reactor turn from a counterspell.
- **Artifact wipe plan**, in order: counter it; Ripples in response (everything with a counter phases out); Inspirit at 8+;
  Resourceful Defense moves every lost counter onto the Reactor, which often wins on the spot; Emry and a hasty Kilo rebuild.
- **Protection of Kilo (enabler)**: he stays home. Airbending Lesson and Ripples (he needs a counter: Coretapper, Overseer,
  Inspirit or a Lux-era recast) answer removal; otherwise recast him.
- **Win-turn shield (R24)**: hold {U} or {1}{U} on the turn the Reactor reaches 20, Lux fires or the loop starts. Bait with
  a draw spell first. Never cast the Reactor or Lux the turn before the shield is up, unless Solar Array makes it win next upkeep.
- **Threat posture (R30)**: rocks and small engines look harmless; the visible pieces are the Reactor and Lux. Kilo taps
  at instant speed and the funnels (Resourceful Defense, Strionic, Lithoform) act at instant speed.
- **Politics**: Fateful Absence's Clue, Swan Song's Bird and Starfall's gift go to the player who is not the leader. Offer
  Tranquilize, Chaos Warp and Alibou's shot as table answers before using them for myself.

## 5. Mulligan, play pattern and test pass

**Keep checklist (R33).** Keep 3 to 5 lands, or 2 with Sol Ring, Signet, Prism, Chalice, Barrels or Star, when the hand has
a play by turn 3. Ship 0 to 1 landers, 6+ landers, 2-landers with no cheap mana, and hands of two colors with no fixer.
Keep almost any land-good hand with: Sol Ring, Solar Array, Insight Engine, Surge Conductor, Inspirit, Pentad Prism.

**20 seeded hands** (seeds 1 to 20 of the final list): 11 kept on the first seven (2, 4, 5, 6, 8, 9, 14, 15, 18, 19, 20);
9 shipped (five 0 to 1 landers; four 2-landers with no cheap mana). Their second sevens (seed + 1000): 7 kept, 2 go to
six cards (a 1-lander and a 6-lander). **18 of 20 at seven cards (90 %)**; the 60,000-hand figure is 92.8 %.

**Goldfish (seeds 101, 103, 104, 107, 108; seeds 102, 105 and 106 are 1-landers and were shipped).**

| Seed | Kilo | Engine online | First lethal threat | Note |
|---|---|---|---|---|
| 101 | T3 | T5 (Emry + Star, Prism, Fireweaver) | after T12 | No closer in 26 cards; Alibou on T9. The closer-light game |
| 103 | T3 | T5 to T6 (Sensor discovers each turn, Trophy Mage for Insight Engine) | T10 to T11 | Skate in hand, no Reactor or Lux in 30 cards |
| 104 | T3 | T5 (Reactor T4, Conductor T5, Sensor T6) | T8 (Reactor at 13) | **Reactor wins in the T10 upkeep** with no funnel |
| 107 | T3 | T6 | T12+ | No rock, Peacemaker the only counters until Lux on T9 |
| 108 | T5 | T5 (Lux T4, Kilo enters as a 6/6) | T10 | Two Mountains and a colorless land; Prism's any-color mana casts Kilo |

Summary: Kilo on turn 3 in 4 of 5; kill turn 10 in the good game, turns 11 to 13 otherwise. The weakness is closer
access, as before; the mana no longer is.

**Disrupted goldfish (R38).**
- (a) Kilo removed at his first tap: recast for 5 with haste next turn. Surge Conductor, Tekuthal, Peacemaker and the spells
  keep one to three proliferates a turn. One turn lost.
- (b) Creature wipe on turn 6: the Reactor, Lux, Insight Engine, the rocks and their counters stay; Ripples first if held.
  Threatens again in one turn. An artifact wipe that resolves costs 3 turns, unless Resourceful Defense is out.
- (c) First win attempt countered (the Reactor): Emry recasts it, or switch to Lux or the alpha. Two turns.

**Play pattern.**
- Turns 1 to 5: a fixer or tapped land on turn 1, a rock or counter two-drop on turn 2, Kilo on turn 3 (an engine first
  when no counter is out yet and the hand has Insight Engine or Solar Array), then an engine a turn. Tap Kilo at home unless a
  lane is empty.
- Turns 6 to 9: the Reactor or Lux with the shield up; Solar Array on the best artifact every turn; Insight Engine at end
  steps; Alibou's shots keep the board clear.
- Late: Skate with Strionic on the Reactor, Gardens as a second Lux, the Cyberdrive alpha from land mana, the loop. Commit
  what wins in two turns; keep one closer in hand when two opponents can wipe.

**Gauntlet (R39).**
1. Fast combo: six instant answers and two counters; weak to a turn-4 win.
2. Stax and taxes: the Reactor, Lux and Fireweaver ignore attack taxes; Chaos Warp, Airbending Lesson and Lux Cannon remove the piece.
3. Go-wide tokens (Board 1): never attack into it; Organic Extinction, Starfall, Lux, the Reactor, Fireweaver, flyers.
4. Big creatures (Board 2): ten spot answers, Alibou every turn, Tranquilize, Patrol; the noncombat closers ignore them.
5. Control: instant-speed pieces, three kinds of closer, six rebuild pieces, two counters for the key turn.

**Final cut pass (the 10 weakest nonland cards and the best free candidate for each).**

| Weak card | Best free candidate | Result |
|---|---|---|
| Meticulous Excavation | Hangarback Walker | Keep: the only compact infinite in the pool. Open question for the reviewer |
| Thrummingbird | Etherium Sculptor | Keep: a second reducer breaks the loop's mana and shrinks sunburst (R5 above) |
| Contentious Plan | Titan Forge | Keep: a turn-2 play that digs; Titan Forge is the slowest card of the old list |
| Chromatic Star, Barrels | Etherium Sculptor | Keep: 3.2 points of turn-3 Kilo |
| Commander's Sphere | Mind Stone (Azula's) | Keep: section 6 |
| Enthusiastic Mechanaut | Hangarback Walker | Keep: Hangarback's Thopter token is not owned |
| Kappa Cannoneer | Depthshaker Titan | Keep: Titan sacrifices the rocks and costs 7 |
| Universal Surveillance | Divination | Keep |
| Moxite Refinery | Golem Foundry | Keep: funnel, and a draw-X with Insight Engine |
| Starfall Invocation | Chain Reaction | Keep: {R}{R} on 16.75 red sources |

## 6. The owner's cards

| Card | Verdict | Reason |
|---|---|---|
| **Commander's Sphere** (Kilo holds the Spanish copy) | **IN** | His point holds here. It makes all three colors in a deck that still misses one in 7 % of games by turn 5, it is the ninth lasting rock (R8), Trophy Mage finds it, and it turns into a card under removal. It is not a turn-3 play: Kilo is |
| **Waterbending Lesson** | **IN** | His question, counted: 46 of the 99 cards (33 artifacts, 4 artifact lands, 9 other creatures) and Kilo can be tapped for it, against 13 in Azula. By turn 5 the board holds four to six of them, and tapping Kilo for the waterbend is a proliferate. Here it reads "draw three and proliferate" for four mana, better than Tezzeret's Gambit |
| **Alibou, Ancient Witness** | **IN** (free Spanish copy; for Titan Forge) | X counts tapped artifacts and this deck taps four to eight every turn before combat. It kills a creature a turn or burns a player, lets Kilo attack safely, and gives haste to the Cyberdrive turn. Its cost is real, so it replaces a slower mana value 3 card, not a cheap one |
| **Evie Frye** (Ezio holds the only copy) | **OUT** | Alone she is a looter, which is selection and not draw; her partner Jacob Frye is English and stays in Ezio, where the pair draws. Insight Engine and Uthros do the job in Kilo |
| **Torrential Gearhulk** (Azula holds the only copy) | **OUT**, not contested | Kilo has 11 instants; Azula has about 30 and copies the recast. An artifact body is welcome, but the card adds more there, and he calls it his best Azula card |
| **Aether Gale** (Azula holds the only copy) | **OUT**, not contested | It clears blockers for an attack; Kilo's closers do not attack. Organic Extinction does the board job |

The other cards of the review cannot be played here: no Spanish copy (Frostcliff Siege, Imprisoned in the Moon, Mana Leak,
Mystical Teachings, Return the Favor, Lydia Frye, Tome of Legends, Deadeye Navigator, The Stasis Coffin, Jacob Frye, Royal
Assassin, Hardened Scales) or outside {U}{R}{W} (Merciless Harlequin, The Revelations of Ezio, Mortify, Utter End,
Inscription of Abundance).

**The four stand-ins of the previous build.**
- Sandbenders' Storm (for Counterspell): **OUT**; Swan Song takes the counter's slot.
- Kappa Cannoneer (for Prologue to Phyresis): **stays on merit** as a combat closer and a Kilo tap.
- Thrummingbird (for Flux Channeler): **stays on merit**, the cheapest repeatable proliferate.
- Enthusiastic Mechanaut (for Tribute Mage): **stays as a reducer**; the plan file no longer calls it a tutor.

## 7. Copies

**Contested (the lead decides): Swan Song**, one Spanish copy, held by Azula.

| | Kilo | Azula |
|---|---|---|
| What it does | Second counter of the deck and third piece of the win-turn shield (R24 asks three); for {U} it stops the artifact wipe that ends Kilo's game and the counterspell on the Reactor | One of four counters (Spell Pierce, Negate, Mana Leak) in a shield of eight pieces |
| Without it | Shield 2, counters 1, five spot answers at MV<=2 becomes the bare minimum | Shield 7, counters 3 + fallback |
| Fallback | Titan Forge (in the deck today: nothing moves) | It'll Quench Ya! (English, 3 free), written in Azula's review M6 |

It adds more in Kilo. The lead already gave it to Kilo on 2026-11-02 (`owner-decisions.md`, scarce-copies table).

**Not contested.** Mind Stone (Azula: a 2-mana rock is worth more to a mana value 4 commander; Kilo takes Solar Array), Pull
from Tomorrow, Torrential Gearhulk and Aether Gale (Azula), Path to Exile, Battlefield Forge and Planar Outburst (Toph), Evie
Frye and Arbaaz Mir (Ezio). Negate and Thirst for Knowledge: Kilo keeps its own copy; Azula's second copies are not needed.
Reckless Fireweaver stays in Kilo.

**Free copies that run short.** Solar Array, Alibou, The Mycosynth Gardens, Rustvale Bridge: one free Spanish copy each,
wanted by no other deck. Path of Ancestry: one Spanish copy, free (Ezio plays an English one). Basics: 8 of 11 Spanish
Islands, 6 of 14 Plains, 4 of 16 Mountains.

**Language.** Every card is Spanish. Tokens: Golem 9/9 is no longer needed; Incubator and Clue are owned; Swan Song's Bird is
not owned (it goes to an opponent; Azula has the same gap); Lithoform and Metamorph need only a Copy marker (owned).

## 8. Changes against the deck as built today (99 cards)

| OUT (back to the Spanish binder) | Function, count after | IN | From | Reason |
|---|---|---|---|---|
| (the empty slot of Talisman of Conviction) | ramp 12 by tag | **Solar Array** | Spanish binder | Rock and sunburst engine (finding 3) |
| Sandbenders' Storm | spot answers 10, protection 5 | **Swan Song** | Azula (contested) | A 4-mana conditional answer for a 1-mana counter |
| Titan Forge | combat route 3 closers; counter sources 19 | **Alibou, Ancient Witness** | Spanish binder | Three {3} activations per Golem against a shot every turn |
| Buried Ruin | rebuild 6 (Emry stays) | **The Mycosynth Gardens** | Spanish binder | Fixes colors (+1.5 points by turn 4) and becomes a second Lux Artillery |
| 1 Island | blue 18.75 | **Path of Ancestry** | Spanish binder | Three colors in one land |
| 1 Mountain | red 16.75 | **Rustvale Bridge** | Spanish binder | Red and white, an indestructible artifact land |

Six in, five out, 100 cards. Everything else stays: the engine is the one he owns, and each remaining slot was checked
against the free Spanish cards (section 5, cut pass).

**Considered and left out** (free Spanish copies): Hangarback Walker (good; its Thopter token is not owned; first in line),
Etherium Sculptor (R5), Wake the Past (returns Chalice, Prism and Cornucopia with no counters), Depthshaker Titan and
Threefold Thunderhulk (7 mana), Mindless Automaton (Etched Oracle draws more), Empowered Autogenerator, Golem Foundry, Cloud
Key, Brute Suit and Katara (cut by the last review), Chain Reaction, Fumigate, Angel of the Ruins, the other Bridges and the
Temples (R10).

## 9. Real-power estimate

| List | Real power (1 to 10) |
|---|---|
| Precon Counter Intelligence | 4.0 to 4.5 |
| Deck as built today (99 cards, four stand-ins; Salt 4.2 on 2026-11-15) | 5.1 to 5.5 |
| **This list** | **5.6 to 6.0**, confidence medium-low (no game played with any Kilo list) |

Why higher: Kilo on time 2 to 4 points more often; Solar Array; a real three-card infinite and four- and five-color
sunburst; a third shield piece; a repeatable shot; a land that doubles Lux Artillery. Why not more: two table-wide closers
with no tutor, no Game Changer, no fast mana beyond Sol Ring and Signet in Spanish. Salt was not measured; expect about
the same as before or slightly higher (the combo it credits is unchanged, two more tapped lands).

## 10. Knowledge used

**The skill and `archetypes.json`.** Hybrid `plus_one_counters` + `artifacts` (plan), band 36 to 37, every gate function
declared under its profile name; `counter_doublers` kept promoted; support lines reported; steps 1 to 15 answered in
sections 1 to 5; references read in full (role-players, plan-file, probability, mana-and-ramp, card-flow, interaction,
win-routes, multiplayer, evaluation, tools). Mis-tags fixed against the old plan file: Mechanaut was a "tutor", Cannoneer
and Lithoform carried "draw", Augury, Plan, Star and Sphere counted as draw.

**The champion addendum, 41 items.**

| # | Item | Status | Where |
|---|---|---|---|
| 1 | One plan and a backup | Applied | 1 |
| 2 | Synergy density | Applied | 2; 0 plan cards outside a function |
| 3 | Redundancy and diversity | Applied | 19 sources, 13 doublers; closers on artifacts, an enchantment and a land |
| 4 | Multi-role slots | Applied | 44 of 62 |
| 5 | Commander-centric balance | Applied | 0 blank without Kilo |
| 6 | Land count | Applied | 37 |
| 7 | Colored sources, joint colors | Applied | 3, simulation |
| 8 | Total mana sources | Applied | 46, lands 80 % |
| 9 | Non-GC fast mana | Partly | Sol Ring, Signet; no other owned in Spanish |
| 10 | Tapped lands | Applied | 3, each justified, cost measured |
| 11 | Window mana | Applied | Relic and Insight Engine at end steps |
| 12 | Curve | Applied | 2 / 8 / 15 / 19 / 11 / 3 / 2 / 2 |
| 13 | Commander cost and tax | Applied | recast 5 with haste |
| 14 | Lands at higher power | Applied | 37 against the Bracket 4 average 35: no fast mana |
| 15 | Engines over one-shots | Applied | Insight Engine, Uthros, Jhoira, Sensor |
| 16 | Table-scaling draw | N/A | none in the Spanish pool; Peacemaker scales its proliferates |
| 17 | Development first | Applied | draw on turns 2 to 3 costs 2 or is an engine; Gambit is the exception (two cards and a proliferate) |
| 18 | Tutors, 10 access cards | **Not applied** | no tutor for a mana value 4 artifact exists in the pool; one tutor (Trophy Mage), copies of Lux instead |
| 19 | Cheap instant answers | Applied | 10 spot, 6 at MV<=2, 8 instants |
| 20 | Counterspells | Applied | 2 |
| 21 | Asymmetric wipes | Applied | Organic Extinction, Starfall |
| 22 | Graveyard hate | Applied | Lantern |
| 23 | Layered commander protection | Applied | 5 pieces, three kinds |
| 24 | Win-turn shield | Applied | 3, if Swan Song is granted |
| 25 | Answers by permanent type | Applied | 4 |
| 26 | Compact routes | Applied | Reactor 2 cards, Lux 1, loop 3 |
| 27 | Two disjoint routes | Applied | 3 |
| 28 | Failure points | Applied | 1 |
| 29 | Threat assessment | Applied | 1, 5 |
| 30 | Archenemy timing | Applied | 4 |
| 31 | Politics | Applied | 4 |
| 32 | Wipe recovery | Applied | 6 pieces |
| 33 | Mulligan standard | Applied | 92.8 %; 18 of 20 |
| 34 | Game Changer slots | N/A | 0 of 3: none owned in Spanish (pool flag checked) |
| 35 | Efficiency | Applied | every MV 5+ card wins, answers several or refills |
| 36 | Non-GC high-power cards | Applied | Swords in; Swan Song contested; Path to Exile is Toph's |
| 37 | Combos and Bracket 3 | Applied | three-card loop, script PASS; no Scepter |
| 38 | Goldfish protocol | Applied | 5 |
| 39 | Gauntlet | Applied | 5 |
| 40 | Cut process | Applied | 5, 8 |
| 41 | Real-game evidence over a score | Applied | 9; Salt not chased |

38 applied or partly, 1 not applied (18), 2 not applicable (16, 34).

**The mana study (`notes/02`, `notes/13`).** Karsten's regression gives 37.9 lands; his source table gives 19 per color for
a gold three-drop; his rock weights and "no rocks for a mana value 3 commander" are in section 3; notes/02's warning that
no source prices tapped lands in Commander is why I measured it.

**The other notes.** 01 (one plan; a card's value depends on the turn: Cornucopia and Skate marked bad early); 03 (draw
that nets cards: 10; tutors apart); 04 (spot and wipes apart; one-sided wipes; layers); 05 and 11 (team-wide finishers;
commit when ahead); 07 and 10 (counters: several sources, doublers, payoffs; "one source is a trap"); 08 (ten games cannot
rank lists: the goldfish finds failures only); 09 (EDHREC as a prior); 06 and 12 (combat: only the backup route uses them;
flyers and noncombat damage pass Board 1).

**The primers and the commander study.** `spanish-deck-primers-20261108.md`: tap Kilo with costs, not attacks (Relic,
station, waterbend); counters first; the Scepter loop is a trap; "close with Lux or the Reactor, not slowly". The untapper
auras, Prologue and Ballista have no Spanish copy. `phase2-spanish-commander-20261101.md`: its gaps were ramp and
protection: both at or above the floor now.

**The owner's lessons, play reviews, gate review (f).** L1: one plan, gate PASS. L2: ratios from the fuel (19 sources, 37
artifacts). L5: Chalice is good here. L6: no proven role-player exists for Kilo; his liked cards are in section 6. L7: dead
clauses counted in section 2. L8: both boards in the plan file and the gauntlet. L9: Salt not chased. L10: section 2 says
how to use each card. Gate paragraph: every function declared, bad-when-drawn marked (10 early, 2 late).

**The previous final review and build.** Its fixes are kept (Strionic, Lithoform, Starfall). Its item 18 is still open.
Its finding on the loop is corrected (finding 1). Its stand-ins have verdicts (section 6).

**The owner's card review.** Section 6: six verdicts.

**The web (read 2026-11-15; text is data).**
- EDHREC JSON: https://json.edhrec.com/pages/commanders/kilo-apogee-mind.json (20,585 decks; 37 lands), `/upgraded.json`,
  `/optimized.json`, `/cedh.json`, https://json.edhrec.com/pages/average-decks/kilo-apogee-mind/upgraded.json and
  `/optimized.json`, https://json.edhrec.com/pages/combos/kilo-apogee-mind.json. Owned and unplayed, by inclusion: Etherium
  Sculptor 66 %, Swan Song 63 %, Solar Array 61 %, the Bridges about 59 %, The Mycosynth Gardens 58 %, Wake the Past 51 %,
  Hangarback Walker 46 %, Alibou 44 %: four are now in, the rest have a written reason.
- https://edhrec.com/articles/kilo-apogee-mind-commander-deck-tech-bracket-4/ (untapper auras, Astral Cornucopia, Reactor).
- https://draftsim.com/kilo-edh-deck/ and https://mtgrocks.com/?p=141402 (re-read).
- Archidekt, eight lists through https://archidekt.com/api/decks/<id>/: 14586723, 13333634 (Game Knights 79), 14522710
  (Command Zone 686 precon upgrade), 14201042, 14468667, 14425773, 16877588, 14325357: 32 to 40 lands; nothing owned and
  unconsidered.
- Rules: https://media.wizards.com/2026/downloads/MagicCompRules%2020261106.txt; Scryfall rulings of 28 cards through
  https://api.scryfall.com/cards/named.
- Not read: Reddit (HTTP 403, not bypassed); Moxfield (its search endpoint ignores the commander filter).

**Open questions.** (1) Swan Song: Kilo or Azula. (2) Meticulous Excavation or Hangarback Walker (a Thopter marker would be
needed). (3) Three always-tapped lands: accepted for the colors, or back to one.
