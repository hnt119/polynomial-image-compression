# MS-O1: exponential relative order-unit population

21 October 2026 · T03 / unchanged mixed-signature carrier · version 1.
Fixed polynomial \(Q(x,y)=x^2+xy+y^2\).

**Result — PROVED from the stated arithmetic inputs.** The relative
order-logarithm lattice has covolume at most \(K_R^{d_j}\), with the explicit
fixed constant below. Consequently one fixed scalar radius \(T_*\) gives
\[
 |U_j(T_*)|\ge 2^{d_j}
 \quad\text{at every tower level.}
 \tag{1}
\]
This proves the action-population gate MS-O1. It does not prove that these
units return on a typical source, a return-tail estimate, or a small
complete quadratic image.

The lead derived the covering argument in §§3–5. The relative-unit
specialist independently challenged its steps and constants, then wrote this
complete proof. No mathematical program, enumeration, network request, new
field, new seed, or changed scalar carrier was used.

## 1. Fixed objects, inherited results, and source boundary

Use exactly the fields and order from the
[20 October field-unit proof](../2026-10-20-mixed-signature/field-units.md):
\[
 F=F_j,\quad [F:\mathbb Q]=d,\qquad
 K=F(s),\quad s^3+s+1=0,\qquad E=K(\omega),\qquad
 R=\mathcal O_K[\omega].
 \tag{2}
\]
The chosen \(s\) and chosen embedding of \(K\) are real; \(F\) is totally real.
The relative involution \(\tau\) fixes \(K\) and sends \(\omega\) to
\(\omega^2\). Write
\[
 D_*=D_0\,31^{1/3},\qquad D_E=\sqrt3\,D_*.
 \tag{3}
\]
MS-F1 proves
\[
 [K:\mathbb Q]=3d,\quad \operatorname{sig}(K)=(d,d),\qquad
 [E:\mathbb Q]=6d,\quad \operatorname{sig}(E)=(0,3d),\qquad
 \operatorname{rd}(E)\le D_E .
 \tag{4}
\]
The parameter \(D_0\), the field tower, and all constants below are fixed
before \(j\) grows.

Let
\[
 \mathcal U_E^1=\{u\in\mathcal O_E^\times:u\tau(u)=1\},\qquad
 \mathcal U_R^1=\mathcal U_E^1\cap R^\times.
 \tag{5}
\]
Choose one representative \(\nu_i\) from each of the \(d\) complex places of
\(K\), and label its two extensions to \(E\) by
\(\nu_i^+,\nu_i^-\), with \(\nu_i^-=\nu_i^+\tau\).
For a relative unit, use the unchanged normalization
\[
 \ell(u)_i=\log|\nu_i^+(u)|,\qquad
 \Lambda_E=\ell(\mathcal U_E^1),\quad
 \Lambda_R=\ell(\mathcal U_R^1).
 \tag{6}
\]
Both are full lattices in ordinary Euclidean \(\mathbb R^d\), using
Dirichlet's theorem as in MS-F3–F4. Their covolumes are
\(\mathcal R_E,\mathcal R_R\). No weighted absolute-regulator convention is
substituted for these definitions.

The inspected inherited facts used here are:

1. MS-F2: \((1+2\omega)\mathcal O_E\) is contained in the conductor of
   \(R\), and
   \[
   [\mathcal U_E^1:\mathcal U_R^1]\le 3^{3d}.
   \tag{7}
   \]
2. MS-F3–F4: if \(w_R=|\mu(E)\cap R|\), then \(6\le w_R\le8d^2\);
   the logarithmic kernel has exactly this multiplicity, and
   \[
   \mathcal R_R\le3^{3d}\mathcal R_E,\qquad
   h(u)=\|\ell(u)\|_1/(3d).
   \tag{8}
   \]
3. MS-F6: the complete inventory containing every nonzero order-unit
   return from the unchanged scalar box is
   \[
   U_j(T)=\{u\in\mathcal U_R^1:\|\ell(u)\|_1\le dL(T)\},
   \qquad L(T)=\tfrac12\log(48T^6).
   \tag{9}
   \]
   The centered logarithmic count, valid for every \(H\ge0\), is
   \[
   |\{u\in\mathcal U_R^1:\|\ell(u)\|_1\le H\}|
      \ge w_R\,\frac{H^d}{d!\mathcal R_R}.
   \tag{10}
   \]
   Its proof averages the half-radius \(\ell^1\)-ball over lattice translates
   and takes differences; it does not require a short lattice basis.

