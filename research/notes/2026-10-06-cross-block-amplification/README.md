# Cross-Block Fiber Amplification Beyond Spreading

**6 October 2026 · T03 · version 1 · strictly offline research cycle.**
Fixed target \(Q(x,y)=x^2+xy+y^2\), on all ordered pairs of one real set.

## 1. Outcome

**PROVED:** a new growing-support factor rule meets the prescribed ML-O1
amplitude inventory and has actual scalar size \(n=\Theta(q^2)\).
Whole-product partial conjugation gives genuine growing encoded fibers.

**FAILED IN STATED SCOPE:** independent factor switches in the two scalar
coordinates cannot give a near-full return certificate. Even allowing
every scalar representation, every norm-equal switched target, sign/swap,
all equal-norm edges inside the encoded union, and arbitrary iterations,
at least \(n^2/2\) sources eventually have at most four certified targets.
This is **not** an upper bound on their full \(Q\)-fibers.

The second rule, quadratic-phase convolution, has an exact shift identity
but collapses its \(8q\) amplitude labels into exactly eight cosets.
It fails the prescribed inventory for every \(q>1\).

**OPEN:** the unrestricted full-fiber tails and actual images of these new
scalar completions. No positive \(\varepsilon,\delta\), or \(c\), is proved.
Neither proposed amplification mechanism survives. No geometric proxy,
rigidity classification, repair, or replacement conjecture is adopted.

## 2. Source boundary and companion map

The controlling predecessor is [XB-O1 → Cross-Block Fiber Growth](../2026-10-06-fiber-growth/README.md),
with [amplitudes](../2026-10-06-fiber-growth/amplitudes.md),
[full-fiber proof](../2026-10-06-fiber-growth/fibers.md), and
[audit](../2026-10-06-fiber-growth/audit.md). Its two rules and FG-O1
are frozen. Its 33-frequency obstruction is not generalized here.
Only its proved cyclotomic field and coefficient-relation facts are reused.

| Companion | Contents |
|---|---|
| [amplitudes.md](amplitudes.md) | AMP-A1–A4: new product recursion, disjoint cosets, scalar growth, encoded norms and exact switch identity |
| [returns.md](returns.md) | AMP-R1–R3: all independent coordinate switches, full cross terms, phase count, and iterative certificate obstruction |
| [identities.md](identities.md) | AMP-G1: quadratic-phase rule, exact shifts, duplicate labels and actual scalar bounds |
| [audit.md](audit.md) | Independent proof audit, DC-M1 scope and complete written reviews |
| [ledger.md](ledger.md) | Input, return, arithmetic and signed-rate accounting for both rules |
| [verification.md](verification.md) | Zero-program budget, exact histogram formulas, audit and repository checks |
| [state.json](state.json) | Machine-readable final statuses and claim records |
| [manifest.json](manifest.json) | Proof, source and local-record file identities |

The prescribed model is \(r=k-1,\ q=7^r,\ m=6q,\ t=8q\),
\(K=\mathbb Q(\zeta_m)\). Let \(\xi=e^{2\pi i/q}\),
\(\omega=e^{2\pi i/3}\), and \(\Delta=1+2\omega\). For every complex
\(z\in K\), its real coordinates are
\[
X(z)=\frac{\omega\bar z-\omega^2z}{\Delta},\qquad
Y(z)=\frac{\bar z-z}{\Delta},\qquad z=X(z)-\omega Y(z).
\]
For an orbit union \(Z\), use the actual deduplicated completion
\(A=X(Z)\cup Y(Z)\), and \(\Gamma=\{(X(z),Y(z)):z\in Z\}\).

The inspected [DC-M1 proof](../2026-09-21-dense-cartesianization/matrix-product.md),
§§1–2, gives
\[
|\Gamma|\le\left\lfloor(3n^2+1)/4\right\rfloor
\]
because \(\omega\Gamma=\Gamma\) under the genuine norm action.
For a valid inventory \(|\Gamma|=48q^2\), this forces \(n\ge8q\).
It is only an encoding bound; unencoded pairs may have many actual collisions.

