# Phase C4: exact higher ramified precision and the signed gate

## Decision

The requested higher-precision local count is proved exactly, in the actual
mixed-characteristic quotient. For the full inverse image of any optimal
critical input fiber,
\[
\boxed{N_1=4,\qquad N_m=22\cdot7^{3m-4}\quad(m\ge2).}
\]
Thus \(N_2=1078\), whereas the neutral count is \(1372\). The ratio
to the neutral scale is exactly \(11/14\) at every \(m\ge2\).
There is one additional saving, followed by exact stabilization of density.

The full local support is a disjoint union of **three complete cosets modulo
\(\mathfrak p^3\) and one complete coset modulo \(\mathfrak p^4\)**.
This proves a multiscale cover, including every Cartesian cross-pair.
Both that cover and the requested modulus-\(7^m\) cover fail the fully
charged global rate gate when combined with full continuous intervals and
uniform ideal-norm packing.

| Review question | Exact answer |
|---|---|
| Lifting recurrence? | \(N_2=1078\); \(N_{m+1}=343N_m\) for \(m\ge2\). |
| Does the one-level saving improve? | Yes, once: the two-input factor becomes \(22/49\), replacing \(4/7\). |
| Best gain for these full inverse images? | \(\frac13\log(49/22)\approx0.2669259483\). No universal optimum over other higher-level input subsets is claimed. |
| Signed rate at fixed \(m\ge2\)? | \(\kappa_m=\log[X^2/(D(22/49)^{1/3}(W+7^m))]<0\). |
| Can deeper levels improve this rate? | It strictly decreases for \(m\ge2\). Only \(m=2\) can improve on the old certificate. |
| Does the sharper multiscale cover help enough? | No. Its uniform full-interval envelope exceeds the actual nontrivial critical-coset population squared by more than \(3.85^d\). |
| Fixed-quartic compression proved? | No. Retire the tested local-class/full-interval route; the actual-image target remains unresolved. |

All research and calculations were offline. The analytic theorem does not
depend on finite experiments. Independent review checked the proof and
reproduced the integer verification results byte-for-byte. External novelty
and literature priority remain unchecked.

# 1. Frozen inputs and the actual local quotient

The polynomial is fixed throughout:
\[
P_4(x,y)=(x+2y)^4+3x-y.
\]
The reviewed C2-C3 state supplies a totally real cyclic cubic base field
\(F\), a unique prime \(\mathfrak p\) over 7, and a tower in which that
prime splits completely relative to the base. The local completion
\(K=F_{\mathfrak p}\) has ramification index 3 and residue degree 1.
Write \(\mathcal O\) for its valuation ring. Then
\[
7\mathcal O=\mathfrak p^3,\qquad
\mathcal O/\mathfrak p=\mathbb F_7,\qquad
|\mathcal O/\mathfrak p^r|=7^r.
\tag{1.1}
\]
Here \(\mathfrak p\) also denotes the maximal ideal of the completion.
The finite quotients agree canonically with those of the localized ring
\(\mathcal O_{F,\mathfrak p}\) in the review: completion does not change
a quotient by a fixed positive ideal power.

For \(m\ge1\), set
\[
R_m=\mathcal O/7^m\mathcal O=\mathcal O/\mathfrak p^{3m}.
\]
For \(m\ge2\), this has characteristic \(7^m\). It is not
\(\mathbb F_7[\pi]/(\pi^{3m})\). We do not extend C3's
characteristic-seven identity to characteristic zero.

Choose one \(a\in\{3,5,6\}\), and use its integer lift \(\alpha=a\).
Let
\[
\mathcal E=\alpha+\mathfrak p,\qquad
E_m=\mathcal E\bmod\mathfrak p^{3m}.
\]
Then \(a^3=-1\) in the residue field, \(E_1\) is an optimal full
critical fiber from C3, and
\[
|E_m|=7^{3m-1},\qquad |R_m|=7^{3m}.
\tag{1.2}
\]
This is exactly the requested full inverse-image family. It imposes no
additional higher-digit input restriction.

# 2. Exact Cartesian parametrization and support saturation

