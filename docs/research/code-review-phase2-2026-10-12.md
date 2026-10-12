Model ID: claude-haiku-5-5

# Independent code review: Phase 2 (Layer A, speed-risk, Spellbook bulk, collectors)

Date: 2026-10-12. Scope: the files listed in the review brief, as found in the working tree
(uncommitted edits in `scripts/layer_a.py`, `scripts/validate_deck_export.py`,
`tests/test_layer_a.py` and docs). Read-only on the project: no network, no script runs, no
writes outside this report, `data/raw/` not read.

Method: code reading; read-only Python imports of `scripts/` with `python -I` against
`data/cache/` (Scryfall oracle bulk 2026-10-11, Spellbook slim file with 114,400 variants,
Spellbook raw bulk 2026-10-12). Probe scripts: scratchpad `review-phase2\probe*.py`.
Offline tests: all five files pass (31 tests: layer_a 15, speed_risk 6, spellbook bulk 3,
rulings 2, research 5).

## Findings

Severity: **blocking** = the gate can say eligible when the spec says no, or the speed input is
wrong; **should fix** = spec divergence or false reject; **minor** = robustness or wording.

| id | severity | file:line | what is wrong | evidence or repro | reproduced |
|---|---|---|---|---|---|
| F-01 | blocking | `scripts/layer_a.py:56-57`, `:410` | Extra-turn grant regex needs `takes? (an/another)? (extra/additional) turn`. Plural counts ("two extra turns") are missed, so the policy reject for 2+ cards is bypassed. Commander-legal oracle text with this miss: Time Stretch ("Target player takes two extra turns after this one.") and Teferi, Master of Time (-10). A scan of all commander-legal oracle text found no other miss. | Fire Lord Azula + Time Stretch + Time Warp + 49 Island + 48 Mountain: `rejected=False`, `floor=2`, `extra_turn_cards=['Time Warp']`. Teferi + Time Warp: same. Fix: accept counted plurals (`two/three/\d+/an/another`) and add tests. | yes |
| F-02 | blocking | `decks/toph-the-first-metalbender.cards.json` (written by `layer_a.py`); read by `scripts/speed_risk.py:128-133`, `:305-314` | The on-disk card-facts file predates the `quantity`, `role`, `power` and `keywords` fields (83 entries; keys: color_identity, mana_cost, mana_value, name, oracle_id, oracle_text, type_line). `build_deck` then finds no commander (library of 83 instead of 99; commander `None`) and reads all powers as 0. `main()` does not check the keys, so the speed flag would be computed silently on the wrong deck. | `build_deck(load(file))` returns library 83, commander `None`. Fix: regenerate with the current `layer_a.py`; `speed_risk.main()` must refuse files without `quantity`/`role`/`power`. | yes |
| F-03 | blocking | `scripts/speed_risk.py:214`, `:241-262` | ETB ramp and ETB tutor on creatures and artifacts are never applied: ramp and tutor only run in the spell branch (`if card["spell"]`, L241-255). Worse, any card with ramp text gets rank 0 (L214), so an ETB-ramp creature is cast before the commander (rank 3, L229), delaying the threat. The error is lean-slow, so the speed flag can understate risk and pass a deck the review should fail. | 5,000 games, seed 1, commander 21 power at cost 5, 40 Forest + 59 two-drop creatures. With ETB-ramp text: frequency 0.037 (cumulative by turn 6). Same creatures without the text: 0.633. Ramp sorcery in the same deck: 0.859. Only the text differs. | yes |
| F-04 | blocking | `scripts/layer_a.py:254-257`, `:288` | Template variants are kept only if they have infinite-turn, control-all or MLD features. Any other template variant (two cards with "Win the game", "Infinite damage", etc.) gets floor 1, `kind=None`, and is dropped from rows, flags and the report. Spec (E-1: "template-only variants as review") requires review. | Synthetic two-card template variant with "Win the game": `{'floor': 1, 'kind': None}`. Bulk: 1,216 two-card template variants have no review kind, e.g. Shalai and Hallar + Leonardo, Cutting Edge (tag S, "Infinite damage", requires "Card That Gives Lifelink") is invisible. For the three commanders only E-tagged template variants are affected (147 for Toph). Fix: every included template variant with a decisive, infinite, MLD, lock or control feature goes to `rows` as review. | yes |
| F-05 | blocking | `scripts/layer_a.py:252-266` | Spec: any combo that uses the commander is a floor-4 candidate (review). Commander plus two other cards gets floor 3 when slow, with no kind and no review note. Only commander plus one card is floored at 4. | `judge_variant` on a synthetic commander + 2 cards, MV 9, "Infinite creature ETB": `floor 3, kind 'two-card combo'`. Bulk: no commander + 2 variant of the three commanders is floor 3 today (all are 4), so no current list is affected. | yes |
| F-06 | should fix | `scripts/layer_a.py:476-477` (printed at `:563`) | `eligible_bracket_3 = not reasons and floor <= 3` ignores pending checks (Spellbook, hazards, speed) and review rows. A clean deck with no Spellbook file reports `eligible_bracket_3: True` while `complete: False`. The name reads as a go signal. | Clean 100-card deck, `spellbook=None`: `eligible True, complete False`. Fix: rename to `layer_a_floor_ok`, or set false while pending or review items exist. | yes |
| F-07 | should fix | `scripts/layer_a.py:49-55`, `:423-430` | Card-text MLD heuristic over-matches: "return all land cards from your graveyard" (Splendid Reclamation); "sacrifice X lands" as a cost (Copper-Leaf Angel, Gaea's Balance, Nahiri's Lithoforming). All get floor 4 (false reject). Under-matches: "Destroy all Plains" (Stench of Evil), "Islands don't untap..." (Choke), "Destroy all creatures and lands" (Devastation; caught only by the name list in `hazards.json`), "sacrifices two lands" (only by name). | `analyze` with Azula and each card: floor 4 for the four over-matches. `mld_reason` is `None` for Choke and Stench of Evil. | yes |
| F-08 | should fix | `scripts/layer_a.py:140` | Snow-covered basics have type "Basic Snow Land", which does not contain "Basic Land", so they get singleton limit 1. Legal in Commander: false reject. | 49 Snow-Covered Island: `singleton violated`. | yes |
| F-09 | should fix | `scripts/layer_a.py:142-146` | "up to three cards named" (and any number word other than seven or nine) defaults to limit 1. Affects Squadron Hawk, Nesting Wurm, Skyshroud Sentinel and Howling Wolf in the bulk. False reject. | Azula + 2 Squadron Hawk: `singleton violated`. | yes |
| F-10 | should fix | `scripts/layer_a.py:284-287`, `:313` | Spec: Spellbook tag is a cross-check (R = 4, S = 3 or 4 review, P = 3, O = 2 or 3, C = 2). The code only counts tags; no disagreement is listed. Examples: 226 R-tagged three-card variants at floor 1 (e.g. The Locust God + Liliana, Dreadhorde General + Yahenni: "Infinite card draw"); 99 R-tagged template variants at floor 1; 1 R-tagged two-card variant at floor 3. | Counts from the bulk file (probe11, probe12). | yes |
| F-11 | should fix | `scripts/layer_a.py:405-420` | Spec row "any chain ... floor 4" is not implemented. Only Spellbook infinite-turn features are floored. No chain detection for recursive extra-turn cards (e.g. Nexus of Fate, which returns to the library). | By reading; no test. | gap, by reading |
| F-12 | should fix | `scripts/layer_a.py:168`, `:262` | v0.7 says speed is "about 6 mana or less, or up to 8 when Spellbook's accuracy flag is false". The raw Spellbook variant has no accuracy field (checked the keys), so only the 6 threshold runs. Two-card non-template variants with MV 7-8: 174 at floor 3, 22 at floor 4. Decide: treat MV 7-8 as floor 4 until the flag exists. No current impact on the three commanders. | Counts from `judge_variant` over the slim file. | yes |
| F-13 | should fix (suspected) | `scripts/speed_risk.py:183-184` | `combo_ready` requires `mana >= max(manaValueNeeded, uncast)`. If `manaValueNeeded` is the total mana value of all pieces, a combo whose pieces are already in play still waits for that mana (slower than the docstring's "leans fast"). Depends on Spellbook's definition. | By reading; not run. | suspected |
| F-14 | minor | `scripts/speed_risk.py:315-318` | CLAUDE.md requires a separate progress log file for any script estimated over 5 minutes. `speed_risk` prints progress with ETA but writes no log. The run time (3 decks x 20,000 games) was not timed. | By reading. | yes (by reading) |
| F-15 | minor | `data/hazards.json:343-362` | `azula-self-copy-loop` needs a copy spell AND a magecraft payoff. Its reason text describes an unbounded copy loop that the copy piece alone enables; the conjunction may under-flag. | By reading of the reason text vs the rule. | suspected |
| F-16 | minor | `scripts/layer_a.py:41-43` | A line with a foil marker but no set ("1 Sol Ring *F*") is read as the name "Sol Ring *F*": STOP, false reject. Lines with a set and `*F*` parse correctly. | `parse_decklist` output. | yes |
| F-17 | minor | `scripts/layer_a.py:375-379` | The commander check accepts any "Legendary" type line, including non-creature legendary artifacts or lands that cannot be commanders. | By reading. | suspected |
| F-18 | minor | `scripts/speed_risk.py:78`, `:82` | `"haste" in text` also matches other creatures' text ("has haste"); a `*` power counts as 0 (undercount). | By reading. | suspected |
| F-19 | minor | `scripts/speed_risk.py:56-61` | Band edges: exactly 10%, 20%, 30%, 40% fall in the higher band. Spec says "0-10%". Ambiguous; state the rule in the report. | By reading. | yes (by reading) |
| F-20 | minor | `scripts/layer_a.py:262` | `mana_value_needed or 0` treats a missing value as fast (conservative). Not present in the current bulk. | By reading. | yes (by reading) |
| F-21 | minor | `scripts/layer_a.py:205`, `:241` | Spellbook `uses.quantity` is ignored (oracle IDs are a set). A combo needing two copies of one non-basic is treated as present. Over-inclusive, so conservative. | By reading. | yes (by reading) |
| F-22 | minor | `scripts/layer_a.py:80-83` | `build_index` keeps the first card for a duplicate face name (`setdefault`); two DFC faces with the same name would resolve to one card silently. | By reading. | suspected |
| F-23 | minor | `scripts/layer_a.py:444`, `:472` | The `"Land" not in type_line` test also matches MDFC "Sorcery // Land" cards in the descriptive averages. Descriptive only. | By reading. | suspected |
| F-24 | minor | `scripts/collect_spellbook_bulk.py:112-113` | `read_bulk` loads the whole ~700 MB text before streaming objects. Works, but peak memory is high. | By reading. | yes (by reading) |
| F-25 | minor | `scripts/validate_deck_export.py:83-85` | `read_csv` does not check binder type when the deck name matches (the condition is always true when a deck name is given), so a binder and a deck of the same name can merge. | By reading. | suspected |
| F-26 | minor | `scripts/layer_a.py:60` | `TUTOR_RE` drops any sentence containing "land", so "search your library for a land or creature card" is not a tutor. Descriptive only. | By reading. | suspected |

## Test gaps

- Plural extra-turn counts (Time Stretch, Teferi); Azula plus two extra-turn cards is rejected
  (E-1 item, no test); Nexus of Fate.
- Snow-covered basics in the singleton check; "up to three cards named".
- Template-only two-card variant without infinite features (review); commander plus two slow
  cards (floor-4 review); Spellbook R-tag versus floor disagreement.
- MLD false positives (Splendid Reclamation, Copper-Leaf Angel) and misses (Choke, Stench of
  Evil); "sacrifices two lands" without a name hit.
- E-1 cases missing from the test file: Gonti's Aether Heart, Caged Sun, The Stasis Coffin,
  Alexios gives no commander flag, Azula + Snap + Dualcaster Mage. All pass when checked by
  hand in the probes, so the gap is only in the tests.
- `speed_risk`: no test for ETB ramp, the rank order (commander versus ramp creatures), the
  mulligan rule, tutors on permanents, a combo whose pieces are already in play, or the guard
  against a stale card-facts file. No fixed-seed regression against a stored value.
- `validate_deck_export.py` has no tests (foil marker, text versus CSV mismatch, Scryfall
  mismatch). `fetch_spellbook` 400 and 429 paths are untested.
- No test that a review row or flag keeps the gate from reporting an eligible result.

## Checked and found correct

- Name resolution: apostrophe normalization, face names, full names win over faces (tested).
  All hazard names resolve in the index (probe: none missing).
- Game Changer floors 0 / 1-3 / 4+, the commander counted.
- Extra-turn exclusions: skip or forbid text (Stranglehold, Gerrard's Hourglass Pendant) is not
  counted; Medomai, Ugin's Nexus, Final Fortune, Time Warp are counted.
- Two-card predicate: commander not counted; commander plus one card floor 4; `must_be_commander`
  enforced; the 1,525 B-tagged variants are all `commander_legal: False` and are skipped.
- Toph one-card combos are floor 4: Mindslaver, The Stasis Coffin, Gonti's Aether Heart,
  Caged Sun. Toph's real report flags Mindslaver and The Stasis Coffin (commander plus one) and
  Bumi, Unleashed + Ashaya (fast two-card). Alexios: no commander flag, as the spec says.
- Hazard semantics: one name per group, conjunction across groups (Thoracle pairs, classic
  two-card infinites); review-only hazards never change the floor.
- `play_game`: lands and rocks count once per turn; creatures cast this turn cannot attack
  without haste; a tapped ramp land gives no mana on its entry turn; commander cost is
  `cmc + 2 x casts`; turns and the inner loop are bounded (6 turns, guard 30); each game copies
  the library, `field` entries are per game, no dict is mutated; the mulligan bottom card is
  inserted at index 0, which is the bottom of a list popped from the end.
- `collect_spellbook_bulk.slim_variant` keys match the raw variant keys; `read_bulk` streams
  objects correctly for gzip and plain JSON.
- `collect_rulings` and `collect_research_data`: no defect that affects the gate; `for ... else`
  in `fetch_spellbook` follows the intended path.

## Could not check

- Speed flag on the real Toph list: `data/raw/` is off limits and `decks/*.cards.json` has no
  quantities. Full 20,000-trial runs not done (2,000 to 5,000 trials in memory only).
- Rules text beyond the oracle bulk: rulings and the Wizards snapshot not re-checked.
- Spellbook's definition of `manaValueNeeded` (no API docs read; network off). Drives F-13.
- `validate_deck_export.py` online mode and the `collect_*` network paths (read only).

Overall: ACCEPT WITH FIXES - do not use the gate for eligibility until F-01 to F-05 are fixed and re-run (F-01 lets a policy-reject list pass; F-02 and F-03 make the speed input wrong or lenient; F-04 and F-05 are review-channel gaps with no current impact on the three commanders' bulk data).
