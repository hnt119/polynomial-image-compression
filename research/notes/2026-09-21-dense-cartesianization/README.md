# Bottom line

**Dense Cartesianization for the Eisenstein quadratic — research report, 21 September 2026.**

- Five mechanisms were examined: split multiplicative indexing, complete block transitions, direct matrix invariance and digit products, rectangular symmetrization, and growing one-axis additive thickening.
- Split-product certificates cover at most $O(n^{3/2})$ pairs per bounded-fiber state. Complete-block partitions leave at least $n^2/k^2$ uncertified pairs. Neither meets the required almost-full coverage gate at subexponential state cost.
- In the explicit depth-two thickening, $n=90$, only **18** pairs have at least four distinct returns, and **8,082** pairs lie below that threshold. Its engineered subset has 81 pairs; engineered membership and high returns are different quantities.
- Those 18 controlled pairs have return distribution $4:8,\ 6:8,\ 9:2$ and median six. On the full square, 8,060 pairs have one return. The faithful ternary digit carriers have one distinct return everywhere under the selected actions.
- No tested construction has a proved power-saving bad-pair bound. In the scoped symbolic certificates the bad set has quadratic exponent; the explicit digit family's bad set is the entire square at every threshold greater than one.
- HR-1 therefore gives no fixed power saving here. Separately, the faithful bounded-digit theorem proves the actual lower bound $|Q(A,A)|\ge n^2/81$ for the explicit ternary family. This lower bound is not asserted for the thickening or the old orbit projection.
- The strongest general obstruction is $|A^2\cap M_u^{-1}(A^2)|\le\lfloor(3n^2+1)/4\rfloor$ for every $N(u)=1$, $u\ne\pm1$. It rules out overlap tending to one for a single mixing action, but leaves many actions with different partial-return domains open.
- The one next obligation is **DC-O1: construct a high-overlap rectangular return witness for the proved symmetrization lemma**, with a fixed positive return exponent and a power-saving rectangular bad set. The precise single obligation appears at the end.

## CARTESIANIZATION FAIL

This verdict concerns the architectures and certificates specified below.
It is not a universal impossibility theorem. No carrier was selected for
further asymptotic development after the coverage/return gate. The
rectangular-to-same-set implication is proved; its required witness is open.

$$\boxed{
\text{distinct units}
\xrightarrow[\text{examined certificates}]{\mathrm{FAILED}}
\text{dense Cartesian pairs}
\xrightarrow[\text{compatible witness missing}]{\mathrm{OPEN}}
\text{many pair returns}
\xrightarrow{\mathrm{PROVED}}
\text{large }Q\text{-fibers}
\xrightarrow[\text{power-saving bad set}]{\mathrm{PROVED}}
\text{power saving}.}$$

The final arrow is the **conditional implication** HR-1, not an achieved
power-saving theorem. The second arrow requires legal action membership,
not just a dense set of coordinate labels.

## 1. Scope, evidence and preserved state

This is the newly commissioned constructive cycle in the user's
`d6bb1cda-2aea-4257-86a7-92ed5e800146` dense-Cartesianization attachment.
It was conducted **strictly offline**. No literature search, external API,
database, outside theorem import, or novelty claim was used. All new
arguments below are elementary local proofs. No external input was needed.

The fixed polynomial remains $Q(x,y)=x^2+xy+y^2$ on one common finite
real set. The earlier
[20 September checkpoint](../2026-09-20-cartesian-norm-freeze/Cartesian_Norm_Symmetry_Research_Checkpoint.md)
is historical context, not authorization to repeat its searches. This
new assignment authorizes the five new mechanisms below. Earlier T03
proofs, data and frozen reports are preserved byte-for-byte.

**Inherited PROVED results used without rerunning their searches:**
[UE-P1–UE-P3](../2026-09-16-unit-exponent/primary-proof.md) supply distinct
multipliers, rich orbit returns and injective seed-$1$ coefficient maps;
[HR-1](../2026-09-16-high-return/return-lemma.md) supplies the support
implication. The old secondary valuation-box image formula is unchanged
and is not used as a premise for a new family.

The T03 target, ARG, eventual TCRC and RC15/4 remain **OPEN**. HR-N1
remains **FAILED / DISPROVED**. This cycle does not attempt the adaptive
RC15/4 obligation, optimize $A-A$, or transfer a nonexistent homogeneous
saving to $Q+x$. Current-state exports and the frozen checkpoint are used
for those status statements; the new proof companions are the evidence
for the new claims. No missing F25 source is needed.

