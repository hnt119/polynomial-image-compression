# The weighted local inequality for \(Q(x,y)=x^2+xy+y^2\)

## A. Frozen checkpoint and verdict

All five frozen conclusions in the problem statement are used as hypotheses. In
particular, this report does not infer weighted tensorization from an ordinary
one-place image inequality, and it does not reopen any inert-prime, ramified-prime,
or one-place Cartesian construction.

The full assertion

\[
|\mathcal R_k|\sum_t\max_{Q(x,y)=t}\alpha_x\beta_y
\ge \Bigl(\sum_x\alpha_x\Bigr)\Bigl(\sum_y\beta_y\Bigr)
\tag{BW-Q}
\]

remains unresolved for every good split local ring. The strongest new positive
result is nevertheless an all-depth theorem:

> **Theorem A (all depths over residue field \(\mathbb F_{13}\)).**  Let
> \(\mathcal O\) be a DVR, let \(\mathfrak p=(\pi)\), suppose
> \(\mathcal O/\mathfrak p\cong\mathbb F_{13}\), and put
> \(\mathcal R_k=\mathcal O/\mathfrak p^k\). Then
> \[
> \boxed{\tau(Q;\mathcal R_k)=1\qquad(k\ge 1).}
> \]

Thus BW-Q is true, sharply, at every prime-power depth above the smallest
previously unresolved split residue field. The proof combines two exact finite
Ferrers certificates over \(\mathbb F_{13}\) with a singular
\(k\mapsto k-2\) lifting theorem.

There is one logical correction to the wording of the research prompt. The
Ferrers inequality

\[
|X|\,|f(E)|\ge |E|\qquad(E\text{ Ferrers})
\tag{F}
\]

implies the weighted inequality by layer cake, but is not equivalent to it for
an arbitrary finite map. For example, the symmetric table

\[
\begin{pmatrix}0&0\\0&1\end{pmatrix}
\]

has \(\tau=1\), while its three-edge zero fiber is Ferrers and violates (F).
To verify the first claim, scale nonzero weights to
\(\alpha=(x,1)\), \(\beta=(y,1)\). The weighted numerator is
\(2(1+\max\{xy,x,y\})\), and

\[
2(1+\max\{xy,x,y\})\ge(x+1)(y+1)
\]

follows separately in the cases where the maximum is \(xy\), \(x\), or
\(y\); the three differences are respectively
\((x-1)(y-1)\), \((x+1)(1-y)\), and \((y+1)(1-x)\).
Accordingly, every use of F-Q below is explicitly one-way.

## B. Exact LP dual and split Ferrers geometry

Let \(f:X^2\to Y\), \(n=|X|\), and \(F_t=f^{-1}(t)\). Define

\[
\mathcal P_f=
\left\{\lambda_{xy}\ge0:
\sum_{(x,y)\in F_t}\lambda_{xy}\le1\quad(t\in Y)\right\}.
\]

For every nonnegative matrix \(w\), independence of the constraints on the
different fibers gives

\[
\sum_t\max_{F_t}w_{xy}
=\max_{\lambda\in\mathcal P_f}\sum_{x,y}\lambda_{xy}w_{xy}.
\tag{1}
\]

Normalize \(\sum_y\beta_y=1\). The standard result used here is the following
finite-dimensional minimax theorem: if \(K,L\) are compact convex subsets of
finite-dimensional real vector spaces and \(B\) is a continuous bilinear form,
then

\[
\min_{x\in K}\max_{y\in L}B(x,y)
=\max_{y\in L}\min_{x\in K}B(x,y).
\]

Applying it to (1) and to the probability simplex in \(\alpha\) proves that BW
is equivalent to the following fractional-capacity certificate:

> For every probability vector \(\beta\), there are \(h_{xy}\ge0\) such that
> \[
> \sum_y\beta_yh_{xy}=1\quad(x\in X),
> \qquad
> \sum_{f(x,y)=t}h_{xy}\le n\quad(t\in Y).
> \tag{2}
> \]

Indeed, take \(h=n\lambda\); row coverages larger than one can be trimmed
rowwise without increasing any output load.

At a split place choose \(r\ne s\) with

\[
Q(x,y)=(x-r y)(x-s y).
\]

The exact change of coordinates and its inverse are

\[
u=x-r y,\qquad v=x-s y,
\]

