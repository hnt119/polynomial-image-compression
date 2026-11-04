# Bottom line

**Unit-Exponent Cartesian Carrier Cycle — T03, 16 September 2026.**

- **Verdict: ACTION GO / CARTESIAN FAIL**, in the two precise scopes below. We obtain $3^d$ distinct actual norm-one actions; the earlier bounded-action collapse is absent.
- **PROVED:** an exponent orbit of $3^d$ points has at least $2^d$ genuine returns at every point. Its typical log-return rate is $\mu=(2\log2+\log3)/3>0$, with an exponential lower tail.
- **PROVED:** direct coefficient projection gives exactly $n_d=2\cdot3^d$ scalar inputs but only $3^d$ engineered pairs. Their density is $1/(4\cdot3^d)$, so the orbit certificate leaves almost the whole Cartesian square uncontrolled.
- **PROVED:** the one permitted mutation, a sparse box of rational valuation exponents, has only the identity return on **every** Cartesian pair, even under all integer powers of all its generators.
- **PROVED independently of that return obstruction:** the mutation has exactly $|Q(A_d,A_d)|=n_d^2/4+n_d/2$. Its input rate is $a=\log3$, output rate $b=2\log3$, and signed gap $2a-b=0$.
- No power saving for real $Q$ is obtained. The primary coefficient set's actual asymptotic image rate remains **OPEN**; the secondary family's image is proved quadratic. The general target and RC15/4 remain **OPEN**. HR-N1 stays closed.
- **One next obligation:** retain the existing T03-O4/RC15/4 whole-signed-root bound, stated in §10. No further carrier mutation or affine cycle is started here.

$$
\text{units}
\underset{\text{PROVED}}{\longrightarrow}
\text{distinct real actions}
\underset{\text{FAILED in the tested scopes}}{\longrightarrow}
\text{typical Cartesian returns}
\underset{\text{PROVED}}{\longrightarrow}
Q\text{-collisions}
\underset{\text{OPEN target}}{\longrightarrow}
\text{power saving}.
$$

The third arrow is the norm identity. The last arrow requires the full-support
hypotheses of the existing HR-1 theorem; collisions alone do not imply an
image upper bound. The first carrier fails its engineered-coverage certificate;
the second fails the Cartesian-return requirement itself. Those statements
have different scopes.

## 1. Exact construction and return counts

### Mathematical statement

Fix $L=1$ for the main construction and all finite diagnostics. The proofs
also work for any fixed integer $L\ge1$, chosen before the depth $d$ grows.
Recursively define

$$P_0=1,\quad t_i=3P_{i-1}^{2L+1},\quad
q_i=t_i^2+t_i+1,\quad P_i=P_{i-1}q_i.$$

Let $\omega=(-1+i\sqrt3)/2$, $K=\mathbb Q(\omega)$, and

$$\alpha_i=t_i-\omega,\qquad
u_i=\frac{\alpha_i}{\bar\alpha_i},\qquad
\Gamma_d=\langle u_1,\ldots,u_d\rangle,$$
$$U_d(h)=\left\{\prod_{i=1}^d u_i^{f_i}:|f_i|\le h\right\},
\qquad h=1.$$

These are fractional norm-one elements, or units after their denominators
are inverted. They are **not** integral units of $\mathbb Z[\omega]$.
The latter group is finite. Also, the $q_i$ need not be prime: their
pairwise coprime prime-support blocks supply the independent directions.

For $u=\alpha+\beta\omega$, the actual real action is

$$T_u(x,y)=(\alpha x+\beta y,-\beta x+(\alpha-\beta)y),
\qquad Q(T_u(x,y))=Q(x,y).$$

For a specified finite action box and a real scalar carrier $A$, call an
exponent label eligible at $(x,y)$ precisely when $T_u(x,y)\in A^2$.
Define

$$R_{\rm label}=\#\{\text{eligible exponent labels}\},$$
$$R_{\rm action}=\#\{\text{distinct multipliers from eligible labels}\},
\qquad
R_{\rm pair}=\#\{T_u(x,y):u\text{ is eligible}\}.$$

Then $R_{\rm pair}\le R_{\rm action}\le R_{\rm label}$.
Below action labels are injective, so the last two counts agree. For a
nonzero pair, cancellation in $\mathbb C$ makes all three agree. At
$(0,0)$, however, every action returns and only one pair is returned.

### What it means

