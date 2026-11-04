# Correlated DC-O1 — proof review, execution and provenance

21 September 2026 · T03 · fixed $Q=x^2+xy+y^2$.
Strictly offline, no new outside result or novelty claim. This record
separates mathematical proof review, exact finite scouting and repository
integrity checks.

## 1. Authorization and fixed scope

Controlling assignment: the user attachment
`704dd481-a765-4807-a314-bd219fd6e17e/已粘贴的文本.txt`, titled
“Correlated DC-O1 Return-Domain Witness.” Its instruction commissions a
new constructive cycle, superseding older freeze prompts as active work
while preserving their mathematical conclusions.

The announced scope was exactly three correlated mechanisms: whole-factor
conjugation, pair-indexed linear-level reflections, and arithmetic partial
divisibility domains. The announced total cap was **2,000,000 charged
evaluations / 600 research and validation CPU seconds**. The parent owned
all program execution; symbolic agents ran no mathematical programs.

Orientation included setup/map/migration audit, master handoff,
T03 current state, track SPEC/STATUS, conflicts, the latest DC-O1 report
and relevant proof companions, DC-R1 and the construction-ledger template.
The previous tensor, balanced-state and moving-pole results were accepted
as frozen context, not reproved. HR-4A/B's already established integer
norm-fiber and divisor bounds were located; the contemplated ordinary
integer-height scout was rejected before execution because it would
repeat a completed bound. It did not become a fourth research mechanism.
The third mechanism instead uses high-height CRT cube-root inputs and
new simultaneous residue constraints. No missing historical source was
reconstructed or needed for its elementary proofs.

## 2. New claim provenance and independent internal audits

| IDs | Complete mathematical source | Exact evidence and review |
|---|---|---|
| FS-1–FS-3 | factor-switching.md, §§1–5 | New symbolic proof by `norm_trace`; independent full audit by `eisenstein_sources`; lead inspection: PASS |
| CR-L1–CR-L4 | level-reflections.md, §§1–4 | New symbolic proof by `eisenstein_sources`; independent full audit by `norm_trace`; lead inspection: PASS |
| CD-1–CD-3 | crt-domains.md, §§2–4 | New symbolic proof by lead; separate complete independent audits by `audit_sign_cube` and `eisenstein_sources`: PASS |

All claims have exact definitions, quantifiers, statuses, dependencies and
ledgers in their companions, dated 21 September 2026. The accompanying
manifest supplies file hashes. These are **internal** audits, not external
peer review. Agreement does not replace the written proofs.

The factor-code review checked coefficient bounds and bounded equality
specialization, action distinctness, norm counts, first-coordinate
injectivity, full encoded return distribution and the unencoded-pair
charge. During preparation a missing mathematical spacing command was
fixed and the entire mixed-term expansion added; no theorem changed.

The reflection review checked the norm-coordinate identity, orientation
reversal versus an actual pair-indexed multiplier, two targets per level,
the affine-rule polynomial, its two-root bound, rule-incidence accounting,
and the exact four-map distribution including zero. The distinction
between the certificate and possible incidental returns from a global
union of ratios was retained throughout.

The CRT reviews checked the elementary infinite supply of suitable primes,
existence and deterministic choice of the norm-prime factors, nonassociated
conjugates, exact CRT population, action independence, integrality
conditions for positive and negative width-one exponents, the norm bound,
strict congruence criterion, fourth moment and $1/48$ constant. No
substantive correction was requested. The theorem excludes nonidentity
returns only in the specified finite action box; it is not an
all-integer-power theorem and does not bound the actual image from below.

The script and three targeted tests were inspected by the lead and
`audit_sign_cube` **before** execution. The final inspected revision
includes charges for modular cube-root queries as well as the norm,
action, divisibility and full-image queries.

## 3. Frozen exact computation

One scout execution only:

```text
python3 -m experiments.correlated_returns \
  --output examples/2026-09-21-correlated-dc-o1.json \
  --pairs-output local-only/runs/T03/2026-09-21-correlated-dc-o1/pairs.json
```

The four fixed cases use $d=1,2,3,4$ and the prefixes of
$(p,\alpha)=(7,2-\omega),(13,3-\omega),(19,3-2\omega),(31,5-\omega)$.
There was no adaptive parameter expansion, random sampling or seed.
The proofs preceded this run; finite data were not used to infer the
uniform density theorem.

Each scalar action is checked in the $1,\omega$ coefficient basis and
independently in real/$\sqrt{-3}$ coordinates. Integrality is also checked
by a separate cleared-factor divisibility formula. Every actual returned
pair is checked against the full norm table. The full union-square image
uses both $x^2+xy+y^2$ and $((2x+y)^2+3y^2)/4$. All equality and
membership decisions use integers and `Fraction`; floating point is used
only for displayed geometric means. The threshold is the exact integer
ceiling of $n^{1/4}$.

