# Parity-Twisted Cartesianization: exact obstructions, the best \(m=2\) carrier, and the remaining composition barrier

## Offline status and scope

This report works entirely offline. It accepts the frozen parity-twisted code and the exact \(m=1\) gadget as input. No web search, external database, or recent-paper citation is used.

The answer is not a proof of the ultimate power-saving target. The strongest rigorous conclusion is:

> **PTCR remains unresolved, but Exact-PTCR is false for every \(m\ge 2\), the natural binary placement is not even approximately repairable with \(o(4^m)\) deleted cells, every endpoint-local/affine two-copy recursion is obstructed, and every fixed imperfect block loses exponentially under ordinary repetition.**

There is nevertheless a new exact finite carrier: for the first two coordinates, six integer coefficients realize all \(16\) twisted codewords. What is missing is a nonlinear, globally reassigning composition law that merges almost all coefficient overhead from one scale to the next.

### Standard results used

Only the following standard facts are used.

1. **Unique factorization.** Positive integers have unique prime factorization. Also, the Eisenstein integers \(\mathbb Z[\omega]\) are Euclidean for the norm and hence are a unique-factorization domain. The latter is used to audit injectivity of the explicit edge recursion.
2. **Finite-field group fact.** \(\mathbb F_r^\times\) has order \(r-1\); hence, when \(r\equiv2\pmod3\), it has no nontrivial element of order \(3\). This proves anisotropy of \(X^2+XY+Y^2\) modulo \(r\).
3. **Kolmogorov--Rogozin concentration inequality.** If \(Y_1,\dots,Y_m\) are independent real random variables and

   \[
   \mathcal Q(Y,h)=\sup_t\Pr(Y\in[t,t+h]),
   \]

   then, for \(0<h_i\le h\),

   \[
   \mathcal Q\!\left(\sum_iY_i,h\right)
   \le C h\left(\sum_i h_i^2
   (1-\mathcal Q(Y_i,h_i))\right)^{-1/2}
   \]

   with an absolute constant \(C\). This precise standard version is assumed in the robust natural-indexing obstruction in Section F.
4. **Finite-field irreducible count and reduction criterion.** The number of monic irreducible degree-\(n\) polynomials over \(\mathbb F_q\) is

   \[
   I_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}.
   \]

   We also use: if \(R\) is a discrete valuation ring with fraction field \(F\), a polynomial in \(R[T]\) has unit leading coefficient, and its reduction has the same degree and is irreducible over the residue field, then it is irreducible in \(F[T]\). These are used only for the digit-composition audit in Section F.

All other arguments are elementary and are proved below. Throughout, the rational primes \(r_i\equiv2\pmod3\) and \(q_i\equiv1\pmod3\) have fresh, pairwise-distinct rational-prime support, and \(q_i=\pi_i\bar\pi_i\) in \(\mathbb Z[\omega]\). This is the standard code hypothesis ensuring the stated word counts and multiplicities.

---

## A. PTCR verdict

### Verdict: unresolved but sharply reduced

Let \(n_m=|A_m|\), let \(e_m=4^m\) be the number of injectively engineered codeword-pairs, and put

\[
d_m=n_m^2-4^m.
\]

No family with \(d_m\le n_m^{2-\xi}\) has been constructed, and PTCR has not been disproved under arbitrary global cell permutations. The following branches are now rigorously closed.

| Mechanism | Rigorous verdict |
|---|---|
| Exact Cartesian realization | Impossible for every \(m\ge2\), under arbitrary cell permutations |
| Natural binary placement | Requires \(d_m=\Omega(4^m)\), even if cells may be deleted |
| Endpoint-local finite-state lift | Impossible on complete blocks of size at least \(3\times3\) |
| Affine two-copy lift | Any parent graph satisfies \(e\le n^2/2+n\) |
| Fixed imperfect block repeated independently | Engineered density decays exponentially |
| Ordinary scalar digit composition | Image has exponent \(2-o(1)\), despite one-block compression |
| Exact edge-level two-state lift | Exists and composes, but its known coefficient carrier is only \(O(4^m)\) |

Thus any surviving PTCR construction must:

1. permute norm words globally rather than retain natural binary indexing;
2. use genuinely mixed dependence on both endpoints rather than two independent vertex maps;
3. repair inherited coefficient overhead, not merely add \(o(n_m)\) new coefficients at every step.

The exact quantitative meaning of item 3 is given in Section G.

---

## B. Exact \(m=2\) verdict

### B.1 The complete norm histogram

Write

\[
r=r_1,\qquad s=r_2,\qquad p=q_1,\qquad q=q_2.
\]

For \(m=2\), the parity-twisted norm multiset is

| Norm value | Multiplicity |
|---|---:|
| \(3,\,3r^2,\,3s^2,\,3r^2s^2\) | \(1\) each |
| \(p,\,ps^2,\,q,\,r^2q\) | \(2\) each |
| \(3pq\) | \(4\) |

All nine displayed values are distinct by unique prime factorization.

### B.2 Complete symbolic obstruction for four rational coefficients

Assume that four rational numbers \(a_1,\dots,a_4\) realize this multiset on all \(16\) cells of their \(Q\)-table, allowing an arbitrary cell permutation.

Because \(Q(a,b)=Q(b,a)\), every off-diagonal occurrence is paired with its transpose. A multiplicity-one value must therefore lie on the diagonal. There are four singleton labels and four diagonal cells, so

\[
\{3a_i^2:1\le i\le4\}
=\{3,3r^2,3s^2,3r^2s^2\}.
\]

