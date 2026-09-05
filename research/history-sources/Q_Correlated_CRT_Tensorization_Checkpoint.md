# Correlated split-CRT restrictions for \(Q(x,y)=x^2+xy+y^2\)

## A. Frozen checkpoint

All four frozen conclusions in the problem statement are used as hypotheses. In
particular, no one-place split, inert, or ramified estimate is reopened, and no
fixed- or varying-prime inert CRT construction is retried.

The new conclusions are these.

1. The scalar one-place inequality does **not** tensorize in abstract finite
   systems, even if the map is symmetric and satisfies the stronger rectangular
   inequality for every pair of input subsets. The failure can accumulate
   exponentially.
2. For the actual quadratic form, CRT-Q is proved for every product of split
   residue fields in which at most one factor has \(3\) square. This includes every
   two-field product having a factor of size \(q\equiv7\pmod {12}\).
3. Arbitrary cross-coordinate correlations based only on the bits
   \(x_i\in\pi_i^{h_i}\mathcal R_i\) cannot compress the image. This holds at
   arbitrary prime-power depths and for an arbitrary family of allowed bit
   patterns.
4. CRT-Q for completely arbitrary correlated subsets of arbitrary split
   prime-power products remains open. A precise weighted local inequality is
   isolated which would imply it with constant \(1\).

No external source is used. The only nontrivial local input imported from the
supplied one-place report is its depth-one rectangular lemma:

> If \(F\) is a good split residue field and \(A,C\subseteq F\), then
> \[
> |F|\,|Q(A,C)|\ge |A|\,|C|.
> \tag{RL}
> \]

The only standard theorem assumed is the following finite-level Hensel lemma:
over a DVR of odd residue characteristic, every simple root
modulo \(\pi\) lifts uniquely to every quotient \(\mathcal O/\pi^k\). In
particular, a unit of \(\mathcal O/\pi^k\) is a square exactly when its residue is
a square.

## B. Abstract tensorization verdict: false

Let \(X=\{0,1,2,3\}\), and define the symmetric map
\(f:X^2\to\{\alpha,\beta,\gamma,\delta\}\) by

\[
\begin{array}{c|cccc}
f&0&1&2&3\\ \hline
0&\alpha&\beta&\beta&\alpha\\
1&\beta&\gamma&\delta&\alpha\\
2&\beta&\delta&\gamma&\alpha\\
3&\alpha&\alpha&\alpha&\alpha.
\end{array}
\tag{1}
\]

It satisfies the stronger local assertion

\[
4|f(A,C)|\ge |A||C| \qquad(A,C\subseteq X).
\tag{2}
\]

Here is a complete finite verification. Every monochromatic rectangle in (1) has
area at most \(4\). This proves (2) whenever \(|A||C|\le8\). For a
\(3\times3\) rectangle, the image sizes, indexed by the omitted row and column,
are

\[
\begin{pmatrix}
3&4&4&4\\
4&3&3&4\\
4&3&3&4\\
4&4&4&4
\end{pmatrix},
\]

so (2) holds there. Every \(3\times4\) or \(4\times3\) rectangle contains one
of these \(3\times3\) rectangles and hence has at least three colors; the full
table has four colors. This exhausts all sizes.

Put \(L=\{0,3\}\) and

\[
B=(L\times X)\cup(X\times L)=X^2\setminus(\{1,2\}^2).
\]

Then \(|B|=12\), while a direct calculation gives

\[
(f\otimes f)(B,B)=
(\{\alpha\}\times\{\alpha,\beta,\gamma,\delta\})
\cup
(\{\alpha,\beta,\gamma,\delta\}\times\{\alpha\})
\cup\{(\beta,\beta)\}.
\tag{3}
\]

The set in (3) has size \(8\). To audit the upper inclusion, an output
\(\gamma\) or \(\delta\) forces both corresponding input coordinates into
\(\{1,2\}\); membership of both input vectors in \(B\) then forces their other
coordinates into \(L\), where the output is \(\alpha\). Thus the only output
with neither coordinate \(\alpha\) is \((\beta,\beta)\). Conversely, all eight
displayed outputs have witnesses; for \((\beta,\beta)\), use the two input
vectors \((0,1)\) and \((1,0)\).

Consequently

\[
\frac{|X|^2|(f\otimes f)(B,B)|}{|B|^2}
=\frac{16\cdot8}{12^2}=\frac89<1.
\tag{4}
\]

Taking products of this bad two-coordinate block, and appending one full factor
when necessary, gives abstract examples with

