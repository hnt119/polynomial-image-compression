# Technical proof appendix: the torsion/frame cycle

T01 · 11 October 2026 · documentation freeze, version 1.

## A1. Sharing maps and the fixed-output locus

All results below are reproduced from the identified sources, with notation explained and scopes retained. This freeze does not add an independent mathematical recertification. PROVED denotes the supplied source-system status.

### PROVED / TC-G1: coordinate model

Fix real z > w, c = z-w, and let r = c<sub>+</sub>(z,u), b = c<sub>+</sub>(w,v), D = c<sub>-</sub>(z,u) = c<sub>-</sub>(w,v). Here c<sub>±</sub>(z,u) = (z-u³±u)/2. Put d = u-v and ℓ = u+v. The sharing identity becomes

\[
d(3\ell^2+d^2+4)=4c,\quad X=12c/d-4,\quad Y=36c\ell/d.
\]

\[
d=12c/(X+4),\quad\ell=Y/(3(X+4)),\quad u=(\ell+d)/2,\quad v=(\ell-d)/2.
\]

Substitution gives E<sub>c</sub>: Y² = X³-48X-128-432c², with discriminant Δ = -2¹²3⁶c²(16+27c²) ≠ 0. This certifies smoothness. At X = -4 the right side is -432c², so this exceptional denominator has no real zero on E<sub>c</sub>.

The three points at infinity of the plane sharing cubic are smooth. They correspond to O and (-4,±12c√(-3)). The functions u,v have simple poles there; each scalar slot r,b,D has pole order three at each and hence degree nine. Only O is real. A function’s degree is the number of generic complex preimages, equivalently its total pole order.

### PROVED / TC-G2: keeping both rows is an extra condition

The row difference r-b = d determines X. Distinct elliptic points with these rows must therefore be R and -R, and negation sends (u,v) to (-v,-u). Equality of r at those points is precisely

\[
(u+v)(u^2-uv+v^2-1)=0.
\]

The first factor gives Y = 0 and R = -R, not two columns. The second factor, together with the sharing equation, gives

\[
3d^2+\ell^2=4,\quad 2d^3-4d+c=0,\quad\ell\ne0.
\]

The original real equation forces d > 0, and ℓ ≠ 0 gives d < 2/√3. The derivative of 4d-2d³ changes sign only once on that interval, so there are at most two d values. Exclude d² = ℓ² = 1 to avoid equal row and column scalar sets. Put h = d/2 and s = |ℓ|/2. The frame center is q = (z+w)/4 and its marked points are

\[
R_\pm=(44-96h^2,\ \pm288s(1-2h^2)),\quad 3h^2+s^2=1.
\]

**Meaning → limitation.** Each positive width has two column choices encoded by ±R, not two different frames. Fixed z,w give at most two widths/four points. Only fixing c leaves a free scalar translation of q. No arbitrary network classification follows.

## A2. The completion cover and its exact scope

### PROVED / TC-G4: branch count before genus

Keep one row r with output z. Factoring P(r,r-u) = P(r,r-u′) gives (u-u′)(u²+uu′+u′²-1) = 0. The nontrivial branch is

\[
u^{\prime}=(-u+W_{\mathrm{cov}})/2,\quad W_{\mathrm{cov}}^2=4-3u^2.
\]

The normalization D<sub>c</sub> is the smooth projective curve obtained from this double cover of E<sub>c</sub>. The map u has degree three and three simple poles. At either u = ±2/√3, v satisfies v³+v = u³+u-c. A repeated root would have v = ±i/√3 and a nonreal critical value v³+v, while the right side is real. Thus there are three distinct v values at each sign, and u is a local coordinate at all six points.

The radicand has six simple zeros and three poles of order two. A square of a rational function has only even zero and pole orders. Hence the radicand is not a square, the cover is connected, and precisely the six zeros are branch points. Riemann-Hurwitz now gives

\[
2g(\mathcal D_c)-2=2(2g(E_c)-2)+6=6.
\]

For any degree-e isogeny E′ → E<sub>c</sub>, followed if desired by a translation, characteristic zero makes the map unbranched. The six branch points pull back to 6e distinct simple zeros. Their odd orders keep the pulled-back double cover connected, and its genus is 1+3e.

### What the scalar formulas do and do not preserve

