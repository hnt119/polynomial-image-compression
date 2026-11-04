# HR-N1 Return Obstruction — Final Proof Report and Research Handoff

**Final freeze: 16 September 2026, version 1.** Track T03; fixed polynomial
$Q(x,y)=x^2+xy+y^2$; separate two-prime multiplier branch.

**Scope:** consolidation and audit of completed proofs, with no new proof
search, repair, replacement conjecture, experiment, or literature search.
All work is offline. The original proof files and historical records are
preserved. No novelty or external peer review is claimed.

### Controlling sources and claim identities

| Record | Authority and use in this report |
|---|---|
| [Completed HR-N1 report](../2026-09-16-hr-n1-offline/README.md), §§1–6 | HN1-2 dominant-gap obstruction and HN1-3 positive-density theorem; complete proofs inspected |
| [Local-action proof](../2026-09-16-hr-n1-offline/local-action.md), §§1–7 | HN1-1: input count, generators, valuations, scalar recovery, all nine depth-order types |
| [Independent audit](../2026-09-16-hr-n1-offline/independent-audit.md), §§1–5 | Written internal review of the obstruction and its scope |
| [Completed verification record](../2026-09-16-hr-n1-offline/verification.md), §§2–4 | Second internal review record, corrections, zero research computation, prior checks |
| [HR-1 return-to-image theorem](../2026-09-16-high-return/return-lemma.md), §§1–4 | Proved support implication, including stabilizer/projection and exceptional-output accounting |
| `local-only/migration/sources/T03_CURRENT_STATE.md`, §§2–4, 7, 13–14 | Surrounding target, actual adaptive family, RC15/4, ARG/TCRC status and existing next obligation |
| T03 archive member `output/TCRC_Root_Algebra_Pair_Maps.md`, §6 | Recorded conditional root-image recurrence, read locally; no certificate program executed |

The last companion is inside
`local-only/migration/research_supplement/T03/T03_RESEARCH_RECORD_20260910.zip`.
Its member list was inspected before reading. These private source locators
do not promise inclusion in a plain Git clone. The local proof of HR-N1 below
has no missing dependency. Historical MC-03 checkpoint designation and the
standalone F25 certificate gap are unrelated to this theorem and unchanged.

This report freezes claims **HN1-1–HN1-3**, all dated 16 September 2026,
without strengthening their conclusions. Its handoff identity is
**HR-N1-FINAL-1**; registry identity **T03-HRN1-F1** is retained.
Source and final-file hashes are recorded in [manifest.json](manifest.json).

## A. Executive summary

**PROVED:**

$$\boxed{\text{HR-N1 is false.}}$$

For every integer $m\ge2$, let $L=10m$ and use the exact rational carrier
$A_L$ and generators $u,v$ defined in §B. At least $|A_L|^2/200$ **ordered**
pairs in $A_L^2$ have exactly one return under the full action
$\{u^rv^s:(r,s)\in\mathbb Z^2\}$: the identity, with $(r,s)=(0,0)$.
The proof first imposes simultaneous denominator restrictions, then uses
norm bounds to exclude every nonzero $19$-exponent, and finally uses a
congruence modulo a power of $19$ to exclude every nonzero $7$-exponent.

Write $n_L=|A_L|$. For arbitrary fixed $\varepsilon,\delta>0$, these pairs
have return count $1<n_L^\varepsilon$ once $n_L>1$, while their number is at
least $n_L^2/200>n_L^{2-\delta}$ once $n_L^\delta>200$.
Since $n_{10m}\to\infty$, this contradicts HR-N1 along an unbounded
subsequence and therefore contradicts its requirement for every sufficiently
large $L$. The conclusion concerns this action's return distribution. It
does not bound the number of distinct polynomial values from below.

$$\boxed{\text{HR-N1 closed; quadratic-image target OPEN; RC15/4 OPEN.}}$$

## B. Mathematical setting and definitions

### B.1 Carrier, input count and fields

For every integer $L\ge1$, define

$$D_L=\{b\in\mathbb Z:1\le |b|\le L,\ \gcd(b,133)=1\},$$
$$A_L=\{b7^{-k}19^{-\ell}:b\in D_L,\quad 0\le k,\ell\le L\}.
\tag{B1}$$

All depth parameters are integers. Both coordinates use this same scalar
set; the domain is the entire ordered square $A_L^2$.
For a nonzero rational number, $v_p$ denotes the exponent of $p$ in its
numerator minus that in its denominator. Thus an input in (B1) satisfies
$v_7(x)=-k$, $v_{19}(x)=-\ell$. These recover $k,\ell$, and then $b$,
including its sign. The parameterization is injective. Inclusion–exclusion
therefore gives, exactly,

$$d_L:=|D_L|=2\left(L-\lfloor L/7\rfloor-\lfloor L/19\rfloor
                              +\lfloor L/133\rfloor\right),$$
$$n_L:=|A_L|=d_L(L+1)^2
             =\frac{216}{133}L^3+O(L^2).
\tag{B2}$$

The error has an absolute constant, coming only from four floor functions;
the proof can use the exact count throughout. In particular $n_L\to\infty$.
Every input is nonzero and rational in its usual real embedding.

Fix $\omega=(-1+\sqrt{-3})/2$ in $\mathbb C$, put
$E=\mathbb Q(\omega)$ and $\mathcal O=\mathbb Z[\omega]$, and write
$\bar\omega=-1-\omega$. The norm is

$$N_{E/\mathbb Q}(z)=z\bar z,\qquad
N(x-\omega y)=x^2+xy+y^2=Q(x,y).
\tag{B3}$$

