# Explicit mixed-parity actions and their certified source domains

**6 October 2026 · T03 · version 1.** Fixed polynomial
$Q(x,y)=x^2+xy+y^2$. This is specialist A's symbolic contribution to
the newly authorized cross-block cycle. The two scalar carriers are
exactly the frozen dyadic carriers; no carrier modification, program
execution, network use or additional mechanism search is performed here.

The controlling definitions and earlier selected-action bounds are in
[the multiscale checkpoint](../2026-09-30-multiscale-packing/README.md),
[composition §§2–5](../2026-09-30-multiscale-packing/composition.md) and
[audit §§7–9](../2026-09-30-multiscale-packing/audit.md). The current
task examines actions outside the previously selected $\mu_m$. It does
not reinterpret that earlier selected-action theorem as an all-action
obstruction.

| Claim | Scope | Proof |
|---|---|---|
| XB-A1 | Every nonzero real pair has an explicit norm-one swap multiplier; at nonzero opposite-parity sources it is outside $\mu_m$ | §1 |
| XB-A2 | A fixed swap multiplier has exactly one certified real source line; precise full-return membership remains separate | §2 |
| XB-A3 | An explicit Vieta multiplier gives genuine returns from pure-coordinate pairs into a mixed-amplitude block of the second frozen carrier | §3 |

These claims are internally proved below; independent review is recorded
by the lead. Full-fiber upper bounds are assigned to another specialist
and are not reproved or assumed in these local action identities.

## 1. XB-A1 — a swap action outside the frozen group

### Statement

Write $\omega=(-1+i\sqrt3)/2$, $\phi(x,y)=x-\omega y$, and
$z=\phi(x,y)\ne0$. Define

$$u_p=\frac{y-\omega x}{x-\omega y}
=-\omega\frac{\overline z}{z}.
\tag{1}$$

Then $N(u_p)=1$ and $M_{u_p}(x,y)=(y,x)$. Its exact real
coefficients are

$$u_p=a_p+b_p\omega,\qquad
a_p=\frac{y^2+2xy}{Q(x,y)},\qquad
b_p=\frac{y^2-x^2}{Q(x,y)}.
\tag{2}$$

For a symmetric scalar set $A=-A$, if $x,y\in A$ are nonzero
and $x\ne\pm y$, the four targets

$$ (x,y),\quad(-x,-y),\quad(y,x),\quad(-y,-x)
\tag{3}$$

are distinct genuine returns under $\{1,-1,u_p,-u_p\}$.

For the frozen field decomposition $K=F\oplus tF$, where
$t=\gamma_0$ and the involution $\sigma$ fixes $F$ and sends
$t$ to $-t$, suppose $x,y\ne0$ lie in opposite eigenspaces.
Then $u_p\notin\mu_m$; its coefficient $b_p$ is in neither
eigenspace. This applies to opposite-parity pairs in the first frozen
carrier and to any such pair present in the second one.

### Meaning

The earlier count of two returns under $\mu_m$ leaves a real gap:
coordinate exchange produces two further targets. The multiplier is
mixed under the field involution. As a function of $(x,y)$ it is
homogeneous of degree zero, so “mixed parity” is the precise distinction,
not a claim of inhomogeneous dependence on the source.

### Consequence

The new action certifies at least four returns on nonzero opposite-parity
pairs. This is a constant gain. The separate [XB-F1 full-fiber
theorem](audit.md) supplies the matching upper bound of four on the
first carrier's opposite-parity population. Thus the finite enlarged
family defined below raises the actual count there from exactly two
to exactly four. No median claim on the whole square is inferred.

### Proof

Since $-\omega\overline z=y-\omega x$, (1) holds. Conjugation and
the unit $-\omega$ preserve modulus, hence $N(u_p)=1$. Multiplying
$u_pz=y-\omega x$ proves the target formula. Rationalizing its
denominator gives

