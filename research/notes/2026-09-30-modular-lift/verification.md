# Verification and provenance

30 September 2026 · T03 · strictly offline modular-to-real lift cycle.

## Authorization, source and inheritance

The controlling request is the attached “7^k Modular-to-Real Lift for the
Eisenstein Quadratic”, attachment `[private attachment identifier withheld]`.
This commissions a new lift cycle, not a replay of earlier research prompts.
The setup, project map, migration audit, master/T03 current state, historical
SPEC, current STATUS, conflict register, latest return-tail checkpoint,
MG-1–MG-4 companion and DC-R1 proof were inspected for the relevant claims.
The full historical source package was not newly audited. The initial
lookup for a `faithful-projection.md` companion failed; the actual source
was located and read as `matrix-product.md`, §5, DC-M4. No missing source
was reconstructed from a title.

The initial worktree had nine modified tracked files and extensive prior
untracked work. Local records preserve the status, tracked diff and hashes
of 252 pre-existing files. No historical source is to be modified, and no
commit, stage, push, reset, clean or remote change is authorized or made.

## Mathematical verification before scouting

The lead derived the proofs in proofs.md, then checked these separately
against their statements: carry signs and zero cases; the permutation-cycle
factorization; generator order and projection fibers; the complete Gram
coefficient bounds; characteristic-zero degree inequality; reality of both
coordinates; orbit count and stabilizers; scalar-shell disjointness; cross-
shell selected returns; the independent four-target full-fiber proof; and
finite histogram/image decomposition. The state-cover theorem was checked
with its faithful-action and bounded-fiber hypotheses, and its primitive-
pair escape explicitly retained.

These are lead proof checks, **not independent internal or external review**.
No subagent was commissioned this turn. Older review records apply to older
proofs only. No literature search or novelty claim is made.

The exact identity (10), injectivity, and decomposition equations (19)-(20)
were written and checked before execution. This is the algebraic gate.
The scout checks only predetermined k=1,2. No candidate parameters are
chosen from its results; no failed family will be expanded. Other direct
lift architectures are resolved analytically in their stated scopes.

## Exact program and finite-budget definition

`experiments/modular_lift.py` was inspected before execution. It constructs
Phi_6 and Phi_42 by exact monic integer division, and works in their
cyclotomic fields using coefficient tuples. It enumerates the angular
cores S^2, verifies each action by both complex multiplication and the
three-scaled real matrix, deduplicates all targets, checks every returned
norm, and independently compares direct Q with z*conjugate(z).

It enumerates all primitive modular orbits at k=1,2 using the fixed generator
-2. Full completed-carrier statistics are **derived from the proved
shell decomposition**, not claimed to be an exhaustive N^2-by-m numerical
run. The radical is represented by proved linear independence through
power 2t; it is never approximated or numerically clustered.

Announced research cap: **100,000 exact research evaluations and 60 CPU
seconds**. One charged evaluation is a modular orbit transition, a core Q
query, its norm oracle, an action query or its matrix oracle. Python helper
operations and document/hash checks are not separate mathematical queries.
Required repository regression tests are recorded separately from this
scouting budget; they do not search new carrier cases. The clock is checked
at each charged query; it is a program guard, not an OS deadline. Only a
displayed geometric mean uses floating point.

Commands, results, actual budgets and file identities appear below after
the fixed run and required checks.

## Frozen finite run

```text
python3 -m experiments.modular_lift \
  --output examples/2026-09-30-modular-lift.json \
  --raw local-only/runs/T03/2026-09-30-modular-lift/core-and-orbits.json
```

Python 3.12.7. Exactly one scout execution; fixed k=1,2. No errors,
failed runs, retries, unreported cases or post-run code edits.

| Charge | Count |
|---|---:|
| Primitive modular orbit transitions | 2,400 |
| Angular-core Q evaluations | 450 |
| Independent norm evaluations | 450 |
| Angular complex actions | 18,576 |
| Independent matrix actions | 18,576 |
| **Total research evaluations** | **40,452 / 100,000** |

