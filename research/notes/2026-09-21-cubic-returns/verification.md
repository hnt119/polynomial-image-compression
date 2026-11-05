# Verification, provenance, and retained limits

2026-09-21 v1. T01 / cubic Cartesian returns. This record separates newly
proved mathematics, finite experimental evidence, repository regressions,
and file-integrity checks.

## Authorization and source selection

The active instruction is the user's “Offline Research Task: Cartesian
Returns and Long Output-Preserving Orbits” attachment at
`[private commissioning attachment; locator withheld]`.
It commissions new proof search for the plus-sign T01 cubic and forbids
internet access. The declared research cap was 200 candidates, at most
256 inputs each, 3,000,000 exact pair checks, and 90 research CPU seconds.
The finite subtask's tighter allocation was 140 candidates, 2,000,000
checks, and 60 seconds. Its explicit 130-candidate grid was inspected and
approved before execution. No new goal, external message, or network
operation was created.

The initial repository status and existing diffs were inspected. Setup,
project map, migration audit, master handoff, T01 current-state export and
checkpoint companions, T01 SPEC/STATUS, migration conflicts, mechanism and
failure libraries, open lemmas, and the construction-ledger template were
consulted. The immediate mathematical sources were:

- [16 September continuation](../2026-09-16-three-branch-continuation/README.md)
  and [rates/fiber maps](../2026-09-16-three-branch-continuation/rates-and-fiber-maps.md).
- [21 September freeze](../2026-09-21-three-branch-freeze/Three_Branch_Continuation_Freeze.md),
  its freeze summary and verification record.

The supplied pair symmetry was rederived in the new proof. The historical
digital/rich-fiber results were not independently recertified. In particular,
the named original bytes of
`Regular_Digital_Carry_Collapse_Universal_NoGo_Checkpoint.md` and
`Cubic_Target_Exact_Elements_and_Candidate_Test.md` remain unavailable locally
under MC-06. A recovery summary is not the missing formal proof. None of the
new return arguments depends on either source.

## Mathematical proof audit

**CR-U1–U5: PROVED in the new source system, independently checked internally.**
The lead read the complete universal proof, recalculated its normalization,
checked primal and dual conic equations and exceptional diagonal cases,
verified the curve graph and crossing argument, and checked the constants
and exponents. A second independent reviewer checked the same steps and
reported no defect. The specific checks include:

- The affine auxiliary target has exactly \(N\) values, and discarding the
  second-coordinate requirement only increases the counted set.
- \(a+b=-2/(3\tau)\ne0\), with no coefficient-dependent intersection
  constant, for every real nonzero \(\tau\).
- Distinct primal hyperbolas meet at most twice; two distinct points belong
  to at most two curves. Dual diagonal lines and mixed cases were checked.
- Consecutive-incidence edges have at most two parallel representatives;
  no edge passes through an unrecorded point. Curve intersections yield at
  most \(q^2\) crossings after local perturbation.
- The simple-graph crossing estimate follows from planar Euler counting
  and random induced subgraphs; adjacent edges can be uncrossed in a
  minimizing drawing. The displayed constant is \(1/72\).
- \(16+2\cdot72^{1/3}<25\), followed by Cauchy–Schwarz, gives the constants
  25 and 5 and the exponents \(8/3\) and \(11/6\).

**CR-P1–P6:** the lead derived the exact fiber, slice, graph and coverage
formulas. Two other reviewers independently checked their identities,
inequality directions, exceptional-pair charges, averages, interleaving,
exact \(2ML\) input count, and growing-step cost. No defect was found.

**CR-B1–B6:** the baseline author supplied exact proofs. The lead checked
the integer and third-integer anchor formulas, fixed-step integrality,
quadratic inverse-interval count, cubic path-span bound, square and modular
examples, and polynomial close-pair estimates with duplicate parameters
charged. The baseline author also independently checked the report's
third-integer formula and summary table. Steps in the AP-union theorem
are explicitly bounded away from zero; polynomial coefficients and the
number of same-degree sequences are fixed before their parameter grows.

These are internal mathematical audits. They are not external review,
formal proof-assistant verification, or a literature/novelty assessment.
Finite tests are not the evidence for the universal asymptotic theorem.

## Exact experiment and accounting

The reviewed implementation is [cubic_returns.py](../../../experiments/cubic_returns.py)
with [targeted tests](../../../tests/test_cubic_returns.py). It uses Python's
standard-library `Fraction`; all input, membership, output, and collision
equalities are exact. Displayed runtimes are measured floating-point seconds,
not mathematical equality evidence. No dependencies were installed.

Command: `python3 -m experiments.cubic_returns`.
Runtime: CPython 3.12.7, macOS Clang 13 build. No random seed: deterministic.

