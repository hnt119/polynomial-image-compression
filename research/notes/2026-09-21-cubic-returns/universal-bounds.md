# A universal bound for Cartesian returns of the cubic pair motion

Date/version: 2026-09-21 v1. T01 / cubic Cartesian returns.
Fixed target polynomial: $P(x,y)=(x-y)^3+x+y$.
**PROVED in this task; independently checked internally by the lead and a second reviewer.**

This is the authorized offline proof subtask. No numerical search, external
source retrieval, PDF operation, or arithmetic construction was performed.
The frozen motion is from
[rates and fiber maps, §§4–5](../2026-09-16-three-branch-continuation/rates-and-fiber-maps.md)
and the [final freeze, §§12–14](../2026-09-21-three-branch-freeze/Three_Branch_Continuation_Freeze.md).
The older setup, T01 state and checkpoint, source hierarchy, conflicts and
scope restrictions remain in force. No historical source bytes are changed.

## 1. Main conclusion

For a pair to return, even its first new coordinate must belong to the old
set. That already imposes a restrictive quadratic equation on three elements
of the set. A geometric counting argument shows that fewer than a fixed
positive proportion of all pairs can satisfy it as the set grows.

The argument works for every nonzero step size, with the same constant. Thus
choosing a different single step, even depending on the finite set, cannot
produce positive-density one-step returns.

**CR-U1 — PROVED internally.** For every finite $A\subset\mathbb R$ of size
$N\ge1$, and every real $\tau\ne0$, let

$$E_\tau(A)=\#\{(x,y)\in A^2:T_\tau(x,y)\in A^2\}.$$

Then

$$\boxed{E_\tau(A)\le5N^{11/6}.}\tag{1.1}$$

In particular

$$\boxed{R_1(N)\le\min\{1,5N^{-1/6}\}\longrightarrow0.}\tag{1.2}$$

Sections 2–5 give a self-contained proof. The planar-graph bound used there
is derived from the elementary planar edge inequality; no unproved
Elekes–Ronyai or general curve-incidence theorem is invoked.

**Scope.** This closes positive-density returns under one nonzero $T_\tau$.
It does not bound the number of all possible collision partners of a pair,
because that permits many different values of $\tau$. It does not give a
lower bound for $|P(A,A)|$: different return paths can have the same output.

## 2. The quadratic equation forced by a return

We can make the counting problem simpler by discarding one requirement.
Every returning pair has its first new coordinate in $A$. Counting all pairs
with that property, even if their second new coordinate leaves $A$, is a
valid upper bound for the true return count.

For $u=x-y$ the first coordinate of the motion is

$$x'=x-\frac{3\tau}{2}u^2-\frac{3\tau^2}{2}u
+\frac{\tau-\tau^3}{2}.$$

Put

$$a=\tau-\frac{2}{3\tau},\qquad b=-\tau,\qquad
F(x,y)=(x-y)^2+ax+by.$$

Then $a+b=-2/(3\tau)\ne0$ and the exact identity is

$$F(x,y)=-\frac{2}{3\tau}x'+\frac{1-\tau^2}{3}.\tag{2.1}$$

Consequently, with the $N$-point real set

$$C=-\frac{2}{3\tau}A+\frac{1-\tau^2}{3},$$

we have

$$E_\tau(A)\le\#\{(x,y)\in A^2:F(x,y)\in C\}.\tag{2.2}$$

For $\tau=1$ this becomes $a=1/3$, $b=-1$, $C=-2A/3$.
The nonzero sum $a+b$ is essential below: it prevents certain hyperbolas
from collapsing to lines. Its magnitude is irrelevant to the count, which
is why the final constant is uniform in $\tau$.

**Scope.** We are bounding a larger set of pairs than the returns. This loss
may make the exponent $11/6$ nonoptimal, but it cannot invalidate the upper
bound. No membership condition is silently assumed.

## 3. An elementary point–curve counting lemma

