# T02 — the quartic and the difference between local savings and global compression

Prepared 2026-09-14 from the record frozen through 2026-09-10. Target:

\[
P_4(x,y)=(x+2y)^4+3x-y.
\]

**OPEN.** No recorded construction establishes a fixed power saving for the
entire image of arbitrarily large same-set inputs. This note explains existing
arguments; it does not extend their scope or rerun their computations.

## What the two papers contributed

The shared work supplied number-field carriers, bounded real projections,
direct products of units and lattice points, and a quantitative way to charge
input density against output density. T02 tested whether a special local
quartic image could make those carriers compress. The central progress was
increasingly precise local counting, followed by a precise identification of
why a specified global packing argument cannot use that saving successfully.
See [shared foundations](00-shared-foundations.md), **S-A**, and **S-T02**.

## SN-T02-1 — the hybrid carrier and the determinant-seven relation

**PROVED, reported; definitions and counting explanation inspected.** Track
T02, fixed quartic above. Sources: **S-T02**, §§2–4; **S-T02-FINAL**;
**S-C2-LOG**. These are existing conclusions, not a new proof audit.

Earlier work considered the deformation
$F_Q(x,y)=(x+2y)^4+Q^3(3x-y)$, for which
$F_Q(Qx,Qy)=Q^4P_4(x,y)$. The later C4 carrier uses $Q=1$.
This scaling identity is necessary when moving between the deformation and
the fixed target; a theorem about variable coefficients alone would not suffice.

The C2 hybrid uses positive units and a translated box with parameters chosen
to make the representation of each input unique. For a ratio $u=g_1/g_2$ and
scale $v=g_2$, a pair of box elements contributes

\[
K_u=\{((ut_1+2t_2)^4,\;3ut_1-t_2):t_1,t_2\in T\},
\qquad v^4\alpha+Q^3v\beta.
\]

The recorded positivity hypotheses give $|K_u|=|T|^2$. Also
$\sum_u|G(u)|=|G|^2$. Thus simply counting these parameters gives the original
$|A|^2$ pair count. Compression requires overlaps between their scalar outputs.
This parameter calculation is **not** an actual-image lower bound.

The useful local relation appears under the linear change

\[
(t_1,t_2)\longmapsto (a,b)=(ut_1+2t_2,\;3ut_1-t_2).
\]

For integral unit $u$, its determinant is $-7u$ and its image satisfies
$a+2b\in7\mathcal O$. The index is $7^d$ in degree $d$.
The determinant relation and its scalar residue consequence describe the same
restriction: they cannot be charged as two independent savings.

## SN-T02-2 — what C3 and C4 actually prove locally

**PROVED, reported; C4 local argument inspected for exposition.** Sources:
**S-C3-LOG**, **S-C4**, §§2–5, and **S-T02-FINAL**.

At the first ramified level, the scalar map is
$h_s(z)=2z^4+sz$, $s\in\{1,-1\}$, over
$R=\mathbb F_7[\pi]/(\pi^3)$. Four regular residue classes contribute 49 images
each and three critical classes contribute four each: $208$ images in total.
C3 proves analytically, for every nonempty $E\subset R$, the bound

\[
\frac{343\,|h_s(3E-E)|}{|E|^2}\ge\frac47.
\]

Equality occurs for a full critical fiber $E=a+\pi R$, $a^3=-s$.
The archived structured enumeration supports the investigation; it was not an
enumeration of all $2^{343}$ subsets and is not the proof of this universal claim.

C4 follows a full critical fiber to higher precision in an actual local ring:
$7\mathcal O=\mathfrak p^3$, residue degree one,
$R_m=\mathcal O/\mathfrak p^{3m}$, and
$E_m=(\alpha+\mathfrak p)\bmod\mathfrak p^{3m}$, where $\alpha$ is the
integer lift of one of $3,5,6$ and $\alpha^3=-1\bmod\mathfrak p$. Then

\[
|R_m|=7^{3m},\quad |E_m|=7^{3m-1},\quad
N_m:=|P_4(E_m,E_m)|=
\begin{cases}4&m=1,\\22\,7^{3m-4}&m\ge2.\end{cases}
\]

Here is the mechanism behind the number 22. Set $L=x+2y$, so

\[
P_4(x,y)=g(L)+\frac72x,\qquad g(L)=L^4-\frac12L.
\]

