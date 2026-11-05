# A changed conic collision pattern: exact bridge and bounded-fiber ladder

2026-10-06, final candidate version. T01, fixed
\(P(x,y)=(x-y)^3+x+y\), using one actual real scalar set in both
coordinates. The one candidate is the two-row conic frame, with the
nonconcentric bridge and fixed-width ladder defined below. It was frozen
before enumeration. The earlier unexecuted reverse-chain draft in this
round was replaced by this stronger realization of the same conic pattern;
no previous report, historical proof, or run was changed.

**PROVED:** the candidate has an exact six-scalar non-AP bridge, whose
controlled outputs have fiber sizes \(4,2,2\). Its nested extension obeys
\[
 N=2m+2,\qquad Q=4m,\qquad Z=m+1\qquad(m\ge1).
\tag{C1}
\]
All selected pairs go between distinct blocks. The two end output fibers
have size two and each of the \(m-1\) interior fibers has size four.
Thus the extension has actual scalar reuse and output merging between
different centers, but only linear pair coverage and bounded selected
fibers. It does not improve the earlier \(N^{4/3}\) rate. More strongly,
one of its two scalar sequences already has \(N^2/4\) distinct outputs,
proving an actual-image obstruction to a fixed power saving for this
ladder. The extension is stopped; incidental collisions cannot remove
that proved sub-square support.

## 1. Sources, changed equalities, and evidence boundary

The predecessor is the
[variable-gap report](../2026-10-06-variable-gap-sharing/README.md), whose
output-first band already attained \(\Theta(N^{4/3})\) selected pairs
but completed to an integer interval. Its construction and compatibility
proofs were read. The current [rigidity companion](rigidity.md) addresses
its old finite deformation question. That equality pattern is not imposed
here: no indexed nearest-neighbor chain or reverse distance-two equality
is preserved.

Two cross-block repeats are imposed simultaneously instead, in (C2).
The local same-first-coordinate conic is inherited from
[NR-C2/NR-C3](../2026-09-21-nonlinear-reuse/rational-reuse-curves.md), whose
inverse-fiber formula and exceptional-conic statement were inspected. The
conic identity is not claimed as new. This round's explicit work is the
simultaneous two-row compatibility, nonconcentric bridge, and exact ladder
accounting. The [construction template](../../templates/CONSTRUCTION_LEDGER.md)
governs its costs. No unavailable historical original or external theorem
is a proof dependency.

The actual-image argument imports the irrational-spacing clause of
[GS-A4](../2026-09-21-growing-step-cubic/progression-laboratory.md), §4,
equations (A17)–(A18), dated 2026-09-21. Its proof was read, and the
fixed ladder's hypotheses and the elementary injectivity argument are
checked explicitly below. It is not an imported lower bound for arbitrary
non-AP sets.

All arguments here are symbolic. No mathematical program, finite enumeration,
network access, package installation, arithmetic tower, or alternate
candidate search was performed by this specialist. The lead and referee
checked the supplied bridge algebra before the final ladder was frozen.
The lead subsequently independently audited the complete saved CP-C1–CP-C4
proofs, including the identities, ordering, counts, actual-image lower
bound, and cost ledger, and found no mathematical correction needed.
The audit and any released finite evidence are recorded separately.
No external review or novelty claim is made.

## 2. CP-C1 — simultaneous two-block compatibility

Take two nondegenerate symmetric blocks
\[
 B=\{r-h,r+h\},\qquad C=\{q-s,q+s\},\qquad h,s>0.
\]
Prescribe before choosing the scalar values
\[
 P(r+h,q+s)=P(r+h,q-s),\qquad
 P(r-h,q+s)=P(r-h,q-s).
\tag{C2}
\]
These are repeats between distinct ordered pairs. They are cross-block
pairs when \(B\ne C\), as in the final construction. The general
statement below includes the equal-block degeneration \(r=q,h=s=1/2\).

**PROVED.** The two equations hold simultaneously if and only if
\[
 \boxed{r=q,\qquad 3h^2+s^2=1.}
\tag{C3}
\]
Their row outputs are
\[
 w_+=2r+H(h),\qquad w_-=2r-H(h),\qquad
 H(h)=4h(1-2h^2).
\tag{C4}
\]
Since \(0<h^2<1/3\), these two outputs are distinct.

**Proof.** For any real \(x\),
\[
 P(x,q+s)-P(x,q-s)=2s\bigl(1-3(x-q)^2-s^2\bigr).
\tag{C5}
\]
The two row equalities require
\(3(r+h-q)^2+s^2=3(r-h-q)^2+s^2=1\).
Subtracting gives \(12h(r-q)=0\), so \(r=q\), then (C3).
Conversely (C3) makes both differences (C5) vanish. Expanding either
common value gives
\[
 P(r+h,r\pm s)=2r+h^3+3hs^2+h=2r+4h-8h^3;
\]
replacing \(h\) by \(-h\) proves (C4). \(\square\)

