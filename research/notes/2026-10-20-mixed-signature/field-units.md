# Mixed-signature field, order, and relative-unit audit

Date: 2026-10-20. Track: T03 / shared norm-quadratic direction.
Polynomial: \(Q(x,y)=x^2+xy+y^2\).
Scope: the fixed extension \(F\subset K=F(s)\subset E=K(\omega)\), where
\(F\) is totally real and \(s^3+s+1=0\) at its real root.

**Disposition.** The field and order supply integral norm-preserving actions
with relative unit rank \(d=[F:\mathbb Q]\). They do not by themselves supply
exponentially many useful actions in a fixed logarithmic window, or a
Cartesian-return theorem. The regulator and logarithmic covering radius are
retained explicitly below. This note proves no small-image construction.

## 1. Source and evidence boundary

The following local sources were read for this audit:

- `local-only/migration/research_supplement/shared/Phase_C0_Corrected.md`,
  §5.1, Lemma 5.1, and the accompanying `C0_CORRECTION_LOG.md`.
  The supplied field input is an infinite sequence of **totally real**
  \(F_j\), degrees tending to infinity, with bounded (indeed constant)
  root discriminant after the source parameter is fixed. Its source-selected
  primes split in \(F_j\). This note does not assert that they split in \(K_j\)
  or \(E_j\), and does not use a prescribed-prime theorem.
- `local-only/migration/sources/TFQ_Direct_Construction_and_Adaptive_Radical_Report.md`,
  §G.4: the explicit cubic seed \(s^2+s\omega\), its integral inverse, and
  its non-torsion proof.
- `local-only/migration/sources/T03_CURRENT_STATE.md`, §10, “Precise standard
  results assumed”: the existing algebraic-number-theory assumptions,
  including Dirichlet's unit theorem and cyclotomic degrees.

**EXTERNAL RESULT / inherited standard input.** We use Dirichlet's unit
theorem in its signature-and-logarithmic-lattice form: for signature
\((r_1,r_2)\), the unit group modulo its finite roots of unity is free of
rank \(r_1+r_2-1\), and its logarithms form a full lattice in the product-formula
hyperplane. The local source names this theorem; its general form is not
reproved or newly externally verified here. We also use the standard
discriminant tower and order-index identities and
\([\mathbb Q(\zeta_m):\mathbb Q]=\varphi(m)\). The applications and elementary
relative calculations are proved below.

Evidence: symbolic proofs, local source inspection, and internal review.
No network, literature search, mathematical program, finite search, or numerical
unit computation was performed by the author of this companion. The fixed
balanced-factor carrier remains retired; the old CM sieve result is unchanged.
This mixed-signature extension has different unit rank and is not covered by a
literal reuse of the CM finite-unit conclusion.

## 2. MS-F1 — degrees, signatures, and discriminants

**Statement — PROVED using the stated field input.**
Let \(F\) be totally real, \([F:\mathbb Q]=d\), and
\(\operatorname{rd}(F)\le D_0\). Choose the real root \(s\) of
\(f(T)=T^3+T+1\), set \(K=F(s)\subset\mathbb R\) at the chosen embedding,
and put \(E=K(\omega)\), where \(\omega^2+\omega+1=0\).
Then
\[
 [K:\mathbb Q]=3d,\quad (r_1(K),r_2(K))=(d,d),\qquad
 [E:\mathbb Q]=6d,\quad (r_1(E),r_2(E))=(0,3d),
 \tag{1}
\]
and
\[
 \operatorname{rd}(K)\le D_0\,31^{1/3},\qquad
 \operatorname{rd}(E)\le D_0\,31^{1/3}\sqrt3.
 \tag{2}
\]

