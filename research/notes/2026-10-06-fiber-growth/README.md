# XB-O1 → Cross-Block Fiber Growth

**6 October 2026 · T03 · version 1 · bounded offline cycle.**
Fixed target: \(Q(x,y)=x^2+xy+y^2\), with one real scalar set in both coordinates.

## 1. Outcome and scope

**PROVED:** explicit amplitudes \(c_{h,j}=h(1+\omega\xi^j)\), \(1\le h\le8\),
\(j\bmod q\), give all \(8q\) required disjoint cosets, actual scalar size
\(n=\Theta(q^2)\), and the completed-set spreading bound
\[
\max_\alpha |(A_q\setminus\{0\})\cap\alpha F|
\le64\sqrt2\,n^{1/2}.
\]
Thus the live XB-O1 gate passes with \(\kappa=1/2,C=64\sqrt2\).

**FAILED IN STATED SCOPE:** a new complete-fiber theorem proves
\[
\boxed{|Q(A_q,A_q)|=\Theta(n^2).}
\]
This is an actual-image obstruction for this new carrier, not merely a
selected-action failure. The second proposal, a seven-factor relative-norm
rule, fails the required disjoint-coset condition. Both finalists reached
rigorous stopping gates. Neither was repaired.

The general quadratic target, ML-O1, DC-O1, RC15/4 and ARG/TCRC remain
**OPEN**. HR-N1 remains **FAILED / DISPROVED**. No claim excludes arbitrary
spreading amplitude families or asserts novelty.

### Sources and companions

The starting point was the [6 October cross-block report](../2026-10-06-cross-block-returns/README.md),
its [full-fiber proof](../2026-10-06-cross-block-returns/audit.md), and the linked
[multiscale composition argument](../2026-09-30-multiscale-packing/composition.md).
Neither old dyadic carrier was repeated. The prescribed inventory is [ML-4](../2026-09-30-modular-lift/proofs.md).

| Companion | Contents |
|---|---|
| [amplitudes.md](amplitudes.md) | FG-A1–A5: fields, recursion, cosets, scalar growth, spreading and encoded coverage |
| [fibers.md](fibers.md) | FG-N1: relative-norm defect; FG-F1: full-fiber and actual-image obstruction |
| [audit.md](audit.md) | Independent symbolic derivations and final written-proof review |
| [ledger.md](ledger.md) | Signed rates, arithmetic costs, claim provenance and failure scopes |
| [verification.md](verification.md) | Exact scouting, validation, counters and repository checks |
| [data.json](data.json) | Complete finite fiber histograms and projective counts |
| [state.json](state.json) | Machine-readable final claim records and statuses |
| [manifest.json](manifest.json) | Companion, source and local-run hashes |

## 2. Exact construction and spreading

Put \(r=k-1\), \(q=7^r\), \(m=6q\), \(t=8q\),
\[
\omega=(-1+i\sqrt3)/2,\quad \xi=e^{2\pi i/q},\quad
K=\mathbb Q(\omega,\xi),\quad K^+=K\cap\mathbb R,\quad \Delta=1+2\omega.
\]
For \(r\ge1\), the unique **index-two subfield** is
\[
F=\mathbb Q(\xi+\xi^{-1}),\qquad K^+=F(\sqrt{21}).
\]
Its involution \(\sigma\) fixes \(\omega\) and inverts \(\xi\). For nonzero
\(a,b\in K^+\),
\[
aF=bF\iff a/\sigma(a)=b/\sigma(b).
\]
At \(r=0\), \(K^+=\mathbb Q\), with no index-two subfield.