### Claim and proof index

Every claim is dated 21 September 2026, T03/dense Cartesianization, fixed
$Q$ on real inputs. Each linked companion records exact quantifiers,
hypotheses, dependencies, proof and costs. Content hashes are recorded in
the [verification record](verification.md).

| ID | Status | Identified proof |
|---|---|---|
| DC-S1/S2 | PROVED; scoped split-product certificate FAILED | [Split indexing](split-index.md), §§1–4 |
| DC-B1/B2 | PROVED; complete-block partition certificate FAILED | [Blocks and rectangles](block-rectangle.md), §§2–3 |
| DC-R1/R2 | PROVED sufficient implications; construction premises OPEN | [Blocks and rectangles](block-rectangle.md), §§4–5 |
| DC-M1 | PROVED universal single-action defect | [Matrix products](matrix-product.md), §§1–2 |
| DC-M2/M3 | PROVED tensor overlap and necessary action budget | [Matrix products](matrix-product.md), §§3–4 |
| DC-M4/M5 | PROVED full-image lower bound under faithful bounded-digit hypotheses; explicit carrier FAILED | [Matrix products](matrix-product.md), §§5–5.1 |
| DC-A1 | PROVED one-axis engineered coverage bound; certificate FAILED | [Additive thickening](additive-thickening.md) |
| DC-E1 | EXPERIMENTAL, exact exhaustive four-case diagnostic | §8 below and [frozen data](../../../examples/2026-09-21-dense-cartesianization.json) |
| DC-O1 | OPEN; one retained obligation | Final section |

## 2. Exact coefficient action, returns and old sparsity

Fix $\omega=(-1+i\sqrt3)/2$, so $\omega^2+\omega+1=0$. The map
$(x,y)\mapsto x-\omega y$ is injective on $\mathbb R^2$, and
$N(x-\omega y)=Q(x,y)$, where $N(z)=z\bar z$.

### Mathematical statement

For $u=a+b\omega$, $a,b\in\mathbb R$, direct multiplication gives

$$u(x-\omega y)=(ax+by)-\omega[-bx+(a-b)y],$$
$$M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},\qquad
\det M_u=N(u)=a^2-ab+b^2.$$

When $N(u)=1$, this action preserves $Q$. For a finite set $U$ of
**actual distinct** norm-one multipliers, define

$$R_{\rm action}(p)=|\{u\in U:M_up\in A^2\}|,\qquad
R_{\rm pair}(p)=|\{M_up:u\in U,\ M_up\in A^2\}|.$$

These counts agree at every nonzero pair, by cancellation of
$x-\omega y\ne0$. At zero all multipliers fix the same pair, so
$R_{\rm pair}(0,0)=1$ if $U$ is nonempty. Labels fixing zero cannot
be counted as distinct returns.

For a threshold $R>1$, let $\mathcal G=\{p:R_{\rm pair}(p)\ge R\}$,
$G=|\mathcal G|$, and $B=n^2-G$. HR-1 gives

$$\boxed{|Q(A,A)|\le n^2/R+B.}\tag{1}$$

Indeed, every output outside the image of the bad pairs has a fiber
containing at least $R$ distinct returned pairs. These fibers are
disjoint in $A^2$. At most $B$ further outputs come from bad pairs.
One may instead charge their actual output set if it is separately
controlled; no such additional compression is assumed here.

### What it means

The established orbit has $M=3^d$ engineered points and $n=2M$ distinct
coefficient values, hence $M/(4M^2)=1/(4M)$ engineered density.
**Cartesian completion squares the coefficient-set size, while the
engineered orbit grows only linearly in the number of coefficient labels.**

### Why it matters

One structured point has one coefficient pair, not many. Increasing
action labels does not cover the missing cross-pairs. New constructions
must either reuse coordinates substantially or make actions return on
many different parts of the full square. If $R\ge n^\varepsilon$ and
$B\le Cn^{2-\delta}$, every strict $0<c<\min(\varepsilon,\delta)$
follows eventually from (1). A constant positive bad fraction does not
pass this particular pair-exception certificate.

## 3. Split exponent indexing — a determinant obstruction

### Mathematical statement

Suppose one state encodes legal cells by

$$x_i-\omega y_j=c+v_iw_j,$$

with one fixed complex offset $c$ and arbitrary complex factors. On a
full four-cell rectangle its determinant would give

$$0=\omega(x_i-x_{i'})(y_j-y_{j'}).\tag{2}$$

