# One tower level controls complete balanced-factor fibers

**11 October 2026 · version 1 · T03 · approach 1.** Fixed polynomial
\(Q(x,y)=x^2+xy+y^2\). This note addresses only the unchanged
balanced-factor carrier and its precise full-fiber obligation BFF-O1.
All arguments are symbolic and offline. This author used no mathematical
program, no network, and no nested agent; the allocation is zero
evaluations and zero research-program CPU seconds.

The controlling sources are the
[frozen BFF-O1 statement](../2026-10-11-balanced-full-fibers/README.md), §7,
the complete [BFF-A1–A3 algebra](../2026-10-11-balanced-full-fibers/algebra.md),
and the [AMP-A1–A3 amplitude proof](../2026-10-06-cross-block-amplification/amplitudes.md).
The finite-family algebra input is the new, fully written
[projection/localization lemma E1–E4](elimination.md).
No 33-frequency theorem or fixed-support assumption is used.

| Claim | Statement and exact scope | Locator |
|---|---|---|
| BFO-T1 | PROVED: a fixed list of 49 local spaces covers every completed scalar target, with all tower carries retained | §§1–2 |
| BFO-T2 | PROVED: at least 1344 of the 2401 ordered local source types have quadratic Jacobian rank four | §3 |
| BFO-T3 | PROVED: bounded-degree exceptional polynomials meet the actual predecessor \(B^2\) in a vanishing fraction, uniformly in their coefficients | §4 |
| BFO-T4 | PROVED from E1–E4 and BFO-T1–T3: at every sufficiently large depth, at least \(32q^4\) actual \(B^2\) sources have a fixed constant bound on their complete \(V^2\) fibers | §5 |

Specialist C independently audited the complete written E1–E4 lemma and
this BFO-T1–T4 application on 11 October 2026 and returned PASS, with no
correction. The review covered all target types, the degree-seven carries,
the actual source count and the exact half-population threshold. The
lead's final acceptance and status change are recorded separately.
No exact numerical fiber constant or starting depth is asserted.

## 1. Exact carrier and one-level coordinates

Write \(q=7^r\), \(\xi_r=e^{2\pi i/q}\),
\(\omega=e^{2\pi i/3}\), and \(\Delta=1+2\omega\). The carrier
has amplitudes

\[
c_{h,\mathbf i}=h\prod_{\ell=0}^{r-1}
 (2-\xi_r^{i_\ell7^\ell}),\qquad
1\le h\le8,\quad i_\ell\in\{-3,-2,-1,0,1,2,3\}.
\tag{1}
\]

Use the exact scalar description

\[
\begin{aligned}
B_r&=\{\xi_r^a c_{h,\mathbf i}:a\bmod7^r\},\\
D_r&=\{\bar b-b:b\in B_r\},\\
V_r&=B_r\mathbin{\dot\cup}(-B_r)\mathbin{\dot\cup}D_r,\\
A_r&=X(V_r),\qquad
X(z)=\frac{\omega\bar z-\omega^2z}{\Delta}.
\end{aligned}
\tag{2}
\]

BFF-A1 proves that \(X:V_r\to A_r\) is bijective and

\[
|B_r|=8q^2,\qquad
16q^2+1\le n_r=|A_r|\le24q^2-7.
\tag{3}
\]

Take \(r\ge2\), put \(j=r-1\), \(Q_0=7^j=q/7\), and set
\(\alpha=\xi_r\), \(\eta=\alpha^7=\xi_j\). Every element of
\(B_r\) has a unique decomposition

\[
v=g_{a,i}(\alpha)b,\qquad
g_{a,i}(T)=T^a(2-T^i),\quad
0\le a\le6,\quad -3\le i\le3,\quad b\in B_j.
\tag{4}
\]

Indeed split the phase exponent into its lowest base-seven digit \(a\)
and its remaining digits, and separate the factor with \(\ell=0\)
from (1). The remaining factors and phase are precisely a point of
\(B_j\). Uniqueness follows from the inherited disjoint amplitude
cosets and phase uniqueness. Thus the 49 local labels are equally sized
disjoint parts of \(B_r\); no labels are counted twice.

### Carry accounting

The expressions in (4) are Laurent polynomials. Whenever an exponent
\(e\) is reduced to \(s\in\{0,\ldots,6\}\), the exact rule is

\[
\alpha^e=\eta^{(e-s)/7}\alpha^s.
\tag{5}
\]

