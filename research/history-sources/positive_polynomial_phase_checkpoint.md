# Positive Polynomial Phase

## The fixed cubic remains open; a non-special higher-degree family is proved

**Offline research checkpoint.** No internet search or external retrieval was used. The supplied reports and the frozen results in the research prompt were treated as primary input. In particular, the earlier prime, prime-power, singular-scaling, and residual-critical branches were not re-opened.

The entropy test used throughout is the following. If

$$
|A_d|=e^{ad+o(d)},
\qquad
|P(A_d,A_d)|\le e^{bd+o(d)},
$$

then a fixed power saving is obtained exactly when $b<2a$, in which case

$$
c=2-\frac ba>0.
$$

## A. Fixed polynomial conjecture

Let

$$
P_3(x,y)=(x-y)^3-3(x+y).
$$

The Cubic Polynomial Small-Image Conjecture (CPSI) asks whether there are a constant $c_3>0$ and arbitrarily large finite $A\subset\mathbb R$ such that

$$
|P_3(A,A)|\le |A|^{2-c_3}.
$$

### Verdict for this checkpoint

CPSI is not proved or disproved here. No construction examined in this cycle gives $b<2a$. The strongest unconditional positive result is instead the following explicit companion theorem.

### Main unconditional theorem

Let

$$
R(x,y)=5(x+y)+(x-y)^2,
$$

and assume the frozen theorem supplying a constant $c_0>0$ and arbitrarily large finite sets $A_n\subset\mathbb R$ for which

$$
|R(A_n,A_n)|\le |A_n|^{2-c_0}.
$$

For every nonconstant $\Phi\in\mathbb R[t]$, every $a\in\mathbb R\setminus\{0\}$, and every $b\in\mathbb R$, define

$$
Q_{\Phi,a,b}(x,y)
=\Phi\bigl(R(ax+b,ay+b)\bigr).
$$

Then there are arbitrarily large finite $A'_n\subset\mathbb R$ satisfying

$$
|Q_{\Phi,a,b}(A'_n,A'_n)|
\le |A'_n|^{2-c_0}.
$$

Moreover, every such $Q_{\Phi,a,b}$ lies outside both polynomial forms

$$
F(g(x)+h(y)),
\qquad
F(g(x)h(y)),
$$

when $g$ and $h$ are required to be nonconstant univariate polynomials. In particular,

$$
P_4(x,y)=R(x,y)^2+R(x,y)
$$

is an explicit degree-four, non-special polynomial with a fixed power-saving construction.

## B. Non-special verification for the cubic

We first record a differential obstruction that will also handle the companion family.

### Lemma B.1: derivative-ratio obstruction

Let $Q\in\mathbb R[x,y]$ have nonzero partial derivatives. If

$$
Q(x,y)=F(g(x)+h(y))
$$

or

$$
Q(x,y)=F(g(x)h(y)),
$$

where $F$ is nonconstant and both $g,h$ are nonconstant univariate polynomials, then the rational function $Q_x/Q_y$ is multiplicatively separable:

$$
\frac{Q_x}{Q_y}=A(x)B(y)
$$

for some nonzero rational functions $A,B$.

Indeed, the two cases give respectively

$$
\frac{Q_x}{Q_y}=\frac{g'(x)}{h'(y)}
$$

and

$$
\frac{Q_x}{Q_y}
=\frac{g'(x)h(y)}{g(x)h'(y)}.
$$

A nonconstant rational function $\rho(x-y)$ cannot have the form $A(x)B(y)$. To see this, take the logarithmic derivative in $x$ and then differentiate in $y$. One obtains