Each transformation acts on rational scalar pairs in the usual real
embedding. There is no finite-field model or projection from a product
algebra. The number of independent support blocks grows with $d$ while
the field stays quadratic.

### Why it matters

This directly addresses the previous $18$-action obstruction: these groups
have infinite order and do not factor through a fixed-exponent finite
group. Actual action growth must still be followed by Cartesian legality.

## 2. Gate I: exponentially many distinct real actions

### Mathematical statement — PROVED, UE-P1

For every finitely supported integer vector $f$,

$$\prod_i u_i^{f_i}=1\quad\Longrightarrow\quad f_i=0\text{ for all }i.$$

In fact the generated group contains no root of unity other than $1$.
Hence $|U_d(h)|=(2h+1)^d$, and the chosen box has action rate $\log3$.

Here is the decisive arithmetic. Since $t_i$ is divisible by
$3P_{i-1}$,

$$q_i\equiv1\pmod{3P_{i-1}}.$$

The norm blocks are pairwise coprime and avoid $3$. The two elements
$\alpha_i,\bar\alpha_i$ are coprime in $\mathbb Z[\omega]$:
a common prime factor would divide $\omega-\bar\omega$, whose norm
is $3$, and also have norm dividing $q_i$.
An irreducible factor $\pi_i$ of $\alpha_i$ therefore satisfies

$$v_{\pi_i}(u_i)>0,\qquad v_{\pi_i}(u_j)=0\quad(j\ne i).$$

Applying these valuations proves independence, including against roots of
unity. Negative exponents, conjugation, denominator clearing and the fixed
injective field embedding do not change this conclusion. The full
[primary proof, §1](primary-proof.md) includes the elementary norm-Euclidean
factorization argument; no external arithmetic theorem is missing.

### What it means

Every exponent label describes a different multiplication in the complex
plane, hence a different norm-preserving real linear map. Distinct actions
also yield distinct images of any fixed nonzero point.

### Why it matters

The action gate passes without a stabilizer or duplicate-label loss.
Any failure below comes from carrier coverage or integrality, rather than
from collapsing exponentially many formal labels to finitely many actions.

## 3. Primary orbit: exact returns and boundary control

### Mathematical statement — PROVED, UE-P2

Set

$$Z_d(L)=\left\{z_e=\prod_{i=1}^d u_i^{e_i}:|e_i|\le L\right\}.$$

All points have norm $1$ and are distinct. For $|f_i|\le h$, independence
gives the exact equivalence

$$u^fz_e\in Z_d(L)\quad\Longleftrightarrow\quad
e+f\in[-L,L]^d.$$

Consequently

$$R_Z(z_e)=\prod_{i=1}^d
\bigl(1+\min(h,L-e_i)+\min(h,L+e_i)\bigr).$$

For $L=h=1$, if $k$ coordinates of $e$ vanish, then

$$R_Z(z_e)=2^{d-k}3^k,
\qquad\#\{e:\text{$k$ zero coordinates}\}=\binom dk2^{d-k}.$$

Thus every point, including every corner, has at least $2^d$ returns.
The exception set at this threshold is empty. The mean and geometric mean
are respectively $(7/3)^d$ and $e^{\mu d}$, where

$$\mu=\frac{2\log2+\log3}{3}.$$

The product parameterization proves the independence used to discuss
typical points. In particular, the zero-coordinate count has the binomial
law with parameter $1/3$ and variance $2d/9$, so
$d^{-1}\log R_Z\to\mu$ in probability.

For an explicit stronger-than-minimum threshold, fix $0<p<1/3$ and put

$$r_p=\log2+p\log(3/2),\qquad
\delta_p=p\log(3p)+(1-p)\log\frac{3(1-p)}2>0.$$

Then, at every depth,

$$\#\{z\in Z_d:R_Z(z)<e^{r_pd}\}
\le e^{(\log3-\delta_p)d}.$$

For example $p=1/6$ gives fixed positive constants. The proof multiplies
the exact one-coordinate exponential moments and applies the elementary
inequality for an indicator of a tail event; it is given in
[primary proof, §2](primary-proof.md). No asymptotic inference from finite
experiments is used.

### What it means

Exponent translation works as intended, even at the boundary. Every
return counted here is an actual distinct equal-norm point, and its unique
coefficient pair lies in the scalar completion defined next.

### Why it matters

