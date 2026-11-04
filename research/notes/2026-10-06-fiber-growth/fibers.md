# Exact fibers and the relative-norm label deficit

6 October 2026 · version 1 · T03 · fixed polynomial
\(Q(x,y)=x^2+xy+y^2=N(x-\omega y)\).

## 1. Scope and claim record

This is the explicitly authorized, strictly offline **XB-O1 → Cross-Block
Fiber Growth** cycle. The lead approved this one relative-norm amplitude
rule as the second finalist, with no repair or parameter scout after its
coset failure. It is distinct from the other finalist's two-term phased
chords. No old carrier, source proof, or checkpoint is edited.

**FG-N1 / PROVED — relative-norm label collapse.** For every integer
\(k\ge2\), the explicit rule (2) below has exactly the required
\(8q\) formal amplitude labels, but at most \(8q/7\) distinct
amplitude cosets modulo \(\mu_{6q}\). Thus it cannot provide the
prescribed injective paired lift. The iterated statement (6) loses a
factor of at least \(7^\ell\) in labels for every permitted depth
\(1\le\ell\le k-1\).

**FAILED:** this exact amplitude rule's required disjoint-coset condition.
This is not an actual-image lower bound or a universal obstruction to
norm composition or to the deduplicated scalar carrier.

**Evidence:** complete symbolic proof below, independently checked by
the lead and audit specialist. Zero mathematical program evaluations,
zero experiment CPU allocation, no network or external theorem import.
There is no external-review or novelty claim.

**Source dependencies:**

- [XB-O1](../2026-10-06-cross-block-returns/README.md), final section,
  specifies \(q=7^{k-1}\), \(m=6q\), \(t=8q\), amplitudes in
  \(K=\mathbb Q(\zeta_m)\), and disjoint cosets \(c_j\mu_m\).
- [ML-4](../2026-09-30-modular-lift/proofs.md), §4, identifies the
  \(8q\) primitive modular orbits, each with \(6q\) elements, and
  the exact paired map obtained from a disjoint amplitude-coset family.
- `research/templates/CONSTRUCTION_LEDGER.md` determines the accounting
  in §4. The arithmetic identity used here is proved locally.

## 2. The one approved relative-norm rule

Fix \(k\ge2\), put \(h=k-1\), and set

\[
q=7^h,\quad m=6q,\quad \zeta=e^{2\pi i/m},\quad
\xi=\zeta^6=e^{2\pi i/q},\quad K=\mathbb Q(\zeta).
\tag{1}
\]

Use the formal labels \((b,r)\), where \(1\le b\le8\) and
\(r\in\mathbb Z/q\mathbb Z\), and define

\[
c_{b,r}=b\prod_{a=0}^{6}\bigl(2-\xi^{r+a q/7}\bigr).
\tag{2}
\]

The factor b is one of eight fixed rational scales. All seven factors
use the same field and a complete seventh-root block. No independent
radical tags or depth-dependent separated rational factors are present.
Each factor is nonzero, so \(c_{b,r}\in K^\times\).
For completeness, at \(k=1\) the rule may be initialized by
\(c_{b,0}=b\), \(1\le b\le8\); the failure at every later
level is sufficient for the asymptotic obligation.

Let \(\eta=\xi^{q/7}\), a primitive seventh root of unity.
The monic degree-seven polynomial with roots \(\eta^aX\),
\(0\le a\le6\), is \(T^7-X^7\). Evaluating at T=2 gives

\[
\prod_{a=0}^{6}(2-\eta^aX)=2^7-X^7.
\]

Taking \(X=\xi^r\) proves the exact seventh-root block identity

\[
\boxed{c_{b,r}=b(128-\xi^{7r}).}
\tag{3}
\]

Here “relative-norm” names the proposed norm-inspired seventh-root block
product. The displayed product, rather than an unstated field-norm
interpretation, is the definition at every label. For labels divisible
by seven it need not equal the literal degree-seven field norm of
\(2-\xi^r\). No such identification is used in the proof.

