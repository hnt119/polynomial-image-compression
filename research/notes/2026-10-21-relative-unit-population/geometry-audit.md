# Relative-unit population: geometry and independent rate audit

21 October 2026 · T03 · fixed \(Q(x,y)=x^2+xy+y^2\) · version 2.

**PROVED:** the exact weight comparisons and the discrete upper bound
below. **INDEPENDENTLY AUDITED — PASS:** the complete written proof
MSU-A1–A3 in [arithmetic.md](arithmetic.md). It proves the commissioned
MS-O1 population gate at one explicit fixed radius, at every tower level.
**OPEN:** a useful lower tail of actual returns and a power saving for the
entire quadratic image.

This is an internal symbolic audit of the unchanged mixed-signature
construction. It introduces no field, carrier, action family, or window
mutation. The specialist executed zero mathematical programs, used zero
mathematical evaluations and zero research-program CPU, and made no
network request. Historical files were not edited. No external review or
novelty claim is made.

## 1. Objects and dependencies

Use the exact fields, order and logarithmic normalization of
[20 October MS-F1–F6](../2026-10-20-mixed-signature/field-units.md):
\[
 [K:\mathbb Q]=3d,\quad \operatorname{sig}(K)=(d,d),\quad
 E=K(\omega),\quad R=\mathcal O_K[\omega],\quad
 \operatorname{rd}(K)\le D_*.
\]
Write \(\mathcal G=\{u\in R^\times:N_{E/K}(u)=1\}\),
\(\ell(u)\in\mathbb R^d\) for the relative logarithms, and
\(\Lambda=\ell(\mathcal G)\). Its ordinary Euclidean covolume is
\(\mathcal R_R\), and each log vector has exactly \(w_R\) unit preimages.
The inherited inequalities are \(6\le w_R\le8d^2\).

