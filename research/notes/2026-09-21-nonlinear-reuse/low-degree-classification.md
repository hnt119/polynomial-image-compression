# Quadratic polynomial charts and low-degree output statistics

T01 / nonlinear coordinate-reuse cycle, 2026-09-21 v1.
The fixed polynomial is \(P(x,y)=(x-y)^3+x+y\).
Let \(U,V\in\mathbb R[r,s]\) have total degree at most two, and put
\[
F=U^3+V,\qquad X=(V+U)/2,\qquad Y=(V-U)/2.
\tag{L0}
\]
Thus \(P(X,Y)=F\). The question in this note is exact polynomial
factorization through a nonconstant statistic of degree at most two.
Small output cardinality on a finite grid is not assumed to imply
such a factorization.

For orientation, \(U=r+s,\ V=(r+s)^2\) makes the output depend on
one scalar \(r+s\); the pair also depends on that same scalar.
Likewise \(U=r^2+s^2,\ V=2U+1\) looks like a nonlinear two-parameter
chart, but its two coordinates lie on a line. The classification below
shows that these two types exhaust the stated ansatz.

No network source, field construction, or carrier search is used.
A bounded exact symbolic coefficient calculation is recorded in §5.

## 1. NR-L1 — the cubic cannot hide a second quadratic direction

### Meaning

If the output is constant along the level curves of an affine or
quadratic statistic, then both input coordinates already have that
same invariance. The high-degree part \(U^3\) cannot be canceled by
the degree-two correction \(V\).

### Exact statement

**PROVED.** For any nonconstant \(\Phi\in\mathbb R[r,s]\) with
\(\deg\Phi\le2\), define
\[
J(A,B)=A_rB_s-A_sB_r.
\]
Then
\[
J(U^3+V,\Phi)=0
\quad\Longrightarrow\quad
J(U,\Phi)=J(V,\Phi)=0.
\tag{L1}
\]
The converse is immediate. Constant \(U\) and constant \(V\) are allowed.

### Proof

The identity is
\[
3U^2J(U,\Phi)+J(V,\Phi)=0,
\tag{L2}
\]
where \(\deg J(V,\Phi)\le2\).
If \(\deg U=2\) and \(J(U,\Phi)\ne0\), the first term has degree
at least four, so cannot cancel the second. Hence both Jacobians vanish.
If \(U\) is constant, the conclusion follows directly from (L2).

Suppose \(\deg U=1\). An invertible affine change of parameter
coordinates makes \(U=r\); such a change preserves degrees and the
vanishing of Jacobians. If \(J(U,\Phi)\) has degree one, the first
term in (L2) has degree three, again impossible. It remains to rule
out \(J(U,\Phi)=c\ne0\).
Since \(J(r,\Phi)=\Phi_s\), this forces
\[
\Phi=ar^2+br+cs+d.
\]
Write
\[
V=Ar^2+Brs+Cs^2+Dr+Es+G.
\]
Direct differentiation gives
\[
\begin{aligned}
J(r^3+V,\Phi)
={}&(3c-2aB)r^2-4aCrs\\
&+(2cA-bB-2aE)r+(cB-2bC)s+cD-bE.
\end{aligned}
\tag{L3}
\]
If \(a=0\), its \(r^2\) coefficient is \(3c\ne0\).
If \(a\ne0\), the \(rs\) coefficient first forces \(C=0\),
then the \(s\) coefficient forces \(B=0\), and the \(r^2\)
coefficient again becomes \(3c\ne0\). This contradiction rules out
the last case. Thus \(J(U,\Phi)=0\), and (L2) gives \(J(V,\Phi)=0\).
\(\square\)

### Why it matters

The Jacobian formulation is broader than assuming \(F=W(\Phi)\):
it covers every polynomial composition and some further algebraic
dependences. The conclusion nevertheless applies to the inputs
separately, before any finite-set counting.

### Scope

The degree bounds and the requirement that \(\Phi\) be nonconstant
are essential hypotheses. A constant \(\Phi\) has zero Jacobian with
every polynomial and provides no restriction. No statement about a
finite set of parameter values alone is used.

## 2. NR-L2 — complete classification of the Jacobian ansatz

### Meaning

