# Phase C2 precision addendum

## Review source and scope

The user supplied the seven C2 precision corrections in the current review
message on 2026-09-08. This supersedes the earlier missing-review placeholder.
All seven corrections have been applied to the current C2 Markdown sources.
They do not change the determinant-7 theorem, its exact count \(208/343\),
the tower refinement, the carrier construction, or the unresolved status of
the fixed quartic. The earlier independent referee report is preserved as a
historical review; it has not been silently rewritten.

For the precise scope of the corrected current text, use the following map.
The paths below are relative to the project root.

## 1. Claim C2-22: occupied classes versus class population

The bound

\[
208^{d/3}(\rho_4Q)^d
\]

controls the **total number of occupied residue classes** modulo
\(7Q\mathcal O_F\). It does not bound the population of an individual
occupied class. Uniform per-class packing is a separate counting step.

**Applied at:** `phase_c2/CLAIM_LEDGER_C2.md`, claim C2-22 and the
Interpretation rule; `phase_c2/Phase_C2_Hybrid_Carrier_Structural_Lemma.md`,
Opening summary. The exact CRT statement in Section 5.3 was already correct
and is unchanged.

## 2. Squared units

The corrected statement is:

> No additional congruence-fiber selection is imposed beyond the paid-for
> restriction to squared units.

The existing squared-unit count, radius-halving cost, and two-element square
kernel remain unchanged. No equidistribution is assumed.

**Applied at:** C2 main report, Section 3.2 and the Section 6.2 rate-ledger
row for the unit congruence restriction.

## 3. The certified rate

The elementary ratio certificate proves no positive gain; set

\[
\kappa_{\mathrm{cert}}=0.
\]

This is a convention for that certificate and does not determine the exponent
of the actual polynomial image. The conditional rate screen remains
unchanged.

**Applied at:** C2 main report, Opening summary's fifth answer, Section 6.2,
Section 7's final paragraph, and Section 8's third attempt; C2 claim ledger,
claim C2-27.

## 4. Scope of the hybrid no-gain statement

The conclusion applies to the displayed elementary parameter count.
Possible overlaps across distinct points of \(\mathcal K_u\), and possibly
across different ratios, were not ruled out.

**Applied at:** C2 main report, Opening summary and Theorem C2.1 in Section
4.3 (statement and concluding proof sentence); C2 claim ledger,
Interpretation rule. The maps, cardinality identities, determinant, and
degree-four fiber bound are unchanged.

## 5. General M2-CORR

The general statement has status **CONJECTURAL**. Only the case
\(p=5,d=2\) was proved in the C1 status addendum.

**Applied at:** C2 main report, Section 1; C2 claim ledger, status key and
claim C2-05. `phase_c2/C1_STATUS_ADDENDUM.md`, Section 2 and its general
M2-CORR status-table row, already used **CONJECTURAL** and remain unchanged.

## 6. Claim C2-28 and the accepted headline

Claim C2-28 now reads “Status of the fixed-quartic compression target,” with
status **UNRESOLVED**. The accepted C2 headline is:

> **USEFUL STRUCTURAL LEMMA PROVED; FIXED-QUARTIC TARGET UNRESOLVED.**

**Applied at:** C2 claim ledger, claim C2-28; C2 main report, opening and
final classifications and the third attempt's verdict; C1 status addendum,
the fixed-quartic compression target row. Earlier historical referee
wording is preserved.

## 7. Non-Frattini primitive-generator elimination

When the killed Frobenius has nonzero image in the Frattini quotient, the
proof now explicitly invokes the standard pro-\(p\)
primitive-generator elimination fact. In a minimal free pro-3 presentation,
a lift has nonzero Frattini image. Complete that image to a basis; the
pro-\(p\) Burnside basis theorem and the Hopfian property of finitely
generated free pro-\(p\) groups show that this lift belongs to a free
generating basis. Imposing that generator equal to 1 removes it, and
substitution in the old relators adds no further relators. This justifies
the existing one-generator loss and the displayed conservative relation
bound. The Golod-Shafarevich calculation is unchanged.

**Applied at:** C2 main report, Section 2.1, paragraph beginning “More
explicitly”; C2 claim ledger, claim C2-07's dependencies.

## Current interpretation

This addendum resolves the original missing-review dependency. It records
wording precision and an explicit justification already needed by the tower
argument. It introduces no new polynomial-image theorem. The independent
referee report remains evidence of its original review, rather than a claim
that its author reviewed these later wording edits. External novelty remains
unchecked.
