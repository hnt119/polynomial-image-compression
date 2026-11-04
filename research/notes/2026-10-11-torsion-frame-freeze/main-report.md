# Torsion, sharing and complete frames

T01 · 11 October 2026 · documentation freeze, version 1.

## Torsion, sharing and complete frames

**MS-C1: PROVED in the supplied source system.**
The marked shift T = R<sub>2</sub> - R<sub>1</sub> has infinite order. TC-O1 is resolved. The cubic image problem remains OPEN.

This report freezes the completed torsion/frame cycle. It explains the existing arguments for a reader with basic group and Galois theory. It is an editorial synthesis, not a new proof audit, computation or literature claim.

### The fixed target

\[
P(x,y)=(x-y)^3+x+y,\qquad |P(A,A)|\le |A|^{2-\varepsilon}.
\]

Here A is one finite real set used in both coordinates, and ε > 0 must be fixed while |A| becomes arbitrarily large. The image includes every ordered pair in A². No result in this cycle supplies that construction.

### Geometry vocabulary used below

**Genus** is the number of handles of the compact Riemann surface (a real two-dimensional surface) associated with a curve. We add points at infinity and take the smooth model resolving singularities, its **normalization**. A **cover** is a finite algebraic map of curves; its degree counts the points in a generic complex fiber. A **branch point** is a point of the base where these sheets merge.

An **elliptic curve** is a smooth genus-one curve with a chosen identity O and a group law. On the displayed Weierstrass model, -(X,Y) = (X,-Y). The symbols [n]R and R-S mean group multiplication and subtraction, not coordinate operations. A point is **torsion** if [n]R = O for some positive n; otherwise it has infinite order.

An **isogeny** is a nonconstant algebraic group homomorphism between elliptic curves. Its degree e is the number of points in a generic complex fiber. In characteristic zero it has no branch points.

### Reading guide and source status

Pages 2-3 separate the two geometric restrictions. Page 4 gives the exact finite attachment and its full-square cost. Page 5 explains the all-orders certificate and closure. The companion appendix retains the detailed calculations and source/status ledger.

PROVED means a complete identified argument in the supplied source system. EXPERIMENTAL means retained exact finite evaluation. The earlier internal audits are reported as such; this freeze checks source fidelity and document presentation only.

## One column is not a frame

### PROVED / TC-G1: what an elliptic point supplies

**Meaning.** A sharing point supplies two output pairs with one common second coordinate. Fix ordered real outputs z > w and write c = z-w > 0. For an output z and difference u = x-y define

\[
c_\pm(z,u)=(z-u^3\pm u)/2,\qquad P(c_+(z,u),c_-(z,u))=z.
\]

**Equation.** Equality of the second coordinates gives the curve C<sub>c</sub>. Its smooth genus-one model is E<sub>c</sub>:

\[
C_c:u^3-v^3+u-v=c,\qquad E_c:Y^2=X^3-48X-128-432c^2.
\]

**Proof.** Put d = u-v, ℓ = u+v. The change X = 12c/d - 4, Y = 36cℓ/d gives E<sub>c</sub>. Its three scalar slots are r = c<sub>+</sub>(z,u), b = c<sub>+</sub>(w,v), D = c<sub>-</sub>(z,u) = c<sub>-</sub>(w,v). Thus P(r,D) = z and P(b,D) = w. The appendix records the inverse and nonzero discriminant.

**Limitation.** These are three scalar slots and two pairs. No second column, and hence no complete frame, has yet been supplied.

### PROVED / TC-G2: fixed ordered outputs leave a finite locus

**Meaning.** A frame is the four selected ordered pairs {q±h} × {q±s}, with h,s > 0, h ≠ s and 3h²+s² = 1. Both columns give output z in the upper row and w in the lower row. The outputs fix q = (z+w)/4.

\[
3d^2+\ell^2=4,\qquad 2d^3-4d+c=0,\qquad d=2h,\ \ell=\pm2s.
\]

**Proof.** A second point with the same ordered rows has the same d, hence the same X. It must be the negative elliptic point. Equality of the rows then imposes the first equation; substituting in C<sub>c</sub> gives the second. On 0 < d < 2/√3, the function 4d-2d³ increases and then decreases, so it takes any value at most twice. Each width gives the two signs of ℓ, which exchange its columns.

