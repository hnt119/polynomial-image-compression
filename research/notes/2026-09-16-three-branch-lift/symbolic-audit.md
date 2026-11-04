# T01 three-branch lift: symbolic rigidity and generic seeds

Date/version: 2026-09-16, v1. Fixed polynomial throughout:

$$P(x,y)=(x-y)^3+x+y.$$

This note records new internal proofs for the user-authorized, strictly offline
three-branch research cycle. No mathematical experiment or network request was
performed by this subtask. The results concern specified classes; the original
arbitrarily-large-real-set problem remains **OPEN**. The lead independently checked every proof below after this note was written. There is no external novelty claim.

The inherited source state was read in `docs/CODEX_SETUP.md`,
`research/CURRENT_PROJECT_MAP.md`, `research/CODEX_MIGRATION_AUDIT.md`,
`local-only/migration/sources/00_MASTER_HANDOFF.md`,
`local-only/migration/sources/T01_CURRENT_STATE.md` (particularly §§4, 6–8,
13–15), the separate `T01_Norm_Trace_Quadratic_Research_Checkpoint.md`, and
T01 `SPEC.md`/`STATUS.md`. The migration conflicts and relevant mechanism,
failure and open-lemma entries were consulted. No supplied historical proof is
claimed to have been independently re-audited by this note.

## 1. TB-A1: separable scalar rigidity

**PROVED internally.** Suppose $H:I\to\mathbb R$ and $K:J\to\mathbb R$ are
nonconstant real analytic functions on open intervals and

$$P(H(X),K(Y))=aP(X,Y)+b\quad(X\in I,Y\in J),\qquad a\ne0.$$

Then, for some $t\in\mathbb R$ and $\varepsilon\in\{1,-1\}$,

$$H(X)=\varepsilon X+t,\quad K(Y)=\varepsilon Y+t,
\quad a=\varepsilon,\quad b=2t.$$

The proof only needs smoothness on subintervals where derivatives are nonzero;
analyticity extends the conclusions to the original intervals.

**Proof.** The mixed derivative gives

$$[H(X)-K(Y)]H'(X)K'(Y)=a(X-Y).\tag{1}$$

Restrict to subintervals on which both derivatives are nonzero. Pick $Y_1,Y_2$
with $K(Y_1)\ne K(Y_2)$. Equation (1) at those two points is a nonsingular
linear system for $HH'$ and $H'$, so both are affine functions of $X$.
Write $H'=pX+q$ and integrate:
$H=pX^2/2+qX+r$. Since $HH'$ is affine, its cubic coefficient $p^2/2$
vanishes; hence $p=0$. Thus $H=\alpha X+\beta$ with $\alpha\ne0$.
The same argument gives $K=\gamma Y+\delta$, $\gamma\ne0$.
The coefficients in (1) imply

$$\alpha^2\gamma=a,\quad\alpha\gamma^2=a,\quad\beta=\delta.$$

Therefore $\alpha=\gamma$, $a=\alpha^3$, and the original identity becomes

$$\alpha^3(X-Y)^3+\alpha(X+Y)+2\beta
=a(X-Y)^3+a(X+Y)+b.$$

Thus $\alpha^3=\alpha\ne0$, proving the assertion. ∎

**Consequences.** If four nonconstant real analytic functions $f,g,h,k$ on
one open interval obey

$$P(f(x),g(y))=P(h(x),k(y))\quad\text{for all }x,y,$$

then $f=h$ and $g=k$. Indeed locally invert $f,g$, apply the theorem with
$a=1,b=0$, and extend analytically. In particular distinct branches cannot
have identical scalar block parameterizations with the same ordered seed
variables. This includes real algebraic and radical branches on any common
analytic interval, and does not presume affinity or fixed digital structure.

Also $P(f(x),g(y))$ genuinely depends on both variables: its derivatives are

$$[1+3(f-g)^2]f'(x),\qquad[1-3(f-g)^2]g'(y).$$

