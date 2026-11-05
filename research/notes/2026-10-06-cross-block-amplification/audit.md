# Independent whole-factor and rate audit

6 October 2026 · T03 · fixed polynomial
\(Q(x,y)=x^2+xy+y^2\). Specialist C; version 2.

## 1. Authority, frozen scope, and evidence

The live authorized cycle is **Cross-Block Fiber Amplification Beyond
Spreading**. This contribution audits the complete-orbit coverage bound
and the lead-selected candidate formulas. It does not design another
candidate, reopen either previous amplitude family, or pursue FG-O1.
No nested agents, network, or mathematical program execution are used.
Specialist C has zero charged program evaluations and zero research-program
CPU seconds; the lead owns the shared computation budget and its reserve.

Inspected controlling sources:

- [Latest fiber-growth report](../2026-10-06-fiber-growth/README.md), with
  its [amplitude](../2026-10-06-fiber-growth/amplitudes.md),
  [fiber](../2026-10-06-fiber-growth/fibers.md), and
  [audit](../2026-10-06-fiber-growth/audit.md) companions. The two
  previously failed rules and FG-O1 remain frozen.
- [DC-M1](../2026-09-21-dense-cartesianization/matrix-product.md), §§1–2:
  the complete ordered-grid proof and fixed-action consequence were read.
- [Construction ledger template](../../templates/CONSTRUCTION_LEDGER.md):
  counts and rates concern actual real inputs and the entire ordered
  Cartesian square, with each projection or parameter loss charged.
- Current [amplitude proof](amplitudes.md), claims AMP-A1–AMP-A4;
  [return proof](returns.md), claims AMP-R1–AMP-R3; and
  [phase-sum proof](identities.md), claim AMP-G1. Each complete written
  proof was read and independently checked before this version was closed.

This is an independent internal mathematical audit. Reading an inherited
proof is distinguished from proving a new application; no external review,
literature search, novelty assessment, or experiment rerun is claimed.

## 2. Exact DC-M1 consequence for a complete orbit union

**Status: PROVED application of inherited DC-M1; independently checked.**
Let \(A\subset\mathbb R\) be finite and nonempty, with \(n=|A|\),
and let \(\phi(x,y)=x-\omega y\),
\(\omega=(-1+i\sqrt3)/2\). Let \(Z\subset\phi(A^2)\) be an actual
finite set of complex orbit points, with all duplicated labels removed.
Suppose there is one common norm-one multiplier \(u\ne\pm1\) such
that \(uZ=Z\). Define the actual encoded-pair count
\[
\Gamma=|\phi^{-1}(Z)|=|Z|.
\tag{1}
\]
Then
\[
\boxed{\Gamma\le\left\lfloor\frac{3n^2+1}{4}\right\rfloor.}
\tag{2}
\]

**Application proof.** Every \(p\in\phi^{-1}(Z)\) satisfies
\(M_up\in\phi^{-1}(Z)\subset A^2\), because
\(\phi(M_up)=u\phi(p)\). Thus the encoded set is a subset of the
one-action return domain \(D_u(A)\). DC-M1 gives
\(|D_u(A)|\le\lfloor(3n^2+1)/4\rfloor\), proving (2).
The equality in (1) uses the exact real-linear bijection \(\phi\),
not injectivity of any amplitude parametrization.

In the prescribed completion of complete \(\mu_{6q}\)-orbits, one can
always choose \(u=\omega\). It is norm one, is not \(\pm1\), and
preserves every complete orbit. Disjoint amplitude cosets permit the
additional equality \(\Gamma=(\hbox{number of cosets})\cdot6q\);
without disjointness that label product is only an upper bound and cannot
replace the actual \(\Gamma\) in a counting argument.

