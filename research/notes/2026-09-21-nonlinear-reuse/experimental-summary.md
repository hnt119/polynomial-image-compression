# Nonlinear chart diagnostics: exact reuse and complement costs

T01, fixed polynomial \(P(x,y)=(x-y)^3+x+y\), 2026-09-21 v1.

**NR-X1 — EXPERIMENTAL.** One approved finite grid examined 16 chart
records on 12 distinct normalized scalar carriers. The largest carrier
had 18 inputs. Every distinct carrier's full square was enumerated once;
charts sharing it used the same exact cached output fibers. No old
three-branch, fixed-step, growing-step, or sublinear grid was rerun.

The new source is `experiments/nonlinear_reuse.py`; independent tiny
oracles are in `tests/test_nonlinear_reuse.py`; all portable counts are in
`examples/2026-09-21-nonlinear-reuse.json`. Complete raw records are under
`local-only/runs/T01/2026-09-21-nonlinear-reuse/`.

## Meaning and counting conventions

An exact coordinate-sharing identity can make several pair descriptions
reuse one scalar. It does not guarantee enough distinct selected pairs
to cover a scalar square. This grid records those quantities separately:

- \(Q_0\): formal parameter labels, including repetitions;
- \(Q\): distinct selected ordered pairs;
- \(N\): actual distinct scalars in either coordinate;
- \(Z=|P(\mathcal E)|\): selected output support;
- \(s=|P(A,A)|\): the actual full-square image;
- \(B=N^2-Q\): all uncovered ordered pairs.

For every chart the directly checked safe upper bound is
\(s\le Z+B\). No label repetition reduces \(B\), and no collision
energy is used as an image upper bound. Both scalar-projection fibers and
pair-projection fibers are stored in full.

## The fixed finite model list

**Reindexing controls, four records.** Let \(0\le r,s<m\), m=5 or 9,
and use \(x=f(r),y=f((s+r^2)\bmod m)\), with
\(f(j)=j^2\) or \(f(j)=j/(j+1)\). Each row permutes the same scalar
set, so this is exactly its full Cartesian square. Modulo reindexing is
not a bounded-degree rational chart. Its automatic full-square scalar
reuse is a control, not a new mechanism.

**Many-to-one controls, two records.** Put
\(x=r^2,y=s^2\), \(-m\le r,s\le m\), for m=3,5. These are polynomial
charts, but sign labels repeatedly describe the same actual pair. The
repetition is charged explicitly.

**Output-forced charts, two records.** For r,s in {1,2}, choose
\((U,Z)=(r+s^2,r+s)\) or \((rs,r+s)\), set \(L=Z-U^3\), then take
\(x=(L+U)/2,y=(L-U)/2\). Here U and Z have degree at most two;
L can have degree six. Both stop after this single illustrative size:
the resulting (N,Q) are (8,4) and (6,3), already displaying the sparse
completion cost. No larger output-forced search was performed.

**Conic charts, four records.** Use
\[
u=\frac{1-t^2}{1+t+t^2},\qquad
v=\frac{t(t+2)}{1+t+t^2},\qquad
t\in\{-1,-1/2,0,1/2,1\}.
\]
These obey \(u^2+uv+v^2=1\), so at a fixed output z the two first
coordinates agree. Put both corresponding pairs into the chart at
outputs z=2b, with b in {0} or {0,1}. Only these minimal H1/H2 records
are expanded. The other two records keep the H2 scalar carrier fixed
and add, respectively, transposed pairs and diagonal pairs, or every
remaining Cartesian pair.

