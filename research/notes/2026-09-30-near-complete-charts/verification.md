# Verification, proof audit and source boundary

T01 / near-complete nonlinear charts, 2026-09-30 v1.
Fixed \(P(x,y)=(x-y)^3+x+y\).

## Authorization and initial state

The active attachment is “T01 Offline Research Task — Near-Complete
Nonlinear Charts”. It commissions new coverage-first research and explicitly
requests a parallel obstruction task. That task was assigned to the
existing proof agent. No separate task was created, and no further
research was launched after the bounded cycle.

Before proof search the lead announced T01 near-complete charts, the exact
full-square obligation, offline policy, and a cap of 24 new carriers,
200,000 exact cubic evaluations and two million additional exact checks.
The numerical scope was reduced to six predetermined first completions,
with a scalar cap of 128, and stopped after all six were sparse.
No old low-degree/fixed-output classification or old carrier grid was rerun.

Initial Git status and tracked differences were inspected; inherited changes
were retained. The setup guide, current project map, migration audit, master
handoff, T01 current state, separate norm–trace checkpoint, T01 SPEC/STATUS,
conflict registry and relevant mechanism/failure/open entries were consulted.
The controlling mathematical source is the 21 September
[nonlinear-reuse report](../2026-09-21-nonlinear-reuse/README.md) and its
proof companions. Their claims are preserved with their original scopes.

Historical digital/rich-fiber originals reported in recovery manifests
remain unavailable locally. They were not reconstructed, re-certified or
used as dependencies. Historical fixed-prime/tower results were not research
assignments. No network, literature search, arithmetic amplification,
dependency installation or novelty assessment occurred.

## Complete internal proof audits

| Claims | Author / independent reviewer | What was checked |
|---|---|---|
| NC-A1/A2 | Parallel obstruction agent / lead | Polynomial inverse degree in u; constant polynomial units; every occupied finite fiber; order reversal; arbitrary growing libraries; certificate versus actual support |
| NC-A3 | Parallel obstruction agent / lead | Strict monotonicity; cubic root count; combining all row/column rules; rational simple-zero obstruction |
| NC-A4 | Parallel obstruction agent / lead | All m>=3; Möbius cycle and tangent pole exclusions; distinct differences; injective second coordinate; m<=N<=2m and complement |
| NC-A5 | Parallel obstruction agent / lead | Jacobian units; forced affine output map; finite output and rank permutations; at most four orbit points; per-orbit output cost |
| NC-C1/C2 | Lead / parallel obstruction agent | Optimal fiber saturation, k=0 and singleton ties; every tail inequality; both exponent directions and constant absorption |
| NC-H1/H2 | Lead / parallel obstruction agent | Disjoint assignment and all stage costs; fiber capacities; energy upper bound used only for support lower bound; rational degree 6d; overlap scope |
| NC-R1 | Lead / parallel obstruction agent | Actual pair/scalar counts; identity and output preservation; growing-K dependence and all new cross-pairs |

One quantitative correction was made during audit: near-full completion
requires N<=(1+o(1))sqrt(K)n for growing K, rather than an additive o(1)
error outside sqrt(K). The exact beta formula is included. Hierarchy
constants are explicitly fixed across the growing family, and the
nonzero-denominator case in H2 is stated. These correct new drafts,
not historical proofs.

All listed proofs were independently checked internally after corrections.
The second agent also checked the main report, construction ledger and
experimental companion against proofs and retained data, including map
degrees, tangent radius, numerical tables and the single next obligation.
Internal audit is not external peer review. The rational m-cycle is a scope
boundary with a proved sparse count, not a candidate search.
No symbolic-search program was run.

## Exact experiment and independent tiny tests

The lead read the complete new source and tests before execution.
The parallel agent independently inspected the experiment source without
executing it and found no exactness or all-square counting defect.
It clarified that the Möbius restriction is the full-cycle domain, not
merely each branch's own pole set; the reports state this explicitly.

