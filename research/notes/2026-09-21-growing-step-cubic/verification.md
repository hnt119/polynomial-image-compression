# Verification and provenance

T01 / growing-step cubic, 2026-09-21 v1. Fixed polynomial
\(P(x,y)=(x-y)^3+x+y\). This record distinguishes new proofs, exact
finite evidence, inherited results, regression tests, and file integrity.

## 1. Active instruction and source boundary

The user commissioned “Offline Research Task: Growing-Step Cartesian
Coverage,” supplied at
`[private commissioning attachment; locator withheld]`.
The request explicitly continues the completed fixed-step cycle and prohibits
internet access. No network call, external message, arithmetic amplification,
or literature search was made.

At task start, repository status, existing diffs and whitespace were inspected.
Setup documentation, current project map, migration audit, master handoff,
T01 state/checkpoint and SPEC/STATUS, migration conflicts, failure/mechanism
libraries, open lemmas and construction template were consulted. The immediate
proof sources are the [preceding report](../2026-09-21-cubic-returns/README.md)
and its [fiber/chain](../2026-09-21-cubic-returns/fibers-and-chains.md),
[baseline](../2026-09-21-cubic-returns/baselines.md), and
[universal-bound](../2026-09-21-cubic-returns/universal-bounds.md) companions.

The conjugacy, uniform single-step theorem CR-U1, and elementary crossing
lemma were accepted as proved dependencies. They were not reproved or
reopened. The new curve family and its hypotheses were checked independently.

Original local bytes of the historical regular-digital and rich-fiber
checkpoints remain unavailable under MC-06. Their recovery summaries are
not substitutes for those proofs; neither result is a dependency here.
No T04 minus-sign or T01 separate quadratic result was substituted.

## 2. New mathematical proof audits

**GS-U1–U3:** the lead and a second reviewer independently checked the
complete new companion. Their audit covered:

- Inverse-step parabola formula, uniqueness of the \((x,\tau)\) curve,
  injectivity from actual returns to incidences, and the discarded scalar
  membership requirement.
- At most two primal intersections, at most two curves through distinct
  points, and the equal-difference-coordinate degeneracy.
- Use of the already-proved crossing lemma with one-component parabolas;
  the constants 9 and 12; powers of \(N\) and \(M\); and the exact
  \(\theta>1/2\) comparison. The coverage threshold is not improved.
- The positive second-coordinate drop, midpoint and separation bounds,
  distinct-difference spacing \(\eta\) versus scalar spacing \(\delta\),
  the full nonsingleton-fiber band, and singleton-output lower counting.
- Common-lattice specialization \(W=D/h^3\), including varying mesh and
  the asymptotic condition \(W=o(N^2)\).

**GS-A1–A4:** the progression author supplied exact analytic proofs; the
lead read and checked the modulo-nine coset condition, lattice preservation,
discrete monotonicity without holes, all-step anchor spans and reflection,
finite-difference component formulas, parity-dependent minimum widths,
uniform edge saturation, nearest-cube gap, and irrational-spacing
injectivity. No unproved asymptotic extrapolation is used.

**GS-P1–P5:** the lead supplied the graph and coordinate-reuse proofs. A
second reviewer checked GS-P1/P2 and the full-support accounting; two
independent reviewers checked GS-P3/P4. The audit covered the interval-union
cardinality, \(4N^{4/3}\) bound, integer projection, distinct degree-three
monomial encoding, coefficient recovery, complete slice classification,
and input/output exponents. Another reviewer checked GS-P5's fixed rational
mesh, exact diameter, \(\Theta(m+1)\) cardinality and all-inventory use of
GS-U3. The two wording corrections made during review were: a fixed-output
restriction can have multiple components; and adjacent singleton scalar
intervals need not overlap when \(L=H=1\). The formulas were unaffected.

No substantive proof gap was found in these scopes. These are independent
internal audits, not external peer review or proof-assistant verification.
No novelty claim is made. The absence of a general growing-step witness
or stronger universal coverage threshold is stated explicitly.

## 3. Experiment, exactness, and finite budget

The overall declared cap was 80 carriers, 240 carrier/inventory cases,
128 distinct inputs each, 3,000,000 exact pair/edge checks and 90 research
CPU seconds. The experiment subtask received 60 carriers, 200 cases,
2,000,000 checks and 60 seconds. The explicit 32-carrier/six-inventory
grid was approved before execution and terminated at that endpoint.

The [experiment source](../../../experiments/growing_step_cubic.py) and
[targeted tests](../../../tests/test_growing_step_cubic.py) were inspected
before execution. The source uses only Python's standard library and exact
`Fraction` arithmetic for mathematical equalities. Command:
`python3 -m experiments.growing_step_cubic`.
Runtime: CPython 3.12.7. No random seed, sampling, added dependencies, or
floating-point collision test was used.

