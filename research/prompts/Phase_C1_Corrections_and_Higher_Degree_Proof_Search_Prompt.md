# Phase C1 — Correct the Baseline and Test Higher-Degree Compression

## 1. Assignment

Continue from the completed Phase C0 report. First prepare a corrected, auditable version of its successful quadratic result. Then conduct a bounded proof search for a genuinely higher-degree extension, starting from the explicit quartic

\[
P_4(x,y)=(x+2y)^4+3x-y.
\]

The target remains

\[
\exists\varepsilon>0\quad\forall N_0\ge1\quad
\exists A\subset\mathbb R\text{ finite}:
|A|\ge N_0,\qquad |P_4(A,A)|\le |A|^{2-\varepsilon}.
\]

The polynomial and exponent must be fixed as the set sizes grow. The same set must appear in both inputs. An unbounded sequence of sizes suffices.

Do not begin another broad candidate-generation cycle. Concentrate on concrete constructions and the precise estimates they require. Do not stop after listing possible approaches while a specific proof calculation remains available.

Success may be a complete proof, a substantive conditional theorem, or a rigorous obstruction for a precisely defined construction or counting method. A failed estimate alone is not an impossibility theorem for the polynomial.

## 2. Environment and supplied sources

Remain offline. Do not browse, retrieve papers, use remote research services, or install tools from the network. This restriction applies to every subagent. Available local computation is permitted.

Supply and read these six C0 results:

- `Phase_C0_Conjecture_Proof_Search.md`
- `Phase_C0_Conjecture_Proof_Search.pdf`
- `SOURCE_MANIFEST.md`
- `REFEREE_REPORT.md`
- `CLAIM_LEDGER.md`
- `CANDIDATE_LEDGER.md`

Also consult the five Phase B Markdown records, the Cycle 2 report, and the original references needed by the selected arguments. In particular, the C0 field input is Proposition 3.8, properties P1–P4, and Remark 3.9 of the supplied unit-distance proof. Phase A supplies the earlier carrier arguments. The discovery transcript is not proof authority.

Record which sources were actually inspected. If a file is missing, continue with supported work and identify the missing dependency. Do not claim that a correction, source verification, or freeze is complete without the documents needed for it.

Treat all supplied files as read-only. Never overwrite frozen Phase A or B materials, synced files under `sources/`, or the submitted C0 results. Write corrected copies and new work under `phase_c1/`.

Do not assess external novelty from unfamiliarity. Keep literature verification as a separate later task. Use: “External novelty and literature status have not been checked.” The offline proof search need not wait for that later check.

## 3. The established C0 starting point

The reviewed C0 argument proves the following within the supplied source system:

For integral coefficients satisfying

\[
\gcd(a,b)=1,\qquad ab(ae-bc)\ne0,
\]

the fixed polynomial

\[
P_2(x,y)=(ax+by)^2+cx+ey
\]

has arbitrarily large finite real sets \(A\) with

\[
|P_2(A,A)|\le |A|^{2-\varepsilon_{P_2}}
\]

for some member-dependent \(\varepsilon_{P_2}>0\). The explicit example is
\((x+2y)^2+3x-y\).

The construction uses

\[
(P_2)_Q=(ax+by)^2+Q(cx+ey),
\qquad (P_2)_Q(Qx,Qy)=Q^2P_2(x,y),
\]

square images modulo fixed split primes, a Minkowski carrier, and a uniform count within every output residue class. It is an extension of the known quadratic mechanism. Do not relabel it as a new compression mechanism.

The field source supplies, for sufficiently large fixed \(\ell\),

\[
t=\left\lfloor\frac{(\ell-1)^2}{100}\right\rfloor
\]

fixed odd primes \(p_i\equiv1\pmod4\), totally real fields \(K_j\) of degrees tending to infinity, and a common root-discriminant bound \(D\) with

\[
\log D=O(\ell\log\ell).
\]

Every selected prime splits completely throughout the same tower. Check the source's notation: its totally real layers are denoted \(F_j\), while its \(K_j=F_j(i)\) are different fields. State explicitly if renaming the totally real layers. Do not accidentally use the complex extensions as totally real carriers.

No arbitrary prescribed-prime splitting theorem is being assumed.

## 4. Stage A — Correct and freeze C0

Perform a focused correction pass, not an unrestricted re-audit of all earlier phases.

### A1. Correct the radius terminology

The submitted bounds

