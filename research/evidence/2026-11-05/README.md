# How to follow a claim to its evidence

Use the [project evidence index](../../EVIDENCE_INDEX.md) for the mathematical narrative. The [claim ledger](claim-ledger.json) records the quantified results and decisions in that narrative. The [checkpoint catalogue](checkpoints.json) opens the rest of the native record, including intermediate lemmas, finite runs, construction ledgers and historical review statements. The paths stored in both JSON files are relative to the repository root.

## Following one result

For **MC-S2**, find `T01/2026-10-21-multiscale-collisions/MC-S2` in the claim ledger. The record identifies the arbitrary finite real set, half-open partition, terminal separation, genuine same-output branching count and exact inequality. Read the [proof](../../notes/2026-10-21-multiscale-collisions/specialist.md), then the [historical independent argument check](../../notes/2026-10-21-multiscale-collisions/referee.md). The [finite lab program](../../notes/2026-10-21-multiscale-collisions/audit.py), [exact result](../../notes/2026-10-21-multiscale-collisions/experiment-summary.json), [independent finite counts](../../notes/2026-10-21-multiscale-collisions/referee-counts.json) and [dated verification record](../../notes/2026-10-21-multiscale-collisions/verification.md) belong to the same checkpoint. The proof uses no numerical result. Read **MC-X1** for the bounded census and **MC-O1** for the separate open two-map problem.

For **MS-C1**, include the track and date. The T01 [marked-shift proof](../../notes/2026-10-11-marked-shift-certificate/arithmetic.md) shows infinite order for a particular elliptic point. T03 reuses the label in its [dyadic packing](../../notes/2026-09-30-multiscale-packing/composition.md) and [mixed-signature construction](../../notes/2026-10-20-mixed-signature/README.md). Likewise, September's three-branch **TC** identifiers and October's torsion **TC** identifiers live in distinct checkpoints.

## What the fields mean

| Field | Interpretation |
|---|---|
| `id`, `native_ids`, `archive_aliases` | A unique archive address identifies a claim or tightly related claims. `native_ids` gives the source labels. An archive alias supplies a readable key for an unnumbered statement or publication-level grouping. A label can recur in another file, track or date. |
| `track`, `polynomial` | The polynomial whose conclusion is being indexed. An explicitly named comparator, the T01 affine-quadratic benchmark and the shared square-plus-linear theorem have separate scopes. |
| `hypotheses_and_quantifiers`, `result`, `scope` | The domain, construction, quantifiers, claimed consequence and its limit. When a carrier has a long definition, the named section supplies its defining equations. The native statement controls any ambiguity in the synopsis. |
| `status`, `evidence_grade`, `locator_role` | `PROVED` records a theorem or a proved implication in the identified source system. The evidence grade distinguishes a public argument, a public digest of an identified theorem, and a result reported from a missing original. `CONDITIONAL` is a conclusion requiring unproved premises. `OPEN` marks an unresolved obligation. `FAILED` identifies the specified route or certificate. `EXPERIMENTAL` is evidence within its stated finite range. `EXTERNAL RESULT` points to the source of an imported theorem. The catalogue also preserves historical and superseded source wording. |
| `proof_locator`, `checkpoint`, `version` | Repository-root-relative path and section. On open, finite and source-reported entries, this identifies the statement, data or report. A dated checkpoint joins to the identically named catalogue key. Records with no checkpoint give a direct locator in a reconciliation, historical proof or separately dated digest. |
| `evidence_locators` | The checkpoint's associated code, data, regression tests and verification files. They can verify different claims in the same report. For example, MC-X1 uses finite output whereas MC-S2 is analytic. Empty arrays mean that no separate portable item was indexed in that category. A verification locator can also be the dated report itself when that is where the audit is recorded. |
| `dependencies`, `supersession`, `audit_this_pass` | Named imports and prerequisites, the scope of a later correction or closure, and the work performed in the November archive pass. Read the dated verification file for earlier proof-checking personnel/roles, commands, evidence and limitations. Historical check counts and source-file digests are not new execution records. |