Thus two distinct scalar rows and two distinct scalar columns cannot
form a legal rectangle. On an injectively indexed $n\times n$ square,
counting pairs of rows sharing a column gives

$$G^2/n-G\le n(n-1),\qquad
G\le\frac n2(1+\sqrt{4n-3})\le n^{3/2}+n/2.\tag{3}$$

To verify the count, if column degrees are $d_j$, a row pair occurs
together at most once; hence $\sum_j\binom{d_j}{2}\le\binom n2$,
and $\sum_jd_j^2\ge G^2/n$. No outside incidence theorem is used.

With $k$ states and at most $H$ row or column labels per scalar per
state, selecting one representative of each scalar pair and applying
the same argument gives

$$G\le k\bigl(H^{3/2}n^{3/2}+Hn\bigr).\tag{4}$$

For $n=e^{ad+o(d)}$, $k,H=e^{o(d)}$, this is
$G\le e^{(3a/2+o(1))d}$ and $B=n^2-G=e^{2ad+o(d)}$.
If $\log k=\kappa d+o(d)$ and $\log H=\sigma d+o(d)$, escaping
this bound requires $\kappa+3\sigma/2\ge a/2$. This necessary cost
is not a sufficient construction theorem.

### What it means

Literal multiplicative splitting of an exponent into a row factor and
a column factor is too rigid, even if the norm varies between cells.
The proof permits deleted cells, repeated labels and offsets; their
costs are counted in (4).

### Why it matters

Subexponential state/fiber counts cannot close the missing coverage gap.
This result does not cover sums of separated products or genuinely
coupled index maps, and does not give an actual-image lower bound.
This architecture was rejected analytically before enumeration.

## 4. Dense block transitions — the largest block cannot mix completely

### Mathematical statement

Partition $A=\bigsqcup_{i=1}^k A_i$. Credit a return on a source block
only if the entire block goes into one target block pair:

$$M_u(A_i\times A_j)\subseteq A_r\times A_s.\tag{5}$$

Every $u\ne\pm1$ has a row with two nonzero coefficients. If $M$ is
the size of a largest block, that row on its diagonal square has at
least $2M-1$ different values, since $|C+D|\ge|C|+|D|-1$ for
finite real sets. For $M\ge2$, no target block can contain them.
Only the two scalar signs can be credited there. Thus for threshold $R>2$,

$$\boxed{B_{\rm cert}\ge M^2\ge n^2/k^2.}\tag{6}$$

### What it means

A fixed partition with $k=e^{o(d)}$ states leaves
$e^{2ad-o(d)}$ pairs without a growing-return certificate. Target
states may depend on the action and source block, but in (5) they
must be fixed across every pair of that source block.

### Why it matters

Whole-block transitions cannot provide the required small exceptional
tail. This does not exclude partial returns, overlapping covers,
action-dependent partitions or targets chosen separately for each
pair. The companion proves the exact transition-size bounds and
explains why deleting pairs cannot silently be covered by (6).
No finite enumeration was needed to reject this certificate.

## 5. Direct matrix invariance and product digit carriers

### Mathematical statement

**DC-M1.** For every finite real $A$, $n=|A|$, and every $N(u)=1$, $u\ne\pm1$,

$$\boxed{N_A(u):=|A^2\cap M_u^{-1}(A^2)|
\le F(n):=\left\lfloor\frac{3n^2+1}{4}\right\rfloor.}\tag{7}$$

Here is the elementary counting mechanism. For increasing sets $X,Y$
of size $n$, partition their ordered index square into monotone chains
of lengths $2n-1,2n-3,\ldots,1$. Along each chain $x_i+y_j$
strictly increases. A target set of size $n$ captures at most the
minimum of $n$ and the chain length. Summing gives $F(n)$. Apply this
to a mixed row of $M_u$; both scaled coordinate sets still have size $n$.

**DC-M2/M3.** For rational actions on an action-faithful digit product
$A=\{\sum_i a_i\theta_i:a_i\in D_i\subset\mathbb Q\}$, with
$n_i=|D_i|\ge2$, membership separates exactly by coordinates, so

$$\frac{N_A(u)}{n^2}=\prod_i\frac{N_{D_i}(u)}{n_i^2}
\le\rho:=\prod_i\frac{F(n_i)}{n_i^2}\le(7/9)^d\quad(u\ne\pm1).\tag{8}$$

Rational linear independence of the $\theta_i$ suffices; a verified
finite no-carry condition also suffices. Mere input properness does not.
For $s=|U\cap\{1,-1\}|\le2$ and $R>s$, double counting yields

