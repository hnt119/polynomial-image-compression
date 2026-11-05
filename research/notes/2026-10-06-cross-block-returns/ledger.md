# Cross-block construction and claim ledger

## Identity and provenance

- **Track/date/version:** T03, 2026-10-06, version1; fixed polynomial
  \(Q(x,y)=x^2+xy+y^2\), same real scalar set in both coordinates.
- **Authority:** live user request “New Cross-Block Returns — Multiscale
  Quadratic Compression”; offline proof research, three specialists,
  at most3 proposed mechanisms and2 finalists, at most1 mutation per
  finalist, at most2,000,000 charged exact evaluations and600 program CPU
  seconds including mathematical validation, with20% reserved.
- **Evidence:** complete local proofs; independent internal audit and lead
  reconstruction. No experiments, external sources or novelty claim.
- **Frozen dependencies:** 2026-09-30 multiscale composition MS-C1/MS-C2
  supplies actual carriers, field involution, scalar line populations,
  input bounds, and selected-action counts. New full-fiber conclusions
  are separately proved here. Prior source bytes remain unchanged.
- **Claims and locators:** XB-A1–A3 in `actions.md` §§1–3;
  XB-C1 in `composition.md` §§2–4; XB-F1 in `audit.md` §2;
  XB-F2 in `audit.md` §§3–5. All **PROVED** within their explicit scopes.
  Both existing carrier compression targets are now
  **FAILED IN STATED SCOPE**. Hashes are in `manifest.json`.

## Construction and coverage

The exact carrier definitions are in the report and proof companions.
Depth \(d\ge1\) is the only growing parameter. No new carrier or amplitude
rule was substituted for either definition. The new finite action library
is the deduplicated set
\[
\widehat U(A)=\mu_{6\cdot2^d}\cup\{\pm u_r:r\in\mathcal R(A)\},
\quad
u_r=\frac{r-\omega}{1-\omega r},\quad u_\infty=-\omega^2,
\]
\[
\mathcal R(A)=\{y/x:x\in A\setminus\{0\},\ y\in A\}
\cup\{\infty\}.
\]
Its inventory is at most \(6\cdot2^d+2(n(n-1)+1)\).
Each fixed action has a one-line swap certificate. That line is not
silently equated with its full return domain. The full-fiber proofs include
every incidental collision under every possible norm-one multiplier.

All bounds below use actual scalar values. No scalar address is assumed
injective. Subsets of sources are used to establish lower bounds for the
entire image; no discarded pair is credited as a constructive saving.

## Signed rate and arithmetic audit

