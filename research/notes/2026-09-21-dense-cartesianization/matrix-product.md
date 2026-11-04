# Matrix returns and product-coordinate carriers

Date: **21 September 2026**. Track: **T03**, fixed polynomial
$Q(x,y)=x^2+xy+y^2$. Branch: newly commissioned dense Cartesianization.

## Identity, scope and evidence

This note gives elementary analytic results for direct matrix returns on
one common scalar set. It does not revive HR-N1, the old orbit-projection
family, or the sparse valuation family. The authorized subtask is strictly
offline, with **zero mathematical evaluations and zero research-program
runs**. Only local source reads and this new note were used. No external
theorem or novelty assertion is imported.

The arguments below are complete internal proofs, authored in this task.
The lead independently supplied the same one-action chain argument after
the author had sent that argument to the lead. This agreement is not an
external review. The companion proof author independently audited
DC-M1–DC-M4 and reported PASS, subject to making the input-growth
qualification explicit in Section 3's polynomial-height example; that
qualification is included below. DC-M5 is a later authored addition;
its independent review subsequently passed, including the no-carry bounds,
root-of-unity test, zero, finite-window scope and height calculation.
The cycle's verification record identifies the separate review assignments.

| ID | Status and exact scope | Proof location / dependencies |
|---|---|---|
| DC-M1 | **PROVED:** at most $\lfloor(3n^2+1)/4\rfloor$ returns for every real norm multiplier other than $\pm1$ on every finite real $A^2$, $n=|A|$ | Sections 1–2; explicit ordered-grid chains |
| DC-M2 | **PROVED:** exact product factorization and exponential one-action loss for rational actions on action-faithful rational digit products | Section 3; DC-M1 and the stated projection hypothesis |
| DC-M3 | **PROVED:** necessary action-count cost for an almost-all-pairs return tail on those products; not a universal tail obstruction | Section 4; double counting and DC-M2 |
| DC-M4 | **PROVED:** fibers at most $m^4$ for bounded-alphabet products whose scalar quadratic projection is faithful | Section 5; elementary positive-definite Gram reconstruction |
| DC-M5 | **PROVED:** an explicit integer-place-value realization with $n=3^d$, full image at least $n^2/81$, and identity-only nonzero returns for the selected independent action box | Section 5.1; DC-M4's finite-faithfulness proof, elementary no-carry bounds and inherited UE-P1 |

Local source context, inspected for the distinction between old and new
scopes:

- `local-only/migration/sources/T03_CURRENT_STATE.md`, Sections 6, 13–15:
  fixed target and adaptive RC15/4 remain open; historical box results do
  not exclude arbitrary Cartesianization.
- ZIP `local-only/migration/research_supplement/T03/T03_RESEARCH_RECORD_20260910.zip`,
  member `output/Quadratic_Norm_Form_Focused_Offline_Report.md`, Sections
  2, 5–6: multiplier matrix, finite invariance forcing torsion, lattice
  denominator/common-core bounds, and the distinction between overlap
  sums and an almost-all-pairs tail. The ZIP member list was read first.
  Its old tower proposal is not adopted here.
- [HR-1 return lemma](../2026-09-16-high-return/return-lemma.md), Sections
  2–6: exact returns, duplicate labels, exceptions and full-support rates.
- [Earlier carrier screen](../2026-09-16-high-return/carrier-screen.md),
  HR-5/6/7/8: specific recursive repair, fixed-action orbit boxes,
  cyclotomic digit modules and literal translates.
- [Unit-exponent report](../2026-09-16-unit-exponent/README.md), Sections
  2–7: actual action growth, sparse engineered coverage and the separate
  sparse valuation-family obstruction.
- [Failure register](../../FAILURE_LIBRARY.md), “T03 — retained current
  failure record,” and [migration conflicts](../../MIGRATION_CONFLICTS.md):
  scopes and source availability. The absent F25/arithmetic originals are
  unnecessary for every proof below.

## 1. Ordered-grid lemma

Let $X,Y,Z\subset\mathbb R$ each have cardinality $n\ge1$. Then

$$\#\{(x,y)\in X\times Y:x+y\in Z\}
\le F(n):=\left\lfloor\frac{3n^2+1}{4}\right\rfloor.\tag{1}$$

