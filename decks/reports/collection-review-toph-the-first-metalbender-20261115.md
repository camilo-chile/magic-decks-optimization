# Collection review: Toph, the First Metalbender (Phase 2 step 12.2, iteration 3, 2026-11-15)

Reviewer: independent champion (Opus 5.5 high), under `docs/proposals/collection-optimization-brief-20261114.md`.
Under review: `decks/phase2/toph-the-first-metalbender.txt`, `.plan.json`, `.build.md` (builder Fable 5.2 high, 7 swaps).
Card text: pool Oracle text and the Oracle cache `oracle-cards-20261011210156`. No purchases, loans or exchanges.

**Verdict: FIX** (two swaps from the binders, nothing blocking). Ranked list in section 8.

## 1. Rules (run by the reviewer)

| Check | Result |
|---|---|
| `python scripts/check_phase2_bracket.py decks/phase2/toph-the-first-metalbender.txt` | **PASS**: floor 3, 2 Game Changers (Crop Rotation, Drannith Magistrate), no extra turns, no mass land denial, no reversible card, 3 review items (section 7 c). Re-run on the real list LAST, after the scratch test. |
| Scratch list with the two fixes (`.../scratchpad/fix/toph-the-first-metalbender.txt`) | **PASS**, same floor, same 3 review items, 2 Game Changers. |
| `python scripts/plan_density.py` | **PASS**, 0 failures, 1 warning (draw 9 against 10). |
| Card count | 100: commander, 61 nonland, 38 lands (script). |
| Game Changers in the pool | Only Crop Rotation and Drannith Magistrate carry `game_changer` in the whole Naya pool (script over 483 cards): the third slot cannot be filled. |

## 2. Independent reading (written before opening the plan file and the notes)

**Commander.** {1}{R}{G}{W} 3/3. Nontoken artifacts are lands (no mana ability); end step: earthbend 2. Fuel: land
entries. Every nontoken artifact cast is a landfall; the one land earthbent per turn returns when it dies or is exiled,
so it is a free re-entry engine for anything with a sacrifice or exile cost. Class: **enabler** (the 99 ramp and ping
without her; the artifact entries, the Coffin loop and loop B need her). 4 MV, recast at 6.

Rules points I checked from Oracle text: an artifact entering under Toph is a land entering (confirmed by the 2026-11-08
review, CR 603.6d); earthbend's return covers exile, so graveyard hate and exile costs do not stop it; earthbend sets base
0/0, so never earthbend Ashaya, Bumi or Gearhulk; Ragost makes every artifact a Food, so an earthbent artifact sacrificed to
Ragost returns.

**Archetype and plan.** `landfall_lands`, noncombat drain: 2 to 4 entries a turn, each 1 damage to every opponent per
pinger (Sabotender, Tannuk, Valakut), Arbaaz on historic entries, Ragost / Bombardment / Archers as burst; loops close it.
Backup: earthbent land army (Earth King, Tutelage, Bumi), reusing the same earthbends.

**My recount from Oracle text.**

| Function | My count | Cards / note |
|---|---|---|
| Lands | 38 | 21 basics, 17 nonbasic; colorless: Secret Tunnel, Urza's Cave; always tapped: Gruul Turf + 3 fetches (4) |
| Ramp, cast by turn 3 | 20 | Sol Ring, Signet, 2 Talismans, Wayfarer's Bauble, Chalice, Rampant Growth, Shared Roots, STE, Cobra, Great Divide Guide, Explore, Druid Class, Harrow, Cycle, Heaped Harvest, Wood Elves, Provisioner, Ascension, Wrenn (Wrenn conditional) |
| Land entries without Toph | about 20 | the land ramp, 3 fetches, Urza's Cave, Gruul Turf, Crop Rotation, Earth King, Ashaya; plus the 14 artifacts with Toph |
| Damage payoffs that hit EACH opponent | 7 | Sabotender, Tannuk, Valakut, Arbaaz, Ragost, Archers (Bombardment is single target); access with Chord = 8, Seismic Sense half |
| Draw that nets cards | 9 | Terrasymbiosis, Pantry, Tracker, Valakut, Tannuk, Ichor, Gearhulk, Wrenn −2, Mishra's Bauble + Lantern at half |
| Spot answers | 8 + 2 modal | Swords, Path, Fateful Absence, Beast Within, Chaos Warp, Stroke, Haywire Mite, Annie; Collective Resistance and Origin once per game state |
| Wipes | 1 | Planar Outburst (spares lands and every artifact-land) |
| Commander protection | 4 | Collective Resistance, Origin, Redirect Lightning, Make a Stand; only 2 stop exile (Collective, Redirect) |
| Graveyard hate | 1 + Drannith | Soul-Guide Lantern |
| Counterspells / table-scaling draw | 0 / 0 | none in the Naya pool |
| Curve | avg MV 2.36 | 0:3, 1:11, 2:20, 3:18, 4:6, 5:3 |
| Pips | G 39, W 13, R 12 | sources with fetches about G 21, R 17, W 17 |

