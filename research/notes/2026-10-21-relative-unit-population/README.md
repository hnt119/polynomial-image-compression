# MS-O1 — Relative-Unit Population and Distortion

21 October 2026 · T03 · version 1 · strictly offline.
Fixed polynomial: \(Q(x,y)=x^2+xy+y^2\).

## 1. Result and its precise meaning

**PROVED — MS-O1.** For the unchanged mixed-signature C0 tower and
the relative **order-unit** inventory specified on 20 October, there is
an explicit fixed radius \(T_*\ge T_0\) such that
\[
\boxed{|U_j(T_*)|\ge 2^{d_j}\quad\text{at every tower level}.}
\tag{1}
\]
Thus the requested population exponent is \(\alpha=\log2>0\).
This is an all-level statement, not a subsequence result.

The proof establishes the uniform relative logarithmic covolume bound
\[
\boxed{\mathcal R_{R,j}\le K_R^{d_j}}
\tag{2}
\]
with an explicit constant depending only on the accepted C0
root-discriminant bound. It uses Minkowski bodies, bounded integral-ideal
and exact relative-norm labels, and a covering of the relative log torus.
It does not import a totally real regulator theorem into mixed signature.

**Meaning.** There are exponentially many distinct integral
norm-preserving actions inside the established finite return cutoff.
This resolves the necessary population gate.

**Consequence and boundary.** No useful return exponent or small exceptional
set has yet been proved. The actual quadratic-image rate of this carrier,
the unrestricted T03 target, and the separate RC15/4 obligation remain
**OPEN**. The carrier is not retired. Neither the previously closed
seed-plus-torsion certificate nor the balanced-factor carrier is reopened.

Companions:

- [Arithmetic proof](arithmetic.md): MSU-A1–A3, including all constants.
- [Geometry and independent proof audit](geometry-audit.md): MSU-G1–G3,
  the weight distribution, an honest discrete comparison, and arithmetic
  audit verdict.
- [Construction and signed-rate ledger](ledger.md): full costs and the
  exact unresolved return gate.
- [Provenance and validation](verification.md): sources, checks, budget
  and preservation record.
- [Machine-readable state](state.json).

## 2. Unchanged tower, scalar carrier and actual actions

The accepted totally real C0 tower has degree
\(d_j=[F_j:\mathbb Q]\to\infty\) and root discriminant at most \(D_0\).
Retain
\[
s^3+s+1=0\quad(s\text{ real}),\qquad
K_j=F_j(s),\qquad E_j=K_j(\omega),\qquad
R_j=\mathcal O_{K_j}[\omega],
\]
where \(\omega^2+\omega+1=0\), and let \(\tau\) fix \(K_j\).
The [20 October field proof](../2026-10-20-mixed-signature/field-units.md)
establishes
\[
[K_j:\mathbb Q]=3d_j,\quad \operatorname{sig}(K_j)=(d_j,d_j),\qquad
[E_j:\mathbb Q]=6d_j,\quad \operatorname{sig}(E_j)=(0,3d_j).
\]
Put
\[
D_*=D_0\,31^{1/3},\qquad D_E=\sqrt3D_*,\qquad T_0=2\sqrt{D_*}.
\]
Then \(\operatorname{rd}(K_j)\le D_*\) and
\(\operatorname{rd}(E_j)\le D_E\).

For one fixed radius \(T\ge T_0\), use exactly
\[
C_j(T)=\{x\in\mathcal O_{K_j}:|\sigma x|\le T
                       \text{ at every embedding}\},\qquad
A_j=\sigma_0(C_j(T)),\quad n_j=|A_j|,
\tag{3}
\]
where \(\sigma_0\) is a real embedding. The constraints at the complex
places are disks, as well as intervals at the real places.
The real embedding is injective; the set is finite, centrally symmetric,
and contains zero. The inspected MS-C1 proof gives
\[
e^{a(T)d_j}\le n_j\le e^{B(T)d_j},\qquad
a(T)=\log\frac{(\pi/2)T^3}{D_*^{3/2}}>0,\quad
B(T)=3\log(2T+1).
\tag{4}
\]
These are bounds on actual distinct scalars. No growth limit for
\(\log n_j/d_j\) is assumed.

