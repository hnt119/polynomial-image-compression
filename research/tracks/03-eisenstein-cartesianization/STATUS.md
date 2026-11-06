# T03 status — full-rank quadratic / Eisenstein norm

**7 November 2026 · fixed target OPEN.** BFF-O1 retires the balanced-factor carrier. MS-O1 supplies units, MS-O2-I asks about occupied labels, and RC15/4 is a separate adaptive obligation. [Restart record](../../OPEN_LEMMAS.md#restart) · [Evidence and later checkpoints](../../EVIDENCE_INDEX.md). The dated record follows.

Reconciled **11 September 2026**, cutoff **10 September**. **Fixed target: OPEN.**

$$Q_E(x,y)=x^2+xy+y^2.$$

The [SPEC](SPEC.md) preserves one fixed positive exponent and arbitrarily large
same-input finite real sets. Its approximate PTCR construction remains OPEN,
but is **HISTORICAL / SUPERSEDED as the selected direction**. The latest
frontier is adaptive radicals and the T03-O4 full signed-root support lemma
RC15/4. No fixed polynomial or conjecture is changed.

**Authority:** `T03_CURRENT_STATE.md`, identical to the frozen copy in
`T03_RESEARCH_RECORD_20260910.zip::output/`, and the five TCRC reports listed
in [the source registry](../../MIGRATION_CONFLICTS.md#source-registry).
`PROVED` means proved or accepted as a frozen result in that record, not newly
reproved or externally certified by this migration.

## PROVED adaptive construction and exact finite ledger

For nonempty symmetric $A$, put $M=\max|A|$, choose $C>M$, and define

$$d_C=C-M,\quad
\mathcal L_C(A)=\{\pm\sqrt{(C+a)/d_C}:a\in A\},$$

$$\mathcal T_C(A)=\{2C+a+b\pm\sqrt{(C+a)(C+b)}:a,b\in A\}.$$

The lift has exactly $2|A|$ distinct inputs, and
$Q_E(\mathcal L_C(A),\mathcal L_C(A))=d_C^{-1}\mathcal T_C(A)$.
Starting at $\mathcal A_0=\{\pm1\}$, the recorded exact finite algorithm
chooses the legal parameter minimizing next image size, with its fixed tie
rule. On these actual adaptive levels, $n_m=2^{m+1}$ and
$s_m=|Q_E(\mathcal A_m,\mathcal A_m)|$ have certified values:

| $m$ | $n_m$ | $s_m$ | Next optimizing parameter $C_m$ |
|---|---:|---:|---|
| 0 | 2 | 2 | $5/3$ |
| 1 | 4 | 5 | $5/2$ |
| 2 | 8 | 17 | $4$ |
| 3 | 16 | 68 | $3$ |
| 4 | 32 | 269 | OPEN / not determined in the supplied record |

These finite values have exact certificates in the frozen record; they are
not an asymptotic theorem. No certificate program was rerun here.
Source: current state §§3–4.1 and inherited ARDC/DSCR records.

For square-class sizes $c_j$ of $C+A$ in exactly
$K^\times/K^{\times2}$, $K=\mathbb Q(A,C)$, write
$W=|\mathcal T_C(A)\cap K|$. **PROVED:**

$$|\mathcal T_C(A)|=n^2-\sum_jc_j^2+W,\qquad
\mathcal T_C(A)\cap K=\bigcup_j\gamma_jQ_E(U_j,U_j).$$

Both root signs and the factors $\gamma_j$ are essential. A saving down to
at most $n^2$ requires $C\in\mathbb Q(A)$: genuinely quadratic parameters
outside that field give at least $n^2+1$ outputs; degree at least three or
transcendental parameters give all $n(n+1)$ branch values. A dominant square
class alone does not control $W$.

## PROVED latest finite root results; exact FAILED scopes

- One-copy inherited-root covers exist at specified parameters, but direct
  parent intersection covers at most half the old input and cannot alone give
  sublinear exceptions. A small root subset is not the full branch image.
- At $\mathcal A_1,C=17/8$, exactly four affine copies are needed for the
  specified 12-value root support. At $\mathcal A_3,C=3$, exactly five are
  needed for the specified 17-value root support. These parameter-specific
  failures do not refute eventual TCRC with other parameters.
- At $\mathcal A_3,C=4$, the 41-value root image fits in one old-image copy,
  but ten exceptional inputs contribute 230 labels, giving full image 271
  rather than the optimizer's 269.
- At the next actual input $\mathcal A_4,C=4$, exact field tests give
  $\sum c_j^2\le128$, $W\ge33$, and hence at least
  $1024-128+33=929>3s_4=807$ outputs. This does not compute $C_4$, reject
  other parameters, or refute an eventual recurrence with error terms.
- Fixed $t$ polynomial same-pair templates of coordinate degree at most $D$
  capture at most $4Dtb$ branch labels on a $b$-element class. Full coverage
  needs $b+1\le4Dt$. Arbitrary history-dependent assignment to other old pairs
  is outside this obstruction.
- Zero-sum completion gives at least $r(r+3)/2$ completion blocks for $r$
  positive roots. This is a block-count lower bound, not an image lower bound:
  distinct blocks may have equal values. Completion alone is an insufficient
  support certificate.

Sources: current state §§4.3–4.6; `TCRC_Finite_Covers_m1_m2.md`,
`TCRC_Finite_Covers_m3_m4.md`, `TCRC_History_Parameters.md`,
`TCRC_Root_Algebra_Pair_Maps.md`, `TCRC_Triangle_Closure.md`.

## OPEN selected obligation and CONDITIONAL consequence

T03-O4 asks for fixed $H<\infty,m_0$ and, at every actual $m\ge m_0$,
an explicit legal $C_m^\dagger\in F_m=\mathbb Q(\mathcal A_m)$, a subset
$B_m\subseteq\mathcal A_m$ with at most $H\sqrt{n_m}$ exceptions, and
positive $\gamma_m,u_a\in F_m$ with $C_m^\dagger+a=\gamma_mu_a^2$.
For $U_m=\{\pm u_a:a\in B_m\}$, require the full signed image bound

$$|\gamma_mQ_E(U_m,U_m)|\le\frac{15}{4}s_m+Hn_m^{3/2}.$$

**CONDITIONAL:** the exact exception charge and one-step optimality give
$s_{m+1}\le\frac{15}{4}s_m+4Hn_m^{3/2}$, hence
$s_m=O((15/4)^m)$ and every $c_E<\log_2(16/15)$ eventually.
A safe conditional exponent is $\frac12\log_2(16/15)$.
The uniform parameter/class/root-image rule remains **OPEN**; the displayed
exponent is not a completed construction. Isolated good steps or alternate
descendants do not justify iteration.

Stronger eventual TCRC, adaptive geometric growth below 4, general weighted
local questions, approximate PTCR, arbitrary-prime mixed-difference coherence,
and full-progression ARDC/DSCR remain **OPEN** as recorded alternatives.
Only T03-O4 is selected as the current constructive obligation.
Source: current state §§7, 13–14; [open-lemma registry](../../OPEN_LEMMAS.md).

## Historical FAILED routes retained with boundaries

| Route | Exact failed scope; what remains outside it |
|---|---|
| Full-input norm sieve / CRT lattice packing | Fixed complete splitting, arbitrary decomposition, and field-dependent-prime variants of the specified certificate; not all arithmetic carriers |
| Common-box norm-one invariance | The stated denominator/common-core construction; non-invariant direct support counts remain possible |
| Local restrictions / weighted defects | One-place settled inequalities, and weighted no-defect results at residues 7 and 13 at all depths; not universal correlated CRT or all-ring weighted theorems |
| Height-restricted inputs | Polynomial-height integers/common-denominator rationals, or polynomial-house integral sets in one fixed totally real field; arbitrary rational sets are not excluded |
| Untwisted CR and exact PTCR | Rational untwisted deficit at least $n^2/3+2^m$; exact PTCR impossible for $m\ge2$. Approximate power-deficit PTCR remains OPEN |
| Code composition | Imperfect block repetition, natural/endpoint-local rules, scalar digits, core-faithful lifts, and cheap equal-norm repair under their stated constraints; not arbitrary global repacking |
| Mixed-difference reconstruction | Specified-prime MDCO and code-independent reconstruction without quadratic calibration; not arbitrary-prime cancellation |
| Deficit recursion | Coefficient 4 retains normalized old loss; a strict coefficient below 4 with actual growth remains sufficient conditionally |
| Repeated complementary radicals | The specific nonoptimizing family has image at least $N^2/8$; not an obstruction to the actual adaptive family |
| Dominant class alone | An auxiliary $b=1$ family can have maximal image; dominance plus a proved whole-root bound is a different condition |

The [failure library](../../FAILURE_LIBRARY.md) retains all individual scopes.
Earlier PTCR/repacking history below is preserved, including its finite example
and open triangle-gap alternative.

## Corrections, provenance, and shared boundary

**HISTORICAL / SUPERSEDED:** Ferrers sufficiency for BW is one-way; near-doubling
TFQ needs an actual growing regime; corrected DSCR uses
$n^2-\sum c_j^2\le(1-b^2)n^2\le2(1-b)n^2$, not the missing-factor-two bound.
The exact outside count 224 exceeds the old erroneous 192.

**EXPERIMENTAL:** unproved finite “no defect found” observations remain
experiments; the standalone $\mathbb F_{25}$ certificate is still missing.
Finite affine mask counts 122 and 134 use different singleton conventions,
not conflicting minima. See [migration issues](../../MIGRATION_CONFLICTS.md).

Phase A/B and corrected rank-one C0 are shared progress, not solutions to
this full-rank norm target. General solvable extensions, addition/multiplication,
and norm/trace remain a possible shared direction; no transfer or new research
cycle is executed here, and no novelty is claimed.

<details>
<summary>HISTORICAL / SUPERSEDED — complete 5 September 2026 STATUS snapshot</summary>

# T03 status and history

**Ultimate Eisenstein target and PTCR: OPEN IN THE AVAILABLE RECORD.**
**Recent constructive direction: global reassignment with deficit contraction.**

## Sequence of results

1. Earlier local work develops [correlated CRT](../../history-sources/Q_Correlated_CRT_Tensorization_Checkpoint.md)
   and [weighted inequalities](../../history-sources/Q_Weighted_Local_Inequality_Checkpoint.md).
   The latter reports an all-depth residue-$13$ theorem, while retaining the
   general weighted problem as open. These are local results, not the real-set target.
2. [The constructive push](../../history-sources/Q_Final_Constructive_Push.md)
   gives a balanced code with $4^m$ engineered pairs and $3^m$ norm values.
   Its missing requirement is near-Cartesian coverage, including unengineered pairs.
3. [The CR verdict](../../history-sources/Norm_Preserving_Cartesianization_CR_Verdict.md),
   main theorem and §§G–I, refutes the original untwisted Cartesianization:
   pairs with $v_3(Q_E(a,b))=0$ have density at most $2/3$ in a rational square.
   The source's stronger code deficit is
   $$|A|^2-4^m\ge |A|^2/3+2^m.$$
   This closes that intermediate conjecture, not the ultimate $Q_E$ target.
4. The same report introduces the parity twist. It preserves the
   $4^m$-to-$3^m$ count and has the exact one-coordinate gadget $A_1=\{1,2\}$.
5. [The composition report](../../history-sources/Parity_Twisted_Cartesianization_Composition_Report.md),
   §§B–G, records obstructions to Exact-PTCR for $m\ge2$, natural binary
   placement, endpoint-local/affine recursions, and ordinary repetition of a
   fixed imperfect block. Arbitrary near-Cartesian reassignment remains open.

These are attributed source results; the import does not certify every proof or
rerun the historical C++ searches.

## Concrete finite example

For $(r_1,q_1)=(2,7)$ and $(r_2,q_2)=(5,31)$, the composition report, §C, gives

$$A_2=\{-25,-10,-5,-2,-1,26\}.$$

It realizes the 16 required directed code cells, with nine engineered norm
values. Its deficit is $6^2-16=20$ and its full $Q_E$ image has 19 values.
The report proves minimality among **integer** carriers for its prescribed
histogram; that is not a claim of minimality among all rational carriers.
No working asymptotic composition of this example is reported.

## Current next step and adversarial alternative

The latest task continuation prioritizes global repacking satisfying the strict
recurrence threshold in [SPEC.md](SPEC.md). A coefficient $4^k$ does not contract
old deficit; ordinary repetition of an imperfect block loses density.

Preserve also the report's §I **cube-shadow triangle-gap lemma** as an open
adversarial alternative. If established under its precise permutation-invariant
hypotheses, it would refute PTCR. It would still not disprove arbitrary
Eisenstein norm compression. The next constructive prompt did not settle or
erase that alternative.

</details>

## 2026-09-16 addendum — HR-N1 is false in its fixed two-prime scope

**FAILED — the HR-N1 existential return-tail assertion. PROVED — HN1-2/3.**
The [strictly offline cycle](../../notes/2026-09-16-hr-n1-offline/README.md)
keeps $Q=x^2+xy+y^2$, the specified numerator bound $L$, denominator primes
$7,19$, and generators $u=(8+5\omega)/7$, $v=(21+16\omega)/19$ fixed as
commissioned. For every $L=10m$ with $m\ge2$, a class of at least
$n_L^2/200$ pairs in the original same-set square has return count exactly
one, even under all $u^rv^s$ with $r,s\in\mathbb Z$.

The [dominant-gap proof, HN1-2](../../notes/2026-09-16-hr-n1-offline/README.md#3-hn1-2--a-dominant-gap-forces-the-identity)
and [positive-density theorem, HN1-3](../../notes/2026-09-16-hr-n1-offline/README.md#4-hn1-3--positive-density-and-disproof-of-hr-n1)
exclude every proposed fixed positive return/exception exponent pair along
an unbounded subsequence. Their proofs were independently audited within
the cycle; this is internal review, not external certification.

The prior [high-return report, §7](../../notes/2026-09-16-high-return/README.md#7-one-next-proof-obligation)
is immutable historical provenance for HR-N1's earlier **OPEN, untested**
state. Its status is superseded only for this exact assertion. No actual
full-image lower bound is proved: other norm-one multipliers or compression
of exceptional outputs would need separate arguments. The actual image
rate of $A_L$, the fixed real-set target and adaptive RC15/4 remain **OPEN**.
No mathematical experiment was run and no network access was attempted.

## 2026-09-16 final freeze — return obstruction and unchanged frontier

**FAILED / DISPROVED — HR-N1; CLOSED — this specific tail certificate.**
See the [final proof report](../../notes/2026-09-16-hr-n1-final-freeze/README.md)
and [final state](../../notes/2026-09-16-hr-n1-final-freeze/final-state.yaml).
For $L=10m$, $m\ge2$, at least $|A_L|^2/200$ ordered pairs have only
the identity return under all $u^rv^s$, $(r,s)\in\mathbb Z^2$. The
quantified contradiction excludes every fixed positive return/exception
exponent pair. The completed proof and two recorded internal reviews are
frozen without a new research search or experiment.

This is a bad-pair lower bound, not an actual-image lower bound. The
quadratic target, actual rational-carrier image rate, ARG, eventual TCRC
and RC15/4 remain **OPEN**. No proved transfer from the HR-N1 rational
carrier to the actual adaptive root sets is present in the inspected
record. The report distinguishes that unavailable bridge from the proved
HR-1 support implication. T03-O4 retains its legal in-field parameter,
$O(\sqrt{n_m})$ exceptional-input count and full signed-root bound
$|\gamma_mQ(U_m,U_m)|\le(15/4)s_m+Hn_m^{3/2}$. No replacement
return conjecture is adopted; the existing obligation is not executed.


## 2026-09-16 later cycle — exact character-correlated block and realization loss

**Verdict: LOCAL GO / GLOBAL FAIL.** See the
[complete two-prime report](../../notes/2026-09-16-two-prime-character/README.md).
For $D=\{(a,b)\in\mathbb F_7^\times\times\mathbb F_{19}^\times:
\chi_7(a)=\chi_{19}(b)\}$ and the full split norm-one group
$G\cong C_6\times C_{18}$, **PROVED TP-L1** gives $|D|=54$, 108
actions, trivial stabilizers, minimum return 8, median 25, and geometric
mean approximately 21.6342 on all 2916 ordered pairs. **PROVED TP-P1**
gives exact product returns, a uniform $8^d$ bound and an explicit
$18^d$ lower-tail exception bound $2772^d$.

This positive entropy belongs to the finite-ring product. **PROVED TP-G1**
shows that a common homomorphism into real norm-one multipliers has image
at most 18; with equivariant scalar projection the exponential local label
count cannot produce exponentially many distinct real returned pairs.
The separately normalized CRT factor is $(8645/1458)^d>1$ after charging
both input densities. These are scoped certificate failures, not actual
real-image lower bounds or a failure of all possible lifts.

One complete exact diagnostic and independent oracle were run; all code
regressions and this computation stayed within the announced offline caps.
No homogeneous real saving survives, so no difference-set or affine cycle
was started. HR-N1 stays CLOSED. The fixed real quadratic target, ARG,
TCRC and RC15/4 stay OPEN. The sole next obligation remains T03-O4 with
its existing legal-parameter, large-root-class and whole-signed-image
hypotheses; this cycle neither solves nor begins that obligation.


## 2026-09-16 — independent unit actions and Cartesian valuation obstruction

**Verdict: ACTION GO / CARTESIAN FAIL.** Complete definitions, proof and
rate ledger: [unit-exponent report](../../notes/2026-09-16-unit-exponent/README.md).
For fixed $L=1$, let $P_0=1$, $t_i=3P_{i-1}^3$,
$q_i=t_i^2+t_i+1$, $P_i=P_{i-1}q_i$, and
$u_i=(t_i-\omega)/(t_i-\bar\omega)$. These are fractional units;
$q_i$ are composite-allowed coprime norm blocks. **PROVED UE-P1:** the
$u_i$ are multiplicatively independent, so their width-one action box has
exactly $3^d$ distinct actual multipliers. **PROVED UE-P2:** the norm orbit
has exact product returns, minimum $2^d$ and typical rate
$(2\log2+\log3)/3$.

**PROVED UE-P3, scoped certificate failure:** coefficient completion has
$n_d=2\cdot3^d$ scalar inputs and only $3^d$ engineered pairs. A
subexponential number of seed norm shells still covers an exponentially
small fraction of the square. This gives no actual-image lower bound for
the primary coefficient family; its asymptotic image and uncontrolled
cross-pair returns remain OPEN.

**PROVED UE-S1/S2, one secondary family:** for
$A_d=\{\pm\prod_{i\le d}q_i^{e_i}:|e_i|\le1\}$ every ordered pair
has only the identity return under all $\prod u_i^{h_i}$,
$h_i\in\mathbb Z$. Independently, its full image equals
$n_d^2/4+n_d/2$, and its signed rate gap is zero. This actual-image
failure applies to this sparse valuation box, not to all rational sets.
Complete arguments and independent internal cross-reviews are retained.

One exact diagnostic tested each of these two carriers at depths 1,2,3;
all pair/action checks used rational arithmetic and an independent oracle.
No affine work or third mutation was undertaken. The fixed target, ARG,
TCRC and RC15/4 remain OPEN. HR-N1 stays closed. The sole next obligation
remains T03-O4 with its full existing hypotheses, not started here.

## 2026-09-20 source-recovery intake

The received T03 addendum and manifest designate `T03_CURRENT_STATE.md` plus
the five TCRC companions as the complete retained final package. They also
report recovery of the exhaustive F25 source/log/executable and
`Quadratic_Tower_Arithmetic_Obstruction.md`. Only the addendum and Markdown
manifest were received in this intake, so those four originals remain absent
locally and are tracked by MC-06. This resolves the repository's final-package
designation, not the original-byte gap. Its 10 September cutoff does not alter
the later 16 September scoped results, RC15/4, or the **OPEN** T03 target.


## 2026-09-20 final Cartesian norm-symmetry checkpoint

**Frozen verdict: ACTION GO / CARTESIAN FAIL, within the proved scopes.**
The [final report](../../notes/2026-09-20-cartesian-norm-freeze/Cartesian_Norm_Symmetry_Research_Checkpoint.md)
consolidates the high-return, HR-N1, two-prime-character and controlling
unit-exponent records. No mathematical source or historical statement is rewritten.
The unit orbit supplies $3^d$ actual actions and at least $2^d$ returns,
but its engineered pairs cover only $1/(4\cdot3^d)$ of the scalar square.
This closes that coverage certificate; the primary actual image rate stays OPEN.
The secondary family's image formula $n^2/4+n/2$ is a separate proved result.

This norm-carrier search is frozen pending a genuinely new Cartesianization
principle and a separately commissioned cycle. The fixed quadratic target,
ARG, eventual TCRC and RC15/4 remain OPEN; HR-N1 remains DISPROVED.
Only **T03-O4 / RC15/4**, with all existing actual-level, in-field,
$O(\sqrt{n_m})$ exception and full-signed-root hypotheses, is retained as
the next constructive obligation. This documentation-only freeze does not
begin it or adopt a replacement conjecture.


## 2026-09-21 dense-Cartesianization research cycle

**Verdict: CARTESIANIZATION FAIL, in explicitly proved scopes.** The
[new report](../../notes/2026-09-21-dense-cartesianization/README.md)
responds to a separately authorized offline proof-search cycle, rather
than treating the frozen checkpoint as research authorization.

PROVED DC-S1/S2: separable product states with subexponential state and
coordinate-fiber counts cover at most $e^{(3a/2+o(1))d}$ pairs when
$n=e^{ad+o(d)}$. PROVED DC-B2: a fixed $k$-block partition certified only
by complete block-to-one-block transitions leaves at least $n^2/k^2$
pairs below every eventually growing return threshold. These are
certificate obstructions, not actual-image lower bounds.

PROVED DC-M1: every mixing norm multiplier has overlap at most
$\lfloor(3n^2+1)/4\rfloor$ on every finite real square. This excludes
Cartesian Følner overlap tending to one, not many partial-return domains.
PROVED DC-M4/M5: faithful bounded-digit quadratic projection has fibers
at most $m^4$; the explicit ternary integer family has actual image at
least $n^2/81$ and one distinct return everywhere under its selected
$3^d$ multipliers. The latter return statement is finite-window scoped.

PROVED DC-A1: arbitrary one-axis shifts of the injective seed-1 orbit
have at most $(n+1)^2/4$ engineered pairs; growing integer interval shifts
are exponentially sparse. Actual incidental returns and image rate for
that thickening remain OPEN. Four exact new cases were tested. No old
carrier was rerun unchanged, no positive carrier selected, and no affine
transfer attempted.

PROVED DC-R1: rectangular returns give
$|Q(A,A)|\le n^2/R+|X\setminus Y|^2+|Y\setminus X|^2+2|E|$ for
$A=X\cup Y$. **One next obligation for this branch: DC-O1**, construct
the high-overlap rectangular witness with fixed positive return and
exception exponents, as quantified in the report. The target, ARG,
eventual TCRC and RC15/4 remain OPEN. HR-N1 stays DISPROVED. The new
branch obligation neither changes RC15/4 nor restarts it.


## 2026-09-21 subsequent DC-O1 witness cycle

**RECTANGULAR WITNESS FAIL, scoped; DC-O1 itself OPEN.** The separately
commissioned [new report](../../notes/2026-09-21-dc-o1/README.md)
examines four partial-domain mechanisms, with six exact scouts in two
concrete mechanisms. Existing completed carrier searches are not repeated.

**PROVED CF-1–CF-4:** for common core C and fringe size F, distinct
fringe returns are at most 2F pointwise and at most min(M,K)nF in total,
where M counts selected actions and K bounds core norm fibers. The
prescribed-action core tail costs at most e+2min(M,K)nF/R. Separately,
rectangular support compression transfers directly to Q(C,C), without
assuming original-action returns survive intersection.

**PROVED DC-T1–DC-T3:** uniform product-domain norm preservation after
real linear scalar assembly synchronizes local rotations when one
local span is full and other spans nonzero (difference spans when zero
is absent). Rank-one reflection exceptions are explicitly bounded.
The certificate does not receive a product of local return counts.

**PROVED DC-TB1–DC-TB4:** balancing complementary alphabet states can
make X=Y, but its compatible pair fraction is at most 1/k for k disjoint
complement-closed states, and equals 1/binom(d,d/2) in the balanced
signed gadget. These are certificate counts, not actual rich-pair counts.

**PROVED MP-1:** correlated zero-sum ternary polynomial words, evaluated
at B_d=[10(d+2)]^(4d), have exponential scalar size and exactly 3^d
selected moving-pole multipliers. Every distinct-return count is at
most 27, because bounded-coefficient polynomials cannot vanish at poles
j+omega or j+conjugate(omega) for j>=4. This scalar proof covers the
finite width-one power window; no all-integer-power claim is made.

All DC-O1 positive exponents remain unconstructed. The sole next branch
obligation stays **DC-O1**, now requiring an explicit correlated domain
identity that avoids the proved uniform tensor synchronization while
controlling almost every rectangular pair. This is a constraint on the
same obligation, not a new broad research program. The ultimate target,
ARG, TCRC and RC15/4 stay OPEN; HR-N1 stays DISPROVED.


## 2026-09-21 correlated DC-O1 return-domain cycle

**CORRELATED GO / TAIL FAIL, within the stated scopes.** The
[report](../../notes/2026-09-21-correlated-dc-o1/README.md) tests three
mechanisms with exact whole-scalar composition identities. Separated
factor words have genuine rich encoded returns but sparse Cartesian
coverage. Linear-level certificates have bounded target capacity and
explicit affine-rule costs. These two results do not bound all incidental
returns on the full common scalar square.

For the explicit CRT cube-root carrier, $X=Y$, $n=3^d$ and $|U|=3^d$.
**CD-3 / PROVED:** at least $n^2/48$ ordered pairs have exactly the identity
return for every $d\ge1$, under the full selected width-one exponent box.
Simultaneous residue constraints, a norm bound and an elementary moment
count establish this. Arbitrary integer powers and actual-image lower
bounds are outside its scope. Four exhaustive exact scouts and separate
internal proof reviews are documented in the new report companions.

The cycle remains strictly offline and within its announced budget.
The single branch obligation is still **correlated DC-O1 / OPEN**.
T03's target, ARG, TCRC and RC15/4 remain OPEN; HR-N1 remains DISPROVED.
Historical source files and prior failure scopes are unchanged. No broad
new carrier program, repaired HR-N1 tail or adaptive RC15/4 search is adopted.


## 2026-09-21 subsequent offline return-tail cycle

**RETURN-TAIL FAIL, within three proved real-carrier scopes.** See the
[report](../../notes/2026-09-21-return-tail/README.md) and four complete
proof companions. The structural lemma computes exact return-domain
intersections and zero-corrected moments; its variance criterion is
sufficient and still requires candidate-specific estimates.

**CY-1–CY-3 / PROVED:** a growing cyclotomic trace carrier has $X=Y$,
$n=3p+1$, $6p$ distinct norm-one actions and no identity-only pair.
Every non-sign action nevertheless has the same $6p$-point domain.
Thus $n^2-6p$ sources have exactly two returns. This does not prove
an actual-image lower bound or exclude other action families.

**MG-1–MG-4 / PROVED modular tail, FAILED proposed real lift:** the full
residue alphabet modulo $7^k$ has the exact return/stabilizer histogram
and a polynomial lower tail. Centered representatives fail scalar norm
preservation; retained HR-4A/B rules out a real tail on those integer
inputs. A rational homomorphic lift collapses to at most six actions.

**RT-D1–RT-D3 / PROVED:** on the stated bounded-rational-height sequence
$H=12L$, large coprime source denominators leave only three possible
target least-common-multiple states. At least $n_H^2/400{,}000$ pairs
have subpolynomial full fibers. This proves an all-action tail failure
and, separately, an actual-image lower bound $n_H^{2-\rho}$ for each
fixed $\rho>0$ eventually on that family. It is not a real-set no-go.

Two exact cyclotomic cases verify full domains and distributions; no
failed parameter family was expanded. Work was offline, independently
reviewed internally, and within its announced computational caps.
The single next branch obligation is still **real correlated DC-O1**.
DC-O1, T03, ARG/TCRC and RC15/4 remain OPEN; HR-N1 remains DISPROVED.
No historical source is rewritten and no broader search is adopted.


## 2026-09-30 — 7^k modular-to-real lift

**EXACT LIFT GO / TAIL FAIL**, in the scopes of the
[final report](../../notes/2026-09-30-modular-lift/README.md).
This was a newly authorized strictly offline lift cycle, not a rerun of
the frozen modular tail or of the historical carrier failures.

PROVED: exact carry error; diagonal scalar-lift collapse to at most k+1
values; exact faithful paired lifting of every primitive modular orbit;
and a full-fiber obstruction for its independent-radius same-set
completion. That completion has N=1+t(m/2-1), with N^2-O(N^(3/2))
pairs of selected return count two and complete Q-fiber four. Its actual
image is at least N^2/4-O(N^(3/2)). This lower bound is confined to the
specified completion. The state-cover theorem retains its faithful-action
hypotheses and the modular-unit restriction escape.

Two fixed exact angular-core/orbit checks at k=1,2 yield the full
completed-carrier counts by a proved decomposition, not an unperformed
large-square enumeration. No external sources or novelty claims.
Lead proof checks are recorded; no independent review is claimed.

The single branch obligation is **ML-O1 / OPEN**, a paired lift with
amplitudes in the same cyclotomic field and a proved Cartesian lower tail.
DC-O1, T03, ARG/TCRC and RC15/4 remain OPEN; HR-N1 remains DISPROVED.
The modular route is not universally closed. No broad search or historical
file revision follows from this handoff.


## 2026-09-30 — multiscale / fractal coordinate packing

**SCOPED RETURN-TAIL FAIL; T03 OPEN.** The
[report](../../notes/2026-09-30-multiscale-packing/README.md) proves
that the dyadic cosine-product carrier has at least 4(n-1)^2/9 ordered
pairs with exactly two selected returns, and its one mixed-amplitude
variant has at least (n-1)^2/2 pairs with at most sixteen. Both statements
use all of the selected group mu_(6*2^d), count actual Cartesian targets,
and allow every scalar projection collision. Exact coordinate reuse
does not amplify the required near-full return tail in these models.

The two-obstruction stop rule was met analytically. Independent internal
and lead checks are recorded; no research program was executed. These
are selected-action failures, not lower bounds on actual quadratic images.
ML-O1 is the sole retained next branch obligation. DC-O1, RC15/4,
ARG/TCRC and the fixed T03 target remain OPEN; HR-N1 remains DISPROVED.
Historical sources and prior research checkpoints are unchanged.


## 2026-10-06 — cross-block full-fiber cycle

**TWO CARRIER OBSTRUCTIONS PROVED; T03 OPEN.** The
[report](../../notes/2026-10-06-cross-block-returns/README.md) now proves
actual quadratic image size for both unchanged dyadic packings. Pure
carrier: image≥(n−1)²/9 from exactly4-point full fibers on at least
4(n−1)²/9 sources. Mixed carrier: image≥(n−1)²/96−(n−1)/12 from
full fibers at most48 on at least(n−1)²/2−4(n−1) sources. These
are uniform in depth and cover arbitrary action enlargements.

Explicit mixed-parity swap/Vieta ratios, allowing fractional multipliers, produce
new genuine targets, but cannot overcome the proved small full fibers.
The 30 September selected-action report is preserved; this is a dated
strengthening from new proofs. No lambda limit, carrier mutation or
finite scout was used. Independent internal and lead audits passed.

The sole next bounded obligation is XB-O1, projective spreading within
the prescribed ML-O1 amplitude model, with exact quantifiers in the
report. It is not asserted equivalent to or sufficient for compression.
ML-O1, DC-O1, ARG/TCRC, RC15/4 and the unrestricted T03 target remain
OPEN; HR-N1 remains DISPROVED. No further search is authorized by this
handoff alone.


## 2026-10-06 — XB-O1 to cross-block fiber growth

**SPREADING PROVED; TWO SCOPED FAILURES; T03 OPEN.** The later
[report](../../notes/2026-10-06-fiber-growth/README.md) gives the explicit
amplitudes c_(h,j)=h(1+omega*xi^j), all8q disjoint cosets, actual
q²/2≤n≤48q², and the completed-set spreading bound64sqrt(2)*sqrt(n).
The unique index-two real subfield is identified. Native input factor49
is proved for this new family, not assumed for historical dyadic carriers.

The new FG-F1 proof bounds complete fibers by48²32⁴ on at leastn²/18432
pairs for q≥7392, proving actual imageTheta(n²), independently of any
selected actions. The separate relative-norm rule fails its8q-coset
inventory by exact sevenfold repetition. Both finalists stopped without
repair. Exhaustive k=1,2 data and full independent norm-distribution checks
used1,335,870 evaluations and35.734223 research-program CPU seconds.
Independent internal and lead proof audits passed; historical files are
preserved and no commit was made.

XB-O1 spreading is now proved with the live fixed prefactor (and each
strict smaller exponent in the older asymptotic coefficient-one version).
The cycle's sole unresolved diagnostic lemma FG-O1 classifies exact33-slot
coefficient matchings in the best explicit family. ML-O1, DC-O1, ARG/TCRC,
RC15/4 and the unrestricted fixed quadratic target remain OPEN. HR-N1
remains DISPROVED. No further search or automatic route pivot is authorized.


## 2026-10-06 — cross-block amplification beyond spreading

**TWO SCOPED MECHANISM FAILURES; FULL FIBERS STILL OPEN.** The
[later report](../../notes/2026-10-06-cross-block-amplification/README.md)
proves disjoint 8q-coset inventory and 8q²≤n≤48q² for balanced products
h prod_l(2−xi^(i_l7^l)), with centered base-seven digits. Whole-product
factor switches give exact encoded fibers 6q·2^s and encoded norm image
8·4^r, but these statements cover only the linear-sized encoded pair set.

The new AMP-R1–R3 phase-count and closure theorem proves the specified
independent coordinate-switch certificate has at most four targets for at
least n²/2 sources at r≥8. All scalar representations, sign/swap and every
equal-Q edge within the encoded set are included, with arbitrary iteration.
This is NOT a full-fiber upper bound or an actual-image lower bound.
The quadratic-phase convolution rule separately collapses to eight cosets
and fails ML-O1's required inventory. No former 33-frequency obstruction
is generalized. Both failures were analytic; zero charged evaluations and
zero research-program CPU seconds were used. Internal independent and
lead proof audits passed.

No amplification mechanism survives this cycle. No proxy, rigidity-classification
successor, repaired carrier, or replacement conjecture is adopted. The new
product carrier's actual full-fiber tail remains OPEN. T03, ML-O1, DC-O1,
ARG/TCRC and RC15/4 remain OPEN; HR-N1 remains DISPROVED. Historical
sources are preserved, nothing is committed, and no further search is
commissioned by this status entry.


## 2026-10-11 — balanced-factor full fibers and coupled phases

**COUPLED MECHANISM FAILED IN STATED SCOPE; CARRIER STILL OPEN.** The
[new report](../../notes/2026-10-11-balanced-full-fibers/README.md) retains
all balanced amplitudes. BFF-A1 proves 16q²+1≤n≤24q²−7 after exact scalar
deduplication; BFF-A2 gives an exact full-fiber equality key over Q(xi).

Complete exact r=0,1 squares have (n,image,median fiber)=(17,44,12) and
(1079,286664,4). At r=1 exactly 1135967 of 1164241 pairs have no targets beyond
their own sign/swap orbit. A complete alternative norm oracle agrees on every
output multiplicity. These are EXPERIMENTAL fixed-depth results only.

BFF-P1/P2 close the one phase-transposed mask rule with corrections in μ₆:
even after joining the old certificate and iterating, at most four targets
remain outside fraction 222(4/7)^r+3/(16q²). This is not a FULL-fiber bound.
No positive ε, δ or c is proved, and the carrier is not retired.

The sole new obligation BFF-O1 is an all-target K-equality count in V²,
polynomial in depth on at least 32q⁴ sources in B², for every sufficiently
large depth. Its conditional actual-image lower bound is n²/[18(r+1)^C].
The premise is OPEN. It was not searched after the mechanism's decisive failure.
No new amplitudes, second mechanism, mutation or larger sweep were introduced.

Internal independent and lead proof reviews passed. Total program usage,
including complete validation, 373301 conservative regression charges and
a transparent 17-check correction, was
971843 charged units and 22.997157 CPU seconds. Historical sources are
preserved and nothing is committed. Full image, T03, ML-O1, ARG/TCRC and RC15/4
remain OPEN; the earlier HR-N1 disproof is unchanged.


## 2026-10-11 — BFF-O1 resolved; balanced-factor carrier retired

**PROVED BFF-O1 / ACTUAL CARRIER FAILURE.** The later
[complete report](../../notes/2026-10-11-bff-o1/README.md) proves that,
for some fixed M and every sufficiently large r, at least32q⁴ ordered
B² sources have at most M unrestricted K-equality targets in ALL V².
Thus BFF-O1 holds with C=1 after enlarging the initial depth, and
|Q(A,A)|≥n²/(18M)=Theta(n²). This retires the unchanged balanced-factor
carrier for every fixed positive saving, including unbounded subsequences.

The proof covers all completed targets by49 spaces in the final degree-seven
extension. At least1344 of2401 local source types have rank-four quadratic
maps. A proved finite-family projection/localization lemma bounds full fibers
outside fixed-degree polynomial zero sets; exact circle counts make those
exceptions o(1) of each good parent square. The count retains strictly more
than half of B². All cyclotomic carries, D identifications and lower-rank
target charts are charged. The constants M and the onset depth are not
numerically evaluated. No exact constant-fiber classification is pursued.

Lead and independent internal written proof audits passed. Two approaches
were considered; the 2-adic screen stopped after the decisive tower proof.
No mathematical program ran:0 charged evaluations,0 research-program CPU
seconds; the completed r=0,1 scouts were not rerun. This dated result
supersedes the preceding carrier/full-fiber OPEN status only. Historical
selected-action proofs remain unchanged. T03, RC15/4, ARG/TCRC and other
carriers remain OPEN. No replacement construction or next research cycle
is adopted, and no commit is made.


## 2026-10-20 — C0 mixed-signature lattice symmetry

**PROVED structural results; full-rank return tail OPEN.** The
[new proof package](../../notes/2026-10-20-mixed-signature/README.md)
base changes the accepted C0 tower by the real root of \(s^3+s+1\),
then adjoins \(\omega\). The resulting degrees, signatures, root
discriminants, relative order-unit rank \(d_j\), and integral norm-preserving
matrices are proved in MS-F1–F6.

For the unchanged all-conjugate scalar box at
\(T_0=2\sqrt{D_0\,31^{1/3}}\), MS-C1 gives
\((4\pi)^{d_j}\le n_j\le(4\sqrt{D_0\,31^{1/3}}+1)^{3d_j}\).
Every nonzero order-unit return lies in the exact finite family
\(U_j(T)=\{u:N_{E_j/K_j}u=1,\ \|\ell_j(u)\|_1\le
(d_j/2)\log(48T^6)\}\), with \(u\in\mathcal O_{K_j}[\omega]^\times\).
Relative regulator, order-index, height and window losses are retained.
No positive return or exceptional-pair exponent is proved.

**FAILED IN STATED SCOPE — MS-C3.** All powers of the inherited seed
\(s^2+s\omega\), even multiplied by all order torsion units, give only
\(O((\log n_j)^3)\) distinct targets per pair, uniformly for \(T_j\ge T_0\).
This is an action-certificate obstruction, not a full-fiber theorem.
The new lattice carrier is not retired. BFF-O1's separate retirement
and all frozen totally real sieve scopes are unchanged.

The one recorded next gate is MS-O1: prove or refute exponential population
of the explicit finite \(U_j(T)\) for one fixed \(T\ge T_0\), uniformly
at all sufficiently large levels. This is necessary for a uniform tail,
not sufficient for compression; subsequences require their own quantifiers.
Complete written proofs passed independent internal and lead checks.
Zero mathematical evaluations and zero research-program CPU seconds were
used. No window mutation, historical rerun, network call, affine pivot or
commit occurred. T03 and RC15/4 remain OPEN.


## 2026-10-21 — MS-O1 relative order-unit population proved

**PROVED — MS-O1, MSU-A1–A3.** The
[new report](../../notes/2026-10-21-relative-unit-population/README.md)
proves a uniform exponential bound for the relative order-log covolume,
\(\mathcal R_{R,j}\le K_R^{d_j}\), with an explicit fixed \(K_R\).
For \(T_*=\max\{T_0,\exp(2K_R/3)\}\), the unchanged inventory satisfies
\[
|U_j(T_*)|\ge2^{d_j}
\]
at every tower level. The all-level population gate is resolved with
\(\alpha=\log2\). This supersedes only MS-O1's preceding OPEN status.

Minkowski product disks approximate every relative log direction;
bounded principal-ideal and exact relative-norm element labels give
a finite log-coset cover. Integrating over the torus bounds the relative
covolume. The order index \(27^{d_j}\) is charged once. No totally real
regulator theorem, class-number estimate or short-unit basis is assumed.

**OPEN — useful returns and the actual image.** The counted units have
bounded Weil height but not uniformly small individual conjugates.
MSU-G1–G3 gives weight comparisons and a discrete overlap upper bound
with cell inflation and the exponential density cost retained. The
continuous diagnostic does not prove a discrete return tail.

The sole next lemma MS-O2 asks for an exponential actual return mean
and exponentially small relative variance of the genuine source domains
at this fixed \(T_*\); its precise statement is in the report. It is a
stronger sufficient incidence condition, not a necessary characterization.
No new search is started. Seed-plus-torsion remains closed, BFF-O1's
carrier remains retired, and this lattice carrier, T03 and RC15/4 remain
OPEN. Independent written proof review and lead checks passed. Zero
mathematical evaluations and zero research-program CPU seconds were used.
No historical source, field, seed or carrier was changed; no commit.

## 2026-10-21 — MS-O2 exact windows and inverse-orbit reduction

**OPEN — actual typical-pair returns.** The later authorized
[MS-O2 cycle](../../notes/2026-10-21-typical-unit-returns/README.md)
keeps the MS-O1 field, order, radius, carrier and exhaustive inventory.
MS2-W1–W3 prove the full source-dependent log-and-phase conditions.
The old finite log cover does not by itself count phase-compatible
units in the required translated source windows.

MTR-L1 proves a genuine discrete incidence lower bound. MTR-L2 shows
that combining this bound with the frozen centered-unit count has
optimized certificate rate \(\log(P_* /(2K_R))<0\). This is only an
insufficient lower estimate; the actual mean still has the proved
baseline \(\mu_j\ge2\), and exponential growth remains OPEN.

MSR-I1–I3 identify actual returns with complete order-unit orbit
intersections. If \(\nu_j\) counts the occupied labels
\((zR_j,z\tau z)\), \(z=x-\omega y\ne0\), then exactly
\[
N_j\mathbb E[1/R_j]=\nu_j,\qquad |Q(A_j,A_j)|\le1+\nu_j.
\]
The tested ambient ideal-divisor upper count gives no exponential gain.
Neither failed estimate refutes MS-O2, a weaker return tail, or the
inverse endpoint. No actual-image lower bound follows.

The one next recorded lemma MS-O2-I is the fixed-rate occupied-label
bound \(\nu_j\le C_1N_j e^{-\gamma d_j}\), uniformly for all large \(j\).
It is exactly the permitted inverse endpoint on the same carrier, not
a new construction. The carrier, actual image, T03 and RC15/4 remain
OPEN. Complete new proofs passed independent internal and lead checks;
zero mathematical evaluations and zero research-program CPU seconds.


## 2026-11-05 — archival cross-reference

The [public evidence index](../../EVIDENCE_INDEX.md) and [dated export](../../reports/2026-11-05-evidence-export/README.md) organize the source claims above. The publication pass checked locators, data packaging and archive integrity; it introduced no new proof, experiment or change to this track’s OPEN target.
