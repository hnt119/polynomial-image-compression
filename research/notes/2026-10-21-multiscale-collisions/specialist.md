# Actual cubic fibers must branch at many scales

T01 | 21 October 2026 | offline, exact multiscale necessity.

The polynomial throughout is \(P(x,y)=(x-y)^3+x+y\).
The result below concerns every ordered pair of one actual finite real
set \(A\), not selected collisions, formal addresses, or quantized outputs.
It supplies a necessary persistence pattern for a small full image.
It is neither a construction nor a sufficient support upper bound.

## MC-S1 — global fiber graph and eight-child bound

**PROVED.** For every real \(z\), the level set \(P(x,y)=z\) is the graph
of a globally defined smooth function \(x=f_z(y)\), with
\[
f_z'(y)=
\frac{3(f_z(y)-y)^2-1}{3(f_z(y)-y)^2+1},
\qquad |f_z'(y)|\le1.
\tag{1}
\]
In particular, every fiber graph is 1-Lipschitz.

For each fixed \(y\), the function \(x\mapsto P(x,y)\) has derivative
\(1+3(x-y)^2\ge1\) and tends to the two different infinities at the
ends of the real line. It therefore has a unique inverse value \(f_z(y)\).
The implicit function theorem and differentiation give (1); the
denominator never vanishes. The derivative bound and the mean value
theorem give the global Lipschitz assertion.

Choose a half-open bounded interval \(I_0\) containing \(A\), and split
each interval into four equal half-open children at every level.
Let \(\mathcal I_j\) be the resulting level-\(j\) partition of \(I_0\)
and let \(\mathcal C_j=\{I\times J:I,J\in\mathcal I_j\}\).
This uses two dyadic levels per refinement. It changes only the
partition, not the scalar inputs or the polynomial.

For a fixed exact output \(z\) and a parent square \(I\times J\),
its actual fiber points occupy at most **eight** of the sixteen child
squares. To prove this, fix one of the four child intervals of \(J\).
The finitely many occupied \(y\)-values in that half-open child have
diameter strictly less than its length. Their \(f_z(y)\)-values have
at most that diameter. Hence they can meet at most two of the equal
length \(x\)-child intervals. Three such intervals would require
two occupied \(x\)-values separated by more than one child length.
There are four \(y\)-children, giving at most eight occupied squares.
Points outside the parent can only reduce this number.

The strict finite-diameter observation handles grid-boundary points.
No generic-position hypothesis or random grid shift is used.

## MC-S2 — a near-full pair mass must have many actual branch events

**Definitions.** Let \(N=|A|\ge2\), let
\[
Z=P(A,A),\qquad s=|Z|,\qquad
F_z=\{(x,y)\in A^2:P(x,y)=z\}.
\]
Choose any finite terminal level \(L\) whose interval length is smaller
than the minimum distance between distinct elements of \(A\).
Each occupied terminal square then contains exactly one ordered pair.
Such an \(L\) exists for every finite set; no bound on \(L\) in terms
of \(N\) is assumed.

For a pair \(\xi=(x,y)\in F_z\), define \(B_L(\xi)\) to be the number
of levels \(0\le j<L\) at which the parent square containing \(\xi\)
has at least two child squares occupied by \(F_z\).
These are branches of the **same exact output**, not branches of the
input set alone and not nearby output values.

