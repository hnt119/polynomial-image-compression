# Finite field and Chebotarev mechanisms for quadratic cubic and fourth power polynomials

11 October 2026 · version 1

The finite-field mechanism gives a fixed power saving when a local output defect survives all arithmetic and archimedean costs before field degree grows. It succeeds for the transverse rank-one quadratic family. The located dense-box cubic certificate and the specified fourth-power certificates fail that quantitative gate. Their failure is not a lower bound for the actual real image. The original norm-one construction supplies many bounded complex directions, but its real trace import still needs an exact all-pairs support theorem.

The report collects the relevant theorem statements, elementary proofs, dependency chains, construction ledgers and source boundaries. Its arithmetic reference is the original OpenAI unit-distance proof. The stronger tower in the human remarks and Pohoata's polynomial theorem are identified separately. The algebraic number-theory theorems remain external inputs; their original statements and use are inspected, rather than independently reproved. The polynomial calculations below are located project arguments and checked elementary consequences. No new candidate, construction search or mathematical experiment is asserted.

Every positive construction concerns one finite scalar set in both coordinates, the entire ordered square, a fixed polynomial and a fixed positive exponent. All constants may depend on the fixed polynomial and the once-chosen arithmetic data, but not on the growing field degree. The local labels A1–A8, G1–G8, Q1–Q5, C1–C9, N1–N5 and F1–F8 are identifiers in this report; they are not invented theorem numbers in the cited papers. Exact provenance, dates or hashes, dependencies and remaining gaps are in the [claim and source ledger](claim-ledger.md).

## Conclusions by polynomial

| Polynomial or family | Relevant theorem or certificate | What is established |
|---|---|---|
| \((ax+by)^2+cx+ey\), integral coefficients, \(\gcd(a,b)=1\), \(ab(ae-bc)\ne0\) | Q1 | **PROVED within the supplied source system:** arbitrarily large same-set real witnesses and a fixed power saving |
| \((x-y)^2+x+y\) | Q2 | **PROVED:** the explicit base \(13D\rho<1\) and exact scaling; matches Pohoata's external theorem |
| \(x^2+xy+y^2\) | Q3–Q4 | **PROVED local results:** full good-prime field image and exact prime-power norm support; no real compression theorem from these alone; T03 **OPEN** |
| T01: \((x-y)^3+x+y\) | C1–C9 | **PROVED local counts and scoped certificate obstructions:** full cube-class/rectangular packing and positive-volume continuous-cover routes fail; T01 **OPEN** |
| T01 on traces of the source norm-one directions | N1–N5 | **PROVED arithmetic, identities and fiber bounds; OPEN actual image:** joint labels and the denominator enclosure fail to supply a saving |
| T02: \((x+2y)^4+3x-y\) | F1–F8 | **PROVED local counts and scoped certificate obstructions:** symmetric fourth-power packing fails; ramified-seven critical support improves once and saturates; T02 **OPEN** |
| A quadratic witness followed by fixed univariate composition, such as \(((x-y)^2+x+y)^2\) | F6 | **PROVED:** the same saving survives, including degree-four examples distinct from T02 |
| Pure powers of a fixed integral linear form | F6 | **PROVED:** integer progressions give \(O(n)\) image; degree three or four by itself is not an obstruction |

T04 retains the different fixed polynomial \((x-y)^3-3(x+y)\) and remains **OPEN**. The plus-sign continuous and norm-one calculations below are not silently transferred to it. The separate quadratic \(P_0=x^2+xy+y^2+x\) is an OPEN benchmark branch, not a replacement for T01 or T03.

## 1 Arithmetic input from the original paper

### A1 Source identity and audit boundary

**EXTERNAL RESULT / inspected source system.** The controlling original is
OpenAI, *Planar Point Sets with Many Unit Distances*. Its Theorem 1.1 concerns
planar point sets with a superlinear number of unit distances, rather than a
small scalar polynomial image. The supplied copy is
`local-only/migration/research_supplement/shared/03-unit-distance-proof.pdf`;
its verified SHA-256 is
`62b5de8cacdfbc0f13ae1940aa81659cd233e6945b936612fbeab0ab8ab3d383`.
The [official PDF URL](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf)
was also accessed. No byte-identity assertion between that response and the
local copy is made. The PDF has no printed date or version; its creation
metadata is not used as mathematical chronology.

This audit read the complete relevant printed pages 6–16. Pages 6–9 and 12–14
were additionally rendered and visually inspected. Bibliographic statements
below are the original paper's identified imports, not fresh verification of
the cited books or papers. In particular, an original-paper proposition label
is distinguished from a theorem number in the underlying reference.

All A1–A8 records belong to this file and version date. Their evidence type is
source inspection, with elementary consequences explicitly identified where
used. Dependencies and retained gaps appear with each record. No external
novelty claim is made.

### A2 Cyclic cubic base field and its discriminant

**EXTERNAL RESULT / original Proposition 3.2, pp. 10–11; Appendix A.11,
p. 16.** Choose distinct rational primes $r_i\equiv1\pmod3$, for
$1\le i\le\ell$. Let $L_i$ be the cyclic cubic subfield of
$\mathbf Q(\zeta_{r_i})$, choose cubic characters $\chi_i$ of conductor $r_i$,
and let $F$ be the cyclic cubic field cut out by $\prod_i\chi_i$ inside
$M=L_1\cdots L_\ell$. With $R_\ell=\prod_i r_i$, the imported cyclotomic facts
and conductor–discriminant formula give

$$
\operatorname{Gal}(M/\mathbf Q)\cong(C_3)^\ell,
\quad\operatorname{Gal}(M/F)\cong(C_3)^{\ell-1},
\quad |D_F|=R_\ell^2,
\quad |D_M|=R_\ell^{2\cdot3^{\ell-1}}.
$$

Both fields are totally real. The equality
$|D_M|=|D_F|^{[M:F]}$, together with the relative discriminant formula, makes
$M/F$ everywhere unramified. Thus it supplies an elementary abelian
unramified 3-extension of rank $\ell-1$. The source cites Washington,
*Introduction to Cyclotomic Fields*, Chapter 3, especially Theorem 3.11, and
Neukirch, Chapter VI. These references are retained as source locators, rather
than reassigned theorem labels.

For the first $\ell$ primes $r_i\equiv1\pmod3$, equation (6), p. 13, uses the
prime number theorem in arithmetic progressions to obtain

$$
\log\operatorname{rd}(F)
=\frac23\sum_i\log r_i=O(\ell\log\ell).
$$

Dependency: A1 and the identified cyclotomic/discriminant imports. The
root-discriminant parameter is attached to these auxiliary primes. It is not
the product of the subsequently chosen completely split primes.

### A3 Relations, generators and survival of the tower

**EXTERNAL RESULTS / original Propositions 3.3–3.5, p. 11; Appendix
A.8–A.10, p. 16.** The sufficient forms are:

1. For a finitely generated pro-$p$ group $G$, write
   $\Phi(G)=\overline{G^p[G,G]}$ for its closed Frattini subgroup. Then
   $d(G)=\dim_{\mathbf F_p}G/\Phi(G)$. If $k$ elements of $\Phi(G)$ are killed
   by their closed normal closure $N$, the quotient retains its generator
   rank and adds at most $k$ relations:
   $$d(G/N)=d(G),\qquad r(G/N)\le r(G)+k.$$
   Relation rank is used for the finitely presented groups in the arithmetic
   application. The original cites Ribes–Zalesskii §2.8, Koch Theorem 4.10,
   and Dixon–du Sautoy–Mann–Segal Proposition 1.9(ii).
2. For $F$ totally real cubic, $\zeta_3\notin F$, and
   $G=\operatorname{Gal}(F^{\mathrm{ur},3}/F)$, Shafarevich's estimate in the
   form used here is
   $$r(G)\le d(G)+C_0$$
   for an absolute constant $C_0$. Here $F^{\mathrm{ur},3}$ means the maximal
   everywhere-unramified pro-3 extension, including infinite places. The
   source cites Shafarevich's 1963/1966 papers and
   Neukirch–Schmidt–Wingberg, Chapter X §10; it supplies no more precise
   underlying theorem number for this specialization.
3. A finite nontrivial pro-$p$ group with generator rank $d$ and relation rank
   $r$ satisfies $r>d^2/4$. Consequently, a nontrivial finitely generated
   pro-$p$ group with $r\le d^2/4$ is infinite. This is original Proposition
   3.4, the Golod–Shafarevich criterion, citing Golod–Shafarevich 1964/1965
   and Koch Chapter 11.

Dependency: A1; A2 supplies $d(G)\ge\ell-1$. These are imported general
results in the source system, not independent proofs in this report.

### A4 Finite Chebotarev choice and what it means

**EXTERNAL RESULT / original Proposition 3.6, p. 11; Appendix A.12,
p. 16.** In a prescribed finite Galois extension of $\mathbf Q$, infinitely
many rational primes split completely, even after a fixed finite exclusion.
Apply this to the normal closure of $E(i)$, where $E/F$ corresponds to the
finite Frattini quotient $G/\Phi(G)$. For any finite requested number $t$,
this selects distinct $q_1,\ldots,q_t$ with

$$
q_b\equiv1\pmod4,\qquad q_b\text{ completely split in }F,
\qquad\operatorname{Frob}_v\in\Phi(G)\quad(v\mid q_b).
$$

The source locators are Neukirch, Chapter VII §13, and Tschebotareff's 1926
paper. The complete-splitting case is all the tower argument needs; no
effective bound on the sizes of the $q_b$ is asserted here.

Dependency: A1–A3. These primes are **chosen after** $F$ and $E$ have been
fixed. The result does not guarantee an arbitrary preassigned list of small
primes. Splitting at this one finite level does not alone imply splitting in
every higher layer: the Frobenius-killing quotient in A5 provides that step.
The stated congruence is $1\bmod4$, with no stated $1\bmod3$ requirement.
Selecting primes through the finite field $E(i,\zeta_3)$ instead would impose
$1\bmod12$ by the same Chebotarev principle; that is an adaptation of the
argument, not the proposition's literal statement.

### A5 The assembled original tower and parameter order

**EXTERNAL RESULT / original Proposition 3.8, pp. 12–14; Remark 3.9,
p. 14.** For every sufficiently large fixed integer $\ell$, put

$$t=\left\lfloor(\ell-1)^2/100\right\rfloor.$$

There are a totally real cyclic cubic base field $F$, the fixed selected
$q_1,\ldots,q_t$, and a tower $F=F_0\subset F_1\subset\cdots$ satisfying:
each $F_j/F$ is finite Galois, everywhere unramified, with a 3-group Galois
group; $f_j=[F_j:\mathbf Q]\to\infty$; every $F_j$ is totally real; and

$$
\operatorname{rd}(F_j)=\operatorname{rd}(F),
\qquad q_b\text{ completely split in every }F_j.
$$

The proof outline explains the quantitative compatibility. A2 gives
$d=d(G)\ge\ell-1$. Each selected rational $q_b$ has exactly three primes
above it in $F$. Killing their Frobenius representatives therefore adds at
most $3t$ relations. By A3 and A4 the quotient $\overline G$ has

$$
d(\overline G)=d,\qquad
r(\overline G)\le d+C_0+3t
\le d+C_0+3d^2/100<d^2/4
$$

for sufficiently large $\ell$. It remains infinite by Golod–Shafarevich.
Finite layers of this quotient have trivial selected Frobenius, which gives
complete splitting at every layer. Unramified extensions preserve root
discriminant. An odd-order extension cannot turn a real place complex.

For $K_j=F_j(i)$, adjoining $i$ gives

$$\operatorname{rd}(K_j)\le2\operatorname{rd}(F).$$

**EXTERNAL RESULT / original Proposition 3.7, p. 12; Appendix A.13,
p. 16.** The sufficient class-number estimate for any number field $K$ is

$$h(K)\le\max\{2,\operatorname{rd}(K)\}^{C_{\rm class}[K:\mathbf Q]}$$

with an absolute constant $C_{\rm class}$. It comes from Minkowski's
ideal-class bound and an ideal-counting/divisor-function estimate, with
Neukirch Chapter I §5 and Lang Chapter V as source locators. Consequently
$h(K_j)\le H_\ell^{f_j}$, with
$H_\ell=(2\operatorname{rd}(F))^{2C_{\rm class}}$ and
$\log H_\ell=O(\ell\log\ell)$. Thus

$$\gamma=t\log2-\log H_\ell>0$$

eventually: $t$ grows quadratically in $\ell$, while the logarithmic
discriminant and class-number costs grow as $O(\ell\log\ell)$.

