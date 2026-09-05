# Final constructive push for \(Q(x,y)=x^2+xy+y^2\)

## Status and main conclusion

All work in this report is offline. The frozen results in the prompt are used as hypotheses and are not re-proved.

I did **not** obtain a set satisfying

\[
|Q(A,A)|\le |A|^{2-c}
\]

with a fixed \(c>0\). The strongest new constructive reduction is nevertheless quite sharp:

> **Balanced four-state norm-code theorem.** There is an explicit sequence of integer sets \(A_m\) and explicit subsets \(G_m\subseteq A_m^2\) such that
> \[
> |G_m|=4^m,\qquad |Q(G_m)|=3^m,
> \]
> and, for every fixed \(0<\varepsilon<1/2\), outside a fraction at most \(e^{-2\varepsilon^2m}\) of \(G_m\), every represented value has at least
> \[
> 2^{(1/2-\varepsilon)m}
> \]
> representations in \(A_m^2\). The construction realizes the split-prime allocations as actual coefficient pairs; it is not an energy argument.

The unresolved issue for this realized-fiber certificate is whether the coefficient projections can be made almost maximally reusable. If

\[
\boxed{
|A_m|^2-4^m\le |A_m|^{2-\xi_0}
}
\tag{CR}
\]

for some fixed \(\xi_0>0\), then the same construction gives

\[
|Q(A_m,A_m)|
\le 3^m+|A_m|^{2-\xi_0}
\le |A_m|^{2-c}
\]

for every fixed

\[
0<c<\min\{2-\log_2 3,\xi_0\}.
\]

Thus the numerical exponent available from the norm code itself is

\[
\boxed{2-\log_2 3=0.415037\ldots.}
\]

No theorem currently proves (CR), and the known data do not justify asserting it.

## Standard results used

The following are the only substantial standard results assumed.

1. **Arithmetic of the Eisenstein integers.** For \(E=\mathbb Z[\omega]\), \(\omega^2+\omega+1=0\), the norm
   \[
   N(a-\omega b)=a^2+ab+b^2
   \]
   is Euclidean. Hence \(E\) is a unique-factorization domain. A rational prime \(q\ne3\) splits as \(q=\pi\bar\pi\) in \(E\) precisely when \(q\equiv1\pmod3\), and it remains prime precisely when \(q\equiv2\pmod3\).

2. **Dirichlet's theorem in the two progressions used here.** Each reduced residue class modulo \(3\) contains infinitely many rational primes. Only the cases \(1\pmod3\) and \(2\pmod3\) are required. This is used solely to choose two disjoint explicit increasing prime sequences.

3. **Hoeffding's inequality.** If \(X_1,\ldots,X_m\) are independent random variables in \([0,1]\), then
   \[
   \Pr\!\left(\sum_iX_i-\mathbb E\sum_iX_i\le-t\right)
   \le e^{-2t^2/m}.
   \]

4. **The \(C_4\)-free bipartite bound.** A bipartite graph whose two vertex classes each have at most \(n\) vertices and which contains no nondegenerate four-cycle has at most
   \[
   n^{3/2}+n
   \]
   edges. This is the elementary balanced form of the Kővári--Sós--Turán bound used in the additive-carrier discussion.

No class-number estimate, Chebotarev theorem, lattice-point asymptotic, or internet-sourced assertion is needed for the main construction.

## A. Best construction found

Let \(q_i\) be the \(i\)-th rational prime congruent to \(1\pmod3\), and let \(r_i\) be the \(i\)-th rational prime congruent to \(2\pmod3\), with the two sequences chosen disjoint. Fix once and for all a factorization

\[
q_i=\pi_i\bar\pi_i
\]

in \(E\). Define the four-state local alphabet

\[
\mathcal S_i=\{1,r_i,\pi_i,\bar\pi_i\}
\]

and the multiplicative code

\[
Z_m=
\left\{
\prod_{i=1}^m\theta_i:\theta_i\in\mathcal S_i
\right\}.
\tag{1}
\]

Every \(z\in E\) has a unique expression

\[
z=a_z-\omega b_z,
\qquad a_z,b_z\in\mathbb Z.
\]

Set

