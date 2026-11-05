# Rational curves for sharing cubic scalar coordinates

T01 / nonlinear coordinate reuse, 2026-09-21 v1.
The fixed polynomial is \(P(x,y)=(x-y)^3+x+y\).
These are new internal symbolic proofs for the authorized offline cycle.
No experiment, external theorem, network source, or novelty claim is used.
Independent internal lead audit of NR-C1–C4 is complete; the cycle's
verification record gives its scope. No external review is claimed.

For example, two different parameters \(u,v\) give the same first
coordinate in one output fiber whenever \(u^2+uv+v^2=1\).
This ellipse has a rational parametrization. The classification below
determines exactly when a rational family can share a scalar coordinate
between two fixed output fibers.

Write
\[
c_s(z,u)=\frac{z-u^3+su}{2},\qquad s\in\{+1,-1\}.
\]
Thus \(c_+=x_z\) and \(c_-=y_z\). For fixed real outputs \(z,w\),
\[
c_s(z,u)=c_t(w,v)
\quad\Longleftrightarrow\quad
F_{s,t,c}(u,v):=u^3-v^3-su+tv-c=0,\qquad c=z-w.
\tag{1}
\]
Here a nonconstant rational parametrization means rational functions
\(U,V\in\mathbb R(r)\), at least one nonconstant, satisfying (1) as
an identity. It does not mean arbitrary algebraic or real analytic
functions, or merely a finite list of points on the curve.

## 1. NR-C1 — polynomial parametrizations only give the diagonal

### Meaning

Allowing nonlinear polynomial matching does not produce a new identity
between two fixed coordinate templates. The cubic leading terms force the
parameters to be identical. This holds in every degree, not just degree two.

### Exact statement — PROVED

Let \(k\ge1\), let \(U,V\in\mathbb R[r_1,\ldots,r_k]\), and suppose
\[
U^3-V^3-sU+tV-c=0
\tag{2}
\]
identically, for \(s,t\in\{+1,-1\}\) and \(c\in\mathbb R\).
If at least one of \(U,V\) is nonconstant, then necessarily
\[
\boxed{U=V,\qquad s=t,\qquad c=0.}
\tag{3}
\]
Conversely these conditions allow every polynomial choice of \(U=V\).

### Proof

If only one function is nonconstant, its cubic term has strictly greater
total degree than the remaining terms, a contradiction. Leading-degree
comparison also shows that both have the same degree \(n\ge1\).
Their degree-\(n\) homogeneous parts have equal cubes and hence are equal:
evaluate at every real point and use injectivity of the real cube map.

Suppose \(H=U-V\ne0\), with degree \(m<n\). Then
\[
U^3-V^3=H(U^2+UV+V^2)
\]
has degree \(m+2n\): the quadratic factor has leading homogeneous part
three times the square of the common leading part. But (2) says that this
equals \(sU-tV+c\), of degree at most \(n\). Since \(m+2n>n\),
this is impossible. Thus \(U=V\), and (2) reduces to
\((t-s)U-c=0\). Nonconstancy gives (3); the converse is immediate.
\(\square\)

### Why it matters

This extends the frozen affine-template restriction SC-R2 to every real
polynomial degree and any finite number of parameters, within identity (1).

### Scope

The outputs are fixed and the equality is an identity. The theorem does
not bound isolated coincidences on a finite grid, or classify models in
which \(z-w\) also varies with the parameters.

## 2. NR-C2 — the complete list of rationally parametrizable cases

### Meaning

Rational functions do allow genuinely nonlinear sharing. Outside explicit
first-coordinate exceptions, however, even arbitrary-degree rational
functions cannot trace a nonconstant family. The obstruction is an
elementary calculation of zeros and poles; no genus theorem is needed.

### Exact statement — PROVED

Set \(a=1/\sqrt3\). A nonconstant pair \(U,V\in\mathbb R(r)\)
satisfying (1) exists exactly in these cases:

| Coordinate signs and output difference | Possible nonconstant image |
|---|---|
| \(s=t=-1,\ c=0\) | The diagonal \(u=v\) only |
| \(s=t=+1,\ c=0\) | The diagonal or the ellipse \(u^2+uv+v^2=1\) |
| \(s=t=+1,\ c=\pm4/(3\sqrt3)\) | The corresponding singular cubic, with the charts in NR-C3 |
| All other real \((s,t,c)\) | No nonconstant real rational parametrization |

