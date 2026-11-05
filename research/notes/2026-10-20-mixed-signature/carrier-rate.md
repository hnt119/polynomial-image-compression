# Mixed signature scalar carrier and return rate

20 October 2026 · T03 / shared full-rank quadratic direction · version 1.
Fixed polynomial \(Q(x,y)=x^2+xy+y^2\).

**PROVED:** the prescribed all-conjugate lattice window gives an exponentially
growing finite real scalar set. The complete finite order-unit inventory
containing every nonzero return is explicit. The inherited seed, even
multiplied by every available torsion unit, supplies only subpolynomial
returns. **OPEN:** the return tail for the entire rank-\(d_j\) relative unit
group, and the actual quadratic-image rate of this carrier.

## 1. Parameters and exact construction

Fix the accepted C0 totally real tower \(F_j\) and its constant \(D_0\) first.
The source is
`local-only/migration/research_supplement/shared/Phase_C0_Corrected.md`,
§5.1. Set
\[
d_j=[F_j:\mathbb Q]\longrightarrow\infty,\qquad
D_*=D_0\,31^{1/3},\qquad
K_j=F_j(s),\quad E_j=K_j(\omega),\quad R_j=\mathcal O_{K_j}[\omega],
\tag{1}
\]
where \(s\) is the real root of \(s^3+s+1\) and
\(\omega=(-1+i\sqrt3)/2\). The
[field audit, MS-F1](field-units.md#2-ms-f1--degrees-signatures-and-discriminants)
proves degree \(3d_j\), signature \((d_j,d_j)\), and
\(\operatorname{rd}(K_j)\le D_*\).

Choose one fixed real radius
\[
T>\sqrt{D_*}(2/\pi)^{1/3}.
\tag{2}
\]
One explicit admissible choice is \(T_0=2\sqrt{D_*}\). Fix one real
embedding \(\sigma_0:K_j\hookrightarrow\mathbb R\) at each level and put
\[
C_j(T)=\{x\in\mathcal O_{K_j}:|\sigma(x)|\le T
                \text{ for every embedding }\sigma:K_j\hookrightarrow\mathbb C\},
\qquad A_j(T)=\sigma_0(C_j(T)),\qquad n_j=|A_j(T)|.
\tag{3}
\]
Complex conjugate embeddings give identical modulus constraints; all of
them are included. The scalar carrier is the entire set (3). There is no
orbit completion, deleted boundary, selected component, or input thinning.

## 2. MS-C1 — finite injective carrier with exponential growth

**Theorem — PROVED.** The set (3) is finite, centrally symmetric, contains
zero, and has no projection multiplicity. For every \(T>0\),
\[
\boxed{\quad
\left(\frac{(\pi/2)T^3}{D_*^{3/2}}\right)^{d_j}
\le n_j
\le (2T+1)^{3d_j}.
\quad}
\tag{4}
\]
In particular the fixed choice \(T_0\) gives
\[
(4\pi)^{d_j}\le n_j\le(4\sqrt{D_*}+1)^{3d_j}.
\tag{5}
\]

**Proof.** Drop \(j\) temporarily. Embed \(\mathcal O_K\) as its
Minkowski lattice \(\Lambda_K\) in \(\mathbb R^d\times\mathbb C^d\), using
ordinary real and imaginary coordinates. Its covolume is
\(2^{-d}\sqrt{|D_K|}\). The corresponding compact symmetric convex body is
\[
W_T=[-T,T]^d\times\{z\in\mathbb C:|z|\le T\}^{d},
\qquad \operatorname{vol}(W_T)=(2\pi)^dT^{3d}.
\tag{6}
\]
A compact set meets a lattice in finitely many points. Negation preserves
both the lattice and the body. The field homomorphism \(\sigma_0\) is
injective; thus distinct algebraic integers remain distinct real scalars.

Average the number of lattice points in translates of \(W_{T/2}\) over
a fundamental domain. The average is its volume divided by the lattice
covolume, so some translate contains at least
\[
\frac{\operatorname{vol}(W_{T/2})}{2^{-d}\sqrt{|D_K|}}
=\frac{(\pi/2)^dT^{3d}}{\sqrt{|D_K|}}
\tag{7}
\]
lattice points. Subtract one point from every point in that translate.
The differences remain distinct lattice points and belong to
\(W_{T/2}-W_{T/2}=W_T\). Since
\(\sqrt{|D_K|}\le D_*^{3d/2}\), this proves the lower bound in (4).
This is a centered count, not an assumption that the body itself is
equidistributed.

For distinct \(x,y\in\mathcal O_K\), the absolute norm of \(x-y\) is a
nonzero integer. Consequently at least one embedding satisfies
\(|\sigma(x-y)|\ge1\): if every modulus were less than 1, their product,
with complex places counted twice, would be less than 1.
The interiors of the bodies \(x+W_{1/2}\), for \(x\in C_K(T)\),
are therefore pairwise disjoint. They all lie in \(W_{T+1/2}\).
Comparing volumes proves
\[
n\le
\frac{\operatorname{vol}(W_{T+1/2})}{\operatorname{vol}(W_{1/2})}
=(2T+1)^{3d}.
\]
Equations (2) and (5) now follow. \(\square\)

Write
\[
a(T)=3\log T+\log(\pi/2)-\tfrac32\log D_*>0,\qquad
B(T)=3\log(2T+1).
\tag{8}
\]
Then \(e^{a(T)d_j}\le n_j\le e^{B(T)d_j}\) exactly. No limiting input
growth constant is asserted or needed.

## 3. Exact finite global actions and genuine returns

Let \(\tau\) be the involution of \(E_j/K_j\). Define the order-unit group
\[
\mathcal G_j=\{u\in R_j^\times:u\tau(u)=1\}.
\]
For \(u=a+b\omega\), the whole-scalar identity is
\[
M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},\qquad
Q(M_u(x,y))=Q(x,y),\qquad M_u\in\mathrm{SL}_2(\mathcal O_{K_j}).
\tag{9}
\]
It is proved by multiplying \(u(x-\omega y)\), not by independent
rotations of embeddings. Its inverse is \(M_{\tau u}\).

