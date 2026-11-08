# Ezio Auditore da Firenze: Phase 2 build notes (2026-11-07, step 6)

**Step 6.** The step-4 list scored 5.4 on Commander Salt (`decks/reports/salt-ezio-auditore-da-firenze-20261107.md`): Win
conditions 81/200, "Casual stall shell, no clear win path" (no combos, fast mana 12, tutors 8), one wipe, few counters, light
draw. Owner standard (2026-11-07): consistent, robust and as powerful as possible, a clear fast win path; Salt floor 6.0.
Checks rerun 2026-11-07: `plan_density.py` PASS (0 failures; warnings team_evasion 4 of 6, ramp 7 of 10), `check_phase2_bracket.py`
PASS (floor 3: Ezio + Magister Sphinx, a commander-plus-one-card kill, late; 0 Game Changers; no infinite), `assign_copies.py`
100 of 100, 0 missing, 0 problems. Every new card is a free copy (Restart Sequence and Merciless Harlequin are Spanish-only).

**The win path now (one plan, a compact kill on top):** Magister Sphinx sets one opponent to 10; Ezio connects (Equipment,
Cover of Darkness, Secret Tunnel, Angelic Intervention) and pays {W}{U}{B}{R}{G}: that player is out. The Sphinx comes back for
the next opponent (Kaya's 0 blinks it to my next upkeep, What Must Be Done's Release Juno, Restart Sequence, Layla returns it
to hand, Kolaghan's Command returns it), while the team damage (Arno, Achilles, Bayek, Rally, Unstoppable Slasher, Shao Jun,
Kaya) brings the others to 10 by itself. Finders: Loyal Inventor and Reckless Handling (artifact tutors; the Sphinx is an
artifact), Entomb (to the yard, then Restart Sequence for {1}{B} after a hit, What Must Be Done or Layla). With Roshan out
every creature is an Assassin, so the Sphinx (and Lion Vulture, Haytham, Thopteryx, Inventor) cost {B}{B} after a hit.
Each piece works alone: the Sphinx is a 5/5 flier that resets the leader; Roshan a 4/4 that makes every spell cheaper;
Reckless Handling finds Boots or Lantern and pings each opponent for 2 when it bins an artifact; Entomb feeds Layla, Jacob and
the reanimators; What Must Be Done is the second wipe.

| Out | In | Reason |
|---|---|---|
| Aven Heartstabber | Magister Sphinx | The kill setter: one card turns an opponent's life into 10 |
| Assassin Initiate | Roshan, Hidden Magister | Freerunning {B}{B} for every creature, the Sphinx included; a 4/4 body; Brotherhood HQ mana for all |
| Vindictive Warden | Reckless Handling | Tutor for the Sphinx, Boots, Lantern or an Equipment; team_finishers back to 6 (the minimum: the Sphinx line is the closer now) |
| Theater of Horrors | Entomb | 1-mana tutor into the reanimators and Layla |
| Royal Assassin | Restart Sequence | Reanimates the Sphinx, Ezio Blade or Bayek for {1}{B} after a hit |
| Hidden Blade | What Must Be Done | Second wipe (Salt: one wipe too thin) or Sphinx recursion; a reset when Board 2 runs away |
| Octopus Form | Mana Leak | A counter that also stops a wrath early (Salt: counterspell coverage light); still commander protection |
| Winter Soldier, Icy Assassin | Merciless Harlequin | A 2-for-1 Assassin (body + card) for {B}{B} or {1}{B} after a hit (draw) |

Counts: tutors 3 (Loyal Inventor, Reckless Handling, Entomb) + Evie fetching Jacob; draw 11 tags, about 9.5 weighted;
spot answers 9 (Mana Leak included), wipes 2; commander protection 7; haste 5; through_wide_board 17 (10 pass Ezio himself);
attackers 19; average MV 2.94; toughness 2 or less among attackers 6 of 20 with Ezio (Evie, Harlequin, Jacob, Lydia, Lion Vulture).

Salt estimate (mine, to be measured): 6.0 to 6.5. Gains: a detected combo (Ezio + Sphinx), tutor score up (3 tutors), two
wipes, a counter; costs: average MV up 0.2, the 7-drop.

### Purchases inside Ezio's about 2,300 CLP (readings of 2026-11-07)
| # | Card | Store, price | Replaces | Gain |
|---|---|---|---|---|
| 1 | Golgari Signet | Game of Magic Singles, 570 | Deathcap Cultivator | Turn-2 rock, {B}{G} for freerunning and the kill |
| 2 | Mind Stone | Game of Magic Singles, 742 | Boros Locket | Turn-2 rock instead of a turn-3 one |
| 3 | Battlefield Forge | Game of Magic Singles, 915 | Clifftop Retreat | Untapped red and white |
Total 2,227 CLP, one store.

### Strong buys over the cap (owner rule 2026-11-07: price and expected gain, he may extend the cap)
| Card | Price | Replaces | Expected gain [J] |
|---|---|---|---|
| Arcane Denial | Tienda La Comarca 3,950 | Get Out | A 2-mana hard counter for wraths and removal; +0.1 to 0.2 Salt |
| Bloodletter of Aclazotz | price to read | Rally the Peasants | Doubles every opponent's life loss on my turn: 40 to 10 in one or two swings; a team finisher and a combo with Unstoppable Slasher; the biggest single gain, +0.3 to 0.5 |
| Wound Reflection | price to read | Rally the Peasants | Each opponent loses again what they lost this turn: the team finisher the deck lacks; combo with the Sphinx and with Slasher |
| Sorin Markov | price to read | Glider Staff | A second "life becomes 10" piece with Ezio (Spellbook combo); a second kill line, +0.2 to 0.3 |
| Brotherhood Regalia | price to read | Hookblade | Ezio unblockable every turn: the kill connects through any board |
| Mox Amber | price to read | Boros Locket | Free mana with 20 legends: fast mana score up |
| Enlightened Tutor (Game Changer) | price to read | Get Out | Finds the Sphinx, Boots, Lantern or Cover; +0.2 to 0.4 |
| Demonic or Vampiric Tutor (Game Changers) | price to read | Rally the Peasants | Any piece of the kill on demand; +0.3 each |
| Teferi's Protection (Game Changer) | price to read | Get Out | Team-wide wrath answer |
| Smothering Tithe (Game Changer) | price to read | Boros Locket | Treasure for the five-color payment |
| Lightning Greaves | PayToWin 9,900 | Haystack | A second hexproof + haste Equipment |