The notation $\mathcal O$ here simply denotes the displayed ring; the proof
does not require a theorem identifying the full ring of integers.

### B.2 Action and legal returns

Fix the elements and the original finite window

$$u=\frac{8+5\omega}{7},\qquad
v=\frac{21+16\omega}{19},\qquad
G_L=\{u^rv^s:(r,s)\in\mathbb Z^2,\ |r|,|s|\le8L\}.
\tag{B4}$$

For $g=\alpha+\beta\omega\in E$, define

$$T_g(x,y)=(\alpha x+\beta y,-\beta x+(\alpha-\beta)y).
\tag{B5}$$

The defining identity is

$$x'-\omega y'=g(x-\omega y),\qquad (x',y')=T_g(x,y).$$

Thus $T_gT_h=T_{gh}$, and norm-one $g$ preserve $Q$. A **return** means
exactly $T_g(x,y)\in A_L^2$: both returned rational coordinates must
individually belong to the same set (B1). Returning to an ideal, coefficient
container, or selected pair set is insufficient.

Define

$$R_L(x,y)=\#\{g\in G_L:T_g(x,y)\in A_L^2\},$$
$$R_L^\infty(x,y)=\#\{u^rv^s:(r,s)\in\mathbb Z^2,
                                      \ T_{u^rv^s}(x,y)\in A_L^2\}.
\tag{B6}$$

Section E.1 proves distinct exponent labels give distinct multipliers and
distinct returned pairs. Consequently even $R_L^\infty$ is finite, at most
$n_L^2$. The identity multiplier $1=u^0v^0$ returns every pair to itself.
It is the unique identity exponent label.

### B.3 Exact HR-N1 assertion

For a fixed $\varepsilon>0$, let the bad-pair set for the original window be

$$\mathcal E_L(\varepsilon)
=\{(x,y)\in A_L^2:R_L(x,y)<n_L^\varepsilon\}.
\tag{B7}$$

The original assertion was

$$\exists\varepsilon,\delta>0\ \exists L_0\in\mathbb N\quad
\forall L\ge L_0:\quad
|\mathcal E_L(\varepsilon)|\le n_L^{2-\delta}.
\tag{HR-N1}$$

The inequality inside the bad-pair definition is **strictly less than**,
not less than or equal to. The exponents and starting level are fixed before
$L$ grows. The stronger conclusion below uses all integer powers, but the
assertion being refuted remains exactly this original finite-window one.

## C. Original role of HR-N1

The ultimate T03 target remains

$$\exists c>0\ \forall N_0\ge1\ \exists\text{ finite }A\subset\mathbb R:
\quad |A|\ge N_0,\qquad |Q(A,A)|\le |A|^{2-c}.$$

The polynomial, exponent and same-set requirement are fixed as displayed.

### C.1 The proved return-to-support implication

**PROVED implication — HR-1, specialized.** Suppose $X=A^2$, $n=|A|$,
and every pair outside an exceptional set $\mathcal E\subseteq X$ has
at least $M>0$ distinct returned pairs in $X$ with the same $Q$-value.
Then

$$|Q(A,A)|\le\frac{n^2}{M}+|Q(\mathcal E)|
                         \le\frac{n^2}{M}+|\mathcal E|.
\tag{C1}$$

Here $Q(\mathcal E)=\{Q(x,y):(x,y)\in\mathcal E\}$.
For completeness, every output outside $Q(\mathcal E)$ has a representative
outside $\mathcal E$, hence a full polynomial fiber containing at least
$M$ scalar ordered pairs. Those fibers are disjoint subsets of $X$.
There are at most $n^2/M$ such outputs, and at most $|Q(\mathcal E)|$
remaining outputs. This proves (C1). If transformations repeat a returned
pair, their multiplicity must first be divided out. Section E.1 verifies
that this loss is one for HR-N1; the scalar projection is also injective.

**CONDITIONAL application, now closed.** Had HR-N1 held, (C1) would give

$$|Q(A_L,A_L)|\le n_L^{2-\varepsilon}+n_L^{2-\delta}.
\tag{C2}$$

For every fixed $0<c<\min(\varepsilon,\delta)$, the right side is at
most $n_L^{2-c}$ for sufficiently large $L$. This would already solve
the same-set T03 target on the rational sequence $A_L$, without needing
an adaptive-radical transfer.

### C.2 Proposed connection with root-image compression

The conceptual route was to use many genuine returns to create sufficiently
large polynomial fibers, prove full-support compression, and seek a use for
that mechanism in the root-image problem. Its logical stages must be separated:

| Arrow | Exact status |
|---|---|
| Distinct legal returns imply equally many distinct points in the same $Q$-fiber | PROVED for this free norm action, §E.1 |
| A nearly-full return threshold implies a full-support upper bound | PROVED implication (C1), with exceptions explicitly charged |
| HR-N1 supplies that threshold on the carrier (B1) | FAILED / DISPROVED |
| Compression of this rational carrier transfers to the actual adaptive signed-root sets | UNKNOWN FROM CURRENT RECORD: no matching transfer theorem or carrier identification is in the completed HR-N1 files |
| The full RC15/4 hypotheses imply a recurrence and a fixed power saving | PROVED implication in the T03 source; its application is CONDITIONAL because RC15/4 is OPEN |

Thus “returns → root-image compression → possible RC15/4” describes an
intended mechanism, not an established chain of transfers for these particular
carriers. In particular $A_L$ is not identified with an adaptive $U_m$.
Large average collision energy alone is not the support argument (C1).

## D. Main theorem

