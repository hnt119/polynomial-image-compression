# Growing-step Cartesian coverage for the plus-sign cubic

**T01 · 2026-09-21 · new offline research cycle · version 1**

\[
P(x,y)=(x-y)^3+x+y.
\]

## 1. Short verdict

**Structural progress and scoped failures; no positive growing-step witness.**
The original cubic power-saving target and the requested sublinear-inventory
coverage construction remain **OPEN**.

This cycle proves a new universal estimate counting different steps together:
for \(N=|A|\), \(M=|S|\),

\[
\boxed{\sum_{\tau\in S}E_\tau(A)
\le9N^2M^{2/3}+NM+12N^2.}
\tag{1.1}
\]

The dependence on the inventory is sublinear, but the power of \(N\) is
larger than in the frozen single-step estimate. **This does not improve
the universal \(N^{1/6}\) threshold for quadratic coverage.** It improves
the edge exponent when \(M=N^\theta\) with \(\theta>1/2\).

Stronger conclusions hold for the actual images of explicit broad families:

- Integer and third-integer intervals already have every whole cubic fiber
  connected by \(T_1\). More steps add redundant edges; their actual images
  are \(N^2-\Theta(N^{3/2})\).
- Every affine-lattice carrier \(A\subset a+h\mathbb Z\) with diameter
  \(D=o(h^3N^2)\) has \(|P(A,A)|=N^2-o(N^2)\), even if every possible
  collision step is supplied.
- Explicit faithful coefficient boxes have all nontrivial fibers confined
  to one-dimensional slices. Their actual images are calculated exactly.
- Fixed rational additive completion, including the tested diagonal-return
  recursion, has actual image \(N^2-O(N^{3/2})\) at every growing depth.

A shared output-by-difference grid achieves \(\Theta(N^{4/3})\)
prescribed pairs from \(N\) scalars, but this still occupies a vanishing
fraction of \(A^2\). No positive-proportion asymptotic coverage construction
was obtained. These are scoped structural theorems, not a universal
impossibility result for the cubic.

Complete proofs are in [structure and reuse](structure-and-reuse.md),
[the progression laboratory](progression-laboratory.md), and
[multi-step bounds](multistep-bounds.md). All new main proofs were independently
checked internally. No external review or novelty claim is made.

## 2. What changed after the fixed-step theorem

The [preceding report](../2026-09-21-cubic-returns/README.md) proved the
uniform bound \(E_\tau(A)\le5N^{11/6}\) for every nonzero real step.
That theorem is a frozen dependency and was not reproved or reopened.

Each \(T_\tau\) translates the difference \(u=x-y\) while holding
\(z=P(x,y)\) fixed. The inverse coordinates are

\[
x_z(u)=\frac{z-u^3+u}{2},\qquad y_z(u)=\frac{z-u^3-u}{2}.
\]

The new question is whether many individually sparse maps can cooperate
to connect almost all pairs. This requires counting actual connected
components, rather than just summing edge counts.

The cycle stayed offline. Its declared finite cap was 80 carriers,
240 carrier/inventory cases, 128 distinct inputs per carrier, 3,000,000
exact pair or edge checks, and 90 research CPU seconds. The approved run
used 32 carriers and six inventories each; no old research grid was rerun.
Arithmetic amplification remained deferred.

## 3. Exact multi-step and fiber-graph formulation

**Meaning.** At a fixed output, a permitted edge joins two allowed difference
coordinates. Every intermediate endpoint of a path must actually occur.

**Precise statement.** Put

\[
U_A(z)=\{u:x_z(u),y_z(u)\in A\}.
\]

For an undirected graph, replace \(S\) by its positive absolute values
\(S^+=\{|\tau|:\tau\in S\}\), removing duplicate signs. Then
\(G(A,S)\) is exactly the disjoint union over \(z\) of the finite
graphs on \(U_A(z)\) joining \(u,v\) when \(|u-v|\in S^+\).
In particular,

\[
e(G)=\sum_{\tau\in S^+}E_\tau(A),\qquad
\boxed{|P(A,A)|\le C(G).}
\tag{3.1}
\]

