# Exact compatibility of the four frozen tetrahedral cases

T01 | 20 October 2026 | version 1 | offline analytic proof.

The fixed polynomial is
\[
P(x,y)=(x-y)^3+x+y.
\]
This appendix proves that none of the four simultaneous real systems in
[the preregistered catalogue](catalogue.md) is realizable. It does not
classify other tetrahedral role assignments or arbitrary four-output
networks. No mathematical program, numerical search, polynomial evaluation,
or finite predicate enumeration was run.

**Proof status.** The common bounds and the two contradictions below were
independently checked during derivation by the lead and the mathematical
referee. The claims are **PROVED** within the stated catalogue. The
unrestricted T01 target remains **OPEN**.

## 1. TJ-C1 — frame equations, signed roles, and common bounds

### 1.1 The frame identity and all positive width branches

For positive \(h,s\) satisfying \(3h^2+s^2=1\), define the frame's
controlled ordered pairs by
\[
E(q_0,h,s)=\{q_0-h,q_0+h\}\times\{q_0-s,q_0+s\}.
\]
The first factor consists of row scalars; the second consists of column
scalars. Expansion gives
\[
P(q_0+h,q_0+s)-P(q_0+h,q_0-s)
 =2s(1-3h^2-s^2)=0.
\]
Their common value is
\[
2q_0+h^3+3hs^2+h
 =2q_0+4h-8h^3.
\]
Consequently, with
\[
C(h)=8h(1-2h^2),\qquad g(h)=C(h)/4=2h-4h^3,
\]
the two row outputs are
\[
P(q_0\pm h,q_0\pm s)=2q_0\pm C(h)/2,
\]
where the column sign is independent of the row sign. Since
\(0<h<1/\sqrt3\), one has \(C(h)>0\). Thus a frame assigned the
ordered outputs \(z_i<z_j\) must satisfy
\[
q_{ij}=(z_i+z_j)/4,\qquad C(h_{ij})=z_j-z_i,\qquad
s_{ij}=\sqrt{1-3h_{ij}^2}>0.
\]
Four distinct scalar slots require \(h_{ij}\ne s_{ij}\), equivalently
\(h_{ij}\ne1/2\).

No positive width branch is discarded in the catalogue. Indeed,
\[
C'(h)=8-48h^2,\qquad
C_{\max}=C(1/\sqrt6)=\frac{16}{3\sqrt6},\qquad
C_{\rm end}=\lim_{h\uparrow1/\sqrt3}C(h)=\frac8{3\sqrt3}.
\]
On the open interval \(0<h<1/\sqrt3\), a gap \(c\) has one positive
root when \(0<c\le C_{\rm end}\), two when
\(C_{\rm end}<c<C_{\max}\), one when \(c=C_{\max}\), and none when
\(c>C_{\max}\). The endpoint \(h=1/\sqrt3\) is never admitted.
When \(c=2\), the root \(h=1/2\) is removed by the four-slot
condition; any other admissible root remains. The proof below applies
to all roots that survive these conditions.

### 1.2 Output rule and exact signed slot equations

Choose \(a,b>0\) and prescribe
\[
(z_0,z_1,z_2,z_3)=(0,a,a+b,D),\qquad D=2a+b.
\]
This reflection-symmetric gap rule is an imposed restriction, not a
normalization of arbitrary four outputs. No scalar scaling is used.
Put
\[
\tau=D/4,\qquad e=a/4,\qquad \ell=(a+b)/4.
\]
The following coordinates are relative to \(\tau\); the actual scalar
coordinate is obtained by adding \(\tau\) to every entry.

| Edge | Relative center | Row halfwidth | Column halfwidth |
| --- | ---: | ---: | ---: |
| 01 | \(-\ell\) | \(u\) | \(v\) |
| 23 | \(\ell\) | \(u\) | \(v\) |
| 02 | \(-e\) | \(p\) | \(q\) |
| 13 | \(e\) | \(p\) | \(q\) |
| 12 | \(0\) | \(w\) | \(r\) |
| 03 | \(0\) | \(H\) | \(S\) |

Here \(q\) denotes a column halfwidth, not a frame center. Every width
is positive, every row halfwidth is less than \(1/\sqrt3\), and
\[
3u^2+v^2=3p^2+q^2=3w^2+r^2=3H^2+S^2=1,
\]
\[
C(u)=a,\quad C(p)=a+b,\quad C(w)=b,\quad C(H)=D.
\tag{1}
\]
Equal width branches on 02 and 13 are imposed by the catalogue;
equal output gaps alone would not imply that choice.
The scalar reflection \(x\mapsto D/2-x\) sends \(P\) to \(D-P\).
It exchanges edges 01 with 23 and 02 with 13, and preserves 03
and 12. It reverses endpoint signs while preserving row and column
roles; interchanging rows with columns is not used as a symmetry.

