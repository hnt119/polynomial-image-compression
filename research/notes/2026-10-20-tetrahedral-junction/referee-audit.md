# Independent audit of the four registered tetrahedral cases

**T01 — 20 October 2026 — internal independent mathematical audit.**

The four cases in [the frozen catalogue](catalogue.md) have no solution
in their stated positive-width domain. The proof is analytic and covers
every admissible width branch within those four cases. No exact seed
survives, so no scalar-square enumeration, full fiber histogram, or
attachment experiment is called for. This is a scoped nonexistence
result, not a classification of tetrahedral frames or a solution of T01.

The fixed polynomial throughout is
\[
P(x,y)=(x-y)^3+x+y.
\]
The same-set real compression target remains **OPEN**.

## 1. Source, assignment, and status

This audit checks the registered endpoint equations and the complete
manual deductions developed in the current authorized offline task.
The construction specialist, independent referee, and lead compared
the exact algebra before the conditional enumeration stage could be activated.
The referee has independently verified the deductions reproduced below.
Agreement between reviewers is not a substitute for those proofs.

The saved [compatibility proof](compatibility.md), version 1,
20 October 2026, was then read in full and accepted without correction
(SHA-256
`01dd084226f890b69f642529563cb5562fbb504282e52a7b15ea2ade6a03625c`).
The [main report](README.md) was also checked for fidelity to this proof,
the conditional counting statements, and the unsearched scope of TJ-O1.
That documentation check found no transcription or scope correction.

| Claim | Audit verdict and precise scope |
| --- | --- |
| TJ-C1 | **PROVED; independently audited.** Exact equations, short-width bound, and \(D>2\) for the registered opposite-edge roles. |
| TJ-C2 | **PROVED; independently audited.** No positive-width solution for either registered A sign. |
| TJ-C3 | **PROVED; independently audited.** No positive-width solution for either registered B sign. |
| TJ-C4 | **PROVED; independently audited.** All four registered cases are impossible. This does not quantify over unregistered endpoint-role assignments. |
| TJ-C5 | **PROVED conditional bookkeeping; independently audited.** The bounds below follow if a specified frame realization exists. They are not measured counts or an actual-image obstruction. |

The earlier [VO-C6 freeze](../2026-10-11-vo-o1-freeze/README.md)
and its [verification record](../2026-10-11-vo-o1-freeze/verification.md)
exist and record the exclusion of the original VO-O1 signed triangle
subsystem. Here they establish the inherited scope boundary only.
The old proof has not been rerun or recertified in this task and is not
used to infer the present four-case exclusion. The present contradictions
are written out independently below. Earlier varying-output counts and
the \(N^2/16\) image lower bound remain separate imported results, not
consequences of TJ-C1–TJ-C5.

## 2. Equation and role audit — TJ-C1

Put
\[
C(x)=8x(1-2x^2),\qquad g(x)=C(x)/4=2x-4x^3.
\]
A positive-width frame has row width \(h\), column width \(s\), and
\[
3h^2+s^2=1,\qquad 0<h<1/\sqrt3,\quad s>0.
\]
The catalogue also excludes \(h=s\), so its four scalar slots are
distinct within each frame.

The chosen outputs are
\[
(z_0,z_1,z_2,z_3)=(0,a,a+b,D),\qquad D=2a+b,\quad a,b>0.
\]
This gap symmetry is imposed; it is not a normalization of arbitrary
four outputs. Relative to the scalar center \(D/4\), the six frame
centers are
\[
q_{01}=-\ell,\quad q_{23}=\ell,\quad
q_{02}=-e,\quad q_{13}=e,\quad q_{12}=q_{03}=0,
\]
where \(e=a/4\) and \(\ell=(a+b)/4\).
The frame widths are \((u,v),(p,q),(w,r),(H,S)\) as in the catalogue.
Thus
\[
e=g(u),\quad \ell=g(p),\quad g(w)=\ell-e,\quad
g(H)=\ell+e,
\]
and
\[
3u^2+v^2=3p^2+q^2=3w^2+r^2=3H^2+S^2=1.
\]
Here \(q\) without an edge index is the column width of frames 02 and 13.

The two opposite-edge identifications read
\[
-\ell+\epsilon u=\ell-v,\qquad
\ell-\epsilon u=-\ell+v,
\]
and both are exactly \(2\ell=v+\epsilon u\), with
\(\epsilon\in\{-1,1\}\). They preserve the stated row and column roles.
Pattern A has precisely
\[
H=r,\qquad S=e+p,
\]
whereas pattern B has precisely
\[
H=e+q,\qquad S=w.
\]
Every scalar slot of frame 03 is therefore an already present scalar
slot if the corresponding system is realizable.

