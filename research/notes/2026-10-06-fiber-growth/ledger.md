# Construction, signed-rate and failure ledger

6 October 2026 · version 1 · T03 · \(Q(x,y)=x^2+xy+y^2\).
This instantiates [the construction template](../../templates/CONSTRUCTION_LEDGER.md).
Only the two displayed amplitude rules were proposed.

## Claim identity and evidence

| Claim | Quantifiers / status | Proof and dependencies | Audit |
|---|---|---|---|
| FG-A1 | PROVED: unique index-two real subfield at every \(q=7^r,r\ge1\) | amplitudes.md §1; elementary cyclotomic/Eisenstein proof and supplied Eisenstein UFD | Lead and independent C |
| FG-A2 | PROVED: \(8q\) nonzero disjoint cosets for every \(r\ge0\) | amplitudes.md §2; sparse equality and norm separation | Lead and C |
| FG-A3 | PROVED: \(q^2/2\le n\le48q^2\) for \(r\ge1\) | amplitudes.md §3; involution and projection fibers | Lead and C |
| FG-A4 | PROVED: \(64\sqrt2 n^{1/2}\) uniform line bound | amplitudes.md §4; FG-A1/A3 and line/ellipse intersection | Lead and C |
| FG-A5 | PROVED: rich encoded sources number \(48q^2=\Theta(n)\) | amplitudes.md §5; exact decode and disjoint orbits | Lead and C |
| FG-F1 | PROVED: full-fiber cap \(48^2 32^4\) on at least \(n^2/18432\) sources eventually; actual image \(\Theta(n^2)\) | fibers.md §§5–6; seven-slot relation, all cross terms, generic-source count | Lead, independent A and C |
| FG-N1 | PROVED obstruction / FAILED rule: at most \(8q/7\) cosets at every \(r\ge1\) | fibers.md §§1–4; whole seventh-root product identity | Lead and C |
| FG-E1 | EXPERIMENTAL: exhaustive \(k=1,2\) full distributions | data.json; verification.md; inspected field arithmetic and independent norm reconstruction | Lead exact validation |
| FG-O1 | OPEN: classify exact 33-slot matchings for separated \(X,X\) sources | README.md §6; only a bounded target inventory is proved | No claim of four-target rigidity |

Every new record is version 1, dated 2026-10-06, on branch T03/ML-O1.
Hashes and source locators are in manifest.json. Reviews are internal
mathematical audits. No external theorem or novelty claim is added.

## Finalist 1 — all costs and rates

Fix scales 1 through 8 once; choose depth \(r\), then \(q=7^r,m=6q,t=8q\),
compatible roots and \(h(1+\omega\xi^j)\). There is no auxiliary extension,
random choice, parameter optimization, or scalar thinning.

