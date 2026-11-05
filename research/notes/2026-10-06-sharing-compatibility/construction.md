# Fixed-gap triangle networks: construction and full-support ledger

2026-10-06, version 1. T01 only, with the fixed polynomial
\(P(x,y)=(x-y)^3+x+y\) on real scalars. This appendix treats the one
authorized directed-triangle family with consecutive output gap
\(2r\), where \(r=1/\sqrt3\) is fixed before the family grows.
No numerical computation, research program, network access, installation,
arithmetic amplification, or additional construction family is used.

**PROVED in this appendix:** the translated family has exact selected-output
count \(Z=N\) and at most \(2N-3\) distinct prescribed ordered pairs.
The consecutive strip attains this pair bound. Its actual full image is
\(N^2-O(N^{3/2})\), by the inherited fixed-spacing progression theorem
specialized below. Thus the strip fails the fixed-power-saving objective.
For arbitrary translates, the linear prescribed coverage is a certificate
obstruction; no general full-image lower bound is asserted here.

## 1. Identity, sources, and proof scope

The predecessor is the
[elliptic-geometry report](../2026-09-30-elliptic-geometry/README.md),
especially its §§5–7, and its
[construction ledger](../2026-09-30-elliptic-geometry/construction-ledger.md).
Those distinguish a sparse prescribed pair set from the full scalar square.
The format follows the
[construction template](../../templates/CONSTRUCTION_LEDGER.md).
The fixed-spacing input is
[GS-A4, §4](../2026-09-21-growing-step-cubic/progression-laboratory.md),
version 1 dated 2026-09-21, equations (A16)–(A18). Its complete elementary
proof was read and its specialization was checked algebraically in this
task. No previous experiment was rerun. The counting proofs below are new
for this specified triangle family; no external novelty claim is made.

All claims SH-C1–SH-C3 are for this fixed T01 polynomial, over the reals,
dated 2026-10-06. The uniqueness and fixed-gap classification
[SH-G2/SH-G3 in the geometry companion](geometry.md) are separate
dependencies only when declaring the translated family exhaustive among
solutions with this fixed ordered output gap. By that classification,
every triangle with ordered outputs \((z,z+2r,z+4r)\) is exactly one
of the translates above, so there is no additional real elliptic branch
within the specified family.
The scalar and pair counts below hold directly for the displayed family.
Neither the unavailable historical proof originals listed in the migration
conflict register nor their reported conclusions are proof dependencies.

## 2. SH-C1 — arbitrary translates and sharp linear coverage

Let \(T\subset\mathbb R\) be any nonempty finite set, \(M=|T|\).
For each \(t\in T\) prescribe the directed triangle
\[
 (a_t,b_t,c_t)=(t-r,t,t+r)
\]
and the three ordered pairs
\[
 (a_t,b_t),\qquad(b_t,c_t),\qquad(c_t,a_t).
\]
Let \(A=T+\{-r,0,r\}\), \(N=|A|\), let \(E\subset A^2\) be the
union of these ordered pairs, and put \(Q=|E|\), \(Z=|P(E)|\).
The formal pair-label count is \(Q_0=3M\); all assertions about \(Q\)
use distinct scalar ordered pairs.

**PROVED.** For every such \(T\),
\[
 M\le N\le3M,\qquad Q\le\min\{3M,2N-3\},\qquad Z=N.
\tag{C1}
\]

**Proof.** Since \(T\subset A\), the lower input bound holds, and the
union of three translates gives the upper bound. In particular \(N\ge3\).
The translation identity and the base triangle give
\[
 P(x+t,y+t)=P(x,y)+2t,
\]
\[
 \bigl(P(a_t,b_t),P(b_t,c_t),P(c_t,a_t)\bigr)
 =2t+\left(-\frac{4r}{3},\frac{2r}{3},\frac{8r}{3}\right).
\tag{C2}
\]
These are three distinct outputs in the required order with gap \(2r\).
Consequently their complete selected support is exactly
\[
 P(E)=2T+\left\{-\frac{4r}{3},\frac{2r}{3},\frac{8r}{3}\right\}
     =2A+\frac{2r}{3},
\tag{C3}
\]
and the affine map on the right is injective, proving \(Z=N\).

There are at most \(3M\) distinct pairs. Each prescribed pair has
difference \(x-y=-r\) or \(2r\). Forgetting orientation therefore
injects \(E\) into unordered edges between scalars separated by \(r\)
or \(2r\): the orientation is uniquely determined by the distance.
Order \(A\) increasingly and charge each such edge to its smaller
endpoint. Every scalar has at most two larger neighbors at these two
distances. The largest scalar has none, and the second largest has at
most one. Thus there are at most \(2(N-2)+1=2N-3\) edges. This proves
(C1). \(\square\)

