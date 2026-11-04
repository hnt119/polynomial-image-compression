# HR-N1: the two-prime return-tail assertion is false

**16 September 2026, version 1. Strictly offline constructive research cycle.**

**PROVED:** for every $L=10m$ with $m\ge2$, at least $|A_L|^2/200$
ordered pairs have exactly one return, the identity, under the specified
$G_L$. In fact those pairs have no other return under **any** integer-power
multiplier $u^rv^s$.

**Disposition: FAILED — HR-N1's existential return-tail assertion.** This
settles the commissioned assertion negatively. It is an obstruction to this
action certificate, not a lower bound on the entire quadratic image.
The original real-set target, the actual image rate of $A_L$, and RC15/4
remain **OPEN**. No follow-on research cycle or carrier search is launched.

## 1. Frozen question and provenance

Keep, exactly as commissioned,

$$Q(x,y)=x^2+xy+y^2,\qquad \omega^2+\omega+1=0,$$
$$A_L=\{b7^{-k}19^{-\ell}:1\le|b|\le L,\ \gcd(b,133)=1,
                              \ 0\le k,\ell\le L\},$$
$$u=\frac{8+5\omega}{7},\qquad v=\frac{21+16\omega}{19},\qquad
G_L=\{u^rv^s:|r|,|s|\le8L\}.$$

For $g=a+b\omega$, the action is

$$T_g(x,y)=(ax+by,-bx+(a-b)y),$$

and $R_{A_L,G_L}(x,y)$ counts distinct multipliers returning to the
**same scalar square** $A_L^2$. No subset replaces that square.

The frozen [preceding report](../2026-09-16-high-return/README.md), §7,
recorded HR-N1 as **OPEN and untested**. That report is preserved verbatim.
The present HN1-3 theorem is the controlling later proof for this particular
assertion. It neither changes T03's polynomial nor replaces its separate
adaptive RC15/4 obligation.

| Claim | Status, quantifiers and proof location | Dependencies / evidence / review |
|---|---|---|
| HN1-1 | **PROVED:** exact input/action algebra, all $L\ge1$; [local action](local-action.md) | Elementary residue-ring valuation proof, with the $7$-prime predecessor HR-2; independently derived and inspected in this task |
| HN1-2 | **PROVED:** every pair satisfying the explicit dominant $19$-gap condition in §3 has only the identity return under all $u^rv^s$ | HN1-1, elementary real norm inequalities and integer congruences; complete proof below, independently audited |
| HN1-3 | **PROVED:** a class of size at least $n_L^2/200$ meets HN1-2 for every $L=10m$, $m\ge2$; HR-N1 is false | HN1-2 and exact Cartesian counting; §4, independent audit |

All claims are dated/versioned by this file and its companions. These are
internal derivations and independent internal reviews, not external review
or novelty claims. The [independent audit](independent-audit.md) records
the proof checks separately. File/source hashes and local verification
results are in the cycle manifest and [verification record](verification.md).

## 2. Input count, action and simultaneous depth constraints

Put

$$B_L=\{b\in\mathbb Z:1\le|b|\le L,\ \gcd(b,133)=1\},$$
$$b_L=|B_L|=2\bigl(L-\lfloor L/7\rfloor-\lfloor L/19\rfloor
                                      +\lfloor L/133\rfloor\bigr).$$

The two rational valuations recover $k$ and $\ell$ in the representation
of an input; the numerator is then recovered exactly. Thus

$$n_L=|A_L|=b_L(L+1)^2
                =\frac{216}{133}L^3+O(L^2).\tag{1}$$

This is both a lower and upper input count; there are no parameter fibers.
All inputs are nonzero rational numbers, so there is no zero-pair exception.

Use the factorizations

$$7=\pi_7\bar\pi_7,\quad \pi_7=3+\omega,\quad
19=\pi_{19}\bar\pi_{19},\quad \pi_{19}=5+2\omega.$$

Then $u=\pi_7/\bar\pi_7$, $v=\pi_{19}/\bar\pi_{19}$ and both have
norm one. Each generator is a unit at both primes over the other rational
prime. The four split valuations of $u^rv^s$ are

