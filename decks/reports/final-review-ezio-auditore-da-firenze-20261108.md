# Final review: Ezio Auditore da Firenze, budget rebuild (Phase 2 step 7.7, 2026-11-08)

Reviewer: independent champion review under `docs/proposals/final-rebuild-brief-20261108.md` (corrected budget section: Ezio
envelope 34,000 CLP all-in, every buy under 3,000 CLP, loans under `decks/phase2/loans.md`). The list reviewed is the budget
rebuild in `decks/phase2/ezio-auditore-da-firenze.txt` (files of 2026-11-08 18:26-18:30), with its `.plan.json` and `.build.md`
(builder total 33,557 CLP). The earlier "no cap" version (217,547 CLP) is void and not reviewed.

**Verdict: FIX** (no blocker; four fixes, ranked below). With the fixes the list is the strongest this collection and this
budget allow that I could find, and it is clearly stronger than the current list.

---

## 1. Rules

| Check | Result | Evidence |
|---|---|---|
| `python scripts/check_phase2_bracket.py decks/phase2/ezio-auditore-da-firenze.txt` | **PASS** (floor 3, target 3, Game Changers 0, review items 0) | run 2026-11-08 by the reviewer |
| `python scripts/plan_density.py` | **PASS**, 0 failures, 2 warnings (team_evasion 3 of 6; 35 lands vs 36-38) | run 2026-11-08; both warnings have a written reason in build.md section 3 |
| 100 cards | 100 (1 commander + 99) | counted by script |
| Game Changers | 0 | bracket script, Oracle cache flags |
| Early two-card infinite | none. Spellbook cache: the only line fully inside the list is Ezio + Magister Sphinx (one-player kill, not infinite, late). Ezio + Ramses is not a Spellbook line and is not infinite | `data/cache/spellbook_variants_slim.jsonl.gz`, 1 match |
| Reversible cards | none (all layouts `normal`) | Oracle cache |
| Language | OK. Every card owned in both languages plays an English copy; Spanish-only cards (Brotherhood Spy, Hookblade Veteran, Hookblade, Harlequin, Restart Sequence, Gauntlet, Ezio Blade, several lands) are owned only in Spanish | pool `by_language` |
| Owned or bought | OK. Every non-buy card is in the pool with a copy for this deck; buys: Ramses, Altaïr, Fellwar, Talisman of Progress, Orzhov Signet, Golgari Signet, Battlefield Forge, Rogue's Passage (+ Swords EN, Command Tower booked to Kilo); loans: Eagle Vision, Bayek, Layla, Footblade, Slasher, Basim, Aya, Eivor | pool check script |
| **Loan rule (Eivor)** | **FAIL of `loans.md` rule 3**: Eivor's replacement is 5,400 (TO EVALUATE) and the owner has not accepted it, yet the .txt plays Eivor. Until he accepts, or a live variant under 5,000 is read (then it is automatic), the list must play the fallback Kaya, Ghost Assassin | `decks/phase2/loans.md` rule 3; build.md section 7 |
| Ramses fallback | **The build notes' claim "the gate passes either way" is false.** With Rooftop Assassin for Ramses the gate FAILS: team_finishers 5 of 6, and Rooftop has no tag | scratch run of both scripts (reviewer) |

Gate runs of the variants (scratch copies, both scripts):
| Variant | Gate | Bracket |
|---|---|---|
| Eivor -> Kaya | PASS (2 warnings) | PASS |
| Ramses -> Rooftop Assassin | **FAIL** (team_finishers 5 of 6; untagged card) | PASS |
| Eivor -> Kaya and Ramses -> Fire Nation's Conquest (owned, team +1/+0, tagged team finisher) | PASS | PASS |
| The reviewer's fixed list (section 6) | PASS (2 warnings) | PASS |

## 2. Facts

### Ramses (Oracle, cache and Scryfall text)
"Deathtouch. Other Assassins you control get +1/+1. Whenever a player loses the game, if they were attacked this turn by an
Assassin you controlled, you win the game." {2}{U}{B}, 4/4. Not a Game Changer.

Conditions, all confirmed by the text:
1. Ramses must be on the battlefield when the player loses. Cast it the turn before (it is a lord anyway).
2. The losing player must have been attacked THIS turn by an Assassin I controlled. So it works on my turn (or an extra
   combat), not on an opponent's turn: a Shao Jun ping that kills on an opponent's turn does not win.
