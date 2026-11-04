# Nonlinear coordinate reuse for the plus-sign cubic

**T01 · 21 September 2026 · version 1 · offline research**

\[
P(x,y)=(x-y)^3+x+y.
\]

This is the commissioned continuation of
[Sublinear cubic symmetries](../2026-09-21-sublinear-cubic/README.md).
It prioritizes direct scalar reuse and direct full-image support.
The old graph obligation remains open; a small symmetry inventory is
not required by this cycle.

## 1. Short verdict

**OPEN:** no full cubic construction or near-complete compressed chart
was found.

**PROVED:** the cycle obtained two substantial scoped classifications
and a rational-grid obstruction:

- For all real \(U,V\) of total degree at most two, exact output
  dependence on an affine or quadratic polynomial statistic forces the
  pair itself through one parameter. Each such chart supplies at most
  \(2N\) distinct pairs in an \(N\)-point scalar square.
- For two fixed cubic output fibers, all nonconstant polynomial and
  rational coordinate-sharing identities are classified, with no degree
  restriction. Rational nonlinear exceptions exist, but only for an
  explicit ellipse and two exceptional first-coordinate cubic curves.
- Independently prescribing one scalar and the output by nonconstant
  rational functions admits no rational formula for the other scalar.
  For degree at most \(d\), each orientation has at most
  \(7d\max(|R|,|S|)\) working labels on a parameter grid.

These fulfill a bounded-degree classification outcome within explicit
hypotheses, together with a further exact reduction. They do not rule
out arbitrary finite-set compression, varying-output correspondences,
or nonrational algebraic branches.

The best genuine cross-output rational family has \(2m\) selected
pairs, between \(m\) and \(3m\) scalar inputs, and only two selected
outputs. Its selected pairs cover \(O(1/m)\) of the full square.
Thus the nonlinear identity is real, but its useful reuse rate fails.

## 2. The coordinate-reuse problem in ordinary language

The goal is to reuse a small pool of scalars across almost every ordered
pair while making many of those pairs share outputs.

These are different requirements. Any full Cartesian square already
has \(N^2\) distinct pairs built from \(N\) scalars. Relabeling its rows
nonlinearly does not change its output set. Conversely, a rational curve
can produce many pairs with one output while requiring almost one new
scalar per pair.

For example, \(x=r^2,y=s^2\), with signed integer labels, has repeated
descriptions because \(r\) and \(-r\) give the same scalar. Deduplicating
the actual pairs removes that apparent gain. The report therefore uses
\(Q_0\) for labels, \(Q\) for distinct selected pairs, \(N\) for scalars,
and \(Z\) for selected outputs.

Full-square scalar reuse alone is not claimed as a structural breakthrough;
it must coexist with the output and completion estimates.

## 3. Exact correlated \((u,L)\) formulation

The frozen bijection is
\[
u=x-y,\qquad L=x+y,\qquad
x=(L+u)/2,\quad y=(L-u)/2.
\]
For an actual scalar set \(A\),
\[
\Omega_A=\{(u,L):(L+u)/2\in A,\ (L-u)/2\in A\},
\quad |\Omega_A|=N^2,
\]
\[
P(A,A)=\{u^3+L:(u,L)\in\Omega_A\}.
\]

A proposed chart \(u=U(r,s),L=V(r,s)\) gives
\[
X=(V+U)/2,\qquad Y=(V-U)/2,\qquad F=U^3+V.
\]
Its parameter domain is not identified with the square until the actual
pair image is counted. Independent difference-set and sumset membership
still cannot replace the two scalar membership conditions.

## 4. Necessary quantitative rates

For a finite parameter domain \(T\), set
\[
Q_0=|T|,\quad E=\{(X(t),Y(t)):t\in T\},\quad Q=|E|,
\quad A=\pi_1(E)\cup\pi_2(E),\quad N=|A|,\quad Z=|P(E)|.
\]
The exact safe bound, restated and proved as NR-A1, is
\[
\boxed{|P(A,A)|\le Z+(N^2-Q).} \tag{1}
\]
Parameter multiplicities sum to \(Q_0\); the distinct selected pairs
have \(2Q\) scalar occurrences and average reuse \(2Q/N\).
Every actual fiber has at most \(N\) pairs, so \(Q\le NZ\).

