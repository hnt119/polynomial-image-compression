"""Exact, bounded continuation diagnostics for the six-point T01 gadget.

Nine rules, three successive levels each, no parameter search.  Full JSON
certificates retain every scalar output, unique ordered-pair fiber, nine-block
membership, and difference slice.  Extra coincidences mean only "not explained
by the two specified identity templates"; they need not be accidental.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from math import gcd
from pathlib import Path
import platform
import sys
import time

MAX_STEPS = 120
MAX_RULES = 16
MAX_INPUTS = 162
MAX_EVALUATIONS = 3_000_000
MAX_CPU_SECONDS = 90
LEVELS = 3
GADGET = tuple(Q(i, 3) for i in range(6))
RULES = (
    "intact_near_gap", "intact_wide_gap", "half_near_gap",
    "intact_third_shift", "half_third_shift", "alternating_scale",
    "stage_shrink", "diameter_reset", "exact_third_translations",
)


class Budget:
    """Preflight every evaluation batch; count actual polynomial calls."""

    def __init__(self):
        self.evaluations = 0
        self.steps = 0
        self.start_cpu = time.process_time()

    def check(self):
        if time.process_time() - self.start_cpu > MAX_CPU_SECONDS:
            raise RuntimeError("Research CPU budget exhausted")

    def preflight(self, evaluations, inputs, continuation=True):
        self.check()
        if inputs > MAX_INPUTS:
            raise RuntimeError("Distinct input cardinality budget exceeded")
        if self.evaluations + evaluations > MAX_EVALUATIONS:
            raise RuntimeError("Polynomial evaluation budget exceeded")
        if continuation:
            if self.steps >= MAX_STEPS:
                raise RuntimeError("Continuation step budget exceeded")
            self.steps += 1

    def polynomial(self, x, y):
        self.evaluations += 1
        if self.evaluations > MAX_EVALUATIONS:
            raise RuntimeError("Polynomial evaluation budget exceeded")
        if self.evaluations % 4096 == 0:
            self.check()
        return (x - y) ** 3 + x + y


def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def fresh_prime(last_prime, values, lower_bound=Q(4)):
    candidate = max(5, last_prime + 1, lower_bound.numerator // lower_bound.denominator + 1)
    while not is_prime(candidate) or any(Q(x).denominator % candidate == 0 for x in values):
        candidate += 1
    return candidate


def choose_maps(rule, values, stage, last_prime):
    diameter = max(values) - min(values)
    if rule == "exact_third_translations":
        # The input 1/(3*product(previous p)) ensures a new p denominator
        # survives, while diameter/p<1/3 gives disjoint branch intervals.
        p = fresh_prime(last_prime, values, 3 * diameter)
        return [(Q(1, p), Q(r, 3)) for r in range(3)], p
    scale = {
        "intact_near_gap": Q(1), "intact_wide_gap": Q(1),
        "half_near_gap": Q(1, 2), "intact_third_shift": Q(1),
        "half_third_shift": Q(1, 2),
        "alternating_scale": Q(2) if stage % 2 else Q(1, 2),
        "stage_shrink": Q(1, stage + 1),
        "diameter_reset": Q(5, 3) / diameter,
    }[rule]
    scaled = [scale * x for x in values]
    if rule in ("intact_near_gap", "half_near_gap"):
        offset = scale * diameter
    elif rule == "intact_wide_gap":
        offset = diameter + 1
    else:
        offset = Q(1, 3)
    p = fresh_prime(last_prime, scaled + [offset, scale])
    shift = offset + Q(1, p)
    return [(scale, r * shift) for r in range(3)], p


def arithmetic_profile(values):
    denominator = 1
    for x in values:
        denominator = denominator * x.denominator // gcd(denominator, x.denominator)
    return {
        "minimum": str(min(values)), "maximum": str(max(values)),
        "diameter": str(max(values) - min(values)),
        "common_denominator": str(denominator),
        "maximum_reduced_numerator": str(max(abs(x.numerator) for x in values)),
        "maximum_reduced_denominator": str(max(x.denominator for x in values)),
    }


def certificate(values, pair_values, blocks):
    """Lossless scalar-output encoding; all multiplicities use unique pairs."""
    values = tuple(sorted(values))
    n = len(values)
    index = {x: i for i, x in enumerate(values)}
    outputs = sorted(set(pair_values.values()))
    output_index = {z: i for i, z in enumerate(outputs)}
    fibers = [[] for _ in outputs]
    parent = list(range(n * n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(pair_a, pair_b):
        a = index[pair_a[0]] * n + index[pair_a[1]]
        b = index[pair_b[0]] * n + index[pair_b[1]]
        if pair_values[pair_a] != pair_values[pair_b]:
            raise AssertionError("Claimed identity does not preserve scalar output")
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    edges = {"unit_difference": [], "third_difference": []}
    for t in values:
        for sign in (-1, 1):
            if t + sign in index:
                a, b = (t, t), (t, t + sign)
                union(a, b)
                edges["unit_difference"].append([index[x] for x in a + b])
            if t + Q(sign, 3) in index and t + Q(2 * sign, 3) in index:
                a, b = (t + Q(sign, 3), t), (t, t + Q(2 * sign, 3))
                union(a, b)
                edges["third_difference"].append([index[x] for x in a + b])
    pair_table = []
    slices = defaultdict(list)
    for i, x in enumerate(values):
        row = []
        for j, y in enumerate(values):
            k = output_index[pair_values[x, y]]
            row.append(k)
            fibers[k].append(i * n + j)
            slices[x - y].append([j, k])
        pair_table.append(row)
    components = []
    classifications = []
    for fiber in fibers:
        sizes = sorted(Counter(find(pair) for pair in fiber).values())
        components.append(sizes)
        if len(fiber) == 1:
            classifications.append("singleton")
        elif len(sizes) == 1:
            classifications.append("template_only")
        elif max(sizes) == 1:
            classifications.append("extra_only")
        else:
            classifications.append("mixed")
    template_components = sum(map(len, components))
    block_ids = [sorted(output_index[z] for z in block) for block in blocks]
    masks = [sum(1 << b for b, block in enumerate(blocks) if z in block) for z in outputs]
    return {
        "inputs": list(map(str, values)), "n": n, "s": len(outputs),
        "outputs": list(map(str, outputs)),
        "pair_output_index": pair_table,
        "output_multiplicities": list(map(len, fibers)),
        "fiber_template_component_sizes": components,
        "fiber_classification": classifications,
        "fiber_classification_counts": dict(Counter(classifications)),
        "template_edges": edges,
        "template_savings": n * n - template_components,
        "extra_savings": template_components - len(outputs),
        "total_savings": n * n - len(outputs),
        "template_covered_pair_count": sum(sum(c for c in sizes if c > 1) for sizes in components),
        "block_order": [[r, s] for r, s in product(range(3), repeat=2)] if len(blocks) == 9 else [],
        "block_output_indices": block_ids,
        "block_sizes": list(map(len, blocks)),
        "sum_block_sizes": sum(map(len, blocks)),
        "block_membership_masks": masks,
        "pairwise_block_intersections": [[len(a & b) for b in blocks] for a in blocks],
        "difference_slices": [
            {"difference": str(d), "anchor_and_output_indices": sorted(rows), "mass": len(rows)}
            for d, rows in sorted(slices.items())
        ],
        "arithmetic_profile": arithmetic_profile(values),
    }


def initial_certificate(budget):
    budget.preflight(len(GADGET) ** 2, len(GADGET), continuation=False)
    pairs = {(x, y): budget.polynomial(x, y) for x, y in product(GADGET, repeat=2)}
    return certificate(GADGET, pairs, [])


def analyze_level(old_values, old_s, maps, budget):
    branches = [{a * x + b for x in old_values} for a, b in maps]
    values = sorted(set().union(*branches))
    evaluation_cost = sum(len(a) * len(b) for a in branches for b in branches)
    budget.preflight(evaluation_cost, len(values))
    before = budget.evaluations
    pair_values = {}
    blocks = []
    for a, b in product(branches, repeat=2):
        block = set()
        for x, y in product(a, b):
            value = budget.polynomial(x, y)
            block.add(value)
            pair_values[x, y] = value
        blocks.append(block)
    if budget.evaluations - before != evaluation_cost:
        raise AssertionError("Evaluation accounting mismatch")
    if len(pair_values) != len(values) ** 2:
        raise AssertionError("Incomplete same-set Cartesian coverage")
    result = certificate(values, pair_values, blocks)
    n_old, n_new = len(old_values), len(values)
    lam = Q(n_new, n_old)
    rho = Q(result["s"], old_s)
    result.update({
        "old_n": n_old, "old_s": old_s,
        "maps": [[str(a), str(b)] for a, b in maps],
        "branch_inputs": [list(map(str, sorted(branch))) for branch in branches],
        "branch_injective": [len(b) == n_old for b in branches],
        "branches_pairwise_disjoint": sum(map(len, branches)) == n_new,
        "lambda": str(lam), "rho": str(rho),
        "normalized_ratio": str(rho / (lam * lam)),
        "image_density": str(Q(result["s"], n_new * n_new)),
        "polynomial_evaluations": evaluation_cost,
        "unique_pair_count": n_new * n_new,
        "repeated_branch_pair_evaluations": evaluation_cost - n_new * n_new,
    })
    budget.check()
    return result


def compact(record):
    keys = ("rule", "stage", "fresh_prime", "old_n", "old_s", "n", "s",
            "maps", "branches_pairwise_disjoint", "lambda", "rho", "normalized_ratio",
            "image_density", "template_savings", "extra_savings", "total_savings",
            "template_covered_pair_count", "fiber_classification_counts", "sum_block_sizes",
            "polynomial_evaluations", "unique_pair_count", "repeated_branch_pair_evaluations",
            "arithmetic_profile", "raw_path", "raw_sha256")
    return {key: record[key] for key in keys}


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def run(output_directory, example_path):
    if len(RULES) > MAX_RULES:
        raise RuntimeError("Rule budget exceeded")
    budget = Budget()
    wall_start = time.perf_counter()
    output_directory.mkdir(parents=True, exist_ok=True)
    if any(output_directory.glob("*-level-*.json")):
        raise RuntimeError("Existing continuation run found; refusing to overwrite research data")
    base = initial_certificate(budget)
    write_json(output_directory / "initial-gadget.json", base)
    summaries = []
    errors = []
    stops = []
    for rule in RULES:
        values, old_s, last_prime = list(GADGET), base["s"], 3
        for stage in range(1, LEVELS + 1):
            try:
                maps, prime = choose_maps(rule, values, stage, last_prime)
                record = analyze_level(values, old_s, maps, budget)
                record.update({"rule": rule, "stage": stage, "fresh_prime": prime})
                path = output_directory / f"{rule}-level-{stage}.json"
                write_json(path, record)
                record.update({"raw_path": str(path),
                               "raw_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
                summaries.append(compact(record))
                values, old_s, last_prime = list(map(Q, record["inputs"])), record["s"], prime
            except Exception as error:
                errors.append({"rule": rule, "stage": stage, "error": str(error)})
                break
        stops.append({"rule": rule, "last_completed_stage": sum(r["rule"] == rule for r in summaries),
                      "reason": "Prespecified three-level diagnostic completed; no asymptotic inference"})
    summary = {
        "status": "EXPERIMENTAL — exact predetermined finite continuations only",
        "polynomial": "(x-y)^3+x+y", "initial_input": list(map(str, GADGET)),
        "initial_s": base["s"], "rules": list(RULES), "levels_per_rule": LEVELS,
        "all_counts": summaries, "stops": stops, "errors": errors,
        "exclusions_without_enumeration": [
            {"rule": "literal x/2+r/3 repetition", "reason": "Root analytical classification; no rerun"},
            {"rule": "fixed-spacing progression tripling", "reason": "TB-P1 from previous report gives s/n^2 tending to1; stopped before enumeration"},
        ],
        "theorem_scope": "All nine evaluated rules introduce a fresh denominator prime at every level, so the fixed-prime-support hypothesis of reported T01.6 does not hold. This gives no positive support bound.",
        "template_convention": "Only P(t,t)=P(t,t±1) and P(t±1/3,t)=P(t,t±2/3) generate the union-find equivalence. Extra savings are not explained by those templates, and are not asserted accidental.",
    }
    write_json(example_path, summary)
    provenance = {
        "date": "2026-09-16", "command": "python3 -m experiments.three_branch_continuation",
        "python": sys.version, "implementation": platform.python_implementation(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "summary_sha256": hashlib.sha256(example_path.read_bytes()).hexdigest(),
        "initial_gadget_sha256": hashlib.sha256((output_directory / "initial-gadget.json").read_bytes()).hexdigest(),
        "input_rule_sha256": hashlib.sha256(json.dumps({"rules": RULES, "levels": LEVELS,
                                                       "initial": list(map(str, GADGET))}, sort_keys=True).encode()).hexdigest(),
        "budget_limits": {"rules": MAX_RULES, "steps": MAX_STEPS, "distinct_inputs": MAX_INPUTS,
                          "polynomial_evaluations": MAX_EVALUATIONS, "cpu_seconds": MAX_CPU_SECONDS},
        "actual": {"rules": len(RULES), "steps": budget.steps,
                   "polynomial_evaluations": budget.evaluations,
                   "cpu_seconds": time.process_time() - budget.start_cpu,
                   "wall_seconds": time.perf_counter() - wall_start},
        "errors": errors, "network": "none", "randomness": "none",
        "counting": "Every polynomial evaluation, including repeated branch-labelled copies of identical scalar ordered pairs, is charged. Output multiplicities use each unique scalar ordered pair exactly once.",
        "interpretation": "This run does not establish an all-level recurrence, asymptotic saving, novelty, or arithmetic amplification.",
    }
    write_json(output_directory / "provenance.json", provenance)
    print(json.dumps({"actual": provenance["actual"], "errors": errors,
                      "rows": [{k: r[k] for k in ("rule", "stage", "n", "s", "normalized_ratio", "template_savings", "extra_savings")} for r in summaries]}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path,
                        default=Path("local-only/runs/T01/2026-09-16-three-branch-continuation"))
    parser.add_argument("--example", type=Path,
                        default=Path("examples/2026-09-16-three-branch-continuation.json"))
    args = parser.parse_args()
    run(args.output_directory, args.example)


if __name__ == "__main__":
    main()
