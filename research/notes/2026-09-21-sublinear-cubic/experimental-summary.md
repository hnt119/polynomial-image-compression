# New sublinear-inventory grid: exact finite results

T01, plus-sign cubic \(P(x,y)=(x-y)^3+x+y\), 2026-09-21 v1.

**SC-X1 — EXPERIMENTAL.** One predeclared, exact, offline grid evaluated
36 model records representing **35 distinct scalar carriers**, with six
inventories per model. The two `projection_q2` records coincide because
\(q+1=2q-1=3\) when \(q=2\); both records and their full costs are
retained. No previous grid was rerun. No result below is an asymptotic
construction or universal impossibility theorem.

The new source is `experiments/sublinear_cubic.py`; it reuses the inspected
fiber and graph functions in `experiments/growing_step_cubic.py`, without
calling that module's historical driver. The portable complete summary is
`examples/2026-09-21-sublinear-cubic.json`. Its machine claim identifier
`SL-X1` denotes this same finite experiment record.

## Fixed definitions and ranges

The list was approved before any full-square polynomial enumeration.
Every displayed range is inclusive at its stated endpoints.

| Class | Exact scalar construction | Six declared records |
|---|---|---|
| Multiscale and nonuniform mesh | \(i/q+j/(q^2+1)\), \(0\le i<q,0\le j<3\); separately \(1/j\), \(1\le j\le n\) | q=4,8,12; reciprocal n=8,16,24 |
| Nonfaithful rational projection | \((qi+aj)/q^2\), \(0\le i,j<2q\), a=q+1 or 2q−1 | q=2,3,4 and both a rules |
| Correlated sum/difference | \(u=j/q,-q\le j\le q;\ L=2r+u^2,0\le r<H\); put both \((L\pm u)/2\) into A | q=4,8,12; H=2,3 |
| Unequal-scale unions | \(\{j/n\}\cup\{c+j/(n^2+1)\}\cup\{-c+j/n^3\}\), \(0\le j<n\) | n=4,8,16; c=1 or n |
| Changing-scale completion | Start {0,1}; at each stage add all shifts \(0,(\tau-\tau^3)/2,-(\tau+\tau^3)/2\) | Three levels of each sequence (1/3,1/5,1/7) and (1/2,1/9,1/125) |
| Shared-anchor reverse fibers | \(a=k/q,0\le k<H;\ u=j/q,0\le j<4;\ z=u^3-u+2a\). Put both fiber coordinates at \(v=u+e/q\), e=−1,0,1, into A | q=3,5,7; H=2,3 |

The rational two-parameter projections are **not** genuine rank-two field
projections. Their formal relation identifies scalar parameters and cubic
coefficients. All actual scalar multiplicities are counted rather than
treated as compression of the Cartesian square.

These are varying-mesh, nonuniform, correlated, or changing-scale tests.
Their exact diameter, greatest affine-lattice mesh, and
\(D/(h^3N^2)\) are saved, so an escape from a previous theorem's
hypotheses is not silently assumed. The finite list alone makes no claim
that a rule continues outside an obstruction at all depths. In particular,
only three changing-scale stages were authorized and tested. There is no
ordinary-AP optimization, fixed-shift continuation, faithful-box search,
or arithmetic amplification in this grid.

## Inventories and bookkeeping

Each model supplies a basic step list before its fibers are known:

- Multiscale: \(1/q,1/(q^2+1)\); reciprocals: \(1/n,1/[n(n-1)]\).
- Projection: \(1/q,a/q^2\); correlated construction: \(1/q,2/q\).
- Unequal unions: \(1/n,1/(n^2+1),1/n^3\).
- Changing completion: the steps used through that level.
- Reverse fibers: \(1/q,2/q\).

For a requested cap, visit positive integer multiples of these basic steps
in rounds, preserving the displayed base order, discarding duplicates,
and stopping at the cap. This is a prescribed common inventory, not a
selection from successful return data. The three caps are
\(\lceil N^{1/6}\rceil,\lceil N^{1/2}\rceil,\lceil N^{2/3}\rceil\).
These give `construction_small`, `construction_sqrt`, and
`construction_two_thirds`.