\[
C_t\le \left(\frac89\right)^{\lfloor t/2\rfloor}.
\tag{5}
\]

Thus local constant \(1\), symmetry, and even every local rectangular inequality
do not prevent exponential cross-coordinate loss.

## C. Two-factor and many-factor split-field verdict

For a finite product \(\mathscr F=\prod_{i=1}^tF_i\) of good split fields, put

\[
C(\mathscr F)=inf_{\varnothing\ne B\subseteq\mathscr F}
\frac{|\mathscr F|\,|Q(B,B)|}{|B|^2}.
\]

### Theorem 1: an exact depth-one class

Suppose at most one \(F_i\) has \(3\) square. Then

\[
\boxed{C(\mathscr F)=1.}
\tag{6}
\]

More strongly, if \(3\) is nonsquare in every factor, then every
\(B\subseteq\mathscr F\) satisfies

\[
\boxed{|Q(B,B)|\ge |B|.}
\tag{7}
\]

For a good split field of odd size \(q\), the discriminant \(-3\) is square.
Hence the quadratic characters of \(3\) and \(-1\) agree. Since splitting also
forces \(q\equiv1\pmod3\), the nonsquare case is exactly
\(q\equiv7\pmod {12}\), and the square case is \(q\equiv1\pmod {12}\).

In particular, for two split fields CRT-Q is proved whenever at least one residue
size is \(7\pmod {12}\). The first unresolved depth-one two-factor regime has
both residue sizes \(1\pmod {12}\).

### Proof

First suppose \(3\) is nonsquare in every factor. Partition \(\mathscr F\) by
the coordinatewise square vector

\[
O_z=\{x\in\mathscr F:x_i^2=z_i\text{ for all }i\}.
\]

On the nonzero coordinates of \(z\), each \(O_z\) is a sign cube. If
\(x,y\in O_z\), then

\[
Q(x_i,y_i)=
\begin{cases}
3z_i,&x_i=y_i,\\
z_i,&x_i=-y_i.
\end{cases}
\tag{8}
\]

Because \(3\) is nonsquare, an output coordinate in (8) determines whether the
signs agree and then determines \(z_i\). Thus the output blocks
\(Q(O_z,O_z)\) belonging to different \(z\) are disjoint.

For arbitrary weights \(w_x\ge0\), define

\[
M_t=\max_{Q(x,y)=t}w_xw_y.
\]

Choose \(x_z\in O_z\) of maximum weight. As \(y\) ranges through \(O_z\), the
values \(Q(x_z,y)\) are distinct by (8), and therefore

\[
\sum_{t\in Q(O_z,O_z)}M_t
\ge w_{x_z}\sum_{y\in O_z}w_y
\ge\sum_{y\in O_z}w_y^2.
\]

Summing disjoint output blocks gives the structural weighted inequality

\[
\boxed{\sum_tM_t\ge\sum_xw_x^2.}
\tag{9}
\]

For \(w=1_B\), the left side is \(|Q(B,B)|\), proving (7). Cauchy--Schwarz
also gives

\[
|\mathscr F|\sum_tM_t\ge\left(\sum_xw_x\right)^2.
\tag{10}
\]

