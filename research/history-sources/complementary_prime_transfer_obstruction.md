# Complementary Split-Prime Transfer Obstruction

## Asymptotic injectivity for \(P_3(x,y)=(x-y)^3-3(x+y)\)

This report was prepared completely offline. It uses the five frozen facts in
the research checkpoint, the already-audited construction for

\[
R(x,y)=(x-y)^2+5(x+y),
\]

and the standard results stated in Section I. No external verification is
claimed.

## A. Frozen checkpoint

The following inputs are used without re-proving them.

1. The totally real bounded-root-discriminant tower and its completely split
   auxiliary primes.
2. The Minkowski-box construction of the quadratic witness, including its
   lattice counts and the estimate
   \[
   |R(A_j,A_j)|\le \Theta_R^{n_j}|A_j|^2,
   \qquad \Theta_R<1.
   \]
3. The bridge identity
   \[
   5P_3(x,y)=5(x-y)^3+3(x-y)^2-3R(x,y).
   \]
4. Injectivity of the cubic map inside every exact quadratic-output fiber.
5. Maximal failure of transfer for the previously treated primes
   \(q\equiv5\pmod {12}\).

Only the complementary choice \(q\equiv1\pmod {12}\) is analyzed below.

## B. Verdict: Outcome III

The Complementary Root Overlap Conjecture is false for the explicit
\(T=Q/8\) quadratic witness. In fact, the opposite phenomenon holds: the
cubic map is asymptotically injective.

### Main theorem

Let \(K\) be totally real of degree \(n\), with
\(\operatorname{rd}(K)\le D\). Let

\[
Q=\prod_{q\in\mathcal S}q,
\qquad |\mathcal S|=t,
\]

where the rational primes in \(\mathcal S\) are distinct, satisfy
\(q\equiv1\pmod {12}\), and split completely in \(K\). Define

\[
\mathcal B=B_K(Q/8)
=\{b\in\mathcal O_K:|\sigma(b)|\le Q/8
\text{ for every real embedding }\sigma\},
\qquad N=|\mathcal B|,
\]

and, for one real embedding \(\sigma_0\),

\[
A=\left\{\frac{\sigma_0(b)}Q:b\in\mathcal B\right\}.
\]

Put

\[
\delta=\frac12\log Q-t\log4-\log(32\sqrt D).
\tag{B.1}
\]

If \(\delta>0\), then

\[
\boxed{
|P_3(A,A)|
\ge \frac{|A|^2}{1+e^{-\delta n}}.
}
\tag{B.2}
\]

For every successful complementary-prime quadratic witness with
\(T=Q/8\), the condition \(\Theta_R<1\) automatically implies
\(\delta>0\). More explicitly, it implies \(t\ge8\), and one may replace
\(\delta\) in (B.2) by

\[
\boxed{
\delta_*(t)
=\frac12\log\!\left(
\frac{41t!}{256(8/3)^t}
\right)>0.
}
\tag{B.3}
\]

Consequently, along the tower \(n=n_j\to\infty\),

\[
1\le
M_{n_j}:=\frac{|A_j|^2}{|P_3(A_j,A_j)|}
\le1+e^{-\delta_*n_j},
\]

and hence

\[
\boxed{
\lim_{j\to\infty}
\frac1{n_j}\log
\frac{|A_j|^2}{|P_3(A_j,A_j)|}=0.
}
\tag{B.4}
\]

This is the requested Outcome III. It closes the remaining transfer branch
of the successful quadratic split-prime architecture. It does **not**
disprove CPSI for other constructions.

## C. The witness and the exact second-digit condition

For the supplied tower, fix the auxiliary parameter first. Its totally real
layers \(K_j\) have

\[
n_j=[K_j:\mathbb Q]\longrightarrow\infty,
\qquad \operatorname{rd}(K_j)\le D,
\]

where \(D\) is fixed. The split primes may be selected with
\(q\equiv1\pmod {12}\) by applying Chebotarev to the fixed compositum that
also contains \(\mathbb Q(i,\zeta_3)\). Once the primes, \(Q\), and
\(T=Q/8\) are fixed, put

