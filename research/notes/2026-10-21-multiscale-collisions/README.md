# Actual cubic collisions across scales

**T01 · 21 October 2026 · offline · version 1**

## Verdict

**PROVED — a necessary branching pattern, not a construction.** For the fixed
polynomial \(P(x,y)=(x-y)^3+x+y\), a small full image forces most ordered
pairs to encounter many successive branches of their **own exact output
fiber**. In a refinement by two dyadic levels, a fiber can enter at most
eight of the sixteen child squares. Consequently, if
\(|P(A,A)|\le N^{2-c}\), then, for every \(0<\gamma<c\), all but
\(N^{2-\gamma}\) pairs have more than
\[
\boxed{\left\lfloor(c-\gamma)\log_8N\right\rfloor}
\]
genuine branching generations before the scalar cells separate \(A\).
The localized version below explicitly charges both cluster masses and
reuse of actual outputs across different cells.

**OPEN — the original power-saving target.** No carrier or image upper
bound is obtained. The theorem does not locate the branching scales, make
the splits balanced, or imply that witnesses must be fractal or concentrated.
TJ-C6 and the earlier closed architectures are untouched.

## 1. Meaning, statement and proof of the scale-transfer lemma

**Meaning.** A rich output cannot remain in one shrinking rectangle forever.
More strongly, if the entire square has few outputs, nearly every pair
must repeatedly share its exact output with another child rectangle.
This is an all-pair statement, not an energy estimate.

**PROVED — MC-S1/S2.** Choose a bounded half-open interval \(I_0\)
containing \(A\), and divide its intervals into four equal children at
each generation. This is a rooted, possibly translated dyadic partition;
no input is rescaled. Stop at a level \(L\) where every scalar interval
contains at most one element of \(A\). For \(\xi=(x,y)\), let
\(b_L(\xi)\) count the generations at which its parent square contains
points with output \(P(\xi)\) in at least two different child squares.
Then, for every integer \(b\ge0\),
\[
\#\{\xi\in A^2:b_L(\xi)\le b\}\le |P(A,A)|\,8^b. \tag{1}
\]

**Proof.** For fixed \(y\), \(P_x=1+3(x-y)^2\ge1\); the cubic tends
to opposite infinities, so every real fiber is a unique graph \(x=f_z(y)\).
Writing \(d=f_z(y)-y\), implicit differentiation gives
\[
f_z'(y)=\frac{3d^2-1}{3d^2+1},\qquad |f_z'(y)|\le1.
\]
Within one child interval for \(y\), the finite occupied values have
diameter smaller than the child width. Their \(x\)-values therefore
meet at most two child intervals. Four \(y\)-children give at most eight
occupied child squares, including boundary cases.

For one exact output, suppress the unbranched vertices of its finite
occupied-cell tree. Each remaining vertex has at most eight children;
its leaves are the actual ordered pairs, and leaf depth is \(b_L\).
Code children with eight symbols. The leaf words are prefix-free, so at
most \(8^b\) leaves can have length at most \(b\): their extensions to
length \(b\) are disjoint. Sum over the actual outputs to prove (1).
Taking \(b=\lfloor(c-\gamma)\log_8N\rfloor\) proves the verdict.
No external entropy theorem enters this argument.

**Scope.** The improvement over an arbitrary square partition is eight
children rather than sixteen. This uses the cubic's global monotonicity;
it also applies to other polynomials whose fibers have the same graph
property. There is no novelty claim. The terminal depth and gaps between
branching generations may be arbitrarily large.

## 2. Within-cell multiplicity versus cross-cell overlap

**Meaning.** On a block of scales, old output overlap and unresolved scalar
mass can account for richness without new branching. They must be charged.