Every prescribed output has at most two pairs in \(E\). Indeed, on a
fixed difference \(d\), \(P(x,x-d)=d^3+2x-d\) is injective in \(x\),
and there are only the two prescribed differences. This concerns the
selected pair set, not complete output fibers in \(A^2\).

The uncovered pair count is exactly \(B=N^2-Q\), so the safe complete
support certificate is
\[
 |P(A,A)|\le Z+B=N^2-Q+N.
\tag{C4}
\]
Equation (C1) implies that this certificate's right-hand side is at least
\(N^2-N+3\). This lower bound on a particular certificate is not a lower
bound on the actual image for arbitrary \(T\). It proves that counting
only these prescribed triangle pairs cannot deliver a positive fixed
power saving, regardless of how the translates are selected.

## 3. SH-C2 — PROVED: consecutive strip attaining the pair bound

For each integer \(m\ge1\), set
\[
 T_m=\{jr:1\le j\le m\},\qquad
 A_m=\{ir:0\le i\le m+1\},\qquad N=m+2.
\]
The triangles are \(((j-1)r,jr,(j+1)r)\). Their prescribed pair set is
the disjoint union
\[
 E_m=\{(ir,(i+1)r):0\le i\le m\}
 \ \cup\ \{((j+1)r,(j-1)r):1\le j\le m\}.
\tag{C5}
\]
The two parts have different directed differences, so they cannot overlap.
Thus
\[
 Q_0=3m,\qquad Q=(m+1)+m=2m+1=2N-3.
\tag{C6}
\]
Among formal labels, each internal adjacent edge \(1\le i\le m-1\)
appears twice, while the other \(m+2\) distinct pairs appear once.
This explicitly charges all \(m-1\) duplicate labels.

Using \(r^2=1/3\), the outputs in the two parts of (C5) are respectively
\[
 r\left(2i+\frac23\right),\quad 0\le i\le m,
 \qquad
 r\left(2(j+1)+\frac23\right),\quad1\le j\le m.
\]
The union is
\[
 P(E_m)=\left\{r\left(2k+\frac23\right):0\le k\le m+1\right\}.
\tag{C7}
\]
Hence \(Z=m+2=N\), as also follows from (C3). Exactly \(m-1\)
selected outputs have two distinct prescribed pairs and three have one;
these counts also cover \(m=1\). Every triangle has three distinct
outputs; no universal output label is held fixed across growing \(m\).

The intersection of all triangle vertex sets is empty for \(m\ge4\).
Thus growing the strip does not retain a common scalar anchor. Adjacent
triangles do share an adjacent directed edge, and (C6) already accounts
for that repetition. There are still only linearly many prescribed pairs:
\[
 B=N^2-2N+3,\qquad Z+B=N^2-N+3.
\tag{C8}
\]
The strip attains the sharp upper bound \(Q\le2N-3\), so it minimizes
the certificate (C4) at its given \(N\) within this translated family.

## 4. SH-C3 — the entire image of the forced strip carrier

The full support, including all uncovered pairs, has the following exact
description by difference slices:
\[
 P(A_m,A_m)
 =r\bigcup_{d=-(N-1)}^{N-1}
 \left\{\frac{d^3}{3}+|d|+2k:
                  0\le k\le N-1-|d|\right\}.
\tag{C9}
\]
Indeed for indices \(i,j\),
\[
 P(ri,rj)/r=(i-j)^3/3+i+j,
\]
and with \(d=i-j\), their sums run from \(|d|\) to
\(2(N-1)-|d|\) in increments of two. Formula (C9) is an exact support
set, not a claim that these slices are disjoint or a closed cardinality
formula.

Put
\[
 D_N=\min\{N-1,\lfloor\sqrt{6(N-1)}\rfloor\}.
\]
Specializing GS-A4 to spacing \(r=1/\sqrt3\) gives: every pair in a
nonsingleton actual fiber has index difference \(|i-j|\le D_N\).
To display the full dependency, if distinct pairs have equal output and
differences \(d,e\), then \(d\ne e\) and
\[
 |d^3-e^3|\le6(N-1).
\]
The nearest different integer cube is at distance at least \(d^2\),
so \(|d|\le D_N\). The same argument applies to either member of any
collision, exactly as in GS-A4. Every pair outside this band therefore
has its own singleton output.

