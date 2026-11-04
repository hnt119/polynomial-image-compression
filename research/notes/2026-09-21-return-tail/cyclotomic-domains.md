# Cyclotomic traces: exact full-square return domains

**Date/version:** 21 September 2026, version 1. **Track:** T03,
return-tail cycle. **Fixed polynomial:** $Q(x,y)=x^2+xy+y^2$.

## Identity, evidence and scope

This is the one cyclotomic trace mechanism assigned in the newly
authorized strictly offline cycle. The active local attachment is
<code>[private task attachment]
The subtask has **zero program runs or mathematical evaluation budget**,
no network access, no outside theorem import and no novelty claim.
Only this new companion is authored.

The statements below are **PROVED by complete internal derivation**.
Independent review is recorded separately. These are counts under the
entire displayed action family on the entire Cartesian square, not
counts confined to an engineered pair subset.

| Claim ID | Quantified scope and proof |
|---|---|
| CY-1 | §§1–2: every prime $p\ge11$, $p\equiv2\pmod3$; an explicit real trace carrier of size $3p+1$, $6p$ distinct actions, and exact sparse cyclic equality |
| CY-2 | §§3–5: every ordered pair of that carrier; exact action domains and the two-valued full return distribution |
| CY-3 | §6: exact lower tails and statistics; no identity-only pairs, but a quadratic actual low-return population at every fixed positive power threshold |

Source history and dependencies:

- [Latest correlated DC-O1 checkpoint](../2026-09-21-correlated-dc-o1/README.md):
  genuine full-square returns, exact exception counts and the retained
  OPEN witness. No earlier CRT, moving-pole, balanced-state or additive
  tensor carrier is modified here.
- [HR-4A](../2026-09-16-high-return/denominator-obstruction.md), §HR-4A,
  and [UE-P1](../2026-09-16-unit-exponent/primary-proof.md), §1.2:
  the supplied elementary proof that $\mathbb Z[\omega]$ is
  norm-Euclidean and hence a UFD. Only that algebraic fact is reused;
  neither old carrier is used.
- [TP-R1](../2026-09-16-two-prime-character/product-realization.md), §4:
  historical bounded-exponent context. The current torsion order $6p$
  grows, and its $6p$ actual actions are distinct.
- [SN-T03-1](../2026-09-14-study-notes/03-eisenstein.md),
  [HR-1](../2026-09-16-high-return/return-lemma.md), and
  [DC-R1](../2026-09-21-dense-cartesianization/block-rectangle.md), §4:
  scalar norm action, return accounting and same-set transport.
- Private status source
  <code>local-only/migration/sources/T03_CURRENT_STATE.md</code>, §§2, 13–15;
  the latest correlated-cycle addenda in
  <code>research/CURRENT_PROJECT_MAP.md</code> and T03 STATUS; and
  <code>research/MIGRATION_CONFLICTS.md</code>, MC-03/MC-05/MC-06.
  No unavailable F25 or arithmetic source is used.

This family uses roots of unity in a growing field and their real
traces. It is not a rational norm-one orbit coefficient completion.
Its exceptional orbit is identified by coefficient calculation, not
assumed as a large norm fiber.

## 1. CY-1 — exact carrier and scalar action

### Statement

Let $p\ge11$ be prime with $p\equiv2\pmod3$. Fix

$$\omega=(-1+i\sqrt3)/2,\quad \xi=e^{2\pi i/p},\quad
\mu_6=\{\pm1,\pm\omega,\pm\omega^2\},$$
$$U_p=\{\kappa\xi^r:\kappa\in\mu_6,\ r\in\mathbb Z/p\mathbb Z\},$$
$$A_p=\{v+v^{-1}:v\in U_p\},\quad X_p=Y_p=A_p,\quad n=3p+1.
\tag{1}$$

Then

$$|U_p|=6p,\quad |A_p|=n,\quad -A_p=A_p,\quad 0\notin A_p,
\quad |X_p\triangle Y_p|=0.\tag{2}$$

Put $\phi(x,y)=x-\omega y$. Every $u\in U_p$ preserves the full
scalar quadratic:

$$Q(\phi^{-1}(u\phi(x,y)))=|u\phi(x,y)|^2=Q(x,y).\tag{3}$$

Writing $u=a+b\omega$ with real $a,b$, the coefficient action is

