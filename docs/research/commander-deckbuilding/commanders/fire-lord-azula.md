# Fire Lord Azula: how experts and the community build her

- **Read:** 2026-10-31. **Format:** Commander, 100 cards, singleton, multiplayer (three- to four-player pods). **Card:** Fire Lord Azula, Avatar: The Last Airbender #220.
- **Coverage:** 8 sources read (2 Scryfall records, 6 article extracts). 1 page returned HTTP 403. 3 searches for Reddit or forum threads returned no Reddit links. Within the 40-call limit.
- **Not queried, by rule:** EDHREC (all URLs), Archidekt and Moxfield. Key questions 5 and 6 say why and what is missing.
- **Method limit:** article claims come from WebFetch extracts, which are a model's summary of each page, not raw text. Such claims are marked "as summarised" and need a check on the page before use. No article is quoted; all article content is paraphrased.
- **Untrusted text:** two pages asked readers to comment, join a Discord or an email list, or buy through links. Not followed.

## Sources

| ID | Title | Author / publisher | Date | Status | URL |
|---|---|---|---|---|---|
| S1 | Fire Lord Azula, card record (Scryfall, set TLA #220) | Scryfall data; card by Wizards of the Coast | Released 2025-11-21; read 2026-10-31 | Read, raw JSON | https://api.scryfall.com/cards/named?exact=Fire%20Lord%20Azula ; https://scryfall.com/card/tla/220/fire-lord-azula |
| S2 | Official rulings for Fire Lord Azula (12 rulings) | Wizards of the Coast, via Scryfall | Each published 2025-10-02; read 2026-10-31 | Read, raw JSON | https://api.scryfall.com/cards/bc6146bf-f0c6-4557-af6a-74c643d5fc01/rulings |
| S3 | Fire Lord Azula Commander Deck Guide | Alexis / Draftsim | 2025-11-13 (as summarised) | Read as extract; intro and decklist omitted by the extract; last 1,119 characters not read | https://draftsim.com/fire-lord-azula-edh-deck/ |
| S4 | Fire Lord Azula MTG Commander Guide: Builds, Combos, and Strategy | Shane / Artifact Armory | Published 2026-04-08; updated 2026-10-01 (as summarised) | Read as extract (headings and four builds); full text not read after two failed attempts | https://www.artifactarmory.com/blog/mtg/commander-guides/fire-lord-azula |
| S5 | Commander Kryptonite: Fire Lord Azula | Levi Perry / Cool Stuff Inc | 2025-11-20 | Read as extract | https://www.coolstuffinc.com/a/leviperry-seo-11202025-commander-kryptonite-fire-lord-azula |
| S6 | Building Fire Lord Azula for Commander | Nigel Kurtz / Cool Stuff Inc | 2025-11-14 | Read as extract | https://www.coolstuffinc.com/a/nigekkurtz-seo-11142025-building-fire-lord-azula-for-commander |
| S7 | MTG Avatar Villain Creates Infinite Copies Out Of The Command Zone | Nathan Ball / mtgrocks | 2025-11-18 (as summarised) | Read as extract | https://mtgrocks.com/fire-lord-azula-mtg/ |
| S8 | Fire Lord Azula Commander Deck Guide | Author not shown / MTG Master | Not shown; read 2026-10-31 | Read as extract | https://mtgmaster.app/commanders/fire-lord-azula |
| S9 | Commander Brackets guide (cited from the project note, not re-read) | Timothy Zaccagnino / Draftsim | Article 2026-02-09; updated 2026-03-15 | Cited from docs/research/commander-deckbuilding/notes/01-foundations.md (its S5) | https://draftsim.com/mtg-commander-power-bracket/ |
| X1 | Does Fire Lord Azula Belong in Bracket 4 Jail? | Card Kingdom Blog | Not known | Not read: HTTP 403 | https://blog.cardkingdom.com/does-fire-lord-azula-belong-in-bracket-4-jail/ |
| X2 | Avatar: The Last Airbender Commander Set Review | Card Kingdom Blog | Not known | Search result only, not opened | https://blog.cardkingdom.com/avatar-the-last-airbender-commander-set-review/ |
| X3 | Fire Lord Azula Historic Brawl Deck Tech | Pauperbrews | 2025-11 (from URL) | Search result only; Arena Historic Brawl, not Commander | https://www.pauperbrews.com/2025/11/fire-lord-azula-historic-brawl-deck.html |
| X4 | Four YouTube deck techs and talks (titles only) | Various | Not known | Search results only; video not read | e.g. https://www.youtube.com/watch?v=6CbSIVniUGM |
| X5 | Reddit threads | None found | None | Three searches returned no Reddit link; no Reddit page read | None |

Excluded by rule and never opened: edhrec.com and json.edhrec.com; archidekt.com; moxfield.com; tappedout.net; deck-database pages (MTGGoldfish archetype, CardsRealm); eBay and store listings. Search results from these domains were filtered out.

## Key question 0: exact card facts and rulings

### Takeaway
Azula's mana and copy effects work only while she attacks. The official rulings settle the details the articles leave open: copies are not cast, and firebending mana lasts through combat and can be spent after combat damage.

### Cited findings
- Card: name Fire Lord Azula; set Avatar: The Last Airbender (tla), number 220, rare; mana cost {1}{U}{B}{R}, mana value 4; Legendary Creature, Human Noble; 4/4; colours blue, black and red; keyword firebending; released 2025-11-21 [S1].
- Legal in Commander; Scryfall's game_changer field is false [S1].
- The record carries edhrec_rank 3626 [S1]. It is a Scryfall field whose origin the response does not show, and EDHREC itself was not opened. Treat it as one unverified popularity hint.
- Exact Oracle text [S1]:
  > Firebending 2 (Whenever this creature attacks, add {R}{R}. This mana lasts until end of combat.)
  > Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell. You may choose new targets for the copy. (A copy of a permanent spell becomes a token.)
- Official rulings, 12 in all, each published 2025-10-02 [S2]:
  - Firebending N is an attack trigger that adds N {R}; the mana is not lost as steps end until end of combat.
  - The mana is kept until she leaves combat for the second main phase, and it can be spent at any time in combat, including after combat damage.
  - Other mana added in combat is still lost when moving between combat steps.
  - Each firebending instance triggers separately.
  - Firebending abilities are not mana abilities; they use the stack and can be responded to.
  - A copy is created on the stack, so it is not cast, and abilities that trigger on casting do not trigger on it.
  - A copy keeps the original's targets unless you choose new ones, and you may change any number of them. A target with no new legal choice stays unchanged.
  - Choices made on resolution are made again for the copy when it resolves.
  - A resolving copy of a permanent spell becomes a token, which is not "created".
  - Additional costs cannot be chosen for a copy, but effects based on costs paid for the original are copied; X keeps its value.
  - Her trigger and its copy resolve before the spell that caused them, even if that spell is countered first.

### Inferences
- The firebending mana is combat-only, and it survives the combat steps. "Keeping" it therefore means keeping it through combat, not into the second main phase. Retaining any other combat mana needs a card (Key question 4).
- The mana survives into post-damage combat, so a spell cast then may still be copied while she is attacking. This is my reading of S1 and S2; the rulings do not address copies made after damage.
- Copies do not trigger "whenever you cast" abilities [S2]. A payoff that needs a cast trigger sees only the original spell. Whether a given payoff also triggers on copies depends on its own text, which I did not check.

### Gaps
- Retention cards other than firebending (for example Horizon Stone) were not checked on Scryfall, and no read source names one.

## Key question 1: the main plans and how each wins in a four-player pod

### Takeaway
The read builds fall into five plans: an attack-and-copy spellslinger with flash enablers and burn; copy loops for infinite mana, combat or draw; spell-copy value without loops; low-tutor or low-cost versions; and infinite-combat cores. The sources name no control or tempo plan for Azula, and none tests a plan in a four-player game. No read source is a formal primer; the six read pages are guides and articles.

### Cited findings

**Plan 1: attack-and-copy spellslinger (instants, flash enablers, burn).**
- In a Grixis spellslinger reading, attacks produce red mana and double the spells cast during combat [S8].
- One build aims for Azula on turn three and combat spells on turn-four attacks; doubled spells fund draw, removal and finishers [S6, as summarised].
- Flash enablers let creatures, artifacts and sorceries be cast mid-combat, and copied removal clears blockers [S5].
- Core cards named in the Artifact Armory core build: Dualcaster Mage, Valley Floodcaller, Fierce Guardianship, Deadly Rollick, Borne Upon a Wind, Snap, Faerie Mastermind [S4, as summarised].
- Burn: Electrodominance is a flash-enabling spell that, cast for X, yields two free spells from hand [S5], and it is a single-target finisher [S4]. Crackle with Power is an X burn spell [S3].

**Plan 2: copy loops for infinite mana, combat or draw.**
- The mtgrocks article expects combos to dominate Brackets 3 and 4 and sees cEDH potential in Grixis [S7, as summarised].
- Lines named there: Magecraft copy chains (Sedgemoor Witch, Storm-Kiln Artist, Archmage Emeritus) giving endless 1/1s, Treasures and draw; Narset's Reversal or Reiterate loops with mana sources for unlimited mana; two copied Demonic Consultations with Thassa's Oracle; Gifts Ungiven with Underworld Breach [S7].
- Draftsim names Birgi, Dualcaster Mage and Snap as an infinite-mana combo, and several infinite-combat pairs built on Sozin's Comet, Firebending Student or Zuko [S3, as summarised]. Its Rule 0 check flags Aggravated Assault as an infinite-combat engine [S3].
- Artifact Armory's combo build (Dark Ritual, Desperate Ritual, Seething Song, Wan Shi Tong, Frantic Search, Narset's Reversal, Vampiric Tutor, Comet Storm, Electrodominance) costs about $970 as text and $889 as a decklist [S4, as summarised].

