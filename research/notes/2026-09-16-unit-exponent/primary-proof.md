# UE-P1–UE-P3 — Independent multipliers, orbit returns and Cartesian coverage

Date/version: **2026-09-16, version 1**. Track: **T03**, the newly
commissioned unit-exponent branch for $Q(x,y)=x^2+xy+y^2$.

## Summary and exact scope

* **PROVED, UE-P1:** an explicit sequence of multiplicatively independent
  norm-one elements in $\mathbb Q(\omega)$ gives $3^d$ distinct actual
  actions in the primary exponent box.
* **PROVED, UE-P2:** a norm orbit box of size $3^d$ has at least $2^d$
  distinct returns at every point. Its typical logarithmic return rate
  is $(2\log2+\log3)/3$, with an explicit exponentially small lower tail.
* **PROVED, UE-P3:** for seed $1$, direct coefficient projection has
  scalar size exactly $2\cdot3^d$. The engineered pairs occupy exactly
  $1/(4\cdot3^d)$ of its Cartesian square. A subexponential number of
  norm shells still covers only an exponentially small fraction.
* **FAILED, scoped certificate:** these orbit-supported returns do not
  give the required almost-everywhere Cartesian return theorem.
  **OPEN:** the full Cartesian return distribution and actual $Q$-image
  rate of the coefficient set. No quadratic-scale image lower bound is
  proved or claimed here.

This is a symbolic proof subtask: no mathematical program, experiment,
network query, literature search or external theorem import was used.
The action and norm identity are inherited; they are not reproved.
The new proof does not re-run any previous carrier family.

## Claim record and provenance

| Field | Record |
|---|---|
| Claim IDs | **UE-P1**, §1; **UE-P2**, §2; **UE-P3**, §3 |
| Status/evidence | **PROVED**, complete internal arguments below, with author audit; independent parent audit is a separate record |
| Polynomial and domain | Fixed $Q=x^2+xy+y^2$ on real scalar pairs; actual multipliers in a fixed complex embedding of $E=\mathbb Q(\omega)$ |
| Quantifiers | Fix integers $L,h\ge1$ and a nonzero seed before $d$ grows; then every integer $d\ge1$; primary choice $L=h=1$, seed $1$ |
| Dependencies | Elementary ring/field arithmetic; norm identity and action from SN-T03-1; the used factorization facts are proved in §1.2 |
| New versus inherited | Independence of this explicit sequence, the exact orbit return law, its tail, and the stated projection/coverage analysis are derived here; the norm identity and return-to-image implication are inherited |
| Audit limits | No finite experiment or actual full Cartesian return count is asserted by this note |
| Remaining gap | Returns for the uncontrolled cross-pairs in $A_d^2$; no full-image power-saving construction follows |
| Novelty | No external novelty or priority claim |

The active user assignment is
`[private commissioning attachment; locator withheld]`.
The inherited action is recorded in
[SN-T03-1](../2026-09-14-study-notes/03-eisenstein.md), with its private
source locator, and the full-image implication in
[HR-1](../2026-09-16-high-return/return-lemma.md).
The previous [two-prime report](../2026-09-16-two-prime-character/README.md),
§6.2, bounds the distinct actions of its finite-exponent group-compatible
realizations; the infinite-order independent multipliers below are a new
candidate and are not covered by that finite-exponent argument.
The historical T03 scope remains
`local-only/migration/sources/T03_CURRENT_STATE.md`, §§4, 7, 13–15;
the present branch does not replace the adaptive RC15/4 obligation.

## 1. UE-P1 — Exponent labels give distinct actual actions

### Mathematical statement

Fix $L\ge1$. Define an infinite sequence of positive integers by

$$
P_0=1,\qquad t_i=3P_{i-1}^{\,2L+1},\qquad
q_i=t_i^2+t_i+1,\qquad P_i=P_{i-1}q_i.
\tag{1}
$$

Fix $\omega=(-1+\sqrt{-3})/2$ in $\mathbb C$ and put

$$
\alpha_i=t_i-\omega,\qquad
u_i=\frac{\alpha_i}{\overline{\alpha_i}}
       \in E^\times,\qquad E=\mathbb Q(\omega).
