---
title: "Rich-fiber results checkpoint"
subtitle: "A corrected coverage criterion and one explicit construction with its exact image"
date: "September 6, 2026"
---

**Offline research.** The supplied frozen results were used as assumptions. No web search, external retrieval, or external verification was performed.

**Result.** CPSI is not proved in this cycle. One explicit changing-number-field construction produces a linearly large cubic fiber, but its complete image is
\[
4N^2-N+1
\]
on a set of size \(2N\). Its exponent gap is exactly zero.

There is also a substantive error in the proposed success criterion: rich fibers covering a fixed positive fraction of the pairs do not immediately bound the whole image by a smaller power. The following correction is necessary before FRC can be used as a route to CPSI. This report retains one concrete construction and gives its complete proof and ledger, rather than presenting a survey of unsuccessful candidates.

## A. Final conjecture and the coverage correction

The target remains
\[
P_3(x,y)=(x-y)^3-3(x+y),
\]
\[
\exists c_3>0,\quad
\exists\text{ arbitrarily large finite }A\subset\mathbb R,
\qquad |P_3(A,A)|\le |A|^{2-c_3}.
\tag{CPSI}
\]
The quadratic witness and the closed rational Chebyshev subclasses were not reopened.

### A.1 Why positive-density rich fibers are insufficient

Let \(f:X^2\to Y\), \(n=|X|\), and let \(m(z)\) be its fiber sizes. Exactly
\[
|f(X,X)|=\sum_{(x,y)\in X^2}\frac1{m(f(x,y))}.
\tag{1}
\]
For \(K\ge1\), put
\[
E_{<K}=\{(x,y)\in X^2:m(f(x,y))<K\}.
\]
Separating these pairs gives
\[
|f(X,X)|\le |E_{<K}|+\frac{n^2-|E_{<K}|}{K}.
\tag{2}
\]
If a fraction at least \(\delta\) lies in fibers of size at least \(n^\varepsilon\), the conclusion supplied by (2) is only
\[
\boxed{|f(X,X)|\le(1-\delta)n^2+\delta n^{2-\varepsilon}.}
\tag{3}
\]
For fixed \(0<\delta<1\), this retains exponent \(2\). The uncovered outputs cannot be discarded.

This invalidates the claimed immediate counting implication from FR/FRC to CPSI on the same witness. It does not disprove the existential possibility of a separate, polynomial-specific amplification theorem taking an FRC family to a different CPSI family.

### A.2 A correct sufficient and necessary criterion

**Proposition 1.** Suppose that fixed \(\varepsilon,\kappa>0\) and \(C<\infty\) satisfy
\[
\#E_{<n^\varepsilon}\le Cn^{2-\kappa}.
\tag{4}
\]
Then
\[
|f(X,X)|\le Cn^{2-\kappa}+n^{2-\varepsilon}
\le(C+1)n^{2-\min(\varepsilon,\kappa)}.
\tag{5}
\]
Conversely, if \(|f(X,X)|\le Cn^{2-c}\), then
\[
\#E_{<n^{c/2}}\le Cn^{2-c/2}.
\tag{6}
\]

**Proof.** Equation (5) is (2). For (6), each output in a small fiber accounts for fewer than \(n^{c/2}\) domain points, so there are at most \(n^{c/2}|f(X,X)|\) such points. \(\square\)

Thus the correct requirement is rich coverage of all but a power-saving number of pairs, or the equivalent reciprocal-multiplicity estimate (1). A fixed positive proportion alone leaves an additional theorem to prove.

### A.3 The issue persists inside the rational Chebyshev construction

Let \(\phi(t)=t^2+t^{-2}\).

**Proposition 2.** Given any finite \(A_0\subset\phi(\mathbb Q_{>0})\) of size \(a\), one can explicitly enlarge it to \(A\subset\phi(\mathbb Q_{>0})\), \(|A|=2a\), such that
\[
|P_3(A,A)|=3a^2+|P_3(A_0,A_0)|\ge\frac34|A|^2.
\tag{7}
\]
Every ordered pair having a new endpoint has its own output, distinct from all old outputs.

