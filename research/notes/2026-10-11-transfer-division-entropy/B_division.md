# B: exact attachment obstruction and real elliptic division test

T01, P(x,y)=(x-y)^3+x+y; 2026-10-11, version 1.
**PROVED — B-CP:** CP-O1 has no solution in its stated real scope.
**EXPERIMENTAL — B-X:** one real 3-division scout has n=14 and full image 188.
**OPEN:** the unbounded same-set power-saving target.

## B1. Recovered equations and the correct curve

The controlling finite question is CP-O1 in
[the 2026-10-06 checkpoint](../2026-10-06-changed-collision-pattern/README.md).
It supersedes VG-O1 as the immediate question; CP-R1 resolved VG-O1 by
rigidity, not by producing a nonarithmetic realization of its old pattern.
The new six-scalar seed is a different incidence pattern. Its constants are

    f(t)=64t^3-80t^2+28t-1=0,   0<t<1/12,
    h=sqrt(t), r=h(4t-2),
    a=h(1-4t), b=h(3-4t), d=h(7-12t), A2={-d,-b,-a,a,b,d}.

The nontrivial real same-row sharing conic comes from the actual fiber
coordinates c_+(z,u)=(z-u^3+u)/2, c_-(z,u)=(z-u^3-u)/2.
Equality c_+(z,u)=c_+(z,v) factors as

    (u-v)(u^2+uv+v^2-1)=0.

The line is the trivial component. On the conic, write the row differences
as u=w-v0, v=w+v0; the equation becomes 3w^2+v0^2=1.
This is a smooth geometrically irreducible projective conic, dimension one,
normalization itself, genus zero, with real base point (w,v0)=(0,1).
For example w=2k/(k^2+3), v0=(3-k^2)/(k^2+3) parametrizes it; this
follows by intersecting the line v0=1-kw with the conic. No elliptic
curve is being assigned to a direct output fiber or to this conic.

For a zero-output row set

    q=4w^3-2w, x=q+w=4w^3-w, j=q-w=4w^3-3w,
    y_-=q-v0, y_+=q+v0,  v0=sqrt(1-3w^2)>0.             (B.1)

These four slots are rational functions on the conic (indeed polynomial
in w,v0); no extra cover is required. On the w-line alone the necessary
double cover is v0^2=1-3w^2, branched at two simple zeros, hence genus zero.
The real admissible domain is 0<|w|<1/sqrt(3), w^2 != 1/4. The last
condition excludes equal widths, so all four slots are distinct. There
are no finite poles on this domain. The rational k chart has only complex
denominator zeros and can be completed at its omitted conic point.

Direct expansion, independently of the finite solver, gives

    P(q+w,q+v0)=P(q+w,q-v0)=0,
    P(q-w,q+v0)=P(q-w,q-v0)=4q.                          (B.2)

Indeed for arbitrary center q and 3w^2+v0^2=1 the row values are
2q +/- (4w-8w^3). This also reconstructs the original attachment equations.
CP-O1 requires q different from +/-r, at least two seed scalars among the
four slots, and x different from +/-a.

## B2. Complete finite obstruction, not a sampled search

**PROVED — B-CP.** No real frame satisfying CP-O1 exists.

First, on |w|<=1/sqrt(3), the extrema and endpoints of 4w^3-w give
|x|<=1/(3sqrt(3)). The seed root satisfies 1/32<t<1/12: f is strictly
increasing on that interval, f(1/32)<0, f(1/12)>0. Consequently
b^2=t(3-4t)^2>2/9>1/27 and d>b. Thus a zero row x that belongs to A2
can only be +/-a, which CP-O1 excludes. The zero row is never a reused
seed scalar.

Next, for a fixed y the map x -> P(x,y) has derivative 3(x-y)^2+1>0.
The exact seed identities say

    P(a,-b)=P(a,d)=P(-a,b)=P(-a,-d)=0.

