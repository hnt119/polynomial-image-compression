---
title: "Phase C0 - Corrected and Auditable Baseline"
subtitle: "A transverse rank-one quadratic family with power-saving image sets"
date: "3 September 2026"
geometry: margin=0.82in
fontsize: 10pt
colorlinks: true
linkcolor: blue
urlcolor: blue
toc: true
toc-depth: 2
---

> **Correction status.** This is a corrected copy of the submitted Phase C0
> report. The submitted Markdown, PDF, ledgers, and referee report remain
> unchanged. The focused corrections are itemized in `C0_CORRECTION_LOG.md`.
> With those corrections incorporated, this baseline is **safe to freeze
> within the supplied source system**. External novelty and literature status
> have not been checked.

# 1. One-page result

## Exact outcome

The bounded offline run succeeds. Define

\[
\boxed{P_*(x,y)=(x+2y)^2+3x-y.}
\]

There is a fixed constant \(\varepsilon>0\) and a sequence of finite sets
\(A_j\subset\mathbb R\), with \(|A_j|\to\infty\), such that

\[
\boxed{|P_*(A_j,A_j)|\le |A_j|^{2-\varepsilon}.}
\]

Consequently, for every \(N_0\ge1\), some member of the sequence has
\(|A_j|\ge N_0\) and satisfies the required inequality. The same set occurs
in both inputs.

The proof establishes the following family theorem.

> **Theorem C0.1.** Let
> \[
> L(x,y)=ax+by,\qquad M(x,y)=cx+ey
> \]
> have integral coefficients, with \(\gcd(a,b)=1\) and
> \[
> ab(ae-bc)\ne0.
> \]
> Then the fixed polynomial \(P=L^2+M\) has a constant
> \(\varepsilon_P>0\) and arbitrarily large finite sets
> \(A\subset\mathbb R\) satisfying
> \[
> |P(A,A)|\le |A|^{2-\varepsilon_P}.
> \]

The exponent is not claimed to be uniform over the family. It depends on the
fixed coefficients and on one fixed number-field tower and parameter choice.

## Status

**PROVED WITHIN THE OFFLINE SOURCE SYSTEM.** Every load-bearing step is either
an inspected statement from a supplied project source, a standard fact stated
precisely below, or a complete derivation in this report. The statement has
been proved within the current offline source system. External novelty and
literature status have not been checked.

## Mechanism and symbolic exponent

For a squarefree product \(Q\) of fixed completely split odd primes, define

\[
P_Q=L^2+QM,
\qquad
P_Q(Qx,Qy)=Q^2P(x,y).
\]

At each \(p\mid Q\), the reduced image is a square set of density
\((p+1)/(2p)\). Put

\[
\rho=\prod_{p\mid Q}\frac{p+1}{2p}.
\]

For the explicit polynomial, a centered Minkowski carrier of radius \(X\)
gives the following normalized factor furnished by the stated bounds:

\[
\Theta(X)=D\rho\left(18+\frac{8Q}{X}+\frac{Q}{X^2}\right).
\]

The supplied field construction gives \(t\asymp\ell^2\) completely split
primes and \(\log D=O(\ell\log\ell)\). Since every selected prime is
\(1\pmod4\), \(\rho\le(3/5)^t\). Thus one fixes \(\ell\) so that
\(27D\rho<1\), and then fixes \(X>\max\{Q,\sqrt D\}\), giving
\(\Theta(X)<1\). One may take

\[
\boxed{
\varepsilon=
\frac{-\log\Theta(X)}{\log(2X+1)}>0.
}
\]

## Why this is a substantive extension of the supplied example

The supplied benchmark is \((x-y)^2+x+y\). A common affine change applied to
both inputs, followed by an affine output change and an optional variable
swap, preserves the projective direction of the rank-one quadratic part. The
benchmark direction is \([1:-1]\), whereas the new explicit polynomial has
direction \([1:2]\). A degree-preserving univariate postcomposition is only an
affine output change. Therefore the new polynomial is not obtained from the
benchmark by a transport that automatically preserves a Cartesian square.