Two additional **diagnostic** lists take the most frequent useful steps,
with caps \(\lceil N^{1/6}\rceil\) and \(\lceil\sqrt N\rceil\);
ties use increasing exact rational value. `all_useful_diagnostic` takes
every actual within-fiber difference. It reproduces the actual output
fibers by definition and is never claimed as a construction. Empty useful
inventories are recorded when the cubic is injective on the square.

Each list includes its cardinality, complete rational entries, denominator
and bit-size costs, useful edge count per step, and number of distinct
outputs reusing each step. Directed edges use positive difference increments;
each is one distinct undirected edge. Cycles are recorded separately from
the component reduction.

## Complete compact table

The table uses the prescribed `construction_two_thirds` inventory. Here
\(s=|P(A,A)|\), \(e\) counts distinct edges, \(V\) is nonisolated
pair mass, \(C\) counts components including isolated vertices, and
\(L_*\) is the maximum graph-component size. The portable JSON retains
all 216 graphs and their complete size distributions.

| Model | N | s | M | e | V | C | L_* |
|---|---:|---:|---:|---:|---:|---:|---:|
| multiscale_q4 | 12 | 144 | 6 | 0 | 0 | 144 | 1 |
| multiscale_q8 | 24 | 567 | 9 | 0 | 0 | 576 | 1 |
| multiscale_q12 | 36 | 1272 | 11 | 0 | 0 | 1296 | 1 |
| reciprocal_n8 | 8 | 64 | 4 | 0 | 0 | 64 | 1 |
| reciprocal_n16 | 16 | 256 | 7 | 0 | 0 | 256 | 1 |
| reciprocal_n24 | 24 | 576 | 9 | 0 | 0 | 576 | 1 |
| projection_q2_near | 14 | 170 | 6 | 32 | 46 | 170 | 3 |
| projection_q2_wide | 14 | 170 | 6 | 32 | 46 | 170 | 3 |
| projection_q3_near | 30 | 786 | 10 | 144 | 198 | 786 | 3 |
| projection_q3_wide | 33 | 951 | 11 | 183 | 231 | 951 | 3 |
| projection_q4_near | 52 | 2480 | 14 | 454 | 320 | 2480 | 6 |
| projection_q4_wide | 60 | 3296 | 16 | 608 | 446 | 3296 | 6 |
| correlated_q4_H2 | 13 | 155 | 6 | 15 | 27 | 155 | 3 |
| correlated_q4_H3 | 19 | 335 | 8 | 33 | 45 | 335 | 3 |
| correlated_q8_H2 | 25 | 591 | 9 | 40 | 59 | 591 | 3 |
| correlated_q8_H3 | 37 | 1304 | 12 | 95 | 103 | 1304 | 4 |
| correlated_q12_H2 | 36 | 1250 | 11 | 46 | 90 | 1250 | 3 |
| correlated_q12_H3 | 53 | 2717 | 15 | 92 | 161 | 2717 | 3 |
| unequal_n4_near | 12 | 140 | 6 | 0 | 0 | 144 | 1 |
| unequal_n4_far | 12 | 144 | 6 | 0 | 0 | 144 | 1 |
| unequal_n8_near | 24 | 568 | 9 | 0 | 0 | 576 | 1 |
| unequal_n8_far | 24 | 573 | 9 | 0 | 0 | 576 | 1 |
| unequal_n16_near | 48 | 2282 | 14 | 0 | 0 | 2304 | 1 |
| unequal_n16_far | 48 | 2288 | 14 | 0 | 0 | 2304 | 1 |
| changing_fresh_level1 | 6 | 28 | 4 | 10 | 14 | 28 | 3 |
| changing_fresh_level2 | 18 | 294 | 7 | 36 | 48 | 294 | 4 |
| changing_fresh_level3 | 54 | 2808 | 15 | 135 | 162 | 2808 | 5 |
| changing_powers_level1 | 6 | 28 | 4 | 10 | 14 | 28 | 3 |
| changing_powers_level2 | 18 | 294 | 7 | 36 | 48 | 294 | 4 |
| changing_powers_level3 | 54 | 2808 | 15 | 126 | 162 | 2808 | 5 |
| reverse_q3_H2 | 24 | 496 | 9 | 162 | 117 | 496 | 7 |
| reverse_q3_H3 | 29 | 723 | 10 | 262 | 167 | 723 | 7 |
| reverse_q5_H2 | 30 | 858 | 10 | 57 | 70 | 858 | 4 |
| reverse_q5_H3 | 40 | 1504 | 12 | 139 | 157 | 1504 | 4 |
| reverse_q7_H2 | 30 | 870 | 10 | 40 | 47 | 871 | 3 |
| reverse_q7_H3 | 40 | 1531 | 12 | 101 | 106 | 1533 | 5 |

