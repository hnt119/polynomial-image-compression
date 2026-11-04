# MS-O2 — Typical-Pair Unit Returns

21 October 2026 · T03 · version 1 · strictly offline.
Fixed polynomial \(Q(x,y)=x^2+xy+y^2\).

## 1. Result

**OPEN — MS-O2 and its weaker return-tail/inverse-moment endpoints.**
This cycle does not prove an exponential actual return mean, a small
low-return population, or a fixed compression exponent \(c>0\).
It does not refute those statements or retire this scalar carrier.

The new proved results are:

1. Exact source-dependent log-and-phase conditions for genuine returns,
   including every real and complex embedding.
2. A genuinely discrete lower incidence bound, with an explicit signed
   deficit when combined with the frozen population estimate.
3. An exact orbit partition: because the finite inventory is exhaustive
   for nonzero returns, \(R_j(p)\) is the size of the full order-unit
   orbit's intersection with the actual Cartesian square.
4. Consequently the inverse-return sum equals the number of occupied
   joint labels \((zR_j,N_{E_j/K_j}z)\), not necessarily the number of
   quadratic outputs.

**Meaning.** The remaining step is a bound on actual occupied arithmetic
orbits. Counting all units in a centered log ball does not establish
such a bound. The explicit lower incidence argument tried here also
does not establish exponential mean growth.

MS-O1 remains **PROVED** and was used as a frozen input, not reproved.
The field, order, radius, complete scalar carrier and action inventory
are unchanged. The seed-plus-torsion certificate stays closed, the
balanced-factor carrier stays retired, and RC15/4 is not pursued.

### Companions

- [Exact source windows and global phases](source-windows.md).
- [Discrete lower incidence and its signed deficit](lower-incidence.md).
- [Exact incidences, orbit labels and inverse moments](incidences.md).
- [Independent proof and rate audit](audit.md).
- [Construction ledger, provenance and computation accounting](ledger-verification.md).
- [Machine-readable state](state.json).

## 2. Frozen construction and quantifiers

Use the [21 October population checkpoint](../2026-10-21-relative-unit-population/README.md)
with its already fixed constants \(D_*,K_R,T_*\). In particular,
\[
K_j=F_j(s),\quad s^3+s+1=0,\qquad
E_j=K_j(\omega),\quad R_j=\mathcal O_{K_j}[\omega],
\]
\[
C_j=\{x\in\mathcal O_{K_j}:|\sigma x|\le T_*
                     \text{ at every embedding}\},\quad
A_j=\sigma_0(C_j),\quad n_j=|A_j|.
\]
The chosen real embedding is injective. Put
\[
a_*=\log\frac{(\pi/2)T_*^3}{D_*^{3/2}}>0,\qquad
B_*=3\log(2T_*+1).
\]
The inherited actual input bounds are
\[
e^{a_*d_j}\le n_j\le e^{B_*d_j}.
\tag{1}
\]
No input-growth limit is assumed. All fixed parameters precede \(j\).

Let
\[
\mathcal G_j=\{u\in R_j^\times:u\tau(u)=1\},\qquad
U_j=\{u\in\mathcal G_j:\|\ell_j(u)\|_1\le d_jL(T_*)\},
\quad L(T)=\tfrac12\log(48T^6).
\]
For \(u=a+b\omega\), the genuine global action is
\[
M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},\qquad
Q(M_up)=Q(p).
\]
Let \(\Omega_j=A_j^2\setminus\{(0,0)\}\), \(N_j=n_j^2-1\), and
\[
D_{j,u}=\{p\in\Omega_j:M_up\in A_j^2\},\qquad
R_j(p)=\#\{M_up:u\in U_j,\ M_up\in A_j^2\}.
\tag{2}
\]
The coefficients are evaluated at \(\sigma_0\); membership means that
the two algebraic coordinates satisfy every defining bound of \(C_j\).
Distinct units have distinct targets off zero. The inventory includes
every nonzero order-unit return, even when the returning multiplier
was initially described as a product of other units.

## 3. Exact source-dependent geometry

