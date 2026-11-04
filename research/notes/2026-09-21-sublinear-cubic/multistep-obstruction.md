# Step size, Cartesian coverage, and the fourth coordinate

T01 / sublinear-step cubic cycle, 2026-09-21 v1.
Fixed polynomial $P(x,y)=(x-y)^3+x+y$.
**New internal proofs; independent internal lead audit completed.**
The audit record is in [verification.md](verification.md).

This authorized subtask is offline and uses no numerical search. Its frozen
inputs are the exact pair motion and the uniform estimate
$E_\tau(A)\le5|A|^{11/6}$ from the
[Cartesian-return cycle](../2026-09-21-cubic-returns/universal-bounds.md),
and the parabola representation from
[GS-U1](../2026-09-21-growing-step-cubic/multistep-bounds.md).
Those theorems are used, not reproved. Previous reports remain unchanged.

## 1. What the fourth coordinate requires

### Meaning

The earlier joint parabola bound kept the new pair and the old first
coordinate in the carrier, but discarded membership of the old second
coordinate. That missing condition has a particularly simple exact form:
each parabola only accepts a translate of the carrier in its horizontal
coordinate. This identifies precisely what a sharper incidence argument
must use.

### Statement — SC-U1, PROVED

Let $A\subset\mathbb R$ and $S\subset\mathbb R\setminus\{0\}$ be finite.
Put

$$\mathcal P_A=\{(d,v)=(v-w,v):v,w\in A\}.$$

For each old first coordinate $x\in A$ and step $\tau\in S$, define

$$\mathcal C_{x,\tau}:\quad
v=-\frac{3\tau}{2}d^2+\frac{3\tau^2}{2}d
+x+\frac{\tau-\tau^3}{2}.$$

Then the directed return count is exactly the number of incidences

$$\boxed{(d,v)\in\mathcal P_A\cap\mathcal C_{x,\tau}
\quad\text{with}\quad d\in x+\tau-A.}\tag{1.1}$$

The last condition is the fourth scalar-coordinate requirement, with no
missing projection multiplicity.

### Proof

At an incidence, the transformed difference is $d$ and the old difference
is $u=d-\tau$. The old second coordinate is therefore

$$y=x-u=x+\tau-d.$$

The displayed parabola is exactly the first-coordinate equation of
$(v,w)=T_\tau(x,y)$, and $w=v-d$. Thus $(d,v)\in\mathcal P_A$ enforces
$v,w\in A$; its curve index enforces $x\in A$; and the additional horizontal
restriction enforces $y\in A$. Conversely a return gives this incidence.
All four coordinates and the step are recovered uniquely. ∎

### Why it matters

The curve family, point set, and allowed horizontal coordinates all come
from the same scalar set. A useful improvement must exploit this correlation.
Counting only unrestricted point–parabola incidences recovers the old bound
and does not use (1.1).

### Scope

This is an exact counting reduction, not a new power bound. In particular
one cannot simply delete the disallowed incidences from the old drawing
argument and assert an improved crossing bound. An arc joining two retained
points can pass through an unretained incidence vertex used by other curves;
the drawing then needs new justification. No such improvement is assumed.

## 2. A bound for coverage by steps above a chosen size

### Meaning

Moving along a fiber always moves the second scalar coordinate in one
direction. Its displacement grows quadratically with the size of the input
difference. Since the two scalar coordinates must stay within the carrier's
diameter, a step that is not very small can only act near the diagonal.

This counts vertices that can be reached, regardless of how many edges
repeat within the same components. It also avoids using a global minimum gap
in $A-A$, which may be extremely small in nonuniform sets.

### Statement — SC-U2, PROVED

Let $A\subset\mathbb R$, $N=|A|\ge2$, and $D=\operatorname{diam}(A)$,
and let $S\subset\mathbb R\setminus\{0\}$ be a finite inventory.
Normalize an undirected step inventory to its distinct positive absolute
values $S^+=\{|\tau|:\tau\in S\}$; this leaves the graph unchanged.
For $t>0$ define

