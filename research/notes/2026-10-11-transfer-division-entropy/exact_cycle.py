"""Bounded, deterministic exact checks; Python standard library only.

Two specializations: the CP seed conic, and c=6 real elliptic 3-division.
No old experiment is imported or executed. Each phase has a 120s alarm.
All equality tests use rational quotient arithmetic, never floating point.
"""
from fractions import Fraction as F
from collections import Counter, defaultdict
from pathlib import Path
import argparse
import hashlib
import json
import platform
import signal
import time


def trim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p


def padd(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def pscale(p, c):
    return trim([x*c for x in p])


def pmul(p, q):
    out = [0]*(len(p)+len(q)-1) if p and q else []
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return trim(out)


def pdiv(p, q):
    p, q = trim(p), trim(q)
    if not q:
        raise ZeroDivisionError
    out = [0]*max(0, len(p)-len(q)+1)
    while len(p) >= len(q):
        i, c = len(p)-len(q), p[-1]/q[-1]
        out[i] = c
        p = padd(p, [0]*i + pscale(q, -c))
    return trim(out), p


def xgcd(p, q):
    s0, s1, t0, t1 = [1], [], [], [1]
    while q:
        a, r = pdiv(p, q)
        p, q = q, r
        s0, s1 = s1, padd(s0, pscale(pmul(a, s1), -1))
        t0, t1 = t1, padd(t0, pscale(pmul(a, t1), -1))
    c = 1/p[-1]
    return pscale(p, c), pscale(s0, c), pscale(t0, c)


class K:
    """An element in Q[T]/f. Constructor fixes the monic modulus."""
    def __init__(self, values, modulus):
        self.mod = tuple(map(F, modulus))
        values = list(values) if isinstance(values, (list, tuple)) else [values]
        rem = pdiv(list(map(F, values)), self.mod)[1]
        self.v = tuple(rem + [F(0)]*(len(self.mod)-1-len(rem)))

    def coerce(self, other):
        if isinstance(other, K):
            assert self.mod == other.mod
            return other
        return K(other, self.mod)

    def __add__(self, other):
        other = self.coerce(other)
        return K(padd(self.v, other.v), self.mod)

    __radd__ = __add__

    def __neg__(self):
        return K([-x for x in self.v], self.mod)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        other = self.coerce(other)
        return K(pmul(self.v, other.v), self.mod)

    __rmul__ = __mul__

    def inverse(self):
        g, s, _ = xgcd(list(self.v), list(self.mod))
        assert g == [F(1)]
        return K(s, self.mod)

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) * self.inverse()

    def __pow__(self, exponent):
        assert exponent >= 0
        ans, base = self.coerce(1), self
        while exponent:
            if exponent & 1:
                ans *= base
            base *= base
            exponent //= 2
        return ans

    def __bool__(self):
        return any(self.v)

    def __eq__(self, other):
        other = self.coerce(other)
        return self.v == other.v

    def __hash__(self):
        return hash((self.mod, self.v))

    def enc(self):
        return [str(v) for v in self.v]


class L:
    """K[Y]/(Y^2-radicand), with K quartic in this one scout."""
    def __init__(self, a, b, radicand):
        self.rad = radicand
        self.a, self.b = radicand.coerce(a), radicand.coerce(b)

    def coerce(self, other):
        if isinstance(other, L):
            assert self.rad == other.rad
            return other
        return L(other, 0, self.rad)

    def __add__(self, other):
        other = self.coerce(other)
        return L(self.a+other.a, self.b+other.b, self.rad)

    __radd__ = __add__

    def __neg__(self):
        return L(-self.a, -self.b, self.rad)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        other = self.coerce(other)
        return L(self.a*other.a+self.rad*self.b*other.b,
                 self.a*other.b+self.b*other.a, self.rad)

    __rmul__ = __mul__

    def inverse(self):
        norm = self.a*self.a-self.rad*self.b*self.b
        return L(self.a/norm, -self.b/norm, self.rad)

    def __truediv__(self, other):
        return self*self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other)*self.inverse()

    def __pow__(self, exponent):
        ans, base = self.coerce(1), self
        while exponent:
            if exponent & 1:
                ans *= base
            base *= base
            exponent //= 2
        return ans

    def __bool__(self):
        return bool(self.a) or bool(self.b)

    def __eq__(self, other):
        other = self.coerce(other)
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash((self.a, self.b))

    def enc(self):
        return [self.a.enc(), self.b.enc()]


