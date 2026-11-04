# T04 — cubic slices and complementary units

Prepared 2026-09-14 from the record frozen through 2026-09-10. Target:

\[
P_-(x,y)=(x-y)^3-3(x+y).
\]

**OPEN.** The current complementary-unit construction has proved exponential
input growth. A strict output exponent gap remains unknown. This target is
kept separate from T01's cubic with the plus sign.

## What the two papers contributed

The unit-distance work supplied the model of producing many structured
relations through algebraic units. The sum-product work supplied the model
of organizing units and real projections with explicit size and distortion
costs. T04 tested quadratic comparisons, rich fibers, trace identities, and
ultimately a fixed pair of complementary units. The enduring issue is that
many relations or many inputs do not themselves bound the full output set.
Sources: **S-T04**; [shared foundations](00-shared-foundations.md).

## SN-T04-1 — quadratic comparison and the slice identity

**PROVED, reported identities and scoped obstructions.** Source: **S-T04**,
quadratic-to-cubic and slice sections; **S-REG**.

The historical quadratic benchmark is
$R(x,y)=(x-y)^2+5(x+y)$. With $u=x-y$,

\[
5P_-(x,y)=5u^3+3u^2-3R(x,y).
\]

This identity still depends on $u$. A small set of quadratic values alone
therefore does not bound the cubic image. For the specified centered box
carriers, the retained results give actual injectivity for two named primes
in the $5\bmod12$ regime and an image of size at least
$|A|^2/(1+e^{-\delta d})$ in the stated $1\bmod12$ regime and parameter range.
These are obstructions for those carriers; they are not universal cubic
impossibility results. Precise carrier hypotheses remain those of **S-T04**.

The slice identity makes the missing overlaps especially clear. Put
$A_u=A\cap(A-u)$, so $y\in A_u$ means $y,y+u\in A$. Then

\[
P_-(A,A)=\bigcup_{u\in A-A}(u^3-3u-6A_u),
\qquad \sum_u|A_u|=|A|^2.
\]

Each individual slice is injective in $y$. Cross-slice collisions must satisfy

\[
6(y-y')=(u-u')(u^2+uu'+u'^2-3).
\]

Consequently, merely finding many rich slices or selected unit-generated
translates does not give an upper bound for this union.

## SN-T04-2 — fibers, local bounds, and traces: lessons that survived

**PROVED, reported identities and scoped failures; OPEN broader mechanisms.**
Source: **S-T04**, coverage, local CRT, and trace sections; **S-REG**.

For any map on $A^2$, if $r(z)$ counts the pairs producing $z$, then

\[
|f(A^2)|=\sum_{(x,y)\in A^2}\frac1{r(f(x,y))}.
\]

This is a useful support criterion. If at most $C n^{2-\kappa}$ ordered pairs
belong to fibers smaller than $n^\varepsilon$, then
$|f(A^2)|\le(C+1)n^{2-\min(\varepsilon,\kappa)}$ for $n=|A|$.
By contrast, a fixed positive fraction of rich pairs can leave a quadratic
tail. The recorded rich-fiber family makes this concrete: for $n=2N$, its
actual image has $4N^2-N+1$ values despite its deliberately rich fiber.

The exact local theorem in the specified depth ratio $2:3$ is an image
**lower** bound under its frozen modulus and coefficient hypotheses. It is
an obstruction, not a compression theorem. The broader deep-precision BP2
statement remains open. The product-tree lower-bound argument in this record
is internal; an earlier attribution to the external sum-product paper is
corrected in **S-REG**, conflict MC-02.

There is also an exact norm–trace reformulation. For a finite positive
rational set $H=H^{-1}$, let $A_H=\{h^2+h^{-2}:h\in H\}$ and

\[
\alpha(t)=(t-t^{-1})^3+\sqrt3(t+t^{-1}).
\]

The recorded identity is

\[
\operatorname{Tr}_{\mathbb Q(\sqrt3)/\mathbb Q}
\bigl(\alpha(h/k)\overline{\alpha(hk)}\bigr)
=2P_-(h^2+h^{-2},k^2+k^{-2}),
\]

with $|A_H|=(|H|+\mathbf1_{1\in H})/2$.
The argument bounds multiplicity of the relevant nonzero products before
taking traces by 72. A bound before the trace does not bound the trace
support from above. The missing trace compression remains an open condition;
the identity itself is not a construction with a certified gap.

For fixed algebraic digit bases $\lambda\notin\{0,1,-1\}$ and the specified
finite graph languages of positive entropy, another recorded obstruction
gives $|P_-(A_m,A_m)|\ge c(m+1)^{-2V}|A_m|^2$.
Its hypotheses concern that fixed-base digit model. They should not be
silently applied to every affine system with different edge multipliers.

