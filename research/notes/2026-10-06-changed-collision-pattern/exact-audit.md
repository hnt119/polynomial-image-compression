# Exact audit of the stopped conic-frame ladder

T01, 2026-10-06, version 1. Fixed polynomial
\(P(x,y)=(x-y)^3+x+y\). Claim **CP-X1 — EXPERIMENTAL**:
exhaustive exact evaluation of every ordered pair for precisely the three
frozen ladder lengths \(m=1,2,3\). This is a finite validation of
[CP-C1–CP-C4](construction.md), whose symbolic proofs are independent of
the run. It is not an experiment on the next obligation CP-O1.

## 1. Proof before enumeration and audit scope

The referee completed [CP-R1](rigidity.md) from the old VG-O1 equations
and the user's supplied outline, checking the exact indices, signs,
positive-root classification, decrement and finite boundaries. The lead
independently inspected the complete saved proof. No separate progress
report was located or claimed read.

The initial same-center reverse-chain draft was never executed. Before
any carrier evaluation, the final candidate became the exact nonconcentric
bridge and its fixed-width ladder. The referee read the saved CP-C1–CP-C4
proof in full and independently checked both directions of compatibility,
the real root specification, bridge signs, scalar order and distinctness,
all endpoint identifications, exact selected fibers, block accounting,
and the irrational-spacing sub-square obstruction. The lead separately
inspected these proofs and then the entire replacement evaluator and test
source before releasing one run. These are internal audits, not external
review or a literature/novelty check.

The actual-image bound \(|P(A_m,A_m)|\ge N^2/4\) was proved before
enumeration. It stopped the fixed-width extension. The finite audit was
reduced to the single frame, six-point bridge and one attachment; sizes
\(m=4,8\) and the reverse-chain draft were removed before any run.
No other candidate, parameter sweep, numerical root search, network,
package installation, arithmetic tower or next-lemma search occurred.

Two interpretive pitfalls were checked explicitly. Distinct symbolic
frame labels do not imply distinct scalars or pairs, so actual coefficients
were deduplicated. A poor selected-pair certificate alone is not an
actual-image lower bound: CP-C4 supplies that lower bound separately,
through an injective progression sub-square.

## 2. Faithful exact arithmetic and two independent evaluators

The real parameters are specified by
\[
f(t)=64t^3-80t^2+28t-1=0,\qquad 0<t<1/12,\qquad h=\sqrt t>0.
\]
Modulo 3, \(f\) is \(T^3+T^2+T+2\), whose three values are
\(2,2,1\). Thus \(f\) is irreducible over \(\mathbb Q\), and
equality of rational degree-at-most-two representatives modulo \(f\)
is exactly equality at the specified real \(t\). No approximate real
embedding is used.

Every input is \(hA(t)\), with \(A\) linear, and
\[
P(hA,hB)/h=t(A-B)^3+A+B.
\]
Because \(h>0\), its common factor does not change equality. The
program stores the exact rational coefficients of \(1,t,t^2\).
There is no need to infer a minimal polynomial for \(h\).

The first evaluator forms the difference cube using generic exact field
multiplication, reducing by polynomial long division after each product.
The second expands \(A^3-3A^2B+3AB^2-B^3\) before reduction and uses
the independently displayed fixed power table
\[
t^3=\frac1{64}-\frac7{16}t+\frac54t^2,\qquad
t^4=\frac5{256}-\frac{17}{32}t+\frac98t^2.
\]
The second evaluator calls neither generic field multiplication nor long
division. Both are charged as separate evaluations of \(P\).
They agreed on all 116 cells. Complete square values are cached; selected
labels, progression injectivity, histograms and tails use that cache and
do not trigger extra polynomial evaluations.

The actual scalar order is the order proved in CP-C3. Lexicographic
coefficient order is used only to serialize output records, never as a
claim about the order of the corresponding real numbers.

## 3. Complete-square results

Here \(N=|A_m|\), \(Q=|E_m|\), \(Z=|P(E_m)|\), and
\(B=N^2-Q\). Each histogram entry \(r:n_r\) means exactly \(n_r\)
complete output fibers have \(r\) ordered pairs.

| \(m\) | \(N\) | \(Q\) | \(Z\) | \(B\) | Safe upper \(Z+B\) | Actual full image | Complete fiber histogram |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 4 | 4 | 2 | 12 | 14 | 14 | \(1:12,\ 2:2\) |
| 2 | 6 | 8 | 3 | 28 | 31 | 29 | \(1:24,\ 2:4,\ 4:1\) |
| 3 | 8 | 12 | 4 | 52 | 56 | 52 | \(1:44,\ 2:6,\ 4:2\) |