The advance is not only one new coefficient choice: the proof classifies and
establishes compression for the whole transverse square-leading family in
Theorem C0.1.

# 2. Scope, sources, and epistemic labels

The run remained offline. No browser, web search, arXiv retrieval, remote
research service, or network installation was used. All supplied sources were
kept read-only. The submitted run's provenance remains in
`phase_c0/SOURCE_MANIFEST.md`; the correction audit is recorded in
`SOURCE_MANIFEST_C1.md`.

The five Phase B Markdown records were read in full before candidates were
selected. The load-bearing field statement is Proposition 3.8 of the supplied
unit-distance proof, PDF pages 12-14. The centered carrier correction was
checked against frozen Phase A, Section 4.1. The local-to-global framework was
checked against Cycle 2, Sections 4-11. Cycle 1 supplied the mandatory warning
that collision energy does not upper-bound support.

The labels used below are:

- **PROVED FROM SUPPLIED SOURCES:** an inspected supplied statement is applied
  with its stated hypotheses;
- **PROVED HERE:** a complete derivation appears in this report;
- **STANDARD FACT:** the exact standard statement used is recorded;
- **ROUTE FAILED:** the tested certificate fails, without refuting the
  polynomial's compression conjecture;
- **OPEN:** a precise dependency remains unresolved.

No original Pohoata paper was supplied for this run. The Cycle 2 report was
therefore used as a supplied-report source, not described as direct primary
verification. The final proof does not need arbitrary prescribed-prime
compatibility and does not rely on the stronger infinite-split-set statement
from the remarks.

# 3. Candidate generation and selection

Four nonduplicate candidate routes were screened. The detailed cards and
eight-component scores are in the original Phase C0 file
[`CANDIDATE_LEDGER.md`](../phase_c0/CANDIDATE_LEDGER.md).

| ID | Candidate | Score | Decision |
|---|---|---:|---|
| C1 | \(L^2+M\), with \(L\) primitive and \(M\) transverse; explicit \((x+2y)^2+3x-y\) | 39/40 | Selected and proved |
| C2 | \((x+2y)^4+3x-y\) | 28/40 | Specified interval-packing certificate obstructed |
| C3 | \(x^2+xy+y^2+3x-y\) | 29/40 | Uniform local route rejected: full image |
| C4 | \(x^2+3y^2+x+y\), modulus \(3^k\) | 24/40 | Exact local theorem; box route failed |

Candidate C1 was selected because it is the only route with all four
load-bearing features simultaneously proved: sparse reductions at every
selected odd prime, common same-input transport, quadratic archimedean scale,
and split-prime compatibility without prescribing special congruence classes.

Candidate C2 has stronger fourth-power density but pays a \(Q^3\) coefficient
and quartic output cost. Candidate C3 shows that a nondegenerate binary
quadratic form is the wrong local residue object. Candidate C4 tests genuine
prime-power amplification; its exact density tends to \(1/2\), not to zero.

**PROJECT CONJECTURE C1 (selection-stage wording).** The polynomial
\(P_*=(x+2y)^2+3x-y\) has a fixed power-saving image sequence on Cartesian
squares. External novelty and literature status have not been checked in this
offline run. Sections 4-8 prove this conjecture within the offline source
system.

# 4. Algebraic classification and local value sets

## 4.1 Unique common-scaling quadratic deformation

Write a quadratic polynomial as \(P=P_2+P_1+P_0\), where the subscripts are
homogeneous degrees.

> **Lemma 4.1 (PROVED HERE).** If \(F_Q\) has degree at most two and
> \[
> F_Q(Qx,Qy)=Q^2P(x,y),
> \]
> then necessarily
> \[
> \boxed{F_Q=P_2+QP_1+Q^2P_0.}
> \]

**Proof.** Write \(F_Q=G_2+G_1+G_0\). Then
\(F_Q(Qx,Qy)=Q^2G_2+QG_1+G_0\). Equality of homogeneous pieces gives
\(G_2=P_2\), \(G_1=QP_1\), and \(G_0=Q^2P_0\). The converse follows by
substitution. \(\square\)

Thus for homogeneous linear forms \(L,M\),