$$m(t)=|S^+\cap(0,t)|,\qquad
Q_A(r)=\#\{(x,y)\in A^2:|x-y|\le r\},$$

$$R(t)=D^{1/3}+\sqrt{\frac{2D}{3t}}.$$

If $V(A,S)$ is the number of nonisolated vertices in the entire graph, then

$$\boxed{V(A,S)\le
\min\left\{N^2,\ 10m(t)N^{11/6}+Q_A(R(t))\right\}}
\quad\text{for every }t>0.\tag{2.1}$$

The same bound applies to the total mass of components of size at least
any prescribed $K\ge2$. It is independent of the number of steps at least
$t$, even if that number is arbitrarily large.

### Proof

Consider any edge and orient it in the positive-difference direction. Its
endpoint differences are $u$ and $u+\tau$, with $\tau>0$, and its output is
$z$. Put $m=u+\tau/2$. The exact second-coordinate drop is

$$y_z(u)-y_z(u+\tau)
=\frac\tau2\left(1+3m^2+\frac{\tau^2}{4}\right).\tag{2.2}$$

Both second coordinates belong to $A$, so (2.2) is positive and at most
$D$. Consequently $\tau/2\le D^{1/3}$ and
$|m|\le\sqrt{2D/(3\tau)}$. Both endpoint differences obey

$$|u|,|u+\tau|\le D^{1/3}+\sqrt{2D/(3\tau)}.$$

In particular every endpoint of an edge with $\tau\ge t$ is one of the
$Q_A(R(t))$ vertices in that band. The steps below $t$ contribute at most
$5m(t)N^{11/6}$ edges by the frozen uniform theorem, and hence at most
$10m(t)N^{11/6}$ incident vertices. Their union with the band contains all
nonisolated vertices. Overlap is allowed in this upper count. This proves
(2.1). Every component of at least two vertices is contained in the
nonisolated set. ∎

### Why it matters

For any $t$ with $Q_A(R(t))\le\beta N^2$, a carrier with
$V(A,S)\ge\theta N^2$, $\theta>\beta$, necessarily satisfies

$$\boxed{m(t)\ge\frac{\theta-\beta}{10}N^{1/6}.}\tag{2.3}$$

Thus it is not enough to pay for $N^{1/6}$ steps anywhere on the real line.
If many pairs lie far from the diagonal, a comparable number of steps must
occur below the specific small scale forced by the carrier.

One may take the infimum in (2.1) over all $t>0$. More generally, for a
partition of $S^+$ into bins $S_j\subset[t_j,\infty)$, their contributions
to nonisolated mass are bounded by

$$V(A,S)\le\sum_j
\min\{10|S_j|N^{11/6},\ Q_A(R(t_j))\}.\tag{2.4}$$

This follows by applying both endpoint bounds to each bin and taking the
union. No disjointness of the reached vertex sets is presumed.

### Scope

This is a coverage bound, not an actual-image lower bound. Pairs isolated
for a chosen step inventory can still have partners at other steps. It does
not increase the universal $N^{1/6}$ inventory threshold: the very small
steps demanded at several scales can be the same nested subinventory.
Neither (2.1) nor (2.4) proves that these separate costs must add.

## 3. A consequence for nonlattice carriers with controlled scalar spacing

### Meaning

The carrier need not lie on any lattice. If its scalar points are separated
and its width grows linearly with their number, steps larger than roughly
$1/N$ can only touch a small band of pairs. Tiny gaps between differences
do not invalidate this conclusion, because it concerns the sizes of the
steps actually selected.

### Statement — SC-U3, PROVED

Fix $c,C>0$ and $0\le\beta<1$. Suppose a growing family $A_N$ satisfies

$$|a-b|\ge c\quad(a,b\in A_N,\ a\ne b),\qquad
\operatorname{diam}(A_N)\le CN.$$

