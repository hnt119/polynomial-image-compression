# Sublinear cubic symmetries: coordinate reuse and structural obstructions

**T01 · 21 September 2026 · version 1 · offline research**

\[
P(x,y)=(x-y)^3+x+y.
\]

This report answers the commissioned follow-up to the
[growing-step cycle](../2026-09-21-growing-step-cubic/README.md).
It contains new proof search and a new bounded exact grid, not a rerun or
documentation freeze. All proof claims are internal; no novelty or external
review is claimed. Earlier reports and their data are preserved.

## 1. Short verdict

**OPEN:** no carrier with a common sublinear inventory and almost-full
polynomial-component coverage was constructed. No universal obstruction
raising the necessary inventory exponent above \(1/6\) was proved.

**PROVED:** substantial new obstructions and exact reductions were obtained:

- Nonfaithful quadratic projections, including an explicitly many-to-one
  three-parameter projection, still have almost \(N^2\) actual outputs.
  At critical rational shrinking scales a positive fraction of pairs still
  lies in fibers of bounded size.
- Changing prime-denominator, nonuniform rational carriers admit an exact
  decomposition of every nontrivial fiber into one residue-class square.
  This proves quadratic actual images in a fine-mesh regime not covered
  by the previous whole-carrier width test.
- A new bound counts **covered vertices** according to the sizes of the
  chosen steps. It applies to arbitrary real carriers and shows that
  separated nonlattice sets require many steps of order \(1/N\) or smaller.
- Exact coordinate-sharing identities constrain affine template reuse and
  the propagation of shared coordinates across a common-step edge.

These are scoped negative and structural results, closest to the prompt's
structural-reduction outcome. They do not fulfill its constructive outcomes
or its requested stronger universal exponent.

## 2. What the preceding cycle proved and did not prove

The accepted starting point is CR-U1, the universal single-step estimate
\(E_\tau(A)\le5N^{11/6}\), and GS-U1,
\[
\sum_{\tau\in S}E_\tau(A)
\le9N^2M^{2/3}+NM+12N^2,\qquad M=|S|.
\]
These were used as frozen inputs. They force at least order \(N^{1/6}\)
steps for almost-full large-component coverage, but do not exclude every
sublinear inventory.

The preceding cycle also proved actual-image obstructions for its stated
AP, moderate-width lattice, faithful-box and fixed rational completion
families, plus the \(4N^{4/3}\) prescribed-pair bound for its full consecutive
fiber grid. Those families were not restarted.

One precision correction to the current prompt: for arbitrary fixed real
AP spacing the earlier theorem is \(N^2-O_h(N^{3/2})\), not universally
\(N^2-\Theta_h(N^{3/2})\). Irrational squared spacing gives injectivity.
The matching loss was proved for the specified integer/third-integer
progressions. This correction does not alter the prior failed-family verdict.

The previous work supplied no almost-full growing-step witness. It also
proved that subgroup-coset containment is not automatic finite connectivity.

## 3. Exact fiber and component formulation

For every output \(z\),
\[
U_A(z)=\{u:(z-u^3+u)/2,\ (z-u^3-u)/2\in A\}.
\]
There are exactly \(N^2\) vertices across these finite fiber sets. Normalize
the undirected inventory to distinct positive absolute values. Within each
\(U_A(z)\), join \(u,v\) exactly when \(|u-v|\) belongs to that inventory.
Paths must remain inside the actual finite set.

Let \(e,V,C\) denote edges, nonisolated vertex mass and components,
respectively, and let \(s=|P(A,A)|\). Always
\[
s\le C,\qquad C\ge N^2-e.
\]
If \(B_K\) is the mass of components smaller than \(K\), then
\[
\boxed{s\le N^2/K+B_K.}
\tag{1}
\]
Thus \(K\ge N^\varepsilon\) and \(B_K=O(N^{2-\delta})\) would solve
the fixed cubic with every positive exponent strictly below
\(\min(\varepsilon,\delta)\). Edges, \(V\), \(C\), and \(s\) remain
different quantities throughout this report.

