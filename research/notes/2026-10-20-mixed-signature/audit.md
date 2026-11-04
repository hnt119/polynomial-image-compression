# Independent rate and full-support audit

**20 October 2026 · version 3, final signoff · T03 / shared full-rank quadratic direction.**
Fixed polynomial: \(Q(x,y)=x^2+xy+y^2\).
Scope: the authorized **C0 Mixed-Signature Lattice Symmetry** cycle, with
\(F\subset K=F(s)\subset E=K(\omega)\), \(s^3+s+1=0\), and the
unchanged all-conjugate scalar window. This is an independent internal audit,
not an external review or novelty assessment.

## 1. Verdict and evidence boundary

**PASS for the written structural and scoped obstruction results.**
The complete proofs MS-F1–F6 in [field-units.md](field-units.md) and
MS-W1–W3 in [window-returns.md](window-returns.md) were independently
inspected and checked in this task. The complete MS-C1–C3 proofs in
[carrier-rate.md](carrier-rate.md), including the torsion-enriched seed
bound, were independently checked as written.

**OPEN for the full-rank unit-return construction and actual image.**
The proofs establish integral actions, relative rank, a finite exhaustive
window of possible order-unit actions, and necessary return conditions. They
do not establish enough actual returns on almost all ordered pairs. The
fixed cyclic seed strategy fails: its complete integer-power action family
has only \(O(\log n)\) returns at each pair; even adjoining every tower
torsion unit gives only \(O((\log n)^3)\) under the stated radius condition.
These results neither bound
the full relative-unit family's returns nor bounds complete quadratic fibers.

The auditor ran **0 mathematical evaluations and 0 research-program CPU
seconds**, used no network, and spawned no agent. No old scout was rerun.
The shared evaluation/CPU cap and verification reserve belong to the lead;
they are not evidence that any mathematical computation occurred.
This audit adds only this new file and preserves historical source bytes.

### Controlling sources read

- Corrected C0: private source
  `local-only/migration/research_supplement/shared/Phase_C0_Corrected.md`,
  especially §5 and Theorem C0.1, with `C0_CORRECTION_LOG.md`.
- Explicit mixed-signature seed: private source
  `local-only/migration/sources/TFQ_Direct_Construction_and_Adaptive_Radical_Report.md`,
  §G.4. The seed and its non-torsion property are inherited, not newly discovered.
- Frozen obstruction scopes: private source
  `local-only/migration/sources/T03_CURRENT_STATE.md`, §§5.2–5.3, the
  global ideal bound in §6, and the standard inputs in §10.
- Existing [HR-1 return-to-support lemma](../2026-09-16-high-return/return-lemma.md),
  especially §2; its exact exceptions and multiplicity hypotheses were read.
- Startup setup/map/migration records, master handoff, T03 SPEC/STATUS, and
  the relevant mechanism, failure, and open-lemma entries were consulted.
  The latest [BFF-O1 retirement](../2026-10-11-bff-o1/README.md) remains in
  force and is not reopened.

The old reported obstructions were read to check their hypotheses; this task
does not claim another independent audit of every historical proof. General
Dirichlet and discriminant identities are explicitly declared inherited
standard inputs in the field companion, rather than silently proved here.

## 2. Field, order, torsion and height audit

The following checks passed in the complete written proof.

1. **Degree and signature.** A cubic reducible over the totally real \(F\)
   would have its unique real root \(s\) in \(F\), contradicting the
   non-totally-real cubic subfield. Thus \([K:F]=3\), and each real
   embedding of \(F\) gives one real and one complex pair in \(K\).
   The resulting signatures are \(K:(d,d)\) and \(E:(0,3d)\), with
   degrees \(3d\) and \(6d\).
2. **Discriminants.** The order discriminants \(-31\) and \(-3\) give
   \(\operatorname{rd}(K)\le D_0 31^{1/3}\) and
   \(\operatorname{rd}(E)\le\sqrt3\operatorname{rd}(K)\).
   No unjustified unramifiedness or new splitting property is assumed.
3. **Coefficient order.** For \(R=\mathcal O_K[\omega]\), the trace
   equations for \(z=a+b\omega\in\mathcal O_E\) give
   \((1+2\omega)z\in R\). Hence
   \((1+2\omega)\mathcal O_E\) is contained in the conductor. This
   yields the explicit relative-unit index bound \(3^{3d}\). The additive
   order index \(3^{3d/2}\) and the unit subgroup index are different costs.
4. **Relative rank.** The norm image contains every \(K\)-unit square.
   Dirichlet ranks therefore give \((3d-1)-(2d-1)=d\) for the relative
   kernel; the order subgroup has the same rank by finite index.
