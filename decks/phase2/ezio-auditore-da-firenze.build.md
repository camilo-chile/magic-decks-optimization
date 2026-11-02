# Ezio Auditore da Firenze: Phase 2 build notes (2026-11-02)

Builder: Opus 5.5 (high), upgrade mode from `decks/scanned/ezio-auditore-da-firenze.txt` (the Phase 1 list). List:
`decks/phase2/ezio-auditore-da-firenze.txt`; plan file: `ezio-auditore-da-firenze.plan.json`. Gate
(`scripts/plan_density.py`): **PASS**, 0 failures, 2 warnings (section 9). Bracket (`scripts/check_phase2_bracket.py`):
**PASS**, floor 1, 0 Game Changers (also checked against the live Scryfall `is:gamechanger` search on 2026-11-02: 53 cards,
none in the list), no extra turns, no mass land denial, no reversible card, 0 Spellbook combos inside the list.
Running the gate script with no arguments also rewrote the consistency reports of Toph and Azula from their own plan files
(deterministic; I did not edit their inputs).

## 1. Commander reading and rules points

Ezio Auditore da Firenze, {1}{B}, 3/2 menace Human Assassin. "Assassin spells you cast have freerunning {B}{B}." "Whenever
Ezio deals combat damage to a player, you may pay {W}{U}{B}{R}{G} if that player has 10 or less life. When you do, that
player loses the game."
- Rewards: Assassin spells (cost reduction after a hit) and Ezio's own combat damage (the kill).
- Fuel: a hit by any Assassin or a commander each turn (turns freerunning on), and Ezio himself connecting while a
  player is at 10 or less, with five colors of mana held for the combat damage step.
- Wins: the kill removes ONE player per Ezio hit, only once that player is at 10. Everything else (the first 30 life of
  each opponent) is combat damage and pings. Single-target kill = backup-style route; the team damage is the main load.
- Dies to: everything (toughness 2), chump blockers (menace fails against 8 goblins), being tapped and open on the
  crack-back. Cheap (2), so recasts are affordable (4, 6) but each recast loses a turn without haste.
- Dependence: **attack engine** (kill only on connecting; the freerunning grant needs him on the battlefield). Commander
  protection min 6, target 8. Haste stays a support line (promotion test fails: the freerunning grant is a static clause
  that acts without attacking) but sits at 5 because the owner lost games with no haste at all.
- Dead clauses in the commander: none. The menace is irrelevant against Board 1.

Rules points to verify:
| Point | Status | What falls if wrong |
|---|---|---|
| The life check happens when Ezio's trigger resolves; once paid, the reflexive trigger kills whatever the life total then | Confirmed, Scryfall ruling 2024-07-05 | Nothing |
| Freerunning is on for the rest of the turn once an Assassin OR a commander dealt combat damage, even if it then leaves | Confirmed, ruling 2024-07-05 | Nothing |
| Ezio's {B}{B} grant needs Ezio on the battlefield when the Assassin is cast | Card text (static ability) | The cheap-cast engine is off while Ezio is dead: cast post-combat only while he lives |
| Brotherhood Headquarters' colored mana can NOT pay Ezio's kill (it pays Assassin spells, freerunning spells, abilities of Assassin sources; the trigger payment is none of these) | Card text and ruling 2024-07-05 (spells and abilities only); not a ruling about triggers, marked "text reading" | It is counted colorless for the payment already |
| Trample damage that passes a chump blocker is combat damage to the player and triggers Ezio (Haunted Cloak) | Rules knowledge (510.1c-d), not re-read | Haunted Cloak drops from through_wide_board (still 15) |
| Shao Jun may tap Equipment (attached) and fresh artifacts to ping | Confirmed, ruling 2024-07-05 (any untapped artifacts); tapped Equipment keeps working (rules knowledge) | Pings slow down |
| Bayek's "historic" = legendary, artifact or Saga | Confirmed, ruling 2024-07-05 | Nothing |
| A creature phased in by Haystack on my untap step can attack (phasing is not a control change) | Rules knowledge 702.26, not re-read | Haystack still saves Ezio, he only waits one turn |
| Bleeding Effect reads only printed keywords of creature CARDS in the graveyard (Hookblade Veteran's and Shao Jun's "during your turn" flying does not count there) | Rules knowledge 113.6 (static abilities work only on the battlefield), not checked in rulings | Already assumed: only Gold-Forged Thopteryx and Aven Heartstabber give flying |
| Kaya's 0 on Ezio returns him at my upkeep, summoning sick | Rules knowledge 302.6 | Already assumed: Kaya is NOT counted as commander protection |