This is a whole-scalar algebraic identity, not an equality of norms
alone. Its very coupling also removes the top seventh-root address:

\[
c_{b,r+q/7}=c_{b,r}.
\tag{4}
\]

For each fixed b there are exactly \(q/7\) distinct amplitudes,
since the remaining \(\xi^{7r}\) values are distinct. Different
b-values could only create additional coset identifications; their
possible absence is not needed. Thus the \(8q\) formal amplitude
labels give at most \(8q/7\) distinct \(\mu_m\)-cosets.

The paired encoding of ML-4 would send the labels \((b,r,j)\) to
\(c_{b,r}\zeta^j\), \(0\le j<m\). Keeping the same j and
changing r by q/7 already produces seven identical complex points.
Consequently

\[
\#\{c_{b,r}\zeta^j\}\le\frac{8q}{7}\,6q
=\frac{48q^2}{7},
\tag{5}
\]

whereas the prescribed primitive plane contains \(48q^2\) points.
Any restriction making this particular label map injective must delete
at least six sevenths of its source labels. This is a **pair-label**
deficit, not an asserted scalar thinning rate or an image bound.

## 3. Iterated composition and its exact scope

For \(1\le\ell\le h\), composing complete seventh-root blocks
gives

\[
c^{(\ell)}_{b,r}
=b\bigl(2^{7^\ell}-\xi^{7^\ell r}\bigr),
\qquad
c^{(\ell)}_{b,r+q/7^\ell}=c^{(\ell)}_{b,r}.
\tag{6}
\]

Here the scale b stays outside the composed norm. To check the
recurrence, multiply the unscaled \(\ell\)-level expression over
\(r+a q/7^{\ell+1}\), \(0\le a\le6\), and use the same
degree-seven identity. It replaces \(2^{7^\ell}\) by its seventh
power and \(\xi^{7^\ell r}\) by its seventh power, proving the
next level. There are at most \(8q/7^\ell\) distinct amplitude
cosets and at most \(48q^2/7^\ell\) encoded complex points.

The failure in (4) occurs before a generic completed-Cartesian return
can be inferred. Multiplication by every element of \(\mu_m\)
still preserves Q on each encoded orbit, but duplicate amplitude
addresses do not become distinct scalar targets. Partial conjugation
of a factor product also preserves its complex norm; no membership of
its two coordinates in the completed scalar set follows from that
identity. Neither formal factor choices nor the norm identity can
repair the violated coset requirement in (4).

This note does not silently enlarge the eight scales, change the label
range, pass to a larger field, or retain only selected norm factors.
Each would be a different amplitude rule and needs separate authorization
under the current two-finalist limit. No such mutation is made.

## 4. Full accounting of this preselection failure

| Item | Exact bound or limitation |
|---|---|
| Prescribed labels | 8q amplitude labels and 6q rotations, hence 48q² primitive pair labels |
| Actual amplitude cosets | At most 8q/7 after one relative norm; at most 8q/7^ell after ell levels |
| Equality and projection fibers | At least 7 repeated labels already give exactly the same complex point, before real projection; real projection cannot undo equality |
| Required input thinning | At least 6/7 of pair labels must be deleted for injectivity of this map; no unproved same-set scalar thinning is inferred |
| Same-set completion | Can still be formed from the deduplicated complex union, but its size and full-image rate are not established here |
| Norm preservation | Whole multiplication by μ_m preserves Q exactly; the seven-factor identity (3) is exact |
| Field degree | Inherited cyclotomic field degree [K:Q]=12·7^(h−1) for h≥1; no auxiliary extension |
| Denominators and heights | All amplitudes are algebraic integers; every conjugate has absolute value at most 8·129 at one level, and at most 8(2^(7^ell)+1) after ell levels |
| Discriminant and regulator | Not evaluated or set to zero; neither is required for this exact equality obstruction |
| Archimedean values | 127b≤abs(c_(b,r))≤129b; these estimates are not used to assert disjoint cosets |
| Local moduli and splitting | No congruence sieve or splitting gain is invoked; q specifies the angular order |
| Branch/return count | A 7-way address block collapses; formal label multiplicity cannot be charged as genuine returns |
| Exceptional or uncovered population | Formula (5) is a global paired-encoding deficit, not an exceptional-tail estimate on an uncomputed scalar square |
| λ,ρ,δ or output saving | None asserted for the deduplicated carrier; this exact rule fails the required injective-lift gate before those quantities |
| Finite evidence | No scout, sampled data, or mathematical program execution; proof and independent symbolic inspection only |

