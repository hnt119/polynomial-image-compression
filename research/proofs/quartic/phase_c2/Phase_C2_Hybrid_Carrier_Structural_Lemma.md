# Phase C2: Hybrid carrier structural-lemma search

## Opening summary

### Final classification

**USEFUL STRUCTURAL LEMMA PROVED; FIXED-QUARTIC TARGET UNRESOLVED.** A one-relation
refinement of the supplied totally real tower forces the unique base prime
above 7 to split in every relative layer while retaining the source-selected
split primes and bounded root discriminant. On each resulting length-three
ramified factor, the exact image of \(2z^4\pm z\) has 208 of 343 elements.
Consequently the complete quartic image occupies at most

\[
208^{d_j/3}(\rho_4Q)^{d_j}
\]

classes modulo \(7Q\mathcal O_{F_j}\). This controls the total number of
occupied classes, not the population of any one class. It gives a full-support gain

\[
s_7=\frac13\log\frac{343}{208}>0
\]

per field degree beyond the earlier fourth-power class restriction.

The gain does not prove the target. Combined with the full continuous output
interval and uniform class packing, its normalized certificate remains worse
than the pair bound by at least

\[
\left(e^{-s_7}\rho_4Q\right)^{d_j}>1.
\]

The exact hybrid ratio audit also proves fiber rigidity and no gain from
the displayed elementary parameter count: for
every admissible ratio \(u\),

\[
|\mathcal K_u|=|T_j|^2,
\]

and the ratio union counted from its displayed parameters gives exactly the
trivial budget

\[
\sum_u |G_j(u)|\,|T_j|^2=|G_j|^2|T_j|^2=|C_j|^2.
\]

For each fixed point of \(\mathcal K_u\), varying the common action \(v\)
produces at least \(|G_j(u)|/4\) outputs. The displayed elementary count
therefore proves no positive gain. Possible savings from overlap would have to come
from overlaps across distinct points of \(\mathcal K_u\), possibly also
across ratios \(u\); no such full-support overlap theorem is present in the
supplied sources or proved here.

### The five required answers

| Question | Answer |
|---|---|
| What exact structural lemma was proved? | The ramified determinant-seven lemma: after a proved one-relation tower refinement, every local factor above 7 is \(\mathbb F_7[\pi]/(\pi^3)\), and \(2z^4\pm z\) has exactly 208 values there. Hybrid fiber rigidity and no gain from the displayed elementary parameter count were also proved. |
| What counting step uses it? | CRT gives at most \(208^{d_j/3}(\rho_4Q)^{d_j}\) output classes modulo \(7Q\mathcal O_{F_j}\); uniform per-class packing then covers the full output support. |
| What per-degree gain results? | The new final-output class gain is \(s_7=\frac13\log(343/208)\approx0.166731\). |
| What costs were charged? | The tower loses at most one pro-3 generator and adds at most one relation; carrier costs include the squared-unit \(\log2\), regulator \(D^d\), additive covolume \(D^{d/2}\), exact ratio union, and distortion. The interval/class certificate retains a wrong-sign deficit at least \(\log(\rho_4Q)-s_7>0\). |
| Was the quartic target proved? | No. The new local gain is too small for the old interval packing, while the elementary ratio certificate proves no positive gain; set \(\kappa_{\mathrm{cert}}=0\). A sharper realized-support theorem is still missing. |

The two C1 roadmap corrections are proved separately in
`C1_STATUS_ADDENDUM.md`. They are not counted as C2 progress. External novelty
and literature status have not been checked.

# 1. Research state and preservation

The corrected Phase C0 theorem is preserved with its existing scope. Within
the supplied offline source system, every fixed integral polynomial

\[
(ax+by)^2+cx+ey,
\qquad \gcd(a,b)=1,\qquad ab(ae-bc)\ne0,
\]

has arbitrarily large same-input finite real sets with a member-dependent
fixed power saving.

The C1 quartic results are also preserved. C1 proves the exact centered
continuous range, the translation-uniform transverse-width lemma, the
specified translated/anisotropic interval-packing obstruction, and the local
cost theorem for coordinate-product restrictions. None is a lower bound on
the actual quartic image.

The addendum makes only these status changes:

1. weak M1-DEFICIT is **PROVED - INSUFFICIENT FOR THE REQUIRED RATE**;
2. M2-CORR is proved at \(p=5,d=2\), while the general correlated statement
   has status **CONJECTURAL**.

The fixed target remains

\[
P_4(x,y)=(x+2y)^4+3x-y.
\]

# 2. Source manifest and simultaneous applicability

All work was offline. Supplied and frozen files were treated as read-only.
The discovery transcript `unit-distance-cot.pdf` was not proof authority.