## What the finite data show

The two changing-scale rules give the same recorded scalar counts and
actual images through the three levels:

\[
N=6,18,54,\quad s=28,294,2808,\quad
V=14,48,162,\quad L_*=3,4,5.
\]

The prescribed larger inventories already connect the actual fibers.
Their nonisolated fractions nevertheless fall from 7/18 to 4/27 to 1/18.
At the final level the 2916 pair vertices include 2754 singletons. Changing
the scales did not produce sustained coverage in these six finite records.
This observation does not prove a general changing-scale obstruction.

The reverse design `reverse_q3_H3` has N=29, actual image 723, and largest
fiber seven. Its ten-step construction list gives 262 edges and 167
nonisolated vertices, with components equal to the full actual fibers.
Only 39 of its 841 pairs lie in components of size at least
\(\lceil\sqrt{29}\rceil=6\). The coverage certificate is
\(841/6+(841-39)=5653/6\), exceeding the trivial square size. Reuse
is real but too sparse for this finite certificate. Its 72 coordinate
occurrences give 29 scalars; the exact ratio is 72/29, with the complete
projection fibers stored.

The largest rational projected box has 64 parameter points but 60 distinct
scalars, image 3296, and 446 pair vertices in nonsingleton actual fibers.
Its maximum fiber is six. The explicit inventory has 16 steps, only four
of which return a pair; they account for 608 edges but only 304 component
identifications. The projection multiplicity is fully charged. Tiny mesh
or a many-to-one scalar parameterization did not supply near-full coverage.

All three reciprocal carriers have injective full cubic images in this
finite range. The multiscale and unequal-union construction lists produce
no edges in the declared ranges, even though frequency-selected lists
detect some actual collisions. Thus the prescribed list and the diagnostic
list can behave differently; no successful diagnostic step is silently
added to a construction list.

For `reverse_q7_H2` and `reverse_q7_H3`, the largest prescribed inventory
leaves respectively one and two outputs split across multiple graph
components. Their component counts 871 and 1533 exceed actual image sizes
870 and 1531. All per-output component counts are retained in raw data.

## Geometry, projection fibers, and complete coverage

Every carrier record includes diameter, minimum scalar gap, difference-set
cardinality and its minimum positive gap, exact rational mesh, denominator,
height bounds, maximum and average actual output-fiber size, and the full
actual-fiber histogram. These are computed from the actual deduplicated
scalar set, not from parameter counts.

For example, the q4 wide projection has D=77/16 and
\(\eta=1/16\). The final fresh-prime completion has D=176/105 and
\(\eta=239/1157625\); the final power-denominator completion has
D=3643/2250 and \(\eta=1/1953125\). The q3,H3 reverse design has
D=73/27 and \(\eta=1/27\). These small gaps are recorded costs and
geometric parameters, not evidence for an asymptotic gain.

Scalar projection files map every exact scalar to all its parameter labels.
Correlated and reverse constructions also retain every distinct prescribed
(output,difference) pair and its parameter multiplicity. Every prescribed
pair is checked for actual membership and agreement with the complete
polynomial image enumeration. Incidental and cross-block ordered pairs are
included in that same enumeration; none is assigned an estimated output.