There are two possibilities. Either all quantities depend on one
affine parameter, or both \(U\) and \(V\) are affine functions of the
same genuinely two-variable quadratic statistic. In the latter case
the pair coordinates lie on a line despite the quadratic parameter.

### Exact statement

Call a quadratic polynomial genuine here if it is not a univariate
polynomial in any nonconstant affine form. For \(\deg U,\deg V\le2\),
the following conditions are equivalent:

1. \(J(U,V)=0\).
2. Some nonconstant \(\Phi\) of degree at most two satisfies
   \(J(U^3+V,\Phi)=0\).
3. The pair \(U,V\) has one of these forms:
   \[
   U=f(\ell),\quad V=g(\ell),
   \quad \ell\ \text{nonconstant affine},\quad \deg f,\deg g\le2;
   \tag{L4}
   \]
   or
   \[
   U=a\Phi+b,\quad V=c\Phi+d,
   \quad \Phi\ \text{a genuine quadratic}.
   \tag{L5}
   \]

The coefficients and functions in these forms may be constant.
For a specified statistic \(\Phi\), (L1) has exactly these solutions:
if \(\Phi\) is affine or a quadratic polynomial in an affine
\(\ell\), then \(U,V\) are polynomials of degree at most two in that
\(\ell\); if \(\Phi\) is genuine quadratic, then (L5) holds.

### Proof: exhaustive quadratic coefficient reduction

We first classify all degree-at-most-two \(Q\) with \(J(Q,\Phi)=0\).
Invertible affine changes of \((r,s)\), and nonzero affine changes of
the value of \(\Phi\), preserve this condition. Every nonconstant
real polynomial \(\Phi\) of degree at most two reduces to one of
\[
r,\qquad r^2,\qquad r^2+s,\qquad r^2+s^2,\qquad r^2-s^2.
\tag{L6}
\]
Here is why this list is exhaustive. A rank-two quadratic homogeneous
part allows a translation removing both linear terms; completing
squares then gives one of the two nondegenerate quadratic forms.
A rank-one part becomes \(r^2\); shifting \(r\) removes its linear
term, leaving either no transverse term or a nonzero linear \(s\)
term, which can be normalized to \(s\). A rank-zero homogeneous part
leaves a nonconstant affine polynomial, normalized to \(r\).
These transformations account for every real coefficient, not just
bounded or rational coefficients.

Write \(Q=Ar^2+Brs+Cs^2+Dr+Es+G\). For \(\Phi=r\) or \(r^2\),
the identity forces \(Q_s=0\), so
\[
Q\in\operatorname{span}_{\mathbb R}\{1,r,r^2\}.
\tag{L7}
\]
For \(\Phi=r^2+s\),
\[
J(Q,\Phi)=-2Br^2-4Crs+(2A-2E)r+Bs+D.
\]
Its vanishing forces \(B=C=D=0\), \(E=A\), and therefore
\[
Q\in\operatorname{span}_{\mathbb R}\{1,\Phi\}.
\tag{L8}
\]
For \(\Phi=r^2+\epsilon s^2\), \(\epsilon\in\{1,-1\}\),
\[
J(Q,\Phi)=-2Br^2+2\epsilon Bs^2
 +4(\epsilon A-C)rs-2Er+2\epsilon Ds.
\]
Thus \(B=D=E=0\), \(C=\epsilon A\), again giving (L8).
This proves the claimed classification for a specified \(\Phi\).

Now condition 2 and NR-L1 put both \(U,V\) in the appropriate
solution space, proving condition 3. Both forms in condition 3 have
\(J(U,V)=0\), proving condition 1. Conversely, if \(U\) is
nonconstant and \(J(U,V)=0\), choose \(\Phi=U\). Then
\(J(U^3+V,\Phi)=0\), proving condition 2. If \(U\) is constant
but \(V\) is not, choose \(\Phi=V\). If both are constant, any
nonconstant affine \(\Phi\) works. \(\square\)

### Why it matters

This is an all-coefficient classification of the bounded-degree
Jacobian ansatz. An input map with \(J(U,V)\ne0\) cannot make its
output depend, even in this Jacobian sense, on any nonconstant
affine or quadratic polynomial statistic.

### Scope

