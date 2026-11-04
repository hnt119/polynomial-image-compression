# Balanced factor products: amplitudes, scalar counts, and exact norm classes

**6 October 2026 · version 1 · T03.** Fixed polynomial
\(Q(x,y)=x^2+xy+y^2\). This is specialist A's sole approved rule in the
authorized offline **Cross-Block Fiber Amplification Beyond Spreading**
cycle. No mathematical program was executed, no network request was made,
and no external theorem or novelty claim is imported. The lead owns the
shared computation budget; this contribution charges zero evaluations and
zero research-program CPU seconds.

The two amplitude rules in the previous
[fiber-growth report](../2026-10-06-fiber-growth/README.md) and FG-O1 remain
frozen. The present support grows with depth; the old 33-frequency
full-fiber obstruction is not applied to it.

| Claim | Status and scope | Locator |
|---|---|---|
| AMP-A1 | PROVED: an explicit convolution recursion with exactly \(8q\) nonzero, pairwise disjoint \(\mu_{6q}\) amplitude cosets | §1 |
| AMP-A2 | PROVED: the exact same-set real completion has \(8q^2\le n\le48q^2\) at every positive depth | §2 |
| AMP-A3 | PROVED: exact encoded norm classes, whole-product partial-conjugation actions, and \(48q^2\) encoded ordered pairs | §3 |
| AMP-A4 | PROVED diagnostic identity: independent coordinate assembly does not commute with a common non-sign multiplier, except on the stated diagonal | §4 |

These claims concern the specified rule. In particular AMP-A4 alone is
**not** a failure of norm equality. The lead's separate norm-equality
count addresses the selected coordinate-switching certificate, including
the possibility that a different multiplier realizes an assembled target.
The full image and unrestricted full-fiber tail of this new carrier remain
**OPEN**. No claim here resolves the fixed T03 target or RC15/4.

## 1. AMP-A1 — one recursive factor rule and its disjoint cosets

### Statement

Fix the digit alphabet \(I=\{-3,-2,-1,0,1,2,3\}\) and the eight
scales \(h\in\{1,\ldots,8\}\) before depth grows. For \(r=k-1\ge0\),
put

\[
q=7^r,\qquad m=6q,\qquad
\xi=\xi_r=e^{2\pi i/q},\qquad
\omega=e^{2\pi i/3},\qquad \Delta=\omega-\omega^2=1+2\omega.
\tag{1}
\]

Choose compatible roots \(\xi_{r+1}^7=\xi_r\). Write
\(H_r=\mathbb Q(\xi_r)\), \(L_r=\mathbb Q(\omega,\xi_r)\), and
\(K_r^+=L_r\cap\mathbb R\). For a word
\(\mathbf i=(i_0,\ldots,i_{r-1})\in I^r\), set

\[
P_{\mathbf i}=\prod_{\ell=0}^{r-1}
 (2-\xi^{i_\ell7^\ell}),\qquad
c_{h,\mathbf i}=hP_{\mathbf i}.
\tag{2}
\]

The empty product at \(r=0\) is 1. A zero digit also contributes 1.
All amplitudes are nonzero. There are exactly \(8q\) amplitude labels,
and their \(\mu_m\) cosets are pairwise disjoint. Hence the actual
encoded complex set

\[
\mathcal Z_r=\bigcup_{h,\mathbf i} c_{h,\mathbf i}\mu_m
\tag{3}
\]

has exactly \(48q^2\) elements. The explicit recursion is

\[
\boxed{c^{(r+1)}_{h,(a,\mathbf i)}
 =(2-\xi_{r+1}^{a})c^{(r)}_{h,\mathbf i},\qquad a\in I.}
\tag{4}
\]

Here \((a,\mathbf i)\) places \(a\) in the new lowest digit and moves
the old digits up one position. Equation (4) uses the same old scalar
through \(\xi_{r+1}^7=\xi_r\).