For the prescribed \(8q\) disjoint \(\mu_{6q}\)-orbits,
\(\Gamma=48q^2\). Equation (2) gives
\(n^2\ge64q^2-1/3\). Since \(n^2\) is an integer, it follows that
\[
\boxed{n\ge8q.}
\tag{2a}
\]
This is an inherited-bound application, not a new candidate or a claim
that the lower bound is attained.

The common non-sign multiplier hypothesis is essential. Closure only
under \(\{1,-1\}\) does not invoke DC-M1. No claim is made for orbit
collections without a common such action.

### Exact meaning of the missing population

Equation (2) implies
\[
|A^2\setminus\phi^{-1}(Z)|
\ge n^2-\left\lfloor\frac{3n^2+1}{4}\right\rfloor
=\left\lfloor\frac{n^2}{4}\right\rfloor.
\tag{3}
\]
These are **unencoded Cartesian pairs**, not pairs proved to have small
fibers. They can have additional collisions with encoded or unencoded
targets. The conclusion gives no bound on their full \(Q\)-fiber sizes,
their incidental returns under other multipliers, or the actual image
size. Even under the fixed \(u\), being unencoded does not imply failure
to return. Conversely, a large encoded orbit supplies only the targets
actually proved inside that orbit; it does not certify a near-full square.

The origin, if present, is one pair with one distinct target. Counting
action labels at the origin does not increase \(\Gamma\) or a genuine
return count. Formula (2) remains valid whether or not the origin is in
the orbit union.

## 3. Whole-factor partial-conjugation audit requirements

The following is a review checklist, not a new construction or a theorem
asserting that any forthcoming candidate satisfies it.

### Exact source and the conjugation operation

For each actual source \(p=(x,y)\in A^2\), start with the assembled
scalar \(z=x-\omega y\). If the proposed mechanism is partial
conjugation, it must give an identity of the form
\[
z=\gamma\prod_{i=1}^{s}\beta_i,
\qquad
z_J=\gamma\prod_{i\notin J}\beta_i\prod_{i\in J}\overline{\beta_i},
\tag{4}
\]
or another equally explicit whole-scalar factorization. The bar must be
the conjugation for which \(N(z)=z\bar z=Q(x,y)\), or a separate exact
norm-preservation proof is required. A field involution used to test
projective spreading is not automatically this conjugation.

For nonzero \(z\) and nonzero factors, (4) yields the actual multiplier
\[
u_J=\prod_{i\in J}\overline{\beta_i}/\beta_i,
\quad N(u_J)=1,\quad u_Jz=z_J.
\tag{5}
\]
The identity is for the full source, including every scalar cross term.
Conjugating one factor of an amplitude does not establish (4) for an
arbitrary pair assembled from coordinates of two different amplitudes.
Conjugating a summand of \(z\) also does not follow from the product
identity. Sources at which a required factor or denominator vanishes
must be treated explicitly. At \(z=0\), positive definiteness forces
\(p=(0,0)\), and there is only one target.

### Membership and coverage

After proving (4), decode every claimed target as
\(z_J=x_J-\omega y_J\) with real \(x_J,y_J\). Both must belong to
the **same actual carrier** \(A\). A formula remaining in the ambient
number field, a formal product alphabet, an amplitude-label set, or a
norm shell does not prove this membership. If a candidate supplies
different coordinate carriers, their symmetrization and unmatched
Cartesian blocks require their own charged proof.

For every source outside an explicitly bounded exceptional set, identify
which factor choices have certified membership. A result only for the
encoded orbit union cannot supply the missing near-full coverage in view
of (3). The unencoded sources remain in the task, but are not presumed
to lack useful collisions.

### Distinct targets and all parameter losses

At a nonzero source, distinct actual multipliers give distinct targets:
\(uz=vz\) implies \(u=v\). Distinct subsets \(J\), factor histories,
branch labels, or conjugation descriptions need not give distinct
multiplier values. Bound those fibers, or prove injectivity, before
crediting exponential return growth. If \(L(p)\) valid labels have
maximum target multiplicity \(M(p)\), the justified lower bound is
only \(L(p)/M(p)\).

