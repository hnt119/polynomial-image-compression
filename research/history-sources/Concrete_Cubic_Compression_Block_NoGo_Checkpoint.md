# Concrete Cubic Compression: Finite-Block No-Go Checkpoint

*Offline, source-disciplined report — 3 September 2026*

## A. Verdict

**Verdict 5: the complete finite-block conjecture is disproved.**

This does **not** disprove the Concrete Cubic Compression Conjecture for

\[
P_3(x,y)=(x-y)^3+x+y.
\]

The frozen quadratic power-saving construction remains valid and is unaffected. The new result disproves the proposed cubic archimedean proof mechanism in every dimension. More precisely, let \(W\subset\mathbb R^m\) be any bounded Borel set of positive volume \(V\), and let

\[
\mathcal P_m(W)=
\{(x-y)^{\circ3}+x+y:x,y\in W\}.
\]

Then

\[
\boxed{
N_1(\mathcal P_m(W))
>
\left(\frac{\sqrt3}{\pi}\right)^mV^2.
}
\tag{A.1}
\]

Consequently every proposed cover by \(\widehat N\) unit cubes has

\[
R_{\max}(W)
:=
\left(\frac{V^2}{\widehat N}\right)^{1/m}
<\frac{\pi}{\sqrt3}.
\tag{A.2}
\]

The totally real tower in `unit-distance-proof.pdf` has root-discriminant bound \(R>\pi/\sqrt3\). Hence its proposed rate always satisfies

\[
\eta=\frac{R^m\widehat N}{V^2}
>
\left(\frac{R\sqrt3}{\pi}\right)^m
>1.
\tag{A.3}
\]

Thus no finite union of rational boxes can be a successful cubic cancellation block. In fact, connectedness, convexity, product structure, rationality, and the number of components are irrelevant to the obstruction.

The earlier block-to-set implication remains correct: **if** \(\eta<1\), it would yield a power-saving real sequence. The new result shows that its hypothesis cannot hold. The obstruction also closes any degree-dependent Minkowski-window method whose input count uses only volume divided by covolume and whose output count uses only a continuous unit-cube cover followed by algebraic norm separation. It does not control the actual image of a sparse lattice subset and therefore does not settle the original discrete conjecture.

## B. Exact conjecture and value

### B.1. Quantifiers and pair-count normalization

The headline conjecture is:

\[
\exists c_3>0\ \forall N_0\ge1\ \exists A\subset\mathbb R
\quad
\bigl(
A\text{ finite},\ |A|\ge N_0,
\ |P_3(A,A)|\le |A|^{2-c_3}
\bigr).
\tag{B.1}
\]

Since \(A^2\) contains \(|A|^2\) ordered pairs, this is equivalently

\[
|P_3(A,A)|
\le (|A|^2)^{1-\varepsilon_3},
\qquad
\varepsilon_3=c_3/2>0.
\]

No result below proves or disproves (B.1). What is disproved is the finite positive-volume block proposed as its next proof mechanism.

### B.2. The unavoidable linear floor

Let \(P\in\mathbb R[x,y]\) be nonconstant. Suppose first that \(d=\deg_yP\ge1\), and write

\[
P(x,y)=p_0(x)+p_1(x)y+\cdots+p_d(x)y^d,
\qquad p_d\ne0.
\]

The exceptional first coordinates are exactly

\[
E_P=
\{a\in\mathbb R:P(a,y)\text{ is constant in }y\}
=
\bigcap_{r=1}^d\{a:p_r(a)=0\}.
\]

They form a finite set because \(E_P\subseteq\{a:p_d(a)=0\}\). If \(|A|>|E_P|\), choose \(a\in A\setminus E_P\). The polynomial \(P(a,y)\) is nonconstant of degree at most \(d\); the elementary root bound therefore gives

\[
|P(A,A)|
\ge |P(a,A)|
\ge\left\lceil\frac{|A|}{d}\right\rceil.
\tag{B.2}
\]

If \(\deg_yP=0\), then \(P(x,y)=q(x)\) for a nonconstant polynomial \(q\), and

\[
|P(A,A)|=|q(A)|\ge\frac{|A|}{\deg q}.
\]

Thus \(|P(A,A)|\gg_P|A|\) for every sufficiently large finite \(A\). For \(P_3\), the coefficient of \(y^3\) is \(-1\), so the preceding argument already has no exceptional coordinates. In fact, fixing any \(b\in A\) gives the stronger bound because

\[
\frac{\partial P_3}{\partial x}(x,b)=1+3(x-b)^2>0.
\]

