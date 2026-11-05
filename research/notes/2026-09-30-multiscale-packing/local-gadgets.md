# Two finite coordinate-reusing norm gadgets

**30 September 2026 · T03 · version 1.** Fixed polynomial
$Q(x,y)=x^2+xy+y^2$. This is Agent A's bounded local-design contribution
to the authorized multiscale-packing cycle. It uses **zero mathematical
program executions**, no network and no outside theorem. Two local gadgets
are recorded; no third gadget or independent search is launched.

The first uses the already recorded finite adaptive seed
$\mathcal A_1=\{\pm1,\pm2\}$ as local input. It does not restart the
adaptive construction, an interval search or a unit family. The second
is the first level of a new shared-amplitude cosine substitution. Its
recursive analysis and its scoped obstruction are controlled by the
architect's [composition companion](composition.md); no local table is
multiplied across levels without a scalar proof.

## 1. MP-L1 — the four-coordinate seed

### Statement

Put $\omega=(-1+i\sqrt3)/2$, $\phi(x,y)=x-\omega y$, and

$$A_* =\{-2,-1,1,2\},\qquad
v=\frac{2-\omega}{1-2\omega}=\frac{8+3\omega}{7},$$
$$U_* =\mu_6\cup\{v,-v,v^{-1},-v^{-1}\},
\qquad \mu_6=\{\pm1,\pm\omega,\pm\omega^2\}.$$

These are ten distinct norm-one multipliers. The exact full-square norm
table and actual selected-return table are

| Norm value | Number of ordered pairs | Distinct returns per source |
|---|---:|---:|
| 1 | 2 | 2 |
| 3 | 6 | 6 |
| 4 | 2 | 2 |
| 7 | 4 | 4 |
| 12 | 2 | 2 |

Thus $|A_*|=4$, $|Q(A_*,A_*)|=5$, and the return histogram is
$\{2:6,4:4,6:6\}$. The identity-only set is empty; median and
arithmetic mean are both four. The geometric mean is
$2^{5/4}3^{3/8}$.

### Meaning

The same four scalar coordinates participate in five norm shells.
The six-point norm-three shell uses the unit rotations; the nonunit
rotation $v$ links two otherwise separate sign pairs at norm seven.
This is genuine coordinate reuse and a whole-scalar identity.

### Consequence

The local table passes the exact-identity and distinct-target gates.
It supplies no recursive return exponent. In particular the local
arithmetic mean four is not a proved per-level factor $\rho=4$.

### Complete local proof

The coefficient action is

$$M_{a+b\omega}(x,y)=(ax+by,-bx+(a-b)y).$$

For $v$ it is $((8x+3y)/7,(-3x+5y)/7)$, which sends $(1,2)$
to $(2,1)$. Integrality requires $x+3y\equiv0\pmod7$.
For $y=-2,-1,1,2$ and $x\in A_*$, the only solutions are
$(x,y)=(-1,-2),(1,2)$. Their displayed targets belong to the square,
so

$$D_v=D_{-v}=\{(1,2),(-1,-2)\},\qquad
D_{v^{-1}}=D_{-v^{-1}}=\{(2,1),(-2,-1)\}.$$

The four non-sign unit actions return exactly when $x+y\in A_*$.
The corresponding six pairs are

$$E_* =\{(1,1),(-1,-1),(1,-2),(-1,2),(2,-1),(-2,1)\},$$

all of norm three. The signs return everywhere. Direct substitution
in the sixteen positions gives the displayed norm table, and these
domains give its return column. All sources are nonzero, so distinct
multipliers give distinct returned pairs. The four added multipliers
are not units and are pairwise distinct: equality up to inverse/sign
would force $v^2=\pm1$, excluded by the displayed coefficients.

The rate auditor independently checked this local proof and table in
this cycle. That audit does not cover any later recursive use.

## 2. MP-L2 — the two-orbit sine-doubling gadget

### Statement

Let $U=\mu_{12}$ and use the two complex norm orbits

$$Z=\sqrt3\,\mu_{12}\ \cup\ 3\mu_{12}.$$

Their two real coordinate projections under $\phi^{-1}$ agree. For
the first orbit the common projection is

$$S=\{0,\pm1,\pm\sqrt3,\pm2\};$$

the second projection is $\sqrt3 S$. Hence

$$S\cap\sqrt3 S=\{0,\pm\sqrt3\},\qquad
A=S\cup\sqrt3 S
=\{0,\pm1,\pm2,\pm3,\pm\sqrt3,\pm2\sqrt3\},\quad |A|=11.$$

Every $u\in U$ acts on the entire scalar $x-\omega y$, preserving
the full quadratic cross term. The exact selected-return histogram is

| Distinct returned pairs | Number of sources in $A^2$ |
|---:|---:|
| 1 | 1 |
| 2 | 64 |
| 6 | 24 |
| 8 | 8 |
| 12 | 24 |

The identity-only set is $\{(0,0)\}$. The median is two, the mean is
$625/121$, and the geometric mean is $2^{160/121}3^{48/121}$.
The full norm image has exactly 24 elements; this last count includes
the extra coincidences under multipliers outside the selected $\mu_{12}$.

