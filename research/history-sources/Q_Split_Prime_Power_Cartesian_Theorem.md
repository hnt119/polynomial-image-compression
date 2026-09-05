# The split-prime-power Cartesian inequality for \(Q(x,y)=x^2+xy+y^2\)

## A. Frozen checkpoint

The five frozen results in the problem statement are used as hypotheses and are not
reproved here. In particular, the full-input norm sieve, varying-prime CRT packing,
inert and ramified Cartesian bounds, previously settled split cases, and the global
ideal-factorization obstruction remain closed.

The new result is the missing split-prime-power theorem.

## B. Main theorem

Let \(\mathcal O\) be a discrete valuation ring with uniformizer \(\pi\) and residue
field \(F=\mathcal O/(\pi)\) of odd cardinality \(R\). Assume
\(\operatorname{char}F\ne3\) and that \(X^2+X+1\) has two distinct roots in \(F\).
Put \(\mathcal R_k=\mathcal O/(\pi^k)\). Then, for every \(k\ge1\) and every
\(B\subseteq\mathcal R_k\),

\[
\boxed{R^k\,|Q(B,B)|\ge |B|^2.}
\]

Equivalently, every split local Cartesian factor satisfies

\[
\Lambda_k(B,B)=\frac{R^k|Q(B,B)|}{|B|^2}\ge1.
\]

No substantial external theorem is needed. We use only the elementary structure of
quotients of a DVR (every reduction fiber
\(\mathcal R_j\to\mathcal R_{j-1}\) has size \(R\), and an element is a unit exactly
when its residue is nonzero) and the following standard finite-level form of Hensel
lifting: a simple root of a polynomial modulo \(\pi\) lifts uniquely and compatibly
to a root modulo \(\pi^j\) for every \(j\ge1\).

## C. Split-coordinate correlation

Choose the two roots \(r,s\in F\). They are simple because the residue
characteristic is not \(3\); by the stated finite-level Hensel lemma they lift to
compatible roots in every \(\mathcal R_k\). Then

\[
Q(x,y)=(x-r y)(x-s y).
\]

Writing \(u=x-r y\), \(v=x-s y\), one has

\[
y=\frac{u-v}{s-r},\qquad x=\frac{s u-r v}{s-r}.
\]

Thus the transformed grid is exactly

\[
T(B^2)=\left\{(u,v):
\frac{s u-rv}{s-r}\in B,\ 
\frac{u-v}{s-r}\in B
\right\}.
\]

It is the intersection of two transverse linear pullbacks of \(B\), not a product
\(U\times V\). In particular,

\[
r_B(t)=\sum_{uv=t}
1_B\!\left(\frac{s u-rv}{s-r}\right)
1_B\!\left(\frac{u-v}{s-r}\right).
\]

The proof below works with this correlation through residue branches rather than
discarding it.

## D. Proof

The empty-set case is immediate, so all sets below are nonempty.

### D.1 A rectangular residue-field lemma

**Lemma 1.** If \(\varnothing\ne A,C\subseteq F\), then

\[
\boxed{R\,|Q(A,C)|\ge |A|\,|C|.}
\tag{1}
\]

**Proof.** By symmetry assume \(a=|A|\le c=|C|\), and put
\(m=|Q(A,C)|\). The split linear change
identifies a nonzero fiber of \(Q\) with \(uv=t\), so every nonzero full fiber has
exactly \(R-1\) points. For a fixed first coordinate, \(Q(x,y)=0\) has at most two
solutions in \(y\). Hence the zero fiber meets \(A\times C\) in at most \(2a\)
points.

If zero is absent from the image, then \(ac\le (R-1)m\), which is stronger than
(1). If zero is present, then

\[
ac\le 2a+(R-1)(m-1).
\tag{2}
\]

The lower bound from (2) implies \(m\ge ac/R\) whenever

\[
a(2R-c)\le R(R-1).
\tag{3}
\]

Suppose (3) fails. Since \(a\le c\), this first forces
\((R-c)^2<R\), hence \(c>R-\sqrt R\), and then