$$M_u(x,y)=(ax+by,-bx+(a-b)y),\quad a^2-ab+b^2=1.$$

The exact domains and distinct-target counts studied here are

$$D_u=A_p^2\cap M_u^{-1}(A_p^2),\qquad
R(p_0)=|\{M_up_0\in A_p^2:u\in U_p\}|.\tag{4}$$

**Proof.** Since $p$ is coprime to 6, the groups $\mu_6$ and
$\langle\xi\rangle$ intersect only at 1; their products are distinct.
If $v+v^{-1}=w+w^{-1}$, then $w=v$ or $v^{-1}$ by the quadratic
$T^2-(v+v^{-1})T+1$. Only $1,-1$ are self-inverse, so the trace
count is $(6p-2)/2+2=3p+1$. Negating $v$ negates its trace.
A zero trace would give $v^2=-1$, forcing order four, impossible
in this group of order $6p$. Equation (3) follows from $|u|=1$.
Every source is nonzero, so distinct multipliers give distinct
returned pairs by cancellation in $\mathbb C$. $\square$

Eligible primes are unbounded by an elementary argument. Given any
finite list of primes $2\pmod3$, include 2 and let their product be
$P$. The integer $3P-1>1$ has none of those prime divisors, is not
divisible by 3, and is $2\pmod3$. At least one of its prime divisors
is $2\pmod3$, since a product of primes all $1\pmod3$ would be
$1\pmod3$. This supplies a new prime; discarding finitely many primes
below 11 still leaves an unbounded family. No density estimate is used.

### Meaning

Same-set compatibility and scalar norm preservation hold exactly.
Simultaneous negation supplies two distinct legal targets everywhere,
so the identity-only count is zero.

### Consequence

The absence of identity-only pairs does not decide the growing
return tail. Every remaining domain is computed below.

## 2. Sparse cyclic coefficient equality

### Statement

For $K=\mathbb Q(\omega)$, the polynomial
$\Phi_p(T)=1+T+\cdots+T^{p-1}$ is irreducible over $K$. Therefore
if $c_r\in K$ and $\sum_{r=0}^{p-1}c_r\xi^r=0$, all $c_r$ are
equal. A relation supported on fewer than $p$ positions is zero
coefficient by coefficient.

### Proof

The polynomial $T^2+T+1$ has no root in $\mathbb F_p$: a root would
have order three in $\mathbb F_p^\times$, but $3\nmid p-1$, and
1 is not a root since $p\ne3$. Thus
$\mathcal O/(p)\cong\mathbb F_p[T]/(T^2+T+1)$ is a field for
$\mathcal O=\mathbb Z[\omega]$, making $p$ a prime element of this UFD.

The shift

$$\Phi_p(T+1)=p+\binom p2T+\cdots+\binom p{p-1}T^{p-2}
+T^{p-1}$$

is monic, all nonleading coefficients are divisible by $p$, and
its constant term is not divisible by $p^2$. The usual content
argument can be checked in this ring: the product of two primitive
polynomials is primitive, because reduction modulo a prime dividing
all product coefficients would contradict the absence of zero
divisors in the resulting polynomial ring. Clearing denominators
and contents consequently turns a factorization of a monic polynomial
over $K$ into monic factors over $\mathcal O$. Modulo $p$, any
nontrivial factorization of the displayed shift would have two
positive-degree factors of $T^{p-1}$, hence two powers of $T$.
Both constant terms would be divisible by $p$, contradicting their
product $p$. This proves irreducibility of the shift and $\Phi_p$.

A polynomial of degree at most $p-1$ vanishing at $\xi$ is thus a
constant multiple of $\Phi_p$. If one of its $p$ coefficients is
zero, that constant is zero. $\square$

### Meaning

Two cyclic expressions with at most four terms each can be compared
coefficientwise, since their difference has at most eight positions
and $8<p$. This is an exact algebraic equality test.

### Consequence

We may classify actual returned scalar pairs by the support of
these short cyclic expressions, without numerical approximation or
assuming that arbitrary polynomial relations are absent.

## 3. CY-2 — classify every source support

### Statement

Put $C=\{-2,-1,1,2\}$. Choose one $k$ from each nonzero frequency
class $\{k,-k\}\subset\mathbb Z/p\mathbb Z$. Besides the four
constants $C$, the carrier consists of exactly the six values

