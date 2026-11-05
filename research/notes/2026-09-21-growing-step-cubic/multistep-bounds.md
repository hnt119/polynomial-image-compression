# Many-step bounds and a lattice-carrier obstruction

Date/version: 2026-09-21, growing-step cycle v1. Track T01, fixed polynomial
$P(x,y)=(x-y)^3+x+y$. **New internal proofs; independently audited by
the lead and a second reviewer within this cycle.**

This authorized subtask is strictly offline, with no numerical search. The
single-step theorem is a frozen dependency, not reproved here. Its exact
statement and elementary graph-counting lemma are in
[the preceding universal-bounds note](../2026-09-21-cubic-returns/universal-bounds.md),
CR-U1 and §3.2. The exact fiber coordinates and group law are from
[the preceding fiber companion](../2026-09-21-cubic-returns/fibers-and-chains.md),
CR-P1–P3. No historical file is modified.

## 1. A new bound counting different steps together

### Meaning

Fix the old first coordinate and the chosen step. As the old second
coordinate varies, the transformed pair traces a parabola. Thus all returns
for many steps can be counted together by looking at a family of parabolas
passing through the new Cartesian square. This uses the interaction between
steps instead of applying the one-step bound separately.

The resulting bound grows like $|S|^{2/3}$ over the relevant range. Its power
of $N$ is larger than in the frozen one-step estimate, however. It improves
the edge bound for sufficiently large inventories; it does not improve the
$N^{1/6}$ threshold for quadratic pair coverage.

### Precise statement

**GS-U1 — PROVED internally.** For every finite real set $A$ with $|A|=N\ge1$
and every finite $S\subset\mathbb R\setminus\{0\}$ with $|S|=M\ge1$, put

$$E_S(A)=\sum_{\tau\in S}E_\tau(A).$$

This counts directed return edges with their step; the number of distinct
undirected edges is at most $E_S(A)$. Then

$$\boxed{E_S(A)\le9N^2M^{2/3}+NM+12N^2.}\tag{1.1}$$

Combining with the frozen theorem and the elementary fiber-size bound gives

$$E_S(A)\le\min\left\{
5MN^{11/6},\ 9N^2M^{2/3}+NM+12N^2,\ N^2(N-1)
\right\}.\tag{1.2}$$

The assertion is uniform in the real values of the steps, including steps
chosen after seeing $A$. For $S=\varnothing$, the count is zero.

### Proof

Write the transformed pair as $(v,w)=T_\tau(x,y)$ and put $d=v-w$.
Its original difference is $u=x-y=d-\tau$. The first-coordinate formula
for $T_\tau$ becomes

$$v=-\frac{3\tau}{2}d^2+\frac{3\tau^2}{2}d
+x+\frac{\tau-\tau^3}{2}.\tag{1.3}$$

For each $(x,\tau)\in A\times S$, let $\mathcal C_{x,\tau}$ be the
parabola (1.3) in the $(d,v)$ plane. There are exactly $q=NM$ different
parabolas: their quadratic coefficient recovers $\tau$, and their constant
coefficient then recovers $x$.

The output pairs give the $p=N^2$ distinct points

$$\mathcal P=\{(v-w,v):v,w\in A\}.$$

Every actual return gives an incidence of one of these points with one of
these curves. This assignment is injective: from the incidence and its
parameters $(x,\tau)$, recover $u=d-\tau$ and $y=x-u$. We allow incidences
whose recovered $y$ is not in $A$, so the incidence count $I$ is an upper
bound for $E_S(A)$.

We check the geometric conditions explicitly.

- Each curve is a smooth graph over the real $d$ axis, hence one simple
  component. It has no closed component or self-intersection.
- Two different curves with the same $\tau$ never meet. With different
  steps, subtracting their equations gives a nonzero quadratic in $d$,
  so they meet at most twice and share no arc.
- Two distinct points with the same $d$ coordinate lie on no common graph.
  For points $(d_1,v_1),(d_2,v_2)$ with $d_1\ne d_2$, subtract (1.3)
  and divide by $d_1-d_2$. A possible step must solve

  $$\tau^2-(d_1+d_2)\tau-
  \frac{2(v_1-v_2)}{3(d_1-d_2)}=0.\tag{1.4}$$

  There are at most two real choices of $\tau$, and each determines $x$
  uniquely from either point. Thus two points belong to at most two curves.

