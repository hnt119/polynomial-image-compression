# Mechanism Library — T03 publication extracts

5 November 2026. Selected original T03 sections, in source order. Other tracks are maintained separately. See the [dated evidence register](exports/2026-11-05-evidence/README.md) for the current theorem scopes.

## 2026-09-16 addendum — exact two-prime Cartesian legality

**T03-HRN1-M1 — PROVED, fixed $7,19$ scope.** In the exact HR-N1 carrier
$A_L=\{b7^{-k}19^{-\ell}:1\le|b|\le L,\ \gcd(b,133)=1,
0\le k,\ell\le L\}$, let
$x=b7^{-k}19^{-\ell}$ and $y=c7^{-h}19^{-j}$.
For $u=(8+5\omega)/7$, $v=(21+16\omega)/19$, the conditions

$$k\ne h,\qquad \ell<j,\qquad19^{j-\ell}>4L^2 7^L$$

force every returning $u^rv^s$, $r,s\in\mathbb Z$, to have $r=s=0$.
The argument first uses the simultaneous returned-depth constraints and
real norm bounds to exclude $s\ne0$, uniformly in $r$. It then uses an
exact norm congruence, both returned numerator bounds and coprimality to
exclude $r\ne0$. It does not multiply marginal local return probabilities.

Source and complete proof: [HN1-2, §3](notes/2026-09-16-hr-n1-offline/README.md#3-hn1-2--a-dominant-gap-forces-the-identity),
with elementary local-action proof HN1-1. [HN1-3, §4](notes/2026-09-16-hr-n1-offline/README.md#4-hn1-3--positive-density-and-disproof-of-hr-n1)
counts at least $|A_L|^2/200$ such pairs for every $L=10m$, $m\ge2$.
These are complete internally audited proofs from a strictly offline cycle,
with no experiment or external review. This mechanism supplies an action
obstruction, not a small-support construction or full-image lower bound.
No extension to other primes, numerator families or growing fields is
claimed. HR-1 remains a valid implication; this carrier fails its proposed
nearly full rich-pair hypothesis. RC15/4 is unchanged.

## 2026-09-16 final freeze — T03-HRN1-M1 scope

The [frozen proof report](notes/2026-09-16-hr-n1-final-freeze/README.md)
retains **PROVED** HN1-1–HN1-3 and closes only the **FAILED / DISPROVED**
HR-N1 tail premise. HR-1 remains a proved support implication with explicit
stabilizer and exceptional-output accounting. The obstruction gives few
returns under this specified action, not an upper bound on entire polynomial
fibers. No proved transfer from its rational carrier to adaptive root sets
is in the inspected record; RC15/4 remains **OPEN**. No new mechanism or
replacement return conjecture is introduced by this freeze.


## 2026-09-16 — TP-L1/TP-P1 and the scalar-action realization test

**PROVED in the finite-ring model.** For the equal-quadratic-character
unit subgroup $D\subset\mathbb F_7\times\mathbb F_{19}$, the full
norm-one group $G\cong C_6\times C_{18}$ has trivial pair stabilizers.
The [exact sign/orbit count](notes/2026-09-16-two-prime-character/local-count-proof.md)
gives the return histogram
$8:216,10:270,12:216,18:108,24:648,26:702,30:540,54:216$.
The [product proof](notes/2026-09-16-two-prime-character/product-realization.md)
establishes $R_d=\prod_i r_i$, uniformly $R_d\ge8^d$, and exponential
tails at every fixed threshold below the mean log return. HR-1 yields
formal support at most $154^d$; the actual modular vector image is $130^d$.

**PROVED realization warning, TP-G1/TP-R1.** If a product group of exponent
18 is mapped homomorphically to complex norm-one multipliers, its image
contains at most 18 elements. An equivariant common scalar projection
therefore pays at least $M/18$ repeated labels for $M$ local returns.
This is the exact loss preventing the finite product from proving a real
quadratic saving. It is not a prohibition on every nonhomomorphic lift.

The [report and ledger](notes/2026-09-16-two-prime-character/README.md)
separate these facts from the known normalized CRT obstruction, all unknown
realization costs and the OPEN real target. Internal proofs were audited
and an independent exact oracle corroborated the one-block data; no external
review or novelty is claimed. The verdict is LOCAL GO / GLOBAL FAIL.


## 2026-09-16 — UE-P1/P2 action growth and UE-S1/S2 valuation separation

**PROVED:** pairwise coprime norm blocks give an explicit free subgroup of
actual norm-one fractional multipliers in the fixed Eisenstein field.
For $t_i=3P_{i-1}^{2L+1}$, $q_i=t_i^2+t_i+1$ and
$u_i=(t_i-\omega)/(t_i-\bar\omega)$, a prime factor of $t_i-\omega$
has nonzero valuation on $u_i$ and zero on every other generator.
Thus exponent boxes count distinct actions, including after denominator
clearing and real realization. The [primary proof](notes/2026-09-16-unit-exponent/primary-proof.md)
then gives exact product returns on exponent orbits, including boundary
points. This proves a norm-orbit mechanism, not full Cartesian compression.

**PROVED, UE-S1:** in the exact sparse scalar valuation box
$A_d=\{\pm\prod q_i^{e_i}:|e_i|\le L\}$, norms recover each block's
minimum input exponent. One prime factor with insufficient residual norm
valuation then forbids any nonzero integer unit action at that block.
All pairs are identity-only under the selected group. **PROVED, UE-S2:**
the same rapidly separated sequence makes every at-most-six-term bounded
degree specialization faithful, giving full image $n_d^2/4+n_d/2$.
See the [secondary proof](notes/2026-09-16-unit-exponent/secondary-proof.md)
for all composite-block, sign, denominator and prime-factor details.

The [report's ledger](notes/2026-09-16-unit-exponent/README.md) separates
these scoped obstructions from the OPEN target. Neither group complexity
nor exponential orbit returns supplies almost-full Cartesian coverage.
The previously proved HR-1 implication remains valid; no affine transfer
or positive power exponent is obtained here.


## 2026-09-20 final return-framework handoff

The [frozen checkpoint](notes/2026-09-20-cartesian-norm-freeze/Cartesian_Norm_Symmetry_Research_Checkpoint.md)
retains $R_{\rm label}\ge R_{\rm action}\ge R_{\rm pair}$ and HR-1's
proved full-support implication, including duplicate actions, projection
fibers and exceptional outputs. The two-prime cycle loses exponential
labels at real action realization; the unit cycle achieves actual action
and orbit-return growth but lacks almost-full Cartesian coverage.
No new mechanism is introduced. The specific search is frozen; general
Cartesian-compatible norm symmetry and the T03 target remain OPEN.


## 2026-09-21 dense Cartesianization — exact transport and costs

[Complete proofs and ledgers](notes/2026-09-21-dense-cartesianization/README.md).
**PROVED DC-R1:** if all but $E\subseteq X\times Y$ have $R$ distinct
norm-one returns into $A^2$, $A=X\cup Y$, then conjugate multipliers
supply the reverse rectangle and
$|Q(A,A)|\le n^2/R+|X\setminus Y|^2+|Y\setminus X|^2+2|E|$.
The identity $JM_uJ=M_{\bar u}$ pays the reverse-rectangle transport.
A witness with $R\ge n^\varepsilon$, $|X\triangle Y|\le Cn^{1-\eta}$
and $|E|\le C'n^{2-\delta}$ would certify every strict
$c<\min(\varepsilon,2\eta,\delta)$. The implication is proved; its
construction is OPEN (DC-O1).

**PROVED DC-M1–M3:** a mixed norm matrix returns at most
$\lfloor(3n^2+1)/4\rfloor$ pairs. For rational actions on independent,
action-faithful digit products, these losses multiply, yielding factor
at most $(7/9)^d$ per action. Summed overlap supplies a necessary action
budget, not an almost-all-pairs lower-tail theorem. **PROVED DC-M4/M5:**
faithful quadratic projection of bounded digits fixes their Gram matrix,
so output fibers have size at most $m^4$; this is an actual-image lower
bound in that scope. No general prohibition on correlated digit returns
or many different partial-return domains is inferred.


## 2026-09-21 DC-O1 — partial domains, fringes and scalar compatibility

[New proved implications and exact scopes](notes/2026-09-21-dc-o1/README.md).
For C=X∩Y, F=|X△Y|, h=|X×Y\C²|≤nF, selected action count M and
maximum positive core fiber K, **CF-1–CF-3** give fringe returns ≤2F
pointwise and total ≤min(M,K)h. A rectangular R-tail outside e pairs
transfers under the same actions to a core R/2-tail outside at most
e+2min(M,K)h/R pairs. **CF-4** separately transfers the entire image:
|Q(C,C)|≤|X||Y|/R+e when targets remain in X×Y. This does not assert
that those original actions return into C².

**DC-T1–DC-T3** compare the scalar norm cross terms in an assembled
local product. Under the stated full-span or full difference-span
hypotheses, local rotations must coincide, with no faithfulness premise
on the scalar weights. Formal product return counts become an intersection
of local action sets. Rank-one reflection possibilities and scope limits
are included. A correlated restricted-domain identity remains OPEN.

**MP-1** uses exact rational-function evaluation and a polynomial root
bound to audit moving-pole partial-return domains on correlated words.
Exponential actual action count coexists with uniformly bounded genuine
returns. No full-image lower bound is inferred from that obstruction.


## 2026-09-21 correlated scalar return identities

The [correlated DC-O1 report](notes/2026-09-21-correlated-dc-o1/README.md)
and its complete, internally audited companions establish:

- **FS-1–FS-3 / PROVED:** switching a factor of the whole scalar product,
  $z=ab\mapsto a\bar b$, has exact pair-dependent multiplier $\bar b/b$.
  The specified varying-norm factor code has $4^d$ encoded points,
  $3^d$ norms/actions, and exactly $2^k$ encoded returns at a word with
  $k$ singly occupied sites. Its first projection is injective; these
  returns do not cover the common scalar square.
- **CR-L1–CR-L4 / PROVED:** for $H=\alpha x+\beta y$, $D=\alpha^2-
  \alpha\beta+\beta^2$ and $J=(2\beta-\alpha)x-(2\alpha-\beta)y$,
  $4DQ=3H^2+J^2$. The associated global reflection has a genuine
  pair-indexed multiplier. Target-level capacity and affine-rule costs
  are exact; extra returns from globalizing all ratios are not bounded.
- **CD-1–CD-3 / PROVED:** whole-factor integrality domains on the CRT
  cube-root carrier are explicit. A simultaneous diagonal-residue
  congruence and norm estimate force identity when $W^3>4P/3$;
  an elementary fourth-moment argument gives at least $n^2/48$ such
  ordered pairs, uniformly in depth, for the width-one action box.

All three scalar identities are valid, but none supplies the almost-full
return tail required by the existing DC-R1 support implication. No new
external theorem, support-transport theorem or novelty claim is imported.


## 2026-09-21 return-domain geometry and exact lower-tail accounting

Complete sources and internal audits:
[return-tail report](notes/2026-09-21-return-tail/README.md).

- **RT-G1–RT-G3 / PROVED:** exact grid/line domains, transformed triple
  intersections, ordered domain moments and origin corrections.
  The variance inequality controls the polynomial-threshold tail under
  explicit mean and relative-variance premises. Sign symmetry alone
  eliminates nonzero identity-only points without a growing return rate.
- **CY-1–CY-3 / PROVED:** for the specified full cyclotomic trace carrier,
  $D_{\pm1}=A^2$ and every other selected action has precisely the same
  orbit domain $E$ of size $6p$. The full actual histogram has only
  counts two and $6p$. Sparse coefficient equality is proved over
  $\mathbb Q(\omega)$, including every constant source case.
- **MG-1–MG-4 / PROVED modular results and scoped lift obstructions:**
  the entire scalar alphabet modulo powers of the fixed prime seven
  has an exact torus action, complete stabilizer histogram and
  $B_\varepsilon^{\rm mod}\le(49/36)n^{2\varepsilon}$ for
  $0<\varepsilon<1$. A canonical centered lift changes the real norm;
  finite-group homomorphic rational lifts have at most six actual values.
- **RT-D1–RT-D3 / PROVED:** large coprime rational denominators force
  every equal-norm target into three least-common-multiple states.
  A positive-density elementary coprimality count yields uniform
  subpolynomial full fibers on at least $n^2/400{,}000$ source pairs
  of the specified rational-height sequence.

No new support-transfer theorem or external mathematical result is used.
Only the rational full-fiber argument and the retained integer-fiber
result justify the stated actual-image conclusions; the cyclotomic
selected-action theorem does not automatically give an image lower bound.


## 2026-09-30 — exact modular orbit lift and carry identities

[ML-1–ML-5](notes/2026-09-30-modular-lift/proofs.md), T03,
fixed Q=x^2+xy+y^2, are proved in the new offline cycle with lead
proof checking; no independent review is claimed.

- **ML-1:** exact first- and second-order carry formulas, including the
  matrix-lift defect and the representative wraparound defect separately.
- **ML-2:** Q(f(x),f(x))=Q(f(x),f(-2x)) for all x modulo 7^k forces
  f constant on every valuation class, hence at most k+1 scalar values.
- **ML-4:** canonical free-orbit labels map to 3 theta^j zeta^r, with
  theta=2^(1/D), D=m(2t+1)+1, m=6*7^(k-1), t=8*7^(k-1).
  Exact group equivariance, reality, injectivity and all m distinct
  returns on every encoded orbit are proved. The common scalar
  completion has N=1+t(m/2-1); its cross-shell majority is obstructed.
- **ML-5:** stabilizer size requires at least that many states in a
  faithful equivariant cover. Restricting both modular inputs to units
  avoids this cost and retains at least m/3 modular returns per pair.

The source includes a full arithmetic/rate ledger. The route remains
OPEN beyond its independent-radius completion; exact action realization
alone is not claimed to supply DC-O1.


## 2026-09-30 multiscale packing — exact reuse and bounded-line audit

[Composition proofs](notes/2026-09-30-multiscale-packing/composition.md)
and [local tables](notes/2026-09-30-multiscale-packing/local-gadgets.md).

- **MP-L2/L3 / PROVED:** two exact norm orbits share scalar coordinates;
  the eleven-scalar seed has the full selected-return histogram
  {1:1, 2:64, 6:24, 8:8, 12:24}. Sine doubling supplies exact recursive
  coordinate reuse with input counts between 3*2^d+1 and 3*4^d+1.
- **MS-C1 / PROVED:** conjugation parity prevents mixed-coordinate returns
  on a quadratic population even when many orbit coordinates coincide.
- **MS-C2 / PROVED:** on a quadratic extension K/F, a carrier in h lines
  over F admits at most 4h selected homogeneous norm-one actions on an
  F-independent source. The specified mixed carrier has h=4 and a
  quadratic population of independent pairs.

These are scoped algebraic obstructions to selected return amplification.
There is no positive asymptotic witness or actual-image lower bound for
these two growing carriers. The sole retained next obligation is ML-O1.


## 2026-10-06 cross-block ratios and conjugate-fiber bounds

**PROVED:** [action identities](notes/2026-10-06-cross-block-returns/actions.md),
[exceptional-output table](notes/2026-10-06-cross-block-returns/composition.md),
and [full-fiber proofs](notes/2026-10-06-cross-block-returns/audit.md).

- XB-A1/A2: u=(y−omega*x)/(x−omega*y) swaps a nonzero pair and
  has mixed field parity on opposite-parity sources. A fixed multiplier's
  swap-certified sources lie on one real line. A finite ratio inventory
  doubles the pure cross-parity selected returns from2 to4 exactly.
- XB-A3: v_t=omega*(t−omega)/(1−omega*t) maps (b,tb) to
  (b,−(1+t)b) within the mixed carrier for the explicit sine-doubling
  amplitude sources. This is a sparse genuine cross-block identity.
- XB-F1: the two components of Q fix xy and x²+y², so opposite-parity
  full fibers in the pure carrier are exactly the two orders and signs.
- XB-C1/F2: two nonproportional conjugate norm forms allow at most4
  targets per independent F-line block. Twelve ordered target blocks and
  two exceptional output lines give full-fiber cap48 outside at most
  4(n−1) independent-source exceptions in the specified mixed carrier.

The resulting quadratic actual-image lower bounds apply to these two
carriers and all actions, with no field-height or lambda assumption.
They do not close arbitrary growing collections of subfield lines.


## 2026-10-06 phased-chord spreading and sparse full-fiber rigidity

**PROVED — FG-A1–A5 / FG-F1**, in the
[fiber-growth report and proofs](notes/2026-10-06-fiber-growth/README.md).
In K=Q(omega,xi), xi of order q=7^(k−1), the unique index-two subfield
of K+ is F=Q(xi+xi^-1), with K+=F(sqrt(21)). The involution fixesomega
and invertsxi; a/sigma(a) exactly identifies nonzero F-lines.

The coupled rule c_(h,j)=h(1+omega*xi^j), h=1,...,8, has8q disjoint
cosets, scalar completion n=Theta(q²), and line bound64sqrt(2)*sqrt(n).
All actual scalar patterns are decoded explicitly. Encoded orbit returns
number6q each but cover only48q²=Theta(n) sources.

FG-F1 expands every completed target norm into at most33 cyclic frequencies.
For generic X,X sources those occupy distinct seven-position relation blocks.
Matching all33 source blocks exhausts target support and forces identical
coefficient arrays, bounding full fibers by48²32⁴ on at leastn²/18432
actual pairs. This proves actual imageTheta(n²) for this carrier, independently
of actions. It is a sparse-support obstruction, not the old bounded-line
obstruction; arbitrary other spreading amplitude families are outside its scope.


## 2026-10-06 whole-product conjugation and the cross-coordinate phase cost

**PROVED — AMP-A1–A4 and AMP-R1–R3**, with complete internally audited
[proofs](notes/2026-10-06-cross-block-amplification/README.md).
For q=7^r, the balanced products h prod_l(2−xi^(i_l7^l)) have exactly
8q disjoint cosets and actual scalar size Theta(q²). Partial conjugation
of s nonzero factors gives 2^s distinct amplitude targets, beyond μ_(6q),
with exact encoded fibers 6q·2^s and exactly 8·4^r encoded norm values.
These are actual whole-product identities on the encoded union only.

For generic scalar assembly (X(z),Y(w)), simultaneous switching has an
explicit missing conjugate term. The accepted rejection does not rely on
that discrepancy alone: the full norm equation for independent switches
is quartic in the second phase, with at most four nontrivial solutions
per fixed first phase and switch pair. Charging all 4^r switch pairs
leaves a potential rich-source fraction at most 24(4/7)^r+3/(4q²),
even after sign/swap and all encoded-edge iterations. This is a selected
certificate theorem, not a bound on full fibers or other unencoded returns.

**PROVED — AMP-G1:** quadratic-phase amplitudes G_j=sum_a xi^(a²+ja)
satisfy G_j=xi^(−j²/4)G_0 and |G_0|²=q. The identity is exact but
collapses all j into one cyclic coset per scale. Only eight cosets remain.
No general convolution obstruction or new actual-image lower bound follows.


## 2026-10-11 balanced-factor scalar and full-fiber algebra

**PROVED — BFF-A1–A4**, [algebra proof](notes/2026-10-11-balanced-full-fibers/algebra.md).
For the fixed centered-digit carrier, write B={c_(h,i)xi^a},D={barb−b},
V=B disjoint-union(-B) disjoint-unionD. Then X:V→A is a bijection and
n=16q²+|D| lies between 16q²+1 and 24q²−7. The exact product law is
M(v,w)=2vw+v barw+barv w−barv barw, X(M(v,w))=3X(v)X(w).
Consequently K(v,w)=M(v,v)+M(v,w)+M(w,w) parametrizes the FULL fibers by
K(s,t)=K(v,w) with targets over all V². This is an exact equality reduction,
not a bound on its number of solutions. Full image and fiber tails remain OPEN.

The sole new [phase-transposed mechanism](notes/2026-10-11-balanced-full-fibers/coupled.md)
BFF-P1 has target(X(kappa c' beta),Y(lambda d' alpha)), kappa,lambda in μ₆,
with source phasesalpha,beta inmu_(6q). Its whole norm defect has a nonzero
quartic unless kappa=±omega andc'=d. The degenerate factorization gives only
±swap or±(y,−x−y), with membership conditions retained. BFF-P2 closes this
specific enlarged iterative certificate, not every possible coupled rule.
All claims were independently checked internally and by the lead.


## 2026-10-11 last-layer full-fiber obstruction for balanced products

**PROVED — BFO-L1 and BFO-T1–T4**,
[algebraic localization](notes/2026-10-11-bff-o1/elimination.md) and
[tower/counting proof](notes/2026-10-11-bff-o1/tower.md). The complete
scalar carrier is covered by49 spaces of dimension≤2 over the predecessor
field. At least1344/2401 ordered local source types have direct two-spaces,
so the full quadratic map has Jacobian rank4. A common projection and
monic coordinate equations bound all target-chart fibers by a fixed M
away from fixed-degree polynomial exceptions. Specialization avoids only
an initial segment; predecessor-circle counts give uniformly vanishing
exception density. This proves BFF-O1 and retires this carrier.

This works at one last tower level; it does not multiply branch losses
through r recursive steps or assume bounded original factor support.
Redundant lower-rank target charts, including completed D representations,
are covered by the same exceptional-output polynomial. The general lemma
requires all its stated rank, target-cover and polynomial-avoidance
hypotheses; it is not a universal full-rank quadratic obstruction.


## 2026-10-20 mixed-signature integral unit actions and finite return cutoff

**PROVED — MS-F1–F6, MS-W1–W2 and MS-C1–C2**,
[complete proof package](notes/2026-10-20-mixed-signature/README.md).
Base change \(K_j=F_j(s)\), \(s^3+s+1=0\), has signature \((d_j,d_j)\)
and root discriminant at most \(D_0 31^{1/3}\).
The relative norm-one unit group of \(\mathcal O_{K_j}[\omega]\) has rank
\(d_j\) and acts by integral determinant-one matrices preserving
\(Q(x,y)=x^2+xy+y^2\). Its index in the maximal-order kernel is at most
\(3^{3d_j}\), a charged cost.

For the complete all-embedding box, centered Blichfeldt and norm separation
give exponential lower and upper input bounds. Every nonzero integral-unit
return satisfies
\[
\|\ell_j(u)\|_1\le \tfrac{d_j}{2}\log(48T^6).
\]
This gives a finite exhaustive candidate action set and a uniform absolute
height cutoff. It does not give a uniform bound on each conjugate or many
Cartesian returns. Nonreal eigenvalues have reciprocal moduli; their
complex-bidisk overlap fraction is at most
\(\min(1,4e^{-2|\lambda|})\) per place.

Relative regulator, basis shape, order passage and actual source-dependent
window conditions remain explicit. The full-support implication is
\(|Q(A,A)|\le n^2/R+|\mathcal E|\), using distinct targets and all ordered
pairs. No positive return/exception rates are proved in this cycle.


## 2026-10-21 relative-unit population by ideal and exact norm labels

**PROVED — MSU-A1–A3**, [complete arithmetic proof](notes/2026-10-21-relative-unit-population/arithmetic.md).
In the unchanged mixed-signature tower, product disks with reciprocal
radii \(B_0e^{x_i},B_0e^{-x_i}\) approximate every relative log vector
within \(3d_j\log B_0\). A supplied algebraic integer \(a\) has bounded
ideal norm and a relative norm \(a\tau(a)\) bounded at every embedding.
There are at most exponentially many pairs of these exact labels.
Equal labels give a genuine relative norm-one unit ratio, not merely an
element of bounded absolute norm.

The resulting finite cover of the relative log torus proves
\(\mathcal R_{R,j}\le K_R^{d_j}\), including the order factor \(27^{d_j}\)
once. Centered logarithmic lattice counting then gives at least \(2^{d_j}\)
units in the established return cutoff at one explicit fixed radius.
This resolves MS-O1; no absolute regulator comparison or short basis
is needed.

**PROVED — MSU-G1–G3**, [distortion proof](notes/2026-10-21-relative-unit-population/geometry-audit.md).
The weight is exactly
\(\exp[-2\sum_i(|\ell_i|-\log2)_+]\). Its sum over all units is finite
in each fixed field, with an explicit basis-shape cost. A uniform
discrete upper comparison pays both thin-strip inflation and an
exponential scalar-density prefactor. Neither this upper comparison nor
the positive unit population proves actual return concentration.
The full-rank image question remains OPEN.

## 2026-10-21 later T03 — exact windows and occupied unit orbits

**PROVED — MS2-W1–W3 / MSR-I1–I3.** The
[typical-unit-return package](notes/2026-10-21-typical-unit-returns/README.md)
derives necessary source-translated log intervals and exact complex
cosine and real sine phase conditions for every actual global unit.
The phase lifts of a log vector are one actual torsion fiber, not
independently selectable local rotations.

The exhaustive inventory makes genuine return counts constant on each
full order-unit orbit's intersection with the complete nonzero square.
For component sizes \(m_i\), one has
\[
S_1=\sum m_i^2,\quad S_2=\sum m_i^3,\quad
\sum_{p\ne0}1/R_j(p)=\nu_j,\quad |Q(A_j,A_j)|\le1+\nu_j.
\]
The components are exactly the occupied joint labels
\((zR_j,z\tau z)\); multiple components may share a quadratic output.
This is a full-support implication, not an inference from collision
energy. MTR-L1 supplies a genuine discrete lower domain count, but
its resulting mean rate is insufficient. The required exponential
inverse-return saving and MS-O2 remain OPEN.


