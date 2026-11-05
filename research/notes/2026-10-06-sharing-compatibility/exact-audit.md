# Exact strip computation and independent proof audit

T01, 2026-10-06, version 1. The fixed polynomial is
\(P(x,y)=(x-y)^3+x+y\). This appendix records **SH-X1 — EXPERIMENTAL**:
one exact run over the eight predeclared lengths of the sole directed-triangle
strip family. It separately records an independent internal inspection of
the complete proofs SH-G1–SH-G3 and SH-C1–SH-C3. Finite agreement is not
used to prove those theorems. No external review or novelty claim is made.

## 1. Release, exact representation, and complete-square scope

The saved [geometry proof](geometry.md) and the entire new scout/test source
were inspected by the lead before release. The computation was then run
**once**, with the exact command

```text
python3 -m experiments.sharing_compatibility --compatibility-proof research/notes/2026-10-06-sharing-compatibility/geometry.md
```

No computation preceded that release. The prescribed inputs were
\(m=1,2,3,4,8,16,32,64\), with
\[
r=1/\sqrt3,\qquad
((j-1)r,jr,(j+1)r),\quad 1\le j\le m.
\]
The scalar \(ar\) is represented by its exact rational coefficient
\(a\). Since \(r\ne0\), equality of these coefficients is exactly
equality of the real scalars. The exact evaluation rule is
\[
P(ar,br)/r=\frac{(a-b)^3}{3}+a+b,
\]
using only \(r^3=r/3\). This does not vary or replace the fixed
polynomial. Fractions are reduced by Python's standard-library
`fractions.Fraction`; no approximate equality, numerical root search,
package, network access, or random seed is involved.

For differences represented by coefficients \(u,v,w\), the three
checked compatibility relations are
\[
u+v+w=0,\quad
\frac{v^3-u^3}{3}-u-v=2,\quad
2u+v-v(u^2+uv+v^2)=0.
\]
The inverse label map is checked exactly as
\[
(z,u)\longmapsto
\left(\frac{z-u^3/3+u}{2},\frac{z-u^3/3-u}{2}\right).
\]
Each raw triangle contributes three labels. The code separately deduplicates
actual endpoint scalars, ordered pairs, and \((z,u)\) labels, rejecting any
inconsistent repeated label. It then evaluates **every ordered pair** in
the resulting actual \(A^2\), once each. No pair outside the triangle
network is omitted. The raw files contain every full output fiber.

## 2. SH-X1 — results over precisely the prescribed finite range

The general formulas \(N=m+2\), \(Q=2m+1\), \(Z=N\), and
\(B=N^2-Q\) are proved in [SH-C1/SH-C2](construction.md).
Every finite case below passed those exact checks, the compatibility
equations, the inverse labels, the full-square accounting, and the
inherited AP collision-band check. Histograms list
`fiber size : number of distinct outputs`.

| m | N | Q | Z | B | Safe bound Z+B | Entire image | Full fiber histogram |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 3 | 3 | 3 | 6 | 9 | 9 | 1:9 |
| 2 | 4 | 5 | 4 | 11 | 15 | 14 | 1:12, 2:2 |
| 3 | 5 | 7 | 5 | 18 | 23 | 21 | 1:17, 2:4 |
| 4 | 6 | 9 | 6 | 27 | 33 | 30 | 1:24, 2:6 |
| 8 | 10 | 17 | 10 | 83 | 93 | 78 | 1:56, 2:22 |
| 16 | 18 | 33 | 18 | 291 | 309 | 260 | 1:208, 2:40, 3:12 |
| 32 | 34 | 65 | 34 | 1091 | 1125 | 974 | 1:872, 2:22, 3:80 |
| 64 | 66 | 129 | 66 | 4227 | 4293 | 3830 | 1:3608, 2:26, 3:88, 4:108 |

For the strict actual small-fiber tail
\(B_A(t)=\sum_{z:r_A(z)<t}r_A(z)\), selected values are:

