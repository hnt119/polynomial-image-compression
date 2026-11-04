# The actual conic-frame locus on the sharing elliptic curve

T01, 11 October 2026, version 2 (bounded audit results appended). The fixed polynomial is
\(P(x,y)=(x-y)^3+x+y\). This appendix is authorized offline symbolic
research. No mathematical program, finite search, or full-square evaluation
was used to derive it. The claims below have complete proofs here; internal
lead/referee verification is recorded separately in verification.md.

The scope is the two-row conic frame already used in CP-C1. It is not a
classification of all collision patterns, all elliptic correspondences, or
all torsion points. In particular, a finite compatible point is not a
growing construction and a compatibility-cover obstruction is not a new
global factorization theorem for P.

## TC-G1. Correct sharing curve, scalar maps, and real fibers

**PROVED.** Fix real outputs z,w with c=z-w nonzero. Write
\[
 x_z(u)=\frac{z-u^3+u}{2},\qquad
 y_z(u)=\frac{z-u^3-u}{2}.
\]
Same-second-coordinate sharing is the smooth genus-one curve
\[
 C_c:\quad u^3-v^3+u-v=c.                                      \tag{1}
\]
Its real elliptic model and inverse are
\[
 E_c:\quad Y^2=X^3-48X-128-432c^2,                             \tag{2}
\]
\[
 d=u-v,\quad \ell=u+v,\quad
 X=\frac{12c}{d}-4,\quad Y=\frac{36c\ell}{d},                  \tag{3}
\]
\[
 d=\frac{12c}{X+4},\quad \ell=\frac{Y}{3(X+4)},\quad
 u=\frac{\ell+d}{2},\quad v=\frac{\ell-d}{2}.                 \tag{4}
\]
The three actual scalar slots are
\[
 A=x_z(u),\qquad B=x_w(v),\qquad D=y_z(u)=y_w(v).              \tag{5}
\]
They satisfy P(A,D)=z and P(B,D)=w. Each is a rational function of degree
nine on E_c. Each has pole order three at exactly
\[
 \Omega=\{O,(-4,12c\sqrt{-3}),(-4,-12c\sqrt{-3})\}.             \tag{6}
\]
Only O is real. Every finite real elliptic point is in the affine chart
(4). The triple (A,B,D) determines its parameter point uniquely. On the
real locus D is injective, A and B each have at most three preimages, and
the ordered pair (A,B) has at most two preimages.

**Proof.** Equation (1) gives
\[
 d(3\ell^2+d^2+4)=4c.
\]
In particular d is nonzero. Substitution gives (2), and (4) is its inverse.
This is the s=-1 specialization of EG-C1 in
[complex-extensions.md](../2026-09-30-elliptic-geometry/complex-extensions.md),
with the sign and short-coordinate shift checked here. Directly,
\[
 \Delta=-2^{12}3^6c^2(16+27c^2)\ne0.
\]
At X=-4 the right side of (2) is -432c^2, so it has no real point there.
The affine plane cubic is smooth; its three projective points at infinity
are also smooth, with u and v having simple poles at each. They map to
(6). Their unique real member [1:1:0] maps to O. The cubic terms in each
slot in (5) therefore have nonzero leading coefficient and pole order
three at all three points. The lower-degree terms cannot cancel them.
This proves degree nine and all assertions about poles.

Equation (1) is precisely y_z(u)=y_w(v). Recovering u=A-D and v=B-D
proves injectivity of the triple. For real u, the equation
\(v^3+v=u^3+u-c\) has exactly one real solution, while
\(D=(z-u^3-u)/2\) is strictly decreasing in u. The cubic expressions
for A and B give the stated real upper bounds for their fibers. Finally
A-B=u-v=d; fixing (A,B) fixes X, which gives at most two elliptic points.
The complex degree nine must not be substituted for an actual real
projection count. \(\square\)

## TC-G2. Exactly when two elliptic points complete the same frame

**PROVED.** Suppose two distinct finite real points of E_c have the same
ordered first-coordinate slots (A,B). Their shared-second-coordinate
slots are distinct. Writing d,ell for the first point, the exact necessary
and sufficient conditions are
\[
 3d^2+\ell^2=4,\qquad 2d^3-4d+c=0,\qquad \ell\ne0.           \tag{7}
\]
The second point is its elliptic negative. Conversely (7) gives such a
pair. For c>0 one has
\[
 0<d<2/\sqrt3,
\]
so there are at most two admissible d values, hence at most four real
points. Over the complex numbers there are at most six points satisfying
(7). For a frame with four distinct actual scalars also exclude
\(d^2=\ell^2=1\).

