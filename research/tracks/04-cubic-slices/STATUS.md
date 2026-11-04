# T04 status — cubic slice / overlap program

Reconciled **11 September 2026**, cutoff **10 September**. **Fixed target: OPEN.**

$$P_-(x,y)=(x-y)^3-3(x+y).$$

The [SPEC](SPEC.md) is unchanged: one fixed positive exponent, arbitrarily large
finite real inputs, and the same set in both coordinates. Its exact slice
union remains useful. The latest selected candidate is a complementary-unit
affine system; input growth is PROVED and full-image compression is OPEN.
This does not replace T01's distinct plus-sign cubic.

**Authority:** `T04_CURRENT_STATE.md` and its latest affine proof/audit package:
`sacc_candidate_input.md`, `sacc_input_audit.md`, `sacc_pair_states.md`.
The older named `parity_twisted_cubic_checkpoint.md` (8 September) supplies the
fixed-base obstruction, not the latest affine state. See the
[source register](../../MIGRATION_CONFLICTS.md#source-registry).
`PROVED` records identified internal/frozen proofs; this migration did not
reprove them or establish external novelty.

## PROVED input theorem; OPEN full output

Let $\epsilon=2+\sqrt3$, $a_0=\sqrt3/2$, and

$$A_0=\{0\},\qquad A_{m+1}=(\epsilon A_m+a_0)
\cup(\epsilon^{-1}A_m-a_0).$$

Every branch history is legal. Scalars lie in the fixed fractional module
$\tfrac12\mathbb Z[\sqrt3]$; field degree and denominator stay fixed.
Different histories collide already at length three, so $2^m$ is a path
count, not the distinct-input count.

For $\Lambda>1$ satisfying $\Lambda^{-1}+\Lambda^{-3}+\Lambda^{-5}=1$,
and $\varphi=(1+\sqrt5)/2$, the independently audited source proves

$$\frac{\Lambda^{m-2}}{m+1}\le|A_m|\le2\varphi^4\varphi^m,\qquad
|A_m|=e^{a_*m+o(m)},$$

$$0.45116944438\ldots=\log\Lambda\le a_*\le
\log\varphi=0.48121182506\ldots.$$

The proof counts injective fixed-block-count classes and distinct affine maps;
it does not assume that all paths have distinct scalar values.

**OPEN:** the only certified full-image upper bound is

$$|P_-(A_m,A_m)|\le|A_m|^2=e^{2a_*m+o(m)}.$$

The certified gap is zero; the actual gap is unknown. This is not a proof
that the true output exponent equals $2a_*$, or a proof of cubic compression.
Sources: current state §4.9; candidate-input and input-audit notes.

## PROVED exact pair evolution; missing output count

In $u=X-Y$, $s=X+Y$, the four branch pairs are, for $\sigma=\pm1$:

$$\begin{array}{lll}
\text{same signs:}&u'=(2+\sigma\sqrt3)u,&s'=(2+\sigma\sqrt3)s+\sigma\sqrt3,\\
\text{opposite signs:}&u'=2u+\sigma\sqrt3(s+1),&s'=\sigma\sqrt3u+2s.
\end{array}$$

The output is $u'^3-3s'$. The ten monomials of degree at most three form
an invariant linear observable space, but their scalar values are unbounded.
Ten coordinates do not certify ten finite output states.
Source: `sacc_pair_states.md`; current state §4.9.

**OPEN — selected T04-O1:** determine whether
$\limsup_m m^{-1}\log|P_-(A_m,A_m)|<2a_*$.
A sufficient construction would encode every ordered pair with at most
$K_0(m+1)^B\kappa^m$ labels, fixed $K_0,B<\infty$, $\kappa<\Lambda^2$,
where equal labels imply equal scalar outputs after all carries/relations.
**CONDITIONAL:** every $c_-<2-\log\kappa/\log\Lambda$ would work.
No such encoding is supplied. Source: current state §§13–14.

## Retained PROVED results and scoped FAILED routes

**PROVED:** the quadratic benchmark $(x-y)^2+5(x+y)$ has a same-set small-image
construction. Common affine input changes and univariate postcomposition
preserve its support bound, giving an even-degree companion such as $R^2+R$.
That companion is neither this cubic nor T02's quartic.

**PROVED — exact self-similar local theorem:** the final self-similar report
settles the $2{:}3$ family $M_t=q^{3t}r^{3t}$,
$C_t=q^{2t}r^{2t}$ for fixed distinct odd primes. It does not settle general
BP2+ or arbitrary residual critical-cell unions. Earlier OPEN wording for
exact SS-BP is superseded. Product-tree attribution remains a source issue.

Every FAILED row below has only the indicated scope. The complete local and
construction failure tables are retained in [FAILURE_LIBRARY](../../FAILURE_LIBRARY.md).

| Route | Exact scope of failure |
|---|---|
| Quadratic transfer, $q\equiv5\pmod{12}$ | The specified $T=Q/8$ witness is exactly cubic pair-injective: $|P_-(A,A)|=|A|^2$ |
| Complementary transfer, $q\equiv1\pmod{12}$ | The successful quadratic $T=Q/8$ witness has cubic image at least $|A|^2/(1+e^{-\delta d})$, fixed $\delta>0$; other windows/carriers are outside this conclusion |
| Direct residue/interval certificates | The stated constant cube-density, full-prime-power/ordinary-ball, and full continuous packing estimates fail after costs; not every correlated mechanism |
| Local tensor/tree/address certificates | Abstract same-set or unary tensorization, static coarea, mass-only recursion, maximal cube-class functional, translation addresses, and the same anchored weight beyond $2{:}3$ fail separately; these are not general BP2+ counterexamples |
| Selected translations and rich fibers | Fixed-difference slices are anchor-injective; a fixed positive fraction of rich pairs leaves an uncontrolled quadratic tail |
| Explicit rich-fiber family | $A_N=\{36i_j^3+3i_j+2,36i_j^3-3i_j+2:1\le j\le N\}$, with the checkpoint's finite-avoidance/CRT choices, has $2N$ inputs and $4N^2-N+1$ outputs; not a theorem about arbitrary rich-fiber sets |
| Pre-trace product compression | Nonzero products of the specified $\alpha$ carrier have fibers at most 72; trace fibers are a separate problem |
| Rational CTC subclasses | Fixed/low multiplicative rank, separated exponent codes, prime-ratio and independent-field constructions, and fixed rational Möbius intervals under source hypotheses; unrestricted correlated trace compression remains OPEN |
| Rational symmetry orbits | The trace-preserving rational group has order at most 3024; neither arbitrary points nor uniform fiber sizes follow |
| Fixed algebraic regular digits | Fixed real algebraic base $\lambda\notin\{0,\pm1\}$, finite algebraic alphabet, fixed graph with $V$ vertices: image at least $c(m+1)^{-2V}|A_m|^2$. Positive scalar entropy excludes a fixed saving; unequal edge multipliers are outside the theorem |
| Formal tensor/scalar lifts | Specified nilpotent or split-algebra models lack faithful real scalar embeddings; their canonical restored cubic tail recovers pairs. This does not exclude all tailored field lifts |
| Current unit walk restrictions | Uniformly sublinear excursions have $|A_m|\le Cm^2(R+1)^2\epsilon^R=e^{o(m)}$ for $R=o(m)$; fixed zero-drift block alphabets grow only polynomially. The unrestricted graph remains OPEN |
| Norm factorization / scalar semiconjugacy | Specified polynomial norm-factorization and scalar affine identities fail; rational norm/trace parametrizations or richer observables are not excluded |
| Ambient containers | Failed continuous/Minkowski enclosing counts are not lower bounds on occupied sparse arithmetic outputs |

Sources: current state §§4–6 and the named final checkpoints in its §10.
The original two transfer proofs and full previous STATUS remain below.

## OPEN alternatives and evidence limits

Besides selected T04-O1, the historical alternatives remain OPEN:
unrestricted inverse-symmetric rational correlated trace compression (O2),
arbitrary deep two-prime polarized BP2+ (O3), and unions of full residual
critical cells at $q^{4t}r^{3t}$ with coefficient $-3q^{2t}r^{2t}$ (O4).
Their exact quantifiers are in [OPEN_LEMMAS](../../OPEN_LEMMAS.md).
No historical alternative is started by this migration.

**EXPERIMENTAL:** the recorded depth-12 affine test has 1,030 distinct inputs,
1,058,120 outputs, 1,060,900 ordered pairs, and maximum observed fiber 8.
Finite data prove no asymptotic gap. The available input-growth JSON stops
at depth 24; the candidate-input note's depth-30 provenance remains unverified here.
No computations were rerun.

**OPEN provenance:** the residual report's attribution of the product-tree
inequality to the supplied sum-product construction conflicts with the
recoverable internal proof in `three_prime_cubic_crt_checkpoint.md`, §D.5.
The malformed complementary-transfer display and older corrupted address note
remain unchanged. See [MIGRATION_CONFLICTS](../../MIGRATION_CONFLICTS.md).

Phase A/B/C0 and the latest general-quadratic addition/multiplication,
norm/trace, and solvable-extension direction remain shared progress. Neither
input growth nor that direction solves this fixed cubic; no novelty is claimed.

<details>
<summary>HISTORICAL / SUPERSEDED — complete 5 September 2026 STATUS snapshot</summary>

# T04 status and history

**Ultimate cubic target: OPEN IN THE AVAILABLE RECORD.**
**Recent direction: direct construction of overlapping cubic slices.**

## Sequence of results

1. [The positive-polynomial checkpoint](../../history-sources/positive_polynomial_phase_checkpoint.md),
   §§A, G–I, records inheritance from the seed $R$ under common affine input
   change and univariate postcomposition. Its companion $R^2+R$ has degree four;
   this does not solve $P_-$ or T02's different quartic.
2. [The quadratic-to-cubic checkpoint](../../history-sources/quadratic_to_cubic_transfer_checkpoint.md),
   main conclusion and §D, analyzes a specific witness with primes
   $q\equiv5\pmod{12}$, $Q=\prod q$, and radius $T=Q/8$. It reports
   $$|R(A_j,A_j)|\le|A_j|^{2-c_0},\qquad
   |P_-(A_j,A_j)|=|A_j|^2.$$
   Cubing recovers the difference modulo $Q$, and the narrow window supplies a
   unique lift. The source also proves injectivity inside each exact quadratic
   output fiber under its stated witness hypotheses.
3. [The complementary-prime checkpoint](../../history-sources/complementary_prime_transfer_obstruction.md),
   §§B, G–H, tests $q\equiv1\pmod{12}$ at the same radius. For successful
   quadratic parameters it reports a fixed $\delta>0$ with
   $$|P_-(A_j,A_j)|\ge
   \frac{|A_j|^2}{1+e^{-\delta n_j}}.$$
   Its explanation uses the stronger $Q^2$ collision congruence and positivity
   of $d^2+de+e^2$ to limit actual lifts.
4. The recent 3 September continuation closes these two transfer tests and
   prioritizes the direct slice union in [SPEC.md](SPEC.md).

These are attributed checkpoint results, not a fresh audit of the imported
field-tower and packing lemmas.

## Exact scope of the closed route

The conclusions concern the two analyzed congruence regimes and the specified
$T=Q/8$ witness. They do not rule out every choice of prime/window, every possible
quadratic witness, or the existence of favorable sets for $P_-$ itself. Historical
phrases such as “the transfer strategy is closed” must be read at that scope.

Earlier [self-similar](../../history-sources/self_similar_cubic_checkpoint.md)
and [residual-critical](../../history-sources/residual_double_critical_cubic_checkpoint.md)
checkpoints remain in the archive for their exact model assumptions; the current
task does not reopen them automatically.

## Next useful result

Construct systematic cross-slice overlap that survives the all-pairs count.
An explicit smaller support or a covering theorem controlling every slice could
qualify. Restating the desired image bound as “large average overlap” without a
mechanism is not new progress. No direct construction meeting the target was
present in the recent task.

</details>

## 2026-09-20 source-recovery intake

The received T04 recovery note and manifest confirm the repository designation
of the current state plus three SACC notes as the final recoverable affine
package. They identify the already local tower PDF locators, while retaining
the product-tree attribution uncertainty, missing early one-/two-prime proof
originals, and absent depth-30 execution evidence. The larger source archive
and additional addenda named by the manifest were not received. The two
documents are preserved under `local-only/migration/recovery_2026-09-20/T04/`;
MC-02, MC-04, MC-05 and MC-06 record the remaining boundaries. The fixed cubic
target and full-output gap remain **OPEN**.
