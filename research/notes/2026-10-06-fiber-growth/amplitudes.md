# Phased chords: explicit amplitudes, scalar growth and subfield spreading

**6 October 2026 · T03 · version 1.** Fixed polynomial
$Q(x,y)=x^2+xy+y^2$. Specialist A; symbolic work only, zero mathematical
program evaluations, zero research-program CPU seconds, no network and no
outside theorem import. The lead approved the single amplitude rule below.
The initial unphased chord suggestion was only screened before selection;
this note claims no proved failure theorem for that suggestion.

The governing question is the prescribed-amplitude XB-O1 model in
[the cross-block checkpoint](../2026-10-06-cross-block-returns/README.md).
Its field quantifier concerns $[K^+:F]=2$, which must not be confused
with $[F:\mathbb Q]=2$. Both classifications are given in §1.
The currently authorized spreading gate allows a fixed constant
$C n^{1-\kappa}$; the theorem here gives explicit $\kappa=1/2$ and
$C=64\sqrt2$. It does not claim a coefficient-one bound at that exponent.

| Claim | Status and exact scope | Locator |
|---|---|---|
| FG-A1 | PROVED: all quadratic-field and index-two-subfield choices for the prescribed cyclotomic real field | §1 |
| FG-A2 | PROVED: exactly $8q$ nonzero amplitudes with disjoint norm-orbit cosets, with an explicit coupled recursion | §2 |
| FG-A3 | PROVED: exact same-set completion, $q^2/2\le n\le48q^2$, input factor49 per tower level | §3 |
| FG-A4 | PROVED: every line over the unique index-two subfield contains at most $64q$ carrier values | §4 |
| FG-A5 | PROVED accounting: encoded rich pairs number $48q^2=\Theta(n)$, not a near-full square; the local identities do not establish a full return tail | §5 |

The local UFD input is the already supplied elementary proof in
[HR-4A](../2026-09-16-high-return/denominator-obstruction.md).
The sparse cyclotomic argument below is written explicitly. The prior
fixed-field and bounded-line carrier obstructions are not silently
applied to this different growing-field completion. Independent internal
reviews and the lead's acceptance are recorded separately.

## 1. FG-A1 — exactly which quadratic subfields occur

### Statement

Let $r=k-1\ge1$, $q=7^r$, $m=6q$, and choose compatible roots

$$\omega=e^{2\pi i/3},\qquad \xi=\xi_r=e^{2\pi i/q},\qquad
L=\mathbb Q(\zeta_m)=\mathbb Q(\omega,\xi),\qquad K^+=L\cap\mathbb R.$$

Then

$$[L:\mathbb Q]=12\cdot7^{r-1},\qquad
[K^+:\mathbb Q]=6\cdot7^{r-1}.$$

There is exactly one subfield $F\subset K^+$ with $[K^+:F]=2$:

$$\boxed{F=\mathbb Q(\xi+\xi^{-1}),\qquad
K^+=F(\sqrt{21}).}\tag{1}$$

There is also exactly one subfield of $K^+$ of degree two over
$\mathbb Q$, namely $\mathbb Q(\sqrt{21})$. These are distinct
descriptions: $[F:\mathbb Q]=3\cdot7^{r-1}$, whereas
$[\mathbb Q(\sqrt{21}):\mathbb Q]=2$.

The involution associated with (1) fixes $\omega$ and sends
$\xi\mapsto\xi^{-1}$. In terms of $\zeta_m$ it is

$$\sigma(\zeta_m)=\zeta_m^{2q-1}=\omega\zeta_m^{-1}.
\tag{2}$$

At $k=1$, $q=1$ and $K^+=\mathbb Q$, so neither type of quadratic
subfield occurs.

### Meaning

For every nontrivial tower level, the spreading maximum in XB-O1 ranges
over one fixed-subfield choice, then all its scalar multiples. The
one-dimensional $F$-spaces remain numerous; uniqueness of $F$ is not
itself a spreading theorem.

### Consequence

To verify the gate it suffices to bound intersections with every
$\alpha F$, $\alpha\in(K^+)^\times$. We will use the exact
decomposition $K^+=F\oplus\sqrt{21}F$.

### Proof: degree, automorphisms and the explicit quadratic element

Put $s=q/7$. The polynomial

$$\Phi_q(T)=1+T^s+\cdots+T^{6s}$$

