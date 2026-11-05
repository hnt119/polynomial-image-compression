# Common-core and fringe return tradeoffs

**Date/version:** 21 September 2026, version 1. **Track:** T03.
**Fixed polynomial:** $Q(x,y)=x^2+xy+y^2$ on real inputs.
**Authorized branch:** DC-O1, almost-common rectangular return domains.

The current assignment is the local attachment
`[private commissioning attachment; locator withheld]`.
This bounded subtask is strictly offline and symbolic: **zero mathematical
program runs or evaluations**, no outside theorem, no literature search,
and no novelty claim. Only this new note is changed. The complete proofs
below are internally authored and checked; independent review is a
separate record. No successful DC-O1 witness is asserted.

## 1. Exact legal domains and fringe capacity — CF-1

### Statement

Let $X,Y\subset\mathbb R$ be finite nonempty sets. Put

$$C=X\cap Y,\quad S_X=X\setminus Y,\quad S_Y=Y\setminus X,$$
$$c=|C|,\quad f_X=|S_X|,\quad f_Y=|S_Y|,\quad
F=f_X+f_Y,\quad n=|X\cup Y|=c+F.$$

Let $U$ be a finite set of $M$ distinct actual norm-one multipliers.
For $u=a+b\omega$, $a,b\in\mathbb R$, the exact coefficient action is

$$T_u(x,y)=(ax+by,-bx+(a-b)y),\qquad a^2-ab+b^2=1.$$

Define, for a source pair $p\in C^2$, the distinct-target counts

$$r_{XY}(p)=\#\{T_up\in X\times Y:u\in U\},$$
$$r_C(p)=\#\{T_up\in C^2:u\in U\},\qquad
\ell(p)=\#\{T_up\in H:u\in U\},$$

where the target fringe and its exact size are

$$H=(X\times Y)\setminus C^2
=(S_X\times Y)\sqcup(C\times S_Y),$$
$$h=|H|=cF+f_Xf_Y\le nF.\tag{1}$$

In particular $r_{XY}(p)=r_C(p)+\ell(p)$, including at zero. The
legal domains for the mechanism are the disjoint pieces

$$D_u^C=C^2\cap T_u^{-1}(C^2),\qquad
D_u^H=C^2\cap T_u^{-1}(H).\tag{2}$$

For every $p\in C^2$,

$$\boxed{\ell(p)\le2F.}\tag{3}$$

For positive norms write
$r_{C^2}^Q(t)=\#\{p\in C^2:Q(p)=t\}$ and define
$K=\max(\{r_{C^2}^Q(t):t>0\}\cup\{0\})$. Then

$$\boxed{\sum_{p\in C^2}\ell(p)\le\min(M,K)h
\le\min(M,K)nF.}\tag{4}$$

**Proof.** At fixed first coordinate $x$, the equation $Q(x,y)=t$
has at most two real solutions in $y$; the same holds after fixing $y$.
Every fringe target has either its first coordinate in $S_X$ or its
second coordinate in $S_Y$. Their union therefore contributes at most
$2f_X+2f_Y$ targets on any norm fiber, proving (3).

For each $u$, invertibility gives $|D_u^H|\le h$. Distinct-target
counting is bounded by the number of action incidences, so summing
over $U$ proves the $Mh$ bound. At a nonzero source the action counts
are in fact exact: $uz=vz$ with $z=x-\omega y\ne0$ forces $u=v$.
Zero has no fringe target, since $(0,0)\in X\times Y$ would imply
$(0,0)\in C^2$.

Independently, count all possible equal-norm core/fringe pairs, without
restricting their ratio to $U$:

$$\sum_{p\in C^2}\ell(p)
\le\sum_{t>0}r_{C^2}^Q(t)r_H^Q(t)
\le K\sum_{t>0}r_H^Q(t)=Kh.$$

This proves (4). No asserted energy lower bound is turned into a
support upper bound. $\square$

### Meaning

The asymmetric pieces allow genuine extra partial returns, but their
capacity is bounded. Each individual norm shell has at most $2F$ fringe
targets. Across the core square, every target can be reached by at most
$M$ selected actions and can share its norm with at most $K$ core pairs.

