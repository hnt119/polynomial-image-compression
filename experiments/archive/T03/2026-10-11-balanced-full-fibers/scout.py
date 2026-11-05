"""Offline, budgeted full-fiber audit of the fixed carrier at r=0,1 only.

Exact arithmetic in Z[zeta_(6*7^r)] on scaled scalar set 3A.
Build and enumeration are separate commands: build, scout, verify.
"""
from collections import Counter
from pathlib import Path
import hashlib
import itertools
import json
import platform
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from experiments.modular_lift import Field

RUN = Path(__file__).resolve().parent


class Budget:
    def __init__(self, stage):
        self.stage = stage
        self.path = RUN / 'budget.json'
        self.data = json.loads(self.path.read_text())
        self.counts = Counter()
        self.start = time.process_time()
        self.error = None

    def charge(self, kind, amount=1):
        previous = self.data.get('runs', [])
        used = sum(sum(x['counts'].values()) for x in previous if x['stage'] == self.stage)
        elapsed = time.process_time() - self.start
        stage_cpu = sum(x['cpu_seconds'] for x in previous if x['stage'] == self.stage)
        limits = self.data['discovery' if self.stage == 'discovery' else 'verification_reserve']
        if used + sum(self.counts.values()) + amount > limits['evaluations']:
            raise RuntimeError('stage evaluation allowance exhausted')
        if stage_cpu + elapsed > limits['program_cpu_seconds']:
            raise RuntimeError('stage program CPU allowance exhausted')
        if sum(x['cpu_seconds'] for x in previous) + elapsed > 598:
            raise RuntimeError('shared program CPU stop margin reached')
        self.counts[kind] += amount

    def finish(self, command):
        elapsed = time.process_time() - self.start
        previous=self.data.get('runs',[])
        stage_cpu=sum(x['cpu_seconds'] for x in previous if x['stage']==self.stage)
        limits=self.data['discovery' if self.stage=='discovery' else 'verification_reserve']
        over_time=(stage_cpu+elapsed>limits['program_cpu_seconds'] or
                   sum(x['cpu_seconds'] for x in previous)+elapsed>600)
        if over_time:
            self.error=self.error or 'Final CPU budget check failed'
        self.data.setdefault('runs', []).append({
            'command': command, 'stage': self.stage, 'counts': dict(self.counts),
            'cpu_seconds': elapsed, 'error': self.error,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'runtime': platform.python_version()})
        self.data['usage'] = {
            'evaluations': sum(sum(x['counts'].values()) for x in self.data['runs']),
            'program_cpu_seconds': sum(x['cpu_seconds'] for x in self.data['runs'])}
        self.path.write_text(json.dumps(self.data, indent=2) + '\n')
        print(json.dumps({'command': command, 'counts': self.counts,
                          'cpu_seconds': elapsed, 'shared_usage': self.data['usage']}), flush=True)
        if over_time:
            raise RuntimeError(self.error)


def mul(f, x, y):
    poly = [0] * (2*f.degree-1)
    for i, a in enumerate(x):
        if a:
            for j, b in enumerate(y):
                if b:
                    poly[i+j] += a*b
    return f.reduce(poly)


