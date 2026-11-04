# From a Finite Frobenius Gadget to a Quadratic Pair Symmetry

**Three-branch continuation for $P(x,y)=(x-y)^3+x+y$**

T01 / Final documentation freeze / 21 September 2026 / Version 1

Mathematical state: the completed 16 September 2026 continuation cycle.
This document consolidates supplied proofs and exact data. It undertakes
no new proof search, carrier test, exploratory computation, literature search,
or attack on the Cartesian-return problem.

## 1. Executive summary

**The ultimate cubic power-saving target remains OPEN.** The six-point
characteristic-zero gadget is a proved finite success. Its literal iteration
and sufficiently separated-copy repairs fail in precise, proved scopes.
Nine other tested continuations supply finite evidence, not an impossibility
theorem.

The main progression is:

$$
\begin{gathered}
\mathbb F_3\text{ collapse}\ \longrightarrow\ \text{finite }36\to22\text{ gadget}\\
\longrightarrow\ \text{failed continuation and }O(N)\text{ fixed-rule diagnosis}\\
\longrightarrow\ P\circ T_\tau=P\ \longrightarrow\
\text{partial Cartesian-return question}.
\end{gathered}
$$

The strongest actual-image conclusion is that the literal maps produce
$n_m=4\cdot2^m+2$ inputs but
$s_m=n_m^2-O(n_m^{3/2})$ outputs. Their rates are
$\lambda=2$ and $\rho=4=\lambda^2$: no exponent gain survives.
Sufficiently separated copies instead triple the inputs and expose
$6n^2$ distinct cross-copy outputs.

The conceptual diagnosis is narrower than a universal obstruction:
a bounded inventory of fixed slice or displacement rules accounts for only
$O(N)$ identifications among $N^2$ pairs. Other adaptive mechanisms remain open.

The cycle nevertheless produced an exact quadratic **pair map** $T_\tau$,
defined in Section 12, which preserves every real cubic output. It cannot
preserve a whole nonempty finite square when $\tau\ne0$. The one next
question is whether $T_1$ has positive-density partial returns to arbitrarily
large squares $A^2$.

> **Frozen disposition.** PROVED finite structure and scoped failures;
> OPEN asymptotic target and Cartesian-return question. This freeze stops
> after documentation and PDF verification. It does not begin the next attack.

“PROVED” below means proved in the identified internal source system.
The September 16 independent internal reviews are reported as such.
This September 21 task checks faithful presentation and artifact integrity;
it is not a new independent proof audit or external review.

## 2. Fixed cubic and finite-field origin

The polynomial throughout is the plus-sign cubic

$$
P(x,y)=(x-y)^3+x+y.
$$

**OPEN - ultimate target.** The target asks for one fixed $c>0$ and arbitrarily large finite
$A\subset\mathbb R$ such that

$$
|P(A,A)|\le |A|^{2-c}.
$$

The same set is used in both coordinates, and every ordered pair in $A^2$
must be covered. A finite saving, selected collisions, or high collision
energy alone does not establish this full-support upper bound. The separate
norm-trace quadratic branch and T04's differently signed cubic are not
substitutes for this fixed target.

**PROVED - finite-field inspiration.** As a function on $\mathbb F_3^2$,

$$
P(x,y)=x^3-y^3+x+y=2x=-x.
$$

Indeed the mixed binomial coefficients vanish in characteristic three,
and $z^3=z$ for $z\in\mathbb F_3$. Thus nine ordered pairs have only three
outputs: the second input disappears. The output support is still the
whole field; this is a fiber collapse, not sparse support inside $\mathbb F_3$.

**Scope.** The identity $z^3=z$ is specific to the prime field, not every
characteristic-three extension field. Over the reals the mixed terms do
not vanish. A characteristic-zero analogue therefore needs exact real
identities and endpoint membership, not an appeal to reduction modulo three.

The preceding finite-gadget report proves a separate prime-power
permutation/density obstruction, TB-L1. It is retained as historical context,
not used to convert the present real gadget into an arithmetic construction.

## 3. The six-point $36\to22$ gadget

The seed has two points. Halving its gap creates unit-separated pairs,
and shifts by thirds interleave the three branches into one six-point set.

**PROVED - frozen finite gadget (TC-A1; preceding report Sections 4-6).**

$$
A=\{0,2\},\qquad F_r(x)=\frac{x}{2}+\frac r3,\qquad r=0,1,2,
$$

$$
G=\bigcup_{r=0}^2F_r(A)=
\left\{0,\frac13,\frac23,1,\frac43,\frac53\right\},
\qquad |P(G,G)|=22.
$$

The branches $B_r=\{r/3,1+r/3\}$ are disjoint. The following table lists
**27 times every output** of each complete ordered block $P(B_r,B_s)$.

| First branch | Second branch 0 | Second branch 1 | Second branch 2 |
|---|---|---|---|
| 0 | $\{0,54\}$ | $\{-28,8,44,62\}$ | $\{-80,10,46,64\}$ |
| 1 | $\{10,28,64,100\}$ | $\{18,72\}$ | $\{-10,26,62,80\}$ |
| 2 | $\{26,44,80,170\}$ | $\{28,46,82,118\}$ | $\{36,90\}$ |

