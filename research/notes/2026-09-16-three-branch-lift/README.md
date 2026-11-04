# Characteristic-zero three-branch lift of the F3 fiber collapse

**2026-09-16 · T01 · fixed polynomial \(P(x,y)=(x-y)^3+x+y\).**
Authorized offline research report, version 1. No network, literature search,
package installation, or external novelty claim. Internal proofs and finite
computations are distinguished below. The other three tracks and T01's
separate norm–trace quadratic branch are unchanged.

## 1. Verdict

**PROVED — a finite gadget with structured complete-slice overlap exists.**
Take
\[
A=\{0,2\},\qquad F_r(x)=x/2+r/3\quad(r=0,1,2).
\]
The three branches are injective and disjoint, and
\[
A'=\{0,1/3,2/3,1,4/3,5/3\},\qquad
|P(A,A)|=4,\quad |P(A',A')|=22.
\]
Thus the complete nine-block union grows by \(11/2<9\), with normalized
factor \(22/(9\cdot4)=11/18\). Two entire difference slices are contained
in other slices; all remaining outputs are counted exactly. This meets the
finite-gadget criterion (Outcome A), in a limited sense: it is a finite
characteristic-zero analogue of fiber overlap, not an exact three-row collapse.

**FAILED — the literal iteration of these maps.** Already at the next stage,
\(F_0(2/3)=F_1(0)=1/3\), so the required disjoint tripling fails.
**PROVED — scoped obstructions** also exclude uniform sub-nine recurrences
on generic seeds for fixed algebraic branches, fixed-spacing interval
tripling, the residue-density approach at every power of 3, and literal
linear coordinate tensorization. These are different, explicitly limited
statements, not a universal no-go for adaptive algebraic constructions.

**OPEN — the original real cubic target.** No recursive all-pairs support
bound with a fixed gap below 9, and no arithmetic scalar realization with
positive signed rate, has been established. No favorable tower claim is made.

## 2. Scope, evidence, and finite budget

This cycle searches for a finite three-branch characteristic-zero gadget and
proves scoped obstructions. Maps depending on the stage or the seed are
allowed by the problem; the generic-seed obstruction below explicitly fixes
the maps first and therefore does not dispose of that broader possibility.