**At most two widths, hence at most four real marked points.** Exclude ℓ = 0 and d² = ℓ² = 1 for four distinct scalars.

**Limitation.** This is a theorem for these complete CP frames at fixed ordered outputs. Fixing only their gap permits scalar translations of the center. Arbitrary networks and varying output pairs are outside the theorem.

## Completing one row needs a cover

### PROVED / TC-G4: a branch choice is additional geometry

**Meaning.** Start with a general point of E<sub>c</sub>, giving the pair (r,D) of output z and difference u = r-D. We now seek a distinct second column D′ with that same row and output. This requirement is weaker than preserving both original rows and both outputs.

\[
u^2+uu^{\prime}+u^{\prime 2}=1,\qquad u^{\prime}=(-u+W_{\mathrm{cov}})/2,\quad W_{\mathrm{cov}}^2=4-3u^2.
\]

Here u′ = r-D′. The variable W<sub>cov</sub> is the cover coordinate, denoted W in TC-G4. It is separate from the fixed positive radical W in the finite attachment. The completed rows are r and r-u-u′; the columns are r-u and r-u′. Its center is q′ = r-(u+u′)/2, and its other output is 4q′-z, which need not equal w.

**Proof.** Factor the equality P(r,r-u) = P(r,r-u′) and remove the trivial factor u-u′. The remaining quadratic gives the displayed square root. On E<sub>c</sub>, u has three simple poles. The radicand 4-3u² has six simple zeros, above u = ±2/√3, and three poles of order two. The odd orders at its zeros make the double cover connected and branched at exactly six points.

The **Riemann-Hurwitz formula** counts the effect of sheets and branching on genus. For a degree-m map C → B it says 2g(C)-2 = m(2g(B)-2) + R, where R is the sum of local branching contributions. A simple branch contributes one. Thus

\[
2g(\mathcal D_c)-2=2(2\cdot1-2)+6=6,\qquad g(\mathcal D_c)=4.
\]

After a degree-e isogeny, even followed by a translation, each branch point has e distinct preimages. The connected normalized pullback has 6e branch points and genus 1+3e. A rational choice of completion on an elliptic source would give a nonconstant map from genus one to genus four; Riemann-Hurwitz would require 0 = 6m + R, impossible.

**Limitation.** This excludes the stated rational elliptic completion. It does not exclude isolated real or algebraic lifts, nor all sharing constructions.

A real lift needs |u| ≤ 2/√3. Four distinct scalar slots further require u, u′, u+u′ and u′-u all nonzero, with poles removed. The branch value W<sub>cov</sub> = 0 is not itself a ban on a frame. Requiring also the original second row b and output w returns to the finite locus on page 2.

Source: TC-G4. The six-branch argument, not the degree of the displayed equation alone, determines the genus.

## Eight controlled pairs in a 36-pair square

### PROVED / TC-G5: an exact different-width attachment

**Meaning.** Two nondegenerate frames can reuse two actual scalars and enlarge both output fibers. All the following roots are positive real roots:

\[
a=\sqrt2,\quad H=\sqrt{(3+a)/14},\quad W=\sqrt{4a-3},
\]

\[
h_1=(a-1)H,\quad h_2=H,\quad s_1=HW,\quad s_2=h_1,
\]

\[
c=8H(4-a)/7,\quad q=c/4,\quad A=\{q\pm h_1,q\pm H,q\pm s_1\}.
\]

| First coordinate | Second coordinates | Output |
| --- | --- | --- |
| q+h<sub>1</sub> | q-s<sub>1</sub>, q+s<sub>1</sub> | c |
| q-h<sub>1</sub> | q-s<sub>1</sub>, q+s<sub>1</sub> | 0 |
| q+H | q-h<sub>1</sub>, q+h<sub>1</sub> | c |
| q-H | q-h<sub>1</sub>, q+h<sub>1</sub> | 0 |

**Proof.** Equal output gaps for h<sub>1</sub> < h<sub>2</sub> give h<sub>1</sub>²+h<sub>1</sub>h<sub>2</sub>+h<sub>2</sub>² = 1/2. At a common center, two shared scalars force a cross-width equality. The admissible choice h<sub>1</sub> = s<sub>2</sub> gives k²+2k-1 = 0 for k = h<sub>1</sub>/h<sub>2</sub>, hence k = √2-1. The displayed constants satisfy both conic equations and 0 < h<sub>1</sub> < H < s<sub>1</sub>. The six scalars and eight listed pairs are distinct.