| File | Portion inspected | Use |
|---|---|---|
| C2 assignment prompt | Entire file | Milestone, scope, stop rules, deliverables |
| C1 review memo | Entire file | Two elementary status corrections |
| Corrected Phase C0 report and PDF | Corrected theorem, field input, carrier, transport, rate, final scope | Preserved Phase C0 baseline |
| Phase C1 higher-degree report and PDF | Source input and Sections 4-10, especially 5, 6.4-6.6, 7.5-7.6, and 9 | C1 widths, certificate scope, signed rate, open statements |
| C0 correction log | Entire file | Field-symbol and scope corrections |
| C1 claim ledger | Entire file | Prior claim statuses |
| C1 referee report | Source, obstruction, rate, and final-check sections | Preserved referee findings |
| C1 source manifest | Entire file | Provenance and exclusions |
| Frozen Phase A reproduction report | Sections 3-6, 9, and 12 | Additive box, unit box, counts, directness, regulator, distortion, parameter order |
| Phase B Cycle 1 report and five living records | Factor-through lemma, rank-two bottleneck, collision warning, rate ledger | Hybrid support and multiplicity rules |
| Phase B Cycle 2 report | Local-to-global rate and fixed-polynomial rules | Rate cross-check only |
| Unit-distance proof source | Propositions 3.2-3.5, Proposition 3.8(P1)-(P4) and its proof, and Remark 3.9 | Base ramification, one-relation tower refinement, fixed split primes, parameter order |
| Local model-2 script | Screened and not run | The \(p=5,d=2\) proof is elementary |

Fix a sufficiently large source parameter \(\ell\), and put

\[
t=\left\lfloor\frac{(\ell-1)^2}{100}\right\rfloor.
\]

Proposition 3.8 starts from a totally real cyclic cubic field \(F\), the
maximal everywhere-unramified pro-3 group \(\mathfrak G\) over \(F\), and
fixed rational primes \(q_1,\ldots,q_t\equiv1\pmod4\). Write

\[
d_0=d(\mathfrak G),
\qquad r_0=r(\mathfrak G).
\]

The source proves

\[
d_0\ge\ell-1,
\qquad r_0\le d_0+C_0,
\]

and chooses the \(3t\) primes of \(F\) above the \(q_b\) so that their
Frobenius representatives lie in the Frattini subgroup.

## 2.1 One additional Frobenius relation at 7

In Proposition 3.2, the first conductor prime is \(r_1=7\), because the
\(r_i\) are the first primes congruent to 1 modulo 3. The product character
cutting out \(F\) has conductor divisible by 7, and the displayed
discriminant has 7-adic exponent 2. Hence 7 ramifies in the Galois cubic
field \(F\). Its inertia group is then the whole group of order 3, so there is
a unique prime \(\mathfrak p\) above 7 and

\[
7\mathcal O_F=\mathfrak p^3,
\qquad \mathcal O_F/\mathfrak p\cong\mathbb F_7.
\]

The prime \(\mathfrak p\) is unramified in the maximal unramified pro-3
extension of \(F\), so choose one Frobenius representative \(\tau_7\in
\mathfrak G\). In addition to the source's \(3t\) relations, quotient by the
closed normal closure of \(\tau_7\). One new relation can lower the generator
rank by at most one and raises the relation rank by at most one. The source's
Frattini Frobenii remain non-generators after this quotient. Thus the final
pro-3 quotient \(\widetilde{\mathfrak G}\) satisfies

\[
d(\widetilde{\mathfrak G})\ge d_0-1,
\qquad
r(\widetilde{\mathfrak G})\le d_0+C_0+3t+1.
\]

More explicitly, if the image of \(\tau_7\) in
\(\mathfrak G/\Phi(\mathfrak G)\) is zero, Proposition 3.3 preserves
\(d_0\) and adds at most one relation. If it is nonzero, invoke the standard
pro-\(p\) primitive-generator elimination fact. In a minimal free pro-3
presentation of \(\mathfrak G\), a lift of \(\tau_7\) has nonzero
Frattini image and extends to a free generating basis: complete its image
to a vector-space basis, then apply the pro-\(p\) Burnside basis theorem
and the Hopfian property of finitely generated free pro-\(p\) groups.
Imposing \(\tau_7=1\) deletes that free generator, and substituting it
by 1 in the old relators introduces no further relators. Thus the
generator rank drops by one and the looser relation bound above still
holds. Images of the source's Frattini elements remain in the Frattini
subgroup of every quotient.

For all sufficiently large \(\ell\),

\[
d_0+C_0+3t+1
<\frac{(d_0-1)^2}{4}
\le\frac{d(\widetilde{\mathfrak G})^2}{4}.
\]

To see this without asymptotic shorthand, put \(L=\ell-1\). The function
\((d-1)^2/4-d\) is increasing for \(d\ge3\), and at \(d=L\) the difference
between the right side and the stated relation upper bound is at least

\[
\frac{(L-1)^2}{4}-L-C_0-\frac{3L^2}{100}-1
=\frac{11L^2}{50}-\frac{3L}{2}-C_0-\frac34,
\]

which is positive for sufficiently large \(L\). Golod-Shafarevich therefore
makes \(\widetilde{\mathfrak G}\) infinite.