**Proof.** Fixed A-B fixes X, so distinct points must be R and -R.
Negation sends (u,v) to (-v,-u). Equality of the first slot becomes
\[
 (u+v)(u^2-uv+v^2-1)=0.                                    \tag{8}
\]
The factor u+v=0 means Y=0 and R=-R, so gives no second point. The other
factor is \((\ell^2+3d^2)/4-1\). Combining it with (1) yields (7).
All steps reverse, and equality of A with fixed d also gives equality
of B. The D slots differ because D is injective on the real locus.

The real equation d(3ell^2+d^2+4)=4c gives sign(d)=sign(c). On the
interval \(0<d<2/\sqrt3\), the function 4d-2d^3 first increases and
then decreases, so a fixed c>0 occurs at most twice. The cubic in (7)
has at most three complex roots and each has at most two ell values.
Rows differ by d and columns by ell. Their two unordered pairs coincide
exactly when d^2=ell^2; under (7) this is d^2=ell^2=1. This is the
equal-block degeneration, not a four-distinct-scalar frame. \(\square\)

In the original frame notation, choose h,s>0 satisfying
\[
 3h^2+s^2=1,\quad H(h)=4h(1-2h^2),\quad c=2H(h),
 \quad z=2q+H(h),\quad w=2q-H(h).                            \tag{9}
\]
The two marked points and all their slots are exactly
\[
 R_\pm=(44-96h^2,\ \pm288s(1-2h^2)),                        \tag{10}
\]
\[
 \begin{array}{c|c|c|c|c|c}
 &u&v&A&B&D\\ \hline
 R_+&h+s&-h+s&q+h&q-h&q-s\\
 R_-&h-s&-h-s&q+h&q-h&q+s
 \end{array}                                                \tag{11}
\]
Indeed d=2h, ell=+/-2s in (3), and (9) gives (10). Direct substitution
in (5) gives (11). The exchange R_+ to R_- swaps the columns of one
frame; it does not make a new width. The diagonal u=v is absent because
c is nonzero; Y=0 is excluded when two distinct columns are requested.

This finite locus is the complete fixed-output CP paired-row locus.
The full elliptic curve parametrizes three-slot sharing, not an entire
one-parameter family of two-column CP frames with the same outputs.

## TC-G3. The original CP seed permits only the column exchange

**PROVED.** For the original CP seed
\[
 f(t)=64t^3-80t^2+28t-1=0,\quad 0<t<1/12,
 \quad h=\sqrt t,\quad s=h(5-8t),                           \tag{12}
\]
the complete admissible fixed-c locus in TC-G2 is just R_+,R_- of
(10). In particular it has no different width at the same ordered
outputs and center.

**Proof.** On [0,1/12], f is strictly increasing, and f(1/24)=7/216>0.
Thus 0<t<1/24. The function t(1-2t)^2 is strictly increasing on
(0,1/6), so
\[
 0<c^2=64t(1-2t)^2<121/54<64/27.
\]
Consequently \(0<c<8/(3\sqrt3)\). On \((0,2/\sqrt3)\),
4d-2d^3 increases up to its unique maximum and then decreases to the
endpoint value \(8/(3\sqrt3)\). Every c strictly below that endpoint
value has exactly one admissible positive d. Here it is d=2h, with the
two signs of ell=2s. \(\square\)

If a translation sends R_+ to the other compatible point, its translating
element is -2R_+. Whether that element has a particular finite order is
an additional finite question; the compatible result still only exchanges
the two existing columns. This statement does not exclude isolated
higher-order torsion relations.

There is also a stronger, already saved seed-specific result: B-CP in
[B_division.md, B1--B2](../2026-10-11-transfer-division-entropy/B_division.md)
excludes the previous CP-O1 attachment even with variable outputs and
center, under its exact zero-row and two-old-endpoint requirements. That
is imported from a separate checkpoint. Its exhaustive role reduction
has been read here; its five saved Bezout identities passed the separately
executed independent arithmetic audit recorded below. They were not
multiplied by this appendix's author. The old c=6 division scout is not
repeated.