### Whole-square accounting: selected pairs are not the square

Let E be the listed pairs. Write N = |A|, Q = |E|, Z = |P(E)| and B = N²-Q. Every unlisted pair may add an output, so |P(A,A)| ≤ Z+B.

| N | Q | Z | B | Z+B | Actual image |
| --- | --- | --- | --- | --- | --- |
| 6 | 8 | 2 | 28 | 30 | 30 |

**EXPERIMENTAL / TC-X1, exact and exhaustive for this fixed set.** The retained full-square audit gives two fibers of size four and 28 singleton fibers: 2·4 + 28 = 36 pairs and 2 + 28 = 30 outputs. No evaluation is rerun for this freeze.

\[
2Q/N=8/3,\qquad Q/Z=4,\qquad Q/N^2=2/9.
\]

**Limitation.** The new frame adds four cross-block pairs with new first coordinates and old scalars that were the first frame’s row coordinates. The other 28 square pairs remain uncontrolled by these fibers and in fact have singleton outputs. There is no growing parameter and no asymptotic saving.

## An all-orders certificate, with a finite scope

### Local arithmetic vocabulary

The **valuation** v<sub>23</sub> counts powers of 23: v<sub>23</sub>(23) = 1; negative values mean powers in a denominator. The field Q<sub>23</sub> completes Q for this notion of closeness. Its integral elements form Z<sub>23</sub>; a **unit** has valuation zero. **Good reduction** means an integral curve equation remains nonsingular modulo 23, here certified by a unit discriminant.

A **formal logarithm** is a convergent power series near O that turns elliptic addition into ordinary addition. The supplied lemma proves that, for a good integral model over Q<sub>p</sub> with p ≥ 5, a finite point with negative X-valuation has a nonzero logarithm and cannot be torsion.

### PROVED / MS-C1: the marked shift is of infinite order

**Meaning and exact object.** Use the constants on page 4, put F = Q(a,H), L = Q(a,H,W), and take the positive-Y marked points R<sub>i</sub> = (44-96h<sub>i</sub>², 288s<sub>i</sub>(1-2h<sub>i</sub>²)). The point T = R<sub>2</sub>-R<sub>1</sub> is their elliptic difference. The exact expanded coordinates are in Appendix A3.

**Proof, step 1.** The source proves [L:Q] = 8 and an automorphism σ fixing a,H and sending W to -W. It fixes R<sub>2</sub> and negates R<sub>1</sub>. Consequently

\[
T+\sigma(T)=2R_2.
\]

**Step 2.** Simple roots a ≡ 18, H ≡ 6 (mod 23) lift to an embedding F → Q<sub>23</sub>. The integral model has c² ≡ 16 and 16+27c² ≡ 11, so its discriminant -2¹²3⁶c²(16+27c²) is a unit. The local criterion applies here without adjoining W.

\[
S=2R_2=(48+24a,-16H(281+208a)/7).
\]

**Step 3.** The identity (281+208a)(281-208a) = -7·23·47 and the second factor’s nonzero residue give v<sub>23</sub>(Y(S)) = 1. Also 3X(S)²-48 ≡ 2. The tangent slope μ = (3X(S)²-48)/(2Y(S)) has valuation -1. Thus

\[
X(4R_2)=\mu^2-2X(S),\qquad v_{23}(X(4R_2))=-2.
\]

**Conclusion and limitation.** The local lemma makes R<sub>2</sub> infinite order. If T were torsion, so would be σ(T) and their sum 2R<sub>2</sub>, a contradiction. This is an all-orders proof, not a finite-order test.

**Settled in scope:** TC-O1, the fixed-output two-width classification, and the stated rational elliptic completion obstruction. **OPEN:** the unrestricted same-set cubic image target.

Infinite order makes the multiples [n]T distinct, so there are infinitely many real elliptic points. Yet the complete-frame conditions still select at most four marked points at these fixed ordered outputs. Extra elliptic points need not be frames. No new construction, rank claim, general torsion classification or successor task is adopted.