$$
\left(\frac{\rho'}{\rho}\right)'=0.
$$

Thus $\rho'/\rho$ is constant. At infinity the logarithmic derivative of a nonzero rational function is $O(1/t)$, so that constant is zero and $\rho$ itself is constant, a contradiction.

For $u=x-y$,

$$
(P_3)_x=3(u^2-1),
\qquad
(P_3)_y=-3(u^2+1),
$$

and hence

$$
\frac{(P_3)_x}{(P_3)_y}
=\frac{1-u^2}{1+u^2}.
$$

This is a nonconstant rational function of $x-y$. Lemma B.1 proves that $P_3$ is in neither special form.

There is also a short degree check. In the additive case, $\deg_xP_3=\deg_yP_3=3$ forces either a linear outer polynomial, which cannot create the mixed cubic terms, or a cubic outer polynomial with linear $g,h$. The leading form then forces $g+h$ to be proportional to $x-y$, contradicting the term $-3(x+y)$. In the multiplicative case, writing $d=\deg F$, $e=\deg g$, and $f=\deg h$ gives $de=df=3$, while the total degree would be $d(e+f)=6$, not $3$.

## C. Results of the parallel mechanisms

The mechanisms were attacked independently and then audited against the full Cartesian requirement.

- **Algebraic identity, norm, and trace.** The polynomial is a coordinate and has exact Chebyshev, determinant, trace-cube, and varying-norm identities. No fixed nontrivial polynomial field-norm representation exists. Every identity found retains a pair label carrying quadratic entropy.
- **Unit-distance and number fields.** A genuine same-set norm-one trace construction gives an exponentially bounded full image, but its certified output base exceeds the squared input base by more than $128D^2$ per degree.
- **Direct sum-product insertion.** Substitution into the frozen $A=GP$ set gives a natural monomial-coordinate code with exactly $|G|^2|P|^2=|A|^2$ labels. The archimedean box is worse.
- **High-dimensional digits.** Transcendental digit strings are asymptotically pair-injective, while good reduction modulo $3$ gives exact injectivity. These real models have $b=2a$.
- **Formal tensor models.** Square-zero and split product algebras have a genuine coordinatewise gap, but they do not embed faithfully as scalar subalgebras of $\mathbb R$.
- **Structured computation.** Nilpotent truncations show apparent compression; every tested honest real or field lift restores near-injectivity. This is hypothesis generation only.
- **Adversarial audit.** Same-set use, cross-pairs, denominators, embeddings, and rate comparisons were checked independently. No cubic claim survives with $b<2a$; the companion theorem does.

The central exact identity emerging from the algebraic branch is more useful than any of the cosmetic rewrites. Put

$$
H_3(u)=u^3-3u,
\qquad
A_u=A\cap(A-u)=\{y\in A:y+u\in A\}.
$$

Then

$$
\boxed{
P_3(A,A)
=\bigcup_{u\in A-A}\bigl(H_3(u)-6A_u\bigr).
}
\tag{C.1}
$$

Every slice has cardinality $|A_u|$, and

$$
\sum_{u\in A-A}|A_u|=|A|^2.
\tag{C.2}
$$

Thus a power saving must come from polynomially large overlap between different difference-slices. A collision between the $u$- and $u'$-slices is exactly

$$
6(y-y')
=(u-u')(u^2+uu'+u'^2-3),
\tag{C.3}
$$

where $y\in A_u$ and $y'\in A_{u'}$. This is the precise global correlation missing from the mechanisms tested below.

## D. Best new constructive mechanism

No valid scalar-real construction for $P_3$ was found. The best conceptual gain is visible in finite tensor algebras, and its failure under real realization identifies the missing information exactly.

Let

$$
\mathcal D_d=\mathbb Q\oplus V,
\qquad V^2=0,
$$

where $V$ has basis $\varepsilon_1,\ldots,\varepsilon_d$, and take

$$
\mathcal A_d
=\left\{\sum_{i=1}^d a_i\varepsilon_i:a_i\in\{0,1\}\right\}.
$$

Then $x^3=0$ for $x\in V$, so

$$
P_3(x,y)=-3(x+y).
$$

Consequently

$$
|\mathcal A_d|=2^d,
\qquad
|P_3(\mathcal A_d,\mathcal A_d)|=3^d,
$$

and the formal exponent is

$$
c_{\mathrm{formal}}=2-\log_2 3>0.
$$

Likewise, in the split algebra $\mathbb R^d$, the alphabet $\Sigma=\{0,1,2,3\}$ has

$$
|P_3(\Sigma,\Sigma)|=14<16,
$$

which tensorizes to $14^d<16^d$.

These are not constructions in the problem. A subring of $\mathbb R$ is an integral domain, so it has neither a nonzero nilpotent nor a nontrivial idempotent. Thus neither tensor algebra admits a faithful algebra embedding into scalar reals.

The obstruction is sharper than that slogan. In a transcendental lift, with $x=T^kf$ and $y=T^kg$,

$$
P_3(x,y)
=-3T^k(f+g)+T^{3k}(f-g)^3.
\tag{D.1}
$$

When a truncation discards all degrees at least $d$ and $3k\ge d$, the second term disappears and creates the formal gain. Before truncation, the linear and cubic degree supports are disjoint. Equality of two outputs recovers $f+g$ and $(f-g)^3$ separately, hence recovers $f-g$ over a real domain and therefore recovers the ordered pair. The deleted cubic tail contains exactly the entropy that the nilpotent model appeared to save.

Specially tailored, highly $3$-ramified real number fields remain logically open; they were not ruled out by this argument.

## E. Full quantitative analysis of the cubic mechanisms

### E.1 Polynomial-coordinate and fixed-norm audit

With

$$
u=x-y,
\qquad z=P_3(x,y),
$$

the map $(x,y)\mapsto(u,z)$ is a polynomial automorphism with constant Jacobian $-6$ and inverse

$$
x=\frac{u^3+3u-z}{6},
\qquad
y=\frac{u^3-3u-z}{6}.
\tag{E.1}
$$

Hence the labelled sets

$$
\{(x-y,P_3(x,y)):x,y\in A\}
$$

and

$$
\{(x+y,P_3(x,y)):x,y\in A\}
$$

both have exactly $|A|^2$ elements. The second assertion follows because $u$ is the unique real cube root of $P_3+3(x+y)$.

There are exact identities

$$
H_3(w+w^{-1})=w^3+w^{-3},
$$

$$
P_3=\det
\begin{pmatrix}
u&0&-3v\\
1&u&0\\
0&1&u
\end{pmatrix},
\qquad v=x+y,
$$

and

$$
P_3=\operatorname{Res}_T(T-u,T^3-3v).
$$

The last is a norm in the algebra $L[T]/(T^3-3v)$, but this algebra varies with the pair through $v$. Retaining $v$ restores all $|A|^2$ labels.

There is no replacement by a polynomial norm from one fixed nontrivial field extension. Precisely, let $K/L$ be a nontrivial finite separable extension in characteristic zero. There are no nonconstant $\psi\in K[x,y]$ and $F\in L[t]$ with

$$
P_3=F(N_{K/L}(\psi)).
$$

Over an algebraic closure, $P_3=u^3-3v$ is irreducible because it is linear in $v$ with unit leading coefficient. If $\deg F>1$, splitting $F$ factors the right side. If $F$ is linear, then a translate $P_3-b$ would equal a product of the at least two nonconstant conjugates of $\psi$, again contradicting irreducibility. Degree comparison also shows that a direct norm identity could never use growing extension degree: $[K:L]\deg\psi\le3$.

This proposition is deliberately scoped to polynomial $\psi$ in a fixed field extension. It does not exclude rational parametrizations, a family of algebras varying with $(x,y)$, or a genuinely new combination of norm and trace.

Two natural identity-driven sets are maximally bad:

- If $T>1$ is transcendental and $A_n=\{T^i+T^{-i}:1\le i\le n\}$, the two largest Laurent exponents of each off-diagonal output recover the ordered pair, so $|P_3(A_n,A_n)|=n^2$.
- If $A_n=\{a+\delta i:0\le i<n\}$ and $\delta^2\notin\mathbb Q$, equality of two outputs gives $\delta^2(d^3-d'^3)=3(s-s')$ for integer differences and sums. Irrationality recovers $d,s$, hence the ordered pair. Again the image has size $n^2$.

A natural growing Galois orbit also fails exactly. In

$$
K=\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_d}),
$$

for distinct positive primes $p_i$, take

$$
A=\left\{\alpha_\varepsilon=\sum_i\varepsilon_i\sqrt{p_i}:
\varepsilon_i\in\{-1,1\}\right\}.
$$

The squarefree radical monomials are a $\mathbb Q$-basis, so $|A|=2^d$. For a pair $(\varepsilon,\eta)$ let $D=\{i:\varepsilon_i\ne\eta_i\}$. In the output, the coefficient of the singleton basis vector $\sqrt{p_i}$ is

$$
-6\varepsilon_i\quad(i\notin D),
$$

and

$$
8\varepsilon_i\left(3\sum_{j\in D}p_j-2p_i\right)\quad(i\in D).
$$

The first has magnitude $6$ and the second has magnitude at least $16$. The output therefore recovers $D$, then every $\varepsilon_i$, and finally $\eta$. Hence this orbit also has exactly $|A|^2$ outputs.

### E.2 Unit-distance and number-field candidate

The supplied unit-distance architecture produces norm-one elements in a CM extension. In the notation of that construction, let $L$ be totally real of degree $f$, let $K=L(i)$, choose a fixed collection of $s$ split primes, put

$$
Q=\prod_{j=1}^s q_j,
\qquad D=Q^2,
$$

and let $H$ be the fixed exponential class-number base. The supplied class-group fiber gives a set $U\subset D^{-1}\mathcal O_K$ of norm-one elements satisfying

$$
|U|\ge\left(\frac{2^s}{H}\right)^f.
$$

Define the genuine same-set candidate

$$
A=\left\{\frac{u+u^{-1}}2:u\in U\right\}\subset L\subset\mathbb R.
\tag{E.2}
$$

The trace map has fibers of size at most two: from

$$
u+u^{-1}=w+w^{-1}
$$

one gets $(u-w)(uw-1)=0$. Therefore

$$
|A|\ge \frac12\left(\frac{2^s}{H}\right)^f.
\tag{E.3}
$$

Every real conjugate of an element of $A$ lies in $[-1,1]$. Since

$$
P_3(x,y)=H_3(x-y)-6y
$$

and $|H_3(t)|\le2$ for $|t|\le2$, every conjugate of every output has absolute value at most $8$. Also, with $E=2D$,

$$
A\subset E^{-1}\mathcal O_L,
\qquad
P_3(A,A)\subset E^{-3}\mathcal O_L.
$$

If two elements of $E^{-3}\mathcal O_L$ are distinct, their difference is at least $E^{-3}$ in some real embedding: after multiplication by $E^3$ its nonzero algebraic norm is a nonzero integer. Sup-norm packing now gives the full Cartesian image bound

$$
|P_3(A,A)|
\le(16E^3+1)^f
=(1+128D^3)^f.
\tag{E.4}
$$

Put

$$
\alpha=\frac{2^s}{H},
\qquad
\beta=1+128D^3.
$$

This candidate is an arbitrarily large family only when the supplied tower and the chosen fixed split-prime set give $\alpha>1$. If that inequality is unavailable, (E.2) should be read only as a finite ledger candidate. The rate obstruction below holds even in the favorable case $\alpha>1$.

Since $H\ge1$ and $Q\ge2^s$,

$$
\alpha^2\le D,
\qquad
\frac\beta{\alpha^2}>128D^2.
\tag{E.5}
$$

Thus this rigorously controlled full-image container loses exponentially. This is a failure of the available counting ledger, not a lower bound on the actual image of the trace set.

The product-window version fails for a structural reason. Let $E_0\subset\mathbb R$ be bounded measurable, let $V=|E_0|$, and put $F=P_3(E_0,E_0)$. Then

$$
\boxed{|F+[-1/2,1/2]|\ge V^2.}
\tag{E.6}
$$

For $V\le3+\sqrt{10}$, the diagonal inclusion $-6E_0\subset F$ and the one-dimensional Brunn-Minkowski inequality give

$$
|F+[-1/2,1/2]|\ge6V+1\ge V^2.
$$

For $V\ge4$, choose $y\in E_0$ near its essential infimum and restrict $x$ to $E_0\cap(y+V/2,\infty)$. This subset has measure arbitrarily close to $V/2$, while

$$
\frac{\partial}{\partial x}P_3(x,y)
=3(x-y)^2-3
\ge\frac{3V^2}{4}-3.
$$

The one-dimensional change-of-variables formula yields

$$
|F|\ge\frac{3V^3}{8}-\frac{3V}{2}\ge V^2.
$$

The ranges overlap. Consequently Blichfeldt averaging in a totally real tower, followed only by ambient output packing, cannot give $b<2a$. For the fractional lattice $D^{-1}\mathcal O_L$, the exact local ledger is

$$
D^3\left|F+
\left[-\frac1{2D^3},\frac1{2D^3}\right]\right|
\ge D^2V^2,
\tag{E.7}
$$

already at the squared input-volume base before root-discriminant loss. Here is the needed proof with the smaller thickening. If $V\ge4$, the monotone-slice argument above gives $|F|\ge V^2$, so the left side of (E.7) is at least $D^3V^2\ge D^2V^2$. If $0<V<4$, the diagonal and Brunn-Minkowski give

$$
\left|F+
\left[-\frac1{2D^3},\frac1{2D^3}\right]\right|
\ge6V+D^{-3}.
$$

After multiplication by $D^3$, this is $6D^3V+1>D^2V^2$ for every integer $D\ge1$.

The substantial standard results in this paragraph are used in these precise forms:

1. One-dimensional Brunn-Minkowski: $|X+Y|\ge|X|+|Y|$ for nonempty measurable $X,Y\subset\mathbb R$.
2. Monotone change of variables: if a $C^1$ map is injective on an interval, then $|g(S)|=\int_S|g'|$ for measurable $S$ in that interval.
3. Blichfeldt averaging: a bounded measurable $W\subset\mathbb R^f$ has a translate containing at least $\operatorname{vol}(W)/\operatorname{covol}(\Lambda)$ points of a full lattice $\Lambda$.
4. Algebraic norm separation: a nonzero algebraic integer has nonzero integral norm, so at least one conjugate has absolute value at least $1$.

### E.3 Direct insertion into the supplied sum-product construction

For the frozen construction $A=GP$, with its fixed parameter $0<\varepsilon\le1$, write $x=g_1p_1$ and $y=g_2p_2$. Then

$$
\begin{aligned}
P_3(x,y)={}&g_1^3p_1^3
-3g_1^2g_2p_1^2p_2
+3g_1g_2^2p_1p_2^2
-g_2^3p_2^3\\
&-3g_1p_1-3g_2p_2.
\end{aligned}
\tag{E.8}
$$

The associated unit tuple and carrier tuple each retain their original ordered pair through their last coordinates. Hence their exact joint parameter count is

$$
|G|^2|P|^2=|A|^2.
\tag{E.9}
$$

This contrasts with multiplication $xy$, where the two unit variables merge into $g_1g_2\in GG$. In the cubic, two independent unit-character directions remain.

The archimedean container is worse. If the frozen construction has

$$
|\sigma(a)|\le2Xe^Y,
$$

then

$$
|\sigma(P_3(x,y))|\le65X^3e^{3Y},
$$

and packing gives the output base $131X^3e^{3Y}$. Against the asymptotic per-degree upper input base $(5Y+1)(2\varepsilon X+1)$ (the frozen finite bound also has a harmless exterior factor $10$), one has for $X,Y\ge2$

$$
\frac{131X^3e^{3Y}}
{\bigl((5Y+1)(2\varepsilon X+1)\bigr)^2}>139.
\tag{E.10}
$$

Thus the box bound is strictly worse than quadratic. The natural exact code above is merely quadratic; it does not rule out additional collisions among its labels. To improve it, one would need a new exponential overlap theorem for the slices in (C.1), equivalently for

$$
3(s-s')=(d-d')(d^2+dd'+d'^2).
$$

The frozen separate estimates for $A+A$ and $AA$ do not control this four-input correlation.

### E.4 High-dimensional digit theorems

Let $\Sigma\subset\mathbb R$ have size $h\ge2$, let $\theta$ be transcendental over $\mathbb Q(\Sigma)$, and set

$$
A_d=
\left\{
\sum_{i=0}^{d-1}a_i\theta^i:a_i\in\Sigma
\right\}.
$$

Then

$$
\boxed{
|P_3(A_d,A_d)|
\ge h^{2d}-h^{d+\lceil d/2\rceil}.
}
\tag{E.11}
$$

To prove this, represent two pairs by polynomials $a,b$ and $a',b'$, put $u=a-b$, $v=a+b$, and similarly $u',v'$. Equality gives

$$
(u-u')(u^2+uu'+u'^2)=3(v-v').
\tag{E.12}
$$

The right side has degree at most $d-1$. If $u\ne u'$ and $D=\max(\deg u,\deg u')$, then the positive-definite leading form $X^2+XY+Y^2$ shows that the second factor has degree $2D$. Therefore equality is impossible if either difference has degree at least $\lceil d/2\rceil$. All such ordered pairs have unique outputs. The excluded pairs agree in their top $\lfloor d/2\rfloor$ digits, and their number is exactly $h^{d+\lceil d/2\rceil}$.