\[
P=L^2+M,\qquad P_Q=L^2+QM,\qquad P_Q(Qx,Qy)=Q^2P.
\]

If a constant \(r\) is included, the correct deformation is
\(L^2+QM+Q^2r\), not \(L^2+Q(M+r)\).

## 4.2 Complete binary-quadratic value-set classification

> **Lemma 4.2 (PROVED HERE).** Let \(q\) be a homogeneous binary quadratic
> form over \(\mathbb F_p\), with \(p\) odd.
>
> - rank \(0\): the value set is \(\{0\}\);
> - rank \(1\): the value set has \((p+1)/2\) elements;
> - rank \(2\): the value set is all of \(\mathbb F_p\).

**Proof.** A rank-one form is \(\lambda u^2\) in suitable linear
coordinates, so its image is a scalar multiple of the squares. A rank-two
isotropic form is equivalent to \(\lambda uv\) and is visibly surjective. A
rank-two anisotropic form is equivalent to
\(\lambda(u^2-dv^2)\), with \(d\) nonsquare. Identify
\(u+v\sqrt d\) with \(\mathbb F_{p^2}\). The displayed form is a nonzero
scalar multiple of the norm to \(\mathbb F_p\). Since
\(\mathbb F_{p^2}^{\times}\) is cyclic, the map \(z\mapsto z^{p+1}\) has
image of order \(p-1\), so the norm is surjective. Zero is also represented.
\(\square\)

For an integral quadratic form, rank drops only at the odd primes dividing
its discriminant, apart from content primes. Hence a nondegenerate rational
quadratic part is locally surjective at all but finitely many odd primes. A
primitive rank-one part remains rank one at every odd good prime.

This partially resolves O1 and O2: within the common-scaling quadratic
scheme, robust sparse reductions occur exactly when the nonzero homogeneous
quadratic part has rank one.

## 4.3 Exact square images

> **Lemma 4.3 (PROVED HERE).** Let \(L=ax+by\) with
> \(\gcd(a,b)=1\). If \(p\mid Q\) is odd, then
> \[
> (L^2+QM)(\mathbb F_p,
> \mathbb F_p)=\{z^2:z\in\mathbb F_p\},
> \]
> and therefore
> \[
> \left|(L^2+QM)(\mathbb F_p,
> \mathbb F_p)\right|=\frac{p+1}{2}.
> \]

**Proof.** At least one of \(a,b\) is nonzero modulo \(p\), so
\(L:\mathbb F_p^2\to\mathbb F_p\) is surjective. Modulo \(p\), the term
\(QM\) vanishes. On \(\mathbb F_p^{\times}\), squaring has kernel
\(\{1,-1\}\); adding zero gives \((p+1)/2\) values. \(\square\)

There are no odd exceptional primes for a primitive homogeneous \(L\). At
\(p=2\), squaring is the identity and gives no local saving; the field source
used below supplies only primes congruent to \(1\pmod4\).

## 4.4 Nonspecialness

> **Lemma 4.4 (PROVED HERE).** Let
> \[
> P=(ax+by)^2+cx+ey+r,
> \]
> with \(ab\ne0\). Then
> \[
> P=g(u(x)+v(y))
> \quad\Longleftrightarrow\quad ae-bc=0,
> \]
> and \(P\) is never of the form \(g(u(x)v(y))\) with both \(u,v\)
> nonconstant.

**Proof.** In an additive representation, dependence on both variables makes
\(g,u,v\) nonconstant. Put \(r=\deg g\) and
\(m=\max\{\deg u,\deg v\}\). The top terms of \(u(x)\) and \(v(y)\) involve
different variables and cannot cancel, so \(rm=2\). If \(r=1\), there is no
mixed monomial, contradicting the nonzero \(xy\) coefficient. Hence
\(r=2,m=1\), and both inner polynomials are affine linear. Expansion then
forces the linear part \(cx+ey\) to be parallel to \(ax+by\), exactly
\(ae-bc=0\). Conversely, parallelism writes \(P\) as a univariate quadratic
in \(ax+by=u(x)+v(y)\).