## 4. Coordinate-reuse reformulation

Full statements and proofs are in
[correlated-reuse, SC-R1–R3](correlated-reuse.md).
For any distinct prescribed labels \(F=\{(z,u)\}\), let \(Q=|F|\), and
let \(A_F\) be the union of their two required scalar coordinates.
These prescribe exactly \(Q\) distinct ordered pairs. If \(N=|A_F|\),
their average coordinate occurrence multiplicity is exactly \(2Q/N\).
Near-full prescribed coverage therefore needs average reuse of order \(N\).

The supplied coordinate-sharing equations are exact. The new classification
is limited but rigorous:

| Reuse pattern | Proven classification |
|---|---|
| Affine matching \(v=\alpha u+\beta\) between two fixed scalar-coordinate templates | At most three matches, unless the entire template is identical |
| Nonzero translation matching | At most two matches |
| Opposite coordinate signs with identical difference parameter | Exactly one match |
| Two distinct outputs sharing both second-coordinate endpoints of the same nonzero step | Exactly one real matched pair before scalar membership restrictions |
| Unrestricted nonlinear or varying-index reuse across many fibers | OPEN |

For the last proved statement, the differences must satisfy \(v=-u-\tau\);
the remaining cubic equation is strictly monotone and has exactly one
solution. This is an exact algebraic constraint, not a finite observation.

The many-to-one projection in §9 is another exact algebraic family, with
every input multiplicity counted. The shared-anchor examples in §6 are
finite experimental patterns. None is promoted to a successful asymptotic
parametrization.

## 5. Correlated sum/difference formulation

SC-R1 identifies the correct domain:
\[
\Omega_A=\{(u,L):(L+u)/2\in A,\ (L-u)/2\in A\},\qquad |\Omega_A|=N^2,
\]
\[
P(A,A)=\{u^3+L:(u,L)\in\Omega_A\}.
\]
Separate membership in \(A-A\) and \(A+A\) is insufficient. For
\(A=\{0,1\}\), the choices \(u=1,L=0\) satisfy those separate conditions
but give scalars \(1/2,-1/2\), outside \(A\).

The new grid tested the genuinely correlated prescription \(L=2r+u^2\)
on its declared rational parameters and then added both required scalars.
Its full square, including all unprescribed and cross-block pairs, was
enumerated. The resulting small fibers did not provide almost-full coverage.

For any reverse prescription organized into connected sets of size at
least \(K\), the exact sufficient bound is
\[
|P(A_F,A_F)|\le Q/K+(N^2-Q).
\tag{2}
\]
This keeps the unprescribed complement visible. A product-like parameter
grid is not enough until both its scalar image and its output/component
multiplicities have been counted.

## 6. Best new construction examined

There is no proved asymptotically successful construction. The most
informative new finite reverse design uses shared scalar anchors:
\[
a=k/q,\quad u=j/q,\quad z=u^3-u+2a,\quad
v=u+e/q,\qquad e\in\{-1,0,1\}.
\]
The middle point has first coordinate exactly \(a\); adjoining both
coordinates at the three values of \(v\) supplies common-step paths.
The tested ranges are \(q=3,5,7\), \(0\le k<H\), \(H=2,3\), and
\(0\le j<4\).

For \(q=3,H=3\), 72 coordinate occurrences collapse to \(N=29\)
scalars. A declared 10-step inventory has:

| Statistic | Exact value |
|---|---:|
| Full ordered-pair count | 841 |
| Actual image | 723 |
| Edges | 262 |
| Nonisolated vertices | 167 |
| Components | 723 |
| Largest component and fiber | 7 |
| Vertices in components of size at least 6 | 39 |