Neither vanishes identically when $f,g$ are nonconstant. Thus the second
coordinate cannot disappear as a two-variable real analytic identity.

## 2. TB-A2: swapped separable identities are impossible over the reals

**PROVED internally.** There are no four nonconstant real analytic functions
with

$$P(f(x),g(y))=P(h(y),k(x))$$

identically on an open Cartesian square.

**Proof.** Locally put $X=f(x)$, $Y=g(y)$,
$H(X)=k(f^{-1}(X))$, $K(Y)=h(g^{-1}(Y))$. The identity becomes

$$P(K(Y),H(X))=P(X,Y).$$

The mixed derivative is now

$$[H(X)-K(Y)]H'(X)K'(Y)=-(X-Y).$$

The rank-two argument in §1 makes $H,K$ affine. Coefficient comparison gives
$H=\alpha X+t$, $K=\alpha Y+t$, with $\alpha^3=-1$, hence $\alpha=-1$.
The left side of the original identity is consequently
$(X-Y)^3-X-Y+2t$, which cannot equal $(X-Y)^3+X+Y$ on an open set. ∎

Realness is essential in this step; the argument must not be imported without
checking signs into the other cubic or a complex-coordinate problem.

## 3. TB-A3: rational branches cannot nontrivially factor through the old P

**PROVED internally.** Let $f,g$ be nonconstant rational functions with real
coefficients. Let $\Psi$ be an algebraic one-variable function, with branches
chosen so that

$$P(f(x),g(y))=\Psi(P(x,y))\tag{2}$$

on a nonempty real open rectangle. Then

$$f(x)=\varepsilon x+t,\quad g(y)=\varepsilon y+t,
\quad\Psi(z)=\varepsilon z+2t,\qquad \varepsilon\in\{1,-1\}.$$

Here $\Psi$ denotes the germ realized in (2); no assertion about other branches
of a reducible presentation of its algebraic equation is intended.

**Proof.** Complexify the rational identity and write $u=x-y$, $z=P(x,y)$.
The inverse formulas

$$x=(z-u^3+u)/2,\qquad y=(z-u^3-u)/2$$

give $\mathbb C(x,y)=\mathbb C(z)(u)$. A rational function in the independent
variable $u$ algebraic over $\mathbb C(z)$ belongs to $\mathbb C(z)$:
otherwise its nonconstant rational relation would make $u$ algebraic over an
algebraic extension of $\mathbb C(z)$, a contradiction. Thus the realized
$\Psi$ is rational.

If $\Psi$ had a finite pole $c\in\mathbb C$, the right side of (2) would have
a pole along the irreducible curve $P(x,y)=c$. In coordinates $(u,z)$ this is
$z=c$, and its displayed parameterization shows it is neither vertical nor
horizontal. The left side has poles only on finitely many vertical/horizontal
lines, those coming from $f$ and $g$. This contradiction proves $\Psi$ is a
polynomial. A finite pole of $f$ or $g$ gives a noncanceling pole of order
three times its order on the left of (2): view it as a polynomial in $f$ over
$\mathbb C(y)$, or in $g$ over $\mathbb C(x)$. Therefore $f,g$ are also
polynomials.

Let $d=\deg\Psi$. Degree in $x$ and $y$ gives $\deg f=\deg g=d$.
If their leading coefficients are $A,B$, and that of $\Psi$ is $C$, the
highest homogeneous parts satisfy

$$(Ax^d-By^d)^3=C(x-y)^{3d}.$$

Taking a cube root in the polynomial identity gives
$Ax^d-By^d=D(x-y)^d$ for a nonzero constant $D$. For $d>1$ the right side
has a nonzero $x^{d-1}y$ coefficient, whereas the left side has none. Hence
$d=1$. Apply §1. ∎

