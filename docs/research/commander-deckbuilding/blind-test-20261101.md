# Blind test of the commander-deckbuilding skill (2026-11-01)

Question: does a reviewer that has ONLY the skill (no CLAUDE.md, no lessons, no names of the owner's cards) find the defects
the owner saw in play? Setup: an agent defined in `.claude/agents/blind-deck-reviewer.md` (Opus 5.5 high, `omitClaudeMd`,
skill preloaded) read five lists under neutral names (two versions each of the Toph and Azula decks, the original and the
Phase 1 one, and the Phase 1 Ezio list) plus the Oracle data of their cards. Round 1 used skill revision 2; the audit of
the same day had found seven soft leaks (pattern texts close to the owner's cards), so round 2 ran after the leaks were
rewritten and the audit's blocking items were fixed. Outputs were kept in the session scratchpad (`blind-test/out-v1`,
`out-v2`); this note keeps the scorecard.

## Scorecard against the owner's lessons

| Lesson | Round 1 | Round 2 |
|---|---|---|
| L1 one plan, no mini-combos | Found (kill that needs three conditions at once; pieces that work only with one card) | Found |
| L2 ratios follow the plan (landfall ramp and re-entries; instants and draw) | Found: 0 extra land drops, 36 lands for an average value of 3.37, draw 8 against 12 | Found, plus the land-recursion engines recognized as plan pieces |
| L3 attackers: haste, team evasion, protection, defense while tapped | Found for both attacking decks | Found; the attack-tax card removed in Phase 1 was recommended back by the reviewer |
| L4 protection follows the commander's dependence | Found (3 against 6 for the attacker) | Found (4.5 against 6) |
| L5 a card's value depends on the curve (the scaling rock) | Missed (counted as ordinary ramp) | Found for the attacking deck ("colorless, does not help the five colors"), kept as an artifact entry in the artifacts deck, which is the owner's own reading |
| L6 proven role-players cut by a score | Partial | Partial, by design: the attack tax was recovered; the window-mana keeper and the counter doubler were still cut candidates |
| L7 dead clauses | Found (vehicle clause, equipment clause, copy card waiting for its partner) | Found |
| L8 the two reference boards | Found | Found |
| L9 Salt is not the measure | Not tested | Not tested |

## What the reviewer did not find, and why
The window-mana keeper: the skill says to judge it by the mana it saves per turn, and the arithmetic (5 mana to save about
two a turn from turn 6) is defensible; only the owner's games say it won. The counter doubler: seen as a one-card package.
These are exactly the cases the rule "proven role-players are strong priors, named by the caller" exists for (CLAUDE.md,
Phase 2 block, and the deck-builder and deck-reviewer agents). The skill cannot know a card won games; revision 3 adds the
rule "the only keeper": a cut needs a replacement that does the same job, and the owner's report outranks the per-turn
arithmetic.

## Fixes made from round 2 (all general)
- Haste: a fit fallback when the promoted line cannot fit (haste 4 to 6 plus commander protection at target), and a clearer
  meaning of "acts without attacking".
- Attack or connect: read the trigger; an engine that triggers on attacking is not stopped by blockers.
- Commander-conditional pieces: a graded weight, 0.5 + 0.5 x min(1, protection pieces / protection min), plus a discount
  for pieces cast before the commander is usually out.
- Re-entry engines (a sacrifice outlet with a land that returns), a mana permanent that is also fuel, window mana with its
  own duration, copies that skip additional costs, the closer count for attackers, and the scope of review proposals.

## Limits of this test
Five lists and one reviewer; the lists are the owner's own, so the rules cannot be tuned against a third deck. The leaks
found by the audit may have helped round 1 on the ramp and draw findings; round 2 is the cleaner reading. No rulings were
available offline, so rules points were marked "not checked" (a Game Changer snapshot is a possible addition). The last
check is play: the owner's games with the Phase 2 lists.
