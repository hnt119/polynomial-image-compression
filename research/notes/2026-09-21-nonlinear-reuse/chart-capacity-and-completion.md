# Nonlinear charts: reuse, independent output grids, and completion

T01 / nonlinear coordinate reuse, 2026-09-21 v1.
Fixed polynomial \(P(x,y)=(x-y)^3+x+y\).
Internal elementary proofs; no external result or novelty claim.

## NR-A1 — Three counts and the exact completion charge

**Meaning.** A nonlinear relabeling can describe every pair without changing
any output. For example, on \(A=\{0,1,4\}\), the labels
\(x=r^2,\ y=((s+r^2)\bmod3)^2\), \(0\le r,s<3\), run through all
nine ordered pairs. This supplies scalar reuse, but does not change
\(P(A,A)\). Repeated descriptions can also inflate the parameter count.

**Exact statement — PROVED.** For a finite parameter set \(T\) and a map
\(\psi:T\to\mathbb R^2\), put
\[
Q_0=|T|,\quad E=\psi(T),\quad Q=|E|,\quad
A=\pi_1(E)\cup\pi_2(E),\quad N=|A|,\quad Z=|P(E)|.
\]
The label multiplicities sum to \(Q_0\). Counting both positions of
each *distinct* pair gives exactly \(2Q\) scalar occurrences, with
average reuse \(2Q/N\). Always
\[
\boxed{|P(A,A)|\le Z+(N^2-Q),\qquad Q\le NZ.} \tag{A1}
\]
Every fixed output fiber has at most \(N\) ordered pairs. Relabeling
without changing \(E\) changes none of these sets or counts.

**Proof.** Split \(A^2\) into \(E\) and its complement; each complement
pair contributes at most one new output. For fixed \(y\), the derivative
of \(P(x,y)\) in \(x\) is \(3(x-y)^2+1>0\), so a fiber has at most
one pair for each second coordinate. Sum over the selected outputs.
The occurrence identities and relabeling invariance follow by counting.

**Why it matters.** Quadratically many distinct pairs on \(N\) scalars
alone are automatic for the full square. Output compression and the
complement remain essential. Even the exponential-rate equality \(q=2a\)
is insufficient: \(Q=N^2/2\) has that rate but leaves half the square.
The safe certificate requires \(N^2-Q=O(N^{2-\delta})\), as well as
\(Z=O(N^{2-\varepsilon})\), unless another bound controls the complement.

**Scope.** Exact bookkeeping and the elementary fiber principle, not a
new construction. Formal projection multiplicities are not input sizes.

## NR-A2 — A bounded rational curve library is too sparse

**Meaning.** A rational coordinate of fixed degree takes a prescribed
scalar value only a bounded number of times. For example,
\(t\mapsto(t^2,t^2+t)\) has at most two parameters above each first
coordinate.

**Exact statement — PROVED.** Let \(|A|=N\). For \(J\) rational maps
\(t\mapsto(f_j(t),g_j(t))\), away from their poles, assume every
nonconstant coordinate has reduced numerator and denominator degrees
at most \(d\ge1\). The union of distinct image pairs inside \(A^2\)
has size
\[
\boxed{Q\le dJN.} \tag{A2}
\]
Likewise \(J\) charts
\((x,y)=(f(\Phi(r,s)),g(\Phi(r,s)))\), with univariate
\(\deg f,\deg g\le2\) and arbitrary \(\Phi\), supply at most \(2JN\)
distinct pairs.

**Proof.** If \(f_j\) is nonconstant, \(f_j(t)=a\) has at most \(d\)
solutions after clearing its reduced denominator. Sum over \(a\in A\).
If \(f_j\) is constant, the chart has at most \(N\) distinct pairs.
Sum over charts. For the second assertion apply the same root count to
\(w=\Phi(r,s)\); repeated labels with the same \(w\) add no pair.

**Why it matters.** Fixed-degree, bounded or subpolynomially many
one-parameter charts cover only \(o(N^2)\). Near-full coverage requires
\(dJ\ge(1-o(1))N\), so a growing library must be charged.

