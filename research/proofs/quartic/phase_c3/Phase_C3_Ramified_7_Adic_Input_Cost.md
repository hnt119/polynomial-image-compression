# Phase C3: Ramified 7-adic input-cost optimization

## Opening decision

The local optimization is settled analytically. For either sign and every
nonempty subset of \(R=\mathbb F_7[\pi]/(\pi^3)\),
\[
\min_E\Phi_s(E)=\frac47,\qquad
\Phi_s(E)=\frac{343|h_s(3E-E)|}{|E|^2},\quad h_s(z)=2z^4+sz.
\]
Equality holds exactly for the three full critical fibers
\(E=a+\pi R\), \(a^3=-s\). This is proved within the supplied offline
source system, not inferred from finite experiments.

The exact second minimum is \(343/576\), attained precisely by removing
one point from a critical full fiber. Among sets meeting at least two
residue fibers, the exact minimum is \(208/343\), attained only by \(R\).
These also give a sharp finite stability gap.

The best local gain is
\[
\gamma_*=\frac13\log\frac74\approx0.186539.
\]
It is insufficient for the audited global certificates:

| Required question | Answer |
|---|---|
| Exact minima in the proved classes? | All sets and complete residue-fiber unions: \(4/7\); multifiber sets: \(208/343\); nonminimizers: \(343/576\). |
| Is the universal bound proved? | Yes, analytically for every nonempty subset and both signs. |
| All proved equality cases? | Respectively: the three critical full fibers; the full ring for the multifiber minimum; a critical full fiber minus one point for the second minimum. |
| Does \(Q>1\) help after costs? | No in the audited split-prime certificate: \(\rho_4Q(4/7)^{1/3}\ge2(4/7)^{1/3}>1\). |
| Best evaluated \(Q=1\) carrier? | The explicit ideal-coset carrier below has rate \(\kappa=\log\!\big[X^2/(D(4/7)^{1/3}(W+7))\big]\le-\log(39.5192D)<0\). |
| Which term prevents a positive rate? | The quartic continuous output width divided by the two-input volume, together with the discriminant cost, exceeds the local gain. |
| Is the fixed-quartic target proved? | No. The no-go conclusions concern specified counting certificates, not the actual polynomial image. |

The exact finite screen covers 2,958,216 structured parameter instances
and agrees with the analytic theorem. It is not a premise of that theorem.
The C2 correction list was unavailable during the original C3 run. It was
supplied in the review of 8 September 2026 and is now applied in the
companion C2 precision addendum and corrected C2 files. The C3 proof is
unchanged. No external research or novelty check was performed.

The external review accepted the analytic theorem and signed certificate
audit from the PDF. The finite screen, JSON results, source manifest,
rate table, addendum, and independent referee report are supplied together
for separate review; that external review is not represented as having
checked those companions. This report is frozen at modulus 7. Higher
precision and smaller realized-support covers are outside its no-go.

# 1. Scope, notation, and preserved state

The fixed target is
\[
P_4(x,y)=(x+2y)^4+3x-y.
\]
The corrected C0 quadratic family theorem and the scoped C1 obstructions
retain their established status. C2's length-three ramified ring and
determinant-seven output restriction remain valid. Its elementary hybrid
parameter count is a certificate with zero saving, not a quadratic lower
bound on the actual image.

All logarithms are natural. In local arguments write \(n=|E|\) and
\(v=|h_s(3E-E)|\); in global arguments \(d=[F_j:\mathbb Q]\) and
\(D=\operatorname{rd}(F_j)\). These are different uses of dimension and
cardinality, never identified.

Two typographical defects in the C3 instruction are corrected in the
formulas below: the missing plus before the \(\pi^2\) term and malformed
occurrences of \(\Phi_s(E)\). These are not purported corrections from
the later-supplied C2 review. The exact inspected-source register is
SOURCE_MANIFEST_C3.md.

# 2. Carrier-independent local algebra

For an integer \(Q\) coprime to 7, put
\[
F_Q(x,y)=(x+2y)^4+Q^3(3x-y),\qquad s=Q^3\bmod7\in\{1,-1\}.
\]
In the characteristic-seven ring \(R\), let \(L=x+2y\), \(M=3x-y\).
Then \(L+2M=7x=0\), so \(L=-2M\) and
\[
F_Q(x,y)=16M^4+sM=2M^4+sM=h_s(M).
\]
Every element of \(3E-E\) is realized by a pair in \(E^2\). Therefore
\[
\boxed{F_Q(E,E)=h_s(3E-E)}
\tag{2.1}
\]
for every nonempty \(E\subseteq R\). No unit set or hybrid presentation
is involved. Globally this identity is a reduction modulo \(7\mathcal O\);
it is not an identity over a characteristic-zero field.

