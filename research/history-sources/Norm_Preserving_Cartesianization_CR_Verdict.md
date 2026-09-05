# Norm-preserving Cartesianization of the balanced four-state code

## Final verdict

All work in this report is offline. The frozen balanced-code facts are used as hypotheses and are not re-derived.

The Norm-Preserving Cartesianization Conjecture (CR) is **false**. The obstruction survives every edge-dependent rational norm-one multiplier, not merely coordinatewise or recursive rephasings.

> **Main theorem.** Let \(A\subset\mathbb Q\) be finite and let
> \[
> \Gamma\subseteq A^2
> \]
> be a set of distinct ordered pairs such that
> \[
> v_3(Q(a,b))=0
> \qquad((a,b)\in\Gamma).
> \]
> Then
> \[
> |\Gamma|\le \left\lfloor\frac{2|A|^2}{3}\right\rfloor.
> \tag{T1}
> \]
> For an injective norm-one rephasing of the balanced code, one has the stronger deficit estimate
> \[
> \boxed{
> |A|^2-4^m
> \ge \frac{|A|^2}{3}+2^m.
> }
> \tag{T2}
> \]

In particular, for every fixed \(\xi>0\),

\[
|A|^2-4^m\le |A|^{2-\xi}
\]

fails for all sufficiently large \(m\). This disproves CR and its almost-all variant.

This does **not** disprove the ultimate assertion that some unrelated sets \(A\subset\mathbb R\) may satisfy

\[
|Q(A,A)|\le |A|^{2-c}.
\]

It closes only the proposed norm-one Cartesianization of a code whose norms are all \(3\)-adic units.

The obstruction also forces a specific constructive pivot. A parity-dependent factor \(1-\omega\), of norm \(3\), removes the obstruction while preserving exactly the same \(4^m\)-to-\(3^m\) exponential profile. The final section states one precise successor conjecture.

## Standard facts used

No external source or unproved research theorem is used. The substantial standard facts required are the following.

1. **The normalized \(3\)-adic valuation.** For \(x,y\in\mathbb Q^\times\),
   \[
   v_3(xy)=v_3(x)+v_3(y),
   \]
   and if \(v_3(x)\ne v_3(y)\), then
   \[
   v_3(x+y)=\min\{v_3(x),v_3(y)\}.
   \]
   The proof below uses direct residue calculations whenever cancellation is possible.

2. **Fundamental theorem of arithmetic.** Distinct exponent vectors at the distinct rational primes \(q_i,r_i\) give distinct rational norm labels.

3. **Elementary quadratic inequality.** For nonnegative real numbers \(x,y,z\),
   \[
   x^2+y^2+z^2\ge \frac{(x+y+z)^2}{3}.
   \]

4. **Frozen Eisenstein arithmetic.** In \(E=\mathbb Z[\omega]\), where \(\omega^2+\omega+1=0\),
   \[
   N(a-\omega b)=a^2+ab+b^2=Q(a,b).
   \]
   The balanced code has \(4^m\) distinct elements, \(3^m\) distinct norm values, and exactly \(2^m\) norm values whose code fiber is a singleton.

The norm-one orbit observation below is proved directly, so Hilbert's Theorem 90 is not assumed.

## A. CR verdict

Let

\[
Z_m=
\left\{
\prod_{i=1}^m\theta_i:
\theta_i\in\{1,r_i,\pi_i,\bar\pi_i\}
\right\},
\]

with \(q_i=N(\pi_i)\equiv1\pmod3\) and \(r_i\equiv2\pmod3\), as in the frozen construction. Every \(q_i\) and \(r_i\) differs from \(3\), so

\[
v_3(N(z))=0
\qquad(z\in Z_m).
\tag{1}
\]

Suppose arbitrary multipliers

\[
u_z\in\mathbb Q(\omega)^\times,
\qquad N(u_z)=1,
\]

are chosen and the elements \(u_zz\) are pairwise distinct. Write

\[
u_zz=a_z-\omega b_z,
\qquad a_z,b_z\in\mathbb Q,
\]

and let

\[
A={a_z:z\in Z_m\}\cup\{b_z:z\in Z_m\}.
\]

Then

\[
v_3(Q(a_z,b_z))
=v_3(N(u_zz))
=v_3(N(z))
=0.
\tag{2}
\]

