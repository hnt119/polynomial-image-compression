# Independent factor switches: exact identities and a sparse source domain

6 October 2026 · version 1 · T03 · lead proof.
Fixed polynomial \(Q(x,y)=x^2+xy+y^2\). All statements below concern
the single product rule defined in §1. They do not extend FG-F1's
33-frequency obstruction.

## 1. Carrier and genuine encoded amplification

Put \(r=k-1\), \(q=7^r\), \(m=6q\), \(\xi=e^{2\pi i/q}\),
\(\omega=e^{2\pi i/3}\), and \(\Delta=1+2\omega\). For
\(\mathbf i=(i_0,\ldots,i_{r-1})\in\{-3,\ldots,3\}^r\), set
\[
c_{h,\mathbf i}=h\prod_{\ell=0}^{r-1}(2-\xi^{i_\ell7^\ell}),
\qquad 1\le h\le8.
\tag{1}
\]
Let \(Z=\bigcup c_{h,\mathbf i}\mu_m\). Decode by
\[
X(z)=\frac{\omega\bar z-\omega^2z}{\Delta},\qquad
Y(z)=\frac{\bar z-z}{\Delta},\qquad z=X(z)-\omega Y(z).
\tag{2}
\]
Set \(A=X(Z)\cup Y(Z)\), \(n=|A|\), and
\(\Gamma=\{(X(z),Y(z)):z\in Z\}\).
The two projections agree because \(Y(z)=X(\omega z)\) and
\(\omega Z=Z\).

The [amplitude proof](amplitudes.md) establishes:
\[
|Z|=|\Gamma|=48q^2,\qquad 8q^2\le n\le48q^2.
\tag{3}
\]
In particular \(n=49^{r+o(r)}\). Scalar collisions have already been
charged in these bounds.

For \(S\subseteq\{0,\ldots,r-1\}\), let \(\mathbf i^S\) negate
the digits indexed by \(S\), and define
\[
u_{\mathbf i,S}=
\prod_{\ell\in S}
\frac{2-\xi^{-i_\ell7^\ell}}{2-\xi^{i_\ell7^\ell}}.
\tag{4}
\]
Every denominator is nonzero; \(|u_{\mathbf i,S}|=1\). The exact
whole-product identity is
\[
u_{\mathbf i,S}c_{h,\mathbf i}=c_{h,\mathbf i^S}.
\tag{5}
\]
Thus switching factors of an encoded point preserves \(Q\) exactly,
including every product cross term. Nonzero flipped digits give distinct
amplitude cosets. If \(s\) digits are nonzero, the encoded equal-norm
fiber has exactly \(6q\,2^s\) distinct targets, after including \(\mu_m\).
This exact encoded-fiber count is proved in amplitudes.md; it is not an
upper bound on the full \(A^2\)-fiber.

## 2. Why coordinatewise switching is not automatically a whole-source action

A general Cartesian source has representations \(x=X(z)\), \(y=Y(w)\)
with \(z,w\in Z\). It need not have \(z=w\). Its actual encoded complex
number is
\[
P(z,w):=X(z)-\omega Y(w)
=\frac{-\omega^2z+\omega\bar z+\omega w-\omega\bar w}{\Delta}.
\tag{6}
\]
For any norm-one \(u\),
\[
uP(z,w)-P(uz,uw)
=\frac{\omega(u-u^{-1})(\bar z-\bar w)}{\Delta}.
\tag{7}
\]
This follows by substituting \(\overline{uz}=u^{-1}\bar z\) into (6).
It shows the precise missing cross term in the proposed common-factor
transport. If \(u\ne\pm1\) and \(z\ne w\), the coordinatewise target
is not the image of the source under this claimed multiplier.

Equation (7) alone is **not** a proof that the two targets have different
norms. A different multiplier could connect equal norms. The theorem below
therefore tests the actual norm equality and counts all coordinatewise
switched targets, allowing independent switches in the two coordinates.

## 3. The precise coordinate-switch certificate

