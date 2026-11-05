# Balanced alphabet states and rectangular compatibility

**Date/version:** 21 September 2026, version 1. **Track:** T03 / DC-O1.
**Fixed polynomial:** $Q(x,y)=x^2+xy+y^2$ on real inputs.

This is a bounded symbolic part of the newly authorized, strictly offline
DC-O1 cycle. It studies fixed-alphabet powers, balanced state unions and
one explicit asymmetric local gadget. It uses **zero mathematical program
runs or evaluations**, no network, no external theorem and no novelty
claim. Only this new note is authored. The arguments below are internally
derived and checked; an independent review, if performed, is recorded
separately by the lead.

## Identity, dependencies and status

The active obligation is [DC-O1](../2026-09-21-dense-cartesianization/README.md),
§12: a high-overlap rectangular witness with growing distinct scalar
returns and a power-saving exceptional set. The sufficient transport
statement is [DC-R1](../2026-09-21-dense-cartesianization/block-rectangle.md),
§4. Neither has a new successful witness here. The earlier complete-block
obstruction DC-B2 is context; the proofs below count state-compatible
partial domains directly and do not invoke it.

| Claim | Status and exact scope | Proof |
|---|---|---|
| DC-TB1 | PROVED: exact overlap of two fixed-alphabet powers under a common injective word encoding; exclusive-letter type classes cannot create overlap | §1 |
| DC-TB2 | PROVED: for disjoint coordinate alphabets and a complement-closed pattern family, the same-set union has complementary-state pair fraction at most the reciprocal of the number of patterns | §2 |
| DC-TB3 | PROVED: exact distinct-word and compatible-pair counts for all balanced patterns with possibly overlapping fixed alphabets; exponentially sparse compatibility for distinct equal-size alphabets | §3 |
| DC-TB4 | PROVED: an explicit rational norm-one gadget on $\{\pm1\}\times\{\pm3\}$, its balanced-state input counts and its complementary-state certificate costs | §§4–5 |

The status **FAILED** below concerns the specified complementary-state
certificate for a power-saving bad-pair bound. It is not an upper bound
on the actual rich-pair population under other legal scalar actions, an
actual-image lower bound, or a universal obstruction to DC-O1. The
companion [tensor-compatibility note](tensor-compatibility.md) separately
studies scalar assembly of local rotations; no result from that note is
needed for the combinatorial proofs here.

## 1. DC-TB1 — fixed support and raw tensor powers

Let $S,T\subset\mathbb R$ be finite and nonempty. Write
$m=|S|$, $\ell=|T|$, $h=|S\cap T|$. Suppose a common map
$\Phi_d:(S\cup T)^d\to\mathbb R$ is injective. For
$X_d=\Phi_d(S^d)$ and $Y_d=\Phi_d(T^d)$, injectivity gives exactly

$$|X_d|=m^d,\quad |Y_d|=\ell^d,\quad
|X_d\cap Y_d|=h^d,$$
$$n_d:=|X_d\cup Y_d|=m^d+\ell^d-h^d,\qquad
|X_d\triangle Y_d|=m^d+\ell^d-2h^d=n_d-h^d.\tag{1}$$

If $S\ne T$, then $M:=\max(m,\ell)>h$ and

$$\frac{h^d}{n_d}\le(h/M)^d\longrightarrow0.\tag{2}$$

Consequently, whenever $n_d\to\infty$, this construction fails
$|X_d\triangle Y_d|\le Cn_d^{1-\eta}$ for every fixed $C$ and
$\eta>0$. Indeed, its symmetric difference is $(1-o(1))n_d$.

Taking a type class does not change the support restriction: for any
$\mathcal X\subseteq S^d$ and $\mathcal Y\subseteq T^d$,

$$\mathcal X\cap\mathcal Y\subseteq(S\cap T)^d.\tag{3}$$

In particular, a type class requiring at least one letter in
$S\setminus T$ is disjoint from every $T$-supported class. More
generally its overlap with a $T$-supported class is at most $h^d$.
This does not prohibit discarding the exclusive letters and working
entirely inside the common alphabet; that is a separate input choice
whose two-coordinate thinning must be charged.

## 2. DC-TB2 — exact equality by balancing disjoint states