The norm-orbit return problem is solved for this carrier. Its population
is a set of paired coefficients; it is still much smaller than the square
obtained by choosing those coefficients independently.

## 4. Gate II: coefficient projection and multistate coverage

### Mathematical statement — PROVED, UE-P3; FAILED coverage certificate

Write $z=x_z-\omega y_z$ and define the primary scalar set

$$A_d^{\rm orb}=\{x_z:z\in Z_d\}\cup\{y_z:z\in Z_d\},
\qquad S_d=\{(x_z,y_z):z\in Z_d\}.$$

For seed $1$, the coordinate maps are individually injective and their
images are disjoint. Therefore, with $M=3^d$,

$$|A_d^{\rm orb}|=2M=n_d,\qquad |S_d|=M,$$
$$\frac{|S_d|}{n_d^2}=\frac1{4M},\qquad
|A_d^{{\rm orb}\,2}\setminus S_d|=4M^2-M.$$

For clarity, the exact injection argument is stronger than the usual
two-points-per-vertical-line bound. Equal first coordinates of distinct
$z,w$ on the norm-one ellipse force $wz=-\omega^2$; equal second
coordinates force $wz=-1$. Equality $x_z=y_w$ forces either
$wz=-\omega$ or $w/z=\omega^2$. Each is impossible in the torsion-free
group generated by the $u_i$. The detailed identities are in
[primary proof, §3.2](primary-proof.md).

The multistate option tested here is a union, or a partition and reunion,
of $k_d=e^{o(d)}$ seed norm orbits. For every finite real set $A$ and
every set of $k$ norm values $\mathcal C$,

$$\#\{(x,y)\in A^2:Q(x,y)\in\mathcal C\}\le2k|A|.$$

Indeed fixing $x$ and a norm value leaves a quadratic equation with at
most two real roots for $y$. If $|A|=e^{ad+o(d)}$, the fraction of pairs
on these shells is at most $e^{-ad+o(d)}$ when $k=e^{o(d)}$.
Thus subexponentially many seed-shell states do not repair the coverage.
Here $k$ counts **norm values**, not arbitrary scalar states: the theorem
does not exclude every possible multistate carrier.

### What it means

The construction has no coordinate-projection duplication. Its loss is
Cartesian completion: $M$ paired points generate $4M^2$ possible ordered
pairs. Almost all of those pairs have no return certificate from the
exponent-orbit argument.

### Why it matters

The uncontrolled complement has exponent $2a$, with $a=\log3$, rather
than the required $2a-\delta$. Fast-rejection rule 4 applies. This is a
**certificate obstruction**: it does not prove that all the uncontrolled
pairs have small actual fibers. The primary family's actual asymptotic
image rate and incidental cross-pair returns remain OPEN.

The underlying one-shell observation is already present in the
[historical constructive report, §E](../../history-sources/Q_Constructive_Local_Compression_to_Real_Set_Report.md).
This cycle applies it to a new independent-action construction and proves
the exact coefficient count; it does not claim the shell obstruction is
new. No additive thickening is introduced, because no new mechanism was
supplied that would justify reopening the previous thickening failures.

## 5. The one secondary mutation: a sparse valuation box

### Mathematical statement — PROVED, UE-S1

Use the same explicit $q_i,u_i$ and define

$$A_d^{\rm val}=\left\{\sigma\prod_{i=1}^d q_i^{e_i}:
\sigma\in\{\pm1\},\quad |e_i|\le L\right\}.$$

This is a bounded box in $d$ independent valuation-support directions.
Prime factors within one possibly composite $q_i$ share the same exponent;
we do not claim all individual prime exponents vary independently.
The scalar parameters are injective, so $n_d=2(2L+1)^d$ exactly.

**Every** pair in this full same-set square has only the identity return:

$$u_1^{h_1}\cdots u_d^{h_d}(x-\omega y)=x'-\omega y',
\quad (x,y),(x',y')\in(A_d^{\rm val})^2
\quad\Longrightarrow\quad h_1=\cdots=h_d=0.$$

This holds for all $h\in\mathbb Z^d$, not merely the tested action
window. Hence $R_{\rm label}=R_{\rm action}=R_{\rm pair}=1$ everywhere.

### What it means

The available transformations are exponentially numerous, but none of the
nonidentity ones returns a Cartesian pair. At a split prime, a norm-one
multiplier adds a valuation on one conjugate factor and subtracts it on
the other. The rational carrier cannot absorb that displacement while
retaining its required common denominator depths.