The reflection \(x\mapsto D/2-x\) satisfies
\[
P(D/2-x,D/2-y)=D-P(x,y).
\]
It reverses the four output labels and endpoint signs, preserving
row and column roles. Transposing row and column roles is not this
symmetry. No input scaling is used. Equal branches on edges 02 and 13
are an explicit catalogue restriction. Equality of their gaps alone
would not justify it.

### The short branch and the strict large-gap inequality

The maximum of \(C\) on the positive row-width interval is
\[
C_{\max}=\frac{16}{3\sqrt6}.
\]
Since \(2a<D=C(H)\le C_{\max}\), one has
\(a<C_{\max}/2\). On \([1/6,1/\sqrt3]\), the only interior critical
point of \(C\) is its maximum, and both endpoint values exceed
\(C_{\max}/2\):
\[
C(1/6)=\frac{34}{27}>\frac8{3\sqrt6},\qquad
C(1/\sqrt3)=\frac8{3\sqrt3}>\frac8{3\sqrt6}.
\]
For the first comparison, squaring positive quantities reduces to
\(1156>864\). Consequently
\[
0<u<1/6.
\]
The function \(C\) is strictly increasing there, so the admissible
short width is unique. No second admissible short branch has been
discarded by choosing the same \(u\) for 01 and 23.

As \(0<3u^2<1\),
\[
v=\sqrt{1-3u^2}>1-3u^2.
\]
Using the opposite-edge equation gives
\[
\begin{aligned}
D&=4(\ell+e)
 =2v+(8+2\epsilon)u-16u^3\\
 &>2+u(6-6u-16u^2)>2.
\end{aligned}
\]
The final factor is positive throughout \(0<u<1/6\); at \(1/6\)
it equals \(41/9\) and it decreases as \(u\) increases.
Since \(C\) decreases on \([1/2,1/\sqrt3]\), with \(C(1/2)=2\),
the strict inequality \(C(H)=D>2\) implies
\[
H<1/2.
\]
All endpoint and maximum cases have been retained until these strict
inequalities exclude them.

## 3. Both A cases — TJ-C2

In pattern A, \(H=r\) and \(3w^2+r^2=1\). Therefore \(H<1/2\)
implies \(w>1/2\), and
\[
S^2=1-3H^2=9w^2-2.
\]
The equations \(S=e+p\) and \(e=g(p)-g(w)\) yield
\[
p+g(p)=S+g(w).
\]
The left side is \(3p-4p^3\), whose maximum on
\(0<p<1/\sqrt3\) is \(1\), attained at \(p=1/2\).

On the other hand, \(S>0\) and \(3w-1>0\), and
\[
S^2-(3w-1)^2=6w-3>0.
\]
Hence \(S>3w-1\), with no sign ambiguity from squaring. Thus
\[
S+g(w)>5w-4w^3-1>1,
\]
because
\[
5w-4w^3-2=(2w-1)(2-w-2w^2)>0
\]
for \(1/2<w<1/\sqrt3\). The second factor is positive even at
the upper endpoint, where it is \(4/3-1/\sqrt3\).
This contradicts \(p+g(p)\le1\).

The proof applies to both signs and every admissible branch for \(p\).
It does not select a numerical root or assume that \(p\ne1/2\).

## 4. Both B cases — TJ-C3