Let \(\mathcal G_j=\{u\in R_j^\times:u\tau(u)=1\}\).
At each of the \(d_j\) complex places of \(K_j\), choose one extension
to \(E_j\), and put
\(\ell_j(u)_i=\log|\nu_i^+(u)|\). The other extension has logarithm
\(-\ell_j(u)_i\). At real \(K_j\) places the modulus is one.
The lattice \(\Lambda_{R,j}=\ell_j(\mathcal G_j)\) has rank \(d_j\).
Here \(\mathcal R_{R,j}\) means its ordinary Euclidean covolume
in these \(d_j\) coordinates, not an absolute regulator in a different
normalization.

For \(u=a+b\omega\in\mathcal G_j\),
\[
M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix}
\in\mathrm{SL}_2(\mathcal O_{K_j}),\qquad Q(M_up)=Q(p).
\tag{5}
\]
These are actual global algebraic units. There is no independent choice
of rotations at individual embeddings.

Retain the exact inventory
\[
U_j(T)=\{u\in\mathcal G_j:\|\ell_j(u)\|_1\le d_jL(T)\},\qquad
L(T)=\tfrac12\log(48T^6).
\tag{6}
\]
The prior norm argument proves that (6) contains every order-unit return
of a nonzero source from (3). It does not say that every unit in (6)
returns. The set is finite and contains the identity.
For \(p\in A_j^2\), define
\[
R_j(p)=\#\{M_up:u\in U_j(T),\ M_up\in A_j^2\},
\tag{7}
\]
interpreting the coefficients at \(\sigma_0\).
Both target coordinates must come from (3), including all their
conjugate constraints. Distinct units give distinct targets when
\(p\ne0\), since multiplication on \(x-\omega y\ne0\) is free.
At zero there is just one target.

## 3. Explicit constants and proof architecture

Fix, in this order,
\[
B_0=2\sqrt{D_E},\quad g=\log B_0,\quad
J_0=64B_0^{12}(2B_0^2+1)^3,\quad
K_E=6egJ_0,\quad K_R=27K_E,\quad C_R=\log K_R,
\tag{8}
\]
and then
\[
\boxed{T_*=\max\{T_0,\exp(2K_R/3)\}.}
\tag{9}
\]
All constants are independent of \(j\). The symbol \(B_0\) is the
arithmetic companion's \(B\); it is unrelated to the input upper
exponent \(B(T)\). The auxiliary Minkowski body used to prove (2)
is not a replacement scalar carrier.

Here is the mechanism; the [arithmetic companion](arithmetic.md)
contains the complete proof.

1. **Approximation in every relative log direction.** For any
   \(x\in\mathbb R^{d_j}\), take complex disks of radii \(B_0\)
   above real \(K_j\) places and \(B_0e^{x_i},B_0e^{-x_i}\)
   above complex ones. Their volume is constant in \(x\) and exceeds
   Minkowski's threshold. They contain \(0\ne a\in\mathcal O_{E_j}\).
   The product formula and integrality give
   \[
   \|p(a)-x\|_1\le3d_jg,\qquad
   p(a)_i=\tfrac12\log\frac{|\nu_i^+(a)|}{|\nu_i^-(a)|}.
   \]
2. **Only exponentially many exact labels.** Record both
   \(I=(a)\) and the element \(b=a\tau(a)\).
   Then \(NI\le B_0^{6d_j}\) and
   \(|\sigma b|\le B_0^2\) at every \(K_j\) embedding.
   Ideal counting by an absolutely convergent Euler product and
   algebraic-norm separation give at most
   \[
   B_0^{12d_j}2^{6d_j}(2B_0^2+1)^{3d_j}=J_0^{d_j}
   \]
   possible label pairs. No class-number estimate is used.
