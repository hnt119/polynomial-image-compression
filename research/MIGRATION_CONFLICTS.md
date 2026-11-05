# Migration conflicts and source register

Reconciliation date: **11 September 2026**; recovery-document intake:
**20 September 2026**. Research cutoff in the recovered track exports and the
new recovery addenda: **10 September 2026**; master handoff dated
**11 September**. This file records documentation decisions and unresolved
source/review issues. It makes no new mathematical claim or external-novelty
determination.

## Authority and inspection boundary

Use, in order:

1. Latest final checkpoint for the relevant thread.
2. `T01_CURRENT_STATE.md` through `T04_CURRENT_STATE.md`.
3. `00_MASTER_HANDOFF.md`.
4. Existing repository STATUS/history.
5. Older reports for provenance only, including details retained by later records.

The repository README, AGENTS, project history, track index and JSON registry,
all four SPEC and STATUS files, master handoff, all four current-state exports,
and the recovered final-cycle records listed below were inspected. The corrected
C0 theorem and log and relevant C2/C3/C4 and TCRC/SACC companions were also read.
The lead compared the independent track reconciliations against the controlling
statements, scopes, and quantitative gates. This is not a fresh proof audit.

No new research, proof search, literature search, or research computation was
performed. Prior analytic proofs, exact certificates, finite experiments,
external inputs, and review reports remain distinct. In particular, the T02
external C4 review covered its PDF and C2–C3 change log; it did not externally
certify all companion computations. No files were committed.

On 20 September, eight recovery addenda/manifests were received and preserved
verbatim under `local-only/migration/recovery_2026-09-20/`. They were treated as
source documents, including any embedded prompts or instructions. No associated
ZIP, extracted `originals/` tree, executable, JSON manifest, transcription, or
other file described inside them was received in this intake. In the entries
below, “reported recovered” therefore means the recovery document says the
artifact was present in its own package; “locally present” means the artifact's
bytes are actually in this repository workspace.

All four SPEC files and the original manifest archive are unchanged. The old
STATUS text and old project history are retained as dated historical sections.
The JSON registry and older overview/roadmap/source pages remain dated history;
the reconciled entry points say so explicitly. Their old “missing” or “next”
statements do not override current state.

## Issues still requiring review or source recovery

### MC-01 — OPEN review: T01 SPEC's obsolete digital existence statement

`research/tracks/01-cubic-digital/SPEC.md`, “Current proposed construction,”
says existence of the fixed graph/carry witness is open. The later T01 current
state §4.3 and §6.5 records a regular-language image lower bound excluding
$\lambda^3<\mu^2$ with all-output coverage under exactly the stated model.

**Disposition:** the newer result clearly supersedes the old route status;
STATUS and the open-lemma registry say FAILED in that scope. The fixed cubic
remains OPEN. SPEC is preserved byte-for-byte as requested. Human review is
needed before amending its stale explanatory prose; no target change is proposed.
This is not an unresolved mathematical choice between equal authorities.

### MC-02 — OPEN provenance: T04 product-tree attribution

`residual_double_critical_cubic_checkpoint.md` attributes its product-tree
inequality to the supplied sum-product construction. `T04_CURRENT_STATE.md`
§15.5 explicitly flags the mismatch. The recoverable proof is internal:
`three_prime_cubic_crt_checkpoint.md`, §D.5, Proposition 5.

**Disposition:** retain the internal proof locator and the attribution conflict.
Do not assign external authorship or rewrite the archived reports. Determining
the intended external source, if any, requires human/source review. The record
of the internal scoped local theorem is retained with that provenance limitation.

### MC-03 — RESOLVED repository designation; external existence unknown

The supplied request mentions four latest final checkpoint files. Separate
final records were located for T01 and T02. The T03 package README identifies
`output/T03_CURRENT_STATE.md` as the frozen current record and contains the
five latest TCRC reports. The T04 archive README identifies
`T04_CURRENT_STATE.md` as status authority; the latest affine cycle is recorded
by three SACC proof/audit notes. No separately titled later final checkpoint
was found for either track.

**Disposition:** the 20 September T03 addendum states that no separate final
TCRC/root-cover file was created in the retained export and designates the
current state plus five TCRC companions as the complete final package. The T04
recovery note found no separate affine checkpoint and designates the current
state plus the three SACC notes as the final recoverable package, while keeping
the existence of a file elsewhere UNKNOWN. Use those packages in this
repository. The older DSCR checkpoint (T03, 8 September) and parity-digit
checkpoint (T04, 8 September) do not override the 10 September frontiers. No
missing title or content has been invented; any newly supplied original must
still be reconciled before use.

