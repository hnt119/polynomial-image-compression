# Full residue alphabets: a fixed-prime modular tail and its real-lift gate

**Date/version:** 21 September 2026, version 1. **Track:** T03, return-tail
cycle. **Fixed polynomial:** $Q(x,y)=x^2+xy+y^2$.

This is one mechanism: the full scalar alphabet modulo powers of the
single fixed prime **7**, its split norm torus, and the canonical centered
integer lift. It uses no prime search, no mutation of the old three-letter
CRT carrier, and no independent additive tensor composition. All results
below are symbolic: **zero mathematical program runs or evaluations**,
strictly offline, no new outside theorem and no novelty claim. Only this
new note is authored.

The active assignment is the local attachment
`[private task attachment]`.

| Claim | Exact status and scope | Proof / evidence |
|---|---|---|
| MG-1 | **PROVED:** full $\mathbb F_7$ alphabet has six distinct returns at every nonzero pair, one at zero | §1; explicit split coordinates |
| MG-2 | **PROVED:** exact prime-power composition, stabilizers, return histogram and polynomial lower tail in $\mathbb Z/7^k\mathbb Z$ | §2; elementary root lifting and valuation counts |
| MG-3 | **FAILED real carrier:** the canonical integer lift has uniformly subpolynomial actual norm-fiber sizes, hence a quadratic bad set at every fixed positive return threshold | §3; application of retained HR-4A/B, not a new interval experiment |
| MG-4 | **PROVED scoped obstruction:** a group-homomorphic lift of the growing modular torus cannot retain its action population in rational norm-one multipliers; finite-group lifts to arbitrary complex multipliers still have at most six nonzero returning actions on this integer carrier | §4; finite-order argument using accepted Eisenstein factorization |

The new modular proofs are internally authored. Independent audit is
pending unless recorded separately by the lead. MG-3 cites an already
proved theorem; it does not claim a new proof or rerun of that theorem.

## 1. MG-1 — the exact local table

### Statement

Let the scalar alphabet be the entire field $D=\mathbb F_7$. Set
$\lambda=2$, $\mu=4$; these are the distinct roots of $T^2+T+1$.
For a pair $(x,y)$ use the invertible split coordinates

$$s=x-\lambda y,\qquad t=x-\mu y,\qquad st=Q(x,y).\tag{1}$$

The norm-one torus is $G=\mathbb F_7^\times$, with six actions

$$T_h:(s,t)\longmapsto(hs,h^{-1}t),\qquad h\in G.\tag{2}$$

Every domain is the whole finite plane $D^2$. The complete distribution
of **distinct returned pairs**, with some states separated for clarity,
is

| Source state | Number of pairs | Stabilizer size | Distinct targets |
|---|---:|---:|---:|
| $(0,0)$ | 1 | 6 | 1 |
| Nonzero $Q=0$ | 12 | 1 | 6 |
| $x=y\ne0$ | 6 | 1 | 6 |
| Remaining $Q\ne0$ states | 30 | 1 | 6 |

Thus the only identity-only state is the origin. The median is 6 and
the geometric mean is $6^{48/49}$. The modular image is all of
$\mathbb F_7$, of size 7.

**Proof.** The determinant $\lambda-\mu$ is nonzero, so the coordinate
change is invertible. The root identities $\lambda+\mu=-1$,
$\lambda\mu=1$ give (1). Equation (2) preserves the product exactly
in the field. If $(s,t)\ne(0,0)$, at least one coordinate is nonzero;
fixing that coordinate forces $h=1$. This proves freeness and six
distinct targets for all 48 nonzero states. Nonzero product-zero
states consist of the two axes with the origin removed, hence 12.
There are six nonzero diagonal pairs, with norm $3x^2\ne0$, leaving
30 other states. Finally $s=1$, $t=q$ realizes every norm $q$.
$\square$

### Meaning

The old cube-root diagonal locking is absent locally. Full field
membership allows all six targets at a diagonal source; equality of
norms no longer forces both output coordinates back to that same
diagonal residue. For example, $T_\omega(1,1)=(1,-2)$ has the same
norm modulo 7 and is an allowed off-diagonal target.

### Consequence

This is a valid local gadget with no identity-only nonzero state.
These are actual actions and targets **in the finite field**. Their
existence does not yet assert a real scalar return or a real image bound.

## 2. MG-2 — correlated composition through powers of 7

### Statement

Fix $k\ge1$, put $R_k=\mathbb Z/7^k\mathbb Z$, and write
$n=|R_k|=7^k$. Choose the compatible root $\lambda_k$ of $T^2+T+1$
reducing to 2 modulo 7, and put $\mu_k=-1-\lambda_k$.
Then $\mu_k$ reduces to 4 and $\lambda_k-\mu_k$ is a unit.

