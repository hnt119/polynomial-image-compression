# Shared-scale dyadic compositions and their return tails

30 September 2026 · version 1 · T03 · fixed real polynomial
\(Q(x,y)=x^2+xy+y^2=N(x-\omega y)\), where
\(\omega=e^{2\pi i/3}\).

## 1. Identity, authority, and evidence

This is the new, explicitly commissioned **offline multiscale/fractal
packing** cycle. Its authority is the user attachment
`[private commissioning attachment; locator withheld]`.
The author, Agent B, performed symbolic derivation and local source inspection
only: **zero mathematical program evaluations, zero experiments, no network**.
The lead controls the shared finite budget. This file is the author's only
new research file in this cycle; previous carriers and proofs are unchanged.

Source history and dependencies:

- `../2026-09-30-modular-lift/proofs.md`, ML-4, §§4–6, gives the frozen
  paired orbit lift and its particular independent-radius obstruction.
  Its §8, ML-O1, asks for amplitudes in the common cyclotomic field and a
  genuine full-Cartesian return tail. The constructions below use related
  amplitudes in that common field; they do not reuse the independent tags.
- `../2026-09-21-dense-cartesianization/block-rectangle.md`, DC-R1, §4,
  is the retained implication from an almost-everywhere genuine-return
  lower bound to an image upper bound. No new proof of that implication
  is claimed here.
- `../2026-09-21-dc-o1/tensor-compatibility.md`, DC-T1–DC-T3, concerns
  independent local rotations and scalar cross terms. Here all actions
  are one **whole-scalar** multiplication; no independent local rotations
  or local-return products are asserted.
- `local-only/migration/sources/T03_CURRENT_STATE.md`, §10, supplies the
  accepted elementary field/cyclotomic background. No new outside theorem,
  literature search, or external novelty claim is added.
- `research/templates/CONSTRUCTION_LEDGER.md` supplies the ledger categories
  in §6. All paths above are repository-relative except the private
  authorization attachment.

The new claims below are complete internally derived proofs. The lead and
Agent D independently inspected the MS-C1 parity argument before the note
was written. A final-file independent audit is recorded separately in
`audit.md`; this sentence does not substitute for that audit.

| Claim | Status and scope | Locator |
|---|---|---|
| MS-C1 | PROVED: explicit shared-scale cosine-product carrier, exact whole-scalar actions, and a quadratic population with exactly two selected returns, for every integer depth d≥1 | §§2–4 |
| MS-C2 | PROVED: the one approved mixed-amplitude variant has a quadratic population with at most sixteen selected returns, for every integer depth d≥1; includes a general finite-line lemma | §5 |

Both constructions' **DC-R1 return-tail certificates are FAILED** under
their stated full selected group. Their complete real Q-images are not
determined by these obstructions. The general T03 target remains OPEN.

## 2. MS-C1 — exact recursive carrier

### Statement

For every integer \(d\ge1\), fix, in this order,

\[
m_d=6\cdot2^d,\qquad \theta_d=2\pi/m_d,\qquad
\zeta_d=e^{i\theta_d},\qquad U_d=\mu_{m_d}=\{\zeta_d^k:0\le k<m_d\}.
\tag{1}
\]

Put \(K_d=\mathbb Q(\zeta_d)\cap\mathbb R\), and define

\[
s_r=-2\sin(r\theta_d),\qquad
S_d=\{s_r:0\le r<m_d\},\qquad
\gamma_\ell=2\cos(2^\ell\theta_d)\quad(0\le\ell<d).
\tag{2}
\]

The depth d is understood in each \(\gamma_\ell\). Define

\[
c_J=\prod_{\ell\in J}\gamma_\ell,\qquad
A_d=\bigcup_{J\subseteq\{0,\ldots,d-1\}}c_JS_d,\qquad n_d=|A_d|.
\tag{3}
\]

These are actual real sets; repeated labels are identified. Equivalently,
start with \(C_{d,0}=S_d\) and successively set

\[
C_{d,L+1}=C_{d,L}\cup\gamma_L C_{d,L}\quad(0\le L<d),
\qquad A_d=C_{d,d}.
\tag{4}
\]