**Theorem HN1-3 — PROVED (positive-density identity-only pairs).**
For every integer $m\ge2$, set $L=10m$ and define

$$\mathcal B_L=
\left\{\left(b7^{-k}19^{-\ell},c7^{-h}19^{-j}\right):
\begin{array}{l}
b,c\in D_L,\quad 0\le k,h\le L,\quad k\ne h,\\
0\le\ell\le m,\quad 9m\le j\le10m
\end{array}\right\}.
\tag{D1}$$

Then

$$|\mathcal B_L|\ge\frac{n_L^2}{200}.
\tag{D2}$$

For every $(x,y)\in\mathcal B_L$ and every $(r,s)\in\mathbb Z^2$,

$$T_{u^rv^s}(x,y)\in A_L^2\quad\Longrightarrow\quad r=s=0.
\tag{D3}$$

Equivalently $R_L^\infty(x,y)=R_L(x,y)=1$ on $\mathcal B_L$.
This statement excludes both signs of each exponent, beyond every finite
window. It makes no assertion that a full polynomial fiber has size one.

## E. Proof architecture and complete proof

The proof first establishes the following statement already proved as HN1-2
in the completed report: for any $L\ge1$, a pair

$$x=b7^{-k}19^{-\ell},\quad y=c7^{-h}19^{-j},\quad b,c\in D_L,$$

satisfying

$$k\ne h,\qquad \ell<j,\qquad
19^{j-\ell}>4L^2 7^L
\tag{E0}$$

has only the identity return under all $u^rv^s$. Section E.4 then verifies
(E0) and counts the class (D1). This is a restatement of the completed
argument, with its elementary local prerequisites included.

### E.1 Simultaneous denominator constraints

#### Split factors and valuations

In $\mathcal O$, put

$$\pi_7=3+\omega,\quad\bar\pi_7=2-\omega,\qquad
\pi_{19}=5+2\omega,\quad\bar\pi_{19}=3-2\omega.$$

Direct multiplication gives

$$\pi_7\bar\pi_7=7,\quad \pi_{19}\bar\pi_{19}=19,\quad
u=\pi_7/\bar\pi_7,\quad v=\pi_{19}/\bar\pi_{19}.
\tag{E1}$$

In particular $N(u)=N(v)=1$. To justify all local valuation steps without
an external factorization theorem, for integers $a,b$ calculate

$$\frac{a+b\omega}{\pi_7}
=\frac{2a+b+(-a+3b)\omega}{7},\qquad
\frac{a+b\omega}{\bar\pi_7}
=\frac{3a-b+(a+2b)\omega}{7},$$
$$\frac{a+b\omega}{\pi_{19}}
=\frac{3a+2b+(-2a+5b)\omega}{19},\qquad
\frac{a+b\omega}{\bar\pi_{19}}
=\frac{5a-2b+(2a+3b)\omega}{19}.
\tag{E2}$$

These show that divisibility by the four factors is respectively equivalent
to

$$a+4b\equiv0\ (7),\quad a+2b\equiv0\ (7),\quad
a+7b\equiv0\ (19),\quad a+11b\equiv0\ (19).
\tag{E3}$$

Each displayed residue of $\omega$ satisfies $X^2+X+1=0$ modulo its prime.
Evaluation is therefore a surjective ring homomorphism onto the prime field,
and (E2) identifies its kernel with the appropriate principal ideal.
These ideals are prime. Opposite factors above the same rational prime
do not divide each other, as evaluation also shows.

For a nonzero integral $z$, define $v_{\pi_p}(z)$ to be the largest power
of $\pi_p$ dividing it, and likewise for $\bar\pi_p$. This is finite
because $N(a+b\omega)=a^2-ab+b^2$ is a positive integer for nonzero
$a+b\omega$, and each such division lowers the norm by $p$.
Primality makes these orders additive on products: after maximal factors
are removed, the two residual nonzero classes have nonzero product.
Subtracting numerator and denominator orders extends the valuations to
$E^\times$. Clearing denominators proves the usual inequality on sums,
with equality when summand valuations differ. No unique-factorization
or class-number hypothesis has been used.

On rational numbers both valuations over $p$ restrict to $v_p$. This
follows from $p=\pi_p\bar\pi_p$ and (E3) for integers prime to $p$,
then by taking quotients. Conjugation exchanges the two valuations. Each
factor above one prime is a unit at both factors above the other: otherwise
its integer norm, $7$ or $19$, would be divisible by the other prime.
Consequently, for every pair of integers $r,s$,

$$\bigl(v_{\pi_7},v_{\bar\pi_7},v_{\pi_{19}},v_{\bar\pi_{19}}\bigr)
                          (u^rv^s)=(r,-r,s,-s).
\tag{E4}$$

This formula includes negative exponents. It proves the labels $(r,s)$
are distinct, and hence $|G_L|=(16L+1)^2$. Since $x-\omega y\ne0$
for a nonzero rational pair, field cancellation shows that distinct
multipliers give distinct returned pairs. All relevant stabilizers are
trivial. The identity is exactly $(r,s)=(0,0)$.

#### Recovering both scalar denominator depths

For $z=x-\omega y$ write $\alpha_p=v_{\pi_p}(z)$ and
$\beta_p=v_{\bar\pi_p}(z)$. Recover the rational coordinates by

$$y=\frac{\bar z-z}{\omega-\bar\omega},\qquad
x=\frac{\omega\bar z-\bar\omega z}{\omega-\bar\omega}.
\tag{E5}$$

