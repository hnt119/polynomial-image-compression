# Unit-exponent cycle — verification, sources and provenance

**16 September 2026, version 1. T03; fixed $Q=x^2+xy+y^2$.**
Main result: [report](README.md). Complete arguments:
[primary](primary-proof.md) and [secondary](secondary-proof.md).
File identities: [manifest](manifest.json).

## Authorization and limits

The user attachment **Full-Rank Quadratic Compression — Unit-Exponent
Cartesian Carrier Cycle** commissioned the primary exponent-orbit carrier
and, after Cartesianization failure, one secondary valuation-box mutation.
The offline restriction was explicit. Before research the lead announced
a shared cap of **2,000,000 charged evaluations and 600 research CPU
seconds**, including validation. The exact schedule was frozen to the two
defined carriers, $L=h=1$, $d=1,2,3$.

No web search, browser, external API/connector, network command, literature
query, installation, download or remote Git operation occurred. No imported
historical research program was executed, no third family was introduced,
and no difference-set or affine problem was investigated. Existing finite
regressions were run only as required validation, not as new research cases.

## Source and proof inspections

Startup inspection included Git state/diff, setup/map/migration audit, the
master handoff, all sections of T03 current state, relevant TCRC companion
proofs inside the inspected local ZIP, T03 SPEC/STATUS, migration conflicts,
and relevant mechanism/failure/open-lemma entries. Archived instructions
were treated as historical context. The controlling assignment is the new
user attachment, not the earlier HR-N1 freeze or an old checkpoint task.

The independent source/scope audit located:

- HR-1's complete finite-fiber support proof in
  [return-lemma.md](../2026-09-16-high-return/return-lemma.md).
- HR-4A's self-contained Eisenstein factorization proof and HR-4's exact
  dense one-prime scope in
  [denominator-obstruction.md](../2026-09-16-high-return/denominator-obstruction.md).
- HR-6's fixed cyclic multiplier and seed-box hypotheses in
  [carrier-screen.md](../2026-09-16-high-return/carrier-screen.md).
- The already recorded one-shell projection observation in the
  [constructive report, §E](../../history-sources/Q_Constructive_Local_Compression_to_Real_Set_Report.md).
- The preceding [two-prime cycle](../2026-09-16-two-prime-character/README.md)
  and [HR-N1 freeze](../2026-09-16-hr-n1-final-freeze/README.md).

No unavailable external result is required. In particular, no prime-density
theorem or prime factorization computation enters the explicit generator
recursion. The $q_i$ are composite-allowed coprime norm blocks, and the
selected norm-one elements are fractional units, not integral units.

### Internal review record

| Review | Checked and result |
|---|---|
| Primary derivation | Separate analyst wrote the complete independence, orbit-product, boundary/tail and projection proofs. Lead inspected the full argument, including exact $n=2M$ and all root-of-unity identities. PASS. |
| Secondary derivation | Separate analyst audited the lead's proposed minimum-valuation and six-term-specialization arguments and wrote complete proofs. Lead inspected splitting, composite-block minima, both exponent signs, full-image classification and rates. PASS. |
| Independent primary review | Secondary analyst independently checked UE-P1–P3: actual action growth, exact returns, tail, coordinate injectivity, shell scope and OPEN cross-pair limitation. PASS. |
| Independent secondary review | Primary analyst independently checked UE-S1–S2, especially the existence of one prime with residual valuation below its block multiplicity and every diagonal/sign degeneracy. PASS. |
| Pre-execution code review | Third analyst checked exact formulas, full ordered-pair coverage, independent oracle, zero/stabilizers, statistics, projection fibers, frozen schedule, budget and exclusive outputs. One correction: compare each labelled oracle action to its corresponding primary target, in addition to aggregate sets. Fixed before the only run. |
| Final report review | Third analyst checked the complete report against both proofs and saved JSON: all six cases, rates, zero handling, scopes, source caveats and the sole next obligation agree. PASS. This consistency review was not another research run. |

One explanatory sentence was added after review to make the primary typical
rate explicit: the binomial variance and Markov's inequality for its squared
deviation give convergence in probability. No theorem changed. These are
internal mathematical reviews, not external peer review or novelty evidence.

## Exact computation

Program: [unit_exponent.py](../../../experiments/unit_exponent.py).
Runtime: **Python 3.12.7**, standard library only. Source SHA-256:
`11ef12740645b5ad4ec2bb597f52195e07d84c9f353ae0cfb131472f54fd681a`.
It was inspected before execution and remained unchanged after the run.

```bash
python3 -m experiments.unit_exponent \
  --output examples/2026-09-16-unit-exponent.json \
  --pairs-output local-only/runs/T03/2026-09-16-unit-exponent/pairs.json
```

The two output paths must be different and new. The JSON summary contains
the explicit integer blocks, rational scalar lists, all return and image
histograms, exact fractions and geometric-mean expressions. Its raw
companion contains every pair's coordinates, norm, three return counts,
finite stabilizer, engineered-membership flag and returned-set hash.
No random seed or sampled subset is used.

