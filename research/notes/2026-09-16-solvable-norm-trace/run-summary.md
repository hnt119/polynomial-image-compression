# Run summary and final disposition — 16 September 2026

The [main report](README.md) gives the construction definitions, source
reconciliation, return-tail criterion, and arithmetic ledgers. The complete
new algebraic proofs are in [algebra.md](algebra.md) and
[sign-cube.md](sign-cube.md). All review in this cycle was internal.

## NT-20260916-7 — bounded constructive rephasing

**Status: EXPERIMENTAL.** Fixed polynomial $q=x^2+xy+y^2$, T03's separate
multiplier branch, version/date: this section, 16 September 2026.
Dependencies: the norm-preserving action in main-report claim
NT-20260916-5; independent-prime exact field arithmetic; F3 word sets in
NT-20260916-6. Evidence: deterministic finite search, followed by exact
norm-by-word verification and enumeration of every Cartesian pair.

For each original balanced word $w\in Z_m$, the candidate list is exactly
$wU_m$. It stays anchored to the original word throughout the search; there
is no hidden expansion of multiplier exponents. Initially place every word
at itself. In lexicographic order, consider all candidates, reject any
already occupied by another word, and accept only strict decreases in the
size of the signed coordinate union. Ties use the first lexicographic
minimum. Allow at most ten sweeps. The fixed tested levels are $m=1,2,3$.

The program verifies distinct word placements, equality of each word's old
and new norm, and a rebuilt coordinate union before counting the full image.
The concrete final coefficient sets and word correspondences are retained
in the raw JSON, with exact rational coefficients and SHA-256 hashes.

| $m$ | Word pairs | Coordinate count before | Coordinate count after | Full image | Accepted moves |
|---|---:|---:|---:|---:|---:|
| 1 | 4 | 7 | 7 | 11 | 0 |
| 2 | 16 | 29 | 29 | 163 | 0 |
| 3 | 64 | 137 | 137 | 4,289 | 0 |

Each case stopped after one complete no-improvement sweep. This certifies
only a **single-word local optimum over these fixed candidate lists**.
It is not a global minimum, an exhaustive joint reassignment search, or a
theorem ruling out beneficial neutral moves or changes of several words
together. The objective minimized coordinate count; full image was computed
afterward. The finite test supplies no asymptotic exponent.

The main report's F1–F3 construction ledger applies. Rephasing additionally
preserves every original engineered norm and has one-point placement fibers.
Its candidate denominator divides $D_m$ because original F3 words are
integral and candidates are $wU_m$; the unchanged final placements here have
denominator one. Norm preservation bounds conjugate size exactly as for F3.
All unengineered pairs still contribute to the counted full image. No input
or output rate beyond these finite sets is asserted.

## Reproducible commands and retained outputs

Run from the repository root with Python 3.10 or later. The executed runtime
was **Python 3.12.7**. Use a new output pathname for reproduction; the scripts
refuse to overwrite run records. These exact commands were executed:

```bash
python3 -m experiments.solvable_norm_trace --output local-only/runs/shared/2026-09-16-solvable-norm-trace/norm-results.json
python3 -m experiments.solvable_norm_trace --output local-only/runs/shared/2026-09-16-solvable-norm-trace/norm-results-v2.json
python3 -m experiments.eisenstein_solvable --output local-only/runs/T03/2026-09-16-solvable-multipliers/eisenstein.json
python3 -m experiments.eisenstein_rephase --output local-only/runs/T03/2026-09-16-solvable-multipliers/rephase.json
python3 -m experiments.eisenstein_solvable --output local-only/runs/T03/2026-09-16-solvable-multipliers/eisenstein-v2.json
python3 -m experiments.eisenstein_rephase --output local-only/runs/T03/2026-09-16-solvable-multipliers/rephase-v2.json
```

The first norm run lacked the added individual-norm and sum/product metrics;
the second retains the same target-image counts and adds those measurements.
The original run is preserved as preliminary evidence and charged to budget.
Its historical code hash is recorded; its exact pre-edit source snapshot was
not saved. Use v2 for complete reproducibility with the current norm module.

