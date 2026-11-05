# Exact elliptic model, complex multiplication, and real descent

T01 / elliptic geometry, 2026-09-30 v1. Fixed target
\(P(x,y)=(x-y)^3+x+y\). This companion is authorized offline symbolic
research. It contains no full-square enumeration, external literature
search, rank computation, or claim of novelty.

The auxiliary sharing curve is
\[
C_{s,c}:\quad u^3-v^3-s(u-v)=c.                 \tag{1}
\]
For the target's same-first-coordinate sharing, s=1 and c=z−w:
\(x_z(u)=x_w(v)\). The parameter s records the exact algebraic family;
s=0 examples below are not substitutes for the fixed T01 problem.

## EG-C1. Exact Weierstrass model and special invariants

### Meaning

The same-sign sharing curve has an explicit real elliptic model away
from its singular parameters. Its special complex automorphisms can be
located exactly; merely recognizing an elliptic curve supplies no scalar
coverage estimate.

### Statement

**PROVED.** Suppose c is nonzero and
\(16s^3-27c^2\ne0\), in characteristic zero. Set
\[
d=u-v,\quad w=u+v,\quad X=12c/d,\quad Y=36cw/d.
\]
Then
\[
Y^2=X^3+12sX^2-432c^2.                        \tag{2}
\]
After \(x=X+4s,y=Y\), the short Weierstrass model is
\[
E_{s,c}:\quad y^2=x^3-48s^2x+128s^3-432c^2.   \tag{3}
\]
Its discriminant and j invariant are
\[
\Delta=2^{12}3^6c^2(16s^3-27c^2),\qquad
j=\frac{4096s^6}{c^2(16s^3-27c^2)}.           \tag{4}
\]
For real s,c with c nonzero, every finite real point of E has x≠4s,
and the inverse is
\[
d=\frac{12c}{x-4s},\qquad
w=\frac{y}{3(x-4s)},\qquad
u=\frac{w+d}{2},\quad v=\frac{w-d}{2}.        \tag{5}
\]
Thus the affine real sharing curve corresponds exactly to the finite
real points of E. Its missing real projective point corresponds to the
Weierstrass identity O.

For s=1, there is no smooth member with j=0. The j=1728 members are
exactly
\[
c=\pm\frac{2\sqrt6}{9},\qquad
E:\ y^2=x^3-48x.                              \tag{6}
\]
No rational c satisfies (6). For real c in the nonsingular range, the
possible j values are precisely \((-\infty,0)\cup[1728,\infty)\).
For s=0 and c nonzero the model instead has j=0.

### Proof

Since c≠0, equation (1) forces d≠0. Direct expansion gives
\[
d(3w^2+d^2-4s)=4c.
\]
Substituting d=12c/X and multiplying the resulting expression for w²
by 9X² gives (2); shifting X=x−4s gives (3). In the notation
\(y^2=x^3+Ax+B\), here A=−48s² and B=128s³−432c². Expanding yields
\[
4A^3+27B^2=2^8 3^6c^2(27c^2-16s^3).
\]
The definitions \(\Delta=-16(4A^3+27B^2)\),
\(c_4=-48A\), and \(j=c_4^3/\Delta\) prove (4).
The assumed nonvanishing discriminant makes the Weierstrass cubic smooth.

At x=4s the right side of (3) is −432c², so this coordinate is impossible
for a real finite point. Equations (5) are inverse substitutions and
recover (1). At infinity, the original projective cubic has u³=v³;
its unique real point is [1:1:0]. The projective birational map sends it
to O. Over the complex numbers the other two points at infinity correspond
to X=0,Y=±12c√−3 in (2); they must not be silently included in the
affine inverse (5).

For a smooth short model, j=0 precisely when A=0, so here s=0. The
condition j=1728 is B=0, giving c²=8s³/27. For s=1 this is (6).
It is not a rational square: the prime exponents of 8/27 include odd
exponents at both 2 and 3. Finally, writing t=c²>0 gives
\(j=4096/[t(16-27t)]\). On 0<t<16/27 the denominator has maximum
64/27, attained at t=8/27, so j≥1728. On t>16/27, j ranges continuously
from negative infinity to zero, without reaching zero. This proves the
real range assertion.

### Why it matters and scope

The fixed cubic admits a genuine real j=1728 sharing member over a real
quadratic coefficient field. It has no j=0 sharing member with s=1.
These statements concern only the specified special j values. They are
not a classification of every possible CM specialization, and they make
no rank assertion. Singular parameters c=0 and 27c²=16s³ require the
separate singular-curve analysis; none is called elliptic here.

## EG-C2. Explicit torsion and an infinite-order rational scout

### Meaning

One can feed exact elliptic points into a reuse chart without guessing
their arithmetic status. The following examples separate finite torsion
orbits from an explicitly certified infinite orbit.