**Proof summary.** Direct substitution gives the nine supports. Their sizes
sum to 30. The complete interblock intersections in Section 4 account for
eight repetitions and no triple intersection, leaving 22 outputs.
The complete support, multiplied by 27, is

$$
\begin{gathered}
\{-80,-28,-10,0,8,10,18,26,28,36,44,46,54,\\
62,64,72,80,82,90,100,118,170\}.
\end{gathered}
$$

The old seed has outputs $\{-6,0,4,10\}$. Hence the one-step image factor
is $22/4=11/2<9$, and the normalized step factor is $11/18$.
All 36 ordered pairs of the enlarged common set are included.

**Scope.** This is a genuine finite characteristic-zero realization of
structured fiber overlap inspired by $\mathbb F_3$. It is not an exact
finite-field row collapse and does not itself give an infinite construction.
The integer set $\{0,1,2,3,4,5\}$ is a different comparison gadget, with
24 outputs; the count 22 belongs to the step-$1/3$ set above.

## 4. Every overlap has an exact explanation

The special differences are large enough to cover much of the small square.
The cubic difference can then be canceled by a shift of the anchor.

**PROVED - complete identity classification (TC-A1).** For every real $t$,

$$
\begin{aligned}
P(t,t\pm1)&=P(t,t)=2t,\\
P(t+1/3,t)&=P(t,t+2/3)=2t+10/27,\\
P(t-1/3,t)&=P(t,t-2/3)=2t-10/27.
\end{aligned}
$$

Call the last two identities $I_+(t)$ and $I_-(t)$. Endpoint membership
in $G$ gives every nonempty intersection between distinct blocks:

| Blocks | Common values, multiplied by 27 | Identity and legal anchors |
|---|---|---|
| 01, 12 | $\{62\}$ | $I_-(4/3)$ |
| 01, 20 | $\{44\}$ | $I_-(1)$ |
| 02, 10 | $\{10,64\}$ | $I_+(0),I_+(1)$ |
| 02, 21 | $\{46\}$ | $I_+(2/3)$ |
| 10, 21 | $\{28\}$ | $I_+(1/3)$ |
| 12, 20 | $\{26,80\}$ | $I_-(2/3),I_-(5/3)$ |

There are no other interblock intersections and no triple intersections.
Define the scaled difference slice

$$
S_d=\{27P(i/3,j/3):0\le i,j\le5,\ i-j=d\}.
$$

The exact whole-slice containments are

$$
S_{-2}\subset S_1,\qquad S_2\subset S_{-1},
\qquad S_{-3}\subset S_0,\qquad S_3\subset S_0.
$$

**Proof summary.** Substitute in the identities and retain precisely the
anchors whose endpoints lie in $G$. The unit-gap identities account for
six duplicates inside diagonal blocks. The other identities account for
the eight interblock duplicates in the table. Thus the output has fourteen
fibers of size two and eight singleton fibers:
$14\cdot2+8=36$ pairs and $14+8=22$ outputs.

**Scope.** These are one-variable polynomial identities producing whole-slice
containments on this seed. They are not accidental collisions, containments
between whole distinct blocks, or identities in two independently varying
seed inputs. The scale creates unit gaps; the shifts supply the endpoints.
Residues modulo three merely label the branches.

## 5. Why changing the affine scale is delicate

The cubic and linear parts scale differently. Shrinking a picture of the
gadget usually destroys the exact equalities that made it useful.

**PROVED - common-scale preservation (TC-A2).** Suppose
$P(a,b)=P(c,d)$ for distinct ordered pairs. Put $u=a-b$, $v=c-d$.
For every real $t$ and every nonzero real $h$,

$$
P(ha+t,hb+t)-P(hc+t,hd+t)
=h(h^2-1)(u^3-v^3).
$$

Moreover $u\ne v$, so the old equality survives exactly at $h=\pm1$.

**Proof.** The old equality gives
$(a+b)-(c+d)=-(u^3-v^3)$. Expansion yields the displayed formula.
If the differences also agreed, equality of the sums would recover the
same ordered pair, a contradiction. This concerns preservation of old
collisions; a new scale may create different ones.

**PROVED - affine-line classification (TC-A3).** An identity

$$
P(\alpha t+a,\beta t+b)=P(\gamma t+c,\delta t+d)
\quad\text{for every real }t
$$

has only these possibilities: the two ordered input lines coincide, or

$$
\alpha=\beta=\gamma=\delta,\qquad
(a-b)^3+a+b=(c-d)^3+c+d.
$$

**Proof.** Cubic coefficients give
$\alpha-\beta=\gamma-\delta=e$. If $e\ne0$, quadratic, linear and constant
coefficients recover respectively the coordinate difference, slope sum,
and coordinate sum, hence the identical lines. If $e=0$, both outputs are
linear in $t$; their slopes and constant terms must agree.

**Scope.** Unequal slopes cannot retain a nontrivial identity along an
entire translated slice. Finite seed-specific coincidences and other
support mechanisms are not excluded.