$$\#\{p:R_{\rm pair}(p)\ge R\}
\le\frac{n^2(|U|-s)\rho}{R-s}.\tag{9}$$

Consequently $|U|=e^{\gamma d+o(d)}$ and an almost-all-pairs threshold
$e^{rd+o(d)}$ require $r\le\gamma-\log(9/7)$. Passing this necessary
test does not establish a return tail.

### What it means

Conventional Cartesian Følner invariance — overlap tending to one under
a mixing action — is impossible, uniformly in the real set and angle.
However, (7) allows many actions returning on different positive
fractions. It therefore does not refute the main many-action goal.
For independent digits, the losses multiply and must be paid.

### Why it matters

Direct matrix designs should not aim to make each mixing action almost
invariant. They need a quantitatively good distribution of different
partial-return domains. Neither a large average nor a large action set
alone proves that distribution.

### Mathematical statement — a separate actual-image obstruction

**DC-M4.** If $|D_i|\le m$ and scalar equality of two $Q$ values
forces equality of their full quadratic digit coefficients, then every
fiber has size at most $m^4$:

$$\boxed{|Q(A,A)|\ge n^2/m^4.}\tag{10}$$

For completeness, put $v_i=(a_i,b_i)\in D_i^2$ and use the positive
definite inner product
$\langle(a,b),(c,e)\rangle_Q=ac+(ae+bc)/2+be$. Equality of all
quadratic coefficients fixes the Gram matrix of the $v_i$. In rank
two, fix two independent anchor indices. There are at most $m^4$
choices for their images; their inner products determine every other
vector uniquely. Rank one allows at most $m^2$ choices, and rank zero
allows one. The indices are fixed from the given Gram matrix, so no
unaccounted factor depending on $d$ occurs.

**DC-M5, explicit new carrier.** Define $P_i,t_i,q_i,u_i,U_d$ by §7
below and set

$$B_d=100P_d,\qquad
A_d^{\rm gap}=\left\{\sum_{i=0}^{d-1}a_iB_d^{3^i}:
a_i\in\{-1,0,1\}\right\}.\tag{11}$$

Then $n=3^d$, every $Q$ fiber has at most 81 pairs, and

$$|Q(A_d^{\rm gap},A_d^{\rm gap})|\ge n^2/81,\qquad
R_{\rm pair}(p)=1\quad\text{for all }p\in(A_d^{\rm gap})^2
\text{ under }U_d.\tag{12}$$

The digit exponent sums $3^i+3^j$ are distinct for unordered index
pairs. Differences of quadratic coefficients are bounded by 12.
For an integer polynomial with coefficients bounded by $C$, evaluation
at $B>C+1$ cannot vanish: the highest term exceeds the sum of all
lower terms. This proves the needed quadratic faithfulness in (11).

Each selected matrix has common denominator dividing $P_d$ and
numerators of size less than $2P_d$. Clearing the denominator from
membership leaves digit coefficients of size at most $5P_d$;
$B_d=100P_d$ again makes membership digitwise. On
$D^2=\{-1,0,1\}^2$, every nonzero return multiplier is a root of
unity: the six norm-one points are the sixth roots, while the two
norm-three points are $\pm(1-\omega)$. UE-P1 says the generated group
has no nonidentity root of unity. Thus a nonidentity selected action
returns only the zero digit pair, proving (12).

### What it means

This family makes the coefficient square completely explicit, but its
selected actions do not move any nonzero pair to another legal pair.
The independent fiber bound shows that changing the action family
cannot rescue this particular scalar carrier's image exponent.

### Why it matters

This is a genuine actual-image obstruction, unlike (3), (6), (7) or
the thickening bound below. Its scope is faithful bounded-alphabet
quadratic projection; it is not a theorem about all GAPs, correlated
digits or arbitrary projections with quadratic relations. At scalar
level the return statement in (12) concerns the finite $U_d$ window,
not all integer powers, whose denominators need not be cleared by $P_d$.

## 6. Rectangles — a useful sufficient bridge with an open witness

### Mathematical statement

Let $A=X\cup Y$, $n=|A|$. Suppose every pair outside
$E\subseteq X\times Y$ has at least $R$ distinct returns into
$X\times Y$ under a finite action family $U$. Then

$$\boxed{|Q(A,A)|\le\frac{n^2}{R}
+|X\setminus Y|^2+|Y\setminus X|^2+2|E|.}\tag{13}$$

