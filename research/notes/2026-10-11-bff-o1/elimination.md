# A finite-family projection and localization lemma

11 October 2026 · BFF-O1 cycle · version 1 · lead proof.
Status: **PROVED — BFO-L1; independent internal written audit PASS**.
This is an algebraic lemma for the unchanged T03 balanced-factor carrier,
not a new carrier or a selected-action estimate. All arguments are symbolic.

## E1. Statement over a rational function field

Let \(k\) be a characteristic-zero infinite field, let \(z\) be
transcendental over \(k\), and put \(F=k(z)\). Fix a finite list of
polynomial maps
\[
\Psi_j:\mathbb A_F^{d_j}\longrightarrow\mathbb A_F^N,
\qquad 0\le d_j\le d,
\]
whose coefficients are rational functions of \(z\). Suppose a specified
nonempty sublist of source maps has \(d_j=d\) and Jacobian rank \(d\)
over its rational function field. Then there exist:

* a matrix \(\pi\in F^{d\times N}\);
* a nonzero polynomial \(H\in F[Y_1,\ldots,Y_d]\);
* fixed integers \(M\ge1,D\ge0\); and
* a nonzero polynomial \(e(z)\in k[z]\)

with the following properties. For any specialization \(z=\eta\) in
any characteristic-zero extension of \(k\), with \(e(\eta)\ne0\), all
these expressions are defined. For each specified source map,
\[
P_{j,\eta}(x)=H_\eta\bigl(\pi_\eta\Psi_{j,\eta}(x)\bigr)
\tag{1}
\]
is a nonzero polynomial of degree at most \(D\). If
\(P_{j,\eta}(x)\ne0\), then the union, over **every** target map in
the original list, of solutions
\[
\Psi_{i,\eta}(y)=\Psi_{j,\eta}(x)
\tag{2}
\]
has at most \(M\) parameter points over an algebraic closure. Thus it
also bounds any union of actual target points parametrized by those maps.
The constants and exceptional specialization polynomial depend only on
the fixed finite family, not on \(\eta\), a later recursion depth, or
any finite carrier inside the parameter spaces.

Maps with a zero-dimensional parameter space are allowed. No assertion
is made about sources on \(P_{j,\eta}=0\).

## E2. Choosing one projection

Consider all maps in the list having maximal Jacobian rank \(d\).
Each has domain dimension exactly \(d\). For each, the determinant of
\(\pi\,D\Psi_j\), viewed as a polynomial in the entries of an
indeterminate \(d\times N\) matrix \(\pi\) with coefficients in
\(F(x)\), is nonzero: a suitable choice of \(d\) independent rows
of \(D\Psi_j\) gives a nonzero minor. Clear denominators and select
one nonzero coefficient in its polynomial expansion in \(x\).
There are finitely many resulting nonzero polynomials in the entries
of \(\pi\). Their product is nonzero, so the infinitude of \(F\)
allows a matrix in \(F^{d\times N}\) where they all remain nonzero.
Fix such a matrix. Write \(f_j=\pi\Psi_j\).

For every rank-\(d\) map the \(d\) components of \(f_j\) are
algebraically independent. For every other map they are algebraically
dependent. Here we use the following elementary characteristic-zero
Jacobian fact. If rational functions have transcendence degree \(a\),
their differentials span an \(a\)-dimensional space over the ambient
rational function field. To see this, take a transcendence basis among
them. It extends to a transcendence basis of the ambient field; the
remaining field extension is algebraic and separable in characteristic
zero. Differentiating each minimal polynomial expresses the differential
of an algebraic element in those of this basis, since the derivative of
its minimal polynomial is nonzero. The differentials of the basis are
independent, as is seen first in the purely transcendental field by its
coordinate derivations and then in the separable extension. In ordinary
coordinates these differentials are the rows of the Jacobian. This proves
the fact used here, including the maps of dimension smaller than \(d\).

For each lower-rank map, fix a nonzero annihilating polynomial
\[
H_j(Y)\in F[Y],\qquad H_j(f_j(x))=0.
\tag{3}
\]
These are polynomial identities, not assertions only at generic points.

## E3. Finite fibers by explicit localization

