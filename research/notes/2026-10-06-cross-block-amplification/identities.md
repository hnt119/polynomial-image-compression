# Quadratic-phase shifts: exact targets and collapsed orbit labels

6 October 2026 · version 1 · T03 · fixed polynomial
\(Q(x,y)=x^2+xy+y^2=N(x-\omega y)\),
\(\omega=e^{2\pi i/3}\).

## 1. Authorization, claim, and scope

This is the explicitly authorized offline **Cross-Block Fiber Amplification
Beyond Spreading** cycle. The lead approved the quadratic-phase rule below
as direction 2's sole preselection finalist and froze it when its amplitude
cosets collapsed. There is no replacement, mutation, or search of a third
mechanism. In particular, neither frozen rule from the previous cycle nor
its FG-O1 matching-classification question is reopened.

**AMP-G1 / PROVED.** For every \(q=7^r\), the amplitudes in (1) have
exactly eight distinct cosets modulo \(\mu_{6q}\), regardless of their
\(8q\) formal labels. Their whole-scalar phase-shift identity is exact,
with certified targets in the encoded orbit union. For \(q>1\) the rule
fails the prescribed \(8q\) disjoint-coset condition before establishing
any general cross-block membership formula.

**FAILED IN STATED SCOPE:** this formula's required amplitude inventory.
The encoded-only coverage estimate below is a certificate deficit, not a
full-return upper bound and not an actual-image lower bound for its
deduplicated completion.

**Evidence:** complete elementary symbolic derivation. The lead approved
the precise formula and stopping gate before this note was written.
The independent audit is recorded separately by the lead. This author
executed no mathematical program, used no experimental data, and made
no network request. No external theorem or novelty claim is imported.

**Sources and distinctions:**

- [ML-4](../2026-09-30-modular-lift/proofs.md), §4, supplies the prescribed
  inventory of \(8q\) primitive modular orbits with \(6q\) points each.
- [Latest fiber-growth report](../2026-10-06-fiber-growth/README.md),
  §§1–4, supplies the frozen state and its two scoped failures. The current
  rule is neither the phased-binomial carrier nor its relative-norm rule.
- `research/templates/CONSTRUCTION_LEDGER.md` supplies the accounting
  categories in §6. The quadratic exponential-sum calculation is proved
  here by a finite change of variables, without an imported Gauss-sum
  evaluation theorem.

## 2. One explicit amplitude rule

Fix an integer \(r\ge0\), set
\(q=7^r\), \(m=6q\),
\(\zeta=e^{2\pi i/m}\), \(\xi=\zeta^6\), and
\(K=\mathbb Q(\zeta)\). For each \(j\in\mathbb Z/q\mathbb Z\),
put

\[
G_j=\sum_{a\in\mathbb Z/q\mathbb Z}\xi^{a^2+ja},
\qquad
c_{h,j}=hG_j\quad(1\le h\le8).
\tag{1}
\]

These are exactly \(8q\) formal amplitude labels, all in K. The
amplitude and angular phase are coupled through the entire residue sum;
no independent coordinate rotations, auxiliary radical tags, or
depth-dependent separated rational scales occur.

For \(q>1\), choose \(e\in\mathbb Z/q\mathbb Z\) with
\(4e=1\). Completing the square and translating the summation variable
gives

\[
a^2+ja=(a+j/2)^2-j^2/4,
\qquad
\boxed{G_j=\xi^{-e j^2}G_0.}
\tag{2}
\]

The fractions in this identity denote inverses in the residue ring,
not real fractions in the exponent. At \(q=1\), there is one residue
and every sum is 1; all conclusions hold directly.

To prove nonvanishing without evaluating the sign or argument of G_0,
compute

\[
|G_0|^2
=\sum_{a,b\bmod q}\xi^{a^2-b^2}
=\sum_{u,v\bmod q}\xi^{uv}
=q.
\tag{3}
\]