Define a relation \(a\rightsquigarrow a'\) on actual scalars in \(A\):
there exist \(h,\mathbf i,\nu,S\), with \(\nu\in\mu_m\), such that
\[
a=X(c_{h,\mathbf i}\nu),\qquad
a'=X(c_{h,\mathbf i^S}\nu).
\tag{8}
\]
All possible representations are allowed; no arbitrary chosen address is
privileged. The relation using \(Y\) instead of \(X\) is identical,
by \(Y(z)=X(\omega z)\). It is reversible and sign-equivariant:
\[
a\rightsquigarrow a'\iff a'\rightsquigarrow a,\qquad
a\rightsquigarrow a'\iff -a\rightsquigarrow -a'.
\tag{9}
\]
The first assertion follows by switching the same digits back; the second
by replacing \(\nu\) with \(-\nu\).

For \(p=(x,y)\), a coordinate-switch target is \(p'=(x',y')\) with
\[
x\rightsquigarrow x',\qquad y\rightsquigarrow y',\qquad
Q(x',y')=Q(x,y).
\tag{10}
\]
Both membership and exact norm equality are required. Define \(D\) as
the set of sources admitting such a target outside \(\{p,-p\}\).
Distinct actual targets, not labels, are counted. At zero, positive
definiteness forces the sole equal-norm target to be zero.

We will also allow simultaneous sign, coordinate swap, and **any**
equal-\(Q\) edge whose two endpoints lie in \(\Gamma\). The last class
includes every encoded root rotation and partial conjugation, and even
all their encoded compositions. Let \(R_{\mathrm{cert}}(p)\) be the number
of actual vertices reachable from \(p\) by any finite sequence of these
edges and (10), including \(p\) itself. All vertices are in \(A^2\)
and preserve \(Q\), so
\[
R_{\mathrm{cert}}(p)\le F_A(p).
\tag{11}
\]
We do not include unidentified returns at unencoded sources simply because
their multipliers belong to \(\mu_m\). Such returns remain part of the
unresolved full-fiber problem.

## 4. AMP-R1 — at most four second phases per fixed first source

**PROVED.** Fix two amplitude words \(c,d\), their switches \(u,v\)
from (4), and \(z=c\nu_1\). Write
\[
x=X(z),\quad x'=X(uz),\qquad w=d\nu,\quad
y=Y(w),\quad y'=Y(vw),\quad \nu\in\mu_m.
\]
If \(v\ne\pm1\), at most four choices of \(\nu\) satisfy
\(Q(x',y')=Q(x,y)\).

Indeed, using \(\bar\nu=\nu^{-1}\),
\[
y=\frac{\bar d\nu^{-1}-d\nu}{\Delta},\qquad
y'=\frac{v^{-1}\bar d\nu^{-1}-vd\nu}{\Delta}.
\]
Expand the **whole** difference, including its mixed scalar terms:
\[
Q(x',y')-Q(x,y)
=(x'^2-x^2)+(x'y'-xy)+(y'^2-y^2).
\tag{12}
\]
As a Laurent polynomial in \(\nu\), it has powers from \(-2\) to \(2\).
The coefficient of \(\nu^2\) is
\[
\frac{d^2(v^2-1)}{\Delta^2}\ne0.
\tag{13}
\]
The mixed term has powers only \(-1,1\), and cannot cancel (13).
Multiplication by \(\nu^2\) therefore gives a nonzero polynomial of degree
four. It has at most four roots, which proves the assertion without any
independence assumption on the other coefficients.

If \(v=\tau\in\{1,-1\}\), then \(y'=\tau y\), and instead
\[
Q(x',\tau y)-Q(x,y)
=(x'-\tau x)(x'+\tau x+\tau y).
\tag{14}
\]
If \(x'=\tau x\), the target is precisely \(\tau p\), which is excluded
from \(D\), regardless of how many switch labels represent it.
Otherwise \(y=-\tau x'-x\) is fixed. A fixed \(Y\)-coordinate on the
nonzero norm circle \(d\mu_m\) has at most two phases. Thus at most two
choices produce any remaining norm-equal target. This includes zero
coordinates and nonempty switches that happen to fix an actual scalar.

## 5. AMP-R2 — the entire switched source population is small

There are \((8q)^2\) amplitude-word pairs, at most \(2^r\) switch subsets
per word, and \(6q\) first phases. For each such choice, §4 leaves at
most four second phases that could put the source in \(D\). Hence
\[
\boxed{|D|\le (8q)^2\,4^r\,(6q)\,4
=1536q^3\,4^r.}
\tag{15}
\]
This is an upper count of labels; duplicate source labels only decrease
the number of actual pairs. No uniform scalar representation hypothesis
is used. By (3),
\[
\frac{|D|}{n^2}\le24(4/7)^r\longrightarrow0.
\tag{16}
\]
The count includes independent switches and every norm coincidence they
produce, not just the originally suggested common-factor multiplier.

## 6. AMP-R3 — sign/swap, encoded orbits and iteration do not repair the certificate

The set \(D\) is invariant under simultaneous sign and coordinate swap:
the scalar relation is sign-equivariant, identical in both coordinates,
and \(Q\) has those symmetries. The exclusion of \(\{p,-p\}\) is likewise
preserved under those operations.

The product-word inventory \(Z\) is closed under negation and conjugation.
Under the decoding map, swap sends \(z\) to \(-\omega\bar z\).
Since \(\mu_mZ=Z\), \(\Gamma\) is therefore also invariant under
sign and swap.

If \(p\notin D\cup\Gamma\), every coordinate-switch edge leads only to
\(\pm p\). A sign or swap edge remains in its at-most-four-point
sign/swap orbit, still outside \(D\cup\Gamma\). Encoded edges cannot
be used at those vertices. Induction on path length proves
\[
\boxed{R_{\mathrm{cert}}(p)\le4
\quad\text{for every }p\notin D\cup\Gamma.}
\tag{17}
\]
Consequently
\[
\#\{p:R_{\mathrm{cert}}(p)\le4\}
\ge n^2-1536q^3\,4^r-48q^2,
\tag{18}
\]
\[
\frac{|D\cup\Gamma|}{n^2}
\le24(4/7)^r+\frac{3}{4q^2}=o(1).
\tag{19}
\]
For example \(r\ge8\) suffices for (19) to be below \(1/2\):
\(48\cdot4^7<7^7\), so its first term is at most \(2/7\),
while the second is at most \(3/196\).

In terms of actual \(n\), put
\[
\alpha=\frac{\log(7/4)}{2\log7}>0.
\]
Equations (3) and (19) also give
\(|D\cup\Gamma|=O(n^{2-\alpha})\). This is a small set on which
the certificate might be rich; **\(\alpha\) is not the requested good
fiber-tail exponent**. Almost all sources have bounded certified returns.

## 7. Consequence and exact limit

**FAILED IN STATED SCOPE:** for arbitrary fixed
\(\varepsilon,\delta,C>0\), once \(n^\varepsilon>4\) and
\(n^\delta>2C\), the \(n^2/2\) low-certificate sources contradict
\[
\#\{p:R_{\mathrm{cert}}(p)<n^\varepsilon\}\le Cn^{2-\delta}.
\]
This closes the coordinatewise factor-conjugation certificate, including
all its specified iterations and encoded-orbit enhancements.

**OPEN:** the full-fiber tail for this exact product carrier and its
actual image size. Equation (11) points in the direction that prevents
using (17) as an upper bound on \(F_A\). Targets not supplied by the
defined certificate may still occur. No quadratic image lower bound,
universal factor-method obstruction, or extension of FG-F1 is claimed.

The valid amplitude packing remains an explicit unresolved full-fiber
family, but it has no surviving amplification mechanism in this cycle.
No replacement geometry, matching-classification problem, carrier mutation,
or next proof search is adopted here.
