# Adversarial review: toph-the-first-metalbender (2026-11-02)

Reviewer: Opus 5.5 high, Phase 2 adversarial reviewer. Inputs: `decks/phase2/toph-the-first-metalbender.txt` (100 cards,
recounted), Oracle text from `data/model/phase2/pool-toph-the-first-metalbender.json` and the Scryfall bulk
`oracle-cards-20261011210156`, the commander's live Scryfall Oracle text and rulings (read 2026-11-02), Spellbook bulk
`spellbook_variants_slim.jsonl.gz`, then the plan file, build notes, consistency and bracket reports, owner decisions and
lessons. Owner decisions honoured as given: Bumi + Ashaya accepted, Hardened Scales out, the Seismic Tutelage target rule,
38 lands, no Omnath or Titania, Nature's Force at the top, Earth Kingdom General out for Sandbenders' Storm. The copy
assignment is treated as final.

## 1. Independent reading (written before opening the plan file and notes)

**Commander.** {1}{R}{G}{W} 3/3. "Nontoken artifacts you control are lands in addition to their other types. (They don't
gain the ability to {T} for mana.) At the beginning of your end step, earthbend 2." Rulings (2025-10-02): earthbend makes a
0/0 land creature with haste, puts the counters, and returns the land tapped "when it dies or is exiled"; it may target a
land that is already a creature; the artifact clause works only on the battlefield (no playing artifacts as lands).
- Rewards: land entries (each nontoken artifact that enters under her is a land entering), land creatures, +1/+1 counters.
- Fuel: land entries per turn. She adds one entry per nontoken artifact cast (14 in the list) and one self-returning land
  creature per turn, which any sacrifice outlet turns into a re-entry.
- Window: her own end step (mandatory target: a land you control). No mana window.
- How it wins: it does not by itself. The 99 win.
- How it dies: spot removal and creature wipes; a 3/3 that never needs to attack.
- Dependence: **enabler**. Without her the deck still has 21 cards that put lands onto the battlefield, but it loses the
  artifact entries, the free per-turn earthbend that feeds Terrasymbiosis (draw 2 a turn) and Zuran Orb / Goblin
  Bombardment re-entries, and the third piece of its best infinite line (below). Protection 3 to 4 fits.
- Cost: 4 MV, three single pips. Simulated (100,000 runs, free redo, tapped lands ignored): Toph castable on turn 4 in
  about 87 % of games.
- Rules points I checked: (a) an artifact entering under Toph triggers landfall (it is a land as it enters; same logic as
  the Ashaya ruling the builder cites); (b) an earthbent land that dies OR is exiled returns, so Rest in Peace does not stop
  the re-entry; (c) a token copy of an earthbent land copies only the printed land (type change and counters are not
  copiable values), so the copy is a plain land that enters untapped and triggers landfall. Point (c) is load-bearing for
  the combo in finding I-1 and is confirmed by Spellbook variant 3470-5702-6871 (status OK).

**Archetype and plan.** `landfall_lands`. Plan as I read the list: make 2 to 4 land entries a turn from turn 4 and turn
them into damage to each opponent (Tannuk, Sabotender, Valakut Exploration, Arbaaz Mir for artifact/legend entries),
Ragost turning artifacts into 3 damage to each opponent, backed by a land army (earthbent lands, Baloths, Titania,
The Earth King, Bumi). The list also holds three infinite lines made of on-plan cards (I-1), which the cards make the
real top end.

**My recount from Oracle text.**