Negative exponents and the cases \(a+i<0\) or \(a+i>6\) therefore
carry explicit powers of \(\eta\). No carry coefficient is discarded.
Conjugation uses \(\bar\alpha=\alpha^{-1}\) and
\(\bar\eta=\eta^{-1}\).

The inherited field degrees give

\[
[\mathbb Q(\omega,\alpha):\mathbb Q(\omega,\eta)]=7
\qquad(r\ge2).
\tag{6}
\]

Thus \(1,\alpha,\ldots,\alpha^6\) is a genuine basis over the
predecessor field. This is consistent with every seven-slot relation:
relations involving the predecessor root are inside the coefficient
field, whereas the seven displayed tower coordinates are independent.
The total product supports may grow as \(2^r\); that does not change
the seven-coordinate description of the last tower step.

## 2. BFO-T1 — one fixed finite list covers all targets

For uniform algebra, introduce a transcendental parameter \(\tau\),
put

\[
k=\mathbb Q(\omega),\qquad F=k(\tau),\qquad
E=F[\alpha]/(\alpha^7-\tau).
\tag{7}
\]

This is a degree-seven field extension: \(T^7-\tau\) is Eisenstein
at the prime \(\tau\) in \(k[\tau]\). Use the involution
\(\omega\mapsto\omega^2\), \(\tau\mapsto\tau^{-1}\),
\(\alpha\mapsto\alpha^{-1}\) to define \(\bar g\). It is not
asserted to fix \(F\); the resulting \(g,\bar g\) are simply two
specified elements of \(E\). For each of the 49 labels in (4), put

\[
U_g=\operatorname{span}_F\{g,\bar g\}\subset E.
\tag{8}
\]

Define a polynomial map with four free formal variables by taking the
seven basis coordinates of

\[
\Psi_{g,h}(u_1,u_2,u_3,u_4)
=Q(gu_1+\bar g u_2,\;hu_3+\bar h u_4).
\tag{9}
\]

There are exactly \(49^2=2401\) maps in this finite list, each of
degree at most two. All coefficients belong to \(k(\tau)\), with
the carry factors prescribed by (5).

### All completed targets are covered

After \(\tau=\eta\), the coefficient field is
\(L_j=\mathbb Q(\omega,\eta)\). If \(b\in B_j\), then

\[
X(gb)=\left(-\frac{\omega^2}{\Delta}\right)gb
       +\left(\frac{\omega}{\Delta}\right)\bar g\bar b
\in U_g.
\tag{10}
\]

Its negative also lies in \(U_g\). For the third completed piece,

\[
X(\overline{gb}-gb)=Y(gb)
=-\frac{1}{\Delta}gb+\frac{1}{\Delta}\bar g\bar b
\in U_g.
\tag{11}
\]

Every target scalar in \(A_r=X(V_r)\) is therefore in one of the
49 specialized spaces. Every ordered target pair in **all** \(A_r^2\)
occurs among the parameters of at least one map (9).

This enlarges each target piece to a linear space over \(L_j\); it
does not restrict the targets to encoded pairs or to a selected action.
The many possible parents of an element of \(D_r\) cause no loss:
counting all parameter solutions is an upper bound for the number of
actual target pairs. If a local space has dimension one, its map (9)
has redundant parameters; the lower-rank part of E1 handles this case
rather than assigning an injectivity assumption to it.

## 3. BFO-T2 — a majority of source types have rank four

Split the seven-dimensional vector space \(E\) as

\[
E=E_0\oplus E_1\oplus E_2\oplus E_3,
\quad E_0=F,\quad E_t=\operatorname{span}_F\{\alpha^t,\alpha^{-t}\}
\ (1\le t\le3).
\tag{12}
\]

The dimensions are \(1,2,2,2\). Reduction modulo seven, with (5),
shows directness. For a local label \((a,i)\), put
\(p=a\bmod7\) and \(s=a+i\bmod7\). The assignment
\((a,i)\mapsto(p,s)\) is a bijection onto the 49 ordered residue
pairs: each residue difference has exactly one representative in
\(\{-3,\ldots,3\}\).

Partition these labels into four classes. A nonzero residue belongs to
one of the three absolute classes \(\{t,-t\}\).

| Local class | Residue condition | Number | Property of \(U_g\) |
|---|---|---:|---|
| Z | \(p=s=0\) | 1 | One-dimensional |
| W | \(p,s\) belong to the same nonzero absolute class | 12 | Exactly \(E_t\) |
| C | \(p,s\) belong to different nonzero absolute classes | 24 | Two-dimensional in \(E_t\oplus E_u\); projection to either summand is injective |
| O | Exactly one of \(p,s\) is zero | 12 | Two-dimensional in \(E_0\oplus E_t\); projection to \(E_t\) is injective |

