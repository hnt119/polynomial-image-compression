# Exact discrete incidences and occupied arithmetic labels

21 October 2026 · MS-O2 cycle · T03 · version 1.
Fixed polynomial: \(Q(x,y)=x^2+xy+y^2\).
Strictly offline; unchanged tower, order, scalar carrier, and radius \(T_*\).

**Result.** Exhaustiveness of the finite unit inventory turns actual returns
into an exact finite orbit partition. The reciprocal-return sum is precisely
the number of occupied order-unit components. These components have an exact
principal-order-ideal and relative-norm classification. The elementary
ambient label count below does not give a positive exponential saving.
No exponential actual mean, concentrated return tail, or image obstruction
is proved by this companion.

## 1. Objects and source boundary

Read the [MS-O1 report](../2026-10-21-relative-unit-population/README.md),
its [arithmetic proof](../2026-10-21-relative-unit-population/arithmetic.md),
and the prior
[field and cutoff proof](../2026-10-20-mixed-signature/field-units.md).
The unchanged objects are
\[
 [F:\mathbb Q]=d,\quad K=F(s),\quad s^3+s+1=0,\quad
 E=K(\omega),\quad R=\mathcal O_K[\omega],\qquad
 G_R=\{u\in R^\times:u\tau(u)=1\}.
 \tag{1}
\]
The signatures are \(K:(d,d)\), \(E:(0,3d)\), and \(\tau\) fixes \(K\).
Fix the already specified \(T=T_*\), and write
\[
 C=C_K(T)=\{x\in\mathcal O_K:|\sigma x|\le T
          \text{ at every embedding}\},\qquad A=\sigma_0(C),\qquad n=|A|.
 \tag{2}
\]
The real embedding \(\sigma_0\) is injective, so below the actual real
set and its algebraic representatives are identified. In particular
\(C=-C\), \(0\in C\), and \(n\ge3\).

Let
\[
 \Omega=C^2\setminus\{(0,0)\},\qquad N=n^2-1,
 \qquad U=\{u\in G_R:\|\ell(u)\|_1\le dL(T)\},\quad
 L(T)=\tfrac12\log(48T^6).
 \tag{3}
\]
For \(u=a+b\omega\), the actual action is
\[
 M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},\qquad
 u(x-\omega y)=x'-\omega y',\qquad Q(x',y')=Q(x,y).
 \tag{4}
\]
The inherited MS-F6 cutoff proves that **every** \(G_R\)-return of a
nonzero source in \(C^2\) belongs to \(U\). It is this exhaustiveness,
not merely the population lower bound \(|U|\ge2^d\), that is used here.

Put
\[
 D_u=\{p\in\Omega:M_up\in C^2\},\qquad
 r(p)=\#\{M_up:u\in U,\ M_up\in C^2\},
 \tag{5}
\]
and retain the exact incidence statistics
\[
 S_1=\sum_{u\in U}|D_u|,\qquad
 S_2=\sum_{u,v\in U}|D_u\cap D_v|,\qquad \mu=S_1/N.
 \tag{6}
\]
No continuous overlap is substituted for one of these discrete counts.
This contribution has zero mathematical-program allocation and does not
derive the separate source-window or convex-body overlap estimates.

## 2. MSR-I1 — complete finite orbit intersections and exact moments

For \(p=(x,y)\ne0\), set \(z(p)=x-\omega y\in R\setminus\{0\}\).
The nonzero assertion follows from \(\omega\notin K\).
Define an equivalence relation on \(\Omega\) by
\[
 p\sim q\quad\Longleftrightarrow\quad z(q)=u z(p)
                  \text{ for some }u\in G_R.
 \tag{7}
\]
Let its nonempty classes be \(\mathcal C_1,\ldots,\mathcal C_M\),
with sizes \(m_1,\ldots,m_M\). Thus \(\sum_i m_i=N\).

**Statement — PROVED.** For every \(p\in\mathcal C_i\),
\[
 \boxed{r(p)=m_i.}
 \tag{8}
\]
Consequently
\[
 \boxed{S_1=\sum_i m_i^2,\qquad S_2=\sum_i m_i^3,\qquad
          \sum_{p\in\Omega}\frac1{r(p)}=M.}
 \tag{9}
\]
In particular
\[
 \mu\ge N/M\ge2,
 \qquad
 \frac{S_2}{N}-\mu^2
   =\frac1N\sum_i m_i(m_i-\mu)^2.
 \tag{10}
\]

