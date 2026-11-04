# BFF-O1 — Balanced-Factor Carrier Retirement

11 October 2026 · T03 · version 1 · strictly offline.

## 1. Decision

**PROVED — BFF-O1.** There are fixed integers \(M\ge1\) and
\(r_*\) such that, for every \(r\ge r_*\), at least
\(32q^4\) ordered sources \((v,w)\in B_r^2\) have at most
\(M\) targets \((s,t)\in V_r^2\) satisfying
\(\mathcal K(s,t)=\mathcal K(v,w)\). These are unrestricted full
quadratic fibers. In particular BFF-O1 holds with the explicit exponent
\(C=1\), after increasing the starting depth to
\(r_0\ge\max(r_*,M-1)\).

**Consequence — the unchanged balanced-factor carrier is retired for
fixed power saving.** For all sufficiently large depths,
\[
\boxed{\frac{n^2}{18M}\le |Q(A_r,A_r)|\le n^2.}
\tag{1}
\]
In particular the requested weaker bound
\[
|Q(A_r,A_r)|\ge\frac{n^2}{18(r+1)}=n^{2-o(1)}
\tag{2}
\]
holds at every sufficiently large depth. This is an actual-image lower
bound, not an obstruction only to selected returns. It excludes any
fixed \(c>0\) for this carrier, including along unbounded subsequences.
The unrestricted same-set target for \(Q(x,y)=x^2+xy+y^2\) and the
separate RC15/4 obligation remain **OPEN**.

The fixed constants \(M,r_*\) are proved to exist; their numerical
values are not calculated. No sharp constant-fiber classification is
needed or claimed. Review and verification provenance is recorded in
[audit.md](audit.md) and [verification.md](verification.md).

## 2. Construction, complete equality, and source boundary

For \(r\ge0\), put \(q=7^r\), \(\xi=e^{2\pi i/q}\),
\(\omega=e^{2\pi i/3}\), and \(\Delta=1+2\omega\).
The unchanged amplitudes are
\[
c_{h,\mathbf i}=h\prod_{\ell=0}^{r-1}(2-\xi^{i_\ell7^\ell}),
\quad 1\le h\le8,\quad i_\ell\in\{-3,-2,-1,0,1,2,3\}.
\]
Define the actual deduplicated sets
\[
B_r=\{c_{h,\mathbf i}\xi^a:a\bmod q\},\qquad
D_r=\{\bar b-b:b\in B_r\},\qquad
V_r=B_r\mathbin{\dot\cup}(-B_r)\mathbin{\dot\cup}D_r.
\]
For \(v\in\mathbb Q(\xi)\), let
\[
X(v)=\frac{\omega\bar v-\omega^2v}{\Delta}.
\]
The frozen [BFF-A1–A2 proof](../2026-10-11-balanced-full-fibers/algebra.md)
establishes the bijection \(X:V_r\to A_r\),
\[
|B_r|=8q^2,\qquad 16q^2+1\le n=|A_r|\le24q^2-7,
\]
and the complete equality key
\[
\begin{aligned}
M(v,w)&=2vw+v\bar w+\bar v w-\bar v\bar w,\\
\mathcal K(v,w)&=M(v,v)+M(v,w)+M(w,w),\\
X(\mathcal K(v,w))&=3Q(X(v),X(w)).
\end{aligned}
\]
The bilinear function \(M(v,w)\) is distinct from the fixed integer
fiber bound \(M\) in the theorem. Thus counting all \(\mathcal K\)-targets in \(V_r^2\) is exactly
counting all distinct real targets in \(A_r^2\). The proof below works
with this equivalent full quadratic equality, not an action-generated
subgraph. In particular no target in \(B,-B,D\) is omitted.

Controlling predecessors, read in this cycle, are the
[11 October BFF report](../2026-10-11-balanced-full-fibers/README.md),
its [algebra](../2026-10-11-balanced-full-fibers/algebra.md),
[coupled proof](../2026-10-11-balanced-full-fibers/coupled.md), and
[audit](../2026-10-11-balanced-full-fibers/audit.md), together with
[AMP-A1–A3](../2026-10-06-cross-block-amplification/amplitudes.md)
for disjoint cosets and exact encoded norm classes. Those files remain
unchanged. Their selected-certificate obstructions are not used as
full-fiber bounds. The old 33-frequency theorem is not used or extended.

## 3. Why the growing factor support can be controlled

The decisive observation is to use **one last degree-seven extension**,
without recursively reconstructing each factor word. Let \(j=r-1\),
\(b=7^j\), \(\alpha=\xi_r\), \(\eta=\alpha^7\), and
\(L_j=\mathbb Q(\omega,\eta)\). Then
\([L_j(\alpha):L_j]=7\) for \(r\ge2\). Every point of \(B_r\)
has a unique expression
\[
g_{a,i}(\alpha)u,\qquad
g_{a,i}(\alpha)=\alpha^a(2-\alpha^i),
\quad 0\le a\le6,\ -3\le i\le3,\quad u\in B_j.
\tag{3}
\]
Carries are exact: reduce powers using \(\alpha^7=\eta\), not
formal independent digits. All completed scalar targets lie in the union
of the 49 spaces
\[
U_{a,i}=\operatorname{span}_{L_j}
  \{g_{a,i}(\alpha),\overline{g_{a,i}(\alpha)}\}.
\tag{4}
\]
Each has dimension at most two. This cover also contains \(X(D_r)\),
including zero and every identification in that block.

