#!/usr/bin/env python3
"""Phase 8: turn a purchase ladder into nested decklists and check every step. No network.

A ladder file (`decks/proposals/<deck>.ladder.txt`) holds a free base list and an ordered list of swaps:

    // Commander
    1 Toph, the First Metalbender

    // Base
    1 Some Owned Card
    20 Mountain

    // Ladder
    + Card To Buy | - Card To Cut | why this swap is worth its price

The base should cost 0 (owned cards and basics only). Each swap adds one copy of the first card and removes
one copy of the second, in the order the owner would make them. Every step must be a valid list: 100 cards,
Layer A at Bracket 3, every purchase in stock. The script prints, per step, the cumulative cost of the whole
list (owned copies free, cheapest English or Spanish offer otherwise, Spanish on a tie), the Layer A floor and
whether the step is valid, then the checkpoints: for each cap, the last step whose cost is at or under it.

Run it with the "Run Python File" button (no arguments) to read every decks/proposals/*.ladder.txt, or pass
files: `python scripts/ladder.py decks/proposals/azula.ladder.txt [--write] [--caps 0,25000,50000]`.
`--write` saves each checkpoint as `decks/proposals/<deck>_cap<N>.txt` (the only place it writes). Read-only
otherwise. Prices are a hint (stock is verified in Phase 9); power is the Commander Salt score of the exact
list, never computed here.
"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_list as cl  # noqa: E402
import layer_a as la  # noqa: E402

PROPOSALS = cl.PROPOSALS
DEFAULT_CAPS = (0, 25000, 50000, 75000, 100000, 150000, 200000)
SPLIT_RE = re.compile(r"^//\s*Ladder\s*$", re.I | re.M)
SWAP_RE = re.compile(r"^\+\s*(?P<add>[^|]+?)\s*\|\s*-\s*(?P<drop>[^|]+?)\s*(?:\|\s*(?P<why>.*))?$")


def split_ladder(text):
    """(base list text, swaps) where each swap is {"add", "drop", "why"}; raises ValueError on a bad swap line."""
    parts = SPLIT_RE.split(text, maxsplit=1)
    head, tail = parts[0], parts[1] if len(parts) > 1 else ""
    swaps = []
    for raw in tail.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = SWAP_RE.match(line)
        if not match:
            raise ValueError(f"not a swap line (expected '+ Card | - Card | why'): {line}")
        swaps.append({"add": match.group("add"), "drop": match.group("drop"), "why": match.group("why") or ""})
    return head, swaps


def base_state(head):
    """(commander entries, {normalized name: [name, qty]}) from the base list text."""
    commanders, main, bad = la.parse_decklist(head)
    if bad:
        raise ValueError(f"unparsed base lines: {bad[:3]}")
    state = {}
    for entry in main:
        slot = state.setdefault(la.normalize(entry["name"]), [entry["name"], 0])
        slot[1] += entry["qty"]
    return commanders, state


def apply_swap(state, add, drop):
    """A new state with one copy of `drop` removed and one of `add` added; ValueError if `drop` is not there."""
    new = {key: list(slot) for key, slot in state.items()}
    dkey = la.normalize(drop)
    if dkey not in new or new[dkey][1] < 1:
        raise ValueError(f"cannot remove '{drop}': it is not in the list at this step")
    new[dkey][1] -= 1
    if new[dkey][1] == 0:
        del new[dkey]
    slot = new.setdefault(la.normalize(add), [add, 0])
    slot[1] += 1
    return new


def render(commanders, state):
    """The list as ManaBox-style text."""
    lines = ["// Commander"] + [f"{e['qty']} {e['name']}" for e in commanders] + ["", "// Main"]
    lines += [f"{qty} {name}" for name, qty in sorted(state.values(), key=lambda s: s[0].lower())]
    return "\n".join(lines) + "\n"


def pick_checkpoints(steps, caps):
    """{cap: index of the last valid step whose cost is at or under the cap, or None}."""
    picked = {}
    for cap in caps:
        picked[cap] = None
        for i, step in enumerate(steps):
            if step["valid"] and step["cost"] <= cap:
                picked[cap] = i
    return picked


def run(path, ctx, caps, write):
    """Materialize one ladder; print the table and return the checkpoints (and write them with `write`)."""
    stem = path.name.removesuffix(".ladder.txt")
    head, swaps = split_ladder(path.read_text(encoding="utf-8-sig"))
    commanders, state = base_state(head)
    states, steps = [state], []
    for swap in swaps:
        states.append(apply_swap(states[-1], swap["add"], swap["drop"]))
    print(f"=== {path.name}: base + {len(swaps)} swaps")
    for i, st in enumerate(states):
        text = render(commanders, st)
        _, verdict = cl.check_text(f"{stem}_step{i}", text, ctx, Counter(), brief=True)
        verdict["valid"] = verdict["ok_layer"] and not verdict["no_stock"]
        steps.append(verdict)
        change = "base" if i == 0 else f"+ {swaps[i - 1]['add']} | - {swaps[i - 1]['drop']}"
        problem = "" if verdict["valid"] else f"  INVALID: {verdict['reasons'][:1] or verdict['no_stock'] or 'Layer A'}"
        print(f"  step {i:>2}  cost {verdict['cost']:>9,}  floor {verdict['floor']}  {change}{problem}")
    print("Checkpoints (last valid step at or under each cap):")
    picked = pick_checkpoints(steps, caps)
    for cap, i in picked.items():
        if i is None:
            print(f"  cap {cap:>9,}: none (no valid step that cheap)")
            continue
        print(f"  cap {cap:>9,}: step {i} costs {steps[i]['cost']:,}")
        if write:
            out = PROPOSALS / f"{stem}_cap{cap}.txt"
            out.write_text(render(commanders, states[i]), encoding="utf-8")
            print(f"            wrote {out.relative_to(cl.ROOT)}")
    return picked


def main(argv):
    """Materialize the given ladders (default: every decks/proposals/*.ladder.txt)."""
    write = "--write" in argv
    caps = DEFAULT_CAPS
    if "--caps" in argv:
        caps = tuple(int(c) for c in argv[argv.index("--caps") + 1].split(","))
    skip = {argv[argv.index("--caps") + 1]} if "--caps" in argv else set()
    files = [Path(a) for a in argv if not a.startswith("--") and a not in skip] \
        or sorted(PROPOSALS.glob("*.ladder.txt"))
    if not files:
        print("No ladders: pass files or put them in decks/proposals/*.ladder.txt")
        return 2
    ctx = cl.build_context()
    if ctx is None:
        print("Missing the Scryfall bulk, the merged prices or the inventory (Phases 1 and 7 first).")
        return 2
    print(ctx["banner"] + "\n")
    for path in files:
        try:
            run(path, ctx, caps, write)
        except ValueError as exc:
            print(f"ERROR in {path.name}: {exc}")
            return 1
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
