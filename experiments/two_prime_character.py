"""One frozen exact 7,19 character-correlated residue experiment.

This is a finite-ring computation, not a real-carrier construction. The only
case is D={x mod 133: x is a unit and chi_7(x)=chi_19(x)} and the full norm-one
group in (Z/133Z)[omega]. A separate oracle uses the two split coordinates at
each prime. No former carrier schedule is called. Only the standard library
is used; there is no network access. Equality and histograms are exact.

Budget units: each tested norm-one coefficient candidate, action-pair test,
or standalone polynomial evaluation costs one. Group parametrization and
ordinary arithmetic within a charged test are not separate evaluations.
"""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import platform
import sys
import time


MODULUS = 133
ROOTS = {7: (2, 4), 19: (7, 11)}


class Budget:
    def __init__(self, cap=2_000_000, cpu_cap=600):
        self.cap = cap
        self.cpu_cap = cpu_cap
        self.counts = Counter()
        self.total = 0
        self.started = time.process_time()

    def charge(self, kind):
        if self.total >= self.cap:
            raise RuntimeError("charged evaluation cap exceeded")
        self.total += 1
        self.counts[kind] += 1
        if self.total % 1024 == 0 and self.cpu_seconds() > self.cpu_cap:
            raise RuntimeError("research CPU cap exceeded")

    def cpu_seconds(self):
        return time.process_time() - self.started