Pair-dependent multipliers are allowed if the formulas and domains are
proved. Their existence alone does not produce additional targets:
\((x',y')\) with the same norm is equivalent to the multiplier
\((x'-\omega y')/(x-\omega y)\), so defining that ratio after guessing
a target cannot substitute for proving target membership or counting
distinct equal-norm pairs.

Actual input lower and upper counts, address-to-scalar fibers, denominator
restrictions, field choices, and any thinning are separate from target
counts. Thinning either scalar coordinate affects the pair population
and must be charged twice. Repeated input or action labels give no gain.

### Full-support and rate gate

The required form is a uniform distinct-target lower bound
\(R(p)\ge n^\varepsilon\) outside at most
\(C n^{2-\delta}\) ordered source pairs, with fixed
\(\varepsilon,\delta>0\). A fixed positive fraction of rich pairs,
a large maximum fiber, or a large average collision count does not imply
this statement.

If that lower tail is proved, the inherited same-set support argument
gives
\[
|Q(A,A)|\le n^2/R+|E|,
\tag{6}
\]
where \(E\) is the exceptional source set. Any output containing a good
source has at least \(R\) pairs in its complete fiber, while every
remaining output is charged to \(E\). Thus every strict
\(0<c<\min(\varepsilon,\delta)\) follows after fixed prefactors are
absorbed. This is a proved implication, not an accepted candidate premise.

If only exponential depth bounds are available, keep them separate:
\[
\log n\ge ad-o(d),\quad \log n\le Bd+o(d),\quad
\log R\ge rd-o(d),\quad \log|E|\le ed+o(d).
\]
The corresponding sufficient gap is
\[
2a-\max\{2B-r,e\}>0.
\tag{7}
\]
Exact input growth simplifies this ledger, but formal words, field degree,
or projective spreading exponents cannot stand in for actual input or
fiber growth.

## 4. Frozen-obstruction boundary and candidate status

The former 33-frequency proof applies to its explicitly frozen scalar
alphabet and its complete coefficient calculation. It is not a theorem
about all sparse expressions, all factor products, or all spreading
amplitudes. Applying a related argument elsewhere requires checking that
candidate's complete source and target supports and every allowed
algebraic relation. This audit does not extend the old result or pursue
its remaining exact-matching lemma FG-O1.

The lead selected exactly two formulas: centered-digit factor products
and quadratic-phase sums. Sections 5–7 audit those formulas and no others.
The former passes its amplitude inventory but its specified coordinate
switching certificate fails on a near-full square. The latter fails its
prescribed amplitude inventory. Neither conclusion bounds the entire
image of its deduplicated scalar completion.

## 5. Centered-digit products: inventory and actual scalar size

**Evidence:** independently checked symbolic argument for the lead's
selected first finalist. Fix \(r\ge1\), \(q=7^r\),
\(\xi=e^{2\pi i/q}\), and \(\mu=\mu_{6q}\). For centered
digits \(i_\ell\in\{-3,-2,-1,0,1,2,3\}\), put
\[
P_{\mathbf i}=\prod_{0\le\ell<r}(2-\xi^{i_\ell7^\ell}),
\qquad c_{h,\mathbf i}=hP_{\mathbf i},\quad 1\le h\le8.
\tag{8}
\]
There are q digit words. A zero digit contributes the factor 1.
All factors are nonzero. Let
\[
\mathcal Z=\bigcup_{h,\mathbf i}c_{h,\mathbf i}\mu,
\quad
Y(z)=\frac{\bar z-z}{\Delta},\quad
X(z)=\frac{-\omega^2z+\omega\bar z}{\Delta},
\quad \Delta=1+2\omega,
\quad A=X(\mathcal Z)=Y(\mathcal Z).
\tag{9}
\]
The last equality follows from \(Y(z)=X(\omega z)\) and
\(\omega\mathcal Z=\mathcal Z\). These are real coordinates and
\(X(z)-\omega Y(z)=z\).