### Why it matters

For any fixed positive return threshold exponent, all $n_d^2$ pairs are
bad once the threshold exceeds one. There is no small exceptional set to
discard. Enlarging the action window, including arbitrarily negative
exponents, cannot repair this particular carrier.

### Proof mechanism: minimum exponents, then a prime valuation

Write $x=\sigma\prod q_i^{e_i}$ and $y=\tau\prod q_i^{f_i}$,
put $m_i=\min(e_i,f_i)$, and divide both coordinates by
$S=\prod q_i^{m_i}$. The residual $X=x/S,Y=y/S$ are nonzero
integers, with exponents between $0$ and $2L$.

For $T>0$, define

$$w_i(T)=\min_{p\mid q_i}\left\lfloor
\frac{v_p(T)}{v_p(q_i)}\right\rfloor.$$

The crucial identity is

$$w_i(Q(x,y))=2m_i.$$

To verify it, $q_i$ must not divide $Q(X,Y)$. When $e_i\ne f_i$,
one residual coordinate is divisible by every prime in the block and the
other is a unit, so the norm is a unit there. When $e_i=f_i$, later
$q_j$ reduce to $1$ modulo $q_i$ and earlier coordinates give

$$Q(X,Y)\equiv Q(X_0,Y_0)\pmod{q_i},
\qquad0<Q(X_0,Y_0)\le3P_{i-1}^{4L}<q_i.$$

Thus at least one $p\mid q_i$, with $k=v_p(q_i)$, satisfies
$v_p(Q(X,Y))<k$. This argument does not assume $q_i$ is prime or
that every prime factor avoids the residual norm.

Norm preservation fixes the same minima $m_i$ at the returned pair, so
the same $S$ makes its two coordinates integral. If $p=\pi\bar\pi$
is oriented toward $\alpha_i$, then

$$v_\pi(u_i)=k,\qquad v_{\bar\pi}(u_i)=-k,$$
$$A=v_\pi(X-\omega Y)\ge0,\quad
B=v_{\bar\pi}(X-\omega Y)\ge0,\quad A+B<k.$$

The returned valuations are $A+kh_i,B-kh_i$. Any nonzero integer
$h_i$ makes one negative, contradicting the target's integrality.
All other generators have zero valuations at these prime factors.
Applying this at every block proves the theorem. Splitting, valuations,
negative exponents and denominators are justified fully in
[secondary proof, §§1–4](secondary-proof.md).

### Why this is outside the closed one-prime carrier theorem

HR-4 concerns $\{bp^{-k}:1\le|b|\le H,\ p\nmid b,\ 0\le k\le K\}$
with a dense numerator alphabet and one denominator prime. The present
carrier has a growing number of disjoint support blocks and only sparse
multiplicative monomials. Placing it inside a large dense container would
charge that container's height, not this carrier's input count.
The new argument above supplies its own full-square obstruction.
The exact earlier hypotheses are recorded in
[HR-4](../2026-09-16-high-return/denominator-obstruction.md).
The fixed-generator HR-6 orbit theorem is likewise not the source of
our growing-rank independence or secondary return conclusion.

## 6. The actual quadratic image of the mutation

### Mathematical statement — PROVED, UE-S2

For $M=(2L+1)^d$ and $n_d=2M$,

$$\boxed{|Q(A_d^{\rm val},A_d^{\rm val})|=M^2+M
=\frac{n_d^2}{4}+\frac{n_d}{2}.}$$

Exactly $M(M-1)$ outputs have four ordered representations, and $2M$
outputs have two. The only identifications are coordinate swapping and
simultaneous sign reversal.

### What it means

This is an actual all-output calculation, not an inference from few
returns. Norm collisions outside $\Gamma_d$ still occur, but their
multiplicity is bounded by four.

### Why it matters

The secondary construction itself has quadratic image growth. For every
fixed $c_0>0$, its image exceeds $n_d^{2-c_0}$ once $n_d^{c_0}>4$.
This excludes this explicit family without making any claim about the
primary coefficient family, RC15/4 or arbitrary finite real sets.

### Proof mechanism: exact specialization of short polynomials