def encpoly(p):
    return [v.enc() if isinstance(v, K) else [str(v)] for v in p]


def attachments():
    t = K([0, 1], [-F(1, 64), F(7, 16), -F(5, 4), 1])
    a, b, d = 1-4*t, 3-4*t, 7-12*t
    cases = []
    # Simultaneous sign negation reduces endpoint B=-a to endpoint B=a.
    for label, A in [('minus_d', -d), ('minus_b', -b),
                     ('minus_a', -a), ('plus_b', b), ('plus_d', d)]:
        B = a
        cubic = [-A, t.coerce(-3), t.coerce(0), 4*t]
        quadratic = [t*(B-A)**2-1, -2*t*(B-A), 4*t]
        g, U, V = xgcd(cubic, quadratic)
        # Audit of the saved certificate by multiplication, not another gcd.
        assert padd(pmul(U, cubic), pmul(V, quadratic)) == g
        cases.append({'reused_other_row': label, 'endpoint': 'plus_a',
                      'gcd': encpoly(g), 'bezout_cubic': encpoly(U),
                      'bezout_quadratic': encpoly(V)})
    return {'cases': cases, 'P_evaluations': 0,
            'all_gcds_one': all(c['gcd'] == [['1','0','0']] for c in cases)}


def modmul(a, b, f, p):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % p
    while len(c) >= len(f):
        v, i = c[-1], len(c)-len(f)
        for j, fj in enumerate(f):
            c[i+j] = (c[i+j]-v*fj) % p
        c.pop()
    return c+[0]*(len(f)-1-len(c))


def modpow(a, n, f, p):
    out = [1]+[0]*(len(f)-2)
    while n:
        if n & 1:
            out = modmul(out, a, f, p)
        a = modmul(a, a, f, p)
        n //= 2
    return out


