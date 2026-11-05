# Elliptic geometry construction and claim ledger

Date: 2026-09-30. Track T01 only; fixed polynomial P(x,y)=(x-y)^3+x+y.
This is a new offline research cycle explicitly commissioned by the user's
“Cubic: elliptic/genus/complex-geometry search” message. It does not replace
the near-complete-chart checkpoint or reopen its proved rational-chart scopes.

## Identity and provenance

The controlling predecessor is
[near-complete charts](../2026-09-30-near-complete-charts/README.md), especially
NC-C2 and NC-O1, with the earlier
[rational sharing-curve proof](../2026-09-21-nonlinear-reuse/rational-reuse-curves.md).
The current task extends the geometric analysis to elliptic maps, complex
structures and a separate quartic comparison; it is not a literature review.
Missing historical source documents remain identified in MC-06 of the migration
conflicts. No unavailable proof is asserted to have been read.

New claims EG-G*, EG-B*, EG-C* are precisely stated and proved in the three
companions genus.md, group-law.md and complex-extensions.md. EG-L1 is the
input and selected-pair counting proof in this ledger; EG-X1 is the
finite experiment below. The report cites those scopes. All are dated
2026-09-30, with file hashes in the local verification manifest. The lead
inspects the mathematical arguments; computational checks support only their
explicit finite range. No novelty, rank or complete endomorphism-ring claim
is made.

Announced total ceiling: 12 candidate sets, 100,000 cubic P evaluations and
20,000 symbolic/curve checks. Network: none. Three specialists handle
geometry/higher genus, elliptic group laws, and complex/extensions; the lead
handles computation and synthesis. Exact rational arithmetic only.

## Construction and full coverage

For the sharing scout fix s=1,c=6 and
E: y²=x³−48x−15424, T=(40,216).
Choose the first m positive multiples of T. The companion proves T has
infinite order. For each point set
X=x−4, d=72/X, w=y/(3X), u=(w+d)/2, v=(w−d)/2.
Then u³−v³−u+v=6 and the three scalar endpoints are

a=(6−u³+u)/2=(−v³+v)/2,
b=(6−u³−u)/2, e=(−v³−v)/2.

Use the one real rational set A_m of all these endpoints. The selected
ordered pairs (a,b),(a,e) have outputs 6,0. There is no pole at x=4 on the
real curve since the right side there is −15552.

PROVED (EG-L1). On the smooth projective sharing cubic, u has three simple
poles at infinity, hence degree 3. Each endpoint function has degree 9:
its cubic leading term cannot cancel its simple linear term at infinity.
Each fixed value of a has at most nine preimages. Consequently
m/9 ≤ |A_m| ≤ 3m. Projection to u or v has fibers at most three, so the number
Q of distinct prescribed ordered pairs obeys 2m/3 ≤ Q ≤ 2m. The output
classes are disjoint because 0≠6. More sharply, for each fixed second
coordinate P is strictly increasing in the first coordinate, so any one
real output has at most N pairs. Thus Q≤2N and the complement
has size at least N²−2N. This is a proved sparse-coverage statement
about the designated pairs, not a lower bound on the entire actual image.

The second scout takes A_m={x(kT):1≤k≤m}. Infinite order gives distinct
x-coordinates: x(kT)=x(lT) forces kT=±lT, hence k=l for positive k,l.
Thus |A_m|=m. No global group-law identity for its P outputs is supplied.

## Quantitative ledger

| Gain or cost | Bound or treatment | Status |
|---|---|---|
| Input before losses | m rational elliptic points; sharing m/9≤N≤3m, direct x projection N=m | PROVED |
| Input thinning in both coordinates | None; enumerate the entire resulting A². No selected parameter square is substituted for it | PROVED |
| Parameter and scalar multiplicity | Sharing endpoints degree 9, pair maps degree 3; distinct pairs deduplicated exactly. General elliptic charts charge degree d and label multiplicity | PROVED |
| Output preservation | Exactly the two selected fibers 0,6; no identity on the remaining square | PROVED |
| Local sparsity, splitting and per-residue population | Inapplicable: no local-density construction or sieve | PROVED |
| Field degree, discriminant, regulator, units | All scout inputs in Q, degree 1. No growing field, regulator or unit selection | PROVED |
| Heights, denominators and normalization | Exact fractions retained; bit lengths and common-denominator bit lengths recorded. No denominator clearing: scaling changes P. No asymptotic height bound used as a counting gain | COMPUTATIONAL |
| Archimedean radii and distortion | Exact real inclusion; no bounded interval or metric claim used | PROVED |
| Branches, ratios, covers, carries | Two output labels and one birational inverse; its real denominator never vanishes. No digit expansion or carry saving | PROVED |
| Exceptional and uncovered outputs | Every uncovered pair costs one in the safe certificate 2+N²−Q. At least N²−2N uncovered pairs in this designated mechanism | PROVED |
| Full image exponent | Only the trivial exponent 2 is proved for this family. Extra coincidences are measured at finite m | OPEN |
| Input rates and gap | In depth log m, log N=log m+O(1); certificate remains N²−O(N). No positive delta or fixed saving exponent is certified | PROVED |
| More general elliptic-chart library | Sum of the explicit degree-weighted coverage bounds in EG-B4; degree, isogeny and number of rules all charged | PROVED |

The ledger does not claim that the actual image is quadratic for all m.
Unknown extra collisions are not charged as a gain.

## Exact finite evidence

COMPUTATIONAL (EG-X1). Run command:
python3 -m experiments.elliptic_geometry.
Source: experiments/elliptic_geometry.py; input and source hashes, Python
version, timing, parameters and raw-output hashes are in
local-only/runs/T01/2026-09-30-elliptic-geometry/experiment-provenance.json.
Portable results: examples/2026-09-30-elliptic-geometry.json.

Exhaustive within each of eight selected scalar sets: sharing prefixes
m=2,4,6,8 and x-coordinate prefixes m=4,8,12,16.
No random seed, sampling within a square, floating-point equality, numerical
root matching, finite-field equality substitution or imported program execution.

The run used 1,444 P evaluations and 104 charged curve/accounting checks.
For sharing prefixes N=5,11,17,23, the only nonsingleton fibers are precisely
the two designated m-pair fibers. The direct x-coordinate prefixes have
exactly two double fibers and all other fibers singleton. This is finite
evidence only. Full actual scalar sets, pair lists, scalar reuse counts,
fiber histograms, ranked fiber sizes, threshold tails and rational heights
are saved; the small portable file links and hashes every raw file.

The unit regression performs 29 additional P evaluations, giving 1,473
P evaluations for this cycle when run once in the required test suite.
It checks known point arithmetic, the inverse map and a complete 5-scalar
square. Existing repository regressions are separate inherited finite checks,
not an expanded search or proof of the research target.

## Evidence and disposition

The global and finite-grid elliptic obstructions are proved in their stated
rational-map scopes. They do not cover arbitrary multivalued correspondences,
growing degree-weighted libraries, or an independently constructed dense
network of sharing curves. Algebraic branches on finite covers require their
own coverage and fiber ledger.

The sole next mathematical obligation is EG-O1 in the report. T01 remains OPEN.
