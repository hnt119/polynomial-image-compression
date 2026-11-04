# Independent full-fiber and quantifier audit

11 October 2026 · version 1 · T03 · independent internal auditor.
Fixed polynomial: \(Q(x,y)=x^2+xy+y^2\).

**Verdict: PASS.** The written tower argument proves the exact frozen
BFF-O1 obligation, and in fact proves a fixed constant bound on complete
fibers for the required source population. Consequently this unchanged
balanced-factor carrier has actual quadratic image size at every sufficiently
large depth. This is a scoped carrier obstruction, not a solution or a
universal impossibility theorem for T03.

This audit independently checked the new symbolic arguments identified below.
It ran no mathematical program, finite scout, rank enumeration, network
request, or nested agent. Its allocation and usage are **0 evaluations and
0 research-program CPU seconds**. Earlier finite results and earlier audit
acceptance are not counted as new verification in this cycle.

## 1. Obligation, sources, and status

The controlling obligation is the frozen
[BFF-O1 statement](../2026-10-11-balanced-full-fibers/README.md), §7.
For the unchanged carrier, put \(q=7^r\), and retain its deduplicated sets
\(B_r,D_r,V_r,A_r\) and complete key \(\mathcal K\). The exact assertion is

\[
\exists C\ge0\ \exists r_0\ \forall r\ge r_0:
\quad
\#\left\{(v,w)\in B_r^2:
\#\{(s,t)\in V_r^2:\mathcal K(s,t)=\mathcal K(v,w)\}
\le(r+1)^C\right\}\ge32q^4.
\tag{1}
\]

Both pair counts are ordered. Targets range over **all actual \(V_r^2\)**.
The exponent and starting depth are fixed before depth grows. A subsequence,
a selected-action return bound, or a bound restricted to target \(B_r^2\)
would not establish (1).

| Record | Evidence and audit disposition in this task |
|---|---|
| Frozen BFF-A1–A3, [algebra.md](../2026-10-11-balanced-full-fibers/algebra.md) | Inspected inherited scalar identities, input bounds, and exact full-key correspondence; these were independently audited in the preceding cycle |
| Frozen AMP-A1–A3, [amplitudes.md](../2026-10-06-cross-block-amplification/amplitudes.md) | Identified inherited dependencies: distinct amplitude cosets and exact norm-shell counts; no new enumeration or rediscovery |
| New BFO-L1 (E1–E4), [elimination.md](elimination.md), version 1 | Complete written proof independently audited here: PASS |
| New BFO-T1–T4, [tower.md](tower.md), version 1 | Complete written proof independently audited here: PASS |
| BFF-O1, exact statement (1) | PROVED by the inspected and independently audited proof chain; \(C=1\) works after enlarging \(r_0\) |
| BFO-F1, actual image conclusion (10) | PROVED for this carrier at every sufficiently large depth; \(\Theta(n_r^2)\), with fixed but uncomputed constants |
| Stopped second approach, [two-adic-screen.md](two-adic-screen.md), version 1 | Its displayed expansions and population limitation were checked; no complete reconstruction theorem is asserted or used |

The evidence is an internal proof audit, not external review or a literature
novelty check. No claim that these ideas are new in the literature is made.

## 2. Frozen scalar identifications and the counting implication

The inherited exact facts are

\[
V_r=B_r\mathbin{\dot\cup}(-B_r)\mathbin{\dot\cup}D_r,
\qquad X:V_r\longrightarrow A_r\text{ bijective},
\]
\[
|B_r|=8q^2,
\qquad16q^2+1\le n_r=|A_r|\le24q^2-7,
\tag{2}
\]
and
\[
\mathcal K(s,t)=\mathcal K(v,w)
\iff Q(X(s),X(t))=Q(X(v),X(w)).
\tag{3}
\]

In particular \(32q^4=|B_r|^2/2\) is an actual source count, not a count
of redundant words. The many representations of a value in \(D_r\) are
deduplicated in \(V_r\). Zero occurs once in \(D_r\) and remains part of
the target set. A nonzero \(B_r^2\) source has positive quadratic norm, so
the target \((0,0)\) cannot lie in its fiber; the proof does not need to
delete zero or any other completed target in advance.

If (1) alone is used, the touched outputs number at least

\[
\frac{32q^4}{(r+1)^C}
\ge\frac{n_r^2}{18(r+1)^C}.
\tag{4}
\]

