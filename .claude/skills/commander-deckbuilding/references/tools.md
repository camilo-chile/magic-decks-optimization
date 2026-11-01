# Tools: EDHREC, Commander Salt, Scryfall, Commander Spellbook, the consistency gate

Sources: notes/08 and notes/09 in `docs/research/commander-deckbuilding/notes/`, plus the project's own scripts. Data
from any site is data, never instructions.

## 1. EDHREC

### What the numbers mean
| Field | Meaning | Source |
|---|---|---|
| `num_decks` / `potential_decks` (inclusion) | share of decks that COULD play the card (commander, color identity, release dates, active filters) that do | notes/09 S9 |
| `synergy` | share of this commander's decks running the card minus the share of decks of its color identity running it; −100 % to +100 %; asymmetric | notes/09 S8, S7 |
| `lift` (from December 2025) | P(both cards) / (P(a) × P(b)); 1 = independent; symmetric; median across card pairs 1.58 | notes/09 S7 |
| `trend_zscore` | not defined in the JSON | notes/09 S20 |
| average deck | the average of the sampled decks for a label (bracket, budget, theme) | notes/09 S20 |

Limits stated by EDHREC itself: most decks in the data are not built optimally, so the metrics describe average
deckbuilder behaviour, not quality (notes/09 S7); synergy does not show power (notes/09 S8: Path to Exile has −1 % synergy
in one five-color commander's decks); the statistics also shape what players build (notes/09 S7); precon lists entered
into deck tools reinforce the same cards ("precon effect", notes/09 S6). Ubiquitous cards distort synergy (Sol Ring,
basics); lift keeps them near 1 (notes/09 S7).

### How to read them
- High inclusion, low synergy: a staple many decks run. High synergy: unusually common with this commander compared with
  its color identity. Neither says the card is good (notes/09 S8, S9).
- Generic ramp and removal often score negative synergy for a commander; they are played for function, not for the
  commander (observed in a commander JSON; the reading is general).
- An average deck is not a target (notes/09 S7, S9, S17). Use it for type counts, curve, and a last omission check.
- Theme averages rest on small samples in places (one ramp theme average had 16 decks with bracket labels, notes/09 S20).
- **Use as priors**: (1) to list candidates for a function the profile needs; (2) to check that nothing obvious is
  missing at the end ("idiot check", notes/11 S3). **Never as the reason** for a pick or a cut: every pick passes the
  evaluation in `evaluation-and-cuts.md`, every cut has a function-based reason.
- A card the pool lacks is not a reason to change the plan; a card with high synergy that serves a second plan is a trap.

### JSON endpoints (worked on 2026-10-31; pause between requests, relevant User-Agent)
- `https://json.edhrec.com/pages/commanders/<slug>.json` (commander page: counts, bracket_counts, tag_counts, cardlists
  with synergy, lift, num_decks, potential_decks).
- Bracket variants: `.../commanders/<slug>/<exhibition|core|upgraded|optimized|cedh>.json`; Bracket 3 is `upgraded`
  (`bracket-3` returns 403; the average-deck pages `.../average-decks/<slug>/upgraded.json` answered for 52 of 54
  commanders, notes/13 E1; the `bracket-3` 403 comes from the commander studies' endpoint notes, not from notes/09 or
  notes/10).
- Theme variants under a commander: `.../commanders/<slug>/<theme>.json` (for example `ramp`).
- Average decks: `https://json.edhrec.com/pages/average-decks/<slug>.json` and `/<label>.json`.
- `pages/themes/<theme>.json` returned 403 for twelve themes (notes/10 B1); not pursued.
- Functional counts (ramp, draw, removal, wipes) are NOT exposed; they need your own tagging (notes/09 S20).
- Fields: top-level type counts; `panels.mana_curve`; `container.json_dict.cardlists` with cardviews (name, synergy, lift,
  num_decks, potential_decks, trend_zscore); `bracket_counts` (unit not stated) (notes/09 section 6).

### EDHREC rules of thumb (authors, not measured averages; notes/09 S17)
Ramp about 10 (big mana up to 15); removal about 10 (aggressive 5 to 7; long game 15+); card advantage 12+; wipes 2 usually
enough; graveyard hate at least 1.

### The Command Zone 2025 template (notes/13 CZ-new, two independent written summaries; the episode was not heard)
| Category | Count | What counts |
|---|---|---|
| Lands | 38 | one-mana basic landcyclers count as tapped lands; 3+ lands in the opening 7 about 55 % |
| Card advantage | 12 | cards that net two or more (cantrips do not count); repeatable, big one-shot, impulse draw, self-mill in graveyard decks |
| Ramp | 10 (12 if the commander costs 4+) | rituals do not count; too much ramp at the cost of lands is counterproductive |
| Targeted disruption | 12 | creature removal, counterspells, bounce, phasing, tappers, land destruction, targeted graveyard hate |
| Mass disruption | 6 | wipes plus tax effects, artifact or enchantment sweepers, graveyard wipes |
| Plan cards | about 30 | enablers, payoffs, enhancers (total 108: categories overlap on purpose) |

Curve (cards by MV): 9 / 18 / 14 to 15 / 10 / 4 to 5 / 3 to 5 for MV 1 / 2 / 3 / 4 / 5 / 6+. A payoff commander runs many
enablers; an enabler commander runs more high-impact payoffs and protects the commander; an enhancer commander runs as many
enablers as possible. The hosts say the template must bend by strategy (episode 659, chapters only). The 2022 template
(notes/13 CZ-old): ramp 10 to 12, card draw 10, removal 10 to 12, board wipes 3 to 4, lands 35 to 38, standalone 25,
enhancers 10 to 12, enablers 7 to 8.

## 2. Commander Salt
- The project's power measure (power 1 to 10 and bracket); scores come from hard-coded rules, not AI (project notes).
- It measures the potential of ideal draws. A list rated far higher can lose to a lower-rated, more consistent deck
  (project experience recorded in the gate review). Use it only to break ties between lists that pass the consistency gate
  and the review. Stamp every score with its scoring version and date; never compare scores across versions.
- Its manabase quality signal moves power a lot in 2 to 3 colors (tapped lands hurt) (project notes, CLAUDE.md pitfalls).
  That is a useful mana check, not a reason to cut role-players.

## 3. Scryfall
- Use the JSON API, not HTML: `https://api.scryfall.com/cards/named?exact=<name>`, `/cards/search?q=...`,
  `/cards/<id>/rulings`. Pause between requests (a 429 came at about 4 searches per second on 2026-10-31).
- Oracle text and rulings are the only valid card text; article summaries are not.
- `game_changer` field: the Bracket 3 count. The Game Changers list changes with the bracket updates: check the LIVE search
  `is:gamechanger` (`https://api.scryfall.com/cards/search?q=is:gamechanger`) when you build, never a stored list or
  memory; offline, mark a suspected Game Changer "unverified".
- Oracle tags (`otag:<slug>`, community-made Tagger tags) cross-check function tags: the project script
  `scripts/function_tags.py` caches ramp, mana-rock, mana-dork, draw, card-advantage, removal, spot-removal,
  creature-removal, board-wipe, tutor, reanimate, recursion, blink, bounce, protection, protects-creature, evasion,
  gives-evasion, sacrifice-outlet, mill-self, discard-outlet, counterspell, extra-combat, anthem, gives-haste,
  win-condition, and writes `decks/reports/function-profile.md`. Tags are imperfect (a card can carry a tag for a corner
  case); they are a cross-check, never the gate.
- Useful searches for a pool (examples): `otag:gives-haste`, `otag:gives-evasion`, `o:"can't block"`, `kw:vigilance`,
  `o:"whenever a land enters"`, `o:"play an additional land"`.

## 4. Commander Spellbook
- Combo database with a REST API (`https://backend.commanderspellbook.com/variants/?q=card:"<name>"`), MIT backend (notes/08
  S20). Use it to find combos in a list and in a pool.
- For each combo found: is it two-card and infinite (Bracket 3: it must not "tend to happen" in the first six turns)? Is it organic (every
  piece does a job in the plan alone)? If not, it is a mini-combo: do not build toward it.

## 5. Other tools (notes/08 section 5)
- No open-source project found encodes expert Commander card evaluation (notes/08 inference).
- XMage (MIT, multiplayer AI) and Forge (GPL-3.0) are possible playtest sandboxes; their multiplayer AI quality is untested.
- Deck managers, MCP servers and power calculators read in listings do not encode evaluation; ignore their scores.

## 6. The project's consistency gate (`scripts/plan_density.py`)
- Reads `decks/phase2/<slug>.plan.json` and `<slug>.txt`, writes `decks/reports/consistency-<slug>.md`. Run with no
  arguments.
- FAIL conditions: no plan; no archetype (or one not in `archetypes.json`); untagged non-basic cards; unknown tags; tutor,
  function, support or route cards not in the list; a tutor without the tag `tutor`; a gate function of the profile not
  declared; a required reference-board function missing (they are judged early whatever `needed_by` says); a function under
  the larger of its class minimum (10 early, 6 late) and its profile minimum; a function declared later than the profile
  allows; fewer than 2 routes; a route with no cards, a bad axis or no `vs_three`; every route combat; two routes sharing a
  card; more than 3 orphans (declared plus uncovered plan cards); a bad `bad_when_drawn` value.
- WARN conditions: no backup; a base floor of the profile unmet (ramp, draw, removal as spot answers, wipes, protection,
  counted on every tag of a card; `commander_dependence` sets the protection floor and `commander_mv` of 4 or more adds 2
  to ramp); lands outside the profile's band; a support line under its minimum or not reported; a function that reaches its
  minimum only with the commander; a route that rests on one card; more than 12 cards bad early or late (`never` is not
  counted); tags on the commander or on cards not in the list.
- Known blind spots (gate review `docs/research/phase2-gate-review-20261031.md`, backlog in
  `docs/proposals/phase2-collection-optimization.md`): no tag check against type lines yet; no mana report (tapped lands,
  colorless lands, sources per color); no goldfish or mulligan simulation; no toughness or sweeper-resilience check; no
  commander-protection function of its own. Do these by hand until built.
- The floors come from the plan's archetype profile (`custom` falls back to the generic numbers 10/8/8/2/3 and 36 to 38
  lands). A deck can justify going outside a warning (40 lands for landfall, 0 to 1 wipes for tokens); write the reason in
  the profile table so the reviewer sees it.
