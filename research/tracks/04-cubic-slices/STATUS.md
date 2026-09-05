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