### Coset labels do not collide

The relevant cyclotomic relation is the accepted, explicitly proved
seven-slot relation in [FG-A1](../2026-10-06-fiber-growth/amplitudes.md),
§1: a cyclic coefficient
array over \(\mathbb Q(\omega)\) represents zero at \(\xi\) exactly
when its coefficients are constant on each block
\(\{a,a+q/7,\ldots,a+6q/7\}\). It follows from the irreducibility
of \(\Phi_{7^r}\) over \(\mathbb Q(\omega)\), already supplied in
the located field proof. This use does not extend any former full-fiber
obstruction.

If a word has s nonzero digits, its product expansion has coefficients
\((-1)^{|J|}2^{s-|J|}\) at subset sums
\(\sum_{\ell\in J}i_\ell7^\ell\). Balanced base-seven uniqueness
makes these \(2^s\) positions distinct modulo q. In a single seven-slot
block at most two positions are occupied: the lower-digit subset sum is
unique modulo \(q/7\), and the top digit has two choices.

Suppose two amplitudes differ by a multiplier \(\kappa\xi^a\),
\(\kappa\in\mu_6\). The difference of their rotated arrays occupies
at most four positions in each seven-slot block. A constant seven-entry
array with at most four nonzero entries is zero, so the arrays agree
coefficient by coefficient. Each product array has a unique largest
coefficient in absolute value, the positive constant \(h2^s\).
Thus the rotation is zero and \(\kappa=1\). Its smallest nonzero
coefficient magnitude is h, giving equality of scales; the coefficients
of magnitude \(h2^{s-1}\) identify precisely the singleton positions.
Their seven-adic orders and centered representatives recover all the
nonzero digits. The s=0 case is the single constant word and is immediate.
Therefore all \(8q\) amplitude cosets are distinct and
\[
|\mathcal Z|=48q^2.
\tag{10}
\]

### A stronger scalar lower bound than (2a)

Let \(H=\mathbb Q(\xi)\) and
\(\mathcal B=\{c_{h,\mathbf i}\xi^a:a\bmod q\}\subset H\).
Coset disjointness gives \(|\mathcal B|=8q^2\). The map X is
injective on H. Indeed, for \(d\in H\), \(X(d)=0\) implies
\(\bar d=\omega d\); if \(d\ne0\), then
\(\omega=\bar d/d\in H\), contradicting
\(\omega\notin\mathbb Q(\xi)\). The latter is part of the same
coprime cyclotomic field setup used for the seven-slot relation. Hence,
with \(n=|A|\),
\[
\boxed{8q^2\le n\le48q^2.}
\tag{11}
\]
This accounts for all scalar projection coincidences: no assumption of
global injectivity on \(\mathcal Z\) is used. In native depth r the
actual input factor is 49.

### Exact encoded norm classes: final written audit of AMP-A3

The norm array of an amplitude is
\[
N(c_{h,\mathbf i})
=h^2\prod_{i_\ell\ne0}
(5-2\xi^{i_\ell7^\ell}-2\xi^{-i_\ell7^\ell}).
\tag{11a}
\]
Balanced digits give exactly \(3^s\) nonzero positions, at most three
in any seven-slot block. Two norm arrays therefore differ in at most six
positions per block, so equality at \(\xi\) forces coefficientwise
equality. Support size recovers s; the unique largest coefficient
\(h^25^s\) recovers h; and coefficients of magnitude
\(2h^25^{s-1}\) recover precisely the signed singleton positions
\(\pm i_\ell7^\ell\). This determines every absolute digit.
Hence AMP-A3's exact count \(8\cdot4^r\) of encoded norm values
and \(6q\,2^s\) encoded points in each corresponding fiber are
valid. The latter is only a lower bound for the full Cartesian fiber.
The complete written recursion, seed \(A_0=\{-8,\ldots,8\}\),
coset recovery and whole-product action in amplitudes.md also pass.

