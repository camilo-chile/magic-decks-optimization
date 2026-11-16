# Toph, the First Metalbender: collection-only optimization (Phase 2 step 12.1, iteration 3, 2026-11-15)

**Fix round (step 12.3, 2026-11-15, the lead on Opus 5.5 high; review `decks/reports/collection-review-toph-the-first-metalbender-20261115.md`, verdict FIX).** Applied ranks 1 and 2 (both free English copies):

| Out | In | Reason |
|---|---|---|
| Explore | Legion Guildmage | The "9 drain cards, not fixable" claim was false: Guildmage deals 3 to each opponent for {5}{R}, taps a blocker or attacker and is a 2-drop; cards reaching the drain 9 -> 10, odds of one by turn 7 76 % -> 80 %. |
| Everflowing Chalice | Solemn Simulacrum | In the owner's original Toph list and missing from the cut log: a card that really nets a card (draw 9 -> 10, the WARN clears), a basic onto the battlefield, and with earthbend plus Ragost 3 damage to each opponent, a draw, a basic and two or three land entries a turn. |

Honest WARN: ramp 19 of 20 (18 at mana value 3 or less, plus Solemn on turn 4). The alternative the review offered,
Solemn for Hardened Scales, keeps ramp at 20 but cuts a card the owner asked for; left as is. Airbender's Reversal (free)
is the first candidate for any slot that opens (protection against exile is thin). Review answers: no counterspell, no
table-scaling draw and no third Game Changer exist in the Naya pool; Reckless Fireweaver stays in Kilo; none of the
three bracket review items breaks a Bracket 3 rule (Bumi + Ashaya on turn 5 or 6 in 1 to 2 % of games; The Stasis
Coffin protects only its controller; Teacher + Gruul Turf is four cards with Toph). Real power: 7.4 to 7.9 (builder),
against 7.5 for the deck as built on 2026-11-09. Confidence medium-low.

Builder: Fable 5.2 high, under `docs/proposals/collection-optimization-brief-20261114.md`. The collection is frozen: no
purchases, no loans, no purchase proposals. Start: the deck as built today (`decks/phase2/toph-the-first-metalbender.txt` at
the last commit). Language: bilingual (the English copy when both are free, otherwise the free copy).

**Result: 7 cards change (7 out, 7 in), all from the binders. No copy is taken from another deck.**

Checks (2026-11-15):
- `python scripts/check_phase2_bracket.py decks/phase2/toph-the-first-metalbender.txt`: **PASS** (floor 3; 2 Game Changers,
  Crop Rotation and Drannith Magistrate; no extra turns; no mass land denial; no reversible card). Three review items, none a
  broken rule: Bumi + Ashaya (two-card infinite combats, late: two 5-drops); Toph + The Stasis Coffin (Spellbook 4155-6871,
  tagged "lock": it prevents damage to ME for {2} a turn, it is not infinite, wins nothing and denies nobody's lands or turns);
  the template line Toph + Hardheaded Teacher + Gruul Turf + Goblin Bombardment (four cards with the commander).
- `python scripts/plan_density.py`: **PASS, 0 failures, 1 warning** (draw 9 against 10; reason in section 3).
- 100 cards by script: the commander, 61 nonland, 38 lands. Live Scryfall check of the 82 names (collection endpoint,
  2026-11-15): all Commander-legal, all inside RGW, layouts `normal` and `class` only, `game_changer` true on two cards.
- Running `plan_density.py` rewrites the four consistency reports; only Toph's content changed.

## 1. Profile

### Commander reading
{1}{R}{G}{W} 3/3. "Nontoken artifacts you control are lands in addition to their other types (they don't gain the ability to
tap for mana). At the beginning of your end step, earthbend 2."
- She rewards land entries: every nontoken artifact cast is a land entering, and an earthbent land that dies or is exiled
  returns tapped (a land entering again).
- Her fuel is one free earthbend a turn. The earthbend is worth the most on a land that wants to leave: an artifact with a
  sacrifice ability (Heaped Harvest, both Baubles, Soul-Guide Lantern, Haywire Mite, The Stasis Coffin), a fetch land, Urza's
  Cave. The +1/+1 counters are a second resource: Terrasymbiosis and Stocking the Pantry turn them into cards, Hardened Scales
  adds one to each earthbend, and the land army uses them.
- She wins nothing alone. Class **enabler** (owner lesson L4): land ramp, fetches and pingers work without her.
- 4 mana: she is recast twice in a normal game.
- Dead clauses to avoid: cards that need an attacking artifact creature (the list has 2), a commander that attacks, or a
  creature with power on an empty board.

Rules points:

| # | Point | Status | What falls if wrong |
|---|---|---|---|
| R1 | A nontoken artifact entering under Toph triggers "whenever a land you control enters". | Confirmed by the final review of 2026-11-08 (CR 603.6d, the Ashaya ruling); Toph's ruling of 2025-10-02 only forbids PLAYING artifacts as lands. | The artifact bonus only; 19 land-entry cards work without it. |
| R2 | An earthbent land that dies (sacrificed as a cost included) or is exiled returns tapped: a land entering. | Confirmed (earthbend rulings 2025-10-02, read on Scryfall 2026-11-15). It does not return from any other zone. | The re-entry engines. |
| R3 | The Stasis Coffin earthbent by Toph: {2}, tap, exile it; it returns tapped; I have protection from everything until my next turn. An earthbent permanent has haste, so it taps the turn it is cast. | Confirmed: Spellbook 4155-6871 (read live 2026-11-15) and the Coffin rulings of 2022-10-14: all damage to me is prevented, I cannot be targeted; creatures may still attack; untargeted effects and life LOSS still work. | The Coffin lock only. |
| R4 | Hardened Scales adds one counter to every earthbend: earthbend first makes the land a creature, then puts the counters. | Follows from the earthbend ruling's wording ("becomes a 0/0 land creature ... Put N +1/+1 counters on it"); no specific ruling. | Scales with earthbend; it still works with Tireless Tracker, Seismic Tutelage and Earthbender Ascension. |
| R5 | Terrasymbiosis draws the number of counters really put (3 with Scales); Stocking the Pantry gets one supply counter per event. | Oracle text; no ruling read. | One card a turn. |
| R6 | Loop A: Springheart Nantuko CAST with bestow on an earthbent land copies the plain land, untapped. | Verified in the final review (Spellbook 3470-5702-6871, 3875-5702-6871). | Loop A. |
| R7 | Loop B: Toph + Hardheaded Teacher + Gruul Turf + Zuran Orb (main phase only). Loop C: Ashaya + Blind Bandit + Zuran Orb or Goblin Bombardment. | Verified in the final review (Spellbook 573-1315-6871-7115, 539-1315-7037, 539-5147-7037). | Loops B and C. |
| R8 | Fire Nation Archers' ability has no tap symbol: it works the turn the Archers enter and several times a turn. | Oracle text. | Its value as a sink. |
| R9 | Ragost untaps only if life was gained BEFORE the end step begins. | Ragost ruling 2025-07-25. | Life gained by an end-step trigger does not untap it that turn. |
| R10 | Planar Outburst spares lands: earthbent lands and Toph's artifact creatures live; Toph and the nonartifact creatures die unless Ashaya is out. | Type change; no ruling read. | The Ashaya case. |

### Plan and backup
**Plan (one sentence).** Put two to four lands onto the battlefield every turn from turn 3 and turn each land entry into 1
damage to EACH opponent (Sabotender, Tannuk, Valakut Exploration; Arbaaz Mir for artifacts and legends), while four card
engines refill the hand, Ragost, Goblin Bombardment and Fire Nation Archers burn the surplus, The Stasis Coffin keeps the table
from hurting me, and an infinite-landfall loop ends the game when it assembles.

**Backup.** The same earthbends build a land army that survives creature wipes: Hardened Scales, The Earth King, Seismic
Tutelage on an unblockable Secret Tunnel, Bumi's extra combat. It reuses Toph's end step and the land entries, so it is not a
second package: its only dedicated cards are the owner's two proven role-players, Bumi, the Blind Bandit and Scales.

### Speed (goldfish of this list, section 5)
- Toph on turn 3 in 53 % of games and by turn 4 in 89 % (with colors, computed in section 3).
- A pinger or burst piece plus two entries a turn: turn 4 to 7.
- Pure drain kills the table around turn 10 to 12. The army removes one player around turn 8 to 9. A loop is together by turn
  7 in about 1 game in 7 and by turn 10 in 1 in 5 (upper bound: tutors free, mana ignored; 13.7 % at 14 cards seen, 20.6 %
  at 17, 34 % at 22).
