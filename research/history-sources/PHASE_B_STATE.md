# PHASE_B_STATE

## Validated abstraction principles

1. **Collision equations are diagnostic, not support certificates.** For
   \[
   E_F(A)=\#\{(a,b,c,d)\in A^4:F(a,b)=F(c,d)\},
   \]
   Cauchy-Schwarz gives \(|F(A,A)|\ge |A|^4/E_F(A)\). Large energy is necessary for compression, but a separate full-support argument is required.

2. **Exact factor-through compression.** If a bounded-multiplicity parameterization of \(A\) makes \(F\) factor through small action and carrier supports, the resulting support bound is valid after the parameter multiplicity is charged.

3. **Bounded-fiber coordinate compression.** A normal form \(F(x,y)=G(u(x)+v(y))\) or \(F(x,y)=G(u(x)v(y))\) is useful only after domains and fibers of every coordinate map are recorded.

4. **Uniform residue-class packing.** Let \(K_d\) have degree \(d\), let \(R\) be a fixed rational modulus, and let \(\Omega_d\subseteq\mathcal O_{K_d}/R\mathcal O_{K_d}\). If an archimedean output region contains at most \(e^{ud+o(d)}\) algebraic integers in each residue class and
   \[
   |\Omega_d|\le e^{(\log R-s)d+o(d)},
   \]
   then the constrained support has size at most
   \[
   e^{(\log R+u-s)d+o(d)}.
   \]
   A total box count and a residue density cannot be multiplied without this per-class bound.

5. **Split-prime amplification.** If an odd prime \(p\) splits completely in a degree-\(d\) field and the reduced polynomial image has density \(q_p<1\) in \(\mathbb F_p\), then the corresponding product restriction has density \(q_p^d\) in \(\mathcal O_K/p\mathcal O_K\). Here “independent” means Cartesian-product factorization under the Chinese remainder theorem, not probabilistic independence.

6. **Local-to-global polynomial compression.** Suppose
   \[
   |A_d|\ge e^{ad-o(d)},\qquad |A_d|\le e^{Bd+o(d)},
   \]
   and an output region has per-class exponent \(u\), while the allowed residue classes have saving exponent \(s\). Put \(c=\log R+u\). Then
   \[
   |F(A_d,A_d)|\le e^{(c-s)d+o(d)}.
   \]
   A normalized exponential saving exists exactly when
   \[
   \delta:=2a-c+s>0,
   \]
   and then
   \[
   |F(A_d,A_d)|\le |A_d|^{2-\delta/B+o(1)}.
   \]

7. **Degree-versus-local-density test.** For \(A=B_K(X)\), root-discriminant bound \(\Delta_K^{1/d}\le D\), fixed \(F\in\mathbb Z[x,y]\) of degree \(m\), coefficient \(\ell_1\)-height \(H\), modulus \(R\), and local density \(\rho^d\), one has the generic bound
   \[
   \frac{|F(A,A)|}{|A|^2}
   \le
   \left[\rho D\left(2H X^{m-2}+\frac{R}{X^2}\right)\right]^d.
   \]
   Thus the bracket must be less than \(1\). Degree \(2\) is special because the main \(X\)-power disappears.

8. **Fixed-polynomial rescaling.** If bijective affine maps \(\tau_Q,\eta_Q\) satisfy
   \[
   F_Q(\tau_Q(x),\tau_Q(y))=\eta_Q(F(x,y)),
   \]
   then passing from \(A_0\) to \(\tau_Q^{-1}(A_0)\) preserves input and output cardinalities. Pohoata uses \(\tau_Q(x)=Qx\) and \(\eta_Q(z)=Q^2z\).

## Rejected principles

1. Large collision energy alone proves a small image.
2. Global action-carrier factorization survives inside every polynomial.
3. A simplifying coordinate map may be used without a domain and fiber audit.
4. A bounded archimedean box alone compresses every fixed-degree polynomial.
5. High dimension automatically creates a saving.
6. A local image density and a total archimedean count may be multiplied without a uniform per-residue-class estimate.
7. One nonsplit rational prime automatically produces \(d\) local restrictions.
8. An auxiliary coefficient \(Q\) may vary with the set size when the target theorem requires one fixed polynomial.

## Current strongest mechanism

The strongest reusable result is the uniform residue-class packing lemma combined with split-prime amplification and the signed condition
\[
2a-c+s>0.
\]
Pohoata's quadratic construction realizes this with
\[
\theta=13D\rho<1,
\qquad
|f_Q(P,P)|\le \theta^d|P|^2.
\]

## Current bottleneck

Given a fixed polynomial \(F\) outside the global additive/multiplicative forms, find a removable arithmetic deformation \(F_Q\) and a fixed collection of completely split primes such that:

- the reduced images have sufficiently small combined density \(\rho\);
- coefficient and modulus growth still satisfy the degree-density inequality;
- an affine/scaling identity returns to the one fixed polynomial \(F\).

Rank-two action-carrier mixing remains a bottleneck for polynomials whose local images are full, but it is no longer the only route around global factorization.

## Next recommended research direction

Conduct a targeted literature review on finite-field polynomial value sets, sparse-image polynomials, exceptional polynomials, character-sum bounds, and prescribed split-prime towers. Do not begin unrestricted Phase C construction search yet.
