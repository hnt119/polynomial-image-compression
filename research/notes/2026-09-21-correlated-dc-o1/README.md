# Bottom line

- **Mechanisms tested:** global factor conjugation, pair-indexed linear-level reflections, and CRT cube-root divisibility domains. These are three mechanisms; only the third required an exact finite scout.
- **Scalar cross terms: PROVED preserved.** Conjugating a factor of the whole scalar product preserves its norm; the reflection identity uses the whole pair.
- **Coordinate overlap: PROVED.** All concrete realizations use $X=Y$, so $|X\triangle Y|=0$.
- **Almost-full polynomial return tail: FAILED in the proved scopes.** Most decisively, the explicit CRT family has at least $n^2/48$ actual identity-only pairs at every depth. The other two failures concern their specified certificates, not all possible returns.
- **DC-R1 supplies no $c>0$ this cycle.** DC-O1, the quadratic target, ARG/TCRC and RC15/4 remain OPEN; HR-N1 remains DISPROVED.
- **One next obligation:** construct the still-missing correlated DC-O1 witness with genuine returns on almost every pair. The exact obligation is at the end.

## CORRELATED GO / TAIL FAIL

$$\boxed{\text{global correlation}
\xrightarrow{\mathrm{PROVED}}\text{scalar-compatible returns}
\xrightarrow[\text{specified constructions/certificates}]{\mathrm{FAILED}}
\text{almost-full return tail}
\xrightarrow[\text{DC-R1 implication}]{\mathrm{PROVED}}\text{power saving}.}$$

The general middle construction step remains **OPEN**. The final arrow is
an existing implication whose hypotheses have not been achieved.

**Correlated DC-O1 research report · 21 September 2026 · T03.**
Strictly offline; no outside theorem import, literature search, or novelty
claim. The prior [DC-O1 checkpoint](../2026-09-21-dc-o1/README.md)
remains frozen. No independent additive tensor, balanced-state, moving-pole
variant, or HR-N1 repair was attempted. No new global compression theorem
was sought. Proofs, exact definitions and full arithmetic ledgers are in
the three linked companions; audit and execution details are in
[verification.md](verification.md).

## 1. Exact scalar action and the distinction being tested

Write $\omega=(-1+i\sqrt3)/2$, $z=x-\omega y$, so $Q(x,y)=z\bar z$.
For $u=a+b\omega$ of norm one,

$$M_u(x,y)=(ax+by,-bx+(a-b)y),\qquad
D_u=(X\times Y)\cap M_u^{-1}(X\times Y).$$

Count distinct genuine returned pairs

$$R(p)=|\{M_up\in X\times Y:u\in U\}|,\qquad
B_\varepsilon=|\{p\in X\times Y:R(p)<n^\varepsilon\}|.$$

At nonzero $p$, distinct multipliers give distinct targets. At zero there
is only one target. Every finite scout below uses the actual oriented
rectangle, here $X=Y=A$.

The old additive composition had cross terms

$$N\left(\sum_i\theta_i z_i\right)
=\sum_i\theta_i^2N(z_i)+2\sum_{i<j}\theta_i\theta_j
\operatorname{Re}(z_i\bar z_j).$$

Replacing $z_i$ by $u_i z_i$ inserts $u_i\bar u_j$ into each mixed
term. The previous synchronization theorem is accepted without rerunning
it. The present mechanisms instead act on a **whole product** or the
**whole scalar pair**, with identities proved before scouting.

## 2. Global factor words — true returns, sparse Cartesian coverage

### Statement

**PROVED — FS-1–FS-3.** Set $B=100^{d+1}$,
$t_i=B^{5^{i-1}}$, $\alpha_i=t_i-\omega$, and

$$Z_d=\{\prod_i\alpha_i^{a_i}\bar\alpha_i^{b_i}:a_i,b_i\in\{0,1\}\},
\quad U_d=\{\prod_i(\bar\alpha_i/\alpha_i)^{h_i}:h_i\in\{-1,0,1\}\}.$$

For $z=vw$, the global switch $z'=v\bar w$ satisfies
$z'=(\bar w/w)z$ and $N(z')=N(z)$. Switching selected occupied factors
composes by symmetric difference of the selected indices, with the
multiplier depending on the current whole word. After exact scalar
specialization,

$$|Z_d|=4^d,\quad |U_d|=3^d,\quad |N(Z_d)|=3^d,\quad R_Z(z)=2^{k(z)},$$

where $k(z)$ counts singly occupied factors. The exact histogram is
$\#\{R_Z=2^k\}=2^d\binom dk$, and the encoded bad fraction below
$2^{d/4}$ is at most $(3\,2^{1/4}/4)^d$.

However, if $A_d$ is the union of the two coefficient projections of
$Z_d$ and $X_d=Y_d=A_d$, then

$$4^d\le n_d\le2\cdot4^d,\qquad
|\Gamma_d|=4^d,\qquad |\Gamma_d|/n_d^2\le4^{-d},$$

where $\Gamma_d$ is the encoded pair set. The first coefficient already
remembers every word. Proof and height costs:
[factor-switching.md](factor-switching.md).

