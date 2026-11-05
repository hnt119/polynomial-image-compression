# One bounded transfer, attachment and entropy cycle

T01 · 11 October 2026 · version 1 · sequential, offline research.
Fixed target: P(x,y)=(x-y)^3+x+y on one finite real scalar set in both
coordinates, counting every ordered pair. **T01 remains OPEN.** The
homogeneous quadratic x^2+xy+y^2 and the other tracks were not changed.

## Result

- **PROVED — B-CP:** the exact six-scalar seed has no CP-O1 attachment.
  Monotonicity and the zero-row range reduce every possible frame to five
  polynomial systems. Saved Bezout certificates exclude all five; a
  separate implementation checked them coefficientwise. This resolves
  the finite obligation by incompatibility, not T01.
- **EXPERIMENTAL — B-X:** actual real 3-torsion and a nonempty real division
  torsor on the existing c=6 sharing curve give 14 distinct scalars, 196
  ordered pairs and 188 outputs. Complete fiber/component histogram:
  186 singletons and two fibers of size five. The singleton-pair fraction
  is 93/98. Every pair is included.
- **PROVED using an EXTERNAL RESULT — A-Q:** the rank-one quadratic baseline
  has c=-log(13D rho)/log(2X+1)>0 with the required fixed parameter order
  and uniform per-residue population bound. The reusable rate gate is
  b<2a, charging input losses twice.
- **PROVED implication / OPEN premise — C-BRIDGE:** a local affine
  projection cover transfers to exact support after paying for all strips,
  per-cell output population and exceptional pairs. The finite elliptic
  carrier has a certified separation bound, but no subquadratic covering
  estimate or useful exceptional-pair tail.

Read [A_transfer.md](A_transfer.md), [B_division.md](B_division.md) and
[C_entropy.md](C_entropy.md) for proofs, claim scopes and construction
ledgers. B was the main constructive effort. Its incompatibility and
negative finite result ended the search; no replacement scout was added.

## Authorization and source recovery

The active user commissioned this A/B/C cycle on 2026-10-11, superseding
historical research-stop instructions for this cycle only. Git was on main,
with nine modified tracked files and many inherited untracked artifacts;
there were no staged changes. Initial hashes and diffs were saved under
ignored `scratch/2026-10-11-cycle/`. No reset, staging, commit, push,
remote mutation or rewriting of frozen reports occurred.

Initial reading was limited to these eight relevant repository files:

| Exact repository-relative path | Recorded chronology |
|---|---|
| `docs/CODEX_SETUP.md` | 2026-09-14 setup, 09-20 intake |
| `research/CURRENT_PROJECT_MAP.md` | 2026-09-14 map; addenda through 10-06 |
| `research/CODEX_MIGRATION_AUDIT.md` | 2026-09-14 audit, 09-20 intake |
| `local-only/migration/sources/00_MASTER_HANDOFF.md` | 2026-09-11 |
| `local-only/migration/sources/T01_CURRENT_STATE.md` | 2026-09-10 export |
| `research/tracks/01-cubic-digital/STATUS.md` | Latest tail through 2026-10-06 |
| `research/notes/2026-10-06-changed-collision-pattern/README.md` | 2026-10-06 bridge, VG-O1 rigidity and CP-O1 |
| `research/notes/2026-09-30-elliptic-geometry/README.md` | 2026-09-30 geometry and obstruction |

Further reading expanded these named proof dependencies:

| Obligation | Exact source / inspected locator |
|---|---|
| Target and chronology | `research/tracks/01-cubic-digital/SPEC.md` (2026-09-03 historical route); `research/MIGRATION_CONFLICTS.md` (2026-09-11, 09-20), MC-01, hierarchy and availability |
| Separate quadratic branch | `local-only/migration/sources/T01_Norm_Trace_Quadratic_Research_Checkpoint.md` (2026-09-10), §§1–2 |
| Quadratic baseline | `local-only/migration/research_supplement/shared/Phase_C0_Corrected.md`, §§5–6, and correction-log field/splitting entries; migration version identified by hash |
| External tower | `local-only/migration/research_supplement/shared/03-unit-distance-proof.pdf`, Proposition 3.8, Remark 3.9, pp. 12–14; publication date not assigned from metadata |
| Cubic packing scope | `research/history-sources/Cubic_Difference_Sum_Research_Checkpoint.md` (2026-09-02), executive verdict and baseline; T01 export §§6.1–6.3 |
| Seed and exact evidence | `research/notes/2026-10-06-changed-collision-pattern/construction.md`, CP-C1/C2; its `exact-audit.md`, §§3–4; `experiments/changed_collision_pattern.py`, arithmetic inspected, not executed |
| Elliptic model and poles | `research/notes/2026-09-30-elliptic-geometry/complex-extensions.md`, EG-C1–C4; its `genus.md`, EG-G1/sharing singularities; its `group-law.md`, EG-B2/B3 |
| Exact projection context | `research/notes/2026-09-21-sublinear-cubic/reuse-and-projections.md`, SC-Q1; not imported for the new field |
| Registry and rate requirements | Relevant T01/splitting entries in `research/MECHANISM_LIBRARY.md`, `research/FAILURE_LIBRARY.md`, `research/OPEN_LEMMAS.md`; `research/templates/CONSTRUCTION_LEDGER.md` |