The same statement holds when the original targets lie in $A^2$.
To prove it, coordinate swap $J(x,y)=(y,x)$ satisfies
$JM_uJ=M_{\bar u}$. Thus $U\cup\bar U$ also covers the reverse
rectangle, with a swapped exception set. The precise uncovered set is

$$A^2\setminus[(X\times Y)\cup(Y\times X)]
=(X\setminus Y)^2\sqcup(Y\setminus X)^2.$$

This gives the bad-pair bound in (13); HR-1 supplies the image bound.
Action unions are deduplicated, and return counts on overlapping
rectangles are not added. Zero is exceptional whenever $R>1$.

In particular, fixed $\varepsilon,\eta,\delta>0$ and

$$R\ge n^\varepsilon,\quad |X\triangle Y|\le Cn^{1-\eta},
\quad |E|\le C'n^{2-\delta}$$

certify every strict $0<c<\min(\varepsilon,2\eta,\delta)$.
This is a **PROVED implication**, with the simultaneous construction
hypotheses **OPEN**.

### What it means

Comparable rectangular side sizes do not suffice. If $X,Y$ are
disjoint and equally sized, the two rectangles cover just half the
square, leaving $n^2/2$ pairs uncertified. Near coincidence of the
coordinate sets is a sufficient way to remove this precise loss.

### Why it matters

The same-set transport issue is completely charged for any future
witness to these hypotheses. No extra conjectural symmetrization step
would remain. The companion also gives an all-four-block version;
we adopt no second next obligation based on that variant.

## 7. Growing one-axis thickening — explicit coverage failure

### Mathematical statement

Reuse the established multiplier sequence, fixed once for all depths:

$$P_0=1,\quad t_i=3P_{i-1}^3,\quad q_i=t_i^2+t_i+1,\quad
P_i=P_{i-1}q_i,\quad
u_i=\frac{t_i-\omega}{t_i-\bar\omega},$$
$$U_d=\{\prod_{i=1}^d u_i^{e_i}:e_i\in\{-1,0,1\}\},\qquad M=3^d.$$

For $z\in U_d$, write $z=x_z-\omega y_z$. The two coefficient maps
are injective, with images $X,Y$ of size $M$. For any finite nonempty
real $T$, $K=|T|$, set

$$A_T=(X+T)\cup Y,\qquad E_T=\{(x_z+t,y_z):z\in U_d,t\in T\}.$$

These are engineered pairs, not automatically high-return pairs. Then

$$|E_T|=MK,\qquad n=|A_T|\ge M+K-1,\qquad
\boxed{|A_T^2\setminus E_T|\ge n^2-(n+1)^2/4.}\tag{14}$$

Here $y_z$ identifies $z$, giving the first equality; the real
sumset inequality gives the input lower bound; and $4MK\le(M+K)^2$
gives the complement bound.

For the new explicit family $T_d=\{0,1,\ldots,M-1\}$,

$$M^2/3\le n_d\le M^2+M,\quad |E_{T_d}|=M^2,\quad
|E_{T_d}|/n_d^2\le9/M^2.\tag{15}$$

To see the lower input count, norm one gives $|x_z|\le2/\sqrt3$.
At most three points of this interval can differ by integers, so the
map $(x,t)\mapsto x+t$ has fibers at most three. Therefore
$\log n_d=2d\log3+O(1)$; the engineered set is exponentially sparse.

### What it means

Arbitrary one-axis shifts cannot turn this injective orbit projection
into almost-full engineered coverage. For the growing interval shifts,
the scalar set grows quadratically in the old orbit size.
Even the old orbit returns are not automatically inherited:
$u(z+t)=uz+ut$, and $ut$ generally ceases to be an allowed real shift.

### Why it matters

This rejects the certificate even if every engineered point were
optimistically granted many returns. It does not bound returns on all
other pairs and does not prove a quadratic image for the thickened
family. That actual asymptotic image rate remains **OPEN**.

## 8. Exact finite scouting — four frozen cases

**EXPERIMENTAL, exhaustive and exact.** The diagnostic tests every
ordered pair and every selected actual multiplier. Every equality uses
rational arithmetic. Every action is independently recomputed in
real/$\sqrt{-3}$ coordinates; every polynomial value is recomputed as
$((2x+y)^2+3y^2)/4$. These are finite verification checks, not
asymptotic proof premises.

Here $G=\#\{R_{\rm pair}\ge2^d\}$ and $B=n^2-G$. The symbol $E$
counts engineered pairs separately. In the digit case $E=A^2$ because
all digit pairs are explicitly encoded; that fact supplies no return gain.