The ambient angle also refines with d: \(\zeta_d^2=\zeta_{d-1}\).
Consequently \(S_{d-1}\subseteq S_d\) and
\(\gamma_{d,\ell+1}=\gamma_{d-1,\ell}\); in particular
\(A_{d-1}\subseteq A_d\) for \(d\ge2\). Formula (4), not a claim
that every angular core stays fixed as d changes, is the precise branching
recurrence.

The same set is used in both coordinates. The actual selected return count
is

\[
R_d(x,y)=\#\{M_u(x,y)\in A_d^2:u\in U_d\},
\quad
M_{a+b\omega}(x,y)=(ax+by,-bx+(a-b)y).
\tag{5}
\]

Multipliers are actual distinct complex numbers. At a nonzero source
distinct multipliers give distinct returned pairs; at the origin the
count is one.

### Exact coordinate reuse and global composition

All factors in (3) are positive: their arguments lie in \((0,\pi/6]\),
so \(\sqrt3\le\gamma_\ell<2\). The trigonometric identity
\(2\cos t\sin t=\sin(2t)\) gives, whenever \(0\le a<b\le d\),

\[
\left(\prod_{\ell=a}^{b-1}\gamma_\ell\right)
\sin(2^a\theta_d)=\sin(2^b\theta_d).
\tag{6}
\]

Thus different amplitude/core labels give exactly the same scalar
coordinates. For example \(c_{\{0,\ldots,b-1\}}s_1=s_{2^b}\).
This is an explicit source of coordinate reuse, not independent radial
tags or numerical coincidence.

The complex orbit \(\sqrt3\mu_{m_d}\) decodes as

\[
\sqrt3\zeta_d^r=x_r-\omega y_r,
\qquad (x_r,y_r)=(s_{r-m_d/3},s_r),\qquad Q(x_r,y_r)=3.
\tag{7}
\]

Indeed \(y_r=-2\sin(r\theta_d)\) and
\(x_r=\sqrt3\cos(r\theta_d)+\sin(r\theta_d)\).
Both coordinate projections of this orbit are exactly \(S_d\).
Every selected amplitude orbit \(c_J\sqrt3\mu_{m_d}\) therefore
has all its coordinates in \(A_d\), with exactly \(m_d\) distinct
returns at each of its points. Even if amplitudes coincide, each
individual nonzero orbit has that many targets.

For all scalar pairs, \(M_u\) preserves Q because multiplication by
\(u\in U_d\) preserves complex norm. The exact action composition is
\(M_uM_v=M_{uv}\). There are only \(m_d\) possible global actions;
formal choices made independently at different levels do not provide
additional distinct multipliers.

### Input bounds

Because \(4\mid m_d\), the sine involution
\(r\mapsto m_d/2-r\) has exactly two fixed residues. All other sine
values have two preimages, so

\[
|S_d|=m_d/2+1=3\cdot2^d+1.
\tag{8}
\]

The empty amplitude set gives the lower bound, while every amplitude
copy has \(m_d/2\) nonzero scalars. Hence

\[
3\cdot2^d+1\le n_d\le 1+2^d(m_d/2)=3\cdot4^d+1.
\tag{9}
\]

No amplitude or projection injectivity is assumed. These are rigorous
lower and upper **distinct-input** counts. An exact asymptotic
\(n_d=\lambda^{d+o(d)}\) is not proved. If that rate exists, (9)
puts \(2\le\lambda\le4\).

## 3. A quadratic extension separates two actual scalar populations

Let \(\sigma\) be the cyclotomic automorphism
\(\sigma(\zeta_d)=-\zeta_d\). It exists because
\(m_d/2+1=3\cdot2^d+1\) is coprime to \(m_d\); it is an
involution. It preserves \(K_d\) and fixes
\(\omega=\zeta_d^{m_d/3}\), since \(m_d/3=2^{d+1}\) is even.
Write

\[
F_d=\{x\in K_d:\sigma(x)=x\},\qquad \gamma=\gamma_0.
\tag{10}
\]

Then \(\sigma(\gamma)=-\gamma\), \(\gamma\ne0\), and
\(K_d=F_d\oplus\gamma F_d\). To justify the latter directly,
every x decomposes as
\((x+\sigma x)/2+(x-\sigma x)/2\), and the second summand divided
by \(\gamma\) is fixed. The two summands intersect only at zero.
In particular \(\gamma^2\in F_d\).

