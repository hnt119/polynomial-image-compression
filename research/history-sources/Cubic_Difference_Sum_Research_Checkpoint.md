# Cubic Difference–Plus–Sum Research Checkpoint

*Offline, source-disciplined report — 2 September 2026*

## A. Executive verdict

**Verdict 2: a conditional construction is reduced to one genuinely simpler lemma.**

For the conditional construction presented here, the sole remaining hypothesis is the fixed finite-dimensional archimedean covering inequality stated in Section I. If one bounded rational-box block \(W\subset\mathbb R^m\) satisfies it, product amplification along a cofinal tail of the supplied tower gives explicit sets \(A_j\subset\mathbb R\), \(|A_j|\to\infty\), and a fixed exponent

\[
c=\frac{\log(1/\eta)}{\log K}>0,
\qquad
\eta=\frac{R^mN_1(\mathcal F_m(W,W))}{\operatorname{vol}(W)^2},
\qquad
K=N_1(W),
\]

for which \(|F_3(A_j,A_j)|\le|A_j|^{2-c}\). The missing object is one finite-dimensional, interval-arithmetic-certifiable block, not an asymptotic family of real sets.

An unconditional secondary result rules out the following precise architecture: take dense translated rectangular sections of the Minkowski lattice of a growing-degree totally real tower, divide by a fixed denominator supported on completely split primes, and try to compress the complete cubic image using only (i) coordinatewise cube-residue restrictions and (ii) norm-separation packing of the permitted archimedean lifts. This includes every prime power and CRT product supported on the selected good primes \(q\equiv1\pmod3\), every translated or anisotropic rectangular window, and the separately audited exceptional cases at \(2\) and \(3\), including the optimistic variant in which \(2\) is also completely split.

For the strongest one-prime version, the exact normalized upper-bound certificate has base

\[
\beta_q(X)=R\delta_{q,2}
\left(2\max\left\{X,\frac{q^2}{X}\right\}+\frac{q^2}{X^2}\right),
\qquad
\delta_{q,2}=\frac{q^2-q+3}{3q^2},
\]

where \(R\) is the root discriminant and \(X\) is the side length of the input window. Its exact minimum is

\[
\inf_{X>0}\beta_q(X)=R\delta_{q,2}(2q+1)>8R\ge8.
\]

Thus this method's residue-and-lift bound is not merely short of a power saving; after optimization it is worse than the trivial pair count. This is a method-level impossibility, not a lower bound for the actual image and not a disproof of the cubic conjecture.

The mandatory quadratic audit does pass: Section B proves, independently from the cubic calculation, that there are arbitrarily large \(A\subset\mathbb R\) and an explicit fixed \(c_2>0\) for which

\[
|F_2(A,A)|\le |A|^{2-c_2}.
\]

Unconditionally, the cubic conjecture remains unresolved. The norm-one trace carrier, the literal Phase-A hybrid \(A=GP\), and the rectangular multiscale variants are also closed under the precise assumptions recorded in Section H.

## B. Conjecture and normalization

### B.1. Exact statement

The candidate conjecture is

\[
\exists c>0\ \forall N\ge1\ \exists A\subset\mathbb R
\quad
\bigl(A\text{ finite},\ |A|\ge N,\ |F_3(A,A)|\le |A|^{2-c}\bigr),
\]

where

\[
F_3(x,y)=(x-y)^3+x+y.
\]

No claim is made here about novelty or literature status. The calculation is completely offline.

Scaling is a normalization device, not a symmetry of \(F_3\). For every \(M\ne0\),

\[
M^3F_3(M^{-1}u,M^{-1}v)
=(u-v)^3+M^2(u+v).
\]

Multiplication of an image by the nonzero scalar \(M^3\) preserves cardinality. If \(u,v\) lie in a number field and \(\sigma\) is a field embedding, then

\[
F_3(\sigma(u),\sigma(v))=\sigma(F_3(u,v));
\]

an injective real embedding therefore preserves both the polynomial relation and all relevant cardinalities.

### B.2. Audited positive baseline for \(F_2\)

We prove the required baseline rather than assuming it.

**Theorem B.1 (quadratic split-prime construction).** There is a fixed \(c_2>0\) and a sequence of finite sets \(A_j\subset\mathbb R\), with \(|A_j|\to\infty\), such that

\[
|F_2(A_j,A_j)|\le |A_j|^{2-c_2},
\qquad
F_2(x,y)=(x-y)^2+x+y.
\]

We use the following standard lattice facts in the proof. If \(L\) is totally real of degree \(d\), its canonical embedding of \(\mathcal O_L\) has covolume \(\sqrt{|\Delta_L|}\). If \(\Lambda\subset\mathbb R^d\) is a full lattice and \(S\) is bounded and measurable, normalized Haar measure on \(\mathbb R^d/\Lambda\) satisfies

\[
\int_{\mathbb R^d/\Lambda}|(t+S)\cap\Lambda|\,dt
=\frac{\operatorname{vol}(S)}{\operatorname{covol}(\Lambda)}.
\]

Finally, a nonzero algebraic integer has nonzero integral norm and hence absolute norm at least \(1\). These statements respectively supply the covolume, the translated lower count, and the separation estimates below.

**Field and prime supply.** Fix a sufficiently large auxiliary integer \(\ell\). Proposition 3.8 of `unit-distance-proof.pdf` supplies a totally real field \(F\), an everywhere-unramified tower \(L_j/F\), and

\[
d_j=[L_j:\mathbb Q]\to\infty,
\qquad
\operatorname{rd}(L_j)=\operatorname{rd}(F)=:R,
\]

together with

\[
t=\left\lfloor\frac{(\ell-1)^2}{100}\right\rfloor
\]

fixed rational primes \(q_1,\dots,q_t\equiv1\pmod4\) which split completely in every \(L_j\). The same source gives

\[
\log R=O(\ell\log\ell).
\]

Set

\[
M=\prod_{b=1}^tq_b,
\qquad
\rho_2=\prod_{b=1}^t\frac{q_b+1}{2q_b}.
\]

As \(q_b\ge5\), \(\rho_2\le(3/5)^t\). Since \(t\asymp\ell^2\) while \(\log R=O(\ell\log\ell)\), we may and do fix \(\ell\) so that

\[
\eta:=\rho_2R<1.
\]

All of \(R,M,\rho_2,\eta\) are then fixed before \(j\to\infty\).

**Input lattice count.** Let

\[
\Phi_j:\mathcal O_{L_j}\longrightarrow\mathbb R^{d_j}
\]

be the canonical real Minkowski embedding. Its covolume is

\[
\sqrt{|\Delta_{L_j}|}=R^{d_j/2}.
\]

For any fixed \(X>0\), Haar averaging over \(\mathbb R^{d_j}/\Phi_j(\mathcal O_{L_j})\) gives a translate \(s_j+[0,X]^{d_j}\) for which

\[
B_j:=\{\alpha\in\mathcal O_{L_j}:\Phi_j(\alpha)\in s_j+[0,X]^{d_j}\}
\]

satisfies

\[
|B_j|\ge\frac{X^{d_j}}{\sqrt{|\Delta_{L_j}|}}
=\left(\frac{X}{\sqrt R}\right)^{d_j}.
\]

Distinct algebraic integers are \(1\)-separated in the sup norm: otherwise the product of the absolute values of all conjugate differences would be \(<1\), contradicting that a nonzero integral norm has absolute value at least \(1\). Packing therefore also gives

\[
|B_j|\le(X+1)^{d_j}.
\]

Define the real set

\[
A_j=\left\{\frac{\sigma_1(\alpha)}{M}:\alpha\in B_j\right\},
\]