| New carrier | $d$ | $n$ | $|U|$ | $|E|$ | $G$ | $B$ | Full $|Q(A,A)|$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| One-axis interval thickening | 1 | 12 | 3 | 9 | 10 | 134 | 71 |
| One-axis interval thickening | 2 | 90 | 9 | 81 | 18 | 8,082 | 4,024 |
| Faithful ternary GAP | 2 | 9 | 9 | 81 | 0 | 81 | 17 |
| Faithful ternary GAP | 3 | 27 | 27 | 729 | 0 | 729 | 139 |

### Complete return distributions

Notation $r:c$ means exactly $c$ ordered pairs have count $r$.

| Carrier/depth | $R_{\rm pair}$ histogram | $R_{\rm action}$ histogram |
|---|---|---|
| Thickening 1 | $1:134,\ 2:8,\ 3:2$ | $1:133,\ 2:8,\ 3:3$ |
| Thickening 2 | $1:8060,\ 2:22,\ 4:8,\ 6:8,\ 9:2$ | $1:8059,\ 2:22,\ 4:8,\ 6:8,\ 9:3$ |
| GAP 2 | $1:81$ | $1:80,\ 9:1$ |
| GAP 3 | $1:729$ | $1:728,\ 27:1$ |

The only discrepancy is zero. In each case one pair has $|U|$ fixing
actions, and the remaining $n^2-1$ pairs have one. At every nonzero pair,
distinct returning actions have distinct targets. The raw data retain each actual target,
not just a claimed number of distinct labels.

| Carrier/depth | One-return fraction | Median $R_{\rm pair}$ | Geometric mean | Minimum outside declared bad set |
|---|---:|---:|---:|---:|
| Thickening 1 | $67/72$ | 1 | 1.055238… | 2 |
| Thickening 2 | $403/405$ | 1 | 1.005579… | 4 |
| GAP 2 | 1 | 1 | 1 | No good pairs |
| GAP 3 | 1 | 1 | 1 | No good pairs |

Geometric means are display approximations only; the data contain exact
histograms and the exact product-root expressions. On the engineered
thickening subsets, the distributions are respectively
$1:4,2:4,3:1$ and $1:64,2:8,4:4,6:4,9:1$. Thus engineered membership
does not inherit the old $2^d$ minimum. Incidental returns outside the
engineered subset also occur; neither subset is silently identified
with the other.

### Complete image multiplicities and HR-1 accounting

Here $h:c$ means $c$ outputs have exactly $h$ ordered preimages.

| Carrier/depth | Image-fiber histogram | Exact reciprocal HR-1 bound $\sum_p1/R_{\rm pair}(p)$ |
|---|---|---:|
| Thickening 1 | $1:10,2:57,4:2,6:2$ | $416/3$ |
| Thickening 2 | $1:82,2:3886,4:51,6:4,18:1$ | $72671/9$ |
| GAP 2 | $1:1,2:4,4:6,6:4,12:2$ | 81 |
| GAP 3 | $1:1,2:13,4:90,6:13,12:22$ | 729 |

Return and stabilizer histogram populations sum to $n^2$. Image-fiber
populations sum to $|Q(A,A)|$; their size-weighted sum is $n^2$.
The full images are measured
independently of the return certificate. The gap between an actual image
count and its return upper bound demonstrates why failure of that upper
bound is not itself an image lower bound.

**Selection gate:** no construction survives. The split and complete-block
certificates were rejected analytically; conventional matrix invariance
is ruled out by (7); the concrete digit family is ruled out by (12);
the engineered thickening certificate is ruled out by (14)–(15).
The rectangular result is a useful implication with no carrier witness,
not an untested asserted success. Four scouts, two sizes per concrete
carrier, were fixed in advance; no parameter expansion followed failure.

## 9. Signed rates and arithmetic audit

The companion ledgers follow the repository construction template.
Here all logarithms are natural. A certificate bad set is distinguished
from an actual low-return set throughout.