For \(\ell\ge1\), \(\sigma(\gamma_\ell)=\gamma_\ell\).
Every \(s_r\) is also an eigenvector of \(\sigma\). More precisely,
write \(i=\zeta_d^{m_d/4}\) and
\(s_r=i(\zeta_d^r-\zeta_d^{-r})\). For \(d\ge2\), i is fixed
and \(\sigma(s_r)=(-1)^rs_r\). At \(d=1\), \(\sigma(i)=-i\),
so \(\sigma(s_r)=(-1)^{r+1}s_r\). This harmless offset must be
retained in the base case.

It follows that every nonzero scalar of \(A_d\) lies in exactly one
of \(F_d\) and \(\gamma F_d\). Define its two populations
\(A_+\) and \(A_-\) according to these signs, and let their sizes
be \(a_+,a_-\). Delete the first amplitude factor and write

\[
B_d=\bigcup_{J\subseteq\{1,\ldots,d-1\}}c_JS_d,
\qquad A_d=B_d\cup\gamma B_d.
\tag{11}
\]

Let \(b_+,b_-\) be the two nonzero population sizes of \(B_d\).
Multiplication by nonzero \(\gamma\) is injective and exchanges
the two signs. Actual set union, with all duplicate values removed,
therefore yields

\[
\max(b_+,b_-)\le a_+,a_-\le b_++b_-.
\tag{12}
\]

Both populations are nonempty, and their ratio lies between 1/2 and 2.
Since \(a_++a_-=n_d-1\), elementary minimization of
\(2t/(1+t)^2\) on \([1/2,2]\) gives

\[
2a_+a_-\ge\frac49(n_d-1)^2.
\tag{13}
\]

This is a count of distinct scalar pairs, independent of label fibers.

## 4. MS-C1 — exact low-return population

### Statement

Every ordered pair in
\((A_+\times A_-)\cup(A_-\times A_+)\) has exactly two distinct
returns under the **entire** selected group \(U_d\). Consequently,
for every fixed \(\varepsilon>0\) and all sufficiently large d,

\[
B_{\varepsilon,d}:=\#\{(x,y)\in A_d^2:R_d(x,y)<n_d^\varepsilon\}
\ \ge\ \frac49(n_d-1)^2.
\tag{14}
\]

### Proof

Write \(u=\zeta_d^k=a+b\omega\) with unique real \(a,b\in K_d\).
The uniqueness follows from \(\omega\notin\mathbb R\). Since
\(\sigma(u)=(-1)^ku\) and \(\sigma(\omega)=\omega\), both a and b,
and also \(a-b\), have the same eigenvalue \((-1)^k\).

Take nonzero x,y of opposite signs. The two summands in
\(ax+by\) have opposite signs whenever both are nonzero. Such a sum
lies in neither eigenspace and cannot be in \(A_d\). Thus a return
requires \(ab=0\). The second coordinate
\(-bx+(a-b)y\) similarly requires \(b(a-b)=0\). If \(b\ne0\),
these equations force \(a=0\) and \(a-b=0\), a contradiction.
Thus \(b=0\). Norm one then gives \(a=\pm1\).

Both signs do return, since \(A_d=-A_d\), and they give distinct
targets at the nonzero source. Hence the return count is exactly two.
Equation (13) proves (14), because (9) makes \(n_d^\varepsilon>2\)
eventually. \(\square\)

### Meaning

The amplitude relations (6) create real scalar reuse, yet they preserve
a two-class field symmetry. The obstruction tests the entire growing
action group on a positive proportion of the actual Cartesian square;
it is stronger than merely counting the sparse engineered orbit points.
No independent-tag or quadratic-faithful digit assumption is used.

### Consequence and limits

There is no fixed \(\delta>0\) for which this bad population is
\(O(n_d^{2-\delta})\). No return lower bound
\(\rho^{d+o(d)}\) with \(\rho>1\) can hold outside a power-saving
exceptional set, while (9) gives positive exponential input growth.
This does not assert that an asymptotic return rate exists for almost
all pairs. Thus this family does not supply the requested DC-R1 hypothesis.

This is **not** a lower bound for \(|Q(A_d,A_d)|\): arbitrary further
norm-one multipliers can have coefficients of mixed conjugation type
and are not excluded. The high-return behavior of other carriers and
the general real power-saving problem remain OPEN. The sign closure
also means the identity-only set is exactly \(\{(0,0)\}\); this does
not rescue the return tail.

