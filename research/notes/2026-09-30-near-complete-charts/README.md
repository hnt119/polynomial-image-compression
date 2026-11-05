# Near-complete nonlinear charts for the plus-sign cubic

**T01 · 30 September 2026 · version 1 · offline research**

\[
P(x,y)=(x-y)^3+x+y.
\]

This commissioned cycle continues the
[nonlinear coordinate-reuse checkpoint](../2026-09-21-nonlinear-reuse/README.md).
It investigates coverage of the actual scalar square. Historical low-degree,
fixed-output and sparse-curve searches were not restarted.

## 1. Short verdict

**OPEN:** no near-complete compressed subset or cubic power saving was found.

**PROVED:** three scoped advances clarify what a successful construction needs:

- Any library of polynomial output-preserving automorphisms that preserves
  a common finite controlled set has equivalence classes of size at most
  two. The library size and polynomial degrees may grow arbitrarily.
  This rules out that long-orbit certificate, not the actual cubic image.
- A growing chart library with bounded contributions per output and
  insufficient total output overlap has near-quadratic selected support.
  This is a support obstruction under explicit overlap hypotheses.
- The original target is equivalent, after reducing fixed exponents, to
  a polynomially small **pair-mass tail of actual small fibers**.

Six new exact completion scouts applied nonlinear rules to every pair
of a seed square. Scalar expansion left only 2–4% prescribed coverage.
They were stopped after their first completion. Their full cumulative
fiber profiles have no substantial finite concentration.

These are scoped obstruction outcomes. No universal rational-chart
impossibility, new positive asymptotic family, or novelty claim is made.

## 2. What the controlled set E means

E is the portion of the Cartesian square where the proposed compression
works. Every pair outside E may produce a new output. With
\[
N=|A|,\quad Q=|E|,\quad Z=|P(E)|,\quad B=N^2-Q,
\]
the safe full-support bound is
\[
\boxed{|P(A,A)|\le Z+B.} \tag{1}
\]

For example, the best coverage among the six new prescribed completions
has N=23, Q=19, Z=7. It leaves B=510 pairs, and its actual image has
517 values. Its seven selected outputs do not control the other pairs.

Near-complete coverage by itself is automatic: E=A² always works as a
set, and N line charts cover it. This is not claimed as a new solution
of the structural problem. Coverage must be accompanied by useful output
compression or an explicit growing-class mechanism.

## 3. Exact correlated coordinates

The frozen bijection is
\[
u=x-y,\qquad L=x+y,\qquad
x=(L+u)/2,\quad y=(L-u)/2.
\]
Thus
\[
\Omega_A=\{(u,L):(L+u)/2\in A,\ (L-u)/2\in A\},\quad |\Omega_A|=N^2,
\]
\[
P(A,A)=\{u^3+L:(u,L)\in\Omega_A\}.
\]
The two memberships remain correlated throughout.

For studying pair maps it is also useful to use z=u³+L:
\[
H(x,y)=(u,z),\qquad
H^{-1}(u,z)=\left(\frac{z-u^3+u}{2},\frac{z-u^3-u}{2}\right). \tag{2}
\]
This is an exact polynomial change of pair coordinates, not a same-set
scalar transformation or permission to replace the domain by a product.
The collision equation is
\[
L-L'=v^3-u^3=(v-u)(u^2+uv+v^2).
\]
Prescribing a new difference v and retaining z enforces this equation;
putting both resulting scalars in one small carrier is the remaining cost.

## 4. The near-complete target and an equivalent tail

The required quantitative gate remains
\[
B=O(N^{2-\delta}),\qquad Z=O(N^{2-\varepsilon}),
\quad\delta,\varepsilon>0\text{ fixed}. \tag{3}
\]
Every strictly smaller exponent than min(delta,epsilon) follows in the
constant-free target. Merely having Q=N^{2+o(1)} does not bound B.

**Meaning.** Almost all pairs must sit in fibers whose sizes grow as a
fixed power of N.

**Precise statement — PROVED, NC-C2.** For actual full-square fibers put
\[
r_A(z)=|P^{-1}(z)\cap A^2|,\qquad
B_A(t)=\sum_{1\le r_A(z)<t}r_A(z).
\]
For every real \(t\ge1\),
\[
|P(A,A)|\le B_A(t)+N^2/t,\qquad B_A(t)\le B+tZ. \tag{4}
\]
Existence of (3) is equivalent, with possibly smaller fixed exponents, to
\[
B_A(N^\eta)=O(N^{2-\gamma}),\qquad \eta,\gamma>0. \tag{5}
\]

