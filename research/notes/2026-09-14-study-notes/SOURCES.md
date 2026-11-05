# Sources, versions, and preservation record

[Study index](README.md)

Version **2026-09-14**. This register identifies the exact local bytes used to
prepare the study notes. Hashing establishes file identity, not mathematical
correctness. The notes have no authority to supersede a research checkpoint.

## Source hierarchy and availability

Current user instructions govern this documentation task. For recorded
mathematical state, the applicable final checkpoint/correction chain controls,
then each current-state export, then the master handoff, then reconciled
repository history. Formal proof evidence remains the argument itself.
A status summary can report a proved result without independently proving it.

The starting orientation used [CODEX_SETUP](../../../docs/CODEX_SETUP.md),
[CURRENT_PROJECT_MAP](../../CURRENT_PROJECT_MAP.md),
[CODEX_MIGRATION_AUDIT](../../CODEX_MIGRATION_AUDIT.md), and all four tracks'
SPEC and STATUS files. Those existing files and their inherited uncommitted
changes were preserved. Original archive identity remains in
[manifest.json](../../manifest.json); separate local-migration identity remains
in [CODEX_SOURCE_MANIFEST.json](../../CODEX_SOURCE_MANIFEST.json).

Private paths below are repository-relative locators. Their files remain in
ignored `local-only/`; they were not copied into these notes. A Git-only handoff
therefore does not include the private references. The source register records
only the references needed to understand this companion, not private manifests
or administrative records.

The primary sum-product paper is **not present in the recovered source bundle
used here**. Phase A's supplied bibliography identifies T. F. Bloom, W. Sawin,
C. Schildkraut and D. Zhelezov, *The sum-product conjecture is false for real
numbers*, arXiv:2605.28781v1, 27 May 2026. This is a transcription of that
bibliography, not an independently checked citation or publication-status claim.
The human remarks manuscript, frozen conceptual guide, discovery record, and
separate source audit named by Phase A were not available in this bundle and
were not claimed as read. The local OpenAI unit-distance manuscript **was** read
at the locations identified below. No network retrieval or novelty check was
performed. T01's earlier arithmetic literature survey is historical work, not
part of this offline documentation task.

## S-REG — reconciled correction and claim libraries

These four existing documents were consulted for the relevant mechanisms,
failures, gaps, and supersessions. They are state/provenance guides, not
substitutes for formal proofs. All describe the 11 September reconciliation.

- `research/MIGRATION_CONFLICTS.md` — SHA-256 `cac0563ca1a3930829e2f16cb5e64e90e314c9e061fccf2bbbc3d2f90c81f1f0`.
- `research/MECHANISM_LIBRARY.md` — SHA-256 `69bf8666425623c5199ca9c04a699548ab4b4cf8dc2b0342a447e8d2465b428e`.
- `research/FAILURE_LIBRARY.md` — SHA-256 `4fe9757355ab93b5ef50a0b2c9efa91a99cf4a1094965d4c7a3196cf766d1217`.
- `research/OPEN_LEMMAS.md` — SHA-256 `4c4395037a444c0c90410a834cb05b7b04cb07afd56b5f5e90739ab6e86ef091`.

Specific boundaries retained:

- **MC-01:** older T01 digital SPEC routes are superseded by the later scoped
  obstructions. The old documents remain unchanged.
- **MC-02:** the residual cubic product-tree attribution is corrected to the
  internal three-prime checkpoint, historically cited as §D.5, Proposition 5.
  The reconciliation supplies that locator; this task did not audit the
  underlying checkpoint or attribute its lemma to the external sum-product paper.
- **MC-03:** no separately titled later final checkpoints are located for T03
  or T04. Their current states plus designated companions control; no missing
  checkpoint was reconstructed from a title.
- **MC-04:** the T04 depth-30 count quoted in the candidate note lacks matching
  retained raw evidence in the reconciliation. It is omitted from the study
  account; no raw data were represented as newly inspected.
- **MC-05:** the standalone T03 F25 certificate and certain earlier T04
  numerical constants remain unavailable at their stated locators. The notes
  neither invent them nor claim to have read them.

## Individually identified sources

Each SHA-256 is computed from the existing file on 14 September 2026. Where a
source lacks an explicit version date, the hash identifies the version without
inventing one. Section locators in the notes refer to these versions.

### S-UD

`local-only/migration/research_supplement/shared/03-unit-distance-proof.pdf`

