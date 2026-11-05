# Validation and evidence ledger

Date: **16 September 2026**. This file records actual research, proof review
and software checks separately. Finite checks do not prove the target.

## Mathematical review

- HR-1: parent independently derived the fiber-partition argument before
  carrier search, then read every written threshold, chosen-lift,
  reciprocal, projection and rate variant.
- HR-2/3/4: parent proposed the valuation and depth-gap arguments; an
  independent agent supplied full proofs, including the elementary norm
  representation/divisor bounds. Parent read the completed proofs and
  checked quantifiers, orientations, injection across small gaps and the
  uniform constants. HR-4 bounds every output fiber, not just cyclic orbits.
- HR-5/6/7/8: proofs were developed independently and read by the parent.
  Return obstructions are distinguished from full-image lower bounds.
- A final independent reader checked the main report and HR-4; any material
  findings are recorded in the completion addendum below.
- The cyclotomic degree/basis fact was checked in the identified primary MIT
  notes. No literature/priority audit or claim of external novelty was made.

## Exact scouting

Command:

```sh
python3 -m experiments.cartesian_returns --output local-only/runs/T03/2026-09-16-high-return/results.json
```

All **18/18** fixed cases completed, with **zero experiment errors**, using
Python **3.12.7**. The main program reports **863,636 charged evaluation
units**, comprising 680 construction actions, 202 norm-preserving matrix
checks, 58,415 polynomial evaluations and 804,339 return-action tests.
Its CPU time was **0.468425 seconds**. Every carrier square was enumerated.
The raw output retains full input lists, state transitions and hashes.

A matrix check evaluates three coefficient identities and is one unit in
the program's counter. Conservatively charging the three identities
separately adds **404**, giving **864,040** main-run units for the cycle
budget. This is an accounting refinement; no code or mathematical result
changed and no main-run replay was needed.

The new tests use 394 implementation-counter units, plus small independent
rational oracles; the standard repository regressions use their existing
fixed small ranges. A deliberately loose **100,000-unit allowance** covers
all fixed regressions, oracles and matrix-check adjustments within those
tests, based on inspecting their finite loops. This is an upper allowance,
not a measured count. The total conservative cycle charge is therefore at
most **964,040**, below the announced **2,000,000** budget. Research CPU
use and the small regression timings remain far below **600 seconds**.
File reads, report generation and source-integrity checks are not research
pair evaluations. No stochastic experiment was run.

The main code was read before execution and independently audited. The
auditor corrected the metadata to say **all nonzero cyclic returns** are
covered: infinitely many powers fix zero, although the finite selected
family and its stabilizer are recorded exactly. This correction occurred
before the main run. The executed source is preserved with the raw result.

## Checks actually run

| Command | Result |
|---|---|
| `python3 -m unittest discover -s tests -v` | **PASS**, 42 tests; reported test time 0.032 seconds |
| `python3 -m experiments verify` | **PASS**, all 159 existing finite benchmark checks |
| `python3 scripts/check_repository.py` | **PASS**, 39 archived source files and local links in 54 Markdown files |
| `python3 scripts/check_codex_setup.py` | **PASS**, 42 local reference files, original import identities, 43 T03 manifest members, duplicate states and C4 hashes; no research code executed |
| `git diff --check` | **PASS**, exit code 0 |

The four new tests compare integer matrix powering with an independent
repeated `Fraction` action, compare every histogram against small full-pair
oracles, check a full repair step, and verify budget/preflight refusal.
No full research schedule is invoked by the tests.

## Files and uncommitted state

This cycle created only:

- `research/notes/2026-09-16-high-return/` and its proof/report/manifest files;
- `experiments/cartesian_returns.py`;
- `tests/test_cartesian_returns.py`;
- `examples/2026-09-16-cartesian-returns.json`;
- ignored raw outputs under `local-only/runs/T03/2026-09-16-high-return/`.

The pre-existing nine tracked modifications retain the same diff statistics
as at cycle start: 912 insertions and 58 deletions. They belong to earlier
work, not this cycle. Prior untracked research/setup files also remain.
No original archive, migration copy, historical section or track SPEC was
modified. No staging, commit, push, reset, clean or remote operation occurred.

`manifest.json` hashes this cycle's portable artifacts (excluding itself).
The separate ignored raw `source-manifest.json` identifies the local formal
sources and selected ZIP members. These local references must accompany a
local handoff; they are not implied to exist in Git.

## Completion addendum

The final independent proof reader found no defect in HR-4. It also checked
the next obligation's norm-one multiplier and exact input count. One summary
scope qualifier was corrected before completion: the logarithmic cyclic
return bound of HR-2 is for **p=7**, while the full-image HR-4 theorem is
uniform over **all primes**. The main report now states both scopes.

The executed source matches the SHA-256 recorded in the main result and is
preserved in the ignored run directory. The final source manifest identifies
14 local files and seven selected Markdown ZIP members without modifying
or extracting the archive. New portable files received a separate content
and whitespace inspection; tracked `git diff --check` alone does not inspect
untracked artifacts. All checks above passed. These checks establish file
and finite-code integrity, separately from the written mathematical proofs.
