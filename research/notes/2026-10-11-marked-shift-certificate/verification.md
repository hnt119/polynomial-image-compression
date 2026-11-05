# Marked shift certificate provenance and verification

T01, 11 October 2026, version 1. The fixed ambient target remains
P(x,y)=(x-y)^3+x+y. This authorized cleanup resolves only the torsion
status of TC-G5's exact marked difference T=R2−R1. No geometric
classification, global factorization, arithmetic tower or rank/CM search
is commissioned or performed.

## Sources and proof status

The controlling source is
[the torsion-compatible checkpoint](../2026-10-11-torsion-compatible-sharing/README.md),
with geometry.md, exact-audit.md and exact-results.json. Its actual
constants, marked points and sign choices are used unchanged. The exact
coordinate vectors are read, not recomputed by rerunning its program.
Its two-width and genus-four theorems remain accepted and closed; this
cleanup neither changes their statements nor repeats their proof searches.

The local criterion is the complete formal-logarithm lemma under EG-C2 in
[complex-extensions.md](../2026-09-30-elliptic-geometry/complex-extensions.md).
That source treats a good integral short Weierstrass model over Q_p,
p≥5, and a nonidentity point of negative X-valuation. The present proof
verifies those exact hypotheses at p=23 over Q_23, without applying its
unramified statement to a ramified extension. Its power-series proof is
inspected by lead and referee and supplied in the arithmetic appendix.
No numerical height estimate, torsion table or unlocated source is used.

The lead inspected the dirty Git state and existing diffs, setup and
migration guides, current map, master handoff, T01 state and separate
quadratic checkpoint, SPEC/STATUS, MC-06 and relevant mechanism/failure/
open records. Historical missing originals are not proof dependencies.
The separate quadratic branch and other tracks are unchanged.

## New claim record

| Field | Record |
|---|---|
| ID and status | MS-C1 / PROVED; resolves TC-O1 |
| Track and polynomial | T01; ambient polynomial (x-y)^3+x+y |
| Quantifier and object | The one specified real algebraic point T=R2−R1 has infinite order; every positive integer m satisfies [m]T≠O |
| Exact hypotheses | Positive real a=√2, H²=(3+a)/14, W²=4a−3; marked positive-Y points and E_c as in README.md and TC-G5 |
| Proof locator | arithmetic.md; summary in README.md |
| Version and date | 1 / 2026-10-11; source and final artifact hashes in the local manifest |
| Dependencies | TC-G5 exact constants; elliptic chord law; explicitly proved square-class and embedding facts; inspected EG-C2 formal-log proof |
| Evidence type | Complete symbolic all-orders proof at one good prime, followed by Galois conjugation; no finite order search |
| Internal audit | Arithmetic specialist derived the certificate; lead and independent referee separately checked field degree, exact points, Hensel roots, good reduction, valuations, formal logarithm and conjugation |
| Scope boundary | No rank or torsion-group classification; no unbounded frame family or asymptotic image saving |
| Remaining point obligation | None: TC-O1 is resolved; no successor research obligation is adopted |

## Execution and preservation

The initial ceiling was three preselected small primes and 10,000 exact
field/group checks if a certificate needed finite computation. The prime
23 was selected from the exact denominator and norm identities before any
search. The successful certificate was then proved entirely by hand:
one prime, zero executable mathematical runs, zero target P evaluations,
and no division-order enumeration. Shell/Python file reads, hashing and
repository validation are administrative checks, not mathematical scouts.

A possible ramified route through 2R1 was noticed symbolically but not
executed or needed. The final proof uses 4R2 over Q_23 and the existing
criterion's original hypotheses. It is the only completed certificate;
no extra prime or alternate point is pursued after resolution.

Before edits, hashes of 358 pre-existing files were saved to
local-only/runs/T01/2026-10-11-marked-shift-certificate/baseline.json.
This cycle adds the four files in this dated note directory and dated
append-only registry updates. Original checkpoints, companions, code,
raw data, migration references, archive files and SPECs are preserved.
No staging, commit, push, reset, clean or remote change is performed.
Final documentation, reference, whitespace and preservation results are
recorded after the completed report is inspected. These checks are not
substitutes for the arithmetic proof.

## Final documentation checks

Using Python 3.12.7, `python3 scripts/check_repository.py` passed:
39 archived sources and links in 206 Markdown files were verified.
`python3 scripts/check_codex_setup.py` passed: 50 local references,
original import identities, 43 T03 manifest members, duplicate states
and C4 hashes were verified without executing research code.
`git diff --check` passed, as did separate whitespace checks for all
four new report files. These are documentation and integrity results;
the proof review is recorded separately in referee-audit.md.

Against the pre-edit 358-file baseline, 353 files are byte-for-byte
unchanged. The five updated registries retain their complete original
contents as byte-identical prefixes, followed only by the dated MS-C1
resolution. No baseline file is missing and no unrelated change occurred
during this cleanup. All six files of the preceding torsion-compatible
checkpoint are unchanged. The report adds no executable code, so the
existing mathematical regression suite was not rerun.

The ignored local run directory contains baseline.json,
registry-prefixes.json, integrity-check.json, validation.json and
artifact-manifest.json. The final manifest identifies the retained source
versions and new report versions. Work remains uncommitted, including
the inherited dirty state; no original artifact was overwritten.