\[
9X^2+4QX,
\qquad 81X^4+4Q^3X
\]

are valid bounding radii obtained by separate estimates. Calling them “exact” or “optimal” is not justified by that derivation.

Replace those labels with “valid upper bound,” or derive and prove the actual extremum. Distinguish an exact maximum over the continuous real square from the maximum over the algebraic carrier, which may be smaller.

For the quartic, useful checks are the four corner values and the fact that

\[
(u+2v)^4+Q^3(3u-v)
\]

is convex as a function of \((u,v)\). Account for its negative minimum when bounding absolute values. Do not assume that the maximum of an absolute value follows immediately from convexity of the polynomial itself.

There is no need to optimize the successful quadratic exponent merely to repair terminology. Its existing valid upper bound already proves the theorem.

### A2. Narrow the quartic failure claim

The C0 calculation establishes failure of its specified local-density-plus-uniform-packing certificate. It does not establish that the actual polynomial image is large, that every proof using the same carrier fails, or that different carrier geometry is mandatory.

Correct Sections 10, 12, and 13 and corresponding ledger entries wherever they exceed this scope. Replace the assertion that any positive answer must use new geometry with the alternatives actually left open: sharper support counting, additional residue information, a different deformation, a different carrier, or another proved mechanism.

### A3. Repair presentation and preserve provenance

Repair malformed formulas, including literal `qquad` text and extraneous punctuation in powers such as \(\mathbb F_p^d\). Retain the exact theorem hypotheses, same-set quantifiers, and distinction between a proved result and unchecked external novelty.

Write a correction log with original location, corrected claim, reason, and effect on the proof. If an unexpected substantive problem appears, isolate it and revise the status honestly. Otherwise produce a corrected C0 baseline marked **safe to freeze within the supplied source system**.

Do not let cosmetic polishing consume the research run.

## 5. Stage B — Establish the precise quartic baseline

Let

\[
L=x+2y,\qquad M=3x-y,
\qquad F_Q=L^4+Q^3M.
\]

Prove

\[
F_Q(Qx,Qy)=Q^4P_4(x,y).
\]

For a fixed squarefree product \(Q\) of the source's split primes,

\[
q_p=\frac{p+3}{4p},\qquad
\rho_4=\prod_{p\mid Q}q_p.
\]

Verify the local count, including zero, and CRT's upper bound of \((\rho_4Q)^d\) allowed classes. The carrier need not cover every residue class for this upper bound.

For the centered carrier

\[
B_K(X)=\{\alpha\in\mathcal O_K:|\sigma_i(\alpha)|\le X\text{ for all }i\},
\]

the existing estimates give

\[
\frac{|F_Q(B_K(X),B_K(X))|}{|B_K(X)|^2}
\le\Theta_4(X)^d,
\]

where

\[
\Theta_4(X)=D\rho_4
\left(162X^2+\frac{8Q^3}{X}+\frac{Q}{X^2}\right).
\]

Reconstruct why this displayed factor exceeds one for every \(X>0\): put \(z=X/Q\), compare \(162z^2\) and \(8/z\), and use

\[
\rho_4Q^2=\prod_{p\mid Q}\frac{p(p+3)}4\ge10^t.
\]

Then ask the narrower substantive question: does the obstruction persist when using the actual continuous output interval and its length, instead of the symmetric interval from the triangle inequality? Prove the answer for that specified certificate. Keep any resulting lower bound on the certificate separate from a lower bound on the actual image size.

The point of this stage is to determine what a successful next argument must improve. Identify the mathematical source of the loss, not merely the symbol in which it appears.

## 6. Stage C — Test explicit construction models

Prepare at most three construction cards and select at most two for sustained work. Each card must define an actual set or parametrization before claiming plausibility. A card saying only “find a better carrier” is invalid.

Use the following concrete starting models, adapting them only with a stated reason.

### Model 1: Translated and anisotropic additive boxes

Define

\[
C_d=\left\{\alpha\in\mathcal O_{K_d}:
|\sigma_i(\alpha)-c_{i,d}|\le X_{i,d}\text{ for all }i\right\}.
\]

Specify how the centers and radii are chosen. Prove input-size bounds rather than assuming every translate is dense. Bound the range of \(F_Q\) on each pair of identical coordinate intervals. Use interval lengths when sharper than symmetric radii.

Derive the corresponding product packing bound and compare it with the input-size estimate. Determine whether translation, unequal widths, or the sharper interval estimate can improve the rate enough. If the optimized certificate fails, state exactly which permitted choices and bounds the obstruction covers.