is irreducible even over $\mathbb Q(\omega)$. Here is a local proof
that also supplies the sparse equality test used later. In the supplied
UFD $\mathbb Z[\omega]$, the element $\pi=3+\omega$ is prime:
the quotient is $\mathbb F_7$, via $\omega\mapsto4$.
Also $\pi\overline\pi=7$, and $\overline\pi=2-\omega$ has
nonzero image modulo $\pi$, so $\pi^2$ does not divide7.

The monic polynomial $\Phi_q(T+1)$ has constant coefficient7.
Modulo7, multiplying it by $T^s$ gives $T^q$, using
$(T+1)^{7^j}=T^{7^j}+1$ in characteristic7. Its reduction is
therefore $T^{q-s}$. All nonleading coefficients are divisible by
$\pi$ and its constant is not divisible by $\pi^2$. The elementary
Eisenstein argument applies: by the UFD content argument, a monic
factorization over the fraction field gives monic factors in the ring;
modulo $\pi$ both positive-degree factors would be powers of $T$,
forcing both constant terms divisible by $\pi$, a contradiction.
This proves the asserted irreducibility and the displayed field degrees.

The automorphisms of $L$ are the independent choices
$\omega\mapsto\omega^\varepsilon$ and $\xi\mapsto\xi^a$,
where $\varepsilon\in\{1,-1\}$ and $a\in(\mathbb Z/q)^\times$.
There are exactly as many as the degree just proved. Complex conjugation
is $(-1,-1)$, so

$$\operatorname{Gal}(K^+/\mathbb Q)
\cong\bigl(\{\pm1\}\times(\mathbb Z/q)^\times\bigr)
/\langle(-1,-1)\rangle
\cong(\mathbb Z/q)^\times,$$

with the last map $(\varepsilon,a)\mapsto\varepsilon a$.
This group has exactly one nontrivial element of order two: if
$a^2=1\pmod{7^r}$, the factors $a-1,a+1$ cannot both be divisible
by7, so one is divisible by $7^r$. Thus $a=\pm1$.
The Galois correspondence gives a unique index-two subfield of $K^+$.
The fixed field of the explicitly displayed involution contains
$\mathbb Q(\xi+\xi^{-1})$, which has the required half-degree,
proving its description in (1).

There is exactly one index-two subgroup of $(\mathbb Z/q)^\times$:
any character to $\{\pm1\}$ vanishes on the odd-order kernel of
reduction modulo7, and $\mathbb F_7^\times$ is cyclic of order6.
Thus $K^+$ has exactly one degree-two field over $\mathbb Q$.
To identify it without a quadratic-field citation, let
$\eta=\xi^{q/7}$ and

$$A=\eta+\eta^2+\eta^4,\qquad
B=\eta^3+\eta^5+\eta^6.$$

Then $A+B=-1$ and $AB=3+\sum_{j=1}^6\eta^j=2$, so
$(A-B)^2=-7$. Since $(1+2\omega)^2=-3$, the nonzero real element
$(1+2\omega)(A-B)$ has square21. It is negated by $\sigma$,
hence lies outside $F$. This proves $K^+=F(\sqrt{21})$ and identifies
the unique degree-two field. Formula (2) follows from
$2q-1\equiv1\pmod6$, $2q-1\equiv-1\pmod q$.

## 2. FG-A2 — one explicit coupled amplitude rule

### Statement

For every $q=7^r$, including the seed $r=0$, choose exactly

$$\boxed{c_{h,j}=h(1+\omega\xi^j),\qquad
h\in\{1,2,\ldots,8\},\quad j\in\mathbb Z/q.}\tag{3}$$

All $8q$ amplitudes are nonzero, belong to $L$, and have pairwise
different squared complex absolute values, that is, relative norms
$N_{L/K^+}(c)=c\overline c$. Consequently their $\mu_m$ cosets are
pairwise disjoint, as required by the prescribed lift model.

This is a coupled tower recursion. With $\xi_{r+1}^7=\xi_r$, every
child index is $a+7j$, $0\le a\le6$, and

$$\boxed{c^{(r+1)}_{h,a+7j}
=\xi_{r+1}^a c^{(r)}_{h,j}+h(1-\xi_{r+1}^a).}\tag{4}$$

The union of amplitude orbits has the exact alternative description

