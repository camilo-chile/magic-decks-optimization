# Fire Lord Azula: collection-only optimization (Phase 2 step 10.1, 2026-11-14)

## Fix round (iteration 3 fix, 2026-11-21, Opus 5.5 max)

Status: DONE. Three swaps; Rogue's Passage and the 36 lands stay. Bracket PASS, gate PASS (4 WARNs, one fewer than before). The
sections below this one describe the list before this round where they differ (Spell Pierce, Go for the Throat, Abrade, Octopus
Form OUT, "five cheap counters"): this section wins. Read: the brief, the owner's card review, the lessons, the decisions file,
the review of 2026-11-14, the gate report, the guide, the Salt diagnosis and Azula's Salt rows, the primer, the pool (held_by
checked against the four deck files today: 0 mismatches, so every copy taken is free and none is held by Ezio, Toph or Kilo).
Web read today (data): Scryfall API, the live Game Changer list (53 cards; only Narset is owned in Grixis) and the Oracle text
and rulings of Fire Lord Azula, Bitter Triumph, Theater of Horrors, Octopus Form and Kolaghan's Command.

| Out | In | Language | Reason |
|---|---|---|---|
| Spell Pierce (EN SOA 23, back to the English binder) | Octopus Form | EN (TLA 66, English binder, 2 free) | Question 2. Protection replaces protection (13 pieces by tag against the attack-engine class 6 to 10). Spell Pierce is a soft counter (R20: early tempo only; late, three opponents keep {2} up). Octopus Form never gets worse: for {U} at instant speed Azula gains hexproof, which also stops targeted ABILITIES (counters do not), +1/+1 (+2/+2 copied: she wins the block), and it untaps her after her attack, so she blocks on the crack-back. A cheap window instant: magecraft triggers, Thermo untap, the target the Storm-Kiln and Return the Favor loops need. |
| Go for the Throat (EN ACR 91, back to the English binder) | Bitter Triumph | EN (TDC 173, the only copy, free: Ezio cut it in iteration 3, after Azula was frozen) | Same cost and color, but it kills ANY creature (artifact creatures too) or a planeswalker. Azula's copy skips the discard or 3 life (ruling 2025-10-02). Brings back the instant planeswalker answer lost with Hero's Downfall. |
| Abrade (EN BLC 191, back to the English binder) | Theater of Horrors | ES (DSC 236, the only copy, no English one owned; free: Ezio held it until iteration 3) | Draw is the one base function under its floor (owner L2: Azula needs the most draw; review I2: about 9 effective). Removal is the surplus function (16 by tag against a target of 10). Theater is a card every upkeep that works without Azula (lands too); I play those cards during my turn once an opponent lost life: Azula's hit on the player who never blocks, a Thermo-Alchemist ping, or its own {3}{R} ping. Its instants cast during her combat are copied (firebending mana lasts through the combat damage step, ruling). Artifacts stay answered by Kolaghan's Command and Chaos Warp (plus Venser and Aether Gale); small creatures by the rest. |

