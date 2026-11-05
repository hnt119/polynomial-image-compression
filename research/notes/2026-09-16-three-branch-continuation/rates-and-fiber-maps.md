# Rates with input losses, and one nonlinear extension of the slice identities

2026-09-16, v1. T01, \(P(x,y)=(x-y)^3+x+y\).
New internal proofs for the explicitly authorized offline continuation cycle.
No computation, external theorem, or arithmetic tower is used in this note.

## 1. TC-R1 — almost tripling needs a small correction

If the growth factor approaches 3, the number of inputs has exponential rate
3. It need not stay within a fixed constant factor of \(3^m\). Small losses
at each stage can accumulate to a polynomial factor. This distinction does
not destroy a strict power-saving argument, but it matters when stating it.

**PROVED.** If positive numbers \(n_m\) satisfy
\(n_{m+1}/n_m\to\lambda>1\), then
\[
\log n_m=m\log\lambda+o(m),\qquad n_m=\lambda^{m+o(m)}.
\tag{R1}
\]
The stronger conclusion \(n_m\asymp\lambda^m\) does not follow alone.

**Proof.** Take logarithms and sum the successive ratios. Their logarithms
tend to \(\log\lambda\), so their average does too. For the limitation,
take \(n_m=\lfloor\lambda^m/(m+1)\rfloor\) at sufficiently large \(m\).
Its successive ratio tends to \(\lambda\), while
\(n_m/\lambda^m\to0\). ∎

This corrects the rate shorthand in the active request; it changes no
construction or previous proved theorem. The earlier cycle's TB-R1
explicitly *assumed* \(n_m\asymp3^m\), so that implication remains valid.

## 2. TC-R2 — the correct gate survives these losses

The useful comparison is the image growth against the **square of the
actual input growth**. A strict gap absorbs both small input losses and
a smaller-order output error. There is no need to assume an exact formula
for the input size.

**PROVED implication.** Suppose \(n_m\to\infty\),
\[
\liminf_m\frac{n_{m+1}}{n_m}\ge\lambda>1,
\qquad
s_{m+1}\le\rho s_m+C n_m^{2-\delta}
\tag{R2}
\]
eventually, with fixed \(C<\infty\), \(\delta>0\),
\(1\le\rho<\lambda^2\). Then every fixed
\[
0<c<\min\{2-\log_\lambda\rho,\delta\}
\tag{R3}
\]
satisfies \(s_m\le n_m^{2-c}\) eventually.

**Proof.** Choose a number \(p\) strictly between
\(\max\{\log_\lambda\rho,2-\delta\}\) and \(2-c\), with \(p>0\).
There is \(1<\lambda_0<\lambda\) such that \(\rho<\lambda_0^p\).
Eventually \(n_{m+1}\ge\lambda_0n_m\). Choose a fixed constant \(D\)
large enough to cover the starting value \(s_m\le Dn_m^p\). Since
\(p>2-\delta\), increase the starting index and \(D\), if necessary, so
that
\[
C n_m^{2-\delta-p}\le D(\lambda_0^p-\rho)
\]
at every later index. Induction gives
\[
s_{m+1}\le D\rho n_m^p+C n_m^{2-\delta}
\le D\lambda_0^pn_m^p\le Dn_{m+1}^p.
\]
Finally \(p<2-c\) absorbs \(D\) as \(n_m\to\infty\). ∎

The hypothesis holds if the actual input ratio tends to \(\lambda\), or
if \(n_{m+1}\ge\lambda n_m-O(n_m^{1-\eta})\), \(\eta>0\), with
\(n_m\to\infty\). If \(\rho<1\), replacing it by 1 gives the same
usable strict exponent range below \(\min\{2,\delta\}\); inconsistent
rates are excluded in any real construction by \(s_m\ge n_m\).

For \(\lambda=3,\rho=8\), the no-error limiting exponent is
\(2-\log_3 8\), approximately \(0.10721\). For actual input growth 2,
the same \(\rho=8\) fails badly: the threshold is then 4.

**What this does not prove.** No candidate acquires a valid uniform \(\rho\)
from one small numerical ratio. This is a proved implication, whose
application remains CONDITIONAL until all hypotheses are supplied.

## 3. TC-R3 — a useful exact finite diagnostic

