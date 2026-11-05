# Directed triangle compatibility for the plus-sign cubic

**T01 · 6 October 2026 · version 1 · commissioned offline research.**

The fixed polynomial is
\[
P(x,y)=(x-y)^3+x+y.
\]
This appendix treats just the directed scalar triangle
\((a,b),(b,c),(c,a)\), with ordered outputs
\((z,z+h,z+2h)\). The commissioned family fixes
\(h=2r\), where \(r=1/\sqrt3>0\), and varies the real translation
parameter \(z\). The ordered-output uniqueness lemma is proved for arbitrary
real output triples because its proof is no longer and handles every
degeneracy. It is not a classification of arbitrary sharing networks.

The earlier [elliptic report](../2026-09-30-elliptic-geometry/README.md)
and [genus companion](../2026-09-30-elliptic-geometry/genus.md), EG-G1/G2,
are accepted predecessors. Their coordinate templates and the genus-one
classification of mixed-coordinate sharing are inherited. The simultaneous
equations, real triangle injectivity, and fixed-gap component calculation
below are newly checked proofs. No genus calculation, global elliptic
group-law search, or former finite scout is rerun.

**Budget and evidence:** no research program, carrier evaluation, numerical
search, or symbolic-computation program is used in this appendix. The
displayed identities and proofs are exact hand algebra over \(\mathbb R\).
Network use and arithmetic amplification are absent. Lead proof audit is
to be recorded separately after review; no external review or novelty
claim is made.

## 1. SH-G1 — simultaneous sharing equations and exact elimination

### Meaning

Three separate coordinate-sharing equations must close on the same three
scalars. Solving any one sharing curve does not ensure that its points fit
the other two edges. Here the compatibility condition can be written as
two explicit equations for the first two directed differences.

### Exact statement — PROVED

For real \(z,h\), put
\[
u=a-b,\qquad v=b-c,\qquad w=c-a.
\]
The ordered output equations
\[
P(a,b)=z,\qquad P(b,c)=z+h,\qquad P(c,a)=z+2h               \tag{1}
\]
are equivalent to
\[
\boxed{v^3-u^3-u-v=h,}                                    \tag{2}
\]
\[
\boxed{2u+v-3v(u^2+uv+v^2)=0,}                            \tag{3}
\]
together with the unique reconstruction
\[
\boxed{
w=-u-v,\qquad
b=\frac{z-u^3-u}{2},\qquad a=b+u,\qquad c=b-v.}             \tag{4}
\]
This equivalence holds without dividing by \(u,v,w,h\), so it has no
exceptional zero-denominator cases.

### Proof: all three coordinate identifications

Use the inherited template
\[
c_s(q,d)=\frac{q-d^3+s d}{2},\qquad s\in\{1,-1\}.
\]
The triangle requires exactly
\[
\begin{aligned}
b&=c_-(z,u)=c_+(z+h,v),\\
c&=c_-(z+h,v)=c_+(z+2h,w),\\
a&=c_-(z+2h,w)=c_+(z,u).
\end{aligned}                                             \tag{5}
\]
After clearing the common denominator two, these are
\[
\begin{aligned}
v^3-u^3-u-v&=h,\\
w^3-v^3-v-w&=h,\\
u^3-w^3-u-w&=-2h.
\end{aligned}                                             \tag{6}
\]
Adding them gives \(u+v+w=0\). Thus the difference closure in (4)
is an actual consequence of simultaneous sharing, not an independent
product-domain assumption.

### Proof: reduction and its converse

Write \(a=b+u,c=b-v\). The first output in (1) gives the formula for
\(b\) in (4). With that substitution,
\[
P(b,c)-z=v^3-u^3-u-v,                                      \tag{7}
\]
\[
P(c,a)-z=-(u+v)^3-u^3-v.                                  \tag{8}
\]
Subtracting twice (7) from (8) gives
\[
u^3-(u+v)^3-2v^3+2u+v
=2u+v-3v(u^2+uv+v^2).                                    \tag{9}
\]
Consequently (1) implies (2) and (3). Conversely, if (2) and (3) hold,
the reconstruction (4) gives \(P(a,b)=z\); equation (7) gives
\(P(b,c)=z+h\); and (8)–(9) give \(P(c,a)=z+2h\). This proves
both directions, including all possible coincident-scalar cases.
\(\square\)

### Why it matters

Every equality in (5), considered separately with fixed real outputs,
is a mixed-coordinate sharing curve and hence a smooth genus-one curve
by inherited EG-G2. The compatibility equations impose all three
identifications at once. An abundance of real points on the separate
elliptic curves does not supply a positive-dimensional real family for a
fixed ordered output triple.