def reps(A,budget):
    n = len(A)
    # Lexicographic tuple order reverses under negation. No real ordering used.
    budget.charge('symmetry_negation_check',n)
    assert all(tuple(-v for v in A[i]) == A[n-1-i] for i in range(n))
    for i in range(n//2+1):
        for j in range(i, n-i):
            weight = len({(i,j), (j,i), (n-1-i,n-1-j), (n-1-j,n-1-i)})
            yield i, j, weight


def digest(distribution):
    h = hashlib.sha256()
    for value, count in sorted(distribution.items()):
        h.update((repr((value,count))+'\n').encode())
    return h.hexdigest()


def build(budget):
    for r in (0,1):
        q = 7**r
        f = Field(6*q)
        scalars = set()
        complex_points = set()
        amplitudes = []
        for h in range(1,9):
            for digits in itertools.product(range(-3,4),repeat=r):
                c = f.scale(f.one,h)
                for ell, digit in enumerate(digits):
                    factor = f.add(f.scale(f.one,2),f.scale(f.powers[(6*digit*7**ell)%f.m],-1))
                    c = mul(f,c,factor)
                amplitudes.append({'h':h,'digits':digits,'value':c})
                for nu in f.powers:
                    z = mul(f,c,nu)
                    budget.charge('complex_point_dedup')
                    complex_points.add(z)
                    x,y = f.decode3(z)
                    budget.charge('scalar_dedup',2)
                    scalars.update((x,y))
        A = sorted(scalars)
        budget.charge('scalar_reality_check',len(A))
        assert all(f.conj(a)==a for a in A)
        budget.charge('zero_membership_check')
        assert f.zero in scalars
        budget.charge('scalar_negation_closure_check',len(A))
        assert all(tuple(-v for v in a) in scalars for a in A)
        assert len(complex_points)==48*q*q
        n=len(A)
        assert 16*q*q+1<=n<=24*q*q-7
        if r==0:
            budget.charge('seed_scalar_identity_check',len(A))
            assert A==[(3*a,0) for a in range(-8,9)]
        case={'r':r,'q':q,'m':f.m,'modulus':f.modulus,'scaled3A':A,
              'amplitudes':amplitudes,'n':n,'encoded_points':len(complex_points),
              'forecast_representatives':(n+1)**2//4,'ordered_pairs':n*n}
        (RUN/f'case-r{r}.json').write_text(json.dumps(case,separators=(',',':'))+'\n')
        print(json.dumps({k:case[k] for k in ('r','n','encoded_points','forecast_representatives','ordered_pairs')}),flush=True)


def scout(budget):
    results=[]
    for r in (0,1):
        case=json.loads((RUN/f'case-r{r}.json').read_text())
        A=list(map(tuple,case['scaled3A']))
        n=len(A)
        f=Field(case['m'])
        # Forecast against the actual remaining allowance, before enumeration.
        previous=sum(sum(x['counts'].values()) for x in budget.data.get('runs',[]) if x['stage']=='discovery')
        assert previous+sum(budget.counts.values())+2*n+(n+1)**2//4<=1600000
        squares=[]
        for a in A:
            budget.charge('scalar_square')
            squares.append(mul(f,a,a))
        distribution=Counter()
        small_orbits=Counter()
        orbit_weights=Counter()
        for i,j,w in reps(A,budget):
            budget.charge('full_Q_symmetry_representative')
            value=f.add(squares[i],mul(f,A[i],A[j]),squares[j])
            distribution[value]+=w
            orbit_weights[w]+=1
            if w<4:
                small_orbits[(value,w)]+=w
        assert sum(w*c for w,c in orbit_weights.items())==n*n
        assert sum(orbit_weights.values())==(n+1)**2//4
        output_hist=Counter(distribution.values())
        pair_hist={fibre:fibre*count for fibre,count in sorted(output_hist.items())}
        assert sum(pair_hist.values())==n*n
        assert distribution[f.zero]==1
        below=sum(count for fibre,count in pair_hist.items() if fibre**4<n)
        exceeding=sum(count for fibre,count in pair_hist.items() if fibre>4)
        exceeding+=sum(count for (value,w),count in small_orbits.items() if w<distribution[value]<=4)
        cumulative=0
        median=None
        for fibre,count in pair_hist.items():
            cumulative+=count
            if cumulative>n*n//2:
                median=fibre
                break
        summary={'r':r,'n':n,'ordered_pairs':n*n,'image_size':len(distribution),
            'median_full_fiber':median,'strict_below_n_quarter':below,
            'pairs_exceeding_own_sign_swap_orbit':exceeding,
            'pairs_equal_to_own_sign_swap_orbit':n*n-exceeding,
            'max_full_fiber':max(output_hist),'output_histogram':dict(sorted(output_hist.items())),
            'pair_weighted_histogram':pair_hist,'symmetry_orbit_weight_counts':dict(orbit_weights),
            'full_distribution_sha256':digest(distribution),'status':'EXPERIMENTAL; complete exact enumeration'}
        (RUN/f'distribution-r{r}.json').write_text(json.dumps(sorted(distribution.items()),separators=(',',':'))+'\n')
        results.append(summary)
        print(json.dumps(summary),flush=True)
    (RUN/'scout-results.json').write_text(json.dumps(results,indent=2)+'\n')


def verify(budget):
    summaries=json.loads((RUN/'scout-results.json').read_text())
    results=[]
    for case_summary in summaries:
        r=case_summary['r']
        case=json.loads((RUN/f'case-r{r}.json').read_text())
        A=list(map(tuple,case['scaled3A']))
        n=len(A)
        f=Field(case['m'])
        previous=sum(sum(x['counts'].values()) for x in budget.data.get('runs',[]) if x['stage']=='verification')
        assert previous+sum(budget.counts.values())+3*n+(n+1)**2//4+(n*n if r==0 else 0)<=400000
        # Different complete representative traversal, plus norm product oracle.
        budget.charge('canonical_scalar_selection',n)
        B=[a for a in A if a!=f.zero and a<tuple(-v for v in a)]
        omega2=f.powers[2*f.m//3]
        budget.charge('norm_preprocessing',2*n)
        wy={a:f.mul(f.omega,a) for a in A}
        w2y={a:f.mul(omega2,a) for a in A}
        distribution=Counter()
        def put(a,b,weight):
            budget.charge('independent_norm_representative')
            z=f.add(a,f.scale(wy[b],-1))
            zb=f.add(a,f.scale(w2y[b],-1))
            distribution[f.mul(z,zb)]+=weight
        put(f.zero,f.zero,1)
        for i,a in enumerate(B):
            put(a,f.zero,4)
            for b in B[:i+1]:
                weight=2 if a==b else 4
                put(a,b,weight)
                put(a,tuple(-v for v in b),weight)
        assert digest(distribution)==case_summary['full_distribution_sha256']
        if r==0:
            integers=Counter()
            for x in range(-8,9):
                for y in range(-8,9):
                    budget.charge('independent_integer_seed_pair')
                    integers[(9*(x*x+x*y+y*y),0)]+=1
            assert distribution==integers
        results.append({'r':r,'n':n,'complete_distribution_match':'PASS',
                        'oracle':'complex norm, alternate complete symmetry traversal; integer raw square additionally at r=0'})
        print(json.dumps(results[-1]),flush=True)
    (RUN/'verification-results.json').write_text(json.dumps(results,indent=2)+'\n')


if __name__=='__main__':
    command=sys.argv[1]
    assert command in ('build','scout','verify')
    outputs={'build':['case-r0.json','case-r1.json'],
             'scout':['distribution-r0.json','distribution-r1.json','scout-results.json'],
             'verify':['verification-results.json']}[command]
    assert all(not (RUN/name).exists() for name in outputs),'Refusing to overwrite prior output'
    budget=Budget('verification' if command=='verify' else 'discovery')
    try:
        globals()[command](budget)
    except BaseException as exc:
        budget.error=repr(exc)
        raise
    finally:
        budget.finish(command)