| Gain/cost | Bound and units | Meaning / status |
|---|---|---|
| Formal scalar addresses | \(48q^2\) | Distinct complex orbit points are not counted as distinct scalars |
| Actual input | \(q^2/2\le n\le48q^2\) | PROVED; \(\log n=(2\log7)r+O(1)\) |
| Input thinning, both coordinates | None | All \(A_q^2\) is retained; restricting sources for a lower bound is not a construction thinning |
| Source projection multiplicity | At most 2 per \(X_{ab}\), hence 4 per ordered source pair | Charged twice in the obstruction |
| Target types / branches | \(48^2\) signed type/scale choices, \(32^4\) angular choices | Labels upper-bound targets; duplicates do not create genuine returns |
| Projective screen | \(\kappa=1/2,C=64\sqrt2\) | PROVED on completed scalars |
| Encoded return gain | \(6q=\Theta(n^{1/2})\) on only \(48q^2=\Theta(n)\) sources | Not a typical full-square gain |
| Stabilizers / origin | Free complex multiplication off zero; origin has one distinct target | No omitted stabilizer loss |
| Actual low-fiber population | At least \(n^2/18432\) sources with \(F_A\le C_*=48^2 32^4\) | Logarithmic return rate zero on a quadratic population |
| Source exceptions | At most \(3696q^3\) angular quadruples | Exact congruence union bound, not an exceptional tail for a successful construction |
| Field degree | \([K:\mathbb Q]=12\cdot7^{r-1}\), \([K^+:\mathbb Q]=6\cdot7^{r-1}\) | Growing; all relations proved uniformly at each depth |
| Local modulus / splitting | Coefficient blocks modulo \(q/7\); \(7=(3+\omega)(2-\omega)\) | Exact algebra, no prime-density or uniform residue-population assumption |
| Denominators | \(3A_q\subset\mathcal O_{K^+}\); \(\Delta^2=-3\) normalizes norms | Fixed invertible scaling preserves equality and fibers |
| Heights / archimedean size | Amplitude conjugates at most16; scalar conjugates at most \(32/\sqrt3\) | No volume or packing gain is claimed |
| Discriminant / regulator / class number / ideal index | Not evaluated; no lattice-volume, ideal-count or divisor estimate used | Inapplicable to this coefficient proof, not a favorable cost assumed zero |
| States / carries | Three scalar patterns, eight scales, two signs, all angular indices | All explicit; no independent-digit or hidden carry model |
| Entire output | \(n^2/(18432C_*)\le\lvert Q(A,A)\rvert\le n^2\) eventually | PROVED actual image, not a failed upper certificate alone |
| Input rates \(a,B\) | \(a=B=2\log7\) per depth \(r\) | Factor49 per level, with bounded logarithmic error |
| Output exponent | \(4\log7\) per depth \(r\) | Factor2401; upper and lower bounds |
| Signed gap | \(2a-4\log7=0\) | No positive fixed \(c\) |
| Requested \(\varepsilon,\delta\) | Every fixed positive pair fails for this carrier | Bad-tail lower bound \(n^2/18432\) eventually |
| Rectangular mismatch exponent \(\eta\) | Inapplicable | One common scalar set, no rectangular transfer |

All displayed constants are independent of depth. The logarithmic \(O(1)\)
errors are uniform because cardinality bounds have fixed prefactors.
For fixed \(\varepsilon,\delta,C'>0\), the contradiction begins once
\(n^\varepsilon>C_*\) and \(n^\delta>18432C'\).
No growth limit is borrowed from a historical dyadic construction.

## Finalist 2 — rejection before scalar or fiber inference

The exact rule
\[
b\prod_{a=0}^6(2-\xi^{j+a q/7})=b(128-\xi^{7j})
\]
has at most \(8q/7\) cosets. Seven pair labels already coincide before
real projection. Making that label map injective deletes at least six
sevenths of its pair labels; no scalar thinning bound is inferred.

All amplitudes are integral; the field is unchanged. Conjugate sizes are
at most \(8\cdot129\) at one step and \(8(2^{7^\ell}+1)\) after
\(1\le\ell\le r\) steps. No discriminant, regulator, class-number,
ideal, denominator, splitting-density or volume gain enters the equality
obstruction. The scalar rate, spreading, fiber rate, exceptional tail and
actual image of the deduplicated carrier remain unestablished here; they
are not assigned zero.

## Failure registry and stop

| Item | Status | Exact scope |
|---|---|---|
| Twisted-binomial fiber-growth carrier | FAILED IN STATED SCOPE | Actual image \(\Theta(n^2)\), independent of all possible action choices |
| Spreading as a sufficient certificate here | FAILED IN STATED SCOPE | This valid completed carrier passes spreading and has quadratic image |
| Relative-norm inventory | FAILED IN STATED SCOPE | Required \(8q\) disjoint cosets collapse to at most \(8q/7\); no image bound for its deduplicated completion follows |
| General ML-O1, DC-O1, T03, RC15/4 | OPEN | No universal no-go or target substitution |

Two candidate rules, two finalists, no post-selection mutations.
The initial ordinary-chord suggestion was a preliminary screen within
the first design; even counting its phase choice as a mutation uses only one.
No rejected rule was repaired and no third candidate was introduced.
The one retained diagnostic obligation is FG-O1 in README.md §6.