## 3. Finalist 1: balanced factor products

Choose the fixed digit alphabet \(I=\{-3,-2,-1,0,1,2,3\}\) and define
\[
\boxed{c_{h,\mathbf i}
=h\prod_{\ell=0}^{r-1}(2-\xi^{i_\ell7^\ell}),
\qquad 1\le h\le8,\quad \mathbf i\in I^r.}
\tag{1}
\]
The recursion is
\(c^{(r+1)}_{h,(a,\mathbf i)}
=(2-\xi_{r+1}^{a})c^{(r)}_{h,\mathbf i}\).
Every factor is nonzero. Balanced digits and the exact seven-slot relation
prove that all \(8q\) cosets \(c_{h,\mathbf i}\mu_m\) are disjoint.
This is not a complete relative norm or an independently tagged construction.
Its coefficient support grows as \(2^s\), where \(s\) is the number of
nonzero digits.

Let \(Z=\bigcup c_{h,\mathbf i}\mu_m\). For the actual completion:
\[
\boxed{8q^2\le n\le48q^2,\qquad |\Gamma|=48q^2,\qquad
n=49^{r+o(r)}.}
\tag{2}
\]
The lower bound uses injectivity of \(X\) on \(\mathbb Q(\xi)\), because
\(X(v)=0\) would imply \(\bar v=\omega v\), while
\(\omega\notin\mathbb Q(\xi)\). It does not assume projection injectivity
on the whole orbit union.

### Exact whole-product identity

Negating the digits in \(S\) gives \(\mathbf i^S\), and
\[
u_{\mathbf i,S}=
\prod_{\ell\in S}
\frac{2-\xi^{-i_\ell7^\ell}}{2-\xi^{i_\ell7^\ell}},
\qquad
u_{\mathbf i,S}c_{h,\mathbf i}=c_{h,\mathbf i^S},\qquad
u_{\mathbf i,S}\bar u_{\mathbf i,S}=1.
\tag{3}
\]
Nonempty switches of nonzero digits produce multipliers outside \(\mu_m\).
They give distinct genuine targets. Encoded norm classes are exactly fixed
\(h\) and fixed \((|i_0|,\ldots,|i_{r-1}|)\): there are \(8\cdot4^r\)
values, with encoded fiber \(6q\,2^s\) for a class having \(s\) nonzero digits.

**Meaning:** multiplicative amplification works on actual encoded pairs.
But those pairs number only \(\Theta(n)\); generic independently assembled
coordinates require another proof.

### Generic cross-block assembly and exact norm test