**Scope.** This is a chart-capacity obstruction, not an actual-image
lower bound for arbitrary scalar sets. It does not apply to genuine
two-dimensional rational maps or arbitrary discrete permutations.

## NR-P1 — Genuine nonlinear cross-output reuse and its exact rate

**Meaning.** Two different fibers can share their first coordinate by a
nonlinear rational identity. Yet the required scalar pool grows linearly
with the useful pair count, so this does not produce dense Cartesian reuse.

**Exact statement — PROVED.** Put \(a=1/\sqrt3,\ z=0,\ w=4a/3\).
For \(t>1\) define
\[
U(t)=1+\frac{3(1+t^2)}{t^3-1},\qquad
V(t)=-1+\frac{3t(1+t^2)}{t^3-1},\qquad
u=aU,\quad v=aV. \tag{P1}
\]
Then \(x_z(u)=x_w(v)\). For integers \(m\ge1\), on \(T_m=\{2,\ldots,m+1\}\), take both
pairs \((x_z(u),y_z(u))\) and \((x_w(v),y_w(v))\), and let \(A_m\)
be their scalar union. Then
\[
Q_0=Q=2m,\qquad m\le N=|A_m|\le3m,\qquad |P(E_m)|=2,
\quad \frac{Q}{N^2}\le\frac2m. \tag{P2}
\]
Their \(4m\) scalar occurrences have average reuse between \(4/3\) and 4.

**Proof.** In the curve \(u^3-u-v^3+v=-4a/3\), substitute
\(u=a+h,\ v=-a+th\). Subtracting the value at \((a,-a)\) gives
\[
h^2\bigl(3a(1+t^2)+(1-t^3)h\bigr).
\]
Taking \(h=3a(1+t^2)/(t^3-1)\) proves the identity and shared coordinate.
Both \(U,V\) strictly decrease for \(t>1\): their derivatives have
numerators respectively \(-3(t^4+3t^2+2t)\) and
\(-3(2t^3+3t^2+1)\), with denominator \((t^3-1)^2\).
Thus each output has \(m\) distinct differences and hence distinct pairs.
The outputs differ, so \(Q=2m\). The function
\(y_z(u)=-(u^3+u)/2\) is strictly decreasing, giving \(N\ge m\).
The common first coordinate leaves at most three scalars per parameter,
giving \(N\le3m\).

**Why it matters.** This escapes SC-R2/R3: the relation is not affine,
and it shares one coordinate, not the two endpoints of a fixed-step edge.
The companion classifies this exceptional cubic among the only
nonconstant rational fixed-output possibilities.
Using depth \(\log m\), the distinct-pair, scalar and selected-output
rates are \(q=1,\ a_{\rm input}=1,\ b_{\rm selected}=0\).
The full certificate is only
\[
|P(A_m,A_m)|\le2+N^2-2m=N^2-\Theta(N). \tag{P3}
\]
Here the right side has a linear saving; the display does not determine
the actual full-image asymptotic.

**Scope.** FAILED prescribed-coverage family: \(Q=o(N^2)\).
The actual full image remains unclassified here. A growing overlapping
library of output charts would need a separate scalar-reuse and complement
proof. The stop rule rejects this sparse family without an expanding search.

## NR-G1 — An independent scalar/output grid has no rational completion

**Meaning.** Choosing a first scalar freely from one parameter and an
output freely from another does not admit a rational formula for the second
scalar. A polynomial parametrization of one fixed output fiber does not
supply this independent two-parameter grid.

**Exact statement — PROVED.** If \(X(r),Z(s)\) are nonconstant real
rational functions, no real rational \(Y(r,s)\) satisfies either identity
\[
P(X(r),Y(r,s))=Z(s),\qquad P(Y(r,s),X(r))=Z(s). \tag{G1}
\]
There is no degree restriction.