where \(\sigma_1:L_j\hookrightarrow\mathbb R\) is any real embedding. It is injective, so \(|A_j|=|B_j|\).

**Restriction of every output.** For \(\alpha,\beta\in B_j\), put

\[
z=(\alpha-\beta)^2+M(\alpha+\beta)\in\mathcal O_{L_j}.
\]

Then

\[
M^2F_2(\sigma_1(\alpha)/M,\sigma_1(\beta)/M)=\sigma_1(z).
\]

For every prime ideal \(\mathfrak q\mid q_b\), the class of \(z\) is the square \((\alpha-\beta)^2\). Complete splitting gives

\[
\mathcal O_{L_j}/q_b\mathcal O_{L_j}\cong\mathbb F_{q_b}^{d_j}.
\]

There are \((q_b+1)/2\) squares in \(\mathbb F_{q_b}\); hence CRT leaves exactly

\[
(\rho_2M)^{d_j}
\]

allowed residue classes modulo \(M\mathcal O_{L_j}\). This condition holds for every pair in \(B_j^2\).

In one conjugate coordinate, two inputs in an interval of side \(X\) give an output interval of length at most

\[
W_2=X^2+2MX.
\]

Two distinct algebraic integers in the same class modulo \(M\mathcal O_{L_j}\) are \(M\)-separated in the sup norm. Consequently each allowed residue class contributes at most \((1+W_2/M)^{d_j}\) archimedean lifts, and

\[
|F_2(A_j,A_j)|
\le\left[\rho_2(M+X^2+2MX)\right]^{d_j}.
\]

Combining this with the input lower bound gives

\[
\frac{|F_2(A_j,A_j)|}{|A_j|^2}
\le\theta_2(X)^{d_j},
\qquad
\theta_2(X)=\eta\left(1+\frac{2M}{X}+\frac{M}{X^2}\right).
\]

Choose once and for all

\[
X\ge
\max\left\{1,\ 2\sqrt R,\ \frac{6M\eta}{1-\eta}\right\}.
\]

Since \(2M/X+M/X^2\le3M/X\), this ensures

\[
\theta_2(X)\le\frac{1+\eta}{2}<1,
\qquad
|A_j|\ge2^{d_j}\to\infty.
\]

Finally \(|A_j|\le(X+1)^{d_j}\), so

\[
d_j\ge\frac{\log|A_j|}{\log(X+1)}.
\]

Thus the fully explicit fixed exponent

\[
\boxed{
c_2=
\frac{\log\!\left(2/(1+\rho_2R)\right)}{\log(X+1)}>0
}
\]

satisfies

\[
|F_2(A_j,A_j)|\le |A_j|^{2-c_2}.
\]

There is no class-group or regulator loss in this baseline. The discriminant enters through the input covolume, the denominator is fixed, CRT is exact, the lift multiplicity is explicitly packed, and the bound covers the complete Cartesian image.

## C. Source-mechanism reconstruction

### C.1. Source record and availability

The formal unit-distance authority used here is `unit-distance-proof.pdf`; `unit-distance-remarks.pdf` is a separate human-verified alternative and `unit-distance-cot.pdf` is a discovery record, not a proof authority. `The_Unit_Distance_Problem_and_the_Sum_Product_Phenomenon_Guide_Final_Frozen(1).pdf` is a secondary guide. The sum-product source available here is the frozen secondary reconstruction `Phase_A_Sum_Product_Reproduction_FINAL_FROZEN.pdf`, together with `Phase_A_FINAL_FROZEN_Change_Log.pdf`.

No separate frozen \(Q\)- or cubic-experiment checkpoint is among the current source attachments. A prior workspace \(Q\)-report is visible but is not elevated to source authority; only the frozen assertions reproduced in the operative prompt are treated as premises. The following other named materials are not present: `Phase_A_Source_Audit.pdf` itself, the Phase-B mechanism/collision/failure/open-lemma libraries, and the original Bloom–Sawin–Schildkraut–Zhelezov paper cited by the Phase-A reconstruction. Accordingly, BSSZ numbering below is reported from the frozen reconstruction and is not claimed to have been checked against the original paper.

### C.2. Exact unit-distance chain

Fix a large \(\ell\). The formal proof constructs a totally real cyclic cubic field \(F\) and uses its maximal everywhere-unramified pro-\(3\) extension. With

\[
t=\left\lfloor\frac{(\ell-1)^2}{100}\right\rfloor,
\]

the relation-rank estimate, a Frattini quotient, Chebotarev, and Golod–Shafarevich produce finite totally real layers \(L_j/F\) such that

\[
f_j=[L_j:\mathbb Q]\to\infty,
\qquad
\operatorname{rd}(L_j)=\operatorname{rd}(F),
\]

and fixed rational primes \(q_1,\dots,q_t\equiv1\pmod4\) split completely throughout the tower. Put \(K_j=L_j(i)\). Then

\[
\operatorname{rd}(K_j)\le2\operatorname{rd}(F),
\qquad
h(K_j)\le H_\ell^{f_j},
\qquad
\log H_\ell=O(\ell\log\ell).
\]

Each \(q_b\) supplies \(f_j\) conjugate prime-ideal pairs in \(K_j/L_j\), so there are \(tf_j\) pairs. Choosing one ideal from each pair gives \(2^{tf_j}\) sign ideals. A class-group pigeonhole retains at least \(2^{tf_j}/h(K_j)\) choices in one ideal class. If \(\eta\) is a fixed choice in that fibre and

\[
(\alpha_\varepsilon)=\mathfrak A_\varepsilon\mathfrak A_\eta^{-1},
\qquad
u_\varepsilon=\frac{\alpha_\varepsilon}{\overline{\alpha_\varepsilon}},
\]

then the valuation vector is

\[
v_{\mathfrak P_s}(u_\varepsilon)=2(\varepsilon_s-\eta_s),
\qquad
v_{\overline{\mathfrak P}_s}(u_\varepsilon)=-2(\varepsilon_s-\eta_s).
\]

It proves distinctness and the fixed-denominator bound

\[
U_j\subset D_{\mathrm{ud}}^{-1}\mathcal O_{K_j},
\qquad
D_{\mathrm{ud}}=\left(\prod_{b=1}^tq_b\right)^2.
\]

Moreover \(u\bar u=1\), so every complex embedding has modulus \(1\). With

\[
\gamma=t\log2-\log H_\ell>0,
\]

the exact direction supply is

\[
\boxed{|U_j|\ge e^{\gamma f_j}.}
\]

Embed \(D_{\mathrm{ud}}^{-1}\mathcal O_{K_j}\) as a full lattice in \(\mathbb C^{f_j}\). For a product of discs of radius \(R_w>1/2\), let \(b(R_w)=\pi R_w^2\), let \(a(R_w)\) be the overlap area of two such discs whose centres are distance \(1\), and put

\[
\rho_{R_w}=\frac{a(R_w)}{b(R_w)}\to1.
\]

Haar unfolding on the lattice torus gives, for some translate, point count \(N_j\) and directed-overlap count \(E_j\) satisfying

\[
E_j\ge |U_j|\rho_{R_w}^{f_j}N_j.
\]

Choose the fixed \(R_w\) so that \(\log\rho_{R_w}>-\gamma/2\). Then

\[
E_j\ge e^{\gamma f_j/2}N_j.
\]

Projection to one complex coordinate is injective. Every selected translation projects to a planar vector of length \(1\), and passing from directed pairs to unordered unit segments costs at most \(2\):

\[
\nu(P_j)\ge\frac12e^{\gamma f_j/2}|P_j|.
\]

Norm separation in the fixed-denominator lattice gives

