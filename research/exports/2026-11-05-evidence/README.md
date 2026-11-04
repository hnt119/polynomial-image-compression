# Polynomial image compression • 5 November 2026 evidence snapshot

**C0 is proved. The full-rank problem is open.** For every fixed integer quadruple, the polynomial $(ax+by)^2+cx+ey$ has a fixed power saving on arbitrarily large same-set real Cartesian squares. Its quadratic part is a square or zero. The positive-definite form $Q=x^2+xy+y^2$ lies outside this theorem. No new construction, proof search or numerical sweep was undertaken for this snapshot.

## Read or present

| Audience | Print | Editable source |
|---|---|---|
| Professor brief | [Brief PDF](professor_brief.pdf) | [Word with native equations](professor_brief.docx) · [Markdown](professor_brief.md) · [LaTeX](professor_brief.tex) |
| Mathematical detail | [Technical PDF](research_report.pdf) | [Markdown](research_report.md) · [LaTeX](research_report.tex) · [bibliography](references.bib) |

For a first reading, go from the C0 theorem to the balanced-factor retirement and then to the last section of the brief: the occupied-label estimate is the exact remaining question for the mixed-signature unit approach.

## Trace a statement

- [Claim register (CSV)](evidence_register.csv) · [same register (JSON)](evidence_register.json) · [current mathematical state](state.json). The register distinguishes the source's mathematical status, historical review, finite computations and documentary checks in this release.
- [Recovered primary proof sources](../../proofs/README.md) and [T03 status with dated addenda](../../tracks/03-eisenstein-cartesianization/STATUS.md). The individual dated proof packages remain at their research/notes locations, with scripts in experiments and tables in examples or in their original note directories.
- [Publication inventory](publication_inventory.csv) records the original and public-byte identities of the included historical material. [Checksums](checksums.sha256) cover the actual public source files and all export artifacts, excluding the checksum list itself. [Verification record](verification.md) describes what was and was not checked.

## Scope, corrections and availability

1. **C0.** The September correction establishes a transverse rank-one family. Its original hypotheses remain in that document. [November Theorem 1](../../proofs/c0-v5/theorem-and-proof.tex) establishes the bound for every fixed integral quadruple; the nonvanishing condition identifies nonspecial examples. The tower input is the cited external field-supply theorem, not an external certification of the project's proof.
2. **From orbits to actual fibers.** A selected-action failure does not imply a quadratic-sized image. In contrast the [balanced-factor proof](../../notes/2026-10-11-bff-o1/README.md) proves an actual image of order $n^2$ for its particular carrier. No full-rank impossibility follows.
3. **Mixed signature.** [MS-O1](../../notes/2026-10-21-relative-unit-population/README.md) supplies at least $2^{d_j}$ order units at a single fixed cutoff. [MS-O2](../../notes/2026-10-21-typical-unit-returns/incidences.md) counts the nonzero order-unit orbit intersections by their *joint* labels: principal ideal of the actual order, and exact relative-norm element. Several labels can have the same output. The exponential decrease of the number of occupied labels relative to the number of ordered nonzero pairs (**MS-O2-I**) remains open.
4. **Availability.** The C0 ledgers, T01 norm–trace program/data, and the [T04 rich-fiber proof](../../proofs/source-recovery/rich_fiber_results_checkpoint.md) are now available. The T01 fixed-prime digital proof is **MISSING SOURCE** in the inspected intake. Its source-reported status is retained. Independent reproduction of external theorems and a literature review were outside this task. All four fixed T01–T04 targets remain separate; the cubic and quartic status files were not overwritten.
5. **Public copies.** Exact archived mathematics and finite numbers are preserved. When a historic file contains a personal absolute locator, only that locator was removed or made relative in the public copy; its local original was not modified. Unchanged historical hash lists describe original runs and are not regenerated. Use this release's checksums for public bytes. Selected T03 register sections and dated navigation are identified as such. References to local-only runs in historical prose document provenance; they are not public download links.
6. **Excluded.** No private correspondence, attachment contents, course-report front matter, private Overleaf index, raw chats, personal paths, new third-party papers, standalone font files, environment files, build caches, or bulk raw runs are published. Large BFF distributions stay local; the [complete pair-weighted and output histograms](../../notes/2026-10-11-balanced-full-fibers/data.json), input tables and original scout code are included. The project's dated September PDF is retained at its canonical path as a historical checkpoint.

## Build and verify

Run from the repository root. Use Python 3.10+ with python-docx, lxml and ReportLab, Poppler’s pdftoppm, and either XeLaTeX (article, amsmath, newtx and the listed preamble packages installed) or Tectonic with an already populated bundle. Set TECTONIC and TECTONIC_CACHE_DIR if the binary/cache are not discovered automatically. No fonts are distributed. Canonical narrative inputs are the two Markdown files. The build creates the native formats from those inputs using installed local dependencies; see the build script for its CLI and the verification record for the toolchain used. No package installation or research sweep is part of the build.

```sh
python3 research/exports/2026-11-05-evidence/verify_snapshot.py
shasum -a 256 -c research/exports/2026-11-05-evidence/checksums.sha256
python3 research/exports/2026-11-05-evidence/build.py
```

Verify the distributed bytes before rebuilding. A different local typesetter or document metadata timestamp can change binary hashes without changing the mathematics.
