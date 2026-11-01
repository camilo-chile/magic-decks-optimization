# Archetype profiles

One section per archetype. The machine-readable twin is `../archetypes.json` (schema 3: same slugs, same numbers). The
tables below are GENERATED from the JSON (between the `<!-- BEGIN table:slug -->` markers); edit the JSON, then regenerate,
never one without the other. Every count is cards in the 99. "min" is the floor below which the builder writes a reason;
"target" is the aim. [J] = builder judgment anchored on the odds tables in `probability.md`; [owner signal] = a lesson from
the owner's play kept as a general principle; everything else names its note and source in
`docs/research/commander-deckbuilding/notes/` (notes/13 = ratio gaps: K1 K2 K3 Karsten, CZ-new Command Zone 2025 template,
E1 EDHREC Bracket 3 average decks counted by function, PG Playgroup opening-hand data).

**How strong is the evidence?** No read source gives a complete, measured function profile for any archetype (notes/06
section 1; notes/07 bottom line; notes/10 gap 8). What exists: creature counts by archetype (notes/06 S1), land counts
by archetype from a simulation (notes/11 S14), type counts of single sample lists (notes/10), role lists without counts,
generic function floors, the Bracket 3 medians of a 1,285-deck survey (notes/11 S15), and, since revision 2, the EDHREC
Bracket 3 average decks counted by function for seven archetypes (notes/13 E1, table below). That table shows community
BEHAVIOUR, not quality: an average deck is the most-included card per slot across many lists, and the Tagger tags are broad.
Plan-function counts without a sample are still [J]: they apply the gate's odds classes (early 10, late 6) to the
archetype's sourced needs.

## How to use a profile
1. Match the commander's text to `recognize` cues. If two match, read the hybrid section at the end.
2. Copy the profile, then adjust each count to the commander (SKILL.md step 3): its fuel rate, its window, its dependence.
3. Commander as a piece: if the commander performs a function, it is a guaranteed piece (lower the count by what it
   supplies, never below what the plan needs when the commander is removed).
