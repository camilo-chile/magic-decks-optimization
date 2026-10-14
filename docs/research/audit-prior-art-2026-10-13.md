# Audit: prior art versus own work (2026-10-13)

Independent audit of the whole pipeline for the "rebuilt by hand what already exists" failure mode.
Evidence: repo files read in full (CLAUDE.md, README, power-scale v1.0, rating-protocol v4,
commandersalt-adoption, evals, anchors, the 3 skills, the agent, stores.md, deck reports, script
headers, test counts) and Commander Salt pages read by hand in the owner's Chrome on 2026-10-13,
one page at a time (site scoring version 2026.4195; footer meta date 9.28.2026). Nothing was
imported, refreshed, signed in or submitted. EDHREC, Archidekt and Moxfield were not opened.

## Verdict
1. The biggest remaining rebuild is **the candidate side**: agent-built reference lists, slot
   rankings, fillers, the ablation ladder and a planned "local surrogate" power model. Commander
   Salt already publishes hundreds of real, already-scored lists per commander, per-card inclusion
   rates by bracket or power bin, and deck-aware upgrade and combo picks. Use them as the candidate
   pool and as measured (list, power) points; stop building our own.
2. Keep as gaps (nothing existing does them): Layer A on Wizards' conditions, owned inventory and
   copy allocation, CLP prices and verified stock at the 7 stores, budget/parity optimization
   (with PuLP, not hand-written), dashboard (Artifact).
3. New owner decision needed: Commander Salt's decimal bracket tracks power (CS bracket <= 3.9 tops
   out near power 7.4-7.5 for all three commanders), while Wizards-spec Bracket 3 decks reach
   8.0-8.2 on the site. The repo's "Wizards only" rule and the site's bracket disagree above ~7.5.

## 1. Item-by-item table
Legend: replace = use the existing tool instead; keep = ours is needed and fine; keep-as-gap = no
existing tool covers it; drop = no longer used by any later phase.