5. **Torsion.** Every totally real subfield of \(K\) lies in \(F\):
   its compositum with \(F\) is an intermediate field of prime degree
   three and cannot equal the mixed-signature \(K\). For a root of unity
   in \(E\), its real trace consequently lies in \(F\). A second
   quadratic extension distinct from \(F(\omega)\) would force degree
   four to divide six. Thus \(\mu(E)=\mu(F(\omega))\), and the stated
   degree estimate gives \(6\le w_R\le8d^2\).
6. **Logarithms and normalization.** At real \(K\)-places the relative
   unit has modulus one. Each nonreal block has logarithms \(t_i,-t_i\),
   repeated under conjugation. Thus the stated relative log lattice has
   dimension \(d\), and
   \[
   h(u)=\|t\|_1/(3d),\qquad
   \max_\sigma|\sigma u|=e^{\|t\|_\infty}.
   \]
   The equality
   \([\Lambda_E:\Lambda_R]=[U_E^1:U_R^1]w_R/w_E\) correctly prevents
   charging torsion twice.

No short basis or favorable regulator bound follows merely from these
statements. The explicit seed is one unit of infinite order; base change
does not turn it into \(d\) independent units.

## 3. Input count and real projection

Let \(D_*=D_0 31^{1/3}\) and

\[
C_K(T)=\{x\in\mathcal O_K:|\sigma x|\le T
                   \text{ at every embedding}\},\qquad T\ge1.
\]

One real embedding is injective, so \(A=\sigma_0(C_K(T))\) is a genuine
same-set carrier of cardinality \(n=|C_K(T)|\). There is no projection
fiber or hidden label count.

In standard real/complex Minkowski coordinates, the scalar body is a product
of \(d\) real intervals and \(d\) complex disks. Its half-body has volume
\((\pi/4)^dT^{3d}\), and the integer lattice has covolume
\(2^{-d}\sqrt{|D_K|}\). Blichfeldt averaging and subtraction of a chosen
lattice point in one translate give the **centered** lower bound

\[
\boxed{\left(\frac{(\pi/2)T^3}{D_*^{3/2}}\right)^d
\le n\le(2T+1)^{3d}.}
\tag{1}
\]

For the upper bound, distinct integer points cannot have every conjugate
difference of modulus strictly below one: their nonzero difference has
nonzero integer absolute norm. Translates of the half-unit body have disjoint
interiors and lie in the body of radius \(T+1/2\), giving (1). Complex
places contribute two real dimensions; this accounts for the exponent
\(3d\) and the covolume factor \(2^{-d}\).

For a fixed radius chosen before the tower grows, define

\[
a=\log\frac{(\pi/2)T^3}{D_*^{3/2}},\qquad B=3\log(2T+1).
\tag{2}
\]

Choosing \(T\) so that \(a>0\) proves exponential actual input growth
and the upper rate needed for conversion to powers of \(n\). A varying
radius requires a separate rate calculation; fixed-field large-radius
asymptotics cannot be substituted for (2) with unchanged constants.
The explicit choice \(T_0=2\sqrt{D_*}\) has
\(n\ge(4\pi)^d\); this constant in MS-C1 is correct.

## 4. Actual actions, nonreal returns and the finite inventory

For \(u=a+b\omega\in R^\times\) with relative norm one, the exact matrix

\[
M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix}
\tag{3}
\]

has integral coefficients, determinant one and integral inverse. Expanding
\(u(x-\omega y)\) proves preservation of the actual polynomial \(Q\).
This is a whole-scalar identity on the entire coefficient lattice.

At a nonreal \(K\)-place, the coordinates \(z=x-\eta y\),
\(w=x-\eta^2y\) are multiplied by \(t,t^{-1}\). The companion correctly
distinguishes the relative involution from complex conjugation here.
The exact transformed bidisk inequalities are retained: independent
rectangle membership in \((z,w)\) is not substituted for them.

Source and target membership imply

\[
|Q_i(x,y)|\le4T^2e^{-|\lambda_i(u)|}
\quad\text{at each complex block},
\]

while each real conjugate has absolute value at most \(3T^2\). For a
nonzero pair, \(Q(x,y)\) is a nonzero algebraic integer. Its absolute norm
therefore yields

\[
1\le48^dT^{6d}e^{-2\|\lambda(u)\|_1},\qquad
\boxed{\|\lambda(u)\|_1\le\tfrac d2\log(48T^6).}
\tag{4}
\]

The exponent two on each complex place is essential and is present.
Thus the finite order-unit set defined by (4) contains **all** order-unit
returns at every nonzero source. Its height cutoff is exactly
\(h(u)\le\frac16\log(48T^6)\). Finiteness follows either from the
logarithmic lattice and finite torsion kernel or from bounded integer
minimal-polynomial coefficients. It is not a quantitative return theorem.
Arbitrary nonintegral norm-one multipliers are outside this action inventory.