### Proof

Write $x_1<\cdots<x_n$ and $y_1<\cdots<y_n$. Partition the index square
into the following $n$ disjoint chains, for $1\le k\le n$:

$$C_k=\{(k,j):1\le j\le n-k+1\}
\ \cup\ \{(i,n-k+1):k+1\le i\le n\}.\tag{2}$$

To see that these partition the square, remove the top row and rightmost
column, then repeat on the remaining rectangle. At step $k$ the remaining
rows are $k,\ldots,n$ and columns $1,\ldots,n-k+1$. Chain $C_k$ is the
removed row followed by the removed column, without repeating its corner.

Along each chain, first increasing $j$ and then increasing $i$, the sum
$x_i+y_j$ strictly increases. Its length is $2n-2k+1$. Consequently the
$n$ target values in $Z$ select at most $\min(n,2n-2k+1)$ members of this
chain, even if equal sums occur on different chains. Thus the left side
of (1) is at most

$$\sum_{k=1}^n\min(n,2n-2k+1).
$$

For $n=2m$ this sum is $2m\cdot m+(1+3+\cdots+(2m-1))=3m^2$.
For $n=2m+1$ it is $(2m+1)(m+1)+(1+3+\cdots+(2m-1))
=3m^2+3m+1$. These equal $F(n)$. No poset or rearrangement theorem is
assumed. $\square$

In particular, for any nonzero real $a,b$ and a finite set $A$ of size
$n$, multiplication by $a$ and $b$ preserves cardinality, so

$$\#\{(x,y)\in A^2:ax+by\in A\}\le F(n).\tag{3}$$

The signs and sizes of $a,b$ do not affect this conclusion.

## 2. DC-M1 — a universal fixed-action Cartesian defect

For $u=\alpha+\beta\omega$, where $\alpha,\beta\in\mathbb R$,
$\omega^2+\omega+1=0$, and $N(u)=\alpha^2-\alpha\beta+\beta^2=1$,
write

$$T_u(x,y)=(\alpha x+\beta y,-\beta x+(\alpha-\beta)y).\tag{4}$$

Define the one-action overlap

$$N_A(u)=\#\{(x,y)\in A^2:T_u(x,y)\in A^2\}.$$

For every nonempty finite real $A$, $n=|A|$, and every $u\ne\pm1$,

$$\boxed{N_A(u)\le F(n).}\tag{5}$$

### Proof

If $\beta=0$, the norm condition gives $\alpha=\pm1$, which is excluded.
Thus $\beta\ne0$. If $\alpha\ne0$, the first coordinate in (4) has two
nonzero coefficients and (3) applies. If $\alpha=0$, the second
coordinate is $-\beta x-\beta y$, and (3) applies to that coordinate.
Returning both coordinates is a stronger condition than returning the
selected coordinate. This proves (5). $\square$

### Exact invariance and limits of this result

For $n>1$, $F(n)<n^2$. Hence the only norm multipliers that can permute a
non-singleton Cartesian square exactly are $u=1$ and $u=-1$. The first
always does so; the second does so exactly when $A=-A$.

For any sequence with $n\to\infty$ and any selected $u\ne\pm1$,
including actions varying with the sequence,

$$\frac{N_A(u)}{n^2}\le\frac34+\frac1{4n^2}.\tag{6}$$

Therefore the full squares cannot be a conventional Følner sequence for
even one such action: overlap tending to one is impossible. This is
stronger in scope than the earlier square-window observation because it
requires no arithmetic, bounded moments, interval shape or height bound.
It also excludes the other nonidentity torsion rotations from exact
Cartesian invariance.

It is **not** an obstruction to many actions each returning on a fixed
positive fraction. Distinct actions may have different returning sets.
It supplies no actual-image lower bound for an arbitrary $A$.

More precisely, for a finite set $G$ of distinct norm multipliers, put
$s=|G\cap\{1,-1\}|\le2$, and count actual returning actions by
$R_G(p)=\#\{u\in G:T_u(p)\in A^2\}$. Double counting gives only

$$\frac1{n^2}\sum_{p\in A^2}R_G(p)
\le s+(|G|-s)\frac{F(n)}{n^2}.\tag{7}$$

