# Exact Fiber Audit and Reproducibility Record

11 October 2026 · T03 · version 1. Finite evidence is exhaustive at two
predetermined depths only. Independent symbolic proof review is recorded
separately in [audit.md](audit.md); file checks do not replace that review.

## 1. Predeclared cases and budget

The lead saved initial worktree status, inherited diffs, hashes of 379
preexisting nonignored files, and a budget policy before executing any
mathematical program. The selected track and obligation were the fixed
balanced-factor carrier's full fibers and one coupled phase/switch rule.
No archived prompt authorized an additional search.

The policy and raw records are local files under:

    local-only/runs/T03/2026-10-11-balanced-full-fibers/

The shared limits were 2000000 charged exact evaluations and 600 measured
program CPU seconds. Discovery was limited to 1600000/480; the remaining
400000/120 was reserved for verification. Only the lead could execute
mathematical programs. All three specialists had zero program allocation;
there was no nested delegation or duplicated mathematical scout.

One charged evaluation means one exact symmetry-representative or ordered
quadratic evaluation, one independent norm/pair validation, one explicit
target equality/membership test, or one exact scalar deduplication/field
identity check. Internal arithmetic is timed but is not charged repeatedly
inside a single evaluation. Carrier construction arithmetic is timed.
Aborted executions would count. Administrative file/hash/link checks are
excluded. Counts do not measure model tokens, credits or total wall time.

Exactly \(r=0,1\) were predeclared. The initial inherited scalar upper
bound already put the primary symmetry computation below 1600000 calls.
Before execution, BFF-A1 sharpened the upper bound to \(n_1\le1169\),
hence at most 342225 representatives, allowing a complete second oracle
within the verification reserve. Build then deduplicated the actual sets
and forecast 81 and 291600 representatives. The primary enumeration checked
its remaining allowance against these actual sizes before it started.

## 2. Exact arithmetic and exhaustive coverage

The inspected library is `experiments/modular_lift.py`, specifically its
cyclotomic modulus, reduction, multiplication, conjugation and integer
decoding functions. Its research main was not invoked. The new isolated
scout builds every original amplitude and every phase in \(\mu_{6q}\),
decodes both coordinates, and deduplicates exact integer vectors for \(3A\).
Reality, negation closure, origin, encoded cardinality and scalar bounds
are checked before full-square evaluation.

All arithmetic uses the Python standard library. The degree is 2 at the
seed and 12 at \(r=1\); coefficient equality modulo \(\Phi_{6q}\) is
exact. No floating-point root comparison, sampling or hash-only equality
is used. Python dictionary keys are the exact coefficient tuples; the
hashes saved for provenance are not collision or equality tests.

The primary traversal selects indices \(i\le j\) with \(i+j\le n-1\)
after lexicographically sorting the scalar tuples. Negation reverses that
order, so each sign/swap orbit is represented exactly once. It evaluates
\(a^2+ab+b^2\), using precomputed scalar squares, and adds the orbit's
actual size. The orbit counts are:

| Depth | Weight 1 representatives | Weight 2 representatives | Weight 4 representatives | Total representatives | Ordered-pair weight |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 16 | 64 | 81 | 289 |
| 1 | 1 | 1078 | 290521 | 291600 | 1164241 |

The verification oracle instead chooses one representative per nonzero
scalar sign pair and enumerates both \((a,b)\) and \((a,-b)\), plus axes
and origin. It evaluates the complex norm
\((a-\omega b)(a-\omega^2b)\) with the library's multiplication, whereas
the primary uses its own sparse-aware multiplication. Both use the same
inspected canonical field reduction; these are not advertised as two
independent implementations of algebraic number fields.

The oracle compares the complete sorted output/multiplicity distribution.
Both cases PASS. At the seed, a separate raw integer enumeration of all
289 ordered pairs also agrees. Saved output and pair-weighted histograms,
medians, strict tails and per-source baseline comparisons are in data.json.
The exact test for the strict threshold is \(f^4<n\). The baseline
comparison uses each source orbit's size, including diagonal, antidiagonal
and zero degeneracies; it does not substitute the test \(f>4\).

No selected-action scan or phase/mask sweep was executed. The optional
six-coordinate \(H\)-key proved in algebra.md was not implemented or used
to claim a second arithmetic-package verification.

## 3. Commands and actual accounting

Commands actually executed from the repository root, in this order:

    python3 local-only/runs/T03/2026-10-11-balanced-full-fibers/scout.py build
    python3 local-only/runs/T03/2026-10-11-balanced-full-fibers/scout.py scout
    python3 local-only/runs/T03/2026-10-11-balanced-full-fibers/scout.py verify

Runtime: **Python 3.12.7**. No seed or random choices. The code was inspected
before execution by the lead and specialists A/C. All three runs completed
without an execution error. No mathematical rerun was made.

| Stage and charged category | Evaluations |
|---|---:|
| Discovery: complex-point deduplication | 2400 |
| Discovery: scalar deduplication | 4800 |
| Discovery: scalar reality checks | 1096 |
| Discovery: zero-membership checks | 2 |
| Discovery: scalar negation closure | 1096 |
| Discovery: scalar squares | 1096 |
| Discovery: symmetry-negation checks | 1096 |
| Discovery: full quadratic representatives | 291681 |
| Discovery: seed scalar identity checks, corrected explicitly | 17 |
| **Discovery total** | **303284** |
| Verification: canonical scalar selection | 1096 |
| Verification: norm preprocessing | 2192 |
| Verification: complete norm representatives | 291681 |
| Verification: raw integer seed pairs | 289 |
| **Verification total** | **295258** |
| **Full-fiber audit subtotal** | **598542** |