**Proof.** Small fibers contribute at most their pair mass in outputs;
large fibers number at most N²/t. Among small-fiber pairs, at most B are
outside E and fewer than t per selected output are inside. For (3) choose
t=N^{epsilon/2}. Conversely take E to be the union of fibers of size at
least N^eta. If the full image is O(N^{2-c}), choosing t=N^{c/2} also
proves (5).

**Why it matters.** This criterion uses actual fibers and imposes no
symmetry inventory or rational parametrization.

**Scope.** It is an equivalence and proved implication, with no witness
yet. Full proof: [coverage-and-overlap, NC-C2](coverage-and-overlap.md).

## 5. Best chart libraries examined

No tested library approaches the gate. The strongest constructive test
was to complete **every old pair**, rather than select one old output fiber.

For a seed set S and every (x,y)∈S², calculate (u,z) by (2). Three charts
use the following new differences, keeping z unchanged:

| Library | Differences used | Domain |
|---|---|---|
| Output-adaptive linear step | u, u+z/2, u−z/2 | Every old pair |
| Output-adaptive quadratic step | u, u+z²/2, u−z²/2 | Every old pair |
| Rational three-cycle | u, 1−1/u, 1/(1−u) | Nonidentity branches only for u∉{0,1}; identity always retained |

Apply H inverse, deduplicate the resulting pairs to form E, and let A
contain all resulting scalar coordinates. Each map preserves P exactly.

These are new all-pair assemblies. The first two permit steps depending
on the output, not a fixed-step grid. The third is a rational map with
a pole, outside the polynomial-automorphism class. The domain restriction
keeps complete finite three-cycles; it is stricter than the domain of an
individual branch. No scalar pair in the final A² is dropped from its
full-image audit.

The two seeds were S₁={0,1/3,1/2} and S₂={0,1/4,1}. Each library was
stopped after its first exact completion. This is finite evidence, not
an asymptotic classification of those recursive formulas.

## 6. Coverage calculation

**Meaning.** Covering the old square does not cover the square of the
new, larger scalar pool.

**Precise statement — PROVED, NC-R1.** If at most K preserving maps,
including identity, are applied to each pair of an n-point seed, then
\[
n^2\le Q\le Kn^2,\qquad n\le N\le2Kn^2,\qquad
P(E)=P(S,S). \tag{6}
\]
Writing beta=B/N²<1, near-full coverage requires
\[
N\le\sqrt{K/(1-\beta)}\,n
=(1+o(1))\sqrt K\,n\quad\text{if }\beta\to0. \tag{7}
\]

**Proof.** Count at most Kn² labels, two scalars each; identity includes
the seed square. Deduplication decreases Q. Output preservation plus
identity gives both output-set inclusions. Divide Q≤Kn² by N².

**Why it matters.** With K=3 and n=3, a near-full first step would need
N near 3√3. The actual N values are 23–35.

**Scope.** Formula (7) is necessary, not a universal scalar-growth lower
bound. Finite failures do not prove every recursive continuation fails.

## 7. Output-support calculation

The prescribed output set is exactly the seed image: nine values for
S₁, seven for S₂. Pair labels are deduplicated before assigning capacity.

| Seed / library | N | Labels Q0 | Q | Z | Q/Z | Full image |
|---|---:|---:|---:|---:|---:|---:|
| S₁ / linear step | 35 | 27 | 25 | 9 | 25/9 | 1201 |
| S₁ / quadratic step | 35 | 27 | 25 | 9 | 25/9 | 1207 |
| S₁ / three-cycle | 27 | 21 | 21 | 9 | 7/3 | 715 |
| S₂ / linear step | 26 | 27 | 21 | 7 | 3 | 657 |
| S₂ / quadratic step | 30 | 27 | 23 | 7 | 23/7 | 881 |
| S₂ / three-cycle | 23 | 19 | 19 | 7 | 19/7 | 517 |

All rows are **EXPERIMENTAL, exact**. Three chart images can overlap in
both pairs and outputs; the data retains both intersections, all parameter
projection fibers, and actual coordinate occurrence counts. Summing the
three chart pair counts is not used as Q.

## 8. Full complement audit