\[
A_m=\{a_z:z\in Z_m\}\cup\{b_z:z\in Z_m\}
\subset\mathbb Z\subset\mathbb R
\tag{2}
\]

and

\[
G_m=\{(a_z,b_z):z\in Z_m\}\subseteq A_m^2.
\tag{3}
\]

The state \(r_i\) is deliberately separated from the split prime \(q_i\). It supplies a second non-split orientation state without forcing every engineered norm to be divisible by \(q_i\). This is the smallest four-state balance that survives the elementary maximum-shell and one-prime marginal tests described below.

## B. Why the construction is Cartesian

Equation (2) places **both** coefficients of every generated Eisenstein integer in one and the same set \(A_m\). Thus, literally,

\[
z=a_z-\omega b_z\in A_m-\omega A_m,
\]

and (3) is an actual subset of the Cartesian square \(A_m^2\). There is no replacement of \(A_m-\omega A_m\) by a convenient non-Cartesian set.

The map

\[
z\longmapsto(a_z,b_z)
\]

is injective because \(1,\omega\) are linearly independent over \(\mathbb Q\). Unique factorization gives distinctness of all products in (1): the exponent of the inert Eisenstein prime \(r_i\) records whether the state is \(r_i\), while the valuations at \(\pi_i\) and \(\bar\pi_i\) distinguish the other two nontrivial states. Consequently

\[
\boxed{|Z_m|=|G_m|=4^m.}
\tag{4}
\]

In particular,

\[
2^m\le |A_m|\le2\cdot4^m.
\tag{5}
\]

The lower bound follows already from \(|G_m|\le|A_m|^2\); the upper bound counts the two displayed coefficients of each element. Hence \(|A_m|\to\infty\), with no denominator or embedding issue.

## C. Pair coverage

For a state vector \(\boldsymbol\theta=(\theta_1,\ldots,\theta_m)\), define

\[
I(\boldsymbol\theta)
=
\{i:\theta_i\in\{\pi_i,\bar\pi_i\}\}.
\]

The corresponding rational norm is

\[
N(z)
=
\prod_{\theta_i=r_i}r_i^2
\prod_{i\in I(\boldsymbol\theta)}q_i.
\tag{6}
\]

Distinct choices, for each \(i\), among the three labels

\[
1,\qquad r_i^2,\qquad q_i
\]

give distinct integers. Therefore

\[
\boxed{|N(Z_m)|=3^m.}
\tag{7}
\]

At present the rigorously controlled portion of the Cartesian square is precisely \(G_m\):

\[
|G_m|=4^m,
\qquad
|A_m^2\setminus G_m|=|A_m|^2-4^m.
\tag{8}
\]

No power-saving upper bound for the second quantity is known. This is not suppressed as a lower-order term.

## D. Actual fiber multiplicity

Fix the three-way norm label at every coordinate. If coordinate \(i\) has norm label \(q_i\), either \(\pi_i\) or \(\bar\pi_i\) may be chosen; the other two labels have one choice. Unique factorization shows that all of these elements are distinct. Hence the norm in (6) has exactly

\[
2^{|I(\boldsymbol\theta)|}
\tag{9}
\]

representations inside \(G_m\). In particular,

\[
r_{A_m}(N(z))\ge2^{|I(\boldsymbol\theta)|}.
\tag{10}
\]

This is realized multiplicity, not a count of merely possible ideal allocations. For every active split prime, both orientations occur as explicit elements of \(Z_m\), and their coefficients are explicit members of \(A_m\).

For a uniformly chosen engineered pair, the indicators \(1_{i\in I}\) are independent Bernoulli variables of mean \(1/2\). Thus, for every fixed \(0<\varepsilon<1/2\), Hoeffding gives

\[
\#\{z\in Z_m:|I(z)|<(1/2-\varepsilon)m\}
\le4^m e^{-2\varepsilon^2m}.
\tag{11}
\]

All remaining engineered pairs lie in fibers of size at least

\[
2^{(1/2-\varepsilon)m}.
\tag{12}
\]

Using the unconditional upper bound in (5), (12) is at least \(|A_m|^{\eta-o(1)}\) for every \(\eta<1/4-\varepsilon/2\). Thus the current construction rigorously has a fixed positive fiber exponent on almost all of its **engineered** pairs. What is missing is near-total coverage of \(A_m^2\).

