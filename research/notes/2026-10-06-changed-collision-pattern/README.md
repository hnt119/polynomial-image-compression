# Changing the collision pattern: a six-scalar bridge and its limit

T01 · 6 October 2026 · version 1 · offline, internally audited research.
Throughout, \(P(x,y)=(x-y)^3+x+y\), on one actual real scalar set.

## Verdict

**PROVED:** VG-O1 is rigid in its stated increasing-real scope: its
equalities force \(x_i=i\). We verified the supplied gap argument directly;
no separate progress-report file was located or claimed read.

**PROVED finite compatibility:** a changed coincidence pattern gives six
nonarithmetic real scalars and eight controlled cross-block pairs using
three outputs, including a four-pair fiber joining two different centers.
This preserves neither the VG equality partition nor its arithmetic gaps.

**PROVED scoped failure:** its fixed-width extension has
\[
N=2m+2,\quad Q=4m,\quad Z=m+1,
\]
and selected fibers of size at most four. Moreover
\(|P(A_m,A_m)|\ge N^2/4\), because half its scalars form a progression
with injective full square. We stopped the extension at that obstruction.
This is a finite bridge and an unsuccessful extension, **not** an improvement
over the earlier \(N^{4/3}\) rate. The unrestricted T01 target is **OPEN**.

## Which old equalities force spacing

**PROVED — CP-R1. Meaning:** moving the old output values cannot release
the scalar positions. **Statement:** every increasing real realization of
VG-O1, normalized by \(x_0=0\), has \(x_i=i\) and \(w_j=2j\);
output distinctness is unnecessary as an assumption.

**Proof:** with \(d_i=x_{i+1}-x_i>0\), nearest-row coincidences give
\(d_i^3-d_i=(-1)^ie_0\). If \(e_0\ne0\), one parity has a unique
gap \(p>1\); the other has \(0<q<1\) among the at most two roots of
\(q^2-pq+p^2-1=0\). The actual distance-two coincidence
\[
P(x_{i+2},x_i)=P(x_{i+5},x_{i+4})
\]
gives, at the appropriate parity,
\[
q_{\rm next}-q=-(p-q)(2p^2-q^2)<0.
\]
Two applications produce three distinct roots of that quadratic, a
contradiction. Hence every gap is 1. The contradiction fits within
\(x_0,\ldots,x_8\); the remaining nearest-row equations propagate it.
**Scope:** increasing real embeddings of this particular incidence pattern,
not other collision partitions. [Full finite-index proof](rigidity.md).

## Changed compatibility and the worked bridge

**PROVED — CP-C1. Meaning:** replace the forcing chain with two simultaneous
row repetitions across a second scalar block. For blocks
\(\{r\pm h\},\{q\pm s\}\), with \(h,s>0\), prescribe
\[
P(r+h,q+s)=P(r+h,q-s),\qquad
P(r-h,q+s)=P(r-h,q-s).
\]
**Statement:** they hold simultaneously exactly when
\[
r=q,\qquad 3h^2+s^2=1;
\]
their outputs are \(2r\pm4h(1-2h^2)\).
**Proof:** subtraction in either row gives
\(2s[1-3(x-q)^2-s^2]\); subtracting the two row conditions forces
the common center. In the inherited templates the two positive-row
differences are \(h-s,h+s\), satisfying
\(u^2+uv+v^2=1\), so both reconstructed first coordinates are the same.
The negative row is enforced simultaneously. **Scope:** the conic identity
is inherited; this is its prescribed two-row use. Distinct blocks require
\(h\ne s\).

Now fix the unique root
\[
64t^3-80t^2+28t-1=0,\qquad 0<t<1/12,
\]
and put
\[
h=\sqrt t,\qquad r=h(4t-2)<0,\qquad s=h(5-8t)=h-2r.
\]
The polynomial is strictly increasing on that interval and changes sign
there. Its equation gives \(s^2=1-3t\), so the two frames centered at
\(-r\) and \(r\) both satisfy the compatibility equations. Their scalar
unions share two endpoints. Write
\[
a=h(1-4t),\quad b=h(3-4t),\quad d=h(7-12t),
\qquad A_2=\{-d,-b,-a,a,b,d\}.
\]

| First coordinate | Two second coordinates | Shared output |
|---|---|---:|
| \(a\) | \(-b,d\) | 0 |
| \(-a\) | \(b,-d\) | 0 |
| \(b\) | \(-b,d\) | \(-4r\) |
| \(-b\) | \(b,-d\) | \(4r\) |

**PROVED finite statement — CP-C2:** all six scalars are distinct, the eight pairs
are distinct, and the zero fiber contains four of them with two different
first coordinates. The central gap \(2a\) differs from the next gap
\(b-a=2h\), so the scalar set is nonarithmetic. Thus
\[
N=6,\quad Q=8,\quad Z=3,\quad B=28,\quad |P(A_2,A_2)|\le31.
\]
**Proof:** substitute \(s=h-2r\) and the two center values into the
simultaneous construction above; the cubic equation for \(t\) supplies
the shared endpoints. **Scope:** this is an exact finite seed. Its complete
square, including unprescribed pairs, is audited separately; it supplies
no asymptotic rate by itself.