### Statement

**PROVED.** At s=0,c=1, the point (12,36) on
\(y^2=x^3-432\) has order three. On the j=1728 model (6), the three
nonidentity real two-torsion points are
\[
(0,0),\quad(4\sqrt3,0),\quad(-4\sqrt3,0).
\]
These are explicit torsion points, not claims describing all torsion over
all number fields.

For the target-relevant rational specialization s=1,c=6,
\[
E:\ y^2=x^3-48x-15424,\qquad R=(40,216),       \tag{7}
\]
the point R has infinite order. It corresponds to (u,v)=(2,0).
The second multiple is
\[
2R=(41,-227),\quad
u=-11/222,\quad v=-443/222.                    \tag{8}
\]
For any finite real point of this curve, its sharing lift at outputs
z=6,w=0 is exactly
\[
X=x-4,\quad d=72/X,\quad w_*=y/(3X),
\quad u=(w_*+d)/2,\quad v=(w_*-d)/2,
\]
\[
a=(6-u^3+u)/2=(-v^3+v)/2,\quad
b=a-u,\quad e=a-v.                            \tag{9}
\]
Thus \(P(a,b)=6\), \(P(a,e)=0\). This is a two-output reuse identity,
not a full-square support bound.

### Proof of the explicit point assertions

For s=0,c=1 the tangent slope at (12,36) is 6. The doubling formula
gives (12,−36), its negative, so the point has exact order three.
The three y=0 points in (6) are distinct and equal their negatives;
each therefore has exact order two.

For (7), 40³−48·40−15424=216². The tangent slope is
\((3\cdot40^2-48)/(2\cdot216)=11\), yielding (8).
Doubling (41,−227) has slope −4995/454, so
\[
x(4R)=\frac{4995^2}{454^2}-82
      =\frac{8048513}{206116}.                 \tag{10}
\]
The prime 227 divides 454 once and does not divide 4995
(4995≡1 modulo 227). Thus \(v_{227}(x(4R))=-2\).
The discriminant from (4) is
\(-2^{16}3^8\cdot239\), so 227 is a good prime.
The elementary local lemma proved next implies that a nonidentity
point with this negative x valuation cannot be torsion. Hence neither
4R nor R is torsion. Formula (5) proves (8) and (9).

### Local lemma used for infinite order

Let \(E:y^2=x^3+Ax+B\) have coefficients in \(\mathbb Z_p\), with
p≥5 and discriminant a p-adic unit. A point T over \(\mathbb Q_p\)
with \(v_p(x(T))<0\) is not torsion.

Here is the formal-log proof, included to avoid an unverified rank or
torsion-table lookup. Good reduction gives the nonsingular cubic its
chord/tangent group law over \(\mathbb Z_p\). At the identity use
\(t=-x/y\), \(w=-1/y\). The curve equation becomes
\[
w=t^3+Atw^2+Bw^3.
\]
The coefficient of w in the defining implicit equation is a unit at
(0,0), so recursive coefficient comparison gives a unique
\(w(t)\in t^3\mathbb Z_p[[t]]\), with w=t³+O(t⁷).
The group law, regular at the identity of the smooth model, gives
\(F(t_1,t_2)\in\mathbb Z_p[[t_1,t_2]]\), with
F=t₁+t₂+terms of degree at least two. Hence p-adic parameters in
p\(\mathbb Z_p\) form a subgroup.

