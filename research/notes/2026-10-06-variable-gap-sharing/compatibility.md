# Variable-output shared-edge compatibility

**T01 · 6 October 2026 · version 1 · commissioned offline research.**

The fixed polynomial is
\[
P(x,y)=(x-y)^3+x+y.
\]
The motif here consists of the two directed triangles
\[
(a,b,c,a),\qquad(a,b,d,a),
\]
sharing the ordered edge \((a,b)\). Its five ordered edges have labels
\[
z_0=P(a,b),\quad z_1=P(b,c),\quad z_2=P(c,a),\quad
z_3=P(b,d),\quad z_4=P(d,a).                               \tag{1}
\]
These outputs are allowed to vary; no fixed-gap condition is imposed.
Coincident vertices or labels are allowed in the exact equivalences and
are explicitly separated from a nondegenerate four-vertex application.

The accepted predecessors are the
[elliptic checkpoint](../2026-09-30-elliptic-geometry/README.md) and
[directed-triangle compatibility proof](../2026-10-06-sharing-compatibility/geometry.md).
The coordinate templates and real triangle uniqueness are inherited.
The shared-edge system, the all-cycle extension including even cycles,
and the integer-label gluing rules below are newly checked. This appendix
does not revisit the old fixed-gap classification, SH-O1, or a global
elliptic group-law identity.

**Evidence and budget:** complete displayed algebraic proofs; zero
research programs, numerical searches, carrier evaluations or
symbolic-computation programs. There is no network use, installation,
arithmetic amplification or novelty claim. On 6 October 2026 the lead
independently checked the complete displayed proofs and accepted VG-G1–VG-G3
without a mathematical correction. The cycle's verification record reports
that internal audit separately from finite computation. No next obligation
is assigned by this appendix.

## 1. VG-G1 — exact simultaneous shared-edge equations

### Meaning

Two individually valid triangles need not share the same scalar edge.
Using one common difference and one common anchor enforces both shared
vertices before any parameter choices are counted.

### Exact statement — PROVED

For prescribed real \(z_0,\ldots,z_4\), put
\[
u=a-b,\qquad v=b-c,\qquad t=b-d.
\]
Define
\[
F(u,s)=s^3-u^3-u-s,
\qquad G(u,s)=-(u+s)^3-u^3-s.                              \tag{2}
\]
The five output equations (1) hold if and only if
\[
\boxed{
z_1-z_0=F(u,v),\quad z_2-z_0=G(u,v),\quad
z_3-z_0=F(u,t),\quad z_4-z_0=G(u,t)}                       \tag{3}
\]
with the reconstruction
\[
\boxed{
b=\frac{z_0-u^3-u}{2},\quad a=b+u,\quad c=b-v,\quad d=b-t,}
                                                                    \tag{4}
\]
and the two closing differences
\[
w=c-a=-u-v,\qquad q=d-a=-u-t.                              \tag{5}
\]
There is no division by an edge difference or output gap.

The four scalar vertices are pairwise distinct exactly when
\[
u\ne0,\quad v\ne0,\quad t\ne0,\quad
u+v\ne0,\quad u+t\ne0,\quad v\ne t.                      \tag{6}
\]
Distinctness of the five output labels is a separate optional condition,
not a consequence of (6).

### Proof: simultaneous scalar sharing

Use the inherited templates
\[
c_s(z,e)=\frac{z-e^3+s e}{2},\qquad s\in\{1,-1\}.
\]
All scalar identifications required by the motif are
\[
\begin{aligned}
a&=c_+(z_0,u)=c_-(z_2,w)=c_-(z_4,q),\\
b&=c_-(z_0,u)=c_+(z_1,v)=c_+(z_3,t),\\
c&=c_-(z_1,v)=c_+(z_2,w),\\
d&=c_-(z_3,t)=c_+(z_4,q).
\end{aligned}                                             \tag{7}
\]
The output of the common edge first gives (4)'s formula for \(b\).
The definitions of \(u,v,t\) then give all other vertices and (5).
Direct substitution yields
\[
\begin{aligned}
P(b,c)-z_0&=v^3-u^3-u-v,\\
P(c,a)-z_0&=-(u+v)^3-u^3-v,\\
P(b,d)-z_0&=t^3-u^3-u-t,\\
P(d,a)-z_0&=-(u+t)^3-u^3-t.
\end{aligned}                                             \tag{8}
\]
Thus (1) implies (3). Conversely, (4) guarantees the first output;
equations (3) and (8) guarantee the other four and therefore all of (7).
This proves necessity and sufficiency, including degenerate cases.
The six differences between the four reconstructed vertices are exactly
the quantities tested in (6), up to sign, proving that assertion.
\(\square\)

