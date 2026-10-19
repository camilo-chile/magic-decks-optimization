# Ezio Auditore da Firenze: round-5 backtrack for Peter Parker's Camera (2026-10-19)

Trigger: the live stock check `data/stock/20261019T1234Z.json` found Peter Parker's Camera out of stock at paytowin, the
only store that listed it (`merged-20261019T1013Z.json`). Base: `decks/measured/ezio-auditore-da-firenze/round4-step39.txt`
(Commander Salt 7.4, scoring 2026.4195, 10 Spellbook lines, nonland average mana value 2.781). Plan priced together with
Azula `round4-step27` and Toph `round3-step21` (`scripts/check_list.py`, owned copies shared in the order Toph, Azula, Ezio).
Lands untouched (Manabase Quality 97 %). Card facts: `oracle-cards-20261011210156.jsonl.gz`; lines: local Spellbook slim file.

**Outcome (2026-10-19):** cand1 was measured on Commander Salt (7.7) and is saved as `decks/measured/ezio-auditore-da-firenze/round5-step40.txt` (`decks/reports/round5-ezio-20261019.md`); the file `ezio-r5-cand1.txt` was removed as a duplicate. cand2 and cand3 stay as unmeasured fallbacks (for example if Magister Sphinx sells out) until the purchase is done.

## What the Camera did
- 3 of the 6 Etrata lines (Spellbook, "target opponent loses the game"): Etrata, the Silencer + Camera + Strionic
  Resonator / Lithoform Engine / Return the Favor. Without it: Etrata + any two of the other three copiers (3 lines).
- A 1-mana artifact found by Reckless Handling and Loyal Inventor; copied Thorn, Ravenloft and other triggers.
- Step 39 without the Camera: 7 lines; the three lists cost 171,074 CLP, room 28,926 CLP under 200,000.

