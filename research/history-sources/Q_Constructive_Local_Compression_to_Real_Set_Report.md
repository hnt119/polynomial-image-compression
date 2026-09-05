# Constructive phase for \(Q(x,y)=x^2+xy+y^2\)

## A. Constructive route selected

No set satisfying the target was obtained. The local-defect search produced no certified common weight with \(\rho<1\), so I made the required pivot to global split-divisor engineering.

The strongest positive result is an explicit sequence \(A_m\subset\mathbb Z\) with

\[
|A_m|=3^m
\]

such that, for at least \(1-e^{-m/18}\) of all pairs \((a,b)\in A_m^2\),

\[
\prod_{\substack{q\mid Q(a,b)\\q\equiv1\pmod3}}
\bigl(v_q(Q(a,b))+1\bigr)
\ge 2^{m/2}
=
|A_m|^{\frac{\log2}{2\log3}}.
\]

Thus the frozen split-divisor necessary condition can be achieved for almost every pair, with a fixed exponential exponent. Nevertheless, the corresponding image estimate loses by at least \((28/9)^m\), so it does not prove the desired power saving.

All supplied frozen conclusions were treated as hypotheses.

### Rigorous local-search conclusions

The following new results were established offline.

| Local family | Rigorous conclusion |
|---|---|
| Every prime \(q\equiv1\pmod{12}\), every two-valued common weight | \(\rho\ge1\) |
| Residue field \(\mathbb F_7\), every depth | \(\tau(Q;\mathcal O/\mathfrak p^k)=1\) |
| \(\mathbb F_{25}\), every two-valued common weight | \(\rho\ge1\), by exhaustive \(2^{25}\)-subset computation |
| \(\mathbb Z/p^2\), constant unit weight and arbitrary weights on \(p\mathbb Z/p^2\) | \(\rho\ge1\) |
| General multilevel weights on \(\mathbb F_{25},\mathbb F_{37},\mathbb F_{49}\) | No defect found; this is computational evidence only |

For the first row, let \(H\subseteq\mathbb F_q\), \(h=|H|\), and put

\[
U=Q(H,\mathbb F_q),\qquad V=Q(H,H).
\]

The identity

\[
4Q(x,y)=3x^2+(x+2y)^2
\]

and Cauchy–Davenport give

\[
|U|+|V|\ge2h.
\tag{1}
\]

Here the precise standard theorem used is:

> If \(C,D\subseteq\mathbb F_p\) and \(p\) is prime, then
> \[
> |C+D|\ge\min\{p,|C|+|D|-1\}.
> \]

Indeed, writing \(q=4n+1\), when \(h\le2n+1\),

\[
|U|\ge2n+\left\lceil\frac h2\right\rceil,
\qquad
|V|\ge\left\lceil\frac{h^2}{q}\right\rceil.
\]

For \(h=2a\), the only nontrivial integer check follows from

\[
4a^2>(3a-2n-1)(4n+1);
\]

for \(h=2a+1\), it follows from

\[
(2a+1)^2>(3a-2n)(4n+1).
\]

Both differences decrease on \(0\le a\le n\) and equal \(3n+1\) at \(a=n\). If \(h>(q+1)/2\), every fiber \(Q(x,y)=t\ne0\) has \(q-1\) points and projects to at least \((q-1)/2\) values of \(x\), so \(U=\mathbb F_q\); then \(q+h^2/q\ge2h\).

For a two-valued weight \(w=1+u1_H\), \(u\ge0\),

\[
\sum_t\max_{Q(x,y)=t}w_xw_y
=
q+u(|U|+|V|)+u^2|V|,
\]

while \(\sum_xw_x=q+uh\). Consequently,

\[
q\sum_t\max_{Q=t}w_xw_y-\left(\sum_xw_x\right)^2
=
qu(|U|+|V|-2h)+u^2(q|V|-h^2)\ge0.
\]

Hence no two-level defect exists in these prime fields.

For residue \(7\), exact Ferrers recurrences give the ordinary maxima