Research CPU **3.072220 seconds**, wall **3.086177 seconds**. Timing is
recorded after mathematical cases, before final JSON serialization.
Executed source SHA-256:
`0be8b14d111991ec4df96141702e9f4ef156088fc70c3517abd377240b0f6f14`.
No other research script was executed. The finite-field modular tail
was not reproved computationally; orbit-label enumeration checks only
the newly used encoding and its free-orbit count.

| k | Full derived return histogram | Full derived image | Threshold ceiling |
|---:|---|---:|---:|
| 1 | 1:1; 2:240; 6:48 | 73 | 3 |
| 2 | 1:1; 2:1,251,264; 6:3,024; 42:2,352 | 313,657 | 6 |

All numbers include zero. The geometric means are approximately 2.394602
and 2.016753; the exact histograms define them without rounding. The
complete angular cores have respectively 9 and 441 ordered pairs; their
images have sizes 3 and 102. The full completed squares have 289 and
1,256,641 pairs. These distinctions are maintained in the report and
raw files. Formula-derived counts are not described as independent
full-square enumeration. No asymptotic claim is inferred from two cases.

## Post-run mathematical and documentation checks

The lead checked the formulas again independently of the finite program:
zero deduplication; no fixed points of the sine reflection because m/2
is odd; radical degree over the whole cyclotomic field; least/greatest
exponents in a mixed norm; exactly four full targets; all three kinds of
pair in the histogram; and the explicit modular-unit restriction costs.
The unit restriction was clarified to include its separately completed
cross-shell population; adjoining zero, if necessary, costs one scalar.
The single future mechanism was made explicit using amplitudes in the
same cyclotomic field. Neither clarification changes the scout identity
or the full-carrier formulas. They are proof/documentation work, not new
parameter cases or an independent review.

ML-2 states an image-size collapse, not a universal impossibility for
all noninjective encodings. ML-5 explicitly permits escaping by input
restriction or polynomially many states. The paired construction's
actual-image lower bound follows from a full-fiber theorem. These
limitations prevent the scoped failures from becoming an unsupported
universal rejection of the modular route.

## Required repository checks

| Command / check | Result |
|---|---|
| `python3 -m unittest discover -s tests -v` | **88 tests PASS**; includes three new arithmetic tests |
| `python3 -m experiments verify` | **159 checks PASS**; existing finite benchmark scope |
| `python3 scripts/check_repository.py` | **PASS**, 39 archived sources and links in 139 Markdown files at the check |
| `python3 scripts/check_codex_setup.py` | **PASS**, 50 local references, 43 T03 archive members and retained identities |

These regression checks are separate from research scouting and do not
constitute a proof of the research target. Logs are retained under
`local-only/runs/T03/2026-09-30-modular-lift/`. The test count reflects the
current inherited repository, not the previous cycle's earlier count.

## Final integrity and concurrent work

The executed program hash and raw angular histograms were checked against
the frozen summary after the run. The median, threshold counts and full
histogram totals agree. New-file formatting and local links are checked
separately from inherited files. `git diff --check` passed.

The baseline audit preserved all 252 original files: 247 are unchanged
and five current handoff files have append-only dated entries, with their
original prefixes matching the startup hashes. Historical proofs, source
archives, SPECs and canonical data remain unchanged. No files are staged
or committed. The final manifest identifies the new report, proofs, ledger,
state, program, tests, finite summary and local raw/log files by hash.
Ignored raw data and private references must accompany a local handoff
separately; Git alone does not include them.

After the initially successful repository check, a later check found a
missing `verification.md` link in concurrent
`research/notes/2026-09-30-near-complete-charts/README.md`. That new T01
work was absent from this task's baseline and was not edited here. All
four Markdown notes in this cycle pass their scoped link check. This
unrelated transient failure is retained in the local checks record;
any later final result is recorded there and below.

Final repository-wide check: **FAILED solely on the concurrent T01 missing verification-note link identified above**. This cycle's scoped links, baseline/prefix audit, tests, finite benchmark checks, setup check and diff check all passed.