Consequently

\[
\{|a_i|:1\le i\le4\}=\{1,r,s,rs\}.
\tag{B1}
\]

Every \(a_i\) is a \(3\)-adic unit. For such units,

\[
Q(a,b)=a^2+ab+b^2\equiv(a-b)^2\pmod3.
\]

In fact, \(v_3(Q(a,b))=1\) when \(a\equiv b\pmod3\), and it is \(0\) when \(a\not\equiv b\pmod3\). Among the six unordered off-diagonal edges, four labels have \(3\)-adic valuation \(0\), while the two edges labeled \(3pq\) have valuation \(1\).

If \(h\) of the four vertices occupy one of the two nonzero residue classes modulo \(3\), the number of cross-class edges is \(h(4-h)\). Hence \(h(4-h)=4\), so \(h=2\). The two \(3pq\)-edges are exactly the two within-class edges and form a perfect matching of the magnitude set in (B1). There are three matchings.

1. For \(\{1,r\},\{s,rs\}\), equal residues force opposite signs at both pairs. The two values are

   \[
   r^2-r+1,\qquad s^2(r^2-r+1),
   \]

   and are unequal.
2. For \(\{1,s\},\{r,rs\}\), the two values are

   \[
   s^2-s+1,\qquad r^2(s^2-s+1),
   \]

   and are unequal.
3. For \(\{1,rs\},\{r,s\}\), equal residues force equal signs at each pair. The two values are

   \[
   1+rs+r^2s^2,\qquad r^2+rs+s^2.
   \]

   Their difference is

   \[
   (r^2-1)(s^2-1)>0.
   \]

Both matching edges would have to carry the same value \(3pq\). Each possibility is impossible. Therefore

\[
\boxed{\text{Exact-PTCR is false at }m=2\text{ under every cell permutation.}}
\]

### B.3 Stronger theorem: Exact-PTCR fails for every \(m\ge2\)

The \(m=2\) obstruction extends to all lengths.

#### Inert-prime anisotropy lemma

If \(r\equiv2\pmod3\) is prime and \(a,b\in\mathbb Q\), then

\[
v_r(Q(a,b))=2\min\{v_r(a),v_r(b)\},
\tag{B2}
\]

with \(v_r(0)=+\infty\). Extract the common power \(r^j\). At least one residual coordinate is an \(r\)-adic unit. A nonzero zero of \(X^2+XY+Y^2\) modulo \(r\) would yield a nontrivial cube root of unity in \(\mathbb F_r^\times\), impossible because \(3\nmid r-1\). The residual \(Q\)-value is a unit, proving (B2).

#### Forced diagonal and coatom values

The \(2^m\) multiplicity-one norm labels are precisely

\[
3\prod_{i\in I}r_i^2,\qquad I\subseteq[m].
\]

Symmetry forces all of them onto the \(2^m\) diagonal cells. Hence any exact coefficient set must be

\[
A=\left\{\varepsilon_I\prod_{i\in I}r_i:I\subseteq[m]\right\},
\qquad \varepsilon_I\in\{\pm1\}.
\tag{B3}
\]

Put \(P=\prod_i r_i\). Consider the off-diagonal pair with coefficient magnitudes \(P\) and \(P/r_i\). Formula (B2) shows that its target has \(r\)-support exactly \([m]\setminus\{i\}\). The only two norm values with that support are

\[
3(P/r_i)^2
\quad\text{and}\quad
(P/r_i)^2q_i.
\]

The first is a singleton already consumed on the diagonal. Thus

\[
q_i=r_i^2\pm r_i+1.
\]

The minus choice is divisible by \(3\); it equals \(3\) for \(r_i=2\) and is a composite multiple of \(3\) for \(r_i>2\). It cannot be the prescribed prime \(q_i\equiv1\pmod3\). Therefore

\[
q_i=r_i^2+r_i+1
\tag{B4}
\]

for every \(i\), and the two coatom signs agree.

#### The all-split target is too large

Let \(r_*=\min_i r_i\). The two largest distinct coefficient magnitudes in (B3) are \(P\) and \(P/r_*\). Therefore every off-diagonal entry satisfies

\[
Q(a,b)\le P^2\left(1+\frac1{r_*}+\frac1{r_*^2}\right).
\tag{B5}
\]

The all-split target is

\[
T=\kappa_m\prod_iq_i,\qquad
\kappa_m=
\begin{cases}
3,&m\text{ even},\\
1,&m\text{ odd}.
\end{cases}
\]

Using (B4),

\[
T=\kappa_mP^2
\prod_i\left(1+\frac1{r_i}+\frac1{r_i^2}\right).
\tag{B6}
\]

When \(m\ge2\), (B6) contains the factor appearing in (B5) and at least one further factor strictly larger than \(1\). Hence \(T\) is larger than every off-diagonal entry. It cannot occur on the diagonal, since all diagonal cells have already been consumed by singleton labels. This contradiction proves

\[
\boxed{\text{Exact-PTCR fails for every }m\ge2,\text{ even after arbitrary cell permutation.}}
\tag{B7}
\]

This theorem does **not** disprove asymptotic PTCR: the \(2^m\asymp n_m\) singleton constraints can be absorbed by a deficit as large as \(n_m^{2-\xi}\) when \(\xi<1\).

---

## C. Best coefficient set found

### C.1 A complete six-point carrier at \(m=2\)

Take

\[
(r_1,q_1)=(2,7),\qquad (r_2,q_2)=(5,31).
\]

