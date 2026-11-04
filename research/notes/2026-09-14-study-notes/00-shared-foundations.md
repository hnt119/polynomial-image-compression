# Shared foundations: what the source constructions contribute

[Study index](README.md) · [Source identities](SOURCES.md)

**Version: 2026-09-14; research cutoff: 2026-09-10.** This is an explanation of
supplied results, with no independent proof audit. In this note, $\mathcal P$
denotes an additive carrier, leaving $P$ for a polynomial.

## SN-S1 — Two achievements with different counting goals

**EXTERNAL RESULT, supplied statement and relevant arguments inspected.** The
supplied OpenAI manuscript *Planar Point Sets with Many Unit Distances* states
that a fixed $\delta>0$ and infinitely many $n$ admit an $n$-point planar set
with at least $n^{1+\delta}$ unordered unit-distance pairs. Its proof counts
selected pairs whose difference is a norm-one translation. It does not claim
that every pair has one of a small number of distances.
Source: **S-UD**, Theorem 1.1, Proposition 2.2, Theorem 2.3 and Lemmas 2.4–2.6.

**EXTERNAL RESULT, reported through the inspected frozen reconstruction.**
Phase A attributes to Bloom–Sawin–Schildkraut–Zhelezov a construction of
arbitrarily large finite real sets with, for fixed $c>0$,

$$\max\{|A+A|,|AA|\}\le |A|^{2-c}.$$

Here the entire sumset and product set are bounded. The primary paper is not in
the recovered bundle used here; its bibliographic identity is recorded as
given by Phase A, without new retrieval. Sources: **S-A**, §§1, 11–13;
**S-A-LOG**.

**Interpretation.** The polynomial project asks for another full-support
statement: all $|A|^2$ ordered pairs must land in at most $|A|^{2-c_P}$ values
of one fixed $P$. Neither many selected edges nor separately small sum and
product sets automatically supplies the required mixed-polynomial bound.

## SN-S2 — Why number fields help

**EXTERNAL RESULT / explanatory unpacking of S-UD and S-A.** A totally real
number field $K$ of degree $d$ has $d$ real embeddings $\sigma_i$. Its algebraic
integers become a lattice in $\mathbb R^d$ under
$\alpha\mapsto(\sigma_1(\alpha),\ldots,\sigma_d(\alpha))$.
The discriminant $\Delta_K$ measures its density: the lattice covolume is
$\sqrt{\Delta_K}$. A bounded root discriminant means
$\Delta_K\le D_0^d$ for a fixed $D_0$, so this density loss is exponential in
degree and can be compared with an exponential gain.

For a nonzero algebraic integer $z$, the product of its conjugates is a nonzero
integer. Thus not all $|\sigma_i(z)|$ can be below one. This gives separation
for lattice packing. One real embedding is injective and preserves polynomial
evaluation exactly; projection to $\mathbb R$ loses no cardinality.
Source: **S-A**, §§3–4; **S-C0**, Lemmas 5.2–5.3 and §6.

**EXTERNAL RESULT, supplied arithmetic theorem inspected.** The unit-distance
paper supplies totally real unramified tower layers $F_j$ of growing degree,
constant root discriminant, and fixed rational primes $q_b\equiv1\pmod4$
splitting completely in every layer. Its construction first fixes a sufficiently
large $\ell$, giving $t=\lfloor(\ell-1)^2/100\rfloor$ such primes and
$\log\operatorname{rd}(F_j)=O(\ell\log\ell)$, then lets the layer grow.
The associated CM fields $F_j(i)$ are complex and have a different role.
Source: **S-UD**, Proposition 3.8(P1)–(P6), Remark 3.9.

The paper's norm-one translations arise from binary choices of conjugate
prime ideals. Selecting a common ideal class converts enough choices into
actual elements, with a class-number loss and fixed denominator. Their
absolute values are one at every complex embedding. Window averaging then
retains many translation edges. Source: **S-UD**, Proposition 2.2 and §2.1.

## SN-S3 — The sum-product mechanism, step by step

**EXTERNAL RESULT, reconstruction inspected; no new primary-source audit.**
In a totally real field, define

$$B^+(T)=\{b\in\mathcal O_K:|\sigma_i(b)|\le T\text{ for all }i\},$$
$$\mathcal P=X+B^+(\varepsilon X),\qquad
G=\{g\in\mathcal O_K^\times:|\log|\sigma_i(g)||\le Y\text{ for all }i\}.$$

Choose a fixed sufficiently small $\varepsilon>0$ and the source's sufficiently
large fixed $Y,X$, with $X$ integral. The construction is $A=G\mathcal P$.

The additive carrier occupies a short positive window around $X$ in every
embedding. If $g_1p_1=g_2p_2$, then the unit $g_1/g_2=p_2/p_1$ is uniformly
close to one in all embeddings. The source's unit-separation lemma forces it
to be one. Consequently $|A|=|G||\mathcal P|$.

Logarithms turn unit multiplication into addition. Hence $GG$ lies in a log
box of radius $2Y$, and the full product count satisfies

$$AA=(GG)(\mathcal P\mathcal P),\qquad
\frac{|AA|}{|A|^2}\le\frac{|GG|}{|G|^2}.$$