**Proof.** Add one new \(x=\phi(t)\) at a time. For the current finite set \(B\), the new output polynomials are
\[
P_3(x,b),\quad P_3(b,x)\quad(b\in B),\qquad -6x.
\]
All are nonconstant. In the first orientation the coefficients of \(x^3,x^2\) are \(1,-3b\); in the second they are \(-1,3b\). Different anchors and orientations therefore give different polynomials. The diagonal has degree one. Equality between two new outputs, or with an old output, excludes only finitely many \(x\). Composing any nonzero polynomial with the nonconstant rational function \(\phi\) still gives a nonzero rational function, so only finitely many rational \(t\) are excluded.

Enumerate positive rationals greater than one by increasing numerator plus denominator, and use the first admissible \(t\). After \(a\) additions, exactly \((2a)^2-a^2=3a^2\) new ordered pairs have distinct new outputs. \(\square\)

Consequently, if rational FRC families exist with parameters \((\varepsilon,\delta)\), they can be enlarged by this procedure while retaining FRC with parameters \((\varepsilon/2,\delta/9)\), yet their new real sets have quadratic image. Indeed, adding each \(t\) with \(t^{-1}\) preserves inversion symmetry, the parameter size grows by at most a factor three, and old multiplicities do not decrease. For large \(n\), \(n^\varepsilon\ge(3n)^{\varepsilon/2}\).

This is a conditional counterexample to the claimed same-witness implication within the precise rational architecture, not a counterexample to CPSI or to the existence of FRC families.

## B. One exact candidate construction

Define integer polynomials
\[
x(i)=36i^3+3i+2,\qquad y(i)=36i^3-3i+2.
\tag{8}
\]
They satisfy identically
\[
\boxed{P_3(x(i),y(i))=-12.}
\tag{9}
\]
We construct increasing positive integers \(i_1,i_2,\ldots\) by the explicit finite-search recursion below. Set
\[
A_N=\{x(i_j),y(i_j):1\le j\le N\}.
\tag{10}
\]
Every new pair of vertices is chosen above all old vertices; hence \(|A_N|=2N\).

For \(x>2\), let
\[
h(x)=\frac{\sqrt{x+2}+\sqrt{x-2}}2>1.
\]
Then
\[
h(x)^{-1}=\frac{\sqrt{x+2}-\sqrt{x-2}}2,\qquad
h(x)^2+h(x)^{-2}=x.
\tag{11}
\]
Define
\[
H_N=\{h(x),h(x)^{-1}:x\in A_N\},
\qquad
L_N=\mathbb Q(\sqrt{x+2},\sqrt{x-2}:x\in A_N).
\tag{12}
\]
We will prove
\[
\boxed{|H_N|=4N,\quad [L_N:\mathbb Q]=16^N,\quad
\sqrt3\notin L_N.}
\tag{13}
\]
The fields are totally real, and the selected embedding in (11) is positive on \(H_N\). Thus this is a legitimate changing-number-field Chebyshev construction.
Here and below
\[
\mathscr F(h,k)=P_3(h^2+h^{-2},k^2+k^{-2}).
\]

### B.1 Choosing each new index without accidental output collisions

For an old vertex \(a\) and \(\epsilon\in\{+1,-1\}\), write
\[
f_\epsilon(i)=36i^3+3\epsilon i+2.
\]
The leading coefficients of \(P_3(f_\epsilon(i),a)\) are
\[
[i^9]=46656,\quad [i^7]=11664\epsilon,\quad
[i^6]=7776-3888a.
\tag{14}
\]
They distinguish every \((\epsilon,a)\). The reversed polynomials have the negatives of these three coefficients, so are mutually distinct and cannot coincide with the first orientation. All have degree nine.

