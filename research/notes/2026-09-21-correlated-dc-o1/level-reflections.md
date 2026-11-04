# Linear-level reflections and genuine correlated returns

**Date/version:** 21 September 2026, version 1. **Track:** T03, correlated
DC-O1. **Fixed polynomial:** $Q(x,y)=x^2+xy+y^2$ on real inputs.

This is one bounded mechanism: pair-dependent global reflections and
transfers between levels of a nonzero linear function. It is not a
search over norm levels, independent tensor rotations or arithmetic
factor-divisibility families. The current local assignment is
`[private task attachment]`.
The work is strictly offline and symbolic, with **zero mathematical
program runs or evaluations**, no imported external result and no novelty
claim. Only this new companion is authored.

| Claim | Exact scope and status | Proof |
|---|---|---|
| CR-L1 | **PROVED:** exact norm coordinates for every nonzero real linear $H$, a global $H$-preserving reflection, and its genuine pair-indexed multiplier | §1 |
| CR-L2 | **PROVED:** at most two equal-norm targets per prescribed $H$-level, hence at most $2k$ returns in a $k$-target-level certificate, including pair-dependent choices of levels | §2 |
| CR-L3 | **PROVED:** an affine transfer between two fixed parallel levels is either one of four symmetry restrictions or is norm preserving at at most two source points; exact library-incidence bound | §3 |
| CR-L4 | **PROVED:** a symmetric interval realizes the four symmetries on every pair, with an exact bounded certificate distribution | §4 |

These are complete new internal derivations. The independent audit by `norm_trace` and the lead inspection both
passed, as recorded in the cycle verification. A bound on
the level-constrained certificate is carefully distinguished below from
the full return count under the union of its pair-indexed multipliers.

## 1. CR-L1 — an exact global correlation

### Statement

Fix real $\alpha,\beta$, not both zero, before defining the levels. Put

$$D=\alpha^2-\alpha\beta+\beta^2>0,\qquad
H(x,y)=\alpha x+\beta y,$$
$$J(x,y)=(2\beta-\alpha)x-(2\alpha-\beta)y,$$
$$w=(w_1,w_2)=(2\alpha-\beta,\,2\beta-\alpha).$$

The exact scalar identity and inverse coordinate map are

$$\boxed{4D Q(x,y)=3H(x,y)^2+J(x,y)^2,}\tag{1}$$
$$x=\frac{w_1H+\beta J}{2D},\qquad
y=\frac{w_2H-\alpha J}{2D}.\tag{2}$$

The reflection

$$S_H(p)=\frac{H(p)}D w-p\tag{3}$$

satisfies $H(S_Hp)=H(p)$, $J(S_Hp)=-J(p)$ and $Q(S_Hp)=Q(p)$.
For nonzero $p=(x,y)$, let $z=x-\omega y$ and
$\nu=w_1-\omega w_2$, where $\omega=(-1+i\sqrt3)/2$. Then

$$z_{S_Hp}=\frac{\nu}{\bar\nu}\bar z,\qquad
\boxed{u_H(p)=\frac{z_{S_Hp}}z
=\frac{\nu}{\bar\nu}\frac{\bar z}z,\quad |u_H(p)|=1.}\tag{4}$$

Thus (3) is implemented at each nonzero input by a genuine norm-one
multiplier. The multiplier generally depends on the entire pair.

**Proof.** The coefficients of $x^2,xy,y^2$ in $3H^2+J^2$ are,
respectively,

$$3\alpha^2+(2\beta-\alpha)^2=4D,$$
$$6\alpha\beta-2(2\beta-\alpha)(2\alpha-\beta)=4D,$$
$$3\beta^2+(2\alpha-\beta)^2=4D.$$

This expands the cross term and proves (1). The matrix of $(H,J)$ has determinant
$-2D$, so (2) follows by inversion. Also $H(w)=2D$ and $J(w)=0$,
which prove the stated effects of (3) on the two coordinates. Equation
(1) then proves norm preservation, including all scalar cross terms.

For the complex formula, use the polarized form

$$B_Q((x,y),(s,t))=xs+(xt+ys)/2+yt
=\operatorname{Re}((x-\omega y)\overline{(s-\omega t)}).$$

Direct substitution gives $B_Q(w,p)=3H(p)/2$ and $Q(w)=3D$.
Consequently $|\nu|^2=3D$ and

$$\frac{H(p)}D\nu-z
=\frac{\nu\bar z+\bar\nu z}{3D}\nu-z
=\frac{\nu}{\bar\nu}\bar z.$$

Division by nonzero $z$ gives (4). Positivity of $Q$ makes $z=0$
equivalent to $p=(0,0)$; there the sole reflected target is zero and
one may use the identity multiplier. $\square$

### Meaning