This upper bound remains exponential if $|G|$ is exponential. At the
origin all actions return the same point; away from the origin distinct
complex multipliers give distinct returned pairs. Equation (7) counts
actions, not distinct returned points at zero.

## 3. DC-M2 — exact product overlap for rational digit actions

Let $D_i\subset\mathbb Q$ be finite nonempty sets, $n_i=|D_i|$, and
let $\theta_1,\ldots,\theta_d\in\mathbb R$ be linearly independent over
$\mathbb Q$. Define one common scalar set

$$A=\left\{\sum_{i=1}^d a_i\theta_i:a_i\in D_i\right\},
\qquad n=\prod_{i=1}^d n_i.\tag{8}$$

Let $G$ be any finite set of norm multipliers with rational coefficients
$\alpha,\beta$. Then every $u\in G$ satisfies the exact identity

$$N_A(u)=\prod_{i=1}^d N_{D_i}(u).\tag{9}$$

### Proof

The coefficient representation in (8) is unique. If
$x=\sum a_i\theta_i$ and $y=\sum b_i\theta_i$, then the first returned
coordinate belongs to $A$ exactly when there are $c_i\in D_i$ with

$$\sum_i(\alpha a_i+\beta b_i-c_i)\theta_i=0.$$

All coefficients are rational, so linear independence makes this
equivalent to $\alpha a_i+\beta b_i=c_i\in D_i$ for every $i$.
The same argument applies to the second coordinate. Thus a pair returns
exactly when every digit-pair returns. Choices of digit-pairs are
independent in the full Cartesian input, proving (9). $\square$

For each $u\ne\pm1$, DC-M1 now gives

$$\frac{N_A(u)}{n^2}\le
\rho:=\prod_{i=1}^d\frac{F(n_i)}{n_i^2}.\tag{10}$$

If every $n_i\ge2$, then

$$\rho\le(7/9)^d.\tag{11}$$

Indeed, even $n_i$ give the factor $3/4$, while odd $n_i\ge3$ give
$3/4+1/(4n_i^2)\le7/9$. Singleton digits give factor one and should be
removed from the count of active coordinates.

### Projection scope: proper inputs alone are insufficient

The proof requires that the displayed membership equations have no
nonzero coefficient relations. Ordinary properness of a finite GAP on
its input box is weaker and does not imply (9). Rational linear
independence is one sufficient hypothesis. A finite-domain no-carry
condition on all the membership equations for the selected actions is
another. Both must be verified rather than assumed.

For example, suppose each $D_i\subset[-H,H]\cap\mathbb Z$, and every
matrix in a fixed finite $G$ has the form
$q^{-1}\left(\begin{smallmatrix}a&b\\c&e\end{smallmatrix}\right)$,
with integer entries, $q\ge1$, $|a|,|b|,|c|,|e|\le K$, and $q\le K$.
Each cleared membership equation has integer digit coefficients of
absolute value at most $C=3KH$. For $\theta_i=B^{i-1}$ with integer
$B>C+1$, a nonzero polynomial of degree at most $d-1$ with coefficients
bounded by $C$ cannot vanish at $B$: its highest term exceeds the sum of
all lower terms. Thus (9) holds in this finite no-carry realization too.
The parameters $H,K,B$ must be fixed before $d$ grows for this example.
If additionally $n\ge e^{c d}$ for a fixed $c>0$ (for example, all
$n_i\ge2$), its heights are polynomial in $n$, so it is already subject
to the inherited fixed-field image obstruction. Without such input
growth this polynomial-height inference is not claimed. It is not
proposed as a new positive construction.

Nonrational multipliers can mix the $\theta_i$ coordinates and are
outside (9). Correlated digit subsets, action-dependent coordinate
systems, and projections with relevant additive relations are also
outside it. The universal bound (5) still applies to each individual
real action.

## 4. DC-M3 — the tail implication and its exact limit

Under the hypotheses of DC-M2, with $s=|G\cap\{1,-1\}|$, equations
(7) and (10) give

$$\sum_{p\in A^2}R_G(p)\le n^2\{s+(|G|-s)\rho\}.\tag{12}$$

For every real $M>s$, the number of pairs with $R_G(p)\ge M$ is at most

$$\boxed{\frac{n^2(|G|-s)\rho}{M-s}.}\tag{13}$$