The factors $\omega,\bar\omega$ are units and
$N(\omega-\bar\omega)=3$, so their use introduces no valuation loss at
$7$ or $19$. The formulas for $z,\bar z$ and the inverse formulas (E5)
give the two inequalities needed for

$$\min\{v_p(x),v_p(y)\}=\min\{\alpha_p,\beta_p\}.
\tag{E6}$$

If $\alpha_p\ne\beta_p$, each numerator in (E5) is a sum of terms
with different valuations. Thus **both** rational coordinate valuations
equal that minimum. Conversely, if $v_p(x)\ne v_p(y)$, the expressions
for $z$ and $\bar z$ have different summand valuations, so

$$\alpha_p=\beta_p=\min\{v_p(x),v_p(y)\}.
\tag{E7}$$

Set, for a pair satisfying (E0),

$$K=\max(k,h),\quad M=j,\quad e=j-\ell>0,\quad
a=K-k,\quad d=K-h.
\tag{E8}$$

The input depths are unequal at each prime. Hence the split valuations
of $z$ are $(-K,-K)$ above $7$ and $(-M,-M)$ above $19$.
For a hypothetical returned pair $(x',y')=T_{u^rv^s}(x,y)$ they are

$$(-K+r,-K-r),\qquad(-M+s,-M-s).
\tag{E9}$$

If $r\ne0$, both returned $7$-depths are $K+|r|$; if $s\ne0$,
both returned $19$-depths are $M+|s|$. Membership in $A_L$ requires
each depth to be an integer between $0$ and $L$ and each recovered
numerator to lie in $D_L$. When the two split valuations tie, (E6)
fixes only the larger coordinate depth; it does not force both depths
to coincide. This distinction is used below.

More generally the action introduces only powers of $7$ and $19$ in
coordinate denominators. For actual membership one must also exclude zero
coordinates and check both numerator bounds $1\le|b'|,|c'|\le L$.
No merely local necessary condition is being treated as sufficient.
In the proof these bounds follow from the explicit assumption of a return.

### E.2 Norm bounds exclude every nonzero $19$-exponent

For all real $X,Y$,

$$\frac34 X^2\le Q(X,Y)\le3\max(|X|,|Y|)^2.
\tag{E10}$$

The lower bound follows from $Q(X,Y)=(Y+X/2)^2+3X^2/4$;
the upper bound bounds the three terms separately. The norm in (B3)
therefore supplies a positive real quantity at the fixed real input
embedding. There is no approximation or choice among real embeddings.

Suppose a return has $s\ne0$. By (E9) and scalar recovery, both
returned $19$-depths equal $M+|s|$. Their $7$-depths are nonnegative
and their numerator magnitudes are at most $L$, so

$$|x'|,|y'|\le L19^{-M-|s|}.
\tag{E11}$$

On the other hand $|x|\ge7^{-L}19^{e-M}$. Norm preservation gives

$$\frac34 7^{-2L}19^{2e-2M}
\le Q(x,y)=Q(x',y')
\le3L^2 19^{-2M-2|s|}.$$

Taking square roots yields

$$19^e\le2L7^L19^{-|s|}\le2L7^L,
\tag{E12}$$

contradicting $19^e>4L^2 7^L$. Thus every return has $s=0$.
This exclusion is uniform in $r$ and in both coordinate signs.
The two primes' constraints have not been treated as independent probabilities.

### E.3 A prime-power congruence excludes every nonzero $7$-exponent

Now suppose $s=0$ but $r\ne0$, and put $t=|r|\ge1$. Both returned
$7$-depths equal $K+t$, so actual membership implies

$$K+t\le L,\qquad d+t\le L.
\tag{E13}$$

The two split valuations above $19$ remain $(-M,-M)$. Equation (E6)
therefore says that the maximum returned $19$-depth is exactly $M$.
After interchanging the returned coordinates if necessary **in the
symmetric norm equation only**, clearing the input denominator $7^K19^M$
and returned denominator $7^{K+t}19^M$ gives

$$Q(b'19^f,c')=7^{2t}Q(b7^a19^e,c7^d),
\qquad b',c'\in D_L,\quad f\ge0.
\tag{E14}$$

All quantities in this equation are integers; $f$ is the difference of
the two returned $19$-depths. The swap does not assert an additional group
action or add a return. Both possible original $7$-depth orderings are
included through $a,d\ge0$.

Apply (E10) to (E14). Since $|b|7^a\ge1$ and both returned numerators
are bounded by $L$,

$$3L^2 19^{2f}\ge\frac34 7^{2t}19^{2e},\qquad
19^f\ge\frac{7^t19^e}{2L}.
\tag{E15}$$

Define the integer $E_0=\min(e,f)$. Both $19^e$ and $19^f$ are at
least $19^e/(2L)$, so the dominant-gap hypothesis gives

$$19^{E_0}\ge\frac{19^e}{2L}>2L7^L.
\tag{E16}$$

In particular $E_0\ge1$, which excludes $f=0$. Reducing the exact
integer equation (E14) modulo $19^{E_0}$ removes every term containing
$19^e$ or $19^f$ and gives

$$c'^2\equiv c^2 7^{2(d+t)}\pmod{19^{E_0}}.
\tag{E17}$$

Equivalently $19^{E_0}$ divides

$$(c'-c7^{d+t})(c'+c7^{d+t}).$$

The two factors cannot both be divisible by $19$: their difference is
$2c7^{d+t}$ and $19\nmid c$. Hence one **entire** factor is divisible
by $19^{E_0}$. But (E13), the numerator bounds, and (E16) give

$$|c'\pm c7^{d+t}|\le L+L7^L\le2L7^L<19^{E_0}.
\tag{E18}$$