### Consequence

The improved factor $\min(M,K)$ matters when many action labels are
available but the core itself has small polynomial fibers. No full-block
invariance is assumed; different actions may use different domains (2).
Thus this result addresses partial fringe domains outside the preceding
complete-block theorem's hypotheses.

## 2. Survival of a rectangular tail on the core — CF-2

### Statement

Suppose $E\subseteq X\times Y$, $|E|=e$, and every pair outside $E$
has at least $R>0$ distinct returns into $X\times Y$ under $U$.
Put $e_C=|E\cap C^2|\le e$. For any $0<\tau<R$,

$$\boxed{\#\{p\in C^2:r_C(p)<\tau\}
\le e_C+\frac{\min(M,K)h}{R-\tau}.}\tag{5}$$

If $R-\tau\ge2F$, the fraction on the right can be omitted: every
rectangular good pair in $C^2$ already has at least $\tau$ core returns.
In particular,

$$\boxed{\#\{p\in C^2:r_C(p)<R/2\}
\le e_C+\frac{2\min(M,K)h}{R}
\le e+\frac{2MnF}{R}.}\tag{6}$$

When $R\ge4F$, the right side in (6) improves to $e_C$.

**Proof.** At every $p\in C^2\setminus E$,
$r_C(p)\ge R-\ell(p)$. If $r_C(p)<\tau$, this implies
$\ell(p)>R-\tau$. Summing over these bad points and applying (4)
proves (5). If $R-\tau\ge2F$, (3) rules out such a point. Set
$\tau=R/2$ for (6). The proof is a direct lower-tail estimate obtained
from an upper bound on lost returns. It does not infer a lower tail
from a large average of total returns. $\square$

For an asymptotic formulation, fix positive $\eta,\varepsilon,\delta$
and suppose

$$F=O(n^{1-\eta}),\quad R\ge n^\varepsilon,\quad
e=O(n^{2-\delta}),\quad M=O(n^\gamma).$$

Then $c=n-F\sim n$. If

$$\delta_C:=\min\{\delta,\eta+\varepsilon-\gamma\}>0,\tag{7}$$

the same $U$ gives at least $R/2$ returns on $C^2$ except for
$O(n^{2-\delta_C})$ pairs. Any strict return exponent below
$\varepsilon$ absorbs the factor $1/2$; any strict exceptional
exponent below $\delta_C$ absorbs constants when expressed in $c$.
If $K=O(n^\kappa)$ is also proved, one may replace $\gamma$ in
(7) by $\min(\gamma,\kappa)$. The pointwise criterion holds
eventually whenever $\varepsilon>1-\eta$.

### Meaning

The original rectangular actions survive core restriction when the
fringe is small compared with the return threshold, or when their
total lost-return capacity is too small to affect many source pairs.
The condition $\eta+\varepsilon-\gamma>0$ is sufficient for this
particular tail-transfer estimate. Its failure is not a disproof of
core returns.

### Consequence

Under (7), HR-1 on the core gives the valid bound

$$|Q(C,C)|\le\frac{2c^2}{R}+e_C+
\frac{2\min(M,K)h}{R}.\tag{8}$$

This is a transfer of the **prescribed actions**. Section 4 supplies a
different, stronger image-only transfer that does not require (7).
Neither transfer constructs the original rectangular tail premise.

## 3. When can a fringe be essential? — CF-3

### Statement

Suppose $\mathcal B\subseteq C^2\setminus E$ has $b$ pairs with
$r_C(p)<\tau<R$. If $b>0$, then

$$b(R-\tau)<\min(M,K)h\quad\hbox{if }b>0,\qquad
R-\tau<2F.\tag{9}$$

The first strict inequality may be weakened to a non-strict bound.
If $b\ge\alpha c^2$ for fixed $\alpha>0$ and $\tau=R/2$, this
requires, in particular,

$$\min(M,K)\ge\frac{\alpha c^2R}{2nF}.\tag{10}$$

For $F=O(n^{1-\eta})$, $R\ge n^\varepsilon$ and $c\sim n$,
a fixed positive-density rescue by the fringe therefore requires
both $M$ and $K$ to be $\Omega(n^{\varepsilon+\eta})$.