**Proof.** The rational-root test proves \(f\) irreducible over \(\mathbb Q\).
Its derivative is positive on \(\mathbb R\), so its cubic field has exactly one
real embedding and one complex pair. If \(f\) became reducible over \(F\), a
cubic would have a root in \(F\); that root must be \(s\). A subfield of a
totally real field is totally real, because every embedding of the subfield
extends to the larger field. This contradicts the signature of
\(\mathbb Q(s)\). Thus \(f\) remains irreducible over \(F\).

Above each real embedding of \(F\), the same polynomial has one real root
and a complex pair. This proves the assertion for \(K\).
Because the chosen copy of \(K\) lies in \(\mathbb R\), it does not contain
\(\omega\). Adjoining \(\omega\) doubles the degree and leaves no real
embedding, proving (1).

The discriminant of \(f\) is \(-31\). The relative field discriminant of
\(K/F\) divides the discriminant of the order \(\mathcal O_F[s]\), namely
the ideal \((31)\). Similarly the relative discriminant of \(E/K\) divides
\((3)\), the discriminant ideal of the basis \(1,\omega\). Consequently
\[
 |D_K|\le |D_F|^3\,31^d,\qquad
 |D_E|\le |D_K|^2\,3^{3d}.
 \tag{3}
\]
Taking the indicated degree roots gives (2). No unramifiedness hypothesis at
3 or 31 is needed. \(\square\)

**Meaning.** The operation preserves bounded root discriminant and produces
mixed signature of a fixed proportion. \(E/K\) is a quadratic extension
with involution \(\tau(\omega)=\omega^2\), but \(K\) is not totally real;
therefore this is not a CM extension of a totally real base.

## 3. MS-F2 — the exact order and its loss

Use throughout
\[
 R=\mathcal O_K[\omega]=\mathcal O_K\oplus\mathcal O_K\omega,
 \qquad \delta=1+2\omega,\qquad \delta^2=-3.
 \tag{4}
\]
This is the order used for actions; it need not be the maximal order
\(\mathcal O_E\).

**Statement — PROVED.** Write \(J=[\mathcal O_E:R]\). Then
\[
 |D_R|=|D_K|^2\,3^{3d},\qquad
 J^2=\frac{3^{3d}}{N_{K/\mathbb Q}\mathfrak d_{E/K}},
 \qquad J\le 3^{3d/2}.
 \tag{5}
\]
The index is supported only at 3. If
\(\mathfrak f=\{z\in\mathcal O_E:z\mathcal O_E\subset R\}\) is the
conductor, then
\[
 \delta\mathcal O_E\subset\mathfrak f,\qquad
 3\mathcal O_E\subset\mathfrak f,\qquad
 [\mathcal O_E:\mathfrak f]\le3^{3d}.
 \tag{6}
\]
For \(U_E^1=\ker(N_{E/K}:\mathcal O_E^\times\to\mathcal O_K^\times)\)
and \(U_R^1=U_E^1\cap R^\times\),
\[
 [U_E^1:U_R^1]\le3^{3d}.
 \tag{7}
\]