Distinct units have distinct targets at a nonzero pair, since multiplication
by \(x-\omega y\ne0\) is injective. At \((0,0)\), the actual return
count is one, regardless of the infinite stabilizer. The zero pair must be
handled as one exceptional output or one exceptional pair, not credited with
infinitely many returned targets.

### Centered unit counts and remaining costs

For relative logarithmic covolume \(\mathcal R_R\), torsion size \(w_R\),
and \(S=\frac12\sum_i\|v_i\|_1\) for a lattice basis, the audited counts are

\[
w_R\frac{H^d}{d!\mathcal R_R}
\le \#\{u:\|\lambda(u)\|_1\le H\}
\le w_R\frac{2^d(H+S)^d}{d!\mathcal R_R}.
\tag{5}
\]

The centered lower bound correctly uses Blichfeldt on the half-ball and
difference subtraction; the upper bound correctly uses outer fundamental
tiles. If, additionally, \(\mathcal R_E\le e^{Cd+o(d)}\), the cutoff
\(H=dL(T)\), \(L(T)=\frac12\log(48T^6)\), has the conditional candidate
action rate

\[
\frac1d\log|\mathcal U_R(T)|
\ge1+\log L(T)-C-3\log3-o(1).
\tag{6}
\]

The regulator premise is not proved in this cycle. Even a positive right
side would count possible actions, not actual returns. The source-dependent
log intervals, exact complex inequalities, and real-coordinate windows
would still need simultaneous control. If one counts directly in the order
lattice, its covolume already includes the subgroup cost; that cost must not
be deducted a second time.

## 5. Seed obstruction and the continuous/discrete distinction

For \(u_0=s^2+s\omega\), all complex blocks have the same expanding modulus
\(\rho>1\), after choosing an extension at each block. The two eigenvalues
have product one and different moduli, since
\(|s_c+\omega|^2-|s_c+\omega^2|^2=2\sqrt3\operatorname{Im}s_c\ne0\).
This verifies that \(\rho\) is fixed independently of \(F,d,T\).

Equation (4) gives, for every returning integer power at a nonzero source,

\[
|k|\le\frac{\log48+6\log T}{2\log\rho}.
\tag{7}
\]

Every positive and negative exponent is covered. Since
\(n\ge2\lfloor T\rfloor+1>T\), all powers give only \(O(\log n)\)
distinct returns; adjoining simultaneous signs changes only a constant
factor. Zero has one target. Thus this cyclic action certificate cannot
satisfy a near-full lower tail at any fixed positive power of \(n\).

The complete MS-C3 proof also adjoins **all** roots of unity in the action
order. They have zero logarithmic vector, so a returning unit
\(\zeta u_0^k\) still satisfies (7). Multiplying the exponent count by
\(w_R\le8d^2\), and using \(d\le\log n/\log(4\pi)\) whenever
\(T\ge T_0\), gives \(O((\log n)^3)\) actual returns. This is uniform
for variable radii \(T_j\ge T_0\), includes negative powers and every
torsion multiplier, and has the whole square as its eventual bad set for
each fixed positive-power threshold. It remains a selected-action bound,
not a bound on complete fibers.

The separate continuous estimates also check:

\[
\operatorname{vol}\text{-fraction of a local return domain}
\le\min\{1,4e^{-2|\lambda|}\},
\]

and the two sets containing all positive/negative seed-power returns have
total continuous fraction at most \(2\theta_\rho^d\), with the stated
\(\theta_\rho<1\). The explicit disk construction proves the strict gap.
Product measure concerns independent ambient coordinate blocks, not
independent global units or independent lattice points.

The lattice version with \(o_K(1)\) is only a **fixed-field** dilation
statement. It is not uniform in the tower. Choosing very large radii
separately at each level can improve that approximation but may change or
destroy the intended input/action exponent comparison. The pointwise bound
(7), by contrast, is uniform and needs no lattice approximation.

## 6. Full-support requirement and rate audit

The existing HR-1 implication applies once the distinct-return count satisfies

\[
\#\{p\in A_j^2:R_j(p)<n_j^\varepsilon\}
\le Cn_j^{2-\delta}
\tag{8}
\]

for fixed \(\varepsilon,\delta>0\) and all sufficiently large levels of
the selected sequence. With zero included in the exception accounting,
fiber partitioning gives

\[
|Q(A_j,A_j)|\le n_j^{2-\varepsilon}+Cn_j^{2-\delta}.
\tag{9}
\]

An alternative convention excluding zero from (8) adds one to (9). Either
way every fixed \(0<c<\min\{\varepsilon,\delta\}\) follows eventually.
The boundary exponent is not automatic because constants must be absorbed.
All ordered pairs use the same scalar set. No common stable core or selected
rich population may replace (8) without charging its complement.

