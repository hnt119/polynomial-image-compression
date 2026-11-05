# Return-tail cycle — internal audits, exact computation and provenance

21 September 2026 · T03 · fixed $Q=x^2+xy+y^2$.
Strictly offline. No external theorem import, literature search or novelty
claim. This record separates proof work, exact finite scouting and
repository integrity checks.

## 1. Authorization and scope

The active user attachment is
`[private attachment identifier withheld]`, titled
“Offline Correlated Return-Tail Search for Q(x,y)=x^2+xy+y^2.” It explicitly
commissions the present constructive cycle. Older attachments and frozen
next-task statements were used as context, not as competing assignments.

The announced scope was three mechanisms: cyclotomic trace domains,
full-residue modular gadgets with no nonzero identity-only state, and
rational carriers organized by denominators. The geometry note is the
requested structural lemma, not a fourth carrier. The shared budget was
**2,000,000 charged evaluations and 600 research/validation CPU seconds**.
The parent retained all mathematical program execution; symbolic agents
ran none. No broad prime search or parameter expansion took place.

The setup/map/migration audit, T03 current-state/master context, track
SPEC/STATUS, conflicts, current checkpoint/companions and relevant library
entries were consulted. Source authority remains distinct from proof
verification. The earlier CRT cube-root, moving-pole, balanced-state and
tensor failures are preserved. No historical theorem was silently
reconstructed. HR-4A/B's complete elementary arithmetic proofs were read
and cited where used; those old experiments and proofs were not rerun as
new research. No unavailable external input was needed.

## 2. Claim and internal review record

| Claims | Complete proof | Authorship and independent checks |
|---|---|---|
| RT-G1–RT-G3 | geometry.md, §§1–3 | `audit_sign_cube`; independent audit by `norm_trace`; lead inspection: PASS |
| CY-1–CY-3 | cyclotomic-domains.md, §§1–6 | `norm_trace`; independent full audit by `eisenstein_sources`; lead independent reconstruction/inspection: PASS |
| MG-1–MG-4 | modular-gadget.md, §§1–4 | `eisenstein_sources`; independent full audit by `norm_trace`; lead inspection: PASS |
| RT-D1–RT-D3 | denominator-domains.md, §§2–4 | Lead; independent full audit by `audit_sign_cube`: PASS after the quantifier clarification below |

Each companion gives its quantified hypotheses, definitions, exact proof,
status and construction ledger. The manifest supplies version hashes and
dependencies. These are **internal reviews**, not external peer review;
review agreement is not substituted for the written argument.

The geometry review checked the transformed triple intersection, missing
ratio-domain condition, ordered second moments, zero corrections, strict
lower tail, constant absorption and rectangular variant. The main summary explicitly assumes $N>0$ before division; the singleton
zero case remains in the companion. The sufficient
variance estimates are not asserted for any construction without proof.

The cyclotomic review checked irreducibility over **Q(omega)**, not merely
Q; sparse equality; all frequency-support cases; all sixteen constant
pairs; the exceptional orbit; exact domains; statistics; and field costs.
A preliminary symbolic tally of the four constant norm-seven pairs was
corrected before the written theorem and execution: their selected unit
returns are only the two signs. The final complete proof and both audits
use the two-class histogram R=2 and R=6p. No failed or discarded numerical
run was involved.

The modular review checked the explicit local table, root lifting, split
coordinates, composition, valuation stabilizers, complete prime-power
histogram, exact tail summation, carry counterexample and homomorphic-lift
scope. The real identity-only count for the six unit actions was made
explicit using the independently proved sign lemma; the stronger
all-action obstruction for the real lift remains an application of
retained HR-4A/B.

The rational review checked reduction of the source norm denominator,
three possible least-common-multiple states, divisor multiplicities,
positive-density coprimality count, constants and zero handling. It
requested one quantifier clarification: the new actual-image lower bound
is stated **along H=12L**, the sequence supported by the proof. That
wording was corrected before finalization; no unsupported all-H statement
is retained.

## 3. Pre-execution gate and exact scout

The whole-scalar composition identity and complete cyclotomic domain
classification passed the lead and independent mathematical audits before
execution. `audit_sign_cube` separately inspected the new exact program
and three tests before execution. That code audit explicitly did not
substitute for field-faithfulness or the mathematical domain proof.

One fixed scout execution:

```text
python3 -m experiments.return_tail \
  --output examples/2026-09-21-return-tail.json \
  --pairs-output local-only/runs/T03/2026-09-21-return-tail/pairs.json
```

The only cases were the two predetermined eligible primes **11 and 17**.
This was an exact check of the stated construction and all its domains,
not a search over primes. The other mechanisms were rejected by their
analytic real-lift/tail gates, with no unnecessary finite runs.

Arithmetic uses integer coefficients in Z[omega,xi], with equality reduced
modulo Phi_p over Q(omega). The proved irreducibility justifies that
representation. Both action calculations are exact:

- Multiply the whole complex source by u, then recover 3x',3y'.
- Independently form 3a,3b for u=a+b*omega and apply the real coefficient
  matrix to x,y.

Comparison with 3A avoids division without changing membership. Every
ordered source/action is checked by both formulas. The full scalar image
is calculated both directly and as z*conjugate(z). Every returned target
is checked against the precomputed norm table. The exceptional orbit is
constructed explicitly as (1+2omega)U, not assumed from a Q-level.
All source and action duplicates are removed, every stabilizer is checked,
and every individual domain size is compared to the proved classification.
The threshold is the exact integer ceiling of n^(1/4). Only displayed
geometric means use floating point.