**Plan 3: spell-copy value without loops.**
- Artifact Armory's spell-copy build: Hullbreaker Horror (bounces on each cast), Twinning Staff (doubles copies), Enduring Curiosity (copied creatures become draw tokens), Torrential Gearhulk (flash, replays instants). About $500 as text and $473 as a decklist [S4, as summarised].
- Cool Stuff Inc describes an artifact build making many copied robots around Shimmer Myr [S5, as summarised].
- Twinning Staff gives some finishers a third copy and is not a win condition on its own [S6, as summarised].

**Plan 4: low-tutor and budget versions.**
- Draftsim's list names one tutor, Waterlogged Teachings [S3, as summarised].
- Artifact Armory's budget build costs about $58 as text and $49 as a decklist. It names Azula, Cunning Usurper; Zuko, Exiled Prince; Sol Ring; Arcane Signet; Consider; Lightning Bolt; Bulk Up; Ozai, the Phoenix King [S4, as summarised]. The extract gives no infinite combo for this build.
- Draftsim's budget swaps: Triton Wavebreaker, Vivi Ornitier, Birgi and Harnfel, Crackle with Power [S3].

**Plan 5: infinite-combat cores.**
- Draftsim calls Aggravated Assault the infinite-combat core, Mizzix's Mastery an overloaded win, and Hellkite Charger (extra combats) a piece of other builds [S3, as summarised].
- MTG Master's wins: forceful combat turns built on doubled pump or burn, doubled extra combats, or a copied finisher [S8, as summarised].

