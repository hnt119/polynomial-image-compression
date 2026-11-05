"""Bounded exact full-image diagnostics, commissioned 2026-09-16.

Run with ``python3 -m experiments.solvable_norm_trace --output PATH``.
This is a finite experiment, not an asymptotic compression certificate.
Only integer power-basis arithmetic is used for equality and collisions.
"""

import argparse
from collections import Counter
import hashlib
from itertools import product
import json
from pathlib import Path
import platform
import sys
import time


def digest(value):
    return hashlib.sha256(json.dumps(value, separators=(",", ":")).encode()).hexdigest()


class Order:
    """Z[t]/(f), for one of the explicitly documented irreducible monic f."""

    def __init__(self, coefficients):
        self.f = tuple(coefficients)  # low to high, monic term omitted
        self.degree = len(self.f)
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)

    def add(self, x, y):
        return tuple(a + b for a, b in zip(x, y))

    def neg(self, x):
        return tuple(-a for a in x)

    def mul(self, x, y):
        d = self.degree
        c = [0] * (2 * d - 1)
        for i, a in enumerate(x):
            for j, b in enumerate(y):
                c[i + j] += a * b
        for k in range(2 * d - 2, d - 1, -1):
            a = c[k]
            for j, b in enumerate(self.f):
                c[k - d + j] -= a * b
        return tuple(c[:d])

    def trace(self, x):
        # Trace of the multiplication matrix, independent of root approximation.
        return sum(self.mul(x, tuple(int(i == j) for i in range(self.degree)))[j]
                   for j in range(self.degree))

    def norm(self, x):
        # Integer Bareiss determinant of the multiplication matrix.
        d = self.degree
        columns = [self.mul(x, tuple(int(i == j) for i in range(d))) for j in range(d)]
        matrix = [list(row) for row in zip(*columns)]
        previous, sign = 1, 1
        for k in range(d - 1):
            pivot_row = next((i for i in range(k, d) if matrix[i][k]), None)
            if pivot_row is None:
                return 0
            if pivot_row != k:
                matrix[k], matrix[pivot_row] = matrix[pivot_row], matrix[k]
                sign = -sign
            pivot = matrix[k][k]
            for i in range(k + 1, d):
                for j in range(k + 1, d):
                    numerator = pivot * matrix[i][j] - matrix[i][k] * matrix[k][j]
                    assert numerator % previous == 0
                    matrix[i][j] = numerator // previous
                matrix[i][k] = 0
            previous = pivot
        return sign * matrix[-1][-1]


FIELDS = (
    # name, minimal polynomial (low to high sans leading 1), unit, inverse
    ("cyclic_cubic", (1, -3, 0), (0, 1, 0), (3, 0, -1)),
    ("s3_real_cubic", (-2, 0, 0), (-1, 1, 0), (1, 1, 1)),
    ("biquadratic", (1, 0, -10, 0), (0, 1, 0, 0), (0, 10, 0, -1)),
)


class Budget:
    def __init__(self, pairs=500000, seconds=120):
        self.limit = pairs
        self.seconds = seconds
        self.pairs = 0
        self.started = time.process_time()

    def charge(self, pairs):
        if self.pairs + pairs > self.limit:
            raise RuntimeError("Exact pair budget exceeded")
        self.check_time()
        self.pairs += pairs

    def check_time(self):
        if time.process_time() - self.started > self.seconds:
            raise RuntimeError("CPU budget exceeded")


def summarize(values, counts):
    n = len(values)
    return {
        "n": n,
        "ordered_pairs": n * n,
        "image_size": len(counts),
        "fiber_histogram": dict(sorted(Counter(counts.values()).items())),
        "input_sha256": digest(sorted(values)),
        "output_sha256": digest(sorted(counts)),
        "largest_coefficient": max(abs(c) for v in values for c in v),
    }