The required histogram is

\[
\begin{array}{c|ccccccccc}
t&3&12&75&300&7&31&124&175&651\\ \hline
\text{multiplicity}&1&1&1&1&2&2&2&2&4.
\end{array}
\tag{C1}
\]

Define

\[
\boxed{A_2=\{-25,-10,-5,-2,-1,26\}.}
\tag{C2}
\]

The four singleton values occur on the diagonals:

\[
Q(-1,-1)=3,\quad
Q(-2,-2)=12,\quad
Q(-5,-5)=75,\quad
Q(-10,-10)=300.
\tag{C3}
\]

Four transpose pairs give the multiplicity-two values:

\[
\begin{aligned}
Q(-2,-1)&=7,&
Q(-5,-1)&=31,\\
Q(-10,-2)&=124,&
Q(-10,-5)&=175.
\end{aligned}
\tag{C4}
\]

Finally,

\[
Q(-25,-1)=Q(-25,26)=Q(-1,26)=651.
\tag{C5}
\]

Any two unordered edges of the \(651\)-triangle in (C5) supply the required four directed cells. Thus all \(16\) codewords occupy distinct cells of \(A_2^2\), and

\[
n_2=6,\qquad e_2=16,\qquad d_2=36-16=20,\qquad v_2=9.
\tag{C6}
\]

The full table has

\[
|Q(A_2,A_2)|=19,
\]

but this isolated numerical compression has no known real composition law.

### C.2 Why the \(651\)-triangle is structural

For \(t\ne0\), if

\[
Q(x,y)=Q(x,z)=t,\qquad y\ne z,
\]

then

\[
0=Q(x,y)-Q(x,z)=(y-z)(x+y+z),
\]

so \(x+y+z=0\), and then \(Q(y,z)=t\). Thus every nonzero level graph of \(Q\) has maximum degree \(2\), and every degree-two component closes into a triangle. The final two coefficients in (C2) exploit exactly this geometry.

### C.3 Exact integral minimality

Six is minimal among **integer** coefficient sets for the histogram (C1). Indeed,

\[
Q(a,b)-\frac{a^2+b^2}{2}=\frac{(a+b)^2}{2}\ge0.
\]

Every endpoint of a selected cell is therefore bounded by

\[
|a|\le\lfloor\sqrt{2\cdot651}\rfloor=36.
\]

An exact enumeration gives \(28\) possible integer endpoints and no realizing subset of size \(4\) or \(5\), while it gives \(12\) realizing subsets of size \(6\). The finite verifier is:

~~~python
from itertools import combinations

need = {3:1, 12:1, 75:1, 300:1,
        7:2, 31:2, 124:2, 175:2, 651:4}

V = sorted({x
    for a in range(-36, 37)
    for b in range(-36, 37)
    if a*a + a*b + b*b in need
    for x in (a,b)})

def realizes(S):
    return all(sum(a*a+a*b+b*b == t for a in S for b in S) >= r
               for t,r in need.items())

for n in (4,5,6):
    ans = [S for S in combinations(V,n) if realizes(S)]
    print(n, len(ans))
~~~

The output is \(0,0,12\). Any unused coefficient could be deleted, so restricting the enumeration to endpoints of required cells loses no minimal realization. Over \(\mathbb Q\), the rigorous conclusion is only

\[
5\le n_{2,\min}^{(\mathbb Q)}\le6.
\]

The five-point rational optimum is not decided here. It is not a composition bottleneck, because every fixed nonexact block is sparse under repetition.

There is a nested finite progression:

\[
A_4=\{-10,-5,-2,-1\},\qquad
A_5=A_4\cup\{-25\},\qquad
A_6=A_5\cup\{26\}.
\]

The set \(A_4\) realizes the four diagonal cells and the four transpose pairs in (C3)--(C4), hence \(12\) codewords. The set \(A_5\) adds the two orientations of \(\{-25,-1\}\), hence realizes \(14\). The final point \(26\) supplies enough of the \(651\)-triangle to realize all \(16\). Their finite scorecard is

| Set | Coefficients | Engineered cells | \(n^2-e\) |
|---|---:|---:|---:|
| \(A_4\) | \(4\) | \(12\) | \(4\) |
| \(A_5\) | \(5\) | \(14\) | \(11\) |
| \(A_6\) | \(6\) | \(16\) | \(20\) |

### C.4 A general \(m\)-coordinate partial core

For any finite admissible list satisfying \(q_i=r_i^2+r_i+1\), define

\[
B_m=\left\{-\prod_{i=1}^m r_i^{x_i}:x\in\{0,1\}^m\right\}.
\tag{C7}
\]

For naturally indexed pairs \((x,y)\) with \(d_H(x,y)=0\), the diagonal identity gives the required factor \(3\). For \(d_H(x,y)=1\), removing the common square factor reduces the value to

\[
Q(-1,-r_i)=r_i^2+r_i+1=q_i,
\]

and the parity twist contributes no \(3\). Hence (C7) realizes exactly

\[
2^m\left(\binom m0+\binom m1\right)=2^m(m+1)
\]

natural codewords. Its fraction of all \(4^m\) codewords is

\[
\frac{m+1}{2^m}\longrightarrow0.
\]

Thus the attractive \(m=2\) four-point core is only a Hamming-radius-one phenomenon.

No assertion that such prime pairs exist for every \(m\) is needed or made; this subsection records the exact algebraic pattern conditional on the chosen finite list.

---

## D. Exact norm table and its finite-state recursion