Take finite Galois layers of this quotient and relabel them \(F_j\). Then

\[
F=F_0\subset F_1\subset F_2\subset\cdots,
\qquad d_j=[F_j:\mathbb Q]\longrightarrow\infty.
\]

Every \(F_j/F\) is an everywhere-unramified 3-extension. The layers are
totally real, their root discriminant is the fixed value

\[
\operatorname{rd}(F_j)=\operatorname{rd}(F)=:D,
\]

every \(q_b\) still splits completely, and \(\mathfrak p\) now splits
completely in every relative layer. Put

\[
Q=\prod_{b=1}^tq_b.
\]

Since \(q_b\equiv1\pmod4\), one has \(7\nmid Q\). If
\(n_j=[F_j:F]=d_j/3\), complete relative splitting gives

\[
\boxed{
7\mathcal O_{F_j}
=\prod_{k=1}^{n_j}\mathfrak P_{j,k}^{3},
\qquad
\mathcal O_{F_j}/\mathfrak P_{j,k}\cong\mathbb F_7.}
\]

Also, with \(\Delta_j=|\operatorname{disc}(F_j)|\),

\[
\Delta_j=D^{d_j}.
\]

The Phase A lattice and unit lemmas are field-local statements for every
totally real field. Hence they apply to these same refined layers, including

\[
R_{F_j}\le\Delta_j=D^{d_j}.
\]

Thus ramified 7-adic repetition, root-discriminant control, regulator
control, the source-selected split primes, and growing degree hold
simultaneously. The source's CM fields \(F_j(i)\) are not used.

# 3. A source-compatible positive hybrid

Fix one layer, write \(F=F_j\), \(d=d_j\), \(\mathcal O=\mathcal O_F\),
\(R=R_F\), and \(\Delta=\Delta_j\). Let

\[
B_F^\times(Z)=
\{h\in\mathcal O^\times:|\log|\sigma_i(h)||\le Z\text{ for all }i\}
\]

and

\[
B_F^+(Z)=
\{b\in\mathcal O:|\sigma_i(b)|\le Z\text{ for all }i\}.
\]

Choose fixed parameters

\[
Y\ge2,\qquad X\in\mathbb Z_{>0},\qquad \tau X\ge1,
\qquad 0<\tau<\sqrt{5}-2.
\]

Define

\[
H_j=B_{F_j}^\times(Y/2),
\qquad
G_j=H_j^2=\{h^2:h\in H_j\},
\]

\[
T_j=X+B_{F_j}^+(\tau X),
\qquad
C_j=G_jT_j.
\]

Squaring is a deliberate replacement for silently assuming that Phase A's
unsigned unit count applies to totally positive units.

## 3.1 Positivity and distortion

Every \(g=h^2\in G_j\) is totally positive and satisfies

\[
e^{-Y}\le\sigma_i(g)\le e^Y.
\]

Every \(t\in T_j\) satisfies

\[
(1-\tau)X\le\sigma_i(t)\le(1+\tau)X,
\]

and is totally positive. Therefore

\[
e^{-Y}(1-\tau)X
\le\sigma_i(c)\le
e^Y(1+\tau)X
\qquad(c\in C_j).
\]

For \(u=g_1/g_2\), \(v=g_2\), with \(g_1,g_2\in G_j\),

\[
e^{-2Y}\le\sigma_i(u)\le e^{2Y},
\qquad
e^{-Y}\le\sigma_i(v),\sigma_i(uv)\le e^Y.
\]

The second pair of bounds retains the admissibility correlation; treating
\(u\) and \(v\) independently would introduce an avoidable distortion loss.

## 3.2 Counts and the squared-unit cost

The square map on \(H_j\) has fibers exactly \(\{h,-h\}\). Phase A's unit
count therefore gives

\[
\boxed{
\frac{(Y/2)^{d-1}}{2\sqrt d\,R}
\le |G_j|
\le5\left(\frac{5Y}{2}+1\right)^{d-1}.}
\]

The exponential sign cost comes from halving the logarithmic radius before
squaring: it is \(\log2\) per degree. The extra two-to-one kernel is only a
fixed factor and contributes \(o(d)\).

The additive count is

\[
\boxed{
(\tau X)^d\Delta^{-1/2}
\le |T_j|
\le(2\tau X+1)^d.}
\]

Since \(H_jH_j,H_j/H_j\subset B_F^\times(Y)\),

\[
G_jG_j=G_j/G_j
\subseteq\{w^2:w\in B_F^\times(Y)\},
\]

and hence

\[
\boxed{|G_jG_j|=|G_j/G_j|\le5(5Y+1)^{d-1}.}
\]

No additional congruence-fiber selection is imposed beyond the paid-for
restriction to squared units. No equidistribution of units modulo \(Q\)
is assumed.