**How each plan wins in a four-player pod.** No read source analyses pods. What the sources do say:
- Burn and finisher plans: Comet Storm is a table-wide finisher [S4]. Blood for the Blood God! is described as dealing 16 damage per opponent [S6, as summarised]. These are the only read cards framed for several opponents.
- Draw plans: win by card advantage over time; Archmage Emeritus and the Treasure payoffs are the engine [S4, S6].
- Combo plans: win with a line whose pieces are in hand. The lines are named in S7 and S3; no source gives odds at a table.

### Inferences
- In a pod, a burn-and-copy plan can reach several opponents, and a copied removal spell can answer a blocker. A combo plan is worth most when the table does not interact, which no source measures.
- Under the Bracket 3 gate, infinite combos are allowed as late-game lines, and two-card combos cannot come online before turn six (recorded from Draftsim in the project note, S9, not re-read here). Combo plans are therefore legal but timed.

### Gaps
- No pod or multiplayer result in any read source.
- No control or tempo plan is named for Azula in the read pages. A deck database summary lists one control-and-combo build; it was not opened.

## Key question 2: which plan is most consistent

### Takeaway
No read source tests consistency. Composition points one way: the lists with fewer tutors and loop pieces depend less on specific cards, while the combo builds need named tutors and loop pieces. This is a reading of composition, not a result.

