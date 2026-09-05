# Source record

This is a curated snapshot of the research materials available on 5 September
2026. It is not the complete project history. Archived files retain their original
wording, including proposals, historical instructions, and claims requiring review.

## Initial snapshots

All six files below were inspected during repository preparation and copied
byte-for-byte. Their sizes and SHA-256 hashes are recorded in
[research/manifest.json](../research/manifest.json).

| File | Role and interpretation |
| --- | --- |
| [Phase C0 prompt](../research/prompts/Phase_C0_Conjecture_Proof_Search_Prompt.md) | Historical conjecture and proof-search assignment; not a completed report |
| [Phase C1 prompt](../research/prompts/Phase_C1_Corrections_and_Higher_Degree_Proof_Search_Prompt.md) | Historical correction and quartic-search assignment; reports the C0 starting result |
| [Phase C1 review](../research/notes/Phase_C1_Review_and_Next_Steps.md) | Review of submitted C1 work; includes two short elementary corrections and a proposed continuation |
| [Phase C2 prompt](../research/prompts/Phase_C2_Hybrid_Carrier_Structural_Lemma_Prompt.md) | Proposed hybrid-carrier structural-lemma task; not evidence that the task was completed |
| [Nonsingular quadratic conjectures](../research/conjectures/nonsingular_quadratic_compression_conjectures.tex) | Original proposed Eisenstein norm and broader quadratic directions; external-status statements have not been checked |
| [Split-prime generalization report](../research/reports/Polynomial_Image_Split_Prime_Generalization.pdf) | Historical nine-page report containing an explicit criterion, classifications, and further claims; inclusion is not independent certification of every theorem |

An additional **33 unique files** were recovered from prior tasks when the owner
requested the four-track history. The archive now contains **39 hashed files**.
See [HISTORY_SOURCES.md](../research/HISTORY_SOURCES.md) for every recovered file
and its provenance. These include Phase A/B records, the original C0 PDF, and
cubic/Eisenstein checkpoints. The original C0 PDF is not its corrected successor.

The overview, roadmap, experiment code, and repository infrastructure were written
for this repository. They were not part of the earlier research phases.

## Source locators and qualifications

- **Same-set target and support accounting:** C0 prompt §§1, 3.2, and 3.6.
- **Reported quadratic family:** C1 prompt §3 and C2 prompt §3, as reported by
  those records. The complete corrected C0 proof is not included.
- **Quartic status and elementary corrections:** C1 review, “Verdict,” “What C1
  establishes,” and “Correction 1” / “Correction 2.” The first correction is
  conditional on the cited C1 width and carrier estimates; its positive deficit
  is insufficient for the target rate.
- **Hybrid model:** C2 prompt §§4–7 defines a proposed carrier and counting
  obligations. These are research instructions, not completed theorems.
- **Explicit sufficient criterion:** split-prime report, Theorem 1 and its proof,
  pp. 1–4. It assumes a specified totally real split tower with bounded root
  discriminant, along with a strictly positive gain after all costs. Its later
  classifications and tower-selection claims need their own source checks.

The early C0 prompt's description of an infinite fixed split-prime set should not
be promoted to a repository assumption. The C1 correction tracks a finite number
of split primes and a jointly dependent discriminant bound. See the
[source audit](source-audit.md) for the comparison with Proposition 3.8 and
Remark 3.9 of the supplied unit-distance proof.

## Available references not redistributed

The local project supplied `unit-distance-proof.pdf`,
`unit-distance-remarks.pdf`, and `unit-distance-cot.pdf`. The source audit inspected
the relevant field-supply passage of the proof. The discovery transcript is
discovery context, not proof authority. These PDFs are not copied into this
repository.

Additional local folders contain Elekes–Rónyai and sum-product papers. They were
not needed for the repository implementation and were not treated as independently
verified literature. No external literature or novelty search was performed.
Bibliographic metadata and stable primary-source links remain a roadmap item;
filenames alone are not sufficient attribution for imported theorems.

Administrative and grant forms are outside the scope of this research archive.
The manifest deliberately records filenames rather than personal machine paths.

## Referenced materials still missing

After recovering the historical task attachments, these dependencies still have
not been recovered:

- The original `Phase_C0_Conjecture_Proof_Search.md` and its separate source,
  candidate, claim, and referee ledgers. The report's PDF is now archived.
- `Phase_C0_Corrected.md`, its PDF, and `C0_CORRECTION_LOG.md`.
- The completed `Phase_C1_Higher_Degree_Proof_Search` report, C1 claim/source/
  referee ledgers, and `model2_local_classes.py`.
- A completed C2 structural-lemma report and its ledgers.

“Missing” means not recovered from the inspected inputs, not that the document
does not exist elsewhere. Temporary paths named in the earlier C0/C1 task no
longer resolve. When a dependency is recovered, record its provenance,
inspect the relevant claim, and update status explicitly.

## Verify the archive

From the repository root:

```bash
python3 scripts/check_repository.py
```

This checks archived file sizes and hashes, all four track records, and local
links in repository-authored Markdown. Historical source links remain unchanged.
It verifies integrity and navigation, not mathematical correctness.