Our sequence satisfies $q_i>6P_{i-1}^{4L}$. Consequently an integer
polynomial of coordinate degree at most $4L$ and coefficient sum of
absolute values at most six cannot vanish at $(q_1,\ldots,q_d)$ unless
it is the zero polynomial. To prove this, expand in the last variable:
each evaluated coefficient has absolute value less than $q_d$. Reducing
modulo $q_d$ forces the constant coefficient to vanish, and repeated
division forces every coefficient to vanish. Induct on $d$.

Clear denominators by $P_d^{2L}$ in an equality of two $Q$-values.
Its difference is just such a six-term polynomial. Thus the equality
is formal, and its terms have exponent support

$$\{2E,E+F,2F\},\qquad
T^{2E}+\sigma\tau T^{E+F}+T^{2F}.$$

For $E\ne F$, the support recovers its unique midpoint and unordered
endpoints; the midpoint coefficient recovers the relative sign.
For $E=F$, the output is $3T^{2E}$ or $T^{2E}$.
These cases give $2\binom M2+2M=M^2+M$ outputs and all stated fibers.
The complete proof is [secondary proof, §§5–6](secondary-proof.md).

## 7. HR-1 application and signed rate ledger

We use the established [HR-1 return-to-image theorem](../2026-09-16-high-return/return-lemma.md).
No new support implication is required.

For the primary set, every point of $S_d$ has at least $2^d$ distinct
returns, but declaring the complement exceptional costs $n_d^2-3^d$
pairs. HR-1 therefore gives no exponent below $2a$ by that certificate.
Since the engineered shell has one value, a direct valid bound is

$$|Q(A_d^{\rm orb},A_d^{\rm orb})|\le n_d^2-3^d+1.$$

This is not claimed sharp; unknown cross-pair output coincidences are
not counted as a saving. For the secondary set, $R_{\rm pair}=1$
makes the return certificate trivial; its independently proved exact
image formula gives $b=2a$ nevertheless.

| Gain or cost | Primary orbit projection | Secondary valuation box |
|---|---|---|
| Parameter order | $L=h=1$ fixed; $d$ grows | Same sequence and fixed width |
| Exact real scalar size | $2\cdot3^d$ | $2\cdot3^d$ |
| Input rates $a,B$ | Both $\log3$ | Both $\log3$ |
| Distinct total actions | $3^d$, rate $\log3$ | $3^d$; full $\Gamma_d$ also audited |
| Proved returning rate | At least $\log2$, typical $\mu$, on the engineered orbit only | Zero on every pair |
| Stabilizers / action duplicates | Trivial off zero; $(0,0)$ has one returned pair | Trivial everywhere; no duplicates |
| Scalar and pair projection fibers | Tagged coefficient map and engineered pair map injective | Sign/exponent scalar map and Cartesian pair map injective |
| Same-set completion | $4\cdot9^d-3^d$ pairs outside the engineered set | Full square covered by obstruction |
| Exceptions | Zero for the orbit theorem; exponent $2a$ for its uncontrolled Cartesian complement | All $n_d^2$ pairs fail any growing threshold |
| States and branches | Subexponentially many seed norms still cover at most $2k_dn_d$ pairs | One scalar set; both signs already counted |
| Input thinning twice | No further thinning; the exact completed square is charged | None; all ordered pairs included |
| Full-output certificate | Quadratic exponent; actual asymptotic image OPEN | Exactly $n_d^2/4+n_d/2$ |
| Signed gap $2a-b$ | Zero for the available certificate | Zero for the actual image rate |
| Fixed positive $c_0$ | None established | None exists for this family |

### Arithmetic audit

| Arithmetic item | Exact accounting |
|---|---|
| Field and embedding | Scalar inputs rational; action field fixed $K=\mathbb Q(\omega)$, degree two, discriminant $-3$, root discriminant $\sqrt3$; the chosen embedding is injective |
| Class number / regulator | Norm-Euclidean factorization is supplied; no class-number estimate, regulator estimate, tower, or density-of-primes theorem enters the construction |
| Integral versus fractional units | The selected $u_i$ are units after inverting $P_d$; the growing support supplies rank. No infinite integral norm-one group is asserted |
| Denominators | Coefficients of $u^e$ have common denominator dividing $P_d^L$; secondary scalars likewise clear by $P_d^L$. Returning secondary pairs use the same exact minimum-exponent factor $S$ |
| Height | $9P_{i-1}^{4L+3}\le P_i\le13P_{i-1}^{4L+3}$, so $\log P_d=\Theta_L((4L+3)^d)$; for $L=1$ this is $\Theta(7^d)$. Heights are not polynomial in input count |
| Archimedean bounds | Primary coordinates have absolute value at most $2/\sqrt3$. Secondary inputs have maximum $P_d^L$ and outputs at most $3P_d^{2L}$. All actions preserve the $Q$ metric exactly |
| Ideal indices and moduli | Exact prime valuations are used, including multiplicities in composite $q_i$. No unproved lattice population or density gain is assumed |
| Carries / coefficient equality | Secondary specialization lemma handles every possible six-term equality. The primary analysis makes no unsupported carry-free assertion |
| Exceptional primes | $3$ is excluded by $q_i\equiv1\pmod3$; distinct blocks have disjoint support. Every other prime used in the argument is justified in the factorization proof |