4. Safety floors (ramp, draw, removal, wipe, protection) follow the archetype; the gate warns at 10/8/8/2/3 and lands
   36 to 38. When the profile sits outside, write the reason. `removal` means SPOT answers only, wipes are counted apart,
   and `protection` here means COMMANDER protection (the class of the actual commander overrides the profile's default).
5. **Tiers.** A **gate** line is declared in the plan file `functions` with its needed_by; its min already meets the
   gate's class (10 early, 6 late). A **support** line (marked "support" below) is checked by the builder and reviewer
   against its own min, but is NOT declared alone in the plan file, because a short line would fail the gate: its cards
   go inside the gate function whose job they share (extra land drops inside `land_entries`, team evasion inside
   `through_wide_board`) or under their primary tag. Support mins assume repeatable permanents; a one-shot effect counts
   half [J]. If the plan cannot work at all without a support line, promote it to a gate function and reach the class
   minimum (SKILL.md step 3.1 gives the haste test).
6. **Payoff functions** have an alternative: when the commander itself is the payoff, the other payoffs are backups for
   when it is removed, so the function is judged late (6 pieces). Otherwise early (10). The same holds for a SOURCE
   function (token makers, counter sources, fodder) when the commander is a guaranteed source every turn it is out [J].
7. Every profile also carries the two gate functions `through_wide_board` and `through_big_creatures` (early, 10+).
8. Total protection = commander protection (base) + `wipe_insurance` (a support function of board-based plans). A card
   counts in both only if it does both jobs.

## Generic base (any archetype, sourced)
| Function | Range | Source |
|---|---|---|
| Lands | 36 to 38 (B3 median 36, IQR 34 to 37; CZ-new 38; EDHREC averages 34 to 36 outside landfall) | notes/11 S15; notes/13 CZ-new, E1 |
| Ramp | 10, or 12 with a 4+ MV commander (CZ-new); B3 median 13 counting rocks and rituals | notes/13 CZ-new; notes/11 S15 |
| Draw | 10; 12 card advantage (CZ-new, cards that net two or more); B3 median 10 | notes/03; notes/13 CZ-new; notes/11 S15 |
| Removal (spot) | spot 5 to 8; B3 spot median 5 (IQR 3 to 7); CZ-new targeted disruption 12 (counters, bounce, tappers, graveyard hate included) | notes/04 S4; notes/11 S15; notes/13 CZ-new |
| Wipes | 1 to 5 by source; B3 median 2; CZ-new mass disruption 6 (wipes plus tax, sweeper and graveyard effects) | notes/04 conflict 1; notes/11 S15; notes/13 CZ-new |
| Total answers | 8 to 10 removal inside 15 to 20 interaction; 8 to 12 including wipes | notes/04 S2 S4 |
| Protection | 5 to 7 (one source) | notes/04 S5 |
| Recursion | 2 to 3 for non-graveyard decks | notes/04 S5 |
| Tutors | B3 median 4 (2 to 7) | notes/11 S15 |
| Graveyard hate | 1+ | notes/09 S17 |
| Average MV | B3 median 3.11 (2.83 to 3.44) | notes/11 S15 |
| Creatures | 20 to 45 overall; typical 25 to 35 | notes/06 S1; notes/01 S3 |
| Plan cards | about 30; enablers 7 to 8 and enhancers 10 to 12 inside 30 to 45 plan cards | notes/13 CZ-new, CZ-old |

### EDHREC Bracket 3 average decks by archetype: community behaviour (notes/13 E1)
Medians over 7 to 8 well-known commanders per archetype, from `json.edhrec.com/pages/average-decks/<slug>/upgraded.json`,
counted 2026-10-31 with Oracle text and Scryfall Tagger tags. READ AS A RANGE ANCHOR, NEVER AS A TARGET: popular is not good,
Tagger tags are broad ("ramp" includes extra land drops and land tutors, "draw" includes cantrips, "protection" includes
equipment and blink) and regex counts miss wordings. Reanimator, blink, artifacts, enchantments, typal, control, pillowfort
and big mana were not sampled.

| Median count | Landfall | Spellsl. | Combat | Tokens | Voltron | Aristocr. | Counters |
|---|---|---|---|---|---|---|---|
| lands | 39.5 | 35 | 35.5 | 35 | 35 | 35.5 | 35 |
| average MV (nonland) | 3.22 | 2.52 | 3.16 | 3.05 | 2.48 | 2.77 | 2.79 |
| creatures | 25.5 | 13 | 30.5 | 26 | 17 | 32.5 | 29.5 |
| instants + sorceries | 20.5 | 36 | 16 | 19 | 13.5 | 16 | 15.5 |
| ramp (broad tag) | 28.5 | 13 | 13.5 | 17 | 10 | 17 | 20 |
| draw tag (incl. cantrips) / card advantage | 8 / 12 | 21 / 25 | 7 / 8.5 | 11 / 11 | 7 / 9 | 10 / 11 | 9.5 / 13 |
| removal (tag) | 5.5 | 11 | 10.5 | 10 | 8.5 | 14.5 | 6.5 |
| wipes / counterspells | 1 / 0.5 | 3 / 5 | 2.5 / 0 | 2 / 0 | 2 / 0 | 2 / 0 | 1 / 0 |
| protection (broad tag) | 2 | 1 | 10 | 4 | 15.5 | 1.5 | 4 |
| gives haste / hasty creatures | 1 / 0 | 1 / 1 | 4 / 2 | 1 / 1 | 2 / 0 | 0.5 / 0.5 | 1.5 / 0.5 |
| gives evasion / evasive creatures | 0 / 2.5 | 0 / 2 | 3 / 12 | 2 / 2 | 5.5 / 1 | 0.5 / 4 | 1.5 / 6 |
| extra land drops / land recursion / lands put onto the battlefield | 7 / 6 / 16 | 0 / 0 / 1 | 0 / 0 / 3 | 0 / 0 / 4 | 0 / 0 / 3 | 0 / 0 / 5.5 | 0 / 0 / 6 |
| landfall payoffs / spell-cast payoffs | 11.5 / 0 | 0 / 8 | 0 / 0 | 2 / 0 | 0 / 0 | 0.5 / 0 | 1 / 0 |
| token makers (regex, incl. Treasure) | 8.5 | 8 | 8 | 32 | 2 | 17 | 7 |
| sacrifice outlets (tag) / death payoffs | 6.5 / 1 | 0 / 0 | 1.5 / 0 | 2 / 0 | 0 / 0 | 18 / 7 | 0 / 0 |
| counter cards / doublers + proliferate | 3.5 / 1 | 0 / 0 | 4 / 0 | 5 / 3 | 0.5 / 0 | 4.5 / 1 | 20.5 / 11 |
| recursion (tag) | 8 | 2 | 1 | 0 | 3 | 5.5 | 2 |

Readings that moved the profiles: landfall runs far more extra land drops (7) and land recursion (6) than the old [J] counts
and puts 16 lands onto the battlefield by effects; spellslinger runs about 36 instants and sorceries and the most draw of
any archetype; combat decks run about 5 haste sources and a median of 12 evasive creatures but almost no team-wide evasion
(1.5 to 3) and no defense while tapped beyond about 4 vigilance creatures (attack taxes, fogs and goad are about 0 in every
archetype sampled): the team-evasion and defense-while-tapped lines of the combat profile come from the owner's losses, not
from community behaviour.

---

## landfall_lands: Landfall / lands matter
**Text cues.** "Whenever a land enters the battlefield under your control", landfall, "you may play an additional land",
"play lands from your graveyard", "for each land you control", lands that become creatures, "sacrifice a land".

**Fuel.** Land entries per turn. One natural land drop is the baseline; the plan wants two or more entries a turn from
about turn 4 [J, owner signal: landfall games needed a very large ramp count and repeated land entries; EDHREC landfall
averages agree on direction, notes/13 E1]. Count entries per turn, not only cards (SKILL.md step 3.2).

<!-- BEGIN table:landfall_lands -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 38 | 40 | | Simulated cast rates: landfall 38 to 40 (notes/11 S14; notes/02 S2). EDHREC Bracket 3 landfall average decks hold a median of 39.5 lands, range 38 to 46 over 8 commanders (notes/13 E1); Playgroup gives 38 to 42 for heavy ramp and landfall (notes/02 S1). Karsten's start of 42, less one per 2 to 3 extra rocks and per 3 to 4 cheap cantrips, lands near 40 at average MV 3.2 (notes/13 K1, K2). Lean 40 when the deck sacrifices or recurs lands; extra land drops need lands in hand. |
| Ramp | base | 18 | 20 | | [J, owner signal] A landfall plan needs far more ramp than another plan, so this profile sits at or above the TOP of the Bracket 3 interquartile range (median 13, IQR 10 to 18, notes/11 S15). EDHREC Bracket 3 landfall average decks tag a median of 28.5 cards as ramp (22 to 37; a broad tag that includes land tutors and extra drops, notes/13 E1). The 2019 note says landfall decks run fewer rocks and more land ramp, and no source gives a landfall total (notes/09 conflict 2). Prefer ramp that puts LANDS onto the battlefield: each is also a landfall trigger. Extra land drops have their own function. |
| Draw (nets cards) | base | 10 | 12 | | CZ-new card advantage 12 (cards that net two or more, notes/13 CZ-new); EDHREC landfall averages: card advantage 12, draw tag 8 (5 to 11) (notes/13 E1). Landfall payoffs that draw count here. Draw also finds the lands that extra drops need. |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only (wipes are separate). B3 spot-removal median 5, IQR 3 to 7 (notes/11 S15); EDHREC landfall averages 5.5 (notes/13 E1); spot 5 to 8 (notes/04 S4). The deck is not combat-centred, so removal is a supporting role (notes/04 S3). |
| Wipes | base | 1 | 2 | | B3 median 2 (notes/11 S15); EDHREC landfall averages 1 (notes/13 E1). A board of lands survives creature wipes, so a wipe costs the deck less than it costs a creature deck; still prefer one-sided wipes (notes/04 S1). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Fuel comes from the 99, so the default is enabler; protect the engine permanents (landfall enchantments, creatures) as much as the commander. |
| `land_entries` | gate | 12 | 16 | early | The fuel function: every card that makes a land enter beyond the natural drop (land ramp onto the battlefield, extra land drops, fetch lands, land recursion, lands-onto-battlefield creatures). EDHREC Bracket 3 landfall averages put a median of 16 lands onto the battlefield by effects (11 to 20, notes/13 E1). Overlaps ramp on purpose (notes/07 S1; notes/11 S14). Budget entries per turn, not only cards (SKILL.md step 3.2): repeatable permanents give an entry every turn, one-shots give one. |
| `landfall_payoffs` | gate | 10 | 12 | early | Ramp without payoffs makes a slow deck (notes/07 S9 snippet, notes/10 N3). EDHREC landfall averages run a median of 11.5 payoffs (5 to 21, notes/13 E1). The big payoffs compete for one role, so do not stack many expensive ones (notes/10 S1). When the commander is the payoff, the others are backups (late 6). If the commander is the payoff: late, 6 to 8. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |
| `extra_land_drops` | support | 5 | 7 | early | REPEATABLE engines: permanents that let you play extra lands or put a land onto the battlefield every turn. The per-turn rate cannot exceed one land a turn without them (notes/07 S1). EDHREC landfall averages run a median of 7 (3 to 10, notes/13 E1). They need lands in hand: keep the land count at the top of the band. A one-shot effect counts half. Cards go inside land_entries. Cards go inside `land_entries`. |
| `land_recursion` | support | 3 | 5 | late | Lets lands enter again and again: sacrifice-and-return effects, graveyard land play, fetch lands that come back. EDHREC landfall averages run a median of 6 (2 to 11, notes/13 E1); the mechanism is also in notes/10 N3 N4 snippets. Cards go inside land_entries. Cards go inside `land_entries`. |
| `mana_sinks` | support | 3 | 4 | late | [J] Surplus mana must have a use: ramp past about five mana is no longer ramp (notes/07 S1); ramp that later turns into cards keeps its value (notes/07 S2). |
| `wipe_insurance` | support | 2 | 3 | late | [J] The payoff creatures and enchantments are the exposed part of the board; team protection, recursion or rebuild engines (notes/04 S1 layers). |

**Curve** 3.0 to 3.5 (average MV of nonland cards). **Creatures** 22 to 30. Landfall preset at MV 3.0 (notes/11 S14); battlecruiser 3.5+ needs 38 to 40 lands (notes/02 S2); EDHREC landfall averages: MV 3.22, 25.5 creatures (notes/13 E1).
<!-- END table:landfall_lands -->

**Wins** by landfall tokens or damage, team pump over tokens, drain or damage per land entry (notes/10 S1 payoff list).
**Failure modes**: ramp with no payoffs; extra drops with no lands in hand; flood with no sink; payoffs competing for the
same role (notes/10 S1); payoffs whose value comes on their own entry, not on landfall (notes/10 S1); land-recursion
engines exposed to graveyard hate.
**What to look for in the commander's text**: does it reward the ENTRY (landfall) or the COUNT of lands? Entry rewards
want extra drops, fetches and recursion; count rewards want land ramp and protection of the land base. Does anything
change what a permanent IS (lands that become creatures, artifacts or creatures that count as lands, a token that copies a
land)? Then read the rulings for abilities it gains or keeps (mana abilities, summoning sickness) and for how those
permanents die or return; a returning land is a land entry.

## spellslinger: Instants and sorceries
**Text cues.** "Whenever you cast an instant or sorcery", magecraft, copy a spell, "noncreature spell", prowess, flash,
cost reduction for spells.

**Fuel.** Instants and sorceries in hand when the commander's window is open. Each cast spends a card: the hand empties
fastest of any archetype ([owner signal]; consistent with notes/03 S2: draw-built commanders need more draw, and the
extension to commanders that SPEND cards is [J]).

<!-- BEGIN table:spellslinger -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 34 | 36 | | EDHREC Bracket 3 spellslinger average decks hold a median of 35 lands (34 to 36) at average MV 2.52 (notes/13 E1); the sample list runs 34 (notes/10 S7). Karsten's formula (60-card tournament decks scaled to 99, not Commander data) gives about 34 at MV 2.5 with 20 cheap draw or ramp pieces (notes/13 K2). This low band holds only under the lean-low rule (average MV under 2.8 AND 10+ cheap pieces); otherwise 36 to 38 [J]. |
| Ramp | base | 10 | 12 | | CZ-new 10, or 12 with a 4+ commander (notes/13 CZ-new); EDHREC spellslinger averages tag 13 (7 to 17, notes/13 E1). Treasure-making spells are the stated mana answer (notes/07 S4). Rituals give same-turn mana only (notes/10 S7 trap) and do not count. |
| Draw (nets cards) | base | 12 | 18 | | A commander built around DRAWING cards needs 15 to 20 (notes/03 S2); extending that to a commander that SPENDS cards is builder judgment [J]. CZ-new card advantage 12 (notes/13 CZ-new). EDHREC spellslinger averages: draw tag 21 (15 to 27, cantrips included) and card advantage tag 25 (20 to 29) against a Bracket 3 all-deck median of 10 (notes/13 E1). Count only draw that nets cards; cantrips replace themselves and go in spell_density (notes/03 S2). |
| Removal (spot answers) | base | 8 | 10 | | Spot answers incl. counterspells (wipes separate). EDHREC spellslinger averages tag 11 removal and 5 counterspells (notes/13 E1); instant-speed removal is also fuel for the commander's window. |
| Wipes | base | 2 | 3 | | Few own creatures, so wipes cost less (notes/04 S1: non-creature decks run more); EDHREC spellslinger averages 3 (notes/13 E1). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Counterspells double as protection (notes/04 S5) and may be counted here when they can answer the removal aimed at the commander; the endgame needs protection and disruption (notes/07 S4). |
| `spell_density` | gate | 30 | 36 | early | Critical mass of instants and sorceries. EDHREC Bracket 3 spellslinger averages run a median of 36 (31 to 43, notes/13 E1); the EDHREC guide's sample list 38 (notes/10 S7); a Draftsim list 40 (snippet). Creatures 25 or fewer (notes/06 S1). If the commander rewards only spells cast in a window (for example while it attacks, or on opponents' turns), count only cards castable in that window (instants, flash). |
| `spell_payoffs` | gate | 10 | 12 | early | Engine plus payoffs or copy effects are the archetype's needs (notes/07 S4). EDHREC averages hold a median of 8 cast-payoffs by regex, which undercounts (3 to 15, notes/13 E1). Read each payoff's text for which spell types it counts (notes/10 S7). When the commander is the payoff, the others are backups (late 6). If the commander is the payoff: late, 6 to 8. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |
| `cost_reducers` | support | 2 | 4 | early | Cost reducers for instants and sorceries make the commander's window cheaper. EDHREC spellslinger averages run a median of 3 (1 to 8, notes/13 E1). Count a reducer as ramp only if it applies to most of the deck's spells; check the window (a reducer that works only on your main phase does nothing in a combat window). Cards go inside `ramp`. |