**Proof.** The frozen coordinate map is a bijection, and each symmetry
is precisely \((u,z)\mapsto(u+\tau,z)\). Every edge therefore stays
in one output fiber. Components map onto outputs, proving (3.1).
Each distinct undirected edge has one positive difference, so its edge
count in (3.1) is exact.

**Why it matters.** This is the full-support certificate. It counts all
isolated vertices as components and charges every pair.

**Scope and correction to the prompt.** If
\(\Gamma=\langle S\rangle_{\mathbb Z}\), a component is contained in
\(U_A(z)\cap(u+\Gamma)\); equality is not automatic. For
\(A=\{-5,-3,0\}\), the zero-output fiber has exactly differences
\(\{0,2\}\). With \(S=\{1\}\), both lie in the same integer coset
but remain disconnected. The proof companion verifies all nine outputs.
Thus the unconditional coset assertion in §13 of the request is corrected,
while its group law is retained.

## 4. Coverage implication and the inventory cost

**Meaning.** Many edges can lie within already connected components.
What matters is how many pairs are organized into genuinely large components.

**Precise statement and proof.** Suppose all but \(B\) vertices lie in
components with at least \(K\ge2\) vertices. The large components number
at most \(N^2/K\); the remaining components number at most their \(B\)
vertices. Hence

\[
\boxed{|P(A,A)|\le C(G)\le N^2/K+B.}
\tag{4.1}
\]

Every connected component of size \(r\) contains a spanning tree with
\(r-1\) edges. Thus

\[
e(G)\ge(1-1/K)(N^2-B).
\]

The frozen single-step bound gives \(e(G)\le5MN^{11/6}\), where
\(M=|S^+|\). With \(K\ge N^\varepsilon\) and
\(B=O(N^{2-\delta})\), necessarily

\[
M\ge(1/5-o(1))N^{1/6}.
\tag{4.2}
\]

**Why it matters.** Such coverage would prove
\(O(N^{2-\min(\varepsilon,\delta)})\) for the whole cubic image.
Every smaller fixed positive exponent absorbs the prefactor.

**Scope.** This cost is inherited and derived here for the multi-step
coverage criterion. It is necessary, not sufficient. Neither the number
of formal step labels nor the number of cyclic edges earns a second saving.

## 5. Arithmetic progressions: more edges, unchanged components

**Meaning.** These carriers provide a complete laboratory: all useful
steps, all component sizes, and the actual image can be determined.

**Precise statement — PROVED.** For \(A_{r,N}=\{j/r:0\le j<N\}\),
\(r\in\{1,3\}\), every nonempty fiber is an interval in one coset of
\(\mathbb Z\). All useful steps are integers. Therefore for every
\(S=\{1,\ldots,M\}\), \(M\ge1\), the components are exactly the
actual cubic fibers, and

\[
|P(A_{r,N},A_{r,N})|=N^2-E_1(A_{r,N}).
\tag{5.1}
\]

For each integer \(k\ge1\), put

\[
b_{r,k}(d)=\frac{3kd^2}{2r}+\frac{3k^2d}{2}
                 +\frac{r(k^3+k)}2,
\quad w_{r,k}(d)=b_{r,k}(d)+\max(0,d)-\min(0,d+rk).
\]

Then the exact count, valid for growing \(k\), is

\[
E_k=\sum_{d\in\mathbb Z}(N-w_{r,k}(d))_+.
\tag{5.2}
\]

For fixed \(k\), it is
\(\frac43\sqrt{2r/(3k)}N^{3/2}+O_{r,k}(N)\).
Writing \(E_0=N^2\), the full fiber/component distribution and threshold
mass are

\[
n_\ell=E_{\ell-1}-2E_\ell+E_{\ell+1},\qquad
B_\ell=\ell E_{\ell-1}-(\ell-1)E_\ell.
\tag{5.3}
\]

The longest component has size \(2(N/r)^{1/3}+O(1)\); an exact
parity-dependent formula is in GS-A3. Nonisolated mass is exactly
\(2E_1-E_2=\Theta(N^{3/2})\), for every inventory containing 1.
No inventory can cover more vertices than these nonsingleton actual fibers.
Meanwhile the number of edges for \(S=\{1,\ldots,M\}\) is

\[
\Theta_r\left(N^{3/2}\sqrt{\min\{M,N^{1/3}\}}\right),
\tag{5.4}
\]

