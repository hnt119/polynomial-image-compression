# Mixed-signature lattice windows: exact return constraints

**20 October 2026 · T03 / shared full-rank quadratic direction · version 1.**
Fixed polynomial \(Q(x,y)=x^2+xy+y^2\). This is the lattice-window
contribution to the authorized **C0 Mixed-Signature Lattice Symmetry**
cycle. The baseline window is unchanged. No correlated-window mutation,
new action family, mathematical program, or network request was made.
This specialist has zero evaluation and research-program CPU allocation;
the lead owns the shared 2,000,000-evaluation / 600-CPU-second budget and
its 20% verification reserve.

| Claim | Status and scope | Locator |
|---|---|---|
| MS-W1 | PROVED: exact diagonal action, local return domain, logarithmic necessary conditions, and a finite integral-unit cutoff containing every nonzero-pair return | §§2–3 |
| MS-W2 | PROVED: complex-bidisk overlap upper bounds; an explicit small domain contains all nonidentity seed-power returns in the continuous window and in each fixed-field lattice-dilation limit | §4 |
| MS-W3 | PROVED: all integer powers of the fixed cubic seed yield only \(O(\log n)\) actual returns at every pair, uniformly in field degree and window radius | §5 |

The seed-power certificate is therefore **FAILED** for positive-power
return amplification. The full rank relative-unit family and the actual
quadratic image are **OPEN** in this note. Failure of the selected action
family is not an actual-image lower bound. No external novelty is claimed.

## 1. Sources, field hypotheses and baseline

The seed and its complete integral norm-one argument are in the supplied
private source
`local-only/migration/sources/TFQ_Direct_Construction_and_Adaptive_Radical_Report.md`,
§G.4. That argument was inspected in this task. Corrected C0's separate
rank-one statement was read at
`local-only/migration/research_supplement/shared/Phase_C0_Corrected.md`,
Theorem C0.1; it is not a theorem for the present full-rank form.
The source hierarchy and relevant scoped norm-unit failures were checked
against the master handoff, T03 current state §§3 and 6, repository maps,
mechanism/failure entries, and the latest T03 checkpoint. The retired
balanced-factor carrier is not reused. This is not a fresh audit of those
unrelated historical proofs.

Let \(F\) be a totally real field of degree \(d\), let \(s\) be the
real root of \(s^3+s+1=0\), and assume
\[
K=F(s),\qquad [K:\mathbb Q]=3d,\qquad
(r_1(K),r_2(K))=(d,d).
\tag{1}
\]
The tower construction and degree/discriminant budget are separate
obligations; the arguments here apply to every field satisfying (1).
Fix a real embedding to realize scalar inputs in \(\mathbb R\).
Since \(K\) has a real embedding, \(\omega=e^{2\pi i/3}\notin K\).
Put
\[
E=K(\omega),\qquad \Delta=\omega-\omega^2,\qquad \Delta^2=-3.
\]
Write \(\iota\) for the nontrivial automorphism of \(E/K\), so
\(\iota(\omega)=\omega^2\). At a nonreal embedding of \(K\), this
relative involution must not be confused with complex conjugation of the
embedded coefficients.

For \(T\ge1\), the unchanged coefficient set is
\[
C_K(T)=\{a\in\mathcal O_K:
 |\sigma(a)|\le T\text{ at every real place and }
 |\tau(a)|\le T\text{ at every complex place}\},\qquad n=|C_K(T)|.
\tag{2}
\]
One representative per conjugate complex pair is used. A real embedding
is injective, so (2) is already the actual scalar set, with no projection
fibers. Its embedded window is a product of \(d\) real intervals and
\(d\) complex disks. The pair window is its full Cartesian square.

For automatic preservation of the coefficient lattice, use the order
\(R=\mathcal O_K[\omega]\), and the group
\[
\mathcal U_R=\{u\in R^\times:u\iota(u)=1\}.
\tag{3}
\]
An arbitrary relative norm-one unit of \(\mathcal O_E\) need not have
both coefficients integral in the basis \(1,\omega\); that order/index
issue cannot be omitted. All the necessary archimedean inequalities below
also apply to such a unit whenever its actual target has integral
coordinates. The finite cutoff may safely include that larger unit group,
but membership must still be checked.