\tag{2}
$$

Then $N(u_i)=1$, and the sequence $(u_i)_{i\ge1}$ is
multiplicatively independent: every finitely supported integer relation

$$\prod_i u_i^{e_i}=1$$

has $e_i=0$ for every $i$. More strongly, the product can be a root of
unity only when all $e_i=0$, in which case the root of unity is $1$.
Consequently, for every fixed integer $h\ge1$ and every $d\ge1$,

$$
U_d(h)=\left\{\prod_{i=1}^d u_i^{f_i}:
                         f_i\in[-h,h]\cap\mathbb Z\right\}
\quad\hbox{has}\quad |U_d(h)|=(2h+1)^d.
\tag{3}
$$

Its elements induce distinct complex multiplications, hence distinct
real linear actions on the coefficient pair in $z=x-\omega y$.
They also act distinctly on every single nonzero seed.

### What it means

The exponential action count in (3) counts actual elements of a fixed
number field, not formal descriptions or modular labels. These are
norm-one **fractional multipliers**, not necessarily units of the
integer ring $\mathbb Z[\omega]$. Growing the number of allowed prime
divisors supplies the independent directions even though $[E:\mathbb Q]=2$.

### Why it matters

Gate I passes with rate $\log(2h+1)$, and in particular rate $\log3$
when $h=1$. The bounded real-action collapse of the previous finite-group
model does not occur for these multipliers. Gate II still needs coverage
of almost all of a same-set Cartesian square.

### 1.1 Pairwise coprime rational norms

Since $t_i$ is divisible by $3P_{i-1}$, equation (1) gives

$$q_i\equiv1\pmod{3P_{i-1}}.\tag{4}$$

Thus $3\nmid q_i$ and $\gcd(q_i,P_{i-1})=1$. Every earlier $q_j$
divides $P_{i-1}$, so the $q_i$ are pairwise coprime. Also $t_i\ge3$
and $q_i>1$. The proof requires no assertion that any $q_i$ is prime.
Direct multiplication gives $N(\alpha_i)=q_i$.

### 1.2 Elementary factorization facts in $\mathbb Z[\omega]$

Write $\mathcal O=\mathbb Z[\omega]$. For $a,b\in\mathbb Z$,

$$N(a+b\omega)=a^2-ab+b^2.$$

This is a nonnegative integer, positive for nonzero elements, and is
multiplicative. The ring is norm-Euclidean: if $a,b\in\mathcal O$ and
$b\ne0$, write $a/b=s+t\omega$ with $s,t\in\mathbb R$, and choose
integers $m,n$ within $1/2$ of $s,t$. For $c=m+n\omega$,

$$
N(a/b-c)\le\frac34<1,
\qquad N(a-bc)<N(b).
\tag{5}
$$

The Euclidean algorithm therefore gives greatest common divisors and
Bezout identities. Every nonunit factors into irreducibles by induction
on its positive integer norm: a nontrivial factorization has factors
with strictly smaller norms. An irreducible $\pi$ is prime, because if
$\pi\nmid a$, then $\gcd(\pi,a)=1$ and a Bezout identity shows that
$\pi\mid ab$ implies $\pi\mid b$. Cancelling these prime factors gives
unique factorization, up to units and order. This is all the
factorization theory needed below.

For each irreducible $\pi$, its factorization exponent defines an
integer valuation $\nu_\pi$ on $E^\times$ by subtracting denominator
exponents. This is well-defined by unique factorization and satisfies
$\nu_\pi(ab)=\nu_\pi(a)+\nu_\pi(b)$. A root of unity has every such
valuation zero: if $\zeta^m=1$, then $m\nu_\pi(\zeta)=0$.

### 1.3 A private factor for each multiplier

No irreducible divides both $\alpha_i$ and $\overline{\alpha_i}$.
Indeed a common irreducible $\pi$ would divide their difference
$\overline\omega-\omega$, of norm $3$. The integer $N(\pi)>1$
would then divide both $3$ and $N(\alpha_i)=q_i$, contradicting (4).