The factor 18 follows from \(n_r^2\le576q^4\), not from an uncharged
projection or thinning. Since \(\log n_r=2r\log7+O(1)\), (4) is
\(n_r^{2-o(1)}\) uniformly at all sufficiently large depths. A source
bound of only \(32q^4-o(q^4)\) would not literally prove the exact
population requirement in (1); the new proof supplies a strict margin.

## 3. Independent audit of E1–E4

The finite-family lemma is sufficient as written. Its substantive steps were
checked separately:

1. **One common projection.** For each rank-four map, a suitable four-row
   minor is nonzero. The associated polynomial conditions on a projection
   matrix form a finite nonzero product. Avoiding its zeros over the infinite
   rational-function field gives one projection that works for every such
   map. Lower-rank maps remain algebraically dependent after projection.
2. **Lower-rank targets.** Each has a nonzero annihilating polynomial in the
   projected output. Multiplying these polynomials into \(H\) removes their
   entire images when \(H\ne0\). This includes maps with redundant
   parameters; their infinite parameter fibers cannot survive this exclusion.
3. **All fibers of each remaining map.** Algebraic independence makes the
   coordinate-function extension finite. A monic equation for each domain
   coordinate, after inverting finitely many output denominators, bounds
   each coordinate by a fixed root count. The product of those degrees
   bounds every parameter fiber off the denominator locus. Summing over the
   fixed target list gives a fixed \(M\), without assuming a sharp degree
   theorem or classifying every fiber.
4. **Nonzero source exceptional polynomials.** Algebraic independence of a
   source's projected coordinates implies \(H\circ f\ne0\). The proof
   preserves a nonzero coefficient of each such polynomial during
   specialization. Thus it does not silently allow an exceptional polynomial
   to become identically zero at a chosen depth.
5. **Uniform specialization.** The finitely many coefficient poles and
   protected numerators form a nonzero polynomial in the predecessor root.
   Its degree is fixed. The predecessor cyclotomic degrees tend to infinity,
   so it cannot vanish at any sufficiently deep specialization. Monic
   equations and cleared polynomial identities then specialize correctly.
   Only an initial segment of depths is lost.

The source exceptional degrees and the fiber bound are fixed for the finite
family. Their numerical values need not be known to prove the existential
constants required by (1). No numerical starting depth is certified.

## 4. Independent audit of BFO-T1–T3

### 4.1 Exact decomposition and complete targets