## 5. MS-C2 — one mixed-amplitude follow-up

This is the lead-approved **second and final analyzed definition**, a
single related mutation of MS-C1. No further family or mutation is
introduced. It changes the amplitude factors, retains the whole-scalar
action group, and deliberately mixes the first conjugation eigenspaces.

### Statement and exact construction

Retain (1), (2), and the same \(K_d,F_d,\sigma,\gamma=\gamma_0\).
For every \(d\ge1\), set

\[
\widetilde c_J=\prod_{\ell\in J}(1+\gamma_\ell),\qquad
\widetilde A_d=\bigcup_{J\subseteq\{0,\ldots,d-1\}}
\widetilde c_JS_d,\qquad \widetilde n_d=|\widetilde A_d|.
\tag{15}
\]

At each level the exact set recurrence is
\(\widetilde C_{d,L+1}=\widetilde C_{d,L}\cup
(1+\gamma_L)\widetilde C_{d,L}\), starting with \(S_d\).
As before, the angle refines between depths. The algebraic relation

\[
(1+\gamma_\ell)s_r=s_r+s_{r+2^\ell}+s_{r-2^\ell}
\tag{16}
\]

follows from the sine addition formula. Also
\(\widetilde c_J=\sum_{I\subseteq J}c_I\). Thus this is an explicit
common-field amplitude mixture, designed to break the eigenvector purity
used in MS-C1. Formula (16) is an exact scalar identity; it does not
assert that all sum labels give the same existing coordinate, that
amplitude copies overlap, or that local return counts multiply.

Each orbit \(\widetilde c_J\sqrt3\mu_{m_d}\) still decodes by (7)
and has \(m_d\) genuine returns inside \(\widetilde A_d^2\).
The full selected return count uses precisely \(U_d\) on the entire
same-set square, with distinct returned pairs as in (5).

For every fixed \(\varepsilon>0\), all sufficiently large d satisfy

\[
\#\{p\in\widetilde A_d^2:R_d(p)<\widetilde n_d^\varepsilon\}
\ \ge\ \frac12(\widetilde n_d-1)^2.
\tag{17}
\]

Here \(R_d\) is computed in \(\widetilde A_d^2\), not the first
carrier. The proof gives a uniform upper bound of sixteen selected
returns on that many pairs, not just an average bound.

### Finite-line return lemma

Let \(F\subset K\subset\mathbb R\) be fields with
\(K=F\oplus tF\), \(t\ne0\), and \(t^2\in F\). Let
\(A\subset K\) be a finite set contained in a union of k distinct
one-dimensional F-linear subspaces \(L_1,\ldots,L_k\) of K.
Let U be any family of norm-one multipliers \(u=a+b\omega\) such
that, for every u, either \((a,b)\in F^2\) or
\((a,b)\in(tF)^2\). Then, for every pair x,y linearly independent
over F,

\[
\#\{M_u(x,y)\in A^2:u\in U\}\le4k.
\tag{18}
\]

U need not be a group or finite; the count of returning targets is
bounded by the same argument.

**Proof.** First take \((a,b)\in F^2\). The map
\((a,b)\mapsto ax+by\) is an F-linear isomorphism from \(F^2\)
to K, because x,y form an F-basis. The inverse image of each
\(L_j\) is a one-dimensional F-line. Choose a nonzero generating
vector \((a_0,b_0)\) for that line. Every candidate action on it
has \((a,b)=q(a_0,b_0)\) for some \(q\in F\), and its norm-one
equation is

\[
q^2(a_0^2-a_0b_0+b_0^2)=1.
\tag{19}
\]

The coefficient in parentheses is strictly positive in the given real
embedding. Hence there are at most two real solutions q, and at most
two that belong to F. This gives at most \(2k\) even actions.
The first output coordinate cannot be zero, since injectivity would
force \(a=b=0\), contradicting norm one.

For \((a,b)=(t a_0,t b_0)\), with \(a_0,b_0\in F\), the map
\((a_0,b_0)\mapsto t(a_0x+b_0y)\) is again an F-linear
isomorphism. Each target line again leaves one F-line of coefficients,
and the norm equation has the additional strictly positive factor
\(t^2\). It still has at most two real solutions. There are thus
at most \(2k\) odd actions as well. The second-coordinate condition
only removes candidates. Each nonzero source has a free complex
multiplication action, so counting possible actions bounds distinct
targets. This proves (18). \(\square\)