Choose any irreducible factor $\pi_i$ of $\alpha_i$, which exists
because $q_i>1$. It divides neither $\overline{\alpha_i}$ nor
$\alpha_j$ nor $\overline{\alpha_j}$ for $j\ne i$. For the latter
two assertions, $N(\pi_i)>1$ would otherwise divide both coprime
integers $q_i,q_j$. Hence

$$
\nu_{\pi_i}(u_i)>0,\qquad
\nu_{\pi_i}(u_j)=0\quad(j\ne i).
\tag{6}
$$

Apply $\nu_{\pi_i}$ to a finite relation $\prod_j u_j^{e_j}=\zeta$
with $\zeta$ a root of unity. Equation (6) gives
$e_i\nu_{\pi_i}(u_i)=0$, so $e_i=0$. This holds for every $i$,
proving independence and the stronger torsion statement.

Conjugation sends $u_i$ to $u_i^{-1}$; it introduces no additional
relation among the exponent labels. Clearing algebraic or rational
denominators cannot change the valuation argument. The chosen embedding
of $E$ into $\mathbb C$ is injective. Finally, if $uz=vz$ for a
nonzero complex $z$, cancellation gives $u=v$. Thus there is neither
action duplication nor a nontrivial stabilizer at a nonzero seed.

## 2. UE-P2 — Exact orbit returns, including boundary points

### Mathematical statement

Fix $L,h\ge1$ and $z_0\in E^\times$ before $d$ grows, and use (1)–(2).
Define

$$
Z_d(L)=\left\{z_e=z_0\prod_{i=1}^d u_i^{e_i}:
                         e_i\in[-L,L]\cap\mathbb Z\right\}.
\tag{7}
$$

Then $M_d=|Z_d(L)|=(2L+1)^d$. For any $e$ in this box and any action
label $f\in[-h,h]^d\cap\mathbb Z^d$, independence gives the equivalence

$$
\left(\prod_i u_i^{f_i}\right)z_e\in Z_d(L)
\quad\Longleftrightarrow\quad e+f\in[-L,L]^d.
\tag{8}
$$

Consequently the exact return count is

$$
R_Z(z_e)=\prod_{i=1}^d b_{L,h}(e_i),\qquad
b_{L,h}(j)=1+\min(h,L-j)+\min(h,L+j).
\tag{9}
$$

There are no duplicated action labels or returned states in (9).
For every $j\in[-L,L]$,

$$
1+\min(h,2L)\le b_{L,h}(j)\le 1+2\min(h,L).
\tag{10}
$$

In particular all orbit points have a uniformly positive return exponent
$\log(1+\min(h,2L))$, with an empty exceptional set.

### What it means

An allowed action translates the exponent vector, exactly as intended.
Boundary coordinates reduce the number of returning shifts but never
reduce it to one when $L,h\ge1$. These returns are genuine equal-norm
points in the fixed complex plane, and their coefficient pairs are
distinct real pairs.

### Why it matters

The orbit mechanism itself passes the return-tail gate. This statement
concerns points of $Z_d$, not arbitrary pairs of coefficients chosen
independently from its scalar projection. The distinction becomes
decisive in §3.

### 2.1 Proof of the product and boundary bounds

Equation (8) follows by cancelling $z_0$ and applying UE-P1. At a fixed
coordinate $j$, the returning shifts are the integers in
$[-h,h]\cap[-L-j,L-j]$. Counting the negative, zero and positive
shifts gives exactly $b_{L,h}(j)$ in (9). The different coordinates
can be selected independently, giving the product count.

For nonnegative numbers $a=L-j$ and $b=L+j$ with $a+b=2L$,
$\min(h,a)+\min(h,b)$ is at least $\min(h,2L)$ and at most
$\min(2h,2L)$. This proves (10). The lower bound is attained at
$j=\pm L$, and the upper bound at $j=0$.

For returns whose target is $Z_d$, the three counts are exactly equal:

$$R_{\rm label,Z}=R_{\rm action,Z}=R_{\rm pair,Z}=R_Z.$$

Here the pair count uses the unique expansion $z=x-\omega y$ in the
real basis $1,-\omega$. These equalities concern the eligible returning
actions in (8). They do not identify $R_Z$ with the possibly larger
return count into the completed set $A_d^2$.

