"""Offline exact checks of the proved 7^k paired lift, k=1,2 only.

Enumerates the cyclotomic angular core, not the much larger completed
Cartesian square. Full-carrier counts use proved shell decomposition.
No numerical equality, algebraic-number packages, or prime search.
"""
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time


class Budget:
    def __init__(self):
        self.counts = Counter()
        self.start = time.process_time()

    def charge(self, kind):
        self.counts[kind] += 1
        if sum(self.counts.values()) > 100000:
            raise RuntimeError('100000 research-query cap exceeded')
        if time.process_time() - self.start > 60:
            raise RuntimeError('60 CPU-second research cap exceeded')


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def exact_division(p, q):
    """Monic polynomial division over Z, requiring zero remainder."""
    p = trim(p)
    assert q[-1] == 1
    result = [0] * max(1, len(p)-len(q)+1)
    while len(p) >= len(q):
        shift, coefficient = len(p)-len(q), p[-1]
        result[shift] = coefficient
        for i, value in enumerate(q):
            p[shift+i] -= coefficient*value
        p = trim(p)
    assert not any(p)
    return trim(result)


def cyclotomic(m):
    cache = {}
    for d in range(1, m+1):
        if m % d:
            continue
        poly = [-1]+[0]*(d-1)+[1]
        for e, factor in cache.items():
            if d % e == 0:
                poly = exact_division(poly, factor)
        cache[d] = poly
    return cache[m]


