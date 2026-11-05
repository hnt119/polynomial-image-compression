"""Exact, bounded scouting of rational Cartesian returns (2026-09-16).

Equality and membership use integers/Fraction, never floating point. Floating
medians/geometric means are descriptive only. This is not an asymptotic test.
Run: python3 -m experiments.cartesian_returns --output NEW_PATH
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from math import exp, gcd, isfinite, lcm, log
from pathlib import Path
import platform
import sys
import time


EVALUATION_CAP = 2_000_000
CPU_CAP = 600.0
SCHEDULE = (
    *(('strata', h, depth) for h in (1, 2, 4) for depth in (2, 4, 8)),
    ('strata', 8, 4), ('strata', 16, 4),
    *(('orbit_box', 1, depth) for depth in (1, 2, 4, 8)),
    *(('repair', 1, depth) for depth in (0, 1, 2)),
)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


class BudgetExceeded(RuntimeError):
    pass


class Budget:
    def __init__(self, cap=EVALUATION_CAP, cpu_cap=CPU_CAP):
        if not isinstance(cap, int) or not 1 <= cap <= EVALUATION_CAP:
            raise ValueError('invalid evaluation budget')
        if not isfinite(cpu_cap) or not 0 < cpu_cap <= CPU_CAP:
            raise ValueError('invalid CPU budget')
        self.cap, self.cpu_cap = cap, cpu_cap
        self.counts = Counter()
        self.total = 0
        self.start = time.process_time()

    def charge(self, kind):
        if self.total >= self.cap:
            raise BudgetExceeded('evaluation budget exhausted')
        self.total += 1
        self.counts[kind] += 1
        if self.total % 256 == 0:
            self.check()

    def check(self):
        if time.process_time() - self.start > self.cpu_cap:
            raise BudgetExceeded('sampled CPU guard exhausted')


# Matrix tuple is (a,b,c,d,q): action ((ax+by)/q,(cx+dy)/q).
IDENTITY = (1, 0, 0, 1, 1)
FORWARD = (8, 5, -5, 3, 7)
BACKWARD = (3, -5, 5, 8, 7)


def compose(left, right):
    a, b, c, d, q = left
    e, f, g, h, r = right
    values = (a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h, q*r)
    common = 0
    for value in values:
        common = gcd(common, value)
    return tuple(value // common for value in values)


def powers(radius):
    if not isinstance(radius, int) or radius < 0:
        raise ValueError('nonnegative integer power radius required')
    result = {0: IDENTITY}
    positive = negative = IDENTITY
    for j in range(1, radius + 1):
        positive = compose(FORWARD, positive)
        negative = compose(BACKWARD, negative)
        result[j], result[-j] = positive, negative
    return sorted(result.items())


def apply_rational(matrix, x, y):
    a, b, c, d, q = matrix
    return (Fraction(a*x+b*y, q), Fraction(c*x+d*y, q))


def q_value(x, y):
    return x*x+x*y+y*y


def floor_log7(value):
    if value < 1:
        raise ValueError('positive integer required')
    exponent = 0
    while value >= 7:
        value //= 7
        exponent += 1
    return exponent


def construct(family, h, depth, budget):
    metadata = {}
    engineered = set()
    if family == 'strata':
        carrier = {Fraction(b, 7**k) for k in range(depth+1)
                   for b in range(-h, h+1) if b and b % 7}
        radius = max(depth, floor_log7(3*h*h))
        metadata['all_nonzero_cyclic_returns_covered'] = True
        metadata['return_upper_bound_HR2'] = 1 + floor_log7(3*h*h)
        metadata['expected_size'] = 2*(h-h//7)*(depth+1)
        assert len(carrier) == metadata['expected_size']
    elif family == 'orbit_box':
        seed = range(-h, h+1)
        for _, matrix in powers(depth):
            for x in seed:
                for y in seed:
                    budget.charge('construction_action')
                    engineered.add(apply_rational(matrix, x, y))
        carrier = {v for pair in engineered for v in pair}
        radius = 2*depth + floor_log7(12*h*h)
        metadata['all_nonzero_cyclic_returns_covered'] = True
        metadata['engineered_pair_count'] = len(engineered)
    elif family == 'repair':
        carrier = {Fraction(b) for b in range(-h, h+1)}
        sizes = [len(carrier)]
        for _ in range(depth):
            old = sorted(carrier)
            fresh = set(carrier)
            for matrix in (FORWARD, BACKWARD):
                for x in old:
                    for y in old:
                        budget.charge('construction_action')
                        fresh.update(apply_rational(matrix, x, y))
            carrier = fresh
            sizes.append(len(carrier))
        radius = floor_log7(3*h*h*13**(2*depth))
        metadata['all_nonzero_cyclic_returns_covered'] = True
        metadata['stage_sizes'] = sizes
        metadata['previous_square_count'] = sizes[-2]**2 if depth else 0
    else:
        raise ValueError('unsupported family')
    return sorted(carrier), powers(radius), engineered, metadata


def histogram(counter):
    return {str(key): counter[key] for key in sorted(counter)}


def distribution_stats(counter):
    total = sum(counter.values())
    if not total:
        return {'population': 0}
    def kth(rank):
        for value in sorted(counter):
            rank -= counter[value]
            if rank < 0:
                return value
        raise AssertionError('rank outside histogram')
    median = Fraction(kth((total-1)//2) + kth(total//2), 2)
    return {'population': total, 'histogram': histogram(counter),
            'identity_only_count': counter[1],
            'identity_only_fraction_exact': [counter[1], total],
            'median_exact': [median.numerator, median.denominator],
            'geometric_mean_float': exp(sum(count*log(value)
                                          for value, count in counter.items())/total),
            'minimum': min(counter), 'maximum': max(counter),
            'sum': sum(value*count for value, count in counter.items())}


def valuation7(value):
    if not value:
        return 'zero'
    num, den = abs(value.numerator), value.denominator
    answer = 0
    while num % 7 == 0:
        num //= 7
        answer += 1
    while den % 7 == 0:
        den //= 7
        answer -= 1
    return str(answer)


def run_case(spec, budget):
    family, h, depth = spec
    before = Counter(budget.counts)
    started = time.process_time()
    scalar, group, engineered, metadata = construct(family, h, depth, budget)
    denominator = lcm(*(x.denominator for x in scalar))
    carrier = [int(x*denominator) for x in scalar]
    membership = set(carrier)
    n = len(carrier)
    # No half-finished case: stop before the expensive exhaustive part.
    estimate = n*n*(len(group)+1) + len(group)
    if budget.total + estimate > budget.cap:
        raise BudgetExceeded(f'preflight refused {spec}: {estimate} evaluations needed')
    for _, matrix in group:
        a, b, c, d, q = matrix
        budget.charge('multiplier_norm')
        if a*d-b*c != q*q or (a*a+a*c+c*c, b*b+b*d+d*d,
                             2*a*b+a*d+b*c+2*c*d) != (q*q,q*q,q*q):
            raise ArithmeticError('matrix does not preserve Q')
    images = Counter()
    raw, effective, nonzero, stabilizers = Counter(), Counter(), Counter(), Counter()
    same_value_check = {}
    transitions = Counter()
    state = {x: valuation7(Fraction(x, denominator)) for x in carrier}
    pair_returns = []
    for x in carrier:
        for y in carrier:
            budget.charge('polynomial')
            value = q_value(x, y)
            images[value] += 1
            returned = set()
            raw_count = fixed = 0
            for exponent, matrix in group:
                budget.charge('return_action')
                a, b, c, d, q = matrix
                xx, yy = a*x+b*y, c*x+d*y
                if xx % q or yy % q:
                    continue
                xx, yy = xx//q, yy//q
                if xx not in membership or yy not in membership:
                    continue
                raw_count += 1
                returned.add((xx, yy))
                fixed += (xx == x and yy == y)
                transitions[(state[x], state[y], state[xx], state[yy])] += 1
            raw[raw_count] += 1
            effective[len(returned)] += 1
            stabilizers[fixed] += 1
            if x or y:
                nonzero[raw_count] += 1
                if len(returned) != raw_count or fixed != 1:
                    raise ArithmeticError('nonzero freeness failed')
            else:
                if len(returned) != 1 or fixed != len(group):
                    raise ArithmeticError('zero stabilizer failed')
            pair_returns.append([x, y, raw_count, len(returned)])
            same_value_check[value] = max(same_value_check.get(value, 0), len(returned))
    if any(same_value_check[value] > count for value, count in images.items()):
        raise ArithmeticError('returns exceed full polynomial fiber')
    tail = []
    # The only structural exception declared is zero. Threshold exceptions
    # include zero and every nonzero pair below threshold, counted exactly.
    for threshold in sorted({1, 2, 3, 4, 8, 16, 32, max(nonzero, default=1)}):
        exceptional = int(0 in membership) + sum(count for ret, count in nonzero.items()
                                                if ret < threshold)
        bound = Fraction(n*n, threshold) + exceptional
        if len(images) > bound:
            raise ArithmeticError('return-to-support bound failed')
        tail.append({'threshold': threshold, 'exceptional_pair_count': exceptional,
                     'minimum_outside_exception': min((r for r in nonzero if r >= threshold),
                                                      default=None),
                     'support_bound_exact': [bound.numerator, bound.denominator]})
    if family == 'strata' and max(nonzero) > metadata['return_upper_bound_HR2']:
        raise ArithmeticError('HR-2 finite regression failed')
    encoded = [[x.numerator, x.denominator] for x in scalar]
    budget.check()
    return {'family': family, 'H': h, 'depth': depth, 'input_size': n,
            'ordered_pairs': n*n, 'full_image_size': len(images),
            'action_count': len(group), 'action_exponents': [j for j, _ in group],
            'common_denominator': denominator, 'cleared_height': max(map(abs, carrier)),
            'carrier': encoded, 'carrier_sha256': digest(encoded),
            'action_matrices_sha256': digest(group),
            'raw_return_distribution_all_pairs': distribution_stats(raw),
            'distinct_returned_pair_distribution': distribution_stats(effective),
            'return_distribution_nonzero': distribution_stats(nonzero),
            'stabilizer_distribution_all_pairs': histogram(stabilizers),
            'image_multiplicity_distribution': histogram(Counter(images.values())),
            'output_fibers_sha256': digest(sorted(images.items())),
            'pair_returns_sha256': digest(pair_returns),
            'zero_exception_count': int(0 in membership),
            'zero_raw_returns_scope': 'finite enumerated action family only',
            'minimum_returns_outside_zero': min(nonzero), 'return_tail': tail,
            'state_transition_counts': [[*key, count] for key, count in sorted(transitions.items())],
            'engineered_density_exact': [len(engineered), n*n] if engineered else None,
            'metadata': metadata,
            'evaluations': dict(budget.counts-before),
            'cpu_seconds': time.process_time()-started}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('output already exists; original results are immutable')
    budget = Budget()
    result = {'status': 'EXPERIMENTAL', 'date_utc': datetime.now(timezone.utc).isoformat(),
              'python': platform.python_version(), 'command': sys.argv,
              'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'schedule': SCHEDULE, 'evaluation_cap': EVALUATION_CAP, 'cpu_cap': CPU_CAP,
              'cpu_guard': 'sampled every 256 evaluations and at case/final completion',
              'arithmetic': 'exact integers/Fraction; statistics marked float are descriptive',
              'seed': None, 'cases': [], 'errors': []}
    try:
        for spec in SCHEDULE:
            result['cases'].append(run_case(spec, budget))
        budget.check()
    except (BudgetExceeded, ArithmeticError, ValueError) as error:
        result['errors'].append(f'{type(error).__name__}: {error}')
    result['evaluations'] = dict(budget.counts)
    result['total_evaluations'] = budget.total
    result['cpu_seconds'] = time.process_time()-budget.start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive open prevents accidental replacement on a race.
    with args.output.open('x') as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write('\n')
    print(json.dumps({key: result[key] for key in ('total_evaluations', 'cpu_seconds', 'errors')}))
    print(f"completed {len(result['cases'])}/{len(SCHEDULE)} finite cases")
    return bool(result['errors'])


if __name__ == '__main__':
    raise SystemExit(main())
