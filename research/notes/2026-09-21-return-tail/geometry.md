# Return-domain geometry and a variance criterion

**Date/version:** 21 September 2026, version 1. **Track:** T03 / correlated
return-tail cycle. **Fixed polynomial:** $Q(x,y)=x^2+xy+y^2$ on real
inputs. This is a structural subtask, not a fourth carrier construction.

The active authorization is the strictly offline return-tail attachment
`[private attachment identifier withheld]`. This note uses zero mathematical
program runs or evaluations, no network, no outside result and no novelty
claim. Only this new file is authored. Proofs are internally derived and
checked; an independent review, if performed, is recorded separately.

## Identity, status and sources

| Claim | Status and quantified scope | Proof |
|---|---|---|
| RT-G1 | PROVED: exact line-incidence and intersection identities for any finite real scalar set and genuine norm-one multipliers | §1 |
| RT-G2 | PROVED: exact domain first/second moments and finite lower-tail inequality; the stated asymptotic sufficient criterion is conditional on its displayed estimates | §2 |
| RT-G3 | PROVED: exact identity-only set and the limitation of that statistic for sign-closed sets | §3 |

The norm convention and genuine-target definition agree with
[the frozen correlated DC-O1 report](../2026-09-21-correlated-dc-o1/README.md),
§1. The only support transfer in view remains the already established
[DC-R1](../2026-09-21-dense-cartesianization/block-rectangle.md), §4.
No alternative global compression theorem is sought or supplied here.
The old single-action overlap bound is neither used nor reproved.
No historical proof or carrier is changed or rerun.

## 1. RT-G1 — exact geometry of the domains

### Statement

Let $A\subset\mathbb R$ be finite and nonempty, $n=|A|$ and
$\Omega=A^2$. Fix $\omega=(-1+i\sqrt3)/2$. For
$u=a+b\omega$ with $a,b\in\mathbb R$ and
$N(u)=a^2-ab+b^2=1$, define

$$M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},\qquad
D_u=\Omega\cap M_u^{-1}(\Omega).$$

Then exactly

$$D_u=\{(x,y)\in A^2:ax+by\in A,\ -bx+(a-b)y\in A\}.\tag{1}$$

Thus $D_u$ is the intersection of the Cartesian grid with the two
families of lines

$$\{ax+by=s:s\in A\},\qquad
\{-bx+(a-b)y=t:t\in A\}.\tag{2}$$

The two row vectors are independent. Every choice of labels $(s,t)$
determines one intersection point $M_u^{-1}(s,t)$; this point is in
$D_u$ precisely when both of its coordinates are in $A$.

If $b(a-b)\ne0$, an exact row-count formula is

$$|D_u|=\sum_{x\in A}
\left|A\cap\frac{A-ax}{b}\cap\frac{A+bx}{a-b}\right|.\tag{3}$$

Here operations on a finite scalar set have their literal set meanings,
including division by a negative number. Formula (1) covers every
vanishing-coefficient case without division. In particular, if $b=0$
then $a=\pm1$ and $D_u=(A\cap aA)^2$.

For any two norm-one multipliers $u,v$,

$$\boxed{M_u(D_u\cap D_v)
=\Omega\cap M_u(\Omega)\cap M_{vu^{-1}}^{-1}(\Omega).}\tag{4}$$

In particular,

$$M_u(D_u)=D_{u^{-1}},\qquad |D_u|=|D_{u^{-1}}|,\tag{5}$$
$$|D_u\cap D_v|\le |D_{vu^{-1}}|.\tag{6}$$

The triple intersection in (4), not just the ratio domain in (6), is
the exact quantity.

### Meaning

For an arbitrary finite scalar set, these domains are grid incidences
with two families of lines. If $A\subseteq[m,M]$, they lie in the
intersection of the strips $m\le ax+by\le M$ and
$m\le-bx+(a-b)y\le M$, but the strips alone do not impose membership
in $A$. Pairwise domain overlap retains an extra transformed-grid
condition even after replacing two actions by their ratio.

### Consequence

Equations (1)–(4) provide exact membership and overlap quantities for a
return-tail argument. They give no lower-tail estimate without further
information about the particular scalar set and action family.

### Proof

Identify a real pair with $z=x-\omega y$. Direct multiplication gives

$$u(x-\omega y)=(ax+by)-\omega[-bx+(a-b)y],$$

so (1) follows. The determinant of $M_u$ is $N(u)=1$, proving the
row independence in (2). Solving the two scalar membership conditions
for $y$ gives (3). For $b=0$, $a^2=1$, and (1) gives the stated
special case.

The same coefficient identity implies $M_vM_u^{-1}=M_{vu^{-1}}$.
For $p\in\Omega$ put $q=M_up$. Membership $p\in D_u\cap D_v$
is exactly the conjunction

$$q\in\Omega,\qquad q\in M_u(\Omega),\qquad
M_{vu^{-1}}q\in\Omega.$$