\[
\mathcal B_j=B_{K_j}(T),
\qquad
A_j=\sigma_j(\mathcal B_j)/Q.
\]

The frozen lattice estimates give

\[
\left(\frac{Q}{8\sqrt D}\right)^{n_j}
\le |A_j|
\le \left(\frac Q4+1\right)^{n_j}.
\tag{C.1}
\]

In particular, the elements of \(A_j\) are distinct and \(|A_j|\to\infty\)
once \(Q/(8\sqrt D)>1\).

For \(b,c\in\mathcal B_j\), write

\[
d=b-c,\qquad s=b+c,
\]

and clear denominators:

\[
S=d^2+5Qs=Q^2R(b/Q,c/Q),
\qquad
Z=d^3-3Q^2s=Q^3P_3(b/Q,c/Q).
\tag{C.2}
\]

The bridge becomes

\[
5Z=5d^3+3Qd^2-3QS.
\tag{C.3}
\]

Thus the sets \(\mathcal Z_S\) in CRO are precisely the values \(5Z\)
above the exact quadratic label \(S\). Multiplication by \(5\) does not
change cardinality.

If two ordered pairs give the same cubic output, and their differences and
sums are \((d,s)\) and \((e,s')\), then

\[
d^3-e^3=3Q^2(s-s').
\tag{C.4}
\]

The essential point is therefore

\[
\boxed{d^3\equiv e^3\pmod{Q^2\mathcal O_K},}
\tag{C.5}
\]

not merely congruence modulo \(Q\). The second \(q\)-adic digit is what
makes almost all formal cube-root alternatives miss the narrow Minkowski
window.

## D. Main lemma

The new mechanism is total-positivity packing.

Let

\[
\mathscr D=B_K(Q/4)
\]

and define the off-diagonal cube-congruence set

\[
\mathscr C_Q=
\{(d,e)\in\mathscr D^2:d\ne e,
\ d^3\equiv e^3\pmod{Q^2\mathcal O_K}\}.
\]

The central estimate is

\[
\boxed{
|\mathscr C_Q|\le(4^{t+1}\sqrt Q)^n.
}
\tag{D.1}
\]

This estimate includes both unit cube-root branches and singular coordinates
where both differences vanish modulo a split prime.

### D.1. Ideal-coset box packing

We first record an elementary lemma.

**Lemma D.1.** If \(\mathfrak a\subseteq\mathcal O_K\) is a nonzero
integral ideal of norm \(A_0\), then every coset \(z+\mathfrak a\) satisfies

\[
|(z+\mathfrak a)\cap B_K(L)|
\le
\left(1+\frac{2L}{A_0^{1/n}}\right)^n.
\tag{D.2}
\]

**Proof.** Partition each interval \([-L,L]\) into at most
\(1+2L/A_0^{1/n}\) half-open intervals of length strictly less than
\(A_0^{1/n}\). Two distinct points of the same product cell would differ
by a nonzero \(\alpha\in\mathfrak a\) with

\[
|N_{K/\mathbb Q}(\alpha)|<A_0.
\]

But \((\alpha)\subseteq\mathfrak a\), so
\(|N(\alpha)|\ge N(\mathfrak a)=A_0\), a contradiction. \(\square\)

### D.2. Four local types modulo \(\mathfrak p^2\)

Because every \(q\mid Q\) splits completely,

\[
Q^2\mathcal O_K=\prod_{\mathfrak p\mid Q}\mathfrak p^2,
\]

and there are \(tn\) prime ideals in this product. Each has
\(N\mathfrak p=q\), and
\(\mathcal O_K/\mathfrak p^2\cong\mathbb Z/q^2\mathbb Z\).

Fix a primitive cube root \(\zeta_{\mathfrak p}\) modulo
\(\mathfrak p^2\). Hensel's lemma applies because \(q\ne3\): the three
simple roots of \(X^3-1\) modulo \(\mathfrak p\) lift uniquely modulo
\(\mathfrak p^2\). Every local solution of
\(d^3\equiv e^3\pmod{\mathfrak p^2}\) has exactly one of four types:

\[
\begin{array}{c|l}
T & d\notin\mathfrak p,\ e\equiv d\pmod{\mathfrak p^2},\\
N_+ & d\notin\mathfrak p,\ e\equiv\zeta_{\mathfrak p}d
      \pmod{\mathfrak p^2},\\
N_- & d\notin\mathfrak p,\ e\equiv\zeta_{\mathfrak p}^{-1}d
      \pmod{\mathfrak p^2},\\
Z & d,e\in\mathfrak p.
\end{array}
\tag{D.3}
\]

Indeed, if \(d\) is a unit, then \(e/d\) is one of the three cube roots
of unity. If \(d\in\mathfrak p\), the congruence forces
\(e\in\mathfrak p\), and then both cubes vanish modulo
\(\mathfrak p^2\).

A global type \(\tau\) chooses one of these four alternatives at all
\(tn\) split prime ideals. Let \(W_T,W_N,W_Z\) be the sums of
\(\log N\mathfrak p\) over the corresponding positions, combining
\(N_+\) and \(N_-\) in \(W_N\). Then

\[
W_T+W_N+W_Z=n\log Q.
\tag{D.4}
\]

Put

\[
u=d-e,\qquad v=d+e,
\]

and define

\[
\mathfrak J_\tau=
\prod_T\mathfrak p^2\prod_Z\mathfrak p,
\qquad
\mathfrak I_\tau=
\prod_{N_+\cup N_-}\mathfrak p^2\prod_Z\mathfrak p.
\tag{D.5}
\]

Then \(u\in\mathfrak J_\tau\). Once \(u\) is fixed, \(v\) lies in one
coset modulo \(\mathfrak I_\tau\). At a nontrivial root position,

\[
v\equiv
\frac{1+\zeta_{\mathfrak p}}
     {1-\zeta_{\mathfrak p}}u
\pmod{\mathfrak p^2},
\tag{D.6}
\]

where \(1-\zeta_{\mathfrak p}\) is a unit; at a \(Z\)-position,
\(u,v\in\mathfrak p\). No global cube root of unity in \(K\) is being
assumed: (D.6) is a separate local congruence at each \(\mathfrak p\).

Write

\[
a=\frac{2W_T+W_Z}{n},
\qquad
b=\frac{2W_N+W_Z}{n}.
\tag{D.7}
\]

Then

\[
N\mathfrak J_\tau=e^{an},
\qquad
N\mathfrak I_\tau=e^{bn},
\qquad
a+b=2\log Q.
\tag{D.8}
\]

Since \(d,e\in B_K(Q/4)\), both \(u\) and \(v\) belong to
\(B_K(Q/2)\). Lemma D.1, first for \(u\) and then for the single
\(v\)-coset, gives for the off-diagonal points of type \(\tau\)

\[
M_\tau
\le
[(1+Qe^{-a})(1+Qe^{-b})]^n.
\tag{D.9}
\]

### D.3. The two packing regimes

Assume first that

\[
a\ge\frac12\log Q.
\]

If the type contains an off-diagonal point, then
\(0\ne u\in\mathfrak J_\tau\), so

\[
e^{an}=N\mathfrak J_\tau
\le|N_{K/\mathbb Q}(u)|
\le(Q/2)^n.
\tag{D.10}
\]

For \(x=Qe^{-a}\), this gives \(2\le x\le\sqrt Q\), while
\(Qe^{-b}=x^{-1}\). Hence

\[
M_\tau
\le(2+x+x^{-1})^n
\le(4\sqrt Q)^n.
\tag{D.11}
\]

Now assume

\[
a<\frac12\log Q.
\]

Let

\[
h=\frac{W_N+W_Z}{n}.
\]

Because \(a\ge2W_T/n\), (D.4) gives

\[
h=\log Q-W_T/n>\frac34\log Q.
\tag{D.12}
\]

Take two distinct off-diagonal points of the same global type, and denote
their difference by \((\Delta d,\Delta e)\). At an \(N_+\) or \(N_-\)
position the same lifted root is used by both points, so
\(\Delta e\equiv\zeta^{\pm1}\Delta d\pmod{\mathfrak p^2}\). At a
\(Z\)-position both differences lie in \(\mathfrak p\). Therefore

\[
H(\Delta d,\Delta e)
:=(\Delta d)^2+\Delta d\,\Delta e+(\Delta e)^2
\in
\prod_{N_+\cup N_-\cup Z}\mathfrak p^2.
\tag{D.13}
\]

The norm of the ideal on the right is \(e^{2nh}\). The binary form

\[
H(X,Y)=X^2+XY+Y^2
\]

is positive definite at every real embedding. For a nonzero pair,
\(H(\Delta d,\Delta e)\ne0\), and ideal divisibility followed by
arithmetic-geometric mean gives

\[
\sum_\sigma
H(\sigma\Delta d,\sigma\Delta e)
\ge ne^{2h}.
\tag{D.14}
\]

Since

\[
H(x,y)\le\frac32(x^2+y^2),
\]

distinct points of this type are separated in \(\mathbb R^{2n}\) by at
least

\[
r=\sqrt{\frac{2n}{3}}e^h.
\tag{D.15}
\]

All type points lie in a Euclidean ball of radius

\[
R=Q\sqrt{n/8}.
\]

The disjoint-ball packing bound in dimension \(2n\) yields

\[
M_\tau
\le(1+2R/r)^{2n}
\le
\left(1+\frac{\sqrt3}{2}Q^{1/4}\right)^{2n}
\le(4\sqrt Q)^n.
\tag{D.16}
\]

There are at most \(4^{tn}\) global types. Summing (D.11) and (D.16)
proves (D.1).

## E. Complete collision-energy proof

Define

\[
Z(b,c)=(b-c)^3-3Q^2(b+c)
\]

on \(\mathcal B^2\), and let

\[
E_Z=
\#\{(b,c,b',c')\in\mathcal B^4:
Z(b,c)=Z(b',c')\}.
\]

For a collision put \(d=b-c\) and \(e=b'-c'\). Equation (C.4) puts
every off-diagonal \((d,e)\) in \(\mathscr C_Q\).

If \(d=e\), equality of outputs forces \(b+c=b'+c'\), so the two ordered
input pairs coincide. These contribute exactly \(N^2\) to \(E_Z\).

Fix \((d,e)\in\mathscr C_Q\). There are at most \(N\) possible first
pairs \((b,c)\) with difference \(d\), because choosing \(b\in\mathcal B\)
determines \(c=b-d\). Once the first pair is fixed, equality determines

\[
s'=s+\frac{e^3-d^3}{3Q^2}
\]

and then uniquely determines

\[
b'=\frac{s'+e}{2},
\qquad
c'=\frac{s'-e}{2}.
\]

