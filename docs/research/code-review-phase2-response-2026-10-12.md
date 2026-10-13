Model ID: claude-sonnet-5-5

# Response to the Phase 2 code review (2026-10-12)

Review: `code-review-phase2-2026-10-12.md` (Haiku 5.5, high): 26 findings (5 blocking, 8
should fix, 13 minor). Every blocking finding was re-checked before fixing. After the fixes all
five test files pass (49 tests: layer_a 31, speed_risk 8, spellbook bulk 3, rulings 2, research 5).

| Id | Verdict | What changed |
|---|---|---|
| F-01 | Fixed | The extra-turn regex accepts "two/three/four/five/N extra turns" (Time Stretch, Teferi); test added |
| F-02 | Fixed | `speed_risk.py` skips a card-facts file without `quantity`, `role`, `power`, `keywords`, `oracle_id`, `mana_value` and says to rerun `layer_a.py`; test added |
| F-03 | Fixed | Land ramp, draw and tutor effects now apply to permanents (enters-the-battlefield effects), not only spells; test shows the frequency rises |
| F-04 | Fixed | A template variant with a winning, infinite, mass land denial, lock or control feature is listed as `review: template unresolved (...)`; counted in `review_items` |
| F-05 | Fixed | Any variant that uses the commander is a floor-4 candidate (`commander combo`), as the commander-effects row says |
| F-06 | Fixed | `eligible_bracket_3` renamed `floor_ok_so_far`; the report adds `review_items`, and the printout lists the pending checks. `complete` stays false until every check runs |
| F-07 | Fixed | Mass land denial patterns tightened (graveyard returns and "sacrifice X lands" as a cost are no longer matches) and widened (destroy all Plains, "Islands don't untap", "destroy all creatures and lands", "each player sacrifices four lands"); still heuristic and over-inclusive |
| F-08 | Fixed | Snow-covered basics are basics (`Basic` and `Land` in the type line) |
| F-09 | Fixed | "up to three/four/... cards named" accepts the number words two to ten |
| F-10 | Partly | A variant whose Spellbook tag implies a higher floor than the predicates is listed with a `tag_note` and counted for review; the floor itself is not changed (the tag stays a cross-check, as the spec says) |
| F-11 | Partly | An extra-turn card that returns itself to the library or hand gets a review note ("chain candidate"). Real chain detection stays a manual check; no list of chains exists in the data |
| F-12 | Fixed | The two-card speed threshold is 8 (no accuracy flag in the bulk file); documented in power-scale v0.7 |
| F-13 | Closed 2026-10-12 | Measured on 108,039 variants: `manaValueNeeded` is the mana beyond the pieces (median ratio to the pieces' total mana value 0.0; it is below that total in 98.8% of variants). The simulator's `max(needed, uncast)` is therefore right for pieces already in play and for spells cast as part of the combo. Layer A's "early" test now also counts the cards' own mana values. Older note: `manaValueNeeded` is not documented by Spellbook in the files read. The simulation uses the larger of that value and the cost of the pieces still to cast. If the value already includes the pieces' own cost, combos in hand wait for mana they do not need, which is slower; the effect on the bands is small and not measured |
| F-14 | Not applicable | The run takes seconds (4,000 games in 0.2 s), well under the 5-minute rule; it prints progress and ETA anyway |
| F-15 | Kept | The hazard needs both a copy piece and a payoff because without a payoff the loop does nothing; the reason text says so |
| F-16 | Fixed | A foil marker on a line without a set is accepted; test added |
| F-17 | Fixed | The commander must be a legendary creature, Vehicle or Spacecraft, or say "can be your commander" |
| F-18 | Fixed | Haste is read only from the card's own keyword line or keyword list; a `*` power still counts as 0 (documented in the model limits) |
| F-19 | Documented | The band edges fall in the higher band (10% is `low`); this is the conservative reading of the spec |
| F-20, F-21 | Kept | Conservative (a missing mana value counts as fast; quantities of a piece are ignored); not present in the current data |
| F-22 | Kept | No duplicate face names observed in the bulk file |
| F-23, F-26 | Kept | Descriptive statistics only |
| F-24 | Kept | Peak memory of about 1 GB while slimming the Spellbook file; works on the owner's machine |
| F-25 | Fixed | `read_csv` keeps only rows of binder type `deck` |

Test gaps closed: plural extra turns, chain note, snow basics and numbered limits, template review,
commander plus two cards, tag cross-check, mass land denial false positives and misses, foil marker
without a set, non-creature commander, ETB ramp, stale card-facts guard.

Still open: the E-1 cases Gonti's Aether Heart, Caged Sun and Azula + Snap + Dualcaster Mage are
checked by hand in the probes but not as tests; `validate_deck_export.py` has no tests.