There is one automatic upper-support restriction. At each completely split
\(q\mid Q\), every reduction of \(g=h^2\in G_j\) is a nonzero square in each
\(\mathbb F_q\)-coordinate. Thus the reduction of \(G_j\) is contained in a
set of size \(((q-1)/2)^d\). This is not a lower count for \(G_j\), and it is
not used as an input-density or image-saving factor.

## 3.3 Directness and multiplicity

Suppose \(g_1t_1=g_2t_2\). Then the unit

\[
w=g_1/g_2=t_2/t_1
\]

obeys

\[
\frac{1-\tau}{1+\tau}
\le\sigma_i(w)\le
\frac{1+\tau}{1-\tau}<\varphi,
\qquad \varphi=\frac{1+\sqrt{5}}{2}.
\]

Phase A unit separation gives \(w=\pm1\). Its embeddings are positive, so
\(w=1\). Thus

\[
\boxed{G_j\times T_j\longrightarrow C_j\text{ is injective},
\qquad \mu_j=1,\qquad |C_j|=|G_j||T_j|.}
\]

Using \(R\le\Delta=D^d\),

\[
|C_j|\ge
\frac1{Y\sqrt d}
\left(\frac{\tau XY}{2D^{3/2}}\right)^d.
\]

A valid pair of exponential rates is

\[
\boxed{
a=\log\frac{\tau XY}{2D^{3/2}},
\qquad
B=\log\left[\left(\frac{5Y}{2}+1\right)(2\tau X+1)\right].}
\]

Choose \(\tau,Y,X\) so that \(a>0\). Then \(|C_j|\to\infty\), and the
multiplicity rate is \(m=0\).

# 4. Exact quartic algebra and all-pairs support

Define

\[
F_Q(x,y)=(x+2y)^4+Q^3(3x-y).
\]

The exact transport identity is

\[
F_Q(Qx,Qy)=Q^4P_4(x,y).
\]

For \(g_i\in G_j\), \(t_i\in T_j\), the binomial theorem gives the seven
monomials

\[
\begin{aligned}
F_Q(g_1t_1,g_2t_2)
={}&g_1^4t_1^4
+8g_1^3g_2t_1^3t_2
+24g_1^2g_2^2t_1^2t_2^2\\
&+32g_1g_2^3t_1t_2^3
+16g_2^4t_2^4
+3Q^3g_1t_1-Q^3g_2t_2.
\end{aligned}
\]

All terms use the same four parameters. No marginal monomial supports are
multiplied.

## 4.1 Ratio and common-action decomposition

For \(u\in G/G\), put

\[
G(u)=\{v\in G:uv\in G\}.
\]

The map

\[
(g_1,g_2)\longmapsto(u,v)=(g_1/g_2,g_2)
\]

is a bijection from \(G^2\) to the admissible pairs
\(\{(u,v):u\in G/G,\ v\in G(u)\}\). Therefore

\[
\boxed{\sum_{u\in G/G}|G(u)|=|G|^2.}
\]

Define

\[
\mathcal K_u=
\{((ut_1+2t_2)^4,3ut_1-t_2):t_1,t_2\in T\}
\]

and

\[
\mathcal S_u=
\{v^4\alpha+Q^3v\beta:
v\in G(u),\ (\alpha,\beta)\in\mathcal K_u\}.
\]

Substitution gives

\[
F_Q(uvt_1,vt_2)
=v^4(ut_1+2t_2)^4+Q^3v(3ut_1-t_2).
\]

Since directness makes the parameterization of \(C^2\) unique, this is an
exact reparameterization of every input pair:

\[
\boxed{F_Q(C,C)=\bigcup_{u\in G/G}\mathcal S_u.}
\]

The condition \(v\in G(u)\) is essential. Replacing it by independent
\((G/G)\times G\) would be incorrect.

## 4.2 Integrality and transformed embedding bounds

All transformed variables remain in the same field and integral domain:

\[
u,v,uv\in\mathcal O^\times,
\qquad
L=ut_1+2t_2\in\mathcal O,
\qquad
M=3ut_1-t_2\in\mathcal O.
\]

Put \(a_0=1-\tau\) and \(b_0=1+\tau\). For every embedding,

\[
a_0X(e^{-2Y}+2)
\le\sigma_i(L)\le
b_0X(e^{2Y}+2),
\]

\[
X(3a_0e^{-2Y}-b_0)
\le\sigma_i(M)\le
X(3b_0e^{2Y}-a_0).
\]

The admissibility conditions \(v,uv\in G\) give the sharper evaluated
bounds

\[
3a_0Xe^{-Y}
\le\sigma_i(vL)\le
3b_0Xe^Y,
\]

\[
X(3a_0e^{-Y}-b_0e^Y)
\le\sigma_i(vM)\le
X(3b_0e^Y-a_0e^{-Y}).
\]

In particular, every output satisfies the uniform containment

\[
|\sigma_i(F_Q(C,C))|
\le81b_0^4X^4e^{4Y}+4Q^3b_0Xe^Y.
\]

