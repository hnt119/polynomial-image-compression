# Verification and provenance

T01 / sublinear cubic symmetry cycle, 2026-09-21 v1.
Fixed polynomial \(P(x,y)=(x-y)^3+x+y\).

## Research scope and source boundary

The current user attachment commissioned this offline cycle after the
completed growing-step report. The lead inspected the working-tree status,
existing changes and whitespace diff before research, and consulted the
setup/map/migration documents, master handoff, T01 current state, separate
quadratic checkpoint, track SPEC/STATUS, conflicts and relevant libraries.
The latest GS/CR report and proof companions control the frozen mathematical
inputs. Their results were used, not re-searched or recertified by finite
tests. Missing original historical digital/rich-fiber sources remain missing
and are not dependencies.

Scope was announced before new research: coordinate reuse and the
sublinear-inventory obligation, no network, no arithmetic amplification,
at most 64 carriers, 384 graphs, two million exact polynomial evaluations,
and ten million counted checks. The graph subtask had the stricter allocation
48/288, 1.5 million evaluations, eight million checks, maximum \(N=160\),
and 60 research CPU seconds. The actual maximum \(N\) was 60.

## Independent internal mathematical audit

These are proof audits, distinct from documentation and finite computation.
No external review or literature/novelty assessment is claimed.

| Claims | Written evidence | Audit actually performed |
|---|---|---|
| SC-R1–R3 | correlated-reuse, first three sections | Lead derived the claims; a separate proof agent checked injectivity, average reuse, polynomial degeneracies, signs and the monotone cubic |
| SC-D1/D2 | correlated-reuse, denominator and residue-descent sections | Lead derived the claims; a separate proof agent checked cube injectivity modulo \(p\), the \(p^2\) width argument, exact confinement and disjointness, application of GS-U3, and the nonuniform family |
| SC-Q1 | reuse-and-projections §1 | Lead and separate proof agent independently checked both substitutions, the nonzero integer product, band counts, anisotropy and scale factors |
| SC-Q2 | reuse-and-projections §2 | Both reviewers checked explicit \(\gamma_D,C_D\), positive source-pair mass, all partner differences, and the bound on the entire actual fiber |
| SC-Q3/Q4 | reuse-and-projections §§3–4 | Both reviewers checked the exact scalar interval and projection multiplicity, parameter-to-pair loss, and the external-scale collision quotient |
| SC-U1–U4 | multistep-obstruction §§1–4 | Lead independently checked the marked incidence bijection, both endpoint bands, sign normalization, spacing corollary, and completed-square geometric intersection count |

All audits passed. Clarifications retained: bounded-aspect/lower-scale
constants can depend on those fixed bounds; the geometric intersection
count concerns curve pairs, not legal returns; small-step costs at nested
cutoffs cannot be added; the prime family's gaps repeat two small gaps
and one large gap. Formatting repairs to the root note changed no proof.

The universal exponent beyond \(1/6\), the almost-full coverage witness,
and the original cubic target remain OPEN. No finite test establishes any
of the symbolic statements or the research target.

## Exact research grid and finite checks

SC-X1 is also identified as SL-X1 in the machine artifact. Its complete
finite range and every diagnostic are specified in
[experimental-summary](experimental-summary.md).
There are 36 charged model records, 35 distinct scalar sets, 216 graph
inventories, and 252 complete raw carrier/graph files.

The new module and the reused graph functions were inspected before their
single grid execution. The lead subsequently read the new implementation,
tests and the reused fiber/graph engine: the output/difference map uniquely
identifies pairs; within-fiber differences supply exactly the return edges;
components cover all \(N^2\) vertices and carry one actual output. Direct
motion oracles check three small declared grid cases. No historical grid
driver was invoked.

The reused raw field called diagnostic_only flags the all-useful inventory.
For the two frequent-step lists the additional inventory_source field
explicitly says actual-fiber diagnostic. Both frequent-step and all-useful
lists are treated as diagnostic throughout the report, irrespective of
that legacy Boolean field.

| Execution | Exact polynomial evaluations | Counted checks | CPU seconds |
|---|---:|---:|---:|
| Input-only preflight | 0 | 1,981 constructor records | 0.006970 |
| One new research grid | 37,243 | 349,851 | 1.290217 |
| Agent's five targeted tests | 576 | 3,328 pair/edge + 4,036 constructor | 0.028299 |
| Root's five prime audits | 1,000 | 1,000 full pair evaluations | 0.004796 |