For a multiplicative representation, write
\(r=\deg g\), \(m=\deg u\), and \(n=\deg v\). All are positive and
\(r(m+n)=2\), so \(r=m=n=1\). Its homogeneous quadratic part is therefore a
scalar multiple of \(xy\), whereas \((ax+by)^2\) has nonzero \(x^2\) and
\(y^2\) terms. \(\square\)

For \(P_*\), \((a,b,c,e)=(1,2,3,-1)\), and
\(ae-bc=-7\ne0\). Thus \(P_*\) is outside both excluded forms.

# 5. Number fields and carrier lemmas

## 5.1 Field supply

> **Lemma 5.1 (PROVED FROM SUPPLIED SOURCES).** For all sufficiently large
> integers \(\ell\), put
> \[
> t=\left\lfloor\frac{(\ell-1)^2}{100}\right\rfloor.
> \]
> There exist distinct rational primes \(p_1,\dots,p_t\), a totally real
> field \(F\), and an infinite tower of totally real fields \(F_j\) such that
> \(d_j=[F_j:\mathbb Q]\to\infty\),
> \[
> \operatorname{rd}(F_j)=\operatorname{rd}(F)=:D,
> \qquad \log D=O(\ell\log\ell),
> \]
> and every \(p_i\equiv1\pmod4\) splits completely in every \(F_j\).

This is Proposition 3.8, properties (P1)-(P4), of the supplied
unit-distance proof. This report retains the source notation: the totally real
layers are \(F_j\). The source's distinct fields \(K_j=F_j(i)\) are CM fields
used in the unit-distance construction and are not carriers here. The primes
are fixed independently of the tower level. Remark 3.9 in that source records
the required order of fixed parameters.

For the family theorem, define

\[
C_P=2\left((|a|+|b|)^2+|c|+|e|\right)+1.
\]

Every selected prime is at least \(5\), hence its square density is at most
\(3/5\). Since \(t\gg\ell^2\) but \(\log D=O(\ell\log\ell)\), one can fix a
sufficiently large \(\ell\) for which

\[
C_PD\left(\frac35\right)^t<1.
\]

After applying Lemma 5.1 at this fixed \(\ell\), set

\[
Q=\prod_{i=1}^t p_i,
\qquad
\rho=\prod_{i=1}^t\frac{p_i+1}{2p_i}.
\]

Then \(Q\) is a fixed odd squarefree integer, all its prime factors split
completely throughout the tower, and

\[
\boxed{\theta:=C_PD\rho<1.}
\]

No prescribed-prime theorem is used. The dependence of \(D\) on \(\ell\)
is charged before \(\ell\) is fixed.

## 5.2 Centered Minkowski carrier

For a totally real field \(K\) of degree \(d\), define

\[
B_K(X)=\{\alpha\in\mathcal O_K:
|\sigma_i(\alpha)|\le X\text{ for all }i\}.
\]

> **Lemma 5.2 (PROVED HERE FROM STANDARD FACTS).** If
> \(|\Delta_K|^{1/d}\le D\), then
> \[
> \boxed{
> \left(\frac X{\sqrt D}\right)^d
> \le |B_K(X)|\le(2X+1)^d.}
> \]

**Proof.** The Minkowski image of \(\mathcal O_K\) is a lattice of covolume
\(\sqrt{|\Delta_K|}\). Blichfeldt averaging applied to
\([-X/2,X/2)^d\) gives a translate containing at least
\(X^d/\sqrt{|\Delta_K|}\) lattice points. This is a translated box, not the
centered carrier. Fix one of those points and subtract it from all the others.
The difference map is injective and lands in \([-X,X]^d\), proving the
centered lower bound.

If \(\alpha\ne\beta\) are algebraic integers, then
\(N_{K/\mathbb Q}(\alpha-\beta)\) is a nonzero integer. Hence some conjugate
difference has absolute value at least \(1\). The carrier points are therefore
\(1\)-separated in sup norm. Packing unit cubes around them inside a cube of
side \(2X+1\) proves the upper bound. \(\square\)

Choose one fixed

\[
X>\max\{Q,\sqrt D\}.
\]