There are exactly
\[
 \sum_{d=-D_N}^{D_N}(N-|d|)
 =N(2D_N+1)-D_N(D_N+1)
\]
pairs in the band. The number outside it is
\((N-D_N)(N-D_N-1)\). Also \(|P(A_m,A_m)|\ge N\), since for fixed
\(y\), the map \(x\mapsto P(x,y)\) has derivative
\(3(x-y)^2+1>0\). Combined with (C8), this proves the explicit bounds
\[
 \boxed{\max\{N,(N-D_N)(N-D_N-1)\}
 \ \le |P(A_m,A_m)|\le N^2-N+3.}
\tag{C10}
\]
In particular
\[
 |P(A_m,A_m)|=N^2-O(N^{3/2}),
 \qquad |P(A_m,A_m)|/N^2\longrightarrow1.
\tag{C11}
\]
For every fixed \(c>0\), (C11) is eventually larger than \(N^{2-c}\),
so this particular strip cannot solve T01. This is an actual-image
obstruction, stronger than its designated-pair certificate failure.
It is a specialization of the existing AP theorem, not a reopened AP
search, and it is not extended to arbitrary finite translate sets.

## 5. Fully charged construction ledger

| Gain or cost | Exact treatment and scope | Status |
|---|---|---|
| Growing parameter and fixed data | Strip: \(m\ge1\), \(r=1/\sqrt3\) and the directed triangle fixed first | PROVED |
| Distinct scalar count | Strip \(N=m+2\); arbitrary \(T\): \(M\le N\le3M\) | PROVED |
| Same-set and real transport | Both coordinates belong to the displayed real set \(A\); no trace or projection is taken | PROVED |
| Input thinning in both coordinates | None. Every one of the \(N^2\) ordered pairs is retained or charged in \(B\) | PROVED |
| Parameter/projection multiplicity | Three injective translate branches; cross-branch scalar coincidences form the union \(A\). Distinct pair count is \(Q\), not \(Q_0\) | PROVED |
| Prescribed coverage | \(Q\le2N-3\) for all translates; strip equality. Selected fibers have size at most two | PROVED |
| Selected support and all exceptions | \(Z=N\), exact uncovered count \(B=N^2-Q\); every uncovered pair costs one in (C4) | PROVED |
| Local sparsity, splitting and residue populations | Inapplicable: no sieve, finite-field realization, or local-density gain | PROVED |
| Field degree and arithmetic costs | Strip lies in fixed \(\mathbb Q(\sqrt3)\), degree two and discriminant 12. No tower, unit selection, regulator estimate, or growing field cost is used | PROVED |
| Denominators, heights and normalization | Strip inputs are \(i\sqrt3/3\), with fixed rational denominator 3 and coefficients growing linearly with \(N\). Formula (C9) is exact evaluation of the fixed \(P\), not a change of polynomial | PROVED |
| Archimedean size | Strip diameter \((N-1)r\). Both embeddings have absolute input size at most \((N-1)r\); no packing or metric saving is claimed | PROVED |
| Branch, ratio and carry costs | Three endpoint branches per triangle; \(m\) triangles, two directed differences. Duplicate labels are fully charged in (C6). No digital carries or ratio family | PROVED |
| Entire output support | Exact union (C9); cardinality bounded by (C10). Only the strip receives the actual-image lower bound | PROVED |
| Input and output rates | With depth \(d=\log m\), \(\log N=d+o(d)\), \(\log\lvert P(A_m,A_m)\rvert=2d+o(d)\). Both input rate bounds equal 1, the output rate is 2, and the net gap is \(\delta=0\) | PROVED |
| Positive fixed saving exponent | None for the strip; none follows from this prescribed-pair certificate for arbitrary translates | PROVED scoped obstruction |

The fixed quadratic field description applies to the explicit strip.
Arbitrary real \(T\) in SH-C1 need not belong to a number field, and the
counting proof uses no field-height or denominator hypothesis for it.

## 6. Evidence and disposition

SH-C1 and SH-C2 are complete symbolic counting proofs for all nonempty
finite \(T\) and all integers \(m\ge1\), respectively. SH-C3 imports
the identified GS-A4 proof and checks its exact specialization; the band
count and selected-support upper bound are displayed here. These are
mathematical proofs, with no finite-data or floating-point premise.
No experiment, full-square evaluation, symbolic-check program, imported
research executable, or old grid was run for this appendix.

The fixed-gap triangle certificate has a **PROVED scoped obstruction** to near-full coverage;
the explicit strip additionally has a **PROVED** actual-image obstruction.
T01 and the predecessor's general elliptic-sharing fiber-tail obligation
remain **OPEN**. This appendix adds no next research obligation; the lead
report retains the one obligation selected for the authorized task.