The announced budget was at most 1,000 rational affine gadgets, seed size
at most 6, enlarged size at most 18, and two further composition computations
with at most 54 enlarged inputs. Actual use: **980 attempts, 423 legal
gadgets, 557 rejected non-disjoint systems, and two composition checks**.
There were 79 legal gadgets with \(s'<9s\). This is exhaustive over the
listed grid only. No random or floating-point equality tests were used.

The [exact example record](../../../examples/2026-09-16-three-branch-lift.json)
contains **all 423 complete image counts**, parameters by trial ID, selected
full certificates, and both composition results. The local file
`local-only/runs/T01/2026-09-16-three-branch-lift/complete-gadgets.json`
contains every attempted seed and branch map, all nine scalar block images
for every legal gadget, complete unions, pairwise intersections, and exact
membership masks for **every higher-order intersection**. Rejected systems
record their input-branch defect and are not treated as gadgets. This local
raw file must accompany a local handoff; Git alone does not carry it.

Implementation: [three_branch_lift.py](../../../experiments/three_branch_lift.py).
There are 14 seeds (integer and half-integer progressions of sizes 2–6, and
four specified sparse/mixed seeds), 35 common-scale translation choices and
35 unequal-scale choices per seed. Parameters and exact runtime/input/code
hashes are in the JSON records and local `provenance.json`. Reproducibility
and audit results are recorded in [verification.md](verification.md).

## 3. Exact finite-field motivation and its limitation

On \(\mathbb F_3\), as a function,
\[
P(x,y)=x^3-y^3+x+y=2x=-x.
\]
There are three output types, each with three input pairs, but the output
support is the entire field. The equality \(z^3=z\) is specific to
\(\mathbb F_3\), not all characteristic-3 extension fields.

For every fixed \(y\), the map \(x\mapsto P(x,y)\) permutes
\(\mathbb Z/3^k\mathbb Z\) for every \(k\ge1\). Indeed the mod-3 map is
bijective and
\[
P(x+3^kt,y)\equiv P(x,y)+3^kt(1+3(x-y)^2)\pmod {3^{k+1}};
\]
the multiplier is 1 modulo 3, giving a unique lift at each step.

More strongly, for any nonempty, possibly correlated subset
\(E\subset(\mathbb Z/3^k\mathbb Z)^d\), fix \(y_0\in E\). The
coordinatewise map \(x\mapsto P(x,y_0)\) is injective, so, with
\(M=3^{kd}\),
\[
|P_{\rm coord}(E,E)|\ge|E|,\qquad
\boxed{\frac{M|P_{\rm coord}(E,E)|}{|E|^2}\ge\frac M{|E|}\ge1.}
\tag{3.1}
\]
In density notation this is \(q/\alpha^2\ge1\): paying the input density
twice defeats any proposed residue-support saving at 3, even with arbitrary
correlated subsets and arbitrarily high precision. This is a **local
certificate obstruction**, not a lower bound for every real cubic image.
Complete proof and scope: [TB-L1](source-scope.md#2-tb-l1--exact-prime-power-permutation-and-normalized-local-obstruction).

## 4. Candidate maps and symbolic nine-block formulas

For arbitrary affine branches \(F_r(x)=\lambda_rx+t_r\), write
\(D_{rs}=t_r-t_s\). Each of the nine blocks is given by the same explicit
polynomial, with its own \(r,s\):
\[
\begin{aligned}
B_{rs}(x,y)={}&\lambda_r^3x^3-3\lambda_r^2\lambda_sx^2y
+3\lambda_r\lambda_s^2xy^2-\lambda_s^3y^3\\
&+3D_{rs}(\lambda_r^2x^2-2\lambda_r\lambda_sxy+\lambda_s^2y^2)\\
&+(3D_{rs}^2+1)\lambda_rx+(1-3D_{rs}^2)\lambda_sy
+D_{rs}^3+t_r+t_s.
\end{aligned}\tag{4.1}
\]
In particular the mixed quadratic terms survive in characteristic zero.

For the successful finite gadget put \(z=(x-y)/2\), \(w=(x+y)/2\),
and \(H_k=z^3+kz^2+(k^2/3)z+k^3/27\). The full symbolic matrix is
\[
\begin{pmatrix}
H_0+w&H_{-1}+w+1/3&H_{-2}+w+2/3\\
H_1+w+1/3&H_0+w+2/3&H_{-1}+w+1\\
H_2+w+2/3&H_1+w+1&H_0+w+4/3
\end{pmatrix}.\tag{4.2}
\]
Equivalently, its \((r,s)\) entry is
\(z^3+(r-s)z^2+(r-s)^2z/3+(r-s)^3/27+w+(r+s)/3\).
This is an identity for all real \(x,y\); the equalities of supports below
use the specified finite seed.

A comparison gadget uses the same seed and \(\widetilde F_r=x/2+2r\).
It produces \(\{0,1,2,3,4,5\}\), and all nine symbolic formulas are
\[
z^3+6(r-s)z^2+12(r-s)^2z+8(r-s)^3+w+2(r+s).
\tag{4.3}
\]
Its exact support size is 24, with normalized factor \(2/3\).
Equations (4.1)–(4.3), together with the recorded parameter grid, specify
the symbolic block polynomials for every computationally tested gadget.

## 5. Complete scalar image and all block intersections

For the main gadget the branches are
\(B_0=\{0,1\}\), \(B_1=\{1/3,4/3\}\),
\(B_2=\{2/3,5/3\}\). They are pairwise disjoint and each contains two
distinct reals. The old image is \(\{-6,0,4,10\}\).

The following table lists **27 times each entire block image**. The common
output scaling is injective, so counts and intersections are unchanged.

| \(r\backslash s\) | 0 | 1 | 2 |
|---|---|---|---|
| 0 | \(\{0,54\}\) | \(\{-28,8,44,62\}\) | \(\{-80,10,46,64\}\) |
| 1 | \(\{10,28,64,100\}\) | \(\{18,72\}\) | \(\{-10,26,62,80\}\) |
| 2 | \(\{26,44,80,170\}\) | \(\{28,46,82,118\}\) | \(\{36,90\}\) |

All nonempty intersections of **different** blocks are:

| Blocks | Intersection, scaled by 27 |
|---|---|
| 01 and 12 | \(\{62\}\) |
| 01 and 20 | \(\{44\}\) |
| 02 and 10 | \(\{10,64\}\) |
| 02 and 21 | \(\{46\}\) |
| 10 and 21 | \(\{28\}\) |
| 12 and 20 | \(\{26,80\}\) |

Every triple or higher intersection is empty. Therefore the nine complete
block sizes sum to 30 and their union has \(30-8=22\) elements:
\[
\frac1{27}\{-80,-28,-10,0,8,10,18,26,28,36,44,46,54,
62,64,72,80,82,90,100,118,170\}.\tag{5.1}
\]
This accounts for every one of the 36 ordered input pairs. The reduction
from 36 to 30 occurs inside diagonal blocks; the reduction from 30 to 22
is overlap between distinct block images. Neither saving is counted twice.

For completeness, the integer comparison gadget's nine blocks, in row order,
are
\[
\begin{array}{ccc}
\{0,2\}&\{-24,-6,-4,2\}&\{-120,-60,-58,-22\}\\
\{4,10,12,30\}&\{4,6\}&\{-20,-2,0,6\}\\
\{32,68,70,130\}&\{8,14,16,34\}&\{8,10\}.
\end{array}
\]
Their sizes again sum to 30. The only repeated values between distinct
blocks are \(0,2,4,6,8,10\), each appearing in exactly two blocks. Thus
the full union has \(30-6=24\) values. This direct enumeration proves
the comparison cardinality without an asymptotic or experimental inference.

## 6. Why the collisions are systematic

For any real finite set \(C\), put \(C_u=C\cap(C-u)\). Then
\[
P(C,C)=\bigcup_{u\in C-C}(u^3+u+2C_u).
\]
Each slice is injective in its anchor. Two slices meet exactly when
\[
a-b=\frac{(v-u)(u^2+uv+v^2+1)}2.
\tag{6.1}
\]
The main gadget uses the following **identities for every real \(t\)**:
\[
\begin{aligned}
P(t,t-1)&=P(t,t)=P(t,t+1)=2t,\\
P(t+1/3,t)&=P(t,t+2/3)=2t+10/27,\\
P(t-1/3,t)&=P(t,t-2/3)=2t-10/27.
\end{aligned}\tag{6.2}
\]
Thus these are not numerical coincidences. Their use on a finite carrier
requires every displayed endpoint to belong to that carrier.

For \(C=A'\), write \(x=i/3,y=j/3\), \(d=i-j\). The scaled slice is
\[
S_d=\{d^3+9d+18j:\max(0,-d)\le j\le\min(5,5-d)\}.
\tag{6.3}
\]
The complete slices satisfy
\[
\begin{array}{ll}
S_0=\{0,18,36,54,72,90\},&
S_1=\{10,28,46,64,82\},\\
S_{-1}=\{8,26,44,62,80\},&
S_2=\{26,44,62,80\}\subset S_{-1},\\
S_{-2}=\{10,28,46,64\}\subset S_1,&
S_{3},S_{-3}\subset S_0.
\end{array}
\]
The four remaining slices are
\(S_4=\{100,118\}\), \(S_{-4}=\{-28,-10\}\),
\(S_5=\{170\}\), \(S_{-5}=\{-80\}\).
These four and \(S_0,S_1,S_{-1}\) are pairwise disjoint: their displayed
values prove this directly. Their sizes total \(6+5+5+2+2+1+1=22\).
This supplies a second, slice-based proof of the entire image count.

The identities continue to act on step-\(1/3\) progressions, but involve
only finitely many difference types. They do not by themselves control a
positive fraction of all pairs as the progression grows. Section 8 proves
the actual fixed-spacing asymptotic obstruction.

The declared grid also varied the seed within one structured family:
\(A_n=\{j/2:0\le j<n\}\), \(F_r(x)=2x+r/3\). The enlarged set is
\((1/3)\{0,\ldots,3n-1\}\). Existing exact records give:

| \(n\) | Old support \(s\) | Complete new support \(s'\) | \(s'/(9s)\) |
|---|---|---|---|
| 2 | 4 | 22 | \(11/18\) |
| 3 | 7 | 49 | \(7/9\) |
| 4 | 12 | 90 | \(5/6\) |
| 5 | 19 | 147 | \(49/57\) |
| 6 | 28 | 216 | \(6/7\) |

These are **EXPERIMENTAL exact** counts on the stated five seeds, already
included in the 980 attempts. The old and new spacings differ, so they do
not form successive levels of one recursive construction.

## 7. Exact symbolic obstructions and their scope

The [symbolic proof companion](symbolic-audit.md) proves the following
statements, audited internally in this cycle.

1. **Separable rigidity.** For nonconstant real analytic local maps, an identity
   \(P(H(x),K(y))=aP(x,y)+b\), \(a\ne0\), on an open rectangle forces
   \(H(x)=\varepsilon x+t\), \(K(y)=\varepsilon y+t\),
   \(a=\varepsilon\in\{1,-1\}\), \(b=2t\).
   In particular exact same-output identities force \(H=x,K=y\).
   A swapped-input exact same-output identity is
   impossible over the reals. Algebraic branches are included on regular
   analytic intervals.
2. **Fixed algebraic branches on generic seeds.** Fix three distinct
   nonconstant real algebraic branches over a coefficient field \(K\), on
   a common regular interval. Choose \(n\) seed values algebraically
   independent over \(K\). The branch values are distinct, and all
   \(9n(n-1)\) outputs with unequal seed indices are distinct. Hence
   \[
   |P(A',A')|\ge9n(n-1),\qquad |P(A,A)|=n^2.\tag{7.1}
   \]
   No fixed \(\rho<9\) and subquadratic error can bound these uniformly
   as \(n\to\infty\). This excludes a seed-independent universal
   compression rule. It does not exclude exceptional structured seeds or
   coefficients chosen after the seed.
3. **Rational old-output factorization.** For nonconstant rational branches
   \(f,g\), a univariate factorization
   \(P(f(x),g(y))=\Psi(P(x,y))\) by a locally algebraic scalar function
   reduces to the reflection/translation identities in item 1. It provides
   no distinct-branch collapse into one old scalar invariant. Its scope
   does not include arbitrary nonrational algebraic \(f,g\).

4. **Adaptive literal row collapse.** For any seed of size \(n\) and any
   three injective disjoint branches, even arbitrary seed-dependent maps,
   group the second-coordinate values into triples
   \(\{F_0(y),F_1(y),F_2(y)\}\), one for each old \(y\). Summed over
   all \(3n^2\) packets obtained by fixing a new first coordinate and an
   old \(y\), the loss of output labels *within packets* is at most \(6n\).
   Indeed for distinct \(b,c\),
   \[
   P(X,b)=P(X,c)\iff
   3(X-(b+c)/2)^2+(b-c)^2/4=1,
   \]
   so each of the three pair comparisons in a triple holds at at most two
   first coordinates. Complete triple collapse occurs for at most one
   first coordinate per triple (its mean). Thus literal synchronous
   Frobenius collapse cannot itself give a quadratic-sized saving.
   **This does not bound the final union:** cross-packet collisions, such
   as the main gadget's translated slice coincidences, remain available.

For a concrete illustration, fixed branches \(F_r(x)=x+r\),
\(r\in\{-1,0,1\}\), produce exactly \(9n^2-4n\) outputs on such generic
seeds. The five diagonal-seed output functions are
\(2x-8,2x-2,2x,2x+2,2x+8\). Thus the singleton \(9\to5\) collapse
survives only as a linear-sized saving on generic large seeds. The actual
finite gadget in Sections 4–6 uses a special rational seed and is fully
consistent with these obstructions.

## 8. Composition checks and a complete progression no-go

The two computational composition checks used the comparison gadget
\(A_6=\{0,\ldots,5\}\), whose complete image has size 24:

| Continuation | Exact input result | Complete output result | Disposition |
|---|---|---|---|
| Repeat \(x/2+2r\) | Only 14 distinct inputs, not 18 | Not treated as a legal gadget | Branch overlap; FAILED |
| Stage-dependent \(x+6r\) | \(A_{18}=\{0,\ldots,17\}\), 18 inputs | 252 outputs; \(252/24=21/2>9\) | Normalized factor \(7/6\); FAILED at this step |

For the best gadget the exact equality \(F_0(2/3)=F_1(0)\) already rejects
literal repetition without another enumeration. No third composition search
was performed. A different adaptive continuation has not been supplied.

**TB-P1 — PROVED, actual-image lower bound.** Let
\(C_N=t+h\{0,\ldots,N-1\}\), \(h>0\), and set
\[
K_N=\max\left(2,\left\lceil\sqrt{\frac{2N}{3h^2}}\right\rceil\right).
\]
If \(K_N<N\), then
\[
|P(C_N,C_N)|\ge(N-K_N)(N-K_N+1).\tag{8.1}
\]
If \(K_N\ge N\), only the trivial nonnegative lower bound is asserted.
In particular for fixed \(h>0\),
\[
|P(C_N,C_N)|=N^2-O_h(N^{3/2}).\tag{8.2}
\]
More generally the ratio to \(N^2\) tends to 1 whenever
\(h=h_N\) satisfies \(h_N\sqrt N\to\infty\).

**Proof.** For a positive index difference \(d\), the \(N-d\) distinct
outputs lie in
\[
I_d=[2t+h^3d^3+hd,\ 2t+h^3d^3+2h(N-1)-hd].
\]
The next lower endpoint minus this upper endpoint is
\[
h^3(3d^2+3d+1)+h(2d+1)-2h(N-1)>0\quad(d\ge K_N).
\]
Negative-difference slices are the reflections of the positive ones about
the output midpoint \(2t+h(N-1)\). The positive and negative tails are
separated because
\(h^2K_N^3+K_N>N-1\): indeed
\(h^2K_N^2\ge2N/3\) and \(K_N\ge2\). All slices with
\(|d|\ge K_N\) therefore have mutually disjoint containing intervals.
Their total cardinality is
\(2\sum_{d=K_N}^{N-1}(N-d)=(N-K_N)(N-K_N+1)\).
The trivial upper bound is \(N^2\). This proves all assertions. ∎

Consequently fixed-spacing interval tripling has
\(s(3N)/s(N)\to9\). It cannot satisfy a uniform recurrence with
\(\rho<9\) and \(O(N^{2-\delta})\) error for \(\delta>0\).
This is a complete independent proof for that family; it does not rely on
the unavailable full digital checkpoint. Rapidly shrinking spacings outside
the displayed hypothesis and non-progression sets remain outside TB-P1.

## 9. Recursive rate implication

**TB-R1 — PROVED implication; no witness supplied.** Suppose actual legal
sets satisfy \(n_m\asymp3^m\), and for fixed
\(1\le\rho<9\), \(\delta>0\), \(C<\infty\), at every sufficiently
large level,
\[
s_{m+1}\le\rho s_m+C n_m^{2-\delta}.
\]
Put \(\lambda=3^{2-\delta}\). Iteration and the two-sided bounds for
\(n_m\) give
\[
s_m=O\!\left(\rho^m+\sum_{j<m}\rho^{m-1-j}\lambda^j\right)
=O\!\left((m+1)\max(\rho,\lambda)^m\right).
\]
The factor \(m+1\) is only needed at resonance, but is harmless in general.
For every
\[
0<c<\min\{2-\log_3\rho,\delta\},
\]
the strict exponent gap absorbs this factor and all fixed constants, yielding
\(s_m\le n_m^{2-c}\) eventually. The lower bound \(s_m\ge n_m\)
also forces consistency of the claimed rates. No step of this implication
promotes the single finite value \(\rho=11/2\) to a valid recurrence.

## 10. Arithmetic amplification gate

The finite coordinate gadget has a positive *formal* tensor rate:
\[
|C^d|=6^d,\quad |P_{\rm coord}(C^d,C^d)|=22^d,\quad
2\log6-\log22=\log(18/11)>0,
\]
where \(C=\{0,1/3,\ldots,5/3\}\). This is a result about vector outputs,
not scalar real outputs. It cannot be transported by an injective linear
scalar encoding intertwining the same polynomial.

**TB-L2 — PROVED.** If \(T(u)=\sum_iw_iu_i\) satisfies
\(P(Tu,Tv)=T(P_{\rm coord}(u,v))\) for every \(u,v\in C^d\), set
\(v=0\). The cubic
\((\sum_iw_iu_i)^3-\sum_iw_iu_i^3\) vanishes on a grid with six distinct
values per coordinate. Repeated univariate root counting makes it the zero
polynomial. Thus \(w_i^3=w_i\) and \(w_i^2w_j=0\) for \(i\ne j\).
At most one weight is nonzero, equal to \(\pm1\), so no such \(T\) is
injective for \(d>1\). The proof applies equally to the integer comparison
grid. This does not exclude nonlinear finite encodings or constrained
number-field carriers with a separate support theorem.

Accordingly no Chebotarev or prescribed-splitting tower construction was
launched. The preliminary transport gate fails in the literal tensor model,
while a different model has no proved carrier or cost bounds. Counting split
primes cannot repair this missing characteristic-zero equality transport.
Equation (3.1) separately excludes a favorable raw 3-adic density factor.

**EXTERNAL RESULT — supplied source, not freshly audited:** the existing
unit-distance proof's Proposition 3.8 is the project's recorded tower source.
The separate T01 norm–trace checkpoint §4 records descriptions of
Hajir–Maire–Ramakrishna Proposition 1.9 and Hamza–Maire Theorem A.
Their full primary texts and any newly needed quantitative constants are
**MISSING SOURCE / PROVENANCE FILE** in this cycle. No such theorem is
invoked in a new construction here; see [source scope](source-scope.md#4-arithmetic-source-boundary).

## 11. Full gain-versus-cost ledger

This instantiates [CONSTRUCTION_LEDGER.md](../../templates/CONSTRUCTION_LEDGER.md).
All finite-gadget entries concern the exact same real set in both arguments.
Parameters \(A=\{0,2\},\lambda=1/2,t_r=r/3\) are fixed before evaluation.

| Gain/cost | Finite gadget: proved amount and reason | Proposed amplification: status |
|---|---|---|
| Input lower and upper count | Both exactly 6; seed size exactly 2 | Formal vector input \(6^d\); scalar carrier OPEN |
| Input thinning in both coordinates | Zero: no seed or enlarged inputs discarded | Any fraction \(\theta_d\) would cost \(\theta_d^2\); unknown, not zero |
| Parameter/projection fibers | One: injective branches, disjoint union, identity real projection | Literal linear transport impossible; other fiber bounds OPEN |
| Complete output support | Exactly 22, including all 36 ordered pairs | Formal vector support \(22^d\); scalar full support OPEN |
| Local sparsity and splitting | No modular restriction used | At 3, density factor \(q/\alpha^2\ge1\); no gain |
| Uniform per-residue population | Inapplicable to direct finite enumeration | No global packing certificate supplied |
| Field degree/discriminant | Field \(\mathbb Q\), degree and discriminant 1 | Growing field realization absent; costs unknown |
| Regulator/class number/unit counts | No unit or ideal construction; no such loss | Unknown for a hypothetical alternative carrier |
| Denominators and coefficients | Branch denominators divide 6; actual inputs divide 3, outputs divide 27; multiplication by 27 injective | Denominator/coefficient growth must be charged; not assumed constant |
| Archimedean size/distortion | Inputs in \([0,5/3]\); outputs exactly (5.1), within \([-80/27,170/27]\); no volume estimate | Tensor-to-scalar distortion and mixed terms unresolved |
| Branches/ratios/covers | All nine blocks, no omitted ratios; union uses exact intersections | No finite closed output-state system supplied |
| Carries | None omitted: rational arithmetic exact; (4.1) retains all mixed terms | Any digital transport must include all carries |
| Exceptional/uncovered outputs | Zero uncovered pairs; four outer slices contribute six outputs and are included | No subquadratic exceptional-tail theorem |
| Finite normalized comparison | \(22/(9\cdot4)=11/18\); nine-block sum 30, union 22 | One-step gain is not a rate theorem |
| Formal vector rates | \(a=B=\log6\), output rate \(b=\log22\) in the product algebra only | Scalar rates \(a,B,b\) unknown |
| Net rate and exponent | Formal vector gap \(\log(18/11)>0\) | No certified scalar \(2a-b>0\), hence no real power-saving exponent |

For an alternative realization, a transparent provisional ledger would be
\(a=\log6-\ell\), \(b=\log22+\kappa\), requiring
\(2\ell+\kappa<\log(18/11)\). Here \(\ell\) must include *all* input,
fiber and arithmetic losses and \(\kappa\) *all* output inflation, with
an actual injective real projection and an input upper bound. Neither
quantity is known. This inequality is bookkeeping, not a proposed tower
theorem or a supported conjecture.

## 12. Compatibility, provenance, and claim ledger

The finite sets have zero volume, so the positive-volume continuous-cover
obstruction does not exclude them. The source's digital obstruction is
asymptotic and requires its specific normalized rational model, fixed prime
support and positive entropy. A finite gain contradicts none of those
hypotheses or conclusions; stage dependence alone would not escape them.
Our fixed-spacing progression continuation is independently rejected by
TB-P1. No cube-residue deformation, literal \(GP\) transfer, scalar
norm-one trace construction, or rich-quadratic-fiber carrier is used.
None of their failed certificates is silently repackaged as a gain.

In particular (6.2) is an unnormalized finite row/slice identity of the kind
warned about in T01 current-state §6.5. It supplies no digitwise carry
closure. Under a common affine scale and shift, (4.1) retains the quadratic
and linear difference terms; discarding them would repeat that failed
mechanism. This report claims a finite count and the stated limited
obstructions, not a new surviving digital construction.

The continuous proof was inspected. The full named digital and rich-fiber
checkpoints are unavailable in the supplied tree: their theorem statements
and sketches in T01 current state are **reported source results**, not newly
audited complete proofs. Their names and the exact missing-source markers,
plus source hashes, are in [source-scope.md](source-scope.md). All original
archives, SPECs, and historical sections remain unchanged.

Every row below is T01 / three-branch branch / the fixed plus-sign cubic,
version dated 2026-09-16. Quantifiers and hypotheses are those in the named
sections; dependencies are explicit. “Internally audited” means separate
agent/lead checking, not external certification or a novelty assessment.

| Claim ID | Status, locator, evidence and dependencies | Remaining gap / scope |
|---|---|---|
| TB-F1 | **PROVED internally**, §§4–6: the specified rational seed, maps, nine-block and 22-value counts; direct algebra and independent slice count, exact data check | Finite only; no recursive closure |
| TB-F2 | **PROVED internally**, §§4,8: integer comparison gadget has 24 outputs; **EXPERIMENTAL exact** continuation has 252; complete stored enumeration | Listed maps only |
| TB-E1 | **EXPERIMENTAL**, §2 and exact JSON: exhaustive declared 980-point parameter grid, 423 legal systems, 79 strict finite gains | No coverage of other maps or larger seeds |
| TB-S1 | **PROVED — inspected supplied proof**, source companion §1: continuous cover theorem | Positive-volume certificate only |
| TB-S2–S4 | **PROVED — reported source status**, source companion §1: digital theorems and exact rich-fiber rejection | Full named proofs missing; no independent full audit claimed |
| TB-L1 | **PROVED internally**, §3 / source companion §2: every \(k,d,E\) in (3.1), unique lifts plus injectivity | Density-based local certificates only |
| TB-L2 | **PROVED internally**, §10 / source companion §3: all dimensions and exact linear intertwiners on the six-point grid | Other scalar encodings not excluded |
| TB-A1–A5 | **PROVED internally**, symbolic companion §§1–5: real separable rigidity, rational factorization, generic-seed bound and translate example | Fixed maps / identity or generic-seed scopes; structured adaptive seeds excluded |
| TB-A6 | **PROVED internally**, symbolic companion §6: every finite seed and arbitrary disjoint injective branches; at most \(6n\) within-packet label savings | Cross-packet collisions not bounded |
| TB-P1 | **PROVED internally**, §8: all progressions with the displayed spacing conditions; interval separation, independently checked | Shrinking-spacing and non-progression cases outside scope |
| TB-R1 | **PROVED implication**, §9; its application is **CONDITIONAL** on an actual all-level recurrence | No candidate meets the premises |
| TB-N1 | **FAILED**, §§8,10: literal repeated branch maps, fixed-spacing progression recursion, literal linear tensor transport | Not universal impossibility |
| TB-O1 | **OPEN**, §§1,10–11: fixed-exponent real construction and profitable scalar arithmetic realization | Missing composable support mechanism and paid realization |

## 13. Exactly one recommended next proof obligation

**Decide the remaining nonrational algebraic factorization problem:** classify
nonconstant real algebraic branches \(f,g,\Psi\), regular on suitable real
intervals, satisfying
\[
P(f(x),g(y))=\Psi(P(x,y))
\]
on an open rectangle. Determine whether any exist beyond
\(f=g=\varepsilon x+t\), \(\Psi(z)=\varepsilon z+2t\),
\(\varepsilon=\pm1\). The rational-input case and affine-output case
are settled here; the genuinely algebraic-input, nonlinear-output case is
not. A proof of rigidity or one exact exception would resolve a defined
identity class relevant to radical branches. No positive existence conjecture
is asserted, and this recommendation does not commission another cycle.