### Model 2: A box intersected with specified congruence classes

Define

\[
C_d=B_{K_d}(X)\cap
\{\alpha:\alpha\bmod\mathfrak m_d\in\Lambda_d\},
\]

or a precisely specified translated-box version. State the ideals \(\mathfrak m_d\), the input class sets \(\Lambda_d\), and their compatibility with the available fields.

Investigate whether restricting inputs creates a substantially smaller output class set. Charge the loss in input cardinality twice in the normalized image ratio. Prove lower bounds for the restricted input count; global lattice density does not automatically supply them for arbitrary classes.

If using powers of existing split primes, prove the required ring structure and lifting bounds. A mod-\(p\) saving does not automatically repeat at each power.

### Model 3: A specified multiplicative-action carrier

Start from a genuinely explicit version of

\[
C_d=G_dT_d,
\]

where \(G_d\) is a selected set of units and \(T_d\) is an additive carrier, both defined quantitatively using the supplied Phase A framework.

Expand \(F_Q(g_1t_1,g_2t_2)\). Identify the exact correlated intermediate support whose control would yield a gain. Track parameterization multiplicity and unit distortion. Do not multiply marginal component supports and then call the resulting estimate a correlated saving.

Before continuing, state one explicit new lemma about that support, with hypotheses that the chosen \(G_d,T_d\) satisfy. A lemma equivalent to the desired compression theorem is not progress.

### Construction-card requirements

For every tested model give:

1. The exact carrier and any transport maps.
2. Which C0 loss it is intended to improve.
3. The carrier-size lower and upper bounds, with proof status.
4. All local input and output restrictions.
5. An output container or another full-support description.
6. The per-class packing or replacement counting lemma.
7. A complete dependency and rate calculation.
8. The single first unproved statement and a concrete plan to prove or disprove it.

Use preliminary calculations to abandon a model promptly when its only proposed gain is demonstrably consumed by its costs. Record the obstruction and move to the next authorized model; do not merely rename the same set.

## 7. Rate, quantifier, and same-set requirements

For the general certificate, establish

\[
e^{ad-o(d)}\le |C_d|\le e^{Bd+o(d)},\qquad 0<a\le B,
\]

an allowed class bound

\[
|\Omega_d|\le e^{(\log R-s)d+o(d)},
\]

and at most \(e^{ud+o(d)}\) outputs in every relevant class. Include all fibers and input losses. The net saving is

\[
\kappa=2a-(\log R+u)+s.
\]

Only a proved \(\kappa>0\) gives a power saving from this certificate. With the full input upper bound, every fixed \(0<\varepsilon<\kappa/B\) then works for sufficiently large degrees. Explain the error terms and inequality directions.

Every finite arithmetic choice must be fixed before tower degree grows. If a proposed construction needs degree-dependent scales or moduli, derive its complete asymptotics afresh and prove a fixed positive exponent; do not reuse fixed-parameter formulas without justification. The final polynomial must remain fixed in every case.

Most importantly, the target concerns **all pairs in \(C_d\times C_d\)**. A small image on selected pairs, a graph of a relation, or a dense subset of pairs is insufficient without a proof controlling the remaining outputs. Distinct constructions in the two coordinates also require an explicit reduction to one set.

## 8. Coordinated subagents

You are explicitly authorized to use multiple subagents. Use bounded, independent assignments and respect the environment's concurrency limit. These are research roles, not separate user-facing tasks.

- **Baseline auditor:** correct C0 and verify the exact scope of the quartic certificate obstruction.
- **Carrier analyst:** define and analyze one selected model's input size and output geometry.
- **Arithmetic analyst:** audit local images, split-prime compatibility, ideals, and lifting for a selected model.
- **Rate analyst:** independently track losses, optimize legitimate parameters, and test whether the proposed improvement can change the sign.
- **Independent referee:** reconstruct the selected argument and attack its weakest claim.

The lead owns model selection, notation, claim integration, and final proof synthesis. Run roles in waves if necessary; do not spend worker slots duplicating the same easy algebra.

Each handoff must contain the exact claim, hypotheses, source locators, proof or computation, dependencies, and one status: `PROVED`, `SOURCE INPUT`, `CONJECTURAL`, `COMPUTATIONAL EVIDENCE`, or `FAILED CERTIFICATE`.