This bound retains the true \(e^Y\) distortion of each original input. Using
it only as a Minkowski box falls under Attempt 1 below and gives no saving.

## 4.3 The hybrid fiber-rigidity theorem

**Theorem C2.1 (fiber rigidity and elementary no-gain).** For every
\(u\in G/G\), the map

\[
(t_1,t_2)\longmapsto
((ut_1+2t_2)^4,3ut_1-t_2)
\]

is injective on \(T^2\). Consequently \(|\mathcal K_u|=|T|^2\). Moreover,
for every fixed \((\alpha,\beta)\in\mathcal K_u\),

\[
\left|
\{v^4\alpha+Q^3v\beta:v\in G(u)\}
\right|
\ge\frac{|G(u)|}{4}.
\]

Finally, counting only the displayed parameters and then taking the union
gives exactly the trivial upper bound \(|C|^2\).
This conclusion concerns that elementary count only. Overlaps across
distinct points of \(\mathcal K_u\), and possibly across different ratios,
are not ruled out.

**Proof.** Put

\[
L=ut_1+2t_2,
\qquad M=3ut_1-t_2.
\]

The linear coefficient matrix is

\[
\begin{pmatrix}u&2\\3u&-1\end{pmatrix},
\qquad \det=-7u\ne0.
\]

The exact inverse over \(F\) is

\[
t_1=\frac{L+2M}{7u},
\qquad
t_2=\frac{3L-M}{7}.
\]

If two pairs give the same \((L^4,M)\), then their \(L\)'s differ by a
fourth root of unity. A totally real field has only \(\pm1\) as possible
fourth roots in the field, and both \(L\)'s are totally positive. Hence the
two \(L\)'s agree. Invertibility then recovers the same \((t_1,t_2)\).
Thus \(|\mathcal K_u|=|T|^2\).

For fixed \((\alpha,\beta)\), \(\alpha=L^4\ne0\). The equation

\[
\alpha v^4+Q^3\beta v=z
\]

has at most four solutions \(v\in F\). Its image on \(G(u)\) therefore has
at least \(|G(u)|/4\) elements. This is a lower bound and cannot be used as
an upper-support certificate.

The elementary parameter count is

\[
\begin{aligned}
|F_Q(C,C)|
&\le\sum_u|\mathcal S_u|\\
&\le\sum_u|G(u)|\,|\mathcal K_u|\\
&=|T|^2\sum_u|G(u)|\\
&=|G|^2|T|^2=|C|^2.
\end{aligned}
\]

No strict factor is present in this elementary upper-bound calculation.
\(\square\)

The inverse formulas are over \(F\), not over \(\mathcal O\). Division by
7 is not being used to claim a lattice automorphism. All forward expressions
remain integral because \(u,v\) are units and \(t_i\in\mathcal O\).

# 5. Three bounded structural attempts

## 5.1 Attempt 1: enclose the hybrid in a box

Every embedding of \(C_j\) lies in the fixed interval

\[
I=[X(1-\tau)e^{-Y},X(1+\tau)e^Y].
\]

Let \(c\) and \(r\) be its center and radius. If one allows the full
continuous interval \(F_Q(I,I)\), the old fourth-power residue envelope, and
norm-separation packing, C1 gives

\[
W_Q(c,r)+Q\ge Q(2r+1)^2.
\]

Since \(|C_j|\le(2r+1)^{d_j}\), that numerical certificate is at least

\[
(\rho_4Q)^{d_j}|C_j|^2,
\qquad
\rho_4=\prod_{p\mid Q}\frac{p+3}{4p},
\]

and

\[
\rho_4Q=\prod_{p\mid Q}\frac{p+3}{4}\ge2^t>1.
\]

The hybrid is sparser than the containing interval, so enclosure only makes
this comparison worse. This branch is stopped exactly within the C1
certificate obstruction; it says nothing about the actual output support.

## 5.2 Lemma card A: multiply the two marginal supports

The tempting cover is

\[
F_Q(C,C)\subseteq(C+2C)^4+Q^3(3C-C).
\]

Because \(C\) is positive, the map

\[
(x,y)\longmapsto((x+2y)^4,3x-y)
\]

is injective on \(C^2\): positivity recovers \(x+2y\) from its fourth
power, and

\[
x=\frac{(x+2y)+2(3x-y)}7,
\qquad
y=\frac{3(x+2y)-(3x-y)}7.
\]

Therefore

\[
|C|^2
\le |(C+2C)^4|\,|3C-C|
=|C+2C|\,|3C-C|.
\]

The marginal-product upper bound can never be smaller than the trivial pair
budget. **Card verdict: REJECTED - EXACT NO-GAIN.**

## 5.3 Lemma card B: determinant-seven graph

**Lemma C2.2 (determinant-seven graph).** For a unit \(u\in\mathcal O^\times\)
define

\[
\Lambda_u(t_1,t_2)=(a,b)
=(ut_1+2t_2,3ut_1-t_2).
\]

Then

