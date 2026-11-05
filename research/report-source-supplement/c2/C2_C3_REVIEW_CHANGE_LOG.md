# C2-C3 review change log

Review source: the user's “Phase C3 review and next steps” message and its
seven-point “Phase C2 precision addendum,” supplied on 2026-09-08.

## C2 precision changes

The C2 mathematical results and proof architecture are preserved. The
following text changes apply the seven supplied review corrections.

| Correction | Current file and location | Exact change in meaning or wording |
|---|---|---|
| C2-22 | `phase_c2/CLAIM_LEDGER_C2.md`, C2-22 and Interpretation rule; C2 main report, Opening summary | The bound counts occupied residue classes in total, not points within an individual class. |
| Squared units | C2 main report, Sections 3.2 and 6.2 rate ledger | No additional congruence-fiber selection beyond the paid-for squared-unit restriction. |
| Certified rate | C2 main report, Opening summary, Sections 6.2, 7, and 8; C2 claim ledger, C2-27 | Replaced the unqualified zero rate by the elementary certificate convention \(\kappa_{\mathrm{cert}}=0\); the actual image exponent is undetermined. |
| Hybrid no-gain | C2 main report, Opening summary and Theorem C2.1; C2 claim ledger, Interpretation rule | Confined the no-gain conclusion to the elementary parameter count; cross-point and cross-ratio overlaps remain possible. |
| M2-CORR | C2 main report, Section 1; C2 claim ledger, status key and C2-05 | General status is consistently **CONJECTURAL**; only \(p=5,d=2\) is proved. The C1 addendum already had this general status. |
| Fixed-quartic status | C2 claim ledger, C2-28; C2 main report, opening and final headlines and attempt verdict; `phase_c2/C1_STATUS_ADDENDUM.md`, final table | C2-28 states the target's status and is **UNRESOLVED**; the accepted headline explicitly says FIXED-QUARTIC TARGET UNRESOLVED. |
| Tower refinement | C2 main report, Section 2.1; C2 claim ledger, C2-07 | Explicitly invoked primitive-generator elimination in the non-Frattini case, with the free pro-3 presentation justification. Existing numerical bounds are unchanged. |

The C2 main report is
`phase_c2/Phase_C2_Hybrid_Carrier_Structural_Lemma.md`.

`phase_c3/C2_PRECISION_ADDENDUM.md` replaces the earlier missing-review
placeholder with the supplied corrections and section-by-section application
map. The original `phase_c2/REFEREE_REPORT_C2.md` and historical analyst
notes are unchanged. The C2 precision-edit subtask did not modify any PDF;
document regeneration and the C3 review changes are recorded separately below.

During rendering, a missing backslash before `qquad` in the C2 Section 3.3
boxed injectivity identity was repaired. This is solely a typesetting
repair; the formula, constants, and mathematical meaning are unchanged.

## C3 precision changes

1. Narrowed the final headline in the main report, decision note, claim
   ledger, README, and current endpoint of the referee report to:
   **SCOPED NO-GO FOR MODULUS-\(7\) INPUT ENGINEERING WITH FULL-INTERVAL CLASS PACKING.**
2. Explicitly excluded higher congruence powers and smaller realized-support
   covers from the frozen C3 no-go. The universal local theorem, all equality
   cases, and every signed rate formula are unchanged.
3. Replaced the obsolete missing-review status with the historical fact that
   the seven corrections were unavailable during the original run and are
   now supplied and applied. The source is the current user message, not an
   invented local review file.
4. Distinguished the user's external PDF-only acceptance from the earlier
   internal independent audit and reproduction. External checking of the
   companion files remains provisional; the full companions are supplied
   for separate inspection.
5. Added an explicitly editorial dated note to the C3 referee report. Its
   historical mathematical audit is preserved; no new independent referee
   work is attributed to its original author.
6. Regenerated the corrected C2 and C3 PDFs from their Markdown, retaining
   the proof architecture, and rebuilt the companion package.

## Separate higher-precision continuation

The bounded lifting question authorized by the review is developed in
`phase_c4/`. Its results do not alter the frozen modulus-7 theorem or expand
the scope of C3's headline. The local full-inverse-image count improves once,
and its separate global certificate audit records the appropriate stop.