Supplied OpenAI manuscript, Planar Point Sets with Many Unit Distances. No date inferred. Theorem 1.1; Proposition 2.2; Theorem 2.3; Lemmas 2.4–2.6; Proposition 3.8 and Remark 3.9. Relevant written arguments read through PDF text extraction; page 12 also rendered and visually inspected. No independent proof audit.

SHA-256: `62b5de8cacdfbc0f13ae1940aa81659cd233e6945b936612fbeab0ab8ab3d383`

### S-A

`local-only/migration/research_supplement/shared/05-Phase_A_Sum_Product_Reproduction_FINAL_FROZEN.pdf`

Final frozen Phase A reconstruction. Full extracted text read, including source map and references. Supplies the sum-product definitions, inequalities, and attribution used here; does not replace primary-paper verification.

SHA-256: `55741837f06336e072b390560dadc3ab7e087a946da69599c292c671db64f514`

### S-A-LOG

`local-only/migration/research_supplement/shared/06-Phase_A_FINAL_FROZEN_Change_Log.pdf`

Companion final correction log; read in full. Controls corrected lattice factors, regulator scope, directness, and parameter choices.

SHA-256: `edfead13a44af821a9d320e6dca989179972444959bca5578b5c3984b24bded1`

### S-B

`research/history-sources/PHASE_B_STATE.md`

Historical Phase B synthesis, Validated abstraction principles 1–8 and Rejected principles. Read; interpreted with the master handoff and 11 September reconciliation. Its historical next-direction paragraph is not an active assignment.

SHA-256: `ec695630f89fdc587045710f560324ee6904a8169fcf5e7e261490349414ea6b`

### S-C0

`local-only/migration/research_supplement/shared/Phase_C0_Corrected.md`

Dated 3 September 2026. Theorem C0.1 and §§5–6 are the formal positive rank-one argument inspected for exposition. Dependencies were not independently recertified.

SHA-256: `8ef3670bb8903b2f851b1bba594435d8635882849dae37912baadf6c49eb85be`

### S-C0-LOG

`local-only/migration/research_supplement/shared/C0_CORRECTION_LOG.md`

Correction companion, read. Controls hypotheses, real-field choice, and quantitative corrections to earlier C0 versions.

SHA-256: `5da48e6372e1ea10af8d395c30faff6e7676bc546749ffa5fc36765a7b040480`

### S-MASTER

`local-only/migration/sources/00_MASTER_HANDOFF.md`

Migration snapshot dated 11 September 2026; read in full. Shared architecture in §§4–7 and novelty caution in §8. Track-specific final records outrank its summaries where applicable.

SHA-256: `b5ea32664e1a755faa4b29ad21848e11f3b16eef94b451d5b3ed5e9d18f6b250`

### S-T01

`local-only/migration/sources/T01_CURRENT_STATE.md`

T01 state export, research cutoff 10 September 2026. §§4–6 support historical successes and scoped failures; §§7–8, 12–15 identify remaining gaps. Reported proof status retained; old cubic proofs were not independently audited here.

SHA-256: `2095cb7b4a5f7d848dea1356956ad36f5303e4037b13b2efe7fa32b0c08f2624`

### S-T01-FINAL

`local-only/migration/sources/T01_Norm_Trace_Quadratic_Research_Checkpoint.md`

Dated 10 September 2026, before the T01 export. Separate P0=x²+xy+y²+x branch. §§2.1–2.3 transfer argument and §§5–7 family/rate calculations read for exposition; §8 final verdict. It cannot replace the cubic target.

SHA-256: `a9de1edb1ebc43465de7e12cd2e815e8647b4199a0c303afff2e4a8815abc0db`

### S-T02

`local-only/migration/sources/T02_CURRENT_STATE.md`

T02 state export, research cutoff 10 September 2026; read. §§4–6 local progress, §§7–11 global carrier and rates, §§12–13 failures/open obligations, §19 evidence boundaries.

SHA-256: `e4ba2cbf3871d71ac45526fa7b16a0f6e468f13cce13261adafec5547830f480`

### S-T02-FINAL

`local-only/migration/sources/T02_C4_REVIEW_ACCEPTANCE_AND_HANDOFF(1).md`

Dated 10 September 2026; read in full. Accepted state, Companion audit and provenance, and final handoff. Records acceptance of the C4 analytic proof with the specified failure scope; distinguishes external review from internal companion checks.

