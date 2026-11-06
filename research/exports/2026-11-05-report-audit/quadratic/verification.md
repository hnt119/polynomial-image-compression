# Verification record and source availability

5 November 2026. The isolated branch started at the fetched remote `main` commit `c689ab52ca3bb9e3221bd09ae9a083a3111e39df`. A second remote read before publication returned the same revision. The input was the original v6 PDF identified on the [audit cover](README.md). Its local TeX was used to disambiguate formulas. Rendered-page inspection determined the cutoff, the radical cardinality bars and the reference ranges. The academic PDF and front matter were read locally.

## Evidence versions

| Existing revision | Role in this comparison |
|---|---|
| `3973f97457902cb3954c417fa264d67d47cd8daa` | Four-track release. Its 96 claim groups and 44 checkpoints include the later scoped quartic and T03 statuses. |
| `87586fe555938cb5358307c0d3857cad9b4193ce` | C0/T03 release and 75-claim register. The integrated manifest on the review base verifies the public bytes. |
| `bd1f2d663262821575eebdfa559b7c25f76b46ab` | Source-support commit used by the thirteen existing GitHub bibliography links. This is the revision against which their headings and child files were checked. |
| `29a8f9fffcd6f4571eb408a0e7b85541bb5ffbca` | The linked bibliography with all 21 original keys. |
| `3aa1e299b213f16a45ee8c49fd2e7aeaeb388ece` and `c689ab52ca3bb9e3221bd09ae9a083a3111e39df` | Reconciliation and publication merge. The 26 historical overlap dispositions remain documented in the earlier release. |

**What was checked now.** The C0 comparison followed the complete counting derivation, extreme coefficient cases and the field proposition. The norm and unit comparison re-derived the shifts, counting factors, cutoff, population lower bound and reciprocal-orbit identity. The BFF comparison followed the all-target specialization, exception bound and support conversion. For radicals, signed-branch equations and the recurrence were checked algebraically and the saved candidate ledgers regrouped; their solvers were not rerun. The quartic comparison rechecked the mixed-characteristic ring, digit expansion, complete local support, both input costs, global carrier, extrema and sign of the specified upper bound. The four topic notes identify the checked dependencies, source labels and finite ranges. These are bounded comparisons and elementary consistency checks. Neither earlier review acceptance nor passing software tests supplies a new asymptotic theorem.

**Available originals and imported inputs.** The original manuscript for the field supply was available locally, SHA-256 `62b5de8cacdfbc0f13ae1940aa81659cd233e6945b936612fbeab0ab8ab3d383`. Proposition 3.8 (P1)–(P4) was checked against the C0 proof. Its upstream existence proof remains an external input. The September C0 record, November proof excerpt, related internal audit, norm-transfer text, field/unit/return companions, balanced-factor algebra and specialization, exact radical records, C2 corrigenda, C3 extrema, C4 argument and scoped review were available. The 13 original/public identities in the citation supplement were matched to local originals (12 whole copies and one dated excerpt). No third-party work was redistributed.

**Limits.** The archive contains the frozen Phase A reproduction and change log, while its separately named source-audit PDF has no located public proof file in this intake. The reported standalone T03 finite-field $\mathbb F_{25}$ certificate is a separate availability gap. It does not enter the five radical image counts or the RC15/4 implication. The T01/T04 semantic audit and any revision of [17] belong to the cubic agent. The 21-key check includes [17] solely for structural link and provenance integrity. The [cubic owner’s published fragment](https://github.com/hnt119/polynomial-image-compression/blob/1ebe48fa718b8dbd8b4cbed544daf98854d5f5f7/research/exports/2026-11-05-report-audit/cubic/citation-snippets.tex) at `1ebe48fa718b8dbd8b4cbed544daf98854d5f5f7` was compared with the existing [17] entry. Their entry text matches. The two proposed index patches were applied successfully in sequence to disposable copies of the shared files. No combined edit was applied to either branch.

## Offline validation

| Command on the separate audit checkout | Result |
|---|---|
| `python3 -m unittest discover -s tests -p test_quadratic_v6_references.py -v` | Seven targeted tests passed. Negative controls cover changed/missing origins, wrong headings or pins, a missing anchor, a section with no evidence link, and a historical destination that exists only in the later checkout. |
| `python3 scripts/check_quadratic_v6_references.py` | All 21 ordered keys and thirteen existing GitHub citations passed. The index has 47 relative file links at the source pin and 48 in the current version. All thirteen provenance rows passed in each tree. The checker reads Git blobs by full SHA and operates without HTTP. |
| `python3 -m unittest discover -s tests -v` | 107 tests passed, comprising the existing 100 and the seven new regression tests. |
| `python3 -m experiments verify` | 159 standard finite checks passed. No archived research sweep ran. |
| `python3 scripts/check_repository.py` | Verified the original 39-file archive manifest and Markdown destinations. |
| `python3 scripts/check_evidence_release.py` | 96 structured claims, 44 checkpoints, 970 section locators, 29 portable-copy hashes, 533 saved ordered-pair entries and 13 export hashes passed. |
| `python3 research/exports/2026-11-05-evidence/verify_snapshot.py` | 267 distributed SHA-256 matches, identical 75-row CSV/JSON registers, 85 distinct source paths and 48 editable Word equations. |
| `shasum -a 256 -c research/exports/2026-11-05-report-references/checksums.sha256` | All 18 published citation-supplement files passed. |
| `git apply --check research/exports/2026-11-05-report-audit/quadratic/integration.patch` | Proposed integration patch applies to the reviewed base. It was left unapplied. |
| `git diff --check` and `git diff --cached --check` | Passed. The staged review contained only new audit, checker and test files. |

The source workspace's separate `python3 scripts/check_codex_setup.py` also verified 50 retained local reference files and 43 T03 manifest members. This check uses private reference material. Python 3.12.7 was used for the local public checks. The dated snapshots, their manifests, prior bibliography and report outputs retain their original bytes on this branch.

## CI and integration

At the reviewed base `.github/workflows/checks.yml` runs the general unit suite, `experiments verify`, `check_repository.py` and `check_evidence_release.py`. The general checker reads the 39-file archive and checks Markdown paths. The four-track checker consumes its own JSON ledgers and report export. Neither it nor the original tests invoke `verify_snapshot.py` or resolve the bibliography at historical Git commits. The new tests use isolated Git fixtures and do not substitute for checking the real release. The [proposed patch](integration.patch) calls both separate checks, fetches the ancestry for historical reads, and adds an entry to the shared evidence index. Run both agents' checks again on the eventual combined tree. The bibliography checker establishes paths, anchors and identities. Mathematical attribution and proof scope require the manual comparisons recorded here.