### 2.2 Complete primary distribution when $L=h=1$

The three one-coordinate return counts are

$$b_{1,1}(-1)=2,\qquad b_{1,1}(0)=3,\qquad b_{1,1}(1)=2.$$

If $k$ coordinates of $e$ are zero, then

$$
R_Z(z_e)=2^{d-k}3^k,
\qquad
\#\{e:\#\{i:e_i=0\}=k\}=\binom dk2^{d-k}.
\tag{11}
$$

This is the complete exact distribution. In particular

$$
\begin{gathered}
\min R_Z=2^d,\qquad \max R_Z=3^d,\qquad
\frac1{3^d}\sum_e R_Z(z_e)=\left(\frac73\right)^d,\\
\frac1{3^d}\sum_e\log R_Z(z_e)
=\mu d,\qquad \mu=\frac{2\log2+\log3}{3}.
\end{gathered}
\tag{12}
$$

Thus the geometric mean is $\exp(\mu d)$, and the fraction with return
count one is zero for every $d\ge1$. Every stabilizer size is one.
The $2^d$ corners have the minimum count, which is still exponential.

### 2.3 An explicit exponential lower-tail estimate

Fix $0<\eta<1/3$, set $p=1/3-\eta$, and define

$$
\rho_\eta=\log2+p\log(3/2),\qquad
\delta_\eta=p\log(3p)+(1-p)\log\!\left(\frac{3(1-p)}2\right)>0.
\tag{13}
$$

Then for every $d\ge1$,

$$
\#\{z\in Z_d(1):R_Z(z)<\exp(\rho_\eta d)\}
\le \exp((\log3-\delta_\eta)d).
\tag{14}
$$

To prove it, under uniform counting on the exponent box the zero count
$K$ has distribution $\Pr(K=k)=3^{-d}\binom dk2^{d-k}$. For $s>0$,

$$
\Pr(K\le pd)
\le e^{spd}\,\mathbb E(e^{-sK})
=\left[e^{sp}\frac{2+e^{-s}}3\right]^d.
$$

Take $e^{-s}=2p/(1-p)$, which is in $(0,1)$ because $p<1/3$.
The bracket equals $e^{-\delta_\eta}$. Formula (11) turns the event in
(14) into $K<pd$, proving the bound. Positivity of $\delta_\eta$
needs no external large-deviation theorem: the function
$p\log(3p)+(1-p)\log(3(1-p)/2)$ has derivative
$\log(2p/(1-p))$, strictly positive second derivative, and minimum
zero at $p=1/3$.

As $\eta\downarrow0$, $\rho_\eta$ tends to $\mu$ from below.
The exact binomial law has $\operatorname{Var}(K)=2d/9$; applying
Markov's inequality to $(K-d/3)^2$ shows $K/d\to1/3$ in probability.
Thus $d^{-1}\log R_Z\to\mu$, justifying the stated typical rate.
At the smaller threshold $2^d$, the exceptional set is exactly empty,
which is stronger than any nonzero exponential exceptional bound.

## 3. UE-P3 — Direct coefficient projection is exponentially sparse

### Mathematical statement

Write each $z\in Z_d(L)$ uniquely as $z=x_z-\omega y_z$ and let

$$
S_d=\{(x_z,y_z):z\in Z_d(L)\},\qquad
A_d=\{x_z:z\in Z_d(L)\}\cup\{y_z:z\in Z_d(L)\}.
\tag{15}
$$

Put $M=(2L+1)^d$ and $n=|A_d|$. Then

$$
|S_d|=M,\qquad \frac M2\le n\le2M,
\qquad \frac{|S_d|}{n^2}\le\frac4M.
\tag{16}
$$

More generally, for any nonempty finite real set $A$ of size $n$ and
any finite set $\mathcal C$ of $k$ norm values,

$$
\#\{(x,y)\in A^2:Q(x,y)\in\mathcal C\}\le2kn.
\tag{17}
$$