The catalogue gives a report, a list of statement/proof section locators, historical claim-register entries, and native code/data/test/verification paths for each public checkpoint. Its transcribed entries may repeat across an original proof, its independent check, and a later summary. Counts of rows therefore are not counts of independent theorems. An old table can still say **OPEN** about an obligation closed later in another checkpoint. The dated supersession in the claim ledger and the [migration conflicts](../../MIGRATION_CONFLICTS.md) tell the reader which statement controls. The [39-file historical manifest](../../manifest.json) continues to identify the original archive.

## Sources and availability

| Evidence | Availability and use in this edition |
|---|---|
| T01 older digital and rich quadratic-fiber no-go | **MISSING SOURCE / PROVENANCE FILE** for `Regular_Digital_Carry_Collapse_Universal_NoGo_Checkpoint.md` and `Cubic_Target_Exact_Elements_and_Candidate_Test.md`. September recovery documents report those originals and give identifying information. Their original bytes were absent from the received supplement. The separately located [continuous-cover proof](../../history-sources/Concrete_Cubic_Compression_Block_NoGo_Checkpoint.md) treats a different object. See [TB-S1–S4](../../notes/2026-09-16-three-branch-lift/source-scope.md) and [MC-06](../../MIGRATION_CONFLICTS.md). |
| T02 old C1 sources and reproduction material | **MISSING SOURCE / PROVENANCE FILE** for the complete historical C1 proof and the omitted ledgers/review items identified in MC-06. The [finite-field report](../../notes/2026-10-11-finite-field-chebotarev-report/report.md) reproduces the analytic C2–C4 arguments and the specified finite correlated C1 subcase. Those do not establish the general correlated C1 claim. |
| T03 original migration certificates | **MISSING SOURCE / PROVENANCE FILE** for the standalone F25 source/log/executable and `Quadratic_Tower_Arithmetic_Obstruction.md`. Their recovery is reported, but the received supplement lacked these original files. The [T03 status](../../tracks/03-eisenstein-cartesianization/STATUS.md) separates the adaptive ledger from the later mixed-signature route. |
| T04 depth-30 record and early source constants | **MISSING SOURCE / PROVENANCE FILE** for the depth-30 raw input-growth result and exact historical invocation, script variant and runtime. The held growth record ends at depth 24. Some early one-/two-prime proof sources and numerical constants remain unlocated. The controlling field-supply locator was subsequently identified. See [MC-04–MC-06](../../MIGRATION_CONFLICTS.md) and the [T04 record](../../tracks/04-cubic-slices/STATUS.md). |
| Raz–Zahl theorem and energy-dispersion input | **MISSING SOURCE / PROVENANCE FILE** for the precise theorem and supporting proposition requested in the multiscale cycle. The [applicability audit](../../notes/2026-10-21-multiscale-collisions/README.md) gives no imported exponent; MC-S1–S3 have elementary proofs. |
| Shared square-plus-linear theorem | The November [mathematical digest](../../../docs/release/2026-11-05/shared-quadratic.md) identifies Theorem 1 and the earlier internal audit of the all-integral statement. It gives a proof sketch and the imported arithmetic proposition. The [October arithmetic report](../../notes/2026-10-11-finite-field-chebotarev-report/report.md) supplies the earlier narrower C0 statement and its proof exposition. Academic working documents and third-party reference PDFs are withheld. |

Private migration materials, local raw runs and restricted PDFs are not portable repository artifacts. A separate received manifest can identify a file without delivering it. Conversely, an available public proof or newly supplied mathematical digest is cited directly even if the original administrative container is withheld. No research was performed to fill an archival gap. See the [reproduction guide](../../../docs/reproducibility.md) for the finite regressions and documentation checks and the [historical project map](../../CURRENT_PROJECT_MAP.md) for the original source hierarchy.

## Native checkpoint directory

The following links cover the public mathematical note directories through the cutoff. Open the catalogue entry with the same date and suffix to reach its individual proof sections, certificates and data.

### T01 plus-sign cubic

