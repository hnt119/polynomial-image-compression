# Fiber connectivity and coordinate reuse

T01 / growing-step cubic cycle, 2026-09-21 v1.
Fixed polynomial \(P(x,y)=(x-y)^3+x+y\).
All scalar carriers are nonempty finite real sets. The frozen coordinate
identity and single-step bound are used as proved inputs, not reproved.

## GS-P1. The graph is exactly a collection of finite difference graphs

**Meaning.** Each permitted step moves along one cubic fiber. A path must
stay inside the actual finite fiber at every intermediate point. Merely
being able to write a displacement as a sum of permitted steps is insufficient.

**Precise statement — PROVED.** Let \(A\subset\mathbb R\), \(|A|=N\),
and let \(S\subset\mathbb R\setminus\{0\}\) be finite. Use a simple
undirected graph: repeated edges and the two signs of one step count once.
Write \(S^+=\{|s|:s\in S\}\), \(M=|S^+|\). Replacing \(S\) by
\(S^+\) leaves the graph unchanged.

Under \((x,y)\leftrightarrow(u,z)\), its restriction to a fixed fiber \(z\) is
the finite induced graph on

\[
U_A(z)=\{u:x_z(u),y_z(u)\in A\},\qquad
x_z(u)=\frac{z-u^3+u}{2},\quad
y_z(u)=\frac{z-u^3-u}{2},
\]

with an edge exactly when \(|u-v|\in S^+\). Therefore

\[
e(A,S)=\sum_{\tau\in S^+}E_\tau(A),\qquad
|P(A,A)|\le C(A,S),
\tag{1.1}
\]

where \(C\) counts components including isolated vertices. The equality
for edges has no multiplicity loss: a distinct unordered pair has one
positive difference. If \(B\) vertices lie in components smaller than
an integer \(K\ge2\), then

\[
C(A,S)\le N^2/K+B,\qquad |P(A,A)|\le N^2/K+B.
\tag{1.2}
\]

Moreover, using the frozen CR-U1 bound,

\[
e\le5MN^{11/6},\quad C\ge N^2-e,
\quad \#\{\text{nonisolated vertices}\}\le2e.
\tag{1.3}
\]

If all but \(B\) vertices lie in components of size at least \(K\), a
spanning forest also gives

\[
e\ge(1-1/K)(N^2-B).
\tag{1.4}
\]

Thus almost-full polynomial-size coverage necessarily costs
\(M\ge(1/5-o(1))N^{1/6}\).

**Proof.** The frozen symmetry is \((u,z)\mapsto(u+\tau,z)\); its
inverse changes the sign of \(\tau\). This identifies every vertex and
every edge, proving the graph description and the edge equality. Every
component has one output, and every output has at least one component,
which proves the image inequality. Long components number at most
\(N^2/K\), and short components number at most their total \(B\)
vertices. This proves (1.2), including all exceptions. A connected component
of \(r\) vertices requires at least \(r-1\) edges. Summing gives both
the component lower bound and (1.4). The remaining assertions follow by
summing the frozen uniform bound and counting edge endpoints.

**Why it matters.** For \(K\ge N^\varepsilon\) and
\(B=O(N^{2-\delta})\), (1.2) gives
\(O(N^{2-\min(\varepsilon,\delta)})\) for the entire image. Every
strictly smaller positive exponent absorbs its constant eventually.

**Scope.** Edges may form cycles. Their raw count need not equal the
number of identifications; only a spanning forest reduces component count.
This distinction is essential when adding steps to already connected fibers.

## GS-P2. Generated subgroup cosets are an invariant, not a connectivity theorem

**Meaning.** An algebraic expression for a displacement can leave the
finite allowed set while it is being carried out.

**Precise statement — PROVED correction.** If
\(\Gamma=\langle S\rangle_{\mathbb Z}\), every graph component is
contained in \(U_A(z)\cap(u+\Gamma)\). Equality need not hold. It holds
exactly when that finite induced graph is connected; this extra hypothesis
cannot be removed.

