# Multiscale packing: independent rate and obstruction audit

Date: 2026-09-30. Track: T03, fixed polynomial
\(Q(x,y)=x^2+xy+y^2\). Author role: Agent D, independent internal auditor.

## 1. Identity, provenance, and task boundary

This note records the explicitly commissioned offline multiscale cycle. It is
an internal mathematical audit, not external review or a literature/novelty
check. Agent D ran no mathematical programs or experiments. File inspection
and symbolic derivation are the evidence recorded here.

The controlling instruction is the current attachment
`[private attachment identifier withheld]`, headed “Full-Rank
Quadratic — Multiscale / Fractal Packing Search.” Historical carrier searches
and the latest modular-lift proof remain unchanged. In particular:

- `../2026-09-30-modular-lift/proofs.md`, ML-4, supplies the frozen exact
  paired lift and the specific independent-radial-tag obstruction. Reading
  that source for this audit does not constitute a new independent audit of
  its entire proof.
- `local-only/migration/sources/T03_CURRENT_STATE.md`, §10, “Precise standard
  results assumed,” item 3, explicitly accepts that rings of integers are
  Dedekind domains with unique ideal factorization. This is an **EXISTING
  ACCEPTED STANDARD INPUT**, recorded there as an external result not
  externally verified in that source. The fixed-field gate below uses this
  input; it is not attributed to HR-4 or claimed as a new external import.
- The same current-state source, §6.3, “Quantitative scopes retained from the
  earlier proofs,” already records the **PROVED global ideal bound** and its
  fixed-field polynomial-house obstruction. That is a frozen inherited
  result. Section 3 below checks its hypotheses for affine recursions; it
  does not claim a new ideal-fiber theorem or re-prove the frozen result.
- `../2026-09-16-high-return/denominator-obstruction.md`, Lemma HR-4B,
  supplies the elementary, complete bound
  \(\tau(N)\le D_\theta N^\theta\) for every fixed \(\theta>0\).
- `research/templates/CONSTRUCTION_LEDGER.md` determines the cost categories
  in §4 below.

The fixed-field result is a **preselection filter**, not a third serious
construction. It addresses exactly the fixed-field affine recursions proposed
for inspection in this cycle. It does not restart a frozen carrier search.

## 2. Finite seed audit

### MS-A1 — exact four-point seed table

**Status: PROVED; independently checked symbolically in this task.** This is
historical finite-seed reuse, not a new interval family or an asymptotic claim.
Put
\[
A_* = \{-2,-1,1,2\},\qquad
v=\frac{8+3\omega}{7},\qquad
U_* = \mu_6\cup\{v,-v,v^{-1},-v^{-1}\}.
\]
Here \(\omega^2+\omega+1=0\), and multiplication acts by
\[
M_{a+b\omega}(x,y)=(ax+by,-bx+(a-b)y).
\]
The identity \(N(v)=(64-24+9)/49=1\) holds, and
\(M_v(1,2)=(2,1)\). The ten elements of \(U_*\) are distinct: the four
nonunit fractions have coefficients different from those of \(\mu_6\),
and \(v\ne\pm v^{-1}\).

The complete ordered-pair norm table is

| Norm | Ordered pairs |
|---|---:|
| 1 | 2 |
| 3 | 6 |
| 4 | 2 |
| 7 | 4 |
| 12 | 2 |

For \(v\), integrality of both target coordinates requires and is implied by
\(x+3y\equiv0\pmod7\). On \(A_*^2\), this leaves exactly
\(\pm(1,2)\), whose images are \(\pm(2,1)\). Consequently
\[
D_v=D_{-v}=\{(1,2),(-1,-2)\},\quad
D_{v^{-1}}=D_{-v^{-1}}=\{(2,1),(-2,-1)\}.
\]
The four elements of \(\mu_6\setminus\{1,-1\}\) return exactly the six
norm-3 pairs. The actions \(1,-1\) return every pair. All source pairs are
nonzero, so distinct multipliers give distinct target pairs. The full actual
return histogram therefore is
\[
\#\{p:R_{\rm pair}(p)=2\}=6,\qquad
\#\{p:R_{\rm pair}(p)=4\}=4,\qquad
\#\{p:R_{\rm pair}(p)=6\}=6.
\]