\[
\boxed{
\Lambda_u(\mathcal O^2)
=\{(a,b)\in\mathcal O^2:a+2b\in7\mathcal O\}.}
\]

This submodule has index \(7^d\). Consequently

\[
\mathcal K_u\bmod7\mathcal O
\subseteq
\{(2r^4,r):r\in\mathcal O/7\mathcal O\},
\]

and every final output obeys

\[
\boxed{
F_Q(C,C)\bmod7\mathcal O
\subseteq
\{2z^4+Q^3z:z\in\mathcal O/7\mathcal O\}.}
\]

**Proof.** Direct calculation gives \(a+2b=7ut_1\). Conversely, if
\(a+2b=7c\), choose

\[
t_1=u^{-1}c,
\qquad t_2=3c-b.
\]

These are integral and map to \((a,b)\). The homomorphism

\[
\mathcal O^2\longrightarrow\mathcal O/7\mathcal O,
\qquad(a,b)\longmapsto a+2b
\]

is onto, so the kernel has index \(|\mathcal O/7\mathcal O|=7^d\).
Modulo 7, \(a\equiv-2b\), hence \(a^4\equiv2b^4\). For an evaluated point,
put \(z=vb\); then

\[
v^4a^4+Q^3vb\equiv2z^4+Q^3z\pmod{7\mathcal O}.
\]

This proves the assertions. \(\square\)

The graph description alone does not shrink \(|\mathcal K_u|\), which remains
exactly \(|T|^2\). The ramified local rings from Section 2.1 nevertheless
make the scalar graph genuinely restrictive.

**Theorem C2.3 (ramified local image).** Let

\[
\mathcal R=\mathcal O_{F_j}/\mathfrak P_{j,k}^3.
\]

Then \(\mathcal R\cong\mathbb F_7[\pi]/(\pi^3)\). For either
\(s\in\{1,-1\}\), the map

\[
h_s(z)=2z^4+sz
\]

has exactly 208 values on the 343-element ring \(\mathcal R\).

**Proof.** The ring has characteristic 7, residue field \(\mathbb F_7\), a
principal maximal ideal generated by \(\pi\), and length three. Thus every
element has a unique form \(a+b\pi+c\pi^2\) with \(a,b,c\in\mathbb F_7\).
Expansion modulo \(\pi^3\) gives

\[
\begin{aligned}
h_s(a+b\pi+c\pi^2)
={}&h_s(a)+(a^3+s)b\pi\\
&+\big((a^3+s)c+5a^2b^2\big)\pi^2.
\end{aligned}
\]

On the residue field, direct evaluation gives

\[
h_+(0,1,\ldots,6)=(0,3,6,4,5,2,1),
\]

\[
h_-(0,1,\ldots,6)=(0,1,2,5,4,6,3).
\]

Both residue maps are permutations. The derivative coefficient \(a^3+s\)
vanishes at exactly three residues. At each of the other four residues, the
map from \((b,c)\) to the two nilpotent coefficients is bijective, giving
\(7^2=49\) outputs. At a critical residue, the \(\pi\)-coefficient is zero
and the \(\pi^2\)-coefficient is the nonzero scalar \(5a^2\) times \(b^2\).
There are four square values, while \(c\) is invisible. Distinct residues
have distinct constant outputs because the residue map is a permutation.
Therefore

\[
|h_s(\mathcal R)|=4\cdot49+3\cdot4=208.
\]

This proves the theorem. \(\square\)

Since \(7\nmid Q\), its cube modulo 7 is one of \(\pm1\). CRT over the
\(d_j/3\) local factors now gives

\[
\boxed{
|F_Q(C_j,C_j)\bmod7\mathcal O_{F_j}|
\le208^{d_j/3}.}
\]

At every source-selected \(q\mid Q\), the output is a fourth power modulo
\(q\), so the earlier split-prime bound permits at most
\((\rho_4Q)^{d_j}\) classes modulo \(Q\mathcal O_{F_j}\). Since \(7\) and
\(Q\) are coprime, another CRT step yields the complete class bound

\[
\boxed{
|F_Q(C_j,C_j)\bmod7Q\mathcal O_{F_j}|
\le208^{d_j/3}(\rho_4Q)^{d_j}.}
\]

Relative to all \(7^{d_j}\) classes at 7, this is the genuine per-degree
saving

\[
\boxed{
s_7=\frac13\log\frac{343}{208}
\approx0.166731>0.}
\]

The earlier index \(7^d\) for the two-coordinate graph is not counted again;
Theorem C2.3 is its scalar, full-output consequence.

**Card verdict: USEFUL STRUCTURAL LEMMA PROVED.** It gives a quantified
full-support class saving. Section 6 tests whether that saving survives the
archimedean and carrier costs.

# 6. Complete rate ledger

Define the proved squared-unit rates

\[
g_- =\log\frac{Y}{2D},
\qquad
g_+=\log\left(\frac{5Y}{2}+1\right),
\]