### Scope

This is an exact elimination for the stated directed triangle and output
order. Reversing edges changes the cubic signs and must not be done
silently. No assertion about the number of compatible points in an
arbitrary larger sharing graph follows from these equations alone.

## 2. SH-G2 — an ordered real output triple has at most one triangle

### Meaning

Two different real triangles cannot have the same three ordered cubic
outputs. The proof compares the two triangles directly, so it does not
require bounded coordinates, nonzero differences, or a chosen elliptic
parametrization.

### Exact statement — PROVED

The map
\[
\mathcal T:\mathbb R^3\longrightarrow\mathbb R^3,
\qquad
\mathcal T(a,b,c)=\bigl(P(a,b),P(b,c),P(c,a)\bigr)           \tag{10}
\]
is injective. Equivalently, for every ordered
\((z_1,z_2,z_3)\in\mathbb R^3\), there is at most one real
\((a,b,c)\) realizing those outputs. Neither the outputs nor the
scalars need be pairwise distinct for this statement.

### Proof

Suppose two triangles have the same ordered outputs. Write their vertices
as \(a_i,a_i'\), with cyclic indices \(i=1,2,3\), and put
\[
\alpha_i=a_i-a_i',\qquad
u_i=a_i-a_{i+1},\quad u_i'=a_i'-a_{i+1}',
\]
\[
k_i=u_i^2+u_i u_i'+(u_i')^2
=\left(u_i+\frac{u_i'}2\right)^2+\frac34(u_i')^2\ge0.
\]
Equality of the \(i\)-th outputs gives exactly
\[
\boxed{(1+k_i)\alpha_i+(1-k_i)\alpha_{i+1}=0.}              \tag{11}
\]
Since \(1+k_i>0\) and \(|1-k_i|\le1+k_i\), it follows that
\[
|\alpha_1|\le|\alpha_2|\le|\alpha_3|\le|\alpha_1|.
\]
All three absolute values therefore equal one number \(M\). If
\(M=0\), the triangles agree. If \(M>0\), then any \(k_i>0\)
would make its inequality strict, since
\(|1-k_i|<1+k_i\). Hence all \(k_i=0\). Equation (11) then reads
\(\alpha_i=-\alpha_{i+1}\) around a cycle of length three, forcing
\(\alpha_1=-\alpha_1\), contrary to \(M>0\). This handles the zero
case explicitly and proves injectivity. \(\square\)

An equivalent exact determinant check also makes the degeneracy harmless.
The linear comparison system (11) has determinant
\[
\prod_{i=1}^3(1+k_i)+\prod_{i=1}^3(1-k_i)
=2(1+k_1k_2+k_2k_3+k_3k_1)>0.                             \tag{12}
\]
In particular it stays invertible when one or all \(k_i\) vanish.

### Why it matters

This is a direct compatibility restriction beyond knowing that each
individual sharing curve has genus one. Once all three outputs are
fixed in their directed order, the real coordinate choices cannot branch
into several distinct scalar triangles.

### Scope

The conclusion is “at most one”; existence for an arbitrary real output
triple is not needed or asserted here. The proof uses the real inequality
\(k_i\ge0\) and is not a uniqueness theorem over \(\mathbb C\).
It also does not bound how many different ordered output triples a large
real scalar set can realize. No universal image lower bound is claimed.

## 3. SH-G3 — the entire real fixed-gap family and its Jacobian

### Meaning

For the commissioned output gap, a known three-point triangle already
provides one solution. Uniqueness then determines every solution. Varying
the initial output only translates those same three points together.

### Exact statement — PROVED

Fix
\[
r=1/\sqrt3>0,\qquad h=2r.
\]
For each real \(z\), the only triangle satisfying (1) is
\[
\boxed{
(a,b,c)=(t-r,t,t+r),\qquad
t=\frac z2+\frac{2r}{3}.}                                 \tag{13}
\]
Thus the full real compatible family, allowing \(z\) to vary, is the
single affine line
\[
(a,b,c,z)=(t-r,t,t+r,\ 2t-4r/3),\qquad t\in\mathbb R.      \tag{14}
\]
The reduced equations (2)–(3) have exactly the one real solution
\((u,v)=(-r,-r)\), independent of \(z\).

For the polynomial map formed by their left sides,
\[
F(u,v)=v^3-u^3-u-v,
\qquad G(u,v)=2u+v-3v(u^2+uv+v^2),
\]
one has everywhere on \(\mathbb R^2\)
\[
\boxed{\det D(F,G)=1+9(u^2+uv+v^2)^2>0.}                  \tag{15}
\]
At \((-r,-r)\) this determinant is \(10\). The unique real intersection
is therefore transverse; it is not hiding a real singular branch.

### Proof: existence and uniqueness

Using only \(r^3=r/3\), the three outputs of \((-r,0,r)\) are
\[
\left(-\frac{4r}{3},\ \frac{2r}{3},\ \frac{8r}{3}\right).
\]
They have successive gap \(2r\). The exact translation identity is
\[
P(x+t,y+t)=P(x,y)+2t.                                    \tag{16}
\]
Consequently (13), with \(z=2t-4r/3\), supplies a triangle for every
real \(z\). SH-G2 excludes any second real triangle with those same
ordered outputs. By SH-G1 the reduced system has no other real solution:
any such solution could be reconstructed into a second triangle for the
same chosen \(z\). This proves (13)–(14) and the complete real solution
description for the reduced equations.

### Proof: the required local calculation

Differentiation gives
\[
D(F,G)=
\begin{pmatrix}
-3u^2-1&3v^2-1\\
2-6uv-3v^2&1-3u^2-6uv-9v^2
\end{pmatrix}.
\]
Expanding its determinant gives
\[
1+9(u^4+2u^3v+3u^2v^2+2uv^3+v^4)
=1+9(u^2+uv+v^2)^2,
\]
which proves (15). At the actual solution the matrix is
\(\left(\begin{smallmatrix}-2&0\\-1&-5\end{smallmatrix}\right)\),
with determinant \(10\).

For comparison, the full ordered-output map (10) has derivative
\[
D\mathcal T=
\begin{pmatrix}
1+3u^2&1-3u^2&0\\
0&1+3v^2&1-3v^2\\
1-3w^2&0&1+3w^2
\end{pmatrix},\qquad w=-u-v.
\]
Formula (12), with \(k_1=3u^2,k_2=3v^2,k_3=3w^2\), yields
\[
\det D\mathcal T
=2\bigl(1+9(u^2v^2+v^2w^2+w^2u^2)\bigr)
=2\bigl(1+9(u^2+uv+v^2)^2\bigr)>0.                        \tag{17}
\]
It equals \(20\) along (14). Positive Jacobian is used only to describe
local nonsingularity; global uniqueness came from the direct comparison
proof, not an unsupported inference from a nonvanishing determinant.
\(\square\)

### Why it matters

For this fixed gap there is no additional real elliptic parameter left
after the three sharing constraints close. Every designated edge has
one of the two differences
\[
a-b=b-c=-r,\qquad c-a=2r.                                 \tag{18}
\]
Any finite assembly must therefore count repeated translated endpoints
and edges as actual scalars and ordered pairs. Their capacity and full-square
complement are charged in the coordinating report and ledger.

### Scope

Only the commissioned real fixed-gap family is classified. This does not
classify a complex intersection away from its identified real point,
different output-gap patterns, different orientations, or larger networks.
The individual sharing curves retain their accepted genera. No high-genus
scarcity statement, new arithmetic mechanism, or independent next proof
obligation is introduced. The fixed T01 target remains **OPEN**.

## Claim and source ledger

All new claims below concern T01 and \(P=(x-y)^3+x+y\), date
2026-10-06, version 1, in this file. The evidence is complete displayed
proof, not finite testing. Initial internal status: author algebra checked;
lead independent audit to be recorded in the cycle's verification record.

| Claim | Quantifiers and hypotheses | Locator and dependencies | Status and boundary |
|---|---|---|---|
| SH-G1 | All real \(z,h,a,b,c\), fixed directed order; no nonzero-difference assumption | §1, exact inherited templates and new substitutions (5)–(9) | PROVED; one directed triangle, no arbitrary network classification |
| SH-G2 | Every ordered real output triple; all real scalar triples, including degenerate ones | §2, difference of cubes and cyclic comparison; no genus or group law used | PROVED injectivity; arbitrary-triple existence and complex uniqueness not asserted |
| SH-G3 | Fixed \(r>0,r^2=1/3,h=2r\); every real \(z\) | §3, SH-G1/G2, one exact seed identity and translation, explicit Jacobian | PROVED complete real component; no full-image bound asserted |

The latest elliptic README and geometric proof companion were read, and
the setup/map/migration, master, T01 state and SPEC/STATUS, conflict and
mechanism/failure/open-lemma records were checked for scope. MC-06's absent
historical originals remain absent and are not proof dependencies. Earlier
source files, accepted results, experiment data and registries are unchanged.
