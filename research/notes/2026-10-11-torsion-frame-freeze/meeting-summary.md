# T01 torsion/frame cycle: one-page meeting summary

T01 · 11 October 2026 · documentation freeze, version 1.

## T01: what the torsion/frame cycle settles

**PROVED in the supplied source system:** T = R<sub>2</sub> - R<sub>1</sub> has infinite order. **TC-O1 is resolved. T01 remains OPEN.**

R<sub>1</sub> and R<sub>2</sub> are the positive-Y marked points of the exact two-width, six-scalar attachment. The fixed target is P(x,y) = (x-y)³+x+y. We still seek arbitrarily large finite real A and a fixed ε > 0 with |P(A,A)| ≤ |A|<sup>2-ε</sup>, counting every ordered pair of the same set.

### The geometric distinction

**Genus** counts handles of a smooth compact complex curve. A **cover** is a finite map; a **branch point** is where its sheets merge. An **isogeny** is a finite-degree elliptic group homomorphism, unbranched in characteristic zero.

**PROVED / TC-G1-G2.** The genus-one sharing equation u³-v³+u-v = c supplies one common column. A complete frame with the same ordered outputs also requires 3d²+ℓ² = 4 and 2d³-4d+c = 0, where d = u-v and ℓ = u+v. The cubic has at most two admissible positive widths: at most four marked points, paired by column exchange.

**PROVED / TC-G4.** Completing one row requires W<sub>cov</sub>² = 4-3u². Six simple branch points give genus four; a degree-e isogeny pullback gives genus 1+3e. Riemann-Hurwitz excludes the stated rational elliptic completion. This does not exclude isolated real lifts, and that completion need not keep the second output.

### The finite attachment and the whole square

**PROVED / TC-G5:** N = 6 scalars, Q = 8 controlled pairs, Z = 2 controlled outputs, B = N²-Q = 28. Hence |P(A,A)| ≤ Z+B = 30. **EXPERIMENTAL / TC-X1, exact finite audit:** the actual image is 30, with two size-4 fibers and 28 singleton fibers. Two rich fibers do not control the remaining pairs.

### Why the arithmetic certificate covers every order

A **valuation** v<sub>23</sub> counts powers of 23. **Good reduction** means the integral curve stays nonsingular modulo 23. A **formal logarithm** turns group addition near the identity into ordinary addition, detecting nonzero points there as non-torsion.

\[
T+\sigma(T)=2R_2,\quad v_{23}(Y(2R_2))=1,\quad v_{23}(X(4R_2))=-2.
\]

**PROVED / MS-C1.** With a = √2, H = √((3+a)/14), W = √(4a-3), all roots positive, L = Q(a,H,W) has degree eight. The automorphism σ fixes a,H and negates W. The embedding Q(a,H) → Q<sub>23</sub> with a ≡ 18, H ≡ 6 has good reduction. The supplied local logarithm lemma makes R<sub>2</sub> infinite order; the conjugation identity then does the same for T.

**Meeting conclusion.** Infinite order gives infinitely many distinct real elliptic multiples, not infinitely many admissible frames: the fixed-output locus still has at most four points. The marked torsion question, fixed-output width classification and stated rational elliptic completion obstruction are settled in scope. The cubic saving remains open. Sources: TC-G1/G2/G4/G5, TC-X1, MS-C1 and its saved referee appendix. This is a documentation freeze, with no new search, proof audit, experiment or next task.
