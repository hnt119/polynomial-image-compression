"""Exact square-class ledger and field-degree certificate for the known A3 lift.

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


"""Exact square-class ledger for 3+A3 in its actual degree-64 field.

Only Fraction, integer square roots, and a recursively proved quadratic-tower
square test are used. No external packages or numerical algebra are used.
"""
from functools import lru_cache
from math import isqrt
from itertools import combinations_with_replacement
import json, time
from pathlib import Path

D=[K(p) for p in (2,3,5,7,13)]+[K(4)+K({2:1})]
def key(x):return tuple(sorted(x.v.items()))
def unpack(x):return K(dict(x))
def split(x,l):
    mask=1<<(l-1)
    assert all(i<2*mask for i in x.v)
    return K({i:v for i,v in x.v.items() if i<mask}), K({i-mask:v for i,v in x.v.items() if i>=mask})
def join(a,b,l):return a+K({i+(1<<(l-1)):v for i,v in b.v.items()})

@lru_cache(None)
def inverse(xx,l):
    x=unpack(xx)
    assert x
    if l==0:return key(K(1/x.v[0]))
    a,b=split(x,l)
    ni=unpack(inverse(key(a*a-D[l-1]*b*b),l-1))
    z=join(a*ni,-b*ni,l)
    assert z*x==1
    return key(z)

TRACE={}
@lru_cache(None)
def square_root(xx,l):
    """Return one exact root as a coefficient tuple, or None iff no root."""
    x=unpack(xx)
    if not x:return ()
    if l==0:
        q=x.v[0]
        if q<0:return None
        a,b=isqrt(q.numerator),isqrt(q.denominator)
        return key(K(F(a,b))) if a*a==q.numerator and b*b==q.denominator else None
    a,b=split(x,l)
    if not b:
        u=square_root(key(a),l-1)
        if u is not None:return u
        v=square_root(key(a*unpack(inverse(key(D[l-1]),l-1))),l-1)
        if v is not None:return key(join(K(0),unpack(v),l))
        return None
    n=a*a-D[l-1]*b*b
    rt=square_root(key(n),l-1)
    if rt is None:return None
    rt=unpack(rt)
    for v in (rt,-rt):
        u=square_root(key((a+v)/2),l-1)
        if u is None:continue
        u=unpack(u)
        assert u
        w=b*unpack(inverse(key(2*u),l-1))
        z=join(u,w,l)
        assert z*z==x
        return key(z)
    return None

def sq(x):
    z=square_root(key(x),6)
    if z is not None:
        z=unpack(z)
        assert z*z==x
        if ksign(z)<0:z=-z
    return z

def span_certificate(representatives):
    """Exhaustively certify a basis of the generated square-class subgroup."""
    subgroup=[(K(1),[])];basis=[];relations=[]
    negative_basis_tests=0;other_negative_tests=0
    for name,h in representatives:
        negatives=0
        for old,indices in subgroup:
            rt=sq(h*old)
            if rt is not None:
                relations.append({'dependent':name,'basis_product':indices,'square_root':rt.text()})
                other_negative_tests+=negatives
                break
            negatives+=1
        else:
            negative_basis_tests+=negatives
            basis.append(name)
            subgroup +=[(old*h,indices+[name]) for old,indices in subgroup]
    return {'basis':basis,'rank':len(basis),'relations':relations,
            'negative_basis_tests':negative_basis_tests,
            'other_negative_tests':other_negative_tests,
            'positive_dependency_tests':len(relations),
            'degree_over_K3':2**len(basis),'absolute_degree':64*2**len(basis)}

def main():
    start=time.time()
    Path('output').mkdir(exist_ok=True)
    alpha=K({32:1});r2=K({1:1});r3=K({2:1});r5=K({4:1});r7=K({8:1});r13=K({16:1})
    beta=r13*(4-r3)*alpha/13
    gamma=(K({9:1})+r2)/2;delta=(K({9:1})-r2)/2
    pos=[K(1),r3,r5,r7,alpha,beta,gamma,delta]
    names=['1','sqrt(3)','sqrt(5)','sqrt(7)','sqrt(4+sqrt(3))','sqrt(4-sqrt(3))','sqrt(4+sqrt(7))','sqrt(4-sqrt(7))']
    A=[];labels=[]
    for x,name in zip(pos,names):
        A.extend([x,-x]);labels.extend([name,'-'+name])
    h=[3+a for a in A]
    classes=[];tests=[]
    for i in range(16):
        for cl in classes:
            j=cl[0];z=sq(h[i]*h[j])
            tests.append({'i':i,'j':j,'is_square':z is not None,'root':None if z is None else z.text()})
            if z is not None:cl.append(i);break
        else:classes.append([i])
    witnesses=[];inside={};inside_occurrences=0
    for cl in classes:
        for i,j in combinations_with_replacement(cl,2):
            z=sq(h[i]*h[j]);assert z is not None
            witnesses.append({'i':i,'j':j,'positive_root':z.text()})
            for sign in (-1,1):
                t=6+A[i]+A[j]+sign*z
                inside.setdefault(key(t),[]).append([i,j,sign])
                inside_occurrences+=1
    # Every different-class pair must fail the complete test, not only the
    # representative comparisons used to build the partition.
    cross_non_squares=0
    for k,cl in enumerate(classes):
        for other in classes[k+1:]:
            for i in cl:
                for j in other:
                    assert sq(h[i]*h[j]) is None
                    cross_non_squares+=1
    sizes=[len(cl) for cl in classes]
    outside=16**2-sum(x*x for x in sizes)
    span=span_certificate([('P3',3+r3),('P7',3+r7),('gamma+',3+gamma),('gamma-',3-gamma),('delta+',3+delta),('delta-',3-delta),('alpha+',3+alpha),('alpha-',3-alpha),('beta+',3+beta),('beta-',3-beta)])
    assert span['rank']==8 and span['negative_basis_tests']==255
    data={'field':'Q(sqrt(2),sqrt(3),sqrt(5),sqrt(7),sqrt(13),sqrt(4+sqrt(3)))','field_degree':64,'A_labels':labels,'A_coefficients':[x.text() for x in A],'classes':[[labels[i] for i in cl] for cl in classes],'class_indices':classes,'class_sizes':sizes,'sum_class_size_squares':sum(x*x for x in sizes),'largest_class_fraction':str(F(max(sizes),16)),'inside_branch_occurrences':inside_occurrences,'inside_distinct_outputs':len(inside),'outside_distinct_outputs':outside,'total_outputs':outside+len(inside),'cross_non_square_tests':cross_non_squares,'representative_tests':tests,'within_class_square_witnesses':witnesses,'inside_outputs':[{'value':unpack(t).text(),'representations':rs} for t,rs in inside.items()],'square_class_span':span,'memoized_square_tests':square_root.cache_info()._asdict(),'elapsed_seconds':time.time()-start}
    assert outside+len(inside)==269
    with open('output/ardc_a3_squareclass_results.json','w') as f:json.dump(data,f,indent=2)
    print(json.dumps({k:v for k,v in data.items() if k not in ('representative_tests','within_class_square_witnesses','inside_outputs','A_coefficients')},indent=2))

if __name__=='__main__':main()