**How it loses.**
- *Wipe:* Sabotender, Tannuk, Arbaaz, Ragost, Archers, Tracker die; lands, earthbent lands, Valakut, Terrasymbiosis,
  Pantry, Bombardment stay. Two to three turns to threaten again.
- *Wide board of small blockers:* irrelevant to the drain; the army has only Bumi and Ascension trample and the Tunnel.
  Their sac-pings kill the toughness-1/2 pingers.
- *Two bigger creatures:* the Coffin blanks their damage; 6 spot creature answers; the drain ignores them.
- *Fast combo:* no counterspell; only instant removal and Drannith.

## 3. Differences with the builder

| # | Builder | Reviewer | Weight |
|---|---|---|---|
| D1 | Toph listed in `land_entries` as a guaranteed piece (gate 26) | Her earthbend is not an entry; her artifact clause only makes artifacts entries. Without Toph-dependent cards about 20. | none (still far above 12) |
| D2 | Seismic Sense counted in full as a tutor for `landfall_payoffs` and `through_wide_board` | It sees the top X (6 to 8 cards): about 40 % to hit one of the 6 creature closers. Half at most. Payoffs: 9 + Chord + half = 10.5, a thin pass. | minor (M1) |
| D3 | `extra_land_drops` 10 cards | Heaped Harvest, both Baubles' cousins, Urza's Cave, Zuran Orb, Bombardment, Gruul Turf all share ONE resource, Toph's single earthbend a turn. Repeatable without Toph: Druid Class, Earth King, Ashaya = 3 (builder says so). | minor (M1) |
| D4 | Drain access 9 "not fixable from the pool" | Fixable: Legion Guildmage, cut by this very build, is free. | IMPORTANT (I1) |
| D5 | Draw 9 "no other card in the pool" | Solemn Simulacrum (free EN) nets a card, ramps and is the best earthbend target with Ragost; missing from the cut log. | IMPORTANT (I2) |
| D6 | Inscription OUT because its fight risks engines | Its fight is free with an earthbent land (the land returns, a landfall). Verdict stands for another reason (M2). | minor |
| D7 | Bumi + Ashaya "turn 6 at the earliest" | Under Ashaya Bumi earthbends himself and gains haste: reachable turn 5 to 6 in rare draws. Not intentional, still legal (section 7 c). | note |

Everything else matches: archetype, enabler class, routes, removal (8 by tag), wipes, the Coffin rules point, the loops.

## 4. Findings

### BLOCKING
None.

### IMPORTANT

**I1. The build cut its own 10th access card to the drain route.** Before this step the access cards were Sabotender,
Tannuk, Valakut, Arbaaz, Ragost, Bombardment, Legion Guildmage + Chord, Seismic Sense, Water Tribe Rallier (10). The
builder swapped Rallier for Fire Nation Archers (net zero) and Legion Guildmage for Talisman of Conviction (−1), then
wrote the 9 as "not fixable from the pool".
- Evidence: Guildmage is free (1 English copy, back in the binder by this build). {5}{R}, tap: 3 damage to EACH opponent;
  {2}{W}, tap: tap a blocker or an attacker; a 2-mana blocker. With Archers the late flood (6 + 5 mana) is 5 damage to every
  opponent a turn. Access by 14 cards seen: 9 cards 76 %, 10 cards 80 % (hypergeometric, 99 cards, no mulligan).
- The slot: **Explore**, the weakest ramp piece: a one-shot extra land drop that needs a land in hand, plus a cantrip. Ramp
  20 to 19 (profile min 18, target 20); land entries 25 to 24.
- Fix: `-1 Explore`, `+1 Legion Guildmage` (EN, English binder). Sourced: R18 (10 access cards), R35; the slot choice [J].