The program deduplicated actual endpoints and ordered pairs. No scalar,
diagonal, reverse pair or distant-frame pair was excluded. The counted
pair masses are respectively \(16,36,64\). Complete output identities
and all pair representatives are retained in the raw files.

| \(m\) | \(2Q/N\) | \(Q/Z\) | \(Q/N^2\) | Selected fibers | Cross-frame repeated-output pair mass |
|---:|---:|---:|---:|---|---:|
| 1 | 2 | 2 | \(1/4\) | \(2:2\) | 0 |
| 2 | \(8/3\) | \(8/3\) | \(2/9\) | \(2:2,4:1\) | 4 |
| 3 | 3 | 3 | \(3/16\) | \(2:2,4:2\) | 8 |

The disjoint partition consists of the \(m\) two-point source blocks
and two boundary singletons. Its total within-block pair count is
\(4m+2\), giving \(6,10,14\); the complementary cross-block counts
are \(10,26,50\). Every selected pair is cross-block and the selected
local count is zero. The last column above counts a subset of those same
selected pairs, not additional pairs or another saving.

Define the strict small-fiber tail by
\[
T_m(K)=\sum_{z:\,|P^{-1}(z)\cap A_m^2|<K}|P^{-1}(z)\cap A_m^2|.
\]
Every integer threshold \(1\le K\le N+1\) is saved. The full tail
functions in this finite range are already determined by:

| \(m\) | \(T_m(1)\) | \(T_m(2)\) | \(T_m(3)=T_m(4)\) | \(T_m(K), K\ge5\) | \(K=\lceil\sqrt N\rceil\) | \(T_m(K)\) there |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 12 | 16 | 16 | 2 | 12 |
| 2 | 0 | 24 | 32 | 36 | 3 | 32 |
| 3 | 0 | 44 | 56 | 64 | 3 | 56 |

The plus-sign progression sub-squares have \(4,9,16\) distinct outputs,
matching the proved \((m+1)^2\) count. The finite full histograms do
not imply a formula for all \(m\); no such inference is made.

## 4. Worked exact bridge, including incidental complete-square repeats

Put
\[
a=h(1-4t),\quad b=h(3-4t),\quad d=h(7-12t),\quad r=h(4t-2).
\]
The six-point bridge is \(A_2=\{-d,-b,-a,a,b,d\}\). The following
table lists **all** its nonsingleton complete fibers, not only the
prescribed classes. The first three rows are the prescribed classes;
the last two arise from unprescribed pairs and are recorded by the full
enumeration.

| Output | Exact ordered-pair representatives | Pair count |
|---|---|---:|
| \(-4r\) | \((b,-b),(b,d)\) | 2 |
| \(0\) | \((a,-b),(a,d),(-a,b),(-a,-d)\) | 4 |
| \(4r\) | \((-b,b),(-b,-d)\) | 2 |
| \(4h\) | \((b,-a),(b,a)\) | 2 |
| \(-4h\) | \((-b,-a),(-b,a)\) | 2 |

These are five distinct outputs. The remaining 24 ordered pairs have
24 different singleton outputs, producing the total 29. This finite
check both confirms the four-pair zero fiber joining two centers and
shows why the safe upper certificate 31 is not an exact image formula.

For a complete worked matrix as well, the \(m=1\) scalars in increasing
order are \((-b,a,b,d)\). The exact matrix \(P(x,y)/h\), with rows
and columns in that order, is
\[
\begin{pmatrix}
-6+8t&-4&-8+16t&-36+176t-192t^2\\
0&2-8t&4-16t&0\\
8-16t&4&6-8t&8-16t\\
44-192t+192t^2&16-32t&12-16t&14-24t
\end{pmatrix}.
\]
Irreducibility makes comparison of these reduced polynomials exact. The
two repeated values are \(0\) and \(8-16t=-4r/h\), each twice;
the remaining 12 values are distinct.

## 5. Released command, costs and reproducibility

The source was inspected before this command ran, once:

```text
python3 -m experiments.changed_collision_pattern --proofs research/notes/2026-10-06-changed-collision-pattern/rigidity.md research/notes/2026-10-06-changed-collision-pattern/construction.md
```

Python 3.12.7; exit code 0; no error or rejected assertion. Recorded
process CPU time was 0.024280 seconds and wall time 0.024591 seconds.
There is no random seed because no randomness is used.