Then \(|B_{F_j}(X)|\to\infty\) as \(d_j\to\infty\).

## 5.3 Uniform packing in a residue class

> **Lemma 5.3 (PROVED HERE).** Every class modulo \(Q\mathcal O_K\) contains
> at most
> \[
> \left(\frac{2M_0}{Q}+1\right)^d
> \]
> points of \(B_K(M_0)\).

**Proof.** Distinct congruent points differ by \(Q\gamma\) for a nonzero
algebraic integer \(\gamma\). Some conjugate of \(\gamma\) has absolute value
at least \(1\), so the points are \(Q\)-separated in sup norm. Disjoint cubes
of side \(Q\) centered at them lie in a cube of side \(2M_0+Q\). \(\square\)

This is a worst-case count for each class; no equidistribution is assumed.

# 6. Complete proof of Theorem C0.1

Fix \(L=ax+by\), \(M=cx+ey\), and all parameters as in Section 5. Put

\[
P=L^2+M,\qquad P_Q=L^2+QM.
\]

In the following steps, \(K\) denotes one totally real source layer \(F_j\)
of degree \(d=d_j\); it does not denote the source's CM field \(F_j(i)\).

The algebraic identity and nonspecialness have already been proved. It remains
to count the complete support.

## Step 1: allowed quotient classes

Complete splitting gives

\[
\mathcal O_K/p_i\mathcal O_K\cong\mathbb F_{p_i}^{d}.
\]

The ideals \(p_i\mathcal O_K\) are pairwise comaximal, so the Chinese
remainder theorem gives

\[
\mathcal O_K/Q\mathcal O_K
\cong\prod_{i=1}^t\mathbb F_{p_i}^{d}.
\]

At each of the \(d\) coordinates for \(p_i\), Lemma 4.3 permits exactly
\((p_i+1)/2\) values. Hence every output reduction lies in a set of at most

\[
\prod_{i=1}^t\left(\frac{p_i+1}{2}\right)^d
=\boxed{(\rho Q)^d}
\]

classes modulo \(Q\mathcal O_K\). This is a Cartesian-product count in the
quotient ring, not probabilistic independence. Surjectivity of the carrier
onto the quotient is neither asserted nor needed.

## Step 2: all-conjugate output radius

For \(\alpha,\beta\in B_K(X)\), every real embedding satisfies

\[
|L(\alpha,\beta)|\le (|a|+|b|)X,
\qquad
|M(\alpha,\beta)|\le(|c|+|e|)X.
\]

Since \(X>Q\),

\[
|\sigma(P_Q(\alpha,\beta))|
\le\left((|a|+|b|)^2+|c|+|e|\right)X^2=:M_0.
\]

Thus \(P_Q(B_K(X),B_K(X))\subset B_K(M_0)\).

For the explicit polynomial, a valid all-conjugate upper bound is

\[
M_0=9X^2+4QX,
\]

which gives

\[
\Theta(X)=D\rho
\left(18+\frac{8Q}{X}+\frac{Q}{X^2}\right)<27D\rho<1.
\]

## Step 3: full-support multiplication

By Lemma 5.3, each allowed class contributes at most
\((2M_0/Q+1)^d\) outputs. Therefore

\[
\begin{aligned}
|P_Q(B_K(X),B_K(X))|
&\le(\rho Q)^d\left(\frac{2M_0}{Q}+1\right)^d\\
&=[\rho(2M_0+Q)]^d.
\end{aligned}
\]

Put \(n=|B_K(X)|\). The carrier lower bound gives
\(X^{2d}\le D^d n^2\). Since
\(2M_0+Q\le C_PX^2\),

\[
\boxed{
|P_Q(B_K(X),B_K(X))|
\le \theta^d n^2,
\qquad \theta=C_PD\rho<1.}
\]

This count covers every output. Collision energy is not used.

## Step 4: real embedding and fixed-polynomial transport

Choose one real field embedding \(\sigma_j:F_j\hookrightarrow\mathbb R\) and
define

\[
A_j=Q^{-1}\sigma_j(B_{F_j}(X)).
\]

A field embedding is injective, and evaluation of an integral polynomial
commutes with it. The same scalar map is used in both input coordinates. Thus

