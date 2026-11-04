# Exact variable-output gluing: finite evidence and referee audit

T01, 2026-10-06, version 1. Fixed polynomial
\(P(x,y)=(x-y)^3+x+y\), with the same real scalar set in both coordinates.
**VG-X1 — EXPERIMENTAL:** three exact, exhaustive full-square checks of the
one prescribed output-window family, at \(k=3,4,5\). The complete proofs
VG-G1–VG-G3 and VG-C1–VG-C3 received a separate independent internal audit
by the exact-computation/referee role. Neither finite evidence nor agent
agreement is substituted for those displayed proofs.

## 1. Proof and release came before enumeration

The [compatibility proof](compatibility.md) and
[construction proof](construction.md) were saved and independently checked
before execution. The evaluator and tests were then read in full by the
lead. The canonical block choice was aligned with construction equation
(C10), and the worked motif was aligned between proof, code and tests.
Only after the final two proof hashes were confirmed did the lead release
the following command:

```text
python3 -m experiments.variable_gap_sharing --proofs research/notes/2026-10-06-variable-gap-sharing/compatibility.md research/notes/2026-10-06-variable-gap-sharing/construction.md
```

The command ran **once**, with exit code 0 and no errors. There was no
earlier carrier enumeration, root search, former fixed-gap scout, old
progression inventory, alternative carrier, random sampling, installation,
or network use. Reading the resulting JSON later did not reevaluate P.

The chosen labels, before reconstructing any scalar, were exactly
\[
L=k^3,\qquad 1\le|u|\le k,\qquad
\frac{u^3+|u|}{2}\le j\le
L-1+\frac{u^3-|u|}{2},\quad j\in\mathbb Z.
\]
The endpoints and output are then
\[
x=j-\frac{u^3-u}{2},\qquad
y=j-\frac{u^3+u}{2},\qquad z=2j.
\]
All halves are integral. Computation uses Python standard-library integers;
`Fraction` is used only to display exact ratios. No floating-point equality
or approximate algebraic-number comparison occurs.

## 2. What was exhaustively checked

The code first constructs the allowed \((j,u)\) labels and their actual
ordered pairs. It deduplicates endpoint scalars and checks that pair and
label counts agree. It verifies the derived scalar union
\(A=\{0,\ldots,L-1\}\), the exact pair count and the complete selected
output interval. The pair set is contained in
\(1\le|x-y|\le k\) and has that band's entire cardinality, proving
finite equality with the band without a second square enumeration.

For **every** selected base edge \((a,b)\), the code uses the proven
canonical block
\[
s=\max\{0,\max(a,b)-k\},\qquad [s,s+k]\subseteq A.
\]
It records all \(k-1\) remaining block vertices and chooses the first two
as \(c,d\). Each of the four non-base edges
\((b,c),(c,a),(b,d),(d,a)\) is explicitly checked against the already
constructed label map. All four vertices are checked distinct, and every
base edge receives one such motif. Thus there are no unrepresented
boundary edges in the selected set.

Crucially, these other edges receive their labels by lookup in the
**predeclared windows**, not by inventing output names after evaluating
new free scalar tuples. Repeated motifs do not create new pairs. There
are \(Q\) canonical double triangles and \(5Q\) recorded motif-edge
occurrences, but their actual pair union still has exactly \(Q\) pairs.
All partner combinations were not enumerated; the general partner count
is proved in VG-C2. The same block proof puts the cross-partner edges
\((c,d),(d,c)\) in the selected band; these are already among the globally
checked selected edges, not an additional output allowance.

Finally, **every ordered pair of the actual scalar union** is evaluated
once and assigned to its exact full output fiber. Selected labels are
checked against those cached values, without extra hidden P evaluations.
No diagonal or large-difference pair is discarded. Raw data contain all
full fibers, all integer strict small-fiber tails through \(N+1\), ranked
fiber sizes, the prescribed windows, labels and canonical motifs.

## 3. VG-X1: counts, reuse, coverage and actual images

The formulas in this table are proved for all \(k\ge3\) in VG-C1–VG-C3:
\[
N=k^3,\quad Q=2k^4-k(k+1),\quad Z=2k^3-k,\quad B=N^2-Q.
\]
The finite entries below all passed exact checks.