In inverse-fiber language, the positive row uses differences
\(u=h-s\), \(v=h+s\), with
\(u^2+uv+v^2=3h^2+s^2=1\). Thus
\(c_+(w_+,u)=c_+(w_+,v)=r+h\), while the corresponding second
coordinates are \(r+s,r-s\). The negative row enforces the other
shared first coordinate at the same time. Endpoints are not chosen
independently and then assigned separate output labels.

## 3. CP-C2 — an exact nonconcentric six-scalar bridge

Let \(t\) be the unique root in \((0,1/12)\) of
\[
 f(T)=64T^3-80T^2+28T-1.
\tag{C6}
\]
The specification is exact: \(f(0)=-1\), \(f(1/12)=22/27>0\),
and throughout this interval
\(f'(T)=192T^2-160T+28>28-160/12>0\).
Define fixed real constants
\[
 h=\sqrt t>0,\qquad r=h(4t-2)<0,\qquad s=h(5-8t)>0.
\tag{C7}
\]
They satisfy the three simultaneous identities
\[
 3h^2+s^2=1,\qquad s=h-2r,\qquad H(h)=-2r.
\tag{C8}
\]
The first follows by rewriting \(f(t)=0\) as
\(t(5-8t)^2=1-3t\); the other two follow directly from (C7).
All four points in each frame
\[
 F(c,h)=\{c-h,c+h,c-s,c+s\}
\]
are distinct, since \(s/h=5-8t>13/3>1\).

**PROVED.** The two frames \(F(r,h)\) and \(F(-r,h)\) have distinct
centers, share exactly two actual scalars, and give a selected output
realized by four distinct controlled ordered pairs with two different
first coordinates.

**Proof and explicit pair list.** Put
\[
 a=-r-h,
 \qquad b=-r+h,
 \qquad d=-r+s=-3r+h.
\tag{C9}
\]
Since \(-r-s=-b\), the two frames are
\[
 F(-r,h)=\{a,b,-b,d\},\qquad
 F(r,h)=\{-a,-b,b,-d\}.
\]
Their union is
\[
 A_2=\{\pm h(1-4t),\ \pm h(3-4t),\ \pm h(7-12t)\}.
\tag{C10}
\]
All three positive magnitudes are strictly increasing, so these are six
distinct points; the frame intersection is exactly \(\{b,-b\}\).
From CP-C1 and \(H(h)=-2r\), the eight controlled pairs are

| Selected output | Distinct controlled ordered pairs |
|---|---|
| \(0\) | \((a,-b),(a,d),(-a,b),(-a,-d)\) |
| \(4r\) | \((-b,b),(-b,-d)\) |
| \(-4r\) | \((b,-b),(b,d)\) |

The first coordinates in the zero row are \(a\ne-a\), so this is
output merging between frames, not four formal descriptions of one row.
The central scalar gap is \(2h(1-4t)\); the next gap is \(2h\),
which is different since \(t>0\). Hence the six-scalar set is not an
AP. This proves the finite bridge. \(\square\)

Its exact ledger is \(N=6,Q=8,Z=3,B=28\), with safe whole-image
certificate \(Z+B=31\). This is a finite algebraic realization; it
does not alone prove an asymptotic saving or an exact full-image count.

## 4. CP-C3 — the fixed-width ladder and its exact counts

Keep \(t,h,r,s\) fixed as above. Only the integer length \(m\ge1\)
grows. Prescribe frame centers and controlled pairs by
\[
 c_j=(2j-1)r,\qquad 0\le j\le m-1,
\]
\[
 E_m=\bigcup_{j=0}^{m-1}
       \{c_j-h,c_j+h\}\times\{c_j-s,c_j+s\}.
\tag{C11}
\]
Let \(A_m\) be the actual union of their scalar endpoints. Since
\(s=h-2r\), the two target endpoints at frame \(j\) are
\(c_{j-1}+h\) and \(c_{j+1}-h\). Thus
\[
 \boxed{A_m=
  \{c_i+h:-1\le i\le m-1\}
  \ \cup\ \{c_i-h:0\le i\le m\}.}
\tag{C12}
\]
This is an exact compatibility rule: adjacent frames reuse actual scalar
endpoints, and their row outputs coincide by (C4), (C8). The definition
does not discard boundary endpoints or identify merely nearby scalars.
Both \(A_m\) and \(E_m\) are nested as \(m\) grows. At \(m=2\),
the centers are \(-r,r\), so (C12) is exactly the bridge (C10).

**PROVED input count and ordering.** Put \(R=-r=h(2-4t)>h\),
\(p_i=c_i+h\), and \(n_i=c_i-h\). Within each displayed sequence,
different indices give different scalars. An equality between the two
sequences would require \((i-j)r=-h\), impossible since \(|r|>h\).
Hence \(N=2m+2\). The complete increasing order is
\[
 n_m,\ n_{m-1},p_{m-1},\ n_{m-2},p_{m-2},\ldots,
 n_0,p_0,\ p_{-1}.
\tag{C13}
\]
The gaps are \(2R\) at both ends, \(2h\) inside each of the \(m\)
source pairs, and \(2R-2h>0\) between successive source pairs. Because
\(R>h\), there are unequal gaps for every \(m\ge1\), so every
\(A_m\) is non-AP.

**PROVED pair and output counts.** All \(2m\) source coordinates are
distinct. Each has two distinct target coordinates, giving exactly
\(Q=4m\) ordered pairs, without repeated pair labels. Their two
outputs at frame \(j\) are
\[
 P(c_j+h,c_j\pm s)=4(j-1)r,\qquad
 P(c_j-h,c_j\pm s)=4jr.
\tag{C14}
\]
Therefore
\[
 \boxed{P(E_m)=\{4r\ell:-1\le\ell\le m-1\},\qquad Z=m+1.}
\tag{C15}
\]
Since \(r\ne0\), these output labels are distinct. The labels
\(\ell=-1,m-1\) each arise from a single row and have two pairs.
Each \(0\le\ell\le m-2\) arises from the positive row of frame
\(\ell+1\) and the negative row of frame \(\ell\), with distinct
first coordinates, and has four pairs. There are no other selected
output identifications. Thus the selected-fiber histogram is exactly
two fibers of size two and \(m-1\) fibers of size four.

## 5. CP-C4 — complete square, actual-image bound, and the stop

The exact ledger for every \(m\ge1\) is
\[
 \begin{aligned}
 N&=2m+2,& Q&=4m,& Z&=m+1,\\
 B=N^2-Q&=4m^2+4m+4,&
 Z+B&=4m^2+5m+5.
 \end{aligned}
\tag{C16}
\]
The three relevant ratios are
\[
 \frac{2Q}{N}=\frac{4m}{m+1},\qquad
 \frac QZ=\frac{4m}{m+1},\qquad
 \frac Q{N^2}=\frac{m}{(m+1)^2}\longrightarrow0.
\tag{C17}
\]
For a disjoint block partition of the actual scalar set, use the \(m\)
source blocks \(\{c_j-h,c_j+h\}\), together with the two singleton
blocks \(\{p_{-1}\}\) and \(\{n_m\}\). Every selected pair joins
different blocks of this partition: its target is in the previous/next
source block or one of the boundary singletons. Thus all \(4m\) selected
pairs are cross-block, and the local-pair count is zero. Exactly
\(4(m-1)\) of them lie in output fibers represented in two distinct
frame centers; the remaining four belong to the two end output fibers.
These counts are subdivisions of \(Q\), not extra gains. Endpoint
sharing and output merging are already reflected in \(N,Q,Z\).

All remaining ordered pairs, including diagonal, reverse, and distant-frame
pairs, remain charged. Without any unproved assertion about their outputs,
\[
 \boxed{|P(A_m,A_m)|\le Z+B=4m^2+5m+5.}
\tag{C18}
\]
This is a safe upper certificate, not an exact cardinality formula. The
selected-support gate is linear, but the complement is quadratic and
selected fibers are bounded by four, already failing to improve the old
\(N^{4/3}\) selected-pair rate.

There is a definitive actual-image obstruction as well. The positive-sign
sequence in (C12), \(\{p_i:-1\le i\le m-1\}\), is an \(m+1\)-point
AP with fixed nonzero step \(q=2r\). Reduction using (C6) gives
\[
 q^2=4t(4t-2)^2=16t^2-12t+1.
\tag{C19}
\]
This is irrational: otherwise \(t\) would satisfy a nonzero rational
polynomial of degree two, contradicting the cubic irreducibility proved
in §6. GS-A4 therefore says that this sub-square has exactly
\((m+1)^2\) distinct outputs.

For completeness, if two index pairs \((i,j),(i',j')\) in an AP
\(a+q\mathbb Z\) have the same output, then
\[
 q^2\bigl((i-j)^3-(i'-j')^3\bigr)
   =(i'+j')-(i+j).
\]
Both the cube difference and the right side are integers. Irrationality
of \(q^2\) forces both to vanish. Real cube injectivity makes the
differences equal, and equality of the sums then makes the ordered pairs
identical. This checks the imported clause directly, including the
negative step \(q\).

Consequently the whole image satisfies
\[
 \boxed{\frac{N^2}{4}=(m+1)^2\le |P(A_m,A_m)|
       \le4m^2+5m+5.}
\tag{C20}
\]
For every fixed \(c>0\), the lower bound eventually exceeds
\(N^{2-c}\). This excludes the fixed ladder as an actual power-saving
family, independently of all incidental collisions. It is a scoped
sub-square argument, not a broad lattice or non-AP impossibility theorem.
The ladder stops here, with no further growth, sweep, or variant pursued.

## 6. Exact equality representation and full cost ledger

Reduction of (C6) modulo 3 is \(T^3+T^2+T+2\), which has no root
in \(\mathbb F_3\): its values at 0,1,2 are 2,2,1 respectively.
The primitive cubic \(f\) is therefore irreducible over \(\mathbb Q\).
Every input has the exact form \(x=hA(t)\), with \(A\) a rational
polynomial, and
\[
 P(hA(t),hB(t))
 =h\{t(A(t)-B(t))^3+A(t)+B(t)\}.
\tag{C21}
\]
Because \(h>0\), output equality is exactly equality of the braces in
\(\mathbb Q[T]/(f)\). This is a faithful exact representation of the
fixed real polynomial, not a numerical embedding or a scaling that changes
the target. The root interval specifies the real embedding. An exact finite
audit needs rational degree-at-most-two representatives modulo \(f\),
with no numerical equality test or field-tower computation.

| Item | Charged treatment | Status |
|---|---|---|
| Fixed choices and growth | Choose the unique \(t\), positive \(h\), and fixed \(r,s\) before varying only \(m\) | PROVED |
| Actual input lower and upper counts | Both equal \(2m+2\), with ordering and cross-branch distinctness proved in (C13) | PROVED |
| Same set and input thinning | One actual \(A_m\) supplies both coordinates. No thinning; every omitted pair remains in \(B\) | PROVED |
| Pair/parameter multiplicities | Four pairs per frame; source coordinates distinct, so \(Q=4m\). Frame or output labels never replace scalar pair counts | PROVED |
| Scalar and output reuse | Both average ratios are \(4m/(m+1)\); exact selected fibers have size two or four | PROVED |
| Useful cross-block counts | All \(4m\) selected pairs cross the stated disjoint block partition; \(4(m-1)\) have outputs represented at two distinct frame centers. Local-pair count is zero | PROVED |
| Simultaneous compatibility and boundaries | (C3), (C8), and (C12) enforce every scalar identification and retain all boundary endpoints | PROVED |
| Local splitting, moduli, and densities | No sieve or local-density gain. Reduction modulo 3 proves only the fixed polynomial's irreducibility | PROVED |
| Field degree and arithmetic machinery | \(t\) has degree three; actual inputs lie in one fixed field \(\mathbb Q(t,h)\) of degree at most six. No growing field, discriminant/regulator estimate, units, or tower is used | PROVED |
| Denominators and heights | Exact rational coordinates modulo fixed \(f\); normalized input coefficients grow linearly in \(m\). No denominator clearing rescales \(P\) | PROVED |
| Real projection and archimedean size | Positive root and the specified real embedding are fixed; diameter from (C13) is \(2(m+1)R+2h\). No packing gain is credited | PROVED |
| Branches and carries | Two scalar sequences, two rows per frame, both counted explicitly. No digit/carry certificate or growing branch saving | PROVED |
| Exceptional and uncovered outputs | Every one of \(B\) unprescribed ordered pairs costs at most one in (C18); incidental complete fibers are not assumed small or large | PROVED |
| Rates | At depth \(d=\log m\), input rate 1, selected pair/support rates 1, actual full-image rate 2 by (C20); net certified gap zero | PROVED |
| Improvement gate | Finite non-AP bridge with a four-pair output fiber; fixed-width extension has actual image at least \(N^2/4\) and is stopped | PROVED scoped obstruction |

CP-C1–CP-C4 concern the fixed T01 polynomial and exactly the hypotheses in
their sections, dated 2026-10-06. Their evidence is complete symbolic proof;
no finite run is a premise. Any separately released finite audit records
the actual complete square and its incidental fibers without changing these
quantifiers. Prior reports and data remain unchanged.

The fixed T01 target remains **OPEN**. The lead's one next finite obligation
concerns a third variable-width conic frame attached to the exact bridge
\(A_2\), sharing at least two old scalars and contributing a third distinct
first-coordinate row to output zero. No such frame is constructed, excluded,
enumerated, or pursued in this appendix.
