# Lift ledger and failure registry

30 September 2026 · T03 · version 1. This ledger follows the repository
[construction template](../../templates/CONSTRUCTION_LEDGER.md). All claims
refer to the explicit hypotheses and proofs in [proofs.md](proofs.md).
The fixed polynomial is always $x^2+xy+y^2$ over real inputs. The user
commissioned only the strictly offline $7^k$ lift route. No broad carrier
search, external input or novelty claim occurs.

## Five requested architectures and the tested scopes

| Architecture | Exact definition / gate | Result and precise boundary |
|---|---|---|
| A: separated digits | Digits 0–6, weights $217^{3^i}$ | ML-3: injective input encoding but every complete Q-fiber has at most 2401 points. The modular equalities cannot all survive. This applies the retained faithful-Gram mechanism rather than re-scouting it. |
| B: algebraic scalar digits | Arbitrary real map preserving all $(x,x)\mapsto(x,-2x)$ equalities; separately exact additive cyclic carry rules | ML-2 gives at most $k+1$ scalar values; full additive carries give only zero. Partial/nonadditive encodings outside these hypotheses remain OPEN. |
| C: paired orbit encoding | Formula (9), free modular orbits, root-of-unity action and independent algebraic radius tags | ML-4: exact identity and distinctness PROVED, full Cartesian return tail FAILED. Full-fiber bound separately disproves power saving for this explicit completion. |
| D: carry-state cover | Equivariant finite cover with at most s states above a modular pair, injective nonzero encoding, faithful group action | ML-5: preserving all but $O(n^{2-\delta})$ base pairs requires $s=\Omega(n^{\delta/2})$. Subpolynomial states fail in this scope; affordable polynomial states are not ruled out. |
| E: modular restriction | Restrict both scalar coordinates to units; density $6/7$ per coordinate | Modular returns remain at least $m/3$, with no state-stabilizer cost. There is no resulting dense real Cartesian lift here. This is a proved escape from ML-5, not a completed positive construction. |

No unproved architecture was scouted. Only the paired encoding passed the
exact-identity gate and received two predetermined local checks. The
naive integer lift and old rational-torsion obstruction were retained as
context, not reproved or rerun. Generic denominator carriers, independent
rotations, balanced words, moving poles, old cube-root carriers and broad
prime searches were not reopened.

## Paired lift: full gain and cost accounting

Fix $k\ge1$ and then set all other parameters by the formulas in ML-4.
There is no optimization after k grows. Here $n=7^k$, $m=6n/7$,
$t=8n/7$, $q=3n/7-1$, $N=1+tq$, $D=m(2t+1)+1$.