class Field:
    def __init__(self, m):
        self.m = m
        self.modulus = cyclotomic(m)
        self.degree = len(self.modulus)-1
        self.zero = (0,)*self.degree
        self.one = (1,)+(0,)*(self.degree-1)
        self.powers = [self.reduce([0]*i+[1]) for i in range(m)]
        self.omega = self.powers[m//3]
        self.delta = self.add(self.one, self.scale(self.omega, 2))

    def reduce(self, p):
        p = list(p)
        for j in range(len(p)-1, self.degree-1, -1):
            c = p[j]
            for i in range(self.degree+1):
                p[j-self.degree+i] -= c*self.modulus[i]
        return tuple((p+[0]*self.degree)[:self.degree])

    def add(self, *args):
        return tuple(sum(v) for v in zip(*args))

    def scale(self, x, c):
        return tuple(c*a for a in x)

    def mul(self, x, y):
        p = [0]*(2*self.degree-1)
        for i, a in enumerate(x):
            for j, b in enumerate(y):
                p[i+j] += a*b
        return self.reduce(p)

    def conj(self, x):
        result = self.zero
        for i, c in enumerate(x):
            result = self.add(result, self.scale(self.powers[-i % self.m], c))
        return result

    def q(self, x, y):
        return self.add(self.mul(x, x), self.mul(x, y), self.mul(y, y))

    def decode3(self, z):
        """Return (3x,3y) for arbitrary z=x-omega*y."""
        y3 = self.mul(self.delta, self.add(z, self.scale(self.conj(z), -1)))
        return self.add(self.scale(z, 3), self.mul(self.omega, y3)), y3

    def matrix3(self, u):
        b3 = self.scale(self.mul(self.delta, self.add(u, self.scale(self.conj(u), -1))), -1)
        a3 = self.add(self.scale(u, 3), self.scale(self.mul(self.omega, b3), -1))
        return a3, b3


def modular_orbits(k, budget):
    n, m = 7**k, 6*7**(k-1)
    remaining = {(s, t) for s in range(n) for t in range(n) if s % 7 or t % 7}
    g = -2 % n
    ginv = pow(g, -1, n)
    orbits = []
    while remaining:
        base = min(remaining)
        orbit, p = [], base
        for _ in range(m):
            budget.charge('modular_orbit_transition')
            orbit.append(p)
            p = (g*p[0] % n, ginv*p[1] % n)
        assert p == base and len(set(orbit)) == m
        assert set(orbit) <= remaining
        remaining.difference_update(orbit)
        orbits.append(orbit)
    assert len(orbits) == 8*7**(k-1)
    return orbits


def scout(k, budget):
    n, m, t = 7**k, 6*7**(k-1), 8*7**(k-1)
    f = Field(m)
    orbits = modular_orbits(k, budget)
    # decode3(zeta^r) is the actual pair decoding 3*zeta^r.
    engineered = [f.decode3(u) for u in f.powers]
    xs, ys = {p[0] for p in engineered}, {p[1] for p in engineered}
    assert xs == ys and len(xs) == m//2 and f.zero in xs
    S = sorted(xs)
    assert all(f.conj(a) == a for a in S)
    S3 = {f.scale(a, 3): i for i, a in enumerate(S)}
    coeffs = [f.matrix3(u) for u in f.powers]
    values, rows, histogram = {}, [], Counter()
    for i, x in enumerate(S):
        for j, y in enumerate(S):
            z = f.add(x, f.scale(f.mul(f.omega, y), -1))
            budget.charge('angular_core_Q')
            q = f.q(x, y)
            budget.charge('angular_core_norm_oracle')
            assert q == f.mul(z, f.conj(z))
            values[i, j] = q
            targets, actions = set(), []
            for r, (u, (a3, b3)) in enumerate(zip(f.powers, coeffs)):
                budget.charge('angular_complex_action')
                target = f.decode3(f.mul(u, z))
                budget.charge('angular_matrix_oracle')
                matrix = (f.add(f.mul(a3, x), f.mul(b3, y)),
                          f.add(f.scale(f.mul(b3, x), -1),
                                f.mul(f.add(a3, f.scale(b3, -1)), y)))
                assert target == matrix
                if target[0] in S3 and target[1] in S3:
                    pair = (S3[target[0]], S3[target[1]])
                    targets.add(pair)
                    actions.append(r)
            assert len(targets) >= 1
            assert len(targets) == (1 if z == f.zero else len(actions))
            histogram[len(targets)] += 1
            rows.append({'source': [i, j], 'returns': sorted(targets), 'actions': actions})
    for row in rows:
        for target in row['returns']:
            assert values[tuple(target)] == values[tuple(row['source'])]
    assert histogram[1] == 1
    q = len(S)-1
    N = 1+t*q
    mixed = t*(t-1)*q*q
    full = Counter({r: t*c for r, c in histogram.items()})
    full[1] = 1
    full[2] += mixed
    assert sum(full.values()) == N*N
    threshold = 1
    while threshold**4 < N:
        threshold += 1
    bad = sum(c for r, c in full.items() if r < threshold)
    V = len(set(values.values()))
    result = {
        'k': k, 'modular_input_size': n, 'primitive_modular_pairs': t*m,
        'orbit_count': t, 'angular_scalar_size': len(S), 'lifted_real_input_size': N,
        'surviving_actions': m, 'median_genuine_returns': 2, 'identity_only_pairs': 1,
        'epsilon': '1/4', 'threshold_ceiling': threshold, 'bad_pairs': bad,
        'mixed_shell_pairs': mixed, 'projection_fibers_on_encoded_pairs': 1,
        'engineered_pairs': t*m, 'symmetric_difference': 0,
        'full_Q_image': 1+t*(V-1)+mixed//4,
        'angular_Q_image': V, 'angular_return_histogram': dict(sorted(histogram.items())),
        'full_return_histogram': dict(sorted(full.items())),
        'geometric_mean_display': math.exp(sum(c*math.log(r) for r, c in full.items())/(N*N)),
        'maximum_genuine_returns': max(full),
        'counts_method': 'exhaustive exact angular core; full completion derived by ML-4 equations (19)-(20)',
        'field_modulus': f.modulus, 'radical_degree_D': m*(2*t+1)+1}
    raw = {'k': k, 'S': S, 'core_pairs': rows,
           'core_values': [{'source': list(p), 'value': v} for p, v in values.items()],
           'primitive_modular_orbits': orbits}
    return result, raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--raw', type=Path, required=True)
    args = parser.parse_args()
    assert args.output.resolve() != args.raw.resolve()
    for p in (args.output, args.raw):
        if p.exists():
            raise FileExistsError(p)
        p.parent.mkdir(parents=True, exist_ok=True)
    budget, wall = Budget(), time.perf_counter()
    records, raw, error = [], [], None
    try:
        for k in (1, 2):
            result, detail = scout(k, budget)
            records.append(result)
            raw.append(detail)
    except Exception as exc:
        error = repr(exc)
        raise
    finally:
        path = Path(__file__)
        output = {'cases': records, 'error': error, 'reproducibility': {
            'command': sys.argv, 'python': platform.python_version(), 'fixed_k': [1, 2],
            'code_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'charged_evaluations': sum(budget.counts.values()), 'categories': dict(budget.counts),
            'cpu_seconds': time.process_time()-budget.start, 'wall_seconds': time.perf_counter()-wall,
            'query_cap': 100000, 'cpu_cap_seconds': 60, 'network_used': False,
            'equality': 'integer coefficients modulo Phi_m; theta powers independent through 2t',
            'rounding': 'geometric mean display only', 'seed': None}}
        args.output.write_text(json.dumps(output, indent=2)+'\n')
        args.raw.write_text(json.dumps(raw, separators=(',', ':'))+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
