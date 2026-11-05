# The affine overlap mechanism behind the 22-output gadget

Date/version: 2026-09-16, continuation v1. Track T01; fixed polynomial
$P(x,y)=(x-y)^3+x+y$. **New internal proofs; independently audited by the lead.**
This authorized subtask is strictly offline and performs no experiments.
It preserves the preceding cycle's files. Its immediate source is the
[preceding report](../2026-09-16-three-branch-lift/README.md), §§4–6,
especially the complete block table and slice count.

The conclusions are restricted to the finite gadget's translated-slice
mechanism and to explicitly defined ways of carrying its collisions into
larger sets. They do not disprove the real-set target or all adaptive affine
constructions. Every substantial conclusion below has its scope after its proof.

## 1. All eight interblock overlaps come from two identities

The six points form a short progression. Two different differences can give
the same output because their cubic terms are offset by a shift in their
anchors. The progression is short enough that these few differences account
for a large fraction of its pairs. All eight overlaps between different
blocks have this explanation; none requires an unexplained numerical accident.

Write

$$G=\{0,1/3,2/3,1,4/3,5/3\},\qquad B_r=\{r/3,1+r/3\}.$$

The two identities, valid for every real $t$, are

$$\begin{aligned}
I_+(t):&\quad P(t+1/3,t)=P(t,t+2/3)=2t+10/27,\\
I_-(t):&\quad P(t-1/3,t)=P(t,t-2/3)=2t-10/27.
\end{aligned}\tag{1.1}$$

**TC-A1 — exact classification.** The table below lists every interblock
equality. Ordered pairs are written as integer indices $(i,j)$ for
$(i/3,j/3)$. The block of $(i,j)$ is $(i\bmod3,j\bmod3)$.

| Scaled output $27z$ | First pair / block | Second pair / block | Identity / anchor |
|---|---|---|---|
| 10 | $(1,0)$ / 10 | $(0,2)$ / 02 | $I_+(0)$ |
| 28 | $(2,1)$ / 21 | $(1,3)$ / 10 | $I_+(1/3)$ |
| 46 | $(3,2)$ / 02 | $(2,4)$ / 21 | $I_+(2/3)$ |
| 64 | $(4,3)$ / 10 | $(3,5)$ / 02 | $I_+(1)$ |
| 26 | $(1,2)$ / 12 | $(2,0)$ / 20 | $I_-(2/3)$ |
| 44 | $(2,3)$ / 20 | $(3,1)$ / 01 | $I_-(1)$ |
| 62 | $(3,4)$ / 01 | $(4,2)$ / 12 | $I_-(4/3)$ |
| 80 | $(4,5)$ / 12 | $(5,3)$ / 20 | $I_-(5/3)$ |

**Proof and classification.** Substitute the displayed pairs into (1.1).
The preceding report's complete nine-block table has exactly these eight
repeated values between different blocks and no triple block intersection.
Alternatively its slices $S_{-2}\subset S_1$ and $S_2\subset S_{-1}$ each
have four elements, giving precisely these eight equalities.
Thus each row is an **exact one-variable polynomial identity** applied at a
legal anchor. Together the rows give **whole-slice containments** on $G$.
They are not identities in two independently varying input variables.
There is no whole-block containment between different blocks: the previous
complete table shows diagonal block supports are disjoint from the others,
and every intersection between two off-diagonal four-element blocks has
size at most two.

The other six lost outputs occur inside the three diagonal blocks. They are
exactly

$$P(t,t-1)=P(t,t),\quad t\in\{1,4/3,5/3\},$$
$$P(t,t+1)=P(t,t),\quad t\in\{0,1/3,2/3\}.\tag{1.2}$$

These again are polynomial identities for all real $t$ when their endpoints
are present. The complete output has 14 values of multiplicity two and eight
of multiplicity one, hence $14\cdot2+8=36$ ordered pairs and 22 outputs.
No extra collision is needed or omitted. ∎

The entire equality pattern can be described by just two moves of an ordered
input pair. Writing $u=x-y$, they are

$$\begin{array}{c|c|c}
\text{move}&\text{differences where output is preserved}&\text{edges on }G^2\\
(x,y)\mapsto(x,y+1)&u=0\text{ or }1&6\\
(x,y)\mapsto(x-1/3,y+2/3)&u=1/3\text{ or }2/3&8.
\end{array}\tag{1.3}$$

