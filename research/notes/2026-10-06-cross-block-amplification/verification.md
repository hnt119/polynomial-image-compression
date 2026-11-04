# Proof audit, exact encoded histograms and budget record

6 October 2026 · version 1 · T03 · strictly offline.

## 1. Mathematical evidence

The lead inspected the written amplitude, phase-sum and independent audit
companions, independently checked each accepted claim, and wrote the
complete coordinate-switch certificate proof in returns.md. Specialist C
independently derived the phase-count and closure arguments and read the
final amplitudes.md, identities.md and returns.md. All passed.
Specialist A also checked the lead's scalar-injectivity and quartic argument.
These are internal mathematical audits, not external peer review.

| Item | Audit result |
|---|---|
| DC-M1 import | Read its chain proof and norm-matrix hypotheses; complete-orbit implication checked without inferring full-fiber information |
| Frozen source use | FG-A1 field and seven-slot relation used within their hypotheses; neither frozen amplitude rule nor FG-O1 reopened |
| Product recursion | Correct tower embedding and digit order; no complete seven-factor norm product |
| Amplitude distinctness | Every block has at most2 support positions; rotated difference has at most4, so exact coefficient recovery applies |
| Actual scalar growth | \(X\) injective on \(\mathbb Q(\xi)\), not assumed globally; \(8q^2\le n\le48q^2\) |
| Encoded norm classification | At most3 support positions per block; norm differences at most6; scale and absolute digits recovered exactly |
| Target distinctness | Distinct sign-flipped nonzero digits give distinct cosets; all zero-digit duplicates discarded |
| Assembly defect | Exact whole-source formula checked; explicitly not used alone as a norm-inequality argument |
| Full norm test | Mixed terms included; nonzero quartic leading coefficient and separate sign factorization checked |
| Source population | All \((8q)^2 4^r(6q)\) label choices charged; actual source count bounded above despite projection repetitions |
| Iteration | Scalar relation reversible and identical in both charts; \(D,\Gamma\) sign/swap invariant; arbitrary finite paths covered |
| Quantifiers and constants | \(r\ge8\), low-certificate mass \(n^2/2\), cap4 and fixed-exponent contradiction checked |
| Quadratic phases | Nonunit residues in orthogonality included; \(q=1\) treated separately; shift labels need not be distinct |
| Scope | No upper bound on full fibers of either new completion, no actual-image lower bound, no universal factor/convolution no-go |

A useful correction during the research was conceptual: failure of the
same-multiplier identity is insufficient to exclude equal norms through
another multiplier. The accepted proof therefore counts actual norm equalities
for all independently switched coordinates. A second clarification separates
encoded cyclic edges from unidentified returns on unencoded sources.
The final theorem definition states exactly which edges and iterations it covers.

No speculative numerical result, agreement between agents, or status summary
substitutes for the complete proofs. No external theorem or novelty claim was added.

## 2. Exact histograms that are proved, and the full histograms not computed

**PROVED — encoded subset only.** For the product rule, let
\(F_\Gamma(p)=|\{s\in\Gamma:Q(s)=Q(p)\}|\), \(p\in\Gamma\).
If an absolute digit word has \(s\) nonzero positions, then
\[
F_\Gamma=6q\,2^s.
\]
There are \(8\binom rs3^s\) distinct norm values of that type.
Consequently the exact **pair-weighted encoded histogram** is
\[
\boxed{
\#\{p\in\Gamma:F_\Gamma(p)=6q\,2^s\}
=48q\binom rs6^s,\qquad 0\le s\le r.}
\]
Summing gives \(|\Gamma|=48q\,7^r=48q^2\); the encoded output
count is \(8\sum_s\binom rs3^s=8\cdot4^r\).
All these counts follow from AMP-A3's proved norm classification.
They are analytic formulas, not finite experiments.

For the quadratic-phase completion, \(\Gamma\) comprises eight disjoint
nonzero norm orbits, each of size \(6q\). Its exact encoded histogram is
\[
\#\{p\in\Gamma:F_\Gamma(p)=6q\}=48q,
\]
and its encoded norm image has eight values.