There is also an exact good-reduction statement. Let $\mathcal O$ be a torsion-free $\mathbb Z$-order for which $\mathcal O/3\mathcal O$ is reduced, and let $A\subset\mathcal O$ reduce injectively modulo $3\mathcal O$. Then $P_3$ is injective on $A^2$. Indeed, equality of outputs gives $u^3=u'^3$ modulo $3$. Frobenius is injective in a reduced characteristic-three ring, so $u\equiv u'\pmod3$. Expanding $u=u'+3w$ then gives $u^3-u'^3\in9\mathcal O$, whence $v\equiv v'\pmod3$ and finally $x\equiv x'$, $y\equiv y'\pmod3$. Injectivity of the chosen residue section finishes the proof.

Ordinary carries do not help for full digit alphabets. For $A_n=\{0,1,\ldots,n-1\}$, difference-slices with $|u|\ge3\sqrt n$ occupy disjoint intervals, giving

$$
|P_3(A_n,A_n)|\ge n^2-O(n^{3/2}).
\tag{E.13}
$$

### E.5 Offline structured computation

Computation was used only to reject or refine candidates. It was not used as proof.

- Formal polynomial digits with $\Sigma=\{0,1\}$ gave exactly $4^d$ outputs for $d\le8$.
- Three-symbol formal alphabets with distinct residues modulo $3$ gave exactly $9^d$ outputs for $d\le5$.
- The formal collision alphabet $\Sigma=\{0,3,6\}$ gave
  $7,75,711,6507,58887,530955$ outputs for $d=1,\ldots,6$; its ratio to $9^d$ rose throughout the tested range.
