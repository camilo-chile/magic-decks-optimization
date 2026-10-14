# Proposal: use Commander Salt as the power yardstick (prior-art review)

Status: **adopted by the owner on 2026-10-13**. Answers: (1) yes, use everything the site offers, even
if the approach changes radically; (2) no email will be sent, use the app as it can be used; (3) the
pilot uses the two scanned decks (Toph and Azula) through their ManaBox links, since Alexios has no deck yet. Trigger: the owner pointed out that the project rebuilt, by hand, things
that an existing site already does (power level, bracket rating, synergy, combos, upgrades).

## 1. What the site is (read in the real browser on 2026-10-13)
Commander Salt (commandersalt.com) analyzes a public Commander deck from a link and returns a
bracket, a power level, a salt score, combos, synergy, mana base, card roles, archetypes and
upgrade suggestions. The analysis is deterministic ("not AI generated"), versioned (latest
scoring release 2026.4195 of 2026-09-29, with a public changelog) and documented in
`/powerlevels` (bands) and `/algorithm` (ingestion flow).

| Output on a deck page | What it gives |
|---|---|
| Bracket | WotC criteria checklist (Game Changers, mass land denial, extra turns, two-card infinite combos, early-game infinite combos), a "Commandersalt" bracket as a decimal (decks of 3.9 and 4.8 exist) and the delta between both, rationale, rule-zero notes |
| Power level | 1 to 10, bands: casual 1-4.99, upgraded casual 5-6.49, mid 6.5-7.59, high 7.6-8.99, fringe cEDH 9-9.29, cEDH tiers above; four pillars (consistency, efficiency, interaction, win conditions) against casual and cEDH baselines; flagged anti-patterns; score drivers up and down |
| Salt | Salt score and report card |
| Combos | Combo lines with score, mana, pieces, outcomes, redundancy, speed and friction |
| Synergy, mana base, cards, archetypes | Synergy score and coverage, mana base breakdown, cards by role with contribution, archetype fingerprint |
| Upgrades | Suggestions by role (counterspells, tutors, fast mana, ramp, wipes, win conditions), "tuned for this commander" from aggregate stats at a chosen bracket or power level |
| Commander page | Number of decks, average power, bracket and salt, a leaderboard of decks sorted by power, card inclusion rates for the commander (for example "Sol Ring 94%, 1394/1485") |

## 2. Reference numbers (the owner's friend's deck and the community)
| Item | Power | Bracket | Salt | Note |
|---|---|---|---|---|
| Friend's deck: Krenko, Mob Boss, "Goblin" by nikolasgg_ | **6.1** (upgraded casual) | 3* (WotC criteria say 2, Commandersalt says 3) | 78.3 | 33 lands, 7 combo wins on one Krenko line, moderate fast mana. **The level to beat** |
| Alexios, 1,553 decks | 5.4 average | 4.0 | 76.3 | Top public decks reach 9.2; a Bracket 3.9 deck scores 7.5 |
| Toph, 4,001 decks | 6.8 average | 4.0 | 93.8 | |
| Fire Lord Azula, 5,298 decks | 7.8 average | 4.1 | 94.0 | |

Reading: power is a separate axis from the bracket, so a Bracket 3 deck can sit well above 6.1
(a public Alexios deck with bracket 3.9 scores 7.5). The averages include cEDH-style lists.

## 3. Access: what is allowed and what is not known
| Question | Finding |
|---|---|
| Public API or MCP | None documented. Searches found no API, MCP server or developer page |
| Terms of service | No terms page found (only a privacy policy dated 2026-06-01 and a changelog). The site is ad-supported and offers Patreon |
| `robots.txt` | Lists three sitemaps and no disallow |
| How a deck gets in | **Paste a link** to a deck hosted on Moxfield, Archidekt, TappedOut, ManaBox, MTGGoldfish, Scryfall, Topdecked and others. Plain text is not accepted |
| How results come out | Only in the web page (and an "export list" button for the decklist). The data is rendered in the browser; no export of scores |
| Does importing publish the deck | Unknown. The privacy policy says imported decklists and deck URLs are saved, and decks appear on commander leaderboards |

Consequences under the project's rules:
- It is not scripted: no documented API, no terms read, so no automated bulk requests (the same
  policy as EDHREC, Archidekt and Moxfield, decision D7).
- It can be used the way a person uses it, one deck at a time, in the owner's browser, with the
  owner's go-ahead for every submitted deck. Claude reads the page; it never signs in, never
  creates an account and never submits anything without an explicit yes.