For the second move, the $u=1/3$ instances are $I_+$, while the $u=2/3$
instances are $I_-$ read in the reverse direction. Subtraction, as in (4.4)
below, proves the displayed allowed differences exactly. Endpoint membership
in $G$ gives the indicated six and eight edges. Thus a very short list of
exact rules explains the whole finite gain.

The scale $1/2$ turns the seed gap 2 into the branch gap 1 used in (1.2).
The translations $r/3$ interleave the three branch pairs into $G$, supplying
the endpoints of (1.1). Residues modulo three label the three branches; no
reduction modulo three proves these real equalities.

**Limits.** Translation of a single identity in $t$ gives many collisions
only if all its endpoints remain in the carrier. It does not by itself count
the pairs at other differences. The finite complete count remains a success,
but its fourteen savings do not automatically multiply under composition.

## 2. Scaling destroys the old equalities unless its magnitude is one

The cubic term scales by the cube of the scale, while the linear term scales
only by the scale. Their cancellation therefore occurs at a specific size.
Moving the gadget preserves every equality; shrinking or enlarging it usually
does not.

**TC-A2 — exact common-scaling rule.** Suppose
$P(a,b)=P(c,d)$ and $(a,b)\ne(c,d)$. Put $u=a-b$, $v=c-d$.
For every nonzero real $h$ and real $t$,

$$P(ha+t,hb+t)-P(hc+t,hd+t)
=h(h^2-1)(u^3-v^3).\tag{2.1}$$

Moreover $u\ne v$. Consequently this old equality survives the common affine
change $x\mapsto hx+t$ exactly when $h=1$ or $h=-1$.

**Proof.** The original equality says
$(a+b)-(c+d)=-(u^3-v^3)$. Expand both new outputs to obtain (2.1).
If $u=v$, the original equality also gives $a+b=c+d$, which recovers the same
ordered pair. Thus $u^3-v^3\ne0$ over the reals. ∎

There is a useful parameter version for the displayed six-point pattern.
Suppose a two-point seed has gap $H\ne0$, all branches have a common scale
$\lambda$, and their translations are $t_0,t_0+q,t_0+2q$. Interleaving the
branches into the same progression pattern requires $\lambda H=3q$.
The intended interblock identity becomes

$$P(t+q,t)=P(t,t+2q)\iff q(9q^2-1)=0.$$

For distinct branches this forces $q=\pm1/3$, hence $\lambda H=\pm1$.
So changing the two-point seed gap and compensating with the branch scale
only recovers a translate or reflection of the same six-point gadget.

**Limits.** Equation (2.1) concerns preservation of old equalities. A new
scale may create different collisions. The result does not claim its image
is injective, or that every family of adaptive scales fails.

## 3. Unequal branch slopes cannot sustain a translated-slice identity

On a slice the two coordinates move together. If their slopes differ, their
difference also changes, and the cubic term exposes that change. Comparing
coefficients shows that a nontrivial identity along an entire line must use
the same slope in all four coordinates.

**TC-A3 — affine-line classification.** For real constants, suppose

$$P(\alpha t+a,\beta t+b)=P(\gamma t+c,\delta t+d)
\quad\text{for every real }t.\tag{3.1}$$

The following two descriptions exhaust the possibilities (and may overlap
in the trivial case):

1. The ordered input lines are identical:
   $\alpha=\gamma$, $\beta=\delta$, $a=c$, $b=d$.
2. All slopes are equal, $\alpha=\beta=\gamma=\delta$, and
   $(a-b)^3+a+b=(c-d)^3+c+d$.

**Proof.** The cubic coefficient gives
$(\alpha-\beta)^3=(\gamma-\delta)^3$, hence both differences equal a real
number $e$. If $e\ne0$, the quadratic coefficient gives $a-b=c-d$;
the linear coefficient then gives $\alpha+\beta=\gamma+\delta$;
and the constant coefficient gives $a+b=c+d$. These equations recover case 1.
If $e=0$, both sides are linear in $t$, and comparison gives precisely case 2. ∎

Here is how this applies to stage-dependent affine branches. Let
$F_r(x)=\lambda_rx+t_r$. Parameterize an old difference slice by
$(x,y)=(z+u,z)$, and a comparison slice by $(z+\eta+v,z+\eta)$.
A nontrivial identity

