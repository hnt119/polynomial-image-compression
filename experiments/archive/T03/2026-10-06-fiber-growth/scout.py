"""Two predetermined exact scouts of the twisted-binomial carrier, k=1,2.
No old experiment main is called. All mathematical work is budgeted.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib,json,math,platform,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from experiments.modular_lift import Field
RUN=Path(__file__).resolve().parent
class Budget:
 def __init__(self):
  self.start=time.process_time();self.counts={'discovery':Counter(),'verification':Counter()}
 def check(self):
  if time.process_time()-self.start>=470:raise RuntimeError('470 CPU-second scout deadline')
 def charge(self,category,kind,count=1):
  self.check(); cap=1600000 if category=='discovery' else 400000
  if sum(self.counts[category].values())+count>cap:raise RuntimeError('reserved budget cap')
  self.counts[category][kind]+=count
 def summary(self):return {'counts':{k:dict(v) for k,v in self.counts.items()},'total_evaluations':sum(sum(v.values()) for v in self.counts.values()),'cpu_seconds':time.process_time()-self.start}
def trim(p):
 p=list(p)
 while p and p[-1]==0:p.pop()
 return p
def divrem(a,b):
 a=trim(a);b=trim(b);q=[Fraction(0)]*max(0,len(a)-len(b)+1)
 while len(a)>=len(b) and a:
  i=len(a)-len(b);c=a[-1]/b[-1];q[i]=c
  for j,x in enumerate(b):a[i+j]-=c*x
  a=trim(a)
 return trim(q),a
def psub(a,b):
 c=list(a)+[Fraction(0)]*max(0,len(b)-len(a))
 for i,x in enumerate(b):c[i]-=x
 return trim(c)
def pmul(a,b):
 c=[Fraction(0)]*max(0,len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def inverse(f,a):
 r0=list(map(Fraction,f.modulus));r1=trim(map(Fraction,a));t0=[];t1=[Fraction(1)]
 while r1:
  q,r=divrem(r0,r1);r0,r1=r1,r;t0,t1=t1,psub(t0,pmul(q,t1))
 assert len(r0)==1
 return f.reduce([x/r0[0] for x in t0])
def sparse_mul(f,a,b):
 p=[0]*(2*f.degree-1)
 aa=[(i,x) for i,x in enumerate(a) if x];bb=[(i,x) for i,x in enumerate(b) if x]
 for i,x in aa:
  for j,y in bb:p[i+j]+=x*y
 return f.reduce(p)
def automorphism(f,a,e):
 z=f.zero
 for i,c in enumerate(a):
  if c:z=f.add(z,f.scale(f.powers[i*e%f.m],c))
 return z
def qvalue(f,x,y,x2,y2):return f.add(x2,sparse_mul(f,x,y),y2)
def projective_key(f,a,sigma,budget):
 budget.charge('discovery','projective_canonical_key')
 b=automorphism(f,a,sigma);ib=inverse(f,b);key=sparse_mul(f,a,ib)
 budget.charge('verification','projective_ratio_oracle')
 assert sparse_mul(f,key,b)==a
 return tuple((v.numerator,v.denominator) if isinstance(v,Fraction) else (v,1) for v in key)
def scout(k,budget):
 q=7**(k-1);m=6*q;f=Field(m)
 budget.check();amp=[]
 for h in range(1,9):
  for j in range(q):amp.append(f.scale(f.add(f.one,sparse_mul(f,f.omega,f.powers[6*j%m])),h))
 # Validate cosets through distinct actual norms, as in the analytic proof.
 norms=[]
 for c in amp:
  budget.charge('verification','amplitude_norm')
  norms.append(sparse_mul(f,c,f.conj(c)))
 assert len(set(norms))==8*q
 A=set();encoded=0
 for c in amp:
  for u in f.powers:
   budget.check();x,y=f.decode3(sparse_mul(f,c,u));A.update((x,y));encoded+=1
 A=sorted(A);n=len(A)
 # Scaled3A has identical cardinalities, fiber counts and F-line populations.
 remaining=1600000-sum(budget.counts['discovery'].values())
 if n*n+n>remaining:raise RuntimeError(f'preflight fails: k{k}, n{n}, square{n*n}, remaining{remaining}')
 print(json.dumps({'phase':'preflight','k':k,'n':n,'pair_evaluations':n*n}),flush=True)
 line_sizes=Counter();cache={}
 if k>=2:
  sigma=2*q-1
  for a in A:
   if a==f.zero:continue
   g=math.gcd(*a);b=tuple(v//g for v in a)
   if next(v for v in b if v)<0:b=tuple(-v for v in b)
   if b not in cache:cache[b]=projective_key(f,b,sigma,budget)
   else:budget.charge('discovery','projective_cached_key')
   line_sizes[cache[b]]+=1
 squares=[sparse_mul(f,a,a) for a in A]
 counts=Counter();validation_limit=min(n*n,1024)
 for i,x in enumerate(A):
  for j,y in enumerate(A):
   budget.charge('discovery','Q_ordered_pair');v=qvalue(f,x,y,squares[i],squares[j]);counts[v]+=1
   if i*n+j<validation_limit:
    budget.charge('verification','complex_norm_oracle')
    z=f.add(x,f.scale(sparse_mul(f,f.omega,y),-1));assert v==sparse_mul(f,z,f.conj(z))
   if k==1:
    budget.charge('verification','rational_scalar_oracle');assert not any(x[1:]+y[1:]);assert v==f.scale(f.one,x[0]**2+x[0]*y[0]+y[0]**2)
 hist=Counter()
 for size in counts.values():hist[size]+=size
 assert sum(hist.values())==n*n
 def quantile(rank):
  s=0
  for size,c in sorted(hist.items()):
   s+=c
   if s>rank:return size
 thresholds={}
 for den in (4,2):
  threshold=1
  while threshold**den<n:threshold+=1
  thresholds['1/'+str(den)]={'threshold_ceiling':threshold,'bad_pairs':sum(c for size,c in hist.items() if size<threshold)}
 data={'k':k,'q':q,'m':m,'t':8*q,'n':n,'image':len(counts),'median_full_fiber':quantile(n*n//2),'full_fiber_histogram':dict(sorted(hist.items())),'max_full_fiber':max(hist),'max_F_line':max(line_sizes.values()) if line_sizes else None,'F_line_population_histogram':dict(sorted(Counter(line_sizes.values()).items())),'projective_directions':len(line_sizes) if line_sizes else None,'tails':thresholds,'zero_fiber':counts[f.zero],'encoded_orbit_points':encoded,'method':'Complete ordered-pair enumeration; exact cyclotomic integer coefficient equality; scalar set is3A'}
 digest=hashlib.sha256()
 for v,c in sorted(counts.items()):digest.update((repr((v,c))+'\n').encode())
 data['full_distribution_sha256']=digest.hexdigest()
 raw={'field_modulus':f.modulus,'scaled3A':A,'summary':data}
 (RUN/f'case-k{k}.json').write_text(json.dumps(raw,indent=2)+'\n')
 print(json.dumps(data),flush=True)
 return data
if __name__=='__main__':
 budget=Budget();results=[];error=None
 try:
  for k in (1,2):results.append(scout(k,budget))
 except BaseException as exc:
  error=repr(exc);raise
 finally:
  summary={'cases':results,'error':error,'budget':budget.summary(),'python':platform.python_version(),'command':sys.argv,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic_dependency_sha256':hashlib.sha256(Path('experiments/modular_lift.py').read_bytes()).hexdigest(),'fixed_sizes':[1,2],'seed':None,'network':False}
  (RUN/'scout-results.json').write_text(json.dumps(summary,indent=2)+'\n')