- The truncated nilpotent binary model gave
  $4,10,34,112,380,1292,5488,20112$ outputs for $d=1,\ldots,8$.
- Cyclic wraps $T^d=\pm1$ with binary digits had full or near-full pair image for $d\le9$.
- Quadratic algebraic recurrences had an observed image exponent rising toward $2$ for $d\le9$.
- Integer intervals were near-quadratic, consistently with the theorem (E.13).

The first two rows are explained by the exact mod-$3$ theorem. The attractive truncated row is explained by the deleted tail in (D.1). The collision alphabet shows why a one-coordinate defect does not automatically tensor under scalar polynomial digits: cross-coordinate convolution restores the missing information.

## F. Independent audit

The final claims were checked against the following failure modes.

- **Distinct real inputs:** transcendental evaluations and field embeddings used above are injective; the companion affine map is a real bijection.
- **Same set in both variables:** every positive theorem uses one common $A'_n$ in both slots. Rich bipartite subgraphs were not promoted to same-set image bounds.
- **Full Cartesian square:** (E.4) and the companion theorem count every pair. Prescribed fiber incidences were rejected because unmatched cross-pairs remain.
- **Energy versus image:** no collision-energy lower bound is used as an image upper bound. Equation (C.1) is a direct union identity.
- **Denominators:** in (E.2), $A\subset(2D)^{-1}\mathcal O_L$ and outputs lie in $(2D)^{-3}\mathcal O_L$; the cubic denominator is fully charged.
- **Embeddings:** a field embedding is injective. Norm separation is applied only after clearing the exact denominator.
- **Class number and root discriminant:** they enter the supplied norm-one theorem through one fixed exponential base $H$; no subexponential saving is claimed.
- **Constants:** $Q,D,H,X,Y,\varepsilon$ are fixed while field degree grows. All failed ledgers fail at the fixed per-degree base.
- **Nilpotents and split coordinates:** their formal gain is excluded from the scalar-real theorem because no faithful algebra embedding into $\mathbb R$ exists.
- **Special-form scope:** the non-special claims concern polynomial $F,g,h$, with both inner polynomials nonconstant. Constant $\Phi$ is excluded from the companion non-special theorem.
- **Computational evidence:** every computational statement is labeled as evidence only and is unnecessary for the proved companion theorem.

