# DC-S1–DC-S2 — Split multiplicative indexing and Cartesian coverage

Date/version: **21 September 2026, version 1**. Track: **T03**, the
newly authorized dense-Cartesianization cycle for the fixed polynomial
$Q(x,y)=x^2+xy+y^2$.

## Result and scope

**PROVED, DC-S1.** A separated product representation

$$x_i-\omega y_j=c+v_iw_j\tag{1}$$

cannot hold on a complete $2\times2$ rectangle with distinct row and
column scalar coordinates. On an injectively indexed $n\times n$
scalar grid it can cover at most

$$\frac n2\bigl(1+\sqrt{4n-3}\bigr)\le n^{3/2}+\frac n2$$

cells. Arbitrary deleted cells are permitted in this statement.

**PROVED, DC-S2.** Repeated coordinate labels do not evade the bound at
subexponential cost. If $|A_d|=e^{ad+o(d)}$, $a>0$, and there are
$e^{o(d)}$ states of the form (1), each with at most $e^{o(d)}$ row and
column labels per scalar, their union covers at most
$e^{(3a/2+o(1))d}$ distinct pairs. Almost the entire Cartesian square
remains outside this representation certificate.

These statements do **not** assume that all represented points have one
norm, or that the factors $v_i,w_j$ have norm one. They therefore apply
to separated products whose norms vary. Their obstruction is different
from the earlier fixed-norm-shell sparsity theorem.

**FAILED in this scope:** almost-full Cartesianization by a
subexponential union of separated-product states with subexponential
coordinate fibers. **OPEN outside this scope:** a sufficiently coupled
parameterization, or a scheme with larger explicitly charged state/fiber
counts, might behave differently. No lower bound for the actual full
$Q(A,A)$ image is proved here.

## Identity, authorization and evidence

| Field | Record |
|---|---|
| Claim IDs | **DC-S1**, §§1–2; **DC-S2**, §§3–4 |
| Polynomial/domain | Fixed $Q=x^2+xy+y^2$ on real scalar inputs; exact equality of complex norm coordinates |
| Quantifiers | Every finite real input grid, every finite label system and every complex choice of the factors and fixed state offsets satisfying (1) on the designated legal cells |
| Status | **PROVED**, complete elementary arguments below |
| Evidence | New internal symbolic derivation; author audit; independent parent audit is a separate record |
| Budget/network | Zero mathematical program executions, zero experiments, strictly offline; no outside theorem or literature search |
| Scope of work | One bounded family: separated multiplicative indexing, its deleted cells, repeated coordinate labels and finite unions of states |
| New versus inherited | The determinant and coverage bounds are derived here. Norm preservation, actual unit-action growth, orbit returns and HR-1 are inherited and are not reproved |
| No novelty claim | No external priority or novelty assessment was performed |

The active assignment is
`[private commissioning attachment; locator withheld]`,
especially directions A–B and the full-square coverage gate. The preceding
[frozen checkpoint](../2026-09-20-cartesian-norm-freeze/Cartesian_Norm_Symmetry_Research_Checkpoint.md),
§§6 and 11, records the missing Cartesian bridge. The present user
assignment authorizes this new cycle; archived continuation instructions
are not its authority.

Relevant inherited sources are
[UE-P1–UE-P3](../2026-09-16-unit-exponent/primary-proof.md), §§1–3,
and [HR-1](../2026-09-16-high-return/return-lemma.md).
The fixed T03 target and separate adaptive obligation are recorded in
`local-only/migration/sources/T03_CURRENT_STATE.md`, §§2–3 and 7.
No prior proof, experiment, historical report or track target is changed.
The factorization/counting argument below has no missing source premise.

## 1. DC-S1 — The four-cell identity

### Mathematical statement

Fix $\omega=(-1+i\sqrt3)/2$. Let $I,J$ be finite index sets, with
real coordinates $x_i$ and $y_j$, complex factors $v_i,w_j$, and a
single complex offset $c$. Let $E\subseteq I\times J$ be any set of
legal cells on which (1) holds. The factors may be zero; no division by
them will be used.

If $(i,j),(i,j'),(i',j),(i',j')\in E$, then

$$\boxed{(x_i-x_{i'})(y_j-y_{j'})=0.}\tag{2}$$

In particular, if both coordinate maps are injective, $E$ has no
complete rectangle with two distinct rows and two distinct columns.
If all of $I\times J$ is legal, then at least one of the two coordinate
maps is constant.

### What it means

Splitting a multiplicative exponent into a row part and a column part
gives a matrix of products. Such a matrix has zero $2\times2$
determinants. A genuine scalar Cartesian norm grid has nonzero
determinants whenever both scalar coordinates vary.

### Why it matters

