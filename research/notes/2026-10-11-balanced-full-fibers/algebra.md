# Balanced-factor scalar algebra and exact full-fiber audit design

**11 October 2026 · version 1 · T03 · specialist A.** Fixed polynomial
\(Q(x,y)=x^2+xy+y^2\). This contribution belongs to the authorized
**Balanced-Factor Carrier Full Fibers and Coupled Phase Returns** cycle.
There is one unchanged carrier, no amplitude search, no new mechanism,
no nested delegation and no network access. This author executed no
mathematical program and has zero charged evaluations and zero research
program CPU seconds. The lead owns all finite computation.

## 1. Source boundary and claims

The controlling carrier and complete prior proofs are
[AMP-A1–A4](../2026-10-06-cross-block-amplification/amplitudes.md),
with the prior
[AMP-R1–R3 certificate theorem](../2026-10-06-cross-block-amplification/returns.md)
and [final report](../2026-10-06-cross-block-amplification/README.md).
That theorem bounds its specified certificate, not full fibers. Its
proof remains unchanged. The earlier 33-frequency theorem is not extended
or used here. The underlying field-degree and seven-slot facts retain
their complete proof locator in
[FG-A1](../2026-10-06-fiber-growth/amplitudes.md), §1.

| ID | Status and exact scope | Locator |
|---|---|---|
| BFF-A1 | PROVED: exact disjoint scalar decomposition and \(16q^2+1\le n\le24q^2-7\) for this carrier | §2 |
| BFF-A2 | PROVED: a six-coefficient arithmetic model at \(r=1\), and an exact pulled-back multiplication law at every depth | §3 |
| BFF-A3 | PROVED: exact two-component full-output equality test and the base-subfield-valued mixed-block locus | §4 |
| BFF-A4 | PROVED: complete sign/swap orbit enumeration and weights, including all degeneracies | §5 |

The formula proofs below are symbolic results. The code review in §6 is
a pre-execution inspection, not a claim that any scout or verification
has run. Finite outputs and their validation belong to the lead's record.
No claim here proves a fixed compression exponent, a full-fiber upper
bound, or a near-full growing return tail.

## 2. BFF-A1 — exact scalar decomposition and improved size bounds

### Statement

Fix \(r\ge0\), \(q=7^r\), \(m=6q\),
\(\xi=e^{2\pi i/q}\), \(\omega=e^{2\pi i/3}\), and
\(\Delta=1+2\omega\), so \(\Delta^2=-3\). Put
\(H=\mathbb Q(\xi)\), \(L=\mathbb Q(\omega,\xi)\), and
\(K^+=L\cap\mathbb R\). The fixed amplitudes are

\[
c_{h,\mathbf i}=h\prod_{\ell=0}^{r-1}(2-\xi^{i_\ell7^\ell}),
\quad 1\le h\le8,\quad
\mathbf i\in\{-3,-2,-1,0,1,2,3\}^r.
\tag{1}
\]

Define

\[
B=\{\xi^a c_{h,\mathbf i}:a\in\mathbb Z/q,\ h,\mathbf i
\text{ as in (1)}\}\subset H,
\qquad D=\{\bar b-b:b\in B\}.
\tag{2}
\]

As before, \(Z=\mu_6B\) and

\[
X(z)=\frac{\omega\bar z-\omega^2z}{\Delta},\qquad
Y(z)=\frac{\bar z-z}{\Delta},\qquad
A=X(Z)=Y(Z).
\tag{3}
\]

Then

\[
\boxed{A=X(V),\qquad V=B\mathbin{\dot\cup}(-B)
                    \mathbin{\dot\cup}D,}
\tag{4}
\]

where the union is disjoint and \(X\) is injective on \(H\). Thus

\[
\boxed{n=|A|=16q^2+|D|,\qquad
16q^2+1\le n\le24q^2-7.}
\tag{5}
\]

Exactly eight points of \(B\) are real: \(1,2,\ldots,8\).
The seed is \(A_0=\{-8,-7,\ldots,8\}\), with \(n_0=17\).