The divisible integer must be zero. This forces
$c'=\pm c7^{d+t}$, impossible because $d+t\ge1$ while $7\nmid c'$.
Therefore $r=0$. Together with §E.2, this proves HN1-2 for arbitrary
integer exponents. The identity is legal, so its return count is exactly
one, rather than merely at most one.

### E.4 Counting the bad pairs

For the class (D1), $e=j-\ell\ge8m$ and $L=10m$. For every $m\ge2$,

$$\frac{19^{8m}}{7^{10m}}
=\left(\frac{19^4}{7^5}\right)^{2m}
>49^m>400m^2=4L^2.
\tag{E19}$$

The first strict inequality uses $19^4=130321>117649=7^6$.
For the second, $49^2=2401>1600$, and induction holds because
$49>((m+1)/m)^2$ for $m\ge2$. This is an exact induction argument,
not extrapolation from enumerated carrier data. Thus every pair in (D1)
satisfies (E0) and has exactly one return.

The input representation is unique by §B.1. There are $d_L^2$ ordered
numerator choices, $(L+1)L$ ordered choices of unequal $k,h$, and
$(m+1)^2$ choices of $\ell,j$. Consequently

$$|\mathcal B_L|=d_L^2 L(L+1)(m+1)^2,$$
$$\frac{|\mathcal B_L|}{n_L^2}
=\frac{L}{L+1}\left(\frac{m+1}{10m+1}\right)^2
\ge\frac12\cdot\frac1{100}=\frac1{200}.
\tag{E20}$$

The two factors use $L/(L+1)\ge1/2$ and
$(m+1)/(10m+1)\ge1/10$. No identification of swapped pairs is made,
and no factor of two for symmetry is inserted. The set is a counted
subset of the original ordered square, not a replacement for that square.
This completes the proof of HN1-3. $\square$

## F. Why HR-N1 is false

Fix arbitrary $\varepsilon,\delta>0$ and any proposed starting level
$L_0$. Let $m$ tend to infinity through integers and set $L=10m$.
By (B2), $n_L\to\infty$, so eventually $L\ge L_0$, $m\ge2$,
$n_L^\varepsilon>1$ and $n_L^\delta>200$. For these levels,

$$\mathcal B_L\subseteq\mathcal E_L(\varepsilon),$$
$$|\mathcal E_L(\varepsilon)|\ge\frac{n_L^2}{200}
>n_L^{2-\delta}.
\tag{F1}$$

Thus no choice of fixed positive exponents and starting level can satisfy
(HR-N1). The sufficient large level may depend on the chosen exponents;
the theorem's constant $1/200$ and its range $m\ge2$ do not.
Failure on this unbounded subsequence suffices to refute “every sufficiently
large $L$”; no assertion for every $L$ is needed.

$$\boxed{\text{HR-N1 is false for every fixed }\varepsilon,\delta>0.}$$

## G. Exact scope of the obstruction

### PROVED consequences

- HR-N1 is **FAILED / DISPROVED** with its exact original quantifiers.
- At least $n_L^2/200$ ordered pairs are identity-only for every
  $L=10m$, $m\ge2$.
- Enlarging the exponent window to all of $\mathbb Z^2$ leaves those
  return counts equal to one. Window enlargement cannot repair this assertion.
- The specific application of (C1) that requires the HR-N1 pair-tail
  premise is **CLOSED**. “Closed” describes this certificate's disposition,
  not a new mathematical status for other constructions.

### Statements not proved

No conclusion of the form

$$|Q(A_L,A_L)|\ge n_L^{2-o(1)}$$

or any comparable full-image lower bound follows from this theorem.
The proof counts **pairs with few selected action returns**, not distinct
values of $Q$ on those pairs. For a pair $p$, the returned points satisfy

$$\{T_g(p):g\in\langle u,v\rangle,\ T_g(p)\in A_L^2\}
\subseteq\{q\in A_L^2:Q(q)=Q(p)\},
\tag{G1}$$

and equality has not been proved. Other norm-one multipliers, or other
descriptions of the same polynomial value, may connect the remaining points.
For example simultaneous sign reversal preserves $Q$ and $A_L^2$.
Its multiplier $-1$ is outside $\langle u,v\rangle$: (E4) would force
$r=s=0$, whose multiplier is $1$. Thus identity-only in this group
does not even mean singleton polynomial fiber.

Nor does a lower bound on $|\mathcal E_L(\varepsilon)|$ imply a lower
bound on $|Q(\mathcal E_L(\varepsilon))|$. Equation (C1) permits the latter
exceptional-output charge, but no useful bound for it is established here.

Accordingly the theorem does **not** prove that the affected rational
carrier has quadratic image, that the adaptive radical family has quadratic
image, that ARG or TCRC is false, that RC15/4 is false, that the ultimate
quadratic target is false, or that every return argument is impossible.
Failure of a sufficient certificate does not refute its desired conclusion.

## H. Relationship to RC15/4

### H.1 Distinct adaptive notation and exact obligation

**OPEN; imported state, unchanged.** To distinguish the adaptive family
from (B1), write it $\mathcal A_m$. Its recorded construction starts at
$\mathcal A_0=\{\pm1\}$. For a finite symmetric real set $A$, put
$M(A)=\max_{a\in A}|a|$ and, for $C>M(A)$,

$$d_C=C-M(A),\qquad
\mathcal L_C(A)=\{\pm\sqrt{(C+a)/d_C}:a\in A\},$$
$$\mathcal T_C(A)=
\{2C+a+b\pm\sqrt{(C+a)(C+b)}:a,b\in A\}.
\tag{H1}$$