They follow by the seed's two conic frames, or direct reduction by f(t).
If a new zero row used any of +/-b,+/-d as an endpoint y, strict
monotonicity would force x=+/-a. Thus any reused second coordinate is
in {-a,a}. Reusing both of them would give q=0; (B.1) would force w=0
or w^2=1/2, neither admissible. Therefore any putative frame reuses
exactly one endpoint B in {-a,a} and its other first coordinate j=A in
A2, A!=B. Simultaneous negation preserves the zero equation and seed,
so it suffices to take B=a and A=-d,-b,-a,b,d. This covers every role
assignment, not only a guessed slot matching. The condition q!=+/-r
need not even be used in the exclusion.

Put W=w/h, Abar=A/h, Bbar=a/h=1-4t. Equation j=A and the conic give

    C_A(W)=4t W^3-3W-Abar=0,
    Q_A(W)=4t W^2-2t(Bbar-Abar)W+t(Bbar-Abar)^2-1=0.       (B.3)

The cubic f is irreducible over Q because its reduction modulo 3 has
no root. Work in the genuine degree-three field K=Q[t]/(f). For each
of the five Abar values, [the exact certificates](attachments_results.json)
give U_A of degree <=1 and V_A of degree <=2 with

    U_A(W) C_A(W)+V_A(W) Q_A(W)=1 in K[W].               (B.4)

All coefficients are saved as ordered rational coefficients of 1,t,t^2,
in increasing powers of W. They are finite, fully reproducible Bezout
proofs, excluding even complex W at the chosen t; no root isolation or
numerical tolerance is used for this elimination. As a short example,
for Abar=b/h=3-4t the coefficients are

    U=(3t-4t^2)+(-1/4+3t-4t^2)W,
    V=(-2+11t-12t^2)-W/4+(1/4-3t+4t^2)W^2.

Substitution and reduction by f proves (B.4). The other four certificates
are provided in the same explicit format. A separate script, with hardcoded
reduction t^3=1/64-7t/16+5t^2/4 and no solver import, multiplied all five
identities out and verified every coefficient. This is an exact exhaustive
algebraic incompatibility proof. It is stronger than a finite failed scout,
but its scope is precisely this seed and these two-row conic frames.

CP-O1 is thereby resolved by incompatibility. Variable widths do not supply
the stipulated third zero row with two seed scalars. We do not continue
to another specialization of this failed attachment problem.

## B3. One target-relevant elliptic component and all scalar slots

To test the specifically requested torsion/division proposal, use the
already justified sharing specialization z=6,w=0, s=t=+1 from
the 2026-09-30 [elliptic model](../2026-09-30-elliptic-geometry/complex-extensions.md),
EG-C1/C2. This is the second and last specialization of the cycle.

    C: u^3-v^3-u+v=6.

This is a curve of dimension one, not the whole three-dimensional collision
variety. The partial derivatives vanish only at u,v=+/-1/sqrt(3);
their possible real constants are 0,+/-4/(3sqrt(3)), never 6. The three
points at infinity are smooth. Thus its projective plane cubic is smooth,
geometrically irreducible and genus one, already its own normalization.
Its unique real point at infinity [1:1:0] is a base point. A reducible
projective cubic would have intersecting components and a singular point.

The explicit Weierstrass model and inverse maps are

    E: Y^2=X^3-48X-15424,
    X=4+72/(u-v), Y=216(u+v)/(u-v),
    u=(Y+216)/(6(X-4)), v=(Y-216)/(6(X-4)),
    a=(6-u^3+u)/2=(-v^3+v)/2, b=a-u, e=a-v.             (B.5)

Their identities are P(a,b)=6 and P(a,e)=0. The discriminant is
-2^16 3^8 239 !=0. At X=4 the right side is -15552, so every finite
real point admits (B.5). The only omitted real point is O. Over C the
three points at infinity of C map to O and U_+/-=(4,+/-72sqrt(-3)).
Every scalar slot is a rational function on E. There is no necessary
further cover; its genus remains one. All three slots have pole order
three at each of these three points, so each has degree nine.