The reflection operates on the full scalar pair, so it preserves cross
terms without independently rotating internal components. It is an
orientation-reversing linear map, not one fixed multiplication by a
complex number; equation (4) supplies the correct input-dependent action.

### Consequence

This is **CORRELATED GO** at the exact identity stage. Membership of
$S_Hp$ in the chosen rectangle is still a separate condition. One such
reflection supplies one additional target at most, regardless of how
many parameter descriptions produce its multiplier.

## 2. CR-L2 — the exact capacity of target levels

### Statement

For a fixed source $p$, put $s=H(p)$ and $r=J(p)$. A target $q$ with
$Q(q)=Q(p)$ and $H(q)=t$ must have

$$J(q)=\pm\sqrt{r^2+3(s^2-t^2)}.\tag{5}$$

It exists over the reals only when the radicand is nonnegative; its
coordinates are then given exactly by (2) with $H=t$. Thus each target
level contains at most two equal-norm points, even before imposing
membership in $X\times Y$.

Let $\Lambda(p)\subset\mathbb R$ be any prescribed set of at most
$k$ target levels, allowed to depend on the source pair or just its
source level. Define the certificate's returned set by

$$\mathcal R_\Lambda(p)=
\{q\in X\times Y:Q(q)=Q(p),\ H(q)\in\Lambda(p)\}.$$

Then

$$\boxed{|\mathcal R_\Lambda(p)|\le2k.}\tag{6}$$

For nonzero $p$, every distinct target counted here gives one distinct
actual norm-one multiplier $u=z_q/z_p$. At zero there is only one
possible target, irrespective of level or action labels.

In particular, an $H$-preserving certificate has only the targets
$p,S_Hp$. A certificate using the two levels $s,-s$ has only

$$p,\quad S_Hp,\quad -p,\quad -S_Hp.\tag{7}$$

**Proof.** Substitute $H(q)=t$ and $Q(q)=Q(p)$ into (1), then use
the invertible coordinates (2). The two square-root signs coincide
when the radicand is zero. Distinctness of the ratios at a nonzero
source follows by cancellation of $z_p$. This proves all assertions.
$\square$

There is also a separate source-coverage bound. If source pairs are
restricted to $k$ fixed global levels of $H$, at most $kn$ pairs of
$X\times Y$ are covered, where $n=|X\cup Y|$. Indeed a nonzero
linear equation fixes at most one coordinate after the other is chosen,
so each line meets the rectangle in at most $n$ points. If both
$\alpha$ and $\beta$ are nonzero, the stronger bound per line is
$\min(|X|,|Y|)$. This source bound does not apply when all source
levels are admitted and only the target-level list is small.

### Meaning

A long linear level can contain many source pairs, but it intersects a
single positive norm ellipse in at most two targets. Keeping a global
sum or difference fixed therefore does not create many representations
of that norm. Moving among a subpolynomial number of target levels still
has subpolynomial certified multiplicity.

### Consequence

For $k=n^{o(1)}$, every fixed threshold $n^\varepsilon$ eventually
exceeds (6). The level-constrained certificate then has bad set equal
to the entire source rectangle. When $X\approx Y$, that rectangle
has $n^2(1-o(1))$ pairs. If $k\ge n^\varepsilon/2$, this argument
alone no longer excludes a tail; exact membership of many branches (5)
would have to be proved.

**Important scope.** On a finite rectangle one can collect all ratios
$z_q/z_p$ credited by this rule into a finite global action set $U$.
It has at most $2k|X||Y|$ nonzero-source descriptions, plus an optional
identity for zero. But a multiplier collected at one input can have
additional returns at another input whose target level is outside that
input's $\Lambda(p)$. Consequently (6) is an upper bound on the
level-constrained certificate, **not** on the unrestricted return count
of this enlarged $U$, unless that further domain restriction is proved.
No actual-image lower bound is inferred from (6).

## 3. CR-L3 — affine transfers between parallel levels

### Statement

Fix source and target levels $s,t$. Let an affine rule on the entire
source line $H=s$ take values in the line $H=t$. In the coordinates
(2), it necessarily has the form

$$H'=t,\qquad J'=\lambda J+\mu\tag{8}$$

for fixed real $\lambda,\mu$. It preserves $Q$ on at least three
distinct points of that source line if and only if

$$\lambda\in\{1,-1\},\qquad\mu=0,\qquad t\in\{s,-s\}.
\tag{9}$$

These rules are exactly restrictions of the four maps in (7), with
possible coincidences on degenerate levels. Every other affine rule
between these two fixed levels is norm preserving at **at most two**
source points, regardless of how its legal domain is subsequently cut.

**Proof.** The coordinate $J$ parametrizes the source line bijectively.
Using (1), equality of source and target norms is precisely

