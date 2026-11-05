# Verification and provenance

T01 elliptic geometry cycle, 2026-09-30. Fixed polynomial
P(x,y)=(x-y)³+x+y. This record concerns the newly commissioned research;
it does not describe documentation checks as a proof audit.

## Mathematical review performed

The lead read the complete three proof companions and checked the arguments,
rather than relying on their summaries or agent agreement.

| Claims | Located proof and dependencies | Internal audit performed |
|---|---|---|
| EG-G1 | genus.md §1; explicit affine and projective maps | Checked inverse maps, cusp orders and collision-variety isomorphism |
| EG-G2 | genus.md §§2–3; derivative tests, irreducibility, local normalization, covering Euler characteristic | Checked every complex critical-value case, infinity and node corrections |
| EG-G3 | genus.md §§2,4; exact quartic comparison | Checked sign reduction, seven critical values, no line/conic factors for c≠0, genus-one zero component, genus-two nodal normalization |
| EG-G4 | genus.md §5; proved ramification formula | Checked source/target genus inequalities and existence of real affine arcs; no real-point scarcity inferred |
| EG-B1–B2 | group-law.md §§1–3; meromorphic poles and finite maps | Checked symmetric/diagonal cases, mixed poles, isogenies and the extension to independent finite covers, including ramification |
| EG-B3–B4 | group-law.md §§4–5; zero/pole counts | Checked exact row pole degree, exceptional-row bound, scalar multiplicity and chart-library costs |
| EG-B5–B6 | group-law.md §§6–7; swapped-label counts | Checked noninjective projection caveats and the real cube-injectivity step |
| EG-C1 | complex-extensions.md first claim; exact substitutions | Checked inverse, discriminant, j values, real excluded points |
| EG-C2 | complex-extensions.md second claim; chord law and displayed local formal logarithm | Checked rational point arithmetic, prime 227, negative valuation, convergence and nonzero logarithm; no rank computation |
| EG-C3–C4 | complex-extensions.md final claims | Checked complex automorphism reality, embedding transport, trace corrections and the same-square real-part classification |
| EG-L1 | construction-ledger.md, construction section; EG-G2, EG-C2 | Lead proved endpoint/pair projection counts; geometry specialist independently checked degree nine, m/9≤N≤3m and Q≤2N |
| EG-X1 | experiments/elliptic_geometry.py and saved exact run | Inspected new code before execution; checked explicit independent point/inverse-map oracles and all-pair histogram totals |
| EG-O1 | README.md §7; retained NC-C2 and NC-O1 | OPEN witness, restated in shared-endpoint coordinates; no new narrower reduction claimed |

The geometry specialist also reviewed the main report and ledger. The lead
applied its clarifications about the nonsingular elliptic condition and the
unchanged scope of the next obligation. An initial proposed scalar version
of the sum bound was restricted to injective projections before reporting:
multiple parameter representatives can realize opposite orientations with
different sums. The full companion retains the correct multiplicity version.

These are internal mathematical audits, not external review or literature
verification. Standard complex-curve and elliptic group-law foundations are
stated where used; the genus covering calculation and local formal-log
argument are supplied explicitly. The fixed T01 target remains OPEN.

## Exact computation and budget

Command: python3 -m experiments.elliptic_geometry.
Python 3.12.7, standard library fractions.Fraction, no network, no randomness.
Eight selected candidate sets; every ordered pair of each resulting scalar
set was evaluated exactly. The program used 1,444 P evaluations and 104
charged curve/accounting checks. No specialist ran an additional search.

New unit regressions use 29 more P evaluations, for 1,473 this cycle.
This is below the announced 12-candidate, 100,000-evaluation,
20,000-symbolic/curve-check ceiling. Existing regression programs are
unchanged finite checks and are not additional research searches.

Code SHA-256:
b094614b8c9cf6a0195e86f90df39023361442e06bcb560839eec7306d7f33bb

Input SHA-256:
9158e8997bfc7f47a091c0c318640209eb58ae70827e70037feb45afe35df53c

Portable result SHA-256:
a6375a6c28f8d84b7496d33b5abe16a6f60418be8a91fa271c07ddb2af98d69d

The exact run's provenance, runtime, parameters, errors (none), full scalar
coordinates and fiber lists are under
local-only/runs/T01/2026-09-30-elliptic-geometry/.
The portable JSON identifies every raw output path and hash.
The writer refuses to overwrite previous runs.

## Repository checks and file scope

Completed checks are recorded in the local validation result. At the time
of the test run, python3 -m unittest discover -s tests -v passed 90 tests;
python3 -m experiments verify passed all 159 fixed finite checks.
Documentation and source-integrity checks are run after report assembly.
They do not establish any mathematical statement.

Post-assembly results: source-integrity verification passed all 50 local
reference files and 43 T03 manifest members; git diff --check passed.
The repository-wide documentation check reported only four missing links
in the concurrently edited, unrelated multiscale-packing report:
verification.md (twice), state.json and manifest.json. It reported no
broken link in this cycle's files or archive-integrity error. Those
concurrent files were not modified to make this task's check pass.

This cycle adds this six-file report bundle, one exact scout module, its
two-test regression and one portable result file. It appends dated entries
to the T01 STATUS, project map, and mechanism/failure/open-lemma registries.
Original-prefix hashes for those five append-only edits are saved locally.
No archive, copied migration source, SPEC, earlier note or earlier raw run
was modified by this work. The pre-existing working tree was already dirty;
unrelated and concurrent changes remain intact. Nothing was staged,
committed or pushed.

The final local verification manifest records hashes of this cycle's files.
It is separate from the immutable original archive and migration manifests.