**Nodal charts, four records.** Work exactly in units of
\(h=1/\sqrt3\). The physical carrier is A=hB and
\[
\frac{P(hx,hy)}h=\frac{(x-y)^3}{3}+x+y.
\]
All stored coordinates and outputs are rational coefficients of h; no
floating-point square root is computed. Use
\[
U=1-\frac{3(1+t^2)}{1-t^3},\qquad
V=-1-\frac{3t(1+t^2)}{1-t^3},\qquad
t\in\{-1,-1/2,0,1/2\}.
\]
For each b in {0} or {0,1}, the normalized outputs are
Z=2b and W=2b+4/3. Their first scalar coordinates coincide using
\[
x/h=(Z-U^3/3+U)/2,\qquad y/h=(Z-U^3/3-U)/2.
\]
As for the conic, the two additional H2 records add transpose/diagonal
pairs or the entire complement on the same scalar carrier.

The conic and nodal matchings are nonlinear rational relations, outside
the fixed affine-template and fixed-translation patterns in SC-R2/R3.
That scope distinction is not evidence of a positive rate. The conic
charts have (N,Q)=(6,5),(10,10); the nodal charts have (10,7),(18,14).
They stop at these minimal sizes because the selected pairs remain
comparable to the scalar count. The completion variants measure the
missing-pair cost and are not further candidate expansions.

## Complete exact result table

For nodal records, the output columns count physical outputs, equivalently
their exact rational coefficients in units of h. The last column is the
maximum actual fiber size on the full square.

| Model | N | Q0 | Q | Z | Full image s | Uncovered B | Safe Z+B | Max fiber |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| permuted squares m5 | 5 | 25 | 25 | 22 | 22 | 0 | 22 | 2 |
| permuted squares m9 | 9 | 81 | 81 | 78 | 78 | 0 | 78 | 2 |
| permuted rational m5 | 5 | 25 | 25 | 25 | 25 | 0 | 25 | 1 |
| permuted rational m9 | 9 | 81 | 81 | 81 | 81 | 0 | 81 | 1 |
| signed square m3 | 4 | 49 | 16 | 14 | 14 | 0 | 14 | 2 |
| signed square m5 | 6 | 121 | 36 | 33 | 33 | 0 | 33 | 2 |
| forced quadratic sum | 8 | 4 | 4 | 3 | 63 | 60 | 63 | 2 |
| forced product | 6 | 4 | 3 | 3 | 34 | 33 | 36 | 2 |
| conic H1 | 6 | 10 | 5 | 1 | 30 | 31 | 32 | 5 |
| conic H2 | 10 | 20 | 10 | 2 | 83 | 90 | 92 | 5 |
| conic H2 + transpose/diagonal | 10 | 50 | 24 | 14 | 83 | 76 | 90 | 5 |
| conic H2 + full complement | 10 | 110 | 100 | 83 | 83 | 0 | 83 | 5 |
| nodal H1 | 10 | 8 | 7 | 2 | 95 | 93 | 95 | 4 |
| nodal H2 | 18 | 16 | 14 | 4 | 306 | 310 | 314 | 4 |
| nodal H2 + transpose/diagonal | 18 | 50 | 46 | 35 | 306 | 278 | 313 | 4 |
| nodal H2 + full complement | 18 | 326 | 324 | 306 | 306 | 0 | 306 | 4 |

## Scalar reuse and collisions outside the charts

The m5 signed-square chart has 121 labels but only 36 selected pairs.
Its pair-projection multiplicities are one pair with multiplicity 1,
ten with multiplicity 2, and 25 with multiplicity 4. The actual image
has 33 values. This separates repeated descriptions from output collisions.

The conic H2 chart uses 10 selected pairs and 10 scalars, with only two
selected outputs. Those are complete five-point fibers: no outside pair
shares either selected output. The other 90 pairs supply 81 entirely new
outputs. The full fiber histogram is 72 singletons, nine doubletons, and
two fibers of size five. The selected support therefore gives no control
over most of the Cartesian square.

The nodal H2 chart uses 14 selected pairs and 18 scalars. Among its 16
labels, twelve pairs occur once and two occur twice. The selected support
contains four outputs; two additional pair vertices outside the chart
land on selected outputs, creating six selected/outside collision pairs.
The complement nevertheless contributes 302 new output values. The full
fiber histogram is 297 singletons, four doubletons, one triple, and four
four-point fibers. Its actual image has 306 values out of 324 pairs.

