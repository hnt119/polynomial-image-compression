# Context from the other fixed tracks

November 5, 2026. These verbatim passages identify the accepted frontier relevant to the comparison. They do not update the separate tracks.

## T02 • status extract

## Accepted C2–C4 results

- **PROVED — C2:** the determinant-7 map has image
  $\{(a,b):a+2b\in7\mathcal O\}$ and index $7^d$. Its scalar consequence is
  $h_s(z)=2z^4+sz$ in $R=\mathbb F_7[\pi]/(\pi^3)$, with
  $|h_s(R)|=208=4\cdot49+3\cdot4$ for $s=\pm1$.
  CRT gives at most $208^{d/3}(\rho_4Q)^d$ occupied classes modulo $7Q$;
  population per class is counted separately. The graph index and scalar
  restriction are not independent savings.
- **PROVED — C2:** the positive hybrid $C=GT$ is direct, $|C|=|G||T|$.
  Its exact ratio decomposition has $|\mathcal K_u|=|T|^2$ and
  $\sum_u|G(u)|=|G|^2$. The displayed elementary count supplies only
  $\kappa_{\rm cert}=0$; cross-point and cross-ratio overlaps are not excluded.
  The actual image exponent remains **OPEN**.
- **PROVED — C3:** every nonempty $E\subseteq R$ and either sign satisfy
  $\Phi_s(E)=343|h_s(3E-E)|/|E|^2\ge4/7$.
  Equality holds exactly for full critical fibers $a+\pi R$, $a^3=-s$.
  The multifiber minimum is $208/343$, only at $R$; the second minimum
  excluding critical full fibers is $343/576$, exactly for a critical full
  fiber minus one point. This universal theorem is analytic.
- **PROVED — C4:** in the actual local cubic with $e=3,f=1$ and
  $7\mathcal O=\mathfrak p^3$, set $R_m=\mathcal O/\mathfrak p^{3m}$ and
  $E_m=(\alpha+\mathfrak p)\bmod\mathfrak p^{3m}$, $\alpha^3=-1\bmod\mathfrak p$.
  Then

  $$N_1=4,\qquad N_m=|P_4(E_m,E_m)|=22\,7^{3m-4}\quad(m\ge2).$$

  The support is exactly three full $\mathfrak p^3$-cosets and one full
  $\mathfrak p^4$-coset. Thus $N_2=1078$, $N_3=369754$, and
  $N_{m+1}=343N_m$ for $m\ge2$. Charging both input fractions gives
  $\Psi_1=4/7$, $\Psi_{m\ge2}=22/49$, and per-degree gain
  $\frac13\log(49/22)\approx0.2669259483$. Density improves once and stabilizes.
  This is not an optimum over arbitrary higher-level subsets. For $m\ge2$
  the quotient has characteristic $7^m$; the proof retains mixed-characteristic carries.

## Carrier and signed rate

**PROVED:** the $Q=1$ tower admits the growing same-input carrier

$$C_j=-1+\{u\in\mathfrak I_j:|\sigma_i(u)|\le X\},\qquad N(\mathfrak I_j)=7^{d_j/3}.$$

With the source root discriminant $D$ fixed before the degree limit,

$$a=\log X-\tfrac13\log7-\tfrac12\log D,\quad B=\log(2X+1),\quad
X=2\,7^{1/3}\sqrt D,\quad a=\log2.$$

The ideal-lattice translate-and-difference lower count assumes neither
bounded-box equidistribution nor surjectivity onto full local inputs.
The exact continuous width in the established growth range is
$W=81(X+1)^4+\frac32X+\frac{27}{16}$.
Uniform packing yields $|P_4(C_j,C_j)|\le U_m=N_m^{d_j/3}(1+W/7^m)^{d_j}$.
The fully charged certificate rates are

$$\kappa_1=\log\frac{X^2}{D(4/7)^{1/3}(W+7)}<0,$$
$$\kappa_m=\log\frac{X^2}{D(22/49)^{1/3}(W+7^m)}<0\qquad(m\ge2).$$

Both input ideal restrictions, discriminant, class count, and per-class packing
are paid. Translation is in $W$; this additive carrier has no hidden unit,
regulator, sign, multiplicity, branch, or omitted-output costs. Level two improves
the negative level-one rate in the chosen growth range; higher levels worsen it.
Saturation-ideal and mixed-depth rates are also negative. These are certificate
exponents, not actual-image exponents. The illustrative $D=7^{2/3}$ table does
not assert a tower attaining that discriminant floor.

## FAILED routes — exact scopes

