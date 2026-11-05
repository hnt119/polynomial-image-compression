# One arithmetic-output triangle and its forced extension

T01, 11 October 2026, version 1. Fixed polynomial
\(P(x,y)=(x-y)^3+x+y\). This is authorized offline symbolic research
on one output-first CP-frame junction. No numerical program, parameter
enumeration, torsion calculation, package installation, or target-P
evaluation was used to derive this appendix. The separately authorized
finite diagnostic is restricted to this family at m=2,3,4.

**PROVED — VO-C1–VO-C5.** The chosen three-output junction has an exact
nonarithmetic real realization. The outer frame adds two genuine
cross-block pairs using existing scalars. Its prescribed repeated
extension has N=4m and Q=6m-2, and its actual full image is at least
N^2/16. Changing to unequal gaps cannot preserve the chosen row-sharing
rule. These are scoped statements about this one candidate; T01 remains
OPEN.

## VO-C1. Outputs and endpoint compatibility before scalars

For h in (0,1/sqrt(3)) write
\[
 C(h)=8h(1-2h^2),\qquad s(h)=\sqrt{1-3h^2}>0.
\]
The imported TC-G2 frame identity is
\[
 P(q+h,q\pm s(h))=2q+C(h)/2,
 \qquad P(q-h,q\pm s(h))=2q-C(h)/2.                       \tag{1}
\]
The four scalar slots are distinct when h differs from s(h), equivalently
h differs from1/2. This identity and its exact scope were read in
[TC-G2](../2026-10-11-torsion-compatible-sharing/geometry.md), together
with the frozen report. It is not a claim about every collision pattern.

Prescribe the three distinct output labels -Delta,0,Delta, with Delta>0,
before choosing any scalar. Write delta=Delta/4. The short edges
(-Delta,0) and (0,Delta) have centers -delta and delta and widths
h and k satisfying C(h)=C(k)=Delta. The outer edge (-Delta,Delta)
has center0 and a width H satisfying C(H)=2Delta. Its column halfwidth
is S=s(H). All positive admissible roots are initially allowed.

The frozen gluing role is equality of the extreme-output first coordinates:
\[
 H=\delta+k,\qquad -H=-\delta-h.                         \tag{2}
\]
Thus the outer positive row is the right short frame's positive row,
and its negative row is the left short frame's negative row. These
are actual scalar equalities, not labels assigned after selecting a set.
No other endpoint-role pattern is searched.

### All short-width branches and the disjoint short blocks

On the admissible interval C has its maximum
\(16/(3\sqrt6)\), at h=1/sqrt(6), and its limit at1/sqrt(3)
is \(8/(3\sqrt3)\). The outer frame requires
\[
 0<\Delta\le8/(3\sqrt6)<8/(3\sqrt3).
\]
Hence C(x)=Delta has exactly one admissible positive root: its decreasing
branch has larger values than Delta. Consequently k=h. Moreover
C(1/6)=34/27>8/(3sqrt(6)), so
\[
 0<h<1/6,\qquad 0<t=h^2<1/36.                            \tag{3}
\]
The two short scalar blocks are
\[
 F_-=-\delta+\{\pm h,\pm s\},\qquad
 F_+=\delta+\{\pm h,\pm s\},\quad s=s(h).
\]
They are disjoint. Indeed
\[
 2h<2\delta=4h(1-2t)<4h<s-h,
\]
where s>5h follows from t<1/36<1/28. Every positive difference between
two elements of {+/-h,+/-s} is either 2h or at least s-h. Thus none
equals2delta. The outer frame must bridge these two disjoint blocks;
the output-label triangle alone has not yet supplied scalar reuse.

## VO-C2. The unique root for the chosen junction

**PROVED.** Equations (2) force
\[
 H=\delta+h=h(3-4t),\qquad \delta=2h(1-2t).
\]
The remaining output-gap compatibility is exactly
\[
 C(H)-2C(h)=8h(2t-1)g(t)=0,
 \qquad g(t)=64t^3-112t^2+52t-1.                         \tag{4}
\]
On the admissible interval (3), there is exactly one root, and
\[
 1/50<t<1/49.                                           \tag{5}
\]
To see this without root search, g is strictly increasing on [0,1/36]:
its derivative 192t^2-224t+52 is positive there. Its endpoint signs are
\[
 g(1/50)=-67/15625<0,\qquad g(1/49)=1779/117649>0.
\]
The factor2t-1 in (4) is inadmissible. Thus (5) identifies the unique
parameter for this row-sharing role.

At this root the additional endpoint identities follow exactly:
\[
 s=h(7-8t)=2\delta+3h,
 \qquad S=h(5-4t)=s-\delta=\delta+3h.                    \tag{6}
\]
For example s^2-h^2(7-8t)^2=-g(t), and both sides of the asserted
square-root identity are positive. Also
\[
 3h^2(3-4t)^2+h^2(5-4t)^2=1
\]
is exactly g(t)=0. This proves (6) with the required positive root.
Both short and long frames have four distinct scalars: s>h and S>H>0.

### The other positive long-width branch is retained explicitly

