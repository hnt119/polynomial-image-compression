# Correlated divisibility domains on a CRT cube-root carrier

21 September 2026 · T03 / correlated DC-O1 · fixed
$Q(x,y)=x^2+xy+y^2$ on real inputs. **PROVED** below by a complete local
argument; independent audit provenance is recorded in verification.md.
No external theorem, network access, or novelty assertion.

## 1. Exact construction and provenance

Let $\omega=(-1+i\sqrt3)/2$, $\mathcal O=\mathbb Z[\omega]$, and
$N(a+b\omega)=a^2-ab+b^2$. The Euclidean algorithm and unique
factorization in this ring are already proved in
[HR-4A](../2026-09-16-high-return/denominator-obstruction.md), not imported
from a new outside source. The old integer-height fiber bound is not
rerun as a research candidate here.

Choose, in increasing order, the rational primes $p_i\equiv1\pmod3$.
For each choose an Eisenstein integer $\alpha_i$ of norm $p_i$, by the
following deterministic convention: among positive integers $a,b$ with
$a^2+ab+b^2=p_i$, choose the lexicographically first pair with $a\ge b$,
and set $\alpha_i=a-b\omega$. Its conjugate is nonassociated to it.
Existence and an unlimited supply of these choices are justified below.
Put

$$P_d=\prod_{i=1}^d p_i,\qquad S_i=\{t\in\mathbb F_{p_i}:t^3=1\},$$
$$A_d=X_d=Y_d=\{x\in\mathbb Z:-(P_d-1)/2\le x\le(P_d-1)/2,
\quad x\bmod p_i\in S_i\ (1\le i\le d)\},$$
$$u_i=\overline{\alpha_i}/\alpha_i,\qquad
U_d=\{\prod_{i=1}^d u_i^{e_i}:e_i\in\{-1,0,1\}\}.$$

Each $S_i$ has three distinct elements. The Chinese remainder theorem
therefore gives exactly

$$n_d=|A_d|=3^d,\qquad |X_d\triangle Y_d|=0,\qquad |U_d|=3^d.\tag{1}$$

The last count follows from the valuations at the two distinct prime
factors $\alpha_i,\bar\alpha_i$; an equality of two action words forces
all their exponent differences to vanish. Every action has norm one.
For $u=A+B\omega$ the exact coefficient action is

$$M_u(x,y)=(Ax+By,-Bx+(A-B)y).\tag{2}$$

A return means that both coordinates of (2) belong to $A_d$. The domain
is precisely $D_u=A_d^2\cap M_u^{-1}(A_d^2)$, with no replacement by a
selected non-Cartesian set. Let $R_d(x,y)$ count distinct returned pairs.
There is no zero coordinate in $A_d$, so every source is nonzero and
actual action labels and distinct targets agree.

### Why the prime choices exist (elementary details)

For $p\equiv1\pmod3$, the group $\mathbb F_p^\times$ contains an element
of order three. One can see this without a primitive-root theorem:
cyclic permutation acts on triples $(a,b,c)$ of nonzero elements with
$abc=1$. There are $(p-1)^2$ triples, divisible by three, so their fixed
triples $(a,a,a)$ number a multiple of three. The identity is one fixed
triple; hence there is a nonidentity cube root. The degree-three
polynomial bounds the number of roots by three. Its two nonidentity
roots $\lambda,\lambda^2$ are distinct.

The quotient $\mathcal O/(p)\cong\mathbb F_p[T]/(T^2+T+1)$ has two
nonzero linear factors whose product is zero. Thus $p$ is not prime in
the Euclidean domain $\mathcal O$, hence is reducible. The norm and
unique factorization argument of HR-4A then gives a factor of norm $p$.
The two factors are nonassociated: the quotient just displayed is a
product of two fields by its distinct linear factors, and has no
nonzero nilpotents, whereas a repeated prime factor would give one.
Multiplication by a unit and conjugation place a norm-$p$ element in
the sector with coordinates $a-b\omega$, $a\ge b\ge0$. A zero coordinate
would make $p$ a square, so $a,b>0$. This also proves termination of the
specified finite search for $a,b$.