Listings and filename searches were navigation, not claims to have read
all sources found. The requested Pohoata v2, Bourgain, Guth–Katz–Zahl and
Mathe–O'Regan v2 primary texts were not located in the searched local cache.
A and C record those availability limits. The supplied tower is an
identified alternative input, not a claimed audit of Pohoata Proposition
3.1 or Section 4. No unavailable proof was inferred from a filename.

## Computation and separate audit

Declared before execution: offline; no paid calls, installed packages,
new algebra stack, PDF generation or subagents. At most two specializations;
m in {3,4,6,8}; 128 scalars per case; 200,000 ordered-pair evaluations;
field degree <=32; 120 seconds per run; 600 seconds research computation.
Existing regression checks are software validation, not additional searches.

Used: the CP conic and existing c=6 elliptic curve; only m=3; maximum field
degree eight and maximum scalar count 14. CP elimination covers all role
assignments by B's proof, not a parameter sample. The elliptic square is
exhaustive for one finite set only. A single preselected modulo-5 field
certificate is not a prime sweep. No computation failed or timed out.

| Command, from repository root | Result | P evaluations | CPU seconds |
|---|---|---:|---:|
| `python3 research/notes/2026-10-11-transfer-division-entropy/exact_cycle.py attachments` | Five unit gcds and Bezout identities | 0 | 0.015667 |
| `python3 research/notes/2026-10-11-transfer-division-entropy/exact_cycle.py elliptic` | Real group identities and full square, two evaluators | 402 | 1.111360 |
| `python3 research/notes/2026-10-11-transfer-division-entropy/audit_results.py` | Separate implementation passed | 196 | 0.115317 |
| Total | No search expansion | **598** | **1.242344** |

The 402 evaluations include 392 square evaluations and ten slot-identity
evaluations. Python 3.12.7, standard library, no randomness. Reading the
supplied PDF used the existing bundled PDF reader only. Per-run wall
times, input definitions, code hashes, all scalars and fibers, and exact
certificates are in [attachments_results.json](attachments_results.json),
[elliptic_results.json](elliptic_results.json) and
[audit_results.json](audit_results.json).

The scripts refuse to overwrite retained results. For a repeat, copy
`exact_cycle.py` and `audit_results.py` together to an empty directory under
ignored `scratch/`, then run the attachment, elliptic and audit commands
using those copied paths. Outputs are relative to the copied scripts.
Runtime metadata will vary; mathematical data must agree. No such rerun
is claimed here. One documentation patch was rejected for a context
mismatch before changing any file; it was then corrected.

Audit was by the same agent in separate derivation/certificate passes,
with independently implemented arithmetic, not by a second researcher
or external reviewer. Equality uses a proved faithful field basis, never
floating-point proximity. No isolated vertices are omitted.

## Source identities

| Source at the exact path above | SHA-256 |
|---|---|
| Supplied tower PDF | `62b5de8cacdfbc0f13ae1940aa81659cd233e6945b936612fbeab0ab8ab3d383` |
| Corrected C0 report | `8ef3670bb8903b2f851b1bba594435d8635882849dae37912baadf6c49eb85be` |
| 2026-10-06 CP README | `4b05ca498a6d5541161fb91ebbc9a7b6186d361a81871b820e1df254532e93fd` |
| 2026-10-06 CP construction | `a534dee8246cc2c71a580e1c136ef169df35511142bddd131a65d30df41ad30b` |
| 2026-09-30 complex-extensions | `ecf894b30c3a0da77e4bccca37734a78ad0434682c9c72f7cb59f27d5da4c03d` |
| 2026-09-30 group-law | `3d1478df936070dad2796b75c5d2d57bd8cd776f8bdcd8e379197ccb8fdc3be9` |
| 2026-09-02 cubic checkpoint | `1a5ecffb8366cd4ef2a0447d16bc183c7c8cde646428db5bc6163959d1e95b92` |

Local-only references remain in place; Git alone does not contain them.
No old archive, manifest, report or experiment result was altered.

## Repository checks and changed files

This cycle adds only this nine-file note directory and a dated T01 STATUS
pointer/addendum. Inherited work remains uncommitted. Verification passed:

- `python3 scripts/check_repository.py`: 39 archived sources and links
  in 194 current Markdown files.
- `python3 scripts/check_codex_setup.py`: 50 local references, 43 T03
  manifest members, original identities, duplicate states and C4 hashes.
- `python3 -m unittest discover -s tests -v`: all 100 tests passed.
- `python3 -m experiments verify`: all 159 existing finite checks passed.
- `git diff --check`: passed; new files were checked separately because
  ordinary Git diff omits untracked files.

These checks validate packaging and finite software regressions; they
do not prove T01. The new mathematical evidence is the explicit argument
and exact certificates above, not the regression count. The prior 338
nonignored files were compared against the saved baseline; the only
modified pre-existing file is T01 STATUS, with its prior contents preserved
as a byte-identical prefix. New files and this task's STATUS addition were
inspected separately from the inherited diff.

## Exactly one next proof obligation

**OPEN — retain EG-O1 / NC-O1, the actual all-pair fiber tail.** Construct
an unbounded family of real same-set carriers A, |A|=n, and prove that
for fixed epsilon,kappa>0, all but O(n^(2-kappa)) ordered pairs have
actual fiber multiplicity at least n^epsilon. Include every isolated
vertex and every unprescribed cross-pair. This is the existing sufficient
obligation, not a claimed simpler reduction or another authorized search.
CP-O1 is now closed in its stated finite scope. This bounded cycle stops.
