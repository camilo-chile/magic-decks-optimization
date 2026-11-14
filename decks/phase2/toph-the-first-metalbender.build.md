# Toph, the First Metalbender: final rebuild (Phase 2 step 7.7, 2026-11-08)

**Fix round (2026-11-09), from the independent review `decks/reports/final-review-toph-the-first-metalbender-20261108.md`
(verdict FIX):**
- F3: Stocking the Pantry out, Mishra's Bauble in (owned EN, free).
- F2: Elsewhere Flask out, Brightglass Gearhulk in (owned EN, free).
- F1: Veil of Summer out, Redirect Lightning in (owned EN; Azula holds the other copy). The Veil buy is dropped: the cheapest
  copy read live is 3,040 at Game of Magic, over the 3,000 line.
- F4: Arbaaz Mir pings only on artifacts and legends entering, not on every land entry. The plan file and these notes are
  corrected.
- F5: Aang's Iceberg has flash.
- F6: two timings added to section 5.
- Checklist items 16, 31 and 36: see section 12.

Rechecked after the fixes: bracket PASS, gate PASS with 0 warnings, 100 cards. All-in falls to 1,020 CLP.

Builder: Opus 5.5 high, rebuilt FROM SCRATCH under `docs/proposals/final-rebuild-brief-20261108.md` (corrected budget), the
skill `.claude/skills/commander-deckbuilding/` with its Champion standard, `champion-addendum-20261108.md`, the Toph study
and primers, the play review of 2026-10-26, the owner lessons, the gate review and `real-power-iterations-20261108.md`.
Language: bilingual (English copy when owned in both). Pool: `data/model/phase2/pool-toph-the-first-metalbender.json`.

Checks (2026-11-09 01:40 UTC):
- `python scripts/check_phase2_bracket.py decks/phase2/toph-the-first-metalbender.txt`: **PASS** (floor 3, 2 Game Changers:
  Crop Rotation and Drannith Magistrate, no extra turns, no mass land denial, no reversible card). Review items: Bumi + Ashaya
  (two-card infinite combats, flagged late: 10 mana over two 5-drops) and the Toph + Hardheaded Teacher + Gruul Turf loop
  (four or more cards with the commander; not a two-card line).
- `python scripts/plan_density.py`: **PASS, 0 failures, 0 warnings** for Toph.
- 100 cards (61 nonland, 38 lands, the commander), counted by script.

## 1. Profile

**Commander reading.** {1}{R}{G}{W} 3/3. "Nontoken artifacts you control are lands in addition to their other types (they
don't gain the ability to tap for mana). At the beginning of your end step, earthbend 2."
- Rewards land entries. Every nontoken artifact cast is a land entering (landfall), and an earthbent land that dies or is
  exiled returns tapped (landfall again).
- Fuel: land entries per turn. Toph adds about one a turn: the artifacts, and the end-step earthbend that a sacrifice outlet
  turns into a re-entry.
- She wins nothing alone. Class **enabler** (owner lesson L4): land ramp, fetches and payoffs work without her. Protection
  3 to 4. At 4 MV she can be recast twice.

Rules points:

| # | Point | Status | What falls if wrong |
|---|---|---|---|
| R1 | A nontoken artifact entering under Toph triggers "whenever a land you control enters". | Confirmed by analogy (Ashaya ruling "enter the battlefield as lands"; Toph ruling "only affects permanents on the battlefield"; CR 603.6 not re-read). | Only Toph's artifact bonus; land_entries counts 21 pieces without it. |
| R2 | An earthbent land that dies (sacrifice included) returns tapped, and the return is a landfall. | Confirmed (earthbend rulings 2025-10-02). | The re-entry engines (Zuran Orb, Bombardment, Harrow-type sacrifices, loop B). |
| R3 | Lantern-type grants (Wrenn and Realmbreaker, Great Divide Guide) make every artifact-land tap for any color. | A granted ability, consistent with the reminder text; no specific ruling read. | Some mana; not counted in ramp. |
| R4 | Loop A: Springheart Nantuko bestowed on a land creature copies only the printed land (earthbend's changes are not copiable). The copy is a plain untapped Forest that taps for the next {1}{G} together with Cobra's mana or a Provisioner Treasure. | Spellbook 3470-5702-6871 and 3875-5702-6871; copiable values confirmed by the round-3 review. | Loop A only. |
| R5 | Loop B: Toph + Hardheaded Teacher + Gruul Turf + Zuran Orb. Sacrifice the earthbent Turf to the Orb. It returns and bounces the Orb (a land under Toph). Recast the Orb for 0; the cast trigger earthbends the Turf again. Everflowing Chalice cast for 0 can replace the recast Orb, and Goblin Bombardment can replace the Orb as the outlet. | Spellbook 573-1315-6871-7115--44 and 573-5147-6871-7115--44, read from the project cache. The bracket script lists the template as "review, unresolved". | Loop B only. |
| R6 | Planar Outburst spares lands, earthbent lands and Toph's artifact creatures. It kills Toph and every nonartifact creature unless Ashaya is out. | Follows from the type change; no ruling read. | The Ashaya case only. |
| R7 | Annie Joins Up doubles the triggers of legendary creatures: Toph's end step, Tannuk, Arbaaz, The Earth King, Bumi, Hardheaded Teacher. | Annie rulings. | Some damage and draw. |

**Plan (one sentence).** Put two to four lands onto the battlefield every turn from turn 3 (cheap land ramp, fetches, extra
drops, and with Toph every cheap artifact), and turn each LAND entry into 1 damage to EACH opponent (Sabotender, Tannuk, Valakut
Exploration) and each artifact or legend entering into 1 more (Arbaaz Mir). Ragost, Goblin Bombardment and Legion Guildmage burst the last points. An infinite-landfall loop
ends the game at once when it assembles.

**Backup.** The same entries build a land army that survives a creature wipe (earthbent lands return):
- The Earth King fetches basics on every power-4+ attack.
- Earthbender Ascension and Bumi give trample.
- Seismic Tutelage grows an unblockable earthbent Secret Tunnel.
- Bumi untaps every land for a second combat.

**Speed (goldfish, section 5).**
- Toph on turn 3 or 4.
- From turn 4 or 5: a pinger or burst piece plus two or more entries a turn.
- First lethal threat to the table: turn 7 to 9.
- The pieces of a loop are together by turn 7 in about 1 game in 8 (upper bound: tutors counted as free, mana ignored).

**Win routes.** Every route hits all three opponents. No failure point is shared by all of them (R28).

| Route | Closers | Kill shape | Survives |
|---|---|---|---|
| 1. Landfall burn (noncombat) | Sabotender, Tannuk, Arbaaz Mir, Valakut Exploration | 1 to each opponent per land entry per pinger; Arbaaz 1 per artifact or legend entering; Valakut at end step | Toph dead (land ramp keeps feeding it); a creature wipe (Valakut is an enchantment; earthbent lands return) |
| 2. Artifact burst (noncombat) | Ragost, Goblin Bombardment, Legion Guildmage | 3 to each opponent per Ragost shot (untaps after lifegain); 3 to each per Guildmage activation; Bombardment finishes | Graveyard hate; counters (permanents already down) |
| 3. Infinite landfall | Nantuko + Cobra or Provisioner (A); Hardheaded + Gruul Turf + Zuran Orb (B); Ashaya + Bandit + Orb or Bombardment (C) | Infinite entries; any pinger, Valakut (the whole library) or Bombardment kills the table | Each loop has different pieces; A needs no Toph (any earthbent Forest) |
| 4. Land army (combat) | The Earth King, Seismic Tutelage, Bumi, Toph the Blind Bandit | Power-4+ attacks, trample, an extra combat; Tutelage kills one player at a time | Artifact and enchantment hate; earthbent attackers return |

Single failure points:
- Route 1 dies to repeated creature wipes plus enchantment removal.
- Route 2 dies to artifact wipes.
- Route 3 dies to a counter on the key spell (Redirect Lightning can move the counter) or removal in response (shields, section 4).
- Route 4 dies to fogs and a big board.

No single answer stops all four routes.

**How it beats three opponents.** Damage and drain hit everyone each time, so the deck never needs to choose a target.
Defense comes from earthbent land creatures: they block and come back as landfall. Threats are spread across creatures,
enchantments (Valakut, Bombardment, Terrasymbiosis, Ascension) and lands, so no single wipe resets it.

**What it fears:**
- Fast spell combo that wins before turn 6. There are no counterspells in Naya, so the answers are instant removal and
  Drannith.
- Artifact plus creature wipes in the same turn.
- Library-search hate (Stranglehold, Aven Mindcensor).
- Graveyard-free stax on lands: Blood Moon is survivable (basics), Armageddon is not.

## 2. The puzzle: roles, synergies, how to use each card

Commander: **Toph, the First Metalbender**.
- Cast her on turn 3 (turn 2 with Sol Ring).
- Each end step, earthbend in this order of priority:
  1. a basic Forest when Springheart Nantuko is in hand (loop A);
  2. Gruul Turf when Hardheaded Teacher and Zuran Orb are out (loop B);
  3. Secret Tunnel, the unblockable attacker and Seismic Tutelage host;
  4. an uncracked fetch land or a land you will sacrifice (re-entry).
- With her out, play cheap artifacts AFTER the pingers.

Ramp and land entries (21):
- **Sol Ring.** Turn 1; with Toph also an entry. Never bad.
- **Arcane Signet, Talisman of Impulse.** Turn-2 rocks for a turn-3 Toph. Never bad.
- **Wayfarer's Bauble.** Turn 1; crack it at an opponent's end step. With Toph it is two entries. Never bad.
- **Everflowing Chalice.**
  - Cast for 0 any time Toph is out: a free landfall (a ping from each pinger, a Cobra mana, a Provisioner Treasure, an
    Arbaaz ping).
  - Cast for 2 on turn 2 without her: a rock.
  - It is the second "0-cost artifact" of loop B and a home for Hardlight Containment.
  - Never bad.
- **Rampant Growth, Shared Roots.** Turn 2, fetch the missing color. Shared Roots is a Lesson: Hardheaded Teacher puts one
  more counter. Never bad.
- **Sakura-Tribe Elder.** Turn 2. Chump-block, then sacrifice for a basic. Never bad.
- **Lotus Cobra.** Turn 2. Each entry is a mana: chain fetches into Harrow. Loop A piece. Never bad.
- **Great Divide Guide.** Turn 2 fixer. With Toph every artifact and land taps for any color, so the Orb, Haystack, the Mite
  and the Gearhulk become rocks. Never bad.
- **Explore.** Turn 2 or 3 with a land in hand: an extra entry and a card. Never bad.
- **Druid Class.**
  - Turn 2: 1 life per entry, which untaps Ragost.
  - Level 2 on turn 3 or 4: an extra land every turn.
  - Level 3 late: a sink.
  - Never bad.
- **Crop Rotation (Game Changer).**
  - Instant, 1 mana. Sacrifice an earthbent land (it returns) for an untapped Gruul Turf (loop B), Ba Sing Se or Secret
    Tunnel.
  - It also saves a land from removal.
  - Never bad.
- **Harrow, Cycle of Renewal, Roiling Regrowth.**
  - Instants. Sacrifice an earthbent land: it returns, plus two basics, so three entries.
  - Cast them at an opponent's end step or with Cobra out.
  - Cycle is a Lesson.
  - Never bad.
- **Heaped Harvest.** Turn 3. A basic on entry and another on sacrifice (Ragost or Zuran Orb). With Toph it is three entries.
  Never bad.
- **Wood Elves (buy).** Turn 3. An untapped Forest, a Chord or convoke body, and a land under Ashaya. Never bad.
- **Tireless Provisioner.** Turn 3. A Treasure per entry: mana on opponents' turns, and Ragost ammunition. Loop A piece.
  Never bad.
- **Earthbender Ascension.** Turn 3. A basic plus a 2/2 land creature. After four entries, each entry gives +1 counter and
  trample (Terrasymbiosis draws). Never bad.
- **Wrenn and Realmbreaker.**
  - Turn 3. All lands tap for any color, so every artifact-land becomes a rock.
  - +1: a 3/3 hexproof vigilance land that blocks.
  - −2: mill 3, take a permanent.
  - Never bad.

Landfall and entry payoffs (10):
- **Sabotender.** Turn 2. 1 damage to each opponent per entry; a reach blocker. Never bad.
- **Arbaaz Mir.** Turn 2. Each nontoken artifact or legend that enters is 1 damage to each opponent and 1 life (Ragost
  untaps). With Toph a cheap artifact triggers both Arbaaz and the landfall pingers. Loop B kills alone with Arbaaz out (the
  Orb re-enters every loop). Never bad.
- **Tannuk.** Turn 3. 1 damage to each opponent per entry and a card on the second entry each turn. Never bad.
- **Valakut Exploration.** Turn 3. Each entry exiles a card you may play; at your end step the unplayed ones deal damage to
  each opponent. With an infinite loop it exiles the library: lethal. Never bad.
- **Tireless Tracker.** Turn 3. A Clue per entry; crack Clues on opponents' turns. Never bad.
- **Springheart Nantuko.**
  - Loop A key. It must be CAST for bestow: Chord puts it onto the battlefield unattached, so Chord never fetches it.
  - Aim Toph's end-step earthbend at a basic Forest while it is in hand. Next turn, with Cobra or Provisioner and a pinger
    out, bestow it on that Forest: infinite entries.
  - Without the second piece it still makes a land copy per {1}{G}, or a 1/1 per entry (Bombardment fodder).
  - Never bestow it on a legend.
  - Never bad.
- **Ragost, Deft Gastronaut.**
  - Every artifact is a Food: {1}, tap, sacrifice for 3 to each opponent.
  - It untaps at EACH end step after any lifegain (Arbaaz, Druid Class, Zuran Orb), so it fires every turn around the table.
  - Sacrifice tokens first, then earthbent artifacts (they return).
  - Never bad.
- **Goblin Bombardment.**
  - Sacrifice earthbent land creatures after Toph's end step (they return: one more entry).
  - Sacrifice anything in response to a wipe.
  - Loop C outlet; loop B outlet in place of the Orb.
  - Never bad.
- **Legion Guildmage.**
  - A 2-drop blocker early.
  - Late, the mana sink of a deck that floods: {5}{R}, tap: 3 to each opponent; {2}{W}, tap: tap an attacker or a blocker.
  - Never bad.
- **Zuran Orb.**
  - Sacrifice earthbent lands, cracked fetches or the Harvest for re-entries and life (Ragost untaps); instant-speed
    insurance against land removal.
  - Loop B and C piece.
  - Never bad with Toph out.

Draw and engines (8):
- **Terrasymbiosis.** Toph's end-step earthbend draws 2 every turn. Seismic Tutelage doubling draws that many. Never bad.
- **Mishra's Bauble (fix F3).**
  - 0 mana. With Toph out it is a free land entry (a ping from each pinger) and an Arbaaz ping.
  - Crack it at any time for a card next upkeep.
  - It is the 0-cost artifact that survives in the Bombardment version of loop B, and a Gearhulk target.
  - Never bad.
- **Ichor Wellspring.** A 2-mana artifact that draws on entry and again when it goes to the graveyard (sacrifice it to Ragost
  or Zuran Orb). With Toph it is an entry and an Arbaaz ping. Never bad.
- **Brightglass Gearhulk (fix F2).**
  - {G}{G}{W}{W}, castable on turn 4 or 5 (W 18 and G 22 sources).
  - On entry it tutors two cards of MV 1 or less: Zuran Orb (loop B) plus Mishra's or Wayfarer's Bauble, Sol Ring, Chalice,
    Haywire Mite or Hardlight Containment.
  - A 4/4 first-strike trampler: a power-4 attacker for The Earth King and a safe Seismic Tutelage host.
  - With Toph it is an artifact-land: an entry and an Arbaaz ping, a Ragost Food, and it survives Planar Outburst.
  - Bad early.
- **Water Tribe Rallier.** Turn 2. From turn 5, waterbend {5} (tap artifacts and creatures to help): look at 4 cards, take a
  creature of power 3 or less (Nantuko, Cobra, Provisioner, every pinger, Hardheaded Teacher, The Earth King). A repeatable
  tutor and sink. Never bad.
- **Seismic Sense.** 1 mana, Lesson. With 6+ lands it finds Nantuko or a pinger, or Gruul Turf for loop B. Never bad.
- **Chord of Calling.** Instant, convoke with land creatures. Targets:
  - Cobra (X=2) or Provisioner (X=3) for loop A;
  - a pinger: Sabotender or Arbaaz (X=2), Tannuk (X=3);
  - Hardheaded Teacher or The Earth King (X=4), Ashaya (X=5).
  - Cast it at an opponent's end step. Bad early.
- **Toph, Hardheaded Teacher.**
  - Each spell earthbends 1: with Zuran Orb or Bombardment that is one re-entry per spell, and counters for Terrasymbiosis.
  - Her entry can regrow Harrow or a removal spell.
  - Loop B hub.
  - Never bad.

Land army (6):
- **The Earth King** (proven role-player). Turn 4. The 4/4 bear plus any power-4+ land creature attack: fetch that many
  basics every combat. Never bad.
- **Toph, the Blind Bandit.** Earthbend 2 on entry; her power is every counter on your lands, so she is the power-4+ attacker
  for The Earth King. Loop C piece with Ashaya. Never bad.
- **Seismic Tutelage** (proven role-player).
  - Put it on a creature that attacks and is NOT a returning land creature, or accept that the Aura falls off when the land
    dies. Default host: an earthbent Secret Tunnel (unblockable) or the bear.
  - Counters double each attack and Terrasymbiosis draws that many.
  - It kills one player per few attacks.
  - Bad early.
- **Bumi, Unleashed.** Earthbend 4 makes a 4/4 haste land that triggers The Earth King the same turn. 5/4 trample. When he
  connects, every land untaps and the land creatures attack again. Bad early.
- **Ashaya, Soul of the Wild.**
  - Every nontoken creature you cast is a land entry and taps for G.
  - Planar Outburst spares your whole team while she is out.
  - Loops: with Bumi (infinite combats) and with the Bandit (loop C). Cast her before them.
  - Bad early.
- **Annie Joins Up.** 5 damage to the biggest creature, then the legendary triggers fire twice (Toph's end step, Tannuk,
  Arbaaz, Earth King, Bumi). Bad early.

Interaction (13):
- **Swords to Plowshares, Path to Exile.** 1-mana instants for the must-answer creature or commander. Never bad.
- **Fateful Absence.** A 2-mana instant for a creature or planeswalker. Never bad.
- **Hardlight Containment.** 1-mana exile.
  - Enchant a rock nobody targets: Sol Ring, Signet or Talisman.
  - Never enchant an artifact you will earthbend or sacrifice.
  - Never bad.
- **Haywire Mite.** 1 mana; with Toph an entry. Sacrifice it at instant speed to exile a stax artifact or enchantment. Never
  bad.
- **Collective Resistance, Origin of Metalbending.** 2-mana instants. Destroy an artifact or enchantment, or protect Toph or
  the combo piece (hexproof plus indestructible, or indestructible plus a counter). Never bad.
- **Return to Nature (buy).**
  - A 2-mana instant: artifact, enchantment, or exile a card from a graveyard.
  - It is the only graveyard hate: exile the reanimation target in response.
  - Never bad.
- **Beast Within, Chaos Warp.** 3-mana instants for any permanent; Chaos Warp has no token. Never bad.
- **Stroke of Midnight.** A 3-mana instant for any nonland permanent. Never bad.
- **Drannith Magistrate (Game Changer).** Turn 2. Opponents cannot cast from outside the hand: a removed commander stays
  gone; flashback and cascade stop. It never touches your own Toph. Never bad.
- **Planar Outburst.**
  - A reset when behind on board: their creatures and tokens die; your lands, earthbent lands and artifact creatures stay.
  - Best with Ashaya out, or with Make a Stand. Awaken at 8 mana.
  - Bad early.

Protection (3, plus Collective Resistance and Origin above):
- **Redirect Lightning (fix F1).**
  - {R} plus {2} or 5 life, instant, Lesson.
  - It changes the target of any single-target spell or ability: removal of any color moves to an opponent's creature, and a
    counterspell aimed at your loop piece moves onto the Redirect itself.
  - It is the deck's only stack tool.
  - Never bad.
- **Make a Stand (buy).** A 3-mana instant: your creatures gain indestructible in response to a destroy or damage wipe (the
  job Hakoda did before Ezio took it). Never bad.
- **Haystack.** {2}: phase out Toph or the key pinger in response to removal or an exile wipe. With Toph it is an entry.
  Never bad.

Lands (38):
- **Command Tower, Exotic Orchard.** Untapped fixing.
- **Ba Sing Se.** Untapped with a basic; {2}{G} earthbend 2 as a sink and rebuild.
- **Untapped duals.** Rootbound Crag, Sunpetal Grove and Clifftop Retreat (check lands); Game Trail, Fortified Village and
  Furycalm Snarl (reveal lands); Rugged Prairie (filter); Battlefield Forge (pain).
- **Secret Tunnel.** An unblockable earthbend target.
- **Gruul Turf.** Loop B. It also bounces an artifact to reuse its entry trigger (Ichor, Mite, both Baubles).
- **Four fetch lands** (Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape, Cabaretti Courtyard). Two entries each, three
  when Toph earthbends an uncracked one first.
- **Basics.** 10 Forest, 5 Mountain, 6 Plains.

Multi-role count (R4): 49 of 61 nonland cards count in two or more counted jobs (land ramp counts as both ramp and a land
entry). About a dozen are single-role: the rocks, Ichor Wellspring, Mishra's Bauble, Terrasymbiosis,
Haywire Mite, Return to Nature, Redirect Lightning and Drannith. Commander-centric count (R5): 3 cards are
near-blank without Toph (Everflowing Chalice is still a rock, Mishra's Bauble still a cantrip, Gruul Turf still a land), well
under 12.

## 3. Curve and ratios

| MV | 0 | 1 | 2 | 3 | 4 | 5 | 6+ |
|---|---|---|---|---|---|---|---|
| Cards (61 nonland) | 3 | 9 | 23 | 18 | 5 | 3 | 0 |

Average MV 2.36. The current list was 2.61; the Bracket 3 median is 3.11. 35 cards cost 2 or less (current list: 30).
Creatures: 21. Nontoken artifacts: 12.

| Ratio | Count | Min / target | Reason |
|---|---|---|---|
| Lands | 38 | band 38-40 | Landfall wants lands in hand for Explore, Druid Class and The Earth King. Low curve, so the bottom of the band. Lands plus lasting ramp = 38 + 9 rocks or dorks + 12 land-ramp spells (R8). |
| Ramp | 21 (19 primary) | 20 / 22 | Landfall floor 18 + 2 for a 4-MV commander. 12 of them put lands onto the battlefield, so they are fuel too. |
| Land entries | 21 + Toph | 12 / 16 | The fuel: 97 % to see one in 12 cards. |
| Landfall payoffs | 9 + 3 tutors | 10 / 12 | 81 % by turn 5. |
| Access to the drain route (R18) | 10 (4 pingers, Ragost, Bombardment, Guildmage, Chord, Rallier, Seismic Sense) | 10 | 73 % by turn 5 and 79 % by turn 7 (Monte Carlo, no extra draw counted). Terrasymbiosis, Tracker and Tannuk push it higher in play. |
| Draw | 10 counted (7 primary) | 10 / 12 | Terrasymbiosis (2 a turn) is the engine. Peak turns spend about 2 cards and gain 1 + 2 + Tannuk + Clues, so the hand stays level. |
| Spot answers | 11 + Annie | 6 / 8 | R19: 8 cost 2 or less, 9 at instant speed (Haywire Mite's sacrifice included), 7 hit artifacts and 7 hit enchantments, 1 hits graveyards. |
| Wipes | 1 | 1 / 2 | A board of lands survives creature wipes; one reset for go-wide and big boards. |
| Protection (commander) | 5 | 3 / 4 | Enabler class: Redirect Lightning, Collective Resistance, Origin of Metalbending, Haystack, Make a Stand. |
| Win-turn shield (R24) | 4 at 1-2 MV (Redirect, Collective, Origin, Haystack) + Make a Stand | 3 | Keep R plus 2 open for Redirect on the loop turn; hold Collective or Origin for the key creature. |
| Tutors | Chord, Seismic Sense, Water Tribe Rallier, Crop Rotation | B3 median 4 | They find pingers and loop A pieces (Seismic and Rallier find Nantuko) and Gruul Turf. |
| Game Changers | 2 of 3 | 3 | Crop Rotation and Drannith Magistrate (owned). Third slot empty: every RGW Game Changer costs over 3,000 (live Scryfall `is:gamechanger`, 30 legal in RGW; the cheapest are Farewell about USD 5 and Underworld Breach about USD 10). |
| Tapped lands | 1 always (Gruul Turf) + 4 fetches to tapped basics | R10: 3 | Each fetch pays back with 2 to 3 entries, and Gruul Turf with loop B and artifact reuse. Written exception. |

## 4. Interaction plan and protection plan

**Interaction:**
- Spend the 1-mana answers (Swords, Path, Hardlight) on commanders and engines.
- Keep one instant (Fateful Absence, Beast Within, Chaos Warp or Stroke) up on opponents' turns from turn 5, for a combo
  piece or a lethal attacker.
- Use the Mite, Return to Nature, Collective Resistance or Origin on stax artifacts and enchantments first.
- Drannith early against commander-centric decks.
- Planar Outburst only when behind on board, ideally with Ashaya out or Make a Stand in hand.

**Protection:**
- Toph is an enabler. Protect her only when her end step matters (a loop turn, Terrasymbiosis out).
- Protect the pingers and loop pieces first: Collective Resistance or Origin against destroy and damage, Haystack against
  exile, Redirect Lightning against any single-target spell (counterspells included), Make a Stand against wipes.
- **Win turn:**
  1. Keep {R} plus {2} (or 5 life) open for Redirect Lightning.
  2. Then the loop piece.
  3. Hold Collective or Origin for the response.
- Never present a lethal threat one turn before you can protect it (R30).
- Defense comes from earthbent land creatures: they block big attackers and return as landfall. Legion Guildmage taps an
  attacker.

## 5. Mulligan and play pattern

**Keep:** 2 to 4 lands (2 only with a 1- or 2-mana ramp piece), a play by turn 2 or 3, and a plan piece (pinger, ramp
engine, tutor) or a way to find one. Keep almost any land-good hand that holds Sol Ring, Lotus Cobra, Druid Class,
Terrasymbiosis or a pinger.

**Ship:** 0 to 1 landers, 6+ landers, hands with no play before turn 4, and interaction-only hands.

20 seeded hands (Monte Carlo script, seed 2026): 17 keep, 3 ship (all three are one-landers). Over 20,000 runs: 78.7 % keep
the first seven, 95.6 % with the free mulligan (target 85 %).

**Play pattern:**
- **Turns 1-5.**
  - Turns 1-2: rock or land ramp, a 2-drop pinger or Cobra.
  - Turn 3: Toph, or Toph plus a 1-drop.
  - Turn 4: a pinger plus land ramp, then cheap artifacts after the pinger.
  - Turn 5: Terrasymbiosis or Tannuk, and Chord for the missing piece.
- **Turns 6-9.** Three to four entries a turn: every turn is 3 to 8 damage to each opponent. Fire Ragost at every end step.
  Assemble a loop with Redirect or Collective Resistance up.
- **Timing (review F6).**
  - Loop B is main-phase only: the Zuran Orb recast is an artifact spell at sorcery speed.
  - Valakut's infinite kill lands at YOUR end step, so the opponents get a window until then. Keep Haystack or Collective
    Resistance up for Valakut, or win at once with a pinger or Arbaaz.
- **Late.** Legion Guildmage, Ba Sing Se and Druid Class level 3 sink the flood. Attack with the army (Earth King triggers)
  only when the crack-back is safe. After a wipe, rebuild:
  - lands return;
  - Chord, Rallier or Seismic Sense find a pinger;
  - Wrenn's −2 or −7.

**Goldfish (5 games to turn 8, seeded draws):**

Played by hand from the seeded hands 1, 3, 4, 7 and 10 and their next eight draws.

| Game | Toph cast | Plan online (pinger or burst + 2 entries) | First lethal threat | Note |
|---|---|---|---|---|
| 1 | T4 | T5 | T8 | Fortified Village tapped on turn 3; Sabotender, Cobra and Druid Class drawn by turn 4 |
| 3 | T3 | T5 | T9 | Signet and Secret Tunnel give Toph on turn 3; Ragost with artifact fodder is the only drain piece |
| 4 | T3 | T6 | T9 | Chalice for 2 and Ba Sing Se give Toph on turn 3; Tracker gives card flow, but no pinger until Guildmage |
| 7 | T4 | T5 | T8 | Two conditional lands enter tapped; Bandit and Ragost, Chord fetches a pinger |
| 10 | T4 | T3 | T7 | Sabotender on turn 2, Ascension on turn 3; Nantuko waits for Cobra or Provisioner (not drawn) |

**Disrupted goldfish:**
- **(a) Toph removed the first time she acts.** Land ramp and pingers keep the drain running. Recast on turn 6. About one
  turn lost.
- **(b) Wipe on turn 6.** Make a Stand or Bombardment in response. Otherwise the lands and earthbent lands stay and Valakut
  stays. Rebuild with Chord or Rallier: threatening again on turn 8.
- **(c) First loop attempt countered.** Without Redirect the piece is lost. With Redirect the counter targets itself and
  the piece resolves. The drain continues in either
  case; one or two turns lost.

## 6. BUY

All lines are inside Toph's 8,000 all-in envelope, each card is under 3,000, and all three stores are already in the order (no
new shipping).

| Card | Store | Price hint (CLP) | Language | Gain | Plays until it arrives |
|---|---|---|---|---|---|
| Wood Elves | Game of Magic Singles (`wood-elves-the-hobbit`) | 570 (NM, read 2026-11-08 18:27 UTC) | EN | 3-MV ramp that is an untapped land entry, a creature for Chord, convoke and Ashaya | Burnished Hart (owned) |
| Make a Stand | Rivendel El Concilio | 300 (stock 2, read 2026-11-09 01:30 UTC) | ES | Team indestructible at instant speed: wipe insurance and win-turn shield, the job Hakoda did | Horrid Vigor (owned) |
| Return to Nature | Rivendel El Concilio | 150 (stock 7, same read) | ES (EN 300) | The only graveyard hate, plus an instant artifact or enchantment answer | Insidious Fungus (owned) |
| **Total** | | **1,020** | | | |

Ranked by gain per CLP: Return to Nature, Make a Stand, Wood Elves. Prices re-read live by the reviewer on 2026-11-09 at
01:50 UTC: Rivendel Make a Stand ES 300 (stock 2), Return to Nature ES 150 (stock 7); Game of Magic Wood Elves NM 570.

**Veil of Summer dropped (fix F1).** The cheapest live copy is 3,040 at Game of Magic, over the 3,000 line; Rivendel has none,
and PayToWin was not readable (HTTP 429). Autumn's Veil is out of stock at Game of Magic and absent at Rivendel. Redirect
Lightning (owned) plays instead. Only if the lead's live read shows a better-than-Damaged Veil at PayToWin for 2,999 or less
may the owner swap it back for Redirect.

Considered and not bought:
- Heroic Intervention (9,600+).
- Boros Charm (4,100+).
- Recruiter of the Guard (4,400).
- Scute Swarm (4,800).
- Dryad of the Ilysian Grove (6,760).
- Nature's Lore (about 2,100): Rampant Growth and Shared Roots do the job.
- Farseek (about 1,000 to 1,640): no 3-MV slot is worth that much to replace.
- Fabled Passage (about 1,560).
- Blossoming Defense (about 445+): the shields are enough.
- Lightning Helix (Rivendel 800): 8 cheap answers already.
- Skyclave Apparition (549): it needs an Illusion token.
- Tunneling Geopede: no stock in the three stores.

Dropped from the earlier plan: Cultivate 900, Generous Gift 1,440, Myriad Landscape 1,440 and Toph's Elephant token 4,300.
The Elephant line in the PayToWin order falls from 2 to 1 (Kilo's).

**Tokens:**
- No new token to buy.
- The deck makes these, all owned: Bear 4/4 (The Earth King), Beast 3/3 (Beast Within), Human 1/1 (Stroke of Midnight),
  Insect 1/1 and Copy (Nantuko), Clue, Food and Treasure, and Wrenn and Realmbreaker's emblem (TMOM 23, English binder).
- Rampaging Baloths left, so its 4/4 Beast (no stock anywhere) is no longer needed.

## 7. Loans

None. The loan candidates (`decks/phase2/loans.md`) are Assassin, black or blue cards outside this plan. Viewpoint
Synchronization is owned (2 free copies); it was considered and not played (5-MV entries; the deck has 21 cheaper).

## 8. Scarce copies

Read against Ezio's final list and Azula's current list (2026-11-09 01:35 UTC). A dry run of `scripts/assign_copies.py` in the
order Ezio, Azula, Toph, Kilo (nothing written) leaves Toph short only of the four buys and Battlefield Forge, which Ezio
covers with its bought English copy (Ezio build notes, section 8).

| Card | Copies | Holders | Toph's case |
|---|---|---|---|
| Hakoda, Selfless Commander | 1 EN | Ezio (priority 1) | Not claimed. Make a Stand (buy, 300) does the wipe-insurance job. |
| Chaos Warp | 4 (2 EN, 2 ES) | Ezio EN, Azula EN, Kilo ES | Toph takes the second ES copy. All four decks are served, with no spare. |
| Everflowing Chalice | 3 (2 EN, 1 ES) | Azula EN, Kilo ES | Toph takes the other EN copy. No conflict. |
| Sol Ring, Arcane Signet | 4 each | one per deck | No spare. |
| Command Tower | 3 (1 EN, 2 ES) | Azula EN; Ezio's ES goes to Kilo (Ezio buys one) | Toph keeps an ES copy. |
| Haystack | 2 EN | Ezio 1 | Toph 1. |
| Swords to Plowshares | 2 ES | Ezio plays a bought EN copy | Toph 1 ES; the other ES goes to Kilo. |
| Battlefield Forge | 1 ES | Ezio and Kilo buy their own (order) | Toph keeps the owned ES copy. |
| Secret Tunnel, Clifftop Retreat, Rugged Prairie, Exotic Orchard | 3 EN / 3 ES / 2 ES / 5 ES | Ezio, Kilo | Enough copies. |
| Goblin Bombardment | EN + ES | Azula dropped it | Toph takes EN; ES is free. |

Azula (priority 2) shares only Sol Ring, Arcane Signet, Chaos Warp, Command Tower, Everflowing Chalice, Exotic Orchard,
Redirect Lightning (2 EN: Azula 1, Toph 1) and Mountain with this list, and every one has enough copies. Mishra's Bauble is
1 EN copy that no final list plays (Ezio's list does not), so it is free. Chaos Warp plays a Spanish copy: Ezio and Azula hold
the English ones. **No card was replaced for Azula.**

**Kilo check (fix round, against the current `decks/phase2/spanish-deck.txt`).** Kilo shares Sol Ring, Arcane Signet,
Chaos Warp, Clifftop Retreat, Everflowing Chalice, Exotic Orchard, Rugged Prairie and basics with this list, and every one has
enough Spanish copies for Kilo. Kilo is priority 4, so Toph keeps its copies. Elsewhere Flask (1 ES) is now free for Kilo.
Spanish-only copies Toph plays that Kilo could still need (not in Kilo's list today), with Toph's fallback if the lead moves
one:

| Card | Copies | Fallback |
|---|---|---|
| Path to Exile | 1 ES | Justice Strike (owned EN) |
| Arbaaz Mir | 1 ES | Buy an English Arbaaz (price to read) or Fire Nation Archers (owned) |
| Planar Outburst | 1 ES | Hour of Revelation (owned EN) |
| Fateful Absence | 2 ES | One stays free for Kilo |

## 9. Comparison with the current list and the iteration-1 list

**Against the current list after purchases** (`moxfield/toph-the-first-metalbender-after-purchases.txt`, Salt 7.0, real
power 7.0-7.4): 13 out, 13 in.

| Out | Why | In | Why |
|---|---|---|---|
| Hakoda | Ezio took it | Make a Stand (buy) | Team indestructible, 300 |
| Rampaging Baloths | 6 MV; its 4/4 Beast token has no stock anywhere; the loops already have closers | Arbaaz Mir | A 2-mana pinger: with Toph every cheap artifact pings twice |
| Generous Gift | 1,440 + a 4,300 Elephant token | Chaos Warp (owned) | Same job, no token |
| Myriad Landscape | 1,440, slow tapped fetch; 4 owned fetches remain | Plains | Sixth white source for 13 white cards |
| Cultivate | 900, a fourth 3-MV ramp spell | Everflowing Chalice (owned) | A free landfall with Toph; the 0-cost artifact of loop B |
| Burnished Hart | 6 mana for two lands | Wrenn and Realmbreaker (owned) | Every artifact-land becomes a rock; card advantage |
| Solemn Simulacrum | 4 MV | Haywire Mite (owned) | 1-mana artifact answer that is also an entry |
| Stocking the Pantry | Needs counters; overlaps Terrasymbiosis | Mishra's Bauble (owned) | Free entry and card (fix F3) |
| Reckless Handling | Random discard; Orb tutor only | Gruul Turf (owned) | Loop B, artifact reuse |
| The Stasis Coffin | Eats Toph's earthbend every turn (the Forest for Nantuko, the Tunnel) | Legion Guildmage (owned) | A drain sink for the flood, and a tapper |
| Aang's Iceberg | 3 MV flash answer that is undone when the enchantment leaves | Fateful Absence (owned) | 2-mana instant |
| True Ancestry | Slow recursion | Return to Nature (buy) | Graveyard hate, artifact or enchantment answer |
| Rogue's Passage | Colorless 4-mana sink | Redirect Lightning (owned) | Stack tool and win-turn shield |

**Cheap answers came back.** Instants and instant-speed answers at 2 MV or less went from 4 to 7 (Swords, Path, Fateful
Absence, Collective Resistance, Origin of Metalbending, Return to Nature, Haywire Mite), plus Hardlight Containment and three
3-mana instants. Spot answers rose from 9 to 11 (plus Annie in both lists).

**The curve got faster.** Average MV 2.61 → 2.36; 35 cards cost 2 or less (was 30); no 6-drop. Brightglass Gearhulk is kept
from the current list (fix F2), and Elsewhere Flask is not played.

**Against iteration 1** (`round3-step21.txt`, Salt 7.4, real power 6.6-7.1):
- 23 cards differ.
- Kept from iteration 1: the low curve, Arbaaz, Wrenn and the cheap-artifact package.
- Dropped from iteration 1: its weak spots, namely Liquimetal Coating (orphan), Haru, Earth Kingdom General, Boros Locket,
  Selesnya Signet, Bender's Waterskin, Nutrient Block and Hunter's Bow.
- Kept from iteration 2: real land entries that work without Toph (four fetches, Roiling Regrowth, Druid Class, Explore, Wood
  Elves) and the owner's proven The Earth King and Seismic Tutelage.
- Iteration 1 had 7 cheap answers; this list has 7 at 2 MV or less plus 4 more.
- Proven role-players are all IN (The Earth King, Seismic Tutelage).

**Cut log (other cards considered):**
- Elsewhere Flask: the weakest artifact slot; Brightglass Gearhulk replaced it (fix F2). Its only copy (Spanish) is now free
  for Kilo.
- Veil of Summer: no copy under 3,000 (fix F1).
- Stocking the Pantry: replaced by Mishra's Bauble (fix F3).
- Justice Strike: 7 spot creature answers plus Annie already; it is the Path fallback.
- Chromatic Lantern: Wrenn and the Guide do its job.
- Omnath and Titania: 6 to 7 MV.
- Hour of Revelation: kills the enchantment engines.
- Mindslaver: no plan role.
- Hardened Scales: no counter plan beyond Tutelage.
- Inspiring Overseer: a 3-MV cantrip; Mishra's Bauble and Ichor are cheaper.
- Bonecrusher Giant (buy, about 549): 8 cheap answers already.

**Final cut pass (10 weakest, redone with the review).** Elsewhere Flask and Stocking the Pantry lost to Gearhulk and
Mishra's Bauble (fixes F2 and F3). Still in: Shared Roots, Explore, Haywire Mite, Legion Guildmage, Drannith Magistrate,
Return to Nature, Planar Outburst, Annie Joins Up. Each was checked against the best unplayed
candidate:
- Shared Roots vs Nature's Lore (about 2,100): an untapped Forest is not worth 2,100.
- Drannith vs Soul-Guide Lantern: Drannith is a free Game Changer slot and strong against commander decks.
- Annie vs Aang's Iceberg: Annie's doubling of Tannuk, Arbaaz and Toph is an engine.

No swap won.

## 10. Real-power estimate (1-10)

| List | Estimate | Note |
|---|---|---|
| Iteration 1 | 6.6-7.1 | real-power review |
| Current (after purchases) | 7.0-7.4 | real-power review |
| **This list, after the fix round** | **7.3-7.7**, central 7.5 | Confidence medium-low (no games played). The reviewer put the pre-fix list at 7.2-7.6 and the fixed list at 7.3-7.7. |

Why higher:
- A lower curve: Toph on turn 3 or 4 and the drain online on turn 4 or 5.
- Interaction restored, from 4 to 7 cheap answers plus 5 more.
- 7 drain closers, up from 5 (Arbaaz and Guildmage).
- A second infinite loop, B (different pieces from A); Brightglass Gearhulk tutors its Zuran Orb.
- Redirect Lightning moves a counter or removal of any color.
- Wipe insurance back, which Hakoda had done.

Why not higher:
- Naya still has no counters against a fast spell combo.
- The third Game Changer slot is empty.
- No table-scaling draw: R16 cards such as Esper Sentinel cost far over 3,000.

Commander Salt guess, not measured: 7.0 to 7.4. Its "combos with no tutors" penalty may stay (Nantuko has two tutors, Gruul
Turf has two). The lead measures it.

## 11. Total spend (Toph, all-in)

| Item | CLP |
|---|---|
| Wood Elves | 570 |
| Make a Stand | 300 |
| Return to Nature | 150 |
| Loans and replacements | 0 |
| Tokens | 0 |
| **All-in** | **1,020** |

Against the **8,000 envelope**: 6,980 under. Against the 8,650 of the earlier plan: 7,630 saved. The spare envelope is not
spent: no readable card under 3,000 beats the owned swaps (Fellwar Stone 1,560, Farseek 1,640, Nature's Lore about 2,100,
Lightning Helix 800, all marginal here).

## 12. Champion checklist items left open by the review

- **36, high-power non-GC cards: FIXED.** Mishra's Bauble (owned) is in (F3) and Brightglass Gearhulk is back (F2). Every
  other R36 card in RGW is unowned and over 3,000 in the three stores (Lotus Petal 21,000+, Dryad 6,760, Urza's Saga, Walking
  Ballista, Deflecting Swat), or it is already in (Swords, Path, Lotus Cobra).
- **16, card advantage that scales with three opponents: not fixable.** No such card is owned in Naya. The candidates (Esper
  Sentinel about USD 53, Smothering Tithe and The One Ring as Game Changers, Sylvan Library about USD 27) are all over 3,000.
  The drain already scales: each entry hits all three opponents.
- **31, politics: fixed at no cost (written here).**
  - The drain is symmetric and visible, so do not show a turn of 3+ damage to everyone before the deck can kill in about two
    turns. Until then, ping with one pinger and let the most threatening opponent draw the table's removal.
  - Offer removal on the table leader: Swords, Path or Chaos Warp on another player's threat buys a turn of peace.
  - Earthbent land creatures are the deterrent. A blocker that returns as landfall makes attacking Toph a bad deal; say so
    when an opponent picks a target.
  - Use Legion Guildmage's tap ability on the attacker heading at someone else only when it buys a deal; otherwise keep it for
    defense.
  - Never make deals that delay the win turn once a loop is assembled.

## Gauntlet (R39) and reference boards

- **(1) Fast combo, turns 5 to 7.**
  - Instant answers on their turn: Swords, Path, Fateful Absence, Beast Within, Chaos Warp, Stroke.
  - Haywire Mite, Collective Resistance, Origin and Return to Nature for artifact or enchantment combos.
  - Drannith stops command-zone and graveyard casts.
  - Weak against pure spell combo: no counters. Pressure with the drain from turn 4.
- **(2) Stax and taxes.**
  - Cheap threats (Chalice and Orb cost 0).
  - 7 artifact and 7 enchantment answers.
  - Basics against Blood Moon.
  - Land ramp ignores spell taxes on their turn (instants).
- **(3) Go-wide tokens (Board 1, eight 1/1 chump blockers).**
  - The pingers, Valakut, Ragost, Guildmage and Bombardment ignore blockers.
  - Planar Outburst clears them and keeps the lands.
  - The army has trample (Ascension, Bumi) and the unblockable Secret Tunnel.
  - Their sacrifice pings kill toughness-1 pingers: hold Make a Stand.
- **(4) Big creatures (Board 2, two creatures bigger than ours).**
  - 7 spot creature answers plus Annie's 5 damage and Planar Outburst.
  - Drannith keeps a removed commander out.
  - Earthbent land creatures chump and return as landfall.
  - Legion Guildmage taps the biggest attacker.
  - The drain and loops ignore the board.
- **(5) Control with counters and wipes.**
  - Redirect Lightning moves a counter onto itself on the key turn.
  - Threats spread across creatures, enchantments and lands.
  - Instant-speed ramp (Harrow, Cycle, Roiling, Crop Rotation, Chord) at their end step.
  - Make a Stand and Bombardment against the wipe.
  - Never commit more than what wins in two turns when two opponents can wipe (R32).