## 2. MS-W1 — exact action and the complex return domain

Write \(u=a+b\omega\) with \(a,b\in K\). Its norm is
\(a^2-ab+b^2\). If this norm is 1, multiplication on
\(x-\omega y\) is exactly
\[
\begin{pmatrix}x'\\y'\end{pmatrix}
=M_u\begin{pmatrix}x\\y\end{pmatrix},\qquad
M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},\qquad
Q(x',y')=Q(x,y).
\tag{4}
\]
For \(u\in\mathcal U_R\), this is an integral matrix of determinant
1, with integral inverse. Thus only window return, rather than a hidden
denominator loss, remains for this group.

At a complex place \(\tau:K\to\mathbb C\), choose one extension
\(\widetilde\tau:E\to\mathbb C\), and denote its image of
\(\omega\) by \(\eta\in\{\omega,\omega^2\}\). With the local
coordinates still denoted by \(x,y\), set
\[
z=x-\eta y,\qquad w=x-\eta^2y,\qquad
t=\widetilde\tau(u),\qquad \lambda=\log|t|.
\]
Then the exact diagonalization is
\[
\boxed{(z,w)\longmapsto(tz,t^{-1}w),\qquad Q(x,y)=zw.}
\tag{5}
\]
For a nonreal place, \(w\) generally is not \(\bar z\), and
\(t^{-1}\) need not be \(\bar t\). Thus \(\lambda\ne0\)
produces genuine expansion in one complex direction and contraction in
the other. At a real place, instead, \(w=\bar z\) and \(|t|=1\).
Even there norm preservation need not preserve the coordinate square.

Let \(\Delta_\eta=\eta-\eta^2\). The bidisk
\(B_T=\{(x,y):|x|,|y|\le T\}\subset\mathbb C^2\) becomes
\[
\Omega_T=\{(z,w):|w-z|\le\sqrt3T,
 |\eta w-\eta^2z|\le\sqrt3T\}.
\tag{6}
\]
Indeed \(y=(w-z)/\Delta_\eta\) and
\(x=(\eta w-\eta^2z)/\Delta_\eta\). The local return domain is
**exactly** \(\Omega_T\cap\operatorname{diag}(t,t^{-1})^{-1}\Omega_T\).
It is not a rectangle in the eigencoordinates.

Source and target membership imply
\[
|z|,|w|\le2T,\qquad |tz|,|t^{-1}w|\le2T.
\tag{7}
\]
For a nonzero global pair, both eigencoordinates are nonzero at every
embedding: otherwise the algebraic equality \(x=\omega y\) or
\(x=\omega^2y\), with \(x,y\in K\), forces \(x=y=0\).
Consequently every returning unit satisfies the finite interval condition
\[
\boxed{
\log\frac{|w_\tau|}{2T}
\le\lambda_\tau(u)
\le\log\frac{2T}{|z_\tau|}
\quad\text{at every complex place.}
}
\tag{8}
\]
These inequalities are necessary, not sufficient: (6), integrality and
all real-place coordinate constraints still have to hold.

### A finite cutoff for all returning integral units

At each complex place, (7) gives
\[
|\tau(Q(x,y))|\le4T^2e^{-|\lambda_\tau(u)|}.
\tag{9}
\]
At a real place \(|\sigma(Q(x,y))|\le3T^2\). Since a nonzero pair
has \(Q(x,y)\in\mathcal O_K\setminus\{0\}\), its absolute field
norm is a positive integer. Remembering the exponent two on each complex
place therefore gives
\[
1\le|N_{K/\mathbb Q}Q(x,y)|
\le48^dT^{6d}\exp\left(-2\sum_\tau|\lambda_\tau(u)|\right).
\]
Thus
\[
\boxed{\sum_\tau|\lambda_\tau(u)|
\le B_d(T):=\frac d2\log(48T^6).}
\tag{10}
\]
In particular, every returning unit at a nonzero pair lies in the exact
finite set
\[
\mathcal U_K(T)=\{u\in\mathcal U_R:
\sum_\tau|\lambda_\tau(u)|\le B_d(T)\}.
\tag{11}
\]
Finiteness needs no unproved quantitative lattice count. All conjugates
of such an integral \(u\) have modulus at most \(e^{B_d(T)}\): those
above real places have modulus 1, while the others have moduli
\(e^{\pm\lambda_\tau}\). Its monic integer minimal polynomial has
degree at most \(6d\) and bounded coefficients, by the elementary
symmetric-function formulas. There are finitely many such polynomials
and roots. The same proof works for the larger group in
\(\mathcal O_E^\times\).

