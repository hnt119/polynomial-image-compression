# Elliptic addition: global identities and finite-grid costs

T01 / elliptic geometry cycle, 2026-09-30 v1.
The fixed polynomial is \(P(x,y)=(x-y)^3+x+y\).
This companion contains new offline symbolic proofs, with **zero carrier
evaluations and zero numerical searches**. No external source or novelty
claim is used. EG-B1–B6, including the finite-cover extension under EG-B2,
have passed independent internal lead audit.

The main distinction is between an identity on an elliptic surface and
equalities on a finite parameter set. The global identity fails. More
quantitatively, bounded meromorphic degree allows only linearly many
successful labels on a balanced grid. Growing degrees, noninjective
projection, and the number of charts must therefore be charged explicitly.

For example, an elliptic parameter set may have \(M\) points while its
coordinate projection contains only \(N<M\) scalars. Counting failures
on \(M^2\) labels is then different from counting uncovered scalar pairs
in \(A^2\). Both counts are kept separate below.

## 1. EG-B1 — the same-coordinate sum and difference identities fail

### Meaning

An elliptic sum is symmetric in its two inputs, whereas the cubic changes
when its scalar arguments are exchanged. An elliptic difference is zero
on the diagonal, whereas the cubic takes the varying value \(2x\) there.

### Exact statement — PROVED

Let \(\mathcal E\) be a complex elliptic curve, regarded as a compact
connected complex curve with its holomorphic group law. Let \(f\) be a
nonconstant meromorphic function and \(H\) a meromorphic function.
Neither identity
\[
P(f(R),f(S))=H(R+S),\qquad
P(f(R),f(S))=H(R-S)
\tag{1}
\]
can hold as an identity of meromorphic functions on
\(\mathcal E\times\mathcal E\).

Real algebraic instances are included after complexification.
Finite pointwise equalities are not being excluded by this statement.

### Proof

For the sum identity, exchange \(R,S\) on the common open set where
all values are finite. Subtraction gives
\[
0=P(f(R),f(S))-P(f(S),f(R))
  =2(f(R)-f(S))^3.
\]
Fixing a regular \(S\) forces \(f\) to be constant, a contradiction.

For the difference identity, first check that \(H\) is finite at the
identity point \(O\). Fix any \(R_0\) where \(f\) is regular and let
\(S\) approach \(R_0\). The left side is holomorphic and bounded, whereas
a pole of \(H\) at \(O\) would make \(H(R_0-S)\) unbounded. Thus \(H(O)\)
is finite. Restricting the meromorphic identity to regular diagonal
points now gives
\[
2f(R)=P(f(R),f(R))=H(O),
\]
again a contradiction. This diagonal argument does not substitute an
undefined value at a pole. \(\square\)

### Why it matters

The simplest elliptic group-law mechanism is unavailable even before
same-set completion or input heights are considered.

### Scope

This does not exclude finite coincidences, multiple charts, varying
formulas on different parameter subsets, or a group-law construction
whose output is not a single meromorphic function of \(R\pm S\).
The finite-grid restrictions below are needed for those distinctions.

## 2. Elementary meromorphic counting facts used below

For a nonconstant meromorphic function \(f\) on a compact complex curve,
write \(D_f\) for its pole divisor, \(d_f=\deg D_f\) for the sum of pole
orders, and \(k_f=|\operatorname{supp}D_f|\) for the number of distinct
poles. These are finite and \(1\le k_f\le d_f\).
For a constant meromorphic function, its pole divisor is empty and
the corresponding degree and support count are zero.

A nonzero meromorphic function has equally many zeros and poles, counted
with multiplicity. One direct proof integrates \(dq/q\) after deleting
small coordinate disks around its zeros and poles. The differential is
closed on the remaining compact surface, so the sum of its boundary
integrals is zero; near a point of order \(n\) the integral is \(2\pi i n\).
The signed orders therefore sum to zero. A meromorphic function with no
poles is constant by the maximum principle. Consequently:

- a nonzero meromorphic function with total pole order at most \(D\)
  has at most \(D\) distinct zeros;
- each finite value of a nonconstant \(f\) has at most \(d_f\) preimages;
- the pole degree of a difference is at most the sum of the two pole degrees.

For a nonzero isogeny \(\alpha:\mathcal E_1\to\mathcal E_0\), let
\(a=|\ker\alpha|\). Every fiber has exactly \(a\) points, and pullback
multiplies pole degree by \(a\). Here is the local justification in
characteristic zero. Translation invariance of the group homomorphism
makes its derivative zero everywhere if it is zero anywhere; that would
make the map constant. Thus a nonconstant isogeny is locally unramified.
It is surjective because its image is both open and compact in the
connected target. Every fiber is a translate of its finite kernel.
Local orders are unchanged at each preimage, proving the pullback rule.

These elementary arguments supply the counting facts used in the
following proofs; no theorem about genus, elliptic uniformization,
rational points, or arithmetic heights is imported.

## 3. EG-B2 — mixed group-law poles obstruct every separated polynomial identity

### Meaning

A polynomial in \(f(R)\) and \(g(S)\) can have a pole only when one of
its separate inputs has a pole. A function of \(\alpha(R)+\beta(S)\)
instead has poles on moving relations between both parameters.
These moving poles cannot all occur at the separate input poles.

### Exact statement — PROVED

Let \(\mathcal E_1,\mathcal E_2,\mathcal E_0\) be complex elliptic
curves. Let \(\alpha:\mathcal E_1\to\mathcal E_0\) and
\(\beta:\mathcal E_2\to\mathcal E_0\) be nonzero isogenies, let
\(T\in\mathcal E_0\), and let \(f,g,H\) be meromorphic functions on
their respective curves, with \(H\) nonconstant. For every polynomial
\(Q(X,Y)\in\mathbb C[X,Y]\), the identity
\[
\boxed{Q(f(R),g(S))=H(\alpha(R)+\beta(S)+T)}
\tag{2}
\]
is impossible.

In particular, this excludes \(Q=P\), distinct scalar maps, both signs
of the group operation, fixed translations, and nontrivial isogeny twists.
For \(Q=P\), a constant \(H\) is also impossible if at least one of
\(f,g\) is nonconstant.

### Proof

Choose a pole \(p\) of \(H\). There are only finitely many \(S\) where
\(g\) has a pole, or where
\[
\beta(S)\in p-T-\alpha(\operatorname{supp}D_f).
\]
Choose \(S_0\) outside that finite set. Surjectivity of \(\alpha\) supplies
\(R_0\) with \(\alpha(R_0)=p-\beta(S_0)-T\), and the choice of \(S_0\)
ensures that \(f\) is finite at \(R_0\). Thus the left side of (2) is
holomorphic near \((R_0,S_0)\). The right side has a pole already on the
slice \(S=S_0\), because \(\alpha\) is unramified at \(R_0\).
This contradicts the identity.

If \(H\) is constant and \(f\) is nonconstant, fix a regular \(S_0\).
The polynomial \(P(f(R),g(S_0))\) has a pole of three times the order
of every pole of \(f\), so is not constant. The case of nonconstant
\(g\) follows by fixing \(R\), with leading term \(-g(S)^3\).
\(\square\)

### Finite-cover extension — PROVED

The global conclusion of (2) also holds when the two input curves are
arbitrary smooth connected compact complex curves \(C_1,C_2\), and
\(\alpha:C_1\to\mathcal E_0\), \(\beta:C_2\to\mathcal E_0\)
are nonconstant finite holomorphic maps rather than isogenies.
The functions \(f,g\) are then single-valued meromorphic functions on
the respective covering curves. Ramification is allowed.

