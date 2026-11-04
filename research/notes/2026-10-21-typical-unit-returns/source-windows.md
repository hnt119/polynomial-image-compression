# Source-dependent unit-return windows, with all phases retained

**21 October 2026 · T03 · MS-O2 authorized cycle · version 1.**
Fixed polynomial \(Q(x,y)=x^2+xy+y^2\). This companion keeps exactly
the fields, order, radius \(T_*\), coefficient carrier and finite unit
inventory frozen in the
[relative-unit population report](../2026-10-21-relative-unit-population/README.md).
It analyzes source-dependent domains; it does not redo MS-O1, change a
window, or perform moment calculations. No mathematical program, network
request, or nested delegation was used. This contribution charges zero
mathematical evaluations and zero research-program CPU seconds.

| Claim | Status and precise scope | Locator |
|---|---|---|
| MS2-W1 | PROVED: exact local return conditions at every complex and real place, including the phases of the actual global unit | §§2–3 |
| MS2-W2 | PROVED: translated necessary log boxes and phase-robust sufficient boxes, with an exact global torsion-fiber count and explicit limits on the sufficient region | §§4–5 |
| MS2-W3 | PROVED: what the frozen finite log-coset cover counts in a source window, including the translations and inflation/erosion losses | §6 |

These are exact identities and scoped counting implications. They neither
prove nor refute MS-O2's exponential mean and exponentially small relative
variance. The actual return tail, image bound and unrestricted T03 target
remain **OPEN** in this companion. No external novelty is asserted.

## 1. Fixed objects and inspected sources

Suppress the tower index \(j\), and write
\[
d=[F_j:\mathbb Q],\quad K=F_j(s),\quad s^3+s+1=0,
\quad E=K(\omega),\quad R=\mathcal O_K[\omega],\quad T=T_*.
\]
Here \(K\) has \(d\) real places and \(d\) complex places, and
\(\omega^2+\omega+1=0\). Write \(\tau\) for the involution of
\(E/K\). Let
\[
\mathcal G=\{u\in R^\times:u\tau(u)=1\},\qquad
\Lambda=\ell(\mathcal G)\subset\mathbb R^d,
\quad \mu_R=\ker\ell,\quad w_R=|\mu_R|.
\tag{1}
\]
The frozen facts are that \(\Lambda\) is a full lattice,
\(\mu_R\) is the finite torsion subgroup, and \(6\le w_R\le8d^2\).
The scalar carrier and inventory are exactly
\[
C=\{x\in\mathcal O_K:|\sigma(x)|\le T\text{ at all embeddings}\},
\quad A=\sigma_0(C),\quad n=|A|,
\]
\[
U=\{u\in\mathcal G:\|\ell(u)\|_1\le dL(T)\},
\qquad L(T)=\tfrac12\log(48T^6).
\tag{2}
\]
The fixed real embedding \(\sigma_0\) is injective; there are no
projection fibers. A nonzero source means \(p=(x,y)\in C^2\setminus
\{(0,0)\}\). Every returning order unit at such a source is already
in (2). Distinct returning units give distinct actual targets. At the
origin there is only one target, and the formulas involving logarithms
below are not used.

The complete current population report, its
[arithmetic companion](../2026-10-21-relative-unit-population/arithmetic.md)
MSU-A1–A3, and its
[geometry companion](../2026-10-21-relative-unit-population/geometry-audit.md)
MSU-G1–G3 were read for the unchanged definitions, covering statement and
counting limitations. The previous exact action and finite cutoff are
[MS-W1](../2026-10-20-mixed-signature/window-returns.md), §§2–3.
Those results are inherited here; no claim is made to have rerun their
proof programme or numerical evidence. Startup also inspected Git state,
setup/maps/migration limitations, the master/T03 state, T03 SPEC/STATUS,
and the relevant open-obligation entry. Historical files remain unchanged.

## 2. MS2-W1 — exact complex-place phase domain

Fix one representative complex place of \(K\), and its designated
extension to \(E\). Let \(\eta\in\{\omega,\omega^2\}\) be the
image of \(\omega\), and abbreviate the embedded source by \(x,y\).
Put
\[
z=x-\eta y,\qquad w=x-\eta^2y,\qquad
h=|zw|=|Q(x,y)|>0,
\]
\[
c_p=\tfrac12\log\frac{|w|}{|z|},\qquad
t=\nu^+(u)=e^{\lambda+i\theta},\qquad
r=\lambda-c_p,
\]
\[
\phi=2\theta+\arg z-\arg w\pmod{2\pi},\qquad
\gamma=\arg\eta=\pm2\pi/3\pmod{2\pi}.
\tag{3}
\]
Nonvanishing follows from \(\omega\notin K\): a zero embedded
eigencoordinate would force the corresponding global algebraic element
to vanish and hence \(x=y=0\). Also \(Q(x,y)\ne0\), since its image
at a real place is positive for a nonzero source.