Use the elementary crossing-number argument already proved in the frozen
note, §3.2. Since our curves have one component, connecting consecutive
incidences gives at least $I-q$ edges, rather than $I-2q$. Parallel edges
have multiplicity at most two. Keeping one representative per parallel
family gives a simple graph with $e\ge(I-q)/2$ edges. No edge passes
through another point of $\mathcal P$ in its interior, because such a
point would have split it. Edges on the same parabola have disjoint
interiors. Distinct parabolas meet at most twice, so the drawing has at
most $q^2$ crossings after the same local perturbation as in the frozen
proof; meetings at incidence vertices are not crossings.

The frozen elementary inequality gives either $e<6p$, or
$e\le72^{1/3}p^{2/3}q^{2/3}$. Therefore

$$I\le q+12p+2\,72^{1/3}p^{2/3}q^{2/3}
\le q+12p+9p^{2/3}q^{2/3}.$$

Insert $p=N^2,q=NM$ to obtain (1.1).

The first term of (1.2) is precisely the frozen sum bound. For the third,
every actual cubic fiber has at most $N$ vertices, since for each fixed
second coordinate the cubic is strictly increasing in the first. Each
vertex therefore has at most $N-1$ other fiber vertices; every such partner
has one uniquely determined step. Summing over the $N^2$ vertices proves
$E_S(A)\le N^2(N-1)$. ∎

### Why it matters

For $1\le M\le N$, (1.1) implies the simpler bound

$$E_S(A)\le22N^2M^{2/3}.$$

If $M=N^\theta$, its leading exponent is $2+2\theta/3$, compared with
$11/6+\theta$ in the frozen sum bound. The new exponent is smaller
exactly when $\theta>1/2$. Thus this is a genuinely different many-step
estimate, useful in the range of large inventories considered in the task.

### Scope

The exponent $2+2\theta/3$ is not below two for any positive $\theta$.
Consequently this result does not strengthen the existing $N^{1/6}$
necessary inventory size for covering a positive proportion of pairs.
It gives no positive carrier, no improved universal coverage threshold,
and no actual-image lower bound. Discarding the old second-coordinate
membership is the explicit relaxation; recovering a quantitative benefit
from that fourth scalar-coordinate requirement remains unresolved.

## 2. A geometric restriction on every nontrivial cubic collision

### Meaning

Along a cubic fiber, increasing the difference always decreases the second
coordinate. The decrease is quadratic in the midpoint of the two
differences and cubic in their separation. Both second coordinates must
stay inside the carrier's diameter. If distinct available differences
cannot be very close, collisions are therefore confined to a short band
around the diagonal $x=y$.

This argument concerns every possible collision partner, regardless of
which steps were listed. It can consequently give an actual-image lower
bound for suitable carriers, not merely a failed graph certificate.

### Precise statement

**GS-U2 — PROVED internally.** Let $A\subset\mathbb R$, $|A|=N\ge2$,
have diameter $D=\max A-\min A$. Define two positive separation parameters

$$\delta=\min_{a,b\in A,\ a\ne b}|a-b|,$$

$$\eta=\min_{u,v\in A-A,\ u\ne v}|u-v|.$$

Put

$$R=D^{1/3}+\sqrt{\frac{2D}{3\eta}},\qquad
B=N\min\left\{N,1+2\left\lfloor\frac R\delta\right\rfloor\right\}.
\tag{2.1}$$

Every vertex $(x,y)\in A^2$ belonging to a cubic fiber of size at least two
satisfies $|x-y|\le R$. Therefore at most $B$ vertices lie in nonsingleton
fibers, and

$$\boxed{|P(A,A)|\ge N^2-B.}\tag{2.2}$$

For every step inventory, of any size, at most $B$ vertices can be
nonisolated or belong to components larger than one.

### Proof

Two distinct pairs in one fiber have distinct differences: the output and
the difference recover the ordered pair. Write these differences as
$u$ and $u+\tau$ with $\tau>0$. Both belong to $A-A$, so $\tau\ge\eta$.
Let $m=u+\tau/2$. Along the fiber with output $z$,

$$y_z(u)-y_z(u+\tau)
=\frac{\tau}{2}\left(1+3m^2+\frac{\tau^2}{4}\right).\tag{2.3}$$

Both second coordinates belong to $A$, so the positive quantity (2.3)
is at most $D$. It follows that

$$\tau^3/8\le D,\qquad |m|\le\sqrt{\frac{2D}{3\tau}}
\le\sqrt{\frac{2D}{3\eta}}.$$