- [2026-09-16 · three branch continuation](../../notes/2026-09-16-three-branch-continuation/README.md)
- [2026-09-16 · three branch lift](../../notes/2026-09-16-three-branch-lift/README.md)
- [2026-09-21 · cubic returns](../../notes/2026-09-21-cubic-returns/README.md)
- [2026-09-21 · growing step cubic](../../notes/2026-09-21-growing-step-cubic/README.md)
- [2026-09-21 · nonlinear reuse](../../notes/2026-09-21-nonlinear-reuse/README.md)
- [2026-09-21 · sublinear cubic](../../notes/2026-09-21-sublinear-cubic/README.md)
- [2026-09-21 · three branch freeze](../../notes/2026-09-21-three-branch-freeze/Three_Branch_Continuation_Freeze.md)
- [2026-09-30 · elliptic geometry](../../notes/2026-09-30-elliptic-geometry/README.md)
- [2026-09-30 · near complete charts](../../notes/2026-09-30-near-complete-charts/README.md)
- [2026-10-06 · changed collision pattern](../../notes/2026-10-06-changed-collision-pattern/README.md)
- [2026-10-06 · sharing compatibility](../../notes/2026-10-06-sharing-compatibility/README.md)
- [2026-10-06 · variable gap sharing](../../notes/2026-10-06-variable-gap-sharing/README.md)
- [2026-10-11 · marked shift certificate](../../notes/2026-10-11-marked-shift-certificate/README.md)
- [2026-10-11 · torsion compatible sharing](../../notes/2026-10-11-torsion-compatible-sharing/README.md)
- [2026-10-11 · torsion frame freeze](../../notes/2026-10-11-torsion-frame-freeze/README.md)
- [2026-10-11 · transfer division entropy](../../notes/2026-10-11-transfer-division-entropy/README.md)
- [2026-10-11 · varying output frames](../../notes/2026-10-11-varying-output-frames/README.md)
- [2026-10-11 · vo o1 freeze](../../notes/2026-10-11-vo-o1-freeze/README.md)
- [2026-10-20 · tetrahedral junction](../../notes/2026-10-20-tetrahedral-junction/README.md)
- [2026-10-21 · multiscale collisions](../../notes/2026-10-21-multiscale-collisions/README.md)
- [2026-10-21 · tj o1 freeze](../../notes/2026-10-21-tj-o1-freeze/README.md)

### T03 homogeneous quadratic

- [2026-09-16 · high return](../../notes/2026-09-16-high-return/README.md)
- [2026-09-16 · hr n1 final freeze](../../notes/2026-09-16-hr-n1-final-freeze/README.md)
- [2026-09-16 · hr n1 offline](../../notes/2026-09-16-hr-n1-offline/README.md)
- [2026-09-16 · two prime character](../../notes/2026-09-16-two-prime-character/README.md)
- [2026-09-16 · unit exponent](../../notes/2026-09-16-unit-exponent/README.md)
- [2026-09-20 · cartesian norm freeze](../../notes/2026-09-20-cartesian-norm-freeze/README.md)
- [2026-09-21 · correlated dc o1](../../notes/2026-09-21-correlated-dc-o1/README.md)
- [2026-09-21 · dc o1](../../notes/2026-09-21-dc-o1/README.md)
- [2026-09-21 · dense cartesianization](../../notes/2026-09-21-dense-cartesianization/README.md)
- [2026-09-21 · return tail](../../notes/2026-09-21-return-tail/README.md)
- [2026-09-30 · modular lift](../../notes/2026-09-30-modular-lift/README.md)
- [2026-09-30 · multiscale packing](../../notes/2026-09-30-multiscale-packing/README.md)
- [2026-10-06 · cross block amplification](../../notes/2026-10-06-cross-block-amplification/README.md)
- [2026-10-06 · cross block returns](../../notes/2026-10-06-cross-block-returns/README.md)
- [2026-10-06 · fiber growth](../../notes/2026-10-06-fiber-growth/README.md)
- [2026-10-11 · balanced full fibers](../../notes/2026-10-11-balanced-full-fibers/README.md)
- [2026-10-11 · bff o1](../../notes/2026-10-11-bff-o1/README.md)
- [2026-10-20 · mixed signature](../../notes/2026-10-20-mixed-signature/README.md)
- [2026-10-21 · relative unit population](../../notes/2026-10-21-relative-unit-population/README.md)
- [2026-10-21 · typical unit returns](../../notes/2026-10-21-typical-unit-returns/README.md)

### Shared and cross-track records

- [2026-09-14 · study notes](../../notes/2026-09-14-study-notes/README.md)
- [2026-09-16 · solvable norm trace](../../notes/2026-09-16-solvable-norm-trace/README.md)
- [2026-10-11 · finite field chebotarev report](../../notes/2026-10-11-finite-field-chebotarev-report/report.md)