**I2. The draw WARN is fixable from the binder, and an owner's original card was never re-examined.** Solemn Simulacrum
(1 English copy, free) is in his original Toph list (lessons appendix, cut by Phase 1) and absent from this build's cut log
and its "re-examined from his original list" line (R36, R40).
- What it does here: an artifact creature, so under Toph a land. Cast: 1 entry + Arbaaz ping, then a basic (entry 2).
  Dies: a card. As Toph's earthbend target it is the best engine in the pool: sacrifice it to Ragost (every artifact is a
  Food: 3 damage to each opponent), Zuran Orb or Bombardment, draw, it returns, fetches a basic: 3 entries, a card and a
  ramp every turn. Chord finds it (X=4). 2/2 body.
- Draw 9 to 10: clears the only gate warning with a card that nets cards, not with a cantrip.
- The slot: **Everflowing Chalice**. On turn 2 it is a 1-colorless rock (owner lesson L5: the same card failed in Ezio);
  with Toph a free entry, a job Mishra's Bauble and Zuran Orb (both 0-cost, both kept) already do, including the 0-cost
  artifact of loop B and the Teacher/Turf template.
- Ramp by tag 19 to 18 timed (profile min 18) plus Solemn on turn 4; lands + lasting ramp stays far above 46 (R8); land
  entries unchanged (Solemn is two). This trades one turn-2 colorless mana for a card, a basic and a repeatable kill
  engine; Toph on turn 4 stays near 89 % (Chalice is 1 of 20 ramp pieces) [J, not simulated].
- Fix: `-1 Everflowing Chalice`, `+1 Solemn Simulacrum` (EN, English binder). Tag it `["draw", "ramp"]`, add it to
  `land_entries`; `bad_when_drawn: never`.

### MINOR

**M1. Plan file generosity (no gate effect).** Toph in `land_entries`; Seismic Sense in full for two functions; six
Toph-pair cards in `extra_land_drops`; Earthbender Ascension in `through_wide_board` (trample on one creature after four
quest counters). Corrected, every gate function still passes; `landfall_payoffs` passes at about 10.5. Write the
corrected numbers in the notes; after I1 Guildmage joins `through_wide_board` and `through_big_creatures`.

**M2. Inscription of Abundance: the verdict is right, part of the reason is wrong.** The fight mode is free with an earthbent
land (it dies, returns, triggers landfall). It stays OUT because an earthbent land has power 2 to 3 (3 to 4 with Scales),
so the fight kills only small creatures and fails against Board 2, and the 5-mana kicked mode is a weak rate next to
Swords, Path and Chaos Warp. Rewrite the line.

**M3. Protection against exile is thin.** After Haystack left, only Collective Resistance and Redirect Lightning stop
Swords or Path on Toph. **Airbender's Reversal** (free EN, {1}{W} instant Lesson): airbend Toph in response, recast her
from exile for {2} with no tax; or destroy an attacking creature. It is the first candidate for the next open slot (over
Make a Stand or Hardened Scales), not a change now [J].

**M4. The Coffin's failure points** (add to section 4 of the notes): it is a land under Toph, so artifact wipes and
"destroy target artifact" kill it before the end step (no return: it was not earthbent yet); it competes with every other
earthbend target; life loss and mill pass through it.

**M5. Pool fields disagree** for some shared copies (Goblin Bombardment and Chaos Warp: `held_by` against `printings`).
Languages are settled by `scripts/assign_copies.py`; Guildmage and Solemn exist only in English.

## 5. Knowledge audit

