# HN1-1 — the exact two-prime carrier and its local actions

**16 September 2026. Claim HN1-1, version 1.** Branch: T03 / the fixed
HR-N1 two-prime return-tail assertion. Polynomial:
$Q(x,y)=x^2+xy+y^2$. This note proves the input, action and valuation
facts needed to analyze that assertion. It does not decide the return tail,
assert an image saving, or change the adaptive RC15/4 obligation.

**Status: PROVED**, by the self-contained internal arguments below;
the parent agent independently inspected this written version in this task.
No external theorem, literature search or novelty claim is used.

## Authorization, source scope and budget

The current user expressly authorized a bounded, **strictly offline** HR-N1
cycle in the local attachment
`[private commissioning attachment; locator withheld]`.
The primes, carrier and multiplier window below are frozen by that request.
This independent subtask is symbolic only: **zero experiments, zero program
executions of mathematical cases, and zero network access**. It does not
spend the parent-controlled allowance for an optional finite diagnostic.

Local arguments inspected include the prior
[HR-1 return theorem](../2026-09-16-high-return/return-lemma.md),
[HR-2–HR-4 denominator proofs](../2026-09-16-high-return/denominator-obstruction.md),
and the exact HR-N1 statement in the
[previous cycle report](../2026-09-16-high-return/README.md#7-one-next-proof-obligation).
Those reports remain unchanged. The elementary split-valuation construction
at 7 below restates the relevant HR-2 proof and extends it explicitly to 19;
it does not import an unproved unique-factorization or local-field theorem.
The 7/19 input count and multipliers were stated previously; their derivations
are independently checked here. The simultaneous coefficient-recovery facts
and nine depth-order classification are derived here for this exact carrier.

No missing local source is needed for these elementary proofs. External links
in earlier sources are provenance only and were not followed.

## 1. Exact input count and rational projection

For every integer $L\ge1$, put

$$
A_L=\{b7^{-k}19^{-\ell}:1\le |b|\le L,
       \ \gcd(b,133)=1,\ 0\le k,\ell\le L\}.
\tag{1}
$$

The valuation of a nonzero rational number at a prime is the exponent of
that prime in its numerator minus its exponent in its denominator; put
$v_p(0)=+\infty$ when needed. If $x=b7^{-k}19^{-\ell}$ occurs in (1),
then

$$v_7(x)=-k,\qquad v_{19}(x)=-\ell.$$

These recover both depths, after which $b=x7^k19^\ell$ is recovered
including its sign. Thus every scalar input has exactly one parameter
label. Inclusion–exclusion for positive integers at most $L$ gives

$$
\boxed{
n_L=|A_L|=
2\left(L-\lfloor L/7\rfloor-\lfloor L/19\rfloor
                   +\lfloor L/133\rfloor\right)(L+1)^2.
}\tag{2}
$$

In particular, $n_L=(216/133)L^3+O(L^2)$ and $n_L\to\infty$.
All inputs are nonzero rational real numbers. The projection to the real
line is the identity, with fiber one, and every ordered pair is in the
same scalar square $A_L^2$.

## 2. Generators, inverses and exact norm preservation

Fix $\omega=(-1+\sqrt{-3})/2$, so $\bar\omega=\omega^2=-1-\omega$.
Let $R=\mathbb Z[\omega]\subset\mathbb C$ and $E=\mathbb Q(\omega)$.
For $z=x-\omega y$ with rational $x,y$,

$$N(z)=z\bar z=x^2+xy+y^2=Q(x,y).\tag{3}$$

The coefficient map $(x,y)\mapsto x-\omega y$ is injective because
$1,\omega$ are linearly independent over $\mathbb Q$.

Write

$$
\pi_7=3+\omega,\quad\bar\pi_7=2-\omega,
\qquad
\pi_{19}=5+2\omega,\quad\bar\pi_{19}=3-2\omega.
$$

Direct multiplication using $\omega^2=-1-\omega$ gives
$\pi_7\bar\pi_7=7$ and $\pi_{19}\bar\pi_{19}=19$. Hence

$$
u=\frac{\pi_7}{\bar\pi_7}=\frac{8+5\omega}{7},
\qquad
v=\frac{\pi_{19}}{\bar\pi_{19}}=\frac{21+16\omega}{19},
\qquad N(u)=N(v)=1.
\tag{4}
$$

For $g=a+b\omega$, multiplying $x-\omega y$ by $g$ gives

$$
T_g(x,y)=(ax+by,-bx+(a-b)y),\qquad
Q(T_g(x,y))=N(g)Q(x,y).
\tag{5}
$$

The two generators and their inverses are therefore exactly

$$
T_u=\frac17\begin{pmatrix}8&5\\-5&3\end{pmatrix},
\quad T_{u^{-1}}=\frac17\begin{pmatrix}3&-5\\5&8\end{pmatrix},
\tag{6}
$$

$$
T_v=\frac1{19}\begin{pmatrix}21&16\\-16&5\end{pmatrix},
\quad T_{v^{-1}}=\frac1{19}\begin{pmatrix}5&-16\\16&21\end{pmatrix}.
\tag{7}
$$

For example, the two numerator determinants are $49$ and $361$;
their inverse products are the corresponding scalar identity matrices.
The norm numerators are
$8^2-8\cdot5+5^2=49$ and
$21^2-21\cdot16+16^2=361$. Multiplication in $E$ proves
$T_gT_h=T_{gh}$, so all these actions commute and all $u^rv^s$ preserve
the same fixed $Q$. Their rational coordinate denominators divide
$7^{|r|}19^{|s|}$; no other denominator prime is introduced.

## 3. Elementary split valuations at both primes

For integers $a,b$, explicit division in $E$ gives

$$
\frac{a+b\omega}{\pi_7}
 =\frac{(2a+b)+(-a+3b)\omega}{7},\qquad
\frac{a+b\omega}{\bar\pi_7}
 =\frac{(3a-b)+(a+2b)\omega}{7},
\tag{8}
$$

$$
\frac{a+b\omega}{\pi_{19}}
 =\frac{(3a+2b)+(-2a+5b)\omega}{19},\qquad
\frac{a+b\omega}{\bar\pi_{19}}
 =\frac{(5a-2b)+(2a+3b)\omega}{19}.
\tag{9}
$$

Thus the kernels of the following evaluations are exactly the displayed
principal ideals:

| Prime | Factor | Evaluation of $\omega$ | Divisibility condition on $a+b\omega$ |
|---|---|---:|---|
| 7 | $\pi_7$ | $4$ | $a+4b\equiv0\pmod7$ |
| 7 | $\bar\pi_7$ | $2$ | $a+2b\equiv0\pmod7$ |
| 19 | $\pi_{19}$ | $7$ | $a+7b\equiv0\pmod{19}$ |
| 19 | $\bar\pi_{19}$ | $11$ | $a+11b\equiv0\pmod{19}$ |

Indeed, every residue in the table satisfies $t^2+t+1=0$ modulo the
indicated prime, so evaluation defines a surjective ring map $R\to\mathbb F_p$.
Equations (8)–(9) show that its kernel is precisely the corresponding
factor times $R$. Those ideals are prime because their quotient rings are
fields. The two factors above any one rational prime do not divide each
other: evaluation of the other factor in the appropriate quotient is
nonzero.

For a nonzero $w\in R$, define $v_{\pi_p}(w)$ as the maximum power of
$\pi_p$ dividing $w$, and define $v_{\bar\pi_p}$ similarly. These maxima
are finite: $N(a+b\omega)=a^2-ab+b^2$ is a positive integer for
$a+b\omega\ne0$, and division by a factor above $p$ divides that norm
by $p$. Factoring out maximal powers and using the nonzero product of
residues proves additivity on products. This extends both valuations
consistently to $E^\times$ by subtracting denominator valuations.

Factoring out a smaller power in a sum proves the valuation inequality,
with equality when the summands have unequal valuations: after reduction
there is then one nonzero summand and one zero summand. Clearing a common
denominator extends that fact from $R$ to $E$. These arguments require no
unique factorization of arbitrary elements or ideals.

On nonzero rational numbers the two valuations restrict to the ordinary
one:

$$
v_{\pi_p}(q)=v_{\bar\pi_p}(q)=v_p(q)\qquad(q\in\mathbb Q^\times).
\tag{10}
$$

For integers this follows from $p=\pi_p\bar\pi_p$, nondivisibility of
opposite factors, and the nonzero residue of an integer prime to $p$.
Fractions follow by additivity. Conjugation exchanges the two factors,
and therefore

$$
v_{\pi_p}(\bar z)=v_{\bar\pi_p}(z),\qquad
v_p(N(z))=v_{\pi_p}(z)+v_{\bar\pi_p}(z).
\tag{11}
$$

All factors above 19 are units for the valuations above 7, and conversely.
For example, their norms are 19 and 7 respectively, so divisibility by a
factor above the other prime would contradict divisibility of their integer
norms. Using (4) gives the complete displacement table:

| Element | $v_{\pi_7}$ | $v_{\bar\pi_7}$ | $v_{\pi_{19}}$ | $v_{\bar\pi_{19}}$ |
|---|---:|---:|---:|---:|
| $u$ | $1$ | $-1$ | $0$ | $0$ |
| $v$ | $0$ | $0$ | $1$ | $-1$ |
| $u^rv^s$ | $r$ | $-r$ | $s$ | $-s$ |

Consequently the labels $(r,s)$ are injective: if $u^rv^s=u^{r'}v^{s'}$,
the valuations above 7 force $r=r'$, and those above 19 force $s=s'$.
For the exact user-specified window,

$$G_L=\{u^rv^s:|r|,|s|\le8L\},\qquad
\boxed{|G_L|=(16L+1)^2.}\tag{12}
$$

Neither generator has finite order. Multiplication by distinct elements
of $G_L$ sends any nonzero $z$ to distinct elements, by cancellation in
the field. Thus all nonzero action stabilizers are trivial and repeated
return labels have multiplicity one. The carrier has no zero input, so
there is no zero pair in $A_L^2$. This identifies action-return counts
with counts of distinct returned scalar pairs; it does not identify them
with the **entire** scalar $Q$-fiber.

## 4. Coefficient recovery: split minima and coordinate depths

Fix $p\in\{7,19\}$, a nonzero $z=x-\omega y$ with $x,y\in\mathbb Q$,
and write

$$\alpha_p=v_{\pi_p}(z),\qquad\beta_p=v_{\bar\pi_p}(z).$$

The elements $\omega$, $\bar\omega$ and
$\omega-\bar\omega=1+2\omega$ are units for both valuations above $p$.
This follows directly by evaluating at the four nonzero residues in the
table; $1+2\omega$ evaluates to $2,5$ modulo 7 and $15,4$ modulo 19.

The coefficient-recovery identities are

$$
y=\frac{\bar z-z}{\omega-\bar\omega},\qquad
x=\frac{\omega\bar z-\bar\omega z}{\omega-\bar\omega}.
\tag{13}
$$

They imply the exact minimum rule

$$
\boxed{\min\{v_p(x),v_p(y)\}=\min\{\alpha_p,\beta_p\}.}\tag{14}
$$

**Proof.** The original formulas for $z$ and $\bar z$ give
$\alpha_p,\beta_p\ge\min\{v_p(x),v_p(y)\}$. Conversely, (13), the
unit denominators and the valuation inequality give both coordinate
valuations at least $\min\{\alpha_p,\beta_p\}$. These two inequalities
prove equality of the minima. $\square$

If $\alpha_p\ne\beta_p$, the two numerator terms in **each** expression
in (13) have unequal valuations. Therefore there is no cancellation at
their minimum, and the stronger assertion holds:

$$
\boxed{v_p(x)=v_p(y)=\min\{\alpha_p,\beta_p\}\quad
       \text{if }\alpha_p\ne\beta_p.}\tag{15}
$$

If instead $v_p(x)\ne v_p(y)$, the original expressions for $z$ and
$\bar z$ have unequal summand valuations, proving

$$\alpha_p=\beta_p=\min\{v_p(x),v_p(y)\}.\tag{16}$$

When $\alpha_p=\beta_p$, (14) is the appropriate conclusion: both
coordinate valuations are at least this value, and at least one equals it.
One cannot conclude that both equal it. Similarly, equal coordinate depths
need not imply a nonzero split-valuation difference.

## 5. The nine depth-order types

Write the two inputs uniquely as

$$x=b7^{-k}19^{-\ell},\qquad y=c7^{-h}19^{-j},\qquad
\gcd(bc,133)=1,\quad 1\le|b|,|c|\le L.$$

Use $U_p(t)=(-t,-t)$ to denote balanced split valuations.
Use $E_p(t,D)$ to mean either ordered pair
$(-t,-t+D)$ or $(-t+D,-t)$, where $D\ge0$; the actual residue determines
which ordering occurs, and $D=0$ gives a balanced pair.

When $k=h$, set $J=\max\{\ell,j\}$ and

$$B_7=b19^{J-\ell},\quad C_7=c19^{J-j},\quad
D_7=v_7(Q(B_7,C_7)).$$

Both $B_7,C_7$ are 7-free. Equations (11) and (14) show that the
split valuations at 7 are $E_7(k,D_7)$. The cleared norm has

$$0<Q(B_7,C_7)\le3L^2 19^{2|\ell-j|},$$

so

$$D_7\le\left\lfloor\log_7(3L^2 19^{2|\ell-j|})\right\rfloor.\tag{17}$$

When $\ell=j$, set $K=\max\{k,h\}$ and similarly

$$B_{19}=b7^{K-k},\quad C_{19}=c7^{K-h},\quad
D_{19}=v_{19}(Q(B_{19},C_{19})),$$

giving split valuations $E_{19}(\ell,D_{19})$ and

$$D_{19}\le\left\lfloor\log_{19}(3L^2 7^{2|k-h|})\right\rfloor.\tag{18}$$

In the following table each entry lists the valuations at 7 and at 19,
in that order. All nine cases are included and are disjoint.

| 7-depth ordering | $\ell<j$ | $\ell=j$ | $\ell>j$ |
|---|---|---|---|
| $k<h$ | $U_7(h),\ U_{19}(j)$; $y$ deeper at both primes | $U_7(h),\ E_{19}(\ell,D_{19})$ | $U_7(h),\ U_{19}(\ell)$; maxima on different coordinates |
| $k=h$ | $E_7(k,D_7),\ U_{19}(j)$ | $E_7(k,D_7),\ E_{19}(\ell,D_{19})$ | $E_7(k,D_7),\ U_{19}(\ell)$ |
| $k>h$ | $U_7(k),\ U_{19}(j)$; maxima on different coordinates | $U_7(k),\ E_{19}(\ell,D_{19})$ | $U_7(k),\ U_{19}(\ell)$; $x$ deeper at both primes |

In the center cell, $D_7=v_7(Q(b,c))$ and
$D_{19}=v_{19}(Q(b,c))$. Thus there is the joint bound

$$7^{D_7}19^{D_{19}}\mid Q(b,c),\qquad
  7^{D_7}19^{D_{19}}\le3L^2.\tag{19}$$

The separate logarithmic bounds in that cell are genuine, but they are
not independent probabilities or independent savings.

## 6. Exact state transitions and simultaneous legality

Multiplying by $u^rv^s$ changes the split valuations exactly to

$$
(\alpha_7+r,\beta_7-r;\ \alpha_{19}+s,\beta_{19}-s).
\tag{20}
$$

By (14), any legal returned pair has maximum denominator depths

$$
K'=-\min\{\alpha_7+r,\beta_7-r\},\qquad
J'=-\min\{\alpha_{19}+s,\beta_{19}-s\},
\tag{21}
$$

both in $\{0,\ldots,L\}$. If the two split valuations at a prime are
unequal, (15) forces **both** returned coordinates to have that same
denominator depth. If they are equal, only the maximum depth is fixed;
the two coordinates can have different depths.

For example, when the input 7-depths are unequal, let $K=\max\{k,h\}$.
Then the input valuations at 7 are $(-K,-K)$, and every legal return
satisfies

$$K'=K+|r|.$$

For $r\ne0$ both returned 7-depths equal $K+|r|$; in particular
$|r|\le L-K$. The corresponding statement at 19 is
$J'=J+|s|$, with both returned depths equal when $s\ne0$, whenever the
input 19-depths are unequal. More generally, a returned pair with unequal
7-depths can occur only when $\alpha_7+r=\beta_7-r$; this determines
at most one integer $r$. The analogous assertion determines at most one
$s$ for unequal returned 19-depths. These are necessary transition
constraints, not complete legality certificates.

For completeness, after evaluating the rational matrix action let its two
coordinates be $x',y'$. Every denominator divides a product of powers of
7 and 19. The exact membership test is therefore:

1. Both $x',y'$ are nonzero.
2. Their four rational valuations at 7 and 19 belong to
   $\{-L,-L+1,\ldots,0\}$, defining the four returned depths.
3. Remove those exact denominator powers from each coordinate. The resulting
   integers $b',c'$ must satisfy $1\le|b'|,|c'|\le L$.

The recovered integers are automatically prime to 133 by the exact
valuation choices. These conditions are necessary and sufficient for
$T_{u^rv^s}(x,y)\in A_L^2$. Conditions at the two primes alone do not
establish the two numerator bounds. Nor may two separate marginal return
fractions be multiplied without a joint argument.

## 7. What survives from the one-prime arguments

- **Survives exactly:** unequal coordinate depths at one prime force balanced
  split valuations there; the output valuation is
  $v_7(Q(x,y))=-2\max\{k,h\}$ or
  $v_{19}(Q(x,y))=-2\max\{\ell,j\}$, respectively. Thus an output
  recovers the deepest depth at every prime where that pair has unequal
  depths. The recovered maxima can belong to different coordinates.
- **Survives exactly:** scalar coefficient recovery, nonzero freeness,
  numerator coprimality, and the valuation displacements (20). These are
  simultaneous identities, not averaged or sampled statements.
- **Survives in the center cell:** when both pairs of depths tie, the
  split-valuation differences satisfy the logarithmic and joint bounds
  from $Q(b,c)\le3L^2$.
- **Fails as a direct uniform transfer:** if only the 7-depths tie, its
  numerator norm is $Q(B_7,C_7)$, with possible height
  $3L^2 19^{2|\ell-j|}$, not $3L^2$. The analogous contamination at 19
  is $7^{2|k-h|}$. Thus HR-2's bound on every split imbalance by
  $O(\log L)$ has not been established for the entire two-prime square.
  The explicit upper bounds (17)–(18) can instead grow linearly in $L$.
- **Fails as an immediate application of HR-3/HR-4:** a one-prime rewriting
  uses a numerator alphabet containing powers of the other prime. It is
  neither the fixed alphabet of HR-3 nor a dense alphabet whose height is
  polynomially comparable with $n_L$ as required to use HR-4 for a
  subpower bound in $n_L$. The HR-4 fiber bound itself remains true for
  its stated family; this observation concerns its attempted transfer.

These failures of a direct import are not evidence that HR-N1 holds.
This classification supplies exact necessary constraints for the separate
analytic screen; it does not assert that a positive-density class has
small returns or that any class has a favorable asymptotic return rate.

## 8. Exact ledger and evidence limit

| Quantity | Certified fact |
|---|---|
| Input count, lower and upper | Exact formula (2); $n_L\asymp L^3$ with fixed constants |
| Input parameter/projection fibers | One; rational valuations recover both depths and the signed numerator |
| Same-set full coverage | The domain is all of $A_L^2$, classified by all nine depth-order cells |
| Multiplier count and fibers | Exact formula (12); distinct labels and distinct returned points at every nonzero pair |
| Field degree | Inputs are rational, degree one; actions use the fixed quadratic field $E$ |
| Denominators | Input common denominator divides $7^L19^L$; multiplier coefficients have denominators dividing $7^{|r|}19^{|s|}$ |
| Heights | $|x|\le L$ and $Q(x,y)\le3L^2$ for scalar inputs, but local numerator normalizations incur the explicit other-prime powers in (17)–(18) |
| Local splitting | Derived by the explicit quotient maps (8)–(9); no unproved UFD, ideal class, regulator, or extension theorem is used |
| Zero/singular exception | No zero input or zero pair lies in $A_L^2$; a transformed coordinate zero is simply not a legal return |
| Full scalar fibers | Every return lies in the correct $Q$-fiber. No equality between that fiber and the chosen multiplier orbit is claimed |
| Return-tail rate and exponent | Not established in this local-action note; HR-1 needs a separate uniform full-pair tail bound |
| Computations and network | None; only local file reads and new documentation writing |

All previous reports remain unchanged. These results verify HN1-1's
elementary premises and state space; they do not themselves settle the
frozen existential HR-N1 assertion or the general T03 target.