**Meaning.** The seed has genuine scalar actions and complete finite
Cartesian accounting.

**Consequence.** No return multiplication, positive asymptotic \(\rho\), or
small bad-pair set follows from this table alone. Reusing the same commuting
scalar factors also does not make formal words distinct.

## 3. MS-A2 — application of the inherited fixed-field filter

### Statement

**Status: PROVED application of the inherited global ideal bound identified
in §1; affine-recursion hypotheses independently checked in this task.** Fix a totally real
number field \(K\subset\mathbb R\), a nonempty finite seed set
\(S\subset K\), and finitely many affine maps
\[
f_i(X)=a_iX+b_i\qquad(a_i,b_i\in K).
\]
All these choices are made before depth \(d\) grows. Let \(A_d\) be any
subset of the values obtained by applying words of length at most \(d\) to
\(S\). Then there is a function \(F(d)=\exp(o(d))\), depending only on
these fixed data, such that, uniformly in every real \(t\),
\[
\#\{(x,y)\in A_d^2:Q(x,y)=t\}\le F(d).
\tag{1}
\]
The statement counts every ordered pair. For \(t=0\), the fiber has size
at most one.

In particular, if the actual scalar count satisfies
\(\log|A_d|\ge ad-o(d)\) for some fixed \(a>0\), then
\[
\max_t\#Q^{-1}(t)\cap A_d^2=|A_d|^{o(1)},\qquad
|Q(A_d,A_d)|\ge |A_d|^{2-o(1)}.
\tag{2}
\]
Every selected family of genuine norm-one returns is bounded by the same
full-fiber bound. If identity is among the allowed actions, any well-defined
exponential return factor is therefore \(\rho=1\).

### Application check: denominators and all embeddings

Choose a fixed positive integer \(M\) such that \(Ms,Ma_i,Mb_i\) are
algebraic integers for every seed and every coefficient. The extra seed
factor is essential: in general the common multiplier is \(M^{d+1}\),
not \(M^d\). Induction gives
\[
M^{d+1}A_d\subset\mathcal O_K.
\tag{3}
\]
Indeed, for a word of length exactly \(r\), if
\(M^{r+1}x\) is integral, then
\[
M^{r+2}(a_i x+b_i)
=(Ma_i)(M^{r+1}x)+(Mb_i)M^{r+1}
\]
is integral. Values from shorter words remain integral after multiplication
by the remaining power of \(M\).

There are finitely many embeddings of the fixed field and finitely many
fixed coefficients. The affine recurrence therefore gives a fixed constant
\(C>1\) such that
\[
|\sigma(M^{d+1}x)|\le C^{d+1}
\qquad(x\in A_d,\ \sigma:K\hookrightarrow\mathbb R).
\tag{4}
\]
For example, first bound every embedded seed and coefficient by a fixed
constant, iterate \(|f_i(x)|\le C_0|x|+C_0\), and absorb \(M^{d+1}\).
This controls every conjugate, rather than just the designated real
embedding.

### Application of the inherited theorem

Put \(E=K(\omega)\), \(D=[E:\mathbb Q]\). For a nonempty positive
fiber, its scaled target \(q=M^{2d+2}t\) is integral, and (4) gives
\[
1\le |N_{E/\mathbb Q}(q)|\le\exp(C_1(d+1))
\tag{5}
\]
with a fixed constant. The inherited ideal bound, enlarged if necessary by
counting every ideal divisor of \((q)\), bounds the fiber by
\(C_E\tau(|N_{E/\mathbb Q}(q)|)^D\). HR-4B makes this
\(\exp(o(d))\), uniformly in \(q\). Negative targets have no pairs, and
positive definiteness gives only \((0,0)\) at target zero. This proves the
stated application. Under the positive exponential input lower bound, (4)
is polynomial house in the actual input size, exactly matching the frozen
fixed-field theorem's scope.

The assumptions check confirms that the ideal bound does not require
principal ideals to be uniquely factored as elements or a trivial class
group. The finite constant \(C_E\) counts integral relative-norm-one units;
it is uniform only because the field is fixed. No new unit, ideal, or
variable-field theorem is claimed here.

