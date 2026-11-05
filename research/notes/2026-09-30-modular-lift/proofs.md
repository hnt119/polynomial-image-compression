# Exact lifts and their scope — proof companion

30 September 2026 · T03 · version 1 · fixed real polynomial
$Q(x,y)=x^2+xy+y^2$.

**Authorization:** the user's “7^k Modular-to-Real Lift” attachment
`[private attachment identifier withheld]`. Strictly offline. These are new
written proofs and applications within that lift obligation, not a rerun
of the frozen modular theorem. No external theorem or novelty claim.
The lead derived and checked the proofs; no independent review is claimed.

## Sources and claim register

The frozen [MG-1–MG-4](../2026-09-21-return-tail/modular-gadget.md)
supply the modular group, split coordinates, stabilizers and tail. Their
centered-lift and rational-torsion failures remain unchanged. The
[DC-R1 transport](../2026-09-21-dense-cartesianization/block-rectangle.md),
§4, remains the sufficient real support theorem. Ordinary field degree,
Eisenstein irreducibility and cyclotomic degree are accepted project facts
(T03 current-state §10); no new outside input is imported.

| ID | Status / quantified scope | Proof locator |
|---|---|---|
| ML-1 | PROVED: exact carry equations and linear-size exact discrepancy state for the stated diagonal family | §1 |
| ML-2 | PROVED: any scalar map preserving the order-three diagonal returns has image at most k+1 | §2 |
| ML-3 | PROVED: explicit separated base-7 digit lift has all fibers at most 2401; exact cyclic carry relations collapse | §3 |
| ML-4 | PROVED: injective equivariant algebraic encoding of every primitive modular pair; same-set completion and its exact obstruction | §§4–6 |
| ML-5 | PROVED: bounded-state equivariant-cover obstruction under faithful action and injective state encoding | §7 |

All pair counts below are ordered. Maps count distinct targets, not labels.

## 1. ML-1 — the exact carry/lift error

Put $n=7^k$. Let $p=(x,y)$ and $q=(v,w)$ be integer representatives
of a modular return. Then $e=(Q(q)-Q(p))/n$ is an integer. For arbitrary
source and target carry vectors $d=(d_1,d_2)$ and $c=(c_1,c_2)$,

$$\begin{aligned}
Q(q+nc)-Q(p+nd)
=n\big[&e+(2v+w)c_1+(v+2w)c_2\\
&-(2x+y)d_1-(x+2y)d_2
+n\{Q(c)-Q(d)\}\big].\tag{1}
\end{aligned}$$

This follows by expanding the three monomials of $Q$. The four linear
terms are the first-order carries; the last term is the quadratic carry.
For a fixed source representative ($d=0$), exact equality holds **if and
only if** the bracket in (1) vanishes. The residue norm alone determines
none of the integer quotient $e$, the representative-dependent gradient,
or the carry vector. These must be retained or solved for.

A matrix version separates the two errors. Put
$J=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)$.
For any integral representative $T$ of the modular action,
$E=(T^tJT-J)/n$ is integral, with even diagonal entries. If the chosen
target is $q=Tp-nc$, then

$$Q(q)-Q(p)=\frac n2p^tEp
-n\nabla Q(Tp)\cdot c+n^2Q(c).\tag{2}$$

The first term is the defect of the integer matrix itself; the other
two arise from reducing its output. Formula (2) does not assume that the
integer matrix is an exact real isometry.

For a concrete size lower bound on an exact discrepancy state, take
centered representatives $[-b,b]$, $b=(n-1)/2$, and the genuine unit
formula $T_\omega(x,y)=(y,-x-y)$. For integers
$b/2<t\le b$, its wrapped image of $(t,t)$ is $(t,n-2t)$, and

$$Q(t,n-2t)-Q(t,t)=n(n-3t).\tag{3}$$

Thus this one diagonal family already gives $\lceil b/2\rceil$
distinct values of $e$. A state from which $e$ alone is recoverable,
without additional input, needs at least that many labels. Centered
representatives also give $|e|<3n/4$, so this quotient has $O(n)$
possible values. A rule which recomputes $e$ from the source is **not**
excluded by this state-count observation. The diagonal has only $O(n)$
pairs; (3) alone is not a quadratic bad-tail theorem.

## 2. ML-2 — scalar algebraic encodings collapse on diagonal returns

