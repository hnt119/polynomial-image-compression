# Actual discrete lower incidences and their signed deficit

21 October 2026 · T03 · version 1.
Fixed \(Q=x^2+xy+y^2\); unchanged fields, order, scalar carrier and \(T_*\).

**PROVED:** a lower bound for the number of actual nonzero sources returned
by each unit, with all places and the lattice determinant charged.
**OPEN:** an exponential lower mean or small lower tail. Optimizing the
estimate below with the frozen population theorem gives a strictly
negative guaranteed mean rate. This is a limitation of the estimate,
not an upper bound on actual returns.

The lead derived this proof; the independent auditor checked the local
volumes, Jacobians, lattice normalization and origin subtraction.
No mathematical program or numerical volume calculation was performed.

## 1. Fixed notation and dependencies

Suppress \(j\), write \(d=d_j\), \(T=T_*\), and
\[
W_T=[-T,T]^d\times\{z\in\mathbb C:|z|\le T\}^{d},\qquad
C=\mathcal O_K\cap W_T.
\]
Let \(n=|C|=|A|\), \(N=n^2-1\), and
\[
\mathcal G=\{u\in\mathcal O_K[\omega]^\times:u\tau u=1\},\quad
H(u)=\|\ell(u)\|_1,\quad
U=\{u\in\mathcal G:H(u)\le dL(T)\}.
\]
The complete nonzero source domain is
\[
D_u=\{p\in C^2\setminus\{0\}:M_up\in C^2\}.
\]
This agrees with the problem's domain through the injective real
embedding. No favorable subset replaces \(C\).

Use the frozen field degree/signature and scalar bounds:
\[
[K:\mathbb Q]=3d,\quad \operatorname{sig}(K)=(d,d),\quad
|\Delta_K|\le D_*^{3d},\quad
n\le(2T+1)^{3d}.
\]
The frozen centered unit count, with the already proved relative
order covolume bound, is
\[
\#\{u\in\mathcal G:H(u)\le dh\}
\ge\frac{w_j(dh)^d}{d!K_R^d}\quad(h>0).
\tag{1}
\]
This is an application of MS-O1's established estimates, not a
new population proof. The order index is already in \(K_R\).

## 2. MTR-L1 — a genuine discrete lower bound

Set
\[
\beta_0=\frac{3\sqrt3\,\pi^3}{512},\qquad
\Theta_T=\frac{\beta_0T^6}{D_*^3}.
\]
For every actual unit \(u\in\mathcal G\),
\[
\boxed{|D_u|+1\ge
\left(\frac{3\sqrt3\,\pi^3}{512}\right)^d
\frac{T^{6d}}{|\Delta_K|}e^{-2H(u)}
\ge \Theta_T^d e^{-2H(u)}.}
\tag{2}
\]
The \(1\) is the origin in this one domain, not one correction for the
whole sum over units.

**Proof.** Let
\[
P_u=W_T^2\cap M_u^{-1}W_T^2
\]
in the real \(6d\)-dimensional pair Minkowski space. It is bounded,
convex and centrally symmetric.

At a real place of \(K\), the ellipse
\[
Q(x,y)\le 3T^2/4
\]
is contained in \([-T,T]^2\). Indeed
\(Q=(y+x/2)^2+3x^2/4=(x+y/2)^2+3y^2/4\).
It is invariant under the actual norm-one action there, independently
of its phase. Its area is
\[
\frac{2\pi}{\sqrt3}\frac{3T^2}{4}
=\frac{\sqrt3\pi}{2}T^2.
\tag{3}
\]

At a complex place use \(z=x-\eta y,\ w=x-\eta^2y\), where
\(\eta\in\{\omega,\omega^2\}\). The inverse formulas are
\[
y=\frac{w-z}{\eta-\eta^2},\qquad
x=\frac{\eta w-\eta^2z}{\eta-\eta^2}.
\]
Thus \(|z|,|w|\le\sqrt3T/2\) imply \(|x|,|y|\le T\).
If the unit value is \(t\), with \(\lambda=\log|t|\), choose the
product of disks
\[
|z|\le\frac{\sqrt3T}{2}\min(1,e^{-\lambda}),\qquad
|w|\le\frac{\sqrt3T}{2}\min(1,e^\lambda).
\tag{4}
\]
Both the source eigen-coordinates and the target \(tz,t^{-1}w\)
have modulus at most \(\sqrt3T/2\). Hence (4) belongs to the
actual intersection, for every phase of this global unit. This
does not choose any local unit independently.