### Meaning

Multiplication convolves coefficient supports and couples successive
levels. Partial conjugation changes selected factors of the whole product.
This is not the previous complete seven-factor relative norm: no product
over a full seven-element fiber is taken. Nor is this a renamed phased
binomial. If \(s(\mathbf i)\) is the number of nonzero digits, its
coefficient support has exactly \(2^{s(\mathbf i)}\) terms.

### Consequence

The prescribed amplitude inventory is genuine, with no discarded labels
or thinning. This establishes neither Cartesian coverage by encoded pairs
nor a lower tail for arbitrary pairs; those are separate obligations.

### Proof: the exact seven-slot relation

For \(r\ge1\), put \(b=q/7\). The already proved field calculation
[FG-A1](../2026-10-06-fiber-growth/amplitudes.md), §1, gives

\[
\Phi_q(T)=1+T^b+\cdots+T^{6b}
\quad\text{irreducible over }\mathbb Q(\omega).
\tag{5}
\]

That source contains the local Eisenstein proof over
\(\mathbb Z[\omega]\), using its supplied UFD proof. Thus a coefficient
array \((e_a)_{a\bmod q}\) over \(\mathbb Q(\omega)\) evaluates to zero
at \(\xi\) if and only if

\[
e_t=e_{t+b}=\cdots=e_{t+6b}\qquad(0\le t<b).
\tag{6}
\]

Indeed its representative polynomial has degree less than \(q\), so
divisibility by \(\Phi_q\) is equivalent to being \(\Phi_q R\) with
\(\deg R<b\). Equation (6) is an exact algebraic relation, not a
numerical test or an assumption of free Fourier coefficients.

### Proof: support and coefficient recovery

Let \(J=\{\ell:i_\ell\ne0\}\) and \(s=|J|\). Expanding (2) gives

\[
P_{\mathbf i}=\sum_{S\subseteq J}
 (-1)^{|S|}2^{s-|S|}
 \xi^{\sum_{\ell\in S}i_\ell7^\ell}.
\tag{7}
\]

Each exponent has balanced base-seven digits in \([-3,3]\), with digit
either 0 or \(i_\ell\). It lies in
\([-(q-1)/2,(q-1)/2]\), and these balanced expansions are unique.
Consequently all \(2^s\) exponents are distinct modulo \(q\).
Within each seven-slot block of (6), at most two positions occur: the
lower digits determine its residue modulo \(b\), and the top digit has
at most the two choices 0 and \(i_{r-1}\). A cyclic shift of a support
preserves this at-most-two property.

Suppose two amplitude cosets meet. Since
\(\mu_{6q}=\mu_6\mu_q\), there exist
\(\kappa\in\mu_6\) and \(a\bmod q\) with

\[
hP_{\mathbf i}=\kappa\xi^a gP_{\mathbf j}.
\tag{8}
\]

The difference of the coefficient arrays has at most four occupied
positions per seven-slot block. By (6) it must be the zero array:
a nonzero constant block would occupy all seven positions. Thus (8)
is equality of the full cyclic arrays, not merely of their evaluations.

Their support sizes give \(s(\mathbf i)=s(\mathbf j)=s\). In each
array the coefficient with unique largest absolute value is the positive
constant coefficient \(h2^s\), respectively \(g2^s\), arising from
the empty subset. It forces \(a=0\), \(\kappa=1\), and \(h=g\).
For \(s>0\), the coefficients of magnitude \(h2^{s-1}\) are exactly
the singleton terms, and their exponents are
\(i_\ell7^\ell\), \(\ell\in J\). Their balanced representatives
recover the signed digits: each nonzero exponent has 7-adic valuation
\(\ell\), because \(i_\ell\in\{\pm1,\pm2,\pm3\}\).
All other digits are zero. For \(s=0\), both words are already the
zero word. This proves \(\mathbf i=\mathbf j\).