$$ (r,-r,s,-s).\tag{2}$$

Consequently the labels are distinct, $|G_L|=(16L+1)^2$, and the action is
free on every pair in $A_L^2$: $x-\omega y\ne0$, so cancellation in the
field makes distinct multipliers give distinct returned pairs.

The exact generator matrices and inverses are

$$U=\frac17\begin{pmatrix}8&5\\-5&3\end{pmatrix},\qquad
U^{-1}=\frac17\begin{pmatrix}3&-5\\5&8\end{pmatrix},$$
$$V=\frac1{19}\begin{pmatrix}21&16\\-16&5\end{pmatrix},\qquad
V^{-1}=\frac1{19}\begin{pmatrix}5&-16\\16&21\end{pmatrix}.$$

Their inverse and norm identities were checked symbolically in the
independent local-action derivation. No floating-point equality, numerical
embedding or empirical inverse test is a proof premise.

### The local fact used at both primes

For $z=x-\omega y$, let $\alpha_p=v_{\pi_p}(z)$ and
$\beta_p=v_{\bar\pi_p}(z)$, for $p=7,19$. The elementary local proof in
HN1-1 gives

$$\min\{v_p(x),v_p(y)\}=\min\{\alpha_p,\beta_p\}.\tag{3}$$

If $\alpha_p\ne\beta_p$, **both** rational coordinates attain that
minimum. If the two input denominator depths at $p$ differ, then the two
split valuations are equal to minus the deeper input depth. These statements
use coefficient recovery from $z,\bar z$; its denominator
$\omega-\bar\omega$ is a unit at $7$ and $19$. The companion proof
establishes the needed prime kernels and valuation rules without an external
factorization, regulator or class-number theorem.

In particular, for unequal input depths at $7$, multiplication by a
nonzero $u$-exponent $r$ forces **both returned $7$-depths** to be the old
maximum plus $|r|$. The corresponding statement holds at $19$ for $s$.
These are simultaneous necessary conditions on actual returned coordinates,
not independent marginal probabilities. HN1-1 lists all nine depth-order
types; equal-depth cases are not silently included in this rule.

## 3. HN1-2 — a dominant gap forces the identity

**Theorem HN1-2 — PROVED.** Fix $L\ge1$ and a pair in the frozen carrier,
written uniquely as

$$x=b7^{-k}19^{-\ell},\qquad y=c7^{-h}19^{-j},\qquad b,c\in B_L.$$

Suppose

$$k\ne h,\qquad \ell<j,\qquad
19^{j-\ell}>4L^2\,7^L.\tag{4}$$

If $T_{u^rv^s}(x,y)\in A_L^2$ for integers $r,s$, then $r=s=0$.
Thus the return count for this pair under $G_L$ is exactly one.

### Proof, step 1: eliminate every nonzero $19$-exponent

Set

$$K=\max(k,h),\quad M=j,\quad e=j-\ell,\quad
a=K-k,\quad d=K-h.$$

The two split valuations initially equal $-K$ at $7$ and $-M$ at $19$.
Equation (2) shifts them to

$$(-K+r,-K-r),\qquad(-M+s,-M-s).\tag{5}$$

Suppose a returning multiplier has $s\ne0$. By (3), both returned
coordinates $x',y'$ have $19$-depth exactly $M+|s|$. Membership in $A_L$
then gives

$$|x'|,|y'|\le L19^{-M-|s|}.$$

For all real $X,Y$,

$$\frac34X^2\le Q(X,Y)\le3\max(|X|,|Y|)^2.\tag{6}$$

The first inequality is $Q=(Y+X/2)^2+3X^2/4$; the second follows by
bounding its three terms. Here $|x|\ge7^{-L}19^{e-M}$ because
$|b|\ge1$ and $k\le L$. Norm preservation and (6) imply

$$\frac34\,7^{-2L}19^{2e-2M}
    \le Q(x,y)=Q(x',y')\le3L^2 19^{-2M-2|s|}.$$

Taking positive square roots yields

$$19^e\le2L\,7^L19^{-|s|}\le2L\,7^L,$$