**Curve** 2.5 to 3.0 (average MV of nonland cards). **Creatures** 10 to 25. Cheap spells and instants rise with power (notes/09 S20 averages); EDHREC spellslinger averages: MV 2.52, 13 creatures (10 to 17), 36 instants and sorceries (notes/13 E1). [J] for the band.
<!-- END table:spellslinger -->

**Wins** by burn or drain copied or repeated against each opponent, token armies made by spells, X spells; include
non-combat damage because boards stall (notes/10 S7).
**Failure modes**: no win condition (notes/07 S4); commander as the only win condition (notes/07 S7, unverified);
running out of cards; payoffs counting spell types the deck lacks; ritual mana wasted; casting restrictions (sorcery speed,
one spell a turn) shut a cast-trigger commander [J].
**What to look for**: WHEN does it reward the action (any time, my turn only, one step such as combat or an end step,
opponents' turns)? Do copies count (a copy is not cast, a token is not cast: not for "whenever you cast" triggers)? Does it
make mana that lasts only a step or a phase (combat-only, end-step-only, made on opponents' turns)? If the window is combat,
apply the combat_attackers profile as a hybrid.

## go_wide_tokens: Go-wide tokens
**Text cues.** "Create ... tokens", "for each creature you control", anthems, populate, token doublers.

**Fuel.** Bodies on the battlefield.

<!-- BEGIN table:go_wide_tokens -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | Token sample list 35 (notes/10 S10); EDHREC Bracket 3 token averages hold a median of 35 (35 to 36) at MV 3.05 (notes/13 E1); B3 median 36 (notes/11 S15); CZ-new 38. Karsten's formula (60-card decks scaled to 99, not Commander data) gives about 38 at MV 3.05 with 8 cheap pieces (notes/13 K2). Go to 35 only under the lean-low rule (meta.lean_low_land_rule). |
| Ramp | base | 10 | 12 | | CZ-new 10 (notes/13 CZ-new); aggressive decks need less (notes/09 S17), but the Bracket 3 median counts 13 (notes/11 S15). Token averages tag 17 as ramp, a broad tag that includes Treasure (notes/13 E1). |
| Draw (nets cards) | base | 10 | 12 | | Base 10 (notes/03); refills after a wipe; aggressive decks need cheap refills (notes/09 S17). |
| Removal (spot answers) | base | 5 | 7 | | Spot answers only. Aggressive decks run 5 to 7 (notes/09 S17); B3 spot median 5 (notes/11 S15); used selectively (notes/04 S2). |
| Wipes | base | 0 | 1 | | Wraths hurt tokens even when you cast them; only one-sided or synergy wipes (notes/04 S1, notes/06 S5). EDHREC token averages run 2 (notes/13 E1) but they are mostly one-sided. |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). The board-wide worry is wipes: count it in wipe_insurance, not here. |
| `token_makers` | gate | 15 | 20 | early | Snippets disagree: 10 to 15 producers (notes/10 N1) against about a third of the list (N2); both unverified. EDHREC Bracket 3 token averages hold a median of 32 by a broad regex that includes Treasure (13 to 35, notes/13 E1). Repeatable makers count more than one-shots. Unsupported 1/1s backfire (notes/06 S1). If the commander is the source: late, 6 to 8. |
| `token_payoffs` | gate | 6 | 8 | late | Anthems, overrun effects, damage per token, drain. EDHREC token averages: anthem tag median 6 (1 to 14), team pump 4 (0 to 6) (notes/13 E1). The N1 snippet's 2 to 3 payoffs is below the gate's late floor of 6. Board-dependent payoffs are weak early (anthem useful at about 5 creatures, lethal at 10, notes/10 S10). |
| `through_wide_board` | gate | 10 | 12 | early | Ways past eight or more small chump blockers: team evasion, flyers, unblockables, trample on a big attacker, 'creatures can't block' effects, one-sided wipes, scaling pingers, non-combat damage or drain. Menace and power-restricted evasion fail here (notes/12 C10; notes/06 S3); a single 1-damage ping counts half (role-players-and-upgrades.md 5). Support lines (evasion, team_evasion) put their cards inside this function. |
| `through_big_creatures` | gate | 10 | 12 | early | Ways past two or more creatures bigger than yours: removal on the few key blockers, deathtouch, flying, forced blocks, pump plus trample, power-restricted evasion (notes/12 C1 C4; notes/06 S3). |
| `doublers` | support | 0 | 2 | late | Strong but dead without tokens in play (notes/10 S10; notes/12 C14). Snippet 1 to 2 (notes/10 N1). |
| `wipe_insurance` | support | 3 | 4 | late | [J] Wipes are the main danger: indestructible, phasing, or rebuild engines (notes/04 S1 protection table; notes/12 C3: two plans, indestructible or recursion and tokens). |
| `sac_outlets` | support | 0 | 2 | late | Free outlets turn wipes and edicts into value (notes/12 C1). |

**Curve** 2.7 to 3.2 (average MV of nonland cards). **Creatures** 25 to 35. Low curve to deploy wide; EDHREC token averages MV 3.05 (2.58 to 3.59), 26 creatures (notes/13 E1); B3 median 3.11 (notes/11 S15). [J] for the band.
<!-- END table:go_wide_tokens -->

**Wins** by overrun or team pump (several players in one combat, notes/05 S4), damage per token entering, sacrifice drain,
monarch drain (notes/10 S10).
**Failure modes**: wipes; attack caps and taxes (notes/05 S5); payoffs drawn before the board; opponents at full life
(notes/05 S3); unsupported 1/1s (notes/06 S1).

## voltron: Equipment or auras on one creature
**Text cues.** "Equipped creature", "enchanted creature", equip, "for each Aura and Equipment attached", double strike,
hexproof on the commander.

**Fuel.** One protected, evasive, big threat that connects every turn.

<!-- BEGIN table:voltron -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 35 | 37 | | One aura list runs 34 (notes/06 S11, an outlier against 36 to 40); EDHREC Bracket 3 voltron averages hold a median of 35 (34 to 36) at MV 2.48 with 10 ramp (notes/13 E1); Karsten's formula (60-card decks scaled to 99, not Commander data) gives about 36 with 12 cheap pieces (notes/13 K2). Below 36 only under the lean-low rule (10+ rocks, MV under 2.8). |
| Ramp | base | 10 | 12 | | 8 to 12 mana rocks to cast the commander on turn 3 (notes/11 S16, opinion; Rate My Decks 8 to 12, notes/13 W1). Karsten: rocks pay off with a 4+ MV commander (notes/13 K1). EDHREC voltron averages tag 10 (3 to 15, notes/13 E1). |
| Draw (nets cards) | base | 8 | 10 | | Below the default 10 on purpose: the one aura list has 11 draw (notes/06 S11); EDHREC voltron averages run draw 7 and card advantage 9 (notes/13 E1); combat-damage draw counts (notes/03 S2 combat-tied category). |
| Removal (spot answers) | base | 5 | 7 | | Spot answers only. Aggressive decks run 5 to 7 (notes/09 S17); Rate My Decks 8 to 10 counts removal loosely (notes/13 W1, opinion). |
| Wipes | base | 1 | 2 | | Few own creatures; a wipe plus an indestructible commander clears the way (notes/06 S9); EDHREC voltron averages 2 (notes/13 E1). |
| Commander protection | base | 6 | 8 | | Commander protection for a default 'attack_engine' commander (meta.commander_dependence): 6 to 8; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). The commander IS the plan: protection ranked first (notes/06 S9); Rate My Decks asks 8 to 10 protection spells (notes/13 W1, opinion); EDHREC voltron averages tag 15.5 (10 to 20, includes equipment, notes/13 E1). Cast the commander only when protection is ready and reserve tutors for protection (notes/11 S16). Stack two layers: one against targeted removal, one against destroy or damage (notes/06 S9 inference). |
| `equipment_auras` | gate | 12 | 16 | early | Rate My Decks asks at least 15 to 20 equipment and auras (notes/13 W1, opinion); search snippets give 12 to 18 (unverified); the one aura list runs about 20 auras (notes/06 S11). Equipment is the safer multiplayer choice because it stays when the creature dies (notes/11 S16). Spread auras over two carriers (notes/06 S11). |
| `through_wide_board` | gate | 10 | 12 | early | Ways past eight or more small chump blockers: team evasion, flyers, unblockables, trample on a big attacker, 'creatures can't block' effects, one-sided wipes, scaling pingers, non-combat damage or drain. Menace and power-restricted evasion fail here (notes/12 C10; notes/06 S3); a single 1-damage ping counts half (role-players-and-upgrades.md 5). Support lines (evasion, team_evasion) put their cards inside this function. |
| `through_big_creatures` | gate | 10 | 12 | early | Ways past two or more creatures bigger than yours: removal on the few key blockers, deathtouch, flying, forced blocks, pump plus trample, power-restricted evasion (notes/12 C1 C4; notes/06 S3). |
| `evasion` | support | 6 | 8 | early | A 1/1 token can absorb a 25-power hit (notes/10 S12); trample, flying or unblockable on the carrier. EDHREC voltron averages tag a median of 5.5 evasion granters (2 to 12, notes/13 E1); snippets say 6 to 8. Evasion is one of three pillars (notes/11 S16). Its cards also count in through_wide_board and through_big_creatures. Cards go inside `through_wide_board`. |
| `haste` | support | 2 | 3 | early | Opponents remove the commander before it can attack (notes/06 S4). EDHREC voltron averages tag a median of 2 haste granters (1 to 4, notes/13 E1). Haste equipment also carries hexproof or shroud (notes/06 S15). Promote to a gate function with the haste test (SKILL.md step 3.1). |
| `recursion` | support | 1 | 2 | late | Return spent auras or equipment (notes/06 S11). |
| `wipe_insurance` | support | 1 | 2 | late | [J] The board is one creature plus its gear; the commander's own protection is counted in base.protection. Equipment that stays and recursion for spent auras are the insurance. |