No contradiction with the frozen local results was found. The present no-go statements concern specific global architectures; they are not presented as a disproof of CPSI.

## G. Proved companion theorem

### Theorem G.1: postcomposition and common-affine inheritance

Let $S\in\mathbb R[x,y]$. Suppose there are $c_0>0$ and finite sets $A_n\subset\mathbb R$, with $|A_n|\to\infty$, such that

$$
|S(A_n,A_n)|\le |A_n|^{2-c_0}.
$$

For fixed $\Phi\in\mathbb R[t]$, $a\ne0$, and $b\in\mathbb R$, put

$$
Q(x,y)=\Phi(S(ax+b,ay+b))
$$

and

$$
A'_n=\frac{A_n-b}{a}
=\left\{\frac{t-b}{a}:t\in A_n\right\}.
$$

Then $|A'_n|=|A_n|$ and

$$
Q(A'_n,A'_n)=\Phi(S(A_n,A_n)).
$$

Because a function cannot increase the cardinality of a finite image,

$$
|Q(A'_n,A'_n)|
\le |S(A_n,A_n)|
\le |A'_n|^{2-c_0}.
\tag{G.1}
$$

All constants are unchanged and independent of $n$.

Apply the theorem with $S=R$. Since

$$
R(ax+b,ay+b)
=a^2(x-y)^2+5a(x+y)+10b,
\tag{G.2}
$$