Each factor has absolute value at least 1, so it is nonzero. Every
nonzero complex number has \(6q\) distinct \(\mu_{6q}\) multiples,
proving the count in (3). At \(r=0\), the eight positive rational
amplitudes have distinct absolute values and the conclusion is immediate.

## 2. AMP-A2 — actual scalar input count

### Statement

For any complex \(z\), define the real coordinates

\[
X(z)=\frac{\omega\bar z-\omega^2z}{\Delta},\qquad
Y(z)=\frac{\bar z-z}{\Delta}.
\tag{9}
\]

They satisfy \(z=X(z)-\omega Y(z)\) and
\(N(z)=Q(X(z),Y(z))\). Define the common scalar carrier

\[
A_r=X(\mathcal Z_r)=Y(\mathcal Z_r),\qquad n_r=|A_r|.
\tag{10}
\]

Then \(A_r\subset K_r^+\), \(A_r=-A_r\), \(0\in A_r\), and,
for every \(r\ge1\),

\[
\boxed{8q^2\le n_r\le48q^2,\qquad
\log n_r=2r\log7+O(1).}
\tag{11}
\]

At \(r=0\), \(A_0=\{-8,-7,\ldots,7,8\}\), so \(n_0=17\).
Thus the asymptotic input factor is 49 per level of this recursion.

### Meaning

The count concerns actual scalar values after every projection collision,
not formal factors or amplitudes. One coordinate map is injective on a
large explicitly identified part of the orbit union. Neither coordinate
is asserted injective on the entire complex plane or on \(\mathcal Z_r\).

### Consequence

The encoded pairs have size \(48q^2=\Theta(n_r)\), while the entire
ordered square has size \(\Theta(q^4)\). Large encoded norm fibers
therefore occupy only a vanishing fraction of the requested source square.
This is a coverage deficit, not an upper bound for full fibers.

### Proof

Set

\[
B_r=\{h\xi^aP_{\mathbf i}:1\le h\le8,
\ a\in\mathbb Z/q,\ \mathbf i\in I^r\}\subset H_r.
\tag{12}
\]

AMP-A1 gives \(|B_r|=8q^2\) and \(\mathcal Z_r=\mu_6 B_r\).
Complex conjugation sends \((a,\mathbf i)\) to \((-a,-\mathbf i)\),
so \(\bar B_r=B_r\). Direct substitution in (9) shows
\(Y(z)=X(\omega z)\). Therefore the two projection sets agree, and
the exact unit-orbit completion is

\[
A_r=\{\pm X(z),\ \pm Y(z),\ \pm(X(z)+Y(z)):z\in B_r\}.
\tag{13}
\]

This proves the upper bound, symmetry and common-set membership. Taking
\(z=h\) gives \(Y(z)=0\), proving that 0 is present.

For the lower bound, the degree calculation in FG-A1 gives
\([H_r:\mathbb Q]=6\cdot7^{r-1}\) and
\([L_r:\mathbb Q]=12\cdot7^{r-1}\), hence \(\omega\notin H_r\).
If \(z,w\in H_r\) and \(X(z)=X(w)\), put \(v=z-w\). Equation (9)
gives \(\bar v=\omega v\). If \(v\ne0\), this would put
\(\omega=\bar v/v\) in \(H_r\), a contradiction. Thus \(X\) is
injective on \(H_r\), and in particular
\(|X(B_r)|=8q^2\). This proves (11).

At the seed, the decoded coordinates of \(h\mu_6\) are exactly
\(0,\pm h\). The claimed seed carrier follows without an experiment.

## 3. AMP-A3 — encoded norm classes and whole-product targets

### Statement

Two amplitudes have equal norm precisely when their scales and absolute
digit words agree:

\[
N(c_{h,\mathbf i})=N(c_{g,\mathbf j})
\quad\Longleftrightarrow\quad
h=g\ \text{ and }\ |i_\ell|=|j_\ell|\text{ for every }\ell.
\tag{14}
\]