| k | N | Q | Z | B | 2Q/N | Q/Z | Q/N² | Safe bound Z+B | Entire image |
|---:|---:|---:|---:|---:|---|---|---|---:|---:|
| 3 | 27 | 150 | 51 | 579 | 100/9 | 50/17 | 50/243 | 630 | 593 |
| 4 | 64 | 492 | 124 | 3604 | 123/8 | 123/31 | 123/1024 | 3728 | 3580 |
| 5 | 125 | 1220 | 245 | 14405 | 488/25 | 244/49 | 244/3125 | 14650 | 14185 |

The certified numbers of block partners per base edge are respectively
2, 3 and 4. These certify respectively at least 2, 6 and 12 ordered
choices of two distinct partners; only one canonical choice was saved
per base edge. No partner or motif multiplicity is counted as a new
scalar pair or a support reduction.

The complete full-fiber histograms are:

| N | Fiber size : number of outputs |
|---:|---|
| 27 | 1:550, 2:16, 4:2, 5:11, 6:14 |
| 64 | 1:3430, 2:62, 3:20, 4:4, 5:2, 6:8, 7:24, 8:30 |
| 125 | 1:13768, 2:212, 3:56, 4:18, 5:6, 7:2, 8:10, 9:61, 10:52 |

Absent fiber sizes have count zero. For the strict pair-mass tail
\(B_A(t)=\sum_{z:r_A(z)<t}r_A(z)\), some representative exact values
are:

| N | B_A(2) | B_A(3) | B_A(5) | ceil(sqrt N) | B_A(ceil(sqrt N)) |
|---:|---:|---:|---:|---:|---:|
| 27 | 550 | 582 | 590 | 6 | 645 |
| 64 | 3430 | 3554 | 3630 | 8 | 3856 |
| 125 | 13768 | 14192 | 14432 | 12 | 15625 |

These finite histograms are not an asymptotic theorem. The actual interval
image theorem is the independently identified GS-A4 import in VG-C3.

## 4. Worked nondegenerate shared-edge motif

Take \(k=3,L=27\) and
\((a,b,c,d)=(1,0,2,3)\). All five labels below lie in the windows chosen
before reconstruction:

| Edge | Prescribed label (j,u) | Reconstructed endpoints | P value |
|---|---|---|---:|
| (a,b) | (1,1) | (1,0) | 2 |
| (b,c) | (−3,−2) | (0,2) | −6 |
| (c,a) | (2,1) | (2,1) | 4 |
| (b,d) | (−12,−3) | (0,3) | −24 |
| (d,a) | (6,2) | (3,1) | 12 |

The four vertices and five outputs are distinct in this worked example.
The general family requires distinct vertices, but does not require five
distinct outputs in every motif. The exact shifts from VG-G3 recover the
four non-base labels from \((j,u)=(1,1)\), with partner differences
\(v=-2,t=-3\). These values were checked by hand before execution and
are retained as a small independent regression oracle.

## 5. Referee findings: complete proofs and their limits

The referee read the complete compatibility and construction companions,
the earlier full output-by-difference grid proof
[GS-P3](../2026-09-21-growing-step-cubic/structure-and-reuse.md), and
the fixed-spacing theorem
[GS-A4, §4](../2026-09-21-growing-step-cubic/progression-laboratory.md).
No defect or required correction was found in the final VG-G1–VG-G3 and
VG-C1–VG-C3 arguments. The following possible overclaims were specifically
checked:

- **Simultaneous gluing:** VG-G1 uses one common edge, difference and anchor
  in both triangles. The reconstruction proves both directions of all four
  remaining output equations. The six nonzero/distinct difference tests
  exactly characterize four distinct scalar vertices. Boundary tests in
  VG-G3 are necessary and sufficient, not an assumption that arbitrary
  independently chosen curve points glue.
- **Even-cycle uniqueness:** the cyclic comparison matrix may be singular
  when its \(k_i\) all vanish. The proof additionally uses
  \(k_i=u_i^2+u_i u_i'+(u_i')^2=0\Rightarrow u_i=u_i'=0\).
  Thus \(\alpha_i-\alpha_{i+1}=0\), while equal outputs give
  \(\alpha_i+\alpha_{i+1}=0\). Both imply \(\alpha_i=0\).
  The alternating linear kernel is not realizable by scalar differences.
  Neither a determinant assertion nor a positive-Jacobian heuristic is
  substituted for this geometric step.
- **Output-first order:** the windows are specified before the scalar
  union. Their exact endpoint reconstruction, injective pair labels,
  interval-overlap calculation and selected support \(Z=2k^3-k\) all
  check. The final carrier nevertheless equals an integer interval; the
  order of its description does not exempt it from existing carrier
  obstructions.
