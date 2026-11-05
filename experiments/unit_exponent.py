"""Frozen offline unit-exponent and one sparse valuation-box diagnostic.

Only L=h=1 and d=1,2,3 are run, for the two specified carriers. All
arithmetic equalities use Fraction. An independent sqrt(-3) representation
checks every action and polynomial value. No factoring or network is used.
Each constructed action norm check, orbit/action test, scalar Q evaluation,
or action/pair test costs one, including the independent oracle. Algebraic
operations within those queries are not separate charges.
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


class Budget:
    def __init__(self, cap=2_000_000, cpu_cap=600):
        self.cap, self.cpu_cap = cap, cpu_cap
        self.counts = Counter()
        self.total = 0
        self.started = time.process_time()

    def charge(self, category):
        if self.total >= self.cap:
            raise RuntimeError("evaluation cap exhausted before query")
        self.total += 1
        self.counts[category] += 1
        if self.total % 128 == 0:
            self.check_time()

    def cpu_seconds(self):
        return time.process_time() - self.started

    def check_time(self):
        if self.cpu_seconds() > self.cpu_cap:
            raise RuntimeError("research CPU cap exhausted")


def mul(z, w):
    """Multiply coefficients a+b*omega in Q(omega)."""
    a, b = z
    c, e = w
    return a*c-b*e, a*e+b*c-b*e


def conjugate(z):
    a, b = z
    return a-b, -b


def norm(z):
    a, b = z
    return a*a-a*b+b*b


def action(u, x, y):
    a, b = u
    return a*x+b*y, -b*x+(a-b)*y


def q(x, y):
    return x*x+x*y+y*y


def oracle_action(u, x, y):
    """Independent real/sqrt(-3) coordinates and complex multiplication."""
    a, b = u
    real_u, imag_u = a-b/2, b/2
    real_z, imag_z = x+y/2, -y/2
    real_out = real_u*real_z-3*imag_u*imag_z
    imag_out = real_u*imag_z+imag_u*real_z
    return real_out+imag_out, -2*imag_out


def oracle_q(x, y):
    return ((2*x+y)**2+3*y*y)/4


def blocks(d):
    previous = 1
    result = []
    for _ in range(d):
        t = 3*previous**3
        modulus = t*t+t+1
        assert modulus > 6*previous**4
        assert modulus % (3*previous) == 1
        alpha = (F(t), F(-1))
        numerator = mul(alpha, alpha)
        unit = tuple(value/modulus for value in numerator)
        result.append((t, modulus, unit))
        previous *= modulus
    return result


def action_box(data, budget):
    units = {}
    for exponents in product((-1, 0, 1), repeat=len(data)):
        value = (F(1), F(0))
        for exponent, (_, _, unit) in zip(exponents, data):
            if exponent:
                value = mul(value, unit if exponent == 1 else conjugate(unit))
        budget.charge("constructed_action_norm_checks")
        assert norm(value) == 1
        units[exponents] = value
    assert len(set(units.values())) == 3**len(data)
    return units


def histogram(values):
    return dict(sorted(Counter(values).items()))


def statistics(values, d):
    counts = Counter(values)
    n = len(values)
    ordered = sorted(values)
    median = F(ordered[(n-1)//2]+ordered[n//2], 2)
    mean = F(sum(values), n)
    log_mean = sum(count*math.log(k) for k, count in counts.items())/n
    return {
        "histogram": dict(sorted(counts.items())), "population": n,
        "minimum": min(values), "median": str(median),
        "arithmetic_mean": str(mean), "maximum": max(values),
        "geometric_mean_approx": math.exp(log_mean),
        "geometric_mean_exact": "("+" * ".join(f"{k}^{v}" for k, v in sorted(counts.items()))+f")^(1/{n})",
        "identity_only_fraction": str(F(counts.get(1, 0), n)),
        "strict_threshold_fractions": {
            str(k): str(F(sum(v for r, v in counts.items() if r < k), n))
            for k in sorted({2**d, 3**d})},
    }


def point_text(point):
    return [str(v) for v in point]


def digest(points):
    encoded = [point_text(p) for p in sorted(points)]
    return hashlib.sha256(json.dumps(encoded, separators=(",", ":")).encode()).hexdigest()


def scalar_case(family, d, data, units, budget):
    z_values = set(units.values())
    orbit_rows = []
    if family == "orbit_projection":
        engineered = {(a, -b) for a, b in z_values}
        carrier = sorted({v for xy in engineered for v in xy})
        for exponents, z in units.items():
            returning = set()
            for unit in units.values():
                budget.charge("orbit_action_tests")
                target = mul(unit, z)
                if target in z_values:
                    returning.add(target)
            expected = math.prod(3 if e == 0 else 2 for e in exponents)
            assert len(returning) == expected
            orbit_rows.append({"exponents": exponents, "returns": expected})
        projection = {
            "x_fibers": histogram(list(Counter(x for x, _ in engineered).values())),
            "y_fibers": histogram(list(Counter(y for _, y in engineered).values())),
            "tagged_coefficient_fibers": histogram(list(Counter(v for xy in engineered for v in xy).values())),
        }
        z_size = len(z_values)
        z_definition = "single norm-one exponent orbit; engineered subset of A^2"
    else:
        scalar_labels = []
        for exponents in product((-1, 0, 1), repeat=d):
            value = F(1)
            for exponent, (_, modulus, _) in zip(exponents, data):
                value *= F(modulus)**exponent
            scalar_labels.extend((value, -value))
        assert len(set(scalar_labels)) == 2*3**d
        carrier = sorted(scalar_labels)
        engineered = set(product(carrier, repeat=2))
        z_size = len(carrier)**2
        z_definition = "full coefficient carrier A-omega*A, not a single norm orbit"
        projection = {"scalar_parameter_fibers": {1: len(carrier)},
                      "pair_parameter_fibers": {1: len(carrier)**2}}

    carrier_set = set(carrier)
    norms = {}
    for x, y in product(carrier, repeat=2):
        budget.charge("scalar_polynomial_evaluations")
        norms[x, y] = q(x, y)

    rows = []
    for x, y in product(carrier, repeat=2):
        returned = set()
        primary_targets = {}
        action_count = fixing = 0
        for unit in units.values():
            budget.charge("scalar_action_pair_tests")
            target = action(unit, x, y)
            primary_targets[unit] = target
            if target[0] in carrier_set and target[1] in carrier_set:
                action_count += 1
                returned.add(target)
                fixing += target == (x, y)
                assert norms[target] == norms[x, y]
        oracle_returned = set()
        oracle_count = oracle_fixing = 0
        for unit in units.values():
            budget.charge("oracle_action_pair_tests")
            target = oracle_action(unit, x, y)
            assert target == primary_targets[unit]
            if target[0] in carrier_set and target[1] in carrier_set:
                oracle_count += 1
                oracle_returned.add(target)
                oracle_fixing += target == (x, y)
        budget.charge("oracle_polynomial_evaluations")
        assert oracle_q(x, y) == norms[x, y]
        assert (oracle_returned, oracle_count, oracle_fixing) == (returned, action_count, fixing)
        assert fixing == (len(units) if x == y == 0 else 1)
        assert len(returned) == (1 if x == y == 0 else action_count)
        rows.append({"x": str(x), "y": str(y), "q": str(norms[x, y]),
                     "R_label": action_count, "R_action": action_count,
                     "R_pair": len(returned), "stabilizer_in_tested_U": fixing,
                     "engineered": (x, y) in engineered,
                     "returned_pairs_sha256": digest(returned)})

    fibers = Counter(norms.values())
    if family == "valuation_box":
        m = 3**d
        assert len(fibers) == m*m+m
        assert Counter(fibers.values()) == Counter({4: m*(m-1), 2: 2*m})
        assert all(row["R_pair"] == row["R_action"] == 1 for row in rows)

    result = {
        "family": family, "d": d, "L": 1, "h": 1,
        "A_size": len(carrier), "Z_size": z_size, "Z_definition": z_definition,
        "action_size": len(units), "formal_action_labels": len(units),
        "carrier": [str(v) for v in carrier],
        "ordered_pairs": len(rows), "engineered_pairs": len(engineered),
        "engineered_density": str(F(len(engineered), len(rows))),
        "uncontrolled_pairs_by_engineered_certificate": len(rows)-len(engineered),
        "R_label": statistics([r["R_label"] for r in rows], d),
        "R_action": statistics([r["R_action"] for r in rows], d),
        "R_pair": statistics([r["R_pair"] for r in rows], d),
        "finite_stabilizer_distribution": histogram([r["stabilizer_in_tested_U"] for r in rows]),
        "full_group_stabilizers": "trivial off (0,0); entire infinite action group at (0,0)",
        "projection_fibers": projection, "full_Q_image_size": len(fibers),
        "Q_fiber_histogram": histogram(list(fibers.values())),
        "norm_one_fiber_size": fibers.get(F(1), 0),
        "HR1_reciprocal_sum": str(sum((F(1, r["R_pair"]) for r in rows), F(0))),
        "oracle": "PASS: every action, returned set, Q-value and finite stabilizer checked independently",
    }
    if orbit_rows:
        result["R_Z"] = statistics([r["returns"] for r in orbit_rows], d)
    return result, {"family": family, "d": d, "pairs": rows, "orbit_rows": orbit_rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pairs-output", type=Path, required=True)
    args = parser.parse_args()
    paths = (args.output, args.pairs_output)
    if paths[0].resolve() == paths[1].resolve() or any(p.exists() for p in paths):
        parser.error("outputs must be distinct new paths")
    budget = Budget()
    wall_start = time.perf_counter()
    results, all_rows = [], []
    try:
        data = blocks(3)
        for d in (1, 2, 3):
            units = action_box(data[:d], budget)
            for family in ("orbit_projection", "valuation_box"):
                result, rows = scalar_case(family, d, data[:d], units, budget)
                results.append(result)
                all_rows.append(rows)
        budget.check_time()
    except Exception:
        print(json.dumps({"failed": True, "charged_evaluations": budget.total,
                          "categories": dict(budget.counts), "cpu_seconds": budget.cpu_seconds()}), file=sys.stderr)
        raise
    output = {
        "status": "EXPERIMENTAL: exact exhaustive finite corroboration; proofs are separate",
        "fixed_schedule": {"d": [1, 2, 3], "L": 1, "h": 1,
                           "families": ["orbit_projection", "valuation_box"]},
        "blocks": [{"t": str(t), "q": str(qi), "u_coefficients": point_text(u)} for t, qi, u in data],
        "cases": results,
        "reproducibility": {
            "command": sys.argv, "python": platform.python_version(),
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "charged_evaluations": budget.total, "categories": dict(budget.counts),
            "cpu_seconds": budget.cpu_seconds(), "wall_seconds": time.perf_counter()-wall_start,
            "evaluation_cap": budget.cap, "cpu_cap_seconds": budget.cpu_cap,
            "seed": None, "network_attempted": False,
        },
    }
    for p in paths:
        p.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as f:
        f.write(json.dumps(output, indent=2, sort_keys=True)+"\n")
    with args.pairs_output.open("x") as f:
        f.write(json.dumps(all_rows, separators=(",", ":"))+"\n")
    print(json.dumps({"cases": [{k: r[k] for k in ("family", "d", "A_size", "Z_size", "action_size", "full_Q_image_size", "R_pair")} for r in results], "reproducibility": output["reproducibility"]}, indent=2))


if __name__ == "__main__":
    main()