All actual fibers are connected in this example, yet 674 vertices remain
isolated. Applying (1) at \(K=6\) gives \(5653/6>841\), a vacuous
power-saving certificate. Coordinate reuse and common steps are present;
their useful pair coverage is insufficient.

For both changing-scale completion rules, the three tested levels give
\(N=6,18,54\), images \(28,294,2808\), and nonisolated mass \(14,48,162\).
The nonisolated fraction falls from \(7/18\) to \(4/27\) to \(1/18\).
This is finite evidence only, not a general recurrence theorem.

## 7. Best new component-coverage estimate

**Meaning.** A large step along a cubic fiber moves the second scalar
coordinate too far unless the source pair lies near the diagonal.

**Statement — PROVED, SC-U2.** Write \(D=\operatorname{diam}(A)\),
\[
Q_A(r)=\#\{(x,y)\in A^2:|x-y|\le r\},\quad
m(t)=|S^+\cap(0,t)|,\quad
R(t)=D^{1/3}+\sqrt{2D/(3t)}.
\]
For every \(t>0\),
\[
\boxed{V(A,S)\le
\min\{N^2,\ 10m(t)N^{11/6}+Q_A(R(t))\}.}
\tag{3}
\]
This also bounds the mass of components of every size threshold \(K\ge2\).

**Proof.** An edge with positive step \(\tau\) and midpoint difference \(m\)
moves the second coordinate by
\(\tau(1+3m^2+\tau^2/4)/2\le D\). Both endpoint differences therefore
have absolute value at most \(R(\tau)\). All edges with \(\tau\ge t\)
stay within the \(Q_A(R(t))\) band. The smaller steps have at most
\(5m(t)N^{11/6}\) edges and twice that many endpoints. Take their union.
The [full proof](multistep-obstruction.md) handles signs and every endpoint.

**Why it matters.** For uniformly separated real sets of diameter \(O(N)\),
all inventories with steps at least \(N^{-\beta}\), \(0\le\beta<1\),
have \(V=O(N^{(3+\beta)/2})\), regardless of inventory size. Positive
density coverage requires order \(N^{1/6}\) steps below \(K/N\) for a
suitable fixed \(K\). This includes perturbed nonlattice carriers whose
difference gaps can be arbitrarily tiny.

**Scope.** This is a graph-coverage bound. It is not an actual-image lower
bound for all such perturbed carriers. The same tiny steps may satisfy
several nested scale restrictions; their costs cannot be added again.

## 8. Best multi-step upper bound and the universal limit

The best proved universal edge-power bound available after this cycle is
still the minimum of the two frozen bounds in §2. Equation (3) is a new,
scale-sensitive vertex-coverage bound, not a stronger universal edge exponent.

**PROVED, SC-U1:** retaining the fourth coordinate gives the exact marked
incidence formulation
\[
(d,v)\in\{(v-w,v):v,w\in A\},\qquad
v=-3\tau d^2/2+3\tau^2d/2+x+(\tau-\tau^3)/2,
\]
\[
\boxed{d\in x+\tau-A,\qquad x\in A,\ \tau\in S.}
\tag{4}
\]
The last condition is exactly the old second-coordinate membership.
No projection multiplicity is omitted.

The attempt to improve the exponent solely by reducing intersections of
these parabolas fails: SC-U4 proves at least
\(N(N+1)M(M-1)/2\) curve-pair intersection incidences whenever
\(S\subset(0,1)\). Those geometric intersections need not be actual
Cartesian returns. Three-point uniqueness also supplies no proved stronger
power bound on its own.

**OPEN:** a universal inventory threshold greater than \(1/6\).
No claim that the fourth-coordinate restriction is powerless is made.

## 9. Multiscale and nonfaithful projection analysis

### Quadratic algebraic projection