\[
x=\frac{s u-rv}{s-r},
\qquad
y=\frac{u-v}{s-r}.
\tag{3}
\]

If a Ferrers graph has nested row neighborhoods
\(C_1\supseteq C_2\supseteq\cdots\) in rows \(x_i\), then in \((u,v)\)
coordinates it is exactly

\[
\bigcup_i
\left\{(u,v):
s u-rv=(s-r)x_i,
\quad
\frac{u-v}{s-r}\in C_i
\right\}.
\tag{4}
\]

Thus the transformed set consists of nested cuts on parallel affine lines. It
is not an arbitrary product \(U\times V\).

## C. Depth-one field result and exact \(q=13\) certificate

For \(T\subseteq\mathbb F_{13}\), define

\[
N_T(x)=\{y:Q(x,y)\in T\},
\qquad
I_T(S)=\bigcap_{x\in S}N_T(x).
\]

If the rows are ordered \(x_1,\ldots,x_{13}\) with decreasing Ferrers
neighborhoods, row \(j\) is contained in
\(I_T(\{x_1,\ldots,x_j\})\). Conversely, taking equality at every row gives
an allowed Ferrers graph. Hence the exact maximum is

\[
D_T(\varnothing)=0,
\qquad
D_T(S)=|I_T(S)|+
\max_{x\in S}D_T(S\setminus\{x\}).
\tag{5}
\]

This subset recurrence checks all \(13!\) row orders without enumerating them.
Enumerating the \(2^{13}\) output sets, using exact integer bit masks, gives

\[
\begin{array}{c|rrrrrrrrrrrrrr}
m&0&1&2&3&4&5&6&7&8&9&10&11&12&13\\ \hline
\max_{|T|=m}D_T&
0&3&10&18&29&40&50&61&75&87&107&127&144&169.
\end{array}
\tag{6}
\]

Every entry is at most \(13m\), with strict inequality for
\(0<m<13\). Therefore

\[
13|Q(E)|\ge |E|
\]

for every Ferrers \(E\subseteq\mathbb F_{13}^2\). Layer cake proves
\(\tau(Q;\mathbb F_{13})\ge1\), and uniform weights give equality. Thus

\[
\boxed{\tau(Q;\mathbb F_{13})=1.}
\tag{7}
\]

The computation was independently recompiled and reproduced. The source
`q13_ferrers_exact.cpp` has SHA-256

```text
8c82d9b211e27e4980ec867e91791d93a06ea4bad9f029972f3df73cb4e483ec
```

The strict entries in (6) also classify weighted equality: for nonzero weights,
equality in BW-Q occurs exactly when both \(\alpha\) and \(\beta\) are positive
constant functions.

For general split \(\mathbb F_q\), the field classification now reads as
follows.

* The frozen \(3\)-nonsquare regime \(q\equiv7\pmod {12}\) is settled.
* The first \(3\)-square case \(q=13\) is settled by (7).
* General \(q\equiv1\pmod {12}\) remains unresolved, but the symbolic regimes
  in Section D are proved.

## D. Symbolic finite-field Ferrers theorems

Let \(F=\mathbb F_q\) be any good split field, let \(E\subseteq F^2\) be
Ferrers, and put \(S=Q(E)\), \(m=|S|\). Then F-Q holds in each of the
following regimes:

\[
m\le \frac q4,
\tag{8}
\]

\[
q-m<\frac{4(q-1)}{25},
\tag{9}
\]

and, if \(0\in S\),

\[
F\setminus S\subseteq(-2r)(F^\times)^2.
\tag{10}
\]

For (8), every row and column degree is at most \(2m\). A nonempty Ferrers
graph with maximum row and column degree \(\Delta\) has at most
\(\Delta^2\) edges: its active row neighborhoods are nested, so a column in
the smallest nonempty neighborhood meets every active row; there are at most
\(\Delta\) active rows, each of degree at most \(\Delta\). Hence

\[
|E|\le4m^2\le qm.
\]

For (9), the case \(0\notin S\) is immediate because every used fiber has
size \(q-1\). Otherwise put \(T=F\setminus S\), \(n=|T|\),
\(H_T=Q^{-1}(T)\), and \(C=F^2\setminus E\). The complement \(C\) is
Ferrers after reversing one order, contains \(H_T\), and