The complete product-indexed carrier fails before one asks how many
norm-one actions return. Deleting cells can remove the offending
rectangles, but §2 counts how many cells can remain.

### Proof

For the indicated four cells, subtract $c$ and use (1). The determinant
of the resulting product matrix is zero:

$$
(v_iw_j)(v_{i'}w_{j'})-(v_iw_{j'})(v_{i'}w_j)=0.
$$

On the scalar side, exact expansion gives

$$
\begin{aligned}
&(x_i-\omega y_j-c)(x_{i'}-\omega y_{j'}-c)\\
&\qquad -(x_i-\omega y_{j'}-c)(x_{i'}-\omega y_j-c)
=\omega(x_i-x_{i'})(y_j-y_{j'}).
\end{aligned}
\tag{3}
$$

Since $\omega\ne0$, (2) follows. If the full grid is legal and two
distinct $x$ values occur, apply (2) to those rows and every two columns;
all $y$ values must be equal. The other case is symmetric. $\square$

## 2. Quantitative deleted-cell bound for injective coordinates

### Mathematical statement

Suppose $|I|=r\ge1$, $|J|=s\ge1$, and both coordinate maps are
injective. Write $g=|E|$. Then

$$
\frac{g^2}{s}-g\le r(r-1),\qquad
\frac{g^2}{r}-g\le s(s-1).
\tag{4}
$$

Equivalently,

$$
g\le \mathcal D(r,s):=
\min\left\{
\frac{s+\sqrt{s^2+4sr(r-1)}}2,
\frac{r+\sqrt{r^2+4rs(s-1)}}2
\right\}.
\tag{5}
$$

The integer count is of course at most the floor of this displayed
bound. At least $rs-\mathcal D(r,s)$ cells of the full rectangle must
be omitted. For an $n\times n$ grid,

$$
\boxed{g\le\frac n2(1+\sqrt{4n-3})\le n^{3/2}+\frac n2,}
\qquad
\boxed{n^2-g\ge n^2-n^{3/2}-\frac n2.}
\tag{6}
$$

The bound is an explicit elementary estimate, not a claim that it is
attained by product representations over the real numbers.

### What it means

Deleting only a power-saving number of cells cannot repair an
injectively indexed product grid. For large square grids the proportion
of legal cells tends to zero, rather than to one.

### Why it matters

Even if every retained cell were granted exponentially many genuine
returns, these cells would not cover the domain required by the
almost-everywhere return theorem.

### Proof

For each column $j$, let $d_j$ be its number of legal rows. By (2),
any pair of distinct rows can occur together in at most one column.
Counting pairs of rows in columns gives

$$\sum_{j\in J}\binom{d_j}{2}\le\binom r2.$$

Also $\sum_j d_j=g$ and
$\sum_jd_j^2\ge g^2/s$, the latter following by expanding
$\sum_j(d_j-g/s)^2\ge0$. Therefore

$$g^2/s-g\le\sum_j(d_j^2-d_j)\le r(r-1).$$

Interchange rows and columns for the second inequality. Solving these
two quadratic inequalities gives (5), and setting $r=s=n$ gives (6).
This supplies the counting proof directly, without invoking an external
extremal graph theorem. $\square$

## 3. DC-S2 — Repeated labels and parameter fibers

### Mathematical statement

Now permit arbitrary, noninjective coordinate maps $i\mapsto x_i$ and
$j\mapsto y_j$. Count distinct scalar pairs, not parameter cells:

$$
\mathcal G=\{(x_i,y_j):(i,j)\in E\},\qquad g=|\mathcal G|.
\tag{7}
$$

Empty index sets contribute no cells and may be omitted. In formulas
with denominators, retain $r=|I|\ge1$ and $s=|J|\ge1$.

Then (4)–(5) still hold for $g$, with $r=|I|$, $s=|J|$.
More precisely, writing

$$r_x=\#\{i:x_i=x\},\qquad s_y=\#\{j:y_j=y\},$$

one has the stronger finite bounds

$$
\frac{g^2}{s}-g\le r^2-\sum_xr_x^2,\qquad
\frac{g^2}{r}-g\le s^2-\sum_ys_y^2.
\tag{8}
$$

If the coordinate images lie in real sets $X,Y$ of sizes $m,n$, and
$r_x\le H_x$, $s_y\le H_y$, it follows in particular that

$$
\boxed{
g\le\min\left\{
H_xm\sqrt{H_yn}+H_yn,
H_yn\sqrt{H_xm}+H_xm
\right\}.}
\tag{9}
$$

### What it means

Giving one scalar value several exponent labels can create many formal
representations of a cell. We count each scalar pair once and retain the
label counts in the bound. Coordinate reuse helps this estimate only
through explicitly growing numbers of labels, not through uncharged
duplication.

### Why it matters