3. Any cause of loss counts once that player was attacked: Ezio's {W}{U}{B}{R}{G} trigger, combat damage, Slasher's halving
   plus damage, Eivor's attack trigger or Kaya's drain on my turn. Eivor damages EACH opponent: an opponent who was not
   attacked by an Assassin that turn and dies to it does NOT win the game. Play rule for the guide: on the kill turn, attack
   every opponent with at least one Assassin (a token is enough).
4. It is a trigger: Stifle-type effects and "you can't win" or "can't lose" permanents stop it.
5. Verdict: yes, one elimination on my turn becomes a table win. The build notes describe it correctly, except point 3.

### Etrata, the Silencer: misread (fix the notes)
Oracle: after each hit, "Etrata's owner shuffles Etrata into their library". Without Mari (no longer in the list) and with no
copiers, the "third hit counter" loss is not a real line: Etrata leaves after every hit. Etrata is a 4-mana unblockable
removal spell on a body ({B}{B} after a hit) and turns freerunning on; she is NOT a closer. Route 1's closers are Ramses,
Magister Sphinx and Unstoppable Slasher (+ Ezio). This changes no card (Etrata is still worth her slot), but the route text,
the access count (10 claimed) and the "Etrata + Ramses" wins in build.md sections 1, 2 and the plan file are wrong.

### Real access to Ramses (it decides the power estimate)
Loyal Inventor and Reckless Handling find artifacts (Sphinx), not Ramses. The cards that put Ramses in hand or play are:
Ramses itself, Adéwalé (6 cards deep: about 7 % to hit Ramses), and Entomb plus a recursion card (Restart, Layla, Jacob,
Altaïr). P(Ramses in the first 14 cards) = 14 %; about 20 % by turn 10. So in most games the deck wins by eliminating
players one by one, and the builder's "+6" for Ramses and 7.1-7.6 estimate are too high. One real tutor doubles the odds
(two cards with access: 26 % by turn 7, 36 % by turn 10). See fix F3.

### Other key Oracle checks (all match the notes unless said)
Eivor (damage = Equipment count to each opponent on attack; haste, vigilance), Kaya (-1: each opponent loses 2), Basim (draw +
unblockable on the first historic spell each turn), Hakoda (sacrifice: team +0/+5 and indestructible, no mana), Adéwalé (dig 6
for an Assassin; the Vehicle clause is dead), Lion Vulture (end-step draw if an opponent lost life), Bayek (other historic
creatures have double strike on my turn), Jacob Frye (the copy is cast, so its cost is paid; freerunning cost allowed as an
alternative cost), Unstoppable Slasher (halves on hit; returns once). Ezio + Magister Sphinx is the only Spellbook combo.

### Prices (reading files and a live search read by the reviewer, 2026-11-08)
Product JSON answered HTTP 429 (as the builder found), so variants and stock per variant are **to read** by the lead. The
store search (`/search/suggest.json`, read 2026-11-08) shows price range and availability per product; the range's low end
is often a damaged variant (project pitfall), the high end the NM price.

| Card | Builder hint | Evidence | Status |
|---|---|---|---|
| Ramses, Assassin Lord | 2,990 cap | PayToWin DMC 1,600-3,500, available; etched 1,600-2,600 sold out; Game of Magic 1,920-3,360 sold out | **to read**: buy only a variant under 3,000 |
| Basim Ibn Ishaq (loan) | 3,400 | Game of Magic 1,920-3,400 available; PayToWin 1,600-3,700 available | to read; an LP may be well under 3,400 |
| Eivor, Battle-Ready (loan) | 5,400 | PayToWin 3,100-5,400 available | to read; an LP under 5,000 makes it automatic |
| Aya of Alexandria (loan) | 915 | Game of Magic 549-915 available | OK |
| Altaïr Ibn-La'Ahad | 2,080 | Game of Magic 1,080-2,080 available | OK |
| Talisman of Progress | 1,500 | Game of Magic 445-1,500 available | OK |
| Orzhov Signet | 1,240 | Game of Magic 342-1,240 available | OK |
| Fellwar Stone | 1,560 | `browser-paytowin-20261107-wishlist.psv` NM 1,560 | reading 1 day old: re-read |
| Golgari Signet, Battlefield Forge, Eagle Vision, Bayek, Layla, Slasher | 570, 915, 742, 2,320, 915, 5,560 | `browser-gameofmagic-20261108-order.psv` | OK |
| Rogue's Passage, Hidden Footblade | 1,440, 1,440 | `browser-paytowin-20261108-order.psv` (LP) | OK |
| Assassin token TACR 4 | 570 | purchase order line 17 | OK |