| Architecture | Input rate | Return rate credited | Bad-pair cost | Resulting certificate |
|---|---|---|---|---|
| Split product, $k,H=e^{o(d)}$ | Hypothesis $\log n=ad+o(d)$ | Even arbitrarily large returns on represented cells do not fix coverage | $B_{\rm cert}=e^{2ad+o(d)}$; represented cells at most $e^{(3a/2+o(1))d}$ | Pair-exception HR-1 exponent $2a$; zero gap |
| Complete $k$-block partition, $k=e^{o(d)}$ | Hypothesis $\log n=ad+o(d)$ | At most two certified targets on largest diagonal block | $B_{\rm cert}\ge e^{2ad-o(d)}$ | No fixed bad-pair deficit; actual incidental returns OPEN |
| Direct single-action invariance | Arbitrary $n$ | One action cannot have overlap fraction tending to one | At least $n^2-F(n)$ pairs leave for that action | Not a many-action tail theorem; no image exponent inferred |
| Action-faithful independent digits | $n=\prod n_i$ | Necessary $r\le\gamma-\log(9/7)$ | Tail not supplied by averaging | Cost only; general many-action case OPEN |
| Explicit faithful ternary GAP | $a=\log3$ exactly | $r=0$ under selected $U_d$ | $B=n^2=e^{2ad}$ for every threshold $>1$ | Actual image exponent $2a$ by $n^2/81\le|Q|\le n^2$ |
| One-axis interval thickening | $a=2\log3$; bounded input prefactors | No positive rate proved after shifts | $B_{\rm cert}=n^2-3^{2d}=e^{2ad+O(1)}$ | Zero certificate gap; actual image OPEN |
| High-overlap rectangle, if witnessed | $\log n=ad+o(d)$ | $R\ge e^{rd-o(d)}$ | $|X\triangle Y|\le e^{(a-\tau)d+o(d)}$, $|E|\le e^{(2a-\delta)d+o(d)}$ | Output at most $e^{[2a-\min(r,2\tau,\delta)]d+o(d)}$; every strict $c<\min(r,2\tau,\delta)/a$ |

For the last row all constants must be fixed before growth; unknown
arithmetic costs of a future witness are not zero. This is a conditional
rate ledger, not a surviving positive construction.

**Denominators, heights and fields.** The two explicit carriers use only
$\mathbb Q$ and multipliers in fixed $\mathbb Q(\omega)$, degree two,
discriminant $-3$. No class-number, regulator, ideal-volume or local
splitting estimate is invoked. Every $U_d$ matrix has common denominator
dividing $P_d$. These are fractional norm-one elements, not an
exponentially large supply of integral units. From
$9P^7\le P_i\le13P^7$ one obtains

$$\frac{\log9}{6}(7^d-1)\le\log P_d
\le\frac{\log13}{6}(7^d-1).$$

The interval thickening adds integer shifts and has scalar magnitude at
most $3^d+2$, but denominator logarithms of order $7^d$. The GAP is
integral and has scalar height with logarithm $\Theta(21^d)$ because
$B_d=100P_d$ and the largest weight exponent is $3^{d-1}$. These
large heights are recorded explicitly; no polynomial-height claim is
used to prove the new obstruction.

**Projection, carries and archimedean size.** Scalar inputs and action
targets are exact real numbers, not traces or modular representatives.
The GAP projection is injective and faithful on the relevant action and
quadratic equations by separate no-carry proofs. For the thickening,
the shifted-pair map is injective and addition fibers are at most three
for the specified interval shifts. No input thinning occurs. The two
coordinates would pay any thinning twice if it were introduced. A
norm-one action is an isometry for $Q$; no unproved Euclidean box
invariance is credited.

**States, exceptions and stabilizers.** States and label fibers appear
explicitly in (4), blocks in (6), and unmatched scalar populations in
(13). Zero is included in every finite diagnostic square and has effective return
one. No singular or boundary pair is silently discarded. No exceptional
output saving is inferred from a pair count or collision energy.

## 10. Failure registry and retained scope

| Record | FAILED scope | What remains OPEN or unaffected |
|---|---|---|
| DC-F1 | Subexponential unions of separable product states with subexponential coordinate fibers cannot nearly cover $A^2$ | Coupled indexing, larger paid fibers, sums of products |
| DC-F2 | Fixed subexponential scalar partitions certified solely by complete block-to-one-block transitions | Partial returns, overlapping covers, action-dependent partitions |
| DC-F3 | A Cartesian Følner sequence with overlap tending to one under any mixing norm multiplier | Many distinct actions with differing partial-return domains |
| DC-F4 | Faithful bounded-alphabet quadratic products, including (11), cannot have fixed power-saving actual images | Correlated digits and quadratic projections with nontrivial relations |
| DC-F5 | One-axis shifts of the specified injective seed-$1$ orbit cannot provide almost-full engineered coverage | Actual incidental returns, other seeds or correlated shift schemes |
| DC-F6 | Symmetrizing a balanced disjoint rectangle alone leaves half the square uncertified | High-overlap rectangular witness for (13) |

