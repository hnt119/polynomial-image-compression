# Phase C0 independent referee report

## Verdict

**PROVED WITHIN THE OFFLINE SOURCE SYSTEM.** The explicit theorem for

\[
P(x,y)=(x+2y)^2+3x-y
\]

survives independent reconstruction and every required adversarial check.
There is no route-invalidating gap and no hidden additional assumption beyond
the inspected supplied field theorem.

## Severity-ranked objections

### 1. Broader nonspecial family needed one extra hypothesis

The phrase “primitive `L` and transverse `M`” would be false as a general
nonspecialness criterion: `L=x`, `M=y` gives `x^2+y`, an additive form.

**Disposition:** statement-refuting only for that overbroad wording.
**Repair applied:** Theorem C1 requires `ab != 0` and `ae-bc != 0`. The
explicit polynomial already satisfies these conditions.

### 2. Nonspecialness required a full degree audit

**Disposition:** resolved by proof. In the additive case, linear outer `g`
has no mixed term; otherwise degree forces quadratic `g` and affine `u,v`,
making the linear part parallel to the square direction. In the
multiplicative case, total degree forces `g,u,v` all linear and hence a
quadratic part proportional to `xy`.

### 3. Field supply could not be silently strengthened

**Disposition:** resolved by direct source inspection. Proposition 3.8 of the
supplied unit-distance proof gives one fixed finite set of `t` completely
split primes in every layer of a fixed tower for each fixed `ell`. The proof
uses exactly those primes and jointly charges `D(ell)`. No arbitrary
prescribed prime and no infinite split set is required.

### 4. Exact and conservative rate factors had to stay distinct

**Disposition:** resolved by bookkeeping. The explicit factor is

\[
\Theta(X)=D\rho\left(18+\frac{8Q}{X}+\frac{Q}{X^2}\right),
\]

whereas the family proof may use the conservative `theta=C_P D rho`. Each
exponent is defined from its own factor.

### 5. The extension claim needed a precise equivalence relation

**Disposition:** resolved. The report claims non-equivalence only under a
common invertible affine input map, an invertible affine output map, and an
optional variable swap. It makes no claim about unrestricted affine maps of
the input plane.

## Required Section 8 checks

| Check | Finding | Disposition |
|---|---|---|
| Fixed polynomial and exponent | All finite parameters are fixed before tower degree varies | Resolved |
| Cartesian square | Same scalar input map in both coordinates | Resolved |
| Fibers | Field embedding and scalar maps are injective | Resolved |
| Special forms | Both excluded by complete degree proofs | Resolved |
| Reductions | Integral coefficients; selected primes odd; no denominator issue | Resolved |
| Same field family | Proposition 3.8 supplies every selected prime in every layer | Resolved |
| Local images | Exact square count includes zero | Resolved |
| CRT | Pairwise comaximal factors and complete splitting | Resolved |
| All conjugates | `M=9X^2+4QX` holds at every real embedding | Resolved |
| Uniform class count | Norm separation; no equidistribution | Resolved |
| Centered carrier | Translated half-box followed by differences | Resolved |
| All costs | Discriminant, modulus, coefficients, and scale appear in the rate | Resolved |
| Positive rate | `t~ell^2` beats `log D=O(ell log ell)` before `d->infinity` | Resolved |
| Exponent direction | Input upper bound is used before inversion | Resolved |
| Strength | Only an unbounded sequence and member-dependent exponent are claimed | Resolved |

## F1-F10 audit

- F1: no collision-energy inference; full support is counted.
- F2: no unconditional hybrid separation.
- F3: every coordinate map has fiber one.
- F4: quadratic shape and local sparsity are both used.
- F5: the signed rate is positive before dimension tends to infinity.
- F6: allowed classes are multiplied by a worst-case per-class count.
- F7: every selected prime is completely split.
- F8: all arithmetic and archimedean costs remain in the rate.
- F9: `Q` is fixed, and the proof returns to one fixed polynomial.
- F10: the failed `xy(x+y)` route is not retried.

## Final referee classification

- Main theorem: **PROVED WITHIN THE OFFLINE SOURCE SYSTEM**.
- External novelty: not checked.
- Route-invalidating objections: none.
- Repairs applied: complete nonspecialness degree proof, `ab != 0` in the
  family theorem, precise Proposition 3.8 citation, distinct rate notation,
  and a scoped same-set equivalence claim.