Put \(L=x+2y\). Since 2 is a unit, the map
\[
(x,y)\longmapsto(L,x),\qquad y=(L-x)/2,
\]
is a bijection
\[
\mathcal E^2\longleftrightarrow
(3\alpha+\mathfrak p)\times(\alpha+\mathfrak p).
\tag{2.1}
\]
Both parameters are independent. Indeed, their residues give
\(y\equiv(3a-a)/2=a\), and the converse is immediate.
The polynomial identity over \(\mathcal O\) is
\[
P_4(x,y)=g(L)+\frac72x,\qquad g(L)=L^4-\frac12L.
\tag{2.2}
\]
Consequently
\[
\boxed{
P_4(\mathcal E,\mathcal E)
=g(3\alpha+\mathfrak p)+\frac72\alpha+\mathfrak p^4.}
\tag{2.3}
\]
The final summand is the entire ideal, because
\((7/2)\mathfrak p=\mathfrak p^4\). This is equality of actual
supports, not merely an enclosing set. Every element on the right is
realized by the independent choice of \(L\) and \(x\), followed by
\(y=(L-x)/2\).

Equation (2.3) identifies the stabilization mechanism: the second input
parameter fills every higher digit beyond \(\mathfrak p^4\). It remains
to count the occupied classes at that precision.

# 3. The exact 22-class theorem

Let \(L_0=3\alpha\), \(A=6L_0^2\), \(B=4L_0\), and
\[
\omega=g(L_0)+\frac72\alpha=P_4(\alpha,\alpha).
\]
The coefficient \(A\) is a unit. Moreover,
\[
g'(L_0)=4L_0^3-\frac12\in7\mathbb Z_7\subseteq\mathfrak p^3,
\]
because \((3a)^3=1\) modulo 7. For \(u\in\mathfrak p\), Taylor's
formula therefore gives
\[
g(L_0+u)-g(L_0)\equiv Au^2+Bu^3\pmod{\mathfrak p^4}.
\tag{3.1}
\]
The linear term belongs to \(\mathfrak p^4\), and \(u^4\) also
vanishes at this precision.

Choose any uniformizer \(\pi\). Modulo \(\mathfrak p^3\), write
\(u=\pi b+\pi^2c\), with integer digit representatives
\(b,c\in\{0,\ldots,6\}\). Equation (3.1) becomes
\[
Au^2+Bu^3\equiv
A b^2\pi^2+(2Abc+Bb^3)\pi^3\pmod{\mathfrak p^4}.
\tag{3.2}
\]
This is an expansion in the actual DVR. A multiple of 7 in a coefficient
of \(\pi^2\) has valuation at least 5; in a coefficient of \(\pi^3\)
it has valuation at least 6. Reducing the displayed digits modulo 7 is
therefore legitimate, with no lost mixed-characteristic carry.

If \(b=0\), the result is zero modulo \(\mathfrak p^4\). If
\(b\ne0\), the leading digit \(Ab^2\) has exactly three nonzero
values. For each, varying \(c\) gives all seven next digits, since
\(2Ab\ne0\) in \(\mathbb F_7\). The two signs of \(b\) give
the same seven lifts; distinct leading squares cannot collide.
Thus precisely
\[
1+3\cdot7=22
\tag{3.3}
\]
classes occur modulo \(\mathfrak p^4\). In view of (2.3), every such
class is filled completely at every higher precision.

Equivalently, choose \(b_1,b_2,b_3\) so their squares are the three
distinct nonzero quadratic residues. The exact infinite support is the
disjoint union
\[
\boxed{
(\omega+\mathfrak p^4)\ \cup\
\bigcup_{i=1}^3
(\omega+A\pi^2b_i^2+\mathfrak p^3).}
\tag{3.4}
\]
The three shallow balls and the one deep ball are maximal balls inside
this support: their parent balls contain omitted residue classes. Formula
(3.4) is the promised smaller multiscale output cover. Its centers depend
on the chosen local field and fiber; the counts do not.