\[
|A_j|=|B_{F_j}(X)|=:n_j
\]

and, from \(P_Q(Qx,Qy)=Q^2P(x,y)\),

\[
|P(A_j,A_j)|
=|P_Q(B_{F_j}(X),B_{F_j}(X))|
\le\theta^{d_j}n_j^2.
\]

There are no input or output fibers to charge.

## Step 5: exponential-to-power conversion

Define

\[
\varepsilon_P=\frac{-\log\theta}{\log(2X+1)}>0.
\]

The direction of the conversion uses the carrier **upper** bound:

\[
n_j\le(2X+1)^{d_j}
\quad\Longrightarrow\quad
n_j^{\varepsilon_P}\le\theta^{-d_j}.
\]

Hence

\[
|P(A_j,A_j)|\le n_j^{2-\varepsilon_P}.
\]

The carrier lower bound and \(X>\sqrt D\) show \(n_j\to\infty\). Therefore
the sets meet every threshold \(N_0\) along the sequence. This completes the
proof of Theorem C0.1 and its explicit corollary. \(\square\)

# 7. Parameter ledger

| Parameter | Fixed when | Depends on | Gain or cost |
|---|---|---|---|
| \(P,L,M,C_P\) | first | explicit coefficient choice | fixes the theorem; \(C_P\) is archimedean cost |
| \(\ell\) | second | \(C_P\) and source thresholds | makes quadratic split-prime gain dominate \(\log D\) |
| \(t,D\) | with the source tower | \(\ell\) | \(t\) supplies savings; \(D\) costs input density |
| \(p_1,\ldots,p_t\) | after \(\ell\) | Proposition 3.8 construction | split square restrictions |
| \(Q\) | after the primes | their product | fixed deformation coefficient and modulus |
| \(\rho\) | after the primes | exact square densities | local gain \(-\log\rho\) |
| \(X\) | after \(Q,D\) | chosen greater than both \(Q\) and \(\sqrt D\) | carrier and output scale |
| \(d_j\) | varies last | tower level | amplifies the already positive fixed rate |

All finite choices are fixed before \(d_j\to\infty\). Increasing the number
of primes would require recomputing \(D,Q,\rho,X\); the proof instead fixes one
sufficiently large \(\ell\) once.

# 8. Proof dependency diagram

| Stage | Claim and status | Output passed forward |
|---:|---|---|
| 1 | Proposition 3.8, **SUPPLIED SOURCE** | Totally real tower, \(d_j\to\infty\), split primes, \(D\) |
| 2 | Quadratic rate comparison, **PROVED HERE** | Fixed \(Q,\rho\) with \(C_PD\rho<1\) |
| 3 | Deformation identity, **PROVED HERE** | \(P_Q(Qx,Qy)=Q^2P(x,y)\) |
| 4 | Square value sets and CRT, **PROVED HERE + STANDARD CRT** | At most \((\rho Q)^d\) output classes |
| 5 | Centered carrier and output radius, **PROVED HERE** | Large input and one bounded all-conjugate region |
| 6 | Worst-class packing, **PROVED HERE** | Full support \(\le[\rho(2M_0+Q)]^d\) |
| 7 | Signed rate, **PROVED HERE** | \(|P_Q(B,B)|\le\theta^d|B|^2\), \(\theta<1\) |
| 8 | Common scalar transport, **PROVED HERE** | Same real set in both inputs |
| 9 | Upper-size exponent conversion, **PROVED HERE** | \(|P(A,A)|\le|A|^{2-\varepsilon_P}\) |

There is no assumed or open arrow in the proof of Theorem C0.1.

# 9. Adversarial audit

The independent referee report is reproduced separately in the original
Phase C0 file [`REFEREE_REPORT.md`](../phase_c0/REFEREE_REPORT.md). The referee
independently reconstructed the algebra,
field supply, full-support count, transport, and exponent conversion, and
returned the verdict **PROVED WITHIN THE OFFLINE SOURCE SYSTEM**.

The serious objections and dispositions were:

1. **Overbroad nonspecial family wording.** Primitive \(L\) and transverse
   \(M\) are insufficient if \(L\) uses only one variable: \(x^2+y\) is
   additive-special. **Resolved:** Theorem C0.1 assumes \(ab\ne0\), as well as
   transversality. The compression mechanism itself works more broadly, but
   the nonspecial claim is made only under the corrected hypotheses.
2. **Compressed degree argument.** A nonspecialness proof must eliminate all
   degree factorizations. **Resolved:** Lemma 4.4 treats the linear and
   quadratic additive cases and the exact multiplicative total-degree case.
3. **Prescribed-prime overreach.** A generic tower statement would be too
   weak. **Resolved:** Lemma 5.1 cites Proposition 3.8 directly and uses only
   the primes produced by that construction.
4. **Rate notation.** The explicit certificate factor \(\Theta(X)\) and conservative family
   factor \(\theta=C_PD\rho\) must not be conflated. **Resolved:** They have
   distinct names and each exponent is defined from the factor used.
5. **Extension scope.** The direction invariant does not rule out arbitrary
   two-variable affine equivalence. **Resolved:** The claim is restricted to
   common affine input maps, affine output maps, and variable swap - the
   operations relevant to automatic preservation of a Cartesian square.
6. **F1-F10 and Section 8 checks.** Every check passed: no collision-energy
   inference, no hidden fibers, no equidistribution, correct complete
   splitting and CRT, centered carrier correction, all-conjugate control,
   fixed parameters, and correct upper-bound exponent conversion.

No repair changed the primary polynomial, construction, rate inequality, or
final quantifiers.

# 10. Failure and mutation history

## C2: quartic local-density and interval-packing certificate

For

\[
P^{(4)}=(x+2y)^4+3x-y,
\qquad
P_Q^{(4)}=(x+2y)^4+Q^3(3x-y),
\]

the identity \(P_Q^{(4)}(Qx,Qy)=Q^4P^{(4)}(x,y)\) holds. At each supplied
split prime, the density of fourth powers is \((p+3)/(4p)\). A valid
symmetric upper bound from separate estimates is

\[
M_4=81X^4+4Q^3X,
\]

so

\[
\Theta_4(X)=D\rho_4
\left(162X^2+\frac{8Q^3}{X}+\frac{Q}{X^2}\right).
\]

Writing \(z=X/Q\), either \(z\ge1/4\) and \(162z^2>10\), or
\(z<1/4\) and \(8/z>32\). Therefore the first two terms exceed
\(10Q^2\). Also

\[
\rho_4Q^2=
\prod_{p\mid Q}\frac{p(p+3)}4\ge10^t.
\]

Hence \(\Theta_4(X)>1\) for every \(X>0\). **CERTIFICATE OBSTRUCTION.** No
choice of \(X\) makes this local-fourth-power-density plus symmetric-interval
plus uniform-packing bound prove a saving. This is not a lower bound for the
actual image. Sharper support counting on the same carrier, additional residue
information, a different deformation, a different carrier, and other proved
mechanisms all remain open.

## C3: full-rank quadratic local image

For \(q=x^2+xy+y^2\), the discriminant is \(-3\). Every supplied split
prime is \(1\pmod4\), hence is not \(3\). Lemma 4.2 makes \(q\) surjective at
all selected primes. The local density is \(1\), so the route has no local
gain. **LOCAL ROUTE REJECTED; CONJECTURE NOT REFUTED.**

## C4: prime-power test

For every \(k\ge1\), exact valuation analysis gives

\[
\left|\{x^2+3y^2\pmod {3^k}:x,y\in\mathbb Z/3^k\mathbb Z\}\right|
=\frac{3^k+1}{2}.
\]

Indeed, the valuations \(2v_3(x)\) and \(1+2v_3(y)\) have opposite parity
and cannot cancel; every represented nonzero unit part is \(1\pmod3\), and
each such unit is a square modulo every \(3^j\). Summing over possible
valuations gives the displayed formula. Its density tends to \(1/2\), and
the exact box ledger remains greater than \(4D\). The supplied source also
does not guarantee complete splitting of the prescribed prime \(3\).
**ROUTE FAILED; CONJECTURE NOT REFUTED.**