The word genuine distinguishes two-variable quadratics from squares
or quadratic polynomials of one affine form; it does not assert a
finite-image cardinality property. A polynomial statistic with large
finite image may still have one-dimensional Jacobian dependence.
Conversely, small finite image need not imply this polynomial identity.

## 3. NR-L3 — exact polynomial compositions

### Meaning

Requiring an actual identity \(U^3+V=W(\Phi)\), rather than just a
vanishing Jacobian, narrows the specified quadratic-statistic solutions
further: both \(U\) and \(V\) must be affine functions of \(\Phi\).

### Exact statement

**PROVED.** Let \(W\in\mathbb R[t]\) and \(\Phi\) be nonconstant.
Under \(\deg U,\deg V\le2\):

- If \(\deg\Phi=1\), then \(F=W(\Phi)\) holds exactly when
  \(U=f(\Phi)\), \(V=g(\Phi)\), with \(\deg f,\deg g\le2\), and
  \(W=f^3+g\).
- If \(\deg\Phi=2\), then \(F=W(\Phi)\) holds exactly when
  \[
  U=a\Phi+b,\qquad V=c\Phi+d,\qquad
  W(t)=(at+b)^3+ct+d.
  \tag{L9}
  \]

Consequently existence of such a polynomial composition through
some nonconstant statistic of degree at most two is also equivalent
to the three conditions of NR-L2.

### Proof

For affine \(\Phi\), use NR-L1 and (L7), taking \(\Phi\) itself
as the affine coordinate. Substitution proves the converse, and
substitution by a nonconstant polynomial is injective on
\(\mathbb R[t]\), so the displayed \(W\) is necessary.

Let \(\deg\Phi=2\). If \(U\) is constant, then \(\deg F\le2\);
degree multiplication under composition forces \(W\) to be affine
or constant, which gives (L9). If \(\deg U=1\), then \(\deg F=3\),
whereas a nonconstant polynomial of \(\Phi\) has even degree.
This case is impossible.

If \(\deg U=2\), then \(\deg F=6\), so \(\deg W=3\). Let the
leading coefficient of \(W\) be \(a^3\), \(a\ne0\). The degree-six
terms imply
\[
U_2^3=a^3\Phi_2^3,
\]
where subscripts denote homogeneous degree-two parts. Real cube
injectivity gives \(U_2=a\Phi_2\), so \(R=U-a\Phi\) has degree
at most one. Expanding
\[
U^3=a^3\Phi^3+3a^2R\Phi^2+3aR^2\Phi+R^3
\]
shows that a nonzero linear part of \(R\) would create degree five,
which no other term of \(W(\Phi)-V\) can cancel. Thus \(R=b\)
is constant. Now
\[
V=W(\Phi)-(a\Phi+b)^3.
\]
Its degree is at most two, so the coefficient of \(\Phi^2\) must
vanish. The remaining polynomial is \(c\Phi+d\), proving (L9).
The converse follows by substitution. The existential equivalence
uses the explicit common statistics in (L4) and (L5). \(\square\)

### Exceptions and scope

If \(F\) is constant, then \(U,V\) are both constant: a nonconstant
\(U\) produces degree at least three, beyond cancellation by \(V\).
If \(U\) is constant and \(V\) is arbitrary quadratic, taking
\(\Phi=V\) gives the expected one-statistic chart. The same applies
with \(V\) constant and \(\Phi=U\).

Jacobian dependence for a specified statistic is weaker than
composition through that statistic. For example
\(\Phi=r^2,\ U=r,\ V=0\) gives \(J(r^3,r^2)=0\), but no polynomial
\(W\) satisfies \(r^3=W(r^2)\). NR-L2 covers this example through
the affine statistic \(r\); NR-L3 does not incorrectly identify the
two requirements.

## 4. NR-L4 — classified charts cover at most linearly many actual pairs

### Meaning

Many parameter labels do not create many distinct pairs when both
coordinates depend on the same scalar statistic. A fixed-degree
curve can meet a finite Cartesian square in only linearly many of
these pairs. Thus this ansatz fails the complete-square requirement
before any favorable output count can be used.

### Exact statement