SHA-256: `8d093d4111e04dfd42d6bf13117305809beffceb44f1e8d81f16b64d4ef7c714`

### S-C2-LOG

`local-only/migration/research_supplement/T02/phase_c3/C2_PRECISION_ADDENDUM.md`

Seven-point C2 precision correction companion; read. C2 formal results are reported here through the state and its correction chain, not claimed as independently audited.

SHA-256: `c747922830646d3311cb106ac2b11b7ee80e30e3a8c99696df71bfa0d378d032`

### S-C3-LOG

`local-only/migration/research_supplement/T02/phase_c3/C2_C3_REVIEW_CHANGE_LOG.md`

C2/C3 review corrections supplied 8 September 2026; read. C3 universal optimization is reported from the retained source system; its full original proof was not independently audited for this task.

SHA-256: `016afcd90e64b0d22f5267e3f1f05960465baacf19cf080687bfeebd0a0dc901`

### S-C4

`local-only/migration/research_supplement/T02/phase_c4/Phase_C4_Higher_Ramified_Precision.md`

C4 analytic report accepted by the 10 September handoff. §§1–4 actual local ring/count; §§5–6 signed gate and covers; §§7–8 checks and scope. Written local and rate arguments inspected. Programs were not executed.

SHA-256: `0c438ad31f11c48ff8a74bff5454bf1eda8dd7cc3b5f8b2cd05e7dd6b582a91c`

### S-C4-RATE

`local-only/migration/research_supplement/T02/phase_c4/C4_SIGNED_RATE_LEDGER.md`

Dated 10 September 2026; explicitly a documentation extraction of existing rates, not a new optimization. Read in full; used for the missing quantitative support obligation.

SHA-256: `76afd88f997cdf5385dda7463654e3a164ef8044ed86cd066ef8e0fd52b4fbd8`

### S-T03

`local-only/migration/sources/T03_CURRENT_STATE.md`

Controlling T03 current state, research cutoff 10 September 2026; read. §3 adaptive definitions; §§4.1–4.7 exact identities and finite results; §§5.2–5.10 historical families; §6 scoped failures; §7 RC15/4; §§13–15 final frontier and limitations.

SHA-256: `8048b4d9d3121757a28abe90e227fa5fba84cb4eb172bef8b6aa7186b3792850`

### S-T03-ZIP

`local-only/migration/research_supplement/T03/T03_RESEARCH_RECORD_20260910.zip`

Frozen supporting archive. Member inventory inspected before selective extraction of the five Markdown reports listed below. Those reports were read in full. No Python/C++ program, JSON computation, or pickle object was executed or deserialized.

SHA-256: `5c51114ec0fa2663b586665db30bc6648f1e3a1beaae2e578099b9abc6e85430`

### S-T04

`local-only/migration/sources/T04_CURRENT_STATE.md`

Controlling T04 state, research cutoff 10 September 2026; read. §§4.3–4.8 supply local, transfer, trace, coverage and digit claims; §4.9 and §5.10 give current input progress; §7 and §§13–15 distinguish active from historical open endpoints.

SHA-256: `17d5bb792fc4a9903bac337e0b96d283bad551796ddccaa3b8965816b8ac59b5`

### S-SACC-INPUT

`local-only/migration/research_supplement/T04/sacc_candidate_input.md`

Designated final affine companion. Read in full: fixed system, separated-block lower bound, occupation upper bound and finite evidence. Large quoted numerical data are subject to MC-04 below.

SHA-256: `e98ebe18d94698a1d79f8f9157f61e455723c31cc18dc2f803189642e2daae28`

### S-SACC-AUDIT

`local-only/migration/research_supplement/T04/sacc_input_audit.md`

Designated input-proof audit companion, read in full. §§1–4 give graph convention, proof checks and entropy limit; §5 explicitly leaves output compression open. This is an inherited internal audit, not an audit performed for these notes.

SHA-256: `938ea55d596119fe269d06b80864864c97606eb4f7f128256b2b10905a0fc10e`

### S-SACC-PAIRS

`local-only/migration/research_supplement/T04/sacc_pair_states.md`

Designated pair-state companion, read in full. Exact transitions, finite-dimensional closure, inherited finite counts and missing output certificate. No computations rerun.

SHA-256: `dd3af5e907e7a8feff5de9fbaee3bef4a6407bb97849ac83f13c6f1db7539355`

## Selected T03 archive members

