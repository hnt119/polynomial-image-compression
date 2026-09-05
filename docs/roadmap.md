# Research roadmap

The repository first needs an auditable research record, then a bounded investigation of a specific missing estimate. This roadmap separates reported results, available elementary proofs, and proposed work. See the [research overview](research-overview.md) for exact statements and quantifiers.

For the owner's four current directions, start with [PROJECT_HISTORY.md](../research/PROJECT_HISTORY.md)
and the individual [track status records](../research/tracks/README.md). The
sections below retain the initial C0–C2 roadmap and its broader source-audit work.

## 1. Complete the source and proof record

**Current state:** the archive includes three phase prompts, the C1 review, a conjecture note, and an additional [split-prime generalization report](../research/reports/Polynomial_Image_Split_Prime_Generalization.pdf). That report's broader quadratic corollary and proper-power classification have not been independently audited for this repository. The prompts name further proof reports and primary sources; their names alone do not verify their contents.

The original C0 PDF, Phase A/B reports, and five core Phase B Markdown files have
now been recovered through the task history. The remaining source milestone is
to recover or audit the following:

- The corrected C0 proof, original Markdown, correction log, claim ledger, source manifest, and referee report.
- The full C1 higher-degree report and its claim ledger, source manifest, and referee report.
- The exact Phase A carrier and unit lemmas, Phase B mechanism records, and field-supply statements cited by the completed arguments.

For each imported result, record the inspected file, a theorem or section locator, its hypotheses, and which later claims depend on it. Distinguish a primary statement inspected directly from a review's report that a statement was checked. Confirm that field signatures, split primes, discriminant bounds, and unit estimates concern compatible field families.

**Completion criterion:** a reader can follow every load-bearing claim in the reported C0 theorem to a complete derivation or an explicitly identified source input. Until then, preserve the label “reported as established in the supplied source system; complete proof not archived here.”

## 2. Preserve the corrected C1 scope

Carry forward the two elementary corrections from the [C1 review](../research/notes/Phase_C1_Review_and_Next_Steps.md):

| Item | Treatment |
| --- | --- |
| Weak M1-DEFICIT | Record the elementary deduction from the stated width and carrier bounds. Mark it insufficient for the required rate. |
| M2-CORR at $p=5,d=2$ | Preserve its direct proof; exhaustive subset enumeration is unnecessary. |
| Interval and residue-class packing obstruction | State exactly the carrier geometry and counting bounds it covers. Do not convert it into a lower bound for the actual image. |
| Coordinate-product local restrictions | Include the loss in input density twice. Do not extend the theorem to arbitrary correlated inputs without proof. |

**Completion criterion:** the claim ledger consistently distinguishes a failed upper-bound certificate from a construction impossibility or a refutation of the polynomial's existential target.

## 3. Test the C2 hybrid with one measurable lemma

The [C2 prompt](../research/prompts/Phase_C2_Hybrid_Carrier_Structural_Lemma_Prompt.md) supplies a concrete proposed model for the quartic $P_4(x,y)=(x+2y)^4+3x-y$. It is a research specification; no successful C2 result is established by that document.

Begin with one precisely defined carrier $C_j=G_jT_j$ in the same totally real field family. Before claiming a gain, establish or explicitly isolate:

1. Unit counts and additive-carrier counts, including sign restrictions and regulator costs.
2. The maximum multiplicity of $(g,t)\mapsto gt$, so the lower bound for the actual set $C_j$ is justified.
3. Exact all-pairs coverage through the ratio decomposition and its correlated supports.
4. A support-specific estimate whose gain survives the ratio-union cost, distortion, input restrictions, and multiplicity.

For a candidate lemma, write its exact hypotheses, the quantity it bounds, a proof or named missing dependency, the baseline it improves, and its per-degree gain. A structural relation or bounded-fiber change of variables does not by itself show a smaller support. Enclosing the hybrid in full output intervals reuses the already obstructed C1 certificate.

The required accounting is

$$
e^{ad-o(d)}\le|C_d|\le e^{Bd+o(d)},\qquad
|F_Q(C_d,C_d)|\le e^{hd+o(d)},\qquad
\kappa=2a-h.
$$

Only a proved $\kappa>0$, with the valid fixed-polynomial transport and $0<a\le B$, yields the final power saving. A positive intermediate gain can be useful even if insufficient, but its remaining deficit must be stated.

**Completion criterion:** either a proved structural lemma with an explicit quantitative contribution, a complete proof of the quartic target, or a rigorously scoped obstruction with its exact failed inequality. A conditional assertion that essentially assumes the desired image bound is not the structural milestone.

**Stopping rule:** keep the next investigation bounded to the C2 prompt's maximum of three serious structural-lemma attempts. Stop a branch if the fully charged rate is nonpositive and no specific remaining improvement is identified. Preserve useful partial results and unresolved assumptions.

## 4. Keep the Eisenstein norm as a separate conjecture track

The proposed target is

$$
\exists\varepsilon>0\quad\forall N_0\ge1\quad
\exists A\subset\mathbb R\text{ finite}:\quad
|A|\ge N_0,\qquad
|\{a^2+ab+b^2:a,b\in A\}|\le |A|^{2-\varepsilon}.
$$

The [nonsingular-quadratic note](../research/conjectures/nonsingular_quadratic_compression_conjectures.tex) motivates this through the Eisenstein norm. Its broader positive-definite and nonsingular quadratic conjectures are later questions, not established generalizations.

A bounded first study should identify an exact support structure obtained from the norm identity and test whether it can provide a gain compatible with a same-set construction. Any proposed use of ideals, units, or correlated residue conditions needs explicit carrier hypotheses and a complete cost calculation.

**Completion criterion:** a precise lemma or scoped obstruction for the canonical form, with all source dependencies stated. Do not describe the reported rank-one C0 result as covering this full-rank form. Check the conjecture note's literature and asymptotic claims separately before relying on them.

## 5. Use computation for a specific mathematical question

Each experiment should name the finite assertion or identity it tests, record its parameters, use exact arithmetic when possible, and distinguish exhaustive coverage from sampling. Preserve reproducible inputs and explain the result's scope.

Useful checks include coefficient identities, fixed finite-field support counts, fiber sizes, and exact candidate inequalities. Avoid repeating the already proved $p=5,d=2$ test as a research milestone. Experiments on unrelated number fields cannot substitute for estimates in the required growing-degree family.

**Completion criterion:** each computational result has an auditable mathematical interpretation. No finite experiment is used to establish an asymptotic construction, arbitrary-prime theorem, or external novelty.

## 6. Review proof status and literature separately

A mathematical review should check fixed coefficients and exponent, the same input set in both coordinates, full Cartesian-square coverage, source compatibility, and every exponential cost. It should specifically inspect lightly represented outputs: collision energy alone is not a full-support upper bound.

Use claim-level statuses such as:

| Status | Meaning |
| --- | --- |
| Reported result | Asserted or reviewed in an archived source; the complete derivation has not been reconstructed here. |
| Proved with stated dependencies | A complete derivation is available and all external inputs are identified. |
| Conditional theorem | A complete implication under explicit unproved assumptions. |
| Computational evidence | A reproducible finite or sampled result with its scope stated. |
| Certificate obstruction | A specified counting method cannot give the required saving. |
| Open in this record | No proof or refutation is supplied in the inspected material. |

Literature verification is a separate future task. It should check the precise theorem, hypotheses, and publication status against original sources. Until that work is complete, retain: **External novelty and literature status have not been checked.**