There are infinitely many such rational primes by the following direct
argument. Given finitely many of them with product $P$, put $t=3P$ and
choose any prime divisor $q$ of $t^2+t+1>1$. It is neither three nor a
divisor of $P$. The residue $t$ has order exactly three modulo $q$:
$t^3=1$ and $t\ne1$, since otherwise $q=3$. Its order divides $q-1$
by partition into cosets of its order-three subgroup. Hence
$q\equiv1\pmod3$, providing a new prime. No prime-density bound is used.

## 2. CD-1 — global conjugation preserves all scalar cross terms

### Statement

For a word $e$ write

$$\beta_e=\prod_{e_i=1}\alpha_i\prod_{e_i=-1}\bar\alpha_i,
\qquad D_e=N(\beta_e)=\prod_{e_i\ne0}p_i.$$

Then $u_e=\bar\beta_e/\beta_e$. For $z=x-\omega y$, integrality of
$u_ez$ is equivalent to $\beta_e\mid z$ in $\mathcal O$. If
$z=\beta_e w$, its candidate return is the single global expression

$$z'=\bar\beta_e w,\qquad N(z')=N(\beta_e)N(w)=N(z).\tag{3}$$

This is only the integrality test. A genuine return additionally requires
the height and every CRT coordinate restriction in the definition of $A_d$.

### Meaning

The divisibility condition depends on the whole scalar pair. It permits
conjugating a selected global factor of $z$, preserving every cross term.
It does not independently rotate summands of $x$ and $y$.

### Consequence

The composition identity passes the required scalar gate. It supplies no
return-tail bound until all target coordinates are checked.

### Proof and cross-term expansion

The ideals generated by $\beta_e$ and $\bar\beta_e$ are coprime, since
at most one factor over each $p_i$ occurs in $\beta_e$. Unique
factorization proves the integrality equivalence. For completely
explicit scalar algebra, if $\beta=a+b\omega$ and $w=c+f\omega$, then

$$\beta w=(ac-bf)+(af+bc-bf)\omega,$$
$$N(\beta w)
=a^2c^2-a^2cf+a^2f^2-abc^2+abcf-abf^2
+b^2c^2-b^2cf+b^2f^2$$
$$=(a^2-ab+b^2)(c^2-cf+f^2).\tag{4}$$

Replacing $(a,b)$ by $(a-b,-b)$ leaves the first factor unchanged.
Equation (4) includes the mixed terms of the composed scalar pair.
Iteration is allowed only through this entire product identity; no
product of independently certified additive returns is claimed.

## 3. CD-2 — simultaneous diagonal residues force identity

### Statement

For $p=(x,y)\in A_d^2$, set

$$J(p)=\{i:x\equiv y\pmod{p_i}\},\qquad
W(p)=\prod_{i\in J(p)}p_i.$$

If

$$\boxed{W(p)^3>\frac43P_d,}\tag{5}$$

then $R_d(p)=1$: only $u=1$ returns under the entire specified $U_d$.
This theorem concerns the width-one exponent box, not arbitrary integer
powers of the generators.

### Meaning

At primes where the two scalar coordinates agree, a returned pair must
agree with the original pair modulo that prime. The resulting congruences
on one global factor overpower its permitted norm.

### Consequence

A substantial diagonal-residue population can obstruct the desired tail,
even though the source often has many other primes available for factor
conjugation. This is an actual-return obstruction for this $U_d$.

### Proof

Suppose $u_e$ returns $(x,y)$ to $(x',y')$. At any $p_i$, two cube roots
of one either coincide or have ratio a nonidentity cube root. Hence

$$Q(x,y)\equiv
\begin{cases}3x^2\ne0,&x=y,\\0,&x\ne y\end{cases}\pmod{p_i}.\tag{6}$$