For \(x,y\in\mathbb F_2^m\), put

\[
U_m(x,y)=\prod_{i=1}^m
r_i^{2x_iy_i}q_i^{x_i\oplus y_i},
\qquad
p(x,y)=d_H(x,y)\pmod2.
\]

The required table and its complementary twist are

\[
T_m^+(x,y)=3^{\mathbf1_{p(x,y)=0}}U_m(x,y),
\qquad
T_m^-(x,y)=3^{\mathbf1_{p(x,y)=1}}U_m(x,y).
\tag{D1}
\]

The original parity-twisted table is \(T_m^+\). Starting from

\[
T_0^+=(3),\qquad T_0^-=(1),
\]

adjoining a coordinate with parameters \((q,r)\) gives

\[
\boxed{
T_{m+1}^+
=
\begin{pmatrix}
T_m^+&qT_m^-\\
qT_m^-&r^2T_m^+
\end{pmatrix},
\qquad
T_{m+1}^-
=
\begin{pmatrix}
T_m^-&qT_m^+\\
qT_m^+&r^2T_m^-
\end{pmatrix}.}
\tag{D2}
\]

Equal new bits preserve old Hamming parity; unequal new bits reverse it. This proves (D2) entry by entry. In particular,

\[
T_1^+=\begin{pmatrix}3&q\\q&3r^2\end{pmatrix},
\qquad
T_1^-=\begin{pmatrix}1&3q\\3q&r^2\end{pmatrix}.
\tag{D3}
\]

For \((q,r)=(7,2)\), \(T_1^+\) is exactly the frozen table on \(\{1,2\}\).

Equation (D2) is an important structural correction: the gadget is a **two-state automaton**, not a one-state tensor factor. The auxiliary table \(T_m^-\) cannot itself be a rational same-set \(Q\)-table: its multiplicity-one labels are rational squares without the factor \(3\), whereas every rational diagonal has the form \(3a^2\).

The cells in (C3)--(C5) have exactly the histogram generated by (D2), so every engineered \(m=2\) cell has the required parity-twisted norm.

---

## E. Explicit norm-one phases

Choose

\[
\lambda=1-\omega,\qquad
\pi_1=2-\omega,\qquad
\pi_2=5-\omega.
\]

Then

\[
N(\lambda)=3,\qquad N(\pi_1)=7,\qquad N(\pi_2)=31.
\]

Use the following explicit assignment of the \(16\) codewords to cells of (C2). A bar denotes Eisenstein conjugation.

| Twisted codeword \(z^\sharp\) | Assigned \((a,b)\) | \(Q(a,b)\) |
|---|---:|---:|
| \(\lambda\) | \((-1,-1)\) | \(3\) |
| \(2\lambda\) | \((-2,-2)\) | \(12\) |
| \(5\lambda\) | \((-5,-5)\) | \(75\) |
| \(10\lambda\) | \((-10,-10)\) | \(300\) |
| \(\pi_1\) | \((-2,-1)\) | \(7\) |
| \(\bar\pi_1\) | \((-1,-2)\) | \(7\) |
| \(\pi_2\) | \((-5,-1)\) | \(31\) |
| \(\bar\pi_2\) | \((-1,-5)\) | \(31\) |
| \(2\pi_2\) | \((-10,-2)\) | \(124\) |
| \(2\bar\pi_2\) | \((-2,-10)\) | \(124\) |
| \(5\pi_1\) | \((-10,-5)\) | \(175\) |
| \(5\bar\pi_1\) | \((-5,-10)\) | \(175\) |
| \(\lambda\pi_1\pi_2\) | \((-25,-1)\) | \(651\) |
| \(\lambda\pi_1\bar\pi_2\) | \((-1,-25)\) | \(651\) |
| \(\lambda\bar\pi_1\pi_2\) | \((-25,26)\) | \(651\) |
| \(\lambda\bar\pi_1\bar\pi_2\) | \((26,-25)\) | \(651\) |

For every row of this table define, explicitly,

\[
\boxed{u_z=\frac{a-\omega b}{z^\sharp}.}
\tag{E1}
\]

Both numerator and denominator lie in \(\mathbb Q(\omega)^\times\). The displayed norm verification gives

\[
N(u_z)=\frac{Q(a,b)}{N(z^\sharp)}=1.
\tag{E2}
\]

The \(16\) cells are distinct, so the rephased elements \(a-\omega b\) are distinct. Thus (E1) verifies membership, norm preservation, and injectivity without a hidden integrality or denominator assumption. The four diagonal phases are \(-1\); the other phases need not be units of \(\mathbb Z[\omega]\), because PTCR requires only norm-one elements of \(\mathbb Q(\omega)\).

---

## F. Composition theorem and composition obstructions

There is an exact composition law on **edges**, but not a successful near-Cartesian composition law on vertices.

### F.1 Exact edge cocycle

Represent \(e=a-\omega b\) by the column \((a,b)^{\mathsf T}\). If \(\eta=c-\omega d\), then

\[
M(\eta)=
\begin{pmatrix}
c&-d\\
d&c+d
\end{pmatrix},
\qquad
Q(M(\eta)(a,b)^{\mathsf T})=N(\eta)Q(a,b).
\tag{F1}
\]

Let \(\pi=c-\omega d\) have norm \(q\), and let \(p\in\{0,1\}\) be the old Hamming parity. Set

\[
\eta_p=\pi\lambda^{2p-1}.
\tag{F2}
\]

Then

\[
N(\eta_0)=q/3,\qquad N(\eta_1)=3q.
\]

