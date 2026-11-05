# DC-O1 — proof audit and execution record

21 September 2026; T03; fixed $Q(x,y)=x^2+xy+y^2$.
Strictly offline. No external theorem import, literature search or novelty
claim. Mathematical proofs, finite research and repository checks are
recorded separately.

## 1. Authorization and source boundary

The active assignment is the DC-O1 attachment with identifier
`[private attachment identifier withheld]`, read before the cycle began.
The inherited dense-Cartesianization report, DC-R1 and HR-1 supply the
current witness obligation and its support implication. Master/current
state, setup/map/audit, track SPEC/STATUS, conflicts and relevant libraries
were consulted for provenance and fixed-target scope. Historical prompts
were not treated as fresh authorization.

New proof claims: **CF-1–CF-4**, **DC-T1–DC-T3**, **DC-TB1–DC-TB4**,
and **MP-1**. Each companion supplies exact hypotheses, quantifiers,
proof and construction ledger, dated to this cycle. There is no missing
external input for these elementary arguments. The existing missing
F25/arithmetic originals are not used or claimed recovered.

## 2. Independent internal mathematical reviews

| Assigned reviewer | Independent work checked | Result |
|---|---|---|
| `eisenstein_sources` | MP-1 moving-pole theorem; DC-T1–DC-T3 tensor compatibility, zero and reflection exceptions | PASS |
| `norm_trace` | CF-1–CF-4 core/fringe bounds and image transfer; DC-TB1–DC-TB4 type balancing and gadget | PASS |
| `audit_sign_cube` | Exact six-case scout and three tests before execution; later finite table/data review | Pre-execution PASS; final record below |
| Lead | All four complete proof companions, scalar action, source/target conventions, rates and exception accounting | PASS |

Reviewers did not execute programs. The reviews are internal, not
external peer review. Their agreement does not replace the complete
written arguments. The CF-3 strict fringe-capacity conclusion was
explicitly qualified by $b>0$ before finalization. The rectangular
image numerator $|X||Y|$ is retained only when returns land in
$X\times Y$; the actual scout uses exactly that convention.

The tensor proof explicitly distinguishes linear from difference spans
when zero is absent. Its rank-one reflection examples are scope tests,
not growing witnesses. The type proof counts distinct scalar pairs,
not duplicate mask incidences. The moving-pole proof covers a finite
width-one action window, not every integer generator power.

## 3. Frozen exact scout

Inspected program: `experiments/rectangular_returns.py`.
Inspected unchanged dependency: `experiments/unit_exponent.py`.
The prior scout entry point in that dependency is not run on import.

```text
python3 -m experiments.rectangular_returns \
  --output examples/2026-09-21-dc-o1.json \
  --pairs-output local-only/runs/T03/2026-09-21-dc-o1/pairs.json
```

Exactly one run, with six cases fixed before execution:

1. Signed local rectangle $\{\pm1\}\times\{\pm3\}$.
2. Its balanced-state scalar construction at depths 2 and 4.
3. Correlated zero-sum ternary polynomial words with moving poles at
   depths 3, 4 and 5.

The fixed threshold is $n^{1/4}$, implemented by an integer fourth-root
ceiling. Every rectangular pair/action is evaluated in two independent
coordinate formulas. Every union-square $Q$ value is evaluated directly
and as $((2x+y)^2+3y^2)/4$. All equality and membership checks use
`Fraction`; only displayed geometric means use floating point.

The program stores every selected multiplier, scalar input, output,
rectangular source, legal action and distinct returned target. The raw
file is local-only and must accompany a raw-data handoff separately.
The frozen summary records complete histograms and individual action
domain sizes. Files are exclusive-created and identical output paths
are rejected. No random seed, factorization, network or sampling.

| Query category | Charges |
|---|---:|
| Constructed action norm checks | 381 |
| Full union-square $Q$ queries | 12,307 |
| Independent full union-square $Q$ queries | 12,307 |
| Rectangular action queries | 755,447 |
| Independent rectangular action queries | 755,447 |
| **Scout total** | **1,535,889** |

