# TCRC root algebra and the necessary complexity of a pair map

This note is an offline subtask report for the three-copy root-cover phase. It proves an exact factorization identity and a quantitative obstruction to a narrowly specified class of prospective cover proofs. It does **not** disprove TCRC for the actual adaptive family, and it does not claim a real power saving.

## 1. Exact expansion and a shifted-product identity

Let \(A\subset\mathbb R\) be finite, \(C>M(A)\), and suppose \(C+a=\gamma u^2\), \(C+b=\gamma v^2\), with \(\gamma>0\) and \(u,v>0\). All expressions below lie in the stated field whenever these quantities do. No extension of that field is made.

Direct expansion gives
\[
Q(\gamma u^2-C,\gamma v^2-C)
=\gamma^2(u^4+u^2v^2+v^4)-3\gamma C(u^2+v^2)+3C^2.
\tag{1}
\]
Put
\[
s=a+b,\quad R=Q(a,b),\quad
z_\pm=\gamma Q(u,\pm v)
=2C+s\pm\sqrt{(C+a)(C+b)}.
\]
Then
\[
z_++z_-=4C+2s,
\qquad z_+z_-=R+3Cs+3C^2.
\tag{2}
\]
Eliminating \(s\) between these two relations yields the useful exact factorization
\[
\boxed{
(z_+-3C/2)(z_--3C/2)=R-3C^2/4.
}
\tag{3}
\]
Thus the two new branches are not independent: after the common translation by \(3C/2\), they form a factorization of the corresponding translated old norm.

Writing \(h=z-3C/2\), each individual branch satisfies
\[
\boxed{R=3C^2/4+(C+2s)h-h^2.}
\tag{4}
\]
For \(h\ne0\), the old pair sum is therefore recovered exactly by
\[
s=\frac{R-3C^2/4+h^2-Ch}{2h}.
\tag{5}
\]
For a fixed old value \(R\ne3C^2/4\), the branch exchange is the genuine Möbius involution
\[
h\longmapsto\frac{R-3C^2/4}{h}.
\tag{6}
\]
The coefficient in this involution depends on \(R\). Consequently (6) is not a fixed family of three maps of the whole old image. At \(R=3C^2/4\), one of the two factors is zero; this is exactly the already-frozen single-fiber transfer, not a new source of quadratic rank.

The identities do give a constructive coordinate system: any successful three-copy cover must organize factorizations of \(R-3C^2/4\) across **different** old \(R\)-values. Neither preserving an old norm nor exchanging its two factors suffices.

## 2. A finite family of low-degree pair templates cannot certify the cover

### Elementary grid zero lemma

If \(P(X,Y)\in\mathbb R[X,Y]\) is nonzero of total degree at most \(d\), and \(B\subset\mathbb R\) has \(b\) distinct elements, then
\[
|\{(x,y)\in B^2:P(x,y)=0\}|\le db.
\tag{7}
\]
For completeness, write \(P=\sum_{j=0}^r P_j(Y)X^j\) with \(P_r\ne0\). There are at most \(d-r\) exceptional \(y\)'s where \(P_r(y)=0\). For any other \(y\), there are at most \(r\) roots in \(x\). Bounding the exceptional rows by \(b\) points gives at most \((d-r)b+rb=db\). This also covers degrees larger than \(b\), where the estimate may simply be weaker than the trivial bound. Only the elementary univariate polynomial root bound is used.

### Polynomial-template theorem

Let \(H(X,Y)\in\mathbb R[X,Y]\) have total degree at most \(d\), where \(d\ge0\). Among all ordered signed branch labels \((a,b,\varepsilon)\in B^2\times\{+1,-1\}\), at most
\[
\boxed{2\max(d,1)b}
\tag{8}
\]
satisfy
\[
2C+a+b+\varepsilon\sqrt{(C+a)(C+b)}=H(a,b).
\tag{9}
\]
Here \(B\subseteq A\), and \(C>M(A)\), so all radicands are strictly positive.

**Proof.** Every such label is a zero of
\[
P_H(X,Y)=\bigl(H(X,Y)-2C-X-Y\bigr)^2-(C+X)(C+Y).
\tag{10}
\]
This polynomial is nonzero. Indeed, if it vanished identically, fixing any real \(Y=y\ne-C\) would express the nonconstant linear polynomial \((C+X)(C+y)\) as a polynomial square. A nonzero square has even degree, whereas this polynomial has degree one. Its total degree is at most \(2\max(d,1)\). Apply (7). For a fixed ordered pair \((a,b)\), its two branch values differ by a nonzero positive quantity, so at most one sign can equal \(H(a,b)\). This proves (8).