The middle change of variables is \(u=a-b,v=a+b\), a bijection
because q is odd. For \(u=0\), the inner sum over v is q. For
each nonzero u, it is zero: the ratio \(\xi^u\ne1\) has q-th
power 1, so its finite geometric sum vanishes. This works for every
odd prime power, including nonunit nonzero values of u. Thus all
\(G_j\ne0\) and \(|G_j|^2=q\).

## 3. Exact whole-scalar target map

Fix a label j and let \(s\in\mathbb Z/q\mathbb Z\). For q>1,
define

\[
u_{j,s}=\xi^{-e(2js+s^2)}.
\tag{4}
\]

At q=1, take the single action \(u_{0,0}=1\).

Then \(|u_{j,s}|=1\), and (2) gives the exact identity

\[
u_{j,s}G_j=G_{j+s}.
\tag{5}
\]

Write \(\Delta=\omega-\bar\omega=1+2\omega\), and define real
coefficients

\[
\beta_{j,s}=\frac{u_{j,s}-\bar u_{j,s}}{\Delta},
\qquad
\alpha_{j,s}=u_{j,s}-\omega\beta_{j,s}.
\tag{6}
\]

They belong to \(K\cap\mathbb R\), and
\(u_{j,s}=\alpha_{j,s}+\beta_{j,s}\omega\). The actual pair map is

\[
T_{j,s}(x,y)=
\bigl(\alpha_{j,s}x+\beta_{j,s}y,
-\beta_{j,s}x+(\alpha_{j,s}-\beta_{j,s})y\bigr).
\tag{7}
\]

Multiplication of \(x-\omega y\) by \(u_{j,s}\) proves
\(Q(T_{j,s}(x,y))=Q(x,y)\) for every real pair. If the source
has the explicit encoded representation

\[
x-\omega y=hG_j\zeta^a,
\]

then its target has the representation

\[
T_{j,s}(x,y)_1-\omega T_{j,s}(x,y)_2
=hG_{j+s}\zeta^a.
\tag{8}
\]

Both decoded target coordinates therefore lie in the same scalar
completion defined below. This is the precise certified membership
condition. No representation of a generic completed pair by a single
\(hG_j\zeta^a\) is assumed.

The q shift parameters do not necessarily label distinct actions:
\(s\) and \(-2j-s\) have the same exponent in (4). More
fundamentally, every action in (4) already belongs to \(\mu_q\),
and all the j-addresses in (8) already lie in one cyclic orbit for each h.
At a nonzero complex source distinct actual multipliers give distinct
targets, but repeated phase labels give no additional target.

## 4. Exactly eight amplitude cosets and the failed lift

By (2), for each fixed h,

\[
c_{h,j}\mu_m=hG_0\mu_m
\qquad(j\bmod q).
\tag{9}
\]

The eight resulting cosets are distinct. Their complex norms are
\(h^2q\), which differ for \(1\le h\le8\), whereas multiplication
by \(\mu_m\) does not change norm. Hence there are **exactly eight**
actual cosets, rather than the required \(8q\).

Let

\[
\mathcal Z_q=\bigcup_{h=1}^8\bigcup_{j\bmod q}c_{h,j}\mu_m
=\bigcup_{h=1}^8 hG_0\mu_m.
\tag{10}
\]

Every point is nonzero, the eight orbits are disjoint, and each has m
points. Thus \(|\mathcal Z_q|=8m=48q\). The formal paired encoding
has \((8q)m=48q^2\) labels. Every actual point has exactly q such
labels: for each j there is exactly one compensating rotation exponent
modulo m. Any injective restriction of this formal map therefore retains
at most a fraction \(1/q\) of its pair labels.

This violates the prescribed disjoint-coset gate for every \(r\ge1\).
The r=0 base case has q=1 and meets the inventory, but cannot supply
the required asymptotic family. Dense summation support in (1) does not
prevent exact phase identities from collapsing the labels.

## 5. Actual scalar completion and certified coverage only

For \(z\in K\), let its real coordinates be

\[
\pi_y(z)=\frac{\bar z-z}{\Delta},
\qquad
\pi_x(z)=z+\omega\pi_y(z).
\tag{11}
\]

