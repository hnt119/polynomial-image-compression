# Quadratic-to-Cubic Transfer Checkpoint

## Exact audit of the split-prime witness for

\[
R(x,y)=(x-y)^2+5(x+y)
\quad\text{and}\quad
P_3(x,y)=(x-y)^3-3(x+y)
\]

This note was prepared completely offline. It uses only the supplied positive-polynomial checkpoint, the supplied split-prime polynomial report, the supplied unit-distance proof, and standard results stated below. No external verification is claimed.

## Main conclusion

The quadratic split-prime theorem does not specify a unique witness sequence; its prime set and Minkowski radius are parameters. There is a fully admissible, explicit specialization of that construction for which the transfer to \(P_3\) fails in the strongest possible way.

**Theorem (maximal loss on an admissible quadratic witness).** The selected split primes in the supplied quadratic construction can all be chosen with

\[
q\equiv 5\pmod {12}.
\]

Put \(Q=\prod q\) and take the Minkowski radius \(T=Q/8\). After fixing sufficiently many selected primes, the resulting sets \(A_j\) satisfy, for a fixed \(c_0>0\),

\[
|R(A_j,A_j)|\le |A_j|^{2-c_0},
\qquad |A_j|\longrightarrow\infty,
\]

but

\[
\boxed{|P_3(A_j,A_j)|=|A_j|^2}
\]

for every tower layer \(j\).

Thus verdict **3** applies to this explicit realization: the quadratic witness rigorously loses all of its exponential saving when passed to the cubic. This is not a universal impossibility theorem for every permitted choice of primes and window in the broader quadratic architecture, and it does not disprove CPSI.

# A. Imported quadratic witness

## A.1. Arithmetic tower

Fix a sufficiently large auxiliary integer \(\ell\). The supplied construction starts with primes \(r_1,\ldots,r_\ell\equiv1\pmod3\) and a totally real cyclic cubic field \(F/\mathbb Q\) with

\[
D_\ell:=\operatorname{rd}(F)
=\left(\prod_{i=1}^{\ell}r_i\right)^{2/3},
\qquad
\log D_\ell=O(\ell\log\ell).
\]

Its unramified pro-\(3\) construction permits

\[
t=\left\lfloor\frac{(\ell-1)^2}{100}\right\rfloor
\asymp \ell^2
\]

fixed rational primes to be forced to split completely in an infinite tower

\[
F=K_0\subset K_1\subset K_2\subset\cdots,
\qquad n_j=[K_j:\mathbb Q]\longrightarrow\infty.
\]

Every \(K_j\) is totally real and

\[
\operatorname{rd}(K_j)=D_\ell.
\]

For this polynomial construction the fields are the totally real layers \(K_j\) themselves. The CM fields and class-number factor used elsewhere in the unit-distance argument do not enter the lattice count below.

### Refining the split primes to \(q\equiv5\pmod{12}\)

This congruence refinement needs a compatibility argument; it does not follow merely by taking a subcollection of primes congruent to \(1\pmod4\).

Let \(E/F\) be the finite Frattini quotient extension in the supplied tower proof, and let \(\widetilde E\) be its normal closure over \(\mathbb Q\). The conjugates of \(E/F\) are \(3\)-extensions over the cyclic cubic field \(F\). Their compositum is therefore a \(3\)-extension over \(F\), so \(\widetilde E/\mathbb Q\) is Galois of \(3\)-power degree. It is totally real: a real place cannot become complex in a Galois extension of odd degree, since the decomposition group at an archimedean place would then have order \(2\).

Consequently

\[
\operatorname{Gal}(\widetilde E(i)/\mathbb Q)
\cong \operatorname{Gal}(\widetilde E/\mathbb Q)\times C_2.
\]

An odd-order group has no quotient of order \(2\), so \(\mathbb Q(i)\) is the unique quadratic subfield of \(\widetilde E(i)\). Since \(\mathbb Q(i)\ne\mathbb Q(\zeta_3)\),

\[
\widetilde E(i)\cap\mathbb Q(\zeta_3)=\mathbb Q.
\]

Apply Chebotarev to the compositum \(\widetilde E(i,\zeta_3)\), prescribing identity Frobenius on \(\widetilde E(i)\) and nonidentity Frobenius on \(\mathbb Q(\zeta_3)\). Infinitely many unramified rational primes have that Frobenius. They split completely in \(\widetilde E(i)\), so they are \(1\pmod4\), and they are inert in \(\mathbb Q(\zeta_3)\), so they are \(2\pmod3\). Hence they are \(5\pmod{12}\). Any fixed finite set, including \(2,3,5\) and all ramified primes, may be excluded.