- **Every-edge coverage:** the canonical block lies inside \([0,L-1]\)
  even at the boundary and contains both base endpoints. It supplies
  \(k-1\ge2\) other vertices. All five motif edges and both local
  cross-partner edges have nonzero distance at most \(k\), hence existing
  in-window labels. There is no fixed universal anchor, lone repeated fan,
  or orphan boundary edge in this selected network.
- **Rates and predecessor:** growing reuse and the rate
  \(Q=\Theta(N^{4/3})\) were already present in GS-P3. The new content
  is the exact simultaneous variable-output motif assembly. It does not
  improve the prior coverage exponent. Here
  \(Q/N^2=\Theta(N^{-2/3})\), and every uncovered pair remains charged.
- **Support scope:** \(Z+B\) is a safe support upper bound, not the
  actual image. VG-C3's actual-image conclusion is the precise spacing-one
  specialization of GS-A4; it is not inferred from failure of the selected
  certificate and does not extend to unrelated scalar completions.

This is an independent **internal** proof inspection, not external peer
review, a literature novelty check, or a classification of all nonlinear
sharing networks.

## 6. Budget, artifacts and provenance

The [new evaluator](../../../experiments/variable_gap_sharing.py) saved
three raw files and `experiment-provenance.json` under
`local-only/runs/T01/2026-10-06-variable-gap-sharing/`. The
[portable data](../../../examples/2026-10-06-variable-gap-sharing.json)
give all summaries and raw-file hashes. Existing destination files are
rejected before any evaluation; none was overwritten.

| Released run item | Actual value |
|---|---|
| Interpreter | Python 3.12.7 |
| Prescribed instances | 3: k=3,4,5 |
| P evaluations | 20,450 = 27²+64²+125² |
| Exact compatibility/accounting checks | 9,349 |
| CPU seconds | 0.18652199999999997 |
| Wall seconds | 0.18929575011134148 |
| Errors | None; exit code 0 |
| Network, installations, randomness | None |

The 9,349 checks comprise 7,448 explicit non-base motif-edge memberships,
1,862 exact selected-label evaluations against cached full-square values,
and 39 complete count, range and nondegeneracy predicates. The label count
is \(150+492+1220=1862\). Checking every partner combination was neither
necessary nor performed; the all-partner statement rests on the proof.

Execution-time hashes, identifying the exact reviewed bytes used in the run:

| Artifact | SHA-256 |
|---|---|
| Evaluator | `15e790645230ba8cf279396c5fc870157d45d5f45ced9a699ec38211427a7576` |
| New tests | `c78627afb9659df2b2b29bb48adf227ee51f6fb57a988e43e6498a64c5d17bc2` |
| Canonical input description | `23fa8a4b3e75c8d3fda5e0aaf4f05198df33703b3e2700147547be95f7bb5366` |
| Compatibility proof | `3091c13a2ce8804d715e36792a33d5e76a37c9896fd1afac9c7be008868f8418` |
| Construction proof | `680282847c4bbebdc4ac749d3a9fd8d47858f179d03a430d17c1a6411024d5e7` |
| Portable data | `aaec0b0ac15254e01c14f33622df68fc2bd2537adf07795f4d49e9fa83d39ffb` |

The three [new unit tests](../../../tests/test_variable_gap_sharing.py)
are assigned to the lead's single full-suite execution, and were not run
by this evaluator. They contain five P evaluations on one worked motif,
25 assertion contexts including expected-error guards and accounting
checks, and no second full-square analysis. Charging all these assertions
conservatively gives combined current-family totals of four instance visits,
20,455 P evaluations and 9,374 checks, below the shared ceilings
12 / 50,000 / 10,000. The lead verification record states their actual
execution result and keeps inherited regressions separate. Reading raw JSON
and `git diff --check` added no P evaluations or compatibility experiments.

## 7. Exact claim status

VG-X1 is **EXPERIMENTAL**, exhaustive on all three explicitly listed
scalar squares. VG-G1–VG-G3 and VG-C1–VG-C3 are **PROVED** by their
identified arguments, independently internally audited here. The network
has growing partner counts and exact gluing, but supplies no positive
full-support exponent. The target for arbitrary real finite sets remains
**OPEN**. This audit introduces no alternative carrier, parameter sweep,
new network search or independent next obligation.