**Curve** 2.3 to 3.0 (average MV of nonland cards). **Creatures** 15 to 30. One voltron list's spells average 1.56 (notes/06 S9); EDHREC voltron averages MV 2.48, 17 creatures (notes/13 E1); cheap pump is central. [J] for the band.
<!-- END table:voltron -->

**Wins** by commander damage (21 from one commander, rules fact not re-checked in the notes), one player at a time: add
extra combats, double strike, or finishers that hit several players (notes/11 S16), plus one non-combat route for the gate.
**Failure modes**: the threat removed before combat (notes/10 S12); chump blockers (notes/10 S12); auras lost in a 2-for-1;
archenemy status; one kill per turn against three opponents (notes/11 S16).

## combat_attackers: Attack-trigger and evasive attackers
**Text cues.** "Whenever ~ attacks", "deals combat damage to a player", "attacking creatures you control", menace,
"can't be blocked", extra combat, raid. Also any commander that acts only while attacking.

**Fuel.** Attackers that survive and connect every turn, from the turn they arrive.

<!-- BEGIN table:combat_attackers -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | B3 median 36 (notes/11 S15); EDHREC Bracket 3 combat averages hold a median of 35.5 (34 to 37) at MV 3.16 (notes/13 E1); CZ-new 38; Karsten's formula (60-card decks scaled to 99, not Commander data) gives about 38 with 10 cheap pieces (notes/13 K2). Aggro aims for a low curve and about 10 ramp (notes/12 C3, opinion): lean to 36 only under the lean-low rule. |
| Ramp | base | 10 | 12 | | Aggro near 10, ramp ahead of early draw (notes/12 C3, opinion); CZ-new 10, or 12 with a 4+ commander (notes/13 CZ-new). EDHREC combat averages tag 13.5 (8 to 21, notes/13 E1). |
| Draw (nets cards) | base | 10 | 12 | | Default 10 (notes/03); combat-damage draw counts at full weight when the deck connects reliably, at half weight otherwise (notes/03 S2 conditional draw). EDHREC combat averages run less (draw 7, card advantage 8.5, notes/13 E1): that is community behaviour, not quality, and an attacker that spends its hand needs the refill. |
| Removal (spot answers) | base | 5 | 7 | | Spot answers only. Aggressive decks 5 to 7 (notes/09 S17); removal is support and clears blockers selectively (notes/04 S2 S3). More answers than closing pieces is a red flag (SKILL.md step 15). |
| Wipes | base | 0 | 1 | | Symmetric wipes hit your own attackers (notes/04 S1, notes/06 S2). Only one-sided wipes. EDHREC combat averages 2.5 (notes/13 E1). |
| Commander protection | base | 6 | 8 | | Commander protection for a default 'attack_engine' commander (meta.commander_dependence): 6 to 8; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Attackers and commander must live: 5 to 7 protection (notes/04 S5); EDHREC combat averages tag 10, a broad tag (notes/13 E1). A commander that is only an enabler uses the enabler class. |
| `attackers` | gate | 12 | 16 | early | The fuel function: creatures that want to attack and can connect (evasive, hasty or big enough). Aggro runs 30+ creatures (notes/06 S1); EDHREC combat averages hold a median of 12 evasive creatures (7 to 26, notes/13 E1). Count only creatures the plan actually attacks with. |
| `through_wide_board` | gate | 10 | 12 | early | Ways past eight or more small chump blockers: team evasion, flyers, unblockables, trample on a big attacker, 'creatures can't block' effects, one-sided wipes, scaling pingers, non-combat damage or drain. Menace and power-restricted evasion fail here (notes/12 C10; notes/06 S3); a single 1-damage ping counts half (role-players-and-upgrades.md 5). Support lines (evasion, team_evasion) put their cards inside this function. |
| `through_big_creatures` | gate | 10 | 12 | early | Ways past two or more creatures bigger than yours: removal on the few key blockers, deathtouch, flying, forced blocks, pump plus trample, power-restricted evasion (notes/12 C1 C4; notes/06 S3). |
| `haste` | support | 4 | 6 | early | Opponents remove an attacker before it can attack (notes/06 S4). EDHREC combat averages tag a median of 4 haste granters (0 to 8) plus 2 hasty creatures, about 5 in all (notes/13 E1); one sourced deck runs six (notes/06 S4). Team haste for a wide board, single-target haste with protection for one or two key attackers (notes/12 U1 snippet). If the commander must attack, at least one haste source should reach it after a recast. Promote to a gate function (early, 10) with the haste test in SKILL.md step 3.1. |
| `team_evasion` | support | 6 | 8 | early | [J, owner signal] Effects that cover the whole attack scale with its size: creatures can't block, type-wide or team-wide flying, fear, unblockable (notes/06 S3). Menace and 'can't be blocked by power 3 or more' do NOT count against a wide board of small blockers (notes/12 C10; notes/06 S3). Community average decks run far fewer (regex 1.5, evasion granters 3, notes/13 E1): the line comes from the owner's losses, not from behaviour. Floor 4 when the pool lacks 6, with through_wide_board carried by flyers, trample and non-combat damage. Cards go inside `through_wide_board`. |
| `defense_while_tapped` | support | 4 | 6 | early | [J] No source counts it as a whole (notes/05 gap, notes/12 gap). Sourced tools: vigilance (attacking does not tap; notes/12 C1; EDHREC combat averages run a median of 4 vigilance creatures (1 to 5), notes/13 E1), attack taxes (push attacks to other players; payers still attack; notes/05 S5, notes/12 C2), deathtouch and reach or flying blockers (notes/12 C1 C2), punishment effects (notes/05 S5), instant-speed responses held (notes/12 C5). Taxes, fogs and goad are about 0 in every community average sampled (notes/13 E1). |
| `combat_draw` | support | 4 | 6 | early | [J] Draw tied to combat damage is the plan's own card flow (notes/03 S2 category); a cheap plan-tied draw spell often beats a generic one in this archetype. |
| `wipe_insurance` | support | 2 | 3 | late | [J] A wide attacking board is a wipe target: team protection, recursion, or creatures that return (notes/12 C1 C3 two plans against wipes). |