The map \(x\mapsto P_3(x,b)\) is strictly increasing, and therefore

\[
\boxed{|P_3(A,A)|\ge |A|}
\tag{B.3}
\]

for every nonempty finite \(A\). Exponent \(1\) is therefore an unavoidable floor; the meaningful target is \(2-c_3\), not \(1-c_3\).

### B.3. Polynomial non-speciality

Here “polynomial special form” means precisely one of

\[
P(x,y)=f(g(x)+h(y))
\quad\text{or}\quad
P(x,y)=f(g(x)h(y)),
\tag{B.4}
\]

where \(f,g,h\in\mathbb R[t]\) are all nonconstant. No external incidence theorem and no novelty claim are attached to this internal algebraic check.

Suppose first that \(P_3=f(g+h)\). Put

\[
r=\deg f,\qquad p=\deg g,\qquad q=\deg h.
\]

Comparison of total degrees gives

\[
3=r\max\{p,q\}.
\]

If \(r=1\), then \(f(g(x)+h(y))\) has no mixed monomial, contradicting the nonzero \(x^2y\) and \(xy^2\) terms of \((x-y)^3\). Otherwise \(r=3\) and \(p=q=1\). Write

\[
g(x)=\alpha x+\beta,
\qquad
h(y)=\gamma y+\delta,
\qquad
\alpha\gamma\ne0.
\]

If \(a\) is the leading coefficient of \(f\), equality of degree-three homogeneous parts gives

\[
a(\alpha x+\gamma y)^3=(x-y)^3.
\]

Hence \(\gamma=-\alpha\), and the whole composition depends only on \(x-y\). This is impossible because

\[
P_3(0,0)=0,
\qquad
P_3(1,1)=2.
\]

Now suppose that \(P_3=f(gh)\). Degree comparison gives

\[
3=r(p+q).
\]

Since \(p,q\ge1\), necessarily \(r=1\) and \(p+q=3\). The top homogeneous part of \(f(g(x)h(y))\) is then one mixed monomial \(cx^py^q\). It cannot equal

\[
(x-y)^3=x^3-3x^2y+3xy^2-y^3.
\]

Therefore \(P_3\) belongs to neither class in (B.4).

## C. Source transfer

### C.1. Source discipline and exact tower constant

The formal unit-distance authority is `unit-distance-proof.pdf`. The remarks are used only as a separate human-verified aid, and the chain-of-thought document only as a discovery record. The frozen Phase-A reconstruction and its change log are the available sum-product authorities. The conclusions of `Cubic_Difference_Sum_Research_Checkpoint.md` are treated as frozen except where this report explicitly advances or corrects them.

In Proposition 3.8 of the formal unit-distance proof, let

\[
r_1<\cdots<r_\ell
\]

be the first \(\ell\) rational primes congruent to \(1\pmod3\), and set

\[
D_\ell=\prod_{i=1}^{\ell}r_i.
\]

The cyclic cubic base field \(F\) has

\[
|\Delta_F|=D_\ell^2.
\]

Every totally real tower layer \(L_j/F\) is everywhere unramified. The relative discriminant formula therefore gives the exact value

\[
\boxed{
R=\sup_j\operatorname{rd}(L_j)
=\operatorname{rd}(F)
=D_\ell^{2/3}.
}
\tag{C.1}
\]

The source does not specify numerical values for its Shafarevich or class-number constants, so it does not identify one explicit admissible \(\ell\) and hence does not provide a single numerical upper bound for \(R\). That omission is immaterial to the no-go theorem: only a universal lower bound for \(R\) is needed.

The tower degrees have the form

\[
d_j=[L_j:\mathbb Q]=3^{a_j+1},
\qquad a_j\to\infty,
\tag{C.2}
\]

because \([F:\mathbb Q]=3\) and \(L_j/F\) has finite \(3\)-group Galois group.

### C.2. Unit-distance mechanism being transferred

The unit-distance construction has the following exact architecture.

1. An unramified totally real tower keeps the root discriminant fixed while the degree grows.
2. Fixed rational primes split completely at every level, producing linearly many prime-ideal coordinates.
3. Binary choices among conjugate prime ideals provide exponentially many norm-one directions; a class-group fibre retains an exponential subfamily.
4. Haar averaging turns one finite overlap ratio into an exponential overlap gain across all embeddings.
5. Fixed-denominator norm separation supplies an exponential point-count ceiling.
6. An exponential gain in the field degree is converted into a fixed power of the final set size.

