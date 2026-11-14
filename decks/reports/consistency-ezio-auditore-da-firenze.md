# Consistency gate: ezio-auditore-da-firenze (PASS)

Plan: Assassin evasion tempo with a table-ending kill: cheap evasive Assassins and Ezio connect from turn 2 or 3 (Hookblade Veteran, Brotherhood Spy, Basim, Ratonhnhaké꞉ton, flying Equipment), every hit makes Assassin spells cost {B}{B} and draws cards (Basim, Ezio Blade, Coastal Piracy, Etrata, Lion Vulture), and Ramses turns the first elimination into a win of the whole game: Ezio's {W}{U}{B}{R}{G} trigger on a player at 10 or less (Magister Sphinx, Unstoppable Slasher and team damage put them there), or damage focused on one player, while Shao Jun and Kaya hit every opponent without combat and an attack tax, deathtouch and vigilance hold the crack-back.
Backup: Without Ezio or Ramses the same evasive Assassins keep connecting under Arno and Bayek with Rally the Peasants, and Shao Jun and Kaya turn the Equipment, the rocks and loyalty into damage to each opponent every turn.
Archetype: combat_attackers + alternate_kill (plan)

## Failures

- none

## Warnings

- support line team_evasion: 3 pieces, the combat_attackers profile asks 6; write the reason in the profile table or promote the line to a declared function
- base: 35 lands, the combat_attackers profile asks for 36 to 38

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| attackers | early (judged at 12 cards) | 12 | 24 | 23 (commander guaranteed) | 85% | 97% | 99% | 100% |
| through_wide_board | early (judged at 12 cards) | 10 | 19 | 19 | 79% | 93% | 98% | 99% |
| through_big_creatures | early (judged at 12 cards) | 10 | 15 | 15 | 70% | 88% | 94% | 97% |
| condition_enablers | early (judged at 12 cards) | 10 | 20 | 19 (commander guaranteed) | 79% | 93% | 98% | 99% |
| team_finishers | late (judged at 20 cards) | 6 | 7 | 7 | 41% | 61% | 72% | 81% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| haste | 4 | 4 | yes |
| team_evasion | 3 | 6 | yes |
| defense_while_tapped | 7 | 4 | yes |
| combat_draw | 7 | 4 | yes |
| wipe_insurance | 8 | 2 | yes |
| payment_enablers | 9 | 6 | yes |

## Tags

Plan cards (engine, payoff, backup): 29 of 64 non-land cards (45%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 1 |
| draw | 6 |
| engine | 19 |
| land | 35 |
| payoff | 9 |
| protection | 6 |
| ramp | 10 |
| removal | 9 |
| tutor | 3 |
| wipe | 1 |

Base functions, counting second tags too: ramp 10, draw 12, removal 11, wipe 1, protection 7.

## Win routes

- Ezio eliminations, made a table win by Ramses (combat): magister sphinx, ramses, assassin lord, unstoppable slasher. Against three opponents: With Ramses on the battlefield, any opponent who loses after an Assassin attacked them that turn makes me win the game, so ONE elimination ends all three opponents (attack every opponent with at least one Assassin on the kill turn): Ezio connects with a player at 10 or less and {W}{U}{B}{R}{G} removes them; Magister Sphinx sets a player to 10, Unstoppable Slasher halves a player's life in the same combat (its trigger resolves before Ezio's check), team damage does the rest. Without Ramses each elimination removes one player and the route repeats. Ramses is found by Diabolic Tutor and Adewale and returned by Entomb plus Restart Sequence, Layla, Jacob or Altair.
- Assassin team beatdown (combat): arno dorian, bayek of siwa, rally the peasants. Against three opponents: Five or six evasive Assassins split their attacks over the three opponents every turn; Arno adds +2/+0 to every other Assassin, Bayek gives the legendary attackers double strike on my turn, and Rally the Peasants adds +2/+0 to the whole team at instant speed, twice with flashback: each resolution raises the damage to every opponent at once.
- Noncombat damage to each opponent (noncombat): kaya, ghost assassin, shao jun. Against three opponents: Both deal damage or life loss to EACH opponent without passing a blocker: Shao Jun taps two untapped artifacts (the seven Equipment keep working while tapped) for 1 damage to each opponent, again and again in one turn (four Equipment and two rocks give 3 to each opponent per turn); Kaya's -1 drains 2 from each opponent. Eivor, Battle-Ready (Equipment count to each opponent per attack) replaces Kaya when the owner accepts its loan or a copy under 5,000 is read.

Cards bad when drawn (early and late only): {'late': 3, 'early': 5}
