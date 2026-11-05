# Exact audit of the one varying-output frame family

T01 · 11 October 2026 · version 1 · offline.

**EXPERIMENTAL — VO-X1, exact and exhaustive in the stated finite scope.**
The approved family was evaluated once, for m=2,3,4 only. Its complete
same-set images have respectively 53, 122 and 223 values. Every ordered
pair was evaluated by two independent exact polynomial formulas. This
finite result is separate from the **PROVED** quadratic image lower
bound VO-C4, which already stops this particular unbounded extension.

The fixed target remains \(P(x,y)=(x-y)^3+x+y\). The compatibility
proof and quantitative statements are in
[compatibility.md](compatibility.md). The preserved evaluator is
[exact_audit.py](exact_audit.py), and every full output fiber is retained
in [exact-results.json](exact-results.json).

## 1. Proof audit and scope before execution

The independently inspected sources were the frozen TC-G2 frame identity,
TC-G5's endpoint conventions, and the complete new compatibility proof
VO-C1–VO-C5. The referee independently checked the positive-width branch
restrictions, the chosen endpoint equations, the isolating interval,
the two repeated pairs in each outer frame, the extension's exact input
and pair counts, the AP image obstruction, and the unequal-gap
contradiction. These checks found no gap in the saved proof.

The source allows all positive admissible short and long widths before
imposing the declared row-sharing rule. The short root is unique. The
other positive long-width branch is explicitly real and admissible, but
does not obey that row-sharing rule. It is not silently discarded as
complex. The s=0, h=s and repeated-column degeneracies are excluded.
The resulting eight-scalar seed is nonarithmetic and has two genuinely
new cross-block ordered pairs. These facts are symbolic conclusions,
not deductions from the finite evaluator.

An early referee message suggested an invalid irreducibility test modulo
3. It was immediately withdrawn, before any executable arithmetic or
saved evaluator depended on it. The final proof instead uses the exact
monic polynomial in §2 and the rational-root criterion. No modular
irreducibility test is used by the proof or program.

The lead read the complete evaluator before authorizing its one run.
Execution waited for the specialist's final claim-ID-only proof edit;
the mathematical content was unchanged by that edit. There was no
parameter sweep, numerical root computation, additional-frame
enumeration, package installation, network access, torsion computation,
or reuse of an imported research implementation.

## 2. Exact representation and independent target formulas

Use the unique root t of
\[
 64t^3-112t^2+52t-1=0,\qquad 1/50<t<1/49,
\]
and put \(u=4t\), \(h=\sqrt t>0\). The evaluator's coefficient field is
\[
 K=\mathbb Q[u]/(u^3-7u^2+13u-1),\qquad 2/25<u<4/49.
\]
The monic cubic can have only the rational roots +1 or -1, whose values
are 6 and -22. Hence it is irreducible and \(1,u,u^2\) is a faithful
basis. The root interval fixes the real embedding. Actual inputs and
outputs are represented as h times a coefficient vector in K. Since
h is nonzero, vector equality is exactly equality of real scalars.
There is no need to assume h belongs to K; the full scalar field has
degree at most six and is fixed before m grows.

In this representation,
\[
 \lambda=h^2=u/4,\quad \rho=\delta/h=2-u,
 \quad s/h=7-2u,\quad H/h=3-u,\quad S/h=5-u.
\]
The actual target is evaluated through the identity
\[
 P(ha,hb)/h=\lambda(a-b)^3+a+b.
\]
Thus the representation does not replace P by a scaled target polynomial.

The first oracle forms the difference cube using generic exact field
multiplication and polynomial long division. The second independently
expands \(a^3-3a^2b+3ab^2-b^3\) as an unreduced polynomial. It reduces
each power using its separately generated recurrence
\(u^j=7u^{j-1}-13u^{j-2}+u^{j-3}\). It calls none of the first oracle's
field multiplication or reduction routines. Every call to either oracle
is charged as one P evaluation.

