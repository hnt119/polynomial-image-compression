# Phase C2 — A Structural Lemma for a Hybrid Carrier

## 1. Assignment and required milestone

Preserve the corrected C0 quadratic theorem and the main C1 obstruction results. Incorporate the two elementary roadmap corrections in `Phase_C1_Review_and_Next_Steps.md`. Then investigate the previously untested carrier

\[
\boxed{C_j=G_jT_j,}
\]

where \(G_j\) is a precisely defined finite set of units and \(T_j\) is a precisely defined additive carrier in the same totally real number field.

The long-term target remains the fixed polynomial

\[
P_4(x,y)=(x+2y)^4+3x-y
\]

and a fixed \(\varepsilon>0\) such that, for every \(N_0\), there is a finite \(A\subset\mathbb R\) with

\[
|A|\ge N_0,\qquad |P_4(A,A)|\le |A|^{2-\varepsilon}.
\]

The same set must occur in both inputs. An unbounded sequence of sizes suffices.

**The immediate C2 milestone is one proved structural lemma that supplies a quantified improvement relevant to this target.** Define the actual carrier, expand the polynomial, identify a specific correlated support, and calculate whether the proposed gain can pay every cost. If a complete proof becomes available, finish it. If no useful lemma survives, report that honestly with the exact obstruction.

Do not spend this run generating another broad list of polynomials. Do not make “prove QCLASS-DEFICIT” the whole assignment. A new name for the desired image bound, or a conditional theorem that assumes essentially that bound, does not meet the milestone.

## 2. Offline scope, sources, and preservation

Remain offline. No browsing, paper retrieval, remote research services, or network installation is allowed, including through subagents. Available local computation may support the work.

Read the following current records:

- `Phase_C1_Review_and_Next_Steps.md` — required; contains the two elementary corrections.
- `Phase_C0_Corrected.md` and its PDF where available.
- `Phase_C1_Higher_Degree_Proof_Search.md` and its PDF where available.
- `C0_CORRECTION_LOG.md`.
- `CLAIM_LEDGER_C1.md`.
- `REFEREE_REPORT_C1.md`.
- `SOURCE_MANIFEST_C1.md`.
- `model2_local_classes.py` only if its finite checks are relevant; it is not proof authority.

Consult these older references for the exact lemmas needed:

- `Phase_A_Sum_Product_Reproduction_FINAL_FROZEN.pdf`, especially definitions of the additive and unit carriers, unit counts, directness, regulator bounds, distortion, and parameter order.
- `Phase_B_Abstraction_Cycle_1.pdf` and `Phase_B_Abstraction_Cycle_2_Local_to_Global.pdf`.
- `PHASE_B_STATE.md`, `POLYNOMIAL_MECHANISM_LIBRARY.md`, `COLLISION_LIBRARY.md`, `FAILURE_LIBRARY_B.md`, and `OPEN_LEMMAS_B.md`.
- The supplied unit-distance proof, Proposition 3.8 and Remark 3.9, when invoking the split-prime tower.

Create a concise manifest of what was actually read. A source lemma about one collection of fields cannot automatically be combined with a lemma about another collection. Verify that unit counts, regulator estimates, splitting, and discriminant control hold simultaneously in the chosen fields.

If a necessary source is absent, identify the missing dependency and continue with algebra or other supported work. Do not reconstruct supposed source statements from memory or claim source verification without inspection.

All supplied files and synced project sources are read-only. Write only new work under `phase_c2/`. Do not rewrite or re-audit all frozen phases. Record necessary status corrections in a short addendum.

External novelty and literature status remain unchecked. A proof developed here may be described as proved within the supplied offline source system, without claiming a globally new theorem.

## 3. Stage A — Reconcile the research state

### A1. Preserve the established results

The corrected C0 theorem covers

\[
P_2(x,y)=(ax+by)^2+cx+ey,
\qquad \gcd(a,b)=1,\quad ab(ae-bc)\ne0,
\]

