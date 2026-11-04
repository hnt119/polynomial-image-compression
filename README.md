# Polynomial Image Compression

Research notes and reproducible experiments on small polynomial image sets, motivated by unit-distance constructions, sum-product methods, and the Elekes–Rónyai problem.

The central question is whether a **fixed** polynomial $P\in\mathbb R[x,y]$, depending on both variables, admits a **fixed** $\varepsilon>0$ and arbitrarily large finite sets $A\subset\mathbb R$ such that

$$
|P(A,A)|\le |A|^{2-\varepsilon}.
$$

The same set occurs in both inputs. The exponent may depend on the fixed polynomial, but cannot change with the size of the set.

## Start here

- [Codex local setup](docs/CODEX_SETUP.md): instructions, checks, and local reference transfer.
- [Concise current project map](research/CURRENT_PROJECT_MAP.md) and [2026-09-14 setup audit](research/CODEX_MIGRATION_AUDIT.md).
- [Reconciled project history](research/PROJECT_HISTORY.md): current four-track state, shared progress, and retained chronology.
- [Track specifications and status](research/tracks/README.md): one precise target and continuation record per track.
- [Mechanism library](research/MECHANISM_LIBRARY.md), [scoped failures](research/FAILURE_LIBRARY.md), and [open lemmas](research/OPEN_LEMMAS.md).
- [Migration conflicts and source identities](research/MIGRATION_CONFLICTS.md): unresolved issues, authority order, and resolved corrections.
- [Historical research overview](docs/research-overview.md): earlier questions and mechanisms.
- [Historical roadmap](docs/roadmap.md): earlier proposed steps; use the reconciled open-lemma registry for current obligations.
- [Historical source record](docs/sources.md): the original archive inventory; current availability is recorded in the migration audit.
- [Reproduce the experiments](docs/reproducibility.md): exact finite computations and their limits.
- [Publish to GitHub](docs/publishing.md): remaining setup for this prepared local repository.

## Research status

Reconciled **11 September 2026** against the latest final records and current-state
exports, with research cutoff **10 September 2026**. This is documentation
reconciliation only; no new proof search, mathematical experiment, or external
novelty assessment was performed.

Eight track recovery addenda/manifests were integrated on **20 September 2026**.
They retain the same 10 September mathematical cutoff and do not supersede the
later dated records in this repository. The attached intake did not include the
larger original-source packages described by those manifests; that boundary is
recorded in the migration conflict register.

| Track | Fixed polynomial | Current recorded state |
| --- | --- | --- |
| T01 | $(x-y)^3+x+y$ | **OPEN**. Continuous-cover and regular/fixed-prime positive-entropy digital routes are closed in their exact scopes; no supported cubic candidate survives. The separate norm–trace quadratic branch is also open. |
| T02 | $(x+2y)^4+3x-y$ | **OPEN**. C2/C3/C4 local structure and counts are proved; the stated full-interval class-packing routes fail. The quartic conjecture is not disproved. |
| T03 | $x^2+xy+y^2$ | **OPEN**. Adaptive radical counts are certified through $(n,s)=(32,269)$; the uniform RC15/4 signed-root support bound is open. |
| T04 | $(x-y)^3-3(x+y)$ | **OPEN**. The selected complementary-unit affine system has proved input entropy; a strict full-image output gap remains open. |

Shared progress is recorded separately: Phase A high-degree sum-product
reconstruction; Phase B's collision/support distinction; local-to-global
split-prime amplification with uniform residue packing; and the corrected
Phase C0 family $P=(ax+by)^2+cx+ey$, with integral coefficients,
$\gcd(a,b)=1$ and $ab(ae-bc)\ne0$, **PROVED within the supplied source system**.
The corrected C0 proof is now locally available. C0 is not one of the four
tracks and does not solve the fixed quartic or full-rank quadratic.

The latest shared supervisor direction is general quadratic forms via
addition and multiplication, norm/trace, and more general solvable extensions.
Its construction frontier remains **OPEN**. No new cycle starts in this migration.
The handoff's caution about related external quadratic constructions is retained;
no external novelty is claimed.

The four `SPEC.md` files remain unchanged. Their dated route descriptions must
be read with current `STATUS.md`; T01's obsolete digital-witness OPEN statement
is explicitly flagged for review. Previous STATUS text and the September 5
history are retained as **HISTORICAL / SUPERSEDED**. The unchanged dated JSON
registry and older overview/roadmap/source documents are historical snapshots,
not competing current-status authorities.

Use the labels **PROVED**, **CONDITIONAL**, **OPEN**, **FAILED**,
**EXPERIMENTAL**, **EXTERNAL RESULT**, and **HISTORICAL / SUPERSEDED**.
A failed certificate is not a disproof of its polynomial target; source proof
labels do not imply a new independent audit or external certification.

## Run locally

Use Python 3.10 or later. The experiment code uses only the standard library; no installation or network access is needed.

```bash
python3 -m experiments verify
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

Inspect the finite-field images of the original polynomials:

```bash
python3 -m experiments local-images --polynomial all --primes 2 3 5 7 --q 1
```

Compare them with an integral deformation, or inspect a same-set carrier:

```bash
python3 -m experiments local-images --polynomial baseline --primes 5 7 --q 35
python3 -m experiments carriers --polynomial mixed-cubic --carrier geometric --size 8 --base 3
```

Outputs are JSON with exact rational quantities. Finite enumeration verifies the listed finite cases; it does not prove an asymptotic theorem or construct a number-field tower. Collision energy gives a **lower** bound on image size and is used only as a diagnostic.

The initial experiment suite implements five benchmark polynomials. The two
distinct cubic targets T01 and T04 are specified in the history but are not yet
implemented in that suite.

## Repository layout

```text
docs/                  Research overview, roadmap, sources, reproduction guide
research/
  PROJECT_HISTORY.md   Reconciled state, shared progress, and retained chronology
  MECHANISM_LIBRARY.md Reusable results with hypotheses and costs
  FAILURE_LIBRARY.md   Scoped failures, including later C2/C3/C4 results
  OPEN_LEMMAS.md       Current obligations and historical alternatives
  MIGRATION_CONFLICTS.md Authority, source identities, and unresolved issues
  tracks/              Specifications, status records, and JSON track registry
  history-sources/     Recovered checkpoints and shared Phase A/B background
  conjectures/         Original proposed nonsingular-quadratic direction
  notes/               Original C1 review and corrections
  prompts/             Historical C0, C1, and C2 research assignments
  reports/             Supplied split-prime generalization report
  manifest.json        Sizes and SHA-256 hashes of the archived files
experiments/           Exact, dependency-free computational tools
examples/              Small reproducible output snapshots
tests/                 Mathematical and command-line regression checks
scripts/               Archive and documentation checks
.github/               Automated checks and contribution templates
```

The historical prompts are research artifacts, not instructions to a contributor or automated agent. Original files were copied without editing; 39 archived files have integrity hashes. Third-party reference PDFs and administrative documents are not distributed here.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Give mathematical claims explicit hypotheses and a status, preserve failed routes, and include exact commands for computations. Correct historical statements in a new note rather than silently changing the archived record.

No repository-wide license has been selected. See [LICENSE-NOTICE.md](LICENSE-NOTICE.md).