### Application to sign, zero-sum, and affine pair transformations

Suppose a prospective certificate assigns each branch to one of \(t\) pair transformations
\[
\Phi_i(a,b)=(P_i(a,b),Q_i(a,b)),
\]
whose two components have degree at most \(D\ge1\), and then uses
\[
z=\alpha_i Q(\Phi_i(a,b))+\beta_i.
\tag{11}
\]
The coefficients may depend arbitrarily on \(A,C,i\); the point is that \(t,D\) are bounded uniformly as \(b\to\infty\). They may even be arbitrary real coefficients. Whether or not \(\Phi_i(a,b)\) actually belongs to \(A^2\), the polynomial on the right has degree at most \(2D\). Hence all \(t\) templates together capture at most
\[
\boxed{4Dt b}
\tag{12}
\]
ordered signed branch labels, and therefore no more than that many unordered signed labels.

The full root image on \(B\) is represented by \(b(b+1)\) unordered signed branch labels. Consequently a certificate of this specific form covering every branch must satisfy
\[
\boxed{b+1\le4Dt.}
\tag{13}
\]
This is impossible for fixed \(t,D\) and unbounded \(b\).

For the original proposed transformations, \(D=1\). In particular, the theorem covers:

- swapping the pair;
- reversing one or both signs;
- the zero-sum completion \((a,b)\mapsto(a,-a-b)\);
- any finite composition of these linear transformations;
- any fixed affine linear transformation of the pair, even if its coefficients vary with the adaptive stage.

For exactly three degree-one templates, no full branch certificate is possible once \(b>11\). A template may carry several branches at the same output; this creates no gap in the argument, because each branch label satisfying its own assigned identity has already been counted separately.

This last statement **does not** assert that three affine copies of the old image fail. An affine image cover may represent a branch from \((a,b)\) by the old norm of a different pair \((x,y)\) with no bounded-degree formula connecting these pairs. It is only the bounded-complexity pair rule that is ruled out.

## 3. Sharper same-old-norm statement

If the proposed pair transformation preserves \(R=Q(a,b)\), then its affine target is \(H=\alpha R+\beta\). For \(\alpha\ne0\), (10) is quartic in the second input variable \(Y\) for each fixed \(a\), with leading coefficient \(\alpha^2\). Thus at most \(4b\) ordered labels satisfy that template. If \(\alpha=0\), it is quadratic in \(Y\), with leading coefficient \(1\), so the bound is \(2b\).

The same bounds hold for a target \(\alpha Q(a,-b)+\beta\): when \(\alpha\ne0\), the quartic leading coefficient remains \(\alpha^2\). Thus retaining the old norm, changing the sign of the mixed term, or permuting a zero-sum triangle cannot supply the needed macroscopic branch coverage through finitely many affine identities.

In particular, (3) does not become an affine cover by prescribing finitely many affine functions of the *same* old \(R\)-value for one factor. Equation (5) then forces the old pair onto one of finitely many algebraic curves with only \(O(b)\) grid points.

## 4. Rational pair maps do not evade the bounded-degree obstruction

Let \(H=P/N\) be a rational function with nonzero polynomial denominator, and assume both \(P,N\) have degree at most \(d\). On pairs where \(N(a,b)\ne0\), branch equality implies
\[
\bigl(P-(2C+X+Y)N\bigr)^2-(C+X)(C+Y)N^2=0.
\tag{14}
\]
The polynomial has degree at most \(2d+2\) and is nonzero. To see the latter, unique factorization in \(\mathbb R[X,Y]\) shows that the exponent of the irreducible factor \(X+C\) in \((C+X)(C+Y)N^2\) is odd, whereas its exponent in a nonzero square is even. The polynomial ring unique-factorization fact used here is the elementary standard theorem that a polynomial ring over a field is a unique factorization domain.

Therefore at most \((2d+2)b\) ordered labels satisfy the rational template. In particular, if a pair map has two rational coordinate functions with a common denominator and all three polynomials have degree at most \(D\), then \(\alpha Q(\Phi(a,b))+\beta\) has numerator and denominator degree at most \(2D\), giving a bound \((4D+2)b\) per template.

The conclusion remains uniform when denominators and coefficients depend on the adaptive stage. Pairs where the denominator vanishes must be excluded from that template and handled elsewhere. They cannot silently be counted as successfully covered.

## 5. Consequence for this research cycle