The same units have $|\sigma_i(g)|\le e^Y$. Every sum in $A+A$ therefore lies
in one ordinary box of radius $4Xe^Y$. These two different mechanisms control
the two full supports.

The frozen report gives, for disposable absolute $c_0>0$,

$$\frac{(c_0XY)^d}{Y\Delta_K^{3/2}}\le|A|\le(XY/c_0)^d,$$
$$\frac{|AA|}{|A|^2}\le c_0^{-d}Y^{1-d}\Delta_K^2,
\qquad |A+A|\le(e^Y/c_0)^d\Delta_K^{1/2}|A|.$$

Fix $D_0$, choose $Y$ to buy product saving, choose $X$ to pay the additive
distortion, then grow $d$. The regulator controls the density of the unit
lattice and is paid through the report's bound $R_K\le\Delta_K$ for totally
real $d\ge2$.

Sources: **S-A**, §§3–8, 10–12; **S-A-LOG**, corrections 1–8.

**Interpretation.** The final sum-product construction uses the unit lattice
directly. It does not reuse the unit-distance proof's split-prime, ideal-class,
fixed-denominator construction. The shared feature is a favorable comparison
of exponential gains and costs, not an identity of the two constructions.

## SN-S4 — What Phase B extracted

**PROVED, reported abstraction.** Write
$r_P(z)=|\{(a,b)\in A^2:P(a,b)=z\}|$ and
$E_P(A)=\sum_zr_P(z)^2$. Cauchy–Schwarz gives

$$|P(A,A)|\ge |A|^4/E_P(A).$$

A large energy lowers this lower bound; it does not upper-bound the image.
Phase B therefore requires a complete output container, a factorization
through a small support, or coverage of almost every pair with a charged tail.
Source: **S-B**, Validated abstraction principles 1–3; **S-MASTER**, §5.

**PROVED, reported local-to-global rule.** Complete splitting gives
$\mathcal O_K/p\mathcal O_K\cong\mathbb F_p^d$. A scalar residue restriction
of density $q_p$ becomes a restriction of density $q_p^d$. To turn that into
a global upper bound, count permitted classes and multiply by a **uniform
worst-case bound within each class**. Multiplying density by a total box count
without this step is unjustified.

If input rates are $e^{ad-o(d)}\le|A_d|\le e^{Bd+o(d)}$ and the full output
rate is at most $e^{(c-s)d+o(d)}$, the required margin is

$$\delta=2a-c+s>0.$$

Every fixed exponent below $\delta/B$ is then certified after absorbing errors.
An input loss of $e^{-\eta d}$ costs $2\eta$ in this comparison because both
inputs are restricted. Source: **S-B**, Validated abstraction principles 4–6; **S-MASTER**, §6;
**S-REG**, mechanism library. This is a gate for a proved construction, not
evidence that its premises hold.

## SN-S5 — The shared positive result: corrected C0

**PROVED within the supplied source system; argument inspected.** For fixed
integral $a,b,c,e$ with $\gcd(a,b)=1$ and $ab(ae-bc)\ne0$,

$$P(x,y)=(ax+by)^2+cx+ey$$

admits arbitrarily large same-input real sets with a fixed positive saving
depending on $P$. Source: **S-C0**, Theorem C0.1, §§5–6; **S-C0-LOG**.

The key calculation is short enough to retain. Let $L=ax+by$, $M=cx+ey$ and
$P_Q=L^2+QM$, so $P_Q(Qx,Qy)=Q^2P(x,y)$. At selected odd primes dividing
fixed $Q$, outputs are squares. Put

$$\rho=\prod_{p\mid Q}\frac{p+1}{2p},\quad
C_P=2((|a|+|b|)^2+|c|+|e|)+1.$$

The source fixes its tower and primes with $\theta=C_PD\rho<1$, then fixes
$X>\max(Q,\sqrt D)$. Its centered carrier $B_j\subset\mathcal O_{F_j}$ obeys

$$ (X/\sqrt D)^{d_j}\le|B_j|\le(2X+1)^{d_j},\qquad
|P_Q(B_j,B_j)|\le\theta^{d_j}|B_j|^2.$$

Taking $A_j=Q^{-1}\sigma_j(B_j)$ gives the fixed target, with exponent
$-\log\theta/\log(2X+1)$. This calculation uses totally real $F_j$, charges
all classes uniformly, and covers every pair. The source has explicit bounds
here; the general asymptotic gate above requires strict exponent loss.

**Scope.** Rank two, degree three, and degree four are separate obligations.
This theorem includes $(x+2y)^2+3x-y$, not T02's quartic. No novelty claim is
made: the master handoff retains a literature-priority caution.

## Recall check

1. What replaces the unit-distance edge count in this project? **A bound on
   the complete polynomial image, including every ordered pair.**
2. Why prove both input bounds? **The lower bound proves growth and pays costs;
   the upper bound converts a degree saving into a power of input size.**
3. Why are norms useful without solving the problem? **They supply exact
   identities and separation, but a common Cartesian carrier and a small
   entire output support still have to be proved.**