The disposition is **FAILED at the prescribed disjoint-coset gate**,
with the general real quadratic target and other amplitude mechanisms
unchanged. Further analysis in this cycle concerns only the already
approved first finalist, not a repaired relative-norm family.

## 5. FG-F1 — full fibers of the approved phased-binomial carrier

This section analyzes the **first already approved finalist**, without
changing its amplitudes. It is separate from the relative-norm rule
in §§1–4. The following proof counts complete polynomial fibers,
including targets obtained by arbitrary norm-one multipliers. Its
conclusion is stronger than a failure of any selected action list.

### Statement and exact scalar set

Fix \(k\ge2\), put \(q=7^{k-1}\), and retain \(m,\zeta,\xi,K\)
from (1). Write \(\omega=e^{2\pi i/3}\) and
\(\Delta=1+2\omega\), so \(\Delta^2=-3\). The first finalist's
amplitudes and complete orbit union are

\[
a_{h,j}=h(1+\omega\xi^j),\quad 1\le h\le8,
\quad j\in\mathbb Z/q\mathbb Z,
\]
\[
\mathcal Z_q=\{h\kappa(\xi^a+\omega\xi^b):
1\le h\le8,\ \kappa\in\mu_6,\ a,b\in\mathbb Z/q\mathbb Z\}.
\tag{7}
\]

The equality of the two orbit descriptions follows from
\(\mu_{6q}=\mu_6\mu_q\). Decode
\(\xi^a+\omega\xi^b=X_{ab}-\omega Y_{ab}\) with real
coordinates. Explicitly, put

\[
C_a=\frac{\xi^a+\xi^{-a}}2,\qquad
D_a=\frac{\xi^a-\xi^{-a}}{2\Delta},
\]
\[
X_{ab}=C_a+D_a-2D_b,\qquad
Y_{ab}=-C_b-2D_a+D_b.
\tag{8}
\]

The same-set coordinate completion is exactly

\[
A_q=\{h\varepsilon T_{ab}:1\le h\le8,\ \varepsilon\in\{1,-1\},
\ T\in\{X,Y,X+Y\},\ a,b\in\mathbb Z/q\mathbb Z\},
\qquad n=|A_q|.
\tag{9}
\]

Indeed, the six Eisenstein units permute and change the signs of
x, y, and x+y. Formula (9) is an exact equality of sets, allowing
every duplication of formal labels.

**FG-F1 / PROVED.** Let \(C_*=48^2\,32^4\). At least

\[
\frac{q^4-3696q^3}{4}
\tag{10}
\]

distinct ordered pairs in \(A_q^2\) have their **complete** Q-fiber
in \(A_q^2\) of size at most \(C_*\). A negative bound is
vacuous. For \(q\ge7392\), the input bounds and consequences are

\[
\frac{q^2}{2}\le n\le48q^2,
\qquad
\#\{p\in A_q^2:\#Q^{-1}(Q(p))\cap A_q^2\le C_*\}
\ge\frac{n^2}{8\cdot48^2},
\tag{11}
\]
\[
\boxed{|Q(A_q,A_q)|\ge\frac{n^2}{8\cdot48^4\cdot32^4}.}
\tag{12}
\]