To prove this, let $R_G^{\rm mix}(p)$ count only actions outside
$\{1,-1\}$. Then $R_G^{\rm mix}(p)\ge R_G(p)-s$. Sum this inequality
on the indicated pairs, and use the mixing-action part of (12).

Consequently a claimed tail with $R_G\ge M$ outside at most
$n^{2-\delta}$ pairs must satisfy the necessary condition

$$(M-s)(1-n^{-\delta})\le(|G|-s)\rho.\tag{14}$$

For example, if $n_i\ge2$, $|G|=e^{\gamma d+o(d)}$, and the requested
threshold is $M=e^{rd+o(d)}$ with fixed $r>0$, an almost-all-pairs tail
requires

$$r\le\gamma-\log(9/7).\tag{15}$$

This is a **necessary** cost, not a sufficient tail theorem. It closes
any such tensor certificate whose actual action exponent fails this
test. It does not close all tensor actions: a sufficiently large
action exponent is not contradicted by (15), and a separate return-tail
proof would still be required. No inference from a large mean to an
almost-all-pairs lower bound is made.

The upper count (13) also bounds the number of pairs with at least $M$
distinct returned points, since that condition implies at least $M$
returning actions. Zero is harmless for this implication, but would
need its correct one-point return count in a positive HR-1 application.

## 5. DC-M4 — bounded alphabets under quadratic-faithful projection

There is a separate actual-image obstruction for generic product
projections. Assume now that the real numbers

$$\{\theta_i\theta_j:1\le i\le j\le d\}\tag{16}$$

are linearly independent over $\mathbb Q$. Let $D_i\subset\mathbb Q$
be finite nonempty sets of size at most $m$, define $A$ by (8), and let
$n=|A|=\prod_i|D_i|$. Then

$$\boxed{\max_t\#\{(x,y)\in A^2:Q(x,y)=t\}\le m^4,
\qquad |Q(A,A)|\ge n^2/m^4.}\tag{17}$$

In particular, fixed $m$ and growing $n$ admit no fixed power saving.
More generally the same conclusion holds when $m=n^{o(1)}$.

### Proof

Condition (16) implies linear independence of the $\theta_i$ themselves:
multiply any rational linear relation by $\theta_1$, and use (16).
Thus all input representations are unique.

Write a pair of input vectors as $v_i=(a_i,b_i)\in D_i^2$. Define

$$\langle(a,b),(c,e)\rangle_Q=ac+(ae+bc)/2+be.$$

This is positive definite because $Q(a,b)=(a+b/2)^2+3b^2/4$.
Expanding the scalar polynomial gives

$$Q\left(\sum_i a_i\theta_i,\sum_i b_i\theta_i\right)
=\sum_i Q(v_i)\theta_i^2+
2\sum_{i<j}\langle v_i,v_j\rangle_Q\theta_i\theta_j.\tag{18}$$

By (16), equal scalar outputs give the same entire Gram matrix
$\bigl(\langle v_i,v_j\rangle_Q\bigr)_{i,j}$. Fix one represented
output and one such matrix.

If its rank is two, choose indices $i,j$ for which $v_i,v_j$ are
linearly independent. In any competing representation $w$, the pair
$w_i,w_j$ is also independent because its two-by-two Gram determinant
is the same positive number. There are at most $|D_i|^2|D_j|^2\le m^4$
choices for $(w_i,w_j)$. Once these are fixed, every other vector $w_k$
is uniquely determined by the two linear equations specifying its
inner products with $w_i$ and $w_j$. Their coefficient functionals are
independent since the form is nondegenerate and $w_i,w_j$ span
$\mathbb R^2$. Digit membership can only reduce this count.

If the rank is one, choose $i$ with $Q(v_i)>0$. There are at most
$|D_i|^2\le m^2$ choices for $w_i$. Every $w_k$ is then forced:
the vanishing two-by-two Gram determinant, equivalently

$$Q(w_i)Q(w_k)-\langle w_i,w_k\rangle_Q^2
=\tfrac34\det(w_i,w_k)^2=0,$$

makes $w_k$ a multiple of $w_i$, and its inner product with $w_i$
specifies that multiple. If the rank is zero, positivity forces all
$w_i=0$, allowing at most one representation. This proves the fiber
bound in every case. Partitioning the $n^2$ ordered input pairs among
their output fibers proves (17). $\square$

