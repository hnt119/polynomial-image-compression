# Independent full-fiber and rate audit

6 October 2026 · T03 · fixed polynomial \(Q(x,y)=x^2+xy+y^2\).
Specialist C; independent internal mathematical audit, version 1.

## 1. Authority, dependencies, and evidence

This is the explicitly authorized offline cross-block cycle, governed by
the live user request “New Cross-Block Returns — Multiscale Quadratic
Compression.” The assigned
scope is to audit the lead's full-fiber arguments for the two already
defined multiscale carriers. No new carrier, mutation, numerical scout,
external source, or novelty claim is introduced here. Mathematical program
use by this auditor is **zero evaluations and zero research-program CPU
seconds**. Local source inspection and symbolic proof checking are the
evidence; repository checks performed by the lead are separate evidence.

The frozen definitions and population counts were inspected in
[the 30 September composition proof](../2026-09-30-multiscale-packing/composition.md):
MS-C1, §§2–4, and MS-C2, §5. Those proofs remain correct within their
selected-action scope and are not edited. Their former absence of a full
image bound is extended by the new XB-F1/XB-F2 arguments below; it is not
treated as an error in the frozen report.

For each integer \(d\ge1\), those carriers use
\[
m=6\cdot2^d,\quad K=\mathbb Q(\zeta_m)\cap\mathbb R,
\quad \sigma(\zeta_m)=-\zeta_m,
\quad F=K^\sigma,
\quad t=2\cos(2\pi/m).
\]
The inherited identities give
\(K=F\oplus tF\), \(\sigma(t)=-t\), and
\(h:=t^2\in F\), with \(3\le h<4\). Both carriers are finite,
contain zero, are closed under negation, and use the same set in both
coordinates. All population counts concern distinct scalar values, with
all address collisions already identified.

The following checks audit new full fibers, not merely the selected group
\(\mu_m\). No result from a fixed-field height theorem is imported into
these growing fields.

## 2. XB-F1 — pure carrier full fibers

**Audit verdict: PASS; PROVED in the stated carrier scope.** Let
\(A\subset F\cup tF\) be the frozen pure carrier, and take nonzero
\(x\in F\), \(y\in tF\), or the reversed orientation. Then
\[
Q(x,y)=\underbrace{x^2+y^2}_{F}
+\underbrace{xy}_{tF},\qquad xy\ne0.
\tag{1}
\]
A target \((v,w)\in A^2\) with the same norm cannot have both
coordinates in the same \(F\)-line, or a zero coordinate: such a norm
would belong to \(F\). Therefore the target also has opposite nonzero
parities. Equality of the two components in (1) gives
\[
vw=xy,\qquad v^2+w^2=x^2+y^2.
\]
Thus the unordered pair \(\{v^2,w^2\}\) is
\(\{x^2,y^2\}\), by the quadratic with sum \(x^2+y^2\) and product
\(x^2y^2\). The sign of the product then leaves precisely
\[
(x,y),\quad(y,x),\quad(-x,-y),\quad(-y,-x).
\tag{2}
\]
These four pairs are present because \(A=-A\), and are distinct:
\(x=\pm y\) would put a nonzero scalar in \(F\cap tF=\{0\}\).
The full fiber has size exactly four.

The frozen population estimate is at least \(4(n-1)^2/9\) ordered
opposite-parity pairs, where \(n=|A|\). Every one belongs to a full
fiber of size four, so
\[
|Q(A,A)|\ge\frac{(n-1)^2}{9}.
\tag{3}
\]
This is an actual-image lower bound. It remains valid after allowing any
additional genuine norm-one multipliers or any other descriptions of
collisions in this same scalar square.

## 3. XB-F2 — independent target blocks have at most four points

**Audit verdict: PASS.** This argument requires a real quadratic
extension \(K/F\) with nontrivial automorphism \(\sigma\), and nonzero
line representatives \(r_i,r_j\in K\) with \(r_i/r_j\notin F\).
For a positive norm value \(q\) arising from a source in \(K^2\), any
target on this ordered line pair has the form
\((r_if,r_jg)\), with \(f,g\in F\), and satisfies
\[
P(f,g)=q,\qquad P^\sigma(f,g)=\sigma(q),
\tag{4}
\]
where
\[
P(f,g)=r_i^2f^2+r_ir_jfg+r_j^2g^2,
\quad
P^\sigma(f,g)=\sigma(r_i)^2f^2+
\sigma(r_i)\sigma(r_j)fg+\sigma(r_j)^2g^2.
\]
Both are positive definite real quadratic forms, since each is \(Q\)
after an invertible real diagonal change of coordinates. Also
\(q,\sigma(q)>0\), because \(\sigma(q)=Q(\sigma(x),\sigma(y))\)
for the nonzero source.

