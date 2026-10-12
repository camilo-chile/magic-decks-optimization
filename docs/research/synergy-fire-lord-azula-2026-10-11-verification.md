Model ID: claude-opus-5-5

# Verification: synergy research for Fire Lord Azula (Phase 3, report dated 2026-10-11)

Verifier role: independent second researcher, trying to find what is wrong or missing.
Date: 2026-10-12. Report under review: `docs/research/synergy-fire-lord-azula-2026-10-11.md`.

Sources:
- `data/cache/pool_fire-lord-azula.jsonl`: 18,563 rows, 0 color-identity violations, 36 `game_changer: true`.
  Multi-face text is in `card_faces`; 424 rows have a null top-level `oracle_text`.
- `data/cache/spellbook_fire-lord-azula.json`: 94 variants.
- The Scryfall oracle bulk file in `data/cache/`, read for legality only.
- `docs/power-scale.md` v0.5 and `docs/research/commander-brackets-rules-snapshot.md` (rules as of
  2026-02-09, beta).
- Network spot checks, never evidence:
  - `backend.commanderspellbook.com`: 13 GET calls, read through WebFetch summaries.
  - `api.scryfall.com`: returned **HTTP 403** to WebFetch on both endpoints tried, so no rulings were
    read.

`data/raw/` and EDHREC were not used. Helper scripts are in the session scratchpad (`verify/`) and
were run with `python -I`. Scryfall's `edhrec_rank` field in the pool was used only to sort the
omission scan, never as evidence.

## Check summary
| # | Check | Verdict | Key evidence |
|---|---|---|---|
| 1 | Name integrity | PASS | 197 table rows; 12 role headers sum to 197 and each matches its row count. 0 duplicates, 0 names missing from the pool, 0 identity violations, and the GC column matches 197/197. Every budget-alternative target is in the list. The prose names, matched against all pool names, are all in the pool; the only non-pool name is Time Walk. "Teferi, Mage of Zhalfir" is split across a line break but resolves |
| 2 | Oracle accuracy | FAIL (1 should-fix, 5 minor) | 197 claims compared with pool oracle text, including `card_faces` for the 15 multi-face rows. Prismari Command "copy picks again" is wrong. Imprecise: Mox Amber, Thrill of Possibility, Brainstorm, Mystic Confluence, Fire Nation Palace |
| 3 | Commander interaction | PASS at oracle level; rulings UNVERIFIED | My re-derivation agrees: the copy is mandatory, applies to any spell you cast while she is attacking, and firebending RR lasts until end of combat. The Archmage Emeritus, Storm-Kiln Artist, Professor Onyx, Veyran, Twinning Staff, Shaun and Kediss claims match both cards' oracle text. Missing nuances are listed under M4 and S6 |
| 4 | Extra turns | PASS (faithful to the docs; owner decision pending) | The report quotes the power-scale policy literally. Doc inconsistencies are listed under M10 |
| 5 | Game Changers | PASS | The 36 pool GCs equal the 36 named in report §4. The 6 GC candidates (Rhystic Study, The One Ring, Fierce Guardianship, Force of Will, Cyclonic Rift, Orcish Bowmasters) are correct. "Pick up to 3" fits Bracket 3 (max 3; Azula is not a GC) |
| 6 | Bracket hazards | FAIL | Two candidate pairs are Spellbook 2-card infinites and are not flagged (S1). Other candidates' 2-card partners are missing from "safe halves" (S2). One candidate-only loop is unchecked (S3). The MLD and stax lists are incomplete (M7). No card is wrongly excluded |
| 7 | Combos (Spellbook file) | PASS | My recount reproduces every number (table below). The API returns exactly 94 variants for the same query (offset 93 exists, offset 94 is empty), so none are missing. No variant is classified "fine" |
| 8 | Completeness | FAIL (should-fix) | High-value omissions, led by Roaming Throne, Helm of the Host and Strionic Resonator (S7). The Stickers claim is verified (48, all `legal` in the bulk file) |
| 9 | Tiers | FAIL (should-fix) | The `core` set contradicts §7's "low" build (S5). The Lightning Greaves shroud anti-synergy is not noted (S6). Several budget pairs are not like-for-like (M6) |

Combo recount from the Spellbook file (all 94 include Azula):