| Seed / library | Uncovered B | Safe Z+B | Actual full image |
|---|---:|---:|---:|
| S₁ / linear step | 1200 | 1209 | 1201 |
| S₁ / quadratic step | 1200 | 1209 | 1207 |
| S₁ / three-cycle | 708 | 717 | 715 |
| S₂ / linear step | 655 | 662 | 657 |
| S₂ / quadratic step | 877 | 884 | 881 |
| S₂ / three-cycle | 510 | 517 | 517 |

The missing mass is decisive in every scout. Adding all remaining pairs
gives full coverage but restores the actual output costs in the last
column. The raw certificates retain selected and unselected members of
every actual output fiber, so incidental collisions are included.

A second strategy covers half of the *remaining* pair mass at each stage,
using the next largest full fibers. This reaches the whole fixed square
in 10–11 stages here, but requires all 517–1207 outputs in total.
This is an exact coverage control, not a new compression construction.

## 9. Fiber distribution and cumulative coverage

**Meaning.** The largest few fibers must capture most of the pair mass.
A maximum fiber of four or six is not enough by itself.

**Precise statement — PROVED, NC-C1.** Sorting full fiber sizes as
r₁≥⋯≥r_s and putting C_A(k)=r₁+⋯+r_k gives
\[
\max_{|P(E)|\le k}|E|=C_A(k),\qquad
\min_{|P(E)|\le k}(|P(E)|+N^2-|E|)=k+N^2-C_A(k). \tag{8}
\]
The unrestricted minimum is exactly the full image size s.

**Proof.** Include every point of a selected fiber. The k largest fibers
maximize coverage. Adding fiber k+1 changes the safe cost by 1−r_{k+1}≤0.

**Why it matters.** Optimizing this certificate over all subsets of a
known carrier cannot beat its actual image. The cumulative curve is the
exact finite diagnostic.

**Scope.** Knowing this optimum does not supply a carrier with a good curve.

For the test budget k=floor(N^{3/2}), the actual counts are:

| Seed / library | k | C_A(k) | N²−C_A(k) | Outputs needed for at least 90% coverage |
|---|---:|---:|---:|---:|
| S₁ / linear step | 207 | 231 | 994 | 1079 |
| S₁ / quadratic step | 207 | 225 | 1000 | 1085 |
| S₁ / three-cycle | 140 | 154 | 575 | 643 |
| S₂ / linear step | 132 | 151 | 525 | 590 |
| S₂ / quadratic step | 164 | 183 | 717 | 791 |
| S₂ / three-cycle | 110 | 122 | 407 | 465 |

Every C_A(k), including k=0 and k=s, is recorded in the
[portable exact results](../../../examples/2026-09-30-near-complete-charts.json).
The [experiment companion](exact-experiments.md) gives the full histograms.
At least 95% of all pairs in each scout lie in singleton fibers.
No asymptotic claim is inferred from this range.

## 10. Best obstruction theorems

### A. Nonlinear polynomial pair automorphisms

**Meaning.** Global polynomial invertibility does not provide growing
finite output-preserving classes, even when the formulas have high degree.

**Precise statement — PROVED, NC-A1/A2.** Every polynomial automorphism
with P∘Phi=P is, in (2),
\[
(u,z)\longmapsto(a u+f(z),z),\qquad a\in\mathbb R^\times,\ f\in\mathbb R[z].
\]
For any common finite invariant E, an arbitrarily large family of such
maps has generated classes of size at most two. If C is their class count,
\[
C+N^2-Q\ge\lceil N^2/2\rceil. \tag{9}
\]

**Proof.** A polynomial inverse forces degree one in u and a constant
nonzero leading coefficient. On any finite ordered fiber section, an
affine permutation is identity or its unique order reversal. All generators
therefore have the same two possible rank actions.

**Why it matters.** This excludes a whole near-complete long-orbit
architecture, uniformly in degree and library size.

**Scope.** It is an orbit-certificate obstruction. Different classes can
share outputs, so (9) is not an actual-image lower bound. Partial-return
rules are outside the common-invariance hypothesis.

NC-A3 also bounds classes generated by arbitrary output-preserving row/
column rules by three; globally rational coordinate-preserving identities
are trivial. NC-A5 treats polynomial output relabeling P∘Phi=psi∘P:
psi must be affine, generated finite orbits have at most four points,
and the correctly charged per-orbit output certificate still costs at
least N²/2. Complete statements and proofs:
[finite invariant sets](affine-fiber-orbits.md).