\[
|H_T|=n(q-1).
\]

If F-Q failed and \(g=|C\setminus H_T|\), then \(g<n\). Every row and
column of \(H_T\) has degree at most \(2n\). If \(C\) has \(R\) active rows
and \(C_0\) active columns, set

\[
a=(R-2n)_+,
\qquad
b=(C_0-2n)_+.
\]

The common column of all active rows forces at least \(a\) added edges; the
common row of all active columns forces at least \(b\), with at most one common
cell. Thus \(a+b\le g+1\le n\), and

\[
n(q-1)\le |C|
\le (2n+a)(2n+b)
\le\frac{25}{4}n^2.
\]

This contradicts (9).

For (10), each excluded value \(t=-2rA^2\) supplies two allowed zero-fiber
edges

\[
(rA,A),\qquad(-rA,-A),
\]

whose cross-values both equal \(t\). A Ferrers graph cannot contain both
zero edges, because it would have to contain one excluded cross cell. The pairs
belonging to distinct \(t\)'s are disjoint. Since

\[
|Q^{-1}(S)|=qm+|F\setminus S|,
\]

this proves the more precise estimate

\[
|E|\le qm+
\left|(F\setminus S)\setminus(-2r)(F^\times)^2\right|.
\tag{11}
\]

When \(q\equiv1\pmod {12}\), \(-1\) and \(r\) are squares, so the coset in
(10) is exactly \(\{t:\chi(t)=\chi(2)\}\).

Consequently a symbolic field counterexample must have

\[
\frac q4<m\le q-\frac{4(q-1)}{25},
\tag{12}
\]

and its excluded output set must contain an element of character
\(-\chi(2)\).

## E. Singular lifting and the strengthened residue inequality

Let \(q=|\mathcal O/\mathfrak p|\), let \(M_k(T)\) denote the maximum
\(\alpha_x\beta_y\) on the \(T\)-fiber in \(\mathcal R_k\), and define

\[
A_a=\sum_{x\equiv a\pmod{\mathfrak p}}\alpha_x,
\qquad
B_b=\sum_{y\equiv b\pmod{\mathfrak p}}\beta_y,
\]

\[
c=A_0B_0,
\qquad
L_t=\max_{\substack{Q(a,b)=t\\(a,b)\ne(0,0)}}A_aB_b.
\]

Suppose BW-Q at depth \(k-2\) has constant \(\rho\). Then

\[
\boxed{
q^k\sum_{T\in\mathcal R_k}M_k(T)
\ge
\max\{\rho c,qL_0\}
+q\sum_{t\in\mathbb F_q^\times}L_t.
}
\tag{13}
\]

Here is the complete factor audit. At a noncentral residue pair
\((a,b)\ne(0,0)\), at least one of

\[
2a+b,\qquad a+2b
\]

is nonzero because their coefficient matrix has determinant \(3\). The
standard theorem used is this finite Hensel/submersion statement:

> If a one-variable polynomial over a DVR has a simple root modulo
> \(\mathfrak p\), then, for every target lift modulo \(\mathfrak p^k\), that
> root has a unique lift in its fixed residue class. Consequently, a smooth
> map from a two-dimensional residue block to a one-dimensional target block
> has exactly \(q^{k-1}\) points in each target fiber.

Therefore fiber averaging in the residue block gives

\[
\sum_{T\equiv Q(a,b)}M_k(T)
\ge\frac{A_aB_b}{q^{k-1}}.
\]

After multiplication by \(q^k\), the best block above residue output \(t\)
contributes \(qL_t\).

For the central block write \(x=\pi X\), \(y=\pi Y\). Since

\[
Q(\pi X,\pi Y)=\pi^2Q(X,Y),
\]

the output depends only on \(X,Y\pmod{\pi^{k-2}}\). Put

\[
\widehat\alpha_\xi=
\max_{X\equiv\xi\pmod{\pi^{k-2}}}\alpha_{\pi X}.
\]

Each \(\xi\) has exactly \(q\) lifts, so

\[
\sum_\xi\widehat\alpha_\xi\ge A_0/q,
\qquad
\sum_\eta\widehat\beta_\eta\ge B_0/q.
\]

Depth \(k-2\) BW-Q, followed by multiplication by the missing factor \(q^2\),
gives the central contribution \(\rho c\). The central and nonsingular-zero
output sets overlap, so they must be combined by a maximum, not a sum. This is
exactly the first term in (13).