The complex determinant of the coordinate map has modulus \(\sqrt3\),
so its real Jacobian is 3. The volume of (4) in scalar \((x,y)\)
coordinates is
\[
\frac{\pi^2}{3}\left(\frac{\sqrt3T}{2}\right)^4
e^{-2|\lambda|}
=\frac{3\pi^2}{16}T^4e^{-2|\lambda|}.
\tag{5}
\]
Multiplying the \(d\) real and \(d\) complex lower volumes gives
\[
\operatorname{vol}(P_u)\ge
\left(\frac{3\sqrt3\pi^3}{32}\right)^d
T^{6d}e^{-2H(u)}.
\tag{6}
\]

For any symmetric convex body \(P\) in a lattice space,
centered Blichfeldt averaging gives
\[
\#(\Lambda\cap P)\ge
\frac{\operatorname{vol}(P/2)}{\operatorname{covol}(\Lambda)}.
\tag{7}
\]
To see this, some translate of \(P/2\) contains at least its
volume-to-covolume ratio of lattice points. Subtract one of those
points from all of them; the differences are distinct and lie in
\(P\). This is not a translated-window equidistribution assertion.

Here \(\Lambda=\mathcal O_K^2\) has covolume
\(2^{-2d}|\Delta_K|\); half-scaling in dimension \(6d\) costs
\(2^{-6d}\). Apply (7) to (6). The lattice points in \(P_u\)
are precisely \(D_u\) and the origin, since \(M_u\) is integral.
This proves (2). \(\square\)

## 3. MTR-L2 — actual first-moment certificate and optimization

For any fixed
\[
0<h\le L(T),\qquad \log\Theta_T>2h,
\tag{8}
\]
the subset \(V_j(h)=\{u:H(u)\le dh\}\) is used only to lower-bound
incidences from the unchanged full inventory \(U_j\).
For all sufficiently large \(d\), (2) yields
\[
|D_u|\ge\tfrac12\Theta_T^d e^{-2hd}\quad(u\in V_j(h)),
\]
because the unsubtracted bound is uniformly at least 2.
Using (1) and \(N\le(2T+1)^{6d}\) therefore gives the **actual**
nonzero-pair mean lower bound
\[
\boxed{\mu_j=\frac{\sum_{u\in U_j}|D_u|}{N_j}
\ge \frac{w_j}{2}\frac{d_j^{d_j}}{d_j!}
\left(\frac{P_T h e^{-2h}}{K_R}\right)^{d_j},}
\qquad
P_T=\frac{\beta_0}{D_*^3(2+1/T)^6}.
\tag{9}
\]
This sums exact lattice source domains and subtracts the origin before
summing; it does not use a continuous-overlap upper estimate as a lower
bound.

The guaranteed logarithmic rate of (9) is
\[
\rho_{\rm cert}(h)=\log P_T+1+\log h-C_R-2h,\qquad
C_R=\log K_R.
\tag{10}
\]
Its maximum over all \(h>0\) occurs at \(h=1/2\), giving
\[
\boxed{\sup_{h>0}\rho_{\rm cert}(h)
=\log\frac{P_T}{2K_R}<0.}
\tag{11}
\]
Indeed \(\beta_0<1\), \(D_*\ge1\), \(K_R>1\), and
\((2+1/T)^6>1\). No numerical approximation is required.
The maximizing value is admissible: the frozen \(L(T_*)\ge2K_R>1/2\),
and \(T\ge2\sqrt{D_*}\) implies
\(\Theta_T\ge3\sqrt3\pi^3/8>e\). Thus (8) holds at \(h=1/2\).

**Meaning — FAILED IN STATED SCOPE.** This specific combination of the
phase-independent product-body lower bound, centered lattice packing,
frozen regulator upper bound and worst-case input upper count supplies
no exponential mean gain. The negative number in (11) is the rate of a
lower certificate, not a bound above on \(\mu_j\). It refutes neither
MS-O2 nor a weaker tail or inverse-moment estimate.

The unconditional pointwise baseline is actually \(R_j(p)\ge2\)
for every nonzero pair: \(1,-1\in U_j\), the scalar carrier is centrally
symmetric, and \(p\ne-p\). Hence \(\mu_j\ge2\).
Coordinate swap is not credited automatically as an order-unit action.
It preserves \(Q\), but its multiplier may be a nonintegral field ratio.

## 4. Costs and stopping point

This lower incidence calculation pays:

- every real and complex embedding constraint;
- actual global phases through phase-independent sufficient subbodies;
- the \(6d\)-dimensional half-body factor;
- the actual pair-lattice covolume;
- the frozen relative regulator and order index, once;
- the input upper count and the origin for each action.

It does not thin or redefine \(A_j\). It selects a smaller set only
inside an intersection used to lower-bound one incidence count.
No claim is made that those interior subbodies cover typical sources.
Since no exponential actual first-moment gain is established by this
route, no lengthy second-moment estimate is built on it.
The exact orbit/inverse formulation in the companion remains available,
with its required arithmetic label-count bound OPEN.