Independent review of the multiplier modules found two bookkeeping issues:
15 setup norm checks in F1–F3 and 6 in F4 were outside the original counters,
and NaN could bypass one CPU-limit input check. These were fixed; the old
executed modules were snapshotted under the shared run directory's
`executed-code/`. Both complete multiplier experiments were then rerun to
new v2 files. Their input/output hashes and mathematical results agree with
the first runs. Limits use cooperative CPU checks, including a final check;
they are not operating-system hard timeouts. All runs completed within their
limits and reported no arithmetic or search errors.

The compact [exact results](../../../examples/2026-09-16-solvable-norm-trace.json)
use the final v2 data. No random seeds or floating equality tolerances are
involved. Timings are measured CPU seconds and are not reproducibility
assertions. Scientific input/output hashes are independent of timing metadata.

## Aggregate budget

There are **11 distinct carrier families and 43 distinct finite cases**:
six fixed-field hybrid/trace families, one growing sign cube, three multiplier
families, and one bounded rephasing family. Reruns do not create new families;
their costs are included below.

| Actual research work, including reruns | Count |
|---|---:|
| Polynomial, sum/product, and engineered-pair evaluations reported by six runs | 770,515 |
| Action-pair membership tests, both full runs | 567,984 |
| Candidate generation and scoring, both rephasing runs | 7,536 |
| Original-run setup norm checks omitted from old counters, charged here | 21 |
| **Conservative combined research evaluations** | **1,346,056** |

The recorded research CPU total is approximately **11.22 seconds**. This is
computation time, not the elapsed time for source reading, proof development,
implementation, and review. A further 100,000 evaluations and 10 CPU seconds
are conservatively reserved for all small arithmetic/oracle regressions and
the existing finite verification suite run during this cycle. Even including
that reserve, the announced 2,000,000-evaluation / 600-CPU-second budget is
not exhausted. No larger search or later adaptive level was run.

## Verification and actual changes

New material consists of three opt-in experiment modules, three test modules,
this dated research-note directory, a compact example result, and ignored
local raw runs. The original 39-file archive manifest and the separate source
manifest remain unchanged. [source-manifest.json](source-manifest.json)
records identities for this cycle without modifying either canonical manifest.

Validation commands:

```bash
python3 scripts/check_repository.py
python3 scripts/check_codex_setup.py
python3 -m unittest discover -s tests -v
python3 -m experiments verify
git diff --check
```

All five checks passed: 39 archived sources and links in 48 Markdown files;
42 local references and 43 T03 archive entries; 38 unit tests; 159 finite
baseline checks; and no whitespace errors. Full outputs are in
`local-only/runs/shared/2026-09-16-solvable-norm-trace/validation.txt`.
Unit tests include
independent rational/integer oracles, exact field products, norm preservation,
all-pair/fiber accounting, denominator-divisibility returns, zero handling,
budget rejection, and a nontrivial improving toy rephasing. These verify the
implementation on finite cases; they do not prove a research target.

All inherited tracked modifications and preexisting untracked migration/study
work were preserved. This task changed no existing tracked file, staged
nothing, and made no commit, push, or remote change. New files remain untracked.

## Precise remaining gap

**OPEN:** construct growing real sets with a fixed positive full-image rate
gap for $q$, $P_0$, or the broader nonspecial full-rank quadratic family.
The exact sign cube is ruled out; the tested norm/trace and multiplier
families have no proved asymptotic saving. These outcomes do not refute the
polynomial targets or all solvable-extension constructions.

For a multiplier-based continuation, the concrete missing estimate is an
actual carrier with many distinct returning norm-one multipliers for almost
every pair, with the light tail and every arithmetic/input cost paid. The
tested independent products do not exhibit that behavior. Joint rephasing
or other correlated carriers were not exhaustively ruled out. No additional
research cycle is scheduled or implied by this note.
