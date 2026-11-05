# Exceptional output rays in the mixed four-line carrier

6 October 2026 · version 1 · T03 · fixed polynomial
\(Q(x,y)=x^2+xy+y^2\).

## 1. Scope, provenance, and claim record

**Authorization:** the live user message **“New Cross-Block Returns —
Multiscale Quadratic Compression”**, 6 October 2026. This is the bounded
offline first gate on the two existing carriers. The lead froze new
amplitude search after the full-fiber obstructions emerged. This companion
contains only the mixed carrier's explicit norm/conjugate-norm formulas,
exceptional output rays, and actual source-pair counts. It does not
introduce a third carrier or repeat the independent full-fiber proof.

**XB-C1 / PROVED — exceptional-ray source count.** For every depth
\(d\ge1\), in the mixed carrier of MS-C2, at least

\[
\frac12(n_d-1)^2-4(n_d-1)
\tag{1}
\]

ordered pairs have coordinates independent over the indicated fixed
subfield and a Q-value outside the two exceptional output rays defined
below. The stronger exact count in (14) is also valid. A negative lower
bound at a small depth is simply vacuous. For large depth, (1) is a
positive quadratic population.

**Evidence:** new complete symbolic derivation; zero mathematical program
evaluations, zero experiments, no network. The lead independently checked
all six polynomial rows, all exceptional ratios, the discriminant sign,
and the resulting count. Agent C separately audits the full-fiber step.
These are internal checks, not external review or a novelty claim.

**Controlling mathematical sources:**

- [Frozen multiscale composition](../2026-09-30-multiscale-packing/composition.md),
  MS-C2, §5, especially equations (20)–(24): exact carrier, four scalar
  lines, repeated actual population sizes, and input bounds. The earlier
  statement bounds selected torsion actions only. The present note adds
  output-ray accounting and does not revise that historical proof.
- [Frozen MS-C1 field setup](../2026-09-30-multiscale-packing/composition.md),
  §3: the involution and quadratic decomposition used unchanged below.
- `local-only/migration/sources/T03_CURRENT_STATE.md`, §§6–7, retains
  the distinctions between carrier-specific obstructions and the general
  OPEN target; the current track SPEC is historical and is not a new
  search instruction.
- `research/templates/CONSTRUCTION_LEDGER.md` supplies the cost categories
  in §6. No unproved height, splitting, or projection saving is used.

The lead's **XB-F2** full-fiber argument uses the source count here.
This note does not claim an actual-image conclusion without that separate
full-fiber proof.

## 2. Exact inherited carrier and the two output rays

Fix an integer \(d\ge1\) and put

\[
m=6\cdot2^d,\quad \theta=2\pi/m,\quad \zeta=e^{i\theta},
\quad K=\mathbb Q(\zeta)\cap\mathbb R,
\quad t=\zeta+\zeta^{-1}=2\cos\theta.
\tag{2}
\]

The involution \(\sigma(\zeta)=-\zeta\) restricts to K. Write
\(F=K^\sigma\) and \(q=t^2\). The frozen argument gives

\[
K=F\oplus tF,\qquad \sigma(t)=-t,\qquad q\in F,
\qquad \sqrt3\le t<2,\quad 3\le q<4.
\tag{3}
\]

Let

\[
S_d=\{-2\sin(r\theta):0\le r<m\},\qquad
\gamma_\ell=2\cos(2^\ell\theta),
\]
\[
A_d=\bigcup_{J\subseteq\{0,\ldots,d-1\}}
\left(\prod_{\ell\in J}(1+\gamma_\ell)\right)S_d,
\qquad n_d=|A_d|.
\tag{4}
\]

Use the four nonzero line representatives

\[
\alpha_0=1,\quad\alpha_1=t,\quad
\alpha_2=1+t,\quad\alpha_3=q+t=t(1+t),
\qquad L_i=\alpha_iF.
\tag{5}
\]

The four lines are distinct. Their nonzero scalar populations in A have
sizes \(b_+,b_-,b_+,b_-\), respectively, and

\[
n_d-1=2(b_++b_-),\qquad
6\cdot2^d+1\le n_d\le3\cdot4^d+1.
\tag{6}
\]

These are actual-value statements from MS-C2, allowing all amplitude
and projection collisions. In what follows write \(n=n_d\).

If both target coordinates are on the same line \(L_i\), their norm
lies in \(\alpha_i^2F\). The squares of the four representatives
give only two distinct F-lines of possible outputs:

\[
\mathcal E_0=F,\qquad
\mathcal E_1=(1+t)^2F=((q+1)+2t)F,
\qquad \mathcal E=\mathcal E_0\cup\mathcal E_1.
\tag{7}
\]

Indeed \(\alpha_1^2=q\in F^\times\), and
\(\alpha_3^2=q\alpha_2^2\). The two lines in (7) are distinct
because \(2t\ne0\). Here “output ray” means one of these algebraic
F-lines restricted to positive Q-values; it is not an assertion that
every positive real on a Euclidean ray is present. Zero-coordinate
targets also have their Q-values in \(\mathcal E\).

For \(w=E+tD\), with \(E,D\in F\), membership is equivalent to

\[
w\in\mathcal E_0\iff D=0,\qquad
w\in\mathcal E_1\iff(q+1)D-2E=0.
\tag{8}
\]

In particular, at any nonzero source,
\(w=Q(x,y)>0\) and \(\sigma(w)=Q(\sigma x,\sigma y)>0\).
The exact norm ratio is

\[
\frac{Q(x,y)}{\sigma Q(x,y)}=\frac{E+tD}{E-tD}.
\tag{9}
\]

Its two exceptional values are 1 and
\(((1+t)/(1-t))^2\), corresponding precisely to (7).

## 3. Complete cross-block polynomial table

Take \(i<j\) and nonzero parameters \(r,s\in F\), so
\(x=\alpha_i r\), \(y=\alpha_j s\). They are automatically
independent over F. Write
\(Q(\alpha_i r,\alpha_j s)=E_{ij}(r,s)+tD_{ij}(r,s)\).
The full table is:

| Block ij | E_ij(r,s) | D_ij(r,s) |
|---|---|---|
| 01 | r²+q s² | rs |
| 02 | r²+rs+(q+1)s² | rs+2s² |
| 03 | r²+qrs+q(q+1)s² | rs+2q s² |
| 12 | q r²+qrs+(q+1)s² | rs+2s² |
| 13 | q r²+qrs+q(q+1)s² | qrs+2q s² |
| 23 | (q+1)r²+2qrs+q(q+1)s² | 2r²+(q+1)rs+2q s² |

**Verification.** For \(\alpha_i=a_i+t c_i\), the coefficient
vectors \((a_i,c_i)\) are \((1,0),(0,1),(1,1),(q,1)\).
Direct multiplication gives

\[
E_{ij}=(a_i^2+q c_i^2)r^2+
(a_i a_j+q c_i c_j)rs+(a_j^2+q c_j^2)s^2,
\]
\[
D_{ij}=2a_i c_i r^2+(a_i c_j+a_j c_i)rs+2a_j c_j s^2.
\tag{10}
\]

Substitution gives every table row. This is an identity in K, not a
formal-label encoding. Transposed source blocks are obtained by
interchanging the two coordinates and their parameters.

Using (8), the complete list of exceptional ratios is:

| Source block ij | r/s when Q lies in E_0 | r/s when Q lies in E_1 |
|---|---|---|
| 01 | none | none |
| 02 | −2 | (q−1)/2 |
| 03 | −2q | −(q−1)/2 |
| 12 | −2 | −(q−1)/(2q) |
| 13 | −2 | (q−1)/2 |
| 23 | none | none |

All listed ratios are nonzero and belong to F. The table gives
necessary and sufficient conditions in each full line product. Actual
membership in the finite scalar sets can only remove those possibilities.

To verify the “none” entries, block 01 has \(D_{01}=rs\ne0\),
while its other ray condition is

\[
-2r^2+(q+1)rs-2q s^2=0.
\tag{11}
\]

The discriminant is \(q^2-14q+1<0\) for \(3\le q<4\), so
(11) has no nonzero real solution. Block 23 has the same discriminant
in \(D_{23}=0\); its other ray expression is
\((q+1)D_{23}-2E_{23}=(q-1)^2rs\ne0\).
For each remaining row the two ray expressions factor into nonzero
constants times one parameter and one linear factor, yielding precisely
the displayed ratios. No root counts or parameter values were obtained
by program execution.

## 4. Exact source accounting and a positive quadratic remainder

Let \(\mathcal I\subset A_d^2\) consist of ordered pairs of
nonzero scalars on distinct lines from (5). These are exactly the pairs
with coordinates independent over F. By the four actual populations,

\[
|\mathcal I|=(n-1)^2-2(b_+^2+b_-^2)
\ \ge\ \frac12(n-1)^2.
\tag{12}
\]

