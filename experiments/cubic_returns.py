"""Bounded exact T1 Cartesian-return and path diagnostics for T01.

Every candidate uses the same scalar set in both coordinates.  Three complete
pair-equivalent passes are charged: direct T1 membership, fiber adjacency, and
the difference-slice formula.  This is conservative relative to counting only
the N^2 direct polynomial/T1 evaluations.  No asymptotic inference is automatic.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import platform
import sys
import time

MAX_CANDIDATES = 140
MAX_INPUTS = 256
MAX_PAIR_CHECKS = 2_000_000
MAX_CPU_SECONDS = 60


def polynomial(x, y):
    return (x - y) ** 3 + x + y


def motion(x, y, tau=Q(1)):
    x, y, tau = Q(x), Q(y), Q(tau)
    u = x - y
    h = (u + tau) ** 3 - u ** 3
    return x + (tau - h) / 2, y - (tau + h) / 2


def inverse_coordinates(u, z):
    u, z = Q(u), Q(z)
    return (z - u ** 3 + u) / 2, (z - u ** 3 - u) / 2


def shift_c(u):
    return (3 * u * u + 3 * u + 2) / 2


class Budget:
    def __init__(self):
        self.candidates = 0
        self.pair_checks = 0
        self.polynomial_evaluations = 0
        self.start_cpu = time.process_time()

    def check(self):
        if time.process_time() - self.start_cpu > MAX_CPU_SECONDS:
            raise RuntimeError("Research CPU budget exhausted")

    def reserve(self, n):
        self.check()
        if n > MAX_INPUTS or n < 1:
            raise RuntimeError("Distinct input size outside declared bounds")
        if self.candidates >= MAX_CANDIDATES:
            raise RuntimeError("Candidate budget exhausted")
        if self.pair_checks + 3 * n * n > MAX_PAIR_CHECKS:
            raise RuntimeError("Pair-check budget exhausted before evaluation")
        self.candidates += 1
        self.pair_checks += 3 * n * n
        self.polynomial_evaluations += n * n


def ceil_root(n, degree):
    k = 1
    while k ** degree < n:
        k += 1
    return k


def analyze(values, budget):
    values = tuple(sorted(set(map(Q, values))))
    n = len(values)
    budget.reserve(n)
    index = {x: i for i, x in enumerate(values)}
    outputs = defaultdict(list)
    slices = defaultdict(set)
    successors = [-1] * (n * n)
    indegrees = [0] * (n * n)
    slice_direct_counts = Counter()
    for i, x in enumerate(values):
        for j, y in enumerate(values):
            u = x - y
            z = polynomial(x, y)
            vertex = i * n + j
            outputs[z].append((u, vertex))
            slices[u].add(y)
            # Expanded T1 coordinates, independently checked against motion
            # and conjugate coordinates in the targeted tests.
            x_next = y - (3 * u * u + u) / 2
            y_next = y - shift_c(u)
            if x_next in index and y_next in index:
                target = index[x_next] * n + index[y_next]
                successors[vertex] = target
                indegrees[target] += 1
                slice_direct_counts[u] += 1
        budget.check()
    if max(indegrees) > 1:
        raise AssertionError("T1 return graph has indegree greater than one")
    edge_count = sum(target >= 0 for target in successors)
    fiber_return_count = 0
    for pairs in outputs.values():
        us = {u for u, _ in pairs}
        if len(us) != len(pairs):
            raise AssertionError("A scalar output and difference fail to determine a unique pair")
        fiber_return_count += sum(u + 1 in us for u in us)
    slice_return_count = 0
    slice_records = []
    for u, anchors in sorted(slices.items()):
        next_anchors = slices.get(u + 1, set())
        count = sum(a - shift_c(u) in next_anchors for a in anchors)
        slice_return_count += count
        if count != slice_direct_counts[u]:
            raise AssertionError("Direct and difference-slice return counts disagree")
        slice_records.append({"difference": str(u), "anchor_indices": sorted(index[a] for a in anchors),
                              "mass": len(anchors), "returns": count})
    if not edge_count == fiber_return_count == slice_return_count:
        raise AssertionError("The three exact E1 formulas disagree")
    paths = []
    visited = set()
    for start in range(n * n):
        if indegrees[start] != 0:
            continue
        path = []
        vertex = start
        while vertex >= 0:
            if vertex in visited:
                raise AssertionError("Return graph contains a cycle or merged paths")
            visited.add(vertex)
            path.append(vertex)
            vertex = successors[vertex]
        paths.append(path)
    if len(visited) != n * n or len(paths) != n * n - edge_count:
        raise AssertionError("Path coverage or vertex-minus-edge count failed")
    path_sizes = Counter(map(len, paths))
    output_values = sorted(outputs)
    output_index = {z: i for i, z in enumerate(output_values)}
    pair_output = [-1] * (n * n)
    fibers = []
    for z in output_values:
        pairs = sorted(outputs[z])
        for _, vertex in pairs:
            pair_output[vertex] = output_index[z]
        fibers.append({"output": str(z), "differences": [str(u) for u, _ in pairs],
                       "vertices": [v for _, v in pairs], "size": len(pairs)})
    for path in paths:
        if len({pair_output[v] for v in path}) != 1:
            raise AssertionError("A return path changes scalar output")
    s = len(outputs)
    if s > len(paths):
        raise AssertionError("Image exceeds the number of return paths")
    thresholds = {"2": 2, "4": 4, "8": 8, "16": 16,
                  "ceil_N_quarter": ceil_root(n, 4), "ceil_sqrt_N": ceil_root(n, 2)}
    long_mass = {}
    for label, threshold in thresholds.items():
        mass = sum(size * count for size, count in path_sizes.items() if size >= threshold)
        long_mass[label] = {"minimum_vertices": threshold, "vertex_mass": mass,
                            "fraction": str(Q(mass, n * n))}
    forward_sum = sum(count * size * (size - 1) // 2 for size, count in path_sizes.items())
    result = {
        "inputs": list(map(str, values)), "N": n, "E1": edge_count,
        "return_density": str(Q(edge_count, n * n)),
        "E1_from_fibers": fiber_return_count, "E1_from_slices": slice_return_count,
        "components": len(paths), "vertices_minus_edges": n * n - edge_count,
        "path_vertex_size_distribution": {str(k): v for k, v in sorted(path_sizes.items())},
        "maximum_path_vertices": max(path_sizes),
        "maximum_forward_steps": max(path_sizes) - 1,
        "vertex_weighted_mean_forward_steps": str(Q(forward_sum, n * n)),
        "vertex_weighted_mean_path_vertices": str(Q(sum(k * k * v for k, v in path_sizes.items()), n * n)),
        "long_component_mass": long_mass,
        "image_size": s, "image_density": str(Q(s, n * n)),
        "maximum_actual_fiber": max(map(len, outputs.values())),
        "average_actual_fiber": str(Q(n * n, s)),
        "paths": paths, "pair_output_index": pair_output,
        "fibers": fibers, "difference_slices": slice_records,
        "charged_pair_checks": 3 * n * n, "polynomial_evaluations": n * n,
    }
    budget.check()
    return result


def orbit_set(z_values, u_values):
    return {coordinate for z, u in product(z_values, u_values)
            for coordinate in inverse_coordinates(u, z)}


def fixed_candidates():
    for h, n in product((Q(1), Q(1, 2), Q(1, 3), Q(2, 3), Q(2)), (4, 8, 16, 32, 64, 128)):
        yield f"ap_h{h}_n{n}", "arithmetic_progression", {h * j for j in range(n)}, {"h": str(h), "length": n}
    for n in (9, 17, 33, 65):
        yield f"symmetric_ap_n{n}", "symmetric_ap", set(map(Q, range(-(n // 2), n // 2 + 1))), {"length": n}
    for h, n, gap_kind in product((Q(1), Q(1, 3)), (4, 8, 16, 32), ("one", "n", "n_squared")):
        gap = {"one": Q(1), "n": Q(n), "n_squared": Q(n * n)}[gap_kind]
        offset = h * n + gap
        values = {h * j + shift for j, shift in product(range(n), (Q(0), offset))}
        yield f"two_blocks_h{h}_n{n}_gap{gap_kind}", "two_blocks", values, {"h": str(h), "block_length": n, "offset": str(offset)}
    sequences = {"square": lambda j: Q(j * j), "shift_c": lambda j: shift_c(Q(j)),
                 "cube": lambda j: Q(j ** 3), "cubic_coordinate": lambda j: Q(j ** 3 - j, 2)}
    for kind, n in product(sequences, (4, 8, 16, 32, 64)):
        yield f"sequence_{kind}_n{n}", "polynomial_sequence", {sequences[kind](j) for j in range(n)}, {"sequence": kind, "parameter_length": n}
    for offset, length in product((Q(0), Q(1, 3)), (2, 4, 8, 16, 32)):
        us = [Q(j) + offset for j in range(-length, length + 1)]
        zs = [Q(0)]
        yield f"orbit_single_offset{offset}_L{length}", "single_orbit", orbit_set(zs, us), {"outputs": ["0"], "u_offset": str(offset), "L": length, "designed_pairs": len(us), "coordinate_occurrences": 2 * len(us)}
    multi_parameters = [(2, length) for length in (2, 4, 8, 16)] + [(4, length) for length in (2, 4, 8)]
    for m, length in multi_parameters:
        us = list(map(Q, range(-length, length + 1)))
        zs = [Q(2 * k) for k in range(m)]
        yield f"orbit_multi_M{m}_L{length}", "multiple_orbits", orbit_set(zs, us), {"outputs": list(map(str, zs)), "L": length, "designed_pairs": len(zs) * len(us), "coordinate_occurrences": 2 * len(zs) * len(us)}
    for kind in ("square", "cubic_minus_linear"):
        zs = sorted({Q(k * k if kind == "square" else k ** 3 - k) for k in range(4)})
        us = list(map(Q, range(-8, 9)))
        yield f"orbit_outputs_{kind}_L8", "multiple_orbits", orbit_set(zs, us), {"outputs": list(map(str, zs)), "L": 8, "designed_pairs": len(zs) * len(us), "coordinate_occurrences": 2 * len(zs) * len(us)}


def compact(record):
    excluded = {"inputs", "paths", "pair_output_index", "fibers", "difference_slices"}
    return {k: v for k, v in record.items() if k not in excluded}


def run(output_directory, example_path):
    budget = Budget()
    wall_start = time.perf_counter()
    if output_directory.exists():
        raise RuntimeError("Refusing to overwrite an existing research run directory")
    output_directory.mkdir(parents=True)
    definitions = list(fixed_candidates())
    if len(definitions) != 97:
        raise AssertionError("Declared fixed candidate inventory changed")
    preflight = {"fixed_candidates": len(definitions),
                 "fixed_pair_checks": sum(3 * len(a) ** 2 for _, _, a, _ in definitions),
                 "greedy_candidates": 33, "greedy_pair_checks": 3 * (17 * 16 ** 2 + 16 * 15 ** 2),
                 "maximum_fixed_input_size": max(len(a) for _, _, a, _ in definitions)}
    if preflight["fixed_pair_checks"] + preflight["greedy_pair_checks"] > MAX_PAIR_CHECKS:
        raise RuntimeError("Entire planned run exceeds pair-check allocation")
    summaries, errors = [], []

    def evaluate(identifier, family, values, parameters):
        record = analyze(values, budget)
        record.update({"id": identifier, "family": family, "parameters": parameters})
        if "designed_pairs" in parameters:
            record["designed_pair_fraction"] = str(Q(parameters["designed_pairs"], record["N"] ** 2))
            record["scalar_coordinate_reuse"] = str(Q(parameters["coordinate_occurrences"], record["N"]))
        filename = identifier.replace("/", "over") + ".json"
        path = output_directory / filename
        path.write_text(json.dumps(record, indent=2) + "\n")
        record["raw_path"] = str(path)
        record["raw_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        summaries.append(compact(record))
        budget.check()
        return record

    try:
        for identifier, family, values, parameters in definitions:
            evaluate(identifier, family, values, parameters)
        current = set(map(Q, range(-8, 9)))
        for stage in (1, 2):
            trials = []
            for removed in sorted(current):
                trials.append(evaluate(f"greedy_stage{stage}_remove{removed}", "greedy_deletion",
                                       current - {removed}, {"stage": stage, "removed": str(removed), "starting_inputs": list(map(str, sorted(current)))}))
            winner = min(trials, key=lambda r: (-r["E1"], tuple(map(Q, r["inputs"]))))
            current = set(map(Q, winner["inputs"]))
    except Exception as error:
        errors.append({"type": type(error).__name__, "message": str(error), "completed_candidates": len(summaries)})
    summary = {"date": "2026-09-21", "status": "EXPERIMENTAL exact; only the declared finite candidates",
               "polynomial": "(x-y)^3+x+y", "tau": "1", "preflight": preflight,
               "candidates": summaries, "errors": errors,
               "path_length_convention": "Path size counts vertices. Forward length counts edges from a vertex to its path endpoint; means weight each of N^2 vertices once.",
               "budget_counting": "Three N^2-equivalent exact checks per candidate: direct membership, fiber adjacency, and difference-slice membership. Only the direct pass evaluates P, N^2 times.",
               "greedy_rule": "Two rounds deleting one point from {-8,...,8}; evaluate every deletion, maximize E1 at that fixed cardinality, choose lexicographically smallest set on ties.",
               "limitations": ["Finite evidence does not determine R1(N) asymptotically.", "A long planted orbit may occupy negligible Cartesian pair mass.", "Different path components may share the same scalar output."]}
    example_path.write_text(json.dumps(summary, indent=2) + "\n")
    provenance = {"date": "2026-09-21", "command": "python3 -m experiments.cubic_returns", "python": sys.version,
                  "implementation": platform.python_implementation(), "network": "none", "randomness": "none",
                  "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "summary_sha256": hashlib.sha256(example_path.read_bytes()).hexdigest(),
                  "fixed_inputs_sha256": hashlib.sha256(json.dumps([[i, f, list(map(str, sorted(a))), p] for i, f, a, p in definitions], sort_keys=True).encode()).hexdigest(),
                  "budget_limits": {"candidates": MAX_CANDIDATES, "inputs": MAX_INPUTS, "pair_checks": MAX_PAIR_CHECKS, "cpu_seconds": MAX_CPU_SECONDS},
                  "actual": {"candidates": budget.candidates, "pair_checks": budget.pair_checks,
                             "polynomial_evaluations": budget.polynomial_evaluations,
                             "cpu_seconds": time.process_time() - budget.start_cpu, "wall_seconds": time.perf_counter() - wall_start},
                  "errors": errors, "preflight": preflight}
    (output_directory / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    best = sorted(summaries, key=lambda r: (-Q(r["return_density"]), r["id"]))[:10]
    print(json.dumps({"actual": provenance["actual"], "errors": errors,
                      "best_return_density": [{k: r[k] for k in ("id", "N", "E1", "return_density", "maximum_path_vertices", "image_size")} for r in best]}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path, default=Path("local-only/runs/T01/2026-09-21-cubic-returns"))
    parser.add_argument("--example", type=Path, default=Path("examples/2026-09-21-cubic-returns.json"))
    args = parser.parse_args()
    run(args.output_directory, args.example)


if __name__ == "__main__":
    main()