**PROVED — exact finite bound.** For every integer \(b\ge0\),
\[
\boxed{\#\{\xi\in A^2:B_L(\xi)\le b\}\le s\,8^b.}
\tag{2}
\]

**Proof.** Fix one \(z\). Its occupied squares form a rooted finite tree.
Every internal vertex has at most eight children by MC-S1.
Suppress all vertices with only one child. The remaining tree has the
same leaves, one for each pair in \(F_z\), and the depth of a leaf is
exactly its number \(B_L\) of genuine branch events.

Assign distinct symbols from an eight-symbol alphabet to the children
of each branching vertex. The words coding the leaves are prefix-free.
For all leaves of depth at most \(b\), extend their words arbitrarily to
length \(b\). The sets of extensions from different leaves are disjoint.
There are only \(8^b\) words of length \(b\), so there are at most
\(8^b\) such leaves. A singleton fiber gives the empty word and also
satisfies this argument. Summing over the \(s\) actual outputs proves (2).
This is the elementary finite prefix-tree counting argument; no
external entropy theorem is used.

**PROVED — necessary power-saving pattern.** Suppose
\[
s\le N^{2-c},\qquad c>0.
\]
For any fixed \(0<\gamma<c\), put
\[
b_N=\left\lfloor(c-\gamma)\log_8 N\right\rfloor.
\]
Then
\[
\boxed{\#\{\xi:B_L(\xi)\le b_N\}\le N^{2-\gamma}.}
\tag{3}
\]
Indeed \(8^{b_N}\le N^{c-\gamma}\), so (3) follows from (2).
Thus at least \(N^2-N^{2-\gamma}\) actual ordered pairs must encounter
more than \(b_N\) distinct genuine branching levels of their own
exact output fiber.

The statement is stronger than exhibiting a few rich fibers or a large
collision energy: it places a condition on all but a power-saving
exceptional number of pairs. It is still only necessary. Many branch
events on selected pairs do not imply a small full image.

**Scale-location limitation.** The result does not control the numerical
positions of the branching levels, the gaps between them, or the terminal
depth \(L\). Arbitrarily long chains with one occupied child are suppressed
in the proof. No uniform distribution over scales, Frostman estimate,
fractal structure, or concentration conclusion follows. The constants
and the conclusion apply to the chosen nested partition; they do not
permit rescaling \(A\) while treating \(P\) as invariant.

## MC-S3 — local mass, output overlap, and a block of scales

### Exact local fiber capacity

For \(C=I\times J\), put \(n_I=|A\cap I|\) and \(n_J=|A\cap J|\).
For every exact output,
\[
\boxed{|F_z\cap C|\le \operatorname{cap}(C)
 :=\min(n_J,3n_I).}
\tag{4}
\]
There is at most one \(x\) for each fixed \(y\), by MC-S1. Conversely,
for fixed \(x,z\), the equation \(P(x,y)=z\) is a nonzero cubic in \(y\),
with leading coefficient \(-1\), so it has at most three distinct real
roots. These two facts prove (4), including all multiple-root cases.

### Local branching transfer

Fix levels \(j\) and \(j+k\le L\). For each occupied level-\(j\) square
\(C\), let
\[
S_C=P\bigl((A\cap I),(A\cap J)\bigr),\qquad
M(C)=\max_{\substack{D\in\mathcal C_{j+k}\\D\subset C}}
       \operatorname{cap}(D).
\]
Empty descendants have capacity zero. For a pair \(\xi\), let
\(B_{j,k}(\xi)\) count its actual same-output branch events at levels
\(j,\ldots,j+k-1\).

**PROVED — exact scale-transfer inequality.** For every integer \(b\ge0\),
\[
\boxed{\#\{\xi\in A^2:B_{j,k}(\xi)\le b\}
 \le 8^b\sum_{C\in\mathcal C_j}M(C)|S_C|.}
\tag{5}
\]
For each \(C,z\), the prefix-tree argument bounds by \(8^b\) the
number of occupied terminal squares at level \(j+k\) with at most
\(b\) branching ancestors in this block. These terminal squares may
contain several pairs, but each contains at most \(M(C)\) pairs
of \(F_z\), by (4). Sum first over \(z\in S_C\), then over \(C\).
Every actual ordered pair belongs to exactly one coarse square, so
there is no pair overcount.

To display explicitly the two competing costs, define
\[
\Omega_{j,k}
 =\frac1s\sum_{C\in\mathcal C_j}M(C)|S_C|
 =\frac1s\sum_{z\in Z}\sum_{\substack{C\in\mathcal C_j\\z\in S_C}}M(C).
\tag{6}
\]
The inner sum counts the occurrence of the **same actual output**
in different coarse cells, weighted by their local terminal capacities.
Thus (6) includes local scalar-cluster mass and cross-cell actual-output
overlap, rather than treating different cells' image sets as disjoint.
If \(s\le N^2/R\), (5) gives
\[
\frac{\#\{\xi:B_{j,k}(\xi)>b\}}{N^2}
 \ge \max\left\{0,\,1-\frac{8^b\Omega_{j,k}}R\right\}.
\tag{7}
\]
For a simpler, weaker bound let \(M_*=\max_C M(C)\) and
\(\overline K_j=s^{-1}\sum_C|S_C|\). Then
\(\Omega_{j,k}\le M_*\overline K_j\).
At the initial square and singleton terminal level, \(\Omega_{0,L}=1\),
recovering (2).

Equation (7) is a quantitative alternative: if a proposed small image
has neither large local terminal capacity nor enough existing cross-cell
output reuse at the start of a scale block, near-full pair mass must
branch within that block. It does not prescribe which alternative holds
for arbitrary \(A\).

### Rich mass and coarse-cell reuse

For completeness, the exact all-output rich-mass implication is
\[
\#\{\xi\in A^2:|F_{P(\xi)}|<T\}\le T s
\quad(T>0).
\tag{8}
\]
It follows by summing the actual sizes of the fibers below \(T\).
Under \(s\le N^2/R\), all but at most \(\eta N^2\) pairs belong to
fibers of size at least \(\eta R\), for any \(0<\eta<1\).
If \(M_j=\max_{C\in\mathcal C_j}\operatorname{cap}(C)\), each such
fiber occupies at least
\[
\left\lceil\eta R/M_j\right\rceil
\tag{9}
\]
coarse cells. This follows from (4); it is a count of exact repeated
output incidences. Equations (5)–(9) specify what local mass and
cross-cell reuse must supply without replacing actual fibers by a
selected collision graph.

## MC-S4 — source availability and the projection-exponent test

**MISSING from the searched local source collection.** The requested
Raz–Zahl source identified as arXiv:2108.07311, its Theorem 1.18, and
the cited energy-dispersion statement were not located. The bounded
offline search covered project notes and local-only sources, including
ignored files, plus the local attachment store. It checked filenames
(including available PDFs) and the Markdown, text, and JSON content
for the authors, arXiv identifier, theorem number, and dispersion terms.
This is a source-availability statement, not a claim about the entire
computer or about the truth of those results. No online substitute was
fetched. Their exact hypotheses, constants, and conclusions are not
asserted or used here.

The locally available
[projection and entropy note](../2026-10-11-transfer-division-entropy/C_entropy.md)
was read. Its C-NORM, C-BRIDGE, and C-ENT distinguish exact support
from covering number, charge local strip and exceptional-pair costs,
and show why a projection lower bound is not a support upper bound.
Those are existing mechanisms, not new results of this note.
In particular,
\[
P(t+\lambda x,t+\lambda y)
=2t+\lambda\bigl[x+y+\lambda^2(x-y)^3\bigr]
\]
shows that input normalization changes the cubic coefficient.

An exponent check that any subsequently supplied theorem must pass is
elementary. If it actually applies and yields \(s\ge c_0N^\beta\),
with fixed \(c_0>0\), it contradicts \(s\le N^{2-c}\) asymptotically
only when \(\beta>2-c\), or with additional compatible constant
information at equality. A merely superlinear lower bound
\(N^{1+\varepsilon}\) does not do this when
\(1+\varepsilon<2-c\). It therefore does not by itself force a
concentration alternative for the proposed power saving.

For a covering-number theorem, one must also verify its scale,
normalization, domain, derivative or nondegeneracy bounds, actual
non-concentration hypotheses, and every exceptional contribution.
The inequality \(N_\delta(Z)\le |Z|\) lets an applicable covering
lower bound imply an exact-cardinality lower bound. A covering upper
bound or small quantized entropy does not imply a small exact support
without a bound on distinct exact outputs per output cell. No such
missing hypothesis is silently inferred here.

The faithful coefficient-recovery argument
[GS-P4, §4](../2026-09-21-growing-step-cubic/structure-and-reuse.md)
was also read. It already proves that the specified separated
coefficient boxes have singleton fibers whenever higher input digits
differ, with remaining collisions confined to individual slices.
Any related two-level coefficient comparison belongs to that imported
mechanism; it is not claimed as a new multiscale construction here.
Its hypotheses do not cover arbitrary nonfaithful or correlated
projections.

## Scope, dependencies, and provenance

MC-S1–MC-S3 are complete elementary arguments for finite real \(A\)
and the fixed plus-sign cubic. Their assumptions, quantifiers,
partitions, capacities, and exception counts are explicit above.
MC-S4 is a source-availability and applicability ledger, not an
imported projection theorem or a new impossibility theorem.

The frozen [TJ-C6 report](../2026-10-21-tj-o1-freeze/README.md)
was read only to preserve its exact scope. No frame equation or
torsion argument is used, and no closed frame task is reopened.
No external novelty assessment is made.

This specialist performed no candidate enumeration, exact-field
scout, polynomial-evaluation run, or mathematical executable.
The lead's six-set finite diagnostic, if performed, is separate
evidence and cannot establish an asymptotic conclusion. No numerical
outcomes are asserted here. T01 remains **OPEN**: actual branching
persistence is a necessary condition, and no construction satisfying
the required full-image upper bound is supplied.