- The honest reading: this is a mid-speed engine deck, so the Coffin and the instant answers matter.

### Win routes
Every route hits all three opponents. No failure point is shared by all of them (R28).

| Route | Closers | Cards with the commander | Kill shape | Its failure point | Survives |
|---|---|---|---|---|---|
| 1. Landfall burn (noncombat, primary) | Sabotender, Tannuk, Valakut Exploration, Arbaaz Mir | a repeatable board engine | 1 to each opponent per entry per pinger | creature wipes plus enchantment removal | Toph dead; a creature wipe (Valakut stays) |
| 2. Artifact and mana burst (noncombat) | Ragost, Goblin Bombardment, Fire Nation Archers | 1 card each | 3 to each per Ragost shot; 2 to each per {5} | artifact wipe (Ragost), a wipe | counters (permanents already down); graveyard hate |
| 3. Infinite landfall (noncombat) | Nantuko + Cobra or Provisioner (A); Teacher + Gruul Turf + Zuran Orb (B); Ashaya + Blind Bandit + Orb or Bombardment (C) | 3 to 4 | any pinger, Valakut or Bombardment kills the table | a counter or removal in response | different pieces per loop; A and C need no Toph |
| 4. Land army (combat, backup) | The Earth King, Seismic Tutelage, Bumi, the Blind Bandit | 2 | power-4+ attackers, trample, an unblockable land, extra combat | fogs, a bigger board | wipes (earthbent lands return) |

### How it beats three opponents
- The damage hits everyone each time, so the deck never chooses a target.
- The Coffin turns off combat damage and targeting against me for {2} a turn, so the slow drain has the turns it needs.
- Earthbent land creatures block and come back as landfall.
- Threats sit on creatures, enchantments, artifacts and lands, so no single wipe resets the deck.

### What it fears
- Spell combo that wins before turn 7: Naya has no counterspell; the answers are 8 instants and Drannith.
- Life loss that is not damage ("each opponent loses life") and mill: the Coffin does not stop them.
- A creature wipe plus enchantment removal in the same turn cycle.
- Search hate (Aven Mindcensor, Stranglehold). Blood Moon is survivable (21 basics); Armageddon is not.
- Its own speed: with no pinger by turn 6 it only ramps (24 % of games see none of the 9 access cards by turn 7).

### The two reference boards
- **Board 1, eight 1/1 chump blockers that can be sacrificed.** Routes 1, 2 and 3 ignore blockers. Planar Outburst clears
  them and keeps my lands. The army has trample (Ascension, Bumi) and the unblockable Tunnel. Their sacrifice pings kill my
  toughness-1 and 2 pingers (11 of 20 creatures): hold Make a Stand or Collective Resistance. The Coffin blanks their attack.
- **Board 2, two creatures bigger than mine.** 6 spot answers for creatures (Swords, Path, Fateful Absence, Beast Within,
  Chaos Warp, Stroke of Midnight), Annie's 5 damage, Planar Outburst, Drannith against a commander that comes back. Earthbent
  lands chump and return. The Coffin prevents their damage. The drain does not care.

## 2. The puzzle: roles, synergies, how to use each card

Commander: **Toph, the First Metalbender.** Cast her on turn 3 or 4, a pinger first when you hold one and she would not come
down a turn earlier. Each end step, earthbend in this order:
1. The Stasis Coffin, when anyone can hurt you this turn cycle (keep {2}).
2. A basic Forest, when Springheart Nantuko is in hand and Cobra or Provisioner is out (loop A next turn).
3. Gruul Turf, when Hardheaded Teacher and Zuran Orb are out (loop B).
4. Heaped Harvest (3 entries and 2 basics a turn for {2}), then Mishra's Bauble (a free card), Soul-Guide Lantern ({1}: a
   card), Wayfarer's Bauble, an uncracked fetch land, Urza's Cave, Haywire Mite (when a target exists).
5. Secret Tunnel, the unblockable attacker and Seismic Tutelage host.

Never earthbend Ashaya, Bumi or Brightglass Gearhulk (their size becomes 0/0 plus counters). With Toph out, play cheap
artifacts AFTER the pingers.

**Ramp (20; 12 cost 2 or less).**
- **Sol Ring.** Turn 1; later a land entry. Never bad.
- **Arcane Signet, Talisman of Impulse, Talisman of Conviction (new).** Turn-2 rocks for Toph on turn 3; Conviction is the
  12th cheap ramp piece and a red-white source. With Toph each is an entry and an Arbaaz ping. Bad late only as a 1-mana-net
  landfall.
- **Wayfarer's Bauble.** Turn 1, crack on turn 2. Earthbent: {2} for a basic and two entries every turn.
- **Everflowing Chalice.** For 2 on turn 2 without Toph; for 0 with her (a free landfall, the second 0-cost artifact of loop
  B).
- **Rampant Growth, Shared Roots, Sakura-Tribe Elder.** Turn 2; fetch the missing color. The Elder chumps first. Shared Roots
  is a Lesson (one more counter with Hardheaded Teacher).
- **Lotus Cobra.** Turn 2. A mana per entry: it pays half of the Coffin every turn. Loop A piece.
- **Great Divide Guide.** Turn 2 fixer and dork. With Toph every artifact-land taps for any color.
- **Explore.** Turn 2 or 3 with a spare land: an entry and a card.
- **Druid Class.** Turn 2: 1 life per entry (untaps Ragost). Level 2: an extra land every turn. Level 3: a sink.
- **Harrow, Cycle of Renewal.** Instants. Sacrifice the earthbent land (it returns) for two basics: three entries. Cast them
  at an opponent's end step, or in your turn with pingers out.
- **Heaped Harvest.** Turn 3: a basic now and another when sacrificed. Earthbent it is the best ramp engine of the deck.
- **Wood Elves.** Turn 3: an untapped Forest; a body for Chord's convoke; a land under Ashaya.
- **Tireless Provisioner.** A Treasure per entry: mana on opponents' turns for instants and the Coffin, and Ragost
  ammunition. Loop A piece.
- **Earthbender Ascension.** Turn 3: a basic and a 2/2 land. After four entries each entry is a counter with trample
  (Terrasymbiosis draws, the Pantry stocks).
- **Wrenn and Realmbreaker.** Every artifact-land becomes a rock; +1 makes a hexproof 3/3 land that blocks; −2 digs for a
  permanent. Its ramp needs Toph and a non-mana artifact (9 in the list): counted as conditional.

**Landfall and entry payoffs, closers (10, plus four of the ramp cards).**
- **Sabotender.** Turn 2. 1 to each opponent per entry; a reach blocker.
- **Arbaaz Mir** (the English copy; Ezio holds the Spanish one). 1 to each opponent and 1 life per nontoken artifact or legend
  that enters: 24 cards of the list (itself included), and the Coffin, the Baubles, the Lantern and the Harvest every time they return.
- **Tannuk.** 1 to each per entry and a card on the second entry of each turn.
- **Valakut Exploration.** A card per entry; unplayed ones are damage to each opponent at the end step. With a loop it is
  lethal at the end step: protect it until then.
- **Ragost.** Every artifact is a Food: {1}, tap, sacrifice for 3 to each opponent. It untaps at each end step after any
  lifegain. Sacrifice tokens first, then earthbent artifacts (they return). Never sacrifice the Coffin unless earthbent.
- **Goblin Bombardment.** Sacrifice earthbent lands after Toph's end step (one more entry), anything in response to a wipe,
  Archers' tokens for reach. Loop C outlet.
- **Fire Nation Archers (new).** A 3/4 reach blocker on turn 4 that never attacks. Late: every spare {5} is 2 to each opponent
  and a 2/2 (a chump blocker, convoke for Chord, Bombardment fodder), at instant speed, with no tap, the turn it lands.
  With Cobra AND Provisioner in loop A it turns the infinite mana into a kill with no pinger. Bad early.
- **Springheart Nantuko.** Loop A key; it must be CAST with bestow (Chord cannot fetch it for the loop). Alone it makes a
  land copy per {1}{G} or a 1/1 per entry.
- **Tireless Tracker.** A Clue per entry; crack them on opponents' turns. Each Clue is also a counter for Terrasymbiosis and
  the Pantry.