**Scope.** This settles exact scalar factor-through identities for rational
input branches, including stage-dependent rational coefficients when each
stage identity holds on an open rectangle. It does not classify arbitrary
algebraic input branches with a nonlinear algebraic $\Psi$, factorization
through several invariants, or identities valid only on a structured finite
set. Those are outside the theorem, not claims of viability.

## 4. TB-A4: complete generic-seed image count

**PROVED internally.** Fix three distinct nonconstant real algebraic analytic
functions $F_0,F_1,F_2$ on one open interval $I$. Let $K\subset\mathbb R$ be
the field generated by the finitely many coefficients in algebraic equations
for these functions. Take $a_1,\ldots,a_n\in I$ algebraically independent over
$K$, and put

$$A=\{a_1,\ldots,a_n\},\qquad A'=\bigcup_{r=0}^2F_r(A).$$

Then every branch is injective on $A$, the three branch sets are pairwise
disjoint, and $|A'|=3n$. Define the nine diagonal algebraic functions

$$D_{rs}(x)=P(F_r(x),F_s(x)).$$

Let $q$ be the number of distinct nonconstant functions among them, and $c$
the number of distinct constant functions among them. Then

$$|P(A,A)|=n^2,\qquad
\boxed{|P(A',A')|=9n(n-1)+qn+c.}\tag{3}$$

Moreover $3\le q\le9$, $q+c\le9$, so

$$9n^2-6n\le |P(A',A')|\le9n^2.$$

**Algebraic genericity fact used.** A nonzero algebraic function in independent
variables cannot vanish at an algebraically independent tuple over its
coefficient field where its analytic branch is defined. For a proof, its
minimal polynomial over the rational-function field has nonzero constant
coefficient (otherwise it has a factor $T$). After clearing denominators,
vanishing of the function forces vanishing of a nonzero coefficient
polynomial. The exceptional singular/denominator sets are also excluded by
algebraic independence. This applies after repeated variable indices are
identified, using the resulting analytic algebraic function in the distinct
variables.

**Proof of (3).** Equalities $F_r(a_i)=F_s(a_j)$ are nonidentical algebraic
equations unless $(r,i)=(s,j)$: for $i\ne j$ the variables are independent,
and for $i=j$, $r\ne s$, the functions were assumed distinct. Thus the input
count is $3n$.

Consider the $9n(n-1)$ outputs

$$P(F_r(a_i),F_s(a_j)),\qquad i\ne j.$$

Every corresponding algebraic function genuinely depends on its two seed
variables (§1). An identity between two of these outputs therefore requires
the same unordered pair of seed indices. If their ordering agrees, §1 forces
the same two branch maps. If it is reversed, §2 rules the identity out.
Genericity now proves all $9n(n-1)$ scalar outputs are distinct. The same
two-variable dependence prevents equality with a diagonal output
$D_{tu}(a_k)$, which depends on at most one seed variable.

For the remaining $9n$ input pairs with equal seed index, each distinct
nonconstant function contributes $n$ values. No two of those values coincide
unless both the function and seed index agree. Distinct constant functions
contribute exactly $c$ more values, distinct from all the nonconstant ones.
This proves (3). Finally the three functions $D_{rr}=2F_r$ are distinct and
nonconstant, so $q\ge3$. The argument applied to the single identity branch
also gives $|P(A,A)|=n^2$. ∎

**Quantitative no-go.** There are no fixed $\rho<9$, $\delta>0$, $C<\infty$
for which

$$|P(A',A')|\le\rho |P(A,A)|+Cn^{2-\delta}$$

holds on all such generic seeds of unbounded size. Equation (3) would imply
$(9-\rho)n^2\le6n+Cn^{2-\delta}$, impossible as $n\to\infty$.
This is an actual full-image statement, not a collision-energy inference.