Suppress \(j\) and write \(T=T_*\). At a complex place of \(K\), let
\[
z=\sigma(x)-\eta\sigma(y),\quad
w=\sigma(x)-\eta^2\sigma(y),\quad
t=\widetilde\sigma(u)=e^{\lambda+i\theta},
\quad \eta\in\{\omega,\omega^2\}.
\]
For a nonzero source, both \(z,w\) are nonzero: they are embeddings
of nonzero field elements. Exact target coordinates are
\[
y'=\frac{t^{-1}w-tz}{\eta-\eta^2},\qquad
x'=\frac{\eta t^{-1}w-\eta^2tz}{\eta-\eta^2}.
\tag{3}
\]
Thus the exact local conditions are the two modulus inequalities
obtained from (3) with right side \(T\).

In particular,
\[
\boxed{\log\frac{|w|}{2T}\le\lambda
                  \le\log\frac{2T}{|z|}.}
\tag{4}
\]
The width and center are
\[
\log\frac{4T^2}{|\sigma Q(x,y)|},\qquad
c_p=\tfrac12\log\frac{|w|}{|z|}.
\tag{5}
\]
These are necessary translated log intervals, not sufficient returns.

The exact phase dependence can also be written explicitly. Put
\[
h=|zw|,\quad r=\lambda-c_p,\quad
\phi=2\theta+\arg z-\arg w.
\]
The two coordinate constraints become
\[
\cos\phi\ge b_p(r),\qquad
\cos(\phi+\arg\eta)\ge b_p(r),\qquad
b_p(r)=\cosh(2r)-\frac{3T^2}{2h}.
\tag{6}
\]
At a real place choose the extension with image \(\omega\).
Write \(z=\sqrt q\,e^{i\psi}\), \(q=Q(\sigma x,\sigma y)>0\),
and \(t=e^{i\theta}\). With \(\chi=\theta+\psi\), the conditions are
\[
|\sin\chi|,\ |\sin(\chi+\pi/3)|
\le\frac{\sqrt3T}{2\sqrt q}.
\tag{7}
\]
Thus the absence of a real log coordinate does not remove real-place
phase constraints.

All complex phases are harmless if
\[
h\le3T^2/4,\qquad
|\lambda-c_p|\le
\operatorname{arcosh}\frac{\sqrt3T}{2\sqrt h};
\tag{8}
\]
all real phases are harmless if \(q\le3T^2/4\).
These provide a sufficient box only for the sources satisfying all
these conditions. Their actual source population is not proved to be
large, and no exceptional population is discarded.

The frozen relative-log cover consists of exponentially many translated
lattice neighborhoods of radius proportional to \(d_j\). It does not
select the particular source translate in (4) or the globally compatible
phases in (6)–(7). A log vector's possible phase lifts come from actual
units and one global torsion fiber; they cannot be chosen independently
at different places. The precise limitations of applying the old cover
are proved in [source-windows.md](source-windows.md).

## 4. Actual discrete first-moment attempt

The previous continuous weight and inflated discrete comparison were
upper bounds. This cycle instead proves a lower bound by putting a
phase-independent product body inside
\(W_T^2\cap M_u^{-1}W_T^2\), then applying centered lattice counting.
For \(H(u)=\|\ell_j(u)\|_1\), it gives
\[
|D_{j,u}|+1\ge
\left(\frac{3\sqrt3\pi^3T_*^6}{512D_*^3}\right)^{d_j}
e^{-2H(u)}.
\tag{9}
\]
The proof pays the real ellipse volumes, complex Jacobians, pair-lattice
covolume and \(6d_j\)-dimensional half-body cost. The origin is subtracted
for each unit before summing.

Using units with \(H(u)\le hd_j\) to lower-bound the same full
inventory mean gives the guaranteed rate
\[
\rho_{\rm cert}(h)
=\log P_*+1+\log h-\log K_R-2h,\qquad
P_*=\frac{3\sqrt3\pi^3}{512D_*^3(2+1/T_*)^6}.
\]
The exact optimization is
\[
\boxed{\sup_{h>0}\rho_{\rm cert}(h)
       =\log\frac{P_*}{2K_R}<0.}
\tag{10}
\]
The maximizing \(h=1/2\) is admissible for this estimate at the fixed
radius. Full details are in [lower-incidence.md](lower-incidence.md).