| Charged query category | Count |
|---|---:|
| Constructed action norm checks | 168 |
| Constructed exceptional orbit points | 168 |
| Full-square Q queries | 3,860 |
| Independent full-square Q queries | 3,860 |
| Whole-complex scalar action queries | 352,104 |
| Independent matrix action queries | 352,104 |
| **Scout total** | **712,264** |

Python **3.12.7**. Measured research CPU **9.963013 seconds**; wall
**9.979887 seconds**. Metadata is taken after all cases and before final
JSON serialization, which is excluded from these figures. The program
budget is checked periodically; it is not presented as an operating-system
hard deadline. Documentation writing and file integrity checks are not
mathematical scout queries. No failed or unreported scout execution occurred.

## 4. Frozen distributions and interpretation

| Prime | Full return histogram r:number of ordered pairs | Identity-only | Domain sizes | Full image |
|---:|---|---:|---|---:|
| 11 | 2:1090; 66:66 | 0 | two domains of size 1156; 64 domains of size 66 | 290 |
| 17 | 2:2602; 102:102 | 0 | two domains of size 2704; 100 domains of size 102 | 677 |

The threshold ceiling is three in both cases. Every source is nonzero and
has stabilizer one, so returning action counts equal distinct target
counts. Exact geometric-mean expressions, full image-fiber histograms and
individual action-domain sizes are in the frozen summary. Raw files retain
every field element, action label, output and returned pair.

The finite image sizes do not establish an asymptotic image formula or
lower bound for the cyclotomic carrier. Its negative result is the exact
selected-action return theorem. The rational carrier's separate actual
image conclusion follows from its full-fiber proof, and the integer lift
uses the previously proved integer-fiber bound. These scopes are distinct.
The modular table and tail are mathematical formulas over a finite ring,
not finite real-set experiments.

## 5. Required regressions and shared budget

The inspected local-only wrapper copies the preceding cycle's guard with
only its summary-data locator changed. It conservatively charges every
project function call in experiments/tests, including helpers and generator
resumptions. It runs the existing required tests and verification, not the
new scout entry point. Thus validation is included in the announced budget.

| Required command | Actual result | Conservative project-call charges | CPU seconds |
|---|---|---:|---:|
| `python3 -m unittest discover -s tests -v` | **81 tests PASS** | 77,319 | 2.805247 |
| `python3 -m experiments verify` | **159 checks PASS** | 25,386 | 0.800854 |
| **Total including scout** | **Within both caps** | **814,969** | **13.569114** |

The final independent read-only data review checked every main table entry,
threshold, return/domain/image histogram, exact and rounded statistic, and
all three executed-source hashes: **PASS**. It verified that finite image
counts were not promoted to asymptotic statements. No mathematical program
was edited after the scout. Full logs are retained locally.

The three new tests check the cyclotomic reduction relation and nonzero
monomials, conjugation/trace/norm behavior, and both three-scaled action
oracles on distinct traces. They are targeted arithmetic checks, not
additional growing carrier cases. Execution metadata records the exact
hashes of the new program and its two unchanged helper modules.

## 6. Repository inheritance and integrity

The initial worktree was already uncommitted, with nine modified tracked
files and substantial prior untracked work, including later T01 research.
The run directory preserves that status, the initial tracked diff and
SHA-256 hashes of **231 pre-existing files**. Nothing was staged,
committed, pushed, reset, cleaned or changed in Git remotes.

This task adds its own note directory, one scout, three targeted tests,
a frozen example and local raw/audit records. Five current status/library
files receive dated append-only handoff entries. Their immediate original
prefixes are separately hashed and verified. Historical proof/checkpoint,
archive, SPEC, source-manifest and prior data files remain immutable.
Concurrent differences, if detected, are recorded separately.

| Check actually performed | Result |
|---|---|
| `python3 scripts/check_repository.py`, initial run | FAILED only on a missing `verification.md` link in concurrent `research/notes/2026-09-21-nonlinear-reuse/README.md`; this task did not alter that work |
| Scoped local-link check for all six new report/proof notes | PASS |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local references, original identities, 43 T03 manifest members, duplicate states and C4 hashes |
| `git diff --check` | PASS |
| Initial baseline audit | 226 of 231 baseline files unchanged; five changes are this task's append-only status/library files; none missing |
| Final baseline audit | 225 of 231 unchanged; the additional changed file is concurrent T01 STATUS, outside this task; none missing |
| Prefix audit | All five original prefixes preserved exactly and match startup at both checks |

Concurrent T01 work added a new `nonlinear-reuse` report, program, tests
and data after this task's baseline. They are not attributed to this
cycle or modified here. The 81-test run includes the tests present at
its execution time. The scoped link check verifies this cycle without
claiming that the initial repository-wide check passed. A final check,
if completed after the concurrent missing file appears, is recorded below.

The final repository-wide check **PASSed** after the concurrent verification
note appeared: **39 archived sources and local links in 133 Markdown
files verified**. This task did not create or edit that T01 note. The
initial failure remains recorded in the local check log.
The final baseline audit also detected the concurrent T01 STATUS update;
it is recorded separately and is not attributed to this cycle.

The content manifest identifies report, proof, state, program, test,
summary and local run files, omitting itself to avoid a circular hash.
Ignored raw files and private migration references must accompany a local
handoff separately; a Git copy alone does not include them.

## 7. Final scope

The one cycle verdict is **RETURN-TAIL FAIL**. All three proposed real
realizations have a proved quadratic-size low-return set in their stated
scopes, even though identity-only counts are zero or one for the explicit
sign-containing action families. The strong finite-ring tail is retained
as a proved modular result, with the failed real-lift gate explicit.

DC-O1, the real quadratic target, ARG/TCRC and RC15/4 remain OPEN. HR-N1
retains its separate DISPROVED status. The main report ends with one next
obligation: an actual real correlated return-tail witness. No barred
carrier or broad new search is launched by this handoff.