Choose one extension to \(E_j\) of each representative complex embedding
of \(K_j\), and define the \(d_j\)-component vector
\(\ell_j(u)=(\log|\widetilde\sigma(u)|)_\sigma\). Put
\[
L(T)=\tfrac12\log(48T^6),\qquad
\boxed{U_j(T)=\{u\in\mathcal G_j:\|\ell_j(u)\|_1\le d_jL(T)\}.}
\tag{10}
\]
This is a finite set of actual algebraic units, with equality in \(E_j\)
used to deduplicate it. It contains 1. The
[window proof, MS-W1](window-returns.md#2-ms-w1--exact-action-and-the-complex-return-domain)
establishes that it contains **every order-unit return at every nonzero
pair of (3)**. Its derivation is
\[
1\le|N_{K_j/\mathbb Q}Q(x,y)|
\le (48T^6)^{d_j}e^{-2\|\ell_j(u)\|_1}.
\tag{11}
\]
The complex places supply the square in the absolute norm. Each
unit in (10) has absolute logarithmic height
\[
h(u)=\frac{\|\ell_j(u)\|_1}{3d_j}\le \frac{L(T)}3.
\tag{12}
\]
Bounded height and bounded degree at each level prove finiteness; the
relative-unit logarithmic lattice gives the same conclusion.

For \(p=(\sigma_0x,\sigma_0y)\in A_j^2\), define
\[
R_j(p)=
\#\{(\sigma_0x',\sigma_0y'):
(x',y')=M_u(x,y)\in C_j(T)^2,\ u\in U_j(T)\}.
\tag{13}
\]
Both target coordinates must satisfy all the constraints in (3).
There are no labels, formal addresses or embeddingwise choices in (13).
If \(p\ne0\), then \(x-\omega y\ne0\), and equality of two target pairs
implies equality of the multipliers. Thus (13) counts units with
multiplicity one at nonzero pairs. At the origin it is exactly one.

### The cost of the unit inventory

