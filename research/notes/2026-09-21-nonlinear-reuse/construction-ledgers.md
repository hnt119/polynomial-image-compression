# Gain-versus-cost and construction ledgers

T01 / nonlinear coordinate reuse, 2026-09-21 v1.
Fixed \(P(x,y)=(x-y)^3+x+y\); real scalars, the same set in both
positions, every ordered pair.
This follows the repository [construction ledger template](../../templates/CONSTRUCTION_LEDGER.md).

## 1. Scope, parameter order and evidence

The current attachment authorizes new offline nonlinear-reuse research,
degree-bounded symbolic classification, and bounded exact chart experiments.
No network or arithmetic amplification is permitted. The announced ceiling
was 48 candidate charts, 20,000 exact coefficient checks, 500,000 full-square
polynomial evaluations and four million additional checks.

First fix the chart's degree, coordinate formulas, coefficient/scale choices
and any library-size rule. Then let its actual parameter-set size grow.
Every scalar and pair image is deduplicated before assigning rates.
All proof claim IDs, quantifiers, dependencies and audited proof locators
are in the main report and its companions. Finite code, input definitions,
runtime and hashes are in verification and the experimental companion.

No unavailable historical digital/rich-fiber proof is a dependency.
The only earlier construction obstruction reused is GS-P3 to identify
the consecutive-grid specialization of the degree-three counterexample;
that family was not searched again.

## 2. Exact nonlinear exceptional-cubic family NR-P1

Fix \(a=1/\sqrt3\), outputs \(0,4a/3\), and the rational formulas (P1)
in chart-capacity-and-completion. For each integer \(m\ge1\), use
\(t=2,\ldots,m+1\), both corresponding pairs, and their scalar union.

| Gain/cost | Charged bound | Evidence and status |
|---|---|---|
| Parameter labels | \(Q_0=2m\) | Two labeled output pairs per parameter |
| Distinct actual pairs | \(Q=2m\) exactly | Strictly decreasing differences, distinct output labels |
| Scalar input lower and upper count | \(m\le N\le3m\) | One strictly monotone coordinate supplies \(m\); shared first coordinate gives at most three per label parameter |
| Pair-projection multiplicity | One on this positive-integer parameter set | Proven, not assumed from formal labels |
| Scalar projection multiplicity | Some cross-parameter coincidences may occur; exact \(N\) need not be known | Both lower and upper counts suffice; \(4m/N\) average coordinate reuse lies between \(4/3\) and 4 |
| Same-set real transport | All required scalars are included in one \(A_m\) | Identity is for the original fixed cubic |
| Input thinning, twice | No input thinning | Selected *pair* set has only \(2m\) vertices; it does not replace \(A_m^2\) |
| Selected output support | Exactly two values | Direct cubic factorization |
| All branches and poles | Use \(t>1\); the pole at 1, vertical-limit point and isolated singular point are excluded by definition | Their exclusion does not remove any pair of the defined carrier square |
| Field degree and discriminant | Fixed quadratic scale \(a\), degree two | No growing field or discriminant rate; this is an exact scalar identity |
| Local moduli, splitting, regulator, units | Inapplicable | No local-sparsity or arithmetic-amplification argument |
| Heights and denominators | In units of \(a\), each coordinate has denominator dividing \(6(t^3-1)^3\) and numerator \(O(m^9)\) | A common denominator can be bounded by \(6\prod_{t=2}^{m+1}(t^3-1)^3\), with logarithm \(O(m\log m)\); it is not treated as fixed |
| Archimedean radii | The normalized \(U,V\) remain bounded for \(t\ge2\); hence scalar coordinates are \(O(1)\) | A small real radius does not give an exact support count |
| Carries/formal states | Inapplicable | Exact rational/algebraic values, no digit encoding |
| Chart library | Two fixed-output pair charts | Enlarging the library would be a new construction cost |
| Uncovered pairs | Exactly \(N^2-2m=N^2-\Theta(N)\) | Every unprescribed and cross-parameter pair is charged |
| Full-image certificate | \(2+N^2-2m\) | Selected support alone yields no power saving |
| Rates in depth \(d=\log m\) | Formal and distinct pair exponent \(q=1\); input \(a=B=1\); selected output \(b=0\); complete certificate exponent 2 | Full net gap \(\delta=0\), not the misleading selected gap 2 |
| Fixed positive saving exponent | None certified | FAILED prescribed-coverage family; actual full-image asymptotic remains OPEN |

The constant-size normalization does not change equality. It does not
authorize applying any homogeneous scaling theorem to the cubic.

## 3. Degree-two output-statistic charts NR-L1–L4

The exact hypothesis is \(\deg U,\deg V,\deg\Phi\le2\), \(\Phi\)
nonconstant, and \(J(U^3+V,\Phi)=0\), or the stronger displayed
polynomial composition. This is a proved identity hypothesis, never
inferred from small finite support.

