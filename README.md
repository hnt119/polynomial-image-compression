# Polynomial Image Compression

> **5 November 2026 evidence snapshot.** Start with the [professor brief, technical report and proof register](research/exports/2026-11-05-evidence/README.md). The latest square-plus-linear theorem covers every fixed integer quadruple. The full-rank quadratic remains open. Earlier status descriptions below record the original archive.


Research notes and reproducible experiments on small polynomial image sets, motivated by unit-distance constructions, sum-product methods, and the Elekes–Rónyai problem.

The central question is whether a **fixed** polynomial $P\in\mathbb R[x,y]$, depending on both variables, admits a **fixed** $\varepsilon>0$ and arbitrarily large finite sets $A\subset\mathbb R$ such that

$$
|P(A,A)|\le |A|^{2-\varepsilon}.
$$

The same set occurs in both inputs. The exponent may depend on the fixed polynomial, but cannot change with the size of the set.

## Start here

- [Project history: four tracks](research/PROJECT_HISTORY.md): recent results, closed routes, and current directions.
- [Track specifications and status](research/tracks/README.md): one precise target and continuation record per track.
- [Research overview](docs/research-overview.md): questions, mechanisms, and mathematical status.
- [Roadmap](docs/roadmap.md): concrete next steps and unresolved dependencies.
- [Source record](docs/sources.md): archived materials, provenance, and missing reports.
- [Reproduce the experiments](docs/reproducibility.md): exact finite computations and their limits.
- [Publish to GitHub](docs/publishing.md): remaining setup for this prepared local repository.

## Research status

This repository organizes a work in progress. It does not announce a new proof or establish external novelty.

| Track | Polynomial | Recent direction and status |
| --- | --- | --- |
| T01 | $(x-y)^3+x+y$ | Exact digital carries after the positive-volume block obstruction; open |
| T02 | $(x+2y)^4+3x-y$ | Hybrid unit/additive carrier and a realized-support lemma; open |
| T03 | $x^2+xy+y^2$ | Parity-twisted norm code and global deficit contraction; open |
| T04 | $(x-y)^3-3(x+y)$ | Direct overlapping slices after two specified quadratic-transfer obstructions; open |

The earlier rank-one quadratic family $(ax+by)^2+cx+ey$ is reported as established
for integral coefficients with $\gcd(a,b)=1$ and $ab(ae-bc)\ne0$. Its original C0
report has been recovered; the complete corrected C0 proof remains missing.
The baseline $(x-y)^2+x+y$ and adversarial mixed cubic $xy(x+y)$ remain benchmarks.

The [C1 review](research/notes/Phase_C1_Review_and_Next_Steps.md) contains two short corrections to the earlier roadmap. A failure of an upper-bound method is not a disproof of compression for the polynomial.

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
  PROJECT_HISTORY.md   Four-track history and current mathematical directions
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