### Scope and arithmetic distinction

Only the faithful implication from scalar equality to equality of all
coefficients in (18) is needed. Independence (16) is a convenient
sufficient condition; faithfulness on the finite set of quadratic
differences would also suffice. This condition is stronger than input
properness or the action-faithfulness used in DC-M2.

This result does not assume polynomial height or a fixed number field.
It applies to real coefficient systems satisfying (16), irrespective
of their heights. If all $\theta_i$ belong to a number field $K$, then
(16) requires $[K:\mathbb Q]\ge d(d+1)/2$ by elementary vector-space
dimension. This is a requirement, not an available free field cost.
No existence or quantitative height assertion for a chosen field family
is needed to prove the conditional-on-projection theorem.

For ordinary integer-place-value weights, the products in (16) have
relations, so this independence theorem cannot simply be asserted.
For growing digit alphabets with $m$ a fixed positive power of $n$,
(17) alone need not exclude a saving. Algebraic coefficient systems
with quadratic relations, correlated input codes and projections with
controlled but nontrivial quadratic fibers remain outside DC-M4.

## 5.1. DC-M5 — a concrete bounded-faithfulness realization

Fix $d\ge1$, put $D=\{-1,0,1\}$, choose an integer $B\ge16$, and set

$$\theta_i=B^{3^i}\quad(0\le i\le d-1),\qquad
A_{d,B}=\left\{\sum_{i=0}^{d-1} a_iB^{3^i}:a_i\in D\right\}.\tag{19}$$

Then, without assuming rational linear independence of these integer
weights,

$$|A_{d,B}|=3^d=n,\qquad
\boxed{|Q(A_{d,B},A_{d,B})|\ge n^2/81.}\tag{20}$$

### No-carry lemma and the full-image bound

If $f(T)\in\mathbb Z[T]$ is nonzero with coefficient absolute values at
most $C$ and $B>C+1$, then $f(B)\ne0$. Indeed, if its degree is $k$,
the highest nonzero term has absolute value at least $B^k$, while the
lower terms have absolute sum at most

$$C\sum_{j=0}^{k-1}B^j
=C\frac{B^k-1}{B-1}<B^k.$$

Input differences in (19) have coefficients bounded by 2 at distinct
exponents, so this proves input injectivity. In a quadratic expansion,
the exponents $3^i+3^j$ for $i\le j$ are also distinct: their base-three
expressions have either a single digit 2 or two distinct digits 1.
There are no carries in these base-three expressions.

The coefficient of $B^{2\cdot3^i}$ in a single $Q$ value is
$a_i^2+a_ib_i+b_i^2\in\{0,1,3\}$. The coefficient of
$B^{3^i+3^j}$, $i<j$, is

$$2a_ia_j+a_ib_j+b_ia_j+2b_ib_j,$$

whose absolute value is at most 6. A difference of two $Q$ values
therefore has integer coefficients bounded by 12. The no-carry lemma
applies because $B\ge16>13$. Scalar output equality thus forces all
the coefficients in (18) to agree. This is precisely the finite
quadratic faithfulness needed by the proof of DC-M4, despite all the
weights being rationally dependent. With alphabet size $m=3$, that
proof gives fibers at most $3^4=81$, proving (20).

This is an actual-image lower bound for every $d,B$ in (19), not merely
a failed ambient support upper bound. Consequently every fixed power
saving fails once $n^c>81$.

### The selected action box and a base paying for its denominators

Reuse the already proved independent multiplier sequence from
[UE-P1](../2026-09-16-unit-exponent/primary-proof.md), Section 1, with
its fixed parameter $L=1$:

$$P_0=1,\quad t_j=3P_{j-1}^3,\quad
q_j=t_j^2+t_j+1,\quad P_j=P_{j-1}q_j,$$
$$u_j=\frac{t_j-\omega}{t_j-\bar\omega},\qquad
U_d=\left\{\prod_{j=1}^du_j^{f_j}:f_j\in\{-1,0,1\}\right\}.
\tag{21}$$