The standard arithmetic inputs are Minkowski's convex-body theorem, the
Minkowski covolume \(2^{-3d}\sqrt{|\Delta_E|}\), unique factorization of
nonzero ideals, and Dirichlet's unit theorem. They are the supplied
number-field/lattice toolkit, not newly verified external results.
The ideal Dirichlet-series estimate used below is proved directly for
the real exponent 2; analytic continuation, a residue theorem, a class-number
formula, and a general-signature regulator theorem are not used.

The source-availability check read the retained text of
`local-only/migration/research_supplement/shared/05-Phase_A_Sum_Product_Reproduction_FINAL_FROZEN.pdf`,
§3, equation (4), and the corresponding
`06-Phase_A_FINAL_FROZEN_Change_Log.pdf` entry for Lemma 3.1.
That regulator comparison explicitly assumes a totally real field.
It is not an estimate for \(E\) or for (6). The proof here supplies the
needed relative covolume estimate directly, with no such transplant.

## 2. Fixed constants

Set
\[
 B=2\sqrt{D_E}\ge2,\qquad g=\log B>0,\qquad
 J_0=64B^{12}(2B^2+1)^3,
 \tag{11}
\]
and define
\[
 K_E=J_0\,6e g,\qquad
 \boxed{K_R=27\cdot64B^{12}(2B^2+1)^3\,6e g},\qquad C_R=\log K_R .
 \tag{12}
\]
Here \(e\) is the base of the natural logarithm. These constants depend only
on the fixed root-discriminant bound. Their size is charged, not optimized.
In particular,
\[
 B^2>\frac2\pi\,\operatorname{rd}(E)
 \tag{13}
\]
at every level.

## 3. MSU-A1 — bounded classes cover the relative logarithmic space

For any nonzero \(a\in E\), define the additive logarithmic projection
\[
 p(a)_i=\tfrac12\bigl(\log|\nu_i^+(a)|
                         -\log|\nu_i^-(a)|\bigr).
 \tag{14}
\]
It satisfies \(p(ab)=p(a)+p(b)\), and \(p(u)=\ell(u)\) for
\(u\in\mathcal U_E^1\).

**Statement — PROVED.** There are at most \(J_0^d\) vectors
\(c_1,\ldots,c_J\in\mathbb R^d\) such that
\[
 \mathbb R^d
 \subseteq\bigcup_{k=1}^J
       \bigl(c_k+\Lambda_E+\mathbb B_1(3dg)\bigr),
 \tag{15}
\]
where \(\mathbb B_1(H)=\{x:\|x\|_1\le H\}\).

### 3.1 An algebraic integer approximating any prescribed relative log vector

Fix \(x=(x_1,\ldots,x_d)\in\mathbb R^d\).
Use one complex embedding of \(E\) above each real place of \(K\), and
the two embeddings \(\nu_i^\pm\) above each chosen nonreal place.
These are the \(3d\) complex-place representatives of \(E\).
In its Minkowski space \(\mathbb C^{3d}\), take the product of disks
with radii
\[
 B\quad(d\text{ disks}),\qquad
 Be^{x_i},\ Be^{-x_i}\quad(1\le i\le d).
 \tag{16}
\]
It is convex, centrally symmetric, and has volume
\(\pi^{3d}B^{6d}\), independently of \(x\). By (13), this volume exceeds
\[
 2^{6d}\operatorname{covol}(\mathcal O_E)
 =2^{3d}\sqrt{|\Delta_E|}.
 \tag{17}
\]
Minkowski's theorem therefore supplies \(0\ne a\in\mathcal O_E\)
in this product of disks. Equivalently, this step follows from the
already-used Blichfeldt averaging: the half-sized body has volume greater
than the lattice covolume, so some translate contains at least two lattice
points. Their nonzero difference lies in the original symmetric convex body.

Write the logarithms at these places as \(\alpha_r,\beta_i,\gamma_i\).
The \(3d\) errors
\[
 \alpha_r,\qquad \beta_i-x_i,\qquad\gamma_i+x_i
 \tag{18}
\]
are all at most \(g\). Their sum is
\(\tfrac12\log|N_{E/\mathbb Q}a|\ge0\), because the norm is a
nonzero integer. The sum of their positive parts is at most \(3dg\);
the sum of their negative parts in absolute value is no larger.
Consequently the sum of their absolute values is at most \(6dg\).
Using only the last \(2d\) coordinates of (18) gives
\[
 \|p(a)-x\|_1
 =\tfrac12\sum_i|(\beta_i-x_i)-(\gamma_i+x_i)|
 \le3dg.
 \tag{19}
\]