### Proof of the local-space assertions

In class W with \(p=s\), the digit is zero, so \(g=\alpha^p\)
up to a nonzero coefficient-field factor, and \(g,\bar g\) span
\(E_t\). In the other W case, after removing a common nonzero
carry factor, the two vectors have the form

\[
2\alpha^t-\lambda\alpha^{-t},\qquad
2\alpha^{-t}-\lambda^{-1}\alpha^t,
\quad \lambda=\tau^e\ne0.
\tag{13}
\]

Their determinant is \(4-1=3\), so they again span \(E_t\).
The same argument applies with \(t\) and \(-t\) interchanged.

In class C, \(g\) has one nonzero coordinate in each of two
different absolute classes, and \(\bar g\) has the respective
opposite coordinates. Both coefficients are nonzero. Projection to
either two-dimensional summand is therefore an isomorphism. In class O,
the two projected nonzero-class coordinates are again opposite and
nonzero, proving the stated injectivity. This proof retains arbitrary
nonzero carry powers \(\tau^e\).

### The count of disjoint source spaces

Fix a class-C source label supported on \(E_t\oplus E_u\). Its
space has zero intersection with:

- all 12 class-W spaces: even if the W space is \(E_t\) or
  \(E_u\), injectivity of the projection to the other summand forces
  the intersection to be zero;
- all 12 class-O spaces: the C space has no \(E_0\) component, and
  its projection to the other occupied nonzero summand again forces
  zero whenever one nonzero class is shared;
- the 16 class-C labels supported on a different unordered pair of
  nonzero classes: each has an exclusive summand, and projection to
  that summand is injective.

Thus each of the 24 C labels has at least 40 admissible second labels.

Fix next a class-W source label, whose space is \(E_t\). It has
zero intersection with all 24 C spaces and with the eight W labels in
the other two nonzero classes. This supplies at least 32 second labels
for each of 12 W labels. The two first-label classes are disjoint, so
these are at least

\[
\boxed{24\cdot40+12\cdot32=1344}
\tag{14}
\]

different ordered local source types. Both spaces in every counted pair
have dimension two and have zero intersection. No assertion about the
remaining local types is needed.

### Jacobian rank

For one of these pairs, evaluate the differential of (9) at
\((u_1,u_2,u_3,u_4)=(1,0,0,0)\), so the scalar arguments are
\((g,0)\). Its columns, as elements of \(E\), are

\[
2g^2,\quad2g\bar g,\quad gh,\quad g\bar h.
\tag{15}
\]

The element \(g\) is nonzero in the field \(E\), so multiplication
by \(g\) is invertible. The columns in (15) are independent exactly
when \(g,\bar g,h,\bar h\) are independent. This holds for all
1344 counted types by the disjointness just proved. Their maps have
Jacobian rank four over \(k(\tau)\).

This is a one-level rank statement. It does not repeatedly incur a
branching factor at each predecessor depth.

## 4. BFO-T3 — actual predecessor labels avoid bounded-degree exceptions

### One parent variable

Let \(j\ge0\), \(Q_0=7^j\), and \(N=|B_j|=8Q_0^2\).
For any nonzero polynomial \(P(Z,W)\in\mathbb C[Z,W]\) of total
degree at most \(d\), define

\[
T_d(j)=16dQ_0+\lfloor d/2\rfloor Q_0 2^j.
\tag{16}
\]

Then, uniformly in every coefficient of \(P\),