Alternatives read live (for the money section): Cover of Darkness Game of Magic 4,760-12,240, PayToWin 5,600-14,700; Achilles
Game of Magic 5,160-8,680 (PayToWin none); Counterspell Game of Magic CMM 2,520-7,220, PayToWin MH2 2,700-4,400; Arcane Denial
none in stock; Smoke Bomb Game of Magic 445-742; **Diabolic Tutor PayToWin 1,200-7,400 (four printings available)**; Whispersilk
Cloak Game of Magic 2,200-3,640; Mari PayToWin 3,200-7,200; Massacre Girl, Known Killer PayToWin 1,840-7,300; Lightning Greaves
5,080+; Beseech the Queen 2,900+; Sorin Markov 4,700+.

## 3. Strength

### Plan and routes
The plan is right for this commander and this pool: cheap evasive Assassins connect from turn 2-3, freerunning makes the 4-5
drops cost {B}{B}, hit-based draw (Basim, Ezio Blade, Coastal Piracy, Etrata DF, Jacob, Eagle Vision, Lion Vulture, BMC)
keeps cards flowing, and the kill is Ezio's trigger on a player at 10 or less, made a table win by Ramses. Three routes with
no shared failure point (Ezio dead: routes 2-3; wipe: Hakoda, Get Out, recursion; counter: recursion). Weak point: route 1's
TABLE win needs Ramses, which the deck sees in about 1 game in 7 by turn 7 (section 2). Without him, each elimination
removes one player and the deck must repeat it, which works (Slasher, Sphinx, focused evasive damage) but is slower.

### Curve and mana
35 lands, 9 rocks + BMC, average MV 2.80, 29 cards at MV 2 or less. Freerunning makes the effective curve lower than printed.
Accepted: Bracket 4 lists of this commander run 33 lands, and the keep rate (19 of 20 with the free mulligan) is good. The
payment needs five colors: green has 13 sources, the minimum for one G pip. Utility lands: Abstergo, Secret Tunnel,
Brotherhood Headquarters (Assassin-only colors), Rogue's Passage and the tapped Path of Ancestry are five lands that do not
pay {W}{U}{B}{R}{G} freely; Rogue's Passage is also the weakest (its 4-mana activation on the kill turn means 9 mana with
the payment, while the deck has three flying Equipment for 1-2). Cutting it for a ninth Swamp (fix F4) improves the mana.

### Interaction and protection
Spot answers 10: Swords, Infernal Grasp, Bitter Triumph, Terminate, Assassin's Trophy, Chaos Warp, Kolaghan's Command, Feed
the Swarm, Mana Leak, Get Out; 8 at MV 2 or less, 9 instants. Artifacts: Trophy, Chaos Warp, K-Command; enchantments: Trophy,
Chaos Warp, Feed, Get Out. Meets R19. Protection: Boots, Thopteryx (ward on all legends), Haystack, Hakoda, Get Out, Mana Leak,
Enter the Avatar State. Win-turn shield (R24): Get Out, Enter the Avatar State, Haystack, Mana Leak, Boots: met, but Mana Leak
is soft late. No Game Changer is affordable that beats its slot; leaving the three slots empty is correct here.