$$t_{\kappa,k}=\kappa\xi^k+\kappa^{-1}\xi^{-k},
\qquad\kappa\in\mu_6,\tag{5}$$

for each class. All these values are distinct.

For $(x,y)\in A_p^2$, let $P_z$ be the cyclic coefficient vector of
$z=x-\omega y$ from these trace expressions. Its support is
nonempty and has size at most four. Either it is a single monomial,
or its support $S$ satisfies

$$S=-S,\qquad 2\le |S|\le4.\tag{6}$$

The monomial sources consist of the 16 constant pairs in $C^2$
and exactly $6(p-1)$ nonconstant pairs. The latter have values
$(\omega^2-\omega)\kappa\xi^r$, $\kappa\in\mu_6$, $r\ne0$.

### Proof

The trace equality criterion in §1 gives (5) and uniqueness after
choosing the sign of $k$. Sparse equality makes its cyclic vector
independent of that description. Distinct nonzero frequency classes
give four nonzero support positions for $x-\omega y$; one constant
and one nonconstant trace give three. Both supports are symmetric.
Two constant inputs give one nonzero coefficient at position zero.

For one common nonzero class, write $x=t_{\kappa,k}$ and
$y=t_{\lambda,k}$. The coefficients are

$$P_z(k)=\kappa-\omega\lambda,\qquad
P_z(-k)=\kappa^{-1}-\omega\lambda^{-1}.\tag{7}$$

The first vanishes exactly when $\kappa=\omega\lambda$, the second
exactly when $\kappa=\omega^2\lambda$; both cannot vanish.
In these cases the respective surviving coefficients are

$$(\omega^2-\omega)\lambda^{-1}\text{ at }-k,\qquad
(\omega^2-\omega)\lambda\text{ at }k.\tag{8}$$

There are twelve such pairs per frequency class, hence $6(p-1)$
in total. Otherwise the support is $\{k,-k\}$. $\square$

### Meaning

A generic source has a small symmetric frequency support.
Multiplication by $\xi^r$ shifts the whole support by $r$.

### Consequence

If a nonmonomial source returns under $u=\kappa\xi^r$, sparse
equality makes the target support exactly $S+r$. It too is
nonmonomial and symmetric, so

$$S+r=-(S+r)=-S-r=S-r,\qquad S+2r=S.\tag{9}$$

For $r\ne0$, translation by $2r$ generates the prime cyclic group,
forcing this nonempty invariant support to be the whole group,
contrary to $|S|\le4<p$. Thus every nonmonomial return has $r=0$.

## 4. The exceptional orbit and the small rotations

### Statement

Put $\Delta=\omega^2-\omega$, so $|\Delta|^2=3$, and

$$E_p=\phi^{-1}(\Delta U_p).\tag{10}$$

Then $E_p\subseteq A_p^2$, $|E_p|=6p$, and

$$\boxed{x+y\in A_p\quad\Longleftrightarrow\quad (x,y)\in E_p.}
\tag{11}$$

Every point of $E_p$ returns under every action of $U_p$.

### Proof

The nonzero-frequency elements in $\Delta U_p$ are exactly (8).
At frequency zero, $\Delta\mu_6$ has coefficient pairs

$$(1,1),\ (-1,-1),\ (1,-2),\ (-1,2),\ (2,-1),\ (-2,1).\tag{12}$$

For example $\Delta=-1-2\omega$ corresponds to $(-1,2)$;
multiplication by $\omega$ acts as $(x,y)\mapsto(y,-x-y)$, and
negation supplies the other signs. This verifies (12) and the
inclusion $E_p\subset A_p^2$. The coset $\Delta U_p$ has $6p$
distinct elements and is invariant under multiplication by $U_p$.

For (11), different nonzero frequency classes, or one constant
and one nonconstant trace, give four or three nonzero positions
in $x+y$. Sparse comparison prevents equality with a trace having
one or two positions. On a common nonzero class,

$$x+y=(\kappa+\lambda)\xi^k+
(\kappa^{-1}+\lambda^{-1})\xi^{-k}.$$

If $\lambda=-\kappa$, this is zero and not in $A_p$.
Otherwise it is in $A_p$ exactly when $\kappa+\lambda\in\mu_6$.
For sixth roots this is equivalent to
$\lambda/\kappa\in\{\omega,\omega^2\}$: the squared magnitude
of the sum is one exactly when the ratio has real part $-1/2$,
and conversely these two sums are sixth roots. These are precisely
the cases (7)–(8).