**Curve** 2.6 to 3.2 (average MV of nonland cards). **Creatures** 28 to 35. Low-ramp aggro needs average 2.8 or lower (notes/12 C3, opinion); EDHREC combat averages MV 3.16, 30.5 creatures (notes/13 E1). Skipping two-drops leaves dead turns (notes/12 C3).
<!-- END table:combat_attackers -->

**Wins** by team-wide damage: overrun, extra combats, team double strike, damage on attack to each opponent. A
one-player-per-trigger kill is a backup (notes/05 S3; notes/12 section 4).
**Failure modes**: menace and power-restricted evasion fail against wide chump boards (notes/12 C10); fragile creatures;
no haste; wide open after attacking; one kill per turn against three opponents; going wide into a sweeper (notes/12 C1);
becoming the main target (notes/12 C6); too much removal and too few threats.
**What to look for**: does the commander need to SURVIVE combat (a trigger on combat damage, a payoff on attack, a mana
ability that works only in combat)? Then it
needs evasion past both reference boards, protection while attacking, haste after a recast, and something that keeps you
alive after the attack. Toughness of the commander and the key attackers: 2 or less dies to pingers and blocks [J].

## plus_one_counters: +1/+1 counters
**Text cues.** "+1/+1 counter", proliferate, "with a +1/+1 counter on it", counter doubling.

<!-- BEGIN table:plus_one_counters -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | Counters guide list 34 (notes/10 S6); EDHREC Bracket 3 counters averages hold a median of 35 (34 to 37) at MV 2.79 (notes/13 E1); B3 median 36 (notes/11 S15). Below 36 only under the lean-low rule (meta.lean_low_land_rule). |
| Ramp | base | 10 | 12 | | CZ-new 10 (notes/13 CZ-new); the upgrade guide cut ramp on a counters list that had too much (notes/09 S17). Counters averages tag 20, a broad tag (notes/13 E1). |
| Draw (nets cards) | base | 10 | 12 | | Base 10; counter payoffs that draw count (notes/10 S6). |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only. The upgrade guide expanded a counters list's 5 removal (notes/09 S17); EDHREC counters averages 6.5 (notes/13 E1). |
| Wipes | base | 1 | 2 | | Prefer wipes that spare countered creatures (notes/07 S5: expected one-sided more than half the time); EDHREC counters averages 1 (notes/13 E1). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). A runaway counter board draws table attention (notes/07 S5); the counter sources must stay in play (notes/07 S5). |
| `counter_sources` | gate | 12 | 18 | early | One counter source making too few counters is a named trap (notes/10 S6). EDHREC counters averages hold a median of 20.5 cards that place +1/+1 counters (3 to 46, notes/13 E1). Repeatable sources count more than one-shots. If the commander is the source: late, 6 to 8. |
| `counter_payoffs` | gate | 6 | 8 | late | [J] Payoff roles: draw, mana, damage, evasion, finishers by proliferate (notes/10 S6). Cards that multiply the trigger resource when the deck's main action happens are payoffs AND fuel. |
| `through_wide_board` | gate | 10 | 12 | early | Ways past eight or more small chump blockers: team evasion, flyers, unblockables, trample on a big attacker, 'creatures can't block' effects, one-sided wipes, scaling pingers, non-combat damage or drain. Menace and power-restricted evasion fail here (notes/12 C10; notes/06 S3); a single 1-damage ping counts half (role-players-and-upgrades.md 5). Support lines (evasion, team_evasion) put their cards inside this function. |
| `through_big_creatures` | gate | 10 | 12 | early | Ways past two or more creatures bigger than yours: removal on the few key blockers, deathtouch, flying, forced blocks, pump plus trample, power-restricted evasion (notes/12 C1 C4; notes/06 S3). |
| `counter_doublers` | support | 4 | 7 | early | Doublers and proliferate multiply every source (notes/07 S5; notes/10 S6); doublers are called essential in green (notes/07 S5). EDHREC counters averages hold a median of 11 (0 to 25, notes/13 E1). |
| `evasion` | support | 4 | 6 | early | Blockers alone can stall a counters board (notes/07 S5); EDHREC counters averages run 6 evasive creatures (2 to 13, notes/13 E1). [J] for the line. Cards go inside `through_wide_board`. |
| `wipe_insurance` | support | 2 | 3 | late | [J] A runaway board is the wipe target; wipes that spare countered creatures, indestructible effects, or counters that survive a bounce. |

**Curve** 2.7 to 3.1 (average MV of nonland cards). **Creatures** 28 to 34. EDHREC counters averages MV 2.79 (2.47 to 3.69), 29.5 creatures (notes/13 E1); B3 median 3.11 (notes/11 S15). [J] for the band.
<!-- END table:plus_one_counters -->

**Failure modes**: blockers stall; a single counter engine; trigger order on the payoff; table attention; black is the
weakest counters color (notes/10 S6).
**Counters on attack**: no source names it as a mechanic (notes/10 S6); a heavily countered evasive attacker wins in few
attacks (notes/10 S6). General rule [J]: a card that multiplies the commander's trigger resource when the deck's main action
happens (counters when a creature attacks, tokens when a spell is cast, drain when a creature dies) is a payoff AND fuel for
the plan; judge it with the main action as its condition (SKILL.md step 3.4).

## aristocrats_sacrifice: Aristocrats / sacrifice
**Text cues.** "Sacrifice a creature:", "whenever a creature you control dies", "whenever another creature dies", drain
per death.

<!-- BEGIN table:aristocrats_sacrifice -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | Aristocrats sample list 35 (notes/10 S11); EDHREC Bracket 3 aristocrats averages hold a median of 35.5 (34 to 36) at MV 2.77 (notes/13 E1); B3 median 36 (notes/11 S15). Below 36 only under the lean-low rule (meta.lean_low_land_rule). |
| Ramp | base | 10 | 12 | | CZ-new 10 (notes/13 CZ-new); EDHREC aristocrats averages tag 17, a broad tag (notes/13 E1). |
| Draw (nets cards) | base | 10 | 12 | | Base 10; outlets and payoffs that draw count (notes/10 S11). |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only; edicts that hit each player fit (notes/04 S2). EDHREC aristocrats averages tag 14.5, a broad tag (notes/13 E1). |
| Wipes | base | 2 | 3 | | Own creatures dying is value here, so symmetric wipes cost less [J]; B3 median 2 (notes/11 S15); EDHREC aristocrats averages 2 (notes/13 E1). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). The plan is spread over many cheap pieces. |
| `sac_outlets` | gate | 10 | 14 | early | Outlets are the most crucial piece: 7 to 12 slots (notes/07 S6 summary, unverified) or 6 to 8 free outlets (notes/07 S14, notes/10 N6, low authority). EDHREC aristocrats averages hold a median of 18 cards tagged as sacrifice outlets (14 to 25), a broad tag that includes costed outlets (notes/13 E1). Gate early class; the commander counts if it is an outlet. Free outlets are far stronger than costed ones (notes/10 S11). Keep a spare outlet before a kill attempt (notes/07 S6). |
| `fodder` | gate | 14 | 18 | early | Missing any of the three legs hurts (notes/10 S11). Token makers and creatures with death or enter value count. EDHREC aristocrats averages: token makers 17 (4 to 24), creatures 32.5 (notes/13 E1). If the commander is the source: late, 6 to 8. |
| `death_payoffs` | gate | 10 | 12 | early | Without payoffs the deck takes long solo turns that do nothing (notes/10 S11). EDHREC aristocrats averages hold a median of 7 by regex, which undercounts (2 to 13, notes/13 E1). Many fodder creatures are also payoffs (multi-role). When the commander is the payoff, the others are backups (late 6). If the commander is the payoff: late, 6 to 8. |
| `recursion` | gate | 6 | 8 | late | The loop is offer, return, offer again (notes/10 S11); generic recursion is 2 to 3, graveyard strategies run more (notes/04 S5). EDHREC aristocrats averages hold a median of 5.5 (2 to 13, notes/13 E1). Gate late class. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |

