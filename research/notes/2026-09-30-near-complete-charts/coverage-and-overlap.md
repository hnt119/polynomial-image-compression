# Exact coverage, fiber tails and chart-output overlap

T01, 30 September 2026, v1. Fixed \(P(x,y)=(x-y)^3+x+y\).
All statements below are elementary internal proofs. No network or external
result is used. Throughout \(A\subset\mathbb R\) is finite, \(N=|A|\),
\(M=N^2\), and all ordered pairs are counted.

## NC-C1 — the optimal subset at a fixed output budget

### Meaning

Suppose the fiber sizes are 4,2,1,1. Two outputs can control six of the
eight pairs. Choosing only part of a selected fiber wastes coverage:
the remaining points have the same already-paid output. This is an abstract
counting example, not a claimed cubic carrier.

### Precise statement — PROVED

Let \(s=|P(A,A)|\), sort the actual fiber sizes as
\(r_1\ge\cdots\ge r_s\ge1\), and set \(C_A(0)=0\),
\(C_A(k)=\sum_{i=1}^k r_i\). For every integer \(0\le k\le s\),
\[
\max_{E\subseteq A^2,\ |P(E)|\le k}|E|=C_A(k), \tag{C1}
\]
\[
\min_{E\subseteq A^2,\ |P(E)|\le k}
\bigl(|P(E)|+M-|E|\bigr)=k+M-C_A(k). \tag{C2}
\]
Without a restriction on k, the latter minimum is exactly s. Searching
all subsets to minimize this certificate therefore amounts to counting
the actual full image.

### Proof

An E using l outputs contains at most \(C_A(l)\) pairs. The union of
the l largest full fibers attains this bound. Thus the second minimum is
\(\min_{0\le l\le k}(l+M-C_A(l))\). Increasing l by one changes this
quantity by \(1-r_{l+1}\le0\), so l=k attains the minimum. At k=s it
equals s. Singleton fibers may be omitted without changing this minimum.

### Why it matters

The entire cumulative curve answers every output-budget coverage question
on a carrier. Saturating selected outputs to full fibers improves coverage
without increasing output cost.

### Scope

This assumes the actual fibers are known. It does not construct compressed
carriers or provide a shortcut for determining their fibers.

## NC-C2 — the actual small-fiber tail is an equivalent target

### Meaning

Almost all pairs must belong to growing fibers. A few large fibers do not
help if most pairs remain in small ones.

### Precise statement — PROVED

For any real \(t\ge1\), put
\[
B_A(t)=\sum_{z:\ 1\le r_A(z)<t}r_A(z),\qquad
r_A(z)=|P^{-1}(z)\cap A^2|.
\]
Then
\[
s\le B_A(t)+M/t. \tag{C3}
\]
If \(E\subseteq A^2\), \(Q=|E|\), \(Z=|P(E)|\), and \(B=M-Q\), then
\[
B_A(t)\le B+tZ. \tag{C4}
\]
For growing carriers these three existence assertions are equivalent,
with possibly smaller fixed positive exponents:

1. \(s=O(N^{2-c})\), for a fixed c>0.
2. There are fixed \(\delta,\varepsilon>0\) and E with
   \(B=O(N^{2-\delta})\), \(Z=O(N^{2-\varepsilon})\).
3. There are fixed \(\eta,\gamma>0\) with
   \(B_A(N^\eta)=O(N^{2-\gamma})\).

Specifically, (1) implies (3) with \(\eta=\gamma=c/2\).
Assertion (2) implies (3) with \(\eta=\varepsilon/2\) and
\(\gamma=\min(\delta,\varepsilon/2)\). Assertion (3) implies (2) with
\(\varepsilon=\eta,\delta=\gamma\), by taking all fibers of size at
least \(N^\eta\). Every strictly smaller exponent than
\(\min(\eta,\gamma)\) absorbs the constants for the constant-free target.

### Proof

