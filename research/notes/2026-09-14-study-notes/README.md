# Study notes: from unit distances and sum-product to four polynomial tracks

Prepared **14 September 2026**, explaining the recorded research through
**10 September 2026** and the **11 September reconciliation**.

All four fixed targets remain **OPEN**. The offline work produced supporting
theorems, exact finite constructions, transfer implications, and precise reasons
that several proposed methods fail. These notes explain that progress without
adding a research result or changing a track's status.

## Reading order

Start with the shared explanation, then read the tracks independently.

| Note | Main question it explains |
|---|---|
| [Shared foundations](00-shared-foundations.md) | What can be carried over from the supplied OpenAI unit-distance manuscript and the frozen sum-product reconstruction? |
| [T01: cubic difference plus sum](01-cubic-plus.md) | Why did the quadratic model succeed, while the tested cubic box, digital, and rich-fiber methods failed? |
| [T02: quartic hybrid and local precision](02-quartic.md) | Why are the exact C2–C4 local improvements real progress, yet insufficient globally? |
| [T03: Eisenstein norm and adaptive radicals](03-eisenstein.md) | How did engineered norm pairs lead to Cartesianization and then to the current signed-root problem? |
| [T04: cubic slices and affine growth](04-cubic-minus.md) | Why do rich fibers and growing affine inputs still require a bound on the entire output? |
| [Sources and preservation record](SOURCES.md) | Which versions support the notes, what was inspected, and what remains unavailable? |

The intended background is elementary algebra and finite-set counting. The
shared note introduces the number-field language used later. Each track has a
worked calculation, a precise unresolved endpoint, and recall questions whose
answers appear in the note. The questions are study exercises, not new research
assignments.

## Four separate endpoints

| Track | Fixed polynomial | Recorded progress | Missing conclusion |
|---|---|---|---|
| T01 | $(x-y)^3+x+y$ | Scoped continuous/digital obstructions and an exactly injective tested rich-fiber family | No supported cubic construction remains. The separate $x^2+xy+y^2+x$ transfer has no witness. |
| T02 | $(x+2y)^4+3x-y$ | Analytic local counts through C4, including saturation at $22/49$ after both input costs | A concrete subcarrier and full-support bound with a positive net rate |
| T03 | $x^2+xy+y^2$ | Exact adaptive inputs and finite image counts through $(32,269)$; root-cover identities and scoped failures | Uniform RC15/4 on the actual adaptive levels |
| T04 | $(x-y)^3-3(x+y)$ | Proved distinct-input entropy for one complementary-unit affine system | A strict full-image exponent gap for that system |

This table restates the controlling state records [S-T01–S-T04](SOURCES.md).
It does not transfer results between tracks. The shared corrected rank-one
quadratic theorem solves none of these four fixed targets.

## How to read the claims

Each numbered study item has an ID, a status, explicit scope, and a source
locator. These are **documentary claim records**, version 2026-09-14; they are
not newly proved mathematical claims. The polynomial, quantifiers, hypotheses,
dependencies, and remaining gap are stated in the item or its note's opening.
Source versions and hashes are in [SOURCES.md](SOURCES.md).

- **PROVED, reported** preserves an identified proof status in the source
  system. Reading its statement does not independently verify its proof.
- **PROVED, argument inspected** means the relevant written argument was read
  for explanation here. No independent proof audit or dependency recertification
  was performed.
- **CONDITIONAL** marks an application with an unproved premise, even when the
  implication itself is proved.
- **FAILED** applies only to the named family, inference, or counting method.
- **EXPERIMENTAL** marks recorded finite evidence, with its range and arithmetic
  specified; no mathematical computations were rerun for these notes.
- **EXTERNAL RESULT** identifies supplied external material. The sum-product
  result is accessed through the frozen reconstruction, not a newly retrieved
  primary paper. No publication-status or novelty check was performed.
- **HISTORICAL / SUPERSEDED** preserves earlier reasoning while identifying
  the later controlling correction. Explanatory interpretations add no theorem.

## Preservation boundary

Only this new dated study folder is intended as a repository addition. Existing
SPECs, STATUS files, archives, manifests, copied references, research code, and
inherited uncommitted changes are preserved. The notes are a reading companion;
they do not become a replacement checkpoint or a new task queue.

This task used local sources only. It performed no proof search, mechanism
pivot, expanded experiment, imported-program execution, literature search,
commit, or publication. Temporary text extractions and preservation hashes are
under ignored `scratch/study-notes-2026-09-14/`.
