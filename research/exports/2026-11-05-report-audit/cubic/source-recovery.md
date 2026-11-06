# T01 fixed-prime digital proof recovery · 5 November 2026

**SOURCE-REPORTED PROVED; ORIGINAL PROOF NOT LOCATED IN CHECKED SOURCES.** The 10 September T01 state gives the theorem, its constants and two intermediate formulas. A 20 September recovery manifest names the full proof, its internal location and expected file hash. The retained recovery intake contains the Markdown manifest and addendum. The bounded search below found neither the named original nor a byte-identical copy under another name. Retain the qualification in reference [17]. [Published state excerpt, §4.3, T01.6](https://github.com/hnt119/polynomial-image-compression/blob/c689ab52ca3bb9e3221bd09ae9a083a3111e39df/research/proofs/source-recovery/T01-state-digital-theorems.md) · [Reference 17 at its existing citation pin](https://github.com/hnt119/polynomial-image-compression/blob/bd1f2d663262821575eebdfa559b7c25f76b46ab/research/exports/2026-11-05-report-references/README.md#ref17).

## Match to the report

V6 §4.4, printed p. 17 (PDF page 19), fixes a nonempty finite prime set $S$ and $\alpha>0$. For every sufficiently large $N$ with all prime divisors in $S$ and every $D\subseteq\{0,\ldots,N-1\}$ with $|D|\ge N^\alpha$, the recorded theorem gives
$$
 |Z_N(D,D)|\ge\eta(S,\alpha)|D|^2,\quad \eta(S,\alpha)>0,\qquad
 Z_N(U,V)=(U-V)^3+N^2(U+V).
$$
The real carrier is $A=D/N$. The identity $N^3P_+(U/N,V/N)=Z_N(U,V)$ with $P_+(x,y)=(x-y)^3+x+y$ preserves the number of distinct outputs. I compared the target, quantifiers and proof-availability clause with §4.3 of the state. Reference [17], printed p. 28 (PDF page 30), accurately identifies the complete standalone proof as unavailable for that revision. Appendix C.5 concerns the separate **minus-sign** rich-fiber construction, whose [full T04 proof, §§B–C and Theorem 3](https://github.com/hnt119/polynomial-image-compression/blob/c689ab52ca3bb9e3221bd09ae9a083a3111e39df/research/proofs/source-recovery/rich_fiber_results_checkpoint.md) is available.

## Identified source and dependencies

| Item | Locator and SHA-256 | Evidence available in this pass |
|---|---|---|
| Fixed-prime proof sought | `Regular_Digital_Carry_Collapse_Universal_NoGo_Checkpoint.md` (3 September), Theorem A.2, §F.2, (F.13)–(F.20). Expected `515efb472ced6f4ac5e64c9a98f5c351d0d6c91977f5ffdd78fda10166df020c` | Manifest identity only. The reported argument uses capped prime valuations, fiber spacing and (F.18) renormalization. The addendum locates safeguards in §§C–D, F, H and identifies no separate proof or corrections file. Its Theorem A.1 in §F.1 concerns the narrower regular-language case. |
| Alternate proof-bearing bundle sought | `Regular_Digital_Carry_Collapse_Research_Bundle.zip`. Expected `6da10ecb9a329d5cae572c39a86570dbf427c88da9775cb1e4771c97863462fa` | The addendum reports 16 entries, including the same checkpoint, code, metadata, reports and ten CSVs. Its original archive and `DIGITAL_ARCHIVE_INVENTORY.csv` were absent from the checked sources. The state identifies `tmp/digital_scout/` as the earlier run location. The reported 7,004 finite depth records concern computational tests. |
| Recovery intake | `MANIFEST.md`, `2ac8142d75ac78b54cb54a62e3e6bf1ff725fcf0c383ac9fdbe52f0f238a7df1`; `T01_RECOVERY_ADDENDUM_2026-09-20.md`, `b1bee6b6618f8abcb50589992b499630da1568a370eec87a8053f401fa913042` | Both hashes recomputed from located documents. Their “PROVIDED” designation describes the larger historical recovery package. These two files were the retained September T01 recovery intake. |
| State and citation witness | `T01_CURRENT_STATE.md`, `2095cb7b4a5f7d848dea1356956ad36f5303e4037b13b2efe7fa32b0c08f2624`; `T01-state-digital-theorems.md`, `80a3faebb937412980227e4703b568bb50f837f652b64c2bfe30847e5c33c693` | Both hashes recomputed. §4.3 gives T01.6, a fiber estimate and a renormalization identity. The 96-group ledger indexes it under `T01/2026-09-16-three-branch-lift/TB-S3`. The 75-claim register uses `T01-DIGITAL`. These refer to one reported result. |
| Located continuous no-go | `Concrete_Cubic_Compression_Block_NoGo_Checkpoint.md`, §F.3, `413dcc5aa06ddc03129d76a68360dc1737a0a7d156d70e27a510a4699d5bbc62` | Recomputed file identity. Its argument treats a positive-volume coordinatewise block and continuous covers. Sparse rational digits with fixed prime support require the separate T01.6 argument. |
| V6 report identification | Local read-only PDF, `9d5ad8f21b86df90f3ff29cd24074bc7925d20f401fdee5a96dcf1ae966066cd` | Recomputed PDF identity and checked §4.4 and [17] directly. The historical November 4 source-limit excerpt concerns a different report revision. |

## Bound and archive inventory

The pass covered five first-party source classes: the public audit checkout at `c689ab52ca3bb9e3221bd09ae9a083a3111e39df`, retained project research/source/supplement directories, project migration and saved T01-run directories, the staged first-party proof collection, and the retained UROP results/migration/prompts/problem/study/Elekes–Rónyai directories. The UROP T01 results folder held its state, separate norm–trace checkpoint, and the norm–trace experiment program and data.

I searched basenames for the exact proof and bundle, the dated rich-fiber candidate-test filename, recovery inventories and checksum filenames. I also searched digital/carry-collapse, fixed-prime/digital and digital-scout name variants. The walk did not follow symlinks. Directory descent stopped at depth 12 and excluded source-control internals, environment/cache directories, administrative records and conversation archives. Within these roots there were 2,269 regular, nonhidden files, counting copies. I compared the expected proof digest with the bytes of all 915 eligible Markdown, plain-text and TeX documents of at most 4 MiB, and checked for the original title or a proof-section heading/display matching §F.2 and (F.13)–(F.20). Mentions in status files, manifests and claim registers led to the same source-reported statement.

Archive inspection was limited to files at most 64 MiB. Five ZIP instances represented three distinct archives. I inspected each unique archive's complete member list before reading its eligible Markdown/plain-text/TeX members in memory, using the same 4 MiB size and identity/section tests. No nested archives appeared.

| Unique ZIP | SHA-256 | Copies | Member names inspected | Text members screened |
|---|---|---:|---:|---:|
| `T02_MIGRATION_PACKAGE.zip` | `e161d1b51bbea51cc102bc950c734d35748b5c1369d5d9e7a7927c8bfb534b69` | 1 | 68 | 50 |
| `T03_RESEARCH_RECORD_20260910.zip` | `5c51114ec0fa2663b586665db30bc6648f1e3a1beaae2e578099b9abc6e85430` | 3 | 45 | 23 |
| `T04_SOURCE_ARCHIVE.zip` | `eeac795be4c5582de9ca7d20cd0b458576f5d346a9decce4867ab49176f75eb2` | 1 | 63 | 52 |

None of the 176 member names matched the sought checkpoint, optional digital bundle or digital-scout variants. None of the 125 eligible text members matched the proof digest or the tested proof-section signatures. The review stopped at this boundary. There was no imported program execution, pickle deserialization, external search or reconstruction of the missing proof. The fixed-prime theorem retains its source-reported status. The unrestricted T01 target remains **OPEN**.