| Candidate group | Exact declared range | Count |
|---|---|---:|
| APs | Steps \(1,1/2,1/3,2/3,2\); sizes \(4,8,16,32,64,128\) | 30 |
| Symmetric integer APs | Sizes \(9,17,33,65\) | 4 |
| Two AP blocks | Steps \(1,1/3\), block sizes \(4,8,16,32\), gaps \(1,n,n^2\) beyond the first block | 24 |
| Polynomial sequences | \(j^2,c(j),j^3,(j^3-j)/2\); parameter lengths \(4,8,16,32,64\) | 20 |
| One planted output | \(z=0\), \(u=j\) or \(j+1/3\), \(-L\le j\le L\), \(L=2,4,8,16,32\) | 10 |
| Equally spaced outputs | \(z=2k\): two outputs at \(L=2,4,8,16\), four at \(L=2,4,8\) | 7 |
| Polynomial output lists | Distinct values of \(k^2\) or \(k^3-k\), \(0\le k<4\), at \(L=8\) | 2 |
| Greedy deletions | All 17 one-point deletions from \(\{-8,\ldots,8\}\), then all 16 deletions from the best remaining set; lexicographic tie-break | 33 |
| **Total** | Whole Cartesian square for each candidate | **130** |

This is exhaustive over each listed finite group and each chosen greedy
stage. It is not exhaustive over all subsets or all real carriers. Some
candidate sets can agree up to translation; the declared models were kept
as separate records. Actual distinct scalar sizes were always used.

The [summary JSON](../../../examples/2026-09-21-cubic-returns.json) contains
every required statistic. Full scalar inputs, output fibers, pair indices,
path decompositions, and difference-slice anchor sets are in
`local-only/runs/T01/2026-09-21-cubic-returns/` (about 56.7 MB of raw records,
ignored by Git). Its `provenance.json` and `verification.json` retain the
original command, runtime, hashes, budget and read-only integrity result.

| Measurement | Observed |
|---|---:|
| Candidates | 130 |
| Maximum actual scalar size | 129 |
| Actual \(P\) evaluations | 274,409 |
| Charged pair checks, three passes per candidate | 823,227 |
| Research-run CPU seconds | 9.047958 |
| Research-run wall seconds | 9.093878 |
| Errors | 0 |

The three passes check direct transformed membership, adjacency in exact
fiber-difference sets, and the independent difference-slice formula. All
three counts agreed for every candidate. Every pair lies in exactly one
recorded path; edges preserve the exact output; the image never exceeds
the component count. Full output support, including all unplanted pairs,
was enumerated.

The original targeted test run passed four tests; it used 52 additional
cubic evaluations, 120 analyzed pair checks, and 27 standalone motion calls.
The complete test-suite run below repeats those small oracles once as
required regression, without rerunning the 130-candidate search. The run
terminated at the prespecified endpoint, with ample budget remaining.

Recorded SHA-256 values:

| Item | Hash |
|---|---|
| Experiment source | `c95649a125794391f24608f07f47af71bd0965bc2d0504866c3b4986daddbecc` |
| Summary JSON | `778a7e0e064cc8a32ff836946995d46443048ca6b298ca1a97f6d10d50e4c76c` |
| Serialized 97 fixed candidate definitions | `3a38cfb3addcc9e1bb545a0f8169b55745bb31cd478213ba297e719fe4d25c93` |
| Targeted test source | `87a22433c37e0a40490dcc6af3d375a33d8e4a588d3d5585c7ebf4ffb7228a0f` |

All 130 raw-record hashes, summary/source hashes, and reconstructed fixed
candidate definitions matched in the recorded read-only integrity check.
That took 0.344699 CPU seconds and zero new polynomial evaluations.

## Repository validation

| Check | Actual result |
|---|---|
| `python3 -m unittest discover -s tests -v` | PASS, 58 tests; 0.131849 child CPU seconds |
| `python3 -m experiments verify` | PASS, 159 existing finite checks; 0.042953 child CPU seconds |
| `python3 scripts/check_repository.py` | PASS: 39 archived source files and links in 97 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local references, 43 T03 manifest members, import/duplicate/C4 checks; no research execution |
| `git diff --check` | PASS |

The two regression logs and measured command records are retained as
`unittest.log`, `experiments-verify.log`, and `regressions.json` in the local
run directory. These existing finite regressions do not establish any
research target. Their tiny historical gadget oracles were not an old
three-branch search rerun: neither the 980-candidate grid nor the adaptive
continuation search was executed.

## Changes and retained gaps

This task adds the six Markdown files in this report directory, one exact
experiment module, one test module, one finite summary JSON, and ignored raw
run/provenance files. Dated addenda are appended to T01 STATUS, the current
project map, open lemmas, failure library, and mechanism library. Historical
sections, SPECs, earlier reports and canonical data remain intact.

The repository already contained tracked edits and untracked migration,
research, PDF, and experiment artifacts. In particular the separate
2026-09-21 dense-Cartesianization T03 work was inherited and was not changed
by this task. No files were staged, committed, reset, cleaned or pushed;
the work remains uncommitted. Tracked diffs and the new untracked report,
experiment, test and summary files were inspected separately; the broad Git
diff includes inherited work, not just this cycle.

Retained mathematical limits: the best return exponent is not determined;
the full cubic image can identify different graph components; no growing-
step witness, full-image power saving, or arithmetic amplification is
provided. The original T01 target remains OPEN. CR-O1 is the sole adopted
next obligation, not a further authorized experiment. Missing historical
proof bytes and absence of a novelty check remain explicit source limits.
