# C0 mixed signature lattice symmetry

20 October 2026 · T03 / shared full-rank quadratic direction · version 1.
Strictly offline research on the unchanged polynomial
\(Q(x,y)=x^2+xy+y^2\).

## 1. Result

**PROVED:** base changing the fixed cubic seed through the accepted C0
tower gives fields of bounded root discriminant, a rank-\(d_j\) group of
integral norm-preserving actions, and an exponentially growing scalar lattice
carrier. Every nonzero order-unit return lies in an explicit finite height
window.

**FAILED IN STATED SCOPE:** the inherited seed \(u_0=s^2+s\omega\), even
with all integer powers and all tower torsion units, gives only
\(O((\log n_j)^3)\) targets per pair. This cannot supply a positive-power
return tail.

**OPEN:** the tail for the entire rank-\(d_j\) order-unit group, the actual
image of this lattice carrier, and the unrestricted T03 target.
No \(\varepsilon,\delta>0\), or resulting \(c>0\), has been proved.
There is no actual-image obstruction retiring this new carrier.

| Question | Proved result or exact deficit |
|---|---|
| Fields | \([K_j:F_j]=3\), signatures \(K_j:(d_j,d_j)\), \(E_j:(0,3d_j)\); \(\operatorname{rd}(K_j)\le D_*=D_0 31^{1/3}\), \(\operatorname{rd}(E_j)\le\sqrt3D_*\) |
| Integral actions | Relative order-unit rank \(d_j\); matrix \(M_u\in\mathrm{SL}_2(\mathcal O_{K_j})\); maximal-order passage can cost index \(3^{3d_j}\) |
| Actual scalar size | At fixed \(T_0=2\sqrt{D_*}\), \((4\pi)^{d_j}\le n_j\le(4\sqrt{D_*}+1)^{3d_j}\) |
| Nonreal distortion | Eigenvalue moduli \(e^{\lambda_\sigma},e^{-\lambda_\sigma}\); local continuous overlap at most \(\min(1,4e^{-2\lvert\lambda_\sigma\rvert})\) |
| Finite unit inventory | All nonzero returns lie in \(\lVert\ell(u)\rVert_1\le d_jL(T)\), \(L(T)=\frac12\log(48T^6)\); its useful population is unproved |
| Return tail | Seed plus torsion fails; full-rank group remains OPEN, with relative covolume and exact pair-dependent window costs |
| Compression exponent | No explicit \(c>0\); the proved implication needs positive return and exception exponents |

Complete arguments:
[field and unit audit](field-units.md),
[window and seed-return proofs](window-returns.md),
[carrier and rate proofs](carrier-rate.md),
[independent review](audit.md).
The provenance, checks and zero-computation record are in
[verification.md](verification.md).

## 2. Exact carrier and choice of parameters

Fix the accepted C0 totally real tower \(F_j\), its bound \(D_0\), and the
radius \(T\) before allowing \(j\) to grow. Let
\[
s^3+s+1=0,\quad s\in\mathbb R,\qquad
K_j=F_j(s),\quad E_j=K_j(\omega),\quad
\omega=(-1+i\sqrt3)/2.
\]
For a chosen real embedding \(\sigma_0\), use
\[
C_j(T)=\{x\in\mathcal O_{K_j}:|\sigma x|\le T
                          \text{ for every embedding }\sigma\},\qquad
A_j=\sigma_0(C_j(T)).
\tag{1}
\]
The complex constraints are disks, not omitted coordinates. The projection
is injective. Compactness of the Minkowski window proves finiteness, and
negation proves central symmetry.

Blichfeldt averaging on the half-window followed by subtraction gives the
centered count
\[
\left(\frac{(\pi/2)T^3}{D_*^{3/2}}\right)^{d_j}
\le n_j\le(2T+1)^{3d_j}.
\tag{2}
\]
The upper bound uses the nonzero integer norm of a difference to pack
disjoint half-unit windows. No uniform lattice equidistribution theorem is
assumed. Choosing \(T_0=2\sqrt{D_*}\) makes the lower rate \(\log(4\pi)>0\).

The fixed cubic remains irreducible over every totally real \(F_j\):
otherwise it would have its unique real root in \(F_j\), placing the
mixed-signature field \(\mathbb Q(s)\) inside a totally real field.
Its discriminant \(-31\), followed by the relative basis discriminant
\(-3\) for \(\omega\), gives the root-discriminant bounds in the table.

## 3. Global integral actions and their costs

Let \(\tau(\omega)=\omega^2\) fix \(K_j\), and use the order
\(R_j=\mathcal O_{K_j}[\omega]\). For
\[
u=a+b\omega\in R_j^\times,\qquad u\tau(u)=a^2-ab+b^2=1,
\]
the exact identity is
\[
u(x-\omega y)=x'-\omega y',\qquad
\binom{x'}{y'}=
\begin{pmatrix}a&b\\-b&a-b\end{pmatrix}\binom{x}{y}.
\tag{3}
\]
Its determinant is 1 and its inverse is the integral action of \(\tau u\).
Hence \(Q(x',y')=Q(x,y)\) on the full coefficient lattice.