The exact constructive identity found here is the shifted norm factorization (3). It converts the signed square-root pair into complementary divisors of the translated old norm, with the old pair sum recovered by (5).

The minimal obstruction to deriving COVER by the proposed sign and zero-sum pair involutions is now explicit: any fixed finite collection of bounded-degree polynomial or rational pair rules covers only \(O(b)\) of the \(b(b+1)\) branch labels. The obstruction holds for each actual adaptive input as well as for arbitrary finite inputs. It survives exceptions \(n-b=O(n^{1-\delta})\), because \(b\to\infty\).

A constructive proof of TCRC must therefore use an assignment across distinct old pairs whose rational degree or number of distinct formulas grows with the history depth, while its **number of output affine maps remains below four**. Radical history maps, which need not be rational functions of the visible pair with bounded degree, are not excluded. No claim is made that such a map exists.

No new \(\rho<4\) image bound has been proved in this subtask. The actual TCRC conjecture and the real TARGET remain unresolved.

## 6. Adversarial audit of the relaxed recurrence

This section records a conditional implication, not a proved cover for the actual family.

Suppose that for every actual adaptive input after some fixed level \(m_0\), a legal comparison parameter and a root subset with \(e_m\) exceptional old inputs satisfy
\[
e_m\le H n_m^{1-\delta_e},\qquad
|R_m|\le\rho s_m+J n_m^{2-\delta_r},
\]
where \(H,J\ge0\), \(\delta_e,\delta_r>0\), and \(0<\rho<4\) are fixed. The subset is used in both root variables. Its cardinality is \(n_m-e_m\).

There are exactly
\[
n_m(n_m+1)-(n_m-e_m)(n_m-e_m+1)
=e_m(2n_m-e_m+1)
\]
remaining unordered signed branch labels. These may coincide with each other or with already counted outputs; counting labels is consequently a valid upper bound. Since \(n_m\ge1\), their number is at most
\[
Hn_m^{1-\delta_e}(2n_m+1)
\le3H n_m^{2-\delta_e}.
\]
Writing \(\delta=\min\{\delta_e,\delta_r\}\) and \(K=3H+J\), the actual optimizer comparison gives
\[
\boxed{s_{m+1}\le\rho s_m+K n_m^{2-\delta}.}
\tag{15}
\]
This uses a good comparison parameter at each **actual** input. It makes no assertion that a separately generated comparison continuation is the actual family.

Set \(q=2^{2-\delta}\). Because \(n_{m_0+j}=2^j n_{m_0}\), iteration over \(r\) steps gives the exact bound
\[
s_{m_0+r}\le\rho^r s_{m_0}
+K n_{m_0}^{2-\delta}
\sum_{j=0}^{r-1}\rho^{r-1-j}q^j.
\tag{16}
\]
For \(\rho\ne q\), the sum is \((\rho^r-q^r)/(\rho-q)\); for \(\rho=q\), it is \(r\rho^{r-1}\). Thus, with \(\kappa=\max\{\rho,q\}<4\),
\[
s_m=O\bigl((m+1)\kappa^m\bigr).
\]
Consequently every
\[
0<c<\min\{2-\log_2\rho,\delta\}
\]
satisfies \(s_m\le n_m^{2-c}\) for all sufficiently large \(m\). Strictness absorbs the constant and the possible factor \(m+1\). This is a complete iteration argument; the remaining missing assertion is the conditional cover hypothesis itself.

For the proposed concrete next-proof constants
\[
\varepsilon=\tfrac14,\quad \rho=4-\varepsilon=\tfrac{15}4,
\quad\delta_e=\delta_r=\tfrac12,
\]
one has \(q=2\sqrt2<15/4\). Hence there is no resonant polynomial loss, and (16) yields
\[
s_{m_0+r}\le
\left(s_{m_0}+
\frac{K n_{m_0}^{3/2}}{15/4-2\sqrt2}\right)(15/4)^r.
\]
A safe conditional exponent is therefore
\[
\boxed{c=\tfrac12\log_2(16/15)\approx0.0465547.}
\tag{17}
\]
The explicit sufficient next statement is: construct, at every sufficiently large actual input, a legal comparison parameter, a common-square-class root subset omitting at most \(H\sqrt{n_m}\) old inputs, and a direct bound
\[
|R_m|\le\tfrac{15}4 s_m+J n_m^{3/2}
\]
with fixed \(H,J\). This statement remains unproved. Allowing its parameter, field coefficients, and individual root representatives to vary with \(m\) does not affect the recurrence, provided the constants \(15/4,H,J\) and the exponents remain fixed.
