# Phase C0 — Conjecture Synthesis and Proof Search

## 1. Assignment and target

Conduct a focused offline research run that moves beyond the supplied Phase B mechanisms toward an explicit polynomial-image compression result. Generate a small number of serious conjectures, select the strongest, and attempt a complete proof. Use coordinated multiple subagents when available, following Section 4.

The target is one fixed, explicit polynomial \(P\in\mathbb R[x,y]\), genuinely depending on both variables, and one constant \(\varepsilon>0\) such that

\[
\forall N_0\ge 1\quad\exists A\subset\mathbb R\text{ finite},\qquad
|A|\ge N_0,\qquad |P(A,A)|\le |A|^{2-\varepsilon},
\]

where \(P(A,A)=\{P(a,b):a,b\in A\}\).

The same set must occur in both inputs. A construction for two unrelated sets \(A,B\) does not establish the target. A sequence of cardinalities tending to infinity suffices; do not silently strengthen the target to every cardinality or every finite set.

Prefer a polynomial outside the additive and multiplicative forms

\[
P(x,y)=g(u(x)+v(y)),\qquad P(x,y)=g(u(x)v(y)),
\]

with univariate real polynomials \(g,u,v\). Explain and prove the claimed exclusion. For an explicit family, state whether \(\varepsilon\) depends on the fixed member or is uniform over the family; do not claim uniformity without proof.

The research sequence is:

\[
\text{concrete conjecture}
\longrightarrow\text{proof obligations}
\longrightarrow\text{complete proof attempt}
\longrightarrow\text{independent audit}
\longrightarrow\text{targeted mutation if needed}.
\]

Do not stop at brainstorming while a concrete proof route remains available. Do not manufacture a proof to satisfy the assignment.

## 2. Offline environment and source integrity

Use no internet during this run. Do not browse, search arXiv, retrieve papers, use remote research services, install packages from the network, or delegate internet use to another agent. Local computation with available tools is allowed.

Use only the supplied project files, standard mathematical knowledge already available internally, and arguments developed during this run. An external paper named in a supplied file is not automatically an independently checked source. Cite the supplied document that actually contains the statement you use. If an original paper is also supplied, inspect its relevant statement directly.

External novelty cannot be established offline. Describe a candidate as **apparently new relative to the supplied project sources** or **a project conjecture whose external status has not been checked**. Do not assert that nobody has proved it, that it is globally new, or that an open problem has been solved.

Read these five core files in full before selecting candidates:

1. `PHASE_B_STATE.md`
2. `POLYNOMIAL_MECHANISM_LIBRARY.md`
3. `OPEN_LEMMAS_B.md`
4. `FAILURE_LIBRARY_B.md`
5. `COLLISION_LIBRARY.md`

Use these supporting references at the points where their lemmas are needed:

- `Phase_B_Abstraction_Cycle_2_Local_to_Global.pdf`
- `Phase_B_Abstraction_Cycle_1.pdf`
- `Phase_A_Sum_Product_Reproduction_FINAL_FROZEN.pdf`
- The supplied unit-distance proof, human-verified remarks, and any frozen study guide.
- `unit-distance-cot.pdf` for discovery context only, not as proof authority, following the Cycle 2 source hierarchy.

Locate files by name within the supplied attachments and project references; do not assume a particular machine's temporary attachment paths. Produce a source manifest showing what was actually read. If a source is missing, record the missing dependency and continue with supported work; do not reconstruct its supposed contents from memory or imply that it was inspected.

All supplied sources are read-only. Do not edit, rename, move, delete, or overwrite files under `sources/`, frozen PDFs, or the supplied Phase B Markdown files. Put research outputs and proposed updates in a separate `phase_c0/` directory. If a source claim fails a relevant check, preserve the original and record the discrepancy separately.

Phase A and Phase B remain the starting record. Their earlier recommendation to conduct a literature review is superseded for this run by this explicit, bounded, offline Phase C0 assignment.

## 3. Verified starting mechanisms and quantitative ledger

Use the following statements with their actual hypotheses. A project label of “validated” does not waive checking that a new application satisfies those hypotheses.