Constant solutions are not excluded. In particular, neither mixed-sign
sharing equation admits a nonconstant rational parametrization at any
fixed real output difference.

### Proof: locate every complex singularity

Complex parameters must be checked because a rational differential can
have a pole at a nonreal parameter value. A finite singular point satisfies
\[
F_u=3u^2-s=0,\qquad F_v=-3v^2+t=0.
\]
At such a point,
\[
c=\frac23(tv-su).
\tag{4}
\]
For \(s=t=+1\), we have \(u,v\in\{a,-a\}\), giving
\(c=0,\pm4a/3\). For \(s=t=-1\), we have
\(u,v\in\{ia,-ia\}\), giving \(c=0,\pm4ia/3\); only zero is real.
For opposite signs, one of \(u,v\) is real and the other purely imaginary
and nonzero. Formula (4) then has nonzero imaginary part.

There are no singular points at infinity. The homogeneous equation is
\[
H(U,V,Z)=U^3-V^3-sUZ^2+tVZ^2-cZ^3=0.
\]
At \(Z=0\), \(U^3=V^3\) and both \(U,V\ne0\), whereas
\(H_U=3U^2\) and \(H_V=-3V^2\) are nonzero. Outside the listed
exceptional real \(c\)'s, the entire projective curve has no complex
singular point.

### Proof: an elementary differential obstruction in every smooth case

Suppose nonconstant rational functions \(U(r),V(r)\) satisfy (1) in a
case with no complex singularity. Both functions are nonconstant: if one
were constant, the other would satisfy a constant-coefficient cubic and
would also be constant. Consider the rational differential
\[
\omega=\frac{dU}{t-3V^2}.
\tag{5}
\]
The denominator is not identically zero, because that would make \(V\)
constant. The numerator is nonzero because a nonconstant rational function
has nonzero derivative in characteristic zero. Thus \(\omega\ne0\).

Check every parameter value, including nonreal values and infinity.
Use a local coordinate \(q\) centered there; at infinity take \(q=1/r\).

If \(U,V\) are both finite and \(F_v=t-3V^2\ne0\), (5) has no pole.
If \(F_v=0\), smoothness gives \(F_u=3U^2-s\ne0\). Differentiating
(1) gives
\[
\omega=-\frac{dV}{3U^2-s},
\]
which again has no pole. This includes parameter values where derivatives
vanish.

If one of \(U,V\) has a pole, both do, with the same order. Otherwise
the cubic term with the largest pole could not cancel in (1). Write
\[
U=Aq^{-n}+\cdots,\qquad V=Bq^{-n}+\cdots,
\qquad n\ge1,\quad A,B\ne0,\quad A^3=B^3.
\]
Then
\[
dU=(-nAq^{-n-1}+\cdots)dq,\qquad
t-3V^2=-3B^2q^{-2n}+\cdots.
\]
Therefore \(\omega\) has order \(n-1\ge0\), so no pole.

This gives a nonzero rational differential with no pole anywhere on the
complex parameter line, including infinity. To see the contradiction
elementarily, write it as \(f(r)\,dr\). No finite pole implies that the
reduced denominator of \(f\) has no complex root, so \(f\) is a polynomial.
If its degree is \(d\ge0\), then
\[
f(r)\,dr=-f(1/q)q^{-2}\,dq
\]
has a pole of order \(d+2\) at infinity. This contradiction excludes every
smooth case without importing a theorem about the genus of a curve.

### Proof: the remaining zero-difference cases

For \(s=t\) and \(c=0\),
\[
F_{s,s,0}(u,v)=(u-v)(u^2+uv+v^2-s).
\tag{6}
\]
The rational function field is an integral domain, so a rational identity
lies entirely in one factor. For \(s=-1\), the second factor is strictly
positive at every real \(u,v\), because \(u^2+uv+v^2\ge0\). It cannot
vanish identically for real rational functions, which are real and defined
away from finitely many real poles. Only the diagonal remains.
For \(s=+1\), the second factor is the stated ellipse. Its chart, and
those for the two remaining singular cubics, are given in NR-C3. These
prove existence in every listed case. \(\square\)

### Why it matters