The exact norm-one action is \((z,w)\mapsto(tz,t^{-1}w)\).
Writing \(Z=tz\), \(W=t^{-1}w\), its target coordinates are
\[
y'=\frac{W-Z}{\eta-\eta^2},\qquad
x'=\frac{\eta W-\eta^2Z}{\eta-\eta^2}.
\tag{4}
\]
Their magnitudes satisfy
\[
|Z|=\sqrt h\,e^r,\quad |W|=\sqrt h\,e^{-r},\quad
\arg Z-\arg W=\phi,
\]
and therefore
\[
\boxed{
|y'|^2=\frac{2h}{3}\bigl(\cosh(2r)-\cos\phi\bigr),\qquad
|x'|^2=\frac{2h}{3}\bigl(\cosh(2r)-\cos(\phi+\gamma)\bigr).
}
\tag{5}
\]
For example the second equality follows by factoring \(\eta\) out
of \(\eta W-\eta^2Z\); the cross term then has angle
\(\arg(\eta Z)-\arg W=\phi+\gamma\).

Define
\[
b_p(r)=\cosh(2r)-\frac{3T^2}{2h}.
\]
The complex-place return condition is **exactly**
\[
\boxed{\cos\phi\ge b_p(r),\qquad
       \cos(\phi+\gamma)\ge b_p(r).}
\tag{6}
\]
The same actual \(u\) supplies \(\lambda\) and \(\theta\).
Choosing a phase that satisfies (6) is not permission to replace the
phase of a global algebraic unit.

### Phase-feasible and phase-robust log intervals

For the two angles separated by \(2\pi/3\),
\[
\max_\phi\min\{\cos\phi,\cos(\phi+\gamma)\}=\tfrac12.
\tag{7}
\]
To verify the upper bound, their average is
\(\tfrac12\cos(\phi+\gamma/2)\le\tfrac12\), after choosing
\(\gamma=\pm2\pi/3\); equality is attained at
\(\phi=-\gamma/2\). Thus there exists a local phase satisfying
(6) if and only if \(b_p(r)\le1/2\). Since \(h\le3T^2\) for a
source in the bidisk, this gives the nonempty translated interval
\[
\boxed{
I_p^{\rm feas}=[c_p-a_p,c_p+a_p],\qquad
a_p=\tfrac12\operatorname{arcosh}\frac{3T^2+h}{2h}.
}
\tag{8}
\]
It is a necessary interval for an actual unit return, not a sufficient
one. It contains zero because the identity unit returns at the source.

Every possible local phase satisfies (6) if and only if
\(b_p(r)\le-1\): one cosine can attain \(-1\), and both are always
at least \(-1\). Equivalently
\[
\sqrt h(e^r+e^{-r})\le\sqrt3T.
\]
Consequently the exact interval that is robust under **all** local
phases is
\[
\boxed{
I_p^{\rm rob}=[c_p-b_p^*,c_p+b_p^*],\qquad
b_p^*=\operatorname{arcosh}\frac{\sqrt3T}{2\sqrt h},
\quad h\le\frac{3T^2}{4}.
}
\tag{9}
\]
When \(h>3T^2/4\), this phase-robust interval is empty. The notation
\(b_p^*\) in (9) is the half-width, distinct from the threshold
function \(b_p(r)\) in (6). The interval (9) need not contain zero:
the source's existing phase can work even when other phases at the same
logarithm do not.

For reference, the older direct necessary interval is
\[
\log\frac{|w|}{2T}\le\lambda\le
\log\frac{2T}{|z|}.
\tag{10}
\]
Equation (8) sharpens it. Indeed any phase-feasible target lies in the
bidisk, and hence obeys the same \(|tz|,|t^{-1}w|\le2T\) inequalities
which prove (10).

### Exact local phase length, without a statistical inference