The four new/new outputs are
\[
\begin{aligned}
P_3(f_+,f_+)&=-216i^3-18i-12,\\
P_3(f_-,f_-)&=-216i^3+18i-12,\\
P_3(f_+,f_-)&=-12,\\
P_3(f_-,f_+)&=-432i^3-12.
\end{aligned}
\tag{15}
\]
The three nonconstant polynomials in (15) are distinct of degree three. All old outputs are constants. Every unwanted equality is therefore a nonzero polynomial equation in \(i\), excluding only finitely many integers. We impose all these exclusions at each stage.

### B.2 Congruences giving the field hypotheses

Impose \(i_j\equiv3\pmod9\). The four positive radicands at a stage are
\[
\begin{aligned}
R_1(i)&=3i(12i^2+1),&
R_2(i)&=36i^3+3i+4,\\
R_3(i)&=3i(12i^2-1),&
R_4(i)&=36i^3-3i+4.
\end{aligned}
\tag{16}
\]
Their valuations at \(3\) are \(2,0,2,0\). Every product of their square classes has even valuation at \(3\), so the class of \(3\) is not in their span.

We use the standard multiquadratic fact: if nonzero rational numbers span an \(r\)-dimensional subspace of \(\mathbb Q^\times/(\mathbb Q^\times)^2\), adjoining their square roots gives a degree-\(2^r\) extension; the quadratic subfields correspond to the nonzero classes in that span. It follows already that \(\sqrt3\notin L_N\).

To obtain exact degree, assign four new odd anchor primes at each stage, one to each polynomial
\[
12i^2+1,\quad36i^3+3i+4,\quad
12i^2-1,\quad36i^3-3i+4.
\tag{17}
\]
These polynomials are squarefree, pairwise coprime over \(\mathbb Q\), and nonzero at zero. Here are direct checks. The two quadratics differ by \(2\). Modulo \(12i^2+1\), the two cubics reduce to \(4\) and \(4-6i\); the latter could vanish only at \(i=2/3\), which is not a root of that quadratic. Modulo \(12i^2-1\), they reduce to \(4+6i\) and \(4\); again there is no common root. The cubics differ by \(6i\), and both are \(4\) at zero. The quadratic derivatives vanish only at zero. A common root of a cubic and its derivative would force \(i=-2\) or \(i=2\), respectively, incompatible with the corresponding derivative equation. These prove the assertions.

Exclude \(2,3\), their finitely many bad discriminant, resultant, leading-coefficient and constant-term primes, all earlier anchors, and all primes dividing previous radicands. For each polynomial choose the least remaining prime that divides one of its integer values. It has a simple root modulo that prime, shared by none of the other polynomials.

The elementary prime-divisor fact used here is that a nonconstant integer polynomial has infinitely many prime divisors among its nonzero integer values. To prove it, translate the variable so that the constant term is \(c\ne0\). If all such primes divided \(P\), then
\[
\frac{f(cPn)}c\equiv1\pmod p\qquad(p\mid P)
\]
is an integer polynomial in \(n\) whose absolute value can exceed one. A prime divisor of that value would also divide \(f(cPn)\), contradicting the congruence. This proves the fact.

At a new anchor \(p\), choose a lift of its root modulo \(p^2\) with valuation exactly one. A simple root has exactly one root lift among the \(p\) possible lifts; any other lift works. The designated radicand has valuation one, and all other current radicands are units at \(p\).

For every earlier anchor \(p\), impose
\[
i\equiv p^2\pmod{p^3}.
\tag{18}
\]
Then \(R_1,R_3\) have valuation two at \(p\), while \(R_2,R_4\) have valuation zero. The Chinese remainder theorem combines these conditions, the new-anchor conditions, and \(i\equiv3\pmod9\) into an infinite arithmetic progression.

Choose the least positive integer in that progression which gives two vertices above the old ones and avoids the finitely many unwanted equalities in B.1. This is a deterministic terminating recursion.

Each of the \(4N\) radicands has an anchor prime at which only its square class has odd valuation: preceding radicands are units there, and subsequent radicands have even valuation by (18). Their square classes are independent. The multiquadratic degree formula proves \([L_N:\mathbb Q]=2^{4N}=16^N\), finishing (13).