### The four actual scalar lines and their populations

Write

\[
\widetilde B_d=\bigcup_{J\subseteq\{1,\ldots,d-1\}}
\widetilde c_JS_d,
\qquad
\widetilde A_d=\widetilde B_d\cup(1+\gamma)\widetilde B_d.
\tag{20}
\]

All factors used in \(\widetilde B_d\) belong to \(F_d\), while
each core scalar is in \(F_d\) or \(\gamma F_d\). Consequently
the nonzero scalars of \(\widetilde A_d\) occupy the four
distinct F-lines

\[
F_d,\quad \gamma F_d,\quad (1+\gamma)F_d,
\quad (1+\gamma)\gamma F_d.
\tag{21}
\]

For completeness, use the basis \(1,\gamma\) and write
\(q=\gamma^2\in F_d\). The four displayed lines are generated by
\((1,0),(0,1),(1,1),(q,1)\). Here \(q\ge3\) in the given
embedding, so \(q\ne0,1\); they are indeed distinct. The two core
parities occur already in \(S_d\), and all amplitude factors are
nonzero, so each line has a nonzero population.

Let \(b_+,b_-\) be the nonzero population sizes of
\(\widetilde B_d\) in its first two lines. Multiplication by
\(1+\gamma\ne0\) is injective. Because all four lines in (21)
are distinct, the four actual nonzero populations have sizes exactly

\[
b_+,\ b_-,\ b_+,\ b_-,\qquad
\widetilde n_d-1=2(b_++b_-).
\tag{22}
\]

Thus no single line contains more than
\((\widetilde n_d-1)/2\) scalars. Among ordered pairs of nonzero
scalars, linear dependence over \(F_d\) occurs exactly when both
coordinates lie on the same one of these four lines. Therefore at
least

\[
(\widetilde n_d-1)^2-2(b_+^2+b_-^2)
\ \ge\ \frac12(\widetilde n_d-1)^2
\tag{23}
\]

ordered pairs have independent coordinates over \(F_d\).

Every \(u\in U_d\) has coefficients a,b of the same conjugation
parity, as proved in §4. They therefore lie together in \(F_d\) or
in \(\gamma F_d\). Apply (18) with k=4 to every pair counted in
(23). It has at most sixteen returns. Since the core alone grows
exponentially, \(\widetilde n_d^\varepsilon>16\) eventually;
this proves (17).

### Size, arithmetic, meaning, and consequence

The copies in (20) are disjoint away from zero, so their sizes obey
an exact top-level count:

\[
\widetilde n_d=1+2(|\widetilde B_d|-1),\qquad
6\cdot2^d+1\le\widetilde n_d\le3\cdot4^d+1.
\tag{24}
\]

The lower bound uses \(S_d\subseteq\widetilde B_d\) and (8);
the upper bound again counts at most \(2^d\) amplitude copies.
No exact input exponent \(\lambda\) is established. Its lower and
upper exponential rates remain \(\log2\) and \(\log4\).

All inputs are algebraic integers in the same real field \(K_d\)
of degree \(2^d\). Every conjugate of \(1+\gamma_\ell\) has
absolute value at most 3, so every input conjugate has absolute value
at most \(2\cdot3^d\). Action denominators, the angular group size,
zero stabilizer accounting, and whole-scalar norm identity are unchanged
from MS-C1. There is no modular-density, regulator, discriminant, or
independent-radius saving in this proof.

**Meaning.** Mixing the two eigenspaces by \(1+\gamma\) breaks the
purity used in §4, but leaves only four possible F-lines for a scalar.
A source using two independent lines leaves at most two norm-one
choices for each first-coordinate target line and action parity. The
second coordinate cannot increase that number.

**Consequence.** Equation (17) excludes every near-full return lower
bound \(\rho^{d+o(d)}\) with \(\rho>1\), and therefore excludes
the requested DC-R1 certificate for this second definition as well.
It makes no assertion that the typical return count has an asymptotic
rate, and supplies no lower bound for the complete real Q-image.
Even arbitrary additional actions with pure coefficient parity satisfy
(18); arbitrary actions with mixed coefficients are outside its scope.

## 6. Exact arithmetic and rate ledger