For a rank-\(d\) map, put \(x=(x_1,\ldots,x_d)\).
Algebraic independence identifies \(F(Y)\) with \(F(f_j(x))\).
The extension
\[
F(x_1,\ldots,x_d)/F(f_{j,1},\ldots,f_{j,d})
\tag{4}
\]
is algebraic: both fields have transcendence degree \(d\). It is
finite because the upper field has finitely many algebraic generators.
For each coordinate \(x_\ell\), choose a monic algebraic equation
\[
x_\ell^{a_{j\ell}}+
\sum_{h<a_{j\ell}}c_{j\ell h}(f_j(x))x_\ell^h=0,
\qquad c_{j\ell h}\in F(Y).
\tag{5}
\]
Choose one nonzero \(h_j(Y)\in F[Y]\) divisible by every denominator
occurring in these finitely many rational functions. Equation (5) holds
in the polynomial ring localized at \(h_j(f_j(x))\): after clearing
denominators it is a polynomial identity. The leading coefficient is 1
in the localized ring.

For a value \(y\) with \(h_j(y)\ne0\), every solution of
\(f_j(x)=y\) consequently satisfies a monic equation of degree
\(a_{j\ell}\) in each separate coordinate. Equivalently the quotient
coordinate algebra is spanned by the monomials
\[
\prod_{\ell=1}^d x_\ell^{e_\ell},
\qquad 0\le e_\ell<a_{j\ell}.
\]
Thus it has dimension at most
\(M_j=\prod_\ell a_{j\ell}\) over the value field. Its number of
distinct geometric points is at most that dimension: evaluation at
any finite set of distinct points gives a surjection to a product of
copies of the algebraic closure, by pairwise comaximal maximal ideals.
In particular the fiber is finite and has at most \(M_j\) points.
The same bound can also be read directly from the separate coordinate
root counts in (5). No sharp degree bound or constant-fiber classification
is needed.

Set
\[
H=\prod_{\text{lower rank }j}H_j
  \prod_{\text{rank }d\ j}h_j,
\qquad M=\sum_{\text{rank }d\ j}M_j.
\tag{6}
\]
Empty products are 1. The source sublist is nonempty, so \(M\ge1\).
All factors are nonzero. At a projected output with \(H\ne0\),
lower-rank target maps have no preimages by (3), and every rank-\(d\)
target map has at most \(M_j\) preimages by (5). Equality of all
\(N\) output coordinates implies equality after projection, so this
bounds the solutions of (2) as well. For every specified source map,
\(H(f_j(x))\ne0\) as a polynomial, by algebraic independence.

## E4. Specialization and uniformity

Only finitely many rational functions of \(z\) have been used:
the maps and bases, the chosen projection, coefficients of (3)–(6),
and the cleared polynomial identities from (5). Include their nonzero
\(z\)-denominators in \(e(z)\). For each source polynomial
\(H(f_j(x))\), choose a coefficient nonzero in \(F\), and include
its nonzero numerator in \(e(z)\). If desired include one nonzero
coefficient of \(H\) too. These form a finite product of nonzero
polynomials. Each identity specializes correctly away from its zeros;
(5) remains monic after the output denominator \(h_j(y)\) is inverted.
Each source polynomial remains nonzero. Its degree is bounded by the
maximum of the finitely many pre-specialization degrees, which defines
\(D\). The same coordinate degrees \(a_{j\ell}\), hence the same
\(M\), remain valid. This proves E1.

In the application \(k=\mathbb Q(\omega)\), and
\(\eta\) is a primitive \(7^{r-1}\)-st root. The inherited
cyclotomic degree formula gives
\[
[k(\eta):k]=6\cdot7^{r-2}\quad(r\ge2).
\]
Once this exceeds \(\deg e\), no nonzero \(e\in k[z]\) can vanish
at \(\eta\). The finitely many exceptional specializations therefore
remove only an initial segment of depths, not an uncontrolled subsequence.

## E5. Scope and provenance

This proof invokes no algebraic-geometric degree theorem, computational
elimination, discriminant estimate, or external source. Algebraic
independence, separable differentiation, polynomial identities, and monic
coordinate equations supply the necessary finite-family bound directly.
The bound \(M\) and exception degree \(D\) exist as fixed integers;
no numerical values or feasible explicit starting depth are claimed.
For BFF-O1 this is sufficient: any fixed \(M\) is at most \((r+1)^1\)
once \(r\ge M-1\). The carrier itself remains completely explicit.

The accompanying tower proof must still establish its finite target
cover, the source rank count, and the actual carrier population avoiding
(1). E1 alone is not a result about the balanced-factor carrier or the
unrestricted quadratic-image problem. Audit status and final disposition
are recorded in the report and independent audit companion.

Independent specialist C audited the complete E1–E4 proof on 11 October
2026 and returned PASS. The algebra specialist also inspected the lemma
and found no issue. The lead independently checked its application to
the written tower proof. These are internal reviews, not external review.