## 2.1 Digit expansion and branches

Write \(z=a+b\pi+c\pi^2\). Since \(\pi^3=0\), direct expansion gives
\[
\boxed{
h_s(z)=h_s(a)+(a^3+s)b\pi+
\big((a^3+s)c+5a^2b^2\big)\pi^2.}
\tag{2.2}
\]
Let \(K_s=\{a:a^3=-s\}\) be the three critical residues, and let
\(J_s=\mathbb F_7\setminus K_s\) be the four regular residues. Explicitly,
\[
K_1=\{3,5,6\},\quad J_1=\{0,1,2,4\},\qquad
K_{-1}=\{1,2,4\},\quad J_{-1}=\{0,3,5,6\}.
\]

The residue map \(a\mapsto h_s(a)\) is a permutation. For \(a\ne0\),
\[
h_s(a)=
\begin{cases}
-sa,&a^3=-s,\\
3sa,&a^3=s.
\end{cases}
\]
The cubes of these outputs are respectively \(1\) and \(-1\), because
\(3^3=-1\) in \(\mathbb F_7\). Each branch is a nonzero scalar
bijection onto its three-element cube class, and zero maps to zero.

On a regular residue fiber, (2.2) is triangular in \((b,c)\) with
nonzero diagonal coefficient, hence bijective onto the corresponding
output residue fiber. On a critical residue fiber it becomes
\[
h_s(a+b\pi+c\pi^2)=h_s(a)+5a^2b^2\pi^2.
\tag{2.3}
\]
Thus the last digit is forgotten, while the first nilpotent digit is
identified only through its square. Outputs from distinct argument
residues are disjoint. In particular,
\[
|h_s(R)|=4\cdot49+3\cdot4=208.
\]
Here an argument residue means a residue of \(3E-E\), not automatically
one of \(E\). When \(E\) lies in a single residue \(a\), its argument
residue is \(2a\); the equivalence of their critical conditions uses
\(2^3=1\).

## 2.2 Sign symmetry

The exact identities
\[
h_{-1}(-z)=h_1(z),\qquad 3(-E)-(-E)=-(3E-E)
\]
imply
\[
\boxed{\Phi_{-1}(-E)=\Phi_1(E).}
\]
Negation is digitwise in \(R\). It transfers critical fibers and all
equality statements between signs. This proves the symmetry before it
is used to halve the computational screen.

# 3. Input-cost normalization and complete fibers

One local factor has 343 elements. The one-input fraction is
\(n/343\); the fraction of the Cartesian square is \((n/343)^2\);
the local output fraction is \(v/343\). Their ratio is
\[
\boxed{\Phi_s(E)=\frac{v/343}{(n/343)^2}=\frac{343v}{n^2}.}
\tag{3.1}
\]
On the full product \(E^{d/3}\), the exact fractions multiply. The
normalized local multiplier is \(\Phi_s(E)^{d/3}\), with per-degree
gain \(-\frac13\log\Phi_s(E)\). A positive local gain is equivalent to
\(\Phi_s(E)<1\). This is a statement about finite quotient proportions,
not equidistribution of algebraic integers in a bounded window. A global
input lower count must still be proved separately.

For a critical full input fiber \(E=a+\pi R\),
\[
3E-E=2a+\pi R,\qquad (2a)^3=a^3=-s.
\]
It follows from (2.3) that
\[
|E|=49,\qquad v=4,\qquad
\boxed{\Phi_s(E)=4/7,\quad \gamma_*=\tfrac13\log(7/4).}
\tag{3.2}
\]
Both input restrictions have been paid.

## 3.1 Complete-residue-fiber theorem

For nonempty \(A\subseteq\mathbb F_7\), set \(E_A=A+\pi R\),
\(B=3A-A\), \(k=|A|\), and
\(r=|B\cap J_s|,\ c=|B\cap K_s|\). Each represented argument
residue has all its nilpotent digits, so
\[
\boxed{|F_Q(E_A,E_A)|=49r+4c,\qquad
\Phi_s(E_A)=\frac{49r+4c}{7k^2}\ge\frac47.}
\tag{3.3}
\]
Equality holds exactly when \(A\) is a singleton critical residue.

Here and below we use Cauchy-Davenport in its precise form
\[
|U+V|\ge\min(7,|U|+|V|-1)
\quad(\varnothing\ne U,V\subseteq\mathbb F_7).
\]
Scalar multiplication by 3 and by \(-1\) preserves cardinality.