The recorded actual optimizer chooses the legal parameter minimizing the
next image, with the fixed finite-list/least-parameter tie rule of T03 state
§3, and sets $\mathcal A_{m+1}=\mathcal L_{C_m}(\mathcal A_m)$.
This report uses that recorded family and one-step comparison property;
it does not reconstruct or rerun its optimizer algorithm. The elementary
lift identity is

$$Q(\mathcal L_C(A),\mathcal L_C(A))=d_C^{-1}\mathcal T_C(A).
\tag{H2}$$

Write

$$F_m=\mathbb Q(\mathcal A_m),\quad M_m=M(\mathcal A_m),\quad
n_m=|\mathcal A_m|=2^{m+1},\quad
s_m=|Q(\mathcal A_m,\mathcal A_m)|.$$

The **RC15/4** obligation, T03-O4, is to establish fixed $0\le H<\infty$ and
$m_0$ such that at every actual level $m\ge m_0$ one can explicitly choose

$$C_m^\dagger\in F_m,\qquad C_m^\dagger>M_m,$$
$$B_m\subseteq\mathcal A_m,\qquad e_m:=n_m-|B_m|\le H\sqrt{n_m},$$
$$\gamma_m>0,\quad u_a>0,\quad \gamma_m,u_a\in F_m,\qquad
C_m^\dagger+a=\gamma_mu_a^2\quad(a\in B_m),$$

so that the signed root set $U_m=\{\pm u_a:a\in B_m\}$ satisfies

$$\boxed{|\gamma_mQ(U_m,U_m)|
\le\frac{15}{4}s_m+Hn_m^{3/2}.}
\tag{RC15/4}$$

The selected $B_m$ lies in a single shifted square class. The roots are
distinct and nonzero, $|U_m|=2|B_m|$, and the corresponding component of
the comparison lift $\mathcal L_{C_m^\dagger}(\mathcal A_m)$ is
$\sqrt{\gamma_m/d_{C_m^\dagger}}\,U_m$. This does not identify the
comparison parameter $C_m^\dagger$ with the actual optimizer $C_m$.
Both signs, both coordinates,
the positive scalar $\gamma_m$, and the in-field conditions are retained.
The coefficient $15/4$, exponent $3/2$, and constants $H,m_0$ are uniform;
the parameters and root representatives may vary with the actual level.

### H.2 Recorded conditional consequence and retained gap

**PROVED implication; CONDITIONAL application.** The source's exception
accounting charges exactly

$$e_m(2n_m-e_m+1)\le3Hn_m^{3/2}$$

remaining unordered signed branch labels in (H1). These are labels for an
upper bound on outputs, distinct from HR-N1's ordered input-pair count.
Combining this with (RC15/4) and the recorded one-step optimizer comparison
would give

$$s_{m+1}\le\frac{15}{4}s_m+4Hn_m^{3/2},\qquad
s_m=O((15/4)^m).
\tag{H3}$$

The iteration is justified in T03 state §§4.7, 7 and the root-algebra
companion §6; $2^{3/2}<15/4<4$ controls the forcing term. Every fixed
$0<c<\log_2(16/15)$ would then give the target eventually. These are
conditional exponents, not results obtained from HR-N1.

HR-N1 explored a return mechanism directed toward the same compression
goal. Its exact pair-tail certificate is now eliminated. There is no proved
bridge in the completed files identifying its rational carrier with these
actual root sets (§C.2). RC15/4 therefore remains **OPEN**, with precisely
the same required hypotheses. A future proof cannot rely on the false
HR-N1 tail estimate; it must justify its root-image bound independently.
No replacement mechanism is proposed or investigated in this freeze.

## I. Research consequences and failure-registry scope

**T03-HRN1-F1 — FAILED / DISPROVED: positive-density identity-only return
obstruction.** The exact hypotheses are the fixed carrier (B1), primes
$7,19$, fixed generators (B4), and genuine return to $A_L^2$ under (B5).
The conclusion excludes every fixed positive exponent pair in (HR-N1),
including an attempted repair by taking all integer powers of these same
generators. It does not quantify over other carriers or actions.

Future arguments must not cite HR-N1, relabel it as an established lemma,
or assume its equivalent nearly-full polynomial-return premise for this
same sequence and action. The proved HR-1 implication remains available;
its false HR-N1 premise is the part that is closed. Historical OPEN/untested
entries are retained with the later controlling disposition linked.

**No replacement return conjecture is adopted in this freeze.**

### Frozen arithmetic and rate ledger

This specializes the [construction-ledger template](../../templates/CONSTRUCTION_LEDGER.md)
to the completed negative result; there is no surviving positive construction.

| Quantity or cost | Exact accounting |
|---|---|
| Input growth | $n_L=d_L(L+1)^2=(216/133)L^3+O(L^2)$, both lower and upper counts |
| Parameter/projection loss | One; the two rational valuations and numerator recover each input |
| Thinning of inputs | None; $\mathcal B_L$ is counted inside the original ordered square |
| Field and embedding | Rational real inputs; fixed $E=\mathbb Q(\omega)$ for actions |
| Discriminant, regulator, class number | No growing-field estimate or such invariant is used by this elementary proof; no arithmetic gain is claimed from them |
| Local primes and integrality | Explicit prime kernels (E2)–(E3); simultaneous depths (E9); both returned numerators lie in $D_L$ |
| Denominators and height | Common input denominator $133^L$; cleared numerators at most $L133^L$; action denominators divide $7^{\lvert r\rvert}19^{\lvert s\rvert}$ |
| Archimedean restrictions | Factors $2L$ and $4L^2 7^L$ are explicitly charged in (E12), (E15)–(E19) |
| Stabilizer/duplicate-action loss | Zero logarithmic loss: distinct multipliers give distinct returned pairs |
| States and branches | No state approximation; both unequal $7$-depth orderings are covered; target-coordinate swap gives no extra return |
| Exceptions for any positive return exponent | At least $n_L^2/200$ on $L=10m$, so the bad-pair exponent is two |
| Signed rate using $d=\log L$ | Input rate $a=B=3$; return rate zero on a positive fraction; exceptional-pair rate $6=2a$ |
| Output certificate | This application supplies no positive gap; only the trivial upper bound $n_L^2=e^{6d+O(1)}$ is asserted here |
| Actual image rate | OPEN; no lower bound follows from the failed certificate |