The [experimental summary](experimental-summary.md) gives all grid definitions,
32 compact carrier rows, the inventory-selection rules, and finite limitations.
The [portable JSON](../../../examples/2026-09-21-growing-step-cubic.json)
contains all 192 cases. The ignored directory
`local-only/runs/T01/2026-09-21-growing-step-cubic/` contains 32 full
carrier certificates and 192 full graph certificates, including every
input, output fiber, ordered-pair label, edge, component, and component's
output. All graph and fiber distributions include the entire square.

| Research-run work | Actual count |
|---|---:|
| Carriers / inventory cases | 32 / 192 |
| Maximum distinct input count | 128 |
| Cubic evaluations | 76,303 |
| Within-fiber unordered pairs enumerated | 23,910 |
| Inventory edge-pool checks | 143,460 |
| Component vertex checks | 457,818 |
| Direct-motion oracle checks | 768 |
| Total charged checks | 702,259 |
| CPU / wall seconds | 2.232581 / 2.242286 |
| Errors | 0 |

The graph construction was compared with direct \(T_\tau\) membership
on the declared small cases. Other invariants include full vertex coverage,
one output per component, correct component/image inequality, exact edge
sign accounting, and recovery of full fibers when all useful steps are
included. The last is a diagnostic identity, not a construction proof.

Four initial targeted tests passed; after adding the requested independent
faithful-box oracle, five tests passed. The two small runs used 1,009 checks
and 267 cubic evaluations combined. Their two box cases have
\((N,s,V_{\rm nonisolated},K_{\max})=(9,69,21,3)\) and \((8,56,16,2)\),
with step 1 already giving the full fiber components. The source grid was
not rerun. The later full suite repeats the final tiny oracles once
(745 checks, 206 cubic evaluations). Total work in the new growing-step
module, including these verification repetitions, is therefore 704,013
checks and 76,776 cubic evaluations. Other existing repository regressions
are recorded separately below; they do not expand the research grid.

## 4. Hashes and file integrity

Original run provenance and the two targeted verification records are
preserved in the local run directory. Recorded SHA-256 values:

| Item | Hash |
|---|---|
| Experiment source | `5f1c98f625ccfb30001a219973ba57b791c0c0c4fefb93a6dc8106df03065f45` |
| Portable summary | `a9df07f99c524d464ae80a63645806bc9de143ab4c9419e1a31aed26066c67f0` |
| Serialized carrier definitions | `90fc5d0c190d64ffe8f12fffcc5d1e03d00d7c04975569fc8fff87d5642abb0f` |
| Final targeted test source | `4414bd40deee890425f0808417f019c0799e5e3357ce18953a468feb3017108b` |

All 224 raw certificate hashes, experiment-source hash and portable-summary
hash matched in the recorded read-only integrity audit (0.044483 CPU seconds,
zero new polynomial evaluations). Final report and immediate-source identities
are recorded separately in `report-manifest.json`. File integrity is not
mathematical proof verification.

## 5. Repository validation and work ownership

| Required check | Result |
|---|---|
| `python3 -m unittest discover -s tests -v` | PASS: 69 tests; 0.142022 child CPU seconds |
| `python3 -m experiments verify` | PASS: 159 existing finite checks; 0.042613 child CPU seconds |
| `python3 scripts/check_repository.py` | PASS: 39 archived source files and local links in 113 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local references, 43 T03 manifest members, import/duplicate/C4 identities; no research execution |
| `git diff --check` | PASS |

Regression commands, runtimes and logs are retained in `regressions.json`,
`unittest.log` and `experiments-verify.log`. The existing finite regressions
do not prove a research target. They do not run the old 980-case three-branch
grid, its continuation search, or the preceding 130-case fixed-step grid.

This task adds seven Markdown report/companion files, one experiment module,
one targeted test module, one portable JSON and ignored raw/provenance files.
It appends dated T01-only addenda to STATUS, the current map, open lemmas,
failure library and mechanism library. Earlier reports, SPECs, archives,
and canonical historical JSON remain unchanged.

The workspace already contained migration edits and completed or concurrent
research from other tasks, including separate T03 rectangular/correlated
return work. Those are not this cycle's contributions and were preserved.
Tracked diffs and this task's new untracked files were inspected separately.
No files were staged, committed, reset, cleaned or pushed; changes remain
uncommitted.

## 6. Retained gaps

No positive asymptotic growing-step carrier was obtained. The joint-step
bound does not raise the universal inventory threshold, and every actual-
image obstruction retains its precise carrier hypotheses. Finite graph
connectivity is not identified with generated-subgroup cosets. Large
inventories chosen from already-known fibers remain diagnostic unless their
complexity and a growing coverage theorem are independently supplied.

CR-O1 remains the sole adopted next obligation, with its sublinear-inventory
subcase prioritized and its broader original version still unresolved.
The fixed cubic target stays OPEN. Missing historical proof bytes, absence
of a literature check and absence of external review remain explicit limits.