Choose \(t\) such primes \(q_1,\ldots,q_t\). Killing their Frobenius elements adds the same \(3t\) Frattini relations as in the supplied proof, so neither the Golod-Shafarevich calculation nor the root-discriminant bound changes.

Put

\[
Q=\prod_{s=1}^t q_s,
\qquad
\rho=\prod_{s=1}^t\frac{q_s+1}{2q_s}.
\]

If \(5\) is excluded, then \(q_s\ge17\), and therefore

\[
Q\ge17^t,
\qquad
\rho\le\left(\frac9{17}\right)^t.
\tag{A.1}
\]

## A.2. Minkowski window and the real set

Fix

\[
T=\frac Q8.
\]

For each tower layer define

\[
B_j(T)=\left\{
b\in\mathcal O_{K_j}: |\tau(b)|\le T
\text{ for every real embedding }\tau:K_j\hookrightarrow\mathbb R
\right\}.
\]

Choose one real embedding \(\sigma_j:K_j\hookrightarrow\mathbb R\), and set

\[
\boxed{
A_j=\left\{\frac{\sigma_j(b)}Q:b\in B_j(T)\right\}.
}
\tag{A.2}
\]

The full Minkowski lattice \(\Phi_j(\mathcal O_{K_j})\subset\mathbb R^{n_j}\) has covolume \(\sqrt{|\Delta_{K_j}|}\). Blichfeldt averaging, followed by subtracting one lattice point from all points in a favorable translate of a cube of side \(T\), gives

\[
|B_j(T)|
\ge \frac{T^{n_j}}{\sqrt{|\Delta_{K_j}|}}
=\left(\frac{T}{\sqrt{D_\ell}}\right)^{n_j}.
\]

Distinct algebraic integers are \(1\)-separated in Minkowski sup norm: otherwise every conjugate of their nonzero difference would have modulus less than \(1\), contradicting the integrality and nonvanishing of its norm. Packing gives

\[
|B_j(T)|\le(2T+1)^{n_j}.
\]

The embedding and division by \(Q\) are injective. Thus all elements of \(A_j\) are distinct and

\[
\boxed{
\left(\frac{Q}{8\sqrt{D_\ell}}\right)^{n_j}
\le |A_j|
\le\left(\frac Q4+1\right)^{n_j}.
}
\tag{A.3}
\]

Because \(t\asymp\ell^2\), \(\log D_\ell=O(\ell\log\ell)\), and \(Q\ge17^t\), one has \(Q/(8\sqrt{D_\ell})>1\) once \(\ell\) is sufficiently large. After such an \(\ell\) is fixed, (A.3) proves \(|A_j|\to\infty\) as \(n_j\to\infty\).

## A.3. Quadratic output restriction and exponent

The homogeneous pieces of \(R\) have oscillations on \([-1,1]^2\)

\[
\omega_2=4,
\qquad
\omega_1=20.
\]

For \(b,c\in B_j(T)\), put \(d=b-c\) and clear the denominator:

\[
S(b,c)=Q^2R(b/Q,c/Q)=d^2+5Q(b+c).
\tag{A.4}
\]

For each \(q_s\mid Q\), complete splitting gives

\[
\mathcal O_{K_j}/q_s\mathcal O_{K_j}\cong\mathbb F_{q_s}^{,n_j}.
\]

Modulo this ring, \(S\equiv d^2\), so every residue coordinate belongs to the \((q_s+1)/2\)-element square set. Across all selected primes, the number of permitted residue classes modulo \(Q\mathcal O_{K_j}\) is

\[
(Q\rho)^{n_j}.
\]

In every real embedding, \(S\) lies in an interval of length at most

\[
W_R(T)=4T^2+20QT.
\]

Points in one residue class modulo \(Q\mathcal O_{K_j}\) are \(Q\)-separated in Minkowski sup norm. Hence

\[
|R(A_j,A_j)|
=|S(B_j(T),B_j(T))|
\le\left[\rho\bigl(Q+4T^2+20QT\bigr)\right]^{n_j}.
\tag{A.5}
\]

Combining (A.3) and (A.5),

