# FAILURE_LIBRARY_B

## Cycle 1 failures retained

### F1. Collision energy as a sufficient certificate

- **Why plausible:** Cauchy-Schwarz relates image size and energy.
- **Failure:** \(|F(A,A)|\ge|A|^4/E_F(A)\) is a lower bound; heavy fibers can coexist with a long light tail.
- **Type:** structural/logical.
- **Mutation:** require full support or tail-complete container control.

### F2. Unconditional hybrid separation

- **Why plausible:** exact separation holds for multiplication on \(A=GP\).
- **Failure:** \(xy(x+y)\) produces two coupled action-carrier terms.
- **Type:** algebraic and quantitative.
- **Mutation:** rank-two correlated-sum analysis.

### F3. Coordinate changes without fiber bookkeeping

- **Failure:** many-to-one maps can manufacture fake compression.
- **Type:** structural.
- **Mutation:** record domain, fibers, and preserved operations.

### F4. Generic bounded coordinates imply compression

- **Failure:** a degree-\(m\) polynomial costs \(X^{md}\), which can consume the \(X^{2d}\) two-input budget.
- **Type:** quantitative.
- **Mutation:** exploit exact structure or local sparsity first.

### F5. Dimension automatically helps

- **Failure:** dimension exponentiates costs as well as gains.
- **Type:** quantitative.
- **Mutation:** require a positive signed rate before sending \(d\to\infty\).

## Cycle 2 failures

### F6. Residue density times total box count

- **Proposed mechanism:** multiply the density of allowed residue classes by the total number of points in an archimedean region.
- **Why plausible:** it resembles uniform distribution.
- **Precise failure:** the region's points may be concentrated entirely in the allowed classes. Density alone gives no proportional saving.
- **Type:** structural/logical.
- **Mutation:** prove a uniform per-residue-class packing bound, as in Pohoata's Lemma 3.3.

### F7. Nonsplit primes give degree-many restrictions

- **Proposed mechanism:** any rational prime produces \(d\) local coordinates in a degree-\(d\) field.
- **Precise failure:** the number of coordinates is the number of prime ideals above \(p\), not automatically \(d\). An inert prime gives only one residue field.
- **Type:** algebraic.
- **Mutation:** require complete splitting, residue degree one, and pairwise comaximal factors.

### F8. Local sparsity alone proves global compression

- **Precise failure:** coefficient height, modulus, output radius, and discriminant can erase the \(\rho^d\) gain.
- **Type:** quantitative.
- **Mutation:** test
  \[
  \rho D\left(2H X^{m-2}+R/X^2\right)<1.
  \]

### F9. A varying auxiliary polynomial solves a fixed-polynomial problem

- **Precise failure:** allowing \(Q\) to grow with \(|A|\) changes the polynomial.
- **Type:** structural.
- **Mutation:** fix \(Q\) before \(d\to\infty\) and prove a cardinality-preserving rescaling identity.

### F10. The polynomial \(xy(x+y)\) has a reusable sparse local image

- **Why plausible:** its homogeneity leaves only three cube classes when \(p\equiv1\pmod3\).
- **Precise failure:** the ratio parameter \(r(1+r)\) hits every cube class for all \(p\equiv1\pmod3\), \(p\ge13\); for \(p\equiv2\pmod3\), cube scaling is already transitive. The only odd exception is \(p=7\), where the density is \(5/7\).
- **Type:** structural and quantitative.
- **Mutation:** none currently validated; prime powers or specially prescribed towers remain open tests.