\[
r,\quad D=r-u,\quad D^{\prime}=r-u^{\prime},\quad r^{\prime}=r-u-u^{\prime},
\]

\[
q^{\prime}=r-(u+u^{\prime})/2,\quad h^{\prime}=(u+u^{\prime})/2,\quad s^{\prime}=(u^{\prime}-u)/2.
\]

These slots satisfy 3h′²+s′² = 1, with outputs z and 4q′-z. Each slot has degree eighteen on D<sub>c</sub>: there are six points above the old poles, and the cubic term of r gives pole order three at each. The linear subtractions do not cancel it. The second row need not be b, and the second output need not be w.

Real completion requires |u| ≤ 2/√3. Four distinct scalars require u, u′, u+u′ and u′-u all nonzero; poles are removed. These conditions list all pairwise differences. A zero value of W<sub>cov</sub> gives one branch choice and does not alone force scalar coincidence.

### The obstruction concerns rational functions, not isolated points

A nonconstant rational map between smooth projective curves extends over its missing points. A genus-one source mapping to D<sub>c</sub> would violate Riemann-Hurwitz: 0 = 6m + R with m ≥ 1 and R ≥ 0. This excludes choosing the extra branch rationally on an elliptic source, including after an isogeny. It neither counts nor excludes isolated real/algebraic lifts. Imposing r′ = b and the original w instead recovers A1’s separate finite-locus theorem.

## A3. The exact attachment, field and marked shift

### PROVED / TC-G5 and MS-C1: fixed conventions

\[
a=\sqrt2,\quad\lambda=(3+a)/14,\quad H=\sqrt\lambda>0,\quad W=\sqrt{4a-3}>0.
\]

Here W is the fixed radical of TC-G5/MS-C1, not the variable cover coordinate W<sub>cov</sub> in A2. Set h<sub>1</sub> = (a-1)H, h<sub>2</sub> = H, s<sub>1</sub> = HW, s<sub>2</sub> = h<sub>1</sub>, c = 8H(4-a)/7 and q = c/4. Then c² = 64(19-3a)/343 and E<sub>c</sub> is defined over F<sub>0</sub> = Q(a).

The positive-Y marked points and their group difference are exactly

\[
R_1=((68+144a)/7,\ 288HW(2+3a)/7),
\]

\[
R_2=((164-48a)/7,\ 288H(5a-6)/7),
\]

\[
X(T)=[110+102a+(54+18a)W]/7,
\]

\[
Y(T)=H[1368+540a+(792+684a)W]/7.
\]

The chord through R<sub>2</sub> and -R<sub>1</sub> has slope m<sub>T</sub> = 3H[a-2-(a+2)W]. The formulas X(T) = m<sub>T</sub>²-X(R<sub>1</sub>)-X(R<sub>2</sub>) and Y(T) = m<sub>T</sub>(X(R<sub>2</sub>)-X(T))-Y(R<sub>2</sub>) give these signs. The preserved referee appendix records the full expansion.

### Why the needed automorphism exists

Put F = F<sub>0</sub>(H), L = F(W). For F<sub>0</sub>, the quadratic norm multiplies the conjugates a ↦ ±a, so N(r+sa) = r²-2s² for rational r,s. The source’s square-class calculation is

\[
N(\lambda)=1/28,\quad N(4a-3)=-23,\quad N((4a-3)/\lambda)=-644.
\]

The first value is not a rational square, so [F:F<sub>0</sub>] = 2. Neither of the last two values can be the norm of a square. If 4a-3 = (x+yH)² with x,y ∈ F<sub>0</sub>, the H coefficient forces 2xy = 0, contradicting one of those two tests. Thus [L:Q] = 8. The point coordinates recover a, then H, then W; L is their exact joint coordinate field. No minimal-field claim for T alone is required.

\[
\sigma(a)=a,\quad\sigma(H)=H,\quad\sigma(W)=-W,\quad T+\sigma(T)=2R_2.
\]

**Meaning → limitation.** This valid automorphism fixes R₂ and negates R₁. If T were torsion, 2R₂ would be torsion. It reduces the one marked-point question to R₂, without a rank or whole-group classification.

## A4. The one-prime valuation certificate

### PROVED / MS-C1: all arithmetic hypotheses at p = 23

