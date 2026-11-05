# Bottom line

- **Best local gadget — PROVED:** two norm orbits reuse coordinates in an eleven-element scalar set; its 121 ordered pairs have selected-return histogram `{1:1, 2:64, 6:24, 8:8, 12:24}`.
- **Composition — PROVED packing / FAILED amplification:** dyadic cosine products give exact recursive coordinate identities. The original packing and its one mixed-amplitude variant both have quadratic-sized populations with bounded returns.
- **Input factor:** both satisfy \(3\cdot2^d+1\le n_d\le3\cdot4^d+1\). Thus any limiting \(\lambda\) lies in \([2,4]\); existence or an exact value is **OPEN**.
- **Return factor:** no near-full \(\rho>1\) is possible for the selected action group. On the obstructed populations, \(R=2\) or \(2\le R\le16\), giving exponential return rate zero.
- **Bad-pair exponent — PROVED:** it is 2: at least \(4(n_d-1)^2/9\) pairs in the first packing and \((n_d-1)^2/2\) in the variant fail every fixed polynomial return threshold eventually.
- **Power saving:** no \(c>0\) follows from these return certificates. Actual quadratic-image rates, T03, DC-O1, ML-O1 and RC15/4 remain **OPEN**.

30 September 2026 · T03 · strictly offline · final bounded-cycle report.
All new mathematical conclusions below were checked symbolically by the lead
and independently by the internal rate auditor. This is not external review.

\[
\boxed{
\text{local gadget}
\xrightarrow{\mathrm{PROVED}}\text{multiscale packing}
\xrightarrow{\mathrm{FAILED}}\rho^d\text{ returns},\ \rho>1
\xrightarrow{\mathrm{OPEN}}\text{small bad set}
\xrightarrow{\mathrm{PROVED\ (DC\!\! -\!\! R1)}}\text{power saving}
}
\]

The OPEN arrow is the unresolved general coverage requirement; its desired
conclusion is **FAILED for both specific packings here**. The last arrow is
a proved conditional implication, not a witness.

## 1. Exact orbit packing

**Statement — PROVED.** Let \(\omega=(-1+i\sqrt3)/2\),
\(\phi(x,y)=x-\omega y\), and \(Q=N\circ\phi\). For integer \(d\ge1\), set
\[
m=6\cdot2^d,\quad \theta=2\pi/m,\quad
S=\{-2\sin(r\theta):r\in\mathbb Z/m\mathbb Z\},\quad
\gamma_\ell=2\cos(2^\ell\theta).
\]
The two analyzed scalar carriers are
\[
A_d^{(0)}=\bigcup_{J\subseteq\{0,\ldots,d-1\}}
\left(\prod_{\ell\in J}\gamma_\ell\right)S,
\qquad
A_d^{(1)}=\bigcup_{J\subseteq\{0,\ldots,d-1\}}
\left(\prod_{\ell\in J}(1+\gamma_\ell)\right)S.
\]
Use \(U_d=\mu_m\), the actual complex \(m\)-th roots of unity, on
**every** ordered pair in the same scalar square. Each scaled copy of
\(S\) is the common coordinate projection of one complete norm orbit.
The original packing has exact reuse
\[
\left(\prod_{\ell=a}^{b-1}\gamma_\ell\right)
\sin(2^a\theta)=\sin(2^b\theta)\qquad(0\le a<b\le d).
\]

**Meaning.** These amplitudes lie in one common growing field and share
actual coordinates. All actions multiply the whole complex scalar, preserving
cross terms. Formal address counts are never counted as distinct returns.

**Consequence.** This advances beyond separated radial tags, but the exact
identity alone does not multiply return counts. The second definition is the
single allowed mixed-amplitude follow-up; no further mutation was attempted.

## 2. The two scoped obstructions

**Statement — PROVED (first packing).** Write \(n=|A_d^{(0)}|\). At least
\[
\frac49(n-1)^2
\]
ordered pairs have exactly two distinct returns under all of \(U_d\), from
the multipliers \(1,-1\).