### General coordinate alphabets and arbitrary pattern families

For each $1\le i\le d$, fix nonempty disjoint sets $S_i,T_i$ with
sizes $m_i,\ell_i$. For $I\subseteq[d]$, set

$$V_I=\prod_{i=1}^d W_i(I),\qquad
W_i(I)=\begin{cases}S_i&i\in I,\\T_i&i\notin I.\end{cases}$$

The word blocks $V_I$ are pairwise disjoint. Let $\mathcal P$ be a
nonempty collection of patterns closed under complementation. Put
$k=|\mathcal P|$ and

$$\mathcal A=\bigcup_{I\in\mathcal P}V_I,
\qquad \mathcal X=\bigcup_{I\in\mathcal P}V_I,
\qquad \mathcal Y=\bigcup_{I\in\mathcal P}V_{I^c}.$$

Then $\mathcal X=\mathcal Y=\mathcal A$. A common injective scalar
encoding preserves this exact equality and every count below. For
$d\ge1$, complementation has no fixed pattern, so $k\ge2$ is even.

Suppose the local gadget only certifies a coordinate pair when its two
letters have opposite states, one in $S_i$ and the other in $T_i$.
Its compatible ordered-pair set is precisely

$$\mathcal C_{\mathcal P}
=\bigsqcup_{I\in\mathcal P}(V_I\times V_{I^c}).\tag{4}$$

Write

$$w_I=|V_I|=\prod_{i\in I}m_i\prod_{i\notin I}\ell_i,
\qquad W=\prod_{i=1}^dm_i\ell_i.$$

Since $w_Iw_{I^c}=W$, disjointness gives the exact identities

$$n=|\mathcal A|=\sum_{I\in\mathcal P}w_I,
\qquad G_{\rm cert}:=|\mathcal C_{\mathcal P}|=kW.\tag{5}$$

For each unordered complementary pair of patterns,
$w_I+w_{I^c}\ge2\sqrt W$. Summing the $k/2$ inequalities proves

$$n\ge k\sqrt W,\qquad
\boxed{\frac{G_{\rm cert}}{n^2}\le\frac1k\le\frac12.}\tag{6}$$

Thus the unhandled population for this certificate satisfies

$$B_{\rm cert}:=n^2-G_{\rm cert}
\ge n^2(1-1/k)\ge n^2/2.\tag{7}$$

This result permits arbitrary coordinate-dependent alphabet sizes,
including multiscale choices. Such size balancing cannot remove the
quadratic unhandled population of the complementary-state certificate.
The set in (4) is **not defined as the actual rich-pair set**. Other
actions may return pairs outside it; (7) makes no claim about those.

### All balanced patterns

Let $d=2r\ge2$, use the same disjoint alphabets $S,T$ in every
coordinate, and take every $r$-element pattern. Then

$$k=\binom d{d/2},\qquad
w_I=(m\ell)^{d/2},$$
$$n=\binom d{d/2}(m\ell)^{d/2},\qquad
G_{\rm cert}=\binom d{d/2}(m\ell)^d,\qquad
\frac{G_{\rm cert}}{n^2}=\binom d{d/2}^{-1}.\tag{8}$$

The central binomial coefficient is the largest of the $d+1$
coefficients whose sum is $2^d$, so

$$\binom d{d/2}\ge\frac{2^d}{d+1},\qquad
\frac{G_{\rm cert}}{n^2}\le\frac{d+1}{2^d}.\tag{9}$$

Exact same-set equality has been achieved, but almost every ordered
pair lies outside this compatibility certificate. The number of masks
has exponential rate $\log2$; it is not an $e^{o(d)}$ cost. Restricting
to a complement-closed family with $k=e^{o(d)}$ changes the counts but
retains (7), since $k\ge2$.

## 3. DC-TB3 — overlapping balanced alphabets, counted without duplicate masks

This section is a general combinatorial comparison, not an additional
scout or proposed carrier. Let $d=2r\ge2$ and allow $S,T$ to overlap.
Write

$$C=S\cap T,\quad h=|C|,\quad
a=|S\setminus T|,\quad b=|T\setminus S|.$$

