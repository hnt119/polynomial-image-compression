# Phase-transposed factor switches: exact membership and a sparse return domain

**11 October 2026 · version 1 · T03.** Fixed polynomial
\(Q(x,y)=x^2+xy+y^2\). This is the sole new mechanism assigned to
specialist B in the authorized **fixed balanced-factor carrier full-fiber**
cycle. The amplitudes and the same-set completion are unchanged. Work is
strictly offline: no mathematical program, phase/mask enumeration, or
network request was made; this contribution charges zero evaluations and
zero research-program CPU seconds against the lead's shared budget.

| Claim | Status and exact scope | Locator |
|---|---|---|
| BFF-P1 | PROVED: the phase-transposed switched target belongs to the same Cartesian square; exact norm equality is a quartic condition, with the stated sign/swap degeneracy | §§2–3 |
| BFF-P2 | PROVED: sources with a target outside their four-point sign/swap orbit number at most \(55296q^3 4^r\); adjoining these moves to the old certificate still leaves almost every source with at most four certified targets | §§4–5 |

**Disposition:** this precisely defined enlarged certificate is **FAILED**
as a source of a positive-power return tail on almost all of \(A^2\).
The full fiber \(F_A(x,y)\), which permits every actual equal-\(Q\)
target, is not bounded by this result. Its asymptotic behavior and the
full image bound remain **OPEN**. No external novelty is asserted.

## 1. Fixed inputs and dependencies

The controlling predecessor is
[amplitudes.md](../2026-10-06-cross-block-amplification/amplitudes.md),
AMP-A1–A4, dated 6 October 2026. The dependency arguments relevant to this
calculation were inspected here.
The inherited independent-switch certificate and its closure theorem are
[returns.md](../2026-10-06-cross-block-amplification/returns.md),
AMP-R1–R3, §§3–6. Their scope is retained exactly below; they are not
full-fiber upper bounds.

For each integer \(r\ge0\), put
\[
q=7^r,\qquad m=6q,\qquad \xi=e^{2\pi i/q},\qquad
\omega=e^{2\pi i/3},\qquad \Delta=1+2\omega,
\qquad \Delta^2=-3.
\tag{1}
\]
Write \(H=\mathbb Q(\xi)\), \(L=\mathbb Q(\omega,\xi)\).
The eight scales and digit alphabet are fixed before depth grows:
\[
c_{h,\mathbf i}=h\prod_{\ell=0}^{r-1}
(2-\xi^{i_\ell7^\ell}),\qquad
1\le h\le8,\quad \mathbf i\in\{-3,-2,-1,0,1,2,3\}^r.
\tag{2}
\]
There are exactly \(8q\) nonzero **bare amplitudes** in (2), all in
\(H\), with pairwise disjoint \(\mu_m\) cosets. Thus two bare
amplitudes which are root-of-unity multiples are the same amplitude with
the same scale and word, and their quotient is exactly 1. Also
\(\omega\notin H\). At positive depth this follows from the field
degrees in AMP-A1–A2; at depth zero it follows from \(H=\mathbb Q\).

Set
\[
Z=\bigcup_{h,\mathbf i}c_{h,\mathbf i}\mu_m,
\quad X(z)=\frac{\omega\bar z-\omega^2z}{\Delta},
\quad Y(z)=\frac{\bar z-z}{\Delta}.
\tag{3}
\]
These are real coordinates with
\[
z=X(z)-\omega Y(z),\qquad
Y(z)=X(\omega z),\qquad X(z)=Y(\omega^2z).
\tag{4}
\]
Consequently
\[
A=X(Z)=Y(Z),\quad n=|A|,\quad
\Gamma=\{(X(z),Y(z)):z\in Z\},
\tag{5}
\]
and the inherited, already projection-adjusted bounds are
\[
|Z|=|\Gamma|=48q^2,\qquad 8q^2\le n\le48q^2.
\tag{6}
\]
The seed has \(A_0=\{0,\pm1,\ldots,\pm8\}\), so \(n_0=17\).
In particular \(n=49^{r+o(r)}\).
The current companion [algebra.md](algebra.md), BFF-A1, §2, strengthens
the actual scalar count for this unchanged carrier to
\[
16q^2+1\le n\le24q^2-7.
\tag{6a}
\]
Its disjoint-decomposition proof was inspected for the refined constants
below. The argument also works with (6), with larger numerical constants.

