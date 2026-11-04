# Cartesian Norm-Symmetry Research Checkpoint

**Final frozen report and research handoff**
**T03: $Q(x,y)=x^2+xy+y^2$**
Research completed: 16 September 2026. Documentation freeze: 20 September 2026. Version 1.

This report consolidates completed source results. It conducts no new proof search, experiment, literature search or independent proof audit. All preparation was offline. `PROVED` below means an identified complete argument in the retained source system, with the original internal reviews recorded in Appendix B. This freeze checks source consistency and presentation; it makes no novelty or external peer-review claim.

## 1. Executive summary

> **Frozen verdict: ACTION GO / CARTESIAN FAIL, in the stated scopes.**

The program sought a full-rank analogue of C0's rank-one compression: use norm-one transformations to give almost every pair of a common scalar Cartesian square many distinct equal-$Q$ representations, then apply a full-support counting lemma.

The completed cycles isolate three separate issues. Earlier rational carriers had too few Cartesian returns. The correlated $7,19$ model then achieved uniformly many modular returns, but every group-compatible realization by real norm-one multipliers had at most 18 distinct actions. Finally, an explicit unit-exponent construction achieved $3^d$ distinct actual real actions and at least $2^d$ genuine returns at every engineered orbit point, with typical log-return rate

$$\mu=\frac{2\log2+\log3}{3}>0.$$

Its scalar coefficient set has $n_d=2\cdot3^d$ elements, while the engineered orbit supplies only $3^d$ ordered pairs. Its fraction of the required full square is therefore

$$\boxed{\frac{3^d}{(2\cdot3^d)^2}=\frac1{4\cdot3^d}.}$$

This vanishing coverage closes the engineered-orbit certificate. It does **not** determine the primary scalar family's incidental cross-pair returns or actual asymptotic image size; both remain **OPEN**. For the separate sparse valuation family, every pair has only the identity return under the entire selected integer-power group. An independent image theorem gives $n_d^2/4+n_d/2$, hence zero signed exponent gap for that family.

No full-rank quadratic power saving follows from these architectures. The missing bridge is **dense Cartesian realization of a high-return norm orbit**. A universal obstruction to norm-symmetry constructions has not been proved.

The carrier search is frozen. The general homogeneous and affine targets remain **OPEN**. The sole retained next constructive obligation is the existing **T03-O4 / RC15/4**, with its original actual-level, large-class and whole-signed-root hypotheses. It is recorded, not attempted, in this task.

## 2. Original goal

### Mathematical statement

For the fixed polynomial

$$Q(x,y)=x^2+xy+y^2,$$

the target is a fixed $c>0$ and arbitrarily large finite $A\subset\mathbb R$ such that

$$|Q(A,A)|\le |A|^{2-c}.$$

The same set must be used in both coordinates, and **every ordered pair** in $A^2$ must be covered. The coefficient $c$ cannot tend to zero with the set size.

Corrected C0 is **PROVED within the supplied source system** for

$$P(x,y)=(ax+by)^2+cx+ey,$$
$$a,b,c,e\in\mathbb Z,\qquad\gcd(a,b)=1,\qquad ab(ae-bc)\ne0.$$

Its saving exponent may depend on the fixed coefficients and is not uniform over the family. Its quadratic part has rank one. In contrast, the symmetric matrix of $Q$ has determinant $3/4$ and rank two. For

$$\omega=\frac{-1+i\sqrt3}{2},\qquad K=\mathbb Q(\omega),$$

the norm identity is

$$Q(x,y)=(x-\omega y)(x-\bar\omega y)=N(x-\omega y).$$

For rational coordinates this is the field norm; for real coordinates it is the same complex absolute-square identity.

### What it means

C0 obtains sparse square residues after an exact deformation and scaling. The proposed extension sought many norm-preserving **Cartesian representations** as a substitute for that rank-one mechanism. Norm identities and more complicated fields are useful only if they lead to a small entire image on a growing common scalar set.

### Why it matters

