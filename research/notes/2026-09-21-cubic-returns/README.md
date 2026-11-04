# Cartesian returns and long output-preserving orbits

**T01 · 2026-09-21 · offline research report · version 1**

Fixed target: \(P(x,y)=(x-y)^3+x+y\), with the same finite real set
in both coordinates and every ordered pair counted.

## 1. Verdict

**PROVED: the fixed-step Cartesian-return mechanism has vanishing density.**
For every nonempty finite \(A\subset\mathbb R\), \(N=|A|\), and every
real \(\tau\ne0\),

\[
\boxed{E_\tau(A):=|\{(x,y)\in A^2:T_\tau(x,y)\in A^2\}|
       \le5N^{11/6}.}
\]

The constant is uniform even if the nonzero step is chosen after seeing
\(A\), or tends to zero with \(N\). In particular,

\[
\boxed{R_1(N)\le5N^{-1/6}\longrightarrow0.}
\]

This is Outcome B / Success 2 of the commissioned task. The proof is
self-contained apart from elementary planar Euler counting; it derives
the needed graph-crossing estimate and verifies all geometric degeneracies.
It has been independently checked internally in this task. No external
review or novelty claim is made.

Only \(O(N^{11/6})\) pairs can lie in **any nontrivial fixed-step path**.
Thus the proposed coverage of almost all of \(A^2\) by long \(T_1\)
chains is **FAILED**, for every finite real carrier, not just the families
tested here. A bounded list of nonzero steps also fails. Individual chains
with \(\Theta(N)\) pairs do exist; their existence does not give enough
coverage.

**The original cubic power-saving target remains OPEN.** Different return
paths can have the same output. The theorem does not give a lower bound
for the actual cubic image, and does not exclude a growing inventory of
steps or other ways of counting coincidences between paths.

Full proofs: [fibers and chains](fibers-and-chains.md),
[baseline families](baselines.md), and [the universal bound](universal-bounds.md).
The [construction ledgers](construction-ledgers.md) charge scalar counts,
projection multiplicities, and all uncovered pairs.

## 2. What the symmetry does

**Meaning.** \(T_1\) increases \(x-y\) by one and adjusts \(x+y\)
exactly enough to keep the cubic output unchanged. Its quadratic formula
looks more complicated than its action is.

**Statement and proof.** Set \(u=x-y\), \(z=P(x,y)\). Then

\[
x=\frac{z-u^3+u}{2},\qquad y=\frac{z-u^3-u}{2}.
\]

These formulas invert \((x,y)\mapsto(u,z)\) on all of \(\mathbb R^2\).
Consequently the motion is simply

\[
\boxed{T_\tau:(u,z)\mapsto(u+\tau,z).}
\]

Returning to the original coordinates, with
\(H_\tau(u)=(u+\tau)^3-u^3\), gives

\[
T_\tau(x,y)=\left(x+\frac{\tau-H_\tau(u)}2,
                     y-\frac{\tau+H_\tau(u)}2\right).
\]

This proves output preservation, \(T_\sigma T_\tau=T_{\sigma+\tau}\),
and the inverse \(T_{-\tau}\). Taking \(\tau=k\) gives every integer
iterate explicitly. Simultaneous returns for \(k=0,\ldots,L\) mean that
both displayed cubic coordinate sequences belong to \(A\) at each of
\(u,u+1,\ldots,u+L\).

**Scope.** These identities rederive the frozen pair symmetry. A finite
Cartesian square cannot be invariant under a nonzero step: its finite
difference set cannot contain all translates of any one difference.
The new question was how many partial returns are possible.

## 3. Exact fibers and return formulas

**Meaning.** A cubic fiber is a set of allowed difference coordinates.
The return problem asks how many adjacent positions in those sets survive
the requirement that both coordinates belong to the same scalar set.

**Statement.** Define

\[
U_A(z)=\left\{u:\frac{z-u^3+u}{2}\in A,
                    \frac{z-u^3-u}{2}\in A\right\}.
\]

Then

\[
\sum_z|U_A(z)|=N^2,\qquad
|P(A,A)|=|\{z:U_A(z)\ne\varnothing\}|,
\]