Indeed, nonconstant finite maps are surjective, and the preimage of a
finite set is finite. Choose the pole \(p\), the regular point \(S_0\),
and a point \(R_0\) in the required \(\alpha\)-fiber exactly as above.
The left side is holomorphic. If the local multiplicity of \(\alpha\)
at \(R_0\) is \(e\ge1\), a pole of order \(m\ge1\) of \(H\)
pulls back to a pole of order \(em\) on the slice \(S=S_0\).
Thus ramification cannot remove the contradictory pole. \(\square\)

This covers algebraic branch formulas that become globally single-valued
meromorphic functions after independent finite covers of the two input
curves. It does not cover arbitrary pair-dependent branch selections or
merely finite multivalued correspondences. The precise exceptional-row
count in EG-B3 continues to assume the stated unramified isogenies;
it is not asserted for these more general covers.

### Why it matters

This is broader than symmetry or the diagonal calculation. It shows why
the usual elliptic addition formulas, which involve denominators creating
mixed poles, cannot directly yield a polynomial separated-scalar identity
of the required type.

### Scope

Rational functions of both scalar coordinates can have mixed poles and
are not covered as replacements for \(Q\). Nor does this theorem exclude
finite-grid coincidences. A pole of an auxiliary formula is not permission
to discard an uncharged part of the final scalar square.

## 4. EG-B3 — finite grids have only a bounded number of exceptional rows

### Meaning

Failure of a global identity is not enough: a nonzero equation could
still hold at many selected points. Here the number of such points is
controlled by the actual degrees of the functions, and the rows on which
the equation holds identically are counted explicitly.

### Exact statement — PROVED

Use the curves and isogenies in EG-B2, with
\[
a=\deg\alpha,\qquad b=\deg\beta,
\]
and assume \(f,g,H\) are nonconstant, with pole degrees \(d_f,d_g,h\).
Let finite \(X\subset\mathcal E_1\), \(Y\subset\mathcal E_2\) avoid the
poles of \(f,g\), respectively. Let \(L\) count the labels
\((R,S)\in X\times Y\) for which the right side below is finite and
\[
P(f(R),g(S))=H(\alpha(R)+\beta(S)+T).
\tag{3}
\]
Put
\[
B_f=
\begin{cases}
b\lfloor k_f/a\rfloor,& ah=3d_f,\\
0,& ah\ne3d_f,
\end{cases}
\qquad
B_g=
\begin{cases}
a\lfloor k_g/b\rfloor,& bh=3d_g,\\
0,& bh\ne3d_g.
\end{cases}
\]
Then
\[
\boxed{
L\le \min\left\{
|X||Y|,\ 
(3d_f+ah)|Y|+B_f|X|,\ 
(3d_g+bh)|X|+B_g|Y|
\right\}.}
\tag{4}
\]

For untwisted addition or subtraction on one curve,
\[
L\le (3d_f+h)|Y|+d_f|X|.
\tag{5}
\]
For the same scalar map \(f\) on a balanced grid \(X\times X\),
\[
\boxed{L\le (4d+h)|X|,\qquad d=\deg D_f.}
\tag{6}
\]
If \(h\ne3d\), the improved coefficient \(3d+h\) is valid in (6).

### Proof

Fix \(S\in Y\). The left side of (3), as a function of \(R\), has
pole divisor exactly \(3D_f\). Its leading term at a pole of \(f\)
is \(f^3\); the remaining terms have lower pole order. The right side
has pole degree \(ah\). Their difference therefore has pole degree
at most \(3d_f+ah\).

Unless this difference is identically zero, it has at most
\(3d_f+ah\) zeros. Every defined successful label in the row is one
of those zeros. Poles, including any common poles with cancellations,
are not counted as successful finite evaluations.

For an identical row, equality of pole divisors requires \(ah=3d_f\).
Fix one pole \(p\) of \(H\). Every point of
\[
\alpha^{-1}(p-\beta(S)-T)
\]
must then lie in \(\operatorname{supp}D_f\). These preimage sets have
exactly \(a\) points; for different values of \(p-\beta(S)-T\), they
are disjoint. Thus at most \(\lfloor k_f/a\rfloor\) target values have
their full \(\alpha\)-fiber contained in that fixed pole support.
Each allowed target value gives at most \(b\) choices of \(S\).
There are therefore at most \(B_f\) identical rows.