The scalar set is the real image of
\[
 C(T)=\mathcal O_K\cap W_T,\qquad
 W_T=[-T,T]^d\times\{z\in\mathbb C:|z|\le T\}^{d}.
\]
The real embedding is injective. Thus \(n=|C(T)|\) is the actual input
size, with no projection fibers. From
[MS-C1](../2026-10-20-mixed-signature/carrier-rate.md#2-ms-c1--finite-injective-carrier-with-exponential-growth),
\[
 \left(\frac{(\pi/2)T^3}{D_*^{3/2}}\right)^d
 \le n\le(2T+1)^{3d}.
 \tag{1}
\]
All unit actions are the global integral matrices
\[
 M_u=\begin{pmatrix}a&b\\-b&a-b\end{pmatrix},
 \qquad u=a+b\omega,\qquad Q(M_up)=Q(p).
 \tag{2}
\]
They are not independent choices at the embeddings.

By [MS-W1](../2026-10-20-mixed-signature/window-returns.md#2-ms-w1--exact-action-and-the-complex-return-domain),
every nonzero-pair return by an order unit lies in the finite exhaustive
inventory
\[
 \mathcal U(T)=\{u\in\mathcal G:H(u):=\|\ell(u)\|_1\le dL(T)\},
 \qquad L(T)=\tfrac12\log(48T^6).
 \tag{3}
\]
The height is exactly \(h(u)=H(u)/(3d)\). The cutoff bounds this height
independently of \(d\), while its direct house bound is
\(\exp(dL(T))\). These are different controls.

The prior local bidisk calculation, MS-W2, supplies the continuous
overlap upper bound
\[
 \frac{\operatorname{vol}(W_T^2\cap M_u^{-1}W_T^2)}
      {\operatorname{vol}(W_T^2)}
 \le w(u):=\prod_{i=1}^d\min\{1,4e^{-2|\ell_i(u)|}\}.
 \tag{4}
\]
Define \(Z(T)=\sum_{u\in\mathcal U(T)}w(u)\). This is a sum of upper
bounds for continuous overlaps, not a count of discrete returns.

## 2. MSU-G1 — exact weight and height comparisons

Put \(b=\log2\) and
\[
 E(u)=\sum_{i=1}^d(|\ell_i(u)|-b)_+.
\]
Then, identically,
\[
 w(u)=e^{-2E(u)},\qquad
 (H(u)-db)_+\le E(u)\le H(u),
\]
and therefore
\[
 \boxed{e^{-2H(u)}\le w(u)\le
             \min\{1,4^d e^{-2H(u)}\}.}
 \tag{5}
\]
These follow by applying
\((s-b)_+=\max(s-b,0)\) in each coordinate and summing.
In particular, units of height at least \(h_0\) have
\[
 w(u)\le \exp\{-2d(3h_0-\log2)_+\}.
 \tag{6}
\]
This is an individual upper bound; the number of units in such a shell
remains a separate quantity.

For the finite inventory (3),
\[
 w_R\le Z(T)\le|\mathcal U(T)|,\qquad
 Z(T)\ge e^{-2dL(T)}|\mathcal U(T)|.
 \tag{7}
\]
The first lower bound is supplied by the torsion kernel. If
\(N(a)=|\{u\in\mathcal U(T):H(u)\le a\}|\), then for
\(0\le a\le dL(T)\),
\[
 Z(T)\le N(a)+\min\{1,4^de^{-2a}\}
                      (|\mathcal U(T)|-N(a)).
 \tag{8}
\]
Thus a population count alone gives no distribution among the weights.
An exact distribution formula, with
\(N_E(s)=|\{u\in\mathcal U(T):E(u)\le s\}|\), is
\[
 Z(T)=e^{-2dL(T)}|\mathcal U(T)|
       +2\int_0^{dL(T)}e^{-2s}N_E(s)\,ds.
 \tag{9}
\]
Indeed integrate \(2e^{-2s}\) from \(E(u)\) to \(dL(T)\) and sum
over the finite inventory.

### What the newly proved population estimate supplies

The arithmetic proof gives \(\mathcal R_R\le K_R^d\) and, for any
fixed admissible \(T\),
\[
 \liminf_{j\to\infty}\frac{\log|\mathcal U_j(T)|}{d_j}
 \ge \beta(L):=1+\log L-\log K_R.
 \tag{10}
\]
Combining only (7) and (10) gives the crude weighted lower rate
\(\beta(L)-2L\). Its maximum over \(L>0\) is
\[
 \max_{L>0}\{1+\log L-\log K_R-2L\}
       =-\log K_R-\log2<0,
 \tag{11}
\]
attained at \(L=1/2\). The sign follows from the explicit \(K_R>1\).
This shows a limitation of that particular lower estimate, not an upper
bound for \(Z(T)\), and not a failure of the unit family. In fact the
torsion contribution already gives the stronger trivial nonnegative
exponential lower rate.

For each fixed field, increasing \(T\) enlarges \(\mathcal U(T)\);
each already included unit keeps exactly the same weight. Consequently
\(Z(T)\) is nondecreasing. Larger \(T\) cannot be described as reducing
this sum. Newly included units may have much smaller weights, and the
population theorem supplies no favorable shell or coordinate distribution.

## 3. MSU-G2 — a fixed-field weighted lattice comparison

Fix one field and a basis \(v_1,\ldots,v_d\) of \(\Lambda\). Let
\[
 P=\left\{\sum_i t_iv_i:-\tfrac12\le t_i<\tfrac12\right\},
 \qquad S=\tfrac12\sum_i\|v_i\|_1 .
 \tag{12}
\]
Extend \(w\) to all \(x\in\mathbb R^d\) by the formula in (4).
The function \(\log w(x)=-2\sum_i(|x_i|-\log2)_+\) is
2-Lipschitz in the \(\ell^1\) metric. For \(x\in\lambda+P\),
\[
 e^{-2S}w(x)\le w(\lambda)\le e^{2S}w(x).
 \tag{13}
\]
The translates of \(P\) tile space up to measure-zero boundaries, and
\[
 \int_{\mathbb R^d}w(x)\,dx=(1+2\log2)^d,
 \tag{14}
\]
because the one-dimensional integral is
\(2\log2+2\int_{\log2}^{\infty}4e^{-2t}\,dt=2\log2+1\).
Integrating (13) over the tiles proves convergence and the two-sided
comparison
\[
 \boxed{
 \frac{w_R e^{-2S}(1+2\log2)^d}{\mathcal R_R}
 \le Z_\infty:=\sum_{u\in\mathcal G}w(u)
 \le \frac{w_R e^{2S}(1+2\log2)^d}{\mathcal R_R}.}
 \tag{15}
\]
Therefore \(Z(T)\uparrow Z_\infty<\infty\) as \(T\to\infty\) with
the field fixed. Since the centered logarithmic population then tends to
infinity, \(Z(T)/|\mathcal U(T)|\to0\) for this fixed-field limit.
This concerns the auxiliary weights, not a return tail.

The basis cost \(S\) is displayed explicitly. The new covolume upper
bound does not remove this shape term, give a covolume lower bound, or
make (15) a uniform upper estimate along the growing tower.

### The restricted continuous-to-discrete limit that is justified

For a fixed field and a fixed finite unit list \(V\), each domain
\(W_T^2\cap M_u^{-1}W_T^2\) is \(T\) times a fixed bounded
Jordan-measurable body. Counting lattice points by fundamental cells gives
its volume asymptotic as \(T\to\infty\): boundary cells have lower-order
total volume. The same applies to \(W_T^2\).
Finite summation consequently gives
\[
 \lim_{T\to\infty}\frac1{n(T)^2}
       \sum_{p\in C(T)^2}R_V(p)
 \le \sum_{u\in V}w(u).
 \tag{16}
\]
At nonzero sources distinct units give distinct targets; the origin
correction is at most \(|V|-1\), which vanishes after normalization.
The continuous counterpart follows directly by integrating indicators.
Its upper mean gives an upper bound for the proportion of rich pairs
by Markov's inequality. Neither bound is a lower-tail conclusion.

The hypotheses “fixed field” and “fixed finite list” in (16) are
essential to this argument. No uniform error for \(\mathcal U_j(T)\),
no interchange with an increasing unit list, and no growing-field
equidistribution statement is being asserted.

## 4. MSU-G3 — an honest discrete comparison with inflation retained

For a unit \(u\), define the actual lattice domain
\[
 D_u(T)=\{p\in C(T)^2:M_up\in C(T)^2\}.
 \tag{17}
\]
For \(s\ge0\), put
\[
 q_T(s)=
 \min\left\{1,
       \left(\frac{2Te^{-s}+1}{T+1/2}\right)^2\right\}.
 \tag{18}
\]
Then, uniformly in the field, the unit and \(T\ge1\),
\[
 \boxed{
 \frac{|D_u(T)|}{n^2}
 \le\frac{(2T+1)^{6d}}{n^2}
                    \prod_{i=1}^d q_T(|\ell_i(u)|)
 \le
 \left[\frac{4D_*^3}{\pi^2}(2+1/T)^6\right]^d
                    \prod_{i=1}^d q_T(|\ell_i(u)|).}
 \tag{19}
\]

**Proof.** Around each center \(p\in D_u(T)\), place the cell
\(p+W_{1/2}^2\). The cell interiors are disjoint. Indeed, a nonzero
algebraic-integer difference has some conjugate of modulus at least one
by its nonzero integer norm. Two intersecting cell interiors would force
all these moduli below one in each differing scalar coordinate.
Every cell lies in \(W_{T+1/2}^2\).

Here \(\eta\) denotes the image of \(\omega\) under the chosen extension
of that complex place, so \(\eta\in\{\omega,\omega^2\}\).
At a complex place with log modulus \(\lambda\ge0\), source and target
membership require \(|x-\eta y|\le2Te^{-\lambda}\).
For \(\lambda<0\), the analogous necessary constraint is
\(|x-\eta^2y|\le2Te^{-|\lambda|}\). Moving inside a cell changes either
linear form by at most one, since each of its two scalar errors has
modulus at most \(1/2\). The entire cell therefore satisfies the
corresponding strip bound of radius \(2Te^{-|\lambda|}+1\).

Inside the ambient bidisk of radius \(T+1/2\), slice over \(y\).
The allowed \(x\)-area is at most the smaller of the ambient disk area
and the strip disk area. Hence the local volume fraction is at most
(18). Multiply these bounds over the independent ambient complex
blocks and bound all real-place fractions by one. Dividing by the cell
volume gives
\[
 |D_u(T)|\le(2T+1)^{6d}
                   \prod_iq_T(|\ell_i(u)|).
 \tag{20}
\]
Finally insert the actual input lower bound (1). This proves (19).
\(\square\)

The additive \(1\) in (18) is necessary for this argument. Erasing it
would replace a proved thickened-cell estimate by an unproved comparison
with the continuous weight. In particular (19) does not justify
\(|D_u|/n^2\le w(u)\).

For a finite nonempty unit list \(V\), let \(R_V(p)\) count distinct
actual targets. There is the exact identity
\[
 \sum_{p\in C(T)^2}R_V(p)
       =\sum_{u\in V}|D_u(T)|-|V|+1.
 \tag{21}
\]
The correction replaces the \(|V|\) labels fixing the origin by its
single distinct target; at nonzero sources the action is free.
Equations (19)–(21) give a genuine uniform discrete upper bound on
mean returns, with its exponential prefactor and the inflated local
weights fully charged. They provide no positive lower bound for that
mean or for a lower tail.

## 5. Independent written-proof audit of MSU-A1–A3

The auditor read all of [arithmetic.md](arithmetic.md), §§1–6,
after its complete proof was written. The following checks are
independent symbolic checks, not reliance on agent agreement or a
finite computation.

1. **Minkowski normalization.** The \(3d\) complex disks have volume
   \(\pi^{3d}B^{6d}\). With \(B=2\sqrt{D_E}\), this strictly exceeds
   \(2^{6d}(2^{-3d}\sqrt{|\Delta_E|})\).
2. **Error budget.** All \(3d\) errors are at most \(g=\log B\), and
   their sum is \(\tfrac12\log|N_{E/\mathbb Q}a|\ge0\).
   Their total absolute sum is at most \(6dg\); the projected relative
   error is at most \(3dg\). No coordinatewise lower error bound is used.
3. **Exact labels.** Both \(I=(a)\) and the element
   \(b=N_{E/K}(a)\) are retained. The ideal norm is at most \(B^{6d}\),
   and every conjugate of \(b\) has modulus at most \(B^2\), including
   the nonreal places of \(K\).
4. **Finite class count.** Unique ideal factorization bounds the number
   of ideals by \(B^{12d}2^{6d}\). Algebraic-norm separation bounds
   the possible elements \(b\) by \((2B^2+1)^{3d}\).
   These are upper bounds, so unrealized or redundant labels cause no
   problem.
5. **Genuine units and the torus cover.** Equal labels give
   \(a/a_k\in\mathcal O_E^\times\) of relative norm exactly one.
   Its projected logarithm is the established \(\ell\), with no factor
   of two missing. Integrating the covering over the relative log torus
   gives \(\mathcal R_E\le J\,2^d(3dg)^d/d!\).
6. **Order and constant.** The factor \(27^d\) is applied once.
   Thus
   \[
   \mathcal R_R\le K_R^d,\qquad
   K_R=27\cdot64B^{12}(2B^2+1)^3\,6e\log B.
   \tag{22}
   \]
   Torsion is not charged again as a loss.
7. **Uniform quantifiers and fixed radius.** For
   \(T_*=\max\{2\sqrt{D_*},\exp(2K_R/3)\}\),
   \(L(T_*)\ge2K_R\). The centered count and \(d!\le d^d\)
   prove \(|\mathcal U_j(T_*)|\ge w_R2^{d_j}\ge2^{d_j}\)
   at every level. All constants precede the growing index.
8. **Scope.** This is a bound on the exhaustive inventory of candidate
   order units. It supplies neither exact target membership nor a
   return distribution. It does not alter the selected seed-family
   obstruction or prove a full-image lower or upper exponent.

**Audit verdict: PASS.** No mathematical gap or correction was found in
the written MSU-A1–A3 proof. This resolves the stated population gate.
It does not resolve T03.

## 6. Rate ledger and remaining obligation

| Item | Audited consequence or retained cost |
|---|---|
| Scalar support | Full same-set Cartesian square; inherited input bounds (1); no thinning |
| Integral actions | Actual norm-one order units; no new coefficient denominator |
| Degree and discriminant | Inherited \(3d,6d\) degrees and bounded root discriminants |
| Order cost | \(27^d\), included once in \(K_R\) |
| Population | Explicit fixed \(T_*\), at least \(2^d\) genuine units at every level |
| Heights | \(h(u)\le L(T_*)/3\); individual house may be \(\exp(dL(T_*))\) |
| Distribution of logs | Only the \(\ell^1\) cutoff is supplied; no favorable shell or bounded-coordinate statement |
| Continuous overlap | Upper bound (4); weight sum is not an actual lower mean |
| Discrete comparison | Proven upper bound (19), including the thickening and exponential prefactor |
| Weighted lattice shape | \(S\) retained in (15); the covolume estimate does not remove it |
| Zero and multiplicity | One zero source; origin correction (21); free unit action elsewhere |
| Exceptional sources | No small exceptional population is established |
| Full image and positive saving | OPEN; no new bound on the entire image follows from population alone |
| Computation | Zero mathematical evaluations and zero research-program CPU |

At the now-fixed \(T_*\), an actual-incidence statement still has to
include both target coordinates and every embedding. The single next
obligation adopted in the main report is MS-O2. Write
\(\Omega=C(T_*)^2\setminus\{(0,0)\}\), \(N=|\Omega|\), and
\[
 S_1=\sum_{u\in\mathcal U(T_*)}|D_u\setminus\{0\}|,\qquad
 S_2=\sum_{u,v\in\mathcal U(T_*)}|(D_u\cap D_v)\setminus\{0\}|.
 \tag{23}
\]
Then the exact nonzero-pair mean is \(\mu=S_1/N\) and its variance is
\(S_2/N-\mu^2\). Bounds
\(\mu\ge e^{\kappa d}\) and
\(S_2/N-\mu^2\le e^{-\eta d}\mu^2\), for fixed positive
\(\kappa,\eta\), would imply by Chebyshev that all but
\(4Ne^{-\eta d}\) nonzero sources have at least
\(\tfrac12e^{\kappa d}\) returns. The origin must additionally be charged.
Both incidence bounds are **OPEN**, and no argument here is claimed to
establish them. Together they form one stronger sufficient lemma, not a
necessary characterization of power saving. Refuting them alone would
not retire the carrier. Recording this obligation does not begin a new
construction or research cycle.

The individual claims MSU-G1–G3 have complete proofs in §§2–4. Their
evidence is local symbolic derivation from the identified frozen
dependencies. The independent arithmetic audit is §5. Any later main
report inspection is a separate consistency check, not a fresh rerun of
the historical mathematics.

## 7. Final main-report and ledger audit

**21 October 2026 — independent final written-file audit: PASS after the
recorded presentation corrections.** The auditor read the complete new
[README.md](README.md), §§1–6, and [ledger.md](ledger.md), then re-read
the corrected support display and table entries. The arithmetic
companion's final provenance paragraph was also inspected; it changes
no mathematical statement or proof.

The following were checked against the complete companion proofs:

- The tower, order, scalar carrier and exhaustive unit cutoff are
  unchanged. The auxiliary arithmetic constant \(B_0\) is explicitly
  distinguished from the scalar upper exponent \(B(T)\).
- The constants \(D_*,D_E,J_0,K_E,K_R,T_*\) agree with MSU-A1–A3.
  The order factor \(27^d\) appears once. The radius precedes the growing
  level, and the proved population bound holds at every level, with
  exponent \(\log2\).
- Candidate unit population is kept separate from actual target
  membership, the continuous overlap diagnostic, the discrete upper
  comparison and the full return distribution.
- The fixed-field weighted limit is not promoted to a uniform
  growing-field result. The negative rate in the crude weighted lower
  estimate is not presented as an upper bound or a carrier obstruction.
- MS-O2 is exactly one eventual, all-large-level, sufficient
  incidence-concentration lemma. It is OPEN, is not claimed necessary,
  and is not implied by MS-O1.
- The selected seed-plus-torsion failure and balanced-factor retirement
  retain their frozen scopes. This new carrier and unrestricted T03
  remain OPEN.

### Independent check of MSU-R1 and the origin

In the report, \(D_{j,u}\) is defined on
\(\Omega_j=A_j^2\setminus\{(0,0)\}\). It therefore corresponds exactly
to \(D_u\setminus\{0\}\) in (23), not to an uncorrected sum that counts
the origin once for each unit. Freeness at nonzero pairs gives
\[
 \frac1{N_j}\sum_{p\in\Omega_j}R_j(p)=\frac{S_{1,j}}{N_j}=\mu_j,
 \qquad
 \frac1{N_j}\sum_{p\in\Omega_j}(R_j(p)-\mu_j)^2
       =\frac{S_{2,j}}{N_j}-\mu_j^2.
\]
Under MS-O2, Chebyshev bounds the number of nonzero pairs below
\(\mu_j/2\) by \(4N_je^{-\eta d_j}\). The full-support implication,
with the origin charged once, is consequently
\[
 |Q(A_j,A_j)|
 \le 2n_j^2e^{-\kappa d_j}
       +4(n_j^2-1)e^{-\eta d_j}+1.
 \tag{24}
\]
From \(n_j\le e^{B(T_*)d_j}\), this is at most
\[
 2n_j^{\,2-\kappa/B(T_*)}
       +4n_j^{\,2-\eta/B(T_*)}+1.
\]
The mean premise and
\(\mu_j\le n_j^2-1<e^{2B(T_*)d_j}\) force
\(\kappa<2B(T_*)\). Hence every positive
\(c<\min(\kappa,\eta)/B(T_*)\) is below two, and the origin and fixed
prefactors are absorbed eventually. This verifies the precise strict
exponent range in the report and ledger without a hidden input-growth
limit or an uncharged exceptional pair.

### Corrections found and confirmed

The initial README display (16) omitted the plus sign before
\(4(n_j^2-1)e^{-\eta d_j}\). The ledger already contained the correct
sum. The lead restored the literal plus sign; the auditor re-read and
confirmed it. This was a transcription correction, not a change in
MSU-R1 or its proof.

Raw mathematical cardinality and absolute-value pipes inside ledger
table cells would have split Markdown columns. They were replaced by
`\lvert` and `\rvert`; the corrected ledger cells were inspected.
The analogous claim-table notation in `verification.md` was inspected
after the same presentation correction. This limited table inspection
is not a claim to have executed or independently reproduced the
administrative checks described in that file.

No remaining mathematical inconsistency was found in the reviewed
main report or ledger. This final review used local reads and edits to
this audit note only: zero mathematical evaluations, zero mathematical
program executions, and no network access. It does not constitute
external peer review, a literature check, or a historical research rerun.