These assertions were checked by expanding
(u-v)(3(u+v)^2+(u-v)^2-4)=24, substituting into E, and substituting
(B.5) back. Poles are charged rather than treated as usable inputs.

## B4. Actual real torsion and a genuine division set

**PROVED — B-DIV.** Let alpha be the unique root in (40,41) of

    g(T)=T^4-96T^2-61696T-768,
    beta=+sqrt(alpha^3-48alpha-15424), S=(alpha,beta), Q=(40,216).

Then

    H_3=E(R)[3]={O,S,-S},
    R0=[3]Q=(196168,86884488),
    D_3=[3]^(-1)(R0) intersect E(R)={Q,Q+S,Q-S}.          (B.6)

Here R0 is an elliptic point, not the real number zero. It is not O, so
the torsion and division sets are disjoint. No nine-complex-point count
is used as a real input count.

For a direct count, the cubic f_E(X)=X^3-48X-15424 has one real zero e0:
both its extrema at +/-4 are negative. The derivative g'=4f_E implies
g decreases until e0 and increases thereafter. Moreover
g(e0)=-(3e0^2-48)^2/3<0; hence it has two real roots, of which just the
larger has f_E>0. Evaluating g at 40 and 41 locates the larger root.
The other cannot be the X-coordinate of a real point. The doubling
condition [2]S=-S is precisely 3g(alpha)=0, with beta!=0. These facts
give exactly two finite real 3-torsion points and O. Any solution of
[3]R=R0 differs from Q by H_3, proving the entire real division set.
Chord/tangent computations verify the displayed R0 exactly.

Algebraic complexity is also certified. Modulo the one preselected prime
5, g=T^4+4T^2+4T+2 has no linear or monic quadratic factor (five and
25 exhaustive checks). It is irreducible. In F_5[T]/g the radicand
T^3+2T+1 has power 312 equal to -1, so is nonsquare. These reductions
prove that L=Q(alpha,beta) is a field of degree eight. The reduction is
separable, and the radicand is a unit; a square in the characteristic-zero
field would reduce to a square in this residue field. The chosen real
embedding gives alpha in (40,41) and beta>0. All group operations and
slots lie in L. Bounded root discriminant, a totally real splitting field
or one fixed number field for all possible m is not needed for this
direct finite cardinality computation.

Only m=3 was executed, within the allowed set {3,4,6,8}. No negative
result triggered an enlargement to another m or another curve.

## B5. Attachment versus group transport

**PROVED — B-MAP.** A point translation does preserve membership in E and
the two identities in (B.5); it does not give an identity reusing a scalar
slot. All three slots have the same pole support {O,U_+,U_-}, with O its
unique real point. If for a nonzero real T any slot_i(R+T) identically
equaled slot_j(R), this support would have to be invariant under translation
by T. Its unique real point would have to be fixed, forcing T=O.
Thus neither translation by Q nor by a nonzero member of H_3 is the
missing repeatable slot attachment. Incidental finite agreements are not
excluded by this pole argument.

Likewise an identity slot_i composed with an isogeny = slot_j on this
curve would have degree 9 deg(isogeny)=9; it cannot use an isogeny of
degree greater than one. This tests an explicit slot-reuse identity,
not all conceivable isogeny correspondences. Negation gives the exact
involutive relation

    (a,b,e)(-R)=(3-a(R),3-e(R),3-b(R)),
    P(3-x,3-y)=6-P(x,y).                                  (B.7)

The curve has both nonzero short coefficients and j neither 0 nor 1728,
so its origin-preserving geometric automorphisms are +/-1: the short-model
scalings must satisfy lambda^4=lambda^6=1. This reflection has order two;
it does not generate growing attachment fibers.