## TC-G4. The necessary completion cover has genus four

**PROVED.** Start with a general point of E_c and the actual pair (A,D)
with output z, as in (5). To complete it to a second distinct column in
the same z-row one must choose
\[
 u'=\frac{-u+W}{2},\qquad W^2=4-3u^2.                       \tag{13}
\]
The smooth projective normalization \(\mathcal D_c\) of this double
cover of E_c is connected of genus four, for every real c nonzero.
The four completed scalar slots are rational on this cover:
\[
 A,\quad D=A-u,\quad D'=A-u',\quad A'=A-u-u'.               \tag{14}
\]
Each has degree eighteen as a function on \(\mathcal D_c\). The frame
has center and signed widths
\[
 q'=A-\frac{u+u'}2,\quad h'=\frac{u+u'}2,
 \quad s'=\frac{u'-u}2,\quad 3h'^2+s'^2=1.                 \tag{15}
\]
Its outputs are z and 4q'-z. It need not have second output w or second
row B from the original elliptic sharing point.

**Proof of the cover and slots.** The nontrivial factor in
\(P(A,A-u)=P(A,A-u')\) is
\[
 u^2+uu'+u'^2=1,
\]
which is equivalent to (13). Subtracting and adding u,u' gives (15).
Equations (14) then give the two row identities of the conic frame.

The map u:E_c to the projective line has degree three and three simple
poles, at (6). For u equal to either \(+2/\sqrt3\) or \(-2/\sqrt3\),
the equation for v is
\[
 v^3+v=u^3+u-c.
\]
It has three distinct complex roots: a repeated root would be
\(v=\pm i/\sqrt3\), whose critical value \(v^3+v\) is nonreal,
whereas the right side is real. At each of these six points u is a local
coordinate (the partial derivative with respect to v is nonzero), so
4-3u^2 has a simple zero. It has a pole of order two at each of the three
points (6), and no other zeros or poles. The six odd valuations show
that it is not a square in the function field. Thus the cover is
connected, branched at exactly six points, and unramified over the
three poles. Riemann--Hurwitz gives
\[
 2g(\mathcal D_c)-2=2(2\cdot1-2)+6=6,
\]
so its genus is four. Above each of the three poles there are two
points. The functions u and u' have simple poles at all six: their
leading ratio is \((-1\pm\sqrt{-3})/2\), never zero. The cubic
leading term of A is unaffected by subtracting any of the linear
terms in (14). All four slots therefore have pole order three at each
of six points, giving degree eighteen. \(\square\)

The real and degeneracy conditions are part of the construction, not
optional corrections after counting:

- Real completion requires \(|u|\le2/\sqrt3\). Generic real points
  outside this interval have no real lift.
- Distinct columns require u' different from u. Their coincidence can
  occur only at u^2=1/3.
- Distinct rows require u+u' nonzero. Its failure occurs at u^2=1
  with u'=-u.
- Four distinct actual scalars further require u and u' both nonzero.
  Together these conditions are sufficient, as all six pairwise scalar
  differences in (14) are among +/-u, +/-u', +/-(u+u'), +/-(u'-u).
- W=0 gives one double choice of u', rather than two choices. It does
  not by itself force a degenerate frame. Poles are never usable inputs.

Over a generic point there are two complex frame completions. Requiring
A'=B as well as the fixed second output w returns exactly the finite
locus TC-G2. No assertion that all six scalars of two arbitrary frames
are rational functions on E_c is being made.

**PROVED, precise global limitation.** There is no nonconstant morphism
from any smooth genus-one curve to \(\mathcal D_c\): Riemann--Hurwitz
would read 0=6 deg(map)+ramification, which is impossible. In particular
one cannot choose (13) rationally on E_c, or rationally after replacing
E_c by an elliptic isogeny source. A rational map between smooth
projective curves extends to a morphism, so restricting to a nonempty
affine open does not evade this conclusion.

More explicitly, let alpha:E' to E_c be an isogeny of degree e and
compose it with any translation. In characteristic zero the isogeny
is unramified. The pullback of (13) has 6e simple branch points. It is
connected because its radicand has odd valuations, and its normalized
genus is 1+3e. Thus passing to a low-degree isogeny increases, rather
than removes, this particular branch-choice cost.

These are global rational-parametrization statements. They give no
upper bound on the number of isolated real or algebraic compatible
points, and do not exclude a finite torsion coincidence. They also do
not classify automorphisms of the cover.

## TC-G5. Exact same-center different-width attachment

**PROVED.** There is a unique unordered pair of distinct positive widths
for two nondegenerate frames with the same center q, the same ordered
outputs, and at least two shared actual scalars. Write h1<h2, put
\[
 k=\sqrt2-1,\quad H=h_2,\quad
 H^2=\frac1{6-2\sqrt2}=\frac{3+\sqrt2}{14},\quad h_1=kH,
\]
\[
 s_2=h_1,\qquad s_1=H\sqrt{4\sqrt2-3}.                     \tag{16}
\]
The common output gap is
\[
 c=8h_1(1-2h_1^2)=8H(1-2H^2)>0.                           \tag{17}
\]
Their actual scalar union is
\[
 \{q\pm h_1,q\pm H,q\pm s_1\},                            \tag{18}
\]
of size six. The controlled ordered pairs are exactly the disjoint union
\[
 \{q\pm h_1\}\mathbin\times\{q\pm s_1\}
 \ \cup\ \{q\pm H\}\mathbin\times\{q\pm h_1\}.            \tag{19}
\]
There are eight distinct pairs, with exactly two selected outputs
\(2q\pm c/2\), each realized by four pairs with two distinct first
coordinates. The two frames share exactly the two actual scalars
q+/-h1. This is a finite compatible attachment, not a scalable family.

**Proof and uniqueness.** Equal positive output gaps for unequal positive
widths imply, after dividing H(h2)-H(h1) by h2-h1,
\[
 h_1^2+h_1h_2+h_2^2=1/2.                                  \tag{20}
\]
At a common center, equality of one nonzero signed scalar also gives
equality of its opposite. Same-type coincidences h1=h2 or s1=s2 force
the widths equal. Hence a different-width attachment must have h1=s2
or h2=s1. With k=h1/h2 in (0,1), the first choice combines (20) and
\(h_1^2+3h_2^2=1\) to give k^2+2k-1=0, hence (16). The second
choice combines (20) and \(3h_1^2+h_2^2=1\) to give
k^2-2k-1=0, with no root in (0,1). This exhausts the possible common-center
role assignments. Equation (16) gives 0<h1<H<s1 and both conic equations.
Thus all six scalars in (18) are distinct, all four scalars within each
frame are distinct, and the pair sets (19) are disjoint because their
first coordinates are disjoint. The row identity (9) proves the exact
output count and multiplicities. \(\square\)

The algebraically selected four compatible elliptic points are
\[
 \{\pm R_1,\pm R_2\},\quad
 R_i=(44-96h_i^2,288s_i(1-2h_i^2)).                         \tag{21}
\]
They exhaust the real locus TC-G2 for this c because there are already
two distinct admissible positive d values, and TC-G2 permits at most two.
Their scalars are exactly those of (19), by (11). All numbers are fixed
algebraic reals defined by positive square roots in (16). One can take
q=0 by common translation, since P(q+x,q+y)=2q+P(x,y).

The finite selected-pair ledger is N=6, Q=8, Z=2, uncovered B=28 and
safe full-image upper bound Z+B=30. The two selected fiber sizes are
exactly four within the controlled set; actual full-square fibers may
contain further pairs. The ratios are 2Q/N=8/3, Q/Z=4 and Q/N^2=2/9.
There is no growing parameter, no asserted positive exponent, and no
claim that selected Z is the entire image. In particular this finite
seed does not pass the project's asymptotic quantitative gate.

## TC-G6. Limited torsion and division consequences

**PROVED.** For a marked point (10), write t=h^2 in (0,1/3). Its tangent
slope and doubled X-coordinate are
\[
 m_R=\frac{2(5-12t)}{\sqrt{1-3t}},\qquad
 X(2R)=\frac{12(1-2t)}{1-3t}.                              \tag{22}
\]
The point is not of order two. It has order three exactly when
\[
 72t^2-51t+8=0,
\]
whose unique root in the admissible interval is
\(t=(17-\sqrt{33})/48\). These formulas follow directly from the
chord/tangent law: the Y-coordinate in (10) is nonzero, and X(2R)=X(R)
is equivalent to the displayed quadratic. If equal X held with 2R=R,
then R=O, impossible, so equal X indeed means 2R=-R.

For the two-width seed (16), each of R2-R1 and R2+R1 is nonzero and
is not of order two. Otherwise 2R2 would equal +/-2R1. But the function
in (22) is strictly increasing in t, with derivative
\(12/(1-3t)^2\), so its values at the unequal h_i^2 cannot coincide.
This is not a determination of their order. The separately authorized
[exact finite audit](exact-results.json) now checks both parameter cases
and n=2,3,4. For each n, the entire admissible locus has empty intersection
with [n]^{-1}(R1), and no translation from R1 to another admissible point
has exact order n. Thus R2-R1 and R2+R1 in the two-width case have none
of orders two, three, or four. The computation uses exact field arithmetic
and retains all tested multiples; its source and outputs have been read
after execution. This appendix did not rerun it. Higher orders remain
**OPEN**. The finite audit is not a torsion classification or an asymptotic
experiment.

**PROVED consequence of those bounded exclusions.** If alpha:E' to E_c
is any real isogeny, then
\[
 \alpha(P+T)=\alpha(P)+\alpha(T),\qquad
 [n]T=O\ \Longrightarrow\ [n]\alpha(T)=O.
\]
Hence under an isogeny followed by a fixed translation, a source torsion
step of order n can give only a target shift whose order divides n.
For n=2,3,4 every nontrivial divisor is among the tested orders. Therefore
no such source step, at any isogeny degree, moves the chosen base image
R1 to another admissible marked destination in either audited case. A
step killed by alpha gives the same target point and no new target slots.
This is only the specified base-point attachment test; no exclusion of
higher-order torsion or all finite isogeny correspondences follows.

**PROVED, global slot identity only.** A nonzero real translation T on
E_c cannot give an identity slot_i(R+T)=slot_j(R), for any two of the
three slots (5). Such an identity would preserve their pole support (6).
Its unique real member O would have to be fixed by T, so T=O. Likewise
an identity between a degree-nine slot pulled back by an isogeny of
degree e and a degree-nine slot on its source forces 9e=9. This only
excludes that explicit type of rational-function identity. It does not
exclude finite matches such as (19), or identities involving a further
cover. This is the checked specialization of the pole/degree reasoning
in imported B-MAP, with the present curve's different sign and poles.

**PROVED, actual real division count.** E_c(R) is connected for real
c nonzero. The cubic in (2) has critical points -4 and 4, with values
-432c^2 and -256-432c^2, both negative. It therefore has one real root.
The two real affine branches join at that root and at O, giving one
smooth compact circle. Its invariant differential dX/(2Y) is real and
nowhere zero, including these two join points. Integration modulo its
nonzero period identifies this connected one-dimensional group with
R/(period)Z: translation invariance of the differential makes addition
additive, and integration once around the circle has degree one. Thus
for every integer n>=1, [n] has exactly n real preimages of every real
elliptic point, not n^2. Intersecting such a fiber with the actual paired-row
locus still gives at most four points (or at most two for (12)). Removing
poles or inadmissible frames can only reduce usable counts. No real
division-point count alone supplies an image estimate for an actual
scalar square.

## Provenance, scope, and retained gap

TC-G1--TC-G6 concern the fixed T01 polynomial and the stated real conic
frame mechanism. Their proof evidence consists of the displayed algebra,
pole divisors, and Riemann--Hurwitz arguments. EG-C1 supplies the existing
Weierstrass template, specialized and checked here; CP-C1 supplies the
frame identity, expanded again here. B-CP is an imported complete
seed-specific attachment obstruction. Its five imported Bezout products
have now passed the separately executed coefficientwise audit. That run
used 652 checks and 144 P evaluations in total, including two exact
evaluations per pair in each of the two six-scalar squares. This appendix's
author reviewed the program and read its recorded results without rerunning
it; the result file retains the pre-execution proof hash. No rank assertion, torsion classification,
literature novelty claim, or new full-square computation is included.

The surviving six-scalar object (16)--(19) is a finite attachment with
both endpoint reuse and output reuse. Its fixed-c compatible locus is
finite, so torsion or division on that one curve cannot turn it into an
unbounded family of distinct compatible widths. The genus-four cover
explains why a general sharing point does not supply a rationally chosen
full frame on an elliptic source. Neither fact rules out every possible
collision pattern. The original same-set power-saving target is OPEN.