### Two useful consequences within the same motif

Subtracting the two partner equations gives
\[
z_3-z_1=(t-v)(t^2+tv+v^2-1),                               \tag{9}
\]
\[
z_4-z_2=-(t-v)
\bigl((u+t)^2+(u+t)(u+v)+(u+v)^2+1\bigr).                 \tag{10}
\]
The bracket in (10) is strictly positive over \(\mathbb R\).
Consequently distinct partners \(c\ne d\) always have distinct closing
outputs \(z_2\ne z_4\), even though \(z_1\) and \(z_3\) can coincide.
Equivalently, with \((a,b)\) fixed, the partner map
\[
v\longmapsto z_2=z_0+G(u,v)
\]
has derivative \(-3(u+v)^2-1<0\). A fixed closing output allows only
one real partner. Growing partner sets in this motif therefore require
growing closing-output sets, which must be counted rather than treated
as fixed labels. Equations (9)–(10) alone are only consequences, not
replacements for the complete system (3).

### Why it matters

The same \(u\), \(z_0\) and \(b\) occur in both triangles. Independently
sampling two sharing curves and then counting their formal incidences
would miss precisely this shared-edge requirement.

### Scope

The statement supplies exact compatibility tests, not the existence of a
small common scalar carrier for many choices of \(u,v,t,z_0\). It gives
no full-image estimate. The real monotonicity consequence is scoped to
one fixed shared edge and does not bound a network with changing edges.

## 2. VG-G2 — uniqueness for every directed real cycle

### Meaning

The accepted triangle uniqueness extends to cycles of every length, but
the odd-cycle determinant proof cannot simply be copied to an even cycle.
At the potentially singular even-cycle comparison matrix, the putative
alternating displacement is incompatible with actual scalar differences.

### Exact statement — PROVED

For every integer \(n\ge2\), the map
\[
\mathcal C_n:\mathbb R^n\longrightarrow\mathbb R^n,
\quad (a_1,\ldots,a_n)\longmapsto
\bigl(P(a_1,a_2),\ldots,P(a_n,a_1)\bigr)                  \tag{11}
\]
is injective. No distinctness assumption is imposed on vertices or output
labels. For a single loop the corresponding statement is immediate from
\(P(a,a)=2a\).

Consequently a prescribed ordered five-label list (1) has at most one
real scalar quadruple \((a,b,c,d)\) satisfying the shared-edge motif.
Existence for arbitrary label lists is not asserted.

### Proof, including the even and fully degenerate cases