and saturates at \(\Theta(N^{5/3})\). The extra edges create cycles
inside components whose sizes were already attained with one step.

**Proof idea, with full proof in [GS-A1–A3](progression-laboratory.md).**
For third-integer inputs, reducing \(27P=d^3+9(i+j)\) modulo nine
forces all difference indices in a fiber into one residue class modulo
three. On this unit-spaced real coset, both \(u^3+|u|\) and
\(u^3-|u|\) are nondecreasing. The interval endpoint restrictions
therefore leave no holes. Counting the span of the four scalar indices
gives (5.2). A fiber of size \(j\) contributes \((j-k)_+\) returns
at step \(k\), which yields (5.3) by finite differences.

**Why it matters.** The actual images are

\[
N^2-\frac43\sqrt{2/3}\,N^{3/2}+O(N)
\quad\text{and}\quad
N^2-\frac{4\sqrt2}{3}N^{3/2}+O(N),
\]

respectively. No value of \(M\) makes these carriers work.

**Scope.** Every fixed real spacing \(h>0\) also has
\(|P(A,A)|=N^2-O_h(N^{3/2})\), by a distinct-cube gap estimate.
If \(h^2\) is irrational, the image is exactly \(N^2\).
The varying-spacing bound is useful when \(h\sqrt N\to\infty\);
it may be uninformative at mesh \(N^{-1/2}\) or below. Interval-fiber
connectivity is asserted only for the two specified spacings.

## 6. A universal bound that counts many steps together

**Meaning.** Fixing the original first coordinate and the step makes the
transformed pair trace a parabola. Returns from all steps can be counted
as incidences of these curves with the new Cartesian square.

**Precise statement — PROVED.** For every real finite carrier and every
finite nonzero step set, here taking \(M=|S|\) and counting both signs
separately if both are present,

\[
\sum_{\tau\in S}E_\tau(A)\le
\min\{5MN^{11/6},\ 9N^2M^{2/3}+NM+12N^2,\ N^2(N-1)\}.
\tag{6.1}
\]

**Proof idea; complete proof in [GS-U1](multistep-bounds.md).** Write
\((v,w)=T_\tau(x,y)\), \(d=v-w\). Then

\[
v=-\frac{3\tau}{2}d^2+\frac{3\tau^2}{2}d
  +x+\frac{\tau-\tau^3}{2}.
\]

The \(NM\) parameter pairs \((x,\tau)\) give distinct parabolas,
and \(A^2\) gives \(N^2\) distinct points \((v-w,v)\). Two curves
intersect at most twice. Two distinct points determine at most two steps,
because their possible \(\tau\)'s satisfy a quadratic equation; each
step then determines \(x\). Every actual return injects into an incidence.
Apply the elementary crossing argument already proved in the preceding
cycle. No new external theorem is assumed.

**Why it matters.** The leading exponent is \(2+2\theta/3\) when
\(M=N^\theta\), improving \(11/6+\theta\) for \(\theta>1/2\).
It is a new joint estimate rather than a restatement of the sum bound.

**Scope.** Its exponent is still above two for every \(\theta>0\).
It does not force subquadratic nonisolated mass in that range. An improvement
in the universal coverage threshold remains unresolved.

## 7. A structural restriction on every actual collision

**Meaning.** Two points on one fiber differ in their second coordinates by
a positive amount. If their difference coordinates are separated, the
cubic forces a large displacement. In a narrow carrier, collisions must
therefore lie close to the diagonal.

**Precise statement — PROVED.** Let \(D\) be the diameter of \(A\),
\(\delta\) its minimum scalar gap, and \(\eta\) the minimum positive
gap between distinct elements of \(A-A\). For \(N\ge2\), every vertex
in a nonsingleton actual fiber satisfies

\[
|x-y|\le R:=D^{1/3}+\sqrt{2D/(3\eta)}.
\]

The total number of these vertices is at most
\(N\min\{N,1+2\lfloor R/\delta\rfloor\}\). In particular, for
\(A\subset a+h\mathbb Z\), set \(W=D/h^3\). Then

\[
\boxed{|P(A,A)|\ge N^2-
N\min\{N,1+2\lfloor W^{1/3}+\sqrt{2W/3}\rfloor\}.}
\tag{7.1}
\]