$$ (y-\omega x)(x-\omega^2y)
=2xy-\omega x^2-\omega^2y^2
=(y^2+2xy)+(y^2-x^2)\omega,$$

which is (2). Positive definiteness makes the denominator nonzero.
Symmetry of $A$ proves membership of all four targets. Distinctness
follows from $x,y\ne0$ and $x\ne\pm y$.

For opposite parities set $E=x^2+y^2\in F$ and $P=xy\in tF$.
Here $E>0$, $P\ne0$, and $x^2-y^2\ne0$, since $x=\pm y$
would contradict the opposite nonzero parities. Thus $b_p\ne0$ and

$$\frac{\sigma(b_p)}{b_p}=\frac{E+P}{E-P}.$$

This ratio cannot be $1$ because $P\ne0$, and cannot be $-1$
because $E>0$. The denominator is $Q(x,-y)>0$. Hence $b_p$ is
neither fixed nor negated by $\sigma$. The frozen coefficient-parity
lemma says that both real coefficients of every $u\in\mu_m$ have
one common parity, so $u_p\notin\mu_m$. This proves the claim.

## 2. XB-A2 — fixed multipliers versus pair-indexed certificates

### Statement

Let $S(x,y)=(y,x)$. For any fixed actual norm-one multiplier
$u=a+b\omega$, define the swap-certified domain on a finite scalar
set by

$$C_u(A)=\{p\in A^2:M_up=Sp\}.$$

There is exactly one real line $L_u$ through the origin such that

$$\boxed{C_u(A)=A^2\cap L_u,\qquad
L_u=\ker\begin{pmatrix}a&b-1\\-b-1&a-b\end{pmatrix}.}
\tag{4}$$

In particular $|C_u(A)|\le|A|$; if $0\in A$, its nonzero part
has at most $|A|-1$ points. These are actual scalar-value counts.

The projective slope parametrization is

$$u_r=\frac{r-\omega}{1-\omega r}\quad(r\in\mathbb R),
\qquad u_\infty=-\omega^2.
\tag{5}$$

Different slopes give different actual multipliers. For finite $r$,

$$C_{u_r}(A)=\{(q,rq):q\in A,\ rq\in A\}.
\tag{6}$$

The full return domain $D_{u_r}(A)=A^2\cap M_{u_r}^{-1}(A^2)$
has the exact, generally broader form

$$\left\{(x,y)\in A^2:
\frac{r(r+2)x+(r^2-1)y}{D_r}\in A,\quad
\frac{(1-r^2)x+(1+2r)y}{D_r}\in A\right\},
\quad D_r=1+r+r^2.
\tag{7}$$

No equality $C_u=D_u$ is asserted.

### Meaning

Constructing a multiplier from each source does not give that
multiplier a two-dimensional certified source domain. Its swap
certificate belongs to one direction. The general domain (7) may
contain additional sources, whose returns require their own accounting.

### Consequence

For a library of $k$ fixed swap multipliers, the union of their
nonzero swap-certified domains contains at most $k(n-1)$ sources
when $0\in A$ and $n=|A|$. In particular covering a quadratic
population by these certificates needs linearly many actual
multipliers; duplicating ratio descriptions gives no further gain.
This is a certificate-incidence bound, not an upper bound for the
full return count of a globally enlarged action family.

### Proof

The matrix in (4) is $M_u-S$, and its determinant is
$a^2-ab+b^2-1=0$. It is not the zero matrix: its entries $b-1$
and $-b-1$ cannot both vanish. It therefore has rank one and a
one-dimensional real kernel. A nonvertical line meets $A^2$ in
at most one point for each first coordinate; a vertical line has
at most $n$ points as well. The origin accounts for the stated
nonzero correction.

Formula (5) is (1) applied to $(1,r)$, with $(0,1)$ providing
the vertical case. If two multipliers in (5) agreed, their kernel
lines in (4) would agree, so their projective slopes would agree.
Alternatively the finite inverse is
$r=(u+\omega)/(1+\omega u)$, with the vertical exception already
listed. Substituting $x=1,y=r$ in (2) gives