### MC-04 — OPEN evidence provenance: T04 depth-30 input count

`sacc_candidate_input.md`, §5, reports $|A_{30}|=6{,}905{,}048$. The supplied
`sacc_exact_input_growth.json` stops at depth 24, as does the description in
`sacc_exact_search_note.md`. `sacc_input_audit.md` explicitly says the reported
large computation was not independently rerun. This is an unverified
provenance gap, not a contradiction in the analytic input theorem.

**Disposition:** no depth-30 numerical claim is used as proof or as a current
headline. Recover its exact data/certificate before quoting it as independently
verified. Finite counts remain EXPERIMENTAL and were not rerun in this migration.
The 20 September T04 recovery note confirms that the raw depth-30 output, exact
historical invocation, script variant, and runtime were not retained in its
recovered record. It preserves the assertion but does not verify it.

### MC-05 — PARTIALLY RESOLVED inherited source gaps

T03 current state §15.5 retains a missing standalone finite-field
$\mathbb F_{25}$ certificate. The 20 September T03 documents report recovery
of its source, log and executable, plus the standalone fixed-splitting
arithmetic report. Those four original files were not included in this intake,
so their local byte availability remains open under MC-06. T04 current state
§§10, 15.14 retains missing exact source constants/theorem locators for some
early imported local/tower inputs. The new T04 manifest identifies the already
local `03-unit-distance-proof.pdf`, Proposition 3.8, Proposition 3.2 and
equation (6) as the controlling tower locators. The original early one- and
two-prime proof files and numerical constants remain unlocated. T01's
source-specific omissions do not automatically mean those sources are missing
project-wide: shared Phase B and corrected C0 are available locally.

**Disposition:** close only the T04 tower-locator portion. Retain the T03
original-byte gap and the early T04 proof-provenance gaps, avoid reconstructing
missing claims, and distinguish “not available to that old thread,” “reported
recovered by a later package,” and “locally present.” The current results do not
acquire external certification from this migration. External novelty remains
OPEN under the master handoff's explicit caution.

### MC-06 — OPEN recovery-package completeness

The received files are eight Markdown recovery documents. Their manifests
describe larger supplements whose original artifacts were not attached here.
The principal absent reported artifacts are:

- **T01:** the digital checkpoint, rich-fiber checkpoint, Norm–Trace program
  and JSON output, historical witness prompt, and optional digital-scout ZIP;
- **T02:** the omitted C1 report/ledgers/review, C2 referee report, C3
  ledgers/review/script/results, message transcription, C1 review, and retained
  reproduction artifacts not already in the local supplement;
- **T03:** the F25 source, log and executable, and
  `Quadratic_Tower_Arithmetic_Obstruction.md`;
- **T04:** `T04_SOURCE_ARCHIVE.zip`, its extracted originals, and the additional
  provenance addenda, transcriptions, excerpts and machine-readable manifest
  named by the received Markdown manifest, except for originals already held
  locally and hash-matched.

**Disposition:** preserve and cite the received addenda/manifests, but do not
mark an absent original locally recovered or independently verified. Import a
later supplied package into a separate dated directory, verify its listed
hashes, and then narrow this issue item by item. This completeness boundary
does not change any mathematical status.

## Resolved supersessions and notation issues