### Meaning

Two distinct radii reuse three coordinates. Each of the norm-three
and norm-nine shells is an entire twelve-point orbit in the completed
square. Some additional cross-orbit pairs acquire eight returns.
Nevertheless a majority of the local square has only the two sign
returns. A rich local orbit does not by itself yield a good typical tail.

### Consequence

This is a genuine finite input for a multiscale coordinate-reuse test.
Its $12$-return population and its mean cannot be treated as independent
factors at different levels. The recursive recipe is specified in §3;
its bad-set analysis is supplied separately in
[composition.md](composition.md), which controls the recursive disposition.

### Complete local proof and full-square table

Write $B=\{-3,-2,-1,0,1,2,3\}$ and
$C=\{-2,-1,0,1,2\}$, so $A=B\cup\sqrt3 C$ with overlap zero.
The subgroup $\mu_6$ has its usual six scalar formulas. A generator
of the other coset is

$$w=\frac{2+\omega}{\sqrt3}=e^{i\pi/6},\qquad
M_w(x,y)=\left(\frac{2x+y}{\sqrt3},
\frac{-x+y}{\sqrt3}\right).$$

For a mixed pair $(a,\sqrt3 b)$ with $a,b\ne0$, the non-sign unit
actions require a coordinate $a+\sqrt3 b$ and fail membership.
The three coordinates of the $\mu_6$-orbit after $w$ are, up to signs,

$$b+\frac{2a}{3}\sqrt3,\quad
b-\frac a3\sqrt3,\quad
2b+\frac a3\sqrt3.$$

They all have nonzero rational and irrational components, so none
belongs to $A$. Swapping the source coordinates gives the same
conclusion. Thus all $2\cdot6\cdot4=48$ mixed nonzero pairs have
exactly two selected returns.

The remaining $49+25-1=73$ sources are classified in this small table.
The column headed $\sqrt3 C$ gives counts of actual pairs with both
coordinates in $\sqrt3 C$, and the origin is included only once.

| Norm | Pairs from $B^2$ | Additional pairs from $(\sqrt3 C)^2$ | Selected returns |
|---:|---:|---:|---:|
| 0 | 1 | 0 | 1 |
| 1 | 6 | 0 | 6 |
| 3 | 6 | 6 | 12 |
| 4 | 6 | 0 | 6 |
| 7 | 12 | 0 | 6 |
| 9 | 6 | 6 | 12 |
| 12 | 2 | 6 | 8 |
| 13 | 4 | 0 | 2 |
| 19 | 4 | 0 | 2 |
| 21 | 0 | 4 | 2 |
| 27 | 2 | 0 | 2 |
| 36 | 0 | 2 | 2 |

For completeness these norm counts follow by taking nonnegative
absolute-coordinate pairs $0\le a\le b\le3$ (or $\le2$), and
using $a^2+b^2\pm ab$, with the two coordinate orders and simultaneous
negatives counted when distinct. The subgroup unit formulas give the
return column within each component. The only common positive norms
of the two components are $3,9,12$. The action $w$ links their two
components: $(1,1)\mapsto(\sqrt3,0)$,
$(3,0)\mapsto(2\sqrt3,-\sqrt3)$, and
$(2,2)\mapsto(2\sqrt3,0)$. Their entire twelve-point angular orbits
therefore contribute respectively $12,12,8$ targets in $A^2$.
Every other odd-coset return would require a common norm absent from
the table. At norm seven the twelve rational pairs are two distinct
six-point unit orbits. These facts prove every return count.

The twelve integer norm values in the table are distinct. The mixed
norms are the following twelve additional, distinct irrational values:

$$4\pm\sqrt3,\quad13\pm2\sqrt3,\quad7\pm2\sqrt3,\quad
16\pm4\sqrt3,\quad12\pm3\sqrt3,\quad21\pm6\sqrt3.$$

Each has four ordered-pair representations. This proves the full
image count $24$ and completes the hand classification of all 121
ordered pairs. No numerical equality test or program enumeration is used.

## 3. MP-L3 — the exact dyadic coordinate-reuse identity

### Statement

For each $d\ge1$, fix

$$m_d=6\cdot2^d,\qquad \theta_d=2\pi/m_d,\qquad
\gamma_\ell=2\cos(2^\ell\theta_d)\quad(0\le\ell<d),$$
$$c_J=\prod_{\ell\in J}\gamma_\ell,\qquad
S_d=\{-2\sin(r\theta_d):r\in\mathbb Z/m_d\mathbb Z\},$$
$$A_d=\bigcup_{J\subseteq\{0,\ldots,d-1\}}c_JS_d,
\qquad U_d=\mu_{m_d}.$$

All $\gamma_\ell$ are positive. Each set $c_JS_d$ is the common
coordinate projection of the exact whole-scalar orbit
$\sqrt3 c_J\mu_{m_d}$. At depth one this is precisely MP-L2.
For $0\le a<b\le d$ there is the exact coordinate identity

$$\boxed{\left(\prod_{\ell=a}^{b-1}\gamma_\ell\right)
\sin(2^a\theta_d)=\sin(2^b\theta_d).}$$