For \(k=1\), (3.2) handles a critical input; a regular input gives
49 outputs. For \(k=2\), writing \(A=\{a,a+t\}\), \(t\ne0\),
the four residues \(2a-t,2a,2a+2t,2a+3t\) are distinct.
At least one is regular because only three residues are critical.
Hence \(49r+4c\ge49>16=4k^2\).
For \(k=3\), Cauchy-Davenport gives \(|B|\ge5\), so \(r\ge2\)
and \(49r+4c\ge98>36\). For \(4\le k\le7\), it gives
\(B=\mathbb F_7\), so \(49r+4c=208>4k^2\).
This proves (3.3) by a short case argument, without subset enumeration.

# 4. The universal local theorem

**Theorem 4.1.** For either sign and every nonempty \(E\subseteq R\),
\[
\boxed{\Phi_s(E)\ge4/7.}
\]
Equality holds exactly for the three critical full residue fibers.

The proof below is independent of the computational results.

## 4.1 Sets in one residue fiber

Suppose \(E\subseteq a+\pi R\) and \(n=|E|\le49\).
If \(a\) is regular, so is \(2a\). Fixing one input shows
\(|3E-E|\ge n\), and local bijectivity gives
\[
\Phi_s(E)\ge343/n\ge7.
\]

If \(a\) is critical, let \(T\subseteq\mathbb F_7\) be the first
nilpotent-digit support of \(E\), and let \(t=|T|\). Then \(n\le7t\).
The first nilpotent digits of \(3E-E\) run exactly over \(3T-T\):
the second digits may be correlated with the first, but (2.3) ignores
them. Consequently
\[
v=|\{b^2:b\in3T-T\}|.
\tag{4.1}
\]
Cauchy-Davenport and the at-most-two fibers of squaring give
\[
v\ge\min(t,4),\qquad
\Phi_s(E)\ge\frac{7\min(t,4)}{t^2}.
\tag{4.2}
\]
For \(t\le3\), use \(|3T-T|\ge2t-1\), so \(v\ge t\).
For \(t\ge4\), \(3T-T=\mathbb F_7\), so \(v=4\).
If \(t\le6\), the last bound in (4.2) is at least \(7/9>4/7\).
If \(t=7\), then \(\Phi_s(E)=1372/n^2\ge4/7\), with equality
if and only if \(n=49\). This proves the theorem in one residue fiber.

## 4.2 A regular branch must touch every input fiber

Let \(A\) be the residue support of \(E\), with \(|A|\ge2\).
Fix \(a\in A\). Some regular residue of \(3A-A\) has a representation
using \(a\). If \(a\) is regular, use the diagonal \(2a\).
If \(a\) is critical, choose \(b\ne a\) in \(A\), and put \(t=b/a\).
If both \(3a-b\) and \(3b-a\) were critical, then
\[
(3-t)^3=(3t-1)^3=1.
\]
Subtracting the two equations in \(\mathbb F_7[t]\) gives
\[
\big((3t-1)^3-1\big)-\big((3-t)^3-1\big)=t-t^2=0.
\]
Thus \(t=0\) or 1. The first does not satisfy \((3-t)^3=1\);
the second contradicts \(a\ne b\). This proves the assertion.

## 4.3 Regular outputs contribute at least one third of the input

For \(a\in A\), write \(E_a=E\cap(a+\pi R)\),
\(n_a=|E_a|\), \(k=|A|\), \(M=\max n_a\), and \(m=\min n_a\).
Let \(D_u\) be the residue-\(u\) part of \(3E-E\). If \(u=3a-b\),
then fixing either input gives
\[
|D_u|\ge|3E_a-E_b|\ge\max(n_a,n_b).
\tag{4.3}
\]
Regular branches are injective and have disjoint output residues.
Their total contribution is therefore at least \(n/3\):

- For \(k=2,3\), Section 4.2 gives one regular branch touching a
  maximal fiber, so its contribution is at least \(M\ge n/3\).
- For \(k=4\), Cauchy-Davenport gives \(3A-A=\mathbb F_7\).
  All four regular branches occur; one contributes at least \(M\)
  and the other three at least \(m\). Since \(n\le3M+m\),
  \(M+3m\ge n/3\).
- For \(k=5,6,7\), fix a maximal fiber at \(a\). The \(k\) distinct
  residues \(3a-b\), \(b\in A\), include at least \(k-3\) regular
  ones, each contributing \(M\). Thus their sum is at least
  \((k-3)M\ge kM/3\ge n/3\).

In particular,
\[
\boxed{|h_s(3E-E)|\ge n/3\quad\text{if \(E\) meets several residues}.}
\tag{4.4}
\]

## 4.4 The cardinality split