These member identities refine **S-T03-ZIP**. Only their Markdown text was
extracted to ignored scratch storage and read.

- `output/TCRC_Finite_Covers_m1_m2.md` — SHA-256 `40d6446b9b4f8bc4bb2ee2c6cc3491b7f6f3beca15ddddab3979f13671a4280f`.
- `output/TCRC_Finite_Covers_m3_m4.md` — SHA-256 `b828d2ee5a2a101dae285627f42bcfa7bec23d5b564054565c6c3e2d319ee65c`.
- `output/TCRC_History_Parameters.md` — SHA-256 `e39299e1c43335bf26e1c28549b3f6eab20edf69fb4ea0aef91cfd7953bf825a`.
- `output/TCRC_Root_Algebra_Pair_Maps.md` — SHA-256 `483a232f4344c9c354e02fd21e8f7ab78cc44557ff48ad02306600c079ac05f0`.
- `output/TCRC_Triangle_Closure.md` — SHA-256 `f6586783e413a57cebc4651cd32a48fe5a0e4a50615ef86af5ef6c23b08f6537`.

## Claim-to-source map

The SN identifiers are documentary study items dated 14 September 2026.
Quantifiers, polynomial, hypotheses, dependencies, and gaps appear in the
corresponding note; this table supplies the principal proof/status locators.
No SN item asserts a new construction or independently audited theorem.

| Study items | Principal locations and evidence |
|---|---|
| SN-S1–S3 | S-UD named theorem/lemmas and Proposition 3.8; S-A §§3–8, 10–13 and S-A-LOG; supplied arguments inspected for exposition |
| SN-S4 | S-B Validated abstraction principles 1–6; S-MASTER §§5–6; reported abstraction with displayed counting inequalities |
| SN-S5 | S-C0 Theorem C0.1, §§5–6 and S-C0-LOG; written proof inspected, dependencies not independently audited |
| SN-T01-1–3 | S-T01 §§4.1–4.5 and §6, its named earlier proof locators, S-REG MC-01; source-reported proofs/failures |
| SN-T01-4 | S-T01-FINAL §§2.1–2.3, 5–8; transfer and rate arguments inspected; premises remain open |
| SN-T02-1–2 | S-T02 §§4–6 and C2/C3 correction chain; S-C4 §§1–4; reported earlier proofs and inspected C4 local argument |
| SN-T02-3–4 | S-C4 §§5–6, S-C4-RATE and S-T02-FINAL; scoped certificate failure and open replacement obligation |
| SN-T03-1–2 | S-T03 §§5–6; reported identities, scoped obstructions, and finite exact certificates |
| SN-T03-3–4 | S-T03 §§3–4 and five S-T03-ZIP reports; exact algebra and finite certificates read, programs not rerun |
| SN-T03-5 | S-T03 §7 RC15/4, §4.7 conditional recurrence and §§13–14; open premises and their conditional payoff |
| SN-T04-1–2 | S-T04 §§4.3–4.8 and §5; source-reported historical identities/obstructions; S-REG MC-02 |
| SN-T04-3–4 | S-SACC-INPUT, S-SACC-AUDIT §§1–5, S-SACC-PAIRS; input and pair arguments inspected; scalar output gap open |

## Work performed and limits

This task added only the seven Markdown files in this dated study folder.
Temporary PDF text, one page render, and a preservation baseline were stored
under ignored `scratch/study-notes-2026-09-14/`. No existing mathematical source,
STATUS, SPEC, manifest, archive, program, or inherited change was edited.
No imported program was executed, no pickle was deserialized, and no new
mathematical experiment, proof search, external review, or literature search
was undertaken. The final checks below concern documentation and file identity.

Validation on 14 September 2026:

- `python3 scripts/check_repository.py` — passed; verified 39 archived sources
  and local links in 40 Markdown files covered by that checker.
- `python3 scripts/check_codex_setup.py` — passed; verified 42 local references,
  original import identities, 43 T03 manifest members, duplicate states and C4
  hashes, without executing research code.
- `git diff --check` — passed for the inherited tracked diffs.
- A separate check of the seven new Markdown files found no broken relative
  links, missing source IDs, trailing whitespace, or unbalanced display delimiters.
- SHA-256 comparison against the task's starting snapshot found all 90
  pre-existing nonignored repository files unchanged. The only nonignored
  additions were these seven notes. Tracked diffs therefore remain inherited.

These checks do not prove any research target. The files remain uncommitted.