\[
t_- =\log(\tau X)-\frac12\log D,
\qquad
t_+=\log(2\tau X+1).
\]

Then

\[
a=g_-+t_-=
\log\frac{\tau XY}{2D^{3/2}},
\qquad
B=g_++t_+,
\qquad m=0.
\]

## 6.1 Ramified local gain and the full packing cost

Let \(I\) be the common embedding interval from Attempt 1, with center \(c\),
radius \(r\), and exact continuous output width \(W_Q(c,r)\). Uniform packing
inside one class modulo \(7\mathcal O_{F_j}\) first gives the full-support
certificate

\[
U_7=208^{d_j/3}
\left(1+\frac{W_Q(c,r)}7\right)^{d_j}.
\]

Put \(S=2r+1>1\). Since \(|C_j|\le S^{d_j}\) and C1 gives
\(W_Q(c,r)+Q\ge QS^2\),

\[
\begin{aligned}
\frac{U_7^{1/d_j}}{S^2}
&\ge208^{1/3}\frac{1+W_Q(c,r)/7}{S^2}\\
&\ge\frac{208^{1/3}}7
\left(Q+\frac{7-Q}{S^2}\right)\\
&>\frac{5\,208^{1/3}}7>4.2.
\end{aligned}
\]

Thus even the new modulus 7 alone gives a numerical interval certificate
strictly worse than \(|C_j|^2\). This check is necessary because adding an
optional modulus can otherwise make an upper-bound certificate worse.

For completeness, combining both independent local restrictions is also
nontrivial in the wrong direction. Uniform packing inside one class modulo
\(7Q\mathcal O_{F_j}\) gives at most

\[
\left(1+\frac{W_Q(c,r)}{7Q}\right)^{d_j}
\]

outputs. Theorem C2.3 and the split-prime fourth-power restriction therefore
give the full-support certificate

\[
\boxed{
U_{7Q}=
208^{d_j/3}(\rho_4Q)^{d_j}
\left(1+\frac{W_Q(c,r)}{7Q}\right)^{d_j}.}
\]

This is a valid upper bound, with no equidistribution assumption. C1's
transverse-width theorem gives

\[
W_Q(c,r)+Q\ge Q(2r+1)^2.
\]

Consequently

\[
1+\frac{W_Q(c,r)}{7Q}
=\frac{W_Q(c,r)+7Q}{7Q}
\ge\frac{(2r+1)^2}{7}.
\]

Since \(|C_j|\le(2r+1)^{d_j}\), the numerical certificate satisfies

\[
\boxed{
\frac{U_{7Q}}{|C_j|^2}
\ge
\left(\frac{208^{1/3}}7\rho_4Q\right)^{d_j}
=\left(e^{-s_7}\rho_4Q\right)^{d_j}.}
\]

Every selected prime is at least 5, so \(\rho_4Q\ge2^t\ge2\), whereas
\(e^{-s_7}=(208/343)^{1/3}\approx0.846427\). Thus

\[
\log(\rho_4Q)-s_7
\ge\log2-s_7
\approx0.526416>0.
\]

The local lemma contributes the positive gain \(s_7\), but the old
interval-and-class architecture remains nontrivial in the wrong direction.
Using the hybrid's actual size rather than its interval upper bound can only
make this numerical comparison worse. This is an insufficiency result for
that certificate, not an image lower bound.

## 6.2 Unit quotient rate and the remaining overlap screen

The quotient upper rate is

\[
\rho_G=\log(5Y+1).
\]

Hence the available unit quotient gain is

\[
\boxed{
\Lambda_G=2g_--\rho_G
=\log\frac{Y^2}{4D^2(5Y+1)}.}
\]

It is positive exactly when

\[
Y>10D^2+2D\sqrt{25D^2+1}.
\]

This proves that the squared-unit set genuinely has exponentially small
quotient support relative to \(|G|^2\). The quartic must still factor through
that quotient saving.

For a precise screen, write \(n_u=|G(u)|\). Suppose a future theorem proved,
uniformly in every occupied \(u\),

\[
|\mathcal S_u|
\le e^{\chi d+o(d)}n_u^\theta|T|^2,
\qquad0\le\theta\le1.
\]

Concavity gives

\[
\sum_u n_u^\theta
\le |G/G|^{1-\theta}
\left(\sum_un_u\right)^\theta
=|G/G|^{1-\theta}|G|^{2\theta}.
\]

After the ratio union and multiplicity are charged, the normalized gain is

\[
\boxed{
\kappa\ge(1-\theta)\Lambda_G-\chi-2m.}
\]

For the proved carrier \(m=0\). The elementary ratio-support count in Theorem
C2.1 has \(\theta=1,\chi=0\). The elementary ratio certificate proves
no positive gain; set

\[
\boxed{\kappa_{\mathrm{cert}}=0.}
\]

This convention does not determine the exponent of the actual polynomial
image. The preceding conditional formula is a rate screen, not a claimed
support theorem. The degree-four
fiber lower bound also shows that a uniform \(\theta<1\) cannot come merely
from collapsing \(v\) while one point of \(\mathcal K_u\) is fixed. It would
have to use overlaps between different carrier points.