There are exactly \(8\cdot4^r\) encoded norm values. For an absolute
digit word with \(s\) nonzero digits, its fiber inside \(\mathcal Z_r\)
has exactly

\[
6q\,2^s
\tag{15}
\]

distinct complex points. These decode to the same number of distinct
ordered pairs in \(A_r^2\). The total encoded source inventory is
exactly \(48q^2\).

For \(S\subseteq\{\ell:i_\ell\ne0\}\), let

\[
P_S=\prod_{\ell\in S}(2-\xi^{i_\ell7^\ell}),\qquad
u_S=\frac{\bar P_S}{P_S}.
\tag{16}
\]

Then \(N(u_S)=1\), and the exact whole-product action is

\[
u_S c_{h,\mathbf i}=c_{h,\mathbf i^S},
\tag{17}
\]

where \(\mathbf i^S\) flips the signs in \(S\). For a nonempty
\(S\), \(u_S\notin\mu_{6q}\), in particular \(u_S\ne\pm1\).
Equation (17), together with the phase action, reaches every encoded
target counted in (15).

### Meaning

This is actual whole-scalar norm preservation with exact target
membership, and the nonempty factor switches produce actions beyond the
cyclic phase group. It has increasing encoded fibers. The statement is
deliberately restricted to the encoded union; it does not assert that
these are the only targets of any source in the full Cartesian square.

### Consequence

For an encoded nonzero source, (15) is a valid lower bound for its full
fiber. It is not an equality for the full fiber. Distinct switch words
give distinct encoded targets by AMP-A1, so no formal action multiplicity
is counted as a gain. The encoded norm count \(8\cdot4^r\) is not an
upper bound for \(|Q(A_r,A_r)|\).

### Proof of the exact norm classification

Writing \(J=\{\ell:i_\ell\ne0\}\), one has

\[
N(c_{h,\mathbf i})
=h^2\prod_{\ell\in J}
 (5-2\xi^{i_\ell7^\ell}-2\xi^{-i_\ell7^\ell}).
\tag{18}
\]

The exponents use the balanced digits
\(0,i_\ell,-i_\ell\). As in (7), they are distinct modulo \(q\).
This gives exactly \(3^{|J|}\) support positions, with at most three
positions in each seven-slot block. In an equality of two expressions
(18), the difference has at most six positions per block. Equation (6)
therefore forces equality of their full cyclic coefficient arrays.

Support size first recovers \(s=|J|\). The unique coefficient of
largest absolute value is the positive constant \(h^25^s\); hence
the positive scale \(h\) is recovered. The coefficients of magnitude
\(2h^25^{s-1}\) occur exactly at the singleton positions
\(\pm i_\ell7^\ell\). More generally, using \(j\) nonconstant
terms gives magnitude \(h^22^j5^{s-j}\), so no other layer has that
magnitude. Balanced representatives and their 7-adic valuations recover
\(|i_\ell|\) at every level. The case \(s=0\) is immediate.
Conversely (18) is unchanged by each digit sign flip. This proves (14).

Each absolute digit is one of \(0,1,2,3\), giving \(4^r\) words
for each scale. There are \(2^s\) sign choices for a word with \(s\)
nonzero entries, and their \(\mu_{6q}\) orbits are disjoint by
AMP-A1. This proves (15). The real-linear decoding (9) is a bijection
between the complex plane and real ordered pairs, so this counts actual
encoded pairs as well.

Equation (17) is cancellation in the whole product; all denominators
are nonzero. If its nonempty switch had \(u_S\in\mu_{6q}\), the
distinct words \(\mathbf i\) and \(\mathbf i^S\) would have the
same amplitude coset, contrary to AMP-A1.

## 4. AMP-A4 — assembly and the scope of the switching certificate

### Statement