3. **Genuine relative units, not arbitrary ratios.** Equal labels imply
   \(a/a'\in\mathcal O_{E_j}^\times\) and
   \(N_{E_j/K_j}(a/a')=b/b=1\).
   Keeping the exact element \(b\) is essential.
   Thus the relative log space is covered by at most \(J_0^{d_j}\)
   translates of \(\Lambda_{E,j}+\mathbb B_1(3d_jg)\).
4. **Covolume and order.** Integrating the covering over the log torus
   yields
   \[
   \mathcal R_{E,j}
   \le J_0^{d_j}\frac{2^{d_j}(3d_jg)^{d_j}}{d_j!}
   \le K_E^{d_j}.
   \]
   The inherited order-unit index is at most \(3^{3d_j}\);
   hence (2). This order cost is charged exactly once.
5. **Centered unit population.** The established count, with
   torsion multiplicity \(6\le w_j\le8d_j^2\), gives
   \[
   |U_j(T_*)|\ge
   \frac{w_j(d_jL(T_*))^{d_j}}{d_j!\mathcal R_{R,j}}
   \ge w_j\left(\frac{L(T_*)}{K_R}\right)^{d_j}
   \ge w_j2^{d_j}.
   \]
   It needs no basis of short units or uniform covering radius for
   a fundamental parallelepiped.

For any fixed admissible \(T\), the same argument and the factorial
asymptotic prove
\[
\liminf_j\frac{\log|U_j(T)|}{d_j}
\ge 1+\log L(T)-C_R.
\tag{10}
\]
There is no extra \(3\log3\) to subtract: it is already in \(C_R\).

## 4. Where are the counted units, and are they useful?

**PROVED location; incomplete distribution.** All counted units lie in
the \(\ell^1\) ball of radius \(d_jL(T_*)\), and
\[
h(u)=\frac{\|\ell_j(u)\|_1}{3d_j}\le L(T_*)/3.
\]
Their individual conjugates are only bounded by \(e^{d_jL(T_*)}\).
The population proof gives no favorable distribution among coordinate
directions or log-height shells.

For \(H=\|\ell_j(u)\|_1\), let
\[
E(u)=\sum_i(|\ell_j(u)_i|-\log2)_+,\qquad
w(u)=e^{-2E(u)},\qquad Z_j(T)=\sum_{u\in U_j(T)}w(u).
\]
The [geometry proof](geometry-audit.md) establishes
\[
e^{-2H}\le w(u)\le\min(1,4^{d_j}e^{-2H}),\qquad
w_j\le Z_j(T)\le |U_j(T)|.
\tag{11}
\]
The continuous overlap fraction of the Cartesian Minkowski window
under \(M_u\) is at most \(w(u)\).
Thus \(Z_j\) is an **upper-bound diagnostic** for a continuous mean,
not a lower bound for actual discrete returns.

**Increasing \(T\).** For each fixed field, \(Z_j(T)\) increases to a
finite weighted lattice sum, whereas \(|U_j(T)|\to\infty\).
Consequently \(Z_j(T)/|U_j(T)|\to0\) in that fixed-field limit:
the growing inventory eventually has vanishing average overlap weight.
This does not establish a tower-uniform conclusion at the particular
fixed radius (9). The weighted sum comparison retains the unknown
log-lattice shape cost explicitly.

The crude lower estimate obtained from (10) and
\(Z_j(T)\ge e^{-2d_jL(T)}|U_j(T)|\) has rate
\[
1+\log L(T)-C_R-2L(T)\le-C_R-\log2<0.
\tag{12}
\]
This says only that this estimate supplies no positive weighted rate.
It is not an upper bound on \(Z_j\), a return obstruction, or a refutation
of the carrier.

**PROVED discrete comparison, with losses retained.** For the actual
source domain \(D_u(T)=\{p\in C_j(T)^2:M_up\in C_j(T)^2\}\),
half-unit cell packing gives
\[
\frac{|D_u(T)|}{n_j^2}
\le
\left[\frac{4D_*^3}{\pi^2}(2+1/T)^6\right]^{d_j}
\prod_i
\min\left(1,
 \left[\frac{2Te^{-|\ell_j(u)_i|}+1}{T+1/2}\right]^2\right).
\tag{13}
\]
The additive \(1\) accounts for cell inflation at thin strips. The
exponential prefactor pays for the actual scalar density. Neither may
be removed to identify the discrete return fraction with \(w(u)\).
This is an upper bound; it supplies no lower tail.

## 5. Full support, status and one next lemma

The inspected same-set lemma states
\[
|Q(A_j,A_j)|\le n_j^2/R+|\{p:R_j(p)<R\}|.
\tag{14}
\]
Outputs with a good source have at least \(R\) distinct full-fiber
members; all remaining outputs are charged to bad sources.
The action orbits need not equal the complete polynomial fibers.

**OPEN.** No fixed positive return exponent \(\kappa\), exception
exponent \(\eta\), or compression exponent \(c\) has been proved here.
The number \(2^{d_j}\) in (1) counts candidate actions, not the value
of (7) at a typical source. The status change is exactly
“MS-O1 OPEN” to “MS-O1 PROVED.”

**One next lemma — MS-O2, actual incidence concentration, OPEN.**
Keep exactly (3), (6), and (9). On
\(\Omega_j=A_j^2\setminus\{(0,0)\}\), put \(N_j=n_j^2-1\) and
\[
D_{j,u}=\{p\in\Omega_j:M_up\in A_j^2\},\quad
S_{1,j}=\sum_u|D_{j,u}|,\quad
S_{2,j}=\sum_{u,v}|D_{j,u}\cap D_{j,v}|,\quad
\mu_j=S_{1,j}/N_j.
\]
Prove or refute the existence of fixed \(\kappa,\eta>0\) such that,
for every sufficiently large \(j\),
\[
\boxed{\mu_j\ge e^{\kappa d_j},\qquad
\frac{S_{2,j}}{N_j}-\mu_j^2\le e^{-\eta d_j}\mu_j^2.}
\tag{15}
\]
This is one explicitly specified sufficient incidence lemma. It is
stronger than merely having many units or a large mean, and is not
claimed necessary for power saving. Refuting (15) alone would not
retire this carrier. Recording it does not start a new search.

**PROVED implication MSU-R1.** On \(\Omega_j\), action freeness makes
the mean and variance of (7) exactly the quantities in (15).
Chebyshev's inequality bounds the number with fewer than \(\mu_j/2\)
returns by \(4N_je^{-\eta d_j}\). Charging the origin once, (14) gives
\[
|Q(A_j,A_j)|
\le 2n_j^2e^{-\kappa d_j}
+   4(n_j^2-1)e^{-\eta d_j}+1.
\tag{16}
\]
Using (4), every
\[
0<c<\frac{\min(\kappa,\eta)}{3\log(2T_*+1)}
\tag{17}
\]
would work eventually, after absorbing constant factors.
The additive \(1\) causes no extra restriction: the mean premise
and \(\mu_j\le n_j^2-1<e^{2B(T_*)d_j}\) force
\(\kappa<2B(T_*)\). Thus every \(c\) in (17) is less than 2.
No premise of (15) is established by this report.

## 6. Audit and execution boundary

The lead derived and independently checked the arithmetic argument;
the arithmetic specialist wrote and challenged the complete proof;
the separate geometry/rate specialist independently audited that
written proof and accepted MSU-A1–A3. The lead also checked MSU-G1–G3.
These are local internal proof checks, not external peer review.

No field data were enumerated and no mathematical program was required:
**0 charged exact evaluations; 0 research-program CPU seconds.**
Administrative repository and preservation checks are recorded separately
in [verification.md](verification.md), within the shared cap.
There was no carrier mutation, historical scout rerun, network access,
literature search, novelty claim, or commit.
