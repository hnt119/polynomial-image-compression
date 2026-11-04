"""Frozen offline exact scout of two cyclotomic trace carriers.

Elements are integral cyclic polynomials in xi with Eisenstein integer
coefficients. Equality reduces modulo Phi_p; p=11,17 are fixed in advance.
No floating-point arithmetic decides equality, membership, or a threshold.
The two action oracles use complex multiplication and the real coefficient
matrix separately. Geometric means alone are rounded for presentation.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

from .unit_exponent import Budget
from .rectangular_returns import fourth_root_ceiling, stats

PRIMES = (11, 17)
ZERO = (0, 0)
ONE = (1, 0)
OMEGA = (0, 1)
DELTA = (1, 2)
ROOTS6 = ((1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1))


def cmul(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c-b*d


def cconj(z):
    a, b = z
    return a-b, -b


def add(*polys):
    out = {}
    for poly in polys:
        for i, (a, b) in poly.items():
            c, d = out.get(i, ZERO)
            out[i] = (a+c, b+d)
    return {i: v for i, v in out.items() if v != ZERO}


def scale(poly, c):
    return {i: v for i, a in poly.items() if (v := cmul(c, a)) != ZERO}


def multiply(z, w, p):
    out = {}
    for i, a in z.items():
        for j, b in w.items():
            k = (i+j) % p
            c, d = out.get(k, ZERO)
            e, f = cmul(a, b)
            out[k] = (c+e, d+f)
    return {i: v for i, v in out.items() if v != ZERO}


def conjugate(z, p):
    return {(-i) % p: cconj(a) for i, a in z.items()}


def key(z, p):
    """Canonical coefficients after xi^(p-1) = -sum_(i<p-1) xi^i."""
    a, b = z.get(p-1, ZERO)
    return tuple((z.get(i, ZERO)[0]-a, z.get(i, ZERO)[1]-b) for i in range(p-1))


def trace(u, p):
    return add(u, conjugate(u, p))


def q_value(x, y, p):
    return add(multiply(x, x, p), multiply(x, y, p), multiply(y, y, p))


def complex_pair(x, y):
    return add(x, scale(y, (0, -1)))


def target_times_three(u, z, p):
    """Act on z=x-omega*y, then recover 3x',3y' without division."""
    target_z = multiply(u, z, p)
    y3 = scale(add(target_z, scale(conjugate(target_z, p), (-1, 0))), DELTA)
    x3 = add(scale(target_z, (3, 0)), scale(y3, OMEGA))
    return key(x3, p), key(y3, p)


def matrix_coefficients_times_three(u, p):
    # u=a+b*omega with a,b real. b=(u-conj(u))/(1+2*omega).
    b3 = scale(add(u, scale(conjugate(u, p), (-1, 0))), (-1, -2))
    a3 = add(scale(u, (3, 0)), scale(b3, (0, -1)))
    return a3, b3


def matrix_target_times_three(coefficients, x, y, p):
    a3, b3 = coefficients
    x3 = add(multiply(a3, x, p), multiply(b3, y, p))
    y3 = add(scale(multiply(b3, x, p), (-1, 0)),
             multiply(add(a3, scale(b3, (-1, 0))), y, p))
    return key(x3, p), key(y3, p)


def make_case(p, budget):
    actions = [({r: c}, (j, r)) for j, c in enumerate(ROOTS6) for r in range(p)]
    assert len({key(u, p) for u, _ in actions}) == 6*p
    one = key({0: ONE}, p)
    for u, _ in actions:
        budget.charge('constructed_action_norm_check')
        assert key(multiply(u, conjugate(u, p), p), p) == one
    scalar = {}
    for u, label in actions:
        x = trace(u, p)
        scalar.setdefault(key(x, p), (x, label))
    A = sorted(scalar)
    assert len(A) == 3*p+1 and key({}, p) not in scalar
    exceptional = set()
    for u, _ in actions:
        budget.charge('exceptional_orbit_point')
        exceptional.add(key(scale(u, DELTA), p))
    assert len(exceptional) == 6*p
    return A, scalar, actions, exceptional


def measure(p, budget):
    A, scalar, actions, exceptional = make_case(p, budget)
    n = len(A)
    needed = 2*n*n*(1+len(actions))
    if budget.total+needed > budget.cap:
        raise RuntimeError('fixed case exceeds remaining shared query budget')
    triple_index = {key(scale(scalar[a][0], (3, 0)), p): i for i, a in enumerate(A)}
    matrix_coeffs = [matrix_coefficients_times_three(u, p) for u, _ in actions]
    values = {}
    complexes = {}
    for i, a in enumerate(A):
        x = scalar[a][0]
        for j, b in enumerate(A):
            y = scalar[b][0]
            z = complex_pair(x, y)
            complexes[i, j] = z
            budget.charge('full_square_Q_query')
            value = key(q_value(x, y, p), p)
            budget.charge('independent_full_square_Q_query')
            assert value == key(multiply(z, conjugate(z, p), p), p)
            values[i, j] = value
    outputs = sorted(set(values.values()))
    out_index = {value: i for i, value in enumerate(outputs)}
    rows, counts, fixing_counts = [], [], []
    domains = [0]*len(actions)
    exceptional_seen = 0
    for i, a in enumerate(A):
        x = scalar[a][0]
        for j, b in enumerate(A):
            y = scalar[b][0]
            z = complexes[i, j]
            rich = key(z, p) in exceptional
            exceptional_seen += rich
            returned, legal = set(), []
            fixing = 0
            for k, ((u, label), coeffs) in enumerate(zip(actions, matrix_coeffs)):
                budget.charge('complex_scalar_action_query')
                target = target_times_three(u, z, p)
                budget.charge('independent_matrix_action_query')
                assert target == matrix_target_times_three(coeffs, x, y, p)
                if target[0] in triple_index and target[1] in triple_index:
                    pair = triple_index[target[0]], triple_index[target[1]]
                    assert values[pair] == values[i, j]
                    returned.add(pair)
                    legal.append(k)
                    domains[k] += 1
                    fixing += pair == (i, j)
                    assert rich or (label[1] == 0 and label[0] in (0, 3))
            assert len(returned) == len(legal) == (6*p if rich else 2)
            assert fixing == 1
            counts.append(len(returned))
            fixing_counts.append(fixing)
            rows.append({'pair': [i, j], 'exceptional_orbit': rich,
                         'returning_actions': legal, 'returned_pairs': sorted(returned),
                         'output_index': out_index[values[i, j]]})
    assert exceptional_seen == 6*p
    for size, (_, (phase, shift)) in zip(domains, actions):
        assert size == (n*n if shift == 0 and phase in (0, 3) else 6*p)
    threshold = fourth_root_ceiling(n)
    summary = {'p': p, 'n': n, 'symmetric_difference': 0, 'action_size': len(actions),
               'identity_only_pairs': counts.count(1), 'R_pair': stats(counts),
               'epsilon': '1/4', 'integer_threshold': threshold,
               'bad_pairs': sum(r < threshold for r in counts),
               'exceptional_orbit_pairs': exceptional_seen,
               'full_Q_image': len(outputs), 'domain_sizes': domains,
               'stabilizer_histogram': dict(Counter(fixing_counts)),
               'image_fiber_histogram': dict(sorted(Counter(Counter(values.values()).values()).items()))}
    raw = {'p': p, 'A': [{'coefficients': a, 'trace_label': scalar[a][1]} for a in A],
           'actions': [label for _, label in actions], 'outputs': outputs, 'pairs': rows}
    return summary, raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--pairs-output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == args.pairs_output.resolve():
        raise ValueError('summary and raw paths must differ')
    for path in (args.output, args.pairs_output):
        if path.exists():
            raise FileExistsError(path)
        path.parent.mkdir(parents=True, exist_ok=True)
    budget = Budget()
    wall = time.perf_counter()
    results, raw_cases = [], []
    error = None
    try:
        for p in PRIMES:
            summary, raw = measure(p, budget)
            results.append(summary)
            raw_cases.append(raw)
            budget.check_time()
    except Exception as exc:
        error = repr(exc)
        raise
    finally:
        files = [Path(__file__), Path(__file__).with_name('unit_exponent.py'),
                 Path(__file__).with_name('rectangular_returns.py')]
        record = {'cases': results, 'error': error, 'reproducibility': {
            'command_argv': sys.argv, 'python': platform.python_version(),
            'fixed_primes': PRIMES, 'network_attempted': False, 'seed': None,
            'source_hashes': {str(p.relative_to(Path.cwd())): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
            'charged_evaluations': budget.total, 'categories': dict(budget.counts),
            'cpu_seconds': budget.cpu_seconds(), 'wall_seconds': time.perf_counter()-wall,
            'evaluation_cap': budget.cap, 'cpu_cap_seconds': budget.cpu_cap,
            'equality_arithmetic': 'integer coefficients in Z[omega,xi], reduced modulo Phi_p',
            'geometric_mean_display': 'floating point only'}}
        with args.output.open('x') as stream:
            json.dump(record, stream, indent=2, sort_keys=True);stream.write('\n')
        with args.pairs_output.open('x') as stream:
            json.dump(raw_cases, stream, separators=(',', ':'));stream.write('\n')
    print(json.dumps({'cases': [{k: r[k] for k in ('p','n','symmetric_difference','action_size','identity_only_pairs','R_pair','bad_pairs','full_Q_image')} for r in results],
                      'reproducibility': record['reproducibility']}, indent=2))


if __name__ == '__main__':
    main()