The algebra

$$R_k[\omega]/(\omega^2+\omega+1)
\longrightarrow R_k\times R_k,\qquad
a+b\omega\longmapsto(a+b\lambda_k,a+b\mu_k)\tag{3}$$

is an isomorphism. It sends conjugation to coordinate exchange and
norm to coordinate product. The norm-one torus is therefore

$$G_k=\{(h,h^{-1}):h\in R_k^\times\},
\qquad |G_k|=6\cdot7^{k-1}.\tag{4}$$

Its action is still (2), with all variables now in $R_k$. Composition
is exactly $T_hT_g=T_{hg}$, and reduction from level $k+1$ to $k$
commutes with the action. This is one global residue-ring action,
not a product of independently rotated scalar summands.

Define $v_7(0)=k$ on $R_k$, and let $v_7(a)\in\{0,\ldots,k-1\}$
be the exact divisibility depth for $a\ne0$. For a nonzero source,
put $m=\min(v_7(s),v_7(t))<k$. Then

$$\boxed{|\operatorname{Stab}_{G_k}(s,t)|=7^m,\qquad
R_k^{\rm pair}(s,t)=6\cdot7^{k-1-m}.}\tag{5}$$

At zero the stabilizer is all of $G_k$ and the distinct-target count
is 1. Equivalently, the complete histogram is

| Distinct return count | Number of pairs | Range |
|---|---:|---|
| 1 | 1 | origin |
| $6\cdot7^{j-1}$ | $48\cdot7^{2j-2}$ | $j=1,\ldots,k$ |

In particular the only identity-only pair remains zero; the smallest
nonzero count is 6 and the median and maximum are $6\cdot7^{k-1}$.
An exact geometric mean is

$$\mathcal G_k=
6^{1-7^{-2k}}
7^{\,k-49/48+49/(48\cdot7^{2k})}=\Theta(n).\tag{6}$$

For every fixed $0<\varepsilon<1$ the modular bad count satisfies

$$\boxed{B_\varepsilon^{\rm mod}(k)
=\#\{p\in R_k^2:R_k^{\rm pair}(p)<n^\varepsilon\}
\le\frac{49}{36}n^{2\varepsilon}.}\tag{7}$$

Thus, in this finite-ring domain, the return exponent is
$\varepsilon$ and the bad exponent can be $\delta=2-2\varepsilon>0$.
The coordinate alphabets agree exactly. For example
$\varepsilon=1/2$, $\delta=1$ gives a fully proved modular tail.

**Proof of the roots and composition.** Suppose $f(\lambda_k)\equiv0$
modulo $7^k$, where $f(T)=T^2+T+1$. For
$\lambda_{k+1}=\lambda_k+c7^k$, expansion gives

$$f(\lambda_{k+1})\equiv
f(\lambda_k)+c7^k f'(\lambda_k)\pmod{7^{k+1}}.$$

Here $f'(\lambda_k)\equiv5\pmod7$ is invertible, so exactly one
$c\in\{0,\ldots,6\}$ makes the next congruence hold. This proves
existence, uniqueness and compatibility without invoking an outside
lifting theorem. The other root and its separation follow from
$\mu_k=-1-\lambda_k$.

The inverse of the split coordinate change for a pair is

$$y=\frac{t-s}{\lambda_k-\mu_k},\qquad
x=\frac{\lambda_k t-\mu_k s}{\lambda_k-\mu_k}.\tag{8}$$

The analogous inverse for $a+b\omega$ proves (3), directly. The two
coordinates of any norm-one element are units whose product is 1,
giving (4). There are $7^k-7^{k-1}$ units in $R_k$. Multiplication of
$(h,h^{-1})$ and $(g,g^{-1})$ gives $(hg,(hg)^{-1})$, proving the
composition and reduction assertions. In ordinary coefficient
coordinates the corresponding action is

$$M_{a+b\omega}(x,y)=(ax+by,-bx+(a-b)y),$$
$$b=\frac{h-h^{-1}}{\lambda_k-\mu_k},\qquad
a=\frac{\lambda_k h^{-1}-\mu_k h}{\lambda_k-\mu_k}.\tag{9}$$

All equations in (3)–(9) are ring equalities. They include the entire
quadratic cross term modulo $7^k$.

**Proof of the stabilizers and histogram.** Fixing $(s,t)$ requires
$(h-1)s=0$ and $(h^{-1}-1)t=0$. Since $h$ is a unit, this is
equivalent to