Earlier rounds below.

## Step 4 header (2026-11-07)

**Step 4** (round-3 re-review R3-1 to R3-6 in `decks/reports/review-ezio-auditore-da-firenze.md`, verdict PASS; owner rule
2026-11-07: Bracket 3 power or higher inside the Bracket 3 rules, built as a competitive expert would). Checks rerun
2026-11-07: `plan_density.py` PASS (0 failures; warnings team_evasion 4 of 6, ramp 7 of 10), `check_phase2_bracket.py` PASS
(floor 1, 0 Game Changers), `assign_copies.py` 100 of 100 covered, 0 missing, 0 problems.

| Change | Reason |
|---|---|
| Restart Sequence -> Vindictive Warden (free English copy) | R3-2: team_finishers 6 -> 7 (margin over the minimum), the non-combat route back to 3 cards (Shao Jun, Warden, Kaya: 41 % by T7 instead of 26 %). Restart Sequence was bad early (empty yard) and wipe insurance stays at 5 (Revelations III, Layla, Get Out, Haystack, Kolaghan's Command; min 2) |
| Boros Guildmage AND Unstoppable Slasher both stay | R3-1, settled by the owner 2026-11-07: Slasher never had to replace Guildmage. Both on merit: Guildmage is one of 4 haste granters for a recast Ezio, Slasher the fastest way to the 10-life threshold |
| Hidden Footblade removed from through_big_creatures in the plan file | R3-5: its first strike +1/+0 does not beat a bigger blocker; it is a haste card. through_big_creatures is 16, above 10 |
| Build text | R3-4 fixed below: haste 5, 3 battle lands, 15 basics, protection 7, wipe insurance 5, payment enablers 8, Coastal Piracy timing |

Counts after step 4: haste 5 (Swiftfoot Boots, Haunted Cloak, Hidden Footblade, Boros Guildmage, Queen Marchesa self; 4
granters reach a recast Ezio, plus Loyal Inventor); evasion: through_wide_board 17 pieces, 10 that pass Ezio himself, team
evasion 4 (one repeatable team card, Cover of Darkness; the pool has no other); commander protection 7; team finishers 7;
lands 36 with about 7 entering tapped on turns 1 to 4.

### Competitive-expert pass (principle 7)

- **Game Changers: 0 used, 3 slots open.** Live Scryfall `is:gamechanger` search 2026-11-07: 53 cards. The two owned ones
  (Crop Rotation, Drannith Magistrate) are Toph's and off-plan here. Wished, all "price to read" (none is in the 2026-11-07
  readings; USD hints from Scryfall put each far above the about 2,300 CLP left for Ezio):
  1. **Teferi's Protection**, replaces Get Out: the only team-wide answer to a wrath and to a lethal crack-back.
  2. **Smothering Tithe**, replaces Boros Locket: ramp and treasure for the {W}{U}{B}{R}{G} payment.
  3. **Fierce Guardianship** (free counter while Ezio is out), replaces Octopus Form.
  Then Enlightened Tutor (Cover of Darkness, Swiftfoot Boots, Chromatic Lantern) and Vampiric or Demonic Tutor if a slot opens.
  Cheap Game Changers (Notion Thief, Narset) were considered and left out: they do not serve an attack plan.
- **Fast mana that is not a Game Changer:** Sol Ring, Arcane Signet, Rakdos Signet in; Golgari Signet and Mind Stone are the
  purchase wishes below. Mana Vault, Grim Monolith and Chrome Mox are Game Changers and out of reach.
- **Cheap interaction:** 1- and 2-mana answers: Swords, Infernal Grasp, Terminate, Assassin's Trophy, Kolaghan's Command,
  Octopus Form, Angelic Intervention, Enter the Avatar State. Fatal Push and Mana Leak (free) were weighed against Rally
  the Peasants and Octopus Form and left out: the finishers and protection are at or near their minimums.
- **Tutors:** only Loyal Inventor (any artifact). Owned tutors that were cut (Entomb, Mystical Teachings, Reckless Handling)
  do not reach the win lines of this plan; the Game Changer tutors above would.

### Purchases (Game of Magic Singles, PayToWin, Tienda La Comarca; readings of 2026-11-07; about 2,300 CLP for Ezio)

Ranked by impact; the list plays the fallback until the card arrives:
| # | Card | Store, price | Replaces (fallback in the list) | Why |
|---|---|---|---|---|
| 1 | Golgari Signet | Game of Magic Singles, 570 (NM EN) | Boros Locket | Turn-2 rock instead of a turn-3 one; {B}{G}: black pays freerunning, green is the kill's thinnest color |
| 2 | Battlefield Forge | Game of Magic Singles, 915 (NM EN) | Clifftop Retreat | Untapped red and white every turn (Clifftop has 4 enablers); tempo and Salt's Manabase Quality |
| 3 | Mind Stone | Game of Magic Singles, 742 (NM EN) | Deathcap Cultivator | A turn-2 rock that needs no green; draws late |
Total 2,227 CLP, one store. Next if money appears: Arcane Denial (Tienda La Comarca 3,950) for Get Out; Llanowar Wastes
(Game of Magic Singles 1,320 LP) for Jungle Shrine; Rogue's Passage (PayToWin 1,440) for Rumble Arena. The English Command
Tower bought for Ezio (PayToWin 900) is charged to Kilo; until it arrives Ezio keeps the Spanish copy the assignment gives it.

Earlier rounds below.

## Round 3 header (2026-11-02)

**Round 3** (adversarial review `decks/reports/review-ezio-auditore-da-firenze.md`, verdict PASS with changes; owner
decisions 2026-11-02; every new card is a free English copy in `data/model/phase2/assignment.json`, 0 decks using it):