For constants in $C$, same-sign unit pairs have sum $\pm2$,
opposite-sign mixed magnitudes have sum $\pm1$, opposite equal
magnitudes have sum zero, same-sign mixed magnitudes have sum
$\pm3$, and same-sign magnitude-two pairs have sum $\pm4$.
Thus $x+y\in C$ occurs exactly for the six pairs (12). This proves
(11). $\square$

### Meaning

Additive triples in the trace carrier identify one explicitly
constructed linear-size orbit. Its existence is derived, rather
than assumed as a large norm fiber.

### Consequence

The six $\mu_6$ targets are

$$(x,y),\ (-x,-y),\ (y,-x-y),\ (-y,x+y),\
(-x-y,x),\ (x+y,-x).$$

Symmetry of $A_p$ makes the last four legal exactly when
$x+y\in A_p$. Outside $E_p$, only the two scalar signs return
among these six rotations.

## 5. Every action domain and its overlap

### Statement

On the full square,

$$\boxed{D_1=D_{-1}=A_p^2,\qquad
D_u=E_p\quad(u\in U_p\setminus\{1,-1\}).}\tag{13}$$

Consequently,

$$\boxed{R(p_0)=2+(6p-2)1_{E_p}(p_0)
\quad\text{for every }p_0\in A_p^2.}\tag{14}$$

All additional domains coincide; every intersection among them
is $E_p$.

### Proof

The two signs return everywhere. The other elements of $\mu_6$
have precisely domain $E_p$ by (11).
For $u=\kappa\xi^r$ with $r\ne0$, (9) makes every returning source
monomial. Every nonzero-frequency monomial source lies in $E_p$.
For a constant source, its coefficient $c=x-\omega y$ moves to
$\kappa c\xi^r$, a nonzero-frequency monomial. By (8), a legal
target requires $\kappa c\in\Delta\mu_6$, hence $c\in\Delta\mu_6$.
Thus this source also lies in $E_p$. Conversely $E_p$ is invariant
under every action. This proves (13); free action at every nonzero
source gives (14). $\square$

### Meaning

There are $6p$ distinct genuine actions, but every action beyond the
two signs spends its entire return domain on the same $6p$ points.

### Consequence

This is a full actual return-tail obstruction for the displayed
action family, not an uncovered-encoding certificate. It does not
restrict returns under other norm-one multipliers.

## 6. CY-3 — complete return statistics and lower tail

### Statement

The exact full-square histogram is

$$\begin{array}{c|cc}
R&2&6p\\\hline
\#\text{ ordered pairs}&n^2-6p&6p .
\end{array}\tag{15}$$

Hence:

- identity-only pairs: **zero**;
- minimum and median: $2$;
- maximum: $6p$;
- geometric mean: $2(3p)^{6p/n^2}\longrightarrow2$;
- arithmetic mean: $2+(6p-2)6p/n^2\longrightarrow6$.

For every real threshold $T$,

$$\#\{p_0:R(p_0)<T\}
=\begin{cases}
0,&T\le2,\\
n^2-6p,&2<T\le6p,\\
n^2,&T>6p.
\end{cases}\tag{16}$$

For every fixed $0<\varepsilon\le1$, eventually

$$\boxed{B_\varepsilon=n^2-6p=n^2-2n+2.}\tag{17}$$

For fixed $\varepsilon>1$, eventually $B_\varepsilon=n^2$.

### Proof

Equation (15) is (14). The high-return population is less than
half the square, since $n^2-12p=(3p-1)^2>0$, so the median is two.
The two means follow from the histogram, and $6p/n^2=O(1/p)$
gives their limits. Equation (16) is immediate. For
$0<\varepsilon\le1$, $n^\varepsilon$ eventually exceeds two and
is at most $n=3p+1<6p$. For $\varepsilon>1$ it eventually exceeds
$6p$. Finally $6p=2n-2$, proving (17). $\square$

### Meaning

Removing identity-only sources raises the typical return count
only to two. The rich orbit is linear in $n$, while the low-return
population is quadratic. The larger arithmetic mean comes entirely
from the sparse rich population.

### Consequence