A **switch** replaces any chosen subset of digits by their negatives.
Write \(c'\) for a switched amplitude from \(c\). There are at most
\(2^r\) mask labels per amplitude. Masks on zero digits can coincide;
they will only enter upper counts. Every such \(c'\) is again a bare
amplitude and satisfies \(N(c')=N(c)\), where \(N(z)=z\bar z\).

## 2. BFF-P1 — one coupled rule, with automatic membership

### Statement

Allow **every** representation of an actual source pair as
\[
p=(x,y)=(X(c\alpha),Y(d\beta)),
\qquad \alpha,\beta\in\mu_m,
\tag{7}
\]
where \(c,d\) are bare amplitudes. Choose switches \(c\mapsto c'\)
and \(d\mapsto d'\) independently, and choose
\(\kappa,\lambda\in\mu_6\). The proposed target is
\[
\boxed{
p'=(x',y')=
\bigl(X(\kappa c'\beta),\,Y(\lambda d'\alpha)\bigr).
}
\tag{8}
\]
Both target coordinates belong to \(A\). An edge is retained **only**
when \(Q(p')=Q(p)\). The allowed correction phases in (8) are exactly
\(\mu_6\), not arbitrary source-dependent corrections in \(\mu_m\).

### Meaning

The two source phases are exchanged, so this is a coupled rule rather
than the predecessor's independent switches at fixed phases. Cartesian
membership is unconditional, but norm preservation is a separate exact
equation. If \(p\ne(0,0)\) and that equation holds, the actual
whole-source action is
\[
u_p=\frac{x'-\omega y'}{x-\omega y},\qquad N(u_p)=1.
\tag{9}
\]
Equation (9) is a consequence of the tested norm equality; no factorwise
action is presumed to preserve the norm of the assembled source.

### Consequence

The rule is a genuine possible source of cross-block targets. Its
eligible-source population, rather than its formal number of switch
labels, is what the following calculation bounds.

## 3. Whole norm equation and its exact degeneracy

Fix \(c,d,c',d',\kappa,\lambda,\alpha\), and write
\[
x=X(c\alpha),\qquad t=Y(\lambda d'\alpha),\qquad U=\kappa c'.
\]
As functions of the second phase \(\beta\),
\[
x'=\frac{-\omega^2U\beta+\omega\bar U\beta^{-1}}{\Delta},
\qquad y=\frac{-d\beta+\bar d\beta^{-1}}{\Delta}.
\tag{10}
\]
The full defect, including the mixed term, is
\[
F(\beta):=Q(x',t)-Q(x,y)
=(x'^2-y^2)+(tx'-xy)+(t^2-x^2).
\]
Direct expansion gives
\[
\begin{aligned}
\Delta^2F(\beta)={}&(\omega U^2-d^2)\beta^2\\
&+\Delta(-\omega^2tU+xd)\beta\\
&+2(N(d)-N(U))+\Delta^2(t^2-x^2)\\
&+\Delta(\omega t\bar U-x\bar d)\beta^{-1}\\
&+(\omega^2\bar U^2-\bar d^2)\beta^{-2}.
\end{aligned}
\tag{11}
\]
If \(\omega\kappa^2(c')^2-d^2\ne0\), multiplying (11) by
\(\beta^2\) gives a nonzero polynomial of degree four. There are
therefore at most four possible \(\beta\in\mu_m\) with equal norm.
This uses a root count over a field, with no assumed independence of the
other coefficients or of cyclotomic powers.

If the leading coefficient vanishes, then
\[
(d/c')^2=\omega\kappa^2\in\{1,\omega,\omega^2\}.
\]
The left side belongs to \(H\), which excludes \(\omega\) and
\(\omega^2\). Hence \(\kappa=\tau\omega\) for
\(\tau\in\{1,-1\}\), and \(d=\pm c'\). Disjointness of the
bare amplitude cosets forces the exact equality \(d=c'\); the negative
case cannot occur. Thus the entire degeneracy is
\[
\boxed{\kappa=\tau\omega,\qquad d=c'.}
\tag{12}
\]
In this case \(x'=\tau y\), and the complete norm defect factors as
\[
\boxed{
Q(\tau y,t)-Q(x,y)=(t-\tau x)(t+\tau x+\tau y).
}
\tag{13}
\]
If \(t=\tau x\), the target is simply \(\tau(y,x)\), for every
second phase. Otherwise equality requires \(y=-\tau t-x\), a fixed
coordinate. On the nonzero circle \(d\mu_m\), a fixed \(Y\)-coordinate
has at most two points: by (4) it is a horizontal line intersecting the
positive-definite ellipse \(X^2+XY+Y^2=N(d)>0\). Since the phase map
\(\beta\mapsto d\beta\) is injective, this gives at most two second
phases. The resulting target, when it exists, is the fixed rotation
\[
p'=\tau(y,-x-y)=\tau M_\omega p.
\tag{14}
\]
Zero coordinates cause no omitted case. At the zero pair, positivity of
\(Q\) permits only the zero equal-norm target.

There is a transparent nonbaseline example, without any search: take
\(c=d=c'=d'=1\), empty switches, \(\alpha=\omega\),
\(\beta=\omega^2\), \(\kappa=\omega\), \(\lambda=1\).
Then (8) sends \((0,1)\) to \((1,-1)\), both of norm 1. These are
outside one another's four-point sign/swap orbit, but both are already
in \(\Gamma\) at every depth. Thus this example supplies no new
generic amplification beyond the encoded certificate.

## 4. BFF-P2 — source population and actual target accounting

For \(p=(x,y)\), define its sign/swap orbit
\[
\mathcal S(p)=\{(x,y),(-x,-y),(y,x),(-y,-x)\}.
\tag{15}
\]
Let \(D_{\rm tr}\subseteq A^2\) consist of the actual sources which
admit at least one retained edge (8) with target outside
\(\mathcal S(p)\). All scalar representations and all allowed masks
and unit corrections are included in this definition.

For each choice of bare amplitudes, two switch masks, first phase and
two correction units, §3 leaves at most four second phases which can
contribute to \(D_{\rm tr}\). In (13), the all-phase branch is
\(\pm\)swap and is excluded; its other branch has at most two phases.
Consequently
\[
\boxed{
|D_{\rm tr}|
\le(8q)^2\,4^r\,(6q)\,36\,4
=55296q^3 4^r.
}
\tag{16}
\]
This is an upper count of labels. Multiple labels for a scalar or a
target only decrease the actual source count; no uniform scalar-lift
regularity is assumed. In particular (6a) gives
\[
\frac{|D_{\rm tr}|}{n^2}\le216(4/7)^r=o(1).
\tag{17}
\]

### Reversibility and sign/swap compatibility

For a retained edge, use target representations with bare amplitudes
\(c',d'\) and phases \(\kappa\beta,\lambda\alpha\). Switching the
same masks back and choosing correction units
\((\lambda^{-1},\kappa^{-1})\) recovers the source. Thus the relation
is reversible, with no expansion of the allowed correction group.

Simultaneous sign is realized by negating both source phases. For swap,
represent
\[
(y,x)=\bigl(X(d\,\omega\beta),Y(c\,\omega^2\alpha)\bigr).
\]
Exchange the amplitude/mask roles and use correction units
\[
(\kappa_{\rm sw},\lambda_{\rm sw})
=(\omega^2\lambda,\omega\kappa)\in\mu_6^2.
\tag{18}
\]
The resulting target is
\[
\bigl(X(\omega\lambda d'\alpha),Y(\omega^2\kappa c'\beta)\bigr)
=(y',x').
\]
Both \(Q\) and the exclusion of \(\mathcal S(p)\) are preserved.
Therefore the relation and \(D_{\rm tr}\) are sign/swap invariant.

## 5. Iteration with the old certificate still has bounded returns

Let \(D_{\rm old}\) be exactly the set in AMP-R2: sources admitting
an old independent coordinate-switch target outside \(\{p,-p\}\).
The inherited theorem gives
\[
|D_{\rm old}|\le1536q^3 4^r.
\tag{19}
\]
It also proves that \(D_{\rm old}\) and \(\Gamma\) are sign/swap
invariant. The latter follows because \(Z\) is closed under negation,
conjugation and multiplication by \(\mu_m\); swap on decoded pairs is
\(z\mapsto-\omega\bar z\).

Define \(R_*(p)\) as the number of distinct actual vertices reachable
by any finite sequence of the following edges, including the source:

1. The new phase-transposed switched edges (8), filtered by exact norm equality.
2. The predecessor's independent coordinate-switch edges, filtered by exact norm equality.
3. Simultaneous sign and coordinate swap.
4. Every equal-\(Q\) edge whose two endpoints both belong to \(\Gamma\).

All these vertices belong to the full fiber, so \(R_*(p)\le F_A(p)\).
For \(p\notin D_{\rm old}\cup D_{\rm tr}\cup\Gamma\), a new
edge stays in \(\mathcal S(p)\), an old switch stays in \(\{p,-p\}\),
and no encoded edge is available. The exceptional union is sign/swap
invariant. Thus all four possible sign/swap states remain outside it,
and induction on path length proves
\[
\boxed{R_*(p)\le4
\quad(p\notin D_{\rm old}\cup D_{\rm tr}\cup\Gamma).}
\tag{20}
\]
In particular
\[
\boxed{
\#\{p\in A^2:R_*(p)\le4\}
\ge n^2-56832q^3 4^r-48q^2.
}
\tag{21}
\]
Using the refined actual input bound in (6a),
\[
\frac{|D_{\rm old}\cup D_{\rm tr}\cup\Gamma|}{n^2}
\le222(4/7)^r+\frac{3}{16q^2}=o(1).
\tag{22}
\]
With only the inherited bound (6), the same argument gives the valid
weaker expression \(888(4/7)^r+3/(4q^2)\).
Hence, for any fixed \(\varepsilon,\delta>0\), this certificate
cannot give \(R_*(p)\ge n^\varepsilon\) outside at most
\(n^{2-\delta}\) sources for all sufficiently large depths. Indeed
(21) gives at least \(n^2/2\) sources with \(R_*(p)\le4\) eventually,
whereas \(n^\varepsilon>4\) and \(n^{2-\delta}<n^2/2\) eventually.

This is **not** an upper bound for \(F_A\): unlisted targets and paths
through such targets remain possible. In particular a small certificate
does not imply a lower bound for the actual image. No full-image exponent
is extracted from (20)–(22).

## 6. Construction and rate ledger

This records the applicable entries of the repository
[construction ledger](../../templates/CONSTRUCTION_LEDGER.md).

| Gain or cost | Exact accounting and scope |
|---|---|
| Fixed data and growing parameter | The same eight scales, digit alphabet and polynomial are fixed; only \(r\) grows, with \(q=7^r\). The new correction group is fixed \(\mu_6\). |
| Actual scalar inputs | BFF-A1 refines the inherited bound to \(16q^2+1\le n\le24q^2-7\); no amplitude or scalar carrier is changed. Thus both input rates are \(a=B=\log49\) per depth. |
| Thinning and projection | No thinning in either coordinate. Scalar collisions are charged through (6a). Source labels are used only as an upper bound in (16), so collisions cannot invalidate the count. |
| Real and same-set transport | Formula (3) gives real coordinates, (4) makes both projections the same set, and (8) proves both target memberships. Every source representation is allowed. |
| Whole polynomial identity | Formula (11) includes the full mixed term. Only exact roots of this equality are retained. Formula (9) defines the whole-source norm-one multiplier after equality has been established. |
| Branch and ratio counts | At most \(4^r\) switch-mask pairs, \(36\) correction pairs, \(6q\) first phases and at most four nonbaseline second phases per fixed remaining data. Degenerate baselines are charged separately in (13). |
| Distinct actions and stabilizers | Only actual target pairs and actual sources are counted. Duplicate masks, phase descriptions or scalar lifts earn no gain. The zero pair has a singleton full fiber. |
| Local moduli and splitting | The exact phase modulus is \(6q\). This proof uses the predecessor's disjoint-coset and \(\omega\notin H\) facts, not a modular return estimate or an unproved lifting step. |
| Field degree | At positive depth \([L:\mathbb Q]=12\cdot7^{r-1}\) and \([K^+:\mathbb Q]=6\cdot7^{r-1}\); at depth zero they are 2 and 1. These costs are not treated as bounded. No factor depending on degree enters the quartic root count. |
| Denominators and heights | Bare amplitudes and phases are algebraic integers. Since \(\Delta^{-1}=-\Delta/3\), the real coordinates have denominator dividing 3 in \(\mathcal O_L\). Each conjugate amplitude has modulus at most \(8\cdot3^r\), and each conjugate scalar at most \(16\cdot3^r/\sqrt3\). No denominator saving is claimed. |
| Discriminant, regulator, units | No estimate for these quantities is needed for this exact finite-label obstruction; their sizes are not asserted to be zero or uniformly bounded. The proof uses no unit count or geometry-of-numbers theorem. |
| Archimedean distortion and carries | Coordinates are evaluated exactly in the stated embedding, with the conjugate bounds above. There is no separated-scale approximation, digit carry assumption, or geometric rounding. |
| Coverage and exceptions | All actual sources outside the explicitly counted union in (21) have at most four certified targets. Encoded pairs cost \(48q^2\), separately from switched-source labels. All other full-fiber targets remain unresolved. |
| Output exponent and net gap | No upper bound smaller than the trivial \(n^2\) is proved for the entire image. There is no certified positive \(\delta\), no power-saving exponent, and no same-set transport to another polynomial. |

## 7. Evidence and stop boundary

The proof above is an internal symbolic derivation using the identified
predecessor lemmas. The lead and independent audit specialist checked its
quartic, degeneracy, constants, reversal and swap formulas before the
written note was saved. The independent specialist subsequently inspected
the complete written BFF-P1/P2 proofs, including all five coefficients in
(11), the refined constants, all-representation counting and iteration,
and reported a pass without corrections. That review is recorded in the
cycle's audit companion. This is internal review, not an external novelty
or literature review.

There are no program commands, runtime observations, seeds, generated
outputs, or mathematical evaluation hashes for this subtask. Any finite
full-fiber evidence belongs to the lead's separate run record. The result
closes this one proposed coupled mechanism within the explicit correction
and iteration rules in §§2 and 5. Arbitrary phase corrections, new
amplitudes, and other mechanisms were not searched; the unrestricted
full-fiber obligation remains open.