Let $\mathcal A_{\rm bal}$ be the union of $V_I$ over all
$|I|=r$. Complementation again makes the two unions equal. A word
with $i$ letters exclusive to $S$, $j$ exclusive to $T$, and $c$
common letters belongs to this union exactly when $i\le r$ and
$j\le r$; here $i+j+c=d$. Therefore its **distinct word** count is

$$n_d=\sum_{\substack{i,j\ge0,\ i+j\le d\\i\le r,\ j\le r}}
\frac{d!}{i!j!(d-i-j)!}\,a^i b^j h^{d-i-j}.\tag{10}$$

The convention $0^0=1$ is the usual empty-choice convention. A word
with these counts has $\binom c{r-i}$ admissible masks. Counting all
block incidences would therefore overcount its multiplicity.

Consider the compatible pair union
$\mathcal C_{\rm bal}=\bigcup_{|I|=r}V_I\times V_{I^c}$.
There are $h^2$ local pairs in $C\times C$, each allowing either
orientation. Of the other legal local pairs, exactly

$$g=|S||T|-h^2=(a+h)(b+h)-h^2$$

force the $S\times T$ orientation, and exactly $g$ force the reverse
orientation. These three classes are disjoint. A pair word with $p$
forced forward coordinates, $q$ forced reverse coordinates, and
$f=d-p-q$ flexible coordinates is compatible exactly when $p\le r$
and $q\le r$. It has $\binom f{r-p}$ compatible masks, but is one
ordered pair. Thus the exact **distinct pair** count is

$$G_d=\sum_{\substack{p,q\ge0,\ p+q\le d\\p\le r,\ q\le r}}
\frac{d!}{p!q!(d-p-q)!}\,g^{p+q}h^{2(d-p-q)}.\tag{11}$$

These formulas include the disjoint case of (8). They also explicitly
charge mask duplication in the overlapping case.

For a useful scoped consequence, suppose $|S|=|T|=s$ and $S\ne T$.
Then $a=b=s-h>0$. Put $v=|S\cup T|=2a+h$ and

$$K=|(S\times T)\cup(T\times S)|=2s^2-h^2
=v^2-2a^2<v^2.$$

Dropping the balance restriction gives $G_d\le K^d$. To lower-bound
$n_d$, choose each word coordinate uniformly from $S\cup T$.
An exclusive letter forces its state; assign a common letter a state
by an independent fair coin. Each resulting state bit is fair, since
the two exclusive alphabets have equal size. The probability of a
balanced assigned mask is $\binom dr/2^d\ge1/(d+1)$. Every word
having such an assignment belongs to $\mathcal A_{\rm bal}$.
Consequently

$$n_d\ge\frac{v^d}{d+1},\qquad
\frac{G_d}{n_d^2}\le(d+1)^2\left(\frac K{v^2}\right)^d
\longrightarrow0.\tag{12}$$

For distinct fixed equal-size alphabets, even allowing a common
alphabet and duplicate masks leaves an exponentially small
complementary-state compatible fraction. No analogous asymptotic
claim for every unequal-size overlapping choice is inferred from
(12); the general exact counts remain (10)–(11).

## 4. DC-TB4 — an explicit two-domain gadget

Fix $\omega=(-1+i\sqrt3)/2$, and identify $(x,y)$ with $x-\omega y$.
Then $N(x-\omega y)=Q(x,y)$. For $u=a+b\omega$ with norm one,

$$T_u(x,y)=(ax+by,-bx+(a-b)y),\qquad
N(u)=a^2-ab+b^2=1.\tag{13}$$

Take the fixed disjoint alphabets

$$S=\{-1,1\},\qquad T=\{-3,3\},$$
$$u_+=\frac{15+8\omega}{13},\qquad
u_-=\frac{3+8\omega}{7}.\tag{14}$$

Their norms are respectively $(225-120+64)/169=1$ and
$(9-24+64)/49=1$. Their matrices are

$$T_{u_+}=\frac1{13}\begin{pmatrix}15&8\\-8&7\end{pmatrix},
\qquad
T_{u_-}=\frac1{7}\begin{pmatrix}3&8\\-8&-5\end{pmatrix}.\tag{15}$$

For both signs $\sigma\in\{-1,1\}$,

