"""Exact audit of the one frozen conic-frame ladder, at m=1,2,3 only.

The real input is x=sqrt(t)*A(t), where t is the root of the irreducible
cubic f=64t^3-80t^2+28t-1 in (0,1/12). Equality is exact in Q[t]/f.
Each of the 116 actual square cells is evaluated twice, charging 232 P
evaluations. No numerical root, package, alternate carrier or sweep is used.
"""
import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json
import platform
import time


CASES = (1, 2, 3)
LIMITS = {"instances": 8, "P_evaluations": 30000,
          "compatibility_checks": 10000}
RUN_DIR = Path("local-only/runs/T01/2026-10-06-changed-collision-pattern")
PORTABLE = Path("examples/2026-10-06-changed-collision-pattern.json")
ZERO = (F(0), F(0), F(0))
ONE = (F(1), F(0), F(0))
T = (F(0), F(1), F(0))


@dataclass
class Budget:
    limits: dict = field(default_factory=lambda: dict(LIMITS))
    counts: Counter = field(default_factory=Counter)
    categories: Counter = field(default_factory=Counter)
    polynomial_methods: Counter = field(default_factory=Counter)

    def charge(self, category, amount=1):
        if amount < 0 or self.counts[category]+amount > self.limits[category]:
            raise RuntimeError(f"Budget exceeded: {category}")
        self.counts[category] += amount

    def check(self, condition, category):
        self.charge("compatibility_checks")
        self.categories[category] += 1
        if not condition:
            raise AssertionError(category)

    def polynomial(self, method):
        self.charge("P_evaluations")
        self.polynomial_methods[method] += 1


def add(left, right):
    return tuple(a+b for a, b in zip(left, right))


def scale(value, coefficient):
    return tuple(F(coefficient)*entry for entry in value)


def reduce_polynomial(coefficients):
    """Long division by f/64, using exact rational coefficients."""
    result = list(map(F, coefficients))
    result.extend([F(0)]*max(0, 3-len(result)))
    for power in range(len(result)-1, 2, -1):
        coefficient = result[power]
        result[power-3] += coefficient/64
        result[power-2] -= 7*coefficient/16
        result[power-1] += 5*coefficient/4
        result[power] = F(0)
    return tuple(result[:3])


def multiply(left, right):
    coefficients = [F(0)]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            coefficients[i+j] += a*b
    return reduce_polynomial(coefficients)


def encoded(value):
    """Coefficients of 1,t,t^2; the actual scalar/output includes sqrt(t)."""
    return [[entry.numerator, entry.denominator] for entry in value]


def p_difference(x, y, budget):
    """Repeated generic field products of t*(x-y)^3+x+y."""
    budget.polynomial("difference_cube_long_division")
    difference = add(x, scale(y, -1))
    cube = multiply(multiply(difference, difference), difference)
    return add(multiply(T, cube), add(x, y))


def p_expanded(x, y, budget):
    """Independent unreduced cubic expansion for the linear input labels.

    No generic field multiplication or long-division function is used here.
    Coefficients through degree four are reduced by a fixed power table.
    """
    if x[2] or y[2]:
        raise ValueError("The frozen ladder has linear input coefficients")
    budget.polynomial("expanded_cube_fixed_power_table")
    polynomial = [F(0)]*5
    for i in range(2):
        for j in range(2):
            for k in range(2):
                polynomial[i+j+k+1] += (
                    x[i]*x[j]*x[k]-3*x[i]*x[j]*y[k]
                    +3*x[i]*y[j]*y[k]-y[i]*y[j]*y[k])
    for i in range(2):
        polynomial[i] += x[i]+y[i]
    powers = (ONE, T, (F(0), F(0), F(1)),
              (F(1, 64), F(-7, 16), F(5, 4)),
              (F(5, 256), F(-17, 32), F(9, 8)))
    return tuple(sum(polynomial[j]*powers[j][i] for j in range(5))
                 for i in range(3))


def constants():
    r_over_h = add(scale(T, 4), scale(ONE, -2))
    s_over_h = add(ONE, scale(r_over_h, -2))
    return r_over_h, s_over_h


def scalar_label(index, sign, r_over_h):
    return add(scale(r_over_h, 2*index-1), scale(ONE, sign))