The cubic C(x)=2Delta factors as
\[
 (x-H)(x^2+Hx+H^2-1/2)=0.                               \tag{7}
\]
Here H>1/sqrt(6): the increasing function t(3-4t)^2 at t>1/50
exceeds its value5329/31250>1/6 at1/50. Also S>H and
3H^2+S^2=1 imply H<1/2. Consequently the other positive root is
\[
 H_{\rm low}=\frac{-H+\sqrt{2-3H^2}}2,
\]
on the increasing branch of C; it is also an admissible width.
The remaining root is negative. The positive root H_low is not discarded
as complex or degenerate: it fails the frozen endpoint equation H=delta+h.
This accounts for every positive branch relevant to the chosen rule,
without conducting a sweep over different slot assignments.

### The finite junction ledger, with duplicate pairs removed

Define four positive magnitudes
\[
 p=h(1-4t),\quad r=h(3-4t)=H,\quad
 u=h(5-4t)=S,\quad v=h(9-12t).
\]
They satisfy 0<p<r<u<v. In these names the old short scalar blocks and
the new outer scalar slots are
\[
 F_+=\{p,r,-u,v\},\quad F_-=\{-p,-r,u,-v\},
 \qquad F_0=\{\pm r,\pm u\}.                            \tag{8}
\]
In particular the outer frame adds no scalar at all. The actual same
scalar carrier is
\[
 A=\{\pm p,\pm r,\pm u,\pm v\},\qquad N=8.
\]
It is not an arithmetic progression: consecutive gaps r-p and u-r
are2h, while the central gap is2p=2h(1-4t), strictly smaller.

The complete selected-pair union is as follows:

| Output | Distinct controlled ordered pairs |
|---|---|
| Delta | (r,-u), (r,v), (r,u) |
| 0 | (p,-u), (p,v), (-p,u), (-p,-v) |
| -Delta | (-r,u), (-r,-v), (-r,-u) |

The outer frame repeats (r,-u) and (-r,u). Its genuinely new pairs
are (r,u) and (-r,-u), crossing between the two disjoint blocks in (8).
Therefore
\[
 N=8,\quad Q=10,\quad Z=3,\quad B=N^2-Q=54,
 \qquad |P(A,A)|\le Z+B=57,                              \tag{9}
\]
\[
 2Q/N=5/2,\qquad Q/Z=10/3,\qquad Q/N^2=5/32.
\]
The prescribed fiber sizes are3,4,3. They are not asserted to be the
actual complete fiber sizes; the 54 uncovered ordered pairs remain
charged. Counting twelve formal frame cells as twelve distinct pairs
would be incorrect.

## VO-C3. Exact extension and the quantitative stop

Choose the parameter (5) once, before m grows. Prescribe
\[
 z_j=j\Delta,\qquad 0\le j\le m,\qquad m\ge2.
\]
For every short edge (j,j+1), take the frame
\[
 q_j=(2j+1)\delta,\quad h,s,\qquad 0\le j<m.
\]
For every long edge (j,j+2), take the frame
\[
 Q_j=2(j+1)\delta,\quad H,S,\qquad 0\le j<m-1.            \tag{10}
\]
Every consecutive output triangle has exactly the already proved role
(2). The m=2 case is the symmetric presentation (8) translated by
2delta in scalar space; its output labels become0,Delta,2Delta.
This is the prescribed extension of the same candidate, not an additional
construction selected after a failed test.

### Actual input count and gluing

Set rho=delta/h=2-4t. It is irrational. Indeed w=4t satisfies
\[
 w^3-7w^2+13w-1=0.                                     \tag{11}
\]
This monic cubic has no rational root: its only possible integer roots
are+1 and-1, and neither is a root. Thus t has degree three over Q.
No modular irreducibility test is used.

Dividing the four scalar slots of short block j by h gives
\[
 (2j+1)\rho+1,\quad (2j+1)\rho-1,
 \quad (2j+3)\rho+3,\quad (2j-1)\rho-3.                 \tag{12}
\]
Their constant terms are respectively1,-1,3,-3. Equality between
two such expressions forces both integer coefficients of1,rho to agree.
Hence all m short blocks are mutually disjoint, giving exactly4m
actual input scalars.

For the long frame j, its upper row is the upper row of short block
j+1, and its lower row is the lower row of short block j. Its upper
column is the upper column of short block j, and its lower column is
the lower column of short block j+1. This follows directly from
H=delta+h and S=delta+3h. Thus all four long-frame scalars are already
present. Two of its four pairs are already controlled inside their
short blocks; the other two cross those neighboring blocks. The new
pairs for different j are distinct because the short blocks are disjoint.

Consequently the actual scalar set A_m and selected set E_m satisfy
\[
 N=|A_m|=4m,\qquad Q=|E_m|=4m+2(m-1)=6m-2,
 \qquad Z=|P(E_m)|=m+1.                                 \tag{13}
\]
Every prescribed output appears in a short frame. No pair is credited
twice, and no additional scalar is hidden in the long edges. There are
4m local controlled pairs and2(m-1) new cross-block pairs under the
partition into short blocks.

