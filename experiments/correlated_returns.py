"""One frozen offline scout: CRT cube-root carriers, depths 1 through 4.

No independent additive tensor is used. Each action conjugates one factor
of the whole scalar Eisenstein integer. Check every pair/action in two
coordinate systems and by the independent factor-divisibility criterion.
All arithmetic equality and thresholds are exact; only geometric-mean
presentation uses floating point. Historical scout entry points are not run.
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

from .unit_exponent import (Budget, action, conjugate, mul, norm,
                            oracle_action, oracle_q, q)
from .rectangular_returns import fourth_root_ceiling, stats

BLOCKS = ((7, (2, -1)), (13, (3, -1)), (19, (3, -2)), (31, (5, -1)))
DEPTHS = (1, 2, 3, 4)


def crt_carrier(blocks, budget=None):
    """Canonical centered representatives; three roots per selected prime."""
    modulus = 1
    residues = [0]
    for prime, _ in blocks:
        roots = []
        for a in range(1, prime):
            if budget is not None:
                budget.charge('local_cube_root_query')
            if pow(a, 3, prime) == 1:
                roots.append(a)
        assert len(roots) == 3
        inv = pow(modulus, -1, prime)
        residues = [r + modulus*((s-r)*inv % prime)
                    for r in residues for s in roots]
        modulus *= prime
    carrier = sorted(F(r if 2*r < modulus else r-modulus) for r in residues)
    assert len(set(carrier)) == 3**len(blocks) and F(0) not in carrier
    return carrier, modulus


def action_words(blocks, budget):
    """Return distinct u=bar(beta)/beta, retaining each whole factor beta."""
    words = []
    for exponents in product((-1, 0, 1), repeat=len(blocks)):
        beta = (F(1), F(0))
        for exponent, (prime, alpha) in zip(exponents, blocks):
            if exponent:
                factor = tuple(map(F, alpha))
                beta = mul(beta, factor if exponent == 1 else conjugate(factor))
        D = norm(beta)
        u = tuple(v/D for v in mul(conjugate(beta), conjugate(beta)))
        budget.charge('constructed_action_norm_check')
        assert norm(u) == 1
        words.append((exponents, beta, u))
    assert len({u for _, _, u in words}) == 3**len(blocks)
    return words


def factor_divides(beta, x, y):
    """Integer divisibility beta | (x-omega*y), separately from action()."""
    a, b = beta
    D = norm(beta)
    # (x-omega*y)*bar(beta): coefficients in the integral basis 1,omega.
    c0 = x*(a-b)-y*b
    c1 = -x*b-y*a
    return c0 % D == 0 and c1 % D == 0


def diagonal_product(blocks, x, y):
    w = 1
    count = 0
    for p, _ in blocks:
        if (x-y) % p == 0:
            w *= p
            count += 1
    return w, count


def measure(d, budget):
    blocks = BLOCKS[:d]
    A, P = crt_carrier(blocks, budget)
    words = action_words(blocks, budget)
    aset, n = set(A), len(A)
    remaining = 2*n*n+3*n*n*len(words)
    if budget.total+remaining > budget.cap:
        raise RuntimeError('fixed case exceeds remaining shared query budget')
    index = {a: i for i, a in enumerate(A)}
    values = {}
    for x, y in product(A, repeat=2):
        budget.charge('full_square_Q_query')
        value = q(x, y)
        budget.charge('independent_full_square_Q_query')
        assert value == oracle_q(x, y)
        values[x, y] = value
    outputs = sorted(set(values.values()))
    output_index = {v: i for i, v in enumerate(outputs)}
    domain_sizes = [0]*len(words)
    integral_domains = [0]*len(words)
    returns, integrals, rows = [], [], []
    witness_count = 0
    threshold = fourth_root_ceiling(n)
    for x, y in product(A, repeat=2):
        w, diagonal_count = diagonal_product(blocks, x, y)
        witness = 3*w**3 > 4*P
        witness_count += witness
        returned, legal = set(), []
        integral_count = fixing = 0
        for j, (exponents, beta, u) in enumerate(words):
            budget.charge('scalar_action_query')
            target = action(u, x, y)
            budget.charge('independent_scalar_action_query')
            assert target == oracle_action(u, x, y)
            integral = all(t.denominator == 1 for t in target)
            budget.charge('factor_divisibility_query')
            assert integral == factor_divides(beta, x, y)
            integral_count += integral
            integral_domains[j] += integral
            if target[0] in aset and target[1] in aset:
                assert values[target] == values[x, y]
                legal.append(j)
                returned.add((index[target[0]], index[target[1]]))
                domain_sizes[j] += 1
                fixing += target == (x, y)
                if witness:
                    assert all(e == 0 for e in exponents)
        assert integral_count == 2**(d-diagonal_count)
        assert len(legal) == len(returned) and fixing == 1
        if witness:
            assert len(returned) == 1
        returns.append(len(returned))
        integrals.append(integral_count)
        rows.append({'pair': [index[x], index[y]],
                     'output_index': output_index[values[x, y]],
                     'returning_actions': legal, 'returned_pairs': sorted(returned),
                     'integral_action_count': integral_count,
                     'identity_obstruction': witness, 'diagonal_product': w})
    assert 48*witness_count >= n*n
    summary = {'d': d, 'primes': [p for p, _ in blocks], 'modulus': P,
               'n': n, 'symmetric_difference': 0, 'action_size': len(words),
               'R_pair': stats(returns), 'R_integral': stats(integrals),
               'epsilon': '1/4', 'integer_threshold': threshold,
               'bad_pairs': sum(r < threshold for r in returns),
               'identity_obstruction_pairs': witness_count,
               'full_Q_image': len(outputs),
               'image_fiber_histogram': dict(sorted(Counter(Counter(values.values()).values()).items())),
               'return_domain_sizes': domain_sizes,
               'integrality_domain_sizes': integral_domains,
               'stabilizer_histogram': {1: n*n},
               'action_vs_pair_counts': 'equal at every source; zero absent'}
    raw = {'d': d, 'A': list(map(str, A)),
           'actions': [{'exponents': e, 'beta': list(map(str, b)), 'u': list(map(str, u))}
                       for e, b, u in words],
           'outputs': list(map(str, outputs)), 'pairs': rows}
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
    wall_start = time.perf_counter()
    results, raw_cases = [], []
    error = None
    try:
        for d in DEPTHS:
            row, raw = measure(d, budget)
            results.append(row)
            raw_cases.append(raw)
            budget.check_time()
    except Exception as exc:
        error = repr(exc)
        raise
    finally:
        sources = [Path(__file__), Path(__file__).with_name('unit_exponent.py'),
                   Path(__file__).with_name('rectangular_returns.py')]
        output = {'cases': results, 'error': error, 'reproducibility': {
            'command_argv': sys.argv, 'python': platform.python_version(),
            'depths': DEPTHS, 'fixed_blocks': BLOCKS,
            'network_attempted': False, 'seed': None,
            'source_hashes': {str(p.relative_to(Path.cwd())): hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in sources},
            'charged_evaluations': budget.total, 'categories': dict(budget.counts),
            'cpu_seconds': budget.cpu_seconds(), 'wall_seconds': time.perf_counter()-wall_start,
            'evaluation_cap': budget.cap, 'cpu_cap_seconds': budget.cpu_cap,
            'equality_arithmetic': 'exact Fraction',
            'geometric_mean_display': 'floating point only'}}
        with args.output.open('x') as stream:
            json.dump(output, stream, indent=2, sort_keys=True);stream.write('\n')
        with args.pairs_output.open('x') as stream:
            json.dump(raw_cases, stream, separators=(',', ':'));stream.write('\n')
    print(json.dumps({'cases': [{k: r[k] for k in ('d','n','symmetric_difference','action_size','R_pair','bad_pairs','identity_obstruction_pairs','full_Q_image')} for r in results],
                      'reproducibility': output['reproducibility']}, indent=2))


if __name__ == '__main__':
    main()