The proposed cubic block was intended to replace step 4: one block with \(\eta<1\) would tensor to \(\eta^k\). The decisive difference is that unit distance needs many selected edges, while cubic compression needs an upper bound for the image of **every** ordered pair.

### C.3. Sum-product mechanism being transferred

The frozen Phase-A reconstruction builds \(A=GP\) in a totally real field. An additive Minkowski box \(P\) supplies many inputs, a bounded-distortion unit box \(G\) has small multiplicative doubling, and directness of \(G\times P\to GP\) makes \(|A|=|G||P|\). The exact factorization

\[
AA=(GG)(PP)
\]

then makes the per-degree multiplicative gain compete against discriminant, regulator, height, and multiplicity costs. Tensorization or degree-to-power conversion begins only after the complete rate base is strictly below \(1\).

For the cubic block the analogous ledger is

\[
\eta=
\frac{
R^m\times\text{complete output-cover cost}
}{
\text{input-volume squared}
}.
\]

The universal specialization bound proves that this base is always above \(1\). Thus the transfer fails at the finite gain stage, before tensorization.

### C.4. Exact dictionary

| Source feature | Role in its source proof | Cubic block analogue | Audited outcome |
|---|---|---|---|
| Finite local seed | Disc overlap or small \(GG/G^2\) ratio | One set \(W\) with \(\eta<1\) | Impossible by (A.1) |
| Product over embeddings | Exponential amplification | \(W^k\) and \(\mathcal P_m(W)^k\) | Algebraically valid |
| Lattice averaging | Inputs from volume/covolume | \(\lvert B\rvert\ge V^k/R^{mk/2}\) | Valid but insufficient |
| Norm separation | Bounds lattice points in small cells | At most one output per unit cube | Valid but the cover is too large |
| Degree-to-power step | Converts \(e^{-\kappa d}\) to \(\lvert A\rvert^{-c}\) | \(c=\log(1/\eta)/\log K\) | Valid only hypothetically; \(\eta>1\) |
| Selected relations | Enough unit edges | Would need all Cartesian pairs | Cannot be transferred |

## D. Amplification proof

This section audits the conditional implication even though Section F proves that its hypothesis is false.

### D.1. Exact tensor case

Let \(W\subset\mathbb R^m\) be a bounded Borel set with

\[
V=\operatorname{vol}(W)>0,
\qquad
K=N_1(W),
\]

and suppose an explicit cover of \(\mathcal P_m(W)\) by \(\widehat N\) half-open unit cubes is given. Assume first that \(d_j=mk_j\), and put

\[
\Omega_j=W^{k_j}\subset\mathbb R^{d_j}.
\]

Let \(\Phi_j(\mathcal O_{L_j})\) be the real Minkowski lattice. Its covolume is

\[
\sqrt{|\Delta_{L_j}|}\le R^{d_j/2}.
\]

Haar averaging on the lattice torus gives a translate \(t_j+\Omega_j\) whose lattice section

\[
B_j=
\{\alpha\in\mathcal O_{L_j}:
\Phi_j(\alpha)\in t_j+\Omega_j\}
\]

satisfies

\[
|B_j|
\ge
\frac{V^{k_j}}{\sqrt{|\Delta_{L_j}|}}
\ge
\left(\frac{V}{R^{m/2}}\right)^{k_j}.
\tag{D.1}
\]

A translate of a half-open unit \(d_j\)-cube contains at most one embedded algebraic integer. Indeed, the difference of two such integers would be nonzero while every real conjugate had absolute value \(<1\), contradicting that its algebraic norm is a nonzero integer. A product of \(K\)-cube covers of \(W\) therefore gives

\[
|B_j|\le K^{k_j}.
\tag{D.2}
\]

If

\[
\Phi_j(\alpha)=t_j+x,
\qquad
\Phi_j(\beta)=t_j+y,
\qquad
x,y\in W^{k_j},
\]

then

\[
\Phi_j(P_3(\alpha,\beta))
=2t_j+(x-y)^{\circ3}+x+y.
\tag{D.3}
\]

Coordinate independence gives the exact identity

\[
\mathcal P_{mk_j}(W^{k_j})
=\mathcal P_m(W)^{k_j}.
\tag{D.4}
\]

The product output cover and the same norm-separation argument imply

\[
|P_3(B_j,B_j)|\le\widehat N^{k_j}.
\tag{D.5}
\]

For any real embedding \(\sigma_1:L_j\hookrightarrow\mathbb R\), set