Subexponential coordinate fibers cannot turn an exponentially sized
separated-product grid into almost-full scalar coverage. Exponential
fibers are not ruled out by this theorem; their actual action/return
behavior would require its own proof and cost accounting.

### Proof

Choose one legal parameter cell for each pair in $\mathcal G$, and
discard the other representations. Let $E_*$ be this selected set.
Then $|E_*|=g$, and its projection to scalar pairs is injective.

The graph $E_*$ has no complete $2\times2$ rectangle. Indeed, if such
a rectangle existed and its two row coordinates were equal, its two
edges in either fixed column would represent the same scalar pair,
contrary to the selection. The column coordinates must likewise be
distinct. Both coordinates therefore vary, contradicting (2).
The proof of (4)–(5) applies to $E_*$.

For (8), two row labels with the same scalar $x$ cannot share any
column label in $E_*$, again because this would duplicate a scalar
pair. There are

$$\frac12\left(r^2-\sum_xr_x^2\right)$$

unordered row-label pairs with different scalar coordinates. Each can
share at most one column. Repeat the degree-square argument of §2,
and then transpose it. This proves (8).

Finally $r\le H_xm$, $s\le H_yn$, and (5) implies the simpler bounds
$g\le r\sqrt s+s$ and $g\le s\sqrt r+r$. Substitution proves (9).
$\square$

### Actual projection multiplicity and zero cells

Within one state, a fixed pair $(x,y)$ has at most $r_xs_y\le H_xH_y$
parameter-cell representations. Since $1,-\omega$ are linearly
independent over $\mathbb R$, the complex value $x-\omega y$ determines
the scalar pair uniquely. Thus counting distinct product values on the
legal cells is the same as counting $\mathcal G$, even when the product
parameterization has multiple descriptions.

The proof permits zero factors and the scalar pair $(0,0)$; it does not
discard a singular tail. If a later return argument counts labels
fixing zero, it must still distinguish them from its one returned scalar
pair under HR-1. No return multiplicity is credited by this note.

## 4. Several states and the coverage rate

### Mathematical statement

Let $A\subset\mathbb R$ have $n\ge1$ elements. Suppose $k$ states
are supplied, each with its own finite row and column index sets,
factors and fixed complex offset. All state coordinates lie in $A$;
each state's coordinate fibers are at most $H_x$ on rows and $H_y$
on columns. Let $\mathcal G$ be the union of all distinct legal scalar
pairs and write $G=|\mathcal G|$, $B=n^2-G$. Then

$$
G\le k\min\left\{
H_xn\sqrt{H_yn}+H_yn,
H_yn\sqrt{H_xn}+H_xn
\right\}.
\tag{10}
$$

This is an upper bound even if states overlap. With balanced fiber bound
$H_x,H_y\le H$ it simplifies to

$$
\boxed{G\le k(H^{3/2}n^{3/2}+Hn),\qquad
B\ge n^2-k(H^{3/2}n^{3/2}+Hn).}
\tag{11}
$$

Fix $a>0$ and let $d\to\infty$. If

$$n_d=e^{ad+o(d)},\qquad k_d=e^{o(d)},\qquad H_d=e^{o(d)},$$

then

$$
G_d\le e^{(3a/2)d+o(d)},\qquad
\frac{G_d}{n_d^2}\le e^{-(a/2)d+o(d)},\qquad
B_d=n_d^2(1-o(1)).
\tag{12}
$$

In particular $\log B_d=2ad+o(d)$, so no fixed positive
bad-pair exponent saving follows from these states.

More generally, for $k_d=e^{\kappa d+o(d)}$ and
$H_d=e^{\sigma d+o(d)}$ with $\kappa,\sigma\ge0$, this argument
still forces exponentially sparse coverage whenever

$$\boxed{\kappa+\tfrac32\sigma<\tfrac12a.}\tag{13}$$

Avoiding the strict inequality (13) is a necessary condition for this
balanced-complexity model to evade the bound. It is not a sufficient
condition for any dense construction or positive return rate.

### What it means

A small collection of product-indexed patches cannot cover the square.
If one attempts to overcome the obstruction using label repetition or
many patches, the required growth is exponential in the same depth as
the desired return gain. That growth must be made explicit.

### Why it matters

The uncontrolled complement retains the full quadratic exponent.
HR-1 cannot give a power-saving image bound merely by declaring this
complement exceptional and counting its pairs. This remains true even
if one grants arbitrary favorable return multiplicities on the legal
cells themselves.

### Proof

Apply (9) in each state with $X=Y=A$ and use the union bound. No pair
is credited more than once in the definition of $G$. This proves (10)
and (11). Under the subexponential assumptions, the leading term on
the right of (11) is at most $e^{(3a/2)d+o(d)}$, giving (12).
For general $\kappa,\sigma$, the two terms in (11) have exponents

