# Torsion compatible sharing and the finite frame obstruction

T01 · 11 October 2026 · offline research, version 1.
Throughout, P(x,y)=(x-y)^3+x+y and both coordinates use one real set.

## Verdict

**PROVED:** the proposed points R± are correct, but a fixed sharing curve
has at most four admissible real points representing complete CP frames.
A general sharing point needs a double cover of genus four to acquire a
second same-output column. After an isogeny of degree e this cover has
genus 1+3e. Thus an elliptic torsion translation, with or without an
isogeny, cannot supply this completion as a nonconstant rational family.
These are correspondence obstructions, not a reopened global-factorization
argument or a scarcity theorem for isolated real points.

**PROVED finite compatibility:** a uniquely forced different-width pair
of frames reuses two endpoints and gives N=6, Q=8, Z=2, B=28. The
fixed-output geometry admits no third width. **EXPERIMENTAL, exact:**
its full image has 30 outputs; the preselected torsion orders 2,3,4 give
no compatible attachment in either tested case. This is a finite
attachment, not an unbounded family or a power-saving result.
**T01 remains OPEN.**

## Geometric model and actual compatibility

**PROVED — TC-G1/G2. Meaning:** membership in a sharing curve supplies
one common column; a complete two-column frame imposes another equation.
Fix real z>w and c=z−w. The sharing equation and maps are

\[
u^3-v^3+u-v=c,\quad d=u-v,\quad \ell=u+v,
\]
\[
E_c:Y^2=X^3-48X-128-432c^2,
\quad X=12c/d-4,\quad Y=36c\ell/d,
\]
\[
u=\frac{Y+36c}{6(X+4)},\qquad
v=\frac{Y-36c}{6(X+4)}.
\]
The actual scalar slots are
\[
a=c_+(z,u),\quad b=c_+(w,v),\quad
 y=c_-(z,u)=c_-(w,v).
\]
They satisfy P(a,y)=z and P(b,y)=w. Their maps each have degree nine;
they have three poles over the complex numbers, only one of them real.
Every finite real E-point is pole-free in these formulas.

**Statement and proof:** a second distinct point with the same ordered
rows a,b has the same d, hence the same X and is the negative point.
Equality of both row slots then requires
\[
3d^2+\ell^2=4,\qquad 2d^3-4d+c=0.
\]
Writing d=2h and \(\ell=\pm2s\) gives
\[
3h^2+s^2=1,\quad c=8h(1-2h^2),\quad
R_\pm=(44-96h^2,\ \pm288s(1-2h^2)).
\]
The frame center is forced to q=(z+w)/4. The admissible domain is
0<h<1/√3, s>0, h≠s. The cubic in h has at most two admissible
positive roots, so at most four real marked points; over the complex
numbers there are at most six candidate points. **Limitation:** none of
these counts classifies arbitrary sharing networks or varying output pairs.

## Why the additional slots need a cover

**PROVED — TC-G4. Meaning:** the missing column cannot be supplied by
quietly treating an algebraic branch as another rational elliptic slot.
For the row a with current difference u, a different difference u′ must obey
\[
u^2+uu'+u'^2=1,\qquad
u'=(-u+W)/2,\qquad W^2=4-3u^2.
\]
The two choices of W encode the two branches. The completed frame has
rows a and a−u−u′, and columns a−u and a−u′. These are actual scalar
formulas on the cover. Real membership and the nondegeneracy exclusions
are listed in [the geometry appendix](geometry.md).

**Proof:** u has three simple poles on E_c. The radicand has six simple
zeros, at u=±2/√3, and only even-order poles. For real c≠0 the corresponding
v-cubics have no repeated roots: their possible critical values are
nonreal. Thus the connected double cover has six branch points and genus
four by Riemann–Hurwitz. Pullback by a translated degree-e isogeny has
6e simple branch points and genus 1+3e. A nonconstant map from an elliptic
curve to either normalization would contradict Riemann–Hurwitz.
**Limitation:** finite division points can still lift, and the cover has
real points. The proof excludes a rational family of completions, not
all finite torsion incidences.

## Worked different-width attachment

**PROVED — TC-G5. Meaning:** two frames can share actual endpoints while
adding rows to both existing outputs, but fixed outputs exhaust the widths.
Define exact positive numbers
\[
\alpha=\sqrt2,\quad k=\alpha-1,\quad
H^2=(3+\alpha)/14,\quad W=\sqrt{4\alpha-3},
\]
\[
h_1=kH,\quad h_2=H,\quad s_1=WH,\quad s_2=h_1,
\quad c=8h_1(1-2h_1^2),\quad q=c/4.
\]
Use the two frames \(\{q\pm h_i\}\times\{q\pm s_i\}\). Their
union of scalar coordinates is
\[
A=\{q\pm h_1,q\pm h_2,q\pm s_1\}.
\]