Use the Euclidean normalization of the relative logarithmic covolume
\(\mathcal R_{R,j}=\det\ell_j(\mathcal G_j)\) in
[MS-F4–F6](field-units.md#5-ms-f4--exact-logarithmic-and-height-accounting).
Let \(w_j\) be its torsion multiplicity and \(S_j\) the half-sum of
the \(\ell^1\)-norms of a lattice basis. Then
\[
6\le w_j\le8d_j^2,\qquad
\mathcal R_{R,j}\le3^{3d_j}\mathcal R_{E,j},
\tag{14}
\]
where \(\mathcal R_{E,j}\) denotes the maximal-order **relative**
logarithmic covolume, not an ordinary regulator. With \(H=d_jL(T)\),
\[
w_j\frac{H^{d_j}}{d_j!\mathcal R_{R,j}}
\le |U_j(T)|
\le
w_j\frac{2^{d_j}(H+S_j)^{d_j}}{d_j!\mathcal R_{R,j}}.
\tag{15}
\]
These are genuine counts with the shape and covolume costs visible.
There is no positive action exponent proved here. For example, the
unproved premise \(\mathcal R_{E,j}\le e^{C_Rd_j+o(d_j)}\) would imply
only the conditional lower action rate
\[
\liminf_j\frac{\log |U_j(T)|}{d_j}
\ge 1+\log L(T)-C_R-3\log3.
\tag{16}
\]
It would not prove a return tail.

## 4. MS-C2 — full support and the signed rate

**Theorem — PROVED implication.** Let \(A\) be any finite real set of
size \(n\), and count distinct genuine \(Q\)-preserving targets as in
(13). For \(R\ge1\), let
\(\mathcal E=\{p\in A^2:R_A(p)<R\}\). Then
\[
\boxed{|Q(A,A)|\le n^2/R+|\mathcal E|.}
\tag{17}
\]

**Proof.** Partition the outputs into those with a source outside
\(\mathcal E\) and those with all sources in \(\mathcal E\). Each output
of the first kind has at least \(R\) distinct members of its full fiber.
The fibers are disjoint subsets of \(A^2\), so there are at most \(n^2/R\)
such outputs. Every remaining output has at least one exceptional
source, so there are at most \(|\mathcal E|\) of them. \(\square\)

This reproves the needed specialization of the established
[HR-1 full-support lemma](../2026-09-16-high-return/return-lemma.md).
It does not identify action orbits with complete fibers; only containment
of returned pairs in the full fiber is needed.

For fixed \(T\), suppose **additionally** that fixed \(\kappa,\eta>0\)
and \(C_1<\infty\) satisfy
\[
R_j(p)\ge e^{\kappa d_j}\quad(p\notin\mathcal E_j),\qquad
|\mathcal E_j|\le C_1n_j^2e^{-\eta d_j}.
\tag{18}
\]
By (8),
\[
|Q(A_j,A_j)|
\le n_j^{2-\kappa/B(T)}+C_1n_j^{2-\eta/B(T)}.
\tag{19}
\]
Consequently every fixed
\[
0<c<\min(\kappa,\eta)/B(T)
\tag{20}
\]
would work eventually. Equivalently, a directly proved pair tail in
terms of \(n_j^\varepsilon\) and \(n_j^{2-\delta}\) gives
every \(c<\min(\varepsilon,\delta)\). The strict inequality absorbs
constant prefactors.

For the present construction, **both rates in (18) are OPEN**.
Equation (15) counts candidate actions, and the continuous overlap bound
\[
\frac{\operatorname{vol}(W_T^2\cap M_u^{-1}W_T^2)}
     {\operatorname{vol}(W_T^2)}
\le \prod_{\sigma\ {\rm complex}}\min(1,4e^{-2|\ell_\sigma(u)|})
\tag{21}
\]
is an upper bound for a different measure. Neither establishes (18).
The fixed-field lattice-dilation error is not uniform in \(j\).
Taking larger \(T_j\) to improve such an error also changes \(a(T_j)\),
\(B(T_j)\), the height cutoff, and every rate conversion.

## 5. MS-C3 — even seed powers with all torsion have zero return exponent

The fixed seed \(u_0=s^2+s\omega\) has a complex modulus \(\rho>1\)
in each of the \(d_j\) expanding blocks, after the extension choices
are fixed. The same constant \(\rho\) works at every level.
[MS-W3](window-returns.md#5-ms-w3--every-source-has-only-logarithmically-many-seed-power-returns)
proves this and the identity \(u_0\tau(u_0)=1\).

**Theorem — PROVED scoped obstruction.** For the group
\[
\mathcal H_j=(\mu(E_j)\cap R_j)\,\langle u_0\rangle,
\tag{22}
\]
every nonzero source in \(C_j(T)^2\), for \(T\ge1\), has at most
\[
w_j\left(1+2\left\lfloor\frac{L(T)}{\log\rho}\right\rfloor\right)
\tag{23}
\]
distinct returning targets. At zero there is one. For every sequence
of radii \(T_j\ge T_0\), this bound is \(O((\log n_j)^3)\), with a fixed
constant depending only on the accepted tower bound and the cubic seed.

**Proof.** Torsion has logarithmic vector zero, so
\(\|\ell_j(\zeta u_0^k)\|_1=d_j|k|\log\rho\).
Equation (11) gives \(|k|\le L(T)/\log\rho\), including negative \(k\).
There are at most \(w_j\) choices of \(\zeta\) for each exponent.
In fact these units are distinct because \(u_0\) has infinite order;
an upper count already suffices. This proves (23).

The integers in \([-T,T]\) belong to \(C_j(T)\), so
\(n_j\ge2\lfloor T_j\rfloor+1>T_j\).
For \(T_j\ge T_0\), monotonicity of (4) gives
\(d_j\le(\log n_j)/\log(4\pi)\). Combining these inequalities with
\(w_j\le8d_j^2\) and \(L(T)=\tfrac12\log48+3\log T\) proves
the asserted bound. \(\square\)

**Meaning and consequence — FAILED IN STATED SCOPE.** For every fixed
\(\varepsilon,\delta>0\), eventually every source has fewer than
\(n_j^\varepsilon\) targets under (22). Thus its bad-pair set is exactly
\(A_j^2\), and cannot have size \(O(n_j^{2-\delta})\).
Any finite subset of (22) fails the same certificate. This includes all
integer powers, all tower torsion units, and all their products.

The conclusion concerns selected actions. It gives no upper bound on the
unrestricted full fiber, and no lower bound on \(|Q(A_j,A_j)|\).
Other independent relative units and nonintegral norm-one multipliers
are not excluded by this argument. The carrier is **not retired**.

## 6. Construction ledger

This ledger follows the repository's
[construction template](../../templates/CONSTRUCTION_LEDGER.md).

| Gain or cost | Exact bound and status |
|---|---|
| Input count | MS-C1: \(e^{a(T)d_j}\le n_j\le e^{B(T)d_j}\); \(T\) fixed first. |
| Input thinning, both coordinates | Zero in the baseline construction: no points are deleted. Any later typical-pair claim must charge all bad sources separately. |
| Parameter and scalar projection fibers | One, since \(\sigma_0\) is injective. No multiset is counted as a set. |
| Local sparsity and splitting | No saving imported. The original C0 selected primes need not retain their splitting under the new extensions. |
| Per-residue population | No residue sieve used; this entry is inapplicable. |
| Degrees and discriminants | Degrees \(3d_j,6d_j\); root-discriminant factors \(31^{1/3},\sqrt3\). The carrier lower rate pays \((3/2)\log D_*\) per \(d_j\). |
| Order and ideals | Additive index at most \(3^{3d_j/2}\); relative-unit subgroup index at most \(3^{3d_j}\). Only the latter is charged in (16); they are not added as independent losses. |
| Regulator and unit generators | Relative covolumes and basis radius retained in (15). Their tower growth is unknown here. Rank \(d_j\) does not remove these costs. |
| Class number | No ideal-class enumeration or principalization step is used. A future regulator argument via a class-number formula would have to state its extra input. |
| Heights and denominators | Exact height cutoff (12). Coefficient denominators are absent inside \(R_j\); the passage to that order is charged separately. |
| Archimedean window | Real intervals and complex disks all enforced. Nonreal eigenvalue moduli \(e^{\lambda},e^{-\lambda}\); (21) measures a loss, not a gain. |
| Branches, states, carries | One window, no auxiliary states, no digit carries or local action branching. Global units cannot be selected independently at different embeddings. |
| Torsion and stabilizers | \(w_j\le8d_j^2\); distinct units act freely at nonzero pairs. Zero has one target. Torsion is not counted twice in relative covolume conversion. |
| Exceptional outputs | At most one output per bad ordered source in (17); no power-saving bad-source estimate is proved. |
| Full output exponent | Only the tautological upper bound \(n_j^2\) is unconditional for this carrier in this cycle. No fixed positive gap is certified. |
| Conditional signed gap | From (18), any \(c<\min(\kappa,\eta)/B(T)\). Both positive rates remain unproved. |
| Seed certificate | MS-C3 gives return rate zero, even with torsion; its bad-source population is the entire square eventually. |

Claim records MS-C1–C3 have the quantifiers in §§2, 4, 5 and dependencies
MS-F1–F6 / MS-W1–W3. Their proof evidence is symbolic, with lead checking
and the independent review recorded in [audit.md](audit.md).
No mathematical program was required, and no empirical tail is reported.

## 7. One next bounded obligation

**MS-O1 — OPEN, necessary unit inventory gate.** For the unchanged tower
and the explicit inventory (10), prove or refute that there exist a
fixed \(T\ge T_0\), a fixed \(\alpha>0\), and \(j_0\) such that
\[
\boxed{\quad |U_j(T)|\ge e^{\alpha d_j}\quad
                 \text{for every }j\ge j_0.\quad}
\tag{24}
\]
This asks about actual order units at the finite height cutoff forced by
Cartesian return, not a formal rank or a basis-dependent list.
Any positive return tail holding at every sufficiently large level of this
fixed-radius tower necessarily implies such an action count: (4) and a
nonexceptional pair give
\(|U_j(T)|\ge n_j^\varepsilon\ge e^{a(T)\varepsilon d_j}\).
Refuting the uniform quantifiers in (24) alone would not exclude a successful
unbounded subsequence; a subsequence version of a return claim would require
only the corresponding subsequence action count.

An affirmative answer would still leave the source-dependent return and
exception inequalities in (18) to be proved. It is not adopted as a
sufficient replacement for the objective. This cycle introduces no window
mutation and makes no affine or difference-set claim.