Let \(J(b)=\{\phi:\cos\phi\ge b,\ \cos(\phi+\gamma)\ge b\}\)
on the circle. For \(-1<b\le1/2\), put \(\alpha=\arccos b\).
Intersecting the two circular arcs of half-width \(\alpha\), whose
centers are separated by \(2\pi/3\), gives
\[
\operatorname{length}J(b)=
\begin{cases}
2\pi,& b\le-1,\\
4\alpha-2\pi,& -1<b<-1/2,\\
2\alpha-2\pi/3,& -1/2\le b\le1/2,\\
0,& b>1/2.
\end{cases}
\tag{11}
\]
For \(\alpha\le2\pi/3\), only the shorter center-to-center overlap
contributes, of length \(2\alpha-2\pi/3\). For larger \(\alpha\),
the opposite overlap adds \(2\alpha-4\pi/3\). This proves (11).
The map \(\theta\mapsto2\theta+\arg z-\arg w\) preserves normalized
circle measure, so (11) also gives the fraction of unrestricted local
phases. It does **not** count algebraic units. At \(b=1/2\), the allowed
finite phase set has measure zero but may still contain actual unit
phases; it must not be discarded in a discrete argument.

## 3. Exact real-place phase domain

At a real place, choose the extension sending \(\omega\) to
\(e^{2\pi i/3}\). Put
\[
q_\sigma=Q(\sigma x,\sigma y)>0,\quad
z_\sigma=\sigma x-\omega\sigma y
=\sqrt{q_\sigma}\,e^{i\psi_\sigma},\quad
\nu_\sigma(u)=e^{i\theta_\sigma}.
\]
The relative norm condition forces modulus one here. With
\(\chi=\psi_\sigma+\theta_\sigma\), decoding gives
\[
y'=-\frac{2\sqrt{q_\sigma}}{\sqrt3}\sin\chi,
\qquad
x'=\frac{2\sqrt{q_\sigma}}{\sqrt3}\sin(\chi+\pi/3).
\tag{12}
\]
Thus the exact real-place return condition is
\[
\boxed{
|\sin\chi|\le\frac{\sqrt3T}{2\sqrt{q_\sigma}},\qquad
|\sin(\chi+\pi/3)|\le\frac{\sqrt3T}{2\sqrt{q_\sigma}}.
}
\tag{13}
\]
Equivalently it is (6) with \(r=0\), \(h=q_\sigma\) and
\(\phi=2\chi\). It holds for every phase exactly when
\[
\boxed{q_\sigma\le3T^2/4.}
\tag{14}
\]
When (14) fails, the log vector contains no coordinate at this real
place that could repair the failure: the actual unit phase is essential.
The identity phase still works at the original source. A norm-preserving
rotation is not automatically a return to the real coordinate square.

## 4. MS2-W2 — exact global count and sufficient boxes

For each complex place form the intervals (8) and (9), and set
\[
\mathcal B_p^{\rm feas}=\prod_{i=1}^d I_{p,i}^{\rm feas},\qquad
\mathcal B_p^{\rm rob}=\prod_{i=1}^d I_{p,i}^{\rm rob},\qquad
\mathcal H=\{\lambda:\|\lambda\|_1\le dL(T)\}.
\tag{15}
\]
An empty factor makes \(\mathcal B_p^{\rm rob}\) empty. The necessary
box contains the origin, but its centered margin
\(\min_i(a_{p,i}-|c_{p,i}|)\) need not have a positive lower bound.
For instance the local bidisk source \(x=y=T\) has
\(h=3T^2,c_p=0,a_p=0\). This is a local boundary example, not a claim
about the frequency of that source in the algebraic carrier.

For each \(\lambda\in\Lambda\), choose one unit \(u_\lambda\)
with that logarithm. Its unit preimages are exactly
\(u_\lambda\mu_R\). Let \(\Theta(u)\) record the actual phase of
\(u\) at each of the chosen real and complex extensions; it is a
vector in a \(2d\)-dimensional circle torus. Let
\(\mathcal P_p(\lambda)\) be the product of the exact real phase
sets (13) and complex phase sets (6) at logarithm \(\lambda\).
These sets are expressed in the **actual unit phase coordinates**
\(\theta\): substitute \(\chi=\psi_\sigma+\theta_\sigma\) at each
real place and \(\phi=2\theta+\arg z-\arg w\) at each complex place.
Then the distinct actual return count is **exactly**
\[
\boxed{
R(p)=\sum_{\lambda\in\Lambda\cap\mathcal H\cap
\mathcal B_p^{\rm feas}}
\#\{\zeta\in\mu_R:
\Theta(u_\lambda)+\Theta(\zeta)\in\mathcal P_p(\lambda)\}.
}
\tag{16}
\]
All inequalities in these sets are closed; boundary returns are retained.
Changing the chosen \(u_\lambda\) permutes the torsion labels and leaves
(16) unchanged. The phase vectors in a logarithmic fiber form a translate
of a finite globally coupled torsion subgroup. They are not independent
continuous choices at the different embeddings.