$$\kappa+\tfrac32(a+\sigma),\qquad \kappa+a+\sigma.$$

The first is larger because $a>0$ and $\sigma\ge0$. Under (13) it
is strictly below $2a$, so the covered fraction decays exponentially.
$\square$

## 5. Construction and rate ledger

This ledger follows the repository construction template. It describes
a necessary obstruction for the stated representation scheme, not a
new real power-saving construction.

| Gain/cost | Exact treatment | Status and limitation |
|---|---|---|
| Fixed polynomial and same set | $Q=x^2+xy+y^2$; every state uses coordinates in one real set $A$ | **PROVED** framework; no rectangular block is substituted for $A^2$ |
| Input size, lower and upper | The finite theorem applies to every $n=|A|$; the rate statement explicitly assumes $\log n_d=ad+o(d)$ with $a>0$ | No unproved count is assigned to a candidate |
| Input thinning in both coordinates | None is used to hide losses: $G$ and $B$ are counted in the original $n^2$ square | A thinned candidate must restate its actual input count and apply the same theorem there |
| Parameter and projection fibers | At most $H_xH_y$ legal parameter cells per scalar pair in one state; at most $kH_xH_y$ across states | **PROVED** upper bounds; one-representative selection avoids counting these descriptions as new pairs |
| Actual actions/stabilizers | This note assumes no action family and asserts no new return count; zero is included | Existing orbit-return results cannot automatically be transferred to a deleted-cell domain |
| Local sparsity, primes, splitting, moduli | No residue class, prime-density or splitting assumption occurs; equality (1) is in $\mathbb C$ | Inapplicable to this algebraic obstruction, not an available arithmetic saving |
| Field degree, discriminant, regulator | Factors may be arbitrary complex numbers; no number-field counting theorem is used | These quantities cannot repair the determinant identity while (1) holds; no zero-cost arithmetic construction is inferred |
| Heights, denominators, normalization | Unrestricted in (1); each fixed scalar seed or nonzero overall multiplier can be absorbed into one factor, and a fixed complex translation is permitted | Obstruction survives arbitrary such choices; no candidate height bound is claimed |
| Archimedean distortion | No metric or approximate equality is used | Numerical near-coincidence cannot create an exact legal cell |
| Branches/states and coordinate reuse | Exact union bound (10); balanced bound (11); $k,H$ remain visible in (13) | **PROVED** necessary rate charge, not an assertion that all such labels duplicate actions |
| Controlled pairs | $G_d\le e^{(3a/2)d+o(d)}$ when $k,H$ are subexponential | **PROVED** even if every represented cell is granted a return certificate |
| Uncovered pairs and outputs | $B_d=n_d^2(1-o(1))$; their actual output support and return counts are not determined | **PROVED** pair count; actual output compression remains **OPEN** |
| Final output exponent from this certificate | Counting uncovered outputs by $B_d$ retains exponent $2a$ | **FAILED** full-image certificate; not an actual-image lower bound |
| Net gap and fixed saving | The uncovered-pair term supplies no positive exponent gap and no $c>0$ | A separate proof on the complement or a different representation would be needed |

The fiber bound in the table is an upper bound available for a later
matched parameter-return model. It is not automatically a realized
loss in every action, and it must not be charged twice. The present
failure already follows from the distinct-pair coverage bound.

## 6. Limits and disposition

The result includes ordinary split exponent indexing: if
$z_{p,q}=z_0\prod_i u_i^{a_i(p)+b_i(q)}$, absorb the seed and row
factors into $v_p$, and the column factors into $w_q$. It also includes
a finite collection of such factorizations with separate fixed offsets.
No assumption of multiplicative independence is needed for the
obstruction; having independent units does not change (3).

The hypothesis is the exact separation in (1). It does not cover
arbitrary functions of both indices, row/column-dependent additive
corrections that are not one fixed state offset, sums of several
separated products, or all direct coefficient-matrix carriers. Indeed
$x_i-\omega y_j=x_i\cdot1+1\cdot(-\omega y_j)$ is already a sum
of two separated products, so extending the determinant conclusion
to such sums would be false without additional hypotheses.

No actual full-image lower bound, universal norm-symmetry obstruction
or new statement about RC15/4 follows. The old one-shell result is not
used: the present factors can have arbitrary norms, and the proof
counts missing Cartesian rectangles instead.

**Scoped verdict: CARTESIANIZATION FAIL** for the low-complexity
split-product scheme described by (12), and more generally by (13).
This subtask supplies one bounded obstruction to the active
constructive cycle. It does not authorize or start another family.

All evidence in this note is symbolic. No computational candidate,
runtime result, numerical equality, source download or external theorem
is used. Historical files remain unchanged; repository-wide checks and
any independently authorized diagnostics belong to the lead's cycle
record.