**Proof and counterexample.** Along a path all displacements are sums of
elements of \(S\cup(-S)\), proving containment. Take

\[
A=\{-5,-3,0\},\quad z=0,\quad S=\{1\}.
\]

The pairs \((0,0)\) and \((-3,-5)\) both have output zero and have
differences 0 and 2. The nine ordered pairs have outputs, by rows ordered
as \(-5,-3,0\),

\[
\begin{pmatrix}-10&-16&-130\\0&-6&-30\\120&24&0\end{pmatrix}.
\]

Hence \(U_A(0)=\{0,2\}\). They lie in the same coset of
\(\Gamma=\mathbb Z\), but are isolated from each other because difference
1 is absent. Taking \(S=\{2\}\) connects them without changing \(A\).

**Why it matters.** This corrects the unconditional equality proposed in
§13 of the active prompt. The integer-interval laboratory proves connectivity
by an additional no-gap argument, not by subgroup membership alone.

**Scope.** The group law remains valid on the entire real plane. Its
intermediate points need not remain in a chosen finite Cartesian square.

## GS-P3. A fully occupied output-by-difference grid has limited scalar reuse

**Meaning.** Choosing many adjacent outputs and an arithmetic run of
differences produces systematic coordinate reuse. The cubic spread still
forces enough scalar points that the prescribed pairs occupy a vanishing
fraction of the square.

**Precise statement — PROVED.** Let integers \(H,L\ge1\) and set

\[
Z=\{2b:0\le b<H\},\quad U=\{1,\ldots,L\},
\quad f(j)=\frac{j^3-j}{2},\quad g(j)=\frac{j^3+j}{2},
\]

\[
A_{H,L}=\{b-f(j),b-g(j):0\le b<H,\ 1\le j\le L\},\quad N=|A_{H,L}|.
\tag{3.1}
\]

All \(HL\) prescribed \((z,u)\) pairs are distinct and lie in \(A^2\),
organized into \(H\) chains of size \(L\). They use \(2HL\) scalar
coordinate occurrences. For every \(H,L\),

\[
HL\le4N^{4/3}.
\tag{3.2}
\]

For \(H=L^3\), the scalar set is exactly an integer interval and

\[
N=H+g(L)=\frac{3L^3+L}{2},\qquad HL=L^4=\Theta(N^{4/3}).
\tag{3.3}
\]

Thus the prescribed-pair/scalar ratio can grow like \(N^{1/3}\), but
the prescribed fraction of the whole square is only \(\Theta(N^{-2/3})\).

**Proof.** The inverse fiber formulas give exactly the two coordinates in
(3.1), so all prescribed pairs exist and their \((z,u)\) labels are unique.
Each \(j\) gives an integer interval of \(H\) consecutive values in the
first-coordinate set. Their ordered offsets satisfy

\[
f(j+1)-f(j)=\tfrac32j(j+1).
\]

Consequently their union has the exact size

\[
N_x=H+\sum_{j=1}^{L-1}\min\{H,\tfrac32j(j+1)\}\le N.
\tag{3.4}
\]

For \(L\ge2\), the largest \(\lfloor L/2\rfloor\ge L/3\) gaps
have indices \(j\ge\lceil L/2\rceil\), so each is at least
\(3L^2/8\ge L^2/3\). Thus

\[
N\ge H,\qquad N\ge\frac L3\min\{H,L^2/3\}.
\tag{3.5}
\]

If \(H\le L^2/3\), then \(HL\le3N\le3N^{4/3}\).
If \(H>L^2/3\), then \(L\le(9N)^{1/3}\), so
\(HL\le9^{1/3}N^{4/3}<4N^{4/3}\). For \(L=1\),
\(HL=H\le N\). This proves (3.2).