| Group | R | S | E | B | Total |
|---|---|---|---|---|---|
| Azula + 2 cards | 0 | 7 | 21 | 0 | 28 |
| Azula + 3 cards | 60 | 0 | 1 | 5 | 66 |
| Buildable in pool | 48 | 7 | 16 | 0 | 71 |

The 23 unbuildable variants:
- 5 need Time Walk (all tag B).
- 18 need off-identity cards: 6 E variants (Eternal Witness, Greenwarden of Murasa, Warden of the
  Eye, Timeless Witness, Returned Pastcaller, Skullwinder) and 12 R variants with Whirlwing
  Stormbrood. One Time Walk variant also needs Whirlwing; it is counted once, under Time Walk.

Other counts that reproduce:
- 65 variants produce "Infinite turns" plus "Lock": 48 buildable + 12 Whirlwing + 5 Time Walk.
- Buildable 2-card variants: 22 (15 E + 7 S).
- Infinite-turn group: 4 flash pieces x 12 extra-turn sorceries = 48.
- The report's `manaValueNeeded` ranges per group match the file (5-9, 0, 3, 1).
- No buildable variant needs a template (`requires` is empty in all 94).

## Findings: blocking
None. Nothing found invalidates the report's main conclusions:
- Archetype A is the right primary.
- Bracket 4 patterns are excluded.
- The Game Changers handling is right.
- The Spellbook counts are right.

## Findings: should fix
**S1 (high). Two candidate pairs are Spellbook 2-card infinite combos, and the report does not name
them.**
- Report text: §3 lists `Sol Ring | core`, `Mox Amber | situational`, and `Hullbreaker Horror |
  situational | Flash; token copy doubles bounces (check loops in Phase 2)`. Neither §5's
  commander-free list nor §6's "safe halves" names the pairing.
- Spellbook API spot check (not evidence):
  - `513-3682`, Hullbreaker Horror + Mox Amber: tag S, `manaValueNeeded` 0, infinite colored mana,
    ETB and storm. Notable prerequisite: "You control a legendary creature that has a color that
    matches the mana symbol in the other permanent's mana cost." Azula is a legendary creature in
    all three colors.
  - `513-5034--46`, Hullbreaker Horror + Sol Ring: tag E, infinite colorless mana and storm. The id
    suffix suggests a template slot.
- Under Layer A a 2-card combo with speed >= 3 floors at 4. Phase 2 would catch this, but the hazard
  section should not present these as safe.
- Fix: add both pairs to §5 and the safe-halves list, or drop Hullbreaker Horror (or Mox Amber, a
  weak card anyway).

**S2. "Safe halves" misses other candidates that have Spellbook 2-card partners.** API spot checks,
to be confirmed by Phase 2 `find-my-combos`:

| Candidate | Spellbook partner(s), variant id, tag | Partner status |
|---|---|---|
| Twinning Staff | Narset's Reversal (`11-2539`, E); Dramatic Reversal (`2539-4821`, E) | Report names Dramatic Reversal only with Isochron Scepter |
| Birgi, God of Storytelling // Harnfel, Horn of Bounty | Grinning Ignus (`392-411`, E) | In pool, not cited |
| Veyran, Voice of Duality | Chain of Smog (`326-4280`, S) | Not cited |
| Storm-Kiln Artist | Chain of Smog (`326-5195`, R); Haze of Rage (`3940-5195`, S); Seething Song + Reiterate (`3368-4036-5195`, E) | Seething Song is a candidate |

**S3. One loop among candidates only is not in the Spellbook file.** This is my derivation from
oracle text, not verified by Spellbook. The pieces are Azula attacking, Storm-Kiln Artist (`core`),
Archaeomancer (or Mnemonic Wall, its listed budget alternative) and Sublime Epiphany. The loop:
- Cast Epiphany with the mode "create a token that's a copy of target creature you control". The
  cast triggers Storm-Kiln once.
- Azula's copy triggers Storm-Kiln again ("cast or copy"). The copy re-targets Storm-Kiln Artist, so
  each loop adds one more Storm-Kiln.
- The original makes an Archaeomancer token. Its ETB trigger goes on the stack after Epiphany is in
  the graveyard, so it can return Epiphany.
