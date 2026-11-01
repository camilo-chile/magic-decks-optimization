# Commander archetypes: EDHREC and expert sources

Read 2026-10-31. Scope: the ten archetypes in the assignment. Access: the project CLAUDE.md, "Sites and their terms" (owner decision 2026-10-31). EDHREC pages and articles were read with WebFetch; requests were spaced by turn, not by a timer. The EDHREC theme JSON was requested with curl and answered HTTP 403 (B1); it was not retried and no block was bypassed. Search snippets are listed for orientation and are never used as evidence. Figures come from the cited page through a summarising fetch: they were checked against totals the page prints, mismatches are in Conflicts, and a figure used in a deck decision should be spot-checked on the page. "Derived" marks a total or average I computed from a page's labels.

## Sources

| ID | Source | Author | Date | URL | Status |
|---|---|---|---|---|---|
| S1 | "The Top 10 Most Played Landfall Cards in Commander" (EDHREC) | Nick Price | July 14, 2025 | https://edhrec.com/articles/the-top-10-most-played-landfall-cards-in-commander | read 2026-10-31 |
| S2 | EDHREC theme page "Landfall" | EDHREC | undated | https://edhrec.com/themes/landfall | read 2026-10-31 |
| S3 | EDHREC average deck: Ramses, Assassin Lord (Assassins) | EDHREC | undated | https://edhrec.com/average-decks/ramses-assassin-lord/assassins | read 2026-10-31 |
| S4 | EDHREC average deck: Commodore Guff (Pillow Fort) | EDHREC | undated | https://edhrec.com/average-decks/commodore-guff/pillow-fort | read 2026-10-31 |
| S5 | EDHREC average deck: Aesi, Tyrant of Gyre Strait (Landfall) | EDHREC | undated | https://edhrec.com/average-decks/aesi-tyrant-of-gyre-strait/landfall | read 2026-10-31 |
| S6 | "EDHREC guide to +1/+1 counters in Commander" | Cooper Gottfried | May 4, 2026 | https://edhrec.com/articles/edhrec-guide-to-1-1-counters-in-commander | read 2026-10-31 |
| S7 | "EDHREC guide to Spellslinger in Commander" | Nick Price | April 8, 2026 | https://edhrec.com/articles/edhrec-guide-to-spellslinger-in-commander/ | read 2026-10-31 |
| S8 | "EDHREC guide to Reanimator in Commander" | Mike Carrozza | April 21, 2026 | https://edhrec.com/articles/edhrec-guide-to-reanimator-in-commander | read 2026-10-31 |
| S9 | "Deep analysis: Blink" (EDHREC) | Bernardo Melibeu | June 22, 2021 | https://edhrec.com/articles/deep-analysis-blink | read 2026-10-31 |
| S10 | "Tokens in Commander" (EDHREC guide) | Cooper Gottfried | February 23, 2026 | https://edhrec.com/articles/edhrec-guide-to-tokens-in-commander | read 2026-10-31 |
| S11 | "Aristocrats in Commander" (EDHREC guide) | Cooper Gottfried | October 27, 2025 | https://edhrec.com/articles/edhrec-guide-to-aristocrats-in-commander | read 2026-10-31 |
| S12 | "How Does MTG Voltron Work" (CoolStuffInc) | Christopher Lai | August 19, 2026 | https://www.coolstuffinc.com/a/how-does-mtg-voltron-work-08192026 | read 2026-10-31 |
| S13 | Pillow Fort strategy breakdown (CoolStuffInc) | Jason Dookeran | March 30, 2026 | https://www.coolstuffinc.com/a/jasondookeran-seo-03302026-what-is-mtg-pillow-fort-strategy-breakdown-best-cards | read 2026-10-31 |
| S14 | EDHREC theme page "Assassins" | EDHREC | undated | https://edhrec.com/themes/assassins | read 2026-10-31 |

Blocked or unusable:

| ID | Target | Result |
|---|---|---|
| B1 | https://json.edhrec.com/pages/themes/<theme>.json for landfall, plus-1-plus-1-counters, spellslinger, assassins, voltron, tokens, pillowfort, reanimator, blink, aristocrats, aggro, tribal | HTTP 403 AccessDenied on all twelve (curl, 2026-10-31, 3-second pause, not retried) |
| B2 | Geeky Domain, landfall guide (https://geekydomain.com/blogs/guides/landfall-how-the-engine-works-in-commander) | HTTP 402 Payment Required |
| B3 | https://edhrec.com/articles/edhrec-guide-to-landfall-in-commander (guessed slug) | HTTP 404 |
| B4 | Krakenthemeta, best Voltron commanders, 2026 (https://krakenthemeta.com/blog/best-voltron-commanders/) | Fetch failed twice (response over the output-size limit) |
| B5 | Card Kingdom, "Commander Archetype Inspection: Go Wide" (https://blog.cardkingdom.com/?p=28915) | HTTP 403 |
| B6 | https://edhrecstatic.com/average-decks/commodore-guff/core/pillow-fort | HTTP 525; the edhrec.com copy (S4) was read instead |

Search snippets only (not opened, not evidence):

| ID | Source | Snippet claim |
|---|---|---|
| N1 | Krakenthemeta go-wide page (search result https://krakenthemeta.com/blog/?p=1274; attribution unconfirmed) | 10 to 15 token producers, 2 or 3 payoffs, 1 or 2 doublers |
| N2 | Gamertagmythras, token generators (https://gamertagmythras.com/blog/magic-the-gathering/best-mtg-token-generators-commander) | About a third of a balanced list is generators |
| N3 | Geeky Domain, landfall (the B2 page) | Ramp without landfall payoffs is sluggish; Ramunap Excavator can reuse Evolving Wilds from the graveyard |
| N4 | EDHREC article "Mechanically Minded - Landfall" (https://edhrec.com/articles/?p=30278) | A commander lets you play lands from the graveyard; a "land dump" category |
| N5 | MTGRocks, best reanimator commanders (https://mtgrocks.com/best-mtg-reanimator-commanders/) | Muldrotha is the strongest reanimator option |
| N6 | edh-match, aristocrats (https://edh-match.vercel.app/strategies/aristocrats) | Six to eight free sacrifice outlets |
| N7 | MTGGoldfish and Deckcheck Ezio and Altair lists (https://www.mtggoldfish.com/deck/7748372 and Deckcheck pages) | Five colours for the main win; combat-damage routes; exposed to sweepers and land hate |

### Sample lists read

These are the sources' own sample lists, not population statistics. Creatures exclude the commander, except the reanimator row, where the article's 55 creatures include it.

| Sample list | Source | Creatures | Instants | Sorceries | Artifacts | Enchantments | Planeswalkers | Lands | Commander | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| Landfall, Aesi average deck | S5 | 28 | 10 | 10 | 4 | 7 | 1 | 39 | 1 | 100 (derived) |
| Assassins, Ramses average deck | S3 | 26 | 10 | 7 | 14 | 8 | 1 | 33 | 1 | 100 (derived) |
| Pillow Fort, Commodore Guff average deck | S4 | 13 | 7 | 5 | 12 | 6 | 20 (verify) | 36 | 1 | 100 (derived) |
| Counters, Cleopatra guide list | S6 | 34 | 9 | 9 | 7 | 6 | 1 | 34 | 1 | 101 (see Conflicts) |
| Spellslinger, Balmor guide list | S7 | 20 | 19 | 19 | 3 | 3 | 1 | 34 | 1 | 100 (derived) |
| Tokens, Rin and Seri guide list | S10 | 31 | 7 | 7 | 8 | 10 | 1 | 35 | 1 | 100 (derived) |
| Aristocrats, Zahur guide list | S11 | 33 | 9 | 7 | 7 | 7 | 1 | 35 | 1 | 100 (derived) |
| Reanimator, The Master guide list | S8 | 54 | none listed | none listed | 6 | 2 | 1 | 36 | 1 | 100 (derived) |
| Blink, Roon list (2021) | S9 | 40 | 9 | 6 | 5 | 2 | none listed | 36 | 1 | 99 (see Conflicts) |

Average land count of the eight non-landfall lists: 34.9 (derived). Landfall: 39, the highest of the nine.

## 1. Landfall / lands matter

**Takeaway.** The landfall sources give deck counts for ten cards (S1), a theme page with names only (S2) and one average deck with 39 lands (S5). No read source states a ramp count, a land-making count or land drops per turn. The owner's "absurd ramp" lesson is partly supported; the "several lands per turn" part is untested.

**Packages.**
- Average deck (S5): 39 lands (derived 17 nonbasic, 22 basic), 28 creatures, 10 instants, 10 sorceries, 7 enchantments, 4 artifacts, 1 planeswalker. The page shows 1,078 filtered decks and no card inclusion numbers.
- Ramp: S1 maps ramp onto two of its ten cards (Aesi, Lotus Cobra), using the fetch summary's labels, not the article's own.
- Theme page (S2), names only, in EDHREC's order. Top cards: Tatyova, Benthic Druid; Scute Swarm; Felidar Retreat; Omnath, Locus of Rage; Lotus Cobra; Swords to Plowshares; The Gitrog Monster; Rampaging Baloths; Tireless Provisioner; Path to Exile. Sorceries I classed by name (not checked against card text): Cultivate, Nature's Lore, Rampant Growth, Farseek, Kodama's Reach, Explore, Three Visits. Mana artifacts: Sol Ring, Arcane Signet, Chromatic Lantern, Simic Signet, Thought Vessel. Utility lands include Bojuka Bog, Reliquary Tower, Field of the Dead, Boseiju, Who Endures, Eumidian Hatchery and Lotus Field. Creatures include Ramunap Excavator and Azusa, Lost but Seeking.

**Most-played cards (S1; deck counts; no data date or method given).**

| Rank | Card | Decks |
|---|---|---|
| 1 | Tireless Provisioner | 321,782 |
| 2 | Scute Swarm | 284,539 |
| 3 | Avenger of Zendikar | 260,260 |
| 4 | Lotus Cobra | 213,016 |
| 5 | Rampaging Baloths | 202,424 |
| 6 | Felidar Retreat | 188,744 |
| 7 | Tatyova, Benthic Druid | 178,152 (6,228 as commander) |
| 8 | Evolution Sage | 182,988 |
| 9 | Tireless Tracker | 141,769 |
| 10 | Aesi, Tyrant of Gyre Strait | 92,622 (10,523 as commander) |

Highest-synergy cards by function: not obtained (B1).

**Expert view and the four-player pod.** S1 says the large landfall payoffs compete for the same role: Rampaging Baloths faces Omnath, Locus of Rage and Phylath, World Sculptor. No read source addresses pods.

**Weakness and fix.** Payoff competition (S1); no fix stated. N3 (snippet) says ramp without landfall payoffs is sluggish; unverified, no fix stated.

**Traps (S1).** Tireless Tracker costs two mana per card drawn and looks poor until spare landfall mana covers it. Avenger of Zendikar's tokens arrive on entry, so landfall adds nothing to them, and its combo needs three or more lands in play and no earlier tokens. Evolution Sage needs cards that grow from its triggers. Honorable mentions may not fit a landfall-focused list.

**Owner's lessons.** "Absurd ramp": partly supported by the 39-land sample; ramp counts unknown. "Ways to make lands enter again and again": untested. N3 and N4 point to graveyard land play (snippets only).

**Cross-link.** Toph, the First Metalbender appears in S2's "Top Commanders" list (order only, no figure). Toph is one of the owner's projects.

## 2. +1/+1 counters

**Takeaway.** The EDHREC guide (S6) supports the doubler lesson: it names three doublers and a set of counter sources and payoffs. It does not name counters-on-attack as a mechanic. It targets Bracket 2.

**Packages (S6, Cleopatra list; total see Conflicts).** Creatures 34, instants 9, sorceries 9, artifacts 7, enchantments 6, planeswalkers 1, lands 34 (16 nonbasic, 11 Forest, 7 Swamp).
- Counter sources named (12): Felidar Retreat, Managorger Hydra, Inti, Bristly Bill, Emissary Green, Forgotten Ancient, Atomize, Innkeeper's Talent, Generous Pup, Essence Capture, Chevill, Cleopatra.
- Doublers: Deepglow Skate (blue), Loading Zone (green), Innkeeper's Talent (eventually doubles; no figure). The Earth Crystal raises counters placed on creatures (fetch summary).
- Payoff roles: card draw (Exemplar of Light, Terrasymbiosis, Chevill, Cleopatra); mana (Incubation Druid, Rishkar, Kami of Whispered Hopes); damage (Caldera Pyremaw, The Red Terror); protection (Together Forever, Innkeeper's Talent); evasion (Herald of Secret Streams); finishers (Vraska, Betrayal's Sting, through proliferate); a selective sweeper (Wave Goodbye).
- Per-role counts: not stated.

**EDHREC data.** None by count (B1).

**Expert view.** The guide ranks the colours: green best (turns counters into mana, makes many, draws, has a doubler); white strong (spreads counters, card advantage, protection); blue has a doubler and payoffs but makes counters less easily; red has good synergies; black ranks last (S6). No pod statement.

**Weakness and fix.** Too few counters from one source: Cleopatra spreads one counter across two creatures a turn, which the guide calls too little (S6). Fix: more counter sources and doublers. Expensive legends need ramp (S6).

**Traps (S6).** Cleopatra as the only counter engine; Essence Capture, which the guide calls weaker than Counterspell; black, the weakest colour for counters.

**Owner's lessons.** Doublers: supported (S6). Counters on attack: not a named mechanic; the nearest idea is a heavily countered creature winning in a few attacks, with no count (S6). Partly supported.

## 3. Spellslinger (instants and sorceries)

**Takeaway.** S7 gives a role list and a sample with 38 instants and sorceries out of 100. It says to keep one main plan with one or two side packages, and that some payoffs count only certain spell types, so each card's text must be read. It targets Bracket 2.

**Packages (S7, Balmor list).** Creatures 20, instants 19, sorceries 19, artifacts 3, enchantments 3, planeswalkers 1, lands 34 (9 Island and 8 Mountain named; 17 others derived), commander 1.
- Payoffs: Third Path Iconoclast, Case of the Ransacked Lab, Grapeshot, Guttersnipe, Shark Typhoon.
- Enablers: Goblin Electromancer, Artist's Talent, Sorcerer Class.
- Cheap spells: Opt, Ponder, Brainstorm.
- Card draw: Treasure Cruise, Mystical Tutor, Solve the Equation.
- Interaction: Counterspell, Lightning Bolt, Abrade, Izzet Charm, Pongify.
- Protection: Rite of the Dragoncaller, Shark Typhoon.
- Mana: Farseek, Dark Ritual, Mana Geyser, Pinnacle Monk, Silundi Vision.
- Finishers: Mizzix's Mastery, Jeskai Ascendancy, Thousand-Year Storm.
- Per-role counts: not stated. The guide also claims Izzet has more payoffs and enablers than any other two-colour pair (S7; not counted).

**EDHREC data.** None by count (B1).

**Expert view.** The main risk is a stalled board: when it stalls or tokens run thin, attacks stop paying, which is why the guide includes non-combat damage (S7). No pod statement.

**Weakness and fix.** Payoffs that count every noncreature spell, and spells that do not help (S7). Fix: read each card's text (S7).

**Traps (S7).** Dark Ritual and Mana Geyser are short-lived mana for same-turn combo. Cyclonic Rift is an option only if one accepts Game Changers. Tutors depend on the bracket. Sol Ring, Arcane Signet and Talisman of Creativity appear in the list with no stated role.

**Owner's lessons.** "Needs the most draw": draw is a named role, with no count or comparison (S7); untested. "Empties its hand fastest": not stated. "Keeps temporary mana": the guide treats temporary mana as same-turn use, not something to hold (S7); not supported as written.

## 4. Typal combat, Assassins as the example

**Takeaway.** Two Assassins sources were read: an average deck (S3) and the theme page (S14). Neither has text about creature fragility or evasion, so the owner's lesson on fragile creatures and one evasion keyword is untested. The average Assassins deck has 26 creatures outside the commander, fewer than six of the other eight sample lists.

**Packages (S3, Ramses average deck, blue-black).** Creatures 26, instants 10, sorceries 7, artifacts 14, enchantments 8, planeswalkers 1, lands 33 (15 nonbasic, 8 Island, 10 Swamp), commander 1. Derived: 40 non-creature, non-land spells. The page shows 195 decks with the assassins tag, no date, one copy per card and no inclusion numbers.

**Theme page (S14).**
- Commanders by deck count: Ezio Auditore da Firenze 1.82K; Altaïr Ibn-La'Ahad 551; Etrata, Deadly Fugitive 339; Ramses, Assassin Lord 195; Edward Kenway 177; Ezio, Blade of Vengeance 82; Evie and Jacob Frye 81; Queen Marchesa 76; Etrata, the Silencer 48.
- Top cards, EDHREC order, no figures: Bayek of Siwa; Aya of Alexandria; Arno Dorian; Basim Ibn Ishaq; Ezio, Blade of Vengeance; Desmond Miles.
- Creatures (order): Mari, the Killing Quill; Lydia Frye; Olivia, Opulent Outlaw; Altaïr Ibn-La'Ahad; Royal Assassin.
- Instants (order): Assassin's Trophy; Path to Exile; Swords to Plowshares; Chain Assassination; Desynchronization; Mortify.
- Cross-link: Ezio Auditore da Firenze is the top Assassins commander by deck count here. The owner's Phase 2 Ezio deck uses it as a proxy commander.

**Expert view and pod.** None read. N7 (unopened snippets) says the five-colour Ezio list is exposed to land hate and sweepers, and that Ramses offers a second win route.

**Weakness, fix and traps.** None sourced.

**Owner's lesson.** Untested. The only observation is the low creature count (26), which is not a test of fragility.

## 5. Aggro / go-wide tokens

**Takeaway.** S10 names the win routes: wide boards, anthems once the count is high, finishers, monarchy drain, sacrifice and early pressure. It gives no counts for token makers, payoffs, anthems or outlets. The two snippet ratios disagree (N1, N2).

**Packages (S10, Rin and Seri list).** Creatures 31, instants 7, sorceries 7, artifacts 8, enchantments 10, planeswalkers 1, lands 35 (19 nonbasic, 16 basic: 6 Forest, 6 Plains, 4 Mountain), commander 1.
- Token makers: Generous Gift, An Offer You Can't Refuse, Bitterblossom, Clone Legion, Ocelot Pride, Ainok Strike Leader, Rin and Seri.
- Payoffs: Battle Hymn, Stadium Headliner, Worldwalker Helm.
- Anthems: Skyhunter Strike Force, Jazal Goldmane, Prava of the Steel Legion.
- Doublers: Anointed Procession, Ocelot Pride, Doubling Season, Second Harvest, Elspeth, Storm Slayer, Parallel Lives.
- Sacrifice: Blood Artist, Anhelo. Protection: Prowling Serpopard; Ainok Strike Leader against sweepers. Removal: Elspeth, Feline Sovereign, Qasali Slingers. Ramp: Jaheira, Enduring Vitality, Mutable Explorer. Draw: Caretaker's Talent.
- Per-role counts: not stated.

**EDHREC data.** None by count (B1).

**Snippet conflict.** N1 says 10 to 15 producers, 2 or 3 payoffs and 1 or 2 doublers. N2 says about a third of a balanced list is generators, around 33 cards. Both cannot hold. Both unverified.

**Expert view and pod.** Monarchy drain through Court of Embereth can last a full round, which the guide calls a fair shot, not a sure thing (S10). Board wipes are the main danger (S10). No pod statement, though the monarchy is a table-level effect.

**Weakness and fix.** Board wipes: Ainok Strike Leader (S10). Blue counterspells: Prowling Serpopard (S10). Board-dependent payoffs: Jazal Goldmane is useful with about five creatures out and can be lethal at ten or more; Battle Hymn and Stadium Headliner need a token-filled board; Blood Artist needs fodder (S10).

**Traps.** The same board dependence; Rin and Seri's damage and life gain scale with the Cat and Dog counts (S10).

**Owner's lessons.** None given for tokens. The guide says doublers make twice the usual tokens and calls them strong (S10).

## 6. Voltron

**Takeaway.** S12 is the only voltron source read. It says protecting the one creature matters as much as growing it, and it names protection, evasion and ways past blockers, and equipment and aura payoffs. No counts. The 2026 Krakenthemeta guide (B4) and the EDHREC voltron theme were not reached.

**Packages (S12, names only, the article's labels).**
- Protection: Champion's Helm, Commander's Plate, Mithril Coat, Swiftfoot Boots, Mask of Law and Grace, Timely Ward.
- Evasion and ways past blockers: Shadowspear, Trailblazer's Boots, Spirit Mantle, Whispersilk Cloak, Brotherhood Regalia, Power Fist, Loxodon Warhammer, Embercleave.
- Equipment payoffs: Excalibur, Sword of Eden; Kaldra Compleat; Sword of Fire and Ice; Umezawa's Jitte. Aura payoffs: Ethereal Armor, Daybreak Coronet.
- Power: Blackblade Reforged, All That Glitters, Ancestral Mask, Colossus Hammer, The Spear of Leonidas, Two-Handed Axe, Buster Sword.
- Tutors: Cloud, Midgar Mercenary; Light-Paws, Emperor's Voice.
- Ramp and card draw: not stated. Counts: none.
- Commander damage: the example is an 11-power creature whose damage doubles to 22 in one hit, which the guide says ends the game. The threshold is not stated.

**EDHREC data.** None (not reached).

**Expert view and pod.** Stacking everything on one creature makes it harder to remove; protecting the commander deserves as much planning as growing it; a threat removed before combat ruins the plan even with evasion; a 1/1 token can absorb a 25-power hit (S12). No pod statement.

**Weakness and fix.** Fragile single threat, commander removal and chump blockers (S12). The fix named is protection and evasion (S12). Sweepers and tapped-out defence are not covered.

**Traps (S12).** Everything on one creature; small creatures or tokens that absorb big attacks.

**Owner's lessons.** Protection, evasion and ways past bigger creatures: supported as roles (S12). Haste, team evasion against wide chump-block boards, and vigilance or defence while tapped: not in S12; untested.

## 7. Pillow fort and defensive packages for attacking decks

**Takeaway.** S13 and the average deck (S4) describe a defence that taxes, punishes or fogs attacks, and then wins through a finisher, a token engine or a combo. S13 counts table politics as part of the plan. The S4 planeswalker count needs checking before use.

**Packages (S4, Commodore Guff average deck; the tag shows 72 decks).** Creatures 13, instants 7, sorceries 5, artifacts 12, enchantments 6, planeswalkers 20 (as read; implausible, verify), lands 36 (22 nonbasic, 14 basic: 6 Island, 3 Mountain, 5 Plains), commander 1. No inclusion numbers.

**Roles (S13, names only).**
- Attack taxes: Sphere of Safety, Ghostly Prison, Windborn Muse, Propaganda. Land Tax appears only as a picture.
- Punishing attacks: No Mercy, Lightmine Field, Blazing Archon, Crawlspace.
- Goad: Coronation of Chaos, Disrupt Decorum, Geode Rager, Marisi, Breaker of the Coil, Kardur, Doomscourge.
- Fog and prevention: Fog, Spike Weaver; Eternal Witness returns fog pieces.
- Defence: Kros, Defense Contractor; Pramikon, Sky Rampart.
- Enchantress support: Authority of the Consuls, Blind Obedience, Collective Restraint, Solitary Confinement.
- Win routes: Darksteel Reactor, Helix Pinnacle, Azor's Elocutors, Luminarch Ascension, Castle Ardenvale, Assemble the Legion, Court of Grace, Felidar Sovereign, Palinchron with Deadeye Navigator, Intruder Alarm.
- Numbers (S13): Crawlspace caps attackers at two per turn; Blazing Archon allows no attacks while in play; Goad forces at least one attacker; Oloro gains two life a turn. Counts of taxes or fogs are not stated.

**EDHREC data.** The theme page was not read (see Gaps).

**Expert view and pod.** The guide says the deck wins over the other players, which buys time, and that it can point opponents at each other before dealing with the last player (S13). It also notes that taxes do not stop opponents who can pay (S13).

**Weakness and fix.** Go-wide aggro (Winota and Caesar make it likelier); board wipes that hit an enchantment board (Cyclonic Rift, Austere Command, Bane of Progress); haste gets around goad, and only Kardur handles it (S13). Fix: name a finisher route (S13).

**Traps (S13).** Blazing Archon's lock ends once removal arrives, and it is costly. Replenish is expensive. Crawlspace does not stop Voltron-style commanders.

**Owner's lessons.** Attack taxes: supported (S13). Defence while tapped: fog, goad and punishing effects are named; vigilance and team evasion are not stated.

## 8. Graveyard / reanimator

**Takeaway.** S8 defines reanimator as the creature-based subset of graveyard decks and names three effect types that need balance: graveyard stocking, reanimation tools and targets. Its sample has 54 creatures plus the commander, 36 lands, 6 artifacts, 2 enchantments and 1 planeswalker (derived total 100).

**Packages (S8).**
- Graveyard stocking: self-mill or discard, looting-style draw (Likeness Looter, Greater Good), surveil, and Blood tokens, which the guide rates highly.
- Reanimation tools: Reanimate, Animate Dead, Breach the Multiverse, Necromancy; Karmic Guide and Doomed Necromancer work this way; graveyard tutors Buried Alive and Entomb.
- Targets: Ashen Rider, Archon of Cruelty, Sheoldred, Whispering One.
- Enablers: not a stated category. A sacrifice build with Shirei, Shizo's Caretaker is mentioned.
- Per-role counts: not stated.
- Top three EDHREC reanimator commanders, as the article gives them: Teval, Meren, Terra. The article classes Muldrotha and Osgir as graveyard-deck commanders, not reanimator leaders. Its sample commander, The Master, Transcendent, is not assessed as a leader.

**EDHREC data.** The three commanders above; no card counts.

**Expert view and pod.** This is the only read source with table-social claims: the reanimator becomes the table's focus, opponents may resent reanimating their cards, many options slow the game, and solo practice is advised (S8). No four-player analysis.

**Weakness and fix.** Graveyard hate: Rest in Peace and Leyline of the Void are named, and the guide expects Bojuka Bog to hit reanimator players more often (S8). Fix: keep a spare reanimation effect or a rebuy option (S8). Draw imbalance: dead draws such as Phyrexian Delver and Sister Hospitaller stall games; fix: looting, dual-role cards and late hard-casts (S8).

**Traps (S8).** Gray Merchant of Asphodel wears out quickly. Terra's power cap is restrictive, the guide asks. Meren needs protection, without specifics.

**Owner's lessons.** None for this archetype.

## 9. Blink

**Takeaway.** S9 is the only blink source read, and it is dated June 22, 2021. It says blink needs both targets (creatures with enter-the-battlefield effects) and blink effects, and that a lopsided list suffers. It gives no counts for either side.

**Packages (S9, 2021 Roon list).** Creatures 40, instants 9, sorceries 6, artifacts 5, enchantments 2, lands 36 (14 snow-covered basics, 22 nonbasic), commander 1. Derived total 99 (see Conflicts). The 40 creatures are not split into targets and payoffs.
- Roles (names): enabler commander Brago, King Eternal; payoff commander Amareth, the Lustrous; flicker Ephemerate, Eerie Interlude, Restoration Angel; enter-the-battlefield payoffs Panharmonicon, Bramble Sovereign, Blessed Sanctuary; draw Wall of Omens, Ice-Fang Coatl, Cloudblazer; ramp Farhaven Elf, Wood Elves, Solemn Simulacrum; haymakers Avenger of Zendikar, Agent of Treachery; removal Solitude, Knight of Autumn; recursion Eternal Witness, Timeless Witness; tutor Trophy Mage.

**EDHREC data.** None by count (B1). The article predates the other sources.

**Expert view and pod.** Enter-the-battlefield hosers (Torpor Orb, Hushbringer, Hushwing Gryff) shut most of the plan down. The article calls them rare at tables and advises more removal if they are common (S9, citing an EDH Wiki excerpt). Removal crowding leaves little room for noncreature removal (S9). No four-player analysis.

**Weakness and fix.** Target and effect imbalance; fix: balance the two (S9). Commander reliance: enablers need less setup but depend on the commander (S9). A blink target can be removed in response to its trigger, a response the article notes (S9).

**Traps (S9).** Haymakers need only one or two blinks to take over. Roon can blink only one creature a turn.

**Owner's lessons.** None for blink.

## 10. Aristocrats

**Takeaway.** S11 defines the loop (offer creatures for value, return them, offer again) and names three legs: outlets, fodder and payoffs. Missing one hurts. It cites over 84,000 EDHREC decks and names Teysa Karlov and Meren of Clan Nel Toth as the most popular commanders. It gives no counts for outlets, fodder or payoffs.

**Packages (S11, Zahur list).** Creatures 33, instants 9, sorceries 7, artifacts 7, enchantments 7, planeswalkers 1, lands 35 (14 nonbasic, 11 Plains, 10 Swamp), commander 1.
- Outlets: Warren Soultrader, Priest of Forgotten Gods, Greater Good, Ghoulcaller Gisa, Umbral Collar Zealot. Zahur is a free outlet; Fleshtaker is the costed contrast.
- Fodder: Ophiomancer, Adeline, Resplendent Cathar, Jadar, Ghoulcaller of Nephalia, On Wings of Gold, God-Eternal Oketra, Liliana, Dreadhorde General.
- Death payoffs: Blood Artist, Cruel Celebrant, Elas il-Kor, Sadistic Pilgrim, Marionette Apprentice, Morbid Opportunist, Pitiless Plunderer, Black Market, Battle of Hoover Dam.
- Recursion: Ox of Agonas, Unearth. Draw: Greater Good, Priest of Forgotten Gods, Morbid Opportunist.
- Protection: none named. Removal: not a named role.

**EDHREC data.** The 84,000-deck figure and the commander names (S11); no card counts.

**Expert view and pod.** At a table, opponents who notice you profiting from deaths may stop cooperating (S11). Without a free outlet you rely on combat or opponents' removal to clear your creatures (S11).

**Weakness and fix.** Costed outlets are far weaker than free ones (S11); fix: free outlets. Missing payoffs make long, solo-style turns, which the article says most deckbuilders overlook (S11); fix: include payoffs.

**Traps (S11).** Fleshtaker as a costed outlet. Ophiomancer's four tokens per table cycle need free, instant-speed outlets. Zahur's extra payoff needs life loss on three or more turns. The example's creature power is low.

**Owner's lessons.** None for aristocrats.

## Conflicts between sources

1. **Bracket.** S6, S7 and S10 target Bracket 2 (no Game Changers, most tutors left out). The project's target is Bracket 3, so their lists are not Bracket 3 evidence. S7 says tutors depend on the bracket.
2. **Reanimator leaders.** S8 places Muldrotha outside the reanimator archetype; N5 (snippet) calls it the strongest option. S8 is used; N5 is unverified.
3. **Go-wide ratios.** N1 (10 to 15 producers) and N2 (about a third of the list) cannot both be true. Both are snippets, not opened.
4. **Landfall ranking.** S1 ranks Tatyova (178,152 decks) seventh and Evolution Sage (182,988) eighth. Counts and ranking disagree, and the basis is not stated.
5. **Counters total.** S6's header counts give 101 entries including the commander, while its text speaks of 99 slots. The fetch summary counts 100 non-commander entries. Cleopatra may be counted twice. Unresolved; check the page.
6. **Blink total.** S9's list sums to 99 with the commander: one card short, or a counting error. The list dates from 2021.
7. **Pillow fort.** S4 reads 20 planeswalkers and 6 enchantments; S13 describes enchantment-heavy builds. The planeswalker figure looks implausible and should be checked on the page.
8. **Reanimator counts.** The fetch summary of S8 lists no instants or sorceries, and the article names Reanimate and Animate Dead, both sorceries. The summary may be incomplete; check the page.
9. **Dates.** S9 (2021) is five years older than the others. Its card pool and advice may be out of date.

## Gaps

1. **EDHREC JSON.** No synergy, num_decks or potential_decks value per card was obtained: all twelve theme JSON URLs returned 403 (B1). The project CLAUDE.md states that a commander JSON page answered on 2026-10-31; not tested here. Next step: test one commander JSON; if the block is per path, use commander pages.
2. **Landfall guide.** No EDHREC landfall guide was found (B3 returned 404; the search did not return one). Geeky Domain is paywalled (B2). The only landfall sample is one average deck (S5).
3. **Voltron.** B4 failed twice and the EDHREC voltron theme was not reached, so S12 is the only voltron source. The snippet claim that Uril, the Miststalker is the top pick for hexproof is unverified.
4. **Go-wide.** B5 blocked; only snippets N1 and N2.
5. **Pillow fort.** The EDHREC pillow-fort theme page was not read. The edhrecstatic copy (B6) returned 525; the edhrec.com copy (S4) was read. The 20-planeswalker figure needs checking.
6. **Typal.** No Assassins card text and no fragility or evasion counts. N7 was not opened.
7. **Owner's lessons untested.** Haste, team evasion against chump-block boards, and vigilance or defence while tapped: none stated in the read sources. "Several lands per turn": none. "Empties its hand fastest": none. Typal fragility: none.
8. **Functional counts.** No read source gives package counts by function. The counts above are type counts from sample lists, and role lists are names only.
9. **Single samples.** Landfall (S5), tokens (S10), reanimator (S8) and pillow fort (S4) each rest on one sample list. Sample lists are examples, not population statistics.
10. **Four-player pods.** No source addresses four-player pods directly. Table-level statements appear in S8, S9, S10, S11 and S13.
11. **Video and podcast techs.** Not read. The Gemstone Mine episode and The Command Zone were not reachable in this session.
12. **Dates.** S2, S3, S4, S5 and S14 are undated, and S1 gives no data date. Counts are not time-matched across sources.
13. **Bracket 3.** None of the read sources targets Bracket 3.
14. **Snippets.** N1 to N7 were not opened. Treat them as leads only.