The residue statement needed for a sharp induction is

\[
\boxed{
\max\{A_0B_0,qL_0\}
+q\sum_{t\ne0}L_t
\ge
\Bigl(\sum_aA_a\Bigr)\Bigl(\sum_bB_b\Bigr).
}
\tag{SR\(_q\)}
\]

It is strictly stronger than ordinary field BW-Q at the distinguished central
pair. If SR\(_q\) holds, (13) inducts separately on even and odd \(k\), from
the singleton ring and from the residue field, and proves \(\tau=1\) at every
depth.

## F. The distinguished \(q=13\) certificate and proof of Theorem A

For \(T\subseteq\mathbb F_{13}^\times\), an independent exact DP maximizes
Ferrers graphs satisfying

\[
(0,0)\in E
\subseteq\{(0,0)\}\cup Q^{-1}(T).
\]

The maxima are

\[
\begin{array}{c|rrrrrrrrrrrrr}
m&0&1&2&3&4&5&6&7&8&9&10&11&12\\ \hline
\max |E|&1&6&13&19&26&35&43&51&57&63&66&74&83.
\end{array}
\tag{14}
\]

This is the same exact recurrence (5), now with allowed neighborhoods from
\(\{(0,0)\}\cup Q^{-1}(T)\).  A two-state flag records whether, at the stage
where row \(0\) is appended, the current intersection contains column \(0\).
Requiring the final flag to be one is exactly the condition
\((0,0)\in E\). Thus the calculation again exhausts every row ordering and
does not relax the distinguished-center constraint.

Thus for every nonempty \(T\),

\[
13|T|-|E|\ge7.
\tag{15}
\]

The source `q13_distinguished_dp.cpp` has SHA-256

```text
dbb49ed9f51735e8972c82da597ca67df8defb91ecbb1e11cafdb39bada4bf36
```

To pass from (15) to SR\(_{13}\), put

\[
c=A_0B_0,
\qquad \ell=L_0,
\qquad H=\max_{t\ne0}L_t,
\]

and use the Ferrers levels

\[
E_u=\{(a,b):A_aB_b\ge u\}.
\]

Define

\[
D(u)=13|Q(E_u\setminus\{(0,0)\})|-|E_u|.
\]

Layer cake gives

\[
\int_0^\infty D(u)\,du
=13\left(\ell+\sum_{t\ne0}L_t\right)-AB.
\tag{16}
\]

For \(u>c\), the center is absent; for \(u\le\ell\), a punctured zero edge
remains after deleting the center. In both ranges ordinary F-Q gives
\(D(u)\ge0\). On \(\ell<u\le c\), (15) gives \(D(u)\ge7\) when a nonzero
output occurs and \(D(u)=-1\) otherwise.

A punctured zero maximizer \((a,b)\) has \(a,b\ne0\). The cross pairs
\((a,0)\), \((0,b)\) have nonzero outputs, and their two weights have product
\(c\ell\). Hence

\[
H\ge\sqrt{c\ell}.
\tag{17}
\]

For \(0<\ell<c\), write \(r=\ell/c\). Equations (15)--(17) give

\[
\int D\ge
c(1-\sqrt r)(7\sqrt r-1).
\tag{18}
\]

If \(r\ge1/49\), this is nonnegative. If \(r\le1/49\), then
\(13\ell\le c\), and the correction needed to turn (16) into the SR numerator
is \(c-13\ell\). Therefore

\[
\int D+c-13\ell
\ge c(8\sqrt r-20r)\ge0.
\tag{19}
\]

The cases \(\ell=0\) and \(c\le\ell\) follow directly. This proves
SR\(_{13}\). Applying (13) proves Theorem A.

More generally, the same argument proves SR\(_q\) if ordinary F-Q holds and
every nonempty distinguished graph has a gap

\[
q|T|-|E|\ge\delta\ge\sqrt q.
\tag{20}
\]

For \(q\ge37\), the gap part of (20) is automatic. Indeed a distinguished
graph has maximum row and column degree at most \(2m+1\), so

\[
|E|\le(2m+1)^2,
\qquad
|E|\le1+(q-1)m.
\]

Consequently

