# Typical unit returns: independent proof and rate audit

21 October 2026 · T03 · fixed \(Q(x,y)=x^2+xy+y^2\) · version 4.

This is the independent proof/scope contribution to the authorized MS-O2
cycle. The fields, order, scalar carrier and fixed radius \(T_*\) are
unchanged. The frozen MS-O1 theorem is an input, not a theorem rerun in
this cycle. There is no new carrier, seed, action mechanism, nested agent,
network request or mathematical program. This specialist's mathematical
evaluation and research-program CPU usage are both zero.

## 1. Precise setting and source boundary

Use the complete construction in the
[MS-O1 report](../2026-10-21-relative-unit-population/README.md), §§2–3:
\[
 K_j=F_j(s),\quad E_j=K_j(\omega),\quad
 R_j=\mathcal O_{K_j}[\omega],\quad
 \mathcal G_j=\{u\in R_j^\times:u\tau(u)=1\}.
\]
Here \(s^3+s+1=0\), \(s\) is real, \(\tau\) fixes \(K_j\), and
\(d_j=[F_j:\mathbb Q]\to\infty\). The fixed radius \(T_*\) and all
its constants precede the growing index. At that radius,
\[
 C_j=\{x\in\mathcal O_{K_j}:|\sigma x|\le T_*\text{ for all }\sigma\},
 \quad A_j=\sigma_0(C_j),\quad n_j=|A_j|,
\]
with injective real embedding \(\sigma_0\), and
\[
 e^{a d_j}\le n_j\le e^{B d_j},\qquad
 a=\log\frac{(\pi/2)T_*^3}{D_*^{3/2}}>0,
 \quad B=3\log(2T_*+1).
 \tag{1}
\]
The source square is the whole ordered Cartesian square, with no thinning.
We identify its algebraic and chosen real versions using \(\sigma_0\).

