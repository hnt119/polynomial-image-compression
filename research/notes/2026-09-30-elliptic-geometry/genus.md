# Fibers, coordinate sharing, and geometric genus

**T01 · 30 September 2026 · version 1 · offline proof note.**

The target remains
\[
P(x,y)=(x-y)^3+x+y.
\]
The quartic \(Q(x,y)=(x-y)^4+x+y\) below is a secondary comparison,
**not T02**, whose fixed polynomial is \((x+2y)^4+3x-y\).
All curves and normalizations in the geometric statements are over
\(\mathbb C\), with real loci discussed separately. For a reducible curve
the normalization is a disjoint union: its component genera are listed,
rather than assigning it the genus of one connected curve.

The older [rational-reuse proof](../2026-09-21-nonlinear-reuse/rational-reuse-curves.md),
NR-C2/C3, already locates the cubic singularities and gives its real rational
exceptions. This note adds the complete complex geometric classification,
the comparison with actual output fibers and collision varieties, and the
quartic comparison. It does not rerun the old parametrization search.
The [near-complete report](../2026-09-30-near-complete-charts/README.md),
especially NC-C2, supplies the retained full-square quantitative criterion.

No carrier evaluations, programs, symbolic computation runs, network calls,
arithmetic amplification or external curve theorem are used. The elementary
covering calculation used to determine genus is proved in §2. Proof status
below means a complete argument is displayed here; independent internal
audit is to be recorded by the lead after review.

## 1. EG-G1 — actual output fibers and the collision variety are rational

### Meaning

An elliptic curve enters when two fixed output fibers are required to share
a scalar coordinate. A single output fiber is a polynomial graph. Confusing
these two curves would give an incorrect genus obstruction to the target.

### Exact statement — PROVED

For \(n=3,4\), put \(P_n=(x-y)^n+x+y\). Every affine fiber
\(P_n=z\) is isomorphic to the affine line by
\[
u=x-y,\qquad
x=\frac{z-u^n+u}{2},\qquad y=\frac{z-u^n-u}{2}.                 \tag{1}
\]
Its projective plane closure has normalization \(\mathbb P^1\) and genus
zero. Its unique point at infinity is singular: its local parametrization
has orders \((n-1,n)\), giving the cuspidal types \((2,3)\) and \((3,4)\)
for the cubic and quartic, respectively.

The entire affine collision variety
\[
\mathcal V_n=\{(x,y,x',y'):P_n(x,y)=P_n(x',y')\}
\]
is isomorphic to \(\mathbb A^3\), with coordinates \((u,v,z)\).
Fixing a common output \(z\) gives \(\mathbb A^2\), not an elliptic curve.

### Proof

Equation (1) and its polynomial inverse give the affine assertion. In
projective coordinates \([U:L:Z]\), where \(U=X-Y\), \(L=X+Y\), the closure is
\[
U^n+LZ^{n-1}-zZ^n=0.
\]
At infinity it has just \([0:1:0]\), and all first partial derivatives
vanish there. The global projective parametrization is
\[
[T:S]\longmapsto[T S^{n-1}:zS^n-T^n:S^n].                    \tag{2}
\]
The three displayed forms have no common zero; the map is one-to-one on
the affine part, where its inverse is \(u=U/Z\). Near \(S/T=w=0\),
\[
U/L=\frac{w^{n-1}}{zw^n-1},\qquad
Z/L=\frac{w^n}{zw^n-1}.
\]
Thus (2) supplies the smooth normalization and the stated local orders.
Finally use (1) twice, with differences \(u,v\) and the same \(z\).
The inverse on \(\mathcal V_n\) is
\((x-y,x'-y',P_n(x,y))\), so this is an affine polynomial isomorphism.
\(\square\)

### Why it matters

Neither the one-output fiber nor the unrestricted collision variety has
positive genus. The higher-genus curve arises only after fixing the two
output labels and imposing an additional coordinate equality.

### Scope

The isomorphism is a change of pair coordinates. It does not preserve a
product scalar domain or give a small same-set carrier. No full-image
estimate follows from rationality of this ambient variety.

## 2. Elementary genus calculation used below