## SN-T04-3 — the complementary-unit input construction

**PROVED, reported; the companion input argument inspected for exposition.**
Sources: **S-SACC-INPUT**, **S-SACC-AUDIT**, and **S-T04**, final frontier.
No independent audit or computation was performed for these notes.

Set $\epsilon=2+\sqrt3$, $a_0=\sqrt3/2$, and

\[
f_+(x)=\epsilon x+a_0,\qquad
f_-(x)=\epsilon^{-1}x-a_0,\qquad
A_0=\{0\},\quad A_{m+1}=f_+(A_m)\cup f_-(A_m).
\]

All inputs lie in the fixed field $\mathbb Q(\sqrt3)$ with denominator at
most two; cubic outputs have denominator at most eight. There are $2^m$
histories, but histories can coincide as scalar inputs: $+-+$ and $-+-$
already both give $-3/2$ at depth three in the companion's composition convention.
Thus history count alone is not a valid input count.

The input proof extracts separated block families. Normalize $z=x/a_0$.
The blocks $B_k=+(+-)^k$, for $k=0,1,2$, have lengths one, three, and five
and act as

\[
z\longmapsto\epsilon z+1-k(1-\epsilon^{-1}).
\]

For a fixed number of blocks, the leading different digit dominates the
remaining tail because $2/(\epsilon-1)<1$. The block words of total length
$m$ obey a recurrence with steps one, three, and five. Grouping them by
block count loses at most a factor $m+1$. If $\Lambda>1$ is defined by
$\Lambda^{-1}+\Lambda^{-3}+\Lambda^{-5}=1$, the proof gives

\[
|A_m|\ge\frac{\Lambda^{m-2}}{m+1}.
\]

The companion audit also bounds occupation arrays and hence affine maps.
With $\varphi=(1+\sqrt5)/2$, it gives
$|A_m|\le2\varphi^4\varphi^m$. If $F_m$ denotes the set of affine maps
represented at depth $m$, then
$|A_m|\le|F_m|\le(m+1)|A_m|$.
Submultiplicativity of the map counts yields an actual input entropy

\[
a_*:=\lim_{m\to\infty}\frac1m\log|A_m|,
\qquad \log\Lambda\le a_*\le\log\varphi.
\]

This is genuine input-side progress in the supplied proof system. It does
not establish an output saving.

## SN-T04-4 — what pair states tell us, and what they do not

**PROVED, reported transition identities; OPEN output bound.** Source:
**S-SACC-PAIRS**, together with **S-SACC-AUDIT**.

For a pair $(X,Y)$, write $u=X-Y$, $s=X+Y$. Applying the same branch
$\sigma\in\{1,-1\}$ to both coordinates gives

\[
u'=(2+\sigma\sqrt3)u,\qquad
s'=(2+\sigma\sqrt3)s+\sigma\sqrt3.
\]

Applying opposite branches, with $\sigma$ assigned to the first coordinate,
gives

\[
u'=2u+\sigma\sqrt3(s+1),\qquad
s'=\sigma\sqrt3u+2s.
\]

These affine transitions act linearly on the ten monomials in $u,s$ of total
degree at most three. This finite-dimensional description is exact, but it
can contain infinitely many scalar states. Ten coordinates do not imply ten
states, or a small number of values of $u^3-3s$.

A sufficient next result would label every ordered pair using at most
$K_0(m+1)^B\kappa^m$ labels, with fixed constants and
$\kappa<\Lambda^2$, in such a way that equal labels imply equal scalar
outputs. It would certify every strict exponent
$c<2-\log\kappa/\log\Lambda$.
The sharper actual frontier is
$\limsup_m m^{-1}\log|P_-(A_m,A_m)|<2a_*$.
Neither assertion is established. The currently certified output bound is
the trivial $|A_m|^2$, so the certified positive gap is zero; the actual gap
is unknown.

The companions report an exact depth-12 example with 1,030 inputs and
1,058,120 output values out of 1,060,900 ordered pairs, with maximum fiber
size eight. It is finite evidence, not a uniform asymptotic conclusion.
The larger depth-30 input count is not used here: the reconciliation identifies
an unmatched provenance gap between that quotation and retained raw data.

## Recall check

1. What does the slice identity require beyond many long slices? **Enough
   overlap between their scalar output sets, with every ordered pair covered.**
2. What was proved for complementary units? **Exponential growth and bounds
   on the actual input set, including the existence of its entropy.**
3. Why is a ten-dimensional pair representation insufficient? **Dimension
   does not bound the number of distinct states or scalar outputs.**