### 3.1 Source map

| Source location | Starting point to preserve |
|---|---|
| `PHASE_B_STATE.md`, validated principles 1–3 | Collision energy is diagnostic; exact factor-through and coordinate arguments must charge multiplicities. |
| `PHASE_B_STATE.md`, principles 4–7 | Uniform residue-class packing, split-prime amplification, signed rate, and the degree-density test. |
| `PHASE_B_STATE.md`, principle 8 and current bottleneck | A sparse integral deformation must return to one fixed polynomial with controlled maps. |
| `POLYNOMIAL_MECHANISM_LIBRARY.md`, mechanism rows | Distinguish validated mechanisms with hypotheses from the unresolved rank-two mechanism. |
| `OPEN_LEMMAS_B.md`, O1–O7 | Candidate supply, removable deformation, higher degree, prescribed splitting, prime powers, correlated sums, and carrier geometry remain separate obligations. |
| `FAILURE_LIBRARY_B.md`, F1–F10 | Use the recorded failures as mandatory tests of each proposed route. |
| `COLLISION_LIBRARY.md`, entries 5–7 | Preserve the mixed cubic obstruction and the known quadratic deformation as benchmarks. |
| Cycle 2 PDF, Sections 4–11 | Field supply as reported, carrier bounds, class packing, full support count, rate, and rescaling. |
| Cycle 2 PDF, Sections 12–13 and 17 | Nonspecialness, the cubic stress test, and open lemmas. |

### 3.2 Collision energy is not an upper bound

For \(n=|A|\),

\[
E_P(A)=\#\{(a,b,c,d)\in A^4:P(a,b)=P(c,d)\},
\qquad |P(A,A)|\ge\frac{n^4}{E_P(A)}.
\]

Large energy is necessary for compression, but does not certify a small image. Every surviving proof must control the full support, including outputs with small fibers.

For exact factor-through compression with a parameterization of maximum multiplicity \(\mu\), the library charges a factor \(\mu^2\) in the normalized support ratio. Record domains, fibers, and all analogous losses explicitly.

### 3.3 General local-to-global certificate

Reserve \(\varepsilon\) for the final power saving and \(\gamma\) for the output exponent before local savings. This avoids the earlier use of \(c\) for two different quantities.

Suppose all necessary fiber costs are included and, as field degree \(d\to\infty\),

\[
e^{ad-o(d)}\le |A_d|\le e^{Bd+o(d)},\qquad 0<a\le B,
\]

the allowed output classes modulo a fixed integer \(R\) satisfy

\[
|\Omega_d|\le e^{(\log R-s)d+o(d)},
\]

and every class contains at most \(e^{ud+o(d)}\) points in the output region. Then, with \(\gamma=\log R+u\),

\[
|P(A_d,A_d)|\le e^{(\gamma-s)d+o(d)},
\qquad
\frac{|P(A_d,A_d)|}{|A_d|^2}
\le e^{-\kappa d+o(d)},
\qquad \kappa=2a-\gamma+s.
\]

This certificate yields a power saving if \(\kappa>0\). For any fixed

\[
0<\varepsilon<\frac{\kappa}{B},
\]

it gives \(|P(A_d,A_d)|\le |A_d|^{2-\varepsilon}\) for all sufficiently large degrees in the construction. Explain absorption of the error terms. A nonpositive value means this particular certificate does not prove a saving; it does not disprove the conjecture.

### 3.4 Explicit box certificate

For a totally real field \(K\) of degree \(d\), write \(\Delta_K\) for its absolute discriminant and assume \(\Delta_K^{1/d}\le D\). Define

\[
B_K(X)=\{\alpha\in\mathcal O_K:|\sigma_i(\alpha)|\le X\text{ for every }i\}.
\]

The supplied framework gives

\[
\left(\frac{X}{\sqrt D}\right)^d
\le |B_K(X)|\le(2X+1)^d.
\]

Use a fixed \(X>\sqrt D\) to ensure unbounded carrier size. Check the underlying lattice argument, including the distinction between a translated box and the centered carrier.