\[
\boxed{E_1(A)=\sum_z|U_A(z)\cap(U_A(z)-1)|.}
\tag{3.1}
\]

Equivalently let \(A_u=A\cap(A-u)\) and
\(c(u)=(3u^2+3u+2)/2\). Then

\[
T_1(y+u,y)=\left(y-\frac{3u^2+u}{2},y-c(u)\right),
\]

\[
\boxed{E_1(A)=\sum_{u\in A-A}|A_u\cap(A_{u+1}+c(u))|.}
\tag{3.2}
\]

**Proof.** The inverse coordinates identify each pair uniquely by
\((u,z)\). The motion replaces \(u\) by \(u+1\), proving (3.1).
A pair of difference \(u\) is \((y+u,y)\), \(y\in A_u\). Its new
second coordinate is \(y-c(u)\) and its new difference is \(u+1\),
which proves (3.2). Each source pair is counted once.

**Scope.** Both formulas count exact equalities and actual scalar membership.
Large formal slices prescribed separately need not arise from one set.

## 4. Baselines and the lower bound

**Meaning.** Dense real lattices allow the quadratic translations to align,
but the translations grow quadratically with the difference. Only about
\(\sqrt N\) differences remain useful inside an interval of \(N\) points.

The following are **PROVED** in [baselines.md](baselines.md), except the
last row, which uses CR-P5 and CR-U1 in the other companions. Precise step,
polynomial, and uniformity hypotheses are stated in those proofs.

| Family | Return count | Reason and scope |
|---|---|---|
| \(\{0,\ldots,N-1\}\) and its translates | \(\frac43\sqrt{2/3}\,N^{3/2}+O(N)\) | All integer shifts align; useful differences have size \(O(\sqrt N)\) |
| \(\{0,1/3,\ldots,(N-1)/3\}\) | \(\frac{4\sqrt2}{3}N^{3/2}+O(N)\) | Every transformed coordinate stays on the third-integer lattice when within its endpoints |
| Fixed positive-step AP, including symmetric AP | Zero unless \(1/h\in\mathbb Z\); otherwise \(\Theta_h(N^{3/2})\) | The difference set must admit a shift by one; reciprocal steps admit enough integral-difference slices |
| A bounded number of AP blocks | \(O(N^{3/2})\) for steps in a fixed interval \(0<h_-\le h\le h_+<\infty\) | Each quadratic translation lands in one of boundedly many difference intervals of width \(O(N)\), even when block centers separate |
| \(\{0^2,1^2,\ldots,(N-1)^2\}\), \(N\ge2\) | Exactly 2 | Only two returns involving 0 and 1 survive |
| \(\{1^2,\ldots,N^2\}\) | Zero | The required downward displacement exceeds the available range at each nonzero difference |
| \(\{c(0),\ldots,c(N-1)\}\) | Zero | All entries are 1 modulo 3, so both \(u\) and \(u+1\) cannot be differences |
| Fixed polynomial sequence of degree 2 | \(O(N\log N)\) | Quadratic spacing leaves few close index pairs |
| Fixed polynomial sequence of degree at least 3 | \(O(N)\) | Faster spacing leaves only linearly many possible source pairs |
| Two-coordinate completion of selected cubic orbits | At least its prescribed edges; universally at most \(5N^{11/6}\) | Long chains are easy, but scalar reuse and full-square coverage are insufficient |

For the integer interval, an exact expression is

\[
E_1=2\sum_{v\ge0}\max\left\{N-1-\frac{3v^2+5v}{2},0\right\}.
\]

The two contributing differences are \(u=v\) and \(u=-v-1\);
the summand is their common number of anchors. This gives the stated
leading term by summing a quadratic up to \(v\sim\sqrt{2N/3}\).

For the third-integer interval, writing \(u=d/3\) gives an integral
translated index \(3c(u)=(d^2+3d+6)/2\). The exact count is

\[
E_1=2(N-2)_+
 +2\sum_{v\ge0}\left(N-3-\frac{v^2+5v}{2}\right)_+,
\]

where \(t_+=\max(t,0)\). Here the paired differences have indices
\(d=v,-v-3\); the two middle indices \(-1,-2\) supply the first term.
Summing to \(v\sim\sqrt{2N}\) proves the stronger lower bound.