contrary to (4). This excludes $s\ne0$ regardless of $r$; there is no
independence assumption between the two prime constraints.

### Proof, step 2: eliminate every nonzero $7$-exponent

Now $s=0$. Suppose $r\ne0$, and put $t=|r|\ge1$. The $7$-valuations
in (5) differ, so both returned coordinates have $7$-depth $K+t$.
Since they are in $A_L$, necessarily

$$K+t\le L,\qquad d+t\le L.\tag{7}$$

The $19$-split valuations still both equal $-M$. By (3), the larger of
the two returned $19$-depths is exactly $M$. After possibly interchanging
the two returned coordinates in the **symmetric norm equation only**, there
are $b',c'\in B_L$ and an integer $f\ge0$ such that

$$Q(b'19^f,c')
       =7^{2t}Q(b7^a19^e,c7^d).\tag{8}$$

Indeed these equations come from clearing the common input denominator
$7^K19^M$ and returned denominator $7^{K+t}19^M$. Both returned scalar
membership conditions, including their numerator bounds and coprimality,
are retained in $b',c'\in B_L$. A swap is not counted as another multiplier.

Using (6), $|b|\ge1$, $a\ge0$, and $|b'|,|c'|\le L$ gives

$$3L^2 19^{2f}\ge\frac34\,7^{2t}19^{2e},\qquad
19^f\ge\frac{7^t19^e}{2L}.$$

Let $E=\min(e,f)$. Then

$$19^E\ge\frac{19^e}{2L}>2L\,7^L.\tag{9}$$

In particular $E\ge1$; this also rules out the possible equal returned
$19$-depth case $f=0$. Reduce (8) modulo $19^E$. All terms involving
$19^e$ or $19^f$ vanish except the unscaled squares, giving

$$c'^2\equiv c^2 7^{2(d+t)}\pmod{19^E}.$$

Thus $19^E$ divides

$$(c'-c7^{d+t})(c'+c7^{d+t}).$$

The two factors cannot both be divisible by $19$, because their difference
is $2c7^{d+t}$ and $19\nmid c$. Therefore one entire factor is divisible
by $19^E$. But (7), (9) and the numerator bounds give

$$|c'\pm c7^{d+t}|\le L+L7^L\le2L7^L<19^E.$$

The divisible factor must be zero. This would require
$c'=\pm c7^{d+t}$, impossible because $d+t\ge1$ and $7\nmid c'$.
The contradiction excludes $r\ne0$. Hence $r=s=0$. The identity belongs
to $G_L$ and returns every pair, proving the asserted exact count. $\square$

## 4. HN1-3 — positive density and disproof of HR-N1

Let $L=10m$, $m\ge2$, and define the following explicit class of ordered
pairs, without changing the carrier:

$$\mathcal C_L=\{(b7^{-k}19^{-\ell},c7^{-h}19^{-j}):
  b,c\in B_L,\ 0\le k,h\le L,\ k\ne h,
  \ 0\le\ell\le m,\ 9m\le j\le10m\}.$$

For every member, $e=j-\ell\ge8m$. The required dominance holds:

$$\frac{19^{8m}}{7^{10m}}
   =\left(\frac{19^4}{7^5}\right)^{2m}
   >49^m>400m^2=4L^2.\tag{10}$$

For the first strict inequality, $19^4=130321>117649=7^6$. The second
holds at $m=2$ since $49^2=2401>1600$, and propagates because multiplying
the left side by $49$ dominates the factor $((m+1)/m)^2\le9/4$ on the
right. This is an exact inequality for every $m\ge2$, not a numerical
fit or finite-search inference.

HN1-2 now gives

$$R_{A_L,G_L}(x,y)=1\qquad((x,y)\in\mathcal C_L).\tag{11}$$

Every scalar parameterization is injective, so the class size is exactly

$$|\mathcal C_L|=b_L^2 L(L+1)(m+1)^2.$$

Using (1),

$$\frac{|\mathcal C_L|}{n_L^2}
   =\frac{L}{L+1}\left(\frac{m+1}{10m+1}\right)^2
   \ge\frac12\cdot\frac1{100}=\frac1{200}.\tag{12}$$

