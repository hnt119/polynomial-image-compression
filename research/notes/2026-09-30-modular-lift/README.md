# Bottom line

- **Tested:** separated digits, algebraic scalar carries, an explicit paired orbit lift, carry-state covers, and restriction to modular units.
- **Exact Q-preservation: achieved on every primitive modular orbit.** The paired algebraic encoding retains all $6\cdot7^{k-1}$ distinct actions and all their distinct orbit targets.
- **The modular tail does not survive Cartesian completion.** Almost every completed pair has only two selected returns and exactly four equal-Q targets in the entire square.
- **Real typical return exponent: zero** for this explicit completion, despite exponent $1/2$ on its sparse encoded subset. The scalar all-return lift separately collapses to at most $k+1$ values.
- **DC-R1 gives no positive c.** DC-O1, RC15/4 and the general real quadratic target remain OPEN.
- **One next obligation:** an exact paired lift with algebraically related radii/phases that reuses scalar coordinates and supplies the missing cross-orbit returns.

## EXACT LIFT GO / TAIL FAIL

$$\boxed{\text{good modular tail}
\xrightarrow[\text{primitive orbits}]{\mathrm{PROVED}}\text{exact lift}
\xrightarrow[\text{encoded pairs}]{\mathrm{PROVED}}\text{genuine real returns}
\xrightarrow[\text{Cartesian completion}]{\mathrm{FAILED}}\text{DC-O1}
\xrightarrow[\text{if hypotheses hold}]{\mathrm{PROVED}}\text{power saving}.}$$

**30 September 2026 · T03 · strictly offline.** Fixed polynomial
$Q(x,y)=x^2+xy+y^2$. The [previous modular theorem](../2026-09-21-return-tail/modular-gadget.md)
is used as frozen input. The long proofs and precise failure scopes are
in [proofs.md](proofs.md); the complete arithmetic and rate audit is in
[ledger.md](ledger.md). No external result or novelty claim is added.

## 1. Carry error and direct scalar lifting

### Statement

**PROVED — ML-1/ML-2.** Write $n=7^k$, and let $(v,w)$ be integer
representatives of a modular return of $(x,y)$. Put
$e=(Q(v,w)-Q(x,y))/n$. For target carries a,b,

$$Q(v+na,w+nb)-Q(x,y)
=n\{e+(2v+w)a+(v+2w)b+n(a^2+ab+b^2)\}.$$

The braces must vanish exactly. A general scalar map $f:R_k\to\mathbb R$
satisfying all the modular diagonal-return equalities

$$Q(f(x),f(x))=Q(f(x),f(-2x))$$

must satisfy

$$\boxed{|f(R_k)|\le k+1.}$$

### Meaning

The first-order and quadratic carries depend on actual representatives,
not just the norm residue. Even without assuming additivity, the diagonal
equalities force f to be constant on each 7-adic valuation class.

### Consequence

An injective scalar lift preserving all modular returns is impossible.
This does not exclude partial lifts that omit these constraints. Exact
additive cyclic carry relations collapse completely; the proposed
separated-digit alternative instead has real Q-fibers of size at most
2401. Their precise hypotheses are in ML-2/ML-3.

## 2. A genuine paired algebraic lift

### Statement

**PROVED — ML-4.** Put

$$m=6\cdot7^{k-1},\quad t=8\cdot7^{k-1},\quad
D=m(2t+1)+1,\quad\theta=2^{1/D},\quad\zeta=e^{2\pi i/m}.$$

The primitive modular plane has t free orbits of size m. Label their
representatives $p_j$ canonically and write each point uniquely as
$T_{(-2)^r}p_j$. Define

$$F(T_{(-2)^r}p_j)=3\theta^j\zeta^r.$$

Then $F(T_h p)=\rho(h)F(p)$ for the faithful rotation action
$\rho((-2)^r)=\zeta^r$. Decode $F(p)=X(p)-\omega Y(p)$ with real
algebraic coordinates. Every encoded orbit has exactly m distinct
Q-preserving returns, and F is injective on the primitive plane.

Let S be the common coordinate projection of the orbit $3\mu_m$.
Then $|S|=m/2$, $0\in S=-S$, and the explicit completion is

$$A=X=Y=\bigcup_{j=1}^t\theta^jS,\qquad
\boxed{N=|A|=1+t(m/2-1)=\Theta(7^{2k}).}$$

### Meaning