**Proof.** If two differences are \(u,u+\tau\), \(\tau>0\), and
\(m=u+\tau/2\), the decrease in the second coordinate is

\[
\frac\tau2\left(1+3m^2+\frac{\tau^2}{4}\right)\le D.
\]

Use \(\tau\ge\eta\), bound the midpoint and the half-step separately,
and count scalars within distance \(R\) of each anchor using spacing
\(\delta\). On a common lattice both separation parameters are at least
\(h\), yielding (7.1). Pairs outside nonsingleton fibers give distinct
singleton outputs. The complete argument is GS-U2/U3.

**Why it matters.** If \(D=o(h^3N^2)\), the exceptional mass in (7.1)
is \(o(N^2)\), proving an actual-image obstruction for every inventory.
For integers this includes arbitrary sparse sets of diameter \(o(N^2)\).
The general formula also gives an explicit necessary small-gap condition
on \(A-A\) for a prospective high-coverage carrier.

**Scope.** Scalar spacing cannot replace difference-set spacing for general
real sets. Tiny \(\eta\), very wide carriers, and rapidly shrinking
common meshes can make this bound vacuous. They are not thereby positive
constructions.

## 8. Best constructive carriers and coordinate reuse

**Shared cubic grid.** Choose outputs \(z=2b\), \(0\le b<H\), and
differences \(1\le j\le L\). Put both coordinates
\(b-(j^3-j)/2\), \(b-(j^3+j)/2\) into one scalar set. This creates
\(HL\) distinct prescribed pairs in \(H\) chains, but GS-P3 proves

\[
HL\le4N^{4/3}.
\]

At \(H=L^3\), the exact scalar count is \((3L^3+L)/2\), and the
construction attains the \(N^{4/3}\) order. Its prescribed-pair/scalar
ratio is \(\Theta(N^{1/3})\); the required quadratic ratio is absent.
At this parameter choice the whole carrier is an integer interval,
so the full-image obstruction also applies to incidental pairs.

**Faithful coefficient boxes.** For fixed rank \(r\ge2\), side length
\(L\), base \(B=100(L+1)^3\), and weights
\(1,B,B^4,B^{16},\ldots\), take all digit vectors in
\(\{0,\ldots,L-1\}^r\). The projection is injective and \(N=L^r\).
GS-P4 gives an exact classification:

\[
|P(A,A)|=N^2-L^{r-1}E_1(I_L).
\tag{8.1}
\]

If the two inputs differ in any higher digit, the cubic, quadratic and
linear coefficient layers recover the entire ordered pair. Every nontrivial
fiber must stay in one common higher-digit slice. The total available mass
is only \(\Theta_r(N^{1+1/(2r)})\), for every inventory. This is a
structural classification of actual fibers, stronger than a failed upper
certificate. The proof charges coefficient size and proves no carries
can identify the outputs.

**Recursive completion.** Fixed rational shifts give
\(A_m=A_0+mC\), \(N_m=\Theta(m+1)\), fixed mesh and diameter
\(O(N_m)\). GS-P5 proves actual image
\(N_m^2-O(N_m^{3/2})\), for all depths and every step inventory.
This includes the exact recursion tested below, obtained by adjoining
coordinates of \(T_1(t,t)\) and \(T_{1/3}(t,t)\).

**Scope.** Correlated subsets of the output/difference grid, nonfaithful
coefficient projections, and nonlinear off-diagonal completions remain
outside these theorems. Their input multiplicities and whole-square costs
have not been solved. No positive asymptotic carrier was produced.

## 9. Exact experiments and component coverage

**EXPERIMENTAL — exact finite evidence only.** Thirty-two carriers were
tested with six inventories each: short integer steps, integer steps up to
\(\lceil\sqrt N\rceil\), third-integer steps, the most frequent useful
steps at two sizes, and all useful steps as a diagnostic benchmark.
Carriers include APs, two blocks, two-dimensional rational coefficient
boxes, polynomial sequences, planted multiple fibers, and two recursive
completion levels.