Charge the ordinary zero bound to every row and at most \(|X|\) extra
labels to each identical row. This gives the second expression in (4).
The column argument is identical, using the leading term \(-g^3\),
and gives the third. The full grid is a trivial cap.

For untwisted addition or subtraction, \(a=b=1\) and \(B_f\le k_f\le d_f\).
Taking \(g=f\) and \(Y=X\) proves (5)–(6), including the stated
nonmatching-degree improvement. \(\square\)

### Why it matters

The bound is uniform over the elliptic curves, the selected points, and
the coefficients. It remains valid when the maps and their degrees vary
with the size of the parameter set. Degree growth is visible rather than
hidden in an unspecified constant.

### Scope

This counts defined successful labels. It is not a lower bound on the
whole scalar image. A high-degree \(H\), an isogeny of growing degree,
or many charts can weaken the estimate; the costs are explicit in (4).
The maps are single-valued meromorphic functions on smooth compact curves.
Multivalued algebraic correspondences require their own degree/domain
accounting.

## 5. EG-B4 — the same-set and growing-library degree barriers

### Meaning

Projecting elliptic parameters to scalars may create duplicates. Those
duplicates cannot be ignored when converting a finite-grid bound into
a statement about the actual Cartesian square.

### Exact statement — PROVED

Let \(X\) be a nonempty finite pole-free parameter set for a nonconstant meromorphic
\(f\), let \(A=f(X)\subset\mathbb R\), and put \(M=|X|\), \(N=|A|\),
\(d=\deg D_f\). Let \(H\) be nonconstant of pole degree \(h\).
For either one untwisted rule \(H(R\pm S+T)\), let \(E_{\rm eq}\subset A^2\)
be the image of all successful labels. Then
\[
N\le M\le dN,\qquad
Q:=|E_{\rm eq}|\le (4d+h)M\le d(4d+h)N.
\tag{7}
\]
Therefore
\[
Q\ge N^2-B
\quad\Longrightarrow\quad
\boxed{d(4d+h)\ge N-B/N.}
\tag{8}
\]
If \(f\) is injective on \(X\), the factor \(d\) outside the parentheses
can be removed.

More generally, let chart \(j\) have a scalar map \(f_j\), pole degree
\(d_j\), output degree \(h_j\), and a finite parameter set \(X_j\) with
\(f_j(X_j)\subseteq A\). The union of its successful-pair images obeys
\[
\boxed{
\left|\bigcup_{j=1}^J E_j\right|
 \le N\sum_{j=1}^J d_j(4d_j+h_j).}
\tag{9}
\]
In particular, if \(d_j,h_j\le D\), near-complete coverage requires
\[
5JD^2\ge N-B/N.
\tag{10}
\]
For charts injective on their parameter sets, \(5JD\) replaces \(5JD^2\).

### Proof

A scalar value has at most \(d\) parameter preimages by the zero count
in §2, so \(M\le dN\). Projection cannot increase the number of successful
labels, giving (7) from EG-B3. Rearrangement proves (8).
For each chart in a library, \(|X_j|\le d_jN\), even if its scalar
image is a proper subset of \(A\). Sum the upper counts, allowing overlaps,
to prove (9). Uniform degree bounds give (10). \(\square\)

### Why it matters

A bounded-degree group-law chart cannot control almost all scalar pairs.
A library with \(J\le N^\theta\), fixed \(\theta<1\), and uniformly
subpolynomial \(d_j,h_j\) also has only \(N^{1+\theta+o(1)}\) controlled
pairs. This is a finite-grid obstruction for a genuinely two-parameter
elliptic ansatz, beyond the earlier one-parameter rational-curve capacity
bound.

### Scope