| # | Source | What it demands of this deck | Met? |
|---|---|---|---|
| 1 | Skill + `archetypes.json` (`landfall_lands`) | Lands 38-40; ramp 18/20; entries 12/16; payoffs 10/12; draw 10 net (cantrips out, modal cards once); removal 6/8; wipe 1; protection 3-4 (enabler); both boards | Lands 38 yes; ramp 20 yes; entries yes; payoffs thin pass (M1); **draw 9 no (I2 fixes)**; removal 8 yes; wipe 1 yes; protection 4 yes; boards yes |
| 2 | Champion addendum, 41 items | See table below | 35 met, 4 partly, 2 not possible |
| 3 | Mana study, notes/02, notes/13; owner: far more ramp, repeated land drops | Karsten sources per pip; untapped early; ≤3 always-tapped; landfall 39.5 lands, 16 entries, 7 extra drops | Sources G 21 / R 17 / W 17 meet 19/17/17 targets on Toph's turn; 4 tapped lands (written exception, each fetch is 2-3 entries); 38 lands at the bottom of the band with avg MV 2.36; entries 25; repeatable extra drops 3 without Toph (Toph is the 4th) |
| 4 | Other notes (03 card flow, 04 interaction, 05/12 multiplayer, 07/10 engines) | Draw 10+ that nets; layered protection; team-wide damage; payoffs or ramp is wasted | All routes hit each opponent; payoff density is the known limit (I1) |
| 5 | Toph primers | Cheap artifacts as entries, Cobra/Provisioner, Zuran Orb, Crop Rotation, Coffin, Solemn (study: B3 1,403/3,150, syn 0.38), Chromatic Lantern; traps: infinite mana with no sink, too few answers | Must-haves owned are in; **Solemn missing (I2)**; Lantern out with a sound reason (mana is not the short resource); Archers + Guildmage are the sinks |
| 6 | Owner lessons, play reviews, gate review (f) | L1-L10; Earth King and Seismic Tutelage in; dead clauses named; every gate function declared | Yes; section 6 |
| 7 | Final review 2026-11-08 and `decks/measured/` | Only 3 true pingers; keep Gearhulk and Mishra's Bauble; cheap answers restored | Gearhulk, Bauble in; cheap answers 6 at MV ≤2; iteration-1 cards (Chromatic Lantern, Reckless Handling, Rogue's Passage, Inscription, Haystack, Hardlight) all weighed |
| 8 | Owner card review 2026-11-14 | A reasoned verdict per card | Coffin IN: agree (protection from everything every opponent turn for {2}, each return a landfall and Arbaaz ping). Scales IN: acceptable, owner priority; it is an orphan by the gate and does nothing alone, first cut if a slot is needed. Inscription OUT: agree, reason partly wrong (M2). Alibou OUT: agree (needs attacking artifact creatures; the list has 2; one target). Return the Favor OUT: agree (Azula's only copy, Redirect does it for {R}). Tome of Legends OUT: agree (Toph enters about twice a game and never attacks). Commander's Sphere OUT: agree (no free copy; Talisman is cheaper). Water Tribe Rallier OUT: agree, Archers is a closer, but the access it gave must be restored (I1) |
| 9 | Dead clauses | Flag value that depends on what the list barely has | Hardened Scales, Pantry, Terrasymbiosis live on Toph's earthbend (slow without her: 3 repeatable sources); Wrenn's mana needs Toph and a non-mana artifact; Springheart's loop needs bestow by CASTING (Chord gives the unattached 1/1 mode); Great Divide Guide's Ally clause a bonus; Annie's doubling has 7 legends. None load-bearing |
| 10 | Copies across the whole collection | Strong free staples not idle | Free and relevant: Solemn Simulacrum (I2), Legion Guildmage (I1), Airbender's Reversal (M3); others weighed: Chromatic Lantern, Mindslaver (2), Rampaging Baloths, Titania, Omnath, Sandbenders' Storm (4), Nutrient Block, Glorious Sunrise, Badgermole (4): each costs 4-7 mana for combat or a second earthbend use, or is weaker than the card it would replace |

**Champion addendum, item by item** (met unless noted): 1 one plan + backup; 2 synergy; 3 redundancy (pingers thin: 3
landfall + Arbaaz); 4 multi-role 41 of 61; 5 commander-centric 3 near-blank; 6 lands; 7 sources; 8 lands + ramp 57; 9
fast mana (Sol Ring, Signet, two Talismans); 10 tapped lands **partly** (4, exception written); 11 window mana
(Provisioner, instants at end step); 12 curve; 13 tax; 14 B4/cEDH compared; 15 engines; **16 not possible** (no scaling
draw in Naya); 17 development first; 18 tutors **partly** (9 access, 10 after I1); 19 cheap answers (8, 6 at MV ≤2, 6
instants); 20 stack tools **partly** (Redirect only; no counterspell owned in Naya, Deflecting Swat is Azula's); 21
one-sided wipe; 22 graveyard hate; 23 protection layers **partly** (exile: 2, M3); 24 win-turn shield 3; 25 answers by
type; 26 compact primary (a board engine); 27 disjoint routes; 28 failure points; 29-31 threat, timing, politics
(written); 32 rebuild; 33 mulligan 92 %; **34 GC slots not possible** (2 owned); 35 efficiency; 36 non-GC power (Solemn
missed, I2); 37 combos; 38 goldfish; 39 gauntlet; 40 cut log (Solemn missing); 41 real-game evidence.

## 6. Lessons checklist (owner lessons L1 to L10)

| # | Covered? | Card / evidence |
|---|---|---|
| L1 one plan | Yes | Landfall drain; army reuses the earthbends |
| L2 ratios from strategy (absurd ramp, repeated entries, no haste) | Yes | Ramp 20 (18 after the fixes, plus Solemn), 25 entry cards, Toph's re-entry engine; ramp after fixes stays at the profile floor, a written trade |
| L3 attacking decks | n/a (backup only) | Coffin as defense; earthbent blockers return |
| L4 dependence | Yes | Enabler, protection 4 |
| L5 card by this deck's curve | Partly | Everflowing Chalice is the L5 example card; I2 removes it |
| L6 proven role-players | Yes | The Earth King, Seismic Tutelage IN; Hardened Scales IN |
| L7 dead clauses | Yes | Named in build section 3 |
| L8 both boards | Yes | Drain for Board 1, removal + Coffin for Board 2 |
| L9 Salt not the measure | Yes | Not measured, not used |
| L10 guide by use | Yes | Build section 2 |

## 7. Questions (a) to (c)

**(a) The builder's "not fixable from the pool" gaps.**
- No counterspell: **true.** No "counter target" card in the Naya pool; the only stack tools are Redirect Lightning (in),
  Deflecting Swat and Return the Favor (Azula's single copies; Swat is a free shield for an attack-engine commander that
  needs it more). Not contested.
- No table-scaling draw: **true.** No Esper Sentinel, Smothering Tithe, monarch or "whenever an opponent" draw in the pool.
- Only 2 of 3 Game Changers: **true** (script over the pool).
- 9 cards on the drain route: **false.** Legion Guildmage is free (I1). Kilo's Reckless Fireweaver is not needed for it.
- Also fixable and missed: draw 9, by Solemn Simulacrum (I2).

**(b) Reckless Fireweaver stays in Kilo: agree.** Here it would be a fifth pinger (artifact tokens included). In Kilo it
is the kill of its loop and one of three burn closers in a Spanish-only pool with fewer options; Kilo already gave up
Arbaaz. Legion Guildmage restores Toph's 10th access card at zero cost to any deck.

**(c) Bracket review items: none breaks a Bracket 3 rule.**
- Bumi + Ashaya: a two-card infinite of combats, 10 MV across two 5-drops, needs Bumi to connect every combat (trample).
  Reachable on turn 5 or 6 only with two ramp pieces and both cards drawn (about 1 to 2 % of games by 13 cards), never
  tutored for early: not an intentional early two-card combo. Allowed.
- Toph + The Stasis Coffin: protection from everything for its controller until his next turn, {2} a turn. It prevents
  damage and targeting of the player only: no opponent loses turns, lands or the ability to play. Not a lock in the
  bracket sense. Allowed.
- Toph + Hardheaded Teacher + Gruul Turf + Goblin Bombardment (with a 0-cost artifact: Zuran Orb or Mishra's Bauble):
  infinite damage, four cards with the commander, late. Allowed. Same for loops A (3 cards) and C (3 cards).

## 8. Verdict: FIX

Ranked change list (both free English copies, English binder; no copy claimed from another deck):

| Rank | Out | In (language, source) | Reason | Expected impact |
|---|---|---|---|---|
| 1 | Explore | **Legion Guildmage** (EN, English binder) | Restores the 10th access card to the drain route (R18); 3 damage to each opponent per {5}{R}; a tapper; Explore is the weakest ramp | Access 76 % to 80 % by turn 7; flood turns into 5 damage to every opponent a turn with Archers; ramp 20 to 19 |
| 2 | Everflowing Chalice | **Solemn Simulacrum** (EN, English binder) | Draw that nets a card, ramp, two entries and an Arbaaz ping; the best earthbend target with Ragost, Zuran Orb or Bombardment; owner's original card | Draw 9 to 10 (gate warning cleared); one more repeatable kill-and-card engine; ramp 19 to 18 timed plus a turn-4 ramp |
| 3 | (plan file and notes) | | M1 counts; M2 Inscription reason; M4 Coffin failure points; Solemn and Guildmage tags (`Solemn: ["draw","ramp"]`, `Legion Guildmage: "payoff"`, both in the burst route and both reference boards) | Honest file; gate unchanged |

If the lead prefers to hold ramp at 20 (owner lesson L2), fix 1 alone is still worth taking, and Solemn should then take
Hardened Scales' slot only with the owner's OK.

**Real power (1-10).** As built: 7.5-7.6 (builder 7.65; the drain still starts late in about a quarter of games and the
deck has no stack defense against a non-targeting combo). With fixes: about +0.1, central 7.6-7.7. Confidence
medium-low: no game played.

**Knowledge gaps.** No web source was read by the reviewer this step (EDHREC figures for Solemn come from the 2026-10-31
study); no simulation of Toph's cast odds after fix 2; rules points R4, R5, R10 of the build remain unruled (Oracle text
only); no Reddit or Moxfield primer read.
