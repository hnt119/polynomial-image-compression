# Multiscale packing — construction and claim ledger

## Identity and provenance

- **Date/track:** 2026-09-30, T03; fixed real polynomial
  \(Q(x,y)=x^2+xy+y^2\). Version 1, hashes in `manifest.json`.
- **Claims:** MS-C1 (dyadic cosine-product return obstruction), MS-C2
  (mixed-amplitude four-line obstruction), both **PROVED** in
  [composition](composition.md); their proposed positive-tail certificates
  are **FAILED**. MP-L1–MP-L3 are exact local identities/tables in
  [local-gadgets](local-gadgets.md).
- **Authorization:** current user attachment headed “Full-Rank Quadratic —
  Multiscale / Fractal Packing Search”; strictly offline; at most two serious
  constructions, one mutation per construction, 2,000,000 charged exact
  program evaluations and 600 measured research-program CPU seconds.
- **Dependencies:** elementary complex multiplication, sine doubling,
  the explicit cyclotomic involution and linear algebra over its real fixed
  field. No class-number, regulator or splitting estimate is used to prove
  either new obstruction. DC-R1 is retained as a previously proved sufficient
  implication; the new packings fail its hypotheses.
- **Evidence:** complete local symbolic proofs, independent internal audit,
  and lead reconstruction. Finite hand tables are proofs over the stated
  small sets, not program experiments or evidence of an asymptotic gain.
- **Historical boundary:** no claim replaces the preceding modular-lift
  checkpoint, adaptive RC15/4 problem, HR-N1 freeze or fixed-field theorem.
  The affine preselection application is inherited, not a third finalist.

## Construction and complete Cartesian accounting

Use the exact definitions of \(A_d^{(0)},A_d^{(1)},S_d,\gamma_\ell\)
in the [report](README.md) and composition proof. Fix the two recipes before
integer depth \(d\to\infty\); there are no tuned parameters or random seeds.
For each recipe all \(2^d\) amplitude addresses project into the **same**
scalar carrier. Distinct addresses and radii need not give distinct scalars.
The lower bound uses just \(S_d\), and the upper bound counts the union,
sharing its zero. Thus, for each \(i=0,1\),
\[
3\cdot2^d+1\le n_d^{(i)}\le3\cdot4^d+1.
\]
For the variant the stronger bound \(6\cdot2^d+1\le n_d^{(1)}\)
follows from its two top-level copies being disjoint away from zero
(composition, equation (24)). Both coordinates use \(A_d^{(i)}\); no rectangle or selected orbit subset
replaces its full square. Zero is present and has one distinct return.
All other pairs have trivial multiplier stabilizer, since
\(u\phi(x,y)=v\phi(x,y)\) with \(\phi(x,y)\ne0\) implies \(u=v\).
The map \(\phi:\mathbb R^2\to\mathbb C\) is a real-linear bijection.

For every fixed \(\varepsilon>0\), let
\(E_{d,\varepsilon}^{(i)}=\{p\in(A_d^{(i)})^2:
R_{\rm pair}(p)<(n_d^{(i)})^\varepsilon\}\).
For sufficiently large \(d\), with threshold exceeding 16, the proofs give
\[
\frac49(n_d^{(0)}-1)^2\le|E_{d,\varepsilon}^{(0)}|
\le(n_d^{(0)})^2,
\qquad
\frac12(n_d^{(1)}-1)^2\le|E_{d,\varepsilon}^{(1)}|
\le(n_d^{(1)})^2.
\]
These are ordered-pair counts. Constants are absolute; the threshold depth
may depend on \(\varepsilon\). For every fixed \(\delta>0\) the ratio to
\(n_d^{2-\delta}\) diverges. No asymptotic uniformity in
\(\varepsilon\downarrow0\) is asserted or needed.

## Fully charged quantitative ledger