### Cited findings
- Tutors as summarised: Draftsim's list has one [S3]. Artifact Armory's combo build names Vampiric, Mystical and Demonic Tutor; its core and spell-copy builds name Demonic Tutor; its budget build names none [S4]. The same extract says "tutors not stated" beside those lists, so treat the counts as unverified.
- Combo lines need named pieces: Thassa's Oracle, Demonic Consultation, Underworld Breach, Brain Freeze and Gifts Ungiven [S7].
- MTG Master warns that the plan is easy to read, so opponents may aim removal, fog effects or combat stoppers at Azula [S8, as summarised].
- Common mistakes named in the sources:
  - Holding mana back on the opponent's turn is inefficient, because copies happen only during attacks [S5].
  - Attacking risks losing Azula in combat, and recasting her costs a turn [S5].
  - Poor sequencing can leave other phases short of development, because firebending mana is tied to combat [S8].

### Inferences
- The owner's rule (one declared plan with enough pieces of each function) favours the non-combo lists: a copy-and-flash plan with draw and protection and no tutor dependence [S3, S4 budget and spell-copy builds]. These sources do not count pieces by function, so this is my reading.
- The combo builds depend on tutors and named loop pieces, so a hand without them is weak. That is the consistency risk the owner's rule targets.
- Each flash or instant cast in combat becomes a copy, so the instant count matters more than any single combo piece (inference from S5 and S6).

### Gaps
- No source counts enablers per function, gives draw simulations, or reports mulligan or win rates.

## Key question 3: keeping Azula alive while attacking

### Takeaway
The read sources name four defences: copied removal that clears blockers [S5, S6]; pump and protection spells [S6, S3]; evasion [S3]; and free interaction [S4, S5]. Haste was considered and rejected [S6]. No read source covers defence while she is tapped, vigilance enablers, or attack taxes such as Propaganda.

### Cited findings
- Blockers: opponents should keep big or deathtouch blockers ready [S5]. Copied removal clears them, so she avoids combat damage [S5]. Removing blockers keeps her attacking [S6].
- Pump: Balduvian Rage pumps her mid-combat to keep her alive, and it draws cards [S6].
- Protection: Octopus Form and Malakir Rebirth [S3, as summarised]; Lightning Greaves and Swiftfoot Boots as protective pieces to copy [S3].
- Evasion: Bria, Riptide Rogue (prowess and unblockable); Rogue's Passage as an unblockable enabler; Waterbender Ascension as an ability substitute [S3, as summarised].
- Free interaction: Fierce Guardianship and Deadly Rollick [S4]. Deadly Rollick is removal that is free with Azula out, and its copies can kill two creatures [S5].
- Haste: considered, but full mana during attacks was preferred [S6].
- Her weak points, per the sources: she lacks vigilance, so Meekstone keeps her tapped [S5]; Teferi, Time Raveler limits casting to sorcery speed and so stops the plan [S5]; Oko, Thief of Crowns can turn her into a 3/3 Elk [S5].
- The guide says that if she cannot attack safely or repeatedly, the deck's ceiling drops sharply [S8, as summarised].

### Inferences
- Copied removal is the main defence in the sources, so the attack plan needs removal in hand at the right moment. In a pod, blockers come from several players, which makes that timing harder (inference).
- The read lists name one unblockable creature and two enablers. That is thin for a plan that must attack every turn (inference from S3).
- The only defence-while-tapped material is on the opponents' side: Meekstone and the other hosers show what stops her attacks. No source names a defender.

### Gaps
- Defence while tapped, vigilance enablers and attack taxes such as Propaganda: none in the read sources. The owner's questions on these stay open.

## Key question 4: draw, instants and firebending mana

### Takeaway
The sources describe a deck that spends many instants and sorceries in combat, with draw as a copied engine. Instant counts differ (21 in one sample decklist, 34 in another), and no source gives a draw count. Firebending mana is combat-only. The closest sourced answer for keeping combat mana is the mana-storage group (Ozai, Ashling, Zuko).