with integral coefficients and a member-dependent fixed power saving on arbitrarily large Cartesian squares. Preserve its scope and proof status.

C1 proves the quartic continuous-range and transverse-width lemmas, and obstructions for the specified interval-and-class-packing methods, including translated and anisotropic boxes. It also proves the local cost theorem for coordinate-product input restrictions. These are not lower bounds on the actual polynomial image.

The general quartic target, general correlated finite-field inequality, and strong output-specific deficit remain unresolved.

### A2. Incorporate the two elementary corrections

Read and independently verify the complete short proofs in `Phase_C1_Review_and_Next_Steps.md`.

1. **Weak M1-DEFICIT:** for a fixed \(r>\max\{Q,\sqrt D\}\), the width bound and the trivial pair bound already prove a positive deficit relative to the oversized ambient packing bound. Mark it `PROVED — INSUFFICIENT FOR THE REQUIRED RATE`. It needs no explicit tower enumeration.
2. **M2-CORR at \(p=5,d=2\):** when \(|S|\le12\), nonemptiness of the image suffices; when \(|S|\ge13\), the intersection argument gives \(S+2S=\mathbb F_5^2\). Mark this finite case proved. Do not run an exhaustive search over its subsets.

Preserve the distinction between those elementary results and the still-open general statements. Do not count their verification as the new structural milestone for C2.

### A3. Carry forward the correct obstruction

C1's transverse-width theorem says that, for a real interval \(I=[c-r,c+r]\) and

\[
F_Q(x,y)=(x+2y)^4+Q^3(3x-y),
\]

the continuous output width satisfies

\[
W_Q(c,r)+Q\ge Q(2r+1)^2
\qquad(Q\ge5).
\]

Consequently, placing any integral carrier inside a product of input intervals, allowing the full corresponding continuous output intervals, and using only the old residue envelope and norm-separation packing cannot supply the desired saving. Verify explicitly how this applies if \(C_j=G_jT_j\) is simply enclosed in another box.

The hybrid must contribute additional information about which outputs are realized. Its different parametrization alone does not escape C1.

## 4. Stage B — Define one actual hybrid carrier

Work in the totally real layers \(F_j\) of the supplied field construction, with

\[
d_j=[F_j:\mathbb Q]\to\infty,
\qquad \operatorname{rd}(F_j)\le D.
\]

Do not confuse these with the unit-distance source's CM fields \(F_j(i)\). If split primes are used, choose the fixed finite set supplied with the same tower, and put \(Q=\prod p\). Track the joint dependence of \(D\), the prime count, and the later parameters.

Begin with the concrete model

\[
G_j(Y)=\left\{g\in\mathcal O_{F_j}^{\times}:
\sigma_i(g)>0,\quad |\log\sigma_i(g)|\le Y\text{ for every }i\right\},
\]

and

\[
T_j(X,\tau)=X+B_{F_j}(\tau X),
\qquad
B_{F_j}(Z)=\{t\in\mathcal O_{F_j}:|\sigma_i(t)|\le Z\text{ for all }i\},
\]

where \(X\) is a positive integer and \(0<\tau<1\). Then

\[
(1-\tau)X\le\sigma_i(t)\le(1+\tau)X
\qquad(t\in T_j),
\]

so the additive carrier is positive and excludes zero.

This is a starting definition, not a claim that its unit count or directness already follows. Compare it carefully with the source's actual definitions. If a source-compatible alternative is necessary, such as a specified set of squared units or a separated subset, state the replacement exactly and charge its losses. Do not silently transfer a lower bound for all units to totally positive units.

Prove or isolate the precise needed estimates for:

- \(|G_j|\), \(|G_jG_j|\), and \(|G_j/G_j|\), insofar as the argument uses them;
- \(|T_j|\), including a justified centered carrier count;
- the maximum multiplicity
  \[
  \mu_j=\max_{c\in C_j}\#\{(g,t)\in G_j\times T_j:gt=c\};
  \]