**Proof.** The relative basis discriminant of \(1,\omega\) is \(-3\).
The absolute discriminant tower and order-index formula give (5).
For \(z=a+b\omega\in\mathcal O_E\), with initially \(a,b\in K\), the traces
\[
 t=\operatorname{Tr}_{E/K}z=2a-b,\qquad
 t'=\operatorname{Tr}_{E/K}(\omega z)=-a-b
\]
belong to \(\mathcal O_K\). Direct multiplication gives
\[
 \delta z=(a-2b)+(2a-b)\omega=(t+t')+t\omega\in R.
 \tag{8}
\]
Thus the \(\mathcal O_E\)-ideal \(\delta\mathcal O_E\) is contained in \(R\)
and hence in its conductor. The assertion for \(3=-\delta^2\) follows.
Moreover
\[
 |\mathcal O_E/\delta\mathcal O_E|
   =|N_{E/\mathbb Q}\delta|=3^{3d}.
\]
Every maximal-order unit congruent to 1 modulo \(\delta\mathcal O_E\),
and its inverse, belongs to \(R\). Restricting the reduction homomorphism
to \(U_E^1\) therefore bounds its index over \(U_R^1\) by
\(|(\mathcal O_E/\delta\mathcal O_E)^\times|\le3^{3d}\). \(\square\)

**Consequence.** There is no coefficient denominator for an action already
chosen in \(U_R^1\). Passing from maximal-order units to these actions can
nevertheless cost an exponential subgroup index. It is incorrect to call
this passage free merely because all action coefficients are integral.

## 4. MS-F3 — rank, torsion, and the fixed seed

**Statement — PROVED using Dirichlet's theorem.**
\[
 \operatorname{rank}U_E^1=\operatorname{rank}U_R^1=d.
 \tag{9}
\]
If \(w_E=|\mu(E)|\) and \(w_R=|\mu(E)\cap R|\), then
\[
 \mu(E)=\mu(F(\omega)),\qquad 6\le w_R\le w_E\le8d^2.
 \tag{10}
\]
The last bound is a convenient coarse degree bound, not an exact torsion count.

**Proof of rank.** The ranks of \(\mathcal O_E^\times\) and
\(\mathcal O_K^\times\) are \(3d-1\) and \(2d-1\). The norm image contains
the squares of every \(K\)-unit, so it has full rank \(2d-1\).
The norm kernel therefore has rank \(d\). Equation (7) gives the same
rank for the order subgroup.

**Proof of torsion.** The maximal totally real subfield of \(K\), in the
sense of containing every totally real subfield of \(K\), is \(F\):
if \(T\subset K\) is totally real, then \(FT\) is totally real, while
the prime degree \([K:F]=3\) forces \(FT=F\) or \(K\). The latter is
impossible.

At the chosen embedding \(\tau\) is complex conjugation. Hence for any root
of unity \(\zeta\in E\), \(\tau\zeta=\zeta^{-1}\);
\(\zeta+\zeta^{-1}\) is totally real and belongs to \(K\), so lies in \(F\).
For nonreal \(\zeta\), \(F(\zeta)/F\) is quadratic. If it differed from
the quadratic field \(F(\omega)\), their compositum would have degree
4 over \(F\), contradicting its inclusion in the degree-6 field \(E\).
This proves the equality in (10). All of these roots have relative norm
one; those in \(R\) are units of \(R\). In particular \(\mu_6\subset R\).
The finite group of roots of unity is cyclic, and a primitive \(w_E\)-th
root generates a field of degree \(\varphi(w_E)\le2d\).
The elementary estimate
\(\varphi(m)^2/m\ge1/2\) follows prime by prime: the only prime-power
factor that is less than 1 is \(2^1\), with factor \(1/2\).
Thus \(w_E\le2(2d)^2\), as claimed. \(\square\)

The supplied explicit seed is
\[
 u_0=s^2+s\omega,\qquad
 u_0\tau(u_0)=s^4-s^3+s^2=1.
 \tag{11}
\]
The equality follows from
\((s-1)(s^3+s+1)=s^4-s^3+s^2-1\).
Both \(u_0\) and its inverse \(\tau(u_0)\) are in \(R\).
If \(u_0\) were a root of unity, then
\(u_0+u_0^{-1}=2s^2-s\) would be totally real. It is irrational, since a
rational value would make \(s\) satisfy a quadratic polynomial. It therefore
generates the cubic field \(\mathbb Q(s)\), a contradiction.
This is the TFQ §G.4 argument, inspected here.

**Scope.** Extending the same \(u_0\) to every \(F_j\) produces the same
infinite cyclic group. It does not explicitly construct \(d_j\) independent
units. Multiplying these powers by torsion does not change that rank.
Ordinary units of \(F\) also do not solve the problem: their relative
norm from \(E\) to \(K\) is their square.

## 5. MS-F4 — exact logarithmic and height accounting

For each of the \(d\) conjugate pairs of nonreal embeddings of \(K\),
choose one representative and one of its two extensions \(\sigma_i\) to \(E\).
For \(u\in U_E^1\), set
\[
 \ell(u)=(t_1,\ldots,t_d),\qquad t_i=\log|\sigma_i(u)|.
 \tag{12}
\]
Changing one extension replaces one coordinate by its negative.
The other extension is \(\sigma_i\tau\) and has logarithm \(-t_i\);
the complex-conjugate pair repeats these absolute values. At each of
the \(d\) real places of \(K\), norm one forces \(|u|=1\).

**Statement — PROVED using Dirichlet's logarithmic form.**
\(\Lambda_E=\ell(U_E^1)\) and \(\Lambda_R=\ell(U_R^1)\) are full lattices
in \(\mathbb R^d\), with torsion as their logarithmic kernels.
In the ordinary Euclidean coordinates (12), define the relative logarithmic
covolumes
\(\mathcal R_E=\det\Lambda_E\), \(\mathcal R_R=\det\Lambda_R\).
These are definitions fixing normalization; no unmentioned weighted-regulator
convention is being used. Then
\[
 \mathcal R_R=[\Lambda_E:\Lambda_R]\,\mathcal R_E,\qquad
 1\le[\Lambda_E:\Lambda_R]\le3^{3d},
 \tag{13}
\]
and the absolute logarithmic Weil height is exactly
\[
 h(u)=\frac{\|\ell(u)\|_1}{3d}.
 \tag{14}
\]
Also
\[
 \max_{\sigma:E\hookrightarrow\mathbb C}|\sigma u|
       =\exp\|\ell(u)\|_\infty.
 \tag{15}
\]

**Proof.** Dirichlet supplies discreteness. The kernel has rank \(d\)
and lies in the indicated \(d\)-dimensional relative subspace, so its
logarithms form a full lattice there. The order subgroup has finite index.
More exactly, if \(e=[U_E^1:U_R^1]\), then
\[
 [\Lambda_E:\Lambda_R]=e\,w_R/w_E,
\]
which proves (13) and avoids counting the torsion loss twice.
Units have no finite-place contribution to height. Each nonreal \(K\)
place contributes \(2|t_i|\) to the sum of positive logs over the \(6d\)
embeddings of \(E\), while the real \(K\) places contribute zero.
This proves (14); the same list gives (15). \(\square\)

Here is a quantitative count with every needed shape parameter visible.
Choose a lattice basis \(v_1,\ldots,v_d\) of \(\Lambda_R\), and let
\[
 \rho=\tfrac12\sum_i\|v_i\|_\infty,\qquad
 N_R(T)=|\{u\in U_R^1:\|\ell(u)\|_\infty\le T\}|.
\]
The centered basis parallelepiped tiles \(\mathbb R^d\), lies inside
\([-\rho,\rho]^d\), and has volume \(\mathcal R_R\). Comparing tiles
with the inner and outer cubes gives, for \(T\ge0\),
\[
 w_R\,\frac{(2(T-\rho)_+)^d}{\mathcal R_R}
 \ \le N_R(T)\le\
 w_R\,\frac{(2(T+\rho))^d}{\mathcal R_R}.
 \tag{16}
\]
Boundary tiles cause no problem because their boundaries have measure zero.
For each fixed field this gives the usual large-\(T\) asymptotic
\(N_R(T)\sim w_R(2T)^d/\mathcal R_R\). It is **not** a uniform
growing-degree asymptotic with fixed \(T\).

In particular, rank \(d\) alone gives neither a useful upper bound for
\(\rho\), nor a useful upper bound for \(\mathcal R_R\), nor an exponential
lower bound for \(N_R(T)\) at the intended \(T\). This audit obtains no such
bound from bounded root discriminant alone; it does not assert that all
possible theorems furnishing such a bound are impossible.

For comparison, if a useful maximal-order unit set were known in the same
window, the coset-pigeonhole argument gives the rigorous implication
\[
 N_R(2T)\ge
 \frac{|\{u\in U_E^1:\|\ell(u)\|_\infty\le T\}|}{3^{3d}}.
 \tag{17}
\]
Indeed choose a largest coset of \(U_R^1\), divide its members by one fixed
member, and use the triangle inequality for logarithms. This pays both
an index loss and a doubled window. If instead one takes a common power
to force individual units into \(R\), an exponent up to \(3^{3d}\)
can be needed by this bound, multiplying every height by that exponent.
These are different conversions and their losses must not be conflated.

For the fixed seed \(u_0\), let \(t_0>0\) denote the absolute logarithm
at a complex place of its degree-6 field. Every complex \(K\)-place
gives \(|t_i|=t_0\). Hence the seed-and-torsion construction contributes
exactly
\[
 w_R\bigl(2\lfloor T/t_0\rfloor+1\bigr)
 \tag{18}
\]
units in this window. At fixed \(T\), (10) bounds this by a polynomial
in \(d\). This explicit base-change supply alone has no positive
exponential action rate in \(d\).

## 6. MS-F5 — integral whole-scalar action and distortion

**Statement — PROVED.** Write \(u=a+b\omega\in U_R^1\). Then
\[
 a,b\in\mathcal O_K,\qquad a^2-ab+b^2=1,
\]
and multiplication of \(z=x-\omega y\) gives
\[
 M_u\binom{x}{y}
  =\begin{pmatrix}a&b\\-b&a-b\end{pmatrix}\binom{x}{y},
 \qquad Q(M_u(x,y))=Q(x,y).
 \tag{19}
\]
The matrix lies in \(\mathrm{SL}_2(\mathcal O_K)\); in any integral
\(\mathbb Z\)-basis of \(\mathcal O_K\), it is an integral automorphism
of the rank-\(6d\) lattice \(\mathcal O_K^2\).

**Proof.** Expand \(u(x-\omega y)\) and use \(\omega^2=-1-\omega\).
The determinant is \(a^2-ab+b^2=N_{E/K}(u)=1\).
Taking the relative norm proves the polynomial identity. The inverse is
the action of \(\tau u=(a-b)-b\omega\), again with coefficients in
\(\mathcal O_K\). \(\square\)

At any embedding of \(K\), the two diagonal coordinates are
\(x-\omega y\) and \(x-\omega^2y\). They are multiplied by the two
extensions of \(u\), reciprocal to each other. In the max norm of these
coordinates the distortion is at most \(e^T\) for
\(\|\ell(u)\|_\infty\le T\). At real \(K\)-places the positive quadratic
norm is preserved exactly; at nonreal places there can be expansion
and contraction.

For ordinary coordinate boxes, solving for the coefficients gives
\[
 b=\frac{u-u^{-1}}{\omega-\omega^2},\qquad
 a=\frac{\omega u^{-1}-\omega^2u}{\omega-\omega^2},
\]
so every embedded coefficient \(a,b,a-b\) has modulus at most
\(2e^T/\sqrt3\). The coordinate sup-norm operator bound
\(4e^T/\sqrt3\) is therefore valid. At real \(K\)-places one can
replace \(e^T\) by 1 in these coefficient bounds.
The fractions in these identities are estimates, not new denominators
in the integral action (19).

**Consequence.** These are global norm-preserving lattice automorphisms.
They do not establish invariance of a finite Cartesian box or many
returns from that box. Counting every unit as a useful return without
checking both transformed coordinates would be an additional unproved step.

## 7. MS-F6 — finite action window containing every nonzero box return

Let \(T\ge1\), and define the all-conjugate scalar box
\[
 B_K(T)=\{x\in\mathcal O_K:|\sigma(x)|\le T
                     \text{ for every }\sigma:K\hookrightarrow\mathbb C\}.
\]
The chosen real embedding identifies it with a finite real scalar set.
For the unit action (19), suppose
\[
 (x,y)\in B_K(T)^2\setminus\{(0,0)\},\qquad
 M_u(x,y)\in B_K(T)^2.
 \tag{20}
\]
Put
\[
 L(T)=\tfrac12\log(48T^6),\qquad H=dL(T),\qquad
 \mathcal U_R(T)=\{u\in U_R^1:\|\ell(u)\|_1\le H\}.
 \tag{21}
\]

**Statement — PROVED.** Every unit satisfying (20) belongs to the finite
set \(\mathcal U_R(T)\), and every member of that set has
\[
 h(u)\le L(T)/3.
 \tag{22}
\]
This contains all nonzero returns arising from integral order units.
It does not assert that every member returns, or that it contains arbitrary
nonintegral norm-one multipliers.

**Proof.** At a representative complex place of \(K\), write
\(z_+=x-\omega y\), \(z_-=x-\omega^2y\). Both source and target values
of these coordinates have modulus at most \(2T\). If \(t_i\ge0\),
the source \(z_+\) has modulus at most \(2Te^{-t_i}\), while the source
\(z_-\) has modulus at most \(2T\). If \(t_i<0\), interchange the two
coordinates. In either case,
\[
 |\sigma_i Q(x,y)|\le4T^2e^{-|t_i|},\qquad
 |t_i|\le\log(4T^2)-\log|\sigma_i Q(x,y)|.
 \tag{23}
\]
The algebraic integer \(Q(x,y)\) is nonzero, because it is positive at
the chosen real embedding. At each real place of \(K\), it lies in
\((0,3T^2]\). Its nonzero integer absolute norm is at least 1, whence
\[
 \sum_{i=1}^d\log|\sigma_i Q(x,y)|
   \ge-\tfrac12\sum_{\sigma\ {\rm real}}\log Q(\sigma x,\sigma y)
   \ge-\tfrac d2\log(3T^2).
\]
Summing (23) gives
\[
 \|\ell(u)\|_1
 \le d\log(4T^2)+\tfrac d2\log(3T^2)
 =\tfrac d2\log(48T^6).
\]
Equation (14) proves (22). Lattice discreteness proves finiteness. \(\square\)

Here a centered count that does not need a short basis on its lower side
is useful. For any \(H\ge0\), set
\[
 N_R^{(1)}(H)=|\{u\in U_R^1:\|\ell(u)\|_1\le H\}|,\qquad
 S=\tfrac12\sum_{i=1}^d\|v_i\|_1
\]
for a chosen basis of \(\Lambda_R\). Then
\[
 \boxed{\quad
 w_R\,\frac{H^d}{d!\,\mathcal R_R}
 \le N_R^{(1)}(H)
 \le w_R\,\frac{2^d(H+S)^d}{d!\,\mathcal R_R}.
 \quad}
 \tag{24}
\]

**Proof of the centered lower bound.** The \(\ell^1\)-ball of radius \(H/2\)
has volume \(H^d/d!\). Averaging its number of lattice points over all
translates modulo a fundamental domain gives volume divided by covolume.
Some translate therefore has at least that many lattice points. Subtract
one of these points from all the others. The differences are distinct lattice
points in the centered ball of radius \(H\). This proves the lower bound;
the \(H=0\) case is immediate. For the upper bound, centered fundamental
tiles attached to points of the radius-\(H\) ball lie in the radius-\(H+S\)
ball. Their disjoint volumes yield the right side of (24).
Multiply each lattice count by the torsion multiplicity \(w_R\). \(\square\)

At the return cutoff \(H=dL(T)\), a prospective bound
\(\mathcal R_E\le e^{Cd+o(d)}\) would, by (13), imply the **conditional
action-count estimate**
\[
 \frac1d\log|\mathcal U_R(T)|
 \ge 1+\log L(T)-C-3\log3-o(1).
 \tag{25}
\]
The elementary factorial estimate
\(\log d!=d\log d-d+O(\log d)\) suffices here.
Equation (25) is not asserted without its regulator hypothesis.
The upper count also retains the unknown \(S\). Torsion has zero exponential
rate by (10); even the coarser degree-only bound \(w_E\le72d^2\)
would suffice.

Neither a regulator estimate restricted to totally real fields nor an
unquantified unit-rank statement is applied here to the mixed-signature
\(K\) or the totally imaginary \(E\). Finally, even a positive lower
exponent in (25) would count potential actions only: it would not prove
that many of them return on a typical Cartesian source.

## 8. Construction ledger and precise remaining scope

| Gain or cost | Bound and scope | Status |
|---|---|---|
| Fixed field input | Totally real \(F_j\), \(d_j\to\infty\), \(\operatorname{rd}\le D_0\), source parameters fixed first | Supplied C0 §5.1 |
| Extended degree/signature | \(K:(3d;d,d)\), \(E:(6d;0,3d)\) | MS-F1 |
| Discriminant | Root-discriminant factors \(31^{1/3}\) and \(\sqrt3\) | MS-F1 |
| Additive order index | \(J\le3^{3d/2}\), supported at 3 | MS-F2 |
| Conductor and unit passage | \(\delta\mathcal O_E\subset\mathfrak f\); relative-unit index \(\le3^{3d}\) | MS-F2 |
| Relative rank | \(d\), using Dirichlet | MS-F3 |
| Torsion | \(6\le w_R\le8d^2\); no blanket assertion \(w_R=6\) | MS-F3 |
| Explicit seed supply | Rank 1 and count (18); subexponential at fixed \(T\) | MS-F3–F4 |
| Relative logarithmic covolume | \(\mathcal R_R\le3^{3d}\mathcal R_E\); absolute size not bounded here | MS-F4 / quantitative gap |
| Window geometry | \(\rho\) retained in (16); no degree-uniform bound supplied | OPEN |
| Height and distortion | \(h(u)=\|t\|_1/(3d)\); spectral distortion \(e^{\|t\|_\infty}\) | MS-F4–F5 |
| All nonzero order-unit returns | Contained in the finite \(\ell^1\)-window (21); height \(\le L(T)/3\) | MS-F6 |
| Centered window count | (24), with explicit covolume and fundamental \(\ell^1\)-radius \(S\) | MS-F6 |
| Action coefficient denominators | Zero for units selected in \(R\) | MS-F5; subgroup cost paid separately |
| Split primes / local sparsity | C0 splitting in \(F\) is not automatically splitting in \(K,E\); unused here | No imported saving |
| Scalar input count and real projection | No finite scalar carrier is constructed by this companion | Not claimed |
| Input thinning, both coordinates | Depends on a later return domain; unknown, not zero | OPEN |
| Full ordered-pair returns / uncovered outputs | Integral norm identity does not count these | OPEN |
| Image exponent and net saving | No bound \(\lvert Q(A,A)\rvert\le \lvert A\rvert^{2-c}\) follows here | OPEN |

Claim record: MS-F1–F6, version 2026-10-20, this file §§2–7, fixed
polynomial \(Q\), all totally real \(F\) satisfying §2. Dependencies are
listed in §1 and at each theorem. Proofs are supplied here; external novelty
has not been checked. On 2026-10-20 the independent internal auditor
`audit_sign_cube` read and passed the complete written MS-F1–F6 proofs,
including the torsion refinement, conductor bound, logarithmic normalization,
return cutoff, and the two centered counting bounds. This is internal
mathematical review, not external verification; it does not resolve the
missing quantitative unit-window or Cartesian-return estimates. No
computation was executed, so there are no experimental runtime, seed,
output, or equality-test claims.
