# Algebraic referee: TJ-O1 is impossible in its stated scope

**T01 · 21 October 2026 · version 1 · offline proof verification.**

**ACCEPTED — PROVED, TJ-C6.** The user-supplied contradiction excludes
TJ-O1 as stated in the preceding [checkpoint, §4](../2026-10-20-tetrahedral-junction/README.md).
The independent algebraic check found no correction necessary. This is
an internal proof audit, not external review or a novelty assessment.
The fixed polynomial is \(P(x,y)=(x-y)^3+x+y\); its unrestricted
same-set real compression target remains **OPEN**.

## Exact statement and source correspondence

Let
\[
C(x)=8x(1-2x^2),\qquad g(x)=C(x)/4,\qquad
D=2a+b,\quad e=a/4,\quad \ell=(a+b)/4,
\]
where \(a,b>0\). There are no positive widths
\(u,v,p,q,w,r,H,S\), with row widths \(u,p,w,H<1/\sqrt3\),
satisfying
\[
3u^2+v^2=3p^2+q^2=3w^2+r^2=3H^2+S^2=1,
\]
\[
C(u)=a,\quad C(p)=a+b,\quad C(w)=b,\quad C(H)=D,
\]
\[
2\ell=v-u,\qquad H=r,\qquad S=e+q.
\tag{1}
\]

These are precisely the necessary scalar equations of TJ-O1:
the \(\epsilon=-1\) opposite-edge roles are retained, while the
closing columns reuse the outward columns of 02 and 13.
In the centered coordinates of the [catalogue](../2026-10-20-tetrahedral-junction/catalogue.md),
those new column identities read \(-S=-e-q\) and \(S=e+q\).
The retained closing row identities read \(\pm H=\pm r\).
No row/column interchange or sign change is implicit.

The original nondegeneracy conditions, at least two new closing
pairs, and a third distinct first coordinate are additional
requirements. They are unnecessary for the contradiction below.

## Independent check of the supplied proof

**1. The unchanged common bounds still apply.** The derivation of
TJ-C1 in the [prior compatibility proof, §1.3](../2026-10-20-tetrahedral-junction/compatibility.md)
uses the output gaps, conics, and opposite-edge equation, not the
old closing-column choice. Indeed,
\[
2a<D\le C_{\max}=\frac{16}{3\sqrt6}
\]
forces the unique short branch \(0<u<1/6\): the decreasing branch
has values above \(C_{\max}/2\), and
\(C(1/6)=34/27>C_{\max}/2\).
Writing \(v=\sqrt{1-3u^2}\) gives
\[
v>1-3u^2,\qquad
D=2v+6u-16u^3
>2+u(6-6u-16u^2)>2.
\]
The last factor is positive on \(0<u<1/6\).
Since \(C(x)\le2\) for \(1/2\le x<1/\sqrt3\), it follows that
\[
H<1/2,\qquad C(H)>2.
\]
The retained negative-sign opposite-edge equation also gives
\[
C(p)=4\ell=2(v-u)<2,
\tag{2}
\]
using \(v<1\) and \(u>0\).

**2. Every admissible \(p\)-branch forces \(p>1/2\).** Since
\(e>0\), the new column equation gives \(S=e+q>q\).
The two corresponding conics imply
\[
3(p^2-H^2)=S^2-q^2>0.
\]
All quantities are positive, so \(p>H\). The exact factorization is
\[
C(x)-2=2(1-2x)(4x^2+2x-1).
\tag{3}
\]
As \(H<1/2\) and \(C(H)>2\), the quadratic factor at \(H\)
is positive. Its value at \(p>H>0\) is strictly larger, since
\[
(4p^2+2p-1)-(4H^2+2H-1)
=(p-H)(4p+4H+2)>0.
\]
Equations (2)–(3) therefore force \(1-2p<0\), hence \(p>1/2\).
This sign argument selects no root in advance and covers all
admissible positive branches. In particular, \(p=1/2\) is excluded
by the strict inequality \(C(p)<2\).

It follows from \(q^2=1-3p^2\) that \(q<p\). Consequently
\[
q+g(p)<p+g(p)=3p-4p^3\le1.
\tag{4}
\]
The last inequality can be checked without differentiation:
\[
1-(3p-4p^3)=(2p-1)^2(p+1)\ge0.
\]

**3. The same quantity must exceed one.** Because \(H=r<1/2\),
the conic \(3w^2+r^2=1\) gives \(w>1/2\). The outer conic yields
\[
S^2=1-3H^2=9w^2-2.
\]
Both \(S\) and \(3w-1\) are positive, and
\[
S^2-(3w-1)^2=6w-3>0.
\]
Thus squaring has introduced no sign ambiguity, and
\[
S+g(w)>5w-4w^3-1>1.
\tag{5}
\]
Here
\[
5w-4w^3-2=(2w-1)(2-w-2w^2)>0
\quad\text{for }1/2<w<1/\sqrt3.
\]
The first factor is positive; the second is greater than
\(4/3-1/\sqrt3>0\).

Finally, the prescribed gaps give
\[
e=\frac{C(p)-C(w)}4=g(p)-g(w).
\]
Together with \(S=e+q\), this is exactly
\[
q+g(p)=S+g(w),
\]
contradicting (4)–(5). This proves TJ-C6.

## Audit scope and stopping record

The referee read the preceding README, catalogue, and compatibility
proof, then checked the supplied contradiction directly: the changed
roles, unchanged common-bound hypotheses, strict inequalities,
factorizations, positivity before square comparisons, and all width
branches. No cancellation by a possibly zero factor is used.
Zero widths or merged output labels lie outside the stated domain;
no boundary classification is claimed.

TJ-O1 is therefore **PROVED IMPOSSIBLE in its exact stated scope**.
This does not classify other endpoint roles, asymmetric output rules,
or arbitrary frame networks. No actual seed or \(N,Q,Z,B\) values
are produced. Earlier finite counts and image bounds remain separate
results, not consequences of this proof.

Only this documentation of the already checked argument was written.
No construction search, numerical enumeration, mathematical program,
target-polynomial evaluation, external lookup, or successor obligation
was undertaken. Earlier artifacts were left unchanged by the referee.