For a multifiber set of size \(n\le171\), (4.4) gives
\[
\Phi_s(E)\ge\frac{343}{3n}\ge\frac{343}{513}>
\frac{208}{343}>\frac47.
\]
The first strict comparison follows from \(117649>106704\).
For \(n\ge172\), every \(z\in R\) belongs to \(3E-E\): the sets
\(3E\) and \(z+E\) both have size \(n\) and hence intersect in the
343-element additive group. Therefore \(3E-E=R\), and
\[
\Phi_s(E)=\frac{343\cdot208}{n^2}\ge\frac{208}{343}>\frac47.
\]
Together with Section 4.1 this proves Theorem 4.1 and exhausts every
equality case. It also proves the sharp multifiber minimum
\(208/343\), with equality only at \(n=343\), namely \(E=R\).

# 5. Sharp second minimum and stability

**Theorem 5.1.** Outside the three full critical fibers,
\[
\boxed{\Phi_s(E)\ge\frac{343}{576}.}
\tag{5.1}
\]
Equality holds exactly at
\[
E=(a+\pi R)\setminus\{z_0\},\qquad a^3=-s.
\]

Indeed, multifiber sets have cost at least \(208/343>343/576\);
regular single-fiber sets have cost at least 7; critical single-fiber
sets with \(t\le6\) have cost at least \(7/9\).
In the remaining case \(t=7\), the image has exactly four elements.
If the fiber is not full then \(n\le48\), so
\(\Phi_s(E)=1372/n^2\ge1372/48^2=343/576\).
Every 48-element subset of a 49-element fiber has all seven first
digits, proving both attainment and the complete equality description.

The exact gap above the minimum is
\[
\frac{343}{576}-\frac47=\frac{97}{4032}.
\]
Thus cost below the second minimum forces an exact extremizer.
More broadly, \(\Phi_s(E)<208/343\) forces concentration in one
critical fiber with 48 or 49 points: all other cases above are excluded,
and \(1372/47^2>208/343\). This is a proved discrete stability statement,
not a limiting assertion about growing finite fields.

# 6. Reproducible structured discovery screen

The standard-library-only program local_7adic_screen.py uses exact integer
arithmetic, no randomness, and no network. Run from the project root:

    python3 phase_c3/local_7adic_screen.py --output phase_c3/local_7adic_results.json

An element is encoded by \(a+7b+49c\); this is a digit encoding, not
arithmetic in \(\mathbb Z/343\mathbb Z\). For digit rectangles the
program uses the proved formula
\[
|h_s(3E-E)|
=r_A|3B-B||3C-C|+c_A|\{b^2:b\in3B-B\}|,
\]
where \(E=A\times B\times C\) in digit coordinates and \(r_A,c_A\)
count argument residues in \(3A-A\). Other reductions are explained
in the accompanying finite-search note. Direct checks use every ordered
input pair, not collision energy.

| Searched family | Parameter instances | Minimum found |
|---|---:|---:|
| Affine subspaces/cosets, dimension 0 | 343 | \(343\) |
| Affine subspaces/cosets, dimension 1 | 2,793 | \(7\) |
| Affine subspaces/cosets, dimension 2 | 399 | \(4/7\) |
| Full ring, dimension 3 | 1 | \(208/343\) |
| All nonempty digit rectangles | 2,048,383 | \(4/7\) |
| One-fiber subsets, size 1 | 343 | \(343\) |
| One-fiber subsets, size 2 | 8,232 | \(343/4\) |
| One-fiber subsets, size 3 | 128,968 | \(343/9\) |
| Two partial fibers, full last digit | 338,709 | \(61/28\) |
| Two partial fibers, full middle digit | 338,709 | \(61/28\) |
| Critical full fiber minus one point | 147 | \(343/576\) |
| Critical full fiber minus two points | 3,528 | \(1372/2209\) |
| Critical full fiber plus one point | 882 | \(9947/1250\) |
| One-point inside/outside exchange | 43,218 | \(57/7\) |
| Saturated quadratic digit graphs | 43,561 | \(31/7\) |

These are 2,958,216 parameter instances, not necessarily distinct sets.
There were no counterexamples or extra equality cases. The JSON records
the exact minimum, representative input/output sizes, examples, all
minimizing parameter ordinals in lossless form, equality descriptors,
and hashes. It is a compact record for every searched family.

The script independently evaluates the original polynomial using ring
multiplication for all \(343^2=117649\) ordered pairs for each sign;
it checks the sign symmetry and all full fibers, and compares the
rectangle formula with direct pair evaluation for 1,331 mask triples.
The small state spaces justify those finite checks only. The universal
and stability theorems were proved in Sections 4-5 without using them.

# 7. The field construction with \(Q=1\)