$$P(F_r(z+u),F_s(z))
=P(F_p(z+\eta+v),F_q(z+\eta))\tag{3.2}$$

forces $\lambda_r=\lambda_s=\lambda_p=\lambda_q=\lambda$.
In particular retaining the full eight-overlap pattern from §1 forces all
three branch slopes to be equal. With that common nonzero scale, put

$$U=\lambda u+t_r-t_s,\qquad V=\lambda v+t_p-t_q.$$

Then (3.2) holds identically exactly when

$$2\lambda\eta=U^3+U-V^3-V+2(t_s-t_q).\tag{3.3}$$

The anchor shift (3.3) is an algebraic condition, but the actual finite
containment additionally needs

$$z,z+u,z+\eta,z+\eta+v\in A$$

for every anchor that is claimed to be covered. No such membership or density
condition follows from (3.3).

**Limits.** Unequal slopes can create finite isolated coincidences. This
classification rules out a nontrivial identity on the full parameter line,
not those coincidences or arbitrary finite block intersections. Common slopes
remain possible, but their required anchor translations and uncovered pairs
must still be counted.

## 4. Boundedly many slice rules cover only linearly many pairs

Each fixed difference slice has at most as many pairs as the set has points.
Therefore a bounded collection of such slices cannot cover most of the
quadratic number of input pairs. This remains true even if the chosen
differences and translations change at every stage.

**TC-A4 — difference-mass bound.** For a finite set $C$ of $N$ real numbers
and any set $D$ of $L$ difference values,

$$\#\{(x,y)\in C^2:x-y\in D\}\le LN.\tag{4.1}$$

Thus at least $N^2-LN$ ordered pairs remain outside those slices. If $L$ is
fixed, or merely $L=o(N)$, this remainder is $N^2-o(N^2)$; it is not a
power-saving exceptional pair tail. To cover all but $O(N^{2-\delta})$ pairs
by such slices requires

$$L\ge N-O(N^{1-\delta}).\tag{4.2}$$

**Proof.** Each $y\in C$ determines at most one $x=y+u$ for a fixed $u$.
Sum the at-most-$N$ bound over $u\in D$, then rearrange. ∎

For the finite gadget's old rules, the differences are
$0,\pm1/3,\pm2/3,\pm1$: seven values. They capture the small gadget well,
but on an $N$-point carrier their total pair mass is at most $7N$.
Scaling the rule changes the seven numbers, not this bound.

**Limits.** This is a pair-coverage statement. The uncovered pairs could
have many collisions through another mechanism. It does not imply their
outputs are distinct. It says that a proof which charges those pairs as an
exceptional tail has a quadratic tail and has not established the required
subquadratic error.

### A stronger bound for a finite list of allowed collision moves

A rule may be specified by how much each coordinate changes, rather than by
its difference. For this cubic, each nonzero coordinate displacement still
works on at most two difference slices. So allowing a bounded list of
displacements cannot bypass (4.1).

**TC-A5 — finite-displacement certificate bound.** Let $\mathcal T$ contain
$M$ nonzero vectors $(h,k)\in\mathbb R^2$. On the $N^2$ vertices $C^2$,
draw an equality edge from $(x,y)$ to $(x+h,y+k)$ whenever both vertices
belong to $C^2$, the vector belongs to $\mathcal T$, and the two outputs
are equal. Then there are at most $2MN$ directed edges, at most $4MN$
vertices incident to a nontrivial edge, and at least

$$N^2-2MN\tag{4.3}$$

connected components in the underlying undirected graph.

**Proof.** With $u=x-y$ and $e=h-k$, subtraction gives

$$P(x+h,y+k)-P(x,y)=3eu^2+3e^2u+e^3+h+k.\tag{4.4}$$

If $e=0$, equality forces $h+k=0$, hence $h=k=0$, which was excluded.
If $e\ne0$, (4.4) is a nonzero quadratic in $u$, with at most two roots.
For each root there are at most $N$ source vertices. This gives the edge
bound and twice it for incident vertices. Each edge can decrease the number
of connected components by at most one, proving (4.3). ∎

Each connected component is a valid single-output label. If these are the
only identifications used in a certificate, its label count is at least
$N^2-2MN$. In particular $M=o(N)$ cannot give a fixed positive fraction
of saved labels relative to the trivial $N^2$ budget.

