# Independent subfield, spreading, and rate audit

6 October 2026 · T03 · version 1 · fixed polynomial
\(Q(x,y)=x^2+xy+y^2\). Specialist C; independent internal audit.

## 1. Scope and provenance

The current explicitly authorized cycle is **XB-O1 → Cross-Block Fiber
Growth**. This auditor verifies the field setup and then the lead-selected
candidate proposals. No web, external lookup, mathematical program,
nested agent, or unrelated carrier search is used. Program accounting
for this contribution is zero exact evaluations and zero research-program
CPU seconds. These are symbolic mathematical checks, not an external
review or a novelty assessment.

The frozen [cross-block report](../2026-10-06-cross-block-returns/README.md)
and its [full-fiber proofs](../2026-10-06-cross-block-returns/audit.md)
were inspected. XB-F1 and XB-F2 concern the two specified dyadic carriers;
they are not applied automatically to a new carrier. Their explicit
XB-O1 successor asks for coordinate spreading over every index-two real
subfield in the prescribed 7-power cyclotomic model.

The existing accepted cyclotomic degree input is recorded in
`local-only/migration/sources/T03_CURRENT_STATE.md`, §10, “Precise
standard results assumed,” item 6. No new outside theorem is imported.
The elementary identifications below supply the needed subfield and
projective-class facts explicitly. Standard finite Galois correspondence
is used with the displayed cyclotomic automorphism group.

## 2. FG-AUD1 — exact real quadratic subfield

**Status: PROVED; independently derived and checked in this task.** Let
\(h\ge1\), \(q=7^h\), \(\xi=e^{2\pi i/q}\), and
\(\omega=e^{2\pi i/3}\). Put
\[
E=\mathbb Q(\zeta_{6q})=\mathbb Q(\xi,\omega),\qquad
K=E\cap\mathbb R,
\qquad F=\mathbb Q(\xi+\xi^{-1}).
\tag{1}
\]
Then
\[
[K:\mathbb Q]=6\cdot7^{h-1},\qquad
[F:\mathbb Q]=3\cdot7^{h-1},\qquad
K=F(\sqrt{21}).
\tag{2}
\]
The field \(F\) is the **unique index-two subfield of \(K\)**. It is
not being confused with the unique degree-two subfield over \(\mathbb Q\).

### Cyclotomic group and involution

Because \(3q\) is odd, \(\mathbb Q(\zeta_{6q})=
\mathbb Q(\zeta_{3q})\). Coprimality of 3 and \(q\) gives the second
equality in (1). The cyclotomic degree is
\(\varphi(3q)=2\varphi(q)=12\cdot7^{h-1}\). Complex conjugation has
order two and fixes the real subfield, so the degree of \(K\) is half
this. Likewise \(\xi\) satisfies a quadratic over
\(\mathbb Q(\xi+\xi^{-1})\), and is nonreal; hence \(F\) has half
the degree \(\varphi(q)\). This proves the degree statements.

Every cyclotomic automorphism is given by a unit exponent. By the Chinese
remainder theorem and quotienting by complex conjugation,
\[
\operatorname{Gal}(K/\mathbb Q)
\cong (\mathbb Z/3q\mathbb Z)^\times/\{\pm1\}
\cong (\mathbb Z/q\mathbb Z)^\times.
\tag{3}
\]
The final isomorphism chooses the unique representative of each sign
coset that is 1 modulo 3. Its residue modulo \(q\) is arbitrary.

For clarity, this group is cyclic: 3 has order 6 modulo 7, and
\(3^6=1+7\cdot104\), with \(7\nmid104\). The elementary binomial
identity gives
\[
v_7\bigl((3^6)^{7^r}-1\bigr)=r+1\qquad(r\ge0).
\]
Indeed if \(v_7(u-1)=s\ge1\), the first binomial term in
\(u^7-1\) has valuation \(s+1\), while every later term has larger
valuation. The order of 3 modulo \(7^h\) therefore is
\(6\cdot7^{h-1}\), the full unit-group size.

