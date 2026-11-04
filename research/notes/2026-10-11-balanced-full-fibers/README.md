# Balanced Factor Carrier Full Fibers and Coupled Phase Returns

**11 October 2026 · T03 · version 1 · strictly offline.**
Fixed polynomial \(Q(x,y)=x^2+xy+y^2\); one unchanged balanced-factor
carrier, one new coupled mechanism, and complete exact audits at depths
\(r=0,1\). Historical files are preserved; no commit or external search.

## 1. Result and exact scope

**EXPERIMENTAL — exhaustive and exact:** at \(r=1\), the deduplicated set
has \(n=1079\), full image size \(286664\), and pair-weighted median full
fiber 4. Exactly \(1135967\) of its \(1164241\) ordered pairs have no
targets beyond their own sign/swap orbit. This is a finite observation,
not a bound at increasing depth.

**PROVED / FAILED IN STATED SCOPE:** exchanging the two source phases,
with independent factor switches and correction units in \(\mu_6\),
does not give a near-full growing return tail. Even adjoining all frozen
certificate moves and taking arbitrary finite compositions leaves at most
four certified targets outside a set of size
\[
56832q^3 4^r+48q^2=o(n^2).
\tag{1}
\]
The restriction on the correction units is part of this theorem.
Arbitrary source-dependent corrective phases in \(\mu_{6q}\) are not
covered by its failure statement.

**OPEN:** unrestricted full-fiber asymptotics and the actual image rate of
this carrier. No positive \(\varepsilon,\delta\), or image-saving
exponent \(c\), follows. The carrier is **not retired**. The cycle stops
on the decisive failure of its one proposed coupled mechanism.

## 2. Sources and companion files

The frozen starting point is the [6 October amplification report](../2026-10-06-cross-block-amplification/README.md),
its [amplitude proofs](../2026-10-06-cross-block-amplification/amplitudes.md),
[AMP-R1–R3](../2026-10-06-cross-block-amplification/returns.md),
[audit](../2026-10-06-cross-block-amplification/audit.md),
[rate ledger](../2026-10-06-cross-block-amplification/ledger.md), and
[verification record](../2026-10-06-cross-block-amplification/verification.md).
The quadratic-phase inventory failure is frozen. No former 33-frequency
obstruction is extended or used. The separate adaptive RC15/4 problem
remains OPEN and is not this cycle's assignment.

| Companion | Content |
|---|---|
| [algebra.md](algebra.md) | BFF-A1–A4: exact completed scalar set, sharper size bounds, full-fiber equality key, symmetry weights |
| [coupled.md](coupled.md) | BFF-P1/P2: complete phase-transposed norm equation, degeneracy, source count and iterative obstruction |
| [audit.md](audit.md) | Independent internal written-proof and code/data audit; precise inspection boundaries |
| [data.json](data.json) | Both complete full-fiber histograms, medians, tails, baseline comparisons and distribution hashes |
| [ledger.md](ledger.md) | Construction, arithmetic, coverage and signed-rate ledger |
| [verification.md](verification.md) | Predetermined cases, counters, actual commands, validation, file preservation and checks |
| [state.json](state.json) | Final claim/status record and the sole remaining obligation |
| [manifest.json](manifest.json) | Companion, source and local reproducibility identities |

## 3. The unchanged carrier and actual scalar growth

Fix \(r\ge0\), \(q=7^r\), \(m=6q\), \(\xi=e^{2\pi i/q}\),
\(\omega=e^{2\pi i/3}\), and \(\Delta=1+2\omega\), so
\(\Delta^2=-3\). The prescribed amplitudes remain
\[
c_{h,\mathbf i}=h\prod_{\ell=0}^{r-1}(2-\xi^{i_\ell7^\ell}),
\qquad 1\le h\le8,\quad \mathbf i\in\{-3,\ldots,3\}^r.
\tag{2}
\]
Their \(8q\) cosets modulo \(\mu_m\) are pairwise disjoint by the
inherited AMP-A1. Put \(Z=\bigcup c_{h,\mathbf i}\mu_m\), and use
\[
X(z)=\frac{\omega\bar z-\omega^2z}{\Delta},\qquad
Y(z)=\frac{\bar z-z}{\Delta},\qquad z=X(z)-\omega Y(z).
\tag{3}
\]
Then \(A=X(Z)=Y(Z)\) is the actual scalar completion and
\(\Gamma=\{(X(z),Y(z)):z\in Z\}\) has \(48q^2\) points.

