# Balanced Factor Construction and Rate Ledger

11 October 2026 · version 1 · T03 · fixed \(Q(x,y)=x^2+xy+y^2\).
This applies the [repository construction template](../../templates/CONSTRUCTION_LEDGER.md)
to the unchanged balanced-factor carrier and its single new coupled mechanism.

## Claim and source record

| ID | Status, quantifiers and scope | Proof and dependencies | Review |
|---|---|---|---|
| BFF-A1 | PROVED, every integer depth: exact scalar decomposition, \(16q^2+1\le n\le24q^2-7\) | algebra.md §2; inherited AMP-A1, field fact \(\omega\notin\mathbb Q(\xi)\) | Lead and independent C checked complete written proof |
| BFF-A2 | PROVED, all \(v,w\in H\): pulled-back product law and exact full-fiber key | algebra.md §3; BFF-A1 injectivity and direct expansion | Lead and independent C |
| BFF-A3 | PROVED, fixed scalar blocks: two-component equality and exact base-subfield-valued mixed locus | algebra.md §4; BFF-A1 and direct expansion | Lead and independent C; other blocks remain unclassified |
| BFF-A4 / BFF-C1 | PROVED, every finite symmetric scalar set containing zero: complete sign/swap representatives and weights | algebra.md §5, audit.md §2 | Independent derivations and lead check |
| BFF-P1 | PROVED, all source representations and allowed masks: whole norm quartic and its degeneracy | coupled.md §§2–3; inherited disjoint cosets, field fact | Lead and independent C checked all coefficients |
| BFF-P2 | PROVED obstruction / FAILED mechanism, all sufficiently large depths: enlarged iterative certificate bounded by four on almost all sources | coupled.md §§4–5; BFF-P1, BFF-A1, AMP-R1–R3 | Lead and independent C checked constants and closure |
| BFF-E1 | EXPERIMENTAL, exhaustive exact \(r=0,1\) only: full distributions | data.json; local scout, full norm oracle and integer seed oracle | Pre-execution review, lead execution, independent result/provenance inspection |
| BFF-O1 | OPEN, fixed \(C,r_0\), every \(r\ge r_0\): polynomial-in-depth full-fiber upper bounds on at least \(32q^4\) sources in \(B^2\) | README.md §7; exact equivalence BFF-A2 | Consequence independently checked; premise unproved |

All claims belong to the T03/ML-O1 balanced-factor branch, version 1 of this
11 October cycle, except the separately versioned audit. File hashes and exact
claim locators are in state.json and manifest.json. These are internal proofs
and audits, not external review or novelty claims. Earlier theorem scopes and
historical files remain unchanged.

## Inputs and quantitative charges

Fix scales 1 through 8, digits −3 through 3, prime 7 and the correction
group \(\mu_6\) before depth grows. Then \(q=7^r\), and all original
amplitudes, both projections and every ordered pair remain in scope.