These elements may fail to be integral or to lie in \(\mathcal B\), but
that only decreases the count. Therefore

\[
E_Z\le N^2+N|\mathscr C_Q|.
\tag{E.1}
\]

The frozen Blichfeldt estimate gives

\[
N\ge\left(\frac{Q}{8\sqrt D}\right)^n.
\tag{E.2}
\]

Combining (D.1), (E.1), and (E.2), and putting

\[
\lambda=
\frac{32\sqrt D\,4^t}{\sqrt Q}=e^{-\delta},
\tag{E.3}
\]

gives

\[
E_Z\le N^2(1+\lambda^n).
\tag{E.4}
\]

If \(m(z)\) is the number of ordered input pairs producing \(z\), then

\[
\sum_zm(z)=N^2,
\qquad
\sum_zm(z)^2=E_Z.
\]

Cauchy-Schwarz gives

\[
N^4
\le |Z(\mathcal B,\mathcal B)|E_Z,
\]

so (E.4) proves (B.2). Because \(\sigma_0\) is an injective field
embedding and

\[
P_3(\sigma_0(b)/Q,\sigma_0(c)/Q)
=\sigma_0(Z(b,c))/Q^3,
\]

the algebraic and real image cardinalities agree.

There is also a stronger incidence interpretation. From