**Rejected after a gate run: Octopus Form for a land (the lead's suggestion).** I first cut Rogue's Passage (better than a basic:
it keeps the colored sources) and ran the gate: a new WARN, "35 lands, the profile asks 36 to 36". This deck's band is exactly
36 (spellslinger 34 to 36 overlapped with the combat modifier 36 to 38), and the skill forbids cutting lands below the band to
make room for spells unless the owner reviews it. The simulation agrees that the 36th land is real: see question 2.

### Question 1: the owner's two swaps of 2026-11-15

**Kolaghan's Command for Failed Fording: KEEP, and Failed Fording was the right cut.**
- Kolaghan's Command is a two-for-one at instant speed. It brings the deck's only creature recursion (Dualcaster Mage,
  Storm-Kiln Artist, Archmage Emeritus, Torrential Gearhulk or Venser back to hand) and, after this round, the main instant
  artifact answer beside Chaos Warp. Its 2 damage kills mana creatures and x/2 utility creatures.
- Correction to the note of 2026-11-15: a copy keeps the two chosen modes; only the targets change (ruling 2015-02-25, "you
  can't choose new modes"). With Azula attacking it is the same two modes twice, not four modes.
- Failed Fording was the weakest answer for a 4-player pod: a temporary one-for-one. Its jobs stay covered:
  - any nonland permanent: Chaos Warp, Venser, Aether Gale;
  - Azula saved from a wipe: Snap, Venser;
  - tokens: Day of Black Sun, Aether Gale.
- Enchantment answers stay at 3 (Chaos Warp, Venser, Aether Gale, plus the counters on the stack): R19 asks 2.

**Chromatic Lantern for Octopus Form: the card added was right, the card cut was wrong.**
- Lantern stays. Simulation (40,000 to 60,000 games per variant; one land a turn, rocks and Nightscape Familiar modeled; colors
  checked; throwaway script `C:\Users\Usuario\AppData\Local\Temp\claude\dbd938bef9190e9c\1e7b0ae2-e522-4c09-97d2-40efe09a9152\scratchpad\azfix\manasim.py`,
  not kept in the repository), against the same list without it:
  - Azula castable by turn 4: +1.8 points (77.4 % against 75.6 %); by turn 5: +1.8;
  - six mana by turn 6: +1.5;
  - {U}{U} on turn 4: +2.2 points; {R}{R}: +1.6; {B}{B}: +2.4.
- It fixes the double pips of all three colors: Turnabout, Narset's Reversal, Archmage, Venser, Gearhulk and Aether Gale in blue;
  Comet Storm, Electrodominance, Return the Favor, Dualcaster and Electro in red; Day of Black Sun and Ozai in black. It also
  turns Rogue's Passage into a colored source.
- R9 prefers 2-mana rocks, but the free ones are gone: Fellwar Stone and Rakdos Signet are Ezio's, Commander's Sphere is Ezio's
  and Kilo's, all frozen. Of the free 3-mana rocks, Lantern beats Dimir Locket and Pristine Talisman.
- Octopus Form was the wrong card to cut. It comes back (question 2), so the net change of the two owner swaps plus this round
  is Kolaghan's Command and Chromatic Lantern in, Failed Fording and Spell Pierce out.

### Question 2: Octopus Form IN, for Spell Pierce, not for a land

The lead's option (a basic land, 36 to 35) was tested and rejected for three reasons:
1. The gate warns: this deck's land band is exactly 36. The skill's cut discipline forbids cutting lands below the band to make
   room for spells unless the owner reviews it.
2. The simulation (same model as question 1) shows a real cost:

   | Cut | Azula by turn 4 | Six mana by turn 6 | Seven mana by turn 7 | Three mana or less on turn 4 | {U}{U}+2 on turn 4 |
   |---|---|---|---|---|---|
   | none (36 lands) | 77.4 % | 58.3 % | 42.5 % | 15.0 % | 70.7 % |
   | one Island | -1.3 to -1.7 | -3.0 to -3.5 | -2.8 to -3.7 | +1.5 to +2.3 | -3.1 |
   | Rogue's Passage | -0.3 | -3.1 | -3.1 | +1.6 | -0.6 |

3. The deck's best turn scales with LANDS, not rocks: copied Turnabout untaps every land twice, and the loop needs 4 lands to
   net mana. Godo, Gearhulk and Ozai cost 6.

Protection is the surplus function: 13 pieces by tag against the attack-engine class of 6 to 10. So Octopus Form replaces the
weakest protection piece, Spell Pierce:
- Spell Pierce is a soft counter (R20: early tempo only). Late in a 4-player game the caster usually has {2} up.
- Octopus Form never gets worse. For {U} at instant speed, Azula gains hexproof, which stops removal spells AND abilities (the
  counters stop spells only). She gets +1/+1, or +2/+2 when copied, so she wins the block. It untaps her, so she blocks on the
  crack-back.
- It is also the cheap instant the Storm-Kiln + Reversal and Return the Favor loops need as a target.

Protection after the swap, in layers:
- hexproof: Swiftfoot Boots, Champion's Helm, Octopus Form;
- redirects: Deflecting Swat, Redirect Lightning, Return the Favor, Narset's Reversal;
- counters: Swan Song, Negate, Mana Leak, plus Venser.
The win-turn shield keeps 8 pieces at MV 2 or less or free (R24 asks 3); defense_while_tapped rises from 4 to 5.

### Further improvements from free copies (two swaps, table above)

- **Bitter Triumph for Go for the Throat.** A straight upgrade in the same slot. Go for the Throat misses artifact creatures (the
  owner's own Kilo deck is built on them) and planeswalkers. Bitter Triumph pays 3 life on the cast; Azula's copy pays nothing.
- **Theater of Horrors for Abrade.** A draw engine from the removal surplus:
  - Spot answers go from 16 to 14 by tag (target 10). The answers that cost 2 or less: Heartless Act, Terminate, Bitter Triumph,
    Snap, Swan Song, Negate, Mana Leak, Narset's Reversal (8; R19 asks 5).
  - Artifacts stay answered by Kolaghan's Command and Chaos Warp, plus Venser and Aether Gale (R19 asks 2).
  - Draw goes from 11 to 12 by tag, about 10 effective. The gate's draw WARN closes; no card was relabeled.
  - Theater works with Azula dead (a Thermo-Alchemist ping or its own {3}{R} ping meets the condition) and plays lands.
  - It plays to the owner's pod: one opponent never blocks, so Azula's hit meets the condition after combat damage. Its instants
    are still cast while she attacks and are copied.

Considered and left out (each against the card it would replace):

| Card (free) | Verdict | Reason |
|---|---|---|
| The Last Agni Kai (EDHREC 46 %) | OUT | Mana is not the bottleneck in the window (firebending, Treasures, untaps, three bankers). Each fight hits Azula: two 2/2s kill her. A token player sacrifices the target and it fizzles. |
| Haunted Cloak (for Champion's Helm) | OUT | Haste, vigilance and trample against the second permanent hexproof and +2/+2. With only Boots as permanent hexproof, the Helm stays. Neutral at best. |
| Escape Detection, Unexplained Disappearance, Failed Fording | OUT | Temporary creature bounces. Snap and Venser already bounce, Venser bounces spells too. |
| Ty Lee, Chi Blocker | OUT | A 2/1 flash lock. A copy made in the window dies to the legend rule, and its lock ends with it. |
| Malcolm, the Eyes; Zuko, Exiled Prince; Azula, On the Hunt; Lion Vulture | OUT | Draw engines on bodies that die in blocks or to pingers. Theater draws with no body to protect, and plays lands. The owner found Lion Vulture slow with Azula. |
| Professor Zei | OUT | A rummage and one regrowth. Gearhulk and Teachings' flashback cover recursion. |
| Hero's Downfall, Murder, Fatal Push, Lightning Axe | OUT | Bitter Triumph does their job cheaper or without conditions. Axe loses a card outside the window. |
| It'll Quench Ya!, Deny Entry, Redirect | OUT | Worse than the counters and redirects in the list. |
| Opt, Consider (ES) | OUT | Cantrips: fuel, not draw. The slot went to an engine. |
| Cloud Key (ES), Dimir Locket | OUT | 3-mana permanents that compete with Azula on turn 3. Lantern fixes more. |
| Cursed Recording | OUT | 20 damage to me every seventh instant or sorcery. |
| Blasphemous Act, Chain Reaction (ES), Inundate | OUT | They kill or bounce my engines. Salt would count them as wipes, but the deck would play worse. |
| Royal Assassin, Deadeye Navigator, Waterbending Lesson, Lo and Li, Reckless Handling, Loyal Inventor, Entomb | OUT | Reasons in section 6 below stand. |
| Embodiment of Fury (ES; the owner's Toph question) | OUT | Its land creatures need landfall. Azula has no land plan. |
| The cards Ezio, Toph and Kilo left free (Murder, Nekrataal, Dimir Locket, Faithless Looting, Intruder Alarm, Liquimetal Coating, Rumble Arena, White Lotus Hideout, Survivors' Encampment, Adéwalé, Lydia Frye, Roshan, Thorn of the Black Rose, Ember Island Production) | OUT | Sorceries never copied, colorless or tapped lands, or Assassin cards. Only Bitter Triumph and Theater of Horrors beat a list card. |

### Rules points added (Scryfall rulings read today)
| # | Point | Status | What falls if wrong |
|---|---|---|---|
| R11 | Azula's copy of Bitter Triumph pays no discard or life. | Azula ruling 2025-10-02: a copy pays no additional costs. Gearhulk casting it still pays them. | Its window value |
| R12 | Cards cast from Theater of Horrors during Azula's combat are copied. Firebending mana lasts through the combat damage step, so they can follow her hit. | Azula rulings 2025-10-02 (the copy is made on cast; firebending mana lasts until the second main phase). Theater ruling 2019-01-25 (normal timing; lands only in a main phase with a land drop left). | Theater's window value |
| R13 | Untapping an attacking creature (Octopus Form) does not remove it from combat, so Azula keeps copying. | Comprehensive Rules 506.4, from memory, not re-read. | Only the order of play: cast Octopus Form after the last spell of the window. |
| R14 | A copied Kolaghan's Command keeps its two modes. | Ruling 2015-02-25. | The guide's wording |

### Checks (run 2026-11-21)
- `python scripts/check_phase2_bracket.py decks/phase2/fire-lord-azula.txt`: **PASS**. Floor 3, 1 Game Changer (Narset; live list
  of 53, read today), 0 extra turns, 0 mass land denial, 0 reversible. Spellbook: 6 variants, 2 flagged and both floor 3 (Narset's
  Reversal + Return the Favor, reviewed by the owner; Godo + Helm of the Host, late).
- `python scripts/plan_density.py`: **PASS**, 0 failures, 4 WARNs (before: 5):
  - attackers 5 of 12: modifier line; one attacker is the whole engine;
  - haste 3 of 4: support. The strong lists spend on protection (review I3), and Siege on Temur is the fourth piece;
  - team_evasion 4 of 6: Azula triggers on attacking, not on connecting;
  - ramp 11 of 12: the free 2-mana rocks are gone; window mana covers the rest.
  The reasons in section 3.3 below stand. The draw WARN closed.
- Plan file:
  - three tags swapped; Spell Pierce left wipe_insurance, and Snap and Venser came in (both return Azula to hand in response,
    then she costs 4 with no tax);
  - Octopus Form joined defense_while_tapped;
  - Venser added to spell_density: a flash card the window copies, missing before;
  - stale Black Market Connections text removed from the plan and route B.
  Counts: spell_density 32, spell_payoffs 11, wide board 14, big creatures 17, window_mana 13, bad when drawn 8 early and 1 late,
  0 orphans.
- 100 cards. Every card is held by Azula or free (0 shortfalls). The curve: MV 0 to 6+ = 1/7/25/17/8/2/3, average 2.67 (was 2.65).
  33 cards at MV 2 or less. 27 instants and 5 flash permanents, 32 window cards. Lands, colored sources (U 19, B 17, R 18) and the
  keep rate (88 % with the free mulligan) are unchanged.

### Boards, gauntlet and tests (what changed)
- Board 2, big creatures: better. Bitter Triumph kills artifact creatures and planeswalkers. Octopus Form copied makes Azula 6/6
  after blocks.
- Board 1, chump blockers: unchanged. Day of Black Sun, Aether Gale, Thermo, Comet Storm, Godo.
- Gauntlet:
  - Fast combo: one 1-mana counter less (Spell Pierce). Artifact combos lose Abrade; Kolaghan's Command and Chaos Warp remain.
  - Control: better. Theater keeps cards flowing with Azula answered.
  - Stax: unchanged.
- Disrupted games:
  - (a) Azula targeted on her first attack: Octopus Form answers for {U} and cannot be paid through.
  - (b) A wipe: 3 counters plus Snap and Venser. Theater is a seventh rebuild piece.
  - (c) The win spell countered: the shield still has 8 pieces.

### Salt (second measure; not measured in this step)
| Swap | Expected effect | Why |
|---|---|---|
| Spell Pierce to Octopus Form | keep (0 to -0.05) | Salt credits counterspells in Interaction (A- 316, far above its reference); Octopus Form adds to protection, already "Dense". |
| Go for the Throat to Bitter Triumph | keep (0 to +0.02) | The same slot with wider targets. |
| Abrade to Theater of Horrors | keep or lower slightly (0 to -0.05) | One removal and one artifact answer fewer. Salt may not credit conditional draw. |
| All three | about 6.8 to 6.9 (now 6.9) | The -0.55 structural ceiling (combos with no tutors to assemble them) is untouched: no free card tutors Storm-Kiln, Dualcaster or Godo. |

### Real power (1-10)
| List | Estimate |
|---|---|
| Before this round (2026-11-15 list, with the owner's two swaps) | 7.6 to 8.0 |
| **After** | **7.7 to 8.1, most likely about 7.9** |

- The gain: a protection piece that never goes stale, a draw engine that survives Azula, and removal that misses nothing. About
  +0.05 to +0.1.
- Confidence: medium-low (no games; the project's estimates have run high).

### Uncertain, and for the lead
1. Salt may read the list 0.05 lower (two interaction cards out). Real power rises; the brief puts consistency first.
2. Theater's yield depends on an opponent losing life on my turn. In a pod where all three opponents block Azula every turn,
   the Thermo ping or {3}{R} is the price.
3. Not touched, as instructed: `data/model/dashboard/guide-azula.json`, `decks/phase2/moxfield/`, `decks/phase2.json`. Each
   needs these swaps:
   - the guide: Spell Pierce, Go for the Throat and Abrade out; Octopus Form, Bitter Triumph and Theater of Horrors in; the
     Kolaghan's Command mode note;
   - the pinned copies (`scripts/assign_copies.py`): Bitter Triumph EN TDC 173, Theater of Horrors ES DSC 236, Octopus Form EN
     TLA 66.
4. If the owner prefers 35 lands anyway, cut Rogue's Passage, not a basic, and keep Spell Pierce: the colored sources stay
   intact (table above).

**Owner swaps (2026-11-15, two free copies that fell between decks; `decks/phase2/owner-card-review-20261114.md`).** Failed Fording out, Kolaghan's Command in (EN, M3C 268): a two-mode instant (artifact kill or 2 damage, plus discard or a creature back from the graveyard), four modes when copied while Azula attacks; a bounce was the weakest answer. Octopus Form out, Chromatic Lantern in (EN, FRC 54): ramp 10 to 11 and the black of Kolaghan's; protection 11 to 10, defense_while_tapped 5 to 4 (min 4). Bracket PASS (1 Game Changer), gate PASS (5 warnings, ramp now 11 of 12), 100 copies covered.

**Fix round (step 10.3, 2026-11-15, the lead on Opus 5.5 high; review `decks/reports/collection-review-fire-lord-azula-20261114.md`, verdict FIX).** Applied ranks 1 to 4 and the plan-file corrections:

| Out | In | Reason |
|---|---|---|
| Hero's Downfall | Return the Favor (EN SOA 47, free) | Owner's decision: kept unless irrefutably outside Bracket 3; Spellbook 11-5940 reviewed (`data/bracket-reviewed.json`). Seventh loop piece, redirects removal and edicts, forks Comet Storm. |
| Black Market Connections (back to Ezio) | Tome of Legends (EN MKC 246, free) | The copy adds more in Ezio (fixing, an Assassin a turn); the owner's rule puts a scarce copy where it adds the most. Tome is a draw engine that works without Azula. |
| Abandon Attachments | Venser, Shaper Savant (EN 2X2 66, free) | A rummage for a flash answer to any spell, creature spells and commanders included; two bounces in the window. |
| 1 Swamp | 1 Mountain | Red double pips outnumber black after Return the Favor. |

Plan file: Helm of the Host and Narset's Reversal leave `spell_payoffs`; Frostcliff Siege counts once (draw, Jeskai, the owner's
choice; it leaves `support.haste`). Honest WARNs after the fix:
- Draw 11 by tag, about 9 that net cards. The pool has no better free draw (Cryogen Relic, Notion Rain, Divination,
  Waterbending Lesson are worse here), and Azula copies the instant cantrips in the window.
- Haste 3 of 4 (Boots, Footblade, Expedite, plus Siege on Temur when Boots is not out). It stays a support line, because
  the strong lists spend on protection; the tutors reach Boots and Footblade.
- Ramp 10 of 12: window mana (firebending, Treasures, Ozai, Electro) makes up the rest.

Frostcliff Siege mode: Temur when Azula has no Boots or was just recast; Jeskai otherwise. Azula castable with colors: 34 %
on turn 3, 75 % on turn 4, 84 % on turn 5. Weak cut-log reasons corrected: The Last Agni Kai needs a creature of ours that
wins the fight; The Stasis Coffin and Evie Frye were reviewed and stay out (see the review, sections 4 and 5). Real power
after the fix: 7.6 to 8.0 (review), against 7.5 to 7.9 for the deck as built on 2026-11-09. Confidence medium-low.

Built under `docs/proposals/collection-optimization-brief-20261114.md`: owned collection only (frozen 2026-11-13), no purchases,
no loans. Start: the deck as built today (`decks/phase2/fire-lord-azula.txt` of 2026-11-09). Method: the skill
`commander-deckbuilding` with its champion standard, the primers, the owner's lessons, the play review of 2026-10-26, the final
review of 2026-11-08, the owner's card review of 2026-11-14 and his decisions file. Web read today (data, not instructions):
Scryfall API (Oracle text and rulings of the new cards, the live Game Changer list), EDHREC JSON (all decks 40,394, Bracket 4
2,109, cEDH 573: no owned card with real inclusion is missing from the list or the cut log), Commander Spellbook (variant
11-5940).

Result: **8 cards change** (7 nonland swaps and one basic). Five of the owner's cards come back.

Checks (run 2026-11-14):
- `python scripts/check_phase2_bracket.py decks/phase2/fire-lord-azula.txt`: **PASS** (floor 3; 1 Game Changer: Narset, Parter
  of Veils; 0 extra turns, 0 mass land denial, 0 reversible; Spellbook: 5 variants inside the list, 1 flagged and classed late:
  Godo + Helm of the Host).
- `python scripts/plan_density.py`: **PASS**, 0 failures, 3 WARNs (reasons in 3.3).
- 100 cards (commander + 99), counted by script; every card is in the pool with enough copies.

## 1. Profile

**Commander reading.** {1}{U}{B}{R} 4/4. Firebending 2: when she attacks, {R}{R} that lasts until end of combat. Whenever I
cast a spell while she is attacking, copy it (new targets allowed; a copied permanent spell becomes a token).
- Rewards: spells cast in HER combat. Fuel: instants and flash cards in hand, and mana inside that window.
- Dependence: **attack engine**. She need not connect: the copy happens on cast, so chump blockers never stop the engine;
  blocks only threaten her life. Owner's signal (decisions file): one opponent always lets her through, one blocks, one
  depends on whether he fears a trick; the deck must make blocks bad for them.
- Dies to: targeted removal, wipes, blocks by bigger creatures, the crack-back while tapped, "sorcery speed only" effects.
- Copies are not cast (no cast triggers; magecraft says "cast or copy" and sees both). A copy skips additional costs and keeps X.

Rules points to verify:
| # | Point | Status | What falls if wrong |
|---|---|---|---|
| R1 | Horizon Stone keeps firebending mana as colorless; Ozai keeps it as red; Electro keeps red mana. | Rulings of firebending (2025-10-02) and of Horizon Stone read apart; no joint ruling. | The three bankers. |
| R2 | Copies keep X and kicker; they skip additional costs (Big Score's discard). | Azula rulings. | Comet Storm 2X, Big Score. |
| R3 | Torrential Gearhulk cast while she attacks is copied: a token Gearhulk and the card, two triggers. Each trigger CASTS an instant from the graveyard, so Azula copies that instant too. | Oracle ("cast"); Gearhulk rulings 2016-09-20 read today; Azula ruling on permanent copies. | Gearhulk's value: 2 bodies + 4 instants instead of 1 + 1. |
| R4 | Gearhulk casts X spells with X = 0 and still pays additional costs (Big Score's discard). | Gearhulk rulings, read today. | Never bin Comet Storm, Electrodominance or Pull from Tomorrow as Gearhulk targets. |
| R5 | Reversal loops: Azula's copy of the Reversal must target the ORIGINAL Reversal; the copy it makes then copies and returns the other spell. | Spellbook variants; traced in the review of 2026-11-08. | Route A. |
| R6 | Turnabout: the choice (artifact, creature or land) is made on resolution, so the copy may choose differently. | Azula ruling ("choices made on resolution are made again"). | Red mana from the Signets inside the loop. |
| R7 | Shred Memory's transmute finds any card of mana value 2. X is 0 outside the stack, so Comet Storm, Electrodominance, Pull from Tomorrow and Day of Black Sun are mana value 2 in the library. | Comprehensive Rules 202.3e from memory; Scryfall gives `cmc` 2.0 for them. | Shred Memory as a tutor for the burn route. |
| R8 | Godo + Helm of the Host: each Helm token is a new Godo, its first attack adds a combat. | Spellbook variant; the bracket script classes it late. | Route C without Azula. |
| R9 | Imprisoned in the Moon on a commander: no zone change, so its owner cannot move it to the command zone. | Oracle. | The lasting commander answer. |
| R10 | Frostcliff Siege, Jeskai: one trigger per player dealt combat damage. | Ruling 2025-04-04, read today. | Its draw rate. |

**Plan.** Azula attacks every turn from turn 4, with haste and hexproof ready and five cheap counters and two free redirects
behind her. In her window every instant is doubled. The win comes in ONE protected combat: a three-card loop with her
(Narset's Reversal with Turnabout, Frantic Search or Storm-Kiln Artist; Snap with Dualcaster Mage) makes unbounded mana or
casts, and a multikicked, copied Comet Storm or Thermo-Alchemist turns it into lethal damage to each opponent.

**Backup (same pieces).** With no loop, Turnabout, Frantic Search, Big Score, Storm-Kiln Artist and banked mana (Horizon
Stone, Ozai, Electro, Treasures) pay for a copied Comet Storm or Electrodominance. With Azula answered, Godo fetches Helm of
the Host for unlimited combats, and Comet Storm is cast once with the banked mana.

**Speed.** Azula lands on turn 3 in about half the games and by turn 4 in 88 % (simulation, colors ignored). First copied
combat turn 4 to 5. First lethal threat to the table: turn 5 to 7 with a loop, turn 7 to 9 fairly (goldfish, section 5).

**Win routes, scored.**
| Route | Cards (with Azula) | Mana on the win turn | Access | Pieces useful alone | Single failure points |
|---|---|---|---|---|---|
| A. Loops | 3 | 6 to 8 (firebending pays 2) | 6 pieces + Mystical Teachings (copied: BOTH missing pieces) + Solve the Equation + Shred Memory + Gearhulk (recasts a used piece) + dig | all six | Azula removed; a counter on the key spell |
| B. Copied X burn | 2 | 10+ | Comet Storm, Electrodominance + the same three tutors | both (removal early) | a counter; half damage without Azula |
| C. Godo + Helm; Helm on Azula; Ozai | 1 to 2 | 11 over two turns | Godo fetches Helm | Helm on Azula doubles the copies | a wipe, artifact removal; does NOT need Azula |

No failure point is shared by all three. Only Gearhulk's recasts use the graveyard.

**Access to the loops** (simulation, 60,000 shuffles, Mystical Teachings counted as two pieces because the window copies it):
28 % by turn 6, 33 % by turn 8, 39 % by turn 10 with no draw spell at all; 39 %, 52 % and 64 % when the draw spells show 4, 7
and 10 more cards [J for those extras]. A finisher or a tutor for one: 49 % by turn 6 with no draw.

**How it beats three opponents.** Every route hits all three at once: Comet Storm with two kicks, Thermo-Alchemist's ping to
each opponent, unlimited combats. It wins in one turn from banked resources, not by attrition.

**What it fears.**
- A fast combo before turn 6: five counters, Narset's Reversal, instant removal.
- "Sorcery speed only" and "one spell a turn" effects: Chaos Warp, Failed Fording, Aether Gale first.
- A wipe after she is equipped: the counters; Boots and Frostcliff Siege stay, so she is recast with haste.
- Graveyard exile: it only blanks Gearhulk's recasts and Teachings' flashback.
- Pingers that kill the 1 and 2 toughness engines.

## 2. The puzzle: every card by function

Commander: **Fire Lord Azula**. Cast turn 3 to 4; attack every turn; cast instants in the declare-blockers step, after blocks.
Never present a lethal threat one turn before you can protect it.

**Ramp (7 rocks + 3 reducers).** All turn-1 to turn-3 plays.
- Sol Ring: turn 1; Azula on turn 3 with any second mana piece. Bad late.
- Arcane Signet, Izzet Signet, Dimir Signet: turn 2; all three make blue. Inside a Turnabout loop, untap artifacts once so
  the Izzet Signet makes the red for Comet Storm.
- Everflowing Chalice: turn 2 for one counter; late, two or three counters for X spells.
- Mind Stone: turn 2; late, crack it for a card.
- Bender's Waterskin: turn 3 with no 2-drop rock; mana on every opponent's turn for a counter or Mystical Teachings.
- Goblin Electromancer, Stormcatch Mentor: turn 2; every instant costs 1 less; with either one the Reversal + Snap loop
  nets mana.
- Nightscape Familiar: turn 2; Azula costs 3; blue and red spells cost 1 less; regenerates to block.

**Loop pieces (5).** Each is good alone; hold them for the protected combat.
- Narset's Reversal: the hub. Alone: return a removal spell aimed at Azula and keep a copy, or steal a draw spell. On a spell
  Gearhulk cast, it returns that card to hand instead of exile.
- Turnabout: copied, it untaps every land twice (8 lands: 16 more mana). With the Reversal: unbounded mana from 4 lands.
  Main phase: tap one player's blockers. Bad early.
- Frantic Search: free in the window (six lands untapped) and loots four. With the Reversal it digs four new cards and nets
  one mana a cycle: it finds Turnabout or Comet Storm; it is not a kill alone. Never loop it with Archmage out.
- Snap: free bounce of a blocker (four lands untapped). With Dualcaster Mage: the Snap loop. With the Reversal and a reducer,
  Electro or Thermo-Alchemist: a third loop.
- Dualcaster Mage: flash in the window, three copies of the best instant; out of combat, copy an opponent's tutor or removal.

**Engines and payoffs (7).**
- Storm-Kiln Artist: two Treasures per instant in the window; loops with the Reversal.
- Archmage Emeritus: two cards per instant in the window. Cast it with a counter up.
- Thermo-Alchemist: turn 2 blocker; one damage to each opponent per untap and per instant I cast, on any turn. The loop outlet.
- Electro, Assaulting Battery: {R} per instant cast and red mana kept between turns; when he dies, X to a player.
- Horizon Stone (proven role-player): banks firebending, Turnabout and end-step mana for X spells, equips and Godo.
- **Black Market Connections (IN, from Ezio):** turn 3 when Azula is not castable. Take the card and the Treasure every turn
  (3 life) while life is above 25, then the Treasure only. Treasures wait for the window. The 3/2 token only as a blocker.
- Glamdring // Gleam of Death: Gleam first (mill six, take every instant and sorcery). Glamdring on Azula: her instants cost
  4 less (Big Score {R}, Turnabout {U}{U}, Teachings {U}), which makes every Reversal loop positive.

**Finishers and second route (6).**
- Comet Storm: two kicks name all three opponents; copied, 2X each. Early, X = 2 to 3 kills blockers.
- Electrodominance: X to any target and a free spell from hand in the window, copied: Gearhulk or Godo at X = 6, Aether Gale
  at X = 5 (twelve permanents bounced).
- **Torrential Gearhulk (IN):** cast it in the window with two instants in the graveyard: a token Gearhulk and the card, each
  recasts an instant for free, and Azula copies both. Best targets: Turnabout and Frantic Search (the Gearhulk is free and
  nets mana), Mystical Teachings (two more tutors), Fact or Fiction, Big Score (discard needed). On an opponent's turn: a 5/6
  blocker that recasts a counter or a removal spell. Mystical Teachings finds it. Bad early.
- Helm of the Host: on Azula, a hasty Azula every combat (every spell copied twice). Godo fetches it. Bad early.
- Godo, Bandit Warlord: turn 6+; Helm onto the battlefield; Helm on Godo: unlimited combats. Bad early.
- Ozai, the Phoenix King: cast before combat, he attacks at once and refunds {R}{R}{R}{R}; with Azula, six red mana per
  combat; he keeps all unspent mana as red. Bad early.

**Tutors and dig (5).**
- Mystical Teachings: in the window it is copied: Narset's Reversal AND Turnabout, the whole loop for the next combat. Or a
  piece and a counter, or Gearhulk. Flashback from the graveyard is copied too.
- Solve the Equation: main phase: the missing loop piece or Comet Storm.
- Shred Memory: transmute for a mana-value-2 card: the Reversal, Snap, Comet Storm or Electrodominance (R7), or Boots. At
  instant speed: exile four cards of a graveyard (copied: two graveyards). The deck's graveyard hate.
- Narset, Parter of Veils (Game Changer): turn 3; two activations dig eight cards for noncreature spells; opponents draw one
  card a turn.
- Brainstorm: end of an opponent's turn, or copied in the window (six cards seen). Put back cards a shuffle will remove.

**Draw (8).**
- Big Score: in the window: discard 1, draw 4, 4 Treasures.
- Thrill of Possibility: in the window: discard 1, draw 4. Discard an instant Gearhulk wants.
- Thirst for Knowledge: draw three at an end step, six in the window; discard a spare rock or equipment.
- Fact or Fiction: end of the last opponent's turn, or copied (two piles of the best cards).
- Pull from Tomorrow: end step with all lands; copied, 2X cards. Bad early.
- Abandon Attachments: {R}{R} of firebending pays it: discard two dead cards, draw four.
- Expedite: {R}; copied it draws two; out of combat it gives a recast Azula, Godo or Gearhulk haste.
- **Frostcliff Siege (IN):** turn 3 with no rock. Temur when Azula is not out or was just killed: she has haste with no
  equip cost (Azula on turn 4 attacks on turn 4), +1/+0 and trample. Jeskai when she is out with Boots: a card every turn
  she hits the opponent who does not block.

**Spot removal (9, plus Snap and the Reversal).** In the window each instant answers two permanents.
- **Heartless Act (IN):** two mana, kills almost any creature.
- Terminate, Go for the Throat: kill the blocker after blocks; the copy kills a second one.
- Hero's Downfall: creature or planeswalker.
- Abrade: 3 damage or an artifact.
- Chaos Warp: any permanent; the instant answer to an enchantment or a land.
- Failed Fording: bounce any nonland permanent; copied, two.
- Amphibian Downpour: flash in the window: storm and the copy turn several creatures or commanders into 1/1 Frogs.
- **Imprisoned in the Moon (IN):** main phase, on the commander the table fears most (it stays on the battlefield as a land),
  or on a planeswalker or a utility land. Never copied.

**Counters (4, five with the Reversal).**
- Spell Pierce, Swan Song: {U} each: the wipe, the removal on Azula, the counter aimed at my loop.
- Negate: any noncreature spell.
- **Mana Leak (IN):** the only cheap counter here that stops a creature spell (a commander, a finisher). Best on turns 2 to 6
  and whenever a player taps out. Late, use it on my own turn against a tapped-out player.

**Protection and haste (6).**
- Swiftfoot Boots: hexproof and haste; a recast Azula attacks at once for {1}.
- Champion's Helm: hexproof and 6/6: she wins most blocks.
- Hidden Footblade: {R}, flash: after blocks, first strike kills the blocker before it deals damage; haste on a recast.
- Octopus Form: hexproof in response, +1/+1 in a block, or untap her as a blocker.
- Deflecting Swat: free while she is out: send the removal to their creature, or a counter to another spell.
- Redirect Lightning: the same for {R} and 2 mana or 5 life.

**Mass answers (2).**
- Day of Black Sun: X = 0 for {B}{B} kills every token; X = 3 spares Azula. Never copied.
- **Aether Gale (IN):** main phase before the attack: six permanents back to hand, none of mine (tokens are gone for good):
  blockers before Godo's combats or a Siege hit, or the stax pieces before a loop turn. Needs six targets. Bad early.

**Utility (1).**
- Propaganda (proven role-player): turn 3; attackers hit the other players while Azula is tapped.

**Lands (36).** 7 Island, 5 Mountain, 5 Swamp; Command Tower, Exotic Orchard; Drowned Catacomb, Dragonskull Summit, Sulfur
Falls; Choked Estuary, Foreboding Ruins, Frostboil Snarl; Smoldering Marsh, Sunken Hollow; Shivan Reef, Sulfurous Springs,
Underground River; Cascade Bluffs, Sunken Ruins, Darkwater Catacombs, Shadowblood Ridge; Fire Nation Palace (firebending 4 on
the big turn); Rogue's Passage (Azula unblockable for {4}: a Siege card, or a safe attack).

Dead clauses: Failed Fording's Desert line (no Deserts); Black Market Connections' changeling types (no typal card).
Commander-centric count: cards weak without Azula: Deflecting Swat (3 mana then), Hidden Footblade, Octopus Form, Champion's
Helm, Fire Nation Palace's ability: 5, under 12.

## 3. Curve and ratios

| MV (X = 0) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Cards | 1 | 8 | 26 | 16 | 7 | 2 | 3 |

Average 2.60 (today's deck 2.48). 35 cards at MV 2 or less. Five cards at 5+: Horizon Stone (proven), Aether Gale, Godo, Ozai,
Gearhulk; each wins a game, answers six permanents or refills. Types: 30 instants, 4 flash permanents, 3 sorceries (+ Gleam),
11 creatures, 13 artifacts, 5 enchantments, 1 planeswalker.

### 3.1 Profile table (spellslinger, with combat_attackers as modifier)
| Function | Tier | Min | Target | Actual | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 36 | 36 | Overlap of the two bands; X spells, Horizon Stone and the Turnabout loop use every land. Lands + lasting ramp: 36 + 7 rocks + 3 reducers = 46. |
| Ramp | base | 12 | 12 | 10 + Black Market Connections (WARN) | 3.3. |
| Draw | base | 12 | 18 | 12 by tag | Four are engines now (Archmage, Black Market Connections, Frostcliff Siege, Narset) against two today; Gearhulk recasts a draw spell on top. |
| Spot answers (with counters) | base | 8 | 10 | 15, and 16 by tag with Shred Memory | 11 at MV 2 or less; 14 instant or flash. |
| Mass answers | base | 2 | 3 | 2 | Day of Black Sun; Aether Gale (one-sided, six targets). |
| Commander protection | attack engine | 6 | 8 | 6 + 4 counters + the Reversal | Hexproof: Boots, Champion's Helm, Octopus Form. Redirect: Swat, Redirect Lightning, the Reversal. Counters: Pierce, Swan Song, Negate, Mana Leak. |
| spell_density | gate early | 30 | 36 | 34 | Instants and flash only. |
| spell_payoffs | gate late | 6 | 8 | 9 + 3 tutors | Azula, Archmage, Storm-Kiln, Dualcaster, Gearhulk, Electro, Helm, the Reversal, Thermo. 8 without Azula. |
| through_wide_board | gate early | 10 | 12 | 11 + 3 tutors | Section 5, Board 1. Electro (one small flier) is the weakest count. |
| through_big_creatures | gate early | 10 | 12 | 15 + 3 tutors | Section 5, Board 2. |
| window_mana | declared late | 6 | 8 | 11 + 3 tutors | Bankers: Horizon Stone, Electro, Ozai. Treasures: Storm-Kiln, Big Score, Black Market Connections. Untaps: Frantic Search, Snap, Turnabout. Fire Nation Palace; Glamdring's discount. |
| Route access | champion | 10 | 12 | 13 | Six loop pieces, two finishers, Teachings, Solve, Shred Memory, Godo, Gearhulk; plus dig. |
| Win-turn shield | champion | 3 | 5 | 8 | Section 4. |
| haste | support | 4 | 6 | 4 | Boots, Frostcliff Siege, Hidden Footblade, Expedite. |
| team_evasion | support | 6 | 8 | 4 (WARN) | 3.3. |
| defense_while_tapped | support | 4 | 6 | 5 | Propaganda, Thermo-Alchemist, Nightscape Familiar, Octopus Form, Gearhulk (flash 5/6). |
| combat_draw | support | 4 | 6 | 5 | Archmage, Frostcliff Siege, Expedite, Thrill, Big Score. |
| wipe_insurance | support | 2 | 3 | 4 | Negate, Swan Song, Mana Leak, Spell Pierce. |
| attackers | support (modifier) | 12 | 16 | 5 (WARN) | 3.3. |
| cost_reducers | support | 2 | 4 | 4 | Electromancer, Stormcatch, Nightscape, Glamdring. |
| Graveyard hate | floor | 1 | 1 | 1 | Shred Memory. |
| Answers to commanders | floor | 2 | 3 | 3 lasting + 3 tempo | Imprisoned in the Moon, Amphibian Downpour, Chaos Warp; Snap, Failed Fording, Aether Gale. |
| Rebuild after a wipe | champion | 4 | | 6 | Azula recast with haste (Boots and Siege stay), Gearhulk, Black Market Connections, Pull from Tomorrow, Fact or Fiction, Godo. |

Fit check: ramp 10 + loop pieces 5 + engines 7 + finishers 6 + tutors and dig 5 + draw 8 + removal 9 + counters 4 +
protection 6 + mass answers 2 + Propaganda = 63; 36 + 63 = 99.

Answers against closers: 13 spot answers and 2 mass answers against 14 closers (Azula, Comet Storm, Electrodominance,
Gearhulk, Thermo, Ozai, Godo, Helm, Storm-Kiln, Dualcaster, Snap, the Reversal, Frantic Search, Turnabout). One more answer
than closers: here every instant answer is also window fuel.

### 3.2 Colors
Lands: blue 19, black 18, red 17; Rogue's Passage is colorless. Rocks add blue 4 (Arcane, Izzet, Dimir, Waterskin), black 3,
red 3. One Mountain became an Island: the new cards are blue ({U}{U} on Gearhulk and Aether Gale; Mana Leak, Imprisoned in
the Moon, Frostcliff Siege), firebending already pays {R}{R} in every window, and goldfish game 5 stalled on a second blue
source. No land always enters tapped.

### 3.3 WARN reasons (none passed by relabeling)
- **Ramp 11 of 12.** Seven rocks and three reducers, all castable by turn 3; the eleventh is Black Market Connections' second
  tag (a Treasure every turn from turn 4). The missing piece is mana only this commander makes: firebending, Turnabout,
  Snap, Frantic Search, Big Score, Storm-Kiln. A third 3-mana rock (Commander's Sphere is free) would compete with Azula on
  turn 3 and replace a window card.
- **Team evasion 4 of 6.** Frostcliff Siege (team trample), Aether Gale and Turnabout (blockers removed or tapped), Rogue's
  Passage. Azula's engine triggers on attacking, not on connecting, so the line matters only for the combat route and for
  Siege's card. Ozai and Electro are evasive attackers, not counted.
- **Attackers 5 of 12.** One attacker is the whole engine; twelve creatures would replace window instants.

## 4. Interaction and protection

**Interaction (15 spot answers, 2 mass answers).**
- At MV 2 or less (11): Heartless Act, Terminate, Go for the Throat, Abrade, Failed Fording, Snap, Spell Pierce, Swan Song,
  Negate, Mana Leak, Narset's Reversal.
- On an opponent's turn against a creature combo or a lethal attack: Heartless Act, Terminate, Go for the Throat, Hero's
  Downfall, Snap, Failed Fording, Abrade, Chaos Warp, Mana Leak, and Gearhulk recasting any of them.
- By permanent type:
  - artifacts: Abrade, Chaos Warp, Failed Fording, Aether Gale;
  - enchantments: Chaos Warp, Failed Fording, Aether Gale, and Swan Song, Negate or Mana Leak on the stack;
  - planeswalkers: Hero's Downfall, Imprisoned in the Moon, Chaos Warp;
  - lands: Imprisoned in the Moon, Chaos Warp;
  - graveyards: Shred Memory;
  - commanders: Imprisoned in the Moon and Amphibian Downpour (no zone change), then Chaos Warp.
- Use removal on the blockers that matter and on combo pieces, never on value creatures.

**Protection of Azula, in layers.** Hexproof (Boots, Champion's Helm, Octopus Form), redirects (Swat free, Redirect Lightning,
the Reversal), counters (Pierce, Swan Song, Negate, Mana Leak), recast with haste (Boots, Siege on Temur, Footblade, Expedite).
Nothing returns her from a resolved wipe without the tax (Undying Malice left for Mana Leak, which stops the wipe and more).

**Win-turn shield, 8 pieces at MV 2 or less or free:** Spell Pierce, Swan Song, Negate, Mana Leak, Narset's Reversal,
Deflecting Swat, Octopus Form, Redirect Lightning. Sequence: hexproof equipment on first; attack; cast the cheapest loop
piece first as bait; keep {U} and Swat; the Reversal last. A redirect aimed at a counterspell makes it target the redirect
itself, so it fizzles.

**Making blocks bad** (owner's signal): removal after blocks, copied; Hidden Footblade after blocks (first strike);
Champion's Helm 6/6; Octopus Form; Siege on Temur (5 power, trample); Aether Gale or Turnabout before the attack. Attack the
opponent who does not block.

**Politics.** Swan Song gives its target's controller a 2/2 flier: aim it at the leader. Swat and Redirect Lightning send a
removal spell at the leader's best creature. Propaganda pushes attacks elsewhere. Narset hurts the strongest draw engine
first. Aether Gale: say what you will not bounce.

**Against wipes.** Commit Azula and one engine, no more, when two opponents can wipe. Equipment, Siege, Black Market
Connections, Horizon Stone and Propaganda survive. Hold Gearhulk for their end step.

## 5. Mulligan, play pattern and tests

**Keep:** 2 to 4 lands (3+ with no 1- or 2-mana rock or reducer), a play by turn 3, and a plan piece or a way to find one
(Azula counts). Keep almost any land-good hand with: Sol Ring, a Signet, Mystical Teachings, Narset, Archmage, Black Market
Connections. Ship 0-1 landers, 6+ landers, answers-only hands, hands with no blue source.

**20 seeded hands (seed 1114, dealt before the Mountain-to-Island swap):** kept 12 on the first seven. Ships: five 1-landers
(hands 2, 7, 9, 13, 18) and three 2-landers with no cheap mana (5, 10, 15). Monte Carlo, 40,000 hands, same rule: 65.5 % keep
on the first seven, **88.1 % with the free mulligan** (target 85 %).

**Turns 1 to 5.** Turn 1 land, Sol Ring. Turn 2 a rock or reducer, or Thermo-Alchemist. Turn 3 Azula (with a rock), else
Black Market Connections, Frostcliff Siege (Temur), Narset or Propaganda. Turn 4 Azula, or attack: Teachings copied is the
best window play, then Big Score, Thrill or Thirst. Turn 5 Archmage or Storm-Kiln with a counter up.
**Turns 6 to 9.** The win turn when the loop is in hand and the shield is up. Otherwise Gearhulk in the window, a copied
Comet Storm, Helm on Azula, Godo if she is answered.
**Late.** Turnabout plus the banked mana for one huge Comet Storm; Godo + Helm; Pull from Tomorrow at end steps.

**Goldfish, five games played turn by turn (the first five kept hands with 3 to 4 lands; no opponents):**
| Game | Opening seven | Azula | What happened |
|---|---|---|---|
| 1 | Izzet Signet, Waterskin, Redirect Lightning, Hero's Downfall, 3 lands | T3 | T4 attack: Mystical Teachings (drawn T3) copied: Reversal and Turnabout. T5, five lands: the loop; Teachings' flashback, copied, finds Comet Storm; a Turnabout resolution untaps the Signet for red. **Kill T5** (the ceiling). |
| 2 | Thirst, Electro, Boots, 4 lands | T4 (no red source on T3) | T3 end step Thirst. T5: Boots on, Gearhulk in the window, copied; one trigger recasts Thirst, copied: six cards (Godo among them), two 5/6. One red source all game: Electro and Ozai are discarded. T6 Godo fetches Helm, T7 Helm on Godo: **kill T7**. |
| 3 | Boots, Imprisoned in the Moon, Fact or Fiction, 4 lands | T4 | Thermo T2, Boots T3. T5 Fact or Fiction copied (I assume the piles give Narset). T6 Narset's first dig finds two lands and two creatures: nothing, and Archmage and Dualcaster go to the bottom. No loop piece seen. T7 Godo (drawn), T8 Helm on Godo: **kill T8**, by the route that ignores Azula. Without Godo: Thermo's pings only, threat T10+. |
| 4 | Big Score, Thirst, Dimir Signet, Deflecting Swat, 3 lands | T3 | T4: Glamdring on Azula, then Big Score for {R} and Thirst for {U}, both copied: ten cards and four Treasures. T5 Black Market Connections. No finisher in the top 29 cards: **threat T8 to 9**. |
| 5 | Chalice, Solve the Equation, Swan Song, Go for the Throat, 3 lands | T4 | One blue source all game. Solve finds Comet Storm (the mana is red); Shred Memory finds Electrodominance. T6 Horizon Stone. T7 Comet Storm X = 8, copied: 16 to each opponent. **Kill T9 to 10.** |

Summary: Azula T3 twice, T4 three times; first copied combat T4 to 5; kills on T5 (loop), T7 and T8 (Godo + Helm, both
times with no loop piece in sight), T9-10 (copied burn), and one game with a threat on T8-9. Loops are the ceiling, copied
value and Godo the floor. A goldfish has no blockers and no removal: Godo's two kills are the least robust. Five games rank
nothing.

**Disrupted:**
- (a) Game 3, Azula killed in response to the Boots equip on T5: recast T6 for 6, first attack T7: two windows lost. In game
  4 the same removal is redirected by Deflecting Swat for free.
- (b) Game 2, a wipe in the turn cycle after T5 (I am tapped out for Gearhulk): it resolves; Azula and both Gearhulks die,
  Boots stays. T6 Godo, T7 Helm on Godo threatens the table again one turn later than planned. A wipe one turn later meets
  Mana Leak with two mana open.
- (c) Game 1, the T5 Turnabout countered: Redirect Lightning makes the counter fizzle. With no shield, the pieces come back
  through Gearhulk or Teachings' flashback, about two turns later.

**Reference boards.**
- Board 1, eight 1/1 chump blockers: they never stop the copies. Day of Black Sun at X = 0 kills every token for {B}{B} and
  none of mine. Thermo-Alchemist, copied Comet Storm and the loops ignore blockers. Aether Gale removes six tokens, or the
  maker and its engine. Godo's unlimited combats outlast them. Propaganda taxes the swarm: eight attackers cost 16.
- Board 2, two or more bigger creatures: attack another player; instant removal after blocks kills two (copied); Snap and
  Failed Fording bounce two; Aether Gale clears six before the attack; Imprisoned in the Moon and Amphibian Downpour last;
  Champion's Helm makes her 6/6; the noncombat routes do not care.

**Gauntlet.**
1. Fast combo: Swan Song, Spell Pierce, Negate, Mana Leak (creature combos too), the Reversal; eight instant creature
   answers; Shred Memory against the graveyard; Gearhulk recasts any of them; Narset's static.
2. Stax and taxes: cheap threats (Azula 4, Thermo 2); Abrade, Chaos Warp, Failed Fording, Aether Gale. Weak point: "sorcery
   speed only".
3. Go-wide: Board 1.
4. Big creatures: Board 2.
5. Control: Narset, spread threats (Azula, Ozai, Godo, Gearhulk at their end step, Black Market Connections), instant draw
   at end steps, the shield on the win turn.

## 6. The owner's cards (review of 2026-11-14)

| Card | Verdict | Reason |
|---|---|---|
| **Torrential Gearhulk** | **IN** (for Waterbending Lesson) | In the window it is two 5/6 bodies and four instants (R3). With Turnabout or Frantic Search in the graveyard it is free and makes mana. It is the deck's only recursion: a countered or used loop piece comes back. On an opponent's turn it is a counter or a kill on a blocker. Mystical Teachings finds it. The earlier cut ("6 mana") ignored that both the body and its instant are copied. Limit: X spells come back at X = 0. |
| **Frostcliff Siege** | **IN** (for Haunted Cloak) | Better haste than the Cloak: no equip cost (Azula on turn 4 attacks on turn 4 with four lands; the Cloak needs a fifth mana and another one after each recast) and it survives a creature wipe. Jeskai is a card each turn against the opponent who never blocks (his decisions file). Lost: the Cloak's vigilance; defense while tapped still has five pieces. |
| **Aether Gale** | **IN** (for Ritual of Soot) | The second mass answer. Ritual of Soot kills six of my own creatures (the three reducers, Thermo, Electro, Dualcaster), overlaps with Day of Black Sun against tokens and does nothing against big creatures. Aether Gale touches nothing of mine, takes any permanent type (stax pieces before a loop turn, blockers before Godo's combats), and kills tokens for good. Cost: 5 mana, sorcery, six targets needed. |
| **Imprisoned in the Moon** | **IN** (for Firebending Lesson) | A second lasting answer to a commander, beside Amphibian Downpour: kill spells and Chaos Warp only send it to the command zone. Also the only answer to a utility land and a third to planeswalkers. Firebending Lesson (2 damage) did not kill a 3/3. |
| **Mana Leak** | **IN** (for Undying Malice; the free second copy) | The only cheap counter in the pool that stops a creature spell: Spell Pierce, Swan Song and Negate all miss commanders and creature finishers. It is a hard counter whenever a player taps out, which is how his pod plays. Undying Malice answered only "destroy" and brought her back tapped; a counter stops the wipe itself. Late it is soft: guide note in section 2. |
| **Mystical Teachings** | **IN** (stays) | Copied in the window it finds both halves of a loop (goldfish game 1), or Gearhulk. The second copy stays in the binder for Ezio. |
| **Return the Favor** | **OUT for now: blocked by the bracket script, not by merit** | With Narset's Reversal in the list the script says FAIL: Spellbook variant 11-5940 (Reversal + Return the Favor, "infinite magecraft triggers") is stored with 5 mana, so the project rule reads it as an early two-card infinite. Its real line casts Return the Favor twice, the Reversal and another instant (9+ mana) and does nothing without a magecraft creature. The Reversal is the hub of three loops and stays. On merit it is IN: firebending pays its {R}{R}, it redirects removal or forks Comet Storm (four copies with Azula), and with Storm-Kiln Artist it is one more three-card loop. **Lead's decision** (section 7). Its jobs today: redirect: Deflecting Swat and Redirect Lightning; fork: Dualcaster Mage. |
| **Waterbending Lesson** | **OUT** | His question: yes, the waterbend is usually payable (13 artifacts, six of them equipment that tap for free), but that is not the problem. It is a 4-mana sorcery: Azula never copies it, and its mana leaves the window. Fact or Fiction, Thirst for Knowledge and Pull from Tomorrow draw at instant speed and are doubled; Gearhulk takes the slot. |
| Tome of Legends | OUT here, left for Ezio | It would be good here (a card a turn for {1}). The collection has one copy and he asked for it in Ezio; Azula claims Black Market Connections from Ezio instead, which does that job better here. If the lead returns that card to Ezio, the Tome takes its slot. |
| Commander's Sphere | OUT | A third 3-mana rock competes with Azula on turn 3. Of the 3-mana rocks, Bender's Waterskin does more here: mana on each opponent's turn for instants. |
| The Stasis Coffin | OUT (Toph's) | It protects the player for one turn; this deck's need is the commander. Propaganda covers the crack-back every turn. One copy, and it is his top Toph card. |
| Royal Assassin | OUT | A 1/1 that needs a turn and never helps the window; the instant removal does its job twice per card in her combat, and Propaganda is the deterrent. |
| Deadeye Navigator | OUT | Six mana and a second creature that must survive; it would blink Gearhulk or Dualcaster, but only after 12 mana in permanents. |
| Merciless Harlequin, Evie Frye, Jacob Frye, Lydia Frye, The Revelations of Ezio | OUT | Assassin cards: freerunning needs combat damage by an Assassin or the commander, the Fryes need each other, the saga returns Assassins. No Assassin in this deck. |
| Mortify, Utter End, Hardened Scales, Inscription of Abundance, Alibou | not in Azula's colors | |

## 7. Copies

**Claimed from another deck (1).**
| Card | Copies | Holder today | Reason | What that deck loses |
|---|---|---|---|---|
| Black Market Connections | 1 (EN, ACR 87; scanned in the Azula deck) | Ezio | Azula spends cards fastest and had two draw engines; this one needs no combat damage. Its Treasures are window mana and raise Storm-Kiln. It was in the Azula list he won with (round4-step27) and left only by build order. | Ezio loses a Treasure for its payment, a card and a changeling Assassin each turn. It keeps Coastal Piracy, Ezio Blade of Vengeance, Lion Vulture, Basim, Eagle Vision and nine rocks. Azula leaves it the two free cards he asked for there (Tome of Legends, Commander's Sphere) and does not touch Ezio's Mana Leak (Azula takes the free second copy). |

Fallback if the lead rules for Ezio: Tome of Legends (free) takes the slot here.

**Not claimed, on purpose:** Fellwar Stone, Rakdos Signet, Diabolic Tutor, Kolaghan's Command, Infernal Grasp (Ezio);
Strionic Resonator, Lithoform Engine (Kilo). Each gains about as much here as its deck loses. Venser, Shaper Savant (free):
considered as a sixth counter and left out (cut log).

**Cards whose copies run short** (one copy per deck that wants it today; no conflict opened by this list):
- with Kilo (Spanish copies): Swan Song (1), Negate (2), Thirst for Knowledge (2), Cascade Bluffs, Shivan Reef, Sulfur Falls,
  Everflowing Chalice, Chaos Warp, Command Tower, Exotic Orchard, Sol Ring, Arcane Signet;
- with Ezio: Propaganda (2), Swiftfoot Boots (2), Hidden Footblade (2), Terminate (2), Bender's Waterskin (3), Drowned
  Catacomb, Dragonskull Summit, Sunken Hollow, Smoldering Marsh, Sulfur Falls;
- with Toph: Redirect Lightning (2), Everflowing Chalice, Chaos Warp, Sol Ring.
- Single copies only Azula plays: every loop piece, Comet Storm, Electrodominance, Gearhulk, Frostcliff Siege, Imprisoned in
  the Moon, Aether Gale, Heartless Act, Horizon Stone.

**Freed for the later decks:** Haunted Cloak, Fatal Push (three free now), Firebending Lesson, Fists of Flame, Undying
Malice, Ritual of Soot, Waterbending Lesson (three free; Kilo keeps its own).

**Language, where it is not English** (no English copy owned or free): Torrential Gearhulk (CMM 128) and Aether Gale
(SOC 186), both new; and as today: Mind Stone, Nightscape Familiar, Narset's Reversal, Helm of the Host, Solve the Equation,
Thirst for Knowledge, Thrill of Possibility, Pull from Tomorrow, Swan Song, Negate, Shred Memory, Command Tower (PIP 259,
pinned), Exotic Orchard, Choked Estuary, Darkwater Catacombs, Sulfurous Springs. Everything else is English.

**For the lead.**
1. The Black Market Connections claim above.
2. Return the Favor: if variant 11-5940 is reclassified (real cost 9+ mana, needs a third card), it comes in for Hero's
   Downfall. Until then the bracket script fails with it by design, so I did not test that list. The plan file would tag it
   payoff and protection and add it to spell_density, spell_payoffs and the burn route. With Azula attacking, the script's
   own hazard list already knows its self-copy loop as floor 3.
3. Tokens: Black Market Connections moves here with its Shapeshifter token (he owns 1); it, Big Score and Storm-Kiln make
   more Treasures than the 2 he owns.

## 8. Changes against the deck as built today

**OUT (back to a binder).**
| Card | Reason |
|---|---|
| Waterbending Lesson (EN) | Sorcery, never copied; its mana leaves the window. |
| Haunted Cloak (EN) | Haste for 4 mana in all; Frostcliff Siege gives it with no equip cost. |
| Ritual of Soot (EN) | Kills six of my creatures, nothing above mana value 3; overlaps with Day of Black Sun. |
| Firebending Lesson (EN) | 2 damage misses most commanders. |
| Fatal Push (EN) | Mana value 2 or less without revolt, and revolt is rare here (Treasures only). |
| Undying Malice (EN) | Only against "destroy"; she returns tapped and out of combat. |
| Fists of Flame (EN) | A cantrip trick; the weakest draw slot. |
| 1 Mountain | Blue sources 18 to 19. |

**IN.**
| Card | From | Reason |
|---|---|---|
| Torrential Gearhulk (ES, CMM 128) | Spanish binder | Section 6. |
| Frostcliff Siege (EN, TDM 187) | English binder | Section 6. |
| Aether Gale (ES, SOC 186) | Spanish binder | Section 6. |
| Imprisoned in the Moon (EN, INR 69) | English binder | Section 6. |
| Mana Leak (EN, 8ED 89) | English binder (the free second copy) | Section 6. |
| Heartless Act (EN, TLA 103) | English binder | Two mana for almost any creature, where Fatal Push needed revolt. |
| Black Market Connections (EN, ACR 87) | **Ezio's deck** | A card and a Treasure every turn; section 7. |
| 1 Island | English binder | Blue for the new cards. |

**Cut log (considered and left out).**
| Card | Job | Count after | Why not |
|---|---|---|---|
| Return the Favor | redirect, fork | shield 8 | Bracket script FAIL with the Reversal (section 6). |
| Venser, Shaper Savant | flash bounce of a spell or permanent | counters 5 | Four mana; Failed Fording and five counters cover it. First in if a counter leaves. |
| Lightning Strike | burn | spot 15 | Paid by firebending, but 3 damage is the least needed answer. |
| Tome of Legends | constant draw | draw 12 | Left for Ezio (section 6). |
| Entomb, Reckless Handling, Loyal Inventor, Lo and Li | tutors | tutors 3 + Godo | Entomb only feeds Gearhulk or a 6-mana flashback; the others find artifacts or Lessons, no loop piece. |
| The Last Agni Kai | fight, keeps red mana | bankers 3 | Azula takes the damage, twice when copied. |
| Zuko, Exiled Prince; Azula, On the Hunt | second firebender | attackers 5 | Four-mana creatures that die in blocks; Ozai does the job with haste. |
| Opt, Consider, Ponder | cantrips | density 34 | Not draw; Expedite and Abandon Attachments net a card when copied. |
| Blasphemous Act, Inundate, Ritual of Soot | wipes | mass answers 2 | Kill or bounce my own engine, or cost 6. |
| Fellwar Stone, Commander's Sphere, Chromatic Lantern | rocks | ramp 10 + 1 | Ezio's, or 3-mana rocks. |
| Firebender Ascension, Unleash Fury, Fire Nation Attacks | EDHREC-listed Azula cards | | The Ascension needs four attack triggers and then copies only firebending; Unleash Fury wants combat damage; Fire Nation Attacks is 5 mana for four 2/2s. |

Proven role-players: Horizon Stone and Propaganda stay.

## 9. Real power (1-10: 4 precon, 6 upgraded, 7-8 high power, 9-10 cEDH)

| List | Estimate | Basis |
|---|---|---|
| Deck as built today | 7.5 to 7.9 | The final review of 2026-11-08. |
| **This list** | **7.6 to 8.1, most likely 7.8 to 7.9** | About +0.2. |

Confidence: medium-low: no games played, and the project's estimates have run high.

Where the gain comes from:
- Gearhulk: the best card of his own games, now doubled by Azula, and the first recursion for the loop pieces.
- Two more draw engines (Black Market Connections, Frostcliff Siege): the fair game stops running out of cards.
- Haste without an equip cost; a counter for creature spells; two lasting commander answers; a one-sided mass answer.

What it costs:
- Three 1-mana instants (Fatal Push, Firebending Lesson, Undying Malice); average mana value 2.48 to 2.60.
- 34 window cards against 35; the Cloak's vigilance.
- No answer left that kills many small NON-token creatures at once.
- Raw loop access is unchanged (same six pieces and three tutors): the gain is in the games without a loop and in getting
  a stopped loop back.

Commander Salt was not measured (not part of this step); expected near today's 7.3 to 7.7.

Self-review: one plan, 0 orphans; every gate function above its minimum without the commander; two noncombat routes and one
combat route with disjoint closers, each against three opponents; Bracket 3 rules pass with 1 of 3 Game Changers (no other
Game Changer is owned in these colors: live Scryfall list, 36 in Grixis identity, checked today); rules points R1 to R10
carry their status.