### Meaning and consequence

This filter allows arbitrary coordinate overlap and parameter collisions.
It bounds the actual full fibers, so no choice or number of norm-one action
labels can evade it. If \(n_d=|A_d|=\lambda^{d+o(d)}\), \(\lambda>1\),
then \(\rho=1\). For every fixed \(\varepsilon>0\), eventually **all**
\(n_d^2\) pairs have fewer than \(n_d^\varepsilon\) genuine returns.
Thus the bad-pair exponent is 2 and the proposed positive-return gate fails.

The conclusion is **scoped**. It does not apply to fields whose degree grows
with depth, arbitrary real/transcendental coefficients, depth-dependent map
lists, or constructions lacking the stated uniform exponential denominator
and conjugate-height control. Without an actual positive exponential input
lower bound, (1) alone does not imply an \(n^{o(1)}\) bound. Nothing here
rules out all multiscale constructions or all fixed-polynomial compression.

## 4. Fully charged preselection ledger

| Gain or cost | Accounted bound and consequence |
|---|---|
| Input counts | If there are \(r\) maps and \(s\) seeds, \(\lvert A_d\rvert\le s\sum_{j=0}^d r^j\). A positive exponential **actual-value** lower bound is a separate hypothesis; formal words do not supply it. |
| Thinning in both coordinates | Arbitrary subsets are allowed in (1). Any thinning must be reflected in the actual \(n_d\); no saving is credited from omitted pairs. |
| Parameter/projection fibers | No injectivity is assumed for the recursion. All bounds use actual real values. The map \((X,Y)\mapsto X-\omega Y\) is exactly injective. |
| Same set and full coverage | Both coordinates lie in the same \(A_d\), and the bound covers all ordered pairs, all targets, and every genuine action family. |
| Denominators | A single factor \(M^{d+1}\) clears every input. Norm targets scale by \(M^{2d+2}\). This changes no fiber cardinality. |
| Field degree/discriminant | \(K,E\) are fixed before depth. Their degree and discriminant may enter fixed constants. No estimate uniform in variable fields is asserted. |
| Local moduli/splitting | No sieve or favorable splitting restriction is used. The inherited ideal bound covers all rational primes, including ramification. |
| Units/regulator/class group | Integral relative-norm-one units contribute the inherited fixed constant \(C_E\). Counting all ideal divisors does not require a trivial class group. No variable-field estimate is suppressed. |
| Heights/archimedean distortion | Every conjugate has height \(\exp(O(d))\); hence the rational norm in (5) is \(\exp(O(d))\). Fixed distortion constants are explicit dependencies. |
| Branches/states/carries | Branch multiplicity is charged through actual input counts. Adding labels to the same scalar value gives no input or return gain. No carry certificate is assumed. |
| Exceptions | No positive-norm exceptions. The zero fiber has at most one pair and only one distinct target. |
| Input rate | When supplied, \(a=B=\log\lambda>0\), for \(n_d=\lambda^{d+o(d)}\). |
| Return rate | \(\log R_{\rm pair}=o(d)\), and therefore \(\rho=1\) when identity is available. |
| Actual image | \(n_d^{2-o(1)}\le\lvert Q(A_d,A_d)\rvert\le n_d^2\); the output has exponential rate \(2\log\lambda\). |
| Net asymptotic gate | No positive gap: \(\delta=2a-2a=0\). This is an actual-image obstruction for the stated fixed-field class, not merely failure of an upper certificate. |

## 5. Audit record and remaining boundary

Corrections made before acceptance: the seed denominator uses
\(M^{d+1}\); the existing T03 global ideal bound is recognized as the
controlling frozen theorem, rather than repackaged as a new obstruction;
HR-4B supplies only the divisor estimate; and the input-growth assumption
refers to distinct scalar values. No historical
file was changed. Agent D's mathematical computation use is zero evaluations
and zero research-program CPU seconds.

The finite seed table is accepted. The fixed-field affine route is rejected
at preselection whenever its actual input growth is exponential. The selected
recursive constructions require their own whole-scalar identities and full
Cartesian accounting; this filter cannot substitute for those audits.