No unknown cost has been assigned a favorable value. The inapplicable
field-invariant estimates are absent from the proof, not waived costs of a
positive construction.

## J. Updated research frontier

| Item | Post-freeze status |
|---|---|
| Ultimate same-set T03 target for $Q$ | OPEN |
| Adaptive input doubling $n_m=2^{m+1}$ | PROVED in the controlling source; unchanged |
| ARG: $s_m\le K\rho^m$ for fixed $K<\infty$, $0<\rho<4$ on actual adaptive levels | OPEN |
| Eventual TCRC: a legal in-field parameter, a common shifted class with bounded exceptions, and three affine old-image copies at every sufficiently large actual level | OPEN |
| RC15/4, T03-O4 | OPEN |
| HR-N1 | FAILED / DISPROVED |
| HR-N1 fixed-positive-exponent pair-tail certificate | CLOSED |
| Actual quadratic-image rate for the rational $A_L$ | OPEN |

TCRC's affine maps may depend on the level but must be fixed across all
pairs at that level, with coefficients in $F_m$; its eventual assertion is
not refuted here. No historical finite obstruction is promoted to a failure
of ARG, TCRC or the arbitrary-real target.

**One existing next mathematical obligation, retained only:** T03-O4,
as selected in T03 current state §§7, 13–14: obtain an explicit legal
in-field parameter at every sufficiently large actual adaptive level, a
common root class with at most $H\sqrt{n_m}$ exceptions, and a direct bound
for the entire signed root image with coefficient $15/4$ and error
$Hn_m^{3/2}$. Identifications must cover all outputs, including those from
different completion blocks. This freeze neither starts that work nor
grants new research authorization.

## K. Proof audit checklist

The complete proof in §E was checked against the completed HN1-1–HN1-3
arguments. The following are proof checks, separate from file-integrity tests.

| Audit item | Resolution and controlling step |
|---|---|
| Quantifier order | Arbitrary fixed $\varepsilon,\delta,L_0$ first; then $m\to\infty$, $L=10m$; (F1) contradicts all sufficiently large levels |
| Ordered versus unordered pairs | HR-N1 and (E20) count ordered scalar pairs. No quotient by sign or swap; RC branch labels in §H are explicitly different |
| Identity convention | The valuation vector (E4) makes $(0,0)$ the unique identity label |
| Negative exponents | Valuations extend to field quotients; (E9) holds for all integers; conclusions use $\lvert r\rvert,\lvert s\rvert$ |
| Zero and diagonal pairs | No input is zero; a returned zero coordinate is illegal. Selected pairs have unequal $7$-depths and hence are not diagonal |
| Denominator clearing | Input denominator $7^K19^M$, returned denominator $7^{K+t}19^M$; their ratio gives precisely $7^{2t}$ in (E14) |
| Integrality and units | $b,c,b',c'\in D_L$; $a,d,e,f,t$ are nonnegative integers where used; both numerator bounds and coprimality are retained |
| Coordinate interchange | Permitted only because $Q$ is symmetric; it normalizes (E14), without assuming a new return |
| Field embedding | Inputs are rational in $\mathbb R$; $E$ is fixed in $\mathbb C$; coefficient map is injective |
| Norm normalization | $N(x-\omega y)=Q(x,y)$, $N(u)=N(v)=1$; real estimates are exactly (E10) |
| Prime-power valuations | Prime kernels (E2)–(E3) imply additive valuations. Whole-prime-power allocation in (E17) uses $19\nmid2c7^{d+t}$ |
| Exceptional primes | Coefficient recovery has norm-three denominator, a unit at both $7,19$; the congruence prime $19$ is odd and different from $7$ |
| Equal returned depths | When $s=0$, only the maximum $19$-depth is initially known. The possible $f=0$ is excluded by (E16), not assumed away |
| Original depth orderings | $k<h$ and $k>h$ are both covered by $K,a,d$; $\ell<j$ is part of the selected class |
| Dependence of constants | $1/200$ and $m\ge2$ are absolute; $4L^2$ and $2L$ are explicit. Only the contradiction's final starting level depends on $\varepsilon,\delta$ |
| Derivation of $1/200$ | Exact count divided by $d_L^2(L+1)^4$; factors at least $1/2$ and $1/100$ in (E20) |
| Uniform asymptotics | No $o(1)$ premise occurs. The only displayed input $O(L^2)$ has an absolute constant and is unnecessary for the exact counting argument |
| All-return coverage | Both nonzero-exponent cases excluded for all $(r,s)\in\mathbb Z^2$; no finite window or pruning assumption |
| Computation needed | None: identities, valuation arguments, inequalities and one induction suffice |
| Image conclusion | Only the selected orbit is counted; (G1) prevents interpreting a return bound as a full-fiber upper bound |