When \(H=L^3\), every gap in (3.4) is at most \(H\), and each
second-coordinate interval overlaps or is adjacent to its first-coordinate partner because
their displacement \(j\le L\le H\). Starting at the leftmost endpoint
\(-g(L)\), these overlapping intervals fill through \(H-1\). This
proves (3.3), including \(L=1\).

**Why it matters.** This is a genuine repeated-coordinate construction:
the number of prescribed pairs grows faster than the scalar count. Its
reuse is quantitatively insufficient for the required quadratic coverage.
In the maximizing regime it becomes an interval, whose *entire* actual
image is handled by the progression theorem; incidental pairs cannot
rescue it there.

**Scope.** Bound (3.2) concerns full rectangular grids of these consecutive
outputs and differences. It does not cover arbitrary correlated subsets
of the \((z,u)\) plane. For other \(H,L\), no actual-image lower bound
is inferred merely from the number of prescribed pairs.

## GS-P4. Faithful coefficient boxes: every nontrivial fiber is confined to one slice

**Meaning.** A box projected into very separated scalar places does reuse
coordinates heavily. But the cubic cross terms then record the differences
of the higher digits so faithfully that almost all ordered pairs have
unique outputs. The only surviving fibers come from one-dimensional
intervals inside individual slices.

**Precise statement — PROVED.** Fix an integer rank \(r\ge2\). For each
integer \(L\ge1\), choose \(B=100(L+1)^3\), and define

\[
w_0=1,\quad w_i=B^{4^{i-1}}\ (1\le i<r),\qquad
A_{r,L}=\left\{\sum_{i=0}^{r-1}a_iw_i:0\le a_i<L\right\}.
\tag{4.1}
\]

Then \(N=L^r\) exactly and

\[
\boxed{|P(A_{r,L},A_{r,L})|=N^2-L^{r-1}E_1(I_L),}
\qquad I_L=\{0,\ldots,L-1\}.
\tag{4.2}
\]

Every pair whose two inputs differ in any digit \(i\ge1\) has a
singleton actual output fiber. For pairs whose higher digits agree, all
collisions stay in that same higher-digit slice, and coincide exactly with
integer-interval collisions in their zeroth digits. Therefore the number
of pair vertices in non-singleton actual fibers is

\[
L^{r-1}\bigl(2E_1(I_L)-E_2(I_L)\bigr)
=\Theta_r(N^{1+1/(2r)})\quad(L\to\infty).
\tag{4.3}
\]

No inventory, regardless of its size, can connect the other vertices.

**Proof: faithful scalar encoding.** First work with indeterminates
\(t_1,\ldots,t_{r-1}\) and inputs
\(a=a_0+\sum a_it_i\), \(b=b_0+\sum b_it_i\).
All monomials of total degree at most three in the \(t_i\)'s acquire
distinct powers of \(B\) under \(t_i=B^{4^{i-1}}\), because each of
their exponent digits is between 0 and 3 in base four. In every output
polynomial, each coefficient has absolute value at most
\(6(L-1)^3+2(L-1)\). The difference of two such coefficients has
absolute value less than \(B\). If two scalar outputs agree, reducing
their difference modulo \(B\), and repeatedly dividing by \(B\),
forces every integer coefficient to vanish. This also proves input
injectivity. Thus scalar output equality is exactly formal polynomial
equality, with no omitted carries.

**Proof: recover a pair or locate its slice.** Put
\(d_0=a_0-b_0\), \(s_0=a_0+b_0\),
\(D=\sum_{i\ge1}(a_i-b_i)t_i\),
and \(Q=\sum_{i\ge1}(a_i+b_i)t_i\). Then

\[
P(a,b)=D^3+3d_0D^2+(3d_0^2D+Q)+(d_0^3+s_0),
\tag{4.4}
\]

displayed in homogeneous degrees three, two, one, and zero. If \(D\ne0\),
the cubic term determines the real linear polynomial \(D\) uniquely:
equality of its cubes implies equality at every real argument. The
quadratic term then determines \(d_0\), since \(D^2\ne0\). The linear
and constant terms determine \(Q,s_0\). All input digits follow from
their sums and differences, so the ordered pair is unique.