This proves (4) in both directions. Taking $v=u$ gives (5), and
dropping the middle condition in (4) gives (6). Every map used is a
bijection, so cardinalities are preserved. These identities concern
actual scalar actions and require no tensor or projection assumption.
$\square$

## 2. RT-G2 — domain moments and the actual lower tail

### Statement

Let $U$ be a finite nonempty set of distinct actual norm-one multipliers.
Write $m=|U|$, and define the distinct-target return count by

$$R(p)=|\{M_up\in\Omega:u\in U\}|\qquad(p\in\Omega).$$

Let $\zeta=1$ if $0\in A$ and $\zeta=0$ otherwise. Remove the
possible origin only for the moment calculation:

$$\Omega_* =\Omega\setminus\{(0,0)\},\qquad
N=|\Omega_*|=n^2-\zeta,\qquad D_u^*=D_u\cap\Omega_*.$$

Assume $N>0$. Put

$$S_1=\sum_{u\in U}|D_u^*|
=\sum_{u\in U}(|D_u|-\zeta),$$
$$S_2=\sum_{(u,v)\in U^2}|D_u^*\cap D_v^*|
=\sum_{(u,v)\in U^2}(|D_u\cap D_v|-\zeta),\tag{7}$$
$$\mu=\frac{S_1}{N},\qquad
V=S_2-\frac{S_1^2}{N}.$$

The pairs $(u,v)$ in (7) are ordered and include $u=v$. Then

$$\mu=\frac1N\sum_{p\in\Omega_*}R(p),\qquad
V=\sum_{p\in\Omega_*}(R(p)-\mu)^2\ge0.\tag{8}$$

For every real $t<\mu$, the exact lower-tail count
$B(t)=|\{p\in\Omega:R(p)<t\}|$ satisfies

$$\boxed{B(t)\le
\zeta\,1_{\{t>1\}}+\frac{V}{(\mu-t)^2}.}\tag{9}$$

For example, fix $\varepsilon,\kappa>0$ and $0<\delta\le2$.
For a growing sequence of sets and actions, the two estimates

$$\mu\ge(1+\kappa)n^\varepsilon,\qquad
\frac{V}{N\mu^2}\le C n^{-\delta}\tag{10}$$

with fixed $C$ imply

$$B(n^\varepsilon)
\le\zeta+C\left(\frac{1+\kappa}{\kappa}\right)^2
Nn^{-\delta}
=O(n^{2-\delta}).\tag{11}$$

The parameters and the constant in (10) are fixed independently of
$n$. No candidate-specific estimate in (10) is asserted here.

### Meaning

The first moment measures total return incidence. The second moment
measures how unevenly those incidences are distributed across pairs.
A polynomial mean together with sufficiently small relative variance
is a sufficient way to obtain the required pointwise lower tail.

### Consequence

This is a precise return-tail criterion for use with the existing DC-R1
implication. A large first moment alone does not verify (10), and the
criterion is not necessary: a large variance may also come from an
upper tail rather than a large bad set. No compression witness is
established by these identities alone.

### Proof and explicit zero correction

For $p\ne(0,0)$, $z=x-\omega y\ne0$. If $M_up=M_vp$, then
$uz=vz$ and cancellation gives $u=v$. Consequently

$$R(p)=\sum_{u\in U}1_{D_u}(p)\qquad(p\in\Omega_*).\tag{12}$$

Summing (12) gives $S_1$. Squaring (12) and summing gives $S_2$,
with ordered action pairs and the diagonal terms included. Expanding
$\sum(R-\mu)^2$ proves (8).

If the origin belongs to $\Omega$, every action fixes it, but these
$m$ labels give **one** distinct target. Hence its contribution to
the first and second moments of $R$ is one in each case. In terms
of full domains, the corrected identities are

$$\sum_{p\in\Omega}R(p)
=\sum_u|D_u|-(m-1)\zeta=S_1+\zeta,$$
$$\sum_{p\in\Omega}R(p)^2
=\sum_{u,v}|D_u\cap D_v|-(m^2-1)\zeta=S_2+\zeta.\tag{13}$$

Thus raw action moments at zero cannot be used as distinct-target
moments. The origin belongs to the strict bad set exactly when $t>1$.
If $N=0$, the only possible carrier is $A=\{0\}$ and this single
pair describes the entire problem; no division by $N$ is made.

For a nonzero pair with $R(p)<t<\mu$, one has
$(R(p)-\mu)^2>(\mu-t)^2$. Summing over these pairs and using
(8) proves (9), with a weak inequality valid also for the empty bad
set. Under (10),

$$\mu-n^\varepsilon\ge\frac{\kappa}{1+\kappa}\mu.$$

Substitution in (9) proves (11), using $N\le n^2$ and
$1\le n^{2-\delta}$ for $\delta\le2$. $\square$

### The normalized overlap form