$$T_{u_+}(\sigma,3\sigma)=(3\sigma,\sigma),\qquad
T_{u_-}(\sigma,-3\sigma)=(-3\sigma,\sigma).\tag{16}$$

Each action has a legal domain of two of the four pairs in
$S\times T$, with target in $T\times S$. The other two source
pairs are not legal for that reverse rectangle: their first output
coordinate is respectively $-9\sigma/13$ or $27\sigma/7$, neither
in $T$. Thus these are different partial domains, not complete-block
inclusions or returns to the original orientation. Since
$T_{\bar u}=T_u^{-1}$, the conjugates handle the reverse domains.

For clarity define the fixed actual action set

$$U=\{\pm1,\ \pm u_+,\ \pm\bar u_+,\
\pm u_-,\ \pm\bar u_-\}.\tag{17}$$

It has ten distinct elements. The absolute $\omega$ coefficients
separate the identity, denominator-13 and denominator-7 groups; the
four signed elements within each nonidentity group have different
coefficient pairs. All are norm one.

On $\mathcal C=(S\times T)\cup(T\times S)$, the norm is 13 for
same-sign pairs and 7 for opposite-sign pairs. Each norm shell has
four points. The actions $\pm1$ give two points in the source
orientation; the appropriate two signed actions from (16), or their
conjugates, give the other two points in the opposite orientation.
Every source in $\mathcal C$ therefore has exactly four distinct
returned points in $\mathcal C$ under $U$.

These are also its only possible equal-norm targets in
$(S\cup T)^2$: pairs in $S^2$ have norm 1 or 3, and pairs in $T^2$
have norm 9 or 27. All eight sources in $\mathcal C$ are nonzero.
For any nonzero source, equality of two returned pairs forces the
two actual multipliers equal, by cancellation in $\mathbb C$.
There are no stabilizer or zero-label gains in this statement.

## 5. Balanced real inputs and what the gadget does not certify

For each even $d\ge2$, use all balanced patterns from §2 and the
alphabets in (14). The word carrier consists exactly of the words
in $\{\pm1,\pm3\}^d$ having $d/2$ letters of each magnitude. Fix
the scalar encoding, before $d$ grows, by

$$\Phi_d(w)=\sum_{i=0}^{d-1}w_i100^i.\tag{18}$$

It is injective on the entire word alphabet. If two words differ,
let $j$ be their largest differing index. The leading difference
has absolute value at least $100^j$, while the smaller differences
have total absolute value at most
$6(100^j-1)/99<100^j$. Cancellation is impossible. Likewise no
word has scalar value zero: its leading term has absolute value at
least $100^{d-1}$ and its smaller terms have total absolute value
at most $3(100^{d-1}-1)/99$.

Let $X_d$ be the encoded union over balanced masks and $Y_d$ the
encoded union over their complements. These are the same real set
$A_d$, and the exact counts are

$$X_d=Y_d=A_d,\qquad
n_d=\binom d{d/2}2^d,$$
$$G_{\rm cert}=\binom d{d/2}4^d,\qquad
B_{\rm cert}=n_d^2-G_{\rm cert}.\tag{19}$$

Here $G_{\rm cert}$ counts source pairs whose digit magnitudes are
opposite at every position, as in (4). It is a compatibility
population, **not an experimentally measured high-return population**.
For the two planned balanced scouts, the symbolic counts are:

| Depth $d$ | Masks | $n_d$ | $n_d^2$ | $G_{\rm cert}$ | $B_{\rm cert}$ |
|---:|---:|---:|---:|---:|---:|
| 2 | 2 | 8 | 64 | 32 | 32 |
| 4 | 6 | 96 | 9,216 | 1,536 | 7,680 |

For each compatible pair, the coordinatewise vector model allows
independent choices of a balanced target mask and two signs at each
coordinate within the preserved local norm shell. It has exactly
$\binom d{d/2}2^d$ such compatible vector targets. This is a count
in $\mathbb R^{2d}$ with a separate local rotation at each coordinate.
**None of these products is credited as a scalar norm-one return.**
Input injectivity of (18) does not prove that these block actions
preserve the scalar polynomial $Q(\Phi_d(w),\Phi_d(v))$ or arise
from a single scalar multiplier.