The geometric idea is to connect consecutive marked points along each curve.
Many such connections would form a graph with many edges. A graph with many
edges must have many crossings, whereas the curves here intersect only a
bounded number of times. Balancing these facts limits the number of marked
points on all the curves.

### 3.1 Crossing inequality for a simple graph

**PROVED elementary lemma.** A finite simple graph with $v\ge1$ vertices,
$e\ge6v$ edges, and crossing number $\operatorname{cr}$ satisfies

$$\operatorname{cr}\ge\frac{e^3}{72v^2}.\tag{3.1}$$

Here crossings count transverse intersections of interiors of edges, not
their common endpoints. The crossing number is the smallest such number in
a plane drawing with simple edge arcs, no edge passing through an unrelated
vertex, and no three edge interiors meeting at a single crossing.

**Proof.** In any such drawing with $X$ crossings, remove at most one edge
per crossing to obtain a planar simple graph. The elementary planar bound
$e_{\mathrm{planar}}\le3v$ gives

$$e\le3v+X.\tag{3.2}$$

The planar bound follows from Euler's elementary identity
$v-e+f=1+c$ for a plane graph with $c$ connected components, and counting face boundaries
in each nontrivial component; components with fewer than three vertices
satisfy the weaker bound $3v$ directly.

Choose a drawing attaining the crossing number. It may be taken to have no
crossing between adjacent edges. To see this, if two edges with a common
endpoint cross, swap their portions from that endpoint to a first crossing
and reconnect there without crossing. Their union is unchanged away from
small reconnection neighborhoods. Crossings with all other edges are merely
reassigned, while this mutual crossing is removed; removing any resulting
self-intersection cannot add crossings. Such a crossing would contradict
minimality. Thus each crossing involves four distinct vertices.

Retain each vertex independently with probability $p$, keeping the induced
edges and their drawing. Apply (3.2) and take expectations. An edge survives
with probability $p^2$ and a crossing with probability $p^4$, so

$$p^2e\le3pv+p^4\operatorname{cr}.$$

Take $p=6v/e\le1$. Then $3pv=p^2e/2$, giving (3.1). ∎

### 3.2 Incidences for the curves used below

**PROVED elementary lemma.** Suppose $\mathcal P$ is a set of $p\ge1$
distinct plane points and $\mathcal C$ is a collection of $q$ distinct
smooth real curves with these properties:

1. Each curve has at most two components, each a simple arc admitting a
   linear ordering of its points.
2. Two distinct curves meet in at most two points and share no arc.
3. Any two distinct points of $\mathcal P$ belong to at most two curves.

If $I$ is the total number of point–curve incidences, then

$$I\le 2q+12p+2\,72^{1/3}p^{2/3}q^{2/3}.\tag{3.3}$$

**Proof.** On each occupied component of each curve, connect its consecutive
incident points by the intervening curve arc. A curve with $k$ incidences
contributes at least $k-2$ edges. Thus this drawing of a multigraph has at
least $I-2q$ edges.

No edge has a point of $\mathcal P$ in its interior: any such point would
have been an incidence and would split the edge. Two drawn edges on the
same curve have disjoint interiors. No loops occur. There are at most two
parallel edges for each unordered pair of vertices, by property 3. Keep
one representative of each parallel family, leaving a simple graph with
$e\ge(I-2q)/2$ edges and $p$ vertices (including any isolated ones).

The drawing can be perturbed locally to be in general position with at most
$2\binom q2\le q^2$ crossings. Indeed intersections belonging to
$\mathcal P$ are graph vertices and contribute no crossing. At every other
intersection of the original curves, separate tangencies or multiple
intersections inside a small disk. Each pair of local branches contributes
at most one crossing in that disk, charged to their original intersection.
Distinct curves have at most two intersections in all. The edges on a
single curve have disjoint interiors, so they add no extra crossings.
Deleting parallel representatives cannot increase this count.

The crossing number of the abstract simple graph is therefore at most
$q^2$. If $e\ge6p$, (3.1) gives
$e\le72^{1/3}p^{2/3}q^{2/3}$. Otherwise $e<6p$. Combining these cases
with $I\le2e+2q$ proves (3.3). For $q=0$, the conclusion is immediate. ∎