**Theorem.** Let $f:\mathbb Z/7^k\mathbb Z\to\mathbb R$ be any map.
Suppose only that the modular return $(t,t)\mapsto(t,-2t)$ lifts to
an exact equality for every residue $t$:

$$Q(f(t),f(t))=Q(f(t),f(-2t)).\tag{4}$$

Then $f$ is constant on every valuation class
$\{t:v_7(t)=j\}$, $0\le j<k$, and hence

$$|f(R_k)|\le k+1.\tag{5}$$

In particular no injective scalar lift of all modular returns exists.
This applies to arbitrary real algebraic encodings, not just additive
or digit-linear ones. It does **not** exclude removing these diagonal
constraints or selecting an action family not containing this action.

**Proof.** With $a=f(t)$, $b=f(-2t)$, (4) factors as

$$(b-a)(b+2a)=0.\tag{6}$$

On a cycle of the permutation $t\mapsto-2t$, a zero value propagates
as zero. Starting from a nonzero value, every step multiplies it by
1 or by $-2$. The product around a cycle is 1, whereas $(-2)^q=1$
for a nonnegative integer $q$ only when $q=0$. Thus every step preserves
the value, and $f(-2t)=f(t)$ for all $t$.

The residue $-2$ generates $(\mathbb Z/7^l\mathbb Z)^\times$ for
every $l\ge1$. Its order modulo 7 is six, and $(-2)^6=64=1+9\cdot7$.
The binomial expansion proves

$$v_7((1+7^a u)^7-1)=a+1\quad(a\ge1,\ 7\nmid u).$$

For an exponent prime to 7 the same expansion retains valuation $a$.
Consequently $v_7(64^q-1)=1+v_7(q)$, so the order is exactly
$6\cdot7^{l-1}$, the number of units. The cycles of multiplication by
$-2$ on $R_k$ are therefore its $k$ nonzero valuation classes and zero.
This proves (5). At least one scalar projection fiber has size
$7^k/(k+1)$. More strongly the unit class of size $6\cdot7^{k-1}$
collapses to one scalar. Its full ordered square collapses to one pair;
none of its modular label multiplicity can be counted as distinct real
returns. $\square$

The bound (5) is a projection obstruction, not a proof that every
unbounded, highly noninjective image family is useless. No return
exponent in the much smaller size $|f(R_k)|$ is asserted without a
separate analysis.

## 3. ML-3 — separated digits and exact additive carries

### 3.1 Explicit faithful digit test

Use digits $x_i\in\{0,\ldots,6\}$ and

$$\Phi(x)=\sum_{i=0}^{k-1}x_i217^{3^i},\qquad A=\Phi(R_k),\quad |A|=7^k.$$

The quadratic coefficients at exponent $2\cdot3^i$ are
$x_i^2+x_iy_i+y_i^2\le108$. At exponent $3^i+3^j$ ($i<j$) they are

$$2x_ix_j+x_iy_j+x_jy_i+2y_iy_j\le216.\tag{7}$$

All these exponents are distinct by their base-three expansions; all
coefficients lie in $[0,216]$. Uniqueness of base-217 expansion means
that equal real $Q$-values have equal complete coefficient data.

For completeness the small-fiber consequence is elementary. Let
$v_i=(x_i,y_i)$ in the positive-definite inner product with matrix
$\left(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\right)$.
The data in (7) and on the diagonal are their Gram matrix. Its rank is
at most two. Choose from the source at most two indices spanning its
vectors. For a target with the same Gram matrix, its vectors at these
indices have at most $49^2=2401$ choices. Once chosen, every other
target vector is uniquely determined: its inner products with this
basis fix its projection, and equality of Gram rank leaves no orthogonal
component. Rank one needs at most 49 choices; rank zero is unique.
Thus every complete image fiber is at most 2401.

Therefore every actual action family on this digit carrier has
$B_\varepsilon=|A|^2$ eventually for every fixed $\varepsilon>0$,
and $|Q(A,A)|\ge |A|^2/2401$. This is an explicit application of the
[retained DC-M4 faithful-Gram obstruction](../2026-09-21-dense-cartesianization/matrix-product.md), §5, not a new general no-go.
It stops the proposed separated-digit architecture without scouting it.

### 3.2 Carry relations built into an algebra

If an additive map $f:R_k\to V$ takes values in any characteristic-zero
vector space, then $7^kf(x)=f(7^kx)=0$, hence $f=0$.
For a digit-linear encoding, imposing **all** exact elementary cyclic
carry relations means