**Theorem HN1-3 — PROVED.** HR-N1 is false. To see the quantifiers
explicitly, fix arbitrary $\varepsilon,\delta>0$. Along $L=10m\to\infty$,
$n_L\to\infty$ and $n_L^\varepsilon>1$. By (11)–(12),

$$\#\{(x,y)\in A_L^2:R_{A_L,G_L}(x,y)<n_L^\varepsilon\}
       \ge\frac{n_L^2}{200}>n_L^{2-\delta}$$

once $n_L^\delta>200$. This contradicts the proposed bound along an
unbounded subsequence, for **every** proposed pair of fixed positive
exponents. Consequently it cannot hold for all sufficiently large $L$.
This is not a failure at finitely many sizes or for one guessed exponent.
$\square$

## 5. Relationship to HR-1 and the one-prime arguments

The preceding [HR-1 theorem](../2026-09-16-high-return/return-lemma.md)
correctly turns a nearly full high-return tail into a full-support bound.
All its action/projection hypotheses here hold with multiplicity one. The
missing hypothesis is now disproved: a positive fraction of pairs has no
nonidentity return. A threshold $n_L^\varepsilon$ would charge at least
$n_L^2/200$ exceptional pairs along this subsequence. A subquadratic pair
exception term is therefore unavailable for this assertion.

What survives from [HR-2–HR-4](../2026-09-16-high-return/denominator-obstruction.md):

- Unique rational denominator depths and the equal split valuations for
  unequal scalar depths survive at **each** prime.
- A nonzero multiplier exponent turns that equal pair of split valuations
  into unequal valuations, forcing **both** returned scalar depths up.
- Real norm bounds and exact integer congruences can still jointly obstruct
  returns when one denominator gap dominates all possible compensation
  from the other prime.

What does not transfer directly:

- The uniform $O(\log H)$ one-prime imbalance bound cannot simply be
  repeated: clearing a $7$-depth gap can leave powers of $19$ in the
  numerator, and conversely. Such a numerator is not bounded by $L$.
- The one-prime full-fiber argument does not establish an actual-image
  lower bound here. Its small-height/divisor estimates are not assumed
  uniform after introducing the other denominator prime.
- Marginal local return fractions cannot be multiplied. The proof first
  excludes $s\ne0$ uniformly in $r$, then uses the remaining exact norm
  equation and coprimality to exclude $r\ne0$.

An arbitrary equal-norm pair may be related by a norm-one multiplier outside
$\langle u,v\rangle$. Therefore (11) does **not** say that its polynomial
fiber is a singleton. Global sign and coordinate swap already illustrate
the distinction. No lower bound on $|Q(A_L,A_L)|$ or on
$|Q(\mathcal C_L)|$ is asserted. Exceptional-output compression, a different
action certificate or a construction on some other subsequence would
require separate results; none has been proved or investigated here.

## 6. Construction and signed-rate ledger

This specializes the [construction-ledger template](../../templates/CONSTRUCTION_LEDGER.md)
to a negative result; identity/provenance and coverage are in §§1–4,
and evidence/disposition are in §§5–7.

The carrier, generators and parameter order are fixed before $L$ grows.
The proof only selects a class of obstructed pairs to disprove the tail; it
does not thin the carrier or propose that class as a non-Cartesian input.