$$(\lambda^2-1)J^2+2\lambda\mu J+
\mu^2+3(t^2-s^2)=0.\tag{10}$$

A nonzero quadratic polynomial has at most two distinct real roots.
If (10) holds at three points, all its coefficients vanish. The first
coefficient gives $\lambda=\pm1$, the second gives $\mu=0$, and
the constant term gives $t=\pm s$. Conversely these choices give the
identity (10) on the whole line and the four maps in (7). $\square$

Here is an explicit rule-count tradeoff for partial domains. Take any
finite library of level rules of the form (8), each assigned one fixed
source level and one fixed target level. Let $K$ count its rules that
are **not** restrictions of the four symmetries. At each source pair,
credit the distinct legal targets produced by the applicable rules,
and, if desired, all four symmetry targets that lie in the rectangle.
Call this count $r_{\rm cert}(p)$. Then

$$\boxed{\sum_{p\in X\times Y}(r_{\rm cert}(p)-4)_+\le2K,}\tag{11}$$
$$\boxed{\#\{p:r_{\rm cert}(p)\ge R\}
\le\frac{2K}{R-4}\quad(R>4).}\tag{12}$$

Indeed every nonsymmetric rule is legal at at most two source points,
and contributes at most one target at each. Symmetric rules, even if
repeated at many levels, contribute only the four targets (7).
Deduplication can only reduce the counts. Summing rule incidences proves
(11), and every pair in (12) contributes at least $R-4$ to that sum.

Thus a tail with threshold $R>4$ outside at most $e$ pairs requires

$$K\ge\tfrac12(R-4)(|X||Y|-e).\tag{13}$$

For $X\approx Y$, $e=o(n^2)$ and $R\ge n^\varepsilon$, this is
$K=\Omega(n^{2+\varepsilon})$. In particular, a library with
$K=n^{2+o(1)}$ cannot certify polynomially many returns on almost all
pairs. If there are $L$ nonsymmetric rules for each of $q$ source
levels, use $K\le Lq$ in (11)–(13); the level count is not free.

### Meaning

A rich part of one line cannot be moved affinely to a genuinely new
parallel level while keeping the norm. Nontrivial transfers can be
fitted to isolated pairs, but this pays for almost every extra return
with an explicit rule incidence.

### Consequence

This closes affine level libraries below the cost (13) as return
certificates. It does not exclude nonlinear square-root branches (5),
many changing reflection directions, or a family whose algebraic
structure proves a large library of compatible partial domains. Rule
count is not automatically action count, and (13) is a necessary cost,
not an impossibility theorem for every larger library.

## 4. CR-L4 — a same-set realization and its exact limitation

### Statement

Take the concrete scalar interval

$$X=Y=A_N=\{-N,-N+1,\ldots,N\},\qquad n=2N+1,\quad N\ge1,$$

and the global level statistic $H=x+y$. Then $D=1$, $J=x-y$,
and $S_H(x,y)=(y,x)$. All four targets (7) belong to $A_N^2$.
Their distinct-target certificate has the exact distribution

$$\begin{array}{c|ccc}
r_{\rm cert}&1&2&4\\\hline
\#\text{ ordered pairs}&1&2n-2&(n-1)^2.
\end{array}\tag{14}$$

Its minimum is 1, maximum 4, and geometric mean is $4^{1-1/n}$.
Its median is 4 for $n\ge5$ and 2 for $n=3$. Symmetric difference
is exactly zero. For every fixed $\varepsilon>0$, once
$n^\varepsilon>4$ its certificate bad count is exactly $n^2$.

For each nonzero $p=(x,y)$ the swap is implemented by

$$u_{\rm swap}(p)=\frac{y-\omega x}{x-\omega y}
=-\omega\frac{\bar z}{z}.\tag{15}$$

The finite family

$$U_N=\{1,-1\}\cup
\{u_{\rm swap}(p),-u_{\rm swap}(p):p\in A_N^2\setminus\{(0,0)\}\}
\tag{16}$$

contains actual norm-one multipliers realizing every credited target.
After deduplication it has at most $2n^2$ elements. Equations (14)
are counts for the four-map certificate; they are **not** asserted to
be the full return distribution of (16).

**Proof.** The four maps are identity, swap, simultaneous negation and
negative swap. The origin has one target. A nonzero point on $x=y$
or $x=-y$ has two; these two diagonals contain $2n-2$ nonzero points
in total. Every remaining point has four distinct targets. This gives
(14), since the remaining count is $n^2-2n+1=(n-1)^2$.
The geometric mean is

$$\bigl(2^{2n-2}4^{(n-1)^2}\bigr)^{1/n^2}=4^{1-1/n}.$$