Command: python3 -m experiments.near_complete_charts.
Runtime: CPython 3.12.7. Two exact seed sets and three formulas are fixed
in source; there is no random seed because the run is deterministic.
All six new squares are exhaustively enumerated with Fraction arithmetic.
The full ranked fibers and cumulative coverage at every k are retained.
No equality decision uses floating point.

The one run used 5,338 polynomial evaluations (54 seed plus 5,284 new-square),
11,072 additional charged checks, and 0.124286 CPU seconds.
The categories are recorded in the experimental companion and provenance;
they do not claim to count every machine instruction or sorting comparison.
Maximum N was 35. All six completed without errors or resource-limit stops;
the sparse-family stopping rule prevented second-level expansion.

Four new tests check hard-coded full fibers for A={0,1}, exhaustive tiny
subset optimality, an independent rational three-cycle identity and
exclusions, adaptive output preservation/differences, and budget rejection
before square evaluation. The targeted four-test run passed.
Each execution uses 45 cubic evaluations, including direct independent
oracles outside the module counter. Targeted and full-suite executions
therefore add 90 to the research total:
**5,428 new-cycle cubic evaluations**. Existing historical regressions
are separately recorded and do not expand the carrier search.

New code SHA-256:
de1beaca50f0019d77e57945ed21e148c86b5d03be56f9ef2bbaca8c4e939779.

Portable results SHA-256:
eccae07a38a5de796b9fd50596aba55d06a265202ed98368eb7087e757bde08f.

The six raw certificates, their hashes, experiment provenance and targeted
test output are retained under
local-only/runs/T01/2026-09-30-near-complete-charts/.
The writer rejects pre-existing outputs; no research rerun was used for
final verification.

## Final checks

| Check | Result |
|---|---|
| python3 -m unittest discover -s tests -v | PASS: 88 tests, reported suite time 0.099 seconds |
| python3 -m experiments verify | PASS: 159 existing finite benchmark checks |
| python3 scripts/check_repository.py | PASS: 39 archived files and links in 143 Markdown files |
| python3 scripts/check_codex_setup.py | PASS: 50 local references, original import identities, 43 T03 manifest members, duplicate states and C4 hashes; no research code executed |
| git diff --check | PASS |
| Independent raw byte/count audit | PASS: six raw hashes, 5,284 stored pair records, cumulative curves and selected/formal counts; no P reevaluation |
| Research source and portable hashes | Both match the recorded run |
| Prior nonlinear-reuse artifacts | All ten prior notes/code/test/data hashes unchanged |
| Registry prefix audit | All five inherited file prefixes retained exactly |
| New-note source check | Six notes: balanced math delimiters, no unexpected control characters |

Complete captured outputs and wall times are in the run directory's
unit-tests-final.json, finite-regressions-final.json, repository-final.json,
codex-setup-final.json and whitespace-final.json. The byte/count audit is
lead-artifact-verification.json. All research data were read for integrity
and stored-count consistency; their cubic evaluations were not rerun.

The totals reflect the current shared workspace, including concurrent
other-track work. Only four tests and six notes were added by this cycle.
The tracked T01 difference and the new source/artifact files were inspected
separately. Final-deliverable hashes are recorded in
final-deliverable-manifest.json; they identify the completion snapshot,
not a mathematical proof. All changes remain uncommitted.

## Changes and retained gaps

This cycle adds six report/companion notes, one experiment module, one
four-test module, and one portable exact result. It appends dated records
to T01 STATUS and the project/mechanism/failure/open registries.
Prefix hashes distinguish these additions from all inherited content.
Old archives, migration references, SPECs, prior reports and prior
experimental data remain unchanged by this cycle.

All work remains uncommitted. Nothing was staged, committed, pushed,
reset or cleaned. Other tracks and inherited files were not edited by this
cycle. Tests and byte hashes do not prove the cubic target.

T01 and the near-complete witness remain OPEN. The invariant-orbit result
does not lower-bound actual images; the growing-library support obstruction
needs its explicit output-overlap hypotheses. The single next obligation,
NC-O1, is the actual small-fiber pair-mass tail, equivalent to NR-O1.