\[
\sum_zm(z)(m(z)-1)\le\lambda^nN^2
\]

it follows that all but at most \(\lambda^nN^2\) ordered input pairs lie
in singleton cubic fibers. Thus the theorem is not merely a lower bound
obtained from a large diagonal term: global cross-fiber collisions occupy
an exponentially vanishing fraction of the Cartesian square.

## F. Why quadratic success forces \(\delta>0\)

For the complementary-prime quadratic witness, put

\[
\rho=\prod_{q\mid Q}\frac{q+1}{2q}.
\]

The frozen quadratic estimate at \(T=Q/8\) is

\[
|R(A,A)|\le\Theta_R^n|A|^2,
\qquad
\Theta_R=D\rho\left(164+\frac{64}{Q}\right).
\tag{F.1}
\]

Suppose \(\Theta_R<1\). Since \(\rho>2^{-t}\) and \(D\ge1\),

\[
1>\Theta_R>164D,2^{-t}.
\]

Consequently

\[
t\ge8,
\qquad
D<\frac{2^t}{164}.
\tag{F.2}
\]

Order the selected primes increasingly. The \(i\)-th distinct prime
congruent to \(1\pmod {12}\) is larger than \(12i\), whether or not every
number in that progression is prime. Hence

\[
Q>12^t t!.
\tag{F.3}
\]