In particular the group in (3) has a unique involution. Equivalently,
one can see uniqueness directly from
\((b-1)(b+1)\equiv0\pmod{7^h}\): the two factors cannot both be
divisible by 7, so \(b\equiv\pm1\pmod{7^h}\).
Its nonidentity involution is induced on \(E\) by the exponent
\[
a\equiv1\pmod3,\qquad a\equiv-1\pmod q.
\]
Denote this automorphism by \(\sigma\). It fixes \(\omega\), sends
\(\xi\) to \(\xi^{-1}\), preserves \(K\), and fixes \(F\)
pointwise. The degrees in (2) show that its fixed field inside \(K\)
is exactly \(F\). The unique order-two subgroup of (3), together with
Galois correspondence, proves uniqueness of the index-two subfield.

### An explicit square root of 21

This identification needs no quadratic Gauss-sum theorem. Set
\(\eta=\xi^{7^{h-1}}\), a primitive seventh root, and put
\[
A=\eta+\eta^2+\eta^4,\qquad
B=\eta^3+\eta^5+\eta^6,\qquad s=A-B.
\]
Since \(A+B=-1\), and direct multiplication gives
\(AB=3+\sum_{j=1}^6\eta^j=2\),
\[
s^2=(A+B)^2-4AB=-7.
\tag{4}
\]
Complex conjugation exchanges \(A\) and \(B\), so it negates \(s\).
The automorphism \(\sigma\) does the same. Let
\(\Delta=1+2\omega\), for which \(\Delta^2=-3\). Then
\[
t=\Delta s\in K,\qquad t^2=21,
\qquad \sigma(t)=-t.
\tag{5}
\]
The product is real because both factors are negated by complex
conjugation. It is nonzero, and is not fixed by \(\sigma\), hence
\(t\notin F\). Since \([K:F]=2\), we obtain
\(K=F(t)=F(\sqrt{21})\). The sign of the chosen real square root is
irrelevant to the field and to the line tests.

### Meaning and scope

For the current 7-power model, the maximum in the XB-O1 gate over
index-two subfields contains exactly one field, namely \(F\). The
description is valid for every \(h\ge1\), corresponding to the frozen
parameter \(k=h+1\ge2\). No assertion is made for \(h=0\), where the
degrees and quadratic extension would be different.

## 3. FG-AUD2 — exact projective-class test

**Status: PROVED; independently checked in this task.** For nonzero
\(a,b\in K\),
\[
aF=bF
\quad\Longleftrightarrow\quad
\frac a{\sigma(a)}=\frac b{\sigma(b)}.
\tag{6}
\]
Indeed the first condition is \(a/b\in F\), equivalently
\(\sigma(a/b)=a/b\), and cross multiplication gives the second.
All denominators are nonzero because \(\sigma\) is an automorphism.

Thus the line population in a finite real scalar carrier is exactly a
fiber cardinality of the map
\[
a\longmapsto a/\sigma(a),\qquad a\ne0.
\tag{7}
\]
The values in (7) have relative norm one for \(K/F\). This relative
norm is distinct from the Eisenstein norm \(E/K\) that defines \(Q\);
the two action or norm conditions must not be conflated.

**Audit requirement for each selected candidate.** Spreading requires a
uniform upper bound for every fiber of (7) on the actual coordinate
completion, together with upper and lower bounds for its actual scalar
cardinality. Many projective classes alone do not bound the largest
class. Spreading of amplitudes alone does not establish spreading of the
union of their two coordinate projections. Formal orbit addresses,
amplitude cosets, scalar coordinates, and returned target pairs remain
four separate counts.

## 4. Candidate audit status

### Relative-norm formula: immediate coset defect

