# Open-lemma registry

## Restart

**7 November 2026.**

The following are the last recorded questions for the four fixed targets and their active branches, through 5 November. The dated registry underneath retains earlier alternatives and supersessions. Use the [evidence index](EVIDENCE_INDEX.md) to distinguish a located argument from a reported result.

| Direction | Question to resume and facts already available | Boundaries and source files |
|---|---|---|
| T01, plus-sign cubic | MC-O1: for the two maps $P(\rho u,\rho v)$ and $P(1+\rho u,\rho v)$ on the same $D^2$, $\rho=1/64$, does the ordered collision-rectangle count $Q_4(D)\le C\vert D\vert ^3$ hold for all finite $D\subset[0,7]$? [Exact definition, §6](notes/2026-10-21-multiscale-collisions/README.md) and [MC-S1–S3 proof](notes/2026-10-21-multiscale-collisions/specialist.md). | This diagnostic follows the necessary branching theorem. No positive cubic construction follows. The specified [modified junction](notes/2026-10-21-tj-o1-freeze/README.md) is impossible. The [digital theorem](proofs/source-recovery/T01-state-digital-theorems.md) remains source-reported proved; its standalone proof and bundle are missing. The optional Raz–Zahl/energy-dispersion input is unavailable. |
| Separate affine quadratic $P_0$ | Find a growing $C$ with $\vert Q(C,C)\vert \le K\vert C\vert ^{2-c_0}$ and $\vert C-C\vert \le D\vert C\vert ^{1+\eta}$ for fixed $0<c_0\le1$, $0\le\eta<c_0/2$. [Norm–trace checkpoint, §2.3](proofs/norm-context/norm-transfer.md) proves the consequent same-set transfer. | The tested shifted product example gives only a constant-factor saving. The witness is missing. [Track record](tracks/01-cubic-digital/STATUS.md) |
| T02, quartic | T02-O1: in the $Q=1$ critical carrier choose a subcarrier of lower input rate $a-\eta>0$ and bound the realized branch support at a rate strictly below $2(a-\eta)$. The [exact width/ideal-sum inequality below](#t02--fixed-quartic-realized-support) charges thinning twice. | C4 counts $4$ outputs at depth one and $22\cdot7^{3m-4}$ at $m\ge2$ for the full critical input. Full-interval uniform packing fails under its specified hypotheses. [C4 proof, §§1–6](proofs/quartic/phase_c4/Phase_C4_Higher_Ramified_Precision.md) · [accepted correction chain](proofs/quartic/T02_C4_REVIEW_ACCEPTANCE_AND_HANDOFF.md). Complete earlier C1/recovery materials are unavailable. |
| T03, adaptive radicals | RC15/4: on every sufficiently large **actual** level, choose the legal $C_m^\dagger$ and one square class covering all but $H\sqrt{n_m}$ inputs and show $\vert \gamma_m Q(U_m,U_m)\vert \le(15/4)s_m+Hn_m^{3/2}$ for fixed $H$. [Precise hypotheses and recurrence, §7](proofs/adaptive-root/state-sections-2-to-7.md). | Exact small levels reach $(n,s)=(32,269)$. The positive-density identity-only obstruction closes [HR-N1](notes/2026-09-16-hr-n1-final-freeze/README.md) for its action. RC15/4 remains open. The missing standalone field-of-25 certificate concerns different evidence. |
| T03, mixed signature | MS-O2-I: at the fixed radius, seek $\nu_j\le C(n_j^2-1)e^{-\gamma d_j}$ for fixed $\gamma>0$ eventually. Here $\nu_j$ counts occupied (principal order ideal, exact norm) labels of nonzero pairs. The full image is at most $1+\nu_j$. [Unit supply](notes/2026-10-21-relative-unit-population/arithmetic.md) · [incidence proof](notes/2026-10-21-typical-unit-returns/incidences.md). | The inventory has at least $2^{d_j}$ units. The ambient label count and mean-overlap arguments supply no adequate bound on the occupied labels. Multiple labels may yield one output. [Current gate](notes/2026-10-21-typical-unit-returns/README.md). Separately, [BFF-O1](notes/2026-10-11-bff-o1/README.md) proves actual quadratic-order image on the retired balanced-factor family. |
| T04, minus-sign cubic | T04-O1: for the fixed complementary-unit recursion $A_m$, show $\limsup_m m^{-1}\log\vert P_-(A_m,A_m)\vert <2a_*$, where $a_*=\lim_m m^{-1}\log\vert A_m\vert $. The distinct-input bounds and four pair transitions are in the [status, “PROVED input theorem” and “PROVED exact pair evolution”](tracks/04-cubic-slices/STATUS.md). | Path counts and ten observable coordinates do not count scalar outputs. The two specified narrow-window transfers fail. [Transfer and rich-fiber proofs](exports/2026-11-05-report-references/README.md#ref17). The original SACC input/pair notes are held locally. The depth-30 execution certificate and product-tree attribution are missing. |

The [availability register](MIGRATION_CONFLICTS.md) also identifies the partial recovery packages. Consult [public proof sources](proofs/README.md) for subsequently recovered originals. The 39-file archive, September state exports and frozen specifications describe earlier points in this chronology.

Reconciled **11 September 2026** from the final records. These are recorded
obligations, not assignments executed by this migration. All four fixed targets
remain **OPEN**, with fixed polynomial, fixed positive exponent, arbitrarily
large finite real sets, and the same set in both input coordinates.

Source identities: [MIGRATION_CONFLICTS.md](MIGRATION_CONFLICTS.md#source-registry).
A **CONDITIONAL** exponent below depends on an unproved premise; it is not a
proved construction. Historical alternatives are retained without reopening them.

## T01 — cubic / digital carry

**OPEN — T01-O1:** the target $(x-y)^3+x+y$. No supported narrower surviving
cubic construction lemma is available. The block hypothesis and regular
all-output automaton criterion are **FAILED** in their specified models, not
remaining open obligations. See [T01 STATUS](tracks/01-cubic-digital/STATUS.md).

**OPEN, separate quadratic branch — T01-O3:** $P_0=x^2+xy+y^2+x$.
The completed norm–trace checkpoint proves a sufficient transfer from growing
homogeneous witnesses $C$ with fixed constants satisfying

$$|q(C,C)|\le K_*|C|^{2-c_0},\qquad
|C-C|\le D_*|C|^{1+\eta},\qquad
q=x^2+xy+y^2,\quad0<c_0\le1,\quad0\le\eta<c_0/2.$$

**CONDITIONAL:** the resulting exponent before constant absorption is
$(c_0-2\eta)/(1-\eta)>0$. No such explicit witness is supplied. The source
records supervisor selection of a concrete positive direction as pending;
there is no adopted amplification conjecture or automatic next proof search.

**OPEN; HISTORICAL / SUPERSEDED as a recommendation — T01-O2:** sparse base-6
renormalization. For $N=6^n$, $D\subset[0,N)\cap\mathbb Z$, $M_0=|D|$,
and $|Z_N(D,D)|\le M_0^{2-c}$, the old proposed lemma seeks
$q=2^u3^v\mid N$, a residue $r$, $E=D\cap(r+q\mathbb Z)$,
$E'=(E-r)/q$, $N'=N/q$, with

$$|E|\ge M_0^{1-c/8},\quad N'\le M_0^{16/c},\quad
|Z_{N'}(E',E')|\le|E'|^{2-c/2}.$$

This would be another obstruction, not a positive construction. It was
expressly deprioritized. Source: T01 current state §§7, 13–14.

## T02 — fixed quartic realized support

**OPEN — T02-O1, the single recorded next obligation:** in the established
$Q=1$ critical-coset carrier $C_j$, with input lower rate
$a=\log X-\frac13\log7-\frac12\log D$, define an explicit
$C'_j\subseteq C_j$ and fixed $0\le\eta<a$ with

$$|C'_j|\ge e^{(a-\eta)d_j-o(d_j)}.$$

Construct an all-pairs cover whose branch $\beta$ lies in the ideal coset
$r_{j,\beta}+J_{j,\beta}$ and has proved real coordinate widths
$w_{j,\beta,i}$, correlated with the actual branch. Require

$$\sum_\beta\prod_{i=1}^{d_j}
\left(1+\frac{w_{j,\beta,i}}{N(J_{j,\beta})^{1/d_j}}\right)
\le e^{[2(a-\eta)-\varepsilon]d_j+o(d_j)},\qquad\varepsilon>0.$$

Every branch, box, pair, exceptional output, input loss, multiplicity,
ratio, and distortion cost must be included. The final checkpoint supplies
no such subcarrier or correlation. Equivalently, an effective output rate
$c_{\rm eff}$ needs $c_{\rm eff}<2(a-\eta)$; an improvement over the saturation
rate $c_{\rm base}$ must exceed $c_{\rm base}-2a+2\eta$.
The coarse $3.54^d$, $3.85^d$, and $4.24^d$ envelope benchmarks are not
sufficient thresholds. Sources: final C4 handoff; T02 current state §§17–18.

**OPEN — retained alternatives:** T02-O2 cross-support overlap; O3 smaller
real support or other carrier geometry; O4 another concrete hybrid mechanism;
O5 arbitrary higher-level input patterns/correlated factors and general
M2-CORR; O6 a justified transfer from shared norm–trace work. In M2-CORR,

$$p^d|\{(x+2y)^{\circ4}:x,y\in S\}|/|S|^2
\ge((p+3)/(4p))^d$$

is sought for nonempty $S\subseteq\mathbb F_p^d$, $p\equiv1\pmod4$.
The $p=5,d=2$ case is **PROVED**. C3's modulus-7 subset optimization and
C4's full critical inverse-image count are **PROVED**, not reopened tasks.
The old C2 overlap screen is **CONDITIONAL** and lacks a concrete overlap source.
Source: T02 current state §13 and [STATUS](tracks/02-quartic-hybrid/STATUS.md).

## T03 — adaptive radical root image

**OPEN — T03-O4, selected RC15/4 obligation:** on the actual adaptive levels
$\mathcal A_m$, write $F_m=\mathbb Q(\mathcal A_m)$,
$n_m=2^{m+1}$, $M_m=\max|\mathcal A_m|$,
$s_m=|Q(\mathcal A_m,\mathcal A_m)|$, $Q=x^2+xy+y^2$.
Seek fixed $H<\infty,m_0$ such that at every $m\ge m_0$ one explicitly chooses

$$C_m^\dagger\in F_m,\quad C_m^\dagger>M_m,\quad
B_m\subseteq\mathcal A_m,\quad n_m-|B_m|\le H\sqrt{n_m},$$

and positive $\gamma_m,u_a\in F_m$ with
$C_m^\dagger+a=\gamma_m u_a^2$, so that $U_m=\{\pm u_a:a\in B_m\}$ satisfies

$$|\gamma_mQ(U_m,U_m)|\le\frac{15}{4}s_m+Hn_m^{3/2}.$$

This is the full signed root image; it is not an energy estimate or a cover
of only selected old pairs. No such uniform rule is known.

**CONDITIONAL:** exception accounting and one-step optimization imply

$$s_{m+1}\le\frac{15}{4}s_m+4Hn_m^{3/2},\qquad
s_m=O((15/4)^m).$$

Every fixed $c<\log_2(16/15)$ would then work, with safe conditional
$c=\frac12\log_2(16/15)$. These constants specify the requested gap; they
are not observed or proved asymptotic rates. Sources: T03 current state §§7,
13–14; current TCRC root-algebra report §6.

**OPEN — retained T03 obligations:** O1 ultimate real target; O2 ARG
($s_m\le K\rho^m$, fixed $\rho<4$); O3 eventual TCRC with legal in-field
parameters, bounded exceptions, one root class, and three affine maps with
coefficients in $F_m$, allowed to vary with $m$ but fixed across every pair
at that level;
O5 general BW-Q/common-weight defect outside settled residues; O6 approximate
PTCR; O7 arbitrary-prime mixed-difference violations; O8 full-progression
ARDC/DSCR contraction. Only O4 is the selected constructive frontier.

**OPEN — historical precision retained:** ARDC seeks fixed $k\ge1$,
$0<\theta<1$ with $p_{m+k}\le\theta p_m$, $p_m=s_m/n_m^2$, on a full
progression of sufficiently large actual levels. Corrected DSCR, with
$u_m=1-b_m$ and $W_m$ the in-field support, requires fixed constants

$$u_{m+k}\le\lambda u_m+Hn_m^{-a},\qquad
W_{m+k}\le(4^k-\varepsilon)W_m+Jn_m^{2-\delta},$$

where $0<\lambda<1$, $a,\delta>0$, $0<\varepsilon<4^k$, and $H,J\ge0$.
Isolated favorable steps and alternative descendants do not justify either
recurrence. Approximate PTCR still requires the fixed power-deficit bound in
[SPEC](tracks/03-eisenstein-cartesianization/SPEC.md); exact PTCR and untwisted
CR are **FAILED** in their stated settings. The older cube-shadow triangle-gap
alternative is preserved as OPEN in the retained STATUS history, not settled
by the specified-prime obstructions. Source: T03 current state §§5–7.

## T04 — affine full-image bound and retained alternatives

**OPEN — T04-O1:** for the exact system

$$A_0=\{0\},\quad A_{m+1}=((2+\sqrt3)A_m+\sqrt3/2)
\cup((2-\sqrt3)A_m-\sqrt3/2),$$

input entropy $a_*>0$ is **PROVED**. Determine whether

$$\limsup_m m^{-1}\log|P_-(A_m,A_m)|<2a_*.$$

A sufficient full-pair encoding has at most $K_0(m+1)^B\kappa^m$ labels,
fixed $K_0,B<\infty$, $\kappa<\Lambda^2$, where
$\Lambda^{-1}+\Lambda^{-3}+\Lambda^{-5}=1$, $\Lambda>1$.
Equal labels must imply equal scalar outputs. All four branch-pair
transitions and scalar carries/relations must be included.
**CONDITIONAL:** every $c_-<2-\log\kappa/\log\Lambda$ would work.
No such encoding is constructed. Sources: T04 current state §§4.9, 13–14,
`sacc_candidate_input.md`, `sacc_input_audit.md`, `sacc_pair_states.md`.

**OPEN — T04-O2, historical alternative:** for inverse-symmetric positive
rational $H$, let $\tau(t)=t+t^{-1}$, $s(t)=t-t^{-1}$, and
$\alpha(t)=s(t)^3+\sqrt3\tau(t)$. Seek arbitrarily large such $H$ with
$|\{\operatorname{Tr}(\alpha(h/k)\bar\alpha(hk)):h,k\in H\}|
\le C|H|^{2-\varepsilon}$ for fixed $C,\varepsilon>0$.
The trace is from $\mathbb Q(\sqrt3)$; excluded subclasses do not exhaust it.

**OPEN — T04-O3, historical local problem:** for fixed distinct odd primes $q,r$,
seek $b_{q,r}>0$ uniformly in depths, $C$, and subsets of
$\mathbb Z/(q^\ell r^m)\mathbb Z$, with

$$|P_C(A,B)|\ge b_{q,r}|A||B|\max(|A|,|B|)/(q^\ell r^m)^2,$$

where $P_C=(x-y)^3+C(x+y)$. Exact self-similar $2{:}3$ is **PROVED**;
general deep singularity is not. This is a local lower-bound problem,
not a positive construction for the cubic.

**OPEN — T04-O4, historical specialization:** in
$R_t=\mathbb Z/(q^{4t}r^{3t})\mathbb Z$, distinct fixed primes $q,r\ge5$,
$C_t=-3q^{2t}r^{2t}$, $H_t=q^tr^tR_t$, $K_t=|H_t|$, seek a depth-independent
$b_{q,r}>0$ for all quotient subsets $X,Y\subseteq R_t/H_t$:

$$|P_{C_t}(X+H_t,Y+H_t)|\ge
b_{q,r}K_t|X||Y|\max(|X|,|Y|)/(q^tr^t)^2.$$

Single full cells do not settle arbitrary unions. Source: T04 current state §7.

## Shared obligations outside the four track identities

**OPEN:** obtain a quantitative full-support mechanism for general full-rank
quadratic forms through addition and multiplication, norm/trace, or more
general solvable extensions. The algebraic reduction is **PROVED**; it does
not provide a suitable common Cartesian carrier or positive output rate.

The [historical Phase B obligations](history-sources/OPEN_LEMMAS_B.md) remain
provenance. Their current scope is:

| Historical entry | Reconciled state |
|---|---|
| O1 sparse local criterion | PROVED for homogeneous binary quadratics over odd fields by rank; OPEN more generally |
| O2 removable deformation | PROVED for common-scaling quadratics and corrected C0; OPEN general classification |
| O3 higher-degree local threshold | OPEN outside the scoped FAILED cubic/quartic certificates |
| O4 prescribed splitting | OPEN for a useful candidate-specific quantitative gain/cost statement; arithmetic existence results alone do not settle it |
| O5 prime powers | PROVED specific T01/T02/T03/T04 formulas and obstructions; OPEN general useful amplification outside those hypotheses |
| O6 correlated sums | OPEN for a concrete full-support mechanism paying every input and output cost |
| O7 beyond boxes | OPEN outside the tested full-interval or continuous-cover certificates |

**OPEN — priority/novelty verification:** the later caution is retained. It is
not an instruction to conduct a literature search during reconciliation.

## 2026-09-16 addendum — disposition of the separate HR-N1 obligation

**HISTORICAL / SUPERSEDED:** the [preceding high-return report, §7](notes/2026-09-16-high-return/README.md#7-one-next-proof-obligation)
recorded the exact $7,19$ HR-N1 return-tail assertion as **OPEN and
untested**. The later [strictly offline HR-N1 proof](notes/2026-09-16-hr-n1-offline/README.md)
settles that assertion as **FAILED**, with a **PROVED** obstruction.

For every $L=10m$, $m\ge2$, at least $|A_L|^2/200$ pairs have only the
identity return, even under all integer powers $u^rv^s$. Consequently the
bad-pair tail cannot have any fixed power deficit for every sufficiently
large $L$. Complete controlling arguments are
[HN1-2, §3](notes/2026-09-16-hr-n1-offline/README.md#3-hn1-2--a-dominant-gap-forces-the-identity)
and [HN1-3, §4](notes/2026-09-16-hr-n1-offline/README.md#4-hn1-3--positive-density-and-disproof-of-hr-n1),
independently audited within the cycle. This is internal proof review, not
external certification or finite experimental inference. No mathematical
experiment or network access occurred.

**OPEN scopes retained:** the actual image size of the specified $A_L$,
any separately justified exceptional-output compression, the original T03
real-set target, and T03-O4/RC15/4. None is resolved by the failure of this
particular action certificate. Existing obligations for T01, T02 and T04
are unchanged. This dated disposition starts no further research cycle.

## 2026-09-16 final freeze — HR-N1 closed, T03-O4 retained

[HR-N1 final proof and handoff](notes/2026-09-16-hr-n1-final-freeze/README.md):
**FAILED / DISPROVED** assertion; its specified return-tail certificate is
**CLOSED**. At least $|A_L|^2/200$ pairs have only the identity return
for every $L=10m$, $m\ge2$, even under all integer powers. This does
not supply an actual-image lower bound.

**OPEN, unchanged:** T03-O1 (target), O2 (ARG), O3 (eventual TCRC), O4
(RC15/4), and the actual image rate for the affected rational carrier.
The only retained next constructive obligation is T03-O4 with its exact
actual-level, in-field, large-class and whole-signed-image hypotheses.
The final report §§H–J states those hypotheses; this documentation freeze
does not begin that obligation or adopt a replacement conjecture.


## 2026-09-16 — character-correlated block cycle completed

The [two-prime cycle](notes/2026-09-16-two-prime-character/README.md)
proves positive finite-product returns and tails (TP-L1/TP-P1), but
closes its group-compatible scalar-action certificate (TP-G1) by the
18-action bound. The normalized CRT rate is separately adverse.
**LOCAL GO / GLOBAL FAIL** does not change any actual real-image status.

**OPEN, retained:** T03 target, ARG, TCRC, RC15/4, and the actual-image
rate of the earlier HR-N1 carrier. HR-N1 itself remains CLOSED. The only
next obligation is the existing **T03-O4/RC15/4** on actual adaptive
levels, with legal in-field parameters, at most $H\sqrt{n_m}$ discarded
inputs, and $|\gamma_mQ(U_m,U_m)|\le(15/4)s_m+Hn_m^{3/2}$.
The new report §10 states the full quantifiers. This cycle starts no
replacement conjecture, difference-set search, affine transfer or proof
of T03-O4.


## 2026-09-16 — unit-exponent cycle disposition

The [unit-exponent cycle](notes/2026-09-16-unit-exponent/README.md)
passes actual action growth but yields **ACTION GO / CARTESIAN FAIL**:
primary orbit coverage is exponentially sparse (UE-P3), and the one
secondary valuation box has identity-only returns on every pair (UE-S1)
and exact quadratic image $n_d^2/4+n_d/2$ (UE-S2).

The primary coefficient family's uncontrolled full-square return behavior
and actual asymptotic image rate are OPEN, not disproved by shell coverage.
The secondary formula is confined to its explicit separated norm-block
sequence. The T03 target, ARG, TCRC and RC15/4 remain OPEN; HR-N1 stays
closed. No replacement return conjecture is adopted.

**One retained next obligation:** T03-O4/RC15/4, with actual adaptive-level
in-field parameters, at most $H\sqrt{n_m}$ omitted inputs and full signed
root support $|\gamma_mQ(U_m,U_m)|\le(15/4)s_m+Hn_m^{3/2}$.
The report §10 states all quantifiers. No further family, affine search or
proof of that obligation was launched during this cycle.


## 2026-09-20 freeze disposition - no new norm-carrier obligation

The [Cartesian norm-symmetry checkpoint](notes/2026-09-20-cartesian-norm-freeze/Cartesian_Norm_Symmetry_Research_Checkpoint.md)
freezes the completed search. Dense Cartesian realization of a high-return
norm orbit is the missing bridge, not an adopted replacement conjecture or
authorization for further search. The general carrier question and primary
actual-image rate remain OPEN.

**One retained next obligation: T03-O4 / RC15/4.** Its exact quantifiers, legal
in-field parameter, large root class, at most $H\sqrt{n_m}$ exceptional
inputs and whole signed-root support bound remain as stated above. This
offline documentation freeze does not attempt that obligation.


## 2026-09-21 authorized branch frontier — DC-O1

The separately commissioned [dense-Cartesianization cycle](notes/2026-09-21-dense-cartesianization/README.md)
proved new scoped obstructions and the rectangular-to-same-set implication
DC-R1. No positive carrier passed its gate. This dated addendum changes
the next obligation for this commissioned branch, preserving the earlier
freeze as history and RC15/4 as a separate OPEN adaptive obligation.

**DC-O1 / OPEN — one high-overlap rectangular return witness.** Construct
explicit finite real $X_d,Y_d$, $A_d=X_d\cup Y_d$, $n_d\to\infty$,
and actual norm-one action families $U_d$, with fixed
$\varepsilon,\eta,\delta>0$, such that
$|X_d\triangle Y_d|\le Cn_d^{1-\eta}$ and, outside at most
$C'n_d^{2-\delta}$ pairs of $X_d\times Y_d$, every pair has at least
$n_d^\varepsilon$ distinct returns into $A_d^2$. Prove scalar membership,
all arithmetic costs and the claimed counts. DC-R1 then certifies every
strict $c<\min(\varepsilon,2\eta,\delta)$. No second mathematical
obligation is adopted by this cycle, and no new search begins in the handoff.


## 2026-09-21 T01 Cartesian-return resolution and retained obligation

The frozen single-step question is now **RESOLVED / PROVED VANISHING**:
\(R_1(N)\le5N^{-1/6}\to0\). In fact
\(E_\tau(A)\le5N^{11/6}\) for all nonzero real steps with a uniform
constant. Source: [new report](notes/2026-09-21-cubic-returns/README.md),
CR-U1 and its complete proof companion; internally independently audited.
The positive-density and almost-full long-path hypotheses are **FAILED**.
This does not resolve the fixed cubic small-image target.

**CR-O1 / OPEN — growing-step Cartesian coverage witness.** Construct
explicit arbitrarily large real \(A_N\), a finite nonzero-step list
\(S_N\), and fixed \(\varepsilon,\delta>0\), so all but
\(O(N^{2-\delta})\) pairs belong to components of size at least
\(N^\varepsilon\) in the graph of returns under \(S_N\). Prove actual
input counts, every endpoint's membership, scalar reuse, and the inventory
size; necessarily \(|S_N|=\Omega(N^{1/6})\). The proved component-count
implication then bounds the entire cubic image. This is the sole next
obligation of this cycle, not an authorized further search. Optimal return
exponents are a retained gap, not an additional adopted next task.


## 2026-09-21 DC-O1 cycle disposition — same obligation, sharper constraint

[DC-O1 witness report](notes/2026-09-21-dc-o1/README.md): no tested
construction has all three positive exponents. Symmetry X=Y is achieved
in two explicit mechanisms, but rich almost-everywhere scalar returns
are not. Independent local return words cannot be multiplied using a
uniform product-domain norm identity that violates the proved scalar
cross-term synchronization theorem.

**One next obligation, still DC-O1 / OPEN:** construct an explicit
high-overlap rectangle with jointly correlated partial domains that
preserve the scalar norm and give n^epsilon distinct genuine returns
outside O(n^(2-delta)) pairs, with |X△Y|=O(n^(1-eta)) and fixed
positive epsilon, eta, delta. This keeps the same quantified witness
problem; it does not adopt another broad search or assume a replacement
conjecture. No further search is launched by the handoff. T03-O4/RC15/4
remains a separate OPEN adaptive obligation, not attempted here.


## 2026-09-21 correlated DC-O1 disposition

The [correlated cycle](notes/2026-09-21-correlated-dc-o1/README.md)
proves scalar composition for all three mechanisms, but none produces
an almost-full polynomial return tail. FS-3 and CR-L2/L3 concern stated
certificates; CD-3 proves a positive-density actual-return obstruction
for its width-one CRT action box. No broader impossibility is asserted.

**One next obligation, unchanged: correlated DC-O1 / OPEN.** Construct
explicit $X_d,Y_d,U_d$ with $n_d=|X_d\cup Y_d|\to\infty$, a proved
whole-scalar norm identity, $|X_d\triangle Y_d|=O(n_d^{1-\eta})$, and
$n_d^\varepsilon$ distinct genuine returns into $X_d\times Y_d$ outside
$O(n_d^{2-\delta})$ pairs, for fixed $\varepsilon,\eta,\delta>0$.
DC-R1 then supplies every strict $c<\min(\varepsilon,2\eta,\delta)$.
The barred tensor, balanced-state and moving-pole searches remain frozen;
no replacement conjecture is adopted. RC15/4 remains a separate OPEN
obligation and is not started by this handoff.


## 2026-09-21 growing-step cycle — CR-O1 retained after scoped progress

**CR-O1 remains OPEN.** The [growing-step report](notes/2026-09-21-growing-step-cubic/README.md)
adds a universal joint-step edge estimate but no stronger universal
coverage threshold than \(N^{1/6}\). New actual-image theorems close only
the stated AP, moderate-width lattice, faithful-box, and rational-completion
families. A generated subgroup is a necessary invariant, not sufficient
finite-fiber connectivity.

The **sole prioritized next obligation** is CR-O1's sublinear-inventory
subcase: explicit \(A_N,S_N\), fixed \(1/6\le\theta<1\) and
\(\varepsilon,\delta>0\), with \(|S_N|\le N^\theta\) and all but
\(O(N^{2-\delta})\) ordered pairs in components of at least
\(N^\varepsilon\) vertices. Prove scalar counts, endpoint membership,
coordinate reuse, useful inventory complexity and all exceptions. The
broader CR-O1 version without the sublinear cap remains unresolved, not
silently replaced as a theorem. No further search is commissioned by this
record, and no arithmetic amplification was started.


## 2026-09-21 sublinear-symmetry cycle — CR-O1 retained

**OPEN — CR-O1 remains the sole adopted next obligation.** The
[sublinear cubic report](notes/2026-09-21-sublinear-cubic/README.md)
requires explicit arbitrarily large real A_N and common step inventories
of size at most N^theta, with fixed 1/6<=theta<1, such that all but
O(N^(2-delta)) pairs lie in components of size at least N^epsilon for
fixed positive epsilon and delta. Actual scalar reuse, finite connectivity,
input multiplicities and every exceptional pair must be proved.

The new quadratic-projection, critical-scale and prime-denominator
obstructions close additional stated families. The new step-size coverage
bound does not raise the universal 1/6 threshold. Their unclosed scope
boundaries are limitations, not additional adopted next obligations or
positive evidence. No witness or positive full-support rate was obtained.


## 2026-09-21 return-tail disposition — same real witness obligation

The [return-tail cycle](notes/2026-09-21-return-tail/README.md)
proves that zero or one identity-only source can coexist with a
quadratic polynomial-threshold bad set. Its modular tail is valid in a
finite ring and its proposed real lift fails. No tested real construction
supplies the required three positive exponents.

**One next obligation, still DC-O1 / OPEN:** construct explicit real
$X_d,Y_d$ and distinct norm-one $U_d$, with
$n_d=|X_d\cup Y_d|\to\infty$, exact whole-scalar norm preservation,
$|X_d\triangle Y_d|=O(n_d^{1-\eta})$, and at least $n_d^\varepsilon$
genuine returned pairs in $X_d\times Y_d$ outside
$O(n_d^{2-\delta})$ sources, for fixed $\varepsilon,\eta,\delta>0$.
The multiplicity must be spread across almost all pairs, not only an
explicit rich orbit or all modular representatives. DC-R1 supplies every
strict $c<\min(\varepsilon,2\eta,\delta)$ once these hypotheses hold.
No tensor, balanced-state, moving-pole, prior cube-root or broad-prime
search is reopened. RC15/4 remains a separate OPEN obligation.


## 2026-09-21 nonlinear coordinate-reuse priority — NR-O1

**OPEN — NR-O1 is the sole adopted next obligation for this T01 direction.**
As stated in the [nonlinear-reuse report, §15](notes/2026-09-21-nonlinear-reuse/README.md),
construct explicit arbitrarily large real A_N, |A_N|=N, and explicitly
parametrized E_N contained in A_N² such that, for fixed delta,epsilon>0,

\[
|A_N^2\setminus E_N|=O(N^{2-\delta}),\qquad
|P(E_N)|=O(N^{2-\varepsilon}),\qquad
P(x,y)=(x-y)^3+x+y.
\]

Prove the distinct scalar and pair counts, every parameter/projection
multiplicity, chart overlaps and the whole complement charge. Degrees
and chart counts must be charged, whether fixed or growing. The exact
completion inequality then supplies every strictly smaller exponent
than min(delta,epsilon).

This is a direct-support obligation and does not require a small symmetry
inventory. It changes the adopted priority from the preceding CR-O1 graph
subcase; CR-O1 itself remains OPEN and is not disproved or solved. The
new curve and low-degree classifications are scoped obstructions, not a
general impossibility theorem. Recording NR-O1 launches no further search.


## 2026-09-30 — ML-O1, coordinate-reusing paired modular lift

**OPEN / one selected obligation for the newly authorized lift branch.**
See the [report](notes/2026-09-30-modular-lift/README.md), §6, and
[proofs](notes/2026-09-30-modular-lift/proofs.md), §8.

For m=6*7^(k-1), t=8*7^(k-1), K_k=Q(zeta_m), choose explicit nonzero
amplitudes c_(k,j) in K_k with disjoint cosets c_(k,j) mu_m. Lift the
canonical free modular orbit by F(T_((-2)^r)p_j)=c_(k,j) zeta_m^r.
The unproved task is to make its same-set scalar completion A_k have
N_k^epsilon distinct genuine returns outside O(N_k^(2-delta)) ordered
pairs for fixed epsilon,delta>0 and N_k tending to infinity. Exact
orbit equivariance is automatic; reuse and cross-orbit returns are not.

This one mechanism specifically avoids ML-4's independent radical tags.
It is not a positive conjecture, a universal necessary form for DC-O1,
or authorization for an additional cycle. DC-R1 gives every strict
c<min(epsilon,delta) if the witness is proved. The general DC-O1 and
separate adaptive RC15/4 obligations remain OPEN; ARG/TCRC and the fixed
T03 target are unchanged.


## 2026-09-30 near-complete charts — NC-O1, equivalent to NR-O1

**OPEN — the single adopted next obligation is an actual small-fiber tail.**
Construct explicit arbitrarily large real A_N, |A_N|=N, and fixed eta,gamma>0
such that, for P(x,y)=(x-y)^3+x+y,

\[
\#\{(x,y)\in A_N^2:
 |P^{-1}(P(x,y))\cap A_N^2|<N^\eta\}
 =O(N^{2-\gamma}).
\]

The [near-complete-chart report](notes/2026-09-30-near-complete-charts/README.md),
NC-C2, proves that the union of large actual fibers supplies E with the
required coverage and output saving. Conversely a near-full compressed E
supplies such a tail with possibly smaller fixed exponents. Thus NC-O1 is
an equivalent reformulation of NR-O1, not a resolution or unrelated assignment.
Distinct scalars, actual returned pairs and every exception must be proved.
A small symmetry inventory is not imposed. CR-O1 remains an OPEN graph
subcase. Recording this statement launches no further research or amplification.


## 2026-09-30 T01 elliptic geometry disposition

**OPEN — EG-O1:** the [report's sole next obligation](notes/2026-09-30-elliptic-geometry/README.md)
is the existing NC-O1/NR-O1 witness, formulated through real coordinate-sharing
curves: for N=|A| choose actual output fibers parametrized by U_z, each
|U_z|≥N^eta, with both scalar endpoints in the same A and total distinct
pair mass at least N²−O(N^(2−gamma)), for fixed eta,gamma>0.
A dense elliptic-sharing network accomplishing this has not been constructed.
The new group-law obstructions narrow a specified architecture; they do
not resolve or replace the original fixed-cubic target.


## 2026-09-30 multiscale packing — ML-O1 retained

**OPEN / one retained next obligation.** The
[multiscale report](notes/2026-09-30-multiscale-packing/README.md) closes
the selected dyadic cosine-product and one mixed-amplitude return
certificates. It does not resolve the earlier ML-O1 obligation: choose
explicit common-cyclotomic-field amplitudes with disjoint orbit cosets
for the primitive 7^k paired lift, whose actual same-set scalar completion
has polynomially many genuine returns outside a power-saving pair tail.
The parameter choices and fixed positive exponents remain exactly those
in the preceding ML-O1 entry. No replacement conjecture is adopted.
General DC-O1, adaptive RC15/4 and T03 remain OPEN.


## 2026-10-06 T01 sharing compatibility disposition

**OPEN — SH-O1**, the [cycle's one next obligation](notes/2026-10-06-sharing-compatibility/README.md):
for r=1/sqrt(3), determine whether an absolute kappa>0 satisfies
|P(A_T,A_T)|≥kappa*|A_T|² for every nonempty finite T⊂R, where
A_T=T+{−r,0,r}. The prescribed triangles always give only Q≤2N−3
pairs; the actual-image obstruction is currently proved here only for
the consecutive strip via GS-A4. The question concerns incidental full-square
collisions within this same family. Its truth is not conjectured here;
a negative answer would not alone prove a fixed power saving.
EG-O1/NC-O1 and the unrestricted fixed T01 target remain OPEN, without
any claim that SH-O1 is equivalent to or resolves them.


## 2026-10-06 cross-block cycle — XB-O1 projective spreading

**OPEN / one next bounded obligation within ML-O1.** See the precise
[statement](notes/2026-10-06-cross-block-returns/README.md), final section.
For m_k=6*7^(k−1), t_k=8*7^(k−1), choose explicit nonzero amplitudes
c_(k,j) in K_k=Q(zeta_(m_k)), with disjoint c_(k,j)*mu_(m_k). Prove
that the actual common scalar completion A_k has n_k→infinity and,
for some fixed kappa>0, every nonzero F-line contains at most
n_k^(1−kappa) scalars of A_k, for every F contained in K_k^+ with
[K_k^+:F]=2. The completion is the union of both real coefficient
projections of the amplitude orbit union under z=x−omega*y.

This is a concrete possible escape gate from bounded-line concentration,
not a positive conjecture, a universal necessary condition or a sufficient
compression theorem. No amplitude candidate was searched after the two
existing dyadic carriers were proved to have quadratic actual images.
ML-O1, DC-O1 and the fixed quadratic target remain OPEN; no automatic
pivot to the separate adaptive RC15/4 obligation is made.


## 2026-10-06 T01 — VG-O1 finite scalar deformation

**OPEN / one next bounded obligation.** The exact system is in the final
section of the [variable-gap report](notes/2026-10-06-variable-gap-sharing/README.md).
Seek increasing x0<…<x26 with x0=0, not an arithmetic progression,
and 51 distinct moving real output labels w_j, −12≤j≤38, such that
P(x_i,x_l)=w_(((i−l)³+i+l)/2) whenever 1≤|i−l|≤3.
Give an exact nonarithmetic realization or prove rigidity of this finite
incidence pattern. Translation alone is normalized, not scale.

The prescribed 150 pairs and 51 output classes are fixed before solving;
579 square pairs are outside the certificate. No solution, deformation
search, asymptotic extension or compression implication is asserted.
The task does not commission SH-O1's broader actual-image question.


## 2026-10-06 XB-O1 disposition and FG-O1 exact matching question

The later [fiber-growth cycle](notes/2026-10-06-fiber-growth/README.md)
proves the current fixed-prefactor XB-O1 screen: for c_(h,j)=h(1+omega*xi^j),
h=1,...,8 and xi of order q=7^(k−1), every permitted subfield line has
at most64sqrt(2)*sqrt(n) completed scalars. The older coefficient-one
asymptotic screen follows for any strict kappa<1/2 eventually. That screening
obligation is thus discharged in its asymptotic form, not left as the
missing step. Separately, FG-F1 proves this carrier's actual imageTheta(n²),
so it cannot witness ML-O1's growing near-full fiber tail.

**FG-O1 / OPEN — one diagnostic lemma, no conjecture adopted.** For the
exact A_q and X_ab defined in the report, classify all33-slot coefficient
matches for a source(X_ab,X_cd) whose33 frequencies are distinct moduloq/7.
Determine whether every target is one of the two orders and simultaneous
signs, or identify all additional matching types. Only the uniform finite
inventory bound48²32⁴ is currently proved. This is a precise residual
rigidity question for an already obstructed family, not a proposed repair
or a replacement positive compression conjecture. The general ML-O1,
DC-O1, adaptive RC15/4 and T03 target remain OPEN. This handoff authorizes
no further proof search by itself.


## 2026-10-06 cross-block amplification disposition — no proxy successor

The later [amplification cycle](notes/2026-10-06-cross-block-amplification/README.md)
keeps FG-O1 frozen and does not pursue its matching classification. It
constructs a valid new balanced-product carrier with 8q²≤n≤48q², but
proves only its specified factor-switch certificate fails on a near-full
square. That carrier's FULL fiber tail and actual image rate remain OPEN;
no full-image lower bound or family impossibility is asserted. The second,
quadratic-phase sum rule fails its required 8q-coset inventory.

Neither proposed amplification mechanism survives. The cycle adopts no
replacement geometric screen, rigidity problem, or new conjecture as a
successor task. The desired full-fiber tail for an explicit real same-set
construction remains the objective. This handoff does not authorize further
search or automatically pivot to adaptive RC15/4. T03, ML-O1, DC-O1,
ARG/TCRC and RC15/4 remain OPEN, and historical FG-O1 retains its separate
unresolved diagnostic status without being selected here.


## 2026-10-06 T01 — VG-O1 resolved; CP-O1 finite bridge attachment

**PROVED resolution:** [CP-R1](notes/2026-10-06-changed-collision-pattern/rigidity.md)
settles VG-O1 by its rigidity alternative. Every increasing normalized real
realization has x_i=i and w_j=2j. The prior OPEN entry and source report
are preserved as historical state, superseded in this exact scope only.

**OPEN / sole next finite obligation:** CP-O1 in the final section of the
[changed-collision report](notes/2026-10-06-changed-collision-pattern/README.md).
For its exact six-scalar bridge A2, construct or exclude one new conic frame
{q±u,q±v}, u,v>0,u≠v,3u²+v²=1, with new center q≠±r,
at least two of its distinct scalars in A2, and a first-coordinate row
x=q±u outside{−a,a} whose two controlled outputs are both0.

This is a finite variable-width attachment system, not a fiber-tail
reformulation. A witness would add a third row to the zero fiber with at
most two new scalars; no witness, search, scaling rule or power saving
is asserted. T01 remains OPEN; global elliptic factorization stays closed
in its accepted scope.


## 2026-10-11 T01 CP-O1 supersession and one torsion obligation

**PROVED resolution of CP-O1:** B-CP in
[the same-date prior checkpoint](notes/2026-10-11-transfer-division-entropy/B_division.md)
excludes its stipulated original six-scalar attachment. The later
[torsion-compatible report](notes/2026-10-11-torsion-compatible-sharing/README.md) independently inspects the role
reduction and verifies all five retained Bezout identities. The preceding
CP-O1 OPEN entry remains historical, superseded in exactly that scope.

**OPEN — TC-O1 / one specified point:** let R1,R2 be the positive-Y points
for the unique different-width attachment in TC-G5. Determine whether
T=R2-R1 is torsion at any order. The exact coordinates are fixed in the
report; orders 2,3,4 are excluded. An infinite-order certificate resolves
this diagnostic. No rank/CM search or growing division computation is
commissioned by this entry. A torsion answer would still be finite and
would not evade the two-width limit or prove a same-set power saving.


## 2026-10-11 T01 TC-O1 resolved by an all-orders certificate

**PROVED — MS-C1:** for the exact TC-G5 positive-Y points,
T=R2−R1 has infinite order. The
[complete arithmetic proof](notes/2026-10-11-marked-shift-certificate/arithmetic.md)
and [independent referee audit](notes/2026-10-11-marked-shift-certificate/referee-audit.md)
check the field, conjugation, good 23-adic embedding, negative valuation
of X(4R2), and the full local logarithm criterion. This supersedes the
preceding TC-O1 OPEN entry in precisely its single-point scope.

No unresolved obligation remains for this commissioned point and no
successor lemma is adopted. The original T01 same-set real image target
remains OPEN; this finite-attachment result gives no asymptotic saving.


## 2026-10-11 T01 one mixed-role varying-output junction

**OPEN — VO-O1:** the sole next finite obligation is stated completely
in [the varying-output report, §6](notes/2026-10-11-varying-output-frames/README.md).
For outputs 0,α,α+β with positive unequal gaps, change exactly the lower
long-frame row to an old lower column. With C(x)=8x(1−2x²), impose
α=C(h),β=C(k),C(H)=α+β and H=s+β/4=k+α/4, together with
3h²+s²=3k²+r²=3H²+S²=1, positive widths and unequal row/column
widths in each frame. Require both long columns in the two short frames'
scalar union, the new lower row outside the old row set, and at least two
new ordered pairs after deduplication. Decide real existence or obstruction.

VO-C5 proves that keeping both former row roles forces equal gaps, which
motivates this one changed role. No feasibility search or witness is claimed;
a finite witness alone would not establish growing coverage. This entry does
not reopen TC-O1, the fixed-output bound or genus-four completion. T01 OPEN.


## 2026-10-11 BFF-O1 direct full-fiber obligation

**OPEN — one next statement on the unchanged balanced-factor carrier.**
Use B,D,V and the exact bilinear expressionM and quadratic keyK from
[the report, §7](notes/2026-10-11-balanced-full-fibers/README.md#7-one-remaining-obligation-bff-o1).
Prove or refute the existence of fixed C≥0,r0 such that for every r≥r0,
at least 32q⁴ ordered sources(v,w) in B² have at most(r+1)^C targets(s,t)
in ALLV² satisfyingK(s,t)=K(v,w). BecauseX is a bijectionV→A, these are
unrestricted full fibers. If true, the actual image is at least
n²/[18(r+1)^C]=n^{2−o(1)}, retiring this carrier without a constant-fiber
classification. The implication is PROVED; the uniform premise is OPEN.

The phase-transposed selected certificate is now closed in its precise
mu6-correction scope. Its failure and the two finite histograms do not
prove BFF-O1. No spreading, energy or formal-state proxy is substituted.
This recorded obligation does not itself authorize another research cycle;
T03 and separate RC15/4 retain their OPEN status.


## 2026-10-11 T01 VO-O1 resolved negatively after verification

**PROVED - VO-C6 / VO-O1 RESOLVED NEGATIVELY.** The original mixed-role
question in the preceding entry has no admissible real solution. The
[freeze note](notes/2026-10-11-vo-o1-freeze/README.md) and independent
referee audit verify the supplied contradiction for its necessary
positive-width subsystem. The cancellation H−k>0 and all strict signs
are justified; no mathematical correction or enumeration was needed.

The previous OPEN entry and source checkpoint are preserved as history,
superseded in this exact signed-role scope only. T01 and other role
patterns remain OPEN. No successor obligation or research cycle is
adopted or authorized by this freeze.


## 2026-10-11 BFF-O1 resolved at all sufficiently large depths

**PROVED — BFF-O1**, superseding its earlier same-day OPEN entry in
exactly the unchanged balanced-factor scope. The
[proof package](notes/2026-10-11-bff-o1/README.md) gives a fixed constant
M bounding ALL V² targets for at least32q⁴ ordered B² sources, for every
sufficiently large r. In the original quantifiers one may take C=1 and
a larger fixed r0. The full image is at least n²/(18M), so this carrier
is retired for fixed power saving. No subsequence or selected-action
qualification is hidden in the conclusion.

No unresolved BFF-O1 step or successor research obligation remains in
this commissioned cycle. The general T03 target, RC15/4 and other carrier
questions remain OPEN; none is disproved or automatically commissioned.


## 2026-10-20 T01 one column-role modification after the tetrahedral test

**PROVED — TJ-C4:** all four registered cases are infeasible; see the
[report](notes/2026-10-20-tetrahedral-junction/README.md).

**OPEN — TJ-O1, not tested:** retain the output rule (0,a,a+b,2a+b),
all conics and positivity/nondegeneracy conditions, and epsilon=-1
opposite-edge sharing from that report. Replace only pattern A's
S=e+p by S=e+q, keeping H=r: the closing columns now reuse the outward
columns of 02/13 instead of their outward rows. Decide existence of an
exact real solution adding at least two distinct closing pairs and a
third distinct first coordinate at output0 orD, with all closing scalars old.
This removes the particular A comparison and does not impose B's S=w.

This is one finite compatibility obligation, not a restatement of the
asymptotic fiber-tail target or evidence of feasibility. No fifth case
was searched. Recording the lemma does not authorize another cycle.
T01 and all roles outside the proved scope remain OPEN.


## 2026-10-20 T03 MS-O1 relative unit inventory at the return cutoff

**OPEN — MS-O1.** Use the unchanged mixed-signature lattice carrier in
[the report](notes/2026-10-20-mixed-signature/README.md) and its
[exact statement](notes/2026-10-20-mixed-signature/carrier-rate.md#7-one-next-bounded-obligation).
With \(K_j=F_j(s)\), \(E_j=K_j(\omega)\),
\(T_0=2\sqrt{D_0\,31^{1/3}}\), and \(L(T)=\frac12\log(48T^6)\),
prove or refute the existence of fixed \(T\ge T_0,\alpha>0,j_0\) such that
\[
\left|\{u\in\mathcal O_{K_j}[\omega]^\times:
N_{E_j/K_j}u=1,\ \|\ell_j(u)\|_1\le d_jL(T)\}\right|
\ge e^{\alpha d_j}\qquad(j\ge j_0).
\]

The inventory is finite and contains every nonzero order-unit return.
Its logarithmic lattice has rank \(d_j\), but the required count is
unproved. A uniform positive return tail implies this gate; its converse
does not follow. Refuting the uniform all-level quantifiers alone would
not exclude an unbounded subsequence. Actual pair-dependent membership,
exception control and the quadratic-image rate remain OPEN.

All seed powers times all torsion give only subpolynomial returns and
are closed as that particular certificate. No new carrier or correlated
window is adopted, and this handoff does not itself commission a new cycle.


## 2026-10-21 T01 TJ-O1 resolved negatively

**PROVED IMPOSSIBLE — TJ-O1; theorem TJ-C6.** The
[proof verification note](notes/2026-10-21-tj-o1-freeze/README.md)
resolves the 20 October changed-column question: epsilon=-1 and
H=r,S=e+q admit no positive real solution under the stated output,
conic and sharing equations. Two independent checking roles and the
lead accepted the supplied contradiction, including the branch step.

The preceding OPEN statement and original checkpoint remain verbatim
as history, superseded only in this exact scope. T01 and other
role patterns remain OPEN. No successor obligation is adopted.


## 2026-10-21 T03 MS-O1 resolved; MS-O2 actual incidence concentration

**PROVED — MS-O1.** The preceding 20 October OPEN population statement
is superseded by [MSU-A1–A3](notes/2026-10-21-relative-unit-population/arithmetic.md).
For an explicit fixed \(K_R\), the unchanged relative order-log lattice
has covolume at most \(K_R^{d_j}\). Fixing
\(T_*=\max\{T_0,\exp(2K_R/3)\}\) gives
\(|U_j(T_*)|\ge2^{d_j}\) at every tower level.

**OPEN — MS-O2, one stronger sufficient incidence lemma.** Retain this
exact \(T_*\), \(A_j\), and full finite unit inventory. For
\(\Omega_j=A_j^2\setminus\{(0,0)\}\), \(N_j=n_j^2-1\), set
\[
D_{j,u}=\{p\in\Omega_j:M_up\in A_j^2\},\quad
S_{1,j}=\sum_u|D_{j,u}|,\quad
S_{2,j}=\sum_{u,v}|D_{j,u}\cap D_{j,v}|,\quad
\mu_j=S_{1,j}/N_j.
\]
Decide whether fixed \(\kappa,\eta>0\) give, for every sufficiently large
\(j\),
\[
\mu_j\ge e^{\kappa d_j},\qquad
S_{2,j}/N_j-\mu_j^2\le e^{-\eta d_j}\mu_j^2.
\]
The [proved implication MSU-R1](notes/2026-10-21-relative-unit-population/README.md#5-full-support-status-and-one-next-lemma)
would then yield every \(c<\min(\kappa,\eta)/(3\log(2T_*+1))\).
The positive population theorem and continuous weight diagnostic do not
establish either incidence bound. This condition is not claimed necessary;
its refutation alone would not retire the carrier. Recording it does not
authorize another cycle. The actual image and unrestricted target remain
OPEN, with the earlier seed certificate still closed.

## 2026-10-21 later T03 — MS-O2-I occupied joint labels

The [completed MS-O2 cycle](notes/2026-10-21-typical-unit-returns/README.md)
does not resolve the preceding concentration assertion or the weaker
tail. It identifies the following exact inverse-return endpoint as the
single next recorded obligation, without launching another cycle.

**OPEN — MS-O2-I.** Keep exactly the fixed \(C_j,R_j,T_*\), and put
\[
Z_j=\{x-\omega y:(x,y)\in C_j^2\setminus\{(0,0)\}\},\qquad
\nu_j=\#\{(zR_j,z\tau z):z\in Z_j\}.
\]
Decide whether there are fixed \(\gamma>0,C_1<\infty,j_0\) such that
\[
\nu_j\le C_1(n_j^2-1)e^{-\gamma d_j}\quad(j\ge j_0).
\]
The [exact orbit theorem](notes/2026-10-21-typical-unit-returns/incidences.md)
proves \(\nu_j=N_j\mathbb E[1/R_j]\) and
\(|Q(A_j,A_j)|\le1+\nu_j\). Therefore this bound would give every fixed
\(c<\gamma/[3\log(2T_*+1)]\) eventually. No such \(\gamma\) is proved.
Counting all ambient norm elements and ideal assignments is insufficient;
the needed count concerns their jointly occupied labels.

This is a reformulation of the user-authorized inverse endpoint, not
a claimed replacement construction or necessary criterion for small
full image. Its refutation would not by itself retire the scalar carrier,
nor exclude all subsequences. The stronger MS-O2, actual image and T03
remain OPEN.


## 2026-10-21 — T01 one cross-block multiscale obligation

**OPEN — MC-O1.** Fix rho=1/64. On D² for a finite D subset [0,7], set
F0(u,v)=P(rho u,rho v) and F1(u,v)=P(1+rho u,rho v).
Let Q4(D) count ordered rectangles of fine pairs with two distinct F0
row labels and two distinct F1 column labels, as defined exactly in
[report §6](notes/2026-10-21-multiscale-collisions/README.md).
Determine whether Q4(D)<=C|D|³ holds with an absolute C, or refute that
specific bound. No rectangle enumeration or proof attempt was made.
This diagnostic couples two maps on the same fine-pair set; it is not
assumed to imply a construction or the original fiber-tail target.
MC-S1–MC-S3 establish the necessary exact branching pattern only.