Distinct units give distinct targets at a nonzero pair, since
\(u_1(x-\omega y)=u_2(x-\omega y)\) implies \(u_1=u_2\).
At \((0,0)\), every unit has the same target and the actual return
count is one; (11) is not asserted to contain its infinite stabilizer.

## 3. What the logarithmic cutoff does and does not settle

For nonzero pairs the actual return problem for the order group has
become finite, with no arbitrary cutoff of the action inventory. However,
the admissible \(\lambda\)-vectors in (8) are the logarithms of
**global units**, not independently chosen coordinates. Even if the
relative unit rank is \(d\), that rank alone gives neither a useful
count in these source-dependent boxes nor a lower bound for actual
returns after imposing (6).

The kernel of the logarithm map is finite torsion. For an elementary
proof, a kernel unit has every conjugate of modulus 1. The same is true
of every power. Their monic integer minimal polynomials have uniformly
bounded degree and coefficients; only finitely many roots can occur,
so two powers agree and the unit is a root of unity. Its finite
multiplicity must still be charged in any count of units by logarithms.

The unresolved baseline task is therefore quantitative and involves
actual pair coverage: count the integral unit vectors in (11) which
satisfy all exact target inequalities, for all but a sufficiently small
set of sources. No regulator estimate, spacing bound, box-count lower
bound or return-tail conclusion is supplied merely by (10).

## 4. MS-W2 — overlap and a genuine seed-return exceptional set

### A local upper bound for any action

Normalize Lebesgue measure on the complex bidisk \(B_T\). If
\(\lambda\ge0\), (7) requires \(|x-\eta y|\le2Te^{-\lambda}\).
For each fixed \(y\) in its disk, possible \(x\) occupy area at most
\(\pi(2Te^{-\lambda})^2\). If \(\lambda<0\), use
\(|x-\eta^2y|\le2Te^{\lambda}\) instead. Therefore
\[
\boxed{
\frac{\operatorname{vol}(B_T\cap M_u^{-1}B_T)}
     {\operatorname{vol}(B_T)}
\le\min\{1,4e^{-2|\lambda|}\}.
}
\tag{12}
\]
Independence of the ambient product factors, not independence of global
units or of lattice points, yields the full continuous-window bound
\[
\frac{\operatorname{vol}(W_T^2\cap M_u^{-1}W_T^2)}
     {\operatorname{vol}(W_T^2)}
\le\prod_{\tau}\min\{1,4e^{-2|\lambda_\tau(u)|}\}.
\tag{13}
\]
Real-place overlap factors were bounded by 1 here. These are upper
bounds, so they cannot certify large returns from a large unit inventory.

For every fixed \(\rho>1\), there is also a useful strict gap even
when the right side of (12) is 1. Put
\[
\varepsilon_\rho=\frac{1-\rho^{-1}}4,
\qquad
\theta_\rho=\min\{4\rho^{-2},\,1-\varepsilon_\rho^4\}<1.
\tag{14}
\]
The condition \(|x-\eta y|\le2T/\rho\) has bidisk probability at
most \(\theta_\rho\). To see the strict gap, take the disk of radius
\(\varepsilon_\rho T\) centered at \((1-\varepsilon_\rho)T\)
for \(x\), and the disk of that radius centered at
\(-\eta^2(1-\varepsilon_\rho)T\) for \(y\). Both lie inside
their original disks. Throughout their product,
\[
|x-\eta y|\ge(2-4\varepsilon_\rho)T
=(1+\rho^{-1})T>2T/\rho.
\]
The product occupies fraction \(\varepsilon_\rho^4\), proving the
second bound in (14); the first is the slice estimate from (12). The
same argument holds with \(\eta\) replaced by \(\eta^2\).