The invariant differential is
\[
\omega=\frac{dx}{2y}
=\frac{tw'(t)-w(t)}{2w(t)}\,dt
=(1+\sum_{n\ge1}a_nt^n)\,dt,\qquad a_n\in\mathbb Z_p.
\]
Its translation invariance can be checked directly from the chord law:
for a fixed point (r,s), put m=(y−s)/(x−r),
\(x'=m^2-x-r\), \(y'=-y+m(x-x')\).
Using y²−s²=(x−r)(x²+xr+r²+A) gives
\[
3x^2+A-2my=(x-r)(2x+r-m^2),
\]
and differentiation yields \(dx'/(2y')=dx/(2y)\).
The identity extends across the finitely many exceptional chord
denominators by regularity.

Integrate the series formally:
\[
\ell(t)=t+\sum_{n\ge1}\frac{a_n}{n+1}t^{n+1}.
\]
It converges for t in p\(\mathbb Z_p\). If \(v_p(t)=r\ge1\), each
term after t has valuation at least
\((n+1)r-v_p(n+1)>r\). Therefore
\(v_p(\ell(t))=r\), so \(\ell(t)\ne0\) for t≠0.
Translation invariance, or differentiating in each variable and using
F(t,0)=t, proves
\(\ell(F(t_1,t_2))=\ell(t_1)+\ell(t_2)\).
A finite-order nonzero parameter would imply
\(n\ell(t)=0\) in characteristic zero, a contradiction.

Finally, if \(v_p(x)=-a<0\), the x³ term strictly dominates Ax and B.
The equation gives \(2v_p(y)=-3a\), so a=2r and
\(v_p(t)=v_p(x)-v_p(y)=r\ge1\). Such a point lies in the just-proved
torsion-free identity subgroup. This proves the lemma and completes
the infinite-order certificate.

### Why it matters and scope

The point R provides an exact infinite sequence for a bounded scout.
No assertion about the rank of E, its entire rational group, or CM status
is needed. Its j invariant is −256/2151; no CM classification is asserted.
Equation (9) still selects only two output fibers. For any real scalar
set A, each fixed output has at most |A| pairs, since for each y the map
\(x\mapsto(x-y)^3+x+y\) is strictly increasing. Thus two fixed outputs
can select at most 2|A| pairs, regardless of how many elliptic points
were used to describe them. Infinite order alone cannot solve the
Cartesian coverage obligation.

## EG-C3. What complex multiplication and real isogenies preserve

### Meaning

Extra complex endomorphisms are exact symmetries of an elliptic curve.
They need not act on its real points, and they do not automatically act
on one real scalar carrier for the cubic.

### Statement and proof

**PROVED.** On the j=1728 model (6),
\[
\iota(x,y)=(-x,iy)
\]
preserves the curve and fixes O. It satisfies \(\iota^2=[-1]\).
For a finite real point, its image is real exactly when y=0. Thus its
real-to-real locus consists precisely of the three displayed two-torsion
points and O. This follows immediately from the displayed formula and
the cubic factorization. It supplies the explicit extra endomorphism
corresponding to multiplication by i; no general CM classification is
used.

At s=0 and real c≠0, the j=0 model has the extra automorphism
\((x,y)\mapsto(\zeta_3x,y)\). For a finite real point its image can
be real only if x=0, but then y²=−432c²<0. Consequently only O remains
real under that automorphism. This j=0 case is auxiliary, not the s=1
target sharing curve.

More generally, on any elliptic curve over the reals let α be a complex
endomorphism distinct from its conjugate \(\bar\alpha\). A real point
T with α(T) real satisfies
\[
(\alpha-\bar\alpha)(T)=O.
\]
The nonzero endomorphism \(\alpha-\bar\alpha\) is nonconstant and has
a finite fiber over O, so the real-to-real locus is finite. Finiteness
here is simply the finite-fiber property of a nonconstant morphism of
smooth projective curves: a nonconstant rational coordinate function
cannot take a fixed value on an infinite closed fiber without being
constant. The bound depends on the chosen map; no uniform assertion
for a growing sequence of endomorphisms is inferred.

A real isogeny does map real points to real points, and has finite
fibers. This fact preserves point identities and incurs a controlled
point-projection multiplicity. It does **not** state an identity for
\(P\) evaluated on independently chosen scalar coordinates of those
points. Such an identity, same-set membership, all cross-pairs, and
scalar fiber multiplicities remain separate obligations.

### Why it matters and scope

The special CM member is real and valid, but its extra order-four
automorphism does not provide arbitrarily many real actions on its
nontorsion real points. Real isogenies are not ruled out as tools.
What is absent is a scalar Cartesian transport theorem, not elliptic
point transport. No negative conclusion is drawn about every conceivable
isogeny-based construction.

## EG-C4. Exact embedding, conjugation, and trace transport

### Meaning

A real field embedding is a valid way to transport an already established
algebraic construction. Taking real parts, traces, or norms is different:
these operations usually introduce cross terms in the cubic.

### Statements

**PROVED: embedding transport.** If K has an embedding
\(\sigma:K\hookrightarrow\mathbb R\), and B is any finite subset
of K, then
\[
P(\sigma B,\sigma B)=\sigma(P(B,B)).
\]
All scalar, pair, and output cardinalities are preserved, because σ is
an injective field homomorphism and P has rational coefficients.
Hence a full-support construction over one such K would genuinely
descend to the same real scalar set. This statement assumes that
construction; it does not produce one. A CM field is totally imaginary
and has no real embedding. Any field containing it has no real embedding
either, by restriction. This does not prevent a CM elliptic equation
or selected points from being defined over a smaller real field.

**PROVED: reality of the complete sharing triple.** For real outputs z,w,
write a shared-endpoint chart as
\[
a=x_z(u)=x_w(v),\qquad b=a-u,\qquad e=a-v.
\]
All three required scalars a,b,e are real if and only if u,v are real.
The forward implication follows from u=a−b,v=a−e; the reverse follows
from the real-coefficient coordinate formulas. Requiring only one scalar
function of a complex point to be real is therefore insufficient.

**PROVED: normalized trace correction.** For a finite characteristic-zero
extension K/k of degree n, put \(T=\operatorname{Tr}_{K/k}/n\).
For a,b in K write
\[
\alpha=T(a),\quad\beta=T(b),\quad
\delta=\alpha-\beta,\quad
\eta=(a-b)-\delta,\quad T(\eta)=0.
\]
Then the exact identity is
\[
T(P(a,b))=P(\alpha,\beta)+3\delta T(\eta^2)+T(\eta^3).       \tag{11}
\]
Expanding \((\delta+\eta)^3\) and using T(η)=0 proves (11).
The extra terms depend on the selected pair. A trace argument must
control their complete support and their correlation with traced inputs.

For a quadratic extension, the unnormalized identity is especially simple.
Let d=a−b. Since
\(\operatorname{Tr}(d^3)=\operatorname{Tr}(d)^3-
3\operatorname{Tr}(d)\operatorname{Norm}(d)\), one has
\[
P(\operatorname{Tr}a,\operatorname{Tr}b)
=\operatorname{Tr}P(a,b)+3\operatorname{Tr}(d)\operatorname{Norm}(d).
                                                               \tag{12}
\]
This follows by expanding the two conjugates of d. It shows exactly
where the tempting norm/trace transfer fails to commute.

For complex conjugation, write a−b=r+it. Then
\[
\operatorname{Re}P(a,b)
=P(\operatorname{Re}a,\operatorname{Re}b)-3rt^2.                \tag{13}
\]
This is just the real part of \((r+it)^3\). If a complex scalar set
B has at least two distinct real parts, equality without the correction
term holds on every pair in B² **if and only if all elements of B have
the same imaginary part**. Indeed (13) requires
\((\operatorname{Re}a-\operatorname{Re}b)
(\operatorname{Im}a-\operatorname{Im}b)^2=0\).
Choose two elements with unequal real parts: their imaginary parts agree.
Any third element differs in real part from at least one of them and
therefore has that same imaginary part. The converse is immediate.
The case of one real part has a one-point real projection and is harmless.

Norm transport also does not preserve this cubic. An exact counterexample
over \(\mathbb Q(i)\) is a=i,b=0:
\[
\operatorname{Norm}(P(i,0))=0,
\qquad P(\operatorname{Norm}(i),\operatorname{Norm}(0))=P(1,0)=2.
\]
It is a failure of that proposed identity, not an impossibility theorem
for all norm-based constructions.

### Why it matters and scope

Equation (13) completely classifies pairwise commutation with real-part
projection on a same-set square: except for a collapsed real projection,
it is merely a common imaginary translation. Such a translation introduces
no new cubic-difference mechanism. More general trace methods remain
possible only with an explicit bound on the correction terms in (11)
and an exact scalar/pair multiplicity ledger. Those controls are OPEN.

## Quantitative ledger and audit boundary

| Proposed tool | Exact positive fact | Missing requirement for T01 |
|---|---|---|
| Weierstrass transformation | Explicit birational map; real affine inverse has no omitted finite real points | Growing scalar reuse and complete Cartesian output support |
| Infinite-order rational point | The c=6 point is certified nontorsion | Its two fixed outputs cover at most 2N real pairs |
| Special CM automorphism | Exact extra automorphism, with explicitly finite real-to-real locus | No growing real carrier action is supplied |
| Real isogeny | Real point transport with finite point fibers | An identity for scalar P and counts of every cross-pair |
| Real field embedding | All existing same-set cardinalities and polynomial identities survive | A compressed full-square algebraic carrier over that field |
| Trace/real part | Exact correction formulas (11)–(13) | Full correction support and projection multiplicities |
| Norm | Concrete failure of the naive commuting identity | A different exact transport identity and rate ledger |

No input thinning, positive exponent gap, arithmetic tower, prime-splitting
condition, or regulator estimate is used. The only number field in the
explicit target CM specialization is real quadratic in its sharing
parameter, with an additional imaginary unit needed for the extra
automorphism. Neither field degree nor algebraic point count is counted
as real scalar input growth.

All claims EG-C1–EG-C4 have track T01, the fixed plus-sign cubic, and
version/date 2026-09-30 v1. Their quantifiers and hypotheses are in the
statements above. Evidence is the displayed exact symbolic argument;
the elliptic chord/tangent group law and its smooth good-reduction model
are the foundational elliptic-curve inputs. The local formal-log proof
is included, rather than a rank-table or Nagell–Lutz lookup. No external
novelty or literature assessment is attempted.

This subtask performed zero full-square evaluations and no computer
algebra search. Arithmetic and substitutions were derived and inspected
symbolically. The coordinating task may separately scout the supplied
point prefixes and audit these proofs; that work is not claimed as
already performed here. Historical files and prior run data are unchanged.
The fixed T01 power-saving target remains **OPEN**.