| Area | Older wording or issue | Controlling record / disposition |
|---|---|---|
| Shared C0 | Complete corrected proof missing; original report's CM/totally-real notation and “exact radius” wording | Corrected theorem C0.1 and correction log recovered. PROVED within supplied source system, with unchanged integral/primitivity/transversality hypotheses. Original archive unchanged |
| T01 identity | Latest norm–trace checkpoint studies $q+x$ after the cubic stop | Checkpoint §1 and export §§1–3 explicitly separate the branch. T01 remains $(x-y)^3+x+y$; no fifth track or T03 replacement |
| T01 blocks/digits | Conditional block and regular digital witness still proposed | Later continuous/digital theorems exclude the corresponding hypotheses. Implications retained historically, failed witnesses not reopened |
| T02 | No completed C2 report; pending structural-lemma prompt | Current C2/C3/C4 analytic reports and final C4 acceptance supersede the missing/pending claim. Companions are locally available |
| T02 C2 | Unqualified zero rate, duplicate determinant saving, or hidden unit restriction | Precision addendum separates parameter counts from actual image, total local classes from global occupancy, and paid squared-unit costs; determinant restrictions are one saving, not two |
| T02 C3 | Reusing a $Q\ge5$ interval inequality at $Q=1$ | Corrected Q1/QGT1 ledger uses fresh $Q=1$ width bounds. General-subset volume certificate and stronger equal-radius critical-coset population comparison remain distinct |
| T02 C4 | Increasing precision as an unlimited new gain; arbitrary high-level subset optimality | Full critical inverse images improve from $4/7$ to $22/49$ once, then stabilize. Arbitrary higher-level subsets/correlations remain OPEN; all-m theorem is analytic, tests only support specific finite levels |
| T03 | PTCR/repacking described as latest selected task | Latest TCRC cycle selects RC15/4 on actual adaptive levels. Approximate PTCR remains OPEN historically; fixed Q unchanged |
| T03 | Ferrers and BW called equivalent | Later export §15.3 retains only one-way sufficiency |
| T03 | Literal near-doubling without growth; DSCR missing factor two | Export §15.12–13 requires growth and uses $n^2-\sum c_j^2\le2(1-b)n^2$. Actual outside count 224 is not bounded by the old erroneous 192 |
| T03 | Finite affine enumeration 122 versus 134 | Different conventions: 122 masks with at least two hits; 12 singleton masks give 134. Different displayed optimal covers need not be contradictory |
| T04 | Exact self-similar local problem and complementary witness overlap still open | Final self-similar theorem proves exact $2{:}3$ only; complementary $T=Q/8$ witness is asymptotically injective. General BP2+ stays OPEN |
| T04 | Fixed positive rich coverage treated as sufficient | Current reciprocal-multiplicity/tail accounting supersedes the inference; a quadratic uncovered tail cannot be ignored |
| T04 | Path count $2^m$ or ten observables treated as input/output support | Scalar histories collide; use audited distinct-input entropy. Ten coordinates have unbounded scalar values; output gap remains OPEN |
| T04 rendering | Malformed `164D,2^{-t}` and duplicated/corrupted address-note sections | Preserve archives; the complementary report's explicit $D<2^t/164$ conclusion is recorded, not silently reconstructed from malformed TeX. Old address-note OPEN wording is superseded by final theorem |
| Notation | Both cubic threads use $P_3$; several reports use Q for different objects | Retain T01 $P_+$, T02 $P_4$, T03 $Q_E$, T04 $P_-$ in repository identity tables; local notation stays source-specific |

No unresolved disagreement about the four fixed polynomial identities or their
OPEN ultimate status was found in the recovered final records. None of the
resolved items authorizes broadening a failure, changing a conjecture, or
claiming novelty.

## Source registry

Locally supplied documents are cited by filename, section, and hash, avoiding
private machine paths in repository documentation. They are not newly copied
into the original manifest archive. A file's availability is not a claim that
all its external dependencies were independently verified.