Root prime audits use \(p=5,11,17,23\) on the nonuniform \(B_p\) family:
the images have respectively 25, 121, 289 and 529 elements. The fifth
case has \(p=5,B=\{0,1,5,6,10,11\}\): image 28, nonsingleton mass 14,
and residue pair budget 18. Every nontrivial collision was checked to
have its source indices congruent modulo five.
These are SC-X2 / EXPERIMENTAL, exact exhaustive checks of five finite
instances, not the proof of SC-D1/D2.

Raw outputs are in the ignored directory
local-only/runs/T01/2026-09-21-sublinear-cubic. The principal records are
provenance.json, targeted-verification.json, artifact-verification.json,
prime-audit.json and prime-audit-provenance.json. The prime-audit stdin
source was retained verbatim after execution, without rerunning it.
All arithmetic uses CPython 3.12.7 standard-library exact fractions.
There were no random seeds, network requests, new dependencies, errors
or resource-limit stops.

## Integrity versus mathematical evidence

All 252 raw certificate hashes and the new source, imported graph engine,
and portable-summary hashes matched in the recorded agent byte audit.
This is an integrity check, not a mathematical rerun.

| Artifact | SHA-256 |
|---|---|
| New experiment source | 9960cbb165c2b992160a039618e72e9568b8f3b0687be8918fa9b6e0fcb15447 |
| Reused graph engine | 5f1c98f625ccfb30001a219973ba57b791c0c0c4fefb93a6dc8106df03065f45 |
| Portable new-grid JSON | 426c27401a969e88089022e7f9ac8fc83cc6af776c8c784f74da6d575bfad2ae |
| Prime-audit source | a7c0b80383180590d8ae2808d7e11c48a0cf6e4e49afa482da47822fb2a2bca0 |
| Prime-audit output | 5c986044c03acc7725eb81c39e63c7c24a091110a145b387e29e594a93bf7cbd |
| Canonical prime-audit inputs | e3a82a4a3916e7a67ce2683e5a0da0f44e5a683d78cca41fd88af7e0cc5f72df |

Final repository regression and documentation results are appended below
after execution. They are finite regressions and file checks, not new
mathematical searches.

## Changes and preservation

This cycle adds the seven-note sublinear-cubic report, one exact experiment
module, its five-test module, the portable summary and ignored raw records.
It appends dated T01 scope/status entries to the existing track status,
project map, mechanism library, failure library and open-lemma registry.

All earlier reports, experimental code and stored data remain unchanged.
The pre-existing tracked edits and untracked migration material were
preserved, including concurrent T03 work. This cycle does not claim that
work, alter other tracks, or modify the archived manifest or historical
SPEC. No reset, cleanup, staging, commit, push or remote change was made.
The working tree remains uncommitted.


## Final check results

- `python3 -m unittest discover -s tests -v`: **PASS**, 74 tests, 0.085 seconds reported by the runner.
- `python3 -m experiments verify`: **PASS**, 159 existing finite checks.
- `python3 scripts/check_repository.py`: **PASS**, 39 archive files and local links in 120 Markdown files.
- `python3 scripts/check_codex_setup.py`: **PASS**, 50 local references, 43 T03 manifest members and the configured identity/hash checks; no research executed.
- `git diff --check`: **PASS**.

The complete suite executes the five new-module tests a second time: another
576 polynomial evaluations and 7,364 pair/edge/constructor checks. New-cycle
work including its targeted tests, the root prime audit, and its tests within
the complete suite totals **39,395 polynomial evaluations and 367,560 charged
checks**, well inside the announced ceilings. The one research grid plus
five prime audit cases accounts for **38,243 polynomial evaluations and
350,851 counted checks**. Existing historical finite regressions within the
74-test suite and the 159-check verifier are separately reported checks, not
new searches or reruns of their archived grids.

Full-suite output is retained in full-suite.json and compact final outcomes
in final-checks.json. Tracked diffs and the new code, report, test and data
files were inspected separately. No unrelated edits were attributed to this
cycle. All work remains uncommitted.
