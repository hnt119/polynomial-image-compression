# Polynomial images on a Cartesian square

**Evidence export, 5 November 2026.** The [full report](report.pdf) gives the chronological T01 argument, dedicated sections for T02–T04, the separate shared quadratic result and an appendix of proof locators. The [one-page summary](summary.pdf) is its first page, compiled separately for distribution. All four fixed-polynomial targets remain open. The [central evidence index](../../EVIDENCE_INDEX.md) provides broader coverage and claim-level records.

The report reproduces the short MC-S1/S2 branching proof. It summarizes the other identified proofs and cites finite checks at their recorded ranges. It also distinguishes reported proofs with restricted underlying sources from publicly included arguments. This edition involved no new mathematical research, proof audit or exploratory experiment.

## Editable files

| File | Contents |
|---|---|
| [report.tex](report.tex), [summary.tex](summary.tex) | The two LaTeX entry points |
| [layout.tex](layout.tex), [one-page.tex](one-page.tex) | Typesetting and shared executive summary |
| [progress.tex](progress.tex) | September–October T01 development and the reproduced elementary proof |
| [other-tracks.tex](other-tracks.tex) | T02, T03, T04 and the November shared quadratic result |
| [evidence.tex](evidence.tex), [references.bib](references.bib) | Claim locators E1–E10 and bibliographic records for three identified internal reports |
| [figures/branching.tex](figures/branching.tex) | Coordinate-editable vector diagram of the eight-child occupancy bound |
| [build.sh](build.sh) | Build in a temporary directory |
| [SHA256SUMS](SHA256SUMS) | SHA-256 inventory of every file in this directory except the checksum file itself |

All equations and the schematic diagram are typeset from native source. No historical reference PDFs are embedded or included in this directory.

## Rebuild

From the export directory, with a POSIX shell, pdfLaTeX and BibTeX on the path, run

~~~sh
sh build.sh
shasum -a 256 -c SHA256SUMS
~~~

On systems with GNU coreutils, use `sha256sum -c SHA256SUMS` for the second command. The script makes three report passes with BibTeX after the first, then two summary passes. It checks the final logs before copying both PDFs back. It uses UTC and fixes the source date to 5 November 2026. Required LaTeX components are the standard article class, T1/Latin Modern fonts, geometry, amsmath, amssymb, array, booktabs, xcolor, url and hyperref. TeX distribution versions, fonts and package versions can affect the binary hashes.

## Checks on this edition

- Used pdfTeX 3.141592653-2.6-1.40.29 and BibTeX 0.99e from TeX Live 2026 (TinyTeX-1 release v2026.11). Compilation and a second build from a separate temporary source copy ran offline. Both output files compared byte-for-byte equal on this toolchain.
- Final compilation produced nine A4 pages in the report and one A4 page in the summary. Final-pass logs had no missing-character, unresolved-reference, package-warning or overfull-box diagnostics.
- Rendered each PDF using Poppler 26.05.0 at 110 dpi. Inspected all nine report pages and the separately rendered summary for formulas, running heads, tables, line breaks, source locators, the figure, missing glyphs and clipping. Checked the final edited pages again and compared unchanged page rasters.
- Extracted text and word bounds for both PDFs. No word rectangle crossed the page margins, no replacement characters or unresolved reference markers appeared, and the public text contained no local user paths.

Repository regressions and release-level verification are recorded separately at the [central evidence index](../../EVIDENCE_INDEX.md).