Pattern B has \(S=w\), so
\[
3H^2+w^2=1,\qquad H<1/2<w<1/\sqrt3.
\]
For \(w\in[1/2,1/\sqrt3)\), set
\[
H(w)=\sqrt{(1-w^2)/3},\qquad
F(w)=3C(H(w))+C(w).
\]
Direct differentiation gives
\[
F'(w)=8\left[
\frac{w(1-2w^2)}{H(w)}-(6w^2-1)
\right].
\]
Both \(H(w)(6w^2-1)\) and \(w(1-2w^2)\) are positive for
\(w>1/2\) in this interval. With \(t=w^2\),
\[
\begin{aligned}
&H(w)^2(6w^2-1)^2-w^2(1-2w^2)^2\\
&\hspace{2em}=\frac{(4t-1)(-12t^2+12t-1)}3>0.
\end{aligned}
\]
Indeed \(1/4<t<1/3\), and the second factor is increasing there
from its value \(5/4\) at \(t=1/4\). The comparison of squares is
therefore valid and shows \(F'(w)<0\). Since \(F(1/2)=8\),
\[
3D+b=F(w)<8.
\]

But the output and opposite-edge equations also give
\[
\begin{aligned}
3D+b
 &=16\ell+8e\\
 &=8v+(16+8\epsilon)u-32u^3\\
 &\ge8(v+u-4u^3)>8.
\end{aligned}
\]
For the last strict inequality,
\[
v+u-4u^3
>1+u-3u^2-4u^3
=1+u(1-4u)(1+u)>1,
\]
using \(0<u<1/6\).
This is a contradiction for either sign.

In particular, the B proof needs only the closing restriction \(S=w\);
the other B restriction \(H=e+q\) is unnecessary for the contradiction.
This strengthens the necessary-subsystem exclusion but does not remove
the restriction \(S=w\) or classify other closing roles.

## 5. Conditional counts and graph capacity — TJ-C5

These are implications about a hypothetical realization, included to
audit the counting rules. TJ-C4 proves that the registered systems have
no realization, so none of these symbols is an observed seed statistic.

Let \(A\) be the deduplicated union of the scalar slots of the six frames,
\(E\subseteq A^2\) the deduplicated union of their four ordered pairs per
frame, and
\[
N=|A|,\quad Q=|E|,\quad Z=|P(E)|,\quad B=N^2-Q.
\]
The first five frames provide at most 20 scalar slots. The two
opposite-edge equations identify two disjoint pairs of these slots,
and frame 03 adds no scalar slots. Consequently \(N\le18\).
Additional coincidences can only reduce this upper bound.

Each frame provides four ordered pairs, so \(Q\le24\). The four
distinct prescribed outputs are all represented, so \(Z=4\).
Thus
\[
B=N^2-Q\ge N^2-24.
\]
This lower bound is allowed to be vacuous for small \(N\).
In particular \(N\le18\) must not be substituted as an equality,
nor may one report \(Q=24\) without deduplication.
The usual uncovered-pair certificate would be
\(|P(A,A)|\le Z+B=N^2-Q+4\); it is neither an equality nor an
actual-image lower bound.

More generally, if the frames form a simple graph on output labels,
each frame incident to output \(z_i\) contributes two ordered pairs
and one first coordinate at \(z_i\). Therefore
\[
|E\cap P^{-1}(z_i)|\le2\deg(i),
\qquad
|\{x:(x,y)\in E,\ P(x,y)=z_i\}|\le\deg(i).
\]
For \(K_4\), this is at most six selected pairs and three first
coordinates at each output. Deduplication may lower both counts.
The proposed admissibility test requires that closing frame 03
contribute a third distinct first coordinate at output \(0\) or \(D\);
this is an additional acceptance condition, not a consequence of
formal endpoint labels. It also requires at least two genuinely new
ordered pairs from 03. Neither condition has been certified on a seed,
because the underlying equations are already inconsistent.

For comparison within the proposed attachment plan, a new output
connected to all four old outputs by four frames could add at most
two selected pairs to each old output and at most eight selected
pairs at the new output, before deduplication. This counts selected
frame pairs only. It provides no bound on unselected pairs or the
complete image and does not establish an exponent saving.

## 6. Strictness, coverage, and stopping record — TJ-C4

All four registered assignments were addressed:
\((+,A),(-,A),(+,B),(-,B)\). No other role catalogue was tested.
The common bound uses \(a,b>0\), positivity of the column widths,
and the fixed polynomial's exact gap function. The A and B
contradictions retain all admissible branches and use only comparisons
whose squared quantities are positive. The excluded boundary
\(u=0\) would remove the strict gap separation and is not an exception
inside the prescribed domain. The value \(H=1/2\) is excluded by
\(D>2\), not by an unproved branch convention.

The prescribed scalar-sharing equations alone connect 01 with 23
and connect 03 with 02, 13, and 12. They do not force those two
groups to share a scalar with each other. The output-label graph is
connected; a connected scalar-sharing graph was never silently assumed.

**Finite budget used:** four analytic case assignments, zero finite
instances enumerated, zero target-\(P\) evaluations, and zero
programmatically checked research predicates. No research program,
package installation, internet search, or old finite test was run by
the referee. File reads and document creation are not mathematical
enumeration.

No \(A\), full-square image size, fiber distribution, finite tail table,
or successful attachment is asserted for this failed catalogue.
Continuation is stopped at the incompatible base case.
TJ-O1, if recorded separately, is a single unsearched future change
to the closing column roles. It is **OPEN**; this audit neither tests
nor resolves it.