Together with the trivial upper bound, (12) proves quadratic actual
image size for this explicit family. Every fixed power saving is
therefore impossible on this carrier, regardless of the action family.
The proof is elementary exact algebra below; finite data are not a
premise. The lead and independent auditor checked the coefficient
vectors, saturation argument, population count, and reconstruction bound
before this complete proof was written.

### 5.1 Exact seven-slot coefficient relations

Let \(E=\mathbb Q(\omega)\) and \(L=q/7\). For coefficients
\(e_r\in E\), one has

\[
\sum_{r=0}^{q-1}e_r\xi^r=0
\quad\Longleftrightarrow\quad
e_{a}=e_{a+L}=\cdots=e_{a+6L}
\quad(0\le a<L).
\tag{13}
\]

Here the common value may depend on a. To justify the necessary
minimal polynomial, \(\Phi_q(T)=\sum_{j=0}^6T^{jL}\) is
irreducible over E. One internal proof uses the accepted Eisenstein
criterion in the Eisenstein integer ring: \(\pi=3+\omega\) has
norm7, \(7=\pi\bar\pi\), and \(\pi^2\nmid7\). The shifted
polynomial \(\Phi_q(T+1)\) has all nonleading coefficients divisible
by7 and constant coefficient7, so is Eisenstein at \(\pi\).
The divisibility follows also from
\(\Phi_q(T+1)\equiv T^{6L}\pmod7\). Primality of \(\pi\)
follows from its prime norm; the distinct conjugate primes show
\(\pi^2\nmid7\). These are the same elementary Eisenstein-ring
facts accepted in the earlier cyclotomic proof system, not a new
external input.

For a polynomial of degree at most q−1 vanishing at \(\xi\),
division by this minimal polynomial leaves a quotient of degree at
most L−1. Multiplication by \(\Phi_q(T)\) puts each quotient
coefficient in precisely its seven positions a+jL. This proves both
directions of (13).

We will refer to each residue class modulo L as a **coefficient block**.
Equality is still equality of actual algebraic numbers; the blocks
describe all allowed relations, rather than assuming formal independence.

### 5.2 The three scalar numerator patterns

Multiply (8) by \(\Delta\), and use \(1+\omega+\omega^2=0\).
The coefficient vectors at angular positions \((a,-a,b,-b)\) are

| Scalar numerator | Coefficients at (a,−a,b,−b) |
|---|---|
| ΔX_ab | (−ω², ω, −1, 1) |
| ΔY_ab | (−1, 1, −ω, ω²) |
| Δ(X_ab+Y_ab) | (ω, −ω², ω², −ω) |

Every coefficient is nonzero. In each row the products at the two
opposite-position pairs are both −1. The formula holds even when
some positions coincide; in that case their coefficients must be added.

For any pair of elements of (9), its normalized norm
\(\Delta^2Q(x,y)\) is therefore represented by a cyclic polynomial
over E supported on at most the following 33 formal frequencies, for
some four angular parameters \(v=(v_1,v_2,v_3,v_4)\):