| Function | My count | Cards and notes |
|---|---|---|
| Land entries (unconditional) | 21 | Rampant Growth, Shared Roots, Sakura-Tribe Elder, Wayfarer's Bauble, Harrow, Cycle of Renewal, Roiling Regrowth, Heaped Harvest, Druid Class (lvl 2), Explore, Crop Rotation, Burnished Hart, Solemn, The Earth King, Titania (ETB), Earthbender Ascension, Ashaya, Evolving Wilds, Terramorphic Expanse, Vibrant Cityscape, Cabaretti Courtyard |
| Land entries (conditional) | +3 | Zuran Orb and Toph, Hardheaded Teacher (re-entry only with an earthbent land plus an outlet), Springheart Nantuko bestowed on a land creature (paid copies) |
| Landfall payoffs that advance a win | 8 | Tannuk, Sabotender, Valakut Exploration, Tireless Tracker, Tireless Provisioner, Earthbender Ascension (after 4 counters), Springheart Nantuko, Rampaging Baloths |
| Weaker or non-landfall payoffs | 3 | Lotus Cobra (mana only), Druid Class (1 life), Titania (land to graveyard, not landfall) |
| Extra land plays (true) | 2 | Druid Class (repeatable), Explore (one-shot). The Earth King puts basics in per power-4+ attack (repeatable). |
| Ramp castable by turn 3 | 18 + 2 conditional | Sol Ring, Arcane Signet, Talisman, Chromatic Lantern, Bender's Waterskin, Rampant, Shared Roots, STE, Lotus Cobra, Great Divide Guide, Bauble, Harrow, Cycle, Roiling, Heaped Harvest, Provisioner, Ascension, Hart; Explore and Druid Class need a land in hand |
| Draw (weighted) | about 9 | Terrasymbiosis (2 a turn with Toph), Tireless Tracker, Tannuk (second entry a turn), Valakut (impulse), Stocking the Pantry, Garruk's Uprising (conditional), Solemn (1), Brightglass Gearhulk (2 tutored), True Ancestry (2-for-1), Ichor Wellspring (two cantrips) |
| Spot removal | 8 (6 unconditional) + Annie | Swords, Path, Beast Within, Fateful Absence, Stroke of Midnight; Hardlight Containment (needs an artifact: met), Sandbenders' Storm (power 4+ only), Rocky Rebuke (needs a big creature of mine) |
| Wipes | 1 | Planar Outburst: kills Toph and every nonland, nonartifact creature of mine unless Ashaya is out |
| Commander protection | 4 | Haystack, Collective Resistance, Origin of Metalbending, Redirect Lightning |
| Graveyard hate | 1 | Soul-Guide Lantern |
| Tutors | 2 + 1 | Chord of Calling (any creature), Brightglass Gearhulk (MV 0-1: Zuran Orb, Bauble, Sol Ring, Soul-Guide, Hardlight, Stocking); Crop Rotation is a land tutor |

**Lands and colors.** 38 lands: 21 basics (11 Forest, 5 Mountain, 5 Plains), 11 colored nonbasics, 2 colorless (Rogue's
Passage, Secret Tunnel), 4 basic-fetch lands. Sources from lands (fetches full): G 21, R 15, W 15, plus Exotic Orchard and
Rugged Prairie partially. With Karsten's partial weights (fetch 2/3, rocks and 2-MV land ramp 0.75): R and W about 20 for
4-MV spells (Toph needs about 16 each, met), about 15 for turn-2 gold {R}{W} (Arbaaz, Ragost need about 18.5 at 38 lands:
turn-3 plays), white short for GGWW Gearhulk on turn 4 (about 25 needed) and fine for Planar Outburst on turn 5 to 6.

**How the deck loses to...**
- *A creature wipe:* Tannuk, Sabotender, Arbaaz, Ragost, Cobra, Tracker, Provisioner, Nantuko, The Earth King, Toph all
  die. Survivors: Valakut Exploration, Terrasymbiosis, Ascension, Druid Class, Garruk's Uprising, Stocking, the lands
  (earthbent lands return as plain lands), artifact creatures only if the wipe says "nonland" or "nonartifact". The primary
  route is gone except Valakut. Real insurance: Haystack (one creature), Collective Resistance (one creature).
- *Eight sacrificeable 1/1s:* the noncombat pings and Ragost ignore them, but that opponent's sacrifice outlets usually ping,
  and 6 of the 9 creature engine pieces have toughness 2 or less (Sabotender 2/1, Cobra 2/1, Nantuko 1/1, Arbaaz 2/2,
  Ragost 2/2, Tracker 3/2).
- *Two bigger creatures:* 8 spot answers plus Annie, and the burn routes ignore blockers. This board is the deck's easiest.

## 2. Differences with the builder

