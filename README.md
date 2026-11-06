# From Unit Distances and Sum–Product to Polynomial-Image Compression

**Huang Yixuan** · MA2288 undergraduate research, National University of Singapore

Supervised by **Prof. Tran Chieu Minh** · 5 November 2026

**[Read the academic report (PDF, 32 pages)](research/reports/2026-11-05-ma2288/MA2288-Polynomial-Image-Compression.pdf)** · [Download the PDF](https://github.com/hnt119/polynomial-image-compression/releases/download/ma2288-report-2026-11-05/MA2288-Polynomial-Image-Compression.pdf) · [One-page research summary](research/reports/2026-11-05-evidence-export/summary.pdf)

If a set contains $n$ numbers, it gives $n^2$ ordered pairs. How few distinct answers can a fixed polynomial give on those pairs? This project takes a construction from the study of unit distances and adapts its arithmetic to polynomial values. It proves a saving for an entire family of quadratics, including $(x+2y)^2+3x-y$. Four further polynomials remain open.

## Main result

For **every fixed integer quadruple** $(a,b,c,e)$, let $P(x,y)=(ax+by)^2+cx+ey$. There is a fixed $\varepsilon_P>0$ and a sequence of finite real sets $A_j$, with $|A_j|\to\infty$, such that

$$
|P(A_j,A_j)|\le |A_j|^{2-\varepsilon_P}.
$$

Both inputs use the same set, and the bound covers every ordered pair. The theorem includes zero coefficients. The extra condition $ab(ae-bc)\ne0$ identifies the nonspecial examples. Section 3.6 of the academic report separately extends the conclusion to fixed rational-coefficient quadratics whose homogeneous quadratic part has rank one. [Theorem 1 and proof](research/proofs/c0-v5/theorem-and-proof.tex) · [Corollary and normalization](research/EVIDENCE_INDEX.md#rational-corollary)

**How the construction works.** Choose algebraic integers whose real conjugates all lie in a fixed interval. One real embedding and a common rescaling turn them into the input set $A_j$. The number of distinct inputs grows exponentially with the field degree. At the selected split primes, the rescaled polynomial can take only square residues. Counting those classes and then packing the possible outputs inside each class gives the saving. Proposition 3.8 of *Planar Point Sets with Many Unit Distances* supplies the fields and split primes. [Counting argument](docs/release/2026-11-05/shared-quadratic.md) · [External field theorem](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf#page=12)

## Four open problems

| Track | Fixed polynomial | What is known |
|---|---|---|
| [T01](research/tracks/01-cubic-digital/STATUS.md) | $(x-y)^3+x+y$ | A saving would force almost every pair to share its exact output across many scales. A construction is missing. |
| [T02](research/tracks/02-quartic-hybrid/STATUS.md) | $(x+2y)^4+3x-y$ | An exact local count is known. The tested interval-packing bound loses the gain when all outputs are counted. |
| [T03](research/tracks/03-eisenstein-cartesianization/STATUS.md) | $x^2+xy+y^2$ | One family has quadratic-order image. A different construction supplies many symmetries, but how often they return pairs to the input square remains open. |
| [T04](research/tracks/04-cubic-slices/STATUS.md) | $(x-y)^3-3(x+y)$ | One recursion produces exponentially many distinct inputs. A power saving for its complete image remains open. |

The [restart record](research/OPEN_LEMMAS.md#restart) gives the precise missing estimate in each direction and distinguishes the separate affine quadratic benchmark.

## Read the evidence

- **For a research overview:** the [nine-page progress report](research/reports/2026-11-05-evidence-export/report.pdf) compares all four tracks. The [three-page quadratic brief](research/exports/2026-11-05-evidence/professor_brief.pdf) focuses on the successful construction and the full-rank obstacle.
- **To check a claim:** the [evidence index](research/EVIDENCE_INDEX.md) leads to the original proof, correction, or finite computation. The [citation inventory](docs/release/2026-11-07/report-citations.md) maps the academic report’s references to their exact destinations. One recorded T01 digital theorem still lacks its standalone proof.
- **To resume or cite the project:** see the [project map](research/CURRENT_PROJECT_MAP.md), [source gaps](research/MIGRATION_CONFLICTS.md), and [website handoff with permanent links](docs/WEBSITE_HANDOFF.md). The research record runs through 5 November 2026. The archive was packaged on 7 November.

## Reproduce the checks

From a full-history clone with Python 3.10 or later:

```sh
python3 scripts/check_repository.py
python3 scripts/check_evidence_release.py
python3 scripts/check_c0_snapshot.py
python3 scripts/check_quadratic_v6_references.py
python3 -m unittest discover -s tests -v
python3 -m experiments verify
```

These commands check published files, citations and finite examples. The asymptotic argument is in the proof linked above. [Reproduction and document builds](docs/reproducibility.md) · [Publication policy](docs/publishing.md) · [License notice](LICENSE-NOTICE.md)
