#!/usr/bin/env python3
"""Ablation ladder: lists of one commander that are known to be weaker than its reference, to be
scored on Commander Salt (power-scale v1.0, calibration in Phase 5).

Run it with the "Run Python File" button (no arguments). No network. For every commander that has
both files below it writes the nested ladder k = 2, 4, 6, 10, 20 into evals/anchors/:

  evals/anchors/<slug>.reference.txt      the accepted reference list (`1 Card Name` per line)
  evals/anchors/<slug>.slot-ranking.json  {"ranking": [{name, role, importance_rank}],
                                           "fillers": {role: [weaker same-role cards, weakest first]}}

Output:
  evals/anchors/<slug>.ladder-k<NN>.txt   the reference with its k most important non-land cards
                                          replaced
  evals/anchors/<slug>.ladder.json        the replaced pairs and the Layer A result of every rung;
                                          the power of each rung is read from Commander Salt

Rule (fixed before any candidate is seen, no prices, no community data): walk the ranking from the
most important card down; each card is replaced by the first unused filler of its own role
(falling back to the role "other"); the lands never change. The sets are nested because rung k uses
the first k pairs of one walk.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layer_a as la  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ANCHORS = ROOT / "evals" / "anchors"
K_VALUES = (2, 4, 6, 10, 20)
FALLBACK_ROLE = "other"


def walk(ranking, fillers, in_list, max_k):
    """The ordered replacement pairs [(out_name, in_name, role)] for the first max_k ranked cards."""
    used = set(in_list)
    pairs = []
    for entry in sorted(ranking, key=lambda e: e["importance_rank"])[:max_k]:
        role = entry["role"]
        for pool_role in (role, FALLBACK_ROLE):
            pick = next((n for n in fillers.get(pool_role, []) if n not in used), None)
            if pick is not None:
                break
        if pick is None:
            raise ValueError(f"no unused filler left for {entry['name']} (role {role})")
        used.add(pick)
        pairs.append((entry["name"], pick, role))
    return pairs


def render(commander_lines, main_entries, replace):
    """Decklist text with `replace` (out name -> in name) applied to the main entries."""
    out = ["// Commander"] + commander_lines + [""]
    out += [f"{qty} {replace.get(name, name)}" for qty, name in main_entries]
    return "\n".join(out) + "\n"


def ladder(commander_lines, main_entries, ranking, fillers, k_values=K_VALUES):
    """Return {k: (decklist text, pairs used)}."""
    names = [name for _, name in main_entries]
    pairs = walk(ranking, fillers, names, max(k_values))
    result = {}
    for k in k_values:
        chosen = pairs[:k]
        result[k] = (render(commander_lines, main_entries, {o: i for o, i, _ in chosen}), chosen)
    return result


def split_list(text):
    """(commander lines, [(qty, name)]) of a decklist file."""
    commanders, main, bad = la.parse_decklist(text)
    if bad:
        raise ValueError(f"unparsed lines: {bad[:3]}")
    return ([f"{e['qty']} {e['name']}" for e in commanders],
            [(e["qty"], e["name"]) for e in main])


def gate(text, slug, index, spellbook, hazards):
    """Layer A summary of one list (floor and rejection reasons)."""
    commanders, main, _ = la.parse_decklist(text)
    report, _ = la.analyze(commanders, main, index, slug, spellbook, hazards,
                           la.TARGET_BRACKET.get(slug, la.DEFAULT_TARGET))
    return {"floor": report["floor"], "rejected": report["rejected"], "reasons": report["reasons"],
            "floor_ok_so_far": report["floor_ok_so_far"]}


def main():
    """Write the ladder of every commander that has a reference and a slot ranking."""
    found = [(s, ANCHORS / f"{s}.reference.txt", ANCHORS / f"{s}.slot-ranking.json")
             for s in la.COMMANDERS]
    found = [(s, r, k) for s, r, k in found if r.exists() and k.exists()]
    if not found:
        print("No evals/anchors/<slug>.reference.txt with a .slot-ranking.json yet.")
        sys.exit(2)
    bulk = la.latest_bulk()
    index = la.build_index(list(la.iter_cards(bulk))) if bulk else None
    spellbook = la.load_spellbook() if la.SPELLBOOK_SLIM.exists() else None
    hazards = la.load_hazards()
    for slug, ref_path, rank_path in found:
        data = json.loads(rank_path.read_text(encoding="utf-8"))
        commander_lines, main_entries = split_list(ref_path.read_text(encoding="utf-8-sig"))
        rungs = ladder(commander_lines, main_entries, data["ranking"], data["fillers"])
        manifest = {"slug": slug, "rungs": {}}
        print(f"== {slug}")
        for k, (text, pairs) in rungs.items():
            (ANCHORS / f"{slug}.ladder-k{k:02d}.txt").write_text(text, encoding="utf-8")
            row = {"k": k,
                   "pairs": [{"out": o, "in": i, "role": r} for o, i, r in pairs]}
            if index is not None:
                row["layer_a"] = gate(text, slug, index, spellbook, hazards)
            manifest["rungs"][str(k)] = row
            flag = row.get("layer_a", {})
            print(f"   k={k:2d}  floor {flag.get('floor')}  "
                  f"rejected {flag.get('rejected')}")
        (ANCHORS / f"{slug}.ladder.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"   wrote evals/anchors/{slug}.ladder.json and 5 ladder lists")


if __name__ == "__main__":
    main()
