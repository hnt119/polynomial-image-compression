# Public evidence edition · 5 November 2026

The [evidence index](../../../research/EVIDENCE_INDEX.md), [structured claim ledger](../../../research/evidence/2026-11-05/claim-ledger.json), and [LaTeX/PDF edition](../../../research/reports/2026-11-05-evidence-export/README.md) are reading and verification tools for existing results. No exploratory grid, extension search, or mathematical proof audit was commissioned. Historical labels refer to the proof and verification record at the cited checkpoint; this release checked the archive.

## Publication inventory

The source checkout began with 79 tracked files (nine modified), no staged changes, and 441 untracked files. Upstream `main` shared the same 73 non-dotfile entries as the historical local commit but had a different root. The new branch starts from upstream. Its inherited selection comprised 377 paths: nine tracked modifications, six repository dotfiles previously absent upstream, and 362 reviewed untracked files. The latter comprise 324 native files without flagged provenance, 29 portable derivatives, and eight project-produced research PDFs plus one cover preview. Neither the old local branch nor the upstream history was rewritten.

| Disposition | What readers can check |
|---|---|
| Native research | Markdown proof and review companions, source identities, arithmetic certificates, editable experiment/test modules, and portable JSON evidence. For example, the marked-shift arithmetic argument and its independent check are preserved; the multiscale oracle contains all 533 pair outputs; the T01 transfer/division checkpoint retains its five Bézout certificates. |
| Historical exports | Eight first-party PDFs (129 pages in total) and one existing mathematical cover preview. These are retained historical renderings, screened for paths/metadata/attachments; the newly created PDFs receive their own page-by-page visual check. No third-party papers were added. |
| Public derivatives | [29 records](portable-derivatives.json) give both original and public SHA-256 identities. In nine JSON files a command or source path is made repository-relative. In twenty Markdown files a private commissioning-attachment locator or identifier is withheld. Each edit affects exactly one provenance line; no substantive data or proof line changes. Historical manifests still refer to the original bytes, not to sanitized publications. |
| Original archive | All 39 size/SHA-256 entries in [the 5 September manifest](../../../research/manifest.json), the four original track specifications, and the license notice are unchanged. The [separate 50-file local inventory](../../../research/CODEX_SOURCE_MANIFEST.json) identifies restricted local reference files, not 50 distributed files. |
| Local only — deliberately withheld | Of the 441 originally untracked files, 79 were excluded: 70 academic submission/editing artifacts, three associated personal PDFs, two academic review/defense notes, and four internal source-recovery prompts. All remain in the source checkout. The [math-only shared C0 digest](shared-quadratic.md) retains the November all-coefficient theorem separately from its personal report packaging. Ignored raw research runs, third-party reference PDFs, private import manifests, correspondence, caches and rendering intermediates also stay outside Git. |
| MISSING SOURCE / PROVENANCE FILE | The Raz–Zahl theorem and energy-dispersion text cited by the multiscale task were not located; no exponent from them is imported. The eight received recovery notes do not supply the larger packages they describe. The T03 standalone F25 verification and T04 depth-30 numeric execution certificate are not claimed recovered. See [migration conflicts MC-02–06](../../../research/MIGRATION_CONFLICTS.md) for precisely which sources are absent, restricted, or only reported. |

The retention list identifies classes without publishing private filenames. The initial working tree, private sources, raw run archives and original hashes are preserved. Public clean-clone verification does not rely on these files. Reference-only historical links in hash-frozen sources identify their original contexts.

## Verification procedure

Run the public checks from the repository root with Python 3.10 or later:

```sh
python3 -m unittest discover -s tests -v
python3 -m experiments verify
python3 scripts/check_repository.py
python3 scripts/check_evidence_release.py
```

The local source owner can additionally run `python3 scripts/check_codex_setup.py` with the private migration bundle in its original relative location. Its 50 reference identities, 43 T03 ZIP member records/CRC and duplicate-state checks passed during packaging. The existing unit suite and baseline verifier passed on the isolated publication tree: **100 tests and 159 finite checks**. Those checks concern finite implementations, not any open research target. For PDF build commands and visual verification, see the [export README](../../../research/reports/2026-11-05-evidence-export/README.md).

GitHub Actions results belong to the pushed commit/PR, not to this local verification record. No new experiment or review acceptance changes a theorem's status.

**Whitespace and source identity.** The archival import's staged whitespace check reported seven historical whitespace warnings in six files: four trailing blank lines at end of file, two TeX alignment spaces, and one Markdown hard break. Every flagged blob matched the original source byte for byte. They have been preserved so existing evidence hashes still identify the originals. The separate publication-authored documentation and export are checked independently. No whitespace rule or CI protection was disabled.

The final machine ledger contains 96 quantified claim groups across 44 dated checkpoints. The release checker resolves 876 statement/proof sections and 94 source-register sections, verifies the 29 portable-copy hashes and 13 export-file hashes, and checks that all 533 ordered pairs occur exactly once in the six saved multiscale fiber tables. These checks establish correspondence and coverage of the published records; they do not evaluate the polynomial again. The nine-page report and one-page summary were compiled, rendered, individually inspected and reproduced byte-for-byte using the recorded TeX toolchain.