\[
\mathcal L(v)=\{0\}\ \cup\ \{\pm2v_i:1\le i\le4\}
\ \cup\ \{\varepsilon v_i+\varepsilon'v_j:
1\le i<j\le4,\ \varepsilon,\varepsilon'\in\{1,-1\}\}.
\tag{14}
\]

There are one constant slot, eight double slots, and 24 mixed slots.
These are formal frequency formulas before reduction modulo q.
Coincidences can only reduce the support size.

Now take the particular source pair
\(x=X_{ab}\), \(y=X_{cd}\), and write \(v=(a,b,c,d)\).
If the 33 expressions in (14) lie in distinct coefficient blocks
modulo L, then all 33 source coefficients are nonzero:

- Each double slot comes from a square of a nonzero coefficient.
- Each mixed slot inside a single scalar comes from twice a product
  of nonzero coefficients; each mixed slot using the two different
  scalars comes from their product in xy.
- The constant coefficient is \(-4-4=-8\), from x² and y².
  No mixed frequency can coincide with zero under the assumption.

Such a source is called **separated** only for the present coefficient
argument. No separated amplitude tags or numerical digit encoding are
being introduced: the carrier remains exactly (9).

### 5.3 Support saturation forces exact coefficient matching

Fix a separated source and any target \((x',y')\in A_q^2\) with
\(Q(x',y')=Q(x,y)\). Choose any labels in (9) for the target and
form its normalized cyclic norm polynomial, reducing exponents modulo q
and combining identical positions. Its support has at most 33 positions
by (14). The source has exactly 33, each in a different block modulo L.

Every occupied source block must contain at least one target support
position. Otherwise the source-minus-target coefficient vector in that
block would have one nonzero entry and six zero entries, contradicting
(13). The 33 occupied source blocks thus use the target's entire support
budget. There is exactly one target position in each of those blocks
and no target position in any other block.

Within one such block, the difference of a source singleton and a
target singleton has at least five zero entries. If its seven entries
are constant, they are all zero. Thus the two singleton positions and
their coefficients agree. We have proved exact equality of the two
cyclic coefficient arrays, not just equality after evaluation at ξ.

An equivalent cost description is that replacing one source slot by
a nonzero seven-slot relation needs at least six target slots in that
block, while only one is available. This explains why the cyclotomic
relations do not create additional target freedom for this population.

### 5.4 Reconstructing targets from a bounded frequency inventory

The target now has 33 nonzero cyclic coefficients. Its formal inventory
(14) has only 33 slots, so every one of its formal frequencies must
remain distinct modulo q; none can be lost by a coincidence or
cancellation. In particular its eight double slots are nonzero and
are among the source's 32 nonzero frequencies.

Since q is odd, multiplication by2 is invertible modulo q. For each
of the target's four angular parameters \(v'_i\), the condition
\(2v'_i\in\mathcal L(v)\setminus\{0\}\) gives at most 32
possibilities. This yields at most \(32^4\) angular quadruples.
Each target scalar has at most 48 choices of type, scale, and sign:
three patterns, eight positive scales, and two signs. Therefore the
complete target fiber has size at most

\[
48^2\,32^4=C_*.
\tag{15}
\]

This is a label upper bound, hence also bounds distinct actual targets
even when labels collide. It counts all target scalars in the completed
set and imposes no restriction on how a target is obtained. In particular
it is not a bound merely on the original encoded orbit or a fixed list
of rotations.

### 5.5 Counting separated source pairs without assuming injective labels

There are \(\binom{33}{2}=528\) possible coincidences between
distinct formal expressions in (14). The difference of two such
expressions is a nonzero integer linear form in a,b,c,d with every
coefficient between −4 and 4. At least one coefficient is nonzero and
therefore prime to 7. For each fixed choice of the other three variables
modulo q, its vanishing modulo L fixes one residue of the remaining
variable modulo L and thus exactly seven residues modulo q.
Each coincidence excludes \(7q^3\) quadruples. The union bound
therefore leaves at least

\[
q^4-528\cdot7q^3=q^4-3696q^3
\tag{16}
\]

separated quadruples. No independence between the exclusion events
is assumed.

The map \((a,b)\mapsto X_{ab}\) has fibers of size at most 2.
For a direct check, use the automorphism fixing ω and sending
\(\xi\mapsto\xi^{-1}\). It preserves the real subfield, fixes
\(C_a\), and negates \(D_a\). Equality of two X-values in (8)
therefore fixes \(C_a\). Equality
\(\xi^a+\xi^{-a}=\xi^{a'}+\xi^{-a'}\) gives
\(a'=a\) or \(a'=-a\), by the roots of the associated quadratic.
For either choice the remaining equation fixes \(D_b\).
The map b↦D_b is injective when q is odd: equality for
\(w=\xi^b,z=\xi^{b'}\) gives
\((w-z)(1+1/(wz))=0\), and \(wz=-1\) is impossible in μ_q.
Thus at most two labels remain.

Consequently the source-pair map has fibers at most 4. Dividing (16)
by 4 proves (10). The same one-coordinate argument gives
\(n\ge q^2/2\); the complete label count in (9) gives
\(n\le48q^2\). If \(q\ge7392\), then (16) is at least
\(q^4/2\), so at least \(q^4/8\ge n^2/(8\cdot48^2)\)
distinct source pairs have full fiber bounded by (15). Partitioning
that population by its actual Q-values proves (12).

### Meaning, return-tail consequence, and limits

Generic cross-block pairs carry 33 independent coefficient blocks in
their scalar norm. Every completed target has room for at most 33
coefficients. Thus the allowed cyclotomic relations cannot change even
one occupied block, and each target's angular parameters come from a
fixed finite inventory. This identifies a concrete full-square deficit
in the proposed fiber-growth mechanism; the obstruction does not come
from restricting the action group or from a bounded number of subfield
lines.

For every fixed \(\varepsilon>0\), eventually \(n^\varepsilon>C_*\).
Every possible family of norm-one actions then has at least
\(n^2/(8\cdot48^2)\) pairs below that return threshold, since its
distinct targets lie inside the complete Q-fiber. Hence there is no
power-saving bad-tail exponent for this carrier. The small encoded
norm orbits, any additional factor-switching actions, and finite observed
rich fibers cannot evade (12).

This is an obstruction for exactly (7)–(9), with the fixed eight scales.
It does not establish a no-go for all cyclotomic amplitudes, all
projectively spread sets, or the unrestricted real quadratic target.
No additional amplitude rule or repair is proposed.

## 6. FG-F1 quantitative and evidence ledger

| Item | Rigorous accounting |
|---|---|
| Actual same-set input | The full completion (9), q²/2≤n≤48q²; no scalar labels treated as distinct without proof |
| Input thinning | None in the carrier; (16) identifies a source population for an obstruction and charges its complement explicitly |
| Source projection fibers | At most 2 for X_ab and at most 4 for the ordered source pair, proved in §5.5 |
| Target projection fibers | Overcounted by 48²32⁴ labels; duplicates cannot enlarge the actual fiber |
| Source exceptions | At most 3696q³ angular quadruples, by an exact congruence union bound; no random sampling or heuristic independence |
| Complete target support | At most 33 cyclic coefficients for every pair in A², including all signs, scales and unit-coordinate patterns |
| Field relations | All seven-slot relations over Q(ω) proved in (13); no quadratic-faithfulness assumption or omitted relation |
| Full-fiber bound | C_*=48²32⁴ on at least(q⁴−3696q³)/4 actual pairs; uniform in depth |
| Full-image lower bound | n²/(8·48⁴·32⁴) for q≥7392; this is independent of any action family |
| Field degree and denominators | [K:Q]=12·7^(k−2); Δ²=−3 clears the common scalar-norm denominator exactly |
| Heights and archimedean size | The eight scales and four scalar coefficients are bounded absolutely; no asymptotic height saving is used |
| Discriminant and regulator | Not evaluated or set to zero; the finite coefficient argument does not depend on either |
| Branches and ratios | All 48 scalar types and all target angular quadruples are charged in (15); formal paths supply no extra gain |
| Growth and exponent | n is Theta(q²); at native depth k−1 this gives n=49^(k−1+o(k)), hence input factor λ=49. No normalized leading constant is assumed. Actual image is Theta(n²), so no positive c survives |
| Programs and evidence | This proof used zero mathematical program evaluations and no network; any lead-run finite scout is separate evidence, not a premise |

The prescribed second finalist fails its disjoint-coset gate by FG-N1,
and the approved first finalist fails the full-image gate by FG-F1.
The general target and any separately stated next obligation retain
their own status; neither proof authorizes another family search.