The new exact description is useful because it retains all scalar
identifications. Set \(H=\mathbb Q(\xi)\) and
\[
B=\{c_{h,\mathbf i}\xi^a:a\bmod q\},\quad
D=\{\bar b-b:b\in B\},\quad
V=B\mathbin{\dot\cup}(-B)\mathbin{\dot\cup}D.
\tag{4}
\]
**PROVED — BFF-A1:** \(X:V\to A\) is a bijection, and
\[
\boxed{n=16q^2+|D|,\qquad16q^2+1\le n\le24q^2-7.}
\tag{5}
\]
Indeed \(\bar B=B\), \(B\cap(-B)=\varnothing\), and every element
of \(D\) is purely imaginary, whereas no element of \(B\cup(-B)\)
is. The identities \(X(\bar b)=X(b)+Y(b)\) and
\(Y(b)=X(\bar b-b)\) give the completion. Injectivity follows from
\(\omega\notin H\): \(X(v)=0\) would force \(\bar v=\omega v\).
Exactly eight elements of \(B\) are real, namely \(1,\ldots,8\);
they all map to zero in \(D\), giving its upper bound.
Thus \(n=49^{r+o(r)}\) is proved after deduplication.

## 4. Complete small full-fiber audit

Define the unrestricted fiber and each source's baseline orbit by
\[
F_A(p)=\#\{s\in A^2:Q(s)=Q(p)\},\qquad
\mathcal S(x,y)=\{(x,y),(y,x),(-x,-y),(-y,-x)\}.
\tag{6}
\]
All statistics below use ordered source-pair weights. The two predeclared
cases were completely enumerated; no sample or deeper sweep is included.