In an exponential ledger, \(Q=e^{qm+o(m)}\),
\(N=e^{am+o(m)}\), \(Z=e^{bm+o(m)}\) require \(q=2a\) and
\(b<2a\) for this route, but even these exponent conditions are not enough:
\(Q=N^2/2\) has \(q=2a\) while leaving a quadratic complement.
The actual requirement is
\[
N^2-Q=O(N^{2-\delta}),\qquad Z=O(N^{2-\varepsilon})
\tag{2}
\]
for fixed positive \(\delta,\varepsilon\), or another proved support
bound on the complement. Every exponent strictly below
\(\min(\delta,\varepsilon)\) then absorbs the constants in (1).

## 5. Coordinate-sharing equations and their complete rational classification

Write \(c_s(z,u)=(z-u^3+su)/2\), \(s=\pm1\), so that \(c_+=x_z\)
and \(c_-=y_z\). Fixed-output sharing is
\[
c_s(z,u)=c_t(w,v)
\iff u^3-v^3-su+tv=c,\qquad c=z-w. \tag{3}
\]

**Meaning.** Nonlinear matching really can exist, but not for every
pair of fixed output fibers or every choice of coordinate positions.

**Exact statement — PROVED, NR-C1–C4.** Nonconstant real polynomial
solutions, in any finite number of parameters and of any degree, only
give \(u=v,\ s=t,\ c=0\). For rational functions the complete list is:

| Coordinates | Output difference | Nonconstant rational image |
|---|---|---|
| Second / second | \(c=0\) | Diagonal only |
| First / first | \(c=0\) | Diagonal or \(u^2+uv+v^2=1\) |
| First / first | \(c=\pm4/(3\sqrt3)\) | Explicit singular cubic chart |
| Mixed first / second | Any real \(c\) | None |
| All other fixed-output cases | — | None |

**Proof.** For polynomials, compare leading degrees in
\((u-v)(u^2+uv+v^2)=su-tv+c\). Unless \(u=v\), the left side
has too high a degree.

For rational maps, first locate all complex singularities using
\(3u^2=s,\ 3v^2=t\). Outside the listed exceptions the rational
differential
\[
\omega=\frac{du}{t-3v^2}
\]
would be nonzero and have no pole at any parameter value. At a common
pole of order \(n\), its order is \(n-1\ge0\); at finite nonsingular
images, the implicit derivative gives regularity. But a nonzero rational
differential on a rational parameter line must have a pole, including
possibly at infinity. The companion proves this directly by polynomial
degree, without importing a genus theorem. The exceptional curves are
parametrized by lines through a known point. Restricting several rational
parameters to a suitable real line gives the same case list.

**Why it matters.** This extends the old affine restriction to all
polynomial degrees and classifies every rational fixed-output identity.
The surviving exceptional cubics are genuine nonlinear families.

**Scope.** This is not a bound on real points or arbitrary finite
correspondences. All these curves have infinitely many real points.
Varying output differences and nonrational algebraic branches remain
outside the theorem. Full proof, charts and exceptional real points:
[rational-reuse-curves](rational-reuse-curves.md).

## 6. Low-degree symbolic classification

**Meaning.** In the degree-two model, compressing the output through
one low-degree statistic also collapses the input pairs onto a curve.
The formal two-parameter grid therefore cannot provide quadratic pair
coverage.

**Exact statement — PROVED, NR-L1–L4.** Suppose
\(\deg U,\deg V\le2\). For every nonconstant polynomial \(\Phi\)
of degree at most two,
\[
J(U^3+V,\Phi)=0
\Longrightarrow J(U,\Phi)=J(V,\Phi)=0,
\quad J(A,B)=A_rB_s-A_sB_r. \tag{4}
\]
Existence of such a statistic is equivalent to \(J(U,V)=0\).
All solutions have one of two forms:
\[
U=f(\ell),\quad V=g(\ell),\quad \deg f,\deg g\le2,
\tag{5}
\]
for a nonconstant affine form \(\ell\), or
\[
U=a\Phi+b,\quad V=c\Phi+d
\tag{6}
\]
for a quadratic \(\Phi\) that is not a polynomial in one affine form.
Every such chart meets any \(A^2\) in at most \(2N\) distinct pairs;
case (6) has at most \(N\).

Consequently, \(J_0\) such charts satisfy
\[
Q\le2J_0N,\qquad
Q\ge N^2-O(N^{2-\delta})
\Longrightarrow
J_0\ge N/2-O(N^{1-\delta}). \tag{7}
\]

**Proof.** Differentiate:
\(3U^2J(U,\Phi)+J(V,\Phi)=0\).
If \(\deg U=2\), degree separation forces both Jacobians to vanish.
For linear \(U\), the one possible constant-Jacobian exception is
eliminated by an explicit coefficient comparison.
Affine changes reduce every statistic to one of
\[
r,\quad r^2,\quad r^2+s,\quad r^2+s^2,\quad r^2-s^2.
\]
Solving the six-coefficient Jacobian equations gives precisely (5)–(6).
For the pair count, fix its first scalar: a nonconstant univariate
quadratic has at most two preimages; a constant first coordinate has
at most \(N\) possible partners. Sum over charts.