## 2. Plan and backup

- **Plan (one sentence):** cheap evasive Assassins and Ezio connect from turn 2 or 3, Equipment (flying, haste, hexproof,
  trample, vigilance) and unblockable Assassins carry Ezio past any board, every hit makes Assassin spells cost {B}{B}
  and draws cards, team damage (Arno, Bayek, Rally, pings to each opponent) pushes all three opponents to 10, and Ezio's
  trigger removes them one per hit, while attack taxes and vigilant or deathtouch bodies hold the crack-back.
- **Backup (same pieces):** without Ezio, the same evasive Assassins with Arno and Bayek keep dealing damage, and the
  repeatable pings to each opponent (Shao Jun, Vindictive Warden, Kaya) finish players that combat already put low.
- Archetype: `combat_attackers` primary + `alternate_kill` secondary (role plan): the kill triggers on combat damage, so
  the attackers are its fuel (skill hybrid rule). Typal Assassin is a modifier (freerunning): 21 of 27 creatures are
  Assassins (78 %), reported in the plan's support block as a note, not a profile line.
- What changed in kind against Phase 1: the reanimation package (Entomb, Magister Sphinx, Roshan, Deadeye Navigator),
  the copy package (Strionic Resonator, Lithoform Engine, Return the Favor, Dualcaster Mage, Ember Island Production) and
  the Sphinx kill setup are gone; the Equipment that were 2 orphans (Winter Soldier's clause) are now 8 pieces that each do
  a support job (haste, evasion, protection, defense), so Winter Soldier's clause and Ratonhnhaké꞉ton's are live.

## 3. Profile table

Card counts are pieces in the 99 (commander counted only where it says so). Odds: hypergeometric, 99-card library, no
mulligan, no extra draw (conservative).

| Function | Tier | Min | Target | Actual | Reason |
|---|---|---|---|---|---|
| attackers | gate early | 12 | 16 | 17 + Ezio | Fuel: one hit per turn turns on freerunning and the draw; 91 % to see one by 12 cards without Ezio |
| through_wide_board | gate early | 10 | 12 | 15 | Owner's loss to 8 goblins: flyers, unblockables, flying Equipment, Gauntlet, Vapors, Secret Tunnel, trample; menace and Lydia not counted; 90 % by 12 cards |
| through_big_creatures | gate early | 10 | 12 | 16 + Loyal Inventor | 7 spot removal + Haytham, Royal Assassin, deathtouch bodies, Hidden Blade, Lydia, Etrata |
| condition_enablers | gate (late via commander) | 6 | 8 | 6 + Ezio | Team damage that puts every opponent at 10. Same cards as team_finishers ON PURPOSE: in this deck the effects that lower all three life totals are the ones that finish them; the condition's extra piece is Ezio's own hit |
| team_finishers | gate late | 6 | 8 | 6 | Arno, Bayek, Rally, Shao Jun, Vindictive Warden, Kaya: each hits all opponents per resolution. At the minimum (75 % by 20 cards); purchase/loan proposals raise it |
| haste | support | 4 | 6 | 5 | Boots, Haunted Cloak, Hidden Footblade, Boros Guildmage (all repeatable), Queen Marchesa (self). 48 % to see one by 12 cards; Loyal Inventor fetches the three Equipment |
| team_evasion | support | 6 (floor 4) | 8 | 4 (about 2.5 weighted) | **WARN.** The pool has no real team evasion: Gauntlet (one-shot, one opponent), Secret Tunnel (two creatures), Mephitic Vapors (one-shot, kills the 1/1s), Bleeding Effect (flying only with a flier in the graveyard). Board 1 is carried by 15 individual pieces instead; Cover of Darkness is proposed (section 6) |
| defense_while_tapped | support | 4 | 6 | 10 | Propaganda, Ghostly Prison, vigilance (Cloak, Winter Soldier, Loyal Inventor), Royal Assassin, deathtouch blockers (Thorn, Etrata DF), Thopteryx, Bleeding Effect (team vigilance/deathtouch when the yard allows) |
| combat_draw | support | 4 | 6 | 7 | Ezio Blade, Coastal Piracy, Eagle Vision, Jacob, Layla, Etrata DF, Theater of Horrors |
| wipe_insurance | support | 2 | 3 | 5 | Restart Sequence, Revelations III, Layla, Swan Song, Haystack; Equipment survive creature wipes and re-haste the rebuild |
| payment_enablers | support | 6 | 8 | 9 | Lantern, Arcane Signet, Sphere, Waterskin, Command Tower, Orchard, Path, Spire, Abstergo |
| ramp (base) | base | 10 | 12 | 7 | **WARN.** Reason: commander costs 2; avg MV 2.71; every Assassin hit makes the 4 and 5 drops cost {B}{B} (Ezio Blade, Bayek, Arno, Layla, Etrata S, Marchesa), so mana is spent on equip costs and the kill, not on big spells. The pool's 2-mana rocks are taken by Toph and Azula; the 3-mana rocks here are also payment fixers. 36 lands + 7 rocks = 43 sources. Mind Stone proposed (section 8) |
| draw (base) | base | 10 | 12 | 12 tags, about 10.5 weighted | Etrata DF (cloak bodies), Queen Marchesa and Thorn (monarch is often stolen) and Kaya (-2 once) count half |
| removal (base, spot) | base | 6 | 8 | 9 | 7 spells + Haytham + Royal Assassin. Answers (10 with the wipe) stay under the closers (17 attackers + 6 finishers) |
| wipe (base) | base | 1 | 2 | 1 | Mephitic Vapors: kills tokens and 1-toughness bodies; a symmetric wrath would kill the plan |
| commander protection | base (attack engine) | 6 | 8 | 6 | Swiftfoot Boots, Gold-Forged Thopteryx (ward 2 on every legend), Haystack, Swan Song, Enter the Avatar State, Get Out. 55 % by 12 cards; layered: hexproof and ward vs targeted, phasing vs exile and wipes, counter vs wipes, bounce vs anything. Kaya's 0 is not counted |
| graveyard hate | base | 1 | | 1 | Abstergo Entertainment (exile all graveyards; also returns a legend) |
| tutors | | | | 1 | Loyal Inventor: any artifact (flying Equipment, Hidden Blade, Gauntlet, Boots, Lantern) |

Fit check: gate mins counted once (17 attackers already include 6 of the 15 wide-board pieces and 5 of the big-creature
pieces; finishers overlap attackers by 3) plus base floors (7 ramp, 9 removal, 1 wipe, 6 protection, 4 draw-only spells,
2 taxes) = 63 non-land cards: it fits in 99 with 36 lands.

Toughness check: attackers and route cards with toughness 2 or less = Ezio, Initiate, Hookblade Veteran, Aven
Heartstabber, Evie, Winter Soldier, Jacob, Lydia, Adéwalé (9 of 21, 43 %): between a third and a half. Covered by Haystack,
Swiftfoot Boots, Get Out, Enter the Avatar State, Glider Staff (+1/+1), Bleeding Effect (deathtouch/first strike from the
yard) and by keeping the x/1s home against a sacrifice outlet. The engine pieces that must live are tougher: Arno 3/3,
Shao Jun 3/3, Etrata S 3/5, Layla 3/4, Ezio Blade 5/5, Bayek 3/4.

## 4. The list by function: how to use each card

Mana written as `{2}{U}`. "FR" = freerunning (cast after an Assassin or commander hit this turn).

**Commander**
- Ezio Auditore da Firenze: cast turn 2; attack every turn he can connect; hold {W}{U}{B}{R}{G} untapped in combat when the
  defender is at 10 or less; never attack into open deathtouch or first strike without an Equipment on him.

**Early attackers (turn 1 to 3 hits that switch on freerunning)**
- Assassin Initiate: turn 1 drop; pay {1} for flying to connect, deathtouch when it must block or attack into a big body; bad late.
- Hookblade Veteran: turn 1 drop that flies on your turn; attack the player without fliers; bad late.
- Aven Heartstabber: 2-mana flier; when it dies it refills (mill 2, draw 1) and puts flying in the yard for Bleeding Effect.
- Desmond Miles: menace grows with every Assassin; attack the player with the fewest blockers; surveil after a hit feeds Bleeding Effect.
- Brotherhood Spy: unblockable every turn you have a legendary Assassin (Ezio and 14 others); your most reliable early hit.
- Evie Frye: cast for Jacob from the library (a free card); loot with {1}; discard a creature card to make Ezio unblockable that turn.
- Winter Soldier, Icy Assassin: vigilance menace 2-drop that holds the fort; +2/+0 per Equipment, so it is the second Equipment carrier; returns himself late.

**Mid attackers and engines**
- Shao Jun: flier with first strike on your turn; tap two Equipment or rocks for 1 damage to each opponent; never tap the rocks you need for the kill.
- Ratonhnhaké꞉ton: hexproof and unblockable until its first hit: a guaranteed hit for freerunning; later returns a dead Equipment onto its menace token.
- Jacob Frye: after Assassins hit, recast a dead Assassin from your graveyard; best when the yard has Ezio Blade or Arno.
- Lydia Frye: attack the player with big blockers (they cannot block her); end-step surveil bins fliers for Bleeding Effect.
- Adéwalé, Breaker of Chains: cast for FR {B}{B}, take the best Assassin of six; dead clause: Vehicles (none in the list); 4/1, so never attack into first strike.
- Etrata, Deadly Fugitive: 1/4 deathtouch wall that stays home; each Assassin hit cloaks a 2/2 ward body from that opponent's library.
- Arno Dorian: +2/+0 to every Assassin: cast it the turn you swing wide; deathtouch makes it a fine blocker; disguise only to dodge a removal read.
- Queen Marchesa: haste deathtouch; take the monarch only when your taxes and deathtouch blockers can keep it.
- Etrata, the Silencer: cast FR {B}{B}; unblockable removal: exile the biggest blocker of the player you hit; she shuffles away after, so cast her when the hit matters.
- Layla Hassan: FR {B}{B}; every Assassin hit returns a legend, Equipment or Saga to hand: your rebuild after a wipe.
- Ezio, Blade of Vengeance: FR {B}{B} on turn 3 or 4; every Assassin hit draws; 5/5 deathtouch also stops big attackers.
- Bayek of Siwa: FR {B}{B}; your legends and artifact creatures get double strike on your turn: cast it the turn before the big swing; bad early at 5 mana with no hit.

**Equipment (support jobs: haste, evasion, protection)**
- Swiftfoot Boots: on Ezio first; recast Ezio and equip for {1} to attack at once with hexproof.
- Haunted Cloak: haste + vigilance + trample: put it on Ezio Blade or Desmond for damage that passes chumps, on Ezio for haste and to stay back as a blocker.
- Hidden Footblade: flash it in on a recast Ezio for haste, or after blocks for first strike +1/+0 against a bigger blocker.
- Hookblade: attaches on entry: flying for Ezio on your turn; 2 mana for evasion.
- Mechanical Glider: 1-mana flying on entry; the first to move when better Equipment arrives; the card Cover of Darkness replaces.
- Glider Staff: exile the key blocker or an opposing commander on entry (they recast it for {2}), then a flying +1/+1 carrier.
- Hidden Blade: hold it; flash it onto a blocked Assassin: first strike + deathtouch kills the bigger blocker first.
- Assassin Gauntlet: cast precombat on the goblin player: their whole board taps, everybody connects; the carrier loots on hits.

**Removal (spot)**
- Swords to Plowshares: the 1-mana answer to a big blocker or a commander.
- Infernal Grasp: instant answer to any creature; use it on attackers aimed at you while you are tapped out.
- Terminate: same, no life cost.
- Assassin's Trophy: any permanent: enchantment taxes, artifacts, planeswalkers.
- Mortify: creature or enchantment (opposing Propaganda effects).
- Utter End: exile any nonland permanent: commanders and indestructible threats.
- Bitter Triumph: 2-mana kill; pay 3 life, or discard an extra land.
- Haytham Kenway: exiles one creature of EACH opponent: your best card against Board 2; keep him alive (Haystack, Get Out).
- Royal Assassin: stays home; kills an attacker that tapped to hit you, or a blocker that attacked last turn.

**Wipe**
- Mephitic Vapors: cast precombat against a token board: all 1/1s die, then everything connects; it also kills your x/1s (Initiate, Aven, Evie, Adéwalé, Royal Assassin, Deathcap), so attack first with them or accept it.

**Commander protection**
- Gold-Forged Thopteryx: turn 2 play; ward {2} on Ezio and every legend; lifelink flying blocker.
- Haystack: keep {2} up; phase out Ezio or Haytham in response to removal or a wipe.
- Swan Song: counter the wrath or the instant removal aimed at Ezio.
- Enter the Avatar State: in response to removal, or in combat to give Ezio flying, first strike and lifelink for the kill.
- Get Out: counter a creature or enchantment spell, or bounce Ezio and one more creature in response to removal and recast them.

**Card flow**
- Eagle Vision: FR {1}{U} after the first hit: three cards for two mana; never pay 5 unless the hand is empty.
- Coastal Piracy: turn 4 or 5 with three attackers out: one card per connecting creature.
- Kaya, Ghost Assassin: -1 drains 2 from each opponent (closer); -2 trades a card with each opponent; 0 only to blink a creature you need back (it returns sick).
- Theater of Horrors: once you hit every turn it is a second hand; {3}{R} ping turns it on when combat failed.
- Thorn of the Black Rose: monarch draw; play it when deathtouch and taxes can defend the crown.
- Loyal Inventor (tutor): vigilance body that finds the missing Equipment (Boots for protection, a flier against goblins, Hidden Blade against big ones) or Chromatic Lantern for the kill.

**Defense while tapped**
- Propaganda: turn 3 play; pushes the goblin swarm to the other players. Proven role-player.
- Ghostly Prison: the second tax; together they make 8 goblins cost 16 mana per attack.

**Team damage and pings (routes)**
- Rally the Peasants: +2/+0 to the team on the swing that can put two players at 10; flashback for the next swing; bad early.
- Vindictive Warden: menace body; spend spare mana at end of turn: {3} = 1 to each opponent.
- Bleeding Effect: cast once a flier (Thopteryx, Aven) or a deathtouch or vigilance creature is in your yard (surveil with Lydia or Desmond, or after trades): team flying, deathtouch, vigilance; bad early.

**Recursion**
- Restart Sequence: FR {1}{B}: return Ezio Blade, Arno or Haytham after removal; bad early (empty yard).
- The Revelations of Ezio: I kills a tapped creature after their attack, II pumps your Assassin swing, III returns an Assassin.

**Ramp and fixing**
- Sol Ring: turn 1.
- Arcane Signet: turn 2 any color; a kill-payment source.
- Rakdos Signet: turn 2; {B}{R} for FR casts.
- Deathcap Cultivator: turn 2 or 3 (needs {G}); taps for {B} for FR.
- Chromatic Lantern: turn 3 or 4; makes every land pay any color: the kill payment's best card.
- Commander's Sphere: turn 3; any color; sacrifice for a card late.
- Bender's Waterskin: turn 3; untaps on every opponent's turn: protection mana and payment on their turns.

**Lands (36)**: Command Tower, Exotic Orchard, Path of Ancestry (tapped; any color, scry on Assassins), Spire of Industry
(any color with an artifact), Brotherhood Headquarters (any color for Assassins and FR spells, NOT the kill), Abstergo
Entertainment (filter; late: return a legend and exile all graveyards), Secret Tunnel ({4}: Ezio and another Assassin
unblockable), Concealed Courtyard, Isolated Chapel, Drowned Catacomb, Sunken Hollow, Dragonskull Summit, Smoldering Marsh,
Woodland Cemetery, Clifftop Retreat, Sulfur Falls, Hinterland Harbor, Prairie Stream, Glacial Fortress, Radiant Summit,
Jungle Shrine (tapped), Murky Sewer (tapped early), Mystic Monastery (tapped), 9 Swamp, Island, Plains, Mountain, Forest.

## 5. Cut log (Phase 1 list against this list: 38 out, 38 in)

Proven role-players for Ezio (owner): Eagle Vision IN, Propaganda IN, Cover of Darkness proposed (section 6, fallback in
the list). None of the 38 cuts was reported by the owner as winning a game; none is cut for a score or inclusion rate.

| Card out | Function it served | Count after (min) | Replaced by / reason |
|---|---|---|---|
| Entomb | reanimation setup (Sphinx) | package dropped | Owner L1/L7: graveyard mini-plan. Recursion stays as wipe insurance (5, min 2) |
| Magister Sphinx | kill setup, 7 MV | condition_enablers 6+Ezio (6) | Bayek and Rally put ALL opponents low instead of one; 7 MV with Roshan/Entomb support only |
| Roshan, Hidden Magister | made non-Assassins Assassins (for Sphinx, Deadeye) | Assassins 21/27 | Static redundant once the non-Assassins are cut; slot to Layla Hassan |
| Deadeye Navigator | protection, 6 MV | protection 6 (6) | Haystack: 2 mana, instant, also beats exile wipes |
| Strionic Resonator, Lithoform Engine | trigger copies | none (orphan package) | Copy package dropped (L1); slots to Bleeding Effect, Shao Jun |
| Dualcaster Mage, Ember Island Production | copy mini-combo | none | L7 named; slots to Vindictive Warden, Rally the Peasants (team finishers 6) |
| Return the Favor | protection/copy | protection 6 (6) | Get Out (UU, counters or saves two creatures) |
| Venser, Shaper Savant | protection/tempo, 4 MV | protection 6 (6) | Swan Song (1 mana, stops wipes) |
| Mana Leak | counter | removal 9 (6) | Weak late; Enter the Avatar State takes the protection job |
| Nekrataal | removal, nonblack only | removal 9 (6) | Play review "replace"; Swords to Plowshares |
| Fatal Push, Murder, Fateful Absence, Stroke of Midnight, Chaos Warp, Kolaghan's Command | spot removal | removal 9 (6, target 8) | Answers outnumbered closers (red flag); kept the 7 cheapest flexible ones. Freed slots go to haste, evasion, taxes |
| Starfall Invocation | wipe | wipe 1 (1) | Symmetric wrath kills the attack plan; Mephitic Vapors is near one-sided against tokens |
| Intruder Alarm | none (no line) | n/a | Orphan (play review) |
| Everflowing Chalice | ramp | ramp 7 (10, WARN) | Owner L5: cast turn 5 for two. Bender's Waterskin (fixes and works on opponents' turns) |
| Dimir Locket | ramp, 3 MV | ramp 7 | Play review "replace"; Commander's Sphere (any color for the kill) |
| Rampant Growth | ramp ({G} on turn 2) | ramp 7 | Green on turn 2 is about 50 % here; replaced by colorless/any-color rocks |
| Mishra's Bauble, Brainstorm, Faithless Looting, Seismic Sense | cantrips (not draw) | draw 12 (10) | Not draw; Eagle Vision, Theater of Horrors |
| Mystical Teachings | tutor for instants, 4 MV | tutors 1 | Few flash targets left; Loyal Inventor finds Equipment |
| Reckless Handling | artifact tutor, random discard | tutors 1 | Random discard can lose the fetched card; slot to Glider Staff |
| Tome of Legends | slow draw | draw 12 (10) | Theater of Horrors gives more per turn; Tome kept as the next draw swap if draw comes short in play |
| Ravenloft Adventurer | initiative + hit counters | attackers 17 (12) | Initiative makes the deck the target while it is open after attacking; hit counters need Etrata (mini-combo); Layla Hassan |
| Rumble Arena, White Lotus Hideout, Survivors' Encampment | colorless/filter lands | lands 36 | Review flagged colorless lands; Path of Ancestry, Spire of Industry, Murky Sewer |
| Frostboil Snarl, Fortified Village, Game Trail | reveal duals (mostly tapped with 1 basic of each) | lands 36 | Jungle Shrine, Mystic Monastery (three colors each), Glacial Fortress |
| Island (one of two) | U source | U about 16.5 | +1 Swamp (B is the heaviest color: 28 pips, {B}{B} FR) |