Write \(R_{ij}^{\sigma}=q_{ij}+\sigma h_{ij}\) and
\(K_{ij}^{\sigma}=q_{ij}+\sigma s_{ij}\). For
\(\epsilon\in\{-1,1\}\), the opposite-edge requirements are
\[
R_{01}^{\epsilon}=K_{23}^{-},\qquad
R_{23}^{-\epsilon}=K_{01}^{+}.
\]
Their relative-coordinate equations are
\[
-\ell+\epsilon u=\ell-v,\qquad
\ell-\epsilon u=-\ell+v,
\]
so both reduce to
\[
2\ell=v+\epsilon u.
\tag{2}
\]
The two closing patterns are exactly:

| Pattern | Signed row reuse | Signed column reuse | Equivalent width equations |
| --- | --- | --- | --- |
| A | \(R_{03}^{\pm}=K_{12}^{\pm}\) | \(K_{03}^{-}=R_{02}^{-}\), \(K_{03}^{+}=R_{13}^{+}\) | \(H=r,\ S=e+p\) |
| B | \(R_{03}^{-}=K_{02}^{-}\), \(R_{03}^{+}=K_{13}^{+}\) | \(K_{03}^{\pm}=R_{12}^{\pm}\) | \(H=e+q,\ S=w\) |

Thus there are four cases: \((+,A),(-,A),(+,B),(-,B)\).
Each closing table would make all four scalar slots of frame 03 old.
The prescribed equalities connect 01 to 23 and separately connect 03
to 12, 02, and 13. They do not themselves establish a scalar-sharing
connection between these two groups.

### 1.3 Common strict bounds

**PROVED — TJ-C1.** Any realization of either closing pattern would have
\[
0<u<1/6,\qquad D>2,\qquad 0<H<1/2.
\tag{3}
\]

First, (1) and \(b>0\) give
\[
0<a<D/2\le C_{\max}/2<C_{\rm end}.
\]
Thus \(u\) is the unique root on the increasing branch of \(C\).
Furthermore
\[
C(1/6)=\frac{34}{27}>\frac{C_{\max}}2,
\]
as is verified without approximation by
\[
\left(\frac{34}{27}\right)^2-
\left(\frac8{3\sqrt6}\right)^2=\frac{292}{729}>0.
\]
Since \(1/6<1/\sqrt6\), monotonicity gives \(u<1/6\).

Equation (2) and \(a=C(u)\) yield
\[
D=a+(a+b)
  =2v+(8+2\epsilon)u-16u^3.
\tag{4}
\]
Since \(0<v<1\), the conic gives \(v>v^2=1-3u^2\).
Therefore, for either sign,
\[
D-2>u(6-6u-16u^2)>0
\]
on \(0<u<1/6\). Finally \(C\) is strictly decreasing on
\([1/2,1/\sqrt3)\), with \(C(1/2)=2\).
The equation \(C(H)=D>2\) thus forces \(H<1/2\).
These deductions retain every branch for \(p,w,H\) not already
excluded by the equations themselves.

## 2. TJ-C2 — both cases of pattern A are impossible

**PROVED.** Assume pattern A. Since \(H=r<1/2\) and
\(3w^2+r^2=1\), one has \(w>1/2\). Combining the two conics gives
\[
S^2=1-3H^2=9w^2-2.
\tag{5}
\]
Meanwhile, the output gaps in (1) imply
\[
e=g(p)-g(w).
\]
The closing equation \(S=e+p\) therefore gives
\[
p+g(p)=S+g(w).
\tag{6}
\]
For every \(0<p<1/\sqrt3\),
\[
p+g(p)=3p-4p^3\le1,
\tag{7}
\]
because its derivative is \(3-12p^2\), with its unique maximum at
\(p=1/2\).

On the other hand, \(S>0\) and \(3w-1>0\), and (5) gives
\[
S^2-(3w-1)^2=6w-3>0.
\]
Thus \(S>3w-1\), and consequently
\[
S+g(w)>5w-4w^3-1>1.
\tag{8}
\]
The last strict inequality follows from
\[
5w-4w^3-2=(2w-1)(2-w-2w^2)>0
\]
for \(1/2<w<1/\sqrt3\). Both factors are positive on that
interval. Equations (6)–(8) contradict one another.

This contradiction is independent of \(\epsilon\) after the common
bound \(D>2\), and it uses no choice of the positive \(p\)-branch.
It excludes both frozen A cases.