The finite rate test can be understood without logarithms. It says that
the fraction of possible ordered pairs appearing as distinct outputs
decreases at that step.

**PROVED.** Define \(d_m=s_m/n_m^2\),
\(\lambda_m=n_{m+1}/n_m\), and \(\rho_m=s_{m+1}/s_m\). Then
\[
\frac{\rho_m}{\lambda_m^2}=\frac{d_{m+1}}{d_m},\qquad
\prod_{j<m}\frac{\rho_j}{\lambda_j^2}=\frac{d_m}{d_0}.
\tag{R4}
\]
These identities follow by canceling the definitions.

Thus a few ratios below 1 show only finite improvement. A uniform factor
strictly below 1 at all large levels, together with exponential input
growth, is a different statement. Conversely, a family with
\(d_m\to1\) cannot have a positive power saving, regardless of early gains.

## 4. TC-Q1 — one nonlinear map preserves every cubic output

The original gadget joins a few pairs of difference slices. The natural
way to extend that idea is to move **every** difference by the same amount,
while adjusting the sum so the cubic value stays fixed. The adjustment is
quadratic in the difference. It therefore depends on both inputs, and is
not an allowed one-variable branch by itself.

For a pair \((x,y)\), write \(u=x-y\), \(s=x+y\). Fix a real \(\tau\)
and define
\[
H_\tau(u)=3\tau u^2+3\tau^2u+\tau^3,
\qquad
T_\tau(x,y)=\left(x+\frac{\tau-H_\tau(u)}2,
y-\frac{\tau+H_\tau(u)}2\right).
\tag{Q1}
\]

**PROVED.** For all real pairs and parameters,
\[
P(T_\tau(x,y))=P(x,y),\qquad
T_\sigma\circ T_\tau=T_{\sigma+\tau},\qquad
T_\tau^{-1}=T_{-\tau}.
\tag{Q2}
\]

**Proof.** The new difference is \(u+\tau\), and the new sum is
\(s+u^3-(u+\tau)^3\). Adding their cubic and linear contributions proves
the first identity. Applying two such changes adds their difference
increments and makes the intermediate cubic terms cancel; this proves
the composition and inverse identities. ∎

For example, \(\tau=-1\) sends the pair \((t+1/3,t)\), whose difference
is \(1/3\), to \((t,t+2/3)\), whose difference is \(-2/3\).
Thus this family contains the gadget's translated-slice identity as one
special case. It is the one nonlinear extension considered after the
affine identity obstruction; no unrelated nonlinear search is launched.

## 5. TC-Q2 — the Cartesian input requirement is still missing

Although this map preserves outputs, it does not preserve a whole finite
Cartesian square. Taking all coordinates visited by a few such motions
introduces new cross-pairs, whose outputs must also be counted.

**PROVED.** If \(A\) is a nonempty finite real set and \(\tau\ne0\), then
\(T_\tau(A^2)\not\subseteq A^2\).

**Proof.** The differences in \(A^2\) form a nonempty finite set. The map
adds \(\tau\) to every difference. If \(\tau>0\), a pair attaining the
largest difference leaves that difference set; if \(\tau<0\), use the
smallest difference. ∎

Partial returns to \(A^2\) are not excluded. Exactly which ones occur is
given by
\[
u+\tau\in A-A,\qquad
a\in A_u,\qquad
a+\frac{u^3+u-(u+\tau)^3-(u+\tau)}2\in A_{u+\tau},
\tag{Q3}
\]
where the pair is \((a+u,a)\). This follows by substituting in (Q1).
It is the original collision equation with its full endpoint restrictions.

**What this does not prove.** There is no supplied carrier with enough such
returns to control the complete support. Exact output preservation on the
plane is not a same-set construction. No new positive conjecture or
arithmetic amplification follows from (Q2).

## 6. Claim provenance

All claims TC-R1–R3 and TC-Q1–Q2 are T01 / three-branch continuation,
fixed plus-sign cubic, dated v1 2026-09-16, PROVED internally by the
displayed elementary arguments. R2 depends only on its explicit numerical
hypotheses; Q2 depends on Q1 and finiteness of the common input set.
No external result, missing source, finite experiment or asymptotic guess
is used as proof. Independent internal audit is recorded in the main
cycle verification file. Actual positive recurrences and useful partial
Cartesian returns remain OPEN outside these implications and obstructions.