| Depth \(r\) | Actual \(n\) | Full image | Median \(F_A\) | Pairs with \(F_A<n^{1/4}\) | Pairs with \(F_A>\lvert\mathcal S(p)\rvert\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 17 | 44 | 12 | 9 | 216 |
| 1 | 1079 | 286664 | 4 | 1135967 | 28274 |

**EXPERIMENTAL:** the maximum full fibers are 18 and 84, respectively.
The complete pair-weighted histograms, also in data.json, are
\[
\begin{aligned}
r=0:\quad &(1:1),(2:8),(4:64),(6:66),(12:132),(18:18);\\
r=1:\quad &(1:1),(2:522),(4:1135444),(6:4392),(8:552),\\
&(12:19500),(14:56),(16:96),(18:1314),\\
&(42:294),(54:54),(84:2016).
\end{aligned}
\tag{7}
\]
Here \((f:h)\) means \(h\) ordered sources have full fiber size \(f\).
Dividing each mass by its fiber size gives the output histogram, not
another pair histogram.

The scout represents \(3A\) by integer coefficient vectors modulo
\(\Phi_{6q}\), so its output keys are exactly \(9Q(A,A)\). Multiplying
by 9 changes neither image cardinalities nor fibers. Sign/swap symmetry
reduces the work to \((n+1)^2/4\) representatives with weights 1, 2 or 4.
The strict threshold is checked by the integer test \(f^4<n\).
The second complete calculation uses
\((a-\omega b)(a-\omega^2b)\), a different representative traversal,
and the same exact field reduction. It matches every output and its
multiplicity. The seed additionally matches a raw integer-square oracle.

### Extra collisions exist, but growing coverage is not established

For example \(Q(1,2)=Q(2,-3)=7\), and all these coordinates belong
to the carrier at every depth through its integer seed. At \(r=0\),
the two pairs are unencoded because encoded norms are integer squares;
there are no factor masks, and the old certificate connects only their
separate sign/swap orbits. Thus full cross-block collisions really can
escape the closed certificate. This example supplies only a fixed number
of targets and no asymptotic return exponent.

## 5. One coupled mechanism and its failure

Take any representations
\(p=(X(c\alpha),Y(d\beta))\), with bare amplitudes \(c,d\) and
\(\alpha,\beta\in\mu_m\). Independently switch their factor masks
to obtain \(c',d'\). The one proposed target family is
\[
p'=\bigl(X(\kappa c'\beta),Y(\lambda d'\alpha)\bigr),
\qquad\kappa,\lambda\in\mu_6.
\tag{8}
\]
It exchanges the source phases, so its rule is outside the predecessor's
fixed-phase switch definition. Both target coordinates belong to \(A\).
Only targets satisfying exact \(Q(p')=Q(p)\) are retained.

**PROVED — BFF-P1:** for fixed amplitudes, switches, corrections and first
phase, the whole norm defect is a Laurent polynomial in \(\beta\) with
powers \(-2,\ldots,2\). Its leading coefficient is
\[
\frac{\omega\kappa^2(c')^2-d^2}{\Delta^2}.
\tag{9}
\]
If nonzero, there are at most four admissible second phases. If it vanishes,
disjoint amplitude cosets and \(\omega\notin H\) force
\(\kappa=\tau\omega\), \(c'=d\), \(\tau=\pm1\). Writing
\(t=Y(\lambda d'\alpha)\), the **whole-scalar** identity becomes
\[
Q(\tau y,t)-Q(x,y)=(t-\tau x)(t+\tau x+\tau y).
\tag{10}
\]
Its all-phase branch gives only \(\tau(y,x)\). Otherwise at most two
phases survive, and the resulting target is \(\tau(y,-x-y)\), an
ordinary norm-one rotation where membership has been established.
No identity with growing generic target multiplicity was found.

**PROVED — BFF-P2:** let \(D_{\rm tr}\) contain sources gaining a target
outside \(\mathcal S(p)\) from (8). Counting all representations gives
\[
|D_{\rm tr}|\le(8q)^2 4^r(6q)36\cdot4=55296q^3 4^r.
\tag{11}
\]
The relation is reversible and sign/swap compatible. Adjoining the old
independent switches, sign/swap and every equal-norm edge within \(\Gamma\)
still gives, under arbitrary finite iteration,
\[
R_*(p)\le4\quad\text{outside }D_{\rm tr}\cup D_{\rm old}\cup\Gamma.
\tag{12}
\]
Here \(|D_{\rm old}|\le1536q^3 4^r\). Using (5), the union occupies
at most the fraction
\[
222(4/7)^r+\frac{3}{16q^2}\longrightarrow0.
\tag{13}
\]
Thus every fixed positive exponent tail fails for this **specified
certificate**. Since \(R_*(p)\le F_A(p)\), a bound above on \(R_*\)
is not a bound above on \(F_A\). No actual-image lower bound follows.

## 6. Full support, rates, and stop

The accepted same-set lemma remains
\[
F_A(p)\ge R\text{ on }A^2\setminus E
\ \Longrightarrow\ |Q(A,A)|\le n^2/R+|E|.
\tag{14}
\]
An output meeting the good set has at least \(R\) preimages; every other
output is charged to an exceptional pair. Neither the finite histograms
nor (12) supplies the premise with \(R=n^\varepsilon\) and
\(|E|=O(n^{2-\delta})\). **No \(\varepsilon,\delta>0\) or explicit
\(c>0\) is proved.** No rectangular mismatch exponent is involved.

The full-fiber audit used **598542 exact evaluation/check charges and
22.089862 CPU seconds**. Required existing repository regressions added
373301 conservative source-line charges and 0.907295 CPU seconds, for a
shared total of **971843 charged units and 22.997157 CPU seconds**.
The total stays within the 2000000/600 caps; the regression allowance was
transferred from unused discovery budget before execution. The 17
seed-comparison charges omitted by the first counter implementation were
explicitly restored; their CPU time was already included. No rerun was hidden.

The lead checked the accepted symbolic proofs and the computation design.
An independent internal specialist checked the completed algebra and coupled
proofs, exact weights, program logic, outputs and provenance. This was not
external peer review. Mathematical search stopped after BFF-P2; no mutation,
second mechanism, larger enumeration, or new amplitude rule was attempted.
T03, this carrier's actual image, and the separate RC15/4 problem remain OPEN.

## 7. One remaining obligation BFF-O1

This is a direct full-fiber lemma for the unchanged carrier, not a
spreading, energy, or selected-action substitute. It is **OPEN**, and no
claim is made that it must hold.

For \(v,w\in H\), put
\[
M(v,w)=2vw+v\bar w+\bar v w-\bar v\bar w,\qquad
\mathcal K(v,w)=M(v,v)+M(v,w)+M(w,w).
\tag{15}
\]
BFF-A2 proves \(X(\mathcal K(v,w))=3Q(X(v),X(w))\), so the complete
fiber of \((X(v),X(w))\) is exactly the set of all \((s,t)\in V^2\)
with \(\mathcal K(s,t)=\mathcal K(v,w)\).

**BFF-O1 — prove or refute the following statement.** There exist fixed
\(C\ge0,r_0\) such that for every integer \(r\ge r_0\), at least
\(32q^4\) ordered sources \((v,w)\in B^2\) have at most
\((r+1)^C\) solutions \((s,t)\in V^2\) to
\[
\boxed{\mathcal K(s,t)=\mathcal K(v,w).}
\tag{16}
\]
The targets must range over **all** \(V^2\). If proved, the statement
would yield
\[
|Q(A,A)|\ge\frac{32q^4}{(r+1)^C}
\ge\frac{n^2}{18(r+1)^C}=n^{2-o(1)},
\tag{17}
\]
retiring this carrier without requiring an exact constant-fiber
classification. The quantifier is every sufficiently large depth;
an obstruction on only a subsequence would not eliminate a different
successful subsequence. This is the sole next obligation recorded here.