\[
A_j=\sigma_1(B_j).
\]

The embedding is an injective field homomorphism, so it preserves both input and polynomial-image cardinalities. If

\[
\eta=\frac{R^m\widehat N}{V^2}<1,
\tag{D.6}
\]

then (D.1) and (D.5) give

\[
\frac{|P_3(A_j,A_j)|}{|A_j|^2}\le\eta^{k_j}.
\tag{D.7}
\]

Since \(\widehat N\ge1\), (D.6) implies \(V>R^{m/2}\), so \(|A_j|\to\infty\). Moreover \(K>1\), and with

\[
c_0=\frac{\log(1/\eta)}{\log K}>0,
\tag{D.8}
\]

the direction of the final comparison is

\[
\eta^{k_j}=K^{-c_0k_j}
\le |A_j|^{-c_0},
\]

because \(|A_j|\le K^{k_j}\) and the exponent is negative. Hence

\[
|P_3(A_j,A_j)|\le |A_j|^{2-c_0}.
\tag{D.9}
\]

The diagonal inclusion \(2W\subseteq\mathcal P_m(W)\) also shows that a genuine block would automatically have \(c_0\le1\), consistently with the linear floor in (B.3).

### D.2. Sharp divisibility audit

For the pure tensor proof, the exact requirement is an unbounded subsequence with

\[
d_j=mk_j,
\qquad k_j\to\infty.
\]

It is not necessary that \(m\) itself occur as a tower-stage degree or that a degree-\(m\) subfield exist. Because the tower is nested, it is enough that \(m\) divide one tower degree; it then divides every later degree. From (C.2), the dimensions that divide a cofinal tail are exactly

\[
\boxed{m=3^a\quad(a\ge0).}
\tag{D.10}
\]

In particular, \(m=2\) is not admissible for a pure tensor along this tower.

There is, however, no divisibility restriction if one only wants some fixed positive exponent. For arbitrary \(m\), write

\[
d_j=mk_j+r_j,
\qquad 0\le r_j<m,
\]

and use

\[
\Omega_j=W^{k_j}\times[0,1)^{r_j}.
\]

Since

\[
\mathcal P_{r_j}([0,1)^{r_j})\subset[0,2)^{r_j},
\]

the preceding proof becomes

\[
|A_j|
\ge
\frac{V^{k_j}}{R^{(mk_j+r_j)/2}},
\qquad
|A_j|\le K^{k_j},
\qquad
|P_3(A_j,A_j)|\le\widehat N^{k_j}2^{r_j}.
\]

Thus

\[
\frac{|P_3(A_j,A_j)|}{|A_j|^2}
\le(2R)^{r_j}\eta^{k_j}.
\tag{D.11}
\]

If the impossible hypothesis \(\eta<1\) held, then for all sufficiently large \(j\),

\[
(2R)^{r_j}\eta^{k_j}
\le\eta^{k_j/2}
\le |A_j|^{-c_0/2}.
\]

So arbitrary \(m\) would suffice with the explicit safe exponent \(c_0/2\). The earlier stage-degree requirement was overstrong, but this correction cannot evade the universal obstruction.

## E. Explicit finite block

No endpoint table can satisfy the required inequality, and no successful cover exists: Section F proves that every bounded positive-volume Borel block violates the required strict inequality. A zero-volume union cannot work either, since its input-volume square is zero while \(\widehat N\ge1\) for a nonempty image.

An exact-rational discovery search was nevertheless run before the universal proof was frozen. It checked \(9{,}609\) candidates in dimensions \(1,2,3\), including single boxes, Boolean and ternary code families, parity and low-weight codes, translations, unequal widths, and non-Cartesian unions. Dimension \(2\) was treated only diagnostically because of (D.10). The best searched admissible \(m=3\) enclosure was

\[
W=[5/28,37/28)^3,
\qquad
V=\frac{512}{343},
\]

with

\[
\mathcal P_3(W)
\subset
[5/686,2053/686]^3
\subset[0,3)^3.
\]

Thus \(\widehat N=27\) and

\[
R_{\max}(W)
=\left(\frac{V^2}{27}\right)^{1/3}
=\frac{64}{147}
<1.
\]

This search is evidence only and is not used in the proof. Once (A.1) was established, the stopping rule correctly terminated further optimization.

## F. Full-image audit

### F.1. The two preliminary necessary tests

For the finite unions of rational boxes required by the prompt, the polynomial images and difference sets below are Lebesgue measurable.

The diagonal is

\[
P_3(x,x)=2x,
\]