**Curve** 2.6 to 3.1 (average MV of nonland cards). **Creatures** 28 to 35. Cheap bodies; EDHREC aristocrats averages MV 2.77, 32.5 creatures (notes/13 E1); B3 median 3.11 (notes/11 S15). [J] for the band.
<!-- END table:aristocrats_sacrifice -->

**Wins** by drain per death across all opponents (hits all three at once), damage per sacrifice, late loops.
**Failure modes**: a missing leg; costed outlets; no spare outlet; table stops cooperating (notes/10 S11); graveyard hate on
the loop; low creature power.

## reanimator_graveyard: Reanimator / graveyard
**Text cues.** "Return target creature card from a graveyard to the battlefield", mill, discard, "from your graveyard",
"cast ... from your graveyard".

<!-- BEGIN table:reanimator_graveyard -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | Reanimator guide list 36 (notes/10 S8); 38 to 40 claimed for Commander generally (notes/07 S3, no source); B3 median 36 (notes/11 S15). Reanimator was not sampled in the EDHREC averages (notes/13 E1). |
| Ramp | base | 8 | 10 | | Below the default on purpose [J]: revival cheats mana, but hard-casting targets late is the backup (notes/10 S8). CZ-new 10 (notes/13 CZ-new). |
| Draw (nets cards) | base | 10 | 12 | | Base 10; looting-style draw also fills the graveyard (notes/10 S8). |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only (notes/04 S2 S4). |
| Wipes | base | 2 | 3 | | Base; a wipe also stocks your graveyard [J]. |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Graveyard-dependent commanders need protection (notes/10 S8, no specifics). |
| `graveyard_fillers` | gate | 10 | 12 | early | [J] Enablers usually cost 3 or less, almost never above 5 (notes/07 S3); self-mill, discard, looting, surveil, cards that put a chosen creature into the graveyard (notes/10 S8). Gate early class. No count sourced. |
| `reanimation` | gate | 10 | 12 | early | Run several revival spells, not one or two (notes/07 S3); keep a spare (notes/10 S8). Gate early class; tutors that find a revival spell count. [J] |
| `reanimation_targets` | gate | 8 | 12 | late | 8 to 12 expensive creatures, usually 5 to 7 MV (notes/07 S3). Judged late because fillers that put a chosen creature into the graveyard give access to a target; above the gate's late class. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |
| `nongraveyard_threats` | support | 3 | 5 | late | [J] Keep threats that work without the graveyard so exile does not end the plan (notes/07 S3). |

**Curve** 3.0 to 3.6 (average MV of nonland cards). **Creatures** 25 to 40. Targets are 5 to 7 MV but are not meant to be cast; enablers are cheap (notes/07 S3). [J] for the band.
<!-- END table:reanimator_graveyard -->

**Failure modes**: graveyard hate (notes/07 S3; notes/10 S8); big targets drawn with no enabler (fix: looting, dual-role
cards, late hard-casts, notes/10 S8); too few revival spells; table focus; slow play punished (notes/07 S3).
**Small graveyard packages inside other decks**: two or three reanimation cards in a deck that is not built to fill its
graveyard are a mini-package, not a plan (notes/07 S3 several revival spells; notes/11 S3 layering). Count them as
recursion (base 2 to 3) and do not add targets for them.

## blink_etb: Blink / enter-the-battlefield
**Text cues.** "Exile ... then return it to the battlefield", "whenever another creature enters", ETB doublers.

<!-- BEGIN table:blink_etb -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | Blink sample list 36 (notes/10 S9, 2021); B3 median 36 (notes/11 S15). Not sampled in the EDHREC averages (notes/13 E1). |
| Ramp | base | 10 | 12 | | Enter-effect ramp creatures count (notes/10 S9); CZ-new 10 (notes/13 CZ-new). |
| Draw (nets cards) | base | 10 | 12 | | Enter-effect draw creatures count (notes/10 S9). |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only; enter-effect removal counts; creature removal crowds out noncreature answers (notes/10 S9). |
| Wipes | base | 1 | 2 | | Creature-based deck: fewer creature-killing effects (notes/04 S5). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Blink in response to removal is protection [J]. |
| `etb_creatures` | gate | 15 | 20 | early | [J] A lopsided mix of targets and blink effects suffers (notes/10 S9). Sample list has 40 creatures (notes/10 S9). |
| `blink_effects` | gate | 10 | 12 | early | [J] Gate early class. No source says whether repeatable or one-shot blink counts more; newer builders overload one-shot flicker and a lopsided mix of targets and blink effects underperforms (notes/07 S15 unverified; notes/10 S9). Judge by what each effect repeats. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |
| `wipe_insurance` | support | 2 | 3 | late | [J] A creature board is the wipe target; blink in response and recursion rebuild it. |

**Curve** 2.8 to 3.3 (average MV of nonland cards). **Creatures** 30 to 40. B3 median 3.11 (notes/11 S15); the sample list holds 40 creatures (notes/10 S9). [J] for the band.
<!-- END table:blink_etb -->

**Failure modes**: ETB hosers; imbalance; target removed in response; creature removal crowding out noncreature answers
(notes/10 S9).

## artifacts: Artifacts matter (weakly supported)
No artifact composition source was read (notes/07 gap). Only sample type counts: a ramp-theme average with 20 artifacts
(notes/09 S20), a typal average deck with 14 (notes/10 S3).

<!-- BEGIN table:artifacts -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 35 | 37 | | [J] No artifact composition source was read (notes/07 gap). Mana rocks are ramp in most definitions (notes/02 S4; notes/07 S2), so an artifact deck with 12+ rocks can sit at the low end under the lean-low rule; otherwise 36 to 38. |
| Ramp | base | 10 | 12 | | Rocks are also artifact fuel; rocks that later become cards keep their value (notes/07 S2); CZ-new 10 (notes/13 CZ-new). |
| Draw (nets cards) | base | 10 | 12 | | Base 10 (notes/03). |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only (notes/04 S2 S4). |
| Wipes | base | 2 | 2 | | Base (notes/11 S15). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Artifact wipes are the archetype's hazard (inference); see wipe_insurance. |
| `artifact_density` | gate | 20 | 25 | early | [J] Only sample type counts exist: a ramp-theme average runs 20 artifacts (notes/09 S20), a typal average deck 14 (notes/10 S3). Weakly supported. |
| `artifact_payoffs` | gate | 10 | 12 | early | [J] No source. Gate early class; late 6 when the commander is the payoff. If the commander is the payoff: late, 6 to 8. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |
| `wipe_insurance` | support | 2 | 3 | late | [J] Artifact wipes and artifact hate are the archetype's hazard: protection that covers artifacts, recursion for them, or payoffs that are not artifacts. |

**Curve** 2.6 to 3.1 (average MV of nonland cards). **Creatures** 15 to 28. [J] No source.
<!-- END table:artifacts -->

**Failure modes**: artifact wipes and hate [J]; rocks with nothing to cast late (notes/07 S2); type count without payoffs.
**Rules check**: when the commander or a key card changes WHAT a permanent is (adds or removes a card type, turns a creature
into a land, makes a token a copy), check the rulings for what that changes: which abilities it gains or keeps (mana
abilities, summoning sickness), which "whenever X enters" triggers fire, what counts as the type for costs and counts;
article claims are not enough.

## enchantments: Enchantments matter (weakly supported)
No enchantress source read. Aura voltron list 27 enchantments (notes/06 S11), pillowfort list 18 (notes/12 C15).