Let
\[
C_{n,s,t,c}:\quad u^n-v^n-su+tv-c=0,\qquad n\in\{3,4\},
\quad s,t\in\{1,-1\}.                                      \tag{3}
\]
Use the normalization of each irreducible component. Geometric genus here
is the genus of the resulting compact complex curve, equivalently the
usual genus of its compact Riemann surface.

### Branch count

The projective equation is
\[
U^n-V^n-sUZ^{n-1}+tVZ^{n-1}-cZ^n=0.                         \tag{4}
\]
There are exactly \(n\) points at infinity, with \(U/V\) an \(n\)-th
root of unity. They are all smooth because the \(U,V\) partial derivatives
there are \(nU^{n-1},-nV^{n-1}\), both nonzero. Projection to \(u\) has
degree \(n\) in total and is unramified at infinity. Indeed, writing
\(w=1/u\), \(r=v/u\), (4) becomes
\[
1-r^n-sw^{n-1}+trw^{n-1}-cw^n=0.
\]
At \(w=0\) its derivative in \(r\) is nonzero, so \(w\) is a local
coordinate and \(u\) has a simple pole.

Finite singularities occur exactly at
\[
nu_0^{n-1}=s,\qquad nv_0^{n-1}=t,\qquad
c=\frac{n-1}{n}(tv_0-su_0).                                \tag{5}
\]
Both \(u_0,v_0\) are nonzero. The second-degree part in
\(h=u-u_0,k=v-v_0\) is
\[
\frac{n(n-1)}2\bigl(u_0^{n-2}h^2-v_0^{n-2}k^2\bigr),
\]
with two distinct, nonvertical tangent lines. This is an ordinary node:
more explicitly, each one-variable difference from the critical value is
its displacement squared times a nonvanishing analytic function. Taking
an analytic square root of that function transforms the local equation
to \(a^2-b^2=0\). Its normalization has two branches, and projection to
\(u\) is unramified on both.

For each of the \(n-1\) critical choices of \(v\), the equation for \(u\)
has \(n\) roots counted with multiplicity. A root at a smooth point has
\(F_u\ne0\), and the local projection to \(u\) has ramification index
two, since the first derivative in \(v\) vanishes and the second does not.
A root that is a node has multiplicity two in this equation and contributes
zero ramification on its two normalized branches. There are no other
ramification points. Consequently, if there are \(\nu\) nodes, the total
ramification contribution on the disjoint normalization is
\[
R=n(n-1)-2\nu.                                               \tag{6}
\]

### Why the branch count determines genus

For completeness, consider a degree-\(d\) map of compact complex curves.
Away from its finitely many branch values it is an ordinary covering.
Choose a triangulation of the target with all branch values among its
vertices. Every open edge and face has \(d\) lifts. A vertex has
\(d-\sum(e_p-1)\) preimages, because the local degrees of its preimages
sum to \(d\). Counting vertices minus edges plus faces therefore gives
\[
\chi(X)=d\chi(Y)-\sum_p(e_p-1).                              \tag{7}
\]
Here local degrees come from the local form of a nonconstant holomorphic
map: a zero of order \(e\) is, after multiplying by a nonvanishing analytic
unit and taking its \(e\)-th root, \(w\mapsto w^e\).
For a connected compact orientable surface, \(\chi=2-2g\). Applying (7)
to the sphere \(\mathbb P^1\), and adding over components if necessary,
proves
\[
\sum_i(2-2g_i)=2n-R.                                        \tag{8}
\]
In particular, an irreducible curve (3) with only the nodes in (5) has
\[
g=\frac{(n-1)(n-2)}2-\nu.                                  \tag{9}
\]
This proves the genus calculation used here, rather than importing a
plane-curve genus formula. The irreducibility needed in each use of (9)
is checked directly in the next sections.

One can also see directly why irreducibility gives a connected surface
in this calculation. If the normalized cover split into two nonempty
unions of connected components, take the product of \(v-v_j(u)\) over
the sheets of either union. Its coefficients are single-valued away from
the branch values. They extend across every finite branch value, since
all roots of the monic equation in \(v\) remain bounded there. At infinity
they have polynomial growth, because \(v/u\) tends to roots of unity.
Thus the coefficients are polynomials in \(u\), by removing the pole at
infinity (or by the elementary Cauchy bounds). These two sheet products
would factor (3) in \(\mathbb C[u,v]\), contradicting irreducibility.

