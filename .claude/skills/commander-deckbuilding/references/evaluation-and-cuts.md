# Card evaluation, dead cards, cuts, testing and diagnosis

Sources: notes in `docs/research/commander-deckbuilding/notes/`, mainly notes/03, notes/08 and notes/11. Expert sources
agree on direction (value is set inside the list) and give almost no numbers. Where this file states a rule with no
source, it is marked [J].

## 1. Judge a card inside this list
- Judge a card by its fit in the specific deck, not by raw power or popularity: synergy, role, replacement candidates,
  mana (does it undercut stronger ramp, does it suit the curve), then playtest (notes/08 S2).
- Each card should push the plan; widely played staples are the most damaging to a theme; fit can outweigh efficiency (a
  token deck chose two on-theme answers over a generic one) (notes/03 S4).
- Prefer cards with several jobs; a single-role card must excel at its one job (notes/03 S5).
- Between two cards with the same job and equal fit, take the cheaper one (mana efficiency), then the one that works in
  more game states [J]; the choice is a tie-break, never a reason to leave out a role-player.
- Keep off-plan answers the deck needs to survive; prefer answers that also advance the plan (notes/03 S4).
- Re-check old staples against today's faster games; high-cost cards with no board impact deserve scrutiny (notes/03 S6).
- A card's value depends on the game stage: a turn-2 ramp card is weak on turn 7 without a draw engine (notes/01 S6).
  Corollary [J]: evaluate each card at the turn THIS deck will usually cast it, with THIS deck's mechanics. The same card
  can be strong in a deck that grows it (proliferate, doublers, recursion) and a wasted turn in a deck that does not.
- Synergy is not power; a card popular in a color identity is not thereby good (notes/09 S8).
- Scan every part of a card (text, cost, types, stats) for hooks the commander or plan references; implicit synergy is
  real (notes/08 S17, low authority).

## 2. Role-players versus staples [J, consistent with notes/03 S4 and notes/08 S2]
A **role-player** is a card that does a job the plan depends on and few other cards in the pool do: it supplies the
commander's specific fuel, removes the commander's specific bottleneck (a mana window, a missing mana ability, an
evasion gap, a timing gap), or is the only piece of its kind.
- Rank it by the job, not by its general rating. If cutting it leaves the job undone or at a count below min, it stays.
- **Proven role-players** (cards the owner or caller says won games with this commander, or that the plan's play history
  shows doing the job) are strong priors. To cut one, write: the job it did, which cards now do that job, the count after
  the cut, and why the replacement is better in THIS deck. The owner reviews it.
- A generic staple with near-zero or negative synergy (generic ramp, generic removal) is fine for its function. It does
  not outrank an on-plan card doing the same function.
- Never use a deck-level power score or an inclusion rate as the reason to cut a role-player. Those measures favor
  generic efficiency and ideal draws (principle 6 in SKILL.md; notes/09 S7 averages describe popular decks).

## 3. Dead clauses, mini-combos, cards bad when drawn
- Cards one step from the commander or plan are usually fine; cards two or more steps away become dead draws because
  their enablers are missing (notes/11 S3).
- Key low-profile synergies off the commander; they work more often than two random cards meeting by chance (notes/11 S8).
- An engine card needs about ten cards that work with it, or many tutors (notes/11 S4, anecdote).
- **Dead clause** [J, from the gate review]: a clause that needs a card type, partner or resource the list barely has
  (for example a clause that rewards a card type, a mechanic or a partner card of which the list holds almost none). It is
  not an orphan if the card has another use; name it and judge the card on its live text only. Either commit (enough
  pieces) or do not count that clause.
- **Mini-combo** [J, project rule]: two cards that only matter together are two dead draws most games. A combo is fine when
  each piece does a useful job alone (organic combo, notes/09 S15).