The main local lemma below shows that at most two thirds of \(A^2\) can satisfy (2). Hence

\[
4^m\le \frac23|A|^2
\tag{3}
\]

and already

\[
|A|^2-4^m\ge\frac13|A|^2.
\tag{4}
\]

The singleton-fiber argument sharpens (4) to (T2).

## B. Complete freedom of norm-one rephasing

The obstruction does not arise from using too narrow a parametrization of norm-one elements.

### Orbit lemma

Let \(z,w\in\mathbb Q(\omega)^\times\). Then

\[
N(w)=N(z)
\quad\Longleftrightarrow\quad
w=uz
\text{ for some }u\in\mathbb Q(\omega)^\times
\text{ with }N(u)=1.
\tag{5}
\]

Indeed, the forward implication follows by taking

\[
u=\frac wz,
\qquad
N(u)=\frac{N(w)}{N(z)}=1,
\]

and the reverse implication is multiplicativity of the norm.

Thus arbitrary norm-one rephasing is exactly the freedom to choose an arbitrary rational coefficient pair \((a,b)\) on the conic

\[
Q(a,b)=N(z).
\]

The proof of CR's failure therefore covers the full permitted search space.

### Exact one-coordinate example

For \(m=1\), choose

\[
r_1=2,
\qquad
q_1=7,
\qquad
\pi_1=2-\omega,
\qquad
\bar\pi_1=3+\omega.
\]

The coefficient set

\[
A_1=\{0,1,2\}
\]

realizes all four codewords through

\[
\begin{array}{c|c|c|c}
z & u_z & u_zz=a-\omega b & (a,b)\\
\hline
1 & 1 & 1 & (1,0)\\
2 & 1 & 2 & (2,0)\\
\pi_1 & 1 & 2-\omega & (2,1)\\
\bar\pi_1 & -\omega & 1-2\omega & (1,2)
\end{array}
\]

because \(-\omega(3+\omega)=1-2\omega\). All four multipliers have norm \(1\), and the four norms are

\[
1,\quad4,\quad7,\quad7.
\]

The lower bound proved below forces \(|A_1|\ge3\), so this example is optimal for \(m=1\). It does not tensor into a CR construction.

For general \(m\), the best explicit all-\(m\) rephasing established here is the trivial choice

\[
u_z=1\qquad(z\in Z_m).
\]

Its original coefficient completion supplies the unconditional upper bound

\[
|A_m|\le2\cdot4^m.
\tag{6}
\]

No all-\(m\) rephasing with coefficient exponent below \(\log4\) is established here.

## C. The exact \(3\)-adic structural lemma

Let \(v=v_3\), normalized by \(v(3)=1\), and set \(v(0)=+\infty\).

### Valuation classification

For \(a,b\in\mathbb Q\), not both zero, put

\[
h=\min\{v(a),v(b)\}.
\]

Write

\[
a=3^hA,
\qquad
b=3^hB,
\]

where \(A,B\in\mathbb Z_{(3)}\) and at least one of \(A,B\) is a \(3\)-adic unit. Then

\[
v(Q(a,b))=
\begin{cases}
2h,&A\not\equiv B\pmod3,\\[2mm]
2h+1,&A\equiv B\pmod3.
\end{cases}
\tag{7}
\]

To prove this, first note that

\[
Q(A,B)=A^2+AB+B^2\equiv(A-B)^2\pmod3.
\tag{8}
\]

If \(A\not\equiv B\pmod3\), the normalized form is a unit. If \(A\equiv B\pmod3\), then both are units. Writing \(B=A+3C\), one obtains

\[
Q(A,A+3C)
=3(A^2+3AC+3C^2),
\tag{9}
\]

and the factor in parentheses is a unit. Multiplication by \(3^{2h}\) proves (7).

Because \(h\in\mathbb Z\), neither \(2h\) nor \(2h+1\) can accidentally become \(0\) in an omitted case. In particular, if \(h<0\), neither possible valuation is zero. We therefore have the exact criterion

\[
\boxed{
v_3(Q(a,b))=0
\iff
a,b\in\mathbb Z_{(3)},\quad
\min\{v_3(a),v_3(b)\}=0,\quad
a\not\equiv b\pmod3.
}
\tag{10}
\]

This includes zero correctly: \(0\) may be the positive-valuation member of a pair with a unit, while \((0,0)\) never has unit norm.