- **Zuran Orb.** Sacrifice earthbent lands and cracked fetches: re-entries, life for Ragost, insurance against land removal.
  Loops B and C.
- **Druid Class, Lotus Cobra, Tireless Provisioner, Earthbender Ascension** count here too (listed above).

**Card flow (9 effective draw pieces) and tutors (10 nonland cards and Urza's Cave).**
- **Terrasymbiosis.** Toph's end step draws 2 every turn, 3 with Hardened Scales; Seismic Tutelage's doubling draws that many.
- **Stocking the Pantry (new).** Turn 1. Every earthbend, every Clue cracked with Tracker out and every Ascension counter
  stocks one card for {2}. It is the sink that turns the flood into cards. Bad early without a counter source.
- **Ichor Wellspring.** A card on entry and one when it dies (Ragost, Zuran Orb); earthbent it draws two a cycle.
- **Mishra's Bauble.** 0 mana: a free entry; earthbent it is a free card every turn.
- **Soul-Guide Lantern (new).** 1 mana: an entry that exiles a card from a graveyard, again every time it returns; the
  sacrifice exiles every opponent's graveyard (the deck's graveyard hate) or draws. Earthbent: {1} for a card every turn.
- **Brightglass Gearhulk.** Turn 5 or later ({G}{G}{W}{W}). It fetches two of: Zuran Orb (loops), Mishra's Bauble, the
  Lantern, Hardened Scales, Stocking the Pantry, Sol Ring, Wayfarer's Bauble, Chalice, Haywire Mite. A 4/4 first-strike
  trampler for The Earth King. Bad early.
- **Seismic Sense.** 1 mana, a Lesson. From 6 lands it finds a pinger, Nantuko or Gruul Turf.
- **Chord of Calling.** Instant; convoke with land creatures and Archers' tokens. Cobra (X=2) or Provisioner (X=3) for loop
  A; Sabotender or Arbaaz (X=2), Tannuk (X=3); Haywire Mite (X=1) as an answer; Archers (X=4); Ashaya (X=5). Bad early.
- **Crop Rotation (Game Changer).** Instant. Sacrifice the earthbent land (it returns) for Gruul Turf, Urza's Cave, Ba Sing Se
  or Secret Tunnel. It also saves a land from removal.
- **Urza's Cave (new, a land).** {3}: any land onto the battlefield, two entries. Earthbent it does that every turn. It finds
  Gruul Turf for loop B, Secret Tunnel for Tutelage, a fetch land for more entries.
- **Toph, Hardheaded Teacher.** Each spell earthbends 1 (2 with Scales): more targets a turn, so the Coffin and a value
  artifact can both be earthbent. Her entry regrows Harrow or a removal spell. Loop B hub.