**Why it matters.** This is an exhaustive all-real-coefficient result
for the stated ansatz, not a finite sample of coefficient choices.
The exact symbolic check verified all five normal-form kernels and
the remaining coefficient identity in 517 charged operations.

**Scope.** Small finite output cardinality is not assumed to imply
a vanishing Jacobian or factorization. The specified-statistic distinction
also matters: \(r^3\) has zero Jacobian with \(r^2\), but is not a
polynomial in \(r^2\). The companion separately classifies exact
\(F=W(\Phi)\) compositions.

The degree cutoff cannot be dropped: \(U=r,\ V=s-r^3\) has
\(F=s\) and \(J(U,V)=1\). Its consecutive full-grid specialization
is the previously closed GS-P3 model, not a positive new construction.
Complete proof and symbolic audit:
[low-degree-classification](low-degree-classification.md).

## 7. Best genuine nonlinear parametrization found

**Meaning.** The exceptional cubic allows two different output fibers
to share a scalar for every parameter value.

**Exact statement — PROVED, NR-P1.** Put \(a=1/\sqrt3,\ z=0,\ w=4a/3\).
For \(t>1\), let
\[
u=a\left(1+\frac{3(1+t^2)}{t^3-1}\right),\qquad
v=a\left(-1+\frac{3t(1+t^2)}{t^3-1}\right).
\tag{8}
\]
Then \(x_z(u)=x_w(v)\).
Taking both corresponding pairs at \(t=2,\ldots,m+1\) gives exactly
\(Q=2m\) pairs on two outputs, with \(m\le N\le3m\).

**Proof.** Substitute \(u=a+h,\ v=-a+th\) into
\(u^3-u-v^3+v=-4a/3\). It factors as
\(h^2(3a(1+t^2)+(1-t^3)h)=0\).
The nonzero branch is (8). Both differences strictly decrease for
\(t>1\), so each output supplies \(m\) distinct pairs. Its second
coordinate is strictly monotone, giving \(N\ge m\); the common first
coordinate gives \(N\le3m\).

**Why it matters.** This is an exact nonlinear cross-output family,
outside SC-R2/R3. It is not merely a one-off coincidence.
Its pair/scalar/selected-output rates in depth \(\log m\) are
\[
q=1,\qquad a_{\rm input}=1,\qquad b_{\rm selected}=0.
\]
These quantify the failure: \(Q/N^2\le2/m\to0\), despite constant
selected support.

**Scope.** Only the prescribed coverage certificate is FAILED.
The actual full-image asymptotic of this scalar family is not determined.
The curve also has an isolated real singular point, a pole in the slope
chart and a separate vertical-limit point; these are handled in the
classification companion, not silently dropped. The selected \(t>1\)
family avoids them. Full counts:
[chart-capacity-and-completion, NR-P1](chart-capacity-and-completion.md).

## 8. Full-square completion audit

For the proved family above, (1) gives only
\[
|P(A_m,A_m)|\le2+N^2-2m.
\]
This is a linear saving in a quadratic upper certificate, not a
fixed power saving and not an actual-image asymptotic theorem.

The finite chart audits make the same distinction concretely:

| Chart | \(N\) | Labels \(Q_0\) | Distinct pairs \(Q\) | Selected outputs \(Z\) | Uncovered pairs | Actual full image |
|---|---:|---:|---:|---:|---:|---:|
| Same-output conic, two translates | 10 | 20 | 10 | 2 | 90 | 83 |
| Distinct-output cubic, two translates | 18 | 16 | 14 | 4 | 310 | 306 |
| Conic, with full complement added | 10 | 110 | 100 | 83 | 0 | 83 |
| Cubic, with full complement added | 18 | 326 | 324 | 306 | 0 | 306 |

Adding transposes and diagonals also remains sparse. Adding the full
complement supplies complete scalar coverage but restores the full output
cost. Every selected/outside collision and every entirely new outside
output is retained in the exact records.

## 9. Best broader rational obstruction

**Meaning.** A rational nonlinear grid cannot independently prescribe
one input scalar and the output, then fill in the other scalar rationally.