<!-- BEGIN table:enchantments -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | [J] No enchantress source was read. Aura voltron list 34 (notes/06 S11); pillowfort lists 36 and 39 (notes/10 S4, notes/12 C15). |
| Ramp | base | 10 | 12 | | CZ-new 10 (notes/13 CZ-new). |
| Draw (nets cards) | base | 10 | 12 | | Enchantress draw counts (notes/10 S13 role list). |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only (notes/04 S2 S4). |
| Wipes | base | 2 | 3 | | Base; few creatures (notes/04 S1). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Enchantment wipes break the board (notes/10 S13); see wipe_insurance. |
| `enchantment_density` | gate | 18 | 25 | early | [J] Aura voltron list 27 enchantments (notes/06 S11), pillowfort list 18 (notes/12 C15). Weakly supported. |
| `enchantment_payoffs` | gate | 10 | 12 | early | [J] No source. Gate early class; late 6 when the commander is the payoff. If the commander is the payoff: late, 6 to 8. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |
| `wipe_insurance` | support | 2 | 3 | late | [J] Enchantment wipes break the board (notes/10 S13): recursion for enchantments, protection that covers them, payoffs that are not enchantments. |

**Curve** 2.6 to 3.2 (average MV of nonland cards). **Creatures** 10 to 25. [J] No source.
<!-- END table:enchantments -->

## typal: Typal (tribal)
**Text cues.** "Other [type]s you control get", "[type] spells you cast", "choose a creature type".

<!-- BEGIN table:typal -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | One typal average deck runs 33 (notes/10 S3); eight non-landfall samples average 34.9 (notes/10); B3 median 36 (notes/11 S15); CZ-new 38. Typal was not sampled in the EDHREC averages (notes/13 E1). Below 36 only under the lean-low rule (meta.lean_low_land_rule). |
| Ramp | base | 10 | 12 | | CZ-new 10 (notes/13 CZ-new). |
| Draw (nets cards) | base | 10 | 12 | | Typal draw counts. The one typal sample ran only 3 draw (notes/06 S12), which is below every base. |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only. 'Too much theme, too few answers' is a named mistake; reserve interaction slots (notes/06 S10). |
| Wipes | base | 1 | 2 | | One that spares your own type; lopsided wipes singled out a typal board in testing (notes/06 S12). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Wide typal boards are wipe targets (notes/06 S5): count that in wipe_insurance. |
| `type_members` | gate | 25 | 30 | early | 30 or more creatures for typal; lords need a dense board (notes/06 S1). When typal is only a SECONDARY modifier (a cost reducer or a one-line bonus, not a body count), use the if_secondary_modifier numbers: members are enough when about a third of the deck's spells carry the type, and 16 pieces give 84 % to hold one by turn 3 (probability.md A) [J]. As a secondary modifier: 16 to 20 (support). |
| `lords_payoffs` | gate | 10 | 12 | early | One typal list runs 11 anthems (notes/06 S12). Gate early class; late 6 when the commander is the lord or payoff [J]. A type-wide effect that gives the whole attack evasion or protection (type-wide flying, 'can't be blocked', 'creatures can't block', type-wide hexproof) is a role-player: one card covers every attacker (notes/06 S3). If the commander is the payoff: late, 6 to 8. |
| `through_wide_board` | gate | 10 | 12 | early | Ways past eight or more small chump blockers: team evasion, flyers, unblockables, trample on a big attacker, 'creatures can't block' effects, one-sided wipes, scaling pingers, non-combat damage or drain. Menace and power-restricted evasion fail here (notes/12 C10; notes/06 S3); a single 1-damage ping counts half (role-players-and-upgrades.md 5). Support lines (evasion, team_evasion) put their cards inside this function. |
| `through_big_creatures` | gate | 10 | 12 | early | Ways past two or more creatures bigger than yours: removal on the few key blockers, deathtouch, flying, forced blocks, pump plus trample, power-restricted evasion (notes/12 C1 C4; notes/06 S3). |
| `theme_share` | support | 32 | 45 | early | Cards on theme out of about 63 non-land cards: about 75 % (45 to 47) as the aim, a floor near half (32), plus reserved interaction slots (notes/06 S10, a 2017 opinion; treat as historical). Also a ceiling: more theme than this starves interaction. Unit: cards on theme out of about 63 non-land cards; ceiling 47. |
| `wipe_insurance` | support | 3 | 4 | late | [J] A dense typal board is a wipe target: team protection, indestructible, recursion (notes/06 S5). |

**Curve** 2.6 to 3.1 (average MV of nonland cards). **Creatures** 28 to 36. B3 median 3.11 (notes/11 S15). [J] for the band.
<!-- END table:typal -->

If the type wins by attacking, add the combat_attackers profile as a hybrid (haste, team evasion, defense while tapped).
A type-wide effect that gives the whole attack evasion or protection (type-wide flying, "can't be blocked", "creatures can't
block", type-wide hexproof) is a role-player: it covers every attacker with one card (notes/06 S3 team effects). When typal
is only a secondary modifier (a cost reducer or a one-line bonus), size `type_members` with the secondary-modifier numbers
(16 to 20, support) instead of 25 to 30 [J].
**Failure modes**: too much theme (notes/06 S10); self-hosing wraths (notes/06 S2 S12); members that are weak cards alone;
fragile members.

## control_stax_lite: Control / light stax (Bracket 3 legal)
<!-- BEGIN table:control_stax_lite -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | B3 median 36 (notes/11 S15); long games need land drops [J]. |
| Ramp | base | 10 | 12 | | CZ-new 10 (notes/13 CZ-new). |
| Draw (nets cards) | base | 12 | 15 | | Control leans on card advantage (notes/03 SN7, snippet); CZ-new card advantage 12 (notes/13 CZ-new); 12+ (notes/09 S17). |
| Removal (spot answers) | base | 12 | 15 | | Spot answers INCLUDING counterspells (the counterspells line counts inside): a long-game deck runs 15 or more (notes/09 S17); CZ-new targeted disruption 12 (notes/13 CZ-new). |
| Wipes | base | 3 | 5 | | Control decks run more wipes; 3 to 5 is the figure for most decks (notes/04 S1), so control sits at its upper end [J]. CZ-new mass disruption 6 (notes/13 CZ-new). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Counterspells double as protection (notes/04 S5). |
| `finishers` | gate | 6 | 8 | late | Each deck needs a named finisher; value alone seldom ends games (notes/03 S5; notes/11 S17). Gate late class; tutors that can fetch a finisher count as pieces. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |
| `counterspells` | support | 4 | 6 | early | B3 median 1 counterspell (IQR 0 to 3) for the average deck (notes/11 S15); EDHREC spellslinger averages 5 (2 to 12, notes/13 E1) is the nearest sample; control runs more. A few counters stop wipes aimed at you (notes/05 S5). Cards also count in base.removal. Cards go inside `removal`. |

**Curve** 2.8 to 3.3 (average MV of nonland cards). **Creatures** 8 to 20. B3 median 3.11 (notes/11 S15). [J] for the band.
<!-- END table:control_stax_lite -->

**Bracket 3 limits**: no mass land denial; extra turns low and never chained. Global locks draw battle lines (notes/11 S8);
sweeper-heavy decks make pods concede (notes/06 S14).

## pillowfort_goad: Pillow fort / goad (politics)
<!-- BEGIN table:pillowfort_goad -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 39 | | Pillowfort lists run 36 (notes/10 S4) and 39 (notes/12 C15). |
| Ramp | base | 10 | 12 | | CZ-new 10 (notes/13 CZ-new). |
| Draw (nets cards) | base | 10 | 12 | | Base 10 (notes/03); slow plan. |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only (notes/04 S2 S4). |
| Wipes | base | 2 | 3 | | Base; go-wide aggro is the archetype's weak spot (notes/10 S13). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). Enchantment wipes break the fort (notes/10 S13); see wipe_insurance. |
| `attack_deterrents` | gate | 10 | 12 | early | [J] Taxes, punishers, fogs, goad and deterrent blockers (notes/10 S13; notes/12 C1 C2 C15). Taxes stop only opponents who cannot pay (notes/05 S5); punishment is preferred by one source (notes/05 S5). No community average sampled runs any: taxes and fogs are about 0 in every archetype sampled (notes/13 E1, no pillowfort sample). |
| `finishers` | gate | 6 | 8 | late | Name a finisher route (notes/10 S13); the last opponent still has to be beaten (notes/05 S5). Gate late class; tutors that can fetch a finisher count. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |
| `wipe_insurance` | support | 2 | 3 | late | [J] Enchantment wipes and go-wide aggro are the weak spots (notes/10 S13). |

**Curve** 2.8 to 3.4 (average MV of nonland cards). **Creatures** 10 to 20. [J] No source.
<!-- END table:pillowfort_goad -->

**Failure modes**: go-wide aggro and opponents who can pay taxes; enchantment wipes; haste beats goad; the last opponent
(notes/05 S5; notes/10 S13). Attack taxes in an attacking deck are a defense-while-tapped tool, not a plan (see
win-routes.md).

## big_mana_ramp: Big mana / battlecruiser
<!-- BEGIN table:big_mana_ramp -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 38 | 40 | | Battlecruiser (MV 3.5+, 8 ramp) 38 to 40 (notes/11 S14, notes/02 S2); high average MV 40 to 44 (notes/02 S1); Karsten starts at 42 + Sol Ring and keeps 38 to 39 with 7 to 9 rocks for a 4 to 6 MV commander (notes/13 K1). |
| Ramp | base | 12 | 15 | | Big-mana commanders up to 15, 20 seen (notes/09 S17); CZ-new 12 for a 4+ commander (notes/13 CZ-new); Karsten: 7 to 9 rocks plus Sol Ring for a 4 to 6 MV commander (notes/13 K1); 14 ramp gives 80 % to have one by turn 3, 20 gives 90 % (notes/03 S1). |
| Draw (nets cards) | base | 10 | 12 | | Base 10 (notes/03). |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only (notes/04 S2 S4). |
| Wipes | base | 2 | 3 | | Base (notes/11 S15). |
| Commander protection | base | 3 | 4 | | Commander protection for a default 'enabler' commander (meta.commander_dependence): 3 to 4; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). |
| `big_threats` | gate | 8 | 10 | late | [J] Six or seven cards at 7+ MV leave many stuck in hand (notes/08 S14); Karsten's model keeps 4 to 10 six-drops by commander MV (notes/13 K1). Count threats, not ramp. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |

