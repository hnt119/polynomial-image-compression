# Open Lemmas — T03 publication extracts

5 November 2026. Selected original T03 sections, in source order. Other tracks are maintained separately. See the [dated evidence register](exports/2026-11-05-evidence/README.md) for the current theorem scopes.

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


