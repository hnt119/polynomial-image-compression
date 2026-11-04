# Verification, provenance and limits

T01 / nonlinear coordinate reuse, 2026-09-21 v1.
Fixed polynomial \(P(x,y)=(x-y)^3+x+y\).

## Authorization and source boundary

The current attachment, “T01 Offline Research Task — Nonlinear Coordinate
Reuse”, commissions this cycle. The announced scope was direct nonlinear
scalar reuse and full-image support: bounded-degree output factorization,
polynomial/rational coordinate sharing, and new exact chart diagnostics.
The global computation ceiling was 48 candidate charts, 20,000 coefficient
checks, 500,000 full-square polynomial evaluations and four million
additional checks. No internet, external literature search, arithmetic
amplification, old family search or old grid rerun was authorized or used.

Orientation inspected the working-tree status and existing differences,
`docs/CODEX_SETUP.md`, `research/CURRENT_PROJECT_MAP.md`,
`research/CODEX_MIGRATION_AUDIT.md`, the local master handoff and T01
current-state export, the separate quadratic checkpoint, T01 SPEC/STATUS,
the conflict and mechanism/failure/open registries, and the construction
ledger template. The preceding
[sublinear-symmetry report](../2026-09-21-sublinear-cubic/README.md)
and its proof companions supply the controlling prior cubic state.
Earlier attachments are historical instructions, not additional searches.

The original historical digital/rich-fiber proof bytes remain unavailable.
They were not reconstructed or used as dependencies. The separate quadratic
branch and other tracks were not substituted for T01. Source orientation
and byte integrity are distinct from mathematical proof verification.

## New proof audits

All audits below are internal. “Independently audited” means a second
agent inspected the complete argument, not external review or a claim
of novelty.

| Claims | Author and independent audit | Concrete audit scope |
|---|---|---|
| NR-C1–C4 | Rational-curves agent; lead independently audited | Total-degree comparison; complete complex singularity list; nonzero differential; every finite and infinite parameter pole; real exceptional charts including isolated node and vertical-limit point; several-parameter specialization |
| NR-L1–L4 | Classification agent; lead and rational-curves agent independently audited | Degree separation; linear-U coefficient exception; five exhaustive real affine normal forms; all six-coefficient kernels; specified-statistic composition; constants and degenerate cases; distinct-pair root count |
| NR-A1/A2, NR-P1 | Lead; rational-curves agent independently audited | Formal/distinct label separation; full complement; rational root count; nodal factorization; both monotonicity derivatives; distinct outputs; lower/upper scalar counts |
| NR-G1/G2 | Lead; rational-curves agent independently audited | Generic specializations and nonconstant differences; exceptional output separations; nonzero cleared equation; total degree 7d; grid root bound; one orientation at a time |

The classification agent also independently checked the main report and
construction ledger against the proofs, including all nodal denominator
and rate claims. Its wording correction distinguishes easy full-square
coverage from the unresolved simultaneous coverage and output saving.

The G2 wording was clarified during audit: its bound applies to each
orientation separately; the union of both orientations has the safe
14d bound. The nodal family explicitly uses integers \(m\ge1\).
The inherited GS-P3 theorem is cited only to identify a previously closed
consecutive-grid specialization. It was not re-proved or re-searched here.

The lead inspected the complete new experiment and test sources. The
experiment agent inspected the source before execution. The classification
agent inspected its new symbolic checker before execution; the lead then
read that checker and its exact results. The proofs are analytic and do
not depend on a finite coefficient sample being exhaustive.

## Exact symbolic calculation

Command: `python3 local-only/runs/T01/2026-09-21-low-degree-symbolic/verify.py`.
The new standard-library program checks the five normal-form Jacobian
kernels and the exceptional linear-U identity by exact rational polynomial
arithmetic. Its analytical normal-form reduction, not coefficient sampling,
supplies exhaustiveness over all real coefficients.

- Runtime: CPython 3.12.7; measured CPU 0.001122 seconds.
- Work: 517 charged coefficient operations/checks; no scalar carrier or
  full-square evaluations; no randomness or floating-point equality.
- Allocated ceiling: 5,000 coefficient checks within the global 20,000.
- Source SHA-256: `29f7138f1c5267c1cda2ad3fee5e2144abf6375cbd51ae982adaa4dd415fc3cc`.
- Result SHA-256: `801feaa65517a02f5787c3c6bdeac8ce18da48dec03a7e55a6e2bbf2581a27d1`.