| Quantity / required cost | Exact bound or reason | Status |
|---|---|---|
| Original modular scalar count | n exactly | PROVED, frozen MG-2 |
| Original modular ordered pairs | $n^2$ | PROVED |
| Base restriction | Primitive plane $tm=(48/49)n^2$; discarded $n^2/49$ is a constant fraction, **not** a negligible exceptional set | PROVED |
| Both-coordinate thinning alternative | Unit restriction has $6n/7$ scalars and $(36/49)n^2$ pairs; it retains at least m/3 modular returns per pair | PROVED ML-5; no unproved real transfer credited |
| Actual paired projection | One-to-one on all tm primitive points, by unique orbit labels and independent radii | PROVED |
| Scalar inputs after completion | $N=1+tq=(24/49)n^2-(8/7)n+1$, both lower and upper counts exact | PROVED |
| Same-set cost | $X=Y=A$; symmetric difference exactly zero; choose any positive eta | PROVED |
| Action labels / actual actions | m labels, m distinct real rotations, exact group law | PROVED |
| Returned pairs on encoded E | m distinct targets at each of tm points, no nonzero stabilizer | PROVED |
| Zero | One actual target; m returning labels at the origin | PROVED, retained in every histogram |
| Engineered coverage | $tm/N^2=\Theta(N^{-1})$; all other Cartesian pairs remain in the accounting | PROVED |
| Cross-shell exceptional population | $t(t-1)q^2=N^2-O(N^{3/2})$ has selected R=2 and complete fiber size 4 | PROVED |
| Nonzero scalar labels | t disjoint shells of q nonzero elements; zero alone is shared | PROVED |
| Field and projection | $K=\mathbb Q(\zeta_m)$, $\theta=2^{1/D}>0$; $[K:\mathbb Q]\le m$, $D/m<[K(\theta):K]\le D$ | PROVED |
| Total degree bound | $[K(\theta):\mathbb Q]\le mD=O(n^3)$; input field is a real subfield of this complex field, not asserted totally real | PROVED |
| Discriminant / root discriminant | No lattice-counting or discriminant estimate used; no favorable zero cost assumed | Inapplicable to the exact counting proof |
| Scalar denominators | None: the scaling by 3 in (9) makes coordinates (11) algebraic integers | PROVED |
| Action coefficients | The real matrix coefficients lie in K; denominators divide 3 by the recovery formulas | PROVED; no denominator membership is assumed |
| Heights / archimedean size | Every conjugate of each scalar has absolute value at most $2\sqrt3\,2^{t/D}<4$; every action conjugate has modulus one | PROVED: conjugates permute the roots of unity and preserve the modulus of theta |
| Ideals, class number, regulator | No principal-ideal count, unit theorem, regulator or class-number estimate used | Inapplicable to this construction |
| Local modulus / exceptional primes | Only $7^k$; root-of-unity period m. Eisenstein at 2 proves radical degree; no selected-prime density estimate | PROVED |
| Input logarithmic rate | $\log N=2k\log7+O(1)$ | PROVED |
| Rich-subset return rate | $\log m=k\log7+O(1)=\tfrac12\log N+O(1)$ | PROVED only on E |
| Typical return rate | $\log R=\log2$ on $N^2-O(N^{3/2})$ pairs; actual all-action count there at most 4 | PROVED |
| Bad-set exponent | Full exponent 2 in N, for every fixed positive threshold exponent | PROVED |
| Full image | $\lvert Q(A,A)\rvert\ge N^2/4-O(N^{3/2})$ | PROVED independently from full fibers |
| Signed gate | Typical return exponent 0; no positive exceptional deficit; DC-R1 supplies no c>0 | FAILED in this family |

The bounded conjugate claim follows from the explicit sine expressions
for both projections, valid at every cyclotomic embedding; conjugates
of theta differ only by roots of unity. It provides no support saving:
field degree and coefficient relations still distinguish the outputs.
No cost is compensated by an unproved volume estimate.

## Other scope-specific rate deficits

**Scalar all-return encoding.** ML-2 collapses each unit valuation class;
$N\le k+1$ rather than $n=7^k$. The unit-square source labels all become
one pair. The modular return exponent cannot be transferred through this
projection by treating labels as targets. No theorem on all possible
small projected image families is asserted.

**Separated digit carrier.** $\log N=k\log7$, but all actual return
fibers are at most 2401, and every pair eventually lies below $N^\varepsilon$.
The input projection is injective; output coefficient retention, not
input collapse, kills compression. Heights satisfy
$\log\max A=O(3^k)$; no height-based bound is needed for the conclusion.
These inputs are integers, with field degree one and no ideal or
regulator cost. All branches and all pairs are covered by the Gram proof.

**Subpolynomial state cover.** ML-5 measures exception size in the base
modular size n. If $N=n^{O(1)}$ and $s=N^{o(1)}$, then the lost base
population is at least $n^{2-o(1)}$. Polynomial state cost can in
principle be affordable; there is no assertion that (21) alone erases
every possible positive rate. Thinning to unit scalar coordinates is
an explicitly stated escape. A full real Cartesian count is still missing.

## Failure registry and remaining scope

- **ML-F1 / FAILED injective full scalar lift:** preserving only all diagonal
  returns of the modular order-three action already gives $N\le k+1$.
- **ML-F2 / FAILED faithful separated digits:** complete real fibers are
  uniformly bounded by 2401 for the explicit fixed digit alphabet.
- **ML-F3 / FAILED separated-radius completion:** exact paired lifting works,
  but almost every Cartesian pair has full fiber four. This includes an
  actual-image obstruction for this newly specified family only.
- **ML-F4 / FAILED subpolynomial state cover:** exact hypotheses of ML-5,
  faithful homomorphic actions and bounded fibers over nearly all base
  pairs. Nonfaithful, partial and sufficiently large state systems remain
  outside its conclusion.

**Cycle verdict: EXACT LIFT GO / TAIL FAIL.** The general modular-to-real
route is not disproved. DC-O1, the real Q target, ARG/TCRC and RC15/4
remain OPEN. HR-N1 remains DISPROVED in its separate frozen scope.
The one next obligation is the coordinate-reusing paired lift in the
main report; no broad replacement program is adopted.