For m short edges, the output labels are \(z_j=j\Delta\), 0≤j≤m.
All m short blocks are reconstructed and their scalar vectors deduplicated.
Every outer-frame scalar is then checked to be an existing short-block
scalar. Ordered pairs are deduplicated with their prescribed outputs
before evaluating the square. The m=2 presentation is the symmetric
seed from VO-C2 translated by 2δ in scalar space, giving output labels
0,Δ,2Δ. No actual scalar or output count changes under that translation.

## 3. Complete square counts and prescribed rows

Write \(N=|A|\), \(Q=|E|\), \(Z=|P(E)|\) and \(B=N^2-Q\), where E
is the prescribed pair union. The upper bound Z+B charges every
unprescribed pair. It is not automatically the actual image size.

| m | N | Q | Z | B | Safe upper Z+B | Actual full image |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 10 | 3 | 54 | 57 | 53 |
| 3 | 12 | 16 | 4 | 128 | 132 | 122 |
| 4 | 16 | 22 | 5 | 234 | 239 | 223 |

The recorded ratios are:

| m | 2Q/N | Q/Z | Q/N² |
|---:|---:|---:|---:|
| 2 | 5/2 | 10/3 | 5/32 |
| 3 | 8/3 | 4 | 1/9 |
| 4 | 11/4 | 22/5 | 11/128 |

For each prescribed output in increasing label order, the following lists
give its selected fiber mass and the numbers of selected columns in its
distinct first-coordinate rows. At each of these tested outputs, the
actual full-square fiber has exactly the selected mass. That last
observation is finite evidence only.

| m | Selected masses at z₀,…,zₘ | Column counts by selected row |
|---:|---|---|
| 2 | 3, 4, 3 | (3); (2,2); (3) |
| 3 | 3, 5, 5, 3 | (3); (2,3); (3,2); (3) |
| 4 | 3, 5, 6, 5, 3 | (3); (2,3); (3,3); (3,2); (3) |

The raw record retains all row and column indices. Scalar indices use
lexicographic coefficient order; they are not claimed to give real
numerical order. No floating-point sorting is used.

## 4. Full fiber histograms and finite tails

A histogram entry r:n means that n distinct full-image outputs each
have exactly r ordered pairs in their fiber.

| m | Complete fiber histogram |
|---:|---|
| 2 | 1:46, 2:4, 3:2, 4:1 |
| 3 | 1:110, 2:6, 3:4, 5:2 |
| 4 | 1:206, 2:8, 3:6, 5:2, 6:1 |

The weighted totals are 64, 144 and 256 ordered pairs. Their unweighted
totals are 53, 122 and 223 outputs. In particular the uncovered B pairs
are not all singletons: additional double and, for m≥3 in this table,
triple fibers occur away from the prescribed labels. They are all
included in the complete image and histogram.

For the strict small-fiber pair mass
\[
 T(K)=\sum_{z:\,r(z)<K}r(z),
\]
the saved thresholds are shown below. A dash means that the evaluator
did not record that threshold; no extra tail computation was run.

| m | T(1) | T(2) | T(3) | T(4) | T(5) | T(6) | T(7) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0 | 46 | 54 | 60 | 64 | — | — |
| 3 | 0 | 110 | 122 | 134 | 134 | 144 | — |
| 4 | 0 | 206 | 222 | 240 | 240 | 250 | 256 |

Every singleton, nonsingleton and ordered-pair representative is retained
in the JSON, not only these summaries. Neither these three image sizes
nor these finite tails certify an asymptotic rate.

## 5. The proof, rather than the scout, stops continuation

**PROVED — VO-C4, independently checked in this task.** The m upper
short-frame rows form an actual AP subset of Aₘ, with step D=2δ and
\[
 D^2=48t^2-36t+1=1-9u+3u^2.
\]
The value is irrational because u has degree three. The frozen GS-A4
argument applies to this same-set AP sub-square: equality of two outputs
forces equality of their integer differences and sums, hence equality
of the ordered pairs. Thus the AP alone contributes m² outputs and
\[
 |P(A_m,A_m)|\ge m^2=N^2/16
\]
for every m≥2. The finite evaluator merely reads this witness out of
its existing matrices, obtaining 4, 9 and 16 outputs without extra P
calls. It is not the evidence for the universal inequality.

