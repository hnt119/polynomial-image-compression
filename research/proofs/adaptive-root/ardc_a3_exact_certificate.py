"""Exact exhaustive A3→A4 optimizer certificate.

All calculations use Fraction and integer square roots. The coefficient field
is Q(sqrt(2),sqrt(3),sqrt(5),sqrt(7),sqrt(13),alpha), alpha^2=4+sqrt(3).
"""
from fractions import Fraction as F
from itertools import combinations,combinations_with_replacement
from functools import lru_cache
from math import isqrt
import json,time
BITS=180;DEN=1<<BITS
PRIMES=(2,3,5,7,13)
def ia(a,b):return a[0]+b[0],a[1]+b[1]
def ine(a):return -a[1],-a[0]
def isc(a,t):return(a[0]*t,a[1]*t)if t>=0 else(a[1]*t,a[0]*t)
def im(a,b):
 z=[x*y for x in a for y in b];return min(z),max(z)
def idiv(a,b):
 assert b[0]>0 or b[1]<0,('interval denominator',b)
 return im(a,(1/b[1],1/b[0]))
def isq(a):
 assert a[0]>=0
 def lo(q):return F(isqrt((q.numerator<<(2*BITS))//q.denominator),DEN)
 return lo(a[0]),lo(a[1])+F(1,DEN)
def sign(a):
 assert a[0]>0 or a[1]<0,('ambiguous sign',a)
 return 1 if a[0]>0 else-1
def intersect(a,b):return a[0]<=b[1]and b[0]<=a[1]
FACT=[1]*32
for m in range(32):
 for j,p in enumerate(PRIMES):
  if m>>j&1:FACT[m]*=p
IV=[isq((F(d),F(d)))if m else(F(1),F(1))for m,d in enumerate(FACT)]
ALPHAIV=isq(ia((F(4),F(4)),IV[2]));IV +=[im(x,ALPHAIV)for x in IV]
MUL=[]
for i in range(64):
 row=[]
 for j in range(64):
  fac=FACT[(i&j)&31];mask=i^j
  if i&j&32:row.append(((mask,4*fac),(mask^2,fac*(3 if mask&2 else 1))))
  else:row.append(((mask,fac),))
 MUL.append(row)
class K:
 def __init__(self,a=0):self.v=a.v if isinstance(a,K)else{m:F(v)for m,v in a.items()if v}if isinstance(a,dict)else({0:F(a)}if a else{})
 def __bool__(a):return bool(a.v)
 def __eq__(a,b):return a.v==K(b).v
 def __add__(a,b):
  z=a.v.copy()
  for m,v in K(b).v.items():z[m]=z.get(m,F(0))+v
  return K(z)
 __radd__=__add__
 def __neg__(a):return K({m:-v for m,v in a.v.items()})
 def __sub__(a,b):return a+-K(b)
 def __rsub__(a,b):return K(b)+-a
 def __mul__(a,b):
  z={}
  for i,x in a.v.items():
   for j,y in K(b).v.items():
    xy=x*y
    for m,f in MUL[i][j]:z[m]=z.get(m,F(0))+f*xy
  return K(z)
 __rmul__=__mul__
 def __truediv__(a,t):return K({m:v/F(t)for m,v in a.v.items()})
 def __pow__(a,j):
  z=K(1)
  for _ in range(j):z=z*a
  return z
 def iv(a):return kiv(tuple(sorted(a.v.items())))
 def text(a):
  return ' + '.join(str(v)+(''if not(m&31)else'*sqrt('+str(FACT[m&31])+')')+('*alpha'if m&32 else'')for m,v in sorted(a.v.items()))or'0'
@lru_cache(None)
def kiv(v):
 z=(F(0),F(0))
 for m,a in v:z=ia(z,isc(IV[m],a))
 return z
def ksign(a):return sign(a.iv())if a else 0
def main():
 start=time.time();alpha=K({32:1});r2=K({1:1});r3=K({2:1});r5=K({4:1});r7=K({8:1});r13=K({16:1})
 smallalpha=r13*(4-r3)*alpha/13
 gamma=(K({9:1})+r2)/2;smallgamma=(K({9:1})-r2)/2
 pos=[K(1),smallgamma,smallalpha,r3,r5,alpha,gamma,r7]
 assert all(pos[i].iv()[1]<pos[i+1].iv()[0]for i in range(7))
 A=[-a for a in reversed(pos)]+pos;M=r7
 pairs=list(combinations_with_replacement(range(16),2));sp=[(A[i]+A[j],A[i]*A[j])for i,j in pairs]
 polys=[];roots=[];boundary=0;nonadmissible=0;nonreal=0;skipped=0
 for i,j in combinations(range(len(pairs)),2):
  s,p=sp[i];t,q=sp[j];D=s-t;E=p-q
  if not D:skipped+=1;continue
  DD=D*D;a=-3*DD;b=2*D*E-2*DD*(s+t);c=E*E-2*DD*(p+q)+DD*DD
  disc=b*b-4*a*c
  pol=(a,b,c,i,j,D,E);ix=len(polys);polys.append(pol)
  if not disc:rads=[((F(0),F(0)),0)]
  elif sign(disc.iv())<0:nonreal+=2;continue
  else:rad=isq(disc.iv());rads=[(ine(rad),-1),(rad,1)]
  for rad,epsroot in rads:
   cv=idiv(ia(ine(b.iv()),rad),isc(a.iv(),2))
   if intersect(cv,M.iv()):
    assert a*M*M+b*M+c==0
    assert ksign(2*a*M+b)==epsroot
    boundary+=1;continue
   if cv[1]<M.iv()[0]:nonadmissible+=1;continue
   assert cv[0]>M.iv()[1]
   roots.append({'iv':cv,'index':ix,'radsign':epsroot})
 print('generated',len(polys),'polynomials',len(roots),'admissible roots',time.time()-start,flush=True)
 roots.sort(key=lambda r:r['iv']);clusters=[];end=None
 for rt in roots:
  if end is not None and rt['iv'][0]<=end:
   clusters[-1].append(rt);end=max(end,rt['iv'][1])
  else:clusters.append([rt]);end=rt['iv'][1]
 print('root clusters',len(clusters),'max cluster',max(map(len,clusters)),time.time()-start,flush=True)
 records=[];hist={}
 for cli,cl in enumerate(clusters):
  assert len({r['index']for r in cl})==len(cl), 'A cluster contains both roots of one quadratic'
  first=polys[cl[0]['index']];a,b,c=first[:3];exact=None
  for ot in cl[1:]:
   aa,bb,cc=polys[ot['index']][:3]
   H=aa*b-a*bb;G=a*cc-aa*c
   if not H:
    assert not G
    assert ot['radsign']==cl[0]['radsign']
   else:
    assert a*G*G+b*G*H+c*H*H==0
    assert aa*G*G+bb*G*H+cc*H*H==0
    assert ksign(2*a*G+b*H)*ksign(H)==cl[0]['radsign']
    assert ksign(2*aa*G+bb*H)*ksign(H)==ot['radsign']
    ev=idiv(G.iv(),H.iv())
    assert intersect(ev,cl[0]['iv'])and intersect(ev,ot['iv'])
    exact=(G,H)
  par=list(range(272));witness=[]
  def root(i):
   while par[i]!=i:par[i]=par[par[i]];i=par[i]
   return i
  for item in cl:
   _,_,_,i,j,D,E=polys[item['index']]
   Z=idiv(ia(ine(im(D.iv(),cl[0]['iv'])),(D*D-E).iv()),isc(D.iv(),2))
   tau=sign(Z);sigma=sign(ia(Z,(-D).iv()))
   u=2*i+(sigma==1);v=2*j+(tau==1)
   par[root(u)]=root(v);witness.append([i,sigma,j,tau])
  groups={}
  for v in range(272):groups.setdefault(root(v),[]).append([v//2,-1 if v%2==0 else 1])
  size=len(groups);hist[size]=hist.get(size,0)+1
  record={'interval':[str(v)for v in cl[0]['iv']],'s':size,'equation_count':len(cl),'groups':[g for g in groups.values()if len(g)>1],'polynomial':[x.text()for x in(a,b,c)],'witness':witness}
  if a*9+b*3+c==0 and cl[0]['iv'][0]<=3<=cl[0]['iv'][1]:
   assert ksign(6*a+b)==cl[0]['radsign']
   record['C_exact']='3'
  if exact is not None:record['field_root_quotient']=[x.text()for x in exact]
  records.append(record)
  if cli%1000==0:print('certified',cli,'best',min(hist),time.time()-start,flush=True)
 best=min(hist);mins=[r for r in records if r['s']==best]
 assert best==269 and len(mins)==1 and mins[0].get('C_exact')=='3'
 assert hist=={271:4520,270:261,269:1}
 result={'A':[a.text()for a in A],'pairs':pairs,'field_basis':'sqrt(2)^e0 sqrt(3)^e1 sqrt(5)^e2 sqrt(7)^e3 sqrt(13)^e4 alpha^e5; alpha^2=4+sqrt(3)','polynomials':len(polys),'skipped_same_sum':skipped,'nonreal_roots':nonreal,'boundary_roots':boundary,'nonadmissible_roots':nonadmissible,'root_records':len(roots),'distinct_admissible_roots':len(clusters),'minimum':best,'least_minimizer':'3','minimizers':mins,'distribution':hist,'candidates':records}
 with open('output/ardc_a3_exact_results.json','w')as f:json.dump(result,f,indent=2)
 print(json.dumps({k:v for k,v in result.items()if k not in('candidates','pairs')},indent=2));print('time',time.time()-start)
if __name__=='__main__':main()