For integer \(R\ge1\), every class modulo \(R\mathcal O_K\) has at most

\[
\left(\frac{2M}{R}+1\right)^d
\]

points in a radius-\(M\) box. The reason is norm separation: two distinct congruent points differ by \(R\beta\), and a nonzero algebraic integer \(\beta\) has at least one conjugate of absolute value at least one.

For an integral polynomial \(F\), suppose every output on \(B_K(X)^2\) lies in \(B_K(M)\), and its reductions occupy at most \((\rho R)^d\) classes. Then

\[
|F(B_K(X),B_K(X))|\le[\rho(2M+R)]^d,
\]

so the normalized bound is

\[
\frac{|F(B_K(X),B_K(X))|}{|B_K(X)|^2}
\le\Theta^d,
\qquad
\boxed{\Theta=\frac{\rho D(2M+R)}{X^2}<1.}
\]

The generic bound \(M=HX^m\), for degree \(m\), coefficient \(\ell_1\)-height \(H\), and \(X\ge1\), gives

\[
\Theta_{\mathrm{generic}}=
\rho D\left(2HX^{m-2}+\frac{R}{X^2}\right).
\]

Use the sharper shape-dependent \(M\) whenever available. Failure of the crude height bound alone is not grounds to discard a candidate.

With exact bounds and \(\Theta<1\), the conversion is

\[
\varepsilon=\frac{-\log\Theta}{\log(2X+1)}>0.
\]

If additional constants or error terms remain, take a smaller positive exponent and justify it.

### 3.5 Splitting and parameter dependence

Complete splitting gives

\[
\mathcal O_K/p\mathcal O_K\cong\mathbb F_p^d.
\]

A reduced image of density at most \(q_p\) therefore gives an allowed product set of density at most \(q_p^d\). For a squarefree modulus \(R=\prod_{p\in S}p\), CRT gives

\[
\rho=\prod_{p\in S}q_p,\qquad |\Omega_d|\le(\rho R)^d.
\]

“Independent” here means Cartesian-product decomposition of quotient rings, not probabilistic independence. Surjectivity of the carrier onto every residue coordinate is not needed for an upper bound, but any claimed equality requires its own justification.

The Cycle 2 report states a supply of totally real fields of unbounded degree, bounded root discriminant, and an infinite fixed set of odd primes splitting completely throughout. It does **not** supply arbitrary prescribed-prime compatibility: that is O4. Nor does an unspecified infinite split set automatically intersect a candidate's special congruence class in sufficiently many primes.

Prefer candidates sparse at every odd prime outside finitely many explicit exceptions, so the supplied split set can be used directly. Otherwise state and prove the required compatibility, or isolate it as an assumption. Track any dependence of \(D\) on a changed field construction or imposed split set.

Fix the field-supply data and all finite choices before \(d\to\infty\): polynomial or family member, primes, deformation parameter \(Q\), modulus \(R\), coefficient height, carrier scale \(X\), and maps. Distinguish \(Q\) from \(R\) unless they coincide. If considering more primes, recompute all costs jointly. Never shrink \(\rho\) while silently holding a dependent cost fixed.

### 3.6 Fixed-polynomial transport

The standard route requires an integral model \(P_Q\) and affine bijections \(\tau_Q,\eta_Q\) such that

\[
P_Q(\tau_Q(x),\tau_Q(y))=\eta_Q(P(x,y)).
\]

Given a real carrier \(A_0\), set \(A=\tau_Q^{-1}(A_0)\). Both input and output cardinalities are preserved. Use the **same** input map in both coordinates. Independent affine changes or arbitrary invertible changes mixing \(x,y\) do not automatically preserve a Cartesian square.

For rational coefficients, clear denominators and track bad primes and scaling. For other real coefficients, justify the coefficient field, reductions, integrality, and the embedding used; do not apply rational-coefficient identities without checking them. Any alternative transport must prove its domain and fiber bounds.

### 3.7 Benchmarks, not final discoveries

The known example is