## Extension, counts and stopping point

**PROVED — CP-C3/C4. Meaning:** reuse the same widths at centers
\(c_j=(2j-1)r\), \(0\le j<m\), and prescribe all four pairs
\(\{c_j\pm h\}\times\{c_j\pm s\}\). **Statement:** their actual
scalar union is
\[
A_m=\{c_i+h:-1\le i\le m-1\}
\ \cup\ \{c_i-h:0\le i\le m\}.
\]
These sets are nested, have \(2m+2\) distinct points, and are nonarithmetic.
Their controlled outputs are exactly \(4r\{-1,0,\ldots,m-1\}\).
The two endpoint outputs have selected fiber size two; the other \(m-1\)
outputs have size four.

**Proof:** \(c_j+s=c_{j-1}+h\) and
\(c_j-s=c_{j+1}-h\) identify actual endpoints between adjacent frames.
Since \(|r|>h\), the two displayed scalar progressions are disjoint.
Each first coordinate occurs in one source frame, giving four distinct
pairs per frame. The row outputs are \(4(j-1)r\) and \(4jr\).
Consecutive scalar gaps include both \(2|r|\) and \(2h\), which differ.
All sharing and output repetitions thus hold simultaneously.

The exact ledger is
\[
\begin{aligned}
N&=2m+2,&Q&=4m,&Z&=m+1,\\
B&=4m^2+4m+4,&Z+B&=4m^2+5m+5.
\end{aligned}
\]
Always \(|P(A_m,A_m)|\le Z+B\), with every omitted pair charged.
The three ratios are
\[
\frac{2Q}{N}=\frac{4m}{m+1},\qquad
\frac QZ=\frac{4m}{m+1},\qquad
\frac Q{N^2}=\frac{m}{(m+1)^2}\to0.
\]
Partition the scalars into the \(m\) source blocks and the two boundary
singletons. All \(4m\) selected pairs cross these blocks; none is a
within-block pair. Of these same pairs, \(4(m-1)\) lie in output fibers
represented at two different frame centers. These are overlapping
descriptions of the counted pairs, not additional coverage.

**Full-square failure, PROVED:** modulo 3 the defining cubic for \(t\)
has no root, hence it is irreducible over \(\mathbb Q\). Consequently
\[
(2r)^2=16t^2-12t+1\notin\mathbb Q.
\]
One displayed scalar progression has \(m+1=N/2\) points and spacing
\(2r\). The irrational-squared-spacing clause of the inherited GS-A4
theorem makes its entire square injective: a collision would equate that
irrational number times a nonzero integer difference of cubes to an integer.
Equal differences and sums instead give the identical pair. Thus
\[
\boxed{|P(A_m,A_m)|\ge(m+1)^2=N^2/4.}
\]
**Scope:** this stops the fixed-width ladder itself, regardless of additional
incidental collisions. It does not exclude other width patterns or general
real sets. Its linear \(Q\) is below the earlier \(N^{4/3}\) benchmark.
[Full proof and cost ledger](construction.md).

## Finite audit

**EXPERIMENTAL — CP-X1:** only the base frame, two-center bridge, and one
attachment are evaluated, after compatibility and source review. The exact
field representation, complete full-square fibers and ledgers are in
[the audit appendix](exact-audit.md) and
[portable data](../../../examples/2026-10-06-changed-collision-pattern.json).

| \(m\) | \(N\) | \(Q\) | \(Z\) | \(B\) | \(Z+B\) | Actual full image |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 2 | 12 | 14 | 14 |
| 2 | 6 | 8 | 3 | 28 | 31 | 29 |
| 3 | 8 | 12 | 4 | 52 | 56 | 52 |

The one run checked all 116 square cells by two exact polynomial evaluators:
232 charged P evaluations and 233 compatibility/accounting checks, with no
errors. Finite values do not establish the asymptotic statements above.

## Exactly one next lemma

**OPEN — CP-O1, one variable-width bridge attachment.** For the exact
six-point \(A_2\) above, decide whether there is a new frame
\[
F=\{q-u,q+u,q-v,q+v\},\qquad u,v>0,\quad
u\ne v,\quad 3u^2+v^2=1,
\]
with \(q\notin\{-r,r\}\), at least two distinct scalars of \(F\)
already in \(A_2\), and a row \(x=q\pm u\notin\{-a,a\}\) satisfying
\[
P(x,q-v)=P(x,q+v)=0.
\]
Give an exact realization or prove it impossible. This asks whether changing
the widths can add a third distinct first coordinate to the existing zero
fiber while substantially reusing endpoints. It is a fixed finite system,
not the original fiber-tail target. No solution, search, or asymptotic
extension is asserted here.

The previous VG and elliptic checkpoints remain unchanged. The supplied
rigidity outline is now a checked proof; the conic identity and GS-A4 are
identified imports with their needed specializations checked. There was no
internet, package installation, arithmetic tower, or literature/novelty claim.
[Proof provenance and repository verification](verification.md).