Reducing an integral polynomial commutes with reduction of its inputs, and
\(\mathcal E\to E_m\) is onto. Consequently the image computed here
is exactly the finite Cartesian image, with no additional liftability
assumption. Modulo \(\mathfrak p^3\), (3.4) has four classes. At every
\(m\ge2\), each of the 22 classes modulo \(\mathfrak p^4\) has
\(7^{3m-4}\) refinements. We have proved:

**Theorem 3.1.** For the actual source local cubic, all three critical
input fibers, and every \(m\ge1\),
\[
\boxed{N_1=4,\qquad N_m=22\cdot7^{3m-4}\quad(m\ge2).}
\tag{3.5}
\]
The proof needs only (1.1), so no unchosen local-field isomorphism class
enters the conclusion.

# 4. Recurrence and both input costs

At the first lift, the central class has 49 descendants modulo
\(\mathfrak p^6\), while each of the other three has 343. Hence
\[
N_2=49+3\cdot343=1078,\qquad
N_{m+1}=343N_m\quad(m\ge2).
\tag{4.1}
\]
The first lift is nonuniform; subsequent lifts are uniform because the
support is already saturated by \(\mathfrak p^4\).

| Precision | Exact image count | Neutral count | Ratio |
|---|---:|---:|---:|
| \(m=1\) | 4 | 4 | 1 |
| \(m=2\) | 1078 | 1372 | \(11/14\) |
| \(m=3\) | 369754 | 470596 | \(11/14\) |
| \(m\ge2\) | \(22\cdot7^{3m-4}\) | \(4\cdot7^{3m-3}\) | \(11/14\) |

The one-input fraction is always \(1/7\). Charging its square gives
\[
\Psi_m:=\frac{N_m/|R_m|}{(|E_m|/|R_m|)^2}
=\begin{cases}4/7,&m=1,\\22/49,&m\ge2.\end{cases}
\tag{4.2}
\]
The per-degree gain over independent cubic factors is therefore
\[
\gamma_m=-\frac13\log\Psi_m
=\begin{cases}
\frac13\log(7/4),&m=1,\\
\frac13\log(49/22),&m\ge2.
\end{cases}
\tag{4.3}
\]
The latter is approximately \(0.2669259483\); the additional gain is
exactly \(\frac13\log(14/11)\approx0.0803873523\).
These are finite-quotient proportions. They do not assert lattice
equidistribution. They are also not an optimization theorem over arbitrary
subsets of the higher rings.

# 5. Fixed carrier and the requested signed gate

Retain C3's \(Q=1\) tower, with degree \(d=d_j\), root discriminant
\(D\ge7^{2/3}\), and
\[
7\mathcal O_{F_j}=\prod_{k=1}^{d/3}\mathfrak P_{j,k}^{3},
\qquad \mathfrak I_j=\prod_{k=1}^{d/3}\mathfrak P_{j,k}.
\]
Each local completion is the original source cubic, since the base prime
splits completely in every relative layer. Use the explicit same-input
carrier
\[
C_j=-1+\{u\in\mathfrak I_j:
|\sigma_i(u)|\le X\text{ for every real embedding }i\}.
\tag{5.1}
\]
Its reduction is contained in the full critical inverse image at every
factor. No surjectivity of this bounded carrier onto the local inputs is
assumed or needed for an output upper bound.

The reviewed ideal-lattice translate-and-difference proof gives
\[
|C_j|\ge e^{ad},\qquad
a=\log X-\frac13\log7-\frac12\log D.
\tag{5.2}
\]
Take \(X=2\,7^{1/3}\sqrt D\), fixed before the degree limit, so
\(a=\log2>0\). On the corresponding interval
\([-1-X,-1+X]\), C3 proved the exact continuous width
\[
W=81(X+1)^4+\frac32X+\frac{27}{16}.
\tag{5.3}
\]
All image points lie in the product of these intervals over the embeddings.

CRT and (3.5) give at most \(N_m^{d/3}\) occupied classes modulo
\(7^m\mathcal O_{F_j}\). A nonzero difference in one such class is
\(7^m\)-separated in sup norm, by the algebraic-integer norm. Cubes
of side length \(7^m\) therefore give the full-support certificate
\[
|P_4(C_j,C_j)|\le U_m
=N_m^{d/3}(1+W/7^m)^d=e^{c_m d}.
\tag{5.4}
\]
This uses every occupied class, every pair, and the actual spacing at
precision \(7^m\). There are no exceptional outputs.