| Route | Scope of failure |
| --- | --- |
| C0/C1 interval packing | Symmetric or exact full-interval fourth-power class certificates; C1 includes translated, unequal, and degree-dependent radii under its $Q\ge5$ hypotheses. Smaller realized support is outside the result. |
| C1 independent thinning | Coordinate-product split-prime input restrictions with both input costs and the same interval certificate; not the general correlated inequality. |
| C2 elementary hybrid counts | Interval enclosure, marginal-support multiplication, and displayed ratio/common-action parameter counts; not all hybrids or possible cross-support overlaps. |
| C2 determinant-7 density alone | The $208/343$ factor with stated full continuous intervals and uniform modulus packing: $U_{7Q}/|C|^2\ge[e^{-s_7}\rho_4Q]^d>1$, $s_7=\frac13\log(343/208)$. |
| C3 one-level optimization | No subset of the same 343-element ring improves the normalized two-input factor below $4/7$, for either sign; arbitrary higher-level subsets are outside the theorem. |
| C3 global certificates | Modulus-7 input engineering with full intervals and uniform class packing. For arbitrary local sets, the $Q=1$ comparison uses the volume-density budget; its stronger actual-population result concerns optimal critical cosets in equal-radius windows. The retained $Q>1$ branch also fails its stated certificate. |
| C4 deeper precision | The same full critical inverse images with full-interval rational-modulus packing for every fixed $m$; no additional density gain occurs after $m=2$. |
| C4 ideal-coset covers | Saturation, mixed-depth, and arbitrary finite 7-supported integral-ideal coset covers of the entire local product, assigning full continuous intervals to every branch and using uniform ideal-norm packing. Actual-population comparisons require the stated nontrivial equal-radius critical-coset carriers. |
| Weak deficits / collisions | These diagnostics alone do not give a sufficiently small all-output support upper bound. Weak M1-DEFICIT itself is PROVED. |

For C4's arbitrary complete-local-support covers,
$U_{\rm cover}/|C|^2\ge[81\,22^{1/3}/64]^d>3.54^d$.
Saturation and mixed envelopes exceed $4.24^d$ and $3.85^d$, respectively.
These are lower bounds on numerical envelopes divided by the pair budget,
not lower bounds on the actual image or sufficient improvement thresholds.
Proper subsets of globally realized branches, smaller branch-dependent real
regions, cross-factor correlations, and other carriers remain outside the
retirement. See [FAILURE_LIBRARY](../../FAILURE_LIBRARY.md).

## T04 • status extract

## PROVED input theorem; OPEN full output

Let $\epsilon=2+\sqrt3$, $a_0=\sqrt3/2$, and

$$A_0=\{0\},\qquad A_{m+1}=(\epsilon A_m+a_0)
\cup(\epsilon^{-1}A_m-a_0).$$

Every branch history is legal. Scalars lie in the fixed fractional module
$\tfrac12\mathbb Z[\sqrt3]$; field degree and denominator stay fixed.
Different histories collide already at length three, so $2^m$ is a path
count, not the distinct-input count.

For $\Lambda>1$ satisfying $\Lambda^{-1}+\Lambda^{-3}+\Lambda^{-5}=1$,
and $\varphi=(1+\sqrt5)/2$, the independently audited source proves

$$\frac{\Lambda^{m-2}}{m+1}\le|A_m|\le2\varphi^4\varphi^m,\qquad
|A_m|=e^{a_*m+o(m)},$$

$$0.45116944438\ldots=\log\Lambda\le a_*\le
\log\varphi=0.48121182506\ldots.$$

The proof counts injective fixed-block-count classes and distinct affine maps;
it does not assume that all paths have distinct scalar values.

**OPEN:** the only certified full-image upper bound is

$$|P_-(A_m,A_m)|\le|A_m|^2=e^{2a_*m+o(m)}.$$

The certified gap is zero; the actual gap is unknown. This is not a proof
that the true output exponent equals $2a_*$, or a proof of cubic compression.
Sources: current state §4.9; candidate-input and input-audit notes.

## PROVED exact pair evolution; missing output count

In $u=X-Y$, $s=X+Y$, the four branch pairs are, for $\sigma=\pm1$:

$$\begin{array}{lll}
\text{same signs:}&u'=(2+\sigma\sqrt3)u,&s'=(2+\sigma\sqrt3)s+\sigma\sqrt3,\\
\text{opposite signs:}&u'=2u+\sigma\sqrt3(s+1),&s'=\sigma\sqrt3u+2s.
\end{array}$$

The output is $u'^3-3s'$. The ten monomials of degree at most three form
an invariant linear observable space, but their scalar values are unbounded.
Ten coordinates do not certify ten finite output states.
Source: `sacc_pair_states.md`; current state §4.9.

**OPEN — selected T04-O1:** determine whether
$\limsup_m m^{-1}\log|P_-(A_m,A_m)|<2a_*$.
A sufficient construction would encode every ordered pair with at most
$K_0(m+1)^B\kappa^m$ labels, fixed $K_0,B<\infty$, $\kappa<\Lambda^2$,
where equal labels imply equal scalar outputs after all carries/relations.
**CONDITIONAL:** every $c_-<2-\log\kappa/\log\Lambda$ would work.
No such encoding is supplied. Source: current state §§13–14.