**Scope.** This lemma has just the two bounded-intersection hypotheses
needed here. It has not been asserted for arbitrary algebraic curves or
families sharing components. We next check every hypothesis explicitly.

## 4. Counting equal values of the quadratic

To count how often the quadratic lands in an $N$-point set, first count
how often it takes the same value at two pairs. The resulting equations are
hyperbolas. The condition $a+b\ne0$ is exactly what keeps the relevant
hyperbolas from acquiring a common line.

**CR-U2 — PROVED internally.** Let $A\subset\mathbb R$, $|A|=N\ge1$,
and let $a,b\in\mathbb R$ satisfy $a+b\ne0$. For
$F(x,y)=(x-y)^2+ax+by$, define

$$Q_F(A)=\#\{(x_1,x_2,y_1,y_2)\in A^4:
F(x_1,y_1)=F(x_2,y_2)\}.$$

Then

$$\boxed{Q_F(A)\le25N^{8/3}.}\tag{4.1}$$

**Proof: remove one degenerate case.** When $y_1=y_2=y$, for each $x_1$
the equation $F(x_2,y)=F(x_1,y)$ is a quadratic in $x_2$ with leading
coefficient 1. There are at most two solutions. These cases contribute at
most $2N^2$.

For every ordered pair $(y_1,y_2)\in A^2$ with $y_1\ne y_2$, use the
curve in the $(X_1,X_2)$ plane

$$\Gamma_{y_1,y_2}:\quad
\left(X_1-y_1+\frac a2\right)^2-
\left(X_2-y_2+\frac a2\right)^2
=-(a+b)(y_1-y_2).\tag{4.2}$$

Its incidences with the $N^2$ points of $\mathcal P=A\times A$ are exactly
the remaining equal-value quadruples. There are $q=N(N-1)$ curves.

**Check the curves and their intersections.** The right side of (4.2) is
nonzero. After translating and rotating coordinates the equation is $UV=c$
with $c\ne0$. It is an irreducible smooth hyperbola with two components,
each a simple arc. The equation is irreducible because a factorization into
affine linear factors of $UV-c$ would force $c=0$; equivalently, treating it
as a polynomial linear in $U$ over $\mathbb R[V]$ gives the same conclusion.

The coefficients of $X_1$ and $X_2$ recover $y_1$ and $y_2$, so different
parameter pairs give distinct curves. Subtracting two distinct curve
equations gives a nonzero affine linear equation. A line meets an
irreducible quadratic curve in at most two points: substitute a linear
parameterization of the line, obtaining a polynomial of degree at most two;
it cannot be identically zero because the line is not a component.
Therefore two distinct curves intersect in at most two points.

**Check that two points lie on at most two curves.** For a fixed point
$(x_1,x_2)$, rewrite its curve-membership condition in the parameter plane
$(Y_1,Y_2)$:

$$\left(Y_1-x_1+\frac b2\right)^2-
\left(Y_2-x_2+\frac b2\right)^2
=-(a+b)(x_1-x_2).\tag{4.3}$$

If $x_1\ne x_2$, this is another irreducible hyperbola. Two distinct
off-diagonal points give distinct such hyperbolas, since their linear
coefficients recover $x_1,x_2$. Subtracting the two equations again gives a
nonzero line, hence at most two common parameter pairs.

If $x_1=x_2=t$, (4.3) factors as

$$ (Y_1-Y_2)(Y_1+Y_2-2t+b)=0.$$

The parameter pairs of our family always have $Y_1\ne Y_2$, so the first
line is excluded. Its permitted parameter set lies on
$Y_1+Y_2=2t-b$. Two distinct diagonal points give distinct parallel lines,
so no common permitted parameter. One diagonal point and one off-diagonal
point give a line and an irreducible hyperbola, hence at most two permitted
parameters. These cases exhaust distinct pairs of points in $\mathcal P$.
Thus hypothesis 3 of §3.2 is verified, including its degeneracies.