\[
|R(A_j,A_j)|\le\Theta_R(T)^{n_j}|A_j|^2,
\]

where

\[
\Theta_R(T)
=D_\ell\rho\left(4+\frac{20Q}{T}+\frac Q{T^2}\right).
\]

At \(T=Q/8\),

\[
\boxed{
\Theta_R
=D_\ell\rho\left(164+\frac{64}{Q}\right).
}
\tag{A.6}
\]

By (A.1), \(\Theta_R\le168D_\ell(9/17)^t\), which tends to \(0\) as \(\ell\to\infty\). Fix \(\ell\) large enough that \(T>\sqrt{D_\ell}\) and \(\Theta_R<1\). All of \(D_\ell,t,q_s,Q,T,\rho\), and \(\Theta_R\) are thereafter fixed while \(j\to\infty\). The imported quadratic exponent may be taken to be

\[
\boxed{
c_0=
\min\left\{
1,
\frac{-\log\Theta_R}{\log(Q/4+1)}
\right\}>0.
}
\tag{A.7}
\]

This completes the construction and the quadratic gain-loss ledger. No denominator, discriminant, class-number, or field-degree factor is hidden in (A.6).

# B. Bridge identity

Write

\[
u=x-y,
\qquad s=x+y.
\]

Since \(R=u^2+5s\),

\[
5P_3=5(u^3-3s)=5u^3+3u^2-3R.
\tag{B.1}
\]

For a finite real set \(A\), define

\[
\Gamma_A
=\{(u,r):u=x-y,\ r=R(x,y),\ x,y\in A\}.
\]

The map \((x,y)\mapsto(u,r)\) is injective: from \((u,r)\),

\[
s=\frac{r-u^2}{5},
\qquad
x=\frac{s+u}{2},
\qquad
y=\frac{s-u}{2}.
\]

Therefore

\[
|\Gamma_A|=|A|^2
\tag{B.2}
\]

and, for \(F(u)=5u^3+3u^2\),

\[
5P_3(A,A)=\{F(u)-3r:(u,r)\in\Gamma_A\}.
\tag{B.3}
\]

For the witness (A.2), write \(x=b/Q\), \(y=c/Q\), and \(d=b-c\). In addition to (A.4), define

\[
Z(b,c)=Q^3P_3(b/Q,c/Q)
=d^3-3Q^2(b+c).
\tag{B.4}
\]

Eliminating \(b+c\) between (A.4) and (B.4) gives

\[
\boxed{5Z=5d^3+3Qd^2-3QS.}
\tag{B.5}
\]

For every selected \(q\mid Q\), directly from (A.4) and (B.4),

\[
\boxed{S\equiv d^2\pmod{q\mathcal O_{K_j}},
\qquad Z\equiv d^3\pmod{q\mathcal O_{K_j}}.}
\tag{B.6}
\]

The second congruence is taken directly from (B.4); no division by \(5\) is involved.

# C. Local entropy analysis

Let \(q\) be an odd prime and put \(g_q=\gcd(3,q-1)\). Cyclicity of \(\mathbb F_q^\times\) gives the following exact table.

| Map on \(\mathbb F_q\) | Image size | Nonzero fiber size |
| --- | ---: | ---: |
| \(d\mapsto d^2\) | \((q+1)/2\) | \(2\) over a nonzero square |
| \(d\mapsto d^3\) | \(1+(q-1)/g_q\) | \(g_q\) over a nonzero cube |
| \(d\mapsto(d^2,d^3)\) | \(q\) | \(1\) |

The joint map is injective over every field. If \(d^2\ne0\), then

\[
d=\frac{d^3}{d^2};
\]

if \(d^2=0\), then \(d=0\). Its image is the cusp

\[
\{(s,z)\in\mathbb F_q^2:z^2=s^3\}.
\]

In particular, if \(s=d^2\ne0\), its two roots \(d\) and \(-d\) have distinct cube values \(d^3\) and \(-d^3\). The cubic coordinate recovers the exact sign bit that the square coordinate forgot.

For one split prime and field degree \(n\), a square residue vector has \(2^w\) roots, where \(w\) is its number of nonzero coordinates; their cube vectors are all distinct. Across all selected primes, the square residue support has size

\[
(Q\rho)^n,
\]

whereas the joint \((S,Z)\)-support has size

\[
Q^n.
\]