**PROVED — MC-S3.** At coarse level \(j\), for \(C=I\times J\), set
\[
S_C=P(A\cap I,A\cap J),\qquad
\operatorname{cap}(C)=\min\{|A\cap J|,3|A\cap I|\}.
\]
Fix a finer level \(j+k\) and let \(M(C)\) be the maximum capacity of
its descendant squares there. Write \(s=|P(A,A)|\), and define
\[
\Omega_{j,k}=\frac1s\sum_C M(C)|S_C|
=\frac1s\sum_{z\in P(A,A)}\sum_{C:z\in S_C}M(C).
\]
If \(b_{j,k}\) counts actual branch events within this block, then
\[
\boxed{\#\{\xi:b_{j,k}(\xi)\le b\}
 \le 8^b\sum_C M(C)|S_C|.} \tag{2}
\]
In particular, if \(s\le N^2/R\), \(R>0\), its left side is at most
\(N^2 8^b\Omega_{j,k}/R\).

**Proof.** There is at most one \(x\) per fixed \(y,z\), and at most
three \(y\)'s per fixed \(x,z\). Thus the displayed capacity bounds
local actual multiplicity. Apply the same prefix argument inside each
\((C,z)\)-tree, allowing terminal weight at most \(M(C)\), and sum.
Coarse squares partition pairs; repeated output labels are retained in
\(\Omega\), not declared disjoint. At the single root with singleton
terminal cells, \(\Omega=1\).

**Scope.** A useful scale block needs a bound on both factors, not merely
small scalar cells. An actual output may occur in many coarse cells.
Equation (2) neither supplies such a bound nor turns approximate overlap
into exact overlap. A direct local-rich-mass transfer, with loss
\(2\cdot4^k\), is proved in the [algebra appendix](appendix.md).

## 3. A worked zoom and the exceptional differences

**PROVED — MC-L0.** Put \(d=a-b\), \(x=a+\rho u\),
\(y=b+\rho v\), with \(\rho>0\). Exact expansion gives
\[
\frac{P(x,y)-P(a,b)}\rho
=(1+3d^2)u+(1-3d^2)v
 +3d\rho(u-v)^2+\rho^2(u-v)^3. \tag{3}
\]
Symbols \(u,v\) are normalized offsets, not new independent scalar sets.
For cells of width \(\rho\), take \(u,v\in[0,1)\). The normalized
nonlinear remainder has absolute value at most \(3|d|\rho+\rho^2\);
the original output error is at most \(3|d|\rho^2+\rho^3\).
An output resolution \(\Delta\) becomes \(\Delta/\rho\) in (3).

At \(d=0\) the quadratic term vanishes, but the cubic remains; the
linear part is \(u+v\). At \(d=\pm1/\sqrt3\), the coefficient of
\(v\) vanishes, the coefficient of \(u\) is 2, and the quadratic term
remains. The appendix gives explicit nearby bounds. Neither case damages
\(P_x\ge1\) or the uniform eight-child estimate. Local linearization
alone does not preserve exact equalities at finer output resolutions.

For an exact example in the tested nonuniform set, take \(\rho=1/64\)
and an offset \(t\in\{0,1,3,7\}\). Then
\[
P(\rho t,\rho t)=P(\rho t,1+\rho t)=2\rho t.
\]
The first cell has \(d=0\), the second \(d=-1\); equal offsets cancel
the nonlinear correction in both. These are different cell pairs with
the same actual output. Refining them produces separate labels for the
different \(t\)'s, rather than a growing fiber. In the 12-point audit,
all 16 nonsingleton pairs have exactly one branching generation.

## 4. Theorem applicability

**MISSING SOURCE.** No local text of Raz–Zahl, arXiv:2108.07311,
Theorem 1.18 or its energy-dispersion input was located in the checked
project sources and attachments. The exact hypotheses, constants and
exponent are unavailable; **no exponent from that theorem is used**.
The available earlier projection note is a local bridge/limitations
argument, not a replacement for the missing paper.

**PROVED — applicability test.** An applicable lower bound
\(|P(A,A)|\ge c_0N^\beta\) contradicts the proposed upper bound only
if \(\beta>2-c\), apart from a separate constant check at equality.
Superlinearity alone need not suffice. A bound on a covering number
\(N_\Delta(S)\) also requires its precise hypotheses and normalization.
Small \(N_\Delta(S)\) does not bound the number of distinct values in
one covering interval. Moreover,
\(N_\Delta(S)\le1+\operatorname{diam}(S)/\Delta\): a small metric
count can simply reflect finite output span. None of these observations
implies scalar concentration. [Source and verification ledger](verification.md).

