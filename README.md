# From unit distances to polynomial image compression

Huang Yixuan’s MA2288 research project at the National University of Singapore, supervised by Prof. Tran Chieu Minh. The starting point was a construction of planar sets with many unit distances. Here the question is how often different real input pairs can give the same polynomial value.

**Start with the [nine-page public progress report](research/reports/2026-11-05-evidence-export/report.pdf)** or its [one-page professor summary](research/reports/2026-11-05-evidence-export/summary.pdf). Then use the [evidence index](research/EVIDENCE_INDEX.md) to reach the original argument, correction or finite computation. The [website handoff](docs/WEBSITE_HANDOFF.md) gives permanent links and identifies the separate academic edition.

## Question and positive result

For a fixed polynomial $P$, find a fixed $\varepsilon_P>0$ and finite real sets $A_j$, with $|A_j|\to\infty$, such that

$$
|P(A_j,A_j)|\le |A_j|^{2-\varepsilon_P}.
$$

The same set supplies both coordinates. The count includes every ordered pair. The exponent can depend on $P$ and is fixed as the sets grow.

**PROVED in the project sources.** This holds for $P(x,y)=(ax+by)^2+cx+ey$ for **every fixed integer quadruple**, including zero coefficients. The additional condition $ab(ae-bc)\ne0$ identifies the nonspecial subfamily. The restricted 3 September statement and the broader November theorem have separate [proofs and corrections](research/exports/2026-11-05-report-references/README.md#ref10).

**The real set.** In a totally real number field $F_j$ of degree $d_j$, take all algebraic integers whose real conjugates have magnitude at most a fixed $X$. Project this box through one embedding into $\mathbb R$ and divide every scalar by the same fixed product $R$ of split primes. Proposition 3.8 of *Planar Point Sets with Many Unit Distances* supplies the fields and primes together. [External field theorem](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf#page=12)

**Why it works.** The box contains exponentially many distinct scalars. Before the common rescaling, the auxiliary polynomial is $(ax+by)^2+R(cx+ey)$. Modulo each selected prime its outputs must be squares. Counting square classes at all $d_j$ primes above each selected rational prime, then packing each class in the box of real embeddings, gives at most $\theta^{d_j}|A_j|^2$ values for a fixed $\theta<1$. The matching upper input bound converts this into the fixed exponent above. [Complete project proof, Theorem 1](research/proofs/c0-v5/theorem-and-proof.tex) · [Parameter choices and counts](docs/release/2026-11-05/shared-quadratic.md)

## Four open targets

| Track | Fixed polynomial | What the evidence establishes |
|---|---|---|
| [T01](research/tracks/01-cubic-digital/STATUS.md) | $(x-y)^3+x+y$ | **OPEN.** A saving would force almost every pair to share its exact output across many scales. A construction with that property is missing. |
| [T02](research/tracks/02-quartic-hybrid/STATUS.md) | $(x+2y)^4+3x-y$ | **OPEN.** The ramified local count is exact. The specified full-interval packing pays back the local gain. |
| [T03](research/tracks/03-eisenstein-cartesianization/STATUS.md) | $x^2+xy+y^2$ | **OPEN.** One balanced-factor family has image of order $n^2$. A different tower has at least $2^{d_j}$ eligible units. A bound on how many return typical pairs is missing. |
| [T04](research/tracks/04-cubic-slices/STATUS.md) | $(x-y)^3-3(x+y)$ | **OPEN.** A complementary-unit recursion produces exponentially many distinct inputs. A strictly smaller rate for its full output than twice its input rate is missing. |

The separate affine quadratic $x^2+xy+y^2+x$ has a proved transfer implication whose simultaneous hypotheses remain open. Individual rich fibers, collision energy and finite examples can guide a search. An upper bound for the complete image requires accounting for all pairs. See the [restart record](research/OPEN_LEMMAS.md#restart) for the exact obligations, failed cases and missing sources.

## Reading and reproduction

- **Public reports, 5 November 2026.** The [four-track report package](research/reports/2026-11-05-evidence-export/README.md) is the primary reading path. The [C0/T03 technical report and three-page professor brief](research/exports/2026-11-05-evidence/README.md) give the detailed quadratic account with editable sources and figures. Compile a disposable copy using the commands in the respective package.
- **Academic report.** The author’s private 32-page *From Unit Distances and Sum–Product to Polynomial-Image Compression* is the 5 November submission-prepared edition after v8. Its [citation inventory and preservation checks](docs/release/2026-11-07/report-citations.md) identify the exact public destinations. The academic PDF and editable submission materials are retained locally.
- **Evidence.** The [claim ledger and checkpoint catalogue](research/evidence/2026-11-05/README.md) point to proof sections, corrections, code and saved data. The [project map](research/CURRENT_PROJECT_MAP.md), [history](research/PROJECT_HISTORY.md) and [source-gap register](research/MIGRATION_CONFLICTS.md) explain chronology and availability. The T01 fixed-prime digital theorem is source-reported proved; its standalone proof remains unavailable.
- **Dates.** The September migration records have a 10 September cutoff. The latest active T01/T03 mechanism checkpoints are 21 October. The public research record through 5 November includes the 3 November shared proof and its 4 November audit. Packaging pass: 7 November 2026.

From a full-history clone with Python 3.10+:

```sh
python3 scripts/check_repository.py
python3 scripts/check_evidence_release.py
python3 scripts/check_c0_snapshot.py
python3 scripts/check_quadratic_v6_references.py
python3 -m unittest discover -s tests -v
python3 -m experiments verify
```

The first four commands check archive integrity, source locators and citations. The last two run finite regressions. Mathematical verification requires reading the proofs and checking their hypotheses, including the imported field supply. [Reproduction guide](docs/reproducibility.md) · [Public/private retention policy](docs/publishing.md) · [Contributing](CONTRIBUTING.md) · [License notice](LICENSE-NOTICE.md)