- Numbers are stamped with the site's scoring version and the date; the site says scores can
  change with new releases.
- No email is sent (owner decision, 2026-10-13: use the site by any means, in the browser, by hand).
  The draft in section 7 is kept only as a record.

## 4. Component by component: keep, replace, drop
| Our component | What the site does | Decision proposed |
|---|---|---|
| Power scale `X.Y` and Layer B (10-judge panel, Bradley-Terry, ablation ladder, local Ollama model, ~1,400 judgments per rating) | Calibrated algorithmic power 1-10 and a decimal bracket on thousands of public decks | **Replace.** Use Commander Salt power and bracket as the yardstick. Drop Layer B, the judge panel, the rubric agent and the Ollama install |
| Layer A (official conditions of the target bracket) | WotC criteria checklist | **Keep as the offline pre-gate** (the optimizer needs thousands of checks; the site cannot be queried in a loop) and cross-check every final list against the site's checklist |
| Speed-risk Monte Carlo | Speed, fast mana, tutor quality, "turns over fast", pillars | **Retire** from the pipeline; the site's speed and pillars replace it (the code stays, no more work) |
| Phase 3 synergy research by agents | Synergy score, combos, role breakdown, upgrades, inclusion rates per commander | **Replace** for any future research. The three finished reports stay as inputs |
| Community anchors dropped in D7 (EDHREC, Archidekt, Moxfield barred) | Leaderboard of real decks with measured power and card inclusion rates per commander | **Restore** as anchors, read by hand from the commander pages |
| Ablation ladder (synthetic, labels `9 - k/4`) | A dense measured spread of real lists per commander | **Dropped 2026-10-14** (prior-art audit): the ladder answers no decision; labels were already removed |
| Claude-built reference decks | Real top decks of each commander at a chosen bracket | **Replaced 2026-10-14**: real lists from the commander page are the candidates (`decks/candidates/`); the agent-built Alexios reference is archived |
| Combos (Spellbook bulk file, local) | Combo lines ranked by score | **Keep Spellbook** as the primary source; use the site as a cross-check |
| Prices and stock in CLP from 7 Chilean stores | none | **Keep.** A search for a Chilean price comparator found none; a deeper prior-art search for stores is still pending |
| Budget optimizer | Upgrades are not budget-aware | **Keep**, with its candidate pool fed by the site's upgrades and inclusion rates |

## 5. What changes in the pipeline
| Phase | Before | After |
|---|---|---|
| 2 | Layer A, speed flag | Layer A stays; speed flag retired |
| 3 | Agent synergy research | Done; future work reads the commander pages |
| 4 | Reference and ablation ladder, accepted by criteria | Candidate menu: real public lists from the commander page, each with its site score, gated by Layer A (done 2026-10-14) |
| 5 | Validate the panel method, install Ollama, 40 known-answer items | **Repeatability only**: the same list scored on two days (done 2026-10-14). No ladder, no Ollama |
| 6 | Panel rates Toph and Azula | Import the owner's two decks (ManaBox share links) and read their power |
| 8 | Optimizer on a surrogate `Y_hat` from the ladder | No surrogate: choose among measured candidates and Meta-pick upgrades with PuLP; each budget point's final list is scored on the site (about 15 lists) |
| Goal | Parity within 0.2 on `Y` | Parity within 0.2 power points, every deck above 6.1 (the friend's deck) and as high as the budget allows |

## 6. Decisions needed from the owner
All answered on 2026-10-13: (1) adopted; (2) no email; (3) pilot with the owner's Toph and Azula
ManaBox links, done; (4) every deck above 6.1, as high as the budget allows.

## 7. Draft email (English, from the owner)
> Subject: Question about using Commander Salt for personal deck analysis
>
> Hi, I am building three Commander decks for casual games with friends and I use Commander Salt
> to read the power level and bracket of my decks. Is there an API or a documented way to read a
> deck's scores, and is it fine to analyze about 30 of my own deck lists over the next weeks by
> hand? I would not scrape or resell anything. Thanks for the site.

## 8. Prior-art rule (added to CLAUDE.md the same day)
Before designing or building anything, search for existing tools and data that already do it,
record the survey in `docs/research/`, and build only the gap. Pending surveys: Chilean card
price and stock sources, deck upgrade and budget optimizers, collection tools already covered
by ManaBox.