\[
[0,3,10,19,27,35,41,49]
\]

for output-set sizes \(0,\ldots,7\), and the distinguished-center maxima

\[
[1,6,11,15,19,21,24].
\]

These imply the strengthened residue inequality

\[
\max\{A_0B_0,7L_0\}
+7\sum_{t\ne0}L_t
\ge
\left(\sum_aA_a\right)\left(\sum_bB_b\right).
\tag{2}
\]

The key point is that a punctured zero pair \((a,b)\) creates two distinct nonzero cross-outputs \(a^2,b^2\). If \(c=A_0B_0\), \(\ell=L_0\), and \(s=\sqrt{\ell/c}\), layer cake and the distinguished gaps give

\[
I\ge c(1-s)(3s-1).
\]

When \(7\ell\ge c\), this is nonnegative because \(s\ge1/\sqrt7>1/3\). When \(7\ell<c\), adding the correction \(c-7\ell\) gives

\[
I+c-7\ell\ge c(4s-10s^2)>0
\]

because \(s<1/\sqrt7<2/5\).

The standard simple-root Hensel theorem then lifts (2) from depth \(k-2\) to depth \(k\): when one coordinate of \(\nabla Q\) is a unit, every lifted target has exactly \(7^{k-1}\) preimages in that residue block. Since

\[
Q(\pi x,\pi y)=\pi^2Q(x,y),
\]

the central block renormalizes to depth \(k-2\). Thus \(\tau=1\) at every depth above \(\mathbb F_7\).

## B. Explicit split-divisor construction

Choose distinct primes \(q_i\equiv1\pmod3\). This can be made recursive without invoking Dirichlet’s theorem. Given \(P_{j-1}=q_1\cdots q_{j-1}\), let \(q_j\) be a prime divisor of

\[
(3P_{j-1})^2+3P_{j-1}+1.
\]

It is new, and \(3P_{j-1}\pmod{q_j}\) has exact order \(3\); hence \(q_j\equiv1\pmod3\).

Let

\[
C_i=\mu_3(\mathbb F_{q_i})
=\{1,\zeta_i,\zeta_i^2\},
\qquad
M_m=\prod_{i=1}^m q_i,
\]

and define

\[
A_m=
\left\{
0\le a<M_m:
a\bmod q_i\in C_i\quad(1\le i\le m)
\right\}.
\tag{3}
\]

By the Chinese remainder theorem,

\[
|A_m|=3^m.
\tag{4}
\]

For \(x,y\in C_i\),

\[
Q(x,y)=0
\iff x\ne y,
\]

because \(x/y\) is then a nontrivial cube root of unity. If \(x=y\),

\[
Q(x,x)=3x^2\ne0.
\]

Thus, for \(a,b\in A_m\),

\[
q_i\mid Q(a,b)
\iff
a\bmod q_i\ne b\bmod q_i.
\tag{5}
\]

For a uniformly chosen ordered pair, the indicators in (5) are independent Bernoulli variables of mean \(2/3\). The precise standard Hoeffding inequality used is

\[
\Pr\!\left(\sum_{i=1}^mX_i-\mathbb E\sum_iX_i\le-t\right)
\le e^{-2t^2/m}.
\]

Taking \(t=m/6\) gives