### Tripartite form of all unit-norm pairs

Partition the \(3\)-integral elements of a finite \(A\subset\mathbb Q\) into

\[
A_+=\{a:v_3(a)=0,\ a\equiv1\pmod3\},
\]

\[
A_-=\{a:v_3(a)=0,\ a\equiv-1\pmod3\},
\]

and

\[
A_0=\{a:v_3(a)>0\}\cup(\{0\}\cap A).
\]

Elements of negative valuation have no incident pair satisfying \(v_3(Q)=0\). By (10), the unit-norm pairs are exactly the ordered pairs joining two different classes among

\[
A_+,\qquad A_-,\qquad A_0.
\]

If their sizes are \(x,y,z\), the number of such pairs is

\[
2(xy+xz+yz)
=(x+y+z)^2-(x^2+y^2+z^2)
\le\frac23(x+y+z)^2
\le\frac23|A|^2.
\tag{11}
\]

Since the left side is integral, (T1) follows. Equality is possible only when there are no negative-valuation elements and the three class sizes differ pairwise by at most one. Thus the constant \(2/3\) is sharp for unrestricted rational sets.

## D. Coefficient count and Cartesian deficit

For the balanced code, (T1) immediately gives

\[
|A|\ge\sqrt{\frac32}\,2^m.
\tag{12}
\]

There is a further forced omission that uses the precise code histogram.

Exactly \(2^m\) norm values have no split state: at every coordinate their local label is either \(1\) or \(r_i^2\). These norm values are distinct rational squares and each has exactly one codeword preimage.

Let \((a,b)\) be the engineered edge assigned to one of these singleton values. It is a unit-norm edge, so its endpoints lie in different \(3\)-adic classes and hence \(a\ne b\). Symmetry gives

\[
Q(b,a)=Q(a,b).
\]

The reverse cell \((b,a)\) cannot be another engineered edge: that would give a second codeword carrying a norm value whose code fiber has size one. The \(2^m\) reverse cells are pairwise distinct. They are unit-norm cells, so they are disjoint from all cells excluded by the tripartite valuation condition.

At least \(|A|^2/3\) cells have nonunit norm by (T1), and the singleton reversals contribute another \(2^m\) missing cells. Therefore

\[
\boxed{
|A|^2-4^m
\ge\frac{|A|^2}{3}+2^m.
}
\tag{13}
\]

Equivalently,

\[
\boxed{
|A|^2
\ge\frac32(4^m+2^m).
}
\tag{14}
\]

For \(m=1,2,3,4\), (14) gives the respective necessary coefficient counts

\[
3,\qquad6,\qquad11,\qquad21.
\]

The exponential coefficient lower bound remains \(2^{m+o(m)}\); the decisive point is the constant-density deficit, not an exponent gap in \(|A|\).

### Contradiction to CR

If CR held for some fixed \(\xi>0\), (4) alone would imply

\[
\frac13|A|^2\le |A|^{2-\xi},
\]

so

\[
|A|^\xi\le3.
\]

But injectivity gives \(|A|^2\ge4^m\), hence \(|A|\ge2^m\). Therefore

\[
m\le\frac{\log_2 3}{\xi},
\]

which excludes infinitely many unbounded \(m\).

The same proof rules out the almost-all version: every engineered subgraph with unit norm has at most \(2|A|^2/3\) edges and therefore can never occupy \((1-o(1))|A|^2\) cells.

### Common-scaling audit

The conjecture permits one common nonzero scaling after the rational coefficients are selected. Apply the proof to the unscaled rational coefficient set. Common scaling is a bijection on coefficient labels and ordered coefficient pairs, so it changes neither \(|A|\), the number of engineered edges, nor the Cartesian deficit. This remains true even if the common scalar is irrational. Hence scaling cannot evade (13).

## E. Rectangle mechanism: what actually fails

The obstruction is not a shortage of abstract rectangles. A balanced complete tripartite graph has positive edge density and contains many \(4\)-cycles. Rather, norm-one rephasing confines every engineered edge to its three off-diagonal \(3\)-adic blocks. The three diagonal blocks, comprising at least one third of the Cartesian square, can never be engineered.

Any actual coefficient rectangle

\[
(a_1,b_1),\quad(a_1,b_2),\quad(a_2,b_1),\quad(a_2,b_2)
\]

would give the additive identity