\[
\boxed{\#\{b\in B_j:P(b,\bar b)=0\}\le T_d(j).}
\tag{17}
\]

If \(d=0\), both sides have the asserted interpretation: a nonzero
constant has no zeros and \(T_0(j)=0\).

**Proof.** Every point of \(B_j\) lies on the circle of one of its
\(8Q_0\) amplitude labels, so there are at most \(8Q_0\) circles.
On a circle of radius \(\rho>0\), substitute
\(Z=\rho u\), \(W=\rho u^{-1}\). If the resulting Laurent
polynomial is nonzero, its powers lie between \(-d\) and \(d\),
so it has at most \(2d\) nonzero complex roots. In particular it
vanishes at at most \(2d\) actual points on that circle.

If that restriction is identically zero, then
\(ZW-\rho^2\) divides \(P\). One direct proof is to reduce each
mixed monomial modulo \(ZW-\rho^2\), replacing a factor \(ZW\)
by \(\rho^2\) until only a pure power of \(Z\) or of \(W\)
remains. Substitution gives distinct positive and negative Laurent
powers, so an identically zero restriction has zero reduced remainder.
For distinct radii these factors are coprime, since their difference is
a nonzero constant. Their product therefore divides \(P\), and there
are at most \(\lfloor d/2\rfloor\) such entire circles.

AMP-A3 classifies every actual norm class: a fixed scale and absolute
digit word with \(s\) nonzero digits has exactly \(Q_0 2^s\)
points in \(B_j\). The factor is \(Q_0\), not \(6Q_0\), because
\(B_j\) uses only its \(\mu_{Q_0}\) phases. Thus any circle
contains at most \(Q_0 2^j\) points. The non-identical restrictions
contribute at most \((8Q_0)(2d)\), and the entire circles contribute
at most \(\lfloor d/2\rfloor Q_0 2^j\). This proves (17).

### Two parent variables with their conjugates

For a nonzero
\(P(Z_1,W_1,Z_2,W_2)\in\mathbb C[Z_1,W_1,Z_2,W_2]\) of total
degree at most \(d\),

\[
\boxed{\#\{(b,c)\in B_j^2:P(b,\bar b,c,\bar c)=0\}
\le2N T_d(j).}
\tag{18}
\]

To prove this, expand in \(Z_2,W_2\) and choose one nonzero
coefficient polynomial in \(Z_1,W_1\). At most \(T_d(j)\)
choices of \(b\) make that coefficient vanish, by (17). Charge all
\(N\) choices of \(c\) for these exceptional \(b\). For every
other \(b\), the specialized polynomial in \(Z_2,W_2\) is nonzero,
so at most \(T_d(j)\) choices of \(c\) vanish. This yields (18).

In particular,

\[
\frac{2N T_d(j)}{N^2}
=\frac{T_d(j)}{4Q_0^2}
\le\frac{4d}{7^j}+\frac{d}{8}\left(\frac27\right)^j
\longrightarrow0.
\tag{19}
\]

The coefficients may depend arbitrarily on the specialized predecessor
root \(\eta\), and their magnitudes need not be bounded. The degree
bound alone controls (19). Thus no archimedean height or distortion
estimate is hidden in this exceptional-set argument.

## 5. BFO-T4 — application to every complete target fiber

Apply E1 with \(k=\mathbb Q(\omega)\), parameter \(\tau\),
domain dimension four, output dimension seven, and the entire list of
2401 maps (9). The source sublist consists of the 1344 maps in (14).
All of these have rank four. E1 gives fixed integers \(M\ge1,d\ge0\),
a nonzero specialization polynomial, and a nonzero exceptional
polynomial of degree at most \(d\) for each source map.

By E4 and the inherited cyclotomic degree formula, every sufficiently
large specialization \(\tau=\eta=\xi_j\) is allowed. Indeed
\([\mathbb Q(\omega,\eta):\mathbb Q(\omega)]=6\cdot7^{j-1}\)
for \(j\ge1\); this eventually exceeds the degree of the fixed
nonzero specialization polynomial. This removes only an initial segment
of depths.

### The conjugate parent parameters do not defeat nonvanishing

For an actual source \(v=gb,w=hc\) in one counted type, its four
parameters in (9) are

\[
\left(-\frac{\omega^2}{\Delta}b,
       \frac{\omega}{\Delta}\bar b,
       -\frac{\omega^2}{\Delta}c,
       \frac{\omega}{\Delta}\bar c\right).
\tag{20}
\]

The diagonal constants are nonzero. Substituting the formal variables
\((Z_1,W_1,Z_2,W_2)\) for \((b,\bar b,c,\bar c)\) in (20)
is an invertible linear substitution, so the exceptional polynomial from
E1 remains a nonzero polynomial of degree at most \(d\). Conjugacy
does not create an identity: the further substitution
\((Z,W)=(x+iy,x-iy)\) is also invertible over \(\mathbb C\).
The exact count on the actual finite parent set is then supplied by
(18), rather than by a presumption that its points are generic.

Consequently, for each of the 1344 source types, at least

\[
N^2-2N T_d(j)
\tag{21}
\]

actual parent pairs have at most \(M\) parameter targets in the
union of all 2401 target maps. Their full actual \(A_r^2\) fibers
are at most \(M\) by §2. The parent parametrization in (4) is
injective, so the source count in (21) is an actual count and different
local source types do not overlap.

Let \(\varepsilon_j=2T_d(j)/N\), which tends to zero by (19).
The total number of good sources in \(B_r^2\) is at least

\[
1344(1-\varepsilon_j)N^2.
\tag{22}
\]

Since \(1344>2401/2\), every sufficiently large \(j\) has

\[
1344(1-\varepsilon_j)\ge2401/2.
\tag{23}
\]

For example it suffices that
\(\varepsilon_j\le287/2688\); no explicit depth is required.
As \(|B_r|=49N=8q^2\), equations (22)–(23) prove

\[
\boxed{\#\{(v,w)\in B_r^2:F_{A_r}(X(v),X(w))\le M\}
\ge \tfrac12|B_r|^2=32q^4}
\tag{24}
\]

at every sufficiently large depth.

### BFF-O1 and the actual image

BFF-A2 gives exact equivalence between a full quadratic fiber and

\[
\mathcal K(s,t)=\mathcal K(v,w),\qquad (s,t)\in V_r^2,
\]

where
\(\mathcal K(v,w)=M_0(v,v)+M_0(v,w)+M_0(w,w)\) and
\(M_0(v,w)=2vw+v\bar w+\bar v w-\bar v\bar w\).
Here \(M_0\) is the inherited bilinear form; it is distinct from
the fixed fiber bound \(M\) in (24). Thus (24) proves BFF-O1:
take its exponent \(C=1\) and enlarge the starting depth until
\(r+1\ge M\). The target count in (24) already ranges over all
\(V_r^2\), not only \(B_r^2\).

In fact the constant bound is stronger. Each output touched by the good
source population contains at most \(M\) such sources, so

\[
\boxed{|Q(A_r,A_r)|\ge\frac{32q^4}{M}
\ge\frac{n_r^2}{18M}.}
\tag{25}
\]

Together with the trivial upper bound \(n_r^2\), this gives actual
image size \(\Theta(n_r^2)\) at every sufficiently large depth for
this exact carrier. It excludes a fixed positive power saving on any
unbounded subsequence of this carrier. It makes no assertion about the
unrestricted T03 construction problem or any other amplitude family.
No exact constant-fiber classification is claimed.

## 6. Accounting and why the recursive difficulty is avoided

The original tower reconstruction attempt would produce seven coupled
quadratic equations in predecessor elements and their conjugates. Those
equations do not automatically descend to a single predecessor
\(\mathcal K\)-fiber; paying a fixed branch factor at each depth would
also be exponential rather than polynomial. The argument above instead
uses only the last tower level. The entire predecessor word is a parameter,
and a fixed finite family of polynomial maps supplies the uniform bound.

| Item | Charge and scope |
|---|---|
| Carrier or amplitude change | None; (1) is frozen |
| Actual inputs | \(16q^2+1\le n_r\le24q^2-7\), after every scalar identification |
| Source count | At least half of the actual \(B_r^2\), hence \(32q^4\); no selected-action substitute |
| Target completion | All \(\pm B_r\) and \(D_r\) covered by the 49 spaces; all ordered pairs included |
| Target projection multiplicity | Enlarging to arbitrary local coefficients can overcount targets; it cannot omit them |
| Source multiplicity | The 49-way decomposition is injective; no source label gain |
| Carries and cyclotomic relations | Powers of \(\eta\) retained by (5); the independent degree-seven basis is justified by (6) |
| Growing product support | Absorbed into actual predecessor parameters; never replaced by a bounded support assumption |
| Field and denominator costs | The previous explicit carrier ledger remains in force; \(1/\Delta\) is fixed, and all rational-function specialization poles are excluded by E4 |
| Heights, discriminant and regulator | No counting theorem involving them is used; the zero-count bound is uniform in polynomial coefficients |
| Exceptional sources | At most \(2N T_d(j)\) per counted type, a proved \(o(N^2)\) fraction |
| Exceptional depths | Only a finite initial segment, from fixed polynomial specialization and (23) |
| Final full-fiber bound | A fixed \(M\), existing by the proved finite-family lemma; no numerical value is asserted |
| Entire image | Actual lower bound (25), not a failed support-upper certificate |
| Computation | None by this specialist; no finite histogram or rank enumeration was run |

The identified E1 lemma and this companion have passed the recorded
independent internal audit. Together they prove the stated scoped carrier
obstruction. No novelty claim, external review, new carrier, extra
approach, or broader impossibility statement is inferred.