Thus adjoining \(Z\) restores exactly the support-count gain

\[
-n\log\rho
=n\sum_{q\mid Q}\log\frac{2q}{q+1}
\tag{C.1}
\]

used by the quadratic residue restriction.

There is also an exact Shannon-entropy statement, used only as a diagnostic and not as an assumption about the distribution of the Minkowski box. If \(D\) is uniform on \(\mathbb F_q\), \(S=D^2\), and \(Z=D^3\), then, in bits,

\[
H(D\mid S)=1-\frac1q,
\qquad
H(D\mid S,Z)=0.
\]

Therefore \(I(D;Z\mid S)=1-1/q\): every conditional sign bit, including the zero correction, is recovered.

For the chosen primes \(q\equiv5\pmod{12}\), \(g_q=1\), so cubing itself is a permutation of \(\mathbb F_q\). Hence \(Z\bmod q\), without \(S\), recovers \(d\bmod q\). By contrast, if \(q\equiv1\pmod{12}\), cubing has three-element nonzero fibers and cube-image density \((q+2)/(3q)\). Those three roots lie in three different square classes; this is new cube-root ambiguity across quadratic labels, not survival of the old \(\pm\) ambiguity.

The small primes cause no hidden exception:

- \(q=2\): squaring and cubing are both the identity, so the quadratic restriction has no sign saving.
- \(q=3\): \(d^3=d\), so cubing is bijective.
- \(q=5\): cubing is bijective. If it were retained, (B.6) must be read directly from (B.4), rather than obtained by dividing (B.5) by \(5\). In the explicit construction above it was simply excluded.

# D. Global fiber and collision analysis

## D.1. Exact injectivity inside every quadratic fiber

The local recovery has a stronger global consequence which does not require \(q\equiv2\pmod3\) or a narrow window.

For a fixed algebraic-integer quadratic output \(S_0\), define

\[
U_{S_0}
=\{d=b-c:b,c\in B_j(T),\ S(b,c)=S_0\}.
\]

Given \(S_0\) and \(d\), equation (A.4) determines \(b+c\), hence determines \((b,c)\). Therefore

\[
\sum_{S_0}|U_{S_0}|=|B_j(T)|^2.
\tag{D.1}
\]

Put

\[
G_Q(d)=5d^3+3Qd^2.
\]

**Fiber lemma.** The map \(d\mapsto G_Q(d)\) is injective on every \(U_{S_0}\).

**Proof.** Suppose \(d,e\in U_{S_0}\) and \(G_Q(d)=G_Q(e)\). By (B.5), the two pairs have the same \(Z\). Modulo every selected \(q\), they therefore have the same \((d^2,d^3)\). Joint injectivity gives

\[
d-e\in Q\mathcal O_{K_j};
\qquad d-e=Qh.
\]

If \(d\ne e\), factoring \(G_Q(d)-G_Q(e)=0\) gives

\[
5(d^2+de+e^2)+3Q(d+e)=0.
\]

Let \(a=d+e\). Since

\[
d^2+de+e^2=\frac{3a^2+Q^2h^2}{4},
\]

division by \(Q^2\) in the characteristic-zero field gives

\[
15(a/Q)^2+12(a/Q)+5h^2=0,
\]

or

\[
15\left(a/Q+\frac25\right)^2+5h^2=\frac{12}{5}.
\tag{D.2}
\]

Under every real embedding, (D.2) implies

\[
|\tau(h)|\le\frac{\sqrt{12}}5<1.
\]

But a nonzero algebraic integer has nonzero integral norm, whose absolute value is at least \(1\). The product of the displayed strict bounds would make \(|N(h)|<1\). Thus \(h=0\), contrary to \(d\ne e\). Hence \(d=e\). \(\square\)

For fixed \(S_0\), (B.5) now shows that the cubic values above this fiber form a set of cardinality exactly \(|U_{S_0}|\). Consequently

\[
\sum_{S_0}
\left|G_Q(U_{S_0})-3QS_0\right|
=|B_j(T)|^2.
\tag{D.3}
\]

Equivalently, \((b,c)\mapsto(S(b,c),Z(b,c))\) is injective. Hence

\[
|R(A_j,A_j)|\,|P_3(A_j,A_j)|\ge |A_j|^2,
\]

