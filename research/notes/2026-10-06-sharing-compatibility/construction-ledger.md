# Counting and provenance ledger for the sharing triangle

T01, 2026-10-06. Fixed polynomial P(x,y)=(x-y)³+x+y.
Research authorized by the current “Offline: compatibility between multiple
cubic sharing curves” request. The only network is a directed scalar triangle
(a,b),(b,c),(c,a) whose ordered outputs are (z,z+h,z+2h), with the fixed
spacing h=2r, r=1/√3. Assemblies are unions of translates of its real branch.
No other network, carrier search, elliptic factorization or arithmetic tower
is commissioned by this record.

## Source and claim identity

The controlling source is the 2026-09-30
[elliptic report](../2026-09-30-elliptic-geometry/README.md), with its genus,
group-law, complex-extension and construction companions. Its accepted
obstructions are imported with their stated scope; they are not independently
reproved in this cycle. The coordinate parametrization and the mixed-coordinate
sharing identity are checked by substitution here.

The new proofs are SH-G1–SH-G3 in geometry.md and SH-C1–SH-C2 in
construction.md. SH-C3 is the explicit application of the existing GS-A4
fixed-spacing progression bound, with its scalar-square specialization
checked here. SH-X1 is exact finite evidence, not a theorem about untested
sizes. All claims use this fixed T01 polynomial, characteristic zero and real
endpoints; date/version is 2026-10-06 v1. Exact file hashes and the completed
internal reviews are recorded separately in verification.md and the local
manifest. No external review or novelty claim is made.

The master/current-state/checkpoint and repository scope records were read.
MC-06's absent historical digital and rich-fiber originals remain absent.
They are not dependencies of these new compatibility proofs.

## Equations fixed before computation

For u=a−b, v=b−c and w=c−a, simultaneous closure requires
\[
u+v+w=0,\quad
u^3-v^3+u+v=-h,\quad
v^3-w^3+v+w=-h,\quad
w^3-u^3+w+u=2h.
\]
The first relation follows by summing the last three as well. Eliminating w
and recovering b from the first prescribed output gives the necessary and
sufficient system
\[
v^3-u^3-u-v=h,\qquad
2u+v-3v(u^2+uv+v^2)=0,\qquad
2b=z-u^3-u.
\]
Each edge is a mixed-coordinate sharing equation. The variables used on
incident edges are the same variables; separately selected edge solutions
are not counted as a closed network.

These equations and their signs were derived and independently confirmed
before any finite run. The geometry proof was saved and the scout code
inspected before execution. The eight predeclared strip sizes are
m=1,2,3,4,8,16,32,64. They are instances of this one branch, not a parameter
search or a rerun of the earlier progression inventory.

Total ceiling: 12 finite instances, 50,000 P evaluations and 10,000 exact
compatibility/accounting checks. All three specialists and the lead share
this budget. Network and installation policy: none. Arithmetic:
standard-library exact integers and fractions only.

## Exact real construction and full-square charge

PROVED — SH-G3 and SH-C1. For h=2r, every real compatible triangle is
\[
(a,b,c)=(t-r,t,t+r),\qquad z=2t-\frac43r.
\]
For a nonempty finite T⊂R, put
\[
A_T=T+\{-r,0,r\},\quad N=|A_T|,
\]
and let E_T be the distinct ordered pairs supplied by its triangles.
This uses both coordinate positions and no universal fixed anchor. There
are |T|≤N≤3|T| distinct input scalars, regardless of overlap.

The selected output set is exactly
\[
P(E_T)=2T+\{-4r/3,2r/3,8r/3\}=2A_T+2r/3,
\]
so Z=N. The only differences of selected ordered pairs are −r and 2r.
Forgetting orientation injects them into edges of lengths r and 2r.
In increasing scalar order, every vertex has at most two larger neighbors,
the largest has none, and the second largest has at most one. Hence
\[
Q=|E_T|\le2N-3,\quad
B=N^2-Q\ge N^2-2N+3,\quad
|P(A_T,A_T)|\le Z+B=N^2-Q+N.
\]
The last expression is a safe upper certificate; its lower bound
N²−N+3 is not a lower bound on the actual full image for arbitrary T.

For the strip T={r,2r,…,mr}, m≥1,
\[
A=\{0,r,\ldots,(m+1)r\},\quad
N=m+2,\ Q=2m+1=2N-3,\ Z=N,\ B=N^2-2N+3.
\]
Its 3m raw edge occurrences reduce to 2m+1 distinct (z,u) labels and
the same number of distinct actual ordered pairs. The three one-pair
selected outputs and m−1 two-pair selected outputs account for Q exactly.
The strip attains the sharp coverage bound for this fixed network family.

## Quantitative costs

| Item | Bound and interpretation | Status |
|---|---|---|
| Input count | General t≤N≤3t, where t is the cardinality of T; strip N=m+2 | PROVED |
| Input thinning in both coordinates | None. All N² pairs of the scalar union are charged | PROVED |
| Parameter and label fibers | Translation t uniquely identifies its triangle; raw edges are deduplicated. Strip 3m occurrences give 2m+1 actual pairs | PROVED |
| Endpoint reuse | Sharp Q≤2N−3 across arbitrary translations, attained by the strip | PROVED |
| Output count | Z=N exactly for the prescribed union; entire image counted separately | PROVED |
| Field and projection | Fixed positive real r=√3/3. Strip inputs lie in Q(√3), degree 2; the integer basis (1,√3) has discriminant 12. This contributes no growing field or projection multiplicity | PROVED |
| Regulator, units and splitting | Inapplicable: no units, extension tower, prime splitting or local population estimate is used | PROVED |
| Heights and denominators | Strip input coefficient height O(m), output coefficient height O(m³); basis denominators 3 for inputs and 9 for outputs are fixed. No scaling of P or clearing inputs is used | PROVED |
| Archimedean size | Strip diameter (m+1)r. For arbitrary T no radius bound is assumed or counted as a gain | PROVED |
| Branches and singularities | One real compatible branch for the fixed output gap, by SH-G2/G3; no discarded real branch | PROVED |
| Carries and moduli | Inapplicable: exact fixed-field scalar equality, no digital encoding | PROVED |
| Uncovered outputs | Every one of B=N²−Q pairs may contribute one new output; none discarded | PROVED |
| Certificate exponent | Z+B≥N²−N+3 within the family, so no positive saving from this certificate | PROVED |
| Actual strip image | Imported GS-A4 gives N²−O(N^(3/2)); specialization and exact band count checked in SH-C3 | PROVED |
| Actual arbitrary-T image | No uniform quadratic lower bound or power-saving construction established | OPEN |
| Rate ledger | In depth log m, log N=log m+O(1); both strip actual image and prescribed certificate have exponent 2. No positive delta or c_P | PROVED |

The failure of the planted-pair certificate for all T and the actual-image
failure of the strip are separate results. Neither is a theorem excluding
all cubic sharing networks or all real sets.

## Evidence and disposition

The exact computation is confined to the eight declared strips and their
complete Cartesian squares. Full fibers, threshold tails, scalar and pair
deduplication, raw-label multiplicities and code/input hashes accompany
SH-X1. The new run and inherited finite regressions are reported separately.

The report's sole next obligation SH-O1 concerns the remaining actual-image
question for arbitrary T in this same translate family. It is not asserted
equivalent to the original target or to be a new constructive reduction.
The unrestricted fixed-cubic target remains OPEN.