UE-P1 proves $|U_d|=3^d$ and, more strongly, that the entire generated
group contains no root of unity other than 1. This note reuses that
accepted action family; its integer scalar carrier (19) is different
from the previous orbit-coordinate and multiplicative valuation sets.

Now set the base **deterministically before defining the scalar set**:

$$B_d=100P_d.\tag{22}$$

Every $u\in U_d$ has coefficients in $P_d^{-1}\mathbb Z[\omega]$.
To verify the denominator bound directly, put $\alpha_j=t_j-\omega$;
then $u_j=\alpha_j^2/q_j$ and $u_j^{-1}=\bar\alpha_j^2/q_j$.
Multiplying one factor of exponent $-1,0,1$ for each $j$ gives the
claimed common denominator, without requiring $q_j$ to be prime.

Write the action matrix as

$$T_u=P_d^{-1}\begin{pmatrix}a&b\\c&e\end{pmatrix},
\qquad a,b,c,e\in\mathbb Z.$$

Every real coefficient of a norm-one matrix in (4) has absolute value
at most $2/\sqrt3<2$. For example,
$\alpha^2-\alpha\beta+\beta^2
=(\alpha-\beta/2)^2+3\beta^2/4=1$ bounds $\beta$; the analogous
completed squares bound $\alpha$ and $\alpha-\beta$.
Therefore $|a|,|b|,|c|,|e|<2P_d$.

For digit vectors $x_i,y_i,z_i\in D$, clearing $P_d$ from one scalar
membership equation gives coefficients

$$ax_i+by_i-P_dz_i$$

of absolute value at most $5P_d$ at exponents $3^i$. The same bound
holds for the second row. Since $B_d=100P_d>5P_d+1$, the no-carry
lemma proves the exact equivalence

$$T_u(x,y)\in A_{d,B_d}^2
\quad\Longleftrightarrow\quad
T_u(x_i,y_i)\in D^2\ \hbox{for every }i.\tag{23}$$

Both directions hold: coefficientwise returns obviously assemble to
a scalar return, and every scalar return has unique target digits to
which the no-carry argument applies. This uses the selected finite
window $U_d$; it does not assume that its denominator bound works for
all integer powers of the generators.

### Identity-only nonzero returns, analytically

For $(x,y)\in D^2$, the norm $Q(x,y)$ is 0, 1 or 3. There is one
norm-zero pair. Under $z=x-\omega y$, the six norm-one pairs give

$$z\in\{1,-1,\omega,-\omega,\omega^2,-\omega^2\},$$

and the two norm-three pairs give $z=\pm(1-\omega)$. Thus if a norm-one
multiplier sends any **nonzero** point of $D^2$ back into $D^2$, it is
a root of unity: the ratio of two norm-one points is a sixth root,
and the ratio of the norm-three points is $\pm1$.

By UE-P1, every nonidentity element of the generated group is excluded
from those possibilities. Hence every $u\in U_d\setminus\{1\}$
returns only the digit pair $(0,0)$. No assumption about the sizes of
prime factors of the composite blocks $q_j$ is used.

Together with (23) and input injectivity, this gives the exact counts
on the full new scalar square:

$$\boxed{R_{U_d}^{\rm action}(p)=1\quad(p\ne(0,0)),\qquad
R_{U_d}^{\rm action}(0,0)=3^d,}\tag{24}$$
$$\boxed{R_{U_d}^{\rm pair}(p)=1\quad\hbox{for every }p\in A_{d,B_d}^2.}
\tag{25}$$

The origin's stabilizer is the whole selected action set, but its
returned-point set is a singleton. Every nonzero point has trivial
stabilizer. Thus the supplied-action return certificate fails on the
entire square at every threshold greater than one. The image obstruction
(20) is independent of this return proof and concerns all actual
polynomial fibers, including coincidences outside $U_d$.

### Charged arithmetic size and disposition

There is no scalar input thinning, projection duplication or missing
cross-pair block: $n=3^d$ and all $n^2$ pairs are counted. Inputs are
integers, so their field degree is 1 and their denominator is 1.
The multiplier field remains $\mathbb Q(\omega)$ and its selected
common denominator is $P_d$. Carry control is paid through (22), not
assumed at a fixed small base for arbitrarily complicated actions.