$$a_r=\frac{r^2+2r}{D_r},\qquad
b_r=\frac{r^2-1}{D_r},\qquad
a_r-b_r=\frac{1+2r}{D_r},$$

which proves (6)–(7). Summing the line capacities proves the
library statement. The source origin has one distinct returned pair
regardless of the number of multiplier labels.

### One explicit finite enlarged action family

For either frozen carrier $A$, which contains zero and nonzero values,
define the actual projective ratio set and actual multiplier set by

$$\mathcal R(A)=\{y/x:x\in A\setminus\{0\},\ y\in A\}
\cup\{\infty\},$$
$$\boxed{\widehat U(A)=\mu_m\cup
\{u_r,-u_r:r\in\mathcal R(A)\}.}
\tag{I}$$

All braces denote sets of actual values; repeated ratios and coinciding
unit values are identified. This is a finite, explicit collection of
norm-one multipliers, with the safe inventory bound

$$|\widehat U(A)|\le m+2\bigl(n(n-1)+1\bigr).$$

For each nonzero source, its own swap ratio belongs to this inventory.
Consequently all four targets in (3) are supplied whenever they are
distinct. The origin supplies one target. On the first carrier's
opposite-parity pairs, XB-F1 in [audit.md](audit.md) bounds the entire
norm fiber by the same four targets; hence the actual
$R_{\widehat U}$ is **exactly four** there. At other sources, returns
from multipliers constructed elsewhere are retained and are not
bounded by the line-certificate count.

## 3. XB-A3 — a concrete Vieta return into a mixed block

### Statement

Keep the second frozen carrier, without alteration. At depth $d\ge1$
write $m=6\cdot2^d$, $\theta=2\pi/m$, $s_r=-2\sin(r\theta)$,
$t=\gamma_0=2\cos\theta$, and

$$B=\bigcup_{J\subseteq\{1,\ldots,d-1\}}
\left(\prod_{\ell\in J}(1+\gamma_\ell)\right)S_d,
\qquad A_d^{(1)}=B\cup(1+t)B.$$

Let $W_d$ be the following actual set, with repeated labels identified:

$$W_d=\left\{c_Js_1:
c_J=\prod_{\ell\in J}(1+\gamma_\ell),\quad
J\subseteq\{1,\ldots,d-1\}\right\}.$$

Every $q\in W_d$ is nonzero, and $q,tq\in B$. The single multiplier

$$v_t=\omega u_t=-\omega^2\frac{1-\omega^2t}{1-\omega t}
=\frac{1-t^2+(1+2t)\omega}{1+t+t^2}
\tag{8}$$

has norm one, is outside $\mu_m$, and gives the genuine return

$$\boxed{M_{v_t}(q,tq)=(q,-(1+t)q)\in(A_d^{(1)})^2
\qquad(q\in W_d).}
\tag{9}$$

The second target coordinate is on a mixed $F$-line rather than
either pure eigenspace. The same identity holds for the simultaneous
negative sources.

More generally, for any nonzero real pair, the pair-indexed multiplier
$v_p=\omega u_p=-\omega^2\overline z/z$ realizes the Vieta
reflection $(x,y)\mapsto(x,-x-y)$. Its certified return condition
on $A^2$ is exactly $-x-y\in A$.

### Meaning

The mixed-amplitude factor does create a concrete target absent from
the pure-line geometry. Membership in (9) comes from the exact
coordinate-reuse identity $t s_1=s_2$ and the existing amplitude
block $(1+t)B$, not from a modular congruence or a formal action label.

### Consequence

This one explicit extra identity is valid but remains a one-line
certificate for the fixed multiplier $v_t$. The address count
$2^{d-1}$ is only an upper bound for $|W_d|$, and in any case
$|W_d|\le|A_d^{(1)}|$. No Cartesian lower tail or recursive return
amplification is inferred.

