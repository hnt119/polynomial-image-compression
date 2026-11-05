# Three-branch continuation: verification and local handoff

2026-09-16, continuation v1. T01, fixed polynomial
\(P(x,y)=(x-y)^3+x+y\). This record concerns the current continuation
cycle only. Earlier finite-gadget files and unrelated inherited work are
preserved.

## Scope and source availability

The active request explicitly commissioned research on composability of the
six-point gadget: symbolic affine analysis, bounded exact multilevel tests,
one nonlinear extension after a scoped affine obstruction, and a report.
The network policy was **strictly offline**. No internet, dependencies,
external novelty review, arithmetic tower, or external publication was used.

The immediate controlling finite source was the preceding
[three-branch report](../2026-09-16-three-branch-lift/README.md).
Initial Git status/diffs and the mandatory setup, project map, migration
audit, master handoff, T01 current-state/final companion, SPEC/STATUS,
conflict/mechanism/failure/open-lemma records, and construction template were
read in the task's orientation and relevant sections revisited for this
continuation. The source hierarchy and fixed plus-sign cubic were retained.

The named full historical digital checkpoint
Regular_Digital_Carry_Collapse_Universal_NoGo_Checkpoint.md and rich-fiber
checkpoint Cubic_Target_Exact_Elements_and_Candidate_Test.md remain
**MISSING SOURCE / PROVENANCE FILE**. Their reported statements and scopes
are available in T01 current state and the preceding
[source audit](../2026-09-16-three-branch-lift/source-scope.md); their complete
proofs were not independently recertified. The new literal-iteration proof
is self-contained and does not depend on either missing proof.

## Mathematical audit

The lead independently inspected the complete arguments in the affine and
direct-iteration companions. This includes:

- All fourteen finite-gadget savings, the full interblock witness table,
  both coordinate-displacement templates, and the absence of further fibers.
- Common-scale collision preservation; coefficient classification of all
  affine-line identities; the exact anchor equation and endpoint requirements.
- Difference-mass and finite-displacement bounds, explicitly distinguished
  from actual-image bounds without an exhaustive-fiber hypothesis.
- The cross-copy survival equation, its exceptional center differences,
  and the linear count of inherited equality edges.
- Exact literal input counts and branch intersections; the power-of-two
  congruence injection, full omitted-pair count, and actual density tending
  to one.
- The sufficiently separated-copy polynomial count, including its finite
  exceptional set and common-scale version.

The lead supplied the strict-exponent recurrence proof and quadratic
output-preserving pair maps. A separate agent independently checked the
entire rates/pair-map companion and found no mathematical defect. The
all-level tripling and growing-prime-support statements for the nine rules
were checked from the explicit parameter selection, prime-integrality or
interval argument, and surviving input points; these input claims do not
imply an output recurrence.

A final independent internal review compared the main report with the
proof companions and stored finite summary. It checked the numerical
fractions, additional slice identities, scope qualifications, and the
single next obligation. Its two wording findings were corrected: constant
*terms* of affine output polynomials, and stale pending-audit labels.
The lead also corrected an aligned-equation line break in the new direct
companion. No change to the experiment algorithm or counts was needed.

These are internal mathematical audits, not external peer review or a
novelty determination. The original real-set power-saving target is OPEN.

## Finite computation and reproducibility

Announced research limits: at most 16 explicit rules, 120 continuation
steps, 162 distinct inputs per evaluated level, 3,000,000 exact polynomial
evaluations, and 90 research CPU seconds. The code was inspected before
execution. The preceding 980-attempt search was not rerun.

Command: python3 -m experiments.three_branch_continuation.
Runtime: CPython 3.12.7, standard library only. All equality and collision
arithmetic uses fractions.Fraction; no random choices or floating-point
equality tests occur. The nine parameter rules were fixed before execution,
then each evaluated for three successive levels from the six-point gadget.

Actual research use:

- 9 rules, 27 continuation steps, inputs \(6\to18\to54\to162\).
- 265,392 polynomial evaluations:
  \(36+9(324+2916+26244)\), including the initial certificate.