| Gain/cost | Original cosine products | Mixed-amplitude variant | Status/source |
|---|---|---|---|
| Distinct input lower/upper counts | \(3\cdot2^d+1\le n\le3\cdot4^d+1\) | \(6\cdot2^d+1\le n\le3\cdot4^d+1\) | PROVED, composition |
| Input thinning, twice | None; both entire coordinates used | None | No omitted cross-pairs |
| Parameter/projection multiplicity | At most \(2^d\) amplitude labels; overlaps not assumed injective | Same | Actual union counts used |
| Scalar pair projection | \(\phi\) injective | Same | No pair-fiber loss |
| Genuine actions | Exactly \(6\cdot2^d\) distinct roots | Same | One global action, not independent local rotations |
| Stabilizer/duplicate loss | Nonzero: 1; zero: all labels give one pair | Same | Exact distinct-target convention |
| Local sparsity/splitting | No sieve or local splitting restriction | Same | Inapplicable to proof; no saving credited |
| Uniform residue populations | No residue-class construction | Same | Inapplicable |
| Field degree | \(K_d=\mathbb Q(\zeta_m)^+\), degree \(2^d\) | Same | Growing; cannot use fixed-field constants uniformly |
| Discriminant/root discriminant | No numerical bound used or claimed | Same | Not needed for algebraic obstruction; unknown numerical costs are not zero |
| Regulator/class number/unit cost | No ideal or fundamental-unit enumeration | Same | Inapplicable to new proof; only explicitly listed roots used |
| Input denominators | Inputs are algebraic integers | Same | \(2\sin r\theta=(\zeta^r-\zeta^{-r})/i\), with \(i\) an integral unit |
| Action coefficients | \(3a,3b\) integral for \(u=a+b\omega\) | Same | Denominator from \(\omega-\bar\omega\), square \(-3\); no integrality-return shortcut |
| Conjugate heights | Input house at most \(2^{d+1}\) | At most \(2\cdot3^d\) | Every embedded cosine factor has absolute value at most 2 |
| Archimedean distortion | Fixed coordinate decoding; no boundary argument | Same | No hidden volume/index approximation |
| Branches/carries/states | All amplitude labels charged in union bound | Same | No carry model; line states used for upper bounds on returns only |
| Exact reuse | Telescoping sine-doubling identity | Shared scalar recursion; four-line mixture | PROVED packing, no multiplicative return law |
| Exceptional/uncovered outputs | \(\ge4(n-1)^2/9\) low-return sources | \(\ge(n-1)^2/2\) low-return sources | Quadratic pair charge; no count of their distinct outputs asserted |
| Return rate on obstructed population | \(R=2\), hence \(\log R/d\to0\) | \(2\le R\le16\), same limit | Rules out any near-full positive return rate |
| Input rates \(a,B\) | Valid lower \(a=\log2\), upper \(B=\log4\) | Same | Exact exponential rate unproved |
| Final output exponent | Actual exponent OPEN; available trivial upper \(n^2\) | Same | Selected-return failure is not a lower image bound |
| Net certificate gap | No positive gap from this tail certificate | Same | Positive-density exceptions defeat the target before any additional arithmetic cost |
| Certified fixed \(c>0\) | None | None | FAILED certificate; target OPEN |

If a subsequence has \(\log n_d/d\to a_*\), then
\(a_*\in[\log2,\log4]\) and its obstructed pair population has log-count
\(2a_*d+o(d)\), while return gain there is \(o(d)\). Thus the needed
strict exceptional exponent deficit is zero. This does **not** supply a
formula for the actual image rate or imply that all pairs have rate zero.

## Failure registry and stop decision

| Certificate | Exact failure | Outside the scope |
|---|---|---|
| MS-C1 | Pure-eigenvector cosine-product carrier, selected \(\mu_{6\cdot2^d}\): a quadratic population has exactly two returns | Nonhomogeneous multipliers, other carriers, actual full image |
| MS-C2 | Specified \(1+\gamma_\ell\) mutation with four fixed-subfield lines: a quadratic population has at most sixteen returns | Growing line inventories or actions not homogeneous for the involution |
| Inherited affine preselection filter | Fixed totally real field, fixed finite affine maps/seed, exponential actual input count; inherited ideal bound applies | Growing fields/maps, uncontrolled heights or arbitrary real coefficients |

Two analyzed definitions, including one related mutation, now have rigorous
scoped obstructions. No additional carrier, mutation, experiment expansion or
replacement conjecture is adopted. The single retained obligation appears
at the end of the report.