| Out | In | Reason |
|---|---|---|
| Bleeding Effect | Lion Vulture | Bleeding did nothing alone and its flying needed one of 2 fliers in the yard (L7); Vulture is a flier (Board 1) that draws every end step an opponent lost life, the deck's own main action; net draw 8.5 -> about 9.5 |
| Hookblade Veteran | Angelic Intervention | A 1-power body, bad late, out; commander protection 6 -> 7 and one more way for Ezio himself to pass blockers (protection from their color) |
| Bitter Triumph | Kolaghan's Command | Instant 2-for-1: removal stays 9, adds the third artifact answer and a recursion mode (wipe insurance); likely raises Salt |
| Vindictive Warden | Hidden Footblade (loan accepted) | Haste 4 -> 5 (Boots, Haunted Cloak, Hidden Footblade, Boros Guildmage, Queen Marchesa self); 4 granters reach a recast Ezio, plus Loyal Inventor. Warden was the weakest route card ({3} per ping); the noncombat route is now Shao Jun + Kaya, a top-off as the review says |
| Command Bridge | Swamp | Tapped every turn and lost on turn 1; a Swamp also turns on Isolated Chapel, Drowned Catacomb, Dragonskull, Woodland Cemetery and the battle lands |
| Murky Sewer | Island | Tapped until a player is at 13; the Island enables Drowned Catacomb, Sulfur Falls, Hinterland Harbor and the battle lands |

Mana trade-off: lands that enter tapped on turns 1 to 4 drop from about 12 to about 7 (Path of Ancestry and Jungle Shrine
always; Abandoned Campground and Raucous Carnival until a player is at 13, which is when the kill is on; the 3 battle lands
and 3 check lands only sometimes, now with 15 basics). Kill payment WUBRG at once (conservative simulation): 35 % by turn 6,
51 % by turn 8, 64 % by turn 10 (round 2: 39 / 55 / 67 %); the tempo gain and Salt's Manabase Quality are worth the points.
Plan file: condition_enablers re-declared EARLY with the attackers and team pumps (review M1); Evie tagged engine (M2);
Mephitic Vapors marked bad late (M5). Propaganda and Ghostly Prison stay tagged engine (the tag set has no defense tag;
"protection" would inflate the commander-protection count). Gate PASS (warnings: team_evasion 4, ramp 7); bracket PASS.

Earlier rounds below.

## Round 2 header

Round 2 applies `decks/phase2/owner-decisions.md` (second round): the three loans to evaluate are accepted, the lead's
scarce-copy resolution is applied, and the swaps are chosen to keep or raise likely Salt power (loans Cover of Darkness,
Unstoppable Slasher and Achilles Davenport are among the strongest Assassin cards on EDHREC for Ezio). Round-2 swaps:
Mechanical Glider -> Cover of Darkness; Boros Guildmage -> Unstoppable Slasher; Adéwalé -> Achilles Davenport; Swan Song
(to Kilo) -> Octopus Form; Hidden Footblade (to Azula) -> Boros Guildmage (keeps haste at 4); Commander's Sphere (to Kilo)
-> Boros Locket; Spire of Industry -> Command Bridge; Glacial Fortress -> Abandoned Campground; Radiant Summit -> Raucous
Carnival; Mystic Monastery -> Rumble Arena (all English, owned, free). Coastal Piracy was already in the list (proven role-player).

Builder: Opus 5.5 (high), upgrade mode from `decks/scanned/ezio-auditore-da-firenze.txt` (the Phase 1 list). List:
`decks/phase2/ezio-auditore-da-firenze.txt`; plan file: `ezio-auditore-da-firenze.plan.json`. Gate
(`scripts/plan_density.py`): **PASS**, 0 failures, 2 warnings (section 9; round 2: team_evasion 5, ramp 7). Bracket (`scripts/check_phase2_bracket.py`):
**PASS**, floor 1, 0 Game Changers (also checked against the live Scryfall `is:gamechanger` search on 2026-11-02: 53 cards,
none in the list), no extra turns, no mass land denial, no reversible card, 0 Spellbook combos inside the list.
Running the gate script with no arguments also rewrote the consistency reports of Toph and Azula from their own plan files
(deterministic; I did not edit their inputs).

## 1. Commander reading and rules points

Ezio Auditore da Firenze, {1}{B}, 3/2 menace Human Assassin. "Assassin spells you cast have freerunning {B}{B}." "Whenever
Ezio deals combat damage to a player, you may pay {W}{U}{B}{R}{G} if that player has 10 or less life. When you do, that
player loses the game."
- Rewards: Assassin spells (cost reduction after a hit) and Ezio's own combat damage (the kill).
- Fuel: a hit by any Assassin or a commander each turn (turns freerunning on), and Ezio himself connecting while a
  player is at 10 or less, with five colors of mana held for the combat damage step.
- Wins: the kill removes ONE player per Ezio hit, only once that player is at 10. Everything else (the first 30 life of
  each opponent) is combat damage and pings. Single-target kill = backup-style route; the team damage is the main load.
- Dies to: everything (toughness 2), chump blockers (menace fails against 8 goblins), being tapped and open on the
  crack-back. Cheap (2), so recasts are affordable (4, 6) but each recast loses a turn without haste.
- Dependence: **attack engine** (kill only on connecting; the freerunning grant needs him on the battlefield). Commander
  protection min 6, target 8. Haste stays a support line (promotion test fails: the freerunning grant is a static clause
  that acts without attacking) but sits at 5 because the owner lost games with no haste at all.
- Dead clauses in the commander: none. The menace is irrelevant against Board 1.

Rules points to verify:
| Point | Status | What falls if wrong |
|---|---|---|
| The life check happens when Ezio's trigger resolves; once paid, the reflexive trigger kills whatever the life total then | Confirmed, Scryfall ruling 2024-07-05 | Nothing |
| Freerunning is on for the rest of the turn once an Assassin OR a commander dealt combat damage, even if it then leaves | Confirmed, ruling 2024-07-05 | Nothing |
| Ezio's {B}{B} grant needs Ezio on the battlefield when the Assassin is cast | Card text (static ability) | The cheap-cast engine is off while Ezio is dead: cast post-combat only while he lives |
| Brotherhood Headquarters' colored mana can NOT pay Ezio's kill (it pays Assassin spells, freerunning spells, abilities of Assassin sources; the trigger payment is none of these) | Card text and ruling 2024-07-05 (spells and abilities only); not a ruling about triggers, marked "text reading" | It is counted colorless for the payment already |
| Trample damage that passes a chump blocker is combat damage to the player and triggers Ezio (Haunted Cloak) | Rules knowledge (510.1c-d), not re-read | Haunted Cloak drops from through_wide_board (still 15) |
| Shao Jun may tap Equipment (attached) and fresh artifacts to ping | Confirmed, ruling 2024-07-05 (any untapped artifacts); tapped Equipment keeps working (rules knowledge) | Pings slow down |
| Bayek's "historic" = legendary, artifact or Saga | Confirmed, ruling 2024-07-05 | Nothing |
| A creature phased in by Haystack on my untap step can attack (phasing is not a control change) | Rules knowledge 702.26, not re-read | Haystack still saves Ezio, he only waits one turn |
| Bleeding Effect reads only printed keywords of creature CARDS in the graveyard (Hookblade Veteran's and Shao Jun's "during your turn" flying does not count there) | Rules knowledge 113.6 (static abilities work only on the battlefield), not checked in rulings | Already assumed: only Gold-Forged Thopteryx and Aven Heartstabber give flying |
| Kaya's 0 on Ezio returns him at my upkeep, summoning sick | Rules knowledge 302.6 | Already assumed: Kaya is NOT counted as commander protection |