- Treasures per loop are 2, 4, 6, 8 and so on, against a cost of 6 (less with Baral, Goblin
  Electromancer or Archmage of Runes, all candidates). About 12 mana starts it, and then it gives
  unbounded mana, magecraft and storm.
- It is not a 2-card combo, so it is not barred by Wizards' wording. It is still a "chain" that the
  bracket-fit review should see.
- Fix: name it in §8 item 4 alongside the general warning.

**S4. Prismari Command misstatement.**
- Report: "2 modes (damage, loot, Treasure, artifact); copy picks again".
- A copy keeps the modes chosen for the original and may change only targets. That is CR 707.10
  (background; Scryfall was not reachable), and it is the report's own §1 statement: "a copy keeps X
  and modes".
- Fix: "copy repeats the same two modes, new targets allowed".

**S5. The `core` tier contradicts the §7 speed table.**
- §7's "Primary A ... low" build excludes "the speed packages: ... Veyran / Twinning Staff / Shaun
  copy multipliers + X burn (Comet Storm, Electrodominance)".
- But Veyran, Voice of Duality and Comet Storm are both `core`.
- Either move them out of `core`, or state that the core list implies the "medium" speed build.

**S6. Lightning Greaves (`core`) and Whispersilk Cloak give Azula shroud, which blocks the deck's
own targeting.**
- Oracle: Greaves gives "shroud (It can't be the target of spells or abilities.)".
- These candidates all target the creature and so cannot be used on Azula while she has shroud:
  - Fire Nation Palace: "{1}{R}, {T}: Target creature you control gains firebending 4".
  - Rogue's Passage, Shizo, Death's Storehouse and Kaya's Ghostform.
  - Mithril Coat's ETB attach.
  - Equip activations of the other equipment.
  - Dive Down, Slip Out the Back, Undying Malice, Fake Your Own Death and Malakir Rebirth.
- Equip {0} lets Greaves move off at sorcery speed only.
- Fix: add a one-line caveat in the tier rationale. Swiftfoot Boots (hexproof) does not conflict.

**S7. Completeness: 20 most valuable omissions.**
- All 20 are in the pool, inside UBR, not Game Changers, and not cited anywhere in the report.
- Rank is Scryfall `edhrec_rank`, used as a sort aid only.