For \(m\ge2\), set \(C_*=(22/49)^{1/3}\). The exact exponents are
\[
c_m=\frac13\log22-\frac43\log7+\log(W+7^m),
\]
\[
\boxed{\kappa_m=2a-c_m
=\log\frac{X^2}{D C_*(W+7^m)}.}
\tag{5.5}
\]
At fixed \(X,D,W\), this strictly decreases with \(m\ge2\).
The neutral leading growth cancels, but the additive packing term
\(7^m\) remains and worsens with precision.

For every center \(b\) and radius \(r\), the diagonal identity
\[
\frac{P_4(b+r,b+r)+P_4(b-r,b-r)}2-P_4(b,b)
=486b^2r^2+81r^4
\]
implies \(W(b,r)\ge81r^4\). Hence
\[
\frac{W+7^m}{X^2}\ge81X^2+\frac{7^m}{X^2}
\ge18\,7^{m/2}.
\]
Substitution into (5.5) proves the uniform signed bound
\[
\boxed{\kappa_m\le-\log(18D C_*7^{m/2})
\le-\log(126D C_*)<0\qquad(m\ge2).}
\tag{5.6}
\]
The accepted \(m=1\) certificate is also negative. Thus no fixed
rational-prime precision passes the gate. The exact threshold for a
positive rate would be \(W+7^m<X^2/(D C_*)\), and (5.6) disproves
it throughout the evaluated carrier family.

Level two can still improve a negative level-one estimate. Precisely,
\[
\kappa_2-\kappa_1
=\frac13\log\frac{14}{11}+\log\frac{W+7}{W+49}.
\tag{5.7}
\]
It is positive when \(W>(49-7q)/(q-1)\), where
\(q=(14/11)^{1/3}\); that threshold is approximately 494.752.
The explicit growth range has \(X>7/2\) and
\(W>81(9/2)^4\), so the improvement does occur there. It remains
insufficient for a positive rate. Among the requested levels, \(m=2\)
is the best certificate for this carrier.

## 5.1 Complete signed ledger

| Term | Contribution to \(\kappa_m\), \(m\ge2\) |
|---|---|
| Two input windows | \(+2\log X\) |
| Both ideal restrictions | \(-\frac23\log7\) |
| Discriminant | \(-\log D\) |
| Exact occupied classes | \(-\frac13\log N_m\) |
| Uniform per-class packing | \(-\log(1+W/7^m)\) |
| Units, regulator, sign selection | 0: no unit carrier or sign selection |
| Translation | Included in the exact width (5.3) |
| Multiplicity, ratio union, exceptional pieces | 0: direct additive carrier; no omitted outputs |
| Fixed real embedding | 0: injective |

The first five entries sum exactly to (5.5). The exponent \(c_m\) is
that of a proved upper certificate; it is not the unknown actual-image
exponent. The base field, tower construction, polynomial, local pattern,
and radius are fixed; only the tower layer and degree vary with \(j\).

# 6. Audit of the smaller ideal and multiscale covers

Rational modulus 49 is not the finest natural description of (3.4).
We audit both sharper covers explicitly before stopping the route.

## 6.1 Twenty-two classes at the saturation ideal

There are \(22^{d/3}\) classes modulo \(\mathfrak I_j^4\).
This ideal has norm \(7^{4d/3}\), giving sup-norm separation
\(7^{4/3}\). Thus the sharper envelope is
\[
U_{\mathfrak I^4}=22^{d/3}(1+W/7^{4/3})^d.
\]
Its signed rate is
\[
\kappa_{\mathfrak I^4}
=\log\frac{X^2}{D C_*(W+7^{4/3})}
\le-\log(18\,22^{1/3}D)<0.
\tag{6.1}
\]
The last bound again uses the diagonal width and AM-GM.

## 6.2 Exact mixed-depth ideal-ball cover