**PROVED.** Let \(A\subset\mathbb R\) have \(N\ge1\) distinct elements.
For a chart satisfying any equivalent condition of NR-L2, and for
any parameter domain \(\mathcal D\subseteq\mathbb R^2\), put
\[
\mathcal E=\{(X(r,s),Y(r,s)):(r,s)\in\mathcal D\}\cap A^2.
\]
Then
\[
|\mathcal E|\le2N.
\tag{L10}
\]
For the genuine-quadratic form (L5), the stronger bound is \(N\).
Constant-coordinate and constant-output charts are included.

If \(m\) such charts are combined, their union contains at most
\(2mN\) distinct ordered pairs. Hence near-complete coverage
\[
|\mathcal E|\ge N^2-O(N^{2-\delta})
\]
requires
\[
m\ge N/2-O(N^{1-\delta}).
\tag{L11}
\]
In particular, any bounded or \(o(N)\) number of these charts covers
only \(o(N^2)\) pairs.

### Proof

In case (L4), the coordinates are univariate polynomials
\[
X(t)=\frac{g(t)+f(t)}2,\qquad
Y(t)=\frac{g(t)-f(t)}2,
\]
each of degree at most two. If \(X\) is nonconstant, each value
in \(A\) has at most two real preimages \(t\), so there are at most
\(2N\) possible pairs. If \(X\) is constant, there are at most
\(N\) pairs because their second coordinate belongs to \(A\).
If both are constant, there is at most one pair.
For case (L5), both coordinates are affine in \(t=\Phi(r,s)\);
the same argument gives \(N\). Counting their possible real
statistics bounds every chosen parameter domain, regardless of
projection multiplicities. Summing over charts proves (L11).
\(\square\)

### Why it matters

The formal parameter count can be quadratic or larger, but the
distinct pair count in these charts remains at most \(2N\).
For finitely many charts, at least \(N^2-O(N)\) cross-pairs still
need a separate argument. Their outputs cannot be omitted.

### Scope

This is a no-go theorem for the exact low-degree factorization/Jacobian
ansatz, not for every quadratic map into a Cartesian square.
Maps with \(J(U,V)\ne0\) are outside the ansatz; their finite output
support remains a separate question. Rational charts, higher-degree
statistics, or a linear number of charts are not excluded by (L11).
Indeed \(N\) constant-first-coordinate row charts can trivially
cover \(A^2\); their existence supplies no output saving.

### Sharp degree boundary

Allowing degree three for \(V\) already defeats the algebraic
classification:
\[
U=r,\qquad V=s-r^3,\qquad F=s,\qquad J(U,V)=1.
\tag{L12}
\]
The output factors through the affine statistic \(s\), while the input
map is not one-statistic. Thus NR-L1–L4 do not extend verbatim to
degree three. This identity is not a new positive finite construction.
On the consecutive full grid \(r\in\{1,\ldots,L\}\),
\(s\in\{2b:0\le b<H\}\), its coordinates are
\[
x=b-\frac{r^3-r}{2},\qquad
y=b-\frac{r^3+r}{2}.
\]
This is exactly the frozen GS-P3 family in
../2026-09-21-growing-step-cubic/structure-and-reuse.md, whose
prescribed distinct pair count obeys \(HL\le4N^{4/3}\). Hence that
specialization still covers \(o(N^2)\) pairs. No old search is rerun.
Arbitrary correlated parameter sets are outside that full-grid theorem;
their necessary scalar reuse is not supplied by identity (L12).

## 5. Exact bounded symbolic coefficient calculation

The search space was reduced analytically to all coefficients in the
five normal forms (L6), not to a sample of real coefficients.
For each normal form, an exact six-column coefficient matrix sends
the coefficients of
\[
Q\in\operatorname{span}\{1,r,s,r^2,rs,s^2\}
\]
to those of \(J(Q,\Phi)\). Standard-library rational row reduction
gave the following complete kernels:

| Statistic normal form | Kernel among degree-at-most-two \(Q\) |
|---|---|
| \(r\) | \(\operatorname{span}\{1,r,r^2\}\) |
| \(r^2\) | \(\operatorname{span}\{1,r,r^2\}\) |
| \(r^2+s\) | \(\operatorname{span}\{1,r^2+s\}\) |
| \(r^2+s^2\) | \(\operatorname{span}\{1,r^2+s^2\}\) |
| \(r^2-s^2\) | \(\operatorname{span}\{1,r^2-s^2\}\) |