### The weakest 10 cards (reviewer's list) and the best replacement this pool and budget allow
| # | Card | Problem | Best option | Verdict |
|---|---|---|---|---|
| 1 | Reckless Handling | artifact tutor only (Sphinx, Boots); random discard; sorcery | **Diabolic Tutor** (buy, PayToWin, to read, must be under 3,000): any card, so Ramses | **REPLACE (F3)** |
| 2 | Kitesail | equip {2} | **Cobbled Wings** (owned free, equip {1}, flying; also an Equipment for Eivor) | **REPLACE (F5, 0 CLP)** |
| 3 | Rogue's Passage (buy 1,440) | colorless, 4-mana activation, bought | 9th Swamp (owned) | **REPLACE (F4, saves 1,440)** |
| 4 | Mana Leak | soft counter, weak late | Counterspell only if a variant under 3,000 is read (Game of Magic CMM, low end 2,520); Arcane Denial has no stock | keep; swap if Counterspell under 3,000 is found |
| 5 | Feed the Swarm | sorcery, life loss | Mortify (owned free, instant, creature or enchantment, 3 MV) | optional (note): R19 still met either way |
| 6 | Hookblade | flying only on my turn, equip {2} | Smoke Bomb (742, Game of Magic): flash shroud for all creatures against the removal on Ezio or Ramses, then one attacker unblockable on the kill turn | optional, first add if money frees |
| 7 | Lion Vulture | 4-mana 2/2, not an Assassin without Roshan | nothing owned or under 3,000 does more for the slot | keep |
| 8 | Mephitic Vapors | symmetric, kills my tokens too | the only cheap answer to 1/1 chump boards besides Gauntlet | keep |
| 9 | Merciless Harlequin | small body | Brotherhood Patriarch, Darkblade Agent (owned) are worse | keep |
| 10 | Rakdos Signet | plain rock | Everflowing Chalice (owned) is colorless | keep |

### Against the current list and iteration 1
| List | Real power (1-10, reviewer) | Why |
|---|---|---|
| Iteration 1 (`round5-step40`, Salt 7.7, lost real games) | 6.4-6.9 | mini-combos (Etrata copiers, Dualcaster), tapped lands, no haste, no answer to chump boards |
| Current after purchases (Salt 6.6) | 6.6-7.1 | Cover of Darkness and Achilles, but 3-4 mana rocks and answers, no table kill |
| **This list as built** (Eivor, Ramses) | **6.9-7.4** | Ramses (when drawn), Basim, cheaper rocks, Hakoda, Eivor; loses team fear and Achilles |
| **This list with the fixes** (Kaya until Eivor is accepted, Diabolic Tutor, Wings, 9th Swamp) | **7.0-7.5** | Ramses access doubled; 2-mana rocks; same answers |
| Fixed list without Ramses (no variant under 3,000) | 6.8-7.2 | route 1 back to one player per elimination |

The builder's 7.1-7.6 is about 0.2 high because Ramses is counted as if drawn most games. Confidence medium-low (no games,
no Salt yet). In a real 4-player game the fixed list is clearly stronger than iteration 1 (consistency, haste, answers,
defense while tapped) and moderately stronger than the current list (the table win, cheaper mana and draw), with the risk
that chump boards of black or artifact creatures now meet 3 team-evasion pieces instead of 4.

## 4. Money

### Dropped loans: right?
- **Cover of Darkness** (replacement 10,600 NM; live low ends 4,760-5,600 are probably damaged copies): 31 % of the envelope
  for one card that fails against black and artifact blockers. Right to drop. The same money buys Ramses + Basim + Bayek +
  the three 2-mana rocks. It stays the first card to add if money appears, and the owner should confirm the drop (he calls it
  a proven role-player).
- **Achilles Davenport** (8,680 Spanish NM; no PayToWin stock): a second +1/+1 lord next to Ramses and Arno. Right to drop.
- No better use of the same CLP exists inside the 3,000 rule: the alternatives are worse or blocked by the rule (Mari 3,200+,
  Whispersilk 3,640 NM, Greaves 5,080+, Sorin Markov 4,700+).

### Ranked buys and loans by gain per CLP
Gain is reviewer judgment [J], points of win rate in a 4-player pod, only to rank. "Cut order" = what to cut first if the
global 90,000 target needs room (1 = first).