Every pair in \(A_r^2\) admits a representation
\((x,y)=(X(z),Y(w))\), with \(z,w\in\mathcal Z_r\). Its whole
complex scalar is

\[
T(z,w)=X(z)-\omega Y(w)
=\frac{-\omega^2z+\omega\bar z+\omega w-\omega\bar w}{\Delta}.
\tag{19}
\]

For every norm-one \(u\),

\[
\boxed{uT(z,w)-T(uz,uw)
=\frac{\omega(u-u^{-1})(\bar z-\bar w)}{\Delta}.}
\tag{20}
\]

Thus the intended coordinatewise target
\((X(uz),Y(uw))\) is the target of that same whole-source multiplier
\(u\) if and only if \(u=\pm1\) or \(z=w\).

For a common factor switch, require that the first and second amplitude
words have the same nonzero digits on \(S\); then (16) uses those
common factors and sends both \(z,w\) into \(\mathcal Z_r\).
This proves membership of the two proposed target coordinates in \(A_r\).
It does not by itself prove their joint norm equality. Independently
switching the two words also proves separate coordinate membership, with
the same norm-equality obligation remaining.

### Meaning

The actual source for a Cartesian pair is (19), not either encoded
factor product separately. In general (19) has no factorization supplied
by (2). The switch identity (17) cannot be applied to (19) merely because
its two coordinate representatives share factors.

### Consequence and exact limit

Equation (20) disproves the proposed **same-multiplier** identity away
from its specified locus. It does not show that the assembled target has
a different norm: a different multiplier could realize it. The final
certificate audit must therefore test

\[
Q(X(uz),Y(vw))=Q(X(z),Y(w))
\tag{21}
\]

directly, for the permitted switches \(u,v\). The lead's phase-count
argument and its independent review are recorded in this cycle's report
and [audit companion](audit.md). They concern this selected switching
certificate, not all norm-preserving maps on \(A_r^2\).

### Proof

Equation (19) is substitution of (9). Since \(\bar u=u^{-1}\),
substituting \(uz,uw\) into (19) and subtracting from \(uT(z,w)\)
leaves exactly the right side of (20). The factors \(\omega,\Delta\)
are nonzero, and \(u-u^{-1}=0\) is equivalent to \(u=\pm1\).
This proves the stated equivalence. Membership under the factor switches
is (17) with unchanged phase, applied separately where necessary.

The scalar switch relation is compatible with the two coordinate charts:
\(Y(z)=X(\omega z)\), \(\mathcal Z_r\) is \(\mu_6\)-stable,
and scalar multiplication commutes with \(\omega\). It is reversible
(flip the same digit signs again) and sign-equivariant. These facts may
be used when auditing iterated selected certificates. Nonempty switch
labels that fix an actual projected coordinate create no new target.

## 5. Construction ledger and disposition

This ledger follows
[CONSTRUCTION_LEDGER.md](../../templates/CONSTRUCTION_LEDGER.md).
The growing parameter is the actual recursion depth \(r\); the digit
alphabet, eight scales, polynomial, and prime are fixed first.