\[
|P_j|\le(4R_wD_{\mathrm{ud}})^{2f_j}=e^{B_{\mathrm{ud}}f_j},
\qquad
B_{\mathrm{ud}}=2\log(4R_wD_{\mathrm{ud}}).
\]

Also \(E_j\le N_j^2\), hence \(N_j\ge e^{\gamma f_j/2}\to\infty\). The exact rates are therefore

| Unit-distance quantity | Per-degree rate |
|---|---:|
| sign/class-group direction supply | \(\gamma=t\log2-\log H_\ell\) |
| product-window overlap | \(\log\rho_{R_w}<0\) |
| surviving directed pairs per point | \(\gamma+\log\rho_{R_w}>\gamma/2\) |
| point budget | \(B_{\mathrm{ud}}=2\log(4R_wD_{\mathrm{ud}})\) |
| raw power gain | \(\gamma/(2B_{\mathrm{ud}})\) |
| formal exponent after absorbing \(1/2\) | \(\delta=\gamma/(4B_{\mathrm{ud}})>0\) |

The decisive arrow is selected-translation overlap. It produces many edges; it does **not** bound the image of a polynomial on every pair.

### C.3. Exact frozen Phase-A sum-product chain

Let \(K/\mathbb Q\) be totally real of degree \(d\ge2\), discriminant \(\Delta_K\), and regulator \(\operatorname{Reg}_K\). The frozen Phase-A reconstruction records

\[
\operatorname{Reg}_K\le\Delta_K
\]

and unbounded-degree fields with

\[
\Delta_K\le D_0^d
\]

for an absolute \(D_0>1\). For

\[
B^+(T)=\{a\in\mathcal O_K:|\sigma_i(a)|\le T\ \forall i\},
\]

the additive lattice estimate, valid for \(T\ge1\), is

\[
T^d\Delta_K^{-1/2}\le|B^+(T)|\le(2T+1)^d.
\]

Choose a sufficiently small absolute \(\varepsilon>0\). In the proof-normalized regime take \(X,Y\ge2\), with \(\varepsilon X\ge1\), and set

\[
P=X+B^+(\varepsilon X).
\]

Then

\[
(\varepsilon X)^d\Delta_K^{-1/2}\le|P|\le(2\varepsilon X+1)^d.
\]

The factor \(\varepsilon^d\) is essential; its omission is one of the errors repaired in the supplied change log.

For

\[
G=B^\times(Y)=
\{u\in\mathcal O_K^\times:|\log|\sigma_i(u)||\le Y\ \forall i\},
\]

Dirichlet's unit lattice and the frozen estimates give

\[
\frac{Y^{d-1}}{\sqrt d\,\operatorname{Reg}_K}
\le|G|\le10(5Y+1)^{d-1},
\qquad
|GG|\le10(10Y+1)^{d-1},
\]

and hence, for an absolute \(c_0>0\),

\[
\frac{|GG|}{|G|^2}
\le c_0^{-d}Y^{1-d}\Delta_K^2.
\]

With \((1+\varepsilon)/(1-\varepsilon)<(1+\sqrt5)/2\), the golden-ratio unit-separation lemma proves that \(G\times P\to GP\) is injective. Thus, for

\[
A=GP,
\]

one has

\[
|A|=|G||P|,
\qquad
\frac{(c_0XY)^d}{Y\Delta_K^{3/2}}
\le|A|\le\left(\frac{XY}{c_0}\right)^d.
\]

The product identity is exact:

\[
AA=(GG)(PP),
\]

so

\[
\frac{|AA|}{|A|^2}
\le\frac{|GG|}{|G|^2}
\le c_0^{-d}Y^{1-d}\Delta_K^2.
\]

For addition, bounded unit distortion puts \(A+A\) in one additive Minkowski box. Since \(1\in G\), the normalization uses \(P\subset A\), not the directness identity, and gives

\[
\frac{|A+A|}{|A|}
\le\left(\frac{e^Y}{c_0}\right)^d\Delta_K^{1/2}.
\]

Under \(\Delta_K\le D_0^d\), the two ledgers become

\[
\frac{|AA|}{|A|^2}
\le Y\left(\frac{D_0^2}{c_0Y}\right)^d,
\qquad
\frac{|A+A|}{|A|}
\le\left(\frac{e^YD_0^{1/2}}{c_0}\right)^d.
\]

Choosing \(Y=4D_0^2c_0^{-1}\), then taking the additive-box parameter sufficiently large, applying the fixed rescaling of that parameter recorded in the frozen reconstruction, and discarding finitely many eligible degrees yields its normalized form

\[
X^d\le|A|\le(CX)^d,
\qquad
|A+A|\le C^d|A|,
\qquad
|AA|\le2^{-d}|A|^2.
\]

If \(X=C^{1/\theta}\), then

\[
|A+A|\le|A|^{1+\theta},
\qquad
|AA|\le|A|^{2-c_1\theta},
\qquad
c_1=\frac{\log2}{2\log C}.
\]

Balancing the exponents at \(\theta=1/(1+c_1)\) gives the fixed sum-product exponent \(c=c_1/(1+c_1)>0\). The compression comes entirely from the factorization \(AA=(GG)(PP)\); no corresponding factorization exists for \(F_3(gp,hq)\).

### C.4. Exact transfer dictionary

| Source mechanism | Quantitative role in the source proof | Proposed cubic analogue | Status |
|---|---|---|---|
| Fixed split rational primes | \(tf\) prime-ideal coordinates; fixed while \(f\to\infty\) | At each degree-one coordinate, force the cleared output to be a cube modulo \(q^2\) | **Proved locally; fails globally** |
| Prime-ideal sign entropy | \(2^{tf}\) norm-one direction candidates | Force compatible \(F_3\)-collisions or fewer output labels | **Fails:** valuation pairs retain both sign vectors |
| Class-group fibre | Loses \(h(K)\le H^f\) to principalize sign ideals | Principalize a correlated input parametrization | **Fails as a standalone transfer:** size gives no collision coherence; an engineered subfibre remains open |
| Fixed denominator | Keeps source packing exponential with fixed base | Makes \(M^2(u+v)\) vanish at split primes | **Fails for the residue-plus-rectangular-lift certificate:** cubic height carries \(M^2\) |
| Minkowski window | Produces the finite source set; overlap/packing have fixed bases | Produce \(A\), its size, and a full archimedean output box | **Fails for the rectangular certificate; nonrectangular blocks remain open** |
| Translation overlap | Gives \(e^{(\gamma+\log\rho)f}\) selected unit edges | Must be replaced by a bound for the complete Cartesian image | **Fails:** for fixed difference, \(F_3(a,a-d)\) is injective in \(a\) |
| Unit box \(G\) | \(\lvert GG\rvert/\lvert G\rvert^2\le e^{-\kappa d}\) with bounded distortion | Collapse the joint states \(g^3,g^2h,gh^2,h^3,g,h\) | **Fails for the displayed literal carrier:** its state map is injective/bounded-fibre |
| Additive box \(P\) | Supplies \((\varepsilon X)^d\Delta^{-1/2}\) inputs and controls addition | Supply dense inputs while paying degree-three output height | **Fails with separate containers:** the \(X^3\) scale wins |
| Degree-to-power conversion | \(e^{-\kappa d}\) plus \(\lvert A\rvert\le e^{Bd}\) gives a fixed power | Same implication for \(F_3\) | **Conditional formal step; no positive cubic \(\kappa\)** |

The row that cannot be transferred is translation overlap. A large set of repeated relations among selected pairs is neither a bound for \(F_3(A,A)\) nor control of pairs outside that selected relation.

## D. Explicit candidate set

### D.1. Cubic field supply