## 3. TJ-C3 — both cases of pattern B are impossible

**PROVED.** Assume pattern B. It is enough to use its requirement
\(S=w\); the further equation \(H=e+q\) will not be needed.
The long-frame conic and (3) give
\[
3H^2+w^2=1,\qquad \frac12<w<\frac1{\sqrt3}.
\tag{9}
\]
Define, on this interval,
\[
H(w)=\sqrt{\frac{1-w^2}{3}},\qquad
\Phi(w)=3C(H(w))+C(w).
\]
Differentiation gives
\[
\Phi'(w)
=8\left[\frac{w(1-2w^2)}{H(w)}-(6w^2-1)\right].
\tag{10}
\]
Both quantities compared inside the brackets are positive. Put
\(\theta=w^2\in(1/4,1/3)\). The exact difference of squares is
\[
H(w)^2(6w^2-1)^2-w^2(1-2w^2)^2
=\frac{(4\theta-1)(-12\theta^2+12\theta-1)}{3}>0.
\tag{11}
\]
The first factor is positive. The second has value \(5/4\) at
\(\theta=1/4\) and positive derivative \(12-24\theta\) on the
whole interval, so it is positive too. Since the terms being
squared are positive, (11) proves \(\Phi'(w)<0\).

The auxiliary function extends continuously to \(w=1/2\), where
\(H=1/2\) and \(\Phi(1/2)=8\). This endpoint is used only for
comparison, not admitted as a nondegenerate frame. Therefore (9)
forces
\[
3C(H)+C(w)<8.
\tag{12}
\]

But (1), (2), and \(e=g(u)\) give
\[
\begin{aligned}
3C(H)+C(w)
 &=3D+b\\
 &=16\ell+8e\\
 &=8v+(16+8\epsilon)u-32u^3\\
 &\ge8\bigl(v+u-4u^3\bigr)\\
 &>8\bigl[1+u(1-3u-4u^2)\bigr]>8.
\end{aligned}
\tag{13}
\]
The penultimate inequality again uses \(v>1-3u^2\);
the final one uses \(0<u<1/6\), which gives
\(1-3u-4u^2>7/18>0\). This contradicts (12).
Both B cases are excluded simultaneously, with no branch
selection for \(p\) or \(q\).

## 4. TJ-C4 — conclusion and exact stopping scope

**PROVED — TJ-C4.** For every \(a,b>0\), neither sign
\(\epsilon\in\{-1,1\}\) admits a positive real solution of pattern
A or pattern B in the frozen catalogue. The statements include every
admissible positive width branch, subject to the imposed matching
branches on reflected edges.

The intended extra tests were that frame 03 add at least two distinct
ordered pairs after deduplication and that some output acquire a third
distinct first coordinate. These tests, and all further scalar
coincidences, cannot repair an empty necessary compatibility system.
There is no actual seed to which \(N,Q,Z,B\), a complete image size,
or an extension rate can be assigned. In particular, none of these
quantities is reported as zero or inferred from the formal slot counts.
The proposed extension stops at its failed base case.

The proof does **not** assert nonexistence for all tetrahedral roles,
unequal outer gaps, unequal reflected width choices, arbitrary frame
networks, or the fixed-polynomial target itself. It does not require
the frozen VO-C6 triangle contradiction: that source was read to
preserve its scope, and no equation here is justified by treating
VO-C6 as a broader exclusion.

## 5. Provenance and computation boundary

The catalogue was selected and saved before elimination. Its output
rule and four signed role assignments were not changed after the
contradictions were found. Frame algebra was read in the preceding
[varying-output compatibility appendix](../2026-10-11-varying-output-frames/compatibility.md)
and expanded explicitly in §1.1 here. The
[VO-C6 freeze](../2026-10-11-vo-o1-freeze/README.md) was inspected
for the boundary of the prior exclusion; it is not a proof dependency.

The lead supplied the useful common bound \(D>2\) and the function
\(3C(H(w))+C(w)\) for pattern B. The construction specialist derived
the pattern-A maximum contradiction and checked the exact B derivative
and factor. The referee independently checked the common bounds,
signed equations, both contradictions, and all strict domains.
These are internal mathematical checks, not external review or a
novelty assessment.

Only four preregistered role assignments were considered.
No exact seed survived. The conditional finite-evaluation stage was
therefore not run: **zero executable polynomial evaluations, zero
enumerated exact predicates, and no mathematical search program**.
File reads and document-integrity checks are not mathematical
enumeration. Historical proof and experiment artifacts are preserved.