so \(2W\subseteq\mathcal P_m(W)\). A cover by \(N\) half-open unit cubes has union volume at most \(N\); consequently

\[
N_1(\mathcal P_m(W))
\ge2^mV.
\tag{F.1}
\]

Thus \(\eta<1\) would require

\[
V>(2R)^m.
\]

For the difference-volume test, define

\[
T(x,y)=(d,z)
=\bigl(x-y,(x-y)^{\circ3}+x+y\bigr).
\]

In each coordinate the Jacobian determinant is

\[
\det
\begin{pmatrix}
1&-1\\
3d_i^2+1&1-3d_i^2
\end{pmatrix}
=2.
\]

The inverse is

\[
x=\frac{z-d^{\circ3}+d}{2},
\qquad
y=\frac{z-d^{\circ3}-d}{2}.
\]

Hence \(T\) is globally bijective and

\[
2^mV^2
=\operatorname{vol}_{2m}(T(W\times W))
\le
\operatorname{vol}(W-W)\operatorname{vol}(\mathcal P_m(W)).
\tag{F.2}
\]

Together with \(N_1(\mathcal P_m(W))\ge\operatorname{vol}(\mathcal P_m(W))\), hypothetical success would require

\[
\operatorname{vol}(W-W)>(2R)^m.
\]

Both preliminary tests are correct, but neither sees the fatal fixed-specialization obstruction.

### F.2. Exact ordered-box ranges

For completeness, let

\[
I=[a,b),
\qquad
J=[c,d),
\qquad
f(u,v)=(u-v)^3+u+v.
\]

Since

\[
\partial_uf(u,v)=1+3(u-v)^2>0,
\]

the lower endpoint of the scalar image is obtained on \(u=a\), and its upper endpoint on \(u=b\), interpreted as an infimum and supremum for half-open boxes. Define

\[
E(q;[c,d])=
\{c,d\}\cup
\bigl(\{q-1/\sqrt3,q+1/\sqrt3\}\cap[c,d]\bigr).
\]

Then the exact closed range envelope is

\[
\left[
\min_{v\in E(a;[c,d])}f(a,v),
\ 
\max_{v\in E(b;[c,d])}f(b,v)
\right].
\tag{F.3}
\]

This checks both boundary values and the critical lines \(u-v=\pm1/\sqrt3\). For two ordered half-open axis boxes, the image is contained in, and its closure equals, the Cartesian product of the closed envelopes (F.3). Thus an interval-certified search can cover every ordered component pair, not merely diagonal component pairs.

For a single interval of length \(s\), the exact image length simplifies to

\[
2\max\{s,s^3\}.
\tag{F.4}
\]

Therefore a single \(m\)-box with side lengths \(s_i\) satisfies

\[
\operatorname{vol}(\mathcal P_m(W))
=\prod_{i=1}^m2\max\{s_i,s_i^3\},
\]

and its normalized factor is at least

\[
\prod_{i=1}^m
2R\max\{s_i,s_i^{-1}\}
\ge(2R)^m.
\tag{F.5}
\]

### F.3. Universal fixed-specialization theorem

Let \(W\subset\mathbb R^m\) be bounded Borel with \(V>0\), and fix any \(y\in W\). Define

\[
\Phi_y(x)=(x-y)^{\circ3}+x+y.
\]

Each scalar coordinate map is strictly increasing and onto \(\mathbb R\). Hence \(\Phi_y\) is a global \(C^1\)-diffeomorphism with positive Jacobian

\[
J_y(x)
=\det D\Phi_y(x)
=\prod_{i=1}^m\bigl(1+3(x_i-y_i)^2\bigr).
\tag{F.6}
\]

The fixed-input slice satisfies

\[
\Phi_y(W)\subseteq\mathcal P_m(W).
\tag{F.7}
\]

The change-of-variables theorem and Cauchy–Schwarz give

\[
\begin{aligned}
V^2
&=
\left(
\int_WJ_y(x)^{1/2}J_y(x)^{-1/2}\,dx
\right)^2\\
&\le
\left(\int_WJ_y(x)\,dx\right)
\left(\int_WJ_y(x)^{-1}\,dx\right)\\
&=
\operatorname{vol}(\Phi_y(W))
\left(\int_WJ_y(x)^{-1}\,dx\right).
\end{aligned}
\tag{F.8}
\]

By Tonelli's theorem and translation invariance,