If, as a separate **additional hypothesis**, every actual output fiber is
connected by the allowed moves, then these components are exactly the
fibers. Under that hypothesis (4.3) becomes an actual-image lower bound.
Without it, (4.3) is a limitation of this certificate only: distinct
components may have equal outputs through unlisted moves.

The statement applies to stage-dependent lists chosen after seeing $C$;
only their cardinality $M$ is controlled. To save at least $\varepsilon N^2$
labels by such a certificate, one necessarily needs $M\ge\varepsilon N/2$.
This is a necessary cost, not a sufficient construction.

In particular the two concrete rules in (1.3) create at most $4N$ equality
edges on any $N$-point carrier. They explain all fourteen savings when $N=6$
but their contribution alone is asymptotically linear.

## 5. Separated copies of G do not inherit a quadratic amount of savings

A copy of the small gadget has its internal collisions. Most pairs in a
large union, however, connect two different copies. The separation between
their centers inserts extra quadratic and linear difference terms. The
following calculation keeps those terms and determines exactly when an old
collision survives inside a cross-copy block.

Let $T$ be a set of $m$ centers and $h\ne0$. Suppose the sets
$t+hG$, $t\in T$, are pairwise disjoint, so

$$C=\bigsqcup_{t\in T}(t+hG),\qquad N=6m.$$

For $a,b\in G$, put $u=a-b$, $w=a+b$, and for centers $t,s$ put $D=t-s$.
The exact cross-copy formula is

$$P(t+ha,s+hb)=(D+hu)^3+t+s+hw.\tag{5.1}$$

**TC-A6 — survival equation and sparse inherited collisions.** Suppose
$P(a,b)=P(c,d)$ is one of the 14 nontrivial equalities of $G$, and put
$v=c-d$. The corresponding equality inside the same ordered pair of copies
survives exactly when

$$3D^2+3hD(u+v)+(h^2-1)(u^2+uv+v^2)=0.\tag{5.2}$$

For each old equality, there are at most $2m$ ordered pairs of centers for
which (5.2) holds. Hence all 14 inherited equalities produce at most $28m$
equality edges among the $36m^2$ input pairs. The label count obtained by
using only these inherited edges is at least

$$36m^2-28m=N^2-\frac{14}{3}N.\tag{5.3}$$

**Proof.** Subtract two instances of (5.1), and use the old collision to
replace $w-(c+d)$ by $-(u^3-v^3)$. The difference factors as

$$h(u-v)\{3D^2+3hD(u+v)+(h^2-1)(u^2+uv+v^2)\}.$$

The prefactor is nonzero by §2. Equation (5.2) is a quadratic in $D$,
so it permits at most two real center differences. For any fixed $D$,
there are at most $m$ ordered pairs $(t,s)\in T^2$ with $t-s=D$.
Summing over the fourteen old equalities gives at most $28m$ edges; quotienting
by them saves at most one label per edge. ∎

For the two main overlap families, (5.2) is especially explicit:

$$\begin{array}{ll}
I_+:&9D^2-3hD+h^2-1=0,\\
I_-:&9D^2+3hD+h^2-1=0.
\end{array}\tag{5.4}$$

Both families survive in the same copy pair only when $D=0$ and $h^2=1$.
Indeed subtracting the equations gives $6hD=0$, and then either equation
gives $h^2=1$. Distinct disjoint copies cannot have $D=0$.
For $h=1$, $I_+$ survives only at $D=0,1/3$ and $I_-$ only at $D=0,-1/3$.
Their roots in general are

$$D=\frac{h\pm\sqrt{4-3h^2}}6\quad(I_+),\qquad
D=\frac{-h\pm\sqrt{4-3h^2}}6\quad(I_-).$$

Thus $|h|>2/\sqrt3$ destroys both main families in every cross-copy block.
For either row family in (1.2), the discriminant of (5.2) is
$12-3h^2$, so $|h|>2$ destroys all fourteen inherited collisions everywhere.

**Limits.** The copies must have a common scale, which may vary with the
stage. The center set can be arbitrary, even chosen adaptively. Equation
(5.3) only counts the old pair matchings inside a fixed pair of copies;
new collisions between unrelated pairs or between different copy blocks
are not counted and could lower the actual image. Consequently (5.3) is
an obstruction to inheriting the finite density by this simple composition
rule, not a proof that every such union has a quadratic actual image.