**Proof.** Each pair in $\mathcal B$ must have more than $R-\tau$
distinct fringe targets. Apply (3) and (4), then $h\le nF$.
This is the converse capacity requirement to CF-2. $\square$

There is also a precise no-rescue statement for a specified weak core.
If $r_C(p)\le L<R$ on a set $W\subseteq C^2$, the number of points
of $W$ that can be raised to $r_{XY}(p)\ge R$ is at most

$$\boxed{\frac{\min(M,K)h}{R-L}.}\tag{11}$$

Indeed every rescued point needs at least $R-L$ fringe targets.
For example, if $K=n^{o(1)}$, $L=n^{o(1)}$, $F=O(n^{1-\eta})$
and $R\ge n^\varepsilon$, then (11) is
$O(n^{2-\eta-\varepsilon+o(1)})=o(n^2)$, regardless of how large
the supplied finite action family is.

### Meaning

A small fringe cannot manufacture a high-return tail over a core whose
actual norm fibers are uniformly small. To repair a positive-density
low-return region, the core must already have large actual fibers,
even if the chosen $U$ has not accessed them.

### Consequence

**FAILED in this precise scope:** adding a power-saving fringe to a
core with $K=n^{o(1)}$ and mostly subpolynomial selected returns cannot
give polynomially many returns on almost every core pair. This is not
a failure theorem for arbitrary almost-common rectangles. Large or
nonuniform core fibers, with different action-dependent domains, remain
outside this conclusion.

No old bounded-digit, interval, orbit or valuation family was rerun or
selected as a new construction here. The result is a theorem about
the proposed fringe repair, not evidence that all cores have small $K$.
No concrete partial-fringe witness supplying the needed growing core
fibers has been constructed in this subtask.

## 4. Direct image transfer and replacement actions — CF-4

### Statement

The rectangular hypothesis of CF-2 itself gives

$$\boxed{|Q(X,Y)|\le\frac{|X||Y|}{R}+e.}\tag{12}$$

Consequently,

$$\boxed{|Q(C,C)|\le\frac{|X||Y|}{R}+e
\le\frac{n^2}{R}+e.}\tag{13}$$

If $F=O(n^{1-\eta})$, $R\ge n^\varepsilon$ and
$e=O(n^{2-\delta})$ with all three exponents positive, then every
fixed

$$0<c_0<\min(\varepsilon,\delta)\tag{14}$$

eventually gives $|Q(C,C)|\le |C|^{2-c_0}$. This conclusion uses
the common core as the new common scalar set. It does not strengthen
the previous union estimate for $A=X\cup Y$.

**Proof.** Any norm value with a nonexceptional representative in the
rectangle has at least $R$ distinct representatives in the same
rectangle. Its complete fibers are disjoint subsets of $X\times Y$,
so there are at most $|X||Y|/R$ such values. Values having only
exceptional representatives contribute at most $e$. This proves
(12). Inclusion $C^2\subseteq X\times Y$ proves (13), regardless
of whether individual returned targets stay in $C^2$. Finally
$|C|/n\to1$, and the strict exponent in (14) absorbs all constants.
$\square$

For completeness, genuine core returns can be recovered with a
different, potentially much larger action set. Let $c=|C|\ge1$ and
write $z_p=x-\omega y$ for $p=(x,y)\in C^2$. Define

$$U_C^*=\{1\}\cup
\{z_q/z_p:p,q\in C^2,\ p\ne(0,0),\ Q(p)=Q(q)\}.
\tag{15}$$

This is a finite set of actual norm-one multipliers with
$|U_C^*|\le c^4+1$. Every nonzero source $p$ returns to every point
in its entire core norm fiber, and no other points. At zero the sole
returned point is zero. Thus distinct-pair return counts under (15)
equal $r_{C^2}^Q(Q(p))$ for all sources, including zero when present.
For any $T>0$,

$$\#\{p\in C^2:R_{U_C^*}^{\rm pair}(p)<T\}
\le T|Q(C,C)|.\tag{16}$$