For every step inventory, of any cardinality, whose nonzero step sizes
satisfy $|\tau|\ge N^{-\beta}$,

$$\boxed{V(A_N,S_N)=O_{c,C}(N^{(3+\beta)/2}).}\tag{3.1}$$

More generally, if all steps are at least $t_N>0$ with $Nt_N\to\infty$,
then $V(A_N,S_N)=o(N^2)$.

If instead positive-density coverage $V(A_N,S_N)\ge\theta N^2$ is
required for fixed $\theta>0$, there is a constant
$K=K(c,C,\theta)<\infty$ such that necessarily

$$|S_N^+\cap(0,K/N)|\ge\frac\theta{20}N^{1/6}\tag{3.2}$$

for every sufficiently large $N$.

### Proof

Scalar spacing gives

$$Q_{A_N}(r)\le N\min\{N,1+2\lfloor r/c\rfloor\}.$$

With all steps at least $t$, (2.1) has $m(t)=0$, giving

$$V(A_N,S_N)\le
N\left(1+\frac2c\left((CN)^{1/3}
+\sqrt{\frac{2CN}{3t}}\right)\right).\tag{3.3}$$

Taking $t=N^{-\beta}$ proves (3.1); dividing (3.3) by $N^2$ proves the
assertion when $Nt_N\to\infty$.

For (3.2), use $t=K/N$. Formula (3.3), now used only to bound the
large-step band, yields

$$\frac{Q_{A_N}(R(K/N))}{N^2}
\le\frac1N+\frac{2C^{1/3}}cN^{-2/3}
+\frac2c\sqrt{\frac{2C}{3K}}.$$

Choose $K$ sufficiently large that the last term is less than $\theta/4$.
The first two terms are less than $\theta/4$ for large $N$. Apply (2.3)
with $\beta$ there equal to $\theta/2$ to obtain (3.2). ∎

### Why it matters

For example, $A_N=\{j+e_j:0\le j<N\}$ with arbitrary
$0\le e_j\le1/4$ has scalar spacing at least $3/4$ and diameter at most
$N$. It need not be contained in an affine rational lattice, and its
difference-set minimum gap can be arbitrarily tiny. The theorem still
prevents every inventory with steps bounded below by $N^{-\beta}$,
$\beta<1$, from covering a positive proportion of its square.

This is outside the affine-lattice hypothesis of GS-U3. It is also distinct
from the old global difference-gap test: no lower bound on the spacing of
$A_N-A_N$ is imposed.

### Scope

These are restrictions on an actual selected inventory. They do not reject
inventories containing sufficiently many smaller steps, and they do not
prove an actual-image lower bound for arbitrary perturbed carriers. Nor do
they cover scalar sets with arbitrarily dense clusters without replacing
the spacing estimate by their actual $Q_A$ profile in (2.1).

## 4. Why the special parabolas alone do not reduce the crossing budget

### Meaning

The parabolas have related coefficients, but they can still intersect each
other as often as a general two-parameter family. Thus an argument that
only tries to replace the old quadratic curve-crossing count by a smaller
power cannot succeed uniformly. The missing fourth-coordinate restriction,
rather than an absence of geometric intersections, must do additional work.

### Statement — SC-U4, PROVED geometric intersection count

Let $A$ contain $N$ distinct real numbers, and let $S\subset(0,1)$ contain
$M$ distinct steps. Among the $NM$ curves $\mathcal C_{x,\tau}$ from §1,
the number of pairwise intersection incidences, counting an intersection
once for each pair of curves through it, is at least

$$\boxed{\frac{N(N+1)M(M-1)}2.}\tag{4.1}$$

Hence the quadratic order $\Theta(N^2M^2)$ of the generic crossing budget
is possible in this exact parabola family.

### Proof

Take $\tau>\sigma$ in $S$ and $x\ge x'$ in $A$. Put
$\Delta=\tau-\sigma\in(0,1)$. Subtract the two curve equations and
complete the square. Their intersections solve

