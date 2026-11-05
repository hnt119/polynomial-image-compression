# MP-1 — Correlated words and moving polynomial return domains

21 September 2026; T03/DC-O1; fixed $Q(x,y)=x^2+xy+y^2$.
**PROVED:** the explicitly defined action family below has $3^d$
distinct multipliers, but at most 27 distinct returns at every pair.
This is a return-certificate obstruction, not an actual-image lower bound.

## Statement

For every integer $d\ge1$, choose

$$B_d=[10(d+2)]^{4d},\qquad
\mathcal C_d=\{(a_0,\ldots,a_{d-1})\in\{-1,0,1\}^d:
\sum_i a_i=0\},$$
$$X_d=Y_d=A_d=\{\sum_{i=0}^{d-1}a_iB_d^i:a\in\mathcal C_d\}.$$

For $1\le j\le d$, first prescribe the rational-function actions

$$v_j(T)=\frac{T-j-\omega}{T-j-\bar\omega},\qquad
u_j=v_j(B_d),\qquad
U_d=\{\prod_{j=1}^d u_j^{e_j}:e_j\in\{-1,0,1\}\}.$$

All these elements have norm one. Their proposed return domains are
determined by divisibility of $f(T)-\omega g(T)$ at the poles, followed
by the requirement that the transformed coefficients remain balanced
ternary words. Different poles provide different partial domains; no
whole block is required to map to one target block.

Then

$$\frac{3^d}{2d+1}\le n_d:=|A_d|=|\mathcal C_d|\le3^d,
\qquad |X_d\triangle Y_d|=0,\qquad |U_d|=3^d,$$
$$\boxed{R_{\rm pair}(p)\le27\quad\text{for every }p\in A_d^2.}$$

Consequently every fixed $\varepsilon>0$ eventually has
$B_\varepsilon=n_d^2$. No positive $\delta$ is available for this
action certificate. These conclusions are uniform in $d$; the small
$d=1$ singleton does not affect $n_d\to\infty$.

## Meaning

The coordinate alphabets are exactly equal, and the action count is
exponential. The digits are correlated by a common sum constraint, and
consecutive place values have many quadratic relations. Thus this is
not the earlier independent faithful-quadratic digit carrier. Its
failure comes instead from the locations of the polynomial poles:
only the first three can divide a nonzero bounded-coefficient word.

## Consequence

This specified moving-pole design fails the return exponent even though
the overlap exponent has no cost. It does not rule out poles in a
bounded region with growing algebraic complexity, other coefficient
alphabets, or correlated return domains that do not factor this way.
No new search in those directions is adopted here.

### Proof: exact scalar counts

Every difference of two digit polynomials has integer coefficients
bounded by 2. Its highest nonzero term dominates all lower terms at
$B_d>3$, so the scalar encoding is injective. Let $c_d(s)$ count words
with sum $s$. It is symmetric and nonincreasing for $s\ge0$:
inductively,

$$c_d(s)-c_d(s+1)=c_{d-1}(s-1)-c_{d-1}(s+2)\ge0.$$

For $s=0$, symmetry changes the first argument to 1, and the same
inequality applies. The base case is immediate. Since the $2d+1$
possible sums have total population $3^d$, their largest, $c_d(0)$,
is at least $3^d/(2d+1)$. This gives
$\log n_d=d\log3+O(\log d)$.

### Proof: evaluation faithfully preserves the required identities

For a polynomial $F(T)$ in $\mathbb Z[\omega][T]$, every nonzero
leading coefficient has complex absolute value at least one, because
its squared absolute value is a positive integer. If the sum of the
absolute values of its coefficients is at most $C$ and $B>C+1$,
the leading term at $B$ exceeds the sum of the lower terms. Therefore
$F(B)=0$ implies $F=0$ under this bound.

Write a word in the rational functions as $N_e(T)/D_e(T)$, with monic
numerator and denominator formed from at most $d$ factors each. In fact
each has at most $d$ factors, and for our estimates this upper bound
suffices. Each linear factor has coefficient absolute-value sum at
most $d+2$, so

$$\|N_e\|_1,\|D_e\|_1\le(d+2)^d.$$

For scalar pair words, $z(T)=f(T)-\omega g(T)$ has
$\|z\|_1\le2d$. Thus a putative scalar return, after clearing its
denominator, is the evaluation of