$$h\equiv1\pmod{7^{k-m}}.$$

For $m<k$ that congruence has $7^m$ unit solutions. The orbit is the
image of the group, and each orbit point has a coset of that stabilizer
as its preimage, proving (5). The number of pairs with minimum depth
$m$ is

$$7^{2(k-m)}-7^{2(k-m-1)}=48\cdot7^{2(k-m-1)}.$$

The split map is invertible, so these are also counts of original
scalar pairs. Set $j=k-m$ for the histogram; it sums to $7^{2k}$
after adding zero. Primitive pairs, $m=0$, make up $48/49$ of all
pairs, which proves the median assertion. Summing the logarithm of
the return count against the histogram proves (6); the needed finite
weighted sum is

$$\sum_{r=0}^{k-1}r49^r
=\frac{(48k-49)49^k+49}{48^2},$$

obtained by subtracting the sum from its multiple by 49.

**Proof of the tail.** Let $b$ be the largest $j\in\{1,\ldots,k\}$
with $6\cdot7^{j-1}<n^\varepsilon$, or put $b=0$ if there is no
such $j$. The origin is bad because $n^\varepsilon>1$. Summing the
first $b$ histogram levels gives the exact count

$$B_\varepsilon^{\rm mod}(k)
=1+48\sum_{j=1}^b7^{2j-2}=7^{2b}.\tag{10}$$

For $b\ge1$, its definition gives
$7^b<(7/6)n^\varepsilon$, which proves (7). The case $b=0$ is
immediate. The restriction $\varepsilon<1$ is essential for a positive
bad exponent; at threshold $n$ the maximum return $(6/7)n$ is already
too small. $\square$

### Meaning

Passing to higher powers of one prime produces many action choices
without any nonzero identity-only residue state. Deeply divisible
pairs have stabilizers, but their populations decrease exactly fast
enough to give the lower-tail bound (7). No probabilistic extrapolation
or independent-digit return product is used.

### Consequence

**Modular gadget and tail: PROVED.** The norm image in the ring is
exactly all $R_k$, since split coordinates $(1,t)$ realize every value.
Its size $n$ and the modular exponents above must not be substituted
into the real DC-R1 theorem without an exact real realization.

## 3. MG-3 — canonical real lift fails the return exponent

### Statement

The canonical centered representatives are

$$A_k=X_k=Y_k=
\{-(7^k-1)/2,\ldots,(7^k-1)/2\}\subset\mathbb Z,
\qquad n=7^k.\tag{11}$$

For an explicit surviving real action family, choose
$U_k^{\rm real}=\mu_6=\{\pm1,\pm\omega,\pm\omega^2\}$.
Its identity-only set is exactly

$$I_k^{\rm real}=\{p\in A_k^2:R_{U_k^{\rm real}}^{\rm pair}(p)=1\}
=\{(0,0)\}.$$

Indeed $A_k=-A_k$, so the two signs return every nonzero pair to
two distinct targets, while zero has only one target. This argument
also applies to every finite actual action family containing
$\{1,-1\}$; it is the sign-closed case of
[RT-G3](geometry.md), §3. Thus removing nonzero identity-only states
does not repair the real return tail proved below.

Coordinatewise reduction is a bijection between $A_k^2$ and $R_k^2$.
Conjugating the modular permutations by that bijection gives
permutations of the integer square, but they need not preserve the
real value of $Q$.

Indeed set $b=(n-1)/2$ and use the modular action corresponding to
$\omega$. Its actual linear formula sends

$$T_\omega(b,b)=(b,-2b),$$

which is outside $A_k^2$. Centered reduction replaces it by $(b,1)$,
and

$$\boxed{Q(b,1)-Q(b,b)
=-n(b-1)\ne0\qquad(k\ge1).}\tag{12}$$

The exact real obstruction is stronger. For every fixed
$\varepsilon>0$, uniformly over **any** supplied family of actual
norm-one multipliers, all pairs of (11) eventually have fewer than
$n^\varepsilon$ distinct genuine returned pairs. Thus

$$\boxed{B_\varepsilon^{\rm real}(k)=n^2
\quad\text{for all sufficiently large }k.}\tag{13}$$

This conclusion uses the accepted integer norm-fiber theorem; it is
not obtained by rerunning an interval search.

**Justification from retained results.**
[HR-4A](../2026-09-16-high-return/denominator-obstruction.md), equation
(20), proves for every positive integer $N$

$$\#\{(x,y)\in\mathbb Z^2:Q(x,y)=N\}\le6\tau(N).$$