There are at most \(B_A(t)\) nonempty small fibers and at most M/t large
fibers, proving (C3). At most B small-fiber pairs lie outside E. Within E,
each of its Z outputs from a small actual fiber contributes fewer than
t pairs, proving (C4). Under (1), \(B_A(t)\le ts\); choose
\(t=N^{c/2}\). Apply (C4) for (2), and the union of large fibers for
(3). The completion inequality gives the remaining implication.

### Why it matters

This is a precise equivalent target without assumed chart libraries or
step inventories. Full fibers admit an abstract cyclic permutation, but
this does not supply an explicit bounded-degree algebraic rule.

### Scope

The criterion is proved; its witness remains OPEN. Selected-action return
counts bound actual fibers only when the returned pairs are distinct.
Formal words and parameter labels are not actual return counts.

## NC-H1 — hierarchical coverage must also accumulate fiber gain

### Meaning

Covering successive portions of the square does not multiply their
compression factors. Their outputs remain in the final union.

### Precise statement — PROVED

For \(E=\bigcup_{j=1}^J E_j\subseteq A^2\), assign each pair to its
first chart, making disjoint \(F_j\subseteq E_j\). Put
\(q_j=|F_j|\), \(z_j=|P(F_j)|\). Then
\[
Q=\sum_jq_j,\quad Z\le\sum_jz_j,\quad
s\le\sum_jz_j+M-Q. \tag{H1}
\]
If Q>0 and \(|F_j\cap P^{-1}(z)|\le D_j\) for every z, then
\[
Z\ge Q/\sum_jD_j. \tag{H2}
\]
Thus near-full Q, \(J=N^{o(1)}\), and \(\max D_j=N^{o(1)}\)
force \(Z\ge N^{2-o(1)}\), even with maximal output overlap.

For a sufficient hierarchy, fix \(\lambda,C,\delta,\varepsilon\) independently
of the growing carriers, with C,delta,epsilon positive. On each *fixed*
carrier suppose the uncovered
remainder contracts each stage by a factor at most \(\lambda\in(0,1)\),
and every stage has \(z_j\le C N^{2-\varepsilon}\). After
\(K=\lceil\delta\log N/\log(1/\lambda)\rceil\) stages,
\[
s\le CK N^{2-\varepsilon}+N^{2-\delta}. \tag{H3}
\]
Every strictly smaller exponent than min(delta,epsilon) follows.
The implication is proved; construction of such stages remains OPEN.

### Proof

Disjoint assignment and a union bound give (H1). Each selected output has
at most \(\sum_jD_j\) assigned pairs, giving (H2). Induction bounds the
remainder by \(\lambda^K M\le N^{2-\delta}\); summing every output charge
gives (H3).

### Why it matters

Logarithmically many stages of bounded fibers cannot produce a power
saving. If the carrier changes, all its new cross-pairs must be charged;
the old-square denominator cannot be retained.

### Scope

The obstruction assumes bounded actual fibers within each stage. Large
constant-output charts need not satisfy it.

## NC-H2 — output overlap is the extra cost for a large library

### Meaning

When each chart contributes few pairs to one output, near-complete
compression requires outputs to recur across many charts. This cost is
different from chart count and pair overlap.

### Precise statement — PROVED

Use the disjoint assignment above. Suppose
\(e_j(z)=|F_j\cap P^{-1}(z)|\le D\), with D>=1, and define
\[
H=\sum_{j<l}|P(F_j)\cap P(F_l)|.
\]
For Q>0,
\[
\boxed{Z\ge\frac{Q^2}{DQ+2D^2H}.} \tag{H4}
\]
Consequently near-full Q, \(D=N^{o(1)}\), and \(H\le N^{2+o(1)}\)
force \(Z\ge N^{2-o(1)}\). One sufficient scope is
\(J\le N^{1+o(1)}\) and
\(|P(E_j)\cap P(E_l)|\le N^{o(1)}\) for every distinct chart pair.
Conversely,
\[
H\ge\frac{Q^2/Z-DQ}{2D^2}. \tag{H5}
\]
For \(Q\asymp N^2\), fixed D, and \(Z\le C N^{2-\varepsilon}\)
with fixed epsilon>0, this forces \(H=\Omega(N^{2+\varepsilon})\).