The scouts instead use the ten actual scalar actions (17), applying
each action directly to the two scalar inputs. Their legal returns
must be measured or proved at the scalar level. At most ten distinct
returns can be supplied by that fixed action set, regardless of $d$;
it is a finite diagnostic and supplies no growing return exponent.
The symmetric carrier guarantees the two distinct scalar returns
from $\pm1$ at every pair, since neither scalar input is zero. No
claim about its other scalar returns is made in this note.

Even granting arbitrarily large genuine return counts on the
compatible population in (19), leaving its complement untreated
would give $B_{\rm cert}=n_d^2(1-o(1))$. That certificate cannot
satisfy the required power-saving exceptional-set bound. A successful
continuation would have to certify the cross-state pairings as well,
or use a different mechanism whose good set is larger than (4).

## 6. Construction ledger and disposition

The quantitative entries below concern the selected disjoint balanced
carrier (18)–(19). The general lemmas have their own explicit finite
counts above. The actual growing parameter is the even word depth $d$.
All digits, the base 100 and the local actions are fixed first.

| Gain or cost | Exact bound or charged rate | Status / reason |
|---|---|---|
| Inputs before balancing | $4^d$ words | Exact |
| Input thinning, both coordinates | $n_d=\binom d{d/2}2^d$; proportion at least $1/(d+1)$ per coordinate, at least $1/(d+1)^2$ on the square | Polynomial losses, both charged |
| Input lower and upper counts | $4^d/(d+1)\le n_d\le4^d$ | Proved in (9), (19) |
| Word/projection multiplicity | One; masks unique because $S\cap T=\varnothing$ | Input injectivity proved after (18) |
| Same-set transport | $X_d=Y_d=A_d$; symmetric difference zero | Exact equality, not a return certificate |
| Local sparsity and splitting | No local sieve or splitting choice | Inapplicable to this rational digit construction |
| Uniform per-residue population | No residue population estimate used | Inapplicable; exact word counts used instead |
| Field degree / discriminant | Inputs in $\mathbb Q$, action field $\mathbb Q(\omega)$ of fixed degree two and discriminant $-3$ | Constant; no degree-based asymptotic gain |
| Regulator / unit rank | No regulator or growing unit-rank estimate used | Inapplicable to the fixed ten multipliers |
| Denominators / local moduli | Integral scalar inputs; action denominators divide 7 or 13 | Constant but membership must still be checked exactly |
| Heights / archimedean radius | $|a|\le3(100^d-1)/99$; $Q(a,b)\le3[3(100^d-1)/99]^2$ | Bounds only; volume is not used to count the image |
| Carries and scalar assembly | Input carries excluded by leading-term proof; product-action or quadratic faithfulness not asserted | No unproved transfer is credited |
| Masks / branches | $\binom d{d/2}$ masks, exponential rate $\log2$ | Included in both input and compatible-pair counts |
| Actual distinct actions | Ten in the selected diagnostic; actual return count at most ten | No positive growing return rate |
| Formal target choices | $\binom d{d/2}2^d$ vector targets on compatible pairs | Zero scalar-return credit |
| Exceptions / uncovered pairs | $B_{\rm cert}=n_d^2[1-\binom d{d/2}^{-1}]$ | Full ordered complement charged |
| Final input rates | $a=B=\log4$, so $\log n_d=d\log4+O(\log d)$ | Proved |
| Certificate output rate | Only the trivial rate $2\log4$ is certified for the entire image | No power-saving support bound obtained |
| Net $\delta$ and fixed saving | $\delta=2\log4-2\log4=0$; no $c>0$ certified | Scoped certificate FAILED |

No experiment, run hash, seed or runtime is claimed by this symbolic
subtask. The finite scout code and its results belong to the lead's
separate experiment record. The two small rows in §5 are direct
substitutions into an exact formula, not a computational run.

The substantive positive result is a concrete local pair of different
legal domains and an exact same-set state construction. The retained
gaps are genuine scalar action assembly with a growing action family
and coverage of the cross-state pairs. Neither gap is filled by mask
balancing. This note makes no universal impossibility, actual-image
lower-bound, RC15/4, or general quadratic claim.