The reviewed VO-C4 closure bound also prevents adding more complete conic
frames on these same scalar carriers from making the selected coverage
quadratic. In any such frame, with halfwidths a,b>0 and 3a²+b²=1,
\[
 |x-y|\le a+b\le2/\sqrt3
\]
for each of its pairs. The carrier is a union of four AP cosets of fixed
step D. From the isolated interval for t,
\[
 D^2=16t(1-2t)^2>
 \frac{17672}{60025}>\frac14.
\]
Hence D>1/2. For a fixed x, the possible partners lie in an interval of
length \(4/\sqrt3\). An AP coset contributes at most
\(\lfloor(4/\sqrt3)/D\rfloor+1\le5\) such partners, so all four
cosets contribute at most 20. Therefore any union of these frame pairs
inside the existing Aₘ has at most 20N pairs. No additional frames were
enumerated to obtain this deterministic bound.

This last statement concerns selected frame coverage; the AP sub-square
is the separate actual-image lower bound. Neither statement excludes a
different varying-output construction with different endpoint roles or
different scalar carriers.

## 6. One command, budget, runtime and preservation

The lead-authorized invocation, run exactly once from the repository
root, was:

```text
python3 local-only/runs/T01/2026-10-11-varying-output-frames/exact_audit.py --compatibility-proof research/notes/2026-10-11-varying-output-frames/compatibility.md
```

It exited with code zero under Python 3.12.7. The result records CPU
time 0.130858 seconds and wall time 0.13095925003290176 seconds. All
assertions passed. There was no failed run or rerun. Subsequent copying,
JSON inspection and hashing did not evaluate P or execute the evaluator.

| Resource | Declared ceiling | Actual use |
|---|---:|---:|
| Justified finite instances | 6 | 3: m=2,3,4 |
| Combined exact predicates and P calls | 5,000 | 1,530 |
| P calls, included in combined ceiling | — | 928: 464 per oracle |
| Explicit checked predicates, included in combined ceiling | — | 602 |

The 464 distinct cells are 8²+12²+16². The 602 predicates include
464 oracle agreements, 48 selected-pair output checks, and the explicit
frame, deduplication, row-count, full-square, histogram and ledger
assertions. These are counted mathematical predicates, not every
rational addition or multiplication performed internally. The complete
category breakdown is in the JSON.

| Frozen item | SHA-256 |
|---|---|
| Compatibility proof at release | `885cfb686b97849391c8337720b15053d7b0357a72fbf972ce393a14381b6658` |
| Reviewed evaluator | `4a302ba39559025da98f4fa1b8d5de48ca7cbb04709e1281f7783a4ac822322c` |
| Complete result JSON | `aac500eaa66bcd5f4c4049a83d636aad15f40589af688b956b97e1fd8e1230bb` |

The original executable and results remain in the ignored local run
directory. Byte-identical copies were placed beside this appendix for
portable review. The archived proof and all earlier research outputs
were preserved. The referee did not run a new test suite; the lead
records the repository's required baseline validation separately.

## 7. Claim record and retained scope

| Record item | Scope |
|---|---|
| Claim, track, polynomial | VO-X1; T01; \((x-y)^3+x+y\) |
| Date/version | 2026-10-11, version 1 |
| Quantifiers | Only m=2,3,4 of the one fixed isolated-root family; every ordered pair in each actual same-set square |
| Dependencies | VO-C1–VO-C5 for compatibility and family definitions; the irreducible monic coefficient polynomial and specified real embedding |
| Evidence | Exact finite arithmetic, exhaustive in this scope, with two independent target formulas and retained complete fibers |
| Audit performed | Referee independently checked the saved compatibility proof; lead inspected the complete evaluator before its release; referee inspected the saved results and provenance after the one run |
| Gaps and limits | No finite-to-asymptotic inference, no other endpoint-role classification, no extra-frame search, no new carrier, and no unrestricted T01 impossibility claim |

The finite triangle succeeds as a three-output endpoint junction. Its
specified extension fails the power-saving objective by the proved
quadratic image lower bound, independently of the scout. The unrestricted
same-set T01 target remains OPEN. This audit adopts no separate next
obligation and authorizes no continuation of the finite search.