For a uniformly chosen $p\in\Omega_*$, put

$$\rho_u=\frac{|D_u^*|}{N},\qquad
\rho_{uv}=\frac{|D_u^*\cap D_v^*|}{N}.$$

Then (7)–(8) say exactly

$$\mu=\sum_u\rho_u,\qquad
\frac VN=\sum_{u,v}(\rho_{uv}-\rho_u\rho_v).\tag{14}$$

These are pointwise-domain covariances, not a count of equal-norm
outputs. Equation (4), with the origin removed on both sides, gives
their exact geometric intersections. Replacing those triple
intersections by a ratio-domain upper bound loses information and
need not produce the relative-variance estimate required in (10).

The moment argument also holds verbatim for $\Omega=X\times Y$:
replace $N$ by $|X||Y|-\zeta$, where $\zeta=1$ precisely when both
sets contain zero. The present note supplies no new rectangular
symmetrization theorem; that remains the established DC-R1 step.

## 3. RT-G3 — what identity-only pairs do and do not detect

### Statement

Assume $1\in U$. The nonzero identity-only set is exactly

$$I_*:=\{p\in\Omega_*:R(p)=1\}
=\Omega_*\setminus\bigcup_{u\in U\setminus\{1\}}D_u^*.\tag{15}$$

Equivalently, for every nonidentity $u=a+b\omega$, at least one of

$$ax+by\notin A,\qquad -bx+(a-b)y\notin A\tag{16}$$

must hold. The full identity-only set adds the origin if $0\in A$.

If $A=-A$ and $\{1,-1\}\subseteq U$, then

$$R(p)\ge2\quad(p\in\Omega_*),\qquad
I_* =\varnothing,\qquad |I|=\zeta.\tag{17}$$

For the fixed action set $U=\{1,-1\}$, equality $R(p)=2$ holds
at every nonzero pair. Therefore, whenever $n^\varepsilon>2$,

$$B(n^\varepsilon)=n^2\tag{18}$$

despite the empty nonzero identity-only population. This observation
applies to any sign-closed scalar set; it is not an additional carrier
family or experiment in this cycle.

### Meaning

Positive-density identity-only pairs immediately refute a polynomial
return tail. The converse is false: adding the negative-identity
action already removes every nonzero identity-only pair of a sign-closed
set, without producing a growing number of returns.

### Consequence

An identity-only count of zero, or one from the origin, is only an early
diagnostic. The actual polynomial-threshold bad set must still be
estimated. No composition or positive return exponent follows from
(17).

### Proof

The identity returns every source. At a nonzero source, a distinct
nonidentity returning action has a different target by cancellation,
which proves (15) and its explicit membership version (16). If
$A=-A$, the negative identity sends $(x,y)$ to $(-x,-y)\in A^2$.
These two pairs are distinct unless $(x,y)=(0,0)$, proving (17).
With only these two actions there are no additional targets, and
both one and two are strictly less than $n^\varepsilon$ in (18).
$\square$

## 4. Structural ledger and retained gap

| Gain or cost | Exact accounting | Scope |
|---|---|---|
| Inputs and growing parameter | Arbitrary finite $A$, exact size $n$; no new parameterized carrier | General finite structural lemma |
| Thinning and same-set transport | No scalar input thinning; both coordinates use $A$ | The removed origin is restored explicitly in (9), (13) |
| Projection and parameter fibers | No projection or formal word encoding | Actual scalar action matrices throughout |
| Action multiplicity | $m$ distinct multipliers; exactly one multiplier per returned target off zero | Cancellation in $\mathbb C$ |
| Zero / stabilizers | $m$ fixing labels but one target at the origin | First-moment correction $m-1$, second-moment correction $m^2-1$ |
| Domain states and branches | $m$ domains and $m^2$ ordered intersections, including equal actions | Fully included in (7), (14) |
| Arithmetic field, moduli, denominators | No algebraic-field construction or arithmetic estimate required by these real identities | Candidate-specific costs remain to be supplied by each construction |
| Heights and archimedean distortion | $Q$ is preserved exactly; membership in the actual finite scalar set is retained | A containing strip is not treated as the scalar set |
| Boundary / uncovered pairs | Every pair counted; strict threshold and the origin handled explicitly | No exceptional source discarded |
| Input and return rates | No unconditional rates asserted | Candidate hypotheses (10) are still required |
| Tail cost | $B(t)\le\zeta1_{t>1}+V/(\mu-t)^2$; criterion (10) yields (11) | PROVED finite inequality and conditional sufficient criterion |
| Full image / signed saving | No new image theorem or positive exponent certified | Apply existing DC-R1 only after a candidate proves its hypotheses |

No script, runtime, seed or experimental result is attributed to this
subtask. Its only deliverable is the complete structural proof above.
The retained task is to establish a genuinely polynomial return tail
for one of the separately authorized candidates, not to infer it from
average overlap or from the absence of identity-only points.