Huge denominators are explicitly present, but they are not invoked as a
generic reason the target fails. The decisive proved costs are the primary
Cartesian completion and the secondary integrality obstruction; the
secondary actual-image theorem then settles its rate directly.

## 8. Finite exact diagnostics — EXPERIMENTAL corroboration only

Exactly two constructions were evaluated at $d=1,2,3$, with $L=h=1$.
All equalities use rational arithmetic. A separate real/$\sqrt{-3}$
representation checks every labelled action, returned set, norm and finite
stabilizer. No higher-dimensional search or action-window expansion was run.

| Carrier | $d$ | $|A|$ | $|Z|$ | Distinct actions | Full $|Q(A,A)|$ | Fraction $R_{\rm pair}=1$ |
|---|---:|---:|---:|---:|---:|---|
| Orbit projection | 1 | 6 | 3 | 3 | 16 | $5/6$ |
| Orbit projection | 2 | 18 | 9 | 9 | 139 | $17/18$ |
| Orbit projection | 3 | 54 | 27 | 27 | 1264 | $53/54$ |
| Valuation box | 1 | 6 | 36 | 3 | 12 | $1$ |
| Valuation box | 2 | 18 | 324 | 9 | 90 | $1$ |
| Valuation box | 3 | 54 | 2916 | 27 | 756 | $1$ |

For the secondary rows, $Z=A-\omega A$ denotes the full coefficient
domain. Its inclusion of every pair asserts coverage, **not** rich returns.
For the primary rows, $Z$ is the smaller engineered norm orbit.

### Complete Cartesian return distributions

Entries are `return count : number of ordered pairs`. Returning labels
and returning actual actions agree in every row.

| Carrier/depth | $R_{\rm action}=R_{\rm label}$ distribution | $R_{\rm pair}$ distribution |
|---|---|---|
| Primary 1 | $1:29,\ 2:4,\ 3:3$ | $1:30,\ 2:4,\ 3:2$ |
| Primary 2 | $1:305,\ 4:8,\ 6:8,\ 9:3$ | $1:306,\ 4:8,\ 6:8,\ 9:2$ |
| Primary 3 | $1:2861,\ 8:16,\ 12:24,\ 18:12,\ 27:3$ | $1:2862,\ 8:16,\ 12:24,\ 18:12,\ 27:2$ |
| Secondary 1 | $1:36$ | $1:36$ |
| Secondary 2 | $1:324$ | $1:324$ |
| Secondary 3 | $1:2916$ | $1:2916$ |

The sole difference between the primary action and pair histograms is
$(0,0)$: every tested action fixes it, producing one distinct pair.
The finite stabilizer histogram is $1:n^2-1,\ 3^d:1$ for the primary
and $1:n^2$ for the secondary. All scalar-parameter, tagged-coordinate
and engineered-pair projection fibers are one for these definitions.

| Primary depth | Mean $R_{\rm action}$ | Geometric mean | Mean $R_{\rm pair}$ | Geometric mean |
|---:|---|---:|---|---:|
| 1 | $23/18$ | 1.183608 | $11/9$ | 1.148033 |
| 2 | $103/81$ | 1.103862 | $101/81$ | 1.096402 |
| 3 | $1787/1458$ | 1.048276 | $887/729$ | 1.047092 |

For every primary full-square row the minimum and median are one and the
maximum is $3^d$; the identity-only action fractions are respectively
$29/36,305/324,2861/2916$. For every secondary row all five statistics
(minimum, median, geometric mean, arithmetic mean, maximum) equal one.