## 6. Audit of the written local-gadget companion

The complete `local-gadgets.md` was subsequently inspected. Claims MP-L1,
MP-L2, and MP-L3 pass the independent symbolic audit, including their
finite tables and statistics. In MP-L2,
\[
A=\{0,\pm1,\pm2,\pm3,\pm\sqrt3,\pm2\sqrt3\},\quad U=\mu_{12}.
\]
The 48 nonzero mixed rational/irrational pairs have only the two sign
returns. The rational and irrational components contribute respectively
six and six pairs at each of norms 3 and 9, and two and six pairs at norm
12. The odd phase \((2+\omega)/\sqrt3\) links these pieces. Hence the
return counts on those shells are 12, 12, and 8. Rational norms 1, 4,
and 7 contribute 24 sources with six returns. The remaining 16
same-component pairs have two returns. With the origin, this proves
\[
H=\{1:1,\ 2:64,\ 6:24,\ 8:8,\ 12:24\}.
\]
The twelve rational norm values and twelve distinct irrational mixed norm
values in that companion also give exactly 24 full-image values locally.
These counts are finite facts, not an asymptotic conclusion.

For MP-L3 the identity
\[
\left(\prod_{\ell=a}^{b-1}2\cos(2^\ell\theta)\right)
\sin(2^a\theta)=\sin(2^b\theta)
\]
is exact. Both coordinate projections of
\(\sqrt3c\mu_m\) equal \(cS_m\), with
\(S_m=\{-2\sin(2\pi r/m)\}\). The action is one global complex
multiplication on the whole scalar \(x-\omega y\); independent local
rotations are not being composed. The actual size bounds in §7 below
charge all address and coordinate collisions. This is genuine coordinate
reuse in the growing field, so the independent-radial-tag obstruction is
not silently applied to it.

## 7. MS-A3 — audit of the cosine-product parity obstruction

**Status: PROVED scoped obstruction, independently checked in this task.**
For \(d\ge1\), put
\[
m=6\cdot2^d,\quad \zeta=e^{2\pi i/m},\quad
\gamma_\ell=\zeta^{2^\ell}+\zeta^{-2^\ell},\quad
A=\bigcup_{J\subseteq\{0,\ldots,d-1\}}
\left(\prod_{\ell\in J}\gamma_\ell\right)S_m,
\quad U=\mu_m.
\]
Let \(K=\mathbb Q(\zeta+\zeta^{-1})\). The automorphism
\(\sigma:\zeta\mapsto-\zeta\) is a well-defined involution fixing
\(\omega\). It preserves \(K\); write \(F=K^\sigma\).
The element \(\gamma_0\) is nonzero and \(\sigma\)-odd, while every
\(\gamma_\ell\), \(\ell\ge1\), is fixed. Thus \(K/F\) is quadratic.

Every element of \(S_m\) is a pure eigenvector of \(\sigma\). At
\(d=1\), \(\sigma(i)=-i\), which reverses the parity assigned to the
sine index but does not change purity; for \(d\ge2\), \(\sigma(i)=i\).
Consequently every nonzero carrier value lies in one of the two lines
\(F\) and \(\gamma_0F\).

For \(u=\zeta^k=a+b\omega\), conjugating the unique real-coefficient
decomposition shows that \(a,b,a-b\) all have the same parity
\((-1)^k\). If nonzero \(x,y\) have opposite parities, the two summands
of \(ax+by\) have opposite parities unless one vanishes. Since every
target coordinate must be pure, the first output requires \(ab=0\).
The second output \(-bx+(a-b)y\) likewise requires
\(b(a-b)=0\). These requirements force \(b=0\), and the real norm-one
condition then gives \(u=\pm1\). Both signs do return, so such a source
has exactly two selected returned pairs.

