# Phase C0 correction log

## Freeze verdict

The submitted Phase C0 files remain unchanged. The corrected copy is
`Phase_C0_Corrected.md`.

**Verdict:** after the corrections below, the quadratic family theorem is
**safe to freeze within the supplied source system**. No correction changes
the polynomial, the hypotheses

\[
\gcd(a,b)=1,\qquad ab(ae-bc)\ne0,
\]

the same-set construction, the rate inequality, or the final quantifiers.
The field-symbol repair is mathematically necessary; the other changes repair
terminology, formulas, and the scope of the quartic conclusion.

External novelty and literature status have not been checked.

## Corrections to the main report

| Original location | Corrected claim or text | Reason | Effect on proof |
|---|---|---|---|
| Section 1, mechanism paragraph | `Theta(X)` is the normalized certificate factor furnished by the stated bounds. | The radius used to derive it was not optimized. | None; a valid upper bound is sufficient. |
| Section 4.1, deformation display | Replace literal `qquad` by `\qquad`. | Malformed TeX reached the submitted PDF. | Cosmetic only. |
| Section 5.1, field-supply lemma | Use the source's totally real layers `F_j`, with `d_j=[F_j:Q]`, `rd(F_j)=rd(F)`, and complete splitting in every `F_j`. State that source-notation `K_j=F_j(i)` is a different CM field and is not used as a carrier. | Proposition 3.8(P1)-(P4) uses `F_j` for the totally real tower. Its `K_j` has no real embeddings. | Necessary provenance and signature repair; the intended argument survives unchanged. |
| Section 5.2 and Section 6, all tower-level carrier occurrences | Replace `B_{K_j}(X)` and real embeddings of `K_j` by `B_{F_j}(X)` and real embeddings of `F_j`. | Propagates the field correction. | Restores the stated real carrier and embedding. |
| Section 6, opening | Explicitly declare that generic `K` denotes one totally real layer `F_j`, not the source's `K_j=F_j(i)`. | Avoids a second notation collision. | Clarifies hypotheses of the generic carrier lemmas. |
| Section 6, Step 1 | Replace `F_{p_i}^{,d}` by `F_{p_i}^{d}` in both CRT displays. | The comma is extraneous punctuation in a power. | Cosmetic only; the intended class count is unchanged. |
| Section 6, Step 2 | Call `9X^2+4QX` a valid all-conjugate upper bound, not an exact radius. | It comes from separately maximizing `|u+2v|` and `|3u-v|`; simultaneous attainment was not proved. | None; the theorem only needs containment. |
| Section 9, rate-factor discussion | Call `Theta(X)` an explicit certificate factor, while retaining the distinct conservative family factor `theta=C_P D rho`. | Prevents an optimization claim. | None. |
| Section 10, quartic radius | Call `81X^4+4Q^3X` a valid symmetric upper bound from separate estimates. | It is not the exact continuous absolute radius, and it need not be attained on the algebraic carrier. | The displayed upper-bound calculation remains valid. |
| Section 10, quartic verdict | Use **CERTIFICATE OBSTRUCTION** for the local-fourth-power class count plus one interval plus uniform per-class packing. | A numerical upper-bound base greater than one is not an image lower bound. | Narrows the conclusion; the quartic target remains open. |
| Section 11, O3 row | State only that the specified quartic certificate fails at every scale; delete the unsupported broader `generic height screens` claim. | No quantified broader carrier class was proved there. | Scope repair only. |
| Section 11, O7 row | A different carrier is one possible route, alongside sharper same-carrier support counting, more residue information, a different deformation, or another proved mechanism. | C0 did not prove new geometry necessary. | Restores all logically open alternatives. |
| Section 12, proposed lemma | Put carriers in `O_{F_j}` and define the packing modulus `R=Q` before use. | Repairs field notation and an undefined symbol. | Makes the proposed dependency auditable. |
| Sections 12 and 13 | Replace `any positive answer must introduce genuinely new carrier geometry` by the scoped alternatives above. | A failed upper bound is not a construction impossibility. | The actual polynomial and the centered carrier remain undecided. |
| Throughout theorem references | Rename the corrected copy's result `Theorem C0.1`. | Avoids collision with the present Phase C1. | Presentation only. |

## Corrected ledger entries

These entries replace the wording of the submitted ledgers for purposes of
the corrected baseline. The submitted ledgers themselves remain untouched.

| Ledger entry | Corrected version | Status |
|---|---|---|
| Claim ledger CL1 | Proposition 3.8 supplies totally real `F_j` with degrees tending to infinity, constant root discriminant, and the source-selected fixed split primes. The distinct CM fields `K_j=F_j(i)` are not used. | SOURCE INPUT |
| Claim ledger CL8 | `9X^2+4QX` is a valid all-conjugate output bounding radius for the explicit quadratic deformation. | PROVED |
| Claim ledger CL16 | The displayed fourth-power-class plus symmetric-interval plus uniform-packing factor exceeds one for every `X>0`. This is not a lower bound for the actual image. | CERTIFICATE OBSTRUCTION |
| Candidate ledger C2 | The specified symmetric interval certificate fails. Sharper all-pairs support counting on the same carrier, additional residue information, a different deformation, a different carrier, and other proved mechanisms remain open. | CERTIFICATE OBSTRUCTION |

## Focused source recheck

The correction pass inspected Proposition 3.8(P1)-(P4), its construction,
and Remark 3.9 in `project_sources/03-unit-distance-proof.pdf`; frozen Phase A
Section 4.1; all five Phase B Markdown records; the proof-bearing portions of
the Cycle 2 report; and all six submitted C0 results. A complete inspection
ledger is in `SOURCE_MANIFEST_C1.md`.

No load-bearing source needed by the corrected quadratic theorem is missing.
The theorem uses only the fixed primes produced with the source tower; it does
not assume an arbitrary prescribed-prime splitting theorem.

## Final provenance statement

The corrected result is an extension of the supplied quadratic mechanism, not
a newly named compression mechanism. The corrected baseline proves, within
the supplied source system, that every fixed

\[
P(x,y)=(ax+by)^2+cx+ey
\]

with `gcd(a,b)=1` and `ab(ae-bc) != 0` admits arbitrarily large same-input
finite real sets with a member-dependent fixed power-saving exponent.