Using (F.2) and (F.3) in (E.3),

\[
\lambda^2
=\frac{1024D\,16^t}{Q}
<
\frac{256}{41}\frac{(8/3)^t}{t!}.
\tag{F.4}
\]

At \(t=8\), the right side is less than \(0.397\). Its ratio at
\(t+1\) to its value at \(t\) is

\[
\frac{8/3}{t+1}<1,
\]

so it decreases for every \(t\ge8\). Thus \(\lambda<1\), and (B.3)
follows. Numerically, \(\delta_*(8)>0.463\).

This argument is stronger than merely choosing a favorable large-prime
subfamily: every \(q\equiv1\pmod {12}\), \(T=Q/8\) witness that achieves
the frozen quadratic inequality \(\Theta_R<1\) automatically lies in the
near-injective cubic regime.

## G. Gain-loss ledger and CRO

| Quantity | Bound or rate | Role |
|---|---:|---|
| Field degree | \(n=n_j\to\infty\) | Only growing parameter after the witness is fixed |
| Root discriminant | \(\operatorname{rd}(K_j)\le D\) | Fixed lattice cost |
| Input size | \((Q/(8\sqrt D))^n\le |A_j|\le(Q/4+1)^n\) | Exponential growth, distinct real inputs |
| Quadratic image | \(|R(A_j,A_j)|\le\Theta_R^n|A_j|^2\), \(\Theta_R<1\) | Frozen benchmark success |
| Local \(Q^2\) types | At most \(4^{tn}\) | \(T,N_+,N_-,Z\) at every split coordinate |
| One type | At most \((4\sqrt Q)^n\) difference pairs | Ideal packing or total positivity |
| All off-diagonal difference pairs | At most \((4^{t+1}\sqrt Q)^n\) | Main new lemma |
| Anchors over fixed \((d,e)\) | At most \(|A_j|\) | Equality determines the second pair |
| Off-diagonal energy ratio | At most \(\lambda^n=e^{-\delta n}\) | Exponentially negligible cross-fiber overlap |
| Cubic image | At least \(|A_j|^2/(1+e^{-\delta n})\) | Asymptotic injectivity |
| GAIN rate | \(n^{-1}\log M_n\to0\) | Rules out CRO and a power saving on this witness |

For the exact quadratic fibers in the question,