The supplied proof's Propositions 3.2-3.5 and the first step of
Proposition 3.8 give a totally real cyclic cubic base \(F\), constructed
from the first \(\ell\) primes \(r_i\equiv1\pmod3\). Since \(r_1=7\),
\[
|\operatorname{disc}(F)|=\left(\prod_i r_i\right)^2,\qquad
D=\operatorname{rd}(F)=\left(\prod_i r_i\right)^{2/3}\ge7^{2/3}.
\]
There is one prime \(\mathfrak p\) over 7 with
\(7\mathcal O_F=\mathfrak p^3\) and residue field \(\mathbb F_7\).

Let \(\mathfrak G\) be the maximal everywhere-unramified pro-3 group
over \(F\), and put \(d_0=d(\mathfrak G)\), \(r_0=r(\mathfrak G)\).
The source gives \(d_0\ge\ell-1\) and \(r_0\le d_0+C_0\).
Kill only a Frobenius representative at \(\mathfrak p\), forming
\(\mathfrak G_7\). If it is in the Frattini subgroup, generator rank
is preserved and relation rank increases by at most one. Otherwise,
include it in a minimal generating basis and eliminate that generator
after quotienting. In both cases the safe bounds are
\[
d(\mathfrak G_7)\ge d_0-1,\qquad
r(\mathfrak G_7)\le d_0+C_0+1.
\]
For \(L=\ell-1\ge3\), it suffices to fix \(\ell\) so large that
\[
\frac{(L-1)^2}{4}-L-C_0-1
=\frac{L^2}{4}-\frac{3L}{2}-C_0-\frac34>0.
\tag{7.1}
\]
The same difference is increasing for \(d_0\ge L\).
Golod-Shafarevich then makes \(\mathfrak G_7\) infinite.

Its finite Galois layers \(F_j\) are unramified 3-extensions of \(F\),
have \(d_j\to\infty\), remain totally real, and satisfy
\(\Delta_j=D^{d_j}\). The killed Frobenius makes \(\mathfrak p\)
split completely in every relative layer. Hence
\[
7\mathcal O_{F_j}=\prod_{k=1}^{d_j/3}\mathfrak P_{j,k}^3,\qquad
\mathcal O_{F_j}/\mathfrak P_{j,k}\cong\mathbb F_7.
\]
The local length-three quotients have characteristic 7, residue
\(\mathbb F_7\), and a principal maximal ideal; a uniformizer gives
the unique three-digit expression and identifies each with \(R\).

No split rational primes \(q_b\) are selected. There is no Chebotarev
step, no \(3t\) added relation cost, no \(\rho_4\) or nontrivial \(Q\),
no adjoining \(i\), and no CM class-number loss. Unit and regulator
estimates are unnecessary for the simplified additive carrier.

# 8. An explicit global critical-fiber carrier

Set
\[
\mathfrak I_j=\prod_{k=1}^{d_j/3}\mathfrak P_{j,k},\qquad
N(\mathfrak I_j)=7^{d_j/3}.
\]
Under the Minkowski embedding, this ideal is a lattice of covolume
\[
7^{d_j/3}\sqrt{\Delta_j}=7^{d_j/3}D^{d_j/2}.
\]
For a fixed real radius \(X>0\), define
\[
\boxed{C_j=-1+\{\alpha\in\mathfrak I_j:
|\sigma_i(\alpha)|\le X\text{ for all }i\}.}
\tag{8.1}
\]
At every ramified factor its reduction lies in the optimal local input
fiber \(-1+\pi R\), since \((-1)^3=-1\). We do not assert that
the bounded carrier surjects onto that fiber.

## 8.1 Rigorous lower count

For a lattice of covolume \(V\), averaging translates of
\([-X/2,X/2]^d\) gives a translate containing at least \(X^d/V\)
lattice points. Fix one such point and subtract it from the others.
The differences lie in the lattice and in \([-X,X]^d\), with
cardinality preserved. Applying this to \(\mathfrak I_j\) proves
\[
\boxed{|C_j|\ge
\left(\frac{X}{7^{1/3}\sqrt D}\right)^{d_j}.}
\tag{8.2}
\]
This is the frozen Phase A half-box/difference argument applied to an
ideal sublattice. The ideal index pays exactly the critical input
restriction. No uniform residue-distribution assertion is used.

Norm separation of algebraic integers also gives
\[
|C_j|\le(2X+1)^{d_j}.
\]
Thus
\[
a=\log X-\tfrac13\log7-\tfrac12\log D,\qquad
B=\log(2X+1).
\tag{8.3}
\]
Choose \(X>7^{1/3}\sqrt D\), for example
\(X=2\,7^{1/3}\sqrt D\), fixed after the tower. Then \(a>0\)
(equal to \(\log2\) for the displayed choice), so this is a genuine
growing carrier. The translation is injective and there is no
parameter multiplicity, unit, regulator, or sign-selection cost.

