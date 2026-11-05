# Exact fibers, return paths, and scalar-coordinate reuse

Date: 2026-09-21. Track T01, fixed polynomial
\(P(x,y)=(x-y)^3+x+y\). All sets below are nonempty finite subsets of \(\mathbb R\).
This is a new offline proof-search companion, not part of the earlier freeze.

## CR-P1. The symmetry is translation along a fiber — PROVED

**Meaning.** The map changes the difference of a pair while holding its
output fixed. In the right coordinates, there is no nonlinear iteration
to solve.

**Statement and proof.** Put \(u=x-y\), \(z=P(x,y)\). The map
\(\Phi(x,y)=(u,z)\) is a bijection \(\mathbb R^2\to\mathbb R^2\), with inverse

\[
x_z(u)=\frac{z-u^3+u}{2},\qquad
y_z(u)=\frac{z-u^3-u}{2}.
\]

Substitution gives both \(x_z(u)-y_z(u)=u\) and
\(P(x_z(u),y_z(u))=z\). Consequently

\[
T_\tau=\Phi^{-1}\circ[(u,z)\mapsto(u+\tau,z)]\circ\Phi.
\]

Writing \(H_\tau(u)=(u+\tau)^3-u^3\) recovers exactly

\[
T_\tau(x,y)=\left(x+\frac{\tau-H_\tau(u)}2,
                     y-\frac{\tau+H_\tau(u)}2\right).
\]

Thus \(P\circ T_\tau=P\), \(T_\sigma T_\tau=T_{\sigma+\tau}\), and
\(T_\tau^{-1}=T_{-\tau}\). In particular this formula with \(\tau=k\)
is the explicit formula for every iterate \(T_1^k\).

**Scope.** The algebraic symmetry and group law were already proved in
the 16 September continuation; this proof rederives them in coordinates.
It does not establish returns to a Cartesian set.

## CR-P2. Two exact formulas for the return count — PROVED

**Meaning.** Each cubic output has a finite set of allowed differences.
A return is precisely a pair of allowed differences separated by one.

**Statement.** For \(N=|A|\), define

\[
U_A(z)=\{u:x_z(u)\in A,\ y_z(u)\in A\}.
\]

Then, with sums taken over the finitely many nonempty fibers,

\[
|U_A(z)|=|\{(x,y)\in A^2:P(x,y)=z\}|,\quad
\sum_z|U_A(z)|=N^2,\quad
|P(A,A)|=|\{z:U_A(z)\ne\varnothing\}|.
\]

For \(E_\tau(A)=|\{v\in A^2:T_\tau(v)\in A^2\}|\),

\[
E_\tau(A)=\sum_z|U_A(z)\cap(U_A(z)-\tau)|.
\tag{2.1}
\]

In the original coordinates put \(A_u=A\cap(A-u)\) and
\(c(u)=(3u^2+3u+2)/2\). Then

\[
E_1(A)=\sum_{u\in A-A}|A_u\cap(A_{u+1}+c(u))|.
\tag{2.2}
\]

**Proof.** The inverse of \(\Phi\) gives the bijection in the first
display. Translation of \(u\) proves (2.1), counting each source pair
exactly once. Write a source pair as \((y+u,y)\), where \(y\in A_u\).
Direct substitution gives

\[
T_1(y+u,y)=\left(y-\frac{3u^2+u}{2},\ y-c(u)\right).
\]

The first transformed coordinate is \(y-c(u)+u+1\). Both belong to
\(A\) precisely when \(y-c(u)\in A_{u+1}\), proving (2.2).

**Scope.** These are exact support and edge counts, without an energy-to-
support inference. Large slices must align at their particular quadratic
translations simultaneously inside the same scalar set.

## CR-P3. The graph is a disjoint union of paths — PROVED

**Meaning.** Consecutive returns organize some pairs into chains. A whole
cubic fiber can contain several chains, with gaps or different residues
of the difference modulo one.

