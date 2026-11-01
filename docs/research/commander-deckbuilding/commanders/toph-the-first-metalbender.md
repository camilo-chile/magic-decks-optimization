# Toph, the First Metalbender: Commander deckbuilding research

- **Read:** 2026-10-31. **Format:** Commander, 100 cards, singleton. **Reference:** the owner's Bracket 3 pods of 3 to 4 players.
- **Method:** Scryfall, EDHREC JSON, Commander Spellbook and Archidekt figures are copied from API fields. Article claims come from WebFetch, which returns a model's summary of each page rather than raw text. They are marked "as summarised" and were not checked line by line.
- **Access:** the owner authorised EDHREC, Archidekt, Moxfield and Reddit on 2026-10-31. Blocked and not bypassed: Reddit (the search tool reports reddit.com as not accessible to its user agent) and one Moxfield primer (HTTP 403).
- **Brackets:** bracket rules are not re-sourced here; the local prior note (S13) holds them.

## Sources

| ID | Source | Author / publisher | Date | Status | URL |
|---|---|---|---|---|---|
| S1 | Scryfall API, exact name lookup for Toph | Scryfall | Card released 2025-11-21 | Read 2026-10-31 | https://api.scryfall.com/cards/named?exact=Toph,%20the%20First%20Metalbender |
| S2 | Scryfall API, collection lookup for the 308 card names in the EDHREC lists (308 found by the API; 102 names looked up for text here) | Scryfall | Read 2026-10-31 | https://api.scryfall.com/cards/collection |
| S3 | EDHREC commander JSON, all brackets (sample 34,847 decks) | EDHREC | Read 2026-10-31 | https://json.edhrec.com/pages/commanders/toph-the-first-metalbender.json |
| S4 | EDHREC commander JSON, Bracket 3 ("upgraded"; sample 3,150 decks) | EDHREC | Read 2026-10-31 | https://json.edhrec.com/pages/commanders/toph-the-first-metalbender/upgraded.json |
| S5 | "Designing Magic: The Gathering | Avatar: The Last Airbender: Team Avatar and Legendary Creatures" | Chris Mooney, Wizards of the Coast | 2026-01-06 (as summarised) | https://magic.wizards.com/en/news/feature/designing-avatar-the-last-airbender-team-avatar-and-legendary-creatures |
| S6 | Avatar: The Last Airbender release notes (Toph entry read in part 2) | Wizards of the Coast; "compiled by Eliana Rabinowitz" (as summarised) | Feature dated 2025-11-07; "last modified" 2025-06-02 (the two dates conflict, as summarised) | https://magic.wizards.com/en/news/feature/avatar-the-last-airbender-release-notes |
| S7 | "Toph, the First Metalbender | Fire and Ice" | Julia Maddalena, EDHREC | 2026-07-31 | https://edhrec.com/articles/toph-the-first-metalbender-fire-and-ice/ |
| S8 | "Toph, the First Metalbender Commander Deck Guide" | A.L. Walser, Draftsim | Published 2025-10-27; updated 2025-11-01 | https://draftsim.com/toph-edh-deck/ |
| S9 | "Toph, the First Metalbender Commander Deck Tech" | Owain Roberts, EDHREC | 2025-09-05 | https://edhrec.com/articles/toph-the-metalbender-commander-deck-tech |
| S10 | Commander Spellbook API, variants containing Toph (first page: 100 results; 30 processed, 22 complete lines and 1 partial shown) | Commander Spellbook | Read 2026-10-31 | https://backend.commanderspellbook.com/variants/?q=card%3A%22Toph%2C%20the%20First%20Metalbender%22 |
| S11 | Archidekt API, deck 20281888, "Toph First Metal Bender Landfall" | Archidekt (author not captured) | Created 2026-02-24; updated 2026-07-21 | https://archidekt.com/api/decks/20281888/ |
| S12 | Archidekt API, deck 17456305, "Toph, the First Metalbender (Bracket 3)" | Archidekt (author not captured) | Created 2025-11-15; updated 2025-12-13 | https://archidekt.com/api/decks/17456305/ |
| S13 | Local prior note on Commander foundations (its bracket facts come from Draftsim, as summarised) | Project file | Dated 2026-10-31 | docs/research/commander-deckbuilding/notes/01-foundations.md |