Put \(A_q=\pi_x(\mathcal Z_q)\cup\pi_y(\mathcal Z_q)\) and
\(n=|A_q|\). Since \(\mathcal Z_q\) is invariant under multiplication
by \(\omega\), and \(M_\omega(x,y)=(y,-x-y)\), its two coordinate
projections agree. Thus A_q is already either one of these projections.

On the nonzero ellipse \(Q(x,y)=q\), a fixed x-value has at most
two possible y-values. The first orbit in (10) has m distinct points,
so it supplies at least m/2 distinct scalar values. The entire first
projection has at most \(8m\) labels. Therefore

\[
3q\le n\le48q.
\tag{12}
\]

These are actual distinct-scalar bounds, not amplitude-label counts.
No exact leading constant is needed. In native depth r they give
\(n=7^{r+o(r)}\).

The decoded set \(E_q=\pi(\mathcal Z_q)\) has exactly \(48q\)
ordered pairs in \(A_q^2\). At each of these sources the whole group
\(\mu_m\) gives m distinct targets still in E_q. Thus the action
identity and its growing returns are genuine on the certified set.
But its coverage is bounded by

\[
\frac{|E_q|}{n^2}\le\frac{48q}{9q^2}
=\frac{16}{3q}\longrightarrow0.
\tag{13}
\]

Equivalently, the present membership certificate leaves at least
\(n^2-48q\) completed pairs uncovered. This does **not** say those
pairs have no incidental returns, few full-fiber targets, or distinct
Q-values. The selected-return count and complete image on those pairs
are not determined by this note. The rule has already stopped at the
coset gate, without exhibiting a general cross-block membership formula.

## 6. Arithmetic and rate ledger

| Item | Exact accounting |
|---|---|
| Required inventory | 8q disjoint amplitude cosets, each with 6q points |
| Actual inventory | Exactly 8 cosets and 48q points; each formal encoded point has q labels |
| Paired-encoding loss | An injective restriction retains at most 1/q of pair labels; no unproved scalar thinning rule is inferred |
| Actual scalar growth | 3q≤n≤48q, so native-depth input factor is 7 |
| Scalar projection fibers | At most 2 on each ellipse; different ellipses may reuse values, and the bounds (12) allow all such coincidences |
| Same-set norm identity | (7) preserves Q on every real pair; (8) proves membership on E_q only |
| Distinct actions and stabilizers | Distinct μ_m actions are free at every encoded nonzero point; duplicate shift labels in (4) are identified; the origin, if present in A_q², has one target |
| Certified rich population | Exactly 48q encoded pairs, each with 6q group returns; coverage is O(1/q) |
| Uncovered pairs | At least n²−48q outside the proved membership domain; no upper bound on their actual returns is asserted |
| Field degree | For r≥1, [K:Q]=12·7^(r−1); at r=0, [K:Q]=2 |
| Amplitude integrality | G_j is a sum of roots of unity; every c_(h,j) is an algebraic integer |
| Coordinate denominators | Δ²=−3, so 3π_x(z) and 3π_y(z) are algebraic integers for every integral encoded z |
| Heights and archimedean size | Every conjugate of G_j has absolute value sqrt(q), by the same orthogonality argument with a unit quadratic coefficient; every encoded conjugate has modulus at most 8sqrt(q), and each scalar conjugate has absolute value at most 16sqrt(q)/sqrt(3) |
| Discriminant and regulator | Not evaluated or set to zero; no bound involving either is needed by this equality obstruction |
| Local moduli, splitting, carries | No local density or carry saving is invoked; q indexes one exact cyclic sum |
| Branch/state counts | The q quadratic-phase addresses collapse inside each of the eight orbits |
| Return and output rates | Growing returns are proved only on E_q; no generic ρ, bad-tail δ, full-image bound, or positive saving c is established |
| Evidence | Complete symbolic proofs; no mathematical program, finite scout, network request, or external result |

The formula is frozen at this gate. This note neither repairs its
amplitudes nor starts a new search. The lead's combined report records
the other approved mechanism, final checks, and the retained project
obligation separately.
