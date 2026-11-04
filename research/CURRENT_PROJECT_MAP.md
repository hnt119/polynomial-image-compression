# Current Project Map — T03 publication extracts

5 November 2026. Selected original T03 sections, in source order. Other tracks are maintained separately. See the [dated evidence register](exports/2026-11-05-evidence/README.md) for the current theorem scopes.

The latest explicit proof or correction governs its own claim. Current-state exports and the master handoff provide older context. The four OPEN fixed targets are T01 $(x-y)^3+x+y$, T02 $(x+2y)^4+3x-y$, T03 $x^2+xy+y^2$, and T04 $(x-y)^3-3(x+y)$. The shared C0 theorem and the separately proposed affine transfer solve none of these targets.

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


