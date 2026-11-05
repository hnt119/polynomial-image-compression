"""Complete adaptive A2 optimizer certificate, using rational arithmetic only.

Arithmetic is in Q(sqrt(3),sqrt(7)); candidate roots are isolated by rational
intervals. Different collision quadratics sharing a root are checked by their
linear gcd. No floating-point assertion participates in the certificate.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from math import isqrt
import json

BITS=160
DEN=1<<BITS
def ia(a,b): return a[0]+b[0],a[1]+b[1]
def ine(a):return -a[1],-a[0]
def isc(a,t):return (a[0]*t,a[1]*t) if t>=0 else (a[1]*t,a[0]*t)
def isqrt_interval(a):
 assert a[0]>=0
 def lo(q): return F(isqrt((q.numerator<<(2*BITS))//q.denominator),DEN)
 return lo(a[0]),lo(a[1])+F(1,DEN)
RAD=[(F(1),F(1))]+[isqrt_interval((F(d),F(d)))for d in (3,7,21)]
class K:
 def __init__(self,a=0):self.v=a.v if isinstance(a,K) else tuple(map(F,a)) if isinstance(a,(tuple,list)) else(F(a),F(0),F(0),F(0))
 def __add__(a,b):b=K(b);return K(tuple(x+y for x,y in zip(a.v,b.v)))
 __radd__=__add__
 def __neg__(a):return K(tuple(-x for x in a.v))
 def __sub__(a,b):return a+-K(b)
 def __rsub__(a,b):return K(b)+-a
 def __mul__(a,b):
  b=K(b);out=[F(0)]*4
  for i,x in enumerate(a.v):
   for j,y in enumerate(b.v):
    common=i&j;out[i^j]+=x*y*(3 if common&1 else 1)*(7 if common&2 else 1)
  return K(out)
 __rmul__=__mul__
 def conj(a,j):return K(tuple(v*(-1 if (i&j).bit_count()%2 else 1)for i,v in enumerate(a.v)))
 def inv(a):
  b=a.conj(1)*a.conj(2)*a.conj(3);n=a*b
  assert n.v[0] and not any(n.v[1:])
  return K(tuple(x/n.v[0]for x in b.v))
 def __truediv__(a,b):return a*K(b).inv()
 def __bool__(a):return any(a.v)
 def __eq__(a,b):return a.v==K(b).v
 def __hash__(a):return hash(a.v)
 def __pow__(a,j):
  assert j>=0;b=K(1)
  for _ in range(j):b=b*a
  return b
 def iv(a):return field_interval(a.v)
 def text(a):
  return ' + '.join(str(v)+(''if i==0 else '*sqrt('+str((1,3,7,21)[i])+')')for i,v in enumerate(a.v)if v)or'0'
@lru_cache(None)
def field_interval(v):
 out=(F(0),F(0))
 for x,r in zip(v,RAD):out=ia(out,isc(r,x))
 return out
def sign(iv):
 assert iv[0]>0 or iv[1]<0,('ambiguous sign',iv)
 return 1 if iv[0]>0 else-1
def check_intersect(a,b):assert a[0]<=b[1] and b[0]<=a[1]
def ksign(a):return sign(a.iv()) if a else 0
def main():
 A=[K(-3),K((0,0,-1,0)),K((0,-1,0,0)),K(-1),K(1),K((0,1,0,0)),K((0,0,1,0)),K(3)]
 pairs=list(combinations_with_replacement(range(8),2))
 sp=[(A[i]+A[j],A[i]*A[j])for i,j in pairs]
 polys={};skipped=0
 for i,j in combinations(range(36),2):
  s,p=sp[i];t,q=sp[j];D=s-t;E=p-q
  if not D:skipped+=1;continue
  b=-(2*E/D-2*(s+t))/3
  c=-(E*E/(D*D)-2*(p+q)+D*D)/3
  polys.setdefault((b,c),[]).append((i,j,D,E/D))
 print('normalized polynomials',len(polys),'pair comparisons',sum(map(len,polys.values())),'same sum',skipped,flush=True)
 roots=[];nonreal=0;nonadmissible=0;boundary=0
 for index,((b,c),edges) in enumerate(polys.items()):
  disc=b*b-4*c
  if not disc:rads=[((F(0),F(0)),0)]
  elif sign(disc.iv())<0:nonreal+=2;continue
  else:
   r=isqrt_interval(disc.iv());rads=[(ine(r),-1),(r,1)]
  for r,epsroot in rads:
   iv=isc(ia(ine(b.iv()),r),F(1,2))
   if iv[0]<=3<=iv[1]:
    assert K(9)+3*b+c==0
    assert ksign(6+b)==epsroot
    boundary+=1;continue
   if iv[1]<3:nonadmissible+=1;continue
   assert iv[0]>3
   roots.append({'iv':iv,'b':b,'c':c,'index':index,'edges':edges,'radsign':epsroot})
 roots.sort(key=lambda x:x['iv'])
 clusters=[]
 for root in roots:
  if clusters and root['iv'][0]<=max(x['iv'][1]for x in clusters[-1]):clusters[-1].append(root)
  else:clusters.append([root])
 print('admissible roots with polynomial multiplicity',len(roots),'clusters',len(clusters),'nonreal',nonreal,'nonadmissible',nonadmissible,'boundary',boundary,flush=True)
 records=[]
 for cl in clusters:
  assert len({r['index']for r in cl})==len(cl), 'A cluster contains both roots of one quadratic'
  first=cl[0];exact=None
  for other in cl[1:]:
   b,c=first['b'],first['c'];bb,cc=other['b'],other['c']
   if b==bb and c==cc:
    assert first['radsign']==other['radsign']
    continue
   assert b!=bb
   val=-(c-cc)/(b-bb)
   assert val*val+b*val+c==0
   assert val*val+bb*val+cc==0
   assert ksign(2*val+b)==first['radsign']
   assert ksign(2*val+bb)==other['radsign']
   check_intersect(val.iv(),first['iv']);check_intersect(val.iv(),other['iv'])
   if exact is not None:assert exact==val
   exact=val
  if exact is None:
   # Recognize rational C=4 for readable reporting, without changing search.
   if K(16)+4*first['b']+first['c']==0 and first['iv'][0]<=4<=first['iv'][1]:
    assert ksign(8+first['b'])==first['radsign']
    exact=K(4)
  par=list(range(72));witness=[]
  def root(i):
   while par[i]!=i:par[i]=par[par[i]];i=par[i]
   return i
  for item in cl:
   for i,j,D,EoverD in item['edges']:
    Z=isc(ia(ine(first['iv']), (D-EoverD).iv()),F(1,2))
    tau=sign(Z);sigma=sign(ia(Z,(-D).iv()))
    u=2*i+(sigma==1);v=2*j+(tau==1)
    par[root(u)]=root(v);witness.append([i,sigma,j,tau])
  groups={}
  for v in range(72):groups.setdefault(root(v),[]).append([v//2,-1 if v%2==0 else 1])
  rep=[g for g in groups.values()if len(g)>1]
  name=exact.text()if exact is not None else 'root(C^2 + ('+first['b'].text()+')C + ('+first['c'].text()+'), radical sign '+str(first['radsign'])+')'
  records.append({'C':name,'interval':[str(t)for t in first['iv']],'image_size':len(groups),'polynomial_count':len(cl),'collision_equations':len(witness),'groups':rep,'witness':witness})
 minimum=min(x['image_size']for x in records)
 mins=[x for x in records if x['image_size']==minimum]
 # Every noncritical C has 72 outputs, so no default is required once a
 # critical value below 72 has been found. Records are in certified order.
 assert minimum<72
 result={'field_basis':['1','sqrt(3)','sqrt(7)','sqrt(21)'],'A':[a.text()for a in A],'pairs':pairs,'normalized_polynomials':len(polys),'admissible_root_records':len(roots),'distinct_admissible_roots':len(clusters),'minimum':minimum,'least_minimizer':mins[0]['C'],'minimizers':mins,'distribution':{str(s):sum(r['image_size']==s for r in records)for s in sorted(set(r['image_size']for r in records))},'candidates':records}
 path='output/ardc_a2_exact_results.json'
 with open(path,'w')as f:json.dump(result,f,indent=2)
 print(json.dumps({k:v for k,v in result.items()if k!='candidates'},indent=2))
if __name__=='__main__':main()
