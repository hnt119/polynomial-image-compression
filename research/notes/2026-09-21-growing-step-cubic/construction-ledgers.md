# Full construction and rate ledgers

T01 / growing-step cubic, 2026-09-21 v1. Fixed real polynomial
\(P(x,y)=(x-y)^3+x+y\). This document instantiates
[the construction-ledger template](../../templates/CONSTRUCTION_LEDGER.md).
The same actual scalar set supplies both inputs throughout.

## 1. Identity, provenance, and permitted scope

The user commissioned a new offline attack on CR-O1 after the completed
fixed-step report. Network policy: no access. Declared overall cap: 80
carriers, 240 carrier/inventory cases, 128 actual inputs per carrier,
3,000,000 exact pair/edge checks and 90 research CPU seconds. The approved
experiment used a tighter 60-carrier/200-case/2,000,000-check/60-second
allocation, with its 32-by-six grid fixed before execution.

Dependencies: the frozen conjugacy and CR-U1; the frozen elementary
crossing argument for the new joint-step proof; and the new GS-P, GS-A,
and GS-U arguments in the three proof companions. These new arguments
were independently checked internally as recorded in [verification.md](verification.md).
No missing historical checkpoint is a dependency. No arithmetic
amplification, literature check, or novelty claim is made.

## 2. Progression and moderate-width lattice carriers

**Exact construction and coverage.** For \(A_{r,N}=I_N/r\),
\(r=1,3\), choose the spacing before \(N\) grows. All \(N\) scalar
points are distinct. For \(S=\{1,\ldots,M\}\), all components are
actual fibers as soon as \(M\ge1\). The actual image equals
\(N^2-E_1\), not just a component upper bound.

For general \(A\subset a+h\mathbb Z\), use the actual size \(N\)
and diameter \(D\); do not substitute the enclosing interval's population
for the input. GS-U3 bounds all nonsingleton-fiber mass through
\(W=D/h^3\). It charges a varying mesh explicitly.

| Template charge | Account |
|---|---|
| Input lower and upper count | Exactly \(N\) for APs; actual subset count \(N\) for the lattice theorem |
| Thinning in both coordinates | None for APs. If a subset is used, its actual \(N^2\) is the pair count |
| Parameter/projection fibers | AP indices map injectively; the general theorem is already about distinct scalar inputs |
| Local sparsity, splitting, per-residue population | No local lifting. The fixed modulo-nine calculation identifies steps; it gives no amplification gain |
| Field degree, discriminant, regulator, units | No growing field or unit construction; rational examples have degree one |
| Heights, moduli, denominators | AP diameter \((N-1)/r\), fixed denominator \(r\). General mesh/width enter as \(D/h^3\); no uncharged shrinking denominator |
| Archimedean distortion | No projection distortion; the actual diameter is used in every displacement bound |
| Branches, ratios, carries | No branch or carry model in these proofs |
| Inventory | \(M\) actual positive steps, but only \(\Theta(N^{1/3})\) distinct integer steps can ever return on the two APs |
| Edges and components | Edges \(\Theta(N^{3/2}\sqrt{\min(M,N^{1/3})})\); components \(N^2-E_1\) for every \(M\ge1\) |
| Exceptional/uncovered pairs | Only \(\Theta(N^{3/2})\) AP pairs lie in nonsingleton fibers. The other \(N^2-O(N^{3/2})\) are actual singleton outputs |
| Final rate | With \(d=\log N\), \(a=B=1\), actual output rate \(c-s=2\), so \(\Delta=2a-(c-s)=0\) |
| Fixed exponent | None. FAILED actual-image family; this is stronger than a failed upper certificate |

For a full AP with varying \(h\), the lattice obstruction applies when
\(h\sqrt N\to\infty\). This is a hypothesis, not a free normalization:
scaling changes the relative cubic and linear terms of the fixed polynomial.

## 3. Full shared-coordinate cubic grids

**Parameters and input.** Choose integers \(H,L\ge1\) and the exact
carrier of GS-P3, consisting of the two integer-coordinate maps over
\(0\le b<H\), \(1\le j\le L\). It has at most \(2HL\) elements;
the proof obtains the distinct lower count from

\[
N\ge H+\sum_{j=1}^{L-1}\min\{H,3j(j+1)/2\}.
\]

Parameter collisions are deliberately allowed and counted through this
actual union size. The prescribed pair map is injective because \((z,u)\)
recovers the pair. There are exactly \(HL\) prescribed pairs, so scalar
reuse is measured as \(HL/N\), not as a parameter-label count.

| Template charge | Account |
|---|---|
| Input lower/upper bounds | Displayed union lower bound; upper \(2HL\). For \(H=L^3\), exact \(N=(3L^3+L)/2\) |
| Thinning, both inputs | None; every one of the \(N^2\) pairs still belongs to the task |
| Projection multiplicity | Coordinate labels may repeat; actual cardinality proved. Prescribed pair labels are distinct |
| Local/field/arithmetic quantities | All coordinates are integers; \((j^3\pm j)/2\) is integral. No splitting, field degree growth, discriminant, regulator, local modulus or residue populations |
| Heights/diameter | Absolute coordinate size and diameter \(O(H+L^3)\), explicitly charged |
| Branches | Two scalar coordinate branches over a full \(H\)-by-\(L\) parameter grid |
| Inventory/edges | Step 1 connects each prescribed fiber segment; at most \(L-1\) positive integer gaps fill each one. Prescribed edges are \(H\sum_{k\le M}(L-k)_+\) for steps 1 through \(M\) |
| Prescribed pair gain | \(HL\le4N^{4/3}\); order attained at \(H=L^3\) |
| All uncovered outputs | At least \(N^2-HL\) pairs remain outside the prescribed list. Treating them individually gives the valid support upper certificate \(H+N^2-HL\), still of quadratic order |
| Rates | In units \(d=\log N\), input \(a=B=1\); prescribed coverage rate at most \(4/3\), full output certificate rate 2, \(\Delta=0\) |
| Disposition | FAILED prescribed-coverage certificate. At \(H=L^3\), the actual carrier is an interval and its actual image is also proved quadratic |