Thus the **best lower and upper bounds proved in this cycle** are

\[
\boxed{\frac{4\sqrt2}{3}N^{-1/2}+O(N^{-1})
       \le R_1(N)\le\min\{1,5N^{-1/6}\}.}
\tag{4.1}
\]

The lower-side notation means the explicit family has the displayed
asymptotic value; equivalently it is a lower bound with error at least
\(-C/N\). The optimal exponent between these bounds remains OPEN.
No claim is made that these are the best bounds in the literature.

## 5. Why the universal upper bound holds

**Meaning.** A returning pair must have its first new coordinate in \(A\).
That requirement alone is rare. After normalization it asks a quadratic
function of two elements of \(A\) to land in a set of only \(N\) values.

**Exact statement.** If
\(F(x,y)=(x-y)^2+ax+by\) with \(a+b\ne0\), and \(|C|=|A|=N\), then

\[
|\{(x,y)\in A^2:F(x,y)\in C\}|\le5N^{11/6}.
\tag{5.1}
\]

**Proof outline; complete proof in [universal-bounds.md, §§2–5](universal-bounds.md).**
For a return with first new coordinate \(x'\), take

\[
a=\tau-\frac2{3\tau},\quad b=-\tau,\quad
F(x,y)=-\frac2{3\tau}x'+\frac{1-\tau^2}{3}.
\]

Thus \(a+b\ne0\), and \(x'\in A\) forces \(F\) into an injective
affine copy \(C\) of \(A\).

To prove (5.1), count equal values of \(F\) at two pairs. After excluding
at most \(2N^2\) solutions with \(y_1=y_2\), each fixed
\((y_1,y_2)\) gives a smooth hyperbola

\[
(X_1-y_1+a/2)^2-(X_2-y_2+a/2)^2
=-(a+b)(y_1-y_2).
\]

There are at most \(N^2\) such curves and \(N^2\) points
\((X_1,X_2)\in A^2\). Distinct curves meet at most twice; two distinct
points lie on at most two curves, including the checked diagonal cases.
Connecting consecutive marked points on each curve produces a graph.
Euler counting and random vertex sampling show that a graph with many edges
must have many crossings. The curves allow only \(O(N^4)\) crossings,
which bounds their total incidences by \(O(N^{8/3})\), explicitly giving

\[
\sum_z |F^{-1}(z)\cap A^2|^2\le25N^{8/3}.
\]

Cauchy–Schwarz over the \(N\) target values in \(C\) now proves (5.1).
Discarding second-coordinate membership only enlarged the set being counted.

**Scope.** This use of an equal-value count bounds the number of pairs
landing in a specified small set. It does not infer an image upper bound
from collision energy. No deep external incidence theorem is assumed.
Uniformity follows from intersection counts, which do not depend on the
numerical sizes of \(a,b,\tau\).

## 6. Paths, orbit lengths, and coverage

**Meaning.** Return chains supply an image certificate only through their
components. Output coincidences between different components remain a
separate issue.

**Statement and proof.** On \(A^2\), direct edges \(v\to T_1v\) when
the endpoint belongs to \(A^2\). Invertibility gives in- and out-degree
at most one; the strictly increasing difference rules out cycles. The
components are paths. If \(n_\ell\) counts components of \(\ell\) vertices,

\[
\sum\ell n_\ell=N^2,\quad
E_1=\sum(\ell-1)n_\ell,\quad
\boxed{C_A=N^2-E_1},\qquad |P(A,A)|\le C_A.
\]

A path of size \(\ell\) contributes forward lengths
\(0,1,\ldots,\ell-1\), so their average over all ordered pairs is

\[
\frac1{2N^2}\sum_\ell\ell(\ell-1)n_\ell.
\]

Also \(y_z(u+1)-y_z(u)=-c(u)<0\), so every path has at most \(N\)
vertices. A single planted cubic fiber attains at least \(N/2\) consecutive
vertices, by CR-P5. For reciprocal-step APs the maximum is
\(\Theta(N^{1/3})\); bounded AP unions have the same upper order.

If all but \(B\) pairs lie in paths of size at least \(K\), their
components number at most \(N^2/K\). The exceptional components number
at most \(B\). Hence

\[
\boxed{|P(A,A)|\le N^2/K+B.}
\tag{6.1}
\]

With \(K\ge N^\varepsilon\), \(B=O(N^{2-\delta})\), this is
\(O(N^{2-\min(\varepsilon,\delta)})\), including every exceptional pair.
Any smaller fixed exponent absorbs the constant for sufficiently large \(N\).

However, a path of size \(\ell\ge2\) has at least \(\ell/2\) edges.
The universal theorem therefore bounds the total mass of nontrivial paths
by \(2E_1\le10N^{11/6}=o(N^2)\). The coverage hypothesis of (6.1)
is impossible for this mechanism. Average component size tends to one;
average forward length is a different statistic, for which we prove only
the general upper bound \(\frac52N^{5/6}\).

**Scope.** This is stronger than ruling out positive one-step density.
It still permits long sparse chains and multiple components in one fiber.
For example, the computed \(c(j)\) set has zero \(T_1\) edges but has
an actual cubic collision. Therefore component counts cannot be read as
actual-image lower bounds.

## 7. Adapted carriers and coordinate reuse

**Meaning.** Prescribing an entire orbit solves its pair equations, but can
spend two new scalar coordinates on nearly every prescribed pair.

**Statement and proof.** For \(j=1,\ldots,L\), take both
\(x_z(j)=(z-j^3+j)/2\) and \(y_z(j)=(z-j^3-j)/2\).
They interleave strictly:

\[
x_z(j)>y_z(j)>x_z(j+1).
\]

Thus \(N=2L\) exactly, with a chain of \(L\) pairs occupying only
\(L/N^2=1/(2N)\) of the square. For \(M\) separated outputs the
exact counts are \(N=2ML\), prescribed pairs \(ML=N/2\), and prescribed
edges \(M(L-1)\). The remaining \(N^2-N/2\) pairs cannot be omitted.
The [full ledger](construction-ledgers.md#l2-one-or-many-explicitly-planted-cubic-fibers)
accounts for the separation, integer heights, two coordinate branches,
and absence of projection multiplicity.

Close output translations, quadratic output choices, and cubic output
choices were also tested exactly; their actual scalar reuse is recorded
in the data. No uniform whole-square gain follows. More generally, the
universal upper bound applies to the actual scalar set produced by any
polynomial/rational parametrization, two-parameter construction,
difference-slice prescription, or recursive completion. None can produce
positive-density returns for one common nonzero step.

**Scope.** These broad conclusions close the commissioned fixed-step
carrier search without requiring an exhaustive classification of carriers.
They do not close full-image compression through different steps.

## 8. Several steps and the cost of a larger inventory

**Meaning.** A different step does not improve the universal bound. Many
different steps might collectively connect pairs, but their number is a
real cost.

**Statement and proof.** If \(S\) contains \(M\) nonzero real steps,
even chosen adaptively from \(A\), the union return graph has at most
\(5MN^{11/6}\) edges, by summing the single-step bound. It has at most
\(10MN^{11/6}\) nonisolated vertices and at least
\(N^2-5MN^{11/6}\) components. Thus \(M=o(N^{1/6})\) still leaves
almost all pairs isolated. To obtain \(O(N^{2-c})\) components for a
fixed \(c>0\), it is necessary that

\[
M\ge(1/5-o(1))N^{1/6}.
\]

**Scope.** This is necessary, not sufficient. A growing step inventory
is not a construction, and formal step labels are not distinct connected
pairs. The bound does not cover useful aggregation over an unrestricted
number of pair-dependent shifts.

## 9. Exact computational evidence

**EXPERIMENTAL — exact rational arithmetic, finite declared grid only.**
The run evaluated 97 structured candidates and 33 candidates in two rounds
of greedy single-point deletion. Every candidate used the whole Cartesian
square. The direct, fiber, and difference-slice return counts agreed, and
the path decomposition covered every pair.

| Model | \(N\) | \(E_1\) | Components | Longest path | Full image | Largest actual fiber |
|---|---:|---:|---:|---:|---:|---:|
| Integer AP | 16 | 60 | 196 | 5 | 196 | 5 |
| Integer AP | 128 | 1,494 | 14,890 | 10 | 14,890 | 10 |
| Step \(1/3\) AP | 8 | 26 | 38 | 3 | 38 | 3 |
| Step \(1/3\) AP | 128 | 2,478 | 13,906 | 7 | 13,906 | 7 |
| Squares \(j^2\), \(0\le j<64\) | 64 | 2 | 4,094 | 2 | 4,093 | 2 |
| Shift sequence \(c(j)\), \(0\le j<64\) | 64 | 0 | 4,096 | 1 | 4,095 | 2 |
| Cubes \(j^3\), \(0\le j<64\) | 64 | 2 | 4,094 | 2 | 4,094 | 2 |
| \((j^3-j)/2\), \(0\le j<64\) | 63 | 0 | 3,969 | 1 | 3,969 | 1 |
| One planted output, \(-32\le u\le32\) | 127 | 66 | 16,063 | 65 | 16,043 | 65 |
| Four planted outputs, \(-8\le u\le8\) | 108 | 360 | 11,304 | 17 | 11,064 | 17 |

Path sizes count vertices. The one-output example has distribution
\(n_1=16060,n_2=2,n_{65}=1\), mean forward length \(2082/16129\),
and mean actual fiber size \(16129/16043\). Its long path covers only
\(65/16129\) of all pairs. For four planted outputs, the four paths
of size 17 cover \(68/11664\); additional short paths are included in
the edge and image counts. The greedy deletions selected interval endpoints,
without finding an improved structure.

The [complete summary](../../../examples/2026-09-21-cubic-returns.json)
records every candidate's exact density, full path-size distribution,
maximum and mean forward lengths, mass above several length thresholds,
full image, maximum and mean actual fiber, and scalar-reuse count where
applicable. Full fibers, paths, input sets, and slice anchors are retained
in the ignored local run directory linked in [verification.md](verification.md).

The research run used **823,227 charged pair checks**, including three
passes per candidate, **274,409 actual cubic evaluations**, and
**9.047958 CPU seconds**. Largest actual input: 129. No random sampling,
floating-point equality, old three-branch grid rerun, or arithmetic
amplification occurred. The proof of the universal bound is independent
of these finite observations.

## 10. Compatibility and the finite-field origin

The [16 September continuation](../2026-09-16-three-branch-continuation/README.md)
and [21 September freeze](../2026-09-21-three-branch-freeze/Three_Branch_Continuation_Freeze.md)
remain unchanged. Their finite 22-output gadget, literal-iteration failure,
separated-copy formula, and bounded-displacement obstruction retain their
original scopes. The bounded-displacement result concerned constant
translations on selected slices; this cycle controls a nonlinear global
map through a new argument. Neither result substitutes for the other.

The frozen question whether \(R_1\) vanishes is now answered by CR-U1.
That supersession applies to the open-return question, not to the original
fixed-polynomial target. The separate quadratic \(P_0\) branch and T02–T04
are unchanged. In particular no minus-sign cubic result has been imported.

Over \(\mathbb F_3\), \(P(x,y)=2x=-x\). The same symbolic motion, for
\(\tau\in\mathbb F_3\), reduces to \((x,y)\mapsto(x,y-\tau)\), since
\(H_\tau=\tau\). Over the reals, the quadratic adjustment survives and
Cartesian returns have the obstruction above. The planar proof uses real
curves and cannot be transferred to characteristic three; its normalization
even divides by 3. No useful real carrier with positive asymptotic return
density retains the modular collapse. The finite-field motivation remains
historical context, without a forced arithmetic amplification phase.

The two named complete historical digital/rich-fiber checkpoints are still
unavailable as original local bytes (MC-06). Their reported results were not
recertified or used as proof dependencies. No external literature or novelty
search was performed under the offline instruction.

## 11. Claim ledger

All entries below are T01 / cubic Cartesian returns, fixed plus-sign cubic,
2026-09-21 v1. Unless marked EXPERIMENTAL, evidence is the identified exact
argument. Internal independent audit is recorded in [verification.md](verification.md).
These are not external peer-review claims.

| ID | Status, quantifiers, and evidence locator | Dependencies and retained gap |
|---|---|---|
| CR-P1 | PROVED; all real pairs and steps; fibers-and-chains §1 | Inverse coordinate substitution; rederives frozen symmetry |
| CR-P2 | PROVED; all finite real \(A\); fibers-and-chains §2 | CR-P1; exact fibers and both return formulas |
| CR-P3 | PROVED; all nonempty finite \(A\); fibers-and-chains §3 | CR-P1/P2; graph components may share an output |
| CR-P4 | PROVED implication and FAILED witness; all fixed \(\varepsilon,\delta>0\); fibers-and-chains §4 | CR-P3/U1; no actual-image lower bound |
| CR-P5 | PROVED; every integer \(M,L\ge1\); fibers-and-chains §5 | Explicit interleaving/separation; incidental cubic image OPEN |
| CR-P6 | PROVED; every finite adaptive nonzero step list; fibers-and-chains §6 | CR-U1 plus spanning-forest counting; large lists unresolved |
| CR-U1 | PROVED; all finite \(A\), all \(\tau\ne0\), uniform \(5N^{11/6}\); universal-bounds §§2–5 | CR-U2/U3; optimal exponent OPEN |
| CR-U2 | PROVED; all \(a+b\ne0\), equal-value count \(25N^{8/3}\); universal-bounds §§3–4 | Explicitly proved graph lemma; degeneracy checked |
| CR-U3 | PROVED; every \(N\)-point auxiliary target; universal-bounds §5 | Cauchy–Schwarz and CR-U2 |
| CR-U4/U5 | PROVED; single-step path and finite-inventory bounds; universal-bounds §§6–7 | CR-U1 and elementary graph counts |
| CR-B | PROVED family bounds listed in §4; baselines.md | Fixed step/polynomial hypotheses in that companion; no universal image claim |
| CR-X1 | EXPERIMENTAL; all 130 declared finite candidates; summary JSON and verification.md | Exact whole-square enumeration; no asymptotic inference |
| CR-O1 | OPEN; growing-step coverage witness, §13 below | Necessary inventory cost proved, sufficient carrier missing |

## 12. Scope and failure ledger

| Proposed conclusion or mechanism | Disposition | Exact limitation |
|---|---|---|
| Positive limsup of \(R_1\) | FAILED; vanishing PROVED | Holds for all finite real carriers |
| Another single nonzero step fixes the problem | FAILED | Bound uniform in the step, including adaptive choices |
| Almost-all pair coverage by long fixed-step chains | FAILED | Even nontrivial-path mass is \(o(N^2)\) |
| A bounded or \(o(N^{1/6})\)-size step inventory suffices | FAILED as a coverage/component certificate | Sum of all edge budgets is \(o(N^2)\) |
| Long paths cannot exist | False; CR-P5 gives linear-size paths | Sparse planted paths do not compress the whole square |
| Large component count proves large actual image | Invalid inference | Different components can share an output |
| Fixed polynomial sequences or bounded AP unions supply positive density | FAILED in the stated baseline scopes | General universal theorem also covers their mutations |
| A growing inventory or cross-path coincidences can compress the image | OPEN | No positive same-set witness or full-image upper bound supplied |
| Original T01 power saving | OPEN | No claim of impossibility or success for the fixed cubic target |
| Arithmetic amplification | Deferred, not attempted | No positive asymptotic Cartesian-return mechanism was obtained |

## 13. Exactly one next proof obligation

**CR-O1 — OPEN: a growing-step Cartesian coverage witness.** Construct
explicit arbitrarily large finite real sets \(A_N\), finite lists
\(S_N\subset\mathbb R\setminus\{0\}\), and fixed
\(\varepsilon,\delta>0\), such that all but \(O(N^{2-\delta})\) of
the \(N^2\) ordered pairs lie in connected components of size at least
\(N^\varepsilon\) in the graph using returns under the steps in \(S_N\).

Prove the actual scalar input count, membership of every claimed endpoint,
coordinate reuse, and the size of the step inventory. The necessary
\(\Omega(N^{1/6})\) inventory cost must be charged explicitly. Applying
the component argument of (6.1) would then give a full-image power saving,
including all exceptional pairs. A list of formal shifts or a selected
collection of rich fibers is not a witness.

This is the sole next obligation for this cycle. It has not been attempted
as a new search and does not authorize arithmetic amplification.