\[
\begin{aligned}
\int_WJ_y(x)^{-1}\,dx
&<
\int_{\mathbb R^m}
\prod_{i=1}^m
\frac{dx_i}{1+3(x_i-y_i)^2}\\
&=
\prod_{i=1}^m
\int_{\mathbb R}\frac{dt}{1+3t^2}
=
\left(\frac{\pi}{\sqrt3}\right)^m.
\end{aligned}
\tag{F.9}
\]

The inequality is strict because \(W\) is bounded and the integrand is positive on its complement. Combining (F.7)–(F.9), every unit-cube cover of the **complete** image also covers \(\Phi_y(W)\), so

\[
\boxed{
\widehat N
\ge\operatorname{vol}(\Phi_y(W))
>
\left(\frac{\sqrt3}{\pi}\right)^mV^2.
}
\tag{F.10}
\]

This proof does not need measurability of the full continuous image: it uses the measurable diffeomorphic slice \(\Phi_y(W)\). It cannot omit a cross-image or reverse a collision inequality. A single fixed-\(y\) slice is a subset of the full image, and a lower bound for that slice is automatically a lower bound for every full-image cover.

## G. Gain-versus-cost ledger

### G.1. Fatal rate

For any proposed block, the complete ledger is

| Quantity | Exact value or bound | Role |
|---|---:|---|
| Input volume | \(V=\operatorname{vol}(W)\) | pair resource \(V^2\) |
| Input cover | \(K=N_1(W)\ge V\) | hypothetical degree-to-power denominator |
| Output cover | \(\widehat N>(\sqrt3/\pi)^mV^2\) | universal specialization cost |
| Tower cost | \(R^m\) | lattice covolume squared |
| Net base | \(\eta=R^m\widehat N/V^2\) | must be \(<1\) |
| Threshold | \(R_{\max}(W)=(V^2/\widehat N)^{1/m}<\pi/\sqrt3\) | root-discriminant threshold for the displayed cover |

The exact source formula (C.1) has no numerically specified upper value because the admissible \(\ell\) is not made effective. A rigorous lower bound is enough. Minkowski's discriminant theorem for a totally real cubic field gives

\[
\sqrt{|\Delta_F|}
\ge\frac{3^3}{3!}=\frac92,
\]

and hence

\[
R=\operatorname{rd}(F)
\ge\left(\frac92\right)^{2/3}
>2
>\frac{\pi}{\sqrt3}.
\tag{G.1}
\]

The last strict comparison follows, for example, from \(\pi<22/7<2\sqrt3\). Alternatively, (C.1) and \(r_1=7\) give \(R\ge7^{2/3}>3>\pi/\sqrt3\). Therefore

\[
\boxed{
\eta
>
\left(\frac{R\sqrt3}{\pi}\right)^m
>1
}
\tag{G.2}
\]

for every \(m\). There is no resulting positive \(c_3\); formula (D.8) would have a negative numerator.

More generally, if \(K\) is any totally real field of degree \(d\ge2\), Minkowski gives

\[
\operatorname{rd}(K)
\ge
\left(\frac{d^d}{d!}\right)^{2/d}
\ge2
>\frac{\pi}{\sqrt3}.
\]

For \(d=2\) the middle inequality is equality. For \(d\ge3\), the arithmetic–geometric mean bound \((d!)^{1/d}\le(d+1)/2\le d/\sqrt2\) proves it.

Thus the same volume-cover certificate fails in every totally real field of degree at least \(2\), not only in the supplied tower.

### G.2. Standard-theorem and hypothesis audit