### 3.2 The two labels that must both be retained

Attach to \(a\) the exact labels
\[
 I=(a),\qquad b=N_{E/K}(a)=a\tau(a).
 \tag{20}
\]
The product of the bounds (16) gives
\[
 NI=|N_{E/\mathbb Q}a|\le B^{6d}.
 \tag{21}
\]
At a real place of \(K\), the image of \(b\) is the squared modulus of
the selected embedding of \(a\), so is at most \(B^2\).
At a complex place, the two bounds \(Be^{x_i}\) and \(Be^{-x_i}\)
multiply to \(B^2\). Thus
\[
 b\in\mathcal O_K\setminus\{0\},\qquad
 |\sigma(b)|\le B^2\quad\text{for every embedding }\sigma\text{ of }K.
 \tag{22}
\]

The number of possible integral ideals in (21) is at most
\[
 B^{12d}\sum_{\mathfrak a\ne0}(N\mathfrak a)^{-2}
 \le B^{12d}\zeta(2)^{6d}<B^{12d}2^{6d}.
 \tag{23}
\]
For completeness, unique ideal factorization gives the Euler product in
the middle. Above a rational prime there are at most \(6d\) prime ideals,
each of residue degree at least 1, so the local product is bounded by
\((1-p^{-2})^{-6d}\). Multiplication over primes proves the comparison
with the rational series. Finally
\(\sum_{n\ge1}n^{-2}<1+\int_1^\infty t^{-2}\,dt=2\).
All sums converge absolutely; no analytic theorem about zeta residues
enters (23).

The number of possible \(b\) in (22) is at most
\[
 (2B^2+1)^{3d}.
 \tag{24}
\]
Indeed a nonzero difference of two such algebraic integers has some
conjugate of modulus at least 1, by its nonzero integer norm. Translate
the mixed interval/disk window of radius \(1/2\) to each \(b\);
the interiors are disjoint, and all are contained in the window of
radius \(B^2+1/2\). Comparing their \(3d\)-dimensional volumes gives
(24). This is a separation argument, with no lattice-equidistribution
assumption.

Equations (23)–(24) bound the number of label pairs by \(J_0^d\).
Keeping the **exact element \(b\)** is essential. Equality of ideals
alone gives an arbitrary unit ratio; equality of integer absolute norms
would not force that ratio to have relative norm one.

### 3.3 Each label pair contributes one genuine unit-logarithm coset

For each nonempty label pair \((I,b)\), choose one representative \(a_k\).
Any \(a\) with the same labels has
\[
 u=a/a_k\in\mathcal O_E^\times,\qquad
 N_{E/K}(u)=b/b=1.
 \tag{25}
\]
Hence \(p(a)=p(a_k)+\ell(u)\).
Take \(c_k=p(a_k)\); (19) now proves (15).
The representatives themselves need not have uniformly bounded logarithms.
Their translations do not affect the volume calculation below. \(\square\)

## 4. MSU-A2 — uniform relative order-log covolume

**Statement — PROVED.**
\[
 \boxed{\mathcal R_E\le K_E^d,\qquad
        \mathcal R_R\le K_R^d.}
 \tag{26}
\]
These bounds hold at every level of the unchanged tower.

**Proof.** Integrate the covering (15) over a fundamental domain of
\(\Lambda_E\). For each \(k\), the sum of indicators of the translated
balls, integrated over that domain, equals the volume of one ball.
The covering gives an integrand at least 1. Therefore
\[
 \mathcal R_E
 \le J\,\operatorname{vol}\mathbb B_1(3dg)
 \le J_0^d\,\frac{2^d(3dg)^d}{d!}
 \le (J_0\,6eg)^d.
 \tag{27}
\]
The last inequality uses \(d!\ge(d/e)^d\), which follows by integrating
\(\log t\) under the sum \(\log(d!)\).
This is a covering of the full logarithmic space by finitely many
translates of a lattice neighborhood; it requires no bound on a chosen
fundamental parallelepiped or on successive minima.

