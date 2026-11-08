# Consistency gate: ezio-auditore-da-firenze (PASS)

Plan: Assassin strike force: cheap evasive Assassins and Ezio connect from turn 2 or 3, Equipment (flying, haste, hexproof, trample, vigilance) and unblockable Assassins carry Ezio past any board, every hit turns Assassin spells into {B}{B} casts and draws cards (Ezio, Blade of Vengeance, Coastal Piracy, Eagle Vision), team damage (Arno, Achilles, Bayek, Rally, Unstoppable Slasher halving a life total, pings to each opponent) pushes all three opponents to 10, and Ezio's trigger removes them one per hit while attack taxes and vigilant or deathtouch bodies hold the crack-back.
Backup: Without Ezio on the table the same evasive Assassins keep attacking for damage with Arno's +2/+0 and Bayek's double strike, and the repeatable pings to each opponent (Shao Jun, Vindictive Warden, Kaya) finish players already low from combat.
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
| condition_enablers | early (judged at 12 cards) | 10 | 22 | 21 (commander guaranteed) | 82% | 95% | 98% | 100% |
| team_finishers | late (judged at 20 cards) | 6 | 7 | 7 | 41% | 61% | 72% | 81% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| haste | 5 | 4 | yes |
| team_evasion | 4 | 6 | yes |
| defense_while_tapped | 9 | 4 | yes |
| combat_draw | 7 | 4 | yes |
| wipe_insurance | 5 | 2 | yes |
| payment_enablers | 8 | 6 | yes |

## Tags

Plan cards (engine, payoff, backup): 34 of 63 non-land cards (54%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 1 |
| draw | 4 |
| engine | 26 |
| land | 36 |
| payoff | 7 |
| protection | 7 |
| ramp | 7 |
| removal | 9 |
| tutor | 1 |
| wipe | 1 |

Base functions, counting second tags too: ramp 7, draw 11, removal 9, wipe 1, protection 7.

## Win routes

- Ezio eliminations (combat): ezio auditore da firenze. Against three opponents: Ezio's trigger removes ONE player per connecting hit when that player is at 10 or less and {W}{U}{B}{R}{G} is paid; team damage from the other routes' cards puts all three opponents at 10, so the route needs three hits on three turns (Secret Tunnel, flying Equipment and Swiftfoot Boots keep Ezio connecting); it is the shortcut for the last 10 life of each player, not the whole kill.
- Assassin team beatdown (combat): achilles davenport, arno dorian, bayek of siwa, rally the peasants. Against three opponents: Five or six evasive Assassins split their attacks over the three opponents each turn; Arno adds +2/+0 and Achilles +1/+1 to every other Assassin, Bayek gives the legendary and artifact attackers double strike, Rally adds +2/+0 to the whole team twice (flashback): one resolution raises the damage to every opponent at once.
- Pings to each opponent (noncombat): kaya, ghost assassin, shao jun, vindictive warden. Against three opponents: Each card hits EVERY opponent and repeats: Shao Jun 1 to each per two untapped artifacts (Equipment and rocks), Vindictive Warden 1 to each per {3} (spare mana at end of turn), Kaya -1 drains 2 from each (5 loyalty); a top-off that closes a table combat already put low, without passing any blocker. Otherwise the deck is all-in on combat.

Cards bad when drawn (early and late only): {'early': 3, 'late': 3}