### Meaning

This strengthens the scalar count for the same carrier. It does not
change any amplitude, omit any projected value, or assume that the full
projection from \(Z\) is injective. All collisions in the third piece
are retained in the actual finite set \(D\).

### Proof

AMP-A1 gives \(|B|=8q^2\), pairwise disjoint amplitude cosets modulo
\(\mu_{6q}\), and uniqueness of the phase within each such coset.
Conjugation negates every digit and the exponent \(a\), hence
\(\bar B=B\). Also \(B\cap(-B)=\varnothing\): a meeting would
first force the same amplitude label by coset disjointness, and then
\(\xi^a=-\xi^{a'}\), impossible because \(q\) is odd.

In particular no \(b\in B\) is purely imaginary. Otherwise
\(\bar b=-b\) would belong to both \(B\) and \(-B\).
Every \(d\in D\) is purely imaginary, including possibly 0, so
\(D\cap(B\cup(-B))=\varnothing\). Moreover \(D=-D\), since
\(\bar B=B\).

Directly from (3),

\[
X(\bar z)=X(z)+Y(z),\qquad
Y(z)=X(\bar z-z).
\tag{6}
\]

The six unit projections of an element \(z\in B\) are
\(\pm X(z),\pm Y(z),\pm(X(z)+Y(z))\). Equations (6) and
\(\bar B=B\) therefore prove (4).

For completeness, \(\omega\notin H\) by the degree calculation in
FG-A1; this also holds at \(q=1\), when \(H=\mathbb Q\).
If \(X(v)=0\) for \(v\in H\), then \(\bar v=\omega v\).
Any nonzero \(v\) would give \(\omega=\bar v/v\in H\), a
contradiction. Thus \(X\) is injective on \(H\), proving the exact
cardinality in (5).

Finally, if \(b=\xi^a c_{h,\mathbf i}\) is real, then
\(\xi^a c_{h,\mathbf i}=\xi^{-a}c_{h,-\mathbf i}\).
Coset disjointness forces \(\mathbf i=-\mathbf i\), hence every
digit is zero. Phase uniqueness then gives \(2a=0\pmod q\), so
\(a=0\). Thus the eight real points are exactly \(b=h\).
They all map to 0 under \(b\mapsto\bar b-b\); the remaining
\(8q^2-8\) points give at most that many further values. Therefore
\(1\le|D|\le8q^2-7\), proving the inequalities.

### Consequence

The depth rate is still \(n=49^{r+o(r)}\). At \(r=1\), the actual
input count is at most 1169, rather than the preceding bound 2352.
This improved bound is useful for exhaustive finite budgeting; it is
not a new asymptotic image estimate.

## 3. BFF-A2 — exact arithmetic through \(H\)

### Statement

For \(v,w\in H\), define the symmetric bilinear expression

\[
M(v,w)=2vw+v\bar w+\bar v w-\bar v\bar w.
\tag{7}
\]

Then

\[
\boxed{X(v)X(w)=X(M(v,w)/3).}
\tag{8}
\]

Consequently the integer expression

\[
\mathcal K(v,w)=M(v,v)+M(v,w)+M(w,w)
\tag{9}
\]

satisfies \(X(\mathcal K(v,w))=3Q(X(v),X(w))\). In particular,
for arbitrary \(v,w,v',w'\in V\),

\[
Q(X(v),X(w))=Q(X(v'),X(w'))
\quad\Longleftrightarrow\quad
\mathcal K(v,w)=\mathcal K(v',w')\text{ in }H.
\tag{10}
\]

### Proof

Write \(v=s+a\), \(w=t+b\), where
\(\bar s=s,\bar t=t,\bar a=-a,\bar b=-b\). Then

\[
X(v)=s+a/\Delta,\qquad X(w)=t+b/\Delta,
\qquad M(v,w)/3=st-ab/3+sb+at.
\]

Since \(\Delta^2=-3\), applying \(X\) to the last expression
gives exactly the product of the first two. This proves (8).
Linearity gives (9), and injectivity of \(X\) on \(H\) gives (10).

### Meaning and arithmetic consequence

At \(r=1\), \(H=\mathbb Q(\xi_7)\) has degree 6. Each element
of \(V\), and each key (9), can be stored as a canonical six-integer
coefficient tuple modulo
\(\Phi_7(T)=1+T+\cdots+T^6\). No rational arithmetic is required
for these keys, even though the original scalar projection contains
\(1/\Delta\). At \(r=0\), the same formula reduces to ordinary
integer arithmetic because conjugation is trivial.

A possible multiplication optimization is

\[
M(v,w)=2(vw)-\overline{vw}
                 +(v\bar w)+\overline{v\bar w}.
\tag{11}
\]

This uses two multiplications in \(H\), together with conjugation
and addition. The current lead scout instead uses the already inspected
12-coordinate cyclotomic field model. Equation (9) is a proved optional
arithmetic model, not a claim that a second implementation was executed.

For independent comparison with a model storing \(3A\), note that
\(3X(\mathcal K)=9Q\). Thus decoding (9) with the integer map
\(z\mapsto3X(z)\) produces exactly the same scaled output as direct
evaluation on \(3A\).

## 4. BFF-A3 — full-output components and a mixed-block locus

### Statement

Let \(F=H\cap\mathbb R\), and use the decomposition in §3. Then

\[
Q(X(v),X(w))=E(v,w)+O(v,w)/\Delta,
\tag{12}
\]

where

\[
\begin{aligned}
E(v,w)&=s^2+st+t^2-(a^2+ab+b^2)/3\in F,\\
O(v,w)&=2sa+sb+ta+2tb\in H,\qquad \bar O=-O.
\end{aligned}
\tag{13}
\]

Two full quadratic outputs are equal if and only if both their \(E\)
components and their \(O\) components agree. Further:

1. Every output from \(X(D)\times X(D)\) belongs to \(F\).
2. For \(v\in B\cup(-B)\) and \(w\in D\),

\[
\boxed{Q(X(v),X(w))\in F
\quad\Longleftrightarrow\quad w=\bar v-v.}
\tag{14}
\]

The latter source is precisely \((X(v),Y(v))\), and hence is an
encoded pair. The same assertion holds after swapping the two coordinates.

### Proof

Expand \(Q(s+a/\Delta,t+b/\Delta)\) to obtain (12)–(13).
The two components are independent: if \(E+O/\Delta=0\) with
\(E\in F\) and \(O\in H\), then a nonzero \(E\) would imply
\(\Delta=-O/E\in H\), contrary to \(\omega\notin H\).
Thus \(E=O=0\). Applying this to a difference gives the equality
test, and it also shows that (12) belongs to \(F\) exactly when
\(O=0\).

For \(v,w\in D\), both are purely imaginary in \(H\), so
\(s=t=0\) and \(O=0\). For \(v\in B\cup(-B)\), BFF-A1
shows that \(s\ne0\); for \(w\in D\), \(t=0\), \(b=w\).
Then \(O=s(2a+b)\), which vanishes exactly when
\(w=b=-2a=\bar v-v\). This value lies in \(D\) because
\(D=-D\), and (6) identifies the encoded coordinates.

### Meaning and limit

Equation (14) identifies an exact interface between the encoded norm
values and the completed square. It does not classify the full fibers:
\(X(B\cup(-B))^2\) can also produce \(F\)-valued outputs, and
\(X(D)^2\) remains a substantial unclassified block. Outputs outside
\(F\) can likewise collide across the other blocks. No small-fiber
population, image lower bound, or image upper saving is inferred from
this decomposition.

## 5. BFF-A4 — complete symmetry weights for the finite audit

### Statement and proof

Let any finite \(A=-A\subset\mathbb R\) contain 0 and have
\(n=2M+1\) elements. Work with exact canonical algebraic tuples, and
choose one representative from each nonzero pair \(\{a,-a\}\),
forming a set \(P\) of size \(M\). The choice can be lexicographic;
it need not be the positive real embedding.

The group generated by simultaneous negation and coordinate swap
preserves \(Q\). The following are complete, nonrepeating orbit
representatives:

| Source representative | Index range | Actual source-pair weight |
|---|---|---:|
| \((0,0)\) | Once | 1 |
| \((a,0)\) | \(a\in P\) | 4 |
| \((a,b)\) | Unordered \(a,b\in P\), repetition allowed | 4 if \(a\ne b\), otherwise 2 |
| \((a,-b)\) | The same unordered index range | 4 if \(a\ne b\), otherwise 2 |

Every ordered pair is equivalent to exactly one listed representative:
if both coordinates are nonzero, their sign choices are either the same
or opposite after simultaneous negation; swapping fixes the unordered
representative indices. The only reduced orbit sizes are the diagonal,
antidiagonal and origin cases already listed. There are exactly

\[
1+M+2\binom{M+1}{2}=(M+1)^2=(n+1)^2/4
\tag{15}
\]

representatives, whose weights sum to \(n^2\). This is a complete
square computation with symmetry weights, not a sample or a thinning.

An alternative traversal used in the lead's primary scout sorts all
tuples \(a_0<\cdots<a_{n-1}\), with
\(-a_i=a_{n-1-i}\), and takes

\[
0\le i\le M,\qquad i\le j<n-i.
\tag{16}
\]

Each unordered pair is selected on the half \(i+j\le n-1\) of
the index square, so (16) describes the same orbit quotient with a
different traversal. Weights are the size of the four-element orbit
set, including coincidences. Summing \(n-2i\) over \(0\le i\le M\)
again gives (15).

### Consequence for the two predeclared cases

At \(r=0\), \(n=17\), so the quotient has 81 representatives.
At \(r=1\), BFF-A1 gives \(n\le1169\), so it has at most
\(585^2=342225\) representatives. These are symbolic forecasts,
not measured scalar counts or program results. The complete ordered
pair histogram is obtained by adding the orbit weights to each exact
output key.

## 6. Pre-execution code inspection and validation design

Inspected locally, without executing mathematical code:

- `experiments/modular_lift.py`: monic cyclotomic polynomial division,
  canonical integer coefficient reduction, multiplication, conjugation,
  and the integer `decode3` formula.
- `experiments/return_tail.py`: the separate Eisenstein-coefficient
  representation over \(\Phi_p\), conjugation, and norm/matrix formulas.
- `local-only/runs/T03/2026-10-11-balanced-full-fibers/scout.py`: the lead's
  new fixed \(r=0,1\) build, full symmetry enumeration and norm oracle.

The inspected scout stores exactly \(3A\) in
\(\mathbb Z[\zeta_{6q}]\), of degree 2 or 12. The primary key is
\(a^2+ab+b^2=9Q(a/3,b/3)\). The independent expression is

\[
(a-\omega b)(a-\omega^2b)=a^2+ab+b^2.
\tag{17}
\]

The primary uses a sparse-aware multiplication routine and traversal
(16); the oracle uses the existing field multiplication and the first
traversal in §5. Both compare the complete exact output-count map, not
only its size or a moment. The seed also permits a separate raw integer
enumeration of all \(17^2\) pairs. The implementations share canonical
field reduction; this review does not describe them as independently
implemented number-field packages.

The following code logic passed the pre-execution inspection:

- complete amplitude, phase and scalar construction, exact reality and
  symmetry checks, including the explicit \(r=0\) scalar seed;
- all symmetry weights and forecasts in §5;
- pair-weighted median of the full fiber size;
- strict threshold \(F_A(p)<n^{1/4}\), tested exactly as
  \(F_A(p)^4<n\), avoiding floating point;
- the count of sources whose full fiber exceeds their **own** sign/swap
  orbit, including pairs in two-element or one-element orbits whose
  full fiber is still at most four;
- complete norm-distribution comparison using (17), zero fiber of size
  one, weighted total \(n^2\), stage budgets and recorded runtime errors.

Two pre-build completion requests were sent to the lead: use new-output
guards for case/distribution/result JSONs while appending the budget log,
and check BFF-A1's stronger size bounds in the build. A later read of
the saved source confirmed both changes. The lead controls the final
source hash, execution, and output provenance. This author did not run
the program; finite results and their completed verification are recorded
separately by the lead.

## 7. Check of the one coordinated coupled-phase mechanism

Specialist B owns the selected phased transposition and its final proof.
The current check concerns its common matching-digit-switch subfamily;
B's theorem also permits independent switches. No mutation is added here.
Write source representatives
\(z=c\alpha,w=d\beta\), \(\alpha,\beta\in\mu_{6q}\). A common
factor switch acts on matching nonzero digits in a subset \(S\), giving
\(c'=uc,d'=ud\). For fixed \(\kappa,\lambda\in\mu_6\), the
proposed target is

\[
\bigl(X(\kappa c'\beta),Y(\lambda d'\alpha)\bigr).
\tag{18}
\]

Its two coordinates belong to \(A\); that alone does not prove
equality of norms. Fix \(c,d,S,\kappa,\lambda,\alpha\) and regard
the full target-minus-source norm difference as a Laurent polynomial in
\(\beta\). After multiplication by \(\Delta^2\), its
\(\beta^2\) coefficient is exactly

\[
\omega\kappa^2(c')^2-d^2.
\tag{19}
\]

Indeed the only \(\beta^2\) contributions come from the square of
the new first coordinate and the square of the old second coordinate;
both mixed scalar terms have Laurent degree at most one. If (19) is
nonzero, multiplication by \(\beta^2\) gives a nonzero polynomial
of degree four, leaving at most four possible phases.

If (19) vanishes, \(d/c'\in\mu_6\), because \(\omega\) has a
square root in \(\mu_6\). The bare amplitude coset theorem then
forces \(d=c'\), and \(\kappa=\pm\omega\). For a nonempty
common switch on matching nonzero digits, \(d=c'\) is impossible:
on each switched digit, the second original word agrees with the first,
whereas the first switched word has its opposite. Thus every nonempty
such common switch has a nonzero coefficient (19).

For the empty switch, the possible degeneracy is confined to \(c=d\).
All sources with that representation have at most
\((8q)(6q)^2=288q^3\) labels before scalar deduplication. This is a
source-domain bound, not a full-fiber bound. The check agrees with B's
selected mechanism and is separate from the former fixed-phase
coordinate-switch obstruction. The final permitted phase/sign closures,
their constants, and any all-depth certificate conclusion are controlled
by B's companion and the lead's audit.

## 8. Accounting, review, and limits

The construction ledger from the previous cycle remains in force:
no thinning, the same scalar set in both coordinates, growing field
degree, fixed denominator 3, amplitude conjugate bound \(8\cdot3^r\),
and no uncharged regulator/discriminant theorem. BFF-A1 changes only the
proved scalar prefactors; it leaves the input rate \(2\log7\) per
depth unchanged. Equations (9) and (12) retain every pair and every
algebraic relation. Symmetry weights remove repeated computation, not
source-pair mass.

Specialist C independently audited the complete written BFF-A1–A4 proofs
and the stated subfamily check in §7, and reported PASS on 11 October
2026. The review included the full-output component equality and the
precise mixed-block locus, without extending it to the other blocks.
The lead independently checked the scalar decomposition and product key.
These are internal reviews, not external review or novelty verification.

**Remaining gap:** neither the exact algebra nor the finite two-level
audit supplies an all-depth full-fiber tail or an upper bound for the
entire image with a fixed positive exponent gap. The coupled certificate
must not be substituted for the full fiber function. T03 and its separate
adaptive RC15/4 obligation remain OPEN. This note commissions no new
carrier, deeper computation, or successor mechanism.
