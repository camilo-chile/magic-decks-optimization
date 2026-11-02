# Toph, the First Metalbender: Phase 2 build notes (2026-11-02, round 3)

Round 3 applies the adversarial review `decks/reports/review-toph-the-first-metalbender.md` (verdict PASS): the three
three-card infinite lines are declared (R8, R9, route "infinite landfall"), Rocky Rebuke became Fire Nation Archers,
Redirect Lightning became Hakoda, Selfless Commander (both free copies in no other deck, checked against
`data/model/phase2/assignment.json` and the pool), Planar Outburst is no longer called one-sided, the padding of the plan
file is fixed (Arbaaz in landfall_payoffs, Soul-Guide Lantern tagged `orphan` as graveyard hate, wipe_insurance lists what
protects the route). Gate PASS 0 warnings; bracket PASS (floor 3, 1 Game Changer).

Builder: Opus 5.5 high, upgrade mode (SKILL step 0b) from `decks/scanned/toph-the-first-metalbender.txt` (Phase 1 list he
plays today) and his original list `data/raw/Toph.txt`. Pool: `data/model/phase2/pool-toph-the-first-metalbender.json`
(484 cards). Language policy "both" (English copy when owned in both). Gate: `decks/reports/consistency-toph-the-first-metalbender.md`
PASS, 0 failures, 0 warnings. Bracket: `decks/reports/bracket-toph-the-first-metalbender.md` PASS (1 Game Changer, live
Scryfall check 2026-11-01: Crop Rotation only).

## 1. Commander reading and rules points to verify

Oracle (Scryfall, read 2026-11-01): {1}{R}{G}{W} 3/3. "Nontoken artifacts you control are lands in addition to their other
types. (They don't gain the ability to {T} for mana.) At the beginning of your end step, earthbend 2."

- Rewards: land entries (every nontoken artifact that enters is a land entering), lands that are creatures, +1/+1 counters
  on lands (earthbend every end step).
- Fuel: land entries per turn. Toph adds two sources of it: each nontoken artifact cast is one more entry, and each end
  step makes an earthbent land that RETURNS to the battlefield when it dies, so a sacrifice outlet turns it into one more
  entry a turn.
- Window: end step (earthbend); the static works all the time.
- How it wins: it does not; the 99 win (pings per entry, Ragost, the land army).
- How it dies: spot removal, wipes. Toph is a 3/3 that never needs to attack.
- Dependence: **enabler** (owner lesson L4: "Toph lives on landfall and its commander matters less"). The plan runs on
  land ramp, fetch lands and payoffs without her; she adds about one entry a turn (artifacts, re-entry) and the counters
  that feed Terrasymbiosis. Protection class enabler: 3 to 4.
- Cost: 4 MV, three colors: ramp floor +2 (20), colors must be ready on turn 4.
- Dead clauses: none on the commander. Its "artifacts are lands" clause is live with 14 nontoken artifacts in the list.

Rules points (load-bearing):
| # | Point | Status | What falls if wrong |
|---|---|---|---|
| R1 | A nontoken artifact entering under Toph triggers "whenever a land you control enters". | Confirmed by analogy: the Ashaya ruling says creatures "enter the battlefield as lands"; Toph's ruling says the static "only affects permanents on the battlefield", which is where ETB triggers look (CR 603.6, not re-read). | Only the commander-conditional bonus (artifact entries); land_entries counts 25 pieces without them. |
| R2 | An earthbent land that dies (sacrifice included) returns tapped and that return is a land entry. | Confirmed (earthbend rulings 2025-10-02: "When it dies or is exiled, return it to the battlefield tapped"; it enters, so landfall triggers). Returns only once per earthbend (new object). | The re-entry engines (Zuran Orb, Goblin Bombardment, Crop Rotation, Harrow-type sacrifices). |
| R3 | Earthbend may target an artifact (it is a land under Toph) or an already earthbent land (counters stack, base 0/0 again). | Confirmed by the rulings ("You may target a land that is already a creature"). | Nothing big; pilot note only. |
| R4 | Chromatic Lantern and Great Divide Guide give "{T}: Add one mana of any color" to LANDS, so every artifact-land taps for mana under Toph. | Granted ability, not the intrinsic one the reminder text denies; consistent with the reminder. Not checked against a specific ruling. | Some ramp from the 14 artifacts; the list does not count it. |
| R5 | Planar Outburst ("destroy all nonland creatures") spares my lands, earthbent lands and artifact creatures under Toph (Hart, Solemn, Gearhulk); it KILLS Toph and every nonartifact creature (all creature pingers, Ragost, The Earth King) unless Ashaya is out, which makes my nontoken creatures lands. | Follows from the type change; not checked against a ruling. | Only the Ashaya case; the wipe is NOT one-sided otherwise (review M-1). |
| R6 | Annie Joins Up makes the end-step earthbend, Tannuk, The Earth King, Titania, Arbaaz and Bumi triggers trigger twice; Tannuk's second resolution in a turn draws. | Annie's rulings confirm "triggers an additional time"; Tannuk's "second time this ability has resolved this turn" counts each instance (reading of the Oracle text, no Tannuk ruling exists). | Some damage and draw. |
| R7 | Bumi, Unleashed + Ashaya is a two-card infinite combat (Bumi is a land creature under Ashaya, so he attacks in each extra combat). | Spellbook variant, classed late by `check_phase2_bracket.py` (floor 3); accepted (owner rule: every legal combo is welcome). | none |
| R8 | Toph + Springheart Nantuko + Lotus Cobra (or Tireless Provisioner): Nantuko bestowed on the land Toph earthbent; each landfall pay {1}{G} for a token copy of that land. The copy copies only the printed land (type change and counters are not copiable), so it is a plain land that enters untapped, triggers landfall again and taps for the next payment together with Cobra's mana (or Provisioner's Treasure): infinite landfall. | Spellbook 3470-5702-6871 and 3875-5702-6871 (status OK); copiable-values point confirmed by the review. | The fourth route only. |
| R9 | Ashaya + Toph, the Blind Bandit + Zuran Orb (or Goblin Bombardment): under Ashaya the Bandit is a Forest land, so her entry earthbend may target herself; sacrificed, she returns (earthbend), enters again and earthbends herself: infinite landfall and life (Orb) or damage (Bombardment). | Spellbook 539-1315-7037 and 539-5147-7037 (status OK). | The fourth route only. |

