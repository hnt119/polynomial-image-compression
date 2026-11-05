# T01 status — cubic / digital-carry program

Reconciled **11 September 2026** from the **10 September** final norm–trace
checkpoint and `T01_CURRENT_STATE.md`. **Fixed target: OPEN.**

$$P_+(x,y)=(x-y)^3+x+y.$$

The [SPEC](SPEC.md) retains this fixed polynomial, one fixed positive exponent,
and arbitrarily large finite real sets using the same set in both inputs.
Its proposed regular digital certificate is now **HISTORICAL / SUPERSEDED**:
the later theorem excludes its witness hypothesis. SPEC is preserved unchanged;
see [migration issue MC-01](../../MIGRATION_CONFLICTS.md).

`PROVED` below means proved in the identified source record, not independently
reproved by this reconciliation or certified as externally novel. Full source
identities are in the [source registry](../../MIGRATION_CONFLICTS.md#source-registry).

## Current cubic state

**OPEN:** no supported all-pairs cubic construction or positive rate ledger
survives. The recorded stop for supervisor reassessment remains part of the
history. Sparse base-6 renormalization is still unproved and was deprioritized;
it is not a supported construction or the current assignment.

**PROVED — positive quadratic baseline:** $(x-y)^2+x+y$ has a fixed power-saving
same-set construction using square residues at completely split primes and
uniform norm-separated packing. This baseline does not solve the cubic.

**PROVED — continuous certificate obstruction:** for every bounded Borel
$W\subset\mathbb R^m$ of positive volume $V$,

$$N_1(\{(x-y)^{\circ3}+x+y:x,y\in W\})>(\sqrt3/\pi)^mV^2.$$

The specified volume/covolume input and continuous-cover output certificate
therefore has normalized factor greater than one in the source tower.
It does not lower-bound arbitrary sparse finite lattice images.

**PROVED — regular digital obstruction:** for fixed integer base $b\ge2$ and
finite strongly connected right-resolving input graph with fixed start, every
state terminal, and spectral radius $\mu>1$, let
$D_n=\{[u]_b:u\in L_n(G)\}$ and $A_n=b^{-n}D_n$. Then

$$|Z_{b^n}(D_n,D_n)|\ge c_G|D_n|^2,\qquad
Z_N(U,V)=(U-V)^3+N^2(U+V).$$

Consequently an all-output automaton of length $3n+O(1)$ with polynomial
prefactor and $\lambda^3<\mu^2$ cannot satisfy the SPEC's proposed criterion.

**PROVED — stronger fixed-prime positive-entropy obstruction:** fix finite
nonempty prime support $S$ and $\alpha>0$. For sufficiently large $S$-smooth
$N$ and every $D\subset[0,N)\cap\mathbb Z$ with $|D|\ge N^\alpha$,

$$|Z_N(D,D)|\ge\eta(S,\alpha)|D|^2.$$

This includes nonregular or depth-dependent digit rules with these hypotheses.
Zero entropy and growing prime support are outside the theorem, without a
positive construction being implied.

**PROVED — actual rich-fiber family failure:** the precisely defined family
$A_j=\sigma_1(T_j/(2\sqrt{\zeta_j}))$ in current-state §4.4 has
$\vartheta^{-d_j}\le|A_j|\le(2X+1)^{d_j}$ and exactly $|A_j|^2$ cubic outputs.
Here $T_j$ is the difference set in a largest quadratic fiber of the stated
translated box, with $\rho_2R\le1/100$, $M\ge64$,
$X=2\lfloor M/8\rfloor\ge4\sqrt R$, and $\vartheta\le0.72$.
This is an actual-image theorem for that family; the other failed envelopes
are not automatically actual-image lower bounds.

## Separate completed norm–trace branch

**OPEN:** the 10 September checkpoint investigated
$P_0(x,y)=x^2+xy+y^2+x$ separately. It neither replaces T01's cubic nor changes
T03's homogeneous target. General quadratic forms through addition,
multiplication, norm/trace, and solvable extensions remain shared direction.

**PROVED algebra:** for $q=x^2+xy+y^2$,

$$P_0(x,y)=q(x+2/3,y-1/3)-1/3.$$

The general quadratic reduction uses a quadratic étale algebra (the split
case is $K\times K$). Completing the norm does not by itself solve the
unequal shifts of a common Cartesian input.

**PROVED implication; CONDITIONAL construction:** if growing $C$ satisfy

$$|q(C,C)|\le K_*|C|^{2-c_0},\quad
|C-C|\le D_*|C|^{1+\eta},\quad
0<c_0\le1,\quad0\le\eta<c_0/2,$$

with fixed constants, a richest nonzero difference produces a same-set
$P_0$ witness with exponent $c_1=(c_0-2\eta)/(1-\eta)>0$ before the usual
constant absorption. **OPEN:** no such homogeneous witness is supplied;
no amplification conjecture was adopted.

**PROVED bound; FAILED power-saving certificate:** the explicit shifted
Phase-A family $A_j=\sigma_1(G_jP_j)-1/6$ has a full-pair reflection bound
$(N_j^2+N_j)/2$ and a box bound $(6L^2+4L+1)^{d_j}$, where
$L=(1+\epsilon)Xe^Y$, $\epsilon=1/10$, $Y\ge2$, and
$N_j\ge e^{hd_j}/(Y\sqrt{d_j})$ with
$h=\log(\epsilon XY)-\tfrac32\log D_0>0$.
The box exponent $g=\log(6L^2+4L+1)$ satisfies $g>2h$.
The reflection gives only a constant factor; the actual family's image remains
**OPEN**. The prescribed-prime norm-residue certificate also loses:
$e^{g-2h}\ge3\rho R>1$ for its tested modulus supported on at most the source's
$t$ prescribed primes (even granting the optional prime 3). This restriction
does not limit all primes splitting in the tower.

## Other scoped FAILED routes retained

| Route | Exact failed scope |
|---|---|
| Cube residues and uniform lifts | Source lattice/CRT certificates, including the recorded anisotropic, algebraic-denominator, separate-scale, enclosing-shell, and exceptional-prime variants; not arbitrary sparse arithmetic inputs |
| Correlated first-level residues | Averaged input-density and uniform allowed-lift count; no lower bound on every exact image |
| Digitwise row collapse | Carry descriptions omitting unread differences, squares, or the scaled linear term; finite tests cannot supply all-depth closure |
| Scalar norm-one traces | Separate product/ratio labels and the stated denominator container; not every possible trace cancellation |
| Literal cubic $GP$ transfer | Mixed monomial labels, shared-scale pairs, and bounded-ratio restrictions do not cover/compress the full square; not a theorem against every $GP$ carrier |
| Norm-one actions for $P_0$ | No nonidentity multiplicative norm action preserves a nonempty finite common grid; partial intersections are outside the statement. Fractional ideal-label integrality weights apply to residue-uniform coefficient boxes only |

See the [failure library](../../FAILURE_LIBRARY.md) for retained formulas and
source scopes. **EXPERIMENTAL:** historical digital and norm-residue finite
checks are evidence at their tested parameters only; none was rerun here.

## Authority and chronology

- 2 September: quadratic success and conditional continuous block route.
- 3 September: continuous block and regular/fixed-prime positive-entropy
  digital obstructions supersede those proposed witnesses.
- 7 September: the selected rich-fiber cubic family is injective; reassessment stop.
- 10 September: `T01_Norm_Trace_Quadratic_Research_Checkpoint.md`, §§1–8,
  completes the separate quadratic branch; `T01_CURRENT_STATE.md`, §§4–8,
  12–15, freezes both branches without a new cubic candidate.

The inherited September 5 record below is retained for provenance. Its
“next useful result” and missing-source statements are not current instructions.

<details>
<summary>HISTORICAL / SUPERSEDED — complete 5 September 2026 STATUS snapshot</summary>

# T01 status and history

**Ultimate target: OPEN IN THE AVAILABLE RECORD.**
**Recent direction: exact digital carries on zero-volume inputs.**

## Sequence of results

1. The [2 September checkpoint](../../history-sources/Cubic_Difference_Sum_Research_Checkpoint.md),
   §§A, E–I, records a failed split-prime/lattice certificate and a conditional
   route through a finite archimedean covering block.
2. The [subsequent block checkpoint](../../history-sources/Concrete_Cubic_Compression_Block_NoGo_Checkpoint.md),
   §§A, F–H, closes the proposed positive-volume block condition. For bounded
   Borel $W\subset\mathbb R^m$ of positive volume $V$, it states
   $$N_1(\{(x-y)^{\circ3}+x+y:x,y\in W\})>
   (\sqrt3/\pi)^m V^2.$$
   For the specified tower with root-discriminant constant $R>\pi/\sqrt3$, the
   source's normalized covering certificate therefore exceeds one.
3. The recent 3 September continuation moves to the exact digital criterion
   in [SPEC.md](SPEC.md), retaining the final same-set target.

These are attributed checkpoint results. The history import inspected their
statements and conclusion sections; it did not independently reprove the
universal covering theorem.

## What is closed, and what is not

The positive-volume covering certificate is closed for the stated tower and
counting architecture. The earlier conditional implication remains a valid
historical implication, but its proposed hypothesis is no longer an open route
under those assumptions.

The obstruction does not count the actual image of an arbitrary sparse lattice
subset and does not disprove $P_+$ compression. No successful fixed input/output
automata are present in the recovered checkpoint.

## Next useful result

Supply one fixed graph pair with a proved exact carry invariant and
$\lambda^3<\mu^2$, then finish the real-set implication. Alternatively, prove a
scoped obstruction to that exact regular-language model. Do not replace the
target with a finite local image count or run another positive-volume box search.

## Dependencies

The two linked checkpoints contain the relevant counting setup and the proposed
digital implication. Their underlying unit-distance and Phase A sources are
recorded in [the recovery index](../../HISTORY_SOURCES.md). The original
unit-distance paper is not redistributed. External novelty is unverified here.

</details>

## 2026-09-16 addendum — finite three-branch characteristic-zero lift

The [offline three-branch report](../../notes/2026-09-16-three-branch-lift/README.md)
proves a finite gadget for the unchanged plus-sign cubic: seed
\(A=\{0,2\}\), branches \(F_r(x)=x/2+r/3\), six disjoint enlarged inputs,
and exactly 22 outputs across all nine blocks, versus \(9|P(A,A)|=36\).
Complete difference-slice containments explain the gain. This is a **PROVED
finite result**, with exact rational certificates; it is not a power saving
on arbitrarily large real sets.

Literal repetition fails branch disjointness. New **PROVED scoped results**
cover generic seeds under fixed algebraic branches, literal same-index row
collapse even under adaptive maps, fixed-spacing progression growth, raw
3-adic density certificates, and exact linear tensor transport. The main
target remains **OPEN**; no recursive rate or profitable scalar tower
realization is supplied. The report recommends exactly one further
algebraic-factorization proof obligation, without commissioning another run.

The finite grid used 980 attempts and two composition checks. New proofs
were internally audited. The older digital and rich-fiber theorems remain
reported source results: their named complete checkpoints are unavailable
here, and were not independently recertified in this cycle. Historical
sections and the original SPEC remain unchanged.

## 2026-09-16 continuation — asymptotic use of the three-branch gadget

The later [continuation report](../../notes/2026-09-16-three-branch-continuation/README.md)
classifies all fourteen savings in the six-point gadget. **PROVED internally
and independently audited:** literal iteration has exact input count
\(n_m=4\cdot2^m+2\) and actual image
\(s_m=n_m^2-O(n_m^{3/2})\), hence \(\lambda=2,\rho=4=\lambda^2\).
This strengthens the earlier disjointness failure to a scoped failure even
when input overlaps are allowed. Sufficiently separated copies have exact
support \(6n^2+3s\), or \(6n^2+3s_a\) after a common scale; that repair also
fails.

A bounded inventory of translated-slice displacement rules gives only
linearly many identifications. This is a **PROVED certificate obstruction**,
not an actual-image lower bound for all adaptive affine constructions.
**EXPERIMENTAL exact:** nine stage-dependent rational rules were evaluated
for three levels each, up to 162 inputs; no sustained normalized gain was
found. The 27 steps used 265,392 polynomial evaluations, without repeating
the prior grid.

No positive uniform rate or arithmetic amplification was obtained.
**T01 remains OPEN.** One quadratic output-preserving pair-map family was
derived symbolically; useful Cartesian partial returns remain unproved.
The current report's single next obligation concerns those returns and
supersedes the prior cycle's recommendation for this continuation only.
It commissions no further run. Historical records and previous proofs/data
remain unchanged; verification and retained source gaps are linked in the
new report.

## 2026-09-20 source-recovery intake

The received T01 addendum and manifest report recovery of the complete digital
checkpoint, rich-fiber checkpoint, Norm–Trace program/output and related
historical records. This intake contains the addendum and manifest, preserved
under `local-only/migration/recovery_2026-09-20/T01/`, but not those reported
original artifacts. Their locators and hashes are now registered as recovery
provenance; local original-byte availability remains open under MC-06. The
addendum has a 10 September mathematical cutoff, so it does not supersede the
16 September finite-gadget records or change the **OPEN** cubic target.


## 2026-09-21 documentation freeze - three-branch continuation

The [final Markdown report](../../notes/2026-09-21-three-branch-freeze/Three_Branch_Continuation_Freeze.md),
[PDF](../../../output/pdf/Three_Branch_Continuation_Freeze.pdf), and
[freeze summary](../../notes/2026-09-21-three-branch-freeze/FREEZE_SUMMARY.md)
preserve the completed 16 September continuation. The finite six-point
gadget has 22 outputs; literal iteration has actual rates
$\lambda=2,\rho=4=\lambda^2$; sufficiently separated copies have exact
image $6n^2+3s$. Bounded inventories of fixed displacement rules supply
only $O(N)$ identifications, a certificate limitation rather than a
universal actual-image theorem.

The exact pair symmetry $P\circ T_\tau=P$ and its additive composition
law are PROVED in the source system. Full finite-square invariance fails
for $\tau\ne0$; partial Cartesian returns remain OPEN. The sole next
obligation is the frozen $R_1(N)$ positive-limsup versus vanishing question.
It was not attempted. **T01 remains OPEN.**

This was strictly offline documentation and PDF production. No proof search,
new independent proof audit, carrier test, experiment or research regression
was performed. Historical proofs, data and statuses remain unchanged.


## 2026-09-21 new research — uniform cubic Cartesian-return obstruction

The separately commissioned offline [Cartesian-return report](../../notes/2026-09-21-cubic-returns/README.md)
answers the frozen return question: **PROVED**, for every finite real
\(A\), \(N=|A|\), and every \(\tau\ne0\),
\(E_\tau(A)\le5N^{11/6}\), uniformly even for an adaptively chosen step.
Thus \(R_1(N)\to0\). The proof uses an explicitly derived planar-graph
count and checked quadratic-curve degeneracies, and was independently
reviewed internally in this task. It is not a novelty or external-review claim.

At most \(10N^{11/6}\) pairs lie in nontrivial fixed-step paths. Almost-all
coverage by long such paths is **FAILED**, as is coverage using
\(o(N^{1/6})\) chosen steps. Individual linear-size paths remain possible.
Third-integer intervals prove the lower bound
\((4\sqrt2/3)N^{-1/2}+O(N^{-1})\) for \(R_1\); the sharp exponent is OPEN.

Different graph components can share outputs. No actual-image lower bound
or original cubic power saving follows. **T01 remains OPEN.** The one next
obligation for this cycle is **CR-O1**, the explicit growing-step coverage
witness in report §13. No such witness or arithmetic amplification was
attempted after the obstruction was established. The earlier freeze and
three-branch results remain intact; only its open-return question is superseded.

Exact finite evidence: 130 approved candidates, at most 129 inputs,
823,227 charged pair checks and 9.047958 research-run CPU seconds. The old
three-branch grid was not rerun. Regressions and proof-audit scope are
separately recorded in the report's verification companion.


## 2026-09-21 later research — growing-step Cartesian coverage

The [new growing-step report](../../notes/2026-09-21-growing-step-cubic/README.md)
keeps CR-U1 frozen and proves a new joint-step bound
\(\sum_{\tau\in S}E_\tau(A)\le9N^2M^{2/3}+NM+12N^2\),
\(M=|S|\). This improves the large-inventory edge exponent but **does not
improve the universal \(N^{1/6}\) coverage threshold**.

New **PROVED actual-image obstructions**: integer and third-integer APs
already have complete fibers connected by \(T_1\), with exact image
\(N^2-E_1\); arbitrary affine-lattice sets of diameter
\(D=o(h^3N^2)\) have image \(N^2-o(N^2)\); faithful fixed-rank coefficient
boxes have explicitly classified fibers and quadratic images; fixed rational
additive completion has image \(N^2-O(N^{3/2})\). A full consecutive
output-by-difference grid supplies at most \(4N^{4/3}\) prescribed pairs,
a scoped coverage obstruction rather than a general actual-image theorem.

The subgroup generated by the steps supplies a coset invariant, not automatic
finite-fiber connectivity; a concrete cubic counterexample corrects the
active prompt's stronger assertion. All new main proofs were independently
checked internally. No novelty or external-review claim is made.

**T01 and CR-O1 remain OPEN.** No asymptotic positive-proportion growing-step
carrier was obtained. The sole next obligation is the prioritized
sublinear-inventory subcase of CR-O1 stated in report §14; the broader
original obligation also remains unresolved. Exact diagnostics used 32
carriers, 192 inventories, 702,259 charged checks and 2.232581 research CPU
seconds. No old grid or fixed-step proof was rerun; no arithmetic
amplification was started. Earlier reports and data remain unchanged.


## 2026-09-21 later research — sublinear cubic symmetries and coordinate reuse

The separately commissioned offline [sublinear-symmetry report](../../notes/2026-09-21-sublinear-cubic/README.md)
keeps T01 and CR-O1 **OPEN**. No almost-full polynomial-component witness
or universal inventory exponent above 1/6 was obtained.

New **PROVED** actual-image obstructions cover deliberately nonfaithful
quadratic coefficient projections, an explicit many-to-one three-parameter
projection, and critical rational shrinking scales. Balanced unscaled
quadratic boxes have image \(N^2-O_D(N^{3/2}\log(2N))\); if
\(h^2L\ge\kappa>0\), a positive fraction of pairs have uniformly bounded
actual fibers. A changing-prime denominator theorem confines all collisions
to disjoint residue-class squares and gives image
\(N^2-O(N(1+\sqrt{W/p}))\) under its stated prime/width hypotheses.
The precise formula and scopes are SC-D1/D2 in the report; no universal
rational or real no-go is asserted.

New **PROVED** graph coverage bound:
\(V\le10|S^+\cap(0,t)|N^{11/6}+Q_A(D^{1/3}+\sqrt{2D/(3t)})\).
For separated nonlattice sets of width O(N), positive-density coverage
requires order \(N^{1/6}\) steps below a suitable constant times 1/N.
The exact fourth-coordinate marked-incidence condition is retained; the
universal threshold does not improve. New affine coordinate-reuse and
shared-edge matching restrictions are also proved.

All main new proofs were independently audited internally. The exact new
grid used 36 model records (35 distinct carriers), 216 graphs, 37,243
polynomial evaluations and 349,851 charged research checks. Five small
prime-denominator audits and regressions are separately recorded. No prior
grid, closed family search, internet work or arithmetic amplification was
restarted. The sole next obligation remains CR-O1's explicit sublinear
inventory and almost-full large-component witness, report §15.


## 2026-09-21 nonlinear coordinate-reuse cycle

The newly commissioned offline [nonlinear-reuse report](../../notes/2026-09-21-nonlinear-reuse/README.md)
keeps **T01 OPEN**. It proves complete fixed-output polynomial/rational
coordinate-sharing classifications, including an explicit nonlinear
exceptional cubic family. That family has exactly 2m selected pairs,
m <= N <= 3m scalars and two selected outputs; its quadratic complement
prevents the prescribed coverage certificate from giving a power saving.
Its actual full-image asymptotic is not classified.

For all real polynomial U,V of total degree at most two, dependence of
U^3+V on an affine/quadratic polynomial statistic forces the pair itself
through one parameter. Each such chart supplies at most 2N distinct
pairs in A². A library of o(N) such charts cannot approach full coverage.
The separate rational-grid theorem forbids independently prescribing a
nonconstant rational scalar X(r) and output Z(s) with a rational other
coordinate; at bounded degree d it bounds working labels by
7d max(|R|,|S|), for each orientation separately.

All major new proofs were independently audited internally. The exact
new grid used 16 chart records, 12 carriers and 924 cached full-square
polynomial evaluations; the exact coefficient audit used 517 operations.
No internet, closed-family search rerun or arithmetic amplification was
used. Finite examples do not prove asymptotic failure beyond the stated
classifications. Earlier reports remain unchanged.

**NR-O1 / OPEN** is now the sole adopted next obligation for this direct
nonlinear-reuse direction: a near-full explicit pair set with
O(N^(2-delta)) uncovered pairs and O(N^(2-epsilon)) selected outputs,
for fixed positive exponents, with every scalar/projection/chart cost
charged. A small symmetry inventory is not required. The earlier CR-O1
graph subcase remains OPEN; this priority change does not resolve it.


## 2026-09-30 near-complete nonlinear-chart cycle

The commissioned offline [near-complete-chart report](../../notes/2026-09-30-near-complete-charts/README.md)
keeps **T01 OPEN**. No near-full compressed subset was found.

**PROVED, internally independently audited:** all polynomial automorphisms
preserving the cubic are affine in the difference on each output fiber.
Any growing library preserving a common finite controlled set generates
classes of size at most two. Polynomial output relabeling permits at most
four-point orbits and still has a per-orbit output certificate costing at
least N²/2. These are certificate obstructions, not actual-image lower bounds;
partial returns and rational maps with poles remain outside the scope.

A separate **PROVED support obstruction** gives Z>=Q²/(DQ+2D²H) for
disjointly assigned chart pairs, per-chart fiber cap D, and total pairwise
chart-output overlap H. Near-full Q, D=N^o(1), and H<=N^(2+o(1)) force
selected support N^(2-o(1)). The overlap premise is not asserted for
arbitrary cubic carriers. Bounded degree or linear chart count alone
does not supply it.

Six new exact all-pair completion scouts used 5,338 polynomial evaluations.
All stopped after first completion: scalar expansion left only about 2–4%
prescribed coverage. Complete full-square fiber histograms and cumulative
coverage curves are retained. This finite evidence is not an asymptotic
failure theorem. No old grid, arithmetic amplification or network work ran.

**NC-O1 / OPEN** is the sole next obligation, an equivalent form of NR-O1:
construct growing real A_N with fixed eta,gamma>0 such that pair mass in
actual cubic fibers smaller than N^eta is O(N^(2-gamma)). The proved
fiber-tail equivalence supplies a near-complete subset and a power saving.
This reformulates the witness obligation; it does not resolve NR-O1 or CR-O1.


## 2026-09-30 elliptic and complex geometry cycle

The later [elliptic-geometry report](../../notes/2026-09-30-elliptic-geometry/README.md)
keeps **T01 OPEN**. This cycle was explicitly commissioned and offline.

**PROVED, complete arguments inspected by the lead:** mixed poles exclude
global polynomial scalar factorization through elliptic sums/differences,
including nonzero isogeny twists. Untwisted finite charts obey the actual
scalar coverage bound d(4d+h)N; chart count and degree growth must be charged.
Injective sum rules and injective difference rules on sets with O(N)
differences have degree-independent quadratic coverage deficits.

The sharing curves are generically elliptic although actual output fibers
are rational. Exact Weierstrass, singularity/genus and real-descent formulas
are retained. The c=6 rational elliptic orbit supplies two fibers, which
can control at most 2N real scalar pairs. Eight exact finite scouts used
1,444 P evaluations and supplied complete scalar-square fiber distributions.
Their observed near-quadratic images are not asymptotic lower bounds.

EG-O1 remains the near-complete actual fiber-tail witness NC-O1, expressed
as a growing elliptic-sharing network. No positive exponent, arithmetic
amplification, novelty claim, or change to another track is made.


## 2026-10-06 compatibility of multiple sharing curves

The [focused offline report](../../notes/2026-10-06-sharing-compatibility/README.md)
keeps **T01 OPEN** and preserves the accepted elliptic-geometry results.

**PROVED, internally independently checked:** the real ordered-output map
(a,b,c)→(P(a,b),P(b,c),P(c,a)) is injective. For the selected fixed output
gap 2r, r=1/sqrt(3), simultaneous compatibility forces exactly the common
translates of (−r,0,r). Any nonempty finite assembly has Z=N and Q≤2N−3; the
consecutive strip attains this sharp linear bound. Thus its prescribed
fibers leave N²−O(N) pairs uncharged by that mechanism.

The strip's full image is N²−O(N^(3/2)), by the prior GS-A4 theorem
specialized and checked in SH-C3; no former progression inventory was
reopened. Eight exact full-square checks of this one network realization
used 6,022 P evaluations after the compatibility equations were saved.
SH-O1 asks about a uniform quadratic actual-image bound for arbitrary
translate sets within the same family. It is the cycle's one retained
question, not a new constructive reduction or a resolution of EG-O1.


## 2026-10-06 variable-gap shared-edge cycle — T01 remains OPEN

The [new report](../../notes/2026-10-06-variable-gap-sharing/README.md)
uses one output-first family and a coordinated three-agent/lead audit.
PROVED: N=k³, Q=2k⁴−k²−k, Z=2k³−k, with simultaneous shared-edge
compatibility, growing partners at every edge and local partner cross-pairs.
This surpasses linear prescribed-pair families but matches the prior GS-P3
N^(4/3) scale. The complement remains quadratic, and the actual interval
carrier has N²−O(N^(3/2)) outputs by inspected GS-A4.

VG-G2 verifies the formerly tentative real uniqueness statement for cycles
of every length. Variable output labels remain outside that fixed-list
restriction. Three exact complete squares used 20,450 P evaluations and
9,349 checks; no old research search was expanded.

The sole next obligation VG-O1 is the explicit finite real-deformation
system on 27 ordered vertices, 150 selected pairs and 51 moving output
classes. It is OPEN and conveys no asymptotic gain. Accepted elliptic and
fixed-gap checkpoints are preserved; the original cubic target is OPEN.


## 2026-10-06 changed-collision round — finite bridge, T01 OPEN

The [new checkpoint](../../notes/2026-10-06-changed-collision-pattern/README.md)
checks the user-proposed VG-O1 rigidity argument completely: the old
increasing real pattern forces x_i=i. This resolves that finite question
without changing the earlier source files or closing other real networks.

A different conic coincidence pattern produces an exact six-scalar non-AP
bridge with eight controlled pairs and three outputs, one represented by
four pairs across different centers. Its compatible fixed-width ladder has
N=2m+2,Q=4m,Z=m+1. The actual image is at leastN²/4 by an injective
half-size AP square, so that extension is stopped. No improvement over
GS-P3's N^(4/3) prescribed-pair rate or fixed power saving is obtained.

The lead, construction specialist and proof/computation referee worked on
this one pattern offline. Compatibility preceded finite evaluation; no
arithmetic tower, package installation, global elliptic restart or old
carrier sweep was used. CP-O1 is the one remaining finite diagnostic:
a variable-width third frame sharing two seed scalars and adding a third
first-coordinate row to the zero fiber. It has not been solved or tested.


## 2026-10-11 bounded transfer, division and entropy cycle

The [new checkpoint](../../notes/2026-10-11-transfer-division-entropy/README.md)
keeps **T01 OPEN** and resolves the preceding finite CP-O1 obligation.
**PROVED, internally audited:** no stipulated variable-width frame can
reuse two scalars of the exact six-point seed and add a third first
coordinate to its zero fiber. Monotonicity reduces all role assignments
to five systems; exact Bezout certificates exclude each. This supersedes
the preceding CP-O1 OPEN statement in that scope only.

One exact real 3-torsion/division scout on the existing c=6 sharing curve
has 14 scalars and 188 outputs from all 196 pairs: 186 singleton fibers
and two fibers of size five. Translation does not evade the existing
pole obstruction. This finite result is not an asymptotic image theorem.

The quadratic arithmetic baseline and b<2a transfer gate were reconstructed
using the identified supplied tower theorem. The requested Pohoata and
projection-paper versions were unavailable locally and were not claimed
audited. An elementary projection-to-support implication charges scale,
population, strip inventory and exceptional mass; its needed subquadratic
estimate remains absent. No external projection theorem is imported.

The sequential offline cycle used 598 exact P evaluations, including a
separate arithmetic audit, with no search expansion. Only this pointer
and the new note directory were changed. The one retained next obligation
is EG-O1 / NC-O1: a growing actual all-pair fiber tail, including isolated
pairs. Earlier reports and other tracks remain unchanged.


## 2026-10-11 torsion compatible sharing cycle

The later [report](../../notes/2026-10-11-torsion-compatible-sharing/README.md)
keeps T01 OPEN. A lead, elliptic/compatibility specialist and exact referee
checked the actual CP sharing locus before any scout. Fixed outputs have
at most four admissible real frame points; the general one-row completion
requires a genus-four cover, with genus 1+3e after a degree-e isogeny.
This is a scoped compatibility obstruction, not a global-factorization restart.

A different-width finite attachment is uniquely forced by two old scalar
coincidences: N=6,Q=8,Z=2,B=28, actual full image 30. Both controlled fibers
have size 4; the other 28 pairs are singleton fibers. No third width at
those fixed outputs or unbounded extension is supplied. The accepted
N^(4/3) benchmark is not improved.

The bounded exact audit used two parameter cases, orders 2,3,4, 144 P
evaluations and 652 exact checks. No compatible division or torsion-translation
matches of these orders survive. The prior B-CP proof is imported and
its five certificates independently multiplied; the original CP-O1 remains
closed. TC-O1 is one remaining diagnostic: decide arbitrary-order torsion
of the new attachment's specified point difference. No asymptotic inference
or broad torsion classification is claimed. Earlier artifacts are preserved.


## 2026-10-11 marked shift cleanup

**PROVED — MS-C1 / TC-O1 resolved:** the TC-G5 exact marked difference
T=R2−R1 has infinite order. The
[new report](../../notes/2026-10-11-marked-shift-certificate/README.md)
identifies its degree-eight joint coordinate field and gives a single-prime
all-orders certificate: a good Q23 embedding has v23(X(4R2))=−2,
and a field conjugation gives T+sigma(T)=2R2. The supplied local
formal-logarithm proof and every arithmetic hypothesis were independently
checked by the lead and referee. No mathematical program or order search
was run.

This dated resolution supersedes the preceding TC-O1 diagnostic only.
The two-width bound, genus-four completion obstruction and finite ledger
are preserved. T01 remains OPEN with no new asymptotic mechanism.
The requested point is resolved and this cleanup stops here.


## 2026-10-11 torsion/frame documentation freeze

The [professor-facing freeze package](../../notes/2026-10-11-torsion-frame-freeze/README.md)
contains a five-page main report, six-page technical proof appendix with
source/status ledger, and one-page meeting summary, each in PDF and Markdown.
MS-C1 is frozen as PROVED in the supplied source system: the exact
T=R2−R1 has infinite order and TC-O1 is resolved. T01 remains OPEN.

This is documentation only. It distinguishes the fixed-output two-width/four-
marked-point theorem from the genus-four general-row completion obstruction,
and retains the N=6,Q=8,Z=2,B=28 ledger and inherited exact full image 30.
The all-orders certificate and its prior internal referee audit are reported
without a new proof audit or mathematical rerun. Historical proofs and data
are preserved; no successor research cycle or commit is initiated.


## 2026-10-11 varying-output frame network cycle

The [new report](../../notes/2026-10-11-varying-output-frames/README.md)
keeps T01 OPEN. A lead, compatibility specialist and independent exact
referee coordinated one output-first pattern offline. Three prescribed
outputs admit an exact eight-scalar junction; the closing frame adds two
new cross-block pairs without adding scalars, giving Q=10,Z=3,B=54.

**PROVED — VO-C1–C5:** its same-rule extension has N=4m,Q=6m−2,
Z=m+1; actual image≥N²/16; all frame-only closure within that same pool
still gives O(N) pairs. Keeping the two selected outside-row identities
forces equal adjacent gaps. Thus this continuation is stopped, with no
improvement on the N^(4/3) selected-pair benchmark or asymptotic saving.

**EXPERIMENTAL — VO-X1:** the three predeclared complete-square audits
m=2,3,4 have full images 53,122,223. One exact run used 928 P evaluations
and 602 explicit predicates, totaling 1530 of the 5000 budget. No larger
case, role sweep, package, internet, rank/CM search or arithmetic tower
was used. VO-O1 is one untested mixed row/column junction, specified in
the report; it is not a fiber-tail reformulation or a claimed extension.
The earlier frozen MS-C1 and geometric proofs are preserved unchanged.


## 2026-10-11 VO-O1 verification and documentation freeze

**PROVED - VO-C6; VO-O1 resolved negatively.** The
[short freeze note and PDF](../../notes/2026-10-11-vo-o1-freeze/README.md)
contain the complete supplied proof, checked independently by the lead
and a mathematical referee. The original signed-role equations reduce
to H=k+g(h)=s+g(k), g(H)=g(h)+g(k), with positive conic widths and
g(w)=2w−4w³. They force both H<1/2<h and H>h, a contradiction.
Cancellation, signs and strict boundary exclusions are audited explicitly.

Unequal gaps and the extra endpoint/pair constraints are not needed.
The old VO-O1 OPEN statement remains preserved as history. Earlier
N=4m,Q=6m−2,Z=m+1 and image≥N²/16 results are imported separately,
not inferred from this contradiction. T01 and other role patterns remain
OPEN. No enumeration, metric-entropy programme, constructive search or
next cycle is performed. No standalone attached proof file was located;
the complete inline proof supplied in the user message was verified.


## 2026-10-20 tetrahedral mixed-role test

**PROVED — TJ-C1–C4; four registered cases FAILED.** The
[new report](../../notes/2026-10-20-tetrahedral-junction/README.md)
tests outputs (0,a,a+b,2a+b), two signs for opposite-edge row/column
sharing, and two explicit zero-new-scalar closing patterns. Every
admissible width branch of those simultaneous systems is excluded.
The common bounds give H<1/2. Pattern A contradicts
p+g(p)≤1<S+g(w); pattern B forces both 3C(H)+C(w)<8 and >8.
These are new scoped arguments, not another use of the VO-O1 subsystem.

The lead, construction specialist and independent referee checked the
exact equations and strict signs. No seed survives: N,Q,Z,B and a full
fiber histogram are not defined, and no growth attachment was run.
The four-case catalogue was fixed before solving; the conditional
5,000-unit seed enumeration budget was not activated. No improvement
over the N^(4/3) prescribed-pair benchmark is claimed.

**OPEN — TJ-O1:** one untested modification replaces pattern A's
closing columns from the outward rows of 02/13 by their outward columns,
keeping epsilon=-1 and H=r. Its exact finite gate is in the report.
This records an obligation, not authorization for another cycle.
T01 remains OPEN. Earlier VO-C3–C6 and torsion/frame proofs are preserved.


## 2026-10-21 TJ-O1 verification and freeze

**PROVED — TJ-C6; TJ-O1 PROVED IMPOSSIBLE in its exact scope.**
The [proof note](../../notes/2026-10-21-tj-o1-freeze/README.md)
verifies the supplied contradiction for epsilon=-1 and H=r,S=e+q,
with the retained (a,b,a) output rule and conic/role equations.
C(H)>2, C(p)<2 and S>q force p>H and then p>1/2.
Thus q+g(p)<1, while H=r forces S+g(w)>1.
The gap and closing equations identify these two quantities.

An algebraic referee and a separate proof-checking agent independently
accepted every implication and strict sign; the lead also checked the
complete argument. The extra pair and third-row restrictions are unused.
The earlier OPEN entry and tetrahedral checkpoint remain unchanged as
history. Other roles and the general T01 target remain OPEN.
No construction search, numerical run, or successor obligation was begun.


## 2026-10-21 — actual-fiber multiscale checkpoint

**PROVED — MC-S1–MC-S3.** A cubic fiber occupies at most eight children
when each scalar interval is quartered. The prefix-tree argument gives
`#{pairs with at most b actual same-output branch events} <= |P(A,A)| 8^b`.
Thus a full image at most N^(2-c) requires more than
floor((c-gamma) log_8 N) branch generations on all but N^(2-gamma) pairs,
for each 0<gamma<c. The local version charges terminal cluster capacities
and repeated actual output labels across coarse cells. It does not locate
scales, imply concentration, or construct a witness.

[Report and complete proof](../../notes/2026-10-21-multiscale-collisions/README.md).
**EXPERIMENTAL:** six exact full-square diagnostic cases, independently
matched on all 533 ordered-pair outputs. The requested Raz–Zahl text is
**MISSING SOURCE**; no theorem exponent is applied. **OPEN — MC-O1:** the
specific two-map collision-rectangle bound in report §6, not yet tested.
TJ-C6 remains frozen and the unrestricted T01 target remains **OPEN**.


## 2026-11-05 — archival cross-reference

The [public evidence index](../../EVIDENCE_INDEX.md) and [dated export](../../reports/2026-11-05-evidence-export/README.md) organize the source claims above. The publication pass checked locators, data packaging and archive integrity; it introduced no new proof, experiment or change to this track’s OPEN target.