\[
\Pr\!\left(\#\{i:q_i\mid Q(a,b)\}<m/2\right)
\le e^{-m/18}.
\]

Since every \(q_i\) splits in \(\mathbb Q(\omega)/\mathbb Q\), almost every pair therefore has split-divisor product at least \(2^{m/2}\).

No denominators, class groups, embeddings, or injectivity losses occur here: \(A_m\) consists of ordinary integers and CRT representatives are unique.

## C. Amplification theorem

Although no defect was found, the local-to-set amplification can be completed exactly.

Let \(\mathcal R\) have \(n\) elements, and let \(p\) be a rational probability weight satisfying

\[
\rho
=
n\sum_t\max_{Q(x,y)=t}p_xp_y<1.
\]

Put

\[
h=-\sum_xp_x\log p_x,
\qquad
s=|\operatorname{supp}p|.
\]

For every sufficiently divisible \(m\), take the exact type class

\[
B_m=
\left\{
\mathbf x\in\mathcal R^m:
|\{i:x_i=x\}|=mp_x\ \forall x
\right\}.
\]

Elementary multinomial estimates give

\[
(m+1)^{-s}e^{mh}\le |B_m|\le e^{mh}.
\tag{6}
\]

Every word in \(B_m\) has product probability \(e^{-mh}\). Exact tensorization of the output maxima gives

\[
\sum_{\mathbf t}
\max_{Q^{\otimes m}(\mathbf x,\mathbf y)=\mathbf t}
p^{\otimes m}(\mathbf x)p^{\otimes m}(\mathbf y)
=
\left(\frac{\rho}{n}\right)^m.
\]

Every output from \(B_m^2\) contributes at least \(e^{-2mh}\), so

\[
|Q(B_m,B_m)|
\le
e^{2mh}\left(\frac{\rho}{n}\right)^m.
\]

Therefore

\[
\boxed{
\frac{n^m|Q(B_m,B_m)|}{|B_m|^2}
\le (m+1)^{2s}\rho^m.
}
\tag{7}
\]

The same \(B_m\) occurs in both variables. Irrational strict defects can first be approximated by rational weights, since the finite maximum functional is continuous.

A useful necessary entropy relation follows from nonemptiness of the output:

\[
-\log\rho\le2h-\log n.
\tag{8}
\]

## D. Global-realization audit

### Distinct rational CRT moduli

Suppose one uses pairwise coprime \(q_i^{k_i}\), with local gain

\[
\eta_i=-\log\rho_i
\]

and entropy \(h_i\). The frozen maximum-fiber bound gives

\[
\eta_i
\le
\log\!\left(1+k_i\left(1-\frac1{q_i}\right)\right)
\le\log(k_i+1).
\]

By (8),

\[
h_i\ge\frac12k_i\log q_i.
\]

Hence

\[
\frac{\eta_i}{h_i}
\le
\frac{2\log(k_i+1)}{k_i\log q_i}.
\tag{9}
\]

For pairwise distinct rational primes, the aggregate ratio tends to zero: large primes make the denominator in (9) large, while increasing the depth at any fixed prime makes \(\log(k+1)/k\to0\). Therefore the canonical integer-CRT/type-shell certificate cannot give a fixed power saving, even if isolated local defects exist.

### Repeating one fixed local factor in number fields

Suppose instead that

\[
\mathcal O_{L_d}/\mathfrak m_d\simeq\mathcal R^{m},
\qquad
m/d\to\theta,
\qquad
\operatorname{rd}(L_d)\to D.
\]

Assume a correlated lattice count of the form

\[
|A_d|
\ge
e^{-o(d)}
\frac{|B_m|}{n^m}
\frac{(\gamma T)^d}{\sqrt{\Delta_{L_d}}}.
\tag{10}
\]

Norm separation in an ideal gives at most

\[
\left(1+3T^2n^{-\theta}\right)^d
\]

output lifts of any one residue. Combining this with (7) yields

\[
|Q(A_d,A_d)|
\le
|A_d|^2e^{-\varepsilon d+o(d)},
\]

where

\[
\varepsilon
=
\theta(-\log\rho)
-
\log\!\left(
\frac{D(n^\theta+3T^2)}{\gamma^2T^2}
\right).
\tag{11}
\]

If

\[
a=
\theta(h-\log n)+\log(\gamma T)-\frac12\log D>0
\]

and \(\varepsilon>0\), then every

\[
0<c<\frac{\varepsilon}{a}
\]

works eventually; for instance \(c=\varepsilon/(2a)\).

No available construction supplies (10) for a bad correlated type class.

There is also a decisive depth-one barrier even under optimistic fixed-scale equidistribution. That model would give

\[
\varepsilon_{\mathrm{vol}}
=
\theta(-\log\rho)+\log(4/3)-\frac12\log D.
\tag{12}
\]

The precise standard Minkowski discriminant bound used is

\[
|\Delta_L|\ge\left(\frac{d^d}{d!}\right)^2
\]

for totally real degree-\(d\) fields, so asymptotically \(D\ge e^2\). At depth one,

\[
\rho\ge\frac q{2q-1}>\frac12,
\]

because the largest split fiber has \(2q-1\) points. Thus

\[
\varepsilon_{\mathrm{vol}}
<
\log2+\log(4/3)-1
=
\log\frac8{3e}<0.
\]

Consequently even a hypothetical depth-one defect cannot win through this standard totally real volume realization. Only a sufficiently strong deep prime-power defect could survive this ledger; residues \(7\) and \(13\) are now closed at every depth.

## E. Image count and final exponent

For the explicit divisor-rich construction (3),

\[
Q(C_i,C_i)=\{0\}\cup3C_i,
\qquad |Q(C_i,C_i)|=4.
\]

Therefore

\[
|Q(A_m,A_m)\bmod M_m|=4^m
\tag{13}
\]

and the normalized CRT factor equals

\[
\frac{M_m4^m}{|A_m|^2}
=
\prod_{i=1}^m\frac{4q_i}{9}
\ge
\left(\frac{28}{9}\right)^m.
\tag{14}
\]

Since \(0\le Q(a,b)<3M_m^2\), every residue modulo \(M_m\) has at most \(3M_m\) possible lifts, giving

\[
|Q(A_m,A_m)|\le3M_m4^m.
\tag{15}
\]

This is larger than the trivial \(9^m\) bound and hence gives no saving.

Cross-coordinate correlations confined to the same ternary alphabet cannot repair the normalized loss. For every \(B\subseteq C^m\), the diagonal map

\[
\mathbf x\longmapsto Q(\mathbf x,\mathbf x)=3\mathbf x^2
\]

is injective. Hence

\[
|Q(B,B)|\ge|B|,
\qquad
\frac{q^m|Q(B,B)|}{|B|^2}
\ge\frac{q^m}{|B|}
\ge\left(\frac q3\right)^m>1.
\]

A separate fixed-norm audit reaches the same Cartesian obstruction. In \(\mathbb Z[\omega]\), choose \(q_i=\pi_i\bar\pi_i\) and

\[
Z_m=
\left\{
\prod_i\pi_i^{\epsilon_i}\bar\pi_i^{1-\epsilon_i}:
\epsilon_i\in\{0,1\}
\right\}.
\]

The standard fact used here is that the Eisenstein integers are norm-Euclidean, hence a UFD. Thus \(|Z_m|=2^m\), all elements have the same norm, and writing \(z=a-\omega b\) gives \(2^m\) pairs with one common \(Q\)-value. But fixing \(a\) leaves a quadratic equation in \(b\), so if \(A\) contains all coefficient projections,

\[
|A|\ge2^{m-1},
\qquad
\frac{\#\text{ engineered pairs}}{|A|^2}
\le2^{2-m}.
\]

One exponentially rich norm shell is therefore exponentially negligible inside the Cartesian completion.

No concrete \(c>0\) has been obtained, and the original target remains unresolved.

## F. The single quantitative obstruction

For the explicit almost-everywhere split-divisor construction, let

\[
\overline q_m=M_m^{1/m}.
\]

The exact CRT/image certificate would have a positive exponent only if

\[
\boxed{\frac{4\overline q_m}{9}<1.}
\tag{16}
\]

But every good split rational prime is at least \(7\), so

\[
\frac{4\overline q_m}{9}\ge\frac{28}{9}>1.
\]

This is the precise obstruction: three divisor-rich input symbols create four output symbols, and the ambient split-prime cost overwhelms the \(9\)-pair input entropy. The construction proves exponential split-divisor richness for almost all pairs, but not a power-saving image bound.