The primary fractions below $2^d$ are the identity-only fractions above,
using the corresponding action or pair histogram. Fractions below $3^d$
are $1-3/n^2$ for actions and $1-2/n^2$ for pairs. Every secondary
fraction below either threshold is one. Exact geometric-mean expressions,
all output-fiber histograms, all $R_Z$ histograms and per-pair certificate
hashes are retained in the [data](../../../examples/2026-09-16-unit-exponent.json)
and its local raw companion.

These finite primary counts are consistent with a poor typical Cartesian
return rate, but no extrapolation from them is used in UE-P3. The secondary
all-depth conclusions rest on UE-S1/UE-S2, not on their finite agreement.

## 9. Evidence, audits and reproducibility

### Proof and source ledger

| ID | Status | Exact source and review |
|---|---|---|
| UE-P1 | PROVED | [Primary proof §1](primary-proof.md): independent actual actions; lead inspection and separate internal review passed |
| UE-P2 | PROVED | Primary proof §2: orbit products, boundary law and tail; same internal reviews |
| UE-P3 | PROVED scoped certificate failure | Primary proof §3: exact coefficient size and shell coverage; cross-pair image remains OPEN |
| UE-S1 | PROVED | [Secondary proof §§1–4](secondary-proof.md): every pair identity-only under all integer powers; lead and independent internal review passed |
| UE-S2 | PROVED | Secondary proof §§5–6: exact full image; separately checked specialization and degeneracies |
| UE-X1 | EXPERIMENTAL | One frozen exact run, six finite cases, all-pair independent oracle |

All proof records are dated 16 September 2026, version 1. The
[manifest](manifest.json) identifies exact versions, dependencies, code and
data by hash. The source/scope audit distinguished HR-4's dense one-prime
theorem, HR-6's fixed cyclic thickening, the inherited ellipse observation,
and the previous bounded-exponent group obstruction. None is silently
expanded into a universal impossibility theorem. No external input was
needed or imported, and no novelty or external peer-review claim is made.

The cycle was strictly offline. The announced shared ceiling was
2,000,000 charged evaluations and 600 research CPU seconds. The
[reproducible program](../../../experiments/unit_exponent.py) uses Python
3.12.7 and the standard library. From the repository root, the actual run was:

```bash
python3 -m experiments.unit_exponent \
  --output examples/2026-09-16-unit-exponent.json \
  --pairs-output local-only/runs/T03/2026-09-16-unit-exponent/pairs.json
```

Use new output names to reproduce: overwriting is refused. Every ordered
pair was enumerated; there was no sampling or random seed. Only logarithms
and displayed geometric-mean decimals are rounded.

The exact diagnostic used **340,986 charges and 5.944325 CPU seconds**.
The mandatory test suite passed **52 tests**, and the fixed verification
suite passed **159 checks**. A shared-budget wrapper conservatively charged
every project function call during these regressions. Total cycle usage was
**431,118 charges and 8.910798 research/validation CPU seconds**.
The new diagnostic ran once; no failed run or rerun occurred.

The [verification record](verification.md) gives command results, budget
categories, internal reviews, preservation checks and exact file changes.
Historical proof files are preserved. Only dated current-state addenda
are made after mathematical completion. All work remains uncommitted.

## 10. One next mathematical obligation

Retain the already selected **T03-O4 / RC15/4**, without starting it here.
For the actual adaptive levels $\mathcal A_m$, write
$F_m=\mathbb Q(\mathcal A_m)$, $n_m=2^{m+1}$,
$s_m=|Q(\mathcal A_m,\mathcal A_m)|$, and
$M_m=\max|\mathcal A_m|$. The existing OPEN obligation is to find fixed
$H,m_0$ and, for every $m\ge m_0$, explicit choices

$$C_m^\dagger\in F_m,\quad C_m^\dagger>M_m,\quad
B_m\subseteq\mathcal A_m,\quad n_m-|B_m|\le H\sqrt{n_m},$$
$$C_m^\dagger+a=\gamma_m u_a^2,\quad
\gamma_m,u_a\in F_m\text{ positive},\quad
U_m=\{\pm u_a:a\in B_m\},$$

such that the entire signed-root image satisfies

$$\boxed{|\gamma_mQ(U_m,U_m)|\le\frac{15}{4}s_m+Hn_m^{3/2}.}$$

This cycle supplies no new premise for that bound and does not change its
status. The unit-exponent attempt has identified its two precise failures;
no replacement conjecture, third carrier family, difference-set analysis
or affine $Q+x$ research is adopted.