## 5. Bounded exact laboratory

**EXPERIMENTAL — exhaustive for six declared sets only.** The budget was
six sets of at most 24 scalars; the actual maximum was 12. Controls are
integer intervals and the already failed CP ladder at \(m=2,3\).
The sole nonuniform diagnostic is
\[
A=\{0,1,3\}+\tfrac1{64}D,\quad
D=\{0,1,3\}\ \text{or}\ \{0,1,3,7\}.
\]
The three clusters are disjoint. Their fine gaps are unequal. This is
an exact two-level test, not a proposed successful continuation.

| Set | \(N\) | All ordered pairs | Actual outputs | Full fiber histogram: size × number |
|---|---:|---:|---:|---|
| Integer interval | 8 | 64 | 44 | 1×36, 3×4, 4×4 |
| Integer interval | 12 | 144 | 108 | 1×96, 3×2, 4×8, 5×2 |
| CP ladder, \(m=2\) | 6 | 36 | 29 | 1×24, 2×4, 4×1 |
| CP ladder, \(m=3\) | 8 | 64 | 52 | 1×44, 2×6, 4×2 |
| Nonuniform, \(|D|=3\) | 9 | 81 | 75 | 1×69, 2×6 |
| Nonuniform, \(|D|=4\) | 12 | 144 | 136 | 1×128, 2×8 |

Both independent computations agree on every one of the 533 ordered-pair
outputs, after exact field-basis and input-order conversion for CP.
There were 1,599 polynomial evaluations in total, counting two lead
formulas and the independent referee formula. No floating-point equality
or enlarged search was used.

For freely placed closed covering intervals, the exact minimum counts are:

| Nonuniform set | Distinct outputs | \(N_1\) | \(N_{1/16}\) | \(N_{1/256}\) |
|---|---:|---:|---:|---:|
| 9 scalars | 75 | 13 | 42 | 62 |
| 12 scalars | 136 | 19 | 79 | 112 |

These are covering counts of the full exact output set; they are not
fiber sizes. The greedy interval-cover calculation uses rational
comparisons and charges output span explicitly in the saved data.

**Accounting and limitation.** For the exhaustive census take \(E=A^2\):
\(Q=N^2\), \(Z\) is the measured full image, \(B=0\), and
\(|P(A,A)|\le Z+B\) is equality, not a constructive bound. Separately,
the imported CP prescribed ledgers are \((N,Q,Z,B)=(6,8,3,28)\) and
\((8,12,4,52)\), giving upper bounds 31 and 56. Its known quadratic
subsquare lower bound remains in force. Progression asymptotics and
CP failure are imports, not inferred from this table. The diagnostic
supplies no improvement on the earlier \(N^{4/3}\) prescribed-pair rate.
The faithful coefficient explanation in the appendix is explicitly an
application of the existing GS-P4 mechanism.

## 6. One next proof obligation

**OPEN — MC-O1, a cross-block collision-rectangle bound.** Keep the same
\(B=\{0,1,3\}\) and \(\rho=1/64\). For any finite \(D\subset[0,7]\),
define, on the **same** fine-pair set \(D^2\),
\[
F_0(u,v)=P(\rho u,\rho v),\qquad
F_1(u,v)=P(1+\rho u,\rho v).
\]
Let \(Q_4(D)\) count ordered quadruples of pairs
\(p_{11},p_{12},p_{21},p_{22}\in D^2\) satisfying
\[
F_0(p_{11})=F_0(p_{12})\ne F_0(p_{21})=F_0(p_{22}),
\]
\[
F_1(p_{11})=F_1(p_{21})\ne F_1(p_{12})=F_1(p_{22}).
\]
Determine whether an absolute constant \(C\) gives
\(Q_4(D)\le C|D|^3\) for every such \(D\), or supply a counterexample
sequence to this precise bound. This asks whether exact branching
relations in two existing parent blocks can repeatedly close together.
It couples two maps on one common set, not projections on changing strips.
The eight-child theorem alone supplies no such cross-map restriction.
This bound is a proposed diagnostic, not an assumed theorem or a replacement
for full-square fiber accounting. It has not been tested or proved here;
either disposition would still leave the original target unresolved.