The rational boundary matters. NC-A4 explicitly constructs m-cycles of a
Möbius rotation on a cubic fiber for every m≥3. Their scalar union has
m≤N≤2m, Q=m and Z=1, leaving B=N²−Theta(N). This is a proved boundary
example, immediately rejected as sparse; no sparse-curve search was run.

### B. Growing libraries with insufficient output overlap

**Meaning.** Enough charts to cover the square are not enough; their
outputs must overlap at a quantitatively growing rate.

**Precise statement — PROVED, NC-H2.** Assign overlapping pairs to their
first chart, obtaining disjoint F_j with union E. Assume Q>0 and D>=1.
Suppose each chart has at most D pairs per output, and set
\[
H_{\rm out}=\sum_{j<l}|P(F_j)\cap P(F_l)|.
\]
Then
\[
\boxed{Z\ge Q^2/(DQ+2D^2H_{\rm out}).} \tag{10}
\]
Near-full Q, D=N^{o(1)} and H_out≤N^{2+o(1)} imply Z≥N^{2−o(1)}.
For Q asymptotic to N² and fixed D, a proposed Z=O(N^{2−epsilon})
requires H_out=Omega(N^{2+epsilon}).

**Proof.** Each diagonal contribution to selected collision energy is at
most D times its pair count; each shared chart-output contributes at most
D² to a cross term. Hence energy≤DQ+2D²H_out. Cauchy–Schwarz then gives
the stated **support lower bound**.

**Why it matters.** This advances from pair capacity to actual support
under a stated overlap condition. Nonconstant-output rational curve charts
of coordinate degree d have D≤6d; polynomial ones have D≤3d.

**Scope.** The overlap hypothesis is not proved for arbitrary cubic
carriers. Constant-output curve charts are excluded from the bounded-D
claim and must have their mass charged separately. A linear chart count
alone does not imply quadratic support.

### C. Hierarchies

NC-H1 proves Z≥Q/(sum D_j) if stage j has at most D_j pairs per output.
Thus subpolynomially many stages with subpolynomial per-stage fibers cannot
give a power saving, even allowing full overlap of their output sets.
Conversely a fixed-factor remainder contraction plus a proved
O(N^{2−epsilon}) output charge per stage would work in O(log N) stages.
Those construction premises remain OPEN. Full proofs of both directions:
[coverage-and-overlap](coverage-and-overlap.md).

## 11. Exact experiments and audit

One new run tested the six predetermined all-pair completions above using
exact rational arithmetic. No prior carrier grid was rerun. The largest
carrier had 35 scalars.

- 5,284 full new-square evaluations plus 54 seed evaluations: **5,338** total.
- **11,072** additional charged checks in the declared accounting categories.
- CPython 3.12.7; 0.124286 research CPU seconds.
- No floating-point equality, randomness, network access or arithmetic amplification.
- Every candidate stopped after its first completion; no second-level expansion.

The global ceiling was 24 carriers, 200,000 cubic evaluations and two million
additional checks. Exact parameters, code/results hashes, full certificates,
independent tiny tests, proof audits and repository checks are in
[verification](verification.md). Finite evidence remains EXPERIMENTAL.

## 12. Full N,Q,Z,B and cost ledger

The [construction ledger](construction-ledger.md) charges scalar growth,
both coordinate projections, duplicate labels, chart and output overlaps,
poles, denominators, coefficient heights and all unselected cross-pairs.

| Model | Proved counts or rates | Disposition |
|---|---|---|
| Common-invariant polynomial preserving-map library | Generated classes≤2; certificate≥N²/2 | FAILED orbit certificate, actual image OPEN |
| Polynomial output-relabeling library | Orbits≤4; per-orbit output certificate≥N²/2 | FAILED stated certificate |
| One rational m-cycle | N=Theta(m), Q=m, Z=1, B=Theta(N²); q=1,z=0,b=2 | FAILED near-full coverage |
| Near-full low-overlap chart library | q=2 and selected support≥N^{2−o(1)} under (10) | FAILED under explicit hypotheses |
| K-map completion of an n-point seed | Q≤Kn²; near-full requires N≤(1+o(1))sqrt(K)n | Necessary rate test; no general scalar-growth theorem |
| Six finite completions | Exact table in §§7–9 | EXPERIMENTAL only; no exponents extrapolated |
| Fixed-carrier hierarchy | All stage output charges plus final remainder | Proved implication; useful stage premises OPEN |