| Carrier/inventory | \(N\) | \(M\) | Edges | Nonisolated vertices | Largest component | Components | Actual image |
|---|---:|---:|---:|---:|---:|---:|---:|
| Integer AP, steps 1–3 | 128 | 3 | 3,404 | 1,926 | 10 | 14,890 | 14,890 |
| Integer AP, all useful | 128 | 9 | 5,644 | 1,926 | 10 | 14,890 | 14,890 |
| Third-integer AP, steps 1–3 | 128 | 3 | 5,508 | 3,220 | 7 | 13,906 | 13,906 |
| Third-integer AP, all useful | 128 | 6 | 7,130 | 3,220 | 7 | 13,906 | 13,906 |
| Two integer blocks, most frequent | 32 | 6 | 316 | 274 | 5 | 846 | 846 |
| Rational box \(i+3j/2\), most frequent | 34 | 4 | 310 | 222 | 5 | 1,002 | 1,002 |
| Four planted fibers, most frequent | 108 | 11 | 1,548 | 820 | 17 | 11,076 | 11,064 |
| Four planted fibers, all useful | 108 | 16 | 1,636 | 842 | 17 | 11,064 | 11,064 |
| Diagonal completion, level 1, most frequent | 16 | 4 | 102 | 96 | 5 | 192 | 192 |
| Diagonal completion, level 2, most frequent | 30 | 6 | 389 | 214 | 8 | 740 | 740 |

These counts include every ordered pair, all singleton components, and
all actual output collisions. The first AP comparison illustrates the
danger: 2,240 additional edges give zero additional coverage or component
reduction. In the planted example, 12 extra components still share outputs
under the frequent-step inventory; component count and image differ.

The [complete summary](../../../examples/2026-09-21-growing-step-cubic.json)
records full component and actual-fiber size distributions, components per
output, cycle excess, all exact step lists and their rational complexity,
threshold coverage, and covered-pair/scalar ratios. Raw records contain
every input, fiber, component and edge. The all-useful inventory connects
whole actual fibers by definition; its size is charged, and it is not an
independent construction theorem.

The run used **76,303 cubic evaluations**, **702,259 charged pair/edge
checks**, and **2.232581 CPU seconds**, with no errors and largest input
128. Direct symmetry oracles agreed with the fiber-based graphs on the
declared small cases. Tiny additional oracles checked the subgroup
counterexample and the exact faithful-box theorem. The [verification
record](verification.md) separates those tests and repository regressions
from the one research grid.

## 10. Full gain-versus-cost ledger

The [completed construction ledgers](construction-ledgers.md) instantiate
the repository template and record selection order, scalar counts, projection
fibers, denominators, heights, inventory size, all uncovered pairs, and
the resulting exponents.

The conclusion is the same across the examined constructions: no strictly
positive full-support exponent gap was established. For the grid, prescribed
coverage is subquadratic and exceptions still number \(N^2-o(N^2)\).
For the classified AP, lattice, faithful-box and rational-completion families,
the actual image is asymptotically quadratic. Finite rational boxes and
planted fibers outside a proved class retain only finite evidence.

No input thinning, parameter multiplicity, or growing denominator was
silently assigned zero cost. No number-field, splitting, Chebotarev, unit,
trace or norm amplification was started.

## 11. Implication for T01 and provenance

The frozen single-step theorem survives unchanged. CR-O1 was commissioned
and attacked here, but its positive witness remains **OPEN**. The new
universal incidence estimate does not close all sublinear inventories.
The actual-image obstructions are explicitly scoped and do not imply that
every finite real set has a quadratic cubic image.

Earlier three-branch and fixed-step reports and their data were preserved.
This cycle uses the locally available coordinate, counting and graph proofs;
the unavailable original historical digital/rich-fiber checkpoint bytes
remain unavailable under MC-06 and are not dependencies. Their proofs were
not reconstructed or recertified. The separate T01 quadratic branch and
the other three fixed targets remain distinct and unchanged by this cycle.

## 12. Claim ledger

Every new entry is T01 / growing-step cubic, polynomial displayed at the
top, 2026-09-21 v1. Evidence is the complete exact proof at the stated
locator, except GS-X1. Independent internal audit scopes are recorded in
[verification.md](verification.md); no external review or novelty is claimed.

