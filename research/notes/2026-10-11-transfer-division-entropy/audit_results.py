"""Independent saved-certificate audit. Does not import exact_cycle.

Hardcoded rational reduction rules verify Bezout identities and all 196
elliptic square cells. This is an audit, not an expanded candidate search.
"""
from fractions import Fraction as F
from collections import Counter, defaultdict
from pathlib import Path
from math import lcm, ceil
import hashlib
import json
import platform
import signal
import time

ROOT = Path(__file__).parent


def conv(a,b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def red3(p):
    p = list(p)+[F(0)]*max(0,3-len(p))
    for i in range(len(p)-1,2,-1):
        c = p[i]
        p[i-3] += c/64
        p[i-2] -= 7*c/16
        p[i-1] += 5*c/4
    return tuple(p[:3])


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def scale(a,c):
    return tuple(x*c for x in a)


def mul3(a,b):
    return red3(conv(a,b))


def poly3(p,q):
    out = [(F(0),)*3 for _ in range(len(p)+len(q)-1)]
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            out[i+j] = add(out[i+j],mul3(x,y))
    return out


def bezout_audit(data):
    zero, one, t = (F(0),)*3, (F(1),F(0),F(0)), (F(0),F(1),F(0))
    a,b,d = (F(1),F(-4),F(0)), (F(3),F(-4),F(0)), (F(7),F(-12),F(0))
    vals = {'minus_d':scale(d,-1),'minus_b':scale(b,-1),
            'minus_a':scale(a,-1),'plus_b':b,'plus_d':d}
    assert len(data['cases']) == 5
    for c in data['cases']:
        A,B = vals[c['reused_other_row']],a
        delta = add(B,scale(A,-1))
        cubic = [scale(A,-1),scale(one,-3),zero,scale(t,4)]
        quadratic = [add(mul3(t,mul3(delta,delta)),scale(one,-1)),
                     scale(mul3(t,delta),-2),scale(t,4)]
        U = [tuple(map(F,x)) for x in c['bezout_cubic']]
        V = [tuple(map(F,x)) for x in c['bezout_quadratic']]
        left,right = poly3(U,cubic),poly3(V,quadratic)
        result = [add(x,y) for x,y in zip(left,right)]
        assert len(left) == len(right) == 5
        assert result == [one,zero,zero,zero,zero]


def red4(p):
    p = list(p)+[F(0)]*max(0,4-len(p))
    for i in range(len(p)-1,3,-1):
        c = p[i]
        p[i-4] += 768*c
        p[i-3] += 61696*c
        p[i-2] += 96*c
    return tuple(p[:4])


def mul4(a,b):
    return red4(conv(a,b))


def mul8(a,b):
    ac,bd = mul4(a[:4],b[:4]),mul4(a[4:],b[4:])
    real = add(ac,mul4(bd,(-15424,-48,0,1)))
    imag = add(mul4(a[:4],b[4:]),mul4(a[4:],b[:4]))
    return real+imag


def decode(value):
    return tuple(F(x) for part in value for x in part)


def conjugate_bound(values):
    # Every conjugate of alpha has modulus <= 1+max(|f_i|).
    # |Y| <= R^2+20000 follows from Y^2=alpha^3-48alpha-15424.
    R, B = 61697, 61697**2+20000
    return ceil(max(sum(abs(v[i])*R**i for i in range(4))+
                    B*sum(abs(v[4+i])*R**i for i in range(4)) for v in values))


def main():
    def timeout(*_):
        raise TimeoutError('120-second audit cap')
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(120)
    start,cpu = time.perf_counter(),time.process_time()
    at = json.loads((ROOT/'attachments_results.json').read_text())
    el = json.loads((ROOT/'elliptic_results.json').read_text())
    bezout_audit(at)
    scalars = [decode(s) for s in el['scalars']]
    assert len(scalars) == len(set(scalars)) == 14
    observed = defaultdict(list)
    for i,x in enumerate(scalars):
        for j,y in enumerate(scalars):
            delta = add(x,scale(y,-1))
            output = add(mul8(mul8(delta,delta),delta),add(x,y))
            observed[output].append([i,j])
    supplied = {decode(row['value']):row['pairs'] for row in el['fibers']}
    assert observed == supplied
    assert sorted(pair for rows in observed.values() for pair in rows) == [
        [i,j] for i in range(14) for j in range(14)]
    assert Counter(map(len,observed.values())) == {1:186,5:2}
    assert len(observed) == 188
    assert sum(F(1,len(rows)) for rows in observed.values() for _ in rows) == 188
    denominator = lcm(*(v.denominator for output in observed for v in output))
    W, S = conjugate_bound(observed), max(1,conjugate_bound(scalars))
    sep_denom = denominator**8*(2*W)**7
    result = {'status':'PASS', 'bezout_certificates':5,
              'independent_P_evaluations':196,
              'full_pair_vertices_including_isolates':196,
              'component_histogram':{'1':186,'5':2},
              'common_output_denominator':str(denominator),
              'all_conjugate_output_bound':str(W),
              'all_conjugate_input_bound':str(S),
              'separation_bound':'1 / (common_output_denominator^8 * (2*all_conjugate_output_bound)^7)',
              'separation_denominator_bits':sep_denom.bit_length(),
              'total_cycle_P_evaluations':at['P_evaluations']+el['P_evaluations']+196,
              'python':platform.python_version(),
              'wall_seconds':time.perf_counter()-start,
              'cpu_seconds':time.process_time()-cpu,
              'hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                        for name in ['exact_cycle.py','attachments_results.json',
                                     'elliptic_results.json','audit_results.py']}}
    assert result['total_cycle_P_evaluations'] <= 200000
    out = ROOT/'audit_results.json'
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    signal.alarm(0)
    print(json.dumps(result))


if __name__ == '__main__':
    main()