This treats rational maps of every degree. In particular, fixed-output
mixed first/second-coordinate sharing, and distinct-output second/second
sharing, cannot be supplied by a rational curve. First/first sharing has
exceptions that must be counted rather than excluded by a broad rigidity
claim.

### Scope

This is a rational-identity theorem, not a real-point bound. Every curve
in (1) has infinitely many real points: for each real \(u\), the equation
in \(v\) has odd degree and a real root. Nonrational algebraic branches
and finite selected correspondences are outside the obstruction.
NR-C2 alone gives no bound for \(|P(A,A)|\).

## 3. NR-C3 — exceptional charts and their exact real domains

### Meaning

There are genuine nonlinear coincidences to work with. These formulas
describe all rationally traceable exceptions and identify the extra point
omitted by a real line-slope chart. They do not yet supply a small common
scalar carrier or cover its Cartesian square.

### Exact statement — PROVED

For the same-output first-coordinate ellipse, put
\[
U(r)=\frac{r^2-1}{r^2+r+1},\qquad
V(r)=-\frac{r(r+2)}{r^2+r+1}.
\tag{7}
\]
Then \(U^2+UV+V^2=1\), so \(x_z(U(r))=x_z(V(r))\) for every
fixed real \(z\). The denominator is positive for real \(r\).
Together with \(r=\infty\), giving \((U,V)=(1,-1)\), this covers
the whole real ellipse. At \(r=-2\) it gives \((1,0)\).

For \(b\in\{a,-a\}\), set \(c=-4b/3\) and put
\[
h(r)=-\frac{3b(1+r^2)}{1-r^3},\qquad
U(r)=b+h(r),\qquad V(r)=-b+rh(r).
\tag{8}
\]
For real \(r\ne1\),
\[
U(r)^3-V(r)^3-U(r)+V(r)=c.
\tag{9}
\]
Hence (8) shares a first coordinate between fixed outputs with \(z-w=c\).
The real affine curve consists of:

- the points (8) for \(r\in\mathbb R\setminus\{1\}\);
- the point \((b,2b)\), obtained at \(r=\infty\);
- the isolated singular point \((b,-b)\), not attained by any real
  parameter of this rational chart.

Every nonconstant real rational parametrization of an exceptional conic
or cubic is a rational substitution \(r=R(q)\) into (7) or (8),
respectively. Diagonal parametrizations are \(U=V=R(q)\).

### Proof

For the ellipse, use the line \(v=r(u-1)\) through \((1,0)\)
and put \(h=u-1\). Its equation becomes
\[
h\bigl(2+r+(1+r+r^2)h\bigr)=0.
\]
The second intersection is (7); at the tangent slope \(r=-2\)
it coincides with the base point. The vertical line has second intersection
\((1,-1)\), the limit at \(r=\infty\). Every other point determines
its finite slope uniquely, proving coverage.

For the singular cubic, \((b,-b)\) lies on (9) since \(b^2=1/3\).
Substituting \(u=b+h,\ v=-b+k\) gives exactly
\[
3b(h^2+k^2)+h^3-k^3=0.
\tag{10}
\]
On \(k=rh\), this is
\[
h^2\bigl(3b(1+r^2)+(1-r^3)h\bigr)=0.
\]
The third intersection is (8). For real \(r\ne1\), its numerator
\(1+r^2\) is nonzero, so the point is not the singular point.
At \(r=1\), the remaining factor has no zero; the third intersection
is at infinity, giving a genuine pole rather than an omitted finite point.
At \(r=\infty\), \(h\to0,\ rh\to3b\), giving \((b,2b)\).
On the vertical line \(u=b\), (10) gives just \((b,-b)\) and
\((b,2b)\). Every other point determines a finite slope and is covered.

The singular point is isolated in the real locus. In (10),
\[
|h^3-k^3|\le\max\{|h|,|k|\}(h^2+k^2).
\]
If \(\max\{|h|,|k|\}<3|b|\), equality (10) forces \(h=k=0\).
Its complex tangent slopes are \(r=\pm i\). Calling it a double
point therefore must not suggest crossing real branches.

Finally, a nonconstant rational map into the ellipse cannot have
\(U\equiv1\), which would give the constant alternatives \(V=0,-1\).
Set \(R=V/(U-1)\); the line factorization gives (7) with \(r=R\).
A nonconstant map into (9) likewise cannot have \(U\equiv b\).
Set \(R=(V+b)/(U-b)\), and the factorization of (10) gives (8).
In both cases \(R\) is nonconstant, since a fixed slope has only
finitely many intersection points. This proves the factorization of all
nonconstant rational maps. \(\square\)