For a rational number, v<sub>p</sub> is the exponent of p in its factorization, normalized by v<sub>p</sub>(p) = 1. Extend it to Q<sub>p</sub>, the completion for the size p<sup>-vₚ</sup>. The ring Z<sub>p</sub> consists of elements of valuation at least zero; its units have valuation zero. Reduction takes an integral element to its residue modulo p.

\[
F\hookrightarrow\mathbb Q_{23},\qquad a\equiv18,\quad H\equiv6\pmod {23}.
\]

The root 18 of a²-2 has nonzero derivative 36 modulo 23. After lifting a, λ = (3+a)/14 has residue 13, and 6 is a simple root of H²-λ with derivative 12. Simple-root lifting means that a root known modulo 23<sup>n</sup> has a unique next digit cancelling its error modulo 23<sup>n+1</sup>. The compatible digits converge in Z<sub>23</sub>. They define the displayed field embedding. It need not respect the ordering of the original real field, and W need not embed in Q<sub>23</sub>.

**Good reduction** means that the integral model remains nonsingular modulo 23. For this short equation it is certified by its discriminant being a unit:

\[
\Delta=-2^{12}3^6c^2(16+27c^2),\quad c^2\equiv16,\quad16+27c^2\equiv11.
\]

### A fixed doubling, not an order search

The tangent slope at R<sub>2</sub> is H(16a-4). Applying the group law once gives the source identity

\[
S=2R_2=(48+24a,-16H(281+208a)/7).
\]

\[
(281+208a)(281-208a)=-7567=-7\cdot23\cdot47.
\]

At the chosen embedding, 281+208a has residue 0 and 281-208a has residue 10. Since the latter is a unit and the product has valuation one, v<sub>23</sub>(281+208a) = 1 exactly. The factors 16,H,7 are units, so v<sub>23</sub>(Y(S)) = 1. Further, X(S) ≡ -3 and 3X(S)²-48 ≡ 2.

\[
\mu=(3X(S)^2-48)/(2Y(S)),\quad v_{23}(\mu)=-1,
\]

\[
U=4R_2,\quad X(U)=\mu^2-2X(S),\quad v_{23}(X(U))=-2.
\]

The two terms of X(U) have valuations -2 and 0, so cancellation is impossible. The denominator is nonzero, so U is a finite point. The following local lemma excludes torsion at every possible order.

**Scope.** Exactly one prime is used. The factor 47 is part of an integer norm identity, not a second local test. This freeze reproduces the saved equalities; no arithmetic program or division search is run.

## A5. Why the formal logarithm excludes all orders

### PROVED / supplied EG-C2 lemma, applied in MS-C1

**Meaning and statement.** Near O, the elliptic group can be mapped injectively enough for torsion detection into an additive field of characteristic zero. If p ≥ 5 and y² = x³+Ax+B has A,B ∈ Z<sub>p</sub> and unit discriminant, every finite Q<sub>p</sub>-point with v<sub>p</sub>(x) < 0 has infinite order.

**Proof.** Use local coordinates t = -x/y and w = -1/y at O. The equation is w = t³+Atw²+Bw³. Recursive coefficient comparison gives w(t) ∈ t³Z<sub>p</sub>[[t]], with w = t³+O(t⁷). The smooth integral group law has an integral local power series F(t<sub>1</sub>,t<sub>2</sub>) = t<sub>1</sub>+t<sub>2</sub>+ terms of higher degree. Thus t ∈ pZ<sub>p</sub> describes a subgroup near O.

An invariant differential is a differential unchanged by translation in the group. Here it is dx/(2y); in t it has integral expansion

\[
\omega=\frac{t w^{\prime}(t)-w(t)}{2w(t)}dt=\left(1+\sum_{j\ge1}a_jt^j\right)dt,\quad a_j\in\mathbb Z_p.
\]

For completeness, invariance is verified in the supplied proof by translating with a fixed point (r,s): m = (y-s)/(x-r), x′ = m²-x-r, y′ = -y+m(x-x′). The identity 3x²+A-2my = (x-r)(2x+r-m²), followed by differentiation, gives dx′/(2y′) = dx/(2y). Regularity extends this across exceptional chord denominators.

The **formal logarithm** is the termwise integral of this power series, normalized to vanish at O:

\[
\log_E(t)=t+\sum_{j\ge1}\frac{a_j}{j+1}t^{j+1}.
\]

If v<sub>p</sub>(t) = r ≥ 1, each later term has valuation at least (j+1)r-v<sub>p</sub>(j+1) > r, and these bounds tend to infinity. Indeed, for k = v<sub>p</sub>(j+1), p<sup>k</sup> ≤ j+1 and p<sup>k</sup> ≥ 1+(p-1)k give k ≤ j/(p-1) < j. The series converges and its leading term cannot cancel: v<sub>p</sub>(log<sub>E</sub>(t)) = r.

Invariance of ω gives log<sub>E</sub>(F(t<sub>1</sub>,t<sub>2</sub>)) = log<sub>E</sub>(t<sub>1</sub>)+log<sub>E</sub>(t<sub>2</sub>). A nonzero torsion parameter would therefore give n log<sub>E</sub>(t) = 0 with log<sub>E</sub>(t) ≠ 0 in characteristic zero, a contradiction.

Finally, if v<sub>p</sub>(x) = -b < 0, x³ strictly dominates Ax and B. Hence 2v<sub>p</sub>(y) = -3b; write b = 2r, so v<sub>p</sub>(t) = r ≥ 1. This is exactly the subgroup just treated. Applying the lemma to U = 4R<sub>2</sub> at p = 23 proves R<sub>2</sub>, and then T by T+σ(T) = 2R<sub>2</sub>, have infinite order.

**Limitation.** This is a local torsion criterion on the specified good model over Q<sub>p</sub>. It is not a torsion classification over arbitrary ramified extensions. Source: EG-C2, reproduced with checked hypotheses in MS-C1 arithmetic §5 and the saved referee audit.

## A6. Source and status ledger

The following identifiers locate complete supplied arguments or retained finite evidence. The chronology is TC checkpoint, then MS certificate, then this documentation freeze. All companions required for this report are present. Older migration gaps are not used as proof dependencies.

| Claim / frozen status | Meaning and precise source scope |
| --- | --- |
| TC-G1 / PROVED | One common column; geometry.md TC-G1 in source [TC]. |
| TC-G2 / PROVED | At fixed z,w, at most two admissible widths/four real marked points; [TC], TC-G2. |
| TC-G4 / PROVED | General one-row completion has genus 4; isogeny pullback genus 1+3e; [TC], TC-G4. |
| TC-G5 / PROVED | Exact finite attachment; N=6, Q=8, Z=2, B=28; [TC], TC-G5. |
| TC-X1 / EXPERIMENTAL | Retained exact, exhaustive finite audit: full image 30; 28 singleton fibers and two size-4 fibers; [TC], exact-audit.md §4. |
| MS-C1 / PROVED | The specified T has infinite order; [MS], arithmetic.md §§1-5. Recorded independent internal review: referee-audit.md. |
| TC-O1 / RESOLVED | Former OPEN status in [TC] is historical and superseded by MS-C1. Earlier files remain unchanged. |
| T01 / OPEN | Arbitrarily large same-set real squares with a fixed positive image exponent saving. No construction is supplied. |

### Source locators, versions and evidence

**[TC]** research/notes/2026-10-11-torsion-compatible-sharing/. README.md, version 1; geometry.md, version 2; exact-audit.md and verification.md, version 1; exact-results.json. Titles: *Torsion compatible sharing and the finite frame obstruction* and its companions. The saved exact_audit.py is preserved and not executed.

**[MS]** research/notes/2026-10-11-marked-shift-certificate/. README.md, arithmetic.md, referee-audit.md and verification.md, all version 1. Title: *Infinite order certificate for the marked bridge shift*. The prior internal arithmetic and referee audits are source evidence, not external review and not a new audit by this freeze.

**[EG]** research/notes/2026-09-30-elliptic-geometry/complex-extensions.md, EG-C2 local formal-logarithm lemma. Its full argument is reproduced in [MS], arithmetic.md §5. Only this earlier local criterion is needed here.

### Preservation and unresolved boundary

The standalone source-status-ledger.md supplies source links and SHA-256 hashes. Earlier proofs are preserved. This freeze checks exposition, availability and rendering only; it does not rerun the finite audit. The original cubic target remains OPEN. No successor task is adopted.