Neither histogram is a full-square histogram. For either carrier,
\(F_A(p)\ge F_\Gamma(p)\) on \(\Gamma\), with possible additional
targets outside \(\Gamma\). The full histogram, full median and full bad-tail
count are **not computed or asserted**. For the product carrier, only the
specified certificate has the proved low-tail population
\[
\#\{p:R_{\rm cert}(p)\le4\}
\ge n^2-1536q^3 4^r-48q^2.
\]
The direction \(R_{\rm cert}\le F_A\) prohibits converting this into
a full-fiber upper bound.

## 3. Shared budget defined before execution

The lead saved the policy before mathematical work in:

    local-only/runs/T03/2026-10-06-cross-block-amplification/budget.json

It charges one exact evaluation per ordered \(Q\)-pair calculation,
source/target equality-and-membership test, projective key/equality test,
or independent validation of one such test. Aborted runs would count.
Carrier arithmetic would be timed, without being separately charged as
ordered-pair evaluations.

| Allocation | Evaluations | Program CPU seconds |
|---|---:|---:|
| Shared cap | 2,000,000 | 600 |
| Discovery allowance | 1,600,000 | 480 |
| Reserved verification | 400,000 | 120 |
| **Actual discovery use** | **0** | **0** |
| **Actual mathematical program validation** | **0** | **0** |
| **Total actual use** | **0** | **0** |

Only the lead could authorize and run mathematical programs. All three
specialists had zero program allocation. No program was needed or executed:
the two mechanisms failed analytic gates before satisfying the prerequisite
for scouting. There is no research script, runtime, seed, parameter sweep
or finite run to report. Exact histogram formulas above require no enumeration.

Two directions, two finalists, zero mutations, no nested agents and no
duplicated program searches. The independent-switch extension and its iterative
closure audit enlarge the tested certificate on the unchanged product carrier;
they do not change amplitudes or introduce another candidate.
The stop was caused by two rigorously scoped mechanism failures, not budget
exhaustion. Model reasoning, tokens, credits and wall time are not program usage.

## 4. Preservation and administrative checks

Initial orientation covered status and diffs; setup/map/migration audit;
the master handoff and T03 state/target; current checkpoint and companions;
SPEC/STATUS; migration conflicts; relevant mechanism/failure/open-lemma entries;
and the construction ledger template. Missing older F25/arithmetic originals
are not dependencies of the present proofs and were not reconstructed.
Only the frozen field lemma and inspected DC-M1 are imported into new arguments.

The initial worktree already contained nine modified tracked files and extensive
untracked work. A baseline of 321 existing nonignored files, the inherited
diff and status were saved in the local run folder. Historical research
checkpoints, private sources, SPECs, canonical manifests, code and tests
are preserved. Any current handoff changes are dated suffixes, with their
exact original bytes and suffixes saved separately.

All work is local. No network, external API, download, cloud document,
package installation, literature search, staging, commit, push, reset or
cleanup occurred. The companion manifest excludes itself. File hashes
and repository checks are administrative validation, not proof audits or
mathematical program reruns.

### Final repository checks

| Check actually performed | Result |
|---|---|
| `python3 scripts/check_repository.py` | PASS: 39 archived sources; links in 185 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local references, original import identities, 43 T03 members, duplicate states and C4 hashes |
| `git diff --check` | PASS |
| Baseline preservation | PASS: 316 of 321 files unchanged; the other five differ only by the recorded dated suffixes |
| Frozen predecessor integrity | PASS: all eight companion hashes match its manifest |
| New Markdown checks | PASS: whitespace, table structure and math delimiters |
| Companion, source and accounting manifest | PASS: eight companion files, eight source files and five local accounting files |

The five suffixes update CURRENT_PROJECT_MAP, MECHANISM_LIBRARY,
FAILURE_LIBRARY, OPEN_LEMMAS and the T03 STATUS handoff. Existing contents
are preserved byte for byte. The new report and companions are separate files.
Table delimiters were corrected during packaging; those changes were formatting
only and did not change a theorem or its scope.

No code or tests were changed by this cycle, so unit tests and the finite
experiment regression suite were not rerun. All changes remain uncommitted.