The one norm-coupled formula supplied for inspection is
\[
c_{b,r}=b\prod_{a=0}^{6}(2-\xi^{r+a q/7}),
\qquad 1\le b\le8,\quad r\in\mathbb Z/q\mathbb Z.
\tag{8}
\]
**Audit verdict: the scoped preselection rejection is valid.** The factors
run over all seventh-root rotations of \(\xi^r\), so
\[
c_{b,r}=b(128-\xi^{7r}).
\tag{9}
\]
All amplitudes are nonzero. For each fixed \(b\), the \(q\) labels repeat
in classes of exactly seven under \(r\mapsto r+q/7\). Therefore the
\(8q\) labels provide at most \(8q/7\) actual amplitudes and at most that
many distinct cosets modulo \(\mu_{6q}\). They cannot satisfy the
prescribed requirement of \(8q\) disjoint amplitude cosets. With a fixed
rotation index, the encoded complex pair state also has at least seven
identical labels. Phase relabeling cannot make equal full cosets disjoint.

For the proposed iterated norm formula
\(b(2^{7^\ell}-\xi^{7^\ell r})\), the same argument gives repetition
\(7^\ell\), with the explicit domain \(1\le\ell\le h\). The auditor
requested this domain qualification before acceptance. No additional
iteration or variation is searched here.

This is a failure of the stated amplitude/label requirement. It does not
assert any image bound or return obstruction for a carrier obtained by
deduplicating these labels. No input or output exponential rate is inferred
from the formal label count.

### Remaining candidate audit boundary

No candidate full-fiber or asymptotic rate conclusion is accepted merely
from the field setup or (9). The lead selects at most two explicit
proposals. The field calculation is a structural input to their audits,
not an additional construction or an authorization for a third search.

## 5. Twisted-binomial finalist: cosets, scalar size, and spreading

The approved first finalist is
\[
c_{H,j}=H(1+\omega\xi^j),\qquad
1\le H\le8,\quad j\in\mathbb Z/q\mathbb Z.
\tag{10}
\]
Capital \(H\) denotes the bounded integer scale, to distinguish it from
the growing depth \(h\). All amplitudes are nonzero: a zero would require
a \(q\)-th root to equal \(-\omega^2\), which has order six.

### Sparse relations and distinct cosets

**Audit verdict: PASS.** The already checked degrees give
\([\mathbb Q(\xi,\omega):\mathbb Q(\omega)]=\varphi(q)\), so the
minimal polynomial of \(\xi\) over \(\mathbb Q(\omega)\) is
\[
\Phi_q(T)=\sum_{j=0}^{6}T^{j q/7}.
\tag{11}
\]
No additional splitting or local irreducibility theorem is needed here.
If a polynomial of degree below \(q\) vanishes at \(\xi\), it is
\(\Phi_q R\), with \(\deg R<q/7\). Its coefficients are constant
on each seven-position block
\(r,r+q/7,\ldots,r+6q/7\), \(0\le r<q/7\). In particular a
nonzero such relation has at least seven nonzero coefficients.

Equality of two amplitude norms gives
\[
2(H^2-G^2)+H^2\omega\xi^j+H^2\omega^2\xi^{-j}
-G^2\omega\xi^\ell-G^2\omega^2\xi^{-\ell}=0.
\tag{12}
\]
After reducing exponents modulo \(q\), this has support at most five,
so every coefficient is zero. If \(j=\ell\), this forces \(H=G\).
If \(j=-\ell\ne0\), it would force
\(H^2\omega=G^2\omega^2\), impossible for positive rational scales.
All remaining distinct nonzero indices leave an uncancelled coefficient.
If exactly one index is zero, the other two nonzero exponent coefficients
cannot disappear; if both are zero, equality is again \(H=G\).
Thus all \(8q\) norms are distinct, and hence all the amplitude cosets
modulo \(\mu_{6q}\) are disjoint.

### Exact coordinate completion