This follows by summing the sizes of the fibers smaller than $T$;
each contributes at most $T$. If $|Q(C,C)|=O(c^{2-s})$ for fixed
$s>0$, taking $T=c^\theta$, $0<\theta<s$, gives a core tail with
return exponent $\theta$ and bad exponent $s-\theta$, up to fixed
constants. No algorithmic, height or denominator bound beyond the
finite ratio definition is claimed for this replacement family.

### Meaning

Fringes may be essential to returns under the originally chosen $U$.
They are not essential to the existence of a compressed common set
once a DC-O1 rectangle has already been proved: the core inherits its
small norm image. A full-fiber ratio family can then realize a core
tail, with its larger action count explicitly charged.

### Consequence

The image transfer (13) avoids the $2\eta$ union-exception term because
it asks for the image of $C$, not of $X\cup Y$. It does not silently
claim that original returns survive an intersection. Equations (5)–(7)
are the needed statements when retention of the original actions matters.
The replacement (15) is a proved implication from an already compressed
core, not a construction of a DC-O1 witness and not a source of new
compression.

## 5. Scope, ledger and remaining obligation

| Required item | Exact treatment |
|---|---|
| Inputs and overlap | $n=c+F$; $F=O(n^{1-\eta})$ implies $c\sim n$ |
| Both-coordinate loss | Core pair count is exactly $c^2$; fringe target count is $h=cF+f_Xf_Y$; no linear loss is substituted for a squared input count |
| Partial domains | $D_u^C,D_u^H$ in (2) may differ freely with $u$; no complete-block inclusion is assumed |
| Action/projection fibers | $U$ contains distinct actual multipliers; off zero they act freely, and all statements count distinct returned pairs |
| Zero | Zero is never a fringe target; above-one tail premises must exclude it or otherwise account for its one returned point |
| Lost returns | Pointwise at most $2F$; total at most $\min(M,K)h$ |
| Prescribed-action core tail | $e_C+2\min(M,K)h/R$ at threshold $R/2$; sufficient gap (7) |
| Fringe-dependent rescue | At most $\min(M,K)h/(R-L)$ for a region with core return bound $L<R$ |
| Actual image | Complete-fiber proof (12) covers every rectangular output; (13) covers the entire core image |
| Replacement actions | Explicit norm ratios, at most $c^4+1$; no zero-stabilizer count is treated as a large returned-point count |
| Arithmetic/field costs | No number field, prime distribution, discriminant, regulator or lattice assumption enters these implications; no free arithmetic realization is inferred |
| Heights/denominators | Unrestricted for the fixed given sets/actions; candidate constructions must still prove exact membership. Replacement ratios have no asserted uniform height bound |
| Branches/states/carries | No auxiliary state encoding or carries are used; all domains and exceptions are actual real pairs |
| Rate conclusion | With the rectangular premises, core output saving has every strict exponent below $\min(\varepsilon,\delta)$; the union retains the existing DC-R1 exponent below $\min(\varepsilon,2\eta,\delta)$ |
| Positive construction | **OPEN:** no input/action sequence satisfying all DC-O1 premises is supplied |

**Source and review locators.** The prior complete rectangular-to-union
proof is [DC-R1](../2026-09-21-dense-cartesianization/block-rectangle.md),
Section 4; its final paragraph explicitly distinguishes an unproved
intersection-return inference from the valid union transport. CF-2
supplies a quantified intersection-return statement, while CF-4 uses a
different image inclusion. The underlying norm action and fiber
partition principle are in [HR-1](../2026-09-16-high-return/return-lemma.md).
The current [dense-Cartesianization checkpoint](../2026-09-21-dense-cartesianization/README.md),
Section 12, states DC-O1. The [project map](../../CURRENT_PROJECT_MAP.md),
[T03 status](../../tracks/03-eisenstein-cartesianization/STATUS.md) and
[migration conflict register](../../MIGRATION_CONFLICTS.md) preserve
earlier scopes and source availability. No unavailable proof is needed
by CF-1–CF-4; the fixed T03 target and separate RC15/4 remain OPEN.

**Single retained obligation:** construct a DC-O1 high-overlap rectangle
whose many distinct partial-return domains give a fixed positive return
exponent outside a fixed power-saving bad set. The present fringe
mechanism requires growing core norm fibers; it has not supplied them.
