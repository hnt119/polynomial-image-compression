# Independent referee report: higher ramified precision

## Scope and disposition

The local lifting theorem is **ACCEPTED**. Its proof works in the actual mixed-characteristic ring of integers of every totally ramified cubic extension of \(\mathbb Q_7\), with residue field \(\mathbb F_7\). It uses the full Cartesian product of the specified critical ball. No enumeration, external retrieval, or equal-characteristic substitution is required.

The fully charged full-interval class-packing certificates considered below are **NEGATIVE**. This is a statement about those upper-bound certificates, not a lower bound on the actual polynomial image. Fixed-quartic compression remains **UNRESOLVED**. The numerical record has been independently reproduced, and the assembled main report has been checked in full, including its general ideal-cover lemma.

## 1. Independent derivation of the exact support

Let \(\mathcal O\) be the local ring of integers, with maximal ideal \(\mathfrak p\), residue field \(\mathbb F_7\), and \(7\mathcal O=\mathfrak p^3\). Fix a lift \(a\in\mathcal O\) with \(\bar a^3=-1\), and let \(B=a+\mathfrak p\). Set

\[
P_4(x,y)=(x+2y)^4+3x-y.
\]

The coordinate transformation \((x,y)\mapsto(x,t=x+2y)\) is a bijection

\[
B\times B\longrightarrow (a+\mathfrak p)\times(3a+\mathfrak p),
\]

because \(2\) is a unit. Thus the two variables on the right are independent, and

\[
P_4(x,y)=G(t)+\frac72x,
\qquad G(t)=t^4-\frac12t.
\]

Consequently the exact image, before quotienting, is

\[
P_4(B,B)=G(3a+\mathfrak p)+\frac72a+\mathfrak p^4. \tag{R1}
\]

The equality \((7/2)\mathfrak p=\mathfrak p^4\) is an equality of actual mixed-characteristic ideals. Treating \(7\) as zero at higher precision would destroy this term and would give the wrong lifting calculation.