## 2. Plan and backup

- **Plan (one sentence):** cheap evasive Assassins and Ezio connect from turn 2 or 3, Equipment (flying, haste, hexproof,
  trample, vigilance) and unblockable Assassins carry Ezio past any board, every hit makes Assassin spells cost {B}{B}
  and draws cards, team damage (Arno, Bayek, Rally, pings to each opponent) pushes all three opponents to 10, and Ezio's
  trigger removes them one per hit, while attack taxes and vigilant or deathtouch bodies hold the crack-back.
- **Backup (same pieces):** without Ezio, the same evasive Assassins with Arno and Bayek keep dealing damage, and the
  repeatable pings to each opponent (Shao Jun, Kaya) finish players that combat already put low.
- Archetype: `combat_attackers` primary + `alternate_kill` secondary (role plan): the kill triggers on combat damage, so
  the attackers are its fuel (skill hybrid rule). Typal Assassin is a modifier (freerunning): 21 of 27 creatures are
  Assassins (78 %), reported in the plan's support block as a note, not a profile line.
- What changed in kind against Phase 1: the reanimation package (Entomb, Magister Sphinx, Roshan, Deadeye Navigator),
  the copy package (Strionic Resonator, Lithoform Engine, Return the Favor, Dualcaster Mage, Ember Island Production) and
  the Sphinx kill setup are gone; the Equipment that were 2 orphans (Winter Soldier's clause) are now 6 pieces (plus Cover of Darkness) that each do
  a support job (haste, evasion, protection, defense), so Winter Soldier's clause and Ratonhnhaké꞉ton's are live.

## 3. Profile table

Card counts are pieces in the 99 (commander counted only where it says so). Odds: hypergeometric, 99-card library, no
mulligan, no extra draw (conservative).

| Function | Tier | Min | Target | Actual | Reason |
|---|---|---|---|---|---|
| attackers | gate early | 12 | 16 | 18 + Ezio | Fuel: one hit per turn turns on freerunning and the draw; 91 % to see one by 12 cards without Ezio |
| through_wide_board | gate early | 10 | 12 | 15 | Owner's loss to 8 goblins: flyers, unblockables, flying Equipment, Gauntlet, Vapors, Secret Tunnel, trample; menace and Lydia not counted; 90 % by 12 cards |
| through_big_creatures | gate early | 10 | 12 | 16 + Loyal Inventor | 7 spot removal + Haytham, Royal Assassin, deathtouch bodies, Hidden Blade, Lydia, Etrata |
| condition_enablers | gate (late via commander) | 6 | 8 | 8 + Ezio (Slasher single-target, half weight) | Team damage that puts every opponent at 10. Same cards as team_finishers ON PURPOSE: in this deck the effects that lower all three life totals are the ones that finish them; the condition's extra piece is Ezio's own hit |
| team_finishers | gate late | 6 | 8 | 6 | Arno, Achilles, Bayek, Rally, Shao Jun, Kaya: each hits all opponents per resolution (Warden left in round 3) |
| haste | support | 4 | 6 | 5 | Round 3: Hidden Footblade loan accepted, so haste = Boots, Haunted Cloak, Hidden Footblade, Boros Guildmage, Queen Marchesa (self) = 5. History, round 2: Hidden Footblade went to Azula and the owner swapped Boros Guildmage for Slasher, which left 3; Boros Guildmage returns in Footblade's slot, so haste = Boots, Haunted Cloak, Boros Guildmage (repeatable), Queen Marchesa (self) = 4, the minimum. Loyal Inventor fetches Boots or Cloak |
| team_evasion | support | 6 (floor 4) | 8 | 4 (about 3 weighted; Bleeding Effect left in round 3) | **WARN.** Cover of Darkness (fear for 22 Assassins and Ezio, repeatable) is now in; the rest of the pool has no more real team evasion: Gauntlet (one-shot, one opponent), Secret Tunnel (two creatures), Mephitic Vapors (one-shot), Bleeding Effect (flying only with a flier in the graveyard). Board 1 is also carried by 15 individual pieces |
| defense_while_tapped | support | 4 | 6 | 9 | Propaganda, Ghostly Prison, vigilance (Cloak, Winter Soldier, Loyal Inventor), Royal Assassin, deathtouch blockers (Thorn, Etrata DF), Thopteryx |
| combat_draw | support | 4 | 6 | 7 | Ezio Blade, Coastal Piracy, Eagle Vision, Jacob, Layla, Etrata DF, Theater of Horrors |
| wipe_insurance | support | 2 | 3 | 5 | Revelations III, Layla, Get Out, Haystack, Kolaghan's Command (Restart Sequence left in step 4); Equipment survive creature wipes and re-haste the rebuild |
| payment_enablers | support | 6 | 8 | 8 | Lantern, Arcane Signet, Waterskin, Command Tower, Orchard, Path, Rumble Arena, Abstergo (8) |
| ramp (base) | base | 10 | 12 | 7 | **WARN.** Reason: commander costs 2; avg MV 2.71; every Assassin hit makes the 4 and 5 drops cost {B}{B} (Ezio Blade, Bayek, Arno, Layla, Etrata S, Marchesa), so mana is spent on equip costs and the kill, not on big spells. The pool's 2-mana rocks are taken by Toph and Azula; the 3-mana rocks here are also payment fixers. 36 lands + 7 rocks = 43 sources. Mind Stone proposed (section 8) |
| draw (base) | base | 10 | 12 | 11 tags, about 9.5 weighted (Lion Vulture in; Evie's loot not counted; Jacob, monarch cards, Kaya, Etrata DF, Boros Locket at half) | Etrata DF (cloak bodies), Queen Marchesa and Thorn (monarch is often stolen) and Kaya (-2 once) count half |
| removal (base, spot) | base | 6 | 8 | 9 | 7 spells + Haytham + Royal Assassin. Answers (10 with the wipe) stay under the closers (17 attackers + 6 finishers) |
| wipe (base) | base | 1 | 2 | 1 | Mephitic Vapors: kills tokens and 1-toughness bodies; a symmetric wrath would kill the plan |
| commander protection | base (attack engine) | 6 | 8 | 7 | Swiftfoot Boots, Gold-Forged Thopteryx (ward 2 on every legend), Haystack, Octopus Form (Swan Song went to Kilo), Enter the Avatar State, Get Out, Angelic Intervention (7). 55 % by 12 cards; layered: hexproof and ward vs targeted, phasing vs exile and wipes, bounce vs anything; no counter to a wrath now (Arcane Denial proposed). Kaya's 0 is not counted |
| graveyard hate | base | 1 | | 1 | Abstergo Entertainment (exile all graveyards; also returns a legend) |
| tutors | | | | 1 | Loyal Inventor: any artifact (flying Equipment, Hidden Blade, Gauntlet, Boots, Lantern) |

Fit check: gate mins counted once (17 attackers already include 6 of the 15 wide-board pieces and 5 of the big-creature
pieces; finishers overlap attackers by 3) plus base floors (7 ramp, 9 removal, 1 wipe, 6 protection, 4 draw-only spells,
2 taxes) = 63 non-land cards: it fits in 99 with 36 lands.

Toughness check: attackers and route cards with toughness 2 or less = Ezio, Initiate, Aven Heartstabber, Evie,
Winter Soldier, Jacob, Lydia, Lion Vulture (8 of 21, 38 %; with Achilles out every other Assassin gets +1/+1): between a third and a half. Covered by Haystack,
Swiftfoot Boots, Get Out, Enter the Avatar State, Glider Staff (+1/+1), Angelic Intervention (protection from a color; formerly Bleeding Effect from the
yard) and by keeping the x/1s home against a sacrifice outlet. The engine pieces that must live are tougher: Arno 3/3,
Shao Jun 3/3, Etrata S 3/5, Layla 3/4, Ezio Blade 5/5, Bayek 3/4.

## 4. The list by function: how to use each card

Mana written as `{2}{U}`. "FR" = freerunning (cast after an Assassin or commander hit this turn).

**Commander**
- Ezio Auditore da Firenze: cast turn 2; attack every turn he can connect; hold {W}{U}{B}{R}{G} untapped in combat when the
  defender is at 10 or less; never attack into open deathtouch or first strike without an Equipment on him.

**Early attackers (turn 1 to 3 hits that switch on freerunning)**
- Assassin Initiate: turn 1 drop; pay {1} for flying to connect, deathtouch when it must block or attack into a big body; bad late.
- Aven Heartstabber: 2-mana flier; when it dies it refills (mill 2, draw 1) and fills the graveyard for Jacob and Restart Sequence.
- Desmond Miles: menace grows with every Assassin; attack the player with the fewest blockers; surveil after a hit sets up the next draws.
- Brotherhood Spy: unblockable every turn you have a legendary Assassin (Ezio and 14 others); your most reliable early hit.
- Evie Frye: cast for Jacob from the library (a free card); loot with {1}; discard a creature card to make Ezio unblockable that turn.
- Winter Soldier, Icy Assassin: vigilance menace 2-drop that holds the fort; +2/+0 per Equipment, so it is the second Equipment carrier; returns himself late.

**Mid attackers and engines**
- Shao Jun: flier with first strike on your turn; tap two Equipment or rocks for 1 damage to each opponent; never tap the rocks you need for the kill.
- Ratonhnhaké꞉ton: hexproof and unblockable until its first hit: a guaranteed hit for freerunning; later returns a dead Equipment onto its menace token.
- Jacob Frye: after Assassins hit, recast a dead Assassin from your graveyard; best when the yard has Ezio Blade or Arno.
- Lydia Frye: attack the player with big blockers (they cannot block her); end-step surveil filters your next draws (formerly for Bleeding Effect.
- Achilles Davenport (loan): FR {U}{B} or {B}{B}; other Assassins +1/+1: cast before the wide swing; it lifts the x/1s out of ping and small-wipe range.
- Unstoppable Slasher (loan): deathtouch 2/3 Assassin; a hit halves that player's life (40 to 20 to 10, then Ezio); returns once with stun counters when it dies without counters. Equip it with flying first.
- Etrata, Deadly Fugitive: 1/4 deathtouch wall that stays home; each Assassin hit cloaks a 2/2 ward body from that opponent's library.
- Arno Dorian: +2/+0 to every Assassin: cast it the turn you swing wide; deathtouch makes it a fine blocker; disguise only to dodge a removal read.
- Queen Marchesa: haste deathtouch; take the monarch only when your taxes and deathtouch blockers can keep it.
- Etrata, the Silencer: cast FR {B}{B}; unblockable removal: exile the biggest blocker of the player you hit; she shuffles away after, so cast her when the hit matters.
- Layla Hassan: FR {B}{B}; every Assassin hit returns a legend, Equipment or Saga to hand: your rebuild after a wipe.
- Ezio, Blade of Vengeance: FR {B}{B} on turn 3 or 4; every Assassin hit draws; 5/5 deathtouch also stops big attackers.
- Bayek of Siwa: FR {B}{B}; your legends and artifact creatures get double strike on your turn: cast it the turn before the big swing; bad early at 5 mana with no hit.

**Equipment (support jobs: haste, evasion, protection)**
- Swiftfoot Boots: on Ezio first; recast Ezio and equip for {1} to attack at once with hexproof.
- Haunted Cloak: haste + vigilance + trample: put it on Ezio Blade or Desmond for damage that passes chumps, on Ezio for haste and to stay back as a blocker.
- Hookblade: attaches on entry: flying for Ezio on your turn; 2 mana for evasion.
- Cover of Darkness (loan, proven role-player): name Assassin on turn 2 or 3: Ezio and 22 Assassins can be blocked only by black or artifact creatures; it beats the goblin board.
- Glider Staff: exile the key blocker or an opposing commander on entry (they recast it for {2}), then a flying +1/+1 carrier.
- Hidden Blade: hold it; flash it onto a blocked Assassin: first strike + deathtouch kills the bigger blocker first.
- Assassin Gauntlet: cast precombat on the goblin player: their whole board taps, everybody connects; the carrier loots on hits.

**Removal (spot)**
- Swords to Plowshares: the 1-mana answer to a big blocker or a commander.
- Infernal Grasp: instant answer to any creature; use it on attackers aimed at you while you are tapped out.
- Terminate: same, no life cost.
- Assassin's Trophy: any permanent: enchantment taxes, artifacts, planeswalkers.
- Mortify: creature or enchantment (opposing Propaganda effects).
- Utter End: exile any nonland permanent: commanders and indestructible threats.
- Kolaghan's Command: instant 2-for-1: 2 damage to a small blocker or pinger plus destroy an artifact, or return a dead Assassin to hand; discard mode when an opponent holds one card.
- Haytham Kenway: exiles one creature of EACH opponent: your best card against Board 2; keep him alive (Haystack, Get Out).
- Royal Assassin: stays home; kills an attacker that tapped to hit you, or a blocker that attacked last turn.

**Wipe**
- Mephitic Vapors: cast precombat against a token board: all 1/1s die, then everything connects; it also kills your x/1s (Initiate, Aven, Evie, Royal Assassin, Deathcap; Achilles saves them), so attack first with them or accept it.

**Commander protection**
- Gold-Forged Thopteryx: turn 2 play; ward {2} on Ezio and every legend; lifelink flying blocker.
- Haystack: keep {2} up; phase out Ezio or Haytham in response to removal or a wipe.
- Octopus Form: {U} in response to targeted removal on Ezio; or untap an attacker to block (defense while tapped).
- Boros Guildmage: {1}{R} gives the recast Ezio (or a freerunning Assassin before a second combat) haste; {1}{W} first strike against a bigger blocker.
- Enter the Avatar State: in response to removal, or in combat to give Ezio flying, first strike and lifelink for the kill.
- Get Out: counter a creature or enchantment spell, or bounce Ezio and one more creature in response to removal and recast them.

**Card flow**
- Eagle Vision: FR {1}{U} after the first hit: three cards for two mana; never pay 5 unless the hand is empty.
- Coastal Piracy (proven role-player): cast it when {U}{U} is up (about 50 % by turn 4; Arcane Signet or Chromatic Lantern first) with three attackers out: one card per connecting creature.
- Kaya, Ghost Assassin: -1 drains 2 from each opponent (closer); -2 trades a card with each opponent; 0 only to blink a creature you need back (it returns sick).
- Theater of Horrors: once you hit every turn it is a second hand; {3}{R} ping turns it on when combat failed.
- Thorn of the Black Rose: monarch draw; play it when deathtouch and taxes can defend the crown.
- Loyal Inventor (tutor): vigilance body that finds the missing Equipment (Boots for protection, a flier against goblins, Hidden Blade against big ones) or Chromatic Lantern for the kill.

**Defense while tapped**
- Propaganda: turn 3 play; pushes the goblin swarm to the other players. Proven role-player.
- Ghostly Prison: the second tax; together they make 8 goblins cost 16 mana per attack.

**Team damage and pings (routes)**
- Rally the Peasants: +2/+0 to the team on the swing that can put two players at 10; flashback for the next swing; bad early.
- Hidden Footblade (loan, accepted 2026-11-02): flash it in on a recast Ezio for haste, or after blocks for first strike +1/+0 against a bigger blocker.
- Lion Vulture: 4-mana flier that draws and grows every end step an opponent lost life (nearly every turn here); hold it back as a flying blocker when the table has fliers.
- Angelic Intervention: in response to removal on Ezio, or on the kill turn: protection from the blockers' color (red goblins) makes him unblockable by them; never on Unstoppable Slasher (its counter stops the return).

**Recursion**
- (Restart Sequence left in step 4 for Vindictive Warden.)
- Vindictive Warden: menace body that can block; spend spare mana at the end of an opponent's turn: {3} = 1 damage to each opponent; firebending adds {R} toward it in combat.
- The Revelations of Ezio: I kills a tapped creature after their attack, II pumps your Assassin swing, III returns an Assassin.

**Ramp and fixing**
- Sol Ring: turn 1.
- Arcane Signet: turn 2 any color; a kill-payment source.
- Rakdos Signet: turn 2; {B}{R} for FR casts.
- Deathcap Cultivator: turn 2 or 3 (needs {G}); taps for {B} for FR.
- Chromatic Lantern: turn 3 or 4; makes every land pay any color: the kill payment's best card.
- Boros Locket: turn 3; red or white, the two thinnest colors; late, four hybrid mana draws two.
- Bender's Waterskin: turn 3; untaps on every opponent's turn: protection mana and payment on their turns.

**Lands (36)**: Command Tower, Exotic Orchard, Path of Ancestry (tapped; any color, scry on Assassins), Rumble Arena (colorless, {1}: any color, scry 1), Brotherhood Headquarters (any color for Assassins and FR spells, NOT the kill), Abstergo
Entertainment (filter; late: return a legend and exile all graveyards), Secret Tunnel ({4}: Ezio and another Assassin
unblockable), Concealed Courtyard, Isolated Chapel, Drowned Catacomb, Sunken Hollow, Dragonskull Summit, Smoldering Marsh,
Woodland Cemetery, Clifftop Retreat, Sulfur Falls, Hinterland Harbor, Prairie Stream, Abandoned Campground, Raucous
Carnival (both untapped once a player is at 13), Jungle Shrine (tapped), 10 Swamp, 2 Island, Plains,
Mountain, Forest.

## 5. Cut log (round 1: Phase 1 list against the round-1 list, 38 out, 38 in; round-2 swaps below)

Proven role-players for Ezio (owner): Eagle Vision IN, Propaganda IN, Cover of Darkness proposed (section 6, fallback in
the list). None of the 38 cuts was reported by the owner as winning a game; none is cut for a score or inclusion rate.

| Card out | Function it served | Count after (min) | Replaced by / reason |
|---|---|---|---|
| Entomb | reanimation setup (Sphinx) | package dropped | Owner L1/L7: graveyard mini-plan. Recursion stays as wipe insurance (5, min 2) |
| Magister Sphinx | kill setup, 7 MV | condition_enablers 6+Ezio (6) | Bayek and Rally put ALL opponents low instead of one; 7 MV with Roshan/Entomb support only |
| Roshan, Hidden Magister | made non-Assassins Assassins (for Sphinx, Deadeye) | Assassins 21/27 | Static redundant once the non-Assassins are cut; slot to Layla Hassan |
| Deadeye Navigator | protection, 6 MV | protection 6 (6) | Haystack: 2 mana, instant, also beats exile wipes |
| Strionic Resonator, Lithoform Engine | trigger copies | none (orphan package) | Copy package dropped (L1); slots to Bleeding Effect, Shao Jun |
| Dualcaster Mage, Ember Island Production | copy mini-combo | none | L7 named; slots to Vindictive Warden, Rally the Peasants (team finishers 6) |
| Return the Favor | protection/copy | protection 6 (6) | Get Out (UU, counters or saves two creatures) |
| Venser, Shaper Savant | protection/tempo, 4 MV | protection 6 (6) | Swan Song (1 mana, stops wipes) |
| Mana Leak | counter | removal 9 (6) | Weak late; Enter the Avatar State takes the protection job |
| Nekrataal | removal, nonblack only | removal 9 (6) | Play review "replace"; Swords to Plowshares |
| Fatal Push, Murder, Fateful Absence, Stroke of Midnight, Chaos Warp, Kolaghan's Command | spot removal | removal 9 (6, target 8) | Answers outnumbered closers (red flag); kept the 7 cheapest flexible ones. Freed slots go to haste, evasion, taxes |
| Starfall Invocation | wipe | wipe 1 (1) | Symmetric wrath kills the attack plan; Mephitic Vapors is near one-sided against tokens |
| Intruder Alarm | none (no line) | n/a | Orphan (play review) |
| Everflowing Chalice | ramp | ramp 7 (10, WARN) | Owner L5: cast turn 5 for two. Bender's Waterskin (fixes and works on opponents' turns) |
| Dimir Locket | ramp, 3 MV | ramp 7 | Play review "replace"; Commander's Sphere (any color for the kill) |
| Rampant Growth | ramp ({G} on turn 2) | ramp 7 | Green on turn 2 is about 50 % here; replaced by colorless/any-color rocks |
| Mishra's Bauble, Brainstorm, Faithless Looting, Seismic Sense | cantrips (not draw) | draw 12 (10) | Not draw; Eagle Vision, Theater of Horrors |
| Mystical Teachings | tutor for instants, 4 MV | tutors 1 | Few flash targets left; Loyal Inventor finds Equipment |
| Reckless Handling | artifact tutor, random discard | tutors 1 | Random discard can lose the fetched card; slot to Glider Staff |
| Tome of Legends | slow draw | draw 12 (10) | Theater of Horrors gives more per turn; Tome kept as the next draw swap if draw comes short in play |
| Ravenloft Adventurer | initiative + hit counters | attackers 17 (12) | Initiative makes the deck the target while it is open after attacking; hit counters need Etrata (mini-combo); Layla Hassan |
| Rumble Arena, White Lotus Hideout, Survivors' Encampment | colorless/filter lands | lands 36 | Review flagged colorless lands; Path of Ancestry, Spire of Industry, Murky Sewer |
| Frostboil Snarl, Fortified Village, Game Trail | reveal duals (mostly tapped with 1 basic of each) | lands 36 | Jungle Shrine, Mystic Monastery (three colors each), Glacial Fortress |
| Island (one of two) | U source | U about 16.5 | +1 Swamp (B is the heaviest color: 28 pips, {B}{B} FR) |

Round 2 cuts (owner decisions and lead's copy resolution, 2026-11-02):

| Card out | Function | Count after (min) | Replaced by |
|---|---|---|---|
| Mechanical Glider | through_wide_board | 15 (10) | Cover of Darkness (team version of the same job) |
| Boros Guildmage (then re-added) | haste | 4 (4) | Unstoppable Slasher took its slot; Guildmage returns in Hidden Footblade's slot |
| Adéwalé, Breaker of Chains | attackers, draw | attackers 18 (12), draw 11 (10) | Achilles Davenport (team pump, toughness fix; dead Vehicle clause gone) |
| Swan Song (to Kilo) | protection, wipe insurance | protection 6 (6), wipe insurance 5 (2) | Octopus Form (same job against targeted removal, not against wraths) |
| Hidden Footblade (to Azula) | haste | 4 (4) | Boros Guildmage (repeatable haste) |
| Commander's Sphere (to Kilo) | ramp, payment | ramp 7 (10, WARN), payment 9 (6) | Boros Locket (R or W; any color lost) |
| Spire of Industry, Glacial Fortress, Radiant Summit, Mystic Monastery (to Kilo) | lands | 36 | Command Bridge, Abandoned Campground, Raucous Carnival, Rumble Arena |

Considered and left out: Hullcarver (1/1 deathtouch, chumped by goblins; no slot), Rooftop Assassin, Merciless Harlequin,
Hunter's Bow (needs {G} early), Champion's Helm (Azula's), Tome of Legends, Fire Nation Archers, Kitesail, Aya of
Alexandria, Vincent, Massacre Girl, What Must Be Done; Expedite is Azula's (haste is 5 since the Hidden Footblade loan).

## 6. Loans

All declared in `decks/phase2.json` `borrowed` and in `restock.md` (owner, 2026-11-02): Eagle Vision, Layla Hassan, Bayek
of Siwa, Cover of Darkness, Unstoppable Slasher, Achilles Davenport (and the proxy commander). From his own collection (no
loan): Assassin Initiate, Hidden Blade, Propaganda (free copy), Ratonhnhaké꞉ton (free copy). No proposal is pending.

## 7. Scarce copies (resolved by the lead, 2026-11-02)

- Ezio keeps: Swords to Plowshares (Spanish copy), Chromatic Lantern, Command Tower, Swiftfoot Boots, Haunted Cloak, one free
  Propaganda, Octopus Form (the free English copy; Azula has the other).
- Ezio gave up: Swan Song, Commander's Sphere, Spire of Industry, Glacial Fortress, Mystic Monastery, Radiant Summit (to Kilo),
  Hidden Footblade (to Azula), Battlefield Forge (Toph). All replaced with owned English cards (section 5).
- Remaining Spanish-only copies in this list (Hookblade, Brotherhood Spy, Evie Frye, Ezio Blade, Utter
  End, Theater of Horrors, Restart Sequence, Revelations, Deathcap Cultivator, Isolated Chapel, Woodland Cemetery,
  Hinterland Harbor, Assassin Gauntlet, Swords, Exotic Orchard, Brotherhood Headquarters, Clifftop Retreat): Kilo's list of
  2026-11-02 uses none of them.

## 8. Purchase proposals (Toph, Azula and Ezio share 5,000 CLP at Game of Magic Singles; prices are hints from the 2026-10-17 reading, verify live stock)

Ranked by impact (consistency first, then likely Salt power):
1. **Arcane Denial** (about 2,840 CLP). Need: no answer to a wrath since Swan Song went to Kilo. Fallback (plays now): Get
   Out (it leaves for Arcane Denial).
2. **Mind Stone** (about 742 CLP). Need: ramp 7 against 10, a turn-2 rock. Fallback: Boros Locket (it leaves).
3. **An untapped dual in two of Ezio's colors, or a 2-mana black Talisman** (Hierarchy, Dominance, Indulgence; price to
   read). Need: fewer tapped lands, more {B}{B}. Fallback: Jungle Shrine (leaves for a dual) or Deathcap Cultivator (for a
   Talisman).
4. **Rogue's Passage** (about 742 CLP), lowest: repeatable unblockable for Ezio, but colorless. Fallback: Rumble Arena.
Second store (owner, 2026-11-02): only the replacement copy of the lent Hidden Footblade (restock), nothing else for Ezio.

## 9. Warning reasons and dead clauses

- WARN ramp 7 < 10: see the profile table (commander MV 2, freerunning as cost reduction, 2-mana rocks taken by other
  decks; Mind Stone and a Talisman proposed).
- WARN team_evasion 5 < 6: Cover of Darkness is in; the pool has no sixth team effect; the profile allows floor 4 with
  through_wide_board carried by flyers, unblockables and the Equipment (15 pieces, 90 % by 12 cards).
- Dead or weak clauses: Cover of Darkness does nothing against black or artifact blockers; Haytham's Knight bonus and protection from Assassins (no
  Knights; irrelevant); Ratonhnhaké꞉ton's Equipment return (live but rare); (round 2 only) Bleeding Effect's flying needed one of 2 flying
  creature cards in the yard (its deathtouch, vigilance, menace come from 8 more); Mephitic Vapors kills my x/1s (fewer with Achilles out);
  Kaya's 0 is a slow blink; Arno's and Bayek's disguise only as anti-removal bluff.
- The two late gate functions share their 6 cards by design (section 3).

## 10. The two reference boards

- **Board 1, eight or more sacrificeable 1/1s:** Assassin Gauntlet taps their whole board for one swing; Mephitic Vapors
  kills all of them precombat; Cover of Darkness gives every Assassin fear (goblins are not black or artifact);
  Ezio flies with Hookblade or Glider Staff, or goes unblockable with Secret
  Tunnel; Brotherhood Spy, Etrata S, Ratonhnhaké꞉ton (first hit), Shao Jun, Initiate, Lion Vulture, Aven fly or pass;
  Haunted Cloak tramples over a chump; pings hit them anyway. Defense: Propaganda + Ghostly Prison charge 2 per goblin,
  deathtouch blockers and Thopteryx. My x/1s do not attack into a board with a sacrifice outlet.
- **Board 2, two or more bigger creatures:** Haytham exiles one per opponent; 7 spot removal; Royal Assassin kills them
  after they attack; Etrata S exiles one per hit; Hidden Blade (first strike + deathtouch) and deathtouch bodies (Arno, Ezio
  Blade, Etrata DF, Unstoppable Slasher, Initiate) make blocks bad for them; Lydia cannot be blocked by power 3+; the fliers go over.
- **One sweeper turn:** Haystack or Get Out saves Ezio or the board; Equipment survive; next turn Ezio (4 mana) + Boots
  or Cloak attacks at once, Layla, Restart Sequence, Revelations III and Jacob rebuild.

## 11. Mana

- 36 lands (band 36 to 38) + 7 rocks/dorks. 23 nonbasic + 13 basic (9 Swamp).
- Colored sources (lands full, any-color lands full, Orchard/HQ 0.75, Abstergo 0.5, rocks 0.75, Lantern full):
  B about 26, U about 16, W about 16, R about 16, G about 12 (round 2 lost two any-color sources and a tri-land). Pips: B 30, U
  21.5, W 19, R 7.5, G 2. B meets {B}{B} on
  turns 3 to 4 (Karsten 2CC about 26); U and W are under the turn-2 targets for 2-drops (19): the blue and white 2-drops
  are often cast on turn 3.
- Tapped lands (round 3): 2 always (Path, Jungle Shrine) + 2 until a player is at 13 (Abandoned Campground, Raucous
  Carnival) + 3 battle lands (Sunken Hollow, Smoldering Marsh, Prairie Stream) tapped until two basics (15 basics: 10 Swamp,
  2 Island, Plains, Mountain, Forest). Check lands: Isolated Chapel, Drowned Catacomb, Dragonskull, Woodland Cemetery
  mostly untapped (10 Swamps); Sulfur Falls (6 enablers) and Hinterland Harbor (5) often; Clifftop Retreat (4) often tapped
  (Battlefield Forge proposed).
- Curve (non-land 63): MV1 6, MV2 20, MV3 22, MV4 12, MV5 3; average 2.78. Turn 2 and 3 plays: 26 cards at MV 1 to 2.
- Keepable hand (2 to 4 lands in 7): 74 % per look, 93 % with the free mulligan.
- Kill payment {W}{U}{B}{R}{G} held in combat (simulation, 20,000 games, conservative: Brotherhood HQ, Abstergo and Sol Ring
  count as colorless, Rakdos Signet one color): round 1 was 43 % by turn 6, 60 % by turn 8, 72 % by turn 10; round 2 about 39 %, 55 % and 67 % (the lands and the
  Sphere given to Kilo were any-color or three-color). With five or more
  sources the colors fit 61 to 78 %; Chromatic Lantern or Loyal Inventor fetching it lifts it. The kill is the shortcut, the
  team damage is not color-bound.

## 12. Open questions for the owner

1. Purchases: Golgari Signet, Battlefield Forge and Mind Stone (2,227 CLP at Game of Magic Singles); approve?
2. Game Changers: if a Teferi's Protection, Smothering Tithe or Fierce Guardianship can be had (gift, trade, a later
   budget), they go in for Get Out, Boros Locket and Octopus Form.