## E. Exceptional set

Let \(\mathcal B_m(\varepsilon)\) consist of the unengineered cross-pairs together with the low-active engineered pairs. Equations (8) and (11) give the exact bound

\[
\boxed{
|\mathcal B_m(\varepsilon)|
\le
|A_m|^2-4^m+4^m e^{-2\varepsilon^2m}.
}
\tag{13}
\]

The first term is presently uncontrolled at power scale. Accordingly, the established exceptional exponent is

\[
\boxed{\xi=0.}
\]

This is the point at which the proof stops; (11) by itself cannot repair (13).

## F. Direct image upper bound

The image is split into engineered and unengineered pairs. From (7) and (8),

\[
\boxed{
|Q(A_m,A_m)|
\le
3^m+|A_m|^2-4^m.
}
\tag{14}
\]

This is a direct output count. It does not pass through collision energy. Without a nontrivial estimate for \(|A_m|^2-4^m\), (14) does not imply a fixed power saving.

## G. Exponent ledger and the conditional amplification theorem

With \(m\) as the construction parameter, the rigorously established ledger is

| Quantity | Established exponent or bound |
| --- | --- |
| Engineered pairs \(|G_m|\) | \(\kappa=\log4\) |
| Engineered norm values | \(\log3\) |
| Typical engineered fiber | \((\tfrac12-o(1))\log2\) |
| Coefficient set \(|A_m|\) | \(\log2\le m^{-1}\log|A_m|\le\log4+o(1)\) |
| Relative fiber power, unconditionally | any fixed \(\eta<1/4\), but only on engineered pairs |
| Exceptional exponent in all of \(A_m^2\) | \(\xi=0\) |

For clarity, a **norm-preserving rephasing** of the code means a choice of elements

\[
u_z\in\mathbb Q(\omega)^\times,
\qquad N(u_z)=1
\quad(z\in Z_m),
\]

such that all \(4^m\) products \(u_zz\) remain distinct. Its coefficient completion \(\widetilde A_m\) contains the \(4^m\) distinct coefficient pairs of these products. In the rephased version below, (CR) means

\[
|\widetilde A_m|^2-4^m
\le |\widetilde A_m|^{2-\xi_0}.
\]

This injectivity requirement is essential: without it neither the subtraction of \(4^m\) nor the realized fiber counts would be valid.
In the conditional theorem, \(A_m\) denotes the relevant completion—original or rephased.

The exact amplification statement is as follows.

> **Conditional theorem.** Suppose that the explicit construction (1)--(3), or an injective norm-preserving rephasing in the preceding sense, satisfies (CR) for some \(\xi_0>0\) along an infinite sequence of \(m\). Then
> \[
> |A_m|=2^{m+o(m)}
> \]
> and
> \[
> |Q(A_m,A_m)|
> \le |A_m|^{\log_2 3+o(1)}+|A_m|^{2-\xi_0}.
> \]
> Consequently, every fixed
> \[
> 0<c<\min\{2-\log_2 3,\xi_0\}
> \]
> works for all sufficiently large members of that subsequence.

Indeed, (CR) and \(|G_m|=4^m\) imply \(|A_m|=2^{m+o(m)}\), while (14) gives the displayed image estimate. A harmless further reduction in \(c\) absorbs the sum of the two terms.

The same hypothesis proves the requested realized-fiber certificate. From (11),

\[
4^me^{-2\varepsilon^2m}
=
|A_m|^{2-2\varepsilon^2/\log2+o(1)}.
\]

For any fixed \(\varepsilon>0\) and every

\[
0<\xi'<\min\left\{\xi_0,\frac{2\varepsilon^2}{\log2}\right\},
\]

all but