It follows by repeated application of $2\sin t\cos t=\sin2t$.
Multiplying by any common amplitude prefix preserves the identity,
so scalar coordinates from different amplitude addresses really coincide.

The exact elementary size bounds are

$$3\cdot2^d+1\ \le |A_d|\ \le3\cdot4^d+1,\qquad |U_d|=6\cdot2^d.$$

### Meaning

The phases are one global rotation group. No independent rotations of
scalar summands are used. The radii satisfy explicit relations in the
same cyclotomic field, so the independent-radius recovery argument from
ML-4 does not automatically apply.

The displayed identity proves coordinate reuse; it does not establish
its frequency among arbitrary completed Cartesian pairs. Subset labels
are not asserted to give distinct radii or distinct scalar coordinates.

### Consequence and exact rate gate

If $|A_d|=\lambda^{d+o(d)}$, the bounds give $2\le\lambda\le4$.
If a typical return factor $\rho$ exists, the actual action inventory
gives $\rho\le2$. Neither factor is inferred from the depth-one table.

The selected orbit union has at most $m_d2^d=6\cdot4^d$ encoded
pairs. If $\lambda>2$, this particular full-orbit certificate is
exponentially sparse in $A_d^2$; this fact alone does **not** bound
incidental returns outside those orbits. At $\lambda=2$ even that
coverage conclusion does not follow. These elementary counts are
superseded for the return-tail decision by the architect's full-square
parity obstruction in [composition.md](composition.md). They are retained
here to distinguish what the local construction alone proves.

### Proof of the size and projection statements

For $z=\sqrt3e^{ir\theta_d}$ the decoded second coordinate is
$-2\sin(r\theta_d)$; the first is
$\sqrt3\cos(r\theta_d)+\sin(r\theta_d)
=2\sin(r\theta_d+\pi/3)$. The angular grid is closed under
the shift by $\pi/3$ and under negation, so the projections agree.
Since $4\mid m_d$, the involution $r\mapsto m_d/2-r$ has two
fixed indices, and equality of sine values identifies exactly its
orbits. Hence $|S_d|=m_d/2+1$. The empty address gives the lower
bound. Every scaled copy contains zero, so their union has at most
$1+2^d(|S_d|-1)$ elements, proving the upper bound. Positivity follows
from $0<2^\ell\theta_d\le\pi/6$.

## 4. Local ledger and provenance

| Required item | MP-L1 | MP-L2 / proposed MP-L3 |
|---|---|---|
| Exact inputs | Four real integers | Eleven real numbers locally; exact recursive bounds in §3 |
| Same set / thinning | $X=Y=A_*$; none | $X=Y=A_d$; none |
| Pair coverage in the local tables | All 16 ordered pairs | All 121 ordered pairs |
| Actual actions | Ten distinct norm-one values | Twelve locally; exactly $6\cdot2^d$ globally |
| Zero / stabilizers | No zero; actions free | Origin one target; actions free at every other pair |
| Scalar preservation | Whole multiplication in $\mathbb Q(\omega)$ | Whole multiplication in the common cyclotomic field |
| Projection fibers | No pair identification under $\phi$ | No pair identification under $\phi$; scalar address fibers not assumed trivial |
| Heights and denominators | Integers; added action denominator 7 | Algebraic sine/cosine amplitudes; no independent-tag or denominator saving claimed |
| Degree / discriminant / regulator | Fixed degree; no asymptotic inference | Growing field; any asymptotic arithmetic costs belong to the architect's ledger, not assigned zero here |
| Local norm support | Exactly 5 | Exactly 24 at depth one |
| Per-level $\lambda,\rho$ | Not supplied by a finite seed | $2\le\lambda\le4$ if it exists, $\rho\le2$; a positive typical factor is not established here |
| Bad-pair exponent | No growing family in this local claim | No positive exponent claimed by these local identities |
| Computation | None | None |

**Source boundary.** The current governing checkpoint is
[the modular-lift report](../2026-09-30-modular-lift/README.md), with
its [proofs](../2026-09-30-modular-lift/proofs.md) and
[ledger](../2026-09-30-modular-lift/ledger.md). MP-L1's four-element
carrier is the historically recorded $\mathcal A_1$ in
`local-only/migration/sources/T03_CURRENT_STATE.md`, §4.1; the new work
here is its explicit local action-domain table and the distinct
coordinate-reusing two-orbit substitution MP-L2/MP-L3. No unavailable
archive certificate is needed. The old tensor, CRT, balanced-word,
moving-pole, denominator and independent-radius families are not rerun.

**Status:** local claims MP-L1–MP-L3 are internally proved as written.
The rate auditor independently checked both local return tables. The
lead then independently checked MP-L1/MP-L2's norm tables, return counts,
the 121-pair partition, the twelve irrational norm values and both
geometric means, and accepted those conclusions. These are internal
audits, not external review. MP-L3's recursive disposition is controlled
by the separately reviewed [composition companion](composition.md).
No novelty claim, global image theorem or recursive return amplification
is asserted in this local companion.