Choose \(c_{h,j}=h(1+\omega\xi^j)\). With compatible roots, the coupled recursion is
\[
c^{(r+1)}_{h,a+7j}
=\xi_{r+1}^{a}c^{(r)}_{h,j}+h(1-\xi_{r+1}^{a}),\qquad 0\le a\le6.
\]
Their squared complex absolute values
\[
N_{K/K^+}(c_{h,j})=h^2(2+\omega\xi^j+\omega^2\xi^{-j})
\]
are distinct, proving disjoint cosets. The orbit union is exactly
\[
Z_q=\{h\kappa(\xi^a+\omega\xi^b):1\le h\le8,\ \kappa\in\mu_6,\ a,b\bmod q\},
\qquad |Z_q|=48q^2.
\]
Define
\[
C_a=(\xi^a+\xi^{-a})/2,\quad D_a=(\xi^a-\xi^{-a})/(2\Delta),
\]
\[
X_{ab}=C_a+D_a-2D_b,\qquad Y_{ab}=-C_b-2D_a+D_b.
\]
Then \(X_{ab}-\omega Y_{ab}=\xi^a+\omega\xi^b\). Both real projections
of \(Z_q\) agree, and their exact completion is
\[
\boxed{A_q=\{\pm hX_{ab},\ \pm hY_{ab},\ \pm h(X_{ab}+Y_{ab}):
1\le h\le8,\ a,b\bmod q\}.}
\]
For \(q\ge7\), the map \((a,b)\mapsto X_{ab}\) has fibers at most two, so
\[
q^2/2\le n\le48q^2,\qquad n=49^{r+o(r)}.
\]
This input growth factor is proved for the new family; none is assumed for
the older dyadic packings.

The even/odd decomposition \(K^+=F\oplus\sqrt{21}F\) bounds line
populations: \(X\) contributes at most \(q\) labels, \(Y\) at most \(q\),
and \(X+Y\) at most \(2q\), by intersection with
\(C_b^2+3D_b^2=1\). The eight scales and two signs give \(64q\).
Thus occupied projective directions number at least
\((n-1)/(64q)=\Omega(\sqrt n)\), with the required maximum controlled.
This is a completed-scalar count, not an amplitude-label count.

The current gate allows a fixed prefactor. The older coefficient-one
asymptotic screen also follows for each fixed \(0<\kappa<1/2\) eventually;
a coefficient-one bound at \(\kappa=1/2\) is not asserted.

## 3. Identity, full fibers and the bad tail

Simultaneous angular shifts give the genuine identity
\[
Q(X_{a+\ell,b+\ell},Y_{a+\ell,b+\ell})
=2+\omega\xi^{b-a}+\omega^2\xi^{a-b}.
\]
The targets belong to \(A_q^2\), and their multipliers are \(\xi^\ell\).
The six units give \(6q\) distinct targets per encoded orbit. But the
encoded source set has only \(48q^2=\Theta(n)\) pairs, a
\(\Theta(n^{-1})\) fraction of the square. **No identity yielding growing
generic cross-block fibers was found.**

For any nonzero source \(p\), every equal-\(Q\) target \(s\) gives the
unique actual norm-one multiplier
\[
u=(s_x-\omega s_y)/(p_x-\omega p_y).
\]
Hence \(R_U(p)\le F_A(p)\) for every selected action family. The origin
has one full-fiber target. No ratio list was credited with new collisions.

**FG-F1 / PROVED.** Let \(C_*=48^2 32^4\). At least
\[
(q^4-3696q^3)/4
\]
distinct ordered source pairs have entire \(Q\)-fiber at most \(C_*\).
For \(q\ge7392\),
\[
\#\{p:F_A(p)\le C_*\}\ge n^2/18432,\qquad
|Q(A,A)|\ge n^2/(18432C_*).
\]

The proof expands every cross term. Every target norm \(\Delta^2Q\)
has at most 33 cyclic frequencies. For generic \((X_{ab},X_{cd})\)
sources, all 33 occupy different blocks modulo \(q/7\). Cyclotomic
relations are constant within each seven-position block. Covering every
source block exhausts the target's 33-position budget, forcing exact
coefficient agreement. Each target angular index has at most 32 choices;
each scalar has 48 signed types. This gives \(C_*\), covering all targets.
The 528 possible frequency coincidences exclude at most \(3696q^3\)
source labels; source projection costs a factor four. Full details and
the independently checked coefficients are in [fibers.md](fibers.md), §5.