- 7.432394 measured research CPU seconds; 7.607706 measured wall seconds.
- No research-run error, budget overrun, or additional candidate enumeration.

The lossless records retain every input/output, the complete scalar pair
matrix, output multiplicities, all nine block supports, block membership
masks encoding every higher intersection, pairwise intersection counts,
every difference slice, and original-template connected-component counts.
Additional equalities are marked unexplained by those two templates, not
accidental. Exact denominators, numerator heights and diameters are recorded
at each level. All pairs in the same scalar set squared are counted.

Portable summary:
[examples/2026-09-16-three-branch-continuation.json](../../../examples/2026-09-16-three-branch-continuation.json).
Lossless records, initial certificate, and provenance/verification JSON are
under local-only/runs/T01/2026-09-16-three-branch-continuation/.
Those ignored files must accompany any local handoff separately.

| Artifact | SHA-256 |
|---|---|
| Executed and final experiment code | 505a6cbd7681f85422cd6da7793d16d561de95937831110694d83c9ce2b33888 |
| Test source | 9a95f260c9ff74a6ac427074d1af7ca19d577e9e1dc47226d2187b6b6fb25999 |
| Portable summary | cbd0d1d964b5089b70cb5773ffbcd95217264fddcdbf285fdd6dae601b542b18 |
| Initial six-point certificate | 183c714530bf4920f42527264fab7b5fb67c408f66fd6bddde296222bcc3a879 |
| Serialized input-rule record | 7842d4b7843ab7586899d8c2e76b36e0a2e8085d5143adb0d43bac7aed4ac799 |

The four targeted tests passed, using 360 additional polynomial
evaluations. All 27 raw certificates passed a read-only structural audit
of hashes, pair matrices, multiplicities, blocks, slice masses and the
savings decomposition, without new polynomial evaluations. That audit
used inefficient list membership; its CPU duration was not measured and
is unavailable, as explicitly recorded in local verification JSON. It
completed before a requested stop, with no residual process. The research
run timing above is separately measured; no aggregate timing is invented.

## Final repository checks

- python3 -m unittest discover -s tests -v: **PASS, 52 tests**.
  This includes the four new tests, adding another 360 continuation-module
  polynomial evaluations to the earlier targeted 360. Thus this cycle's
  research run plus its two executions of these new tests used 266,112
  continuation-module polynomial evaluations. Other inherited regressions
  are separate finite checks, not candidate searches.
- python3 -m experiments verify: **PASS, 159 finite baseline checks**.
- python3 scripts/check_codex_setup.py: **PASS**, 42 local references,
  43 T03 manifest members, original import identities, duplicate states
  and C4 hashes. No research code is run by that integrity check.
- python3 scripts/check_repository.py: **PASS**, 39 archived sources
  and local links in 73 Markdown files.
- git diff --check: **PASS**.
- New code, test, summary, initial certificate, serialized rule record,
  and all 27 raw-file hashes: **PASS**, checked against recorded hashes
  without rerunning the continuation.
- The preceding cycle's code, tests, portable counts and complete raw
  gadget data match their preserved verification hashes.
- Tracked diffs and the newly created files were inspected separately.
  The new Markdown files passed control-character and trailing-space
  checks. Existing archive and SPEC files remain unchanged.

These checks test packaging, source integrity and finite regressions; they
do not prove the asymptotic research objective.

## Changes and retained gaps

New work consists of the main report, three mathematical companions, this
verification record, one experiment module, four tests, a portable summary,
and ignored lossless data. Dated addenda in T01 STATUS and the project map
point to the new scoped results. No old archive, SPEC, finite-gadget report,
canonical JSON, or unrelated research result is rewritten.

Literal iteration and sufficiently separated copies fail in their proved
scopes. Bounded inventories of the stated slice moves fail as complete
compression certificates. General adaptive affine constructions, useful
partial returns under the quadratic pair motion, and the ultimate target
remain OPEN. The report retains exactly one next proof obligation, without
launching further work.

All earlier modified/untracked work remains inherited. No reset, clean,
staging, commit, push or remote change occurred; this cycle remains
uncommitted.