**Apply the elementary bound.** Use (3.3) with $p=N^2$, $q\le N^2$.
Adding back the at-most-$2N^2$ degenerate cases gives

$$\begin{aligned}
Q_F(A)&\le 16N^2+2\,72^{1/3}N^{8/3}\\
&\le25N^{8/3},
\end{aligned}$$

since $N^2\le N^{8/3}$ and $2\,72^{1/3}<9$. ∎

**Scope.** This is a bound for equal values of a particular quadratic, not
an inference that collision energy upper-bounds image support. The next step
uses it to upper-bound the number of pairs landing in a specified small
target set. The transverse condition $a+b\ne0$ cannot be dropped: if it
vanishes, (4.2) becomes reducible and the proof does not apply.

## 5. Finish the return bound

If many pairs landed in only $N$ possible quadratic values, some of those
values would be repeated very often. The previous section limits exactly
how much repetition is possible.

**CR-U3 — PROVED internally.** Under the hypotheses of CR-U2, for every
real set $C$ with $|C|=N$,

$$\#\{(x,y)\in A^2:F(x,y)\in C\}\le5N^{11/6}.\tag{5.1}$$

**Proof.** Write $r(z)=\#\{(x,y)\in A^2:F(x,y)=z\}$, and let
$M=\sum_{z\in C}r(z)$. Cauchy–Schwarz gives

$$M^2\le N\sum_{z\in C}r(z)^2
\le NQ_F(A)\le25N^{11/3}.$$

Take square roots. Applying this to (2.1)–(2.2) proves CR-U1. ∎

All estimates are independent of the numerical values of $a,b$ except for
$a+b\ne0$. Therefore the constant 5 in CR-U1 is independent of $A,N,\tau$,
and the assertion also holds when a nonzero $\tau$ is chosen adaptively from
$A$, or tends to zero or infinity with $N$.

## 6. Most pairs cannot lie even in a two-vertex return path

This bound does more than rule out very long paths covering most pairs.
It says that almost every vertex has no edge at all under a single selected
step. Long exceptional paths may still exist, but their total pair mass is
small compared with $N^2$.

**CR-U4 — PROVED internally.** Fix $\tau\ne0$. In the graph on $A^2$ with
edges $v\to T_\tau(v)$ when the endpoint is in $A^2$:

1. The number of connected components is $N^2-E_\tau(A)$, hence at least
   $N^2-5N^{11/6}$.
2. The number of vertices in components with at least two vertices is at
   most $2E_\tau(A)\le10N^{11/6}$.
3. For any integer $L\ge2$, the number of vertices in components with at
   least $L$ vertices is at most
   $\dfrac{L}{L-1}E_\tau(A)\le\dfrac{5L}{L-1}N^{11/6}$.

**Proof.** The frozen inverse and difference-translation identities show
that each vertex has at most one incoming and one outgoing edge, and there
are no directed cycles: the difference changes by the nonzero amount $\tau$
at every step. Components are finite directed paths. A path with $\ell$
vertices has $\ell-1$ edges, proving the first assertion on summing. For
$\ell\ge2$, $\ell\le2(\ell-1)$. For $\ell\ge L$,
$\ell\le L(\ell-1)/(L-1)$. Summing these inequalities proves the rest. ∎

In particular the proposed coverage of all but $O(N^{2-\delta})$ pairs by
$T_1$ paths of at least $N^\varepsilon$ vertices is **FAILED** for every
fixed $\varepsilon,\delta>0$. Its covered mass would be $N^2-o(N^2)$,
whereas CR-U4 makes it $O(N^{11/6})$.

**Scope.** The number of paths is not the number of actual cubic outputs.
Different paths may share the same output, through gaps in a fixed-step
orbit or through difference coordinates in distinct cosets modulo $\tau$.
These conclusions do not supply an actual-image lower bound and do not
disprove the fixed cubic target. They bound coverage, not maximum path
length; individual long paths are not ruled out.