\[
f=x+y+(x-y)^2,\qquad f_Q=Q(x+y)+(x-y)^2,
\qquad f_Q(Qx,Qy)=Q^2f(x,y).
\]

For odd \(p\mid Q\), its deformation has density \((p+1)/(2p)\). The supplied shape bound yields \(\theta=13D\rho<1\) after appropriate fixed choices. The original \(f\) is nevertheless surjective modulo every odd prime. Thus full local image of the original polynomial is not a rejection test for a useful deformation.

Do not present this example, its affine/scalar renaming, variable swap, or an immediate univariate postcomposition as the main research advance. If a candidate is an extension of it, identify precisely what additional lemma or family classification is being proved.

Keep \(h(x,y)=xy(x+y)\) as an adversarial benchmark. The supplied collision library records, on the benchmark progression \(A=\{q^0,\ldots,q^{N-1}\}\) with integer \(q\ge3\),

\[
|h(A,A)|=\frac{N(N+1)}2,\qquad E_h(A)=2N^2-N,
\]

and local image sizes \(1\) at \(p=2\), \(5\) at \(p=7\), and \(p\) at every other prime. Do not repeatedly retry the failed full-box, one-prime route. Prime powers, a different carrier, or rank-two control require genuinely new arguments.

## 4. Coordinated multiple-subagent workflow

You are explicitly authorized to use multiple subagents for this research run. Use them for independent, bounded work with a clear mathematical output, within the environment's concurrency limits. Do not create separate user-facing tasks merely to implement subagent work. If subagents are unavailable, perform the same roles sequentially and report that limitation honestly.

The lead agent owns candidate selection, notation, dependency tracking, final synthesis, and acceptance of claims. Subagent agreement is not proof.

| Role | Bounded responsibility | Required handoff |
|---|---|---|
| A — Conjecture and algebra | Explicit candidates, deformation identities, equivalence and nonspecialness tests; primarily O2. | Candidate cards, coefficient checks, and exact unresolved algebraic claims. |
| B — Finite-field analysis | Prove local value-set bounds and audit exceptional primes or lifting; O1 and O5. | Exact hypotheses, proofs or certified finite computations, density bounds, bad-prime list. |
| C — Number fields and packing | Check supplied field theorems, splitting, discriminant, carrier size, and per-class counts; O4 and O7. | Source locators, applicability audit, and any missing field-supply hypothesis. |
| D — Rate optimization | Track all dependencies and find a rigorous positive-rate parameter choice; O3. | Complete gain/cost ledger, parameter order, and a proved bound or explicit failed inequality. |
| E — Proof synthesis | Assemble accepted lemmas into a dependency-complete proof for a selected candidate. | Theorem statement, numbered proof, exponent conversion, and gap list. |
| F — Independent referee | Try to invalidate the selected statement and proof; use F1–F10 and Section 8. | Severity-ranked objections, resolutions, and verdict. |

These are roles, not a requirement to run six agents simultaneously. The lead may perform synthesis and rate work. With three available worker slots, for example, start A, B, and C alongside useful lead work; assign D and E once candidate data exist; reserve a later independent pass for F.

Coordinate in stages:

1. The lead reads the core sources, prepares a shared notation sheet, source manifest, and initial candidate IDs.
2. Give each worker the offline restriction, relevant source files, exact question, fixed assumptions, and required handoff. Avoid overlapping file edits and uncontrolled recursive delegation.
3. Before expensive proof work, hold an integration checkpoint: agree on one version of \(P,P_Q,Q,R,S,D,X,M,\rho\), the target inequality, and which lemmas remain unproved.
4. Each handoff must distinguish `SOURCE`, `PROVED HERE`, `STANDARD FACT`, `COMPUTATIONAL EVIDENCE`, `CONJECTURE`, and `GAP`. Include source section locators and full proof details for load-bearing claims. An uncertain remembered theorem is a gap until justified.
5. The lead independently verifies the deformation identity, CRT argument, carrier and packing estimates, dependence ledger, and exponent conversion. Do not paste incompatible agent arguments into one proof.
6. Give the referee the precise claim, proof, sources, and ledger. Resolve disagreements by a derivation, counterexample, or explicit remaining gap, never by majority vote.