Searched, not read (search snippets only; no fact below relies on them): EDHREC cEDH landfall top ten (DougY); EDHREC budget deck tech; EDHREC average-deck pages; mtgdecks.net cEDH lists; a TableCommander Naya list; the Archidekt "Upping the Average" build; two Moxfield lists.

## 0. Card text (checked)

- **Scryfall (S1):** mana cost {1}{R}{G}{W}; Legendary Creature, Human Warrior Ally; 3/3; colours green, red, white; keyword earthbend; set Avatar: The Last Airbender, number 247; released 2025-11-21; legal in Commander. The owner's description matches.
- **Exact Oracle text (S1, read 2026-10-31):**

> Nontoken artifacts you control are lands in addition to their other types. (They don't gain the ability to {T} for mana.)
>
> At the beginning of your end step, earthbend 2. (Target land you control becomes a 0/0 creature with haste that's still a land. Put two +1/+1 counters on it. When it dies or is exiled, return it to the battlefield tapped.)

- **Two consequences used below:** a land that Toph makes into a land gains no mana ability unless it already had one; an earthbent land that dies or is exiled re-enters tapped, which is a land entering the battlefield.

## 1. How experienced players build Toph, and how each plan wins

### Takeaway

Four plans recur: artifact-lands with landfall and ramp (the most common), earthbend recursion as the engine that powers the rest, a land-animation attack with counters and extra combats (secondary), and combos. No source measures which plan is most consistent. Every full list read (S7, S8, S9, S11) combines artifacts with land-based synergy.

### Cited findings

- **Artifact-lands and landfall.** Draftsim describes a Naya landfall deck that fills the board with tokens, uses cheap artifacts for card draw and extra landfall triggers, and closes with team pumps (S8). It says Mishra's Bauble and Soul-Guide Lantern count as landfall triggers, two or three per turn, and cites no rule (S8). Owain Roberts reuses artifacts that have enter-the-battlefield effects by sacrificing an earthbent artifact, which returns; the returning land gives landfall cards repeat value (S9).
- **Earthbend recursion.** Draftsim says earthbend shields key lands from removal such as Stone Rain and works with sacrifice lands such as Urza's Saga and Windswept Heath (S8). It advises using earthbend for sacrifice-and-return value rather than for an army of animated lands (S8). Owain says a land that would leave returns tapped instead (S9). Fire and Ice says earthbent lands rarely attack (S7, as summarised).
- **Land-animation attack.** Toph, Greatest Earthbender gives land creatures double strike. Bumi, Unleashed untaps your lands on combat damage and adds a combat phase. Toph, Earthbending Master earthbends each time you attack (S2 card text). Draftsim's deck closes with team pumps and wide attacks (S8). Fire and Ice calls combat secondary (S7).
- **Combos.** The Spellbook first page holds 100 variants (S10). Of the 30 processed, 22 were readable in full. Most use three or four cards, built around Bumi, Unleashed, Mycosynth Lattice, Zuran Orb, Candelabra of Tawnos or Springheart Nantuko (S10). Draftsim calls its combos minimal (S8). Owain describes a Grinding Station loop that he calls infinite and that needs an off-list card (S9).
- **Winning in a four-player pod.** Draftsim names Cloud's Limit Break and Grasp of Fate as answers that handle all three opponents at once, Mindslaver as a way to disrupt a leader, and Elspeth, Storm Slayer's zero ability as a finisher (S8). Agate Instigator and Warleader's Call deal damage as tokens enter (S8). Fire and Ice lists Germination Practicum as a finisher for players who avoid combo, and calls Emil's large Fractal the author's expectation, unsupported (S7). Owain's damage plan is chip damage from Sabotender and Cyberman Patrol (S9).
- **Consistency.** Draftsim lists its own weak points: a ramp-landfall-ramp rhythm, hands clogged by big artifacts, no mana from artifact-lands without a Dryad-type effect, and thin interaction (S8). Fire and Ice shows no testing or win data (S7).

### Inferences

- My reading, not measured: the landfall and artifact engine has the most functional support across the sources. Combos and the attack plan are narrower. The most consistent core on paper is earthbend, cheap artifacts and ramp together. A test would be needed to rank the plans.

### Gaps

- No source gives win rates, consistency tests or a target count for ramp or landfall per turn (see section 3).

## 2. EDHREC data (S3, S4) and Commander Spellbook (S10)

### URLs that work

| URL | Result |
|---|---|
| json.edhrec.com/pages/commanders/toph-the-first-metalbender.json | Works: 126,176 bytes; all brackets (S3) |
| json.edhrec.com/pages/commanders/toph-the-first-metalbender/upgraded.json | Works: 118,416 bytes; Bracket 3 (S4) |
| Theme pages on the same host, such as .../landfall.json | Not tested |
| edhrec.com commander and average-deck pages (bracket and theme paths) | Appeared in search results; not read |
| archidekt.com/api/decks/{id}/ | Works (S11, S12) |
| backend.commanderspellbook.com/variants/ | Works (S10) |
| moxfield.com primer page | HTTP 403; not bypassed |
| reddit.com | Blocked by the search tool; not bypassed |


### Sample and brackets

- All brackets: the budget tiers sum to 34,847 (3,484 + 27,879 + 3,484), the largest `potential_decks` value. Bracket 3: 3,150 (315 + 2,520 + 315).
- `bracket_counts` (S3; S4 shows the same values): Bracket 1: 66 (1.1%); 2: 1,079 (18.2%); 3: 3,150 (53.0%); 4: 1,348 (22.7%); 5: 296 (5.0%). Percentages are of the 5,939 decks with a bracket label (my arithmetic).
- `tag_counts` (S3; 131 tags; EDHREC does not state the denominator): lands-matter 2,005; artifacts 1,802; +1/+1 counters 1,730; earthbending 881; landfall 683; ramp 365; combo 337; land-animation 188; aggro 127; midrange 120; tokens 102; extra-combats 94; land-destruction 73; sacrifice 57; proliferate 13; voltron 13; card-draw 11.

### Average deck, curve and popularity

- Average deck, all brackets (S3): 24 creatures, 8 instants, 7 sorceries, 17 artifacts, 7 enchantments and 36 lands (15 basic, 21 nonbasic): 99 cards plus the commander.
- Mana curve, all brackets (S3): cost 0: 2; 1: 10; 2: 14; 3: 17; 4: 10; 5: 4; 6: 3; 7: 1; 8: 1. The sum is 62, against 63 nonland cards in the same JSON; unreconciled. Bracket 3 (S4): 0: 2; 1: 9; 2: 14; 3: 17; 4: 10; 5: 4; 6: 3; 7: 1; 8: 1 (sum 61).
- Rank among commanders by month (S3 `rank_over_time`): Aug 2025 46; Sep 109; Oct 99; Nov 2 (1.32% of decks); Dec 2; Jan 2026 6; Feb 11; Mar 15; Apr 18; May 16; Jun 17; Jul 18; Aug 16; Sep 17 (0.36%); Oct 29 (partial month).

### Top cards (num_decks / potential_decks)

| Card | Synergy (S3) | All brackets (S3) | Bracket 3 (S4) |
|---|---|---|---|
| Bumi, Unleashed | 0.60 | 22,444 / 32,716 | 2,265 / 3,033 |
| Toph, Hardheaded Teacher | 0.59 | 21,664 / 32,305 | 2,174 / 3,009 |
| Earthbender Ascension | 0.53 | 19,661 / 32,426 | 1,986 / 3,016 |
| Ichor Wellspring | 0.52 | 19,692 / 34,847 | 1,987 / 3,150 |
| Toph, the Blind Bandit | 0.51 | 20,056 / 34,704 | 1,794 / 3,147 |
| Tannuk, Memorial Ensign | 0.50 | 19,899 / 34,847 | 1,970 / 3,150 |
| Swords to Plowshares | 0.00 | 20,082 / 34,847 | 1,957 / 3,150 |
| Toph, Earthbending Master | 0.46 | 17,372 / 32,716 | 1,741 / 3,033 |
| Toph, Greatest Earthbender | 0.46 | 17,113 / 32,716 | 1,773 / 3,033 |
| Great Divide Guide | 0.46 | 17,033 / 32,366 | 1,716 / 3,014 |

Sources: all-brackets columns from S3 (its Top Cards and Creatures lists); Bracket 3 from S4 (its Top Cards list).

### High synergy (derived here; S3 has no "High Synergy" list)

Synergy of 0.30 or more across S3's twelve card lists: Ba Sing Se 0.60; Badgermole Cub 0.45; Zuran Orb 0.44; Secret Tunnel 0.44; Liquimetal Torque 0.43; Chromatic Lantern 0.42; The Stasis Coffin 0.42; Lotus Cobra 0.42; Avatar Kyoshi, Earthbender 0.40; Evolution Sage 0.39; Ashaya, Soul of the Wild 0.39; Solemn Simulacrum 0.38; Badgermole 0.38; Haywire Mite 0.37; Tireless Provisioner 0.37; The Legend of Kyoshi 0.37; Terrasymbiosis 0.35; Earthshape 0.34; Dryad of the Ilysian Grove 0.33; Cycle of Renewal 0.33; Origin of Metalbending 0.33; Rumble Arena 0.33; Terra Eternal 0.32; Bitter Work 0.31; Earthbending Student 0.31; The Boulder, Ready to Rumble 0.31.

The JSON does not define the synergy field, so treat it as EDHREC's own relative figure (unverified). Generic ramp spells score below zero there: Cultivate -0.24, Rampant Growth -0.22, Farseek -0.16. They are played for ramp, not for Toph.



### Commander Spellbook (S10)

- First page: 100 variants, with no total count in the response. Of the 30 processed, 22 printed in full and one partly (output cut at 12,000 characters). All carry colour identity RGW.
- **Two-card lines (Toph plus one card):**
  - The Stasis Coffin (variant 4155-6871): at your end step Toph earthbends the Coffin; paying {2}, tapping and exiling it gives protection until your next turn, and it returns tapped. The produces list includes prevention of damage and protection during opponents' turns.
  - Mindslaver (1167-6871): an earthbent Mindslaver; {4}, tap and sacrifice it to control a player's turn; Toph returns it from the graveyard.
  - Gonti's Aether Heart (4636-6871): infinite turns once six energy is produced.
  - Caged Sun (5175-6871): steps truncated; the product is a game draw.
- **Bumi lines** (plus Liquimetal Torque, Liquimetal Coating, Mycosynth Lattice or Ashnod's Transmogrant): Bumi's combat trigger untaps all lands, Bumi included because Toph makes it a land, and grants an extra combat phase. Repeated, this gives infinite combat phases.
- **Zuran Orb lines:** plus Mycosynth Lattice (infinite artifact and creature enter and leave triggers), or plus Toph, Hardheaded Teacher and a land such as Gruul Turf, Selesnya Sanctuary or Boros Garrison (infinite landfall and lifegain).
- **Springheart Nantuko lines:** plus Lotus Cobra, Tireless Provisioner or Nissa, Resurgent Animist (infinite landfall triggers and tapped land tokens).
- **Candelabra of Tawnos lines:** plus Gaea's Cradle, Mana Vault, Lotus Field, Grim Monolith or Basalt Monolith (infinite mana).
- **Other lines:** Krark-Clan Ironworks plus Mycosynth Lattice (infinite mana and artifact triggers); Sylvan Safekeeper plus Mycosynth Lattice (infinite creature enter and leave triggers and landfall).
- **Gate note:** S13 (Draftsim, as summarised) says two-card combos cannot come online before turn six in Bracket 3. The four two-card lines above need the project's Layer A check. The steps are Spellbook's text and were not checked against rulings.

## 3. Primers and community discussion

### What was read

- **Owain Roberts, EDHREC, 2025-09-05 (S9).** A Naya list that the author calls far from typical Toph lists and says is built only from Universes Beyond cards (as summarised; the page does not name them, so it is not a Bracket 3 template). Its engine: earthbent artifacts with enter-the-battlefield effects return through sacrifice, and landfall fires as earthbent lands come back, so a board wipe costs no lands. Roles given: Tifa Lockhart and Gladiolus Amicitia (landfall), Tireless Tracker and Tireless Provisioner (landfall value), Harrow (sacrifice an earthbent artifact, fetch two lands), Ashnod's Altar (two mana per sacrifice), Branching Evolution (doubles counters on earthbent permanents), Sabotender and Cyberman Patrol (damage). Stated limits: few earthbend cards existed at the time, and the author doubts that returned artifacts count as lands again. Counts (derived from list headings, as summarised): 37 lands, 25 creatures, 14 artifacts, 12 instants, 10 sorceries, 1 enchantment.
- **Julia Maddalena, EDHREC, 2026-07-31 (S7).** EDHREC's average Toph deck with hot cards added and cold cards removed. Counts: 100 cards including the commander; 36 lands (15 basic: 7 Forest, 4 Mountain, 4 Plains); 17 artifacts; 24 creatures; 7 enchantments; 9 instants; 6 sorceries. Rising: Planar Engineering (sacrifice two earthbent lands for four basics), Erode, Germination Practicum, Emil, Vastlands Roamer and Haywire Mite. Falling: Earthbending Lesson, Badgermole, Earth Rumble and Haru, Hidden Talent. Popularity: Great Divide Guide 51%, Zuran Orb 51%, The Stasis Coffin 45%. The article says Toph ranks 23rd with close to 30,000 decks. It names no brackets, no tests and no ramp count, and it never mentions landfall. Some cost comparisons rest on mana costs that are blank in the scraped text (Toph, Badgermole, Haywire Mite).
- **A.L. Walser, Draftsim, published 2025-10-27, updated 2025-11-01 (S8).** A Naya landfall guide with 16 artifacts. Claims: artifacts give two or three landfall triggers a turn; cheap artifacts supply card draw; a Dryad-type effect is essential, because artifact-lands make no mana on their own; Skullclamp is the strongest artifact on the list; Brightglass Gearhulk can trigger landfall up to three times with Toph. Mana: the guide aims for 40 lands but its list has 34 land cards. Bracket: Bracket 3 because of two Game Changers, one of them Field of the Dead; the guide says it passes Rule 0 if disclosed. Pod: built against three opponents. One phrase, as quoted in the summary: the deck "doesn't win with card quality but quantity."
- **Archidekt, deck 20281888, landfall list (S11).** Created 2026-02-24, updated 2026-07-21, 441 views, no description text. It has 103 entries, 12 of them sideboard, so it is not a clean 100-card list. The author's own category tags (they overlap): Land 22, Ramp 16, Removal 13, Artifact 12, Counters 12, Landfall 6, Creature 5, Protection 5, Draw 3, Finisher 2.
- **Archidekt, deck 17456305, "(Bracket 3)" (S12).** Created 2025-11-15, updated 2025-12-13. Its description holds two image links and no primer. It has 173 entries, 91 of them in the Maybeboard, so it is not a clean list. The bracket field was not read.
- **Moxfield.** The primer page in the search results returned HTTP 403, so it was not bypassed.
- **Reddit.** No thread was read. The search tool reports reddit.com as not accessible to its user agent, so this was not bypassed.

### How many ramp pieces and landfall triggers per turn

- Draftsim: two or three landfall triggers per turn (S8). This is a claim, not a count.
- Archidekt landfall list: 16 ramp-tagged and 6 landfall-tagged cards (S11, the author's tags).
- EDHREC average: 36 lands and 17 artifacts; no ramp or landfall count (S3, S7).
- Owain: no counts (S9). Fire and Ice: no ramp count and no landfall mention (S7).
- No source gives a target. The owner's "absurd" ramp level has no source behind it.

### How the decks close games

- Draftsim: wide boards with team pumps; tokens with Agate Instigator and Warleader's Call; Glacier Godmaw and Canyon Jerboa turn token boards into lethal attacks; Elspeth's zero ability and Field of the Dead serve as direct finishers (S8).
- Fire and Ice: earthbent lands rarely attack, so the finish is card-based or combo-based, with Germination Practicum and Emil's Fractal (S7; the Emil claim is unsupported).
- Owain: chip damage and repeated value rather than one win condition (S9).

### Common mistakes named in the sources

- Draftsim: a predictable ramp-landfall-ramp rhythm; big artifacts that clog the hand; earthbend used to build an army instead of for sacrifice-and-return value; artifact-lands making no mana without a Dryad-type effect; too little interaction; Mox Amber needing legends to shine (S8).
- Fire and Ice: overpriced cards with weak rates: Earthbending Lesson, Badgermole, Earth Rumble and Haru (S7).
- Owain: too few earthbend cards at the time, so the deck needed more to work fully (S9).

## 4. Cards most recommended by function

Synergy and inclusion are from S3 (all brackets) and S4 (Bracket 3), as num_decks / potential_decks. "Recommended by" names only what the author said. "Data" means the figures alone, with no recommendation.

| Function | Card | Syn. | All brackets | Bracket 3 | Recommended by / why |
|---|---|---|---|---|---|
| Ramp | Dryad of the Ilysian Grove | 0.33 | 13,906 / 34,847 | 1,350 / 3,150 | Draftsim: essential; extra land drop; gives artifact-lands a mana ability |
| Ramp | Lotus Cobra | 0.42 | 17,243 / 34,847 | 1,650 / 3,150 | Draftsim: among the strongest enablers |
| Ramp | Solemn Simulacrum | 0.38 | 15,431 / 34,847 | 1,403 / 3,150 | Owain: enter-the-battlefield land fetch |
| Ramp | Harrow | 0.17 | 8,806 / 34,847 | 738 / 3,150 | Owain: sacrifice an earthbent artifact, it returns, fetch two lands |
| Ramp | Sol Ring; Chromatic Lantern | 0.03; 0.42 | 30,387; 18,842 (of 34,847) | 2,841; 1,811 (of 3,150) | Data. Lantern gives every land a mana ability, so it helps artifact-lands (S2 text) |
| Extra land drop | Azusa, Lost but Seeking | 0.06 | 3,713 / 34,847 | not in lists | Data. Two extra land drops (S2 text) |
| Landfall payoff | Scute Swarm | 0.27 | 13,139 / 34,847 | 1,289 / 3,150 | Draftsim: top landfall threat; more tokens with six lands |
| Landfall payoff | Springheart Nantuko | 0.15 | 6,324 / 34,847 | not in lists | Draftsim: top landfall threat; Spellbook lines with Lotus Cobra or Tireless Provisioner |
| Landfall payoff | Tireless Provisioner | 0.37 | 16,715 / 34,847 | 1,573 / 3,150 | Owain: Food or Treasure on landfall |
| Landfall payoff | Tannuk, Memorial Ensign | 0.50 | 19,899 / 34,847 | 1,970 / 3,150 | Draftsim: a scarce red card-draw option; damage when boards stall |
| Landfall payoff | Felidar Retreat | 0.22 | 13,399 / 34,847 | 1,314 / 3,150 | Draftsim: first-tier token source |
| Cheap artifact | Mishra's Bauble | 0.29 | 10,923 / 34,847 | 1,065 / 3,150 | Draftsim: sacrifice for a draw; claimed landfall trigger (no rule cited) |
| Cheap artifact | Soul-Guide Lantern | 0.09 | 3,358 / 34,847 | not in lists | Draftsim: sacrifice for a draw; claimed landfall trigger |
| Cheap artifact | Ichor Wellspring | 0.52 | 19,692 / 34,847 | 1,987 / 3,150 | Data. Its text draws on entering and on dying (S2), so an earthbend loop draws each cycle (derived) |
| Cheap artifact | Haywire Mite | 0.37 | 14,407 / 34,847 | 1,469 / 3,150 | Fire and Ice: rising; reusable exile of a noncreature artifact or enchantment, and lifegain (S7) |
| Land sacrifice | Zuran Orb | 0.44 | 17,716 / 34,847 | 1,701 / 3,150 | Data. Sacrifice a land for 2 life; central to the Spellbook loops |
| Counters | Branching Evolution | 0.10 | 5,638 / 34,847 | 565 / 3,150 | Owain: doubles counters on earthbent permanents |
| Counters | Hardened Scales | 0.15 | 8,527 / 34,847 | 792 / 3,150 | Data. One extra counter (S2 text) |
| Counters | Doubling Season | -0.06 | 2,614 / 34,847 | not in lists | Data. Doubles counters and tokens (S2 text) |
| Counters | The Ozolith | 0.26 | 11,181 / 34,847 | 1,185 / 3,150 | Draftsim: keeps counters from creatures that leave, moves them to a keeper such as Scute Swarm |
| Counters | Toph, Earthbending Master | 0.46 | 17,372 / 32,716 | 1,741 / 3,033 | Data. An attack trigger that earthbends X (S2 text) |
| Protection | The Stasis Coffin | 0.42 | 15,783 / 34,847 | 1,599 / 3,150 | Fire and Ice lists its 45% popularity, no role; Spellbook protection lines (S10) |
| Protection | Terra Eternal | 0.32 | 12,224 / 34,847 | 1,182 / 3,150 | Data. All lands have indestructible (S2 text) |
| Protection | Sylvan Safekeeper | 0.29 | 11,820 / 34,847 | 1,170 / 3,150 | Data. Sacrifice a land for shroud; Spellbook lines (S10) |
| Removal | Swords to Plowshares | 0.00 | 20,082 / 34,847 | 1,957 / 3,150 | Fire and Ice: praised removal (S7) |
| Removal | Path to Exile | -0.03 | 17,562 / 34,847 | 1,715 / 3,150 | Fire and Ice: praised removal (S7) |
| Removal | Hour of Revelation | 0.28 | 11,007 / 34,847 | 1,153 / 3,150 | Data. Destroys nonland permanents; by the rules, artifact-lands are lands, so this spares them (inference) |
| Draw | Esper Sentinel | 0.19 | 11,122 / 34,847 | not in lists | Draftsim: draws at least one card, more with pumps such as Bristly Bill |
| Draw | Spelunking | 0.09 | 4,591 / 34,847 | 488 / 3,150 | Data. Draws, then puts a land from hand onto the battlefield, a landfall event (S2 text) |
| Draw | Skullclamp (no S3 row) | n/a | n/a | n/a | Draftsim: the strongest artifact on the list; fed by 1/1 tokens |
| Finisher | Bumi, Unleashed | 0.60 | 22,444 / 32,716 | 2,265 / 3,033 | EDHREC's top card (S3, S4); extra combat in the Spellbook loops |
| Finisher | Toph, Greatest Earthbender | 0.46 | 17,113 / 32,716 | 1,773 / 3,033 | Data. Land creatures you control have double strike (S2 text) |
| Finisher | Field of the Dead | 0.15 | 6,740 / 34,847 | 742 / 3,150 | Draftsim: one of two Game Changers; a late-game threat that can end games alone |
| Finisher | Elspeth, Storm Slayer (no S3 row) | n/a | n/a | n/a | Draftsim: a token doubler whose zero ability can finish a player |
| Finisher | Germination Practicum | 0.04 | 1,003 / 15,999 | not in lists | Fire and Ice: rising; a finisher for players who avoid combo (S7) |

## 5. The owner's view against the sources

| Owner's view | What the sources show | Verdict |
|---|---|---|
| Lives on landfall and +1/+1 counters | Landfall-and-artifact lists dominate (S7, S8, S9, S11). Tags: landfall 683, +1/+1 counters 1,730, artifacts 1,802 (S3) | Supported by counts |
| Rarely attacks | S7: earthbent lands rarely attack. S8: the deck finishes with wide attacks and pumps. S2 and S10: double-strike and extra-combat lines exist | Partly; the sources disagree |
| Needs an absurd amount of ramp | Ramp-tagged cards: 16 (S11). Mana artifacts are near-universal (Sol Ring 2,841 of 3,150, S4). No source gives a target | Not quantified |
| Ways to make lands enter repeatedly, several per turn | Draftsim: two or three triggers a turn (a claim, S8). Owain: returning lands fire landfall again (S9). Spellbook: infinite landfall lines (S10) | Mechanism supported; the per-turn figure is a claim |
| Counter doublers and counters-on-attack were near-win conditions | Bracket 3 inclusion: Hardened Scales 792 of 3,150; Branching Evolution 565 of 3,150; Doubling Season 2,614 of 34,847 across all brackets, synergy -0.06 (S3). Counters on attack: Toph, Earthbending Master (S2); Tale of Katara and Toph 474 of 3,014 (S4) | Included at moderate rates; no source measures power; the owner's games are unsourced |
| Needs protection | Protection and removal inclusion is high: Swords 1,957 of 3,150, Path 1,715, The Stasis Coffin 1,599 (S4) | Supported by inclusion |
| Depends less on the commander than an attacking deck | No source compares them | Not testable here |

## 6. The artifact-landfall question (open)

- **Settled by the card text (S1):** Toph gives a land no mana ability of its own.
- **Settled by the release-note summary (S6):** Toph's artifacts cannot be played as lands, so they cannot serve as the land drop. The clarification says the ability "only affects permanents on the battlefield." This is a quote from the WebFetch summary, not verified against the page.
- **Mana from artifact-lands (S2 texts):** Dryad of the Ilysian Grove and Prismatic Omen make lands every basic land type, which gives them mana abilities. Chromatic Lantern, Wrenn and Realmbreaker and Great Divide Guide grant a tap-for-mana ability to lands.
- **Open:** whether an artifact that enters while Toph is out triggers landfall. Draftsim says cheap artifacts do, without citing a rule (S8). The release-note summary does not address landfall (S6). Returning earthbent lands do trigger landfall in two sources (S9, and the landfall lines in S10), which fits a land entering the battlefield.
- **Action:** verify with a rules source or a judge before building around artifact landfall. This is not resolved in these notes.

## Conflicts between sources

1. **Deck count.** S7 says "close to 30,000 decks"; S3's all-brackets sample is 34,847.
2. **Popularity.** S7 gives rank 23 (31 Jul 2026); S3 gives rank 18 for July 2026, 16 to 17 for August and September, and 29 for October (partial month).
3. **Land count.** S8 aims for 40 but lists 34 land cards; S7 gives 36 (15 basic); S9 gives 37 (18 basic); S3's average is 36; S11 has 22 "Land" tags plus 16 "Ramp" tags, which may overlap.
4. **Artifact landfall.** S8 says artifacts trigger landfall, citing no rule. S6, as summarised, says only that artifacts cannot be played as lands and that the effect applies to permanents on the battlefield. Not resolved (section 6).
5. **Attack role.** S7 calls combat secondary; S8 builds its finish on wide attacks, pumps and lethal token attacks.
6. **Instants and sorceries.** S3's average is 8 and 7; S7's hot-and-cold-adjusted list is 9 and 6. Both total 99, which fits the stated adjustment.
7. **Mana curve.** The S3 curve sums to 62 and the S4 curve to 61, against 63 nonland cards by type in S3. Unreconciled.
8. **Release-note dates.** The feature is dated 2025-11-07 and the document 2025-06-02, both as summarised. The page version is unclear.
9. **Brightglass Gearhulk.** S8 says it draws two. The S2 text shows an enter-the-battlefield search for up to two artifact, creature or enchantment cards; the visible text does not show a draw. Unverified.
10. **Two-card combos.** S10 shows four two-card lines. S13 (Draftsim, as summarised) says two-card combos cannot come online before turn six in Bracket 3. This is a gate question for Layer A, not a conflict between sources.
11. **Owain's list is not a template.** It is Universes Beyond only (as summarised), so its numbers do not describe a Bracket 3 Naya build.

## Gaps

- **Moxfield and Reddit:** no primer and no Reddit thread was read. The owner's request for Reddit discussion is unmet; the block was not bypassed.
- **Not read:** EDHREC's cEDH landfall top ten; the EDHREC budget deck tech; the EDHREC average-deck pages (landfall and upgraded); the theme JSON (landfall) and bracket-plus-theme JSON; the mtgdecks.net cEDH lists.
- **Spellbook:** 22 of the first 30 processed variants were read in full and one partly; the other 70 on the first page were not printed, and later pages were not fetched. The steps are the site's text.
- **Scryfall:** card text was checked for 101 of the 102 names looked up (the EDHREC lists hold 308 names); The Legend of Kyoshi did not match in the lookup table, so its text is unchecked. Some lookups were cut at 150 characters (for example Kutzil, Springheart Nantuko, Scute Swarm, Brightglass Gearhulk and Earthbender Ascension).
- **EDHREC JSON:** the synergy, lift and trend fields, and the tag-count denominator, are not defined in the JSON. S3 has no "High Synergy" list; the list in section 2 was derived here.
- **Outcomes:** no source tests win rates, consistency, ramp targets or landfall per turn. The owner's experience (counter doublers, protection needs) is unsourced.
- **Ashaya and Toph:** Owain calls the pairing a rules headache for judges (S9); no ruling was found.
- **Bracket facts:** the Game Changers count and the turn-six rule come from the prior note's summary of Draftsim (S13). Wizards' full bracket text was not read here.