**Proof.** Multiplication on nonzero \(z(p)\) is free: if two units have
the same target, they are equal. Every member \(q\) of the full-group
orbit intersection in (7) is a return from \(p\), so its connecting
unit belongs to \(U\) by the cutoff. Conversely each return counted
in (5) belongs to the same class. This proves (8), even though \(U\)
itself is not a subgroup.

Freeness gives \(r(p)=\sum_{u\in U}1_{D_u}(p)\). Summing this and
its square over \(p\) proves the first two identities of (9).
Each class contributes exactly 1 to the reciprocal sum. Cauchy's inequality
\((\sum_i m_i)^2\le M\sum_i m_i^2\) proves \(\mu\ge N/M\).
The element \(-1\in G_R\) sends every nonzero source to its distinct
negative, and both lie in \(\Omega\); thus every \(m_i\) is even and
at least 2, giving \(M\le N/2\). Expanding the last sum proves the
variance identity. \(\square\)

**First-moment boundary.** The unconditional lower bound furnished here is
\(\mu\ge2\). An exponential inventory does not improve this bound by
itself: the domains \(D_u\) for many non-sign units may be empty, or may
cover only a small part of \(\Omega\). An exponential first moment has
not been established. A large first moment alone would not bound \(M\)
above: a few large classes can dominate \(\sum m_i^2\) while many small
classes remain. The exact reciprocal statistic in (9) avoids that ambiguity.

The origin must remain excluded in (6). It has one actual target but is
fixed by every unit, so including it would add \(|U|\) to the incidence
sum rather than 1. Its image contribution is charged separately below.

## 3. MSR-I2 — reciprocal returns, exceptions, and full support

**Statement — PROVED.** For every real threshold \(H>0\),
\[
 |\{p\in\Omega:r(p)<H\}|\le H M,
 \qquad |Q(A,A)|\le M+1.
 \tag{11}
\]
The number \(M\) is a component count, not generally the number of
nonzero quadratic values.

**Proof.** Classes of size less than \(H\) contribute their sizes to
the bad-pair count, at most \(H\) per class. The polynomial \(Q\) is
constant on each class by (4), so the number of nonzero values is at
most \(M\). Positive definiteness at \(\sigma_0\) makes the zero fiber
exactly the origin, accounting for the additional 1. Several components
can have the same \(Q\)-value; the inequality does not identify a unit
orbit with a complete quadratic fiber. \(\square\)

For example, a proved bound
\[
 M\le N e^{-\rho d}\quad(\rho>0\text{ fixed})
 \tag{12}
\]
would immediately give, for each \(0<\kappa<\rho\),
\[
 |\{p:r(p)<e^{\kappa d}\}|\le N e^{-(\rho-\kappa)d},\qquad
 |Q(A,A)|\le n^2e^{-\rho d}+1.
 \tag{13}
\]
With the unchanged upper input exponent \(B(T)=3\log(2T+1)\), this
would imply every fixed \(0<c<\min\{\rho/B(T),2\}\) eventually.
No concentration of \(r(p)\) around its mean is needed for this
implication. Conversely, the reciprocal-average assertion
\(N^{-1}\sum_p1/r(p)\le e^{-\rho d}\) is exactly (12).
Neither assertion is proved in this companion. This is a reformulation
of the inverse-return route on the same carrier, not a replacement
construction or a claim that MS-O2's variance premise is necessary.
A fixed prefactor \(C_0\) in (12) simply multiplies the two decaying terms
in (13) by \(C_0\); the strict eventual power-saving range is unchanged.

## 4. MSR-I3 — exact arithmetic labels for the components

For \(z=z(p)\), attach the joint label
\[
 \boxed{\bigl(zR,\ b=z\tau(z)=Q(x,y)\bigr).}
 \tag{14}
\]
Here \(zR\) is the principal ideal of the order, and \(b\) is the
**exact element of \(K\)**, not its absolute integer norm.

**Statement — PROVED.** Two nonzero sources lie in the same component
if and only if their labels (14) agree. Thus \(M\) equals the number
of these labels actually occupied by \(C^2\setminus\{0\}\).