## 3. EG-G2 — complete cubic sharing classification over the complex numbers

### Meaning

For example, equality of two first coordinates from outputs \(z,w\) is
\(u^3-v^3-u+v=z-w\). Usually this is a smooth genus-one curve. At three
special real differences it degenerates to rational components or a nodal
rational cubic. Mixed first/second-coordinate sharing is smooth for every
real output difference.

### Exact statement — PROVED

For \(c=z-w\), the equality of coordinate templates
\[
\frac{z-u^3+su}{2}=\frac{w-v^3+tv}{2}
\]
is precisely \(C_{3,s,t,c}\). Set \(a=1/\sqrt3\). Its complete complex
singularity and normalization list is:

| Signs | Singular values of \(c\) | Normalization at those values |
|---|---|---|
| \(s=t=1\) | \(0,\ \pm4a/3\) | At zero: line and conic, genera \((0,0)\). At either nonzero value: irreducible nodal cubic, genus zero. |
| \(s=t=-1\) | \(0,\ \pm4ia/3\) | The same component and genus descriptions over \(\mathbb C\). |
| \(s=-t\) | \(\{(2a/3)(\epsilon+i\eta):\epsilon,\eta\in\{\pm1\}\}\) | At each of the four distinct values: irreducible nodal cubic, genus zero. |

All values not listed give a smooth irreducible cubic of genus one. All
three points at infinity are smooth. Thus for **real** \(c\):

- first/first sharing has only the exceptional values \(0,\pm4/(3\sqrt3)\);
- second/second sharing has only the exceptional value \(0\);
- mixed-coordinate sharing is always smooth of genus one.

Every smooth real curve in this list has the real point \([1:1:0]\).
With that point designated, it is an elliptic curve, meaning a pointed
smooth projective genus-one curve. No particular group-law formula or
finite invariant set is asserted here.

The designated real infinity point need not be a flex. Its tangent is
\(U=V\), whose restriction to (4) is
\(Z^2((t-s)U-cZ)\). On a smooth cubic this has intersection multiplicity
three at \([1:1:0]\) when \(s=t\), and two when \(s\ne t\). Thus a
chord-and-tangent group-law convention that requires a flex origin cannot
be applied unchanged to this chosen point in the mixed-sign cases.

### Proof: singularities and irreducibility

Formula (5) gives \(u_0^2=s/3,v_0^2=t/3\) and
\(c=2(tv_0-su_0)/3\). Enumerating these two choices in each coordinate
gives exactly the table. At \(s=t,c=0\) there are two singular points;
at every other listed value there is exactly one. Section 2 proves that
each is an ordinary node and that infinity is smooth.

A reducible cubic over \(\mathbb C\) has a line component. A vertical
line is impossible because the coefficient of \(v^3\) is \(-1\). Write
any other line as \(u=\lambda v+\mu\). The coefficients of \(v^3,v^2,v\)
in its substitution force, in order,
\[
\lambda^3=1,\qquad \mu=0,\qquad t=s\lambda.
\]
Since \(t/s\) is \(1\) or \(-1\), these imply \(\lambda=1,s=t\);
the constant term then forces \(c=0\). Conversely,
\[
C_{3,s,s,0}:\quad (u-v)(u^2+uv+v^2-s)=0.                    \tag{10}
\]
The conic is smooth and meets the line transversely at
\(u=v=\pm\sqrt{s/3}\). A smooth complex conic is rational directly by
projection from any one of its points: a line of slope \(r\) has one
known intersection and its remaining intersection is rational in \(r\).
This also constructs its \(\mathbb P^1\) normalization. Thus (10) has
normalization \(\mathbb P^1\sqcup\mathbb P^1\).

All other cubics are irreducible. Equations (6)–(9) give genus one in
the smooth case and genus zero when there is one node.

### Proof: normalization of every nodal irreducible cubic