### Why it matters

Formula (8) escapes SC-R2 because its nonconstant image is not a line.
It also imposes no common translated second-coordinate edge as required
by SC-R3. This is an exact nonlinear identity, but not evidence of
favorable completion rates.

For instance, \(r=0\) gives \((U,V)=(-2b,-b)\), and
\(U^3-V^3-U+V=-4b/3\). The identity holds for every admissible
parameter, not merely this example.

### Scope

The ellipse stays within one output fiber. The cubic permits only output
separation \(\pm4/(3\sqrt3)\). Its isolated point is one extra coincidence,
not a rational family. Scalar reuse across many charts, projection
multiplicities, actual input count, and every unprescribed Cartesian pair
still need separate estimates.

## 4. NR-C4 — more rational parameters add no fixed-output cases

### Meaning

A second or third rational parameter cannot avoid the classification
while the output labels remain fixed. A nonconstant family can always
be examined along one parameter line.

### Exact statement — PROVED

Let \(k\ge1\) and \(U,V\in\mathbb R(r_1,\ldots,r_k)\) satisfy (2),
with at least one nonconstant. Then \((s,t,c)\) is in NR-C2's allowed
list. In a nondiagonal case, the map factors through (7) or (8), with
a single rational function \(R\in\mathbb R(r_1,\ldots,r_k)\).

### Proof

A nonconstant rational function has a nonzero partial derivative in some
variable. There exists a real point where this derivative and all relevant
denominators are nonzero: a product of their nonzero polynomial numerators
and denominators cannot vanish everywhere on \(\mathbb R^k\).
Fix all other variables at their values at that point. Restriction to
this coordinate line gives a nonconstant one-variable rational identity,
with the same \((s,t,c)\). NR-C2 supplies the allowed list.

In those cases the factorizations and slope calculations of NR-C3 work
in the multivariable rational function field without change and give the
single rational function \(R\). \(\square\)

### Why it matters

There is no additional rational surface of fixed-output sharing hidden
by the one-parameter notation. Any such model factors through one of the
displayed curves, with multiplicity still to be charged.

### Scope

Varying output separation, identities only on finite grids, and nonrational
algebraic functions are outside the theorem. Factoring through one rational
function does not determine its finite-grid value count.

## 5. Claim, accounting, and provenance ledger

The starting coordinate formula is the frozen inverse-fiber identity in
the [preceding reuse report](../2026-09-21-sublinear-cubic/correlated-reuse.md).
The classification and differential argument above are new proofs in this
cycle. No unavailable historical digital or rich-fiber proof is used.
No theorem about genus, external curve classification, or novelty is
imported. The elementary facts used are polynomial factorization,
derivatives, and orders of rational functions at complex poles.

| ID | Status and quantifiers | Proof locator and dependencies | Remaining boundary |
|---|---|---|---|
| NR-C1 | PROVED; real polynomial maps in any finite number of parameters, every fixed \((s,t,c)\) | §1; total degree and factorization | Varying outputs and finite selected equalities |
| NR-C2 | PROVED; one-variable real rational maps of every degree, fixed output pair | §2; complex singularities and pole calculation | Nonrational branches and arbitrary finite point sets |
| NR-C3 | PROVED; exact real charts and all rational maps in the exceptional cases | §3; line substitution and exceptional points | Same-set completion and its rates |
| NR-C4 | PROVED; rational maps in any finite number of parameters | §4; restriction to a line and chart factorization | Projection multiplicity and finite-grid value counts |

All claims concern T01 and its fixed plus-sign cubic, version 1 dated
2026-09-21. Evidence: complete internal symbolic proofs in this file;
independent internal lead audit of NR-C1–C4 is complete. No numerical or
symbolic-search program was run.

There is no asymptotic construction in this note, so no input or output
exponent is asserted. The charts give coordinate coincidences only.
Their parameter count is not counted as a scalar count, and the
unprescribed complement of a scalar square is not silently discarded.
The full cubic target remains **OPEN**. The lead report states the cycle's
single next obligation; this companion adds no competing assignment.