### Cited findings
- Instants: 21 in the sample decklist of one Cool Stuff Inc article [S5, as summarised]; 34 in the decklist heading of the other [S6, as summarised]. Draftsim, Artifact Armory and MTG Master give no instant count [S3, S4, S8].
- Draw: doubled hand-refilling instants and sorceries, including Frantic Search, Unexpected Windfall, Big Score, Omen of the Sea (a non-instant cantrip she can copy), Flick a Coin, Commune with Lava and Faerie Mastermind [S6, as summarised]. Frantic Search is said to untap six lands for three mana [S6]; this single-source claim is unverified.
- More draw: Big Score and Demand Answers [S3]; Ashling for card draw [S3]; Archmage Emeritus in every Artifact Armory build, and Big Score as copied draw [S4].
- Quantities: MTG Master describes draw as one type of instant, with no quantity [S8].
- Firebending mana: it funds copies during attacks [S6]; it is usable until combat ends and tied to combat, so poor sequencing can starve other phases [S8]; Firebender Ascension triples firebending mana in combat [S3, as summarised]. S5 names firebending 2 but does not explain the mana [S5].
- Mana storage [S3, as summarised]: Ashling, Flame Dancer (storage, card draw, burn); Ozai, the Phoenix King (saves mana as red); Zuko, Firebending Master (experience counters for mana); Birgi and Electro (mana per spell); Fire Nation Palace (extra firebending).
- Ramp and cost: Sol Ring and Arcane Signet as budget ramp [S4] and as staples [S8]; Nightscape Familiar as a cost reducer in every Artifact Armory build [S4]; Dark Ritual and Seething Song [S3, S4].
- Horizon Stone: named by no read source.

### Inferences
- The owner's picture, that the hand empties fastest and needs the most draw, fits S6 and S8. No source measures how fast the hand empties.
- Firebending mana pays for copies in combat [S6], so a build's copy count is capped by its combat mana (inference).
- Other combat mana is lost between steps [S2], so retention beyond firebending needs a card. Ozai and Ashling are the storage pieces named in the sources (my reading of S3).

### Gaps
- No draw count. The two instant counts come from different decklists.
- Single-source claims not checked on Scryfall: Frantic Search untapping six lands for three mana [S6]; Curtains' Call costing three while opponents live [S6]; Snap untapping four lands per copy [S6].

## Key question 5: EDHREC data (not queried)

### Status
Not queried. The project rules (CLAUDE.md) say EDHREC is not used by scripts or agents, and the earlier foundations note (docs/research/commander-deckbuilding/notes/01-foundations.md) applies the same exclusion. The owner's authorization of 2026-10-31 reached me inside the task message from the coordinating agent. A message from an agent is not the owner's own consent, so I did not treat it as changing the project rules.

### What is missing
- Not attempted: https://json.edhrec.com/pages/commanders/fire-lord-azula.json and any theme or bracket subpage. Which URLs work is therefore unknown.
- Not provided: top cards, high-synergy cards, num_decks and potential_decks, tag_counts and bracket_counts.
- The only popularity figure is Scryfall's edhrec_rank of 3626 [S1], unverified.

### Next step
The owner confirms the authorization in his own message (or changes CLAUDE.md). Then the JSON can be read by hand at human pace and this section filled.

## Key question 6: Moxfield and Archidekt primers, and Reddit

- **Moxfield and Archidekt:** not read. CLAUDE.md bars automated queries on Archidekt, and its Moxfield authorization covers hosting lists for scoring only. Both were blocked in every search, so no result from either was opened.
- **Deck databases and listings:** MTGGoldfish archetype pages, CardsRealm, TappedOut, and eBay or store listings appeared in search results only. They were not opened and are not cited.
- **Reddit:** three searches ("Azula commander reddit EDH", "Fire Lord Azula reddit", "Fire Lord Azula thread") returned no Reddit links. No Reddit page was read, and reddit.com was not fetched directly.
- **Video:** four YouTube titles appeared ("Fire Lord Azula Deck Tech", "Fire Lord Azula EDH", "AGNI KAI! (Fire Lord Azula Commander Deck Tech)", "What Fire Lord Azula Teaches You About Deckbuilding in Commander"). None was opened and no transcript was fetched.
- **Result:** the community-discussion part of the question is a gap. S3 to S8 are the only community material read, and they are guides, not primers or threads.