For the old two-point interleaving pattern, seed gap $H$ and common scale
$a$ require $aH=3q$, while
$P(t+q,t)=P(t,t+2q)$ requires $q(9q^2-1)=0$.
Distinct branches force $q=\pm1/3$ and $aH=\pm1$: this only recovers
the same six-point pattern up to translation or reflection.

## 6. Literal iteration: exact input loss

Allowing copies to overlap still creates arbitrarily large sets. The correct
input count, however, grows by a factor approaching two, not three.

**PROVED - literal input formula (TC-D1).** Start at $A_0=G$ and set

$$
A_{m+1}=\bigcup_{r=0}^2\left(\frac12A_m+\frac r3\right).
$$

For every integer $m\ge0$, with $q=2^m$,

$$
\boxed{A_m=\frac1{3q}\{0,1,\ldots,4q+1\},\qquad n_m=4q+2.}
$$

Consequently $n_{m+1}=2n_m-2$ and $\lambda=\lim n_{m+1}/n_m=2$.

**Proof.** At the next level, use denominator $6q$. The three numerator
intervals are

$$
[0,4q+1],\qquad[2q,6q+1],\qquad[4q,8q+1].
$$

Their union is $[0,8q+1]\cap\mathbb Z$, which proves induction from $G$.
The two adjacent intersections have $2q+2$ points each; the outer
intersection and the triple intersection have two each. Inclusion-exclusion
therefore gives $8q+2$ distinct points.

Each branch is injective, but merging the labels loses

$$
3n_m-n_{m+1}=n_m+2
$$

inputs relative to naive tripling. The rate comparison must charge this
loss in both coordinates.

**HISTORICAL / SUPERSEDED interpretation.** The first finite-gadget report
observed that the next branches overlap. This remains true. The later
continuation proves the stronger conclusion in Section 7: even allowing
those overlaps and their unbounded input growth does not save the mechanism.

**Scope.** The formula starts at the six-point set, not the original
two-point seed. It concerns exactly these literal maps; it does not
describe arbitrary adaptive affine branches.

## 7. Literal iteration: almost every pair is distinguishable

Close spacing in a bounded interval does not force exact outputs to
coincide. Most input differences can be recovered from the output modulo a
large power of two; the output then recovers the sum.

**PROVED - actual image theorem (TC-D2-D3).** For the literal sets, put
$s_m=|P(A_m,A_m)|$. For $m\ge4$, let

$$
T=\lfloor m/2\rfloor-1,\qquad Q=2^T,\qquad q=2^m,\qquad n=4q+2.
$$

Then

$$
n^2(1-1/Q)-2+4/Q\le s_m\le n^2.
$$

In particular,

$$
\boxed{s_m=n_m^2-O(n_m^{3/2}),\qquad
\lambda=2,\quad\rho=4=\lambda^2.}
$$

**Self-contained proof summary.** For inputs $i/(3q),j/(3q)$, clear the
denominator exactly:

$$
W(i,j)=(3q)^3P(i/(3q),j/(3q))=(i-j)^3+9q^2(i+j).
$$