No missing premise or mathematical gap was identified in this audit.
Surrounding adaptive results are attributed to their controlling sources;
the freeze is not a new audit of all historical adaptive proofs.

## L. Independent review record

**Two independent internal reviews passed in the completed research cycle.**
They are not external peer reviews.

| Review | Recorded scope and evidence |
|---|---|
| First full obstruction review | [independent-audit.md](../2026-09-16-hr-n1-offline/independent-audit.md), §§1–5, directly records the generator convention, prime valuations, scalar recovery, signs and both depth orderings, denominator clearing, norm inequalities, congruence, explicit density and existential-quantifier contradiction; disposition PASS |
| Second full obstruction review | [verification.md](../2026-09-16-hr-n1-offline/verification.md), §2, records that the independent local-action author also read the complete HN1-2/3 proof and passed its joint-prime and quantifier checks. That review is recorded there rather than in a separate standalone review file |

The local-action companion separately supplies the independent HN1-1
derivation and records the lead's inspection. It is not by itself a second
standalone HN1-2/3 review text. The completed verification record reports a
cosmetic TeX correction identified by both reviewers; the corrected source
is preserved. It records no substantive mathematical correction. The final
theorem statement, constants, parameter range, and action scope did not
change. The evidence is an analytic proof, not a computational certificate.

For this final freeze, the lead and a delegated reader rechecked the
completed proof's assumptions and scope, and the source audit checked the
RC15/4 boundary. These are documentation/proof-audit activities, not a new
research cycle or additional claimed external certification.

## M. Computation, checks and reproducibility

| Item | Completed cycle and this freeze |
|---|---|
| Charged mathematical evaluations | **0** |
| Research-program CPU seconds | **0** |
| Carrier enumeration or finite oracle run | None |
| Why enumeration was omitted | The analytic obstruction settled the commissioned assertion before the conditional diagnostic was needed |
| Generator/inverse verification | Exact symbolic norm and matrix checks in HN1-1, §§2–3; no numerical equality premise |
| Network, literature search, downloads or installs | None attempted |
| Research or regression programs | Not run during this freeze; no experiment/test code changed |

Zero computation describes provenance; it does not confer additional
mathematical strength. The proof is reproducible by following §§B–F.
There are no new histograms, empirical rates, random seeds or finite data
to interpret as an asymptotic theorem.

The completed cycle ran `python3 scripts/check_repository.py`,
`python3 scripts/check_codex_setup.py`, and `git diff --check`, plus
new-file whitespace and baseline preservation checks. Recorded passes
covered 39 archived sources, links in 58 Markdown files, 42 local
references, 43 T03 archive members, 55 protected hashes and five original
navigation byte prefixes. These prior results are not mislabeled as new runs.

The same appropriate local documentation/reference checks are recorded
for the final freeze in [verification.md](verification.md), with commands,
actual results, runtime, preservation scope and hashes. Scripts are inspected
before execution. No historical source, completed proof, SPEC, archive, or
canonical source manifest is rewritten. New report/state/provenance files
and dated navigation appendices remain uncommitted. The machine-readable
state below is also provided as [final-state.yaml](final-state.yaml).

## N. Final theorem and failure ledger

| Item | Status | Meaning |
|---|---|---|
| HR-N1 | FAILED / DISPROVED | Positive-density identity-only pairs contradict every fixed-positive-exponent tail bound |
| Identity-only pair theorem | PROVED | At least $n_L^2/200$ ordered pairs for every $L=10m$, $m\ge2$ |
| All-integer-power conclusion | PROVED | Every nonidentity $u^rv^s$ return is excluded on those pairs |
| HR-N1 return certificate | CLOSED | The specified tail premise cannot establish the desired compression |
| Actual quadratic-image rate | OPEN | No full-image lower bound follows from the return obstruction |
| ARG and eventual TCRC | OPEN | Their adaptive-family premises are not refuted here |
| RC15/4 | OPEN | Its direct whole-root-image obligation remains unchanged |
| T03 quadratic target | OPEN | No disproof of the same-set real construction target |

## O. Machine-readable final state

```yaml
thread: T03
result_id: HR-N1
status: FAILED
mathematical_status: DISPROVED
theorem:
  parameter_range: "L=10m, m>=2"
  bad_pair_lower_bound: "|A_L|^2/200"
  return_count: 1
  surviving_return: "identity only"
  identity_exponents: [0, 0]
  action_scope: "all integer powers u^r v^s"
proof_mechanisms:
  - "simultaneous denominator constraints"
  - "norm bounds"
  - "prime-power congruence"
consequence:
  - "HR-N1 tail bound fails for every fixed epsilon,delta>0"
  - "the specified HR-N1 return-tail certificate is closed"
does_not_imply:
  - "quadratic-image target is false"
  - "actual image has quadratic size"
  - "RC15/4 is false"
  - "ARG/TCRC are false"
  - "every return-based argument is impossible"
remaining_status:
  quadratic_image_rate: OPEN
  quadratic_target: OPEN
  RC15_4: OPEN
  ARG: OPEN
  TCRC: OPEN
research_decision:
  - "freeze HR-N1 as disproved"
  - "do not repair or reuse the same tail certificate"
  - "do not adopt a replacement conjecture without a separate research cycle"
  - "retain T03-O4 as the existing next obligation; do not execute it in this freeze"
review:
  internal_reviews_passed: 2
  external_peer_review_claimed: false
computation:
  charged_evaluations: 0
  research_program_cpu_seconds: 0
  enumeration_performed: false
offline:
  network_access_attempted: false
```