From an old edge element \(e\), form

\[
e,\qquad re,\qquad \eta_pe,\qquad \bar\eta_pe.
\tag{F3}
\]

Their norm multipliers are exactly the four multipliers required in (D2). Conjugate children reverse the ordered endpoints because, with \(S=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)\),

\[
M(\bar\eta)=SM(\eta)S.
\]

Starting from the exact \(m=1\) edges, (F3) produces \(4^m\) distinct child edges of the correct norms at every level. Fresh prime support and unique factorization in \(\mathbb Z[\omega]\) show that distinct state words remain nonassociate and hence distinct. The division by \(\lambda\) in \(\eta_0\) causes no integrality defect: every parity-zero old word already contains the required \(\lambda\)-factor.

If \(\Gamma_m=\Gamma_m^0\sqcup\Gamma_m^1\subseteq A_m^2\) is partitioned by old parity, an explicit coefficient carrier is

\[
\begin{aligned}
\mathcal C_{m+1}={}&A_m\cup rA_m\\
&\cup\bigcup_{p=0}^1\operatorname{coord}(M(\eta_p)\Gamma_m^p)\\
&\cup\bigcup_{p=0}^1\operatorname{coord}(SM(\eta_p)S\Gamma_m^p),
\end{aligned}
\tag{F4}
\]

where \(\operatorname{coord}\) is the union of the two coordinate projections. This is a genuine exact, all-\(m\) edge composition theorem. Its present bound is only

\[
|\mathcal C_{m+1}|\le2|A_m|+4\cdot4^m.
\tag{F5}
\]

Starting with \(n_1=2\), (F5) gives

\[
n_m\le2\cdot4^m-3\cdot2^m.
\tag{F6}
\]

This has exponential rate at most \(\log4\), not the required \(\log2\). For the canonical lift from \((2,7)\) to \((5,31)\), the carrier is

\[
\{-10,1,2,5,10,25,29\},
\]

of size \(7\) and deficit \(49-16=33\). The separately found set (C2) improves the finite carrier to size \(6\), but it is not produced by a useful recursion.

### F.2 Endpoint-local lifting is algebraically impossible

The mixed matrices in (F1) are forced, not an artifact of one choice.

**Separated-variable rigidity.** Let \(X,Y\subset\mathbb Q\) each contain at least three points. If arbitrary functions \(F:X\to\mathbb Q\), \(G:Y\to\mathbb Q\) satisfy

\[
Q(F(x),G(y))=\kappa Q(x,y)
\quad(x\in X,\ y\in Y),\qquad \kappa\ne0,
\]

then

\[
F(x)=\varepsilon\sqrt\kappa\,x,\qquad
G(y)=\varepsilon\sqrt\kappa\,y
\]

for one sign \(\varepsilon\); in particular \(\sqrt\kappa\in\mathbb Q\).

To prove this, subtract the equations for two \(y\)-values. The result makes \(F\) affine; reversing the variables makes \(G\) affine. The resulting polynomial of total degree at most \(2\) vanishes on a \(3\times3\) grid and is therefore the zero polynomial. Coefficient comparison forces equal slopes and zero translations.

An endpoint-local lift would require the same endpoint map to scale one complete block by \(1\) and another by \(q/3\). Rigidity would force its squared slope to equal both numbers, which is impossible. Thus no bounded-state endpoint-local exact lift survives once a state block contains at least three coefficients.

### F.3 Quantitative affine no-go theorem

Suppose

\[
F_0(t)=\alpha t+\beta,\qquad
F_1(t)=\gamma t+\delta
\]

are used to lift a parent graph \(\Gamma\subseteq A^2\), \(|A|=n\), blockwise. The same-copy children scale \(Q\) by \(1\) and \(r^2\), while cross children scale it by \(q/3\) or \(3q\) according to old parity. Then

\[
\boxed{|\Gamma|\le\frac{n^2}{2}+n.}
\tag{F7}
\]

Here is the proof. A nonzero polynomial of total degree at most \(2\) has at most \(2n\) zeros on \(A^2\): writing it as a polynomial in \(Y\), the exceptional rows where it vanishes identically and the remaining rowwise zeros together total at most \(2n\). If \(|\Gamma|>2n\), the two same-copy identities must therefore hold as polynomial identities, which forces

\[
F_0(t)=\varepsilon t,\qquad F_1(t)=\eta rt
\]

for signs \(\varepsilon,\eta\). Let \(S_\Gamma=\Gamma\cap\Gamma^{\mathsf T}\). Then

\[
|S_\Gamma|\ge2|\Gamma|-n^2.
\]

On every \((x,y)\in S_\Gamma\), the two transposed cross descendants have the same required norm. Their difference is

\[
Q(\varepsilon x,\eta ry)-Q(\varepsilon y,\eta rx)
=(1-r^2)(x^2-y^2).
\]

Thus \(y=\pm x\), giving at most \(2n\) choices. Hence \(2|\Gamma|-n^2\le2n\), which proves (F7). Consequently every such affine recursion has parent deficit

\[
d\ge\frac{n^2}{2}-n,
\]

incompatible with PTCR. The same asymptotic conclusion persists if the four successor states are permuted according to parity: on dense symmetric parity blocks, the repeated cross multiplier is forced onto the two off-diagonal blocks, returning to the argument above.

### F.4 A fixed imperfect block cannot compose by products

If a length-\(k\) block has \(h\) coefficients and \(e<h^2\) engineered cells, then \(j\) independent repetitions have abstract parameters