Consequently, when $n=\exp(ad+o(d))$ with $a>0$ and
$k_d=\exp(o(d))$, a union of these $k_d$ shells covers at most a
fraction $\exp(-ad+o(d))$ of $A_d^2$.

For the primary seed $z_0=1$, the sharper exact formulas are

$$
n=2M,\qquad \frac{|S_d|}{n^2}=\frac1{4M}.
\tag{16a}
$$

Each coordinate projection is then injective and their two scalar
images are disjoint. This strengthening uses the absence of nontrivial
torsion in the generated multiplier group; it is not asserted for an
arbitrary nonzero seed.

### What it means

The orbit is large but lies on one fixed ellipse. Projecting its
coordinates already requires a scalar set of comparable size; completing
that set to a Cartesian square creates quadratically many pairs. The
proved returning pairs therefore form an exponentially small part of
the domain that the polynomial problem requires us to cover.

### Why it matters

The favorable orbit return exponent cannot pay for treating almost the
entire Cartesian square as exceptional. Adding only a subexponential
number of seed norm shells leaves the same coverage failure. This
rejects the stated orbit-supported certificate, not every possible
additional return among the completed cross-pairs.

### 3.1 Proof of the projection bounds

All $z\in Z_d(L)$ have the same positive real norm
$C=N(z_0)>0$. The coefficient map is injective, so $|S_d|=M$.
For a fixed real $x$, the equation

$$y^2+xy+x^2=C$$

has at most two real solutions $y$. Therefore the projection
$S_d\to\{x_z\}$ has fibers of size at most two, giving
$|\{x_z\}|\ge M/2$ and hence $n\ge M/2$. Each of the two coordinate
sets has at most $M$ elements, giving $n\le2M$. The density bound in
(16) follows immediately. The same fiber bound holds for the other
coordinate. Projection to the ordered pair has fiber one.

Every returning state from §2 lies in $S_d\subset A_d^2$, so each
engineered pair has at least its $R_Z$ distinct Cartesian returns.
Actual multipliers remain distinct on these nonzero pairs. However,

$$
|A_d^2\setminus S_d|=n^2-M
\ge \frac{M^2}{4}-M,
\qquad
\frac{|A_d^2\setminus S_d|}{n^2}\ge1-\frac4M.
\tag{18}
$$

These are counts of pairs without a certificate from the orbit-box
argument. They are not a claim that those pairs have few actual returns.

### 3.2 Exact coefficient size for seed one

Let $\Gamma=\langle u_1,u_2,\ldots\rangle\subset E^\times$.
By UE-P1 its only root of unity is $1$, and all its elements have norm
one. We prove a slightly more general statement: for every finite
$Z\subset\Gamma$, the two coordinate maps $z\mapsto x_z$ and
$z\mapsto y_z$ are injective and have disjoint images.

Suppose first that distinct $z,w\in\Gamma$ have the same first
coordinate $x$. Their second coordinates are the two roots of
$Y^2+xY+x^2=1$, so $y_w=-x-y_z$. It follows that

$$
w=x-\omega(-x-y_z)=-\omega^2\overline z,
\qquad wz=-\omega^2.
$$

This would put the nontrivial root of unity $-\omega^2$ in $\Gamma$,
a contradiction. Hence the first coordinate map is injective.

If distinct $z,w$ have the same second coordinate $y$, their first
coordinates have sum $-y$, giving

$$w=-\overline z,\qquad wz=-1.$$

This is the same contradiction with the nontrivial root of unity $-1$.
Hence the second coordinate map is injective.

Finally suppose $x_z=y_w$. Write $z=x-\omega y$ and $w=a-\omega x$.
The equations $Q(x,y)=Q(a,x)=1$ give

$$a^2+ax=y^2+xy,\qquad (a-y)(a+y+x)=0.$$

If $a=y$, then $w=y-\omega x=-\omega\overline z$, so
$wz=-\omega$. If $a=-x-y$, then $w=\omega^2z$, so
$w/z=\omega^2$. Both possibilities put a nontrivial root of unity
in $\Gamma$, a contradiction. The coordinate images are disjoint.
Each therefore has $|Z|$ elements, proving (16a) for $Z=Z_d(L)$
and seed $1$.