The [tower proof](tower.md) identifies at least **1344 of the 2401**
ordered local type pairs for which both spaces have dimension two and
intersect only at zero. On each such product, the full quadratic map
\((S,T)\mapsto S^2+ST+T^2\) has Jacobian rank four: at
\((S,T)=(g,0)\) its differential is
\(g(2\,dS+dT)\), injective on the direct sum of the two spaces.

The [finite-family lemma](elimination.md) now gives a fixed full-target
bound \(M\), outside the zero set of a nonzero polynomial of fixed
degree \(D\) in the two parent elements and their conjugates. It
includes all 2401 target space pairs, even targets not belonging to the
carrier. It first chooses one linear projection retaining the rank-four
maps, then uses algebraic coordinate equations to bound their fibers.
Lower-rank target images are excluded by polynomial equations. A rational
function parameter records \(\eta\); clearing finitely many denominators
and using its growing cyclotomic degree proves validity at **all**
sufficiently large depths.

This is a finite-dimensional argument at the last layer. There is no
unproved recurrence of independent branches and no \(C_0^r\) ambiguity
silently called polynomial in depth.

## 4. The exceptions are small enough to retain half of \(B_r^2\)

Let \(N=|B_j|=8b^2\). For a nonzero polynomial in one complex variable
and its conjugate, of total degree at most \(D\), the tower proof gives
\[
Z_D(j)\le16Db+\lfloor D/2\rfloor b2^j.
\tag{5}
\]
Indeed, on an amplitude circle the restriction is a Laurent polynomial
with at most \(2D\) roots unless the whole circle is a component.
There are \(8b\) amplitude labels. At most \(\lfloor D/2\rfloor\)
entire circles can divide the polynomial, and each contains at most
\(b2^j\) points of \(B_j\), by the frozen norm classification.
The bound is uniform in the polynomial's complex coefficients.

For a nonzero polynomial of degree at most \(D\) in two elements
and their conjugates, the number of zeros in \(B_j^2\) is at most
\(2N Z_D(j)\): first discard first-coordinate values where a chosen
nonzero coefficient vanishes, then apply (5) in the second coordinate.
Consequently the excluded fraction in any good local source type is at
most
\[
\frac{2Z_D(j)}N
\le\frac{4D}{b}+\frac D8\left(\frac27\right)^j
\longrightarrow0.
\tag{6}
\]
Choose the depth so this is at most \(1/10\). Distinct local types and
parent elements are distinct actual sources by the frozen coset theorem.
The number of retained ordered \(B_r^2\) sources is at least
\[
\frac9{10}\,1344\,(8b^2)^2
>32(7b)^4=32q^4,
\tag{7}
\]
since \(9\cdot1344>5\cdot2401\). Each has at most \(M\)
**full** targets. This proves the theorem, including its exact half-square
threshold and every sufficiently large depth. It does not merely prove
\(32q^4-o(q^4)\) sources.

## 5. Actual image, logical scope, and stopping point

Map the retained sources through the bijection \(X\) in each
coordinate. Each quadratic output receives at most \(M\) such sources,
because its entire fiber has at most \(M\) points. Therefore
\[
|Q(A_r,A_r)|\ge\frac{32q^4}{M}
\ge\frac{n^2}{18M},
\]
using \(n\le24q^2\). This proves (1), and then (2) for
\(r+1\ge M\). For any fixed positive compression exponent \(c\),
once \(n^c>18M\), this lower bound is larger than \(n^{2-c}\).
Thus the unchanged carrier fails the fixed-saving target.

The theorem neither says every fiber is bounded nor contradicts the
known growing encoded fibers. Those lie among allowed exceptions or
other local types. It gives no universal obstruction for other amplitude
rules, all ML-O1 carriers, RC15/4, ARG/TCRC, or the unrestricted T03 target.
Those remain OPEN. No new carrier, replacement conjecture, action search,
exact constant-fiber classification, or automatic RC15/4 pivot is adopted.

## 6. Approaches, evidence, and final handoff

Exactly two structured approaches were considered: the successful
last-layer tower argument and the stopped
[2-adic reconstruction screen](two-adic-screen.md). Only the tower
argument enters the theorem. The r=0,1 full-fiber scouts were read as
historical EXPERIMENTAL evidence and were **not rerun**. No r=2 square,
parameter sweep, or new mathematical program was executed.

The [construction/rate ledger](ledger.md), [audit](audit.md),
[verification record](verification.md), [machine state](state.json), and
[manifest](manifest.json) give source hashes, quantitative charges,
independent checks, and preservation evidence. Research computation:
**0 charged exact evaluations; 0 research-program CPU seconds**.
Repository checks and their separately measured administrative CPU are
recorded in verification.md. No files were committed.

**Final handoff: BFF-O1 PROVED; unchanged balanced-factor carrier RETIRED
for fixed power saving; unrestricted quadratic target OPEN. No successor
research obligation is adopted in this cycle.**