Set
\[
C_a=(\xi^a+\xi^{-a})/2\in F,\qquad
D_a=(\xi^a-\xi^{-a})/(2\Delta)\in tF.
\]
Both quantities are real and satisfy \(C_a^2+3D_a^2=1\). The decoded
coordinates of \(\xi^a+\omega\xi^b\) are
\[
X_{ab}=C_a+D_a-2D_b,\qquad
Y_{ab}=-C_b-2D_a+D_b,
\tag{13}
\]
since \(X_{ab}-\omega Y_{ab}=\xi^a+\omega\xi^b\).
The common scalar completion is exactly
\[
A=\bigcup_{H=1}^{8}\{\pm HX_{ab},\ \pm HY_{ab},
\ \pm H(X_{ab}+Y_{ab}):a,b\bmod q\}.
\tag{14}
\]
The six unit rotations give these coordinate types, and the \(q\)
rotations shift both angular indices. Consequently (14) accounts for
both coordinate projections of every prescribed orbit, using one real
set in both variables.

For odd \(q\), the map \(a\mapsto D_a\) is injective: equality of
the corresponding sine values would give equal angles or supplementary
angles, and the latter require a half-integral residue modulo odd \(q\).
Also \(C_a\ne0\), since a \(q\)-th root cannot have order four.
Equality of two \(X\) values forces \(C_a=C_{a'}\), hence
\(a'=a\) or \(-a\). Each of those possibilities determines \(D_{b'}\)
and then \(b'\) uniquely. The \(q^2\) labels \(X_{ab}\) therefore
have fibers at most two. Writing \(n=|A|\),
\[
q^2/2\le n\le48q^2.
\tag{15}
\]
These are counts of actual scalar values, not orbit addresses.

### Uniform projective spreading

**Audit verdict: PASS for the live fixed-prefactor gate.** A line with
nonzero even component has the form \(O=RE\), with fixed \(R\in tF\),
where \(E\in F\) and \(O\in tF\) are the even and odd components of
a scalar. On the \(X\) array, fixing \(a\) determines \(D_b\), hence
at most one \(b\). On the \(Y\) array, fixing \(b\) similarly leaves
at most one \(a\). Thus each of those arrays contributes at most \(q\)
labels to a fixed line. On
\[
X_{ab}+Y_{ab}=(C_a-C_b)-(D_a+D_b),
\]
fixing \(a\) leaves one real linear equation in \((C_b,D_b)\). Its
intersection with \(C_b^2+3D_b^2=1\) has at most two points, hence at
most two indices \(b\). This array contributes at most \(2q\).

For the pure odd line, the \(X\) and \(Y\) arrays contribute no values,
since their even parts never vanish. The third array requires
\(C_a=C_b\), hence at most \(2q\) labels. Scaling by the sixteen
choices \(\pm H\) preserves each \(F\)-line. All scalar duplication
can only decrease the count. Uniformly over every line,
\[
|(A\setminus\{0\})\cap\alpha F|
\le64q\le64\sqrt2\,n^{1/2}.
\tag{16}
\]
The live request allows a fixed prefactor, so this proves
\(\kappa=1/2\), \(C=64\sqrt2\), at every \(q\ge7\). The auditor
initially flagged the older coefficient-one convention; the lead
clarified this difference in the live task. Under that older convention,
(16) by itself only absorbs its prefactor for each strict
\(\kappa<1/2\) eventually. That qualification does not weaken the
current fixed-prefactor screen.

## 6. Twisted-binomial finalist: independent full-fiber obstruction

**Audit verdict: PASS; a uniform actual-image obstruction.** The lead
and the composition specialist proposed the following sparse-frequency
argument after the spreading screen. Every step was independently
checked here without computation or inference from finite outputs.

### Thirty-three formal frequencies

Multiplying (13) by \(\Delta\) gives
\[
\Delta X_{ab}=-\omega^2\xi^a+\omega\xi^{-a}
-\xi^b+\xi^{-b}.
\tag{17}
\]
For the source pair \((X_{ab},X_{cd})\), the expression
\(\Delta^2Q\) has the following 33 formal frequencies:
\[
\Lambda=\{0\}\cup\{\pm2v_i:1\le i\le4\}
\cup\{\epsilon v_i+\epsilon'v_j:
1\le i<j\le4,\ \epsilon,\epsilon'\in\{1,-1\}\},
\tag{18}
\]
where \((v_1,v_2,v_3,v_4)=(a,b,c,d)\). The constant coefficient is
\(-8\), and every other formal coefficient is nonzero. The eight
double frequencies come from squares, the eight cross frequencies within
the two coordinate arrays have a factor two, and the sixteen cross
frequencies between the arrays come from the mixed product.

The same maximum of 33 frequencies applies to **every** target in
\(A^2\), including targets represented by different scales and coordinate
types. To check this point explicitly, the coefficient vectors of
\(\Delta X\), \(\Delta Y\), and \(\Delta(X+Y)\), at
\((+a,-a,+b,-b)\), are respectively
\[
(-\omega^2,\omega,-1,1),\qquad
(-1,1,-\omega,\omega^2),\qquad
(\omega,-\omega^2,\omega^2,-\omega).
\tag{19}
\]
All entries are nonzero, and both opposite-index products in every row
are \(-1\). For arbitrary nonzero signed scales with absolute values
\(H,G\in\{1,\ldots,8\}\), the formal norm constant is
\(-4(H^2+G^2)\ne0\). Thus there are 33 nonzero formal slots before
substituting angular indices. Colliding frequencies can only reduce the
actual support after substitution; they cannot increase it.

### Generic sources and saturation of relation blocks

Call a source label quadruple generic when all 33 values in (18) are
distinct modulo \(q/7\). Its reduced polynomial therefore has one
nonzero coefficient in each of 33 different seven-position blocks from
(11). Suppose any target in \(A^2\) has the same \(Q\)-value.
Subtracting its reduced polynomial from the source polynomial gives a
multiple of \(\Phi_q\). In each block the seven difference coefficients
are constant.

Each occupied source block must have at least one nonzero target
coefficient: otherwise a singleton nonzero source vector could not be
constant on that block. The target has at most 33 support positions in
total. Consequently it has exactly one position in each of the 33 source
blocks and none elsewhere. A singleton source and singleton target can
have constant difference only when their positions and coefficients are
identical; the other five or six zero positions force that constant to
be zero. Therefore the two reduced polynomials agree coefficient by
coefficient.

This argument accounts for cyclotomic cancellation, rather than assuming
that equality of algebraic values implies equality of formal coefficients.
It also forces all 33 target formal slots to remain distinct: otherwise
its actual support would be less than 33.

Every target angular index \(v\) therefore has its double \(2v\)
among the 32 nonzero source frequencies. Since \(q\) is odd, doubling
is invertible modulo \(q\), leaving at most 32 choices for each of four
target indices. There are at most 48 signed scalar types per coordinate
in (14). Hence the **entire** fiber of a generic source has size at most
\[
K_0=48^2\,32^4.
\tag{20}
\]
This counts target labels as an upper bound; duplicate target labels only
reduce the actual number of returned pairs. Zero coordinates and
degenerate angular labels cannot create omitted targets: they would
reduce support and are already excluded by saturation.

### Actual generic-pair population and rates

There are \(\binom{33}{2}=528\) possible collisions between the
linear forms in (18). Each difference is a nonzero integer linear form
whose coefficients have absolute value at most four, so at least one
coefficient is a unit modulo 7. Its vanishing modulo \(q/7\) has exactly
\(7q^3\) quadruple solutions modulo \(q\). The union bound gives at
most \(3696q^3\) nongeneric label quadruples.

The coordinate map \((a,b)\mapsto X_{ab}\) has fibers at most two,
as independently checked in §5. Thus generic labels give at least
\[
\frac{q^4-3696q^3}{4}
\tag{21}
\]
**distinct ordered source pairs** whose full fiber satisfies (20).
For small \(q\) this lower bound can be vacuous. For \(q\ge7392\),
(21) is at least \(q^4/8\), and (15) then gives a population of at least
\(n^2/18432\). In particular this holds along all \(q=7^h\) with
\(h\ge5\).

Dividing the actual source population by the full-fiber cap gives
\[
|Q(A,A)|\ge \frac{q^4-3696q^3}{4K_0},
\qquad
|Q(A,A)|\ge\frac{n^2}{18432K_0}\quad(q\ge7392).
\tag{22}
\]
Together with the trivial upper bound, this proves
\(|Q(A,A)|=\Theta(n^2)\) for this finalist. Every action family has
at most \(K_0\) genuine targets on the same quadratic population, so
no fixed positive near-full return-tail exponents can hold.

The actual size is \(n=\Theta(q^2)=49^{h+O(1)}\), and the actual
image size is \(\Theta(q^4)=2401^{h+O(1)}\). The input growth factor
is 49 per depth \(h\), while the obstructing population has bounded
full fibers and exponential return factor 1. The normalized image
exponent is 2; the construction supplies no positive power saving.

## 7. Charged audit disposition

| Item | Exact accounting |
|---|---|
| Number of proposals | One approved twisted-binomial finalist and one relative-norm formula rejected by its coset defect; no additional construction is introduced here. |
| Disjoint amplitude cosets | All \(8q\) twisted-binomial norms are distinct. Relative-norm labels provide at most \(8q/7\) cosets and fail that requirement. |
| Projection and parameter loss | Twisted completion uses actual values; \(q^2/2\le n\le48q^2\). Source coordinate labels have fibers at most two, charged twice in (21). Target labels are only an upper count. |
| Same set and complete target coverage | Both coordinates use (14). All 48 target scalar types and all angular labels are included in the full-fiber bound. |
| Spreading | Unique index-two subfield \(F\); line population at most \(64\sqrt2\,n^{1/2}\). The live fixed-prefactor screen passes. |
| Field costs | \([K:\mathbb Q]=6\cdot7^{h-1}\) grows. The seven-position cyclotomic relation blocks are proved at each depth; no fixed-field divisor estimate is used. |
| Coefficient and denominator costs | Multiplication by the fixed nonzero \(\Delta^2=-3\) preserves equality and fiber size. Scales 1 through 8 and all signs/types are charged explicitly. |
| Heights, discriminants, regulators, local splitting | No volume, unit-divisor, or residue-population estimate contributes to the obstruction. No unproved favorable arithmetic cost is assigned zero. |
| Exceptional sources | At most \(3696q^3\) nongeneric source labels; the separate projection loss is the factor four in (21). |
| Full fibers | Uniform cap \(K_0=48^2 32^4\) on at least \(n^2/18432\) actual sources for \(q\ge7392\), independently of action choices. |
| Rate | Twisted finalist has input factor 49 and output factor 2401 per \(h\), so actual-image exponent 2 and no positive gap. Relative-norm rejection yields no deduplicated-carrier rate theorem. |
| Evidence | Symbolic derivation and independent internal audit. No result here relies on the lead's finite scout outputs. |

**Scope.** Projective spreading does not rescue this particular
twisted-binomial carrier. The proof does not exclude arbitrary spreading
amplitude families, does not establish a universal relation between
spreading and image growth, and does not close the general ML-O1 or T03
target. The two proposals have received their scoped dispositions;
no further mutation, proof search, or experiment is proposed by this audit.

## 8. Final written-proof review

The completed [amplitude companion](amplitudes.md), FG-A1–FG-A5, and
[fiber companion](fibers.md), FG-N1 and FG-F1, were subsequently read
and checked against the independent derivations above. The field
involution formula, local Eisenstein alternative, sparse norm separation,
coupled amplitude recursion, exact scalar completion, uniform spreading,
seven-slot saturation, angular reconstruction, and both parameter-loss
counts pass. The iterated relative-norm domain is explicitly restricted
to the available tower levels. No remaining mathematical or transcription
defect was found in those two written proofs.

This final-file review does not claim a rerun of the lead's finite scout,
an audit of its output data, or validation of repository/hash metadata.
Those are separate evidence categories. This auditor's contribution
remains symbolic, with no mathematical program execution or network use.