Unit rotations and Vieta/swap reflections at a single source certify
at most twelve targets. If their multipliers are pooled over different
sources, incidental additional returns must again be checked; the
twelve-target statement is not an all-action full-fiber bound.

### Proof

For $\ell\ge1$, $1+\gamma_\ell$ is fixed by the frozen involution,
and all these factors are positive. The scalar $s_1$ is nonzero and
pure, so every $q\in W_d$ is nonzero and pure. Sine doubling gives

$$tq=c_J\,2\cos\theta\,(-2\sin\theta)=c_Js_2\in B.$$

Thus $(q,tq)$ is a pair of nonzero opposite-parity coordinates in
the frozen carrier, and $-(1+t)q\in(1+t)B$ by symmetry of $B$.
Equation (1), followed by multiplication by $\omega$, gives

$$\omega u_p z=\omega(y-\omega x)
=x+\omega(x+y)=\phi(x,-x-y).$$

This proves the general Vieta identity and (9). Multiplying the
coefficients of $u_t$ by $\omega$ gives (8). By XB-A1,
$u_t\notin\mu_m$; since $\omega\in\mu_m$, also
$v_t\notin\mu_m$.

The multiplier in (8) already belongs to the finite family (I),
without an extra unit-closure operation. Indeed

$$v_t=u_{-(1+t)/t},$$

by direct substitution in (5). The slope $-(1+t)/t$ is realized by
the actual source $(tq,-(1+t)q)\in(A_d^{(1)})^2$, and $tq\ne0$.
Thus $\widehat U(A_d^{(1)})$ genuinely contains the action used in
(9), as well as its negative.

For a fixed Vieta reflection matrix $V$, $\det V=-1$ and $V$
preserves $Q$. The same calculation as (4), or applying (4) after
a unit rotation, makes $\ker(M_{v_t}-V)$ one real line. Here it
is precisely $y=tx$. Finally, all the unit and reflected-unit
images of a fixed complex scalar belong to

$$\mu_6 z\ \cup\ \mu_6\overline z,$$

a set of at most twelve values. This proves only the explicitly
stated per-source certificate bound.

## 4. Scope and charged local ledger

| Item | Exact accounting |
|---|---|
| Carriers | Both frozen dyadic carriers remain unchanged; same set in both coordinates |
| New actual actions | The explicit finite set (I); its realized ratio set already contains the single Vieta identity |
| Field and scalar identity | Actions lie in $K(\omega)$ whenever source coordinates lie in $K$; full scalar norm equality is exact |
| Source/action fibers | Swap multipliers are indexed injectively by real projective slopes, not by source labels |
| Target fibers | Actions act freely at nonzero sources; the origin always has one distinct target |
| Denominators | Formula (2) divides by the actual positive $Q(x,y)$; (8) by $1+t+t^2>0$. No denominator population estimate is used |
| Coordinate reuse | $t(c_Js_1)=c_Js_2$ is exact; repeated $c_Js_1$ are identified |
| Thinning and coverage | No thinning of the carrier. Vieta-certified sources are a subset of one line, not a declared near-full square |
| Line incidence cost | At most $n-1$ nonzero swap-certified sources per fixed action; no free proliferation of branch labels |
| Per-source gain | Swap gives four distinct targets on opposite-parity sources; XB-F1 separately proves equality on the first carrier. Unit/reflection certificates give at most twelve, with no global-median claim |
| Uncharged incidental returns | Not discarded or bounded here; they belong to the separate full-fiber analysis |
| Asymptotic gate | These identities alone establish no positive return exponent, bad-pair exponent or image saving |
| Program budget | Zero evaluations, zero research-program CPU seconds; symbolic derivation only |

This companion establishes exact cross-block identities and their source
domains. It does not duplicate the independently assigned full-fiber proof
or launch another carrier or action search. Any final all-action conclusion
must cite that separate proof, rather than the incidence or twelve-target
certificate statements above.
