# Exact growing-step diagnostics

T01, fixed polynomial \(P(x,y)=(x-y)^3+x+y\), 2026-09-21 v1.

**GS-X1 — EXPERIMENTAL.** This is one exact, deterministic finite run of
32 explicitly specified carriers and six inventories per carrier. It does
not establish an asymptotic construction, image lower bound, or universal
obstruction. Every count includes all ordered pairs of the actual scalar
carrier. The reusable source is `experiments/growing_step_cubic.py`; the
portable results are `examples/2026-09-21-growing-step-cubic.json`.

## Declared finite range

The grid was fixed and approved before execution:

1. \(h\{0,\ldots,n-1\}\), \(h=1,1/3\),
   \(n=8,16,32,64,128\): ten carriers.
2. \(h([0,n-1]\cup[3n,4n-1])\), \(h=1,1/3\),
   \(n=4,8,16\), integer interval notation: six carriers.
3. \(\{i+w j:0\le i,j<L\}\), \(L=4,8\),
   \(w=3/2,5/3,L+1/3\): six coefficient boxes. Input coincidences
   are removed before either coordinate is counted.
4. \(\{j^2:0\le j<n\}\) and
   \(\{(j^3-j)/2:0\le j<n\}\), \(n=16,32\): four carriers.
5. All two coordinates of \((z,u)=(2k,j)\),
   \(0\le k<M,-L\le j\le L\), for
   \((M,L)=(2,4),(4,4),(2,8),(4,8)\): four planted carriers.
6. Starting from \(G=\{j/3:0\le j<6\}\), take two successive
   scalar completions \(A\mapsto A+\{0,-1,4/27,-5/27\}\).
   These add the two coordinates of \(T_1(t,t)\) and
   \(T_{1/3}(t,t)\), while retaining \(t\): two carriers.

Each carrier has the six inventories below. All steps are positive;
opposite signs and repeated edges are not double counted. Write
\(k=\lceil N^{1/6}\rceil\), \(l=\lceil\sqrt N\rceil\).

| Inventory label | Exact definition |
|---|---|
| `integer_small` | \(\{1,\ldots,k\}\) |
| `integer_sqrt` | \(\{1,\ldots,l\}\) |
| `third_sqrt` | \(\{j/3:1\le j\le l\}\) |
| `frequent_small` | First \(k\) useful positive steps, ranked by actual edge count |
| `frequent_sqrt` | First \(l\) useful positive steps, ranked by actual edge count |
| `all_useful_diagnostic` | Every positive difference between vertices of one actual fiber |

Ranking ties use increasing exact rational step. Fewer than the requested
number are used if fewer useful steps exist. An empty inventory is valid
when there are no collisions. Every inventory's complete list, common
denominator, numerator/denominator bit bounds, and serialized length are
recorded. Exact duplicate inventory/model records remain separate.

The last inventory connects every actual fiber by definition. Its equality
of component count and image size is a diagnostic identity, not an
independently useful image certificate. It is charged in full. The other
frequency-selected inventories also use knowledge of actual fibers;
finite success does not give an independently specified growing rule.

## Compact results

The table uses `frequent_sqrt`. Here \(s\) is the actual full image size,
\(e\) is the number of distinct undirected edges, \(V\) is nonisolated
pair mass, \(C\) counts all graph components, and \(L_*\) is the largest
component. The final column is the size of the all-useful inventory. All
192 cases, not only these rows, are in the portable JSON.