Workers may write separate notes under `phase_c0/agents/`. Only the lead edits consolidated outputs. Maintain a compact shared claim ledger with claim ID, candidate version, owner, hypotheses, dependencies, source/proof location, status, and referee resolution. Recheck dependent claims after any mutation.

## 5. Generate and screen 3–6 serious candidates

Produce 3–6 explicit candidate cards, without padding the list with renamings. Identify the relevant open lemma O1–O7 for each. If the source constraints leave fewer credible candidates, explain why rather than inventing plausibility.

Each card must state:

1. The fixed polynomial or precisely defined family and the full compression conjecture.
2. Why it is not an immediate known example, special group form, or transport/postcomposition corollary.
3. The full-support mechanism and proposed carrier.
4. An explicit deformation and transport identity, if used.
5. Local image bounds, good and bad primes, and what is proved versus expected.
6. Split-prime availability and any unproved compatibility requirement.
7. The output radius, coefficient and modulus costs, and input-size bounds.
8. A preliminary signed-rate inequality with all dependencies visible.
9. The largest unresolved proof obligation and the quickest meaningful falsification test.

Search in this order:

- **Quadratic families:** Start with \(ax^2+bxy+cy^2+dx+ey+r\). Examine which homogeneous quadratic parts become sparse after lower-degree terms vanish modulo selected primes. Classify promising degeneracies without assuming every quadratic works. Check coordinate changes against the same-set requirement.
- **Removable deformations:** Solve the coefficient identities for \(P_Q(\tau_Qx,\tau_Qy)=\eta_Q(P(x,y))\). Determine which coefficient-weight patterns permit local simplification at acceptable global cost.
- **Higher degree:** Confront the factor \(X^{(m-2)d}\) explicitly. Proceed only with a concrete improvement in local density, output geometry, or carrier structure.
- **Alternative mechanisms:** O5–O7 or the O6 rank-two route are allowed when a specific new lemma addresses a recorded obstruction. Replace the box certificate with a proved appropriate certificate; do not impose local sparsity on a route whose gain comes from another mechanism.

Score each candidate from 0–5 for explicitness, local sparsity or alternative support gain, fixed-polynomial transport, archimedean efficiency, field-supply compatibility, positive-rate plausibility, substantive extension beyond known examples, and proof tractability. Give a total out of 40, with a short justification. Scores prioritize effort; they do not validate mathematics.

Reject a proposed route when its required transport fails, fibers are uncontrolled, its only purported gain is absent, or its actual best justified ledger is nonpositive with no identified improvement. A local-density route with \(\rho=1\) has no local gain; an alternative route may still be viable. Do not reject solely because the original polynomial has full finite-field image or because a crude bound fails.

Select at most two candidates for sustained proof attempts, with one primary candidate. State the primary as **PROJECT CONJECTURE C1**, including: “External novelty and literature status have not been checked in this offline run.”

## 6. Attempt a complete proof

For the primary candidate, write a short motivation connecting polynomial structure to a full-support bound, then prove the following obligations. Adapt the lemma architecture explicitly if using another mechanism.

1. **Algebra and nontriviality.** Prove the deformation identity coefficient by coefficient, integrality conditions, nonspecialness where claimed, and the precise relationship to known examples.
2. **Local images.** Prove the required value-set bounds at every selected prime. Count zero and exceptional characteristics correctly. For prime powers, prove the lifting bounds and analyze ramification; do not raise a mod-\(p\) density to a power without justification.
3. **Field supply.** State exactly which fields, split primes, and discriminant bound are required. Give a source locator and check hypotheses, prove the new statement, or mark it as an explicit assumption. Do not silently strengthen the supplied tower result.
4. **Carrier growth.** Define the carrier and prove both size bounds. Justify centered or translated windows, nonemptiness, unbounded size, embedding injectivity, and any fiber losses.
5. **CRT amplification.** Specify the quotient rings, comaximal factors, and number of allowed output classes. Prove the product-density upper bound.
6. **All-conjugate output bound.** Bound every embedding of every output. Use polynomial shape to sharpen \(M\). Include coefficient growth, translations, denominators, and all exceptional components.
7. **Uniform packing.** Prove a worst-case bound for every relevant residue class. Do not assume equidistribution or multiply density by an unrelated total point count.
8. **Full-support count.** Multiply the number of allowed classes by the maximum points per class. State the exact normalized inequality, with no omitted exponential factors.
9. **Positive rate and parameter order.** Prove \(\Theta<1\) or \(\kappa>0\) using a legitimate fixed parameter choice. Prove simultaneous satisfiability of all constraints; a numerical guess is insufficient. Explain when each parameter is selected and what depends on it.
10. **Return to the fixed polynomial.** Apply the real embedding and transport maps to obtain the same input set in both coordinates. Prove \(|A|\to\infty\), derive a symbolic positive \(\varepsilon\), and justify the exact target inequality for arbitrarily large sets.

