"""Bounded exact Eisenstein multiplier diagnostics in multiquadratic fields.

This separate T03 multiplier branch does not continue the adaptive radical
optimizer. Finite all-pairs counts are not an asymptotic construction.

Run: python3 -m experiments.eisenstein_solvable --output PATH
No archived programs or serialized field objects are imported.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
from itertools import product
import json
from math import lcm
from pathlib import Path
import platform
import sys
import time


PRIMES = (2, 3, 5)
PAIR_CAP = 600_000
ACTION_CAP = 1_000_000
CPU_CAP = 240.0
SCHEDULE = (("F1", 1), ("F1", 2), ("F1", 3), ("F2", 1),
            ("F2", 2), ("F3", 1), ("F3", 2), ("F3", 3))


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


class Multiquadratic:
    """Exact basis indexed by subsets of the distinct positive prime radicands.

    Independence of the prime square classes makes coefficient equality exact.
    The real embedding chooses every displayed square root positive.
    """

    def __init__(self, primes):
        self.primes = tuple(primes)
        if self.primes not in (PRIMES[:1], PRIMES[:2], PRIMES):
            raise ValueError("only the authorized prime prefixes are supported")
        self.dimension = 1 << len(primes)
        self.zero = (0,) * self.dimension
        self.one = (1,) + (0,) * (self.dimension - 1)
        overlap = [1] * self.dimension
        for mask in range(self.dimension):
            for i, p in enumerate(primes):
                if mask & (1 << i):
                    overlap[mask] *= p
        self.table = tuple(tuple((i ^ j, overlap[i & j])
                                 for j in range(self.dimension))
                           for i in range(self.dimension))

    def constant(self, value):
        return (value,) + (0,) * (self.dimension - 1)

    def root(self, i):
        result = [0] * self.dimension
        result[1 << i] = 1
        return tuple(result)

    @staticmethod
    def add(a, b):
        return tuple(x + y for x, y in zip(a, b))

    @staticmethod
    def neg(a):
        return tuple(-x for x in a)

    @staticmethod
    def sub(a, b):
        return tuple(x - y for x, y in zip(a, b))

    @staticmethod
    def scale(a, scalar):
        return tuple(scalar * x for x in a)

    def mul(self, a, b):
        result = [0] * self.dimension
        right = tuple((j, y) for j, y in enumerate(b) if y)
        for i, x in enumerate(a):
            if x:
                row = self.table[i]
                for j, y in right:
                    k, factor = row[j]
                    result[k] += x * y * factor
        return tuple(result)

    def q(self, a, b):
        return self.add(self.add(self.mul(a, a), self.mul(a, b)), self.mul(b, b))

    def eisenstein_mul(self, z, w):
        """Pairs (a,b) represent a - omega*b, omega^2 + omega + 1 = 0."""
        a, b = z
        c, d = w
        bd = self.mul(b, d)
        return (self.sub(self.mul(a, c), bd),
                self.add(self.add(self.mul(a, d), self.mul(b, c)), bd))

    def conjugate(self, z):
        a, b = z
        return self.add(a, b), self.neg(b)

    def multiplier(self, i, budget=None):
        """(1 - omega*sqrt(p))/(1 - conjugate(omega)*sqrt(p))."""
        p = self.primes[i]
        t = self.root(i)
        divisor = p * p + p + 1
        a = self.scale(self.sub(self.constant(p + 1), t),
                       Fraction(1 - p, divisor))
        b = self.scale(self.add(self.constant(p * (p - 1)),
                               self.scale(t, p + 2)), Fraction(1, divisor))
        if budget is not None:
            budget.pair()
        if self.q(a, b) != self.one:
            raise ArithmeticError("multiplier norm identity failed")
        return a, b


def multiply_letters(arithmetic, letters):
    """Enumerate and deduplicate every word exactly, preserving no label fiction."""
    words = {(arithmetic.one, arithmetic.zero)}
    for alphabet in letters:
        words = {arithmetic.eisenstein_mul(z, w) for z in words for w in alphabet}
    return words


def construct(family, m, budget=None):
    if (family, m) not in SCHEDULE:
        raise ValueError("family or level outside authorized finite schedule")
    arithmetic = Multiquadratic(PRIMES[:m])
    identity = (arithmetic.one, arithmetic.zero)
    units = [arithmetic.multiplier(i, budget) for i in range(m)]
    multipliers = multiply_letters(
        arithmetic, [(arithmetic.conjugate(u), identity, u) for u in units])
    if family == "F1":
        words = multipliers
    elif family == "F2":
        shells = set()
        for bits in product((0, 1), repeat=m):
            c = arithmetic.one
            for i, bit in enumerate(bits):
                if bit:
                    c = arithmetic.add(c, arithmetic.root(i))
            shells.add(c)
        words = {(arithmetic.mul(c, a), arithmetic.mul(c, b))
                 for c in shells for a, b in multipliers}
    else:
        alphabets = []
        for i in range(m):
            t = arithmetic.root(i)
            pi = arithmetic.one, t
            alphabets.append((identity, (t, arithmetic.zero), pi,
                              arithmetic.conjugate(pi)))
        words = multiply_letters(arithmetic, alphabets)
    carrier = {x for z in words for coordinate in z
               for x in (coordinate, arithmetic.neg(coordinate))}
    return arithmetic, carrier, words, multipliers


def integerize(values):
    """Clear one shared denominator; this injective scaling preserves Q counts."""
    values = tuple(values)
    denominator = 1
    for value in values:
        for coefficient in value:
            denominator = lcm(denominator, Fraction(coefficient).denominator)
    integers = [tuple(int(coefficient * denominator) for coefficient in value)
                for value in values]
    return denominator, integers


class BudgetExceeded(RuntimeError):
    pass


@dataclass
class Budget:
    pair_cap: int = PAIR_CAP
    action_cap: int = ACTION_CAP
    cpu_cap: float = CPU_CAP
    pairs: int = 0
    actions: int = 0
    started: float = field(default_factory=time.process_time)

    def check(self):
        if time.process_time() - self.started > self.cpu_cap:
            raise BudgetExceeded("CPU budget exhausted")

    def pair(self):
        if self.pairs >= self.pair_cap:
            raise BudgetExceeded("ordered pair-output evaluation budget exhausted")
        self.pairs += 1
        if self.pairs % 128 == 0:
            self.check()

    def action(self):
        if self.actions >= self.action_cap:
            raise BudgetExceeded("action-pair test budget exhausted")
        self.actions += 1
        if self.actions % 128 == 0:
            self.check()


def full_image(arithmetic, carrier, budget):
    """Every ordered pair is evaluated; histogram gives outputs by fiber size."""
    counts = Counter()
    squares = {a: arithmetic.mul(a, a) for a in carrier}
    for a in carrier:
        for b in carrier:
            budget.pair()
            output = arithmetic.add(arithmetic.add(squares[a], squares[b]),
                                    arithmetic.mul(a, b))
            counts[output] += 1
    if sum(counts.values()) != len(carrier) ** 2:
        raise ArithmeticError("all-pairs accounting failed")
    return counts


def return_tail(arithmetic, carrier, multipliers, budget):
    """Count exact Cartesian returns under all listed norm-one actions.

    The zero pair is separated: all multipliers send it to the same point.
    For each nonzero pair, distinct multipliers produce distinct points.
    """
    coordinates = [coordinate for z in sorted(multipliers) for coordinate in z]
    denominator, coefficients = integerize(coordinates)
    actions = [(coefficients[i], coefficients[i + 1])
               for i in range(0, len(coefficients), 2)]
    carrier_set = set(carrier)
    histogram = Counter()
    zero_pairs = 0
    for a in carrier:
        for b in carrier:
            if a == arithmetic.zero and b == arithmetic.zero:
                zero_pairs += 1
                continue
            count = 0
            for r, s in actions:
                budget.action()
                # Here u=r-omega*s, so T_u(a,b)=(ra-sb,sa+(r+s)b).
                first = arithmetic.sub(arithmetic.mul(r, a), arithmetic.mul(s, b))
                second = arithmetic.add(arithmetic.mul(s, a),
                                        arithmetic.mul(arithmetic.add(r, s), b))
                if (all(x % denominator == 0 for x in first)
                        and all(x % denominator == 0 for x in second)
                        and tuple(x // denominator for x in first) in carrier_set
                        and tuple(x // denominator for x in second) in carrier_set):
                    count += 1
            histogram[count] += 1
    if 0 in histogram:
        raise ArithmeticError("identity multiplier did not return every pair")
    if sum(histogram.values()) + zero_pairs != len(carrier) ** 2:
        raise ArithmeticError("return-tail all-pairs accounting failed")
    tail_bounds = []
    for threshold in sorted(histogram):
        exceptions = zero_pairs + sum(n for k, n in histogram.items() if k < threshold)
        bound = Fraction(len(carrier) ** 2, threshold) + exceptions
        tail_bounds.append({"M": threshold, "exceptional_pairs": exceptions,
                            "support_bound_numerator": bound.numerator,
                            "support_bound_denominator": bound.denominator})
    return {"tested_all_multipliers": True, "multipliers": len(actions),
            "multiplier_common_denominator": denominator,
            "multiplier_hash": digest({"primes": arithmetic.primes,
                                       "denominator": denominator, "actions": actions}),
            "nonzero_pairs_by_return_count": dict(sorted(histogram.items())),
            "zero_pairs_charged_as_exception": zero_pairs,
            "fiber_tail_bounds": tail_bounds}


def case(family, m, budget, include_tail=True):
    started = time.process_time()
    before_pairs, before_actions = budget.pairs, budget.actions
    arithmetic, rational_carrier, words, multipliers = construct(family, m, budget)
    budget.check()
    denominator, carrier = integerize(sorted(rational_carrier))
    carrier = sorted(set(carrier))
    counts = full_image(arithmetic, carrier, budget)
    word_pairs = []
    for a, b in sorted(words):
        word_pairs.append((tuple(int(x * denominator) for x in a),
                           tuple(int(x * denominator) for x in b)))
    # These are additional engineered-pair Q evaluations, charged to the cap.
    norms = set()
    for a, b in word_pairs:
        budget.pair()
        norms.add(arithmetic.q(a, b))
    if not norms <= set(counts):
        raise ArithmeticError("engineered norms absent from Cartesian image")
    input_payload = {"primes": arithmetic.primes, "denominator": denominator,
                     "carrier": carrier, "engineered_pairs": word_pairs}
    output_payload = {"primes": arithmetic.primes,
                      "denominator": denominator * denominator,
                      "output_fibers": sorted(counts.items())}
    result = {
        "family": family, "m": m, "primes": arithmetic.primes,
        "field_degree": arithmetic.dimension,
        "status": "EXPERIMENTAL; exhaustive exact finite same-set enumeration",
        "input_size": len(carrier), "full_image_size": len(counts),
        "word_labels_before_deduplication": {"F1": 3, "F2": 6, "F3": 4}[family] ** m,
        "engineered_pairs": len(words), "engineered_norms": len(norms),
        "unengineered_ordered_pairs": len(carrier) ** 2 - len(words),
        "ordered_pairs": len(carrier) ** 2,
        "input_common_denominator": denominator,
        "max_abs_scaled_coefficient": max(abs(x) for a in carrier for x in a),
        "max_abs_scaled_output_coefficient": max(abs(x) for a in counts for x in a),
        "output_fibers_by_multiplicity": dict(sorted(Counter(counts.values()).items())),
        "input_sha256": digest(input_payload), "output_sha256": digest(output_payload),
        "engineered_norms_sha256": digest(sorted(norms)),
    }
    if family in ("F1", "F2") and include_tail:
        result["return_tail"] = return_tail(arithmetic, carrier, multipliers, budget)
    else:
        result["return_tail"] = {"tested": False,
                                 "reason": "not in requested tail schedule"}
    result.update(pair_output_evaluations=budget.pairs - before_pairs,
                  action_pair_tests=budget.actions - before_actions,
                  cpu_seconds=time.process_time() - started)
    return result


def run(schedule=SCHEDULE, cpu_cap=CPU_CAP):
    if not 0 < cpu_cap <= CPU_CAP:
        raise ValueError("CPU cap must be positive and at most 240 seconds")
    if any(item not in SCHEDULE for item in schedule) or len(schedule) != len(set(schedule)):
        raise ValueError("schedule must be a subset without repetition")
    budget = Budget(cpu_cap=cpu_cap)
    wall_started = time.monotonic()
    result = {
        "experiment": "eisenstein-solvable-multiplier-carriers",
        "branch": "T03 separate multiplier diagnostics; not adaptive RC15/4",
        "polynomial": "x^2+xy+y^2",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version, "platform": platform.platform(),
        "command": [sys.executable, "-m", "experiments.eisenstein_solvable", *sys.argv[1:]],
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "exact independent multiquadratic coefficients; shared-denominator integer Q and action tests",
        "embedding": "all square roots positive; injective real field embedding",
        "families": {
            "F1": "Z=product u_i^{e_i}, e_i in {-1,0,1}",
            "F2": "Z=(1+sum b_i sqrt(p_i))*product u_i^{e_i}; b_i in {0,1}, e_i in {-1,0,1}",
            "F3": "Z=product {1,sqrt(p_i),pi_i,conjugate(pi_i)}",
            "common": "pi_i=1-omega sqrt(p_i); u_i=pi_i/conjugate(pi_i); A=signed union of both coefficient projections of Z",
        },
        "budget": {"pair_output_cap": PAIR_CAP, "action_pair_cap": ACTION_CAP,
                   "cpu_seconds_cap": cpu_cap},
        "schedule": schedule, "results": [], "errors": [],
        "limitations": ["Finite exact counts do not establish an asymptotic power saving.",
                        "Field degree and denominator/height growth have not been converted into a positive rate.",
                        "No random sampling, external data, or imported serialized state is used.",
                        "F3 tail actions are not tested; F1 and F2 use every listed multiplier."]}
    try:
        for family, m in schedule:
            result["results"].append(case(family, m, budget))
        budget.check()
    except BudgetExceeded as error:
        result["errors"].append(str(error))
    result.update(completed=len(result["results"]) == len(schedule) and not result["errors"],
                  pair_output_evaluations=budget.pairs, action_pair_tests=budget.actions,
                  cpu_seconds=time.process_time() - budget.started,
                  wall_seconds=time.monotonic() - wall_started)
    result["results_sha256"] = digest(result["results"])
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="new JSON output file; existing files are not overwritten")
    parser.add_argument("--cpu-seconds", type=float, default=CPU_CAP)
    args = parser.parse_args(argv)
    if args.output is not None and args.output.exists():
        parser.error("output already exists; choose a new run path")
    try:
        result = run(cpu_cap=args.cpu_seconds)
    except ValueError as error:
        parser.error(str(error))
    text = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is None:
        print(text, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x") as stream:
            stream.write(text)
        print(json.dumps({"output": str(args.output.resolve()), "completed": result["completed"],
                          "cases": len(result["results"]),
                          "pair_output_evaluations": result["pair_output_evaluations"],
                          "action_pair_tests": result["action_pair_tests"],
                          "cpu_seconds": result["cpu_seconds"], "errors": result["errors"]}))
    return 0 if result["completed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