- the regulator and discriminant costs behind any unit count;
- archimedean distortion and any congruence restrictions on the selected units.

Use

\[
\frac{|G_j||T_j|}{\mu_j}\le |C_j|\le |G_j||T_j|.
\]

Do not claim injectivity merely because the two sets are defined in different coordinates. If using the Phase A directness lemma, check its exact hypotheses and prove that this \(G_j,T_j\) satisfies them.

Fix all finite parameters before degree grows. Any exception requires a complete new asymptotic calculation and a fixed final exponent. The target polynomial may never vary with set size.

## 5. Stage C — Expand exactly and preserve correlations

### C1. Full expansion

Independently verify

\[
\begin{aligned}
F_Q(g_1t_1,g_2t_2)
={}&g_1^4t_1^4
+8g_1^3g_2t_1^3t_2
+24g_1^2g_2^2t_1^2t_2^2\\
&+32g_1g_2^3t_1t_2^3
+16g_2^4t_2^4
+Q^3(3g_1t_1-g_2t_2).
\end{aligned}
\]

The seven terms are coupled through the same four parameters. Bounds for their marginal supports cannot be multiplied or added and then described as a correlated saving without the resulting quantitative proof.

### C2. Ratio and common-action decomposition

For one layer suppress \(j\), put \(u=g_1/g_2\), \(v=g_2\), and define

\[
G(u)=\{v\in G:uv\in G\},\qquad u\in G/G.
\]

The admissible \((u,v)\) pairs are not the whole product \((G/G)\times G\). In particular,

\[
\sum_{u\in G/G}|G(u)|=|G|^2.
\]

Define the correlated carrier support

\[
\mathcal K_u=
\{((ut_1+2t_2)^4,\,3ut_1-t_2):t_1,t_2\in T\}
\]

and the evaluated support

\[
\mathcal S_u=
\{v^4\alpha+Q^3v\beta:
v\in G(u),\ (\alpha,\beta)\in\mathcal K_u\}.
\]

Verify the exact identity

\[
\boxed{F_Q(C,C)=\bigcup_{u\in G/G}\mathcal S_u.}
\]

The union bound \(\sum_u|\mathcal S_u|\) is legitimate but may be costly. Charge it. An improvement based on overlap between different \(u\) must prove control of the whole union; exhibiting a few overlaps is insufficient.

### C3. Mandatory elementary checks before proposing a lemma

Determine the fiber size of

\[
(t_1,t_2)\longmapsto((ut_1+2t_2)^4,3ut_1-t_2).
\]

The underlying linear map has nonzero determinant \(-7u\). Fourth powering has bounded fibers, and positivity in the starting model may make the pair map injective. Prove the precise conclusion. Do not claim that merely expressing \(\mathcal K_u\) as a parametrized surface makes it exponentially smaller than \(T^2\).

Likewise, \(v\mapsto(v^4,v)\) is injective. Its graph structure is a relation to exploit, not a cardinality saving by itself.

Finally, verify that the chosen units, their ratios, and all transformed carrier expressions stay in the stated fields and integral domains, and track their embedding bounds. Do not lose the dependence on \(u\) when claiming a uniform estimate.

## 6. Stage D — Propose and prove one useful structural lemma

Use the exact decomposition to identify the point at which there might be fewer distinct outputs than input parameter choices. Prepare at most two lemma cards. Each must contain:

1. An explicit mathematical statement about the chosen sets, maps, or supports.
2. Checkable hypotheses and a proof that the carrier satisfies them, or a clearly identified remaining hypothesis.
3. The concrete structure that could produce a saving: for example, an exact factor-through representation, a proved cover by quantitatively small supports, or a support-specific arithmetic restriction with a usable count.
4. The baseline estimate it improves, and the size of that improvement per degree.
5. The complete cost of applying it, including exceptional pieces and summation over ratios.
6. A short proof plan using named identities or source lemmas, not “exploit correlations.”

