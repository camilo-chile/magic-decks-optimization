# Consistency gate: ezio-auditore-da-firenze (PASS)

Plan: Assassin strike force with a compact kill: cheap evasive Assassins and Ezio connect from turn 2 or 3, Equipment and unblockable Assassins carry Ezio past any board, every hit makes Assassins (all creatures with Roshan) cost {B}{B} and draws cards; Magister Sphinx, found by Loyal Inventor, Reckless Handling or Entomb and re-used by Kaya, What Must Be Done and Restart Sequence, sets one opponent to 10 and Ezio's trigger removes that player, while team damage (Arno, Achilles, Bayek, Rally, Unstoppable Slasher, pings) drops the rest and attack taxes plus deathtouch bodies hold the crack-back.
Backup: Without Ezio the same evasive Assassins keep attacking with Arno, Achilles and Bayek, Magister Sphinx turns one opponent's 40 into 10 for the team, and Shao Jun and Kaya ping every opponent.
Archetype: combat_attackers + alternate_kill (plan)

## Failures

- none

## Warnings

- support line team_evasion: 4 pieces, the combat_attackers profile asks 6; write the reason in the profile table or promote the line to a declared function
- base: 7 ramp cards, the combat_attackers profile asks for 10 or more

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| attackers | early (judged at 12 cards) | 12 | 19 | 18 (commander guaranteed) | 77% | 92% | 97% | 99% |
| through_wide_board | early (judged at 12 cards) | 10 | 17 | 17 | 74% | 91% | 96% | 99% |
| through_big_creatures | early (judged at 12 cards) | 10 | 17 | 17 | 74% | 91% | 96% | 99% |
| condition_enablers | early (judged at 12 cards) | 10 | 24 | 23 (commander guaranteed) | 85% | 97% | 99% | 100% |
| team_finishers | late (judged at 20 cards) | 6 | 6 | 6 | 36% | 55% | 66% | 75% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| haste | 5 | 4 | yes |
| team_evasion | 4 | 6 | yes |
| defense_while_tapped | 7 | 4 | yes |
| combat_draw | 6 | 4 | yes |
| wipe_insurance | 7 | 2 | yes |
| payment_enablers | 8 | 6 | yes |

## Tags

Plan cards (engine, payoff, backup): 33 of 63 non-land cards (52%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 2 |
| draw | 3 |
| engine | 24 |
| land | 36 |
| payoff | 7 |
| protection | 7 |
| ramp | 7 |
| removal | 8 |
| tutor | 3 |
| wipe | 2 |

Base functions, counting second tags too: ramp 7, draw 11, removal 9, wipe 2, protection 7.

## Win routes

- Ezio eliminations (combat): ezio auditore da firenze, magister sphinx. Against three opponents: Magister Sphinx sets one opponent to 10, Ezio connects and {W}{U}{B}{R}{G} removes that player; the Sphinx is re-used for the next opponent (Kaya's 0 blinks it back at my upkeep, What Must Be Done returns it, Restart Sequence and Layla bring it back), and team damage puts the others at 10 anyway: one player per Ezio hit, three hits on three turns. Found by Loyal Inventor, Reckless Handling and Entomb; costs {B}{B} after a hit with Roshan out.
- Assassin team beatdown (combat): achilles davenport, arno dorian, bayek of siwa, rally the peasants. Against three opponents: Five or six evasive Assassins split their attacks over the three opponents each turn; Arno adds +2/+0 and Achilles +1/+1 to every other Assassin, Bayek gives the legendary and artifact attackers double strike, Rally adds +2/+0 to the whole team twice (flashback): one resolution raises the damage to every opponent at once.
- Pings to each opponent (noncombat): kaya, ghost assassin, shao jun. Against three opponents: Both hit EVERY opponent and repeat: Shao Jun 1 to each per two untapped artifacts (Equipment and rocks), Kaya -1 drains 2 from each (5 loyalty); a top-off that closes a table combat already put low, without passing any blocker.

Cards bad when drawn (early and late only): {'early': 6, 'late': 2}