### All powers of a repeated seed: a union bound independent of the number of powers

Suppose one fixed norm-one seed has, after choosing the extension at
each complex place, the same modulus \(\rho>1\) in all \(d\)
blocks. Every positive-power return, regardless of exponent, then lies
in the single set
\[
E_+=\{(x,y)\in W_T^2:
 |z_\tau|\le2T/\rho\text{ for every }\tau\};
\]
every negative-power return lies in the analogous \(E_-\) defined by
\(|w_\tau|\le2T/\rho\). Equations (14) and the product measure give
\[
\boxed{
\frac{\operatorname{vol}(E_+\cup E_-)}
     {\operatorname{vol}(W_T^2)}\le2\theta_\rho^d.
}
\tag{15}
\]
Outside this union there are no nonidentity seed-power returns. This is
a direct exceptional-set statement, not an inference of a typical tail
from high collision energy or a large mean. With actions \(\pm u^k\),
the outside return set consists of the simultaneous-sign targets only.

For each **fixed** field \(K\), the same density statement transfers
to \(\mathcal O_K^2\) as \(T\to\infty\):
\[
\frac{\#\{p\in C_K(T)^2:
 \text{some }u^k,\ k\ne0,\text{ returns}\}}{n^2}
\le2\theta_\rho^d+o_K(1).
\tag{16}
\]
Indeed the source window and \(E_\pm\) are fixed bounded sets scaled
by \(T\), with boundary of Lebesgue measure zero. Tiling by any fixed
fundamental parallelepiped of the Minkowski lattice shows that their
lattice counts, divided by \(T^{6d}\), tend to volume divided by
covolume: only cells meeting a shrinking boundary neighborhood can
contribute to the discrepancy. This also proves (16) for the union.

The error \(o_K(1)\) is not asserted uniform in a growing tower. A
sequence of sufficiently large radii can be chosen separately at each
field to make it small, but the resulting input/height cost must then be
charged by the lead. Formula (16) alone does not settle a prescribed
fixed-radius tower. The pointwise theorem next has no such limitation.

## 5. MS-W3 — every source has only logarithmically many seed-power returns

Take the explicit inherited seed
\[
u_0=s^2+s\omega.
\tag{17}
\]
It and its inverse belong to \(\mathcal O_K[\omega]\), because
\[
u_0\iota(u_0)=s^4-s^3+s^2=1,
\qquad
(s-1)(s^3+s+1)=s^4-s^3+s^2-1.
\tag{18}
\]
The cubic is irreducible by the rational-root test and has exactly one
real root, since its derivative is positive. Let \(s_c\) be either
nonreal root. The two values above that complex place are
\(s_c(s_c+\omega)\) and \(s_c(s_c+\omega^2)\); their product is 1.
Their moduli differ, since
\[
|s_c+\omega|^2-|s_c+\omega^2|^2
=2\sqrt3\,\operatorname{Im}(s_c)\ne0.
\tag{19}
\]
Thus exactly one has modulus \(\rho>1\). Switching the chosen
extension if needed makes the expanding modulus \(\rho\) at each
complex place. Every block restricts to one of this same fixed cubic's
two complex embeddings; consequently \(\rho\) is independent of
\(F,d,T\). In particular \(u_0\) has infinite order.

For a nonzero pair returning under \(u_0^k\), (10) gives
\[
d|k|\log\rho\le\frac d2\log(48T^6),
\qquad
\boxed{|k|\le H(T):=
\frac{\log48+6\log T}{2\log\rho}.}
\tag{20}
\]
Equivalently this follows directly from
\[
1\le|N_{K/\mathbb Q}Q(x,y)|
\le(3T^2)^d(4T^2\rho^{-|k|})^{2d}.
\]
The degree cancels. This bound is valid for every field satisfying (1),
every \(T\ge1\) and every nonzero source, with no lattice asymptotic.
Hence the number of actual targets under all integer powers satisfies
\[
\boxed{R_{\langle u_0\rangle}(x,y)
\le1+2\lfloor H(T)\rfloor=O(1+\log T).}
\tag{21}
\]
Allowing \(-u_0^k\) at most doubles this bound. At zero the actual
target count is exactly one, independently of the infinite stabilizer.
The constants are absolute for this fixed seed. At nonzero sources the
powers are distinct actions and distinct targets whenever they return;
there is no hidden action multiplicity being called a gain.

