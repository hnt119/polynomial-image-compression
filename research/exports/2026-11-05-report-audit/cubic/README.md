# Cubic evidence audit for the MA2288 v6 report

**Verdict, 5 November 2026.** Keep the mathematics in §4.4 and Appendix C.5, and retain bibliography key `ref17` with its existing permanent link. The published proofs support both minus-sign transfer bounds and the rich-fiber count. For the plus-sign digital theorem the report accurately gives the hypotheses and the recorded result. Its identified standalone proof was absent from the bounded recovery pass. Both unrestricted cubic targets remain **OPEN**. [Published evidence for reference 17](https://github.com/hnt119/polynomial-image-compression/blob/bd1f2d663262821575eebdfa559b7c25f76b46ab/research/exports/2026-11-05-report-references/README.md#ref17)

| Passage in v6 | Verdict and precise scope |
|---|---|
| §4.4, pp. 16–17. Bridge and witness | **PROVED.** The bridge uses P₂=(x−y)²+5(x+y) and P₋=(x−y)³−3(x+y). Its explicit pair example and the growth condition Q/8>√D agree with the proof. The totally real tower is an imported arithmetic input. |
| §4.4 and C.5, pp. 17, 25. Split primes | **PROVED.** On the centered Q/8 witness, all primes 5 mod 12 give exactly N² outputs. For all primes 1 mod 12, the specific quadratic certificate Θ<1 implies δ>0 and at least N²/(1+exp(−δd)) cubic outputs. N counts scalar inputs and d is field degree. |
| §4.4 and C.5, pp. 17, 25. One rich fiber | **PROVED.** Here N counts indices. There are 2N inputs and N ordered pairs attaining −12. Each of the other 4N²−N pairs gives its own output, for 4N²−N+1 outputs. Finite avoidance is sufficient for this count. The extra progression conditions establish properties of its historical field lift. |
| §4.4, p. 17 and [17], p. 28. Fixed-prime digits | **SOURCE-REPORTED PROVED; ORIGINAL PROOF NOT LOCATED IN CHECKED SOURCES.** The normalized-scalar identity and consequence were checked directly. The missing argument is Theorem A.2 for all sufficiently large integers smooth over one fixed finite prime set, with input size at least a fixed positive power. |
| Ref17, p. 28 | **Citation verified.** The original anchor and all five linked files resolve at the historical evidence commit. The native sources distinguish the two cubic signs and the evidence available for each. |
| Later T01 frontier | **PROVED necessary condition; EXPERIMENTAL finite census.** The optional editor note states the scope and separates the six stored examples from the analytic proof. |

Page numbers above are printed numbers. The corresponding PDF pages are 18–19, 27 and 30. The local comparison used the 30-page v6 PDF with SHA-256 `9d5ad8f21b86df90f3ff29cd24074bc7925d20f401fdee5a96dcf1ae966066cd`.

## Audit records

- [Proof checks](proof-checks.md) show the arithmetic estimates, finite exclusions, normalization and report comparison.
- [Claim-to-source map](claim-to-source.json) gives claim-level wording, conditions, dependencies, date, source hash, pinned section link and separate register identities. Equation labels in the native manuscripts and aliases assigned by the archive are distinguished.
- [Recovery record](source-recovery.md) identifies the exact missing file and bundle, the checked source classes and the bounds on the search.
- [Citation snippet](citation-snippets.tex) reproduces the verified existing entry for the editor. The only proposed shared edit is an [unapplied correction to the evidence index](proposed-index-note.patch) for a mistaken migration-register pointer.
- [Optional editor note](optional-frontier.md) treats MC-S1–S3, the six saved cases and the current limits separately from the report.
- [Verification](verification.md) records the checks and their scope.

## Publication and source identities

The reviewed remote was `hnt119/polynomial-image-compression`, default branch `main`, at `c689ab52ca3bb9e3221bd09ae9a083a3111e39df`. It matched the commissioning snapshot. The two original transfer manuscripts, the recovered 6 September rich-fiber proof, the two state excerpts, the October multiscale package and the bibliography were already present. The audit adds only the records in this directory. The supplied PDF was used locally.

The bibliography addition at `29a8f9fffcd6f4571eb408a0e7b85541bb5ffbca` cites the preceding source-support commit `bd1f2d663262821575eebdfa559b7c25f76b46ab`. The latter pin contains the source index and its five [17] destinations. The two transfer manuscripts are indexed by the **96-group** register under `T04/migration/T04-Q8-INERT` and `T04/migration/T04-Q8-SPLIT`. Their native equation labels are used in the audit map. The **75-claim** register uses `T04-RICH` and `T01-DIGITAL`; the 96-group register also records the digital theorem at `T01/2026-09-16-three-branch-lift/TB-S3` with its missing-proof grade. MC-S1–S3, MC-X1 and MC-O1 are indexed in the 96-group register and its 44-checkpoint catalogue. Each register keeps its own identifiers and counting convention. [96-group ledger](https://github.com/hnt119/polynomial-image-compression/blob/c689ab52ca3bb9e3221bd09ae9a083a3111e39df/research/evidence/2026-11-05/claim-ledger.json) · [75-claim register](https://github.com/hnt119/polynomial-image-compression/blob/c689ab52ca3bb9e3221bd09ae9a083a3111e39df/research/exports/2026-11-05-evidence/evidence_register.json) · [Checkpoint catalogue](https://github.com/hnt119/polynomial-image-compression/blob/c689ab52ca3bb9e3221bd09ae9a083a3111e39df/research/evidence/2026-11-05/checkpoints.json)