**Statement.** Direct an edge \(v\to T_1v\) whenever both ends lie in
\(A^2\). Let \(n_\ell\) be the number of components containing exactly
\(\ell\) vertices, including isolated vertices. Then

\[
\sum_{\ell\ge1}\ell n_\ell=N^2,\quad
E_1(A)=\sum_{\ell\ge1}(\ell-1)n_\ell,\quad
C_A:=\sum_{\ell\ge1}n_\ell=N^2-E_1(A).
\tag{3.1}
\]

Every component has one cubic output, so

\[
|P(A,A)|\le C_A.
\tag{3.2}
\]

There is no reverse inequality without controlling different components
with the same output. If \(L_A(v)\) counts consecutive forward edges
starting at \(v\), then

\[
\max_vL_A(v)=\max\{\ell:n_\ell>0\}-1,
\qquad
\frac1{N^2}\sum_vL_A(v)
=\frac1{2N^2}\sum_\ell\ell(\ell-1)n_\ell.
\tag{3.3}
\]

For every integer \(K\ge2\), the number \(W_K\) of vertices in
components of size at least \(K\) satisfies

\[
W_K\le\frac K{K-1}E_1(A)\le2E_1(A).
\tag{3.4}
\]

**Proof.** The map is a function and is invertible, so in- and out-degree
are at most one. Along any directed edge the real difference increases
by one. Cycles are impossible. A finite graph with these degree bounds
and no directed cycle consists of directed paths. A path of \(\ell\)
vertices has \(\ell-1\) edges and forward lengths
\(0,1,\ldots,\ell-1\), proving (3.1) and (3.3). Equation (3.2)
follows by mapping components onto their outputs. For (3.4), each long
path contributes at least \((1-1/K)\ell\) edges.

Also

\[
y_z(u+1)-y_z(u)=-c(u),\qquad
c(u)=\tfrac32(u+\tfrac12)^2+\tfrac58>0.
\]

