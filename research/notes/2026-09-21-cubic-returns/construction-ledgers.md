# Construction and claim ledgers

2026-09-21 v1; T01 / cubic Cartesian returns. Instantiates
[the repository template](../../templates/CONSTRUCTION_LEDGER.md).
The fixed target throughout is \(P(x,y)=(x-y)^3+x+y\) on real scalars.

## Identity, authorization, and evidence

The user commissioned the new offline Cartesian-return cycle, after the
three-branch documentation freeze. Its obligation is to determine the scale
of \(E_1(A)\), then analyze chains and whole-square coverage. Network policy:
no access. Declared overall research cap: 200 candidates, 256 distinct inputs
per candidate, 3,000,000 exact pair checks, 90 research CPU seconds. The finite
subtask received 140 candidates, 2,000,000 checks and 60 seconds within that
cap; its approved endpoint was 130 candidates. No arithmetic amplification
was authorized without a positive asymptotic carrier, and none was attempted.

The proof sources are the new [baseline](baselines.md),
[fiber/chain](fibers-and-chains.md), and [universal-bound](universal-bounds.md)
companions. Exact computation has its own [verification record](verification.md).
The earlier continuation supplies the already-proved symmetry, not the new
return upper bound. Original named digital/rich-fiber checkpoint bytes remain
unavailable locally under MC-06; they are not dependencies of these proofs.

## L1. Integer intervals and fixed-step progressions

**Construction and coverage.** For integers \(N\ge1\),
\(A_N=\{0,\ldots,N-1\}\), with no thinning or projection. The baseline
companion counts all differences and anchors and proves
\(E_1(A_N)=\frac43\sqrt{2/3}\,N^{3/2}+O(N)\).
The step \(1/3\) improves the coefficient to \(4\sqrt2/3\), with the same exponent.
For a fixed reciprocal-integer step \(h=1/q\), translations and this fixed
step are chosen before \(N\) grows; return count is \(\Theta_q(N^{3/2})\).
Translations preserve return counts because
\(T_1(x+t,y+t)=T_1(x,y)+(t,t)\).
Other fixed steps have no returns unless \(1/h\) is an integer.

| Template charge | Account and status |
|---|---|
| Input count before losses | Exactly \(N\), PROVED |
| Thinning in both coordinates | None; all \(N^2\) ordered pairs retained |
| Parameter/projection multiplicity | One scalar per index, exactly one |
| Local sparsity/splitting and per-residue populations | Inapplicable: no local lifting. Integrality of transformed coordinates is checked explicitly in the AP proof |
| Field degree/discriminant/regulator/units | No growing number field; rational APs have degree one; no such rate is used |
| Heights/moduli/denominators | Integer height \(O(N)\); fixed denominator \(q\) for step \(1/q\); no hidden denominator parameter |
| Archimedean size/distortion | Diameter \((N-1)/q\), used explicitly to restrict useful differences to \(O_q(\sqrt N)\) |
| Branches/ratios/covers/carries | No branches or digital states. All difference slices are summed once |
| Uncovered pairs/outputs | At most \(2E_1=O_q(N^{3/2})\) vertices are in nontrivial paths. All other \(N^2-O_q(N^{3/2})\) pairs must still be counted |
| Full-image upper certificate | Path count \(N^2-E_1=N^2-O_q(N^{3/2})\), with leading quadratic order; additional output coincidences are not discarded |
| Input/output rates | In units \(d=\log N\), \(a=B=1\), certified output exponent \(c-s=2\), hence \(\Delta=2a-(c-s)=0\) |
| Fixed saving exponent | None certified. FAILED as a positive-density single-step or long-path coverage mechanism |

The leading image certificate is insufficient regardless of a large finite
edge-density example. No universal actual-image lower bound follows from it.

## L2. One or many explicitly planted cubic fibers

**Construction.** For integers \(L\ge1,M\ge1\), let
\(D=L^3+L+1\), \(z_m=2mD\), and

\[
A_{M,L}=\left\{\frac{z_m-j^3+j}{2},
                    \frac{z_m-j^3-j}{2}:
                  0\le m<M,\ 1\le j\le L\right\}.
\]

CR-P5 proves strict interleaving within each block and separation between
blocks. Thus \(N=2ML\) exactly. The construction realizes \(M\) selected
outputs, each with \(L\) consecutive pairs. It can be built recursively by
adding the next two cubic coordinates at each step, but each stage is still
one real scalar set. The same universal return bound applies at every stage.

| Template charge | Account and status |
|---|---|
| Input count before losses | Exactly \(2ML\); both lower and upper counts proved |
| Thinning in both coordinates | None; full square size \(4M^2L^2\) |
| Parameter/projection multiplicity | One per coordinate occurrence, by interleaving and disjoint blocks. No scalar reuse in this separated construction |
| Local sparsity/splitting and residue populations | Inapplicable; no finite-field realization or CRT layer |
| Field degree/discriminant/regulator/units | All chosen coordinates are integers: \(j^3\pm j\) are even; no growing extension or unit parameter |
| Heights/moduli/denominators | Absolute scalar size \(O(ML^3)\); denominator cancels exactly; no local moduli |
| Archimedean size/distortion | The separation \(D=L^3+L+1\) is charged. It is chosen explicitly for each \(L\), with no unspecified generic projection |
| Branches/ratios/covers/carries | Two coordinate branches, each of length \(ML\), disjoint; \(M\) chosen output labels |
| Prescribed gain | \(ML=N/2\) pairs; \(M(L-1)\) edges; path length \(L\). Prescribed-pair density \(1/(2N)\) |
| Uncovered-pair cost | \(N^2-N/2\) pairs are outside the prescribed list. Counting each separately gives full support upper bound \(M+N^2-ML\), of quadratic order |
| Incidental returns | Unknown individually, but total \(E_1\le5N^{11/6}\) is proved; they cannot repair positive-density fixed-step coverage |
| Rate ledger | For any growing choice with \(N\to\infty\), use \(d=\log N\), \(a=B=1\), certified \(c-s=2\), \(\Delta=0\) |
| Fixed saving exponent | None. Actual full-image exponent remains OPEN; positive-density fixed-step certificate is FAILED |

Selecting close outputs instead can reuse coordinates; the finite diagnostic
measures coordinate occurrences divided by actual \(N\). No parameter count
is substituted for the true scalar count. The universal theorem covers these
overlapping variants and all other polynomial, rational, two-parameter,
difference-engineered or recursive carriers, for a common nonzero step.
It does not prove their actual cubic images large.

## L3. Universal upper bound, not an asymptotic construction

CR-U1 holds for every finite real \(A\), all \(\tau\ne0\), with no input
losses. Its auxiliary affine target
\(-2A/(3\tau)+(1-\tau^2)/3\) has exactly \(N\) elements; its projection
multiplicity is one. The proof is uniform in coefficient size and uses
real planar intersections, so small \(\tau\), large heights, or growing
denominators incur no omitted incidence constant. There is no field-degree,
splitting, regulator, carry or archimedean packing assumption.

For a list of \(M\) shifts, all \(M\) edge counts are charged separately:
at most \(5MN^{11/6}\). No local saving is counted twice. This is an
obstruction to particular image certificates, not a claimed favorable
construction ledger. The actual image remains uncontrolled between components.

## Evidence and disposition

The asymptotic statements rely on the displayed proofs and their recorded
internal audits. Finite rational evidence is exact over the approved grid
only. The new report answers the frozen \(R_1\) question and records one
next obligation, CR-O1; neither the old three-branch reports nor canonical
historical data are overwritten. No novelty or external review is claimed.