## 6. Independently switched coordinates: exact certificate obstruction

**AMP-R1–AMP-R3 / PROVED, independently audited scoped certificate
theorem.** For the sets (8)–(9),
allow every independent subset of factor conjugations on each encoded
parent of each scalar coordinate. Retain a resulting pair only when its
actual Q-value equals the source Q-value. Enrich these transitions by
simultaneous sign, coordinate swap, every equal-norm edge whose endpoints
both belong to the encoded set, and arbitrary finite compositions of
these transitions.
For every \(r\ge8\), at least \(n^2/2\) ordered sources have at
most four distinct targets in this generated certificate. More precisely,
the exceptional population is at most
\[
1536q^3 4^r+48q^2,
\quad\hbox{a fraction at most}\quad
24(4/7)^r+\frac{3}{4q^2}=o(1).
\tag{12}
\]
This does not bound full Q-fibers or other return domains on unencoded
pairs. The claim is a proof of failure of this specified certificate,
not a full-image theorem.

### 6.1 Exact amplitude switches and the cross-coordinate defect

For a word \(\mathbf i\) and a subset S of its r positions define
\[
u_{\mathbf i,S}=
\prod_{\ell\in S}
\frac{2-\xi^{-i_\ell7^\ell}}{2-\xi^{i_\ell7^\ell}}.
\tag{13}
\]
It has complex norm one and switches the selected digit signs. For
\(z=c_{h,\mathbf i}\kappa\), \(\kappa\in\mu_{6q}\), the point
\(u_{\mathbf i,S}z\) lies in \(\mathcal Z\). The value of this
multiplier depends on the word and subset, not on the phase \(\kappa\).

For independent encoded parents z,w, the actual assembled source is
\[
\phi(X(z),Y(w))
=\frac{-\omega^2z+\omega\bar z+\omega w-\omega\bar w}{\Delta}.
\tag{14}
\]
For a common norm-one multiplier u, direct subtraction gives
\[
u\phi(X(z),Y(w))-\phi(X(uz),Y(uw))
=\frac{\omega(u-u^{-1})(\bar z-\bar w)}{\Delta}.
\tag{15}
\]
Thus the proposed common-u whole-scalar identity holds exactly when
\(u=\pm1\) or \(z=w\). This identity failure alone would not
rule out an equal norm through another multiplier. The next step counts
all actual norm equalities among the independently switched targets,
including those incidental equalities.

### 6.2 At most four phases yield a new equal-norm target

