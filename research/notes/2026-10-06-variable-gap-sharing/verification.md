# Variable-gap cycle: provenance and verification

T01, 2026-10-06, version 1. Fixed polynomial P(x,y)=(x-y)³+x+y.
This is the user-commissioned constructive shared-edge network round,
coordinated by a lead and three mathematical subagents. All work was offline.

## Source authority and preservation

The controlling sources are the accepted
[elliptic checkpoint](../2026-09-30-elliptic-geometry/README.md) and latest
[sharing-compatibility checkpoint](../2026-10-06-sharing-compatibility/README.md)
with their relevant geometry/construction companions. Their global
elliptic/isogeny exclusions and fixed-gap classification remain imported
accepted results; this task does not claim new audits of all those proofs.
The exact coordinate templates and directed-cycle argument needed for this
round were checked from their equations.

The complete GS-P3 proof in
[structure-and-reuse §3](../2026-09-21-growing-step-cubic/structure-and-reuse.md)
and GS-A4 proof in
[progression-laboratory §4](../2026-09-21-growing-step-cubic/progression-laboratory.md)
were inspected. The former supplies the rate comparison, not an upper bound
for arbitrary correlated windows. The latter applies directly to the derived
spacing-1 carrier; its collision argument and exact outside-band count were
independently checked. These imports are distinguished from the new gluing
and all-cycle proofs.

The setup guide, current map, migration audit, master handoff, T01 state,
checkpoint/companions, SPEC/STATUS, migration conflicts, and relevant
mechanism/failure/open records were consulted. Missing historical originals
listed in MC-06 remain unavailable and are not proof dependencies. No
unavailable argument was reconstructed from a title or summary.

The working tree was dirty before this round, including unrelated T03 work.
Historical archives, migration copies, SPECs, earlier reports, prior scouts
and data were not edited. The five registry changes are dated additions;
their preceding bytes have recorded hashes. No staging, commit, push,
reset, clean or remote change was made.

## Proof audit and claim records

All new claims are T01, over the reals for the displayed fixed polynomial,
dated/versioned 2026-10-06 v1. Exact quantifiers, hypotheses and limits are
in the listed statements. The final local manifest records content hashes.

| ID | Proof/evidence locator | Dependencies; audit and remaining scope |
|---|---|---|
| VG-G1 | compatibility.md §1; every real shared-edge five-label list | Exact substitutions and reconstruction, all endpoint orientations. Author, lead and referee checked both directions. Does not provide dense carriers. |
| VG-G2 | compatibility.md §2; every directed cycle length, real vertices with repetitions allowed | Difference-of-cubes comparison. Author, lead and referee checked the even-cycle degenerate kernel. Uniqueness only, no existence or complex classification. |
| VG-G3 | compatibility.md §3; every integer k≥3 and its displayed windows | Parity, injective endpoint reconstruction, exact four label shifts and boundary equivalence. Independently checked. No ignored out-of-window labels. |
| VG-C1 | construction.md §2; every integer k≥3,L=k³ | VG-G3, interval unions; exact N,Q,Z and distinctness. Author, lead and referee checked counts and endpoint support. |
| VG-C2 | construction.md §3; every edge in E_k | Shared-edge shifts and a valid k+1-point block. Every edge has at least k−1 partners and local cross-partner closure. Motif multiplicity is never counted as new pairs. |
| VG-C3 | construction.md §4; this one window family and its integer carrier | Exact complement, ratios, safe support certificate; imported GS-A4 specializes to actual N²−O(N^(3/2)) image. GS-P3 comparison prevents claiming a new N^(4/3) rate. |
| VG-X1 | exact-audit.md; scout, portable and raw data | EXPERIMENTAL, three exhaustive complete squares with exact integer equality. No inference beyond the declared finite range. |
| VG-O1 | README.md final obligation | OPEN, one finite ordered-real deformation of the same 27-vertex incidence pattern. Not solved or searched; no scaling or compression conclusion claimed. |

The construction agent separately scope-checked VG-O1 against the accepted
results. Only translation is normalized, since scaling does not preserve
the fixed polynomial. The output variables move jointly, so fixed-label
cycle uniqueness does not settle it. This scope check is not a proof of
existence or a claim that an elementary rigidity argument cannot exist.

## Execution and finite budget

Before any enumeration the lead declared ceilings of 12 finite instances,
50,000 exact P evaluations and 10,000 compatibility/accounting checks.
The shared-edge equations, window identities and count proofs were saved;
the lead and referee read both proof companions. The lead inspected the
new evaluator and tests, aligned the canonical block with the proof and
released a single run. Proof-at-release hashes are retained in provenance.

Command:

```
python3 -m experiments.variable_gap_sharing --proofs research/notes/2026-10-06-variable-gap-sharing/compatibility.md research/notes/2026-10-06-variable-gap-sharing/construction.md
```

The exact/referee agent ran only k=3,4,5, L=k³. Python 3.12.7 standard
library, exact integers and rational reporting, no randomness, external
packages, numerical roots or floating-point equality. Runtime and code,
test, input, proof and output hashes are in
local-only/runs/T01/2026-10-06-variable-gap-sharing/experiment-provenance.json.
The writer refuses existing result files.

The one scout used 3 instances, 20,450 P evaluations and 9,349 charged
checks. The unit source adds one worked-motif visit, 5 P evaluations and
25 assertion contexts, including fixed boundary/scope oracles. When run
once, the combined current-family cost is therefore 20,455 evaluations
and 9,374 checks, below the original ceilings. No square was enumerated
again by the lead. Existing repository regression checks are separate
fixed validations, not expanded or rerun research searches.

## Validation record

The lead's final repository/documentation, local-source integrity, unit,
fixed regression, whitespace and artifact-hash outcomes are recorded below
and in the local validation log. They verify software/document consistency;
they do not establish the T01 target. The mathematical conclusions rest on
the displayed proofs with the exact scopes above.

Deliverables are the concise report, four proof/audit/verification companions,
one reviewed scout, three focused unit tests, portable exact data and five
dated registry addenda. The full raw fibers and local integrity manifest
remain under local-only/runs/T01/2026-10-06-variable-gap-sharing.

The lead ran each required validation once after report assembly:

| Command | Actual result |
|---|---|
| python3 -m unittest discover -s tests -v | 97 tests passed, including the three new focused tests |
| python3 -m experiments verify | All 159 existing finite benchmark checks passed |
| python3 scripts/check_repository.py | 39 archived sources and links in 175 Markdown files verified |
| python3 scripts/check_codex_setup.py | 50 local references, 43 T03 manifest members and recorded import identities verified |
| git diff --check | Passed |

Thus the actual combined current-family computation cost, including the
single unit-suite visit, is 20,455 P evaluations and 9,374 checks. There
was no need to enlarge the declared budget or repeat the scout. A final
geometry-agent reading of the concise report found no algebra or scope
errors and did not attempt VG-O1. All edits remain uncommitted.