def image_counts(order, values, budget):
    values = sorted(set(values))
    budget.charge(4 * len(values) ** 2)
    squares = {a: order.mul(a, a) for a in values}
    q_counts, p_counts = Counter(), Counter()
    sums, products = set(), set()
    for x in values:
        budget.check_time()
        for y in values:
            xy = order.mul(x, y)
            sums.add(order.add(x, y))
            products.add(xy)
            q = order.add(order.add(squares[x], xy), squares[y])
            q_counts[q] += 1
            p_counts[order.add(q, x)] += 1
    return {"q": summarize(values, q_counts), "q_plus_x": summarize(values, p_counts),
            "sum_size": len(sums), "product_size": len(products)}


def hybrid(order, unit, inverse, depth):
    assert order.mul(unit, inverse) == order.one
    units = {order.one}
    positive = negative = order.one
    for _ in range(depth):
        positive = order.mul(positive, unit)
        negative = order.mul(negative, inverse)
        units.update((positive, negative))
    box = {tuple(v + (4 if i == 0 else 0) for i, v in enumerate(bits))
           for bits in product((0, 1), repeat=order.degree)}
    values = {order.mul(g, b) for g in units for b in box}
    return values, len(units) * len(box)


def sign_cube(primes, budget):
    m = len(primes)
    values = list(product((-1, 1), repeat=m))
    budget.charge(2 * len(values) ** 2)
    q_counts, p_counts = Counter(), Counter()
    for x in values:
        budget.check_time()
        for y in values:
            constant = sum(p * (2 + a * b) for p, a, b in zip(primes, x, y))
            cross = tuple(2*x[i]*x[j] + x[i]*y[j] + y[i]*x[j] + 2*y[i]*y[j]
                          for i in range(m) for j in range(i+1, m))
            # Canonical basis: 1, sqrt(p_i), sqrt(p_i p_j).
            q_counts[(constant,) + (0,) * m + cross] += 1
            p_counts[(constant,) + x + cross] += 1
    return {"q": summarize(values, q_counts), "q_plus_x": summarize(values, p_counts)}


def run():
    budget = Budget()
    rows = []
    for name, f, unit, inverse in FIELDS:
        order = Order(f)
        for depth in (0, 1, 2, 4):
            values, parameter_count = hybrid(order, unit, inverse, depth)
            rows.append({"family": "unit_times_additive_box", "field": name,
                         "minimal_polynomial_low_first": f + (1,), "depth": depth,
                         "parameter_count": parameter_count, "distinct_inputs": len(values),
                         "scalar_norm_size": len({order.norm(v) for v in values}),
                         "results": image_counts(order, values, budget)})
            # An actual scalar trace carrier, not a projection of the output image.
            traces = {(order.trace(v),) for v in values}
            rows.append({"family": "trace_of_unit_times_box", "field": name,
                         "depth": depth, "parameter_count": parameter_count,
                         "pretrace_inputs": len(values), "distinct_inputs": len(traces),
                         "results": image_counts(Order((0,)), traces, budget)})
    primes = (2, 3, 5, 7, 11, 13, 17, 19)
    for m in range(1, 9):
        rows.append({"family": "multiquadratic_sign_cube", "m": m,
                     "primes": primes[:m], "field_degree": 2 ** m,
                     "results": sign_cube(primes[:m], budget)})
    return {"status": "EXPERIMENTAL; exact exhaustive pairs for the listed finite sets",
            "date": "2026-09-16", "python": platform.python_version(),
            "command": "python3 -m experiments.solvable_norm_trace " + " ".join(sys.argv[1:]),
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "seed": None, "carrier_families": 7,
            "pair_evaluations": budget.pairs, "pair_limit": budget.limit,
            "cpu_seconds": time.process_time() - budget.started,
            "cpu_limit_seconds": budget.seconds, "results": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Refusing to overwrite an existing experiment record")
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "results"}, indent=2))


if __name__ == "__main__":
    main()