and every cubic fiber meets any fixed quadratic fiber in at most one ordered pair. Thus none of the large exact fibers responsible for the small quadratic image remains a fiber of the cubic. Any cubic saving on a different choice of quadratic witness would have to arise from exponential overlap between the translated sets in (D.3), not from compression within one quadratic fiber.

## D.2. The exact collision equation

Let \((b,c)\) and \((b',c')\) have differences \(d,d'\), sums \(s,s'\), quadratic outputs \(S,S'\), and cubic outputs \(Z,Z'\). Equality \(Z=Z'\) is

\[
d^3-d'^3=3Q^2(s-s').
\tag{D.4}
\]

Using (A.4), this is equivalent to

\[
5(d^3-d'^3)+3Q(d^2-d'^2)=3Q(S-S'),
\tag{D.5}
\]

and hence to

\[
(d-d')
\left(5(d^2+dd'+d'^2)+3Q(d+d')\right)
=3Q(S-S').
\tag{D.6}
\]

These are equalities in \(\mathcal O_{K_j}\), not merely coordinatewise numerical identities.

## D.3. Global pair-injectivity on the chosen witness

Suppose \(Z(b,c)=Z(b',c')\). Reducing (B.4) modulo a selected \(q\) gives

\[
d^3\equiv d'^3\pmod{q\mathcal O_{K_j}}.
\]

Complete splitting identifies the quotient with \(\mathbb F_q^{n_j}\). Since \(q\equiv2\pmod3\), cubing is a permutation in each factor. Hence

\[
d\equiv d'\pmod{q\mathcal O_{K_j}}
\]

for every selected \(q\). The ideals \(q\mathcal O_{K_j}\) are pairwise comaximal, so the ideal Chinese remainder theorem gives

\[
d-d'\in Q\mathcal O_{K_j};
\qquad d-d'=Q\beta
\]

for some \(\beta\in\mathcal O_{K_j}\).

On the other hand, for every real embedding \(\tau\),

\[
|\tau(d-d')|
\le |\tau(b)|+|\tau(c)|+|\tau(b')|+|\tau(c')|
\le4T=\frac Q2<Q.
\]

If \(\beta\ne0\), norm integrality forces \(|\tau(\beta)|\ge1\) for at least one embedding, and then \(|\tau(Q\beta)|\ge Q\), a contradiction. Thus \(d=d'\). Returning to (B.4) gives \(s=s'\), and

\[
b=\frac{s+d}{2}=b',
\qquad
c=\frac{s-d}{2}=c'.
\]

The chosen real embedding is injective, so equality of real outputs is equivalent to equality of the cleared algebraic-integer outputs. We have proved injectivity on the entire ordered Cartesian square:

\[
\boxed{|P_3(A_j,A_j)|=|A_j|^2.}
\tag{D.7}
\]

In particular, every solution of (D.5)-(D.6) inside the actual box is diagonal, and the cubic collision energy is exactly \(|A_j|^2\).

More generally, if \(Q_-\) is the product of those selected primes for which cubing is bijective, the same proof gives pair-injectivity whenever \(4T<Q_-\). The explicit specialization has \(Q_-=Q\).

## D.4. Why unit-distance averaging does not restore compression

There is a literal torus-averaging analogue, but it points in the wrong direction. Let \(\Lambda=\Phi_j(\mathcal O_{K_j})\), \(W=[-T,T]^{n_j}\), and \(X_a=(a+\Lambda)\cap W\). For a difference \(d\), anchors \(b\) with \(b,b-d\in X_a\) lie in a two-window overlap. The standard lattice-unfolding identity computes its average over \(a\in\mathbb R^{n_j}/\Lambda\).

On such a slice, however,

\[
Z_d(b)=d^3-3Q^2(2b-d)
=\Psi_Q(d)-6Q^2b,
\qquad
\Psi_Q(d)=d^3+3Q^2d.
\tag{D.8}
\]

For fixed \(d\), the map \(b\mapsto Z_d(b)\) is injective. Two difference slices \(d,e\) can overlap only if

\[
\frac{\Psi_Q(d)-\Psi_Q(e)}{6Q^2}\in\mathcal O_{K_j}.
\tag{D.9}
\]

If (D.9) holds, their averaged intersection is a four-window volume divided by \(\operatorname{covol}(\Lambda)\); if it fails, it is zero. The translating coset \(a\) cancels from (D.9), so torus averaging cannot manufacture the missing arithmetic collisions. Moreover the square-root patterns forgotten by \(d^2\) have distinct \(d^3\)-residues, so averaging those slices counts distinct cubic outputs. Unlike unit distance, the output is not invariant under the anchor: the term \(-6Q^2b\) remains.

Finally, a translation family controls only selected pairs, whereas an upper bound for \(P_3(A,A)\) must control every pair of the full Cartesian square. Ordinary residue packing of all outputs recovers only the already-closed degree-three container. On the witness used here, (D.7) is conclusive: no averaging choice can create a collision that does not exist.

# E. Verdict on the quadratic seed

**Verdict 3: the explicit quadratic witness above is rigorously shown to lose its exponential saving for the cubic.**

The result is stronger than failure of a proposed upper bound. The map

\[
(x,y)\longmapsto P_3(x,y)
\]

is injective on \(A_j\times A_j\). Equivalently, the projection

\[
(u,r)\longmapsto 5u^3+3u^2-3r
\]

is injective on the full correlated graph \(\Gamma_{A_j}\). Therefore the target (QT) fails for every \(c>0\) on this sequence.

The exact mechanism is now clear:

1. The quadratic restriction \(S\equiv d^2\) deletes square-root signs.
2. The joint residue \((S,Z)\equiv(d^2,d^3)\) restores every deleted sign for every odd prime.
3. For \(q\equiv5\pmod{12}\), \(Z\equiv d^3\) alone restores \(d\bmod Q\).
4. The window inequality \(4T<Q\) makes that residue lift unique.
5. The exact cubic output then restores \(b+c\), so it restores the ordered pair.

What has been ruled out is automatic transfer of the successful square-image mechanism. What has not been ruled out is a different legal choice of quadratic parameters whose cube-root ambiguity creates exponential overlap across distinct quadratic fibers, or an unrelated construction for CPSI.

# F. Exponents and rate ledger

The quadratic exponent is the explicit fixed number (A.7). No positive cubic exponent exists on this sequence because of (D.7).

For the requested exponential ledger, pass to a subsequence along which

\[
a_j:=\frac1{n_j}\log|A_j|\longrightarrow a.
\]

Such a subsequence exists by (A.3), and \(a>0\). Put

\[
\varepsilon_0=-\log\Theta_R>0.
\]

Then

\[
|A_j|=e^{a n_j+o(n_j)},
\]

\[
|R(A_j,A_j)|
\le e^{(2a-\varepsilon_0)n_j+o(n_j)},
\]

whereas

\[
|P_3(A_j,A_j)|
=e^{2a n_j+o(n_j)}.
\]

Thus at least the entire imported rate \(\varepsilon_0\) is lost. More exactly, after a further subsequence let

\[
r=\lim_j\frac1{n_j}\log|R(A_j,A_j)|,
\qquad
\varepsilon_R=2a-r\ge\varepsilon_0.
\]

The increase from the actual quadratic rate \(r\) to the cubic rate \(2a\) is

\[
\eta_{\rm lost}=2a-r=\varepsilon_R.
\]

Therefore the exact net collision rate is

\[
\boxed{\varepsilon_R-\eta_{\rm lost}=0.}
\tag{F.1}
\]

There is consequently no formula \(c=(\varepsilon_R-\eta_{\rm lost})/a>0\) for this witness; it gives \(c=0\).

# G. Independent proof audit

## G.1. Standard theorems invoked

The substantial standard inputs, in the precise forms used, are:

1. **Prime number theorem in the progression \(1\pmod3\), weak form.** The first \(\ell\) primes in that progression have total logarithm \(O(\ell\log\ell)\). This supplies \(\log D_\ell=O(\ell\log\ell)\) in the supplied base-field construction.
2. **Shafarevich relation-rank estimate, supplied version.** For the maximal everywhere-unramified pro-\(3\) extension of the totally real cubic base field used in the report, the relation rank is at most the generator rank plus an absolute constant.
3. **Golod-Shafarevich inequality, pro-\(p\) form.** A nontrivial finite pro-\(p\) group with generator rank \(d\) and relation rank \(r\) satisfies \(r>d^2/4\). Thus the quotient in the supplied proof is infinite once its relation count is at most \(d^2/4\).
4. **Chebotarev density theorem.** If \(L/\mathbb Q\) is finite Galois and \(C\) is a conjugacy class in \(\operatorname{Gal}(L/\mathbb Q)\), the unramified rational primes with Frobenius class \(C\) have density \(|C|/|\operatorname{Gal}(L/\mathbb Q)|\). It is applied to the singleton central class \((1,\text{nonidentity})\) in \(\widetilde E(i,\zeta_3)\).
5. **Unramified discriminant formula.** A finite extension unramified at every finite prime has unchanged root discriminant. Odd-degree Galois extensions of a totally real field remain totally real.
6. **Blichfeldt averaging.** A measurable set of volume \(V\) contains, in some translate relative to a lattice of covolume \(\delta\), at least \(V/\delta\) lattice points. Subtraction converts the favorable translate into the centered box used here.
7. **Ideal Chinese remainder theorem.** Reduction modulo pairwise comaximal ideals is the product of the individual reductions; in particular, \(d\equiv d'\pmod{q\mathcal O_K}\) for every \(q\mid Q\) implies \(d-d'\in Q\mathcal O_K\).
8. **Finite-field power-map count.** Since \(\mathbb F_q^\times\) is cyclic, \(x\mapsto x^r\) has kernel size \(\gcd(r,q-1)\) and image size \((q-1)/\gcd(r,q-1)\) on nonzero elements.
9. **Lattice unfolding, in the averaging audit.** For a full lattice \(\Lambda\subset V\), Haar probability on \(V/\Lambda\), and integrable \(h\),
   \[
   \int_{V/\Lambda}\sum_{\lambda\in\Lambda}h(a+\lambda)\,da
   =\frac1{\operatorname{covol}(\Lambda)}\int_Vh(x)\,dx.
   \]

## G.2. Checklist

| Audit item | Verification |
| --- | --- |
| Distinct real inputs | A field embedding is injective; division by fixed nonzero \(Q\) preserves distinctness. |
| Growing parameter | \(\ell,Q,T,D_\ell\) are fixed first; only \(n_j\to\infty\). |
| Constants | \(c_0\), \(Q\), \(T\), \(\rho\), and \(D_\ell\) are independent of \(j\). |
| Denominators | \(R\) is cleared by \(Q^2\); \(P_3\) is cleared by \(Q^3\). The resulting maps into \(\mathcal O_{K_j}\). |
| Output counting | The maps \(S\mapsto\sigma_j(S)/Q^2\) and \(Z\mapsto\sigma_j(Z)/Q^3\) are injective, so algebraic and real image cardinalities agree. |
| Split reductions | Complete splitting gives exactly \(n_j\) copies of \(\mathbb F_q\); no residue-degree factor is omitted. |
| CRT | Distinct rational-prime ideals are comaximal and their product is \(Q\mathcal O_{K_j}\). |
| Unique lift | \(4T=Q/2<Q\), and norm integrality excludes a nonzero element of \(Q\mathcal O_{K_j}\) inside that window. |
| Root discriminant | It appears as the factor \(D_\ell\) in \(\Theta_R\); unramified layers add no further loss. |
| Class number | No ideal-class choice is made in this polynomial witness, so there is no class-number loss. |
| Exceptional primes | \(2,3,5\) and all ramified primes may be excluded. Even if \(5\) were retained, the direct congruence \(Z\equiv d^3\) remains valid. |
| Full Cartesian requirement | The injectivity proof applies to every ordered pair in \(B_j(T)^2\), not to a selected edge subset. |
| Scope | The theorem concerns a legal explicit specialization; it does not quantify over every possible prime/window choice in the split-prime architecture. |

# H. Exactly one next statement

The smallest remaining test of the quadratic architecture is the complementary cube-root regime:

**Complementary-prime witness problem.** Choose the split primes in the same supplied tower with \(q\equiv1\pmod{12}\) (compatible by the same disjoint-compositum Chebotarev argument), put \(Q=\prod q\), take \(T=Q/8\), and define \(A_j\) by (A.2). Determine whether there exists a fixed \(\eta>0\) such that

\[
\boxed{
\left|
\left\{(b-c)^3-3Q^2(b+c):b,c\in B_j(T)\right\}
\right|
\le e^{-\eta n_j}|B_j(T)|^2
}
\]

for arbitrarily large \(j\).

Here the cubic residue has genuine threefold fibers, but the fiber lemma proves that any saving must come from overlap across distinct exact quadratic outputs. Resolving this one statement decides whether the only remaining local cube-root ambiguity in the quadratic witness can become a global cubic power saving.