| # | Item | What we do today | Existing alternative | Evidence (observed 2026-10-13 unless noted) | Accuracy comparison | Recommendation | Effect on the plan |
|---|---|---|---|---|---|---|---|
| 1 | Power yardstick (Phase 5/6) | Commander Salt by hand (adopted) | same | Deck pages show power, bracket, salt, pillars, drivers | Site is deterministic and versioned; small inconsistencies seen (Toph header 6.5 vs its own field report "6.6"; one Alexios deck 8.6/5.0 on the leaderboard vs 8.0 header and 8.1 rationale on its page) | keep; always transcribe the header value; leaderboard values are not evidence | none |
| 2 | Alexios reference list (Phase 4, `evals/anchors/*reference*`) | Built by a Sonnet builder plus a Haiku reviewer, never scored on the site | Commander page leaderboard of 1,555 scored Alexios decks; Cards tab inclusion rates (Bracket 3 bin: 332 decks) | `/commanders/id/alexios_deimos_of_kosmos`: decks sorted by power; deck `f4b8cc3a...` ("[Bracket 3] ...") power 8.0, WotC spec 3, same 3 Game Changers as our reference (Ancient Tomb, Jeska's Will, The One Ring) | Real lists are measured; ours is judgment ("Ranking is judgment, not data", reference-notes (h)12). Ours encodes rules traps the site does not model (control swaps, pro-red) | replace as the source; keep our list only as ONE more candidate, scored once | Phase 4 becomes "candidate menu from the site" |
| 3 | Slot ranking and fillers (`slot-ranking.json`, 486 lines) | Agent judgment | Per-card power contribution on any deck page (Cards and Power Level tabs), inclusion % per bin | Deck `9354c58f...` Cards tab: 89 unique cards, each with "Power" and "Synergy" numbers; Power Level tab shows per-card deltas (e.g. "Expedition Map +2.8") | Site numbers are computed in context; ours are opinion | drop | retire file (keep only if a test needs it) |
| 4 | Ablation ladder (`build_ablation_ladder.py`, 5 rungs, 5 tests) | Synthetic weaker lists to test the site's monotonicity | Leaderboard already gives a dense measured spread (Toph CS bracket <= 3.9 page: powers 7.4 down to 6.7 in 50 rows) | as left | Monotonic response to removing the best cards is not in doubt for a scorer used on 1.9 M decks; the ladder answers no decision | drop (never run; saves 5 hostings plus 5 imports) | Phase 5 shrinks |
| 5 | Phase 5 calibration as designed | Score reference plus 5 rungs, score one list twice | none needed beyond repeatability | Field-report vs header mismatch (row 1) | The only open accuracy question is repeatability and version drift | keep only: score one list twice on different days; stamp versions | Phase 5 = 1-2 imports |
| 6 | "Local surrogate calibrated on site scores" (rating-protocol.md:18, adoption.md:79) | Planned custom model predicting power of unscored lists | Measured lists from leaderboards plus site scoring of the ~15 final lists | as left | A surrogate trained on a few points would be our own power scale again (the exact failure mode) | drop; optimize over measured candidate lists instead (section 4) | Phase 8 simpler, no model |
| 7 | Upgrade candidates (build-deck step 2 "Candidates by role") | Claude proposes by role | Deck page Upgrades tab, Meta mode: most-played missing cards from real decks of the commander, by bracket or power bin, with % and USD price; Combos source with "In your deck / Missing" | Toph deck Upgrades, Meta, Staples, Bracket 3 bin: "1.652 DECKS", "100 of 1921 picks" (Sol Ring 90%, Arcane Signet 80%, Chromatic Lantern 61%...). Combos source: "100 of 497 picks" | Community frequency at the right bin beats agent recall; but picks are not bracket-safe (see row 8) and prices are USD | replace (candidate pool = site picks); keep Layer A on top | build-deck step 2 rewritten |
| 8 | Layer A (`layer_a.py`, 35 + 6 tests) | Offline gate on Wizards' conditions | Site's WotC criteria checklist; Spellbook `POST /estimate-bracket` | Upgrades Combos at Bracket 3 bin suggests "infinite-turns" Gonti's Aether Heart + Toph (5%) and Mycosynth Lattice + Vandalblast "opponents-locked". Alexios deck `f4b8cc3a...`: site says WotC spec 3 with "Two-card infinite combos: Present - upgraded tier 2" (Aggravated Assault + Neheb, Blasphemous Act + Repercussion); our reference-notes (e) treat Aggravated Assault + Sword-style lines as early, floor 4. Spellbook schema lists `/estimate-bracket` (GET/POST) | Site checklist is more lenient than Layer A on two-card combos and is per-link only; Layer A runs in a loop offline | keep (essential); show the site checklist as a cross-check only | none |
| 9 | Game Changer list | Scryfall `game_changer` from bulk | same (official flag) | Local bulk `oracle-cards-20261011210156`: 38,721 cards, 53 with `game_changer` true (read-only count) | Official | keep | none |
| 10 | Combo detection | Spellbook bulk matched locally plus `data/hazards.json` | Spellbook `find-my-combos`; site Combos tab | Schema read (WebFetch, spot check) | Same data; bulk is the documented way | keep | none |
| 11 | Phase 3 synergy reports (3 x ~550 lines plus verifications) | Agent research | Site Synergy, Combos, Cards by role, Archetypes | Commander and deck tabs exist (Synergy/Archetypes tabs not opened) | Site covers synergy; our reports add rules readings (control changes, lifelink on Alexios, pro-red) that no tool gives | keep as archived inputs; no new research | none |
| 12 | Rules check, rulings collector | Scryfall rulings bulk plus CR text | none better | — | Official texts | keep (done) | none |
| 13 | Collection scanning | ManaBox (free) | — | done in Phase 1 | Existing tool already | keep | none |
| 14 | Inventory and copy allocation (`build_inventory.py`) | Own script | ManaBox shows the collection but not cross-deck allocation | — | Gap | keep-as-gap | none |
| 15 | Deck export validator | Own script | — | done | Gap (Spanish printings) | keep | none |
| 16 | `collect_research_data.py` pools | Scryfall pools per commander for builder agents | Site picks | — | Pools only fed agents | keep bulk download (Layer A needs it); pool files no longer used | minor |
| 17 | Rules freshness (E-2, planned script) | Planned | Re-download Scryfall bulk; GC count and banned flags already in it | row 9 | Same data | merge into a Layer A run (print bulk date, GC count 53, diff names) | E-2 script not needed |
| 18 | CLP prices (Phase 7) | Planned manual or scripted reading of 7 stores | marketplace.scry.cl (Chilean aggregator in CLP, stores plus players); tcgmatch.cl | Web search only (domain not named by the owner, not opened): snippets say Scry gathers singles stock from Chilean stores and players, CLP prices, Webpay plus 2% fee. Whether it lists the 7 stores is unknown | Marketplaces are barred for purchase; as a price index it is unverified, coverage and terms unknown | keep-as-gap; owner may look at Scry by hand to see if his stores appear; never evidence | O1 widened |
| 19 | Store reading method | `stock-verifier` reads rendered pages | Store platforms' own JSON (stores 4, 6, 7 use `/collections/` URLs, typical of Shopify; store 3 uses `/product-category/`, typical of WooCommerce) | URL shapes in data/stores.md only; not fetched | Product JSON gives exact variant availability, better than page text | keep plan "a" of check-stock (raw JSON by a user-run script) once O1 is checked per store | O1 |
| 20 | Purchase optimizer (E-6, planned) | Planned own optimizer | PuLP (CBC, free) or OR-Tools: fixed shipping per store is a standard fixed-charge MILP | evals/README.md:20 already lists `pulp` | Exact optimum, less code | use PuLP; write only the model | E-6 smaller |
| 21 | Global allocation and budget curve (Phase 8) | Planned own method plus surrogate | none covers CLP, owned copies and parity | — | Gap | keep-as-gap, as enumeration/MILP over measured candidates | see section 4 |
| 22 | Dashboard | Planned | Artifact tool | memory | — | keep (Artifact) | none |
| 23 | Budget-aware upgrade tools (Grimoria, EDHREC budget pages, MTGGoldfish Budget Commander) | — | They use USD and EDHREC data, no Chilean stock | Web search only | No CLP, no stock, terms bar automation for EDHREC | do not use in scripts; owner may browse EDHREC by hand | none |
| 24 | Speed risk flag | Retired 2026-10-13 | Site "Turns over fast", curve and speed fields | Deck `9354c58f...` "CURVE & SPEED ... Turns over fast" | — | keep retired; fix stale CLAUDE.md text | doc fix |
| 25 | Builder/reviewer agent runs for Toph and Azula references (README Phase 4 "Toph and Azula follow") | Planned | Site leaderboards and Upgrades | rows 2, 7 | — | drop | saves 2 builder plus 2 reviewer runs |

## 2. What the Commander Salt pages actually give
Checked by hand in Chrome, 2026-10-13. "VERIFIED" = seen on the page; "NOT VERIFIED" = not seen.

### Commander page (`/commanders/id/<slug>`; found from the deck pages' "Commander page" link and, for Alexios, from the Commanders list filtered by red, power 5-6, 100+ decks; no typing)
| Question | Answer | Status |
|---|---|---|
| Header | Deck count, average power, bracket, salt, synergy. Toph 4,003 decks / 6.8 / 4.0; Azula 5,301 / 7.8 / 4.1; Alexios 1,555 / 5.4 / 4.0 (counts grow daily: docs say 4,001 / 5,298 / 1,553) | VERIFIED |
| Tabs | Decks, Cards, Combos, Salt, Synergy, Manabase, Archetypes | VERIFIED (only Decks and Cards opened) |
| Leaderboard rows | Title, commander, author, decimal bracket, salt, added date, power. **No card list on the leaderboard** | VERIFIED |
| Sort and filter | Sort default "Power" (other sort keys not checked). Filters: text search, power slider 1-10 with presets, bracket slider (UI 2-5, integer steps), salt 0-500+, archetype, color identity. URL takes decimals: `?bracket_max=3.9`, `?bracket_min=4&bracket_max=4.4` worked | VERIFIED |
| Filter quirks | Decks with no bracket value (imported ">2y ago") pass `bracket_max`; an Alexios deck shown as 3.9 / 7.5 in the unfiltered list was missing from the `bracket_max=3.9` view (probably stored as 3.95) | VERIFIED (cause NOT VERIFIED) |
| Full list of a ranked deck | On its deck page: Cards tab lists every unique card (89 rows for a 100-card list, basics once) with per-card power and synergy; **Export list copies the 100 cards to the clipboard** ("Copied 100 cards to clipboard"); View deck links to the source site (Moxfield/Archidekt profile shown) | VERIFIED (note: Export list overwrote the owner's clipboard once) |
| Per-card inclusion rates | Cards tab: "% and n/N" per card, bins Bracket 1-5 or Power 1-3/3-5/5-7/7-9/9-10, optional archetype. Toph Bracket 4 bin 1,301 decks (Sol Ring 93%, 1208/1301); Alexios Bracket 3 bin 332 decks (Sol Ring 89%, Chaos Warp 70%, Shiny Impetus 64%...) | VERIFIED |
| Scoring version per listed deck | Not shown on rows; rows show "added" dates up to >2 years old, so many scores predate 2026.4195 | NOT VERIFIED per deck |
| Max power, CS bracket <= 3.9 | Toph 7.4 (DJfox deck, page shows bracket 3*, WotC spec 2, 0 Game Changers); Azula 7.4 (7 decks at 3.9 / 7.4); Alexios 7.5 (shown 3.9, see quirk) else 7.4 (a no-bracket deck from >2y ago) | VERIFIED |
| CS bracket versus power | Near-monotonic: Toph 3.9 -> 7.3-7.4, 3.8 -> 7.0-7.2, 3.7 -> 6.8-7.0, 3.6 -> 6.7; Azula 4.0 -> 7.5, 4.4 -> 8.1-8.2. Alexios is less regular (4.8 at 7.4). The rationale text says the bracket is "driven mainly by a power level above its WotC criteria read" | VERIFIED |
| Max power with WotC spec 3 (site checklist) | Azula >= 8.2 (deck `507bfae4...`: 3 GCs, no MLD, extra turns or two-card infinites per the site; CS bracket 4*). Alexios >= 8.0 (deck `f4b8cc3a...`: 3 GCs plus 2 two-card combos the site counts as Bracket 3; Layer A would likely reject Aggravated Assault + Neheb as early). Toph: only a 7.4 WotC-spec-2 deck sampled. True maxima unknown: the leaderboard cannot filter by WotC spec | VERIFIED samples; maxima NOT VERIFIED |

### Upgrades tab (on a deck page; read on the owner's Toph deck)
| Question | Answer | Status |
|---|---|---|
| Modes | "All cards" (format-wide by role) and "Meta" (tuned to the commander) | VERIFIED |
| All cards | Category select (Counterspells, Tutors, Fast Mana, Ramp, Board Wipes, Wincons...), types, color identity, "Include Reserved List", Advanced filters: oracle text, mana value range, **Max price (USD)**, keywords, supertypes, subtypes, produces mana, additional categories, land/effect/trigger/result filters, qualifiers, sort and page size | VERIFIED (panel only; no category run, so its output is NOT VERIFIED) |
| Meta | Source: Staples, Synergy, Manabase, Archetype, Combos. Bin: Bracket 1-5, Power 1-3 ... 9-10 ("10 tuning bins"); default bin Bracket 4; deck count per bin; optional archetype | VERIFIED |
| Meta output | Card name, inclusion % in the bin, TCG USD price or "Buy on TCG"; 100 shown per page with "Show more" | VERIFIED |
| Deck-aware | Text says it "surfaces cards the deck is missing"; none of ~25 top Staples checked against `data/raw/Toph.txt` is in the deck; Combos marks each piece "In your deck" / "Missing" with "N cards away" | VERIFIED (exclusion rule inferred) |
| Budget | Only a per-card USD max-price filter; no total budget, no CLP, no owned collection | VERIFIED |
| Bracket safety | Not filtered to Wizards' Bracket 3: suggests two-card infinite-turn and lock lines at the Bracket 3 bin | VERIFIED |
| Roles | Role categories in All-cards mode; Meta shows no role per card | VERIFIED |

### Deck page facts used above
Bracket tab: "WOTC SPEC" vs "COMMANDERSALT" with delta, criteria checklist (GC count, MLD, extra
turns, two-card infinites, early infinites), rationale, rule-zero notes, "drop to a lower bracket"
moves. Power tab: pillars, fingerprint, drivers, suggestions, per-card contributions. VERIFIED.
Not checked: how import works (plain text versus link) beyond what the docs say; whether a deck
page shows its scoring version.

## 3. Revised pipeline
| Phase | What it does now | Who | Blocked by | Retired work |
|---|---|---|---|---|
| 0 Rules | Snapshot done; re-check at the 2026-11-30 announcement and in Phase 11 (Layer A run prints bulk date and GC count) | Claude (web read) | none | E-2 script |
| 1 Digitize | Loose collection scan in ManaBox; rebuild inventory | Owner, then owner runs `build_inventory.py` | owner | — |
| 2 Layer A | Done; run on every candidate list | Owner runs, Claude reads | — | speed flag (already) |
| 3 Synergy | Closed; reports archived as rules-trap inputs | — | — | further agent research |
| 4 Candidate menu (new) | Per commander, pick 8-15 recent public decks spanning power ~6.0 to the top that passes Layer A at Bracket 3, from the leaderboard (CS bracket filter as a first cut, then Layer A); copy each list (Export list, one deck at a time), save as `decks/candidates/<slug>/<id>.txt` with power, CS bracket, WotC spec, date, version. Add our Alexios reference as one candidate. For Toph and Azula also note the Meta Staples/Combos picks at the owner's target bin | Owner copies (or Claude in Chrome reads the Cards tab plus basics), Claude records; owner runs Layer A | owner OK on how many decks may be read (Q3) | agent references for Toph and Azula, slot ranking, fillers, ladder |
| 5 Repeatability | Score one list twice on different days; confirm the version | Claude in browser | owner hosts nothing new (reuse Toph link) | ladder calibration |
| 6 Owner decks | Done (Toph 6.5, Azula 4.0); owner picks locked cards (O2) | Owner | owner | — |
| 7 Prices | CLP prices for the union of missing cards across all candidates, from the store catalogs (method per store from O1); fill shipping and fees | Owner runs a reader script or Claude reads pages | O1, stores.md rule (see section 5) | — |
| 8 Allocation and curve | For each budget point, choose one list per deck (candidates plus owner deck plus partial upgrades of it built from the Meta picks) minimizing cost with PuLP, maximizing the minimum power at parity 0.2; intermediate lists that are not already scored get hosted by the owner and scored (about 15); dashboard Artifact | Claude writes code and tests; owner runs; Claude scores by hand | 6, 7 | surrogate model |
| 9 Stock | Verify stock for the shortlist (JSON first, browser second) | Owner runs script / stock-verifier | 8 | — |
| 10 Backtrack | Re-plan on stock failure; re-score changed lists | Claude plus owner | 9 | — |
| 11 Final | Rules freshness, site score of frozen lists, 24 h stock re-check, pull list, purchase by owner, reconciliation | Owner buys | 10 | — |

Phase 4 does not depend on Phase 3 any more; it depends on Phase 2 (Layer A) only. Phase 7 needs
Phase 4 (the card union), Phase 1 (owned cards) and O1.

## 4. Risks and open questions for the owner
| ID | Question | Recommendation |
|---|---|---|
| Q1 | Bracket target: Wizards' conditions only (Layer A, current rule) or also "Commander Salt bracket below 4" (about power 7.4-7.5 cap)? | Keep Wizards-only as the gate (your rule), show the site's bracket on the dashboard, and decide after seeing the curve; note decks above ~7.5 will read as "bracket 4" on the site your friends may also use |
| Q2 | Leaderboard decks from older scoring versions | Use only decks added after 2026-09-29 (release 2026.4195) or re-score them through your own ManaBox copy |
| Q3 | Reading 8-15 public decks per commander (24-45 deck pages) by hand, one at a time: within the 2026-10-13 authorization? | Yes if done at human pace, one page at a time, no Refresh/Import of others' decks; confirm |
| Q4 | Retire the Alexios reference, slot ranking, fillers and ladder? | Retire ladder, ranking and fillers now; keep the reference as one candidate and score it once (owner hosts it on ManaBox) |
| Q5 | Parity 0.2 with a site that shows 0.1 steps and small header/report mismatches | Keep 0.2, measure repeatability in Phase 5 first; widen only if two scores of one list differ by 0.1 or more |
| Q6 | Store visits in Phase 7 (stores.md allows visits only in Phases 9-11) | Allow catalog price reading in Phase 7 (stock still only in 9-11) and update stores.md |
| Q7 | Scry.cl as a price index | Look at it yourself once: if your 7 stores list there, it may save Phase 7 work as a price hint; never as stock evidence and never as a place to buy |
| Q8 | Public lists will not contain your locked cards | Treat locked cards as forced swaps and re-score the final lists (already part of Phase 8) |
| Q9 | stock-verifier on Haiku (D9) versus "strongest models" (CLAUDE.md) | Sonnet for the final 24 h re-check |

## 5. Stale or contradictory statements (file:line)
| Where | Problem |
|---|---|
| CLAUDE.md:135-136 | Says speed appears as a 5-level Monte Carlo flag; retired 2026-10-13 (README.md:20, power-scale.md:3-4) |
| CLAUDE.md:122 | `evals/` described as "Reference lists and ablation rungs"; both proposed for retirement |
| CLAUDE.md:62 and :121 vs evals/README.md:4 | CLAUDE.md lets Claude run `pytest`; evals says pytest is not installed and tests run with `python tests/<file>.py` |
| README.md:50-51 | Calls `docs/power-scale.md` "superseded"; CLAUDE.md layout calls it the source of truth and it is v1.0 current |
| README.md:31 | "Status as of 2026-10-12" while rows carry 2026-10-13 updates |
| README.md:22-23, power-scale.md:102-103, rating-protocol.md:22-25, evals/README.md:13, :18 | Phase 4/5 still built on the reference plus ablation ladder |
| rating-protocol.md:18, commandersalt-adoption.md:79 | "local surrogate" power model: a new own scale; contradicts the prior-art rule |
| commandersalt-adoption.md:54-55, :82-88, :90-96 | Still proposes the email and lists decisions as open, while its own status line (:3-5) says adopted and no email |
| commandersalt-adoption.md:66 | "Ablation ladder: keep, but measure it" vs this audit |
| data/stores.md:4-5 vs :24-25 and README.md:25 | Store visits allowed only in Phases 9-11, yet Phase 7 reads catalogs and fills shipping |
| power-scale.md:28 | Community counts (1,553 / 4,001 / 5,298) already moved (1,555 / 4,003 / 5,301); say "as of" or drop |
| scripts/layer_a.py:13 and :578 | Docstring and message say "Toph only" / `data/raw/Toph.txt`; code (:36-37) also reads `Azula.txt` |
| .claude/skills/build-deck/SKILL.md:17-19 | Step 2 has Claude invent candidates by role; should start from the site's Meta picks and candidate lists |
| .claude/skills/rate-deck/SKILL.md:20 | Says "Import deck"; memory notes the working path is the home page "Decklist URL" field |
| memory project-mazos-magic.md:26 | "Budget 200,000 CLP total; max 3 stores": superseded by the curve and no store cap |
| memory project-mazos-magic.md:36 and feedback-working-style.md | Stock verifier "Sonnet"; agent file says `model: haiku` (D9 Haiku) |

Checks behind this file: test counts by `def test_` (35, 6, 7, 5, 5, 5, 3, 2 = 68); hook table
147 lines minus 7 comment lines = 140 cases (matches README); Game Changers 53 in the cached bulk;
leaderboard rows read in full: 50 per view in 6 views (Toph unfiltered, `bracket_max=3`,
`bracket_max=3.9`; Azula `bracket_max=3.9`; Alexios unfiltered and `bracket_max=3.9`), plus the
first 5 rows and the last row of Azula `bracket_min=4&bracket_max=4.4` (read through the find tool,
a model summary). Deck pages opened: owner's Toph and Azula, Toph `9354c58f...`, Azula `507bfae4...`,
Alexios `f4b8cc3a...`.
