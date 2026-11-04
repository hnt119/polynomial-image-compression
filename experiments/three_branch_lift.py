"""Bounded exact rational experiments for T01's three-branch lift.

Every accepted gadget records all scalar outputs and their nine-block membership
masks.  Intersecting any collection of blocks means selecting masks containing
all its bits, so this is a lossless certificate for every higher intersection.
No finite result is a uniform recursive or asymptotic claim.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
import platform
import sys
import time

Q = Fraction
MAX_GADGETS = 1000


def polynomial(x: Q, y: Q) -> Q:
    return (x - y) ** 3 + x + y


def image(values):
    return {polynomial(x, y) for x, y in product(values, repeat=2)}


def encoded(values):
    return [str(x) for x in sorted(values)]


def analyze(seed, maps, identifier):
    """Return exact data even for rejected (non-disjoint) branch systems."""
    seed = tuple(sorted(set(map(Q, seed))))
    maps = tuple((Q(scale), Q(shift)) for scale, shift in maps)
    branches = [{scale * x + shift for x in seed} for scale, shift in maps]
    enlarged = set().union(*branches)
    injective = [len(branch) == len(seed) for branch in branches]
    disjoint = all(not (branches[r] & branches[s]) for r in range(3)
                   for s in range(r + 1, 3))
    base = {
        "id": identifier, "seed": encoded(seed),
        "maps": [[str(a), str(b)] for a, b in maps],
        "branches": [encoded(branch) for branch in branches],
        "branch_injective": injective, "branch_disjoint": disjoint,
        "n": len(seed), "n_prime": len(enlarged),
        "accepted": all(injective) and disjoint,
    }
    if not base["accepted"]:
        return base
    old_image = image(seed)
    blocks = [{polynomial(x, y) for x in branches[r] for y in branches[s]}
              for r, s in product(range(3), repeat=2)]
    complete = set().union(*blocks)
    masks = {z: sum(1 << j for j, block in enumerate(blocks) if z in block)
             for z in complete}
    mask_sizes = Counter(masks.values())
    pairwise = [[len(blocks[i] & blocks[j]) for j in range(9)]
                for i in range(9)]
    summed = sum(map(len, blocks))
    base.update({
        "old_image": encoded(old_image), "s": len(old_image),
        "s_prime": len(complete),
        "image_ratio": str(Q(len(complete), len(old_image))),
        "normalized_ratio": str(Q(len(complete), 9 * len(old_image))),
        "block_order": [[r, s] for r, s in product(range(3), repeat=2)],
        "block_sizes": list(map(len, blocks)),
        "block_images": [encoded(block) for block in blocks],
        "complete_image": encoded(complete),
        "membership_masks": [[str(z), masks[z]] for z in sorted(complete)],
        "membership_mask_counts": {str(k): v for k, v in sorted(mask_sizes.items())},
        "pairwise_intersections": pairwise,
        "sum_block_sizes": summed,
        "union_to_block_sum": str(Q(len(complete), summed)),
        "overlap_saving": summed - len(complete),
    })
    return base


def grid():
    """Exactly 980 attempts, with <=6 seed inputs and <=18 enlarged input values."""
    seeds = [(f"ap_{n}", tuple(map(Q, range(n)))) for n in range(2, 7)]
    seeds += [(f"half_ap_{n}", tuple(Q(j, 2) for j in range(n)))
              for n in range(2, 7)]
    seeds += [
        ("sparse_013", (Q(0), Q(1), Q(3))),
        ("sparse_0124", (Q(0), Q(1), Q(2), Q(4))),
        ("double_ap_2", (Q(0), Q(2))),
        ("mixed_half", (Q(0), Q(1, 2), Q(1), Q(2))),
    ]
    for name, seed in seeds:
        for scale, shift in product(
                (Q(1, 3), Q(1, 2), Q(1), Q(2), Q(3)),
                (Q(1, 3), Q(1, 2), Q(1), Q(2), Q(3), Q(4), Q(6))):
            maps = tuple((scale, r * shift) for r in range(3))
            yield f"{name}:common:{scale}:{shift}", seed, maps
        patterns = ((1, 1, 2), (1, 2, 1), (1, 2, 3), (1, -1, 1),
                    (1, -1, 2), (Q(1, 2), 1, 2), (2, 1, Q(1, 2)))
        for index, scales in enumerate(patterns):
            for shift in (Q(1, 2), Q(1), Q(2), Q(3), Q(4)):
                maps = tuple((scales[r], r * shift) for r in range(3))
                yield f"{name}:unequal:{index}:{shift}", seed, maps


def summarize(record):
    keys = ("id", "n", "n_prime", "s", "s_prime", "image_ratio",
            "normalized_ratio", "sum_block_sizes", "union_to_block_sum",
            "overlap_saving")
    return {key: record[key] for key in keys}


def run(output_directory, example_path):
    start = time.perf_counter()
    output_directory.mkdir(parents=True, exist_ok=True)
    records = []
    for identifier, seed, maps in grid():
        if len(records) >= MAX_GADGETS:
            raise RuntimeError("Finite computation budget exceeded")
        if len(seed) > 6:
            raise RuntimeError("Seed size budget exceeded")
        records.append(analyze(seed, maps, identifier))
    accepted = [record for record in records if record["accepted"]]
    ranking = sorted(accepted, key=lambda r: (Q(r["normalized_ratio"]), r["id"]))
    # These representative mechanisms are fixed before adaptive ranking.
    representative_ids = (
        "double_ap_2:common:1/2:2",
        "half_ap_2:common:2:2",
        "half_ap_2:common:1/3:1/3",
        "ap_2:common:1:2",
    )
    by_id = {record["id"]: record for record in records}
    representatives = [by_id[identifier] for identifier in representative_ids]
    if not all(record["accepted"] for record in representatives):
        raise AssertionError("Preselected representative unexpectedly rejected")
    compositions = []
    for label, maps in (("repeat", [(Q(1, 2), 2 * r) for r in range(3)]),
                        ("ap18", [(Q(1), 6 * r) for r in range(3)])):
        record = representatives[0]
        seed = sorted({Q(x) for branch in record["branches"] for x in branch})
        composed = analyze(seed, maps, record["id"] + ":" + label)
        if composed["n_prime"] > 54:
            raise RuntimeError("One-further-composition size budget exceeded")
        compositions.append(composed)
    raw = {
        "status": "EXPERIMENTAL — exact, exhaustive only over the stated grid",
        "polynomial": "(x-y)^3+x+y", "arithmetic": "fractions.Fraction",
        "attempted": len(records), "accepted": len(accepted),
        "rejected": len(records) - len(accepted), "records": records,
        "one_further_compositions": compositions,
    }
    raw_path = output_directory / "complete-gadgets.json"
    raw_path.write_text(json.dumps(raw, indent=2) + "\n")
    summary = {
        "status": raw["status"], "polynomial": raw["polynomial"],
        "attempted": len(records), "accepted": len(accepted),
        "rejected": len(records) - len(accepted),
        "strict_normalized_gain": sum(Q(r["normalized_ratio"]) < 1 for r in accepted),
        "best_ten": [summarize(r) for r in ranking[:10]],
        "representatives": representatives,
        "one_further_compositions": compositions,
        "all_counts": [summarize(r) for r in accepted],
        "local_complete_data": str(raw_path),
        "grid": {"seed_count": 14, "common_scale_choices": ["1/3", "1/2", "1", "2", "3"],
                 "common_shift_choices": ["1/3", "1/2", "1", "2", "3", "4", "6"],
                 "unequal_scale_patterns": [[str(x) for x in p] for p in
                     ((1, 1, 2), (1, 2, 1), (1, 2, 3), (1, -1, 1),
                      (1, -1, 2), (Q(1, 2), 1, 2), (2, 1, Q(1, 2)))],
                 "unequal_shift_choices": ["1/2", "1", "2", "3", "4"]},
    }
    # Include the strongest observed finite gadget as a complete certificate.
    if ranking[0]["id"] not in representative_ids:
        summary["representatives"].append(ranking[0])
    example_path.parent.mkdir(parents=True, exist_ok=True)
    example_path.write_text(json.dumps(summary, indent=2) + "\n")
    provenance = {
        "date": "2026-09-16", "python": sys.version,
        "implementation": platform.python_implementation(),
        "command": "python3 -m experiments.three_branch_lift",
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "raw_sha256": hashlib.sha256(raw_path.read_bytes()).hexdigest(),
        "summary_sha256": hashlib.sha256(example_path.read_bytes()).hexdigest(),
        "grid_input_sha256": hashlib.sha256(json.dumps([
            [identifier, encoded(seed), [[str(a), str(b)] for a, b in maps]]
            for identifier, seed, maps in grid()
        ], sort_keys=True).encode()).hexdigest(),
        "runtime_seconds": time.perf_counter() - start,
        "network": "none", "randomness": "none", "errors": [],
        "budget": {"attempts": 1000, "actual_attempts": len(records),
                   "maximum_seed_size": 6, "maximum_enlarged_size": 18,
                   "one_further_composition_limit": 2,
                   "actual_one_further_compositions": len(compositions),
                   "maximum_composed_size": 54},
        "limitations": ["Only the specified rational affine grid was searched.",
                        "Rejected non-disjoint branch systems have no block-image computation.",
                        "Finite savings do not prove a uniform recursive support bound.",
                        "One selected gadget was continued twice by predetermined maps; no deeper search."],
    }
    (output_directory / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps({key: summary[key] for key in (
        "attempted", "accepted", "rejected", "strict_normalized_gain", "best_ten")}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path,
                        default=Path("local-only/runs/T01/2026-09-16-three-branch-lift"))
    parser.add_argument("--example", type=Path,
                        default=Path("examples/2026-09-16-three-branch-lift.json"))
    args = parser.parse_args()
    run(args.output_directory, args.example)


if __name__ == "__main__":
    main()