**Meaning.** The involution \(\zeta_m\mapsto-\zeta_m\) splits every carrier
scalar into one of two eigenspaces. The two populations have ratio at most
two. A pair with nonzero coordinates in opposite eigenspaces cannot return
under a mixing matrix whose entries have one common parity.

**Consequence.** For every fixed \(\varepsilon,\delta>0\), its bad tail
\(\#\{p:R_{\rm pair}(p)<n^\varepsilon\}\) is not
\(O(n^{2-\delta})\) as \(d\to\infty\).

**Statement — PROVED (mixed variant).** Write \(n=|A_d^{(1)}|\).
At least \((n-1)^2/2\) ordered pairs have at most sixteen distinct returns.

**Meaning.** Mixing parity removes eigenpurity but leaves only four
one-dimensional spaces over the involution's fixed subfield. On pairs
independent over that subfield, each possible target coordinate space and
action parity permits at most two norm-one actions. There are four spaces
and two parities, hence the bound \(4\cdot2\cdot2=16\).

**Consequence.** The same fixed-exponent tail fails. These are
**selected-action obstructions**, not actual-image lower bounds: other
norm-one multipliers can encode additional polynomial collisions.
The detailed proof handles all projection collisions, zero and depth one;
see [composition](composition.md) and [independent audit](audit.md).

## 3. Full-support gate and remaining scope

**Statement — PROVED implication / OPEN witness.** The frozen
[DC-R1](../2026-09-21-dense-cartesianization/block-rectangle.md) and its
underlying same-set fiber lemma give
\[
|Q(A,A)|\le n^2/R+|E|
\]
if every pair outside \(E\) has at least \(R\) genuine targets. Therefore
\(R\ge n^\varepsilon\), \(|E|=O(n^{2-\delta})\) certify every strict
\(0<c<\min(\varepsilon,\delta)\) eventually.

**Meaning.** Each good source lies in an actual polynomial fiber of size
at least \(R\); those fibers are disjoint. Outputs without a good source
are charged to exceptional pairs. Neither energy nor formal orbit labels
replace this all-output accounting.

**Consequence.** Here a quadratic exceptional population defeats that
certificate. It does not show quadratic actual images, disprove RC15/4 or
ARG/TCRC, or close all multiscale packings. A separate fixed-field affine
preselection filter was only an application of the already frozen T03
ideal bound; it is identified as inherited in [audit §3](audit.md).

## 4. Completion and handoff

- **Budget used:** 0 / 2,000,000 charged exact program evaluations;
  0 / 600 research-program CPU seconds. Finite tables were proved by hand.
  Both candidates failed analytic gates, so no scout or depth sweep was run.
- **Team:** local designer, recursive architect and independent auditor;
  the lead held the exact-scout role and independently checked the proofs.
  Two local gadgets, two analyzed carrier definitions, one related mutation.
  The two-obstruction stop rule was met.
- **Checks:** repository, setup/source-integrity and whitespace checks are
  recorded with actual results in [verification](verification.md). No code
  changed; regression programs were not rerun.
- **Files:** [local identities/tables](local-gadgets.md),
  [recursive proofs](composition.md), [audit](audit.md),
  [charged rate ledger](ledger.md), [verification](verification.md),
  [machine state](state.json), [hash manifest](manifest.json).

**Exactly one next mathematical obligation — ML-O1 / OPEN (retained).**
For \(m=6\cdot7^{k-1}\), \(t=8\cdot7^{k-1}\), choose explicit amplitudes
\(c_{k,j}\in\mathbb Q(\zeta_m)\setminus\{0\}\) with disjoint cosets
\(c_{k,j}\mu_m\), so the faithful paired lift of the \(t\) primitive
modular orbits has a same-set scalar completion \(A_k\), \(|A_k|\to\infty\),
with at least \(|A_k|^\varepsilon\) genuine returns outside
\(O(|A_k|^{2-\delta})\) ordered pairs, for fixed \(\varepsilon,\delta>0\).
This is the existing [ML-O1 obligation](../2026-09-30-modular-lift/proofs.md),
not a new conjecture or authorization for another cycle. The present dyadic
tests do not settle it.