The identity belongs to the exponent box and has coefficients $(1,0)$,
so the primary scalar set contains zero. The completed pair $(0,0)$
has only one distinct returned pair, regardless of the number of
multiplier labels fixing it. It is outside the positive-norm engineered
shell and is not credited with the orbit return count. This one singular
pair is separate from the much larger uncovered complement.

### 3.3 Shell completion and a subexponential number of states

For fixed $x\in A$ and $c\in\mathcal C$, the same quadratic equation
has at most two real $y$ values. Summing over $n$ choices of $x$ and
$k$ norm values proves (17), including zero and negative norm values
(which respectively have at most one or no real pair for this form).

Even if one credits every pair on the original norm shell, its size is
at most $2n$, and the complement has at least $n^2-2n$ pairs. If a
multistate certificate credits only pairs lying on $k_d=\exp(o(d))$
seed norm shells, its covered fraction is at most $2k_d/n$.
For example, a union of $k_d$ orbit boxes of the same size $M$ has
coefficient set size between $M/2$ and $2k_dM$, so
$\log n=d\log(2L+1)+o(d)$ and its credited fraction still tends to
zero at exponential rate $\log(2L+1)$.

This statement applies to schemes whose proved pairs are restricted to
those shells. It does not exclude a new proof of returns for cross-pairs
on exponentially many other norm values, nor does it classify all
multistate Cartesian carriers.

## 4. Rate accounting and the exact unresolved point

For the primary choice $L=h=1$, the proved rates are

| Quantity | Exact count or rate | Status |
|---|---|---|
| Distinct actions | $3^d$ | **PROVED** |
| Orbit points | $M=3^d$ | **PROVED** |
| Orbit returns, minimum | $2^d$ | **PROVED**, no exceptions inside $Z_d$ |
| Orbit returns, typical log rate | $(2\log2+\log3)/3$ | **PROVED**, tail (14) |
| Scalar inputs, seed $1$ | $n=2M=2\cdot3^d$, hence $a=\log3$ | **PROVED** |
| Duplicate-action/stabilizer losses | None at nonzero orbit points | **PROVED** |
| Projection to ordered scalar pairs | Injective | **PROVED** |
| Coordinate projection, seed $1$ | Each fiber one; the two coordinate images are disjoint | **PROVED** |
| Engineered pair coverage | Exactly $1/(4\cdot3^d)$ | **PROVED** |
| Uncontrolled cross-pairs | $n^2-M=4\cdot9^d-3^d=\exp(2ad+O(1))$ | **PROVED** count; their general return distribution remains **OPEN** |
| Full-image exponent from these certified pairs alone | Quadratic exponent $b=2a$; no positive signed gap | **FAILED** certificate |

The field degree is fixed at two. The construction introduces genuinely
growing prime support rather than hiding a bounded action group.
For completeness, if the seed's two rational coefficients have common
denominator $D_0$, then every coefficient in $A_d$ has denominator
dividing $D_0P_d^L$: for $e\ge0$, $u_i^e=\alpha_i^{2e}/q_i^e$,
and for $e<0$ use the conjugate formula. These denominators are genuine,
and no favorable height or lattice-packing estimate is inferred from
the action count. The coverage failure already occurs for exact real
sets before such an arithmetic construction estimate is attempted.

In particular, setting the uncertified pairs aside leaves an exceptional
set of exponent $2a$, not $2a-\delta$ for any fixed $\delta>0$.
Even the fact that every engineered pair has the same output only gives
the valid elementary certificate

$$|Q(A_d,A_d)|\le n^2-M+1,$$

which has exponent two in $n$. No assertion that this bound is sharp
is made. Applying HR-1 with the uncontrolled pairs counted separately
has the same exponent obstruction.

**Narrow primary verdict: ACTION GO / CARTESIAN FAIL.** This means that
the direct projection and any certificate supported on a subexponential
number of norm shells fail the requested coverage gate. The point left
unresolved is whether an additional mechanism supplies exponentially
many distinct returns for almost all of the completed Cartesian
cross-pairs. This note makes no actual full-image lower-bound claim and
does not launch another family or the affine $Q+x$ problem.