For odd $n\ge5$, $(n-1)^2>n^2/2$, so the median is 4; the
$n=3$ distribution gives median 2. The norm identity for swap is
immediate or follows from CR-L1; $y-\omega x=-\omega\bar z$
proves (15). Negating a multiplier produces the negative target.
There are at most two descriptions for each of $n^2-1$ nonzero
sources plus the two scalar signs, proving the bound in (16).
$\square$

### Meaning

This realizes the desired global correlation on every ordered pair
with exactly equal coordinate sets. It supplies only a bounded number
of distinct targets per pair through the prescribed sum-level rules.
The pair-dependent formula itself does not amplify return multiplicity.

### Consequence

The example has **CORRELATED GO / TAIL FAIL for this certificate**:
the norm identity and $X=Y$ are proved, but its return exponent is zero.
It is an analytic illustration of the new level mechanism, not a
rerun of an old interval search or an application of an interval
image theorem. No actual-image rate or full-action bad-set theorem
for (16) is claimed here; additional cross-level returns would need
their own proof and counting mechanism.

## 5. Construction ledger, sources and final scope

| Item | Exact accounting |
|---|---|
| Fixed polynomial and statistic | $Q=x^2+xy+y^2$; nonzero $H=\alpha x+\beta y$, never $Q$ itself. An affine shift in $H$ merely relabels its levels. |
| Scalar cross terms | Expanded exactly in (1); CR-L1 is a genuine scalar identity, not an independent local norm product. |
| Inputs and projection | General lemmas use actual real pairs; the concrete set has exact $n=2N+1$, unique scalar labels and all $n^2$ ordered pairs. |
| Input thinning twice | None. Source-level restrictions, when used, cover at most $kn$ actual pairs and do not replace the square count. |
| Same-set comparison | The concrete realization has $X=Y$ and zero symmetric difference; arbitrary rectangles retain their actual side sizes in all bounds. |
| Actions and duplicates | Pair-indexed ratios are actual norm-one numbers off zero. Distinct targets at a fixed nonzero pair give distinct multipliers; repeated levels/maps do not give new targets. The concrete global inventory is at most $2n^2$. |
| Zero | Norm zero has only the origin, which has one returned point. A large collection of ratios elsewhere supplies no zero multiplicity gain. |
| Levels and rules | At most $2k$ targets on $k$ prescribed levels; nonsymmetric affine rules cost at least one rule per two source incidences. The full library cost is (13). |
| Legal membership | Formula (5) must be real and both coordinates in the rectangle. No arithmetic square-root or integrality condition is waived. |
| Denominators/heights/fields | General identities require no number field. The concrete input height is $N$ and its multipliers lie in $\mathbb Q(\omega)$ by (15); rationalizing the ratio gives a denominator dividing $Q(x,y)$. No field-degree, discriminant, regulator, class-number, splitting or modulus gain is credited. |
| Composition | Preserving or reversing one linear level gives only the four maps (7); compositions of those same four maps remain in that four-element symmetry group. Changing levels nonlinearly or changing directions leaves that scope and requires a fresh proof. |
| Exceptions and tail | For the four-map certificate, every pair is bad once the target threshold exceeds four. For a library, (12) bounds the certified rich set; incidental global-action returns are not asserted absent. |
| Signed rate | Concrete certificate has positive input growth and exact overlap, but $\varepsilon=0$ and no fixed positive bad-tail deficit. Hence it supplies no $c>0$ through DC-R1. |
| Actual image | No new lower or upper asymptotic image estimate is proved for the concrete interval or for arbitrary carriers. |

The accepted reflection-versus-multiplier distinction is also recorded
in [DC-T2](../2026-09-21-dc-o1/tensor-compatibility.md), Section 2;
this note goes beyond that rank-one scope example by deriving a full
linear-level identity, legal target branches and the affine-rule count.
The existing full-support implication is
[HR-1](../2026-09-16-high-return/return-lemma.md), and the same-set
rectangular transport is [DC-R1](../2026-09-21-dense-cartesianization/block-rectangle.md),
Section 4. The preceding [DC-O1 checkpoint](../2026-09-21-dc-o1/README.md)
supplies the controlling OPEN witness and the frozen carrier failures.
The [T03 status](../../tracks/03-eisenstein-cartesianization/STATUS.md)
and [migration conflicts](../../MIGRATION_CONFLICTS.md) preserve the
separate adaptive RC15/4 obligation and source-availability boundaries.
No missing outside input is used by CR-L1–CR-L4.

**Scoped disposition:** the global reflection identity is proved;
bounded-level and small affine-library certificates fail the polynomial
return-tail requirement in the exact senses of (6), (12) and (14).
Many legal nonlinear level branches or different reflection directions
are not ruled out. No further family is launched by this note.

**Single retained obligation:** the commissioned correlated DC-O1
witness—preserve all scalar cross terms while proving polynomially many
genuine returns for almost every pair of an almost-common rectangle.