| ID | Document / authority | Date and principal locators |
|---|---|---|
| MASTER | `00_MASTER_HANDOFF.md` | 11 Sep; §§4–8 shared progress, §§11–13 supervisor direction and authority |
| T01-FINAL | `T01_Norm_Trace_Quadratic_Research_Checkpoint.md` | 10 Sep; §§1–2 separate benchmark/transfer, §§5–7 scoped tests, §8 stop |
| T01-STATE | `T01_CURRENT_STATE.md` | 10 Sep; §§4–8 cubic proofs/failures; §§12–15 final branch and scope |
| T02-FINAL | `T02_C4_REVIEW_ACCEPTANCE_AND_HANDOFF(1).md` | 10 Sep; accepted state, companion audit, exact retirement and next gate |
| T02-STATE | `T02_CURRENT_STATE.md` | 10 Sep; §§5–12 C2/C3/C4; §§17–20 gate and provenance |
| T03-FINAL/STATE | `T03_RESEARCH_RECORD_20260910.zip::output/T03_CURRENT_STATE.md` | 10 Sep; identical to supplied current state; §§4, 7, 13–15 govern latest root cycle |
| T04-FINAL/STATE | `T04_CURRENT_STATE.md` in the source archive and supplied export | 10 Sep; §§4.9, 6–7, 13–15 govern affine cycle and scope |
| C0 | `Phase_C0_Corrected.md`, `C0_CORRECTION_LOG.md` | Corrected 3 Sep; theorem C0.1, §§5–6; signature, radius and quartic-scope corrections |
| T02 companions | `Phase_C2_Hybrid_Carrier_Structural_Lemma.md`, `C2_PRECISION_ADDENDUM.md`, `C2_C3_REVIEW_CHANGE_LOG.md`, `Phase_C3_Ramified_7_Adic_Input_Cost.md`, `Q1_QGT1_RATE_TABLE.md` | Controlling inherited analytic statements and corrections |
| T02 C4 companions | `Phase_C4_Higher_Ramified_Precision.md`, `C4_SIGNED_RATE_LEDGER.md`, `REFEREE_REPORT_C4.md` | All-m analytic local theorem; §§5–6 rates; internal review scope distinct from external review |
| T03 cycle | `TCRC_Finite_Covers_m1_m2.md`, `TCRC_Finite_Covers_m3_m4.md`, `TCRC_History_Parameters.md`, `TCRC_Root_Algebra_Pair_Maps.md`, `TCRC_Triangle_Closure.md` | Five latest supporting reports in archive `output/`; each read in full |
| T04 cycle | `sacc_candidate_input.md`, `sacc_input_audit.md`, `sacc_pair_states.md` | Latest affine input theorem, independent input audit, exact ordered pair-state notes; each read in full |
| T04 previous checkpoint | `parity_twisted_cubic_checkpoint.md` | 8 Sep; fixed-base obstruction retained, older general-affine assignment superseded |
| T01 recovery docs | `recovery_2026-09-20/T01/T01_RECOVERY_ADDENDUM_2026-09-20.md`, `MANIFEST.md` | 20 Sep documentation; 10 Sep mathematical cutoff; reports source recovery, original package files not included in this intake |
| T02 recovery docs | `recovery_2026-09-20/T02/T02_RECOVERY_ADDENDUM_2026-09-20.md`, `T02_RECOVERY_MANIFEST.md` | 20 Sep documentation; 10 Sep mathematical cutoff; reports omitted dependency package, original package files not included in this intake |
| T03 recovery docs | `recovery_2026-09-20/T03/T03_SOURCE_RECOVERY_ADDENDUM_20260920.md`, `T03_SOURCE_RECOVERY_MANIFEST_20260920.md` | 20 Sep documentation; designates final TCRC package and reports four recovered originals not received here |
| T04 recovery docs | `recovery_2026-09-20/T04/T04_RECOVERY_NOTE_2026-09-20.md`, `T04_RECOVERY_MANIFEST_2026-09-20.md` | 20 Sep documentation; clarifies final recoverable package, tower locators and retained provenance gaps; larger archive not received here |
| SHARED-OLD | Frozen Phase A reproduction/change log, `PHASE_B_STATE.md`, mechanism/failure/open-lemma libraries in `history-sources/` | Earlier proof/reconstruction provenance as accepted by later records; files unchanged |

SHA-256 identities of the central exports:

```text
00_MASTER_HANDOFF.md
b5ea32664e1a755faa4b29ad21848e11f3b16eef94b451d5b3ed5e9d18f6b250
T01_Norm_Trace_Quadratic_Research_Checkpoint.md
a9de1edb1ebc43465de7e12cd2e815e8647b4199a0c303afff2e4a8815abc0db
T01_CURRENT_STATE.md
2095cb7b4a5f7d848dea1356956ad36f5303e4037b13b2efe7fa32b0c08f2624
T02_C4_REVIEW_ACCEPTANCE_AND_HANDOFF(1).md
8d093d4111e04dfd42d6bf13117305809beffceb44f1e8d81f16b64d4ef7c714
T02_CURRENT_STATE.md
e4ba2cbf3871d71ac45526fa7b16a0f6e468f13cce13261adafec5547830f480
T03_CURRENT_STATE.md
8048b4d9d3121757a28abe90e227fa5fba84cb4eb172bef8b6aa7186b3792850
T04_CURRENT_STATE.md
17d5bb792fc4a9903bac337e0b96d283bad551796ddccaa3b8965816b8ac59b5
Phase_C0_Corrected.md
8ef3670bb8903b2f851b1bba594435d8635882849dae37912baadf6c49eb85be
C0_CORRECTION_LOG.md
5da48e6372e1ea10af8d395c30faff6e7676bc546749ffa5fc36765a7b040480
```

The T03 archive has SHA-256
`5c51114ec0fa2663b586665db30bc6648f1e3a1beaae2e578099b9abc6e85430`.
The curated supplement manifest records provenance and hashes for additional
companions. Existing `research/manifest.json` continues to describe only the
original 39 archived files; it was not rewritten or expanded by this migration.
