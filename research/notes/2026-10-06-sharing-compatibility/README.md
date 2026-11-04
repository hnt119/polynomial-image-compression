# Compatibility of three cubic sharing curves

T01 · 6 October 2026 · P(x,y)=(x-y)³+x+y · offline.

## Verdict

**PROVED — a sharp obstruction for one closed network family.** Three
mixed-coordinate sharing curves can close and reuse endpoints, but the
directed triangles with ordered outputs
\[
(z,z+2r,z+4r),\qquad r=1/\sqrt3,
\]
have only one real shape: (t−r,t,t+r). For every nonempty finite assembly of these
triangles, its actual scalar union A and prescribed pair set E satisfy
\[
\boxed{N=|A|,\quad Q=|E|\le2N-3,\quad Z=|P(E)|=N,\quad
B=N^2-Q,\quad |P(A,A)|\le Z+B.}
\]
The bound on Q is attained. Even optimal endpoint reuse in this family
leaves N²−O(N) pairs uncovered. The selected-output gate holds with
ε=1, but the coverage gate fails for every fixed δ>0. This resolves the prescribed-pair mechanism
negatively in the chosen scope; **the unrestricted T01 target remains OPEN**.

The accepted [elliptic report](../2026-09-30-elliptic-geometry/README.md)
supplies the coordinate templates and genus-one edge description.
The simultaneous compatibility and counting proofs below are new internal
proofs, independently checked in this cycle. Global elliptic factorization
is imported as a frozen scoped result and is not reopened.

## Small worked example

Take the two triangles
\[
(0,r,2r),\qquad(r,2r,3r).
\]
Their ordered outputs, in units r/3, are (2,8,14) and (8,14,20).
The repeated pair (r,2r) is counted once, giving
\[
N=4,\quad Q=5,\quad Z=4,\quad B=11,\quad Z+B=15.
\]
The complete square has the following exact table of 3P(x,y)/r.

| x/r ∖ y/r | 0 | 1 | 2 | 3 |
|---:|---:|---:|---:|---:|
| 0 | 0 | 2 | −2 | −18 |
| 1 | 4 | 6 | 8 | 4 |
| 2 | 14 | 10 | 12 | 14 |
| 3 | 36 | 20 | 16 | 18 |

**EXPERIMENTAL — exact exhaustive count:** the full image has 14 values.
One double fiber, value 14 in the table, is prescribed; the other, value 4,
is incidental. This illustrates why prescribed coverage and actual fibers
must be counted separately. Longer strips have no common scalar anchor
once they contain at least four triangles.

## Compatibility lemma

**PROVED — SH-G1.** Put u=a−b, v=b−c, w=c−a. The identifications are
\[
c_-(z,u)=c_+(z+h,v),\quad
c_-(z+h,v)=c_+(z+2h,w),\quad
c_-(z+2h,w)=c_+(z,u).
\]
Their simultaneous necessary and sufficient equations are
\[
\boxed{v^3-u^3-u-v=h,\qquad
2u+v-3v(u^2+uv+v^2)=0,}
\]
with w=−u−v and
\[
b=(z-u^3-u)/2,\quad a=b+u,\quad c=b-v.
\]
To prove this, substitute the reconstruction into the second and third
outputs; subtracting twice the second output gap from the third gives the
second boxed equation. Reversing the substitution proves sufficiency.
There is no division by a difference, hence no discarded branch.

**PROVED — SH-G2/G3.** An ordered real output triple determines at most one
directed triangle. Indeed, compare two solutions, let α_i be their vertex
differences and
\[
k_i=u_i^2+u_i u_i'+(u_i')^2\ge0.
\]
Equality of their edge outputs gives
\[
(1+k_i)\alpha_i+(1-k_i)\alpha_{i+1}=0
\]
cyclically. This linear system has determinant
\[
2(1+k_1k_2+k_2k_3+k_3k_1)>0,
\]
so every α_i vanishes. For h=2r, the seed (−r,0,r) and
P(x+t,y+t)=P(x,y)+2t therefore give **all** real solutions:
\[
(a,b,c)=(t-r,t,t+r),\qquad z=2t-4r/3.
\]
The reduced intersection is nonsingular: its Jacobian determinant is
1+9(u²+uv+v²)², equal to 10 at (−r,−r).
The separate elliptic edge curves do not leave an elliptic parameter
after closure. This says nothing about other network shapes or output-gap
patterns. [Full compatibility proof](geometry.md).