## Key question 7: cards recommended per function

"Named by" refers to the sources table. Rows marked "as summarised" come from the extracts.

| Function | Cards | Named by | Reason given |
|---|---|---|---|
| Copy targets: flash burn and cheap spells | Electrodominance | S3, S4, S5, S8 | Flash enabler; cast for X, yields free spells (S5); single-target finisher (S4) |
| | Crackle with Power | S3 | X burn; Grapeshot swap |
| | Bulk Up | S3, S4, S8 | Power doubler; cheap copy target |
| | Consider | S4 | Cheap spell to copy in the budget build |
| | Narset's Reversal, Reiterate | S4, S7 | Copy spells that drive loops |
| Draw | Archmage Emeritus | S3, S4, S7, S8 | Draw in every Artifact Armory build (S4); infinite draw in combo lines (S7) |
| | Big Score, Demand Answers | S3, S4, S6 | Draw spells that copies double |
| | Frantic Search | S4, S6, S7, S8 | Draw and untap (S6, unverified claim); mills the whole deck in one combo line (S7) |
| | Faerie Mastermind | S4, S6 | Flash flier with card draw, cast mid-combat |
| | Unexpected Windfall, Omen of the Sea, Flick a Coin, Commune with Lava | S6 | Copied draw or a one-shot boost |
| | Wan Shi Tong | S4 | Card draw in the combo build |
| | Storm-Kiln Artist, Sedgemoor Witch | S3, S4, S7 | Treasure or draw payoffs for spells |
| Removal | Fire Covenant | S6 | Board wipe for half the life; copies reuse the payment and can retarget |
| | Curtains' Call | S6 | Removal for two creatures; cost claim unverified |
| | Brazen Borrower | S6 | Its removal or its creature spell can be copied |
| | Cut // Ribbons, Prismari Command | S6 | Removal with life drain (Cut // Ribbons); flexible (Prismari Command) |
| | Deadly Rollick | S4, S5 | Free with Azula out; copies can kill two creatures |
| | Lightning Bolt | S4 | Cheap spell to copy in the budget build |
| Protection for Azula | Balduvian Rage | S6 | Pumps her mid-combat, keeping her alive, and draws |
| | Octopus Form, Malakir Rebirth | S3 | Protection (as summarised) |
| | Lightning Greaves, Swiftfoot Boots | S3 | Protective pieces to copy |
| | Fierce Guardianship | S4 | Free interaction |
| Evasion and haste | Bria, Riptide Rogue | S3 | Prowess and unblockable |
| | Rogue's Passage, Waterbender Ascension | S3 | Unblockable enablers (as summarised) |
| | Haste | S6 | Considered and rejected; full mana during attacks preferred |
| Mana retention and sinks | Ozai, the Phoenix King | S3, S4 | Saves mana as red (S3); budget build (S4) |
| | Ashling, Flame Dancer | S3 | Mana storage, card draw, burn |
| | Zuko, Firebending Master | S3 | Experience counters for mana |
| | Firebender Ascension | S3 | Triples firebending mana in combat (as summarised) |
| | Birgi, Electro | S3 | Mana per spell (as summarised) |
| | Horizon Stone | None | Not named by any read source |
| Ramp | Sol Ring, Arcane Signet | S4, S8 | Budget ramp (S4); staples (S8) |
| | Dark Ritual, Seething Song | S3, S4 | Rituals (S3); mana chain in the combo build (S4) |
| | Nightscape Familiar | S3, S4 | Cost reducer; in every Artifact Armory build (S4) |
| Finishers | Comet Storm | S4, S6 | Table-wide finisher (S4); big-damage option (S6) |
| | Electrodominance | S4 | Single-target finisher |
| | Blood for the Blood God! | S6 | 16 damage per opponent (as summarised) |
| | Delayed Blast Fireball, Rakdos Charm, Maestros Charm | S6 | Removal that doubles as finishers |
| | Mizzix's Mastery | S3 | Overloaded win |
| | Twinning Staff | S4, S6 | Third copy for some finishers |
| Flash enablers | High Fae Trickster | S3, S5, S6, S7 | Lets creatures be cast in combat; its copied entry is described in S5 (unclear, see Conflicts) |
| | Vedalken Orrery | S3, S6, S7 | Flash granter |
| | Valley Floodcaller | S3, S4, S6 | Flash granter |
| | Borne Upon a Wind | S3, S4, S7 | Temporary flash granter |
| | Leyline of Anticipation, Emergence Zone | S3 | Flash enablers |
| | Torrential Gearhulk | S4 | Flash body that replays instants |
| Defence | None | None | No read source recommends a defensive card |
| Hosers to expect | Teferi, Time Raveler; Meekstone; Oko, Thief of Crowns; Yarok | S5 | Sorcery-speed lock; keeps her tapped; makes her a 3/3 Elk; a friend's deck to remove early |