\[
n=h^j,\qquad e_j=e^j,\qquad
\frac{e_j}{n^2}=\left(\frac e{h^2}\right)^j\longrightarrow0.
\tag{F8}
\]

For the complete six-point gadget, this density is \((16/36)^j=(4/9)^j\). For the five-point partial gadget with \(14\) codewords it is \((14/25)^j\), and it also loses a fraction \((14/16)^j\) of the codewords. Therefore no fixed imperfect block gives PTCR by ordinary graph/product composition.

Even the abstract product calculation is not automatically a real construction: a direct-product algebra has orthogonal idempotents, while a subfield of \(\mathbb R\) does not, and an ordinary digit embedding creates cross-coordinate terms in \(Q\). Treating coordinatewise products as scalar \(Q\)-values would assume the missing composition theorem.

There is a sharper inherited-endpoint obstruction for the partial core. Tensoring two or more core blocks forces coefficient magnitudes to be subset products. An edge differing in two coordinates \(i,j\) would require

\[
3q_iq_j
=3(r_i^2+r_i+1)(r_j^2+r_j+1),
\]

whereas its endpoint magnitudes \(1\) and \(r_ir_j\) give at most

\[
Q(1,r_ir_j)=r_i^2r_j^2+r_ir_j+1<3r_i^2r_j^2<3q_iq_j.
\]

Thus any composition retaining inherited endpoint labels fails already across two split coordinates. A successful composition must globally reassign those edges.

### F.5 Ordinary scalar digit composition also fails

The most direct attempt to turn a finite gadget into a real set is

\[
A_k(D;T)=\left\{\sum_{i=0}^{k-1}a_iT^i:a_i\in D\right\}.
\]

It does not preserve coordinatewise norms. If

\[
X(T)=\sum_i a_iT^i,\qquad Y(T)=\sum_i b_iT^i,
\]

then the coefficient of \(T^n\) in \(Q(X,Y)\) is

\[
\sum_{i+j=n}(a_ia_j+a_ib_j+b_ib_j).
\tag{F9}
\]

These cross-position polar terms restore essentially all pair information.

For the exact \(m=1\) alphabet \(D=\{1,2\}\) and transcendental \(T\), one can prove exactly

\[
Q(X,Y)=Q(U,V)\Longrightarrow \{X,Y\}=\{U,V\}.
\]

Indeed, modulo \(3\), equality gives

\[
(X-Y)^2=(U-V)^2.
\]

All difference coefficients lie in \(\{-1,0,1\}\), so reduction modulo \(3\) is injective on them and

\[
U-V=\pm(X-Y).
\]

Using

\[
4Q(X,Y)=3(X+Y)^2+(X-Y)^2
\]

then gives \(U+V=X+Y\), because the coefficient sums are positive. Hence

\[
\boxed{|Q(A_k(\{1,2\};T),A_k(\{1,2\};T))|
=\frac{N(N+1)}2,\qquad N=2^k.}
\tag{F10}
\]

For the six-point alphabet \(D=A_2\) from (C2), let \(N=6^k\), with \(k\ge2\). The digit set has three even and three odd elements, so reduction of the \(36\) symbols \(a-\omega b\) modulo the inert prime \(2\) is uniform on \(\mathbb F_4\), with \(9\) lifts of every residue. Put \(n=k-1\). There are \(3I_4(n)\) irreducible degree-\(n\) polynomials with arbitrary nonzero leading coefficient, and

\[
I_4(n)\ge\frac{4^n}{2n}.
\]

For \(n\ge2\), this follows directly from the exact formula by bounding the contribution of all proper-divisor terms by \(n4^{n/2}\le4^n/2\); \(n=1\) is immediate. Every residue coefficient vector has \(9^k\) lifts. The reduction criterion stated at the start makes every such lift irreducible over \(\mathbb Q(\omega)\). Thus at least

\[
\frac{3}{8(k-1)}36^k
\]

pairs have \(Z=X-\omega Y\) irreducible in \(\mathbb Q(\omega)[T]\). If

\[
W\bar W=Z\bar Z,
\]

unique factorization gives \(W=cZ\) or \(W=c\bar Z\). Choosing the leading digit of \(W\) gives at most \(36\) choices in either case, so such norm fibers have size at most \(72\). Therefore

\[
\boxed{
|Q(A_k(A_2;T),A_k(A_2;T))|
\ge\frac{N^2}{192(k-1)}.}
\tag{F11}
\]

The same proof works for the explicit carry-free integer base \(T_k=4056k+2\). Every coefficient in the difference of two possible norm polynomials has magnitude at most \(4056k\), so its highest nonzero base-\(T_k\) term dominates all lower terms; input digit expansions are also injective since their digit differences have magnitude at most \(51<T_k-1\). Thus neither the exact one-bit gadget nor the six-point two-bit gadget yields a fixed power saving through ordinary scalar digits.

### F.6 Robust no-go for the natural binary placement

The natural table itself cannot be repaired by deleting \(o(4^m)\) cells.

**Theorem.** Assume the \(q_i\) are distinct. For all sufficiently large \(m\), any partial real \(Q\)-table agreeing with \(T_m^+(x,y)\) at naturally indexed cells must omit \(\Omega(4^m)\) directed cells.

For independent uniform \(x,y,z\in\mathbb F_2^m\), write

\[
B_m(x,y)=\prod_i r_i^{2x_iy_i}q_i^{x_i\oplus y_i}.
\]

The random variable