The independent variables range through
$(3\alpha+\mathfrak p)\times(\alpha+\mathfrak p)$.
The second summand fills a translate of $\mathfrak p^4$. Expanding $g$ about
$L_0=3\alpha$ and writing the increment as $\pi b+\pi^2c$, the relevant
terms modulo $\mathfrak p^4$ are (the linear term vanishes because
$g'(L_0)\in7\mathbb Z_7\subset\mathfrak p^3$)

\[
A_0b^2\pi^2+(2A_0bc+B_0b^3)\pi^3,
\qquad A_0=6L_0^2,\quad B_0=4L_0.
\]

$A_0$ is a unit. The case $b=0$ gives one class; the three nonzero squares
$b^2$ each allow seven next coefficients. Hence $1+3\cdot7=22$.
The local image consists of three shallower cosets and one deeper coset.
Lifting them yields the formula for every $m\ge2$.
At these higher levels the ring has mixed characteristic; replacing it by a
longer truncated polynomial ring over $\mathbb F_7$ would change the problem.

Normalize the image density by the square of the input density:

\[
\Psi_m=\frac{N_m/|R_m|}{(|E_m|/|R_m|)^2}
=\begin{cases}4/7&m=1,\\22/49&m\ge2.\end{cases}
\]

There is an improvement at the second level and then saturation. Increasing
precision does not repeatedly earn a fresh factor $22/49$.
C4 counts this specified full fiber; it is not a theorem optimizing every
subset at every higher precision.

## SN-T02-3 — why the specified global certificate is retired

**FAILED, for the stated full-interval packing certificate; PROVED, reported
failure inequality.** Sources: **S-C4**, §§6–8; **S-C4-RATE**;
**S-T02-FINAL**. No actual-image lower bound follows from this failure.

For the recorded totally real tower, let $D$ be its fixed root discriminant
and let $I_j$ be the product of primes above seven. Its norm is $7^{d/3}$.
The carrier is the real projection of

\[
C_j=-1+\{u\in I_j: |\sigma(u)|\le X\text{ for every real embedding}\}.
\]

The lower input exponent is
$a=\log X-\frac13\log7-\frac12\log D$, with upper count $(2X+1)^d$.
The chosen $X=2\,7^{1/3}\sqrt D$ gives $a=\log2$.
Projection through a fixed real embedding is injective.
Membership in a local fiber does not assert that this bounded carrier fills it.

The full archimedean output interval has width
$W=81(X+1)^4+\frac32X+\frac{27}{16}$.
Combining this interval with the local support gives the upper certificate

\[
U_m=N_m^{d/3}(1+W/7^m)^d.
\]

For $m\ge2$, its signed rate gap is

\[
\kappa_m=\log\frac{X^2}
{D(22/49)^{1/3}(W+7^m)}<0.
\]

The quartic width overwhelms the fixed local gain. The final record also
retires saturation mixtures and finite covers of the entire local product
when every branch is charged by the specified full interval and uniform norm
packing, within the stated equal-radius carrier scope. A lower bound on the
size of this *upper certificate* does not show the actual image is large.

## SN-T02-4 — the precise remaining task

**OPEN.** Source: **S-C4-RATE**, final obligation; **S-T02-FINAL**.
One needs a new, fully charged bound for the actual carrier or an explicitly
thinned subcarrier. If thinning costs $e^{-\eta d}$ in input size, the pair
budget loses $2\eta d$. A sufficient certificate would bound the whole image
by $\exp((2(a-\eta)-\varepsilon)d+o(d))$, with fixed
$0\le\eta<a$ and $\varepsilon>0$, while preserving upper and lower input
counts. All branches and uncovered pairs must be included.

The record supplies no witness meeting this obligation. Local C4 counting
remains progress even though its specified global application fails.
The C4 acceptance record covers its named materials; it does not constitute
external acceptance of every companion argument or of the target itself.

## Recall check

1. Why divide output density by **squared** input density? **Restricting the
   same input set restricts both coordinates.**
2. Does deeper precision give unbounded savings? **No: $\Psi_m=22/49$ for
   every $m\ge2$ in this full-fiber construction.**
3. What failed globally? **A specified interval-and-congruence upper
   certificate, not every possible construction for the quartic.**