By the previously proved order-index comparison (8),
\[
 \mathcal R_R\le3^{3d}\mathcal R_E\le(27K_E)^d=K_R^d.
 \tag{28}
\]
This charges the order passage once. Torsion is not another multiplicative
loss: more exactly the log-lattice index equals the unit-group index
multiplied by \(w_R/|\mu(E)|\), so (8) is already a safe upper bound.
\(\square\)

## 5. MSU-A3 — an explicit fixed radius proving MS-O1

Let \(T_0=2\sqrt{D_*}\), as in the unchanged scalar-carrier theorem, and fix
\[
 \boxed{T_*=\max\{T_0,\exp(2K_R/3)\}.}
 \tag{29}
\]
It is fixed independently of tower level.
Then \(L(T_*)\ge2K_R\).
Apply (10) and (26), using \(d!\le d^d\):
\[
 |U_j(T_*)|
 \ge w_R\,\frac{(dL(T_*))^d}{d!K_R^d}
 \ge w_R\left(\frac{L(T_*)}{K_R}\right)^d
 \ge w_R\,2^d\ge2^d.
 \tag{30}
\]
Thus the requested fixed exponent can be taken to be
\(\alpha=\log2\), and the assertion holds at every level, in particular
uniformly at all sufficiently large levels.

For any fixed \(T\), the sharper factorial asymptotic yields
\[
 \liminf_{j\to\infty}\frac{\log|U_j(T)|}{d_j}
 \ge 1+\log L(T)-C_R.
 \tag{31}
\]
Here \(\log d!=d\log d-d+O(\log d)\), and the torsion factor is
nonnegative and has zero exponential rate by \(w_R\le8d^2\).
The term \(C_R\) already contains \(3\log3\); subtracting that order
cost again would be double counting.

By the inherited height identity, every counted unit satisfies
\(h(u)\le L(T_*)/3\). This is bounded absolute logarithmic height, not
a bound independent of degree on each individual conjugate:
the direct conjugate bound remains \(e^{dL(T_*)}\).
No explicit basis of short units is needed or constructed.

## 6. Ledger, scope, and evidence

| Item | Charged statement | Status |
|---|---|---|
| Field and scalar carrier | Exactly (2) and the previous all-conjugate box; only one radius \(T_*\ge T_0\) is fixed before growth | Unchanged |
| Discriminant and degree | \(6d\), root discriminant \(\le D_E\), entering \(B=2\sqrt{D_E}\) | Inherited MS-F1 |
| Principal-ideal labels | At most \(B^{12d}2^{6d}\) | Proved (23) |
| Exact relative-norm labels | At most \((2B^2+1)^{3d}\) | Proved (24) |
| Denominators in ratios | Same integral principal ideal makes the ratio a maximal-order unit | Proved (25) |
| Relative norm of ratios | Equality of exact \(b\in K\) makes the norm 1 | Proved (25) |
| Covering error | \(\ell^1\)-radius \(3d\log B\) | Proved (19) |
| Relative covolume | \(\mathcal R_E\le K_E^d\), \(\mathcal R_R\le K_R^d\) | MSU-A2 |
| Order condition | Factor \(27^d\), included once in \(K_R\) | Inherited MS-F2 plus (28) |
| Torsion and multiplicities | Each log vector has exactly \(w_R\) units; \(6\le w_R\le8d^2\) | Inherited MS-F3–F4 |
| Unit population | At least \(2^d\) at the explicit fixed radius (29) | MSU-A3 |
| Input thinning and real projection | No input thinning or change; the prior real field embedding remains injective | Unchanged |
| Useful pair-dependent returns | No population-to-return implication is proved | OPEN |
| Exceptional pairs and full output support | No new bound | OPEN |
| Compression exponent | No positive \(c\) is established by this action count alone | OPEN |

Claim identifiers MSU-A1–A3 refer to this version's §§3–5, with the
quantifiers and dependencies stated above. The derivation and the specialist's
independent challenge are internal evidence. A separate specialist read and
accepted the entire written proof; the checks and PASS verdict are recorded in
[geometry-audit.md, §5](geometry-audit.md#5-independent-written-proof-audit-of-msu-a1a3).
The lead independently checked the deductions. No external review or novelty
claim is made.

The specialist used zero mathematical evaluations and zero research-program
CPU. Reading local text and writing this companion are not experiment
reruns. Historical reports and source files were not edited.