For arbitrary fixed \(\varepsilon,\delta,C'>0\), eventually
\[
n^\varepsilon>C_*,\qquad n^\delta>18432C',
\]
so \(\#\{F_A<n^\varepsilon\}\ge n^2/18432>C'n^{2-\delta}\).
Thus no positive \(\varepsilon,\delta\) works for this carrier, and
no \(c>0\) follows. The actual lower bound additionally rules out any
fixed image power saving here. Spreading's \(\kappa\) is not a fiber
exponent; \(\eta\) is inapplicable because one set already serves both coordinates.

The same-set support lemma remains valid: outputs meeting \(A^2\setminus E\)
have at least \(R\) source pairs each, and outputs confined to \(E\)
number at most \(|E|\). Hence \(|Q(A,A)|\le n^2/R+|E|\).
Its high-fiber hypothesis fails for this carrier.

## 4. Second rule: sevenfold coset collapse

**FG-N1 / FAILED IN STATED SCOPE.** The other recursive rule is
\[
c_{b,j}=b\prod_{a=0}^{6}(2-\xi^{j+a q/7})=b(128-\xi^{7j}).
\]
The exact identity \(c_{b,j+q/7}=c_{b,j}\) leaves at most \(8q/7\)
cosets instead of \(8q\). Iteration loses \(7^\ell\) labels for
\(1\le\ell\le r\). This proposal stopped at the amplitude gate.
No scalar-size, spreading, or actual-image assertion is made for its
deduplicated completion.

## 5. Predetermined exact scouts

**EXPERIMENTAL — exhaustive at \(k=1,2\), not an asymptotic premise.**
The integer coefficient model uses \(3A_q\); homogeneous scaling preserves
all counts. The median is pair-weighted. The threshold \(\varepsilon=1/4\)
is a fixed diagnostic, not an asserted asymptotic exponent.

| \(k\) | \(n\) | \(\max_F L_F(A)\) | Median \(F_A\) | \(\#\{F_A<n^{1/4}\}\) | \(\lvert Q(A,A)\rvert\) |
|---|---:|---:|---:|---:|---:|
| 1 | 17 | N/A | 12 | 9 | 44 |
| 2 | 1,025 | 48 | 4 | 1,009,385 | 256,053 |

At \(k=2\), the 40 nonzero projective classes have sizes 16 (25 classes),
32 (6 classes), and 48 (9 classes). All fiber histograms and the
\(\varepsilon=1/2\) diagnostic are in [data.json](data.json).
Complete distributions were independently reconstructed using complex
norms and sign/swap representatives; projective classes were regrouped
by cross products rather than inversion. Both checks passed.

Shared use including validation: **1,335,870 evaluations and 35.734223
measured program CPU seconds**. Both caps and the 20% verification reserve
were respected. These are not model-token, credit or wall-time counts.

## 6. One unresolved lemma

Both failures concern exactly the displayed rules. Their scope does not
extend to arbitrary cyclotomic amplitudes or the quadratic target.
The mathematical cycle stopped after these two failures; packaging did
not reopen the search.

**FG-O1 / OPEN — exact matching classification.** For this \(A_q\), classify
the 33-slot coefficient matches for a source \((X_{ab},X_{cd})\) whose
33 frequencies are distinct modulo \(q/7\): determine whether every target
is one of \(\pm(X_{ab},X_{cd})\), \(\pm(X_{cd},X_{ab})\), or identify
all additional matching types. This is one concrete unresolved rigidity
lemma, not an adopted conjecture, an attempted repair, or a route to power
saving on an already obstructed carrier.