The actual global action and finite inventory are
\[
 M_u=\begin{pmatrix}a_u&b_u\\-b_u&a_u-b_u\end{pmatrix},
 \quad u=a_u+b_u\omega\in\mathcal G_j,
 \quad U_j=\{u\in\mathcal G_j:\|\ell_j(u)\|_1\le d_jL(T_*)\}.
 \tag{2}
\]
The inherited cutoff theorem
[MS-W1](../2026-10-20-mixed-signature/window-returns.md#2-ms-w1--exact-action-and-the-complex-return-domain)
contains **every** order-unit return of every nonzero source in \(U_j\).
The inventory need not be a subgroup. Every matrix is integral and
preserves \(Q\), and two units giving the same target at a nonzero pair
are equal.

Let
\[
 \Omega_j=A_j^2\setminus\{(0,0)\},\quad N_j=n_j^2-1,
 \quad D_{j,u}=\{p\in\Omega_j:M_up\in A_j^2\},
\]
and let \(R_j(p)\) count distinct actual targets from \(U_j\).
All scalar target membership constraints are retained, at every embedding.

The earlier source hierarchy, corrected C0 boundary, T03 fixed target,
and the frozen mixed-signature proofs were inspected in this audit chain.
At the present startup, Git state, setup/migration guidance, the master
handoff, T03 current-state scope, SPEC/STATUS and the relevant registries
were checked. Inherited uncommitted files were preserved. Memory was
used only as an orientation pointer; current mathematical statements
were checked in the located repository sources. No absent source was
reconstructed from its title.

## 2. MTR-A1 — exhaustive orbit intersections and reciprocal support

**PROVED.** Partition \(\Omega_j\) by the full group \(\mathcal G_j\):
two sources are equivalent when one is obtained from the other by a
matrix \(M_u\) with \(u\in\mathcal G_j\). Let the nonempty intersections
with \(\Omega_j\) have sizes \(m_1,\ldots,m_J\). Then
\[
 R_j(p)=m_i\quad(p\text{ in the }i\text{th intersection}),\qquad
 \sum_{p\in\Omega_j}\frac1{R_j(p)}=J.
 \tag{3}
\]

**Proof.** Any target obtained from \(U_j\) is in the full group orbit.
Conversely, any point of that orbit which is in \(A_j^2\) is a returning
target of an order unit. Since the source is nonzero, the exhaustive
cutoff places that unit in \(U_j\). Thus its full finite orbit
intersection is exactly its returned target set. A target cannot be
zero because \(M_u\) is invertible. Group equivalence partitions the
nonzero square even though the displayed finite inventory itself need
not be closed under multiplication. Each intersection contributes
\(m_i/m_i=1\) to the reciprocal sum. \(\square\)

Every intersection lies in one \(Q\)-fiber. Since \(Q\) is positive
definite on the chosen real plane, its zero fiber consists just of the
origin. Consequently
\[
 \boxed{|Q(A_j,A_j)|\le1+J
        =1+\sum_{p\in\Omega_j}\frac1{R_j(p)}.}
 \tag{4}
\]
The added one is the origin's single output, not one per unit label.
There is no claim of equality between \(J\) and the number of nonzero
quadratic values.

### Why complete quadratic fibers can be larger

Write \(z=x-\omega y\) and \(z'=x'-\omega y'\). If two nonzero
pairs have equal \(Q\), then \(u=z'/z\in E_j^\times\) has relative
norm one. It need not be in \(R_j^\times\). Thus equal norms alone do
not put the pairs in the same integral-unit orbit.

The exact order-level label for an orbit is
\[
 (zR_j,\ b=z\tau(z)).
 \tag{5}
\]
Multiplying by an order unit of relative norm one preserves both labels.
Conversely, equality \(zR_j=z'R_j\) implies that both \(z'/z\) and
its inverse belong to \(R_j\); equality of the element \(b\) gives
relative norm one. This reasoning uses no ideal-factorization property
of the nonmaximal order.

In particular, common negation always supplies two distinct targets at
nonzero sources: \(-1\in U_j\), and \(A_j=-A_j\). Coordinate swap
also preserves \(Q\), but its field ratio
\(-\omega\tau(z)/z\) need not be an order unit. A four-point sign/swap
baseline must not automatically be assigned to \(R_j\).

For a different, nonexhaustive finite action list containing the identity,
orbit constancy in (3) need not hold. The weaker bound (4) still follows
fiber by fiber from \(R(p)\le|Q^{-1}(Q(p))\cap A^2|\). This observation
does not replace the stronger exhaustive statement actually used here.

## 3. MTR-A2 — exact moments, inverse returns and rate conversion

Write
\[
 S_1=\sum_{u\in U_j}|D_{j,u}|,\quad
 S_2=\sum_{u,v\in U_j}|D_{j,u}\cap D_{j,v}|,\quad
 \mu=S_1/N_j.
\]
Freeness and (3) give the exact identities
\[
 N_j=\sum_i m_i,\qquad
 S_1=\sum_i m_i^2,\qquad S_2=\sum_i m_i^3,
 \tag{6}
\]
\[
 \operatorname{Var}_{p\in\Omega_j}R_j(p)=S_2/N_j-\mu^2.
 \tag{7}
\]
These are algebraic counting identities. They do not assert any favorable
distribution of the orbit sizes. For example, Cauchy–Schwarz gives
\(J\ge N_j/\mu\), the lower direction; a large mean alone does not
give an upper bound for \(J\).

Define the normalized reciprocal statistic
\[
 \mathcal H_j=\frac1{N_j}\sum_{p\in\Omega_j}\frac1{R_j(p)}=rac J{N_j}.
 \tag{8}
\]
If, for one fixed \(\gamma>0\) and all sufficiently large \(j\),
\(\mathcal H_j\le e^{-\gamma d_j}\), then (4) directly gives
\[
 |Q(A_j,A_j)|\le1+(n_j^2-1)e^{-\gamma d_j}.
 \tag{9}
\]
Using (1), every
\[
 0<c<\min\{\gamma/B,2\}
 \tag{10}
\]
would then be a fixed image saving eventually. This is a proved
implication; no reciprocal estimate of this strength has been established
by these identities.

The same conclusion holds with a fixed positive prefactor:
if \(\mathcal H_j\le C e^{-\gamma d_j}\) eventually, then
\[
 |Q(A_j,A_j)|\le1+C(n_j^2-1)e^{-\gamma d_j}.
\]
There is no independent exponent cap to impose in this setting.
Indeed \(J\ge1\) and \(N_j<e^{2Bd_j}\) give
\(\mathcal H_j=J/N_j>e^{-2Bd_j}\). A fixed \(C\) in the
assumed upper bound forces \(\gamma\le2B\) as \(d_j\to\infty\);
otherwise \(C e^{(2B-\gamma)d_j}\) would tend to zero while exceeding
one. Hence every \(0<c<\gamma/B\) is automatically below two.
Strictness absorbs both the prefactor and the origin. Formula (10)
is the equivalent conservative form with this automatic restriction
displayed.

The same premise yields a genuine lower tail: for \(0<\kappa<\gamma\),
\[
 |\{p\in\Omega_j:R_j(p)<e^{\kappa d_j}\}|
 \le N_j e^{-(\gamma-\kappa)d_j}.
 \tag{11}
\]
Indeed every term from this exceptional set exceeds
\(e^{-\kappa d_j}\) in the reciprocal sum. The origin is one further
source if a statement is made on the full square. Conversely, a lower
tail with threshold \(e^{\kappa d_j}\) outside at most
\(C N_j e^{-\eta d_j}\) nonzero sources gives
\[
 \mathcal H_j\le e^{-\kappa d_j}+C e^{-\eta d_j},
 \tag{12}
\]
using \(R_j(p)\ge1\) on the exceptional set. These comparisons apply
to ordered sources and use actual distinct targets.

### The precise MS-O2 sufficient condition

MS-O2 asks for fixed \(\kappa,\eta>0\) such that, eventually at every
level,
\[
 \mu\ge e^{\kappa d_j},\qquad
 S_2/N_j-\mu^2\le e^{-\eta d_j}\mu^2.
 \tag{13}
\]
Chebyshev's inequality then bounds the number below \(\mu/2\) by
\(4N_j e^{-\eta d_j}\). Thus
\[
 \mathcal H_j\le2e^{-\kappa d_j}+4e^{-\eta d_j},
\]
and in particular
\[
 |Q(A_j,A_j)|
 \le1+2N_j e^{-\kappa d_j}+4N_j e^{-\eta d_j}.
 \tag{14}
\]
The previous report's slightly weaker first term \(2n_j^2e^{-\kappa d_j}\)
is also valid. The origin is charged once in either form.
Since \(\mu\le N_j<e^{2Bd_j}\), consistent premises force
\(\kappa<2B\). Therefore every
\[
 0<c<\min(\kappa,\eta)/B
 \tag{15}
\]
would work eventually; its strictness absorbs fixed prefactors, and
\(c<2\) absorbs the origin. This is the independently checked MSU-R1
rate with no new premise silently supplied.

MS-O2 is a stronger sufficient condition, not a necessary characterization
of a small image or of a useful lower tail. Its failure alone would not
retire the carrier. A failure of an attempted estimate for (13) is still
weaker: it does not refute (13) itself. Eventual all-level assertions and
subsequence assertions must retain their different quantifiers.

## 4. Evidence and audit status

MTR-A1–A2 are complete independent symbolic checks of the support and
rate implications, based on the identified exhaustive cutoff and
integral-action facts. They were communicated to the lead before this
note was written. They establish no new return lower bound, small
exceptional set, or full-image exponent.

The completed source-window, discrete-incidence and lower-estimate
companions were subsequently read and independently checked as recorded
in §5. Agreement with their earlier outlines is distinguished from
inspection of their complete written proofs. No historical proof or
experiment was rerun. The general T03 target, this carrier's actual
return behavior, and the separate RC15/4 obligation remain OPEN on the
evidence recorded here.

## 5. Independent written-companion reviews

### 5.1 MTR-L1–L2: actual discrete lower incidence

**PASS:** the complete [lower-incidence.md](lower-incidence.md), §§1–4,
was read after writing. The following constants and logical steps were
checked independently.

At a real place the invariant ellipse \(Q\le3T^2/4\) lies in the
coordinate square and has area \((\sqrt3\pi/2)T^2\). At a complex
place the eigen-coordinate change has real Jacobian three. The two
disks of radii
\[
 (\sqrt3/2)T\min(1,e^{-\ell}),\qquad
 (\sqrt3/2)T\min(1,e^{\ell})
\]
therefore have scalar-coordinate volume
\((3\pi^2/16)T^4e^{-2|\ell|}\). Both source and target belong to
the bidisk for every phase of the actual global unit. This is a
sufficient subbody used to bound an incidence below, not a replacement
input carrier.

The full product volume is
\((3\sqrt3\pi^3/32)^dT^{6d}e^{-2H}\). Half-body Blichfeldt in
dimension \(6d\), divided by pair-lattice covolume
\(2^{-2d}|\Delta_K|\), gives exactly
\[
 |D_u|+1\ge
 \left(\frac{3\sqrt3\pi^3}{512}\right)^d
 \frac{T^{6d}}{|\Delta_K|}e^{-2H}.
 \tag{16}
\]
The origin is subtracted for each unit separately. For the smaller
inventory \(H\le dh\) with \(\log\Theta_T>2h\), its effect is
absorbed by a factor two only after the per-unit lower bound exceeds
two. The normalization in the companion's equation (9) is consequently
correct:
\[
 \mu_j\ge\frac{w_j}{2}\frac{d_j^{d_j}}{d_j!}
 \left(\frac{P_T h e^{-2h}}{K_R}\right)^{d_j},\qquad
 P_T=\frac{3\sqrt3\pi^3}{512D_*^3(2+1/T)^6}.
 \tag{17}
\]
Inserting the upper input count, rather than a volume approximation for
the input count, is necessary for this lower bound.

The maximizing value \(h=1/2\) is admissible: the frozen cutoff has
\(L(T_*)\ge2K_R>1/2\), and
\(\Theta_T\ge3\sqrt3\pi^3/8>e\). The optimized certificate rate
is exactly \(\log(P_T/(2K_R))<0\). This is the rate of a particular
lower estimate. It is not an upper bound for the actual mean, a
refutation of MS-O2, or an actual-image obstruction. The unconditional
\(\mu_j\ge2\) from signs remains valid. No correction to this proof
was required.

### 5.2 MSR-I1–I4: exact labels and the ambient upper estimate

**PASS:** the complete [incidences.md](incidences.md), §§1–6, was read.
Its orbit and reciprocal identities agree with the independently
derived MTR-A1–A2 above. The following additional arithmetic details
were checked.

- Principal-order-ideal equality is used directly; no Dedekind
  property is asserted for \(R\). The second label is the exact element
  \(b=z\tau(z)\), not its absolute norm.
- Equal maximal-order labels give a free maximal-order relative-unit
  orbit. It splits into at most \([G_E:G_R]\le27^d\) full order-unit
  orbits, and intersecting with the finite source set cannot increase
  this number of classes. There is no second torsion or order loss.
- For an ideal \(I\) satisfying \(I\tau(I)=(b)\mathcal O_E\), a
  split prime contributes \(v_{\mathfrak p}(b)+1\) choices; an inert
  prime requires an even valuation and then has one choice; at a
  ramified prime the exponent of \((b)\) doubles after extension and
  again gives one choice. The relaxation includes nonprincipal and
  unoccupied ideals only in an upper count.
- The field-uniform divisor estimate is valid with the displayed
  fixed \(C_\epsilon\). For small prime-ideal norms its local proof is
  \((e+1)r^e\le\sum_{k=0}^e r^k\le(1-r)^{-1}\); for norms at least
  \(2^{1/\epsilon}\), use \(e+1\le2^e\). There are at most \(3d\)
  prime ideals above any rational prime. The dependence on the fixed
  \(\epsilon\) remains charged.
- Every actual output is contained in the all-conjugate radius
  \(3T^2\) box. The norm and ambient cardinality bounds are upper
  relaxations, not assertions that all candidate outputs occur.
- The conversion uses
  \(N=n^2-1\ge(8/9)V(T)^{2d}\), since \(n\ge3\). It gives exactly
  the companion's factor \(9/8\), coefficient \(108D_*^3/\pi^2\),
  and the strict lower bound \(23328D_*^3/\pi^2\) for the base of
  that upper certificate. The last number is \(108\cdot216\).

Thus the stated ambient upper estimate supplies no exponentially small
occupied-label ratio. The companion correctly does not turn this
failure into a lower bound on the actual number of occupied labels.
No mathematical correction was required. Raw absolute-value pipes in
two Markdown table cells were reported as presentation defects; the
author subsequently replaced them with `\lvert` and `\rvert`, and
the corrected cells were re-read and confirmed.

A fixed prefactor \(C_0\) in an eventual bound
\(J\le C_0N_j e^{-\gamma d_j}\) only multiplies the corresponding
decaying terms in (9) and (11). The same strict eventual exponent range
is valid. This observation does not supply the missing bound.

### 5.3 MS2-W1–W3: exact source windows and cover limitations

**PASS:** the complete [source-windows.md](source-windows.md), §§1–7,
was read. This is a written-proof audit beyond the earlier outline check.

The complex target norms are exactly
\[
 \frac{2h}{3}(\cosh(2r)-\cos\phi),\qquad
 \frac{2h}{3}(\cosh(2r)-\cos(\phi+\arg\eta)).
\]
The maximum over \(\phi\) of the smaller cosine is \(1/2\);
the threshold for every phase is \(-1\). These give the displayed
necessary and all-phase sufficient intervals with their exact centers,
widths and empty-window conditions. The real-place sine formulas and
the threshold \(q_\sigma\le3T^2/4\) also check out.

The circular-arc length formula was checked on both sides of
\(b=-1/2\), at \(b=-1\), and at the zero-measure endpoint
\(b=1/2\). A zero phase measure is correctly not interpreted as
absence of discrete phase returns. The torsion-fiber sum tests all
actual globally coupled phase vectors, not independent local phases.
Its value is independent of the representative chosen for a log vector.
The robust lower count requires all the stated real and complex source
conditions; it is not asserted for every source.

The real ellipse fraction \((\pi\sqrt3/8)^d\) is used only in
continuous geometry. No uniform growing-field lattice frequency is
deduced from it. The normalized-source scaling observation is likewise
a local geometric identity, not a source-distribution theorem.

Both finite-cover count inequalities were checked by integrating the
covering indicators. The first counts lattice points in inflated sets
and retains every offset. The second counts offset translates of an
eroded set; its erosion radius is the full \(3d\log B_0\). For a
coordinate box, any single coordinate can incur this whole error,
so an average-coordinate subtraction would be invalid. The note makes
none of these invalid substitutions. Its translated empty-box example
is explicitly abstract and is not identified with an actual necessary
source box, which always contains the identity log vector.

No mathematical correction was required. A clarity sentence was
added to spell out the change from actual unit phase coordinates
\(\theta\) to the shifted \(\chi\) and doubled/shifted \(\phi\)
used in the local conditions before defining the exact global phase
set. The added sentence was re-read and confirmed. This does not
change the formulas or the proof.

## 6. Audited stopping boundary

The new written proofs establish exact domains, orbit labels, moment
identities and two rigorously charged estimates. They do not establish
an exponential actual mean, a small lower tail, a reciprocal-return
saving, or either premise of MS-O2. They also do not refute any such
statement. The closed conclusions are only that the specified product
subbody lower estimate and ambient ideal-label upper estimate fail to
provide a positive rate with the bounds used.

Counting the **occupied** exact labels \((zR,N_{E/K}z)\) is precisely
the reciprocal-return route, by (3) and (5). It is an arithmetic
reformulation of the unresolved quantity; it is not a proved reduction
in its difficulty or evidence that the desired bound holds. No new
carrier or search is commissioned by recording this identity.

All reviews in §5 are internal symbolic proof checks. The specialist
executed no mathematical programs or finite scouts and did not reproduce
administrative repository checks. Historical reports remain unchanged.

## 7. Final main-report review

**PASS — independent complete written-file review.** The auditor read
the complete new [README.md](README.md), §§1–6, and checked it against
all three reviewed companions. The final phase-coordinate clarification
and incidence-table presentation corrections were confirmed separately.

The report correctly retains the following distinctions:

- MS-O1 is a frozen proved population input. The fields, order, actual
  scalar set, fixed radius, real embedding and exhaustive finite
  inventory are not changed.
- The source-dependent log intervals are necessary conditions; the
  actual global phases remain in the exact membership test. The
  all-phase sufficient boxes are conditional on their source
  restrictions, with no uncounted sources discarded.
- The optimized negative rate of the new discrete lower estimate is
  not an upper bound on true returns. The ambient ideal-label count
  fails only as the particular upper certificate stated. Neither
  failure is promoted to an actual no-gain theorem.
- Exhaustive order-unit orbit intersections, exact occupied joint
  labels, and the reciprocal-return sum count the same objects.
  Complete quadratic fibers may unite several such objects. This
  preserves the direction of the full-support inequality.
- The inverse-return implication permits a fixed prefactor and every
  strict exponent \(c<\gamma/B_*\). The explicit argument just after
  (10) verifies that the origin imposes no omitted restriction:
  any consistent premise forces \(\gamma\le2B_*\) asymptotically.
- The sole next recorded endpoint is MS-O2-I, the bound on the number
  of actually occupied labels \((zR_j,z\tau z)\), with fixed
  constants and every sufficiently large original level. It is exactly
  the inverse-return endpoint in arithmetic notation, not a geometric
  proxy, a claimed easier problem, or a new carrier. It is OPEN.
- Refuting that eventual endpoint would not by itself exclude a
  favorable unbounded subsequence or establish an actual quadratic-image
  lower bound. The stronger MS-O2 concentration assertion also remains
  OPEN. The earlier seed certificate, balanced-factor retirement and
  separate RC15/4 status are not changed.

No mathematical correction to the main report was required. The
proofs of MTR-A1–A2 and the independent reviews here establish
implications and validate the written scoped results; they do not
supply an unproved exponential return or label-count bound.

This final main-report review involved local reads and edits to this
new audit note only. Mathematical evaluations and research-program CPU
remain zero. It is not an external review, literature search, finite
experiment, or execution of the administrative validation described
elsewhere. A separate ledger or verification file is not presumed
inspected merely because it is linked from the main report.

## 8. Final ledger and machine-state consistency check

**PASS — read-only content review, 21 October 2026.** The auditor read
the complete newly added [ledger-verification.md](ledger-verification.md)
and [state.json](state.json), and compared their mathematical statements
and statuses with the accepted proofs and main report.

The constants, order/discriminant costs, source and target multiplicities,
actual sign baseline, two distinct certificate deficits, reciprocal
identity and conditional exponent range are consistent. MS-O1 remains
frozen and PROVED; MS-O2, its weaker tail and inverse endpoints, the
occupied-label bound, and an actual image saving remain OPEN. The
machine state does not retire the carrier or promote either failed
estimate to a theorem about true return growth. Its one next lemma has
the stated eventual all-level quantifiers and explicitly carries no
claim of truth, ease, or necessity for actual-image saving.

The reported zero mathematical evaluations/program CPU agree with the
scope of the symbolic work. Administrative validation results are still
pending in the reviewed ledger; this check does not mark them passed.
It does not execute a JSON validator, repository checker, preservation
comparison, regression or mathematical computation. The reported runtime,
preservation baseline and six dated handoffs were not independently
reproduced or exhaustively inspected in this limited review. No
mathematical or status correction was required. Only this new audit note
was updated.