def character(value, prime):
    residue = pow(value % prime, (prime - 1) // 2, prime)
    return -1 if residue == prime - 1 else residue


def q(x, y, modulus):
    return (x*x + x*y + y*y) % modulus


def crt(a, b):
    return (a + 7 * (((b-a) * 11) % 19)) % MODULUS


def split_action(t, x, y, prime):
    """Independent diagonal action and inverse coordinate reconstruction."""
    w, wb = ROOTS[prime]
    first = t * (x - w*y) % prime
    second = pow(t, -1, prime) * (x - wb*y) % prime
    yy = (second-first) * pow(w-wb, -1, prime) % prime
    xx = (first + w*yy) % prime
    return xx, yy


def split_coefficients(t, prime):
    w, wb = ROOTS[prime]
    beta = (t-pow(t, -1, prime)) * pow(w-wb, -1, prime) % prime
    return (t-beta*w) % prime, beta


def fraction_text(value):
    return str(value.numerator) if value.denominator == 1 else str(value)


def returned_digest(points):
    return hashlib.sha256(json.dumps(sorted(points), separators=(",", ":")).encode()).hexdigest()


def frozen_case(budget):
    carrier = [x for x in range(MODULUS)
               if character(x, 7) != 0
               and character(x, 7) == character(x, 19)]
    carrier_set = set(carrier)
    assert len(carrier) == 54

    group = []
    for alpha, beta in product(range(MODULUS), repeat=2):
        budget.charge("primary_norm_candidates")
        if (alpha*alpha-alpha*beta+beta*beta) % MODULUS == 1:
            group.append((alpha, beta))
    assert len(group) == 108 and len(set(group)) == 108

    norms = {}
    for x, y in product(carrier, repeat=2):
        budget.charge("primary_polynomial_evaluations")
        norms[x, y] = q(x, y, MODULUS)

    rows = []
    for x, y in product(carrier, repeat=2):
        returned = set()
        raw_count = stabilizer = 0
        for alpha, beta in group:
            budget.charge("primary_action_pair_tests")
            xx = (alpha*x+beta*y) % MODULUS
            yy = (-beta*x+(alpha-beta)*y) % MODULUS
            if xx in carrier_set and yy in carrier_set:
                raw_count += 1
                returned.add((xx, yy))
                stabilizer += (xx, yy) == (x, y)
                assert norms[xx, yy] == norms[x, y]
        assert raw_count == len(returned) and stabilizer == 1
        rows.append({"x": x, "y": y, "norm": norms[x, y],
                     "returns": raw_count, "distinct_returned_pairs": len(returned),
                     "returned_pairs_sha256": returned_digest(returned),
                     "stabilizer": stabilizer})

    # Independent field-product representation: no CRT carrier membership
    # test or primary action formula is used for the returned points.
    local_groups = {}
    for prime in (7, 19):
        local = set()
        for alpha, beta in product(range(prime), repeat=2):
            budget.charge("oracle_local_norm_candidates")
            if (alpha*alpha-alpha*beta+beta*beta) % prime == 1:
                local.add((alpha, beta))
        parametrized = {split_coefficients(t, prime) for t in range(1, prime)}
        assert local == parametrized
        local_groups[prime] = parametrized
    lifted_group = {(crt(a7, a19), crt(b7, b19))
                    for a7, b7 in local_groups[7]
                    for a19, b19 in local_groups[19]}
    assert lifted_group == set(group)
    oracle_carrier = {(a, b) for a in range(1, 7) for b in range(1, 19)
                      if character(a, 7) == character(b, 19)}
    assert {(x % 7, x % 19) for x in carrier} == oracle_carrier
    oracle_norms = Counter()
    for row in rows:
        x, y = row["x"], row["y"]
        budget.charge("oracle_polynomial_evaluations")
        norm_pair = (q(x % 7, y % 7, 7), q(x % 19, y % 19, 19))
        oracle_norms[norm_pair] += 1
        assert crt(*norm_pair) == row["norm"]
        oracle_returned = set()
        for t7, t19 in product(range(1, 7), range(1, 19)):
            budget.charge("oracle_action_pair_tests")
            x7, y7 = split_action(t7, x % 7, y % 7, 7)
            x19, y19 = split_action(t19, x % 19, y % 19, 19)
            if (x7, x19) in oracle_carrier and (y7, y19) in oracle_carrier:
                oracle_returned.add(((x7, x19), (y7, y19)))
        assert len(oracle_returned) == row["returns"]
        scalar_returned = {(crt(*xx), crt(*yy)) for xx, yy in oracle_returned}
        assert returned_digest(scalar_returned) == row["returned_pairs_sha256"]

    histogram = Counter(row["returns"] for row in rows)
    expected = {8: 216, 10: 270, 12: 216, 18: 108,
                24: 648, 26: 702, 30: 540, 54: 216}
    assert histogram == expected  # Independent symbolic prediction, frozen first.
    fibers = Counter(norms.values())
    assert Counter(fibers.values()) == Counter(oracle_norms.values())
    count = len(rows)
    sorted_returns = sorted(row["returns"] for row in rows)
    mean = sum(Fraction(k*h, count) for k, h in histogram.items())
    reciprocal_mean = sum(Fraction(h, count*k) for k, h in histogram.items())
    mean_log = sum(h*math.log(k)/count for k, h in histogram.items())
    result = {
        "claim_status": "EXPERIMENTAL: exact exhaustive finite verification",
        "scope": "Finite residue ring and coordinatewise products; not real scalar returns",
        "parameters": {"primes": [7, 19], "modulus": 133,
                       "carrier_rule": "units x with chi_7(x)=chi_19(x)",
                       "action": "all alpha+beta*omega of norm 1 modulo 133"},
        "carrier": carrier, "input_size": len(carrier), "ordered_pairs": count,
        "group_size": len(group), "return_histogram": dict(sorted(histogram.items())),
        "distinct_returned_pairs_histogram": dict(sorted(histogram.items())),
        "stabilizer_histogram": dict(Counter(row["stabilizer"] for row in rows)),
        "identity_only_count": histogram.get(1, 0),
        "identity_only_fraction": fraction_text(Fraction(histogram.get(1, 0), count)),
        "median": fraction_text(Fraction(sorted_returns[count//2-1]+sorted_returns[count//2], 2)),
        "mean": fraction_text(mean), "geometric_mean_approx": math.exp(mean_log),
        "mean_log_return_approx": mean_log,
        "geometric_mean_exact": "(" + " * ".join(f"{k}^{h}" for k, h in sorted(histogram.items())) + f")^(1/{count})",
        "minimum": min(histogram), "maximum": max(histogram),
        "reciprocal_mean": fraction_text(reciprocal_mean),
        "hr1_reciprocal_support_bound": fraction_text(count*reciprocal_mean),
        "strict_threshold_tails": {str(k): sum(h for r, h in histogram.items() if r < k)
                                   for k in range(1, len(group)+2)},
        "full_modular_image_size": len(fibers),
        "image_multiplicity_histogram": dict(sorted(Counter(fibers.values()).items())),
        "norm_zero_pairs": fibers[0],
        "missing_modular_outputs": [t for t in range(MODULUS) if t not in fibers],
        "normalized_crt_factor": fraction_text(Fraction(MODULUS*len(fibers), count)),
        "independent_oracle": "PASS: split diagonal action agrees at every ordered input pair",
        "numeric_limit": "Only logs/geometric mean are rounded; every equality, count and ratio is exact",
    }
    return result, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pairs-output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == args.pairs_output.resolve():
        parser.error("summary and pair outputs must be distinct")
    for path in (args.output, args.pairs_output):
        if path.exists():
            parser.error(f"refusing to overwrite {path}")
    budget = Budget()
    wall_start = time.perf_counter()
    try:
        result, rows = frozen_case(budget)
        if budget.cpu_seconds() > budget.cpu_cap:
            raise RuntimeError("research CPU cap exceeded")
    except Exception:
        print(json.dumps({"failed": True, "charged_evaluations": budget.total,
                          "counts": dict(budget.counts), "cpu_seconds": budget.cpu_seconds()}),
              file=sys.stderr)
        raise
    result["reproducibility"] = {
        "argv": sys.argv, "python": platform.python_version(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "charged_evaluations": budget.total, "evaluation_categories": dict(budget.counts),
        "cpu_seconds": budget.cpu_seconds(), "wall_seconds": time.perf_counter()-wall_start,
        "evaluation_cap": budget.cap, "cpu_cap_seconds": budget.cpu_cap,
        "seed": None, "network_attempted": False,
    }
    for path in (args.output, args.pairs_output):
        path.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        stream.write(json.dumps(result, indent=2, sort_keys=True)+"\n")
    with args.pairs_output.open("x") as stream:
        stream.write(json.dumps(rows, separators=(",", ":"))+"\n")
    print(json.dumps({key: result[key] for key in [
        "input_size", "ordered_pairs", "group_size", "return_histogram", "median", "mean",
        "geometric_mean_approx", "mean_log_return_approx", "full_modular_image_size",
        "reciprocal_mean", "normalized_crt_factor", "reproducibility"]}, indent=2))


if __name__ == "__main__":
    main()