\[
O\!\left(|A_m|^{2-\xi'}\right)
\]

pairs lie in fibers of size at least \(|A_m|^\eta\) for every fixed

\[
0<\eta<1/2-\varepsilon.
\]

Thus (CR) is sufficient both by direct image counting and by CNF.

## Why this is the first balanced surviving state code

The construction was reached by imposing two necessary local entropy balances.

### Maximum-shell balance

For an \(s\)-state tensor alphabet, let \(c_{\max}\) be the size of its largest one-coordinate norm class. Tensoring produces a same-norm shell of size \(c_{\max}^m\). Since, for fixed \(a,t\), the equation

\[
b^2+ab+a^2=t
\]

has at most two real solutions in \(b\), its coefficient completion has size at least \(c_{\max}^m/2\). Hence

\[
\frac{|Z_m|}{|A_m|^2}
\le4\left(\frac{s}{c_{\max}^2}\right)^m.
\tag{15}
\]

Near-Cartesian coverage therefore requires

\[
c_{\max}\le\sqrt s.
\tag{16}
\]

This immediately kills the natural three-state code \(\{1,\pi,\bar\pi\}\), where \((s,c_{\max})=(3,2)\), and the complete depth-two allocation triangle, where \((s,c_{\max})=(6,3)\).

For the balanced alphabet \(\{1,r_i,\pi_i,\bar\pi_i\}\),

\[
(s,c_{\max})=(4,2),
\]

so (16) holds with equality.

### One-prime marginal balance

Modulo a split prime \(q\), the nonzero solutions of \(Q(a,b)=0\) form disjoint directed triangles: on every multiplicative coset of \(\mu_3\), the allowed pairs are the off-diagonal pairs. If a triangle has vertex weights \(w_1,w_2,w_3\), its directed edge mass is

\[
(w_1+w_2+w_3)^2-(w_1^2+w_2^2+w_3^2)
\le\frac23(w_1+w_2+w_3)^2.
\tag{17}
\]

Thus a near-Cartesian construction cannot force more than \(2/3\) of all pairs into the primitive zero branch at one fixed split prime. The balanced alphabet activates that branch on only two of its four states, a proportion \(1/2\), and so it is not excluded by (17). This does not prove (CR), but it shows why the new state balance escapes the earlier fixed-support failures.

## Two new constructions that are now rigorously closed

These results explain why the balanced code, rather than another long orbit or full divisor box, is the remaining candidate.

### Cyclic norm-one/Chebyshev families

Let \(u\in\mathbb Q(\omega)^\times\) be non-torsion with \(N(u)=1\), and let

\[
Z(C,K)=\{cu^{\pm k}:c\in C,\ k\in K\},
\]

where \(C\subset\mathbb Q_{>0}\) and \(K\subset\mathbb Z_{>0}\) are finite. Some split prime \(q\) and prime \(\mathfrak p\mid q\) satisfy

\[
v_{\mathfrak p}(u)=e>0,
\qquad
v_{\bar{\mathfrak p}}(u)=-e.
\]

Writing \(u^k=a_k-\omega b_k\), unequal-valuation noncancellation gives

\[
v_q(a_k)=v_q(b_k)=-ek.
\]

If \(A\) contains both coefficients of every element of \(Z(C,K)\), partitioning by \(v_q(c)-ek\) yields

\[
\boxed{
|A|\ge\sqrt2\,|K|\sqrt{|C|},
\qquad
\frac{|Z(C,K)|}{|A|^2}\le\frac1{|K|}.
}
\tag{18}
\]

Thus a long cyclic direction loses precisely the reciprocal of its engineered fiber size in Cartesian coverage. This statement concerns the prescribed orbit pairs only; it does not rule out unrelated coincidences among cross-pairs.

An entirely explicit example uses \(\pi=2-\omega\), \(N(\pi)=7\), and \(u=\pi/\bar\pi\). With

\[
z_{h,k}^{\pm}=7^hu^{\pm k},
\qquad 0\le h<n,\quad1\le k\le n,
\]

one obtains \(n\) norm shells, exactly \(2n\) prescribed representations per shell, and \(2n^2\) engineered pairs. Its coefficient set satisfies

\[
|A|\ge
\sqrt2\left(\sqrt n+2\sum_{j=1}^{n-1}\sqrt j\right)
=
\left(\frac{4\sqrt2}{3}+o(1)\right)n^{3/2},
\]

so the engineered density is at most \((9/16+o(1))/n\). This closes the long Chebyshev-recurrence version of coefficient reuse.

### Independent full exponent boxes

For

\[
Z_{m,h}
=
\left\{
\prod_{i=1}^m\pi_i^{e_i}\bar\pi_i^{f_i}:
0\le e_i,f_i\le h
\right\},
\]

unique factorization gives

\[
|Z_{m,h}|=(h+1)^{2m},
\qquad
|N(Z_{m,h})|=(2h+1)^m.
\]

A valuation-marker subcode proves

\[
|A(Z_{m,h})|\ge(2h+1)^m.
\]

Here is the complete counting argument. At coordinate \(i\), restrict \((e_i,f_i)\) to

\[
(h,h),
\quad
(g+1,g),
\quad
(g,g+1)
\qquad(0\le g<h).
\]

In either imbalanced state, both rational coefficients have exact \(q_i\)-adic valuation \(g\). After division by \(q_i^g\), if one coefficient were divisible by \(q_i\), the congruence \(Q(a,b)\equiv0\pmod{q_i}\) would force the other to be divisible as well; then both \(\pi_i\) and \(\bar\pi_i\) would divide the Eisenstein integer, contradicting split valuations \((1,0)\) or \((0,1)\). In the state \((h,h)\), both coefficients have valuation at least \(h\). Thus the vector of truncated valuations recovers \(g\) or the diagonal state.

For one fixed category vector, all orientation choices have one common norm. The first coefficient is injective on these choices: equal first coefficient and equal norm force the second coefficients to be either equal or related by \(b'=-a-b\). The latter replaces \(z\) by \(-\omega^2\bar z\), whose leading unit is incompatible with the unit-\(1\) normalized products in this subcode. A category vector with \(r\) imbalanced coordinates therefore supplies \(2^r\) distinct first coefficients. Summing over category vectors gives

\[
\sum_{r=0}^m\binom mr h^r2^r=(2h+1)^m,
\]

as claimed.

Consequently

\[
\boxed{
\frac{|Z_{m,h}|}{|A(Z_{m,h})|^2}
\le
\left(\frac{h+1}{2h+1}\right)^{2m}.
}
\tag{19}
\]

Thus merely adding many independent exponent shells makes the engineered set exponentially sparse. The structural change in (1) is to keep every prime direction binary and to add a separate neutral state so that neither (15) nor the fixed-zero-branch inequality (17) already forces a loss.

## Audit of the direct unit-distance-style invariant carrier

The most literal transplant of the supplied unit-distance mechanism can also be quantified. This paragraph has deliberately narrow scope.

At one split place of residue norm \(R\ge4\), an optimistic fractional shell-carrier relaxation assigns fractions \(0\le\lambda_n\le1\) to exponent levels. Its normalized coverage and output costs are

\[
C_R=\sum_{n\ge0}(n+1)\lambda_nR^{-n},
\qquad
I_R=\sum_{n\ge0}\lambda_nR^{-n}.
\]

Subject to \(C_R\ge1\), the exact fractional minimum is

\[
I_R^{\min}
=
\frac{R^2-3R+1}{(R-1)^2}.
\]

Indeed, the cost per unit of coverage at level \(n\) is \(1/(n+1)\), so all levels \(n\ge1\) are filled before level \(0\). Their total coverage is

\[
\sum_{n\ge1}(n+1)R^{-n}
=\frac{2R-1}{(R-1)^2}<1,
\]

leaving

\[
\lambda_0=\frac{R^2-4R+2}{(R-1)^2}.
\]

Adding \(\lambda_0\) to \(\sum_{n\ge1}R^{-n}=1/(R-1)\) gives the displayed minimum. At finite depth, the raw uniform output and pair densities represented by these normalizations are, asymptotically,

\[
(1-R^{-1})I_R
\quad\text{and}\quad
(1-R^{-1})^2C_R,
\]

respectively. Thus the calculation below is explicitly an optimistic reweighted-carrier ledger, not a construction covering the uniform pair space.

For \(R=4\), this is \(5/9\). A phase-invariant one-place norm ellipse

\[
\{(a,b):a^2+ab+b^2\le T^2\}
\]

occupies only

\[
\delta=\frac{3\pi}{8\sqrt3}=0.680175\ldots
\]

of its smallest equal-coordinate containing square. Even before any class-number, regulator, denominator, or discriminant loss, the one-prime retained-gain multiplier is

\[
\delta\sqrt{\frac95}
=
\frac{9\pi}{8\sqrt{15}}
=
0.912550\ldots<1.
\]

Equivalently, that particular carrier would need effective retention exceeding \(\sqrt5/3\), an improvement of \(0.091512\ldots\) in logarithmic gain per real degree. This is only a fractional, one-prime, all-rotations-invariant calculation: \(C_R=1\) does not itself prove near-all-pair coverage, and the conclusion is not a universal obstruction to finite correlated windows.

## Comparison with the frozen branches

The balanced construction changes the structural assumption in three ways.

1. It counts exact equalities in \(\mathbb Z[\omega]\), not equality modulo a CRT modulus.
2. It realizes each orientation as an actual pair in one coefficient set; divisor richness is not used as a proxy for representations.
3. It uses a globally correlated multiplicative code. The split-prime branch is active on only half the states, rather than imposing an independent Cartesian restriction at every place.

The remaining problem is therefore not another local density calculation. It is to force the \(4^m\)-edge coefficient graph of (1) to reuse approximately \(2^m\) row/column labels.

There is a useful additive interpretation. A rectangle in the coefficient graph gives

\[
z_{11}+z_{22}=z_{12}+z_{21}.
\]

Hence near-Cartesian coefficient reuse requires quadratically many nontrivial additive relations inside the multiplicative code. More precisely, if the coefficient graph has \(n\) available labels on each side and the products admit no nondegenerate rectangle relation, that graph is \(C_4\)-free and therefore has at most \(n^{3/2}+n\) edges by the stated bipartite bound, far below the required \(n^{2-o(1)}\). In particular, any choice for which these products are additively Sidon cannot work. The factors must instead be embedded in an additive carrier of the kind supplied by the high-degree sum-product mechanism; multiplicative independence alone does not provide the required rectangles.

## H. Exact final checkpoint

1. **Construction closest to TARGET.** The explicit balanced code (1), with \(A_m\) given by the common coefficient completion (2). It has \(4^m\) realized pairs and \(3^m\) exact norm values. For every fixed \(\varepsilon>0\), all but at most an \(e^{-2\varepsilon^2m}\) fraction of its realized pairs lie in fibers of size at least \(2^{(1/2-\varepsilon)m}\). Alternatively, choosing \(\varepsilon_m=m^{-1/4}\) gives fibers \(2^{m/2-o(m)}\) outside a fraction \(e^{-2\sqrt m}=o(1)\); these two rates are not asserted simultaneously.

2. **Its exponents.** In absolute \(m\)-scale notation,
   \[
   \kappa=\log4,\qquad
   \eta_{\mathrm{abs}}=\tfrac12\log2,\qquad
   \log2\le a_m:=m^{-1}\log|A_m|\le\log4+o(1).
   \]
   Relative to the unconditional upper bound on \(|A_m|\), any \(\eta<1/4\) holds on almost all engineered pairs. For the whole Cartesian square the established exceptional exponent is \(\xi=0\).

3. **The single inequality still preventing this certificate from producing \(c>0\).** It is precisely
   \[
   \boxed{|A_m|^2-4^m\le|A_m|^{2-\xi_0}}
   \]
   for some fixed \(\xi_0>0\). No such estimate is presently proved.

4. **Smallest identified concrete modification that could reverse it.** Rephase the entries of the balanced multiplicative code by edge-dependent norm-one elements, preserving distinctness and chosen so that the rephased coefficient graph is almost Cartesian and satisfies (CR). Equivalently, build an additive carrier producing exponentially many rectangle relations among the four-state products. Tensoring with the natural row/column indexing cannot itself supply this: the local matrices
   \[
   \begin{pmatrix}1&\pi_i\\ \bar\pi_i&r_i\end{pmatrix}
   \]
   have nonzero determinant \(r_i-q_i\), so their tensor table has rank \(2^m\), whereas a naturally indexed table \((a_x-\omega a_y)_{x,y}\) has rank at most \(2\). This comparison rules out Cartesianization only when that natural tensor row/column indexing is respected; it does not exclude an accidental Cartesian coefficient-pair set after arbitrary cell reindexing. A norm-one, almost-everywhere mask is the smallest identified structural change that invalidates the scoped rank mismatch while preserving every norm.

The exactly one next unresolved statement is (CR) for a norm-one rephasing of the balanced four-state code.