The lead independently checks the transport identity, field applicability, all-pairs support count, parameter dependence, and exponent conversion. Subagent agreement does not establish a theorem. Resolve disagreements mathematically and retain unresolved gaps.

Workers write separate notes; only the lead edits consolidated deliverables. Keep all original sources read-only.

## 9. Bounded proof and mutation policy

After the baseline correction, allow at most four serious research attempts total, including mutations. Each must concern a named construction and an explicit lemma. Do not exceed two sustained models at once.

Prefer a complete proof of one meaningful intermediate lemma to several speculative full proofs. Computation may reject identities or guide parameters, but finite tests do not establish asymptotic claims. Exact finite enumeration can certify a fixed finite claim when its coverage is auditable.

If the first two selected models fail, permit one tightly justified change of deformation or target polynomial. Explain exactly which obstruction the change repairs. Any new target must be explicit, fixed, genuinely depend on both variables, and pass the same-set and nonspecialness audits.

A higher-degree polynomial obtained simply as a univariate postcomposition of the proved quadratic is an inherited corollary. Record it if useful, but it does not meet this run's objective of extending the compression mechanism beyond that inherited case.

Do not claim an impossibility theorem from a failed upper bound. Use precise verdicts:

- **PROVED WITHIN THE OFFLINE SOURCE SYSTEM:** all load-bearing dependencies are justified.
- **CONDITIONAL THEOREM:** a complete implication under separately stated, substantive assumptions; every missing assumption is listed.
- **PARTIAL THEOREM:** a useful exact lemma is proved, but the target remains open.
- **CERTIFICATE OBSTRUCTION:** no parameter choice makes a specified proved counting bound yield a saving; actual compression remains undecided.
- **CONSTRUCTION IMPOSSIBILITY:** a lower bound or other argument rules out the desired result for every carrier in an explicitly defined class.
- **UNRESOLVED ATTEMPT:** the model has an identified gap and neither success nor impossibility has been proved.

## 10. Referee requirements

Before accepting a conclusion, independently check:

- All source statements are actually available and applied with their hypotheses.
- Field signatures and notation are correct.
- The polynomial and final exponent have the claimed fixed dependence.
- Input restrictions are charged quantitatively, including multiplicity and density loss.
- Every output from the Cartesian square is covered.
- Every conjugate, residue class, exceptional prime, and denominator is handled.
- Local density is combined with uniform per-class control, not an assumed equidistribution law.
- Translation and anisotropy estimates apply to the actual carrier.
- The rate is positive under simultaneous, valid parameter choices.
- A numerical search or a failed certificate has not been promoted to a theorem.
- The final claim does not exceed the class of constructions or inequalities actually analyzed.

## 11. Deliverables

Write under `phase_c1/`:

1. `Phase_C0_Corrected.md` and `C0_CORRECTION_LOG.md`, with a clear freeze verdict and no edits to submitted originals.
2. `Phase_C1_Higher_Degree_Proof_Search.md`, containing the quartic baseline, selected model cards, full successful derivations, exact failed inequalities, and referee findings.
3. `SOURCE_MANIFEST_C1.md`, `CLAIM_LEDGER_C1.md`, and `REFEREE_REPORT_C1.md`.
4. Corrected C0 and C1 PDFs if offline tools permit; render and inspect them. Complete Markdown remains required if PDF tooling is unavailable.

Keep scripts or experiments only when they support a reported claim. Include a compact dependency diagram distinguishing proved steps from open ones.

Make the final report easy to study: define symbols before using them, explain what each estimate controls, and place the strongest result first. State clearly whether the quartic target was achieved. If not, give the strongest proved intermediate result and one exact next lemma; preserve the full gap list elsewhere.

End with a short comparison:

| Question | Required answer |
|---|---|
| What remains established from C0? | Corrected quadratic family theorem and its precise source dependence. |
| What did C1 actually add? | A proved extension, intermediate lemma, or scoped obstruction. |
| Which attempted mechanism failed, and why? | The exact inequality or false lemma. |
| What would the next successful step need to prove? | One mathematical statement, not a general research aspiration. |

Do not end with another unrestricted search proposal. Do not begin an external novelty audit or a further phase during this run.

## Begin

Inspect the C0 results, prepare the focused corrections, and establish the precise quartic baseline. Coordinate independent subagents to test at most two explicit construction models. Pursue their proof obligations through a complete argument or a rigorously scoped obstruction, keeping all sources read-only and the entire run offline.