The largest absolute input is exactly $\sum_{i=0}^{d-1} B_d^{3^i}$,
between $B_d^{3^{d-1}}$ and $dB_d^{3^{d-1}}$. In particular its logarithm
is between $3^{d-1}\log B_d$ and $3^{d-1}\log B_d+\log d$.
The retained recursion gives
$\log P_d=\Theta(7^d)$, so this logarithmic height is
$\Theta(21^d)$. It is not polynomial height in $n$; the actual-image
obstruction here instead follows from the explicitly paid no-carry
faithfulness. No field discriminant, regulator, prime splitting or
modular-density gain is asserted.

This concrete proposed product realization is **FAILED both as a
selected-action return certificate and as an actual power-saving
carrier**, by (24)–(25) and (20), respectively. These formulas are
proved for all $d\ge1$ and do not require a diagnostic. Any finite
scout would be corroboration only and belongs to the lead's separately
budgeted execution record, not to this symbolic subtask.

## 6. Construction ledger and disposition

No positive construction is certified. The ledger below specifies the
costs of the proposed independent-coordinate mechanism and which
obstructions actually address full images.

| Item | Action-faithful digit product | Quadratic-faithful bounded-alphabet product |
|---|---|---|
| Inputs and growing parameter | Rank $d$; exact $n=\prod n_i$ | Same exact count; $n_i\le m$ |
| Thinning in both coordinates | None; all of $A^2$ counted | None; all of $A^2$ counted |
| Parameter/scalar fibers | One under the stated linear faithfulness | One, implied by quadratic faithfulness |
| Exact real projection | (8), with rational digits; membership proof in Section 3 | (8), equality proof in Section 5 |
| All ordered pairs | Product identity (9), no selected orbit core | Every output fiber bounded in (17) |
| Actual actions and duplicates | $G$ is a set of distinct multipliers; at most two unmixed actions | No action count is used |
| Nontrivial action loss | At least $\log(9/7)$ per active digit in the summed-return upper bound | Not used or double-counted |
| Zero, signs, branches | Origin has action stabilizer but one returned point; $\pm1$ separated explicitly | Rank-zero and rank-one cases included; all signed digit pairs counted |
| Norm shells or auxiliary states | None omitted or claimed to cover the square | Full Gram data retained, not treated as a scalar support upper bound |
| Denominators and carries | Rational actions/digits must satisfy the stated membership equations; no-carry condition is explicit when used | No denominator saving; all rational coefficient equalities exact |
| Field degree/discriminant/regulator | No arithmetic-field count claimed; changing to nonrational mixing actions leaves DC-M2's scope | Field degree at least $d(d+1)/2$ if (16) is realized in a field; no discriminant or regulator gain credited |
| Local moduli/splitting | Inapplicable to these proofs; no modular gain asserted | Inapplicable; no local-to-real transfer asserted |
| Heights and archimedean distortion | Arbitrary in DC-M1/2; the displayed finite no-carry example charges fixed $H,K,B$ | Arbitrary under the equality-faithfulness premise; no missing height estimate is set to zero |
| Exceptional/uncovered pairs | Necessary tail test (14); no positive tail established | No exceptions in (17) |
| Input/output rates | If $n=e^{ad+o(d)}$, action count alone gives no image exponent | Fixed $m$, $a>0$: $\log|Q(A,A)|=2ad+o(d)$ from (17) and $|Q(A,A)|\le n^2$ |
| Signed gap | Unknown for unconstrained many-action families; impossible for claims violating (14) | Zero for fixed $m$ or $m=n^{o(1)}$ |

**Disposition.** Conventional Cartesian Følner invariance under a
nontrivial mixing norm action is **FAILED universally**, by DC-M1.
The independent rational digit-action route pays the exact tensor loss
DC-M2 and must satisfy DC-M3; it is not universally closed by that cost
alone. Quadratic-faithful bounded-alphabet products are **FAILED actual
carriers**, by DC-M4. These are different scopes and must not be merged
into a no-go theorem for all GAPs or all dense Cartesianization.

No finite scout is needed to verify these analytic statements. A
genuinely different candidate may use many partially returning actions,
nonrational coordinate mixing, correlated digits or nontrivial quadratic
projection relations, but this note supplies no construction or tail for
any of them. The fixed T03 target and RC15/4 remain **OPEN**.
