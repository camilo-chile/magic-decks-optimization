# Independent review: Alexios, Deimos of Kosmos, mono-red 100-card list (reference v2)

Reviewer: independent (did not build the list). Date: 2026-10-12. Scope: offline and read-only, per the brief.
Inputs: `reference.txt`, `reference-notes.md`, `slot-ranking.json`, the rules-check file, `data/cache/comprehensive-rules.txt` (effective 2026-09-25), `data/cache/rulings_pool.jsonl`, `data/cache/spellbook_variants_slim.jsonl.gz`, `data/cache/pool_alexios-deimos-of-kosmos.jsonl`, `gate.py` (`check`, `lookup`).

Temp files I wrote in this folder (allowed by the brief): `names_all.txt`, `lookup_list.txt`, `oneaway_missing.txt`, `oneaway_missing_ok.txt`, `oneaway_lookup.txt`, `fillers_names.txt`, `fillers_lookup.txt`, `candidates.txt`, `candidates_lookup.txt`.

Tooling note: `gate.py lookup` crashes with `UnicodeEncodeError` on a Windows console when a card text has a non-cp1252 character, unless it runs with `python -I -X utf8` (the env var `PYTHONIOENCODING` is ignored under `-I`). I used `-I -X utf8` for every run.

---

## A. Legality and counts

| Check | Result |
|---|---|
| `gate.py check reference.txt` | bulk `oracle-cards-20261011210156`; cards 100, recognized 100, floor 3, rejected False; game changers 3 = ['Ancient Tomb', "Jeska's Will", 'The One Ring']; extra-turn 0; mass land denial {}; Spellbook 0 variants inside the deck, 0 flagged, 97 one card away; hazard floor 3 (review-only stax row for Silent Arbiter); speed very high (83.1% by turn 6) |
| Unique names sent to `lookup` | 76 (75 non-Mountain names + Mountain once; Mountain x25 = 100 cards) |
| `lookup` found | 76 / 76 |
| Legal (both formats) | 76 / 76 |
| Color identity | 36 entries with CI R (includes Alexios and Mountain), 40 colorless (CI []); none outside R |
| Singleton (non-basic) | 75 names, 1 copy each; `dup []` |
| Game Changers from lookup flags | 3: The One Ring, Jeska's Will, Ancient Tomb (matches gate) |
| Names exact | all 76 names match Scryfall names (DFC names in full) |

Result: 100 cards, 3 Game Changers, floor 3, all legal, all in R or colorless, singleton. No BLOCKER on conditions 1 and 2.

## B. Extra turns and mass land denial

Extra turns: none. No oracle text in the 76 names contains "extra turn". Extra phases only: Genji Glove and Godo ("additional combat phase"). Per CR 500.8 these add combat phases, not turns. Condition 4 holds (0 cards).

Cards that affect lands (every oracle text read):