| Charged query category | Count |
|---|---:|
| Local cube-root tests | 126 |
| Constructed action norm checks | 120 |
| Full-square $Q$ queries | 7,380 |
| Independent full-square $Q$ queries | 7,380 |
| Scalar action queries | 551,880 |
| Independent scalar action queries | 551,880 |
| Factor-divisibility queries | 551,880 |
| **Scout total** | **1,670,646** |

Python **3.12.7**. Measured scout CPU: **13.777365 seconds**;
wall: **13.800429 seconds**. CPU metadata is taken after all cases and
before final JSON serialization, which is excluded from this figure.
The guard is a periodically checked program budget, not an operating
system hard deadline. File writing and documentation checks are not
mathematical scouting. No unsuccessful or unreported scout run occurred.

Frozen per-pair histograms:

| Depth | Genuine returns $r:\#p$ | Criterion (5) witnesses | Integral-candidate histogram |
|---:|---|---:|---|
| 1 | $1:9$ | 3 | $1:3,2:6$ |
| 2 | $1:69,2:12$ | 45 | $1:9,2:36,4:36$ |
| 3 | $1:719,2:10$ | 297 | $1:27,2:162,4:324,8:216$ |
| 4 | $1:6519,2:42$ | 2,673 | $1:81,2:648,4:1944,8:2592,16:1296$ |

The observed maximum two is not asserted uniformly in depth. The proven
uniform statement is a positive-density identity-only subset. Every
source in this scout is nonzero, and its stabilizer is exactly the
identity. Individual domain sizes, complete image-fiber histograms and
exact geometric-mean expressions are in the frozen summary JSON.
Raw pairs/actions are local-only and must accompany a raw-data handoff
separately.

## 4. Validation budget and actual commands

The inspected local regression wrapper is copied from the preceding
cycle with only the frozen-summary locator changed. It conservatively
charges **every project Python call** in experiments/tests, including
helpers and generator resumptions, so validation queries are not treated
as free. It runs the existing required regressions, not the new scout
entry point. Its cumulative totals include the exact scout above.

| Required command | Result | Conservative project-call charges | CPU seconds |
|---|---|---:|---:|
| `python3 -m unittest discover -s tests -v` | **64 tests PASS** | 67,107 | 2.293337 |
| `python3 -m experiments verify` | **159 checks PASS** | 25,386 | 0.813451 |
| **Total including scout** | **Within both caps** | **1,763,139** | **16.884153** |

The independent final data reviewer checked every main table entry,
threshold, histogram, exact/rounded statistic, scoped conclusion and all
three execution source hashes: **PASS**. No finite observed maximum was
promoted to a uniform theorem. Logs are retained in the local run directory.

The three new tests check centered CRT completeness, the conjugate-factor
orientation in the divisibility test, and simultaneous diagonal-prime
accounting. They are small correctness tests, not additional research
cases. Source hashes in the frozen JSON identify the exact executed code
and its two unchanged arithmetic/statistics dependencies.

## 5. Repository and inheritance record

Startup found nine modified tracked files and inherited untracked work.
The run directory stores the initial status, tracked diff and SHA-256
identities of **201 pre-existing files**. Historical proofs, checkpoints,
archive files, SPECs, source manifests and previous exact data are not
rewritten. No staging, commit, push, reset, clean or remote changes.

This task adds its new note directory, one exact scout, three small tests,
a frozen example and local run records. Five shared status/library files
receive dated addenda only; immediate pre-append prefixes are hashed and
preserved. Concurrent changes, if any, are recorded separately from this
task's work.

| Check actually performed | Result |
|---|---|
| `python3 scripts/check_repository.py` | PASS: 39 archived source files and local links in 106 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local references, original identities, 43 T03 manifest members, duplicate states and C4 hashes |
| `git diff --check` | PASS |
| Baseline content audit | 196 of 201 files unchanged; the five changed files are exactly this task's dated status/library addenda; none missing |
| Append-prefix audit | All five original prefixes preserved exactly and matched startup; no concurrent baseline changes detected |

The independent final data review also confirmed all three executed-source
hashes match their current bytes. No post-execution mathematical program
edit was made. Final new-file whitespace/completion checks and manifest
content identities are retained in the local handoff. Repository checks
do not constitute mathematical proof reruns.

## 6. Handoff and scope

The [main report](README.md) is the concise reader-facing deliverable.
Its single verdict is **CORRELATED GO / TAIL FAIL**. The first two
mechanisms have scoped certificate failures; the CRT mechanism has a
proved actual-return tail failure under its selected actions. None gives
an actual quadratic-image lower bound or disproves DC-O1, ARG, TCRC,
RC15/4 or the ultimate quadratic target. HR-N1's separate disproof remains
unchanged. The final report retains exactly one next mathematical
obligation: the same correlated DC-O1 witness.

The manifest records completed report/proof/program/test/data hashes and
source dependencies, with itself omitted to avoid circular hashing.
Local-only raw data and migration references are not made public or
silently treated as tracked repository content.
