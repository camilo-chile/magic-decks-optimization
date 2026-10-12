Model ID: claude-opus-5-5

# Verification: synergy report for Alexios, Deimos of Kosmos

| Item | Value |
|---|---|
| Report under review | `docs/research/synergy-alexios-deimos-of-kosmos-2026-10-11.md` |
| Role | Independent second researcher; goal was to find errors and omissions |
| Run date | 2026-10-12 (UTC); network spot checks made on this date |
| Local data | `data/cache/pool_alexios-deimos-of-kosmos.jsonl` (7,552 cards, Scryfall bulk 2026-10-11T21:01:56Z), `spellbook_alexios-deimos-of-kosmos.json`, `collect_manifest.json`, `collect_progress.log` |
| Network | `backend.commanderspellbook.com` JSON API: worked. `api.scryfall.com`: **HTTP 403** on all 3 attempts (`/cards/{id}`, `/cards/{id}/rulings`, `/cards/named`), so no Scryfall rulings were read |
| Not used | `data/raw/`, EDHREC, any other domain |
| Method | Read-only Python (`python -I`, `magic-decks` env) in the session scratchpad: report-table parser, pool regex search over oracle and face text, hazard-name validator. Card facts below are quoted from pool oracle text unless marked otherwise |

## Summary of checks

