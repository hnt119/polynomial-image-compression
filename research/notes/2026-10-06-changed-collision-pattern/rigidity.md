# Rigidity of the fixed 150-edge variable-gap incidence pattern

T01, 2026-10-06, version 1. Fixed polynomial
\(P(x,y)=(x-y)^3+x+y\). This is a newly commissioned offline proof
audit of VG-O1 from the
[preceding variable-gap report](../2026-10-06-variable-gap-sharing/README.md#exactly-one-next-proof-obligation).
The user supplied the key gap/decrement outline. No separate progress
file was located; the proof below is verified directly from the displayed
VG-O1 equations, not attributed to an unseen report.

No numerical enumeration, symbolic-search program, network access,
package installation, arithmetic tower, or alternative construction was
used. This note preserves the preceding report as historical state and
adds a dated resolution of its one finite rigidity question. It does not
resolve the unrestricted T01 target.

## CP-R1 — the increasing real realization is uniquely the unit interval

### Meaning

Keeping all the old output coincidences also keeps a small, rigid pattern
inside them. Nearest-neighbor coincidences force alternating gap errors.
The distance-two coincidences then force three strictly decreasing positive
gaps into a set of at most two possible values. Thus the scalar positions
cannot deform away from their original unit spacing.

### Exact statement — PROVED

Suppose
\[
x_0<x_1<\cdots<x_{26},\qquad x_0=0,
\]
and real numbers \(w_j\), \(-12\le j\le38\), satisfy
\[
P(x_i,x_\ell)=w_{((i-\ell)^3+i+\ell)/2}
\quad\text{whenever }0\le i,\ell\le26,
\quad1\le|i-\ell|\le3.                         \tag{R1}
\]
Then necessarily
\[
\boxed{x_i=i\quad(0\le i\le26),\qquad
w_j=2j\quad(-12\le j\le38).}                   \tag{R2}
\]
Conversely these values satisfy (R1). Pairwise distinctness of the
\(w_j\) is not needed as a hypothesis: it follows from the conclusion.
Without the normalization \(x_0=0\), the same proof gives
\(x_i=x_0+i\) and \(w_j=2x_0+2j\).

Consequently VG-O1's proposed nonarithmetic increasing realization does
not exist. Its alternative requested rigidity conclusion is established.

### Proof, step 1: identify the actual repeated output classes

Write
\[
d_i=x_{i+1}-x_i>0,\qquad e_i=d_i^3-d_i,
\quad0\le i\le25.
\]
For an adjacent forward edge, the prescribed index is
\[
\frac{(-1)^3+i+(i+1)}2=i,
\]
whereas the reverse edge has index \(i+1\). Hence (R1) gives
\[
w_i=P(x_i,x_{i+1})=2x_i-e_i,
\qquad
w_{i+1}=P(x_{i+1},x_i)=2x_{i+1}+e_i.          \tag{R3}
\]
For every \(1\le i\le25\), compare the two actual representatives
\((x_i,x_{i+1})\) and \((x_i,x_{i-1})\) of the class \(w_i\).
It follows that
\[
-e_i=e_{i-1},\qquad
\boxed{e_i=(-1)^i e_0\quad(0\le i\le25).}     \tag{R4}
\]
This uses coincidences in (R1), not a relation imposed on the moving
values \(w_j\).

The reverse distance-two edge has index
\[
\frac{2^3+(i+2)+i}2=i+5.
\]
For \(0\le i\le21\), the reverse-adjacent edge
\((x_{i+5},x_{i+4})\) exists and has the same index. Thus
\[
\boxed{P(x_{i+2},x_i)=P(x_{i+5},x_{i+4})=w_{i+5}}
\quad(0\le i\le21).                         \tag{R5}
\]
All index ranges in (R3)–(R5) are within the stipulated vertices and
output classes.

### Proof, step 2: classify positive gap choices when the error is nonzero

If \(e_0=0\), positivity and \(d_i^3-d_i=0\) force \(d_i=1\)
for every \(i\), proving the scalar conclusion immediately. Assume
instead \(e_0\ne0\), and put \(C=|e_0|>0\).

For positive real \(t\), the condition \(t^3-t=C\) forces \(t>1\).
The function is strictly increasing there, so it has one possible value
\(p>1\). On the other parity, \(q^3-q=-C\) forces \(0<q<1\).
Combining its equation with that of \(p\) gives
\[
0=p^3+q^3-p-q
=(p+q)(p^2-pq+q^2-1).
\]
Since \(p+q>0\), every small gap therefore satisfies the same quadratic
\[
\boxed{q^2-pq+p^2-1=0.}                     \tag{R6}
\]
There are at most two such real values, with a repeated root allowed.
When written explicitly they are
\(q=(p\pm\sqrt{4-3p^2})/2\); the proof only needs the at-most-two
count, so no discriminant or repeated-root exception is lost.

Choose \(j=0\) if \(e_0>0\), and \(j=1\) if \(e_0<0\).
By (R4), the relevant consecutive gaps have the form
\[
(d_j,d_{j+1},\ldots,d_{j+6})
=(p,q_0,p,q_1,p,q_2,p),                     \tag{R7}
\]
where every \(q_r\in(0,1)\) obeys (R6). This uses only indices
through \(d_7\).

### Proof, step 3: the precise distance-two decrement

Apply (R5) first at \(i=j\), then at \(i=j+2\). For either
application, write \(q=d_{i+1}\) and \(q'=d_{i+3}\), so that
\[
x_{i+2}-x_i=p+q,\qquad
x_{i+5}-x_i=3p+q+q'.
\]
The right side of (R5) can be evaluated using its reverse-adjacent
representative, since \(d_{i+4}=p\):
\[
P(x_{i+5},x_{i+4})=2x_{i+5}+C.
\]
This avoids introducing a nonexistent extra forward edge at a boundary.
The left side equals \((p+q)^3+2x_i+p+q\). Subtract \(2x_i\) and
use \(C=p^3-p\) to obtain the exact equation
\[
2q'=(p+q)^3-p^3-4p-q.                       \tag{R8}
\]
Using \(p^3+q^3=p+q\) and (R6), (R8) simplifies to
\[
q'=3p^2q-2p^3,
\]
and hence
\[
\boxed{q'-q=-(p-q)(2p^2-q^2)<0.}           \tag{R9}
\]
For the factorization, expanding its right side gives
\(-2p^3+2p^2q+pq^2-q^3\); multiplying (R6) by \(q\) gives
\(pq^2-q^3=p^2q-q\), yielding the displayed difference.
The strict sign follows from \(p>1>q>0\), so both factors are positive.

The two applications give \(q_0>q_1>q_2\), three distinct roots of
the same quadratic (R6). This contradiction proves \(e_0=0\).
Equation (R4) now forces every gap to be 1, so \(x_i=i\).

For clarity, the largest index used in this contradiction is
\(x_{j+7}\), at most \(x_8\), and the largest output index is
\(j+7\), at most 8. The four available choices (R5) at
\(i=0,1,2,3\) suffice to handle both signs of \(e_0\); for each
sign only two of them are used. There is no appeal to an infinite
sequence or an equation beyond the finite boundary.

### Proof, step 4: recover every output label and the converse

With \(x_i=i\), every selected pair has value
\[
P(i,\ell)=(i-\ell)^3+i+\ell=2j
\]
at its declared class \(j\). Every class in (R1) is represented:
forward distance-three edges \((i,i+3)\), \(0\le i\le23\), have
classes \(i-12\), covering \(-12\) through 11; reverse distance-three
edges \((i+3,i)\) have classes \(i+15\), covering 15 through 38.
Adjacent edges cover classes 0 through 26 and fill the remaining gap.
Thus \(w_j=2j\) for all 51 labels. Direct substitution proves the
converse. The identity
\(P(x+t,y+t)=P(x,y)+2t\) gives the unnormalized version.
\(\square\)

### Why it matters

The obstruction is caused by particular inherited collision equalities,
not by treating all output values as fixed numbers. They remain rigid
even while the \(w_j\) move freely and before requiring those values to
be distinct. To alter this finite completion, a proposed new pattern must
change some of these forcing coincidences; merely relabeling their common
outputs cannot supply a nonarithmetic seed.

A compact forcing certificate consists of the 25 nearest-neighbor
coincidences in (R4), together with (R5) at \(i=0,1,2,3\).
The first seven nearest-neighbor coincidences and those four distance-two
equalities already force unit spacing on the first nine vertices; the
remaining nearest-neighbor equalities propagate it through all 27.
No distance-three equation is needed to force the scalar positions.

### Scope

Strictly increasing real vertices are essential to the positive-gap
argument. This does not classify unordered real or complex realizations,
other collision partitions, arbitrary sharing graphs, or independently
changed cross-block patterns. It is neither an actual-image lower bound
for arbitrary finite real sets nor a proof that all nonlinear coordinate
deformations fail.

## Provenance, audit status and disposition

| Item | Record |
|---|---|
| Claim | CP-R1 |
| Track and fixed polynomial | T01; \((x-y)^3+x+y\) |
| Quantifiers | Every increasing real realization of all 150 declared edges on vertices 0 through 26, with the 51 original moving output classes |
| Hypotheses | Equations (R1), strict real order, normalization \(x_0=0\); output distinctness not needed |
| Proof source | Full argument above; exact original system in the preceding README's VG-O1 |
| Input from current user | Alternating-gap and distance-two-decrement outline; checked here directly |
| Version/date | 1 / 2026-10-06 |
| Evidence | Complete symbolic hand proof; zero research evaluations or program checks |
| Internal audit | Referee independently checked indices, signs, quadratic roots, decrement and finite boundaries; the lead independently inspected the complete saved proof and confirmed all steps, including recovery of all 51 outputs |
| Missing source boundary | No separate supplied progress report was located; none is claimed read or audited |
| Disposition | VG-O1 is resolved by rigidity; its proposed nonarithmetic witness is excluded in its stated scope |
| Retained gap | The unrestricted T01 power-saving target and a useful changed collision pattern remain open |

Earlier files and statuses are preserved as historical records. The lead
will reconcile this dated resolution and select any subsequent obligation;
this companion introduces none independently. No external theorem,
literature search, novelty claim or external review is used.
