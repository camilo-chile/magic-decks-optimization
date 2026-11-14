# Final review: Kilo, Apogee Mind, the 100 % Spanish deck (Phase 2 step 7.7, 2026-11-09)

Reviewer: an independent champion (Opus 5.5 high). The list under review is `decks/phase2/spanish-deck.txt`, with its
`.plan.json` and `.build.md`. The mandate is `docs/proposals/final-rebuild-brief-20261108.md`, corrected budget:
- Kilo's envelope is 18,000 CLP all-in, hard cap 20,000; the whole order stays under 100,000, target 90,000;
- every buy costs under 3,000, comes from Game of Magic Singles (GoM), PayToWin (PTW) or Rivendel (Riv), and is a Spanish copy;
- any condition better than Damaged.

Read: the skill and its Champion standard, the champion addendum (41 items), the Kilo primer, `real-power-iterations-20261108.md`,
the pool `data/model/phase2/pool-spanish-deck.json`, the collection inventory `data/cache/collection_inventory.json`, the
current list `decks/phase2/moxfield/spanish-deck-after-purchases.txt`, and the final Ezio, Azula and Toph lists. Card text comes
from the Oracle cache `oracle-cards-20261011210156`; combo data from `spellbook_variants_slim.jsonl.gz`; prices from
`data/prices/rivendel-20261108.psv`, `browser-*-20261108-order.psv`, `20261107T2140Z.json`, the builder's scratch reads, and
my own read of the GoM and PTW search endpoints on 2026-11-09 (section 3).

**Verdict: FIX.** Three swaps with owned Spanish cards that no final deck plays (no new money), and a stock read of the
five "to read" buys before the order. No blocker.

## 1. Rules

| Check | Result |
|---|---|
| `python scripts/check_phase2_bracket.py decks/phase2/spanish-deck.txt` | **PASS**: floor 1, 0 Game Changers, no extra turns, no mass land denial, no reversible card; Spellbook: 1 variant inside the list (Crawler + Lux + Excavation), 0 flagged. |
| `python scripts/plan_density.py` | **PASS** for Kilo: 0 failures, 1 WARN (the poison route rests on one card; reason written in build section 3). The other three decks also PASS. |
| Card count | 100 by script (1 commander + 99): 37 lands, 62 nonland. |
| Game Changers | 0 (script). |
| Early two-card infinite, chained extra turns | None. The only infinite is the four-card loop Lux Artillery + Crystalline Crawler + Meticulous Excavation + Surge Conductor (section 2), late by construction. Magistrate's Scepter is not in the list. |
| Reversible cards | None. |
| Language and copies | Script over the four final lists and the inventory, other decks taking English first: every owned card has a free Spanish copy, with one dependency: **Thirst for Knowledge** (1 Spanish copy, Azula also plays it); covered because Azula buys its own copy (Azula build notes line 119, "BUY, stock line"). The 11 buys have no owned Spanish copy, as claimed. |
| Claimed moves | **Swords to Plowshares**: 2 Spanish, 0 English; Toph and Ezio both play it, so Kilo's copy exists only if Ezio plays the English copy bought at GoM (2,500); Ezio's notes say so (lines 305, 345). Correct. **Command Tower**: 2 Spanish + 1 English; Azula EN, Toph ES, Ezio ES; Ezio takes a bought copy (Ezio notes line 344). Correct, see finding F6 for a simpler way. **Fateful Absence**: 2 Spanish; Toph plays one, Ezio's final list does not: the spare is free. Correct. Chaos Warp (2 ES + 2 EN, three other decks): one Spanish copy free. Correct. |
| Reports | The scripts were rerun on the real list after my scratch tests (scratch reports went to the scratchpad only). `decks/reports/bracket-spanish-deck.md` and `consistency-*.md` show the real lists. |

## 2. Verdicts on the closer claims (Oracle text and Spellbook cache)

