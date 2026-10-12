Model ID: claude-opus-5-5

# Verification: synergy research for Toph, the First Metalbender (2026-10-11 report)

Independent second-researcher check, done 2026-10-12. Phase 3. The report under review is
`docs/research/synergy-toph-the-first-metalbender-2026-10-11.md`. It was not edited.

| Input | Use |
|---|---|
| `data/cache/pool_toph-the-first-metalbender.jsonl` | 18,537 cards; oracle text, including `card_faces` for 411 multi-face cards; `game_changer` |
| `data/cache/spellbook_toph-the-first-metalbender.json` | 1,099 variants, all containing Toph, all status OK |
| `data/cache/collect_manifest.json` | Game Changer cross-check |
| Rules | `docs/power-scale.md` v0.5, `docs/research/commander-brackets-rules-snapshot.md` (2026-02-09 beta) |
| Scripts | `scratchpad\toph-verifier\tv_*.py` (my own, written fresh; the original author's scripts were not used), run with `python -I` on local files only |
| Network | Commander Spellbook API: 7 variants spot-checked (4155-6871, 1167-6871, 4636-6871, 5175-6871, 486-6871-7033, 3470-5702-6871, 478-1766-6871). All 7 match the local file field for field. A `card="Toph..."` query returns `count: null` with first id 4155-6871, which also matches. Scryfall API: both calls (`/cards/named`, `/cards/{id}/rulings`) returned **HTTP 403**, so no official ruling could be read |

Labels: **rules background** = comprehensive-rules reasoning, not checkable against the pool.

## 1. Verdicts

| # | Check | Verdict | Evidence (short) |
|---|---|---|---|
| 1 | Name integrity | PASS | My own parse finds 198 rows, 0 duplicates, 0 missing from the pool, 0 color-identity violations, 0 Game Changers. Tiers: core 21, strong 92, situational 43, budget 42. Every role count matches its heading (35/8/16/19/11/12/22/17/7/5/46). All 42 budget targets are candidates. Prose: 386 pool names found; the only non-pool names are the 4 the report itself flags (Mana Crypt, Meloku the Clouded Mirror, Overburden, Tolarian Academy) |
| 2 | Oracle accuracy | PASS (minor) | 198 claims compared with the oracle text, using `card_faces` for the 4 multi-face candidates. No material error; 8 imprecise phrasings (M1) |
| 3 | Commander interaction | PASS | Re-derived from Toph's text; Spellbook descriptions back the Yavimaya and Caged Sun readings. Two rules gaps (M6). No official ruling could be read (HTTP 403) |
| 4 | Game Changers | PASS | 30 `game_changer: true` cards in the pool, the same set as the manifest. The section 4 table lists all 30 once, with none extra. The verdicts are consistent with "up to 3" and Wizards' Bracket 3/4 role wording |
| 5 | Bracket hazards | **FAIL** | A candidate-only infinite combo with the commander is missing (B1). Magus of the Candelabra is called a two-card combo but needs 3 pieces (S1). The section 6 wording on infinite-turn loops is wrong (S2). The MLD, sacrifice-outlet and extra-turn lists are incomplete (S3-S5) |
| 6 | Combos (counts) | PASS | Every count in the section 6 tables recomputes exactly. 0 Spellbook variants assemble from candidates + Toph, with or without templates. The 8 one-card-away cards are the same set. Sacrifice outlets: 262 by my text test vs. the report's 261 (M2) |
| 7 | Completeness | FAIL (partial) | 20 in-pool omissions that fit the archetype (S7). Toph's repeatable engines are not flagged (S8) |
| 8 | Speed claim | UNVERIFIED | Qualitative only. "Low" leaves out three early-kill packages that are in the candidate list (S6) |
| 9 | Tiers | PASS (notes) | Core picks and budget pairs are sensible and the colors match. Notes in M8 |

## 2. Findings

### Blocking

**B1. An unregistered deterministic infinite combo with the commander, built only from candidates.**
The report says (sections 3 and 6): "No subset of them, together with Toph, assembles any of the
1,099 Spellbook variants" and "Fine for Bracket 3: the recommended build needs no combo." The first
claim is true against Spellbook only. The candidate list holds this loop, which is not in the
Spellbook export: no Toph variant uses Emeria Shepherd, Prismatic Omen, Dryad, Lotus Petal or
Commander's Sphere (checked by script).

| Piece | Tier | Oracle text (pool) |
|---|---|---|
| Toph, the First Metalbender | commander | "Nontoken artifacts you control are lands" |
| Emeria Shepherd | situational | "Landfall — ... return target nonland permanent card from your graveyard to your hand. If that land is a Plains, you may return that nonland permanent card to the battlefield instead." |
| Prismatic Omen (or Dryad of the Ilysian Grove, core) | strong | "Lands you control are every basic land type" |
| Lotus Petal | situational | "{T}, Sacrifice this artifact: Add one mana of any color." |
| Commander's Sphere | strong | "Sacrifice this artifact: Draw a card." |

The loop, with Petal and Sphere in the graveyard and any landfall to start it:
1. Petal returns to the battlefield as a land and a Plains, and Shepherd triggers. The trigger targets Sphere.
2. In response, sacrifice Petal for one mana.
3. The trigger resolves and Sphere returns. Petal's last known information was a Plains (rules background, CR 608.2h), so the card goes to the battlefield, not the hand.
4. Sphere's entry triggers Shepherd, targeting Petal. In response, sacrifice Sphere and draw.
5. Repeat from step 1.

Each cycle gives +1 mana of any color, +1 card, 2 landfall triggers and 2 artifact enters and
leaves. That is unbounded. It wins with candidates such as Reckless Fireweaver, Tannuk or Ingenious
Artillerist (infinite damage), Scute Swarm or Felidar Retreat.
- Variants: Mind Stone in place of Sphere. With Lotus Cobra, any two self-sacrificing artifacts work.
- Bracket status: by Wizards' letter this is a 4-card combo, not a two-card one. Under project
  policy, "any combo that uses the commander is reviewed as a floor 4 candidate" (power-scale,
  Commander effects).
- Why it blocks: Layer A finds commander combos through Spellbook only, so it cannot catch this loop.
- Fix: list it in sections 5-6 as an unregistered combo. Exclude Emeria Shepherd, or forbid it
  together with Omen/Dryad and two self-sacrificing artifacts. Add to section 8 that combo screening
  must also look for loops Spellbook does not list.

### Should fix

**S1. Magus of the Candelabra is not a two-card combo.** Section 5 puts it in the "Two-card combos"
row ("Each completes an infinite with Toph plus one common card"). All 16 of its in-identity variants
have 3 pieces: Magus + Thousand-Year Elixir + a mana doubler, all tagged E. One of the doublers,
Nissa, Who Shakes the World, is a candidate. Move it to the larger-combo table. The exclusion stays.

**S2. Section 6 calls 3+ piece families "unclear (allowed by the letter...)".** That is wrong for
the infinite-turn loops in the same table: Ugin's Nexus (21 variants, tag R) and Magistrate's Scepter
(1, R).
- Wizards: extra turns must be "not intended to be chained in succession or looped".
- Power-scale: "any chain or infinite-turn combo -> floor 4".
- Section 5 calls these same combos floor 4, so the report contradicts itself.
- Aeon Engine (feature "Locks out all of your opponents but one") is a stax-style lock, so it should
  "bracket up".

**S3. The MLD list reads as complete but is not.** These pool cards meet Wizards' definition and are
missing: Global Ruin, Cataclysm, Cleansing, Fall of the Thran, Natural Balance, Restore Balance,
Balancing Act, Devastation, Apocalypse, Decree of Annihilation, Worldfire, Worldslayer, Bearer of the
Heavens, Myojin of Infinite Rage, Thoughts of Ruin, Bend or Break, Burning of Xinye, Epicenter, Ajani
Vengeant (−7), Price of Glory, Smokestack, Tectonic Instability, Wake of Destruction, Quicksilver
Fountain and Nature's Will ("tap all lands that player controls").
- Toph-specific: Nature's Revolt and Living Plane make all lands creatures, so any candidate creature
  wipe (Wrath of God, Blasphemous Act...) then destroys the opponents' lands. That is an MLD-by-intent
  pairing, like the Lattice + Vandalblast case the report already lists.
- None of these is a candidate. Mark the list as non-exhaustive or complete it before Layer A
  curation uses it.

**S4. The sacrifice-outlet hazard row names 8 cards; the export has 22 or more.** The others, with
their in-identity Toph variant counts:

| Count | Outlets |
|---|---|
| 16 | Need for Speed, Lithatog, Thaumatog, Troubled Healer, Trenching Steed |
| 15 | Thermopod |
| 10 | Extruder, Atog, Megatog, Krark-Clan Grunt, Ravenous Intruder |
| 6 | Spawning Pit |
| 5 | Grinding Station |
| 4 | Blasting Station |
| 1 | Oxidda Daredevil |

The Haru changelings are also missing: Stonework Puma 22, Firdoch Core 22, Stalactite Dagger 19,
Three Tree Mascot 18, Barkform Harvester 18, Bloodline Pretender 18, Universal Automaton 14.
Firdoch Core and Three Tree Mascot look like ordinary mana rocks, so a Phase 4 builder could add
them by accident. They are harmless only while Haru stays out.

**S5. The extra-turn list misses 3 pool cards.**
- Seedtime: "Take an extra turn after this one if an opponent cast a blue spell this turn".
- Emrakul, the Promised End: control of an opponent's next turn, then that player takes an extra turn.
- Perch Protection: gift an extra turn.

None is a candidate. The Layer A extra-turn count needs them.

**S6. The speed profile (section 7) leaves out early-kill packages that are in the candidate list.**
- Valakut, the Molten Pinnacle + Prismatic Omen or Dryad makes every artifact cast "3 damage to any
  target". Ancient Greenwarden ("land entering") and Panharmonicon ("artifact ... entering") each add
  one more trigger, so up to 9 damage per artifact. The report lists Valakut only as a win condition.
- Sylvan Awakening or Kamahl's Will turns every land and artifact into a hasty attacker. With
  Overwhelming Stampede or Craterhoof that is a one-turn alpha strike.
- The B1 loop.

Package size: 35 nonland artifacts, 7 of them at MV 0-1 and 16 at MV 2; Birds, Llanowar Elves,
Elvish Mystic, Joiner Adept, Lotus Cobra and Badgermole Cub; 7 land-ramp spells.
- The base list has no rituals and no Game Changer fast mana, so "low" is plausible. It is not shown.
- State it as "low to medium, unverified until the Monte Carlo run" and list these packages.

**S7. Completeness: 20 omissions** (all in the pool; reasons from the pool's oracle text).

| # | Card | Why it fits Toph |
|---|---|---|
| 1 | Dune Chanter | "Lands you control have '{T}: Add one mana of any color.'" The fifth lands-tap engine; the report lists 4 |
| 2 | Gavony Township | "+1/+1 counter on each creature you control": earthbended lands, tokens, Terrasymbiosis |
| 3 | Sword of Feast and Famine | "untap all lands you control", which under Toph means all your artifacts too |
| 4 | Blackblade Reforged | +1/+1 per land (artifacts count); equip legendary {3} (Toph) |
| 5 | Mithril Coat | Flash indestructible for Toph; the report's weakness list says "no ... protection" |
| 6 | Thought Vessel | 2-MV rock, peer of Mind Stone |
| 7 | Mox Amber | 0 MV, taps for Toph's colors: free landfall (speed note) |
| 8 | Mishra's Bauble | 0-MV free landfall + delayed draw |
| 9 | Tormod's Crypt | 0-MV landfall + graveyard hate (report section 8: graveyard hate "thin") |
| 10 | Expedition Map | 1-MV landfall; fetches Yavimaya, Valakut or Gavony |
| 11 | Steel Overseer | Counter on each artifact creature; earthbended artifacts qualify |
| 12 | Foundry Inspector | Artifacts cost {1} less: more landfall per turn |
| 13 | Planar Cleansing | "Destroy all nonland permanents": the Hour of Revelation asymmetry with no condition |
| 14 | Oblivion Stone | Colorless one-sided nonland wipe; a fate counter can save Toph |
| 15 | Starstorm | Instant creature wipe; earthbended lands return |
| 16 | Reclamation Sage / Force of Vigor / Rip Apart / Fateful Absence | Interaction the report calls thin (section 8, item 8) |
| 17 | Harrow | Instant; "sacrifice a land" (a spent artifact-land qualifies): 2 untapped basics |
| 18 | Geode Rager | Landfall: goad a whole board; each artifact cast goads |
| 19 | Cathars' Crusade | A counter on each creature per creature entering (Scute Swarm, Avenger Plants) |
| 20 | Moonshaker Cavalry; Avatar Kyoshi, Earthbender | A Craterhoof-style finisher with flying; earthbend 8 + untap every combat, hexproof on your turn |

Weak candidates to reconsider:
- Exploration and Azusa: the report itself says artifacts cannot be played as lands.
- Organic Extinction: 10 MV.
- Hellkite Tyrant: 20 artifacts is unrealistic with the report's 12-14-artifact slot shape.
- Darksteel Forge: 9 MV.
- Sensei's Divining Top: the claimed "loop" does not exist (M1).
- Lotus Petal and Emeria Shepherd: B1.

**S8. Toph's repeatable earthbend engines are not flagged.** An earthbended land that is sacrificed
"dies" and returns tapped, so Toph's end-step earthbend 2 makes these repeatable every turn:
- Inventors' Fair: "{4}, {T}, Sacrifice Inventors' Fair: Search your library for an artifact card",
  so a repeatable artifact tutor.
- Urza's Saga: re-enters at chapter I and fetches a 0/1-cost artifact again.
- Fetch lands and Myriad Landscape: an extra land and 2-3 landfall triggers per turn.

These break no Layer A rule (tutors are unrestricted). They matter for the bracket-fit review
(consistency and intent) and for tiering. The report mentions this only for Mind Stone, Burnished
Hart and Solemn.

### Minor

**M1. Imprecise phrasings, checked against the oracle text.**
- Nissa, Who Shakes the World: "+1 animates and untaps a land". The oracle says "target
  **noncreature** land", so it cannot target lands that are already earthbended.
- Earth Rumble: "the land creature does the fighting". The oracle says "up to one target creature you
  control fights", so any creature can.
- Sensei's Divining Top: "Draw-and-recast loop". The oracle puts it "on top of its owner's library",
  so there is no loop without another draw.
- Section 2 B: "counter doublers (Hardened Scales, Kami of Whispered Hopes)". Both add one counter
  ("that many plus one"); they do not double.
- Section 2 D: the one-card combos give "locks, skipped turns or infinite turns". None skips turns;
  Mindslaver gives opponent control.
- Section 1: "earthbended artifacts with sacrifice abilities reusable (Mind Stone, Burnished Hart,
  Solemn Simulacrum)". Solemn has no sacrifice ability; it is reusable when it dies.
- Darksteel Forge: "protects your lands from artifact and creature wipes". Indestructible does not
  stop exile wipes (Farewell).
- Section 6 calls the Elder/Weaver partners "an artifact-maker", but the family includes Marvin,
  Murderous Mimic (1606-5963-6871), which copies Ley Weaver's ability instead.

**M2. Outlet count:** 262 variants by a cost-text test. Oxidda Daredevil (6871-6879-7298-7369, a
Haru loop) explains the gap to the report's 261. Not material.

**M3. Heading "Three-card loops with Toph":** Toph, Hardheaded Teacher's 70 variants have 4 pieces,
and 15 of Staff of Domination's 47 have 4 pieces.

**M4. The bounce-land note** names 3 lands (36 variants). Arid Archway and Guildless Commons (12
Teacher variants each) are missing.

**M5. Combo-adjacent candidates:** the closing list in section 6 is incomplete. Also adjacent:
- Thran Dynamo and Everflowing Chalice: two-card Candelabra partners.
- Lotus Cobra, Tireless Provisioner and Nissa, Resurgent Animist: Springheart partners.
- Everflowing Chalice and Lotus Petal: they fill Teacher's "Artifact Castable for {0}" template.
- The 6 earthbend-on-entry creatures: they fill the Lattice templates.
- Doubling Season: with Clock of Omens + Bootleggers' Stash.

**M6. Rules gaps (rules background, not checkable: Scryfall 403).**
- Earthbending an attached Equipment makes it a creature, which then cannot stay attached (CR 301.5c).
- Artifact creatures that Toph makes lands (Solemn, Burnished Hart) are still summoning-sick for {T}
  mana abilities that Lantern grants.

The report's own rules claims are consistent with Spellbook descriptions:
- 1144-2645-4178-6871: "adding {G} as it's a Forest land due to Toph and Yavimaya".
- 5175-6871: Caged Sun "is a land due to Toph".

Blood Moon removing the artifact-lands' abilities stays unverified.

**M7. Shorthand names in prose** (Yavimaya, Urborg, Haru, Nissa, "Coating") are not exact card
names. Harmless, but tables should use full names.

**M8. Tiers.**
- Skullclamp (core): the rationale "earthbend-1 land" fits only Badgermole Cub and Bumi, Eclectic
  Earthbender. Toph's own earthbend 2 makes a 3/1 under Clamp, which does not die. The real payoff is
  Avenger's 0/1 Plants and Scute Swarm's 1/1 Insects. Keep core, fix the reason.
- Tamiyo's Safekeeping covers one permanent, so it is a weak "budget alternative" to Heroic
  Intervention's board-wide protection.

## 3. Hazard cards examined (check 5)

| Card | Spellbook (local; API-checked where marked) | Rule applied | B3 problem? | Report |
|---|---|---|---|---|
| The Stasis Coffin | 4155-6871, S, Lock, protection on opponents' turns, {2} per turn (API ✓) | Lock = review flag; commander combo = floor-4 candidate | Review; exclusion sound | Agrees |
| Mindslaver | 1167-6871, R, "control one opponent on each of their turns", Lock, {4} per turn (API ✓) | R = floor-4 flag (power-scale) | Yes | Agrees |
| Gonti's Aether Heart | 4636-6871, R, Infinite turns, 6 energy per turn (API ✓) | Looped extra turns -> floor 4 | Yes | Agrees |
| Caged Sun | 5175-6871, R, Draw the game, mandatory (API ✓) | Not a bracket category | Unplayable | Agrees |
| Staff of Domination | 47 E variants; 32 with Yavimaya/Urborg + doubler, incl. candidate Nissa, Who Shakes the World | 3-card commander infinite: policy review | Policy | Agrees |
| Mycosynth Lattice | 37 variants (3 two-card); + Vandalblast (candidate) = opponents' lands destroyed | MLD by intent; two-card | Yes | Agrees |
| Candelabra of Tawnos | 24 two-card variants, MV 0, partners include candidates Thran Dynamo and Everflowing Chalice (API ✓ 478-1766) | Early two-card infinite | Yes | Agrees |
| Magus of the Candelabra | 16 three-piece variants, E | Not two-card | Policy only | Wrong row (S1) |
| Springheart Nantuko | 4 two-card variants, S, MV 4, partners are 3 candidates (API ✓ 3470-5702) | Two-card, speed >= 4 | Yes | Agrees |
| Bumi, Unleashed | 7 two-card variants, E, MV 0-2, infinite combats (API ✓ 486-6871-7033) | Two-card infinite | Floor-4 candidate | Agrees |
| Argothian Elder / Ley Weaver | 7 / 8 two-card variants, S, infinite mana | Two-card infinite | Yes | Agrees |
| Haru, Hidden Talent | 159 three-card variants | 3-card commander infinite | Policy | Agrees |
| Sacrifice outlets | 22+ cards across 262 variants | Not hazards alone | Combo check | Incomplete (S4) |
| Emeria Shepherd + Omen/Dryad + Petal + Sphere | **Not in Spellbook** | Commander combo -> floor-4 candidate | Yes, by policy | **Missed (B1)** |

## 4. Reproduction (scratchpad `toph-verifier\`)

| Script | Result |
|---|---|
| `tv_v1_names.py` | 198 rows; dup 0; missing 0; CI violations 0; GC 0; tiers 21/92/43/42 |
| `tv_v2_dump.py 0 198` + `card_faces` | 198 claims compared with the oracle text |
| `tv_v3_sb.py` | 1,099; tags E 991, S 57, R 46, P 3, B 2; pieces 4/90/717/288; in-identity 400, tags E 333, S 39, R 25, P 3, pieces 4/52/274/70; features Lock 26, Infinite turns 23, combat phases 7, draw 2, opponent control 1 |
| `tv_v6_combos.py` | Full assemblies from candidates 0; one-card-away cards: Springheart x3, Candelabra x2, Stasis Coffin, Mindslaver, Gonti's, Caged Sun, Staff, Meloku |
| `tv_v7_small.py two` | 52 in-identity two-card variants = Candelabra 24 + Elder/Weaver 15 + Bumi 7 + Springheart 4 + others 2 |
| `tv_v8_fam.py` | Family make-up; outlet count 262; Magus 16 x 3-piece |
| `tv_v9_scan.py`, `tv_v10_present.py` | Extra-turn, earthbend, land-effect and MLD scans; presence of the omissions |

Overall: ACCEPT WITH FIXES. Every count, name, Game Changer and Spellbook classification checks
out, and the 4 one-card combos match the live API. B1 must be fixed before Phase 4 uses the list,
because it is a candidate-only commander combo that Spellbook-based Layer A cannot detect. The fix
is small: one exclusion note plus a screening caveat. S1-S8 are corrections and additions, not a
rework.