\[
(a_1-\omega b_1)+(a_2-\omega b_2)
=(a_1-\omega b_2)+(a_2-\omega b_1).
\]

The balanced unit-norm code may realize rectangles contained in cross-class blocks, but it cannot supply edges in the within-class blocks needed for an almost-complete coefficient graph. No additive carrier, denominator choice, or arbitrary cell reindexing can change this while every engineered norm remains a \(3\)-adic unit.

This precisely locates the failure: the old tensor-rank mismatch is unnecessary, and arbitrary edge-dependent norm-one phases do not help.

## F. Norm preservation and the forced constructive pivot

Put

\[
\lambda=1-\omega,
\qquad N(\lambda)=3.
\]

For \(z=\prod_i\theta_i\in Z_m\), let

\[
\ell(z)=
\#\{i:\theta_i\in\{\pi_i,\bar\pi_i\}\},
\]

and define

\[
\varepsilon(z)=
\begin{cases}
1,&\ell(z)\text{ is even},\\
0,&\ell(z)\text{ is odd}.
\end{cases}
\]

The **parity-twisted code** is

\[
Z_m^\sharp
=
\{\lambda^{\varepsilon(z)}z:z\in Z_m\}.
\tag{15}
\]

This is the smallest identified modification that removes the proved obstruction.

### Exact ledger for the twist

1. **Elements.** Since every \(z\in Z_m\) is prime to \(\lambda\), the \(\lambda\)-valuation distinguishes the two values of \(\varepsilon\). Within either value, multiplication by a fixed nonzero \(\lambda^\varepsilon\) is injective. Thus
   \[
   |Z_m^\sharp|=4^m.
   \]

2. **Norm values.** The integer \(\ell(z)\) is determined by the old norm word: it is the number of local labels \(q_i\). Therefore \(\varepsilon\) is constant on each old norm fiber. If \(t\) is an old norm value with \(\ell(t)\) split labels, its new value is
   \[
   3^{\mathbf1_{\ell(t)\text{ even}}}t.
   \]
   Distinct old values with the same parity remain distinct, while values with different parity have different \(3\)-adic valuations. Consequently
   \[
   \boxed{|N(Z_m^\sharp)|=3^m.}
   \tag{16}
   \]

3. **Fibers.** The twist is constant on every old norm fiber, so a norm word with \(\ell\) split coordinates still has exactly
   \[
   2^\ell
   \]
   codewords: at each split coordinate the two orientations \(\pi_i,\bar\pi_i\) are the only choices, while every nonsplit norm label determines its state uniquely. The typical realized-fiber exponent is unchanged.

Thus the twist repairs the ramified-prime obstruction at **zero exponential cost**.

### Why this parity is the correct one

Index the \(4^m\) state words by cells \((x,y)\in\mathbb F_2^m\times\mathbb F_2^m\), using at coordinate \(i\)

\[
(0,0)\mapsto1,
\qquad
(1,1)\mapsto r_i,
\qquad
(1,0)\mapsto\pi_i,
\qquad
(0,1)\mapsto\bar\pi_i.
\tag{17}
\]

Then

\[
\ell(z)=d_H(x,y).
\]

Color the formal vertex \(x\) by the parity of \(|x|\). The vertices \(x,y\) have the same color exactly when \(d_H(x,y)\) is even. The twist therefore assigns

\[
v_3(N)=1
\quad\text{to same-color cells},
\qquad
v_3(N)=0
\quad\text{to opposite-color cells}.
\]

This is exactly the valuation pattern of \(Q\) on a set of \(3\)-adic units split between its two nonzero residue classes: same-residue pairs have valuation \(1\), and opposite-residue pairs have valuation \(0\).

The array (17) solves the abstract state-word grouping problem. It does **not** by itself create rational coefficient labels or the additive rectangle identities; that is the remaining arithmetic problem.

This profile is also forced asymptotically. Exactly half of the \(4^m\) twisted codewords have even \(\ell\), hence norm valuation \(1\), and half have odd \(\ell\), hence norm valuation \(0\). Suppose a realization had deficit \(o(|A|^2)\). Elements of negative valuation have no incident pair of valuation \(0\) or \(1\), so their number is \(o(|A|)\). The class of elements of positive valuation, including zero, also has size \(o(|A|)\), because every pair internal to that class has norm valuation at least \(2\). If \(x,y\) are the sizes of the two remaining unit residue classes, the valuation-zero edges number \((1/2+o(1))|A|^2\) and can occupy only