\[
\sum_S|\mathcal Z_S|=|A_j|^2,
\qquad
\left|\bigcup_S\mathcal Z_S\right|=|P_3(A_j,A_j)|.
\]

Therefore

\[
\boxed{
\frac{1}{1+e^{-\delta n_j}}
\le
\frac{|\bigcup_S\mathcal Z_S|}
     {\sum_S|\mathcal Z_S|}
\le1.
}
\tag{G.1}
\]

CRO requires the middle ratio to be at most \(e^{-\eta n_j}\) for some
\(\eta>0\). Equation (G.1) shows that it instead tends to \(1\).

The surviving \(\mu_3\)-ambiguity is therefore formal local entropy, not
realized global multiplicity. Exact equality demands a lift modulo
\(Q^2\); the product of the narrow archimedean window with ideal-norm and
total-positivity separation leaves exponentially few nontrivial lifted
partners.

Since \(|A_j|\to\infty\), (B.2) also shows that for every fixed \(c>0\),

\[
|P_3(A_j,A_j)|>|A_j|^{2-c}
\]

for all sufficiently large \(j\). Thus these quadratic witness sets cannot
prove CPSI.

## H. Consequence and exactly one next unresolved statement

Both congruence choices available in the fixed \(T=Q/8\) quadratic
split-prime transfer are now closed:

- the \(q\equiv5\pmod {12}\) witness is exactly injective for \(P_3\);
- the \(q\equiv1\pmod {12}\) witness is asymptotically injective by (B.2).

The conclusion is about this transfer architecture, not about the polynomial
itself. The one next problem is therefore the direct form of CPSI:

\[
\boxed{
\text{Construct explicit }A_j\subset\mathbb R,\ |A_j|\to\infty,
\text{ such that }
\liminf_{j\to\infty}
\frac{\log(|A_j|^2/|P_3(A_j,A_j)|)}{\log|A_j|}>0.
}
\]

Such a construction must introduce a source of cubic collisions not inherited
from the quadratic square-residue witness.

## I. Standard results used

For completeness, the proof invokes the following standard statements in
these precise forms.

1. **Chebotarev density theorem.** For a finite Galois extension
   \(L/\mathbb Q\) and a conjugacy class \(C\subseteq\operatorname{Gal}(L/\mathbb Q)\),
   the unramified rational primes with Frobenius class \(C\) have natural
   density \(|C|/|\operatorname{Gal}(L/\mathbb Q)|\). Here it supplies
   arbitrarily many primes split in the fixed tower quotient and in
   \(\mathbb Q(i,\zeta_3)\).
2. **Blichfeldt's lattice principle.** If a measurable set in
   \(\mathbb R^n\) has volume \(V\) and a full lattice has covolume
   \(\Delta\), some translate contains at least \(V/\Delta\) lattice
   points. Applied to a cube and followed by subtraction, it gives (E.2).
3. **Hensel's simple-root lemma.** A root \(a\) of \(f\) modulo a prime
   ideal with \(f'(a)\) invertible lifts uniquely modulo every higher power;
   only the lift from \(\mathfrak p\) to \(\mathfrak p^2\) is used here.
4. **Ideal norm divisibility.** If \(0\ne\alpha\in\mathfrak a\) for an
   integral ideal \(\mathfrak a\), then \((\alpha)\subseteq\mathfrak a\)
   and \(|N_{K/\mathbb Q}(\alpha)|\ge N\mathfrak a\).
5. **Arithmetic-geometric mean.** For positive real numbers
   \(x_1,\ldots,x_n\), \(n^{-1}\sum x_i\ge(\prod x_i)^{1/n}\).
6. **Euclidean packing bound.** If points in a ball of radius \(R\) in
   \(\mathbb R^m\) are mutually at distance at least \(r\), disjoint balls
   of radius \(r/2\) give at most \((1+2R/r)^m\) points.
7. **Cauchy-Schwarz for fibers.** If a finite map has domain size \(M\),
   image size \(L\), and collision energy \(E\), then \(M^2\le LE\).