Let \((u_0,v_0)\) be its unique node. Put \(v-v_0=r(u-u_0)\). After
removing the doubled intersection at the node, the remaining root is
\[
h(r)=-\frac{3(u_0-v_0r^2)}{1-r^3},\qquad
u=u_0+h(r),\quad v=v_0+r h(r).                              \tag{11}
\]
The inverse away from the node and vertical line is
\(r=(v-v_0)/(u-u_0)\), so (11) is birational. In homogeneous slope
coordinates \([R:S]\) its projective forms are
\[
\begin{split}
U&=u_0(S^3-R^3)-3(u_0S^2-v_0R^2)S,\\
V&=v_0(S^3-R^3)-3(u_0S^2-v_0R^2)R,\\
Z&=S^3-R^3.
\end{split}                                                \tag{12}
\]
They have no common zero in the irreducible case. Indeed, a common zero
would have \(r^3=1\), \(u_0=v_0r^2\). Using \(u_0^2=s/3,v_0^2=t/3\)
then gives \(r=s/t\); hence \(r=1,s=t,u_0=v_0,c=0\), the excluded
reducible case. Thus (12) gives the normalization map from \(\mathbb P^1\).
The two slopes \(r^2=u_0/v_0\) give the two points over the node.
\(\square\)

### Why it matters

This identifies exactly where an elliptic mechanism can enter coordinate
sharing. The earlier real rational exceptions are precisely degenerations
of this genus-one family; the smooth cases cannot be traced by a rational
parameter, as also proved without genus in NR-C2.

### Scope

The genus is that of a fixed sharing curve, with \(z,w,s,t\) fixed. An
elliptic point operation does not by itself preserve the other scalar
coordinates, a selected finite point set, or the same-set Cartesian square.
No support or finite-coordinate-reuse bound follows just from the table.
For \(s=t=-1,c=0\), the complex conic in (10) has no real points; the
real locus is only the diagonal. For the two real nodal first/first cubics,
the real node is isolated and its two normalization preimages are nonreal,
as already described in NR-C3. These real qualifications do not change
their complex normalization genus.

## 4. EG-G3 — the quartic sharing comparator

### Meaning

The analogous sharing curve for a fourth power generally has genus three.
Its zero-difference degeneration still contains an elliptic component.
This supplies a genuine higher-genus comparison without changing the
fixed T01 target or silently substituting another polynomial for T02.

### Exact statement — PROVED

For \(Q=(x-y)^4+x+y\), equality of the corresponding signed coordinates
is
\[
C_{4,s,t,c}:\quad u^4-v^4-su+tv-c=0.
\]
Let \(\alpha=4^{-1/3}\), \(\omega=e^{2\pi i/3}\), and
\(\beta=3\alpha/4\). For every sign pair, its singular values are
\[
\mathcal D=\{\beta(\omega^j-\omega^i):i,j\in\{0,1,2\}\}.
                                                                    \tag{13}
\]
There are seven distinct values: zero and six nonzero, nonreal values.
The complete classification is:

| Value | Projective curve | Normalization |
|---|---|---|
| \(c\notin\mathcal D\) | Smooth irreducible quartic | Genus 3 |
| \(c\in\mathcal D\setminus\{0\}\) | Irreducible quartic with exactly one ordinary node | Genus 2 |
| \(c=0\) | A line and a smooth irreducible cubic meeting transversely at three points | Disjoint components of genera \((0,1)\) |

All four points at infinity are smooth. In particular, **every nonzero
real \(c\)** gives a smooth genus-three curve, for every choice of signs.

### Proof: reduction and singularities

Set \(a=su,b=tv\). Because the exponent is even and \(s^2=t^2=1\),
the equation becomes, independently of the signs,
\[
a^4-b^4-a+b-c=0.                                           \tag{14}
\]
Its critical points have \(a=\alpha\omega^i,b=\alpha\omega^j\),
and (5) gives (13). The three choices \(i=j\) give zero. The six
ordered differences with \(i\ne j\) are all distinct: explicitly they
are \(\pm(1-\omega),\pm(1-\omega^2),\pm(\omega-\omega^2)\), multiplied
by \(\beta\). None is real. Thus there are three nodes at zero and
one node at each other singular value. Section 2 proves the node and
infinity assertions.

### Proof: components and irreducibility

At zero,
\[
a^4-b^4-a+b=(a-b)\bigl((a+b)(a^2+b^2)-1\bigr).              \tag{15}
\]
Write \(D=(a+b)(a^2+b^2)-1\). Its finite partial derivatives are
\[
D_a=3a^2+2ab+b^2,\qquad D_b=a^2+2ab+3b^2.
\]
If both vanish, their difference gives \(a^2=b^2\), and either sign
then forces \(a=b=0\), which is not on \(D=0\). At infinity its three
distinct leading directions are \(a/b=-1,i,-i\), and these are smooth.