## 7. A bounded collection of steps also has too few edges

Using several step sizes can connect more pairs, but a bounded collection
still has a vanishing share of possible edges. The bound remains useful even
for a slowly growing list chosen after the set is known.

**CR-U5 — PROVED internally.** Let $\mathcal S\subset\mathbb R\setminus\{0\}$
have $K$ elements, with no restrictions on its dependence on $A$. The graph
using all returns under $T_\tau$, $\tau\in\mathcal S$, has at most

$$5K N^{11/6}\tag{7.1}$$

directed edges. At most $10K N^{11/6}$ vertices are incident to an edge, and
the underlying undirected graph has at least $N^2-5K N^{11/6}$ components.

**Proof.** Sum CR-U1 over the $K$ steps. Every edge has two endpoints and
can reduce the initial component count by at most one. The bounds allow
duplicate undirected edges, which can only make the stated upper edge count
or lower component count weaker. ∎

Thus $K=o(N^{1/6})$ leaves $N^2-o(N^2)$ vertices isolated under all the
chosen steps. Covering a fixed positive fraction $\theta N^2$ of vertices
by nontrivial connections requires

$$K\ge\frac{\theta}{10}N^{1/6}.\tag{7.2}$$

This necessary condition does not prove that $K$ of this size is sufficient,
or that a larger family has a small number of components or outputs.
Unrestricted pair-dependent shifts remain outside the bound.

## 8. Claim, scope, and cost ledger

Every new claim concerns T01 / cubic Cartesian returns, dated 2026-09-21 v1.
The fixed target is the plus-sign cubic at the top. Evidence is the exact
proof in the indicated section. Independent lead and second-reviewer audits were completed in this task; there is
no claim of external review or novelty.

| ID | Status and quantifiers | Proof and dependencies | Retained limit |
|---|---|---|---|
| CR-U1 | PROVED internally: all finite real $A$, every real $\tau\ne0$, uniform $5N^{11/6}$ | §§2–5, CR-U2 and CR-U3 | Does not count all possible shifts jointly |
| CR-U2 | PROVED internally: all $a+b\ne0$, quadratic equal-value count $25N^{8/3}$ | §§3–4; proved graph lemmas and elementary Euler bound | Degenerate $a+b=0$ excluded |
| CR-U3 | PROVED internally: any $N$-element target set $C$ | §5; Cauchy–Schwarz and CR-U2 | Only a triple-membership upper bound |
| CR-U4 | PROVED internally: path coverage and component bounds for any nonzero step | §6; frozen group law plus CR-U1 | Paths with equal outputs remain distinct graph components |
| CR-U5 | PROVED internally: every finite adaptive step list | §7; sum of CR-U1 | Large or unrestricted lists remain outside useful range |
| CR-UF1 | FAILED: positive-density one-step return assertion, including adaptive nonzero steps | (1.1)–(1.2) | Original real small-image target remains OPEN |
| CR-UF2 | FAILED: almost-all-pair coverage by polynomial-length single-step paths | §6 | Sparse exceptional long paths remain possible |

No carrier is proposed here. The real scalar input is the original $A$, used
in both coordinates; input thinning is absent. Normalization (2.1) changes
only the auxiliary target set by an injective affine map, with exactly $N$
elements and no uncharged fibers. Discarding the second coordinate is an
explicit relaxation for an upper bound. Every pair and every step in the
stated list is charged. Field degree, discriminant, regulator, primes,
denominators, coefficient heights and arithmetic packing are inapplicable to
these coefficient-uniform finite real incidence counts; no number-field rate
is asserted. No infinite asymptotic construction or favorable gain-versus-cost
ledger has been produced.

The historical fixed-prime digital and bounded-displacement obstructions are
not needed for this proof. Their scopes remain unchanged. The frozen open
$R_1$ question is answered here by a new quantitative argument; its original
statement must be preserved as historical state. Any publication-level
novelty or optimal-exponent assessment would require a separately authorized
primary-source literature check, which was not undertaken offline.
