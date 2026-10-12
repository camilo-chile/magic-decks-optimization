Model ID: claude-sonnet-5-5

# Comprehensive Rules check of the open rules readings (2026-10-12)

Closes the readings that the three rules-check reports (`synergy-*-2026-10-12-rules-check.md`)
left "unverified" because the Comprehensive Rules (CR) text was not on disk.

| Item | Value |
|---|---|
| Source | `data/cache/comprehensive-rules.txt`, 9,372 lines, 977,752 bytes, sha256 starts `8d860e451f20f388` |
| Version | "These rules are effective as of September 25, 2026" (line 3 of the file) |
| Method | One reader (Claude Sonnet 5.5) read each cited rule in the file; no second reviewer |
| Labels | CR TEXT = the rule says it. READING = my application of the rule to the cards; not cross-verified |

## 1. Citation fixes
| Cited in the reports | Actual rule in this CR |
|---|---|
| "CR 727" for loops (Azula rules-check, rows 49 and questions 6) | 727 is "Restarting the game" (Karn Liberated). Loops and shortcuts are **CR 732** |
| CR 707.10, 113.7a, 506.4, 903.9a, 704.5n, 613.8, 613.4b, 608.2h, 603.2d, 605.1b, 104.4b, 603.3a, 603.10a, 714.3a, 400.7, 702.122 (Crew), 702.51 (Convoke) | Exist with the content the reports assumed |

## 2. Toph
| # | Question | CR TEXT | Result |
|---|---|---|---|
| T1 | Do Yavimaya, Urborg, Prismatic Omen, Dryad of the Ilysian Grove and Blood Moon apply to artifact-lands whatever their timestamp? | 613.8a: an effect depends on another if applying the other changes what the first applies to; 613.8b: a dependent effect waits until the effects it depends on are applied | READING: Toph's type-changing effect decides which permanents are lands, so Yavimaya, Omen, Dryad and Blood Moon (all layer 4) depend on it and apply after it, regardless of timestamp. Confirms the assumption behind the Spellbook variants |
| T2 | B1 two-piece version: is "that land is a Plains" read when the land has left? | 608.2h: if the object is no longer in the zone it was expected to be in, the effect uses its last known information | READING: yes, the check uses the land's last known information, so the two-piece version works as the verifier described. Keep it as a hazard |
| T3 | Do Ancient Greenwarden and Panharmonicon stack? | 603.2d: an additional-times effect "doesn't invoke itself repeatedly and doesn't apply to other effects that affect how many times an ability triggers" | READING: they add, they do not multiply: 1 + 1 + 1 = 3 triggers per artifact entering (not 4 or 9 triggers). "Up to 9 damage" with Valakut is 3 triggers x 3 damage |
| T4 | Caged Sun loop: is it a draw? | 104.4b / 732.4: a loop of only mandatory actions is a draw | READING: a draw if every action is mandatory; "may" actions break it. Still needs the loop to be mandatory in play |
| T5 | Humility vs earthbend base 0/0 | 701.66a: the land "becomes a 0/0 land creature"; 613.4b layer 7b sets base P/T; 613.7 timestamp order within a layer | READING: the later effect wins in layer 7b: earthbend after Humility gives 0/0 plus counters; Humility entering after the earthbend gives 1/1 plus counters |
| T6 | Titania with a dying artifact-land | 603.10a: leaves-the-battlefield triggers and "put into a graveyard from the battlefield" look back in time | READING: the look-back applies, so Titania sees the land die, including artifact-lands that die by other means |
| T7 | Saga returned by earthbend | 714.3a: a Saga without read ahead "enters with a lore counter" (replacement effect); 400.7: a zone change makes a new object | READING: it re-enters at chapter I and gets a new earthbend trigger only when earthbended again; the cadence of about one fetch per two turns stands |