**Proof.** A norm-one order unit preserves both entries of (14).
Conversely, \(zR=z'R\) gives \(z'=zr\), \(z=z'r'\) for
\(r,r'\in R\), hence \(rr'=1\) and \(r\in R^\times\).
Equality of the second entries gives
\(N_{E/K}(r)=b/b=1\). This uses no Dedekind assertion for the
nonmaximal order \(R\). \(\square\)

There is a useful upper relaxation to maximal-order labels. Let
\(G_E=\ker(N_{E/K}:\mathcal O_E^\times\to\mathcal O_K^\times)\).
Equality of
\[
 \bigl(I=(z)\mathcal O_E,\ b\bigr)
 \tag{15}
\]
places two sources in one free \(G_E\)-orbit. Such an orbit splits
into at most \([G_E:G_R]\le27^d\) full \(G_R\)-orbits. Intersecting
with \(\Omega\) does not increase that bound. A valid ideal label
necessarily satisfies
\[
 I\tau(I)=(b)\mathcal O_E.
 \tag{16}
\]

For a nonzero \(b\in\mathcal O_K\), define
\[
 a(b)=\#\{I\subset\mathcal O_E\text{ nonzero integral ideal}:
                         I\tau(I)=(b)\mathcal O_E\}.
 \tag{17}
\]
Unique ideal factorization gives the exact formula
\[
 a(b)=
 \begin{cases}
 \displaystyle\prod_{\mathfrak p\text{ split in }E/K}
                  (v_{\mathfrak p}(b)+1),
       &v_{\mathfrak p}(b)\text{ even at every inert }\mathfrak p,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{18}
\]
Only primes dividing \((b)\) contribute nontrivial factors.
Indeed at a split prime, the two exponents of \(I\) must sum to
\(v_{\mathfrak p}(b)\), giving that exponent plus one choices.
At an inert prime, the unique exponent must be half of
\(v_{\mathfrak p}(b)\). At a ramified prime, the exponent of
\((b)\mathcal O_E\) is doubled, so the exponent of \(I\) is uniquely
\(v_{\mathfrak p}(b)\).

Let \(\mathcal B=Q(C,C)\setminus\{0\}\), regarded as actual elements
of \(K\). We obtain the fully scoped upper bound
\[
 \boxed{M\le27^d\sum_{b\in\mathcal B}a(b).}
 \tag{19}
\]
This allows nonprincipal ideals and ideals having no generator with exact
relative norm \(b\), and it ignores the scalar window. Each relaxation
only increases the upper count; none asserts that all labels are realized.

## 5. MSR-I4 — a uniform divisor estimate and its scoped deficit

For a fixed \(\epsilon>0\), set the finite constant
\[
 C_\epsilon=\prod_{\substack{p\text{ rational prime}\\p<2^{1/\epsilon}}}
                       (1-p^{-\epsilon})^{-1}.
 \tag{20}
\]
This definition involves no prime enumeration in this task.
For any nonzero integral ideal \(\mathfrak a\) of the degree-\(3d\)
field \(K\), its divisor count satisfies
\[
 \tau_K(\mathfrak a)
       \le C_\epsilon^{3d}(N\mathfrak a)^\epsilon.
 \tag{21}
\]
To prove it, write \(\mathfrak a=\prod\mathfrak p^{e_{\mathfrak p}}\).
When \(N\mathfrak p\ge2^{1/\epsilon}\), use
\(e+1\le2^e\le(N\mathfrak p)^{\epsilon e}\).
For smaller norms, with \(r=(N\mathfrak p)^{-\epsilon}\),
\[
 (e+1)r^e\le\sum_{k=0}^e r^k\le(1-r)^{-1}.
\]
At most \(3d\) prime ideals lie above each rational prime, and
\(N\mathfrak p\ge p\). Multiplying these estimates proves (21).
The constant is uniform in the field; its dependence on \(\epsilon\)
is explicit and is not discarded.