| Gain or cost | Actual bound or charge | Use and limitation |
|---|---|---|
| Complex inventory | \(8q\) disjoint cosets, \(48q^2\) encoded points | Inherited AMP-A1; no new inventory search |
| Scalar projection and deduplication | \(A=X(B\dot\cup(-B)\dot\cup D)\), \(n=16q^2+\lvert D\rvert\) | Exact bijection, every duplicate in \(D\) retained only once |
| Input bounds | \(16q^2+1\le n\le24q^2-7\) | \(a=B=2\log7\), uniformly \(\log n=2r\log7+O(1)\) |
| Input thinning | None, in either coordinate | The completed square is enumerated and is the theorem domain |
| Encoded fiber gain | Inherited \(6q2^s\), for \(s\) nonzero digits | Only \(48q^2=\Theta(n)\) source pairs are encoded |
| New phase rule | Source phases in \(\mu_{6q}\), interchanged between coordinates | Corrections remain in fixed \(\mu_6\); no larger correction rule is silently included |
| Branches | At most \(4^r\) mask pairs and 36 correction pairs | All charged in the source bound; no address entropy counted as targets |
| Phase eligibility | At most four second phases per fixed remaining labels outside baseline | Whole quartic equation; degeneracy is explicitly factored |
| Source and target multiplicity | All representations allowed; actual source set bounded above by labels | Duplicate labels only increase the upper bound; no false lower target count |
| New nonbaseline source set | At most \(55296q^3 4^r\) | Fraction at most \(216(4/7)^r\) |
| Old moves and encoded edges | At most \(1536q^3 4^r+48q^2\) further exceptional sources | Included before arbitrary finite iteration |
| Full enlarged certificate | At most four targets outside fraction \(222(4/7)^r+3/(16q^2)\) | A near-full low-return set, not a small bad tail |
| Origin and stabilizers | Origin has one full target; nonzero equal-norm targets determine unique multipliers | All counts concern distinct actual pairs |
| Coefficient field | \([K:\mathbb Q]=12\cdot7^{r-1}\) for \(r\ge1\); degree 2 at seed | Growth recorded; the quartic root bound is independent of this degree |
| Scalar denominators | \(3A\) integral; \(\Delta^{-1}=-\Delta/3\) | Fixed exact normalization; output scale 9 is a bijection |
| Switch and ratio denominators | Nonzero products of \(2-\xi^j\); actual whole-pair ratio only for nonzero source | No denominator-count saving is assumed; target membership follows directly from (8) in coupled.md |
| Heights and embeddings | Every amplitude conjugate at most \(8\cdot3^r\); scalar conjugates at most \(16\cdot3^r/\sqrt3\) | Charged growth; no rounding or geometric-box approximation |
| Norm convention | \(z\bar z\) for complex conjugation, equals the real quadratic at the specified embedding | Exact whole-scalar identities, including mixed terms |
| Local moduli, carries and ideal index | Exact cyclotomic phases and inherited coset distinctness; no new local-density or ideal-index estimate | No modular equality is used as a real collision |
| Discriminant, regulator, class number | No estimate using them is invoked | Their sizes are not assumed zero or bounded; future arguments must charge any dependence |
| Scalar output key | \(\mathcal K\) in \(H\), with target domain all \(V^2\) | Exact equivalence to full fibers, not a compression bound |
| Exception outputs for a success certificate | Uncontrolled for unrestricted full fibers | A selected-return obstruction cannot be inserted as a full-fiber upper bound |

## Signed-rate decision

The entire-image upper bound supplied by this cycle is still the trivial
\(n^2=\exp(4r\log7+O(1))\). Thus the supplied full-support signed gap is
\(2a-4\log7=0\), with \(a=2\log7\). This records absence of a proved
positive gap; it is not an actual-image lower bound.

For every fixed \(\varepsilon,\delta,C_0>0\), once \(n^\varepsilon>4\)
and \(n^\delta>2C_0\), the enlarged certificate's eventually at least
\(n^2/2\) bounded-return sources contradict a certificate tail of size
\(C_0n^{2-\delta}\). The same conclusion is **not** established for
\(F_A\). No positive \(\varepsilon,\delta\), or resulting \(c\), is
proved, and no rectangular \(\eta\) is needed.

The sole remaining BFF-O1 premise, if proved at every sufficiently large
depth, would instead give \(n^2/[18(r+1)^C]\) distinct actual outputs.
That implication is proved; the premise remains OPEN. It does not demand
an exact constant-fiber classification. It was not searched after the
single mechanism's decisive failure.

## Decision and evidence limits

One carrier; one phase-transposed mechanism; no mutation, second mechanism,
amplitude repair, deeper sweep, numerical clustering, or literature search.
Finite data are complete at exactly \(r=0,1\). Neither those cases nor
the selected-return proof retires the carrier. General T03 and RC15/4
remain OPEN. The separate phased-binomial, dyadic, relative-norm and
quadratic-phase failures retain their own scopes.
