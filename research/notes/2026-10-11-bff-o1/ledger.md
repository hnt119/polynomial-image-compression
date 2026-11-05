# BFF-O1 construction, proof, and rate ledger

11 October 2026 · version 1 · T03 balanced-factor branch.
This follows the [construction ledger template](../../templates/CONSTRUCTION_LEDGER.md).
The polynomial is the fixed real \(Q(x,y)=x^2+xy+y^2\).

## Identity, authorization, and provenance

The user authorized deciding exactly BFF-O1 for the unchanged carrier,
strictly offline, with at most two proof approaches and two specialists.
No amplitude mutation or enlargement of an action family was authorized
or performed. Historical source files, archived proofs, and the completed
r=0,1 scouts are immutable inputs. No source missing from the controlling
proof chain was reconstructed from a title.

| Claim ID | Status, scope, and quantifiers | Complete proof and dependencies | Audit |
|---|---|---|---|
| BFO-L1 | PROVED: a fixed finite family of polynomial maps of domain dimension at most d has uniformly finite all-map fibers away from fixed-degree source exceptions, for rank-d sources, outside finitely many parameter specializations | elimination.md E1–E4; characteristic-zero differentiation, algebraic field extensions and monic equations, all proved there | Independent C and lead; symbolic |
| BFO-T1 | PROVED: for every r≥2 the full scalar carrier is covered by 49 spaces of dimension at most two in the last degree-seven extension | tower.md; frozen BFF-A1 and exact alpha⁷=eta carries | Independent C and lead |
| BFO-T2 | PROVED: at least 1344 of 2401 ordered local source type pairs have direct two-dimensional spaces and rank-four full quadratic map | tower.md; explicit support-class count and differential | Independent C and lead |
| BFO-T3 | PROVED: uniform fixed-degree polynomial-zero-set bounds on B_j and B_j², tending to zero as a fraction | tower.md; inherited AMP-A3 norm shell classification | Independent C and lead |
| BFF-O1 | PROVED: fixed M,r_* exist; for every r≥r_* at least32q⁴ ordered B² sources have at most M unrestricted targets in V²; hence requested exponent C=1 eventually | tower.md application, README §§3–5; BFO-L1, BFO-T1–T3 and frozen BFF-A1–A2 | Independent C and lead |
| BFO-F1 | PROVED / carrier FAILED: actual full image lies between n²/(18M) and n² for all sufficiently large depths | README §5; BFF-O1 and n≤24q² | Independent C and lead |
| 2-adic screen | OPEN as a complete reconstruction method, stopped without adoption | two-adic-screen.md; not a theorem dependency | Auditor inspected the narrow signature idea, not an all-target conclusion |

The named BFO-L1/BFO-T1–T4/BFO-F1 labels are new to this report. Historical
BFF-A and AMP labels retain their exact earlier meanings. Current file
hashes and locators are in manifest.json and state.json. Reviews are
internal; no external review or novelty claim is made.

## Full coverage and quantitative charges

Fixed first: digit alphabet −3,…,3, scales1,…,8, prime7, the quadratic,
and the finite rational-function map family. Then choose its projection,
monic coordinate identities, M,D and exceptional parameter polynomial.
Finally choose a starting depth meeting specialization, zero-set-density,
and M≤r+1 requirements. Only afterward let r tend to infinity.

| Gain/cost | Bound and use | Status / charge |
|---|---|---|
| Actual scalar inputs | 16q²+1≤n≤24q²−7; log n=2r log7+O(1) | Frozen proved bijection, not labels |
| Parameter fibers of B | Exactly8q² distinct points; 49 distinct last-layer types times B_(r−1) | Frozen coset uniqueness; exact carries |
| D identifications | D is a deduplicated set; all its scalars lie in the same49-space cover | No injectivity of b↦bar b−b needed or assumed |
| Same-set transport | X:V→A bijective, and K equality iff full Q equality | All targets in A² retained |
| Source thinning | Retain at least32q⁴≥n²/18 ordered sources | Count already concerns pairs; no uncharged two-coordinate thinning |
| Local source types | At least1344/2401 have rank4, strictly more than1/2 | Explicit count, no probabilistic independence assumption |
| Target branches | All2401 space pairs, including lower-dimensional spaces | Their complete fiber bounds are summed into fixed M |
| Exceptional source polynomial | Degree≤D fixed before depth; coefficients may depend on eta | Root bound uniform in coefficients; heights irrelevant to exact root count |
| Exception fraction in a good local type | ≤4D/7^j+(D/8)(2/7)^j, j=r−1 | Eventually≤1/10, leaving more than32q⁴ sources |
| Origin and degenerate targets | Origin included in cover and counted once as an actual pair; nonzero B² sources cannot have Q=0 | Positive-definite real Q and injective X |
| Scalar denominators | Delta⁻¹=−Delta/3, fixed | Exact normalization only, no lattice-index estimate |
| New algebraic denominators | Finitely many rational functions in eta and projected outputs | Parameter zeros excluded at all large depths; output zeros are charged by polynomial exceptions |
| Field degree | Last extension degree7; base degree grows like7^(r−1) | Precisely what prevents fixed nonzero parameter polynomials vanishing eventually |
| Cyclotomic carries | alpha⁷=eta, with negative powers reduced using eta⁻¹ | No formal-frequency independence assumption |
| Growing factor support | Entire parent element remains a variable in a fixed-dimensional polynomial map | No support bound2^r silently replaced by a constant |
| Heights and embeddings | Inherited amplitude bound8·3^r in each complex embedding | No archimedean approximation; zero-set bounds independent of these heights |
| Discriminant, root discriminant, regulator, class number | No counting estimate using them is invoked | No boundedness claim and no hidden arithmetic-lattice cost |
| Projection / chart multiplicity | Rank-four charts have independent scalar coefficients; lower-rank redundant charts have no targets off the charged exceptional set; overlaps only overcount | Summed into M, not counted as extra collisions |
| Stabilizers / actions | Not used | Direct unrestricted full equality, not orbit multiplicity |
| Recursion and branch accumulation | One last layer only, at each depth | No iterated constant branching or C₀^r loss |
| Exceptional outputs | Not discarded in an upper-support argument | The theorem is an image lower bound from a positive-density bounded-fiber population |
| Computational cost | No mathematical program or finite audit run | 0 exact evaluations,0 research-program CPU seconds; administrative checks separately measured |

## Rate and decision

The input rate is \(\log n=2r\log7+O(1)\). The proved full image rate is
\[
\log |Q(A_r,A_r)|=4r\log7+O(1)=2\log n+O(1).
\]
Constants here may depend on the fixed algebraic map family, never on
r. There is no positive saving exponent for this carrier. In the requested
polynomial-in-depth form, choose C=1 and absorb M into the starting depth:
\[
|Q(A_r,A_r)|\ge n^2/[18(r+1)]=n^{2-o(1)}.
\]
The o(1) is uniform along every sufficiently large integer depth because
\(\log(r+1)/\log n\to0\). No subsequence exception remains.

More directly, for any fixed \(\varepsilon>0\), once \(n^\varepsilon>M\),
at least \(n^2/18\) sources have full fibers smaller than
\(n^\varepsilon\). This contradicts a purported upper bad-tail bound
\(C'n^{2-\delta}\) for any fixed \(\delta>0\) once
\(n^\delta>18C'\). Thus no success exponents epsilon,delta or c follow
for this carrier. No rectangular eta parameter is involved.

The carrier is retired. The unrestricted T03 target, RC15/4, ARG/TCRC,
and other amplitude families remain OPEN. This cycle adopts no replacement
conjecture, exact constant-fiber classification, or next search.