At a fixed radius, a sufficient degree-form version is a distinct-return
threshold \(e^{\kappa d-o(d)}\) outside at most
\(n^2e^{-\eta d+o(d)}\) bad pairs, with fixed \(\kappa,\eta>0\).
Using the upper input rate \(B\) in (2), this certifies any

\[
0<c<\min\{\kappa,\eta\}/B.
\tag{10}
\]

Neither exponent is supplied by rank \(d\), the finite cutoff, the
conditional candidate action count (6), or a continuous overlap upper bound.
For a varying radius, the corresponding input upper rate is
\(B_j=3\log(2T_j+1)\); useful positive ratios must be proved rather than
retaining (10) unchanged. Any scalar thinning must be charged in both
coordinates, and any uncounted boundary or exceptional outputs must remain
in the support estimate.

## 7. Historical scopes and final unresolved obligations

| Item | Correct disposition in this cycle |
|---|---|
| Corrected C0 | Supplies the accepted totally real tower and counting discipline; its rank-one quadratic theorem does not prove the present full-rank target |
| C0 selected split primes | Their splitting in \(F_j\) is not asserted in \(K_j,E_j\); no local sparsity gain is imported |
| Frozen T03 §5.3 sieve obstruction | Restricts its specified residue/packing certificate; it is not an actual-image lower bound for the current unit mechanism |
| Frozen global ideal bound | Its finite relative-unit factor uses a CM extension of a totally real base. The present base is mixed-signature and its relative-unit rank is positive; also the field degree grows. No literal fixed-field/totally-real conclusion transfers |
| Frozen Phase-A regulator input | A totally-real regulator estimate or assumption is not silently a bound on this relative logarithmic covolume |
| Balanced-factor carrier | Remains retired by BFF-O1; neither its carrier nor its proof search is reopened |
| Scalar and action denominators | Input is integral. Actions selected in \(R\) have integral coefficients; passing to \(R\) from maximal-order units has the separately charged subgroup cost |
| Heights and distortion | Exact cutoff and formulas are proved; they do not imply simultaneous window return |
| Relative regulator / basis shape | Absolute covolume and useful shape estimates remain quantitative unknowns, not zero costs |
| Return tail / full support | The seed tail fails even with all order torsion. The full-rank order-unit tail and actual image rate remain OPEN |
| Correlated-window variant | None was proposed or analyzed in the inspected companions; no additional mechanism is inferred from this audit |

The missing positive theorem is a quantitatively adequate actual return tail
for the specified finite order-unit inventory and common lattice carrier,
with its unit-lattice and all window costs paid. Even proving a candidate
unit-count exponent would leave that separate tail obligation. Conversely,
failure to prove that tail here is not a theorem that the carrier or the
unrestricted real quadratic target has no power-saving construction.

The one retained **MS-O1** gate is correctly narrower: for the fixed tower,
ask for fixed \(T\ge T_0\), \(\alpha>0\), and \(j_0\) with
\(|U_j(T)|\ge e^{\alpha d_j}\) for every \(j\ge j_0\). This is necessary
for the uniform all-large-level return tail formulated in this cycle,
because one nonexceptional source already requires at least
\(n_j^\varepsilon\ge e^{a(T)\varepsilon d_j}\) actions. It is insufficient
for the tail. Refuting its all-large-level quantifiers alone would not
exclude favorable unbounded subsequences or other towers. No proof of this
gate is claimed in the present audit.

No positive compression exponent, global impossibility theorem, or new
successor carrier is certified by this audit. Mathematical status remains
OPEN beyond the exact structural results and the scoped cyclic-seed failure.

## 8. Final report consistency check

The final [README](README.md), [carrier/rate ledger](carrier-rate.md), and
[machine state](state.json) were read after the companion proof audits.
**PASS:** their constants, quantifiers and statuses match the written proofs.
In particular:

- the exponential input count uses actual scalars and the degree of \(F_j\);
- the action inventory contains all nonzero order-unit returns but is not
  asserted to consist of useful actions;
- bounded Weil height is explicitly separated from the possible
  \(e^{d_jL(T)}\) conjugate bound and its nonuniform distortion;
- the torsion-enriched seed failure is stated for \(T_j\ge T_0\), and is
  not promoted into a full-fiber or actual-image obstruction;
- fixed-field continuous-to-lattice limits are not called uniform in the
  growing tower, and no arbitrary correlated-window impossibility is claimed;
- MS-O1 retains its fixed-tower, all-sufficiently-large-level quantifiers,
  the unbounded-subsequence caveat, and its insufficiency for compression;
- \(\varepsilon,\delta,c\) remain unproved, the new carrier remains OPEN,
  and the unrelated BFF carrier remains retired.

No material mathematical or cross-file scope defect remained in the files
inspected at this signoff. This final step was a report-consistency read,
not a mathematical rerun, an artifact-integrity certification, or an external
review. The lead records administrative checks and source hashes separately.