$$\left(d-\frac{\tau+\sigma}{2}\right)^2
=\frac13-\frac{\Delta^2}{12}
+\frac{2(x-x')}{3\Delta}.\tag{4.2}$$

The right side is strictly larger than $1/4$, so there are exactly two
distinct real intersections. There are $\binom M2$ step pairs and
$N(N+1)/2$ choices $x\ge x'$. Thus the indicated subcollection of curve
pairs contributes $2\binom M2 N(N+1)/2$, which is (4.1). ∎

### Why it matters

Three distinct points with different horizontal coordinates determine at
most one curve, because they determine the coefficients of a parabola.
That additional observation does not invalidate (4.1), nor does it itself
improve the two-point crossing argument. No stronger exponent follows by
simply recording this three-point uniqueness.

### Scope

The intersections counted in (4.1) need not belong to $\mathcal P_A$ or
satisfy the fourth-coordinate mark in (1.1). This is a failure of a proposed
geometric shortcut, not a lower bound on actual returns and not a counterexample
to a sharper marked-incidence theorem.

## 5. Honest stopping point for the universal exponent

The fourth-coordinate condition has been retained exactly in (1.1), while
actual endpoint membership yields the step-size coverage restriction (2.1).
No new estimate of the
form $O(N^\alpha M^\beta)$ with $\alpha+\theta\beta<2$ for a universal
$\theta>1/6$ has been established in this subtask.

The following shortcuts were examined and do not supply that conclusion:

- Dropping the horizontal mark in (1.1) is exactly the previous GS-U1
  incidence problem; it does not use the extra coordinate.
- Reducing the total number of pairwise parabola intersections is impossible
  uniformly by (4.1).
- Three-point uniqueness does not replace the known two-point incidence
  bound with a proved better exponent.
- Summing the required small-step counts at nested scales would double-count
  the same steps. Formula (2.3) gives a scale-dependent necessary condition,
  not an additive cost over scales.
- A large collection of unmarked geometric intersections supplies no actual
  edges, component coverage, or image bound.

The universal marked-incidence/coverage problem beyond the frozen threshold
therefore remains **OPEN**. No positive or negative conjecture is adopted.
The lead report chooses the cycle's one next proof obligation; this note
does not create a competing task.

## 6. Claim and scope ledger

All claims are T01 / sublinear-step cubic, fixed plus-sign polynomial, dated
2026-09-21 v1. Evidence is the exact algebraic and counting proof in the named
section. Independent internal lead audit of SC-U1–U4 is complete and recorded
in [verification.md](verification.md); no external review or novelty
assessment is claimed.

| ID | Status and exact scope | Proof and dependencies | Retained limit |
|---|---|---|---|
| SC-U1 | PROVED: exact marked-parabola count for all finite real carriers and inventories | §1; frozen pair formula | Reformulation without a new power bound |
| SC-U2 | PROVED: coverage-spectrum bound for every carrier, inventory and cutoff $t>0$ | §2; exact second-coordinate drop and frozen CR-U1 | Does not force different scales to pay for disjoint steps |
| SC-U3 | PROVED: uniformly separated width-$O(N)$ real carriers and the stated step-size conditions | §3; SC-U2 and scalar packing | Smaller steps and dense nonuniform clusters remain possible |
| SC-U4 | PROVED: quadratic-order curve intersections for every $A$ and $S\subset(0,1)$ | §4; exact intersection equation | These are not necessarily legal Cartesian returns |
| SC-UGAP | OPEN, retained gap only: universal coverage threshold strictly above $1/6$ | §5 | No additional adopted next obligation |

There is no input thinning or surrogate parameter cardinality in these
counts. Both inputs and both transformed coordinates are tracked in §1;
the endpoint band in §2 uses actual membership of both transformed second
coordinates. Scalars are real throughout, and no number-field, prime,
discriminant, regulator or arithmetic-amplification input is used. Full-square
exceptions are retained as vertices; no energy-to-support inference occurs.
