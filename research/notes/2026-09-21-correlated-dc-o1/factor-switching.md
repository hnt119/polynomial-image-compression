# Global factor switching: exact returns and coordinate cost

**Date/version:** 21 September 2026, version 1. **Track:** T03,
correlated DC-O1. **Fixed polynomial:** $Q(x,y)=x^2+xy+y^2$.

## Identity, evidence and source history

This is one bounded symbolic mechanism in the newly authorized strictly
offline cycle. Its authorization is the local attachment
`[private commissioning attachment; locator withheld]`.
There are **no program runs, allocated mathematical evaluations, network
calls, outside results or novelty claims**. Only this new file is authored.

The complete proofs below establish **FS-1–FS-3, PROVED by internal
derivation**. Independent review is a separate record. The construction
passes scalar norm composition and has many genuine returns on its
encoded factor words. It fails the stated encoded-coverage certificate
for almost every pair of the common scalar square. Its actual full
Cartesian return distribution and image rate are not determined here.

| ID | Exact scope and location |
|---|---|
| FS-1 | §1: partial conjugation of arbitrary nonzero complex factors, exact composition and pair-dependent norm multipliers |
| FS-2 | §§2–4: the explicit separated integer factor code, every integer depth $d\ge1$; exact word, action, norm and encoded-return counts, with finite-window specialization proved |
| FS-3 | §5: injectivity of the first coefficient on this code; same-set size $4^d\le n_d\le2\cdot4^d$ and exponentially sparse encoded coverage; certificate-only failure |

Controlling context and dependencies:

- [Latest DC-O1 checkpoint](../2026-09-21-dc-o1/README.md), §§1, 3,
  7, 9: genuine scalar cross terms, exceptions, and the retained
  correlated witness obligation. The old moving-pole, additive-tensor
  and balanced-state searches are not resumed.
- [SN-T03-1](../2026-09-14-study-notes/03-eisenstein.md):
  $N(x-\omega y)=Q(x,y)$ and the real coefficient action.
- [DC-R1](../2026-09-21-dense-cartesianization/block-rectangle.md), §4,
  and [HR-1](../2026-09-16-high-return/return-lemma.md): same-set
  transport and full-support return accounting. Their positive
  hypotheses are not supplied by the present encoded coverage.
- [Historical PTCR composition report](../../history-sources/Parity_Twisted_Cartesianization_Composition_Report.md),
  §§A, F: earlier factor-code and coefficient-overhead context. The
  present code has no parity twist, inert-prime alphabet, CRT lift or
  rephasing assertion; none of those historical searches is rerun.
- [UE-P1–UE-P3](../2026-09-16-unit-exponent/primary-proof.md), §§1–3,
  supply context for the earlier fixed-norm orbit and its coverage
  loss. That orbit and its generator recursion are not used here.
  The current code has $3^d$ different norm values, integral factor
  words, and a separate coefficient-injectivity proof.
- Private status authority `local-only/migration/sources/T03_CURRENT_STATE.md`,
  §§2, 5.5, 13–15; `research/CURRENT_PROJECT_MAP.md`, the dated DC-O1
  addendum; and `research/MIGRATION_CONFLICTS.md`, MC-03/MC-05/MC-06.
  Historical divisor richness did not establish Cartesian membership.
  No absent F25 or arithmetic-obstruction original is needed below.

## 1. FS-1 — partial conjugation is a scalar composition law

### Statement

Let $z=ab$ with $a,b\in\mathbb C^\times$. Then