| Rank | Card | Kind | CLP | Gain [J] | Gain per 10k | Verdict | Cut order |
|---|---|---|---|---|---|---|---|
| 1 | Ramses, Assassin Lord | buy (under 3,000 only) | 2,990 cap | +4.0 (table win when drawn; lord; deathtouch) | 13.4 | **KEEP** | never |
| 2 | Eagle Vision | loan | 742 | +0.8 | 10.8 | KEEP | 13 |
| 3 | Aya of Alexandria | loan | 915 | +0.7 | 7.7 | KEEP | 12 |
| 4 | Layla Hassan | loan | 915 | +0.7 | 7.7 | KEEP | 11 |
| 5 | Golgari Signet | buy | 570 | +0.3 | 5.3 | KEEP | 10 |
| 6 | Basim Ibn Ishaq | loan | 3,400 (LP may be ~2,000) | +1.5 | 4.4 | KEEP | 9 |
| 7 | Bayek of Siwa | loan | 2,320 | +1.0 | 4.3 | KEEP | 8 |
| 8 | **Diabolic Tutor** (new) | buy (under 3,000 only) | about 1,200-2,990, to read | +0.8 (Ramses access x2) | 4.0 | **ADD (F3)** | 7 |
| 9 | Talisman of Progress | buy | 1,500 | +0.5 | 3.3 | KEEP | 6 |
| 10 | Fellwar Stone | buy | 1,560 | +0.5 | 3.2 | KEEP | 6 |
| 11 | Orzhov Signet | buy | 1,240 | +0.35 (over Everflowing Chalice, owned) | 2.8 | KEEP | 4 (-> Everflowing Chalice) |
| 12 | Hidden Footblade | loan | 1,440 | +0.4 (haste 5; 4 without it, still at min) | 2.8 | KEEP | 5 |
| 13 | Battlefield Forge | buy | 915 | +0.25 | 2.7 | KEEP | 5 |
| 14 | Altaïr Ibn-La'Ahad | buy | 2,080 | +0.4 (over Lydia Frye, owned) | 1.9 | KEEP | 3 (-> Lydia Frye) |
| 15 | Unstoppable Slasher | loan (accepted) | 5,560 | +1.0 | 1.8 | KEEP | 4b, after Altaïr and Orzhov |
| 16 | Eivor, Battle-Ready | loan (TO EVALUATE) | 5,400 (LP under 5,000 = automatic) | +0.8 over Kaya | 1.5 | **Kaya plays until accepted (F1)**; accept only if an LP under 5,000 is read | 1 (-> Kaya) |
| 17 | Rogue's Passage | buy | 1,440 | +0.2 | 1.4 | **CUT (F4)** -> 9th Swamp | 2 |
| - | Assassin token (TACR 4) | token | 570 | required (Ratonhnhaké꞉ton, Aya) | - | KEEP (Aya makes several: markers for the rest) | never |
| - | Swords EN, Command Tower EN | booked to Kilo | 2,500, 900 | language swap with Kilo | - | KEEP (lead) | - |

Totals (price hints; Ramses at its cap):
| List | Ezio all-in CLP |
|---|---|
| As built | 33,557 |
| With the fixes, Eivor not accepted (Kaya), Diabolic Tutor at its 2,990 cap | 29,707 (34,000 envelope: 4,293 left) |
| With the fixes and Eivor accepted at 5,400 | 35,107 (1,107 over the envelope) |
| Room the cut order frees, steps 1-4 (Eivor, Passage, Altaïr, Orzhov) | 10,160 |

## 5. Findings (ranked)