**Boundary of the result.** The branches are fixed before the seed is chosen
generically over their coefficient field. The theorem allows different
branches at different stages only if that stage's seed has the stated
independence. It does not exclude coefficients chosen from the seed itself,
arithmetic/algebraically dependent seeds, finite exceptional gadgets, arbitrary
branch permutations of a structured finite set, or recursive sets whose
defining identities make them nongeneric. It proves no universal impossibility
for the fixed cubic. It also does not turn a lack of pointwise identities
alone into a lower bound on arbitrary finite seeds; algebraic independence is
the additional substantive hypothesis.

## 5. Nine affine block formulas and a finite diagonal collapse

For arbitrary affine branches $F_r(x)=\lambda_rx+t_r$, put
$d_{rs}=t_r-t_s$. For all nine $(r,s)\in\{0,1,2\}^2$, exactly

$$\begin{aligned}
P(F_r(x),F_s(y))={}&\lambda_r^3x^3
-3\lambda_r^2\lambda_sx^2y
+3\lambda_r\lambda_s^2xy^2-\lambda_s^3y^3\\
&+3d_{rs}(\lambda_r^2x^2-2\lambda_r\lambda_sxy+
\lambda_s^2y^2)\\
&+(3d_{rs}^2+1)\lambda_rx+(1-3d_{rs}^2)\lambda_sy
+d_{rs}^3+t_r+t_s.
\end{aligned}\tag{4}$$

For common scale $\lambda$ and $u=x-y$, this is

$$\lambda^3u^3+3\lambda^2d_{rs}u^2+3\lambda d_{rs}^2u
+\lambda(x+y)+d_{rs}^3+t_r+t_s.\tag{5}$$

The mixed/unread difference terms in (5) are actual scalar terms, not carries
that can be discarded using characteristic three.

Take $F_0(x)=x-1$, $F_1(x)=x$, $F_2(x)=x+1$. On the seed diagonal, the
nine constants $D_{rs}(x)-2x$ form the matrix

$$\begin{pmatrix}-2&-2&-8\\0&0&0\\8&2&2\end{pmatrix}.$$

Thus $q=5,c=0$ and (3) is exactly

$$|P(A',A')|=9n^2-4n$$

for generic $A$. A singleton seed $A=\{0\}$ has the exact full image
$\{-8,-2,0,2,8\}$ on $A'=\{-1,0,1\}$, a finite $9\to5$ count.
Its repeated diagonal coincidences are algebraic, but for larger generic
seeds they account for only $4n$ outputs. Therefore this identity does not
produce a fixed gap below nine with a subquadratic error. This analytic
calculation did not run a finite search, and is not an experiment report.

## 6. TB-A6: finite synchronous row collapse has only linear size

**PROVED internally.** This result applies to any finite seed $A$, $|A|=n$,
and any three maps injective on $A$ with disjoint images; the maps may depend
on $A$ and need not be algebraic. Put $A'=\bigsqcup_sF_s(A)$.

For each $X\in A'$ and $y\in A$, define the three-output packet

$$\mathcal R_{X,y}=\{P(X,F_0(y)),P(X,F_1(y)),P(X,F_2(y))\}.$$

There are $3n^2$ packets partitioning the $9n^2$ ordered input pairs before
taking outputs. Their total reduction from coincidences *inside individual
packets* satisfies