The actual-image lower bound belongs only to DC-F4. In particular,
the new report proves neither a quadratic image for the old primary
coefficient set nor a quadratic image for the growing thickening. It
does not disprove the main quadratic target, RC15/4, ARG, TCRC or all
return methods. A future argument must not silently assume any failed
coverage certificate or infer an almost-everywhere tail from mean overlap.

## 11. Proof audit and reproducibility

Three bounded theoretical subtasks were run in parallel, with no program
budget allocated to them. Independent internal cross-reviews checked
the determinant and label counts, mixed-row and largest-block arguments,
swap and unmatched-square formula, monotone chains, tensor membership,
Gram reconstruction, and concrete no-carry realization. The lead also
inspected the proofs. These are **internal mathematical audits**, not
external peer review or evidence of novelty.

Corrections before finalization: a block-summary sentence now requires
an eventually growing threshold $R>2$, not merely a positive threshold;
the fixed-place-value polynomial-height remark is restricted to
exponential input growth; integer denominator/magnitude claims in the
thickening ledger are restricted to its integer shifts; the concrete
digit indexing is aligned to $i=0,\ldots,d-1$. None changes the main
theorem conclusions. The pre-execution program audit also added an
explicit rejection of identical summary/raw output paths.

The program is
[dense_cartesianization.py](../../../experiments/dense_cartesianization.py).
Its inspected arithmetic dependency is the unchanged unit-exponent
module; importing it does not execute its old experiments. The current
scout was run exactly once:

```text
python3 -m experiments.dense_cartesianization \
  --output examples/2026-09-21-dense-cartesianization.json \
  --pairs-output local-only/runs/T03/2026-09-21-dense-cartesianization/pairs.json
```

Outputs are exclusive-created. For reproduction choose fresh paths.
The local raw file contains all scalar values, multipliers, output
values, ordered pairs, returning action indices and distinct target
pairs. The tracked-size example is the complete summarized diagnostic.
No random seed, approximate equality, sampling, factorization or network
access was used. Python runtime: **3.12.7**.

The announced shared cap was **2,000,000 charged evaluations and 600 CPU
seconds**, including required regressions. The single scout used
**205,644** semantic query charges and **2.511953 CPU seconds**.
Its two tiny exception/accounting tests are included in the required
test suite; no carrier scout is rerun by the tests. Regression calls are
charged conservatively at every project Python call, overcounting the
underlying mathematical queries: 64,949 for unit tests, 25,386 for
the verification suite. **Total: 295,979 charges; 5.480470 CPU seconds.**
The guard checks CPU periodically rather than claiming an OS-enforced
hard deadline. The run ended far below both caps.

**Validation:** 54 unit tests and 159 existing exact verification checks
passed. Documentation, setup, diff and source-integrity checks are
recorded separately in [verification.md](verification.md); those are
repository checks, not extra mathematical proof or research searches.
No old archive was modified, no canonical manifest was rewritten, and
nothing was staged or committed. The repository already contained
uncommitted work when this cycle began; it is preserved. Concurrent T01
documentation/status changes and a preceding current-map edit were
detected during integrity checking, left intact, and recorded separately
from this task's five dated addenda.

## 12. One next mathematical obligation — DC-O1

**OPEN: high-overlap rectangular return witness.** Construct explicit
sequences $X_d,Y_d\subset\mathbb R$, finite sets $U_d$ of distinct
norm-one multipliers, and fixed $\varepsilon,\eta,\delta>0$, with
$A_d=X_d\cup Y_d$, $n_d=|A_d|\to\infty$, such that

$$|X_d\triangle Y_d|\le Cn_d^{1-\eta},$$
$$|E_d|\le C'n_d^{2-\delta},\qquad E_d\subseteq X_d\times Y_d,$$
$$\#\{M_up\in A_d^2:u\in U_d\}\ge n_d^\varepsilon
\quad\text{for every }p\in(X_d\times Y_d)\setminus E_d.$$

The last line counts distinct legal target pairs, not words or states.
The constants are fixed before $d$ grows, and the construction must
verify all scalar, denominator and projection costs. By DC-R1 this
single witness would immediately give every strict
$0<c<\min(\varepsilon,2\eta,\delta)$ for the same-set quadratic.
The sufficient transport lemma is now proved; this witness is the
remaining obligation within dense Cartesianization. No additional
carrier search is begun in this report.