These are coverage and degree-cost theorems, not an actual-image lower
bound outside the ansatz. For constant \(H\), the chart lies in one actual
cubic fiber and has at most \(N\) distinct real scalar pairs by the frozen
strict-monotonicity fiber bound. Thus constant output is not an omitted
near-complete exception. Nothing here says that finite output compression
must factor through the displayed elliptic group statistic.

## 6. EG-B5 — sum antisymmetry, with projection multiplicities retained

### Meaning

Even if the degree of \(H\) grows, a single sum rule cannot succeed in both
orientations of a pair of distinct, uniquely represented scalars. With
multiple parameter representatives, the label obstruction survives but
must not be silently promoted to the same scalar-pair obstruction.

### Exact statement — PROVED

Let \(X\) be a nonempty finite subset of any abelian group, \(M=|X|\), let
\(f:X\to\mathbb R\), and set \(A=f(X)\), \(N=|A|\).
Let \(H\) be any single-valued partial function on \(T+(X+X)\).
Write \(a_x=|\{R\in X:f(R)=x\}|\), and let \(L\) count defined labels
satisfying
\[
P(f(R),f(S))=H(R+S+T).
\tag{11}
\]
Then
\[
\boxed{L\le\frac{M^2+\sum_{x\in A}a_x^2}{2}.}
\tag{12}
\]
If \(n_1\) scalar values have exactly one representative, the distinct
successful scalar-pair image satisfies
\[
\boxed{Q\le N^2-\binom{n_1}{2}.}
\tag{13}
\]
In particular, injective projection gives
\(Q=L\le N(N+1)/2\), independently of every degree.
Near-complete scalar coverage with \(B=O(N^{2-\delta})\) requires
\(n_1=O(N^{1-\delta/2}+1)\).

### Proof

If both \((R,S)\) and \((S,R)\) succeed, their right sides agree.
Subtracting the cubic values gives
\(2(f(R)-f(S))^3=0\), so \(f(R)=f(S)\).
Among the \(M^2-\sum_xa_x^2\) labels with unequal scalar values, at most
one orientation in each swapped pair succeeds. Labels with equal values
contribute at most \(\sum_xa_x^2\). This proves (12).

For two distinct scalar values with unique representatives, the two
opposite scalar pairs have only the corresponding swapped labels.
At least one is absent. Different unordered pairs give different missing
scalar pairs, proving (13) and its consequences. \(\square\)

### Why it matters

The injective single-sum ansatz has a quadratic uncovered set even when
the meromorphic degrees grow arbitrarily.

### Scope

If \(f\) is not injective, opposite scalar pairs may use different label
sums. Thus the bound \(N(N+1)/2\) is not valid without the stated
injectivity or an additional well-defined descent to scalar pairs.
For instance, the even coordinate map on a Weierstrass curve identifies
\(R\) with \(-R\); the labels \((R,S)\) and \((-S,-R)\) have opposite
scalar orientations but sums \(R+S\) and \(-(R+S)\).

Different charts can also cover opposite orientations using different
rules. Formula (13) is for one rule, not a union bound excluding all
multi-chart assemblies.

## 7. EG-B6 — the difference rule on a small-difference parameter set

### Meaning

For a difference rule, the two orientations use \(H(T+t)\) and
\(H(T-t)\). Together those two values determine a real ordered scalar
pair uniquely. If the parameter difference set is small, both orientations
cannot succeed on nearly the entire parameter square.

### Exact statement — PROVED

Use the finite abelian-group and real-scalar setting of EG-B5, but let
\[
K=|X-X|,\qquad D=\max_{x\in A}a_x.
\]
For any single-valued partial \(H\) on \(T+(X-X)\), let \(L\) count
defined successful labels for
\[
P(f(R),f(S))=H(T+R-S).
\tag{14}
\]
Then
\[
\boxed{L\le \min\left\{M^2,\frac{M^2+DK}{2}\right\}.}
\tag{15}
\]
For injective \(f\), this bounds the actual successful scalar pairs.
In particular, if \(X\) is a finite subgroup and \(f\) is injective,
then \(K=M=N\) and
\[
Q\le N(N+1)/2.
\tag{16}
\]
More generally, bounded \(D\) and \(K=O(M)\) prohibit near-full label
coverage, independently of meromorphic degrees.