| Gain/cost | Bound, source and exact scope | Status |
|---|---|---|
| Fixed inputs and polynomial | Exactly the commissioned $A_L$ and $Q$, both coordinates from the same set | PROVED setup |
| Lower and upper input count | Exact (1), $n_L=(216/133)L^3+O(L^2)$ | PROVED |
| Parameter and scalar projection fibers | One, recovered from the two rational valuations and numerator | PROVED |
| Input thinning, both coordinates | No thinning. The obstructed pair class is counted inside the original square by (12), not used as a substitute input | PROVED |
| Field degree / real projection | Inputs in $\mathbb Q\subset\mathbb R$; fixed quadratic norm field $\mathbb Q(\omega)$ | PROVED |
| Discriminant / root discriminant | Fixed field, discriminant $-3$; no degree limit or lattice-volume gain is used | Inapplicable asymptotic cost |
| Regulator / class number / units | Explicit fractional generators and residue kernels suffice; no regulator or class-number estimate is invoked | Inapplicable estimates |
| Local splitting and ideal indices | Both primes factored explicitly; four valuation shifts exactly (2). Legality is proved pointwise, without a residue-density approximation | PROVED |
| Input denominators and heights | Common denominator $133^L$; input absolute value at most $L$; cleared numerator height at most $L133^L$ | PROVED |
| Action denominators | Coefficients of $u^rv^s$ have denominators dividing $7^{|r|}19^{|s|}$; required returned depths are charged in (5)–(7) | PROVED |
| Archimedean distortion | Exact real norm inequalities (6), with both signs allowed. They force the dominant-gap contradiction; no continuous overlap heuristic | PROVED |
| Stabilizers and duplicate labels | Trivial on every pair; $(r,s)$ labels injective. No zero inputs | PROVED |
| Branches, swaps, states and carries | Nine input depth-order types identified; proof uses the explicit unequal/unequal class. The target swap is only in a symmetric equation and gives no extra action count | PROVED |
| Available action count | $(16L+1)^2$, but every point of $\mathcal C_L$ has effective return count one even under all integer powers | PROVED |
| Exceptional-pair cost | For any positive return threshold exponent, at least $n_L^2/200$ pairs must be exceptional when $L=10m$, $m\ge2$ | PROVED |
| Signed rate in $d=\log L$ | Input rate $a=B=3$. Raw action-count capacity is 2, but return rate on the obstructed class is 0 with duplicate loss 0. The bad-pair exponent is $6=2a$ | FAILED tail gate |
| Full-support consequence | HR-1 remains valid, but its pair-exception premise gives no positive fixed gap here. Actual output exponent not determined | OPEN actual image |
| Available uniform support certificate | The trivial $|Q(A_L,A_L)|\le n_L^2=e^{6d+O(1)}$ remains; net certified gap $2a-6=0$, so no positive exponent below gap$/B$ is supplied | PROVED bound; FAILED positive-rate certificate |
| Target disposition | No fixed $\varepsilon,\delta>0$ can satisfy HR-N1 for all large $L$ | FAILED assertion, PROVED obstruction |

No unknown arithmetic cost was set to zero. The entries marked inapplicable
are estimates absent from this elementary negative proof, not claimed gains
in an unbuilt positive construction.

## 7. Computation decision, offline boundary and verification

The announced global ceiling was **2,000,000 charged evaluations and
600 CPU seconds**, shared by all agents. The exact $L=1,2$ diagnostic was
conditional on an unresolved mechanism after the analytic screen. HN1-2/3
closed the assertion before that condition arose, so the exhaustive
diagnostic was **not run**. No $L=3$ or larger case was enumerated, no
smaller action window was substituted, and no return or image histogram
is presented as newly measured evidence.

**Actual mathematical computation usage: zero charged pair/polynomial
evaluations and zero research-program CPU seconds.** Generator and inverse
checks were exact symbolic identities, independently derived in HN1-1;
no finite oracle or research program was executed. Local file hashing,
documentation checks and proof reading are recorded separately. This cycle
therefore has no EXPERIMENTAL mathematical claim, random seed, or omitted
research error log.

Only local files, local tools and Python's standard library were used.
**No network access was attempted by the lead or any delegated agent.**
No external link was followed, package installed, download made, connector
used, browser opened, or remote Git operation performed. All proof
dependencies needed here are locally available or proved in the new notes;
there is no missing premise for HN1-1–HN1-3. The historical MC-03 checkpoint
designation and standalone F25 gap remain unrelated and unchanged.

The local repository/reference check scripts were inspected before
execution: they perform local reads/hashes and skip external URLs. Their
actual results, commands, runtime and hashes are in [verification](verification.md).
No experiment or test code changed, so the existing mathematical regression
suites were not rerun. Completed reports, archives, migration sources,
SPECs and inherited work are preserved. Dated entries are appended to the
project map, T03 status and the mechanism/failure/open-lemma registries.
All changes remain uncommitted.
