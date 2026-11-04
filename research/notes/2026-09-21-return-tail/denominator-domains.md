# Denominator-adapted rational carriers: identity-only disappears, the tail does not

21 September 2026 · T03 / return-tail cycle · fixed $Q(x,y)=x^2+xy+y^2$.
**PROVED** below by new local arguments, using only the already proved
Eisenstein representation and divisor bounds HR-4A/B. Internal review is
recorded separately in verification.md. No outside result, program run,
prime search, or novelty claim.

## 1. Construction, exact actions and prior inputs

For $H\ge1$ put

$$A_H=X_H=Y_H=\{a/b\in\mathbb Q: |a|\le H,\ 1\le b\le H,
\ \gcd(a,b)=1\},\qquad n_H=|A_H|.$$

Every scalar has its unique reduced description with positive denominator;
in particular zero has only $(a,b)=(0,1)$. Thus $n_H\le2H^2+1\le3H^2$.
The carrier is closed under negation. A concrete growing action family is

$$U_H=\{\pm\bar\beta/\beta:\ \beta=m+k\omega\ne0,
\quad m,k\in\mathbb Z,\ |m|,|k|\le H\},\tag{1}$$

with duplicates removed, where $\omega=(-1+i\sqrt3)/2$. It contains
$\pm1$. The $H+1$ ratios from $\beta_k=1+k\omega$, $0\le k\le H$,
are distinct: equality for $k,\ell$ gives
$(\ell-k)(\omega-\bar\omega)=0$, hence $k=\ell$. The complete
inventory has at most $2((2H+1)^2-1)$ elements. Each action is a genuine rational norm-one multiplier and
preserves the full scalar norm by

$$N((\bar\beta/\beta)z)=N(z),\qquad z=x-\omega y.$$

For $u=A+B\omega$ the exact domain is

$$D_u=\{(x,y)\in A_H^2:Ax+By\in A_H,
\ -Bx+(A-B)y\in A_H\}.\tag{2}$$

These are simultaneous reduced-numerator/denominator conditions on the
whole pair, not independent local rotations. Multiplication of any two
such global actions is again norm preserving; membership in the finite
selected set and return to the carrier must each be checked separately.
No formal action-word growth is credited.

The obstruction below is stronger than needed for (1): it bounds the
**entire polynomial fiber** on a positive-density source set, hence holds
for every possible finite family of norm-one actions, even if it depends
on $H$. This stronger statement is established by proof, not inferred
from low selected-action counts.

The only prior arithmetic inputs are the complete local proofs
[HR-4A and HR-4B](../2026-09-16-high-return/denominator-obstruction.md):

$$\#\{(s,t)\in\mathbb Z^2:Q(s,t)=N\}\le6\tau(N),\qquad N\ge1,\tag{3}$$
$$\tau(N)\le D_\theta N^\theta\quad(N\ge1,\ \theta>0),\tag{4}$$

where $D_\theta$ depends only on $\theta$. They are cited, not reproved
or rerun. Here the new issue is that the rational scalar denominators
vary independently, so there is no one small common denominator for the
whole carrier. The simultaneous denominator constraints below control
that cost per norm fiber.

## 2. RT-D1 — exact denominator domains of a typical rational fiber

### Statement

Suppose $x=a/b$, $y=c/d$ are reduced, $1\le a,c\le H$,
$H/2<b,d\le H$, and $\gcd(b,d)=1$. Set

$$K=bd,\qquad N=a^2d^2+abcd+c^2b^2.$$

Then $Q(x,y)=N/K^2$ is in lowest terms, with $1\le N\le3H^4$.
Every target $(x',y')\in A_H^2$ having this norm has reduced
denominators $e,g$ satisfying

$$\operatorname{lcm}(e,g)=tK\qquad\text{for some }t\in\{1,2,3\}.\tag{5}$$

Consequently the full fiber $\mathcal F_H(x,y)$ obeys

$$\boxed{|\mathcal F_H(x,y)|
\le6\sum_{t=1}^3\tau(tK)^2\tau(t^2N).}\tag{6}$$

For every fixed $\nu>0$ this is at most $C_\nu H^\nu$, uniformly
in all such source pairs and $H$, with a constant depending only on $\nu$.

### Meaning

A pair of large coprime input denominators forces almost their entire
product into the denominator of every equal-norm target. The target
cannot distribute that product among unrestricted denominator states:
only three common multiples fit inside the scalar denominator bound.

### Consequence

Even allowing every possible norm-preserving action, these sources have
only subpolynomially many genuine returns as a function of the carrier
size. A positive-density supply of these pairs will defeat the tail.

### Proof

