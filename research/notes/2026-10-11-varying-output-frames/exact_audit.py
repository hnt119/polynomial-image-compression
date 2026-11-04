"""One released exact audit of the fixed AP-output triangle family.

No parameter search, extra-frame enumeration, numerical roots, or imports
from earlier research programs. Equality is in Q[u]/(u^3-7u^2+13u-1).
The actual positive scalar scale h satisfies h^2=u/4.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys
import time


CASES = (2, 3, 4)
MAX_INSTANCES = 6
MAX_CHECKS_AND_P = 5000
MODULUS = (F(-1), F(13), F(-7), F(1))
ZERO = (F(0), F(0), F(0))
ONE = (F(1), F(0), F(0))
U = (F(0), F(1), F(0))
COUNTS = Counter()


def charge(category):
    COUNTS[category] += 1
    if sum(COUNTS.values()) > MAX_CHECKS_AND_P:
        raise RuntimeError("Declared combined exact-check/P budget exceeded")


def check(condition, category):
    charge("check_" + category)
    if not condition:
        raise AssertionError(category)


def const(n):
    return (F(n), F(0), F(0))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def scale(a, n):
    return tuple(F(n) * x for x in a)


def mul(a, b):
    raw = [F(0)] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            raw[i + j] += x * y
    for degree in range(4, 2, -1):
        leading = raw[degree]
        for j, coefficient in enumerate(MODULUS):
            raw[degree - 3 + j] -= leading * coefficient
    return tuple(raw[:3])


LAMBDA = scale(U, F(1, 4))
RHO = sub(const(2), U)
SHORT_S = sub(const(7), scale(U, 2))
LONG_H = sub(const(3), U)
LONG_S = sub(const(5), U)


def p_difference(a, b):
    """Return P(ha,hb)/h by generic field multiplication/reduction."""
    charge("P_difference_cube")
    difference = sub(a, b)
    cube = mul(mul(difference, difference), difference)
    return add(mul(LAMBDA, cube), add(a, b))


# Independent reduction data for the expanded oracle. This recurrence uses
# u^j=7u^(j-1)-13u^(j-2)+u^(j-3), rather than generic long division.
POWER_TABLE = [
    (F(1), F(0), F(0)),
    (F(0), F(1), F(0)),
    (F(0), F(0), F(1)),
]
for exponent in range(3, 8):
    POWER_TABLE.append(tuple(
        7 * POWER_TABLE[exponent - 1][j]
        - 13 * POWER_TABLE[exponent - 2][j]
        + POWER_TABLE[exponent - 3][j]
        for j in range(3)
    ))


def p_expanded(a, b):
    """Separate expanded-cube oracle; calls no generic field operations."""
    charge("P_expanded_cube")
    raw = [F(0)] * 8
    for i in range(3):
        for j in range(3):
            for k in range(3):
                raw[i + j + k + 1] += (
                    a[i] * a[j] * a[k]
                    - 3 * a[i] * a[j] * b[k]
                    + 3 * a[i] * b[j] * b[k]
                    - b[i] * b[j] * b[k]
                ) / 4
    for i in range(3):
        raw[i] += a[i] + b[i]
    result = [F(0), F(0), F(0)]
    for exponent, coefficient in enumerate(raw):
        for j in range(3):
            result[j] += coefficient * POWER_TABLE[exponent][j]
    return tuple(result)


def vector(a):
    return [str(x) for x in a]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frame(center, row_half_width, column_half_width, low, high, name):
    rows = (sub(center, row_half_width), add(center, row_half_width))
    columns = (
        sub(center, column_half_width),
        add(center, column_half_width),
    )
    check(len(set(rows + columns)) == 4, "frame_four_distinct_scalars")
    return {"name": name, "rows": rows, "columns": columns,
            "row_outputs": (low, high)}


def audit_case(m):
    before = COUNTS.copy()
    outputs = [scale(RHO, 4 * j) for j in range(m + 1)]
    short_frames = []
    for j in range(m):
        short_frames.append(frame(
            scale(RHO, 2 * j + 1), ONE, SHORT_S,
            outputs[j], outputs[j + 1], "short_" + str(j),
        ))
    long_frames = []
    for j in range(m - 1):
        long_frames.append(frame(
            scale(RHO, 2 * j + 2), LONG_H, LONG_S,
            outputs[j], outputs[j + 2], "long_" + str(j),
        ))

    short_endpoints = [x for f in short_frames for x in f["rows"] + f["columns"]]
    scalars = sorted(set(short_endpoints))
    check(len(short_endpoints) == len(scalars) == 4 * m, "disjoint_short_blocks")
    index = {value: i for i, value in enumerate(scalars)}
    for f in long_frames:
        check(all(x in index for x in f["rows"] + f["columns"]),
              "long_frame_adds_no_scalars")

    pair_targets = {}
    frame_records = []
    for f in short_frames + long_frames:
        pairs = []
        for row, target in zip(f["rows"], f["row_outputs"]):
            for column in f["columns"]:
                pair = (index[row], index[column])
                if pair in pair_targets:
                    check(pair_targets[pair] == target, "consistent_shared_pair_label")
                pair_targets[pair] = target
                pairs.append(list(pair))
        frame_records.append({"name": f["name"], "ordered_pairs": pairs,
                              "row_outputs_over_h": [vector(x) for x in f["row_outputs"]]})
    check(len(pair_targets) == 6 * m - 2, "selected_pair_formula")
    check(set(pair_targets.values()) == set(outputs), "selected_output_formula")

    values = {}
    fibers = defaultdict(list)
    for i, a in enumerate(scalars):
        for j, b in enumerate(scalars):
            value = p_difference(a, b)
            independent = p_expanded(a, b)
            check(value == independent, "independent_P_oracles_agree")
            values[(i, j)] = value
            fibers[value].append([i, j])
    check(len(values) == (4 * m) ** 2, "complete_square")
    for pair, target in pair_targets.items():
        check(values[pair] == target, "selected_pair_has_prescribed_output")

    selected_rows = defaultdict(lambda: defaultdict(list))
    for (i, j), output in pair_targets.items():
        selected_rows[output][i].append(j)
    output_records = []
    for label, output in enumerate(outputs):
        rows = selected_rows[output]
        selected_mass = sum(len(columns) for columns in rows.values())
        expected_mass = ((2 + (label <= m - 2)) if label < m else 0)
        expected_mass += ((2 + (label >= 2)) if label >= 1 else 0)
        check(selected_mass == expected_mass, "selected_fiber_mass_formula")
        check(len(rows) == (1 if label in (0, m) else 2),
              "selected_rows_per_output")
        output_records.append({
            "label": label, "output_over_h": vector(output),
            "selected_mass": selected_mass,
            "full_fiber_mass": len(fibers[output]),
            "selected_rows": [{"first_index": i, "second_indices": sorted(columns)}
                              for i, columns in sorted(rows.items())],
        })

    # Read the approved AP witness out of the already evaluated matrix.
    # This neither enlarges the carrier nor evaluates any extra P cell.
    ap_indices = [index[f["rows"][1]] for f in short_frames]
    ap_image = {values[(i, j)] for i in ap_indices for j in ap_indices}
    check(len(ap_image) == m * m, "AP_witness_is_injective")
    histogram = Counter(len(pairs) for pairs in fibers.values())
    check(sum(size * count for size, count in histogram.items()) == len(values),
          "full_fiber_histogram_covers_square")
    check(sum(histogram.values()) == len(fibers), "full_fiber_histogram_counts_image")
    selected_histogram = Counter(sum(len(v) for v in rows.values())
                                 for rows in selected_rows.values())
    n, q, z = len(scalars), len(pair_targets), len(selected_rows)
    b = n * n - q
    check((n, q, z, b, z + b) ==
          (4 * m, 6 * m - 2, m + 1, 16 * m * m - 6 * m + 2,
           16 * m * m - 5 * m + 3), "entire_ledger_formula")
    check(len(fibers) <= z + b, "safe_full_image_upper_bound")
    return {
        "m": m, "N": n, "Q": q, "Z": z, "B": b,
        "safe_image_upper": z + b, "actual_full_image": len(fibers),
        "ratios": {"2Q_over_N": str(F(2 * q, n)),
                   "Q_over_Z": str(F(q, z)), "Q_over_N_squared": str(F(q, n * n))},
        "scalars_over_h": [vector(x) for x in scalars],
        "scalar_index_order": "lexicographic coefficient order, not real order",
        "frames": frame_records,
        "selected_pairs": [list(p) for p in sorted(pair_targets)],
        "selected_outputs_and_rows": output_records,
        "selected_fiber_histogram": {str(k): v for k, v in sorted(selected_histogram.items())},
        "complete_fiber_histogram": {str(k): v for k, v in sorted(histogram.items())},
        "complete_fibers": [{"output_over_h": vector(output), "ordered_pairs": pairs}
                            for output, pairs in sorted(fibers.items())],
        "strict_small_fiber_pair_mass": {
            str(k): sum(size * count for size, count in histogram.items() if size < k)
            for k in range(1, max(histogram) + 2)
        },
        "AP_witness_indices": ap_indices, "AP_witness_image_size": len(ap_image),
        "charged_counts": dict(sorted((COUNTS - before).items())),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compatibility-proof", type=Path, required=True)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("exact-results.json"))
    args = parser.parse_args()
    if not args.compatibility_proof.is_file():
        raise SystemExit("The released saved compatibility proof is required")
    if args.output.exists():
        raise SystemExit("Refusing to overwrite existing finite evidence")
    if len(CASES) > MAX_INSTANCES:
        raise SystemExit("Case ceiling exceeded")
    start_wall, start_cpu = time.perf_counter(), time.process_time()
    check(add(scale(LAMBDA, 3), mul(LAMBDA, mul(SHORT_S, SHORT_S))) == ONE,
          "short_conic_identity")
    check(add(scale(mul(LAMBDA, mul(LONG_H, LONG_H)), 3),
              mul(LAMBDA, mul(LONG_S, LONG_S))) == ONE, "long_conic_identity")
    check(sub(SHORT_S, RHO) == LONG_S, "shared_column_identity")
    check(add(RHO, ONE) == LONG_H, "shared_row_identity")
    check(mul(LAMBDA, mul(scale(RHO, 2), scale(RHO, 2))) ==
          (F(1), F(-9), F(3)), "AP_step_squared_formula")
    cases = [audit_case(m) for m in CASES]
    check(COUNTS["P_difference_cube"] == COUNTS["P_expanded_cube"] == 464,
          "frozen_P_evaluation_count")
    result = {
        "claim": "EXPERIMENTAL: exact, exhaustive for only m=2,3,4",
        "track": "T01", "polynomial": "(x-y)^3+x+y",
        "scope": "fixed compatible AP-output triangles; no extra-frame enumeration",
        "field": {"modulus_low_to_high": [str(x) for x in MODULUS],
                  "real_root_interval": ["2/25", "4/49"],
                  "coefficient_degree": 3, "scalar_scale": "h>0, h^2=u/4",
                  "faithfulness": "u^3-7u^2+13u-1 is monic with no rational roots +/-1"},
        "frozen_cases": list(CASES),
        "budget": {"maximum_instances": MAX_INSTANCES,
                   "maximum_checks_plus_P": MAX_CHECKS_AND_P,
                   "actual_instances": len(CASES),
                   "actual_checks_plus_P": sum(COUNTS.values()),
                   "P_evaluations": COUNTS["P_difference_cube"] + COUNTS["P_expanded_cube"],
                   "exact_checked_predicates": sum(v for k, v in COUNTS.items()
                                                   if k.startswith("check_")),
                   "counting_unit": "explicit checked predicates plus each target-P oracle call; not rational machine operations"},
        "charged_counts": dict(sorted(COUNTS.items())),
        "cases": cases,
        "provenance": {"command": sys.argv,
                       "python_version": platform.python_version(),
                       "source_path": str(Path(__file__)),
                       "source_sha256": sha256(Path(__file__)),
                       "compatibility_proof_path": str(args.compatibility_proof),
                       "compatibility_proof_sha256": sha256(args.compatibility_proof),
                       "cpu_seconds": time.process_time() - start_cpu,
                       "wall_seconds": time.perf_counter() - start_wall,
                       "network": False, "randomness": False,
                       "imports_previous_research_code": False},
        "limitations": ["No asymptotic image upper bound follows from these finite counts.",
                        "The proved AP sub-square already gives a quadratic actual-image lower bound.",
                        "No other widths, parameters, orders, carriers, or complete frames are searched."],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(json.dumps({"output": str(args.output), "budget": result["budget"],
                      "cases": [{k: case[k] for k in
                                 ("m", "N", "Q", "Z", "B", "safe_image_upper",
                                  "actual_full_image", "complete_fiber_histogram")}
                                for case in cases]}, indent=2))


if __name__ == "__main__":
    main()