def analyze(m, budget):
    if m not in CASES:
        raise ValueError("Only the three frozen audit lengths are authorized")
    budget.charge("instances")
    r_over_h, s_over_h = constants()
    budget.check(add(multiply(T, add(scale(ONE, 3),
                                    multiply(s_over_h, s_over_h))),
                     scale(ONE, -1)) == ZERO, "conic_compatibility")
    # This is the real ordering proved in CP-C3, not coefficient lexicography.
    order = [(m, -1)]
    for index in reversed(range(m)):
        order.extend([(index, -1), (index, 1)])
    order.append((-1, 1))
    records = [{"coset_index": index, "sign": sign,
                "part": f"source_{index}" if 0 <= index < m else f"boundary_{index}",
                "coefficient": scalar_label(index, sign, r_over_h)}
               for index, sign in order]
    indices = {row["coefficient"]: i for i, row in enumerate(records)}
    n = len(indices)
    budget.check(n == len(records) == 2*m+2, "distinct_actual_scalars")
    endpoint_set = set()
    selected, labels = {}, []
    for frame in range(m):
        center = scale(r_over_h, 2*frame-1)
        budget.check(add(center, s_over_h) == scalar_label(frame-1, 1, r_over_h),
                     "positive_target_gluing")
        budget.check(add(center, scale(s_over_h, -1)) == scalar_label(frame+1, -1, r_over_h),
                     "negative_target_gluing")
        for row_sign in (-1, 1):
            x = add(center, scale(ONE, row_sign))
            output_index = frame if row_sign < 0 else frame-1
            expected = scale(r_over_h, 4*output_index)
            for column_sign in (-1, 1):
                y = add(center, scale(s_over_h, column_sign))
                endpoint_set.update((x, y))
                pair = (indices[x], indices[y])
                budget.check(pair not in selected, "distinct_selected_pairs")
                budget.check(records[pair[0]]["part"] != records[pair[1]]["part"],
                             "selected_pair_crosses_partition")
                selected[pair] = expected
                labels.append({"frame": frame, "row_sign": row_sign,
                               "column_sign": column_sign, "output_index": output_index,
                               "pair_indices": list(pair), "output_coefficients": encoded(expected)})
    budget.check(endpoint_set == set(indices), "actual_endpoint_union")
    q, z = len(selected), len(set(selected.values()))
    expected_histogram = {2: 2}
    if m > 1:
        expected_histogram[4] = m-1
    budget.check((q, z) == (4*m, m+1), "expected_Q_Z")
    budget.check(Counter(Counter(selected.values()).values()) == expected_histogram,
                 "selected_fiber_histogram")
    represented_frames = defaultdict(set)
    for label in labels:
        represented_frames[label["output_index"]].add(label["frame"])
    cross_frame_mass = sum(len(represented_frames[label["output_index"]]) > 1
                           for label in labels)
    budget.check(cross_frame_mass == 4*(m-1), "cross_frame_repeated_output_mass")
    if budget.counts["P_evaluations"]+2*n*n > budget.limits["P_evaluations"]:
        raise RuntimeError("Insufficient budget for both complete-square formulas")
    fibers, values = defaultdict(list), {}
    for a, x in enumerate(records):
        for b, y in enumerate(records):
            primary = p_difference(x["coefficient"], y["coefficient"], budget)
            oracle = p_expanded(x["coefficient"], y["coefficient"], budget)
            budget.check(primary == oracle, "independent_P_agreement")
            fibers[primary].append((a, b))
            values[(a, b)] = primary
    for pair, expected in selected.items():
        budget.check(values[pair] == expected, "prescribed_output")
    histogram = Counter(map(len, fibers.values()))
    budget.check(sum(size*count for size, count in histogram.items()) == n*n,
                 "complete_square_pair_mass")
    budget.check(sum(histogram.values()) == len(fibers), "complete_image_count")
    plus_indices = [i for i, row in enumerate(records) if row["sign"] == 1]
    ap_image = {values[(a, b)] for a in plus_indices for b in plus_indices}
    budget.check(len(ap_image) == (m+1)**2, "AP_subsquare_injectivity")
    budget.check(len(fibers) >= n*n//4, "actual_image_stop_lower_bound")
    budget.check(len(fibers) <= z+n*n-q, "safe_support_upper_bound")
    tails = {str(k): sum(size*count for size, count in histogram.items() if size < k)
             for k in range(1, n+2)}
    threshold = isqrt(n)
    if threshold**2 < n:
        threshold += 1
    summary = {
        "id": f"conic_ladder_m{m}", "m": m, "N": n, "Q": q, "Z": z,
        "B": n*n-q, "full_square": n*n, "safe_support_upper_bound": z+n*n-q,
        "two_Q_over_N": str(F(2*q, n)), "Q_over_Z": str(F(q, z)),
        "Q_over_N_squared": str(F(q, n*n)),
        "selected_cross_block_pairs": q, "selected_local_pairs": 0,
        "cross_frame_repeated_output_pair_mass": cross_frame_mass,
        "all_local_partition_pairs": 4*m+2,
        "all_cross_partition_pairs": n*n-(4*m+2),
        "full_image": len(fibers), "maximum_fiber": max(histogram),
        "fiber_histogram": dict(sorted(histogram.items())),
        "selected_fiber_histogram": dict(sorted(expected_histogram.items())),
        "strict_small_fiber_tails": tails,
        "sqrt_tail_threshold": threshold, "sqrt_tail_pair_mass": tails[str(threshold)],
        "ranked_fiber_sizes": sorted(map(len, fibers.values()), reverse=True),
        "AP_subsquare_image": len(ap_image), "proved_actual_image_lower_bound": n*n//4,
        "excluded_scalar_pairs": 0,
    }
    raw = {
        "summary": summary,
        "representation": "Each triple encodes sqrt(t)*(c0+c1*t+c2*t^2), rational entries [numerator,denominator].",
        "actual_scalars_in_increasing_order": [dict(index=i,
             coset_index=row["coset_index"], sign=row["sign"], part=row["part"],
             coefficients=encoded(row["coefficient"])) for i, row in enumerate(records)],
        "selected_pair_labels": labels,
        "full_fibers": [{"output_coefficients": encoded(key),
                         "pair_indices": [list(pair) for pair in pairs]}
                        for key, pairs in sorted(fibers.items())],
    }
    if m <= 2:
        raw["complete_output_matrix"] = [[encoded(values[(a, b)])
                                          for b in range(n)] for a in range(n)]
    return summary, raw


def write_new(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, sort_keys=True, indent=2)
        stream.write("\n")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(proof_paths):
    proof_paths = [Path(path) for path in proof_paths]
    if len(proof_paths) != 2 or any(not path.is_file() for path in proof_paths):
        raise FileNotFoundError("Two saved and reviewed proof companions are required")
    destinations = [PORTABLE, RUN_DIR/"experiment-provenance.json"]
    destinations += [RUN_DIR/f"conic_ladder_m{m}.json" for m in CASES]
    if any(path.exists() for path in destinations):
        raise FileExistsError("Existing artifact; no evaluations performed")
    cells = sum((2*m+2)**2 for m in CASES)
    if CASES != (1, 2, 3) or len(CASES) > LIMITS["instances"] or 2*cells > LIMITS["P_evaluations"]:
        raise RuntimeError("The frozen run exceeds its scope or budget")
    cpu, wall = time.process_time(), time.perf_counter()
    budget, summaries = Budget(), []
    for m in CASES:
        summary, raw = analyze(m, budget)
        path = RUN_DIR/f"conic_ladder_m{m}.json"
        digest = write_new(path, raw)
        summaries.append(dict(summary, raw_path=str(path), raw_sha256=digest))
    inputs = {
        "m": CASES, "minimal_polynomial": [-1, 28, -80, 64],
        "real_root_interval": ["0", "1/12"], "h": "positive sqrt(t)",
        "r_over_h": "4*t-2", "s_over_h": "5-8*t",
        "centers": "c_j=(2*j-1)*r, j=0,...,m-1",
        "selected_pairs": "union_j {c_j-h,c_j+h} x {c_j-s,c_j+s}",
        "fixed_polynomial": "(x-y)^3+x+y",
    }
    portable = {
        "claim_id": "CP-X1", "status": "EXPERIMENTAL", "date": "2026-10-06",
        "inputs": inputs, "models": summaries,
        "arithmetic": "Rational coefficient triples in Q[t]/(64*t^3-80*t^2+28*t-1); two independent cubic formulas/reductions.",
        "scope": "Three frozen prefixes of one conic ladder; complete actual scalar squares; no scalar exclusions.",
        "limitations": "Finite validation only. The separate symbolic N^2/4 lower bound stops the fixed ladder; no extension search.",
    }
    portable_hash = write_new(PORTABLE, portable)
    provenance = {
        "command": "python3 -m experiments.changed_collision_pattern --proofs "+" ".join(map(str, proof_paths)),
        "python": platform.python_version(), "network": "none", "randomness": "none",
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "test_sha256": hashlib.sha256(Path("tests/test_changed_collision_pattern.py").read_bytes()).hexdigest(),
        "input_sha256": hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest(),
        "proofs": [{"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                   for path in proof_paths],
        "portable_sha256": portable_hash, "limits": LIMITS,
        "charged_counts": dict(budget.counts),
        "full_square_cells": cells,
        "polynomial_methods": dict(budget.polynomial_methods),
        "check_categories": dict(budget.categories),
        "cpu_seconds": time.process_time()-cpu, "wall_seconds": time.perf_counter()-wall,
        "errors": [], "scope": "One released run; unit regressions are charged separately.",
        "unexecuted_draft": "Reverse-chain draft and lengths 4,8 were removed before any carrier evaluation.",
    }
    write_new(RUN_DIR/"experiment-provenance.json", provenance)
    print(json.dumps({"models": [{key: row[key] for key in
          ("m", "N", "Q", "Z", "B", "full_image", "fiber_histogram", "sqrt_tail_pair_mass")}
          for row in summaries], "provenance": provenance}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proofs", nargs=2, required=True,
                        help="Saved rigidity and final construction proofs")
    arguments = parser.parse_args()
    run(arguments.proofs)