## C. Rich-fiber theorem and exact multiplicities

**Theorem 3.** The family (10)--(12) satisfies
\[
|A_N|=2N,\qquad
m_{A_N}(-12)=N,
\tag{19}
\]
and every other represented output has multiplicity one. In particular,
\[
\boxed{|P_3(A_N,A_N)|=4N^2-N+1.}
\tag{20}
\]

**Proof.** Equation (9) supplies \(N\) distinct ordered pairs. By (14)--(15) and the recursion, every other new pair produces a new output distinct from all old outputs and all other new outputs. Induction establishes the complete histogram. There are \(4N^2\) pairs; merging precisely the \(N\) matched pairs loses \(N-1\) output values. \(\square\)

The map \(h\mapsto h^2+h^{-2}\) has exactly two representatives in \(H_N\) for each vertex. Consequently each ordered \(A_N\)-pair has exactly four ordered \(H_N\)-lifts. With the task's definition of \(m_H\),
\[
\boxed{m_{H_N}(-12)=4N=|H_N|.}
\tag{21}
\]
Every other represented cubic value has \(H_N\)-multiplicity four. In the relative-trace normalization, these same fibers have trace value \(2z\), so the rich trace value is \(-24\). The multiplicities and image cardinalities are unchanged by this scalar factor.

This is a polynomially rich, explicitly constructed fiber in changing totally real fields. It is not a rational \(H_N\) construction. Indeed, if a positive rational \(h=a/b\) in lowest terms has \(h^2+h^{-2}\) integral, its denominator \((ab)^2\) is coprime to its numerator, forcing \(a=b=1\). Our vertices are integers greater than two.

## D. Cartesian coverage

The rich pairs cover exactly
\[
\frac{N}{(2N)^2}=\frac{4N}{(4N)^2}=\frac1{4N}
\tag{22}
\]
of the respective full squares. This tends to zero.

More precisely, for every fixed \(0<\varepsilon<1\), once \(N\) is sufficiently large,
\[
4<(4N)^\varepsilon\le4N.
\]
The complete histogram therefore gives
\[
\boxed{
\#\{(h,k)\in H_N^2:
m_{H_N}(\mathscr F(h,k))<|H_N|^\varepsilon\}
=16N^2-4N.
}
\tag{23}
\]
Thus almost all pairs are in the small fibers. The condition (4) fails for every fixed \(\kappa>0\). The cross-pairs have been counted explicitly; none is omitted or inferred from an energy estimate.

The reciprocal identity confirms the count directly:
\[
\sum_{(h,k)\in H_N^2}\frac1{m_{H_N}(\mathscr F(h,k))}
=\frac{4N}{4N}+\frac{16N^2-4N}{4}
=4N^2-N+1.
\tag{24}
\]

## E. Input exponent and arithmetic costs

Reindex by \(N=2^s\). Then
\[
|A_{2^s}|=2^{s+1}=e^{(\log2)s+O(1)},\qquad
|H_{2^s}|=2^{s+2}.
\]
In this cardinality-growth parameter, the input exponent is
\[
a=\log2.
\tag{25}
\]
The parameter \(s\) is not the field degree. With \(d_N=[L_N:\mathbb Q]=16^N\),
\[
\log|A_N|=\log(2N)=O(\log\log d_N)=o(d_N).
\tag{26}
\]
Thus this construction also fails the requested positive input exponent per field degree.

All \(h(x)\) are algebraic-integer units: they satisfy the monic equation
\[
T^4-xT^2+1=0,
\]
and \(h(x)^{-1}=xh(x)-h(x)^3\). At every real embedding \(h(x)\) is sent to one of \(\pm h(x),\pm h(x)^{-1}\); its Chebyshev value remains the rational integer \(x\).

Let \(I_N=\max_j i_j\). The complete cost ledger is:

| Quantity | Exact value or proved bound |
|--------------------------------|------------------------------------------------------------|
| Real input size | \(2N\) |
| Parameter size | \(4N\) |
| Field degree | \(16^N\) |
| Denominators | \(1\); the parameters are algebraic-integer units |
| Largest real input | \(36I_N^3+3I_N+2\) |
| All conjugate parameter magnitudes | Less than \(\sqrt{36I_N^3+3I_N+4}\) |
| Output container magnitude | At most \(8X_N^3+6X_N\), where \(X_N=\max A_N\) |
| Regulator or class-number estimates | Not used; inputs are explicitly listed |
| Root discriminant | Unbounded; lower bound below |

Every anchor is an odd ramified prime. The ramified part of a multiquadratic extension of \(\mathbb Q_p\), for odd \(p\), has ramification index at most two; here it is exactly two. The standard tame different formula gives discriminant exponent \(d_N/2\) at such a prime in this Galois extension. Therefore
\[
\operatorname{rd}(L_N)\ge
\left(\prod_{\text{anchor }p}p\right)^{1/2}.
\tag{27}
\]
For completeness, the usual compositum discriminant inequality and the bound \(|\operatorname{disc}\mathbb Q(\sqrt R)|\le4R\) give
\[
\operatorname{rd}(L_N)
\le\prod_{j=1}^N\prod_{\nu=1}^4(4R_\nu(i_j))^{1/2}.
\tag{28}
\]
These costs are not suppressed as constants. Neither the radius nor root discriminant stays fixed along this family. There is no projection ambiguity: the selected real embedding is injective on \(L_N\), and all the output equalities have already been proved over \(\mathbb Q\).

## F. Output exponent

Equation (20) gives, in the parameter \(N=2^s\),
\[
|P_3(A_{2^s},A_{2^s})|
=4\cdot 2^{2s}-2^s+1
=e^{(2\log2)s+O(1)}.
\]
Thus
\[
b=2\log2.
\tag{29}
\]
This is an exact full-image count, not merely a container upper bound.

## G. Main numerical test

Combining (25) and (29),
\[
\boxed{\Delta=2a-b=0.}
\tag{30}
\]
Also
\[
\frac{|P_3(A_N,A_N)|}{|A_N|^2}
=1-\frac{N-1}{4N^2}\longrightarrow1.
\tag{31}
\]
The normalized rich-fiber proportion vanishes, and the image is asymptotically the full square.

For comparison with the requested rate convention, bounds with unspecified \(o(s)\) terms and \(b<2a\) would justify every fixed \(c_3<2-b/a\). Equality at the boundary \(c_3=2-b/a\) requires control of those remainder terms. A safe explicit exponent would be half that gap. Here there is no positive gap to convert.

## H. Final result and status

No one of the three requested positive/closure labels has been established:

- CPSI is not proved.
- No noncircular constructive lemma with a proved positive-rate consequence has been isolated for a still-viable candidate.
- The rational Chebyshev route is not closed for all rational \(H\).

Selecting any of those labels would overstate the mathematics. In particular, proposing an unproved bound for the complete image of a newly named set, without additional reduction, would merely restate the target. For the concrete construction retained here, such a positive-rate bound is already false by (20).

The unconditional deliverable is the exact rich-fiber construction (8)--(21), its complete Cartesian histogram, and the correction (1)--(7) to the proposed FRC implication. The rational FRC conjecture itself remains unresolved. A separate amplification theorem would be needed before positive-density FRC could be used to establish CPSI.

## I. The precise next construction requirement

For the explicit family in this report, the desired next inequality
\[
\#\{(h,k)\in H_N^2:
m_{H_N}(\mathscr F(h,k))<|H_N|^\varepsilon\}
\le C|H_N|^{2-\kappa}
\qquad(\varepsilon,\kappa>0)
\tag{32}
\]
is disproved by its exact histogram; for \(\varepsilon\ge1\), failure is immediate as well. It cannot honestly be listed as a remaining constructive lemma.

Accordingly this family must be replaced before a positive results phase can continue. No new unresolved theorem about it is presented as if it could yield a power saving. The missing requirement for a replacement is (32), rather than fixed positive-density coverage.