[HR-4B](../2026-09-16-high-return/denominator-obstruction.md), equation
(21), proves for every $\theta>0$ a constant $D_\theta$ with
$\tau(N)\le D_\theta N^\theta$. These complete local proofs were
read for this application, not rederived or rerun.

For (11), $0\le Q(x,y)\le3b^2<3n^2/4$. Any actual norm-preserving
return remains in the corresponding integer norm fiber. Taking
$\theta=\varepsilon/4$ in the two cited bounds gives, uniformly for
every nonzero source, at most

$$6D_{\varepsilon/4}(3n^2/4)^{\varepsilon/4}
=O_\varepsilon(n^{\varepsilon/2})<n^\varepsilon$$

targets for sufficiently large $n$. Zero has only one. This proves
(13), even if every norm-one multiplier producing a return is allowed.
The same retained bounds imply the familiar actual-image lower bound
$|Q(A_k,A_k)|\ge c_\xi n^{2-\xi}$ for every fixed $\xi>0$; no
fixed power saving holds for this specific lift.

### Meaning

The full modular domains count targets with norm merely congruent to
the source norm. Real returns require exact equality. Centered
wraparound already breaks that equality for the torsion action
$\omega$, and the retained integer-fiber bound excludes an alternative
large real return family on these same inputs.

### Consequence

**Canonical centered lift: RETURN-TAIL FAIL.** This is a scoped
application to the polynomial-height integer carrier (11), not a
universal obstruction to other real realizations of a modular gadget.
For each modular norm residue there are $O(n)$ possible integer norm
values in the actual range $[0,3b^2]$; ignoring this quotient or carry
coordinate would lose exactly the distinction between a modular
support bound and a real one.

## 4. MG-4 — the composition cost of a homomorphic action lift

### Statement

Every finite-order element of the rational norm-one group

$$\mathcal T(\mathbb Q)=
\{u\in\mathbb Q(\omega)^\times:u\bar u=1\}$$

belongs to $\{\pm1,\pm\omega,\pm\omega^2\}$. Consequently every
group homomorphism $\rho:G_k\to\mathcal T(\mathbb Q)$ has

$$\boxed{|\rho(G_k)|\le6.}\tag{14}$$

For $k\ge2$ there is no group-homomorphic section of reduction that
lifts every element of $G_k$ to a rational norm-one multiplier while
preserving the same multiplication law. Such a section would be
injective, whereas $|G_k|=6\cdot7^{k-1}>6$.

More explicitly, restrict reduction to rational coefficients whose
denominators are coprime to 7. Equation (3) then defines a reduction
map from those norm-one elements to $G_k$. A section of that map is
impossible for $k\ge2$. At $k=1$, the six Eisenstein roots of unity
do reduce bijectively to $G_1$; this still does not supply Cartesian
membership for the integer lift, as (12) shows.

**Proof.** The accepted norm-Euclidean proof in HR-4A gives unique
factorization in $\mathbb Z[\omega]$. If $u\in\mathbb Q(\omega)$
has finite order, each irreducible valuation of $u$ is zero, since
an integer multiple of it is the valuation of 1. Cancelling numerator
and denominator factors therefore makes $u$ an integral unit. HR-4A
also proves that there are exactly six such units, the displayed
roots. A finite group's image consists of finite-order elements, so
(14) follows. The section contradiction is immediate. $\square$

The field restriction in (14) must remain explicit: arbitrary complex
roots of unity can form larger finite groups. There is nevertheless
a corresponding obstruction for this **integer carrier** even if the
homomorphism is allowed to take arbitrary complex norm-one values.
If $u$ maps a nonzero integer pair $p$ to an integer pair $q$, then

$$u=\frac{x_q-\omega y_q}{x_p-\omega y_p}\in\mathbb Q(\omega).
\tag{15}$$

Every value of a finite-group homomorphism has finite order. By (15)
and the proved six-unit statement, at most six distinct values in such
an image can have a nonzero return to (11). The origin has one distinct
target. This does not exclude nonhomomorphic assignments of modular
labels to infinite-order rational actions, but MG-3 independently
excludes a polynomial return tail for those actions on (11).

### Meaning

A composition-preserving rational lift collapses at least
$7^{k-1}$ labels per largest fiber: at most six actual multipliers
remain from $6\cdot7^{k-1}$ modular labels. Passing to additional
complex roots of unity does not make those roots act on nonzero integer
pairs unless they already lie in the rational Eisenstein field.

### Consequence