| Claim | Verdict | Evidence |
|---|---|---|
| Crawler + Lux Artillery + Meticulous Excavation needs four colors | **Confirmed** | Spellbook variant 1034-1350-2060: `mana_needed` "{4} in four different colors". Crawler (converge) + Lux (gives artifact creature spells sunburst) count colors twice: 3 colors = 6 counters = 6 mana; a loop costs {2}{W} + {4} = 7. In a three-color identity mana of a fourth color cannot be made, so the three-card loop loses 1 mana per turn. |
| The four-card version with Surge Conductor | **Confirmed** | Surge Conductor proliferates when Crawler (another nontoken artifact) enters: 7 counters = 7 mana = net 0, unbounded: each loop is one more proliferate (Surge), one artifact entry (Fireweaver ping) and one Lux count. With Tekuthal: 8 counters, +1 mana per loop. Excavation works only during my turn. Four cards, not early, Bracket 3 legal. |
| Darksteel Reactor | **Works** | Alternate win at 20 charge counters, indestructible; fed by its upkeep, every proliferate, Coretapper and Inspirit; funnels Resourceful Defense (instant), Moxite Refinery (sorcery), Deepglow Skate (doubles). Realistic 3 to 4 rounds after it lands; with Deepglow (and, after F1, Strionic Resonator copying Deepglow's trigger: x4) much faster. Fails to exile, bounce, Chaos Warp-type tucks and artifact counterspells. |
| Prologue to Phyresis poison | **Works by the rules; not sourced** | Prologue: "Each opponent gets a poison counter. Draw a card." Proliferate chooses players, so every proliferate adds one to each opponent. Needs 9 more proliferates on the players: 2 to 4 rounds with Kilo + Surge + Flux, about half that with Tekuthal. But no store has shown a copy (section 3): today the route has no card. |
| Lux Artillery + Reckless Fireweaver | **Works (Lux); Fireweaver is support** | Lux deals 10 to EACH opponent at my end step with 30+ counters on my artifacts and creatures (poison on players does not count; charge counters on the Reactor do). Four end steps kill a 40-life table; with Strionic copying the trigger (F1) two. Fireweaver pings 1 per artifact entry; it is "infinite" only inside the four-card loop. |
| Cyberdrive Awakener / Titan Forge | **Works, with a condition the notes omit** | Cyberdrive makes every noncreature artifact a 4/4 and gives artifact creatures flying. Rocks and artifact lands tapped to cast the 6-drop cannot attack, so the 6 mana must come from lands for the alpha to be big. Titan Forge needs three {3} activations (fewer with proliferate) per 9/9. A real backup, not a fast one. |
| Kilo's tap outlets | **Mostly confirmed** | Kilo becomes tapped by: attacking; Relic of Legends' second ability (a cost with no {T} of its own, so it repeats while a legend is untapped); Brute Suit crew 1; waterbend costs (Katara {6}, North Pole Patrol {3}, Waterbending Lesson {2}); improvise (Universal Surveillance, Organic Extinction); station (Inspirit, Uthros; sorcery speed). Instant-speed outlets: Relic, Brute Suit, Katara, Patrol's waterbend. |
| Kilo's untap outlets | **Only one: North Pole Patrol** | "{T}: Untap another target permanent you control": once per round, not the turn it lands, and not in a round when Patrol waterbends. So Kilo taps at most twice per round; "one to three times every turn cycle" (plan sentence) overstates by one. Copies of the trigger (Strionic, Lithoform, F1/F2) are the realistic way to a third and fourth proliferate. |

## 3. Facts: buy prices and stock

| # | Card | Claimed | Evidence found | Verdict |
|---|---|---|---|---|
| 1 | Negate | Riv 300, 4 ES | Builder's live Riv read (scratch `riv.json`/`riv.log`, 2026-11-08 22:57): "Negate: ES=300 (español no foil, q=4)". Not in a repo price file. | Correct; save the read (F5) |
| 2 | Volt Charge | Riv 200, 14 ES | `rivendel-20261108.psv`: 200 Español, 14 | Correct |
| 3 | Contentious Plan | Riv 300, 1 ES | Scratch `riv.json`: 300 "español no foil", quantity 1. Not in a repo price file. | Correct, single copy; save the read (F5) |
| 4 | Meticulous Excavation | Riv 300, 16 ES | `rivendel-20261108.psv`: 300 Español, 16 | Correct |
| 5 | Relic of Legends | Riv 2,500, 3 ES | `rivendel-20261108.psv`: 2,500 Español, 3 | Correct |
| 6 | Talisman of Conviction | GoM 1,500 ES | `browser-gameofmagic-20261108-order.psv`: Near Mint Español 1,500 (TDC) | Correct |
| 7 | Command Tower (for Ezio) | PTW 900 | `browser-paytowin-20261108-order.psv`: LP English 900 (CMR) and **LP Spanish 900 (C17)** | Correct; F6 |
| 8 | Swords to Plowshares EN (for Ezio) | GoM 2,500 | `browser-gameofmagic-20261108-order.psv`: NM Regular EN 2,500 (the Spanish GoM copy is 3,000, at the line) | Correct |
| 9 | Prologue to Phyresis | to read, ~400 | Riv: none (`riv.json`). GoM and PTW: the store search (`search/suggest.json`, read by me 2026-11-09) returns no Prologue product at either store (top results are other Phyrexia cards). The builder's script reads of GoM and PTW returned `[]`, but product pages answer HTTP 429 to scripts (I reproduced it), so `[]` is not stock evidence. | Spanish copy under 3,000: price plausible (ONE uncommon, 0.52 USD), **stock unlikely** in all three stores |
| 10 | Counterspell | to read, ~2,500 | Riv: none. Products exist at PTW (7ED, MH2, DMR retro, Ice Age, Revised...) and GoM (CMM, DMR...); variants and languages unread (429). | Plausible but uncertain: a Spanish Counterspell under 3,000 is not common in Chilean stock |
| 11 | Flux Channeler | to read, ~2,600 | Riv: none. A WAR product exists at PTW and at GoM; variants unread. | Plausible only near the line (2.59 USD) |
| 12 | Tribute Mage | to read, ~1,000 | Riv: none. PTW lists MH1, MH2 retro, Secret Lair; GoM search shows no product. | Plausible at PTW |
| 13 | Trophy Mage | to read, ~600 | Riv: none. PTW lists AER and an AER promo; GoM search shows no product. | Plausible at PTW |

Five buys (about 7,100 of the 15,600) have no reading. The script cannot read GoM and PTW product pages; the lead must read
them in the browser (`scripts/browser_shopify_lookup.js` through `browser-runner`) before the order.

## 4. Strength, as a champion

**Plan and routes.** One clear plan: Kilo plus 21 counter sources and 12 proliferate pieces turn counters into mana, cards
and three noncombat closers that hit the whole table. Routes are disjoint enough: no failure point is shared by every route,
and the Reactor and Lux routes work with Kilo dead. Weak spots: the poison route is one card that is not yet sourced, and no
tutor reaches a finisher (Trophy and Tribute Mage find MV 3 and MV 2 artifacts; Reactor and Lux are MV 4). Access to the
primary route is Reactor + Long-Range Sensor (discover 4) + dig (Augury, Thirst, Waterbending Lesson, Insight Engine) +
recursion (Emry, Buried Ruin): short of R18's 10 cards. The builder's answer (four routes, redundancy) is reasonable for this
budget, but it is why the deck is a 5-6, not a 7.

**Curve and mana.** 37 lands + 9 lasting rocks = 46 (R8 met), 1 always-tapped land (R10 met), average MV 2.89. Land
color sources by my count: blue 19, white 16, red 16, plus six any-color rocks; fine for {U}{R}{W} on turn 3. Keep rate: I
reproduce 80.7 % with the builder's rule (2-landers only with a 1-2 mana rock, 5-landers shipped). R33 ships 0-1 and 6+
landers; keeping 5-landers (a mana-hungry deck with Karn's Bastion, Insight Engine and Titan Forge sinks) gives **85.3 %**,
and keeping 2-landers with Barrels or Chromatic Star gives 83.4 %. The shortfall is the stricter house rule, not the build. No change.

**Interaction and protection.** 12 spot answers, 6 at MV 2 or less, 8 instants, 3 answers each to artifacts and enchantments
(Chaos Warp, Airbending Lesson, Lux Cannon): R19 met. Counters 2 + Ripples (R20 met for a tap-out engine deck). The win-turn
shield is 3 only if Counterspell arrives; otherwise Negate + Ripples. Wipes: Organic Extinction is near one-sided; Fumigate
is symmetric in a deck with 20 creatures, most of them engines (Surge Conductor, Tekuthal, Steel Overseer, Coretapper,
Crawler, Flux): it costs this deck more than it costs a token deck (R21, F4).

**Game Changer slots: 0 used, correctly.** No Game Changer is owned in Spanish (the only owned one, Drannith Magistrate, is
English). Live Game Changer list in {U}{R}{W}: the cheapest are Narset, Parter of Veils (1.24 USD; Riv has only a 13,000 Spanish
foil), Gifts Ungiven (4.52 USD), Farewell (5.27 USD); the rest cost 10 USD or more. Narset is the one worth a read: a Spanish
non-foil WAR copy at GoM or PTW could be under 3,000, and with Kilo proliferating loyalty it digs four cards every turn (F9).

**The weakest 10 cards (in games where drawn) and better replacements.**

| Weak card | Problem | Replacement | Source |
|---|---|---|---|
| Brute Suit | A 3-mana vehicle whose only job is a Kilo tap that Relic and waterbend already give | **Strionic Resonator** (F1) | owned ES, free |
| Katara, Bending Prodigy | {6} waterbend for one card; a weak tap outlet | **Lithoform Engine** (F2) | owned ES, free |
| Fumigate | Symmetric wipe that kills my engines | **Starfall Invocation** (F4) | owned ES, free |
| Commander's Sphere | 3-mana rock in a deck with 9 rocks | keep (R8 needs 46); Narset if found (F9) | watch |
| Thought Monitor | Fine; affinity draw 2 | Fabricate or Whir of Invention if a Spanish copy under 3,000 appears (tutor to Reactor/Lux, F9) | watch |
| Titan Forge | Slow 9/9s | keep: second piece of the backup route | none better |
| Chromatic Star | Low impact | keep: cheap artifact entry for Surge Conductor, Fireweaver, Jhoira, Uthros | none better |
| Astral Cornucopia | Bad early | keep: grows with every proliferate | none better |
| Meticulous Excavation | Alone, a slow bounce | keep: 300 CLP, the loop piece and ETB reuse | none better |
| Deepglow Skate | Bad early | keep, and better with F1 (Strionic copies its trigger: x4 counters) | none better |

Why these swaps are free: the pool's `held_by` (written 2026-11-02) still shows Strionic Resonator and Lithoform Engine in
Ezio and Starfall Invocation in Ezio, but Ezio's FINAL list (2026-11-09) plays none of them. Each has one Spanish copy in the
Spanish Cards binder (inventory) and no other final deck lists it. The builder's cut pass compared against this stale pool,
so it never saw them. Also free now and not proposed: Consider and Torrential Gearhulk (Azula's final list dropped both).

**Against the current list and the precon in a real 4-player game.** Against the precon: clearly stronger (curve, untapped
mana, answers, three table-wide closers). Against the current list after purchases: most of the new strength sits in the
five unread buys (Prologue, Flux Channeler, Counterspell, Trophy and Tribute Mage). If they all arrive, about +0.4; if they
do not, the stand-ins make it about equal to the current list (cleaner mana, Negate, Fateful Absence and Contentious Plan
against Swan Song, Generous Gift and Solar Array), for 6,700 CLP less. With my three free fixes it is clearly stronger in
both cases: Strionic and Lithoform double the commander's trigger and the closers' triggers at instant speed.

## 5. Findings and exact changes (ranked)

| # | Severity | Finding | Exact change |
|---|---|---|---|
| F1 | **fix** | Strionic Resonator (owned Spanish, MOC, unused by every final deck) is missing. At {2} it copies Kilo's proliferate at instant speed (a second or third proliferate per round), Lux Artillery's end-step trigger (20 to each opponent: Lux kills in two end steps), Deepglow Skate's trigger (x4 on the Reactor), Surge Conductor, the Reactor's upkeep, Jhoira and Uthros draws. MV 2 artifact: Tribute Mage finds it. | **-Brute Suit, +Strionic Resonator.** Plan: add to `counter_doublers`, `artifact_density`; drop Brute Suit from `kilo_tap_outlets` (11 to 10, and 9 with F2; minimum 6). |
| F2 | **fix** | Lithoform Engine (owned Spanish, ZNR, unused) is missing. {2}: copy Kilo's or Lux's trigger; {3}: copy Prologue (one more poison counter on each opponent and a card), Universal Surveillance or Thirst; {4}: copy Lux Artillery, Reactor or Deepglow as they are cast. It also reduces the poison route's one-card risk once Prologue resolves. | **-Katara, Bending Prodigy, +Lithoform Engine.** Plan: add to `counter_doublers`, `artifact_density`; drop Katara from `kilo_tap_outlets`. |
| F3 | **fix (before the order)** | The five "to read" buys (7,100 of 15,600) have no reading; the script reads of GoM and PTW are blocked (HTTP 429), so their `[]` results prove nothing. Prologue shows no product at GoM or PTW and none at Riv. | The lead reads Prologue, Counterspell, Flux Channeler, Trophy Mage and Tribute Mage in the browser at GoM and PTW (Spanish, any condition better than Damaged, under 3,000). If Prologue has no Spanish copy: Kappa Cannoneer keeps the slot, and the plan file drops the poison route (do not keep a route the deck does not hold); the build notes say so. |
| F4 | fix (small) | Fumigate kills this deck's own engines (R21). Starfall Invocation (owned Spanish, BLB, unused) is the same 5-mana wipe, and with the gift promised it returns my best destroyed creature (Surge Conductor or Tekuthal). | **-Fumigate, +Starfall Invocation.** Plan: same functions (`through_wide_board`, `through_big_creatures`, tag wipe). |
| F5 | note | The Negate and Contentious Plan readings exist only in the builder's scratchpad. Contentious Plan has one copy. | Save the Rivendel read to `data/prices/` (or re-read) so the order has evidence; Contentious Plan first in the Rivendel cart. |
| F6 | note | PTW sells a Spanish LP Command Tower (C17) at 900, the same price as the English one. | Buy the Spanish copy for Kilo directly; Ezio keeps its own Spanish copy. Same cost, no card moves between decks. |
| F7 | note | Plan text: "one to three times every turn cycle" and the plan names Brute Suit's crew and Katara's waterbend. Kilo has one untapper (North Pole Patrol): two taps per round at most. | Rewrite the plan sentence: "Kilo is tapped once or twice per round (Relic, waterbend, North Pole Patrol's untap) and his trigger is copied by Strionic Resonator and Lithoform Engine". |
| F8 | note | Keep rate 80.8 % is under a rule stricter than R33 (5-landers shipped). R33's ship list keeps them: 85.3 %. | Write the R33 number next to the house number in build section 5. No list change. |
| F9 | note | No tutor reaches a finisher (R18), and Narset (the one Game Changer near the price line) was read only at Riv. | Browser-read Spanish Narset, Parter of Veils, Fabricate and Whir of Invention at GoM and PTW. If one is under 3,000: Narset for Commander's Sphere; Fabricate or Whir for Thought Monitor. Sinking Feeling stays first on the watch list (infinite with Relic). |
| F10 | note | The Cyberdrive alpha needs its 6 mana from lands (rocks tapped for mana cannot attack). | One line in the play pattern. |

Scratch test of F1 + F2 + F4 (copy of the list and plan in the scratchpad, reports written there): `check_phase2_bracket`
PASS (floor 1, 0 Game Changers, 0 rejections); `plan_density` PASS, 0 failures, the same single WARN (poison route), doublers
12 to 14, tap outlets 11 to 9 (minimum 6), `through_wide_board` 11 (minimum 10). No token is needed: Strionic and Lithoform
copy abilities and spells (a Lithoform copy of a permanent spell is a token; a marker or a proxy token is enough).

## 6. Money: buys ranked by gain per CLP

| Rank | Card | CLP | Gain | Cut order if the global target needs room |
|---|---|---|---|---|
| 1 | Volt Charge | 200 | Instant answer + proliferate | keep |
| 2 | Negate | 300 | Win-turn shield, stops wipes | keep |
| 3 | Contentious Plan | 300 | 2-mana proliferate + card | keep |
| 4 | Prologue to Phyresis (if found) | ~400 | A whole route against the table | keep |
| 5 | Meticulous Excavation | 300 | The four-card loop; ETB reuse | keep |
| 6 | Trophy Mage | ~600 | Finds Relic, Surge Conductor, Insight Engine, Inspirit | keep |
| 7 | Tribute Mage | ~1,000 | Finds Talisman/Pentad early, Strionic Resonator (after F1), Overseer, Coretapper | keep |
| 8 | Talisman of Conviction | 1,500 | Turn-2 rock, Kilo on turn 3 | keep |
| 9 | Relic of Legends | 2,500 | Instant Kilo tap every round, fixing, the future Sinking Feeling infinite | keep |
| 10 | Command Tower | 900 | Untapped three-color land instead of a basic | **3rd** |
| 11 | Swords to Plowshares EN (for Ezio) | 2,500 | The best 1-mana answer | **2nd** (owned stand-in: Watery Grasp or Detained by Legionnaires) |
| 12 | Counterspell | ~2,500 | Third shield piece | **4th** (shield falls to Negate + Ripples) |
| 13 | Flux Channeler | ~2,600 | Proliferate per noncreature spell; dies to everything | **1st** (after F1 and F2 the deck has 13 doublers without it) |

Kilo all-in: 8,500 confirmed + about 7,100 to read = **about 15,600**, under the 18,000 envelope. My fixes cost 0. Cutting
Flux, Swords and Command Tower would free about 6,000 if the global order needs it, at about -0.1 to -0.2 real power.

## 7. Real power (scale: 4 = precon, 6 = upgraded deck, 7-8 = high power)

| List | Salt | Real power | Note |
|---|---|---|---|
| Precon Counter Intelligence | 3.8 | 4.0-4.5 | project estimate |
| Current list after purchases | 4.6 | 4.8-5.3 | project estimate |
| New list, all 13 buys arrive | not measured | **5.3-5.8** (builder 5.4-5.9) | no tutor to a finisher; the poison clock is 2-4 rounds |
| New list, the five unread buys fail (stand-ins) | | 5.0-5.4 | about the current list, for less money |
| **New list + F1, F2, F4**, all buys arrive | | **5.6-6.1** | Kilo's and Lux's triggers copied: Lux kills in two end steps, three to four proliferates a round |
| New list + F1, F2, F4, the unread buys fail | | 5.3-5.7 | still clearly above the current list |

Confidence: medium-low (no games played with any Kilo list).

## 8. Champion checklist (41 items)

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | One plan plus a backup | APPLIED | Plan sentence + Cyberdrive/Titan Forge backup reusing the artifact board |
| 2 | Synergy density | APPLIED | Every card counts in plan functions; 0 plan cards outside functions (gate) |
| 3 | Redundancy of key effects | APPLIED | 21 counter sources, 12 doublers, 4 routes |
| 4 | Multi-role slots | APPLIED | 47 of 62 nonland in two or more functions (build section 2) |
| 5 | Commander-centric balance | APPLIED | 3 of 62 blank without Kilo (limit 12) |
| 6 | Land count from curve and ramp | APPLIED | 37 lands, band 36-38, avg MV 2.89 |
| 7 | Colored sources | APPLIED | My count: U 19, W 16, R 16 land sources + 6 any-color rocks (not printed in the notes) |
| 8 | Total mana sources | APPLIED | 37 + 9 = 46, lands 80 % |
| 9 | Non-GC fast mana | APPLIED | Sol Ring, Arcane Signet, Talisman; Fellwar/Mind Stone no Spanish copy; Mox Opal over the price line |
| 10 | Tapped lands | APPLIED | 1 always-tapped land (Mystic Monastery) |
| 11 | Window mana and costs | APPLIED | Relic mana and Insight Engine/Bastion sinks at opponents' end steps |
| 12 | Curve by archetype | APPLIED | 2 / 7 / 15 / 23 / 10 / 2 / 1 / 2 by MV, affinity and improvise discounted |
| 13 | Commander MV and tax | APPLIED | MV 3 with haste: recast for 5 and tap at once (disrupted goldfish a) |
| 14 | Lands at higher power | APPLIED | 37 against the B4 average 35, justified by no fast mana and 4-5 mana sinks |
| 15 | Engines vs one-shots | APPLIED | Insight Engine, Uthros, Jhoira, Etched Oracle, Seedshark |
| 16 | Card advantage that scales | N/A | No Rhystic, Remora or Esper Sentinel owned in Spanish; all over 3,000 |
| 17 | Development before card advantage | APPLIED | Turn-2/3 draw is 2 mana (Augury, Contentious Plan); 4+ mana draws 3 |
| 18 | Tutors (10 access cards to the primary route) | **NOT APPLIED** | Trophy/Tribute Mage find engines, not Reactor or Lux; access about 6-8 cards (F9) |
| 19 | Cheap instant answers | APPLIED | 12 spot, 6 at MV 2 or less, 8 instants, 3 artifact and 3 enchantment answers |
| 20 | Counterspell count | APPLIED | 2 + Ripples for a tap-out engine deck |
| 21 | Wipes as a reset (asymmetry) | **NOT APPLIED** | Fumigate is symmetric in a 20-creature engine deck (F4) |
| 22 | Graveyard hate | APPLIED | Soul-Guide Lantern |
| 23 | Commander protection in layers | APPLIED | Airbending Lesson, Ripples, Inspirit 8+, two counters, cheap recast |
| 24 | Win-turn shield | APPLIED | Counterspell, Negate, Ripples, named and sequenced (conditional on Counterspell arriving) |
| 25 | Answers across permanent types | APPLIED | Creatures, artifacts, enchantments, planeswalkers (Fateful, Chaos Warp, Airbending, Lux Cannon) |
| 26 | Compact routes | APPLIED | Reactor is a repeatable board engine; Prologue one card; Lux one card |
| 27 | Two+ disjoint routes vs three opponents | APPLIED | Reactor, poison, Lux all hit the whole table |
| 28 | Failure points | APPLIED | Table in build section 1; no shared failure point; two routes work with Kilo dead |
| 29 | Threat assessment | APPLIED | Gauntlet and "what it fears" |
| 30 | Archenemy timing | APPLIED | Kilo taps at home at instant speed; never show a closer a turn before it can be protected |
| 31 | Politics | **NOT APPLIED** | No deal or gift guidance (Fateful's Clue, Chaos Warp, Starfall's gift, Peacemaker's crime trigger as a deterrent) |
| 32 | Wipe recovery | APPLIED | 6 rebuild pieces, commit rule written |
| 33 | Mulligan standard | APPLIED | Keep checklist written; 80.8 % under a stricter rule, 85.3 % under R33 (F8) |
| 34 | Game Changer slots | APPLIED | 0 of 3, each candidate priced; none owned or under 3,000 in Spanish (Narset to re-read, F9) |
| 35 | Efficiency over value | APPLIED | 5+ MV cards win, refill or answer many (Organic Extinction, Thought Monitor discounted) |
| 36 | Non-GC high-power cards | APPLIED | R36 list walked with reasons (build section 6) |
| 37 | Combos that break Bracket 3 | APPLIED | Scepter loop avoided; script PASS |
| 38 | Goldfish protocol | APPLIED | 20 hands, 5 goldfish, 3 disrupted games written |
| 39 | Gauntlet | APPLIED | Five opponent types with named answers |
| 40 | Cut process | **NOT APPLIED** | The final cut pass used a stale pool: Strionic Resonator, Lithoform Engine and Starfall Invocation (free) were never candidates (F1, F2, F4) |
| 41 | Real-game evidence over a score | APPLIED | Real-power estimate argued; Salt not chased |

**Count: 36 APPLIED, 4 NOT APPLIED (18, 21, 31, 40), 1 N/A (16).** Items 21 and 40 became F4 and F1/F2; item 18 is F9
(no affordable fix known today); item 31 is a guide note, no list change.

## 9. Verdict

**FIX**, ranked:
1. -Brute Suit, +Strionic Resonator (owned Spanish).
2. -Katara, Bending Prodigy, +Lithoform Engine (owned Spanish).
3. Before the order: browser-read the five unread buys at GoM and PTW; if Prologue has no Spanish copy, drop the poison route
   from the plan and keep Kappa Cannoneer.
4. -Fumigate, +Starfall Invocation (owned Spanish).
5. Notes F5 to F10 in the build notes (saved Rivendel read, Spanish Command Tower at PTW, plan sentence, R33 keep rate,
   watch list Narset/Fabricate/Whir, Cyberdrive mana).

Is it champion-level for this collection and this budget? With the fixes, yes for the engine and the closers: every
engine the Spanish binder holds is in, the mana is clean and the interaction meets the champion counts. It stays a 5.5-6
deck because the strongest Kilo lines (Freed from the Real or Pemmin's Aura combos, Walking Ballista, Enlightened Tutor,
Rhystic/Esper Sentinel) have no Spanish copy under 3,000; that ceiling is the budget and the language rule, not the build.