$$7\theta_i=\theta_{i+1}\ (i<k-1),\qquad7\theta_{k-1}=0.$$

They force all $\theta_i=0$. Relations only on selected states, nonlinear
encodings and nonadditive corrections are outside this argument.
ML-2 is stronger for the specific all-return scalar requirement and
does not assume any additive relations.

## 4. ML-4 — an explicit exact two-coordinate lift

The positive step is an actual characteristic-zero action realization.
It preserves equality along modular orbits, not the numerical residue
norm and not equality between different modular orbits.

Put

$$n=7^k,\quad m=6\cdot7^{k-1},\quad t=8\cdot7^{k-1},\quad
\zeta=e^{2\pi i/m},\quad K=\mathbb Q(\zeta),\quad \omega=\zeta^{m/3}.$$

Use the frozen split coordinates $(s,t_0)$, writing $t_0$ to avoid
confusion with the orbit count $t$. The primitive plane consists of
pairs for which at least one of $s,t_0$ is a unit; by invertibility of
the split map it is also $R_k^2\setminus(7R_k)^2$. It has
$48\cdot7^{2k-2}=tm$ pairs. Every such pair has trivial stabilizer,
so there are exactly $t$ free modular orbits, each of size $m$.

Choose in each orbit the least pair in lexicographic order on split
representatives $0,\ldots,n-1$; order these representatives and call
them $p_1,\ldots,p_t$. By §2, $g=-2$ generates the unit group.
Each primitive point is uniquely $T_{g^r}p_j$, $0\le r<m$.

Take the explicit integer and positive real algebraic number

$$D=m(2t+1)+1,\qquad\theta=2^{1/D}.$$

The polynomial $X^D-2$ is Eisenstein at 2, so

$$[K(\theta):K]\ge D/[K:\mathbb Q]\ge D/m>2t+1.\tag{8}$$

In particular $1,\theta,\ldots,\theta^{2t}$ are linearly independent
over $K$. This is the exact equality guarantee; no numerical separation
is used. Define the injective correlated encoding

$$F(T_{g^r}p_j)=3\theta^j\zeta^r\in\mathbb C.\tag{9}$$

Let $\rho(g^r)=\zeta^r$. Then

$$F(T_h p)=\rho(h)F(p),\qquad |F(T_h p)|^2=|F(p)|^2=9\theta^{2j}.
\tag{10}$$

All $m$ actions and all $tm$ encoded points are distinct. The orbit
representative choice makes (9) fully specified and finite; no search
for field parameters or primes occurs.

Decode $z=x-\omega y$ into its unique real pair. Set $\Delta=1+2\omega$.
For $z=3\zeta^r$ the coordinates are the algebraic integers

$$b_r=\Delta(\zeta^r-\zeta^{-r}),\qquad
 a_r=3\zeta^r+\omega b_r.\tag{11}$$

Indeed $\Delta^2=-3$, so $b_r$ is real,
$a_r-\omega b_r=3\zeta^r$, and $a_r$ is real by conjugation.
Their norm is $Q(a_r,b_r)=9$.

The two coordinate projections of this orbit agree: multiplication by
$\omega$ takes $(x,y)$ to $(y,-x-y)$, so each second coordinate is
a first coordinate in the same orbit. Write their common set as $S$.
It is symmetric and contains zero. More explicitly,
$b_r=-2\sqrt3\sin(2\pi r/m)$. Two sine values coincide exactly when
$r'=r$ or $r'=m/2-r$ modulo $m$. The latter involution has no fixed
point because $m/2=3\cdot7^{k-1}$ is odd. Thus

$$|S|=m/2,\qquad q:=|S\setminus\{0\}|=m/2-1.$$

The same-set Cartesian completion is now explicit:

$$A=X=Y=\bigcup_{j=1}^t\theta^jS,\qquad
N=|A|=1+tq=1+\frac{8n}{7}\left(\frac{3n}{7}-1\right).\tag{12}$$

Distinct nonzero scalar labels are distinct by (8). The encoded subset
$E=\{(\theta^j a_r,\theta^j b_r):1\le j\le t,\ 0\le r<m\}$
has exactly $tm$ points in $A^2$, with $m$ genuine returns at each.
Its density is