Splitting the phase exponent as \(a_0+7a'\) and separating the lowest
digit factor gives the disjoint decomposition

\[
B_r=\coprod_{a_0=0}^{6}\ \coprod_{i=-3}^{3}
g_{a_0,i}(\xi_r)B_{r-1},
\qquad g_{a,i}(T)=T^a(2-T^i).
\tag{5}
\]

All negative-exponent and wraparound carries are powers of
\(\eta=\xi_r^7\); they are retained in the coefficient field. For
\(r\ge2\) the extension over the predecessor field has degree seven.
The seven tower coordinates are therefore independent even though the full
product supports grow with depth.

For each of the 49 labels, \(U_g=\operatorname{span}\{g,\bar g\}\)
contains all three scalar types \(X(gb),-X(gb),Y(gb)\). Hence the
2401 ordered local quadratic maps cover **every** completed target pair,
including all \(D_r\) identifications. Enlarging these pieces to linear
spaces can overcount targets but cannot omit any. Dimension-one spaces
produce lower-rank maps handled by §3, not a false target injectivity claim.

### 4.2 The selected majority of rank-four source types

The residue classification into Z, W, C, O has sizes
\(1,12,24,12\). Carry coefficients are nonzero. W spaces fill one
two-dimensional absolute-residue summand; C and O have the injective
projections stated in the proof. The W determinant is \(4-1=3\).

A C first label has 40 specified disjoint partners; a W first label has
32 specified disjoint partners. The resulting

\[
24\cdot40+12\cdot32=1344>2401/2
\tag{6}
\]

are distinct **ordered** types. Uncounted types need not be classified.
For each counted type, the differential at scalar arguments \((g,0)\)
has columns \(2g^2,2g\bar g,gh,g\bar h\). Multiplication by nonzero
\(g\) is invertible, and the two source spaces are disjoint, proving
rank four. This cost is incurred once, not at every predecessor level.

### 4.3 Uniform avoidance by actual parent points

For \(j=r-1\), write \(Q_0=7^j\), \(N=8Q_0^2\). The inherited
norm-shell formula bounds the number of points of \(B_j\) on any circle
by \(Q_0 2^j\). There are at most \(8Q_0\) circles.

A nonzero polynomial of total degree at most \(d\) in \((b,\bar b)\)
has at most \(2d\) zeros on any circle on which it does not vanish
identically. Each identically vanishing circle contributes the distinct
factor \(ZW-\rho^2\), so there are at most \(\lfloor d/2\rfloor\)
such circles. This proves the uniform bound

\[
T_d(j)=16dQ_0+\lfloor d/2\rfloor Q_0 2^j.
\tag{7}
\]

Expanding a nonzero four-variable polynomial in its second conjugate pair
and selecting one nonzero coefficient bounds its zeros on \(B_j^2\) by
\(2NT_d(j)\). The relative bound tends to zero:

\[
\frac{2T_d(j)}N
\le\frac{4d}{7^j}+\frac d8(2/7)^j\longrightarrow0.
\tag{8}
\]

These bounds are uniform in coefficient sizes and in their dependence on
\(\eta\). They do not presume that a finite set is generic. For an actual
source, the substitution of formal \((b,\bar b,c,\bar c)\) into the four
local coefficients is an invertible diagonal linear change with nonzero
constants \(-\omega^2/\Delta,\omega/\Delta\). Consequently the
exceptional polynomial remains nonzero before (7)–(8) are applied. Complex
conjugacy imposes no complex polynomial identity here: the real-coordinate
substitution \((Z,W)=(x+iy,x-iy)\) is invertible over \(\mathbb C\).

## 5. Exact conclusion, rates, and retained boundaries

E1–E4 and §4 give a fixed \(M\ge1\) and a fixed exceptional degree
\(d\). Each of the 1344 disjoint source types has at least
\((1-\varepsilon_j)N^2\) good actual sources, where
\(\varepsilon_j=2T_d(j)/N\to0\). The explicit margin

\[
\varepsilon_j\le287/2688
\quad\Longrightarrow\quad
1344(1-\varepsilon_j)\ge2401/2
\tag{9}
\]

checks. Since \(49N=8q^2\), this yields at least \(32q^4\) sources
whose complete \(A_r^2\), equivalently \(V_r^2\), fibers have size at
most \(M\). Taking \(C=1\) and also requiring \(r+1\ge M\) proves
the exact quantifiers in (1).

The stronger conclusion actually proved is

\[
|Q(A_r,A_r)|\ge\frac{32q^4}{M}
\ge\frac{n_r^2}{18M}
\qquad\text{for every sufficiently large }r.
\tag{10}
\]

With the trivial upper bound, the actual image is \(\Theta(n_r^2)\).
Thus no unbounded subsequence of this carrier has any fixed positive power
saving. This does **not** say that every source fiber is bounded by \(M\);
large exceptional fibers may remain. Nor does it classify those fibers.
It supplies the required full-target bound on a sufficiently large actual
source population and the consequent entire-image lower bound.

The depth rates are \(\log n_r=2r\log7+O(1)\) and
\(\log|Q(A_r,A_r)|=4r\log7+O(1)\). The carrier has zero asymptotic
power-saving gap. Field degrees, denominator poles, scalar completion,
source multiplicities, and exceptional sources are charged in the proof;
no volume estimate, height restriction, regulator, or discriminant count is
used. In particular uncontrolled coefficient heights are not being assigned
zero cost in a height-based argument—the zero count is uniform in them.

The unrestricted T03 problem and other carrier families remain OPEN. The
earlier selected-certificate failures and finite histograms are neither
substituted for this proof nor promoted into more general conclusions.

## 6. Second approach and execution provenance

The two-adic approach was the second and last authorized structured approach.
Its exact normalization, reduction of \(\mathcal K\) modulo 2, and square
expansion modulo 8 were checked. A proposed word-signature injectivity step
was also inspected symbolically, but the complete all-target reconstruction
was not adopted. Its simplest same-valuation scale population is only
\((4^2+2^2+1^2+1^2)q^4=22q^4\), below the requested \(32q^4\).
It remains an unfinished argument, stopped once the tower proof succeeded,
and is not a dependency of (10).

No mathematical experiment or regression was run by this auditor. This file
is the auditor's only new file in this cycle; historical proofs and reports
were not edited. Administrative repository checks and final artifact hashes,
if performed by the lead, are reported separately and must not be described
as mathematical proof reruns. No third approach, new carrier, or new research
obligation is proposed here.