| # | Card (rank) | Why it fits Azula (pool oracle) |
|---|---|---|
| 1 | Roaming Throne (133) | Name Human: "If a triggered ability of another creature you control of the chosen type triggers, it triggers an additional time." Azula's copy trigger then fires twice for **every** spell (Veyran: only instants and sorceries), and firebending gives RRRR. It also doubles Archmage Emeritus (Human Wizard). Raises speed risk |
| 2 | Helm of the Host (392) | Each combat: a hasty, non-legendary token copy of Azula that attacks, so a second firebending and a second copy trigger (a stronger Shaun). Speed risk; also the commander-free Godo pair (M8) |
| 3 | Strionic Resonator (603) | "{2}, {T}: Copy target triggered ability you control": copies Azula's copy trigger or firebending |
| 4 | Harmonic Prodigy (640) | "If a triggered ability of a Shaman or another Wizard you control triggers, that ability triggers an additional time." Doubles Storm-Kiln Artist, Archmage Emeritus, Veyran, Ashling, Guttersnipe and others |
| 5 | Village Rites (204) | Instant {B}, sacrifice as additional cost, draw 2. The copy pays no sacrifice: 4 cards for {B} (the report's own Deadly Dispute logic) |
| 6 | Thought Vessel (21) | 2-mana rock; no maximum hand size for the big draws |
| 7 | Mind Stone (32) | 2-mana rock that cycles itself late |
| 8 | Pongify (155) / Rapid Hybridization (208) | 1-mana instant kill; the copy kills a second creature |
| 9 | Abrade (145) | 2-mana instant: 3 damage to a creature or destroy an artifact; doubled |
| 10 | Dismember (923) | Instant -5/-5 payable with life; works off firebending turns |
| 11 | Opt (216) | 1-mana instant cantrip: cast + copy = 2 draws and 2 magecraft triggers |
| 12 | Consider (364) | Same pattern as Opt |
| 13 | Faerie Mastermind (288) | Flash 2-drop draw engine; the token copy doubles it |
| 14 | Flusterstorm (309) | 1-mana instant answer to the removal spell aimed at Azula in combat |
| 15 | Expedite (1212) | Instant {R}: haste plus a draw. Azula can attack the turn she lands; the copy draws again |
| 16 | Return the Favor (573) | Spree: copy a triggered ability (Azula's trigger) or redirect removal |
| 17 | Cryptic Command (1610) | Copy repeats "tap all creatures your opponents control" plus counter, bounce or draw |
| 18 | Plaza of Heroes (473) | Land: any color for legendary spells, or any color among your legendaries |
| 19 | Sword of Feast and Famine (544) | Protection from black on the attacker; untaps lands for main phase 2 |
| 20 | Three Steps Ahead (1072) | Spree instant: counter, token copy of a creature or loot; all modes doubled |

Also worth a look:
- Thousand-Year Storm, Galvanic Iteration and Double Vision (copy multipliers; speed).
- Drown in Dreams ("If you control a commander ... choose both"; X kept on the copy).
- Hall of the Bandit Lord (haste), Relic of Legends, Brainsurge.
- Conqueror's Flail: it would get the same review flag as Tidal Barracuda.
- Karlach, Fury of Avernus and Genji Glove: extra combats, each one a new firebending and copy window.

Weak candidates to reconsider:
- Mox Amber and Hullbreaker Horror (S1).
- Kozilek's Return (2 damage to each creature also kills the 2/2 engines Storm-Kiln Artist, Archmage
  Emeritus and Veyran).
- Evacuation (returns Azula too, so commander tax).
- Insurrection (8-mana sorcery).
- Najal, the Storm Runner (5 mana; redundant flash enabler).
- Young Pyromancer, Murmuring Mystic and Kessig Flamebreather (cast-only triggers gain nothing from
  copies).
- Blasphemous Act at `strong` (it kills Azula).

## Findings: minor
- **M1 Mox Amber**: the report says "makes U/B/R only while Azula (legendary) is out". Oracle: "any
  color among legendary creatures and planeswalkers you control". Veyran, Baral, Ashling, Professor
  Onyx and others also count.
- **M2 Card arithmetic**:
  - Thrill of Possibility "net +3 cards": hand change is +2 (Thrill and the discard leave, 4 cards
    arrive).
  - Brainstorm "draw 6, put back 4": the second draw redraws the two cards put back, so only 4 new
    cards are seen.
  - Fire Nation Palace "6 red in combat": that is gross. After {1}{R} and the Palace's own tap, the
    net gain is +3.
- **M3 Mystic Confluence**: "the copy gives 3 more modes". The copy repeats the same three choices.
- **M4 Legend rule**: copies of legendary permanent spells become legendary tokens. Ertai
  Resurrected, Venser, Shaper Savant and Mithril Coat therefore leave one body after the legend
  rule, though both ETB triggers still happen. Not mentioned.
- **M5 §1 copy window list**: it omits spells cast during resolution, which Azula also copies
  (Electrodominance's free spell, Torrential Gearhulk's instant, cascade). It also omits flash
  noncreature permanents. Electrodominance also lets a sorcery be cast mid-combat, so it is a
  flash-style enabler for extra-turn sorceries. This is moot at 0 extra-turn cards.
- **M6 Budget pairs and price labels**:
  - These pairs are not like-for-like: Anger of the Gods and Ritual of Soot versus Damnation (both
    spare Azula); Fireball versus Comet Storm (a sorcery, so no copy without flash); Thrill versus
    Big Score (no Treasures); Commander's Sphere versus Arcane Signet (3 mana versus 2).
  - The label "budget" assumes prices, which the project treats as `unknown`. "Functional
    substitute" would be safer.
- **M7 MLD and stax lists**: incomplete. None of the missing cards is a candidate, and Layer A uses
  its own curated flags. All of these are in the pool and not cited:
  - MLD by the "four or more lands" definition: Apocalypse, Worldfire, Death Cloud, Devastating
    Dreams, Tectonic Break, Bend or Break, Mana Vortex, Mana Breach, Overburden, Storage Matrix,
    Infernal Darkness ("produces {B} instead"), Zhao, the Moon Slayer ("nonbasic lands are
    Mountains"), Curse of Marit Lage, Boil and Boiling Seas (destroy all Islands), and Pox.
  - Stax: Arcane Laboratory, Trinisphere, Chalice of the Void, Lodestone Golem, Defense Grid, Null
    Rod, Cursed Totem, Damping Matrix, Torpor Orb, Mindlock Orb, Void Winnower, God-Pharaoh's Statue
    and Imi Statue.
  - Conqueror's Flail belongs with the Tidal Barracuda review flags.
  - No card in the report's lists is wrongly excluded.
- **M8 Commander-free pairs list**: incomplete. All of these are in the pool:
  - Sanguine Bond + Exquisite Blood.
  - Godo, Bandit Warlord + Helm of the Host.
  - Birgi + Grinning Ignus (S2).
  - Hullbreaker Horror + Sol Ring and + Mox Amber (S1).
- **M9 Data quality**: the 48 Stickers rows are confirmed: type `Stickers`, set `sunf`,
  `legalities.commander: legal` in the bulk file. The pool also holds 22 Attraction or Contraption
  cards, which are not main-deck cards in practice. Drop them too.
- **M10 Extra turns: what the docs say, and the two readings** (decision for the owner).
  - `power-scale.md` Layer A has three relevant rules:
    - Per card: "1 card -> floor 2".
    - Count: "a card multiplied by the commander (Azula copies a spell cast while she attacks)
      counts as 2 | policy | 2 or more -> policy reject"; also "any chain or infinite-turn combo ->
      floor 4".
    - Commander effects: "a multiplied extra-turn card counts as 2 (conservative...)".
  - The snapshot quotes Wizards: "low quantities" and "not intended to be chained in succession or
    looped". "No numeric definition of 'low quantities' exists". So the official Bracket 3 text
    limits both the count (undefined) and the pattern (no chains or loops). It is not "only
    chained".
  - Reading A (Wizards' text alone): one extra-turn card is a low quantity, so 1 is allowed (floor 2).
  - Reading B (project policy, conservative): a copied spell gives two successive extra turns. That
    counts as 2, which is a reject, so 0 cards. It is arguably also a "chain", which would mean
    floor 4.
  - The report's "may hold 0" is the literal policy outcome and is correctly sent to the owner in
    §8.1.
  - Doc inconsistencies:
    - The power-scale table says "not chained" and drops "or looped".
    - The rationale "Spellbook tags 2+ as Ruthless" does not cover a single copied card. Spellbook
      counts cards, so it would tag C unless a combo flags `extraTurn`. The report's line "Spellbook
      alone also tags 2+ extra-turn cards R" is true but does not apply to this case.
    - "Multiplied" fits only spells Azula can copy. Extra-turn permanents with activated abilities
      (Magistrate's Scepter, Sage of Hours, Time Sieve) are not multiplied unless the permanent
      spell itself is cast in combat.
- **M11 Combo labels**: Bloodthirsty Conqueror + Arcbond (an Azula + 2-card infinite) and the
  Kiki-Jiki variant are labelled "unclear". Layer A says "any combo that uses the commander is
  reviewed as a floor 4 candidate". Label them "floor-4 candidate", as the conclusion (exclude)
  already implies.
- **M12 Kiki-Jiki variant name**: the Kiki-Jiki variant uses "Blazing Firesinger // Seething Song" (a
  `prepare` card). That is a different pool card from the candidate "Seething Song", so the variant
  does not touch the candidate. Fine, but worth one clarifying word.

## Could not verify
- Scryfall rulings for the 4 open questions in report §8.2 and for Azula's copy trigger: HTTP 403.
  - (a) Do Electro and Ashling keep firebending mana?
  - (b) The Shaun token copy.
  - (c) Veyran.
  - (d) CR 707.10.
  - My oracle reading agrees with (b) and (c). (a) remains open. (d) is background rules knowledge.
- Spellbook 2-card combos outside the Azula file (S1, S2): WebFetch summaries only. Phase 2
  `find-my-combos` must confirm them.
- Prices: none, as the project rules require.

Overall: ACCEPT WITH FIXES. Counts, names, Game Changers and Spellbook classification are correct, but the hazard section misses 2-card combos among the candidates (S1-S2) and one candidate-only loop (S3), with one copy-rule error (S4), a core-tier versus speed-table conflict (S5) and high-value omissions led by Roaming Throne (S7).
