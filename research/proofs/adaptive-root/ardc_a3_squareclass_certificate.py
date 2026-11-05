"""Exact square-class ledger for 3+A3 in its actual degree-64 field.

Only Fraction, integer square roots, and a recursively proved quadratic-tower
square test are used. No external packages or numerical algebra are used.
"""
from ardc_a3_exact_certificate import K, F, ksign
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
