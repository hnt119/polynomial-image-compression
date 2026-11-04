# Infinite order certificate for the marked bridge shift

T01 · 11 October 2026 · version 1 · offline, internally audited.

**PROVED — MS-C1 / TC-O1 resolved:** the marked shift
\(T=R_2-R_1\) has infinite order. The certificate uses one good prime,
23, and a field conjugation. It rules out every torsion order at once;
no finite division-order search or numerical height estimate is used.

## Exact field and point

Use precisely the positive real constants of
[TC-G5](../2026-10-11-torsion-compatible-sharing/geometry.md):
\[
a=\sqrt2,\qquad H=\sqrt{(3+a)/14},\qquad W=\sqrt{4a-3},
\qquad L=\mathbb Q(a,H,W).
\]
The field L has degree eight over the rationals. The curve is defined
already over \(\mathbb Q(a)\):
\[
E_c:Y^2=X^3-48X-128-432c^2,
\qquad c=\frac{8H(4-a)}7,\qquad
c^2=\frac{64(19-3a)}{343}.
\]
The positive-Y marked points are
\[
R_1=\left(\frac{68+144a}{7},\frac{288HW(2+3a)}7\right),
\quad
R_2=\left(\frac{164-48a}{7},\frac{288H(5a-6)}7\right).
\]
Their exact difference is
\[
T=\left(
\frac{110+102a+(54+18a)W}{7},\quad
\frac{H\{1368+540a+(792+684a)W\}}7
\right).
\]
The signs are fixed by the displayed positive real square roots. These
coordinates agree with the predecessor's retained chord-law data.

## All orders proof

**1. Conjugation reduces the question to R₂.** Put
\(F=\mathbb Q(a,H)\). The quadratic norms
\[
N((3+a)/14)=1/28,\quad N(4a-3)=-23,\quad
N((4a-3)/((3+a)/14))=-644
\]
show that H gives a quadratic extension of \(\mathbb Q(a)\), and W
gives another quadratic extension of F. Consequently L has an automorphism
\(\sigma\) fixing F and sending W to −W. It fixes the curve and R₂,
and sends R₁ to −R₁. Thus
\[
T+\sigma(T)=2R_2.
\]
If T were torsion, R₂ would be torsion as well.

**2. Choose an exact 23-adic embedding.** There is an embedding
\(F\hookrightarrow\mathbb Q_{23}\) with
\[
a\equiv18=-5\pmod{23},\qquad H\equiv6\pmod{23}.
\]
Both roots lift by the simple-root form of Hensel's lemma:
18²≡2 and \((3+18)/14\equiv13\equiv6²\), with nonzero derivatives.
The coefficients of E are integral there. Since
\[
c^2\equiv16,\quad16+27c^2\equiv11\pmod{23},
\]
its discriminant
\(-2^{12}3^6c^2(16+27c^2)\) is a unit. The curve has good reduction.

**3. A fixed doubling supplies the certificate.** Exact chord arithmetic gives
\[
S=2R_2=\left(48+24a,-\frac{16H(281+208a)}7\right).
\]
The norm identity
\[
(281+208a)(281-208a)=-7\cdot23\cdot47
\]
and the residues \(281+208a\equiv0\), \(281-208a\equiv10\)
prove \(v_{23}(Y(S))=1\). Also \(X(S)\equiv-3\), so
\(3X(S)^2-48\equiv2\) is a unit. The tangent slope at S has
valuation −1; therefore
\[
X(4R_2)=\left(\frac{3X(S)^2-48}{2Y(S)}\right)^2-2X(S)
\quad\text{has }v_{23}=-2.
\]
The existing formal-logarithm lemma, whose hypotheses and proof are
checked in [the arithmetic appendix](arithmetic.md), says that a
nonidentity point with negative X-valuation on this good integral model
over \(\mathbb Q_{23}\) cannot be torsion. Hence R₂ has infinite order,
and the conjugation identity proves that T has infinite order. ∎

## What this resolves

This settles the single question TC-O1: the exact change from R₁ to R₂
in this finite attachment is not a torsion translation of any order.
It does not reopen or alter the accepted two-width bound or genus-four
completion obstruction. The six-scalar attachment remains finite, and
this certificate supplies no growing fixed-output frame family and no
asymptotic cubic image saving. T01 remains **OPEN**. The commissioned
point is resolved; this cleanup stops here without proposing another task.

[Independent referee audit](referee-audit.md) ·
[Provenance and preservation](verification.md).