| Result used | Precise form | Hypothesis check |
|---|---|---|
| Univariate root bound | A nonzero degree-\(d\) real polynomial has at most \(d\) real roots | Applied only to nonconstant specializations |
| Relative discriminant formula | \(\lvert\Delta_M\rvert=\lvert\Delta_F\rvert^{[M:F]}N_{F/\mathbb Q}(\mathfrak d_{M/F})\) | \(L_j/F\) is everywhere unramified, so the relative discriminant is trivial |
| Minkowski covolume | The real canonical embedding of \(\mathcal O_L\) has covolume \(\sqrt{\lvert\Delta_L\rvert}\) | Every \(L_j\) is totally real |
| Haar/Blichfeldt averaging | The mean number of lattice points in a translated bounded measurable set is volume divided by covolume | Applied to bounded Borel products \(\Omega_j\) |
| Algebraic norm separation | A nonzero algebraic integer has nonzero integral norm of absolute value at least \(1\) | Input and output differences lie in \(\mathcal O_{L_j}\) |
| Change of variables | A global \(C^1\)-diffeomorphism sends measurable volume by integrating \(\lvert\det D\Phi\rvert\) | \(\Phi_y\) has derivative factors \(1+3(x_i-y_i)^2>0\) and is onto |
| Cauchy–Schwarz | \((\int fg)^2\le(\int f^2)(\int g^2)\) | Used with \(f=J_y^{1/2}\), \(g=J_y^{-1/2}\) on finite-volume \(W\) |
| Tonelli/product integration | A nonnegative product integrand factors over \(\mathbb R^m\) | \(J_y^{-1}\ge0\) and is integrable |
| Cauchy integral | \(\int_{\mathbb R}(1+3t^2)^{-1}dt=\pi/\sqrt3\) | Direct substitution in \(\int(1+s^2)^{-1}ds=\pi\) |
| Minkowski discriminant bound | For totally real degree \(d\), \(\sqrt{\lvert\Delta_K\rvert}\ge d^d/d!\) | Applied to the totally real cubic base and, separately, arbitrary \(d\ge2\) |
| Perron–Frobenius theorem | For a finite irreducible nonnegative adjacency matrix of spectral radius \(\mu\), path counts from any fixed state to all terminal states are \(\asymp\mu^n\) | The graph in Section I is finite and strongly connected; right-resolvingness identifies paths with label words |

Every conditional inequality in Section D is labeled as such. The unconditional conclusion is (F.10), and it directly negates the strict block inequality.

## H. Failure update

### H.1. Entire positive-volume block class closed

**Closed class.** Every bounded positive-volume Borel set \(W\subset\mathbb R^m\), including arbitrary finite unions of rational boxes, correlated sets, disconnected sets, convex bodies, curved semialgebraic sets, and non-product blocks.

**Reason.** The fixed-specialization diffeomorphism gives (F.10), hence \(R_{\max}(W)<\pi/\sqrt3<R\).

This is a disproof of the complete finite-block conjecture, not merely a failure of a search family.

### H.2. Broader Minkowski volume-cover architecture closed

Let \(K\) be a totally real degree-\(d\) field with \(d\ge2\), let \(\Omega\subset\mathbb R^d\) be any bounded positive-volume Borel window of volume \(V\), and let \(N=N_1(\mathcal P_d(\Omega))\). The usual translated-window certificate is

\[
|B|\ge\frac{V}{\sqrt{|\Delta_K|}},
\qquad
|P_3(B,B)|\le N.
\]

Its normalized factor is necessarily

\[
\frac{|\Delta_K|N}{V^2}
>
\left(
\operatorname{rd}(K)\frac{\sqrt3}{\pi}
\right)^d
>1.
\tag{H.1}
\]

Thus variable block dimensions, nonstationary products, mixtures of blocks, arbitrary translations, and degree-dependent windows do not help if the **only** lower bound for inputs is volume/covolume and the **only** upper bound for outputs is continuous unit-cube covering plus norm separation.

The conclusion is method-level. It does not say that the actual image of every lattice section is large: an anomalously dense translate, a zero-volume or sparse arithmetic set, or an exact discrete collision theorem could evade both estimates in (H.1).

### H.3. Stronger product and box obstructions

If \(S\subset\mathbb R\) is bounded Borel with length \(s>0\), take points \(y\in S\) approaching \(\operatorname{ess\,inf}S\). The one-dimensional specialization formula gives

\[
\operatorname{vol}(P_3(S,S))
\ge
s+3\int_S(x-\operatorname{ess\,inf}S)^2\,dx
\ge s+s^3
\ge2s^2.
\]

For the moment inequality, translate the essential infimum to \(0\) and write \(E\subset[0,\infty)\) with \(|E|=s\). Layer-cake integration and \(|E\cap(u,\infty)|\ge(s-u)_+\) give

\[
\int_Et^2\,dt
=\int_0^\infty2u\,|E\cap(u,\infty)|\,du
\ge\int_0^s2u(s-u)\,du
=\frac{s^3}{3}.
\]

Therefore, for every coordinate product \(W=S_1\times\cdots\times S_m\),

\[
\operatorname{vol}(\mathcal P_m(W))
\ge2^m\operatorname{vol}(W)^2,
\qquad
\eta\ge(2R)^m.
\tag{H.2}
\]

This independently closes all Cartesian-power blocks. Formula (F.5) is the exact single-box specialization.

More generally, suppose \(W\) is a union of \(s\) axis boxes. Choose a component of maximal volume \(v\ge V/s\). Its self-image and (F.4) give

