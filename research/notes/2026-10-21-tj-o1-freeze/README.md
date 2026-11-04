# TJ-O1 freeze: the modified column closure is impossible

T01 · 21 October 2026 · version 1 · offline proof verification

**PROVED — TJ-C6. TJ-O1 is PROVED IMPOSSIBLE in its stated scope.**
The supplied contradiction is correct. The lead, an algebraic referee,
and a separate proof-checking agent independently checked its implications,
domains and signs. The fixed target \(P(x,y)=(x-y)^3+x+y\) remains **OPEN**.

The reason is elementary: the changed column identification forces one
row width onto the upper branch of the cubic gap function. The closing
equation then identifies a quantity strictly below one with a quantity
strictly above one.

[Algebraic referee](algebraic-referee.md) · [Separate proof check](proof-check.md) ·
[Source and verification ledger](verification.md)

## Exact statement and geometric meaning

Keep the [accepted checkpoint](../2026-10-20-tetrahedral-junction/README.md),
its output rule \((0,a,a+b,D)\), and its \(\epsilon=-1\) roles, where
\[
a,b>0,\qquad D=2a+b,\qquad e=a/4,\qquad \ell=(a+b)/4,
\]
\[
C(x)=8x(1-2x^2),\qquad g(x)=C(x)/4=2x-4x^3.
\]
The four row halfwidths \(u,p,w,H\) lie in \((0,1/\sqrt3)\);
the column halfwidths \(v,q,r,S\) are positive. They satisfy
\[
3u^2+v^2=3p^2+q^2=3w^2+r^2=3H^2+S^2=1,
\]
\[
C(u)=a,\quad C(p)=a+b,\quad C(w)=b,\quad C(H)=D,
\qquad 2\ell=v-u.
\tag{1}
\]
TJ-O1 adds precisely
\[
H=r,\qquad S=e+q.
\tag{2}
\]
**TJ-C6:** no real tuple satisfies these conditions. In particular, none
satisfies the additional frame nondegeneracy, two-new-pair and third-row
requirements of TJ-O1.

Here \(q\) is a column halfwidth, not a frame center. Relative to the common
scalar center \(D/4\), frame \(03\) has rows \(\pm H\) and columns \(\pm S\);
frame \(12\) has columns \(\pm r\); frames \(02,13\) have centers \(-e,e\)
and column halfwidth \(q\). Thus (2) says
\[
R_{03}^{\pm}=K_{12}^{\pm},\qquad
K_{03}^{-}=K_{02}^{-},\quad K_{03}^{+}=K_{13}^{+},
\]
where \(R\) means a row scalar and \(K\) a column scalar. The opposite-edge
roles are \(R_{01}^{-}=K_{23}^{-}\) and \(R_{23}^{+}=K_{01}^{+}\);
both give \(2\ell=v-u\). No sign or role has been changed.

## Complete contradiction

**1. The inherited common bounds still apply.** The derivation of TJ-C1
uses only (1), positivity and the conics, not either former closing pattern.
For clarity, \(C_{\max}=16/(3\sqrt6)\) and
\(a<D/2\le C_{\max}/2\) force \(0<u<1/6\): on
\([1/6,1/\sqrt3]\), the only interior critical point of \(C\) is a maximum,
and both endpoint values exceed \(C_{\max}/2\).
Since \(0<v<1\), we have \(v>v^2=1-3u^2\), so
\[
C(H)=D=C(u)+2(v-u)=2v+6u-16u^3
>2+u(6-6u-16u^2)>2.
\]
As \(C\) decreases from \(C(1/2)=2\) on
\([1/2,1/\sqrt3)\), this forces \(H<1/2\). Also
\[
C(p)=a+b=2(v-u)<2.
\tag{3}
\]

**2. The new columns force \(p>H\).** Since \(e>0\), (2) gives \(S>q>0\).
The conics therefore give
\[
3(p^2-H^2)=S^2-q^2>0.
\]
Both row widths are positive, hence \(p>H\).

**3. The branch inference is strict and includes every admissible root.**
The exact factorization is
\[
C(x)-2=2(1-2x)(4x^2+2x-1).
\]
Because \(H<1/2\) and \(C(H)>2\), we have \(4H^2+2H-1>0\).
The quadratic \(4x^2+2x-1\) strictly increases for \(x>0\).
If \(H<p<1/2\), both factors would be positive at \(p\), giving \(C(p)>2\).
If \(p=1/2\), then \(C(p)=2\). Both contradict (3), so \(p>1/2\).
Consequently
\[
p^2-q^2=4p^2-1>0,\qquad q<p.
\]
Using positive \(p,q\) and the identity
\(1-(3p-4p^3)=(2p-1)^2(p+1)\ge0\), we obtain
\[
q+g(p)<p+g(p)=3p-4p^3\le1.
\tag{4}
\]

**4. The central column identification forces the opposite inequality.**
Since \(H=r<1/2\) and \(3w^2+r^2=1\), we have
\(1/2<w<1/\sqrt3\). Combining the conics gives \(S^2=9w^2-2\).
Both \(S\) and \(3w-1\) are positive, and
\[
S^2-(3w-1)^2=6w-3>0.
\]
Thus \(S>3w-1\), and
\[
S+g(w)>5w-4w^3-1>1.
\tag{5}
\]
The final strict inequality follows from
\[
5w-4w^3-2=(2w-1)(2-w-2w^2)>0.
\]
The first factor is positive; the second is greater than
\(4/3-1/\sqrt3>0\) throughout the admissible interval.

**5. The gap equation identifies the two quantities.** From (1),
\[
e=\frac{C(p)-C(w)}4=g(p)-g(w).
\]
Substituting this into \(S=e+q\) yields
\[
S+g(w)=q+g(p),
\]
contradicting (4) and (5). This proves TJ-C6.

## Sign audit and scope of the freeze

Every square comparison above has positive terms. No possibly zero
expression is cancelled. The inequalities \(u>0\), \(e>0\), \(H<1/2\),
\(p>1/2\), and \(w>1/2\) are proved or explicit hypotheses. The comparisons
at \(1/2\) are auxiliary boundary values, not admitted solutions.
In the common bound, \(6-6u-16u^2>41/9>0\) for \(0<u<1/6\).

**PROVED, exact scope:** symmetric gaps \((a,b,a)\), the retained reflected
frame branches, the \(\epsilon=-1\) opposite-edge roles, and the modified
closing equations \(H=r,\ S=e+q\). Distinct scalar slots, pair deduplication,
two new closing pairs and a third distinct row are unused additional
restrictions; they cannot repair this inconsistent necessary subsystem.
No seed counts or full-image values are assigned.

**HISTORICAL / SUPERSEDED:** the 20 October TJ-O1 OPEN entry is preserved
verbatim, superseded only by this dated resolution. TJ-C1–C4 remain
unchanged. Other role assignments and the unrestricted T01 problem
remain **OPEN**.

The argument was supplied in the user's current message and verified here;
it is not a novelty claim. No numerical search, new construction, role sweep,
or successor research obligation was undertaken or adopted.