An assertion of the form “the outputs occupy exponentially fewer points” is only a target until a specific supporting structure and proof are supplied. A structural relation without a quantitative consequence also does not meet the milestone.

Possible proof forms include an explicit smaller intermediate support, a full-support cover, or a count over output classes that uses additional information about realized values. Do not require identical savings in every residue class if a proved total count or a controlled exceptional-class argument is stronger and easier to justify.

Collision energy is diagnostic only. A large average collision count cannot upper-bound the image. If a fiber argument is used, it must account for every output, including any exceptional or lightly represented values.

## 7. Measure gain against the actual input size

Maintain a ledger containing \(Q,D,X,Y,\tau\), all regulator and sign losses, all unit and carrier rates, \(\mu_j\), ratio counts, support-cover costs, and any local saving. Separate proved quantities from conjectured ones.

For example, if

\[
|G_j|\ge e^{g_-d_j-o(d_j)},\qquad
|T_j|\ge e^{t_-d_j-o(d_j)},\qquad
\mu_j\le e^{m d_j+o(d_j)},
\]

then a valid carrier lower rate is

\[
a=g_-+t_--m.
\]

Prove an upper rate \(|C_j|\le e^{Bd_j+o(d_j)}\), with \(0<a\le B\). If the full output support is bounded by \(e^{h d_j+o(d_j)}\), the required net rate is

\[
\boxed{\kappa=2a-h>0.}
\]

Equivalently, if a proved support lemma gives

\[
|F_Q(C_j,C_j)|
\le e^{-\lambda d_j+o(d_j)}|G_j|^2|T_j|^2,
\]

then multiplicity alone consumes up to \(2m\) of that gain, and the surviving rate is \(\lambda-2m\). This is an accounting template, not an acceptable substitute for proving the support lemma.

If the lemma improves only an intermediate bound, explicitly calculate the remaining deficit. Distinguish:

- a strict algebraic refinement with no exponential gain;
- a positive exponential gain that remains insufficient after costs;
- a positive net rate that proves the target.

If the net rate is positive, finish the proof using

\[
A_j=Q^{-1}\sigma_j(C_j),\qquad
F_Q(Qx,Qy)=Q^4P_4(x,y),
\]

and any fixed \(0<\varepsilon<\kappa/B\). Prove \(|A_j|\to\infty\), all-pairs coverage, and absorption of every error term. The same embedding and scalar map must serve both inputs.

## 8. Coordinated multiple subagents

You are explicitly authorized to use multiple subagents. Use bounded assignments, shared notation, and staged handoffs within the environment's concurrency limit. Do not create separate user-facing tasks for this internal work.

Suggested roles:

- **Carrier and source analyst:** inspect the exact Phase A unit and carrier lemmas; establish simultaneous field applicability, growth, and multiplicity estimates.
- **Algebra and support analyst:** verify the seven-term expansion, ratio decomposition, elementary fiber checks, and propose one concrete structural lemma.
- **Rate analyst:** independently charge every loss and test whether the proposed lemma could change the sign of the final rate.
- **Independent referee:** attack the selected proof after its hypotheses and parameters are fixed; this may be a later assignment when a worker slot becomes free.

The lead verifies the two roadmap corrections, owns model selection and synthesis, and independently checks every load-bearing identity and inequality. Subagent agreement is not proof.

Each handoff must include exact statements, hypotheses, source locators, full proofs or reproducible calculations, dependence on degree and parameters, and a precise status. Workers write separate notes; only the lead edits consolidated results.

At an integration checkpoint, agree on one exact version of \(G_j,T_j,Q,X,Y,\tau\) and the selected lemma. Resolve inconsistencies before undertaking a full proof. Never combine a count for one unit set with directness for another without a proof of compatibility.

## 9. Bounded search and stopping rule

