"""Frozen six-set diagnostic. Exact full squares; no parameter search."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, platform, sys, time
sys.path.insert(0, str(Path.cwd()))
from experiments.changed_collision_pattern import analyze, Budget

OUT=Path('local-only/runs/T01/2026-10-21-multiscale-collisions')
PARAMS={'AP_N':[8,12], 'CP_m':[2,3], 'B':[0,1,3], 'rho':'1/64',
        'D':[[0,1,3],[0,1,3,7]], 'metric_deltas':['1','1/16','1/256'],
        'tree_root':'[0,16)', 'tree_q':4, 'tree_levels':5,
        'scope':'six complete squares; metric and dyadic data only on four rational sets'}

def cover(values, delta):
    # Minimum number of freely placed closed intervals of length delta.
    left=None; count=0
    for value in sorted(values):
        if left is None or value>left+delta:
            left=value; count+=1
    return count

def rational_case(label, a):
    a=sorted(set(a)); fibers=defaultdict(list)
    for i,x in enumerate(a):
        for j,y in enumerate(a):
            z=(x-y)**3+x+y
            assert z==x**3-3*x*x*y+3*x*y*y-y**3+x+y
            fibers[z].append((i,j))
    hist=Counter(map(len,fibers.values())); branch_hist=Counter(); local=[]
    # q=4 is two standard dyadic levels per generation; root contains all scalars.
    assert all(0<=x<16 for x in a)
    for z,pairs in fibers.items():
        for i,j in pairs:
            count=0
            for level in range(5):
                width=F(16,4**level); finer=width/4
                parent=(a[i]//width,a[j]//width)
                children={(a[u]//finer,a[v]//finer) for u,v in pairs
                          if (a[u]//width,a[v]//width)==parent}
                assert len(children)<=8
                count+=len(children)>1
            branch_hist[count]+=1
    assert len({x//F(16,4**5) for x in a})==len(a)
    for level in range(6):
        width=F(16,4**level); cell_outputs=defaultdict(Counter)
        for z,pairs in fibers.items():
            for i,j in pairs:cell_outputs[(a[i]//width,a[j]//width)][z]+=1
        local.append({'level':level,'scalar_width':str(width),
                      'actual_cell_output_incidences':sum(map(len,cell_outputs.values())),
                      'max_local_actual_fiber':max(v for co in cell_outputs.values() for v in co.values()),
                      'local_pair_mass_at_least_2':sum(v for co in cell_outputs.values() for v in co.values() if v>=2)})
    metric=[]
    for delta in map(F,PARAMS['metric_deltas']):
        count=cover(fibers,delta); span=max(fibers)-min(fibers)
        assert count<=1+span/delta
        metric.append({'interval_length':str(delta),'minimum_cover':count,
                       'span':str(span),'capacity_upper':str(1+span/delta)})
    raw={'id':label,'N':len(a),'Q':len(a)**2,'Z':len(fibers),'B_uncovered':0,
         'fiber_histogram':dict(sorted(hist.items())),
         'branch_event_pair_histogram':dict(sorted(branch_hist.items())),
         'local_actual_fibers':local,'metric_covers':metric,
         'scalars':list(map(str,a)),
         'full_fibers':[{'z':str(z),'pairs':pairs} for z,pairs in sorted(fibers.items())]}
    assert sum(k*v for k,v in hist.items())==len(a)**2
    return raw

def main():
    start=time.perf_counter(); data=[]
    for n in PARAMS['AP_N']:data.append(rational_case('AP'+str(n),list(map(F,range(n)))))
    budget=Budget()
    for m in PARAMS['CP_m']:
        summary,raw=analyze(m,budget)
        data.append({'id':'CP'+str(m),'N':summary['N'],'Q':summary['Q'],'Z':summary['Z'],
                     'B_uncovered':summary['B'],'full_image':summary['full_image'],
                     'fiber_histogram':summary['fiber_histogram'],'raw':raw})
    for d in PARAMS['D']:
        data.append(rational_case('two_level_D'+str(len(d)),[F(b)+F(s,64) for b in PARAMS['B'] for s in d]))
    assert len(data)==6 and max(row['N'] for row in data)<=24
    charged=2*sum(row['N']**2 for row in data)
    output={'parameters':PARAMS,'results':data,'provenance':{
        'command':'python3 local-only/runs/T01/2026-10-21-multiscale-collisions/audit.py',
        'python':platform.python_version(),'network':'none','randomness':'none',
        'P_evaluations':charged,'elapsed_seconds':time.perf_counter()-start,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'import_sha256':hashlib.sha256(Path('experiments/changed_collision_pattern.py').read_bytes()).hexdigest(),
        'parameter_sha256':hashlib.sha256(json.dumps(PARAMS,sort_keys=True).encode()).hexdigest()}}
    with (OUT/'exact-audit.json').open('x') as f:json.dump(output,f,indent=2);f.write('\n')
    for row in data:
        print(row['id'],row['N'],row.get('full_image',row['Z']),row['fiber_histogram'],row.get('branch_event_pair_histogram'),row.get('metric_covers'))
    print('P evaluations:',charged)
if __name__=='__main__':main()