Fix any nonzero first coordinate x. If its line is 0 or 1, the only
other lines on which an exceptional output is possible are 2 and 3.
If its line is 2 or 3, they are 0 and 1. For each of those two lines,
the ratio table leaves at most two values of the second coordinate y:
at most one for each exceptional output ray. Transposing a table block
does not change this bound, since every listed ratio is nonzero.
Consequently

\[
\#\{(x,y)\in\mathcal I:Q(x,y)\in\mathcal E\}
\le4(n-1).
\tag{13}
\]

This charges both ordered directions and counts actual values. It uses
no uniform-distribution assumption and no control of formal parameter
fibers. Removing these exceptional sources gives the more precise bound

\[
\#\{p\in\mathcal I:Q(p)\notin\mathcal E\}
\ge(n-1)^2-2(b_+^2+b_-^2)-4(n-1),
\tag{14}
\]

which implies (1). For example, when \(n-1\ge16\), (1) is at least
\((n-1)^2/4\). This holds for all \(d\ge2\) by (6), and hence
gives a uniform positive fraction for every sufficiently large depth.

## 5. Meaning and exact interface to the full-fiber argument

Same-line target blocks are the only places where the norm and its
conjugate can be proportional as quadratic forms in the two target
parameters. One way to check the structural statement is to put
\(h_i=\sigma(\alpha_i)/\alpha_i\). Proportionality would require

\[
h_i^2=h_i h_j=h_j^2,
\]

so \(h_i=h_j\), equivalently \(\alpha_i/\alpha_j\in F\).
For distinct lines this is impossible. The same-line blocks' outputs
are exactly restricted to the two rays in (7).

The independently written **XB-F2** argument counts solutions in each
different-line target block by intersecting its two nonproportional
positive norm equations. The result (14) supplies the positive quadratic
source population whose outputs avoid every same-line target block.
This companion does not repeat that intersection proof or infer an
image lower bound merely from the old selected-action failure.

No new composition rule is attempted: the existing mixed carrier already
reaches a decisive obstruction in the current first gate. This is a
scope-specific conclusion. It does not rule out carriers on many more
F-lines, other quadratic-field arrangements, or the general T03 target.

## 6. Construction and quantitative ledger

| Gain or cost | Exact accounting in this companion |
|---|---|
| Carrier and selection order | Exactly the frozen MS-C2 family (2)–(4), one fixed definition for every integer d≥1; no new amplitude mutation |
| Distinct input count | 6·2^d+1 ≤ n_d ≤ 3·4^d+1; exact exponential input rate not asserted |
| Input thinning, both coordinates | None: all estimates concern the actual full same-set square; the subset in (14) is counted to prove an obstruction |
| Projection and parameter fibers | Inherited duplicates already removed; each scalar on a fixed nonzero line has a unique F-parameter; no formal-label multiplicity credited |
| Same-set transport and real embedding | Both coordinates use A_d⊂K⊂R; direct expansion (10) uses the actual scalar polynomial |
| Cross-block populations | Exact four nonzero populations b_+,b_-,b_+,b_-; all 12 ordered different-line blocks counted in (12) |
| Exceptional output count | Two algebraic F-lines, with at most4(n−1) independent source pairs landing on their union |
| Remaining source mass | At least (n−1)²/2−4(n−1), with the stronger expression (14) |
| Field and involution | Inherited [K:Q]=2^d and [K:F]=2; q=t²∈F and 3≤q<4 are used explicitly |
| Heights and denominators | Inherited input algebraic integrality and conjugate bound2·3^d; no height or denominator estimate enters this ray count |
| Discriminant and regulator | Not evaluated or set to zero; neither is needed by the finite algebraic count, and no positive construction gain is inferred from them |
| Local moduli, splitting, carries | None are invoked; cyclotomic m is an angular order, not an uncharged residue gain |
| Branches and equality tests | Four actual F-lines, six unordered source formulas, two output-ray tests; all are explicit above |
| Returns and complete image | This note supplies the source side of XB-F2 only; the full-fiber proof is a separate dependency for any image lower bound |
| Rate conclusion | No new positive output-saving exponent or typical-return rate is asserted; exact λ remains unproved |
| Experiments and programs | Zero mathematical program evaluations, zero experiment CPU allocation, no network; symbolic proof and internal inspection only |

The root records the combined full-fiber disposition, repository checks,
and the single retained next obligation. This companion leaves historical
notes, source exports, and track specifications unchanged.