Let \(n=d/3\). In (3.4), each local factor chooses either one of
three shallow \(\mathfrak p^3\)-cosets or the single deep
\(\mathfrak p^4\)-coset. Choosing the deep option at exactly \(k\)
factors gives \(\binom nk3^{n-k}\) global cosets of a mixed ideal
with norm \(7^{d+k}\). Its norm separation is \(7^{1+k/d}\).
The exact local product support is covered by the resulting envelope
\[
\boxed{
U_{\mathrm{mix}}=
\sum_{k=0}^{n}\binom nk3^{n-k}
\left(1+\frac{W}{7^{1+k/d}}\right)^d.}
\tag{6.2}
\]
The branch count, mixed-ideal spacing, and sum over all branches are paid.
No branch-dependent reduction of the real width is assumed.

Its exponential rate exists and can be written
\[
c_{\mathrm{mix}}=
\max_{0\le\theta\le1}
\left\{
\frac{H(\theta)+(1-\theta)\log3}{3}
+\log(1+W/7^{1+\theta/3})
\right\},
\tag{6.3}
\]
where \(H(\theta)=-\theta\log\theta-(1-\theta)\log(1-\theta)\),
with the usual zero endpoint convention. This follows from the binomial
coefficient estimate and a sum of only \(n+1\) terms; its logarithmic
error is \(o(d)\).

The all-shallow term \(k=0\) alone proves
\[
c_{\mathrm{mix}}\ge\tfrac13\log3+\log(1+W/7),
\]
and therefore
\[
\boxed{
2a-c_{\mathrm{mix}}
\le-\log\left[18\sqrt7\,D(3/7)^{1/3}\right]<0.}
\tag{6.4}
\]
Even the actual smaller multiscale support, used with full continuous
intervals and uniform ideal packing, does not pass the rate gate.

## 6.3 Volume budgets and actual populations are separate

For an equal-radius window of radius \(r\), the more favorable periodic
volume input budget is
\[
L=7^{-d/3}(2r)^dD^{-d/2}.
\]
Translation averaging proves that some translate attains at least this
budget; it does not assert uniformity for every prescribed center.
The modulus-\(7^m\) certificate normalized by \(L^2\) has factor
\[
D C_*\frac{W+7^m}{4r^2}
\ge\frac92D C_*7^{m/2}>1\qquad(m\ge2).
\]
The \(\mathfrak I^4\) version is at least
\(\frac92\,22^{1/3}D>1\); the mixed cover already has factor at
least \(\frac{9\sqrt7}{2}D(3/7)^{1/3}>1\) from its all-shallow
term. These ratios use \(L\), not the actual population.

There is also a direct actual-population obstruction in equal-radius
critical-coset windows. Put \(t=7^{1/3}\). Ideal norm separation gives
\[
|C|\le(1+2r/t)^d.
\]
If \(|C|>1\), then \(z=2r/t\ge1\). Using the all-shallow term
of (6.2) and \(W\ge81r^4\),
\[
\frac{U_{\mathrm{mix}}}{|C|^2}
\ge\left[
3^{1/3}\frac{1+(81t/16)z^4}{(1+z)^2}
\right]^d
\ge\left[
\frac{3^{1/3}(1+81t/16)}4
\right]^d>3.85^d.
\tag{6.5}
\]
The function \((1+Kz^4)/(1+z)^2\) is increasing for \(z\ge1\)
when \(K=81t/16>1\): after removing positive factors its derivative
has numerator \(2Kz^4+4Kz^3-2>0\). This proves the second inequality.
Similarly, direct saturation-ideal packing satisfies
\[
\frac{U_{\mathfrak I^4}}{|C|^2}
\ge\left[\frac{97\,22^{1/3}}{64}\right]^d>4.24^d.
\tag{6.6}
\]
These are lower bounds for the numerical envelopes. They are not lower
bounds for \(|P_4(C,C)|\). A smaller realized real support inside a
local class remains outside the statements.

## 6.4 Arbitrary ideal-coset covers of the full local support