Dependencies: A2–A4 and the identified class-number estimate. This is an
existence theorem for arbitrarily large **fixed finite lists**, with the
tower depending on the construction parameters. It makes no original-paper
claim of infinitely many common split primes in one tower. Remark 3.9 fixes
$\ell$, then the $q_b$ and $Q=\prod_bq_b$, then the window radius; only
afterward does $j$ vary. Large selected primes affect $Q$ and subsequent
packing/exponent constants, even though they do not raise
$\operatorname{rd}(F)$ in this construction.

### A6 What the original norm one construction supplies

**EXTERNAL RESULT / original Definition 2.1 and Proposition 2.2, pp. 6–7.**
For an admissible datum $L$, $K=L(i)$, fixed completely split
$q_b\equiv1\pmod4$, $f=[L:\mathbf Q]$, and $h(K)\le H^f$, set
$Q=\prod_bq_b$. Each rational prime gives $f$ conjugate prime-ideal pairs
$\{\mathfrak P_s,c\mathfrak P_s\}$ in $K$, so there are $tf$ pairs.
The $2^{tf}$ binary choices of one member of each pair occupy at most $h(K)$
ideal classes. Ratios within one largest class fibre are principal. The
source constructs distinct elements $u_\varepsilon=\alpha_\varepsilon/
c(\alpha_\varepsilon)$, with

$$
uc(u)=1,\quad |\sigma(u)|=1\text{ for every complex embedding},\quad
U\subset Q^{-2}\mathcal O_K,\quad |U|\ge e^{\gamma f}.
$$

Distinctness and denominators follow from valuations
$v_{\mathfrak P_s}(u_\varepsilon)=2(\varepsilon_s-\eta_s)$ and their
negatives at conjugate primes. These are norm-one elements with controlled
poles, not a claim that every element is an algebraic-integer unit.
Dependencies: A5 for a growing sequence and $\gamma>0$. In this section the
original notation $D=Q^2$ denotes a **denominator**, not root discriminant.

### A7 The selected-translation theorem and its packing cost

**EXTERNAL RESULT / original Theorem 2.3 and Lemmas 2.4–2.6, pp. 7–9.**
Embed $D^{-1}\mathcal O_K$ in $\mathbf C^f$, using one complex embedding
over each real embedding of $L$. For the resulting lattice $\Lambda$, let
$X_a=(a+\Lambda)\cap B_R$, where $B_R$ is a product of radius-$R$ discs.
Write $N_a=|X_a|$ and count only selected translations:

$$E_a=\#\{(x,x')\in X_a^2:x'-x\in U\}.$$

If $\rho_R$ is the overlap-area ratio for two such discs with centres one
unit apart, averaging gives a coset with
$E_a\ge |U|\rho_R^fN_a$. Fix $R>1/2$ so that
$\log\rho_R>-\gamma/2$. Then

$$
E_a\ge e^{\gamma f/2}N_a,\qquad
e^{\gamma f/2}\le N_a\le(1+2RD)^{2f}\le e^{Bf},
\quad B=2\log(4RD).
$$

Projection onto one **complex** coordinate is injective on the lattice
coset, because its differences are field elements. It gives a planar set of
the same cardinality and at least $\tfrac12e^{\gamma f/2}N_a$ unit distances.
Theorem 2.3 obtains a fixed saving parameter $\delta=\gamma/(4B)>0$ for
that unit-distance assertion. Dependencies: A6 and original averaging,
field-embedding injectivity and norm-based packing. This is selected-edge
abundance; it controls neither the complement of those edges nor every
scalar polynomial output on a complete Cartesian square.

### A8 Infinite splitting, scalarization and retained obligation

**Separate stronger EXTERNAL RESULT / optional.** The human-authored
*Remarks on the Disproof of the Unit Distance Conjecture*, Proposition 2.3,
printed p. 6, states that one bounded-root-discriminant totally real tower
can have infinitely many completely split rational primes $q\equiv1\pmod4$.
Its recursive Chebotarev/cutting argument uses $F(i)$ whenever a split
prime of a finite field $F$ is selected. The remarks cite
Hajir–Maire–Ramakrishna, arXiv Theorem 2.8 / published Theorem 4. That
underlying paper was not independently checked here.
The [remarks PDF](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf?utm_source=chatgpt.com)
was read through the web; no local byte hash or printed version date is
asserted. This stronger input must not be silently attributed to A5.
Pohoata's [2026 polynomial-image paper](https://arxiv.org/abs/2606.13619)
is a separate secondary comparison in the wider report. Its polynomial
theorem and constants are not conclusions of the original unit-distance
Theorem 1.1.

**Elementary consequences inspected here; full scalar support OPEN.** There
is no field embedding $L(i)\to\mathbf R$. Taking real parts of a full complex
window loses injectivity: its field-difference kernel is $iL$. For $U$ alone,
however, put $r(u)=(u+c(u))/2$ and $s(u)=(u-c(u))/(2i)$. They belong to
$(2D)^{-1}\mathcal O_L$, all their real conjugates have modulus at most one,
and $r(u)^2+s(u)^2=1$. A prescribed real part has at most two norm-one
preimages, so $|r(U)|\ge|U|/2$. The circle relation concerns matched
coordinates of one $u$, not every pair in $r(U)^2$; multiplication and the
original unit-distance geometry are not preserved by real-part projection.

For T01 the missing requirement remains a same-set real carrier with lower
input rate $a>0$ and an entire cubic-image upper rate $c<2a$, with every
projection fibre, denominator, exception and uncovered pair charged.
An exponential input loss $e^{\eta f}$ changes the pair budget to
$2(a-\eta)$. A6–A7 supply no such full-support theorem. Even on a fixed
difference slice,
$P_3(a,a+d)=-d^3+2a+d$ is injective in $a$. Cross-slice collisions require
additional control. The original arithmetic tower survives; the requested
cubic support certificate remains **OPEN**.

## 2 The support and rate lemmas

The field degree is denoted by \(d\), the root-discriminant bound by \(D\), a rational residue modulus by \(m\), and the radius of a centered input box by \(X\). These are different quantities. In a tower, all parameters other than its layer and degree are fixed first.

### Lemma G1 Integral norm separation