The cubic \(D\) is irreducible. A line component could not be vertical.
Substitution \(a=\lambda b+\mu\) would first force
\(\lambda^3+\lambda^2+\lambda+1=0\). The coefficient of \(b^2\) is
\(\mu(3\lambda^2+2\lambda+1)\), whose second factor is nonzero at each
of those three simple roots; hence \(\mu=0\), leaving the impossible
constant term \(-1=0\). Its genus is one: project \(D=0\) to the
slope \(r=b/a\), obtaining
\[
a^3=\frac1{(1+r)(1+r^2)}.
\]
This is a degree-three cover with ramification index three over each of
the three simple zeros of \((1+r)(1+r^2)\). At \(r=\infty\), set
\(t=1/r\), \(a=tA\); then \(A^3=1/((1+t)(1+t^2))\), so it is
unramified there. There are no further branch points. Hence (7) gives
\(2-2g=6-3\cdot2=0\). The line in (15) meets it at
\(a=b,4a^3=1\). The respective gradients are \((1,-1)\) and
\((6a^2,6a^2)\), so these three intersections are transverse.

For \(c\ne0\), a line component in (14) would have the form
\(a=\lambda b+\mu\). Its coefficients give successively
\(\lambda^4=1,\mu=0,\lambda=1,c=0\), a contradiction.
If there is a factorization without a line component, it is a product
of two quadratics. Write the factors as
\(q_2+q_1+q_0\) and \(r_2+r_1+r_0\), with homogeneous subscripts.
Their top parts multiply to \(a^4-b^4\), so \(q_2,r_2\) are coprime.
The absent cubic term requires
\(q_2r_1+r_2q_1=0\). Coprimality and degrees force
\(q_1=r_1=0\). The product would then have no linear term, contradicting
\(-a+b\) in (14). Thus every \(c\ne0\) curve is irreducible.

Now (9) gives genus three without a node and genus two with one node.
This also verifies every claimed normalization genus. At zero the two
components are already smooth, so normalization simply separates their
three crossings. \(\square\)

### A concrete model for the nodal normalization

For completeness, at a nonzero complex singular value let \((a_0,b_0)\)
be the node of (14). Projection from that node, with
\(a=a_0+h,b=b_0+rh\), leaves the quadratic equation
\[
(1-r^4)h^2+4(a_0-b_0r^3)h+6(a_0^2-b_0^2r^2)=0.              \tag{16}
\]
Thus its normalization is the smooth projective model of
\[
Y^2=16(a_0-b_0r^3)^2
      -24(1-r^4)(a_0^2-b_0^2r^2),                           \tag{17}
\]
with \(Y=2(1-r^4)h+4(a_0-b_0r^3)\). These equations are birational
away from the finitely many excluded slopes. The genus-two assertion
comes from the complete branch count above, not from assuming that an
unsimplified displayed equation automatically has genus two.

### Why it matters

The comparison provides smooth genus-three and nodal genus-two sharing
curves by the same elementary calculation as the cubic elliptic curves.
It separates the role of the degree in coordinate sharing from the
rationality of the actual output fibers, which remains true in both cases.

### Scope

This is a geometric classification of a fixed comparison family. It is
neither a T02 theorem nor a real-point or Cartesian-grid estimate for Q.
The zero-difference elliptic component is an explicit exception to any
claim that all quartic sharing components have genus at least two.

## 5. EG-G4 — exactly what positive genus obstructs

### Meaning

Positive genus prevents a rational parameter from tracing the whole
sharing curve. Genus at least two also prevents an elliptic curve from
mapping nonconstantly onto it. Neither assertion makes its real points
scarce or bounds finite scalar reuse.

### Exact statement — PROVED

For the normalized components above:

1. No genus-at-least-one component admits a nonconstant rational
   parametrization from \(\mathbb P^1\).
2. No genus-at-least-two component admits a nonconstant algebraic map
   from a smooth projective genus-one curve.
3. Every real sharing curve (3) has infinitely many real affine points,
   including all the smooth real genus-three curves in EG-G3.

### Proof