There is a stronger scoped check that also permits coarser or overlapping
covers. Let \(S\) be the entire product of the local supports (3.4) at
the \(d/3\) ramified factors. Suppose finitely many congruence classes
defined by integral ideals \(J_\ell\), supported only at primes over 7
and viewed in the local completions, cover \(S\).
Refine them all to a common sufficiently deep finite quotient. The fraction
occupied by \(S\) is \((22/7^4)^{d/3}\), and the fraction occupied
by a \(J_\ell\)-coset is \(1/N(J_\ell)\). Subadditivity gives
\[
\sum_\ell\frac1{N(J_\ell)}\ge(22/7^4)^{d/3}.
\]
Therefore their uniform full-interval packing envelope satisfies
\[
U_{\mathrm{cover}}=
\sum_\ell(1+W/N(J_\ell)^{1/d})^d
\ge W^d(22/7^4)^{d/3}.
\tag{6.7}
\]
For the actual equal-radius critical-coset input population above, with
\(|C|>1\) and \(z\ge1\), this implies
\[
\frac{U_{\mathrm{cover}}}{|C|^2}
\ge\left[\frac{81\,22^{1/3}z^4}{16(1+z)^2}\right]^d
\ge\left[\frac{81\,22^{1/3}}{64}\right]^d>3.54^d.
\tag{6.8}
\]
The function \(z^4/(1+z)^2\) increases for \(z>0\), proving the
last step. Thus changing only the ideal-coset cover of the entire local
product support cannot rescue this interval-packing method. The hypothesis
that the cover contains the entire \(S\) is essential: a much smaller
set of residues actually realized by a special finite global carrier, or
a smaller real region inside each class, is not excluded.

# 7. Exact checks and independent review

The accompanying standard-library Python script works in the explicit
mixed-characteristic models
\[
(\mathbb Z/7^m\mathbb Z)[\pi]/(\pi^3-7u),
\qquad u\in\{1,2,4\}.
\]
These represent the three tame ramified cyclic cubic possibilities; the
model note supplies the local algebra justification. The analytic proof
above does not require that classification or any particular presentation.

The script checks all nine combinations of those twists and the three
critical input residues. It evaluates all 21,609 ordered input pairs at
modulus 7, all 151,263 allowed \(L\)-values at modulus 49 across those
cases, and 1,197 further comparisons with the original polynomial identity.
At levels two and three it constructs exactly 1,078 and 369,754 actual
outputs per model from valid input pairs. The analytic saturation theorem
supplies the general upper support bound; a full Cartesian enumeration at
modulus 343 is not claimed.

Run from the project root:

```sh
python3 phase_c4/higher_precision_check.py --output phase_c4/reproduced_results.json
cmp phase_c4/higher_precision_results.json phase_c4/reproduced_results.json
```

An independent referee reran the complete script and obtained byte-identical
results, checked both analytic derivations and the global estimates, and
audited the precise support and population scopes. The proof, code, results,
and referee report are supplied together for separate external inspection.

# 8. Fixed choices, preserved claims, and stop

Choose the source base with the established one-Frobenius
Golod-Shafarevich margin, fix its tower and \(D\), choose the critical
fiber and \(X=2\,7^{1/3}\sqrt D\), and choose a fixed precision or
the exact finite multiscale partition. Only then let \(j\to\infty\).
No polynomial coefficient, local input pattern, or radius varies with the
degree. Units, regulators, and hybrid ratio decompositions are not used.

The seven C2 precision changes are applied, and C3 is frozen with its
narrowed modulus-7/full-interval headline. C4 proves an additional local
theorem for the specified full inverse images; it does not reopen the
solved subset optimization in \(R_1\).

The extra higher-level local gain is real but insufficient. Retire this
tested arithmetic route: full critical inverse images, their exact local
class or maximal-ball covers, full continuous output intervals, and the
stated uniform packing and input counts. No unrestricted carrier search or
abstract hybrid-overlap claim is started. A different polynomial mechanism,
or a proved smaller realized-support region with quantified cross-support
overlap, would require a new argument. The actual fixed-quartic compression
target remains unresolved, and no external novelty claim is made.

**HIGHER-PRECISION LOCAL COUNT PROVED; FULL-INTERVAL CLASS-PACKING ROUTE RETIRED WITHIN THE STATED SCOPE.**