The records report both formal coordinate reuse \(2Q_0/N\) and actual
selected-pair coordinate reuse \(2Q/N\). For the conic H2 these are
4 and 2; for the nodal H2 they are 16/9 and 14/9. Counting formal labels
instead of actual selected pairs would overstate both reuse and coverage.

All records separately count selected/selected, selected/outside, and
outside/outside unordered collision pairs. They also retain the actual
selected and outside vertices in every full output fiber. Thus incidental
collisions are included without replacing the safe complement bound by
an energy heuristic.

## Reproducibility and exact budget

The approved allocation was at most 36 model charts, 160 scalar inputs per
carrier, 400,000 full-square polynomial evaluations, 3,000,000 checks,
and a self-imposed 60 research CPU seconds. Input-only preflight recorded
all chart sizes and stop reasons before enumeration: 16 records,
12 normalized carriers, maximum N18, and 924 required full-square
evaluations. It took 0.002472 CPU seconds and 980 constructor-label checks,
with no full-square evaluation.

After inspecting the complete new code, the single run was
`python3 -m experiments.nonlinear_reuse`, using CPython 3.12.7 and
standard-library `Fraction`. There was no network access, randomness,
dependency installation, or old-grid rerun. Its measured work was:

| Research category | Count |
|---|---:|
| Formal label construction checks | 980 |
| Full-square polynomial evaluations | 924 |
| Formal chart-pair checks | 980 |
| Per-chart full-square coverage checks | 1772 |
| Fiber-overlap checks | 1642 |
| Total | 6298 |

Research CPU time was **0.036732 seconds**, wall time 0.037140 seconds.
All scheduled models completed without errors or resource stops. The
declared sparse-family stops prevented any further size expansion.

Four targeted tests passed, covering an independent conic rational oracle,
an independent nodal normalized oracle and excluded pole, actual Q0/Q
separation with a hard-coded four-output example, safe full completion,
and the declared preflight. Tests used eight additional polynomial
evaluations (four full-square and four direct identity evaluations),
1013 checks including constructor labels, and 0.003102 measured CPU
seconds. Their exact work is in `targeted-verification.json`.

The 12 raw carrier certificates contain the entire normalized output
support, every fiber's pair vertices, and the complete ordered-pair output
map. The 16 raw chart certificates contain every parameter/pair projection
fiber, every coordinate occurrence, and selected/outside membership for
every actual output. All 28 raw hashes matched; the source and portable
summary hashes also matched. This byte audit used 0.001992 CPU seconds
and was not a mathematical rerun. The new writer rejects overwriting any
individual artifact. `git diff --check` passed.

Source SHA-256:
`4bc2201e00eafdb6eba4ac31705de512b1751b317d52e71f12cb08c2c87f282b`.
Portable summary SHA-256:
`a87f5e7ca346b2865c018cee2d00a89d4dc7d8abca276552376f940d11719c62`.
`provenance.json`, `targeted-verification.json`, and
`artifact-verification.json` record the commands, runtime, parameters,
limits, hashes, and absence of errors.

Including input preflight, this new grid, and the targeted test run, this
agent used **932 polynomial evaluations and 8291 charged checks**.
Root's proof audits and later repository regressions are separate. No
full-suite result is claimed in this subtask.

## Claim scope

NR-X1 is T01 / nonlinear coordinate reuse, the fixed polynomial displayed
above, 2026-09-21 v1. Its quantifiers are restricted to the explicit finite
models. Evidence is complete exact enumeration, preserved raw certificates,
and targeted independent numeric oracles. The conic and nodal symbolic
identities are supplied by the current cycle's proof work; these finite
tests do not replace their proofs. No independent general proof audit or
novelty claim is made here.

The grid confirms coordinate coincidences while exposing their selected
coverage and complement costs. It supplies no asymptotic nonlinear chart,
power-saving exponent, or universal nonlinear-reuse obstruction. The fixed
cubic target remains **OPEN**.