\[
a+c>\frac{R(R-1)}{2R-c}+c\ge 2R-2\sqrt R.
\tag{4}
\]

For \(R\ge19\), the right side of (4) exceeds \((3R+1)/2\). If a nonzero
\(t\) were missing from \(Q(A,C)\), every point on its \((R-1)\)-point conic would
have first coordinate outside \(A\) or second coordinate outside \(C\). Each fixed
missing coordinate covers at most two conic points, so the conic would have fewer
than

\[
2(R-a)+2(R-c)<R-1
\]

points, a contradiction. Zero is already represented, so the whole field is the
image.

The only odd split residue sizes below \(19\) are \(R=7,13\). The integer pairs
not handled by (3) or the preceding complement argument are respectively
\((a,c)=(5,5)\) and \((10,10)\). Formula (2), with integrality of \(m\), gives
\(m\ge4\) and \(m\ge8\), while \(25/7<4\) and \(100/13<8\). This proves (1).
\(\square\)

### D.2 The weighted residue lemma

For \(w:F\to[0,1]\), write

\[
S=\operatorname{supp}w,\quad s=|S|,\quad W=\sum_{x\in F}w_x,
\quad a=w_0.
\]

For \(t\in F\), define the noncentral branch height

\[
L_t=\max_{\substack{x,y\in S,\ Q(x,y)=t\\(x,y)\ne(0,0)}}
\max(w_x,w_y),
\]

with an empty maximum equal to zero, and put

\[
H=\sum_{t\ne0}L_t+\max\left(L_0,\frac{a^2}{R}\right).
\]

**Lemma 2.** One has

\[
\boxed{H\ge\frac{W^2}{R}.}
\tag{5}
\]

**Proof.** First include the central pair and set

\[
K_t=\max_{\substack{x,y\in S\\Q(x,y)=t}}\max(w_x,w_y).
\]

For \(A_u=\{x:w_x\ge u\}\), symmetry of \(Q\) gives the exact layer-cake identity

\[
\sum_tK_t=\int_0^1|Q(A_u,S)|\,du.
\tag{6}
\]

Lemma 1 therefore yields

\[
\sum_tK_t\ge\frac{sW}{R}.
\tag{7}
\]

Let \(z=L_0\). If \(a\le z\), then the left side of (5) is the left side of
(6), and (5) follows from \(s\ge W\). Assume \(a>z\). Replacing the ordinary
central height \(a\) by \(\max(z,a^2/R)\) loses

\[
\Delta=a-\max\left(z,\frac{a^2}{R}\right).
\tag{8}
\]

For \(z<u\le a\), zero is represented in \(A_u\times S\) only by \((0,0)\).
If \(h_u=|A_u|\), exact fiber counting now gives

\[
|Q(A_u,S)|\ge1+\frac{s h_u-1}{R-1}
=\frac{s h_u}{R}+\frac{R^2-2R+s h_u}{R(R-1)}.
\tag{9}
\]

Using \(h_u\ge1\), integrating (9) on that interval, using Lemma 1 elsewhere,
and subtracting (8), it is enough to prove \(J\ge0\), where

\[
J=W(s-W)+(a-z)\frac{R^2-2R+s}{R-1}-R\Delta.
\tag{10}
\]

This last inequality is elementary, but the audit is included because it is where the
singular branch is paid for. Put \(d=R-s\). Then

\[
\frac{R^2-2R+s}{R-1}=R-\frac d{R-1}.
\]

If \(z=0\), then \(a\le W\le a+s-1\) and

\[
J=W(s-W)+a^2-\frac{da}{R-1}.
\]

This is concave in \(W\). At the two endpoints it equals

\[
J(a)=\frac{aR(s-1)}{R-1},
\qquad
J(a+s-1)=(s-1)\left(1-\frac{a(R-2)}{R-1}\right),
\]

both nonnegative.

Now let \(z>0\). A noncentral isotropic pair supplies two distinct supported
nonzero residues, both of weight at most \(z\). Therefore

\[
s-W=\sum_{x\in S}(1-w_x)\ge (1-a)+2(1-z),
\qquad W\ge a.
\tag{11}
\]