$$F(T)=z'(T)D_e(T)-z(T)N_e(T),\qquad
\|F\|_1\le4d(d+2)^d.$$

Our $B_d$ exceeds this bound plus one. A scalar return therefore
implies the exact polynomial identity $z'D_e=zN_e$; the converse also
holds if both coefficient pairs are legal balanced words.

Likewise, equality of two action values gives
$N_eD_f-N_fD_e$ with coefficient sum at most $2(d+2)^{2d}<B_d-1$.
It therefore gives equality of rational functions. All roots
$j+\omega$ and $j+\bar\omega$ are distinct: different $j$ have
different real parts and conjugate roots have different imaginary
parts. The zero or pole at each such root recovers $e_j$, so the
actions in $U_d$ are distinct. This is only the stated finite window;
no evaluation-faithfulness assertion for arbitrary integer powers is
being made.

### Proof: the root bound excludes every later return domain

For nonzero $z=f-\omega g$, every coefficient has absolute value at
most 2 and its leading coefficient has absolute value at least one.
If $|w|>3$, then

$$\left|\sum_{i<k}z_iw^i\right|
\le2\frac{|w|^k-1}{|w|-1}<|w|^k\le|z_kw^k|.$$

Hence $z(w)\ne0$. For $j\ge4$,

$$|j+\omega|^2=|j+\bar\omega|^2=j^2-j+1\ge13>9.$$

Suppose $e_j\ne0$ for such a $j$ in a nonzero returned pair. A
root of the corresponding denominator factor is outside the radius-3
disk. The numerator does not vanish there, since all factor roots are
distinct. Evaluating $z'D_e=zN_e$ at this root forces $z$ to vanish
there, a contradiction. Therefore every returning action at a nonzero
pair has $e_j=0$ for all $j\ge4$. There are at most
$3^{\min(d,3)}\le27$ remaining action words. At zero all $3^d$
actions fix the same pair, giving one distinct return. This proves the
theorem without enumerating any carrier.

### Construction and signed-rate ledger

| Item | Exact accounting |
|---|---|
| Fixed choices, growth | Ternary digits, zero coefficient sum, width-one powers and displayed base recipe are fixed before integer $d\to\infty$. |
| Input lower and upper counts | $3^d/(2d+1)\le n_d\le3^d$; rate $a=\log3$. No thinning beyond the explicitly counted correlation. Both coordinates use this same set. |
| Scalar/projection fibers | One, by the separate linear evaluation bound. Quadratic coefficient faithfulness is neither claimed nor needed. |
| Actual actions | Exactly $3^d$; numerator/denominator comparison proves distinctness at the chosen scalar base. |
| Return exponent | $R_{\rm pair}\le27$, so no fixed positive $\varepsilon$ is possible. |
| Symmetry exponent | Symmetric difference zero, satisfying every fixed positive $\eta$. |
| Bad pairs | For every fixed $\varepsilon>0$ and all sufficiently large $d$, exactly $n_d^2$ pairs have fewer than $n_d^\varepsilon$ distinct returns. |
| Stabilizers | One at nonzero pairs; zero has all action labels but one returned pair. |
| Arithmetic | Fixed field $\mathbb Q(\omega)$, degree two, discriminant $-3$. All scalars integral. For $t_j=B_d-j$, each multiplier has denominator dividing $t_j^2+t_j+1$; a selected word has common denominator dividing their product. No regulator, class-number, splitting or ideal-count estimate is used. |
| Heights/denominators | $\log B_d=O(d\log d)$, $\log\max(1,|A_d|_{\rm height})=O(d^2\log d)$, and logarithm of the common denominator is $O(d^2\log d)$. These are charged explicitly, not called polynomial in input size. |
| Domains and local factors | All pole indices $j\ge4$ have empty nonzero return domains. The remaining three are not assumed to return every pair. |
| Final rate | Pair-return certificate has $\varepsilon=0$ and no fixed bad-tail deficit; no $c>0$. Actual $Q$-image rate remains OPEN for this family. |

### Evidence and provenance

This is a new local symbolic proof, not an application of the old
faithful-quadratic image theorem. It uses only the elementary Eisenstein
norm, polynomial arithmetic and the explicitly proved leading-term/root
bounds. No missing external input, novelty claim or network access.
The finite scout at $d=3,4,5$ uses the same definitions and is separate
from the proof. Independent internal audit is recorded in the cycle's
verification note. No historical source was changed.