The forms are not proportional over \(\mathbb R\). Indeed, putting
\(c_i=\sigma(r_i)/r_i\) and \(c_j=\sigma(r_j)/r_j\),
proportionality would force
\(c_i^2=c_ic_j=c_j^2\), hence \(c_i=c_j\ne0\).
It would follow that \(\sigma(r_i/r_j)=r_i/r_j\), contrary to
the distinct-line hypothesis.

Subtract the normalized equations in (4). Every target lies on
\[
H(f,g):=\sigma(q)P(f,g)-qP^\sigma(f,g)=0,
\tag{5}
\]
a nonzero homogeneous binary quadratic. Its nonzero real zero set is
contained in at most two lines through the origin. This is elementary:
for \(f\ne0\), the slope \(g/f\) solves a quadratic; if the vertical
line occurs, the remaining polynomial has degree at most one. Each such
line meets the positive ellipse \(P=q\) in at most two points. Thus
there are at most four real target pairs, and therefore at most four
targets whose parameters lie in \(F\).

No general intersection theorem, algebraic closure count, or multiplicity
convention is needed. The estimate counts actual real ordered targets.

## 4. XB-F2 — same-line output spaces and the exceptional count

The frozen mixed carrier has four distinct \(F\)-lines with representatives
\[
r_0=1,\quad r_1=t,\quad r_2=1+t,\quad r_3=h+t=t(1+t).
\tag{6}
\]
Its nonzero line populations are exactly
\(b_+,b_-,b_+,b_-\). Put \(s=n-1=2(b_++b_-)\).
At least \(s^2/2\) ordered source pairs have independent coordinates
over \(F\), by the frozen four-line population calculation.

A same-line target has norm in \(r_i^2F\); targets with one zero
coordinate satisfy the same condition. There are exactly two distinct
such output spaces:
\[
\mathcal R_0=F,\qquad \mathcal R_1=(1+t)^2F.
\tag{7}
\]
Here “output space” means a one-dimensional \(F\)-linear subspace of
\(K\), not a ray in the usual real-geometric sense. The equality
\(t^2F=F\) identifies the other two squares. The spaces in (7) are
distinct because \((1+t)^2=(1+h)+2t\notin F\).

The sharper exceptional count was independently checked by expanding all
six unordered source blocks. For
\((x,y)=(r_i a,r_j b)\) with \(a,b\in F\setminus\{0\}\), write
\(Q(x,y)=E+tO\), where \(E,O\in F\). Membership in \(\mathcal R_0\)
is \(O=0\); membership in \(\mathcal R_1\) is
\(2E-(h+1)O=0\). The complete admissible ratio table is

| Source lines \(i,j\) | Ratio \(a/b\) for \(\mathcal R_0\) | Ratio \(a/b\) for \(\mathcal R_1\) |
|---|---|---|
| 0,1 | none | none |
| 0,2 | \(-2\) | \((h-1)/2\) |
| 0,3 | \(-2h\) | \(-(h-1)/2\) |
| 1,2 | \(-2\) | \(-(h-1)/(2h)\) |
| 1,3 | \(-2\) | \((h-1)/2\) |
| 2,3 | none | none |

For block 0,1 the two tests are \(ab=0\) and
\(2a^2-(h+1)ab+2hb^2=0\); for block 2,3 they are
\(2a^2+(h+1)ab+2hb^2=0\) and \(-(h-1)^2ab=0\).
The displayed quadratic discriminant is \(h^2-14h+1<0\) for
\(3\le h<4\). These tests give no nonzero real pairs in those blocks.
In each other block the two tests factor into the ratios displayed above.
The reversed orientation uses reciprocal ratios, with no denominator
zero since \(h\ge3\).

For a fixed nonzero first scalar, only two other source lines can occur
in this table. Each of the two output spaces determines at most one
second scalar on each viable line. Actual membership in the finite
carrier can only reduce the count. Consequently at most \(4s\)
ordered independent sources have norm in the union (7).

At least
\[
G:=s^2/2-4s
\tag{8}
\]
ordered sources therefore have a norm outside both spaces. If this
expression is negative, the inequality is simply vacuous; no positivity
for small depths is asserted.

## 5. XB-F2 — full fiber, actual image, and all-action tail