Dirichlet ranks give
\((3d_j-1)-(2d_j-1)=d_j\), since the norm image contains every
\(K_j\)-unit square. The conductor contains
\((1+2\omega)\mathcal O_{E_j}\), yielding the explicit unit subgroup index
\[
[\ker N_{E_j/K_j}(\mathcal O_{E_j}^{\times}):
 \ker N_{E_j/K_j}(R_j^\times)]\le3^{3d_j}.
\tag{4}
\]
Thus integral coefficients do not make passage from the maximal order free.

For each complex \(K_j\)-place choose one extension to \(E_j\), and let
\(\ell_j(u)\) list its \(d_j\) logarithmic moduli. Write
\(\mathcal R_{R,j}\) for the covolume of the resulting relative log lattice.
This is a specifically normalized relative regulator, not the ordinary
regulator of \(K_j\). Its size and useful basis shape remain unbounded by
the arguments here. The finite torsion group has size \(w_j\le8d_j^2\).

## 4. Nonreal distortion and the complete finite inventory

At a complex place with image \(\eta\) of \(\omega\), put
\[
z=x-\eta y,\qquad w=x-\eta^2y,\qquad t=\widetilde\sigma(u).
\]
The exact action is \((z,w)\mapsto(tz,t^{-1}w)\), with \(Q=zw\).
Here \(w\) need not be \(\bar z\), and \(t^{-1}\) need not be \(\bar t\).
Return requires both inverse coordinate expressions
\[
y'=\frac{t^{-1}w-tz}{\eta-\eta^2},\qquad
x'=\frac{\eta t^{-1}w-\eta^2tz}{\eta-\eta^2}
\tag{5}
\]
to have modulus at most \(T\), together with every real-place constraint.
One actual global unit must satisfy all these inequalities.

Source and target membership imply
\[
|\sigma Q(x,y)|\le4T^2e^{-|\ell_\sigma(u)|}.
\]
For a nonzero source, taking its nonzero integer absolute norm gives
\[
1\le |N_{K_j/\mathbb Q}Q(x,y)|
\le(48T^6)^{d_j}e^{-2\|\ell_j(u)\|_1}.
\tag{6}
\]
Consequently the explicit finite family
\[
U_j(T)=\{u\in R_j^\times:u\tau(u)=1,\
                 \|\ell_j(u)\|_1\le d_jL(T)\},\qquad
L(T)=\tfrac12\log(48T^6),
\tag{7}
\]
contains every nonzero order-unit return. Each member has absolute
logarithmic height \(h(u)\le L(T)/3\).
This does not bound every conjugate by a degree-independent constant:
the cutoff gives only
\(\max_{\widetilde\sigma}|\widetilde\sigma u|\le e^{d_jL(T)}\).
At a nonzero source, distinct units give distinct actual target pairs;
at the origin there is exactly one target.

With \(H=d_jL(T)\) and \(S_j\) the half-sum of the \(\ell^1\)-norms
of a relative log-lattice basis,
\[
w_j\frac{H^{d_j}}{d_j!\mathcal R_{R,j}}
\le |U_j(T)|
\le
w_j\frac{2^{d_j}(H+S_j)^{d_j}}{d_j!\mathcal R_{R,j}}.
\tag{8}
\]
The unknown regulator and shape costs are retained. A hypothetical bound
\(\mathcal R_{E,j}\le e^{C_Rd_j+o(d_j)}\) would give only the candidate
action rate \(1+\log L(T)-C_R-3\log3\). It would not imply that these
units satisfy (5) for typical sources.

The continuous overlap upper bound is
\[
\frac{\operatorname{vol}(W_T^2\cap M_u^{-1}W_T^2)}
     {\operatorname{vol}(W_T^2)}
\le\prod_{\sigma\ {\rm complex}}\min(1,4e^{-2|\ell_\sigma(u)|}).
\tag{9}
\]
This quantifies loss from nonreal expansion. Neither large rank nor mean
overlap supplies the required discrete exceptional-pair tail. The available
fixed-field dilation limit has no asserted uniform error along the tower.

## 5. A decisive obstruction for the inherited seed

The supplied TFQ §G.4 seed is
\[
u_0=s^2+s\omega,\qquad u_0\tau(u_0)=s^4-s^3+s^2=1.
\]
At each nonreal block it has the same expanding modulus \(\rho>1\).
For a nonreal cubic root \(\beta\), this follows from the reciprocal
eigenvalues and
\[
|\beta+\omega|^2-|\beta+\omega^2|^2
=2\sqrt3\,\operatorname{Im}\beta\ne0.
\]
Equation (6) forces every returning integer power, positive or negative,
to satisfy
\[
|k|\le L(T)/\log\rho.
\tag{10}
\]
Thus all powers together give only \(O(1+\log T)\) targets per pair.