\[
qm-|E|\ge
\max\{m-1,\;qm-(2m+1)^2\}.
\tag{21}
\]

Writing \(t=\sqrt q\ge6\), the second expression is a concave function of
\(m\). On \(1\le m\le t+1\), its minimum is at an endpoint, where it is at
least \(t\); for \(m\ge t+1\), the first expression is at least \(t\).
Thus (20) follows. For all \(q\ge37\), the only missing input to this sharp
lifting criterion is ordinary finite-field F-Q.

## G. General dual certificates and counterexample restrictions

Normalize \(\sum_y\beta_y=1\). The exact dual (2) gives the following
symbolic positive regimes over every split \(\mathbb F_q\).

1. If \(\max_y\beta_y\ge2/q\), choose such a column \(y_0\), put
   \(h_{x,y_0}=1/\beta_{y_0}\), and put all other entries to zero. Each output
   equation has at most two solutions in \(x\), so every output load is at most
   \(2/\beta_{y_0}\le q\).
2. If \(\sum_y\beta_y^2\ge2/q\), put
   \[
   h_{xy}=\frac{\beta_y}{\sum_z\beta_z^2}.
   \]
   Again, each output load is at most \(2/\sum\beta^2\le q\).
3. The sharp uniform certificate is
   \[
   h_{00}=0,
   \quad
   h_{xy}=\frac q{2(q-1)}\quad(Q(x,y)=0,(x,y)\ne(0,0)),
   \]
   \[
   h_{xy}=\frac q{q-1}\quad(Q(x,y)\ne0).
   \]
   Row normalization preserves its output capacities whenever
   \[
   \beta_0\le1/q,
   \qquad
   \beta_{x/r}+\beta_{x/s}\le2/q\quad(x\ne0).
   \]

Thus a depth-one counterexample must be diffuse in both weights and must also
overload a central atom or a neighboring pair on an isotropic three-cycle in
both one-sided dual tests.

## H. Exact or best-known \(\tau\), and CRT consequence

The current ledger is

| local factor | exact/best rigorous value |
|---|---:|
| \(\mathbb F_q\), frozen \(q\equiv7\pmod {12}\) regime | \(\tau=1\) |
| \(\mathbb F_{13}\) | \(\tau=1\) |
| \(\mathcal O/\mathfrak p^k\), residue \(\mathbb F_{13}\) | \(\tau=1\) for every \(k\) |
| general good split \(\mathcal R_k\) | \(\frac{q}{q+k(q-1)}\le\tau\le1\) |

The upper bound is supplied by uniform weights, since split coordinates make
\(Q=uv\) surjective.

By the frozen exact tensor identity, every product of split local factors with
residue \(\mathbb F_{13}\), at arbitrary and unequal depths, satisfies

\[
N|Q(B,B)|\ge|B|^2
\]

for every correlated subset of the product. Hence such factors provide no
cross-prime Cartesian compression at all.

If a common probability weight \(w\) ever gives \(q\sum_tM_t=\rho<1\), exact
type classes in tensor powers give actual correlated indicator sets with

\[
\lambda(B_m)\le (m+1)^{2q}\rho^m.
\]

Thus a common-weight failure would produce exponential set-level loss. An
asymmetric pair \((\alpha,\beta)\) does not automatically give one same-set
counterexample; it gives rectangular type classes, and an additional
symmetrization condition is needed. This distinction prevents an unjustified
claim about the global real problem from a merely asymmetric weighted failure.

## I. Consequence and exactly one next unresolved statement

The all-depth \(q=13\) theorem closes every correlated split-CRT construction
built only from residue-
\(13\) factors. It does not close the full split local-restriction branch, and
it does not by itself construct or rule out real sets with a fixed power saving.

The single next unresolved statement is:

\[
\boxed{
\mathrm{SR}_q\text{ holds for every good split finite residue field }\mathbb F_q.
}
\]

Explicitly, this is the assertion

\[
\max\{A_0B_0,qL_0\}
+q\sum_{t\ne0}L_t
\ge
\Bigl(\sum_aA_a\Bigr)\Bigl(\sum_bB_b\Bigr)
\]

for all nonnegative residue weights. It is a finite-field statement, is strictly
stronger than ordinary depth-one BW at the central singular branch, and, by
(13), would settle BW-Q with \(\tau=1\) at every prime-power depth.