## 2. Plan and backup

- **Plan:** put two to four lands onto the battlefield every turn from turn 4 (land ramp that puts lands into play, four
  fetch lands, Druid Class and Explore, The Earth King, and with Toph every nontoken artifact), re-enter Toph's earthbent
  lands through Zuran Orb, Goblin Bombardment and the land-sacrifice ramp, and turn each entry into 1 damage to EACH
  opponent (Tannuk, Sabotender, Arbaaz Mir, Valakut Exploration) while Terrasymbiosis, Tireless Tracker and Tannuk refill
  the hand; Ragost's 3-damage-to-each-opponent sacrifices and Fire Nation Archers (2 to each opponent per {5}) end it.
- **Combo top end (route "infinite landfall", all legal at Bracket 3 and accepted by the owner's standing rule):** (R8)
  Toph + Springheart Nantuko bestowed on her earthbent land + Lotus Cobra or Tireless Provisioner = infinite landfall,
  possible from turn 5; (R9) Ashaya + Toph, the Blind Bandit + Zuran Orb or Goblin Bombardment = infinite landfall and
  life or damage; (R7) Bumi + Ashaya = infinite combats and mana. Each piece is on plan by itself. With a pinger or
  Valakut out, every opponent dies at once. Odds (review): R8 8 % by turn 7, 15 % by turn 13 (Chord fetching a missing
  piece); R9 5 % by turn 13; R7 7 % by turn 9. Pilot rules: when Nantuko is in hand, point Toph's end-step earthbend at
  an untapped basic Forest; cast the pinger first, then go off; Chord fetches the missing half.
- **Backup:** the same entries build a land army (earthbent lands, Rampaging Baloths beasts, Titania elementals, The Earth
  King's bear): power-4+ attacks make The Earth King fetch more lands, Garruk's Uprising and Earthbender Ascension give
  trample, Seismic Tutelage doubles counters, Bumi untaps every land for an extra combat. It reuses the fuel and the
  payoffs; only its closers are its own.

Entries-per-turn budget (turns 4 to 8) [J]: 1 natural drop + one-shot land ramp (25 entry cards, about 3 seen by turn 6,
each worth 1 to 3 entries; fetch lands give 2 from one drop) + Toph's artifacts (14) and end-step re-entry with an outlet
(about 0.5 to 1 a turn) + repeatables (Druid Class, The Earth King, Ashaya). Realistic rate 2 to 3 a turn with Toph out,
about 2 without her. The owner's "several a turn" target is met from turn 4 to 5 on.

Card-flow budget [J]: peak turns spend about 2 cards (a land and one or two cheap spells). Gain: 1 natural + Terrasymbiosis
2 a turn with Toph (her end-step earthbend 2) + Tannuk 1 (second entry each turn) + Tracker clues (1 per {2}) + Valakut
impulse + Stocking the Pantry and Garruk's Uprising. One engine out keeps the hand level; with none the hand empties
around turn 7.

## 3. Profile table (archetype `landfall_lands`, no secondary)

| Function | Tier | Min | Target | Actual | Needed by | Reason |
|---|---|---|---|---|---|---|
| land_entries | gate | 12 | 16 | 25 + Toph (+2 tutors) | early | The fuel. Owner L2: "absurd" entries, several a turn. 21 cards put lands onto the battlefield by themselves (Rampant Growth, Shared Roots, STE, Wayfarer's Bauble, Harrow, Cycle of Renewal, Roiling Regrowth, Heaped Harvest, Druid Class, Explore, Crop Rotation, Burnished Hart, Solemn, The Earth King, Titania, Earthbender Ascension, Ashaya, 4 fetch lands); Zuran Orb and Toph, Hardheaded Teacher count as re-entry pairs [J, mana-and-ramp.md 3]. Toph adds the 14 artifacts (commander-conditional, not counted). 98 % to see one by 12 cards. |
| landfall_payoffs | gate | 10 | 12 | 13 (12 + Chord) | early | Commander is not a payoff, so early 10. Tannuk, Sabotender, Valakut Exploration, Tireless Tracker, Tireless Provisioner, Lotus Cobra, Earthbender Ascension, Springheart Nantuko, Rampaging Baloths, Arbaaz Mir (pays on every artifact or legend entry, which under Toph are land entries); Druid Class (1 life a landfall, weak) and Titania (land-to-graveyard, a lands-matter trigger, not landfall) are listed with that caveat: about 11 honest pieces with Chord (review M-2). 83 % by turn 5. |
| through_wide_board | gate | 10 | 12 | 15 | early | Noncombat damage to each opponent (Tannuk, Sabotender, Arbaaz, Valakut, Ragost, Fire Nation Archers, Bombardment), a wipe that clears their chump board (Planar Outburst, symmetric for my nonartifact creatures unless Ashaya is out), team trample (Garruk's Uprising), trample (Ascension, Baloths, Bumi), unblockable (Rogue's Passage, Secret Tunnel). Bombardment's ping is single-target but repeatable. |
| through_big_creatures | gate | 10 | 12 | 17 | early | 7 spot removal + Annie + Planar Outburst + unblockable lands + noncombat closers that ignore blockers (Tannuk, Sabotender, Ragost, Fire Nation Archers). |
| extra_land_drops | support (inside land_entries) | 5 | 7 | 7 listed, about 5.0 weighted | early | Druid Class (1), The Earth King (1, needs a power-4+ attack, met with its own bear), Ashaya (1: every nontoken creature cast is an entry), Explore (0.5, one-shot), Zuran Orb, Goblin Bombardment, Ba Sing Se (0.5 each: one re-entry a turn when an earthbent land exists). The pool has no other repeatable extra-land-drop card; purchase proposal 1 fixes it. |
| land_recursion | support (inside land_entries) | 3 | 5 | 4 | late | Titania (returns a land), True Ancestry, Zuran Orb and Goblin Bombardment (an earthbent land comes back). |
| mana_sinks | support | 3 | 4 | 7 | late | Ba Sing Se, Rogue's Passage, Secret Tunnel, Stocking the Pantry, Tireless Tracker, Springheart Nantuko, Ragost. |
| wipe_insurance | support | 2 | 3 | 4 | late | What protects the ROUTE, not only bodies (review I-3): Haystack (phases one pinger or Toph out), Hakoda (sacrifice at instant speed: +0/+5 and indestructible for the whole team, blanks destroy and damage wipes), Collective Resistance (one creature), Ba Sing Se (rebuilds land creatures). Valakut Exploration is the one pinger that is not a creature. |
| ramp (base) | base | 20 (18 + 2 for MV 4) | 22 | 20 | cast by turn 3 | 17 primary + Earthbender Ascension, Tireless Provisioner, Burnished Hart (cast turn 3; its two lands arrive turn 4 or 5, written so). Every one is castable by turn 3; 91 % to see one by turn 3. Land ramp preferred (12 of 20), the 5 rocks are also entries with Toph. |
| draw (base) | base | 10 | 12 | 10 | early | Terrasymbiosis, Ichor Wellspring, Stocking the Pantry, Garruk's Uprising, True Ancestry primary; Tannuk, Valakut, Tracker (plan-tied draw met most turns), Solemn, Brightglass (two cards) second. 74 % by turn 5. |
| removal (base, spot) | base | 6 | 8 | 7 spot + 3 second | early | Swords, Path, Beast Within, Fateful Absence, Stroke of Midnight, Hardlight Containment, Sandbenders' Storm. Second tags: Annie (5 damage), Origin of Metalbending and Collective Resistance (artifact/enchantment modes). Soul-Guide Lantern is graveyard hate, tagged `orphan` because the tag set has no graveyard-hate tag (review M-2). |
| wipe (base) | base | 1 | 2 | 1 | late | Planar Outburst: a reset when behind; it kills Toph and my nonartifact creatures unless Ashaya is out (R5). Landfall average is 1 (notes/13 E1). |
| protection (base, commander) | base | 3 (enabler) | 4 | 4 | early | Haystack (phasing: removal and exile wipes), Collective Resistance (hexproof + indestructible), Origin of Metalbending (indestructible), Hakoda (team indestructible and +0/+5 at instant speed: saves Toph from destroy and damage, and the pingers from a wipe). |
| graveyard hate | floor 1 | 1 | 1 | 1 | late | Soul-Guide Lantern. |
| tutors | B3 median 4 | | | 2 | | Chord of Calling (creatures: Earth King, Tannuk, Baloths, Titania, Cobra), Brightglass Gearhulk (Zuran Orb, Wayfarer's Bauble, Hardlight, Stocking, Sol Ring). |

Fit check: gate mins counting each card once: land_entries 12 + landfall_payoffs 10 (Ascension and Druid Class overlap)
+ boards (most pieces are removal and payoffs already counted) + base removal 6 + draw 10 (3 overlap) + protection 3 + wipe 1
+ tutors 2 = about 50 nonland slots; 61 nonland slots available with 38 lands. It fits.

Lands 38 (band 38 to 40): average MV 2.61 with 20 cheap ramp pieces; Karsten's regression gives about 33, the landfall band
asks 38 to 40; 38 because the deck fetches most of its lands from the library rather than needing them in hand. Opening
hands: 2 to 4 lands in 7 is 75.5 %, 94 % with the free redo; 3+ lands 54.8 %.

Curve (nonland, 61): MV0 1, MV1 9, MV2 21, MV3 18, MV4 7, MV5 4, MV6 1. Plays on turns 1 to 3 are dense; 5 cards at 5+.

## 4. The list grouped by function (how to use it here; when it is bad to draw)

Commander: **Toph, the First Metalbender**. Cast turn 3 or 4. At each end step earthbend the land you want to keep
growing (Secret Tunnel for an unblockable attacker) or a land you will sacrifice (fetch land, a land for Zuran Orb). With
her out, every artifact you cast is a landfall trigger: sequence artifacts after the pingers.

Ramp (20)
- Sol Ring: turn 1 to 2; with Toph also an entry. Never bad (late it still is an entry).
- Arcane Signet: turn 2 rock for the turn-3 Toph. Never bad.
- Talisman of Impulse: turn 2, makes R or G. Never bad.
- Chromatic Lantern: turn 3; with Toph every artifact-land taps for any color (R4). Bad late (a 3-MV rock drawn on turn 8).
- Bender's Waterskin: untaps on each opponent's untap step: hold mana for Chord or Harrow on their turns. Bad late (a 3-MV rock, lesson L5).
- Rampant Growth: turn 2, fetch the missing color. Never bad (an entry late).
- Shared Roots: turn 2, as Rampant Growth; it is a Lesson (Toph, Hardheaded Teacher puts 2 counters). Never bad.
- Sakura-Tribe Elder: turn 2, chump-block then sacrifice for a basic. Never bad.
- Lotus Cobra: turn 2; each entry is one mana of any color: chain Harrow or a fetch into a big turn. COMBO piece (R8): with Toph and Springheart Nantuko bestowed on an earthbent land, Cobra pays every copy: infinite landfall. Never bad.
- Great Divide Guide: turn 2 fixer; under Toph every artifact and land taps for any color. Never bad.
- Wayfarer's Bauble: turn 1, crack turn 2 or at an opponent's end step; with Toph two entries. Never bad.
- Harrow: instant; sacrifice an earthbent land (it returns) for three entries and two untapped lands. Never bad.
- Cycle of Renewal: instant Lesson; same trick as Harrow, lands come tapped; cast at an opponent's end step. Never bad.
- Roiling Regrowth: instant twin of Cycle of Renewal. Never bad.
- Heaped Harvest: turn 3; fetches on entry and when sacrificed (Zuran Orb, Ragost, its own Food ability); with Toph three entries. Never bad.
- Druid Class: turn 2 (1 life per entry untaps Ragost), level 2 on turn 3 or 4 for an extra land every turn, level 3 late as a sink. Never bad.
- Explore: turn 2 or 3 with a land in hand: extra entry and a card. Never bad (a cantrip late).
- Burnished Hart (ramp second): turn 3, activate turn 4 or 5 for two basics; with Toph three entries. Never bad.
- Earthbender Ascension and Tireless Provisioner: listed under payoffs (ramp second).

Land entries and re-entry engines (11)
- Crop Rotation (Game Changer): instant, 1 mana; sacrifice an earthbent land (it returns) to fetch Ba Sing Se, Secret Tunnel or the missing color untapped; also dodges land removal. Never bad.
- Zuran Orb: sacrifice earthbent lands (they return: re-entry), fetch lands after cracking, Heaped Harvest or Ichor Wellspring under Toph; each gives 2 life (Ragost untaps) and, with Titania, a 5/3. COMBO piece (R9): with Ashaya and Toph, the Blind Bandit, sacrifice the Bandit over and over (infinite landfall and life). Bad early (no earthbent land yet).
- Solemn Simulacrum: turn 4; a basic, a chump blocker, a card when it dies; with Toph two entries. Never bad.
- The Earth King (proven role-player): cast turn 4 to 5; attack with the bear plus any power-4+ land creature and fetch that many basics every combat. Protect it with Haystack. Never bad.
- Titania, Protector of Argoth: returns a fetch land; then every fetch, Harrow-type spell or Zuran Orb sacrifice makes a 5/3. Bad early (5 MV).
- Ashaya, Soul of the Wild: every nontoken creature you cast becomes a land entry and taps for G; while she is out Planar Outburst spares all your creatures. COMBO hub: with Bumi (R7) infinite combats; with Toph, the Blind Bandit plus Zuran Orb or Goblin Bombardment (R9) infinite landfall. Cast her before the Bandit or Bumi. Bad early.
- Toph, Hardheaded Teacher: each spell earthbends 1 (Lessons 2): pair with Bombardment or Zuran Orb for one entry per spell; its entry regrows Harrow or a removal spell. Never bad.
- Toph, the Blind Bandit (route closer): earthbend 2 on entry; her power is every counter on your lands, so she is the power-4+ attacker for The Earth King. With Ashaya out she is a land: point her own entry earthbend at herself, then sacrifice her to Zuran Orb or Goblin Bombardment and repeat (R9). Never bad.
- Bumi, Unleashed (route closer): earthbend 4 makes a 4/4 haste land that triggers The Earth King the same turn; trample; when he connects all lands untap and land creatures attack again. Bad early.

Landfall and entry payoffs (13)
- Tannuk, Memorial Ensign: turn 3; 1 damage to each opponent per entry and a card on the second entry each turn. Never bad.
- Sabotender: turn 2; 1 damage to each opponent per entry; reach blocker. Never bad.
- Valakut Exploration: turn 3; each entry exiles a card you may play; what you do not play deals damage to each opponent at your end step. Never bad.
- Tireless Tracker: turn 3; a Clue per entry; crack Clues on opponents' turns (each counter draws with Terrasymbiosis). Never bad.
- Tireless Provisioner: turn 3; Treasure for mana, Food when Ragost needs fodder or a lifegain. COMBO piece (R8): with Toph and a bestowed Springheart Nantuko, take a Treasure each landfall to pay the next copy. Never bad.
- Springheart Nantuko: the KEY combo piece (R8). When Toph earthbends at your end step, aim her at an untapped basic Forest while Nantuko is in hand; next turn, with Lotus Cobra or Tireless Provisioner out and a pinger or Valakut already on the table, bestow Nantuko ({1}{G}) on that land creature: each landfall pay {1}{G} for an untapped copy of the land, which triggers the next landfall: infinite entries, every opponent dies to the pinger. Without the second piece, still bestow it on an earthbent land (each paid copy is one more land entry) or cast it alone for a 1/1 per entry (Bombardment fodder). Never bestow it on a legendary creature (the copy dies to the legend rule). Never bad.
- Earthbender Ascension: turn 3; a basic and a 2/2 land at once; after four entries each entry gives +1 counter and trample. Never bad.
- Rampaging Baloths: a 4/4 per entry; the beasts are power-4 attackers for The Earth King and draw with Garruk's Uprising. Bad early.
- Seismic Tutelage (proven role-player): put it on a creature that is NOT one of Toph's returning land creatures and that attacks: Brightglass Gearhulk (first strike and trample keep it alive and connecting), Bumi (trample), The Earth King's bear, Toph the Blind Bandit, Tireless Tracker with clue counters, a Baloths beast; it doubles the counters each attack. It kills one opponent per attack (third route), not the table. Bad early (needs that creature).
- Arbaaz Mir: each nontoken artifact or legendary that enters pings each opponent and gains 1 life (Ragost untaps). Never bad.
- Ragost, Deft Gastronaut: every artifact is a Food: {1}, tap, sacrifice one for 3 damage to each opponent; untaps at every end step after any lifegain, up to four shots a turn cycle. Sacrifice tokens first, earthbent artifacts (they return). Never bad.
- Goblin Bombardment: sacrifice earthbent land creatures at the end step after Toph earthbends (they return: one more entry), beasts and tokens before a wipe; finishes the last player. COMBO piece (R9): with Ashaya and Toph, the Blind Bandit, sacrifice the Bandit endlessly: unlimited damage to any targets. Never bad.
- Annie Joins Up: 5 damage to the biggest creature; then the end-step earthbend, Tannuk, The Earth King, Titania and Arbaaz trigger twice. Never bad.

Draw (5 primary; 5 more as second tags above)
- Terrasymbiosis: turn 3; Toph's end-step earthbend draws 2 every turn; clue counters on Tracker draw on opponents' turns. Never bad.
- Ichor Wellspring: a card now and one when it goes (Zuran Orb, Ragost); with Toph an entry. Never bad.
- Stocking the Pantry: 1 mana; every earthbend adds a supply counter; spend spare {2} for cards. Never bad.
- Garruk's Uprising: team trample for land creatures; a card for each power-4+ creature entering (beasts, elementals, the bear). Never bad.
- True Ancestry: return The Earth King, a payoff or a fetch land and get a Clue; Lesson. Bad early (empty graveyard).

Removal (8 spot) and graveyard hate
- Swords to Plowshares: the must-answer creature or commander. Never bad.
- Path to Exile: same; the land it gives matters little against a landfall deck. Never bad.
- Beast Within: any permanent (artifact or enchantment engines included). Never bad.
- Fateful Absence: instant creature or planeswalker answer. Never bad.
- Stroke of Midnight: any nonland permanent. Never bad.
- Fire Nation Archers: cast turn 4 as a 3/4 reach blocker (survives pings); from turn 7 every spare {5} is 2 damage to EACH opponent and a 2/2: the mana sink that turns the ramp into the clock. Chord target (X=4). Never bad.
- Hardlight Containment: 1-mana exile; enchant a rock nobody targets, never one you will earthbend or sacrifice to Ragost or Zuran Orb (the creature comes back). Never bad (14 artifacts).
- Sandbenders' Storm: destroy a power-4+ creature, or at an opponent's end step earthbend 3. Never bad.
- Soul-Guide Lantern (graveyard hate, tag `orphan`): exile a reanimation target, or the whole yards; else cash it for a card; an entry with Toph. Never bad.

Protection (4)
- Haystack: phase out Toph, The Earth King or a pinger in response to removal or an exile wipe. Never bad.
- Collective Resistance: hexproof and indestructible on Toph, or kill an artifact or enchantment (escalate for both). Never bad.
- Origin of Metalbending: indestructible plus a counter (a Terrasymbiosis draw), or destroy an artifact or enchantment. Never bad.
- Hakoda, Selfless Commander: 4-MV 3/5 vigilance blocker; look at the top card and cast Allies from it (The Earth King, both Tophs, Bumi, Great Divide Guide); when a wipe or a damage sweep is cast, sacrifice it in response: your team gets +0/+5 and indestructible, pingers and Toph survive. An Ally, so Great Divide Guide makes it tap for mana. Never bad.

Wipe (1)
- Planar Outburst: a reset when you are behind on board, NOT one-sided: it kills Toph and every nonartifact creature of yours (pingers, Ragost, The Earth King) unless Ashaya is out; your lands, earthbent lands and artifact creatures (Hart, Solemn, Gearhulk) stay. Best cast with Ashaya on the battlefield, or with Hakoda ready to sacrifice. Awaken at 8 mana. Bad early.

Tutors (2)
- Chord of Calling: instant; convoke with land creatures. Which piece: the missing combo half (Springheart Nantuko X=2, Lotus Cobra X=2, Tireless Provisioner X=3, Toph the Blind Bandit X=3 with Ashaya out), else a pinger (Tannuk X=3, Sabotender X=2), else The Earth King or Fire Nation Archers (X=4); cast it at an opponent's end step. Bad early.
- Brightglass Gearhulk: Zuran Orb plus Wayfarer's Bauble or Stocking the Pantry; a 5/5 first-strike trampler; an entry with Toph. Bad early (GGWW).

Lands (38)
- Command Tower, Exotic Orchard: untapped fixing. Never bad.
- Ba Sing Se: untapped with a basic; {2}{G} earthbend 2 as a sink and rebuild. Never bad.
- Rootbound Crag, Sunpetal Grove, Clifftop Retreat (check lands); Game Trail, Fortified Village, Furycalm Snarl (reveal lands); Rugged Prairie (filter); Battlefield Forge (pain): untapped duals. Never bad.
- Rogue's Passage: {4} makes the big land creature or Baloths unblockable. Never bad.
- Secret Tunnel: earthbend it every end step: an unblockable attacker that grows +2 a turn. Never bad.
- Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape, Cabaretti Courtyard: two entries from one drop, a land in the yard for Titania; earthbend an uncracked one and crack it for three entries. Never bad.
- 11 Forest, 5 Mountain, 5 Plains: 21 basics for 15 basic-fetching cards.

## 5. Cut log

Role-player test (reference section 2) applied to every card that leaves the Phase 1 list. None was reported by the owner as
winning games. Counts are after the whole change.

| Card cut | Function it served | Count after (min) | Replacement and reason |
|---|---|---|---|
| Hardened Scales | multiplier of earthbend counters (no declared function) | n/a | Not a land entry or payoff; the counters line is fed every turn by Toph anyway. Slot to Garruk's Uprising (team trample + draw). Owner may want it back for Seismic Tutelage: open question 2. |
| Earth Kingdom General | earthbend 2 + lifegain | land_entries 25 (12) | Its lifegain for Ragost is covered by Zuran Orb, Druid Class, Arbaaz, Foods; Sandbenders' Storm adds an answer to big creatures (Board 2) with an earthbend mode. |
| Haru, Hidden Talent | earthbend on Ally entries | land_entries 25 (12) | About 6 Allies: trigger rarely met (dead clause). Replaced by Druid Class (repeatable extra land drop). |
| Wrenn and Realmbreaker | fixing (lands tap any color), 3/3 land each turn, -2 card | ramp 20 (20) | Its fixing job is done by Chromatic Lantern and Great Divide Guide; replaced by The Earth King (proven) in the slot. |
| Everflowing Chalice | rock, free entry under Toph | ramp 20 (20) | Owner lesson L5 (cast late for little); replaced by Roiling Regrowth (land ramp, two entries, works without Toph). |
| Selesnya Signet | rock | ramp 20 (20) | Land ramp preferred for landfall; replaced by Burnished Hart (three entries with Toph). |
| Boros Locket | rock, late draw 2 | ramp 20 (20), draw 10 (10) | 3-MV rock competing with 3-MV land ramp; replaced by Explore (2 MV, entry plus card). |
| Reckless Handling | artifact tutor with random discard | tutors 2 | Card disadvantage; slot to Solemn Simulacrum (entries plus card). |
| Seismic Sense | selection for a land or creature | n/a (not draw) | Selection, not draw; slot to Stocking the Pantry (repeatable draw with earthbend). |
| Liquimetal Coating | turns a permanent into an artifact for artifact removal | removal 8 (6) | Two-card mini-combo with Haywire Mite (L7); slot to Titania, Protector of Argoth. |
| Haywire Mite | noncreature artifact/enchantment answer | artifact/enchantment answers 4 (Beast Within, Stroke, Origin, Collective) | Covered; slot to Rampaging Baloths. |
| Hunter's Bow | bite equipment | removal 7 spot (6) | Needs my big creature; slot to Seismic Tutelage (proven). |
| Inscription of Abundance | fight / counters / life | removal 8 (6) | Surplus removal (8 spot remain); slot to Cabaretti Courtyard (fetch land, two entries). |
| Nutrient Block | artifact cantrip, Food | draw 10 (10) | Low impact; slot to Evolving Wilds (fetch land, two entries). |
| The Stasis Coffin | player protection for one turn cycle | protection 4 (3) | Protects the player, not the commander; slot to fetch lands. |
| Rocky Rebuke (round 3) | spot removal that needs my big creature (bad early) | removal 7 spot (6); through_big_creatures 17 (10) | Fire Nation Archers: a mana sink that damages each opponent with no tap (review I-2: the main route's clock was thin). |
| Redirect Lightning (round 3) | commander protection (moves a targeted removal) | protection 4 (3) | Hakoda, Selfless Commander: team indestructible at instant speed protects Toph AND the creature pingers from wipes (review I-3). |
| Rumble Arena | colorless land with filter | lands 38 (38) | Colorless; replaced by Battlefield Forge (untapped R/W). |
| 2 Forest | basics | basics 21 | Replaced by the four fetch lands and Secret Tunnel (net lands 35 to 38). |

Proven role-players: The Earth King and Seismic Tutelage are IN (they were cut by Phase 1). None left out.

Considered from his original list and the pool, not played: Omnath, Locus of Rage and Titania, Nature's Force (7 and 6 MV
payoffs: the curve already holds 5 cards at 5+; open question 5), Moraug (extra combats; the deck rarely attacks),
Badgermole (Garruk's Uprising gives trample cheaper), Bumi Eclectic, The Boulder, Rockalanche, Earthbending Lesson,
Awakening of Vitu-Ghazi (more land-army cards would be a second package), Blossoming Tortoise (needs attacks), Elemental
Teachings and Viewpoint Synchronization (5-MV entries; the deck has 21 cheaper), Hour of Revelation and Blasphemous Act
(kill the pingers), Mindslaver, Karn's Sylex, Meteor Sword (off plan), artifact bridges and Jungle Shrine (tapped),
Urza's Cave (colorless), Mycosynth Wellspring and Barrels of Blasting Jelly (low impact), bounce lands (Gruul Turf: piece
of the Toph, Hardheaded Teacher loops, kept out on purpose).

## 6. Loans

- Used: none. The loan candidates are Assassin, black or blue cards outside this plan. Viewpoint Synchronization is owned
  (2 free copies), so it is not a loan; considered and not played (5-MV entries).
- Proposals to evaluate: none.

## 7. Scarce copies (fewer copies than decks that could want them)

Other decks: Ezio (five colors), Azula (UBR), Spanish deck (Spanish copies only; leading candidate Kilo, RUW). Where it
adds most is judgment [J].

| Card | Copies | Held today | Could want it | Adds most in | Toph's fallback if it loses it |
|---|---|---|---|---|---|
| Command Tower | 3 (1 EN, 2 ES) | Azula, Ezio, Toph | all four | Toph takes the EN copy (rule); the ES copies decide Azula vs Spanish | a basic (Toph has 38 lands, strong fixing) |
| Chromatic Lantern | 2 EN | Ezio, Toph | Ezio, Azula, Toph | Toph (bridge: every artifact-land taps for any color) | Great Divide Guide already does the same job; the slot goes to Pentad Prism (ES, free) or a basic |
| Swords to Plowshares | 2 ES | Toph, free | Toph, Ezio, Spanish | Spanish deck if white (it can only use ES) | Fateful Absence is already in; then Sandbenders' covers |
| Path to Exile | 1 ES | Toph | Toph, Ezio, Spanish | Toph or Spanish (lead decides) | Inscription of Abundance (EN, free) |
| Fateful Absence | 2 ES | Ezio, Toph | Ezio, Toph, Spanish | Ezio and Toph hold them | Inscription of Abundance |
| Planar Outburst | 1 ES | Toph | Toph, Ezio, Spanish | Toph (spares her lands and artifact creatures; one-sided only with Ashaya, R5) | What Must Be Done (symmetric) |
| Battlefield Forge | 1 ES | free | Toph, Ezio, Spanish (RW) | Spanish deck if RW | Rumble Arena (EN) |
| Arbaaz Mir | 1 ES | Toph | Toph, Ezio, Spanish (candidate commander) | Spanish deck if it is its commander; otherwise Toph | Titania, Nature's Force (ES) or Omnath, Locus of Rage (EN) as the replacement payoff; the landfall-burn route keeps Tannuk, Sabotender, Valakut |
| Burnished Hart | 1 ES | free | any deck (colorless) | Toph (three entries) | Viewpoint Synchronization (EN, free) |
| Vibrant Cityscape | 2 ES | free | any deck | Toph | another basic |
| Soul-Guide Lantern | 2 ES | Toph, free (Azula's list names it too) | Toph, Azula, Spanish | Azula and Toph hold; Spanish needs one | no other graveyard hate in the pool for these colors: Toph would drop under the floor of 1 (a written gap) and play Ichor-type value instead (Mycosynth Wellspring, EN) |
| Solemn Simulacrum | 1 EN | free | any deck | Toph | Viewpoint Synchronization |
| Lotus Cobra, Chord of Calling | 1 ES each | Toph | Toph, Ezio | Toph (landfall) | Raucous Audience; Seismic Sense |
| Cabaretti Courtyard, Annie Joins Up | 1 EN each | free / Toph | Toph, Ezio | Toph | Terramorphic copy 2 (4 owned); Lightning Axe |

`scripts/assign_copies.py` (lead) decides; Toph's changes can absorb any single loss above with the fallback named.

## 8. Purchase proposals (ranked by impact; Game of Magic Singles only)

Budget (owner update, 2026-11-02): of the shared 10,000 CLP the Spanish deck may use up to 5,000, so Toph, Azula and Ezio
share the other 5,000 or more. Ranked by impact on this plan; all three together are about 2,900 CLP plus Exploration's
price, and rank 1 alone is the one that matters most. The list above is complete from the pool; none of these is in it.
Price hints are from the browser reading of 2026-10-17 (`data/prices/browser-gameofmagic-*.psv`), stale: live stock and
price are the lead's check.

Owner update 2026-11-02: Toph, Azula and Ezio share 5,000 CLP at Game of Magic Singles (the Spanish deck has its own
5,000); a second store is allowed only for Hidden Footblade and Overpowering Attack, which do not concern Toph. Power wish
first (owner: name a purchase that clearly raises power).

| Rank | Card | Need it fills | Price hint | Plays instead of |
|---|---|---|---|---|
| 1 | Eladamri's Call | Power and Salt: an instant creature tutor ({G}{W}) for the combo halves (Springheart Nantuko, Lotus Cobra, Tireless Provisioner, Toph the Blind Bandit) and the pingers; with Chord it doubles the tutors that reach the R8 line and answers Salt's "no tutors for the combo" ceiling seen in Phase 1. | no reading | Sandbenders' Storm (spot removal stays at 6 = min) |
| 2 | Exploration | The only weak support line: repeatable extra land drops (about 5.0 weighted, only Druid Class is a true repeatable). {G}: one extra land every turn from turn 1. | no reading | Explore |
| 2 | Cultivate | Land ramp that is two entries' worth and works without Toph (the profile prefers land ramp to rocks). | 1,120 CLP NM EN | Bender's Waterskin |
| 3 | Farseek | 2-MV land ramp (Mountain or Plains) instead of a rock; one more entry. | 1,760 CLP NM EN | Talisman of Impulse |

Dryad of the Ilysian Grove (9,880 CLP) and Azusa (12,480 CLP) are over the shared budget; Dryad is also a piece of a
curated Toph loop (hazard `toph-emeria-omen-loop`, harmless without Emeria Shepherd).

## 9. WARN reasons and dead clauses

- Gate warnings: none. Bracket review items: two.
  - Bumi, Unleashed + Ashaya (Spellbook, two-card infinite combats, flagged late, floor 3). Both cards are here for their
    own jobs; it needs 10 mana across two specific cards, so it does not "tend to happen" in the first six turns. Accepted.
  - The three-card lines R8 and R9 (Spellbook, inside the list, not flagged): three-card lines are not barred by any
    bracket rule; the owner's standing rule accepts every legal combo. Declared in the plan file as the fourth route.
  - Hazard `toph-loop-hubs` (Toph, Hardheaded Teacher): its loops need a bounce land, a 0-MV artifact cast again and an
    outlet; the list has no bounce land, so none can assemble. Checked by hand.
- Dead or conditional clauses: Toph, Hardheaded Teacher's Lesson bonus (5 Lessons, a bonus only); Garruk's Uprising's draw
  (needs power-4+ creatures entering: beasts, elementals, bear, Gearhulk, Bumi); Secret Tunnel's second ability (two
  creatures sharing a type: tokens only); Planar Outburst's awaken (8 mana); Druid Class level 3 (late sink); Ragost's
  untap clause (met: Zuran Orb, Druid Class, Arbaaz, Foods, Cabaretti); Seismic Tutelage needs a non-land attacker
  (bear, Toph the Blind Bandit, Tracker, beasts); Hardlight Containment needs an artifact (14 in the list).
- Commander-conditional pieces (enabler, weight 0.5): the 14 artifacts as entries, the end-step re-entry, Terrasymbiosis's
  2 a turn. None is counted in a gate function.
- After a creature wipe the creature pingers die (Tannuk, Sabotender, Arbaaz, Ragost, Archers); the lands, the earthbent
  lands and Valakut stay. Answers: Hakoda sacrificed in response (team indestructible, +0/+5: destroy and damage wipes),
  Haystack (one creature, exile wipes too), Collective Resistance (one creature); deploy pingers one or two at a time,
  Valakut first; with Ashaya out, aim Toph's end-step earthbend at a pinger (it is a land) so it returns if it dies.
  Rebuild: Chord and True Ancestry find a pinger.
- Pilot notes from the review: from turn 8 fetch basics for the card that needs them most (21 basics for about 22
  basic-fetching effects plus The Earth King); library-search hate (Stranglehold-type) is the worst single hate card:
  Beast Within or Stroke of Midnight it.

## 10. The two reference boards

- **Board 1, eight 1/1 chump blockers that sacrifice:** the main route ignores them: every entry pings each opponent
  (Tannuk, Sabotender, Arbaaz), Valakut's end-step damage, Ragost's 3 and Archers' 2 to each opponent; Planar Outburst clears
  them and keeps the land creatures (my nonartifact creatures die too unless Ashaya is out). Their sacrifice-pings kill my
  toughness-2 pingers: hold Hakoda. The land army has team trample (Garruk's Uprising, Ascension) and unblockable lands
  (Secret Tunnel, Rogue's Passage). Their sacrifice outlets cost the deck little: earthbent attackers return.
- **Board 2, two creatures bigger than yours:** 8 spot answers (Swords, Path, Beast Within, Fateful Absence, Stroke, Hardlight,
  Sandbenders' for power 4+) plus Annie's 5 damage; the pings, Ragost and Fire Nation Archers ignore them; land creatures
  and the 3/4 reach Archers block (earthbent lands come back); Hakoda's +0/+5 survives a big attack; Planar Outburst resets.

## 11. Mana

- Colored sources from lands (fetch lands at 2/3 each, Exotic Orchard 0.75): G 20.4, R 15.4, W 15.4. With partial
  sources (Arcane Signet, Lantern, Waterskin, Talisman for R/G, Guide, Cobra, three 2-MV basic fetchers at 0.75): about
  G 23, R 21, W 20 for spells of MV 3+.
- Against Karsten (41-land table, scaled): green 1C on turn 2 needs 19 (20.4 from lands: met); Toph RGW on turn 4 needs
  17 each (met with partials); Ragost and Arbaaz (R and W on turn 2) need 20 each: lands give 15.4, so they are turn-3
  plays in practice; Planar Outburst (WW) and Brightglass Gearhulk (GGWW) are short of 23 to 26 white sources and are
  marked late (bad early).
- Tapped lands: the four fetch lands put a tapped basic (each pays back two entries); Ba Sing Se, three check lands and
  three reveal lands are conditional and usually untapped. Colorless lands: 2 (Rogue's Passage, Secret Tunnel).
- Ramp: 20 pieces castable by turn 3: 88 % to see one by turn 2 (9 cards), 91 % by turn 3.
- Keepable hands: 2 to 4 lands in 7 at 38 lands is 75.5 % per look, 94 % with the free redo.

## 12. Open questions for the owner

Answered by the owner and applied (review header): Bumi + Ashaya kept (all legal combos accepted), Hardened Scales out,
the Seismic Tutelage target rule, Earth Kingdom General out for Sandbenders' Storm, no Omnath or Titania, Nature's Force,
38 lands. Open: none. Purchase wish (section 8): Eladamri's Call first, for power and Salt.

## 13. Salt (second objective)

Phase 1 Toph measured 7.1 free / 7.4 at purchase on Salt; its ceiling was "combo wincons with no tutors". This list
declares four Spellbook infinites (R7, R8 x2, R9 x2) made of on-plan cards and keeps the tutors that reach them (Chord,
Brightglass for Zuran Orb), the one Game Changer (Crop Rotation) and an untapped-heavy mana base (4 fetch lands are the only
tapped-by-design lands). Round 3 adds a closer (Archers) and wipe protection (Hakoda) without dropping any function.
Expected to hold 7.0 or more; the lead measures it. Do not cut without a new review (they carry Salt's combo reading):
Crop Rotation, Chord of Calling, Lotus Cobra, Tireless Provisioner, Springheart Nantuko, Ashaya, Bumi, Toph the Blind
Bandit, Zuran Orb, Goblin Bombardment. The best Salt-raising buy is Eladamri's Call (section 8).