- **Bad when drawn**: mark each card bad early (expensive or needs a board) or bad late (narrow early answers); a card
  that is never bad is left out of the list, because the gate counts every listed value. Cheap ramp is bad late by design:
  count it as bad late only above the profile's ramp target [J], otherwise every list trips the warning. Over about 12 is
  a warning (gate, judgment). Multiplayer, long games and singleton create dead-card problems; a card can alternate
  between dead and live (notes/08 S15).
- Pet cards: sources disagree (notes/01 conflict 4). In this skill a pet card must pass the same tests as any card.

## 4. Cuts
- Weigh each card against the deck's main goal; when unsure, playtest the extra cards and cut what performs (notes/08 S14).
  A cut-order rule that trims the most-played staples first exists but is unclear in summary (notes/08 S16).
- Group the list by function to expose off-plan cards, surplus and gaps (notes/03 S5).
- **Never cut** without a written, reviewed reason [J]: a piece that takes a function below its min; the only answer to a
  permanent type; a proven role-player; lands below the band.
- **Cut first** [J]: orphans; cards whose only live text is weak after naming a dead clause; cards bad when drawn most of
  the game; surplus in a function above target; generic staples whose job on-plan cards already cover; a second plan's
  cards.
- **Cut log** per cut: card, function(s) it served, count after the cut against min, replacement, reason. A score or an
  inclusion rate alone is never a reason.
- Expensive additions should come with costed swaps that keep the curve low (notes/03 S6).

## 5. Testing
- Solo goldfishing answers narrow questions (turn-two consistency); loose goldfishing misleads (notes/08 S9). Over 80 % of
  players goldfish in some way; about 18 % play two of their decks against each other (notes/11 S11, self-selected poll).
- A d20 table can simulate interaction (wipes, removal, counters) in solo games (notes/11 S11, author's proposal).
- Test solo until the deck works and the pilot is competent, then play people (notes/08 S26, weak source); the first game
  with a new deck is a test, not a plan (notes/11 S9).
- Ten games cannot rank two close lists (5 of 10 wins has a 95 % interval of about 24 % to 76 %, computed in notes/08).
  Log what each card did and when (notes/08 inference).
- Lands-by-turn and "piece by turn N" can be computed without playing (`probability.md`); a script can run London
  mulligan simulations (notes/08 inference; not built in the project yet).
- Record the mulligan rule; keep pod results apart from 1v1 results (notes/08 inference).

## 6. Diagnosing a deck that loses or does nothing
Signs and fixes (notes/03 S6; notes/11 section 5; notes/06 section 7):
| Sign | Likely cause | Fix |
|---|---|---|
| Mulligans of one-land hands | too few lands | add lands, not cut them (notes/03 S6) |
| Empty hand by turn 6 | too little draw for the plan's spend | draw, cheaper fuel (notes/03 S6) |
| Runs dry late | too little action or selection | selection, recursion (notes/03 S6) |
| Hands full of 4+ drops | curve too high | lower curve (notes/03 S6) |
| Key cards uncastable on time | ramp too thin for the curve | ramp (notes/03 S1) |
| Engine cards rot in hand | enablers missing; card two steps from the plan | cut or add enablers (notes/11 S3, S4) |
| Attacks bounce off blockers | evasion that does not fit the table's blockers | team evasion, trample, removal on key blockers (notes/12) |
| Creatures die before attacking | no haste, fragile bodies, no protection | haste, protection, tougher bodies (notes/06 S4, S9) |
| Killed on the crack-back | no defense while tapped | vigilance, deterrent blockers, taxes (notes/12 C1 C2) |
| Opponents survive at low life | single-target finisher | team-wide finisher (notes/05 S3) |
| Many small packages, each rarely assembled | several plans | one plan; cut second plans (notes/03 S5; notes/06 S14) |
| Repeated unexplained losses | the list itself | log games; group by function; trusted review (notes/03 S6) |

A suggested repair order (notes/03 inference): mana counts first; cut second and third plans; add draw or selection where
hands empty; add backups for the key effect and a second finisher.

Losses that cluster in long games can point at the pilot's patience rather than the list (notes/11 S17, opinion).