The algebraic rewrite supplies symmetries but does not establish where their images land. The completed program therefore tested the chain from actual actions, through genuine returns, to a full-support upper bound. The extension from C0 to $Q$ remains incomplete. The broader affine benchmark $Q+x$ is discussed in Section 10. Sources: [C0 and transfer locators](#appendix-c-source-register-and-authority), [unit cycle](../2026-09-16-unit-exponent/README.md).

## 3. Return framework

### 3.1 Actual action and three different counts

For $u=\alpha+\beta\omega$ with real $\alpha,\beta$ and $N(u)=1$, multiplication of $z=x-\omega y$ induces

$$T_u(x,y)=(\alpha x+\beta y,-\beta x+(\alpha-\beta)y),$$
$$Q(T_u(x,y))=Q(x,y).$$

Let $\mathcal L$ be a finite family of transformation labels, possibly repeated, acting on a finite scalar carrier $A$. A label is **eligible** at $p=(x,y)$ only if its actual transformed pair belongs to the same $A^2$. Define

$$\begin{aligned}
R_{\rm label}(p)&=\#\{\ell\in\mathcal L:T_\ell(p)\in A^2\},\\
R_{\rm action}(p)&=\#\{T_\ell:\ell\text{ eligible at }p\},\\
R_{\rm pair}(p)&=\#\{T_\ell(p):\ell\text{ eligible at }p\}.
\end{aligned}$$

Thus $R_{\rm label}\ge R_{\rm action}\ge R_{\rm pair}$. A finite-ring return is a return in that ring; it becomes a real return only after an actual compatible realization is proved. One cannot compare counts across those domains without such a map.

**PROVED.** Distinct complex multipliers act freely on every nonzero $z$: $uz=vz$ implies $u=v$. If $0\in A$ and the action family is nonempty, at $(0,0)$ all actions fix the same pair, so $R_{\rm pair}=1$ even if $R_{\rm action}$ is large. Repeated labels and projection fibers create additional losses in more general models.

### 3.2 Return-to-image theorem (HR-1, retained proof)

**Mathematical statement - PROVED.** Let $n=|A|$, $\mathcal E\subseteq A^2$, and suppose every $p\notin\mathcal E$ has at least $M>0$ eligible, value-preserving labels. Assume at most $D$ such labels produce any one returned scalar pair. Then

$$\boxed{|Q(A,A)|\le\frac{n^2}{\lceil M/D\rceil}+|Q(\mathcal E)|
\le\frac{n^2D}{M}+|\mathcal E|.}$$

**Proof.** Every output with a nonexceptional representative has at least $\lceil M/D\rceil$ pairs in its complete fiber. These fibers are disjoint subsets of $A^2$. Outputs having only exceptional representatives contribute at most $|Q(\mathcal E)|$. This accounts for every output.

For decorated states $S$ with a surjection $\pi:S\to A^2$, choose one lift of each nonexceptional scalar pair. If at most $h$ labels give one returned state and at most $\Lambda$ returned states give one scalar pair, use $D=h\Lambda$. Preservation must be the exact identity $Q(\pi(Ts))=Q(\pi(s))$. Surjectivity, denominators, branches and scalar membership cannot be omitted. Group stabilizers bound label-to-point duplication; a partial action needs its own bound. These are the chosen-lift hypotheses of [HR-1(a')](../2026-09-16-high-return/return-lemma.md).

**What it means.** Only distinct returned scalar pairs lower-bound the actual polynomial fiber. Neither a large label count nor a selected collection of rich fibers controls the remaining outputs.

**Why it matters.** If

$$n=e^{ad+o(d)},\quad M=e^{rd-o(d)},\quad D=e^{sd+o(d)},\quad
|\mathcal E|\le e^{(2a-\delta)d+o(d)},$$

with fixed $a>0$, the output exponent is at most

$$b\le\max\{2a-r+s,2a-\delta\}.$$

A positive gap requires $\min(r-s,\delta)>0$. Every fixed $c<\min(r-s,\delta)/a$ then works eventually. This implication is **PROVED**; a suitable full-square premise remains **OPEN**. Collision energy alone provides no substitute for this support argument.

## 4. High-return cycle and HR-N1 closure

### 4.1 Dense one-prime denominator carriers

**Mathematical statement - PROVED, HR-4.** For a prime $p$ and integers $H\ge1$, $L\ge0$, set

$$A_{H,L,p}=\{bp^{-k}:1\le|b|\le H,\ p\nmid b,\ 0\le k\le L\}.$$

Then $n=2(H-\lfloor H/p\rfloor)(L+1)$. For every fixed $\eta>0$ there is $C_\eta$, uniform in $p,H,L$, such that

$$\max_t\#\{(x,y)\in A_{H,L,p}^2:Q(x,y)=t\}\le C_\eta H^\eta,$$
$$|Q(A_{H,L,p},A_{H,L,p})|\ge C_\eta^{-1}n^{2-\eta}.$$

**What it means.** Even denominator depth large enough to defeat a polynomial-height screen does not produce a fixed saving for this dense numerator alphabet. The proof recovers depths using valuations, separates large and small gaps, and counts integer norm representations.

**Why it matters.** This is an actual image obstruction for this family, stronger than failure of one action. It does not cover arbitrary sparse alphabets or several denominator primes. The other early architecture failures and their boundaries are listed in Section 9.

### 4.2 The two-prime rational tail assertion HR-N1

**Mathematical statement - FAILED / DISPROVED.** Here the rational carrier and action were

$$A_L=\{b7^{-k}19^{-\ell}:1\le|b|\le L,\ \gcd(b,133)=1,
\ 0\le k,\ell\le L\},$$
$$u=\frac{8+5\omega}{7},\quad v=\frac{21+16\omega}{19},\quad
G_L=\{u^rv^s:|r|,|s|\le8L\}.$$

Here all denominator depths and action exponents are integers. Writing $n_L=|A_L|$, HR-N1 asserted the existence of fixed $\varepsilon,\delta>0$ such that, for every sufficiently large $L$,

$$\#\{(x,y)\in A_L^2:R_{A_L,G_L}(x,y)<n_L^\varepsilon\}
\le n_L^{2-\delta}.$$

**PROVED, HN1-2/3.** For every $L=10m$, $m\ge2$, at least $n_L^2/200$ ordered pairs have exactly one return, even under **all** $u^rv^s$, $(r,s)\in\mathbb Z^2$. The surviving exponent pair is $(0,0)$. Simultaneous denominator constraints, norm bounds and a prime-power congruence prove this statement analytically.

**What it means.** Along $m\to\infty$, $n_L\to\infty$. For any fixed positive $\varepsilon,\delta$, these pairs lie below $n_L^\varepsilon$ and $n_L^2/200>n_L^{2-\delta}$ eventually. The asserted tail is false with its original quantifiers.

**Why it matters.** HR-N1 and its sufficient tail certificate are closed. This is a bad-pair theorem, not an image lower bound: collisions from other multipliers or other mechanisms remain possible. The initial high-return report's HR-N1 `OPEN` entry is **HISTORICAL / SUPERSEDED** by the [completed final proof report](../2026-09-16-hr-n1-final-freeze/README.md). No replacement conjecture is adopted.

## 5. Correlated two-prime $7,19$ cycle

> **LOCAL GO / GLOBAL FAIL.** Many modular returns were achieved. The compatible real action count collapsed.

### Mathematical statement - PROVED, TP-L1/TP-P1

Let $R=\mathbb F_7\times\mathbb F_{19}$ and let $\chi_p$ be the quadratic character. Define

$$D=\{(a,b)\in\mathbb F_7^\times\times\mathbb F_{19}^\times:
\chi_7(a)=\chi_{19}(b)\}.$$

There are $|D|=54$ scalars and $2916$ ordered pairs. At each prime the Eisenstein algebra splits, and norm-one multiplication in its two factors is $(t,t^{-1})$. The full action group is $G\cong C_6\times C_{18}$, of size 108. It acts by the coefficient formula in Section 3, interpreted in $R$. Both transformed coordinates must belong to $D$.

The exact local return distribution is:

| Return count | 8 | 10 | 12 | 18 | 24 | 26 | 30 | 54 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ordered pairs | 216 | 270 | 216 | 108 | 648 | 702 | 540 | 216 |

All stabilizers are trivial, even on the relevant zero-norm pairs. The minimum is 8, median 25, maximum 54, mean $218/9$, and geometric mean

$$2^{5/3}3^{7/9}5^{5/18}13^{13/54}\simeq21.6342.$$

On $D^d$ with the product action, returns multiply exactly:

$$R_d=\prod_{i=1}^d r_i\ge8^d,\qquad
\#\{R_d<18^d\}\le2772^d.$$

There are $2916^d$ total pairs. The exact modular vector image has size $130^d$; the reciprocal-return support bound gives $154^d$. These are finite-ring counts.

### What it means - PROVED realization obstruction, TP-G1

For any group homomorphism $\rho:G^d\to\{z\in\mathbb C:|z|=1\}$, every image element has order dividing 18. Thus

$$|\rho(G^d)|\le18.$$

Under a common equivariant realization of pairs, no more than 18 distinct actual actions, hence 18 returned real pairs, survive. Among $M$ returning labels some actual pair receives at least $M/18$ labels. The exponential formal return gain is lost to duplication.

### Why it matters

This model failed at **real action realization**, not local return scarcity. The theorem is restricted to group-homomorphic compatible lifts and supplies no actual real-image lower bound. The separate adverse CRT factor is recorded in Section 8. Source: [two-prime report and proofs](../2026-09-16-two-prime-character/README.md), Sections 2-7.

## 6. Unit-exponent / Følner cycle

> **ACTION GO / CARTESIAN FAIL.** The construction passes the actual-action and engineered-orbit return gates. Its proved coverage of the completed scalar square is too sparse.

### 6.1 Exact fractional multipliers and actual actions

**Mathematical statement - PROVED, UE-P1.** Fix $L\ge1$ before the depth $d$ grows. Recursively define

$$P_0=1,\quad t_i=3P_{i-1}^{2L+1},\quad q_i=t_i^2+t_i+1,
\quad P_i=P_{i-1}q_i,$$
$$\alpha_i=t_i-\omega,\quad u_i=\frac{\alpha_i}{\bar\alpha_i},\quad
\Gamma_d=\langle u_1,\ldots,u_d\rangle.$$

The $q_i$ are pairwise coprime norm blocks, not necessarily primes. The $u_i$ are fractional norm-one elements, or units after inverting the relevant primes; they are **not** an infinite collection of integral units in $\mathbb Z[\omega]$.

The sequence is multiplicatively independent, even modulo roots of unity. Therefore

$$U_d(h)=\{\textstyle\prod_i u_i^{f_i}:|f_i|\le h\},\qquad
|U_d(h)|=(2h+1)^d.$$

In the primary choice $L=h=1$, there are exactly $3^d$ actual norm-preserving real actions.

**Retained proof mechanism.** Since $q_i\equiv1\pmod{3P_{i-1}}$, the norm supports are disjoint and avoid 3. The conjugate factors $\alpha_i,\bar\alpha_i$ are coprime: a common factor would divide $\omega-\bar\omega$, of norm 3. In the norm-Euclidean ring $\mathbb Z[\omega]$, a factor $\pi_i\mid\alpha_i$ satisfies

$$v_{\pi_i}(u_i)>0,\qquad v_{\pi_i}(u_j)=0\quad(j\ne i).$$

Applying these valuations to a relation proves independence. Every root of unity has all these valuations zero. The retained proof supplies the Euclidean and factorization details; no prime-density or tower theorem is required.

**What it means.** Each exponent vector represents a different multiplier in a fixed quadratic field, and these act distinctly at every nonzero point. The bounded 18-action obstruction is absent.

**Why it matters.** Exponential actual action growth is achievable. It does not yet say that independently chosen scalar coordinates remain in the carrier after the action.

### 6.2 Exact orbit returns, including the boundary

**Mathematical statement - PROVED, UE-P2.** With seed 1, put

$$Z_d(L)=\{z_e=\textstyle\prod_i u_i^{e_i}:|e_i|\le L\}.$$

All its points have norm 1. Independence gives

$$u^fz_e\in Z_d(L)\quad\Longleftrightarrow\quad e+f\in[-L,L]^d.$$

Consequently

$$R_Z(z_e)=\prod_{i=1}^d
\bigl(1+\min(h,L-e_i)+\min(h,L+e_i)\bigr).$$

For $L=h=1$, let $k$ be the number of zero coordinates of $e$. Then

$$R_Z(z_e)=2^{d-k}3^k,\qquad
\#\{e:\text{$k$ zero coordinates}\}=\binom dk2^{d-k}.$$

In particular,

$$\min R_Z=2^d,\quad\max R_Z=3^d,\quad
\operatorname{mean}R_Z=(7/3)^d,$$
$$\operatorname{geommean}R_Z=e^{\mu d},\qquad
\boxed{\mu=\frac{2\log2+\log3}{3}}.$$

There are no exceptions at threshold $2^d$. Under uniform orbit counting, $k$ has the binomial law with parameter $1/3$, so $d^{-1}\log R_Z\to\mu$ in probability. More explicitly, for fixed $0<p<1/3$, set

$$r_p=\log2+p\log(3/2),\qquad
\delta_p=p\log(3p)+(1-p)\log\frac{3(1-p)}2>0.$$

The retained exponential-moment proof gives

$$\#\{z\in Z_d:R_Z(z)<e^{r_pd}\}\le e^{(\log3-\delta_p)d}.$$

**What it means.** The exponent box behaves as an additive translation box: all coordinates return independently, and even its corners have exponential return multiplicity. Each counted return is a distinct actual equal-norm point, hence a distinct ordered coefficient pair.

**Why it matters.** The orbit return theorem is complete. Its population is $Z_d$, however, rather than the full square of a scalar coordinate set. The name “Følner cycle” refers to this exponent-translation architecture; with fixed width it does not assert overlap tending to one for every generator as $d$ grows.

### 6.3 Exact Cartesian coverage loss

**Mathematical statement - PROVED, UE-P3.** Write $z=x_z-\omega y_z$ and form

$$A_d^{\rm orb}=\{x_z:z\in Z_d\}\cup\{y_z:z\in Z_d\},\qquad
S_d=\{(x_z,y_z):z\in Z_d\}.$$

For seed 1, both coordinate maps are injective and their images are disjoint. For the primary choice $L=1$, put $M=3^d$. This gives

$$|A_d^{\rm orb}|=2M=n_d,\qquad |S_d|=M,$$
$$\boxed{\frac{|S_d|}{|(A_d^{\rm orb})^2|}
=\frac{M}{4M^2}=\frac1{4\cdot3^d}.}$$

The exact count follows from torsion exclusion. Equal first coordinates of distinct orbit points force $wz=-\omega^2$; equal second coordinates force $wz=-1$. Equality $x_z=y_w$ forces $wz=-\omega$ or $w/z=\omega^2$. None can hold in the torsion-free generated group.

**What it means.** The numerator counts the engineered paired coefficients. The denominator counts all ordered pairs obtained by choosing two elements of the common scalar set independently. Although every engineered pair has exponentially many genuine returns, the engineered orbit occupies an exponentially vanishing fraction of that square. Its complement has exactly $4M^2-M$ pairs without this certificate.

**Why it matters.** Charging that complement as exceptional gives exponent $2\log3$, with no positive exceptional-pair deficit. Even using the fact that the engineered shell has one output gives only

$$|Q(A_d^{\rm orb},A_d^{\rm orb})|\le n_d^2-3^d+1.$$

This bound has quadratic exponent. It is not asserted sharp, and it is not an image lower bound. The actual image rate and additional cross-pair returns are **OPEN**.

The retained extension to $k$ seed norm values is also precise:

$$\#\{(x,y)\in A^2:Q(x,y)\in\mathcal C\}\le2k|A|,
\qquad |\mathcal C|=k.$$

For fixed $x$ and a norm value, a quadratic equation has at most two real solutions for $y$. Thus $k_d=e^{o(d)}$ shells still occupy at most $e^{-ad+o(d)}$ of a square with $|A_d|=e^{ad+o(d)}$, $a>0$. Here $k_d$ counts **norm values**, not arbitrary carrier states. General multistate Cartesianization is not excluded. Sources: [primary proof](../2026-09-16-unit-exponent/primary-proof.md), Sections 1-3.

## 7. Secondary Cartesian family

### 7.1 Identity-only return theorem

**Mathematical statement - PROVED, UE-S1.** Use the same fixed $L$ and recursive norm blocks, and define

$$A_d^{\rm val}=\{\sigma\textstyle\prod_{i=1}^d q_i^{e_i}:
\sigma\in\{\pm1\},\ |e_i|\le L\}.$$

Its scalar parameters are injective, so $n_d=2(2L+1)^d$. For all $h\in\mathbb Z^d$,

$$u^h(x-\omega y)=x'-\omega y',\quad
(x,y),(x',y')\in(A_d^{\rm val})^2
\quad\Longrightarrow\quad h=0.$$

Thus every pair has exactly one return under the entire selected group. The set contains no zero, and there are no exceptional pairs or nontrivial stabilizers.

**Retained proof mechanism.** For exponent vectors $e,f$, put $m_i=\min(e_i,f_i)$ and $S=\prod q_i^{m_i}$. Then $X=x/S,Y=y/S$ are integers. Define, for a positive rational $T$,

$$w_i(T)=\min_{p\mid q_i}\left\lfloor\frac{v_p(T)}{v_p(q_i)}\right\rfloor.$$

The source proves $w_i(Q(x,y))=2m_i$. At unequal exponents the residual norm is a unit at every prime in the block. At equal exponents, later blocks reduce to 1 modulo $q_i$, while earlier coordinates give

$$0<Q(X_0,Y_0)\le3P_{i-1}^{4L}<q_i.$$

Hence some $p\mid q_i$, with $k=v_p(q_i)$, has $v_p(Q(X,Y))<k$. Norm preservation fixes the minima at the target, so its coordinates also become integral after division by the same $S$. Orient the split factors $p=\pi\bar\pi$ toward $\alpha_i$. The two valuations of $X-\omega Y$ satisfy

$$A,B\ge0,\quad A+B<k,$$

whereas multiplication by $u_i^{h_i}$ gives $A+kh_i,B-kh_i$. Either sign of a nonzero integer $h_i$ makes one negative, contradicting target integrality. Other generators have zero valuation at these factors. This argument handles composite blocks and all negative powers.

**What it means.** Moving from paired orbit coordinates to a genuine full scalar valuation box destroys the returning-action mechanism. Disjoint norm blocks provide independent actions, but the scalar denominator constraints cannot absorb any nonzero action exponent.

**Why it matters.** Every pair fails every growing return threshold. There is no small bad set to discard. This conclusion concerns this explicit sparse multiplicative family, not all valuation carriers or all rational sets.

### 7.2 Independent full-image theorem and signed rate

**Mathematical statement - PROVED, UE-S2.** Put $M=(2L+1)^d$ and $n_d=2M$. Then

$$\boxed{|Q(A_d^{\rm val},A_d^{\rm val})|=M^2+M
=\frac{n_d^2}{4}+\frac{n_d}{2}.}$$

Exactly $M(M-1)$ outputs have four ordered representations and $2M$ outputs have two. The identifications are coordinate exchange and simultaneous sign reversal.

The retained proof is independent of the return theorem. The inequality $q_i>6P_{i-1}^{4L}$ makes specialization faithful for integer polynomials of coordinate degree at most $4L$ and coefficient absolute sum at most 6. Clearing denominators in equality of two $Q$-values produces such a six-term relation. Its formal support

$$T^{2E}+\sigma\tau T^{E+F}+T^{2F}$$

recovers the unordered endpoints and relative sign when $E\ne F$; for $E=F$ it gives $3T^{2E}$ or $T^{2E}$. This yields all fibers and all outputs.

**What it means.** A small action orbit does not imply a small polynomial fiber, so the actual image formula requires this separate argument. Here that argument establishes only constant-factor compression.

**Why it matters.** For $L=1$,

$$n_d=e^{ad+O(1)},\quad |Q(A_d^{\rm val},A_d^{\rm val})|=e^{bd+O(1)},$$
$$a=\log3,\qquad b=2\log3,\qquad\boxed{2a-b=0}.$$

Every fixed $c>0$ fails once $n_d^c>4$. This settles the actual rate for the **secondary family only**. Source: [secondary proof](../2026-09-16-unit-exponent/secondary-proof.md), Sections 1-6.

## 8. Mechanism audit and arithmetic ledger

### Mathematical statement: the logical gates

$$\boxed{\text{units}\longrightarrow\text{distinct real actions}
\longrightarrow\text{Cartesian returns}\longrightarrow Q\text{-fibers}
\longrightarrow\text{power saving}}$$

| Gate | Frozen status and precise interpretation |
|---|---|
| Fractional units to distinct real actions | **PROVED**, UE-P1: $3^d$ independent actual actions. |
| Actions to high returns on the engineered orbit | **PROVED**, UE-P2: at least $2^d$ at every orbit point. |
| Engineered orbit to dense Cartesian returns | **FAILED IN TESTED SCOPE**, UE-P3: direct coefficient completion has engineered density $1/(4\cdot3^d)$. Incidental returns are OPEN. |
| Genuine returns to polynomial fibers | **PROVED** by exact norm preservation and distinctness of returned pairs. |
| Almost-full rich fibers to a support saving | **PROVED implication**, HR-1; **OPEN application**, because the required full-square premise is absent. |
| Secondary full-square carrier | **FAILED** by UE-S1; separately UE-S2 proves its quadratic image rate. |

### What it means: signed rate accounting

The following rates use the fixed primary width $L=h=1$.

| Item | Primary orbit completion | Secondary valuation family |
|---|---|---|
| Input exponent $a$ | $\log3$ | $\log3$ |
| Total action exponent | $\log3$ | $\log3$ in width-one box |
| Proved return exponent | At least $\log2$, typical $\mu$, only on $S_d$ | Zero on every pair, even under $\Gamma_d$ |
| Action/projection loss | Zero off the origin; exact coordinate injections | Zero; injective scalar parameters |
| Uncontrolled/bad-pair count | $n_d^2-3^d$ for the orbit certificate | $n_d^2$ for any growing threshold |
| Available output exponent | $2\log3$ for this certificate; actual rate OPEN | $2\log3$ actual |
| Strict positive signed gap | None established | Zero, proved |

### Why it matters: all arithmetic costs remain visible

The action field is fixed: degree 2, discriminant $-3$, root discriminant $\sqrt3$, with the specified injective complex embedding. Both scalar sets are rational. The source supplies norm-Euclidean factorization; it uses no tower, class-number growth, regulator estimate or density-of-primes theorem. No ideal-index saving or unproved uniform residue population is credited.

Common denominators of the two scalar carriers divide $P_d^L$; actions in $U_d(h)$ have common denominator dividing $P_d^h$. The recurrence gives

$$9P_{i-1}^{4L+3}\le P_i\le13P_{i-1}^{4L+3},\qquad
\log P_d=\Theta_L((4L+3)^d).$$

For $L=1$ this is $\Theta(7^d)$, so cleared heights are not polynomial in $n_d$. Primary scalar coordinates have absolute value at most $2/\sqrt3$; secondary scalars have maximum $P_d^L$ and outputs at most $3P_d^{2L}$. Multipliers preserve the $Q$ metric exactly. Prime 3 is excluded; composite-block multiplicities are retained in every valuation argument.

For the earlier two-prime certificate, the normalized CRT factor is

$$\left(\frac{133\cdot130}{54^2}\right)^d=\left(\frac{8645}{1458}\right)^d>1.$$

This charges the input density in both coordinates. It is a separate adverse certificate from the 18-action collapse, not an additional loss to count twice. Neither is an actual real-image lower bound.

There is no uncharged input thinning, scalar fiber, sign branch or state count. The primary loss is completion to the **entire square**, and the secondary loss is an exact integrality obstruction followed by an independent image count. Large denominators are accounted for, not asserted to be a universal reason for failure.

## 9. Failure registry: exact scopes

In this section $\operatorname{coord}(Z)$ is the union of both scalar coordinate projections. Put $P=\{-1,0,1\}$ and $T=T_{(8+5\omega)/7}$. Each entry concerns its displayed architecture only.

| Architecture and exact hypothesis | Proved obstruction | Not ruled out |
|---|---|---|
| Common-scaled interval $D^{-1}([-N,N]\cap\mathbb Z)$, $D>0$ | **FAILED actual carrier:** inherited polynomial-height image obstruction after common scaling | Arbitrary rational height or varying-field carriers |
| Dense one-prime $A_{H,L,p}$ of Section 4 | **FAILED actual carrier:** HR-4 bounds fibers by $C_\eta H^\eta$, uniformly in depths and prime | Several denominator primes; other sparse alphabets |
| Fixed finite nonzero $p$-free integer alphabet $B$, finite nonempty $S\subseteq\mathbb Z_{\ge0}$, scalars $\{bp^{-k}:b\in B,k\in S\}$ | **FAILED actual carrier:** HR-3 gives uniformly bounded fibers depending on $p,B$, for finite depth sets $S$ | Growing alphabets outside that theorem |
| $Z_J=\bigcup_{\lvert k\rvert\le J}T^k(P^2)$, $A_J=\operatorname{coord}(Z_J)$ | **FAILED cyclic-return certificate:** HR-6 gives sum of full cyclic return counts at most $145n^2$, over nonzero pairs | Other seeds/actions; actual image coincidences beyond the certificate |
| $C_J=\operatorname{coord}\{T^k(1,0):\lvert k\rvert\le J\}$, $A_J=P+C_J$ | **FAILED cyclic-return certificate:** HR-8 gives the corresponding nonzero-pair sum at most $49n^2$ | Other correlated translates or growing component populations |
| $A_0=P$; $A_{j+1}=A_j\cup\operatorname{coord}(T(A_j^2))\cup\operatorname{coord}(T^{-1}(A_j^2))$ | **FAILED actual carrier:** HR-5, cleared height at most $13^j$, input at least $2^{j+1}+1$, and logarithmic cyclic returns at every nonzero pair | Closures with different input/height behavior |
| Full digit module $Z_{m,H}=\{\sum_{i=0}^{m-1}c_i\zeta_m^i:\lvert c_i\rvert\le H\}$, $3\mid m$, $H\ge1$; signed coefficient union over the real subfield | **FAILED supplied-action certificate:** HR-7, $n\ge(2H+1)^{\varphi(m)/2}$ but only $m$ torsion actions; effective exponent tends to zero | Sparse codes, different actions; no image lower bound follows here |
| HR-N1's exact rational $7,19$ carrier and generators | **FAILED / DISPROVED:** at least $n_L^2/200$ identity-only pairs for $L=10m,m\ge2$, all integer powers | Actual image rate, other actions, ARG/TCRC/RC15/4 |
| Equal-character $D^d$, homomorphic equivariant norm-one real realization | **FAILED realization certificate:** at most 18 actual actions | Nonhomomorphic lifts with independently proved returns |
| Direct coefficients of the unit orbit; or certificates on $e^{o(d)}$ norm shells | **FAILED coverage certificate:** density $1/(4\cdot3^d)$; general shell bound $2k/n$ | Incidental cross-pair returns, arbitrary states, new Cartesianization |
| Exact separated norm-block scalar family $A_d^{\rm val}$ | **FAILED actual family:** UE-S1 identity-only; independently UE-S2 image $n^2/4+n/2$ | Other norm blocks, valuation sets, or arbitrary real sets |

The mean-return bounds imply that at most $145n^2/M$ or $49n^2/M$ pairs, respectively, can have $M$ distinct cyclic returns (among nonzero pairs). For polynomially growing $M$, the exceptional complement has order $n^2$. Those are action-certificate obstructions; they do not turn into actual image lower bounds without a separate argument.

The early exact diagnostic tested 18 finite cases, all with median return 1. This is **EXPERIMENTAL** corroboration over its recorded range, not a universal theorem. The earlier independent-radical family also has separately proved formulas recorded in Section 10. No failed-family statement here disproves the ultimate $Q$ target.

## 10. Relation to C0 and the affine benchmark $Q+x$

### Mathematical statement - retained same-set transfer

Let $P_0(x,y)=Q(x,y)+x$. The exact translation identity is

$$P_0(x,y)=Q(x+2/3,y-1/3)-1/3.$$

The translations differ by 1, so a rectangular identity alone does not solve the same-set problem. The accepted transfer theorem states: suppose a growing family $C\subset\mathbb R$, $|C|=N\ge2$, satisfies, for fixed constants $K,D>0$ and exponents $0<c_0\le1$, $0\le\eta<c_0/2$,

$$|Q(C,C)|\le K N^{2-c_0},\qquad |C-C|\le D N^{1+\eta}.$$

Then one obtains a common scalar input set $B$, with $|B|\ge N^{1-\eta}/(2D)$, for which

$$|P_0(B,B)|\le K(2D)^{2-c_1}|B|^{2-c_1},\qquad
\boxed{c_1=\frac{c_0-2\eta}{1-\eta}>0}.$$

This is a **PROVED implication**, with **OPEN premises** for a suitable construction in this branch. The explicit constant must be retained; a coefficient-free eventual bound follows for every fixed exponent strictly below $c_1$.

**Retained mechanism.** A difference $t\ne0$ has at least $N^{1-\eta}/(2D)$ representations $a,a+t\in C$. Scale $C$ by $1/t$ and choose the common set $B$ so that both $B+2/3$ and $B-1/3$ lie in $C/t$. The displayed identity then transports every ordered pair of $B^2$ into $Q(C/t,C/t)$.

### What it means

A useful future homogeneous carrier would ideally combine **high Cartesian returns** with a small additive difference set. The completed norm program does not yet supply the first requirement on almost all pairs, so it supplies no affine saving through this theorem. The transfer is not invalidated by the failed carriers.

C0's rank-one square-residue mechanism remains proved under its corrected hypotheses. The attempted conceptual extension was

$$\begin{array}{ccc}
L^2+M&\longrightarrow&\text{sparse square residues}\\
Q=N(x-\omega y)&\longrightarrow&\text{many Cartesian norm representations}.
\end{array}$$

The first row has a completed construction in the source system; the second has no completed fixed power-saving carrier.

### Why it matters

The simple independent-radical family is already closed. For distinct primes $p_i$ and

$$A_m=\{\textstyle\sum_{i=1}^m\varepsilon_i\sqrt{p_i}:
\varepsilon_i\in\{\pm1\}\},\qquad n=2^m,$$

the retained proof gives

$$|Q(A_m,A_m)|=n^2/4+n/2,\qquad |P_0(A_m,A_m)|=n^2.$$

Growing multiquadratic degree alone therefore does not repair this family. Its failure does not close the affine benchmark or the general full-rank affine quadratic problem with fixed rational coefficients. Sources: [sign-cube proof](../2026-09-16-solvable-norm-trace/sign-cube.md), and the T01 transfer checkpoint in Appendix C.

## 11. Open frontier and next obligation

> **The missing norm-symmetry bridge is dense Cartesian realization of a high-return norm orbit.** No such growing family has been constructed in this program.

The homogeneous full-rank target, general Cartesian-compatible norm carriers, fundamentally different Cartesianization principles, $Q+x$, and general full-rank affine quadratics with fixed rational coefficients remain **OPEN**. The primary unit-orbit scalar image rate and the earlier HR-N1 carrier's actual image rate remain **OPEN**. Adaptive radical growth (ARG), eventual TCRC and RC15/4 retain their **OPEN** status.

The strategic decision is to freeze this carrier search. Another prime pair, character table, unit box, routine orbit thickening or simple denominator stratification is not adopted as a next task. Revival requires a genuinely new Cartesianization principle and a separate authorized research cycle. This report proposes none.

### Mathematical statement - OPEN, T03-O4 / RC15/4

Let $\mathcal A_m$ be the **actual adaptive levels** of T03, with

$$n_m=2^{m+1},\quad s_m=|Q(\mathcal A_m,\mathcal A_m)|,\quad
F_m=\mathbb Q(\mathcal A_m),\quad M_m=\max_{a\in\mathcal A_m}|a|.$$

These levels start from $\mathcal A_0=\{\pm1\}$ and use the retained exact optimizer and tie rule for the lift

$$\mathcal L_C(A)=\{\pm\sqrt{(C+a)/(C-M)}:a\in A\},\quad C>M.$$

RC15/4 asks for fixed $H<\infty,m_0$ and explicit choices for **every** actual $m\ge m_0$ such that

$$C_m^\dagger\in F_m,\quad C_m^\dagger>M_m,\quad
B_m\subseteq\mathcal A_m,\quad n_m-|B_m|\le H\sqrt{n_m},$$
$$C_m^\dagger+a=\gamma_m u_a^2\quad(a\in B_m),\qquad
\gamma_m,u_a\in F_m\text{ positive},$$
$$U_m=\{\pm u_a:a\in B_m\},\qquad
\boxed{|\gamma_mQ(U_m,U_m)|\le\frac{15}{4}s_m+Hn_m^{3/2}.}$$

Both root signs, the scaling factor, legal in-field parameter and exceptional-input count are part of the obligation. A large square class without this whole-image bound is insufficient.

### What it means

The source proves the **CONDITIONAL** consequence

$$s_{m+1}\le\frac{15}{4}s_m+4Hn_m^{3/2},\qquad
s_m=O((15/4)^m).$$

Since $15/4<4$, while doubling input size multiplies the pair budget by 4, every fixed $0<c<\log_2(16/15)$ would then give an eventual saving. This is not a completed construction.

### Why it matters

The requested root-image compression is a direct support bound with a precise exception budget. HR-N1 was one proposed source of compression, not a proved bridge to these adaptive root sets. Its failure, and the later norm-carrier failures, supply no disproof of RC15/4. **This exact existing statement is the one retained next mathematical obligation; no proof is attempted here.** Source: T03 current state Sections 7, 13-14 and [current T03 status](../../tracks/03-eisenstein-cartesianization/STATUS.md).

## 12. Final frozen state

```yaml
thread: T03
checkpoint_id: CNS-FREEZE-20260920
version: 1
research_completed: "2026-09-16"
documentation_date: "2026-09-20"
mode: DOCUMENTATION_FREEZE
network_policy: STRICTLY_OFFLINE
verdict: "ACTION GO / CARTESIAN FAIL"
scope: "the explicitly defined architectures and certificates"
return_framework:
  ordering: "R_label >= R_action >= R_pair"
  full_support_implication: PROVED
two_prime_character:
  verdict: "LOCAL GO / GLOBAL FAIL"
  local_carrier_size: 54
  local_pair_count: 2916
  local_return_range: [8, 54]
  product_minimum_returns: "8^d"
  below_18_power_exception_bound: "2772^d"
  compatible_real_action_bound: 18
  realization_scope: "group-homomorphic and equivariant"
unit_exponent_primary:
  actual_actions: "3^d"
  engineered_orbit_size: "3^d"
  minimum_orbit_returns: "2^d"
  typical_log_return_rate: "(2 log 2 + log 3)/3"
  scalar_carrier_size: "2*3^d"
  engineered_pair_density: "1/(4*3^d)"
  engineered_coverage_certificate: FAILED
  incidental_cross_pair_returns: OPEN
  actual_asymptotic_image_rate: OPEN
unit_exponent_secondary:
  return_count_every_pair: 1
  action_scope: "all integer powers of the selected generators"
  exact_image_size: "n_d^2/4 + n_d/2"
  image_theorem_independent_of_return_theorem: true
  input_exponent: "log 3"
  output_exponent: "2 log 3"
  signed_gap: 0
hr_n1:
  status: "FAILED / DISPROVED"
  tail_certificate: CLOSED
remaining_status:
  homogeneous_quadratic_target: OPEN
  general_cartesian_norm_carrier: OPEN
  general_cartesianization_principle: OPEN
  affine_Q_plus_x: OPEN
  general_full_rank_affine_quadratic_rational_coefficients: OPEN
  ARG: OPEN
  TCRC: OPEN
  RC15_4: OPEN
research_decision:
  carrier_search: FROZEN
  revival_requires: "a new Cartesianization principle and authorization"
  replacement_conjecture_adopted: false
  only_next_obligation: "T03-O4 / RC15/4, unchanged"
this_freeze:
  new_mathematical_searches: 0
  research_experiments_or_reruns: 0
  new_independent_proof_audit: false
  external_review_or_novelty_claim: false
  commit_made: false
```

## Appendix A. Finite exact evidence

All data here are copied from completed reports and retained exact JSON. No mathematical experiment was rerun for this freeze. Finite observations and rounded summaries do not establish asymptotic results.

### Unit-exponent diagnostics: $L=h=1$, $d=1,2,3$

| Carrier | Depth | $n$ | Actual actions | Full image | Fraction $R_{\rm pair}=1$ |
|---|---:|---:|---:|---:|---|
| Primary orbit projection | 1 | 6 | 3 | 16 | $5/6$ |
| Primary orbit projection | 2 | 18 | 9 | 139 | $17/18$ |
| Primary orbit projection | 3 | 54 | 27 | 1264 | $53/54$ |
| Secondary valuation box | 1 | 6 | 3 | 12 | $1$ |
| Secondary valuation box | 2 | 18 | 9 | 90 | $1$ |
| Secondary valuation box | 3 | 54 | 27 | 756 | $1$ |

The full-square returned-pair distributions are:

| Carrier/depth | $R_{\rm pair}$ : number of ordered pairs |
|---|---|
| Primary 1 | $1:30,\ 2:4,\ 3:2$ |
| Primary 2 | $1:306,\ 4:8,\ 6:8,\ 9:2$ |
| Primary 3 | $1:2862,\ 8:16,\ 12:24,\ 18:12,\ 27:2$ |
| Secondary 1 | $1:36$ |
| Secondary 2 | $1:324$ |
| Secondary 3 | $1:2916$ |

Labels and actual actions agree. In each primary row their histogram replaces one occurrence of return 1 by one occurrence of return $3^d$, because every action fixes $(0,0)$. The finite stabilizer histogram is $1:n^2-1,\ 3^d:1$ in the primary and $1:n^2$ in the secondary.

Every full-square median and minimum is 1. Primary returned-pair geometric means are approximately 1.148033, 1.096402, 1.047092; the means are $11/9,101/81,887/729$. Secondary means and geometric means are all 1. The complete orbit distribution is the exact binomial formula in Section 6; it must not be substituted for these Cartesian distributions.

The independent $1,\sqrt{-3}$ oracle checked every labelled action and each norm against $((2x+y)^2+3y^2)/4$, using exact rational equality. Scalar parameter and tagged coefficient fibers are 1. All image-fiber histograms, action statistics and pair hashes are retained in [unit data](../../../examples/2026-09-16-unit-exponent.json) and the original raw companion.

### Earlier evidence and its limits

The high-return run contained 18 exact cases with median 1. Its largest recorded examples include the 72-element strata carrier with 1262 outputs and 5040 identity-only pairs among 5184; and the 83-element orbit box with 1642 outputs and 6744 identity-only nonzero pairs among 6888. The [complete early distributions](../2026-09-16-high-return/experiments.md) retain every case and threshold.

The two-prime one-block histogram in Section 5 is both analytically derived and corroborated exhaustively by an independent split-coordinate oracle. Its product statements are proofs, not product-sized enumerations. The six unit cases corroborate UE-P1-P3 and UE-S1-S2; no extrapolation of the primary finite identity-only fractions is adopted.

## Appendix B. Reproducibility, review and this documentation task

### Already completed cycle records

| Cycle | Recorded computation and validation |
|---|---|
| High-return | One 18-case run: 863,636 implementation-counter units; 0.468425 CPU seconds; zero errors. Original validation records 42 unit tests and 159 baseline checks passed. |
| HR-N1 | Charged evaluations 0; research-program CPU seconds 0. Analytic obstruction sufficed. Two independent internal reviews passed; no enumeration was needed. |
| Two-prime character | One fixed diagnostic: 653,787 charges; 0.691836 CPU seconds. 42 unit tests and 159 baseline checks passed. Combined cycle total 736,357 charges and 3.607404 CPU seconds. |
| Unit-exponent | One six-case diagnostic: 340,986 charges; 5.944325 CPU seconds. 52 unit tests and 159 baseline checks passed. Combined cycle total 431,118 charges and 8.910798 CPU seconds. |

The high-return record refines its diagnostic count to 864,040 when each matrix identity is charged separately, then adds a 100,000-unit upper allowance for validation, giving at most 964,040 total. That allowance is not measured usage. Its original cycle included one authorized check of an external cyclotomic degree/basis fact; this strictly offline freeze does not reopen that source or relabel the earlier cycle as wholly offline.

Counts and runtimes are historical provenance, not current rerun results. The two-prime and unit cycles used Python 3.12.7 and exact standard-library arithmetic. Their announced caps were 2,000,000 evaluations and 600 research/validation CPU seconds each. The recorded totals include conservatively charged regressions. The two-prime record includes a failed wrapper launch with six import calls and no mathematical run; the unit diagnostic had no failed run or rerun. No such program was executed during this freeze.

### Internal review provenance

The original unit cycle records lead inspection and independent cross-review of both complete proofs: independence, orbit boundary/tail, exact coefficient size and shell scope; and minimum valuations, composite blocks, negative powers, specialization and diagonal/sign cases. All passed. Its pre-execution code review required per-label oracle comparison in addition to aggregate returned sets; this was fixed before the sole diagnostic. A clarification of the binomial typical-rate argument changed no theorem. The final report/data consistency review passed. These are internal reviews, not external peer review.

The two-prime cycle retains separate reviews of the local sign/orbit calculation and product/realization proof. The HR-N1 freeze retains its two independent internal reviews. The present task reads and consolidates these records; it does not add a new independent proof-audit claim.

### This freeze: preservation and checks

The initial checkout was on `main`, with nine already modified tracked files and many existing untracked artifacts. Those inherited changes totaled 1153 insertions and 58 deletions. A 162-file hash baseline and the inherited diff were saved before authoring. Historical mathematical sources, experiments, data, manifests and SPECs are preserved. Only the new report package, PDF, local rendering/provenance files and dated navigation/status addenda belong to this task.

This freeze performs no new mathematical search, charged evaluation, research-program run or network access. PDF typesetting, rendering, source hashing and repository checks are document-production work. They are not mathematical experiments or proofs. No commit, staging, push, reset or remote change is performed. Deliverables remain uncommitted.

Current check results and the PDF page-inspection record are supplied in the companion [verification record](verification.md). Documentation checks use `python3 scripts/check_repository.py`, `python3 scripts/check_codex_setup.py` and `git diff --check`. Code tests are not rerun because no research code changes in this freeze. The reported 52 tests and 159 baseline checks belong to the completed unit cycle.

| Documentation check run in this freeze | Result |
|---|---|
| Repository integrity and local links | **PASS:** 39 archived sources; 80 Markdown files |
| Local source/setup integrity | **PASS:** 50 references; 43 T03 manifest members; no research code executed |
| Tracked whitespace check | **PASS** |
| PDF equation and internal-link validation | **PASS:** 350 math expressions; zero rendering errors or broken internal targets |

Every page is visually inspected before final handoff; the final page and preservation counts are recorded in the companion verification file. All changes remain uncommitted.

## Appendix C. Source register and authority

The branch chronology is high-return, then completed HR-N1 closure, then two-prime character, then **unit-exponent**, all dated 16 September 2026. The last is controlling for this branch's final verdict. File modification time does not determine mathematical authority. The new 20 September recovery intake has a 10 September mathematical cutoff and does not supersede these later cycles.

| Source | Exact role and retained locator |
|---|---|
| [High-return report](../2026-09-16-high-return/README.md) | HR-1 support theorem, HR-2-HR-8 scoped carrier results; original Section 7 HR-N1 proposal is historical. |
| [Return lemma](../2026-09-16-high-return/return-lemma.md) | HR-1(a),(a'): full support, chosen lifts, stabilizers, scalar fibers and exceptions. |
| [Denominator proof](../2026-09-16-high-return/denominator-obstruction.md) and [carrier screen](../2026-09-16-high-return/carrier-screen.md) | HR-3/4 actual-image theorems; exact HR-5/6/7/8 definitions and scopes. |
| [HR-N1 final freeze](../2026-09-16-hr-n1-final-freeze/README.md) | Controlling HN1-2/3 theorem, quantitative disproof, scope and two-review record; links completed proof and local-action companion. |
| [Two-prime report](../2026-09-16-two-prime-character/README.md) | TP-L1/P1/G1 and normalization; complete [local count](../2026-09-16-two-prime-character/local-count-proof.md), [product/realization](../2026-09-16-two-prime-character/product-realization.md), [verification](../2026-09-16-two-prime-character/verification.md). |
| [Unit-exponent report](../2026-09-16-unit-exponent/README.md) | Controlling final verdict and exact arithmetic/rate ledger; [primary proof](../2026-09-16-unit-exponent/primary-proof.md) UE-P1-P3; [secondary proof](../2026-09-16-unit-exponent/secondary-proof.md) UE-S1-S2; [verification](../2026-09-16-unit-exponent/verification.md). |
| [Solvable norm/trace report](../2026-09-16-solvable-norm-trace/README.md) | Earlier sign-cube theorem and the full-rank norm/trace context; no rerun or stronger inference here. |
| Corrected C0 source | `local-only/migration/research_supplement/shared/Phase_C0_Corrected.md`, Theorem C0.1, with `C0_CORRECTION_LOG.md`. Rank-one theorem only. |
| Affine transfer source | `local-only/migration/sources/T01_Norm_Trace_Quadratic_Research_Checkpoint.md`, Section 2.3, equation (2.6); exact constant and exponent. |
| T03 final state | `local-only/migration/sources/T03_CURRENT_STATE.md`, Sections 7, 13-14; identical current-state member in `T03_RESEARCH_RECORD_20260910.zip`. The five retained TCRC companions govern the preceding root-cycle results. |
| Current navigation | [Project map](../../CURRENT_PROJECT_MAP.md), [T03 status](../../tracks/03-eisenstein-cartesianization/STATUS.md), [open lemmas](../../OPEN_LEMMAS.md), [failure registry](../../FAILURE_LIBRARY.md), [migration conflicts](../../MIGRATION_CONFLICTS.md). |

All research sources above retain their original bytes. The original manifests identify proof, code and exact-data versions by hash; this freeze's companion manifest identifies the report, PDF and consulted source identities. The recovered 20 September addendum reports further F25/arithmetic originals, but those original bytes were not supplied in that intake. No claim here depends on them, and they are not described as inspected.

**Final handoff:** the specified norm-symmetry searches are frozen; the general target remains **OPEN**; **T03-O4 / RC15/4** is the only retained next constructive obligation.