This argument counts actual scalar values. Define \(B\) by omitting
the factor \(\gamma_0\) from the product addresses, so
\(A=B\cup\gamma_0B\). Let \(b_+,b_-\) be the two nonzero parity
populations of \(B\), and let \(a_+,a_-\) be those of \(A\). Since
nonzero scaling is injective and multiplication by \(\gamma_0\) swaps
parities,
\[
\max(b_+,b_-)\le a_+,a_-\le b_++b_-.
\]
Hence \(a_+/a_-\in[1/2,2]\). Writing \(n=|A|=1+a_++a_-\),
\[
\#\{(x,y)\in A^2:R_{\rm pair}(x,y)=2\}
\ge2a_+a_-\ge\frac49(n-1)^2.
\tag{6}
\]
No address injectivity, radius independence, or numerical equality test
is used. The origin has one returned pair.

**Meaning.** Actual coordinate reuse is present, but a fixed positive
fraction of the completed Cartesian square still has only sign returns.

**Consequence.** For these selected actions no fixed positive return-tail
exponents exist. This proof does not bound fibers under all possible
norm-one multipliers and does not establish an actual-image lower bound.

## 8. MS-A4 — audit of the mixed-amplitude four-line obstruction

**Status: PROVED scoped obstruction, independently checked in this task.**
The one selected follow-up variant uses
\[
\widetilde A=
\bigcup_{J\subseteq\{0,\ldots,d-1\}}
\left(\prod_{\ell\in J}(1+\gamma_\ell)\right)S_m,
\qquad U=\mu_m.
\]
The field, involution, and action parity are those of §7. Put
\(\gamma=\gamma_0\), and let \(B\) use only indices \(\ell\ge1\).
Then \(B\subset F\cup\gamma F\) and
\(\widetilde A=B\cup(1+\gamma)B\). Its nonzero values lie on the four
distinct \(F\)-lines
\[
F,\qquad \gamma F,\qquad(1+\gamma)F,\qquad(1+\gamma)\gamma F.
\tag{7}
\]
Here \(\gamma^2\in F\), \(\gamma\notin F\), and
\(\gamma=2\cos(2\pi/m)\ge\sqrt3\). In particular
\(\gamma^2\ne1\), which is needed to distinguish the last two lines.
Different lines intersect only at zero. Thus, if the two nonzero
populations of \(B\) are \(b_+,b_-\), the four populations in (7) are
exactly \(b_+,b_-,b_+,b_-\), including empty lines if one population
vanishes. Put \(s=|\widetilde A|-1=2(b_++b_-)\). The largest line
population is at most \(s/2\), so at least
\[
s^2-\sum_{j=1}^4m_j^2\ge s^2/2
\tag{8}
\]
ordered sources have \(F\)-independent coordinates.

For completeness, the target-line return bound has the following exact
scope. Suppose \(K/F\) is a real quadratic extension and a carrier lies
in \(k\) one-dimensional \(F\)-lines. Allow only norm-one actions with
both real coefficients in \(F\), or both in \(\gamma F\). For an
\(F\)-independent source \((x,y)\), the map
\((a,b)\mapsto ax+by\) is an \(F\)-linear isomorphism from
\(F^2\) to \(K\). The same is true on the odd coefficient space after
factoring out \(\gamma\). For each target first-coordinate line and
each coefficient parity, its inverse image is one coefficient line.
The positive-definite equation
\(a^2-ab+b^2=1\) meets that real line in at most two points.
The target first coordinate cannot be zero, because that would force
both coefficients to be zero. Therefore at most \(4k\) actions can
return, even before requiring membership of the second coordinate.
Distinct actions give distinct targets for these nonzero sources.

Applying this with \(k=4\), (8) gives
\[
\#\{p\in\widetilde A^2:R_{\rm pair}(p)\le16\}
\ge\tfrac12(|\widetilde A|-1)^2.
\tag{9}
\]

**Meaning.** Mixing the two eigenspaces removes the pure-parity condition
of the first carrier, but leaves bounded width over the fixed subfield
at each depth.

**Consequence.** The selected \(\mu_m\) action still fails the positive
return-tail requirement. General actions with coefficients outside the
two indicated parity spaces, arbitrary carriers in the growing field,
and actual full-image lower bounds are outside this proof.

## 9. Final charged gate for the two selected architectures