Since every integer of absolute value at most \(T\) belongs to
\(C_K(T)\),
\[
n\ge2\lfloor T\rfloor+1>T,\qquad n\ge3.
\tag{22}
\]
Thus (21) is \(O(\log n)\), uniformly in both tower degree and radius.
For every fixed \(\varepsilon>0\), all sources have fewer than
\(n^\varepsilon\) seed-power targets once \(n\) is sufficiently
large. No exceptional-set allowance rescues a near-full polynomial
return tail for this action family. This decisive statement concerns
only the fixed cyclic seed group (or its simultaneous-sign extension),
not a growing-rank group of other norm-one units.

## 6. Quantitative ledger and remaining gap

The applicable entries of the
[construction ledger](../../templates/CONSTRUCTION_LEDGER.md) are:

| Item | Charged statement |
|---|---|
| Input and parameter choice | The carrier (2) is unchanged. The exact field degrees/signature in (1) are hypotheses here. Full input lower/upper asymptotics and the tower's radius choice belong to the lead's lattice-count ledger; this proof only needs (22). |
| Projection and thinning | A real field embedding is injective. There is no input thinning, in either coordinate, and all ordered pairs are included in the pointwise seed bound. |
| Integral action | The seed and its inverse are in \(\mathcal O_K[\omega]\); their matrices act on \(\mathcal O_K^2\) with no denominator loss. For arbitrary \(\mathcal O_E\) units the coefficient-order condition must be checked. |
| Complex distortion | It is hyperbolic: local eigenvalue moduli are \(e^{\lambda},e^{-\lambda}\). Equations (6)–(10) charge this distortion; it is not treated as a rotation at nonreal places. |
| Field norm and degree | Complex places enter the absolute norm with exponent two. Degree \(3d\) for \(K\) and \(6d\) for \(E\) yields the exact factor \(48^dT^{6d}\). |
| Unit inventory and stabilizers | (11) is a finite exhaustive integral-unit cutoff for nonzero-pair returns. Logarithmic rank alone gives no usable count; the torsion kernel must be charged. Zero has one actual target. |
| Regulator and discriminant | No estimate for either is used or supplied here. They remain real costs in a quantitative growing-rank lattice-window construction; neither is declared bounded or zero. |
| Seed branches | Every integer power, including negative exponents, is included. The repeated cubic modulus gives at most \(1+2\lfloor H(T)\rfloor\) possible exponents; adjoining signs costs at most a factor two. |
| Local overlap and exceptions | (13) is an upper bound for continuous overlap. For the seed, the genuine continuous exceptional fraction is at most \(2\theta_\rho^d\); the lattice transfer (16) is fixed-field only. The stronger pointwise bound (21) is uniform and has no exceptional pairs. |
| Full image and exponent | No entire-image upper or lower bound is deduced. No positive compression exponent or net rate gap is certified. An upper bound for selected returns cannot be substituted for an upper bound on full fibers. |

The exact remaining full-rank-unit deficit is to bound actual lattice
returns inside the finite inventory (11), with the order condition, real
and complex inequalities, unit-log multiplicities, all-pair exceptions,
and tower costs charged simultaneously. This note supplies constraints
and a seed-family obstruction, not a new window designed to solve that
deficit. No additional mechanism is adopted here.

## 7. Evidence and audit scope

MS-W1–W3 are complete internal symbolic arguments above. The lead and
independent auditor checked the seed norm inequality and its uniform
\(O(\log n)\) consequence before final-file review. The independent
auditor subsequently read the complete MS-W1–W3 proofs, checked the local
domains, cutoff, overlap geometry, lattice-limit qualifier and uniform
seed bound, and reported a pass without corrections. That review is
recorded in this cycle's audit companion. No
numerical value of \(\rho\), lattice count, empirical tail, or source
rerun was used. Repository/setup checks are administrative checks to be
recorded by the lead; they do not establish these mathematical claims.