For \(p=(X(z),Y(w))\), the whole source is \(P=X(z)-\omega Y(w)\).
Independent switches give a candidate target
\[
p'=(X(uz),Y(vw))\in A^2.
\tag{4}
\]
Membership is proved for all allowed representations. Equality of norms
must still be tested. Even the common-switch formula has the exact defect
\[
uP-\bigl(X(uz)-\omega Y(uw)\bigr)
=\frac{\omega(u-u^{-1})(\bar z-\bar w)}{\Delta}.
\tag{5}
\]
We do not infer unequal norms from this defect. Instead fix \(z,u,v\)
and write \(w=d\nu\), \(\nu\in\mu_m\). In the full expansion
\[
Q(x',y')-Q(x,y)
=(x'^2-x^2)+(x'y'-xy)+(y'^2-y^2),
\]
the coefficient of \(\nu^2\) is \(d^2(v^2-1)/\Delta^2\).
For \(v\ne\pm1\), a nonzero quartic therefore leaves at most four phases.
For \(v=\tau=\pm1\),
\[
Q(x',\tau y)-Q(x,y)
=(x'-\tau x)(x'+\tau x+\tau y);
\]
outside the trivial target \(\tau p\), at most two phases remain.

There are \((8q)^2\) amplitude pairs, at most \(4^r\) independent switch
pairs and \(6q\) first phases. Consequently the actual source set \(D\)
gaining any switched equal-norm target beyond \(\pm p\) satisfies
\[
|D|\le1536q^3\,4^r.
\tag{6}
\]
All scalar representations and incidental norm equalities of (4) are
included. This is not just a failure of the multiplier asserted in (5).

### Iteration and final certificate tail

The scalar replacement relation is the same in both coordinate charts,
reversible and sign-equivariant. Thus \(D\) and \(\Gamma\) are
sign/swap invariant. Outside \(D\cup\Gamma\), no sequence of independent
switches, sign/swap or equal-norm encoded edges escapes the four-point
sign/swap orbit. For this precisely defined certificate,
\[
\boxed{\#\{p:R_{\rm cert}(p)\le4\}
\ge n^2-1536q^3\,4^r-48q^2,}
\tag{7}
\]
\[
\frac{|D\cup\Gamma|}{n^2}
\le24(4/7)^r+\frac{3}{4q^2}=o(1).
\tag{8}
\]
For \(r\ge8\), at least \(n^2/2\) sources have at most four certified
targets. Hence every fixed positive \(\varepsilon,\delta\) fails for this
certificate. **The full-fiber tail remains OPEN**, since
\(R_{\rm cert}\le F_A\), not conversely. Arbitrary additional phase
returns at unencoded sources are outside the theorem.

## 4. Finalist 2: quadratic-phase convolution

Define
\[
G_j=\sum_{a\bmod q}\xi^{a^2+ja},\qquad c_{h,j}=hG_j.
\tag{9}
\]
Completion of the square gives
\[
G_j=\xi^{-j^2/4}G_0,\qquad
|G_0|^2=\sum_{u,v\bmod q}\xi^{uv}=q.
\tag{10}
\]
Fractions in exponents are modular inverses. The exact target multiplier
\(\xi^{-(2js+s^2)/4}\) sends \(hG_j\nu\) to \(hG_{j+s}\nu\).
It preserves the whole norm and has target membership on the encoded union.

However, (10) places all \(j\) for each \(h\) in the same \(\mu_m\)-coset.
There are exactly eight cosets and \(48q\) actual encoded points, with
\(q\) duplicate paired labels per point. The deduplicated completion has
\[
3q\le n\le48q.
\]
Its \(48q\) certified rich sources each have \(6q\) root-rotation targets;
the remaining \(n^2-48q\) sources are uncovered by this membership argument,
not proved to have small full fibers. The required coset gate already fails.

## 5. Full support, computation and stopping decision

The same-set implication is unchanged:
\[
F_A(p)\ge R\text{ outside }E
\quad\Longrightarrow\quad |Q(A,A)|\le n^2/R+|E|.
\]
An output meeting the good set consumes at least \(R\) pairs; all other
outputs are charged to \(E\). Neither rule provides its required premise.
No positive full-fiber \(\varepsilon,\delta\), or image exponent \(c\), is
established. Both constructions already use the same scalar set; no
rectangular mismatch exponent is involved.

Both proposed mechanisms failed analytic gates before scouting. **Zero
charged evaluations and zero research-program CPU seconds** were used,
including validation. No finite full-\(Q\) histogram was computed or inferred.
The exact encoded histogram is supplied symbolically in verification.md,
clearly separated from full fibers. All three specialist contributions
and the lead's accepted proofs were checked symbolically.

The stop is by two rigorously scoped mechanism failures, not budget exhaustion.
Historical sources are preserved and nothing is committed. The product carrier
is still a valid explicit family with unknown unrestricted full fibers;
it is not a surviving proved amplification construction. **No mechanism
survives this cycle, and no replacement lemma or proxy task is adopted.**
The general T03, ML-O1, DC-O1, ARG/TCRC and RC15/4 targets remain OPEN.
