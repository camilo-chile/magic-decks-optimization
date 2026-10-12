Model ID: claude-sonnet-5-5

# Rules check: Fire Lord Azula synergy report (2026-10-12)

Report under check: `docs/research/synergy-fire-lord-azula-2026-10-11.md` (plus its verification file).
Evidence: `data/cache/rulings_pool.jsonl` (official Wizards rulings as reprinted by Scryfall),
`data/cache/pool_fire-lord-azula.jsonl` (oracle text), `data/cache/spellbook_fire-lord-azula.json`.
No network, no Comprehensive Rules (CR) text on disk: any CR number below is labelled **unverified**.
Method: read-only Python (`python -I`, exact card-name match) plus keyword searches over all 68,266
rulings; helper scripts live in the session scratchpad. Rulings are paraphrased; "(date)" is
`published_at`, source is always `wotc`. A face name can match a prepare card ("X // Seething Song"),
so only exact-name matches were used as evidence.

Verdict key: CONFIRMED = a ruling or the oracle text says it. PARTLY = true but incomplete or
conditional. CONTRADICTED = the report must change. NOT COVERED = rulings do not settle it.

## 1. Commander and core cards: all rulings read
- Fire Lord Azula: 12 rulings (2025-10-02), all used below.
- Core cards: Sol Ring 0, Big Score 0, Infernal Grasp 0, Counterspell 0, Arcane Signet 3, Command Tower 3
  (colors follow the commander's identity, UBR), Storm-Kiln Artist 4, Archmage Emeritus 4,
  Deadly Rollick 2, Fire Covenant 3, Toxic Deluge 2, Swiftfoot Boots 1, Deflecting Swat 5.
  Nothing there changes a core-tier call; relevant items are in the table and in section 4.

## 2. Claim table
| # | Claim (report section) | Verdict | Evidence |
|---|---|---|---|
| 1 | Copy trigger is mandatory ("copy that spell", no "may"); only the new targets are optional (§1) | CONFIRMED | Oracle text has no "may" on the copy; Azula (2025-10-02): you "may change any number of the targets ... or none of them" |
| 2 | Window = only while she is an attacking creature: from declare attackers until she leaves combat or combat ends; own turn only (§1) | CONFIRMED | Oracle "while Fire Lord Azula is attacking". Leaving combat: phasing out removes an attacker from combat (Slip Out the Back 2022-04-29; Talon Gates 2024-06-07); losing creature type does too (Weeping Angel 2023-10-13) |
| 3 | Copies spells cast while another spell/ability resolves (Electrodominance, Torrential Gearhulk); Electrodominance puts a sorcery into combat (§1) | CONFIRMED | Electrodominance (2024-04-12): spell is cast during resolution, "ignore timing restrictions based on the spell's type"; Torrential Gearhulk (2016-09-20): cast as part of the trigger's resolution; Mystic Confluence (2021-03-19) / Great Train Heist (2024-04-12): triggers wait until the spell finishes resolving |
| 4 | Copies are not cast: cast triggers (Guttersnipe, prowess) fire once; magecraft fires on cast and on each copy (§1) | CONFIRMED | Azula: copy "is created on the stack, so it's not cast"; Storm-Kiln Artist / Archmage Emeritus / Veyran (2021-04-16): magecraft triggers once per copy created |
| 5 | Firebending adds RR and lasts until end of combat (§1) | CONFIRMED | Azula: mana "isn't lost until you leave combat and go to your second main phase"; usable "even after combat damage" |
| 6 | Open (a): "keep red mana" effects (Electro, Ashling) keep firebending mana (§8.2a) | CONFIRMED | Firebending = "add N {R}" (Azula). Electro (2025-09-19) and Ashling (2024-06-07): you keep unspent red mana "indefinitely", other mana is lost. No ruling names both together: this is two rulings read jointly. Effect: RR survives into main 2 and later turns while the permanent stays; if it leaves, until end of that step or phase |
| 7 | Weakness: "blockers or removal cast in response to the first spell turn the engine off" (§1) | PARTLY | Azula: copy and trigger resolve "even if the spell is countered". Phasing out / non-creature removes her from combat (row 2). A blocker alone does not remove her from combat (no ruling; CR 506.4 unverified). Whether the already-triggered copy still happens if she is removed in response: not in rulings (CR 113.7a unverified) |
| 8 | Open (d): a copy keeps X (§1) | CONFIRMED | Azula; Twinning Staff (2020-04-17); Return the Favor (2024-04-12); Expansion // Explosion (2024-01-12) |
| 9 | A copy keeps the chosen modes and may only change targets (§1, §3 Prismari/Kolaghan/Cryptic/Confluence/Epiphany) | CONFIRMED | Kolaghan's Command (2015-02-25) and Mystic Confluence (2021-03-19): "can't choose new modes"; Twinning Staff, Narset's Reversal (2019-05-03), Great Train Heist (spree) say the same. Variable target count and divided damage are fixed too (Deflecting Swat 2020-04-17) |
| 10 | A copy pays no additional costs (discard, sacrifice, life) (§1) | CONFIRMED | Azula: "can't choose to pay any additional costs". Nuance missing from the report: effects based on additional or alternative costs paid for the original are copied as though paid (Azula; Dualcaster Mage 2016-06-08). Kicker, entwine and overload carry over |
| 11 | A copy sees 0 for "mana spent": Memory Deluge copy looks at 0 cards (§1, §5) | CONFIRMED | Memory Deluge (2021-09-24): "no mana was spent to cast the copy, so X will be 0 ... You won't look at any cards" |
| 12 | Big Score and Fire Covenant: free copy; Fire Covenant "X damage divided twice" (§1, §3) | CONFIRMED | Azula (additional costs, X). Wording nuance: the division is fixed at cast (Fire Covenant 2007-09-16; Deflecting Swat); the copy keeps the same per-target amounts and may retarget |
| 13 | Dig Through Time copy needs no delve (§3) | CONFIRMED | Azula (not cast) plus Memory Deluge (no mana spent for the copy). Delve is neither alternative nor additional (Dig Through Time 2021-03-19) |
| 14 | Comet Storm copy keeps X and the kicks: double spread (§3) | CONFIRMED | Comet Storm (2024-11-08): "If you copy a kicked spell on the stack, the copy is also kicked" |
| 15 | Copied adventure instants (Swift End, Stomp, Petty Theft): the copy adds no extra card; the card still goes on an adventure (§3) | CONFIRMED | Twice Upon a Time (2023-10-13): a copy of an Adventure spell is exiled as it resolves and ceases to exist. Swift End copy also costs 2 more life (oracle), not in the report |
| 16 | Copies of legendary permanent spells are legendary tokens; the legend rule leaves one; both ETB triggers still happen (Ertai, Venser, Mithril Coat) (§1, M4) | CONFIRMED | Azula: copy "becomes a token"; Lithoform Engine (2020-09-25) / Thurid (2024-11-08): spell-copy-to-token follows permanent-spell rules; Splinter Twin (2013-07-01): legend rule applies to a token copy; Inalla (2017-08-25): ETB triggers still occur before the legend rule. Order: the copy resolves first (Twinning Staff), so its ETB resolves before the original enters |
| 17 | Mandatory-copy trap: Pact of Negation copied "creates two upkeep triggers" (§5) | PARTLY | Pact (2021-03-19): a Pact that does not resolve creates no delayed trigger. If the copy keeps the original target, the copy counters it and the original fizzles: 1 trigger. Two triggers only if both resolve (different targets, or target can't be countered). The owner can avoid the second by keeping the target |
| 18 | Final Fortune copied: you lose at the end of the first extra turn (§5) | CONFIRMED | Oracle: each resolution makes its own "that turn's end step" loss trigger; Final Fortune (2022-12-08): extra turns are taken most recent first. Same text on Last Chance and Warrior's Oath; uncleaved Alchemist's Gambit (oracle) |
| 19 | Veyran: Azula's trigger fires twice on instants/sorceries; doubles magecraft (§3, §8.2c) | CONFIRMED | Oracle ("casting or copying an instant or sorcery ... causes a triggered ability of a permanent you control to trigger"); Veyran (2021-04-16): it "just causes the ability to trigger again", choices made separately. Not for flash creature spells |
| 20 | Roaming Throne naming Human: Azula's copy trigger fires twice for every spell and firebending twice (RRRR) (§3, §8.2c) | CONFIRMED | Oracle; Roaming Throne (2023-11-10); Azula: multiple firebending instances trigger separately. Wording fix: firebending fires once per attack (twice with Throne), not "for every spell" |
| 21 | Harmonic Prodigy doubles Shaman/Wizard triggers: Storm-Kiln, Archmage Emeritus, Veyran, Ashling, Guttersnipe (§3) | CONFIRMED | Oracle ("a Shaman or another Wizard you control"); pool types: Dwarf Shaman, Human Wizard, Efreet Wizard, Elemental Shaman, Goblin Shaman. 0 rulings on the card; sister rulings (Roaming Throne) describe the same mechanism |
| 22 | §8.2(c): Prodigy doubles "Azula's and the engines' triggers" | CONTRADICTED | Azula is a Human Noble; Prodigy only affects Shamans and other Wizards. Prodigy does not double Azula's copy or firebending triggers. Sedgemoor Witch (Warlock), Professor Onyx and Ral (planeswalkers) are not doubled either |
| 23 | Copy multipliers "double every copied spell"; speed package = medium (§7) | PARTLY | Additive per source: two Veyrans give 3 triggers (2021-04-16), two Thrones 3 (2023-11-10), two Staves 2 extra copies (2020-04-17). Different cards stacking is inferred, not ruled. Copies per spell = (1 + extra triggers) x (1 + Staff extras); Veyran + Throne + Staff on an instant = 6 copies. Each copy still triggers magecraft once (Storm-Kiln 2021-04-16) |
| 24 | Strionic Resonator copies Azula's copy trigger once per turn (§3) | PARTLY | Oracle "{2},{T}"; Strionic Resonator (2018-03-16): copies a triggered ability on the stack, resolution choices made separately. No ruling covers a trigger that says "that spell". Lithoform Engine (2020-09-25): "triggers additional times" effects do not apply to copying an ability, so Throne/Veyran don't double the Resonator copy |
| 25 | Twinning Staff: each Azula copy becomes two; Staff {7} on Dramatic Reversal loops with rocks making 4+ (§3, §5) | CONFIRMED | Oracle: "If you would copy a spell one or more times ... plus an additional time" (any spell, not only instants); Staff rulings (2020-04-17). Arithmetic checked: net 2R-7 per cycle |
| 26 | Open (b): Shaun's token gives no firebending (not declared) but has the copy trigger (§8.2b) | CONFIRMED | Shaun (2024-03-08): token "was never declared as an attacking creature", attack triggers don't fire; it is attacking, so the "while attacking" condition is met. Oracle: token is "not legendary", so no legend rule |
| 27 | Open (b): Helm of the Host token = hasty non-legendary Azula: second firebending and copy trigger (§3) | CONFIRMED | Oracle; Helm (2018-04-27): not legendary, gains haste. It is created at beginning of combat, so it can be declared an attacker: firebending triggers |
| 28 | Helm of the Host + Godo = infinite combats, commander-free (§5) | CONFIRMED | Helm (2018-04-27): the non-legendary exception is copiable; oracle of Godo (untap and extra combat on first attack each turn per object) |
| 29 | One extra-turn spell cast while she attacks gives 2 extra turns (§5) | CONFIRMED | Time Warp / Temporal Manipulation (2022-12-08), Alchemist's Gambit (2021-11-19): several extra-turn effects in one turn are all taken, newest first; Tempt with Mayhem (2024-06-07): when the copied spell grants extra turns they are "added one at a time" |
| 30 | 49 pool cards mention extra turns; only Nexus of Fate and Final Fortune are instants needing no flash enabler (§5) | CONFIRMED | Pool scan: 49 matches; instants among them: Final Fortune, Nexus of Fate (Gerrard's Hourglass Pendant has flash but only stops turns). Nexus: original is shuffled (2018-07-13), copy ceases |
| 31 | "Three of them stop extra turns: Gerrard's Hourglass Pendant, Stranglehold, Ugin's Nexus" (§5) | PARTLY | Pendant and Ugin's Nexus skip any player's extra turn. Stranglehold (oracle) skips only an opponent's, so it does not stop the owner's. Rulings (2022-09-09, 2014-09-20, 2011-09-22): the turn is still created and skipped only when it would begin |
| 32 | Extra-turn permanents with activated abilities are not copied unless the permanent spell is cast in combat (§5) | PARTLY | True for Azula alone. Return the Favor mode 1 copies an activated ability (2024-04-12), so it doubles Time Sieve, Magistrate's Scepter, Sage of Hours (a candidate). Return the Favor, Expansion (MV 4 or less), Reiterate, Dualcaster Mage and Twinning Staff also copy extra-turn spells without Azula |
| 33 | Chain of Smog + any magecraft payoff: "copy it any number of times" (§5) | PARTLY | Chain of Smog: 0 rulings; oracle: the target player discards two cards each time. Needs an empty hand (or equivalent), which the report omits. Magecraft triggers per copy (Storm-Kiln 2021-04-16) |
| 34 | Hullbreaker Horror + Sol Ring / Mox Amber nets mana per cycle (§5) | CONFIRMED | Oracle (cast trigger bounces a nonland permanent); Mox Amber (2018-04-27): color from your legendary creatures (Azula supplies it). Net +2 per cycle checked |
| 35 | Twinning Staff + Dramatic Reversal / Narset's Reversal (§5) | CONFIRMED | Oracle and Staff rulings (copy resolves before the original, which stays on the stack) |
| 36 | Birgi + Grinning Ignus is mana-neutral: unbounded casts (§5) | CONFIRMED | Oracle; Grinning Ignus (2021-03-19): it is a mana ability. Cost 3, Birgi +1, Ignus +2 net = 0 |
| 37 | Storm-Kiln + Haze of Rage (buyback storm) and Reiterate + Seething Song (§5) | CONFIRMED | Haze of Rage (2022-12-08): storm copies are not cast but magecraft counts copies; Reiterate (2021-03-19). Reiterate loop nets +1 per cycle |
| 38 | Candidate chain: Storm-Kiln + Archaeomancer + Sublime Epiphany + Azula (§5) | CONFIRMED | Every step is ruled: copy keeps modes, retargets (Mystic Confluence); triggers wait for resolution end (Mystic Confluence); Archaeomancer (2018-12-07): can target the spell that put it onto the battlefield; Storm-Kiln magecraft per copy |
| 39 | Commander-free pairs list (Kiki-Jiki, Dualcaster, Scepter, Oracle, Niv-Mizzet, Worldgorger, Sanguine Bond) (§5) | CONFIRMED | Oracle level only (all in pool, pieces read); loop legality itself is CR 727 (unverified). Tainted Pact + Oracle fails in singleton with duplicate basics left (oracle) |
| 40 | Lock flags: Tidal Barracuda, Conqueror's Flail, Teferi, Mage of Zhalfir (§5) | CONFIRMED | Barracuda (2020-04-17): opponents can't cast during your turn, can still activate abilities; Flail (2016-11-08); Teferi (2021-03-19): sorcery timing only |
| 41 | Ritual arithmetic: Dark Ritual "6 for 1", Seething Song "10 red for 3" (§3) | PARTLY | Azula: "any other mana you add during combat will still be lost" between steps. Only firebending mana persists; red also persists with Electro/Ashling; Birgi keeps its own R. The burst must be spent inside one step |
| 42 | Lightning Greaves' shroud blocks your own targeting; Equip {0} lets it move (§1, S6) | CONFIRMED | Lightning Greaves (2020-08-07): cannot simply unequip; if she is the only creature you can't target her (equips, Palace, Passage) until you have another creature to move it to |
| 43 | Slip Out the Back / Talon Gates: protection by phasing out (§3) | PARTLY | Rulings 2022-04-29 / 2024-06-07: an attacker that phases out is removed from combat, so the copy window and any later firebending end for that combat. The report omits this cost |
| 44 | Fire Nation Palace: separate firebending 4 trigger, +RRRR, net +1 (§3) | CONFIRMED | Fire Nation Palace and Azula (2025-10-02): multiple firebending instances trigger separately; must be active before attackers are declared |
| 45 | Delayed Blast Fireball "5 if foretold" (§3) | PARTLY | DBF (2022-06-10): 5 if cast from exile for any reason. A copy "wasn't cast from" any zone (Coal Stoker 2022-12-08; Sevinne's Reclamation 2019-08-23), so by analogy it deals 2; not ruled for this card |
| 46 | Mana Drain: mana "next main phase" (§3) | CONFIRMED | Mana Drain (2020-11-10): cast during combat, mana comes at the postcombat main phase. With a same-target copy the original fizzles and gives none |
| 47 | Extra combats: Great Train Heist / Savage Beating, copies add combats (§5) | PARTLY | Spree copy keeps its modes (Great Train Heist 2024-04-12), so each copy adds a combat phase; no main phase between (Heist; Savage Beating 2004-12-01). Whether firebending mana survives into the next combat phase is not ruled (keyword text "until end of combat" vs ruling "until second main phase") |
| 48 | Undying Malice / Fake Your Own Death / Kaya's Ghostform / Malakir Rebirth "return Azula" (§3) | PARTLY | Kaya's Ghostform works once (2019-05-03). Azula is a commander: the owner may move her to the command zone after she dies (Sauron 2023-06-16; Iname 2021-06-18), which loses the recursion. To use it she must be left in the graveyard (CR 903.9a, unverified) |
| 49 | 65 Spellbook variants give "infinite turns plus lock" (§6) | NOT COVERED | Spellbook data. Components are ruled (Narset's Reversal 2019-05-03: copy resolves first, spell returns to hand), but loop validity is CR 727 (unverified) and Spellbook's own classification |
| 50 | MLD, stax, tutor and Game Changer statements (§4, §5) | NOT COVERED | Wizards bracket text, not Oracle rulings; the rulings file cannot settle them |

Counts: 35 CONFIRMED, 1 CONTRADICTED, 12 PARTLY, 2 NOT COVERED (50 claims).

## 3. Facts for the extra-turn decision (facts only, no policy)
- The copy is not optional. Only the choice of new targets is. There is no way to decline it once she is attacking (row 1).
- It exists only for spells cast while she is an attacking creature. An extra-turn sorcery cast in a main phase is never copied (row 2); sorceries are copied only with a flash enabler, instants (Nexus of Fate, Final Fortune) need none (row 30).
- What is copied: the spell as cast. Same X, modes, number of targets and divided damage; targets may change; effects tied to additional or alternative costs apply as if paid; no cast trigger; not "cast from" any zone; the copy resolves before the original and even if the original is countered (rows 4, 8-10, 45; Azula 2025-10-02).
- Result for one extra-turn spell: copy and original each resolve and each creates an extra turn: two consecutive extra turns, newest first (row 29). Nexus of Fate: original shuffles back, copy vanishes. Lose-the-game cards (Final Fortune, Last Chance, Warrior's Oath, uncleaved Alchemist's Gambit): the first extra turn taken ends in a loss (row 18). For "target player takes an extra turn" spells the copy may be retargeted (Azula), so both turns can still be the owner's.
- Skips: Gerrard's Hourglass Pendant and Ugin's Nexus skip every extra turn when it would begin; Stranglehold only the opponents' (row 31).
- Other sources of the same duplication exist in the candidate list and are independent of Azula: Return the Favor (also copies activated abilities), Expansion (extra-turn cards with mana value 4 or less: Final Fortune, Last Chance, Warrior's Oath, Savor the Moment, Stitch in Time, Alchemist's Gambit, Temporal Extortion), Reiterate, Twinning Staff, Dualcaster Mage (row 32).

## 4. Rulings or derivations the report missed (impact)
| # | Item | Impact | Source |
|---|---|---|---|
| M1 | **Self-copy loop (derived)**: with Azula attacking, a copy of Expansion, Reiterate or Return the Favor (mode 1) may target the original spell, then every copy creates another copy of it, with no mana. Any magecraft payoff turns it into unbounded Treasures, drain, pings or draws. No Spellbook variant in the file uses these cards | Floor-4 candidate, loop class missing from §5 and §6. Expansion // Explosion is `strong`, Return the Favor `situational`, Reiterate named only with Seething Song. The `core` payoffs (Storm-Kiln, Archmage Emeritus) make it a 3-card combo with the commander. Needs Phase 2 confirmation; every step is ruled, the loop shortcut is CR 727 (unverified) | Expansion // Explosion (2024-01-12): copy any instant/sorcery up to MV 4, copy resolves before original, new targets; Reiterate (2021-03-19); Return the Favor (2024-04-12); Azula (new targets); Storm-Kiln (2021-04-16) |
| M2 | Copy and trigger resolve before the spell and "even if the spell is countered before the copy is created" | Counterspells on the original do not stop the copy; the hazard list should not imply they do | Azula 2025-10-02 |
| M3 | Other mana is lost between steps; only firebending persists | Ritual bursts are step-bound; changes the "6 for 1" and "10 for 3" claims and speed modelling | Azula; Fire Nation Palace (2025-10-02) |
| M4 | Magecraft triggers once per copy created, including copies from Staff and multiple triggers | Confirms the speed package multiplies magecraft linearly per copy | Storm-Kiln, Archmage Emeritus (2021-04-16) |
| M5 | Firebending is not a mana ability: it uses the stack and can be responded to | Opponents can respond to the trigger; low impact | Azula 2025-10-02 |
| M6 | A resolving copy of a permanent spell is not "created": no token-creation interaction | No doubler chains through Azula's copies; token-count payoffs do not see them. Positive for bracket fit | Azula; Lithoform Engine 2020-09-25 |
| M7 | A copy of Electrodominance makes you cast another free spell (oracle, X kept): two free casts, each copied | Raises burst and extra-turn reach (MV <= X, timing ignored) | Electrodominance 2024-04-12; Azula |
| M8 | "If you cast it" ETBs do not fire on a token copy (Eon Frolicker, Transcendent Dragon) | Only the cast original counters (Transcendent Dragon); the token copy does not. Not in the report | Coal Stoker (2022-12-08) by analogy; oracle |
| M9 | Azula's triggers resolve before the spell, so a flash creature copy's ETB resolves before the original enters | Explains why both ETBs fully happen even with the legend rule (row 16) | Twinning Staff 2020-04-17; Azula |

## 5. Required report changes, by severity
1. **High: add the self-copy loop (M1)** to §5 and §6. Exclude Reiterate outright (not only "with Seething Song"), exclude Return the Favor and Expansion // Explosion, or tier them out while any magecraft payoff is in the list. Add them to the safe-halves list as "never with Azula". Ask Phase 2 `find-my-combos` to confirm.
2. **High: row 22.** §8.2(c) and §3: Harmonic Prodigy does not double Azula; it only doubles Shaman/Wizard engines. Say which of the three multipliers affects which trigger.
3. **Medium: §5 extra turns.** Fix "three of them stop extra turns" (Stranglehold is opponents-only). Add the facts of section 3: other copy sources (Return the Favor, Expansion, Reiterate, Staff, Dualcaster) duplicate extra turns and activated abilities without Azula; correct "not multiplied" for activated-ability permanents.
4. **Medium: §7 speed.** State that multipliers stack additively per source and multiplicatively with Twinning Staff (rows 23, 25; M4). Two or three multipliers are more than "double".
5. **Medium: §5 hazards.** Pact of Negation is conditional (row 17); add the empty-hand requirement to Chain of Smog (row 33); add "copy keeps costs-based effects as paid" (row 10); add Swift End's second 2 life (row 15).
6. **Low: §1 weaknesses.** Replace "blockers or removal cast in response to the first spell turn the engine off" with the ruled facts: copy resolves even if the spell is countered (M2); phasing out or losing the creature type removes her from combat (rows 2, 43); a blocker alone does not (unverified).
7. **Low: wording.** Roaming Throne does not fire firebending "for every spell" (row 20); Lightning Greaves' Equip {0} needs another creature (row 42); Delayed Blast Fireball is 5 if cast from exile and the copy is not (row 45); rituals are step-bound (row 41); recursion cards need her left in the graveyard (row 48); firebending mana across extra combats is unknown (row 47).
8. **Low: §8.2.** Close items (a), (b), (c), (d) as answered in rows 6, 26, 27, 19-22, 8-11; keep only the open questions below.

## 6. Questions the rulings could not answer
1. Does firebending mana survive into an additional combat phase (Great Train Heist, Savage Beating)? Ruling says "until you ... go to your second main phase"; keyword says "until end of combat".
2. Does a copy of a spell cast from exile (Delayed Blast Fireball) deal the 2 or the 5? Analogous rulings point to 2.
3. When Strionic Resonator or Return the Favor copies Azula's trigger, does "that spell" still refer to the spell that triggered it (CR 707.10, unverified)?
4. If she is removed after her trigger goes on the stack, does the copy still happen (CR 113.7a, unverified)? The ruling only covers the spell being countered.
5. Do different "triggers an additional time" sources add up across cards (Veyran + Throne + Prodigy)? Only same-card rulings exist.
6. Is the self-copy loop (M1) a valid shortcut and how does Layer A classify it (CR 727, unverified; Spellbook has no variant)?
7. Exact timing of moving a dying commander to the command zone against "dies" triggers (CR 903.9a, unverified; Sauron and Iname rulings only imply it).

## 7. Checks run
| Check | Result |
|---|---|
| Azula rulings read | 12 of 12 |
| Core cards read | 13 of 13 (counts in section 1) |
| Cards queried for rulings | about 150 exact names; face-only matches excluded |
| Extra-turn scan of the pool | 49 cards, 2 instants; matches the report |
| Report edited | No. This file is the only write |