Incidental pairs are not assumed singleton outside the specified actual-
interval regime. Their support remains separately charged, not erased.

## 4. Faithful coefficient boxes

**Parameters and projection.** Fix rank \(r\ge2\), then let side length
\(L\) grow. Choose exactly \(B=100(L+1)^3\), weights
\(w_0=1,w_i=B^{4^{i-1}}\), and all digits \(0\le a_i<L\).
The scalar projection is injective; \(N=L^r\) exactly. The proof also
shows output coefficients survive the projection, using an explicit
coefficient-difference bound smaller than \(B\).

| Template charge | Account |
|---|---|
| Input lower and upper count | Exactly \(L^r\); no formal-state count replaces it |
| Thinning in both coordinates | None; \(L^{2r}\) pairs retained |
| Projection fibers | Exactly one for inputs. Cubic output collisions classified completely by GS-P4 |
| Local/field quantities | Integer scalar construction, degree one; no splitting, regulator, discriminant or local-population estimate |
| Heights/denominators | Denominator one; diameter at most \(rL B^{4^{r-2}}\). For fixed \(r\), this is polynomial in \(L\) with the stated exponent |
| Archimedean cost | Large separation is explicit. No bounded-radius or volume certificate is claimed |
| Branches/carries | \(r\) input places, all cross monomials of degree at most three retained. Base-four exponent encoding separates monomials; modulo-\(B\) recovery proves absence of output carries |
| Useful connected pairs | Every nontrivial actual fiber lies in one identical-higher-digit slice; their total mass is \(\Theta_r(L^{r+1/2})\) |
| Inventory | All actual nontrivial steps are interval steps within those slices; step 1 already connects every actual fiber. Any larger inventory cannot join different outputs |
| Entire image | Exactly \(N^2-L^{r-1}E_1(I_L)\), including every off-slice pair, whose output is unique |
| Rates | With \(d=\log L\), \(a=B=r\); actual output exponent \(2r\), subtracted saving of order \(L^{r+1/2}\), net \(\Delta=0\) |
| Disposition | FAILED actual-image family and structural classification. Nonfaithful scalar projections are outside scope |

No growing field is smuggled into the projection, and no local theorem is
used. This is a new finite-rank coefficient identity, not a rerun of the
historical regular-language search.

## 5. Recursive rational completion and the finite models

For fixed rational \(A_0,C\), \(|C|\ge2\), GS-P5 proves
\(m+1\le N_m\le D_m/h+1=O(m+1)\), where
\(D_m=D_0+m\operatorname{diam}(C)\) and the common mesh \(h\) is fixed.
Label multiplicities in the \(|C|^m\) formal words are therefore large;
they are not scalar growth. With \(d=\log(m+1)\), the input rate is one
and the actual output rate is two. There is no positive gap, regardless of
the chosen graph inventory. No thinning, field extension or exceptional
pair deletion is used.

The two tested levels used \(C=\{0,-1,4/27,-5/27\}\), denominator 27,
and the six-point seed. They have actual counts 16 and 30, versus 24 and 64 coordinate
occurrences at those transitions (96 formal two-stage labels before
deduplication). The general theorem controls all later
depths of this same recursion. Nonlinear or changing-shift completion is
not covered by that statement.

The tested rational coefficient boxes also charge duplicate parameters:
for side 8 and weight \(3/2\), 64 labels produce only 34 scalars; for
weight \(5/3\), they produce 49. These fixed-weight families have fixed
mesh and diameter \(O(N)\), so GS-U3 closes their growing versions. For
weight \(L+1/3\), the \(L\) scalar blocks are disjoint and \(N=L^2\),
with fixed mesh \(1/3\) and diameter \(O(N)\); GS-U3 again applies.

Planted multiple fibers in the finite grid use their actual scalar unions,
with every cross pair evaluated. Their coordinate-occurrence/scalar ratio
and prescribed-pair fraction are recorded separately. No asymptotic image
theorem for every such planted family is asserted from this experiment.

For every finite inventory the data record the actual step list, size,
common rational denominator, numerator/denominator bit lengths, and
serialized size. The “all useful steps” case is explicitly diagnostic.
It recovers full actual fibers by construction and does not provide a
bounded-complexity asymptotic realization.

## 6. Evidence and disposition

The proofs, experiments, audits and regression results are separated in
[verification.md](verification.md). The deterministic research grid was
executed once; finite evidence is exact over its declared range only.
All raw inputs, graphs, fibers, output supports and hashes are preserved
in the ignored local run directory. No historical archive or previous
canonical JSON was overwritten.

No ledger here has \(\Delta>0\). The main report retains one next
obligation, the sublinear-inventory subcase of CR-O1, with actual scalar
reuse and almost-full component coverage still to be supplied.