Now write \(\mathscr F=G\times H\), where all factors in \(G\) have \(3\)
nonsquare and \(H\) is the possible single exceptional field. For
\(B\subseteq G\times H\), let \(B_g\subseteq H\) be its fibers and put
\(w_g=|B_g|\). For each \(G\)-output \(t\), choose a pair \((g,g')\) attaining
\(M_t=\max_{Q(g,g')=t}w_gw_{g'}\). The imported rectangular lemma (RL) gives

\[
|Q(B_g,B_{g'})|\ge \frac{M_t}{|H|}.
\]

The sections for different \(t\) are disjoint, so (10) yields

\[
|G||H|\,|Q(B,B)|
\ge |G|\sum_tM_t
\ge\left(\sum_gw_g\right)^2=|B|^2.
\]

The full set \(B=\mathscr F\) has \(Q(B,B)=\mathscr F\), so equality is
possible and (6) is exact.

## D. Key tensor lemma and exact correlation

At each split local factor choose roots \(r_i\ne s_i\). With
\(r=(r_i)\), \(s=(s_i)\), the simultaneous linear change is

\[
u=x-r y,\qquad v=x-s y,
\]

and its inverse is

\[
x=\frac{s u-rv}{s-r},\qquad y=\frac{u-v}{s-r}.
\]

Thus the transformed copy of \(B^2\) is exactly

\[
\left\{(u,v):
\frac{s u-rv}{s-r}\in B,
\frac{u-v}{s-r}\in B
\right\},
\tag{11}
\]

and \(Q=uv\) coordinatewise. Formula (11), an intersection of two linear
pullbacks of the same globally correlated set, is the correlation that cannot be
replaced by a product \(U\times V\).

The correct abstract strengthening of a scalar image inequality is the following.
For a finite map \(f:X^2\to Y\), define

\[
\tau(f)=\inf_{\alpha,\beta\ge0}
\frac{|X|\sum_{z\in Y}\max_{f(x,y)=z}\alpha_x\beta_y}
{(\sum_x\alpha_x)(\sum_y\beta_y)}.
\tag{12}
\]

Zero denominators are omitted. Then

\[
\boxed{\tau(f\otimes g)=\tau(f)\tau(g).}
\tag{13}
\]

For the lower bound, let \(A_{x,u},B_{y,v}\) be weights on the product. For
fixed \(x,y\), apply the defining inequality for \(g\) to the \(u,v\) rows.
For each outer output, use

\[
\sum_s\max_{f(x,y)=t}c_{x,y,s}
\ge \max_{f(x,y)=t}\sum_sc_{x,y,s},
\]

and then apply the inequality for \(f\) to the row sums. This gives the product
of the two constants. Product-form weights give the reverse inequality in (13).

For indicator weights of arbitrary \(A,C\subseteq X\), the sum of maxima in
(12) is exactly \(|f(A,C)|\). Therefore

\[
\boxed{\tau(f)\ge1}
\tag{BW}
\]

for every local split factor would imply the full rectangular product inequality,
and hence CRT-Q, for every number of correlated factors. The abstract example in
Section B fails (BW): the weights \((4,2,2,4)\) give normalized value \(8/9\).

There is an exact zero-error reformulation. For fixed weights let

\[
E_u=\{(x,y):\alpha_x\beta_y\ge u\}.
\]

After ordering the two vertex classes by their weights, every \(E_u\) is a
Ferrers (chain) bipartite graph, and layer-cake gives

\[
\sum_z\max_{f(x,y)=z}\alpha_x\beta_y
=\int_0^\infty |f(E_u)|\,du,
\qquad
(\sum\alpha)(\sum\beta)=\int_0^\infty|E_u|\,du.
\tag{14}
\]

Thus the local inequality \(|X||f(E)|\ge|E|\) for all Ferrers edge sets would
imply (BW). Ordinary Shannon entropy cannot replace this zero-error statement.
Indeed, for uniform independent inputs over a split field of size \(q\), the
split coordinates are uniform independent \(u,v\), and

\[
\Pr(uv=0)=\frac{2q-1}{q^2},\qquad
\Pr(uv=t)=\frac{q-1}{q^2}\quad(t\ne0).
\]

This distribution is nonuniform, so \(H(Q)<\log q\); the naive local entropy
inequality \(H(Q)\ge H(x)+H(y)-\log q\) already fails for uniform inputs.

## E. Quantitative bounds and correlated families

### E.1 General products of split residue fields

Let \(S\) index the factors in which \(3\) is square, and let \(s=|S|\). In a
split field \(F_q\), a nonzero full fiber of \(Q\) has \(q-1\) points and the
zero fiber has \(2q-1\) points. Hence, for arbitrary nonnegative weights,

\[
\left(\sum_x\alpha_x\right)\left(\sum_y\beta_y\right)
\le(2q-1)\sum_t\max_{Q(x,y)=t}\alpha_x\beta_y,
\]

so

\[
\tau(Q;F_q)\ge\frac{q}{2q-1}>\frac12.
\tag{15}
\]

Group all nonsquare-\(3\) factors and use (9). On the remaining \(s\) factors,
iterate (15) on \(s-1\) factors and use (RL), with constant \(1\), on the last.
This proves, for \(s\ge1\),

\[
\boxed{
C(\mathscr F)\ge
\max_{j\in S}\prod_{i\in S\setminus\{j\}}
\frac{q_i}{2q_i-1}
>2^{-(s-1)}.
}
\tag{16}
\]

For \(s=0\), Theorem 1 gives \(C=1\). Thus \(C=1\) is exact for \(s\le1\),
while for \(s\ge2\) the present rigorous interval is

\[
2^{-(s-1)}<C(\mathscr F)\le1.
\]

The upper bound is again supplied by the full ambient set. The exact value in the
last regime is not determined.

### E.2 Arbitrary split prime-power factors

Let \(\mathcal R_k\) have residue size \(R\), and put \(n=R^k\). The split
linear transformation is bijective and changes \(Q\) to \(uv\). If
\(v(t)=j<k\), direct valuation counting gives

\[
|Q^{-1}(t)|=(j+1)(R-1)R^{k-1};
\]

for \(t=0\), it gives

\[
|Q^{-1}(0)|=R^k+k(R-1)R^{k-1}
=R^{k-1}\bigl(R+k(R-1)\bigr).
\tag{17}
\]

For completeness, in the nonzero case choose \(v(u)=h\), where
\(0\le h\le j\). There are \((R-1)R^{k-h-1}\) choices for \(u\), and then
\(R^h\) choices for \(v\). For \(uv=0\), each of the \(k\) finite valuations
of \(u\) contributes \((R-1)R^{k-1}\) pairs, and \(u=0\) contributes \(R^k\).
Thus (17) is the largest full fiber.

The maximum-fiber argument in (12) now gives

\[
\tau(Q;\mathcal R_k)
\ge c(R,k):=\frac{R}{R+k(R-1)}
=\frac1{1+k(1-1/R)}.
\tag{18}
\]

By (13), every arbitrary correlated \(B\subseteq\prod_i\mathcal R_i\) obeys

\[
\boxed{
N|Q(B,B)|
\ge
\left(\prod_{i=1}^t
\frac{R_i}{R_i+k_i(R_i-1)}\right)|B|^2.
}
\tag{19}
\]

If all depths are at most \(K\), the certified constant is at least
\((K+1)^{-t}=e^{-O(t)}\). With unbounded depths, the logarithmic loss in (18)
is at most \(\sum_i\log(k_i+1)\), but is not \(o(t)\) uniformly. Thus (18) is
quantitative but does not rule out the exponentially small regime relevant to the
global problem.

### E.3 A broad correlated valuation family has constant \(1\)

For each factor choose \(1\le h_i\le k_i\), and put

\[
D_i=\pi_i^{h_i}\mathcal R_i,qquad U_i=\mathcal R_i\setminus D_i.
\]

For an arbitrary family \(\mathcal F\subseteq\{0,1\}^t\), define the genuinely
correlated union of cells

\[
B_{\mathcal F}=
\bigcup_{\sigma\in\mathcal F}
\prod_{i=1}^t
\begin{cases}
D_i,&\sigma_i=1,\\
U_i,&\sigma_i=0.
\end{cases}
\tag{20}
\]

Then

\[
\boxed{N|Q(B_{\mathcal F},B_{\mathcal F})|
\ge |B_{\mathcal F}|^2.}
\tag{21}
\]

This includes arbitrary Boolean codes, antichains, linked-depth threshold sets,
and recursive binary Cantor conditions at the chosen depths.

To prove (21), work at one coordinate and write
\(p=|D|/|\mathcal R_k|=R^{-h}\). Set

\[
A=Q(D,D)=\pi^{2h}\mathcal R_k,
\]

with the convention that this is \(\{0\}\) when \(2h\ge k\). Its output
density is at least \(p^2\). Let \(S\) be the set of unit squares. The stated
Hensel fact gives

\[
\frac{|S|}{|\mathcal R_k|}=\frac{R-1}{2R},
\]

and \(S\subseteq Q(D,U)\cap Q(U,D)\), since \(Q(0,y)=y^2\). The sets \(A\)
and \(S\) are disjoint. Moreover

\[
2p(1-p)\le\frac{2(R-1)}{R^2}
\le\frac{R-1}{2R},
\tag{22}
\]

because every good odd split residue field has \(R\ge7\).

Finally,

\[
Q(U,U)=\mathcal R_k.
\tag{23}
\]

Indeed, units lie in \(U\). In split coordinates \(uv=t\), if \(t\) is a
nonunit choose \(u\) a unit and \(v=t/u\); the inverse formulas make both
original coordinates units. If \(t\) is a unit, choose the residue of \(u\)
to avoid the at most four nonzero residues satisfying
\(u^2=t\) or \(u^2=(r/s)t\). Since \(R-1\ge6\), such a unit exists, and again
the inverse coordinates are units.

Now take two independent Bernoulli\((p)\) state bits \(X,Y\). Couple them to a
uniform output \(C\in\mathcal R_k\) as follows. Allocate the state \((1,1)\),
of mass \(p^2\), inside \(A\); allocate the two exact-one states, of total mass
\(2p(1-p)\), inside \(S\); and allocate the remaining uniform output mass to
state \((0,0)\). The capacity inequalities above and the disjointness of
\(A,S\) make the residual measure nonnegative, while (23) makes every residual
output compatible with \((0,0)\).

Take these couplings independently in all coordinates. The output vector \(C\)
is uniform on \(\mathscr R\), and the two state vectors \(X,Y\) are independent
with exactly the state distribution of a uniform input vector. Whenever
\(X,Y\in\mathcal F\), coordinatewise compatibility shows
\(C\in Q(B_{\mathcal F},B_{\mathcal F})\). Hence, writing
\(\beta=|B_{\mathcal F}|/N\) and
\(\gamma=|Q(B_{\mathcal F},B_{\mathcal F})|/N\),

\[
\gamma\ge\Pr(X\in\mathcal F,Y\in\mathcal F)=\beta^2,
\]

which is (21). This argument charges the loss of every input restriction exactly;
there is no hidden independence assumption on \(\mathcal F\).

## F. Constants and extremizers

The current ledger is:

| setting | rigorous constant | status |
|---|---:|---|
| abstract symmetric maps with every local rectangular bound | at most \((8/9)^{\lfloor t/2\rfloor}\) | exponential failure exists |
| split fields, at most one \(q_i\equiv1\pmod {12}\) | \(C=1\) | exact |
| split fields, \(s\ge2\) such factors | \(2^{-(s-1)}<C\le1\) | exact value open |
| arbitrary split prime powers | \(\prod_i[1+k_i(1-1/R_i)]^{-1}\le C\le1\) | exact value open |
| binary ideal-pattern sets (20) | \(\lambda(B_{\mathcal F})\ge1\) | exact no-compression theorem |

The full ambient set always has normalized factor \(1\). Products of central
ideals \(B=\prod_i\pi_i^{h_i}\mathcal R_i\) also have factor \(1\) whenever
\(2h_i\le k_i\) in every coordinate. Thus \(1\) is the correct sharp constant
in every class where the lower bound \(1\) has been proved.

Single graphs \(B=\{(x,\phi(x))\}\) have \(|B|=\sqrt N\), so their CRT-Q
threshold is only \(|Q(B,B)|\ge1\); they cannot by themselves supply a
counterexample. Theorem (21) rules out the much broader natural attempt of linking
valuation depths across primes by arbitrary Boolean codes.

## G. Consequence for the global \(Q(A,A)\) problem

This checkpoint changes a structural assumption from the closed branches: the local
input is allowed to be arbitrarily correlated across split primes. The abstract
counterexample proves that the frozen one-place constants alone do not close this
branch.

For the actual norm form, however, two large correlated regimes are now closed:

* all depth-one products having at most one \(3\)-square residue field;
* all arbitrary-depth correlations determined solely by membership in one chosen
  ideal at each place.

The only unconditional general estimate presently available is (19), whose constant
can be exponentially small in the number of bounded-depth factors. Therefore the
current theorem does not prove an \(e^{-o(t)}\) lower bound and does not close all
correlated split-CRT constructions. Any successful escape must use finer residue or
valuation information than the binary ideal states in (20), and in the depth-one
case must involve at least two \(q\equiv1\pmod {12}\) factors.

If the weighted inequality below is true, then (13) gives \(C_t=1\) for arbitrary
products. Combined with the frozen inert and ramified obstructions, that would close
the entire Cartesian local-restriction strategy. If it is false, the failure must
still be converted into actual indicator sets and must survive the global
discriminant, CRT-index, and lattice-packing costs; a weighted failure alone is not
yet a construction of a small real image set.

## H. Exactly one next unresolved statement

Prove or refute the following local weighted assertion:

\[
\boxed{
|\mathcal R_k|
\sum_{t\in\mathcal R_k}
\max_{Q(x,y)=t}\alpha_x\beta_y
\ge
\left(\sum_x\alpha_x\right)
\left(\sum_y\beta_y\right)
\quad
(\alpha,\beta\ge0)
}
\tag{BW-Q}
\]

for every good split local ring \(\mathcal R_k\). By the exact tensor identity
(13), (BW-Q) would imply CRT-Q with the sharp constant \(C_t=1\) for every number
of split prime-power factors. The frozen same-set one-place theorem does not imply
(BW-Q), as Section B shows in the abstract setting.