$$\sum_{X\in A',\,y\in A}(3-|\mathcal R_{X,y}|)\le6n.\tag{6}$$

There are at most $n$ completely collapsed packets with
$|\mathcal R_{X,y}|=1$.

**Proof.** For any distinct real $b,c$, subtraction and completion of a square
give the exact equivalence

$$P(X,b)=P(X,c)
\iff 3\left(X-\frac{b+c}{2}\right)^2+\frac{(b-c)^2}{4}=1.\tag{7}$$

Consequently each of the three unordered pairs in the distinct triple
$F_0(y),F_1(y),F_2(y)$ can agree at at most two distinct first coordinates
$X$. For fixed $y$, there are at most six pair-equality incidences across
$A'$. In any packet its loss $3-|\mathcal R_{X,y}|$ is bounded above by
its number of unordered equal-output pairs: the possibilities are losses
$0,1,2$ with $0,1,3$ equal pairs. Sum to prove (6).

For three distinct $b_0,b_1,b_2$ to have a common output at $X$, they must be
the three roots of

$$Y^3-3XY^2+(3X^2-1)Y-X^3-X+z=0$$

for that output $z$. The two highest Vieta equations force

$$X=(b_0+b_1+b_2)/3,\qquad\sum_{s=0}^2(b_s-X)^2=2.\tag{8}$$

Conversely (8) makes $\prod_s(Y-b_s)$ have those three highest coefficients;
choosing $z$ to match its constant coefficient proves that all three outputs
agree. In particular the given triple has at most one such $X$. There is
one triple for each $y$, so at most $n$ completely collapsed packets. ∎

This closes the literal same-old-$y$ Frobenius identification as a source of
a quadratic number of savings, even with fully adaptive branch maps. It does
**not** lower-bound the final union: different packets may have additional
collisions. An argument that encodes each packet's distinct outputs separately
uses at least $9n^2-6n$ labels, but more efficient labels crossing packets are
not excluded. The restriction is on the matching scheme, not all possible
block intersections or the ultimate real-set target.

## 7. Provenance, dependencies and retained gaps

| ID | Scope and quantifiers | Status / evidence | Proof locator and dependencies |
|---|---|---|---|
| TB-A1 | All real analytic nonconstant separable maps with affine scalar-output identity on an open rectangle | PROVED internally; symbolic proof; independently audited by the lead | §1, v1 2026-09-16; elementary differentiation and polynomial comparison |
| TB-A2 | All real analytic nonconstant swapped separable block identities | PROVED internally; symbolic proof; independently audited by the lead | §2; rank argument of TB-A1 |
| TB-A3 | All nonconstant rational branches factoring through one algebraic function of old P | PROVED internally; symbolic proof; independently audited by the lead | §3; rational-function fields, elementary pole and degree arguments, TB-A1 |
| TB-A4 | Three fixed distinct real algebraic branches; every algebraically independent seed in a common analytic interval | PROVED internally; complete image count; independently audited by the lead | §4; TB-A1, TB-A2 and proved genericity fact |
| TB-A5 | Translations by -1,0,1; singleton exact count and generic-seed exact count | PROVED internally; nine explicit formulas; independently audited by the lead | §5; direct algebra and TB-A4 |
| TB-A6 | Every finite seed and three arbitrary injective maps with disjoint images; only same-old-second-index output packets | PROVED internally; exact finite bound; independently audited by the lead | §6; subtraction, quadratic root count and Vieta |

All claims have track T01, branch “characteristic-zero three-branch lift”, and
the polynomial stated at the top. No external theorem or numerical constant
from a tower paper is used. No arithmetic amplification is justified by these
obstructions. For this subtask field-degree, discriminant, regulator,
denominator, class-number and splitting costs are inapplicable because no
number-field construction is proposed, not because such costs are zero in a
future construction.

The inherited T01 regular-digital and fixed-prime positive-entropy theorems
(current-state §4.3 and §6.5–6.6) remain separate reported results. Our generic
seed theorem uses no fixed base or prime-support hypothesis and does not
re-prove those historical results. Conversely it excludes none of their
arithmetic seeds by genericity. The continuous-cover result (current-state
§4.2) is also separate: no positive-volume counting certificate is used here.
The singleton translation calculation is not evidence against any of those
theorems and does not establish a recursive carrier.

**OPEN, outside this note:** structured seed-dependent algebraic branches with
many genuinely two-variable cross-block collisions, and an all-depth support
recurrence with a fixed gap. Arbitrary algebraic input semiconjugacies with
nonlinear $\Psi$ are not classified by TB-A3. No claim of universal impossibility,
positive conjecture or arithmetic tower construction is made.