### Proof

Let \(\mathcal L\subseteq X^2\) be the successful labels. Its transpose
has the same cardinality, so
\[
|\mathcal L\cap\mathcal L^{\rm op}|\ge2L-M^2.
\]
For a label in the intersection, put \(t=R-S\), \(x=f(R)\), \(y=f(S)\).
The two successful equations imply
\[
2(x+y)=H(T+t)+H(T-t),\qquad
2(x-y)^3=H(T+t)-H(T-t).
\]
The real cube map is injective. Hence for each \(t\), these values
determine at most one real ordered pair \((x,y)\).
There are at most \(D\) choices of \(R\) with that first scalar value,
and \(S=R-t\) is then determined. Summing over the \(K\) possible
differences gives
\(2L-M^2\le DK\). This proves (15) and its consequences. \(\square\)

### Why it matters

This finite structured-set obstruction remains when the pole-degree
bound becomes weak because \(H\) has high degree. It includes complex
elliptic parameter points whose chosen scalar values are real; no order
on the elliptic parameter group is assumed.

### Scope

Without injectivity, a label deficit need not be a scalar-pair deficit.
For complex scalar values the cube equation has up to three solutions,
so the same proof gives \(3DK\) in place of \(DK\); the sharper real
version is the one relevant to the final same-set target.
Parameter sets with large difference sets and multi-chart assemblies
remain outside the indicated corollaries.

## 8. Quantitative accounting and provenance

The fixed output identity and same-set completion requirements are inherited
from the [near-complete-chart checkpoint](../2026-09-30-near-complete-charts/README.md).
The results above are new group-law and finite-grid arguments. The prior
rational fixed-output classification was not rerun and is not a proof
dependency. No unavailable historical source is used.

| Claim | Status and scope | Complete proof / dependencies | Retained boundary |
|---|---|---|---|
| EG-B1 | PROVED; global same-map sum/difference identities on complex elliptic curves | §1; symmetry and regular diagonal | Finite selected equalities |
| EG-B2 | PROVED; separated polynomial expressions versus nonconstant twisted group-law outputs, including independently algebraized branches on finite covers | §3; mixed poles and finite-map fibers | Rational mixed denominators, pair-dependent branch choices and finite grids |
| EG-B3 | PROVED; every finite pole-free grid, all stated degrees/isogenies | §4; zero/pole count and explicit exceptional rows | Growing degree costs may be large |
| EG-B4 | PROVED; real scalar projections and growing same-map chart libraries | §5; degree, projection and union counts | Arbitrary finite compression need not have this form |
| EG-B5 | PROVED; any finite abelian-group sum rule | §6; antisymmetry with exact scalar multiplicities | Noninjective scalar projection and multiple rules |
| EG-B6 | PROVED; any finite abelian-group difference rule with real scalar values | §7; reverse-label count and real cube injectivity | Large difference sets or noninjective scalar projection |

All claims concern T01 and \(P=(x-y)^3+x+y\), version 1 dated
2026-09-30. Evidence consists of the full internal proofs above;
EG-B1–B6, including the finite-cover extension under EG-B2, have passed
independent internal lead audit, as recorded in this cycle's verification
record. No external review or novelty claim is made.

Pole degrees include multiplicity. Isogeny degrees, parameter projection
fibers, successful labels, distinct scalar pairs, chart count, and
uncontrolled labels are kept separate. Every full-square completion still
costs \(N^2-Q\) potentially new outputs. None of these obstructions is
presented as a universal actual-image lower bound. Heights, field degrees
and arithmetic amplification supply no saving here and were not used.

No carrier evaluations or symbolic-search programs were run. The global
T01 target and the actual small-fiber-tail witness remain **OPEN**.
The lead report will retain exactly one next obligation; this companion
adds no competing research assignment.