**FAILED IN STATED SCOPE:** this particular lower-bound combination
does not certify exponential mean growth. Equation (10) is not an upper
bound for the true mean and does not refute MS-O2. The actual universal
baseline is \(R_j(p)\ge2\), because both \(p\) and \(-p\) return.
No lengthy second-moment calculation is built on an unproved exponential
first moment.

## 5. Exact orbit accounting and the inverse-return route

Let \(\mathscr C_j\) be the set of nonempty intersections of full
\(\mathcal G_j\)-orbits with \(\Omega_j\). If such an intersection has
size \(m\), every one of its points has return count exactly \(m\):
every target in that intersection is reached by a unit, and the
exhaustive cutoff places that unit in \(U_j\).

If its component sizes are \(m_1,\ldots,m_{\nu_j}\), then
\[
N_j=\sum_i m_i,\qquad
S_1=\sum_i m_i^2,\qquad S_2=\sum_i m_i^3,\qquad
\boxed{N_j\,\mathbb E_{\Omega_j}[1/R_j]=\nu_j.}
\tag{11}
\]
These are exact discrete identities. They do not infer a lower tail
from a large mean.

For \(z=x-\omega y\ne0\), the component label is exactly
\[
\boxed{(zR_j,\ z\tau z).}
\tag{12}
\]
Equal principal \(R_j\)-ideals imply that the ratio is an order unit;
equality of the exact relative-norm element makes its norm one.
Conversely a norm-one order unit preserves both labels. This proof
works in the nonmaximal order without assuming unique factorization
there. A maximal-order label can split into at most \(27^{d_j}\)
order-unit components; that cost is not silently omitted.

The attempted ambient ideal-divisor bound in
[incidences.md](incidences.md) is too large after all costs. It does not
give \(\nu_j/N_j\) exponential decay. It is an upper certificate that
fails to establish a gain, not an actual lower bound for \(\nu_j\).

Since \(Q\) is constant on each component and zero is the only source
of output zero,
\[
\boxed{|Q(A_j,A_j)|\le1+\nu_j
       =1+N_j\mathbb E_{\Omega_j}[1/R_j].}
\tag{13}
\]
Different components can have the same output. Equal-\(Q\) field ratios
need not be integral order units. Consequently failure of this certificate
would not establish a lower bound for the full quadratic image.

If the still-unproved estimate
\(\mathbb E[1/R_j]\le C_1e^{-\gamma d_j}\) held, Markov's inequality
would give
\[
\Pr[R_j<e^{\kappa d_j}]
\le C_1e^{-(\gamma-\kappa)d_j}\quad(0<\kappa<\gamma).
\]
More directly, (13) and (1) would yield every
\[
0<c<\gamma/B_*.
\tag{14}
\]
The origin and constants are absorbed by strictness; the independent
audit checks the allowable rate range. No positive \(\gamma\) is proved.

## 6. Status and one unresolved lemma

The main incidence-concentration statement, the weaker direct tail and
the inverse-moment estimate all remain **OPEN**. Neither a positive
compression exponent nor a retirement theorem follows. The exact
discrete obstruction to the attempted estimates is quantified by (10)
and the ideal-count ledger, not by an asserted failure of actual returns.

**One next lemma — MS-O2-I, actual occupied joint-label bound, OPEN.**
For the unchanged \(C_j,R_j,T_*\), set
\[
Z_j=\{x-\omega y:(x,y)\in C_j^2\setminus\{0\}\}.
\]
Prove or refute the existence of fixed \(\gamma>0,C_1<\infty,j_0\)
such that
\[
\boxed{\#\{(zR_j,z\tau z):z\in Z_j\}
\le C_1(n_j^2-1)e^{-\gamma d_j}
\quad(j\ge j_0).}
\tag{15}
\]
This is the exact inverse-return endpoint for this carrier, expressed
as an arithmetic label count. It controls all actual sources; no
sparse favorable subset or geometric proxy is substituted. It is not
claimed true and no new research cycle is started by recording it.
Even its refutation would concern the integral-unit certificate,
not automatically the full quadratic image or another subsequence.