\[
2xy+o(|A|^2)
\]

cells. Since \(x+y=(1+o(1))|A|\) and \(2xy\le(x+y)^2/2\), equality is forced asymptotically:

\[
x=y=(1/2+o(1))|A|.
\]

Thus the parity twist matches the unique possible first-level \(3\)-adic profile of any near-Cartesian realization; it is not merely sufficient to evade the earlier upper bound.

### Exact \(m=1\) twisted Cartesianization

With \(r_1=2\) and \(q_1=7\), the twisted norm multiset is

\[
3,\quad12,\quad7,\quad7.
\]

It is exactly the full \(Q\)-table on

\[
A=\{1,2\}:
\qquad
\bigl(Q(a,b)\bigr)_{a,b\in A}
=
\begin{pmatrix}
3&7\\
7&12
\end{pmatrix}.
\tag{18}
\]

At the element level,

\[
\lambda\mapsto1-\omega,
\qquad
2\lambda\mapsto2-2\omega,
\qquad
\pi_1\mapsto2-\omega,
\qquad
\bar\pi_1\mapsto1-2\omega,
\]

where the final map uses the norm-one phase \(-\omega\). Hence the successor construction is exactly Cartesian for one coordinate. No claim of tensorization is made.

## G. Consequence for \(Q(A,A)\)

For the original norm-one code, write

\[
d_m=|A_m|^2-4^m.
\]

The only general direct image estimate supplied by engineered versus unengineered pairs is

\[
|Q(A_m,A_m)|\le3^m+d_m.
\tag{19}
\]

But (13) gives

\[
d_m\ge\frac13|A_m|^2+2^m.
\]

Therefore (19), as a certificate, necessarily retains a quadratic-size error term. This is an obstruction to the certificate, not a lower bound on \(|Q(A_m,A_m)|\): the unengineered pairs might have additional coincidences not controlled by this argument.

Accordingly, the ultimate real-set problem remains open in this report.

For the parity-twisted code, a CR-type Cartesianization would again give

\[
|Q(A_m,A_m)|
\le3^m+|A_m|^{2-\xi},
\tag{20}
\]

because (16) preserves exactly \(3^m\) engineered values.

## H. Final exponent

There is no positive exponent \(c\) obtained from original CR, because CR is false.

Conditionally on a power-saving Cartesianization of the parity-twisted code, one has

\[
|A_m|=2^{m+o(m)}
\]

and hence

\[
3^m=|A_m|^{\log_2 3+o(1)}.
\]

Combining this with (20), every fixed

\[
\boxed{
0<c<\min\{2-\log_2 3,\xi\}
}
\tag{21}
\]

would work for all sufficiently large members of the sequence. The intrinsic numerical ceiling remains

\[
2-\log_2 3=0.415037\ldots.
\]

## I. Exactly one next statement

The original CR is resolved negatively. The single successor statement closest to it is the following.

> **Parity-Twisted Cartesianization Conjecture (PTCR).** There exist \(\xi>0\) and infinitely many \(m\) such that one can choose, for every \(z^\sharp\in Z_m^\sharp\), a multiplier
> \[
> u_{z^\sharp}\in\mathbb Q(\omega)^\times,
> \qquad N(u_{z^\sharp})=1,
> \]
> for which the elements \(u_{z^\sharp}z^\sharp\) are pairwise distinct and, writing
> \[
> u_{z^\sharp}z^\sharp=a_z-\omega b_z,
> \]
> their common coefficient completion
> \[
> A_m=\{a_z\}\cup\{b_z\}
> \]
> satisfies
> \[
> \boxed{
> |A_m|^2-4^m\le |A_m|^{2-\xi}.
> }
> \tag{PTCR}
> \]

PTCR differs from the false conjecture by only the parity-dependent ramified factor in (15). It retains \(4^m\) code elements, exactly \(3^m\) norm values, and the same realized-fiber multiplicities. By (20)--(21), a proof of PTCR would immediately yield

\[
|Q(A_m,A_m)|\le |A_m|^{2-c}
\]

for every fixed

\[
0<c<\min\{2-\log_2 3,\xi\}.
\]

This is the unique constructive next step identified by the present obstruction.