For $i\in J$, equality of the norms implies $x'=y'$ modulo $p_i$.
It also implies $(x')^2=x^2$. Squaring is injective on the three cube
roots, so $(x',y')=(x,y)$ modulo $p_i$.

Moreover $p_i\nmid N(z)$ there. By CD-1, $e_i\ne0$ would force a
factor of norm $p_i$ to divide $z$, a contradiction. Thus $e_i=0$ on
$J$ and

$$D_e\le P_d/W.\tag{7}$$

Both $\beta_e$ and $z$ are invertible modulo $p_i$ for $i\in J$.
The equality $u_ez=z$ in $\mathcal O/(p_i)$ therefore gives
$\bar\beta_e=\beta_e$ modulo $p_i$. Write $\beta_e=a+b\omega$.
Since $\bar\beta_e-\beta_e=-b-2b\omega$, comparison in the basis
$1,\omega$ gives $p_i\mid b$ and hence

$$W\mid b,\qquad
\frac34b^2\le N(\beta_e)=D_e\le P_d/W.\tag{8}$$

Under (5), these inequalities imply $|b|<W$, so $b=0$ and $u_e=1$.
The distinct-action argument after (1) then forces $e=(0,\ldots,0)$.
Conversely the identity always returns. No boundary or height estimate
was needed to exclude the other actions. $\square$

## 4. CD-3 — a uniform positive fraction of identity-only pairs

### Statement

For every $d\ge1$, at least

$$\boxed{\frac{n_d^2}{48}}\tag{9}$$

ordered pairs satisfy (5), and therefore have $R_d=1$. In particular,
for every fixed $\varepsilon>0$,

$$B_\varepsilon(d)=|\{p\in A_d^2:R_d(p)<n_d^\varepsilon\}|
\ge n_d^2/48.\tag{10}$$

For all fixed $\varepsilon,\delta>0$ and $C'<\infty$, (10) eventually
contradicts $B_\varepsilon\le C'n_d^{2-\delta}$, since $3^{d\delta}>48C'$.

### Meaning

This counts actual Cartesian ordered pairs, not action words or a selected
multiplicative orbit. The bad fraction is bounded below independently
of the depth and of the sizes of the chosen distinct split primes.

### Consequence

The specified CRT cube-root carrier and width-one factor actions fail
DC-O1. They have perfect coordinate overlap and exponentially many
actual actions, but no positive exceptional-tail exponent.

### Proof

Under the uniform distribution on all $n_d^2=9^d$ pairs, the CRT
coordinates are independent and uniform in $S_i^2$. Thus
$I_i=1_{\{x=y\bmod p_i\}}$ are independent Bernoulli variables of
parameter $1/3$. With $w_i=\log p_i$, put

$$T=\sum_i w_i(I_i-1/3),\qquad
\sigma^2=\mathbb E T^2=\frac29\sum_i w_i^2.$$

The single-coordinate fourth centered moment is $2/27$, and independence
and zero means give exactly

$$\mathbb E T^4=3\sigma^4-\frac{2}{27}\sum_i w_i^4\le3\sigma^4.\tag{11}$$

Hölder applied to $|T|^{2/3}|T|^{4/3}$ gives
$\sigma^2\le(\mathbb E|T|)^{2/3}(\mathbb E T^4)^{1/3}$, whence
$\mathbb E|T|\ge\sigma/\sqrt3$. For $T_+=\max(T,0)$, zero mean implies

$$\mu=\mathbb E T_+\ge\frac{\sigma}{2\sqrt3},\qquad
\mathbb E T_+^2\le\sigma^2.$$

Let $F=\{T_+\ge\mu/2\}$. Splitting the expectation over $F$ and its
complement and then using Cauchy–Schwarz gives

$$\mu/2\le\mathbb E(T_+1_F)\le\sigma\sqrt{\Pr(F)},
\qquad\Pr(F)\ge\frac1{48}.\tag{12}$$

On $F$, $T\ge\sigma/(4\sqrt3)$. Since $p_i\ge7$ and $d\ge1$,

$$\frac{\sigma}{4\sqrt3}\ge\frac{\log7}{6\sqrt6}
>\frac{\log(4/3)}3.\tag{13}$$

For an elementary strict check in (13), $\log(4/3)<1/3$ and
$\log7>\log6=2\log2+\log(3/2)\ge4/3+2/5=26/15>5/3>2\sqrt6/3$;
the lower logarithm bounds follow by integrating, or differentiating,
$\log t\ge2(t-1)/(t+1)$ for $t\ge1$.

Finally $\log W=(\log P_d)/3+T$. Thus (13) implies
$3\log W>\log P_d+\log(4/3)$, exactly (5). Multiplying (12) by
$9^d$ proves (9). The lower bound need not be an integer; the actual
cardinality is at least its ceiling. $\square$

## 5. Exact domain audit and rate ledger

The finite program uses the first four primes $7,13,19,31$, with
$\alpha=2-\omega,3-\omega,3-2\omega,5-\omega$. These are fixed
in advance; depths 1–4 form one mechanism, not four constructions.
It tests all actions and all pairs using two independent exact formulas.
It also verifies (5) pointwise and the factor-divisibility integrality
criterion before testing CRT membership and the scalar height bound.

For any nonzero $z$, unique factorization shows that a factor word can
be integral only if each selected prime factor divides the whole $z$.
At each off-diagonal prime exactly one of the two conjugate factors is
eligible. At each diagonal prime neither is eligible. Thus if
$k=d-|J|$, exactly $2^k$ selected actions give integral candidate targets.
These are not $2^k$ returns to $A_d^2$. CD-2 identifies a positive-density
population on which only one of those integral candidates returns.

| Gain/cost | Exact bound or status | Reason |
|---|---|---|
| Input count before/after CRT restriction | $P_d$ centered integers reduce to $n_d=3^d$ per coordinate | CRT; both inputs pay thinning, so density is $(3^d/P_d)^2$ |
| Input rates | $a=B=\log3$ per depth | Exact count, no asymptotic error |
| Coordinate overlap | zero symmetric difference; choose $\eta=1$ | Same scalar set |
| Action labels and projection fibers | $3^d$ distinct actions; scalar/pair CRT parameter fibers one | Unique factorization; CRT representatives |
| Potential integral factor switches | $2^{d-\lvert J\rvert}$ per pair | Exact divisibility, insufficient for return |
| Effective uniform tail | $B_\varepsilon\ge n_d^2/48$ for every fixed $\varepsilon>0$ | CD-3; no positive $\delta$ |
| Stabilizers / duplicate actions | one at every source | All sources nonzero; multiplication faithful |
| Field / discriminant | $\mathbb Q(\omega)$, degree two, discriminant $-3$ | Fixed throughout |
| Regulator, class number, prime density | no estimates used | Explicit elements and elementary factorization/infinitude suffice |
| Denominators and local moduli | action coefficients have denominator dividing $D_e\mid P_d$ | $u_e=\bar\beta_e^2/D_e$ |
| Heights / archimedean bounds | $\lvert x\rvert\le(P_d-1)/2$; $N\beta_e\le P_d$; each action has complex modulus one | Exact, no uncharged height assumption |
| State / branch costs | one scalar CRT state per residue word; $3^d$ actions counted once | No formal word multiplicity gain |
| Carries / boundary | returns tested in centered interval as well as all residues | No modular return silently lifted |
| Exceptional outputs | at most one output per bad pair; proved bad count has full two-input exponent | The prescribed certificate cannot absorb the exceptions |
| Final support exponent / signed gap | DC-R1 certifies no fixed $c>0$ | A positive return threshold requires $\delta=0$ or worse for this action family |
| Actual image rate | OPEN in this cycle | Other norm-preserving multipliers and other collisions are not excluded |

In particular $\log P_d$ is retained explicitly; no polynomial-height
assumption in $n_d$ is made. Even a very favorable count for the complement
of (9) cannot remove the fixed bad fraction. This obstruction applies to
any chosen distinct split primes and the same width-one box, but does not
cover larger exponent windows, other scalar residue sets, or all possible
norm-preserving actions. No extension of that scope is adopted here.