After the short state-reconciliation step, allow at most three serious structural-lemma attempts, including repairs or changes of carrier parameters. Keep at most two lemma cards active. Retain the fixed quartic target during this run.

Use local symbolic or finite computations only when they address a specific remaining question. Screen proposed experiments for elementary proofs first. If explicit tower polynomials are missing, do not invent them or treat a sample unrelated field as representative of the whole tower.

Stop a branch when its only claimed improvement reduces to the old box certificate, uncontrolled fibers, marginal support multiplication, or a nonpositive fully charged rate with no named improvement left to test.

Do not force a success label. The possible final outcomes are:

- **TARGET PROVED WITHIN THE OFFLINE SOURCE SYSTEM.** Complete proof and fixed exponent.
- **USEFUL STRUCTURAL LEMMA PROVED.** Quantified improvement and its precise contribution to the rate; target still open if a deficit remains.
- **SCOPED OBSTRUCTION PROVED.** A specified structural approach or counting method cannot deliver the needed estimate; distinguish this from impossibility of the actual construction.
- **NO USEFUL LEMMA FOUND.** Preserve the exact attempts and gaps without presenting another restatement of the target as the achievement.

A conditional implication may be recorded, but a hypothesis containing the desired compression claim does not count as a useful proved structural lemma. If an intermediate hypothesis remains open, state all of it explicitly and explain why it is independently tractable, if there is evidence for that.

## 10. Final referee questions

Check especially:

- Do the unit bounds and split-prime properties hold in the same totally real fields?
- Were sign restrictions, squared-unit maps, regulator costs, and parameterization multiplicities charged?
- Is \(C_j\) truly large after all restrictions?
- Does the argument cover every pair in \(C_j\times C_j\), rather than only equal-unit pairs or another selected subset?
- Is the ratio decomposition exact, with the dependence between \(u\) and \(v\) preserved?
- Are correlations used by a proved counting step, rather than merely displayed?
- Does the alleged smaller support have exponentially smaller size, rather than a bounded-fiber reparametrization of the same set?
- Does the proof avoid falling back to the interval-and-class method already obstructed in C1?
- Are all exceptional classes, uncovered outputs, and union costs controlled?
- Is the new gain stronger than the trivial positive deficit identified in the C1 review?
- Is the final net rate strictly positive under one simultaneous valid parameter choice?
- Does the stated conclusion match exactly what was proved?

## 11. Deliverables

Keep the output focused on mathematical progress. Write under `phase_c2/`:

1. `C1_STATUS_ADDENDUM.md` — the two elementary corrections and preserved statuses; do not reissue every earlier report.
2. `Phase_C2_Hybrid_Carrier_Structural_Lemma.md` — exact carrier, source applicability, expansion, selected lemma, full derivation, complete rate ledger, and final status.
3. `CLAIM_LEDGER_C2.md` — proved, source-dependent, conjectural, rejected, and unresolved claims kept distinct.
4. `REFEREE_REPORT_C2.md` — substantive objections and their resolutions or surviving gaps.
5. A PDF of the main report if offline tools permit; render and inspect it. Complete Markdown is required even if PDF generation is unavailable.

Include a one-page opening summary answering:

- What exact structural lemma was proved, if any?
- What counting step uses it?
- What numerical or symbolic per-degree gain does it supply?
- What costs consume that gain?
- Was the quartic target proved? If not, what exact deficit or mathematical gap remains?

Explain formulas in plain mathematical prose. Avoid a long report whose only new content is a renamed conjecture. If no useful lemma is found, a concise rigorous failure report is preferable.

## Begin

Verify the two elementary roadmap corrections, preserve C0 and C1, and define a source-compatible unit-times-additive carrier. Coordinate subagents to establish its size and multiplicity, reconstruct the correlated support exactly, and prove one structural lemma with a measurable contribution to the rate. Remain offline and keep every supplied source unchanged.
