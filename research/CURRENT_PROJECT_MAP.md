# Current project map

**Reading map · 7 November 2026.** Start with the [four-track public report](reports/2026-11-05-evidence-export/report.pdf), then the [evidence index](EVIDENCE_INDEX.md) for proof and computation, and the [restart record](OPEN_LEMMAS.md#restart) for the surviving questions. The [academic edition and public derivatives](../docs/WEBSITE_HANDOFF.md) have different purposes. The September map below identifies the migration sources. October checkpoints and the November shared theorem control the later results.

Setup snapshot: **2026-09-14**. Reconciled snapshot: **2026-09-11**, with
**2026-09-10** research cutoff. Source-recovery documents were integrated on
**2026-09-20**; their own mathematical cutoff is still 10 September. All four
fixed targets remain **OPEN**. This map adds navigation; it changes no
mathematical status.

## Controlling sources

Paths below are relative to the Git root. Code-formatted private paths remain
readable in distributed documentation without promising files in a plain clone.

| Area | Read first | Current checkpoint/companions |
|---|---|---|
| Shared | `local-only/migration/sources/00_MASTER_HANDOFF.md` | `local-only/migration/research_supplement/shared/Phase_C0_Corrected.md` and `C0_CORRECTION_LOG.md`; formal proof and frozen Phase A PDFs in that directory |
| T01 | `local-only/migration/sources/T01_CURRENT_STATE.md` | `local-only/migration/sources/T01_Norm_Trace_Quadratic_Research_Checkpoint.md`, §§1–2, 5–8; separate branch |
| T02 | `local-only/migration/sources/T02_CURRENT_STATE.md` | `local-only/migration/sources/T02_C4_REVIEW_ACCEPTANCE_AND_HANDOFF(1).md`; C2–C4 reports and correction/claim/source/rate ledgers under `local-only/migration/research_supplement/T02/` |
| T03 | `local-only/migration/sources/T03_CURRENT_STATE.md` | `local-only/migration/research_supplement/T03/T03_RESEARCH_RECORD_20260910.zip`; identical `output/T03_CURRENT_STATE.md`, later ARDC/DSCR and five TCRC reports in `output/` |
| T04 | `local-only/migration/sources/T04_CURRENT_STATE.md` | `local-only/migration/research_supplement/T04/sacc_candidate_input.md`, `sacc_input_audit.md`, `sacc_pair_states.md` |

No separately named later final checkpoint was recovered for T03/T04; their
designated frozen state files and companions control. MC-03 remains recorded.
An older titled checkpoint cannot replace a later documented frontier.

The eight recovery documents are preserved verbatim under
`local-only/migration/recovery_2026-09-20/`, separated by track and registered
by hash. This intake contains addenda and Markdown manifests only. A manifest's
label `PROVIDED` describes its source package; it does not establish that the
listed original was among these eight received files. See
[the migration conflict register](MIGRATION_CONFLICTS.md) for the resulting
availability boundary. The recovery summaries do not supersede the dated
16 September research records below.

## Targets and missing steps

| Track | Target | Recorded progress and remaining obligation |
|---|---|---|
| [T01](tracks/01-cubic-digital/STATUS.md) | (x-y)³+x+y | No supported cubic candidate; continuous/digital obstructions are scoped. Separate P0=x²+xy+y²+x is OPEN. Proved transfer requires BOTH small homogeneous image and small difference set, eta<c0/2; no witness. State §§12–14; final checkpoint §§1–2, 8. |
| [T02](tracks/02-quartic-hybrid/STATUS.md) | (x+2y)⁴+3x-y | C4 counts N1=4, Nm=22·7^(3m-4) for m>=2 are recorded PROVED; factor 22/49 stabilizes. Full-local-support/full-interval uniform packing fails in scope. Missing concrete subcarrier and branch-dependent all-pairs support with c_eff<2(a-eta). State §§17–18; final C4 handoff. |
| [T03](tracks/03-eisenstein-cartesianization/STATUS.md) | x²+xy+y² | Recorded exact adaptive (n,s): (2,2),(4,5),(8,17),(16,68),(32,269). Missing T03-O4/RC15/4: legal in-field parameters at every sufficiently large actual adaptive level, O(sqrt(n)) exceptions, signed-root image <=(15/4)s+O(n^(3/2)). Asymptotic exponents remain conditional. State §§4, 7, 13–15. |
| [T04](tracks/04-cubic-slices/STATUS.md) | (x-y)³-3(x+y) | A0={0}; A(m+1)=((2+sqrt(3))Am+sqrt(3)/2) union ((2-sqrt(3))Am-sqrt(3)/2). Input entropy log(Lambda)<=a*<=log(phi) recorded PROVED, Lambda^(-1)+Lambda^(-3)+Lambda^(-5)=1. Missing full-output gap below 2a*. Sufficient all-pair encoding needs polynomial prefactor and kappa<Lambda². State §§4.9, 13–15. |

These are preserved obligations, not assignments. T01's benchmark does not
replace T03; the cubic signs differ. Shared C0 is a rank-one quadratic result
with integral/primitivity/transversality hypotheses, not a full-rank or quartic
solution. Norm–trace and solvable extensions remain shared research direction.

## Working map

| Location | Role |
|---|---|
| [PROJECT_HISTORY.md](PROJECT_HISTORY.md), [tracks/](tracks/README.md) | Preserved reconciliation plus older history; SPECs unchanged |
| [MECHANISM_LIBRARY.md](MECHANISM_LIBRARY.md) | Reusable mechanisms with hypotheses and costs |
| [FAILURE_LIBRARY.md](FAILURE_LIBRARY.md) | Scoped failed certificates, families, and inferences |
| [OPEN_LEMMAS.md](OPEN_LEMMAS.md) | Current gates and historical alternatives |
| [MIGRATION_CONFLICTS.md](MIGRATION_CONFLICTS.md) | MC-01–MC-06 and source/supersession records |
| [CODEX_MIGRATION_AUDIT.md](CODEX_MIGRATION_AUDIT.md) | Checkout choice, setup changes, verification and gaps |
| [templates/CONSTRUCTION_LEDGER.md](templates/CONSTRUCTION_LEDGER.md) | Quantitative/provenance template for future constructions |
| `history-sources/`, `prompts/`, `manifest.json` | Original preserved archive; prompts inactive |
| `tracks/registry.json`, older `docs/` overview/roadmap | Dated metadata; not current assignments |
| `experiments/`, `tests/`, `examples/` | Existing finite exact baseline; T01/T04 are not fully implemented |
| `local-only/migration/`, `local-only/runs/`, `scratch/` | Private references, new raw runs, temporary work |

Retain T04 product-tree attribution and depth-30 numeric provenance gaps and
the missing early one-/two-prime proof originals. The recovery documents locate
the T04 tower source already held locally. They report recovery of T03's F25
certificate and arithmetic obstruction, but those original files were not in
this eight-file intake. No external novelty assessment was performed.

## 2026-09-16 addendum — HR-N1 two-prime multiplier branch

**FAILED assertion; PROVED scoped obstruction.** The later
[strictly offline HR-N1 cycle](notes/2026-09-16-hr-n1-offline/README.md)
disproves the specified $7,19$ Cartesian return-tail assertion. For every
$L=10m$, $m\ge2$, at least $|A_L|^2/200$ ordered pairs have exactly one
return under $G_L$, and under all integer-power multipliers $u^rv^s$.
Complete proofs: [HN1-2, §3](notes/2026-09-16-hr-n1-offline/README.md#3-hn1-2--a-dominant-gap-forces-the-identity)
and [HN1-3, §4](notes/2026-09-16-hr-n1-offline/README.md#4-hn1-3--positive-density-and-disproof-of-hr-n1).

This is a separate T03 multiplier branch. The actual image rate of this
$A_L$, T03's original real-set target and RC15/4 remain **OPEN**; the other
track obligations are unchanged. The preceding high-return report's §7
**OPEN, untested** entry is preserved as historical state and superseded for
HR-N1 alone by this later proof. Review was independent and internal, not
external. No experiment or network access occurred in the new cycle.

## 2026-09-16 final freeze — HR-N1 handoff

The [final proof report](notes/2026-09-16-hr-n1-final-freeze/README.md)
consolidates HN1-1–HN1-3, with a self-contained proof, scope audit and
[machine-readable state](notes/2026-09-16-hr-n1-final-freeze/final-state.yaml).
**HR-N1: FAILED / DISPROVED; its specified pair-tail certificate: CLOSED.**
The theorem gives at least $|A_L|^2/200$ identity-only ordered pairs for
every $L=10m$, $m\ge2$, even under all integer powers $u^rv^s$.
The actual image rate, T03 target, ARG, TCRC and RC15/4 remain **OPEN**.
The existing next obligation is still T03-O4; no new research is launched.
This freeze preserves the completed proof and historical source bytes.

## 2026-09-16 addendum — T01 finite three-branch lift

The [three-branch report](notes/2026-09-16-three-branch-lift/README.md)
proves a finite same-set gadget for \((x-y)^3+x+y\):
\(A=\{0,2\}\), \(F_r(x)=x/2+r/3\), and six enlarged inputs with exactly
22 outputs, a one-step factor \(11/2<9\). Exact whole-slice containments
explain the overlap. Literal iteration fails disjointness; no uniform
recursive gap or arithmetic scalar amplification has been proved.
**The T01 asymptotic target remains OPEN.** The report gives scoped
obstructions and complete exact finite data, with source/proof availability
and internal audit limits stated explicitly. The other tracks are unchanged.


## 2026-09-16 later cycle — two-prime character correlation

**LOCAL GO / GLOBAL FAIL, scoped to the audited realization.** The
[new report](notes/2026-09-16-two-prime-character/README.md) defines the
54-element equal-character carrier in $\mathbb F_7\times\mathbb F_{19}$.
TP-L1 proves 8–54 distinct returns on all 2916 pairs, with no identity-only
pairs. TP-P1 proves exact products, $R_d\ge8^d$ without exceptions and
$\#\{R_d<18^d\}\le2772^d$. These are finite-ring statements.

TP-G1 (TP-R1 in its companion) proves that every homomorphic realization
of $G^d\cong(C_6\times C_{18})^d$ by real scalar norm-one multipliers
has at most 18 distinct actions. Duplicate actions consume the return
exponent. The separate normalized CRT contribution is also negative.
This does not prove a real-image lower bound or rule out other actions.
The new one-block diagnostic and independent oracle were exact and offline;
all current-cycle computation plus regressions used 736,357 charged calls
and 3.607404 research CPU seconds. Historical records are preserved.
HR-N1 remains CLOSED; T03, ARG, TCRC and RC15/4 remain OPEN. The sole
retained next obligation is T03-O4, not started during this cycle.

## 2026-09-16 continuation — T01 three-branch composability

The [continuation report](notes/2026-09-16-three-branch-continuation/README.md)
preserves the finite 22-output gadget and proves scoped failures of two
natural repairs. Literal iteration has \(n_m=4\cdot2^m+2\) and
\(s_m=n_m^2-O(n_m^{3/2})\), so its actual rates satisfy
\(\rho=4=\lambda^2\). Sufficiently separated copies expose all six
cross-copy blocks, giving \(6n^2+3s\) outputs before common scaling.
Bounded inventories of the gadget's slice rules supply only \(O(n)\)
identifications; this limits that certificate, not every adaptive carrier.

Nine explicit adaptive rational rules were tested exactly through three
levels, \(6\to18\to54\to162\), with no sustained normalized gain.
The new strict-rate implication correctly accounts for input losses, but
no candidate supplies its hypotheses. **T01 remains OPEN**; no arithmetic
tower or internet research was undertaken. The one retained next obligation
for this branch concerns partial returns under a specified quadratic
output-preserving pair map. Other tracks and all historical records remain
unchanged.


## 2026-09-16 — unit-exponent Cartesian cycle

**ACTION GO / CARTESIAN FAIL, in two stated scopes.** The
[unit-exponent report](notes/2026-09-16-unit-exponent/README.md) supplies
explicit multiplicatively independent fractional norm-one elements in the
fixed field $\mathbb Q(\omega)$. Their boxes contain $3^d$ distinct real
actions. **PROVED UE-P1/P2:** the corresponding $3^d$-point norm orbit
has at least $2^d$ genuine returns everywhere, with an exact product law
and exponential tail. **PROVED UE-P3:** its coefficient carrier has
$2\cdot3^d$ elements, but only $3^d$ engineered pairs; this certificate
has exponentially sparse Cartesian coverage. Its actual full-image rate
remains OPEN.

The one secondary sparse valuation box has **PROVED UE-S1:** only the
identity returns any pair under all integer generator powers. Separately,
**PROVED UE-S2:** its actual full image is $n_d^2/4+n_d/2$, so this
particular family fails power saving. Neither result closes other unit,
valuation or norm-symmetry constructions. The target, ARG, TCRC and RC15/4
remain OPEN; HR-N1 stays closed. T03-O4 remains the sole next obligation.
The cycle was offline, with one exact six-case diagnostic and independent
oracle; code regressions passed. Historical reports were preserved.


## 2026-09-20 documentation freeze - Cartesian norm-symmetry

The [final Markdown checkpoint](notes/2026-09-20-cartesian-norm-freeze/Cartesian_Norm_Symmetry_Research_Checkpoint.md)
and [PDF](../output/pdf/Cartesian_Norm_Symmetry_Research_Checkpoint.pdf) freeze the completed
16 September branch as **ACTION GO / CARTESIAN FAIL**, in its exact scopes.
Actual independent actions and rich orbit returns are proved; direct coefficient
completion has engineered density $1/(4\cdot3^d)$. The primary actual image
and incidental cross-pair returns remain OPEN. The separate valuation family
has identity-only returns and an independently proved image $n^2/4+n/2$.

The carrier search is frozen. Revival requires a genuinely new Cartesianization
principle and separate authorization, not another routine prime, character,
unit-box or denominator mutation. General homogeneous/affine targets remain
OPEN. **T03-O4 / RC15/4 is the one retained next obligation, unchanged and
not attempted here.** This task is offline documentation and PDF production;
no research experiment, proof search or new independent proof audit occurred.


## 2026-09-21 documentation freeze - T01 pair symmetry

The [final report](notes/2026-09-21-three-branch-freeze/Three_Branch_Continuation_Freeze.md)
and [PDF](../output/pdf/Three_Branch_Continuation_Freeze.pdf) consolidate the
16 September three-branch continuation without new research. Finite
$36\to22$ overlap is PROVED; literal iteration has critical rate
$\rho=\lambda^2$ and sufficiently separated copies have quadratic image.
The bounded-rule obstruction retains its certificate-only scope.

The global quadratic pair map satisfies $P\circ T_\tau=P$. Its partial
Cartesian-return quantity $R_1(N)$ is the one frozen next obligation,
not attempted during this task. A positive answer would not by itself
prove the original power saving. **T01 remains OPEN**; the other tracks
are unchanged. The PDF and Markdown preserve chronology, source
availability, exact finite evidence and all failure scopes.


## 2026-09-21 newly authorized dense-Cartesianization cycle

The [new report](notes/2026-09-21-dense-cartesianization/README.md)
records **CARTESIANIZATION FAIL in the proved scopes**, after the user
separately commissioned five new Cartesianization principles. This
supersedes the 20 September no-search disposition only for this cycle;
the earlier checkpoint and proofs remain intact.

New PROVED results: separated-product coverage obstruction; largest-block
complete-transition obstruction; universal single-action overlap at most
$\lfloor(3n^2+1)/4\rfloor$; faithful bounded-digit image fibers at most
$m^4$; one-axis thickening coverage cost; and a precise rectangular
symmetrization implication. Four exact new cases were scouted, without
repeating the old carriers unchanged. No positive carrier survives.

The one next obligation for this commissioned branch is **DC-O1**, the
high-overlap rectangular return witness in report §12. Its same-set
transport is proved; the witness is OPEN. T03-O4/RC15/4 remains a separate
OPEN adaptive obligation, not replaced or attempted. The target, ARG and
TCRC remain OPEN; HR-N1 remains DISPROVED. No affine or difference-set
optimization was started.


## 2026-09-21 new T01 research — vanishing fixed-step returns

The [Cartesian-return report](notes/2026-09-21-cubic-returns/README.md)
proves the uniform bound \(E_\tau(A)\le5|A|^{11/6}\) for every nonzero
real step, with complete internal proof and independent internal checking.
The frozen \(R_1\) obligation is resolved: **PROVED \(R_1(N)\to0\)**.
Almost-all-pair coverage by long fixed-step paths is **FAILED**, and any
\(o(N^{1/6})\)-size inventory still leaves almost every pair isolated.
The best explicit lower bound in this cycle is
\((4\sqrt2/3)N^{-1/2}+O(N^{-1})\), from third-integer intervals.

This is a new authorized offline proof-search cycle, following the freeze,
not a revision to its historical proofs. Exact diagnostics covered 130
prescribed finite candidates. No arithmetic amplification or old-grid rerun
occurred. Graph components may share cubic outputs, so **T01 remains OPEN**.
The single next obligation is **CR-O1**, an explicit growing-step Cartesian
coverage witness; it was not started. Other tracks and the separate T01
quadratic branch are unchanged.


## 2026-09-21 DC-O1 rectangular-witness cycle

The [DC-O1 report](notes/2026-09-21-dc-o1/README.md) records
**RECTANGULAR WITNESS FAIL in the proved scopes**. Four mechanisms were
examined: asymmetric core fringes, local return products, balanced state
words, and correlated polynomial words with moving poles. Six exact
cases were scouted; no positive exponent triple survived.

PROVED: quantitative fringe-return capacity and core-tail transfer;
scalar cross-term synchronization for independent local rotations;
quadratic bad mass in the complementary-state balancing certificate;
and an explicit moving-pole family with $X=Y$, $3^d$ distinct actions,
but at most 27 distinct returns everywhere. The latter is a return
obstruction, not an actual-image lower bound. No new actual-image lower
bound is claimed by this cycle.

**DC-O1 remains OPEN.** Its one retained obligation is the same
high-overlap witness, with jointly correlated partial domains that
preserve scalar cross terms and prove a positive return/tail exponent.
The quadratic target, ARG, TCRC and RC15/4 remain OPEN; HR-N1 remains
DISPROVED. No broad replacement search, affine transfer, difference-set
optimization or adaptive RC15/4 work was started.


## 2026-09-21 correlated DC-O1 cycle

The [correlated report](notes/2026-09-21-correlated-dc-o1/README.md)
records **CORRELATED GO / TAIL FAIL** in three proved scopes. Whole-factor
switching preserves scalar cross terms and has an exponential encoded
return tail, but its separated coefficient completion covers at most a
$4^{-d}$ fraction of the square. Linear-level reflections preserve the
norm, but $k$ target levels yield at most $2k$ certified targets; affine
level libraries have the stated incidence cost. These are certificate
failures, not full-action bad-pair theorems.

The CRT cube-root carrier has $X=Y$, $n=3^d$ and $3^d$ distinct
width-one factor actions. **CD-3 proves at least $n^2/48$ actual
identity-only ordered pairs for every $d\ge1$**, excluding its required
return tail. The proof does not extend to all integer powers or infer an
actual-image lower bound. Four exact scouts are separate supporting data.

The single branch obligation remains **correlated DC-O1 / OPEN**. The
quadratic target, ARG/TCRC and RC15/4 stay OPEN; HR-N1 remains DISPROVED.
No historical family is reopened and no replacement conjecture is adopted.


## 2026-09-21 later T01 research — growing-step graph cycle

The [growing-step report](notes/2026-09-21-growing-step-cubic/README.md)
proves a joint-step edge bound \(9N^2M^{2/3}+NM+12N^2\). It improves
large-inventory edge counts, **not** the frozen \(N^{1/6}\) necessary
coverage exponent. It also proves actual-image obstructions for fixed-spacing
APs, common-lattice carriers with \(D=o(h^3N^2)\), faithful coefficient
boxes, and fixed rational additive completion, with precise scopes.

The 32-carrier/192-case exact diagnostic counted full graphs and full images;
no positive asymptotic witness was obtained. **T01 and CR-O1 remain OPEN**.
CR-O1's sublinear-inventory coverage witness is the one prioritized next
obligation; its original unrestricted-inventory version is not declared
resolved. The false general equality of components and generated-subgroup
coset intersections is corrected by an actual cubic-fiber counterexample.
This was a newly authorized offline cycle, not a rewrite of the prior
fixed-step proof. Other tracks, historical artifacts and arithmetic-amplification
boundaries remain unchanged by this work.


## 2026-09-21 T01 continuation — sublinear inventories and scalar reuse

The [sublinear cubic report](notes/2026-09-21-sublinear-cubic/README.md)
adds internally audited actual-image obstructions for nonfaithful quadratic
projections, critical rational scaling, and specified changing-prime
fine meshes, plus a step-size-sensitive bound for graph vertex coverage.
The new finite grid has 36 model records, 35 distinct carriers and 216
inventories. It supplies no asymptotic witness. **T01 / CR-O1 remain OPEN**;
the universal necessary inventory exponent remains 1/6. Earlier four-track
identities and other tracks are unchanged. See the report's full ledger,
proof companions and separate verification record.


## 2026-09-21 later T03 return-tail cycle

The [return-tail report](notes/2026-09-21-return-tail/README.md)
records **RETURN-TAIL FAIL** in three precise real-carrier scopes.
Identity-only counts of zero or one do not supply a polynomial tail.
For the cyclotomic trace family, $n=3p+1$, $|U|=6p$, and every domain
other than the two signs is exactly the same $6p$-point orbit. Hence
$R=2$ on $n^2-6p$ pairs and $R=6p$ on the remaining $6p$ pairs.
This is a full selected-action theorem, not a full-image lower bound.

The full residue alphabet modulo $7^k$ has a proved modular tail with
explicit stabilizers and no nonzero identity-only state; its canonical
integer lift fails exact scalar norm preservation and the retained
integer-fiber bound rules out its real tail. The rational-height family
$A_H=\{a/b:|a|,b\le H,\ b>0,\ \gcd(a,b)=1\}$, along $H=12L$,
has at least $n_H^2/400{,}000$ low-return pairs under any action family.
A separate full-fiber proof gives its actual-image lower bound
$n_H^{2-\rho}$ for every fixed $\rho>0$, eventually on that sequence.

The structural geometry note supplies exact domain intersections and
a sufficient variance criterion. Two exact cyclotomic cases are finite
checks, not the source of the uniform theorems. The single next branch
obligation remains the **real correlated DC-O1 return-tail witness**.
DC-O1, T03, ARG/TCRC and RC15/4 stay OPEN; HR-N1 stays DISPROVED.


## 2026-09-21 T01 nonlinear coordinate-reuse cycle

The [nonlinear-reuse report](notes/2026-09-21-nonlinear-reuse/README.md)
adds internally audited fixed-output rational-curve classifications,
a degree-two output-statistic classification with at most 2N distinct
pairs per chart, and an independent scalar/output rational-grid
obstruction. Genuine exceptional nonlinear cubic matching exists, but
the proved two-output family has only linear prescribed pair coverage.
The 16-chart exact grid accounts for the full Cartesian complement.
No positive full-support exponent is obtained: **T01 remains OPEN**.

For this direction, **NR-O1** supersedes CR-O1 as the adopted next
priority, not as a resolution: construct a near-complete direct pair
chart with subquadratic selected support and fully charged scalar,
multiplicity and complement counts. CR-O1 remains an OPEN graph subcase;
no small symmetry inventory is imposed here. The source hierarchy,
other tracks and arithmetic-amplification boundary are unchanged.


## 2026-09-30 T03 modular-to-real lift cycle

The [modular-lift report](notes/2026-09-30-modular-lift/README.md)
records **EXACT LIFT GO / TAIL FAIL**. The explicit paired encoding
realizes every primitive 7^k modular orbit with all its distinct rotations
in characteristic zero. Its independently tagged Cartesian completion has
N=Theta(7^(2k)), but N^2-O(N^(3/2)) cross-shell pairs have exactly two
selected returns and full Q-fiber size four. This separately proves an
actual-image obstruction for that completion, not for all modular lifts.

A scalar map preserving even all diagonal returns of the modular
order-three action has image at most k+1. Exact carry equations,
a scoped state-cover lower bound, and the modular-unit restriction
are also recorded. Two fixed exact core checks support the proved
full-carrier decomposition. No external input or broad search occurred.

The one new branch obligation is **ML-O1 / OPEN**: use amplitudes in
the same cyclotomic field to obtain a coordinate-reusing paired lift
with the required full Cartesian return tail. This refines the authorized
modular-lift route; DC-O1, T03, ARG/TCRC and RC15/4 remain OPEN.
HR-N1 remains DISPROVED. Historical sources are unchanged.


## 2026-09-30 T01 near-complete nonlinear charts

The [near-complete-chart report](notes/2026-09-30-near-complete-charts/README.md)
adds internally audited invariant-orbit obstructions for arbitrary growing
polynomial pair-map libraries, a selected-support lower bound under explicit
chart-output overlap hypotheses, and an exact equivalence with the actual
small-fiber pair-mass tail. Six new all-pair completion scouts fail their
finite coverage gates; they were stopped before recursive expansion.
**T01 remains OPEN.** Certificate obstructions are not actual-image theorems.

The sole next obligation is **NC-O1**, the actual cubic fiber-tail witness,
proved equivalent to unresolved NR-O1. CR-O1 remains an OPEN graph subcase.
No small symmetry inventory is required. All other tracks, historical sources
and prior reports are unchanged.


## 2026-09-30 T01 elliptic geometry addendum

The later commissioned [elliptic-geometry report](notes/2026-09-30-elliptic-geometry/README.md)
keeps T01 OPEN. PROVED within its displayed hypotheses: global separated
polynomial factorization through elliptic addition/difference is impossible;
a same-map finite-grid rule of degrees d,h covers at most d(4d+h)N actual
scalar pairs. The report also gives degree-free injective sum and
small-difference-set obstructions, complete sharing-curve genus calculations,
and exact complex/real descent formulas. These are architecture-specific
obstructions, not a universal image lower bound. Eight new exact finite scouts
used 1,444 P evaluations; two prescribed elliptic fibers remain sparse.
EG-O1 is the existing NC-O1 fiber-tail witness expressed as an elliptic-sharing
network. Earlier rational/chart results and the fixed target remain unchanged.


## 2026-09-30 T03 multiscale coordinate packing

The [bounded offline report](notes/2026-09-30-multiscale-packing/README.md)
freezes two scoped selected-action obstructions. Dyadic cosine products
have at least 4(n-1)^2/9 ordered pairs with exactly two genuine returns;
the one mixed-amplitude variant has at least (n-1)^2/2 pairs with at most
sixteen, under the complete selected group mu_(6*2^d). Exact coordinate
reuse survives, but neither carrier supplies a positive fixed return tail.
These are internally audited proofs, not actual-image lower bounds.
No research program was needed (zero charged evaluations/CPU seconds).
The sole next branch obligation ML-O1 is retained; DC-O1, T03, RC15/4
and ARG/TCRC remain OPEN, and HR-N1 remains DISPROVED.


## 2026-10-06 T01 compatibility of three sharing curves

The [sharing-compatibility report](notes/2026-10-06-sharing-compatibility/README.md)
studies one directed triangle with ordered outputs (z,z+2r,z+4r), r=1/sqrt(3).
PROVED: an ordered real output triple has at most one triangle; this fixed-gap
family consists exactly of translates of (−r,0,r). Every nonempty finite translated
assembly has Z=N and Q≤2N−3, sharply, so its prescribed-pair mechanism remains
linear. The consecutive strip attains the bound and has actual image
N²−O(N^(3/2)), by the inherited GS-A4 progression theorem checked at this
spacing. Eight exact strips were enumerated only after compatibility was
derived. T01 remains OPEN; earlier elliptic results are preserved. SH-O1 is
a scoped full-image question for arbitrary translations, not an equivalent
reformulation of T01 or a claimed constructive reduction.


## 2026-10-06 T03 cross-block full-fiber cycle

The [cross-block report](notes/2026-10-06-cross-block-returns/README.md)
adds new full-fiber proofs to the unchanged two dyadic carriers. The pure
carrier has at least4(n−1)²/9 pairs with full fiber4, giving actual image
at least(n−1)²/9. The mixed carrier has at least(n−1)²/2−4(n−1) pairs
with full fiber at most48, giving actual image at least
(n−1)²/96−(n−1)/12. Both images are therefore Theta(n²); action
enlargement cannot rescue either carrier. Explicit mixed-parity swap and
Vieta multipliers do supply additional targets, but no growing tail.

This is a new proof strengthening the earlier selected-action checkpoint,
whose bytes and claims are retained. No input-growth limit is assumed.
Independent internal and lead audits passed; no mathematical program ran.
The sole next bounded obligation XB-O1 is an explicit projective-spreading
gate within ML-O1, stated in the report; it is not a claimed sufficient
or universally necessary condition for compression. T03, ML-O1, DC-O1,
ARG/TCRC and RC15/4 remain OPEN. HR-N1 remains DISPROVED.


## 2026-10-06 T01 variable-gap sharing cycle

The [variable-gap report](notes/2026-10-06-variable-gap-sharing/README.md)
constructs one output-first shared-edge network with N=k³,
Q=2k⁴−k²−k, Z=2k³−k. All actual edges have growing partner degree,
and both partner cross-edges remain controlled locally. Endpoint and
selected-output reuse grow, but coverage tends to zero. This equals,
rather than improves, the prior GS-P3 N^(4/3) selected-pair rate.

The reconstructed carrier is an integer interval; imported GS-A4,
independently specialized, gives actual image N²−O(N^(3/2)). Thus the
family is closed as a power-saving candidate. VG-G2 newly verifies real
ordered-output uniqueness for every directed cycle, including even cycles.
Three exact full-square instances followed proof and code review.

T01 remains OPEN. The sole next obligation VG-O1 is a finite nonarithmetic
real embedding of the same 27-vertex/150-edge/51-output incidence pattern,
with output values allowed to vary; a rigidity proof is the alternative.
It is not a claimed asymptotic reduction, and no deformation search ran.
Earlier elliptic and fixed-gap reports remain unchanged.


## 2026-10-06 T03 XB-O1 spreading and full-fiber cycle

The later [fiber-growth report](notes/2026-10-06-fiber-growth/README.md)
constructs c_(h,j)=h(1+omega*xi^j), h=1,...,8, j mod q, q=7^(k−1),
with all 8q amplitude cosets disjoint and actual completed size n=Theta(q²).
PROVED: its unique index-two real subfield is F=Q(xi+xi^-1), and every
F-line contains at most64sqrt(2)*n^(1/2) nonzero scalars. The current
fixed-prefactor XB-O1 screen passes; the older coefficient-one asymptotic
screen follows for each strict kappa<1/2 eventually.

PROVED separately: at least n²/18432 pairs have full fibers at most
48²*32⁴ for q≥7392, so this new carrier's actual image is Theta(n²).
Spreading does not supply growing generic fibers here. A second relative-norm
rule has at most8q/7 cosets and fails the prescribed inventory. Neither
failed rule was repaired. Exact k=1,2 scouts and full independent distribution
validation used1,335,870 charged evaluations and35.734223 CPU seconds.
The one remaining diagnostic lemma FG-O1 classifies exact33-slot target
matches for generic X,X sources. T03, ML-O1, DC-O1, ARG/TCRC and RC15/4
remain OPEN; HR-N1 remains DISPROVED. Earlier checkpoints are preserved.


## 2026-10-06 T03 cross-block amplification beyond spreading

The later [amplification report](notes/2026-10-06-cross-block-amplification/README.md)
introduces two rules without reopening either frozen FG family or FG-O1.
Balanced products c_(h,i)=h prod_l(2−xi^(i_l7^l)), with digits −3 through 3,
have exactly 8q disjoint cosets and actual 8q²≤n≤48q². Their encoded norm
classes number 8·4^r and encoded fibers are 6q·2^s for s nonzero digits.

PROVED scoped certificate obstruction: all independent coordinate factor
switches, all scalar representations, sign/swap, all equal-Q edges within
the encoded set, and their finite iterations give at most four targets
outside at most 1536q³4^r+48q² pairs. Thus at least n²/2 sources have
bounded certified returns for r≥8. Full fibers and actual image remain OPEN.
The quadratic-phase sum rule has exactly eight amplitude cosets instead
of 8q and fails its required inventory. These are mechanism/inventory
failures, not new full-image lower bounds. No research program ran.

No amplification mechanism survives and no replacement proxy or rigidity
lemma is adopted. T03, ML-O1, DC-O1, ARG/TCRC and RC15/4 remain OPEN;
HR-N1 remains DISPROVED. Earlier proof scopes and sources are preserved.


## 2026-10-06 T01 changed-collision pattern cycle

The [new report](notes/2026-10-06-changed-collision-pattern/README.md)
resolves VG-O1 by rigidity (CP-R1): its increasing real realizations satisfy
x_i=i, even without distinct output values. The user-supplied outline was
checked directly against the saved equations; no separate progress file
was located. Earlier VG artifacts remain unchanged.

A changed conic pattern gives a six-scalar non-AP bridge with Q=8,Z=3,
including a four-pair fiber across two different centers. Its fixed-width
ladder has N=2m+2,Q=4m,Z=m+1 and bounded selected fibers. A half-size AP
has irrational squared spacing and an injective square, so the actual
image is at leastN²/4. The ladder stops; it does not improve GS-P3's
N^(4/3) selected-pair benchmark. T01 remains OPEN.

The sole next lemma CP-O1 is a finite variable-width third-frame attachment
to that exact six-point seed: reuse at least two scalars and add a third
first coordinate to the zero output fiber. No such attachment or asymptotic
extension is asserted or searched. Only three small complete squares are
assigned to finite audit; no old carrier sweep or arithmetic tower is used.


## 2026-10-11 T01 torsion compatible sharing

The later [torsion-compatibility report](notes/2026-10-11-torsion-compatible-sharing/README.md) derives the actual CP
paired-row locus on the plus-linear sharing curve. It has at most four
admissible real points at fixed outputs. A general second-column
completion requires a connected genus-four double cover; its pullback
under a degree-e isogeny has genus 1+3e. These are scoped correspondence
obstructions, not a renewed global factorization search.

A uniquely forced different-width attachment has six scalars, eight
controlled pairs and two outputs. Its exact full image is 30, with 28
singletons and two fibers of size 4. No third fixed-output width exists.
The two preselected cases have no admissible division or translation
matches at orders 2,3,4. Higher orders are not classified; T01 is OPEN.

The separate same-date B-CP result closing the original CP-O1 is imported
and its five certificates independently checked. This supersedes the older
CP-O1 OPEN pointer above in its finite scope. The sole new diagnostic
TC-O1 asks whether one specified inter-frame point difference is torsion
at any order, without asserting an asymptotic consequence.


## 2026-10-11 T01 marked shift all-orders resolution

**PROVED — MS-C1; TC-O1 resolved:** the exact positive-Y marked
difference T=R2−R1 in TC-G5 has infinite order. The
[all-orders certificate](notes/2026-10-11-marked-shift-certificate/README.md)
proves the degree-eight joint coordinate field, uses a good 23-adic
embedding with v23(X(4R2))=−2, and applies the supplied formal-logarithm
lemma with its proof and hypotheses checked. A field conjugation gives
T+sigma(T)=2R2. Lead, arithmetic specialist and independent referee
checked the argument; no division-order search was run.

This dated resolution supersedes only the preceding TC-O1 OPEN pointer.
It concerns one finite attachment; the accepted two-width and genus-four
bounds are unchanged, and T01 remains OPEN. No successor research
obligation is commissioned by this cleanup.


## 2026-10-11 T01 torsion/frame documentation freeze

The [frozen report package](notes/2026-10-11-torsion-frame-freeze/README.md)
provides a main PDF, technical appendix, one-page meeting summary and
editable Markdown with a source/status ledger. MS-C1 remains PROVED in
the supplied source system, TC-O1 resolved, and the fixed cubic target
OPEN. This offline documentation pass preserves prior proof/data bytes
and does not launch research or claim another independent proof audit.


## 2026-10-11 T01 varying-output frame junction

The later [varying-output report](notes/2026-10-11-varying-output-frames/README.md)
proves an exact output-first three-label junction. Its closing long-edge
frame adds two new cross-block pairs and no scalar: N=8,Q=10,Z=3.
The chosen continuation has N=4m,Q=6m−2,Z=m+1 and an injective
(N/4)-square, so its actual image is at least N²/16. Even all complete
frames inside that scalar pool control only O(N) pairs. This family is
stopped and does not improve the prior N^(4/3) prescribed-pair benchmark.

Keeping the same two outside-row identifications forces equal adjacent
output gaps; this is a scoped role obstruction, not a universal statement
about varying-output networks. Three predeclared exact finite audits give
full images 53,122,223 for N=8,12,16. VO-O1 is the one untested next
finite compatibility question: change the lower long row to an old column,
retain unequal gaps, and close its columns inside the old scalar pool.
T01 remains OPEN; MS-C1 and the frozen torsion/frame results are unchanged.


## 2026-10-11 T03 balanced-factor full fibers and coupled phases

The [fixed-carrier report](notes/2026-10-11-balanced-full-fibers/README.md)
proves the exact scalar decomposition A=X(B disjoint-union(-B) disjoint-unionD),
n=16q²+|D|, and 16q²+1≤n≤24q²−7. Complete exact full-square audits at
r=0,1 give (n,image,median fiber)=(17,44,12),(1079,286664,4); a second complete
complex-norm calculation agrees on every output multiplicity. These are finite
EXPERIMENTAL results, not an asymptotic obstruction.

The one new phase-transposed switch certificate, with corrections in mu6,
has at most four targets outside a fraction 222(4/7)^r+3/(16q²), even after
adjoining the frozen moves and arbitrary iteration. This closes that mechanism
only. The balanced carrier's actual full-fiber asymptotics and image remain OPEN.
BFF-O1 is the sole recorded next obligation: bound all exact K-equality targets
in V² by a polynomial in depth on at least 32q⁴ sources in B², uniformly for every
sufficiently large depth. Its n^{2−o(1)} image consequence is proved conditionally;
the premise is unproved. No other carrier or mechanism was searched.

The cycle used 971843 charged units and 22.997157 program CPU seconds,
including complete validation, 373301 conservative regression charges, and
an explicit 17-check accounting correction.
Lead and independent internal proof audits passed. T03 and RC15/4 remain OPEN;
historical sources are preserved and no commit was made.


## 2026-10-11 T01 VO-O1 proof verification and freeze

**PROVED - VO-C6; VO-O1 resolved negatively:** the exact mixed-role
junction in the preceding varying-output checkpoint has no positive real
solution. The [freeze note and readable PDF](notes/2026-10-11-vo-o1-freeze/README.md)
verify the supplied elementary contradiction with an independent referee.
The signed roles imply an inconsistent necessary subsystem: H<1/2<h
and H>h. All cancelled factors and comparison signs are checked.

This supersedes only the prior VO-O1 OPEN pointer, whose original text
remains historical. The earlier continuation counts and N²/16 actual-image
bound are separate imported results. T01 and other role patterns remain
OPEN. No enumeration, metric-entropy programme or successor research cycle
is authorized or begun. The proof supplied inline was checked; no separate
proof-note attachment was located or claimed read.


## 2026-10-11 T03 BFF-O1 carrier-retirement theorem

**BFF-O1 PROVED; balanced-factor carrier RETIRED.** The later
[report and complete proofs](notes/2026-10-11-bff-o1/README.md) establish
a fixed full-fiber bound M on at least32q⁴ ordered B² sources at every
sufficiently large depth. All V² targets are included. Hence actual image
size is at least n²/(18M)=Theta(n²); the requested polynomial-depth form
holds with C=1 eventually. This supersedes only this carrier's earlier
full-fiber OPEN entries, preserved above.

The proof uses the last degree-seven layer,1344 rank-four source types
out of2401, a uniform algebraic finite-fiber lemma, and polynomial-zero-set
counts on the predecessor carrier. Independent internal and lead checks
passed. No new mathematical computation or historical scout rerun was
needed. The unrestricted Q target and separate RC15/4 remain OPEN.
The carrier is retired without adopting another amplitude rule or obligation.


## 2026-10-20 T01 tetrahedral mixed-role catalogue

**PROVED — TJ-C1–C4:** the
[four-case tetrahedral test](notes/2026-10-20-tetrahedral-junction/README.md)
has no admissible real seed. The registered scope is symmetric gaps
(a,b,a), paired opposite-edge sharing, matching reflected width branches,
and either of two specified closing-role patterns. Exact inequalities
exclude all branches; no parameter enumeration or growth attachment follows.
This does not classify arbitrary tetrahedra or reopen the frozen VO-O1,
fixed-output or torsion results.

The independent internal referee accepts the proofs. There are no actual
N,Q,Z,B values or full-square histogram for an infeasible seed. The target
and one precisely specified column-role modification TJ-O1 remain OPEN;
the modification was not tested. Historical files remain unchanged.


## 2026-10-20 T03 mixed-signature arithmetic lattice carrier

**PROVED field/carrier structure; OPEN full-rank return tail.** The
[C0 base-change report](notes/2026-10-20-mixed-signature/README.md)
uses \(K_j=F_j(s)\), \(E_j=K_j(\omega)\), \(s^3+s+1=0\), and the complete
all-conjugate scalar box. It proves bounded root discriminant, relative
order-unit rank \(d_j\), exponential actual scalar growth and a finite
height window containing every nonzero order-unit return.

The seed \(s^2+s\omega\), with all integer powers and all order torsion,
has only \(O((\log n_j)^3)\) returns per pair. That certificate fails;
the full-rank group and actual image of this carrier remain OPEN.
The sole next gate MS-O1 asks for exponentially many actual order units
inside the explicit return-height window at one fixed radius. It is
necessary, not sufficient, for a uniform eventual tail.

The report includes exact nonreal overlap losses and regulator/order/height
costs. No correlated-window change or affine optimization was made.
BFF-O1's carrier retirement, the closed totally real norm-sieve
certificates, and the OPEN status of T03 and RC15/4 are preserved.


## 2026-10-21 T01 TJ-O1 proof verification and freeze

**PROVED — TJ-C6; TJ-O1 PROVED IMPOSSIBLE.** The
[new proof note](notes/2026-10-21-tj-o1-freeze/README.md) verifies the
supplied contradiction for the exact epsilon=-1 modified column closure
H=r,S=e+q. Its equations force the equal quantities q+g(p) and S+g(w)
to be respectively less than and greater than1. The crucial p>1/2
branch inference is proved explicitly, with no branch discarded.

The lead, algebraic referee and separate proof-checker accept the proof.
Earlier TJ-O1 OPEN text is preserved and superseded only in this scope.
T01 and other role patterns remain OPEN; no next search was adopted.


## 2026-10-21 T03 MS-O1 relative-unit population

**PROVED — MS-O1.** The
[relative-unit report](notes/2026-10-21-relative-unit-population/README.md)
keeps the 20 October mixed-signature fields, order and scalar carrier.
A direct Minkowski/ideal-and-norm covering argument gives
\(\mathcal R_{R,j}\le K_R^{d_j}\). One explicit fixed \(T_*\) therefore
has \(|U_j(T_*)|\ge2^{d_j}\) at every level. The order cost is included
once; no totally real regulator theorem is transplanted.

The associated distortion audit retains unknown log-shape distribution,
proves a discrete upper comparison with cell inflation, and does not
infer a lower return tail from continuous weights. MS-O1's earlier OPEN
entry is superseded; the full-rank return tail and actual image remain
OPEN. MS-O2 is the one precisely stated sufficient actual-incidence
concentration obligation at \(T_*\), not a newly launched research cycle.

The seed certificate and balanced-factor retirement are unchanged.
T03 and separate RC15/4 remain OPEN. Symbolic proofs received independent
internal and lead checks; no mathematical program, network access,
carrier mutation or commit occurred.

## 2026-10-21 later T03 checkpoint — MS-O2 remains OPEN

The [typical-unit-return report](notes/2026-10-21-typical-unit-returns/README.md)
retains the entire MS-O1 construction and fixed radius. It proves exact
source log/phase windows, a fully charged discrete lower incidence
bound, and exact orbit accounting. Neither the lower incidence
certificate nor the ambient ideal-label upper certificate supplies a
positive return exponent. Their failure does not refute actual returns.

The reciprocal-return sum equals the number \(\nu_j\) of occupied
principal-order-ideal/exact-norm labels, and the whole image is at most
\(1+\nu_j\). The one next recorded lemma MS-O2-I asks for
\(\nu_j\le C_1(n_j^2-1)e^{-\gamma d_j}\) with fixed \(\gamma>0\)
at all sufficiently large levels. This is the allowed inverse endpoint,
still OPEN; no follow-on cycle is started. MS-O1 remains PROVED;
the carrier, T03 and RC15/4 remain OPEN. Retired families stay retired.


## 2026-10-21 — T01 actual cubic fibers across scales

[Multiscale checkpoint](notes/2026-10-21-multiscale-collisions/README.md):
**PROVED** eight-child fiber geometry, actual-pair branching necessity and
localized cluster-mass/output-overlap transfer. **EXPERIMENTAL** six exact
diagnostic squares, with independent full-output agreement. **MISSING SOURCE**
for the requested Raz–Zahl theorem; no expansion exponent imported.
**OPEN** MC-O1 is one fixed two-map collision-rectangle question. This adds
no successful carrier or full-image upper bound; T01 and the frozen
scope of TJ-C6 are unchanged. Full proof, source and audit records accompany
the report. No next experiment was run.
