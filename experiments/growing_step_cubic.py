"""Exact bounded growing-step graphs for P=(x-y)^3+x+y.

Enumerate full scalar fibers once per carrier.  Candidate steps and every edge
come from actual differences within those fibers.  The all-useful-step graph is
a diagnostic benchmark, not an independently small-support certificate.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
import hashlib
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path
import platform
import sys
import time

MAX_CARRIERS = 60
MAX_CASES = 200
MAX_INPUTS = 128
MAX_CHECKS = 2_000_000
MAX_CPU_SECONDS = 60


def polynomial(x, y):
    return (x - y) ** 3 + x + y


def motion(x, y, tau):
    x, y, tau = Q(x), Q(y), Q(tau)
    u = x - y
    h = (u + tau) ** 3 - u ** 3
    return x + (tau - h) / 2, y - (tau + h) / 2


def orbit_coordinates(z, u):
    return (z - u ** 3 + u) / 2, (z - u ** 3 - u) / 2


def ceil_root(n, degree):
    result = 1
    while result ** degree < n:
        result += 1
    return result


class Budget:
    def __init__(self):
        self.checks = Counter()
        self.carriers = 0
        self.cases = 0
        self.start_cpu = time.process_time()

    def time_check(self):
        if time.process_time() - self.start_cpu > MAX_CPU_SECONDS:
            raise RuntimeError("Research CPU allocation exhausted")

    def reserve(self, category, count):
        self.time_check()
        if sum(self.checks.values()) + count > MAX_CHECKS:
            raise RuntimeError("Exact pair/edge-check allocation exhausted before batch")
        self.checks[category] += count


def carrier_definitions():
    for h, n in product((Q(1), Q(1, 3)), (8, 16, 32, 64, 128)):
        yield f"ap_h{h}_n{n}", "ap", {h * j for j in range(n)}, {"h": str(h), "length": n}
    for h, n in product((Q(1), Q(1, 3)), (4, 8, 16)):
        a = {h * (j + shift) for j, shift in product(range(n), (0, 3 * n))}
        yield f"two_blocks_h{h}_n{n}", "two_blocks", a, {"h": str(h), "block_length": n, "offset_in_grid_units": 3 * n}
    for length in (4, 8):
        for w in (Q(3, 2), Q(5, 3), Q(length) + Q(1, 3)):
            a = {i + w * j for i, j in product(range(length), repeat=2)}
            yield f"box_L{length}_w{w}", "coefficient_box", a, {"side": length, "weight": str(w), "parameter_count": length * length}
    for kind, n in product(("squares", "cubic_coordinate"), (16, 32)):
        a = {Q(j * j) if kind == "squares" else Q(j ** 3 - j, 2) for j in range(n)}
        yield f"sequence_{kind}_n{n}", "polynomial_sequence", a, {"kind": kind, "parameter_count": n}
    for m, length in ((2, 4), (4, 4), (2, 8), (4, 8)):
        a = {c for k, j in product(range(m), range(-length, length + 1))
             for c in orbit_coordinates(Q(2 * k), Q(j))}
        pairs = m * (2 * length + 1)
        yield f"planted_M{m}_L{length}", "planted_fibers", a, {"M": m, "L": length, "outputs": [2 * k for k in range(m)], "designed_pairs": pairs, "coordinate_occurrences": 2 * pairs}
    current = {Q(j, 3) for j in range(6)}
    # These four exact shifts are both coordinates of T_{1/3}(t,t) and
    # T_1(t,t), together with the retained t. No arbitrary closure is taken.
    diagonal_shifts = (Q(0), Q(-1), Q(4, 27), Q(-5, 27))
    for level in (1, 2):
        previous = current
        current = {t + shift for t, shift in product(previous, diagonal_shifts)}
        yield f"diagonal_completion_level{level}", "recursive_diagonal_completion", current, {"level": level, "previous_inputs": list(map(str, sorted(previous))), "steps": ["1/3", "1"], "coordinate_occurrences": 4 * len(previous), "prescribed_source_pairs": len(previous)}


def enumerate_fibers(values, budget):
    values = tuple(sorted(set(map(Q, values))))
    n = len(values)
    if not 1 <= n <= MAX_INPUTS or budget.carriers >= MAX_CARRIERS:
        raise RuntimeError("Carrier count or input cardinality exceeds allocation")
    budget.reserve("scalar_pair_evaluations", n * n)
    budget.carriers += 1
    by_output = defaultdict(list)
    for i, x in enumerate(values):
        for j, y in enumerate(values):
            by_output[polynomial(x, y)].append((x - y, i * n + j))
        budget.time_check()
    edge_count = sum(len(fiber) * (len(fiber) - 1) // 2 for fiber in by_output.values())
    budget.reserve("within_fiber_pair_enumeration", edge_count)
    edges_by_step = defaultdict(list)
    fibers = []
    output_of_vertex = [-1] * (n * n)
    for output_index, (z, entries) in enumerate(sorted(by_output.items())):
        entries.sort()
        for _, vertex in entries:
            output_of_vertex[vertex] = output_index
        for (u, v), (w, t) in combinations(entries, 2):
            if w <= u:
                raise AssertionError("The output and difference do not recover the pair")
            edges_by_step[w - u].append((v, t))
        fibers.append({"output": str(z), "differences": [str(u) for u, _ in entries], "vertices": [v for _, v in entries], "size": len(entries)})
    if any(z < 0 for z in output_of_vertex):
        raise AssertionError("Incomplete full Cartesian pair coverage")
    return {"values": values, "N": n, "fibers": fibers, "output_of_vertex": output_of_vertex,
            "edges_by_step": dict(edges_by_step), "edge_pool_size": edge_count,
            "image_size": len(fibers)}


def inventories(carrier):
    n = carrier["N"]
    small, medium = ceil_root(n, 6), ceil_root(n, 2)
    ranked = sorted(carrier["edges_by_step"], key=lambda s: (-len(carrier["edges_by_step"][s]), s))
    return [
        ("integer_small", tuple(map(Q, range(1, small + 1)))),
        ("integer_sqrt", tuple(map(Q, range(1, medium + 1)))),
        ("third_sqrt", tuple(Q(j, 3) for j in range(1, medium + 1))),
        ("frequent_small", tuple(sorted(ranked[:small]))),
        ("frequent_sqrt", tuple(sorted(ranked[:medium]))),
        ("all_useful_diagnostic", tuple(sorted(ranked))),
    ]


def inventory_profile(steps):
    denominator = 1
    for step in steps:
        denominator = denominator * step.denominator // gcd(denominator, step.denominator)
    return {"cardinality": len(steps), "common_denominator": str(denominator),
            "maximum_numerator_bits": max((abs(s.numerator).bit_length() for s in steps), default=0),
            "maximum_denominator_bits": max((s.denominator.bit_length() for s in steps), default=0),
            "serialized_character_count": sum(len(str(s)) for s in steps)}


def graph_case(carrier, label, steps, budget, direct_oracle=False):
    n = carrier["N"]
    steps = tuple(sorted(set(map(Q, steps))))
    if any(s <= 0 for s in steps):
        raise ValueError("This diagnostic uses positive steps only")
    if budget.cases >= MAX_CASES:
        raise RuntimeError("Carrier/inventory case allocation exhausted")
    # Charge complete scans of the pool and all vertices before starting.
    budget.reserve("inventory_edge_pool_checks", carrier["edge_pool_size"])
    budget.reserve("component_vertex_checks", n * n)
    if direct_oracle:
        budget.reserve("direct_motion_oracle_checks", n * n * len(steps))
    budget.cases += 1
    parent = list(range(n * n))
    used_vertices = set()
    selected_edges = []
    per_step = {}

    def find(v):
        while v != parent[v]:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    selected = set(steps)
    for step, edges in carrier["edges_by_step"].items():
        if step not in selected:
            continue
        per_step[str(step)] = len(edges)
        for v, w in edges:
            selected_edges.append([v, w])
            used_vertices.update((v, w))
            a, b = find(v), find(w)
            if a != b:
                parent[b] = a
    for step in steps:
        per_step.setdefault(str(step), 0)
    groups = defaultdict(list)
    for vertex in range(n * n):
        groups[find(vertex)].append(vertex)
    components = sorted(groups.values(), key=lambda c: c[0])
    distribution = Counter(map(len, components))
    component_outputs = []
    output_components = Counter()
    for component in components:
        outputs = {carrier["output_of_vertex"][v] for v in component}
        if len(outputs) != 1:
            raise AssertionError("A component crosses actual scalar outputs")
        z = next(iter(outputs))
        component_outputs.append(z)
        output_components[z] += 1
    if sum(size * count for size, count in distribution.items()) != n * n:
        raise AssertionError("Components fail to cover the full square")
    if len(components) < carrier["image_size"]:
        raise AssertionError("Image/component inequality is reversed")
    edge_count = len(selected_edges)
    if sum(per_step.values()) != edge_count:
        raise AssertionError("Directed and distinct-undirected counts disagree for positive steps")
    if direct_oracle:
        values = carrier["values"]
        index = {x: i for i, x in enumerate(values)}
        expected = set()
        for step, i, j in product(steps, range(n), range(n)):
            xp, yp = motion(values[i], values[j], step)
            if xp in index and yp in index:
                expected.add((i * n + j, index[xp] * n + index[yp]))
        if expected != {tuple(edge) for edge in selected_edges}:
            raise AssertionError("Fiber-difference graph and direct T_tau graph disagree")
    thresholds = {"2": 2, "4": 4, "8": 8, "16": 16,
                  "ceil_N_quarter": ceil_root(n, 4), "ceil_sqrt_N": ceil_root(n, 2)}
    masses = {}
    for key, threshold in thresholds.items():
        mass = sum(size * count for size, count in distribution.items() if size >= threshold)
        masses[key] = {"minimum_size": threshold, "covered_pairs": mass,
                       "covered_fraction": str(Q(mass, n * n)), "covered_pairs_per_scalar": str(Q(mass, n)),
                       "full_support_certificate": str(Q(n * n, threshold) + n * n - mass)}
    result = {
        "inventory": label, "steps": list(map(str, steps)), "N": n, "M": len(steps),
        "inventory_profile": inventory_profile(steps),
        "useful_selected_steps": sum(c > 0 for c in per_step.values()),
        "directed_counts_by_step": per_step, "directed_edge_count": edge_count,
        "distinct_undirected_edges": edge_count,
        "nonisolated_vertices": len(used_vertices), "nonisolated_fraction": str(Q(len(used_vertices), n * n)),
        "covered_pairs_per_scalar": str(Q(len(used_vertices), n)),
        "component_size_distribution": {str(k): v for k, v in sorted(distribution.items())},
        "largest_component": max(distribution), "component_count": len(components),
        "image_size": carrier["image_size"],
        "actual_fiber_size_distribution": dict(sorted(Counter(f["size"] for f in carrier["fibers"]).items())),
        "components_per_output": [output_components[z] for z in range(carrier["image_size"])],
        "components_per_output_distribution": dict(sorted(Counter(output_components.values()).items())),
        "fragmented_output_count": sum(c > 1 for c in output_components.values()),
        "component_excess_over_image": len(components) - carrier["image_size"],
        "missing_within_fiber_connections": carrier["edge_pool_size"] - sum(len(c) * (len(c) - 1) // 2 for c in components),
        "cycle_excess_edges": edge_count - (n * n - len(components)),
        "long_component_mass": masses,
        "components": components, "component_output_indices": component_outputs,
        "edges": selected_edges, "direct_motion_oracle": "PASS" if direct_oracle else "not run",
        "diagnostic_only": label == "all_useful_diagnostic",
    }
    if label == "all_useful_diagnostic" and result["component_count"] != carrier["image_size"]:
        raise AssertionError("All useful steps fail to connect each complete fiber")
    budget.time_check()
    return result


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n")


def run(output_directory, example_path):
    budget = Budget()
    wall = time.perf_counter()
    if output_directory.exists():
        raise RuntimeError("Refusing to overwrite an existing research directory")
    definitions = list(carrier_definitions())
    if len(definitions) != 32 or max(len(a) for _, _, a, _ in definitions) > MAX_INPUTS:
        raise AssertionError("Declared carrier preflight failed")
    if len(definitions) * 6 > MAX_CASES:
        raise RuntimeError("Declared inventory count exceeds allocation")
    output_directory.mkdir(parents=True)
    records, all_cases, errors = [], [], []
    try:
        for identifier, family, values, parameters in definitions:
            carrier = enumerate_fibers(values, budget)
            carrier_record = {"id": identifier, "family": family, "parameters": parameters,
                              "inputs": list(map(str, carrier["values"])), "N": carrier["N"],
                              "image_size": carrier["image_size"], "fibers": carrier["fibers"],
                              "pair_output_index": carrier["output_of_vertex"],
                              "edge_pool_size": carrier["edge_pool_size"],
                              "all_useful_step_counts": {str(s): len(e) for s, e in sorted(carrier["edges_by_step"].items())},
                              "actual_fiber_size_distribution": dict(sorted(Counter(f["size"] for f in carrier["fibers"]).items()))}
            if "parameter_count" in parameters:
                carrier_record["parameter_to_scalar_ratio"] = str(Q(parameters["parameter_count"], carrier["N"]))
            if "coordinate_occurrences" in parameters:
                carrier_record["coordinate_reuse"] = str(Q(parameters["coordinate_occurrences"], carrier["N"]))
            if "designed_pairs" in parameters:
                carrier_record["prescribed_pair_fraction"] = str(Q(parameters["designed_pairs"], carrier["N"] ** 2))
            safe_id = identifier.replace("/", "over")
            carrier_path = output_directory / f"{safe_id}-carrier.json"
            write_json(carrier_path, carrier_record)
            carrier_record["raw_path"] = str(carrier_path)
            carrier_record["raw_sha256"] = hashlib.sha256(carrier_path.read_bytes()).hexdigest()
            records.append({k: v for k, v in carrier_record.items() if k not in {"fibers", "pair_output_index"}})
            for label, steps in inventories(carrier):
                oracle = label == "frequent_small" and identifier in {"ap_h1_n8", "ap_h1/3_n8", "diagonal_completion_level1"}
                case = graph_case(carrier, label, steps, budget, direct_oracle=oracle)
                case["carrier_id"] = identifier
                case_path = output_directory / f"{safe_id}-{label}.json"
                write_json(case_path, case)
                case["raw_path"] = str(case_path)
                case["raw_sha256"] = hashlib.sha256(case_path.read_bytes()).hexdigest()
                all_cases.append({k: v for k, v in case.items() if k not in {"components", "component_output_indices", "edges", "components_per_output"}})
                budget.time_check()
    except Exception as error:
        errors.append({"type": type(error).__name__, "message": str(error), "completed_carriers": len(records), "completed_cases": len(all_cases)})
    summary = {"date": "2026-09-21", "status": "EXPERIMENTAL exact, declared growing-step diagnostics only",
               "polynomial": "(x-y)^3+x+y", "carriers": records, "cases": all_cases, "errors": errors,
               "step_sign_convention": "Positive steps only. Each successful directed return points from smaller to larger difference; it gives one distinct undirected edge.",
               "all_useful_warning": "Taking every actual within-fiber difference makes components equal full fibers by construction. Its recorded cardinality is charged, and it supplies no independently proved power saving.",
               "connectivity_warning": "Belonging to one coset of the subgroup generated by the steps is necessary, not sufficient: missing intermediate fiber values can disconnect the induced graph."}
    write_json(example_path, summary)
    provenance = {"date": "2026-09-21", "command": "python3 -m experiments.growing_step_cubic",
                  "python": sys.version, "implementation": platform.python_implementation(), "network": "none", "randomness": "none",
                  "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "summary_sha256": hashlib.sha256(example_path.read_bytes()).hexdigest(),
                  "carrier_definition_sha256": hashlib.sha256(json.dumps([[i, f, list(map(str, sorted(a))), p] for i, f, a, p in definitions], sort_keys=True).encode()).hexdigest(),
                  "budget_limits": {"carriers": MAX_CARRIERS, "cases": MAX_CASES, "inputs": MAX_INPUTS, "pair_edge_checks": MAX_CHECKS, "cpu_seconds": MAX_CPU_SECONDS},
                  "actual": {"carriers": budget.carriers, "cases": budget.cases, "checks_by_category": dict(budget.checks), "charged_checks": sum(budget.checks.values()),
                             "cpu_seconds": time.process_time() - budget.start_cpu, "wall_seconds": time.perf_counter() - wall},
                  "errors": errors,
                  "counting": "N² scalar P evaluations once per carrier; each within-fiber pair enumerated once; all edge-pool entries and N² vertices charged again for each inventory; direct motion oracles charged N²|S|. No old research grid is rerun."}
    write_json(output_directory / "provenance.json", provenance)
    leaders = sorted(all_cases, key=lambda r: (-Q(r["nonisolated_fraction"]), r["carrier_id"], r["inventory"]))[:8]
    print(json.dumps({"actual": provenance["actual"], "errors": errors,
                      "highest_coverage": [{k: r[k] for k in ("carrier_id", "inventory", "N", "M", "nonisolated_fraction", "largest_component", "component_count", "image_size")} for r in leaders]}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path, default=Path("local-only/runs/T01/2026-09-21-growing-step-cubic"))
    parser.add_argument("--example", type=Path, default=Path("examples/2026-09-21-growing-step-cubic.json"))
    args = parser.parse_args()
    run(args.output_directory, args.example)


if __name__ == "__main__":
    main()