None of the hypotheses of the frozen global elliptic pole obstruction
has changed. Translating a torsor, restricting to real torsion, and passing
to algebraic division points do not remove the mixed poles or provide
a meromorphic identity on E x E. The earlier finite-grid bounds retain
their stated degree and multiplicity hypotheses. Our conic test is outside
the elliptic component but has its own exact obstruction B-CP.

## B6. Scalar carrier, full image and complete graph audit

Define the one scout carrier

    T=(H_3 union D_3) minus {O},
    A=union_(R in T) {a(R),b(R),e(R)}.                    (B.8)

There are five real finite parameter points and no affine pole. Exact
deduplication in the degree-eight field gives 14 scalars from 15 slots.
The maps (B.5) recover u,v from their triple, so triples themselves have
no hidden parameter identification. Every saved input and output is
represented uniquely in the basis 1,alpha,alpha^2,alpha^3,beta,alpha beta,
alpha^2 beta,alpha^3 beta. Nonzero basis vectors are nonzero in the chosen
real embedding; coefficient equality certifies actual real equality.

| Quantity | Exact result |
|---|---:|
| Distinct scalars n | 14 |
| All ordered pairs, including diagonals and reversals | 196 |
| Full image | 188 |
| Complete fiber histogram (size:number of outputs) | 1:186, 5:2 |
| Singleton-pair fraction | 186/196 = 93/98 |
| Prescribed pairs at outputs 0 and 6 | 10 |
| Certified collision components, including isolates | 186 components of size 1; 2 of size 5 |

The certified graph joins all pairs with the same exact output. Thus in
this finite case its components are actual full fibers; the prescribed
two-fiber graph happens to have the same components. The pair partition,
every value, and every pair representative are in [the saved result](elliptic_results.json).
No asymptotic conclusion is extrapolated from this table. More generally,
two fixed output fibers can prescribe at most 2n real pairs, since for
each second coordinate an output fixes at most one first coordinate.
That certificate leaves at least n^2-2n pairs, even if a growing division
set could be evaluated. Additional full-fiber collisions would need proof.

## B7. Ledger, audit and exact scope

| Cost | Actual charge |
|---|---|
| Inputs and growth | Exactly 14 in one scout; no asymptotic input rate asserted |
| Thinning, both coordinates | O removed before projection; five usable parameters; all 14^2 scalar pairs enumerated |
| Slot multiplicities | 15 slots -> 14 distinct scalars; all duplicates identified |
| Field, discriminant, regulator | Degree 8; no tower or unit carrier, so no discriminant/regulator density argument |
| Denominators/heights | Exact rational basis coefficients saved; separation paid in C |
| Splitting/local moduli | None in construction; prime 5 only certifies field arithmetic |
| Archimedean/domain/poles | Chosen real root; O removed; X=4 impossible on finite real locus |
| Covers/branches | No extra cover; positive beta chosen, negative included explicitly |
| Carries and ratios | Inapplicable: no digital or ratio encoding |
| Exceptional pairs | All 186 singleton pairs retained; no discarded cross-pairs |
| Rate conclusion | No b<2a established; finite reduction is constant only |

Discovery used five exact polynomial gcds, then one full elliptic square.
The identities and geometry above were reviewed separately from discovery.
The script evaluated the full square by both difference-cube and expanded
cubic formulas. [A separate implementation](audit_results.py) imported
neither solver nor field classes: it checked the saved Bezout certificates
by coefficient multiplication and re-evaluated every saved square cell
using hardcoded eight-basis multiplication. All checks passed.

Claim records B-CP, B-DIV and B-MAP are **PROVED** in their displayed
quantifiers and scope, using the identified seed and elliptic companion
plus elementary exact algebra; audit is internal by the same agent in
separate derivation/certificate passes, not independent external review.
B-X is **EXPERIMENTAL, exact and exhaustive** for this one finite carrier.
The local obstruction is not a theorem about all attachments, all torsors,
all finite real sets, or T01. Earlier reports remain unchanged.