## Sharp construction and obstruction

**PROVED — SH-C1/C2.** For any nonempty finite translation set T,
\[
A=T+\{-r,0,r\},\qquad |T|\le N\le3|T|.
\]
The prescribed outputs are exactly
\[
P(E)=2T+\{-4r/3,2r/3,8r/3\}=2A+2r/3,
\]
so Z=N. Every prescribed pair has difference −r or 2r. Forget its
orientation, which is recoverable from its distance. Each scalar has at
most two larger neighbors at distances r,2r; the largest has none and
the second largest at most one. Hence Q≤2N−3. In fact every selected
output has at most two prescribed pairs.

The consecutive choice T={r,2r,…,mr} attains the bound:
\[
\boxed{A=\{0,r,\ldots,(m+1)r\},\quad
N=m+2,\quad Q=2m+1,\quad Z=N,\quad
B=N^2-2N+3.}
\]
Its 3m raw edge occurrences reduce to 2m+1 distinct (z,u) labels and
actual ordered pairs. The common-edge overlaps are genuine endpoint reuse,
but only a constant amount per scalar.

Thus the safe certificate Z+B=N²−Q+N is always at least N²−N+3
within this family. This is a lower bound on that certificate, not an
actual-image lower bound for arbitrary T.
[Counting proof and exact support formula](construction.md).

## Full-square limitations and exact checks

**PROVED — SH-C3, importing and checking GS-A4.** The strip is a fixed-spacing
progression, so the accepted
[progression theorem](../2026-09-21-growing-step-cubic/progression-laboratory.md)
applies. With
\[
D=\min\{N-1,\lfloor\sqrt{6(N-1)}\rfloor\},
\]
every nonsingleton actual pair has index difference at most D, and
\[
\max\{N,(N-D)(N-D-1)\}\le |P(A,A)|\le N^2-N+3.
\]
The proof uses the exact equality
P(ri,rj)/r=(i−j)³/3+i+j: a collision of distinct pairs forces
|d³−e³|≤6(N−1), while distinct integer cubes are separated by at least d².
Pairs outside the band are singleton fibers. Consequently
\[
|P(A,A)|=N^2-O(N^{3/2}).
\]
This is an actual-image obstruction for the strip. It also leaves
N²−O(N^{3/2}) pair mass in singleton fibers, precluding the requested
fiber-tail bound there. The argument does not extend here to arbitrary T.

**EXPERIMENTAL — SH-X1.** After recording the compatibility proof, eight
predeclared strips were enumerated exactly over their complete scalar squares.

| m | N | Q | Z | B | Z+B | Actual image |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 6 | 9 | 9 |
| 2 | 4 | 5 | 4 | 11 | 15 | 14 |
| 3 | 5 | 7 | 5 | 18 | 23 | 21 |
| 4 | 6 | 9 | 6 | 27 | 33 | 30 |
| 8 | 10 | 17 | 10 | 83 | 93 | 78 |
| 16 | 18 | 33 | 18 | 291 | 309 | 260 |
| 32 | 34 | 65 | 34 | 1091 | 1125 | 974 |
| 64 | 66 | 129 | 66 | 4227 | 4293 | 3830 |

The run used 6,022 P evaluations and 3,140 exact checks. Scalars were
represented as rational coefficients of the fixed positive r, so equality
was exact. These data verify the finite counts; the preceding proof,
not extrapolation, establishes the strip's asymptotic failure.
[Exact audit](exact-audit.md), [data](../../../examples/2026-10-06-sharing-compatibility.json),
and [complete cost ledger](construction-ledger.md).

## One next proof obligation

**OPEN — SH-O1.** For the same fixed r and arbitrary nonempty finite T⊂R,
decide whether there is an absolute κ>0 such that
\[
A_T=T+\{-r,0,r\}
\quad\Longrightarrow\quad
|P(A_T,A_T)|\ge\kappa |A_T|^2.
\]
This concerns the unprescribed pairs in the same family. The sharp linear
coverage obstruction does not prove it, and the progression theorem covers
only the consecutive strip. A refutation would mean vanishing image density;
it would not by itself establish a fixed power saving. No truth claim,
equivalence with T01, or new constructive reduction is asserted.

[Proof provenance and repository verification](verification.md).