If the copies cease to be disjoint, $N=6m$ must be replaced by the actual
input count and the input loss charged in both coordinates. Copy-label
counts alone then give no valid gain-versus-cost conclusion.

## 6. What these obstructions do and do not charge

The gap is quantitative. A bounded collection of the six-point gadget's
identities supplies $O(N)$ identifications. A fixed saving in the full pair
budget requires $\Theta(N^2)$ identifications or another complete support
bound. Merely changing the constants at each stage does not change that
count. Growing the collection to order $N$ is necessary in this class, but
no rule supplying the corresponding endpoint closure or complete support is
proved here.

This is the construction-ledger accounting for the schemes actually studied:

| Gain or cost | Exact amount or status | Meaning |
|---|---|---|
| Carrier input | $N$; for disjoint common-scale copies, exactly $6m$ | Both lower and upper input counts known under stated disjointness |
| Input loss | None assumed in the lemmas; non-disjoint copies require a fresh count | Thinning or duplicate labels cannot be treated as free |
| Fixed difference inventory | At most $LN$ pairs | A quadratic pair tail remains if $L=o(N)$ |
| Collision displacement inventory | At most $2MN$ edges | Saving a fixed fraction of labels requires $M=\Omega(N)$ |
| Inherited copy mechanism | At most $28m$ edges for $N=6m$ | Formal support labels remain $N^2-O(N)$ |
| Missing/uncovered identifications | Uncontrolled | They may exist, but are not a proved saving |
| Common scaling | Old collisions persist only at $h=\pm1$ within one copy | Cubic-versus-linear distortion is exactly (2.1), not zero |
| Cross-copy mixed terms | Exactly (5.1)–(5.2) | All terms retained; no digitwise omission |
| Denominators/heights | Exact identities allow arbitrary real parameters | No numerical height or arithmetic amplification bound is asserted |
| Field/discriminant/regulator/splitting | Inapplicable to these real finite combinatorial lemmas | No number-field construction or tower theorem is invoked |
| Complete actual-image bound | Known for $G$; unresolved for general adaptive continuations | A large certificate count is not an actual-image lower bound without the stated exhaustiveness hypothesis |
| Asymptotic rate | No certified $\rho<\lambda^2$ from these schemes | Linear savings cannot on their own supply a uniform quadratic-budget gap |

These results use no volume model or fixed prime support. They do not invoke
the older digital obstruction beyond preserving its warning about omitted
mixed terms (T01 current state §6.5). They therefore neither reopen nor
independently re-audit those historical theorems. A stage-dependent affine
system outside their hypotheses remains subject to the direct counting
bounds here whenever its claimed savings use only the specified finite list
of slice or displacement identities.

## 7. Claim ledger and retained proof gap

All entries: T01; branch “three-branch continuation”; polynomial at the top;
date/version 2026-09-16 v1; symbolic exact evidence; no network or experiment;
new internal proof with independent lead audit recorded in [verification.md](verification.md).

| ID | Status and exact scope | Proof/dependencies | Gap retained |
|---|---|---|---|
| TC-A1 | PROVED: all eight interblock overlaps and six internal duplicates of the specified $G$ | §1; prior complete table plus explicit identities | Does not compose the finite count |
| TC-A2 | PROVED: preservation of every nontrivial old scalar collision under common affine scaling | §2; cubic expansion | New collisions after scaling unrestricted |
| TC-A3 | PROVED: every real affine-line equality and its consequence for translated old slices | §3; coefficient comparison | Isolated finite coincidences unrestricted |
| TC-A4 | PROVED: every finite carrier and every difference inventory of size $L$ | §4; at most $N$ pairs per difference | Uncovered outputs may collide |
| TC-A5 | PROVED: every carrier and finite displacement list, including adaptively selected lists | §4; quadratic in the difference and graph count | Actual-image lower bound requires exhaustive fiber connectivity |
| TC-A6 | PROVED: disjoint common-scale copies of $G$, counting precisely inherited old matchings | §5; survival quadratic and pair-difference count | Additional cross-copy collisions unrestricted |

**OPEN:** a growing family of legal slice identities, or a different complete
image certificate, that covers almost all required pairs and pays for actual
input growth. This is a retained gap rather than a new positive conjecture.
The note makes no proposed pivot to algebraic semiconjugacy, nonlinear branch
search, or arithmetic towers. The lead report chooses the cycle's single next
proof obligation after combining these proofs with the finite continuation
work.