| ID | Status and quantifiers | Proof locator/dependencies | Retained limit |
|---|---|---|---|
| GS-P1 | PROVED; all finite real carriers/inventories, graph and coverage counts | structure-and-reuse §1; frozen conjugacy and CR-U1 | No sufficient carrier |
| GS-P2 | PROVED correction; subgroup containment with explicit failure of equality | structure-and-reuse §2 | Connectivity needs a path inside the finite fiber |
| GS-P3 | PROVED; every integer \(H,L\ge1\), full cubic-grid reuse bound | structure-and-reuse §3; exact interval union | Arbitrary correlated grids outside scope |
| GS-P4 | PROVED; every fixed rank and all side lengths, faithful-box fiber classification | structure-and-reuse §4; coefficient recovery, GS-A1/A3 | Nonfaithful projections outside scope |
| GS-P5 | PROVED; fixed rational seed/shifts, every growing depth | structure-and-reuse §5; GS-U3 | Nonlinear/changing-step recursions outside scope |
| GS-A1/A2 | PROVED; integer/third-AP exact fibers and every integer-step count | progression-laboratory §§1–2 | Other spacings may have fiber gaps |
| GS-A3 | PROVED; those APs, every inventory \(1,\ldots,M\), full distribution and edge saturation | progression-laboratory §3 | Redundant edges do not enlarge components |
| GS-A4 | PROVED; all real AP spacings, explicit varying-scale bound | progression-laboratory §4 | Small meshes can make bound vacuous |
| GS-U1 | PROVED; all finite real carriers and step sets | multistep-bounds §1; frozen elementary crossing lemma | No improved universal coverage threshold |
| GS-U2/U3 | PROVED; all real sets with stated separations; affine-lattice specialization | multistep-bounds §§2–3; exact cubic displacement | Width/mesh or gap hypotheses essential |
| GS-X1 | EXPERIMENTAL; 32 carriers, 192 declared graphs | summary JSON and verification record | No asymptotic promotion |
| CR-O1 | OPEN; one controlled growing-step coverage witness | §14 below; GS-P1 implication | Construction missing |

## 13. Failure and scope ledger

| Mechanism or inference | Status | Exact scope |
|---|---|---|
| Generated-subgroup cosets are automatically components | FAILED assertion | Counterexample is an actual cubic fiber, not just an abstract graph |
| Many added AP steps create new coverage | FAILED | Whole fibers already connected for the two specified spacings |
| Fixed-spacing APs give power saving | FAILED actual-image family | Every fixed real spacing; irrational squared spacing is injective |
| Moderate-width common-lattice carriers | FAILED actual-image family | \(D=o(h^3N^2)\), including varying mesh when this ratio vanishes |
| Full consecutive output-by-difference grids | FAILED prescribed-coverage certificate | At most \(4N^{4/3}\) prescribed pairs; selected counts alone do not lower-bound all images |
| Faithful coefficient boxes | FAILED actual-image family | Fixed rank, cubic output coefficients survive projection |
| Fixed rational additive/diagonal completion | FAILED actual-image family | Fixed seed and shift set, all depths, every graph inventory |
| New \(M^{2/3}\) estimate closes every sublinear inventory | Not proved | It improves large-inventory edge counts only |
| All useful steps establish a small-support construction | Invalid inference | They merely reproduce whatever actual fibers already exist |
| General growing-step Cartesian witness | OPEN | No positive asymptotic coverage construction obtained |

## 14. Exactly one next proof obligation

**CR-O1 remains OPEN — the prioritized sublinear-inventory subcase.**
Construct arbitrarily large finite real \(A_N\), \(|A_N|=N\), and
explicit nonzero step lists \(S_N\), with fixed
\(1/6\le\theta<1\) and \(\varepsilon,\delta>0\), such that
\(|S_N|\le N^\theta\) and all but \(O(N^{2-\delta})\) vertices lie
in components of size at least \(N^\varepsilon\).

Prove actual scalar membership and counts, coordinate reuse, useful step
complexity, connectivity without missing intermediate points, and the
exception count. A witness must escape the actual-image families closed
here; merely widening a step list on those carriers cannot work. Equation
(4.1) then supplies the complete cubic power saving. The broader original
obligation without a sublinear inventory cap also remains unresolved.

This is the sole adopted next obligation. The other unresolved estimates
are retained limitations, not a menu of new assignments. No further search
or arithmetic amplification is started by recording it.