| Budget item | Declared ceiling | This one research run |
|---|---:|---:|
| Finite instances | 8 | 3 |
| Exact \(P\) evaluations | 30,000 | 232 |
| Compatibility/accounting checks | 10,000 | 233 |

The 232 evaluations comprise 116 calls to each evaluator. The 233 checks
comprise 116 oracle agreements; 24 pair-dedup checks; 24 partition checks;
24 prescribed-output checks; 12 endpoint-gluing checks; and 33 further
compatibility, count, histogram and sub-square checks. Full per-category
counters are saved in the provenance JSON.

The companion tests contain eight additional evaluations on the four
already-used seed pairs, using both formulas. They add one repeated seed
instance, four charged identity checks and seven unittest assertions.
The referee did not run them. The lead ran the complete repository suite
once: all 100 tests passed, including these three new tests; the existing
fixed verification also passed all 159 cases. Counting every new test
assertion conservatively gives combined totals of four instance visits,
240 evaluations and 244 checks. The global ceilings were not changed.
Existing fixed repository regressions are separate software validation,
not additional research searches. Full check commands and outcomes are
recorded in [verification.md](verification.md).

Only JSON inspection and hashing followed the run; no \(P\) evaluation
was repeated. There was one unsuccessful file-replacement patch during
source preparation, which failed before modifying a file; it was not a
program execution, mathematical failure or consumed research instance.

The following hashes identify the exact released input and evidence:

| Artifact | SHA-256 |
|---|---|
| `rigidity.md` at release | `6061ea56c6f2d22d4d99887197ce6b762f0b154fd973dbb1df2f2e3d41c6975d` |
| `construction.md` at release | `a534dee8246cc2c71a580e1c136ef169df35511142bddd131a65d30df41ad30b` |
| `experiments/changed_collision_pattern.py` | `50c3b2ee6892718ac2e17346a01d827dce5b43c743bbf18bd5ec74da552b7f33` |
| `tests/test_changed_collision_pattern.py` | `0b4d69944039292e62848cca0074ba06ca71c5fa1c737a44c179510c2ff0605a` |
| Canonical JSON input descriptor | `d5a4e5aeaa6614a6858850ab18860b73476eae3a7226c826d31433fda3f27abf` |
| Portable data | `82a5dd82ab93158b6db0b4e094ca06e2000d01a930f8ab75f2cc281c349d4e4f` |
| Raw \(m=1\) | `ac5b3763c16d80ccadcffa53b3f3d603bdc1dcd44970a991330e8b26bc68a6f7` |
| Raw \(m=2\) | `683b15f719cb3b649fcb3b7208c25a32a08895f4b4383ce94a33adc6ced5fa85` |
| Raw \(m=3\) | `2bc47c5d96b03639f73da89b39ebaaba94d8581e1aeb849b2a2fbc1cc3b3c2ff` |
| Raw `experiment-provenance.json` | `98741e8bf612d839f9ff83e8b5753d362d9407c468fff2cf25beb0c85ccfd453` |

The raw paths are
`local-only/runs/T01/2026-10-06-changed-collision-pattern/conic_ladder_m{1,2,3}.json`
and `experiment-provenance.json` in the same directory. They retain every
actual scalar, selected pair label, complete fiber and ranked fiber size.
Portable summary data are in
`examples/2026-10-06-changed-collision-pattern.json`.

## 6. Claim record and limits

| Item | Record |
|---|---|
| Claim | CP-X1 |
| Track, polynomial, date/version | T01; \((x-y)^3+x+y\); 2026-10-06 / 1 |
| Quantifiers | Exactly \(m=1,2,3\) of the fixed CP-C3 ladder, all \(A_m^2\) ordered pairs |
| Hypotheses | The specified positive real cubic root, fixed \(h,r,s\), actual scalar union and prescribed pair rule in construction.md |
| Dependencies | CP-C1–CP-C4 for compatibility, faithful root representation and the independent asymptotic stopping proof |
| Evidence type | EXPERIMENTAL, exact and exhaustive over the stated finite squares; two separately implemented polynomial formulas |
| Inspection | Lead inspected complete code/tests before release; referee inspected all summary results, all nonsingleton fibers and the worked matrix after execution |
| Retained boundary | No all-length histogram formula, useful power saving, other carrier, variable-width extension or CP-O1 answer is claimed |

The finite bridge is compatible and nonarithmetic. Its fixed-width ladder
has a proved quadratic actual-image lower bound, so it is a **FAILED**
power-saving family in that exact scope. The unrestricted T01 construction
target remains **OPEN**. This appendix introduces no independent next
obligation and does not replace the report's single CP-O1.