**Curve** 3.5 to 4.0 (average MV of nonland cards). **Creatures** 20 to 30. Battlecruiser preset MV 3.5 (notes/02 S2).
<!-- END table:big_mana_ramp -->


## alternate_kill: Alternate kill / conditional elimination
**Text cues.** "Target player loses the game", "each opponent with N life or less loses", "if that player has N or less
life", "you win the game", a threshold of permanents or counters, an elimination that needs a payment in a window.

**Fuel.** Progress toward the condition for EVERY opponent (life lost, counters, devotion, a board threshold) and the
resources to pay for the kill when it opens (mana, colors, a window).

<!-- BEGIN table:alternate_kill -->
| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 38 | | [J] No source; follows the commander's cost and the mana the kill needs. Lean to the top of the band when the kill costs a lot of mana in a window; the odds of paying it are in probability.md E and E2. |
| Ramp | base | 10 | 12 | | CZ-new 10 (notes/13 CZ-new); add mana for the kill's payment, not only the commander's cast. |
| Draw (nets cards) | base | 10 | 12 | | Base 10 (notes/03). |
| Removal (spot answers) | base | 6 | 8 | | Spot answers only; they also keep the table off the commander's window (notes/04 S2 S4). |
| Wipes | base | 1 | 2 | | Base [J]; a board is not the plan, so a one-sided wipe is cheap. |
| Commander protection | base | 5 | 7 | | Commander protection for a default 'engine' commander (meta.commander_dependence): 5 to 7; the class of the actual commander overrides this. Wipe insurance is counted apart (functions.wipe_insurance). The commander IS the kill: it is the visible threat and each removal on it delays the plan by a recast and its tax. |
| `condition_enablers` | gate | 10 | 12 | early | [J] Cards that move EVERY opponent toward the condition (damage, life loss, counters, devotion or a board threshold). A team-wide effect counts full; a single-target effect counts half, because the kill must be repeated per opponent. The commander's own trigger is a guaranteed piece. If the commander is the source: late, 6 to 8. |
| `team_finishers` | gate | 6 | 8 | late | [J] Cards that finish or damage every opponent at once. The commander's own kill is usually one player per resolution and is therefore a backup route (notes/05 S3 inference; notes/12 section 4), so the main route must reach the table: drain to each opponent, overrun, a spell that hits all. |
| `through_wide_board` | gate | 10 | 12 | early | How the closing route beats eight or more small chump blockers: non-combat damage or drain to each opponent, flyers or unblockables, one-sided wipes, 'creatures can't block' effects. Closers that ignore blockers count (notes/12 C14). |
| `through_big_creatures` | gate | 10 | 12 | early | How the closing route beats two or more creatures bigger than yours: removal on the key blockers, deathtouch, flying, forced blocks, finishers that ignore blockers (notes/12 C1 C4 C14). |
| `payment_enablers` | support | 6 | 8 | early | [J] The mana, colors, cost reduction and window access the kill needs when it is open: untapped sources in the window, instant-speed fixing, ways to keep or convert mana across steps. Check the joint-color odds (probability.md E2) and what else the mana is wanted for that turn. Window COSTS are treated in mana-and-ramp.md section 6. Cards go inside `condition_enablers`. |

**Curve** 2.5 to 3.2 (average MV of nonland cards). **Creatures** 20 to 32. [J] No source.
<!-- END table:alternate_kill -->

**Wins** by the commander's own elimination plus a team-wide finisher: the commander's kill is one player per resolution
(a backup route by the win-route rules), so the profile adds `condition_enablers` that push EVERY opponent under the
threshold at once and `team_finishers` that reach the whole table. The gate's second route must be disjoint from it.
**Failure modes**: the condition met for one opponent only; the payment not available when the kill opens; the commander
removed or answered before the kill resolves; opponents change the threshold (life gain); the window competes with other
uses of the same mana.
**What to look for**: is the condition about each opponent (life, counters) or about you (devotion, board size)? What does
the payment cost and in which step must it be made (mana-and-ramp.md section 6, window costs)? Which colors does it need at
once (probability.md E2)? Can a response remove the commander before the kill resolves (protection class: engine)?

## Group hug
Not supported by the read sources (one ramp card is called a group-hug pick, notes/07 S1). Build from the generic base and
mark every count [J], or use pillowfort_goad for politics plans.

---

## Hybrids
Rule (same as `archetypes.json` `meta.hybrid`):
1. Combine only when the commander rewards both, or one archetype is the fuel of the other.
2. One primary, one secondary. Land band: the primary's, or the overlap.
3. Shared functions: the higher min and target, never the sum. Protection takes the class of the actual commander.
4. Secondary-only functions keep their min, but at least half of their pieces must also serve a primary function [J].
5. A secondary that is only a MODIFIER (a cost reducer, a one-line bonus, a clause that rewards a card type) is sized as a
   support line with the profile's `if_secondary_modifier` numbers when it has them (typal members 16 to 20) [J].
6. Fit check: the mins, counting each card once, must fit in the non-land slots (SKILL.md step 3.5). If not, shrink the
   secondary to the pieces that serve the primary, and drop every card that exists only for a secondary function that no
   longer reaches its min.
7. Conflicting ranges (creature count, average MV, spell density counted only on instants and flash): take the stricter one
   and write why.
8. Routes: at least one from the primary; the secondary may provide the non-combat route.

Valid pairs: tokens + sacrifice; landfall + counters; spellslinger + combat attackers; reanimator + sacrifice; alternate
kill + combat attackers (the kill triggers on combat damage); typal + combat attackers (the type wins by attacking).

**Window-limited payoff + attackers, worked pattern [J].** A commander whose payoff or mana exists only inside one window
needs the profile that owns the window plus the payoff's profile. Three unrelated cases: (1) spell payoffs that trigger only
while attacking: spellslinger + combat, with spell density counted only on cards castable in combat (instants, flash); (2)
mana that exists only during your end step: spellslinger or artifacts + control, counting only end-step or flash plays; (3)
a payoff on opponents' turns: spellslinger counting only instants and flash, plus protection at instant speed. In every
case: the highest draw of the two profiles, haste after a recast if the commander must attack, evasion and protection so it
survives the window, defense while tapped if it attacks every turn, and a list of what can be cast with the window mana plus
cards that keep or convert the leftover (mana-and-ramp.md section 6).

**Landfall + counters, worked pattern [J].** Land entries place counters; doublers multiply each trigger. Ramp and extra
land drops follow landfall (the higher counts); counter doublers follow counters (4 to 7); the deck rarely needs haste;
evasion is needed only if the counters are meant to attack.

**Alternate kill + combat attackers [J].** The kill triggers on combat damage: the attacker profile supplies haste, evasion
and protection; `condition_enablers` must reach every opponent so the kill is not one player per resolution; the payment (mana,
colors, a window) is a COST to budget (mana-and-ramp.md section 6, probability.md E2).

## A commander that fits no profile
Build the profile from scratch with SKILL.md step 3: name the fuel, set the fuel functions by the odds classes (early 10,
late 6, plan-critical 12 to 15), take the generic base for safety functions, and mark every count [J].
