# T02 current status — fixed quartic / hybrid / ramified precision

**7 November 2026 · fixed target OPEN.** C4 gives the exact local count on the full critical input. T02-O1 asks for a bound on support actually attained. [Restart record](../../OPEN_LEMMAS.md#restart) · [Evidence and later checkpoints](../../EVIDENCE_INDEX.md). The dated record follows.

Reconciled 2026-09-11 from the accepted checkpoint dated 2026-09-10.
**Fixed-quartic target: OPEN.** The [SPEC](SPEC.md) remains the fixed target:

$$P_4(x,y)=(x+2y)^4+3x-y.$$

The requirement is one fixed positive exponent and arbitrarily large finite real
sets, with the same set in both inputs. No quartic impossibility theorem or
novelty claim is established. The C0 rank-one quadratic family is shared project
progress, recorded separately in [PROJECT_HISTORY](../../PROJECT_HISTORY.md).

## Accepted C2–C4 results

- **PROVED — C2:** the determinant-7 map has image
  $\{(a,b):a+2b\in7\mathcal O\}$ and index $7^d$. Its scalar consequence is
  $h_s(z)=2z^4+sz$ in $R=\mathbb F_7[\pi]/(\pi^3)$, with
  $|h_s(R)|=208=4\cdot49+3\cdot4$ for $s=\pm1$.
  CRT gives at most $208^{d/3}(\rho_4Q)^d$ occupied classes modulo $7Q$;
  population per class is counted separately. The graph index and scalar
  restriction are not independent savings.
- **PROVED — C2:** the positive hybrid $C=GT$ is direct, $|C|=|G||T|$.
  Its exact ratio decomposition has $|\mathcal K_u|=|T|^2$ and
  $\sum_u|G(u)|=|G|^2$. The displayed elementary count supplies only
  $\kappa_{\rm cert}=0$; cross-point and cross-ratio overlaps are not excluded.
  The actual image exponent remains **OPEN**.
- **PROVED — C3:** every nonempty $E\subseteq R$ and either sign satisfy
  $\Phi_s(E)=343|h_s(3E-E)|/|E|^2\ge4/7$.
  Equality holds exactly for full critical fibers $a+\pi R$, $a^3=-s$.
  The multifiber minimum is $208/343$, only at $R$; the second minimum
  excluding critical full fibers is $343/576$, exactly for a critical full
  fiber minus one point. This universal theorem is analytic.
- **PROVED — C4:** in the actual local cubic with $e=3,f=1$ and
  $7\mathcal O=\mathfrak p^3$, set $R_m=\mathcal O/\mathfrak p^{3m}$ and
  $E_m=(\alpha+\mathfrak p)\bmod\mathfrak p^{3m}$, $\alpha^3=-1\bmod\mathfrak p$.
  Then

  $$N_1=4,\qquad N_m=|P_4(E_m,E_m)|=22\,7^{3m-4}\quad(m\ge2).$$

  The support is exactly three full $\mathfrak p^3$-cosets and one full
  $\mathfrak p^4$-coset. Thus $N_2=1078$, $N_3=369754$, and
  $N_{m+1}=343N_m$ for $m\ge2$. Charging both input fractions gives
  $\Psi_1=4/7$, $\Psi_{m\ge2}=22/49$, and per-degree gain
  $\frac13\log(49/22)\approx0.2669259483$. Density improves once and stabilizes.
  This is not an optimum over arbitrary higher-level subsets. For $m\ge2$
  the quotient has characteristic $7^m$; the proof retains mixed-characteristic carries.

## Carrier and signed rate

**PROVED:** the $Q=1$ tower admits the growing same-input carrier

$$C_j=-1+\{u\in\mathfrak I_j:|\sigma_i(u)|\le X\},\qquad N(\mathfrak I_j)=7^{d_j/3}.$$

With the source root discriminant $D$ fixed before the degree limit,

$$a=\log X-\tfrac13\log7-\tfrac12\log D,\quad B=\log(2X+1),\quad
X=2\,7^{1/3}\sqrt D,\quad a=\log2.$$

The ideal-lattice translate-and-difference lower count assumes neither
bounded-box equidistribution nor surjectivity onto full local inputs.
The exact continuous width in the established growth range is
$W=81(X+1)^4+\frac32X+\frac{27}{16}$.
Uniform packing yields $|P_4(C_j,C_j)|\le U_m=N_m^{d_j/3}(1+W/7^m)^{d_j}$.
The fully charged certificate rates are

$$\kappa_1=\log\frac{X^2}{D(4/7)^{1/3}(W+7)}<0,$$
$$\kappa_m=\log\frac{X^2}{D(22/49)^{1/3}(W+7^m)}<0\qquad(m\ge2).$$

Both input ideal restrictions, discriminant, class count, and per-class packing
are paid. Translation is in $W$; this additive carrier has no hidden unit,
regulator, sign, multiplicity, branch, or omitted-output costs. Level two improves
the negative level-one rate in the chosen growth range; higher levels worsen it.
Saturation-ideal and mixed-depth rates are also negative. These are certificate
exponents, not actual-image exponents. The illustrative $D=7^{2/3}$ table does
not assert a tower attaining that discriminant floor.

## FAILED routes — exact scopes

| Route | Scope of failure |
| --- | --- |
| C0/C1 interval packing | Symmetric or exact full-interval fourth-power class certificates; C1 includes translated, unequal, and degree-dependent radii under its $Q\ge5$ hypotheses. Smaller realized support is outside the result. |
| C1 independent thinning | Coordinate-product split-prime input restrictions with both input costs and the same interval certificate; not the general correlated inequality. |
| C2 elementary hybrid counts | Interval enclosure, marginal-support multiplication, and displayed ratio/common-action parameter counts; not all hybrids or possible cross-support overlaps. |
| C2 determinant-7 density alone | The $208/343$ factor with stated full continuous intervals and uniform modulus packing: $U_{7Q}/|C|^2\ge[e^{-s_7}\rho_4Q]^d>1$, $s_7=\frac13\log(343/208)$. |
| C3 one-level optimization | No subset of the same 343-element ring improves the normalized two-input factor below $4/7$, for either sign; arbitrary higher-level subsets are outside the theorem. |
| C3 global certificates | Modulus-7 input engineering with full intervals and uniform class packing. For arbitrary local sets, the $Q=1$ comparison uses the volume-density budget; its stronger actual-population result concerns optimal critical cosets in equal-radius windows. The retained $Q>1$ branch also fails its stated certificate. |
| C4 deeper precision | The same full critical inverse images with full-interval rational-modulus packing for every fixed $m$; no additional density gain occurs after $m=2$. |
| C4 ideal-coset covers | Saturation, mixed-depth, and arbitrary finite 7-supported integral-ideal coset covers of the entire local product, assigning full continuous intervals to every branch and using uniform ideal-norm packing. Actual-population comparisons require the stated nontrivial equal-radius critical-coset carriers. |
| Weak deficits / collisions | These diagnostics alone do not give a sufficiently small all-output support upper bound. Weak M1-DEFICIT itself is PROVED. |

For C4's arbitrary complete-local-support covers,
$U_{\rm cover}/|C|^2\ge[81\,22^{1/3}/64]^d>3.54^d$.
Saturation and mixed envelopes exceed $4.24^d$ and $3.85^d$, respectively.
These are lower bounds on numerical envelopes divided by the pair budget,
not lower bounds on the actual image or sufficient improvement thresholds.
Proper subsets of globally realized branches, smaller branch-dependent real
regions, cross-factor correlations, and other carriers remain outside the
retirement. See [FAILURE_LIBRARY](../../FAILURE_LIBRARY.md).

## OPEN next obligation — recorded, not begun

Specify one concrete $C'_j\subseteq C_j$ with
$|C'_j|\ge e^{(a-\eta)d_j-o(d_j)}$, $0\le\eta<a$, and branches correlated
with real embeddings. Prove an all-pairs realized-support cover satisfying

$$\sum_\beta\prod_i\left(1+\frac{w_{j,\beta,i}}{N(J_{j,\beta})^{1/d_j}}\right)
\le e^{[2(a-\eta)-\varepsilon]d_j+o(d_j)}\quad(\varepsilon>0).$$

Include every branch, box, pair, input loss, multiplicity, distortion, and
exception. Equivalently $c_{\rm eff}<2(a-\eta)$; relative to
$c_{\rm base}=\frac13\log22+\log(1+W/7^{4/3})$, require
$g>c_{\rm base}-2a+2\eta$. No concrete carrier meeting this gate is in the record.
The old hybrid overlap screen is **CONDITIONAL**, pending a concrete overlap
source and positive fully charged rate. General M2-CORR is **OPEN**, while
its $p=5,d=2$ case is **PROVED**. See [OPEN_LEMMAS](../../OPEN_LEMMAS.md).

## Authority, corrections, and verification boundary

Controlling sources: `T02_C4_REVIEW_ACCEPTANCE_AND_HANDOFF(1).md`, Accepted state
and Handoff; `T02_CURRENT_STATE.md`, §§4–13, 17–20. Inspected supplements:
`C2_PRECISION_ADDENDUM.md`; `C2_C3_REVIEW_CHANGE_LOG.md`;
`Phase_C2_Hybrid_Carrier_Structural_Lemma.md`, §§3.2–3.3, 4.3, 5.3;
`Phase_C3_Ramified_7_Adic_Input_Cost.md`, §§6, 9;
`Phase_C4_Higher_Ramified_Precision.md`; and `C4_SIGNED_RATE_LEDGER.md`.

The seven C2 corrections preserve class/population separation, paid squared
units, certificate-only zero rate, scoped hybrid counting, general M2-CORR and
target OPEN statuses, and primitive-generator elimination. No additional unit
congruence selection is imposed; automatic square support at split primes is
not an input lower count or independent saving. C3 proves its $Q=1$ widths
directly without applying C1's $Q\ge5$ estimate.

**EXPERIMENTAL:** C3's finite screen covers structured parameter instances;
C4's exact checks cover levels 1–3, not full Cartesian enumeration at every
higher level. The universal and all-$m$ theorems are analytic. No computation
was rerun in migration. External C4 acceptance covered the PDF and C2–C3 change
log; prior companion reproduction remains internal evidence. External novelty
is unchecked. No T02 mathematical conflict was found; see
[MIGRATION_CONFLICTS](../../MIGRATION_CONFLICTS.md).

The earlier repository status below is preserved as **HISTORICAL / SUPERSEDED**.
Its unrecovered-C2 and next-C2 statements describe the earlier import, not the
latest accepted state.

<details>
<summary>HISTORICAL / SUPERSEDED — complete 5 September 2026 STATUS snapshot</summary>

# T02 status and history

**Ultimate quartic target: OPEN IN THE AVAILABLE RECORD.**
**Recent direction: C2 unit-times-additive carrier structural lemma.**

## Sequence of results

1. **2 September:** the task creates the C0 proof-search prompt and subsequently
   reviews a submitted family proof. The [original C0 report](../../history-sources/Phase_C0_Conjecture_Proof_Search.pdf),
   Theorem C1 and §§5–6, reports compression for integral
   $P_2=(ax+by)^2+cx+ey$ with $\gcd(a,b)=1$ and $ab(ae-bc)\ne0$.
   The exponent depends on the fixed family member.
2. The review requests corrections to “exact radius” wording, the scope of the
   unsuccessful quartic estimate, and formula formatting. The original report
   is preserved rather than relabeled as the corrected version.
3. **3 September:** the task prepares C1, reviews its submitted results, and
   records [two elementary roadmap corrections](../../notes/Phase_C1_Review_and_Next_Steps.md).
   C1's stated obstructions cover the specified interval/class methods,
   including translated and unequal-width windows; they are not lower bounds
   on the actual quartic image.
4. The task creates the [C2 prompt](../../prompts/Phase_C2_Hybrid_Carrier_Structural_Lemma_Prompt.md).
   Its requested structural lemma is the latest proposed work. No completed C2
   report was recovered.

## Preserve the corrections

- Weak M1-DEFICIT follows from the stated width estimates and trivial pair bound.
  A positive deficit relative to an oversized container is insufficient for the
  required rate.
- The M2-CORR case $p=5,d=2$ has the elementary small-set/large-set proof in the
  review. It is not the unresolved general correlated inequality.
- The original C0 report is available; its complete corrected version and the
  full C1 proof package remain missing. Their temporary paths in the old task
  no longer resolve.

## Next useful result

Prove one explicit gain for the correlated support in [SPEC.md](SPEC.md), with
every cost included. The recent task authorizes a prompt for that research;
preparing the prompt is not evidence that its mathematical objective was met.

## Status of the baseline

The source system reports and reviews the rank-one quadratic family as proved.
This history entry preserves that attributed status, while retaining the missing
corrected-proof dependency. The original theorem is a family extension of an
existing mechanism, not a new mechanism certified by this repository import.
External novelty has not been reverified here.

</details>

## 2026-09-20 source-recovery intake

The received T02 addendum and manifest identify the retained C1–C3 dependency
and review files omitted from the curated local selection and state that they
survive in a larger recovery package. Only the two Markdown recovery documents
were received here; absent originals are not treated as locally recovered.
Their item-level roles and hashes are preserved under
`local-only/migration/recovery_2026-09-20/T02/` and tracked by MC-06. The
documents retain the 10 September C4 handoff as the final mathematical state:
the fixed quartic target remains **OPEN**, and the scoped C2/C3/C4 failures are
unchanged.


## 2026-11-05 — archival cross-reference

The [public evidence index](../../EVIDENCE_INDEX.md) and [dated export](../../reports/2026-11-05-evidence-export/README.md) organize the source claims above. The publication pass checked locators, data packaging and archive integrity; it introduced no new proof, experiment or change to this track’s OPEN target.