For univariate rational pair charts \((f_j(t),g_j(t))\) whose coordinate
numerators/denominators have degrees at most d and whose output is
nonconstant, D=6d is valid on arbitrary pole-free parameter subsets.
For polynomial coordinates of degree at most d, D=3d is valid.
In particular the preceding classified quadratic nonconstant pair charts
have D=6. Constant pair charts have bound one. Nonconstant charts whose
output is constant are excluded from this bounded-D conclusion.

### Proof

With \(r_E(z)=\sum_j e_j(z)\), we have
\[
\sum_zr_E(z)^2
=\sum_{z,j}e_j(z)^2+2\sum_{z,j<l}e_j(z)e_l(z)
\le DQ+2D^2H.
\]
Cauchy–Schwarz gives \(Q^2\le Z\sum_zr_E(z)^2\), proving (H4).
This uses an **energy upper bound** for a **support lower bound**.
Large energy is never used as a support upper bound. Rearrangement
gives (H5). Original-chart output intersections bound assigned-chart
intersections, so their stated sufficient bounds give
\(H\le\binom J2 N^{o(1)}\).

For rational f=a/b,g=c/e, put D0=be and T=ae−cb. Then
\[
P(f,g)=\frac{T^3+(ae+cb)D0^2}{D0^3}.
\]
Numerator and denominator degrees are at most 6d. A fixed output has at
most 6d parameter preimages unless this rational output is constant.
Distinct-pair count is at most preimage count. Polynomial coordinate
degree d gives output degree at most 3d. For d=2 a nonconstant pair
cannot have constant output: with U=f−g,V=f+g, the leading degree of
U³ cannot be canceled by V unless U is constant, which then forces V
constant as well.

### Why it matters

This is an actual selected-support obstruction for growing libraries
under an explicit output-overlap hypothesis. A linear chart count alone
is not a failure: the missing requirement is large compatible overlap.

### Scope

The overlap bound is not proved for arbitrary cubic charts or carriers.
Every A² already has N horizontal line charts \((t,a)\), t∈A, with
injective output per chart. A universal near-quadratic theorem for all
these covers would already be a universal theorem about the cubic image;
capacity alone cannot establish it. For mixed libraries, remove the union
of constant-output charts and apply (H4) only to the remaining pair mass.
The removed mass and output count are not free.

## NC-R1 — pair completion changes the scalar denominator

### Meaning

Closing every old pair under exact symmetries introduces new scalars.
Their cross-pairs are not automatically in the construction.

### Precise statement — PROVED

Let a nonempty seed B have n scalars. Apply at most K output-preserving maps per
seed pair, including identity, wherever defined. Let E be their distinct
pair union and A its scalar union, N=|A|. Then
\[
n\le N\le2Kn^2,\quad n^2\le Q\le Kn^2,\quad
P(E)=P(B,B),\quad B_{\rm miss}=N^2-Q. \tag{R1}
\]
Writing \(\beta=B_{\rm miss}/N^2<1\), the exact constraint is
\(N\le\sqrt{K/(1-\beta)}\,n\). Near-full coverage therefore requires
\(N\le(1+o(1))\sqrt K\,n\). If K is fixed
and N/n tends to infinity, then Q/N² tends to zero.

### Proof

Identity includes B² and its scalars. At most Kn² labels each give two
coordinates. Preservation and identity give both output-set inclusions.
Divide \(Q\le Kn^2\) by N² for the final conclusions. Label repetitions
and chart overlaps can only reduce Q.

### Why it matters

A symmetry applied to every old pair is not a near-full chart on the
expanded carrier. This rate test applies before recursion.

### Scope

No universal lower bound on N is claimed. Finite expansions are measured
exactly below; those examples do not prove an asymptotic growth theorem.

## Provenance and status

NC-C1/C2/H1/H2/R1: T01 near-complete charts, 2026-09-30 v1, PROVED by
the complete arguments in their named sections. The degree consequences
are proved here; the earlier degree-two classification is only used to
identify the already classified charts. Independent internal audit is
recorded in verification. No novelty or external review is claimed.
The main report states the single next obligation.
