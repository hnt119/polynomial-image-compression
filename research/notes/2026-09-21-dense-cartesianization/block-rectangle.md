# Complete block transitions and rectangular symmetrization

## Claim record and task boundary

- **Date/version:** 21 September 2026, version 1.
- **Track:** T03, newly authorized dense Cartesianization cycle.
- **Fixed polynomial:** \(Q(x,y)=x^2+xy+y^2\), on finite subsets of
  \(\mathbb R\), with the same scalar set in both final coordinates.
- **DC-B1 — PROVED:** cardinality growth under a norm-one map sending an
  entire finite rectangle into another rectangle, §2.
- **DC-B2 — PROVED:** a fixed partition into subexponentially many scalar
  blocks cannot supply the requested return tail using only complete-block
  transitions, §3. This is a certificate obstruction, not an obstruction to
  partial returns or a lower bound for the actual image.
- **DC-R1 — PROVED implication / CONDITIONAL construction:** rectangular
  return tails extend to a common scalar union with an explicit unmatched
  square cost; sufficiently high overlap gives a power-saving implication,
  §4. No carrier satisfying those premises is constructed here.
- **DC-R2 — PROVED implication / CONDITIONAL construction:** charging the
  remaining diagonal blocks, or all four rectangular blocks, gives an
  honest same-set return theorem, §5.
- **Dependencies:** elementary order and finite-set counting, the norm
  coefficient identity, and the established
  [HR-1 return-to-image theorem](../2026-09-16-high-return/return-lemma.md),
  especially §2 and its chosen-lift version. The proofs below are complete
  for the new implications and scoped obstruction.
- **Authorization:** the current dense Cartesianization assignment,
  directions C/E and rectangular symmetrization. This is a symbolic-only
  subtask with **zero evaluations**, no program execution, no network,
  and no imported external theorem or novelty claim.
- **Evidence/audit:** new internal derivations, with author checks of the
  coefficient signs, degenerate rows, overlap counts, ordered pairs and
  zero. Any independent lead review is recorded separately.
- **Historical scope:** the completed
  [Cartesian norm checkpoint](../2026-09-20-cartesian-norm-freeze/Cartesian_Norm_Symmetry_Research_Checkpoint.md)
  is retained. This note does not rerun or alter the earlier orbit,
  denominator or sparse valuation families, nor study \(Q+x\) or \(A-A\).

## 1. Exact coefficient action and coordinate swap

Fix \(\omega=(-1+i\sqrt3)/2\). For real \(a,b\), put
\(u=a+b\omega\). Multiplying and using \(\omega^2=-1-\omega\) gives

\[
u(x-\omega y)=(ax+by)-\omega\bigl(-bx+(a-b)y\bigr).
\]

Consequently

\[
M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},\qquad
N(u)=a^2-ab+b^2=\det M_u.
\tag{1}
\]

If \(N(u)=1\), this is an invertible real-linear map preserving
\(Q\). The conjugate is \(\bar u=(a-b)-b\omega=u^{-1}\). With
\(J(x,y)=(y,x)\), direct matrix multiplication gives

\[
J M_u J
=\begin{pmatrix}a-b&-b\\b&a\end{pmatrix}
=M_{\bar u}.
\tag{2}
\]

Thus a return from \(X\times Y\) to \(X\times Y\) yields a return
from \(Y\times X\) to \(Y\times X\) after swapping both source and
target and replacing \(u\) by \(\bar u\). Swap itself need not be
norm-one multiplication; equation (2) is the exact transported action.

Distinct multipliers produce distinct returned pairs at every nonzero
pair, by cancellation of the nonzero complex number \(x-\omega y\).
At zero there is only one distinct returned pair. All sufficient lemmas
below are stated in terms of **distinct returned pairs**, so zero must be
declared exceptional whenever the required threshold exceeds one.

## 2. DC-B1 — an entire mixed block must grow

### Mathematical statement

Let \(X,Y,X',Y'\subset\mathbb R\) be nonempty finite sets, of sizes
\(m,n,m',n'\). Suppose \(N(u)=1\) and

\[
M_u(X\times Y)\subseteq X'\times Y'.
\tag{3}
\]

Then the coordinate inclusions are exactly

\[
aX+bY\subseteq X',\qquad -bX+(a-b)Y\subseteq Y'.
\tag{4}
\]

Each row with two nonzero coefficients therefore forces its target size
to be at least \(m+n-1\). In particular, when
\(ab(a-b)\ne0\),