We use Chebotarev in the following standard form. If \(E/\mathbb Q\) is finite Galois and \(C\) is a conjugacy class in \(\operatorname{Gal}(E/\mathbb Q)\), the unramified rational primes with Frobenius class \(C\) have density \(|C|/|\operatorname{Gal}(E/\mathbb Q)|\). In particular, primes splitting completely in \(E\) have positive density. An odd rational prime splits completely in \(\mathbb Q(i)\) exactly when it is \(1\pmod4\), and an unramified rational prime splits completely in \(\mathbb Q(\zeta_3)\) exactly when it is \(1\pmod3\).

For the cubic sieve, let \(\widetilde E/\mathbb Q\) be the normal closure of the finite Frattini extension used in the unit-distance proof, and apply this statement to \(\widetilde E(i,\zeta_3)\), after excluding its finite ramified set. The fixed rational primes can then be chosen with

\[
q\equiv1\pmod{12},
\]

while their Frobenius elements are still trivial in the relevant finite Frattini quotient. Killing those Frobenius elements has the same finite relation cost as in Proposition 3.8. Thus one obtains a nested totally real unramified tower

\[
L_1\subset L_2\subset\cdots,
\qquad
d_j=[L_j:\mathbb Q]\to\infty,
\qquad
\operatorname{rd}(L_j)=R,
\]

in which the fixed prime \(q\equiv1\pmod{12}\) splits completely. Adjoining \(i\) retains the complete-splitting input of the attached proof, while adjoining \(\zeta_3\) supplies the cubic residue condition. This congruence refinement is a standard Chebotarev modification of the attached proof; it is not asserted to be a displayed proposition in that PDF.

### D.2. The dense split-prime candidate

Fix a side length \(X>\sqrt R\). Haar averaging supplies \(s_j\in\mathbb R^{d_j}\) such that

\[
B_{j,X}=
\{\alpha\in\mathcal O_{L_j}:\Phi_j(\alpha)\in s_j+[0,X]^{d_j}\}
\]

satisfies

\[
\left(\frac{X}{\sqrt R}\right)^{d_j}
\le |B_{j,X}|\le(X+1)^{d_j}.
\]

There is no congruence restriction on the inputs: all residue classes which happen to occur in this translated window are retained. Define

\[
\boxed{
A_{j,X}=q^{-1}\sigma_1(B_{j,X})\subset\mathbb R.
}
\]

Here \(L_j\) is the ambient field, \(q\) is the fixed denominator, \(s_j+[0,X]^{d_j}\) is the complete lattice window, and \(\sigma_1\) is a specified real embedding. The set is explicit up to the Blichfeldt translate \(s_j\), whose existence is proved by averaging. It is arbitrarily large because \(X/\sqrt R>1\) and \(d_j\to\infty\).

For \(u,v\in B_{j,X}\), put

\[
Z(u,v)=(u-v)^3+q^2(u+v)\in\mathcal O_{L_j}.
\]

Then

\[
q^3F_3(\sigma_1(u)/q,\sigma_1(v)/q)=\sigma_1(Z(u,v)).
\]

Section E bounds the image of **all** pairs \((u,v)\in B_{j,X}^2\).

### D.3. Precisely defined variants covered by the audit

The same audit permits:

- a fixed integer denominator \(M\) supported on finitely many good split primes;
- any CRT modulus \(m\mid M^2\) supported on those primes;
- translated anisotropic windows \(\prod_i[c_i-R_i,c_i+R_i]\);
- an algebraic denominator \(\mu\) with \(\mu^2\in m\mathcal O_L\), even when its conjugates are anisotropic;
- same-centre two-scale pieces, provided self- and cross-images are bounded separately by the same residue/container argument;
- arbitrary correlations among the residue coordinates at the squarefree level, provided input density is certified only by residue-density averaging and the global lift uses only uniform norm-separation packing.

These extensions are part of the failed architecture, not additional candidate constructions.

## E. Full-image bound

### E.1. Exact local arithmetic and prime-power lifting

Let

\[
P_C(x,y)=(x-y)^3+C(x+y)
\]

over \(R_k=\mathbb Z/p^k\mathbb Z\), where \(p\) is odd, and set

\[
r=\min\{v_p(C),k\}.
\]

For \(r=0\), interpret \(\mathbb Z/p^0\mathbb Z\) as the one-class quotient and set \(c_p(0)=N_0(0)=1\).

Writing \(d=x-y\) and \(x=y+d\) gives

\[
P_C=d^3+Cd+2Cy.
\]

Because \(2\) is invertible and \(2Cy\) runs over \(p^rR_k\),

\[
\boxed{
\operatorname{im}P_C
=\{z\in R_k:z\bmod p^r\text{ is a cube}\}.
}
\]

If \(N_r(a)\) is the number of cube roots of \(a\) modulo \(p^r\), then the exact fibre size is

\[
\boxed{
r_{P_C,k}(z)=p^kN_r(z\bmod p^r).
}
\]

For \(p\ne3\), put \(g=\gcd(3,p-1)\). The number of cubes modulo \(p^r\) is

\[
c_p(r)=1+\frac1g
\sum_{h=0}^{\lfloor(r-1)/3\rfloor}\varphi(p^{r-3h}).
\]

When \(p\equiv1\pmod3\), \(g=3\), and the density is

\[
\delta_{p,r}=\frac{c_p(r)}{p^r}
=p^{-r}+\frac{p-1}{3p}
\sum_{h=0}^{\lfloor(r-1)/3\rfloor}p^{-3h}.
\]

In particular,

\[
\delta_{p,1}=\frac{p+2}{3p},
\qquad
\delta_{p,2}=\frac{p^2-p+3}{3p^2},
\qquad
\lim_{r\to\infty}\delta_{p,r}=\frac{p^2}{3(p^2+p+1)}.
\]

For \(C=M^2\), the usable depth at \(p\) is only \(r\le2v_p(M)\). Beyond it, the coefficient no longer vanishes to the new depth and the density does not improve. If \(p\) splits completely in a degree-\(d\) field, then

\[
\mathcal O_L/p^k\mathcal O_L\cong(\mathbb Z/p^k\mathbb Z)^d,
\]

so the permitted density is exactly \(\delta_{p,r}^d\). Densities at distinct rational primes multiply exactly by CRT; there is no hidden local lifting multiplicity.

For the candidate in Section D, take \(C=q^2\) and reduce modulo \(q^2\). Every output is a cube and the number of permitted residue classes is exactly

\[
\left(\delta_{q,2}q^2\right)^{d_j},
\qquad
\delta_{q,2}=\frac{q^2-q+3}{3q^2}.
\]

### E.2. Exact archimedean range

Let \(I=[c-X/2,c+X/2]\). For \(u,v\in I\), put

\[
d=u-v,
\qquad
s=u+v-2c.
\]

The feasible set is the diamond

\[
|d|+|s|\le X.
\]

Therefore

\[
Z(u,v)-2q^2c=d^3+q^2s.
\]

For \(0\le t\le X\), the largest possible absolute value at \(|d|=t\) is \(t^3+q^2(X-t)\). This is convex in \(t\), so its maximum occurs at an endpoint. The exact continuous output width is consequently

\[
\boxed{
W_q(X)=2\max\{X^3,q^2X\}.
}
\]

The translation \(c\) changes only the centre \(2q^2c\); it cannot reduce the width. This coupled calculation is sharper than treating \(u-v\) and \(u+v\) as independent intervals.

### E.3. Counting all permitted lifts

If two distinct algebraic integers \(z,z'\) are congruent modulo \(q^2\mathcal O_{L_j}\), then \(z-z'=q^2\gamma\) for a nonzero algebraic integer \(\gamma\). Hence