There is a unique \(b\in3a+\mathfrak p\) with \(G'(b)=0\): the residue is critical and \(G''(b)=12b^2\) is a unit, so Hensel lifting applies. For \(u\in\mathfrak p\),

\[
G(b+u)-G(b)
=6b^2u^2\left(1+\frac{2u}{3b}+\frac{u^2}{6b^2}\right).
\]

The expression in parentheses belongs to \(1+\mathfrak p\), and has its unique square root congruent to \(1\). The change of variable

\[
v=u\sqrt{1+\frac{2u}{3b}+\frac{u^2}{6b^2}}
\]

is a bijection of \(\mathfrak p\). One way to check surjectivity as well as injectivity is to use its integral formal power series: its linear coefficient is \(1\), it has an integral inverse power series, and both series converge on \(\mathfrak p\). Hence

\[
P_4(B,B)=c+6b^2\{v^2:v\in\mathfrak p\}+\mathfrak p^4,
\qquad c=G(b)+\frac72a. \tag{R2}
\]

This proves both inclusion directions and the full Cartesian support assertion. It is independent of a choice of Eisenstein polynomial or tame unit in the equation relating a uniformizer to \(7\).

## 2. Exact counts and equality of lifting scales

Modulo \(\mathfrak p^4\), the square set in (R2) consists of zero and 21 classes of valuation exactly two. Indeed, writing \(v=\pi w\) with \(w\) a unit identifies its nonzero classes with unit squares modulo \(\mathfrak p^2\). That unit group has order \(6\cdot7=42\), and its squaring map has kernel of order two. There are therefore exactly 21 such classes, plus zero.

Modulo \(\mathfrak p^3=7\mathcal O\), there are three nonzero square classes of valuation two, plus zero. Reducing the exact support (R2) modulo \(7^m\mathcal O=\mathfrak p^{3m}\) gives

\[
N_1=4,\qquad
N_m=22\,7^{3m-4}\quad(m\ge2). \tag{R3}
\]

Every residue-class pair modulo \(7^m\) lifts to a pair in \(B\times B\), so reduction of (R2) is exactly the finite-ring image, not merely a containing set.

Thus

\[
N_2=1078,\qquad N_{m+1}=343N_m\quad(m\ge2),
\qquad
\frac{N_m}{4\,7^{3(m-1)}}=\frac{11}{14}\quad(m\ge2).
\]

The first higher-precision step improves the neutral density by \(11/14\). Every subsequent step is exactly neutral. Since \(|E_m|=7^{3m-1}\), the natural input-costed factor is

\[
\frac{7^{3m}N_m}{|E_m|^2}
=\frac{22}{49}\quad(m\ge2),
\]

and its corresponding gain is \(\tfrac13\log(49/22)\approx0.2669259483\). This statement concerns this specified inverse-image carrier. It is not a universal minimization theorem for all subsets at higher precision.

## 3. Signed audit of the requested integer-modulus certificate

For the explicit C3 critical-ideal carrier, retain the proved input lower rate

\[
a=\log X-\tfrac13\log7-\tfrac12\log D.
\]

The exact local counts give, for \(m\ge2\),

\[
\kappa_m
=\log\frac{X^2}
{D(22/49)^{1/3}(W+7^m)}. \tag{R4}
\]

For a full continuous interval, the elementary diagonal estimate is \(W\ge81X^4\). Therefore

\[
\frac{W+7^m}{X^2}
\ge18\,7^{m/2},
\qquad
\kappa_m\le-\log\bigl(18\,7^{m/2}D(22/49)^{1/3}\bigr)<0.
\]

Already at \(m=2\), the quantity inside the logarithm is approximately \(96.48195D>1\). At each fixed \(X,W,D\), the rates strictly decrease with \(m\ge2\), so testing infinitely many higher fixed powers is unnecessary after the exact recurrence is proved.

For the separate volume-density input count on an equal-radius box, the corresponding normalized factor is

\[
\Theta_m
=D(22/49)^{1/3}\frac{W+7^m}{4r^2}
\ge\frac92\,7^{m/2}D(22/49)^{1/3}>1.
\]

These two displays use different input lower bounds, with the expected factor of four between them. Neither may be interpreted as a lower bound for the actual polynomial-image ratio.

## 4. The sharper ideal-modulus cover must also be checked

The support theorem itself gives 22 classes modulo \(\mathfrak p^4\), which is sharper than simply listing all their refinements modulo \(7^m\). Globally put \(I=\prod_k\mathfrak p_k\), so \(\operatorname{N}(I^4)=7^{4d/3}\). Nonzero differences in \(I^4\) have Minkowski sup norm at least \(7^{4/3}\). Thus the natural full-interval envelope is

\[
U_{I^4}=22^{d/3}\left(1+\frac{W}{7^{4/3}}\right)^d.
\]

Using the volume-density input normalization, its factor satisfies

\[
\Theta_{I^4}
=D(22/49)^{1/3}\frac{W+7^{4/3}}{4r^2}
\ge\frac92\,22^{1/3}D
\approx12.60918D>1. \tag{R5}
\]

The inequality follows directly from \(W\ge81r^4\) and the arithmetic-geometric mean inequality. Hence this obvious support-based improvement does not rescue the specified certificate either.

A stronger statement about the *envelope divided by actual input size* is available for equal-radius carriers contained in one critical ideal coset. Let \(t=7^{1/3}\). Such inputs are \(t\)-separated, so

\[
|C|\le(1+2r/t)^d.
\]

If \(2r<t\), the carrier has at most one point. Otherwise set \(z=2r/t\ge1\). Then

\[
\frac{U_{I^4}}{|C|^2}
\ge\left[
22^{1/3}\frac{1+81z^4/16}{(1+z)^2}
\right]^d
\ge\left[22^{1/3}\frac{97}{64}\right]^d
>4.2468^d. \tag{R6}
\]

For the last step, differentiating \((1+Bz^4)/(1+z)^2\), with \(B=81/16\), leaves a positive numerator proportional to \(Bz^3(z+2)-1\) for \(z\ge1\). The bound remains about the displayed full-interval envelope, even though the denominator in (R6) is the actual input size.

## 5. Required limitations of the conclusion

Before stating the limitations, a sharper exact multiscale cover also deserves an explicit audit. In (R2), the valuation-two square values comprise three complete \(\mathfrak p^3\)-cosets, since a unit is a square exactly when its residue is a square. The remaining values form one \(\mathfrak p^4\)-coset. These four balls are pairwise disjoint and maximal in the local image. Thus the local support partition has three shallow balls and one deep ball.

With \(n=d/3\) local factors, choosing the deep ball in exactly \(k\) factors gives \(\binom nk3^{n-k}\) global cosets of a mixed ideal of norm \(7^{d+k}\). Its norm-based spacing is \(7^{1+k/d}\). The exact support partition therefore gives the full-interval envelope

\[
U_{\mathrm{mix}}
=\sum_{k=0}^{n}\binom nk3^{n-k}
\left(1+\frac{W}{7^{1+k/d}}\right)^d. \tag{R7}
\]

This is generally sharper than replacing every shallow ball by its seven refinements modulo \(\mathfrak p^4\). Nevertheless its \(k=0\) term alone is

\[
3^{d/3}(1+W/7)^d.
\]

Against the explicit C3 input lower count, the corresponding certificate factor is at least

\[
D(3/7)^{1/3}\frac{W+7}{X^2}
\ge18\sqrt7\,D(3/7)^{1/3}
\approx35.90563D>1. \tag{R8}
\]

The volume-density normalization has the same expression divided by four, which is still greater than one. Against actual input size, the separation argument from Section 4 gives

\[
\frac{U_{\mathrm{mix}}}{|C|^2}
\ge\left[
3^{1/3}\frac{1+81\,7^{1/3}z^4/16}{(1+z)^2}
\right]^d
\ge\left[
\frac{3^{1/3}}4\left(1+\frac{81\,7^{1/3}}{16}\right)
\right]^d
>3.8523^d. \tag{R9}
\]

Here \(z=2r/7^{1/3}\ge1\), and the same one-variable derivative check proves the displayed minimum occurs at \(z=1\). This closes the obvious maximal-ball multiscale refinement of the full-interval certificate. It does not establish an impossibility theorem for every conceivable multiscale cover or every finer archimedean support estimate.

There is also a direct bound for any finite cover of the **entire local product support** by congruence classes defined by ideals supported above seven. Each class is viewed in the product of the local completions, rather than as a discrete subset of the global field. Let \(S\) denote that support in the product of the \(d/3\) local rings. Give this product normalized additive measure. By the exact local theorem,

\[
\mu(S)=(22/7^4)^{d/3}.
\]

If \(S\subseteq\bigcup_\ell(a_\ell+J_\ell)\), where each \(J_\ell\) is supported above seven, then finite subadditivity gives

\[
\sum_\ell\operatorname{N}(J_\ell)^{-1}\ge\mu(S).
\]

This is also an elementary finite-residue count: refine all the cosets to a common sufficiently deep product quotient and count. The associated full-interval, norm-spacing envelope therefore satisfies

\[
U_{\mathrm{cover}}
:=\sum_\ell\left(1+\frac{W}{\operatorname{N}(J_\ell)^{1/d}}\right)^d
\ge W^d\mu(S). \tag{R10}
\]

For an actual critical-coset input carrier with at least two points in an equal-radius box, retain \(z=2r/7^{1/3}\ge1\), the bound \(|C|\le(1+z)^d\), and \(W\ge81r^4\). They give

\[
\frac{U_{\mathrm{cover}}}{|C|^2}
\ge\left[
\frac{81\,22^{1/3}z^4}{16(1+z)^2}
\right]^d
\ge\left[\frac{81\,22^{1/3}}{64}\right]^d
>3.5463^d. \tag{R11}
\]

The function \(z^4/(1+z)^2\) is increasing for positive \(z\). This result permits refinement, coarsening, overlap, and different ideal depths in different local factors. Its scope remains strict: the cosets must cover the *entire* permitted local product support, and every class receives the full-interval norm-spacing population bound. A cover of only the finite globally realized outputs, or a smaller archimedean population estimate inside a class, is not covered by (R10)-(R11).

The resulting limitations are:

1. The exact local support is saturated modulo \(\mathfrak p^4\). No further local-density gain exists for this **full inverse image of one critical fiber**.
2. No universal higher-precision subset optimization is proved here.
3. The global conclusions retain a full continuous interval inside every occupied congruence class. They do not exclude a substantially smaller proved archimedean realized-support region.
4. Local equality in (R2) for the complete \(7\)-adic ball does not imply every allowed residue class is realized by a particular finite global carrier.
5. No lower bound for \(|P_4(A,A)|\) for arbitrary real sets is obtained.
6. External novelty is unchecked; this audit was entirely offline.

## 6. Review status

The independent analytic derivation and signed calculations above are complete. I also read the independent lifting note, the mixed-characteristic model note, and the complete Python script. The two coordinate normal forms use different univariate polynomials, \(t^4-t/2\) and \(t^4+2t/3\), but each follows from its own invertible Cartesian coordinate change and each retains the entire transverse \(\mathfrak p^4\) term. Their identical counts are consistent.

I independently reran `higher_precision_check.py` and obtained a byte-for-byte identical JSON record. It covers nine twist/critical-residue combinations. The verification scopes are accurately distinguished: exhaustive Cartesian pairs modulo seven; exhaustive admissible \(t\)-coordinates plus the proved saturation modulo 49; explicit output construction plus the analytic upper bound modulo 343. It is not represented as an exhaustive higher-precision Cartesian enumeration.

- Script SHA-256: `9193e2ce67c32ff063f54219f39a5c03102942226ceccdca6ca4f0113f10a20a`.
- Result SHA-256: `21ce5b48f0e4ce62a98ee9a1b1a0396b955e97c89fc5abde83fd41a30b3ac5fb`.

I read the assembled main report `Phase_C4_Higher_Ramified_Precision.md` in full. Its direct Taylor expansion is a separate elementary proof of the 22-class count; its explicit support formula correctly uses the diagonal value as center, because the discarded derivative term begins at valuation four. Its finite mixed-cover expression, entropy limit, and signed rate bounds are correct. The entropy limit follows from uniform binomial coefficient estimates and maximization over a grid in a compact interval, with an error of order \(\log d/d\).

I also checked the main report's general ideal-cover lemma against (R10)-(R11). Its hypothesis that the cover contains the entire permitted local product support is retained explicitly. This lemma does not turn a numerical packing envelope into a lower bound for the actual image.

Three wording refinements were requested during review: specify that the selected digits have the three distinct nonzero quadratic residues as their squares; distinguish fixed base/tower parameters from varying extension layers; and view global-ideal congruence classes in the local completions when covering the full local product support. These do not alter any proved formula.

**Final disposition: ACCEPT the exact higher-precision local theorem and the signed full-interval certificate audit, within their stated scopes. No mathematical or computational objection remains.**