$$z'=a\bar b=u_bz,\qquad u_b=\bar b/b,\qquad |u_b|=1,$$
$$N(z')=N(a)N(b)=N(z).\tag{1}$$

For any nonzero factors $\alpha_1,\ldots,\alpha_d$, consider

$$z_{\mathbf a,\mathbf b}
=\prod_{i=1}^d\alpha_i^{a_i}\bar\alpha_i^{b_i},
\qquad a_i,b_i\in\{0,1\}.$$

For $S\subseteq[d]$, let $F_S$ swap $a_i,b_i$ at the indices in
$S$. These are initially maps on labelled words; they need not be
well defined on an unlabelled value until injectivity is proved.
Conjugating exactly those site factors gives

$$F_S(z)=u_S(z)z,\qquad
u_S(z)=\prod_{i\in S}(\bar\alpha_i/\alpha_i)^{a_i-b_i}.
\tag{2}$$

On factor labels, the exact composition is

$$F_TF_S=F_{S\triangle T},\qquad
u_T(F_Sz)u_S(z)=u_{S\triangle T}(z).\tag{3}$$

Equations (1)–(3) are identities of actual complex numbers, hence of
the real scalar quadratic under $z=x-\omega y$.

**Proof.** Conjugation is multiplicative and preserves $b\bar b$,
which proves (1). Swapping an occupied $\alpha_i$ to $\bar\alpha_i$
multiplies by $\bar\alpha_i/\alpha_i$; the opposite swap uses its
inverse. A doubly occupied or empty site is unchanged. This proves
(2). Each swap is an involution, and swaps at different sites commute,
giving (3); the multiplier identity also follows by cancellation of
the nonzero starting value.

Here is the mixed-term calculation in scalar coefficients. Write
$a=r+s\omega$ and $b=t+v\omega$. Then

$$ab=(rt-sv)+(rv+st-sv)\omega,$$
$$a\bar b=(rt-rv+sv)+(st-rv)\omega.$$

Expanding the two norms gives the identical nine-term expression:

$$\begin{aligned}
N(ab)
&=(rt-sv)^2-(rt-sv)(rv+st-sv)+(rv+st-sv)^2\\
&=r^2t^2-r^2tv+r^2v^2-rst^2+rstv-rsv^2
  +s^2t^2-s^2tv+s^2v^2,\\
N(a\bar b)
&=(rt-rv+sv)^2-(rt-rv+sv)(st-rv)+(st-rv)^2\\
&=r^2t^2-r^2tv+r^2v^2-rst^2+rstv-rsv^2
  +s^2t^2-s^2tv+s^2v^2\\
&=(r^2-rs+s^2)(t^2-tv+v^2).
\end{aligned}$$

For a complex coefficient pair $C+D\omega$, its scalar representation
is $(x,y)=(C,-D)$ and this norm is exactly $Q(x,y)$. Thus the displayed
expansion verifies the scalar mixed terms as well as (1). $\square$

### Meaning

This changes factors in the complete scalar product. All cross terms
are preserved by the exact multiplicative norm identity. The same
label $S$ can require different actual multipliers at different input
words; it is not a claimed homomorphism from the finite swap group
to scalar norm multipliers.

### Consequence

The scalar composition gate passes. Distinctness, allowed returned
coordinates and the number of represented Cartesian pairs still
require proof. They are supplied, with their losses, for one explicit
factor-word carrier below.

## 2. FS-2 — explicit specialization and finite equality control

### Statement

Fix $\omega=(-1+i\sqrt3)/2$. For every integer $d\ge1$, set

$$B_d=100^{d+1},\qquad t_i=B_d^{5^{i-1}}\quad(1\le i\le d),$$
$$\alpha_i=t_i-\omega,\qquad
q_i=\alpha_i\bar\alpha_i=t_i^2+t_i+1,\qquad
u_i=\bar\alpha_i/\alpha_i.$$

All choices are deterministic functions of $d$; there is no prime
selection or search. Define

$$Z_d=\left\{\prod_i\alpha_i^{a_i}\bar\alpha_i^{b_i}:
a_i,b_i\in\{0,1\}\right\},$$
$$U_d=\left\{\prod_i u_i^{h_i}:h_i\in\{-1,0,1\}\right\}.
\tag{4}$$

Then

$$|Z_d|=4^d,\qquad |U_d|=3^d,\qquad
|N(Z_d)|=3^d.\tag{5}$$

These are actual evaluated sets in $\mathbb Q(\omega)$.
The $U_d$ assertion concerns the displayed finite exponent window;
no all-integer-power independence statement is required or asserted.

### Proof of the specialization bounds

Work first with independent indeterminates $T_1,\ldots,T_d$, and put
$\mathcal A_i=T_i-\omega$, $\mathcal B_i=T_i-\bar\omega
=T_i+1+\omega$, $\mathcal Q_i=T_i^2+T_i+1$.
For a polynomial with coefficients written uniquely as $a+b\omega$
with $a,b\in\mathbb Z$, define its coefficient size $H$ as the sum
of $|a|+|b|$ over all its monomials. Since $\omega^2=-1-\omega$,

$$H(PQ)\le2H(P)H(Q).\tag{6}$$

For completeness, the coefficient product is
$(a+b\omega)(c+e\omega)=(ac-be)+(ae+bc-be)\omega$;
the triangle inequality gives (6), first for coefficients and then
after summing polynomial products.

Each local factor $1,\mathcal A_i,\mathcal B_i,\mathcal Q_i$
has size at most 3. A code polynomial therefore has size at most
$6^d$. A product of at most two linear factors at each site has
local size at most $2\cdot3^2=18$ and total size at most $36^d$.
The norm polynomials $\prod_i\mathcal Q_i^{s_i}$,
$s_i\in\{0,1,2\}$, have nonnegative integer coefficients of total
size at most $9^d$.

Every difference used below consequently has coefficient size at most
$C_d=2\cdot36^d$ and degree at most 4 in each $T_i$. Substitute
$T_i=T^{5^{i-1}}$. Distinct monomials remain distinct: their exponent
vectors have entries $0,1,\ldots,4$, the unique base-five digits of
the resulting exponent. Thus a nonzero component polynomial remains
a nonzero integer polynomial, with coefficients of magnitude at most
$C_d$.

Finally, a nonzero integer polynomial $f$ of degree $k$ whose
coefficients have magnitude at most $C_d$ cannot vanish at
$B_d>C_d+1$. Its highest term has magnitude at least $B_d^k$, while
all lower terms have sum at most

$$C_d\frac{B_d^k-1}{B_d-1}<B_d^k.$$

The inequality $100^{d+1}>2\cdot36^d+1$ holds for every $d\ge1$.
Choose either nonzero integer component in the basis $1,\omega$
when the polynomial coefficients lie in $\mathbb Z[\omega]$.
This proves faithfulness for exactly these bounded differences.
No general algebra embedding into the real numbers is claimed.

### Proof of the counts

Write the code polynomial as

$$P_{\mathbf a,\mathbf b}
=\prod_i\mathcal A_i^{a_i}\mathcal B_i^{b_i}
=\mathcal X_{\mathbf a,\mathbf b}-\omega
\mathcal Y_{\mathbf a,\mathbf b},$$

with integer component polynomials. Put $s_i=a_i+b_i$. Its top
monomial is $\prod_iT_i^{s_i}$, with coefficient 1. This is also
the leading monomial of $\mathcal X$ in lexicographic order.
Hence different vectors $\mathbf s$ have different $\mathcal X$.
For fixed $\mathbf s$, when $s_i=1$ the coefficient of the monomial
$T_i^{s_i-1}\prod_{j\ne i}T_j^{s_j}$ in $\mathcal X$ is

$$0\quad\text{if }(a_i,b_i)=(1,0),\qquad
1\quad\text{if }(a_i,b_i)=(0,1).\tag{7}$$

Indeed, the relevant local constants are $-\omega$ and $1+\omega$,
and every other factor contributes its leading coefficient 1.
Sites with $s_i=0$ or 2 have only one possible word. Thus
$\mathcal X$ distinguishes all $4^d$ words. The proved
specialization bound preserves these differences, so even the first
evaluated coefficient is injective. In particular $|Z_d|=4^d$.

The norm polynomial is $\prod_i\mathcal Q_i^{s_i}$. Its leading
multidegree is $2\mathbf s$, so different $\mathbf s$ give different
polynomials and, by the same bound, different scalar norm values.
Every vector in $\{0,1,2\}^d$ occurs, proving $|N(Z_d)|=3^d$.

To count actions, for $\mathbf h\in\{-1,0,1\}^d$ write its formal
ratio as $N_{\mathbf h}/D_{\mathbf h}$, where

$$N_{\mathbf h}=\prod_i\mathcal B_i^{h_i^+}
\mathcal A_i^{h_i^-},\qquad
D_{\mathbf h}=\prod_i\mathcal A_i^{h_i^+}
\mathcal B_i^{h_i^-},$$

and $h_i^+=\max(h_i,0)$, $h_i^-=\max(-h_i,0)$. Ratios with different
$\mathbf h$ are distinct as rational functions. At $T_i=\omega$,
the zero/pole order of $N_{\mathbf h}/D_{\mathbf h}$ is $-h_i$:
$\mathcal A_i$ has a simple zero and $\mathcal B_i$ is nonzero.
All factors from other variables are nonzero elements of their
coefficient field. This elementary one-variable order test requires
no factorization theorem about the evaluated integers.

Therefore $N_{\mathbf h}D_{\mathbf h'}-
N_{\mathbf h'}D_{\mathbf h}$ is nonzero for distinct words. Each
site contributes at most two linear factors, so the preceding
$2\cdot36^d$ size bound and degree bound apply. Its evaluated
difference is nonzero and the denominators are nonzero. Thus the
$3^d$ evaluated actions are all distinct, proving (5). $\square$

### Meaning

Neither formal action labels nor assumed prime independence are counted
as actual actions. The separated integer evaluation pays explicitly
for every equality used in the code and finite action window.

### Consequence

The code has many distinct norm-preserving actions and many different
norm levels. Its geometry cannot be assessed by treating it as one
fixed-norm orbit. The required Cartesian count is made in §5.

## 3. Exact factor-switch return domains

### Statement

For $z=z_{\mathbf a,\mathbf b}$ put

$$k(z)=\#\{i:a_i+b_i=1\}.$$

The number of distinct returns **into $Z_d$** under $U_d$ is exactly

$$R_Z(z):=|\{uz\in Z_d:u\in U_d\}|=2^{k(z)}.\tag{8}$$

For $\mathbf h\in\{-1,0,1\}^d$, its exact encoded return domain is

$$u_{\mathbf h}z_{\mathbf a,\mathbf b}\in Z_d
\quad\Longleftrightarrow\quad
\begin{cases}
(a_i,b_i)=(1,0)&h_i=1,\\
(a_i,b_i)=(0,1)&h_i=-1,
\end{cases}\tag{9}$$

with no restriction at $h_i=0$. In particular, its domain contains
$4^{d-|\operatorname{supp}\mathbf h|}$ encoded pairs.

**Proof.** Norm preservation and the proved norm injectivity force any
target word to have the same vector $\mathbf s=\mathbf a+\mathbf b$.
There are exactly two choices at each singly occupied site, and only
one at every other site. All $2^{k(z)}$ choices are achieved by FS-1.
They are distinct codewords and hence distinct returned pairs.

The ratio to a target $(\mathbf a',\mathbf b')$ on this same norm
level is the element of $U_d$ with exponent
$h_i=a_i-a_i'=b_i'-b_i$. The finite-window action injectivity makes
this the only exponent label for that ratio. The allowed bits give
exactly (9). Every word is nonzero, so different actual multipliers
also act distinctly at each source. $\square$

### Meaning

The domains depend on the factorization of the whole scalar pair.
The norm identity is exact before and after scalar evaluation. The
return product in (8) is therefore genuine on the encoded factor
carrier, with no additive cross-term assumption.

### Consequence

There is a real gain at the composition gate. Equation (8) counts
targets inside $Z_d$, not all targets in the eventual scalar square.
It is a lower bound for those larger return counts at encoded sources;
it says nothing about unencoded sources without another proof.

## 4. The complete encoded return distribution

### Statement

For $0\le k\le d$,

$$\#\{z\in Z_d:R_Z(z)=2^k\}=2^d\binom dk.\tag{10}$$

Thus the minimum is 1, maximum is $2^d$, one-return fraction is
$2^{-d}$, arithmetic mean is $(3/2)^d$, and geometric mean is
$2^{d/2}$. The distribution of $\log_2R_Z$ is exactly the symmetric
binomial distribution with $d$ coordinates; its central value is
$d/2$ (the two central integers when $d$ is odd).

An elementary exponential lower-tail estimate is

$$\#\{z:R_Z(z)<2^{d/4}\}
\le3^d2^{d/4}=4^d\left(\frac{3\,2^{1/4}}4\right)^d,
\qquad \frac{3\,2^{1/4}}4<1.\tag{11}$$

**Proof.** Choose the $k$ singly occupied sites, choose their two
orientations, and choose empty or doubly occupied at every other site.
This gives $\binom dk2^k2^{d-k}=2^d\binom dk$.
Summing (10) gives the mean and geometric mean. For the tail, a word
with $k<d/4$ has $2^{-k}>2^{-d/4}$, while

$$\sum_{z\in Z_d}2^{-k(z)}
=2^d(1+1/2)^d=3^d.$$

This proves (11). Its strict base inequality follows by fourth powers:
$3^4\cdot2=162<256=4^4$. No external probabilistic estimate is used.
$\square$

### Meaning

Most encoded factor words have exponentially many genuine returns.
The statement is pointwise outside an explicitly counted encoded
tail, rather than only a large average.

### Consequence

This tail is on $4^d$ factor words. It cannot be substituted for a
tail on the full Cartesian square, whose size is squared after
coefficient completion.

## 5. FS-3 — common scalar completion has sparse encoded coverage

### Statement

Write every $z\in Z_d$ uniquely as $z=x_z-\omega y_z$, with
$x_z,y_z\in\mathbb Z$. Define

$$A_d=\{x_z:z\in Z_d\}\cup\{y_z:z\in Z_d\},
\qquad X_d=Y_d=A_d,\qquad n_d=|A_d|,$$
$$\Gamma_d=\{(x_z,y_z):z\in Z_d\}\subseteq A_d^2.$$

Then

$$|X_d\triangle Y_d|=0,\qquad
4^d\le n_d\le2\cdot4^d,\qquad |\Gamma_d|=4^d,\tag{12}$$
$$\boxed{\frac{|\Gamma_d|}{n_d^2}\le4^{-d},\qquad
|A_d^2\setminus\Gamma_d|=n_d^2-4^d=n_d^2(1-o(1)).}\tag{13}$$

The valid full-support certificate obtained from these norm levels is

$$|Q(A_d,A_d)|\le n_d^2-4^d+3^d.\tag{14}$$

It has output exponent $2\log4$ and zero asymptotic saving relative
to the input rate $\log4$. It is an **upper certificate**, not an
actual-image asymptotic or a lower bound on actual low-return pairs.

**Proof.** Equation (7) and the specialization proof make $z\mapsto x_z$
injective, giving $4^d$ different scalar inputs already in the first
coordinate. The union has at most twice that many. Complex coefficient
uniqueness gives the exact count of $\Gamma_d$. These prove (12)–(13).
The encoded pairs have exactly $3^d$ norm values by (5), and each
remaining ordered pair adds at most one value. This proves (14).
$\square$

### Meaning

The first coefficient remembers the entire factor word. Hence the
encoded pairs form a graph with one point per first-coordinate value,
even though their norm fibers inside that graph can be large. Forcing
$X=Y$ by common coefficient completion does not create new encoded
factorizations for the missing cross-pairs.

### Consequence

Even granting every point of $\Gamma_d$ arbitrarily many genuine
returns leaves a quadratic certificate bad set. The actual set
$\{p\in A_d^2:R_{U_d}^{\rm pair}(p)<n_d^\varepsilon\}$ is
**not** determined by (13). Additional returns or factorizations on
the unencoded pairs remain unproved, rather than impossible.

One may take any positive overlap exponent $\eta$ because $X_d=Y_d$.
Equation (11) gives at least $n_d^\varepsilon$ genuine returns on
most encoded pairs for every strict $0<\varepsilon<1/8$ eventually,
using $n_d\le2\cdot4^d$. But the encoded-coverage certificate has
no positive exceptional exponent $\delta$. Therefore DC-R1 supplies
no fixed $c>0$ from this mechanism as implemented here.

## 6. Full construction and rate ledger

The carrier above is the only family analyzed in this subtask. Depth
$d$ grows; the alphabets, exponents and base recipe are fixed first.
Let $Q_d=\prod_iq_i$ (this is an auxiliary integer, not the target
polynomial). Since $u_i=\bar\alpha_i^2/q_i$, every action matrix in
$U_d$ has common denominator dividing $Q_d$. There is no assumption
that the $q_i$ are primes or pairwise coprime.

Every factor word has $|z|\le Q_d$, so the positive-definite formula
for $Q$ gives $|x_z|,|y_z|\le2Q_d/\sqrt3$. The all-doubly-occupied
word is the real integer $Q_d$, hence $\max|A_d|\ge Q_d$. Moreover
$t_i^2\le q_i\le4t_i^2$, so

$$\log Q_d=2\sum_i\log t_i+O(d)
=\frac{5^d-1}{2}\log B_d+O(d)=\Theta(d5^d).\tag{15}$$

These heights are explicitly paid; no polynomial-height or ambient
volume support estimate is used.

| Required gain or cost | Exact accounting / status |
|---|---|
| Fixed polynomial and exact projection | $Q(x,y)=N(x-\omega y)$; integral coefficient pairs in one fixed complex embedding |
| Input lower and upper counts | $4^d\le n_d\le2\cdot4^d$; $\log n_d=d\log4+O(1)$ |
| Both-coordinate thinning | None. Restricting the support argument to $\Gamma_d$ does not thin the required scalar square; all $n_d^2-4^d$ omitted pairs are charged |
| Parameter and coordinate fibers | Factor labels injective; first coordinate injective by (7); no unproved bound on the second-coordinate fibers is used |
| Same-set comparison | $X_d=Y_d=A_d$ exactly; any fixed positive $\eta$ is allowed |
| Actual action inventory | $3^d$ distinct finite-window multipliers, proved by bounded specialization; no all-power independence assumption |
| Global scalar composition | Exact partial conjugation (1)–(3), preserving all scalar cross terms |
| Distinct returned pairs | Exactly $2^{k(z)}$ within $\Gamma_d$, because sources are nonzero and the factor words are distinct |
| Zero and stabilizers | $0\in A_d$ from the real codeword $1$, but no encoded $z$ is zero. The unencoded origin has one distinct target and is charged with the complement |
| Branches and factor assignments | Four states per site; duplicates from switching empty or doubly occupied sites removed, leaving $2^{k(z)}$ actual targets |
| Norm/support counts | Exactly $3^d$ values on encoded pairs; no such bound asserted for the entire square |
| Encoded return tail | Complete histogram (10), and encoded bad fraction at most $(3\,2^{1/4}/4)^d$ at threshold $2^{d/4}$ |
| Actual full return tail | OPEN; not inferred from the encoded histogram |
| Coverage exceptions | $B_{\rm cert}\ge n_d^2-4^d=n_d^2(1-o(1))$, even with optimistic returns on all encoded pairs |
| Field degree / discriminant | Inputs rational integers; multiplier field $\mathbb Q(\omega)$, fixed degree 2 and discriminant $-3$ |
| Regulator, units and local splitting | No such estimates used. Multipliers are fractional norm-one elements; no free growing supply of integral units is asserted |
| Denominators and coefficient heights | Every denominator divides the declared common denominator $Q_d$; $\log Q_d$ and the logarithm of the maximum scalar magnitude are $\Theta(d5^d)$, by (15). No lower bound for each reduced denominator is asserted |
| Carries and arithmetic distinctness | Degree-at-most-four base-five monomial encoding, coefficient cap $2\cdot36^d$, and $B_d>2\cdot36^d+1$ proved explicitly |
| Local residue population and moduli | Inapplicable: no local sieve, CRT or residue-density saving is used |
| Archimedean distortion | Partial conjugation is an exact norm isometry at each source; coefficient magnitude bounded above as stated |
| Final signed rates | Input $a=B=\log4$; certificate output rate $2\log4$ from (14), net $2a-c+s=0$ |
| Fixed saving | No positive $c$ certified; the full Cartesian image rate remains OPEN in this note |

## 7. Disposition and precise limit

**Scalar composition: PROVED. Encoded return tail: PROVED.
Almost-full Cartesian coverage: FAILED for this separated direct
coefficient certificate.** This is not a universal obstruction to
factor switching, global rephasing, other specializations or correlated
factor assignments with genuine coordinate reuse. It is not an
actual-image lower bound for the explicit $A_d$.

No finite scout is needed for these exact all-depth statements, and
none was run by this subtask. Independent review and any repository
validation are recorded by the lead; no program validation is implied
by this symbolic proof. The sole active obligation remains correlated
DC-O1: a scalar-compatible return construction covering almost every
pair with positive return and exceptional exponents. No additional
carrier family is started here.