No positive exceptional exponent $\delta$ is possible for this
family at any fixed positive return exponent. The reciprocal HR-1
certificate gives only

$$|Q(A_p,A_p)|\le
\frac{n^2-6p}{2}+1=\frac{n^2}{2}-3p+1.\tag{18}$$

This is a constant-factor upper bound, not a fixed power saving.
It is not claimed to be the exact image size: different $U_p$-orbits
can have the same norm. No actual-image lower bound follows here.

## 7. Arithmetic and construction ledger

The parameter is the eligible prime $p\to\infty$, with the recipe
(1) fixed first. No scout is a premise of these all-parameter claims.

The action field $L_p=\mathbb Q(\omega,\xi)$ has degree $2(p-1)$,
by §2. A primitive $6p$-th root in $U_p$ generates this field.
Its trace generates the real subfield of degree $p-1$: the root
satisfies a quadratic over its trace field and is not real, so
the degree over that trace field is exactly two. Thus the field
degree genuinely grows; no fixed-field unit argument is used.

Inputs are algebraic integers and all their real conjugates have
absolute value at most two. Actions are integral roots of unity.
For $u=a+b\omega$ with real coefficients,

$$b=\frac{u-\bar u}{\omega-\bar\omega},\qquad
a=\frac{\omega\bar u-\bar\omega u}{\omega-\bar\omega}.$$

These coefficients lie in the real field, and $3a,3b$ are algebraic
integers since $(\omega-\bar\omega)^2=-3$. Every real conjugate
of $a,b,a-b$ has magnitude at most $2/\sqrt3$, by the same
completed-square norm identity. These are exact algebraic matrix
entries, not floating-point rotations.

| Required item | Exact accounting and status |
|---|---|
| Input counts | Exact $n=3p+1\to\infty$ |
| Same-set comparison | $X=Y=A_p$; any fixed positive $\eta$ is allowed |
| Input thinning twice | None; all $n^2$ ordered pairs are classified |
| Trace fibers | Exactly inverse pairs in $U_p$, with the two self-inverse elements treated separately |
| Pair projection | $(x,y)\mapsto x-\omega y$ is injective on real pairs |
| Actual actions | Exactly $6p$ roots of unity; no label collapse |
| Scalar composition | Whole-scalar multiplication, equation (3) |
| Zero and stabilizers | $0\notin A_p$; every source is nonzero with trivial multiplier stabilizer |
| Domain overlap | Signs have full domain; every other action has the same $6p$-point domain |
| Identity-only tail | Exactly zero, but the typical return count is two |
| Actual full return tail | Exact (16); $B_\varepsilon=n^2-2n+2$ eventually for $0<\varepsilon\le1$ |
| Norm-shell use | The exceptional orbit is explicitly derived in (7)–(12), not assumed |
| Field degree | Real input field degree $p-1$; action field degree $2(p-1)$ |
| Discriminant, regulator, ideal volume | No estimate is used or assigned a favorable zero cost; no lattice-packing or growing-field support bound is claimed |
| Local prime condition | $p\equiv2\pmod3$ makes $p$ prime in $\mathbb Z[\omega]$, proved in §2; no residue-density saving is used |
| Heights and denominators | Inputs integral with conjugates bounded by two; actions integral; real matrix entries have denominator dividing three in the real field |
| Coefficient equality | Sparse cyclic comparison uses at most eight positions, below $p$ |
| Branches and exceptions | Every frequency class and all 16 constant pairs included; exact rich population $6p$ |
| Size/rate parameter | With $d=\log p$, $\log n=d+O(1)$ and $\log\lvert U_p\rvert=d+O(1)$; typical $\log R=\log2$ |
| Signed gate | Positive threshold exponent leaves quadratic bad mass, so no positive $\delta$ and no fixed $c>0$ via DC-R1 |
| Actual image | Only the constant-factor upper certificate (18); no exact asymptotic or new lower bound |

## 8. Disposition

**RETURN-TAIL FAIL for this cyclotomic trace carrier and the full
selected family $U_p$.** Scalar compatibility, distinct growing
actions, exact same-set overlap and no identity-only points are
proved. Polynomially growing returns occur on only $2n-2$ pairs.

Other trace carriers and additional norm-one action families are
outside this theorem. The sole active obligation remains DC-O1:
polynomially many genuine returns on almost every pair of an
almost-common rectangle. No additional mechanism is begun here.