\[
N_1(\mathcal P_m(W))
\ge2^mv^2
\ge\frac{2^mV^2}{s^2},
\]

so

\[
\eta\ge\frac{(2R)^m}{s^2}.
\tag{H.3}
\]

In particular, Boolean or sign-pattern thickenings with at most \(2^m\) component boxes fail because \(R>2\). The exact centre identities

\[
P_3(a,a)=P_3(a,a+1)=2a,
\qquad
P_3(a+1,a)=P_3(a+1,a+1)=2a+2
\tag{H.4}
\]

do produce a perfect one-bit discrete row collapse, but positive-volume thickening cannot survive the diagonal and specialization costs.

### H.4. What remains open

The original real-set conjecture (B.1) remains open. The new theorem does not apply directly to finite sets, whose Lebesgue volume is zero. A surviving method must exploit exact discrete collisions rather than the volume of a continuous polynomial image. It must also avoid the previously frozen failures of fixed-denominator residue lifting, the literal norm-one trace carrier, the literal \(A=GP\) carrier, and separately bounded monomial containers.

The fixed-\(y\) injectivity behind (B.3) requires every successful construction to retain at least linear output entropy. Conversely, if a proposed encoding lets the output recover the ordered input pair up to subexponential multiplicity, it cannot give a power saving. The remaining window lies strictly between those two rates.

## I. Exactly one next statement

The local identities (H.4) suggest a zero-volume replacement: try to propagate the one-bit collapse through exact positional carries rather than by thickening a Boolean cube. Fix an integer base \(b\ge2\) and put \(\Sigma_b=\{0,\ldots,b-1\}\). Digit words are read least-significant digit first. Thus, for

\[
u=u_0u_1\cdots u_{n-1}\in\Sigma_b^n,
\qquad
[u]_b=\sum_{i=0}^{n-1}u_ib^i.
\]

Leading zeroes are retained, so fixed-length words represent distinct integers. Define \(\operatorname{can}_b(0)=+0\); for \(z\ne0\), let \(\operatorname{can}_b(z)\) be its sign followed by the unique least-significant-first base-\(b\) digit string for \(|z|\), with nonzero final digit.

A right-resolving digit graph has at most one outgoing edge of each label from each state. For a graph \(G\) with one initial state, let \(L_n(G)\) be the label words of all length-\(n\) paths from that state, with every terminal state allowed. For an output automaton \(H\), \(L(H)\) denotes the language accepted from its specified initial state to its specified set of final states. Requiring fixed regular input and output languages at every depth is a substantially more structured sufficient condition for the original conjecture. It does not use the positive-volume covering certificate or the previously closed fixed-denominator number-field residue-lifting architecture.

> **Regular digital carry-collapse conjecture.** There exist an integer \(b\ge2\); a finite strongly connected right-resolving graph \(G\) labeled by \(\Sigma_b\), with one initial state and adjacency spectral radius \(\mu>1\); a finite trim deterministic automaton \(H\) over \(\{+,-\}\cup\Sigma_b\), with one initial state, specified final states, and a constant \(\lambda>1\); and constants \(C_0\in\mathbb Z_{\ge0}\), \(C_1>0\), and \(q\ge0\), such that
> \[
> \mu\le\lambda^3<\mu^2,
> \]
> for every integer \(L\ge1\), the number of words of length at most \(L\) in \(L(H)\) is at most \(C_1L^q\lambda^L\), and, for every \(n\ge1\) and every \(u,v\in L_n(G)\),
> \[
> \operatorname{can}_b\!\left(
> Z_n([u]_b,[v]_b)
> \right)\in L(H),
> \qquad
> Z_n(U,V)=(U-V)^3+b^{2n}(U+V),
> \]
> with canonical output length at most \(3n+C_0\). Then, for
> \[
> A_n=b^{-n}\{[u]_b:u\in L_n(G)\},
> \]
> right-resolvingness and Perron–Frobenius theory give \(|A_n|\asymp\mu^n\), while
> \[
> b^{3n}P_3(b^{-n}U,b^{-n}V)=Z_n(U,V)
> \]
> and the output-language bound give
> \[
> |P_3(A_n,A_n)|\ll n^q\lambda^{3n}.
> \]
> In particular, with \(g=2\log\mu-3\log\lambda>0\), the explicit safe exponent
> \[
> \boxed{c_3=\frac{g}{2\log\mu}>0}
> \]
> satisfies \(|P_3(A_n,A_n)|\le|A_n|^{2-c_3}\) for all sufficiently large \(n\).
