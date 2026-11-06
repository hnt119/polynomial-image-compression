# Verification record

**Scope and inputs.** On 5 November 2026 the remote default branch was `main` and its head was `c689ab52ca3bb9e3221bd09ae9a083a3111e39df`, equal to the supplied baseline. The audit started at that commit in its own worktree on `codex/cubic-v6-evidence-audit`. The comparison document was the supplied local v6, SHA-256 `9d5ad8f21b86df90f3ff29cd24074bc7925d20f401fdee5a96dcf1ae966066cd`. Printed pp. 16–17, 25 and 28 correspond to PDF pp. 18–19, 27 and 30. We read the report text directly and checked the typeset C.5 formulas on its rendered page.

**Work performed.** The transfer and rich-fiber reviewers read the full relevant source arguments and compared the steps with v6. The lead checked the signs, witness, numerical factors, energy-to-image direction, induction, coverage, report locators and status distinctions. A separate bounded search checked the T01 original's availability. The lead and a second reader checked the later graph, finite prefix-tree and local capacity proofs. These are internal checks of these particular arguments. The unramified tower construction, field-supply theorems and standard arithmetic inputs were taken under the hypotheses stated in the cited proofs.

## Published citation chain

The published bibliography at the reviewed head has 21 entries. Its `ref17` link uses the earlier source-support commit `bd1f2d663262821575eebdfa559b7c25f76b46ab`. We read the bibliography entry, opened the committed Markdown blob at that precise revision, located its `## ref17` heading and resolved relative paths from the index directory inside that same tree. All 47 relative file links plus the in-page heading link in that revision of the index resolved. The five file links in [17] lead to the following exact evidence. [Ref17 at its actual pin](https://github.com/hnt119/polynomial-image-compression/blob/bd1f2d663262821575eebdfa559b7c25f76b46ab/research/exports/2026-11-05-report-references/README.md#L59-L63)

| Pinned source | Confirmed section |
|---|---|
| [T01 state excerpt](https://github.com/hnt119/polynomial-image-compression/blob/bd1f2d663262821575eebdfa559b7c25f76b46ab/research/proofs/source-recovery/T01-state-digital-theorems.md#L14-L30) | §4.3, (T01.6) and the retained proof ingredients |
| [T04 state excerpt](https://github.com/hnt119/polynomial-image-compression/blob/bd1f2d663262821575eebdfa559b7c25f76b46ab/research/proofs/source-recovery/T04-state-transfer-rich-fiber.md#L5-L57) | §4.5 on transfer and §4.7 on rich-fiber counting |
| [First transfer proof](https://github.com/hnt119/polynomial-image-compression/blob/bd1f2d663262821575eebdfa559b7c25f76b46ab/research/history-sources/quadratic_to_cubic_transfer_checkpoint.md#L498-L546) | §D.3, including (D.7) |
| [Complementary transfer proof](https://github.com/hnt119/polynomial-image-compression/blob/bd1f2d663262821575eebdfa559b7c25f76b46ab/research/history-sources/complementary_prime_transfer_obstruction.md#L37-L647) | §§B–F, main theorem, (D.1), energy §E and positivity §F |
| [Rich-fiber proof](https://github.com/hnt119/polynomial-image-compression/blob/bd1f2d663262821575eebdfa559b7c25f76b46ab/research/proofs/source-recovery/rich_fiber_results_checkpoint.md#L102-L245) | §§B–C, especially B.1, B.2 and Theorem 3 at lines 223–235 |

The evidence release, source-support package, bibliography commit and publication reconciliation are ancestors of the reviewed head. The source excerpts were checked against their provenance records. The two native transfer files and the recovered native rich-fiber file are already public. Their exact bytes and proof locators are identified in the claim map. The digital recovery record gives hashes of located witnesses separately from the expected hash of the absent proof.

The final structured map contains 15 report and citation entries and five separately marked optional frontier entries. All 39 primary and secondary locators matched their committed source hashes and line bounds across 12 pinned source versions. An independent final reading checked all 60 distinct GitHub URLs across the eight deliverables.

## Local checks and execution limits

Python 3.12.7. The following commands ran from the isolated checkout. Each completed with exit status 0. The command line in the last row is a read-only applicability check on the proposed shared-index note.

| Command | Result |
|---|---|
| `python3 -m unittest discover -s tests -v` | 100 existing tests passed |
| `python3 -m experiments verify` | 159 finite regression checks passed |
| `python3 scripts/check_repository.py` | Original 39 archive hashes and links in 303 Markdown files passed |
| `python3 scripts/check_evidence_release.py` | 96 structured groups, 44 checkpoints, 970 source sections, 29 portable-copy hashes, 533 saved ordered-pair entries and 13 export hashes passed |
| `python3 research/exports/2026-11-05-evidence/verify_snapshot.py` | 267 hashes, 75 matching CSV/JSON claims, 85 distinct claim-source paths and 48 editable Word equations passed |
| `git diff --check` and `git diff --cached --check` | Working and staged whitespace checks passed |
| `git apply --check research/exports/2026-11-05-report-audit/cubic/proposed-index-note.patch` | Proposed one-paragraph index addendum applies to the reviewed snapshot. It is supplied for coordinated integration. |

Separately, in the source checkout with its private references, `python3 scripts/check_codex_setup.py` passed 50 local reference hashes, 43 T03 member records and the related setup identity checks.

**Table integrity versus recomputation.** The checker reads the saved six-set referee table. For each case it verifies the number, range and uniqueness of the ordered pair indices, the fiber-size histogram and the number of output records. All six stored sizes and histograms agree with the published summary. No MC evaluator, digital scout, polynomial search, arithmetic tower, or T04 depth-30 computation was executed for this audit. The existing unit and finite benchmark suites above were run separately. [Source of the table check](https://github.com/hnt119/polynomial-image-compression/blob/c689ab52ca3bb9e3221bd09ae9a083a3111e39df/scripts/check_evidence_release.py#L74-L87)

GitHub's checks for the pushed review head are reported in the PR and final handoff. The public audit contains first-party mathematical notes, locators and hashes. The PDF, private source bundles and local execution logs stay in the local workspace.