No positive net exponent is obtained. Arithmetic/field/discriminant/
regulator/local-modulus/carry costs are inapplicable because no such
construction is used, not because an unknown cost has been assigned zero.

## 13. Implication for T01

**T01 remains OPEN.** The new proofs rule out broad invariant-orbit
certificates and quantified low-overlap chart libraries. They do not prove
a universal near-quadratic image theorem. The finite completions fail their
measured coverage gates and were not expanded.

All major new proofs were independently checked internally by a second
agent. This is separate from finite computation and byte integrity; no
external peer review or novelty claim is made. The unavailable historical
digital/rich-fiber originals remain unavailable and are not dependencies.
Other tracks and the separate quadratic branch remain unchanged.

## 14. Claim ledger

All entries are T01 / near-complete charts, fixed plus-sign cubic,
2026-09-30 v1. Exact quantifiers and hypotheses are at the named proof
sections; verification records internal audits and final source hashes.

| Claim | Status / evidence | Retained boundary |
|---|---|---|
| NC-C1 | PROVED, coverage companion; exact optimum at output budget k | Requires actual fibers, not a construction |
| NC-C2 | PROVED, coverage companion; full-image / near-full-subset / actual-tail equivalence | Tail witness OPEN |
| NC-H1 | PROVED, coverage companion; hierarchy cost and bounded-stage-fiber obstruction | Helpful stage premises unproved |
| NC-H2 | PROVED, coverage companion; overlap-sensitive support lower bound | Needs explicit per-chart fibers and overlap hypotheses |
| NC-R1 | PROVED, coverage companion; scalar-expansion capacity test | Does not force scalar expansion in all families |
| NC-A1/A2 | PROVED, orbit companion §§1–2; all-degree polynomial classification and finite invariant libraries | Orbit-certificate obstruction only |
| NC-A3 | PROVED, orbit companion §3; row/column classes and rational identities | Both-coordinate partial maps outside |
| NC-A4 | PROVED, orbit companion §4; exact arbitrarily long rational cycles | Only linear pair coverage |
| NC-A5 | PROVED, orbit companion §5; polynomial output relabeling | Invertible polynomial maps/common invariance required |
| NC-X1 | EXPERIMENTAL, six complete rational carrier audits | Finite range only |
| NC-O1 | OPEN, §16; actual small-fiber pair-mass tail | Equivalent reformulation of NR-O1 |

## 15. Failure and scope ledger

| Proposed shortcut | Disposition |
|---|---|
| Many polynomial preserving automorphisms create long finite invariant orbits | FAILED, even with growing degrees/count |
| A polynomial output relabeling can merge outputs under an automorphism | FAILED; output map must be affine and injective |
| Row-wise output preservation gives polynomially growing classes | FAILED; classes≤3 |
| The invariant affine-fiber obstruction covers all rational maps | FALSE; explicit Möbius m-cycles |
| A long rational cycle on one fiber suffices | FAILED coverage: Q=Theta(N) |
| Applying rules to every seed pair covers the expanded scalar square | FAILED inference; new cross-pairs must be counted |
| Geometric reduction of uncovered mass multiplies output savings | FAILED inference; every stage's outputs must be charged |
| J≈N bounded-degree charts automatically force quadratic image | NOT PROVED; output overlap is an additional hypothesis |
| High collision energy supplies an image upper bound | INVALID; never used |
| Finite near-quadratic images disprove all continuations of the tested formulas | NOT PROVED; only these finite completions audited |

## 16. Exactly one next proof obligation

**NC-O1 / OPEN — an actual cubic fiber-tail witness.**

Construct explicit arbitrarily large finite real A_N, |A_N|=N, and fixed
eta,gamma>0 such that
\[
\boxed{\#\{(x,y)\in A_N^2:
 |P^{-1}(P(x,y))\cap A_N^2|<N^\eta\}
 =O(N^{2-\gamma}).}
\]

Prove the distinct scalar count and the actual distinct returned-pair
multiplicities, including every exceptional pair. NC-C2 then gives
E_N as the union of all large fibers and a power saving for every
strictly smaller exponent than min(eta,gamma).

This is the same unresolved near-complete direct-support obligation NR-O1
in an equivalent, diagnostically sharper form. It does not impose a small
symmetry inventory or a particular chart class. Recording it launches no
further search.