To prove (16), every candidate order unit has exactly one logarithm in
\(\Lambda\cap\mathcal H\). Local decoding (4) and (12), together
with its integral matrix, says that it returns if and only if all stated
phase inequalities hold. Each returning unit gives a distinct target at
a nonzero source. Thus no labels or stabilizers have been mistaken for
distinct returns. This also proves the upper bound
\[
R(p)\le w_R\,|\Lambda\cap\mathcal H\cap\mathcal B_p^{\rm feas}|.
\tag{17}
\]

There is a rigorous phase-independent sufficient lower bound. If
\(q_\sigma\le3T^2/4\) at **every** real place, then
\[
\boxed{
R(p)\ge w_R\,|\Lambda\cap\mathcal H\cap\mathcal B_p^{\rm rob}|.
}
\tag{18}
\]
Indeed (9) handles every complex phase and (14) handles every real phase,
so all \(w_R\) units over each counted log vector return. If one real
condition fails, (18) is not asserted; actual returns still use (16).
The explicit cutoff in (18) is safe. In fact any global order unit
satisfying all these robust conditions automatically obeys that cutoff,
by the frozen norm bound on actual nonzero returns.

## 5. Limits of the phase-robust sufficient region

These restrictions are conditions on sources in the **unchanged**
carrier, not a newly selected input carrier. No source is silently
discarded in an image estimate.

The real phase-robust source region can already be small in continuous
geometry. In one real square \([-T,T]^2\), the ellipse
\(Q(x,y)\le3T^2/4\) is entirely contained in the square. Indeed
\(Q=(y+x/2)^2+3x^2/4\ge3x^2/4\), and likewise for \(y\).
Its area is
\[
\frac{\pi(3T^2/4)}{\sqrt{3/4}}
=\frac{\pi\sqrt3}{2}T^2,
\]
so its square-area fraction is \(\pi\sqrt3/8<1\). Consequently,
even ignoring all complex restrictions, the sufficient all-phase source
region in the product Minkowski square has volume fraction at most
\[
\left(\frac{\pi\sqrt3}{8}\right)^d.
\tag{19}
\]
This is a continuous-volume statement, not an estimate for the actual
lattice source fraction at fixed \(T_*\) along the tower. No uniform
equidistribution has been proved, so (19) is not used as a discrete
exceptional-set obstruction or a refutation of MS-O2.

Also, all interval centers and widths in (8)–(9), and the phase thresholds
in (13), depend only on the normalized local source \((x/T,y/T)\).
Scaling a local source and its window radius together does not enlarge
these local log windows. The very large fixed \(T_*\) proving MS-O1
therefore does not, by itself, make the return windows of geometrically
similar sources wider. Neither a near-full robust-source count nor a
useful count in (18) follows from the population theorem.

## 6. MS2-W3 — what the frozen finite coset cover can count

Use the unchanged arithmetic constants \(B_0,g=\log B_0,J_0\) from
MSU-A1. Its proved cover is
\[
\mathbb R^d=\bigcup_{k\le J_0^d}
\bigl(c_k+\Lambda_E+\mathbb B_1(3dg)\bigr).
\]
The order-log sublattice has index at most \(27^d\). Splitting each
\(\Lambda_E\) coset into order-log cosets gives, for some offsets
\(v_1,\ldots,v_M\),
\[
\boxed{
\mathbb R^d=\bigcup_{k=1}^M
\bigl(v_k+\Lambda+\mathbb B_1(H_0)\bigr),
\qquad M\le(27J_0)^d,\quad H_0=3dg.
}
\tag{20}
\]
This simply expresses the inherited cover in the order lattice. It is
not another order-index loss in the already established covolume bound.
The offsets need not be bounded representatives; changing them modulo
\(\Lambda\) does not affect the cover.

### Exact count supplied by the covering statement

For any compact \(D\subset\mathbb R^d\), let
\(B=\mathbb B_1(H_0)\). Integrating the covering indicators over \(D\)
gives the rigorous inequality
\[
\boxed{
\sum_{k=1}^M|\Lambda\cap(D+B-v_k)|
\ge\frac{\operatorname{vol}D}{\operatorname{vol}B}.
}
\tag{21}
\]
To prove it, a covering ball centered at \(v_k+\lambda\) can meet
\(D\) only if \(\lambda\in D+B-v_k\), since \(B\) is symmetric.
Its intersection with \(D\) has volume at most \(\operatorname{vol}B\).
Summing these intersection volumes bounds the covering integral above,
while that integral is at least \(\operatorname{vol}D\).