Thus each path has distinct second coordinates, and has at most \(N\)
vertices. More generally \(y_z'(u)=-(3u^2+1)/2<0\), so every actual
cubic fiber has size at most \(N\). These facts do not force fibers to
be paths. Finally (3.3) gives
\(N^{-2}\sum_v L_A(v)\le E_1(A)/(2N)\).

**Scope.** Positive edge density alone bounds the number of components
by a constant multiple of \(N^2\). Small edge density does not prove
a large actual cubic image. Even though almost every vertex may be
isolated in this graph, many isolated vertices could share one output.

## CR-P4. Long-path coverage would suffice, but is impossible here — PROVED

**Meaning.** To use chains as the image certificate, almost all ordered
pairs must lie in long chains. Counting the exceptional pairs is necessary.

**Statement and proof of the implication.** Suppose for fixed
\(\varepsilon,\delta>0\), all but \(B\le D N^{2-\delta}\) pairs
lie in components with at least \(K=\lceil N^\varepsilon\rceil\)
vertices. There are at most \(N^2/K\) such components. The remaining
components number at most \(B\), since each contains at least one
exceptional pair. Therefore

\[
|P(A,A)|\le C_A\le N^2/K+B
\le(1+D)N^{2-\min(\varepsilon,\delta)}.
\tag{4.1}
\]

The same implication holds if coverage is initially stated using
overlapping consecutive orbit segments: each segment lies in one
maximal component, which is at least as large.

**Obstruction.** CR-U1 in [universal-bounds.md](universal-bounds.md)
proves \(E_1(A)\le5N^{11/6}\). Hence (3.4) gives

\[
W_K\le10N^{11/6}=o(N^2)\quad(K\ge2).
\tag{4.2}
\]

For large \(N\), this contradicts even positive-density coverage by
nontrivial paths, and therefore contradicts the hypothesis of (4.1).
Moreover \(C_A\ge N^2-5N^{11/6}\). The average component size
\(N^2/C_A\) tends to one. The average *forward length* is a different
quantity and need not tend to zero; the bound proved above is only
\(\frac52N^{5/6}\). In particular we do not confuse an average over
components with an average over vertices.

**Scope.** The coverage implication is a proved implication whose
\(T_1\) hypothesis is now disproved asymptotically. The cubic target
remains OPEN because it allows coincidences between different paths.

## CR-P5. Polynomial-length chains exist on sparse pair sets — PROVED

**Meaning.** Creating one long chain is easy. Creating enough chains
without spending new scalar coordinates on each one is the real cost.

**Statement.** For an integer \(L\ge1\), fix \(z\in\mathbb R\) and set

\[
A_L(z)=\{x_z(j),y_z(j):1\le j\le L\}.
\]

This set has exactly \(2L\) elements and contains \(L\) consecutive
pairs of the fiber \(z\), hence a path segment of size \(L=N/2\).
It gives \(E_1\ge L-1\), but its engineered pairs occupy only
\(L/(2L)^2=1/(2N)\) of its full Cartesian square.

**Proof.** For \(j\ge1\),

\[
x_z(j)-y_z(j)=j>0,\qquad
y_z(j)-x_z(j+1)=\frac{3j^2+j}{2}>0.
\]

Thus the displayed \(2L\) scalar values strictly interleave, with no
projection multiplicity. Consecutive pairs are related by \(T_1\).
The coverage fraction counts just these prescribed pairs, not any
incidental ones.

For \(M\) fibers an explicit two-parameter version is available. Put
\(D=L^3+L+1\), \(z_m=2mD\) for \(0\le m<M\), and
\(A_{M,L}=\bigcup_m A_L(z_m)\). Each block lies in
\([mD-(L^3+L)/2,mD]\), so blocks are disjoint. Consequently

\[
|A_{M,L}|=2ML,\qquad \text{prescribed pairs}=ML=N/2,
\qquad \text{prescribed edges}=M(L-1).
\]

Every prescribed four-point return is realized in one actual common set.
The bound on all edges in CR-U1 nevertheless applies, including incidental
returns across blocks. It rules out repairing coverage by scalar reuse
so effectively that a positive proportion of pairs have a common fixed
nonzero step. This applies also to recursive completion of selected
returns: at every finite stage its actual distinct scalar set obeys the
same theorem, irrespective of its parameter count.

**Scope.** Linear-size maximum chains are possible. They are not evidence
of large pair-mass coverage or a full-image power saving. No lower bound
for the actual image of these particular orbit carriers is claimed.

## CR-P6. Several shifts and the remaining mechanism — PROVED

**Meaning.** Changing the step does not remove the obstruction. A growing
inventory of different steps is necessary before these symmetries could
connect most pairs.

**Statement and proof.** Let \(S\subset\mathbb R\setminus\{0\}\)
have size \(M\), and join pairs whenever one is \(T_\tau\) of the
other for some \(\tau\in S\). Count undirected edges only once.
The uniform CR-U1 bound, including when steps depend on \(A\), gives

\[
e(G_{A,S})\le\sum_{\tau\in S}E_\tau(A)
\le5M N^{11/6}.
\]

Thus at most \(10M N^{11/6}\) vertices are nonisolated. The number
of components is at least \(N^2-5M N^{11/6}\), by deleting cycles
to form a spanning forest. If \(M=o(N^{1/6})\), almost every pair is
isolated. If these components number \(O(N^{2-c})\) for a fixed
\(c>0\), necessarily

\[
M\ge(1/5-o(1))N^{1/6}.
\tag{6.1}
\]

All components still have constant \(P\)-value. Formula (4.1) applies
to their sizes as well; paths are no longer needed for that counting
implication. This supplies a precise test for a growing-step proposal.

**Scope.** Every fixed nonzero real step, including a rational or
algebraic choice, and every fixed finite inventory are closed as
positive-density return mechanisms. Inventories of order at least
\(N^{1/6}\), or unbounded pair-dependent steps, are not closed by
this estimate. Neither are output coincidences among its components.
