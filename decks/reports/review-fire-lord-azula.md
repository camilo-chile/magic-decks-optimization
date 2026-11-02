# Adversarial review: fire-lord-azula (Phase 2, round 2 list, 2026-11-02)

Reviewer: Opus 5.5 high. Inputs: `decks/phase2/fire-lord-azula.txt`, Oracle text from `data/model/phase2/pool-fire-lord-azula.json`
(the commander text and rulings were read live from the Scryfall API on 2026-11-02, because the pool file has no commander entry),
then `fire-lord-azula.plan.json`, `fire-lord-azula.build.md`, `decks/reports/consistency-fire-lord-azula.md`,
`decks/phase2/owner-decisions.md` (all three rounds; binding), `data/model/phase2/assignment.json` (final), `decks/phase2.json`.
Scripts run by the reviewer: `python scripts/check_phase2_bracket.py decks/phase2/fire-lord-azula.txt` (PASS) and
`python scripts/plan_density.py` (PASS, 2 warnings); live Scryfall `is:gamechanger` search (53 cards, none in the list).
Odds: hypergeometric, 99-card library, cards seen by turn N = 7 + N, no mulligan (`references/probability.md`).

## 1. Independent reading (written before opening the plan file and the notes)

**Commander.** Fire Lord Azula {1}{U}{B}{R}, 4/4. Firebending 2 ({R}{R} on attack, kept through every combat step). Whenever you
cast a spell while she is attacking, copy it. Rulings (2025-10-02) checked: the copy is not cast (Electro's {R} and
Thermo-Alchemist's untap see only the original; magecraft says "cast or copy", so Archmage Emeritus and Storm-Kiln Artist trigger
twice); X and paid kickers are copied; additional costs are not paid for the copy (copied Big Score and Thrill draw without a
discard); the trigger resolves even if the original is countered; firebending is not a mana ability.
- Window: declare attackers to end of combat; only instants and flash cards can be cast there. A BLOCKED Azula still copies: blocks
  cost her body and her damage, not the engine.
- Dependence: attack engine. She acts only by attacking (the spell trigger needs her attacking) and costs 4, so the haste
  promotion test says haste should be a gate function.
- Archetype: spellslinger (primary) + combat_attackers (secondary). Plan: Azula attacks from turn 5, casts one to three instants
  with {R}{R} plus open lands, each copied; closes with copied X burn, extra combats and Ozai.
- Dies to: spot removal while tapped out, sweepers (her own wipes spare her, theirs do not), blocks by bigger creatures, the
  crack-back, and any "spells only at sorcery speed" effect (shuts the window entirely).