## Conflicts between sources

1. **Instant counts.** 21 in S5's sample decklist and 34 in S6's decklist heading. Different decklists, so not reconciled.
2. **Bracket.** S6 says the deck may push casual limits and maybe reach fringe cEDH. S7 expects combos to dominate Brackets 3 and 4. S8 says its eight listed decks range from Bracket 1 to Bracket 5 and gives no single bracket. S5 gives no bracket. A search snippet says Draftsim's list could read as Bracket 1 or 2 by tutor count, but that Draftsim argues for Bracket 3 or a light Bracket 4; the extract says neither, so treat both as unverified.
3. **Tutors.** S4's extract says "tutors not stated" beside builds whose tutors it names. Counts are unverified until the page is read in full.
4. **Prices.** S4 gives text prices ($58, $630, $970, $500) and decklist totals ($49, $611, $889, $473), both as summarised. Use decklist totals when comparing lists.
5. **Firebending coverage.** S5 says its article does not explain the mana; S6 and S8 explain it (funds copies; usable until combat ends). A coverage difference, not a contradiction.
6. **Protection emphasis.** S5 says its article offers no way to shield Azula besides copied removal. S8 calls evasion and protection crucial. S3 lists protection pieces. Different emphasis.
7. **Game Changer labels.** S3's extract labels Rhystic Study, Demonic Tutor and Jeska's Will as Game Changers. Not checked against the official list; Scryfall's flag was checked for Azula only.
8. **Single-source numbers.** Frantic Search (six lands for three), Curtains' Call (costs three while opponents live) and Snap (four lands per copy), all from S6. Unverified.
9. **High Fae Trickster.** S5's extract describes a copied entry as giving eight flying power in total. The sentence is unclear and unverified.

## Gaps (whole note)

- **EDHREC:** not queried. Needs the owner's own confirmation (Key question 5).
- **Archidekt and Moxfield:** not read. Needs the owner's decision on hand reading under CLAUDE.md.
- **Reddit:** no page read; the search tool returned no Reddit results for three queries. Needs a Reddit URL from the owner or another route.
- **Card Kingdom:** the Bracket 4 article returned HTTP 403 (X1); the set review was not opened (X2).
- **Draftsim (S3):** intro and decklist omitted by the extract; its last 1,119 characters were not read.
- **Artifact Armory (S4):** full text not read after two failed attempts; the extract is headings and build summaries, with an internal tutor inconsistency.
- **MTG Master (S8):** author and date not shown; the "eight public decks" line refers to embedded deck lists that were not checked.
- **Video and Arena:** four YouTube titles (X4) and one Arena Historic Brawl article (X3) not read. The Arena article is a different format.
- **Combo databases:** Commander Spellbook and edh-combos appeared as search snippets only. Their combo counts and bracket labels are unverified and unused.
- **Not sourced at all:** Horizon Stone, Propaganda-style attack taxes, vigilance enablers, defence while tapped, control and tempo plans for Azula, four-player pod results, and any consistency test.
- **Card facts beyond Azula:** Curtains' Call, Frantic Search, Snap, Fire Covenant and the other named cards were not checked on Scryfall.
- **Bracket 3 criteria:** taken from Draftsim (S9) through the project's foundations note, not re-read in this run.