This is a homomorphic-action realization obstruction. The centered
height obstruction in MG-3 is a separate argument and should not be
charged as an additional multiplicative loss to the same hypothetical
construction. Neither theorem rules out a different noninteger carrier
with a separately proved scalar identity and full return tail.

## 5. Exact ledger and disposition

| Item | Modular gadget | Canonical real lift |
|---|---|---|
| Scalar inputs | Exactly $n=7^k$ residue classes | Exactly $n=7^k$ centered integers |
| Coordinate overlap | $X=Y=R_k$ | $X=Y=A_k$ |
| Thinning in both coordinates | None; all $n^2$ modular pairs | None; all $n^2$ integer pairs |
| Parameter/projection fibers | One under invertible split coordinates | One as a set-theoretic representative map; that map does not preserve scalar $Q$ |
| Action inventory | $6\cdot7^{k-1}$ distinct ring multipliers | A homomorphic rational lift has at most six distinct multipliers; arbitrary real return families are separately bounded by integer fibers |
| Composition | Exact $T_hT_g=T_{hg}$ in one residue ring; compatible under reduction | No exact real realization of the full wrapped action is supplied; (12) disproves the canonical one |
| Stabilizers | $7^m$ at minimum depth $m<k$; all labels at zero | Distinct real multipliers act freely off zero; zero has one target |
| Identity-only pairs | Exactly one, the origin | Exactly one, the origin, for the explicit surviving family $U_k^{\rm real}=\mu_6$, or any finite actual family containing both signs; nevertheless all actual counts are eventually below every fixed $n^\varepsilon$ |
| Median / geometric mean | Median $(6/7)n$; geometric mean (6), of order $n$ | Both at most $n^{o(1)}$, by the cited uniform fiber bound |
| Bad count | Exact (10), at most $(49/36)n^{2\varepsilon}$ for $0<\varepsilon<1$ | Exactly $n^2$ eventually for every fixed $\varepsilon>0$ |
| Scalar norm support | All of $R_k$, size $n$ | At least $c_\xi n^{2-\xi}$ for every fixed $\xi>0$, by retained HR-4A/B |
| Moduli and local splitting | One fixed split prime 7; modulus $7^k$ and explicit compatible roots | Modulo equality has an additional integer quotient/carry coordinate; it is not real equality |
| Heights and denominators | No archimedean assertion for residue representatives | Input height $(n-1)/2$, denominator 1; any nonzero integer return has multiplier (15) in the fixed field |
| Field/discriminant/regulator | Split finite ring, not a real field construction | Integer inputs and rational Eisenstein return ratios; degree 2, discriminant $-3$; no regulator/class-number/prime-density estimate used |
| Labels, branches and exceptions | Entire finite plane; zero and every valuation stratum explicitly included | Wrapped targets cannot be credited without checking exact $Q$; all genuine targets are charged by the full integer fiber |
| Rates | Modular input rate $\log7$, available $\varepsilon\in(0,1)$ and $\delta=2-2\varepsilon$; any positive overlap exponent | Return exponent zero in the required asymptotic sense; no positive bad-tail deficit; no $c>0$ via DC-R1 |

**Source boundary.** The preceding
[CRT cube-root proof](../2026-09-21-correlated-dc-o1/crt-domains.md),
CD-2/CD-3, used a three-letter scalar signature at distinct split primes
and a width-one rational factor-action box. Here the local alphabet is
the entire residue ring, there is only one fixed prime, and composition
uses its full norm torus through powers. The old diagonal obstruction
is genuinely absent in MG-1/MG-2, as their complete histograms show.
No old cube-root carrier is rerun.

The real-lift rejection applies the already proved
[HR-4A/B integer representation and divisor bounds](../2026-09-16-high-return/denominator-obstruction.md),
equations (20)–(21). The target implication remains
[DC-R1](../2026-09-21-dense-cartesianization/block-rectangle.md), Section
4, with **real** genuine returns. Its hypotheses are not supplied by a
finite-ring image count. The [project map](../../CURRENT_PROJECT_MAP.md),
[T03 status](../../tracks/03-eisenstein-cartesianization/STATUS.md) and
[migration conflicts](../../MIGRATION_CONFLICTS.md) preserve the fixed
target, separate RC15/4 obligation and source availability; no missing
external input is needed for this note.

**Scoped disposition:** a strong fixed-prime **modular** return tail is
proved; its canonical integer realization and composition-preserving
lift fail in the precise senses above. This is not a real DC-O1 witness.
No alternate field, prime or carrier search is launched here.

**Single retained obligation:** construct globally compatible **real**
partial-return domains with polynomial multiplicity outside a fixed
power-saving bad set on almost-common coordinate sets.