**PROVED; elementary argument inspected.** Let \(K\) be totally real of degree \(d\). If distinct \(z,z'\in\mathcal O_K\) are congruent modulo \(m\mathcal O_K\), some real embedding satisfies

\[
|\sigma_i(z-z')|\ge m.
\]

**Proof.** Write \(z-z'=m\alpha\), where \(0\ne\alpha\in\mathcal O_K\). Its norm is a nonzero integer, so \(\prod_i|\sigma_i(\alpha)|\ge1\). At least one factor is at least one. This proves separation in the maximum norm over all embeddings. It gives no degree-independent separation in one chosen real embedding. \(\square\)

### Lemma G2 Input counts in a centered box

**PROVED; complete elementary proof.** Define

\[
B_K(X)=\{\alpha\in\mathcal O_K:|\sigma_i(\alpha)|\le X\text{ for every }i\}.
\]

If \(\operatorname{rd}(K)\le D\), then for \(X\ge1\),

\[
\boxed{(X/\sqrt D)^d\le |B_K(X)|\le(2X+1)^d.}
\]

**Proof.** The Minkowski lattice has covolume \(\sqrt{|\Delta_K|}\). Blichfeldt averaging on a cube of side \(X\) produces a translate containing at least \(X^d/\sqrt{|\Delta_K|}\) lattice points. Subtract one of these points from every point in that translate. The resulting distinct lattice points lie in the centered cube of radius \(X\). This proves the lower count. Lemma G1 with \(m=1\) permits disjoint half-open cubes of side one around all input points; their union is contained in a cube of side \(2X+1\). Comparing volumes proves the upper count. \(\square\)

Thus \(X>\sqrt D\) ensures unbounded input size when \(d\to\infty\). The lower count uses the discriminant; an archimedean upper bound alone does not establish enough inputs.

### Lemma G3 Uniform output population in every residue class

**PROVED; complete elementary proof.** Suppose all conjugates of the outputs lie in intervals of lengths \(W_1,\ldots,W_d\), and let \(\Omega\subset\mathcal O_K/m\mathcal O_K\) be their allowed residue classes. Then

\[
\#\{z\in\mathcal O_K:z\bmod m\in\Omega,
\ \sigma_i(z)\in I_i\text{ for every }i\}
\le |\Omega|\prod_{i=1}^d(1+W_i/m).
\]

In particular, if \(|\sigma_i(z)|\le H\), the bound is \(|\Omega|(1+2H/m)^d\).

**Proof.** By G1 the points in any one residue class are \(m\)-separated in maximum norm. Center disjoint half-open cubes of side \(m\) at them. Their union lies in the product of intervals enlarged by \(m/2\) at each end, with volume \(\prod_i(W_i+m)\). Divide by the volume \(m^d\) of one cube, then sum over all allowed classes. \(\square\)

This is a worst-case estimate per residue class. It assumes neither equidistribution of the input box nor statistical independence of its reductions.

### Lemma G4 Complete splitting and vertical amplification

**PROVED from CRT and the definition of complete splitting.** Suppose each distinct rational prime \(p_i\) splits completely in \(K\). Then for fixed positive integers \(r_i\),

\[
\mathcal O_K/\Bigl(\prod_i p_i^{r_i}\Bigr)\mathcal O_K
\cong\prod_i(\mathbb Z/p_i^{r_i}\mathbb Z)^d.
\]

For \(r_i=1\) this is the product of \(d\) copies of \(\mathbb F_{p_i}\) for each prime. For higher powers, complete splitting means that the local fields are \(\mathbb Q_{p_i}\), so their integral quotients are \(\mathbb Z/p_i^{r_i}\mathbb Z\). CRT combines the factors.

If every output belongs to a specified subset of density \(\eta_i\) in every coordinate above \(p_i\), then, with \(m=\prod_i p_i^{r_i}\) and \(\eta=\prod_i\eta_i\),

\[
|\Omega|\le(\eta m)^d.
\]

The quotient coordinates are independent algebraic factors. The actual bounded carrier may occupy a correlated subset of them, which can only reduce this allowed output set. For other splitting types, one must count the actual residue degrees, ramification and number of factors; \(d\) degree-one copies cannot be assumed.

### Lemma G5 The fully charged box criterion

**PROVED implication; its antecedents must be established for the actual carrier.** Let \(F\in\mathbb Z[x,y]\), use \(B=B_K(X)\), and suppose every output belongs to at most \((\eta m)^d\) residue classes and has all conjugates bounded by \(H(X)\). Then

\[
|F(B,B)|\le[\eta(2H(X)+m)]^d
\le\Theta(X)^d|B|^2,
\]

\[
\boxed{\Theta(X)=D\eta\frac{2H(X)+m}{X^2}.}
\]

**Proof.** Apply G3 and G4, then square the lower bound in G2. \(\square\)

If \(\Theta<1\), \(X>\sqrt D\), and a proved same-set real transport preserves input and image cardinalities, G2 gives the exact exponent

\[
c=\frac{-\log\Theta}{\log(2X+1)}>0.
\]

Indeed \(|B|\le(2X+1)^d\) implies \(\Theta^d\le |B|^{-c}\). If this numerical certificate has \(\Theta\ge1\), that certificate fails; it does not lower-bound the occupied image. A local defect \(\eta<1\), complete splitting and bounded root discriminant do not alone imply \(\Theta<1\).

### Lemma G6 General rates and the cost of input losses

**PROVED implication; complete proof.** Suppose a family of actual real scalar sets satisfies

\[
\log|A_d|\ge ad-o(d),\quad \log|A_d|\le Bd+o(d),\quad
\log|P(A_d,A_d)|\le bd+o(d),
\]

where \(a>0\), \(B>0\), and \(\delta=2a-b>0\). Every fixed \(0<c<\delta/B\) is eventually certified.

**Proof.** The image divided by \(|A_d|^2\) is at most \(e^{-\delta d+o(d)}\). Since \(\log|A_d|\le Bd+o(d)\), a strict choice \(cB<\delta\) absorbs all error terms and any fixed or polynomial prefactors. \(\square\)

If thinning, projection or parameter fibers lose \(e^{\lambda d+o(d)}\) inputs, replace \(a\) by \(a-\lambda\). The gap decreases by \(2\lambda\). An unknown loss is not zero. Boundary exponents require additional error control; they do not follow from this asymptotic lemma. G5 has an exact finite bound and therefore has stronger boundary control in that particular situation.

### Lemma G7 Common scaling and finite local images

**PROVED; elementary identities.** For a nonzero integer \(Q\), if \(P=\sum_{j=0}^kP_j\), with \(P_j\) homogeneous of degree \(j\), the unique polynomial of degree at most \(k\) satisfying \(F_Q(Qx,Qy)=Q^kP(x,y)\) is

\[
F_Q=\sum_{j=0}^k Q^{k-j}P_j.
\]

This follows by comparing homogeneous pieces. Its reduction at \(p\mid Q\) is the leading homogeneous part \(P_k\). For a real embedding and an algebraic carrier \(B\), the correct normalized set is \(A=Q^{-1}\sigma(B)\); then the image cardinalities agree. Scaling alone gives no additional compression.

For a nonzero linear form \(L\) over \(\mathbb F_p\),

\[
|L(\mathbb F_p,\mathbb F_p)^k|=1+\frac{p-1}{\gcd(k,p-1)}.
\]

**Proof.** \(L\) is surjective. The cyclic group \(\mathbb F_p^\times\) has a power-map kernel of size \(\gcd(k,p-1)\), and zero supplies one additional value. \(\square\)

For an odd prime \(p\nmid k\), the number of \(k\)-th powers modulo \(p^r\) is

\[
1+\frac1g\sum_{h=0}^{\lfloor(r-1)/k\rfloor}\varphi(p^{r-kh}),
\qquad g=\gcd(k,p-1).
\]

Every nonzero power has valuation \(kh<r\); its unit part is a \(k\)-th power in the cyclic unit group at the remaining precision, with kernel \(g\). Different valuations give disjoint values. The density tends to

\[
\frac{p-1}{gp(1-p^{-k})}>0.
\]

Consequently greater precision at one good fixed prime does not supply a density tending to zero for this full power-residue support.

The undeformed T01 polynomial has full image over every odd finite field: in coordinates \(h=x-y\), \(s=x+y\), it is \(h^3+s\). For T02, the change \((x,y)\mapsto(x+2y,3x-y)\) has determinant \(-7\), so the undeformed polynomial has full field image at \(p\ne7\). The residue permutation in F7 also covers the field at seven. The useful power-residue defect is therefore a property of the removable deformation, or of a more refined restricted-input quotient; it is not a sparsity assertion about the original unrestricted field image.

### Lemma G8 Restricted inputs and exact output fibers

**PROVED; elementary bookkeeping.** For a finite ring \(R\), a same-set input \(E\subset R\), and its actual polynomial image, the local factor relative to the pair budget is

\[
\kappa(R,E,F)=\frac{|R|\,|F(E,E)|}{|E|^2}.
\]

This is output density divided by the square of input density. Product factors multiply only when the construction and all local restrictions are proved to have that product structure. A finite product ring does not admit an injective unital ring map into \(\mathbb R\) when it has nontrivial zero divisors; a quotient calculation therefore still requires a faithful arithmetic realization and a full rate ledger.

For any finite real \(A\), set \(r(z)=|\{(a,b)\in A^2:P(a,b)=z\}|\). Then

\[
|P(A,A)|=\sum_{(a,b)\in A^2}\frac1{r(P(a,b))}.
\]

Each nonempty fiber contributes one. If all but \(O(n^{2-\eta})\) ordered pairs have actual fiber at least \(n^\varepsilon\), then

\[
|P(A,A)|\le O(n^{2-\eta})+n^{2-\varepsilon}.
\]

Large collision energy alone gives the opposite Cauchy-Schwarz inequality, \(|P(A,A)|\ge n^4/\sum_zr(z)^2\). Small Shannon entropy and coarse covering numbers also do not upper-bound exact support without an exact population bound for each cell. These are support requirements, not extra saving factors.

**Sources for G1–G8.** Corrected C0 §§4–6; the cubic checkpoint §§B, E–F; the 2026-10-11 transfer note §§A2–A3 and entropy note §C5. The statements and elementary proofs above are inspected consolidations. Their source identities and audit scopes appear in the claim ledger.

## 3 Quadratic compression

### Theorem Q1 The transverse rank one family

**PROVED within the supplied source system; complete argument inspected and reproduced.** Let

\[
L=ax+by,\qquad T=cx+ey,
\]

have integral coefficients with \(\gcd(a,b)=1\) and \(ab(ae-bc)\ne0\). For the fixed polynomial \(P=L^2+T\), there are arbitrarily large finite \(A\subset\mathbb R\) and a fixed \(c_P>0\) with

\[
|P(A,A)|\le |A|^{2-c_P}.
\]

**Proof.** Put \(A_0=(|a|+|b|)^2\), \(A_1=|c|+|e|\), and \(C_P=2(A_0+A_1)+1\). The original tower input A5 supplies \(t\asymp\ell^2\) primes \(p_i\equiv1\pmod4\), with \(\log D=O(\ell\log\ell)\). Choose \(\ell\) large enough that

\[
C_PD(3/5)^t<1.
\]

After the primes are selected, fix \(Q=\prod_i p_i\),
\(\rho=\prod_i(p_i+1)/(2p_i)\), and \(X>\max\{Q,\sqrt D,1\}\). All these parameters precede the growing tower layer.

Use \(F_Q=L^2+QT\). Since \(L\) is primitive it is surjective over every selected residue field, so every output is a square in each CRT coordinate. G4 gives at most \((\rho Q)^d\) classes. Every conjugate of every output has absolute value at most \(A_0X^2+A_1QX\). G5 therefore gives

\[
|F_Q(B_K(X),B_K(X))|\le \theta^d|B_K(X)|^2,
\qquad \theta=C_PD\rho<1.
\]

The embedding and common input scaling \(A=Q^{-1}\sigma_1(B_K(X))\) preserve both cardinalities by G7. With \(n\le(2X+1)^d\), choose

\[
c_P=-\log\theta/\log(2X+1)>0.
\]

The lower input count tends to infinity, proving the fixed-polynomial, same-set theorem. Every ordered pair was counted, including the diagonal. \(\square\)

For \(P_*=(x+2y)^2+3x-y\), the sharper displayed certificate is

\[
\Theta_*(X)=D\rho(18+8Q/X+Q/X^2)<27D\rho.
\]

The original finite-list tower is sufficient. An infinite common split-prime set, regulator estimate and class-group selection for the input carrier are unnecessary here. The class-group bound is an ingredient in the original unit-distance direction count, not a further charge in this quadratic box proof.

**Nonspecialness under the stated hypotheses.** An additive representation \(g(u(x)+v(y))\) of total degree two either has linear \(g\), which cannot produce a mixed term, or quadratic \(g\) with affine inner functions. In the latter case its linear part is parallel to its rank-one quadratic direction, requiring \(ae-bc=0\). A multiplicative representation at degree two has affine \(g,u,v\), and its leading part is a multiple of \(xy\), whereas \(L^2\) has nonzero \(x^2\) and \(y^2\) terms. Hence the family is nonspecial. The conditions \(ab\ne0\) and transversality qualify this claim; they must not be omitted from the sourced theorem.

Source: corrected C0, Theorem C0.1 and §§4–6, dated 2026-09-03. External novelty has not been assessed by this report.

### Theorem Q2 The reference quadratic with the factor 13

**EXTERNAL RESULT and independently reconstructed elementary implication.** For

\[
f=(x-y)^2+x+y,\qquad f_Q=(x-y)^2+Q(x+y),
\]

choose fixed split primes so that \(\theta=13D\rho<1\), then fix
\(X\ge\max\{Q,2\sqrt D,1\}\). The centered box gives

\[
(X/\sqrt D)^d\le n\le(2X+1)^d,
\quad |f_Q(B,B)|\le(13D\rho)^d n^2.
\]

The normalized real set \(A=Q^{-1}\sigma_1(B)\) therefore satisfies

\[
|f(A,A)|\le n^{2-c},\qquad c=-\log(13D\rho)/\log(2X+1)>0.
\]

**Proof of the numerical constant.** All outputs have conjugate radius at most \(2QX+4X^2\le6X^2\). G3–G4 yield \([\rho(12X^2+Q)]^d\le(13\rho X^2)^d\). Divide by the squared input lower bound. The identity \(f_Q(Qx,Qy)=Q^2f(x,y)\) supplies the exact common transport. \(\square\)

For every fixed \(\epsilon>0\), choosing larger fixed \(X\) gives \(|A+A|\le |A|^{1+\epsilon}\): use \(B+B\subset B_K(2X)\), the upper bound \((4X+1)^d\), and choose \(4X+1\le(X/\sqrt D)^{1+\epsilon}\). The saving exponent may decrease but remains positive.

This is Pohoata, *Split primes and the Elekes–Rónyai problem*, arXiv:2606.13619v2, Theorem 1.1, Lemmas 3.2–3.3 and Proposition 4.1. His Proposition 3.1 uses the stronger infinite common split-prime tower. Q2 also follows from the original finite-list input A5, because \(13D\rho<1\) can be arranged before the primes and box radius are fixed. The original unit-distance paper itself does not state Q2 or the constant 13.

### Lemma Q5 The finite interval comparison

**PROVED elementary interval bound; a separate comparison with Pohoata Proposition 2.1 and Corollary 2.2.** For \([N]=\{1,\ldots,N\}\), fixed distinct odd primes with product \(Q\), and their square density \(\rho\),

\[
|f_Q([N],[N])|\le\rho(2QN+N^2+Q).
\]

**Proof.** The integer outputs lie in an interval of length at most \(2QN+N^2\) and occupy at most \(\rho Q\) classes modulo \(Q\). Each class supplies at most the interval length divided by \(Q\), plus one. \(\square\)

The prime number theorem permits \(t=(1+o(1))\log N/\log\log N\) primes in \([\log N,2\log N]\), with \(Q\le N\). The product of their factors \(1+1/p\) is \(e^{o(1)}\), so the bound becomes

\[
N^2\exp\left[-(\log2-o(1))\frac{\log N}{\log\log N}\right].
\]

Exact rescaling to \(A=[N]/Q\) keeps \(f\) fixed even when \(Q\) varies. The saving furnished by this particular interval comparison has exponent tending to zero. It does not prove a fixed positive exponent. Thus a varying auxiliary modulus is not intrinsically invalid when an exact transport removes it; the missing issue is a uniform positive rate. The tower replaces growing rational primes with growing numbers of prime-ideal coordinates while keeping the remaining costs fixed.

### Lemma Q3 Full rank binary quadratics at good primes

**PROVED; complete finite-field argument.** Over \(\mathbb F_p\) with odd \(p\), a homogeneous binary quadratic form has image \(\{0\}\) at rank zero, a set of \((p+1)/2\) elements at rank one, and the entire field at rank two.

**Proof.** Rank one is a nonzero scalar times the square of a surjective linear form. An isotropic rank-two form is equivalent to \(\lambda uv\), which represents every value. An anisotropic rank-two form is equivalent to \(\lambda(u^2-av^2)\), with \(a\) nonsquare. This is a scalar multiple of the norm \(\mathbb F_{p^2}\to\mathbb F_p\). On the cyclic multiplicative group, the norm \(z\mapsto z^{p+1}\) has image of size \(p-1\); zero is also represented. \(\square\)

For an integral nondegenerate quadratic form, only finitely many primes divide its determinant, discriminant or content. At the other odd primes, adding linear and constant terms preserves surjectivity by completing the square and translating the inputs and output. The common-scaling deformation in G7 therefore has no unrestricted first-level density defect at good primes.

In particular \(q=x^2+xy+y^2\) has full image for every odd \(p\ne3\). Selecting more good completely split primes supplies no square-type saving for T03. This says nothing by itself about restricted inputs, prime powers, correlated observables or other real carriers. Source: corrected C0, Lemma 4.2 and §10 C3.

### Lemma Q4 Prime power norm images and their limits

**PROVED in the located norm–trace checkpoint; valuation proof inspected.** For \(q=x^2+xy+y^2\) modulo \(p^k\):

- If \(p\equiv1\pmod3\), the image is the full ring.
- If \(p\equiv2\pmod3\), including \(p=2\), it consists of zero and residues of even valuation. Its size is \((p^{k+1}+1)/(p+1)\) for even \(k\), and \((p^{k+1}+p)/(p+1)\) for odd \(k\). Its density is at least \(p/(p+1)\).
- For \(p=3\), it consists of zero and residues whose first nonzero ternary digit is one. Its size is \((3^k+1)/2\).

**Proof.** At a split prime, an invertible local change of variables factors the form into two independent linear forms, so setting one equal to one represents every residue. At an inert prime, anisotropy modulo \(p\) forces both inputs divisible by \(p\) whenever the output is divisible by \(p\); dividing the form by \(p^2\) gives the even-valuation condition recursively. Every unit is represented by a nonsingular finite-field solution and Hensel lifting. This includes \(p=2\), since at a nonzero input at least one of the partial derivatives \(y,x\) is nonzero modulo two. Summing the unit counts at even valuations gives the displayed sizes.

At three, \(q\equiv(x-y)^2\). Unit outputs have leading ternary digit one. If the inputs are not both divisible by three and \(q\equiv0\), write \(x=y+3t\); then \(q=3(y^2+3yt+3t^2)\), with valuation one and leading digit one. Common divisibility reduces by nine. Conversely units congruent to one modulo three are 3-adic squares: \(q(s,0)=s^2\) and \(q(s,s)=3s^2\), followed by common powers of three, represent the permitted residues. Summing \(3^{k-v-1}\) over \(0\le v<k\), and adding zero, gives \((3^k+1)/2\). \(\square\)

Source: the separate T01 norm–trace checkpoint, §7.1, dated 2026-09-10. This is a local theorem about the homogeneous quadratic, not a solution of its real target or of \(P_0=q+x\). These positive but saturating defects need a separate field-compatibility and packing ledger. Broader asymptotic norm-sieve obstructions use extra arithmetic results and are not conclusions of the original unit-distance paper alone.

## 4 Cubic local restrictions and packing

### Cubic local image

**C1 — PROVED; inspected elementary argument.** For every odd prime \(p\),
integer \(C\), and \(k\ge1\), set \(r=\min(v_p(C),k)\), taking
\(v_p(0)=\infty\). On \(R_k=\mathbb Z/p^k\mathbb Z\), the full image of
\(P_C(x,y)=(x-y)^3+C(x+y)\) is exactly
\[
\{z\in R_k:z\bmod p^r\text{ is a cube}\}.
\]
If \(N_r(a)\) counts cube roots modulo \(p^r\), its ordered fiber size is
\[
r_{P_C,k}(z)=p^kN_r(z\bmod p^r).
\]
For \(r=0\), the quotient has one class and \(N_0=1\).
Source: cubic checkpoint §E.1; polynomial and quantifiers are as stated.

**Proof.** The invertible change \(d=x-y\) gives
\(P_C=d^3+Cd+2Cy\). Since \(2\) is a unit, \(2Cy\) ranges over
\(p^rR_k\), proving the image statement. For a permitted \(z\), there
are \(N_r(z) p^{k-r}\) choices of \(d\); for each, the equation for
\(y\) has \(p^r\) solutions. Their product is the claimed fiber size.
This also covers \(r=k\), where \(C\) vanishes in \(R_k\).

**C2 — PROVED; inspected count.** For odd \(p\ne3\), put
\(g=\gcd(3,p-1)\). For every \(r\ge1\), the number of cubes is
\[
c_p(r)=1+\frac1g
\sum_{h=0}^{\lfloor(r-1)/3\rfloor}\varphi(p^{r-3h}).
\]
In particular, for \(p\equiv1\pmod3\),
\[
\delta_{p,r}:=\frac{c_p(r)}{p^r}
=p^{-r}+\frac{p-1}{3p}
\sum_{h=0}^{\lfloor(r-1)/3\rfloor}p^{-3h},
\]
\[
\delta_{p,1}=\frac{p+2}{3p},\qquad
\delta_{p,2}=\frac{p^2-p+3}{3p^2},\qquad
\lim_{r\to\infty}\delta_{p,r}=\frac{p^2}{3(p^2+p+1)}.
\]
Source: §E.1; dependency C1 for application to \(P_C\).

**Proof.** A nonzero cube has valuation \(3h<r\). On units modulo
\(p^s\), cubing has kernel size \(g\): there are \(g\) cube roots of
unity in \(\mathbb F_p\), and each lifts uniquely because its derivative
\(3x^2\) is a unit. Thus the valuation-\(3h\) shell contains
\(\varphi(p^{r-3h})/g\) cube classes. Add the zero class and divide by
\(p^r\). The limit follows by summing a geometric series. This formula
does not cover \(p=3\); C1's image description still does.

**C3 — PROVED conditional on the stated splitting; inspected arithmetic.**
If \(p\) splits completely in a degree-\(d\) number field \(L\), then
\[
\mathcal O_L/p^k\mathcal O_L
\cong(\mathbb Z/p^k\mathbb Z)^d.
\]
Indeed every completion at a prime above \(p\) is \(\mathbb Q_p\);
the prime-power Chinese remainder decomposition gives the identity.
Consequently C1 imposes exactly \(d\) copies of its scalar restriction,
with density \(\delta_{p,r}^d\). Distinct rational primes multiply by CRT.
This is a product-ring identity, not a random independence assumption.
Sources: §E.1 and the identified tower input.

For the fixed-polynomial clearing identity
\[
M^3P_3(u/M,v/M)=(u-v)^3+M^2(u+v),
\tag{C.1}
\]
usable precision at \(p\mid M\) saturates at \(2v_p(M)\). Beyond this,
C1 gives the inverse image of the same cube set, so its density no longer
decreases. Complete splitting amplifies this fixed defect vertically;
it does not turn increasing precision into an unbounded local gain.

### Cubic range and population

**C4 — PROVED; inspected exact continuous range.** For real
\(I=[c-X/2,c+X/2]\), \(X>0\), and integer \(M>0\), the image of
\(Z_M(u,v)=(u-v)^3+M^2(u+v)\) on \(I^2\) is an interval of width
\[
W_M(X)=2\max(X^3,M^2X).
\tag{C.2}
\]
Source: §E.2 and §H.4; the polynomial has the positive linear sign.

**Proof.** Put \(d=u-v\), \(s=u+v-2c\). Their feasible region is
\(|d|+|s|\le X\), and the centered output is \(d^3+M^2s\).
For \(|d|=t\), its largest absolute value is
\(t^3+M^2(X-t)\). This convex function has its maximum at \(t=0\)
or \(t=X\). The region is centrally symmetric, both extreme signs
occur, and its continuous image is connected. Translation changes only
the output center \(2M^2c\).

**C5 — PROVED upper certificate; inspected full-pair counting.** Let
\(L\) be totally real of degree \(d\), root discriminant \(R\), and
let a fixed prime \(p\equiv1\pmod3\) split completely in \(L\).
Averaging gives a translate of a side-\(X\) Minkowski cube whose integral
section \(B\) satisfies
\[
(X/\sqrt R)^d\le |B|\le(X+1)^d.
\]
For \(A=\sigma_1(B)/p\), every ordered pair satisfies
\[
|P_3(A,A)|\le
\left[\delta_{p,2}\{p^2+2\max(X^3,p^2X)\}\right]^d.
\tag{C.3}
\]
Sources: §§D.2, E.3 and F.1; dependencies C1–C4, lattice covolume,
and the integral norm. All primes, denominators and widths are fixed
before tower degree grows; \(X>\sqrt R\) supplies input growth.

**Proof.** The lattice covolume is \(R^{d/2}\), giving the lower count
by translated averaging. A nonzero algebraic integer has norm of absolute
value at least one, so two integral points differ by at least one in
some real coordinate; packing side-one cubes proves the upper count.
The real field embedding and division by \(p\) are injective.

The cleared output in (C.1) occupies at most
\((p^2\delta_{p,2})^d\) residue classes modulo \(p^2\mathcal O_L\).
Within each class, differences are \(p^2\gamma\), with integral
\(\gamma\ne0\); one conjugate difference is at least \(p^2\).
Packing side-\(p^2\) cubes in the output rectangle bounds each class
by \((1+W_p(X)/p^2)^d\). Multiplication gives (C.3). No input
equidistribution or omitted-pair hypothesis is needed.

Dividing this certificate by the squared input lower bound yields
\[
\beta_p(X)=R\delta_{p,2}
\left[2\max(X,p^2/X)+p^2/X^2\right].
\tag{C.4}
\]
The root-discriminant cost, fixed denominator and cubic height are all
present. Class groups and regulators do not enter this box calculation.

**C6 — PROVED optimization; FAILED certificate.** For every eligible
\(p\ge7\),
\[
\inf_{X>0}\beta_p(X)=R\delta_{p,2}(2p+1).
\tag{C.5}
\]
For the checkpoint's \(p\equiv1\pmod{12}\), hence \(p\ge13\),
\[
\inf_X\beta_p(X)\ge1431R/169>8R\ge8.
\]
Source: §§D.1 and F.2; dependencies C2 and C5.

**Proof.** For \(X\le p\), the bracket in (C.4) is
\(2p^2/X+p^2/X^2\), which decreases. For \(X\ge p\), it is
\(2X+p^2/X^2\), whose derivative \(2-2p^2/X^3\) is positive.
The minimum is therefore at \(X=p\). The resulting scalar factor is
\(2p/3-1/3+5/(3p)+1/p^2\), increasing for \(p\ge7\).
Its value at 13 is \(1431/169\). Restricting to \(X>\sqrt R\)
can only increase this lower bound.

The congruence \(1\bmod12\) comes from retaining splitting in
\(\mathbb Q(i)\) and also prescribing splitting in
\(\mathbb Q(\zeta_3)\), a stated adaptation of the source Chebotarev
step. Cube sparsity alone needs \(1\bmod3\). Even allowing \(p=7\)
leaves the base \(225R/49>1\). Thus the extra congruence is not the
reason the certificate fails. A failed upper certificate is not an
actual-image lower bound.

### Further precision and input restrictions

**C7 — PROVED obstruction for the specified packing architecture.** Fix
\[
M=\prod_{b=1}^t p_b^{a_b},\quad
m=\prod_{b=1}^t p_b^{r_b}\mid M^2,\quad
1\le r_b\le2a_b,
\]
with distinct completely split primes \(p_b\equiv1\pmod3\),
\(a_b\ge1\), and \(t\ge1\). Put
\(\delta_m=\prod_b\delta_{p_b,r_b}\). For translated anisotropic
Minkowski rectangles of half-widths \(h_i>0\), cleared outputs counted
by their cube classes and uniform norm packing have normalized
certificate
\[
R^d\delta_m^d\prod_i\Phi_{M,m}(h_i),\qquad
\Phi_{M,m}(h)=\frac m{4h^2}+\max(4h,M^2/h).
\]
Every coordinate has exact minimum
\[
\inf_{h>0}\Phi_{M,m}(h)=2M+m/M^2.
\]
Sources: §§F.2–F.3 and H.4; dependencies C2–C5.

**Proof.** Use (C.2) with \(X=2h\), modulus \(m\), and divide
the population bound by input volume squared. Below \(h=M/2\)
both terms decrease; above it, the derivative is
\(4-m/(2h^3)>0\), since \(m\le M^2\) and \(M\ge7\).
Also
\[
p_b^{a_b}\delta_{p_b,r_b}
\ge p_b^{a_b}\frac{p_b-1}{3p_b}\ge2,
\]
so \(M\delta_m\ge2^t\). The best normalized base is consequently
larger than \(2R M\delta_m\ge2^{t+1}R>1\). Anisotropy and
translation do not repair it. Beyond coefficient saturation, the density
is unchanged while a larger modulus increases the same population
expression; extra digits do not improve this certificate either.

The inherited algebraic-denominator extension is also scoped: take
\(\mu\in L^\times\) with \(\mu^2\in m\mathcal O_L\), where
\(m\) is the same completely split good-prime modulus specified above,
and put \(a_i=|\sigma_i(\mu)|\). A denominator in an extension of
\(L\) would require its own field degree and embedding ledger.
Its normalized factors obey
\[
\frac m{4h_i^2}+\max(4h_i,a_i^2/h_i)\ge2a_i,
\qquad |N(\mu)|\ge m^{d/2}.
\]
Their geometric mean is at least \(2\sqrt m\). For good primes,
\(\sqrt{p^r}\delta_{p,r}>1\): for \(r=1\) this is
\((p+2)/(3\sqrt p)>1\); for \(r\ge2\) the bound is at least
\((p-1)/3\ge2\). Thus this variant also has base greater than one.
This closes the displayed denominator-and-rectangle argument, not
arbitrary algebraic input sets.

The same source §F.3 records three exceptional-prime tests. Even granting
complete splitting at 2 and 3, which the supplied tower does not assert,
their optimized certificate bases are

| Restriction | Optimized base |
|---|---|
| Unscaled cubic parity | \((3/2)2^{1/3}R\) |
| Denominator 3, cubes modulo 9 | \(7R/3\) |
| Both preceding restrictions | \(4R/3\) |

These are additional inspected deductions under C7's **FAILED certificate**
scope, rather than claims that 2 or 3 can be used in the existing tower.
To verify them, write the unscaled polynomial as
\(d^3+d+2y\). Since \(d^3+d\) is even and \(d=0\) reaches
every even residue, its image modulo \(2^k\) is exactly the even
classes. The density stays \(1/2\); the best packing modulus is 2.
The normalized factor is
\(R[X^{-2}+\max(X,X^{-1})]\). On \(X\le1\) it decreases;
on \(X\ge1\) its derivative vanishes at \(X=2^{1/3}\), giving
the first base.

For denominator 3, the cubes modulo 9 are \(0,1,-1\). The factor is
\((R/3)[9/X^2+2\max(X,9/X)]\), decreasing to \(X=3\) and
increasing thereafter, giving \(7R/3\). The cleared polynomial also
has the parity restriction. Combining it with the modulo-9 condition
uses modulus 18, density \(1/6\), and factor
\((R/6)[18/X^2+2\max(X,9/X)]\), likewise minimized at 3.
All three bases exceed one. This paragraph settles only these explicitly
specified exceptional restrictions; it is not a theorem about every
mixed-prime coefficient or every restricted input set.

**C8 — PROVED obstruction with input thinning charged twice.** Let
\(M=\prod_{b=1}^t p_b\) be squarefree as above,
\(\mathcal R=\prod_b\mathbb F_{p_b}\), and let an arbitrary nonempty
correlated code \(\mathcal C\subset\mathcal R^d\) restrict inputs.
Write \(\mathcal D=(\mathcal C-\mathcal C)^{\circ3}\). The
averaged-input/uniform-lift certificate still fails. Source: §E.4 and
export §6.3; dependencies C4–C5 and elementary finite-ring fibers.

**Proof.** A prescribed output difference-cube has at most \(3^t\)
differences per coordinate, each with exactly \(M\) ambient ordered
pairs. Therefore
\[
|\mathcal D|\ge|\mathcal C|^2/(3^tM)^d.
\]
Translated averaging guarantees only
\(|B|\ge |\mathcal C|X^d/(M^dR^{d/2})\). Counting the allowed
output classes uniformly gives the normalized certificate
\[
\frac{M^d|\mathcal D|}{|\mathcal C|^2}
\left[\frac{R\{M+2\max(X^3,M^2X)\}}{X^2}\right]^d.
\]
Its base is at least
\(3^{-t}R(2M+1/M)>2R\prod_b(p_b/3)>1\).
The squared denominator \(|\mathcal C|^2\) is essential. This does
not exclude an anomalously dense input translate combined with a new
residue-sensitive output count, or arbitrary sparse real carriers.

### Continuous positive-volume covers

**C9 — PROVED continuous-cover theorem; inspected complete argument.**
Let \(m\ge1\), let \(W\subset\mathbb R^m\) be bounded Borel with
positive volume \(V\), and define the coordinatewise full image
\[
\mathcal P_m(W)=\{(x-y)^{\circ3}+x+y:x,y\in W\}.
\]
If \(N_1\) denotes the least number of translates of half-open unit
axis cubes covering this image, then
\[
N_1(\mathcal P_m(W))>(\sqrt3/\pi)^m V^2.
\tag{C.6}
\]
Source: the 3 September continuous checkpoint §F.3, equations
(F.6)–(F.10); dependency only the displayed analytic argument.

**Proof.** Fix any \(y\in W\). The map
\(\Phi_y(x)=(x-y)^{\circ3}+x+y\) is a global continuously
differentiable diffeomorphism: each coordinate has positive derivative
\(1+3(x_i-y_i)^2\) and ranges over the real line. Its Jacobian is
\(J_y(x)=\prod_i(1+3(x_i-y_i)^2)\). Change of variables and
Cauchy–Schwarz give
\[
V^2\le\left(\int_W J_y\right)\left(\int_W J_y^{-1}\right)
=\operatorname{vol}(\Phi_y(W))\int_W J_y^{-1}.
\]
Since \(W\) is bounded and the integrand is everywhere positive,
\[
\int_W J_y^{-1}<\int_{\mathbb R^m}J_y^{-1}
=\left(\int_{\mathbb R}\frac{dt}{1+3t^2}\right)^m
=(\pi/\sqrt3)^m.
\]
Thus \(\operatorname{vol}(\Phi_y(W))>(\sqrt3/\pi)^mV^2\).
Every cover of the full image covers this fixed-input slice; a union
of \(N\) unit cubes has volume at most \(N\). This proves (C.6)
without needing measurability of the entire two-input image.

For the source's volume/covolume input count followed by a full
continuous-image cover and norm packing, the block factor is
\[
\eta_{\rm block}=R^m N_1(\mathcal P_m(W))/V^2
>(R\sqrt3/\pi)^m.
\]
The standard Minkowski discriminant bound gives \(R\ge2\) for
every totally real field of degree \(d\ge2\). Precisely,
\(R\ge(d^d/d!)^{2/d}\); for \(d=2\) this lower bound is 2,
and for \(d\ge3\), AM–GM gives
\((d!)^{1/d}\le(d+1)/2\le d/\sqrt2\).
Consequently \(\eta_{\rm block}>1\). Source: §G.1; this last step
uses Minkowski's standard theorem as an identified external input.

This excludes the stated certificate for every bounded positive-volume
Borel window, including disconnected, correlated and nonrectangular
ones. Its hypotheses concern continuous volume and the cover used to
count all permitted lifts. It supplies no lower bound on an arbitrary
sparse finite lattice image. A discrete carrier with an additional
exact-support argument is outside this theorem's conclusion.

## 5 The norm one trace import



**N1 — PROVED relative to the source arithmetic supply.** In the CM
field \(K=L(i)\), complex conjugation \(c\) exchanges the \(td\)
selected prime pairs. Binary choices give ideals
\(\mathfrak a_\epsilon\). A largest ideal-class fiber, anchored at
\(\eta\), permits
\((\alpha_\epsilon)=\mathfrak a_\epsilon\mathfrak a_\eta^{-1}\)
and \(u_\epsilon=\alpha_\epsilon/c(\alpha_\epsilon)\). Then
\[
uc(u)=1,\quad v_{\mathfrak p_s}(u)=2(\epsilon_s-\eta_s),\quad
Q_0^2u\in\mathcal O_K,\qquad Q_0=\prod_bq_b,
\]
\[
e^{\gamma d}\le |U|\le2^{td},\qquad
\gamma=t\log2-\log H>0.
\tag{N.1}
\]
Sources: checkpoint §§C.2/H.2, export §4.5 and formal source Proposition
2.2; the supplied bound is \(h(K)\le H^d\). There is no new arithmetic
input or assertion of a prescribed numerical \(\gamma\).

**Proof of the deductions.** Ideal-class pigeonholing retains at least
\(2^{td}/H^d\) choices. Distinct binary vectors give distinct displayed
valuations, proving distinctness. The valuations bound the poles by
\(Q_0^2\), and CM conjugation gives modulus one in every complex
embedding. For \(t(u)=u+u^{-1}\), trace equality implies
\(v=u\) or \(v=u^{-1}\). The latter requires
\(\epsilon+\epsilon'=2\eta\), which forces both vectors to equal
\(\eta\). Hence \(t\) is injective on this \(U\), and
\(T=t(U)\subset L\) has \(|T|=|U|\) with conjugates in \([-2,2]\).

The export §4.5 additionally records
\(|UU|,|U/U|\le4\cdot3^{td}\) from the source's ideal labels.
This supporting arithmetic bound is retained as reported, with its
original proof input identified; no new class-number or unit-theorem
audit is claimed. It explains the attraction of product and ratio
parameters: each has three valuation possibilities where the inputs
have four ordered binary choices. N2 below shows why counting them
separately is insufficient. Their joint valuation information recovers
both ordered input vectors.

**N2 — PROVED joint identities; no parameter saving.** For all ordered
\((u,v)\in U^2\), let \(p=t(uv)\), \(s=t(u/v)\),
\(D=t(u)-t(v)\), \(E=t(u)+t(v)\). Expansion gives
\[
D^2=(p-2)(s-2),\qquad E^2=(p+2)(s+2),\qquad P_3=D^3+E.
\tag{N.2}
\]
The joint map \((u,v)\mapsto(p,s)\) has fibers at most eight.
Source: §H.2; dependency N1.

**Proof.** Each trace determines its nonzero argument up to inversion,
so there are at most four choices of \((uv,u/v)\). Each determines
\(u^2=(uv)(u/v)\), with at most two roots, then determines \(v\).
Thus the joint parameter image has at least \(|U|^2/8\) states.
The identities retain both parameters and signed roots; counting this
joint support alone gives only a constant-factor reduction.

**N3 — PROVED fixed-label fiber bound; full cubic fibers remain OPEN.**
Fix either \(uv=\xi\) or \(u/v=\xi\), and a cubic output \(z\).
There are at most six ordered pairs satisfying both constraints. Source:
§H.2; dependencies N1–N2.

**Proof.** In both cases \(t(v)=\xi/u+u/\xi\). Put
\(a=1-\xi^{-1},b=1-\xi,c=1+\xi^{-1},e=1+\xi\).
Then \(D=au+b/u\), \(E=cu+e/u\). Multiplying \(D^3+E=z\)
by \(u^3\) gives
\[
a^3u^6+(3a^2b+c)u^4-zu^3+(3ab^2+e)u^2+b^3=0.
\]
If \(\xi\ne1\), its leading coefficient is nonzero. For \(\xi=1\),
the polynomial is \(2u^4-zu^3+2u^2\), also nonzero. Its degree
is at most six; the fixed label determines \(v\) from \(u\).
Consequently
\[
|P_3(T,T)|\,|UU|\ge|U|^2/6,\qquad
|P_3(T,T)|\,|U/U|\ge|U|^2/6.
\]
These are not quadratic lower bounds for the actual image. A full
cubic fiber of size \(r\) must bridge at least \(r/6\) products
and \(r/6\) ratios. Separate small product or ratio sets do not prove
the required overlap between different labels.

**N4 — PROVED container; FAILED certificate.** Since
\(Q_0^2T\subset\mathcal O_L\),
\(Q_0^6P_3(T,T)\subset\mathcal O_L\). The bound
\(|\sigma(P_3)|\le4^3+4=68\) and integral-norm packing give
\[
|P_3(T,T)|\le(136Q_0^6+1)^d.
\]
For the source primes \(q_b\ge5\), this expression exceeds
\(Q_0^{6d}\ge5^{6td}>2^{2td}\ge|T|^2\).
Source: §H.2; dependencies N1 and the packing argument of C5.

The pole is genuine at a coordinate where labels vary: an active trace
has valuation \(-2\), whereas the anchored inactive trace is integral.
Their difference-cube has valuation \(-6\), and their sum has
valuation \(-2\); cancellation is impossible. Norm one therefore
does not uniformly remove cubic denominator growth. This proves failure
of the displayed full-denominator container, not of every finer count.

For real coordinates \(r_u=t(u)/2\), (N.2) gives
\(8P_3(r_u,r_v)=D^3+4E\). The useful planar identity
\[
(r_u-r_v)^2+(s_u-s_v)^2=2-t(u/v),\qquad
s_u=(u-u^{-1})/(2i),
\]
controls squared distances, not the scalar cubic. Also
\(P_3(a,a-h)=h^3+2a-h\) is injective in the anchor \(a\).
Selected unit-distance translations leave all other ordered pairs
uncontrolled; no exact same-set cubic transport is supplied.

### The missing entire support statement

**N5 — PROVED implications; OPEN source-specific premises.** Applied
to the actual trace family, an entire-image estimate
\[
\log|P_3(T_d,T_d)|\le bd+o(d),\qquad b<2\gamma,
\]
would certify every fixed
\(0<c<(2\gamma-b)/(t\log2)\), by (N.1). This is the charged
rate gate in the 11 October `A_transfer.md` §A3: divide by the squared
input lower count and use \(\log|T_d|\le(t\log2)d\).
Any thinning or parameter-to-scalar loss reduces the input rate twice
in the pair budget. No such \(b\) is established for this family.

A relative formulation is equally explicit. For fixed \(C>0\),
\(m\ge0\) and \(\kappa>0\), the source-carrier-specific premise
\[
|P_3(T_d,T_d)|\le C d^m e^{-\kappa d} n_d^2,
\qquad n_d=|T_d|,
\tag{N.3}
\]
would give every fixed \(0<c<\kappa/(t\log2)\) eventually.
Indeed \(\log n_d\le(t\log2)d\), and the strict inequality absorbs
\(\log C+m\log d\). Equation (N.3) is **OPEN** for this carrier,
not a simpler lemma already supplied by the unit-distance paper.

The exact identities N2 also give a signed-radical presentation:
\[
P_3(t(u),t(v))=
\sigma\{(p-2)(s-2)\}^{3/2}
+\tau\sqrt{(p+2)(s+2)},\qquad \sigma,\tau\in\{-1,1\}.
\tag{N.4}
\]
The radicands are nonnegative because they are \(D^2,E^2\);
the signs come from the actual \(D,E\), with coinciding choices at
zero. Only states attained by actual ordered pairs are counted, not an
independent product of product traces and ratio traces. A bound such as
(N.3) for this entire attained radical support would suffice. N2's
bounded joint fibers and N3's fixed-label root bounds do not prove it:
the required coincidences between different attained states remain OPEN.

For the existing sufficient fiber route, let \(n=|A|\) and
\(r(z)=\#\{(a,b)\in A^2:P_3(a,b)=z\}\). The exact identity
\[
|P_3(A,A)|=\sum_{(a,b)\in A^2}\frac1{r(P_3(a,b))}
\]
shows that, if all but \(O(n^{2-\kappa})\) pairs have actual full
fiber at least \(n^\epsilon\), then the image is
\(O(n^{2-\kappa}+n^{2-\epsilon})\). This includes isolated pairs
and all cross-pairs. Source: latest `C_entropy.md` §C5, equations
(C.8)–(C.9). Large collision energy or a few selected rich fibers
does not supply this tail.

For the trace carrier, N3 makes the needed overlap especially explicit.
A rich actual cubic fiber must contain a growing number of distinct
products and ratios, despite the bounded number of pairs contributed
by each one. A theorem about one product label, one direction, or a
selected principal ideal-class subfiber leaves this obligation unresolved.
Any excluded ordered pairs must be counted as exceptions in the tail;
a fixed positive fraction of excluded pairs contributes order \(n^2\)
possible outputs and therefore gives no positive exponent by this argument.
This is a necessary bookkeeping condition for this certificate, not a
new obstruction against an unidentified carrier.

The 11 October record retains **EG-O1 / NC-O1** as this OPEN actual
all-pair fiber-tail obligation; it closes only the finite CP-O1 attachment.
The separate 10 September norm–trace checkpoint concerns
\(P_0=x^2+xy+y^2+x\), not \(P_3\). Its quadratic norm identities,
conditional same-set transfer, and norm-action tests supply no cubic
support bound. No additional candidate or research assignment is created
by this report.

## 6 Fourth power restrictions and the ramified refinement

### F1 fourth power values and exact fixed polynomial transport

**PROVED, elementary identities checked here.** For an odd prime \(p\),
cyclicity of \(\mathbf F_p^\times\) gives

\[
|\{z^4:z\in\mathbf F_p\}|
=1+\frac{p-1}{\gcd(4,p-1)}.
\]

Thus primes \(p\equiv1\pmod4\) give \((p+3)/4\) values, including zero,
and density \((p+3)/(4p)\). At \(p\equiv3\pmod4\) the density is only
the square density \((p+1)/(2p)\). Prime two supplies no such saving.
Since \(L(x,y)=x+2y\) is surjective on full field inputs, these are also
the exact values of \(L^4\).

Write \(T(x,y)=3x-y\). For a fixed product of selected split primes
\(Q=\prod_{i=1}^t p_i\), the removable deformation is

\[
F_Q=L^4+Q^3T,
\qquad F_Q(Qx,Qy)=Q^4P_4(x,y).
\tag{F1.1}
\]

The coefficient is \(Q^3\), not \(Q\). At each selected prime dividing
\(Q\), \(F_Q\) reduces to \(L^4\). If \(p_i\) splits completely in a
totally real degree-\(d\) field \(K\), then
\(\mathcal O_K/p_i\mathcal O_K\cong\mathbf F_{p_i}^d\). CRT therefore
allows at most

\[
(Q\rho_4)^d\quad\text{output classes modulo }Q\mathcal O_K,
\qquad \rho_4=\prod_{p\mid Q}\frac{p+3}{4p}.
\tag{F1.2}
\]

This is quotient-ring product factorization, not probabilistic independence
or equidistribution of a bounded carrier. For a finite algebraic carrier
\(C\), choose one real embedding \(\sigma\) and set \(A=\sigma(C)/Q\).
Then (F1.1) preserves input and output cardinalities exactly. Fix the tower,
its root discriminant, the primes, \(Q\), and the real radius before the
degree grows. Chebotarev in one finite extension alone does not ensure
splitting in every tower layer.

### F2 the symmetric fourth power certificate has the wrong rate

**PROVED certificate obstruction; the actual image is OPEN.** Let
\(\operatorname{rd}(K)=D\), and use
\(C=B_K(X)=\{u\in\mathcal O_K:|\sigma_i(u)|\le X\}\).
The half-box translate-and-difference argument and norm separation give

\[
(X/\sqrt D)^d\le n:=|C|\le(2X+1)^d.
\]

Every conjugate of every output of \(F_Q\) has absolute value at most

\[
M_4=81X^4+4Q^3X.
\]

This is a valid enclosure obtained by separate estimates, not an exact
continuous radius. Distinct outputs in one class modulo \(Q\mathcal O_K\)
are \(Q\)-separated in sup norm: their difference is \(Q\) times a
nonzero algebraic integer. Cubes of side \(Q\) consequently bound each
class population by \((1+2M_4/Q)^d\). Combining this uniform bound with
(F1.2) yields

\[
|F_Q(C,C)|\le[\rho_4(2M_4+Q)]^d
\le\Theta_{4,\mathrm{sym}}(X)^d n^2,
\]

\[
\Theta_{4,\mathrm{sym}}(X)
=D\rho_4\left(162X^2+\frac{8Q^3}{X}+\frac Q{X^2}\right).
\tag{F2.1}
\]

For every \(X>0\), put \(z=X/Q\). If \(z\ge1/4\), then
\(162z^2\ge162/16>10\); if \(z<1/4\), then \(8/z>32\).
Hence the first two terms in parentheses exceed \(10Q^2\). Meanwhile

\[
\rho_4Q^2=\prod_{p\mid Q}\frac{p(p+3)}4\ge10^t,
\]

because the selected primes are \(1\pmod4\) and at least five.
Thus \(\Theta_{4,\mathrm{sym}}(X)>1\). No radius makes this particular
fully charged comparison prove compression. Adding those primes strengthens
the local defect but increases the coefficient/modulus cost even faster.

The conclusion concerns this numerical upper certificate. It does not say
the actual image equals the enclosure, give an actual-image lower bound,
or exclude a sharper count of globally realized outputs on the same carrier.

### F8 Stronger C1 statements and the correlated input boundary

**PROVED as reported in the controlling state; original main proofs unavailable for independent inspection in this report.** T02's state, §4 C1, records the following stronger results for the same deformation \(F_Q\). For the centered interval \([-X,X]\), writing \(z=X/Q\), its exact continuous width is \(W(X)=Q^4w(z)\), where

\[
w(z)=\begin{cases}
8z,&0<z\le40^{-1/3},\\
80z^4+6z,&40^{-1/3}\le z\le1/2,\\
81z^4+\tfrac{11}{2}z+\tfrac3{16},&z\ge1/2.
\end{cases}
\]

For every \(Q\ge5\), center \(b\in\mathbb R\) and radius \(r>0\), it records

\[
W_Q(b,r)\ge7Q^3r,\qquad W_Q(b,r)\ge(7r/3)^4,
\qquad W_Q(b,r)+Q\ge Q(2r+1)^2.
\]

For every prime \(p\equiv1\pmod4\) and nonempty \(E\subseteq\mathbb F_p\), the recorded local theorem is

\[
\frac{p\,|\{(x+2y)^4:x,y\in E\}|}{|E|^2}
\ge\frac{p+3}{4p},
\]

with equality exactly for \(E=\mathbb F_p\). Thus independent coordinate input restrictions cannot improve that normalized factor after both input losses. The reported sharper interval certificate has

\[
\Theta_{4,\mathrm{int}}(X)=D\rho_4\frac{W(X)+Q}{X^2}
>9(80/3)^{1/3}D\rho_4Q^2>1.
\]

Its translated/anisotropic full-interval envelope obeys
\(U=\rho_4^d\prod_i(W_i+Q)\) and
\(U/|C|^2\ge(\rho_4Q)^d\ge2^{td}\).
The main C1 proof is identified by the recovery package but was not received locally. These precise statements are recorded as reported results, not substituted for the inspected proofs of F2–F5.

**PROVED; complete available proof for the correlated finite case.** The located `phase_c2/C1_STATUS_ADDENDUM.md`, §2, proves that for every nonempty \(S\subseteq\mathbb F_5^2\), with \(n=|S|\),

\[
H_5(S)=\{(x+2y)^{\circ4}:x,y\in S\},\qquad
\frac{25|H_5(S)|}{n^2}\ge\frac4{25},
\]

with equality only for \(S=\mathbb F_5^2\).

**Proof.** If \(n\le12\), nonemptiness gives the strict lower bound \(25/144>4/25\). If \(n\ge13\), the sets \(S\) and \(z-2S\) intersect for every \(z\) in the group of order 25, so \(S+2S=\mathbb F_5^2\). Coordinatewise fourth powers then give exactly \(\{0,1\}^2\), with four values. The normalized factor is \(100/n^2\ge4/25\), with equality only at \(n=25\). \(\square\)

**OPEN.** The corresponding all-prime/all-dimension inequality

\[
\frac{p^d|\{(x+2y)^{\circ4}:x,y\in S\}|}{|S|^2}
\ge\left(\frac{p+3}{4p}\right)^d,
\qquad \varnothing\ne S\subseteq\mathbb F_p^d,
\quad p\equiv1\pmod4,
\]

is not established by the finite case. Even a useful opposite defect would still require a compatible real realization and a positive fully charged global rate.

The same available addendum, §1, explains why a weak exponential deficit relative to a full class container can follow from the trivial pair bound: for \(r>\max(Q,\sqrt D)\), its reported width lower bound makes the container base larger than \((2r+1)^2\). This weak deficit supplies no proof that the saving exceeds \(\log\Theta_{4,\mathrm{int}}\). An improvement measured against an oversized envelope must cross the actual rate threshold before it certifies compression. No enumeration is a premise of these conclusions.


### F7 the C2 reduction and C3 universal one level optimum

**PROVED in the identified source system; the complete analytic proof was
read and its case argument checked here.** In the characteristic-seven ring
\(R=\mathbf F_7[\pi]/(\pi^3)\), assume \(7\nmid Q\) and put
\(s=Q^3\bmod7\in\{1,-1\}\). Since
\(L+2T=7x=0\), \(L=-2T\), so for **every nonempty** \(E\subseteq R\),

\[
F_Q(E,E)=h_s(3E-E),\qquad h_s(z)=2z^4+sz.
\tag{F7.1}
\]

This is an exact quotient-ring identity, not a characteristic-zero identity.
C2's integral determinant-seven graph encodes the same relation: for a unit
\(u\), the map \((t_1,t_2)\mapsto(ut_1+2t_2,3ut_1-t_2)=(a,b)\) has
image exactly \(a+2b\in7\mathcal O\), of index \(7^d\). The graph index
and its scalar consequence \(h_s\) are not independent savings.

Expansion gives

\[
h_s(a+b\pi+c\pi^2)
=h_s(a)+(a^3+s)b\pi+[(a^3+s)c+5a^2b^2]\pi^2.
\tag{F7.2}
\]

The residue map is a permutation. The three critical residues are
\(K_1=\{3,5,6\}\), \(K_{-1}=\{1,2,4\}\), defined by \(a^3=-s\).
Each of the other four branches is bijective in its two nilpotent digits.
Each critical branch keeps only the square of the first digit. Disjoint
output residues therefore give \(|h_s(R)|=4\cdot49+3\cdot4=208\).

Charge both input fractions by setting
\(\Phi_s(E)=343|h_s(3E-E)|/|E|^2\). C3 proves all three sharp statements:

\[
\min_{\varnothing\ne E\subseteq R}\Phi_s(E)=4/7,
\tag{F7.3}
\]

with equality exactly at the three full critical fibers \(a+\pi R\);

\[
\min_{E\text{ meets at least two residue fibers}}\Phi_s(E)=208/343,
\tag{F7.4}
\]

with equality only at \(E=R\); and, excluding the three extremizers,

\[
\min\Phi_s(E)=343/576,
\tag{F7.5}
\]

with equality exactly at a full critical fiber minus one point.

Here is the complete case structure. Write \(n=|E|\). In a single regular
input fiber, fixing one input gives \(|3E-E|\ge n\), and the corresponding
argument fiber is regular because \(2^3=1\); thus \(\Phi_s(E)\ge343/n\ge7\).
In a single critical fiber, let \(T_1\subseteq\mathbf F_7\) be its first
nilpotent-digit support, of size \(t_1\). Then \(n\le7t_1\), and the
output count is exactly \(|\{b^2:b\in3T_1-T_1\}|\). Cauchy-Davenport,
in the precise form \(|U+V|\ge\min(7,|U|+|V|-1)\), and the at-most-two
fibers of squaring give at least \(\min(t_1,4)\) outputs. For \(t_1\le6\)
the resulting normalized cost is at least \(7/9\). For \(t_1=7\), it is
exactly \(1372/n^2\), minimized only at \(n=49\).

For a multifiber set, every input residue touches a regular argument branch.
A regular residue uses the diagonal argument \(2a\). For a critical
\(a\) and another residue \(b\), if both \(3a-b\) and \(3b-a\) were
critical, putting \(t=b/a\) would give
\((3-t)^3=(3t-1)^3=1\). Their difference is \(t-t^2=0\), whose two
possibilities either fail the first equation or contradict \(a\ne b\).
On a regular branch reached from input fibers of sizes \(n_a,n_b\),
fixing either input gives at least \(\max(n_a,n_b)\) distinct outputs.
Summing these disjoint regular branches gives at least \(n/3\): with two
or three input residues use a largest fiber; with four, Cauchy-Davenport makes all seven argument residues occur, so use its contribution
and the three remaining branches: writing \(M,m\) for the largest and
smallest fiber sizes, their contribution is at least \(M+3m\), while
\(n\le3M+m\), so it is at least \(n/3\). With at least five a largest fiber touches
at least \(k-3\ge k/3\) regular branches.

For \(n\le171\) this yields \(\Phi_s(E)\ge343/(3n)>208/343\).
For \(n\ge172\), the two size-\(n\) sets \(3E\) and \(z+E\) intersect
for every \(z\in R\), so \(3E-E=R\) and
\(\Phi_s(E)=343\cdot208/n^2\ge208/343\), with equality only at \(n=343\).
This proves (F7.3)–(F7.4). Outside their extremizers, the only remaining
case able to attain (F7.5) is a critical fiber with all seven first digits
and \(n\le48\): \(1372/48^2=343/576\), attained by every one-point
deletion. For complete unions \(E=A+\pi R\), the source also gives the
exact formula \(|F_Q(E,E)|=49r+4c\), where \(r,c\) count regular and
critical residues in \(3A-A\), and
\(\Phi_s(E)=(49r+4c)/(7|A|^2)\). The gap above \(4/7\) is exactly
\(97/4032\). Moreover \(\Phi_s(E)<208/343\) forces 48 or 49 points in
one critical fiber, since \(1372/47^2>208/343\). These are exact discrete
stability statements, not asymptotic hypotheses.

These analytic arguments cover all subsets; the historical structured screen
is not their proof. No screen or supplied program was rerun here. The sharp
minimum applies to the 343-element ring only: F3's higher-level full-fiber
count improves it once, without proving any universal higher-level optimum.

### F3 the complete C4 local theorem and its saturation proof

**PROVED in the identified source system; its analytic argument is inspected
and checked below.** C4 uses a separate ramified-seven refinement with
\(Q=1\). Let \(\mathcal O\) be the valuation ring of the actual local
cubic, with maximal ideal \(\mathfrak p\), ramification index three and
residue degree one:

\[
7\mathcal O=\mathfrak p^3,\quad
\mathcal O/\mathfrak p=\mathbf F_7,\quad
|\mathcal O/\mathfrak p^r|=7^r.
\]

For \(\alpha\in\{3,5,6\}\), so \(\alpha^3=-1\bmod\mathfrak p\), set
\(\mathcal E=\alpha+\mathfrak p\),
\(R_m=\mathcal O/\mathfrak p^{3m}=\mathcal O/7^m\mathcal O\), and
\(E_m=\mathcal E\bmod\mathfrak p^{3m}\).
Then \(|R_m|=7^{3m}\), \(|E_m|=7^{3m-1}\), and

\[
N_m:=|P_4(E_m,E_m)|=
\begin{cases}4,&m=1,\\22\,7^{3m-4},&m\ge2.\end{cases}
\tag{F3.1}
\]

To prove this for the entire Cartesian image, use the bijection
\((x,y)\mapsto(L,x)\), \(L=x+2y\),
from \(\mathcal E^2\) to
\((3\alpha+\mathfrak p)\times(\alpha+\mathfrak p)\).
The inverse is \(y=(L-x)/2\); two is a unit. Over the actual valuation ring,

\[
P_4(x,y)=g(L)+\tfrac72x,
\qquad g(L)=L^4-\tfrac12L,
\]

\[
P_4(\mathcal E,\mathcal E)
=g(3\alpha+\mathfrak p)+\tfrac72\alpha+\mathfrak p^4.
\tag{F3.2}
\]

Equality holds because the independent \(x\)-parameter fills the entire
ideal \((7/2)\mathfrak p=\mathfrak p^4\). This is precisely why there
can be no further higher-digit saving for these full inverse images.

Put \(L_0=3\alpha\), \(A_0=6L_0^2\), \(B_0=4L_0\), and
\(\omega=P_4(\alpha,\alpha)\). The coefficient \(A_0\) is a unit, and
\(g'(L_0)=4L_0^3-1/2\in7\mathbf Z_7\subset\mathfrak p^3\), since
\((3\alpha)^3=1\bmod7\). Taylor expansion, for \(u\in\mathfrak p\), gives

\[
g(L_0+u)-g(L_0)\equiv A_0u^2+B_0u^3\pmod{\mathfrak p^4}.
\]

Choose a uniformizer \(\pi\) and write
\(u=\pi b+\pi^2c\bmod\mathfrak p^3\), with digits \(b,c\in\mathbf F_7\).
The expression becomes

\[
A_0b^2\pi^2+(2A_0bc+B_0b^3)\pi^3\pmod{\mathfrak p^4}.
\]

For \(b=0\) there is one class. For \(b\ne0\), the leading square
has three distinct nonzero values, and varying \(c\) fills all seven
next digits because \(2A_0b\ne0\). Hence exactly \(1+3\cdot7=22\)
classes occur modulo \(\mathfrak p^4\). Multiples of seven in coefficients
of \(\pi^2\) and \(\pi^3\) have valuations at least five and six,
respectively, so digit reduction loses no mixed-characteristic carry.

Equivalently the actual infinite local support is the disjoint union

\[
(\omega+\mathfrak p^4)
\ \cup\ \bigcup_{i=1}^3
(\omega+A_0\pi^2b_i^2+\mathfrak p^3),
\tag{F3.3}
\]

where \(b_i^2\) are the three nonzero quadratic residues. Reducing this
support gives four classes modulo \(\mathfrak p^3\), and 22 fully filled
classes modulo \(\mathfrak p^4\). Each latter class has
\(7^{3m-4}\) descendants, proving (F3.1),
\(N_2=49+3\cdot343=1078\), and \(N_{m+1}=343N_m\) for \(m\ge2\).
For \(m\ge2\), \(R_m\) has characteristic \(7^m\); replacing it with
\(\mathbf F_7[\pi]/(\pi^{3m})\) would be invalid.

### F4 both input costs and the rational-modulus rate

**PROVED count and FAILED positive-rate certificate.** The raw output
density for \(m\ge2\) is \(22/7^4\). Each input fraction is \(1/7\);
charging both gives

\[
\Psi_m=\frac{N_m/|R_m|}{(|E_m|/|R_m|)^2}
=\begin{cases}4/7,&m=1,\\22/49,&m\ge2.\end{cases}
\tag{F4.1}
\]

There are \(d/3\) independent local cubic blocks, not \(d\) copies of
this ramified quotient. The per-degree local gain therefore improves once
from \(\frac13\log(7/4)\) to \(\frac13\log(49/22)\), then stabilizes.
This is not optimization over arbitrary higher-level subsets.

The required ramified tower is a separate adaptation, not an assertion
that the rational prime seven splits completely. The original cyclic
cubic base includes the conductor prime seven and has one prime
\(\mathfrak p\) over it, with \(7\mathcal O_F=\mathfrak p^3\).
If its unramified pro-3 group has ranks \(d_0\ge\ell-1\) and
\(r_0\le d_0+C_0\), killing a Frobenius at \(\mathfrak p\) gives
generator rank at least \(d_0-1\) and relation rank at most
\(d_0+C_0+1\). A Frattini element preserves generator rank; a
non-Frattini element can be included in a generating basis and its
generator eliminated in a free pro-3 presentation. For fixed sufficiently
large \(\ell\),

\[
d_0+C_0+1<(d_0-1)^2/4,
\]

so Golod-Shafarevich keeps the quotient infinite. Only the prime of the
base is forced to split in the relative layers; the original ramification
index remains three. This is the construction proved in C3 §7, with its
generator-elimination correction retained in the C2 precision addendum.
The resulting tower has
\(7\mathcal O_{K_j}=\prod_{k=1}^{d/3}\mathfrak P_{j,k}^3\), constant
\(D\ge7^{2/3}\), and identical local completions because the base prime
splits in every relative layer. Set

\[
\mathfrak I_j=\prod_k\mathfrak P_{j,k},\quad
N\mathfrak I_j=7^{d/3},\quad
C_j=-1+B_{\mathfrak I_j}(X).
\]

The ideal lattice has covolume \(7^{d/3}D^{d/2}\). Applying the half-box
argument to this lattice gives

\[
e^{ad}\le|C_j|\le e^{Bd},\qquad
a=\log X-\tfrac13\log7-\tfrac12\log D,\quad B=\log(2X+1).
\]

Fix \(X=2\,7^{1/3}\sqrt D\), giving \(a=\log2\). The bounded carrier
is contained in the critical fibers; surjectivity onto them is neither
asserted nor needed. A real embedding preserves all cardinalities.
The directly proved C3 width on \([-1-X,-1+X]^2\) is

\[
W=81(X+1)^4+\tfrac32X+\tfrac{27}{16}.
\]

It comes from the convex maximum at a vertex and the one-variable minimum
of \(w^4-w/2\) at \(w=1/2\). This proof works at \(Q=1\) and uses
no missing C1 inequality. CRT and uniform separation give

\[
|P_4(C_j,C_j)|\le U_m=N_m^{d/3}(1+W/7^m)^d.
\]

With \(C_*=(22/49)^{1/3}\), its signed rate is

\[
\kappa_m=2a-\frac1d\log U_m
=\log\frac{X^2}{DC_*(W+7^m)}\qquad(m\ge2).
\tag{F4.2}
\]

For the diagonal polynomial \(d(t)=P_4(t,t)=81t^4+2t\),
the average of the endpoint values minus the center value is

\[
\frac{d(b+r)+d(b-r)}2-d(b)=486b^2r^2+81r^4.
\]

This quantity is at most the full continuous width, so that width is
at least \(81r^4\).
Thus
\((W+7^m)/X^2\ge81X^2+7^m/X^2\ge18\,7^{m/2}\), and

\[
\kappa_m\le-\log(18DC_*7^{m/2})<0.
\]

The same argument makes
\(\kappa_1\le-\log[18\sqrt7D(4/7)^{1/3}]<0\).
Level two can improve a negative level-one estimate; all levels above
two strictly worsen (F4.2) at fixed radius. The ledger charges two windows,
both ideal restrictions, discriminant, occupied classes, and worst-class
population. Translation is in \(W\); units, regulators, ratios, parameter
fibers, denominator clearing and exceptions are inapplicable to this direct
integral additive carrier. Mixed-characteristic carries were retained in F3.

For clarity, the construction ledger's nonzero contributions, in natural
logarithms per field degree, are exactly

| Entry | Contribution to the signed rate for \(m\ge2\) |
|---|---|
| Two input windows | \(+2\log X\) |
| Critical input thinning, twice | \(-\frac23\log7\) |
| Field discriminant | \(-\log D\) |
| Exact output classes | \(-\frac13\log N_m\) |
| Uniform population within each class | \(-\log(1+W/7^m)\) |
| Translation and coefficient height | Included in the proved width \(W\) |
| Real projection and parameter fibers | Zero loss: field embedding and translation are injective |
| Exceptional or uncovered outputs | None; every ordered pair is covered |

Only the tower layer varies. The radius and the chosen rational precision
are fixed beforehand; taking a degree-dependent precision does not convert
the already saturated density into a new saving. If a new subcarrier lost
input rate \(\eta\), its pair budget would lose \(2\eta\). A replacement
output rate \(c_{\mathrm{eff}}\) would need
\(c_{\mathrm{eff}}<2(a-\eta)\), with all additional branches and exceptions
included. Then only exponents strictly below
\([2(a-\eta)-c_{\mathrm{eff}}]/B\) are automatically certified when
subexponential errors occur. None of F3's local proportions supplies this
missing inequality.

### F5 saturation, mixed depth, and the exact retirement scope

**PROVED obstruction for the specified full-support/full-interval envelopes.**
The saturation ideal gives the sharper valid certificate

\[
U_{\mathfrak I^4}=22^{d/3}(1+W/7^{4/3})^d,
\quad
\kappa_{\mathfrak I^4}
\le-\log(18\,22^{1/3}D)<0.
\]

Using three shallow choices and one deep choice in every factor gives

\[
U_{\mathrm{mix}}
=\sum_{k=0}^{d/3}\binom{d/3}{k}3^{d/3-k}
(1+W/7^{1+k/d})^d.
\]

All branches are included. Its all-shallow term already yields
\(2a-d^{-1}\log U_{\mathrm{mix}}
\le-\log[18\sqrt7D(3/7)^{1/3}]<0\).

More generally, let integral-ideal cosets, supported at seven, cover the
**entire product** of the local supports (F3.3). In a common finite quotient,
the product occupies fraction \((22/7^4)^{d/3}\); a coset of an ideal
\(J_\ell\) occupies fraction \(1/NJ_\ell\). Subadditivity gives
\(\sum_\ell1/NJ_\ell\ge(22/7^4)^{d/3}\). Consequently their uniform
full-interval envelope satisfies

\[
U_{\mathrm{cover}}
=\sum_\ell(1+W/(NJ_\ell)^{1/d})^d
\ge W^d(22/7^4)^{d/3}.
\]

This also fails against actual nontrivial equal-radius critical-coset
population. Ideal separation gives \(|C|\le(1+2r/7^{1/3})^d\);
\(|C|>1\) forces \(z=2r/7^{1/3}\ge1\). Together with \(W\ge81r^4\),

\[
U_{\mathrm{cover}}/|C|^2
\ge[81\,22^{1/3}z^4/(16(1+z)^2)]^d
\ge[81\,22^{1/3}/64]^d>3.54^d.
\]

These are lower bounds on numerical envelopes, never on the actual image.
The hypotheses include entire local product support, full continuous
intervals on every branch, uniform ideal-norm packing, and the stated input
population normalization. A proper subset of globally realized residues,
smaller branch-dependent real widths, correlated factors, arbitrary deeper
input subsets, or another carrier lies outside this retirement. The local
theorem alone supplies none of these improvements. The illustrative floor
\(D=7^{2/3}\) is not a claim that the constructed tower attains that value.

### F6 degree four can succeed, without solving T02

**PROVED elementary consequences.** A quadratic polynomial with compressed
image remains compressed after composition with any fixed univariate
polynomial. For the reconstructed rank-one quadratic baseline
\(f(x,y)=x+y+(x-y)^2\), the degree-four polynomial \(f(x,y)^2\) satisfies
\(|f(A,A)^2|\le|f(A,A)|\) on the same witnesses. Likewise pure
\((x-y)^4\) has exactly \(n\) values on \(A=\{0,\ldots,n-1\}\).
More generally, fixed integer linear forms raised to a power have \(O(n)\)
image on integer progressions. These are composition/additive-form examples,
not transverse quartic mixtures such as T02. Degree alone is not the boundary.

The broader C1 translated/anisotropic interval theorem and independent
coordinate-thinning inequality are **PROVED as reported in the controlling
record**, but their complete original main proof was not received in the
curated local supplement. The recovery addendum identifies a larger package
whose original files were not part of the received intake. This chapter does
not independently verify that unavailable proof or use it as a dependency of
F2–F5; the symmetric obstruction and C4/C3 arguments above are inspectable.

## 7 Construction ledgers and the surviving support requirements

These ledgers apply the repository's construction-ledger template to the mechanisms actually described above. A missing support improvement is marked OPEN. Inapplicable costs are explained, rather than silently omitted.

### The exact quantitative comparison

| Mechanism | Lower input rate \(a\) | Full output certificate rate \(b\) | Gap furnished by the certificate |
|---|---|---|---|
| Centered rank-one quadratic | \(\log X-\tfrac12\log D\) | \(\log\rho+\log(2H_2+Q)\) | Positive after the original finite-list parameter choice; Q1–Q2 |
| Side-length cubic rectangle, denominator \(p\) | \(\log X-\tfrac12\log R\) | \(\log\delta_{p,2}+\log[p^2+2\max(X^3,p^2X)]\) | \(2a-b=-\log\beta_p(X)<0\); C5–C6 |
| Symmetric T02 fourth-power box | \(\log X-\tfrac12\log D\) | \(\log\rho_4+\log(162X^4+8Q^3X+Q)\) | \(2a-b=-\log\Theta_{4,\mathrm{sym}}(X)<0\); F2 |
| Ramified-seven C4 carrier | \(\log X-\tfrac13\log7-\tfrac12\log D\) | \(\tfrac13\log N_m+\log(1+W/7^m)\) | Negative for every fixed precision in the specified full-interval certificate; F4–F5 |
| Source norm-one traces | \(\gamma=t\log2-\log H\) | Existing enclosure: \(\log(136Q_0^6+1)\) | No saving; the actual output rate is OPEN; N4–N5 |

All use upper input rates as well: centered boxes use \(B=\log(2X+1)\); the cubic side-length rectangle uses \(B=\log(X+1)\); source traces use \(B=t\log2\). A positive asymptotic gap \(\delta=2a-b\) certifies every strict \(c<\delta/B\). Only the exact finite inequalities in Q1–Q2 justify their displayed boundary exponents without extra control.

### Where each cost is paid

| Cost or gain | Quadratic and cubic additive boxes | Symmetric and ramified quartic carriers | Norm-one trace carrier |
|---|---|---|---|
| Input lower and upper counts | G2 or translated averaging; the lower count pays \(D^{d/2}\) | G2; C4 ideal lattice also pays \(7^{d/3}\) per input | Actual ideal-class fiber yields \(e^{\gamma d}\); trace injectivity and the binary upper bound give actual scalar counts |
| Input thinning twice | Zero for full additive boxes; C8 charges a code's density squared | Zero for F2; C4 charges \(7^{-2d/3}\); deeper subsets require a fresh count | Class-number loss is already in \(\gamma\); any additional loss \(\lambda\) changes the pair budget to \(2(\gamma-\lambda)\) |
| Field degree and discriminant | Degree grows last; \(\log D\) is a cost in the normalized output comparison | Same, with \(d/3\) actual ramified blocks in C4 | Degree is \([L:\mathbb Q]\), not \([L(i):\mathbb Q]\); bounded discriminant enters the retained class-number bound |
| Local moduli and splitting | G4 gives the actual quotient coordinates; local powers and precision are fixed | F2 uses split primes; C4 uses ramification index three and relative splitting, not \(d\) copies of \(\mathbb F_7\) | Original split prime pairs generate valuation labels; no new local output saving is assumed |
| Denominators and transport | \(Q\), \(M\), and the cleared coefficients occur in the radius and packing modulus; exact common scaling has no fiber loss | \(Q^3\) occurs in F2's height; C4 with \(Q=1\) is integral | Pole denominator \(Q_0^2\) becomes \(Q_0^6\) for cubic outputs; trace embedding is injective, but the enclosure remains expensive |
| Coefficient height and archimedean distortion | Explicit \(H_2\) or exact coupled cubic width; no unit distortion | Explicit \(81X^4+4Q^3X\), or the proved translated width \(W\) | Every trace conjugate is bounded by two, and outputs by 68; bounded radius does not erase poles |
| Regulator and class group | Regulator inapplicable and no class selection of these additive carriers | Inapplicable to the direct integral additive carriers; original arithmetic supply is separately sourced | Regulator inapplicable; class-number cost is essential and charged once in input supply |
| Branches, ratios and carries | Full output classes are counted; C8's correlated code is charged as one actual code | All C4 local classes and mixed-depth branches are counted; actual characteristic \(7^m\) preserves carries | Joint product/ratio labels have quadratic support; the signed branches are attained by actual ordered pairs; their further collapse is OPEN |
| Parameter and real projection fibers | Zero loss: one real field embedding and scalar multiplication are injective | Zero loss for the same real embedding and translation/scaling | Zero loss for the actual anchored binary trace family; other scalarizations need proved fiber bounds |
| Exceptions and uncovered pairs | None in the displayed full-square bounds | None in the displayed full-square bounds | None in the enclosure; every exception in a proposed support or tail theorem must be charged |
| Additional actual-support saving | Established only for the quadratic comparison | OPEN beyond the retired certificates | OPEN; neither selected edges nor energy supplies it |

A direct exact-output encoding can avoid paying a full ambient packing capacity. Its cardinality must be proved from actual equalities and cover every scalar ordered pair. Poles and other arithmetic constraints still govern the realization; they do not disappear because a cardinality proof is proposed.

### What a replacement theorem must actually say

For the source trace carrier, N5 states the concrete missing bound

\[
|P_3(T_d,T_d)|\le C d^m e^{-\kappa d}|T_d|^2,
\qquad \kappa>0,
\]

on an unbounded sequence of layers, with all constants fixed. The source upper count then certifies every \(c<\kappa/(t\log2)\). This is a conditional subproblem restricted to that carrier, not an established simplification of T01. Its rich fibers must connect many products and ratios by N3. The existing broader EG-O1/NC-O1 obligation is the actual full-fiber tail in G8; it includes isolated and unprescribed pairs.

For the C4 quartic carrier, if an actual subcarrier loses rate \(\lambda\), a new branch-dependent all-pairs cover needs total output rate \(b_{\mathrm{eff}}<2(a-\lambda)\). The input loss, every branch, its actual residue population and real width, and every exceptional pair must all enter that inequality. The stabilized local proportion \(22/49\) alone supplies no such bound.

For a full-rank quadratic, Q3 blocks unrestricted first-level square-residue compression at good primes. Q4's higher-power densities, a restricted-input norm identity or a solvable-extension realization become useful only after their hypotheses and global costs are proved for one real same-set carrier. Completing a quadratic norm or obtaining many norm-one actions supplies algebra, not automatically a small support.

## 8 What the mechanism establishes and what it leaves open

Chebotarev selects suitable primes at a finite extension. The original group's relation calculation then enforces their splitting in every layer while keeping the tower infinite. CRT repeats a proved local restriction across actual residue coordinates. Uniform per-class packing controls all arithmetic lifts. The final step is a positive fully charged rate followed by an injective same-set real transport. Each arrow has its own statement above.

The quadratic proof completes every arrow. For the audited cubic and fourth-power routes, the rate comparison fails even though the local defects and tower are valid. A failed numerical certificate is not a lower bound on occupied outputs, a proof of near-quadratic expansion on every real set, or an impossibility theorem by degree. Quartic composition and pure integral-linear powers give explicit positive counterexamples to any degree-only impossibility claim.

The stronger infinite-prime tower in the remarks is useful arithmetic infrastructure, but it does not remove coefficient heights, modulus spacing, squared input losses or full-pair coverage requirements. Likewise, the original unit-distance edge count does not upper-bound the support of a scalar cubic. Its norm-one trace import remains OPEN at the exact output-counting step.

The report uses no sum-product exponent as a polynomial compression exponent. The additive-box/unit-box construction and its published quantitative saving concern a different factorization and cost ledger. The source arithmetic does not print numerical values for all relation-rank and class-number constants or one numerical admissible \(\ell\); the positive quadratic exponents here are symbolic fixed constants after the parameter choice, not asserted numerical records. No novelty conclusion, independent external review, new mathematical experiment or new construction is claimed.

## 9 Source availability and verification

The original unit-distance PDF, corrected C0 with its correction log, the complete cubic checkpoint and continuous-cover proof, and C2–C4 analytic quartic reports are locally present and their relevant arguments were inspected. The original C1 quartic report and some broader recovery-package artifacts are absent from the received local supplement. Stronger C1 assertions are retained as reported state and are not dependencies of the proofs above. The identified external number-theory references behind the original paper have not all been independently read or reproved. These boundaries are recorded in the [claim and source ledger](claim-ledger.md) and the existing migration conflict register.

The earlier 11 October transfer note recorded Pohoata as unavailable in its offline cache. The present report's source comparison uses the primary v2 text accessed during this conversation. The earlier file remains unchanged; its historical availability claim was true for that task and is not silently rewritten. No theorem is inferred from a missing title or retrospective review acceptance. A later same-date torsion-compatible sharing note and append-only registry updates appeared concurrently. That separate elliptic branch lies outside this report's mechanism audit; the source versions and scopes used here remain explicit, and T01 remains OPEN.

The report is a consolidation and source/algebra audit. Packaging checks validate files and references; they do not prove the research targets. This task creates only this dated report directory. Historical sources, canonical manifests, SPECs, STATUS files and inherited uncommitted work are preserved. The [verification record](verification.md) lists the actual checks and their results.
