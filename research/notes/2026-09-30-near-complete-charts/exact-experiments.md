# Exact all-pair completion and cumulative fiber audit

T01, 2026-09-30 v1. **NC-X1 / EXPERIMENTAL**, fixed
\(P(x,y)=(x-y)^3+x+y\). Six predetermined new carriers; exhaustive on
each resulting finite square, not an exhaustive search over formulas or sets.
No old carrier grid was rerun.

## Inputs, charts and domain

Seeds are S1={0,1/3,1/2} and S2={0,1/4,1}. Fix one seed and one
of three rules, then apply its three branches to every seed pair.
The branches act on u=x−y, z=P(x,y), retain z, and invert using
\(x=(z-u^3+u)/2,y=(z-u^3-u)/2\).

- Adaptive linear: u, u+z/2, u−z/2.
- Adaptive quadratic: u, u+z²/2, u−z²/2.
- Möbius: u, 1−1/u, 1/(1−u). Both nonidentity branches are omitted
  at u=0 or u=1 to retain a complete finite-cycle domain. This is stricter
  than each branch's individual pole exclusion. Identity is always included.

The pair E is a set, not a list of labels. Its scalar union A includes every
coordinate. The program computes all of A², including new cross-pairs.
The raw record retains each (branch,seed-row,seed-column) label above each
actual pair, and formal versus distinct-pair coordinate multiplicities.
All equalities and output ordering use exact standard-library Fraction.

The construction is an output-adaptive all-pair assembly rather than a
fixed-step or isolated-rational-curve search. Each candidate stops after
its first completion, because measured scalar expansion leaves only about
2–4% pair coverage. This is an early finite rejection, not a proved
asymptotic failure for all iterations of its defining rule.

## Complete histograms and scalar costs

Histogram entries are **fiber size: number of outputs of that size**.
Actual reuse counts both coordinate positions of each distinct selected pair.
The denominator is a valid common denominator of all actual input scalars.

| Model | N | Full fiber histogram | Mean actual scalar reuse 2Q/N | Common denominator |
|---|---:|---|---:|---:|
| third_half_adaptive_linear | 35 | 1: 1189, 2: 4, 3: 4, 4: 4 | 10/7 | 161243136 |
| third_half_adaptive_quadratic | 35 | 1: 1199, 3: 6, 4: 2 | 10/7 | 1624959306694656 |
| third_half_mobius_threecycle | 27 | 1: 708, 2: 1, 3: 5, 4: 1 | 14/9 | 148176000 |
| quarter_one_adaptive_linear | 26 | 1: 647, 2: 4, 3: 3, 4: 3 | 21/13 | 4194304 |
| quarter_one_adaptive_quadratic | 30 | 1: 871, 2: 4, 3: 5, 6: 1 | 23/15 | 1099511627776 |
| quarter_one_mobius_threecycle | 23 | 1: 511, 2: 1, 3: 4, 4: 1 | 38/23 | 148176000 |

The main report gives every N,Q0,Q,Z,B, full-image and safe-certificate
count. The portable record additionally stores all pair and output chart
intersections and the disjoint-assignment quantities used in NC-H2.
These are measured values; neither scalar reuse nor chart overlap is inferred
from the number of formal labels.

## Full cumulative profiles

For every carrier the portable JSON contains every entry of C_A(k),
0<=k<=s, together with the exact output value ordering and all fiber sizes.
Ties are resolved by increasing exact rational output. It also records:

- the optimum controlled subset using k=floor(N^(3/2)) outputs, with
  this floor computed as integer square root of N³;
- the minimum output count reaching 50%, 90%, 99% and 100% of pair mass;
- actual small-fiber pair-mass tails for thresholds 2,3,4 and ceil(sqrt(N));
- a hierarchy that takes the next largest complete fibers until at least
  half of the remaining pair mass is covered at each stage.

The hierarchy uses disjoint output sets, so its final output charge is
exactly the full image. It takes 10–11 stages in the six examples. This is
an accounting control: coverage contracts geometrically, but support remains
large. All curves and stages are derived from the one cached full enumeration;
there is no additional carrier evaluation or output-budget search.

At least 95% of pair mass in every scout is in singleton fibers. For all
six, k=floor(N^(3/2)) already includes every nonsingleton fiber. Consequently
its safe certificate k+N²−C_A(k) equals the full image exactly, even though
most pairs are still outside the selected subset. This illustrates the
singleton ties in NC-C1, not success at near-complete coverage.

## Raw certificates and execution

Portable results: [exact JSON](../../../examples/2026-09-30-near-complete-charts.json).
The six raw files under local-only/runs/T01/2026-09-30-near-complete-charts/
contain all normalized scalars, all output fibers and pair vertices, selected
members of each fiber, label projections, and coordinate occurrences.
No imported program or serialized object was executed.

The complete new source and four independent tiny tests were inspected
before the single research execution. The command was
`python3 -m experiments.near_complete_charts`, with CPython 3.12.7.
Maximum N was 35; pre-enumeration guards enforce N<=128. The declared
ceilings were 24 carriers, 200,000 polynomial evaluations and 2,000,000
additional checks. The actual run used:

| Category | Count |
|---|---:|
| Seed-square evaluations | 54 |
| Full new-square evaluations | 5284 |
| Total polynomial evaluations | 5338 |
| Constructor label checks | 148 |
| Prescribed-output checks using cached full outputs | 148 |
| Full-pair accounting records | 5284 |
| Fiber-profile records | 5178 |
| Chart-overlap membership charges | 296 |
| Global accounting assertions | 18 |
| Total additional charged checks | 11072 |

These are the declared counting categories, not a claim to count every
integer instruction, Fraction operation, sorting comparison or rendering
operation. No floating-point equality was used. CPU time was 0.124286
seconds, wall time 0.124323 seconds. There was no randomness, network,
resource stop or run error. Writes reject existing files, and the research
run was not repeated for final checking.

Code SHA-256: `de1beaca50f0019d77e57945ed21e148c86b5d03be56f9ef2bbaca8c4e939779`.
Portable SHA-256: `eccae07a38a5de796b9fd50596aba55d06a265202ed98368eb7087e757bde08f`.
All complete raw certificates have separate SHA-256 references in the JSON.
The verification companion separates code tests and byte checks from
mathematical proof audits. None of these finite data proves an asymptotic
cubic obstruction or a positive exponent.