| N | B_A(2) | B_A(3) | B_A(4) | B_A(5) | ceil(sqrt N) | B_A(ceil(sqrt N)) |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 9 | 9 | 9 | 9 | 2 | 9 |
| 4 | 12 | 16 | 16 | 16 | 2 | 12 |
| 5 | 17 | 25 | 25 | 25 | 3 | 25 |
| 6 | 24 | 36 | 36 | 36 | 3 | 36 |
| 10 | 56 | 100 | 100 | 100 | 4 | 100 |
| 18 | 208 | 288 | 324 | 324 | 5 | 324 |
| 34 | 872 | 916 | 1156 | 1156 | 6 | 1156 |
| 66 | 3608 | 3660 | 3924 | 4356 | 9 | 4356 |

The artifacts save every integer threshold from 1 through \(N+1\), the
ranked full-fiber sizes, and all exact pairs. For the table's \(N=3,t=5\)
entry, the tail is already saturated at \(N^2=9\), as follows directly
from its singleton histogram. No untested asymptotic tail conclusion is
inferred from the observed maximum fiber sizes.

## 3. Worked m=2 example, with all ordered pairs included

Here \(A=\{0,r,2r,3r\}\). Rows and columns below are the scalar
coefficients \(0,1,2,3\), and an entry is \(3P(ar,br)/r\):
\[
\begin{pmatrix}
0&2&-2&-18\\
4&6&8&4\\
14&10&12&14\\
36&20&16&18
\end{pmatrix}.
\]
This table was derived by hand before execution and is a separate
small regression oracle. The five distinct prescribed pairs and their
outputs, all in coefficient units, are

| Ordered pair | Output coefficient P/r | Difference coefficient |
|---|---:|---:|
| (0,1) | 2/3 | −1 |
| (1,2) | 8/3 | −1 |
| (2,0) | 14/3 | 2 |
| (2,3) | 14/3 | −1 |
| (3,1) | 20/3 | 2 |

The six formal triangle labels repeat the edge \((1,2)\) once. The
distinct label count and ordered-pair count are both five. The full square
has two double fibers:
\[
P(r,0)=P(r,3r)=\frac{4r}{3},\qquad
P(2r,0)=P(2r,3r)=\frac{14r}{3}.
\]
The first double fiber is entirely outside the selected network. Therefore
\(Z+B=15\) is a valid upper certificate, while the actual image is 14.
This explicitly demonstrates why the selected-output calculation cannot
be silently identified with the full-image count.

## 4. Independent internal proof challenges and outcome

The exact-computation auditor read the complete current
[geometry](geometry.md) and [construction](construction.md) companions,
and the inherited [GS-A4 proof, §4](../2026-09-21-growing-step-cubic/progression-laboratory.md).
The following challenges were resolved by the displayed proofs, without
numerical or symbolic-search premises:

- **SH-G1:** all three scalar identifications use consistent signs and the
  same edge variables. Summing them genuinely forces \(u+v+w=0\).
  Substitution proves both directions of the reduced system. No division
  by a difference or gap creates an exceptional case.
- **SH-G2:** the comparison coefficients
  \(k_i=u_i^2+u_i u_i'+(u_i')^2\) are nonnegative for real data.
  The cyclic absolute-value inequalities force equality; strictness when
  any \(k_i>0\), and the odd-cycle sign contradiction when all vanish,
  both hold. Independently expanding the comparison determinant gives
  \(2(1+k_1k_2+k_2k_3+k_3k_1)>0\). Complex uniqueness is not claimed.
- **SH-G3:** translation of the exact base triangle supplies existence
  for every real \(z\); SH-G2 supplies global uniqueness. The Jacobian
  identity \(1+9(u^2+uv+v^2)^2\) and its value 10 at \((-r,-r)\)
  check algebraically. A positive Jacobian alone would not justify global
  injectivity; the proof does not make that inference.
- **SH-C1:** the selected support is exactly \(2A+2r/3\), including
  arbitrary repeated endpoint coincidences, so \(Z=N\). The two allowed
  directed differences uniquely determine orientations after edges are
  made unordered. Charging to the smaller endpoint gives at most
  \(2N-3\) edges. The lower bound on the safe certificate's right side
  is not promoted to an actual-image lower bound for arbitrary translates.
