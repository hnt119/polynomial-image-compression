"""Reserved exact validation: reconstruct complete Q distributions via symmetry
representatives and the complex norm; regroup F-lines by cross products.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,sys,time
from scout import Field,sparse_mul,automorphism
RUN=Path(__file__).resolve().parent
previous=json.loads((RUN/'scout-results.json').read_text())
start=time.process_time();counts=Counter();results=[];error=None
used=sum(previous['budget']['counts']['verification'].values())
def charge(kind):
 if used+sum(counts.values())>=400000:raise RuntimeError('verification evaluation reserve exhausted')
 if time.process_time()-start>=119:raise RuntimeError('119 CPU-second verification deadline')
 if previous['budget']['cpu_seconds']+time.process_time()-start>=600:raise RuntimeError('shared CPU cap')
 counts[kind]+=1
try:
 for k in (1,2):
  raw=json.loads((RUN/f'case-k{k}.json').read_text());A=list(map(tuple,raw['scaled3A']));f=Field(6*7**(k-1));n=len(A)
  index={a:i for i,a in enumerate(A)};neg=[index[tuple(-v for v in a)] for a in A]
  omegaY=[sparse_mul(f,f.omega,y) for y in A];omega2=f.powers[2*f.m//3];omega2Y=[sparse_mul(f,omega2,y) for y in A]
  distribution=Counter();representatives=0
  for i in range(n):
   for j in range(n):
    orbit={(i,j),(j,i),(neg[i],neg[j]),(neg[j],neg[i])}
    if (i,j)!=min(orbit):continue
    charge('symmetry_orbit_complex_norm');representatives+=1
    z=f.add(A[i],f.scale(omegaY[j],-1));zb=f.add(A[i],f.scale(omega2Y[j],-1));value=sparse_mul(f,z,zb);distribution[value]+=len(orbit)
  assert representatives==(n+1)**2//4
  assert sum(distribution.values())==n*n
  digest=hashlib.sha256()
  for value,c in sorted(distribution.items()):digest.update((repr((value,c))+'\n').encode())
  assert digest.hexdigest()==raw['summary']['full_distribution_sha256']
  line_sizes=None
  if k>=2:
   sigma=2*7**(k-1)-1;reps=[];line_sizes=[];sigmas={a:automorphism(f,a,sigma) for a in A if a!=f.zero}
   for a in A:
    if a==f.zero:continue
    for ri,b in enumerate(reps):
     charge('projective_cross_product')
     if sparse_mul(f,a,sigmas[b])==sparse_mul(f,b,sigmas[a]):line_sizes[ri]+=1;break
    else:reps.append(a);line_sizes.append(1)
   assert dict(sorted(Counter(line_sizes).items()))=={int(a):b for a,b in raw['summary']['F_line_population_histogram'].items()}
  results.append({'k':k,'n':n,'norm_distribution':'PASS','symmetry_representatives':representatives,'projective_cross_product_grouping':'PASS' if line_sizes else 'N/A'})
  print(json.dumps(results[-1]),flush=True)
except BaseException as exc:
 error=repr(exc);raise
finally:
 data={'cases':results,'error':error,'verification_evaluations':dict(counts),'cpu_seconds':time.process_time()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'shared_total_evaluations':previous['budget']['total_evaluations']+sum(counts.values()),'shared_total_cpu_seconds':previous['budget']['cpu_seconds']+time.process_time()-start}
 (RUN/'verification-results.json').write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps(data),flush=True)