For fixed nonsquare \(D>0\), take
\(A=t+h\{a+b\sqrt D:0\le a<L,\ 0\le b<K\}\), \(N=LK\).
Formal cubic coefficients collapse because \((\sqrt D)^2=D\).
Nevertheless **SC-Q1 / PROVED** confines every nonsingleton pair difference
\(p+q\sqrt D\) to
\[
|p^2-Dq^2|\le\frac{8(L-1+\sqrt D(K-1))}{3\beta},
\quad \beta=\sqrt{|h^2(h^2)'|},\quad h^2\in\mathbb Q(\sqrt D).
\]
For balanced unscaled boxes this gives
\[
\boxed{|P(A,A)|=N^2-O_D(N^{3/2}\log(2N)).}
\tag{5}
\]
The proof multiplies two real cube-factor inequalities and uses a nonzero
integer product of conjugate differences. It imports no norm/trace
amplification or external theorem.

For balanced boxes with rational \(h^2\), **SC-Q2 / PROVED** goes further:
if \(h^2L\ge\kappa>0\), a fixed positive fraction of all vertices belongs
to actual fibers of bounded size. Hence
\[
|P(A,A)|\ge c_{D,\kappa}N^2.
\tag{6}
\]
The theorem covers the critical scale \(h\asymp N^{-1/4}\).
The smaller regime \(h^2L\to0\) is outside this conclusion.

The explicit projection
\((a,b,c)\mapsto a+b\sqrt D+c(\sqrt D)^2\) has \(L^3\) parameter
points but only \(((D+1)(L-1)+1)L\) actual scalars. **SC-Q3 / PROVED**
computes every projection fiber and still obtains (5).
**SC-Q4 / PROVED:** if \(h^2\notin\mathbb Q(\sqrt D)\), any finite
carrier in that coefficient field becomes exactly cubic-injective after
scaling by \(h\). Full proofs and constants:
[quadratic projections](reuse-and-projections.md).

### Growing prime denominator

**SC-D1/D2 / PROVED.** Let \(A=a+B/p\), \(B\subset\mathbb Z\), width
\(W\), \(p\ge5\) prime, \(p\equiv2\pmod3\), \(2W<p^2\).
Every off-residue pair is a singleton actual fiber. All remaining fibers
are confined to exactly one residue-class square, and the images of these
squares are disjoint. Consequently, with
\(F(D)=1+2\lfloor D^{1/3}+\sqrt{2D/3}\rfloor\),
\[
\boxed{|P(A,A)|\ge N^2-NF(W/p),\qquad
\text{nonsingleton mass}\le NF(W/p).}
\tag{7}
\]
In particular \(W/p=o(N^2)\) closes this nonuniform fine-mesh class for
every inventory. The old test on the whole carrier would use
\(Wp^2/N^2\), while the new sufficient test uses \(W/(pN^2)\), under
the explicit additional congruence and width hypotheses.

**Proof idea.** Clearing denominators forces \(d^3=e^3\pmod{p^2}\).
For \(p\nmid d\), cube injectivity modulo \(p\), factorization and the
width bound give \(d=e\), hence identical pairs. Otherwise both
differences are divisible by \(p\); reduction after division by \(p^2\)
forces both pairs into the same residue class. Frozen GS-U3 then applies
to each actual integer-mesh subcarrier, with disjoint outputs and every
cross-pair charged. The [complete proof](correlated-reuse.md) is elementary.

For the nonuniform family
\(B_p=\{j+p\lfloor j/3\rfloor:0\le j<p\}\), all residues differ and
the full cubic image has exactly \(N^2=p^2\) outputs. This provides an
explicit tiny-gap family outside the old whole-carrier width regime.

These are actual-image failures of stated families. They are not a
universal obstruction for arbitrary algebraic relations, denominators,
multiscale sets or real carriers.

## 10. Exact experiments

The new approved grid has 36 model records, 35 distinct carriers, 216
graphs and maximum \(N=60\). It includes multiscale rationals, reciprocals,
nonfaithful rational projections, correlated sum/difference sets,
unequal-scale unions, changing-scale completion and shared-anchor reverse
fibers. The duplicate model is explicitly retained and charged.

Research used 37,243 full-square polynomial evaluations, 349,851 charged
checks and 1.290217 CPU seconds, with zero errors. Five small prime-theorem
audits added 1,000 polynomial evaluations. All equality decisions were exact.
No random sampling, numerical tolerance, network call, or old grid rerun
was used.

The [complete table and finite limitations](experimental-summary.md), and
[portable results](../../../examples/2026-09-21-sublinear-cubic.json), record
input and inventory sizes, image, useful steps, edges, nonisolated mass,
component histograms, components per output, fragmented outputs, maximum
fibers, diameter, difference gaps and scalar/projection reuse. Raw files
retain every actual output fiber and graph component. The all-useful lists
are diagnostics only.

## 11. Full gain-versus-cost ledger

The [construction ledgers](construction-ledgers.md) charge exact scalar
lower and upper counts, both coordinate losses, projection multiplicities,
denominators, coefficient sizes, both real substitutions, degree, step
inventories, every exceptional pair and every unprescribed cross-pair.

The proved failed families have actual output exponent two in \(N\);
their net rate gap is zero. The many-to-one projection loses one factor
of order \(L\) in each input coordinate before the output is counted.
The exact residue descent sums every \(n_r^2\) square and the complete
cross-residue complement. No thinning gain is counted once when it should
be paid twice.

For the finite candidate families, the required asymptotic input, reuse,
inventory and exception exponents are **OPEN**. Unknown costs are not set
to zero. No arithmetic amplification is proposed or started.

## 12. Implication for T01

**T01 and CR-O1 remain OPEN.** This cycle rules out additional specific
ways to exploit nonfaithful projection and small scales, and sharpens the
necessary scale distribution of an inventory. It neither supplies a
positive full-support rate nor excludes every possible real carrier.

All major new proofs were independently audited internally. Finite tests,
artifact hashes and repository checks are separately documented in
[verification](verification.md); none proves the research target.
The separate T01 quadratic benchmark and the other three tracks remain
unchanged by this cycle.

The original historical regular-digital and rich-fiber proof files remain
unavailable under the recorded migration limitation. They were not
reconstructed, read, or recertified here, and are not dependencies of the
new arguments.

## 13. Claim ledger

All entries are T01 / sublinear cubic, polynomial fixed at the top,
2026-09-21 v1. Quantifiers and hypotheses are in the indicated statements.
Evidence is a complete symbolic proof except SC-X1 and SC-X2, which are
exact finite evidence. The audit record and artifact hashes are in
verification. No external result or novelty claim is imported.

| ID | Status / scope | Proof or evidence locator | Dependencies / gap |
|---|---|---|---|
| SC-R1 | PROVED; all finite prescribed label sets and scalar carriers | correlated-reuse, first section | Frozen inverse identity; construction missing |
| SC-R2 | PROVED; fixed affine matching of real fiber templates | correlated-reuse, second section | Polynomial coefficient comparison; nonlinear reuse outside |
| SC-R3 | PROVED; two distinct outputs and one nonzero step | correlated-reuse, third section | Cube difference and strict monotonicity |
| SC-D1 | PROVED; all index subsets with the stated prime and width | correlated-reuse, growing denominator theorem | Elementary congruence and width; other moduli outside |
| SC-D2 | PROVED; exact residue-square decomposition and full image bound | correlated-reuse, final theorem | SC-D1 plus frozen GS-U3 on actual subcarriers |
| SC-Q1 | PROVED; fixed quadratic field, all stated coefficient rectangles/scales | reuse-and-projections §1 | Two substitutions and integer product; small norm-scale can be inconclusive |
| SC-Q2 | PROVED; balanced boxes, rational scale square, critical lower bound | reuse-and-projections §2 | Whole-fiber bound on explicit positive pair mass |
| SC-Q3 | PROVED; all \(L\ge D\), exact three-parameter projection | reuse-and-projections §3 | Explicit multiplicity plus SC-Q1 |
| SC-Q4 | PROVED; any finite coefficient-field set, external scale square | reuse-and-projections §4 | Exact collision quotient; field-compatible scales outside |
| SC-U1 | PROVED; all finite real carriers/inventories | multistep-obstruction §1 | Exact fourth-coordinate marked incidence |
| SC-U2 | PROVED; all real carriers/inventories and \(t>0\) | multistep-obstruction §2 | Displacement identity plus frozen CR-U1 |
| SC-U3 | PROVED; separated width-\(O(N)\) carriers, stated step sizes | multistep-obstruction §3 | SC-U2; tiny inventories outside |
| SC-U4 | PROVED; geometric intersection lower bound | multistep-obstruction §4 | Completed square; not a return lower bound |
| SC-X1 / machine SL-X1 | EXPERIMENTAL; the 36-record, 216-graph grid | experimental-summary and portable JSON | Exact finite range; no asymptotic conclusion |
| SC-X2 | EXPERIMENTAL; five prime-denominator audit cases | verification and local prime-audit JSON | 1,000 exact pair evaluations; proof supplied separately |
| SC-UGAP | OPEN; stronger universal inventory threshold | multistep-obstruction §5 | Fourth-coordinate correlation not yet quantitatively exploited enough |
| CR-O1 | OPEN; commissioned sublinear-inventory coverage witness | §15 below | No witness |

## 14. Failure and scope ledger

| Attempt or inference | Disposition and exact limit |
|---|---|
| Quadratic coefficient projection automatically creates output compression | FAILED for Q1's regimes; actual image near quadratic |
| Three-parameter descriptions count as \(L^3\) distinct scalars | FAILED; Q3 gives exact \(N\asymp L^2\) and charges every projection fiber |
| Critical rational shrinking scale rescues balanced quadratic boxes | FAILED when \(h^2L\ge\kappa>0\); actual image at least a fixed multiple of \(N^2\) |
| Generic external scaling creates collisions | FAILED for Q4's field-carrier hypothesis; exact injectivity |
| A changing denominator automatically escapes arithmetic obstruction | FAILED in D1/D2's stated prime and width range |
| Arbitrarily many steps bounded below rescue separated nonlattice carriers | FAILED for U3's specified lower step scales; only a coverage obstruction |
| Special parabolas have subquadratically many curve intersections | FAILED by U4; legal marked incidences remain a separate question |
| Affine matching reuses entire distinct fiber-coordinate templates | FAILED by R2; nonlinear matching remains outside |
| Connected actual fibers imply almost-full useful coverage | FAILED inference; singleton fibers remain, as exact examples demonstrate |
| Many edges, frequent-step diagnostics, or all-useful inventories certify the target | FAILED inference; they do not supply the missing component tail |
| General correlated/multiscale/nonfaithful real construction | OPEN; no universal no-go follows from these scoped results |

## 15. Exactly one next proof obligation

**CR-O1 remains the sole next obligation — explicit sublinear-inventory
Cartesian coverage.** Construct arbitrarily large finite real \(A_N\)
with \(|A_N|=N\), and explicit nonzero inventories \(S_N\), with fixed
\[
1/6\le\theta<1,\qquad \varepsilon,\delta>0,\qquad |S_N|\le N^\theta,
\]
such that all but \(O(N^{2-\delta})\) vertices of \(A_N^2\) lie in
components of size at least \(N^\varepsilon\).

The construction must prove actual scalar membership and reuse, input
lower and upper counts, inventory complexity, finite-path connectivity
and the full exception bound. It must escape the precisely stated old
and new obstructions; falling outside their hypotheses is not evidence
that the obligation holds. Equation (1) then supplies the fixed-polynomial
power saving. This is the one adopted next obligation, not authorization
for further unbounded search.