def field_certificate():
    # One preselected good reduction, p=5. No prime search.
    f, p = [2, 4, 4, 0, 1], 5
    linear_roots = [x for x in range(p) if sum(c*x**i for i,c in enumerate(f)) % p == 0]
    quadratic_divisors = []
    for a in range(p):
        for b in range(p):
            # Remainder on division by T^2+a*T+b.
            r = f[:]
            for i in range(4, 1, -1):
                c = r[i]
                r[i-1] = (r[i-1]-c*a) % p
                r[i-2] = (r[i-2]-c*b) % p
            if r[0] == r[1] == 0:
                quadratic_divisors.append([b,a,1])
    square_test = modpow([1,2,0,1], (5**4-1)//2, f, p)
    assert not linear_roots and not quadratic_divisors
    assert square_test == [4,0,0,0]
    return {'prime': p, 'quartic': f, 'linear_roots': linear_roots,
            'quadratic_divisors': quadratic_divisors,
            'radicand_power_312': square_test, 'field_degree': 8}


def ecadd(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    X, Y = Q
    if x == X and y == -Y:
        return None
    slope = (3*x*x-48)/(2*y) if P == Q else (Y-y)/(X-x)
    xx = slope*slope-x-X
    return xx, slope*(x-xx)-y


def ecmul(n, P):
    R = None
    while n:
        if n & 1:
            R = ecadd(R, P)
        P = ecadd(P, P)
        n //= 2
    return R


def elliptic():
    cert = field_certificate()
    alpha = K([0,1], [-768,-61696,-96,0,1])
    rad = alpha**3-48*alpha-15424
    xx, yy = L(alpha,0,rad), L(0,1,rad)
    S, Q = (xx,yy), (xx.coerce(40),xx.coerce(216))
    assert ecmul(3,S) is None
    R0 = ecmul(3,Q)
    torsion = [None, S, (xx,-yy)]
    division = [ecadd(Q,T) for T in torsion]
    assert all(ecmul(3,T) == R0 for T in division)
    points = torsion[1:]+division
    assert len(set(points)) == 5
    scalars, triples = [], []
    identities = 0
    for x,y in points:
        assert y*y == x*x*x-48*x-15424
        assert x != 4
        u = (y+216)/(6*(x-4))
        v = (y-216)/(6*(x-4))
        a = (6-u*u*u+u)/2
        assert a == (-v*v*v+v)/2
        b, e = a-u, a-v
        # Two direct cubic identities, outside full-square counters.
        assert (a-b)**3+a+b == 6
        assert (a-e)**3+a+e == 0
        identities += 2
        triples.append((a,b,e))
        for s in (a,b,e):
            if s not in scalars:
                scalars.append(s)
    assert len(scalars) <= 128
    fibers = defaultdict(list)
    for i,a in enumerate(scalars):
        for j,b in enumerate(scalars):
            p = (a-b)**3+a+b
            # Separate expanded polynomial is the full-square audit oracle.
            audit = a**3-3*a*a*b+3*a*b*b-b**3+a+b
            assert p == audit
            fibers[p].append([i,j])
    hist = Counter(map(len, fibers.values()))
    n = len(scalars)
    assert sum(r*c for r,c in hist.items()) == n*n
    # Reciprocal multiplicity identity, audited over every pair.
    assert sum((F(1,len(v)) for v in fibers.values() for _ in v), F(0)) == len(fibers)
    selected = defaultdict(set)
    for a,b,e in triples:
        selected[6].add((scalars.index(a),scalars.index(b)))
        selected[0].add((scalars.index(a),scalars.index(e)))
    selected_pair_count = sum(map(len,selected.values()))
    selected_components = Counter({1:n*n-selected_pair_count})
    selected_components.update(map(len,selected.values()))
    return {'m':3, 'c':6, 'field_certificate':cert,
            'torsion_real_points_including_O':3, 'division_real_points':3,
            'parameter_points_after_pole_removal':5,
            'R0': [z.enc() for z in R0],
            'n':n, 'ordered_pairs':n*n, 'full_image':len(fibers),
            'fiber_histogram':dict(sorted(hist.items())),
            'singleton_pair_fraction':str(F(hist.get(1,0),n*n)),
            'full_collision_component_histogram':dict(sorted(hist.items())),
            'selected_collision_component_histogram':dict(sorted(selected_components.items())),
            'selected_pairs':selected_pair_count,
            'scalars':[s.enc() for s in scalars],
            'fibers':[{'value':z.enc(),'pairs':pairs} for z,pairs in fibers.items()],
            'P_evaluations':2*n*n+identities}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=['attachments','elliptic'])
    args = parser.parse_args()
    def timeout(*_):
        raise TimeoutError('120-second computational cap; no mathematical failure implied')
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(120)
    start, cpu = time.perf_counter(), time.process_time()
    result = attachments() if args.phase == 'attachments' else elliptic()
    signal.alarm(0)
    result['provenance'] = {'python':platform.python_version(), 'phase':args.phase,
        'command':'python3 research/notes/2026-10-11-transfer-division-entropy/exact_cycle.py '+args.phase,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'wall_seconds':time.perf_counter()-start, 'cpu_seconds':time.process_time()-cpu,
        'seed':None, 'equality':'exact rational quotient arithmetic',
        'degree_cap':32, 'per_run_seconds_cap':120, 'cycle_seconds_cap':600,
        'ordered_pair_evaluation_cap':200000}
    assert result['P_evaluations'] <= 200000
    path = Path(__file__).with_name(args.phase+'_results.json')
    if path.exists():
        raise FileExistsError('Preserving an existing result: '+str(path))
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('scalars','fibers','cases')}))


if __name__ == '__main__':
    main()