| # | Check | Verdict | Key evidence |
|---|---|---|---|
| 1 | Name integrity, counts | **PASS** | 195 rows, 195 unique, 0 missing from pool, 0 identity violations; role counts 29/29/21/14/15/47/11/6/23 match; tiers 15 core / 74 strong / 78 situational / 28 budget match; all 28 budget targets are candidates; 81 hazard names all in pool, 81 unique, group counts 27/13/8/21/12 match |
| 2 | Oracle accuracy | **FAIL (minor)** | 8 misstatements, none changes the plan (see M1-M8) |
| 3 | Commander interaction | **PASS** with 1 claim error | Core reading is correct; the 110-damage arithmetic is correct; the Andúril / Captain's Claws "blockers" claim is wrong (S7) |
| 4 | Rules readings R1-R8 | **FAIL** | R5 consequence WRONG, R8 "only Helm" WRONG; R3, R7 CONFIRMED from text and logic; R1, R2, R4, R6 UNVERIFIED (Scryfall 403, CR not read) |
| 5 | Game Changers | **PASS** | Pool has 15 GCs, equal to the manifest; candidates hold exactly 3 GCs (Jeska's Will, Ancient Tomb, The One Ring), all labelled; none mislabelled or missing; "2, optional 3rd" stays within the snapshot's "max 3"; commander is `game_changer: false` |
| 6 | Bracket hazards | **FAIL** | No candidate is itself a hazard, but the exclusion list misses Spellbook-flagged MLD (6), extra turns (2), 4 two-card combos and several stax / opponent-control cards; the tutor statement is wrong (S1-S6) |
| 7 | Completeness | **FAIL** | 20 high-value omissions (table below), led by All Is Dust, Brotherhood Regalia, Furious Rise and equipment tutors |
| 8 | Spellbook | **PASS** | Empty result is real: the Spellbook card record shows Alexios `variantCount: 0`; the same query returns results for Helm of the Host; `count: null` is normal for this API |
| 9 | Tiers | **PASS** with notes | 15 core are reasonable; 3 budget pairs have a closer substitute in the pool; 2 tier inconsistencies (M9-M11) |

## Check 3: how the commander works (re-derived from its oracle text)

Pool text: "Trample / Alexios attacks each combat if able, can't be sacrificed, and can't attack its owner. / At the beginning of each player's upkeep, that player gains control of Alexios, untaps it, and puts a +1/+1 counter on it. It gains haste until end of turn."

- Each player controls it on their own turn; it gains a counter and haste at every upkeep; it can never attack its owner; edicts and sacrifice costs cannot touch it. The report states all of this correctly.
- Cast in your main phase it has no haste, so it does not attack on the turn it is cast. From your turn 4 to just before your turn 7 it attacks 3 + 1 + 3 + 1 + 3 = 11 times at power 5..15, sum 110. **Arithmetic confirmed.** Under the report's own assumptions (never blocked or removed), 110 damage across 3 opponents gives at least 37 to one of them, so "at least one opponent dies to commander damage" holds.
- Equipment triggers worded "you ..." (Sword of Fire and Ice "you draw a card", Sword of the Animist "you may search") are the Equipment's own abilities, so they pay you on every turn. Quoted abilities granted to the creature (The Reaver Cleaver, Diamond Pick-Axe, Vibranium Strike Gauntlets) pay whoever controls Alexios. The report's synergy claims agree with this split.
- Claim errors: Andúril / Captain's Claws (S7). Minor wording issues are in M1-M8.

## Check 4: rules readings

| # | Verdict | Evidence |
|---|---|---|
| R1 | UNVERIFIED (consistent with text) | The trigger wording on the Equipment ("you draw", "you may search") supports it. Scryfall rulings could not be read (403). From memory, CR 301.5d separates equipment control from creature control; not verified here. It still carries archetype A, so open question 4 stays open |
| R2 | UNVERIFIED (consistent with text) | The granted abilities are quoted (Reaver Cleaver, Diamond Pick-Axe, Sticky Fingers). Guild Artisan, Popular Entertainer and Tavern Brawler are Backgrounds ("Commander creatures you own have ...") and are legal in the 99 |
| R3 | CONFIRMED (text) | Super State, Pain for All and Breath of Fury read "Enchant creature you control"; Shiny Impetus and The Sound of Drums read "Enchant creature". The state-based action itself is CR, not read |
| R4 | UNVERIFIED | No CR text or ruling read; it is the standard reading |
| R5 | Rule UNVERIFIED; **consequence WRONG** | See S7: the tokens enter tapped |
| R6 | UNVERIFIED | No Tome of Legends ruling was reachable |
| R7 | CONFIRMED (logic) | Both triggers fire as the upkeep begins, while the previous player still controls Alexios, so a granted "your upkeep" trigger never matches. Edge case: an effect that returns Alexios to you before your upkeep (for example Homeward Path) would let it fire |
| R8 | Legend-rule part CONFIRMED; **"Only Helm of the Host makes non-legendary copies" WRONG** | See S8 |

## Check 8: Spellbook (live API, 2026-10-12)

- `GET /variants/?q=card="Alexios, Deimos of Kosmos"`: `count: null`, `next: null`, 0 results (the same as the cached file).
- `GET /cards/?q=Alexios`: the record exists, with `identity: "R"`, `gameChanger: false`, `variantCount: 0`, commander-legal. So the name resolves and **no combo uses Alexios**. Open question 5 can be closed.
- Positive control: the same syntax for Helm of the Host returns many variants, also with `count: null`. A null count is how this API always answers, not a sign of failure (the manifest shows `count: null` for Toph's 1,099 variants too).
- Side note: the `collect_progress.log` lines ("page 1/1 ... ETA") do not match the current `fetch_spellbook` branch for `count is None`, so the script was probably edited after the run. Harmless, but re-run it before Phase 4 if the cache is reused.

## Findings

### Blocking

None. Every gap below is either outside the candidate list or would be caught by the Phase 2 Spellbook gate on the final list, which the report itself requires.

### Should fix

**S1. Helm of the Host partner list is incomplete.** Report: "Keep Helm only with all six creatures excluded" (Godo, Combat Celebrant, Port Razer, Bloodthirster, Fear of Missing Out, Raphael). Spellbook with `card="Helm of the Host" ci<=r` lists these two-card variants: Combat Celebrant (1692-2105), Godo (1692-4251), Kiki-Jiki (618-1692), Port Razer (1548-1692), **Scourge of the Throne (1405-1692)**, **Akki Battle Squad (1692-4367)**, Fear of Missing Out (1692-6188) and Breath of Fury (1692-3259). Scourge of the Throne and Akki Battle Squad are in the pool and **missing from the report**. Kiki-Jiki and Breath of Fury are excluded for other reasons. Bloodthirster and Raphael do not appear as Helm variants in Spellbook; they are plausible from oracle text, so keeping them excluded is harmless. Fix: name all 8 partners as the condition for keeping Helm.

**S2. Fable of the Mirror-Breaker (candidate, "strong") is a two-card combo hub.** Spellbook 2105-3337--140: Fable // Reflection of Kiki-Jiki + Combat Celebrant gives infinite combat phases. Spellbook also lists Fable + Zealous Conscripts + Panharmonicon (1537-2397-3337). The report's combo 5 lists only Kiki-Jiki, Mirror Breaker. Fable is safe only while Combat Celebrant stays excluded, and that exclusion is currently justified only through Helm. Add Fable to the combo table.

**S3. Missing two-card combo: Metalworker + Staff of Domination** (Spellbook 578-2645, identity C, both cards in the pool). It gives infinite colorless mana, cards and life, with the prerequisite "at least three artifact cards in hand". It is likely to come up in an artifact-heavy deck. Add it to the hazard list.

**S4. The mass land denial list (27) misses cards that Spellbook itself flags `massLandDenial: true`** (checked one by one on 2026-10-12):
- Myojin of Infinite Rage ("Remove a divinity counter ...: Destroy all lands.")
- Quicksilver Fountain (turns lands into Islands)
- Winter Moon ("Players can't untap more than one nonbasic land")
- Rumbling Crescendo ("Destroy up to X target lands")
- Wake of Destruction
- Boil ("Destroy all Islands")

Same text as Boil, flag not checked: Boiling Seas and Flashfires. Spellbook does not flag Scorched Earth, Orcish Settlers or Ember Swallower, so those stay judgment calls. Fix: either add these cards or say the list is non-exhaustive and that Layer A relies on Spellbook's card flag.

**S5. The extra-turn list (8) misses 2 Spellbook-flagged cards** (`extraTurn: true`). Emrakul, the Promised End also gives "control of target opponent during that player's next turn". Ugin's Nexus reads "instead exile it and take an extra turn". Opponent-control effects are absent from all groups: Emrakul, Mindslaver ("You control target player during that player's next turn") and The Dominion Bracelet (granted ability, same effect). Under the power-scale Lock / control row these are review flags.

**S6. The tutor statement is false.** Report §5: "this pool's tutors are few: Gamble, Urza's Saga, Inventors' Fair, Godo". A pool search for "search your library for a/any ... card", excluding basic-land fetches, returns **56 cards**. Examples: Imperial Recruiter, Goblin Matron, Goblin Engineer, Expedition Map, **Reckless Handling** (any artifact), **Maximus, Knight Apparent** (Equipment with mana value 2), **Tezzeret, Cruel Captain** (artifact with mana value 1 or less), Kuldotha Forgemaster, Fervent Mastery, Cool but Rude, Planar Bridge, Treasure Chest. There is no bracket effect (tutors have been unrestricted since 2025-10-21), but the equipment tutors are missing from the candidates (see check 7).

**S7. R5 consequence and the Andúril / Captain's Claws claims are wrong.** Andúril: "create two tapped 1/1 white Spirit creature tokens with flying. If that creature is legendary, instead create two of those tokens that are tapped and attacking." Captain's Claws: "a 1/1 ... token that's tapped and attacking." On opponents' turns these tokens enter **tapped** and not attacking. They cannot block that turn; they untap in your untap step and can block on later opponents' turns only if they did not attack on yours. Fix the sentence "Andúril, Flame of the West and Captain's Claws give you blockers on opponents' turns". Moonsilver Spear's Angel enters untapped and is the real blocker source.

**S8. R8: "Only Helm of the Host makes non-legendary copies" is wrong.** Pool cards that do the same:
- Delina, Wild Mage: "a tapped and attacking token that's a copy of that creature, except it's not legendary"
- Tempestra, Dame of Games: "a copy of another target creature you control, except it isn't legendary"
- Hall of Mirrors: "except it isn't legendary"

Mirror Box ("The 'legend rule' doesn't apply to permanents you control"), Mirror Gallery and Hall of Echoes switch the legend rule off. With one of them, copies from Heat Shimmer, Twinflame, Molten Duplication and Blade of Selves survive. Fix the wording. Any copy effect plus Mirror Gallery or Mirror Box needs a combo check in Phase 4.

**S9. Twenty high-value omissions** (all in the pool; card text quoted from the pool). The ranks are Scryfall's `edhrec_rank` field from the bulk file, a popularity hint only.

| # | Card | Why it fits Alexios (from oracle text) |
|---|---|---|
| 1 | All Is Dust | "Each player sacrifices all permanents ... that are one or more colors": Alexios "can't be sacrificed", and colorless equipment, rocks and lands stay. A near one-sided wipe that suits this deck better than any listed sweeper |
| 2 | Brotherhood Regalia | Ward {2}, "can't be blocked", "Equip legendary creature {1}" (rank 562). Note that ward also taxes your own targeting while an opponent controls Alexios |
| 3 | Furious Rise | Card each of your end steps "if you control a creature with power 4 or greater" (Alexios on your turn) |
| 4 | Endless Atlas | "Draw a card. Activate only if you control three or more lands with the same name": always on in a Mountain base |
| 5 | Reckless Handling | {1}{R}: search for any artifact (any Sword, Helm or Plate) |
| 6 | Maximus, Knight Apparent | Tutors an Equipment with mana value 2 (Swiftfoot Boots, Sword of the Animist, Jitte, Mask, Blackblade) |
| 7 | Magnetic Theft | {R} instant: "Attach target Equipment to target creature": equip at instant speed on any turn, including onto Alexios while an opponent controls it |
| 8 | The Spear of Leonidas | The Equipment's own trigger on every attack: double strike, a Phobos token for you, or loot (counts as a multiplier when the double strike mode is used) |
| 9 | Mjölnir, Storm Hammer | Attaches itself to a legendary creature; each attack taps and stuns a creature and deals damage to each of your opponents |
| 10 | Strength-Testing Hammer | On attack, "if it has the greatest power ... draw a card" (you draw; Alexios is usually the biggest) |
| 11 | Dream-Thief's Bandana | Per hit, exile the victim's top card; "you may play it" |
| 12 | Glamdring | Per hit, cast an instant or sorcery from hand free (a Buster Sword analogue) |
| 13 | Bloodforged Battle-Axe | Per hit, "create a token that's a copy of this Equipment": it snowballs on every turn |
| 14 | Bitterthorn, Nissa's Animus | The same basic-land-on-attack trigger as Sword of the Animist; a closer budget alternative than Explorer's Scope |
| 15 | Lavaspur Boots | Haste plus ward {1}, equip {1}; a closer budget alternative to Swiftfoot Boots than Leather Armor (which gives no haste) |
| 16 | Thran Power Suit | +1/+1 per attached Equipment and ward {2} |
| 17 | Not of This World | Counters a spell or ability that targets your permanent; costs {7} less when it protects a creature with power 7 or more (a grown Alexios on your turn) |
| 18 | Slicer, Hired Muscle | The same pass-the-bomb design (passed to opponents at their upkeep, goaded, "can't be sacrificed", double strike) for archetype B |
| 19 | Fast Forward | "Goad all creatures your opponents control", cheaper after Alexios attacks; a second Disrupt Decorum |
| 20 | Buried Ruin | Land that returns a destroyed key artifact to hand |

Also worth a look: Tezzeret, Cruel Captain; Imperial Recruiter (finds Komainu Battle Armor or Lizard Blades); Hero's Blade; Karn's Bastion (proliferate Alexios's counters on any turn); Delina, Wild Mage (non-legendary Alexios copies).

**S10. Combo-class rationale misquotes the power scale.** Combos 2 and 3 are labelled "Floor-4 trigger (8 mana or less ...)". The power scale's floor-4 threshold is `speed >= 3`: about 6 mana or less, or up to 8 **only when Spellbook's accuracy flag is false**. The conclusion (exclude Aggravated Assault and Neheb) is unchanged, but the stated rule is wrong. Spellbook confirms Sword of Feast and Famine + Aggravated Assault (900-3750) and Hellkite Charger + Sword of Feast and Famine (900-3398). Speed can only be read from `/estimate-bracket` and was not checked here.

### Minor

- **M1. Blasphemous Act:** "a grown Alexios (13+ toughness) survives". 13 damage kills a creature with toughness 13; it needs **14 or more**.
- **M2. Agitator Ant:** "Each end step". The text says "At the beginning of **your** end step, each player **may** ...".
- **M3. Curse of Opulence:** omits "Each opponent attacking that player does the same". The active opponent who sends Alexios at the cursed player also gets Gold, and that opponent picks the target.
- **M4. Sol Ring:** "puts Alexios out on turn 3". A turn-1 Sol Ring plus 2 lands gives 4 mana on turn 2, and §7 itself says "turn 2 or 3".
- **M5. Sword of Truth and Justice:** "Alexios grows faster". On opponents' turns "put a +1/+1 counter on a creature you control" cannot target Alexios; only the proliferate adds 1.
- **M6. Wild Magic Surge:** omits that its controller reveals until a permanent sharing a type and puts it onto the battlefield.
- **M7. Mana base:** "RRR only on Furnace of Rath and Fiery Emancipation". The overload costs of Mizzium Mortars ({3}{R}{R}{R}) and Spectacular Showdown ({4}{R}{R}{R}) also need RRR.
- **M8. Assault Suit:** "repeats Alexios's own text" is inaccurate. It adds +2/+2 and "can't attack you **or planeswalkers you control**", which plugs the planeswalker weakness the report names. It is still weak, but the stated reason is wrong.
- **M9. Inconsistent exclusion:** Hexplate Wallbreaker is excluded for giving the active opponent an extra combat, while Genji Glove ("there is an additional combat phase") has the same effect and is kept as situational.
- **M10. Tiers:** Whispersilk Cloak is "strong" and Lightning Greaves "situational", although both have shroud. Shroud and hexproof gear (Swiftfoot Boots is core) also stop you targeting Alexios on opponents' turns with Rogue's Passage (core), Bolt Bend or Magnetic Theft. Note this anti-synergy in the core rows.
- **M11. Spectacular Showdown in core** sits awkwardly with §7 ("favor value, evasion and protection equipment over multipliers; cap multipliers at 1 or 2"). It is acceptable as the single multiplier if stated explicitly.
- **M12. Budget pairs that are weak substitutes:** Explorer's Scope for Sword of the Animist (Bitterthorn is closer), Leather Armor for Swiftfoot Boots (Lavaspur Boots is closer), Flame Slash for Lightning Bolt (a sorcery, creatures only). The other 25 pairs are genuine functional substitutes.
- **M13. Weak candidates to demote or drop:**
  - Ellie, Brick Master: on every Alexios attack during an opponent's turn, "that attacking player creates a tapped 1/1 ... token", so opponents get permanent bodies.
  - Fumiko the Lowblood: forced attacks can target you.
  - Goblin Spymaster: gives opponents tokens that can attack you.
  - Twinflame Tyrant and Fiery Emancipation: they double or triple Alexios only on your turn.
- **M14. A four-card Spellbook combo with three candidate pieces:** Sword of Feast and Famine + Sword of Hearth and Home + Seize the Day or Relentless Assault + Ardent Elementalist (900-1550-2239-2481 and -2489). It is not two-card, so not a Bracket 3 rule issue, but list it for the bracket-fit review.
- **M15. Rules snapshot:** the report says to re-check after the 2026-10-12 announcement. That date is today, so re-check the 15 Game Changer flags before Phase 4 (not done here).

## What could not be verified

- No Scryfall rulings were read (HTTP 403 on every endpoint tried), and no Comprehensive Rules text was read. R1, R2, R4 and R6 stay unverified; R1 is the critical one.
- Spellbook `speed` and two-card class for the combos (only `/estimate-bracket` exposes speed; it was not called).
- Spellbook MLD flags for Boiling Seas and Flashfires.
- Whether Bloodthirster + Helm and Raphael + Helm are real infinites (absent from Spellbook; plausible from oracle text).

Overall: ACCEPT WITH FIXES. Names, counts, Game Changers, the commander reading and the speed arithmetic are correct, and no candidate breaks Bracket 3. The hazard and combo maps are incomplete (S1-S5: Helm and Fable partners, Metalworker + Staff, 6 Spellbook MLD cards, 2 extra-turn cards). Two rules consequences are wrong (S7, S8), the tutor claim is false (S6), and about 20 strong fits are missing (S9). All of these should be fixed before the Phase 4 reference build.