Fix two amplitude labels, two independently chosen subsets, and a first
phase z. Write their multipliers as u,v and put
\(x=X(z)\), \(x'=X(uz)\). Vary w over the \(6q\) phases of
the second nonzero amplitude. Its squared radius R is fixed and positive,
so \(\bar w=R/w\). Then
\[
y=Y(w)=\frac{R/w-w}{\Delta},\qquad
y'=Y(vw)=\frac{v^{-1}R/w-vw}{\Delta}.
\tag{16}
\]
If \(v\ne\pm1\), the Laurent polynomial
\(\Delta^2[Q(x',y')-Q(x,y)]\) has powers between −2 and 2 and
its coefficient of \(w^2\) is \(v^2-1\ne0\). Multiplication
by \(w^2\) therefore gives a nonzero polynomial of degree at most
four. At most four complex w-values, hence at most four of the distinct
orbit phases, produce equal norm. There is no numerical root test here.

If \(v=\tau\in\{1,-1\}\), then \(y'=\tau y\) and
\[
Q(x',\tau y)-Q(x,y)
=(x'-\tau x)(x'+\tau x+\tau y).
\tag{17}
\]
When the first factor vanishes the target is just \(\tau(x,y)\).
Otherwise equality requires \(Y(w)=-\tau x'-x\). A fixed real
coordinate cuts a nonzero circle in at most two points (equivalently,
(16) is a quadratic in w). Thus this case contributes at most two phases
giving a target beyond \(\{(x,y),(-x,-y)\}\). In either case
the uniform upper bound of four applies.

Let D be the actual set of sources possessing at least one independently
switched, equal-norm target outside their simultaneous-sign pair. Counting
all representations rather than selecting one gives
\[
|D|\le (8q)^2\,4^r\,(6q)\,4
=1536q^3 4^r.
\tag{18}
\]
The factors respectively count amplitude-label pairs, independent subset
pairs, first phases, and the possible second phases. Duplicate labels,
trivial switches, scalar projection coincidences, or duplicated targets
only reduce the actual source count. This union bound therefore covers
every possible encoded-parent representation of every completed source.
No fixed thinning or uncharged choice of representation is used.

### 6.3 Sign, swap, encoded returns, and iteration

Define a scalar replacement relation C by
\[
X(z)\ C\ X(u_{\mathbf i,S}z)
\quad(z=c_{h,\mathbf i}\kappa,\ \kappa\in\mu_{6q}).
\tag{19}
\]
The corresponding Y-based relation is identical, since
\(Y(z)=X(\omega z)\) and multiplication by a switch commutes with
\(\omega\). The relation is reversible: flipping the same positions
in the target word returns the original word, with inverse multiplier.
It is sign equivariant because the phase set contains −1. Consequently
the definition of D using an independently chosen C-replacement in each
coordinate is invariant under simultaneous sign and coordinate swap.
The condition that the new pair is not \(\pm p\) is preserved by both
operations, and Q is also invariant under them.

Let \(\Gamma=\phi^{-1}(\mathcal Z)\subset A^2\). Conjugation
of (8) reverses all digit signs, so \(\bar{\mathcal Z}=\mathcal Z\).
The complex scalar associated with a swapped pair is
\(-\omega\bar z\). Therefore \(\Gamma\), as well as D, is
invariant under sign and swap. Also \(|\Gamma|=48q^2\), and
every allowed encoded edge has both endpoints in \(\Gamma\).
This includes all encoded cyclic returns and partial conjugations, and
allows every equal-norm edge within \(\Gamma\), whether or not its
multiplier has already been listed.

Start with a source \(p\notin D\cup\Gamma\). Any independently
switched equal-norm step can reach only \(\pm p\), by the definition
of D. Sign and swap can reach only the four-point set
\[
\{p,-p,\operatorname{swap}p,-\operatorname{swap}p\},
\tag{20}
\]
and every one of these points remains outside \(D\cup\Gamma\).
No encoded step is available there. Induction on path length now
proves that arbitrary finite compositions of the allowed transitions
remain in (20). Reversal introduces no new edges. The origin, if
present, has only one distinct target; degeneracies of (20) likewise
reduce its size.

Combining (10), (11), and (18) proves (12). At r=7,
\(48\cdot4^7=786432<823543=7^7\), so for r≥8,
\(24(4/7)^r\le2/7\). Also \(3/(4q^2)\le3/196\).
Their sum is less than 1/2, proving the claimed half-square bound.

This enriched certificate includes all independently switched targets
with verified norm equality, common-factor switches, their reversals,
sign/swap symmetries, and every equal-norm edge within the encoded set.
It does not include uncertified \(\mu_{6q}\) membership on unencoded
pairs, arbitrary
additional phase factors on independently switched coordinates, or
other whole-source factorizations. Those cannot be added without a new
membership and counting argument. Actual full fibers remain OPEN.

## 7. Quadratic-phase sum: independent audit of AMP-G1

The complete written proof in [identities.md](identities.md) was read
and independently checked. With \(q=7^r\), it takes
\[
G_j=\sum_{a\bmod q}\xi^{a^2+ja},\qquad c_{h,j}=hG_j.
\tag{21}
\]
For odd q>1, completion of the square gives
\(G_j=\xi^{-j^2/4}G_0\), and the invertible change of variables
\((a,b)\mapsto(a-b,a+b)\) gives
\(|G_0|^2=\sum_{u,v}\xi^{uv}=q\). Every nonzero u, including
nonunits modulo q, has zero inner geometric sum. At q=1 the statement
holds directly. These calculations establish nonvanishing without an
external evaluation of a quadratic exponential sum.

The phase-shift multiplier \(\xi^{-(2js+s^2)/4}\) acts on the
whole scalar, and its decoded targets belong to A whenever the source
belongs to the encoded orbit union. Its labels may repeat; for example,
s and \(-2j-s\) give the same action. For each h, all q amplitudes
lie in one \(\mu_{6q}\)-coset. Different h are separated by norm
\(h^2q\). Thus there are exactly eight actual cosets and \(48q\)
encoded points, with exactly q formal labels per encoded point.

The written scalar bounds \(3q\le n\le48q\) and encoded coverage
\(48q/n^2\le16/(3q)\) are valid. They prove the required
\(8q\)-coset inventory fails for every r≥1. They do not bound
returns on the unencoded population. The r=0 base is correctly isolated;
it cannot establish an asymptotic family. No discrepancy was found in
the phase formulas, real decoding, action duplicates, conjugate heights,
or scope of the written ledger.

## 8. Rate, cost, and final scope ledger

| Item | Independently audited conclusion |
|---|---|
| Target | Fixed Q, same real scalar set in both coordinates, all ordered pairs |
| First finalist's actual input | 8q²≤n≤48q², native-depth input factor 49 |
| First finalist's orbit labels | Exactly 8q distinct amplitude cosets, 48q² encoded points |
| Projection and address fibers | Full union bound over all scalar representations; no injectivity assumed except the proved restriction of X to Q(ξ) |
| First finalist's certified tail | Outside at most 1536q³4^r+48q² sources, the enriched iterative certificate has at most four targets |
| Exceptional fraction | At most 24(4/7)^r+3/(4q²), tending to zero; below 1/2 for r≥8 |
| Tail consequence | This certificate cannot provide n^ε targets off O(n^(2−δ)) exceptions for any fixed ε,δ>0 |
| Second finalist's loss | Exactly q labels per encoded point; required 8q cosets collapse to eight |
| Second finalist's actual input | 3q≤n≤48q, native-depth input factor 7 |
| Input thinning | None performed; discarded labels do not count as actual scalar growth |
| Denominators and arithmetic | All product factors and phase sums are algebraic integers; the common real decode has fixed Δ denominator, with 3X and 3Y integral; switch denominators are nonzero and are used only in exact identities |
| Field degree | For r≥1, Q(ξ,ω) has degree 12·7^(r−1); r is the actual recursion depth |
| Heights | Factor amplitudes have all conjugates bounded by 8·3^r; phase sums have all conjugates bounded by 8sqrt(q); no volume count is used |
| Discriminant, regulator, local density | No estimates or savings from these quantities enter the algebraic certificate obstructions; they are not assigned a fictitious zero cost |
| Carries and branch counts | Balanced base-seven uniqueness is proved for the product inventory; all 4^r independent switch pairs are charged |
| Full-image rate | OPEN for both current completions; no nontrivial full-image estimate is proved here |
| Frozen results | DC-M1 and the field relation are applied within their proved hypotheses; no former full-fiber obstruction is generalized |
| Audit evidence | Independent internal symbolic proofs and written-source inspection, zero mathematical program evaluations, zero research-program CPU, no network |

**Final status:** the two selected formulas fail the stated routes to the
required near-full return certificate. The general T03 construction
remains OPEN. This audit asserts neither a universal obstruction to
partial conjugation or convolution nor a full-fiber obstruction for
either current scalar completion.