Since \(a(b)\le\tau_K((b))\), and every actual output satisfies
\[
 |\sigma b|\le3T^2,\qquad
 |N_{K/\mathbb Q}b|\le(3T^2)^{3d},\qquad
 |\mathcal B|\le(6T^2+1)^{3d},
 \tag{22}
\]
equations (19)–(21) imply
\[
 M\le\left[27 C_\epsilon^3(3T^2)^{3\epsilon}
                              (6T^2+1)^3\right]^d.
 \tag{23}
\]
The first bound in (22) is the triangle inequality for \(Q\); the last
is the previously proved norm-separated scalar packing count at radius
\(3T^2\). It is an ambient count, not a claim that every such scalar
is a quadratic value.

To see exactly what this bound certifies, use the unchanged input lower
bound
\[
 n\ge V(T)^d,\qquad V(T)=\frac{(\pi/2)T^3}{D_*^{3/2}}.
 \tag{24}
\]
Since \(n\ge3\), \(N=n^2-1\ge(8/9)V(T)^{2d}\). Thus this particular
combination of bounds gives
\[
 \frac MN\le\frac98\,\Theta_\epsilon(T)^d,
 \qquad
 \Theta_\epsilon(T)=
 \frac{108D_*^3}{\pi^2}\,
 C_\epsilon^3(3T^2)^{3\epsilon}
 \frac{(6T^2+1)^3}{T^6}.
 \tag{25}
\]
For every \(\epsilon>0\) and \(T\ge T_0\),
\[
 \Theta_\epsilon(T)>\frac{23328D_*^3}{\pi^2}>1.
 \tag{26}
\]
Indeed \(C_\epsilon\ge1\), \((3T^2)^{3\epsilon}\ge1\),
\((6T^2+1)^3/T^6>216\), and \(D_*\ge1\).

**FAILED IN STATED SCOPE — this upper certificate.** Counting all ambient
norm values, all allowed maximal-order ideal assignments, and then paying
the order index does not establish an exponentially small \(M/N\),
even with the adjustable uniform divisor bound (21).
The estimate is weaker than the elementary \(M\le N/2\) from signs.
Equation (26) is about the base in an upper bound. It is not a lower
bound for \(M\), not a theorem that actual orbit components are small,
and not an actual-image obstruction. Sharper counts of **occupied**
joint labels remain outside this failure statement.

## 6. Ledger and precise retained gap

| Item | Exact charge or statement | Evidence/status |
|---|---|---|
| Source carrier, field, radius | Exactly the MS-O1 objects at \(T_*\) | Unchanged |
| Real projection | Injective; no source thinning in either coordinate | Inherited |
| Unit/target multiplicity | Free on nonzero sources; one target at zero | MSR-I1 |
| Exhaustive return cutoff | All full-group returns between window points lie in \(U\) | Inherited MS-F6 |
| Component support | \(r(p)=m_i\); reciprocal sum \(M\) exactly | MSR-I1 |
| Actual first moment | \(\mu=N^{-1}\sum m_i^2\ge N/M\ge2\); no positive exponential lower rate yet | MSR-I1 / OPEN rate |
| Exact label | Principal \(R\)-ideal and exact element \(b=Q(p)\) | MSR-I3 |
| Maximal-order relaxation | At most \(27^d\) order orbits per maximal-order orbit | MSR-I3 |
| Local ideal assignments | Formula (18), including inert parity and ramification | MSR-I3 |
| Uniform divisor cost | \(C_\epsilon^{3d}\lvert Nb\rvert^\epsilon\), fixed \(\epsilon\) chosen before growth | MSR-I4 |
| Ambient output cost | \((6T^2+1)^{3d}\); no realization assertion | MSR-I4 |
| First-moment/variance concentration | Exact identities, no new asymptotic bounds | OPEN |
| Inverse-return improvement | Equivalent to exponentially few occupied order labels | OPEN |
| Full image | \(\lvert Q(A,A)\rvert\le M+1\); no new improving bound for \(M\) | MSR-I2 / OPEN rate |
| Mathematical program use | Zero evaluations, zero research-program CPU | No experiment performed |

MSR-I1–I4 are complete internal symbolic proofs, with hypotheses and
quantifiers above. Unique ideal factorization and the quadratic prime
factorization cases are inherited standard arithmetic inputs; no external
literature or theorem search occurred. On 21 October 2026 the independent
internal auditor read and passed the complete written MSR-I1–I4 proofs,
including all orbit, label, divisor, and normalization formulas. Two table
delimiter renderings were corrected after that review. No external review
or novelty claim is made. Only this new companion was written; historical
sources remain unchanged.
