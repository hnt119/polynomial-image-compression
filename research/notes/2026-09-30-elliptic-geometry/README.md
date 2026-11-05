# Elliptic geometry for the cubic image problem

T01 · 2026-09-30 · offline research · fixed P(x,y)=(x-y)³+x+y.
**OPEN:** no asymptotic real power-saving construction is obtained.
The latest [near-complete-chart checkpoint](../2026-09-30-near-complete-charts/README.md)
remains in force. Three mathematical specialists and the lead divided geometry,
group laws, complex extensions and exact computation; proofs are supplied in
the linked companions. No literature or novelty claim is made.

## 1. Strongest result

**PROVED — global obstruction.** No nonconstant meromorphic maps on elliptic
curves can satisfy
\[
 P(f(R),g(S))=H(\alpha R\pm\beta S+T)
\]
identically when H is nonconstant and α,β are nonzero isogenies to a common
elliptic curve. The left side has poles only on vertical or horizontal
divisors. Every pole of H pulls back to a divisor projecting onto both
coordinates, where the left side is generically finite. This also survives
base extension to C and algebraizing branches on separate finite covers.

**PROVED — finite-grid obstruction.** On one elliptic curve, let
d=deg(f), h=deg(H)>0. For finite parameter sets X,Y avoiding input poles,
the number of successful, defined equations
\[
 P(f(R),g(S))=H(R\pm S+T)
\]
is at most
\[
 (3d+h)|Y|+d|X|.
\]
A nonidentical row has at most 3d+h zeros; at most d rows can be identities,
since a fixed pole of H must translate into a pole of f.
For A=f(X), N=|A| and X used in both coordinates, |X|≤dN, so this rule
covers at most d(4d+h)N actual scalar pairs. A fixed finite library of fixed
degree therefore covers only O(N) pairs. Near-full coverage by a growing
library requires its sum of these degree costs to be Ω(N).
[Full proofs and isogeny costs](group-law.md).

## 2. Equations and actual genera

**PROVED.** Write u=x−y and z=P(x,y). Then
\[
 x=c_+(z,u),\quad y=c_-(z,u),\qquad
 c_s(z,u)=\frac{z-u^3+s u}{2}.
\]
An actual output fiber is an affine line parametrized by u; its projective
cubic closure has a cusp at infinity and normalization genus 0. The complete
collision variety is affine three-space with coordinates (u,v,z).

Sharing a scalar between outputs z,w instead gives the plane curve
\[
 C_{s,t,c}:\ u^3-v^3-su+tv=c,\qquad c=z-w,\quad s,t\in\{1,-1\}.
\]
All three points at infinity are smooth. Its finite singularities satisfy
\[
 u^2=s/3,\qquad v^2=t/3,\qquad c=\tfrac23(tv-su).
\]
Each is an ordinary node. Outside these explicit critical values the cubic
is smooth of genus 1. At a nonzero critical value it is irreducible with
normalization genus 0. At s=t,c=0 it factors as
\[
 (u-v)(u^2+uv+v^2-s)=0,
\]
with genus-zero line and conic components. Over R the nonzero critical
values occur only for s=t=1, at c=±4/(3√3); mixed signs have no real
critical value.

For the **separate comparator** Q=(x−y)⁴+x+y, signs reduce every sharing
equation to a⁴−b⁴−a+b=c. Every real c≠0 is smooth of genus 3.
At c=0 it is a line plus the smooth genus-one cubic
(a+b)(a²+b²)=1. Over C its six nonzero critical values have one node
and normalization genus 2. Thus degree alone does not determine genus.
This comparison makes no claim about the different T02 polynomial.
[Singularities, irreducibility and normalization proofs](genus.md).

## 3. Best elliptic candidate

**PROVED.** For s=t, set d=u−v and w=u+v. For c≠0 and
16s³−27c²≠0,
\[
 d(3w^2+d^2-4s)=4c,\quad
 X=\frac{12c}{d},\quad Y=\frac{36cw}{d},
\]
giving Y²=X³+12sX²−432c². After x=X+4s,
\[
 E_{s,c}:\quad y^2=x^3-48s^2x+128s^3-432c^2.
\]
The rational example s=1,c=6 has T=(40,216) of infinite order.
Its multiples give pairs on the two actual output fibers 6 and 0,
with a shared first coordinate. This is a genuine elliptic source of
rational scalar reuse. It supplies no factorization of the full Cartesian
P table through the group law.

**COMPUTATIONAL.** Exact full-square enumeration gave:

| Sharing prefix m | Actual N | Prescribed pairs | Entire image | Other fibers |
|---:|---:|---:|---:|---|
| 2 | 5 | 4 | 23 | 21 singletons |
| 4 | 11 | 8 | 115 | 113 singletons |
| 6 | 17 | 12 | 279 | 277 singletons |
| 8 | 23 | 16 | 515 | 513 singletons |

In each row the remaining two fibers have size m. Direct elliptic
x-coordinate prefixes of sizes 4,8,12,16 gave image size N²−2,
with exactly two double fibers. These are eight finite examples, not
asymptotic evidence establishing a failure theorem.

## 4. Complex and extension findings

**PROVED.**
\[
 \Delta=2^{12}3^6c^2(16s^3-27c^2),\qquad
 j=\frac{4096s^6}{c^2(16s^3-27c^2)}.
\]
For s=1, the smooth family has no j=0 member. It has j=1728 at
c²=8/27, giving y²=x³−48x and the complex automorphism
(x,y)↦(−x,iy). Such extra automorphisms and isogenies still obey the
mixed-pole obstruction. No high-rank or full torsion classification is claimed.

A real field embedding preserves the fixed polynomial and all cardinalities.
Taking real parts generally does not: if a−b=r+it, then
\[
 \operatorname{Re}P(a,b)=P(\operatorname{Re}a,\operatorname{Re}b)-3rt^2.
\]
For a same-set square with at least two distinct real parts, this discrepancy
vanishes everywhere only when all inputs have the same imaginary part.
Thus conjugation trace offers no new coordinate compression in that case.
A real shared-endpoint triple already has real u and v.
[Exact models, descent and infinite-order certificate](complex-extensions.md).

## 5. Full Cartesian coverage and rates

**PROVED.** The explicit sharing family has m/9≤N≤3m and at most 2m
designated pairs. More sharply, every real output fiber has at most N
pairs: for fixed y, P(x,y) is strictly increasing in x. The two prescribed
fibers therefore cover at most 2N pairs, leaving at least N²−2N pairs.
The safe image certificate remains 2+N²−Q.
Additional collisions outside those pairs are unresolved asymptotically;
the finite table does not prove that they never occur.

**PROVED.** There are also degree-independent constraints. With an injective
real scalar projection, a single sum rule covers at most (N²+N)/2 ordered
pairs, by swapping the inputs. A single difference rule on a parameter
set with K distinct differences covers at most (N²+K)/2 pairs.
An elliptic progression has K=O(N), so neither rule can cover almost all
pairs, even if H has growing degree. Noninjective projections require the
multiplicity corrections in the group-law companion.

**CONDITIONAL.** If the actual small-fiber tail satisfies
B_A(N^η)≤C N^(2−γ), then
|P(A,A)|≤C N^(2−γ)+N^(2−η). Every fixed exponent
0<c₀<min(η,γ) follows for sufficiently large N.
No such tail bound is proved here. [Complete cost ledger](construction-ledger.md).

## 6. Proved failures and their scope

**PROVED:** global elliptic sum/difference factorization fails; fixed
degree-weighted libraries fail near-full coverage; injective sum rules and
injective small-difference-set rules fail even without a degree bound.

**PROVED:** no nonconstant map from a genus-zero or genus-one smooth
projective curve to a curve of genus at least two exists, by the
ramification formula. This excludes a global rational or elliptic
parametrization of the generic quartic sharing curve. It does not bound
arbitrary finite real point sets or prove that high genus obstructs the
original T01 target.

**OPEN:** dense networks of multiple sharing correspondences, finite branch
selections without a global group identity, and growing libraries beyond
the degree-cost bounds. None is certified as a surviving positive
construction.

## 7. Exactly one next proof obligation

**OPEN — EG-O1.** Construct an unbounded family of real scalar sets A,
|A|=N, and real output-indexed parameter sets U_z such that, for fixed
η,γ>0,
\[
 c_+(z,U_z),c_-(z,U_z)\subseteq A,\qquad
 |U_z|\ge N^\eta,\qquad
 \sum_z|U_z|\ge N^2-O(N^{2-\gamma}).
\]
All repeated endpoints must be identified as actual scalars, using the
sharing equations above; all ordered pairs outside these fibers must be
charged. This is the existing near-full fiber-tail obligation written
in shared-endpoint coordinates, not a claimed new geometric reduction.

---

Reproducibility: [exact data](../../../examples/2026-09-30-elliptic-geometry.json),
[code](../../../experiments/elliptic_geometry.py),
[verification record](verification.md). Eight candidate sets used 1,444
P evaluations; the new unit regression adds 29. Research remained offline.