- **SH-C2:** the strip has \(m-1\) repeated raw edges, \(m-1\) selected
  double outputs, and three selected singleton outputs, including the
  boundary case \(m=1\). The sharp coverage count is \(2m+1\).
- **SH-C3:** GS-A4 is applied at the fixed positive spacing
  \(r=1/\sqrt3\). The nearest different integer cube estimate gives
  the stated \(D_N\); every pair outside that band is an actual singleton.
  The exact outside-band count \((N-D_N)(N-D_N-1)\), the entire difference
  slice union, and the rate \(N^2-O(N^{3/2})\) all check. This is scoped
  to the strip, not arbitrary finite translate sets.

**Outcome:** no gap or required correction was found in SH-G1–SH-G3 or
SH-C1–SH-C3. These were complete internal proof inspections; neither
agent agreement nor finite tests replace the displayed arguments.

## 5. Computation budget and immutable run provenance

The new [scout](../../../experiments/sharing_compatibility.py) saves to
`local-only/runs/T01/2026-10-06-sharing-compatibility/` and refuses existing
destination files before any evaluation. The
[portable summary](../../../examples/2026-10-06-sharing-compatibility.json)
contains all eight models and each raw file's SHA-256. The raw provenance
file is `experiment-provenance.json` in that local run directory.

| Item | Actual released-run value |
|---|---|
| Interpreter | Python 3.12.7 |
| Instances | 8 prescribed strips |
| P evaluations | 6,022 = sum of the eight actual N² values |
| Exact compatibility/accounting checks | 3,140 |
| Research CPU seconds | 0.10361800000000002 |
| Wall seconds | 0.10380533407442272 |
| Reported errors | None; exit code 0 |
| Network, packages, randomness | None |

The 3,140 checks include 390 triangle equations, 390 inverse labels,
780 repeated-pair/repeated-label consistency checks, 268 selected-output
checks against cached full-square values, 1,216 nonsingleton difference-band
checks, and 96 count/accounting checks. The latter count includes the
eight singleton lower-bound checks. Polynomial evaluations are cached per
actual pair; label verification does not secretly reevaluate P.

Execution-time hashes:

| Artifact | SHA-256 |
|---|---|
| Scout source | `a710c25c38a840b8ef587cf5e6c444efbe77fe724f85dcf292aab3143f11881b` |
| New test source | `12af5765aa35093015515300d8c79e14ac17891ae765473f3fce6e20cef5036c` |
| Canonical input description | `c372f0adebf3e177bae3ba9ddd014b7dc8a49cf27d3adf23452bf40485f08d93` |
| Released geometry file | `9600020ab00e139d6ae9b5afca49121b51a8387b9da1acdafd8048217da5ca6b` |
| Portable data | `876625afb3bf70f91941f8e882ffebf8351952b199e6ea64acdaf79cbb71cf3f` |

These identify the bytes used at execution, even if proof-audit metadata is
subsequently finalized. The new four-test regression source is prepared;
execution is assigned to the lead's one full-suite run, not duplicated by
this auditor. Its prescribed arithmetic cost is 25 P evaluations and 53
compatibility checks across two already declared small instances. With that
regression, the current-family totals are 10 charged instance visits,
6,047 P evaluations and 3,193 checks, below the shared ceilings
12 / 50,000 / 10,000. The lead verification record records whether that
regression actually passed and separates inherited regression work.

## 6. Claim status and retained boundary

SH-X1 is **EXPERIMENTAL**, exact and exhaustive on every scalar square in
the stated eight-element list of sizes. All pairs outside the selected
network are included. The mathematical strip obstruction is **PROVED** by
SH-C3, independently of this finite range. Arbitrary translated assemblies
receive the selected-coverage obstruction SH-C1, not that strip's general
actual-image conclusion. No other carrier family or parameter inventory was
evaluated. This appendix introduces no next proof obligation. The fixed
T01 target remains **OPEN**.