If \(z\ge a^2/R\), formula (10) becomes

\[
J=W(s-W)-\frac{d(a-z)}{R-1}.
\]

If \(z\le a^2/R\), it becomes

\[
J=W(s-W)+a^2-Rz-\frac{d(a-z)}{R-1}
\ge W(s-W)-\frac{d(a-z)}{R-1}.
\]

Finally, (11) gives

\[
W(s-W)\ge a(3-a-2z)\ge a-z.
\]

After subtraction, the last inequality is linear in \(z\); at \(z=0\) it is
\(2a-a^2\ge0\), and at \(z=a\) it is \(3a(1-a)\ge0\). Since
\(0\le d/(R-1)\le1\), this proves \(J\ge0\).

This proves (5). \(\square\)

### D.3 Branch lifting and induction

Assume the theorem through depth \(k-2\), with the depth-zero statement interpreted
on the one-element ring. Put \(M=R^{k-1}\) and decompose

\[
B=\bigcup_{a\in F}(\widetilde a+\pi B_a),
\qquad n_a=|B_a|,
\qquad w_a=\frac{n_a}{M}.
\]

Thus \(|B|=MW\) and \(0\le w_a\le1\).

For a residue pair \((a,b)\ne(0,0)\), expansion modulo \(\pi^k\) gives a lift map
whose two partial derivatives modulo \(\pi\) are

\[
2a+b,\qquad a+2b.
\tag{12}
\]

They cannot both vanish because their determinant is \(3\). If both are units,
fixing either coordinate shows that the cell image has at least
\(\max(n_a,n_b)\) elements: the difference of two outputs factors as the input
difference times a unit.

If exactly one derivative vanishes, say \(b=-2a\ne0\), that cell gives at least
\(n_b\) outputs. But

\[
Q(a,-2a)=3a^2=Q(a,a),
\]

and the diagonal cell \((a,a)\), in the same output residue class, has both
derivatives equal to \(3a\); it gives at least \(n_a\) outputs. Pooling the two
cells therefore gives at least \(\max(n_a,n_b)\) outputs. The case
\(a=-2b\) is symmetric. Notice that only a maximum, never a sum, is taken, so
overlap creates no loss or double count.

It follows that the output values reducing to \(t\) have cardinality at least
\(M L_t\) for every noncentral residue representation.

For the central cell, let \(C\subseteq\mathcal R_{k-2}\) be the reduction of
\(B_0\subseteq\mathcal R_{k-1}\). A reduction fiber has size \(R\), so
\(|C|\ge n_0/R\). Homogeneity and induction give

\[
|Q(\pi B_0,\pi B_0)|
=|Q(C,C)|
\ge\frac{|C|^2}{R^{k-2}}
\ge\frac{n_0^2}{R^k}
=M\frac{w_0^2}{R},
\tag{13}
\]

where the first equality identifies \(Q(C,C)\) with its injective image after
multiplication by \(\pi^2\). The central and noncentral zero outputs may overlap,
so their valid combined lower bound is their maximum.

Lemma 2 now gives

\[
|Q(B,B)|\ge MH\ge M\frac{W^2}{R}
=\frac{|B|^2}{R^k}.
\]

Lemma 1 with \(A=S=B\) is the base case \(k=1\). Strong induction completes the
proof.

## E. Extremizers and tested structured families

The theorem does not require a complete equality classification. It does give the
following exact examples.

For the central ideal \(B=\pi^h\mathcal R_k\),

\[
Q(B,B)=
\begin{cases}
\pi^{2h}\mathcal R_k,&2h<k,\\
\{0\},&2h\ge k,
\end{cases}
\]

so \(\Lambda_k(B,B)=1\) exactly when \(2h\le k\), and it equals
\(R^{2h-k}>1\) when \(2h>k\).

If \(B=c+\pi^h\mathcal R_k\) is a noncentral ball and
\(\ell=v_\pi(c)<h\), direct expansion gives

