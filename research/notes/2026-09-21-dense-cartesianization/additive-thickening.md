# DC-A1 — One-axis thickening and its Cartesian cost

Date/version: **21 September 2026, version 1**. Track **T03**, newly
authorized dense-Cartesianization branch; fixed $Q(x,y)=x^2+xy+y^2$.
**PROVED**, by the complete internal argument below. This is a coverage
obstruction for a specified certificate, not an actual-image lower bound.

## Identity, sources and exact definition

Use the established seed-$1$ orbit $Z_{0,d}=U_d(1)$ of
[UE-P1–UE-P3](../2026-09-16-unit-exponent/primary-proof.md), §§1–3.
Explicitly, $P_0=1$, $t_i=3P_{i-1}^3$, $q_i=t_i^2+t_i+1$,
$P_i=P_{i-1}q_i$, $u_i=(t_i-\omega)/(t_i-\bar\omega)$, and

$$U_d=\left\{\prod_{i=1}^d u_i^{e_i}:e_i\in\{-1,0,1\}\right\}.$$

The inherited theorem gives $M=|U_d|=3^d$ distinct actual multipliers.
Write $z=x_z-\omega y_z$. The coordinate sets $X=\{x_z\}$ and
$Y=\{y_z\}$ each have $M$ elements: both maps are injective for this
seed. These are precisely the hypotheses used below; the theorem is not
asserted for arbitrary seeds with noninjective coordinate maps.

For any nonempty finite $T\subset\mathbb R$, $K=|T|$, define

$$Z_T=\{z+t:z\in Z_{0,d},\ t\in T\},\qquad
E_T=\{(x_z+t,y_z):z\in Z_{0,d},\ t\in T\},$$
$$A_T=(X+T)\cup Y,\qquad n=|A_T|.$$

The letter $E_T$ here denotes **engineered pairs**, not bad pairs. Every
element is genuinely in $A_T^2$. The pair map and $x-\omega y$ map
are injective on $(z,t)$, since $y_z$ identifies $z$ and then $t$.
Thus $|Z_T|=|E_T|=MK$. No return claim has yet been made.

## Mathematical statement

For every such orbit and every nonempty $T$,

$$\boxed{|E_T|=MK\le\frac{(n+1)^2}{4},\qquad
|A_T^2\setminus E_T|\ge n^2-\frac{(n+1)^2}{4}.}\tag{1}$$

If the growing thickening is specifically
$T_d=\{0,1,\ldots,M-1\}$, then

$$\boxed{\frac{M^2}{3}\le n_d\le M^2+M,\quad
|E_{T_d}|=M^2,\quad
\frac{|E_{T_d}|}{n_d^2}\le\frac9{M^2}.}\tag{2}$$

In particular $\log n_d=2d\log3+O(1)$ and the engineered fraction
tends to zero exponentially. Even optimistically crediting high returns
to every engineered pair leaves a bad-pair certificate of exponent
$2\log n_d$, with no fixed deficit.

## Proof

For finite nonempty real sets, the increasing chain of sums proves
$|X+T|\ge|X|+|T|-1=M+K-1$. Hence $M+K\le n+1$ and
$4MK\le(M+K)^2\le(n+1)^2$, proving (1), including its explicit
ordered-pair complement count.

For (2), the upper bound follows from $|X+T_d|\le M^2$ and $|Y|=M$.
Every $z\in Z_{0,d}$ has norm one. Completing the square gives

$$1=Q(x_z,y_z)=(y_z+x_z/2)^2+3x_z^2/4,$$

so $X\subset[-2/\sqrt3,2/\sqrt3]$, an interval of length
$4/\sqrt3<3$. For a fixed sum $s=x+t$ with integer $t$, the possible
$x\in X$ differ by integers. At most three numbers with mutual
integer differences fit in this interval. Thus the addition map from
$X\times T_d$ has fibers at most three, and
$|X+T_d|\ge M^2/3$. The remaining conclusions follow immediately.
All constants are uniform in $d$. $\square$

## What it means