**My recount from Oracle text (one verb per function).**
| Function | My count | Cards |
|---|---|---|
| Window-castable spells (instants + flash) | 31 | 27 instants + Amphibian Downpour, Dualcaster Mage, Hidden Footblade, Torrential Gearhulk |
| Net draw, weighted | about 9 | Full: Archmage Emeritus, Black Market Connections, Fact or Fiction, Pull from Tomorrow, Gleam of Death. 0.75: Azula, On the Hunt (Clue costs {2}, she must attack as a 4/3). Half: Big Score, Thrill of Possibility (net 0 alone, +2 copied), Frostcliff Siege (Jeskai, exclusive with Temur), Dimir Locket (late). Copied cantrips at half: Fists of Flame, Blazing Crescendo, Cunning Maneuver (Expedite, Mind Stone, Soul-Guide Lantern replace themselves) |
| Ramp castable by turn 3 | 8 + 3 reducers | Sol Ring, Arcane Signet, Dimir Signet, Izzet Signet, Mind Stone, Dimir Locket, Bender's Waterskin, Black Market Connections; reducers Goblin Electromancer, Stormcatch Mentor, Nightscape Familiar. Glamdring reduces only once equipped to Azula (turn 5+) |
| Spot removal | 10 + 2 counters | Abrade, Amphibian Downpour, Chaos Warp, Go for the Throat, Hero's Downfall, Imprisoned in the Moon, Lightning Strike, Snap, Terminate, The Last Agni Kai; Negate, Narset's Reversal. X burn (Comet Storm, Electrodominance) doubles as removal |
| Wipes | 2 | Day of Black Sun, Ritual of Soot (Ritual kills 7 of the deck's 13 creatures: Thermo-Alchemist, Electro, Dualcaster, Electromancer, Stormcatch, Nightscape, Loyal Inventor) |
| Commander protection | 8 | Swiftfoot Boots, Champion's Helm, Octopus Form (hexproof); Deflecting Swat, Redirect Lightning, Narset's Reversal (redirect or return); Negate (counter); Undying Malice (death return) |
| Haste for Azula | 4.5 | Swiftfoot Boots, Haunted Cloak, Hidden Footblade, Frostcliff Siege (Temur), Expedite (one-shot, half). Equipment stays after she dies, so it is repeatable |
| Defense while tapped | about 4.5 | Propaganda, Haunted Cloak (vigilance), Loyal Inventor (2/3 vigilance), Thermo-Alchemist (0/3 defender), Octopus Form (one-shot untap, half) |
| Window-mana keepers | 4 | Horizon Stone, Electro, Ozai, The Last Agni Kai |
| Graveyard hate | 1 (to buy) | Soul-Guide Lantern |
| Answers to commanders | 3 | Imprisoned in the Moon, Amphibian Downpour, Chaos Warp |

**Mana.** 36 lands (17 basics: 7 Island, 5 Mountain, 5 Swamp). Land sources: blue 19, black 18, red 17. Four filter lands
(Darkwater Catacombs and Shadowblood Ridge make nothing alone; Cascade Bluffs and Sunken Ruins make {C} alone), Rogue's Passage
colorless, Exotic Orchard depends on the opponents. Nine lands enter tapped under a condition, none always tapped. Pips: red 33,
blue 21, black 14. Curve (X at 0): MV1 7, MV2 27, MV3 16, MV4 8, MV5 2, MV6 3; average 2.68.

**Three tests.**
- A wipe: Azula dies (recast 6, equipment left on the table gives haste for {1}); Undying Malice and Negate are the only answers;
  the rest of the board is small, so little is lost.
- Eight chump blockers: the copies still happen; damage needs trample (Fists of Flame, Haunted Cloak, Frostcliff Temur, Ozai),
  Rogue's Passage, Day of Black Sun X=0, Ritual of Soot, burn (Comet Storm copied) and Thermo pings.
- Two bigger creatures: a 4/4 Azula dies in a block unless a copied trick or copied removal is cast after blocks; about 16
  cards do that for {R}{R} plus 0 to 2 lands.

## 2. Differences with the builder

| Item | Builder | Reviewer | Effect |
|---|---|---|---|
| Draw | 12 by tag (consistency report "draw 12"); profile text admits "about 9 weighted alone" | About 9 weighted; 12 only because Fists of Flame, Blazing Crescendo and Cunning Maneuver carry the PRIMARY tag `draw` while the notes put them in the deck for "make blocks bad" | B1 |
| Ramp by turn 3 | 12 (incl. Glamdring) | 11 (8 + 3 reducers); Glamdring needs Azula out and {2} equip | Minor (still above 10) |
| Spot removal tag | 11 primary (Soul-Guide Lantern tagged `removal`) | 10; Lantern is graveyard hate, not spot removal | Minor |
| window_mana (declared) | 10 pieces, one function | Two verbs merged: keepers (4: Horizon Stone, Electro, Ozai, Last Agni Kai) and "more window mana" (Fire Nation Palace, Azula OtH, Storm-Kiln, Big Score, Frantic Search, Snap) | I3 |
| Defense while tapped | 6 | 4.5 (Bender's Waterskin is ramp; Octopus Form one-shot) | Minor (still at min 4) |
| Frostcliff Siege | Counted in draw, combat_draw, haste, team_evasion, through_wide_board | Exclusive modes: one or the other per game | Minor |
| Haste | Support line by "fit fallback" | The builder's own fit check leaves 7 free slots, so the fallback's condition (no fit) is not met; the true reason is that the pool has no more haste givers (only steal effects) | Minor (reason mislabeled, choice sound) |
| Route 2 claim | "copied Unleash Fury on an unblocked Azula is 21 commander damage" | 4 x 2 x 2 = 16; 21+ needs power 6 first (Champion's Helm: 24) | Minor |
| Godo + Helm floor | "earliest realistic turn 7 (turn 6 only with Sol Ring and two more rocks)" | Theoretical floor is turn 4 (Sol Ring turn 1, a Signet turn 2, Godo turn 3, equip {5} turn 4); about 5 % of games by turn 6 | Owner check, section 4 |
| Command Tower language | "Azula keeps the English copy" | Assignment gives Azula the Spanish EOC copy (Toph has the English one) | Minor, text only |
| Toughness, curve, sources, density 31, protection 8 | Same | Same | None |

## 3. Findings

### BLOCKING

**B1. Card draw is under the spellslinger minimum, and the plan file hides it by tagging three combat tricks as primary draw.**
- Failure: the deck the owner says "empties her hand fastest and needs the most draw" (L2) runs about 9 weighted draw pieces against
  the profile's min 12 and target 18. The gate reads "draw 12" only because Fists of Flame, Blazing Crescendo and Cunning Maneuver
  are tagged `draw` first; each replaces itself (a cantrip, an impulse card, a Clue) and nets a card only when Azula copies it
  (weight 0.5, `archetypes.json` meta.weights). The notes themselves place them in "make blocks bad". Tag by the job (SKILL 14).
- Evidence (card flow, turns 5 to 8): Azula's turn spends 2 window spells plus a land; the natural draw gives 1; the repeatable
  engines are two cards (Archmage Emeritus, Black Market Connections), seen by turn 6 in 25 % of games and by turn 8 in 28 %.
  Without them the hand loses about one card a turn and is empty around turn 7 to 8, which matches the owner's complaint. Round 2
  removed four real or half draw pieces (Insight Engine, Thirst for Knowledge, Lion Vulture, Abandon Attachments) and replaced them
  with tricks. 9 pieces give 70 % to see one by turn 5; 12 give 81 %.
- Fix [J]: retag the three tricks (primary `payoff` or `engine`, `draw` second), and add real draw from free owned cards, cutting
  the softest slots. Candidates, best first:
  - **Zuko, Exiled Prince** ({3}{R} 4/3, free, English): firebending 3 plus "{3}: exile the top card, you may play it this turn".
    A bridge card (SKILL step 9): it turns the window mana that empties at end of combat into cards, and the card it exposes is
    cast in the window and copied. It was in the owner's original list and is "left out" in the notes with no reason.
  - **Malcolm, the Eyes** ({U}{R} 2/2 flying haste, original list): a Clue on the second spell cast each turn, which Azula's turns
    meet; also a flier for Board 1.
  - **Waterbending Lesson** (sorcery, draw 3, discard unless waterbend {2}; 4 free copies) or **Abandon Attachments** (instant,
    copied rummage; the round-2 cut).
  - Soft slots that keep every function at or above its min: Expedite (haste 4.5 to 4, min 4), Nightscape Familiar (reducers 4 to
    3, min 2), Redirect Lightning (protection 8 to 7, min 6), The Last Agni Kai (removal 10 to 9, min 8; its copy makes Azula
    fight twice and can kill her).

### IMPORTANT

**I1. The non-combat route leans on one card: Comet Storm.**
- Failure: route 1 lists Comet Storm, Electrodominance and Thermo-Alchemist, but only Comet Storm reaches all three opponents.
  Electrodominance copied hits at most two players for X each; Thermo-Alchemist pings 1 per untap (chip damage against 120 life).
  The recursion does not help: Torrential Gearhulk and Electrodominance cast spells "without paying their mana cost", so a
  recast Comet Storm or Pull from Tomorrow has X = 0 (rules: X is 0 when cast without paying the cost; not in the notes, and the
  guide line for Gearhulk should say "never on an X spell").
- Evidence: access pieces Comet Storm + Mystical Teachings = 30 % by turn 9, 36 % by turn 13; adding Electrodominance as a weak
  stand-in, 41 % and 50 %. The gate's late class asks 75 % by 20 cards.
- Fix [J]: **Solve the Equation** (owned, free, Spanish; bilingual deck) back in. It was cut as "sorcery outside the window", but
  a tutor is cast in the main phase precisely to fetch the window card (Comet Storm, Electrodominance, Unleash Fury, Overpowering
  Attack). Four access pieces: 51 % by turn 9, 60 % by turn 13. It also adds a tutor, a Salt driver (I4).

**I2. Commander Salt is likely to drop against the Phase 1 list (8.4), and nobody has measured it.**
- Evidence: against the Phase 1 list he plays (`decks/scanned/fire-lord-azula.txt`) 17 cards changed. Out: three tutors
  (Solve the Equation, Reckless Handling, Lo and Li) plus Entomb, four one-mana cantrips (Brainstorm by owner decision, Ponder,
  Opt, Consider), Mana Leak, three cheap removal spells (Fatal Push, Heartless Act, Ultimate Price), Banefire, Goblin
  Bombardment, Aether Gale. In: role-players and tricks (Thermo-Alchemist, Expedite, Blazing Crescendo, Cunning Maneuver, Fists of
  Flame, Unleash Fury, Hidden Footblade, Haunted Cloak, Horizon Stone, Propaganda, Dimir Locket, Azula OtH, Pull, Thrill,
  Overpowering Attack, Lantern). Tutor density and cheap interaction are what Salt rewards; the notes call the net "neutral to
  slightly up" without a measurement. The owner said a significant drop forces a new round.
- Fix: measure the list on Salt before shipping (exact printings). Swaps that should raise Salt and keep or improve consistency
  [J]: Solve the Equation for Expedite (I1); Fatal Push ({B} instant; revolt is easy here: Clues and Treasures from Big Score,
  BMC, Storm-Kiln, Cunning Maneuver, Azula OtH, Mind Stone) for The Last Agni Kai; Zuko and Malcolm for B1. None takes a function
  under its min.

**I3. `window_mana` merges two jobs to reach 10.**
- Failure: the plan text says "Horizon Stone, Electro and Ozai keep the leftover window mana"; the cards that KEEP it are 4
  (Horizon Stone, Electro, Ozai, The Last Agni Kai), below the late class of 6. The other six add mana in the window, a different
  verb (SKILL 3.4: no merged vague function to reach a count).
- Fix: split it: `window_mana_keepers` (4) as a support line reported short, `window_mana` (more mana) as written. If The Last
  Agni Kai goes (B1/I2), keepers drop to 3; Zuko (B1) is a converter, not a keeper, and covers the same waste. Not blocking: the
  window spells are paid in the window, so keepers are a bonus, not the plan.

**I4. Godo + Helm of the Host: verified late, but it does not close against Board 2 by itself.** (The owner's acceptance stands;
this is the arithmetic he asked for.)
- Cost: Godo {5}{R} puts Helm onto the battlefield; equip {5} at sorcery speed; 11 mana over at least two main phases. Floor:
  Sol Ring turn 1, a 2-mana rock turn 2, Godo turn 3 (6 mana), equip turn 4 (7 mana): unlimited combats on turn 4. Frequency:
  Sol Ring in the opening seven 7.1 %, Godo seen by turn 3/4/5 10 % / 11 % / 12 %; Godo is not tutorable (Mystical Teachings
  finds instants and flash only). By turn 6 about 5 % of games (judgment from those odds); typical turn 7 to 9. Spellbook gives
  no mana figure (`mana_value_needed` 0); the script classes it "two-card combo, late" (floor 3). It is not an early two-card
  infinite in the sense of the rule (it does not "tend to happen" by turn 6). Correct the notes' floor (turn 4, not 6).
- Closing: each combat attacks with only two Godo tokens (3/3; a token untaps only on its first attack), so one opponent with two
  untapped bigger creatures blocks forever. It wins when Azula has Haunted Cloak (vigilance: she attacks every combat, firebending
  every combat) and a keeper (Horizon Stone, Ozai, Electro) turns that into unbounded mana for Comet Storm or Electro's
  leave trigger: a 4 to 5 card late line. The notes say "it does not win by itself": honest; keep that wording in the guide.

### MINOR

- **M1. Haste reason mislabeled.** Promotion test says promote (attack-only, MV 4). The fallback the notes cite applies when the
  line does not fit; the fit check shows 92 of 99. The real reason is pool scarcity (no further haste givers except steal
  effects). Rewrite the reason; the choice (support 4.5, protection at target 8) is sound.
- **M2. Route 2 arithmetic.** "Copied Unleash Fury ... 21 commander damage" is 16 from a 4/4; 24 with Champion's Helm. Also a
  blocked Azula without trample deals none of it to the player: pair it with Fists of Flame, Haunted Cloak or Rogue's Passage.
- **M3. Day of Black Sun against Board 2** is listed in `through_big_creatures`, but X at the blocker's mana value (usually 4+)
  also kills Azula (MV 4). Count it only against Board 1 (X = 0 kills every non-copy token for {B}{B}).
- **M4. Own wipes kill the backup.** Ritual of Soot kills Thermo-Alchemist (route 1), Electro (keeper), Dualcaster and the three
  reducers. Use it only when those are absent or as a reset; say so in the guide.
- **M5. Dead clause not named:** Loyal Inventor puts the artifact in hand only with an Assassin (only BMC's changeling token
  qualifies), so it is a tutor to the top of the library (a skipped draw). The tutor entry is still valid.
- **M6. Red sources.** Red has the most pips (33) and the fewest land sources (17 + Arcane Signet, Izzet Signet, Waterskin,
  partial: about 19). Single red pips on turns 2 to 3 (Thermo, Stormcatch, Electromancer, Footblade) want 19 (Karsten 1C); Electro
  {1}{R}{R} on turn 3 wants 28 and lands about 55 % of the time. Firebending pays red only in the window. Consider one Island to
  Mountain (blue 19 to 18, red 17 to 18) [J].
- **M7. Soul-Guide Lantern in the list while not owned.** It is the owner's planned purchase (binding), but the `.txt` holds the
  card while the notes say "fallback Run Amok until it arrives": the assignment gives 0 copies and the pull list leaves the slot
  empty, so the physical deck has 99 cards. Put Run Amok in the pull list (or the `.txt`) until the Lantern is scanned. Run Amok
  (+3/+3 and trample on an attacker, copied +6/+6) is also the best owned answer to the blocking problem in the pool.
- **M8. Purchase proposals 2 to 4 have no live reading.** Talisman of Dominance's only reading is a 12,840 CLP foil, above the
  5,000 CLP envelope shared by Toph, Azula and Ezio; Swan Song has no Game of Magic Singles reading; Arcane Denial's reading
  (2,840 CLP) is from 2026-10-17. They are proposals, not in the list; the lead verifies stock before any order.
- **M9. Tag inflation, minor:** Soul-Guide Lantern tagged `removal`; Bender's Waterskin counted as defense while tapped; Frostcliff
  Siege counted in five lines with exclusive modes; Glamdring counted as turn-3 ramp. No function falls under its min after the
  correction (removal 10, defense 4.5, ramp 11).
- **M10. Answers against closers.** Answers 14 (10 spot, 2 counters, 2 wipes); the 16 "closers" include engines (Archmage,
  Storm-Kiln, Dualcaster, Gearhulk, Narset's Reversal). Damage-dealing closers are about 10 (Azula, Comet Storm,
  Electrodominance, Thermo, Ozai, Unleash Fury, Godo, Helm, Overpowering Attack, Azula OtH). Acceptable because the removal is
  also window fuel, but B1's swaps should not add more answers.

## 4. Owner decisions checked (binding; not findings)

| Decision | Check | Result |
|---|---|---|
| Godo + Helm accepted if it stays late | Arithmetic in I4: 11 mana over two main phases; floor turn 4 with Sol Ring + rock; about 5 % by turn 6; not tutorable; script: late | Holds. Notes understate the floor; fix the wording |
| Overpowering Attack loan accepted | `decks/phase2.json` Azula `borrowed` (loan_class evaluate, in_stock false), `restock.md` row, only in Azula; assignment pick "loan from the Standard decks" | Holds. Freerunning {2}{R} needs Azula to connect; against the blocker it costs {3}{R}{R} in main phase 2, when firebending mana is gone unless a keeper holds it |
| Blocks must be punished | About 16 cards beat a blocker after blocks for {R}{R} plus 0 to 2 lands: Fists of Flame (trample), Blazing Crescendo, Cunning Maneuver, Unleash Fury, Octopus Form, Hidden Footblade (first strike), Abrade, Lightning Strike, The Last Agni Kai, Terminate, Go for the Throat, Hero's Downfall, Snap, Chaos Warp, Amphibian Downpour, Electrodominance, Comet Storm; static: Champion's Helm (6/6), Haunted Cloak (trample), Rogue's Passage. 16 pieces: 90 % to have seen one by turn 5, 71 % two by turn 7 | Covered. The weak point is B1: each punisher is spent, and an empty hand removes the threat the "in between" opponent fears |
| Lion Vulture felt slow | Out, reason written (cut log round 2) | Holds; Coastal Piracy also out with a sound reason (it needs connection) |
| Soul-Guide Lantern planned purchase | In the list; 0 copies assigned | Holds; see M7 for the fallback in the pull list |

## 5. Multiplayer check

- **How it beats three opponents:** mainly one at a time. Commander damage (Azula 4, copied pump to 16 to 24) removes one player per
  turn that she connects; Comet Storm copied is the only table-wide burst (2X to each); Overpowering Attack and Godo add windows;
  Helm on Azula multiplies copies. The table-wide finish is thin (I1).
- **Pod interaction (Bracket 3 medians, turn 8: about 2.3 spot removal, 0.9 wipes, 0.45 counters seen across the table):** spot
  removal on Azula is covered by 8 protection pieces (3 hexproof, 3 redirect or return, 1 counter, 1 death return) and by
  equipment that gives the recast haste; a wipe costs Azula and the small creatures (Negate and Undying Malice only); graveyard hate
  barely matters (Gearhulk, Teachings flashback, Gleam). Attack taxes (Propaganda effects) eat the firebending mana.
- **Single cards that end the plan:** a "cast spells only at sorcery speed" or "no spells during combat" permanent (Teferi or
  Grand Abolisher style) shuts the window completely; answers: Chaos Warp, Abrade (if an artifact), Imprisoned in the Moon (if a
  creature), Negate before it resolves. A pacifism on Azula: Snap or Chaos Warp on her own Azula resets it. A second answer exists
  for each.

## 6. Lessons checklist

| Lesson | Status | Evidence |
|---|---|---|
| L1 one plan | Covered | Spell-copy window plan; equipment package (6 + Godo + Loyal Inventor) all serves Azula |
| L2 ratios follow the plan (Azula: most draw) | **Not covered** | B1: about 9 weighted draw against min 12, target 18 |
| L3 attackers connect, live, haste, defend | Covered, thin | Haste 4.5, protection 8, defense 4.5, trample and Rogue's Passage, ~16 block punishers |
| L4 dependence | Covered | Attack engine, protection at target 8 |
| L5 card judged in context | Mostly | Glamdring counted as turn-3 ramp (M9); Dimir Locket justified on turn 3 |
| L6 proven role-players | Covered for Horizon Stone and Propaganda | Original-list cards (Zuko, Exiled Prince; Malcolm; Run Amok; Fire Nation Attacks; Firebender Ascension; others) are "left out" in one line with no per-card reason; Zuko is a bridge card (B1) |
| L7 dead clauses, mini-combos | Mostly | Listed; Loyal Inventor's Assassin clause missing (M5); Godo + Helm accepted by the owner, Godo also works alone (extra combat, equipment onto the battlefield, Hidden Footblade gives him haste) |
| L8 two reference boards | Covered | Board 1: wipes X=0, trample, burn; Board 2: copied removal and tricks (M3 on Day of Black Sun) |
| L9 Salt is not the measure | Covered, but unmeasured | I2: measure before shipping, as the second objective |
| L10 guide says how to use | Covered | Two corrections: Gearhulk never on X spells (I1); Unleash Fury arithmetic (M2) |

## 7. Rules checklist

| Rule | Result |
|---|---|
| Pool and copies | 99 of 100 assigned (`assignment.json` problems: none); Soul-Guide Lantern 0 given (planned purchase, M7) |
| Language (bilingual: English when owned in both) | Spanish picks only where the English copies are used elsewhere or not owned (Command Tower, Exotic Orchard, Helm of the Host, Mind Stone, Negate, Narset's Reversal, Nightscape Familiar, Pull from Tomorrow, Thrill, Gearhulk, Choked Estuary, Darkwater Catacombs, Sulfurous Springs); assignment final |
| Loans | Only Overpowering Attack (evaluate, accepted by the owner), in Azula only; no automatic loans; Propaganda and Hidden Footblade come from free English copies, not the loan copies |
| Owed cards | Smoldering Marsh: Azula plays the English LTC copy; the owed Spanish MSC copy goes to Ezio; counted once |
| Purchases | Lantern (owner decision); proposals 2 to 4 unverified and Talisman above the envelope as priced (M8); none of them in the list except the Lantern |
| Scarce copies | Named in notes section 7 (Swan Song, Insight Engine, Thirst to Kilo; Pull and Footblade to Azula; Command Tower; Propaganda) |
| Bracket 3 | PASS: 0 Game Changers (live search 2026-11-02, 53 cards), no mass land denial, no extra turns, one combo (Godo + Helm) classed late and verified (I4); no reversible cards (Glamdring is an Adventure) |

## 8. Verdict: FIX

Blocking item:
1. **B1**: raise real draw to the spellslinger floor (about 12 weighted) with owned cards (Zuko, Exiled Prince; Malcolm, the Eyes;
   Waterbending Lesson or Abandon Attachments) from the soft slots named, and retag Fists of Flame, Blazing Crescendo and Cunning
   Maneuver by their job.

To do in the same round (not blocking): I1 Solve the Equation back; I2 Salt measurement before shipping (with the Salt-raising
swaps listed); I3 split `window_mana`; fix the notes' Godo floor (I4), Unleash Fury arithmetic (M2), Gearhulk X note (I1) and the
Run Amok fallback in the pull list (M7). The plan itself is right: Azula's window, 31 window spells, 8 protection pieces and about
16 block punishers make a coherent deck; it runs out of cards before it runs out of plan.