| Gain/cost | Rigorous accounting | Status |
|---|---|---|
| Inputs before word identifications | 2^d amplitude labels and m_d angular labels; repeated sine values and amplitudes are identified | Definition; no label count used as input lower bound |
| Actual input count | 3·2^d+1 ≤ n_d ≤ 3·4^d+1 | PROVED (9) |
| Input thinning, both coordinates | None: the set in (3) is used in the entire ordered square | Zero by definition, not discarded exceptions |
| Projection/parameter fibers | Base sine fibers are 1 or 2; amplitude/coordinate fibers are not bounded. (9), (12), and (13) already count actual values | No unproved injectivity or second thinning |
| Real same-set projection | Each orbit has pair coordinates (c_J s_(r−m/3), c_J s_r); both projections equal c_JS_d | PROVED (7) |
| Encoded pair coverage | At most m_d 2^d=6·4^d encoded pairs; overlaps can reduce this. No all-square coverage follows | Upper count only |
| Global actions and distinctness | card(U_d)=m_d=6·2^d; nonzero action is free; origin has one target | Exact |
| Local splitting/moduli/residue populations | No modular population is invoked. m_d is an angular order, not a residue-support saving | Inapplicable to this direct real model |
| Field degree | [Q(ζ_d):Q]=2^(d+1), [K_d:Q]=2^d, [K_d:F_d]=2 | Growing degree is explicit; not a fixed-field argument |
| Discriminant and regulator | No bound or saving involving either is invoked; their values are not evaluated here | Uncharged quantities cannot support a positive certificate; rejection is independent of them |
| Algebraic integrality/heights | All inputs are algebraic integers; every conjugate of every input has absolute value ≤2^(d+1), since conjugate factors have modulus ≤2 and abs(s_r)≤2 | Direct exact bound |
| Matrix denominators | With Δ=ω−bar(ω), b=(u−bar(u))/Δ; since Δ²=−3, 3a and 3b are algebraic integers | Fixed denominator 3; no height-free rationality assertion |
| Archimedean distortion | √3≤γ_l<2 in the selected embedding; all input scalars lie in [−2^(d+1),2^(d+1)] | No uniform separation is needed or claimed |
| Branch/state/carry cost | 2^d formal amplitude branches; no scalar carry model. Whole products collapse to at most m_d actual rotations | No multiplication of local return labels |
| Bad/uncovered pairs | At least 4(n_d−1)^2/9 pairs have exactly two returns under all U_d | PROVED (14), not a neglected tail |
| Input rates | a=log2 and B=log4 are valid lower/upper exponential rates; exact λ is not established | PROVED bounds only |
| Near-full return growth | No lower bound ρ^(d+o(d)) with ρ>1 can hold outside a power-saving bad set; no almost-everywhere return asymptotic is asserted | PROVED rejection of every ρ>1 |
| Whole-image exponent | Only the trivial upper bound n_d² is available from this analysis | No actual-image lower bound is asserted |
| Net saving / strict c | No positive δ or c is supplied by this return certificate; the exceptional term is quadratic | FAILED certificate, not universal impossibility |

For MS-C2 the same ledger applies with these exact replacements: the
amplitude branches are \(1+\gamma_\ell\); the distinct input bounds
are (24); scalar conjugates are bounded by \(2\cdot3^d\); top-branch
nonzero projection populations are exactly (22); and the bad-pair lower
bound is \((\widetilde n_d-1)^2/2\), with at most sixteen selected
returns on every counted pair. No other cost is silently set to zero.
Its engineered-orbit count is still at most \(6\cdot4^d\), and the
entire image has only its trivial quadratic upper bound in this note.

## 7. Evidence and disposition

All equalities and counts above are symbolic proofs over actual algebraic
numbers. No sampled or floating-point equalities, executable scouts,
oracle calls, generated data, or empirical asymptotic extrapolations are
used. The exact finite local gadget belongs to the companion local-gadget
record; it is not substituted for the all-depth proof here.

The root-approved MS-C1 family and its single approved MS-C2 follow-up
are frozen after (14) and (17). The lead and Agent D independently
checked both new obstruction arguments; Agent A also checked the
four-line proof. These are internal mathematical audits, not external
review or evidence of novelty. This note does not authorize a new
family, a parameter search, or a rerun of an old carrier.
The root's final report records the one remaining project obligation
after disposition of the approved shortlist.