Maintain a table of every parameter, its dependencies, its gain or cost, and the point where it is fixed. Retain any multiplicative constant until it is explicitly absorbed.

For each lemma use one status: `PROVED FROM SUPPLIED SOURCES`, `PROVED HERE`, `ASSUMED — EXACT STATEMENT GIVEN`, or `OPEN / FAILED ATTEMPT`. A complete-looking proof with an open dependency is not unconditional.

## 7. Computation policy

Use local symbolic calculations, finite-field enumeration, and small carrier experiments to check identities, reject candidates, or guide bounds. Keep scripts and reproducible inputs when they contribute to a conclusion.

Separate evidence from proof. Testing many primes does not prove a statement for infinitely many primes. Exhaustive exact enumeration may certify a finite value-set claim for a specifically fixed prime if the algorithm and coverage are auditable. It does not establish the required field supply or asymptotic support estimate. Floating-point parameter optimization suggests choices; rigorous inequalities must validate them.

Never treat failure to find small images in a finite experiment as a disproof of the existence of arbitrarily large favorable sets.

## 8. Independent adversarial audit

After each serious proof attempt, have the referee actively search for failure. Check at least:

- Is the final polynomial fixed, with fixed coefficients, and is the exponent independent of set size?
- Do the maps preserve a Cartesian square and the claimed cardinalities?
- Is the candidate only a known example under a permitted transformation or simple postcomposition?
- Are reductions defined over the stated rings, with denominators and bad primes handled?
- Are selected primes actually available in the same field family, and is complete splitting proved?
- Is an infinite split set being incorrectly treated as a prescribed split set?
- Are local image bounds rigorous, including zero, exceptional primes, and lifting?
- Does CRT provide the asserted coordinates without probabilistic assumptions?
- Are all conjugates controlled, with a uniform bound in every residue class?
- Has a translated lattice count been incorrectly used as a centered count?
- Are input cardinality, fiber, discriminant, coefficient, modulus, and geometry costs all charged?
- Is the rate strictly positive under one simultaneous, fixed choice of parameters?
- Does the exponential-to-power conversion use the input **upper** bound in the correct direction?
- Are uncertain remembered theorems, source gaps, or computational evidence being used as proof?
- Is the result stronger than its hypotheses justify, or is a conjectured lemma merely the desired theorem restated?

For each objection give its mathematical significance and one disposition: resolved by proof, requires an explicit assumption, invalidates this route, or refutes the statement. Repeat relevant checks after a repair.

## 9. Bounded mutation loop and honest status

If an attempt fails, preserve it and identify its dominant obstruction. Mutate only one or two components at a time: polynomial coefficients, deformation, local map, finite prime set, carrier geometry, output estimate, prime-power level, or transport map. Explain which failed inequality or lemma the mutation repairs and which dependencies must be rechecked.

Use versioned candidate IDs, such as C1.1 and C1.2. Run at most **six serious conjecture-and-proof iterations total**, including mutations, with at most two candidates receiving sustained effort at once. Do not restart the budget by renaming candidates.

Classify the strongest result as exactly one of:

- **PROVED WITHIN THE OFFLINE SOURCE SYSTEM:** All load-bearing steps follow from checked supplied statements, explicitly stated standard mathematics, or complete derivations in this run. Report: “The statement has been proved within the current offline source system. Its external novelty and literature status remain unverified.”
- **CONDITIONAL:** A complete implication has been proved under precise, substantive additional assumptions. List every assumption, preferably isolate one dominant missing lemma, and explain why it is not just the target restated. Do not hide several gaps behind one label.
- **PLAUSIBLE BUT OPEN:** An explicit conjecture survives the available tests, but the proof still contains unresolved steps. Identify exactly which ones.
- **NO VIABLE CANDIDATE FOUND:** The explored candidates or routes do not yet justify a credible target. Preserve the strongest obstruction and proved intermediate results.

For individual attempts distinguish **ROUTE FAILED** from **CONJECTURE REFUTED**. A failed estimate, full local image, or failed proof attempt does not refute the conjecture. Refutation requires a logically sufficient counterargument to its quantifiers.

If no full proof survives, extract the strongest correct partial theorem or conditional implication. Do not inflate an elementary corollary into a research breakthrough.

## 10. Deliverables and readability

Produce a consolidated, self-contained report at:

`phase_c0/Phase_C0_Conjecture_Proof_Search.md`

Also produce `phase_c0/Phase_C0_Conjecture_Proof_Search.pdf` if local PDF creation is available. Render and inspect it for readable mathematics, unclipped tables, and complete pages. If PDF tooling is unavailable offline, deliver the complete Markdown and state that limitation without downloading tools.

The report must include:

1. **One-page result:** The exact best polynomial/conjecture, quantifiers, proof status, symbolic exponent if established, substantive extension over the known example, and any indispensable assumption.
2. **Source manifest:** Files actually read, source locators for imported lemmas, missing materials, and relevant discrepancies. Distinguish supplied-report reliance from direct primary-source verification.
3. **Candidate comparison:** The 3–6 cards or justified smaller list, scores, and selection decisions.
4. **Complete derivation:** Numbered lemmas, full proofs of successful steps, parameter ledger, fixed-polynomial transport, and exponent conversion.
5. **Proof dependency diagram:** Show the chain from \(P\) through deformation, local images, field supply, packing, support count, and \(|A|^{2-\varepsilon}\). Mark every assumed or open arrow visibly.
6. **Referee report:** Serious objections and their resolutions or surviving gaps.
7. **Failure and mutation history:** Preserve exact obstructions and distinguish route failures from refutations.
8. **Mechanism progress:** State which of O1–O7 were resolved, narrowed, or unchanged, and what has been proved beyond the supplied examples.
9. **Next bottleneck:** State one prioritized mathematical lemma with explicit hypotheses and conclusion, while retaining the full remaining-gap list elsewhere.

Use clear prose around formulas. Define symbols before use, explain why each lemma is needed, and follow major calculations with a brief explanation of what the bound controls. Keep theorem statements separate from motivation and empirical evidence. Do not compress the central argument into phrases such as “standard counting gives” or “many primes compensate.”

Write supporting ledgers as needed:

- `phase_c0/SOURCE_MANIFEST.md`
- `phase_c0/CLAIM_LEDGER.md`
- `phase_c0/CANDIDATE_LEDGER.md`
- `phase_c0/REFEREE_REPORT.md`

Place proposed Phase B updates in `phase_c0/proposed_updates/`, with one clearly marked proposed update corresponding to each of the five core Markdown sources. State additions and status changes precisely; do not silently rewrite the frozen record or mark an open lemma solved by a conditional argument. Preserve useful local computation under `phase_c0/experiments/`.

End with the exact status, the strongest established conclusion, and the remaining mathematical bottleneck. Stop after the bounded research run and its deliverables; do not begin an external novelty search or another phase.

## Begin

Read and map the core Phase B sources, initialize the coordinated research roles, and generate the candidate cards. Select the strongest candidate using a full-support mechanism and a plausible positive-rate ledger. Attempt its proof, subject it to independent attack, and repair or mutate only in response to a specific mathematical obstruction. Remain offline throughout.