| Gain/cost | Charged bound | Consequence |
|---|---|---|
| Formal labels | Arbitrary finite parameter domain, possibly \(m^2\) or larger | Formal size is not distinct pair size |
| Actual scalar pool | Exactly \(N=|A|\), independently defined | Both coordinates must belong to this same set |
| Distinct pair capacity | At most \(2N\) per chart; \(N\) for the genuine quadratic-statistic form | All projection multiplicities are absorbed by root counting |
| Label-to-pair loss | Average multiplicity at least \(Q_0/(2N)\) when all labels lie in the square | Cannot be credited as output compression |
| Chart count | \(J_0\) charts give at most \(2J_0N\) pairs | Near-full coverage requires \(J_0\ge N/2-O(N^{1-\delta})\) |
| Chart overlaps | Counted by an upper bound on the union | Overlap can only reduce coverage further |
| Coefficients/heights | Arbitrary real coefficients; capacity bound uniform in them | No favorable bounded-height assumption is made |
| Denominators | No parameter denominators in this polynomial class | No hidden rational normalization |
| Affine normal-form changes | Changes in proof parameter coordinates only | They do not transport or shrink the scalar carrier |
| Field/discriminant/regulator/splitting | Inapplicable | Elementary polynomial classification over the reals |
| Branches | Constant-coordinate, constant-output, affine-statistic and genuine quadratic cases all included | No omitted exceptional component |
| Uncovered-pair charge | At least \((N^2-2J_0N)_+\) | Quadratic for \(J_0=o(N)\) |
| Quantitative rate | For \(J_0=N^\kappa\), \(q\le(1+\kappa)a\) if input rate is \(a\) | When \(\kappa<1\), cannot reach full pair rate \(2a\) |
| Positive full-support rate | Not supplied; complete generic upper certificate remains of order \(N^2\) | FAILED stated chart-cover architecture |

All coefficient systems are classified analytically. The five exact kernel
computations check the arithmetic of that classification; they do not
supply a finite-to-asymptotic inference.

## 4. Rational chart libraries and independent scalar/output grids

For ordinary one-parameter rational pair charts of coordinate degree at
most \(d\), NR-A2 gives \(Q\le dJ_0N\). Degree and number of charts are
both charged. A library with \(dJ_0=o(N)\) cannot cover a positive
proportion of the square. Denominator poles are excluded from each chart
domain explicitly; the full carrier square still has no excluded inputs.

NR-G1/G2 treats a different model: one scalar \(X(r)\) and the output
\(Z(s)\) are independently prescribed by nonconstant rational functions,
and the other scalar is rational \(Y(r,s)\). If numerator/denominator
degrees are at most \(d\), then on \(m\times m\) parameter sets at most
\(7dm\) labels work, for each orientation separately.

No assertion that those working labels are distinct is needed; deduplication
can only lower their count. \(J_0\) such charts give at most \(7dJ_0m\)
working labels. If the intended scalar size is comparable to \(m\),
then \(dJ_0\) must be order \(m\) even to approach quadratic coverage.
That comparison of scalar and parameter sizes is a stated condition,
not a general theorem.

All denominator products enter the nonzero polynomial of degree at most
\(7d\); poles are excluded before counting. Coefficient magnitudes are
unrestricted, and the bound is uniform in them. Field extensions, splitting,
units, regulators, digit carries and arithmetic distortion estimates play
no role. Arbitrary algebraic inverse functions are not counted as rational
maps. No positive rate is asserted outside these hypotheses.

## 5. Full-square relabeling and many-to-one projection controls

A row permutation \(x=f(r),y=f(\pi_r(s))\) on an injective finite list
\(f\) gives \(Q=N^2\) and changes no output. This separates genuine
nonlinear coordinate notation from a new algebraic compression mechanism.
The modular examples in the grid are discrete permutations, not
bounded-degree rational maps.

For the signed-square chart \(x=r^2,y=s^2\), \(-m\le r,s\le m\),
\[
Q_0=(2m+1)^2,\qquad N=m+1,\qquad Q=(m+1)^2.
\]
A positive scalar has two sign descriptions and zero has one. Each pair's
multiplicity is the product of the two scalar multiplicities: one label
for \((0,0)\), two for a pair with exactly one nonzero coordinate, and
four for a pair with both coordinates nonzero. The two-coordinate loss
is charged exactly; its scalar set and full image are the same as the
unsigned square carrier. No asymptotic image theorem is claimed from
the two finite checks.

Thus these controls have full pair rate \(q=2a\), but no independently
proved smaller output rate. Their apparent extra formal rate is not a gain.

## 6. Exact finite conic/cubic chart audits

For every tested chart, the portable and raw records give \(Q_0,Q,N,Z\),
every pair and coordinate projection multiplicity, and the entire full
output-fiber decomposition. Exact physical scalars are either rational
or rational multiples of the fixed \(1/\sqrt3\). All denominators and
heights are available as exact fractions; no finite test replaces an
asymptotic height estimate.

The conic H2 example has \(N=10,Q=10,Z=2\), leaving 90 pairs; they
supply 81 new output values. The cubic H2 example has \(N=18,Q=14,Z=4\),
leaving 310 pairs; they supply 302 new output values. Incidental collisions
between selected and outside pairs are counted explicitly and do not
erase these complements.

These are EXPERIMENTAL finite records. The sparse families were stopped at
the minimal declared sizes; only completion audits on the same cached
carrier were added. No favorable \(q,a,b\) is extrapolated.
A serious successful family still needs both a near-full distinct pair
count and a subquadratic selected support. Their simultaneous achievement
in a compression construction remains OPEN.