\[
\prod_{i=1}^{d_j}|\sigma_i(z-z')|
=q^{2d_j}|N_{L_j/\mathbb Q}(\gamma)|
\ge q^{2d_j},
\]

so one conjugate difference has absolute value at least \(q^2\). A permitted residue class contains at most

\[
\left(1+\frac{W_q(X)}{q^2}\right)^{d_j}
\]

points in the full output rectangle. Combining the exact local count and the archimedean lifts gives

\[
\boxed{
|F_3(A_{j,X},A_{j,X})|
\le
\left[
\delta_{q,2}
\left(q^2+2\max\{X^3,q^2X\}\right)
\right]^{d_j}.
}
\]

No pair has been discarded: the congruence and range statements hold simultaneously for every \((u,v)\in B_{j,X}^2\). There are no residue, valuation, unit, or scale branches, so there are no omitted cross-pairs. Multiplication by \(q^3\) and the injectivity of \(\sigma_1\) preserve image cardinality.

### E.4. Why residue correlations at the first level do not repair the lift

Let \(M=\prod_{b=1}^tq_b\), with all \(q_b\equiv1\pmod3\), and let

\[
\mathcal R_M=\prod_{b=1}^t\mathbb F_{q_b}.
\]

For an arbitrary correlated code \(\mathcal C\subset\mathcal R_M^d\), set

\[
\mathcal D=\{(c-c')^{\circ3}:c,c'\in\mathcal C\}.
\]

In one coordinate, a prescribed output has at most \(3^t\) possible differences and, for each difference, exactly \(M\) ordered ambient pairs. Thus

\[
|\mathcal D|\ge\frac{|\mathcal C|^2}{(3^tM)^d},
\qquad
\frac{M^d|\mathcal D|}{|\mathcal C|^2}\ge3^{-td}.
\]

If the input lattice section is restricted to the residue vectors in \(\mathcal C\), translation averaging gives only

\[
|B|\ge
\frac{|\mathcal C|X^d}{M^d\sqrt{\Delta_L}}.
\]

With the same denominator \(M\), the exact coupled output width is \(2\max\{X^3,M^2X\}\). Uniform norm-packing of every permitted output residue therefore gives the normalized certificate

\[
\frac{M^d|\mathcal D|}{|\mathcal C|^2}
\left[
R\,\frac{M+2\max\{X^3,M^2X\}}{X^2}
\right]^d.
\]

The second factor has minimum

\[
R\left(2M+\frac1M\right)
\]

per degree. Even the information-theoretically best permitted code would therefore leave base at least

\[
3^{-t}R\left(2M+\frac1M\right)
>2R\prod_{b=1}^t\frac{q_b}{3}>1.
\]

This closes correlated residue coordinates only for the stated certificate: averaged input density plus a uniform norm-packing lift. It does not rule out an anomalously dense translate combined with a residue-sensitive lift theorem, and it says nothing about the correlated archimedean blocks proposed in Section I.

## F. Exponential-rate ledger

### F.1. Cubic candidate

The input estimates are

\[
\left(\frac X{\sqrt R}\right)^{d_j}
\le|A_{j,X}|\le(X+1)^{d_j}.
\]

Thus \(X>\sqrt R\) gives the positive input growth rate

\[
\alpha=\log X-\frac12\log R>0,
\]

and the size-budget rate is \(B=\log(X+1)\). Dividing the full-image estimate by the square of the input lower bound gives

\[
\frac{|F_3(A_{j,X},A_{j,X})|}{|A_{j,X}|^2}
\le\beta_q(X)^{d_j},
\]

where

\[
\boxed{
\beta_q(X)
=R\delta_{q,2}
\left(
2\max\left\{X,\frac{q^2}{X}\right\}
+\frac{q^2}{X^2}
\right).
}
\]

| Quantity | Exact or bounded form | Per-degree gain/cost | Dependence |
|---|---|---:|---|
| Input size | \((X/\sqrt R)^{d_j}\le\lvert A\rvert\le(X+1)^{d_j}\) | \(\alpha=\log X-\tfrac12\log R\), \(B=\log(X+1)\) | \(R,X\) fixed before \(j\to\infty\) |
| Local cube saving | \(\delta_{q,2}^{d_j}\) | gain \(-\log\delta_{q,2}\) | fixed \(q\) |
| Discriminant cost | \(\Delta_{L_j}=R^{d_j}\) in the normalized ratio | \(+\log R\) | fixed tower |
| Denominator and height | \(q^2\) in the linear term; exact width \(2\max(X^3,q^2X)\) | \(+\log(2\max\{X,q^2/X\}+q^2/X^2)\) | fixed \(q,X\) |
| Class-group/regulator | absent from this candidate | \(0\) | none |
| CRT multiplicity | exact product | \(0\) | none |
| Archimedean lift multiplicity | \((1+W_q(X)/q^2)^{d_j}\) | included above | fixed \(q,X\) |
| Net compression | \(\beta_q(X)^{d_j}\) | \(\kappa_3(X)=-\log\beta_q(X)\) | must be \(>0\) |

The requested feasibility inequality is exactly

\[
\boxed{
\underbrace{\log\frac1{\delta_{q,2}}}_{\text{local gain}}
>
\underbrace{\log R}_{\text{discriminant}}
+
\underbrace{\log\left(
2\max\{X,q^2/X\}+q^2/X^2
\right)}_{\text{degree-three height, denominator, and lifts}}.
}
\]

There is no multiplicity or class-group term to hide.

### F.2. Exact optimization and fatal inequality

The function inside the last logarithm decreases up to \(X=q\) and increases afterward. Therefore

\[
\inf_{X>0}\beta_q(X)=R\delta_{q,2}(2q+1).
\]

Since \(q\ge13\),

\[
q\delta_{q,2}
=\frac{q^2-q+3}{3q}
\ge\frac{53}{13}>4,
\]

and hence

\[
\boxed{
\inf_X\beta_q(X)>8R\ge8.
}
\]

For the most favorable admissible prime \(q=13\), the exact lower bound is

\[
\inf_X\beta_{13}(X)
\ge\frac{1431}{169}\approx8.467.
\]

Equivalently, the best possible net rate certified by this architecture satisfies

\[
\kappa_3(X)\le-\log(1431/169)<0
\]

even before charging any root-discriminant cost. Deeper powers do not amplify the local gain: \(\delta_{q,r}\) tends to a positive constant, while the denominator scale grows. More precisely, let

\[
M=\prod_{b=1}^tq_b^{a_b},
\qquad
m=\prod_{b=1}^tq_b^{r_b}\mid M^2,
\qquad
\delta_m=\prod_{b=1}^t\delta_{q_b,r_b},
\]

with every \(r_b\ge1\). Since

\[
\delta_{q_b,r_b}q_b^{a_b}
\ge\frac{q_b-1}{3q_b}\,q_b^{a_b}
\ge\frac{q_b-1}{3}\ge2,
\]

one has \(M\delta_m\ge2^t\). Thus adding depth or CRT primes only increases the fatal optimized factor.

There is a stronger method-level check. In an interval of side \(X\), the input has at most \(X+1\) lattice points per degree in the norm-packing sense. For every \(X>0\),

\[
\delta_{q,2}
\left(q^2+2\max\{X^3,q^2X\}\right)
>(X+1)^2.
\]

Thus the residue/container expression used as an upper bound for the image is itself larger than the trivial bound \(|B|^2\), for every translate. This is why the conclusion is a failure of the certificate, not a lower bound for the actual image.

### F.3. Anisotropic and exceptional-prime ledgers

For half-widths \(R_i>0\), denominator \(M\), and CRT modulus \(m\mid M^2\), let

\[
\delta_m=\frac{|\{x^3:x\in\mathbb Z/m\mathbb Z\}|}{m}.
\]

The exact one-coordinate half-width is

\[
H_M(R_i)=\max\{8R_i^3,2M^2R_i\},
\]

and the normalized factor is

\[
\Phi_{M,m}(R_i)
=\frac{m+2H_M(R_i)}{4R_i^2}
=\frac m{4R_i^2}+\max\left\{4R_i,\frac{M^2}{R_i}\right\}.
\]

It is minimized at \(R_i=M/2\), with

\[
\min_{R_i>0}\Phi_{M,m}(R_i)=2M+\frac m{M^2}.
\]

Every coordinate optimizes independently, so anisotropy cannot improve the geometric-mean rate. Translation changes only the centre. The resulting necessary condition

\[
-\log\delta_m>\log R+\log\left(2M+\frac m{M^2}\right)
\]

fails for every nonempty set of good primes.

Even granting extra complete splitting not supplied by the tower does not change the verdict:

| Exceptional local effect | Exact optimized base |
|---|---:|
| parity: unscaled \(F_3\) modulo \(2^k\) has exactly the even image | \(\tfrac32\,2^{1/3}R\approx1.890R\) |
| denominator \(3\), cube restriction modulo \(9\) | \(7R/3\) |
| parity combined with the modulo-\(9\) restriction | \(4R/3\) |

Here are the optimizations behind the table. Modulo \(2^k\), the unscaled identity

\[
F_3(x,y)=(x-y)^3+(x-y)+2y
\]

has exactly the even classes as its image, of density \(1/2\); deeper \(k\) leaves the density unchanged, so the best packing modulus is \(2\). Its base is

\[
R\left(X^{-2}+\max\{X,X^{-1}\}\right),
\]

minimized at \(X=2^{1/3}\). With denominator \(3\), the cubes modulo \(9\) are \(0,\pm1\), of density \(1/3\), and the exact factor

\[
\frac R3\left(\frac9{X^2}+2\max\{X,9/X\}\right)
\]

is minimized at \(X=3\), giving \(7R/3\). Combining parity with this condition uses modulus \(18\) and density \(1/6\); at \(X=3\) its minimum is \(4R/3\). All are \(>1\). The supplied tower does not in any event assert that \(2\) or \(3\) splits completely.

### F.4. Correct degree-to-power conversion

Had a construction produced

\[
|F_3(A_j,A_j)|\le C_*e^{-\kappa d_j}|A_j|^2,
\qquad
|A_j|\le C_Ae^{Bd_j},
\]

with fixed \(B,\kappa>0\), then

\[
d_j\ge\frac{\log|A_j|-\log C_A}{B}.
\]

Consequently every fixed

\[
0<c<\frac\kappa B
\]

would work for all sufficiently large \(j\); \(c=\kappa/(2B)\) is a safe explicit choice after absorbing \(C_*C_A^{\kappa/B}\). In the present cubic sieve, \(\kappa_3<0\), so this formal conversion never starts. In the quadratic baseline there is no prefactor and Section B obtains the sharper displayed \(c_2\).

## G. Proof audit

### G.1. Substantial standard results and hypotheses

| Result | Precise form used | Hypothesis check |
|---|---|---|
| Relative discriminant formula | \(\lvert\Delta_M\rvert=\lvert\Delta_F\rvert^{[M:F]}N_{F/\mathbb Q}(\mathfrak d_{M/F})\) | \(L_j/F\) is everywhere unramified, so root discriminant is constant |
| Conductor–discriminant formula | For an abelian extension, \(\lvert\Delta_L\rvert=\prod_\chi f(\chi)\) | Used inside the attached construction of its cyclic cubic base field |
| Burnside/Frattini basis theorem | \(d(G)=\dim_{\mathbb F_p}G/\Phi(G)\); killing elements of \(\Phi(G)\) preserves generator rank | Frobenius elements are chosen in the Frattini subgroup |
| Golod–Shafarevich | A finite nontrivial pro-\(p\) group has relation rank \(r>d^2/4\) | The attached proof establishes the opposite inequality after adding the split-prime relations |
| Shafarevich relation estimate | In the exact totally real cubic pro-\(3\) setting of the source, \(r(G)\le d(G)+C_0\) | Used only in the source reconstruction, with the source's hypotheses |
| Chebotarev density theorem | A conjugacy class \(C\) in finite Galois \(E/\mathbb Q\) occurs with density \(\lvert C\rvert/\lvert\operatorname{Gal}(E/\mathbb Q)\rvert\) among unramified primes | Applied to the normal closure \(\widetilde E(i,\zeta_3)\); complete splitting gives trivial Frattini Frobenius and \(q\equiv1\pmod{12}\) |
| Minkowski covolume | A totally real \(\mathcal O_L\) embeds as a lattice of covolume \(\sqrt{\lvert\Delta_L\rvert}\) | Every \(L_j\) used for real sets is totally real |
| Haar/Blichfeldt averaging | The average number of lattice points in a translated bounded measurable set is volume divided by covolume | Cubes and the later finite unions of boxes are bounded and Jordan measurable |
| Algebraic norm separation | A nonzero algebraic integer has nonzero integral norm, hence absolute norm at least \(1\) | Applied only to differences in \(\mathcal O_L\), or after explicitly clearing a modulus |
| Complete splitting and CRT | If \(q\) splits completely, \(\mathcal O_L/q^k\mathcal O_L\cong(\mathbb Z/q^k\mathbb Z)^d\) | The selected primes are unramified and completely split at every tower level |
| Cube count modulo \(p^r\) | Units have kernel size \(\gcd(3,p-1)\) under cubing for \(p\ne3\); valuations of cubes are multiples of \(3\) | The central prime satisfies \(q\equiv1\pmod{12}\), \(q\ge13\) |
| Dirichlet unit theorem | Logarithmic units form a rank-\((d-1)\) lattice of covolume \(\sqrt d\operatorname{Reg}_K\) in the frozen convention | Used only in reconstructing the totally real Phase-A field |
| Polynomial root bound | A nonzero degree-\(r\) polynomial over a field has at most \(r\) roots | Used for the carrier-recovery bounds in Section H |

The class-number estimate, regulator estimate, golden-ratio unit-separation lemma, and Martinet-type bounded-root-discriminant supply are used in exactly the special forms stated in the attached formal/frozen reports. Their original cited sources were not supplied, so no independent source attribution is claimed.

### G.2. Mandatory kill-test audit

| Test | Audit result |
|---|---|
| Full Cartesian | Passed: E.3 applies to every \((u,v)\in B^2\) |
| Cross-branch | Passed for the main candidate; H.4 audits exactly two same-centre scales, not arbitrary shifted or many-scale systems |
| Full image | Passed: allowed residues times all archimedean lifts bounds the complete image |
| Collision direction | Passed: no use of Cauchy–Schwarz is reversed |
| Carrier recovery | The literal norm-one trace and \(GP\) carriers are rejected after bounded-fibre recovery |
| Degree-three height | Passed: \(2\max(X^3,q^2X)\) is exact |
| Lattice density | Passed: every input lower bound contains \(\sqrt\Delta=R^{d/2}\) |
| Class group | Paid explicitly in the unit-distance source; not invoked by the cubic lattice candidate |
| Denominator | Passed: \(q^3\) is cleared, the coefficient \(q^2\) and modulus \(q^2\) both remain in the ledger |
| Constant dependence | \(q,M,R,X\) are fixed before degree tends to infinity |
| Arbitrarily large | \(X>\sqrt R\) gives \(|A_j|\ge(X/\sqrt R)^{d_j}\to\infty\) |
| Real embedding | A field embedding is injective and commutes with \(F_2,F_3\) |

### G.3. Logical boundary and unresolved items

The following claims are **not** made:

- no lower bound for \(|F_3(A,A)|\) for arbitrary real \(A\);
- no disproof of the candidate conjecture;
- no claim that a disconnected or curved archimedean block has the same image size as its enclosing rectangle;
- no claim that separate bounds for unit monomials control their joint state;
- no novelty or literature-status claim.

The only conditional component of the final research direction is the fixed finite-dimensional inequality in Section I. Everything through Section H is an unconditional audit of the stated constructions and proof mechanisms.

## H. Failure library update

### H.1. Branch A — split-prime lattice sieve

**Closed assumptions.** The input is a dense translated Minkowski rectangle; the denominator is fixed and supported on completely split primes; all polynomial compression comes from cube residues modulo a divisor of \(M^2\); all global counting comes from one archimedean rectangle and norm-separated lifts.

**Fatal statement.** For one prime, the optimized base is \(R\delta_{q,2}(2q+1)>4R\). For anisotropic rectangles, every coordinate has the same lower minimum. Prime-power depth saturates and extra CRT primes worsen the product. At squarefree depth, even arbitrary correlations among residue coordinates cannot beat the fibre bound enough to pay the lift factor.

**Scope.** This closes the proof architecture, not the actual family of lattice sections under an unknown additional collision theorem.

### H.2. Branch B — unit-distance norm-one carrier

Let the source supply

\[
U=\{u_\varepsilon\}\subset Q_0^{-2}\mathcal O_K,
\qquad
|U|\ge e^{\gamma f},
\qquad
Q_0=\prod_{b=1}^tq_b,
\]

and define

\[
t(u)=u+u^{-1}\in L,
\qquad
T=t(U).
\]

The one-sided valuation vectors show that \(t\) is injective on \(U\), so \(|T|=|U|\), and all conjugates of \(T\) lie in \([-2,2]\). For \(x=t(u)\), \(y=t(v)\), put

\[
P=t(uv),\quad S=t(u/v),\quad D=x-y,\quad E=x+y.
\]

Then the exact identities are

\[
D^2=(P-2)(S-2),
\qquad
E^2=(P+2)(S+2),
\qquad
F_3(x,y)=D^3+E.
\]

The valuation pair \((uv,u/v)\) recovers the two ordered sign vectors coordinate by coordinate. Even after taking traces, \((u,v)\mapsto(t(uv),t(u/v))\) has fibres at most \(8\), and hence its image has at least \(|U|^2/8\) states.

The claimed recovery bound can be seen directly. Fix \(\xi=uv\), write \(v=\xi/u\), and set

\[
a=1-\xi^{-1},\quad b=1-\xi,\quad
c=1+\xi^{-1},\quad e=1+\xi.
\]

If \(z=F_3(t(u),t(v))\), then multiplication by \(u^3\) gives

\[
a^3u^6+(3a^2b+c)u^4-zu^3
+(3ab^2+e)u^2+b^3=0.
\]

This polynomial is nonzero and has degree at most \(6\); for \(\xi=1\), the surviving coefficients \(c=e=2\) keep it nonzero. The analogous substitution for fixed \(u/v\) has the same bound. Consequently

\[
|F_3(T,T)|\,|UU|\ge\frac{|U|^2}{6},
\qquad
|F_3(T,T)|\,|U/U|\ge\frac{|U|^2}{6}.
\]

Thus separate smallness of \(UU\) or \(U/U\) supplies no joint compression.

The robust full-image container also loses. Since \(T\subset\mathcal D^{-1}\mathcal O_L\), with \(\mathcal D=Q_0^2\),

\[
\mathcal D^3F_3(T,T)\subset\mathcal O_L,
\qquad
|\sigma(F_3(T,T))|\le68,
\]

and hence

\[
|F_3(T,T)|\le(136Q_0^6+1)^f.
\]

This container certificate is genuinely worse than the trivial pair count, even if the class fibre is larger than its guaranteed lower bound. Indeed,

\[
|T|=|U|\le2^{tf},
\qquad
(136Q_0^6+1)^f>Q_0^{6f}
\ge5^{6tf}>2^{2tf}\ge|T|^2.
\]

Cross-pairs make the sixth-order denominator genuine: when one sign coordinate is active and the other inactive, the cubic term has valuation \(-6\) and cannot cancel with the linear term of valuation \(-2\).

Finally, source translation overlap points the wrong way. For a fixed real difference \(d\),

\[
F_3(a,a-d)=d^3+2a-d
\]

is injective in \(a\). Many unit edges with one direction create many distinct outputs, while non-edge and cross-direction pairs remain uncontrolled.

**Closed assumptions.** Bounded-conjugate traces plus their fixed-denominator container; separate product/ratio collision counts; literal reuse of source translation overlap.

### H.3. Branch C — modified Phase-A hybrid

For \(A=GP\), the full expansion is

\[
F_3(gp,hq)
=p^3g^3-3p^2qg^2h+3pq^2gh^2-q^3h^3+pg+qh.
\]

The joint homogeneous carrier

\[
(g,h)\longmapsto(g^3,g^2h,gh^2,h^3)
\]

is injective over a totally real field; even \((g,h)\mapsto(g^2h,gh^2)\) is injective, because the only real cube root of \(1\) is \(1\). With \(r=h/g\),

\[
F_3(gp,rgq)=g^3(p-rq)^3+g(p+rq),
\]

so for fixed \(r,p,q\) every output has at most three possible scales \(g\). Same-scale pairs are only a \(1/|G|\) fraction of \(A^2\), and a bounded ratio set controls only a bounded multiple of that fraction.

Small multiplicative doubling is therefore insufficient even in the strongest elementary example:

\[
G_n=\{10^i:0\le i<n\}
\]

has \(|G_nG_n|=2n-1\) but \(|F_3(G_n,G_n)|=n^2\). Indeed, the coefficient vector of

\[
P_{ij}(T)=(T^i-T^j)^3+T^i+T^j
\]

recovers the ordered pair \((i,j)\). A difference of two such polynomials has coefficients of magnitude at most \(8\); at \(T=10\), its leading term strictly dominates the sum of all lower terms. Hence the \(P_{ij}(10)\) are pairwise distinct.

The Phase-A size and height ledgers make the rate failure explicit. Replacing \(c_0\) by \(\min(c_0,1)\) can only weaken the source bounds, so assume \(c_0\le1\). Put \(L=(1+\varepsilon)Xe^Y\). Then

\[
|A|\ge\frac{(c_0XY)^d}{Y\Delta^{3/2}},
\qquad
|F_3(A,A)|\le(21L^3)^d,
\]

and, under \(\Delta\le D_0^d\),

\[
\frac{|F_3(A,A)|}{|A|^2}
\le
Y^2\left[
\frac{21(1+\varepsilon)^3D_0^3Xe^{3Y}}{c_0^2Y^2}
\right]^d.
\]

Even the sharper set factorization

\[
F_3(A,A)\subset(A-A)^{[3]}+(A+A)
\]

only gives

\[
\frac{|F_3(A,A)|}{|A|^2}
\le
Y^2\left[
\frac{25(1+\varepsilon)^2D_0^3e^{2Y}}{c_0^2Y^2}
\right]^d,
\]

whose base is \(>1\) because the prescribed \(Y=4D_0^2/c_0\ge4\). Increasing \(X\) cancels out of this sharper comparison.

**Closed assumptions.** Literal small-\(|GG|\) transfer, independent monomial containers, diagonal/shared-scale arguments, and bounded-ratio variants. An engineered hybrid with a new theorem forcing exponential overlap across different \((r,p,q)\)-blocks is not ruled out.

### H.4. Branch D — anisotropic, thin, and multiscale windows

For a translated interval \([c-R,c+R]\), the exact cleared-output half-width is

\[
H_M(R)=\max\{8R^3,2M^2R\}.
\]

Thus a translated anisotropic rectangle has the full-image certificate

\[
|Z(B,B)|
\le\delta_m^d\prod_{i=1}^d\bigl(m+2H_M(R_i)\bigr).
\]

Each coordinate's normalized factor has the same minimum \(2M+m/M^2\). In fact, for good-prime support and every \(R>0\),

\[
\delta_m\bigl(m+2H_M(R)\bigr)>(2R+1)^2,
\]

so this proposed image bound exceeds the square of the universal input packing bound coordinate by coordinate. For completeness, put \(C=\delta_mm\ge3\) and \(E=\delta_mM\ge2\). On \(0<R\le M/2\), the difference between the two sides is the concave quadratic

\[
C-1+(4\delta_mM^2-4)R-4R^2,
\]

positive at both endpoints. On \(R\ge M/2\), it is

\[
C+16\delta_mR^3-(2R+1)^2;
\]

its value and derivative are positive at \(M/2\), and its derivative increases thereafter.

Allowing an algebraic denominator \(\mu\) with \(\mu^2\in m\mathcal O_L\) also fails: if \(a_i=|\sigma_i(\mu)|\), direct optimization and \(|N(\mu)|\ge m^{d/2}\) give the geometric-mean lower factor

\[
\left(\prod_i\Phi_{a_i,m}(R_i)\right)^{1/d}\ge2\sqrt m,
\]

which the cube density at good primes cannot pay. The displayed lower bound follows immediately from

\[
\Phi_{a_i,m}(R_i)
=\frac m{4R_i^2}+\max\{4R_i,a_i^2/R_i\}
\ge2a_i
\]

and \(|N(\mu)|\ge m^{d/2}\).

For two same-centre scales \(R\ge S\), the exact cross-block half-width is

\[
\max\{(R+S)^3+M^2(R-S),\ (R-S)^3+M^2(R+S)\},
\]

and its normalized factor is no smaller than the single-scale optimum. Indeed, with \(a=R+S\) and \(b=R-S\), its half-width is at least both \(a^3\) and \(M^2a\), while \(4RS=a^2-b^2\le a^2\); the normalized expression is therefore at least

\[
\frac m{a^2}+2\max\{a,M^2/a\}
\ge2M+\frac m{M^2}.
\]

A thin shell treated merely as a subset of an enclosing rectangle inherits the failed bound; opposite-sign shell pairs retain a cubic span of order \(R^2w\).

**Closed assumptions.** Full rectangles; shells controlled only by their enclosing rectangles; same-centre scale blocks whose images are bounded separately. **Not closed:** a genuinely nonrectangular correlated block whose actual continuous polynomial image has a much smaller covering number. That is the sole direction retained in Section I.

### H.5. Common obstruction

The quadratic baseline wins because each split-prime coordinate contributes about one bit of residue saving while the quadratic archimedean scale matches the two-input benchmark \(X^2\). In the cubic problem, the difference and sum variables form a diamond, and even its exact optimization leaves a scale comparable to \(M\) after normalization. The cube density is only about \(1/3\), so denominator height consumes more than the entire local gain. The source entropies do not help: norm-one signs and unit products remain recoverable carrier labels. Any successful next mechanism must compress the **whole** polynomial image before the final lattice packing step.

## I. Exactly one next statement

The residue-code replacement is not viable: for odd \(q\), the invertible change of variables \(u=x-y, v=x+y\) gives \(\overline F_3(x,y)=u^3+v\), so every output in \(\mathbb F_q\) has exactly \(q\) ambient preimages. Coordinatewise, every fibre has \(q^d\) points, and every \(\mathcal C\subset\mathbb F_q^d\) obeys

\[
|\overline F_3^{\otimes d}(\mathcal C,\mathcal C)|
\ge\frac{|\mathcal C|^2}{q^d}.
\]

The next direction must therefore leave residue density behind.

Fix the nested totally real tower \((L_j)\) and put

\[
R=\sup_j\operatorname{rd}(L_j)<\infty.
\]

For a bounded set \(S\subset\mathbb R^m\), let \(N_1(S)\) be the least number of translates of half-open, axis-parallel unit \(m\)-cubes covering \(S\). For \(W\subset\mathbb R^m\), define the coordinatewise image

\[
\mathcal F_m(W,W)=
\{(x-y)^{\circ3}+x+y:x,y\in W\}.
\]

Here is the complete conditional deduction. Suppose a tower stage \(L_{j_0}\) has degree \(m\), and \(W\subset\mathbb R^m\) is a finite union of bounded rational axis-parallel boxes. For a later stage write

\[
d_j=[L_j:\mathbb Q]=mk_j
\]

and set \(\Omega_j=W^{k_j}\subset\mathbb R^{d_j}\), after ordering the embeddings into \(k_j\) blocks of size \(m\). Torus averaging gives a translate \(t_j+\Omega_j\) whose lattice section

\[
B_j=\{\alpha\in\mathcal O_{L_j}:\Phi_j(\alpha)\in t_j+\Omega_j\}
\]

satisfies

\[
|B_j|
\ge\frac{\operatorname{vol}(W)^{k_j}}{\sqrt{|\Delta_{L_j}|}}
\ge
\left(\frac{\operatorname{vol}(W)}{R^{m/2}}\right)^{k_j}.
\]

Let \(A_j=\sigma_1(B_j)\). If \(\Phi_j(\alpha)=t_j+x\) and \(\Phi_j(\beta)=t_j+y\), then

\[
\Phi_j(F_3(\alpha,\beta))
=2t_j+(x-y)^{\circ3}+x+y.
\]

Consequently

\[
\Phi_j(F_3(B_j,B_j))
\subset
2t_j+\mathcal F_m(W,W)^{k_j}.
\]

A half-open unit \(d_j\)-cube contains at most one embedded algebraic integer: two would have a nonzero integral difference with every conjugate of modulus \(<1\), contradicting the norm. Thus, with

\[
N=N_1(\mathcal F_m(W,W)),
\qquad
K=N_1(W),
\]

one has

\[
|F_3(A_j,A_j)|\le N^{k_j},
\qquad
|A_j|\le K^{k_j}.
\]

If

\[
\eta=\frac{R^mN}{\operatorname{vol}(W)^2}<1,
\]

then \(N\ge1\) forces \(\operatorname{vol}(W)>R^{m/2}\), so \(|A_j|\to\infty\), and \(K>1\). Moreover,

\[
\frac{|F_3(A_j,A_j)|}{|A_j|^2}\le\eta^{k_j}
\le |A_j|^{-c},
\qquad
c=\frac{\log(1/\eta)}{\log K}>0.
\]

This checks every Cartesian and cross-block pair because

\[
\mathcal F_{mk_j}(W^{k_j},W^{k_j})
=\mathcal F_m(W,W)^{k_j}
\]

exactly. This rational-box requirement makes a successful inequality a fixed, finite certificate: its volume is exact, and an explicit unit-cube cover of its polynomial image can be verified by interval arithmetic. It is enough to exhibit a cover with \(\widehat N\) cubes satisfying \(R^m\widehat N<\operatorname{vol}(W)^2\); one need not certify that \(\widehat N=N_1(\mathcal F_m(W,W))\). This is structurally different from the denominator sieve and strictly simpler than constructing an asymptotic real family.

> **Finite archimedean cancellation-block conjecture.** For the fixed tower above, there exist a tower-stage degree \(m\) and a set \(W\subset\mathbb R^m\) that is a finite union of bounded rational axis-parallel boxes such that
> \[
> \boxed{
> R^mN_1\!\left(\mathcal F_m(W,W)\right)
> <\operatorname{vol}_m(W)^2.
> }
> \]
