# Independent proof check: TJ-O1

T01 | 21 October 2026 | fixed polynomial \(P(x,y)=(x-y)^3+x+y\).

**Verdict: ACCEPTED. PROVED — TJ-C6.** The exact TJ-O1 system has no
admissible positive real solution. Thus **TJ-O1 is PROVED IMPOSSIBLE**
in its stated scope. This is internal independent proof verification,
not external review or a novelty claim.

## Sources and independence

The checker read the complete preceding
[README, especially §4](../2026-10-20-tetrahedral-junction/README.md),
[registered catalogue](../2026-10-20-tetrahedral-junction/catalogue.md),
and [compatibility proof](../2026-10-20-tetrahedral-junction/compatibility.md).
The user-supplied argument was conveyed through the lead's current
verification assignment. No separate verbatim proof attachment was
supplied to this checker; none is claimed read.

The checker independently verified the entire stated chain before
communicating a verdict or consulting the other referee. Historical
sources were not edited. No enumeration, mathematical executable,
polynomial-evaluation run, network access, or new role search occurred.

## Exact statement checked

Retain the positive-width, positive-gap system of TJ-O1:
\[
a,b>0,\quad D=2a+b,\quad e=a/4,\quad \ell=(a+b)/4,
\]
\[
3u^2+v^2=3p^2+q^2=3w^2+r^2=3H^2+S^2=1,
\]
\[
C(u)=a,\quad C(p)=a+b,\quad C(w)=b,\quad C(H)=D,
\qquad C(x)=8x(1-2x^2).
\]
All halfwidths are positive, with row halfwidths in
\((0,1/\sqrt3)\). The original distinct-slot restrictions are retained,
although the contradiction does not need them. Fix \(\epsilon=-1\)
in the opposite-edge roles and impose the changed closing roles
\[
H=r,\qquad S=e+q.
\]
The nonexistence conclusion includes every admissible positive width
branch under the matching reflected-branch choices of TJ-O1.

## Independent checklist

1. **Actual signed-role reduction.** Relative to the common scalar
   offset \(D/4\), the centers of \(01,23,02,13,12,03\) are
   \(-\ell,\ell,-e,e,0,0\). The opposite roles
   \(R_{01}^{-}=K_{23}^{-}\) and \(R_{23}^{+}=K_{01}^{+}\)
   both reduce to \(2\ell=v-u\). The closing rows
   \(R_{03}^{\pm}=K_{12}^{\pm}\) give \(H=r\).
   The closing columns \(K_{03}^{-}=K_{02}^{-}\) and
   \(K_{03}^{+}=K_{13}^{+}\) give \(S=e+q\).
   Thus the argument addresses the actual signed TJ-O1 roles.

2. **Applicability of the common bounds.** The earlier derivation of
   \(0<u<1/6\) uses only \(2a<D\le C_{\max}\) and the shape of \(C\).
   Its proof of \(D>2\) uses only the conic and opposite-edge equation:
   \[
   D=2v+6u-16u^3,\qquad v>1-3u^2,
   \]
   \[
   D-2>u(6-6u-16u^2)>0.
   \]
   It does not depend on either former closing pattern.
   Since \(C(x)\le2\) on \([1/2,1/\sqrt3)\), it follows that
   \(H<1/2\). Also
   \[
   C(p)=a+b=2(v-u)<2
   \]
   because \(0<v<1\) and \(u>0\).

3. **Width order without assuming a branch.** Since \(e>0\),
   \(S=e+q>q\). The conics give
   \(S^2-q^2=3(p^2-H^2)>0\), so positivity implies \(p>H\).
   Suppose \(p\le1/2\). The derivative
   \(C'(x)=8-48x^2\) changes sign once, from positive to negative;
   therefore the minimum of \(C\) on \([H,1/2]\) is attained at
   an endpoint. Consequently
   \[
   C(p)\ge\min\{C(H),C(1/2)\}=2,
   \]
   contradicting \(C(p)<2\). Thus \(p>1/2\).
   The conic \(q^2=1-3p^2\), with \(p,q>0\), then gives \(q<p\).

4. **Upper comparison.** Put \(g=C/4=2x-4x^3\).
   The output gaps imply \(e=g(p)-g(w)\), so the changed closure gives
   \[
   S+g(w)=q+g(p)<p+g(p)=3p-4p^3\le1.
   \]
   The maximum assertion follows from the derivative
   \(3-12p^2\); the maximum on the positive frame domain is \(1\)
   at \(p=1/2\). The preceding strict inequality is justified by
   \(q<p\), independently of whether the maximum is attained.

5. **Incompatible lower comparison.** Since \(H=r<1/2\),
   the conics give \(1/2<w<1/\sqrt3\) and \(S^2=9w^2-2\).
   Both \(S\) and \(3w-1\) are positive, and
   \[
   S^2-(3w-1)^2=6w-3>0.
   \]
   Hence \(S>3w-1\), with no sign ambiguity from comparing squares.
   Therefore
   \[
   S+g(w)>5w-4w^3-1>1,
   \]
   where
   \[
   5w-4w^3-2=(2w-1)(2-w-2w^2)>0.
   \]
   The first factor is positive. The second is positive because
   \(w<1\) and \(w^2<1/3\) imply
   \(2-w-2w^2>1/3\). This contradicts item 4.

## Boundaries, unused conditions, and scope

Every strict step follows from a stated positive width or gap.
The disallowed boundary \(u=0\) would give \(a=0\) and merge output
labels. The value \(p=1/2\) is excluded by \(C(p)<2\), and
\(H=1/2\) by \(C(H)>2\); neither exclusion is assumed to choose
a favorable branch. No cancellation by a potentially zero variable
or sign-ambiguous squaring is used.

The distinct-slot restrictions, additional scalar coincidences,
requirement of at least two new ordered pairs, and requirement of a
third distinct first coordinate are not used. They only restrict an
already empty necessary system. There is consequently no seed and no
numerical \(N,Q,Z,B\) or full-image ledger to report.

TJ-C6 resolves only the specified TJ-O1 roles with \(\epsilon=-1\),
the \((a,b,a)\) output rule, and the stated reflected branch choices.
It neither classifies other tetrahedral roles nor establishes a
general obstruction for frame networks or for the fixed T01 target.
No successor construction or search is proposed by this check.