Both carriers contain \(S_m\), and each is a union of \(2^d\) scaled
copies sharing zero. Thus the exact collision-tolerant bounds are
\[
3\cdot2^d+1\le n_d\le3\cdot4^d+1.
\]
They use the same scalar set in both coordinates, with no thinning. The
whole-scalar norm identity is exact. Scalar address fibers can be large;
they have already been charged by using actual unions throughout.

| Quantity | Audit conclusion for the selected carriers |
|---|---|
| Actual input factor | An exact \(\lambda\) is not proved. If it exists, \(2\le\lambda\le4\). The displayed bounds alone are sufficient to make \(n_d\to\infty\). |
| Actual action inventory | Exactly \(m=6\cdot2^d\) distinct multipliers. At nonzero sources, action-to-target is injective; the origin has one distinct target. |
| Whole-scalar preservation | Multiplication by each \(u\in\mu_m\) preserves \(Q\) exactly, including all scalar cross terms. No independent per-level action product is credited. |
| Return factor on the obstructing population | At least \(4(n-1)^2/9\) sources have exactly 2 returns in the first carrier; at least \((n-1)^2/2\) have at most 16 in the variant. Their exponential return factor is 1. No single uniform \(\rho\) for every source is claimed. |
| Bad-pair exponent | For every fixed \(\varepsilon>0\), eventually the relevant displayed population lies below \(n^\varepsilon\). It has exponent 2, so no \(\delta>0\) is possible for these selected-action certificates. |
| Field degree | The real field has degree \(2^d\), and \(\mathbb Q(\zeta)\) has degree \(2^{d+1}\). This is a growing field; the inherited fixed-field filter is inapplicable. |
| Denominators/heights | Inputs are algebraic integers. Their conjugate absolute values are at most \(2^{d+1}\) for pure products and \(2\cdot3^d\) for mixed products. Action coefficients can be written in \((1/3)\mathcal O_K\); exact membership is used, not a free denominator-lattice population estimate. |
| Discriminant/regulator/local splitting | No volume, unit counting, or sieve argument is used in these obstruction proofs. No favorable cost is assigned to these growing arithmetic quantities. |
| Branches and projection | The parity argument uses actual union cardinalities; the mixed argument uses four distinct subfield lines with exact nonzero branch populations. All projection collisions are allowed. |
| Origin and unmatched pairs | The origin is one pair with one target. Equations (6) and (9) concern nonzero sources and already give quadratic-size bad populations; there is no uncharged exceptional tail or rectangular transport. |
| Actual image / power-saving conclusion | The full-image asymptotics of these growing carriers remain OPEN. The selected return route is FAILED. No \(c>0\) follows, and the failure of that route is not promoted to an actual-image obstruction. |

The cycle's two selected architectures therefore fail their genuine
return-tail gate before any new computation. No third candidate or further
mutation is audited or proposed here. This final audit remains strictly
symbolic: zero mathematical program evaluations, zero research-program CPU
seconds, and no network use.

### Final-file transcription check

The written first-carrier proof, main report, and ledger were inspected in
addition to the earlier proof messages. One orbit-decoding transcription
error was identified and sent to the author: with
\(s_r=-2\sin(r\theta)\) and \(\phi(x,y)=x-\omega y\), the exact formula is
\[
\sqrt3\zeta^r=s_{r-m/3}-\omega s_r,
\qquad s_{r-m/3}=\sqrt3\cos(r\theta)+\sin(r\theta).
\]
The initially written shift \(m/6\) and minus sign were incorrect.
The correction preserves the equal-projection statement, all input counts,
and both return obstructions. The local-gadget companion already had the
correct plus-sine formula. This check is separate from any repository or
source-hash validation performed by the lead.

The author then saved the corrected decoding in all three locations and
completed MS-C2 in `composition.md`, §5. A bounded final-file mathematical
audit passed: its addition identity, finite-line lemma, four-line counts,
and the stronger variant lower bound \(6\cdot2^d+1\) were checked, along
with all scope and rate qualifications. The common weaker lower bound in
§9 remains valid. Two unescaped table delimiters were reported as a
formatting correction; they affect no mathematics. No unresolved
mathematical gap was found in either of the two scoped obstruction proofs.