A nonconstant algebraic map between smooth projective complex curves is
a finite branched covering; the local-order and triangulation proof of
(7) applies. Thus
\[
2g_X-2=d(2g_Y-2)+R,\qquad d\ge1,\ R\ge0.                  \tag{18}
\]
For \(g_X=0,g_Y\ge1\) the left side is negative and the right side
nonnegative. For \(g_X=1,g_Y\ge2\) the left side is zero and the right
side positive. These contradictions prove the first two assertions.
A rational parametrization of a projective plane curve lifts to its
normalization: remove common factors from its projective coordinates to
extend it at parameter poles, and at a node lift along the analytic
branch occupied on a punctured parameter disk. Thus the same argument
also excludes rational charts whose image is the singular genus-two
quartic rather than its normalization.

For the third assertion, in the infinity chart used in §2 choose
\(r(0)=1\). The derivative in \(r\) equals \(-n\ne0\). With real
coefficients the implicit analytic solution \(r(w)\) is real for all
sufficiently small real \(w\). Every nonzero such \(w\) gives the
distinct affine real point \((u,v)=(1/w,r(w)/w)\). This proves a real
continuum of points, independently of genus. \(\square\)

### Why it matters

An elliptic construction cannot be transferred to a fixed smooth quartic
sharing curve by a nonconstant algebraic map from its elliptic parameter
curve. That is a precise obstruction to one proposed type of transfer.
It does not obstruct arbitrary real finite correspondences or a changing
family of parameter curves.

### Scope and the retained quantitative gate

No theorem about rational points over a number field, uniform rational
point counts, or finite groups is used or asserted. In particular, no
Faltings-type claim is inferred for real sets, and no such imported result
is needed for the displayed proofs. Genus alone supplies neither a bound
for \(|C\cap(U\times V)|\) nor a uniform bound for the coordinate
occurrences generated by a varying family of sharing curves.

For any proposed T01 scalar carrier and controlled pair set, the unchanged
ledger is
\[
N=|A|,\quad Q_E=|E|,\quad Z_E=|P(E)|,\quad B=N^2-Q_E,
\qquad |P(A,A)|\le Z_E+B.                                   \tag{19}
\]
An elliptic or higher-genus description supplies none of the missing
estimates \(B=O(N^{2-\delta})\), \(Z_E=O(N^{2-\varepsilon})\)
for fixed positive exponents. The sole retained target-level obligation
is the actual small-fiber pair-mass tail NC-O1 from the near-complete
report; this companion does not add a second unresolved obligation.

## 6. Claim and provenance ledger

All entries are dated 2026-09-30, version 1, in this file. They are complete
displayed proofs, with no external result, computation, novelty claim or
external peer review. Lead internal audit is pending at initial writing.

| ID | Track/branch and polynomial | Quantifiers and hypotheses | Proof locator and dependencies | Status / unresolved boundary |
|---|---|---|---|---|
| EG-G1 | T01 plus explicitly separated quartic comparison; \(P_n=(x-y)^n+x+y\) | Every \(z\in\mathbb C\), \(n=3,4\); entire collision variety | §1, explicit polynomial maps and projective parametrization | PROVED; no same-set or support consequence |
| EG-G2 | T01; \(P=P_3\) | Every \(s,t\in\{\pm1\},c\in\mathbb C\); real restrictions stated separately | §§2–3; direct derivatives, line factors, elementary covering formula; consistent with NR-C2/C3 | PROVED; finite coordinate-reuse rates remain open |
| EG-G3 | Comparison only; \(Q=P_4\), not T02 | Every \(s,t\in\{\pm1\},c\in\mathbb C\) | §§2,4; exact sign change, factor analysis, branch count | PROVED; no quartic image bound asserted |
| EG-G4 | T01 and stated quartic comparison | Fixed normalized components; nonconstant algebraic maps of smooth projective curves; real coefficients for real-locus claim | §5 and the proved formula (7) | PROVED; no real-point scarcity, arithmetic finiteness, or unrestricted correspondence theorem |

**Source availability.** The complete older rational-reuse proof and current
near-complete proof report were read. The migration summaries, T01
SPEC/STATUS and MC-06 were checked for scope. The historically missing
digital and rich-fiber originals remain unavailable and are not dependencies.
The T04 export's reported high-genus/arithmetic results are a different
track; they are not used as proof evidence for any assertion here.
