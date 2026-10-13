# Power measurement (v1.0)

Status: v1.0, 2026-10-13. Replaces the project's own `X.Y` scale, the Layer B judge panel and
the speed-risk flag (archived in `research/archive-power-scale-v0.8.2-2026-10-12.md`). Rules
snapshot: the Wizards update of 2026-02-09 (Brackets still "beta"), re-checked on 2026-10-13
against Wizards' own pages: no Commander, Brackets or Game Changers change; re-check at the
2026-11-30 Banned and Restricted announcement and in the Phase 11 freshness check. Source reports:
[commander-brackets-rules-snapshot](research/commander-brackets-rules-snapshot.md) and
[commandersalt-adoption](proposals/commandersalt-adoption.md).

## What measures a deck
| Question | Measured by | Where |
|---|---|---|
| Does the list break an official condition of its target bracket? | **Layer A** (offline, ours): legality, 100 cards, singleton, color identity, Game Changers, mass land denial, extra turns, early two-card infinite combos | `scripts/layer_a.py` |
| How strong is it? | **Commander Salt power**, 1 to 10, and its decimal bracket | commandersalt.com, read by hand |
| How good are its parts? | Commander Salt pillars (consistency, efficiency, interaction, win conditions), synergy, combos, mana base, salt, upgrade suggestions | commandersalt.com |

### Commander Salt power bands (from the site's `/powerlevels`)
| Band | Power |
|---|---|
| Casual | 1 - 4.99 |
| Upgraded casual | 5 - 6.49 |
| Mid power | 6.5 - 7.59 |
| High power | 7.6 - 8.99 |
| Fringe cEDH and cEDH | 9 and above |

Reference deck to beat: the owner's friend's Krenko, Mob Boss deck, **power 6.1**, bracket 3*, salt
78.3. Community averages (2026-10-13): Alexios 5.4 (1,553 decks), Toph 6.8 (4,001), Azula 7.8 (5,298).

## Rules of use
- Commander Salt has no documented API, MCP or terms page. It is used by hand in the browser, one
  deck at a time, with the owner's authorization (2026-10-13). No scripting, no bulk requests.
- A deck enters by a link to a deck hosted on Moxfield, Archidekt, ManaBox, Scryfall or another
  listed site; plain text is not accepted.
- Every score is stamped with the site's scoring version (changelog, latest 2026.4195 of
  2026-09-29) and the date. Scores can move with new releases: compare only inside one version.
- Scores are transcribed to `decks/reports/<commander-slug>-<UTC date>.md` (power, bracket, salt,
  pillars, flagged anti-patterns, suggestions, version).

## Limits
- **Power first (user decision, 2026-10-12).** The decks are for casual games with friends and
  the goal is the strongest, most consistent list the chosen budget buys. The only limits are
  Wizards' official conditions of each deck's **target bracket** and Commander legality. A rule
  that is only this project's own, and that lowers power, is not allowed. All three decks target
  Bracket 3 (`TARGET_BRACKET` in `scripts/layer_a.py` supports another target per deck).
- Intent cannot be computed. Layer A only produces a minimum bracket (floor) plus flags. Bracket 5
  is only ever declared by the user.
- Every price is in CLP from the 7 specialist stores in `data/stores.md`; never marketplaces or
  private sellers; no currency conversion. A card's cost is `unknown` before the catalogs are
  read, never an estimate.

## Layer A: deterministic gate (floor and flags)
Rules snapshot (as of 2026-02-09, beta):

| Bracket | Game Changers | Mass land denial | Extra turns | Two-card infinite combos | Tutors |
|---|---|---|---|---|---|
| 1 Exhibition | 0 | none (intentional) | none (intentional) | none (intentional) | no limit |
| 2 Core | 0 | none (intentional) | low quantities, not chained | none (intentional) | no limit |
| 3 Upgraded | up to 3 | none | low quantities, not chained | none that are intentional and early | no limit |
| 4 Optimized | unlimited | allowed | allowed | allowed | no limit |
| 5 cEDH | unlimited | allowed | allowed | allowed | no limit |

Tutors lost their restriction on 2025-10-21; Wizards relies on the Game Changers list to catch the
most efficient ones, but not every efficient tutor is on it (Demonic Consultation is not).