### Meaning

This varying-norm factor code has genuine exponentially many returns on
most of its encoded pairs. Its same-set completion is much larger than
those encoded pairs: almost every cross-pair lacks the proved factor-word
representation.

### Consequence

**FAILED encoded-coverage certificate.** Even granting all encoded points
arbitrarily many returns leaves $n_d^2-4^d$ uncertified pairs. The resulting
full-support bound $n_d^2-4^d+3^d$ has no fixed exponent saving. The actual
full-square return tail and image rate are OPEN; no actual bad-pair lower
bound is inferred from a missing representation.

## 3. Linear-level reflections — exact identity, bounded level capacity

### Statement

**PROVED — CR-L1–CR-L4.** For nonzero
$H(x,y)=\alpha x+\beta y$, put

$$D=\alpha^2-\alpha\beta+\beta^2,\quad
J=(2\beta-\alpha)x-(2\alpha-\beta)y.$$

Then

$$4D Q=3H^2+J^2,\qquad
S_H(p)=\frac{H(p)}D(2\alpha-\beta,2\beta-\alpha)-p$$

preserves $Q$ and $H$. At $p\ne0$ its genuine multiplier is
$u(p)=z_{S_Hp}/z_p$; it depends on the whole pair.
A norm fiber has at most two points on any fixed $H$-level, so a
certificate allowing at most $k$ target levels per source supplies at
most $2k$ targets. Moreover a nonsymmetric affine map between two fixed
parallel levels preserves $Q$ at at most two source points. A library
of $K$ such nonsymmetric rules therefore obeys

$$\#\{p:r_{\rm cert}(p)\ge R\}\le\frac{2K}{R-4}\quad(R>4).$$

The symmetric maps are $p,S_Hp,-p,-S_Hp$. For $H=x+y$ and a symmetric
integer interval they all return and give at most four targets.
Full proofs: [level-reflections.md](level-reflections.md).

### Meaning

A large sum or difference level need not contain many equal-norm points.
Subpolynomially many permitted target levels cannot supply polynomially
many returns through this certificate. General affine rules also pay an
explicit source-incidence cost.

### Consequence

**FAILED bounded-level / small affine-library certificates.** Taking all
pair-indexed ratios into a global $U$ could create extra cross-level
returns. The bounds above do not exclude those incidental returns; no
full-action or actual-image lower bound is asserted. Many nonlinear
branches or changing reflection directions remain outside the theorem.

## 4. CRT cube roots — a positive-density actual-return obstruction

### Statement

**PROVED — CD-1–CD-3.** Let $p_1<\cdots<p_d$ be the first primes
congruent to one modulo three, $P=\prod p_i$, and choose
$\alpha_i\in\mathbb Z[\omega]$ with $N\alpha_i=p_i$. Define

$$A_d=X_d=Y_d=\{x\in\mathbb Z:|x|\le(P-1)/2,
\quad x^3\equiv1\pmod{p_i}\text{ for all }i\},$$
$$U_d=\{\prod_i(\bar\alpha_i/\alpha_i)^{e_i}:e_i\in\{-1,0,1\}\}.$$

Then $n_d=|A_d|=3^d=|U_d|$, and all sources are nonzero. For a source,
let $J=\{i:x=y\pmod{p_i}\}$ and $W=\prod_{i\in J}p_i$. The exact
identity-only criterion is

$$\boxed{W^3>4P/3\quad\Longrightarrow\quad R_d(x,y)=1.}$$

At least $n_d^2/48$ ordered pairs satisfy this criterion for every
$d\ge1$. Therefore, for every fixed $\varepsilon>0$,

$$\boxed{B_\varepsilon(d)\ge n_d^2/48.}$$

This excludes $B_\varepsilon\le C'n_d^{2-\delta}$ for every fixed
$\delta>0$ and finite $C'$, eventually as $d\to\infty$.

### Meaning

There are exactly $2^{d-|J|}$ **integral** factor-conjugation candidates
per pair. Returning to the common scalar residue set is a stronger
condition. At each diagonal residue prime, an actual return must fix
the original residue pair, imposing simultaneous constraints on the
whole multiplier.

### Consequence

**FAILED actual return-tail witness for this carrier and width-one action
box.** This is stronger than a certificate-coverage failure: the stated
positive-density pairs really have only the identity return under every
selected action. It is not an all-integer-power theorem, an actual-image
lower bound, or a disproof of DC-O1.

The proof is short in outline. Write $u=\bar\beta/\beta$,
$\beta=a+b\omega$, $N\beta=D$. Integrality forces all selected factors
to divide $z$. At primes in $J$ this forces the exponent to vanish;
return membership then forces $u=1$ modulo those primes. Consequently

$$W\mid b,\qquad \frac34b^2\le D\le P/W.$$

The displayed criterion gives $b=0$ and hence the identity. Under the
uniform distribution on $A_d^2$, the indicators of $J$ are independent
Bernoulli variables of parameter $1/3$. A complete second/fourth-moment
argument gives probability at least $1/48$ that
$\log W>(\log P+\log(4/3))/3$. The proof, constants, elementary supply
of split primes and all integrality details are in
[crt-domains.md](crt-domains.md); no prime-distribution theorem is used.