Considered and left out: Hullcarver (1/1 deathtouch, chumped by goblins; no slot), Rooftop Assassin, Merciless Harlequin,
Hunter's Bow (needs {G} early), Champion's Helm (Azula's), Tome of Legends, Fire Nation Archers, Kitesail, Aya of
Alexandria, Vincent, Massacre Girl, What Must Be Done, Octopus Form (first protection add if Swan Song goes to Azula).

## 6. Loans

Used (already declared or auto class):
- Eagle Vision (declared `borrowed`, ACR 17 EN): in the list.
- Layla Hassan (auto, 915 CLP replacement): recursion engine, wipe insurance, 3/4 first strike. Lead: add the `borrowed`
  entry and the restock row.
- Bayek of Siwa (auto, 915 CLP): team double strike for legends and artifact creatures: team_finisher and condition enabler.
  Lead: add the `borrowed` entry and the restock row.
- From his own collection (no loan): Assassin Initiate, Hidden Blade, Hidden Footblade (free copy), Propaganda (free
  copy), Ratonhnhaké꞉ton (free copy).

Proposals TO EVALUATE (the list keeps the fallback):
1. **Cover of Darkness** (proven role-player per the owner; 10,360 CLP LP foil, the only copy at Game of Magic Singles).
   Need: team_evasion is 4 pieces (about 2.5 weighted) against a profile min of 6; it is the owner's named loss (8 goblins).
   Naming Assassin gives fear to 21 of 27 creatures and Ezio: only black or artifact creatures can block them. Replacement
   situation: 10,360 CLP, over the 5,000 limit, in stock on 2026-10-31. Fallback in the list: **Mechanical Glider**.
2. **Unstoppable Slasher** (5,560 CLP, in stock). Need: condition_enablers and team_finishers sit at their minimum; a hit
   halves a player's life (40 to 20 to 10), the fastest way to Ezio's threshold; Assassin, deathtouch, returns once.
   Fallback in the list: **Boros Guildmage** (haste stays at 4 = min without it).
3. **Achilles Davenport** (8,680 CLP ES, in stock). Need: other Assassins +1/+1 fixes the toughness profile (43 % at 2 or
   less) and adds damage to every attack; FR {U}{B}. Fallback in the list: **Adéwalé, Breaker of Chains**.

## 7. Scarce copies (for `scripts/assign_copies.py`)

| Card | Copies | Wanted by | Where it adds most | If Ezio loses it |
|---|---|---|---|---|
| Swan Song | 1 (ES) | Ezio, Azula | Azula (instant density, copied by Azula); Ezio has a same-job free card | Octopus Form (free copy) |
| Hidden Footblade | 1 free + 1 in the Standard binder (no stock) | Ezio, Azula | Ezio (cheap commander recast needs haste; Footblade is one of 4 repeatable haste pieces) | Haste 4 (= min); add Expedite |
| Chromatic Lantern | 2 | Ezio, Toph (Azula if she adds it) | Ezio (only five-color kill payment fixer of its kind) | Payment odds drop; Commander's Sphere and Arcane Signet remain |
| Command Tower | 3 (1 EN, 2 ES) | Ezio, Toph, Azula (+ Spanish deck if it wants it) | Any; Ezio can take an ES copy | Exotic Orchard-type land |
| Propaganda | 2 free + 1 loan | Ezio, Azula | One each; the loan copy is auto class if a third deck wants it | Ghostly Prison stays |
| Battlefield Forge (avoided) | 1 (ES) | Toph | Toph: I replaced it with Radiant Summit | n/a |
| Layla Hassan, Bayek of Siwa | 1 loan each | Ezio | Ezio (Assassin legends; one loan serves one deck) | Etrata S, Arno carry the finishers |
| Spanish-only cards here (Hookblade, Hookblade Veteran, Brotherhood Spy, Evie Frye, Ezio Blade, Utter End, Theater, Restart Sequence, Revelations, Commander's Sphere, Deathcap, Spire of Industry, Glacial Fortress, Mystic Monastery, Radiant Summit, Isolated Chapel, Woodland Cemetery, Hinterland Harbor, Assassin Gauntlet, Swords, Exotic Orchard, Brotherhood HQ, Clifftop) | ES copies | The Spanish deck (Kilo) list read 2026-11-02 wants none of them | n/a | Re-check if the Spanish list changes (Kilo is URW: Mystic Monastery, Glacial Fortress, Spire, Sphere, Radiant Summit are its colors) |

## 8. Purchase proposals (Game of Magic Singles; the three bilingual decks share at least 5,000 CLP; prices are hints from the 2026-10-17 browser reading, verify live stock)

Ranked by impact on this deck:
1. **Mind Stone** (about 742 CLP). Need: ramp 7 against min 10; a colorless 2-drop rock cast on turn 2. Plays instead of:
   Deathcap Cultivator (needs {G} on turn 2).
2. **A 2-mana B Talisman or Signet** (Talisman of Hierarchy, Dominance or Indulgence, or Orzhov/Dimir Signet; price to
   read). Need: ramp and black sources for {B}{B}. Plays instead of: Commander's Sphere (3 MV).
3. **Rogue's Passage** (about 742 CLP; his two copies sit in Toph and Azula). Need: repeatable unblockable for Ezio himself
   against any board. Plays instead of: Murky Sewer (tapped early).
4. **Arcane Denial** (about 2,840 CLP). Need: a second counter for commander protection (6 = min). Plays instead of: Get Out.
Not proposed: Lightning Greaves (11,680 CLP), Cover of Darkness as a purchase (section 6 instead).

## 9. Warning reasons and dead clauses

- WARN ramp 7 < 10: see the profile table (commander MV 2, freerunning as cost reduction, 2-mana rocks taken by other
  decks; Mind Stone proposed).
- WARN team_evasion 4 < 6: the pool lacks team evasion; the profile allows floor 4 with through_wide_board carried by
  flyers, unblockables and the Equipment (15 pieces, 90 % by 12 cards); Cover of Darkness proposed.
- Dead or weak clauses: Adéwalé's Vehicle return (no Vehicles); Haytham's Knight bonus and protection from Assassins (no
  Knights; irrelevant); Ratonhnhaké꞉ton's Equipment return (live but rare); Bleeding Effect's flying needs one of 2 flying
  creature cards in the yard (its deathtouch, vigilance, menace come from 8 more); Mephitic Vapors kills 6 of my x/1s;
  Kaya's 0 is a slow blink; Arno's and Bayek's disguise only as anti-removal bluff.
- The two late gate functions share their 6 cards by design (section 3).

## 10. The two reference boards

- **Board 1, eight or more sacrificeable 1/1s:** Assassin Gauntlet taps their whole board for one swing; Mephitic Vapors
  kills all of them precombat; Ezio flies with Hookblade, Mechanical Glider or Glider Staff, or goes unblockable with Secret
  Tunnel; Brotherhood Spy, Etrata S, Ratonhnhaké꞉ton (first hit), Shao Jun, Initiate, Hookblade Veteran, Aven fly or pass;
  Haunted Cloak tramples over a chump; pings hit them anyway. Defense: Propaganda + Ghostly Prison charge 2 per goblin,
  deathtouch blockers and Thopteryx. My x/1s do not attack into a board with a sacrifice outlet.
- **Board 2, two or more bigger creatures:** Haytham exiles one per opponent; 7 spot removal; Royal Assassin kills them
  after they attack; Etrata S exiles one per hit; Hidden Blade (first strike + deathtouch) and deathtouch bodies (Arno, Ezio
  Blade, Etrata DF, Initiate) make blocks bad for them; Lydia cannot be blocked by power 3+; the fliers go over.
- **One sweeper turn:** Haystack or Swan Song saves Ezio or the board; Equipment survive; next turn Ezio (4 mana) + Boots
  or Cloak attacks at once, Layla, Restart Sequence, Revelations III and Jacob rebuild.

## 11. Mana

- 36 lands (band 36 to 38) + 7 rocks/dorks. 23 nonbasic + 13 basic (9 Swamp).
- Colored sources (lands full, any-color lands full, Orchard/Spire/HQ 0.75, Abstergo 0.5, rocks 0.75, Lantern full):
  B about 27, U about 17, W about 17, R about 17, G about 13. Pips: B 28, U 21.5, W 19, R 8.5, G 2. B meets {B}{B} on
  turns 3 to 4 (Karsten 2CC about 26); U and W are under the turn-2 targets for 2-drops (19): the blue and white 2-drops
  are often cast on turn 3.
- Tapped lands: 4 always (Path, Jungle Shrine, Mystic Monastery, Murky Sewer early) + 4 battle lands tapped until two
  basics (13 basics). Check lands mostly untapped (9 Swamps).
- Curve (non-land 63): MV1 8, MV2 19, MV3 22, MV4 11, MV5 3; average 2.71. Turn 2 and 3 plays: 27 cards at MV 1 to 2.
- Keepable hand (2 to 4 lands in 7): 74 % per look, 93 % with the free mulligan.
- Kill payment {W}{U}{B}{R}{G} held in combat (simulation, 20,000 games, conservative: Brotherhood HQ, Abstergo and Sol Ring
  count as colorless, Rakdos Signet one color): 43 % by turn 6, 60 % by turn 8, 72 % by turn 10. With five or more
  sources the colors fit 61 to 78 %; Chromatic Lantern or Loyal Inventor fetching it lifts it. The kill is the shortcut, the
  team damage is not color-bound.

## 12. Open questions for the owner

1. Cover of Darkness (10,360 CLP): accept the loan (Mechanical Glider leaves)? Unstoppable Slasher and Achilles too?
2. Layla Hassan and Bayek of Siwa are auto loans: OK to lend both to Ezio?
3. Swan Song (one Spanish copy) to Azula or Ezio? My view: Azula; Ezio then plays Octopus Form.
4. Hidden Footblade: the free copy to Ezio (haste for the recast commander) or to Azula?
5. Is the attack-tax pair (Propaganda + Ghostly Prison) welcome at your table, or do you prefer vigilance bodies?