The primary action uses the $1,\omega$ basis; the independent oracle uses
$1,\sqrt{-3}$ and direct complex multiplication. Every labelled action
target agrees, including targets outside the carrier. Every ordered pair's
norm is also checked against $((2x+y)^2+3y^2)/4$. At zero, the finite
action stabilizer has $3^d$ elements but the returned-pair count is one.
Every equality test uses `Fraction`; only logarithmic summaries are rounded.

| Query category | Charged count |
|---|---:|
| Constructed action norm checks | 39 |
| Orbit/action tests | 819 |
| Scalar polynomial evaluations | 6,552 |
| Scalar action/pair tests | 163,512 |
| Oracle action/pair tests | 163,512 |
| Oracle polynomial evaluations | 6,552 |
| **Diagnostic total** | **340,986** |

The diagnostic ran exactly once, with **5.944325 CPU seconds** and
**5.945250000004307 wall seconds**. All asserted predictions and oracle
checks passed. There were no failed mathematical runs or reruns.

## Required regressions and combined budget

The existing tests and relevant modules were inspected before execution,
including the separate three-branch modules imported by current tests.
The standard module commands were executed through a local `runpy` guard:

```bash
python3 -m unittest discover -s tests -v
python3 -m experiments verify
```

The wrapper adds the repository import path and conservatively charges
every Python call in `experiments/` or `tests/`, including helper functions
and generator resumptions. It checks the cumulative budget against the
diagnostic and earlier regression logs. This overcounts mathematical
queries, and ensures regression work is not treated as free.

| Execution | Result | Charges | CPU seconds |
|---|---|---:|---:|
| Exact two-carrier diagnostic | All six cases and oracle checks PASS | 340,986 | 5.944325 |
| Unit suite | **52 tests PASS** | 64,746 | 2.171053 |
| Finite baseline verification | **159 checks PASS** | 25,386 | 0.795420 |
| **Total** | Within both shared caps | **431,118** | **8.910798** |

Wrapper source, exact module arguments, per-function counts and output logs
are in `local-only/runs/T03/2026-09-16-unit-exponent/`.
No additional research query is performed by file hashing, link checks or
formatting verification. Those metadata checks are not proofs.

## Preservation and file scope

The inherited checkout had nine modified tracked files, totaling 1,010
insertions and 58 deletions, plus many existing untracked artifacts. Those
changes predate this cycle. Git status and diff at the preservation
checkpoint were retained locally, together with hashes of **137 protected files** and original
bytes of five potential current-state append targets. The independently
active three-branch continuation note directory was excluded from the
protected historical-note set; this cycle does not edit it.

New files in this cycle are only:

- `research/notes/2026-09-16-unit-exponent/README.md`,
  `primary-proof.md`, `secondary-proof.md`, `verification.md`, `manifest.json`;
- `experiments/unit_exponent.py`;
- `examples/2026-09-16-unit-exponent.json`;
- ignored raw/provenance records in the corresponding `local-only/runs/T03/`
  directory.

After mathematical completion, dated addenda are appended to the current
project map, T03 STATUS, and the failure/mechanism/open-lemma libraries.
Immediate pre-append bytes and exact added sections are retained separately
so unrelated shared-checkout changes are not attributed to this cycle.
Historical reports, old SPECs, original manifests, imported sources,
existing experiment modules and tests are preserved. No commit, staging,
reset, cleanup, push, remote change or historical rewrite is performed.

## Final validation

| Check actually performed | Result |
|---|---|
| `python3 scripts/check_repository.py` | PASS: 39 archived sources and local links in 77 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 42 local references, original import identities, 43 T03 manifest members, duplicate states and C4 hashes; no research code executed |
| `git diff --check` | PASS |
| Separate `git diff --no-index --check /dev/null FILE` on seven new files | PASS; ordinary Git diff would omit these untracked artifacts |
| Protected-file hashes | PASS: all 137 baseline identities unchanged |
| Five current-state append records | PASS: immediate prior bytes and exact appended sections unchanged |
| Other tracked diff blocks | PASS: eight match the saved preservation-checkpoint diff; only this cycle's T03 STATUS append changes the ninth |
| Independent final report consistency review | PASS, with no corrections requested |

The first Git inspection reported 1,010 inherited insertions. A separate
T01 STATUS appendix appeared before the preservation checkpoint was saved;
it is included in that saved baseline, not attributed to this cycle. The
comparison above refers to that precisely retained checkpoint.

`preservation.json` records the actual comparison counts. The manifest
identifies finished artifacts and local records by hash, and identifies
the five append sections separately from shared navigation files. It does
not require those navigation files to remain frozen against later tasks.
No integrity check is represented as a mathematical proof audit.

All required code regressions passed earlier in this cycle; no subsequent
code change required a rerun. The final deliverables remain uncommitted.