If a rational prime $p$ divides $b$, then it divides neither $a$ nor
$d$, so $N\equiv a^2d^2\ne0\pmod p$. Similarly no prime divisor
of $d$ divides $N$. Thus $\gcd(N,K)=1$, including higher prime powers,
and $N/K^2$ is fully reduced.

For $x'=a'/e$, $y'=c'/g$ reduced, write $\Lambda=\operatorname{lcm}(e,g)$.
Both $s=a'\Lambda/e$ and $t'=c'\Lambda/g$ are integers, so
$Q(x',y')=Q(s,t')/\Lambda^2$. Equality to the reduced $N/K^2$ forces
$K^2\mid\Lambda^2$, equivalently $K\mid\Lambda$. Since
$K>H^2/4$ and $\Lambda\le eg\le H^2$, the ratio is one of $1,2,3$.
This proves (5).

For a fixed choice $\Lambda=tK$, there are at most $\tau(tK)^2$
ordered choices of divisors $e,g$. This overcounts those with a smaller
least common multiple and is therefore a valid upper bound. Once $e,g$
are fixed, the map from target numerators to the integer pair $(s,t')$
is injective, and its norm must equal $t^2N$. Bound (3) proves (6).

By (4), $tK\le3H^2$ and $t^2N\le27H^4$ give

$$|\mathcal F_H(x,y)|
\le18D_\theta^3\,3^{5\theta}H^{8\theta}.
\tag{7}$$

Choose $\theta=\nu/8$. No constants depend on the source pair or $H$.
The source is positive and nonzero, so the integer norm in (3) is
positive. $\square$

## 3. RT-D2 — a positive-density supply of the denominator pattern

### Statement

Let $H=12L$ with integer $L\ge10{,}000$. There is an explicitly defined
set $\mathcal B_H\subset A_H^2$ consisting of pairs in RT-D1 such that

$$\boxed{|\mathcal B_H|\ge\frac{n_H^2}{400{,}000},
\qquad \frac{H^2}{288}\le n_H\le3H^2.}\tag{8}$$

All constants are fixed, and all pairs are ordered.

### Meaning

The denominator obstruction is not confined to a thin prime-denominator
subset. Elementary counting supplies a fixed fraction of the entire
rational carrier square, with no prime-density theorem.

### Consequence

The actual low-return population is quadratic in size, even though the
carrier has almost no identity-only pairs.

### Proof

Set

$$C_H=\{m\in\mathbb Z:H/2<m\le H,\ m\equiv1\pmod6\}.$$

It has exactly $L$ elements, none divisible by two or three. Define
$\mathcal B_H$ through the quadruples $(a,b,c,d)\in C_H^4$ satisfying

$$\gcd(a,b)=\gcd(c,d)=\gcd(b,d)=1.\tag{9}$$

Reduced positive fractions have unique numerator/denominator labels, so
these quadruples map injectively to ordered scalar pairs. They satisfy
all the hypotheses of RT-D1.

A failure of one gcd condition involves a prime $p\ge5$. The number
of elements of $C_H$ divisible by $p$ is at most $L/p+1$, since the
arithmetic progression has step six, invertible modulo $p$. The number
of bad ordered pairs for one gcd is at most

$$\sum_{5\le p\le H\atop p\text{ prime}}(L/p+1)^2
\le\frac7{50}L^2+2L(1+\log H)+H.\tag{10}$$

Indeed all these primes are odd, and

$$\sum_{p\ge5}p^{-2}\le\sum_{j\ge0}(5+2j)^{-2}
\le\frac1{25}+\int_0^\infty(5+2t)^{-2}\,dt=\frac7{50};$$

the other two sums are bounded by the harmonic sum and the number of
integers at most $H$. Multiplying (10) by $L^2$ for the other two
coordinates and summing over the three gcd conditions gives a bad
quadruple fraction at most

$$\frac{21}{50}+
\frac{6(1+\log(12L))+36}{L}<\frac12
\qquad(L\ge10{,}000).\tag{11}$$

For the strict inequality, the second term decreases for $L\ge10{,}000$,
and at that endpoint $\log120{,}000<12$, so it is at most
$114/10{,}000<2/25$. Thus at least $L^4/2$ quadruples are good.
Using $n_H^2\le9H^4$,

$$|\mathcal B_H|\ge\frac{H^4}{2\cdot12^4}
\ge\frac{n_H^2}{18\cdot12^4}
=\frac{n_H^2}{373{,}248}>
\frac{n_H^2}{400{,}000}.$$

The same pair estimate (10) is below $L^2/2$ in this range. Hence
$C_H^2$ contains at least $L^2/2$ coprime numerator/denominator pairs,
giving $n_H\ge L^2/2=H^2/288$. The upper bound was established in §1.
$\square$

## 4. RT-D3 — full tail failure with only one identity-only pair

### Statement

For the family (1), the identity-only set is exactly

$$I_H=\{(0,0)\}.\tag{12}$$

Nevertheless, for every fixed $\varepsilon>0$ and all sufficiently large
$H=12L$,

$$\boxed{B_\varepsilon(H)\ge n_H^2/400{,}000.}\tag{13}$$

Statement (13) holds for **any** finite family of genuine norm-one
multipliers, not only (1). The identity-only statement (12) uses that
(1) contains both signs.

### Meaning

Removing identity-only pairs solves only the threshold-one problem.
These rational denominator states have at least two returns everywhere
except zero, yet a fixed fraction never reaches any fixed positive
polynomial threshold.

### Consequence

**FAILED** rational-height return-tail witness. Here the full-fiber
argument also gives, for every $\rho>0$ and sufficiently large $H=12L$,
a genuine image lower bound $|Q(A_H,A_H)|\ge n_H^{2-\rho}$.
This separately proved scope concerns this rational-height family only,
not arbitrary real carriers, DC-O1, or the T03 target.

### Proof

For nonzero $p$, identity and simultaneous negation yield two distinct
points of $A_H^2$. Every action fixes zero, which has just one target.
This proves (12).

In RT-D1 take $\nu=\varepsilon$. By (8),

$$R(p)\le |\mathcal F_H(p)|\le C_\varepsilon H^\varepsilon
\le C_\varepsilon(288n_H)^{\varepsilon/2}<n_H^\varepsilon$$

for every $p\in\mathcal B_H$, eventually uniformly in that set.
Equation (8) proves (13). No fixed $\delta>0$ can absorb this population
into $O(n_H^{2-\delta})$.

For the stated image consequence, take any $\rho>0$ and use the same
argument with return/fiber exponent $\rho/2$. Every fiber containing a
point of $\mathcal B_H$ has at most $n_H^{\rho/2}$ total points for
large $H$. Their output values therefore number at least
$n_H^{2-\rho/2}/400{,}000$, which eventually exceeds
$n_H^{2-\rho}$. This is an actual fiber upper bound followed by counting;
it is not a collision-energy or failed-certificate inference. $\square$

## 5. Construction ledger and exact scope

| Quantity or cost | Bound / accounting |
|---|---|
| Inputs | Reduced fractions have unique labels; $H^2/288\le n_H\le3H^2$ for the stated sequence |
| Input rates | In parameter $s=\log H$, $\log n_H=2s+O(1)$ |
| Same-set compatibility | $X=Y=A_H$, so zero symmetric difference; choose $\eta=1$ |
| Both-coordinate thinning | The whole rational carrier is retained. Its proved bad subpopulation comes from (9), with its constant density charged explicitly |
| Actual multipliers | Explicit deduplicated (1), at most $2((2H+1)^2-1)$; already at least $H+1$ from $\beta=1+k\omega$, $0\le k\le H$, whose ratios are distinct |
| Composition and cross terms | Whole multiplication by $\bar\beta/\beta$, with exactly unit norm; no independent internal rotations or tensor return multiplication |
| Stabilizers | Every nonzero source has trivial multiplier stabilizer; zero has one distinct target |
| Denominator states | For bad sources the target least common multiple is one of $K,2K,3K$; at most $\tau(tK)^2$ denominator pairs per state |
| Scalar/action heights | Numerators and denominators bounded by $H$; action coefficient denominators divide $N\beta\le3H^2$ |
| Field/discriminant | Rational inputs, fixed multiplier field $\mathbb Q(\omega)$ of degree two and discriminant $-3$ |
| Regulator/class number | No estimates used; (3)–(4) are the existing explicit elementary arithmetic inputs |
| Primes / local packing | Only the fixed progression modulo six and elementary reciprocal sums occur; no growing-prime selection or splitting estimate |
| Archimedean cost | Source norm numerator $N\le3H^4$; integer target norms at most $27H^4$; all counts charged through (7) |
| Identity-only tail | Exactly one pair for the concrete action family |
| Polynomial low-return tail | At least $n_H^2/400{,}000$ for every fixed positive threshold exponent, eventually |
| Signed rate | Positive input rate and exact overlap, but no positive exception deficit; DC-R1 yields no fixed saving |
| Actual image | The separate family-specific lower bound in RT-D3 is proved from actual fiber bounds, not from return failure alone |

No finite scout was needed or run for this mechanism. It is rejected by
the proved all-action obstruction before any parameter expansion. The
scope is the stated bounded-numerator/denominator rational carrier and
its large-coprime-denominator subpopulation; sparse rational carriers
with heights growing faster than every fixed power of size are not
covered. There is no claim that every denominator-adapted construction
or real carrier fails.
