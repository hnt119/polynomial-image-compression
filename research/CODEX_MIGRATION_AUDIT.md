# Codex migration setup audit — 2026-09-14

**Documentation/setup only.** Research cutoff remains 2026-09-10. No new proof,
candidate, mathematical search, literature review, or novelty claim is added.
Recorded source results are not independently recertified by this setup.

## Repository selection and initial Git state

The calling ChatGPT project mirror had no `.git` directory. A local search
located two older project checkouts:

| Checkout name | HEAD / branch | Initial state |
|---|---|---|
| `polynomial-image-compression` | `484df0c`, main | Seven modified tracked files and four untracked migration registries; no staged changes; no remote configured |
| `polynomial-image-compression-github` | `b4578ad`, main | Clean; one commit ahead of its locally recorded origin/main; origin points to `hnt119/polynomial-image-compression` |

The first checkout contains the 11 September reconciliation and was selected
as the current local source. The second contains older orientation/state and
was inspected for provenance only. No remote was fetched, so “ahead” describes
the local tracking ref, not independently verified live GitHub state. Their
distinct histories were not merged or reset.

This new working directory copies the selected checkout with its Git history,
index and uncommitted work. The original checkouts were left untouched. No Git
history was invented and no baseline commit was made. Private absolute source
paths and full baseline hashes are in `local-only/setup-audit/baseline.json`.

The inherited modified files are `README.md`, `research/PROJECT_HISTORY.md`,
`research/tracks/README.md`, and the four track `STATUS.md` files. The inherited
untracked files are `research/MECHANISM_LIBRARY.md`, `FAILURE_LIBRARY.md`,
`OPEN_LEMMAS.md`, and `MIGRATION_CONFLICTS.md` (all under `research/`). They remain
uncommitted. Only the README receives additional setup links from this task;
all other inherited migration records remain byte-identical.

## Reconciliation against migration authority

The master handoff, all four state exports, T01 norm–trace checkpoint, T02 C4
acceptance/handoff, curated import manifest, existing track STATUS/SPEC identity
records, and relevant final-cycle summaries were inspected. T04's independent
input audit was read. Companion files are preserved with their manifests;
this task does not claim to have re-audited every companion proof. The existing
11 September reconciliation matches the controlling fixed targets and frontiers.

| Area | Resolution retained |
|---|---|
| Shared C0 | Corrected integral rank-one theorem and log control; not a general full-rank theorem or quartic result |
| T01 | Plus-sign cubic remains OPEN; conditional block/digital witnesses superseded by scoped obstructions. Latest P0 benchmark is a separate OPEN branch; no witness to its proved transfer premise |
| T02 | C2–C4 corrections and accepted analytic counts control. The 22/49 full inverse-image factor stabilizes. Retire only the specified full-interval uniform-packing architecture; actual quartic target OPEN |
| T03 | Later adaptive radicals/TCRC replace PTCR as selected frontier, without closing historical approximate PTCR. RC15/4 uniform signed-root support remains OPEN; finite certificates do not give an asymptotic theorem |
| T04 | Current affine input theorem and pair-state notes control; full output gap OPEN. Path count and ten observable coordinates are not scalar input/output counts |

See [the current map](CURRENT_PROJECT_MAP.md) for exact source paths and section
locators, and [the preserved conflicts](MIGRATION_CONFLICTS.md) for detailed
supersession history. No old statuses, conjectures, failed hypotheses, SPECs,
or original archive bytes were silently rewritten.

## Retained unresolved records

- **MC-01:** T01 SPEC still contains obsolete OPEN digital-witness prose. Newer
  status clearly supersedes it; SPEC is preserved, with no target ambiguity.
- **MC-02:** T04 product-tree attribution mismatch remains; use the recorded
  internal proof locator, without fabricating external attribution.
- **MC-03:** No separately titled later T03/T04 final checkpoints were recovered.
  Their designated frozen state files and companions are used explicitly.
- **MC-04:** T04 depth-30 numeric claim lacks the matching retained certificate;
  available source growth data stopped at depth 24. No large count was rerun.
- **MC-05:** T03 standalone F25 certificate and some early T04 constants/tower
  locators remain unrecovered. Old per-thread omissions do not imply sources
  are still missing project-wide; corrected C0/shared material is now present.

These source/provenance issues do not require changing the four OPEN targets.
They remain limits on future dependent claims. Additional supplied checkpoints
must be reconciled before they can supersede this map.

## Actual setup changes

- Expanded root `AGENTS.md` with objective, source hierarchy, track identities,
  claim vocabulary, provenance, research/documentation boundaries, quantitative
  ledger, experiments/artifacts policy, and verification requirements.
- Added setup guide, concise map, this audit, a construction-ledger template,
  and a relative-path/hash inventory for 42 local migration reference files.
- Added a local integrity checker. Updated the existing link checker to skip
  ignored private/scratch/environment directories; original archive checks stay
  active. Added regression tests for corruption, missing/escaping paths, and
  current-versus-private historical link handling.
- Added two README setup links. No historical status text was edited.
- Copied the 42 references verbatim into ignored `local-only/migration/`;
  the mirror originals and curated supplement remain untouched. Their original
  private-path manifest and reference PDFs are not proposed for Git commits.
- At the parent mirror only, added `AGENTS.override.md` and a README that direct
  future tasks to this Git root while preserving the protected parent AGENTS.

The original 39-file manifest and all four SPECs remain unchanged. The old
JSON track registry stays a dated historical snapshot. No automatic research
startup, model change, remote mutation, or external publication was configured.

## Verification and review artifacts

The setup checks compare source size/SHA-256 against both the new inventory and
the original import manifest, validate T03 ZIP CRC and its 43 manifest entries,
check duplicate current-state copies, and compare C4 code/results identities.
Existing regression tests and `experiments verify` cover the finite computational
baseline; they do not execute the imported research programs. Results are saved
in `local-only/setup-audit/verification.txt` after running the checks.

Validation passed on 2026-09-14: 39 archived sources and 33 current Markdown
documents; 42 local references and 43 T03 archive manifest entries; 23 unit
tests; 159 finite baseline checks; and `git diff --check`. The setup regressions
include intentional same-size corruption and missing-path rejection. No
imported research code or serialized computation state was executed/loaded.

`local-only/setup-audit/setup-only.patch` shows this task relative to the copied
uncommitted baseline. `tracked-vs-head.patch` shows all tracked changes including
inherited migration work. `untracked-files.patch` includes new files and the
inherited untracked registries; `parent-entrypoints.patch` covers the two parent
additions. Private reference contents are excluded from patches; their inventory
and hashes are reviewable. The Git index remains unchanged and nothing is committed.

## Recovery-document intake — 2026-09-20

Eight supplied Markdown files were copied verbatim into
`local-only/migration/recovery_2026-09-20/`, grouped under T01–T04, and added to
the hash inventory. The inventory now verifies 50 immutable source files. The
generic T01 `MANIFEST.md` name is preserved inside its track directory.

The intake did not include any source ZIP, extracted `originals/` tree,
executable, JSON manifest, message transcription, or other artifact named by
the recovery documents. Those documents are therefore evidence about the
reported recovery package and its stated source locators; they are not a local
byte-level substitute for the absent originals. Existing local originals were
matched by their recorded identities where possible, including the T04 current
state, SACC notes, and supplied tower PDF.

The recovery documents all declare a 10 September mathematical cutoff. They
resolve the repository designation of the T03 final package and clarify the
T04 recoverable package, but they do not supersede later 16 September records
or change any target status. No embedded assignment was executed, no research
program was run, and no external source was consulted.