the resulting explicit family is

$$
\boxed{
Q_{\Phi,a,b}(x,y)
=\Phi\bigl(a^2(x-y)^2+5a(x+y)+10b\bigr).
}
\tag{G.3}
$$

For nonconstant $\Phi$, its partial-derivative ratio is

$$
\frac{(Q_{\Phi,a,b})_x}{(Q_{\Phi,a,b})_y}
=\frac{2a(x-y)+5}{5-2a(x-y)}.
\tag{G.4}
$$

This is a nonconstant rational function of $x-y$, so Lemma B.1 proves that every polynomial in (G.3) is outside both special forms. Its degree is $2\deg\Phi$.

For the requested concrete polynomial, take $a=1$, $b=0$, and $\Phi(t)=t^2+t$. Then

$$
\boxed{
P_4(x,y)
=\bigl((x-y)^2+5(x+y)\bigr)^2
+(x-y)^2+5(x+y).
}
$$

It has degree $4$, is non-special, and the original frozen witness sets for $R$ satisfy

$$
|P_4(A_n,A_n)|
\le |R(A_n,A_n)|
\le |A_n|^{2-c_0}.
$$

Thus $c=c_0$ is an explicit inherited exponent in terms of the already-proved seed theorem.

## H. Verdict

**3. CPSI remains open, but an explicit new polynomial family with a proved power saving has been established.**

The proved family is (G.3), and every nonconstant member is non-special in the polynomial sense. The cubic work did not merely stop at unsuccessful experiments: it isolated the exact translated-slice union (C.1), ruled out a fixed field-norm amplification, proved near- or exact injectivity for broad digit models, and showed quantitatively why the direct number-field and $A=GP$ containers do not cross the entropy threshold.

## I. Exactly one next mathematical target

Fix one explicit witness sequence $A_n^{(R)}$ from the proved theorem for $R$. Prove or refute the existence of a constant $c>0$ such that, for arbitrarily large $n$,

$$
\boxed{
\left|
\bigcup_{u\in A_n^{(R)}-A_n^{(R)}}
\left(
H_3(u)-6\bigl(A_n^{(R)}\cap(A_n^{(R)}-u)\bigr)
\right)
\right|
\le |A_n^{(R)}|^{2-c}.
}
$$

This is CPSI restricted to the already successful quadratic-seed sets, and it asks for exactly the cross-slice overlap missing from the current sum-product and number-field estimates.