$$\frac{|E|}{N^2}=\frac{tm}{(1+tq)^2}=\Theta(n^{-2})=\Theta(N^{-1}).
\tag{13}$$

This is the full cost of this coordinate completion, not a Cartesian
interpretation of the primitive modular plane.

## 5. ML-4 — almost all completed pairs have only two selected returns

Let $U=\mu_m$, acting by the genuine real norm matrices
$M_u=\left(\begin{smallmatrix}a&b\\-b&a-b\end{smallmatrix}\right)$
for $u=a+b\omega$, $a,b\in K\cap\mathbb R$.
All matrix coefficients belong to $K$ because of conjugation and (11).

Consider the cross-shell population

$$C=\{(\theta^j a,\theta^\ell b):j\ne\ell,\ a,b\in S\setminus\{0\}\}.
$$

There are exactly

$$|C|=t(t-1)q^2=(N-1)^2(1-1/t)=N^2-O(N^{3/2}).\tag{14}$$

If such a pair returns to $A^2$, independence (8) means each row of
$M_u$ has at most one nonzero entry: otherwise it produces a sum of
two nonzero distinct powers of $\theta$, which is not in $A$. Since
the matrix is invertible, it must be monomial. In this norm-rotation
family the only monomial matrices are $\pm I$: a diagonal matrix has
$b=0$, $a=\pm1$; an antidiagonal matrix would require $a=a-b=0$,
contradicting invertibility. Both signs return, so

$$R_U(p)=2\quad(p\in C).\tag{15}$$

The identity-only population is exactly $\{(0,0)\}$ because $-A=A$
and $\pm1\in U$. Every nonzero stabilizer is trivial; the origin has
$m$ returning labels but only one returned pair. The maximum is $m$,
achieved on $E$. Since $t\ge8$, $q\ge2$, (14) occupies more than half
the square: $|C|/N^2\ge(7/8)(16/17)^2>1/2$. The median is exactly 2.
The geometric mean tends to 2, since the remaining nonzero population
has proportion $O(1/t)$ and return count between 2 and $m$.

For every fixed $\varepsilon>0$, eventually
$B_\varepsilon\ge |C|$. Thus no positive exceptional exponent survives,
despite return exponent $1/2$ on the sparse encoded subset $E$.

## 6. ML-4 — full-fiber strengthening and exact finite reduction

There is also an independent **actual-image obstruction for this
specific carrier**, even if arbitrary additional norm actions are used.
For a cross-shell source, say $j<\ell$,

$$Q(\theta^j a,\theta^\ell b)
=a^2\theta^{2j}+ab\theta^{j+\ell}+b^2\theta^{2\ell}.\tag{16}$$

All three coefficients are nonzero. A same-shell or zero-coordinate
target has only one nonzero exponent, so cannot have the same value
by (8). A cross-shell target has least exponent twice its least shell
index and greatest exponent twice its greatest shell index, with
positive coefficients there. Equality forces the same unordered shell
indices; the two squares then fix the absolute scalar values, and the
middle coefficient fixes their relative sign. Exactly four ordered
real targets remain: the source, its negative, its swap and its negative
swap. They are distinct because nonzero scalar shells are disjoint.
All four belong to $A^2$. Hence

$$|\{(x',y')\in A^2:Q(x',y')=Q(p)\}|=4\quad(p\in C),\tag{17}$$
$$|Q(A,A)|\ge |C|/4=N^2/4-O(N^{3/2}).\tag{18}$$

This image lower bound follows from (16)–(17), not merely from failure
of the selected returns. It rules out every fixed power saving for
this separated-radius completion, not for other modular lifts.

It also permits a small exact finite scout without enumerating $N^2m$
triples. Let $h_r$ be the complete return histogram of $S^2$ under
$U$, counting distinct targets, and let $V=|Q(S,S)|$. Within each
nonzero shell, returns remain in that shell (or have one zero coordinate)
by (8), and their counts are exactly those on $S^2\setminus\{0\}$.
All source pairs partition into these $t$ shell squares, the origin,
and $C$. Therefore the full carrier histogram is exactly

$$H_r=t(h_r-1_{r=1})+1_{r=1}+|C|1_{r=2}.\tag{19}$$

Here $h_1=1$ by the sign argument. Positive same-shell outputs in
different shells are distinct by (8), and (16) separates mixed outputs.
Thus the **full** image size is

$$|Q(A,A)|=1+t(V-1)+|C|/4.\tag{20}$$