Including every torsion unit gives at most
\[
8d_j^2\left(1+2\left\lfloor L(T)/\log\rho\right\rfloor\right)
\tag{11}
\]
targets. For every sequence \(T_j\ge T_0\), equations (2) and
\(n_j\ge2\lfloor T_j\rfloor+1>T_j\) make (11)
\(O((\log n_j)^3)\). Therefore, for every fixed \(\varepsilon>0\),
eventually **every** pair has fewer than \(n_j^\varepsilon\) targets
under this seed-and-torsion group. Its bad-pair population is \(n_j^2\).

This is a pointwise obstruction, so no discrete volume approximation is
needed. The same argument would obstruct a window reshaping only if its
actual input count retained the bounds used to convert (11) into a
subpolynomial bound. No theorem about arbitrary thinned or correlated
windows is asserted. No correlated-window mutation is introduced here.
Other independent relative units remain outside this
obstruction, as do nonintegral multipliers and unrestricted full fibers.

## 6. Full support and the remaining quantitative deficit

Let \(R_j(p)\) count distinct targets from (7) that genuinely belong to
the same \(A_j^2\). If
\(\mathcal E_j=\{p:R_j(p)<R\}\), then partitioning full polynomial fibers gives
\[
|Q(A_j,A_j)|\le n_j^2/R+|\mathcal E_j|.
\tag{12}
\]
Every output represented by a good source has at least \(R\) full-fiber
members; outputs represented only by bad sources number at most
\(|\mathcal E_j|\). Equality between an action orbit and a full fiber
is not needed.

At fixed \(T\), put \(B=3\log(2T+1)\). A proved return threshold
\(e^{\kappa d_j}\) outside at most \(C n_j^2e^{-\eta d_j}\) bad pairs
would yield every fixed \(c<\min(\kappa,\eta)/B\).
Neither \(\kappa>0\) nor \(\eta>0\) is established.
The full [signed ledger](carrier-rate.md#6-construction-ledger) accounts
for discriminant, order index, relative regulator, unit height, lattice
shape, all embedding constraints, stabilizers and exceptional outputs.
No cost is silently replaced by zero.

## 7. Exact relationship to frozen results

| Frozen result | Hypothesis or mechanism relevant here |
|---|---|
| Corrected C0 | Its theorem concerns a rank-one quadratic. Its totally real tower and lattice-count method are inherited inputs; its compression conclusion does not transfer to \(Q\). |
| Totally real CM unit factor | T03's global ideal bound uses a totally real coefficient field, making the relative norm-one unit group finite. The present coefficient field has signature \((d_j,d_j)\), and the kernel has rank \(d_j\). That finite-unit conclusion does not apply. |
| Full-input norm sieve | The fixed-prime criterion \(3D\prod q/(q+1)<1\), and its wider decomposition variants, remain closed in their stated scope. This cycle uses an archimedean unit-return certificate and imports no sieve gain or improved splitting assertion. Mixed signature alone is not declared to evade every local inequality. |
| Previous number-field box actions | Exact finite invariance and a small common stable core were not enough. The present order removes coefficient denominators only after paying its index; the nonreal boundary and typical-pair return problem remain. |
| Phase-A regulator comparison | A hypothesis or estimate stated for totally real fields is not a proved bound for \(\mathcal R_{E,j}\) or \(\mathcal R_{R,j}\). No such transfer is made. |
| BFF-O1 | The balanced-factor carrier remains retired by its full-fiber theorem. It is not used or reopened here. |

The main quadratic target and the separate adaptive RC15/4 obligation remain
**OPEN**. This cycle neither pivots to RC15/4 nor analyzes the affine
polynomial \(Q+x\) or a difference-set optimization.

## 8. Audit and next obligation

MS-F1–F6, MS-W1–W3 and MS-C1–C3 have complete local proofs. The lead
checked the mathematical deductions, and a separate internal auditor read
and checked the written proofs. No novelty or external review is claimed.
There were **0 charged exact mathematical evaluations** and **0 research
program CPU seconds**. Administrative validation is reported separately.
No historical scout was rerun.

**One next lemma — MS-O1, OPEN.** For the unchanged tower and the
explicit inventory (7), prove or refute the existence of fixed
\(T\ge T_0\), \(\alpha>0\), and \(j_0\) such that
\[
|U_j(T)|\ge e^{\alpha d_j}\qquad(j\ge j_0).
\tag{13}
\]
This is a necessary action-population gate for a uniform eventual return
tail on this tower, not a sufficient compression theorem. Refuting its
uniform quantifiers alone would not exclude an unbounded subsequence.
An affirmative answer would still require the exact pair-dependent return
and exception estimates in (12). No replacement carrier is adopted.