$$Z_q=\bigcup_{h,j}c_{h,j}\mu_m
=\{h\kappa(\xi^a+\omega\xi^b):
h=1,\ldots,8,\ \kappa\in\mu_6,\ a,b\in\mathbb Z/q\}.
\tag{5}$$

It has exactly $48q^2$ actual complex elements.

### Meaning

The child rule rotates about the shared center $h$, with changing
tower phases. It does not attach independent radial tags. Equation (5)
couples two angular addresses and is the source of scalar coordinate
reuse in the Cartesian completion.

### Consequence

The amplitude-count, distinct-coset and exact whole-scalar action gates
pass. The $8q$ radii are actual distinct values, not repeated labels.
Disjointness of the complex orbits does not imply that their scalar
coordinate projections are disjoint.

### Proof: sparse cyclic equality and norm separation

For coefficients in $\mathbb Q(\omega)$, any polynomial of degree
less than $q$ vanishing at $\xi$ is a multiple of $\Phi_q$, by §1.
Its quotient has degree less than $s=q/7$. Thus its cyclic coefficient
vector is constant on each seven-position block
$\{a,a+s,\ldots,a+6s\}$, $0\le a<s$.
In particular a relation supported on fewer than seven positions is
zero coefficient by coefficient.

The norm in (3) is

$$N(c_{h,j})=h^2(2+\omega\xi^j+\omega^2\xi^{-j}).$$

Equality with the norm indexed by $(g,\ell)$ would give

$$2(h^2-g^2)+h^2\omega\xi^j+h^2\omega^2\xi^{-j}
-g^2\omega\xi^\ell-g^2\omega^2\xi^{-\ell}=0.\tag{6}$$

There are at most five occupied cyclic positions, so each coefficient
vanishes. If $j,\ell\ne0$ and $\ell\ne\pm j$, a position occupied
by only one term contradicts this. If $\ell=j$, coefficient comparison
gives $h=g$. If $\ell=-j$, it would give $h^2\omega=g^2\omega^2$,
impossible for positive rational $h,g$. If exactly one index is zero,
the other contributes a nonzero isolated coefficient. If both are zero,
the norms are $h^2,g^2$. This proves distinctness for $r\ge1$; at
$r=0$ only the last case occurs. Nonvanishing follows also because
$1+\omega\xi^j=0$ would put the order-six root $-\omega^2$ in
the odd order-$q$ group.

Equation (4) is direct substitution. Every root in $\mu_m$ has a unique
expression $\kappa\xi^a$, because 6 and $q$ are coprime. Replacing
$a+j$ by $b$ proves (5). Each nonzero orbit has $6q$ points and the
$8q$ orbits are disjoint, proving $|Z_q|=48q^2$.

## 3. FG-A3 — actual scalar growth and projection reuse

### Statement

Decode $z=x-\omega y$ with real coordinates, and let $A_q$ be the
union of both projections of $Z_q$. The two projections agree because
$\omega\in\mu_m$ and $M_\omega(x,y)=(y,-x-y)$.
Thus $A_q$ is the exact same-set completion, with $A_q=-A_q$ and
$0\in A_q$.

For $q\ge7$, put $\Delta=1+2\omega$ and

$$C_a=\frac{\xi^a+\xi^{-a}}2\in F,\qquad
D_a=\frac{\xi^a-\xi^{-a}}{2\Delta}\in\sqrt{21}F.$$

These are real and satisfy $C_a^2+3D_a^2=1$. The pair decoding
$\xi^a+\omega\xi^b$ is

$$X_{a,b}=C_a+D_a-2D_b,\qquad
Y_{a,b}=-C_b-2D_a+D_b.\tag{7}$$

Consequently the precise scalar alphabet is

$$\boxed{A_q=\bigcup_{h=1}^8
\{\pm hX_{a,b},\ \pm hY_{a,b},\ \pm h(X_{a,b}+Y_{a,b}):
a,b\in\mathbb Z/q\}.}\tag{8}$$

Writing $n_q=|A_q|$, one has

$$\boxed{q^2/2\le n_q\le48q^2.}\tag{9}$$

In particular, with depth $r=k-1$, $n_q=49^{r+o(r)}$. This input
factor49 is proved for this new family, not inferred for an older carrier.

### Meaning

Two addresses are coupled in each scalar. Many different orbit points
share an individual coordinate, but the first projection retains at
least a quadratic number of distinct scalar values. These bounds charge
all address coincidences exactly at the level needed for the rate.