If \(D=0\), all higher input digits agree. The linear term \(Q\)
determines that common vector, since its coefficients are twice those
digits. Within that slice, equality reduces precisely to equality of
\(d_0^3+s_0=P(a_0,b_0)\). It cannot collide with a \(D\ne0\) output.
There are \(L^{r-1}\) such slices, each with \(L^2\) pairs and
\(|P(I_L,I_L)|=L^2-E_1(I_L)\) outputs by the new progression theorem.
The remaining \(N^2-L^{r+1}\) pairs are singleton fibers. Summing
proves (4.2), and the exact interval nonisolated count gives (4.3).

**Why it matters.** This is a structural classification of all actual
fibers in a family of coefficient boxes, not merely a failed graph upper
certificate. Large connected components force matching higher digits,
and their total available mass is subquadratic for every step inventory.

**Scope.** Rank is fixed before \(L\) grows; all heights and the varying
base are explicit. More generally the recovery argument holds for any
scalar projection faithful on these output polynomials. It does not cover
projections where cubic coefficient information merges, carriers with
correlated digits outside the full box, or arbitrary scalar real sets.
No historical digital no-go theorem is imported or reproved.

## GS-P5. Fixed rational diagonal completion fails at every depth

**Meaning.** Repeatedly adding the coordinates needed for selected diagonal
returns looks like an expanding closure process. With finitely many fixed
rational steps, it only builds a scalar set on one fixed lattice with
linearly growing width. The all-step lattice obstruction then applies.

**Precise statement — PROVED.** Fix a nonempty finite rational seed
\(A_0\) and a finite rational shift set \(C\) with at least two distinct
elements. Define \(A_{m+1}=A_m+C\), and \(N_m=|A_m|\). Then
\(N_m=\Theta(m+1)\), and

\[
|P(A_m,A_m)|=N_m^2-O_{A_0,C}(N_m^{3/2})\qquad(m\to\infty).
\tag{5.1}
\]

For every choice of step inventory at depth \(m\), the nonisolated pair
mass is \(O_{A_0,C}(N_m^{3/2})\).

**Proof.** Choose a common rational mesh \(h>0\) with
\(A_0,C\subset h\mathbb Z\). For fixed \(a\in A_0\) and two distinct
\(c_0,c_1\in C\), the \(m+1\) values
\(a+(m-j)c_0+jc_1\), \(0\le j\le m\), all lie in \(A_m\).
Thus \(N_m\ge m+1\). The diameter is exactly
\(D_m=\operatorname{diam}(A_0)+m\operatorname{diam}(C)\), and the common
lattice gives \(N_m\le D_m/h+1=O(m+1)\). In particular
\(D_m=O(N_m)\). Apply GS-U3 in [multistep-bounds.md](multistep-bounds.md)
with fixed \(h\): its nonsingleton-fiber bound is \(O(N_m^{3/2})\).
This proves the actual-image and all-inventory conclusions.

**Why it matters.** The finite experiment's two recursive levels use
\(A_0=\{j/3:0\le j<6\}\) and
\(C=\{0,-1,4/27,-5/27\}\). Indeed the two coordinates of
\(T_\tau(t,t)\) are \(t+(\tau-\tau^3)/2\) and
\(t-(\tau+\tau^3)/2\); steps \(1,1/3\), together with retention of
\(t\), give exactly this \(C\). Equation (5.1) rules out a later
asymptotic rescue for this tested recursion, even by adding all possible
collision steps to its graph.

**Scope.** The seed and rational shift inventory are fixed before depth
grows. This is an actual-image theorem for additive completion of this
form. It does not cover nonlinear completion of general off-diagonal
pairs, changing shifts, changing denominators, or arbitrary recursive
carriers. No claim is based only on the two observed finite levels.