| Carrier | N | s | M | e | V | C | L_* | M_all |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Integer AP 8 | 8 | 44 | 3 | 36 | 28 | 44 | 4 | 3 |
| Integer AP 16 | 16 | 196 | 4 | 126 | 82 | 196 | 5 | 4 |
| Integer AP 32 | 32 | 848 | 6 | 462 | 232 | 848 | 7 | 6 |
| Integer AP 64 | 64 | 3580 | 7 | 1630 | 666 | 3580 | 8 | 7 |
| Integer AP 128 | 128 | 14890 | 9 | 5644 | 1926 | 14890 | 10 | 9 |
| Third AP 8 | 8 | 38 | 2 | 30 | 48 | 38 | 3 | 2 |
| Third AP 16 | 16 | 168 | 3 | 132 | 134 | 168 | 4 | 3 |
| Third AP 32 | 32 | 746 | 4 | 530 | 384 | 746 | 5 | 4 |
| Third AP 64 | 64 | 3258 | 5 | 1996 | 1106 | 3258 | 6 | 5 |
| Third AP 128 | 128 | 13906 | 6 | 7130 | 3220 | 13906 | 7 | 6 |
| Two integer blocks, n4 | 8 | 50 | 3 | 20 | 22 | 50 | 3 | 3 |
| Two integer blocks, n8 | 16 | 212 | 4 | 76 | 64 | 212 | 4 | 4 |
| Two integer blocks, n16 | 32 | 846 | 6 | 316 | 274 | 846 | 5 | 6 |
| Two third blocks, n4 | 8 | 52 | 1 | 12 | 24 | 52 | 2 | 1 |
| Two third blocks, n8 | 16 | 202 | 3 | 62 | 100 | 202 | 3 | 3 |
| Two third blocks, n16 | 32 | 800 | 5 | 334 | 350 | 800 | 4 | 5 |
| Box L4, w3/2 | 14 | 164 | 3 | 54 | 46 | 164 | 4 | 3 |
| Box L4, w5/3 | 16 | 192 | 3 | 92 | 104 | 192 | 4 | 3 |
| Box L4, w13/3 | 16 | 230 | 4 | 38 | 42 | 230 | 4 | 4 |
| Box L8, w3/2 | 34 | 1002 | 4 | 310 | 222 | 1002 | 5 | 4 |
| Box L8, w5/3 | 49 | 1879 | 4 | 1142 | 703 | 1879 | 5 | 4 |
| Box L8, w25/3 | 64 | 3877 | 4 | 347 | 342 | 3877 | 4 | 4 |
| Squares n16 | 16 | 253 | 2 | 3 | 6 | 253 | 2 | 2 |
| Squares n32 | 32 | 1021 | 2 | 3 | 6 | 1021 | 2 | 2 |
| Cubic coordinate n16 | 15 | 225 | 0 | 0 | 0 | 225 | 1 | 0 |
| Cubic coordinate n32 | 31 | 961 | 0 | 0 | 0 | 961 | 1 | 0 |
| Planted M2, L4 | 28 | 694 | 6 | 184 | 126 | 696 | 9 | 8 |
| Planted M4, L4 | 44 | 1706 | 7 | 544 | 316 | 1706 | 9 | 8 |
| Planted M2, L8 | 60 | 3426 | 8 | 410 | 250 | 3430 | 17 | 16 |
| Planted M4, L8 | 108 | 11064 | 11 | 1548 | 820 | 11076 | 17 | 16 |
| Completion level 1 | 16 | 192 | 4 | 102 | 96 | 192 | 5 | 6 |
| Completion level 2 | 30 | 740 | 6 | 389 | 214 | 740 | 8 | 7 |

Within these finite data, `frequent_sqrt` connects complete actual fibers
in 29 of 32 carriers. The other three retain respectively 2, 4, and 12
extra components for planted (M,L)=(2,4),(2,8),(4,8). The graph records
retain each component's actual output, so this loss is not inferred from
edge count or energy.

For every tested full integer or third AP, `integer_small` already attains
the actual image component count. Additional edges only add cycles inside
already connected fibers. The finite record is consistent with the separate
progression proof; the numerical check does not prove that theorem.

The largest planted example has four components of size 17. Together they
contain just 68 of 11664 ordered pairs, fraction 17/2916, and their
pair/scalar reuse ratio is 17/27. Total nonisolated mass is 820/11664.
The two completions have nonisolated fractions 3/8 and 107/450; their
frequency-selected step lists are respectively
\(\{1/3,2/3,1,5/3\}\) and
\(\{1/3,2/3,1,4/3,5/3,2\}\). Components of size at least
\(\lceil\sqrt N\rceil\) contain 53/256 and 56/900 of their squares.
Their direct coverage certificates \(N^2/K+B\), namely 267 and 994,
even exceed the corresponding square sizes 256 and 900. Long components
exist, but their uncovered pair costs dominate these certificates.