Python **3.12.7**. Measured research CPU through completed cases:
**59.575291 seconds**; wall **59.705767 seconds**. Metadata is captured
before final JSON serialization, which is not included in this CPU
figure. The measurement includes every mathematical query and oracle.
The symbolic proofs do not depend on the observed small-depth counts.

## 4. Required regressions and shared budget

The announced shared cap was **2,000,000 charged evaluations and 600
research/validation CPU seconds**. The inspected local-only regression
wrapper charges every call in `experiments/` and `tests/`, including
helpers and generator resumptions. This deliberately overcounts their
semantic mathematical queries and includes existing regression cases.
It invokes the required commands via `runpy`, without running the new
scout entry point. The CPU guard is checked periodically, not presented
as an operating-system hard deadline.

| Required command | Result | Conservative call charges | CPU seconds |
|---|---|---:|---:|
| `python3 -m unittest discover -s tests -v` | **61 tests PASS** | 67,053 | 2.321487 |
| `python3 -m experiments verify` | **159 checks PASS** | 25,386 | 0.798039 |
| **Total including scout** | **Within cap** | **1,628,328** | **62.694817** |

Three new tests check oriented-rectangle membership, zero label/target
separation and exact threshold rounding. They do not rerun the six
carriers. Regression logs and category breakdowns are retained in the
local run directory. No expanded search followed the fixed scout.

## 5. Repository provenance

Startup on `main` found nine modified tracked files and inherited
untracked work. Local `baseline.json` hashes **188 pre-existing files**;
`inherited.patch` and `inherited-status.txt` preserve the initial view.
This task does not reset, stage, commit, push or alter remotes.

New outputs are confined to this cycle's note directory, exact program,
tests, frozen example and local run directory. Existing state/library
files receive only dated addenda, with original prefixes hashed before
append. The four earlier targets, old SPECs, historical proofs,
checkpoints and canonical source manifests are not rewritten.

## 6. Final report, repository and source checks

The independent finite-data reviewer checked every main-table size,
threshold, median, empty good set, return histogram, fraction, geometric
mean and full-image count against the frozen JSON: **PASS**. The same
review kept the experimentally observed maximum of two separate from
the uniform proved MP-1 bound of 27. Both execution source hashes were
independently checked and matched. The mathematical report reviewer
checked the new theorems and scope against all companions: **PASS**.

| Check performed | Actual result |
|---|---|
| `python3 scripts/check_repository.py` | PASS: 39 archived files and local links in 101 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local references, original import identities, 43 T03 manifest members, duplicate states and C4 hashes |
| `git diff --check` | PASS |
| New note/code/test/data whitespace and completion-marker check | PASS |
| Exact program/dependency hashes against scout metadata | PASS; no post-execution source edits |
| Baseline and append-prefix inspection | 181 of 188 baseline files unchanged; five task addenda preserve their entire immediate pre-append prefixes; no baseline file missing |

Concurrent work changed two additional pre-existing T01 files:
`research/notes/2026-09-21-cubic-returns/construction-ledgers.md` and
`research/tracks/01-cubic-digital/STATUS.md`. This task did not edit them.
The four shared map/library files had also changed before this task
appended its entries. Their pre-append prefixes were preserved exactly;
they are not reported as matching startup. T03 STATUS's preserved prefix
does match startup. These differences are recorded separately in local
`integrity.json` and `addenda-prefixes.json`, not attributed wholesale
to this cycle. All earlier T03 proof/checkpoint/data files in the baseline
are unchanged.

The task's changes are the new report and four proof companions,
verification/manifest, one exact program, three small tests, six-case
summary and local raw records, plus five dated status/library addenda.
The inherited working tree remains uncommitted. No Git history or
canonical archive manifest was changed. These checks concern file and
repository integrity; they do not rerun the mathematical proofs.

## 7. Reproducible content identities

The accompanying `manifest.json` records SHA-256 and byte sizes of
the completed report, proof companions, this verification record, scout,
tests, frozen summary, local raw pairs and regression wrapper. It omits
itself to avoid a circular hash. The summary independently records the
exact scout/dependency hashes from execution. Local-only raw files and
private references must be supplied separately for a complete local
handoff; a Git copy alone does not include them.