## 8.2 Exact continuous output width for \(Q=1\)

All inputs lie in \(I=[-1-X,-1+X]\) in every real embedding. The
growth condition and \(D\ge7^{2/3}\) imply \(X>7^{2/3}>7/2\).
For this range, the exact extrema on \(I^2\) are
\[
U=81(X+1)^4-2X-2,\qquad
m=-\frac72X-\frac{59}{16},
\]
so
\[
\boxed{W=U-m=81(X+1)^4+\frac32X+\frac{27}{16}.}
\tag{8.4}
\]

To verify the maximum, convexity of \(P_4\) reduces it to the four
vertices. Their values are
\[
81(X+1)^4-2X-2,\quad81(X-1)^4+2X-2,\quad
(X+3)^4+4X-2,\quad(X-3)^4-4X-2.
\]
The first exceeds the second by \(648X^3+644X\).
It exceeds the third by
\(80X^4+312X^3+432X^2+210X>0\).
It exceeds the fourth since \(3(X+1)>|X-3|\) and its linear term
is larger by \(2X\).

For the minimum write \(x=-1+u,y=-1+v\), and use
\(L'=u+2v\), \(M'=3u-v\), with \(u,v\in[-X,X]\).
For fixed \(L'\), the least \(M'\) is
\[
M'_{\min}(L')=
\begin{cases}
(-7X-L')/2,&-3X\le L'\le X,\\
3L'-7X,&X\le L'\le3X.
\end{cases}
\]
Put \(w=L'-3\). The first branch of \(P_4\) becomes
\(w^4-w/2-7X/2-7/2\), minimized at \(w=1/2\).
This point is feasible when \(X\ge7/2\). On the second branch,
\(w\ge X-3\ge1/2\), and the derivative of
\(w^4+3w+7-7X\) is positive. This proves the minimum.
Continuity and connectedness show the full continuous image is
\([m,U]\). No \(Q\ge5\) inequality has been imported here.

## 8.3 Full-support certificate and signed rate

The local theorem permits four output classes per ramified factor.
Every global output therefore lies in one of at most \(4^{d/3}\)
classes modulo \(7\mathcal O\). Two distinct points in one class
are 7-separated in sup norm, by the nonzero integer norm of their
difference divided by 7. Packing cubes of side length \(7\) gives
\[
|P_4(C_j,C_j)|\le U_{7,j}
=4^{d_j/3}(1+W/7)^{d_j}.
\tag{8.5}
\]
Every pair is covered; no exceptional or lightly represented output
is omitted. Set
\[
c=\tfrac13\log4+\log(1+W/7).
\]
Using (8.3), the certificate rate is exactly
\[
\boxed{\kappa_{\rm cert}=2a-c
=\log\frac{X^2}{D(4/7)^{1/3}(W+7)}.}
\tag{8.6}
\]
The word certificate is essential: \(c\) is a proved upper exponent,
not the unknown exponent of the actual image.

# 9. Uniform negative rate and the \(Q\) audit

## 9.1 Width inequalities valid at \(Q=1\)

For any real center \(c_0\) and radius \(r>0\), two elementary checks
inside \([c_0-r,c_0+r]^2\) prove
\[
W_1(c_0,r)\ge7r,\qquad
W_1(c_0,r)\ge\alpha r^4,\quad \alpha=81.
\tag{9.1}
\]
The first slice uses \((c_0+r,c_0-r/2)\) and
\((c_0-r,c_0+r/2)\), for which \(x+2y\) agrees and \(3x-y\)
differs by \(7r\). For the sharper quartic bound restrict to the
diagonal, where \(f(t)=P_4(t,t)=81t^4+2t\). Then
\[
\frac{f(c_0+r)+f(c_0-r)}2-f(c_0)
=486c_0^2r^2+81r^4\ge81r^4.
\]
The average of two endpoint values is at most the maximum, while
the center value is at least the minimum. Their difference is therefore
at most the full output width, proving the bound.
These proofs work directly at \(Q=1\). Only the first inequality
acquires \(Q^3\) for general \(F_Q\); the diagonal's linear term
cancels for every \(Q\).

By (9.1) and arithmetic-geometric mean,
\[
\frac{W_1(c_0,r)+7}{r^2}\ge
\alpha r^2+\frac7{r^2}\ge2\sqrt{7\alpha}.
\tag{9.2}
\]
Thus (8.6) satisfies, for every evaluated growth radius,
\[
\boxed{\kappa_{\rm cert}\le
-\log\left[18\sqrt7(4/7)^{1/3}D\right]
\approx-\log(39.51926350D)<0.}
\tag{9.3}
\]
The quartic-width term already gives the wrong sign even at \(D=1\).
For the explicit \(X=2\,7^{1/3}\sqrt D\), this already gives the
uniform numerical margin \(\kappa_{\rm cert}<-4.97\)
using \(D\ge7^{2/3}\). No numerical value of the source constant
\(C_0\), or of the chosen tower's \(D\), is being invented.

## 9.2 Arbitrary local sets: the volume-density certificate

This subsection deliberately gives the input estimate its more favorable
full-volume normalization. Let a local set \(E\) have size \(n\),
image size \(v\), and density \(\delta=n/343\).
In degree \(d\), its CRT pattern is a union of \(n^{d/3}\)
cosets of \(7\mathcal O\). Averaging a window of volume \(V_{\rm box}\)
over a fundamental domain of \(7\mathcal O\) gives an expected
population \(\delta^{d/3}V_{\rm box}/\sqrt\Delta\); at least one
translate attains that average. This proves existence of a dense
translate, not uniformity for a prescribed translate or control of
its center.

For an equal-radius window the corresponding input budget is
\(\delta^{d/3}(2r)^d/\sqrt\Delta\). Dividing the full-class
certificate \(v^{d/3}(1+W/7)^d\) by the square of this budget gives
the per-degree factor
\[
\Theta_{\rm vol}=D\,\Phi_s(E)^{1/3}\frac{W+7}{4r^2}.
\tag{9.4}
\]
The same formula multiplies coordinatewise for anisotropic windows.
Equations (9.2) and Theorem 4.1 imply
\[
\boxed{\Theta_{\rm vol}\ge
D(4/7)^{1/3}\frac{9\sqrt7}{2}
\approx9.879815874D>1.}
\tag{9.5}
\]
Even this more favorable input-count certificate fails for every local
set \(E\), every translate, and every positive choice of radii.
The fixed-center ideal carrier in Section 8 pays an additional factor
4 in the normalized certificate because its guaranteed lower count
uses the half-box/difference argument.

This is a no-go for the volume-density plus full-continuous-interval
plus uniform-modulus-packing calculation. It does not rule out a
stronger actual input count or a smaller realized output cover.

## 9.3 Actual population check for the optimal critical cosets

For the optimal critical full-fiber pattern, a stronger scoped statement
does not depend on the input lower count. Suppose \(C\) is any subset
of a fixed coset of \(\mathfrak I_j\) in an equal-radius Minkowski
window of radius \(r\), with arbitrary coordinate centers.
Put \(t=7^{1/3}\). A nonzero ideal difference has norm at least
\(N(\mathfrak I_j)=7^{d/3}=t^d\), hence sup norm at least \(t\).
If \(2r<t\), the carrier has at most one point. Otherwise
\[
|C|\le(1+2r/t)^d.
\]
Let \(z=2r/t\ge1\) and \(K=\alpha t/16>1\). For the full
four-class-per-factor interval certificate, (9.1) yields
\[
\frac{U_7}{|C|^2}\ge
\left[
4^{1/3}\frac{1+Kz^4}{(1+z)^2}
\right]^d
\ge\left[\frac{4^{1/3}(1+K)}4\right]^d
>4.24^d.
\tag{9.6}
\]
The middle inequality follows because the derivative numerator is
\(2Kz^4+4Kz^3-2>0\) on \(z\ge1\).
Thus a stronger input population cannot rescue this particular
full-envelope certificate for optimal critical cosets in equal-radius
windows. Replacing its class envelope or output region is outside
this statement.

## 9.4 The \(Q>1\) branch

If the source-selected primes are retained, \(Q=\prod q_b>1\) and
\(\rho_4=\prod_{q_b}(q_b+3)/(4q_b)\). The C2 tower construction
then includes the \(3t\) Frobenius relations in addition to the one
at 7, with its already verified generator-relation margin.
At the split primes the output is a fourth power. For local \(E\)
at 7 the combined full-volume factor is
\[
\Theta_{Q,\rm vol}
=D\,\Phi_s(E)^{1/3}\rho_4
\frac{W_Q(c_0,r)+7Q}{4r^2}.
\tag{9.7}
\]
Indeed, the class count is \(v^{d/3}(\rho_4Q)^d\), the per-class
packing is \((1+W_Q/(7Q))^d\), and both input fractions are
\(\delta^{d/3}\). This derives the normalization without a density
shortcut.

Now \(Q\ge5\), so C1's proved inequality applies:
\[
W_Q(c_0,r)+Q\ge Q(2r+1)^2.
\]
Consequently \(\Theta_{Q,\rm vol}\) is strictly larger than
\(D\rho_4Q\,\Phi_s(E)^{1/3}\). Since
\[
\rho_4Q=\prod_{q_b}\frac{q_b+3}{4}\ge2,
\]
Theorem 4.1 gives the normalized obstruction
\[
\boxed{\rho_4Q\,\Phi_*^{1/3}
\ge2(4/7)^{1/3}\approx1.659653>1,\qquad\Phi_*=\frac47.}
\tag{9.8}
\]
Thus no positive fully charged contribution from \(Q>1\) survives
in this certificate. This does not deny that the split-prime
restrictions are valid; it says their combined cost here has the
wrong sign.

For an explicit carrier in the \(Q>1\) tower, replace the shift
\(-1\) in (8.1) by \(-s\). Its local fiber is critical because
\((-s)^3=-s\), and its lower rate \(a\) is unchanged. With
\(W_Q=W_Q(-s,X)\), the full-support upper rate is
\[
c_Q=\tfrac13\log4+\log(\rho_4Q)+
\log(1+W_Q/(7Q)),
\]
and
\[
\kappa_{Q,\rm cert}=
\log\frac{X^2}{D(4/7)^{1/3}\rho_4(W_Q+7Q)}
<-\log\!\left[4D(4/7)^{1/3}\rho_4Q\right]<0.
\tag{9.9}
\]
The inequality uses \(W_Q+7Q>4QX^2\), a direct consequence
of the \(Q\ge5\) width comparison. One may also discard the
optional split-prime modulus and use only 7. The fresh bound
\(W_Q(c_0,r)\ge81r^4\) still applies, so (9.3) and (9.5)
remain negative for that optional certificate as well.

# 10. Complete ledger, gate, and next permitted action

| Contribution | Explicit \(Q=1\) carrier | Effect on \(2a-c\) |
|---|---|---|
| Radius and two inputs | \(X^{2d}\) | \(+2\log X\) |
| Ideal congruence restriction | \(7^{-2d/3}\) | \(-\tfrac23\log7\) |
| Discriminant | \(\Delta^{-1}=D^{-d}\) | \(-\log D\) |
| Four local output classes | \(4^{d/3}\) | \(-\tfrac13\log4\) |
| Uniform class packing | \((1+W/7)^d\) | \(-\log(1+W/7)\) |
| Units and regulator | No unit carrier | \(0\) |
| Sign selection and distortion | No sign restriction; shift \(-1\) included in \(W\) | No hidden cost |
| Multiplicity and ratio sum | Direct additive parameterization; no ratio union | \(0\) |
| Exceptional outputs | None omitted | \(0\) |
| Real embedding and scaling | Injective; \(Q=1\) | \(0\) |

The first five entries sum exactly to (8.6); reorganizing them displays
the maximum local gain \(+\gamma_*\) against
\(2\log X-\log D-\log(W+7)\).
For \(Q>1\), (9.7)-(9.8) additionally charge split-prime classes,
modulus spacing, and the \(Q^3\) term in the actual width.
The companion rate table gives the same ledgers separately.

The fixed-parameter order is: choose the source base and \(\ell\)
satisfying (7.1); kill its Frobenius at 7 and fix the tower and \(D\);
choose the local critical fiber and the fixed radius
\(X=2\,7^{1/3}\sqrt D\); only then let \(j\to\infty\).
The ideal changes with the layer by its stated algebraic definition,
not by changing the local pattern or a scale parameter.

The signed gate is negative for the explicit growing construction,
for every local set under the broader volume-density certificate,
and for the full-envelope certificate on actual optimal critical
cosets in equal-radius windows. No further unrestricted global
carrier search was opened.

If desired later, the injective real embedding
\(A_j=\sigma_j(C_j)\) gives arbitrarily large real same-input sets.
But the present estimates do not give a positive compression exponent,
so they do not complete the target. For general fixed \(Q\),
\(F_Q(Qx,Qy)=Q^4P_4(x,y)\) remains the correct transport identity.

The next permitted mathematical action is to formulate and prove a
strictly smaller realized-support cover, with a separately charged
quantitative gain, or to obtain a new instruction authorizing a
different arithmetic mechanism. Merely tightening the local subset
\(E\) cannot improve \(\Phi_*=4/7\). The abstract hybrid overlap
screen is not promoted to a proved lemma. The subsequently supplied C2
wording corrections are recorded separately and do not change this proof.

The independent referee checked the local proof, exact equality cases,
finite-screen implementation, lattice normalization, width calculations,
and these scope restrictions. The fixed-quartic target remains a
project conjecture whose external status has not been checked.

**SCOPED NO-GO FOR MODULUS-\(7\) INPUT ENGINEERING WITH FULL-INTERVAL CLASS PACKING.**