## 3. Azula
| # | Question | CR TEXT | Result |
|---|---|---|---|
| A1 | Does firebending mana survive into an additional combat phase? | 702.189a: "Whenever this creature attacks, add N {R}. Until end of combat, you don't lose this mana as steps and phases end." | READING: the effect lasts until the end of that combat; an additional combat phase is a different combat, so the mana does not carry into it. This agrees with the 2025 ruling ("until the second main phase"). It settles the "extra combats" question against carrying the mana over |
| A2 | If Azula leaves combat after her trigger is on the stack, does the copy still happen? | 113.7a: once triggered, an ability "exists on the stack independently of its source"; its removal "won't affect the ability". Azula's text is "Whenever you cast a spell while Fire Lord Azula is attacking", which is a trigger condition, not an intervening "if" (603.4) | READING: the copy still happens |
| A3 | Do Strionic Resonator or Return the Favor copying Azula's trigger keep "that spell"? | 707.10: a copy of an ability copies all decisions made for it; 707.10b: same source | READING: the copy of the trigger is tied to the same triggering spell, so "copy that spell" copies it again. Not covered by a specific ruling; keep as READING |
| A4 | Copy keeps modes, targets, X, additional and alternative costs; choices made on resolution are not copied | 707.10 | CR TEXT: confirms rulings rows 8-10 |
| A5 | Loops | 732.1b, 732.2a, 732.4: loops can be shortcut; a mandatory-only loop is a draw | CR TEXT. The self-copy loop (Expansion, Reiterate, Return the Favor with a magecraft payoff) is a loop in which the owner can choose to stop (new targets are optional), so it is not a draw and is shortcut-able. Phase 2 must still detect it |
| A6 | Dying commander and recursion cards | 903.9a: the owner may put a commander that was put into a graveyard or exile since the last state-based action check into the command zone (state-based action); 903.9b: replacement for hand or library | CR TEXT: the owner chooses; to use graveyard recursion they must leave her in the graveyard |
| A7 | Azula copies any spell, not only instants and sorceries | Card text in the pool: "Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell" | CR TEXT of the card: permanent spells are copied too (the copy becomes a token). Reports that say "instant or sorcery" for the trigger should read "spell" |

## 4. Alexios
| # | Question | CR TEXT | Result |
|---|---|---|---|
| X1 | R7: does the previous controller still control Alexios at each upkeep so granted "your upkeep" triggers never fire? | 603.3a: a triggered ability is controlled by the player who controlled its source when it triggered; 603.2: it triggers when the event matches | READING: a granted "at the beginning of your upkeep" ability triggers for whoever controls the creature at that time. Alexios's own text changes control at each upkeep, so the check depends on the order of the two triggers. Keep R7 as a READING with a low weight |
| X2 | Crew and convoke taps on a creature that must attack | 702.122a (crew taps creatures as a cost); 702.51a (convoke taps creatures); 508.1d: attack requirements are checked on declaration | READING: a creature tapped before attackers are declared does not attack, so the opponent may tap it with crew or convoke. Confirms rules-check row C6 |
| X3 | Equipment attached to an illegal permanent | 704.5n: it becomes unattached and stays on the battlefield; 704.5m: an Aura attached illegally goes to the graveyard | CR TEXT: confirms the protection-from-red conflict (red Equipment unattaches, red Auras die) |
| X4 | Protection | 702.16e: damage from sources with the quality is prevented; 702.16f: attacking creatures with protection can't be blocked by creatures with the quality | CR TEXT: confirms Commander's Plate and Sword of Fire and Ice effects on blocks |

## 5. What stays open
- Whether any Spellbook-only combo works exactly as described: not a rules question (combo by combo).
- Two-piece B1 and the self-copy loop are READINGS until Phase 2's combo detector reproduces them on a real list.
- Bracket policy and Game Changer flags after the 2026-10-12 announcement.
- Jeska's 0 ability "until your next turn" after a control change: layers 611.2c / 613 were not read here.