The complete-square ledger is
\[
 B=16m^2-6m+2,\qquad
 |P(A_m,A_m)|\le Z+B=16m^2-5m+3,                         \tag{14}
\]
\[
 2Q/N=3-1/m,\quad Q/Z=6-8/(m+1),\quad
 Q/N^2=(6m-2)/(16m^2).
\]
The selected fibers have size at most6: for m=2 their sizes are3,4,3;
for m>=3 the two endpoint sizes are3, the next two are5, and any
remaining interior sizes are6. This bound concerns only E_m, not all
of A_m squared. The selected mass is linear in N and its coverage
tends to zero. It does not improve the earlier prescribed-pair benchmark.

### VO-C4. Actual full-image lower bound, not merely a failed upper certificate

The m upper short-frame rows form the arithmetic progression
\[
 B_m=\{\delta+h+2j\delta:0\le j<m\}\subset A_m.
\]
Its fixed step2delta has squared value
\[
 (2\delta)^2=16t(1-2t)^2=48t^2-36t+1.                    \tag{15}
\]
The second equality uses g(t)=0. This number is irrational; otherwise
t would satisfy a nonzero quadratic over Q, contradicting (11).

The irrational-squared-spacing clause of
[GS-A4, §4](../2026-09-21-growing-step-cubic/progression-laboratory.md)
therefore applies to this actual sub-square. Its proof was read for
this import: on an AP a+di the output, after subtracting2a and dividing
by d, is d^2(i-j)^3+i+j. Irrational d^2 forces two equal outputs to have
both equal differences and equal sums, hence identical ordered pairs.
Thus it gives exactly m^2 different outputs on B_m squared. Therefore
\[
 |P(A_m,A_m)|\ge m^2=N^2/16.                            \tag{16}
\]
This is an actual obstruction to a fixed positive exponent saving for
this extension. It does not treat all bounded unions as one AP, and
it makes no assertion about unrelated varying-output networks.

### Charged construction costs and stopping rule

The output labels, the single isolated root t, its positive square root
h, and every branch/endpoint role are fixed before m grows. The coefficient
field Q(t) has degree three; all actual scalars lie in the fixed real
field Q(t,h), of degree at most six. Its field degree, discriminant and
denominators do not grow with m. No favorable bound on those quantities,
no regulator, local splitting, or field tower is used for an image saving.
There is no thinning, random selection, or exceptional input removal:
(12) is an exact injective input count. The two duplicate pairs per long
frame are subtracted explicitly in (13), with no uncharged multiplicity.
All unprescribed ordered pairs, including diagonals and reversals, are
charged in (14). Their support is not inferred from collision energy.

The parameter height of the displayed scalars grows with the integer
index j, but no bounded-height conclusion is used. Branch counts are
fully recorded above. The independent AP lower bound (16) already
stops the architecture; finite diagnostics at m=2,3,4 cannot change it
and authorize no additional instances or role changes.

## VO-C5. Unequal gaps cannot repair this same row-sharing rule

**PROVED, specified roles only.** Consider increasing labels
0,alpha,alpha+beta with positive alpha,beta. Let short widths h,k>0
and outer width H>0 have the same frame meanings, so
\[
 \alpha=C(h),\quad\beta=C(k),\quad C(H)=\alpha+\beta.
\]
Keeping the outer lower row equal to the left short lower row, and the
outer upper row equal to the right short upper row, imposes
\[
 H=h+\beta/4=k+\alpha/4.                                \tag{17}
\]
Subtracting gives
\[
 (h-k)\{1-4(h^2+hk+k^2)\}=0.                            \tag{18}
\]
If h differs from k, put p=h+k and r=hk. Then
\[
 r=p^2-1/4,\qquad x^3=x/4-pr\quad(x=h,k),
\]
so C(h)=4h+16pr and C(k)=4k+16pr. Equation (17) becomes
\[
 H=p+4pr=4p^3.
\]
The output-gap equation reads C(H)=8H-4p; comparing with
C(H)=8H-16H^3 gives4H^3=p. Thus256p^8=1. Positivity gives
p=1/2 and hence r=0, contradicting h,k>0.

Therefore h=k and alpha=beta. The surviving parameter is exactly the
arithmetic-label case already classified in VO-C2. This does not exclude
unequal-gap junctions with different slot assignments; none is proposed
or tested here. No alternative label spacing is adopted.

## Evidence and unresolved scope

VO-C1–VO-C5 are complete symbolic arguments in this appendix. The lead
and referee independently checked the identities and counts before any
finite diagnostic was released; their saved verification is a separate
record. The local TC frame identity and the GS-A4 AP clause are identified
imports whose hypotheses were checked above. Historical elliptic torsion,
rank and completion-cover results are not reused as substitutes for these
endpoint equations.

The finite seed succeeds at an actual three-output endpoint junction.
Its same-role unbounded extension is explicitly quantified and has a
quadratic actual image lower bound. The unrestricted same-set T01 target
remains OPEN. No further candidate, spacing change or research expansion
is authorized by this appendix.