| Quantity | Proved value or bound | Rate effect |
|---|---|---|
| Root discriminant | \(\Delta_j=D^{d_j}\) | additive cost \(\tfrac12\log D\) |
| Regulator | \(R_j\le D^{d_j}\) | unit cost \(\log D\) |
| Positive squared units | radius \(Y/2\), square kernel 2 | \(\log2\) per degree from radius halving; kernel is \(o(d)\) |
| Additive carrier | \((\tau X)^d\Delta_j^{-1/2}\le|T_j|\) | \(t_-\) above |
| Product multiplicity | \(\mu_j=1\) | \(m=0\) |
| Ratio union | \(\sum_u|G(u)|=|G|^2\) | fully charged, no independent-product error |
| Intermediate support | \(|\mathcal K_u|=|T|^2\) | no saving |
| Fixed-point common action | fibers at most 4 | no exponential upper-support saving |
| Ramified determinant-seven image | \(208\) of \(343\) values per length-three local factor | \(s_7=\frac13\log(343/208)>0\) per degree |
| Combined \(7Q\) interval packing | all classes and every output covered | remaining wrong-sign gap at least \(\log2-s_7\) per degree |
| Archimedean distortion | \(|\sigma(c)|\le X(1+\tau)e^Y\) | retained; old box certificate remains nonpositive |
| Unit congruence restriction | no additional congruence-fiber selection beyond squared units | squared-unit cost already charged; no further density cost |
| Transport | injective embedding and fixed scaling | zero cardinality cost |

# 7. Parameter order and transport

A simultaneous valid order is:

1. choose \(\ell\), choose the source primes, impose their Frobenius
   relations together with the one relation at \(\mathfrak p\mid7\), and
   thereby fix the refined tower, \(D\), \(t\), and \(Q\);
2. choose fixed \(0<\tau<\sqrt{5}-2\);
3. choose fixed \(Y\ge2\), and if quotient absorption is to be available,
   impose the exact threshold \(\Lambda_G>0\);
4. choose a fixed integer \(X\) with \(\tau X\ge1\) and
   \(\tau XY>2D^{3/2}\);
5. only then let \(j\to\infty\).

No parameter or polynomial coefficient varies with \(j\).

For any fixed real embedding \(\sigma_j:F_j\hookrightarrow\mathbb R\), put

\[
A_j=Q^{-1}\sigma_j(C_j).
\]

The embedding and scalar multiplication are injective, so

\[
|A_j|=|C_j|\longrightarrow\infty
\]

and

\[
|P_4(A_j,A_j)|=|F_Q(C_j,C_j)|.
\]

Thus a future \(\kappa>0\) would complete the fixed-polynomial proof with
any fixed

\[
0<\varepsilon<\frac\kappa B.
\]

Neither audited certificate proves a positive gain: the elementary ratio
certificate has \(\kappa_{\mathrm{cert}}=0\), while the combined
interval-and-class certificate is worse than the pair budget. Thus this
conversion cannot be invoked from these estimates. The exponent of the
actual polynomial image remains undetermined.

# 8. Attempt ledger and exact surviving gap

| Attempt | Concrete mechanism | Fully charged result | Verdict |
|---:|---|---|---|
| 1 | Enclose \(G_jT_j\) in its embedding interval; use fourth-power classes and uniform packing | Numerical certificate at least \((\rho_4Q)^{d_j}|C_j|^2\) | STOPPED: existing C1 certificate obstruction |
| 2 | Factor through the marginal supports \((C+2C)^4\) and \(3C-C\) | Their product is at least \(|C|^2\) by injectivity | REJECTED: exact no-gain |
| 3 | Ratio/common-action support, determinant-seven graph, and one-relation ramified tower refinement | Local class gain \(s_7=\frac13\log(343/208)>0\); combined interval certificate still loses at least \(\log2-s_7\); elementary ratio certificate proves no positive gain, so \(\kappa_{\mathrm{cert}}=0\) | USEFUL STRUCTURAL LEMMA PROVED; FIXED-QUARTIC TARGET UNRESOLVED |

The exact unresolved mathematical gap is not carrier growth, signs,
multiplicity, field compatibility, or parameter order. It is an upper bound
for the complete evaluated union that exploits overlaps across distinct
points of \(\mathcal K_u\) and survives the ratio sum. The rate screen shows
exactly what would be sufficient, but no such theorem is claimed here.

Nothing in this report proves a lower bound near \(|C_j|^2\) for the actual
quartic image. It rules out only the three stated counting routes. A different
support theorem for the same carrier, a different source-compatible carrier,
or another mechanism remains logically possible.

**Final quartic status: UNRESOLVED.**

**Final C2 status: USEFUL STRUCTURAL LEMMA PROVED; FIXED-QUARTIC TARGET UNRESOLVED.**
