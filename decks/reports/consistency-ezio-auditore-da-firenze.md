# Consistency gate: ezio-auditore-da-firenze (PASS)

Plan: Assassin tempo that ends the table: Ezio lands on turn 2 and cheap evasive Assassins (Hookblade Veteran, Basim, Brotherhood Spy, Ratonhnhaketon, Shao Jun, a flying or unblockable Ezio) connect from turn 3, so every Assassin costs {B}{B} for the rest of the turn and the hits draw cards (Ezio Blade of Vengeance, Coastal Piracy, Basim, Etrata, Waterbender Ascension, Eagle Vision); lords, double strike, a 7/6 trampler and the initiative (Ravenloft Adventurer) push one player after another to 10 or less, where Ezio's {W}{U}{B}{R}{G} trigger removes them, and with Ramses on the battlefield the FIRST elimination wins the whole game, while Arbaaz Mir and Shao Jun damage every opponent without combat and Propaganda, Royal Assassin, deathtouch and vigilance hold the crack-back.
Backup: Without Ezio or Ramses the same Assassins keep connecting (freerunning works from any Assassin hit) under Arno, Bayek and Rally the Peasants and kill by plain damage, with Arbaaz Mir and Shao Jun adding damage that ignores blockers, and Ghostly Prison and Propaganda holding the counterattack; Restart Sequence, Layla, Jacob, Altair and The Revelations of Ezio rebuild after a wipe.
Archetype: combat_attackers + alternate_kill (plan)

## Failures

- none

## Warnings

- support line team_evasion: 4 pieces, the combat_attackers profile asks 6; write the reason in the profile table or promote the line to a declared function
- base: 9 draw cards, the combat_attackers profile asks for 10 or more

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| attackers | early (judged at 12 cards) | 12 | 22 | 21 (commander guaranteed) | 82% | 95% | 98% | 100% |
| through_wide_board | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |
| through_big_creatures | early (judged at 12 cards) | 10 | 15 | 15 | 70% | 88% | 94% | 97% |
| condition_enablers | early (judged at 12 cards) | 10 | 18 | 17 (commander guaranteed) | 74% | 91% | 96% | 99% |
| team_finishers | late (judged at 20 cards) | 6 | 7 | 7 | 41% | 61% | 72% | 81% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| haste | 4 | 4 | yes |
| team_evasion | 4 | 6 | yes |
| defense_while_tapped | 7 | 4 | yes |
| combat_draw | 7 | 4 | yes |
| wipe_insurance | 10 | 2 | yes |
| payment_enablers | 10 | 6 | yes |

## Tags

Plan cards (engine, payoff, backup): 29 of 63 non-land cards (46%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 2 |
| draw | 5 |
| engine | 19 |
| land | 36 |
| payoff | 8 |
| protection | 8 |
| ramp | 10 |
| removal | 8 |
| tutor | 2 |
| wipe | 1 |

Base functions, counting second tags too: ramp 11, draw 9, removal 11, wipe 1, protection 9.

## Win routes

- Ezio's elimination, made a table win by Ramses (combat): ramses, assassin lord, unstoppable slasher. Against three opponents: With Ramses on the battlefield, any opponent who loses the game after an Assassin attacked them that turn makes me win at once (ruling 2022-09-09: any cause of loss counts), so ONE elimination beats all three: Ezio connects with a player at 10 or less and {W}{U}{B}{R}{G} removes them, or plain combat damage does. Unstoppable Slasher halves a player's life on a hit, and with Ezio in the same combat a player at 26 or less is removed (Slasher's trigger resolves first). On the kill turn every opponent is attacked by at least one Assassin. Without Ramses the route repeats once per opponent. Ramses is found by Diabolic Tutor, by Entomb plus Restart Sequence, Layla, Jacob, Altair or The Revelations of Ezio.
- Assassin team beatdown (combat): arno dorian, bayek of siwa, eivor, wolf-kissed, rally the peasants. Against three opponents: Five or six Assassins split their attacks over the three opponents each turn: Arno gives every other Assassin +2/+0, Bayek gives the legendary attackers double strike on my turn, Rally the Peasants adds +2/+0 to the whole team at instant speed and again with flashback, Eivor is a 7/6 trampler for {B}{B}. Each of these raises the damage on all three players at once, and each kill by damage is also a Ramses win.
- Noncombat damage to each opponent (noncombat): arbaaz mir, shao jun. Against three opponents: Both hit EACH opponent without passing a blocker: Arbaaz Mir deals 1 to each opponent whenever a nontoken historic permanent enters under my control (40 of the 99 cards are legendary, artifacts or the Saga, and each recast of Ezio counts), and Shao Jun deals 1 to each opponent for every two untapped artifacts I tap (17 artifacts; tapped Equipment keeps working). Together they bring all three players toward 10 at the same time, where Ezio's trigger or one attack finishes each of them.

Cards bad when drawn (early and late only): {'late': 3, 'early': 8}