**Spellbook data source.** Combos are matched **locally** against Commander Spellbook's published
bulk file (`variants.json.gz`, fetched by `scripts/collect_spellbook_bulk.py`; its API
documentation asks clients not to export the dataset through the API). The bulk file has
`bracketTag`, produced features, `manaNeeded` / `manaValueNeeded` and the card list. Variants with
template requirements ("any creature with persist") cannot be resolved offline and are listed for
review. Spellbook's own tag is a cross-check. Combos Spellbook does not list are covered by the
curated hazard list `data/hazards.json`, built from the Phase 3 reports.

Provenance: **official** = Wizards defines it and it is enumerable; **curated** = needs a list
maintained by someone else; **heuristic** = a proxy; **policy** = a choice of this project;
**control** = an integrity check of the pipeline itself.

| Rule | Method | Provenance | Floor / flag |
|---|---|---|---|
| Legality, 100 cards, singleton, color identity | Scryfall data | official | invalid -> reject |
| Game Changers (the commander counts) | Scryfall `game_changer` | official | 0 -> no constraint; 1-3 -> floor 3; 4+ -> floor 4 |
| Mass land denial | Spellbook feature, Wizards' definition ("four or more lands per player"), curated names | curated | any card or combo -> floor 4 |
| Lock, skipped turns, control of opponents | Spellbook features | curated | review note only (Wizards' text names none of them) |
| Extra turns, per card | Scryfall oracle text | curated | 1 card -> floor 2 |
| Extra turns, count | count of flagged cards; a card multiplied by the commander (Azula) counts as 1 with a review note (user decision, 2026-10-12) | curated | Wizards: "low quantities, not chained or looped". Read as at most 3 cards (the 4th -> floor 4; 2 and 3 are a note); any chain or infinite-turn combo -> floor 4 |
| Two-card infinite combos | Spellbook variants of 2 cards or fewer (the commander counts as a card) whose features are infinite or win the game; "early" = mana to assemble, the larger of `manaValueNeeded` and the cards' own mana values (`manaValueNeeded` is the mana beyond the pieces: median ratio 0.0 over 108,039 variants) | heuristic | Early (6 or less) -> floor 4. 7 or 8 -> floor 3 plus a note. 9 or more -> floor 3. Finite combos and combos of 3 or more cards set no floor |
| Commander effects | Spellbook combos that contain the commander; commander text that multiplies a flagged card | policy | follows the rows above; extra-combat cards are a note, not a count |
| Name resolution | canonicalize every card to a Scryfall oracle ID | control | recognized cards must equal 100, or stop |

Descriptive statistics (tutor count, average mana value) are reported and never decide a floor.

## Goal and acceptance
Nothing is bought until the user picks a budget from the **budget curve**.
- For each budget point (100,000 to 300,000 CLP in steps of 50,000) the 3 decks are built together
  to reach the highest Commander Salt power they can **at parity**: within 0.2 power points of each
  other, maximizing the lowest. Every deck is above the friend's 6.1 whenever the budget allows.
- The curve plots budget against each deck's power, with the Layer A result and the site's
  suggestions per point.
- A list is eligible only with: Layer A floor at or below its target bracket and no rejection; a
  Commander Salt score of the frozen list (version-stamped); verified stock; and the Phase 11
  freshness check of the rules.
- Calibration (Phase 5): score the reference list and its 5 ablation rungs, check that power falls
  as cards are replaced, and score the same list twice to see the site's repeatability.

## Data sources
| Need | Source |
|---|---|
| Card data, Game Changers | Scryfall oracle-cards bulk file (2 requests/s on live search) |
| Combos | Commander Spellbook bulk file, matched locally |
| Power, bracket, salt, synergy, upgrades, community averages | Commander Salt, by hand |
| Prices and stock | The 7 Chilean stores, read in Phases 7 and 9 |

Use JSON APIs and bulk files, not HTML pages, except Commander Salt (no API exists).

## Changelog
- v1.0 (2026-10-13): owner decision: Commander Salt's power and bracket replace the `X.Y` scale,
  Layer B and the speed flag. Layer A stays. Old text archived.
- v0.8.x (2026-10-12): power first; official conditions only; target bracket per deck; the "early"
  two-card test counts the cards' own mana values (F-13 closed with data).
- Earlier versions: see the archive.