\[
D=\log B_m(x,y)-\log B_m(x,z)
\]

is a sum of independent coordinate variables. With \(R_i=2\log r_i\) and \(P_i=\log q_i\), the \(i\)-th summand has law

\[
0\ (1/2),\qquad
\pm P_i\ (1/8\text{ each}),\qquad
\pm(R_i-P_i)\ (1/8\text{ each}).
\tag{F12}
\]

Fix \(h>2\log4\). Since the \(q_i\) are distinct, only \(O_h(1)\) of them satisfy \(P_i\le h\). For every remaining coordinate, any interval of length \(h\) captures at most \(3/4\) of the mass in (F12). Kolmogorov--Rogozin therefore gives

\[
\mathcal Q(D,h)=O(m^{-1/2}).
\]

The parity factor changes a log-difference only by \(-\log3,0,\log3\). Hence

\[
\Pr\bigl(
|\log T_m^+(x,y)-\log T_m^+(x,z)|\le\log4
\bigr)=O(m^{-1/2}).
\]

The same holds for the other two pairs of triangle edges. With probability \(1-O(m^{-1/2})\), the largest of the three prescribed norms exceeds four times the second largest.

But every real \(Q\)-triangle obeys the opposite inequality. Indeed, if \(|a|\ge|b|,|c|\), then

\[
\frac34a^2\le Q(a,b),Q(a,c)\le3a^2,
\qquad
Q(b,c)\le3a^2.
\]

Thus, if \(M_1\ge M_2\ge M_3\) are the three edge values,

\[
\boxed{M_1\le4M_2.}
\tag{F13}
\]

For large \(m\), at least half of the \(\binom{2^m}{3}\) unordered triples violate (F13) in the natural norm table. Avoiding a contradiction requires every such triangle to contain an unordered edge with **both** orientations omitted. One fully omitted unordered edge destroys at most \(2^m-2\) triangles and costs two directed cells. Hence, for all sufficiently large \(m\), the directed deficit is at least

\[
2\frac{\tfrac12\binom{2^m}{3}}{2^m-2}
=\frac{2^m(2^m-1)}6
=\Omega(4^m).
\tag{F14}
\]

Thus any surviving PTCR construction must use a genuinely nonlinear global permutation of the norm words.

---

## G. Cartesian deficit: exact bounds and the corrected recurrence

### G.1 Universal lower bound after Exact-PTCR fails

Every full carrier contains \(4^m\) distinct ordered pairs, so \(n_m\ge2^m\). By (B7), equality is impossible for \(m\ge2\). Therefore

\[
\boxed{
n_m\ge2^m+1,\qquad
d_m\ge(2^m+1)^2-4^m=2^{m+1}+1.}
\tag{G1}
\]

This lower bound is only linear in \(n_m\), so it is compatible with PTCR for every \(\xi<1\).

### G.2 An exact cube-shadow invariant that survives a power deficit

For a putative full realization \(\Gamma_m\subseteq A_m^2\), define

\[
X_i=\{a\in A_m:v_{r_i}(a)\ge1\},
\qquad
X_S=\bigcap_{i\in S}X_i.
\]

By (B2), the \(i\)-th code letter is \(r_i\) exactly when both endpoints lie in \(X_i\). Therefore, for every \(S\subseteq[m]\),

\[
\boxed{|\Gamma_m\cap(X_S\times X_S)|=4^{m-|S|}.}
\tag{G2}
\]

Since only \(d_m\) cells of \(A_m^2\) are outside \(\Gamma_m\),

\[
\boxed{
2^{m-|S|}\le|X_S|\le\sqrt{4^{m-|S|}+d_m}.}
\tag{G3}
\]

If \(d_m\le n_m^{2-\xi}\), then \(n_m=2^m(1+o(1))\). Inclusion-exclusion in (G3) shows that the membership vectors

\[
(\mathbf1_{X_1}(a),\dots,\mathbf1_{X_m}(a))
\]

are asymptotically uniform on every selected set of at most

\[
(\xi/3-\varepsilon)m
\]

coordinates. More precisely, for disjoint \(U,V\subseteq[m]\), \(|U|+|V|=k\),

\[
\frac1{n_m}
\#\{a:a\in X_i\ (i\in U),\ a\notin X_i\ (i\in V)\}
=2^{-k}+O(2^{-\xi m+2k+o(m)}).
\tag{G4}
\]

Relative to the main term \(2^{-k}\), the error is \(o(1)\) when \(3k<\xi m-o(m)\). This invariant survives arbitrary codeword permutations and arbitrary norm-one phases.

### G.3 Exact deficit identity

For any four-child recursion, regardless of how coefficients are chosen,

\[
d_{m+1}=n_{m+1}^2-4^{m+1}
=4d_m+n_{m+1}^2-4n_m^2.
\tag{G5}
\]

Writing

\[
n_{m+1}=2n_m+s_m
\]

gives

\[
\boxed{d_{m+1}=4d_m+4n_ms_m+s_m^2.}
\tag{G6}
\]

Equivalently, with \(\delta_m=d_m/n_m^2\) and \(\rho_m=n_{m+1}/(2n_m)\),

\[
\boxed{1-\delta_{m+1}=\frac{1-\delta_m}{\rho_m^2}.}
\tag{G7}
\]

If a nested construction always has \(n_{m+1}\ge2n_m\), then its engineered density can never increase. Starting from the exact seed, one strict enlargement creates a positive deficit density which persists unless a later step achieves \(n_{j+1}<2n_j\) and repairs old coefficient overhead.