**Exact statement — PROVED, NR-G1/G2.** For nonconstant real rational
\(X(r),Z(s)\), there is no rational \(Y(r,s)\) satisfying
\[
P(X(r),Y(r,s))=Z(s),
\quad\text{or}\quad P(Y(r,s),X(r))=Z(s)
\tag{9}
\]
as an identity. If all numerator/denominator total degrees are at most
\(d\), then for each orientation separately the number of defined labels
satisfying its equation on \(R\times S\) is at most
\[
\boxed{7d\max\{|R|,|S|\}.} \tag{10}
\]

**Proof.** Specialize two generic output-parameter values in a putative
identity. They would give rational fixed-output coordinate sharing at
a nonexceptional output difference, contradicting NR-C2. Clearing the
denominators in a finite-grid equation produces a nonzero polynomial of
total degree at most \(7d\). Counting its roots row by row proves (10).

**Why it matters.** This is not restricted to quadratic rational maps.
It also controls finite exceptions on large grids, with all constants
and denominator exclusions explicit.

**Scope.** The independently prescribed coordinates are one scalar
and the output. Arbitrary rational parametrizations of the two original
inputs are not excluded. Small finite support does not imply this
independence. Proof and the general bounded rational-curve library bound:
[chart-capacity-and-completion](chart-capacity-and-completion.md).

## 10. Exact finite experiments

One approved grid tested 16 chart records on 12 distinct normalized
carriers, with maximum \(N=18\). It included nonlinear row-permutation
controls, many-to-one square maps, output-forced low-degree expressions,
rational conic charts, exceptional cubic charts and multi-chart
completion audits.

The chart grid used 924 cached full-square polynomial evaluations,
6,298 charged checks and 0.036732 research CPU seconds. Sparse families
stopped at the declared minimal examples; no closed search was restarted.
The exact symbolic run used 517 coefficient operations/checks, no carrier
grid and no floating-point equality.

For the exceptional cubic, physical scalars are \(hB\), \(h=1/\sqrt3\).
The exact identity
\[
P(hx,hy)/h=(x-y)^3/3+x+y
\]
permits rational coefficient arithmetic for the same fixed polynomial;
it is not a changing-polynomial construction.

The [complete finite table](experimental-summary.md) and
[portable results](../../../examples/2026-09-21-nonlinear-reuse.json)
include projection multiplicities, coverage fractions, actual fiber
histograms, maximum fibers, scalar reuse, selected/outside collisions
and full completion. These are EXPERIMENTAL finite records, not
asymptotic evidence promoted to proof.

## 11. Gain-versus-cost ledger

The [full ledger](construction-ledgers.md) follows the repository template.
Its essential distinctions are:

| Model | Distinct-pair rate | Actual scalar count | Output and completion cost |
|---|---|---|---|
| Classified degree-two charts | At most \(2J_0N\) | Exact scalar pool \(N\) | \(o(N)\) charts leave a quadratic complement |
| Bounded-degree rational curve library | At most \(dJ_0N\) | Exact scalar pool \(N\) | Chart count and degree cannot be free |
| Exceptional two-output family | \(Q=2m\) | \(m\le N\le3m\) | Selected \(Z=2\), uncovered \(N^2-\Theta(N)\) |
| Independent scalar/output rational grids | At most \(7d\max(|R|,|S|)\) working labels per orientation | Must still deduplicate scalars | Most labels fail the equation on comparable large grids |
| Full-square nonlinear reindexing | \(Q=N^2\) | No change | Full output support unchanged |
| Finite conic/cubic completions | Exact recorded \(Q_0,Q,N\) | Every projection fiber retained | Complement outputs counted exactly |

No unknown scalar projection loss, chart overlap or denominator cost is
assigned zero. No positive net rate survives. No field tower, prescribed
splitting, regulator, norm/trace amplification, digit carry scheme or
external theorem is used.

## 12. Implication for T01

**T01 remains OPEN.** This cycle proves substantial classifications within
the commissioned degree and rational-identity scopes. It finds a genuine
nonlinear cross-output identity, but its scalar reuse is quantitatively
too weak for near-full coverage.

The general nonlinear direct-support problem remains unresolved.
The earlier CR-O1 graph witness also remains OPEN, but a sublinear step
inventory is not imposed on the current direct-chart obligation.
Neither the cubic sign nor the same-set/full-square target changed.
Other tracks and the separate T01 quadratic benchmark are unchanged.

All major new proofs were independently audited internally.
[Verification](verification.md) distinguishes those proof audits from
the exact finite computations, source hashes and repository regressions.
The unavailable historical digital/rich-fiber originals remain unavailable
and were not reconstructed or used as proof dependencies.

## 13. Claim ledger