For an uninflated set, define its erosion
\(D\ominus B=\{x:x+B\subseteq D\}\). Applying the same argument
over this eroded set yields
\[
\boxed{
\sum_{k=1}^M|\Lambda\cap(D-v_k)|
\ge\frac{\operatorname{vol}(D\ominus B)}{\operatorname{vol}B}.
}
\tag{22}
\]
Indeed any covering-ball center within distance \(B\) of an eroded
point lies in \(D\). For a box
\(D=\prod_i[c_i-b_i,c_i+b_i]\), its erosion is empty if any
\(b_i<H_0\); otherwise it is exactly
\(\prod_i[c_i-(b_i-H_0),c_i+(b_i-H_0)]\). Each coordinate can bear
the whole \(\ell^1\)-error \(H_0\), so replacing this by an average
coordinate loss would be invalid.

### Why these are not yet the counts in (17) or (18)

There are three distinct gaps:

1. Equations (21)–(22) count a sum over the offsets \(v_k\), while
   (17)–(18) require the actual lattice in the particular source box.
   A favorable offset need not be the required one. The arithmetic
   labels \(((a),a\tau(a))\) retain exactly the information giving
   these offsets; dropping them does not turn their representatives
   into norm-one units returning at the source.
2. Inflation in (21) can destroy the return inequalities and can leave
   the finite inventory \(\mathcal H\). In (22) the erosion radius
   is \(3dg\), while no corresponding lower bound for every source
   half-width is established. The erosion can be empty.
3. The covering theorem records logarithmic moduli only. Even a correct
   log-box count does not supply the coupled phase tests in (16), unless
   the stronger hypotheses of (18) have been proved for those sources.

The logical translation issue is real even for much simpler lattices:
\(\mathbb Z^d+\mathbb B_1(d/2)=\mathbb R^d\) is a one-coset cover
with covolume 1, yet the translated box
\((1/2,\ldots,1/2)+[-1/4,1/4]^d\) contains no lattice point.
This is only a counterexample to a general inference from a covering or
covolume bound to arbitrary translated-box counts. It is not asserted
to be the actual unit lattice or a realized source box. Necessary source
boxes contain zero, but this ensures the identity log vector only; it
does not supply exponentially many points with valid phases.

Thus the frozen finite cover remains valid and useful for MS-O1. Its
present exact consequence for source windows is (21)–(22), not a
lower count of actual source returns. No failure of a stronger,
source-specific arithmetic argument is asserted.

## 7. Cost and evidence ledger

| Item | Accounting in this contribution |
|---|---|
| Carrier/radius | Exactly the frozen \(C_j(T_*)\); no change, thinning, correlated window, or new scale. The inherited actual input bounds remain in force. |
| Whole scalar identity | Equations (4)–(6) and (12) are exact at every embedding; both coordinates are checked. No independent local rotations are realized as a global unit. |
| Unit inventory | The existing finite \(U_j(T_*)\) is retained. Actual distinct targets are counted freely at nonzero sources; the zero target is separate. |
| Torsion and phase multiplicity | Every logarithm has exactly \(w_R\) unit preimages. Formula (16) tests their actual coupled phase vectors; polynomially bounded torsion is not silently replaced by independent phase choices. |
| Order and coset labels | Order passage is inherited. The explicit \(M\le(27J_0)^d\) in (20) is a cover count, not an additional covolume penalty. Offsets remain in (21)–(22). |
| Window loss | The complete half-widths and empty-window conditions are (8), (9), (14). Inflation/erosion costs \(3dg\) are retained. Real and complex restrictions both remain. |
| Lattice versus volume | (11) and (19) are continuous geometric facts only. No growing-field fixed-radius equidistribution or phase-distribution theorem is inferred. |
| Full-pair coverage | The necessary criterion and exact formula cover every nonzero pair; the sufficient box is expressly conditional on its source restrictions. No uncounted source region is discarded. |
| Rates and output | No positive mean exponent, variance exponent, return exponent, or full-image saving is established here. Moment work belongs to the other assigned contribution. |

The formulas and cover-count implications are new internal symbolic
derivations within the frozen setup. The independent auditor checked the
complex threshold and real-place formulas before the full note was saved,
then inspected the complete written MS2-W1–W3 proofs and reported a pass.
The review included the phase-length endpoints, exact torsion-fiber sum,
conditional robust lower bound, continuous-only ellipse calculation and
both covering inequalities. Its phase-coordinate clarity suggestion was
incorporated before (16). This is internal proof review, recorded in the
cycle's audit companion. No
program output or finite scout is cited as proof, and no historical file
was edited. The exact remaining gap is a source-specific count of the
global units satisfying (16), with the required coverage across actual
algebraic lattice pairs. This companion does not claim that gap is
impossible or solved.