Measured program CPU: build 0.236385 seconds, primary scout 10.777160
seconds, and verification 11.076317 seconds; total **22.089862 seconds**.
Timers cover carrier construction, exact arithmetic, mathematical aggregation
and output serialization from budget initialization through final accounting.
Interpreter startup/imports and file-only preparation before the timers are
not included. No agent executed a mathematical program. The required existing
repository regression checks below were separately metered afterward.

### Transparent counter correction

The post-run audit noticed that the build's comparison of its 17 seed
scalars with the interval was timed but had not been separately charged.
Exactly 17 discovery evaluations were added to budget.json; additional
CPU is zero because those comparisons were already inside the build timer.
The executed source is preserved byte for byte as `scout-executed.py`,
matching all three saved run hashes. The corrected reproduction source
`scout.py` charges these comparisons inline. No result, input, theorem,
execution time or finite distribution changed, and no run was repeated.

Reproduction uses the corrected script in a fresh local directory with a
fresh copy of budget-initial.json named budget.json. Output files have
no-overwrite guards. The raw directory contains both scalar sets, both full
distributions, the primary and verification results, budget versions and
both source versions. The manifest records all identities. Ignored local
files must accompany a local handoff; Git alone does not include them.

## 4. Proof audit and completion checks

The lead independently checked the new scalar bijection, product/key law,
two-component equality, all symmetry weights, the whole Laurent expansion,
the degenerate branches, the 36 correction choices, reversibility,
sign/swap invariance and arbitrary iterative closure. Specialist C read
the final written algebra and coupled proofs and recorded PASS. This is
an independent internal audit, not external peer review.

The finite results remain EXPERIMENTAL despite complete arithmetic checks.
The symbolic certificate obstruction remains scoped to its exact permitted
moves. Neither is an unrestricted full-fiber obstruction. BFF-O1's
conditional image consequence was checked, but its premise was not searched
or proved. The mathematical work stops on the one mechanism's failure.

### Required existing regressions

The isolated research program is code, so the repository-required regressions
were also run. Before execution, budget.json recorded a bounded additional
verification allowance transferred from unused discovery budget: at most
1000000 conservative charges and 90 CPU seconds, with the shared 2000000/600
caps unchanged. The initial 20% reserve was honored through the complete
full-fiber validation; this later transfer allocated unused capacity.

The wrapper `check_regressions.py` ran the normal commands in process:

    python3 -m unittest discover -s tests -v
    python3 -m experiments verify

It conservatively charged every executed source line in repository tests
and experiment modules, including arithmetic internals and comprehension
iterations. These are intentionally overcharged validation units rather than
new polynomial-query counts. Live charge and CPU guards were not reached.
No research experiment main, enlarged case, new carrier or parameter sweep
was invoked. The fixed regressions are not evidence for an asymptotic result.

Both commands PASS: **100 unit tests and 159 fixed benchmark checks**.
The additional conservative charge was **373301**, with **0.907295 CPU
seconds**. Thus final shared usage, including all current-cycle mathematical
validation, is **971843 charged units and 22.997157 CPU seconds**.
The local wrapper, command log and result file are preserved and hashed.
The log retains a nonfatal `runpy` warning: the test suite had already
imported `experiments.__main__` before the fixed verify command ran in the
same process. Both commands completed successfully; no warning was hidden
and no rerun was needed.

### Final repository and preservation checks

| Check actually performed | Result |
|---|---|
| `python3 scripts/check_repository.py` | Earlier PASS: 39 archived sources and links in 222 Markdown files; latest recheck found two unfinished links in concurrent T01 work, detailed below |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local references, original import identities, 43 T03 members, duplicate states and C4 hashes |
| Unit tests and fixed benchmark regressions | PASS: 100 tests and 159 checks, charged above |
| `git diff --check` | PASS |
| Baseline preservation | PASS: 374 of 379 baseline files unchanged; the other five have only recorded dated suffixes |
| Frozen predecessor | PASS: all eight companion hashes match its frozen manifest |
| New Markdown | PASS: whitespace, table structure and mathematical delimiters |

The first link check found the not-yet-created companion manifest; after
creating it the complete link check passed. This was a packaging correction,
not a mathematical failure or rerun. Final source/companion hashes are checked
after all records are saved.

A later repository-wide recheck encountered a newly created, unrelated
`research/notes/2026-10-11-vo-o1-freeze/README.md` with two then-unfinished
links: its PDF and `verification.md`. That file was absent from this cycle's
baseline and belongs to concurrent T01 work. Its PDF appeared by the subsequent
file-inventory snapshot; no claim is made here about later completion of that
other task. The observed check result and concurrent new files are saved in
`concurrent-work-record.json`. They were left untouched. This package's files
and source hashes remain checked; the latest global link check is not reported
as a clean pass.

The five dated suffixes update CURRENT_PROJECT_MAP, MECHANISM_LIBRARY,
FAILURE_LIBRARY, OPEN_LEMMAS and the T03 STATUS handoff. Their exact original
prefixes and current suffixes are preserved in the local run folder. No
preexisting archive, proof, canonical manifest, experiment module or test was
edited. There were nine inherited modified tracked files and substantial
inherited untracked work; these remain preserved. All changes are uncommitted.