### Consequence

Actual input growth is established. Field degree grows with $q$;
bounded conjugate sizes do not bring this family into the frozen
fixed-field height obstruction.

### Proof

The involution of §1 fixes $C_a$ and negates $D_a$; conjugation fixes
both real values. Since $\xi^a=C_a+\Delta D_a$, its norm-one
identity gives $C_a^2+3D_a^2=1$. Expanding
$\xi^a+\omega\xi^b$ and using $\omega^2=-1-\omega$ gives
(7). The six unit actions permute, up to sign, the coordinates
$x,y,x+y$, proving (8). The case $a=b=0$ has $X=1,Y=-1$,
so a unit-rotated point supplies the coordinate zero.

The real values $D_a=\sin(2\pi a/q)/\sqrt3$ are injective as
$a$ runs modulo the odd integer $q$: equality of two sine values
requires equal angles modulo $2\pi$ or angles summing to $\pi$
modulo $2\pi$, and the second option would require $2(a+b)$ to
be an odd multiple of $q$. Also $C_a=C_{a'}$ forces $a'=\pm a$,
and $C_a\ne0$ because an odd-order root cannot have argument
$\pi/2$ modulo $\pi$.

If $X_{a,b}=X_{a',b'}$, comparing even parts gives $C_a=C_{a'}$,
leaving at most two choices for $a'$. Its odd part then determines
$D_{b'}$, hence at most one $b'$. The $q^2$ first-coordinate labels
therefore have fibers of size at most two. This proves the lower bound
in (9). Equation (8) has at most $8\cdot6q^2$ labels, proving the
upper bound without assuming any further injectivity.

## 4. FG-A4 — quantitative spreading over every relevant subfield line

### Statement

For every $q\ge7$ and every $\alpha\in(K^+)^\times$,

$$\boxed{|(A_q\setminus\{0\})\cap\alpha F|
\le64q\le64\sqrt2\,n_q^{1/2}.}\tag{10}$$

Since $F$ is the unique subfield with $[K^+:F]=2$, this bounds the
entire subfield maximum in the active spreading gate. It proves that
gate with $C=64\sqrt2$ and $\kappa=1/2$.

### Meaning

The new amplitude rule escapes concentration in a bounded number of
lines over the relevant fixed field. The estimate counts scalar values,
not phase labels or formal projections.

### Consequence

The spreading prerequisite passes. Spreading alone does not prove
large quadratic fibers or a near-full genuine-return tail.

### Proof by a projective equation

Write $\alpha=E_0+O_0$ with $E_0\in F$, $O_0\in\sqrt{21}F$.
For $z=E+O$, membership in $\alpha F$ is exactly
$E_0O-O_0E=0$. If $E_0\ne0$, put $R=O_0/E_0$; the condition
becomes $O=RE$. If $E_0=0$, it becomes $E=0$.

For $X_{a,b}$, the even part is the nonzero $C_a$. A pure odd line
contains none of these values. On every other line the equation is
$D_a-2D_b=RC_a$. For each $a$, it determines $D_b$ uniquely,
hence at most one $b$. This gives at most $q$ labels. For $Y_{a,b}$,
fixing $b$ similarly determines $D_a$, again giving at most $q$.

Finally

$$X_{a,b}+Y_{a,b}=(C_a-C_b)-(D_a+D_b).$$

On a pure odd line, $C_a=C_b$, so each $a$ allows at most two
$b$. Otherwise the line equation rearranges to

$$D_b-RC_b=-D_a-RC_a.$$

For fixed $a$, this is a genuine real affine line in $(C_b,D_b)$:
its $D_b$ coefficient is one. A line meets the ellipse
$C_b^2+3D_b^2=1$ in at most two points; the angular parametrization
is injective. Hence there are at most $2q$ labels of this third type.

Every $h\in\{1,\ldots,8\}$ is a nonzero element of $F$ and does
not alter line membership. The two signs and eight scales in (8)
therefore give at most $16(q+q+2q)=64q$ values on any line.
Counting labels only enlarges the bound, so repeated scalar values
cause no difficulty. The lower bound in (9) implies
$q\le\sqrt{2n_q}$ and proves (10).

## 5. FG-A5 — what the orbit identities do and do not cover

### Statement

The finite selected action family is the actual group $\mu_m$.
At every encoded pair $\phi^{-1}(z)$, $z\in Z_q$, it gives all
$6q$ distinct members of that amplitude orbit, all inside $A_q^2$.
There are exactly $48q^2$ such encoded pairs, by (5) and injectivity
of the real map $(x,y)\mapsto x-\omega y$.

Together with (9), this says

$$|\phi^{-1}(Z_q)|=48q^2=\Theta(n_q),\qquad
\frac{|\phi^{-1}(Z_q)|}{n_q^2}=\Theta(n_q^{-1}).\tag{11}$$

These are selected full-orbit points only. Every unencoded Cartesian
pair remains part of the target problem; none is removed or credited
with the encoded return multiplicity.

### Meaning

The amplitudes, real projection, input rate and projective spreading
are now proved. The encoded return factor7 per tower level, on only
linearly many pairs, is not a typical return factor for the completed
square. Reusing scalar coordinates has not yet supplied the necessary
cross-block norm equalities.

### Consequence

A completed-square fiber theorem is required beyond these identities.
The separate specialist has now supplied it for this unchanged rule:
[FG-F1, fibers.md §§5–6](fibers.md), proves a quadratic-sized source
population with uniformly bounded complete fibers, and hence
$|Q(A_q,A_q)|=\Theta(n_q^2)$. That proof was independently audited
after the structural claims here. Thus the cross-block growth gate is
**FAILED for this carrier**, while its amplitude, input and spreading
gates remain proved. The image lower bound comes from that full-fiber
proof, not from the sparse engineered subset or an old bounded-line
obstruction.

## 6. Charged construction ledger

| Required item | Exact accounting |
|---|---|
| Parameter order | Choose $r=k-1$, then $q=7^r,m=6q$, compatible $\xi$, and the fixed eight scales; no further parameter search |
| Amplitude inventory | Exactly $8q$ actual nonzero amplitudes, all orbit cosets disjoint by norm separation |
| Exact scalar projection | Equation (8); the two coordinate projections agree; repeated scalar labels identified |
| Input lower/upper counts | $q^2/2\le n_q\le48q^2$, hence input factor49 per tower level |
| Input thinning twice | None; the final carrier is used in both coordinates and all $n_q^2$ pairs remain in scope |
| Spreading | The unique index-two subfield is $F$; every scalar multiple meets $A_q\setminus\{0\}$ in at most $64\sqrt2\,n_q^{1/2}$ values |
| Norm-preserving actions | Exactly $6q$ distinct roots of unity; whole-scalar multiplication preserves every cross term |
| Stabilizers / zero | All encoded points are nonzero and actions are free; zero is in the completed square and has one distinct returned pair |
| Encoded coverage | Exactly $48q^2=\Theta(n_q)$ pairs, hence only $\Theta(1/n_q)$ of the square |
| Field degree | $[L:\mathbb Q]=12\cdot7^{r-1}$ and $[K^+:\mathbb Q]=6\cdot7^{r-1}$; these grow |
| Denominators | Amplitudes and actions are algebraic integers; decoded inputs satisfy $3A_q\subset\mathcal O_{K^+}$ because division uses $1+2\omega$, whose square is $-3$ |
| Conjugate sizes | Every amplitude conjugate has absolute value at most16; every decoded coordinate conjugate has absolute value at most $32/\sqrt3$. No fixed-field conclusion follows from this bound |
| Discriminant / regulator / splitting | No volume, regulator or prime-density estimate is used to claim a gain; the sole local split prime in the sparse proof is explicitly $7=(3+\omega)(2-\omega)$ |
| State and branch multiplicity | Eight scales and all angular addresses are charged; norm labels are injective, scalar labels need not be |
| Full-image / tail gate | FAILED for this exact carrier by the separate FG-F1 full-fiber proof; the structural identities alone establish no positive full-square return exponent |
| Evidence | New exact symbolic derivations and specified internal audits; zero program runs, no numerical comparison |

This finishes specialist A's one approved amplitude rule. There is no
new mutation, prime sweep, third construction or proposed computation in
this file. The complete written FG-A1–FG-A5 argument passed the audit
specialist's independent internal mathematical review. The lead's final
acceptance and the separate FG-F1 review are recorded in the cycle report.
These are internal audits, not external review. The general target remains
separate from the positive spreading result and this carrier's negative
full-image result.