**Land army and counters (7).**
- **Hardened Scales (new; the owner's card).** Turn 1 or from the Gearhulk. Every earthbend is one counter bigger: the lands
  Toph makes are 3/3, a land earthbent twice is 6/6 (an Earth King attacker), Terrasymbiosis draws 3. Bad when no counter
  source is out.
- **The Earth King** (proven). Turn 4. The bear and every power-4+ attacker fetch a basic each combat.
- **Seismic Tutelage** (proven). On an earthbent Secret Tunnel (unblockable) or the bear; never on a land you plan to
  sacrifice. Its counters double each attack. Bad early.
- **Toph, the Blind Bandit.** Earthbend 2 on entry; her power counts every counter on your lands. Loop C piece.
- **Bumi, Unleashed.** Earthbend 4 (5 with Scales): a hasty attacker for The Earth King at once. When he connects, every
  land untaps and the land creatures attack again. Bad early.
- **Ashaya, Soul of the Wild.** Every creature you cast is a land entry; Planar Outburst then spares your team. Loops with
  Bumi and with the Bandit. Bad early.
- **Annie Joins Up.** 5 damage to the biggest creature, then every legendary trigger doubles: Toph earthbends twice (the
  Coffin AND a value target), Tannuk and Arbaaz ping twice, The Earth King fetches twice. Bad early.

**Interaction (7 spot answers, Drannith, the wipe; Annie is above) and protection (5).**
- **Swords to Plowshares, Path to Exile.** 1 mana, for the must-answer creature or commander.
- **Fateful Absence.** 2 mana, creature or planeswalker.
- **Beast Within, Chaos Warp, Stroke of Midnight.** 3-mana instants for any permanent (Stroke: nonland). Keep one up from
  turn 5 for a combo piece.
- **Haywire Mite.** 1 mana; instant-speed exile of a noncreature artifact or enchantment. Earthbent it does it every turn.
- **Collective Resistance, Origin of Metalbending.** 2-mana instants. Their main job is the shield (hexproof plus
  indestructible, or indestructible plus a counter that draws with Terrasymbiosis); their other mode destroys an artifact or
  enchantment. Each counts in ONE job per game state.
- **Drannith Magistrate (Game Changer).** Turn 2: no opponent casts a commander from the command zone, or anything from a
  graveyard or exile. It draws removal; that removal is not aimed at a pinger.
- **Planar Outburst.** The reset when behind on board; best with Ashaya out or Make a Stand in hand. Bad early.
- **Redirect Lightning.** {R} plus {2} or 5 life: moves any single-target spell or ability, a counterspell included (onto the
  Redirect). The only stack tool.
- **Make a Stand.** Team indestructible against a destroy or damage wipe. Bad early.
- **The Stasis Coffin (new; the owner's card).** 3 mana, then {2} a turn with Toph: protection from everything on every
  opponent's turn, and each return is an entry and an Arbaaz ping. Activate it at your own end step when in doubt. Holding the {2}
  until the attack or the spell that matters saves mana, but an opponent can kill or exile the earthbent Coffin first (it
  returns tapped, so no protection that turn cycle). Without Toph it is a one-shot. Bad early.

**Lands (38).**
- **Command Tower, Exotic Orchard.** Untapped fixing.
- **Ba Sing Se.** Untapped with a basic; {2}{G}: earthbend 2, a sink that feeds Terrasymbiosis and the Pantry.
- **Rootbound Crag, Sunpetal Grove, Clifftop Retreat; Game Trail, Fortified Village, Furycalm Snarl; Rugged Prairie;
  Battlefield Forge.** Untapped or conditional duals.
- **Secret Tunnel.** The unblockable earthbend target.
- **Urza's Cave.** Above.
- **Gruul Turf.** Loop B; it also bounces an artifact or a fetch land to reuse it.
- **Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape.** Two entries each, three when earthbent before the crack.
- **10 Forest, 5 Mountain, 6 Plains.**

Multi-role count (R4): 41 of 61 nonland cards do two or more counted jobs. Commander-centric count (R5): 3 cards are near
blank without Toph (the Coffin after its one shot, Zuran Orb, Chalice for 0); Scales, the Pantry and Terrasymbiosis keep 9
other counter sources. Far under 12.

## 3. Curve and ratios

| MV | 0 | 1 | 2 | 3 | 4 | 5 | 6+ |
|---|---|---|---|---|---|---|---|
| Cards (61 nonland) | 3 | 11 | 20 | 18 | 6 | 3 | 0 |

Average MV 2.36 (today 2.36; Bracket 3 median 3.11). 34 cards cost 2 or less. Creatures 20, nontoken artifacts 14, instants
14, enchantments 10, sorceries 5, planeswalkers 1.

| Function | Tier | Min / target | Actual | Reason for this commander |
|---|---|---|---|---|
| Lands | band | 38-40 | 38 | Bottom of the landfall band: average MV 2.36 and 20 ramp cards; flood is spent by 9 sinks. A 39th land was simulated: +1.7 points of Toph on turn 4, at the price of the weakest spell; not taken. |
| Ramp | base | 20 / 22 | 20 by tag: 19 unconditional + Wrenn (needs Toph and a non-mana artifact) | Landfall floor 18 + 2 for a 4-MV commander. 12 of them cost 2 or less (was 11). Roiling Regrowth left for the Pantry: the ramp sits AT the floor on purpose, because the honest draw count was the shorter line. |
| Land entries | gate, early | 12 / 16 | 19 cards that work without Toph + 3 that need her (Zuran Orb, Mishra's Bauble, Soul-Guide Lantern); the gate counts 26 with Toph and the tutors | The fuel. 98 % to see one in 12 cards. |
| Extra land drops, repeatable | support | 5 / 7 | Druid Class, The Earth King, Ashaya; with Toph's earthbend: Heaped Harvest, Wayfarer's Bauble, Urza's Cave, Zuran Orb, Goblin Bombardment, Gruul Turf; Explore (one-shot, half) | Three work without Toph; the rest are her re-entry pairs. Short of 5 without her: she is the engine of this line, and the notes say so. |
| Land recursion | support | 3 / 5 | 4 | Zuran Orb, Bombardment, Gruul Turf, Wrenn's emblem; Toph's earthbend is the fifth. |
| Landfall payoffs | gate, early | 10 / 12 | 9 + 2 tutors | 78 % by turn 5. |
| Access to the drain route (R18) | champion line | 10 | 9: Sabotender, Tannuk, Valakut, Arbaaz, Ragost, Bombardment, Archers + Chord, Seismic Sense | 71 % by turn 5 and 76 % by turn 7 from natural draws (Monte Carlo); the five engines raise it. One short: Water Tribe Rallier was the tenth and found a creature in 60 % of its {5} activations; no better access card is free in the pool (Reckless Fireweaver is Kilo's closer, section 7). |
| Draw (cards that net cards) | base | 10 / 12 | **9 effective**: Terrasymbiosis, Stocking the Pantry, Tireless Tracker, Valakut, Tannuk, Ichor Wellspring, Gearhulk (2 cards), Wrenn (−2) = 8; Mishra's Bauble and Soul-Guide Lantern loop with Toph's earthbend and count half each | WARN, reason below. Explore is a cantrip and is not counted. |
| Spot answers | base | 6 / 8 | 7 dedicated + Annie; Collective Resistance and Origin of Metalbending are counted as protection | R19: 9 with the two modal cards, 6 at MV 2 or less, 8 instants plus the Mite's ability, none above 3 mana, 6 hit artifacts, 6 hit enchantments, 6 stop a creature at instant speed. |
| Wipes | base | 1 / 2 | 1 | A land board survives creature wipes; one reset that spares it. |
| Commander protection | base | 3 / 4 | 4: Redirect Lightning, Make a Stand, Collective Resistance, Origin of Metalbending | Enabler class. The Stasis Coffin carries the protection tag too, but it protects the PLAYER: the gate shows 5, the commander count is 4. |
| Win-turn shield (R24) | champion line | 3 | Redirect Lightning, Collective Resistance, Origin of Metalbending | All at 1 to 3 mana at instant speed. |
| Wipe insurance | support | 2 / 3 | Make a Stand, Goblin Bombardment, Valakut (an enchantment) | Plus the earthbent lands that return. Haystack left: it covered one creature. |
| Mana sinks | support | 3 / 4 | 9 | Archers, Ba Sing Se, Urza's Cave, the Coffin, the Pantry, Tracker's Clues, Ragost, Druid Class, Secret Tunnel. |
| Tutors | Bracket 3 median 4 | | 5 | Chord, Seismic Sense, Crop Rotation, Brightglass Gearhulk, Urza's Cave (new). |
| Game Changers | at most 3 | | 2 | Crop Rotation, Drannith Magistrate. No third one is owned in Naya (pool `game_changer` flags and the live list of 53). |
| Lands + lasting ramp (R8) | 46+ | | 38 + 19 | Lands are two thirds of the sum. |
| Always-tapped lands (R10) | 3 | | 4: Gruul Turf and three fetch lands | One fewer than today (Cabaretti Courtyard left). Each fetch pays back with two or three entries. Written exception. |

Fit check, each card once: 38 lands + 20 ramp + 10 payoffs and closers + 10 card flow and tutors + 7 army and counters + 9
answers (7 spot, Drannith, the wipe) + 5 protection = 99. Lotus Cobra, Provisioner, Ascension and Druid Class are payoffs
counted with the ramp; Urza's Cave is a tutor counted with the lands.

**WARN, draw 9 against 10.** The count is honest: only cards that net cards, the two loop cantrips at half weight.
- Four of the nine are engines that give two or more cards a turn (Valakut, Tracker, Terrasymbiosis, the Pantry) and Tannuk
  gives one; an engine is on the table by turn 7 in 55 % of games from natural draws.
- The frozen pool has no other Naya card that nets cards at 3 mana or less without combat: checked all 64 pool cards with
  "draw" in their text. The next candidates are combat-tied or loop cantrips: Bitter Work (needs a power-4 attacker),
  Elsewhere Flask and Nutrient Block (more loop cantrips for the one earthbend a turn).
- No table-scaling draw is owned (Esper Sentinel, Smothering Tithe): R16 stays open.
- I did not tag the Lantern, Explore or Seismic Sense as draw to reach 10.

**Orphans by the gate: 2.** Drannith Magistrate (declared: a stax Game Changer outside the plan) and Hardened Scales (a bridge
card: a multiplier of the commander's own action, in no gate function because the army is the backup).

**Dead clauses (owner's lesson L7): what each conditional card needs, counted in this list.**

| Card | Needs | Count in the list | Verdict |
|---|---|---|---|
| Arbaaz Mir | nontoken artifacts and legends entering | 24 cards, and every return of an earthbent artifact | live |
| Ragost | artifacts to sacrifice; lifegain to untap | 14 nontoken artifacts, Treasures (Provisioner), Clues (Tracker); lifegain from Arbaaz, Druid Class, Zuran Orb, Haywire Mite, any Food ability | live |
| Hardened Scales, Terrasymbiosis, Stocking the Pantry | +1/+1 counters put on my creatures | Toph every turn, plus Hardheaded Teacher, Blind Bandit, Bumi, Earthbender Ascension, Ba Sing Se, Tireless Tracker, Seismic Tutelage, Origin of Metalbending, Planar Outburst's awaken: 10 sources | live with Toph; slow without her (3 repeatable sources) |
| The Stasis Coffin | Toph on the battlefield for the lock | the commander; Annie and the Teacher add earthbends | live with Toph, one shot without |
| The Earth King | attackers with power 4+ | its own bear, Gearhulk, Bumi and his land, Ashaya, the Bandit, any land earthbent twice | live |
| Seismic Tutelage | a creature with counters that attacks | every earthbent land; Secret Tunnel first | live (proven) |
| Brightglass Gearhulk | artifacts, creatures, enchantments of MV 1 or less | 9: Zuran Orb, both Baubles, Sol Ring, Chalice, Lantern, Haywire Mite, Scales, the Pantry | live |
| Springheart Nantuko (loop) | a land creature and Cobra or Provisioner | 8 ways to animate a land; 2 partners, Chord finds both | loop in few games; alone it still copies a land or makes a 1/1 |
| Toph, Hardheaded Teacher (Lesson clause) | Lessons | 5: Shared Roots, Cycle of Renewal, Seismic Sense, Origin of Metalbending, Redirect Lightning | a bonus only; her earthbend works on all 61 spells |
| Annie Joins Up (doubling) | legendary creatures with triggers | Toph, Tannuk, Arbaaz, The Earth King, the Teacher, the Bandit, Bumi: 7 | live |
| Wrenn and Realmbreaker (mana) | artifacts with no mana ability, with Toph | 9 | conditional; its other two abilities carry it |
| Great Divide Guide (Ally clause) | Allies | Toph and 5 creatures | a bonus; it is a dork and a fixer alone |
| Water Tribe Rallier, Alibou, Inscription's fight | see section 6 | | out |

Other dead text, none load-bearing: Fateful Absence gives a Clue to the opponent; Wrenn's −7 is never the plan; the Coffin
does nothing for the board; the Blind Bandit has power 0 with no counters on lands.

**Toughness.** 11 of the 20 creatures have toughness 2 or less. They are engines, not attackers (the attackers are lands
that return), so the combat rule of a third does not apply; against pingers and small wipes they are covered by Make a Stand,
Collective Resistance, Origin of Metalbending and by the three enchantment payoffs that do not die.

### Mana
**Colored sources** (lands; Exotic Orchard 0.75; a fetch land 2/3 of each color):

| Color | Pips in the 61 spells | Cards that need it | Land sources | With rocks, dorks and cheap land ramp (Karsten weights) | Karsten target |
|---|---|---|---|---|---|
| Green | 39 | 34 (14 at MV 2 or less) | 19.8 | about 21.5 | 19 for {1}{G} on turn 2 |
| Red | 12 | 12 (5 at MV 2 or less) | 15.7 | about 20.5 | 17 for Toph on turn 4, 19 on turn 3 |
| White | 13 | 11 (6 at MV 2 or less) | 15.7 | about 20 | 17 for Toph on turn 4, 19 on turn 3 |

Basics 10 Forest, 6 Plains, 5 Mountain follow the pips. {G}{G}{W}{W} (Gearhulk) and {3}{W}{W} (Outburst) want 26 white
sources on curve: they are turn-6 cards here, as played.

**Odds of casting Toph on time WITH colors** (scratch simulator, 20,000 games: 99 cards, free first mulligan, 7 + N cards by
turn N, tapped and conditional lands, fetches, the 18 ramp cards of MV 3 or less it models, color-aware payment):

| | Turn 3 | Turn 4 | Turn 5 |
|---|---|---|---|
| This list, with colors | 53 % | 89 % | 93 % |
| This list, mana only | 61 % | 95 % | 97 % |
| Today's list, with colors | 51 % | 89 % | 94 % |

- Three colors cost 6 points on turn 4, about 2 per color (green alone already costs 3: Secret Tunnel, Urza's Cave and the
  filter land make no green).
- No single land swap moved the result by more than 0.6 points (Jungle Shrine, Mossfire Valley, basics moved between colors
  were all tested): the base is balanced.
- Urza's Cave costs 0.6 points on turn 4 against Cabaretti Courtyard; Talisman of Conviction gives 3 points on turn 3.
- Untapped lands: 21 basics, Command Tower, Exotic Orchard, Battlefield Forge, Rugged Prairie, Secret Tunnel, Urza's Cave
  always; Ba Sing Se, 3 check lands and 3 reveal lands usually; Gruul Turf and 3 fetches never.

**Opening hand.** Keep 72.7 % of first sevens, 92.4 % with the free mulligan (40,000 hands; target 85 %).

## 4. Interaction plan and protection plan

**Interaction.**
- The 1-mana exiles go to commanders and engines, never to a mere big creature that the Coffin or a chump can handle.
- From turn 5 keep one instant up on opponents' turns for a combo piece: Beast Within, Chaos Warp, Stroke of Midnight,
  Fateful Absence.
- Artifacts and enchantments: the Mite first (it repeats when earthbent), then the three 3-mana instants, then the removal
  mode of Collective Resistance or Origin when no shield is needed.
- Graveyards: the Lantern's entry trigger exiles the reanimation target; its sacrifice exiles all opposing graveyards.
- Drannith early against commander decks. Planar Outburst only when behind.
- Politics: the drain is symmetric and visible. Until the deck can kill in two turns, ping with one pinger and offer removal
  on the table's leader. Say out loud that attacking you is a bad deal (blockers that return; the Coffin).

**Protection.**
- Toph is an enabler: protect her when her end step matters (the Coffin lock, a loop turn, Terrasymbiosis out).
- Pingers and loop pieces: Collective Resistance or Origin against destroy and damage, Redirect Lightning against any
  single-target spell, Make a Stand and Bombardment against a wipe.
- **The Coffin.** Cast it with {2} left (5 mana that turn). It does not protect the board: opponents will aim at Toph or at
  the Coffin on your turn, so keep a shield for Toph while it runs. It does not stop life loss or mill.
- **Win turn.** 1) {R} plus {2} (or 5 life) open for Redirect; 2) the loop piece; 3) Collective or Origin for the response.
  Loop B is main phase only. Valakut's kill waits for your end step. Never show lethal one turn before you can protect it.
- **Rebuild after a wipe (R32).** Lands and earthbent lands stay, Valakut, the Pantry and Terrasymbiosis stay, Toph costs 4 or
  6, Chord and Seismic Sense find a pinger, Archers make bodies, the Teacher regrows a spell. Commit what wins in two turns.

## 5. Mulligan and play pattern

**Keep:** 2 to 4 lands (2 only with a ramp piece of 2 mana or less; 5 with a play of 3 mana or less), a play by turn 2 or 3, and a
plan piece or a way to find one (Toph herself counts when the mana is there). Keep almost any land-good hand with Sol Ring,
Lotus Cobra, a pinger, Tireless Tracker or Terrasymbiosis.
**Ship:** 0 or 1 land, 6 or more, 2 lands with no cheap ramp, no play before turn 4, answers only.

**20 seeded hands** (seed 20261115): 13 keep, 7 ship. The ships: 3, 10, 19 and 20 (one land; hand 3 has Sol Ring and is still
a ship), 8, 11 and 15 (two lands, no cheap ramp). Rate over 40,000 hands: 72.7 % and 92.4 % with the free mulligan.

**Play pattern.**
- **Turns 1 to 5.** Turn 1 Sol Ring, Wayfarer's Bauble, the Pantry or Scales. Turn 2 ramp, or a 2-mana pinger with a rock
  already down. Turn 3 Toph, or a pinger plus a 1-drop. Turn 4 a pinger and land ramp, cheap artifacts after the pinger.
  Turn 5 an engine (Tracker, Terrasymbiosis, Valakut) or the Coffin with {2} up.
- **Turns 6 to 9.** Three to four entries a turn. Fire Ragost at every end step. Crack Clues and the Pantry with spare mana;
  Archers take what is left. Assemble a loop behind Redirect or Collective. Attack with the earthbent land only when it is
  free (it returns) or when The Earth King or Tutelage pay for it.
- **Late.** Archers, Urza's Cave, Ba Sing Se and Druid Class level 3 sink the flood. The Coffin every turn. One player at a
  time dies to the Tunnel with Tutelage while the pings finish the others.

**Goldfish, 5 games to turn 8** (seeded hands 1, 2, 4, 5 and 7, played by hand):

| Game | Toph cast | Plan online | Damage to each opponent by turn 8 | Note |
|---|---|---|---|---|
| 1 | T3 | T7 (Tannuk) | 4 | Pantry turn 1, Terrasymbiosis turn 5, 20 cards seen by turn 7 and no pinger before the 20th: the engines dug to it |
| 2 | T3 | T5 (army) | 0 drain; 25 to 30 combat on one or two players | No pinger in 16 cards; Ascension, Gearhulk (Orb and Bauble) and the Teacher grow an 8/8 land |
| 4 | T4 | T6 (Bombardment, Tracker) | about 6 | Tracker makes 6 Clues by turn 6; Chord on turn 8 fetches Tannuk |
| 5 | T3 | T7 (Tannuk) | about 3 | Cobra gives Toph on turn 3; Ragost has no artifacts; the Coffin and the Pantry on turns 5 and 6 |
| 7 | T3 | T4 (Tannuk) | about 18 | Tannuk, the Bauble loop, Arbaaz on turn 6: 6 to 7 a turn |

Reading: Toph lands on time. The drain alone kills around turn 10 to 12 and starts late in three games of five. That is the
deck's real limit (9 access cards), and it is why the Coffin, the Pantry and the army are in.

**Disrupted goldfish.**
- **(a) Toph removed the first time she acts.** Land ramp and pingers keep working; the Coffin, Scales and the loop cantrips
  wait. Recast for 6 on turn 5 or 6: one turn lost.
- **(b) Wipe on turn 6.** Make a Stand or Bombardment in response. Otherwise the pingers die and the lands, Valakut, the
  Pantry, Terrasymbiosis and Bombardment stay; Toph again on turn 7, Chord or Seismic Sense for a pinger: threatening again
  on turn 8 or 9.
- **(c) First loop attempt countered.** With Redirect the counter fizzles on itself. Without it one piece is lost and the
  drain goes on: one or two turns lost.

**Gauntlet (R39).**
- **Fast combo, turns 5 to 7.** 8 instants and the Mite on their turn; Drannith stops command-zone and graveyard casts; the
  Coffin stops a targeted kill and a combat kill. Weak against a spell combo that does not target: no counterspell.
- **Stax and taxes.** Three 0-cost artifacts and 11 one-drops; 6 answers each to artifacts and enchantments; 21 basics.
- **Go-wide tokens.** Board 1 above; the Coffin makes their attack worthless.
- **Big creatures.** Board 2 above.
- **Control with counters and wipes.** Instant-speed ramp and Chord at their end step, threats on four permanent types,
  Redirect on the key turn, lands that return.

## 6. The owner's cards (review of 2026-11-14)

Only the cards inside Toph's colors need a verdict; the blue, black and multicolor cards of the review are not in this pool.

| Card | Verdict | Reason |
|---|---|---|
| **The Stasis Coffin** | **IN** | With Toph it is protection from everything on every opponent's turn for {2}, and each return is a land entry and an Arbaaz ping (Lotus Cobra pays half). The earlier cut said it "eats Toph's earthbend": wrong weight. The deck kills around turn 10 and has no counterspell, so the turns it buys are worth more than one extra card a turn; Terrasymbiosis, the Pantry and Scales still get their counters from the same earthbend. It takes Hardlight Containment's slot. |
| **Hardened Scales** | **IN** | 1 mana, fetched by the Gearhulk. Every earthbend gets one more counter: Toph every turn, the Teacher on every spell, Bumi, the Bandit, Ascension, Ba Sing Se, Tracker, Tutelage (10 sources). It draws one more card with Terrasymbiosis and makes the backup army half again as big, which is the route that won his games. The older owner decision "Hardened Scales: out" (iteration 2) is replaced by his review of 2026-11-14. It took Haystack's slot. |
| **Inscription of Abundance** | **OUT** | Each of its three modes has a better card in the list. Removal: its fight needs a board (an earthbent land with 4 or more counters, or one of Gearhulk, Bumi, Ashaya and the bear; the other creatures are engines with toughness 2 to 4 that I would not risk), so it fails exactly when the deck is behind, after a wipe or with Toph dead, and it never answers an artifact, an enchantment or a combo piece; Swords and Path do it for 1 mana and Fateful Absence for 2 with no condition, and Chaos Warp, the card it would replace, answers any permanent. Counters: Toph's earthbend and Origin of Metalbending (which also gives indestructible and is a Lesson for the Teacher). Lifegain for Ragost: Zuran Orb for 0, Druid Class, Arbaaz. All three modes together cost 5. If he wants it anyway, it replaces Chaos Warp. |
| **Alibou, Ancient Witness** | **OUT** | Its trigger needs an artifact creature that ATTACKS: the list has two (Haywire Mite 1/1 and Gearhulk) plus at most one earthbent artifact a turn. For 5 mana it then damages ONE target. Ragost does the job better: 2 mana, 3 damage to EACH opponent per artifact, no attack. At 5 mana Bumi and Ashaya each open an infinite line. |
| **Return the Favor** | **OUT** | One copy, in Azula, where copying instants is the plan. Here its redirect mode costs {R}{R}{1} with 16 red land sources; Redirect Lightning does it for {R} plus {2} or 5 life. Not contested. |
| **Commander's Sphere** | **OUT** | No free copy (Kilo and Ezio hold them). At 3 mana it competes with Toph's own turn; Talisman of Conviction (free, 2 mana) ramps a turn earlier, and Soul-Guide Lantern (free, 1 mana) does the earthbend-sacrifice-draw trick for less. Not contested. |
| **Tome of Legends** | **OUT** | One copy, in Azula, who attacks every turn. Toph does not attack: it would draw two cards a game. Stocking the Pantry does this job here: a card for every earthbend. |
| **Water Tribe Rallier** (in today; he asked for a judgment) | **OUT** | His doubt is right. Waterbend {5} looks at four cards for a creature of power 3 or less: it hits in 60 % of activations (17 such creatures in about 85 cards), and before turn 5 it is a vanilla 2-drop. Fire Nation Archers takes the slot: the same late mana becomes 2 damage to each opponent and a body, every time. |

Also re-examined from his original list (`data/raw/Toph.txt`), all still out: Mindslaver, Moraug, Omnath, both Titanias,
Hour of Revelation, the three Bridges, Darksteel Citadel, Rockalanche, Badgermole (cut log, section 8). Urza's Cave and
Stocking the Pantry, both from his original list, are back.

## 7. Copies

**Nothing is claimed from Kilo and nothing is contested with Azula or Ezio.** All seven new cards have a free copy.

| Card | Copies | Where | Decision |
|---|---|---|---|
| Arbaaz Mir | 1 Spanish (scanned), 1 English (owned, not scanned) | Ezio took the Spanish copy in step 11 | Toph plays the English copy (`pending_owned`). |
| Soul-Guide Lantern | 2 Spanish | Kilo 1, free 1 | Toph takes the free Spanish copy. |
| The Stasis Coffin, Hardened Scales, Stocking the Pantry, Talisman of Conviction, Fire Nation Archers, Urza's Cave | 1 English each | free | Taken. Each is the only copy; no other list plays them (Ezio's notes leave the Coffin, Scales, Inscription and Alibou to Toph). |
| Reckless Fireweaver | 1 Spanish | Kilo | **Not claimed.** It would be a fifth pinger here (every artifact entering, Treasures and Clues included). In Kilo it is the kill of its Meticulous Excavation loop and one of three cards of its burn route; Kilo already gave Arbaaz away. It adds more there. Fire Nation Archers plays instead. If the lead decides the other way, Fireweaver replaces Stroke of Midnight here and Kilo needs a new finisher for its loop. |
| Deflecting Swat | 1 English | Azula | Not contested. Here it would be a free shield on the loop turn; Azula is an attack engine that copies it. Toph's fallback is Redirect Lightning, already in. |
| Fellwar Stone, Swiftfoot Boots, Hakoda, Mind Stone | 1 or 2 | Ezio, Azula | Not contested: Talisman of Conviction, the shields and Make a Stand do these jobs from the binder. |

Spare copies of strong staples, checked for the whole pool (155 non-basic cards with two or more copies and one free):
Chromatic Lantern (free; out, cut log), Bender's Waterskin, Blasphemous Act (2), Mindslaver (2), Reckless Handling (3),
Sandbenders' Storm (4), Badgermole (4), Rogue's Passage, Rumble Arena (2), Path of Ancestry (2), Jungle Shrine: each has a
line in the cut log. Arcane Signet, Rampant Growth, Evolving Wilds, Terramorphic Expanse, Heaped Harvest, Origin of
Metalbending, Cycle of Renewal, Seismic Sense, Stroke of Midnight, Bumi and the Blind Bandit are played and leave spares.

**Language.** English wherever an English copy is free. Spanish copies in the list (14): Lotus Cobra, Chord of Calling,
Swords to Plowshares, Path to Exile, Fateful Absence, Planar Outburst, Make a Stand, Exotic Orchard, Clifftop Retreat,
Fortified Village, Rugged Prairie, Battlefield Forge, Vibrant Cityscape (all as today) and Soul-Guide Lantern (new). Each
has no free English copy. Stocking the Pantry is a foil (BLB 194).

## 8. Changes against the deck as built today

| OUT (goes to a binder) | Why | IN (comes from) | Why |
|---|---|---|---|
| Hardlight Containment (English binder) | The weakest answer: an Aura that needs a host artifact the deck does not sacrifice or earthbend, undone by one removal. Spot answers 10 to 9 (7 dedicated), still over the target of 8. | **The Stasis Coffin** (English binder, BRO 245) | The owner's card; the lock of section 1. |
| Haystack (English binder) | Protects one creature for {2} a turn. Commander protection 5 to 4 (target 4); wipe insurance 4 to 3. | **Hardened Scales** (English binder, FIC 307) | The owner's card; a counter more on every earthbend. |
| Water Tribe Rallier (English binder) | Section 6. | **Fire Nation Archers** (English binder, TLE 237) | A closer and the best sink: {5} for 2 to each opponent, no tap. |
| Legion Guildmage (English binder) | {5}{R} and a tap for 3 to each opponent once a turn; Archers do it better and Guildmage was no early access. Its tap ability is lost. | **Talisman of Conviction** (English binder, TDC 329) | The 12th ramp piece of 2 mana or less: Toph on turn 3 in 53 % instead of 51 %; a red-white source. |
| Roiling Regrowth (English binder) | The weakest of three "sacrifice a land, two basics" instants (tapped basics, not a Lesson). Ramp 21 to 20, the floor. | **Stocking the Pantry** (English binder, BLB 194 foil) | A fifth card engine; the honest draw count goes from 8 to 9. |
| Return to Nature (Spanish binder) | Its graveyard mode moves to the Lantern. Artifact and enchantment answers 7 to 6 each. | **Soul-Guide Lantern** (Spanish binder, EOC 143) | Graveyard hate that is an entry, a ping and a card, every turn when earthbent. |
| Cabaretti Courtyard (English binder) | The one fetch that cannot wait to be earthbent. Land entries: 22 cards (21 today). | **Urza's Cave** (English binder, MH3 234) | A land tutor that repeats with the earthbend; untapped. |
| Arbaaz Mir, Spanish copy (to Ezio, decided in step 11) | | Arbaaz Mir, English copy (owned, not scanned) | Same card. |

**Cut log (cards considered and left out).**

| Card | Function it would serve | Why not |
|---|---|---|
| Chromatic Lantern (free) | Mana from artifact-lands | 9 of 12 public lists play it, with 17 to 22 artifacts. Here Wrenn and Great Divide Guide already do it, 9 artifacts lack a mana ability, and mana is not the short resource. A 3-mana rock is not early ramp (R9). |
| Reckless Handling (3 free) | Tutor for the Coffin, the Orb, the Harvest | Sorcery, random discard, one card down; the Gearhulk finds the Orb and nothing of the plan depends on one artifact. |
| Mindslaver (2 free) | Control of one opponent every turn with Toph | 6 mana plus {4} a turn, on one player of three; a griefer line that draws the whole table. No 6-drop in the list. |
| Moraug, Omnath, Rampaging Baloths, both Titanias | Army finishers | 5 to 7 mana and all combat; the owner decided "keep the curve" and the list has three 5-drops that each open a loop. |
| Bitter Work (2 free) | Combat-tied draw | Needs a power-4 attacker most turns; counted half. The Pantry draws without attacking. First candidate if the draw line must reach 10 (it would replace Seismic Sense). |
| Elsewhere Flask, Nutrient Block, Brainstone, Mycosynth Wellspring | Loop cantrips | Toph gives one earthbend a turn and the list has 9 good targets already. |
| Hour of Revelation, Blasphemous Act, Karn's Sylex | Wipes | They kill my enchantment engines or my pingers; Planar Outburst spares the lands and the enchantments. |
| Liquimetal Coating | Bumi infinite combats | Its only job; Bumi + Ashaya is the same line with two good cards. |
| Darksteel Citadel, the three Bridges, Rumble Arena, Rogue's Passage, Jungle Shrine, Mossfire Valley | Lands | Colorless or always tapped; every swap was simulated and none helped Toph's cast odds. |
| Sandbenders' Storm, Earth Kingdom General, Badgermole, Rockalanche, Earthbending Lesson, Bumi, Eclectic Earthbender | More earthbend | 3 to 5 mana for what Toph does free every turn; the backup needs multipliers (Scales), not more sources. |
| Insidious Fungus | A 1-mana body that later destroys an artifact or enchantment or draws | The best replacement for Return to Nature if the lead wants a seventh answer; it would take Seismic Sense's slot. |
| Stroke of Midnight (stays), Haystack, Roiling Regrowth, Hardlight Containment, Legion Guildmage, Return to Nature | | First replacements, in this order, if a new card fails in play. |

**Final cut pass, the 10 weakest nonland cards of the new list**, each against the best unplayed candidate:

| # | Card | Best candidate | Decision |
|---|---|---|---|
| 1 | Seismic Sense | Bitter Work | Keep: the only card that finds Nantuko; R18 (never trade a tutor for generic draw). |
| 2 | Shared Roots | Chromatic Lantern | Keep: turn-2 land ramp works without Toph and after an artifact wipe. |
| 3 | Everflowing Chalice | Elsewhere Flask | Keep: turn-2 rock, free landfall, loop B. |
| 4 | Chaos Warp | Inscription of Abundance | Keep: an instant answer to ANY permanent in a deck with no counterspell. |
| 5 | Make a Stand | Haystack | Keep: the only team protection. |
| 6 | Explore | Roiling Regrowth | Keep: 2 mana, replaces itself. |
| 7 | Fire Nation Archers | Legion Guildmage | Keep: no tap, repeatable, a 3/4 reach body. |
| 8 | Hardened Scales | Inscription of Abundance | Keep: permanent, 1 mana, every earthbend. |
| 9 | Drannith Magistrate | Insidious Fungus | Keep: a Game Changer that shuts off every opposing commander. |
| 10 | Annie Joins Up | Reckless Handling | Keep: removal plus the doubling of Toph, Tannuk and Arbaaz. |

No swap won. Proven role-players: The Earth King and Seismic Tutelage are both IN.

## 9. Real-power estimate (1-10; 4 precon, 7-8 high power, 9-10 cEDH)

| List | Estimate | Note |
|---|---|---|
| Iteration 1 (`round3-step21`) | 6.6-7.1 | real-power review of 2026-11-08 |
| Today's deck | 7.3-7.7, central 7.5 | final review of 2026-11-08 |
| **This list** | **7.4-7.9, central 7.65** | Confidence medium-low: no game played with it. |

Why higher (+0.15, range +0.05 to +0.3):
- The Coffin: against tables that win by attacking or by targeted burn, the deck stops losing while it drains. This is the
  largest single gain, and it is zero against life-loss, mill and untargeted combo.
- A fifth card engine (the Pantry) and a looping cantrip that is also the graveyard hate.
- Toph on turn 3 slightly more often; a land tutor; a sink that kills.
- The backup army half again as big (Scales).

Why not higher:
- The drain still starts late in about one game in four (9 access cards) and kills around turn 10 to 12 alone.
- No counterspell, no table-scaling draw, no third Game Changer: none is owned in Naya.
- One answer fewer than today (9 against 10 spot answers) and no Haystack.

Commander Salt was not measured (the brief says so). Guess: about the same as today, 7.0 to 7.4.

## 10. Knowledge used

| Source | What it demands of this deck | How the list answers |
|---|---|---|
| Skill `commander-deckbuilding` (SKILL.md, 11 references), upgrade mode 0b | Start from the owner's list; fewest changes that close the gaps; one plan and a backup that reuses its pieces; counts from the fuel | 7 swaps; plan and backup unchanged; every swap named with its function and the count after it (section 8) |
| `archetypes.json`, profile `landfall_lands` | Lands 38-40; ramp 18 (+2 for a 4-MV commander); land entries 12/16; payoffs 10/12; draw 10; removal 6/8; wipes 1; protection by class; support lines; both reference boards at 10 | Profile table in section 3; all gate functions declared under the profile names; one WARN (draw 9) |
| `references/role-players-and-upgrades.md` | Bridge cards judged with the commander out; "bad use is not the card"; timed ramp | The Coffin, Scales and the Pantry are bridges of the earthbend; the Coffin's earlier cut for "eating the earthbend" is reversed; ramp counted by cast turn (12 at MV 2 or less) |
| `references/plan-file.md` and gate review section (f) | Declare every function, tag by the job, name dead clauses, both boards, a noncombat route, say when each card is bad | Plan file rewritten from Oracle text; Collective Resistance and Origin tagged once; Explore, Lantern and Seismic Sense not tagged draw; 2 orphans shown; 12 cards bad early |
| Champion addendum, items 1-3 (one plan, synergy, redundancy) | One plan; every card works alone and with many | Section 2; 25 entry cards, 9 access cards, 5 engines |
| 4, 5 (multi-role; commander-centric) | Many two-job cards; 12 or fewer blank without the commander | 41 of 61; 3 near blank |
| 6-8 (land count, colored sources, total sources) | Lands from curve and ramp; Karsten sources; lands + lasting ramp 46+ | 38 lands argued and simulated; sources table; 38 + 19 |
| 9, 10 (fast mana, tapped lands) | Talismans before 3-mana rocks; at most 3 always-tapped lands | Talisman of Conviction in, Chromatic Lantern out; 4 tapped lands (was 5), exception written |
| 11-14 (window mana, curve, commander MV, higher-power lists) | Instant-speed use of mana; low curve; recast arithmetic; compare with Bracket 4 and cEDH lists | Provisioner Treasures, Archers and the Coffin use mana on others' turns; average MV 2.36; Bracket 4 lists run 34 lands and 18 artifacts, cEDH 29 and 22: this list has 38 and 14 because its fuel is real land entries |
| 15-17 (engines, scaling draw, development first) | Engines over one-shots; draw that scales; cheap draw early | 5 engines; **16 not applied**: none owned in Naya; the Pantry, Scales and the Lantern cost 1 |
| 18 (tutors) | 10 access cards to the primary route; never trade tutors for draw | 9 access cards (one short, reason in section 3); 5 tutors, Urza's Cave added, Seismic Sense kept |
| 19-22 (cheap answers, stack, wipes, graveyard) | 8+ spot answers, 5 at MV 2 or less, 5 instants; non-blue stack tools; a one-sided reset; graveyard hate | 9 / 6 / 8; Redirect Lightning (Deflecting Swat is Azula's); Planar Outburst; Soul-Guide Lantern |
| 23-25 (protection layers, win-turn shield, answers by type) | Hexproof, indestructible, a redirect; 3 shield pieces at MV 2 or less; all permanent types | Collective Resistance, Origin, Redirect, Make a Stand; phasing is gone with Haystack (exile wipes are not covered); 6 answers each for artifacts and enchantments |
| 26-28 (compact routes, disjoint routes, failure points) | Primary route is a board engine or 3 cards; no shared failure point | Route table in section 1 |
| 29-32 (threat, archenemy timing, politics, wipe recovery) | Low profile until the win; deterrents; 4 rebuild pieces | Section 4; the Coffin and returning blockers as deterrents; 6 rebuild pieces |
| 33 (mulligans) | Keep checklist and rate, 85 % target | Section 5: 92.4 % |
| 34-36 (Game Changer slots, efficiency, non-GC high-power cards) | Fill three slots; MV 5+ must win, answer several or refill; consider Bracket 4 and 5 cards | 2 of 3 (no third owned); Bumi and Ashaya open loops, Outburst answers a board; Deflecting Swat, Fellwar Stone and Swiftfoot Boots are in decks already optimized and not contested, Urza's Cave and The Stasis Coffin (both in the Bracket 4 and cEDH lists) are added |
| 37-39 (combos, goldfish, gauntlet) | Legal lines only; 20 hands, 5 goldfish, 3 disrupted; five opponent types | Bracket script PASS, three review items explained; section 5 |
| 40, 41 (cut log; real-game evidence over score) | Every cut logged; proven cards stay | Section 8; The Earth King and Seismic Tutelage in; the owner's two surprises are in on their merits |
| Mana study, `notes/02-mana.md` | Colored sources per pip, untapped early, tapped lands with a payoff, sinks for flood | Sources table; simulated cast odds; 9 sinks |
| `notes/13-ratio-gaps.md` (Karsten K1-K3, Command Zone 2025, EDHREC E1) | 42 lands minus rocks and cantrips; rocks pay with a 4-MV commander; landfall averages 39.5 lands, 7 extra drops, 16 lands put onto the battlefield, 11.5 payoffs | 38 lands with 5 rocks and 12 cheap ramp; 25 entry cards; 11 payoffs with tutors |
| `notes/01`, `08`, `09` (foundations, evaluation, EDHREC use) | Fit over popularity; inclusion is a prior, never a reason | Chromatic Lantern (54 % inclusion) stays out with a reason; Fire Nation Archers (no EDHREC row) comes in |
| `notes/03` (card flow) | 10 pieces that net cards; cantrips are not draw; tutors are not draw | The honest count of 9 and its WARN |
| `notes/04` (interaction, protection) | Spot answers across types; one-sided wipes; protection by layer | Section 4 |
| `notes/05`, `11`, `12` (multiplayer, community, combat) | 120 life: team-wide damage; menace and small pings fail against a wide board; defense while tapped | Routes 1 to 3 hit each opponent; the Coffin is the defense; the army attacks only when it is free |
| `notes/06`, `07`, `10` (archetypes) | Landfall: land ramp over rocks, extra drops need lands in hand, payoffs or the ramp does nothing | 13 land-ramp cards against 5 rocks; 38 lands; the failure mode "ramp with no payoff" is measured (24 % with no access card by turn 7) and named |
| Primers: `toph-the-first-metalbender.md`, `-primers-20261108.md` | Engine: cheap artifacts as land drops, Cobra and Provisioner, Zuran Orb, Crop Rotation; traps: infinite mana with no sink, too few answers, artifact removal hits lands; must-haves owned | The owned must-haves are in, Soul-Guide Lantern and The Stasis Coffin now too; out: Liquimetal Coating (its only job is the Bumi line), Deflecting Swat (Azula's copy), Rampaging Baloths and Omnath (curve), Reckless Handling, Abrade (Azula's copy). Archers is the sink for loop A's mana; 9 instant answers; 21 basics |
| Owner lessons L1-L10 | One plan; ratios from the strategy (far more ramp, repeated entries, no haste); enabler commander; proven cards; dead clauses; both boards; guide by use | Sections 1 to 3; section 2 says how to use each card |
| Play reviews of 2026-10-26 | Coffin "medium-high, keep" with the lock; Inscription "keep"; Scales "watch"; Gearhulk keep; earthbend targets; protection thin against exile | Coffin in; Inscription out with reasons; Scales in; target order in section 2; the exile gap is written in section 4 |
| Final review of 2026-11-08 | Only 3 true landfall pingers; loops 1 game in 8; no scaling draw; Gearhulk and Mishra's Bauble must stay | Unchanged limits, stated; both stay; the Coffin, the Pantry and Scales raise the floor of the non-loop games |
| Iteration-1 lists (`decks/measured/`) and the owner's original list | Learn, not copy: iteration 1 had the Coffin, Scales, Inscription, Soul-Guide Lantern, Chromatic Lantern, Reckless Handling | Coffin, Scales and the Lantern return; the rocks that only worked with Toph do not |
| Owner's card review of 2026-11-14 | A verdict with weight for each card in Toph's colors | Section 6: 2 in, 6 out |
| Web, read 2026-11-15 | | |
| `https://json.edhrec.com/pages/commanders/toph-the-first-metalbender.json`, `.../optimized.json`, `.../upgraded.json`, `.../cedh.json` | Priors: the Coffin 45 % (56 % in Bracket 4), Chromatic Lantern 54 %, Scales 25 %, Urza's Cave 11 % in cEDH | Used to find candidates only; every pool card on those pages has a line in sections 6 to 8 |
| `https://api.scryfall.com/cards/search?q=is:gamechanger` (53 cards), `/cards/collection`, rulings of Toph, The Stasis Coffin, Hardened Scales, Ragost, Alibou, Chromatic Lantern | Game Changers, legality, rules points R2, R3, R9 | Section 1 |
| `https://backend.commanderspellbook.com/variants/` (Toph + The Stasis Coffin, 4155-6871) | The lock's steps and its result | R3 and the bracket note |
| `https://edhrec.com/articles/toph-the-first-metalbender-fire-and-ice/` (Maddalena) | Haywire Mite as an earthbend target; lands rarely attack; the Coffin among the three most played cards | Target order; army as backup |
| `https://cloudflare.edhrec.com/articles/top-10-landfall-cards-for-toph-the-first-metalbender-in-cedh` (DougY) | Cobra and Provisioner first; do not split into +1/+1 counters in cEDH; infinite mana needs a sink | Both in; Scales is one 1-mana card, not a package; Archers |
| `https://draftsim.com/toph-edh-deck/` (Walser) | Its list runs Urza's Cave, Soul-Guide Lantern, Mishra's Bauble, Mindslaver | Three of the four are in |
| `https://edhrec.com/articles/toph-the-metalbender-commander-deck-tech` (Roberts) | Harrow on an earthbent artifact; sacrifice-and-return value | Harrow, Cycle of Renewal |
| `https://archidekt.com/api/decks/v3/?commanderName=...` and 12 lists by views (ids 16258887, 5996567, 17368282, 17888732, 17824522, 15283301, 15231919, 15296372, 17154005, 16428901, 15464527, 17735802) | 33 to 39 lands; Chromatic Lantern 9 of 12, Zuran Orb 8, Moraug 7, Crop Rotation 7, the Coffin 4, Alibou 2, Inscription 0, Rallier 0 | Lantern and Moraug weighed and left out with reasons |
| Moxfield (`api2.moxfield.com` search ignored the commander filter) and Reddit (HTTP 403) | | Not read; no wall was bypassed |

**Knowledge gaps not closed.** No game was played with this list. Reddit and Moxfield primers were not readable. No rule
source was read for R4, R5 and R10 (they follow from Oracle text). The simulator plays greedily (Toph first), so the turn-3
figure is a ceiling for games where a pinger goes first.

**Open questions for the owner.**
1. The Coffin lock makes you untouchable in combat: his table may answer by ganging up on Toph. Is that acceptable in his pod?
2. Drannith Magistrate stops every opposing commander. It stays as the stronger choice; he may prefer Insidious Fungus.
3. If he wants Inscription of Abundance back, it replaces Chaos Warp.