| # | Severity | Finding | Exact change |
|---|---|---|---|
| F1 | **fix** (rules) | Eivor is a TO EVALUATE loan (5,400) not yet accepted; `loans.md` rule 3 says the list plays the fallback | In `ezio-auditore-da-firenze.txt`: `1 Eivor, Battle-Ready` -> `1 Kaya, Ghost Assassin`; in the plan file rename Eivor to Kaya in every function (team_finishers, condition_enablers, through_wide_board, through_big_creatures, attackers, haste, defense_while_tapped). Eivor goes back in only when the owner accepts, or automatically if the lead reads a variant under 5,000 live. Gate PASS checked |
| F2 | **fix** (false claim) | The Ramses fallback Rooftop Assassin fails the gate (team_finishers 5 of 6, untagged) | Fallback ladder in build.md section 6: if no Ramses under 3,000 is live, play Kaya, Ghost Assassin in Ramses's slot when Eivor plays; when Kaya already holds Eivor's slot, play Fire Nation's Conquest (owned free, team +1/+0, tagged team finisher). Both variants checked PASS. Or ask the owner for a one-card exception (money question 1) |
| F3 | **fix** (strength) | Only Ramses itself and a 7 % Adéwalé dig reach the table win; Reckless Handling cannot find a creature | `1 Reckless Handling` -> `1 Diabolic Tutor` (PayToWin, four printings available 1,200-7,400; buy only a variant under 3,000; Reckless Handling plays until it arrives). Plan file: tutors entry `Diabolic Tutor` for condition_enablers, team_finishers, through_big_creatures, through_wide_board. Checked PASS |
| F4 | **fix** (money and mana) | Rogue's Passage is a 1,440 buy of a colorless land whose activation costs 4 on the turn the deck also needs {W}{U}{B}{R}{G} | `1 Rogue's Passage` -> ninth Swamp (`8 Swamp` -> `9 Swamp`); drop the order line (PayToWin 1,440). Checked PASS |
| F5 | note (free upgrade) | Kitesail equips for {2}; the owned Cobbled Wings gives flying for equip {1} | `1 Kitesail` -> `1 Cobbled Wings` (owned, 2 free English copies). Checked PASS |
| F6 | note (documentation) | Etrata, the Silencer shuffles herself away after each hit: the "third hit counter" elimination is not a line without Mari | Rewrite route 1 in build.md and `win_routes` in the plan file: closers Ramses, Sphinx, Slasher; Etrata is removal on an unblockable body. Access to route 1 is 4-5 cards plus Diabolic Tutor, not 10 |
| F7 | note (play guide) | Ramses wins only for players attacked this turn by an Assassin | Guide line: on the kill turn attack every opponent with at least one Assassin before Eivor's or Kaya's damage |
| F8 | note (power estimate) | 7.1-7.6 assumes Ramses most games | Write 7.0-7.5 with the fixes (6.8-7.2 without Ramses) |
| F9 | note (optional swaps, 0 to 742 CLP) | Feed the Swarm is a sorcery; Hookblade is the weakest Equipment | Feed the Swarm -> Mortify (owned free, instant); Hookblade -> Smoke Bomb (742, Game of Magic) if the envelope has room. Not required |
| F10 | note (scarce copies, lead) | BMC claimed from Azula, Hakoda from Toph (pool shows Hakoda free); Rogue's Passage and Battlefield Forge also have owned copies held by Toph and Azula | Lead resolves when Azula and Toph are rebuilt; F4 removes the Passage question |
| F11 | note (tokens) | Aya makes a menace Assassin token on every historic hit; one bought token (TACR 4) plus markers. Queen Marchesa's deathtouch-haste token: no stock (marker) | none |

## 6. The fixed list in one line
As built, with: Eivor -> Kaya (until accepted), Reckless Handling -> Diabolic Tutor, Rogue's Passage -> Swamp (9 Swamps),
Kitesail -> Cobbled Wings. 100 cards; bracket PASS (0 Game Changers); gate PASS (2 warnings with reasons). About 29,700 CLP
all-in (Ramses and Diabolic Tutor at their 2,990 caps).

## 7. Money questions for the owner
1. **Ramses** is the biggest gain per CLP of the whole deck. If no variant under 3,000 is in stock live (PayToWin NM showed
   3,500; Game of Magic sold out), is a one-card exception of about 500 CLP over the rule acceptable? Without Ramses the
   list loses about 0.3 real power and the table win.
2. **Eivor** (5,400 NM, to evaluate): accept it, or keep Kaya and save 5,400? Reviewer: keep Kaya unless an LP under 5,000
   is read (then it is automatic and worth it).
3. **Cover of Darkness** (his proven role-player, 10,600): confirm the drop. **Unstoppable Slasher** (5,560, accepted) is
   now the most expensive line; keep it, but it is the next cut after Eivor, Rogue's Passage, Altaïr and Orzhov Signet if the
   global 90,000 target needs room.

## 8. Champion level?
For this collection and this budget: yes, after the fixes. The structure is what Bracket 4 Ezio lists run (Sol Ring, Arcane
Signet, Fellwar, Basim, Ezio Blade, Bayek, Ramses, Aya, Altaïr, Layla, Arno, Queen, BMC, Swords, Trophy), minus the cards the
3,000 rule excludes (Cover of Darkness, Regalia, Greaves, Mari, Mox Amber, the Game Changer tutors and Fierce
Guardianship). What keeps it below 7.5: one real tutor, no fast mana beyond Sol Ring, three team-evasion pieces, and a table
win that depends on one 4-drop.