No mutation of candidate C1 was needed after the integrated proof and audit. The run
used one successful serious iteration and three bounded screening iterations,
within the six-iteration limit.

# 11. Mechanism progress relative to O1-O7

| Open lemma | Phase C0 progress |
|---|---|
| O1: sparse local value-set criterion | **Resolved for all homogeneous binary quadratics over odd fields.** Rank one gives a square set; rank two is surjective. Still open for arbitrary bivariate polynomials. |
| O2: removable arithmetic deformation | **Resolved for common-scaling quadratics and proved for the transverse rank-one family.** The unique degree weighting is \(P_2+QP_1+Q^2P_0\). General deformations remain open. |
| O3: higher-degree threshold | **Scoped certificate obstruction.** For the tested quartic, the displayed local-density plus symmetric-interval plus uniform-packing bound is greater than one at every scale. No actual-image lower bound follows. |
| O4: prescribed split primes | **Avoided, unchanged.** Candidate C1 is sparse at every odd selected prime, so Proposition 3.8's own primes suffice. |
| O5: prime powers | **Narrowed by one exact theorem.** The \(x^2+3y^2\) image modulo \(3^k\) has \((3^k+1)/2\) values, insufficient here. General lifting remains open. |
| O6: rank-two correlated sums | **Unchanged and unnecessary for candidate C1.** |
| O7: carriers beyond boxes | **Unchanged.** Different carriers are one possible route; sharper same-carrier support counting and additional residue information remain possible as well. |

The main advance beyond the supplied example is the proof of an entire
same-set family and the local classification explaining why rank-one
quadratic leading parts are the robust quadratic source of sparse reductions.

# 12. Prioritized next bottleneck

The next prioritized lemma is a higher-degree carrier statement, not another
unstructured polynomial search.

> **Proposed O7/O3 carrier lemma.** Fix an even \(m>2\), primitive
> two-variable integral \(L\), and transverse integral linear \(M\). For the
> common-scaling deformation
> \[
> F_Q=L^m+Q^{m-1}M,
> \qquad F_Q(Qx,Qy)=Q^m(L^m+M),
> \]
> construct, or rule out, carriers \(C_j\subset\mathcal O_{F_j}\) in the
> supplied totally real split-prime tower for which:
> \[
> e^{ad_j-o(d_j)}\le |C_j|\le e^{Bd_j+o(d_j)},
> \]
> for packing modulus \(R=Q\), every allowed output class has at most
> \(e^{ud_j+o(d_j)}\) points in the exact
> output region, and
> \[
> 2a-(\log R+u)-\log\rho_m>0,
> \]
> where \(\rho_m\) is the allowed output-class density modulo \(R\), with
> every coefficient, modulus, and fiber cost included.

This lemma is narrower than the target theorem: it asks for a specific
uniform class-packing certificate for a fixed higher-power deformation. The
quartic calculation only obstructs the displayed interval-based uniform
packing estimate. A positive answer could instead use sharper support counting
on the same carrier, additional residue information, a different deformation,
a different carrier, or another proved mechanism.

The full remaining-gap list is: arbitrary sparse-value criteria beyond
quadratics, general removable deformations, general prime-power lifting,
prescribed split-prime compatibility, rank-two correlated sums, and
non-box carriers.

# 13. Final status

**Exact classification:** PROVED WITHIN THE OFFLINE SOURCE SYSTEM; SAFE TO
FREEZE WITHIN THE SUPPLIED SOURCE SYSTEM.

**Strongest established conclusion:** every fixed transverse square-leading
integral polynomial in Theorem C0.1, in particular

\[
(x+2y)^2+3x-y,
\]

has arbitrarily large same-input finite real sets with a fixed power-saving
image bound.

**Remaining mathematical bottleneck:** obtain a full-support estimate that
beats the explicit quartic degree and deformation cost. The displayed
local-density plus interval-packing certificate does not do so, but the
quartic polynomial and the centered carrier are not ruled out.

The statement has been proved within the current offline source system.
External novelty and literature status have not been checked. Phase C0 stops
here.
