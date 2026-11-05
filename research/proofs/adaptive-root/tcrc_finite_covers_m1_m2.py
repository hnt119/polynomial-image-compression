"""Exact finite root-cover certificates; Python standard library only.

All affine-cover searches use Fraction arithmetic. The degree-four arithmetic
is the basis 1,sqrt(3),sqrt(7),sqrt(21), whose independence is proved in the note.
Run from any working directory: no input or output files are needed.
"""
from fractions import Fraction as F
from itertools import combinations, permutations


def rational_Q_image(A):
    return {x*x+x*y+y*y for x in A for y in A}


def affine_masks(S, R):
    """All distinct hit sets of maps meeting R in at least two points.

    Every such affine map is determined by two distinct matched source and
    target points. Maps hitting fewer points are dominated by one of these.
    """
    S, R = sorted(S), sorted(R)
    index = {x: i for i, x in enumerate(R)}
    candidates = {}
    for s1, s2 in combinations(S, 2):
        for r1, r2 in permutations(R, 2):
            alpha = (r2-r1)/(s2-s1)
            beta = r1-alpha*s1
            hit = {alpha*s+beta for s in S} & set(R)
            mask = sum(1 << index[x] for x in hit)
            candidates.setdefault(mask, (alpha, beta))
    return candidates


def cover_audit(S, R):
    candidates = affine_masks(S, R)
    # Dominated hit sets cannot improve any union of hit sets.
    masks = [m for m in candidates
             if not any(m != n and m & n == m for n in candidates)]
    maxima = {}
    maxima[1] = max(m.bit_count() for m in masks)
    maxima[2] = max((a | b).bit_count() for a, b in combinations(masks, 2))
    maxima[3] = max((a | b | c).bit_count()
                    for a, b, c in combinations(masks, 3))
    return len(candidates), len(masks), maxima


class K:
    """Exact Q(sqrt(3),sqrt(7)) arithmetic; no numerical comparison."""
    def __init__(self, a=0):
        self.v = a.v if isinstance(a, K) else (
            tuple(map(F, a)) if isinstance(a, (tuple, list))
            else (F(a), F(0), F(0), F(0)))
    def __add__(a, b):
        b=K(b); return K(tuple(x+y for x,y in zip(a.v,b.v)))
    __radd__=__add__
    def __neg__(a): return K(tuple(-x for x in a.v))
    def __sub__(a,b): return a+-K(b)
    def __rsub__(a,b): return K(b)+-a
    def __mul__(a,b):
        b=K(b); out=[F(0)]*4
        for i,x in enumerate(a.v):
            for j,y in enumerate(b.v):
                common=i&j
                out[i^j]+=x*y*(3 if common&1 else 1)*(7 if common&2 else 1)
        return K(out)
    __rmul__=__mul__
    def __hash__(a): return hash(a.v)
    def __eq__(a,b): return a.v==K(b).v


def signed(values):
    return {z for v in values for z in (v,-v)}


def K_Q_image(A):
    return {x*x+x*y+y*y for x in A for y in A}


def union_images(S, maps):
    return {alpha*s+beta for alpha,beta in maps for s in S}


def main():
    A1=set(map(F,[-2,-1,1,2])); S1=rational_Q_image(A1)
    assert S1==set(map(F,[1,3,4,7,12]))

    # Certified optimizer C=5/2; two exact, non-vacuous affine images.
    R1={t/2 for t in rational_Q_image(set(map(F,[-3,-1,1,3])))}
    assert R1=={F(t,2) for t in [1,3,7,9,13,27]}
    maps1=[(F(-1),F(15,2)),(F(3),F(-15,2))]
    hits1=[R1 & union_images(S1,[ell]) for ell in maps1]
    assert list(map(len,hits1))==[4,3] and set.union(*hits1)==R1
    assert R1 | {F(3,2),F(9,2),F(7,2),F(21,2)} == R1|{F(21,2)}
    assert 16-(2**2+1+1)+len(R1|{F(21,2)})==17
    count1=cover_audit(S1,R1)
    assert count1[2][1]==4 and count1[2][2]==6

    # Comparison C=3: largest class {-2,1}, root set A1, one copy.
    assert {F(3)+a for a in [F(-2),F(1)]}=={F(1),F(4)}
    W3=S1|set(map(F,[2,6,5,15])); assert len(W3)==9
    assert 16-(4+1+1)+len(W3)==19

    # Comparison C=17/8: a larger root class, but three affine maps fail.
    Aroot=set(map(F,[-5,-3,-1,1,3,5])); T=rational_Q_image(Aroot)
    assert T==set(map(F,[1,3,7,9,13,19,21,25,27,31,49,75]))
    assert {F(17,8)+a for a in [F(-2),F(-1),F(1)]}=={F(1,8),F(9,8),F(25,8)}
    count17=cover_audit(S1,T)
    assert count17[2]=={1:5,2:8,3:11},count17
    three=[(F(1),F(0)),(F(6),F(3)),(F(6),F(7))]
    assert T-union_images(S1,three)=={F(19)}
    four=three+[(F(3),F(-2))]
    assert T<=union_images(S1,four)
    assert 16-(3**2+1)+len({x/8 for x in T}|{F(33,8),F(99,8)})==20

    # Actual m=2 input; two different exact one-copy comparison covers.
    r3=K((0,1,0,0)); r7=K((0,0,1,0)); r21=r3*r7
    A2=signed([K(1),r3,r7,K(3)]); S2=K_Q_image(A2)
    assert len(A2)==8 and len(S2)==17
    U4=signed([K(1),r3,r7]); R4=K_Q_image(U4)
    assert len(R4)==11 and R4<=S2
    assert {K(4)+a for a in [K(-3),K(-1),K(3)]}=={u*u for u in [K(1),r3,r7]}
    # Second square class represented by gamma=1/2, roots sqrt(7) +/-1.
    V4=signed([r7-K(1),r7+K(1)])
    W4=R4|{F(1,2)*t for t in K_Q_image(V4)}
    for gamma in [K(5),K(4)-r3,K(4)+r3]:
        W4|={gamma,3*gamma}
    assert len(W4)==20
    assert 64-(3**2+2**2+1+1+1)+len(W4)==68

    U6=signed([r3,r7,K(3)]); R6=K_Q_image(U6)
    assert len(R6)==11 and R6<=S2
    assert {K(6)+a for a in [K(-3),K(1),K(3)]}=={u*u for u in [r3,r7,K(3)]}
    W6=set(R6)
    for gamma in [K(5),K(6)-r3,K(6)+r3,K(6)-r7,K(6)+r7]:
        W6|={gamma,3*gamma}
    assert len(W6)==21
    assert 64-(3**2+1+1+1+1+1)+len(W6)==71
    print('m=1, C=5/2:',count1,'two-map hit sizes',list(map(len,hits1)))
    print('m=1, C=17/8:',count17,'three-map miss {19}/8; four maps cover')
    print('m=2: |S|=17, |R4|=|R6|=11, both identity covers')
    print('Full branch image cardinalities: C=5/2:17; C=3:19; C=17/8:20; m2 C=4:68; C=6:71')
    print('All assertions passed exactly.')


if __name__=='__main__':
    main()