| Item | Builder | Reviewer | Matters? |
|---|---|---|---|
| Infinite lines in the list | Only Bumi + Ashaya (R7); `toph-loop-hubs` "none can assemble" | Three more lines, all Spellbook-listed and inside the list: Toph + Springheart Nantuko + Lotus Cobra (3470-5702-6871), Toph + Nantuko + Tireless Provisioner (3875-5702-6871), Ashaya + Toph, the Blind Bandit + Zuran Orb (539-1315-7037) or + Goblin Bombardment (539-5147-7037). The bracket report counts "9 variants inside the list"; the notes never name them | Yes, I-1 |
| Springheart Nantuko use | "Bestow on Sabotender or Tireless Tracker" | Its game-winning use is bestowed on an earthbent basic with Cobra or Provisioner out (infinite landfall) | Yes, I-1 |
| Primary route clock | "Two pingers and 3 entries a turn: 6 to every opponent each turn" | Two of the four pingers by turn 7 (14 cards): 9.5 %; by turn 13: 18 %. Typical board: 0 or 1 pinger, 3 per opponent a turn | Yes, I-2 |
| Wipe insurance | 5 (Haystack, Ba Sing Se, Baloths, Titania, Nantuko) | 1 to 2 for the primary route: Ba Sing Se, Baloths, Titania and Nantuko rebuild bodies, not pingers | Yes, I-3 |
| Planar Outburst | "One-sided for this deck"; "a second symmetric wipe would kill the pingers" | Planar Outburst itself kills Toph and every pinger unless Ashaya is out; it spares only lands, earthbent lands and artifact creatures | M-1 |
| landfall_payoffs | 11 + Chord = 12 | 8 that advance a win + Cobra; Druid Class (1 life) and Titania (not landfall) are padding. With Arbaaz (artifact/legend entries) and Chord: about 11 | M-2, gate still passes |
| land_entries | 25 + Toph | 21 unconditional; Zuran Orb and Hardheaded Teacher are conditional pairs | M-2, no effect (min 12) |
| Ramp | 20 | 18 unconditional + Explore and Druid Class conditional | M-2, at the profile min 18 |
| Draw | 10 | About 9 weighted; Terrasymbiosis (commander-conditional) carries it | M-3 |
| Soul-Guide Lantern | primary tag `removal` | Graveyard hate, not a spot answer; base removal reads 9 primary instead of 8 | M-2 |
| Extra land drops | 7 listed, 5.0 weighted | 2 cards grant land plays; the rest are re-entries. The builder already writes it as the weak line | Agree |
| Seismic Tutelage targets | bear, Bandit, Tracker, beasts | Same, plus Brightglass Gearhulk (4/4 first strike, trample) and Bumi (5/4 trample), the best non-land targets | M-4 |
| Colors, lands, curve, cast odds | G 20.4 / R 15.4 / W 15.4; 75.5 % keepable | Agree (75.5 % recomputed; Toph on turn 4 about 87 %) | No |

## 3. Findings

### BLOCKING
None. No Bracket 3 rule is broken (section 5), every card is in the pool with its assigned copy, and an honest recount
still passes the gate (land_entries 21, landfall_payoffs about 11 with Arbaaz and Chord, both boards over 10).

### IMPORTANT

**I-1. The plan file and notes hide the deck's three strongest closers, and the guide teaches the weak use of the key piece.**
- Failure: the list holds infinite landfall lines made of cards that are on plan anyway, but R7, the routes, section 9
  and the guide name only Bumi + Ashaya. The guide line "bestow on Sabotender or Tireless Tracker" makes the owner miss a
  turn-5 win.