\[
Q(B,B)=
\begin{cases}
3c^2+\pi^{\ell+h}\mathcal R_k,&\ell+h<k,\\
\{3c^2\},&\ell+h\ge k,
\end{cases}
\]

and hence \(\Lambda=R^{h-\ell}>1\) in the first case and
\(\Lambda=R^{2h-k}>1\) in the second. Thus among individual residue balls, the
only equality examples are the appropriate central ideals.

Likewise, a complete valuation shell \(\pi^h\mathcal R_k^\times\) has
\(\Lambda=R^2/(R-1)^2>1\) when \(2h<k\). For completeness, the primitive-shell
surjectivity follows directly in split coordinates. Given a nonunit target \(t\), take
\(u=1,v=t\); the inverse linear formulas give unit \(x,y\). Given a unit target,
take \(u\in\mathcal R_k^\times\), \(v=t/u\), with the residue of \(u\) avoiding
\(u^2=t\) and \(u^2=(r/s)t\). There are at most four forbidden residues and
\(R-1\ge6\). Thus \(Q(\mathcal R_k^\times,\mathcal R_k^\times)=\mathcal R_k\);
scaling proves the displayed shell formula.

These calculations explain why balls, shells, and their elementary mixtures did not
reveal a counterexample. A complete classification of all equality sets is not needed
here and remains open.

## F. Consequence for local restrictions

Every good split place and every prime-power depth now contributes normalized factor
at least one. Thus split places contribute no compression whatsoever to a standard
CRT construction using independent local Cartesian restrictions.

Combining this with the frozen results closes that entire standard branch:

* split factors are at least \(1\) by the theorem above;
* inert factors cannot beat the frozen \(R/(R+1)\) parity factor, and fixed or
  varying inert-prime CRT certificates are already globally obstructed;
* ramified/singular factors cannot acquire a depth-dependent gain, by the frozen
  \(R/[2(R+1)]\) bound and the already audited discriminant/order-index ledger.

This conclusion is deliberately limited to product-type local Cartesian restrictions
combined by the standard CRT/lattice-packing certificate. It does not rule out a
global set whose residue conditions are correlated across different primes, nor a
direct ideal-factorization construction that does not pass through local allowed-output
densities.

## G. Next unresolved global statement

The smallest next extension is tensorization under correlated CRT restrictions:

> If
> \[
> \mathscr R=\prod_{\nu}\mathcal R_{\nu,k_\nu}
> \]
> is a finite product of good split local rings and
> \(B\subseteq\mathscr R\) is arbitrary, must
> \[
> \boxed{|\mathscr R|\,|Q(B,B)|\ge|B|^2?}
> \]

The theorem proves this when \(B=\prod_\nu B_\nu\), because the local inequalities
multiply. It does not prove it for a set whose coordinates at different primes are
correlated. The one-place induction cannot simply be iterated: its fibers would be
different subsets in the remaining factors, and the critical-cell diagonal pooling
used above need not survive. A counterexample would therefore be a genuinely new
cross-prime mechanism; a proof would close split congruence restrictions without any
independence hypothesis.

Beyond this tensor problem, the frozen global fiber bound gives the next
ideal-factorization obstruction. For \(K=L(\omega)\), a power-saving image would
force a positive proportion of pairs to have exponentially large split-divisor product

\[
\prod_{\substack{\mathfrak p\mid Q(a,b)\\
\mathfrak p\text{ split in }K/L}}
\bigl(v_{\mathfrak p}(Q(a,b))+1\bigr).
\]

A precise broader global theorem would be either:

1. construct bounded-root-discriminant fields \(L_j\) and exponentially sized
   Cartesian sets \(A_j\) with such split-divisor richness on a positive proportion
   of \(A_j^2\), and then directly bound the number of resulting norm values; or
2. prove an upper-tail theorem showing that, for every admissible exponential-size
   family \(A_j\), the proportion of pairs for which the displayed product is at
   least \(|A_j|^\eta\) tends to zero for every fixed \(\eta>0\).

Either statement changes a structural hypothesis of the now-closed local CRT branch:
it concerns global cross-prime correlation rather than a product of independent local
Cartesian restrictions.