| Gain or cost | Exact bound or status | Source and scope |
|---|---|---|
| Formal amplitude inventory | \(8\cdot7^r=8q\) | (2), with all labels distinct modulo \(\mu_{6q}\) |
| Actual encoded points/pairs | \(48q^2\) | AMP-A1 and real-linear decoding; no zero encoded point |
| Actual scalar inputs | \(8q^2\le n\le48q^2\), \(r\ge1\) | AMP-A2; seed \(n_0=17\) |
| Input thinning, charged twice | None | No scalar or pair thinning is used; all of \(A^2\) remains required |
| Parameter and projection fibers | Orbit parametrization injective; \(X\) injective on \(B_r\), other projected coincidences allowed | Lower and upper counts already charge every projection collision |
| Encoded norm values | \(8\cdot4^r\) | AMP-A3; restricted to \(\mathcal Z_r\) |
| Encoded fiber of a word with \(s\) nonzero digits | \(6q2^s\) distinct targets | Exact only inside \(\mathcal Z_r\); a full-fiber lower bound there |
| Local moduli and splitting | Fixed prime 7; exact seven-slot relation | The irreducibility/splitting input is inherited with its proof locator; no new prime selection |
| Local populations and carries | Supports \(2^s\) for amplitudes, \(3^s\) for norms; at most 2 or 3 positions per seven-slot block | Balanced digits prove no exponent collisions; (6) charges the cyclotomic relations |
| Field degree | \([L_r:\mathbb Q]=12\cdot7^{r-1}\), \([K_r^+:\mathbb Q]=6\cdot7^{r-1}\) | For \(r\ge1\); not fixed as \(r\) grows |
| Discriminant, regulator, units | No counting theorem involving these invariants is used | No zero-cost asymptotic theorem is inferred from their omission; any later such use needs its own bounds |
| Integral normalization | All amplitudes algebraic integers; \(3A_r\subset\mathcal O_{K_r^+}\) | From (9) and \(1/\Delta=-\Delta/3\); fixed scalar denominator only |
| Action denominators | Exact ratios \(\bar P_S/P_S\), with nonzero denominator | At every complex embedding \(1\le\lvert P_S\rvert\le3^{\lvert S\rvert}\); no uncontrolled division or rational-lattice model is invoked |
| Heights and archimedean radius | Every amplitude conjugate has magnitude at most \(8\cdot3^r\); every scalar conjugate at most \((16/\sqrt3)3^r\) | Each factor magnitude lies in \([1,3]\), and (9) gives the scalar bound |
| Action distortion | \(\lvert u_S\rvert=1\), and the same holds in every complex embedding | Each embedding commutes with complex conjugation; this does not imply coordinate membership beyond the proved domains |
| Branch count | At most \(2^r\) switch choices per word and \(4^r\) independent switch pairs | Counts are labels until target equality/deduplication is checked |
| Encoded coverage | \(48q^2/n^2=O(q^{-2})\) | Leaves \(n^2-48q^2\) actual source pairs outside the encoded union |
| Exceptional and uncovered outputs | No saving proved | Unencoded pairs may still have collisions; they cannot be discarded or charged zero outputs |
| Input rates | \(a=B=2\log7\) per depth \(r\) | Equation (11) with fixed multiplicative constants |
| Entire output exponent | Only \(\lvert Q(A_r,A_r)\rvert\le n^2\) here | Encoded image count is not substituted for the full image |
| Certified net gap | \(\delta=0\) from the trivial full-image bound | No fixed positive compression exponent follows from these claims |
| Computation, seeds, runtime, hashes | Not applicable: no script or data artifact used | Symbolic proofs only, zero mathematical evaluations/CPU; no hidden scout |

### Evidence and review provenance

The seven-slot and field-degree inputs were read from the identified
complete proof in the frozen predecessor; they are not reconstructed from
its status summary. The new coefficient-recovery, input-injectivity,
encoded-norm, and action identities are proved in this note. Specialist C
independently audited the complete written AMP-A1–AMP-A4 proofs on
6 October 2026 and returned PASS, including the exact norm classification,
seed, counts, recursion, and diagnostic-only scope of (20). The lead
independently supplied and checked the stronger \(8q^2\) input lower
bound; the lead's final acceptance is recorded in the cycle report.
All reviews are internal, not external review or a literature check.

### Disposition

The structural claims AMP-A1–AMP-A3 pass. The same-multiplier assembly
claim fails in precisely the scope of AMP-A4. The additional direct
norm-equality audit, rather than (20) alone, controls the final rejection
of the selected coordinate-switching certificate. The actual full image
and unrestricted return tail of this carrier are **OPEN**. This note
authorizes no mutation, third rule, further experiment, or automatic
continuation of that open question.
