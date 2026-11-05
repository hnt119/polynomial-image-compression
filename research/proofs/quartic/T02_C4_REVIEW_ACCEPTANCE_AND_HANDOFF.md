# C4 review acceptance and documentation handoff

Date: 2026-09-10. Track: T02, fixed polynomial `P4(x,y)=(x+2y)^4+3x-y`.

This note applies `upload/Phase_C4_Review_and_Next_Steps.md` before the migration export. It records the supplied review and audits existing companions. It introduces no new mathematical result, proof search, computation, or external novelty claim. The accepted C4 proof files are unchanged.

## Accepted state

- **PROVED:** for the actual mixed-characteristic local cubic, the full inverse images of a critical fiber have `N1=4` and `Nm=22*7^(3m-4)` for every `m>=2`.
- **PROVED:** the support is three complete cosets modulo the third maximal-ideal power and one complete coset modulo the fourth power. The normalized local factor improves from `4/7` to `22/49` once and then stabilizes.
- **FAILED:** higher rational-prime precision, the saturation-ideal cover, mixed-depth covers, and arbitrary 7-supported ideal-coset covers of the entire local product support cannot yield a positive rate when used with the stated full continuous intervals and uniform ideal-norm packing. This failure has exactly that scope.
- **OPEN:** the same-input fixed-quartic power-saving target and any actual-image lower bound that would disprove it.

The accepted headline is:

> **HIGHER-PRECISION LOCAL COUNT PROVED; FULL-INTERVAL CLASS-PACKING ROUTE RETIRED WITHIN THE STATED SCOPE.**

No optimization over arbitrary higher-precision input subsets has been proved. Smaller globally realized local support, branch-dependent real ranges, arithmetic correlations across factors, and other carrier mechanisms remain outside the retirement.

## Companion audit and provenance

The supplied external review inspected only the C4 PDF and the C2-C3 change log. Its acceptance of the analytic proof does not assert external verification of the companions.

This documentation pass found all 13 C4 deliverables in the existing 36-entry `Phase_C2_C3_C4_Reviewed_Package.zip`; their bytes match the current local files. The canonical JSON matches the retained independent-referee reproduction JSON. These are file-consistency checks, not a new mathematical rerun. The prior internal referee's complete script reproduction remains prior internal evidence.

| Item | Existing location | Audit record |
|---|---|---|
| Analytic proof | `Phase_C4_Higher_Ramified_Precision.md` and matching PDF | Supplied external review accepts theorem and scoped gate |
| Checking script | `higher_precision_check.py` | Present; hash below matches existing manifest |
| Canonical results | `higher_precision_results.json` | Present; matches retained referee JSON |
| Local-model note | `agents/higher_model.md` | Present |
| Alternative lifting note | `agents/higher_lifting.md` | Present |
| Rate calculations and numerical table | `agents/higher_rate.md`, Section 2; main report, Sections 5-6 | Present inside these documents; no pre-existing separate C4 rate-table file |
| Source manifest | `SOURCE_MANIFEST_C4.md` | Present; its review chronology describes the original C4 run |
| Claim ledger | `CLAIM_LEDGER_C4.md` | Present |
| Referee report | `REFEREE_REPORT_C4.md` | Present; internal research-workflow audit, not external peer review |

The new `C4_SIGNED_RATE_LEDGER.md` is an explicitly labelled extraction of the existing rates and illustrative table. It does not retroactively claim that a separate rate table existed during the original review.

Recorded SHA-256 values:

- Script: `9193e2ce67c32ff063f54219f39a5c03102942226ceccdca6ca4f0113f10a20a`
- Canonical and retained reproduced JSON: `21ce5b48f0e4ce62a98ee9a1b1a0396b955e97c89fc5abde83fd41a30b3ac5fb`

The numerical table uses the illustrative discriminant floor `D=7^(2/3)`; no constructed tower is asserted to attain that floor. The actual base-field discriminant is fixed by the source construction.

## Handoff and stopping rule

Freeze the accepted theorem and retire increasing `m` for this full inverse-image pattern as a route to additional density savings. Do not restart the modulus-7 subset search.

The one next proof obligation is to specify a concrete subcarrier of the established critical-coset carrier and a branch variable correlated with its real embeddings, then prove an all-pairs, branch-dependent realized-support cover with a positive fully charged signed rate. `T02_CURRENT_STATE.md`, Sections 17-18, gives the precise gate. No such carrier or lemma has been produced by this documentation pass.

The reported factors exceeding `3.54^d`, `3.85^d`, and `4.24^d` are lower bounds for particular numerical envelopes divided by the actual pair budget. They are necessary lower benchmarks for any proposed reduction of those envelopes, not sufficient improvement thresholds. The exact remaining envelope gap and all subcarrier-density, branch, distortion, and multiplicity costs must be paid.

The review permits a later mechanism pivot if no concrete correlation is found. That fallback has not been executed. The export prompt explicitly forbids new research and asks for one next obligation only; the migration handoff therefore records the realized-support obligation and stops.