| First coordinate | Two second coordinates | Output |
|---|---|---:|
| q+h₁ | q−s₁, q+s₁ | c |
| q−h₁ | q−s₁, q+s₁ | 0 |
| q+h₂ | q−h₁, q+h₁ | c |
| q−h₂ | q−h₁, q+h₁ | 0 |

**Proof:** equality of the two output gaps, for h₁<h₂, gives
h₁²+h₁h₂+h₂²=1/2. Two reused scalar endpoints force a cross-width
identification. The admissible one is h₁=s₂, and its equations reduce
to k²+2k−1=0. The displayed positive root yields exactly the constants
above. Direct substitution gives both conic equations. Since
0<h₁<h₂<s₁, all six scalars and all eight pairs are distinct. The new
four pairs have new first coordinates, use two old scalars, previously first coordinates,
and enlarge each selected output fiber from two to four.

The exact ledger is
\[
N=6,\quad Q=8,\quad Z=2,\quad B=28,\quad |P(A,A)|\le30,
\]
\[
2Q/N=8/3,\qquad Q/Z=4,\qquad Q/N^2=2/9.
\]
With the old frame as one scalar block and the two new rows as the other,
exactly four new pairs cross the blocks; the other four are retained local
pairs. **Limitation:** there are just two admissible widths at this fixed
output pair. No growing coverage or improvement over the earlier
N^(4/3) prescribed-pair benchmark follows.

## Division audit and whole square

The two parameter cases and marked base points are fixed before the scout:
the accepted CP seed, and the different-width attachment above. In each
case the base point is the positive-Y point of the smaller width. For
n=2,3,4, the audit intersects [n]⁻¹(R₁) with the entire admissible frame
locus and tests translations from R₁ to the other admissible points.
**EXPERIMENTAL — TC-X1, exact and exhaustive within this scope:** for
both cases and each n=2,3,4, the valid division intersection has M=0.
No distinct compatible destination is reached by a translation of order
2,3 or 4. The initial compatible loci have two and four points respectively;
these are separate from the empty division intersections. The original
six-scalar bridge also uses two different absolute output pairs. The
following ledgers concern the two initial scalar constructions, not new
scalars produced by division.

| Initial construction | N | Q | Z | B | Z+B | Full image | Full fiber histogram |
|---|---:|---:|---:|---:|---:|---:|---|
| Original CP seed | 6 | 8 | 3 | 28 | 31 | 29 | 24 singletons, 4 doubles, 1 quadruple |
| Different-width attachment | 6 | 8 | 2 | 28 | 30 | 30 | 28 singletons, 2 quadruples |

The new construction has exactly 28 singleton pairs: no unprescribed
cross-pair is omitted or credited to a large fiber. The one run used
144 P evaluations and 652 exact checks. Two independent cubic formulas
agreed on all 72 square cells. Exact coordinates and every full fiber
are in [the audit](exact-audit.md) and [retained data](exact-results.json).
The finite results assert nothing about higher torsion orders.

**PROVED implication:** an isogeny sends n-torsion to points killed by n,
since α(P+T)=α(P)+α(T). Thus the failed target shifts also exclude using
source torsion of orders 2,3,4 through any fixed isogeny and common offset
to connect these marked frames from the chosen base image. It does not
classify arbitrary isolated equations α(R₁)+T=R₂ with an untransformed
old frame, higher-order source torsion, or matches on other curves.

**PROVED counting safeguards — TC-G1/G6:** E_c has one real component,
so [n]⁻¹(R₁) has n real points, compared with n² over the complex numbers.
Only the compatible, pole-free points are eligible. For every nonconstant
scalar map of degree d, M valid points give at least M/d scalar values.
An invariant parameter set X+T=X merely permutes fixed-slot frames and
creates no new prescribed pairs. The frozen finite-grid degree bounds
remain in force within their hypotheses; the cover argument does not
remove their multiplicity or degree costs.

The old six-scalar CP seed has no CP-O1 attachment, by the later local
B-CP proof. Its exhaustive role reduction is inspected and its five
Bezout certificates are independently checked here. This imported
obstruction applies to that exact seed even if an isogeny or a different
parameterization is used. It does not exclude the new attachment above,
which starts from a different four-scalar frame.

## Exactly one next lemma

**OPEN — TC-O1.** For the unique different-width attachment above, let
R₁ and R₂ be its positive-Y marked points on E_c. Determine whether
T=R₂−R₁ is torsion, with a proof covering every order. An infinite-order
certificate is an acceptable resolution. This is one specified algebraic
point, not a rank/CM search. Even a torsion answer would supply only this
finite attachment; it would not evade the two-width bound or imply an
asymptotic saving. This remaining question is not pursued in this cycle.

[Provenance, cost ledger and verification](verification.md). Earlier
artifacts are preserved; no literature or novelty claim is made.