### G.4 Correction to the proposed near-recursion criterion

The recurrence suggested in the prompt,

\[
d_{m+1}\le4d_m+O(n_m^{2-\delta}),
\tag{G8}
\]

does **not** imply a power saving. When \(n_m\asymp2^m\), direct iteration permits

\[
d_m
\ll4^m\sum_{j<m}2^{-\delta j}
=O(4^m)
=O(n_m^2).
\]

Early defects are reproduced by the factor \(4\) at every later scale.

A sufficient recurrence must contract inherited deficit:

\[
d_{m+1}\le\kappa d_m+C n_m^{2-\delta},
\qquad
\kappa<4.
\tag{G9}
\]

If \(n_m=2^{m+o(m)}\), iteration of (G9) gives

\[
d_m\le
n_m^{\max\{\log_2\kappa,\,2-\delta\}+o(1)}.
\]

Thus, allowing an arbitrarily small loss in the resonant case, every

\[
\boxed{
0<\xi<\min\{\delta,\,2-\log_2\kappa\}}
\tag{G10}
\]

is certified. Equivalently, if \(\kappa=2^{2-\eta}\), every \(\xi<\min\{\delta,\eta\}\) follows.

This is the exact quantitative composition threshold. Merely creating \(o(n_m)\) new labels per step is insufficient; the recursion must also merge enough old labels to make the effective coefficient of \(d_m\) strictly smaller than \(4\).

### G.5 Scorecard

| Construction | \(n_m\) | \(e_m\) | \(d_m\) or density | \(v_m\) |
|---|---:|---:|---:|---:|
| Frozen \(m=1\) gadget | \(2\) | \(4\) | \(0\) | \(3\) |
| Best full \(m=2\) carrier | \(6\) | \(16\) | \(20\) | \(9\) |
| Canonical edge lift at \(m=2\) | \(7\) | \(16\) | \(33\) | \(9\) |
| Subset-product partial core | \(2^m\) | \(2^m(m+1)\) | density \((m+1)/2^m\) | at most \(3^m\) |
| Explicit edge carrier | at most \(2\cdot4^m-3\cdot2^m\) | \(4^m\) | no near-Cartesian bound | \(3^m\) |
| Hypothetical PTCR | \(2^{m+o(m)}\) | \(4^m\) | at most \(n_m^{2-\xi}\) | \(3^m\) |

---

## H. Consequence for the ultimate target

No unconditional \(c>0\) follows from the constructions presently available.

Conditionally, suppose a future globally reassigning composition satisfies

\[
n_m=2^{m+o(m)}
\]

and the contraction recurrence (G9). Choose any

\[
0<\xi<\min\{\delta,\,2-\log_2\kappa\}.
\]

Then \(d_m\le n_m^{2-\xi}\) for all sufficiently large \(m\). The engineered pairs use exactly the \(3^m\) twisted norm values, while every unengineered cell contributes at most one further value. Therefore

\[
|Q(A_m,A_m)|\le3^m+d_m.
\]

Since \(n_m=2^{m+o(m)}\),

\[
3^m=n_m^{\log_2 3+o(1)}.
\]

Consequently every fixed

\[
\boxed{
0<c<\min\{2-\log_2 3,\,\xi\}}
\tag{H1}
\]

would yield

\[
|Q(A_m,A_m)|\le n_m^{2-c}
\]

for all sufficiently large \(m\). For a completely explicit safe choice under \(\kappa=2^{2-\eta}\), one may take

\[
\boxed{
c=\min\left\{
\frac{2-\log_2 3}{2},
\frac{\min\{\delta,\eta\}}4
\right\}>0.}
\tag{H2}
\]

The present exact edge carrier (F4) does not satisfy (G9), and the six-point block does not compose, so (H1) remains conditional.

---

## I. Exactly one next unresolved statement

The narrowest currently isolated statement that would definitively settle the surviving arbitrary-permutation branch is the following.

### Cube-shadow triangle-gap lemma

Fix \(\xi>0\). Then there should exist \(c(\xi)>0\) such that, for all sufficiently large \(m\), the following holds.

Let \(W_m\) be the parity-twisted norm-word multiset, with its numerical norm labels and inert-coordinate indicators. Let \(\Gamma\subseteq V^2\) have

\[
|\Gamma|=4^m,\qquad
|V|^2-4^m\le|V|^{2-\xi},
\]

and let \(\phi:\Gamma\to W_m\) be a bijection. Assume:

1. whenever both orientations of an unordered edge lie in \(\Gamma\), their numerical labels agree;
2. there are subsets \(X_i\subseteq V\) such that the \(i\)-th letter of \(\phi(a,b)\) is \(r_i\) exactly when \(a,b\in X_i\).

Then at least \(c(\xi)|V|^3\) complete unordered triangles have numerical edge labels whose largest value is more than four times their second largest.

Here “complete” means that each of the three unordered edges has at least one orientation in \(\Gamma\); assumption 1 makes its numerical label unambiguous when both orientations occur.

A PTCR realization satisfies assumptions 1--2 by symmetry and the exact inert-prime identity (G2), but a real \(Q\)-table satisfies the universal triangle inequality (F13). Therefore a proof of this one finite, permutation-invariant lemma would disprove PTCR completely. The natural-placement theorem proves the lemma when \(\phi\) is the natural binary assignment; the unresolved content is precisely whether arbitrary nonlinear reassignment can use the split-prime factors to eliminate almost all triangle gaps while retaining the cube-shadow constraints.
