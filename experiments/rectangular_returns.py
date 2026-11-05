"""Frozen DC-O1 exact scouts: six cases in two concrete mechanisms.

The local signed gadget and its two balanced-state realizations are one
mechanism; three moving-pole correlated-word carriers are the other.
All selected actions and all rectangular input pairs are checked, together
with the full union-square image. No formal tensor return is credited.
"""

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import platform
import sys
import time

from .unit_exponent import (Budget, action, conjugate, mul, norm,
                            oracle_action, oracle_q, q)


CASES = (("local_signed_rectangle", 1), ("balanced_states", 2),
         ("balanced_states", 4), ("moving_poles", 3),
         ("moving_poles", 4), ("moving_poles", 5))


def fourth_root_ceiling(n):
    t = 1
    while t**4 < n:
        t += 1
    return t


def stats(values):
    if not values:
        return None
    counts = Counter(values)
    ordered = sorted(values)
    size = len(values)
    return {"histogram": dict(sorted(counts.items())), "population": size,
            "minimum": min(values), "maximum": max(values),
            "median": str(F(ordered[(size-1)//2]+ordered[size//2], 2)),
            "mean": str(F(sum(values), size)),
            "one_return_fraction": str(F(counts.get(1, 0), size)),
            "geometric_mean_approx": math.exp(sum(c*math.log(r) for r, c in counts.items())/size),
            "geometric_mean_exact": "("+" * ".join(f"{r}^{c}" for r, c in sorted(counts.items()))+f")^(1/{size})"}


def make_case(family, d, budget):
    if family in {"local_signed_rectangle", "balanced_states"}:
        plus, minus = (F(15, 13), F(8, 13)), (F(3, 7), F(8, 7))
        positive = [(F(1), F(0)), plus, conjugate(plus), minus, conjugate(minus)]
        U = sorted({tuple(sign*a for a in u) for u in positive for sign in (-1, 1)})
        assert len(U) == 10
        if family == "local_signed_rectangle":
            X, Y = [F(-1), F(1)], [F(-3), F(3)]
            masks = None
            definition = {"S": [-1, 1], "T": [-3, 3]}
        else:
            assert d % 2 == 0
            words = [w for w in product((-3, -1, 1, 3), repeat=d)
                     if sum(abs(v) == 1 for v in w) == d//2]
            encoded = {F(sum(a*100**i for i, a in enumerate(w))): w for w in words}
            assert len(encoded) == len(words) == math.comb(d, d//2)*2**d
            X = Y = sorted(encoded)
            masks = {x: tuple(abs(a) == 1 for a in w) for x, w in encoded.items()}
            definition = {"base": 100, "digits": [-3, -1, 1, 3],
                          "abs_one_count": d//2,
                          "compatible_pair_count_formula": math.comb(d, d//2)*4**d}
    elif family == "moving_poles":
        B = (10*(d+2))**(4*d)
        generators = []
        for j in range(1, d+1):
            t = B-j
            alpha = (F(t), F(-1))
            generators.append(tuple(c/(t*t+t+1) for c in mul(alpha, alpha)))
        U = []
        for exponents in product((-1, 0, 1), repeat=d):
            value = (F(1), F(0))
            for e, u in zip(exponents, generators):
                if e:
                    value = mul(value, u if e == 1 else conjugate(u))
            U.append(value)
        assert len(set(U)) == 3**d
        words = [w for w in product((-1, 0, 1), repeat=d) if sum(w) == 0]
        X = Y = sorted(F(sum(a*B**i for i, a in enumerate(w))) for w in words)
        assert len(set(X)) == len(words)
        masks = None
        definition = {"base": str(B), "digits": [-1, 0, 1], "digit_sum": 0,
                      "pole_indices": [1, d], "exponent_window": [-1, 1]}
    else:
        raise ValueError(family)
    for u in U:
        budget.charge("constructed_action_norm_check")
        assert norm(u) == 1
    return X, Y, U, masks, definition


def measure(X, Y, U, budget, masks=None):
    X, Y = tuple(map(F, X)), tuple(map(F, Y))
    assert len(set(X)) == len(X) and len(set(Y)) == len(Y)
    assert len(set(U)) == len(U) and (F(1), F(0)) in U
    xs, ys = set(X), set(Y)
    A = sorted(xs | ys)
    index = {x: i for i, x in enumerate(A)}
    n = len(A)
    threshold = fourth_root_ceiling(n)
    needed = 2*n*n+2*len(X)*len(Y)*len(U)
    if budget.total+needed > budget.cap:
        raise RuntimeError("case exceeds remaining shared query budget")
    values = {}
    for x, y in product(A, repeat=2):
        budget.charge("union_square_Q_query")
        z = q(x, y)
        budget.charge("independent_union_square_Q_query")
        assert z == oracle_q(x, y)
        values[x, y] = z
    outputs = sorted(set(values.values()))
    output_index = {z: i for i, z in enumerate(outputs)}
    rows, rp, ra, stabs, good = [], [], [], [], []
    compatible = 0
    domain_sizes = [0]*len(U)
    for x, y in product(X, Y):
        returned, legal = set(), []
        fixing = 0
        for j, u in enumerate(U):
            budget.charge("rectangular_action_query")
            target = action(u, x, y)
            budget.charge("independent_rectangular_action_query")
            assert target == oracle_action(u, x, y)
            if target[0] in xs and target[1] in ys:
                assert values[target] == values[x, y]
                legal.append(j)
                domain_sizes[j] += 1
                returned.add((index[target[0]], index[target[1]]))
                fixing += target == (x, y)
        assert returned
        a, r = len(legal), len(returned)
        if (x, y) == (0, 0):
            assert r == 1 and a == fixing == len(U)
        else:
            assert a == r and fixing == 1
        ra.append(a); rp.append(r); stabs.append(fixing)
        if r >= threshold:
            good.append(r)
        is_compatible = None
        if masks is not None:
            is_compatible = all(i != j for i, j in zip(masks[x], masks[y]))
            compatible += is_compatible
        rows.append({"pair": [index[x], index[y]], "output_index": output_index[values[x, y]],
                     "returning_actions": legal, "returned_pairs": sorted(returned),
                     "fixing_actions": fixing, "complementary_masks": is_compatible})
    summary = {"X_size": len(X), "Y_size": len(Y), "union_size": n,
               "symmetric_difference": len(xs ^ ys), "rectangle_pairs": len(X)*len(Y),
               "action_size": len(U), "epsilon_threshold": "1/4", "integer_threshold": threshold,
               "good_pairs": len(good), "bad_pairs": len(rp)-len(good),
               "bad_fraction": str(F(len(rp)-len(good), len(rp))),
               "R_pair": stats(rp), "R_action": stats(ra), "good_returns": stats(good),
               "stabilizer_histogram": dict(sorted(Counter(stabs).items())),
               "return_domain_sizes": domain_sizes,
               "compatible_pairs": compatible if masks is not None else None,
               "full_union_Q_image": len(outputs),
               "rectangular_Q_image": len({values[p] for p in product(X, Y)}),
               "union_image_fiber_histogram": dict(sorted(Counter(Counter(values.values()).values()).items()))}
    raw = {"A": list(map(str, A)), "X_indices": [index[x] for x in X],
           "Y_indices": [index[y] for y in Y], "U": [list(map(str, u)) for u in U],
           "outputs": list(map(str, outputs)), "pairs": rows}
    return summary, raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pairs-output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == args.pairs_output.resolve():
        raise ValueError("summary and raw paths must differ")
    for path in (args.output, args.pairs_output):
        if path.exists():
            raise FileExistsError(path)
        path.parent.mkdir(parents=True, exist_ok=True)
    budget = Budget()
    wall_start = time.perf_counter()
    results, raw_cases = [], []
    error = None
    try:
        for family, d in CASES:
            X, Y, U, masks, definition = make_case(family, d, budget)
            row, raw = measure(X, Y, U, budget, masks)
            row.update({"family": family, "d": d, "definition": definition})
            if family == "moving_poles":
                assert row["R_pair"]["maximum"] <= 27
            if family == "balanced_states":
                assert row["compatible_pairs"] == definition["compatible_pair_count_formula"]
            results.append(row)
            raw_cases.append({"family": family, "d": d, **raw})
            budget.check_time()
    except Exception as exc:
        error = repr(exc)
        raise
    finally:
        source = Path(__file__)
        output = {"cases": results, "error": error, "reproducibility": {
            "command_argv": sys.argv, "python": platform.python_version(),
            "fixed_cases": CASES, "network_attempted": False, "seed": None,
            "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "arithmetic_sha256": hashlib.sha256(source.with_name('unit_exponent.py').read_bytes()).hexdigest(),
            "charged_evaluations": budget.total, "categories": dict(budget.counts),
            "cpu_seconds": budget.cpu_seconds(), "wall_seconds": time.perf_counter()-wall_start,
            "evaluation_cap": budget.cap, "cpu_cap_seconds": budget.cpu_cap,
            "equality_arithmetic": "exact Fraction", "geometric_mean_display": "floating point only"}}
        with args.output.open('x') as f:
            json.dump(output, f, indent=2, sort_keys=True);f.write('\n')
        with args.pairs_output.open('x') as f:
            json.dump(raw_cases, f, separators=(',', ':'));f.write('\n')
    print(json.dumps({"cases": [{k: r[k] for k in ('family','d','X_size','Y_size','union_size','symmetric_difference','action_size','good_pairs','bad_pairs','full_union_Q_image','R_pair')} for r in results], "reproducibility": output['reproducibility']}, indent=2))


if __name__ == '__main__':
    main()