## 5. Exact finite scout

**EXPERIMENTAL — exhaustive and exact.** Only the CRT mechanism was
scouted, at the four predetermined depths. Its scalar composition proof
preceded execution. All pairs, all actual actions, integrality and the
full image were checked. The finite threshold is $n^{1/4}$; thus
$B_{1/4}$ counts sources strictly below that real threshold.
Geometric means below are rounded presentation values.

| $n$ | $\lvert X\triangle Y\rvert$ | $\lvert U\rvert$ | Median $R$ | Geometric mean $R$ | Maximum $R$ | $B_{1/4}$ | Full $\lvert Q(A,A)\rvert$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 0 | 3 | 1 | 1.000000 | 1 | 9 | 4 |
| 9 | 0 | 9 | 1 | 1.108146 | 2 | 69 | 33 |
| 27 | 0 | 27 | 1 | 1.009554 | 2 | 729 | 320 |
| 81 | 0 | 81 | 1 | 1.004447 | 2 | 6561 | 2956 |

Complete return, integral-candidate, stabilizer and image-fiber histograms
and all individual domain sizes are stored separately in the
[frozen JSON](../../../examples/2026-09-21-correlated-dc-o1.json).
The raw local record retains every action and returned pair. The symbolic
factor-word and level results were rejected at their exact coverage gates;
no unnecessary finite rerun was performed for them. Their analytically
proved distributions are in their companions, not presented as experiments.

## 6. Signed rates and arithmetic audit

| Mechanism | Input and overlap | Proved return gain | Full-pair cost / final deficit |
|---|---|---|---|
| Factor words | $\log n=d\log4+O(1)$; $X=Y$ | $2^{d/4}$ outside an exponential encoded tail | Only $4^d$ of $n^2$ pairs encoded; certificate output rate $2\log4$, gap zero |
| Linear levels | Concrete $n=2N+1$; $X=Y$ | At most $2k$ targets in $k$ levels; four in the concrete certificate | $k=n^{o(1)}$ gives return rate zero; rich affine-library cost $K\gtrsim Rn^2$ |
| CRT cube roots | $n=3^d$ exactly; $X=Y$ | $2^{d-\lvert J\rvert}$ integral candidates, which are not all returns | Actual $B_\varepsilon\ge n^2/48$; no fixed positive exceptional exponent |

All rational constructions use the fixed field $\mathbb Q(\omega)$ of
degree two and discriminant $-3$. No regulator, class-number, or lattice
volume estimate is used. Factor-word denominator heights have logarithm
$\Theta(d5^d)$ and are paid explicitly. Reflection ratios have denominators
dividing their source norm. CRT action denominators divide $P$; scalar
height is at most $(P-1)/2$, with no assumption that $P$ is polynomial in
$n$. CRT restriction thins **each** integer coordinate from $P$ points to
$3^d$, so the two-input population cost is $(3^d/P)^2$.

All coefficient and action multiplicities are proved or explicitly
retained as unknown. Zero is absent in the CRT carrier; in the other
common scalar sets it has one target. All missing Cartesian pairs and
all level restrictions are charged. None of the three ledgers supplies
the three positive exponents required by DC-R1.

## 7. Failure registry and retained frontier

| ID | Status | Exact scope |
|---|---|---|
| FS-3 | FAILED certificate | Separated varying-norm factor code with injective first projection; encoded pairs are at most a $4^{-d}$ fraction |
| CR-L2/L3 | FAILED certificates | Subpolynomial target-level lists; affine level-rule libraries below the proved incidence cost |
| CD-3 | FAILED witness | CRT cube-root scalar set and specified width-one factor actions have at least $n^2/48$ identity-only pairs |
| Correlated DC-O1 | OPEN | No almost-full polynomial return tail constructed |
| T03 quadratic target; ARG/TCRC; RC15/4 | OPEN, unchanged | None is disproved by these scoped obstructions |
| HR-N1 | FAILED / DISPROVED, unchanged | Its prior proof and scope remain frozen |

The first two rows must not be cited as actual bad-pair lower bounds for
all actions. The third row must not be cited for arbitrary integer
powers, other residue carriers, or the full polynomial image. No proposed
replacement conjecture or adaptive RC15/4 search is adopted here.

## 8. One next mathematical obligation

**OPEN — correlated DC-O1 witness.** Construct explicit $X_d,Y_d,U_d$
with $n_d=|X_d\cup Y_d|\to\infty$, a proved whole-scalar norm identity,
$|X_d\triangle Y_d|=O(n_d^{1-\eta})$, and at least $n_d^\varepsilon$
distinct genuine returns into $X_d\times Y_d$ outside
$O(n_d^{2-\delta})$ pairs, for fixed $\varepsilon,\eta,\delta>0$.
The already proved DC-R1 then gives every strict
$c<\min(\varepsilon,2\eta,\delta)$. This is one obligation; independent
tensor rotations, balanced states, moving-pole variants and broad carrier
searches remain frozen.