Raw graph records contain every component, every directed edge, and every
component's actual output index, including singleton vertices. The code
checks full square coverage, the image/component inequality, and direct
return-map agreement on three declared small cases. For a sorted carrier,
vertex (i,j) has index iN+j. These records allow graph and overlap counts
to be reconstructed without a new mathematical search.

## Budget, runtime, hashes, and verification

The allocation was 48 carriers, 288 graphs, at most 160 scalar inputs per
carrier, 1.5 million polynomial evaluations, 8 million charged checks, and
60 research CPU seconds. Input-only preflight found 36 records, 216 graphs,
maximum N=60, and exactly 37,243 full-square polynomial evaluations. The
preflight used 0.006970 CPU seconds and 1,981 constructor-record checks,
with no polynomial image evaluation.

The single research command was `python3 -m experiments.sublinear_cubic`,
using CPython 3.12.7 and standard-library `Fraction`, with no randomness,
network access, or new dependency. It completed all scheduled cases with
no error or resource stop in **1.290217 research CPU seconds**, 1.295039
wall seconds. The exact research work was:

| Category | Count |
|---|---:|
| Constructor records | 1,981 |
| Exact full-square polynomial evaluations | 37,243 |
| Within-fiber pair enumeration | 3,162 |
| Difference-pair checks | 37,243 |
| Difference-gap checks | 11,596 |
| Prescribed pair membership checks | 435 |
| Inventory edge-pool checks | 18,972 |
| Component vertex checks | 223,458 |
| Step/output reuse checks | 14,145 |
| Direct symmetry checks | 1,616 |
| Research total | 349,851 |

Every enumeration/check batch is reserved before execution. The separate
preflight does not assume how many collisions will occur; the incremental
cap stops before a batch that would exceed the allocation.

Five targeted tests passed in 0.028299 measured CPU seconds. They include
independent exact scalar/multiplicity oracles for the q2 projection and
q4,H2 correlated carrier; an explicit shared-anchor fiber chain plus direct
return-map comparison; declared-grid preflight; and restoration of engine
limits after an exception. Only the shared-anchor test enumerates a square:
576 polynomial evaluations and 3328 charged pair/edge checks. Test
constructor work is separately recorded as 4036 record checks. Including
the initial preflight, research, and this test run, this agent used
**37,819 polynomial evaluations and 359,196 charged checks**. Root's prime
audit and later repository regressions are separate work.

The ignored run directory is
`local-only/runs/T01/2026-09-21-sublinear-cubic/`. Its 36 complete carrier
files and 216 complete graph files all matched their stored SHA-256 hashes.
Source, imported graph-engine, and portable-summary hashes also matched.
This byte audit took 0.027176 CPU seconds; it was not a research or proof
rerun. The source hash is
`9960cbb165c2b992160a039618e72e9568b8f3b0687be8918fa9b6e0fcb15447`;
engine hash
`5f1c98f625ccfb30001a219973ba57b791c0c0c4fefb93a6dc8106df03065f45`;
portable hash
`426c27401a969e88089022e7f9ac8fc83cc6af776c8c784f74da6d575bfad2ae`.

`provenance.json`, `targeted-verification.json`, and
`artifact-verification.json` retain the full accounting. Existing root
`prime-audit.json` was preserved. The new writer rejects overwriting any
individual artifact. All new code and reused engine functions were read
before execution; the new tests were read before their run.
`git diff --check` passed. Full-suite verification is coordinated separately
by root; it is not claimed here.

## Claim scope and remaining limit

SC-X1/SL-X1 has track T01, branch “sublinear cubic”, the fixed polynomial
at the top, the explicit finite quantifiers above, and date/version
2026-09-21 v1. Evidence consists of exact full-square enumeration and
checked graph certificates, with source/hash provenance. Dependencies are
the frozen fiber-coordinate identity and the previously inspected exact
graph implementation. This task adds no independent universal proof audit
or literature/novelty claim.

These data exhibit bounded coordinate reuse and shared steps, but no
near-full polynomial-component coverage. They establish neither an
asymptotic carrier nor a stronger universal inventory obstruction. The
fixed cubic target and the unrestricted sublinear-inventory witness remain
**OPEN**.