The source and full coefficient matrices/results are retained together
under the local run directory. They were not rerun to overwrite the record.

## Exact finite chart calculation

Command: `python3 -m experiments.nonlinear_reuse`.
The [experimental companion](experimental-summary.md) specifies every
parameter range, normalization, model and stop condition. The portable
[JSON record](../../../examples/2026-09-21-nonlinear-reuse.json)
contains exact summary counts. The local run directory
`local-only/runs/T01/2026-09-21-nonlinear-reuse/` contains 12 complete
carrier certificates, 16 chart certificates, and provenance.

Input-only preflight preceded enumeration. The one research grid used
16 charts on 12 carriers, maximum N=18, 924 cached full-square polynomial
evaluations, and 6,298 charged checks. CPU time was 0.036732 seconds,
wall time 0.037140 seconds, on CPython 3.12.7. Every equality used exact
`Fraction` arithmetic, including the fixed quadratic scaling. There was
no seed because there was no randomness. Errors and resource stops: none.
Sparse-family stops are explicit and prevented any larger search.

The initial preflight used 980 constructor checks and no polynomial
evaluations. Four targeted independent-oracle tests used eight further
polynomial evaluations and 1,013 checks. Thus that agent's complete
cycle used 932 polynomial evaluations and 8,291 charged checks. The
research count includes its 924 polynomial evaluations; these accounting
categories are not all disjoint and are not added twice.

Source SHA-256:
`4bc2201e00eafdb6eba4ac31705de512b1751b317d52e71f12cb08c2c87f282b`.
Portable JSON SHA-256:
`a87f5e7ca346b2865c018cee2d00a89d4dc7d8abca276552376f940d11719c62`.
All 28 raw artifact hashes matched in the experiment agent's byte audit.
This byte check did not rerun the mathematics.

## Final repository validation

| Command or inspection | Result |
|---|---|
| `python3 -m unittest discover -s tests -v` | PASS: 81 tests, including this cycle's four new tests; reported suite time 0.121 seconds |
| `python3 -m experiments verify` | PASS: 159 existing finite benchmark checks |
| `python3 scripts/check_repository.py` | PASS: 39 archived source files and local links in 133 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local references, original import identities, 43 T03 manifest members, duplicate states and C4 hashes; no research code executed |
| `git diff --check` | PASS |
| Lead independent byte audit | PASS: 28 raw certificates and four source/summary hashes |
| Append-only registry audit | PASS: all five inherited file prefixes have exactly their pre-addendum hashes |
| New-note source inspection | PASS: seven notes, balanced math delimiters and no unexpected control characters |

Full captured outputs and wall times are retained in the local run folder's
`unit-tests-final.json`, `finite-regressions-final.json`,
`repository-final.json`, `codex-setup-final.json`, and
`whitespace-final.json`. The suite counts reflect the shared workspace,
including inherited and other-track tests; only four tests were added
by this cycle. The lead inspected the tracked T01 difference separately
from the new notes, experiment, test and data files.

The full-suite run repeats the four new tests once, adding eight polynomial
evaluations and 1,013 charged checks. Thus the **new-cycle total**, including
preflight and both new-test executions, is **940 polynomial evaluations
and 9,304 charged checks**, plus the separately counted **517 symbolic
coefficient operations**. The one research grid itself still uses only
924 full-square evaluations. All totals are within the announced ceilings.
Byte checks and the existing finite regressions are separately recorded;
the latter do not constitute a larger carrier search.

`lead-artifact-verification.json` records the independent hash/prefix/source
audit. `final-deliverable-manifest.json` identifies the final 15 report,
code, data and registry files by SHA-256. These integrity checks do not
replace the proof audits above. Neither tests nor archive hashes prove T01.

## Change boundary and retained gaps

This cycle adds seven report/companion notes, one experiment module,
four tests in one test module, one portable finite output, and dated
addenda to T01 STATUS and the project/mechanism/failure/open registries.
Original archives, migration references, SPECs and older report sections
remain unchanged by this cycle. Inherited migration, prior T01 and
other-track work remains present and uncommitted. Nothing was staged,
committed, pushed, reset or cleaned.

No full or near-complete compressed scalar square was constructed.
The nodal family's actual full-image asymptotic remains unresolved;
its sparse prescribed-pair count only disproves that coverage certificate.
Arbitrary finite correspondences, higher-degree two-dimensional charts
and nonrational branches are outside the classifications. T01 is OPEN.
NR-O1 in the main report is the sole adopted next obligation; recording
it does not initiate a further research cycle.