- Evidence (Spellbook bulk, all "status OK", all cards in the list):
  - Toph + Springheart Nantuko + Lotus Cobra, or + Tireless Provisioner: bestow Nantuko ({1}{G}) on the land Toph
    earthbent at the end step; each landfall pay {1}{G} for a token copy of that land (a plain Forest, enters untapped);
    the token taps for G and Cobra (or Provisioner's Treasure) adds 1, so the loop is free: infinite landfall. With
    Sabotender or Tannuk it is infinite damage to EACH opponent; with Valakut Exploration the whole library is exiled and
    deals that much to each opponent at the end step; with both Cobra and Provisioner it is infinite mana too.
    Assembly: Toph turn 3 to 4, then Cobra + bestowed Nantuko = 4 mana: turn 5 is possible. Odds of holding Nantuko plus
    Cobra or Provisioner (Chord fetching one missing piece): 8 % by turn 7, 10 % by turn 9, 15 % by turn 13.
  - Ashaya + Toph, the Blind Bandit + Zuran Orb or Goblin Bombardment: under Ashaya Bandit is a Forest land; her ETB
    earthbend can target herself; sacrifice her, she returns, earthbends herself again. Infinite landfall and life with
    Zuran Orb; infinite damage to any targets with Bombardment. 2.5 % by turn 9, 5 % by turn 13.
  - Bumi + Ashaya (owner-accepted): 7 % by turn 9.
- Bracket: these are three-card lines with the commander counted (Toph + Nantuko + Cobra) or three cards of the 99
  (Ashaya lines); `check_phase2_bracket.py` includes them and flags none, and the owner's 2026-10-18 combo rule welcomes
  three-card lines with the commander. Not a rule break. Report it so the owner knows the deck has a turn-5 three-card
  infinite that uses his commander's free trigger, and so Commander Salt's combo reading is not a surprise.
- Fix: add R8 and R9 to the rules points; add a fourth route in `plan.json` (noncombat, closers that no other route lists,
  for example Springheart Nantuko, Lotus Cobra, Tireless Provisioner, Ashaya) or describe the lines in `vs_three` of the
  existing routes; rewrite the guide lines of Springheart Nantuko, Lotus Cobra, Tireless Provisioner, Ashaya, Toph the
  Blind Bandit, Zuran Orb, Goblin Bombardment and Chord of Calling (which piece to fetch when). Pilot rules: point Toph's
  end-step earthbend at an untapped basic Forest when Nantuko is in hand; cast the pinger first, then go off. Sourced
  (Spellbook) for the lines; odds computed here.

**I-2. The declared main route has four closers and its stated clock is a best case.**
- Failure: "landfall burn" closes with Tannuk, Sabotender, Valakut Exploration and Arbaaz Mir only. The `vs_three` text
  counts two pingers at once.
- Evidence: one of the four by turn 7 (14 cards) 46 %, 54 % with Chord; two of the four 9.5 % by turn 7, 18 % by turn 13.
  With one pinger and 3 entries a turn each opponent takes 3 a turn: 13 turns for 40 life. Adding Ragost and Bombardment,
  two closers of six by turn 7 is 20 %. The deck makes far more mana than its closers can spend (7 mana sinks are utility:
  Rogue's Passage, Secret Tunnel, Ba Sing Se, Stocking, Tracker, Nantuko, Ragost).
- Fix [J]: add a mana sink that damages each opponent with no tap: **Fire Nation Archers** (owned, free copy, in no other
  list; {3}{R} 3/4 reach; "{5}: 2 damage to each opponent and a 2/2", repeatable). At 10 to 15 mana by turns 7 to 8 it is 4
  to 6 damage to every opponent a turn plus blockers, survives pings (toughness 4) and is a Chord target (X=4). Cut
  **Rocky Rebuke** (removal 8 to 7 spot, min 6; through_big_creatures 17 to 16, min 10; it is the one "bad early" answer
  that needs my own big creature). Legion Guildmage (free, {R}{W}, tap: 3 to each opponent for 6) is the cheaper,
  weaker alternative. Rewrite the route's `vs_three` with the real odds. Salt effect: neutral to positive (one more
  closer, no function below min).

**I-3. The primary route dies to one creature wipe, and the wipe-insurance line is padded.**
- Failure: every pinger except Valakut Exploration is a creature, most with toughness 2 or less; the five listed insurance
  cards mostly rebuild bodies.
- Evidence: three opponents have seen about 0.9 wipes by turn 8 (63 % at least one, skill section 6). A wipe kills
  Tannuk, Sabotender, Arbaaz, Ragost, Cobra, Tracker, Provisioner, Nantuko, The Earth King and Toph. Ba Sing Se, Baloths,
  Titania and Nantuko do not bring back a pinger; Haystack saves one creature for {2} and must be untapped with the mana
  held. Toughness: 6 of the 9 creature engine pieces are toughness 2 or less, so the Board 1 opponent's sacrifice-pings
  also pick them off.
- Fix [J]: (a) **Hakoda, Selfless Commander** (owned, free copy; {3}{W} 3/5 vigilance; "Sacrifice Hakoda: creatures you
  control get +0/+5 and gain indestructible until end of turn", instant speed; an Ally, so Great Divide Guide makes it tap
  for mana) for **Redirect Lightning** (protection stays 4: Hakoda also saves Toph from destroy and damage). (b) Correct the
  `wipe_insurance` support line to what protects the route (Haystack, Hakoda, Collective Resistance; Valakut as the
  enchantment pinger). (c) Pilot notes: deploy pingers one or two at a time, Valakut first; with Ashaya out, Toph's
  end-step earthbend may target a pinger (it is a land) so it returns when it dies; Chord and True Ancestry rebuild.
  Salt effect: neutral.

### MINOR

- **M-1. Planar Outburst's guide line and the wipe reasoning are wrong.** "Destroy all nonland creatures" kills Toph and
  every pinger unless Ashaya is out; it spares lands, earthbent lands and Hart, Solemn, Gearhulk (artifact-lands under
  Toph). Write it as a reset when behind, best with Ashaya out, and drop "one-sided" from R5 and the wipe row. [J]
- **M-2. Padding in the plan file (no gate effect).** Druid Class (1 life) and Titania (land to graveyard) in
  landfall_payoffs; Toph, Hardheaded Teacher and Zuran Orb in land_entries; Soul-Guide Lantern primary-tagged `removal`
  (it is graveyard hate). Honest counts: payoffs about 11 with Arbaaz and Chord, land_entries 21, spot removal 8, ramp 18
  plus 2 conditional. Fix: move Arbaaz Mir into landfall_payoffs (it pays on every artifact or legend entry), keep
  Titania as a lands-matter payoff with the note, retag Soul-Guide Lantern.
- **M-3. Draw is at its floor with several half pieces.** Garruk's Uprising draws only on power-4+ entries; Valakut is
  impulse; Ichor Wellspring is two cantrips; Terrasymbiosis carries it and depends on Toph. No change needed if I-2 and
  I-3 are applied; if a slot opens later, Glorious Sunrise (owned, Spanish only, free) draws every combat with a power-3+
  creature and also gives a land {G}{G}{G}. [J]
- **M-4. Seismic Tutelage guide (owner's target rule kept).** Add Brightglass Gearhulk (first strike and trample keep the
  doubled creature alive and connecting) and Bumi (trample) as targets; note that it is a single-target clock (one opponent
  per attack), the third route's closer, not a table kill.
- **M-5. Basics can run out in long games.** 21 basics against about 22 basic-fetching effects (two-land spells counted
  twice) plus The Earth King every attack and four fetch lands. Pilot note: from turn 8 on, fetch with priority for the
  card that needs a basic most (The Earth King, Harrow-type spells).
- **M-6. Hardlight Containment on an artifact-land.** If Toph's end step earthbends the enchanted artifact, or it is
  sacrificed to Ragost or Zuran Orb, the exiled creature returns. Pilot note.
- **M-7. Bender's Waterskin and Chromatic Lantern "never bad".** Both are 3-MV rocks in a list with 18 three-drops
  (lesson L5); late they are weak draws. The builder's purchase proposals already replace Waterskin (Cultivate).
- **M-8. Purchase proposals carry no live evidence.** Exploration (rank 1) has no price reading; Cultivate and Farseek
  are 2026-10-17 hints. They are proposals only (none is in the list); the lead verifies live stock at Game of Magic
  Singles before any of them is used.

### Salt (second objective)
- Raising without hurting consistency: Fire Nation Archers (I-2). The infinite lines of I-1 are already in the list and
  Salt reads Spellbook combos, so declaring them changes nothing on Salt but much in play.
- Would drop Salt significantly (do not cut without a new review): Crop Rotation (the one Game Changer), Chord of Calling,
  Lotus Cobra, Tireless Provisioner, Springheart Nantuko, Ashaya, Bumi, Toph the Blind Bandit, Zuran Orb, Goblin
  Bombardment (all combo pieces, I-1).

## 4. Lessons checklist

| Lesson | Covered? | Evidence |
|---|---|---|
| L1 one plan | Yes, with I-2 | One fuel (entries) feeding three routes that share it; main route closers thin |
| L2 ratios follow the plan | Yes | 21 land-entry cards, 18 to 20 ramp, 38 lands; no haste needed (earthbend gives it) |
| L3 attacking decks | Partial (backup only) | Land army has trample (Garruk's Uprising, Ascension, Bumi), unblockable lands, built-in haste; defense while tapped: Bumi untaps lands, earthbent lands return, Sabotender and Archers (if added) have reach |
| L4 dependence | Yes | Enabler, protection 4 (Haystack, Collective Resistance, Origin, Redirect Lightning) |
| L5 value by turn | Mostly | Everflowing Chalice, Selesnya Signet, Boros Locket cut; Waterskin and Lantern remain (M-7) |
| L6 proven role-players | Yes | The Earth King and Seismic Tutelage are in; Horizon Stone and Propaganda are Azula's and Ezio's priors, not Toph's |
| L7 dead clauses, mini-combos | Yes | Liquimetal + Haywire Mite cut; named: Hardheaded's Lesson bonus, Secret Tunnel's pair clause, Druid Class lvl 3, Outburst's awaken. The combo pieces all work alone (I-1) |
| L8 reference boards | Yes | Board 1: pings, Valakut, Ragost, Garruk's trample, Outburst; Board 2: 8 spot answers plus Annie, burn ignores blockers |
| L9 Salt is not the measure | Yes | No pick or cut by score |
| L10 guide says how to use | Partial | Nantuko, Planar Outburst and Seismic Tutelage lines need the fixes of I-1, M-1, M-4 |

## 5. Rules checklist

| Rule | Result |
|---|---|
| Pool and copies | 100 cards, every name in the pool and in `assignment.json` with its copy; assignment reports 0 missing, 0 problems |
| Language (bilingual: English when owned in both) | All 15 Spanish picks are cards owned only in Spanish (Lotus Cobra, Burnished Hart, Arbaaz Mir, Swords, Path, Fateful Absence, Planar Outburst, Chord, Soul-Guide Lantern, Exotic Orchard, Clifftop Retreat, Fortified Village, Rugged Prairie, Battlefield Forge, Vibrant Cityscape) |
| Loans | None used, none proposed |
| Owed cards | Smoldering Marsh (UB) does not concern this deck |
| Purchases | Three proposals at Game of Magic Singles only, none in the list, within the shared budget on hints; live check pending (M-8) |
| Scarce copies | Builder's table names the contested cards; the lead's resolution (Battlefield Forge and one Soul-Guide Lantern to Toph) holds. Proposed swaps use free copies in no other list (Fire Nation Archers, Hakoda). Reckless Fireweaver was checked and is NOT available (Spanish deck plays the only copy) |
| Bracket 3 (`check_phase2_bracket.py`, run 2026-11-02) | PASS, floor 3. Game Changers: Crop Rotation only (live Scryfall `is:gamechanger`, 53 cards, read 2026-11-02). No extra turns, no mass land denial, no reversible cards. Two-card infinite: Bumi + Ashaya, late (owner-accepted). Three-card lines of I-1 are not two-card combos |
| Nothing cut or held back to look weaker | None found |

## 6. Mana and flow

- Keepable (2 to 4 lands in 7) 75.5 % per look; Toph on turn 4 about 87 % (simulation, tapped lands ignored).
- Ramp by turn 3 (10 cards): 18 unconditional pieces give 88 %; the builder's 91 % (20 pieces) reproduces.
- Colors: G 21 land sources, R and W 15 each; Arbaaz and Ragost are turn-3 plays; Gearhulk is a turn-5 play.
- Curve: 61 spells, average MV 2.61, MV 3 holds 18 cards (turn 3 is crowded; turn 2 has 21 plays).
- Card flow: about 2 cards spent a turn at peak; gain 1 natural + Terrasymbiosis 2 (with Toph) + Tannuk or Tracker. Without
  Toph and Terrasymbiosis the hand empties by about turn 7, as the builder writes.
- Bad when drawn: 11 early (builder) plus Waterskin and Lantern late (M-7): 13, slightly over the warning of about 12.

## 7. Multiplayer check

- Against three: pings, Valakut and Ragost hit each opponent at once; the land army kills one player per attack; the I-1
  lines kill the table at once with a pinger or Valakut out.
- The pod's interaction: spot removal on Ragost or Tannuk slows the burn but no single card ends the plan (no single
  permanent carries it; Valakut is the only non-creature pinger). A creature wipe is the real threat (I-3). Graveyard hate
  barely matters (earthbent lands return from exile too; only Titania's ETB and True Ancestry use the graveyard). Attack
  taxes hit only the backup. Library-search hate (Stranglehold, Opposition Agent, Aven Mindcensor-type cards) is the
  deck's worst single-card hate: about 20 of the 21 entry cards search the library; answers: Beast Within, Stroke of
  Midnight, and the creature removal for the creature versions.

## 8. Verdict

**PASS (ship to Salt).** No rule is broken and the honest recount passes the gate. Before the guide is written, apply
I-1 (declare and document the infinite lines; rewrite the Nantuko line), and consider the two swaps of I-2 and I-3
(Rocky Rebuke to Fire Nation Archers, Redirect Lightning to Hakoda), which add a closer and wipe insurance without taking
any function under its minimum.

## Round 3 re-review (2026-11-07)

Scope: commit 21674e6 against 30de44d (`decks/phase2/toph-the-first-metalbender.*`). List change: Rocky Rebuke to Fire
Nation Archers, Redirect Lightning to Hakoda, Selfless Commander; plan file and build notes rewritten. Owner's standing
rules of 2026-11-07 applied: card choices free, only Bracket 3 rules and the deck's copy and budget rules bind, every legal
combo accepted, Salt second with Toph at 7.0 or more.

### Checks rerun
- `plan_density.py`: PASS, 0 failures, 0 warnings. land_entries 26, landfall_payoffs 13, through_wide_board 15,
  through_big_creatures 17; bad when drawn 10 early + 2 late = 12 (at the warning line, not over).
- `check_phase2_bracket.py`: PASS, floor 3, 1 Game Changer (Crop Rotation), Bumi + Ashaya the only flagged line (late).
- `assignment.json`: Fire Nation Archers (TLE 237, EN) and Hakoda (TLA 23, EN) are given to Toph only, no other deck holds
  them; Rocky Rebuke and Redirect Lightning are released; problems 0, missing 0.

### Recount from Oracle text (changes only)
| Function | Round 2 | Round 3 | Note |
|---|---|---|---|
| Spot removal | 8 (6 unconditional) | 7 (6 unconditional + Sandbenders' Storm, power 4+ only) | min 6 met |
| Commander protection | 4 | 4: Haystack, Collective Resistance, Origin of Metalbending, Hakoda | Against targeted EXILE (Swords, Path) only Haystack and Collective Resistance's hexproof remain; Hakoda covers destroy and damage. Enough for an enabler (3 to 4) |
| Wipe insurance for the route | 1 to 2 | 3: Hakoda (team), Haystack, Collective Resistance (+ Valakut as the non-creature pinger) | I-3 closed |
| Landfall payoffs | about 11 honest | 12 + Chord, Arbaaz moved in | honest now |
| Ramp, draw | 18 + 2, about 9 weighted | unchanged | M-3 still minor |
| Closers | main route 4 | main route 5 (Archers), 4 routes, 15 unique closers | I-2 closed |

Round-2 items: I-1, I-2, I-3, M-1, M-2, M-4, M-5, M-6, M-7 closed in the files. Open: M-3 (draw at its floor, minor) and
M-8 (no live price; the lead's stock step).

### Findings

**R3-1 (IMPORTANT, my own round-2 error carried into the notes): Chord of Calling cannot fetch Springheart Nantuko for the
R8 combo.** Chord puts the creature onto the battlefield; Nantuko only attaches when CAST for its bestow cost, so a
Chord-fetched Nantuko is an unattached 1/1 that makes Insects, not land copies. The build notes' Chord line ("the missing
combo half (Springheart Nantuko X=2, ...)") and the R8 odds (8 % by turn 7, 15 % by turn 13, from my round-2 simulation
that let Chord find Nantuko) are wrong. Recomputed (300,000 runs; Chord finds only Cobra or Provisioner): **5.0 % by turn
7, 6.4 % by turn 9, 9.7 % by turn 13**. Fix: Chord's guide line reads "for R8 fetch Lotus Cobra (X=2) or Tireless
Provisioner (X=3), never Nantuko; for R9 fetch Ashaya (X=5) or the Bandit (X=3)"; correct the odds in section 2 and the
route. Sourced (Oracle text of Springheart Nantuko and Chord of Calling).

**R3-2 (IMPORTANT, purchase choice): Eladamri's Call is the right power buy, if the live price fits.**
- Value: an instant creature tutor that puts the card in HAND, so it is the only tutor in the list that can find Nantuko
  for R8. Simulation: R8 by turn 7 goes from 5.0 % to 10.6 %, by turn 13 from 9.7 % to 19.6 %; it also finds Ashaya, the
  Bandit, Bumi, any pinger, Ragost, Fire Nation Archers or The Earth King. It answers the Phase 1 Salt cap ("combo wincons
  with no tutors").
- Price risk: the only Game of Magic hint (2026-10-17 reading) is a NM FOIL at 25,080 CLP; no non-foil was read. After the
  other reviewers' picks (Azula Soul-Guide Lantern about 742, Ezio Golgari Signet about 570 and Battlefield Forge about
  915) about 2,770 CLP is left for Toph before Arcane Denial. Buy it only if a non-foil copy is at or under that remainder.
- Swap: cut **Bender's Waterskin** (3-MV rock, now tagged bad late; ramp by the plan's count 20 to 19, profile min 18)
  rather than Sandbenders' Storm (that would take spot removal to the minimum 6). [J]
- Fallback if Eladamri's Call does not fit, in power per CLP (old hints, live check by the lead): **Wood Elves** (about
  570 CLP: 3-MV creature that puts a Forest onto the battlefield UNTAPPED; land entry, Ashaya body, convoke and Bombardment
  fodder) for Bender's Waterskin; then **Farseek** (about 1,760) or **Cultivate** (about 1,120) for Chromatic Lantern only if
  money remains. Exploration has no reading at Game of Magic. Too expensive in the hints: Three Visits 7,960, Azusa 12,480,
  Dryad of the Ilysian Grove 9,880, Worldly Tutor 39,400.

**R3-3 (MINOR): the "infinite landfall" route names Arbaaz Mir as a closer for R8.** The R8 copies are tokens and not
historic, so Arbaaz never triggers; he does close R9 (the Bandit is a nontoken legendary entering each loop). Closers for
R8: Sabotender, Tannuk, Valakut Exploration, Fire Nation Archers when the loop also makes mana (Cobra AND Provisioner),
Rampaging Baloths (army), Earthbender Ascension (one huge trampler). Fix the `vs_three` wording.

**R3-4 (MINOR): the Nantuko pilot rule asks for an "untapped" basic Forest.** Tapped status is not copiable: every copy
enters untapped whatever the original's state. Any earthbent land that taps for {G} works; a basic Forest is best. Wording
only.

### Salt
No change lowers Salt: Archers adds a closer and a sink, Hakoda replaces a narrow protection spell, every combo piece and
tutor stays. Eladamri's Call is the one buy likely to raise it (tutor for the combo pieces). Do not cut the combo pieces
listed in build notes section 13.

### Verdict round 3
**PASS (ship to Salt).** No Bracket 3 rule broken, gate passes, the round-2 findings are closed. Before the guide is
written, fix R3-1 (Chord line and R8 odds) and the R3-3 and R3-4 wording. Purchase: Eladamri's Call for Bender's Waterskin
if a non-foil copy fits the roughly 2,770 CLP left; otherwise Wood Elves for Bender's Waterskin.