For any source counted in (8), every target in the full scalar square
must have nonzero independent coordinates. Otherwise its norm would lie
in (7). There are twelve ordered pairs of distinct target lines. By §3,
each contributes at most four targets. Therefore the entire fiber has
size at most 48, and
\[
|Q(A,A)|\ge\frac{(n-1)^2/2-4(n-1)}{48}
=\frac{(n-1)^2}{96}-\frac{n-1}{12}.
\tag{9}
\]
The constants do not depend on depth, field degree, or the sizes of the
individual line populations. Since the actual scalar size grows to
infinity, (9) is a quadratic image lower bound.

Every genuine returned target belongs to the source's full fiber. In
fact, at a nonzero source \(z=x-\omega y\), every equal-norm target
\(z'\) is realized by the unique multiplier \(u=z'/z\) with norm one.
Thus the full-fiber conclusions imply the following uniform statement,
even for arbitrary depth-dependent choices of norm-one actions:

- For the pure carrier, at least \(4(n-1)^2/9\) sources have at most
  four distinct returned targets; with all norm-one multipliers, the
  count on that population is exactly four.
- For the mixed carrier, at least \((n-1)^2/2-4(n-1)\) sources have
  at most 48 distinct returned targets.

For every fixed \(\varepsilon,\delta>0\), these populations eventually
lie below the threshold \(n^\varepsilon\), and have cardinality
\(\Theta(n^2)\), which is not \(O(n^{2-\delta})\). The conclusion is
now about all genuine actions on these carriers, not only \(\mu_m\).
The zero source has norm zero and one distinct target, regardless of
the number of action labels, and is excluded from the population counts.

## 6. Charged rate and scope ledger

| Item | Audit conclusion |
|---|---|
| Fixed target and coordinates | The same polynomial \(Q\) and the entire ordered same-set square are used. |
| Actual input bounds | Pure: \(3\cdot2^d+1\le n\le3\cdot4^d+1\). Mixed: \(6\cdot2^d+1\le n\le3\cdot4^d+1\). Frozen actual-union bounds, with every address collision allowed. |
| Thinning | None. Selected source populations prove lower bounds for the image of the full carrier; omitted source pairs cannot reduce that image. |
| Pair projection | \((x,y)\mapsto x-\omega y\) is injective. A nonzero source determines its multiplier uniquely from a target. |
| Population loss | Pure: no exception inside the cross-parity population. Mixed: the exact table charges at most \(4(n-1)\) exceptional independent sources. |
| Full target coverage | Pure fiber exactly four. Mixed fiber at most 48 after excluding both same-line output spaces. Every target line and zero-coordinate possibility is accounted for. |
| Field degree and coefficients | The fields grow with depth. Only the explicit real quadratic extension \(K/F\) and \(3\le t^2<4\) are used; all constants are uniform in the growing ambient degree. |
| Heights, denominators, discriminants, regulators, local splitting | No lattice population, norm-divisor, volume, or unit-counting estimate is used. These arithmetic quantities support no claimed saving and are not assigned artificial zero values. |
| Branches and state fibers | The proof uses actual scalar line populations; formal addresses and repeated multiplier descriptions give no gain. |
| Input factor | Exact \(\lambda\) remains unproved. If it exists, \(2\le\lambda\le4\). |
| Output exponent | Both full images have \(\log\lvert Q(A_d,A_d)\rvert=2\log n_d+O(1)\). Along any input-rate subsequence, the output rate is twice the input rate. |
| Net gap | No fixed power saving: normalized output exponent is 2 and the gap is zero for these two families. |
| Genuine-return gain | A quadratic-size source population has uniformly bounded full fibers; its exponential return factor is 1. No global return asymptotic is asserted. |

**Final disposition.** XB-F1 and XB-F2 pass the independent mathematical
audit. These two existing carrier families fail the fixed-power image
target itself. This does not prove a universal obstruction for other
coordinate-reusing packings, does not resolve ML-O1, DC-O1, adaptive
ARG/TCRC/RC15/4, and does not resolve the general fixed real-polynomial
target. The lead's two-family stop instruction is respected: no further
proof search, mutation, or experiment is proposed here.

## 7. Final written-companion inspection

After the proof-message audit, the completed [composition companion](composition.md)
was inspected independently. Every row of its six-block \(E,D\) table,
both exceptional-ratio columns, the reversed orientations, and its
\(4(n-1)\) actual-source count agree with the derivation above.
No transcription or scope defect was found.

The completed [action companion](actions.md) was also inspected. Its swap
coefficients, projective-slope parametrization, rank-one kernel domain,
selected-group exclusion, and concrete Vieta target and membership pass
symbolic checking. Its certified-line domains are correctly distinguished
from full return domains; its per-source twelve-target certificate is
correctly distinguished from a full-fiber bound. These identities do not
alter the XB-F1/XB-F2 obstruction. This is an internal mathematical audit;
no finite experiment or source-hash check is claimed by these inspections.