Every entry is T01 / nonlinear coordinate reuse, the fixed polynomial
at the top, date/version 2026-09-21 v1. Precise quantifiers, hypotheses
and complete proofs are at the named sections. Verification records
audit scopes and hashes. No novelty or external review is claimed.

| ID | Status and scope | Evidence / dependencies | Retained boundary |
|---|---|---|---|
| NR-A1 | PROVED; all finite chart label maps | chart-capacity first section; exact completion and elementary fiber count | No construction |
| NR-A2 | PROVED; bounded-degree rational one-parameter libraries | chart-capacity second section; root count | Two-dimensional pair maps outside |
| NR-P1 | PROVED; all integers \(m\ge1\), exceptional two-output family | chart-capacity third section; exact factorization and monotonicity | Only linear prescribed coverage; full image unclassified |
| NR-C1 | PROVED; polynomial fixed-output sharing, every degree and parameter count | rational-reuse §1; leading terms | Varying outputs outside |
| NR-C2 | PROVED; complete fixed-output rational case list | rational-reuse §2; singularity and differential calculation | Nonrational branches and finite point selections outside |
| NR-C3/C4 | PROVED; full exceptional charts and rational several-parameter extension | rational-reuse §§3–4; slope and specialization | Scalar/completion counts require separate proof |
| NR-L1/L2 | PROVED; all-coefficient degree-two Jacobian ansatz | low-degree §§1–2; degree and normal forms | No cardinality-to-identity inference |
| NR-L3/L4 | PROVED; specified polynomial composition and \(2N\) chart capacity | low-degree §§3–4; coefficient/root count | Higher degree and growing chart libraries outside |
| NR-G1/G2 | PROVED; rational independent scalar/output completion and finite-grid bound | chart-capacity final theorems; NR-C2 and root count | Nonconstant independent coordinates essential |
| NR-X1 | EXPERIMENTAL; 16 declared chart audits, 12 carriers | finite companion and portable JSON | No asymptotic conclusion |
| NR-X2 | EXPERIMENTAL exact symbolic audit; five kernels and one identity | low-degree §5 and retained symbolic result | Exhaustiveness proved analytically, not inferred from a sample |
| NR-O1 | OPEN; near-full direct-chart witness | §15 | Scalar/output rates not achieved simultaneously |

## 14. Failure and scope ledger

| Proposal or inference | Disposition |
|---|---|
| Higher-degree polynomial matching of two fixed coordinate templates produces a new family | FAILED beyond the identical diagonal, by NR-C1 |
| Every rational fixed-output sharing curve is rigid | FAILED assertion: the conic and exceptional cubics are explicit exceptions |
| The exceptional cubic identity alone yields quadratic useful reuse | FAILED prescribed family: \(Q=2m,\ N=\Theta(m)\) |
| Degree-two output rank reduction keeps two-dimensional pair coverage | FAILED in the exact affine/quadratic-statistic ansatz |
| A library of rational one-parameter charts with \(dJ_0=o(N)\) covers nearly all pairs | FAILED by the \(dJ_0N\) capacity bound |
| Independent rational scalar/output grid can be filled rationally | FAILED under NR-G1/G2's explicit nonconstant hypotheses |
| Nonlinear row permutations or sign-label duplicates compress outputs | FAILED inference: reindexing and duplicate descriptions do not change support |
| Full completion preserves the small selected-output count | FAILED in the audited conic/cubic examples; the complement adds most outputs |
| Degree-two classification applies verbatim at degree three | FAILED inference; \(U=r,V=s-r^3\) is an explicit counterexample |
| Arbitrary rational/real nonlinear reuse cannot work | OPEN; not proved or asserted |

## 15. Exactly one next proof obligation

**NR-O1 / OPEN — a near-complete nonlinear direct-support chart.**
Construct explicit arbitrarily large finite real sets \(A_N\), \(|A_N|=N\),
and explicitly parametrized subsets \(E_N\subseteq A_N^2\), with fixed
\(\delta,\varepsilon>0\), such that
\[
\boxed{|A_N^2\setminus E_N|=O(N^{2-\delta}),\qquad
|P(E_N)|=O(N^{2-\varepsilon}).}
\]
Prove the distinct scalar and pair counts, every parameter/projection
multiplicity, chart overlap and the entire complement bound. Chart degrees
and chart counts, whether fixed or growing, must be charged; one cannot
use a formal one-statistic description in place of these counts.
Equation (1) then gives the cubic power saving.

This is the single adopted next obligation for the nonlinear-reuse
direction. It does not require a symmetry inventory. The older graph
subcase remains unresolved, and no additional research is launched by
recording this obligation.