The scout enumerates only the exact angular core and modular orbit labels;
(19)–(20), rather than an unperformed full-square enumeration, give
its reported completed-carrier quantities.

## 7. ML-5 — what a subpolynomial carry-state cover cannot do

This statement has explicit extra hypotheses and is not an obstruction
to every multiscale construction. Let $G=R_k^\times$ act on the modular
plane. Let a finite $G$-set $\widetilde\Omega$ have an equivariant map
$\pi:\widetilde\Omega\to R_k^2$ with at most $s$ states above each
base point. Suppose an injective encoding
$F:\widetilde\Omega\to\mathbb C$ satisfies
$F(hq)=\rho(h)F(q)$ for a **faithful** homomorphism
$\rho:G\to\{u:|u|=1\}$.

If a base point has minimum split valuation $a<k$ and possesses a
nonzero encoded lift, then

$$s\ge 7^a.\tag{21}$$

Indeed its modular stabilizer has size $7^a$ by MG-2. It acts inside
that fiber. No nonidentity stabilizer element can fix the chosen state,
since injectivity and faithful rotation at a nonzero complex number
would contradict that equality. The fiber therefore contains its
$7^a$ distinct stabilizer translates. At base zero the corresponding
bound is $s\ge m$ for a nonzero encoded lift.

For $s<7^{k-1}$ put $j=\lfloor\log_7 s\rfloor$. All nonzero base
points divisible by $7^{j+1}$ in both split coordinates lack a nonzero
encoded lift. Their number is

$$\frac{n^2}{7^{2(j+1)}}-1\ \ge\ \frac{n^2}{49s^2}-1.\tag{22}$$

Consequently a cover of all but $O(n^{2-\delta})$ base points needs
$s=\Omega(n^{\delta/2})$ for fixed $0<\delta\le2$. In particular
$s=n^{o(1)}$ cannot retain the frozen full-plane exceptional exponent.
If the real size $N=n^{O(1)}$, then $s=N^{o(1)}$ also fails this test.
Projection collapse, nonfaithful actions, changing the base population
or non-group state transitions do not satisfy these hypotheses.
Polynomially many states might be affordable and are not excluded.

A useful limitation: scalar restriction to units already makes all its
pairs primitive. It has input density $6/7$ and ordered-pair density
$36/49$, so (21) imposes no extra state cost there. In every primitive
modular orbit at least $m/3$ points have both original coordinates units.
To see this, reduce the six-element orbit modulo 7. Each of $x=0$ and
$y=0$ meets a nonzero norm orbit in at most two points; on a product-zero
orbit both original coordinates are nonzero. Thus at least two of the
six points have both coordinates nonzero. Each residue action has
$m/6$ lifts, proving the claim. This restriction retains a good modular
tail but **does not fix** the separated-radius Cartesian failure (14).
Indeed, restricting (9) to unit-coordinate modular sources leaves at least
$m/3$ encoded points on every orbit. Each scalar coordinate value occurs at
most twice on a circle, so its same-set scalar completion has between
$m/6-1$ and $m/2-1$ nonzero scalars in each of the $t$ independent shells.
Writing these shell counts as $q_j$, the completed input size is
$N'=1+\sum_jq_j=\Theta(tm)$ (adjoin zero if necessary), and its cross-shell count is
$(N'-1)^2-\sum_jq_j^2=N'^2-O(N'^{3/2})$. The proof of (17) applies
unchanged. Sign closure is retained because the modular unit restriction
is invariant under -1. Thus this restricted, independently tagged
completion also has exactly four targets on its cross-shell population;
this conclusion does not address algebraically dependent radius tags.

## 8. Exactly one remaining obligation

**OPEN — ML-O1.** Replace (9)'s independent radical tags by explicit
$c_{k,j}\in K_k^\times$ with disjoint cosets $c_{k,j}\mu_m$.
The same formula $F(T_{(-2)^r}p_j)=c_{k,j}\zeta_m^r$ remains exactly
equivariant and injective on the encoded primitive points. Its two
coordinate projections still agree because the group contains omega.
The unproved requirement is a polynomial genuine-return lower tail on
the entire scalar completion, including cross-orbit pairs. Choosing
amplitudes in K avoids the independent-power hypothesis (8); it does
not itself prove coordinate reuse or the tail. This is the single
candidate obligation in the main report, not a new proof search here.
