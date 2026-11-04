"""Four frozen exact scouts for the 2026-09-21 dense Cartesianization cycle.

Run only one-axis orbit thickening at d=1,2 and faithful ternary GAPs at
d=2,3. Reuse the inspected unit arithmetic, not the prior carrier scout.
Every scalar polynomial or action query, including its independent oracle,
is charged. No networking, random search, factorization or float equality.
"""

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from pathlib import Path
import platform
import sys
import time

from .unit_exponent import (Budget, action, action_box, blocks, oracle_action,
                            oracle_q, q, statistics)


CASES = (("one_axis_thickening", 1), ("one_axis_thickening", 2),
         ("faithful_ternary_gap", 2), ("faithful_ternary_gap", 3))


def carrier(family, d, data, units):
    if family == "one_axis_thickening":
        seed = {(a, -b) for a, b in units.values()}
        M = 3**d
        assert len({x for x, _ in seed}) == len({y for _, y in seed}) == M
        shifts = range(M)
        engineered = {(x+t, y) for x, y in seed for t in shifts}
        A = sorted({v for pair in engineered for v in pair})
        assert len(engineered) == M*M
        assert 4*len(engineered) <= (len(A)+1)**2
        definition = {"seed_orbit_size": M, "T": [0, M-1],
                      "engineered_pair_count": len(engineered)}
    elif family == "faithful_ternary_gap":
        P = 1
        for _, modulus, _ in data:
            P *= modulus
        B = 100*P
        weights = [B**(3**i) for i in range(d)]
        A = sorted(F(sum(a*w for a, w in zip(digits, weights)))
                   for digits in product((-1, 0, 1), repeat=d))
        assert len(set(A)) == 3**d
        engineered = set(product(A, repeat=2))
        definition = {"base": str(B), "weight_exponents": [3**i for i in range(d)],
                      "digits": [-1, 0, 1], "engineered_pair_count": len(A)**2}
    else:
        raise ValueError(family)
    return A, engineered, definition


def measure(A, units, engineered, d, budget):
    """Exhaust all ordered pairs and every actual action; retain target indices."""
    A = tuple(map(F, A))
    assert len(set(A)) == len(A)
    n = len(A)
    index = {x: i for i, x in enumerate(A)}
    U = tuple(units.values())
    assert len(set(U)) == len(U) and (F(1), F(0)) in U
    values = {}
    for x, y in product(A, repeat=2):
        budget.charge("Q_query")
        value = q(x, y)
        budget.charge("independent_Q_query")
        assert value == oracle_q(x, y)
        values[x, y] = value
    outputs = sorted(set(values.values()))
    output_index = {t: i for i, t in enumerate(outputs)}
    rows, action_counts, pair_counts, stabilizers = [], [], [], []
    good_counts, engineered_counts = [], []
    threshold = 2**d
    for x, y in product(A, repeat=2):
        targets, returning = set(), []
        fixing = 0
        for j, u in enumerate(U):
            budget.charge("action_query")
            target = action(u, x, y)
            budget.charge("independent_action_query")
            assert target == oracle_action(u, x, y)
            if target[0] in index and target[1] in index:
                assert values[target] == values[x, y]
                targets.add((index[target[0]], index[target[1]]))
                returning.append(j)
                fixing += target == (x, y)
        assert targets
        ra, rp = len(returning), len(targets)
        if (x, y) == (0, 0):
            assert ra == fixing == len(U) and rp == 1
        else:
            assert ra == rp and fixing == 1
        action_counts.append(ra)
        pair_counts.append(rp)
        stabilizers.append(fixing)
        if rp >= threshold:
            good_counts.append(rp)
        if (x, y) in engineered:
            engineered_counts.append(rp)
        rows.append({"pair": [index[x], index[y]], "output_index": output_index[values[x, y]],
                     "returning_action_indices": returning,
                     "returned_pairs": sorted(targets), "fixing_actions": fixing,
                     "engineered": (x, y) in engineered})
    fibers = Counter(values.values())
    summary = {
        "A_size": n, "ordered_pairs": n*n, "action_size": len(U),
        "engineered_pair_count": len(engineered_counts),
        "engineered_complement": n*n-len(engineered_counts),
        "engineered_density": str(F(len(engineered_counts), n*n)),
        "return_threshold": threshold, "controlled_G": len(good_counts),
        "bad_B": n*n-len(good_counts),
        "min_return_outside_bad_set": min(good_counts) if good_counts else None,
        "R_action": statistics(action_counts, d), "R_pair": statistics(pair_counts, d),
        "engineered_R_pair": statistics(engineered_counts, d) if engineered_counts else None,
        "stabilizer_histogram": dict(sorted(Counter(stabilizers).items())),
        "full_Q_image_size": len(outputs),
        "image_fiber_histogram": dict(sorted(Counter(fibers.values()).items())),
        "reciprocal_HR1_bound": str(sum((F(1, r) for r in pair_counts), F(0))),
    }
    raw = {"A": list(map(str, A)), "actions": [list(map(str, u)) for u in U],
           "outputs": list(map(str, outputs)), "pairs": rows}
    return summary, raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pairs-output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == args.pairs_output.resolve():
        raise ValueError("summary and raw-pair paths must be different")
    for path in (args.output, args.pairs_output):
        if path.exists():
            raise FileExistsError(path)
        path.parent.mkdir(parents=True, exist_ok=True)
    budget = Budget()
    started = time.perf_counter()
    results, raw_cases = [], []
    error = None
    try:
        for family, d in CASES:
            data = blocks(d)
            units = action_box(data, budget)
            A, engineered, definition = carrier(family, d, data, units)
            required = 2*len(A)**2*(1+len(units))
            if budget.total+required > budget.cap:
                raise RuntimeError("preflight evaluation bound exceeds remaining budget")
            result, raw = measure(A, units, engineered, d, budget)
            result.update({"family": family, "d": d, "definition": definition})
            if family == "faithful_ternary_gap":
                assert result["R_pair"]["maximum"] == 1
                assert 81*result["full_Q_image_size"] >= len(A)**2
            results.append(result)
            raw_cases.append({"family": family, "d": d, **raw})
            budget.check_time()
    except Exception as exc:
        error = repr(exc)
        raise
    finally:
        source = Path(__file__)
        output = {"cases": results, "error": error, "reproducibility": {
            "command_argv": sys.argv, "python": platform.python_version(),
            "cases_fixed_before_run": CASES, "network_attempted": False, "seed": None,
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "arithmetic_source_sha256": hashlib.sha256(source.with_name("unit_exponent.py").read_bytes()).hexdigest(),
            "charged_evaluations": budget.total, "categories": dict(budget.counts),
            "cpu_seconds": budget.cpu_seconds(), "wall_seconds": time.perf_counter()-started,
            "evaluation_cap": budget.cap, "cpu_cap_seconds": budget.cpu_cap,
            "exact_equalities": True, "geometric_mean_display_only": "floating point"}}
        with args.output.open("x") as stream:
            json.dump(output, stream, indent=2, sort_keys=True)
            stream.write("\n")
        with args.pairs_output.open("x") as stream:
            json.dump(raw_cases, stream, separators=(",", ":"))
            stream.write("\n")
    print(json.dumps({"cases": [{k: r[k] for k in
         ("family", "d", "A_size", "controlled_G", "bad_B", "full_Q_image_size", "R_pair")}
         for r in results], "reproducibility": output["reproducibility"]}, indent=2))


if __name__ == "__main__":
    main()