The generic exceptional identity (L3) was also verified with all of
its coefficients retained as independent indeterminates.
The analytic degree argument and affine normal-form reduction prove
exhaustiveness; no finite computation is substituted for that proof.

**Exact finite symbolic audit: PASS.** One run used **517 charged
coefficient arithmetic operations and identity checks**, below the
declared cap of **5,000**. It checked five kernel systems and one
generic polynomial identity. There were zero scalar/carrier/parameter
grid points and zero floating-point equality tests.

The reviewed standard-library script and full coefficient matrices
are retained in the ignored directory
local-only/runs/T01/2026-09-21-low-degree-symbolic/:

- Command: python3 local-only/runs/T01/2026-09-21-low-degree-symbolic/verify.py
- Runtime: Python 3.12.7.
- CPU time: 0.001122 seconds.
- Code SHA-256:
  29f7138f1c5267c1cda2ad3fee5e2144abf6375cbd51ae982adaa4dd415fc3cc.
- Complete output: result.json in that directory.
- Output SHA-256:
  801feaa65517a02f5787c3c6bdeac8ce18da48dec03a7e55a6e2bbf2581a27d1.

The script was inspected before execution. Its operation counter
charges coefficient additions, multiplications, divisions, negations,
and six final identity checks; exponent bookkeeping and file hashing
are not coefficient arithmetic. No numerical or field search occurred.

## 6. Full-square accounting and claim records

These charts use exactly the scalar set \(A\) of size \(N\) in both
coordinates. Parameter descriptions are never counted as distinct
pairs or scalars. If a finite parameter grid has \(Q_{\rm labels}\)
labels but its chart satisfies (L10), its average multiplicity onto
distinct represented pairs is at least \(Q_{\rm labels}/(2N)\)
when all labels give pairs in \(A^2\). This multiplicity cannot be
credited as scalar or output compression.

For \(m\) charts, the unrepresented pair count is at least
\((N^2-2mN)_+\), even before overlaps reduce the chart union.
The safe completion inequality remains
\[
|P(A,A)|\le |P(\mathcal E)|+(N^2-|\mathcal E|).
\]
No claim about the full image follows from a small
\(|P(\mathcal E)|\) when this complement is quadratic.
In an exponential ledger, distinct chart pairs have exponent at most
the scalar exponent \(a\) for a fixed number of charts, not the
required \(2a\). A large parameter-label exponent does not change that.

The only projection costs here are the explicitly counted parameter
fibers and chart count. All coefficients are real and arbitrary;
there is no field degree, denominator restriction, modulus, splitting,
regulator, digit carry, input thinning, or exceptional-output deletion.
Affine normal-form changes are proof coordinates, not a change to the
fixed cubic target or an uncharged transport of scalar sets.

| ID | Status and exact scope | Evidence locator and dependencies | Retained limit |
|---|---|---|---|
| NR-L1 | PROVED; all real \(U,V,\Phi\), degree at most two, \(\Phi\) nonconstant | §1, degree separation and explicit coefficient identity | No higher-degree/rational extension asserted |
| NR-L2 | PROVED; complete all-coefficient classification of the Jacobian ansatz | §2, five exhaustive affine normal forms and NR-L1 | Finite cardinality does not imply this ansatz |
| NR-L3 | PROVED; exact polynomial composition through specified affine/quadratic statistics | §3, NR-L1/L2 and leading-degree comparison | Jacobian dependence need not be composition through the specified statistic |
| NR-L4 | PROVED; every finite real \(A\), every parameter domain and chart inventory | §4, univariate root counting and NR-L2 | \(o(N)\) such charts cannot cover nearly all pairs; other charts remain open |

All claims are T01, the fixed plus-sign cubic, 2026-09-21 v1.
The proof evidence is the complete internal argument above, accompanied
by the exact bounded coefficient check. The coordinating agent
independently reviewed NR-L1–L4, including the normal forms, coefficient
exception, composition degree comparison, constant cases, and distinct
pair counts, and found no mathematical gap. A second independent
review by the parallel obstruction agent also found no gap in the
displayed NR-L1–L4 proofs; that review did not rerun or audit the
symbolic script. These internal proof audits are separate from the
finite symbolic calculation. No external result, unavailable
historical proof, novelty claim, or external peer review is used.
The original cubic target remains OPEN.
