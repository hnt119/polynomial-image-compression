# Source audit and historical qualifications

The initial repository preserved six supplied research artifacts: three prompts, a review note, a conjecture source, and a nine-page report. The later four-track history import recovered 33 additional artifacts; see [the recovery record](../research/HISTORY_SOURCES.md). These are research records, not a complete independently verified proof package. Prompts describe earlier or proposed assignments; their instructions do not establish that those assignments were completed.

## What the archive supports

| Record and locator | Qualification for readers |
| --- | --- |
| [C1 prompt](../research/prompts/Phase_C1_Corrections_and_Higher_Degree_Proof_Search_Prompt.md), §3; [C1 review](../research/notes/Phase_C1_Review_and_Next_Steps.md), “Verdict” | These records report a corrected C0 result for integral coefficients in `(ax+by)^2+cx+ey`, with `gcd(a,b)=1` and `ab(ae-bc)≠0`. The exponent may depend on the fixed polynomial. The underlying corrected proof and its ledgers are absent here, so this is an attributed historical status. |
| [C1 review](../research/notes/Phase_C1_Review_and_Next_Steps.md), “What C1 establishes” and “How to interpret QCLASS-DEFICIT” | The reported obstructions concern specified counting bounds. They do not prove that the actual quartic image has quadratic size. Compression for `(x+2y)^4+3x-y` remains unresolved in these records. |
| [C1 review](../research/notes/Phase_C1_Review_and_Next_Steps.md), Corrections 1–2 | The note supplies short arguments for weak M1-DEFICIT and the finite M2-CORR case `p=5,d=2`. The first relies on width/carrier bounds from the absent C1 report and is explicitly insufficient for compression. The second does not settle general `p,d`. |
| [Conjecture source](../research/conjectures/nonsingular_quadratic_compression_conjectures.tex), opening discussion and Conjectures 1–3 | The Eisenstein-norm and broader nonsingular-quadratic targets are conjectures. The opening phrase “known 2026 counterexamples” and references to recent constructions are historical source wording; external literature status has not been verified for this release. |
| [Split-prime report](../research/reports/Polynomial_Image_Split_Prime_Generalization.pdf), Theorem 1, pp. 1–4; §7, pp. 7–8 | The explicit sufficient criterion assumes a suitable totally real split-prime field sequence. The “unconditional” quadratic corollary invokes a supplied tower construction that is not reproduced in this repository. This release does not independently certify that dependency or the report's other theorems. |
| [C2 prompt](../research/prompts/Phase_C2_Hybrid_Carrier_Structural_Lemma_Prompt.md), §§1, 3, 11 | The hybrid carrier is a proposed investigation. The prompt is not evidence that a useful structural lemma or the quartic target has been proved. |

## A field-supply discrepancy

The [C0 prompt](../research/prompts/Phase_C0_Conjecture_Proof_Search_Prompt.md), §3.5, attributes an “infinite fixed set” of split primes to an earlier report. The later C1 prompt, §3, instead uses a **finite** set of `t=floor((ell−1)^2/100)` primes for each fixed auxiliary parameter `ell`, with `log D=O(ell log ell)`. That later formulation matches Proposition 3.8, p. 12, of the locally supplied *Planar Point Sets with Many Unit Distances*, attributed to OpenAI; Remark 3.9, p. 14, fixes the arithmetic choices before the tower level varies. Those passages were inspected locally for this comparison. The paper is not redistributed here, and this comparison does not certify its proof. Do not infer arbitrary prescribed-prime compatibility or silently hold the discriminant cost fixed while changing the prime supply.

## Missing dependencies

The five core Phase B Markdown records, Phase A reproduction, both Phase B cycle reports, and original C0 PDF have now been recovered. The corrected C0 proof package, original C0 Markdown and separate ledgers, main C1 report and its correction/source/claim/referee records, and completed C2 deliverables remain missing. A reference to a file is not evidence that its proof has been checked. Tracing these dependencies remains necessary for a complete proof-reproducibility claim.

## Publication check

The text of all six artifacts, the report's PDF metadata, link actions, and embedded attachment were inspected for obvious personal, administrative, and credential data. No personal contact information, machine-specific paths, or authentication secrets were found in that scope. The PDF retains Content Credentials identifying ChatGPT and its generation software, timestamp, and signing provenance. These describe artifact origin, not mathematical validity. This was a bounded content check; external novelty, literature status, and independent theorem verification remain unchecked.