\[
m',n'\ge m+n-1.
\tag{5}
\]

Writing \(s=m+n-2\) and \(s'=m'+n'-2\), all norm-one cases are:

\[
\begin{array}{ll}
b=0:&u=\pm1,\quad m'\ge m,\ n'\ge n,\quad s'\ge s;\\
a=0:&b=\pm1,\quad m'\ge n,\ n'\ge m+n-1,
       \quad s'\ge s+(n-1);\\
a=b\ne0:&a=\pm1,\quad m'\ge m+n-1,\ n'\ge m,
       \quad s'\ge s+(m-1);\\
ab(a-b)\ne0:&s'\ge2s.
\end{array}
\tag{6}
\]

Thus if \(m,n\ge2\), every transition with \(u\ne\pm1\) strictly
increases \(m+n-2\). The only monomial matrices in this multiplication
family are \(+I,-I\); the four other Eisenstein root-of-unity matrices
have one mixed row, not two independent coordinate permutations.

### Proof

For nonempty finite real sets \(C,D\), list their elements increasingly.
The sums
\(c_1+d_1<\cdots<c_m+d_1<c_m+d_2<\cdots<c_m+d_n\)
give

\[
|C+D|\ge|C|+|D|-1.
\tag{7}
\]

Scaling by a nonzero real number preserves cardinality, including for
negative scalars. Applying (7) to either mixed row proves (5) and the
mixed-row parts of (6). A row with one nonzero coefficient has exactly
the cardinality of that coordinate. Finally, substituting \(b=0\),
\(a=0\) or \(a=b\) into \(a^2-ab+b^2=1\) gives the listed cases.
They exhaust all possible zero entries of (1). \(\square\)

### What it means

A whole rectangular block cannot rotate into a block of the same two
sizes unless the action is one of the scalar signs, apart from degenerate
one-point sides. Making the angle very small does not remove this exact
cardinality increase. The inequality concerns an entire block; it is not
an estimate for an arbitrary dense subset of the block.

### Why it matters

For a finite transition system of rectangles with both sides of size at
least two, no directed cycle of complete transitions can contain a
non-scalar action: (6) would strictly increase \(s\) around that cycle.
Fully mixed transitions double \(s\). A chain with initial excess \(s_0>0\)
and all scalar side sizes at most \(M\) therefore contains at most

\[
\left\lfloor\log_2\frac{2(M-1)}{s_0}\right\rfloor
\tag{8}
\]

fully mixed steps, even with other complete transitions interspersed.
In a sequence where the starting sides and the largest block all have
size \(e^{ad+o(d)}\), this number is \(o(d)\). These are size-growth
constraints on the complete transition graph, not bounds on the number
of partial-return actions.

## 3. DC-B2 — subexponentially many partition blocks do not fix coverage

### Mathematical statement

Let \(A\) be a finite real set of size \(n\), partitioned into
\(k\) nonempty, pairwise disjoint scalar blocks

\[
A=A_1\sqcup\cdots\sqcup A_k.
\]

A **complete-block return certificate** for a source block
\(A_i\times A_j\) may credit a multiplier \(u\) only when some
indices \(r,s\) satisfy

\[
M_u(A_i\times A_j)\subseteq A_r\times A_s.
\tag{9}
\]

The target indices may depend on \(u,i,j\), but not on the individual
pair inside this source block. Different source blocks may use different
actions. All credited multipliers are actual distinct norm-one elements.

Put \(M=\max_i|A_i|\). If \(M\ge2\), every pair of a largest diagonal
block \(A_{i_*}^2\) has at most two distinct returned pairs credited by
this certificate. Consequently, for every required return threshold
\(R>2\), its uncertified set has size at least

\[
\boxed{B_{\rm cert}\ge M^2\ge n^2/k^2.}
\tag{10}
\]

In particular, if \(n_d=e^{ad+o(d)}\), \(a>0\), and
\(k_d=e^{o(d)}\), this architecture leaves
\(B_{\rm cert}\ge e^{2ad-o(d)}\). It cannot prove the desired bound
\(B_{\rm cert}\le e^{(2a-\delta)d+o(d)}\) with any fixed
\(\delta>0\), while certifying an eventually growing return threshold.

### Proof

Every norm-one \(u\ne\pm1\) has a mixed row by (6). Its image on
\(A_{i_*}^2\) has at least \(2M-1>M\) different values in that
coordinate. No target block, of size at most \(M\), can contain this
coordinate image. Such a multiplier cannot satisfy (9).

Only \(+I,-I\) remain, and some of these might also be illegal. They
produce at most two different returned pairs, or only one at zero.
Because the source blocks form a partition, a pair in \(A_{i_*}^2\)
cannot obtain a different source-block certificate from another
membership. Thus all \(M^2\) pairs lie below a threshold \(R>2\).
Finally \(n=\sum_i|A_i|\le kM\), proving (10). Under the displayed
asymptotic assumptions \(M\ge n/k\to\infty\), and
\(\log(n^2/k^2)=2ad-o(d)\); this contradicts any fixed positive
exceptional-set deficit. \(\square\)

### What it means

The largest block is already too large to fit the mixed coordinate sum
into any target block. Its square is a subexponential fraction of the
domain when the number of states is subexponential; that is still much
larger than the exponentially small bad fraction required by the target.

### Why it matters, and exact limitations

This rejects the literal partition model whose return certificates use
complete block-to-block inclusions. It leaves **OPEN** approximate
inclusions, target blocks chosen separately for individual pairs, a
different source partition for each action, overlapping covers with a
separate valid assignment argument, and incidental returns not certified
by (9). It is not an actual image lower bound.

There is a simple quantitative reason not to overextend (7). If (3)
holds only after removing \(B\) source pairs, the same elementary
argument gives merely

\[
|X'|\ge m+n-1-B
\tag{11}
\]

for a mixed first row, and analogously for the second. Indeed each
coordinate value lost by removing pairs must have at least one removed
pair, so at most \(B\) such values disappear. For a largest square
block this only forces \(B\ge M-1\), a linear cost. It supplies no
quadratic bad-pair lower bound for approximate transitions. No such
approximate-return obstruction is inferred here.

## 4. DC-R1 — swap and high-overlap symmetrization

### Mathematical statement

Let \(X,Y\subset\mathbb R\) be finite nonempty sets, put
\(A=X\cup Y\), \(n=|A|\), and define

\[
X_0=X\setminus Y,\qquad Y_0=Y\setminus X,\qquad
p=|X_0|,\quad q=|Y_0|.
\]

Let \(U\) be a finite set of actual norm-one multipliers. Suppose that,
outside \(E\subseteq X\times Y\), every pair has at least \(R>0\)
distinct returns into \(X\times Y\) using \(U\). Then the action
set \(U\cup\bar U\), with duplicates removed, supplies at least
\(R\) distinct returns into \(A^2\) outside a set of at most

\[
\boxed{B\le p^2+q^2+2|E|.}
\tag{12}
\]

The established HR-1 theorem consequently gives

\[
\boxed{|Q(A,A)|\le\frac{n^2}{R}+p^2+q^2+2|E|.}
\tag{13}
\]

More generally the same conclusion holds if the original rectangular
returns land in \(A^2\) rather than \(X\times Y\); their swapped
targets are still in \(A^2\).

In particular, fix positive \(\varepsilon,\eta,\delta\) and constants
\(C,C'<\infty\). If along arbitrarily large such unions

\[
R\ge n^\varepsilon,\qquad
|X\mathbin\triangle Y|\le Cn^{1-\eta},\qquad
|E|\le C'n^{2-\delta},
\tag{14}
\]

then every fixed

\[
0<c<\min\{\varepsilon,2\eta,\delta\}
\tag{15}
\]

eventually satisfies \(|Q(A,A)|\le n^{2-c}\).
This is a proved sufficient implication; no witness to (14) is supplied.

### Proof

By (2), transposing every source and target of a rectangular return
transports it to a conjugate-multiplier return on \(Y\times X\).
Distinct targets remain distinct under the swap. The transported bad
set is \(J(E)\), of the same size as \(E\).

Every pair not in \((X\times Y)\cup(Y\times X)\) must have both
coordinates in \(X_0\), or both in \(Y_0\), and each such pair is
indeed outside those rectangles. Thus, exactly,

\[
A^2\setminus\bigl((X\times Y)\cup(Y\times X)\bigr)
=X_0^2\sqcup Y_0^2.
\tag{16}
\]

The set
\(X_0^2\cup Y_0^2\cup E\cup J(E)\) therefore contains every
uncertified pair and has size at most (12). Returns from either rectangle
are genuine returns into the same \(A^2\); deduplicating the union of
actions does not remove any distinct target certified by that rectangle.
No sum of two return counts is asserted on their overlap.

Apply HR-1 to obtain (13). Finally
\(p^2+q^2\le(p+q)^2=|X\mathbin\triangle Y|^2\), so (14) gives

\[
|Q(A,A)|\le n^{2-\varepsilon}
 +C^2n^{2-2\eta}+2C'n^{2-\delta}.
\tag{17}
\]

For every strict exponent in (15), division by \(n^{2-c}\) makes
all three terms tend to zero. This absorbs their constants and proves
the final coefficient-free bound. \(\square\)

### What it means

Swapping coordinates provides the reverse rectangle with no exponential
loss. It does not automatically provide the two same-side squares. The
cost of those squares is exactly the sum of the squares of the two
unmatched scalar populations. High overlap is sufficient because it
makes those populations smaller by a fixed power.

### Why it matters

Comparable rectangular side sizes alone are not enough. For disjoint
\(X,Y\) with \(|X|=|Y|=m\), the two controlled rectangles occupy
\(2m^2\) of the \(n^2=4m^2\) pairs; the remaining \(n^2/2\)
pairs cannot be discarded in a power-saving argument. This is a
coverage accounting statement, not a claim that those remaining pairs
actually have few returns.

Taking \(A=X\cap Y\) instead does not fix this automatically: a
return into \(X\times Y\) can leave the intersection square. A
separate surviving-return bound would be needed after that input
thinning. The union lemma avoids this loss by retaining every target.

## 5. DC-R2 — complete accounting of the remaining blocks

### Mathematical statement

Retain the sets of §4. Suppose the rectangular premise with threshold
\(R\) and exception set \(E\) holds. Suppose also that, outside
\(F_X\subseteq X_0^2\) and \(F_Y\subseteq Y_0^2\), pairs in the two
exclusive squares have at least \(R\) distinct norm-one returns into
\(A^2\), using finite action sets \(U_X,U_Y\). Then the union of
these actions and \(U,\bar U\) gives

\[
B\le2|E|+|F_X|+|F_Y|,
\qquad
|Q(A,A)|\le\frac{n^2}{R}+2|E|+|F_X|+|F_Y|.
\tag{18}
\]

An alternative sufficient premise gives a return threshold \(R\)
on each of \(X^2,X\times Y,Y\times X,Y^2\), with respective
exception sets \(E_{XX},E_{XY},E_{YX},E_{YY}\). Taking the union of
the four finite action sets gives

\[
B\le\sum_{V,W\in\{X,Y\}}|E_{VW}|,
\qquad
|Q(A,A)|\le\frac{n^2}{R}+\sum_{V,W\in\{X,Y\}}|E_{VW}|.
\tag{19}
\]

These are conditional sufficient criteria, not assertions that such
blockwise return families exist.

### Proof and meaning

Equation (16) identifies the only blocks missing from the two rectangular
certificates. The added hypotheses cover them except for \(F_X,F_Y\),
giving (18). For (19), the four rectangles cover \(A^2\). Any pair
outside the union of their exceptional sets has a valid certificate from
at least one rectangle containing it. The union of the actual action
sets retains that certificate without multiplying its return count.
HR-1 proves both displayed image bounds.

This states precisely what a rectangular construction must pay for when
the two coordinate sets do not overlap sufficiently. It is enough to
control the exclusive same-side squares; proving redundant certificates
on every overlap is unnecessary.

### General partition accounting and overlapping covers

If \(A=\bigsqcup_{i=1}^k A_i\), let \(\mathcal S\) be the block
pairs having a threshold certificate, with bad sets
\(E_{ij}\subseteq A_i\times A_j\). Then

\[
B\le\sum_{(i,j)\notin\mathcal S}|A_i||A_j|
       +\sum_{(i,j)\in\mathcal S}|E_{ij}|.
\tag{20}
\]

This follows from the disjoint decomposition of \(A^2\), with an
action union and no duplicated-target gain. If there are
\(k_d=e^{o(d)}\) blocks, summing \(k_d^2\) uniformly bounded bad
populations costs only \(e^{o(d)}\). The individual hypotheses must
still hold; DC-B2 rules them out for the exact complete-transition
partition architecture when an eventually growing return threshold, hence
eventually $R>2$, is sought.

For overlapping covers, \(\sum|A_i||A_j|\) is not automatically a
count of distinct scalar pairs. If each scalar belongs to at most
\(\kappa\) blocks, each pair is counted at most \(\kappa^2\) times.
A counted collection of block pairs then gives only the corresponding
lower bound divided by \(\kappa^2\) for its union. Near-full coverage
requires the actual union/complement or a valid assignment of pairs;
an incidence sum alone does not establish (20). No such assignment or
refinement cost is silently supplied here.

## 6. Construction and signed-rate ledger

| Gain or cost | Complete-block partition | Rectangular symmetrization |
|---|---|---|
| Growing parameter and fixed choices | For the rate statement, choose fixed \(a>0\) and a sequence with \(\log n_d=ad+o(d)\), \(\log k_d=o(d)\); the partition and its complete-transition rule are explicit hypotheses. | Fix threshold, overlap and bad-set exponents before growth; the sets and finite actual action families must supply the hypotheses. |
| Scalar input size | Exact \(n=\sum_i|A_i|\) for disjoint blocks. | Exact \(n=|X|+|Y|-|X\cap Y|\), between the maximum and sum of the side sizes. No cardinality is inferred from labels. |
| Parameter/projection fibers | Scalar coordinates themselves; no field trace or many-to-one projection. Overlap incidences, if introduced, cost \(\kappa^2\), not one factor. | Ordinary set union; overlapping scalar values are deduplicated. The coefficient representation \(x-\omega y\) is injective. |
| Input thinning, both coordinates | No thinning in DC-B2; every pair of the largest block is counted. | No thinning in DC-R1: every original target remains in \(A^2\). Restriction to \(X\cap Y\) would need a new return-survival proof. |
| Actual actions and stabilizers | Only \(\pm I\) can give complete returns from the largest square; at most two distinct returned pairs, at most one at zero. Other partial actions are not counted or excluded. | Swap uses conjugate multipliers; the union has at most twice the original action population before other blocks are added. There is no exponential label cost and no claim of twice as many returns. Zero cannot meet a distinct-pair threshold above one. |
| Norm, field and embedding | Fixed real coefficient norm identity (1); rationality or a growing number field is not required. | Same exact real action; conjugation and the swap identity are explicit in (2). |
| Degree, discriminant, regulator and local splitting | No field tower, lattice-volume argument, integral-unit count or splitting estimate is used; none is credited with a gain. | Likewise inapplicable to the combinatorial implication. Arithmetic realizations must independently verify their own legal-return hypotheses. |
| Heights and denominators | The obstruction is invariant under scalar rescaling and uses exact cardinalities, not a height bound. | No denominator or height estimate is supplied: membership of every returned scalar coordinate is part of the premise. Unknown arithmetic costs of a future witness are not zero. |
| Blocks, branches and carries | Complete transition targets must be one fixed block pair for the whole source rectangle. Changing this rule leaves the theorem's scope. | At most four action families in (19); no return counts are multiplied across families or overlapping source rectangles. No digit/carry encoding is used. |
| Exceptional/uncovered pairs | At least \(n^2/k^2=e^{2ad-o(d)}\) uncertified pairs when the threshold exceeds two. This is not a bound on their actual return multiplicity. | At most \(p^2+q^2+2|E|\) in DC-R1, or the separately charged bad sets in (18)/(19). Every ordered pair is accounted for. |
| Rate conclusion | The complete-block certificate has no positive exceptional-tail deficit. Actual image rate and approximate-return rate remain OPEN. | If \(R\ge e^{rd-o(d)}\), \(|X\triangle Y|\le e^{(a-\tau)d+o(d)}\), and \(|E|\le e^{(2a-\delta)d+o(d)}\), then the output exponent is at most \(2a-\min(r,2\tau,\delta)\). |
| Strict target exponent | None follows for this certificate. | Every \(0<c<\min(r,2\tau,\delta)/a\) follows, provided all three rates are positive and the stated \(n=e^{ad+o(d)}\) input count holds. |

## 7. Evidence and disposition

These statements are symbolic proofs, with no finite scouting, numerical
fit, factorization, enumeration or external input. All ordered-pair counts,
zero exceptions, action unions and overlap multiplicities are explicit.
This subtask's evaluation count is zero. Only this new note was authored;
historical reports and source bytes were not edited. Repository-wide
checks and any separately authorized diagnostics are the lead's recorded
responsibility, not proof premises here.

The complete-block partition certificate is **FAILED in the precise scope
of DC-B2**. The high-overlap and four-block symmetrization implications
are **PROVED**, with their construction premises **OPEN**. The note does
not select a new carrier, launch an extra search, or claim a universal
obstruction to dense approximate Cartesian returns.