| Gain or cost | Exact accounting | Status |
|---|---|---|
| Input count | Pure: \(3\cdot2^d+1\le n\le3\cdot4^d+1\). Mixed: \(6\cdot2^d+1\le n\le3\cdot4^d+1\). | PROVED inherited counts |
| Input thinning twice | None. Entire unchanged scalar sets and their ordered squares are used. | No free thinning |
| Parameter and projection fibers | All amplitude duplicates removed. Each scalar on a fixed nonzero F-line has one F-coordinate. \(\phi(x,y)=x-\omega y\) is injective. | Exact |
| Enlarged action inventory | At most \(m+2(n(n-1)+1)\); this quadratic possible inventory is not a return gain. | PROVED |
| Certified domains | At most \(n-1\) nonzero swap sources per fixed multiplier; the fixed Vieta action also has a one-line certified domain. | PROVED; full domains may be larger |
| Distinct actions/targets | Nonzero sources have trivial multiplier stabilizer. At the origin all labels give one pair. | Exact |
| Denominators | Swap coefficients divide by \(Q(x,y)>0\), or \(1+r+r^2\); Vieta denominator is \(1+t+t^2>0\). No uniform integrality or denominator-height assumption is imposed. | Fractional actions allowed |
| Input integrality/height | Inherited inputs are algebraic integers; conjugate magnitudes at most \(2^{d+1}\) or \(2\cdot3^d\). These bounds are not used to bound the new full fibers. | PROVED inherited |
| Field degree | Real field degree \(2^d\), relative quadratic extension \(K/F\). All fiber constants are independent of degree. | Explicit growing field |
| Discriminant, regulator, class number | No ideal counting, unit enumeration or volume estimate is invoked; no numeric bound or favorable cost is assumed. | Inapplicable to the algebraic counting proof |
| Local sparsity/splitting/populations | No congruence sieve or residue count. The integer \(m\) indexes angular actions. | No saving credited |
| Archimedean distortion | Two real embeddings give positive definite forms. Their conditioning is irrelevant to the exact intersection count. | At most4 intersections per independent target-line block |
| Branches/carries/state costs | Two or four actual F-lines;12 ordered independent target-line blocks in the mixed case. Formal amplitude branches supply no multiplicity. No carry argument used. | Fully charged |
| Pure full-fiber population | At least \(4(n-1)^2/9\) pairs; full fiber exactly4. | PROVED XB-F1 |
| Mixed full-fiber population | At least \((n-1)^2/2-4(n-1)\) pairs; full fiber at most48. | PROVED XB-F2 |
| Mixed source exception | Two output F-lines; at most \(4(n-1)\) independent sources land on them. Other same-line sources are not assumed small-fiber. | PROVED XB-C1 |
| New return gain | Pure cross-parity pairs improve exactly2→4 under \(\widehat U\). Vieta gives additional mixed-block targets on the specified line. | Constant gains only |
| Final image exponent | Pure image \(\ge(n-1)^2/9\); mixed image \(\ge(n-1)^2/96-(n-1)/12\). Both images \(\le n^2\). | Actual \(\Theta(n^2)\), not just certificate failure |
| Input rates a,B | Valid bounds \(a=\log2\), \(B=\log4\); existence of a limiting rate is unproved. | No assumed lambda |
| Net normalized gap | \(\log\lvert Q(A,A)\rvert=2\log n+O(1)\); hence the gap below exponent2 is0. | PROVED for these carriers |
| Requested epsilon,delta | Every fixed positive pair fails uniformly over all selected action libraries on these carriers. | FAILED IN STATED SCOPE |
| Rectangular eta | No rectangular intermediate carrier. | Inapplicable |
| Certified positive c | None; indeed no fixed positive c is possible for either family. | General real-set target remains OPEN |

The exception of size \(O(n)\) in the mixed proof is removed from a
quadratic-sized **small-fiber** population. It is not a constructive
exception bound for a large-return population. Confusing these two roles
would reverse the result.

## Quantifiers and final disposition

For each \(d\), allow any finite deduplicated norm-one family \(U_d\)
containing1, with unrestricted dependence on the carrier and depth.
Every returned pair is a member of the full fiber. Therefore for any fixed
\(\varepsilon,\delta>0\), once \(n^\varepsilon>48\), the relevant
proved quadratic source population belongs to
\(\{p:R_{U_d}(p)<n^\varepsilon\}\). Its ratio to \(n^{2-\delta}\)
diverges as depth grows. No constant \(C\) repairs the requested tail.
The norm-ratio correspondence proves the same conclusion even if all
possible norm-one multipliers are allowed.

For every fixed \(c>0\), the actual-image lower bounds eventually exceed
\(n^{2-c}\). Thus the new failure is specific to the **two carriers**,
not merely their old torsion-action certificates. No conclusion about
other carriers, general ML-O1, RC15/4, ARG/TCRC or the ultimate target
follows. The earlier checkpoints are extended by this dated record,
not rewritten.

The two-finalist stop rule was satisfied analytically. Direction B was
not started, no mutation was used, and no mathematical program execution
was necessary. The sole next obligation XB-O1 is stated precisely in the
report; its projective-spreading condition is an unproved proposed escape
gate, not an asserted equivalent of the power-saving target.