Adding arbitrarily many real shifts creates more structured points, but
one coefficient still identifies the original orbit point. The sumset
bound forces the scalar carrier to grow too fast for these selected
points to cover nearly all its square. For the explicit integer interval
thickening, the input size itself grows from order $M$ to order $M^2$.

## Why it matters — the return warning

The unchanged orbit return law does not extend automatically to $Z_T$:

$$u(z+t)=uz+ut.$$

For $t\ne0$ and a nonreal $u$, the last summand is not real and is
not a permitted one-axis translation. Therefore (1) is already an
optimistic certificate bound: it would still fail if all $MK$ selected
pairs were given many legal returns for free. It proves neither that
all these points actually have many returns nor that unselected pairs
have few. The finite scout measures those separate questions exactly.

**FAILED in the stated scope:** using only these one-axis shifted
orbit points as the high-return coverage certificate. **OPEN outside
this scope:** other seed families, two-axis or correlated shifts,
and additional incidental returns on the full square. No actual-image
lower bound follows from (1) or (2).

## Construction ledger

This ledger follows `research/templates/CONSTRUCTION_LEDGER.md`.

| Gain/cost | Explicit accounting |
|---|---|
| Fixed choices and growth | Fixed recurrence above and $T_d=[0,3^d-1]\cap\mathbb Z$; then integer $d\to\infty$. General (1) permits any $T$. |
| Scalar input bounds | $3^{2d}/3\le n_d\le3^{2d}+3^d$, so lower and upper rate $a=2\log3$. |
| Input thinning, both coordinates | None. The entire $A_T^2$ is the domain. |
| Parameter/projection fibers | Engineered pair parameterization injective; $X\times T_d\to X+T_d$ has fibers at most three. Inclusion of $Y$ is a set union with exact deduplication. |
| Engineered gain | $|E_T|=MK$ exactly; explicit interval case $|E_T|=e^{ad}$. These are not all verified rich-return pairs. |
| Return gain | Inherited $2^d$ orbit returns apply only before adding shifts. After thickening, a uniform positive return rate is unproved. No gain is credited. |
| Exceptional-pair cost | Even granting every engineered pair a certificate, $B_{\rm cert}=n_d^2-M^2=e^{2ad+O(1)}$. General bound (1) leaves asymptotic fraction at least $3/4$. |
| Stabilizers/action labels | $|U_d|=3^d$ actual actions. Distinct targets at nonzero pairs; origin has one target, regardless of labels. |
| Field/discriminant/regulator/ideals | Fixed $\mathbb Q(\omega)$, degree two, discriminant $-3$; no regulator, class-number, ideal-volume or splitting count is used. No field-growth gain is claimed. |
| Denominators and heights | For the explicit $T=T_d$: orbit coefficients have denominator dividing $P_d$; integer shifts introduce none. Norm-one coefficients have absolute value at most $2/\sqrt3$. Scalars in $A_{T_d}$ have magnitude at most $M+2$. Here $\log P_d=\Theta(7^d)$; this is recorded, not hidden as a subexponential-height condition. Arbitrary real $T$ in (1) has no asserted rational denominator or height bound. |
| Local moduli, populations, archimedean loss | No residue-density gain, approximate equality or lattice count. Membership is exact. The interval bound is used solely for the three-to-one addition estimate. |
| Branches/states/carries | Every $z,t$ included; no uncounted branch. No digit carry gain. |
| Full-image exponent and signed gap | HR-1 with the optimistic pair-exception charge retains exponent $2a$ from the uncovered pairs. Certified gap zero. Actual full-image rate remains OPEN. |
| Strict fixed saving | None follows from this certificate. A separate compression of exceptional outputs would be additional work, not supplied here. |

## Evidence and audit

The symbolic argument needs no program. An independent internal reviewer
checked (1), the seed-$1$ injectivity hypothesis, and the distinction
between engineered and returning pairs; the final bounded-interval
refinement (2) is separately included in the cycle audit. Exact scouts
at $d=1,2$ are recorded in the main report and reproducibility file;
they are not proof premises. Historical sources are unchanged. No
external theorem, literature search, novelty assertion or external peer
review is claimed.