Since $\tau/2\le D^{1/3}$, both differences satisfy

$$|u|,|u+\tau|\le|m|+\tau/2\le R.$$

This holds for every pair of distinct vertices in a fiber, so every vertex
in a nonsingleton fiber lies in the stated band.

For a fixed $y\in A$, at most $\lfloor R/\delta\rfloor$ other elements
of $A$ lie between $y$ and $y+R$, and at most that many between $y-R$ and
$y$. Including $x=y$ gives the bound in (2.1), capped by $N$ possibilities.
Sum over $y$ to obtain $B$.

Every vertex outside nonsingleton fibers has a distinct output appearing
nowhere else in $A^2$. These singleton outputs number at least $N^2-B$,
proving (2.2). A graph component larger than one necessarily lies in a
nonsingleton actual fiber, so the same bound applies to every inventory. ∎

### Why it matters

This exposes a geometric requirement of a prospective carrier: if it has
many output collisions and is not extremely wide, its difference set must
have very small gaps relative to its scalar spacing. The relevant small
gap is in $A-A$, not just in $A$ itself.

For example, if at least $\theta N^2$ vertices belong to nonsingleton fibers,
then necessarily

$$R\ge\frac{\delta(\theta N-1)}2.$$

When the right side exceeds $D^{1/3}$, rearranging gives the precise
necessary condition

$$\eta\le
\frac{2D}{3\left(\delta(\theta N-1)/2-D^{1/3}\right)^2}.\tag{2.4}$$

### Scope

All finite sets have a positive $\eta$, but it can be arbitrarily small.
Thus (2.2) can be vacuous for unrestricted real sets. In particular a lower
bound on scalar spacing $\delta$ does not justify replacing $\eta$ by
$\delta$: differences of well-separated points can be extremely close.
No universal multi-step impossibility follows from this parameterized bound.

## 3. Arbitrary lattice subsets of moderate diameter fail for every inventory

### Meaning

On one arithmetic lattice, distinct differences are separated by at least
the lattice spacing. The preceding bound then becomes explicit. If the
carrier is not too spread out, almost every input pair has a unique cubic
output. Adding more steps cannot help because most pairs have no collision
partner at all.

This covers arbitrary sparse subsets of the lattice, rather than only
complete arithmetic progressions. Both the lattice and its spacing may
change along the family.

### Precise statement

**GS-U3 — PROVED internally.** Suppose $A\subset a+h\mathbb Z$ is finite,
with $h>0$, $|A|=N\ge2$, and diameter $D$. Put

$$W=\frac{D}{h^3},\qquad
K=\min\left\{N,1+2\left\lfloor
W^{1/3}+\sqrt{2W/3}\right\rfloor\right\}.$$

Then at most $NK$ vertices lie in nonsingleton cubic fibers, and for every
step inventory at most $NK$ vertices can be in nontrivial components.
In particular

$$\boxed{|P(A,A)|\ge N^2-NK.}\tag{3.1}$$

For every growing sequence of such carriers, with potentially varying
$a,h,D$, if

$$\frac{D}{h^3N^2}\longrightarrow0,\tag{3.2}$$

then

$$|P(A,A)|=N^2-o(N^2),$$

and every step inventory, even the complete collection of possible
collision steps, leaves $N^2-o(N^2)$ singleton components.

### Proof

Both $A-A$ and every difference of two of its elements lie in $h\mathbb Z$.
Thus $\delta\ge h$ and $\eta\ge h$. Use (2.1) with these lower bounds.
The permitted difference band divided by $h$ is at most

$$\frac{D^{1/3}}h+\sqrt{\frac{2D}{3h^3}}
=W^{1/3}+\sqrt{2W/3}.$$

Alternatively count the available lattice points directly, yielding $K$.
This proves the finite statement.

If $W=o(N^2)$, then $\sqrt W=o(N)$ and $W^{1/3}=o(N)$, so $K=o(N)$.
Equation (3.1) and the trivial upper bound $|P(A,A)|\le N^2$ prove the
asymptotic conclusion. ∎

### Why it matters

For integer sets, $h=1$. Any family of $N$ integers whose diameter is
$o(N^2)$ has an asymptotically quadratic actual cubic image. More explicitly,
if $D\le C N^{2-\gamma}$ for fixed $C<\infty$ and $0<\gamma\le1$, then
the nonsingleton-fiber mass is