| Card | Text (lookup) | Judgment |
|---|---|---|
| Argentum Armor | "Whenever equipped creature attacks, destroy target permanent." | Judgment, see F-01. Single target per attack, any permanent, controller's choice. Repeated land destruction is possible if the controller chooses lands. Not a mass effect by text. |
| Chaos Warp | "The owner of target permanent shuffles it into their library..." | Single target. OK. |
| Wild Magic Surge | "Destroy target permanent an opponent controls..." | Single target. OK. |
| Sword of Feast and Famine | "...you untap all lands you control." | Own lands only, untap. OK. |
| Pip-Boy 3000 | "Check Map: Untap up to two target lands." | Untap, per attack. OK. |
| Sword of the Animist, Sword of Hearth and Home, Solemn, Wayfarer's Bauble, Urza's Saga | fetch a basic land or an artifact | Ramp. OK. |
| Abrade, Fiery Confluence | "Destroy target artifact" | No land in the list is an artifact (Urza's Saga is an enchantment land). OK. |
| Blasphemous Act, Anger of the Gods, Mizzium Mortars, Comet Storm, Rebel Salvo, Fury | creatures / planeswalkers / any target, damage only | No land effect. OK. |
| Mystic Forge | "...cast artifact and colorless spells from the top of your library" | Ruling 2019-07-12: no lands. OK. |

Treasure or land recursion loops: none found. Goblin Engineer returns artifacts only; Hearth blinks creatures only (one per Alexios hit); Solemn makes one land per ETB. No loop.

Verdict B: condition 3 holds on the text. Argentum Armor is the judgment call (F-01).

## C. Combos (Spellbook plus manual)

Spellbook (local slim bulk, 114,400 variants):
- Variants with every card inside the 76 names: **0** (matches gate).
- Variants with exactly one card outside the list (no filter on status): 99. Gate reports 97; the gap is not investigated (likely the commander-legal filter).
- Variants fully inside list + 141 fillers: **0** (filler check passes).
- Notes' one-card-away list: all 32 partners that are red or colorless and legal were found by `lookup` (`oneaway_lookup.txt`). All 32 are in the notes' never-add list. None is in the list. Toralf, God of Fury resolves as `legal not_legal` (not Commander-legal). Yavimaya Bloomsage did not resolve (green by printing, UNVERIFIED).

Pairs and loops checked by hand (step by step):

| # | Pair / loop | Mana | Needs a third card? | Result |
|---|---|---|---|---|
| 1 | Godo + Sword of Hearth and Home | Godo 6, Hearth 3 | Yes: 16 red-identity haste/untap enablers (Spellbook tag E, MV 0), none in the list | Not a 2-card combo. Enablers outside the list. |
| 2 | Godo + Hearth + Swiftfoot Boots (in list) + Ardenn | - | Yes: Ardenn, Intrepid Archaeologist (`CI ['W']`, not R) | Not buildable in R. Spellbook 1550-4251-6233--78. Boots in the list is the haste piece. |
| 3 | Godo + Hearth + Boots by hand (no Spellbook entry) | - | - | Hearth triggers only from the equipped creature (Alexios), and Godo's haste comes from Boots only once. Glove untaps Alexios in the first combat only. No repeating cycle. Not infinite. UNVERIFIED by engine. |
| 4 | Sword of Hearth and Home + Akki Battle Squad | 0 | Akki is outside the list | Spellbook 1550-4367. Never add (in notes). |
| 5 | Goblin Engineer + Hearth blink, or + Mind Stone | Engineer R | No | Each activation taps Engineer. Re-untap only via a Hearth blink, one per Alexios hit. Finite. |
| 6 | Walking Ballista loops | - | - | Ballista does not untap; rocks do not untap; lands untap once per hit (Feast) or per attack (Pip-Boy). Each counter costs 4. Finite. Spellbook Ballista partners are all non-R (Heroic Feast, Spider-Man, Destined White Mage, Urban Daggertooth, Mortuary (B)). |
| 7 | Mystic Forge + Foundry Inspector / Jhoira's Familiar | - | Sensei's Top (outside, never add) | No loop with the list. |
| 8 | Kediss + Grafted Exoskeleton | 4 + 2 | Yes (outside, colorless) | Spellbook 2822-3681. Never add (in notes). Kediss + Glistening Oil / Phyresis / Tainted Strike / Corrupted Conscience / Triumph of the Hordes: not red or colorless (not in the 32), not buildable. |
| 9 | Thorin + Hearth blink | 4 | No | One Thorin trigger per hit. Finite. |
| 10 | Genji Glove + Godo | - | No | At most one extra combat per Glove trigger and per Godo attack. Finite. |
| 11 | Masterwork of Ingenuity + Hammer | 1 | No | Copy enters, Hammer triggers once per copy. Legend rule (CR 704.5j with 707.2) blocks Jitte, Animist and Hammer copies. Finite. |
| 12 | Argentum Armor + Goblin Engineer | - | No | Armor destroys my own artifact, Engineer returns it once per untap. Finite. |
| 13 | Kediss + Alexios | - | No | The copy is not combat damage and does not re-trigger Kediss (ruling 2020-11-10). No chain. |
| 14 | Any 2-card win within 6 mana | - | - | Alexios is 4/4 base (pool file). Best 2-card hit: Alexios + Flail, 5 power x2 = 10 damage. Not lethal. |

Verdict C: no in-list 2-card infinite or 2-card win found (Spellbook: 0; manual: 14 pairs, none closes). Loops 1, 3 and 5 involve a repeating combat cycle that the list cannot sustain (UNVERIFIED by a rules engine).

## D. Rules claims (15 most important)

| # | Claim in notes | Source checked | Verdict |
|---|---|---|---|
| 1 | Equipment triggers stay with the Equipment's controller when an opponent controls Alexios | Pact Weapon 2022-06-10: "you still control Pact Weapon"; "attacks with it, you will draw a card". Armory Automaton 2016-11-08: an Equipment's "you" refers to the Equipment's controller; triggers fire if attached at declaration | CONFIRMED |
| 2 | Pro-red: red spells cannot target; red Equipment cannot attach; red creatures cannot block | CR 702.16b (targeting), 702.16d (Equipment unattaches, SBA 704.5n), 702.16f (blocking) | CONFIRMED |
| 3 | Own red sweepers deal no damage to pro-red Alexios | CR 702.16e: damage from sources with the quality is prevented | CONFIRMED |
| 4 | Double strike doubles combat-damage triggers (Sword triggers) | Warren Instigator 2009-10-01: "its triggered ability will thus trigger twice" | CONFIRMED |
| 5 | Thorin cannot target Alexios once Sword of Fire and Ice is attached | Thorin's ETB source is red; CR 702.16b; protection definition (Sword of Truth ruling 2019-06-14). No Thorin ruling on file | CONFIRMED (CR + oracle, no ruling) |
| 6 | Genji Glove: double strike; untap Alexios after the first combat; extra combat | Oracle text (lookup); CR 500.8. No ruling on file. Opponents'-turn reading follows from the oracle | CONFIRMED (oracle); "on opponents' turns" UNVERIFIED (no ruling) |
| 7 | Silent Arbiter + Alexios: Alexios is the only attacker | CR 508.1d example: "No more than one creature can attack each turn ... The only legal attack is for just the creature that 'attacks if able'". No Arbiter ruling on file | CONFIRMED (CR example) |
| 8 | Kediss copy is not combat damage and not commander damage | Kediss 2020-11-10: "isn't combat damage. It isn't tracked with combat damage dealt by commanders and won't cause Kediss's ability to trigger again" | CONFIRMED |
| 9 | Masterwork cannot copy Jitte, Animist or Hammer (legend rule) | CR 704.5j (legend rule), 707.2 (copiable values include supertype). Ruling 2020-08-07: copy enters unattached | CONFIRMED |
| 10 | Mystic Forge cannot cast lands from the top | Ruling 2019-07-12: "you never cast a land card" | CONFIRMED |
| 11 | Hammer of Nazahn attaches each entering Equipment to a creature I control, free | Oracle; ruling 2020-08-07: triggers for each Equipment that enters. The notes say "on my turn" (no such limit in the text, see F-06) | CONFIRMED (wording F-06) |
| 12 | Commander's Plate: protection from W/U/B/G for an R commander; from all five with Sword of Fire and Ice | Ruling 2020-11-10 (Plate, colored commander); Sword rulings | CONFIRMED |
| 13 | Inquisitor's Flail doubles damage dealt by and to the equipped creature; x4 with double strike | Ruling 2011-09-22 (both directions); x4 follows from two damage events each doubled | CONFIRMED |
| 14 | Jeska's Will: both modes while I control any commander | Ruling 2026-03-20: "controlling any commander will satisfy its condition" | CONFIRMED |
| 15 | Tome of Legends gets a page counter when another player controls my commander and it attacks | Ruling 2019-10-04 | CONFIRMED |

Extra checks (not required): Alexios 2024-07-05 (attack costs, owner leaves, controller leaves) CONFIRMED; Argentum Armor 2011-01-01 (may target any permanent; must target own if none other) CONFIRMED; Swiftfoot Boots hexproof relative to controller (Champion's Helm 2011-09-22) CONFIRMED by analogy; Blasphemous Act survival: see F-02 (WRONG as worded).

Verdict D: no WRONG rules claim among the 15. UNVERIFIED: Genji Glove on opponents' turns (no ruling).

## E. Consistency: mana base and curve

| Item | Recomputed | Notes | Result |
|---|---|---|---|
| Lands | 36 = 25 Mountain + 5 colorless + 3 red utility + 3 MDFC | 36 | OK |
| Red land sources | 31 (25 Mountain, Castle Embereth, Sokenzan, The Lonely Mountain, 3 MDFC land faces) | 31 | OK |
| Red sources incl. rocks | 33 (+ Arcane Signet, Fire Diamond) | 33 | OK |
| Colorless-only lands | 5 | 5 | OK |
| Mana rocks / ramp | Sol Ring, Mind Stone, Thought Vessel, Thran Dynamo, Everflowing Chalice, Bauble, Solemn; plus 9 mana artifacts listed | 9 | OK |
| Types (63 nonland) | 36 artifacts (19 Equipment + 17 other incl. 6 artifact creatures), 14 instant/sorcery (7+7), 2 enchantments, 11 non-artifact creatures | 36/14 | OK |
| Average nonland MV | 3.03 (X = 0; Blasphemous Act = 9) | 3.05 | F-10 |
| MV curve | 0:2, 1:7, 2:17, 3:16, 4:11, 5:5, 6+:5 | - | OK |
| RR costs | 10 nonland (Goldspan, Glorybringer, Fury, Dracosaur, Titan, Pyromancer, Confluence, Anger, Comet Storm, Wild Magic Surge) + 2 MDFC fronts (Shatterskull XRR, Pinnacle Monk 3RR) = 12 | 10 | F-11 |
| Single R nonland | 17 (+ Valakut front) | 17 | OK |
| Castability of RR | P(at least 2 red sources by turn 4, 10 cards) = 90.4% (33 sources), 87.9% (31 land sources only) | 90.8% | Castable; F-12 |

Probability checks (hypergeometric, 100 cards): P(2 to 4 lands in 7) = 73.7% (notes 74%); P(0 or 1 land in 7) = 20.7% (notes 20%); P(at least 4 mana sources by turn 4, 45 sources) = 74.6% (notes 75.6%); P(at least 8 lands in 14) = 7.2% (notes 7.6%); P(at least 1 red by turn 2, 8 cards) = 96.5% (notes 96.6%). Differences of 0.4 to 1.0 points: definitional, no verdict effect (F-12).

Verdict E: mana base consistent; red-heavy costs castable with 33 red sources.

## F. Internal consistency

| Check | Result |
|---|---|
| Every nonland card in reference.txt is in the notes' table (a) | 63 / 63 (`notes table minus nonland ref: []`) |
| Every row in the notes' table is in reference.txt | 63 / 63 |
| Land table covers the 11 non-basic lands | Yes (5 colorless, 3 red utility, 3 MDFC) |
| Ranking has exactly the 63 nonland cards | Yes, same order as the table |
| Role counts (table = ranking = notes' claim) | draw 6, ramp 10, equipment-engine 12, protection 4, extra-combat 1, multiplier 2, finisher 6, tutor 4, other 6, interaction 9, wipe 3 = 63 |
| Filler count | 141 unique; 140 found by `lookup`, all legal, all R or colorless, none a Game Changer, none an extra-turn card |
| Filler not in the list | Yes (overlap = []) |
| Filler not a partner of a Spellbook combo with a list card | 0 variants fully inside list + fillers touching a filler |
| Filler name exact | "Vance's Blasting Cannons" does not resolve; exact name is "Vance's Blasting Cannons // Spitfire Bastion" (F-04) |

Verdict F: consistent, one name fix (F-04).

## G. Missed power (inside the official conditions; every card below verified by lookup and Spellbook)

| Candidate (CI, legal, GC) | Text (lookup) | Swap | Reason |
|---|---|---|---|
| Kaldra Compleat ({7}, colorless, legal, GC no) | "Living weapon. Indestructible. Equipped creature gets +5/+5 and has first strike, trample, indestructible, haste..." | For Walking Ballista (rank 62) | With Hammer, it attaches to Alexios for free on entry: a 5-point first-strike, trample, haste, indestructible threat. Indestructible answers destroy wipes and Blasphemous Act style damage. Spellbook: 0 variants with list cards. |
| Batterskull ({5}, colorless, legal, GC no) | "Living weapon... +4/+4 and has vigilance and lifelink. {3}: Return this Equipment to its owner's hand." | For Wayfarer's Bauble (rank 63) or Jhoira's Familiar (rank 61) | Lifelink pays for Ancient Tomb and The One Ring. Hammer re-attaches it for free each recast (8 mana per cycle; a mana sink, not an infinite). Spellbook: 0 variants with list cards. |
| Hellrider ({2}{R}{R}, CI R, legal, GC no) | "Haste. Whenever a creature you control attacks, this creature deals 1 damage to the player or planeswalker it's attacking." | For Light Up the Stage (rank 59) (judgment; adds an RR card) | 1 damage per Alexios attack (4 per round, 8 with Genji Glove) from a hasty body. Spellbook: 0 variants with list cards. |

Not suggested: Hexplate Wallbreaker (red Equipment; cannot equip pro-red Alexios, CR 702.16d); Smuggler's Copter (Crew 1 needs other creatures; Alexios must attack); Coalition Relic (no clear gain over the rocks already in the list).

---

## Findings

| ID | Severity | Card or claim | Evidence | Suggested fix |
|---|---|---|---|---|
| F-01 | MEDIUM | Argentum Armor (rank 25), condition 3 | Oracle: "Whenever equipped creature attacks, destroy target permanent." Ruling 2011-01-01: "You may target any permanent with the triggered ability ... If no other player controls a permanent, you must target one of your own." Not land-specific; the "never target lands" policy is the controller's choice. Up to 8 attacks per round with Glove. | Keep only if the user accepts the judgment and the policy is written as a deck rule. Otherwise swap (Kaldra Compleat or Batterskull, section G). |
| F-02 | MEDIUM | Notes (a) #40, Blasphemous Act: "Alexios survives (pro-red, Hammer, Plate toughness, or counters)" | Pool file: Alexios 4/4 base. With Plate: toughness 7. Blasphemous Act deals 13 to each creature (oracle). Survives only with pro-red (CR 702.16e), indestructible (Hammer, Darksteel Plate), or toughness 14+ (about 10 counters). Plate alone does not save it. | Reword to "(pro-red from Sword of Fire and Ice, indestructible from Hammer or Darksteel Plate, or toughness 14+ from counters)". |
| F-03 | LOW | Notes (h)(3) and (e): "Nothing in the list completes them" | Correct for red identity. Spellbook 1550-4251-6233--78 needs Swiftfoot Boots (in the list) plus Ardenn (W, not buildable). The note omits that Boots is the haste piece. | Add a sentence: Boots is the haste piece of an Ardenn loop; Ardenn is white and cannot be added. |
| F-04 | LOW | Filler "Vance's Blasting Cannons" (draw), notes "all legal, verified by lookup" | `lookup` returns NOT FOUND for the short name; the exact name is "Vance's Blasting Cannons // Spitfire Bastion" (legal, CI R). | Store the full DFC name in `slot-ranking.json` and re-run lookup. |
| F-05 | LOW | Notes (c)(3): "The only red card that targets a creature I control is Thorin" | Lightning Bolt and Galvanic Blast ("any target"), Comet Storm ("any target"), Abrade ("target creature"), Rebel Salvo ("creature or planeswalker"), Chaos Warp ("target permanent"), Fury and Shatterskull ("creatures"). None is restricted to opponents. Thorin is the only one whose text requires targeting a creature I control. | Reword: "Thorin is the only red card whose text requires targeting my own creature." |
| F-06 | LOW | Notes (a) #4 Hammer: "attaches ... for free on my turn" | Oracle: "you may attach that Equipment to target creature you control." No turn restriction. Alexios is mine only on my turn, so the note is true for Alexios only. | Reword: "Hammer attaches every entering Equipment for free; on my turn it can go on Alexios." |
| F-07 | LOW | Notes (a) #11 Sword of the Animist: "up to 4 per round" | Notes (a) #25 and the Glove line give 8 attacks per round with Glove. | "4 per round, 8 with Genji Glove." |
| F-08 | LOW | Notes (a) #47 Wurmcoil Engine: "survives removal" | Oracle: "When this creature dies, create a 3/3 ... and a 3/3 ... token." It dies and leaves two tokens. | "leaves two tokens when it dies." |
| F-09 | LOW | Notes (a) #17 Buster Sword: "cast a spell ... (any type, any turn; damage is large so any mana value)" | Oracle: cast a spell with mana value less than or equal to the damage dealt. Early hits are smaller. | "mana value up to the damage dealt (usually 5+ with Alexios)." |
| F-10 | LOW | Notes: average nonland MV 3.05 | Recomputed 3.03 from lookup costs (X = 0, Blasphemous Act = 9). | Change to 3.03 or state the X convention. |
| F-11 | LOW | Notes: "10 cards need RR" | Shatterskull Smashing ({X}{R}{R}) and Pinnacle Monk ({3}{R}{R}) front faces also need RR: 12. | Change to 12 (or count the MDFC fronts separately). |
| F-12 | LOW | Notes: mana probabilities; MDFC counted as full lands | Recomputed: 4 sources by T4 74.6% (note 75.6%), 8 lands in 14 cards 7.2% (note 7.6%), 2 red by T4 90.4% (note 90.8%), 0-1 lands 20.7% (note 20%). Three MDFC lands counted as full lands. | Note the convention (full or half credit) and the exact sources used. |
| F-13 | LOW | Notes (e): Toralf listed as never-add | Lookup: "Toralf, God of Fury // Toralf, God of Fury ... legal not_legal" (not Commander-legal). The never-add entry is harmless. | Mark it "not Commander-legal". |
| F-14 | LOW | Tooling: `gate.py lookup` | Exit 1 with `UnicodeEncodeError` on Windows cp1252 consoles when a card text has non-cp1252 characters; `PYTHONIOENCODING` is ignored under `-I`. | Run with `python -I -X utf8`; document in the README. |

Counts: BLOCKER 0, HIGH 0, MEDIUM 2, LOW 13.

Open UNVERIFIED items (no finding, no ruling on file): Genji Glove on opponents' turns (logic from oracle, CR 500.8); Godo + Hearth + Boots loop by hand (no engine); Yavimaya Bloomsage identity (not in local bulk); the Spellbook one-card-away count (99 unfiltered vs gate's 97).

---

## Verdict

Verdict: PASS WITH FIXES

Conditions 1 to 5 hold on the evidence above. No BLOCKER. Fix F-01 (decide on Argentum Armor) and F-02 (Blasphemous Act wording) before freezing; the LOW items are documentation.