Suppose two scalar cycles \((a_i)\) and \((a_i')\) have the same ordered
outputs. With cyclic indices, set
\[
\alpha_i=a_i-a_i',\quad u_i=a_i-a_{i+1},\quad
u_i'=a_i'-a_{i+1}',
\]
\[
k_i=u_i^2+u_i u_i'+(u_i')^2
=\left(u_i+\frac{u_i'}2\right)^2+\frac34(u_i')^2\ge0.
\]
Factoring the difference of the two cubic outputs gives
\[
(1+k_i)\alpha_i+(1-k_i)\alpha_{i+1}=0.                    \tag{12}
\]
Thus \(|\alpha_i|\le|\alpha_{i+1}|\) around the entire cycle, and
all absolute values equal some \(M\ge0\). If \(M=0\), the cycles
agree. If \(M>0\), the strict inequality
\(|1-k_i|<1+k_i\) for \(k_i>0\) forces every \(k_i=0\).

This last case contains the even-cycle issue. Positive definiteness in
the displayed expression for \(k_i\) implies
\(u_i=u_i'=0\) for every edge. Hence
\[
\alpha_i-\alpha_{i+1}=u_i-u_i'=0.
\]
But (12) with \(k_i=0\) also gives
\(\alpha_i+\alpha_{i+1}=0\). Therefore \(2\alpha_i=0\), a
contradiction to \(M>0\), regardless of the parity of \(n\).
This proves (11). To deduce the motif assertion, apply the triangle case
to the ordered triples \((z_0,z_1,z_2)\) and \((z_0,z_3,z_4)\).
Any two realizations agree on \((a,b,c)\) and on \((a,b,d)\), hence
agree entirely. \(\square\)

For clarity, the cyclic comparison matrix has determinant
\[
\prod_i(1+k_i)+(-1)^{n-1}\prod_i(1-k_i).                   \tag{13}
\]
For even \(n\) and all \(k_i=0\), this is zero. The linear system
viewed in isolation then has an alternating kernel. The preceding proof
excludes that kernel using the additional identity
\(\alpha_i-\alpha_{i+1}=u_i-u_i'\), which is essential.
We do not assert that all these Jacobians are nonsingular.

### Why it matters

A fixed ordered cycle-label list cannot be multiplied into many distinct
real scalar cycles by choosing different real branches. Variable labels
and their sharing across motifs remain available and must be charged
explicitly; uniqueness of one label list does not count their number.

### Scope

This is a newly proved real-cycle statement. It is not a classification
of arbitrary directed graphs or complex solutions, and does not prove
that arbitrary output lists are realizable. It imposes no fixed-gap
restriction and does not use or reopen the prior fixed-gap family.

## 3. VG-G3 — integer output labels and exact gluing shifts

### Meaning

The proposed output-first window chooses actual outputs \(2j\) and
differences \(u\), then reconstructs their two scalar endpoints. Its
allowed output interval depends on the difference and is fixed before
forming the scalar union. Gluing edges is an exact shift of the integer
output index. Every shifted label must stay in its own allowed interval.

### Exact statement — PROVED

For integers \(u,j\), define
\[
p(u)=\frac{u^3-u}{2},\qquad q(u)=\frac{u^3+u}{2}=p(u)+u,
\]
\[
X(j,u)=j-p(u),\qquad Y(j,u)=j-q(u).                        \tag{14}
\]
Both \(p(u)\) and \(q(u)\) are integers, and
\[
X(j,u)-Y(j,u)=u,\qquad P(X(j,u),Y(j,u))=2j.                \tag{15}
\]
The map \((j,u)\mapsto(X(j,u),Y(j,u))\) is injective.

For the one chosen construction fix an integer \(k\ge3\), put
\(L=k^3\), and define
\[
D_k=\{-k,\ldots,-1,1,\ldots,k\},\qquad
I_u=\left[\frac{u^3+|u|}{2},\,
L-1+\frac{u^3-|u|}{2}\right]\cap\mathbb Z.
\]
For each allowed difference \(u\), the exact boundary identity is
\[
\boxed{j\in I_u
\quad\Longleftrightarrow\quad
X(j,u),Y(j,u)\in\{0,\ldots,L-1\}.}                       \tag{16}
\]
Define the prescribed pair set from these labels by
\[
E_k=\{(X(j,u),Y(j,u)):u\in D_k,j\in I_u\}.
\]
From one common-edge label with \(u\in D_k,j\in I_u\), choose integers
\(v,t\), and set
\[
\begin{aligned}
w&=-u-v,&
j_1&=j-q(u)+p(v),& j_2&=j-p(u)+q(w),\\
q_0&=-u-t,&
j_3&=j-q(u)+p(t),& j_4&=j-p(u)+q(q_0).
\end{aligned}                                             \tag{17}
\]
Here \(q_0\) denotes the second closing difference, to distinguish it
from the integer function \(q(\cdot)\).
These labels supply the exact shared-edge motif
\[
(j,u),\quad(j_1,v),\quad(j_2,w),\quad(j_3,t),\quad(j_4,q_0)
                                                                    \tag{18}
\]
inside \(E_k\) if and only if
\[
\boxed{
v,w,t,q_0\in D_k,\qquad
j_1\in I_v,\quad j_2\in I_w,\quad
j_3\in I_t,\quad j_4\in I_{q_0}.}                         \tag{19}
\]
Its output list is \((2j,2j_1,2j_2,2j_3,2j_4)\). The four vertices
are pairwise distinct precisely when (6) holds. If five distinct outputs
are required, impose pairwise distinctness of \(j,j_1,j_2,j_3,j_4\)
in addition; this is not implicit in (19).

### Proof

For every integer \(u\), \(u^3-u\) is even, and \(u^3+u\) has the
same parity. Thus (14) is integral. Its difference is \(q(u)-p(u)=u\),
and its sum is \(2j-u^3\), proving (15). The inverse of the pair map
on its image is \(u=X-Y,j=P(X,Y)/2\); hence it is injective.

Both endpoints lie between zero and \(L-1\) exactly when
\[
\max\{p(u),q(u)\}\le j\le L-1+\min\{p(u),q(u)\}.
\]
The maximum is \((u^3+|u|)/2\) and the minimum is
\((u^3-|u|)/2\), proving (16). The interval is nonempty because
\(|u|\le k<L\). These are conditions on the predefined labels; they
are not a later enlargement of the allowed output windows.

For the common edge let
\[
a=j-p(u),\qquad b=j-q(u),\qquad c=b-v,\qquad d=b-t.
\]
To start the next edge at \(b\), one must have
\[
X(j_1,v)=j_1-p(v)=j-q(u),
\]
which is exactly the first shift in (17). Its second endpoint is then
\(Y(j_1,v)=b-v=c\). The closing edge has difference \(w=c-a\),
and ending it at \(a\) forces
\[
Y(j_2,w)=j_2-q(w)=j-p(u),
\]
the second shift in (17). Its first endpoint is \(a+w=c\). Replacing
\(v\) by \(t\) proves the other two shifts. These arguments prove both
necessity and sufficiency. Since every edge label has a unique pair,
there is no alternative in-window label that can rescue a failed boundary
test in (19).

The shifts are exactly the integer form of VG-G1:
\[
2(j_1-j)=F(u,v),\qquad 2(j_2-j)=G(u,v),
\]
and analogously for \(t\). For example, \(q(-u-v)=-q(u+v)\), so
\[
2(j_2-j)=-(u^3-u)-((u+v)^3+u+v)
=-(u+v)^3-u^3-v.
\]
This checks the orientation and sign of the closing edge directly.
\(\square\)

In particular, if the four pairwise distinct vertices of the motif
all lie in an integer block \([s,s+k]\subseteq[0,L-1]\),
then all five edge differences are nonzero and have absolute value at
most \(k\). Their endpoints lie in \([0,L-1]\), so (16) puts every
shifted output index in its required interval. This is the exact gluing
justification for the coordinated block construction. Its number of
partner choices and its scalar, pair and output counts are charged in
the construction companion, rather than inferred from this identity.

### General shared-scalar rule within the same label model

Writing
\[
C_\sigma(j,u)=j-\frac{u^3-\sigma u}{2},\qquad \sigma\in\{1,-1\},
\]
the complete endpoint equality rule is
\[
\boxed{
C_\sigma(j,u)=C_\tau(\ell,v)
\quad\Longleftrightarrow\quad
\ell-j=\frac{v^3-\tau v-u^3+\sigma u}{2}.}                 \tag{20}
\]
Here \(\sigma,\tau\in\{1,-1\}\) are endpoint signs. All numerators
are even for integer differences.
This identity includes first/first, first/second and second/second reuse.
It follows by rearranging the scalar equality and introduces no extra
free incidence labels.

### Why it matters

The shifts (17) allow many different partner differences to be tested
against one common edge while preserving both closing edges exactly.
Boundary membership and repeated actual scalars remain part of the
construction. In particular, solving the algebra does not authorize
discarding any shifted label outside the prescribed interval or counting
two descriptions of the same scalar pair twice.

### Scope

This is an exact identity and boundary test for the chosen label
windows. It does not by itself count a growing number of valid partners,
good scalar reuse, near-full Cartesian coverage, or a full-image saving.
Those counts belong in the coordinated construction and rate ledger.
The square of the final scalar union includes all unprescribed cross-pairs.

## 4. Provenance and claim record

All new entries are T01, \(P=(x-y)^3+x+y\), real scalars, date
2026-10-06, version 1, with exact quantifiers at the indicated sections.
Evidence is the displayed proof. Author algebra checks and the lead's
independent internal review of the exact proofs are complete; all three
claims were accepted without a mathematical correction on 6 October 2026.
No external theorem, finite computation, novelty assessment or unavailable
source is a dependency.

| ID | Quantifiers and hypotheses | Proof locator / dependencies | Status and limit |
|---|---|---|---|
| VG-G1 | Every real five-label list and scalar quadruple, fixed shared-edge orientation | §1; inherited templates, new exact substitutions and reconstruction | PROVED equivalence; no prescribed density or full-support bound |
| VG-G2 | Every finite directed cycle length, all real vertices and ordered labels, including repetitions | §2; exact difference-of-cubes comparison, new even-cycle degeneracy argument | PROVED injectivity; not an arbitrary-network or complex uniqueness result |
| VG-G3 | Every integer k≥3, L=k³ and the displayed difference-dependent intervals I_u; all candidate partner differences | §3; exact integer parity, endpoint identities, VG-G1 orientation | PROVED gluing and boundary criterion; partner growth and rates not inferred |

The latest sharing report, its compatibility appendix, and the elliptic
checkpoint were read. The setup/map/migration, T01 and conflict records
remain the scope framework; missing originals in MC-06 are not used.
Earlier proof files and data remain unchanged. This note creates no
independent next research obligation and makes no claim about the truth
of the original T01 target.