Select the pairs with $Q\nmid i-j$. If two selected pairs have equal
outputs, their differences $d,d'$ satisfy
$d^3\equiv(d')^3\pmod{2^{2m}}$. Write $t=v_2(d)$, $t'=v_2(d')$.
Both are less than $T$. Unequal valuations would make the valuation of
the cube difference $3\min(t,t')<2m$, so $t=t'$.
Write $d=2^ta$, $d'=2^tb$ with $a,b$ odd. Since $a^2+ab+b^2$ is odd,

$$
2^{2m-2t}\mid d-d',\qquad
2^{2m-2t}\ge16q>8q+2\ge|d-d'|.
$$

Thus $d=d'$. Equality of $W$ recovers $i+j=i'+j'$, hence the pair itself.
The selected pairs are injective among themselves, which suffices for a
support lower bound; they need not avoid the omitted pairs' outputs.

Set $a_0=4q/Q$. Among the $n$ indices, two residue classes modulo $Q$
have $a_0+1$ members and the other $Q-2$ have $a_0$. Exactly

$$
2(a_0+1)^2+(Q-2)a_0^2=n^2/Q+2-4/Q
$$

pairs are omitted. Subtracting proves the bound. Since $Q$ is comparable
to $\sqrt n$, $s_m/n_m^2\to1$ and $s_{m+1}/s_m\to4$.

**FAILED - literal family.** Almost every pair becomes distinguishable
again. No fixed positive power saving survives. This is an actual-image
result, not failure of an upper-bound certificate. It does not rule out
other adaptive affine constructions.

## 8. Sufficiently separated copies expose the cross pairs

Large separation fixes disjointness while keeping each intact copy's
internal collisions. But outputs between two different copies then record
both endpoints, and those six blocks dominate.

**PROVED - separated-copy theorem (TC-D4-D5).** For a fixed nonempty finite
real set $C$, write $n=|C|$, $s=|P(C,C)|$. For all sufficiently large
positive $H$, and more generally outside a finite exceptional set with
disjoint copies,

$$
B=C\sqcup(C+H)\sqcup(C+2H),\qquad
\boxed{|P(B,B)|=6n^2+3s.}
$$

**Proof.** For $x,y\in C$, $r,t\in\{0,1,2\}$, set $k=r-t$, $u=x-y$.
The output polynomial in $H$ is

$$
\begin{aligned}
P(x+rH,y+tH)={}&k^3H^3+3k^2uH^2\\
&+(3ku^2+r+t)H+u^3+x+y.
\end{aligned}
$$

If $k\ne0$, its coefficients recover $k,u,r+t,x+y$, and hence
$r,t,x,y$. All $6n^2$ cross-copy output polynomials are therefore distinct.
The same-copy blocks give exactly $3s$ distinct linear polynomials
$2rH+z$, $z\in P(C,C)$. No cubic equals one of these linear polynomials.
Two distinct polynomials agree at finitely many $H$; the finite union
of these exceptional values proves the count.

For $C=G$, this yields $282$ outputs on $18$ inputs, so
$\rho=282/22=141/11>9$. Repeated unscaled admitted separations satisfy

$$
\frac{s_{m+1}}{n_{m+1}^2}
=\frac13\frac{s_m}{n_m^2}+\frac23\longrightarrow1.
$$

If a nonzero common scale $a$ is fixed before choosing $H$, the same
argument gives $6n^2+3|P(aC,aC)|\ge(2/3)|B|^2$.

**FAILED in scope.** Such sufficiently separated stages cannot give a
power saving, even with stage-dependent common scales. The theorem fixes
$C$ and its scale first. It does not exclude deliberately exceptional
separations, unequal scales, or other coupled parameter choices.

## 9. Why finitely many slice rules cannot scale

A fixed difference has at most $N$ pairs on an $N$-point set. A few
difference rules can matter greatly on six points, but cover only a small
part of a growing Cartesian square.

**PROVED - difference mass and displacement bounds (TC-A4-A5).**
For any $N$-point real set $C$, $L$ selected differences cover at most
$LN$ ordered pairs. Consequently, covering all but
$O(N^{2-\delta})$ pairs this way requires
$L\ge N-O(N^{1-\delta})$.

For $M$ nonzero fixed pair displacements $(h,k)$, draw an equality edge
whenever both endpoints lie in $C^2$ and the displacement preserves $P$.
There are at most $2MN$ directed edges and at least $N^2-2MN$
connected components in the underlying equality graph.

**Proof.** A fixed difference and second coordinate determine at most one
first coordinate. For a displacement, write $u=x-y$, $e=h-k$:

$$
P(x+h,y+k)-P(x,y)=3eu^2+3e^2u+e^3+h+k.
$$

If $e\ne0$, this has at most two real roots, each allowing at most $N$
source pairs. If $e=0$, equality forces $h+k=0$, hence the excluded zero
displacement. Each edge reduces the component count by at most one.

The original gadget needs just two moves:

$$
(x,y)\mapsto(x,y+1),\qquad
(x,y)\mapsto(x-1/3,y+2/3).
$$

They work at differences $\{0,1\}$ and $\{1/3,2/3\}$ respectively.
Together they supply at most $4N$ edges on any carrier.

**FAILED certificate, not universal actual-image theorem.** A bounded
inventory produces only $O(N)$ systematic identifications among $N^2$
pairs. Even parameters chosen adaptively at each stage do not remove the
inventory cost. Distinct graph components could still share outputs by
unlisted relations. Only an additional hypothesis that these moves connect
every actual output fiber converts the component bound to an image bound.

**PROVED - inherited-copy limitation (TC-A6).** For $h\ne0$, take disjoint common-scale copies

$$
C=\bigsqcup_{t\in E}(t+hG),\qquad |E|=m,\qquad N=6m.
$$

An old equality with differences $u,v$ survives inside centers of
difference $D$ precisely when

$$
3D^2+3hD(u+v)+(h^2-1)(u^2+uv+v^2)=0.
$$

Expansion gives this factor after removing $h(u-v)\ne0$. There are at
most two allowed center differences per equality, each realized at most
$m$ times. The fourteen old matchings supply at most $28m$ edges among
$36m^2$ pairs. New cross-copy equalities remain outside this certificate.

## 10. Exact continuation experiments

**EXPERIMENTAL exact - TC-E1.** Nine predetermined rational affine rules
were evaluated over three successive levels from $G$:

$$
6\longrightarrow18\longrightarrow54\longrightarrow162.
$$

Every tested step has $\lambda_m=3$. The complete scalar images were
computed with exact rational arithmetic, without floating-point equality
tests. No experiment is rerun for this freeze.

Rules 1-8 use $F_r(x)=ax+r(q+1/p)$, where $D=\max A-\min A$ and $p\ge5$
is the smallest fresh prime larger than the preceding one and dividing
none of the denominators of $aA,a,q$.

| Rule | Scale $a$ | Base shift $q$ |
|---|---|---|
| 1. Intact, near gap | $1$ | $D$ |
| 2. Intact, wider gap | $1$ | $D+1$ |
| 3. Half scale, near gap | $1/2$ | $D/2$ |
| 4. Intact, perturbed thirds | $1$ | $1/3$ |
| 5. Half scale, perturbed thirds | $1/2$ | $1/3$ |
| 6. Alternating scale | $2$ at odd levels, $1/2$ at even levels | $1/3$ |
| 7. Stage-dependent shrink | $1/(m+1)$ at level $m\ge1$ | $1/3$ |
| 8. Diameter reset | $(5/3)/D$ | $1/3$ |
| 9. Exact thirds | $1/p$, with fresh $p>3D$ | Exact shifts $r/3$ |

For rule 9, $p$ also exceeds the preceding prime and avoids old denominators.

**PROVED input statement - TC-E2.** These rules triple inputs at every
level if continued: rules 1-8 cannot collide between branches because the
nonzero $(r-s)/p$ term is not integral at $p$, while the other terms are.
Rule 9's intervals have width less than $1/3$. Fresh denominator primes
actually occur: zero persists, and rules 1-8 contain $q+1/p$; in rule 9,
repeated branch zero retains $1/(3\prod p)$. This is an input theorem,
not an all-level output theorem.

Write $\rho_j=s_j/s_{j-1}$. Starting from $s_0=22$, the recorded complete
counts and normalized step factors are:

| Rules | $s_1$ | $s_2$ | $s_3$ | $\rho_1/9$ | $\rho_2/9$ | $\rho_3/9$ |
|---|---|---|---|---|---|---|
| 1, 2, 4 | 282 | 2790 | 25866 | $47/33$ | $155/141$ | $479/465$ |
| 3, 5, 7 | 312 | 2916 | 26244 | $52/33$ | $27/26$ | $1$ |
| 6 | 324 | 2790 | 26226 | $18/11$ | $155/162$ | $47/45$ |
| 8 | 282 | 2916 | 26244 | $47/33$ | $54/47$ | $1$ |
| 9 | 288 | 2880 | 26136 | $16/11$ | $10/9$ | $121/120$ |

No rule sustained a normalized gain over all three steps. Rule 6 temporarily
lowered density at the second step, then lost that gain at the third.

The data retain all nine block supports, every scalar pair, multiplicities,
difference slices and higher intersection masks. These are full scalar
counts, not formal block-label counts. The old two templates explain the
following savings; other equalities are not classified as accidental.

| Rules | Old-template savings at levels 1, 2, 3 | Additional savings |
|---|---|---|
| 1, 2, 4 | $(42,126,378)$ | $(0,0,0)$ |
| 3, 5, 7 | $(12,0,0)$ | $(0,0,0)$ |
| 6 | $(0,126,0)$ | $(0,0,18)$ |
| 8 | $(42,0,0)$ | $(0,0,0)$ |
| 9 | $(12,36,108)$ | $(24,0,0)$ |

For example, further frozen identities include
$P(t,t+3/7)=P(t,t+5/7)=2t+120/343$ and
$P(t+26/21,t)=P(t+34/21,t+8/3)$. They explain finite extra
coincidences but supply no proved repeatable rate.

The recorded run used 27 steps, 265,392 polynomial evaluations and
7.432394 research CPU seconds on CPython 3.12.7, within its announced
16-rule, 120-step, 162-input, three-million-evaluation, 90-CPU-second limits.
The prior 980-gadget grid was not repeated.

**Scope.** Three finite levels do not establish asymptotic impossibility.
Growing prime support escapes that hypothesis of the older fixed-prime
obstruction, but escaping a no-go theorem is not a positive construction.

## 11. The corrected rate criterion

Input losses must be squared in the comparison. A small output factor
alone is not enough if the input factor has also fallen.

**PROVED implication - TC-R2.** Suppose $n_m\to\infty$ and eventually

$$
\liminf_{m\to\infty}\frac{n_{m+1}}{n_m}\ge\lambda>1,\qquad
s_{m+1}\le\rho s_m+C n_m^{2-\delta},
$$

with fixed $C\ge0$, $\delta>0$ and $1\le\rho<\lambda^2$.
Then every fixed

$$
\boxed{0<c<\min\{2-\log_\lambda\rho,\delta\}}
$$

eventually satisfies $s_m\le n_m^{2-c}$.

**Proof summary.** Choose $p>0$ strictly between
$\max\{\log_\lambda\rho,2-\delta\}$ and $2-c$.
Choose $1<\lambda_0<\lambda$ with $\rho<\lambda_0^p$.
Eventually $n_{m+1}\ge\lambda_0n_m$. Since $p>2-\delta$, a fixed
constant $K$ can absorb the error:

$$
s_{m+1}\le K\rho n_m^p+C n_m^{2-\delta}
\le K\lambda_0^p n_m^p\le K n_{m+1}^p.
$$

Induction supplies $s_m\le K n_m^p$. The strict inequality $p<2-c$
absorbs $K$ for large $m$. The endpoint exponent is not asserted.

**PROVED correction - TC-R1.** The condition $n_{m+1}/n_m\to\lambda$
gives $n_m=\lambda^{m+o(m)}$, not necessarily $n_m\asymp\lambda^m$.
This follows by summing logarithms; $\lfloor\lambda^m/(m+1)\rfloor$
shows why a constant-factor comparison need not hold.

**PROVED finite diagnostic - TC-R3.** Defining
$\lambda_m=n_{m+1}/n_m$, $\rho_m=s_{m+1}/s_m$ gives

$$
\frac{\rho_m}{\lambda_m^2}
=\frac{s_{m+1}/n_{m+1}^2}{s_m/n_m^2}.
$$

A good step lowers normalized output density. A uniform exponential
improvement, with the requisite input growth control, is what can produce
a fixed power saving. For $\lambda=3,\rho=8$, the strict allowable gap
is below $2-\log_3 8\approx0.10721$, also limited by $\delta$.

**CONDITIONAL application.** This is a proved implication. No frozen
candidate supplies all its uniform hypotheses.

## 12. The quadratic pair symmetry

The original rules use constant coordinate shifts and work only at a few
differences. The pair symmetry instead adjusts the motion to the current
difference. It preserves the cubic output for every real pair.

**PROVED - TC-Q1.** Put $u=x-y$. For any real $\tau$, define

$$
H_\tau(u)=3\tau u^2+3\tau^2u+\tau^3=(u+\tau)^3-u^3
$$

and

$$
\boxed{
T_\tau(x,y)=
\left(x+\frac{\tau-H_\tau(u)}2,\;
y-\frac{\tau+H_\tau(u)}2\right).
}
$$

For all real $x,y,\sigma,\tau$,

$$
\boxed{P(T_\tau(x,y))=P(x,y),\qquad
T_\sigma\circ T_\tau=T_{\sigma+\tau}.}
$$

Also $T_0$ is the identity and $T_\tau^{-1}=T_{-\tau}$.

**Proof.** Let $(x',y')=T_\tau(x,y)$ and $s=x+y$. Subtracting and
adding the new coordinates gives

$$
u'=x'-y'=u+\tau,\qquad
s'=x'+y'=s-H_\tau(u).
$$

Therefore

$$
P(x',y')=(u+\tau)^3+s-H_\tau(u)=u^3+s=P(x,y).
$$

Applying $\tau$ and then $\sigma$ changes the difference to
$u+\tau+\sigma$. The two changes of the sum telescope:

$$
s+u^3-(u+\tau)^3+(u+\tau)^3-(u+\tau+\sigma)^3
=s+u^3-(u+\tau+\sigma)^3.
$$

Difference and sum determine the ordered pair, proving the composition
law and inverse.

The gadget identity is an exact special case:

$$
T_{-1}(t+1/3,t)=(t,t+2/3).
$$

**Significance and scope.** This is a global output-preserving quadratic
map of the plane. It is a **pair map**, not a one-variable branch applied
independently to each coordinate. Output invariance on the plane does not
supply a finite common scalar set with many legal returns. No novelty or
arithmetic amplification is claimed.

## 13. Why full finite-square invariance is impossible

An output-preserving motion need not keep both coordinates in the chosen
set. Here the difference always advances by the same nonzero amount,
so an extremal difference must leave a finite difference set.

**PROVED - TC-Q2.** For every nonempty finite $A\subset\mathbb R$ and
every $\tau\ne0$,

$$
T_\tau(A^2)\not\subseteq A^2.
$$

**Proof.** The differences of pairs in $A^2$ form the finite nonempty set
$A-A$. If $\tau>0$, choose a pair attaining its largest difference.
Its transformed difference is larger by $\tau$ and is outside $A-A$.
For $\tau<0$, use the smallest difference. Thus at least one pair leaves
the square.

**Scope.** This closes exact invariance of a whole finite square under
one nontrivial motion. It gives no asserted asymptotic bound on the
proportion of pairs which do return.

The exact endpoint condition for partial returns is already frozen in
the source. Let $A_u=A\cap(A-u)$ and write the source pair as $(a+u,a)$.
Then a return requires

$$
u+\tau\in A-A,\qquad a\in A_u,
$$

$$
a+\frac{u^3+u-(u+\tau)^3-(u+\tau)}2\in A_{u+\tau}.
$$

This is the old collision equation with all endpoint restrictions retained.
It is a description of legal returns, not a construction satisfying it
at positive density. Taking all coordinates from selected moving pairs
also creates new cross pairs; their outputs cannot be omitted.

## 14. The Cartesian-return problem remains open

The new frontier asks whether the global pair motion can meet a large
part of a finite Cartesian square even though it cannot preserve all of it.

**OPEN - the frozen quantity.** For $N\ge1$, define

$$
\boxed{
R_1(N)=
\sup_{\substack{A\subset\mathbb R\\ |A|=N}}
\frac{|\{(x,y)\in A^2:T_1(x,y)\in A^2\}|}{N^2}.
}
$$

The question concerns arbitrarily large one-dimensional real sets whose
square contains a positive proportion of pairs returning under $T_1$.
The sign is deliberate: $T_1$ is the inverse direction of the gadget's
$T_{-1}$ matching.

**CONDITIONAL significance, not a solved consequence.** A positive
$\limsup R_1(N)$ would mean that some fixed positive proportion of the
$N^2$ pairs return along arbitrarily large sizes. This would provide
quadratically many exact output-preserving pair relations arising from
the gadget's pair symmetry, beyond the old bounded-list $O(N)$ mechanism.

It would not automatically hold for every sufficiently large size.
More importantly,

$$
\boxed{\text{Positive-density returns alone do not prove power saving.}}
$$

Large output fibers or a complete support compression argument would
still have to be established. This freeze does not attempt either step,
test a carrier, improve a constant, or decide the return question.

**Current bottleneck.** The algebraic symmetry is fully explicit.
What is missing is quantitative compatibility with a common Cartesian
input set, followed by the stronger control needed for the entire image.

## 15. The conceptual transition

The results form a progression, not a claim that finite-field compression
automatically transfers to growing real sets.

| Stage | Frozen mathematical content | Status |
|---|---|---|
| Finite-field inspiration | On $\mathbb F_3$, $P(x,y)=-x$ | PROVED |
| Finite real realization | The six-point $G$ has 36 pairs and 22 outputs | PROVED |
| Literal continuation | Actual rates satisfy $\rho=4=\lambda^2$ | FAILED family |
| Separated-copy repair | Six cross-copy blocks give $6n^2$ outputs | FAILED in scope |
| Quantitative diagnosis | Bounded fixed rules supply only $O(N)$ identifications | PROVED certificate bound |
| Global pair motion | $P\circ T_\tau=P$, with additive composition | PROVED |
| Cartesian compatibility | Positive-density partial returns under $T_1$ | OPEN |

$$
\begin{gathered}
\boxed{\text{finite special collisions}}\\
\downarrow\\
\boxed{\text{failed recursive gadget}}\\
\downarrow\\
\boxed{\text{global output-preserving pair symmetry}}\\
\downarrow\\
\boxed{\text{Cartesian-return problem}}.
\end{gathered}
$$

The move from fixed shifts to a difference-dependent quadratic motion is
the structural outcome of the completed cycle. It is not a completed
construction, a novelty claim, or authorization to begin the next problem.

## 16. Claim and status ledger

All entries concern T01's fixed plus-sign cubic and the completed
16 September 2026 sources, frozen here on 21 September. Proofs are
identified internal proofs, reproduced or faithfully summarized above.
No new research theorem is asserted by this document.

| Source claim | Frozen status and scope | Proof locator |
|---|---|---|
| Finite-field identity | PROVED on $\mathbb F_3^2$ as a function | Preceding report Section 3; here Section 2 |
| TC-A1 | PROVED: all 14 savings of this $G$ | Affine companion Section 1; here Sections 3-4 |
| TC-A2-A3 | PROVED: preservation of old collisions; full affine-line identities | Affine companion Sections 2-3; here Section 5 |
| TC-A4-A5 | PROVED: finite difference/displacement inventory bounds | Affine companion Section 4; here Section 9 |
| TC-A6 | PROVED: inherited same-copy-pair matching bound | Affine companion Section 5; here Section 9 |
| TC-D1-D3 | PROVED / FAILED family: literal inputs and actual image | Direct companion Sections 1-2; here Sections 6-7 |
| TC-D4-D5 | PROVED / FAILED class: sufficiently separated copies | Direct companion Section 3; here Section 8 |
| TC-E1 | EXPERIMENTAL exact: nine rules, three levels | Stored exact JSON; here Section 10 |
| TC-E2 | PROVED inputs only: tripling and growing prime support | Continuation report Section 8; here Section 10 |
| TC-R1-R3 | PROVED rate implications and finite diagnostic | Rates companion Sections 1-3; here Section 11 |
| TC-Q1-Q2 | PROVED: pair symmetry and failure of full finite-square invariance | Rates companion Sections 4-5; here Sections 12-13 |
| Uniform favorable recurrence | CONDITIONAL application; no witness supplied | Here Section 11 |
| Adaptive continuation, $R_1$, ultimate target | OPEN | Continuation report Section 13; here Sections 14 and 18 |

No EXTERNAL RESULT is needed for the displayed elementary proofs.
Historical fixed-prime and rich-fiber statements retain their source
availability limits in Section 19. Internal proof reviews are not external
peer review; novelty has not been assessed.

## 17. Failure scopes and quantitative bookkeeping

Each failure has a defined scope. None disproves the original cubic target.

| Result | What it closes | What it leaves open |
|---|---|---|
| Literal iteration | Exactly $A_{m+1}=A_m/2+\{0,1/3,2/3\}$ from $G$ | Other adaptive affine constructions |
| Separated copies | Fixed carrier and common scale, separation avoiding a finite exceptional set | Exceptional separations and coupled parameters |
| Bounded-rule count | A bounded inventory of fixed difference/displacement identities | Growing inventories and unlisted collisions |
| Inherited-copy bound | The 14 old matchings in a fixed ordered copy pair | New cross-copy equalities |
| Nine continuation tests | Only the recorded three levels and parameters | Their unproved asymptotics and other rules |
| Full-square obstruction | Exact $T_\tau(A^2)\subseteq A^2$ for $\tau\ne0$ | Partial returns |
| Pair symmetry | Exact invariance of outputs in the plane | Independent one-variable branches and Cartesian compression |

The construction ledger uses actual scalar sizes and actual depth.
For literal iteration, inputs are exactly $4\cdot2^m+2$, the image is
$n_m^2-O(n_m^{3/2})$, and the input/output logarithmic rates are
$\log2$ and $2\log2$: the net gap is zero.
The $n_m+2$ duplicate input labels per step are charged in both coordinates.

For separated copies, inputs are exactly $3n$ and all nine blocks are
counted. The six cross blocks already give at least two thirds of the
new square's size. For the tests, all scalar pairs are counted once;
denominators, heights, diameters, blocks and intersections are retained
in the exact data. Unknown extra collisions are not credited as savings.

Congruences in the literal proof establish injectivity; fresh primes in
the tested rules establish disjointness. Neither is an uncharged output
saving. These real or rational arguments require no field-degree,
discriminant, regulator, splitting, norm or trace estimates.
Chebotarev, Golod-Shafarevich and arithmetic towers have no justified
amplification role until a reusable positive scalar rate exists.

## 18. Exactly one next proof obligation

**OPEN - retained verbatim in mathematical content, not attempted.**

$$
\boxed{
\text{Decide whether }\limsup_{N\to\infty}R_1(N)>0,
\quad\text{or prove }R_1(N)\to0.
}
$$

Here $R_1(N)$ is exactly the supremum defined in Section 14 for the
specific quadratic motion $T_1$ of Section 12. A positive outcome requires
a growing carrier witnessing positive-density partial returns. The other
outcome is an asymptotic vanishing statement.

This is the sole next obligation of this frozen branch. It supersedes
the preceding finite-gadget report's earlier recommendation only in the
chronology of the completed continuation. It is not a new task launched
by this freeze.

Even a positive answer would be an intermediate result. The ultimate
target

$$
|P(A,A)|\le |A|^{2-c}\quad\text{for one fixed }c>0
$$

on arbitrarily large finite common real sets remains **OPEN**.
No assertion here disproves that target or proves the desired saving.

## 19. Sources, chronology and final freeze

The primary authority is the completed
[continuation report](../2026-09-16-three-branch-continuation/README.md),
with these explicitly referenced companions:

- [Affine mechanism](../2026-09-16-three-branch-continuation/affine-mechanism.md):
  TC-A1-A6, exact identities, scopes and inherited-copy accounting.
- [Direct iteration and separated copies](../2026-09-16-three-branch-continuation/direct-iteration.md):
  TC-D1-D5, full elementary proofs.
- [Rates and pair maps](../2026-09-16-three-branch-continuation/rates-and-fiber-maps.md):
  TC-R1-R3 and TC-Q1-Q2.
- [Continuation verification](../2026-09-16-three-branch-continuation/verification.md):
  historical internal audits, code/data hashes and regression results.
- [Preceding finite-gadget report](../2026-09-16-three-branch-lift/README.md):
  the finite-field motivation, full nine-block table and earlier chronology.
- [Exact continuation summary](../../../examples/2026-09-16-three-branch-continuation.json)
  and [preserved implementation](../../../experiments/three_branch_continuation.py).

**Chronology.** The finite-gadget cycle proved $36\to22$ and noticed failed
disjointness. The later continuation proved the actual-image failure even
with overlaps, corrected the input-rate shorthand, and selected the
$R_1$ question. The old records are preserved, not silently rewritten.

The 20 September intake contains recovery addenda and Markdown manifests
only. They report recovery of the older full digital and rich-fiber proofs
in another package; their original bytes were not received locally.
Their mathematical cutoff is 10 September, so they do not supersede the
16 September continuation. See MC-06 in the
[migration conflict register](../../MIGRATION_CONFLICTS.md).
The new continuation proofs are locally present and independent of those
missing older originals.

**Verification boundary.** The 16 September record reports 52 tests and
159 finite baseline checks. Those are inherited results, not reruns in this
freeze. This task checks source hashes and faithful transcription, builds
the PDF locally, inspects rendered pages, and runs documentation/setup
integrity checks. Details and final outcomes are in
[verification.md](verification.md). No research computation or new
independent proof audit is claimed.

The 27 lossless continuation certificates remain under the ignored
local-only/runs/T01/2026-09-16-three-branch-continuation/ directory and must
travel separately in a local handoff. The Markdown is the searchable,
editable formula source; the PDF is the frozen reading edition.

No asymptotic impossibility theorem is claimed for the nine experimental rules.

> **FINAL FREEZE.** The six-point characteristic-zero Frobenius gadget is
> genuine but its tested affine continuation mechanisms do not yield an
> asymptotic power saving. Literal iteration has critical rate
> $\rho=\lambda^2$, sufficiently separated copies recover quadratic
> cross-pair complexity, and a bounded list of slice rules supplies only
> $O(N)$ systematic identifications. The cycle nevertheless reveals an
> exact quadratic pair symmetry $T_\tau$ satisfying $P\circ T_\tau=P$.
> The next research problem is whether $T_1$ can have a positive proportion
> of returns to $A^2$ on arbitrarily large finite real sets.
>
> **The original T01 target remains OPEN. Research is stopped at this
> checkpoint; the Cartesian-return problem has not been attempted.**
