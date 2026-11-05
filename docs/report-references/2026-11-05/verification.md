# Citation edition verification — 5 November 2026

This is documentary verification, not a mathematical proof audit, new experiment,
external review or literature search. The personal v6 report was read for its
bibliography and was not edited or uploaded.

## Source identity and citation checks

- Archive PR #1 was merged as `3973f97457902cb3954c417fa264d67d47cd8daa` after its unchanged head and successful CI were checked.
- The native supplement is commit `145d0e5a6ff725ab13cbb5c696bf335352e6f4a1`: 24 mathematical source files or explicit excerpts, plus a reading guide and manifest. Payload: 6,464,266 bytes.
- A source worker and an independent reviewer matched the copied originals, inspected ZIP members and section excerpts to their retained sources. The public [manifest](../../../research/report-source-supplement/manifest.json) records original and copied hashes. All 24 public hashes were independently checked.
- The citation map has 13 reference groups and 38 distinct source paths. Every path and recorded hash was checked against the **committed Git blob**, as well as its working copy. The TeX links include the supplement's certificate index as an additional destination.
- All 21 bibliography keys and their order were retained. The eight external entries were compared to the supplied text and are unchanged. The 13 project entries agree between the complete and project-only variants. No external paper was retrieved or newly verified.
- T01/T04 polynomial signs, the September/November C0 scopes, historical internal review dates and finite/asymptotic distinctions received an independent documentary check. The T01 digital standalone proof remains **MISSING SOURCE / PROVENANCE FILE**.
- Sensitive-content checks found no personal filesystem paths, credentials, private chat identifiers or correspondence in the new source supplement. The original 39-file archive, license, specifications and historical proofs were not modified.

## Checks run for this supplement

| Check | Result and scope |
|---|---|
| `python3 -m unittest discover -s tests -v` | 100 tests passed; existing regressions only |
| `python3 -m experiments verify` | 159 finite benchmark checks passed; no exploratory grids |
| `python3 scripts/check_repository.py` | Original 39 archive hashes and current local Markdown links passed |
| `python3 scripts/check_evidence_release.py` | Existing 96 claims, 44 checkpoints, 970 locators, 29 portable-copy hashes, 533 saved ordered pairs and 13 export hashes passed |
| `python3 scripts/check_codex_setup.py` in the source checkout | 50 local references and 43 T03 archive manifest entries passed; private references are not in a public clone |
| Native supplement/source-map checks | All 24 source hashes and 38 pinned source blobs passed |
| `git diff --check` for the citation/navigation edits | Passed |
| `git show --check 145d0e5` | Five inherited blank-at-EOF notices in exact section excerpts, deliberately preserved to retain copied bytes |

The five preserved notices are in the adaptive state, November C0 theorem,
T01 digital state, T04 state and norm-transfer excerpts. They affect whitespace,
not source text or mathematical status. No source was rewritten to silence them.
The inherited dirty primary checkout and the parallel publication branch were
not staged, reset or merged by this citation task.

## LaTeX integration check

The full bibliography was compiled offline using the already available
pdfTeX 1.40.29 toolchain in a minimal A4 article with `amsmath`, `amssymb`,
`hyperref` and Latin Modern fonts. The report's `sec:quadratic` label was supplied
as section 3 in the test harness. No dependencies were installed.

The initial harness lacked an available T1 bitmap font; selecting the existing
Latin Modern package corrected that harness issue. The final compile had no
undefined references, missing-character messages or overfull boxes. Both pages
were rendered with Poppler and visually inspected. Their 39 distinct URI links
include all 31 expected permanent GitHub destinations. The original report's
pagination was not tested, because its PDF was not rebuilt.

The temporary integration PDF and build logs remain local. The delivered files
are editable TeX snippets and the public source/citation ledger. Importing the
snippet into the actual report still requires the report's normal LaTeX build.