## Reproducibility, work ledger, and verification

The reviewed source ran once with
`python3 -m experiments.growing_step_cubic`, under CPython 3.12.7.
Arithmetic is standard-library `Fraction`; no network, randomness, external
dependency, inherited-grid rerun, or follow-up carrier search was used.
The source refuses to overwrite an existing raw research directory.

| Charged research work | Count |
|---|---:|
| Exact scalar polynomial evaluations | 76,303 |
| Within-fiber unordered pair enumeration | 23,910 |
| Inventory edge-pool checks | 143,460 |
| Component vertex checks | 457,818 |
| Direct return-map membership checks | 768 |
| Total | 702,259 |

The predeclared allocation was at most 60 carriers, 200 cases, 128 actual
inputs per carrier, 2,000,000 checks, and 60 research CPU seconds. Actual
use was 32 carriers, 192 cases, maximum input count 128, 2.232581 CPU
seconds and 2.242286 wall seconds. All scheduled cases completed; no
resource stop or execution error occurred. Batch checks are reserved before
execution, and CPU limits are checked during enumeration and between cases.

The ignored directory
`local-only/runs/T01/2026-09-21-growing-step-cubic/` contains 32 complete
carrier certificates and 192 complete graph certificates. Carrier files
include every exact output, its differences and vertex identifiers, and a
complete ordered-pair-to-output table. Graph files include every edge,
component, component-output assignment, higher component-size mass, and
number of components for each output. Vertex `(i,j)` has identifier
`i*N+j` in the listed sorted scalar carrier. Thus all coverage and overlap
counts can be reconstructed from saved records without new polynomial
enumeration. All 224 stored raw hashes, the source hash, and the portable
summary hash were checked and matched. That byte audit used 0.044483 CPU
seconds and was not a mathematical rerun.

Four initial targeted tests passed in a reported 0.004 seconds. They test
the six-point full-fiber oracle, the concrete subgroup-coset counterexample,
the all-useful diagnostic, and the declared grid limits. A separately
requested fifth test adds two independent faithful-box numeric oracles:
rank2/side3 gives `(N,s,nonisolated,max)=(9,69,21,3)`, and rank3/side2 gives
`(8,56,16,2)`. In both, the single-step graph already has the full image
component count and agrees with direct return-map membership. All five
tests passed in a reported 0.007 seconds. These five tiny oracle carriers
are verification inputs, not extra research-grid candidates. The first
test run charged 264 checks/61 polynomial evaluations; the second charged
745 checks/206 evaluations. Combined research plus these verification runs
therefore used 703,268 checks and 76,570 polynomial evaluations.

The original research provenance remains unchanged. `verification.json`
records the initial checks; `verification-box-oracles.json` records the
additional test run and combined work. Root's later full-suite checks are
separate. `git diff --check` passed after code generation.

## Claim and audit scope

GS-X1 is exact finite evidence with quantifiers restricted to the declared
grid, source version/hash in saved provenance, and dependencies consisting
of the stated polynomial, explicit carrier definitions, and the frozen
fiber-coordinate identity. The complete code and initial tests were read
before first execution. The later faithful-box test was also read before
execution. Numerical tests do not independently prove any asymptotic claim.

A separate read-only symbolic audit in this task inspected
`structure-and-reuse.md` GS-P1/P2: edge uniqueness, sign convention,
component and spanning-forest inequalities, exceptional-pair coverage,
the 1/5 inventory constant, and the exact counterexample. No gap was found.
It also inspected `multistep-bounds.md` GS-U1–U3: return-to-parabola
normalization and injectivity, primal and dual two-intersection conditions,
constants and the stated inventory range, distinct-difference separation
versus scalar spacing, the complete nonsingleton-fiber band, and the
lattice-mesh substitution and asymptotic regime. No gap was found in that
scope. The frozen crossing lemma and one-step theorem were dependencies,
not reproved during this cycle. These are internal audits, not external
review or novelty checks.

The unrestricted growing-step construction remains OPEN. This bounded
run supplies neither near-total polynomial-component coverage nor an
asymptotic exclusion outside the separately proved carrier regimes.