$$O_C(N^{2-\gamma/2}),$$

so the image is at least $N^2-O_C(N^{2-\gamma/2})$.
Bounded-diameter multiples of $N$, including bounded unions of integer
progressions inside such an interval, have at most $O(N^{3/2})$ pairs in
nonsingleton fibers, regardless of the number of listed steps.

For the full progression of spacing $h$ and length $N$, condition (3.2)
reduces to $h\sqrt N\to\infty$ up to the immaterial $N-1$ factor, matching
the earlier progression regime. Here the carrier need not be a progression.

### Scope

The lattice restriction is essential to this proof. Its mesh $h$ must be a
valid common spacing, not the smallest gap between adjacent scalar points
of an arbitrary nonlattice set. Rational carriers with rapidly shrinking
mesh, sets of diameter comparable to or larger than $h^3N^2$, and genuinely
nonlattice real carriers are not excluded. This is a broad carrier-specific
obstruction, not a universal impossibility theorem for the cubic.

## 4. Exact remaining gap and accounting

The new universal count (1.1) gives a sublinear dependence on inventory size
but does not increase the frozen $N^{1/6}$ coverage threshold. The lattice
argument does close every inventory in the moderate-diameter regime (3.2),
because it bounds the mass of actual nonsingleton fibers.

A precise stronger universal statement remains **OPEN**: find fixed
$\theta_0>1/6$ and $\xi>0$ and a coefficient-independent bound forcing
the nonisolated mass to be $O(N^{2-\xi})$ for all finite real $A$ and all
$|S|\le N^{\theta_0}$, or exhibit a carrier refuting such a bound. The
present argument does neither. This is a recorded proof gap, not a positive
conjecture or a separate research assignment.

| Quantity or cost | What is proved | What remains unproved |
|---|---|---|
| Distinct scalar inputs | Exactly $N$, in both coordinates | No growing carrier is proposed |
| Directed return edges | Minimum of the three bounds in (1.2) | No universal quadratic-coverage threshold beyond $1/6$ |
| Inventory | Actual $M=|S|$ distinct nonzero real parameters | A formal list with no returns earns no saving |
| Projection fibers | Return-to-incidence map injective | Extra incidences arise when the old second coordinate is discarded |
| Full pair coverage | All $N^2$ pairs charged; nonsingleton mass bounded in §§2–3 | Outside those regimes uncovered pairs cannot be discarded |
| Actual image | Lower bound (3.1) in the stated lattice scope | Universal or positive image upper bound absent |
| Arithmetic parameters | Mesh $h$ and diameter $D$ explicitly charged through $D/h^3$ | Shrinking mesh or large width can defeat this obstruction |
| Thinning | None in these proofs | Any future thinning must alter the actual input count in both coordinates |
| Number fields, splitting, regulator, discriminant | Inapplicable: no such construction or theorem used | No arithmetic amplification is inferred |
| Exponent gain | No positive construction rate | Sublinear inventory coverage remains OPEN outside proved scopes |

## 5. Claim ledger

All claims below have track T01, branch “growing-step cubic”, the fixed
plus-sign cubic, and date/version 2026-09-21 v1. Proof evidence is symbolic
and exact. Independent lead and second-reviewer audits found no gap in the
displayed arguments; these are internal audits, not external certification.
No external novelty claim is made.

| ID | Status and quantifiers | Proof locator and dependencies | Scope limit |
|---|---|---|---|
| GS-U1 | PROVED internally: all finite real carriers and finite nonzero step inventories | §1; frozen elementary crossing lemma, explicit new parabola family | Improved inventory dependence does not improve coverage threshold |
| GS-U2 | PROVED internally: every finite real carrier with its actual $D,\delta,\eta$ | §2; exact fiber coordinate and scalar separation count | May be vacuous when the difference gap is tiny |
| GS-U3 | PROVED internally: every affine-lattice carrier and every inventory, including all collision steps | §3; GS-U2, or its direct lattice count | Moderate-diameter condition required for asymptotic obstruction |
| GS-GAP1 | OPEN, retained gap only: universal coverage estimate improving the exponent $1/6$ | §4 records the exact missing estimate | No conjectured answer or additional adopted obligation |

The original four research targets remain distinct. No norm, trace,
Chebotarev, digital-language or algebraic-factorization pivot occurs here.
The lead report selects the cycle's one next proof obligation after auditing
these results and the other bounded subtasks.