This construction realizes the modular group action exactly in
characteristic zero. It preserves equality along modular orbits; it is
not an entrywise reduction section or a preservation of the numerical
residue norm. The primitive restriction discards a constant 1/49 of the
modular plane, which is explicitly charged rather than called negligible.

### Consequence

The exact-identity and distinct-target gates pass. The encoded tm rich
pairs occupy only $\Theta(N^{-1})$ of the completed square, so this
alone does not establish the required real return tail.

## 3. The decisive completion obstruction

### Statement

**PROVED — ML-4.** Set $q=m/2-1$. The cross-shell population has size

$$C_k=t(t-1)q^2=N^2-O(N^{3/2}).$$

Every such pair has exactly two returns under the lifted group and
exactly four targets in its full real Q-fiber. Consequently

$$B_\varepsilon\ge C_k\quad\text{eventually for every fixed }\varepsilon>0,$$
$$\boxed{|Q(A,A)|\ge C_k/4=N^2/4-O(N^{3/2}).}$$

The identity-only set is just the origin. The median return count is two.

### Meaning

Independent radius tags make scalar coordinates distinct but preserve
too much quadratic information. For coordinates from different shells,
the smallest and largest powers of theta identify the shells, and the
remaining coefficient determines the relative sign.

### Consequence

This particular exact lift cannot give a fixed power saving, even after
adding arbitrary norm-preserving actions. The image lower bound comes
from a complete fiber proof, not from a failed return certificate. Other
paired lifts with algebraic relations between radii remain OPEN.

## 4. Carry states and modular subfamilies

### Statement

**PROVED — ML-5, scoped.** A faithful equivariant group lift with an
injective state encoding and at most s states per modular pair needs

$$s=\Omega(n^{\delta/2})$$

to encode nonzero images above all but $O(n^{2-\delta})$ modular points.
Subpolynomial state count cannot suffice under these hypotheses.
Restricting each scalar coordinate to units avoids the stabilizers:
it retains $(36/49)n^2$ modular pairs and at least m/3 returns per pair.

### Meaning

Deeply divisible modular pairs have stabilizers that a nonzero real
rotation cannot have. Extra states must distinguish their stabilizer
translates. Primitive input restriction avoids this particular cost.

### Consequence

Neither this state obstruction nor scalar collapse closes all modular
lifts. The unit restriction retains good modular combinatorics but does
not solve the real Cartesian completion problem demonstrated above.

## 5. Two fixed exact checks

**EXPERIMENTAL:** exact enumeration of the angular core and primitive
modular orbits at k=1,2. Full completed-carrier counts use the proved
shell decomposition (19)–(20); they are not an unperformed full-square
search. Equality uses integer cyclotomic coefficients, never numerical
clustering. Here $B_{1/4}$ counts R below $N^{1/4}$.

| Quantity | k=1 | k=2 |
|---|---:|---:|
| Modular input size | 7 | 49 |
| Lifted real input size N | 17 | 1121 |
| Surviving distinct actions | 6 | 42 |
| Median genuine returns | 2 | 2 |
| Identity-only pairs | 1 | 1 |
| $B_{1/4}$ | 241 | 1,251,265 |
| Pair projection fibers | 1 | 1 |
| Encoded pairs / full square | 48 / 289 | 2352 / 1,256,641 |
| Full $\lvert Q(A,A)\rvert$ | 73 | 313,657 |

The [frozen exact data](../../../examples/2026-09-30-modular-lift.json)
contain the full return histograms. [Verification](verification.md)
records the computation, checks and review limits. No parameter sweep or
post-failure expansion occurred.

## 6. One next mathematical obligation

**OPEN — ML-O1, coordinate-reusing paired lift.** In the same cyclotomic
field $K_k=\mathbb Q(\zeta_m)$, choose explicit nonzero amplitudes
$c_{k,1},\ldots,c_{k,t}$ with disjoint cosets $c_{k,j}\mu_m$.
Use $F(T_{(-2)^r}p_j)=c_{k,j}\zeta_m^r$, whose exact orbit preservation
is automatic, and prove that its same-set scalar completion has at least
$N^\varepsilon$ distinct genuine returns outside $O(N^{2-\delta})$
pairs for fixed $\varepsilon,\delta>0$. Amplitudes in K remove the
independent radical tags responsible for coefficient recovery; coordinate
reuse and cross-orbit returns still need proof. This is one specific
unproved lift mechanism, not a broad carrier restart. A proof would give
every strict $c<\min(\varepsilon,\delta)$ through DC-R1.