**Proof.** Use NR-C2 in
[rational-reuse-curves](rational-reuse-curves.md), proved there by an
elementary rational-differential argument. First-coordinate templates
at fixed outputs can share a nonconstant rational parameter only when
the output difference is \(0,\pm4/(3\sqrt3)\). Second-coordinate
templates cannot share such a parameter at distinct outputs.

Suppose the first identity holds. Except for finitely many \(s\),
the denominator of \(Y(r,s)\) does not specialize to the zero polynomial
in \(r\), and \(Z(s)\) is finite. Choose two allowed specializations
\(s_1,s_2\) whose output difference avoids those three values. This is
possible because a nonconstant rational function has infinite real image.
The rational functions \(u_i(r)=X(r)-Y(r,s_i)\) must be nonconstant:
otherwise \(Z(s_i)=u_i^3-u_i+2X(r)\) would vary with \(r\).
But
\[
x_{Z(s_1)}(u_1(r))=X(r)=x_{Z(s_2)}(u_2(r))
\]
contradicts NR-C2. For the second orientation, put
\(u_i=Y(r,s_i)-X(r)\) and use the second-coordinate templates;
only distinct outputs are needed.

**Why it matters.** This excludes a broad rational nonlinear completion
ansatz of arbitrary degree, beyond affine matching and quadratic maps.

**Scope.** It does not exclude arbitrary rational two-parameter pair maps,
nor assert that small finite output support forces (G1). Both \(X,Z\)
must be nonconstant. Correlated parameter subsets and nonrational algebraic
inverse branches remain outside the theorem.

## NR-G2 — The bounded-degree finite-grid consequence

**Meaning.** The failed rational identity also limits isolated exact
equalities on a large parameter rectangle.

**Exact statement — PROVED.** In NR-G1, assume all numerators and
denominators have total degree at most \(d\ge1\). For finite real
\(R,S\), for each chosen orientation separately, the number of denominator-defined
labels satisfying its equation is at most
\[
\boxed{7d\max\{|R|,|S|\}.} \tag{G2}
\]
Thus an \(m\times m\) grid has only \(O_d(m)\) working labels.

**Proof.** Write \(X=A/B,\ Y=C/D,\ Z=E/G\). Clear
\((BD)^3G\). For the first orientation the numerator is
\[
H=(AD-BC)^3G+(AD+BC)(BD)^2G-E(BD)^3. \tag{G3}
\]
For the other orientation reverse the difference numerator.
Its total degree is at most \(7d\), and NR-G1 proves \(H\ne0\).

A nonzero polynomial of total degree at most \(k\) has at most
\(k\max(|R|,|S|)\) zeros on \(R\times S\). Indeed, write its degree
in \(s\) as \(j\). The nonzero leading coefficient in \(r\) has degree
at most \(k-j\); charge all \(|S|\) points in those at most \(k-j\)
exceptional rows, and at most \(j\) roots in every other row. The bound
\((k-j)|S|+j|R|\le k\max(|R|,|S|)\) follows.
Apply it to \(H\); removing poles only decreases the count.

**Why it matters.** A union of \(J\) such comparable \(m\times m\)
charts has at most \(7dJm\) working labels, before deduplication.
Fixed \(d\) and subpolynomial \(J\) cannot supply quadratic coverage
within this model.

**Scope.** The independently prescribed coordinates are one scalar and
the output, not the two original scalar inputs. No theorem that all
compressed finite sets have this form is assumed. Parameter multiplicities
can only reduce the number of actual pairs.

## Provenance

All NR-A1/A2/P1/G1/G2 claims concern T01's fixed plus-sign cubic,
date/version 2026-09-21 v1. Quantifiers and hypotheses appear above;
evidence is the complete proof in each named section. NR-A1 restates the
frozen completion/fiber principles in the current notation. NR-G1/G2
depend on NR-C2, not an imported genus theorem or internet result.
An independent proof agent audited NR-A1/A2/P1/G1/G2 in full; the orientation
wording in NR-G2 was clarified without changing the intended theorem.
Finite checks and the audit scope are recorded separately in verification.
The general near-full direct-support witness remains OPEN.

