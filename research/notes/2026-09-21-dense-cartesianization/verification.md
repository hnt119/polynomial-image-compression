# Dense Cartesianization — audit and reproducibility

Date: 21 September 2026. Fixed polynomial: $Q=x^2+xy+y^2$.
This file distinguishes mathematical proof audit, exact finite research,
and repository integrity checks. No external review or novelty claim.

## 1. Mathematical audits actually performed

| Reviewer assignment | Work independently checked | Result |
|---|---|---|
| `norm_trace` | DC-M1–M4; DC-B1/B2/R1/R2; DC-A1 and its interval/height refinement | PASS; fixed-place-value height and arbitrary-real-shift ledger qualifications corrected |
| `eisenstein_sources` | DC-S1/S2; DC-B1/B2/R1/R2 | PASS; complete-block summary corrected to an eventually growing threshold, hence $R>2$ |
| `audit_sign_cube` | Exact scout and two accounting tests before execution; complete DC-M5 proof after indexing alignment | PASS; output-path collision guard added before the only execution |
| Lead | All four new proof companions; exact action and HR-1 application; full support, zero, scope and rate ledger | PASS |

These assignments were independent of the authorship of the proofs they
reviewed. The review agreement is not itself the proof: the full arguments
are in the four companions. Reviewers ran no programs. Final report/data
cross-review is recorded below after completion.

## 2. Frozen research execution

- New module: `experiments/dense_cartesianization.py`.
- Inspected reusable dependency: `experiments/unit_exponent.py`; unchanged.
- Fixed schedule: growing one-axis interval thickening at $d=1,2$;
  faithful ternary GAP at $d=2,3$.
- Command: `python3 -m experiments.dense_cartesianization --output
  examples/2026-09-21-dense-cartesianization.json --pairs-output
  local-only/runs/T03/2026-09-21-dense-cartesianization/pairs.json`.
- Exactly one scout execution; four cases; every ordered pair/action
  tested using `Fraction`, plus a separately charged independent oracle.
- Python 3.12.7; no network, seeds, sampling, factorization or float equality.
- Raw pair file includes every distinct returned target and output fiber.
  It is local-only; transfer it separately when a raw-data handoff is needed.
- Summary: `examples/2026-09-21-dense-cartesianization.json`.

| Research query category | Charges |
|---|---:|
| Constructed action norm checks | 48 |
| Scalar $Q$ evaluations | 9,054 |
| Independent scalar $Q$ evaluations | 9,054 |
| Action/pair tests | 93,744 |
| Independent action/pair tests | 93,744 |
| **Scout total** | **205,644** |

Scout CPU: **2.511953 seconds**; wall: **2.5144815 seconds**.
These timings are provenance, not mathematical evidence. Exact histograms
establish the finite claims; symbolic proofs establish the asymptotic claims.

## 3. Required regression accounting

The inspected local-only `regression_guard.py` invokes the standard
repository commands through `runpy`, without invoking the scout entry
point. It conservatively charges every call in `experiments/` and
`tests/`, including helpers and generator resumptions. This overcounts
the semantic mathematical queries. Two new tests use only the origin
and a nine-pair ternary square to check duplicates, mixed returns and
full-image accounting.

| Required command | Result | Conservative charges | CPU seconds |
|---|---|---:|---:|
| `python3 -m unittest discover -s tests -v` | 54 tests PASS | 64,949 | 2.174586 |
| `python3 -m experiments verify` | 159 checks PASS | 25,386 | 0.793931 |
| **Combined with scout** | **Within cap** | **295,979** | **5.480470** |

Shared announced cap: 2,000,000 charged evaluations and 600 CPU seconds.
Every query is guarded; CPU checks are periodic rather than an operating
system hard deadline. No further research executions were undertaken.
The two regression logs and their category breakdowns are in the local
run directory. Formatting data tables and hashing files are separate
documentation operations, not added carrier experiments.

## 4. Source and workspace integrity

Startup records in `local-only/runs/T03/2026-09-21-dense-cartesianization/`:
`baseline.json`, `inherited.patch`, and `inherited-status.txt`.
The baseline records 170 pre-existing repository files. The task began
on `main` with nine tracked modified files and earlier untracked research
artifacts. This cycle preserves that work; its changes are identified
separately rather than attributed to this task wholesale.

Only dated addenda are permitted in the existing current map, T03 status,
mechanism library, failure library and open-lemma register. Historical
proofs, sources, data, checkpoints, SPECs and canonical manifests are not
rewritten. No stage, commit, push, reset or remote change was requested
or performed. Missing private sources from earlier migration audits are
not needed by any new proof.

## 5. Final report review and repository checks

The final data reviewer independently read the four-case JSON and both
regression logs. All tables, fractions, geometric means, reciprocal
bounds, test totals and budget figures matched. Corrections distinguish
image-fiber populations (summing to image size) from their size-weighted
sum (equal to $n^2$), place action injectivity at nonzero **pairs**, and
restrict the zero-inclusion statement to the diagnostic squares. The
mathematical report reviewer independently checked its scopes and
implications; the image-histogram wording was also identified there.

| Check actually performed | Outcome |
|---|---|
| `python3 scripts/check_repository.py` | PASS: 39 archived sources; local links in 89 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local reference files; original import identities; 43 T03 manifest members; duplicate states and C4 hashes |
| `git diff --check` | PASS |
| New note/code/test/data trailing-whitespace inspection | PASS |
| Scout and reusable arithmetic source hashes against execution metadata | PASS; source bytes unchanged since execution |
| Baseline/prefix integrity comparison | 162 baseline files unchanged; four addenda preserve their startup bytes; current-map addendum preserves its immediate pre-append bytes |

The initial baseline comparison deliberately assumed that only this
task's five existing files could change. It detected concurrent changes
to three T01 files, so that assumption failed. A provenance-aware check
then separated them without reverting or editing them:

- `research/notes/2026-09-21-three-branch-freeze/Three_Branch_Continuation_Freeze.md`
- `research/notes/2026-09-21-three-branch-freeze/verification.md`
- `research/tracks/01-cubic-digital/STATUS.md`

The current map had also changed before this task appended its dated
entry. Its exact immediate pre-append prefix was retained; it is not
reported as matching the startup hash. These concurrent edits are not
attributed to this task. All earlier T03 proof/data/checkpoint hashes
in the baseline are unchanged. The final inspection found no missing
baseline file. Detailed checks are in local `integrity.json` and
`addenda-prefixes.json`.

This task created the report, four proof companions, this verification
record, the new exact scout, two small tests, and the four-case summary.
It appended only the current map, T03 status, mechanism library, failure
library and open-lemma register. Local raw data, baseline snapshots,
regression logs and the scoped source manifest accompany those changes.
The repository remains uncommitted, with inherited changes retained.

## 6. Hash manifest

`manifest.json` in this note directory hashes the finished report, four
proof companions, verification record, new program/tests, frozen summary,
raw pairs and regression wrapper. It excludes itself to avoid a circular
hash. The original archive manifests are not changed. The frozen summary
also contains the exact program and arithmetic-dependency hashes used
at execution, independently checked above.