## Replacements surveyed (in stock in the merged prices, inside WUBRG, Commander-legal, one face)
| Card | CLP (store) | Spellbook lines it completes here | Verdict |
|---|---|---|---|
| Roaming Throne | 67,990 (cardnexus) | 3 (the Camera's own Etrata lines) | over the room |
| Kiki-Jiki, Mirror Breaker | 18,500 (lacomarca) | 2: + Intruder Alarm (8 mana, floor 3 with a note); + Dualcaster + Return the Favor | cand3 |
| Magister Sphinx | 10,850 (lacomarca) | 1: Ezio (commander) + Sphinx, "target opponent loses the game", 12 mana, floor 3 | cand1, 2, 3 |
| Hullbreaker Horror | 8,360 (gameofmagic) | 1: + Intruder Alarm (mana and storm engine, no kill feature) | not used |
| Annie Joins Up | 990 (cardnexus) | 0 (not in Spellbook): Etrata's trigger triggers twice, so Etrata + Annie + any one copier kills | cand2 |
| Wizard's Staff | 7,100 (lacomarca) | 0 (same effect as Annie, equip {3}) | Annie is cheaper and better |

Wishlist (not in the merged prices, no stock evidence, never in a list until priced): Adric, Mathematical Genius and The
Peregrine Dynamo (each restores the three Etrata lines), Tawnos, Urza's Apprentice, Abstruse Archaic, and Gogo, Master of
Mimicry (Etrata + Gogo, two cards, 7 mana, floor 3 with a note).

## Candidates
| | cand1 | cand2 | cand3 |
|---|---|---|---|
| Swaps vs step 39 | - Camera + Magister Sphinx | - Camera + Magister Sphinx; - Royal Assassin + Solve the Equation; - Lydia Frye + Annie Joins Up | - Camera + Magister Sphinx; - Royal Assassin + Kiki-Jiki; - Entomb + Diabolic Intent |
| Together (3 decks) | 181,924 CLP | 188,304 CLP | 197,604 CLP |
| Ezio cost | 83,591 | 89,971 | 99,271 |
| Layer A | floor 3, 0 Game Changers, ELIGIBLE | same | same (+ Kiki + Alarm flagged floor 3) |
| Spellbook lines | 8 | 8 (+3 Annie lines Spellbook does not list) | 10 |
| Nonland average mana value | 2.875 | 2.891 | 2.922 |
| Stores | the same 7 as step 39 | same | same |

Bought cards new to the plan (merged prices 2026-10-19T10:13Z; only Solve the Equation was read live, at 12:34Z):
| Card | Cheapest offer | Other offers |
|---|---|---|
| Magister Sphinx | lacomarca 10,850 (en, LP, Conflux) | lacomarca 12,050 NM, 14,900 (2X2); paytowin 18,700 (etched foil) |
| Solve the Equation | cardnexus 5,390 (es, NM, 4 in stock live; Azula takes 1) | lacomarca 6,250; oasis 7,320 |
| Annie Joins Up | cardnexus 990 (en, NM, 7) | cardnexus 1,490 foil; oasis 2,940; magic4ever 4,300; lacomarca 6,650 |
| Kiki-Jiki, Mirror Breaker | lacomarca 18,500 (en, LP, The List) | lacomarca 25,200 (es), 26,800; paytowin 87,100 |
| Diabolic Intent | gameofmagic 19,580 (es, NM) | paytowin 29,900, 30,200 |

### Why
- **cand1 (one swap).** The Sphinx sets a player to 10 life and Ezio's own trigger then wins on combat damage: a
  Salt-visible kill line with the commander, which is always available. Like the Camera it is an artifact, so Reckless
  Handling and Loyal Inventor still find the line; also Seismic Sense, Entomb + Restart Sequence, and Adéwalé when Roshan is
  out. The copier package stays intact and gets a new target: a copied Sphinx trigger puts a second opponent at 10.
- **cand2.** cand1 plus tutor reach: Solve the Equation finds Starfall Invocation and Ember Island Production (the two
  Dualcaster pieces that no tutor reached), Return the Favor, Restart Sequence and Mystical Teachings. Annie Joins Up brings
  back the Camera's three kills in play (Etrata + Annie + Strionic, Lithoform or Return the Favor). It is also removal
  (5 damage) and doubles the triggers of the legends (Ezio, Blade of Vengeance, Etrata, Deadly Fugitive, Adéwalé, Venser,
  Haytham, Queen Marchesa, Jacob Frye, Desmond). Cuts are the two weakest slots: Royal Assassin (slow removal on a 1/1) and
  Lydia Frye.
- **cand3.** Back to 10 Spellbook lines: Kiki adds two, and Diabolic Intent, a tutor to hand, reaches Intruder Alarm, the
  only piece of three lines that nothing tutors (it costs 2,820 CLP less than Entomb). Risks: (1) Round-4 step 43 added Kiki
  lines and fell from 7.4 to 6.2. That step also cut Coastal Piracy, Theater of Horrors and Kaya, which stay in this list.
  (2) The margin is 2,396 CLP. If the single cheapest Kiki copy (next 25,200) or Diabolic copy (next 29,900) sells, the plan
  goes over 200,000.

## Measure order
1. **cand1**: one change, the cheapest, and it shows what losing the Camera costs. If it scores 7.4 or more, stop.
2. **cand2**: the most tutor coverage without Kiki. Measure it if cand1 scores below 7.4.
3. **cand3**: the highest line count, but the most variance (the step-43 precedent) and a thin price margin.

Before any purchase: run the live stock check on the new cards (Sphinx, Annie, Kiki, Diabolic Intent; only Solve the Equation
has been read live). `check_list.py` prints "commander not recognized" for Ezio because `layer_a.COMMANDERS` does not list
him. The default target, Bracket 3, still applies, as it did for step 39. Nothing in these lists is a power estimate: only
the Salt score of the exact list counts.
