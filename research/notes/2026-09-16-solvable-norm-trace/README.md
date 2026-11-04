# Solvable extensions, norm/trace, and the Eisenstein multiplier

**Research cycle: 16 September 2026. Outcome: OPEN — no power-saving
construction established.** This is commissioned research with new exact
experiments and written proofs. It is separate from the earlier migration
and study-note work. The four fixed track polynomials remain unchanged.

## 1. Scope and strongest conclusions

The user requested general solvable extensions combining addition and
multiplication, especially norm/trace structures beyond corrected C0, followed
by the SN-T03-1 Eisenstein multiplier if the first route failed. The shared
benchmarks here are

$$q(x,y)=x^2+xy+y^2,\qquad P_0(x,y)=q(x,y)+x.$$

For each fixed polynomial, the objective remains arbitrarily large finite
real $A$, one fixed positive exponent, and an upper bound on the image of
**every ordered pair** in $A^2$. The separate $P_0$ branch does not replace
T01's cubic. The multiplier experiments are separate from T03's actual
adaptive sequence; they do not establish RC15/4.

Results, with their scopes:

1. **PROVED, internally derived and independently inspected:** a literal
   higher-degree norm of a polynomial, plus its lower-degree trace term,
   cannot represent a quadratic. A separate exact intermediate-field lemma
   shows that forcing the entire mixed-quadratic image into a subfield
   reduces the input to that subfield, up to a common quadratic scaling and
   common shift in the specified case. See [algebra](algebra.md).
2. **EXPERIMENTAL, exhaustive exact finite sets:** additive/unit carriers in
   cyclic cubic, real cubic with solvable $S_3$ closure, and biquadratic fields
   have small individual norm supports and some product compression. Their
   complete quadratic images remain close to the symmetry bound in the
   tested range. Taking scalar traces loses many distinct inputs.
3. **PROVED, every $m\ge1$, independently audited internally:** for the
   multiquadratic sign cube with $n=2^m$,

   $$|q(A_m,A_m)|=n^2/4+n/2,\qquad |P_0(A_m,A_m)|=n^2.$$

   This particular growing solvable-field family is **FAILED** for a fixed
   power saving. The result does not exclude other carriers in those fields.
   See the complete [sign-cube proof and ledger](sign-cube.md).
4. **EXPERIMENTAL:** extension-valued Eisenstein multipliers create rich
   engineered fibers, but most pairs of the completed coordinate set have
   only the identity return under the tested multiplier set. Full images,
   input denominators, and return tails are counted exactly.

The finite tests do not establish an asymptotic lower bound for the other
families. Their disposition is **no supported positive rate in this cycle**,
not a universal impossibility result.

## 2. Authorization, budget, and source reconciliation

The cycle was announced before research: at most **12 carrier families,
2,000,000 exact ordered-pair evaluations, and 600 CPU seconds**, using the
Python standard library. Action-pair tests, candidate evaluations, and
research reruns are reported separately and charged conservatively to that
same two-million ceiling. Finite proof-regression tests are also disclosed.
No package installation, remote mutation, or imported research program was
used. No pickle was loaded. ZIP member names were inspected before reading
selected Markdown members; archives were not extracted or altered.

Network policy was primary-source verification only. Actual use was one
targeted primary-source search about multiquadratic bases and an unsuccessful
direct PDF open. No external theorem, bibliographic claim, or novelty claim
depends on those results. The needed basis statement has an elementary proof
in [sign-cube.md](sign-cube.md). This was not a literature or priority audit.

Controlling sources inspected:

- Corrected `Phase_C0_Corrected.md`, Theorem C0.1, §§4–6, and
  `C0_CORRECTION_LOG.md`, in `local-only/migration/research_supplement/shared/`.
  The rank-one square-saving mechanism and its arithmetic costs are retained.
  This cycle did not independently recertify its source tower theorem.
- `local-only/migration/sources/00_MASTER_HANDOFF.md`, especially §§7, 11–13;
  T01 and T03 current-state exports; the final T01 norm–trace checkpoint;
  both selected tracks' SPEC and STATUS; setup/map/audit and the mechanism,
  failure, conflict and open-lemma registries.
- `research/notes/2026-09-14-study-notes/03-eisenstein.md`, SN-T03-1, and its
  formal supporting `Quadratic_Norm_Form_Focused_Offline_Report.md`, §§2–6,
  inside the T03 ZIP. The five final TCRC companions were read to retain the
  actual adaptive frontier and avoid claiming this separate branch advances it.

The existing arbitrary-decomposition and variable-prime full-input sieve
obstructions are **inherited**, already recorded in T03 current state §6.
They are not discoveries of this cycle. Likewise, completing a norm does
not repair the unequal shifts in $P_0$; the T01 checkpoint §2.3 transfer still
requires an unavailable homogeneous witness with sufficiently small differences.

The retained missing standalone F25 certificate and separate final-checkpoint
designation issue are recorded in `research/MIGRATION_CONFLICTS.md`. Neither
is used by the proofs or experiments here. No missing proof was reconstructed.

## 3. NT-20260916-4 — actual additive/unit and trace carriers

**Status: EXPERIMENTAL.** Date/version: this file, 2026-09-16. Evidence:
reviewed new standard-library code, independent small arithmetic oracles,
and exhaustive enumeration of all pairs of every listed finite set.
Dependencies: irreducible power-basis definitions below; no source tower,
regulator, or residue-uniformity theorem is assumed. Code and data hashes
are in the cycle manifest and result files.

For a selected field $K=\mathbb Q(\theta)$ of degree $d$, fix

$$B=\{4+\textstyle\sum_{i=0}^{d-1}b_i\theta^i:b_i\in\{0,1\}\},
\quad G_k=\{u^e:-k\le e\le k\},\quad C_k=G_kB.$$

Use one injective real embedding for $A_k=\sigma(C_k)$. The separate scalar
trace carrier is $T_k=\{\operatorname{Tr}_{K/\mathbb Q}(c):c\in C_k\}$;
its collisions are explicitly deduplicated **before** either input count.
Both polynomials are evaluated on $A_k^2$ and separately on $T_k^2$.
The fixed tested depths are $k=0,1,2,4$.

| Field and chosen real root | $u$ and integral inverse | Algebraic justification |
|---|---|---|
| Cyclic cubic, $\theta^3-3\theta+1=0$, root in $(1,2)$ | $u=\theta$, $u^{-1}=3-\theta^2$ | No rational root; discriminant $81$ is square; all three roots real. Irreducible cubic has transitive group in $A_3$, hence $C_3$. |
| $\theta=\sqrt[3]2$ | $u=\theta-1$, $u^{-1}=1+\theta+\theta^2$ | Eisenstein at $2$; closure $\mathbb Q(\sqrt[3]2,\omega)$ has solvable group $S_3$. The real cubic itself is not Galois or totally real. |
| $\theta=\sqrt2+\sqrt3$ | $u=\theta$, $u^{-1}=10\theta-\theta^3$ | $\theta^4-10\theta^2+1=0$; $1/\theta=\sqrt3-\sqrt2$ recovers both radicals, so degree four and group $C_2\times C_2$. |

Here the cubic irreducibility and Galois classifications are elementary
algebraic checks of these explicit fields, not an assumed quantitative
realization theorem. Polynomial arithmetic reduces exactly modulo the stated
minimal polynomial. Individual absolute norms use the determinant of the
multiplication matrix; traces use its diagonal sum.

The largest tested unit depth gives:

| Carrier, $k=4$ | $n$ | $|N_{K/\mathbb Q}(C_k)|$ | $|A_k+A_k|$ | $|A_kA_k|$ | $|q(A_k,A_k)|$ | $|P_0(A_k,A_k)|$ |
|---|---:|---:|---:|---:|---:|---:|
| Cyclic cubic | 72 | 16 | 2,211 | 612 | 2,628 | 5,118 |
| Real cubic with $S_3$ closure | 72 | 8 | 2,373 | 612 | 2,620 | 5,163 |
| Biquadratic | 144 | 16 | 7,593 | 2,312 | 10,440 | 20,240 |

For example, $2,628=72\cdot73/2$: at this cyclic-cubic input, swapping the
two inputs accounts for every homogeneous collision. A small support of
**individual absolute norms** does not bound $q(A,A)$, which is a relative
quadratic norm of the correlated set $A-\omega A$.

At the same depths, trace projection leaves only $44,49,23$ distinct inputs,
respectively. Their homogeneous images have $812,986,274$ values; the $P_0$
images have $1,764,2,132,529$. The projection loss cannot be omitted or counted
only once. These are exact finite observations, with no fitted limiting exponent.

### Carrier ledger

| Cost or gain | Accounting and scope |
|---|---|
| Inputs and parameter fibers | At listed levels, $|C_k|=2^d(2k+1)$ by exhaustive deduplication; no assertion of this equality at untested depths. The full finite size and parameter count are recorded at every level. |
| Trace thinning/fibers, both inputs | Exact trace cardinalities replace the input size on both axes; trace is not an injective real projection. An asymptotic trace-fiber bound is unknown. |
| Field degree, discriminant, regulator | Fields are fixed degree $3,3,4$. Their integral power-basis discriminants are $81,-108,147456$; maximal-order discriminants are not needed. No regulator or lattice estimate enters exact enumeration. Fixed low degree supplies no growing-degree rate. |
| Units, heights, denominators | Explicit integral $u,u^{-1}$ verified algebraically; all inputs and outputs lie in $\mathbb Z[\theta]$. Denominators are one. Coefficient growth is recorded; it is not discarded. |
| Conjugate distortion | With $H_B=\max_\sigma\sum_i|\sigma(\theta)|^i+4$ and $H_u=\max_\sigma\max(|\sigma(u)|,|\sigma(u)|^{-1})$, input house is at most $H_BH_u^k$ and output house at most $3H_B^2H_u^{2k}+H_BH_u^k$. Complex embeddings are included for the real cubic. These bounds are not used as a small-support certificate. |
| Local sparsity/splitting and uniform packing | No sieve or class-population estimate is used; there is no local gain to add. |
| Ratios, branches, carries | Every unit exponent and box input is included and deduplicated; every cross-pair is evaluated. There is no digit or separate-ratio compression assertion. |
| Exceptional outputs | None in the finite counts. No large-level exception theorem is supplied. |
| Final rates and exponent | Unknown beyond the bounded range. No positive $\delta$ or fixed target exponent is certified. |

## 4. NT-20260916-5 — a zero-safe multiplier support certificate

**Status: PROVED**, inherited criterion independently rederived with its
zero case explicit. Formal source: T03 ZIP
`output/Quadratic_Norm_Form_Focused_Offline_Report.md`, §6, Lemma 6.1;
SN-T03-1 identifies the coordinate action. Version/correction: this section,
16 September 2026. No numerical premise is used.

For a real field $L$, set $E=L(\omega)$, $\omega^2+\omega+1=0$. If
$u=r+s\omega$ and $r^2-rs+s^2=1$, then

$$T_u(a,b)=(ra+sb,-sa+(r-s)b),\qquad q(T_u(a,b))=q(a,b).$$

Let $A\subset L$ be finite, $n=|A|$, $U\subset E$ a finite set of distinct
norm-one elements containing $1$, and

$$R_U(a,b)=|\{u\in U:T_u(a,b)\in A^2\}|.$$

Let $E_M$ contain $(0,0)$ if it belongs to $A^2$, together with every
nonzero pair with $R_U(a,b)<M$, where $M\ge1$. Then

$$|q(A,A)|\le n^2/M+|E_M|.$$

**Proof.** The map $(a,b)\mapsto a-\omega b$ is injective because $a,b$
are real and $\omega$ is nonreal. Distinct multipliers applied to a nonzero
element give distinct representatives of the same norm. Thus every output
having a representative outside $E_M$ has a full fiber of at least $M$
points, and there are at most $n^2/M$ such outputs. Outputs represented
only inside $E_M$ contribute at most $|E_M|$ more. This covers all pairs.

**Dated precision correction:** the source's preamble explicitly restricts
distinct representatives to $z\ne0$, but its displayed lemma omits the zero
exception. Including zero in $E_M$ is necessary, for example when $A=\{0\}$
and $M>1$. The corrected form above and the code both charge it. Also, bounds
$M\ge n^\epsilon$ and $|E_M|\le Cn^{2-\eta}$ give any exponent strictly
below $\min(\epsilon,\eta)$ eventually, absorbing constants. They do not
automatically give the boundary constant-free exponent. The archive is unchanged.

The **OPEN** construction obligation is to prove such a growing return
threshold and subquadratic exceptional tail for actual same-set carriers,
after their complete input and arithmetic costs. Neither an average return
count nor one rich norm fiber supplies that statement.

## 5. NT-20260916-6 — extension-valued Eisenstein experiments

**Status: EXPERIMENTAL**, exact and exhaustive for the finite sets below.
Code: [eisenstein_solvable.py](../../../experiments/eisenstein_solvable.py).
The fields are $L_m=\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_m})$, with the
fixed prefix $(p_1,p_2,p_3)=(2,3,5)$ and all roots positive. Write

$$\pi_i=1-\omega\sqrt{p_i},\qquad
u_i=\pi_i/\overline{\pi_i},\qquad
U_m=\prod_i\{u_i^{-1},1,u_i\}.$$

All multipliers have norm one by direct multiplication. Each $u_i$ has
coefficients with rational denominator dividing $p_i^2+p_i+1$; products in
this finite alphabet therefore have a shared denominator dividing
$D_m=\prod_i(p_i^2+p_i+1)$, which equals $7,91,2821$ at the tested levels.

For each word set $Z$, take **one** signed union of both coordinate
projections of $z=a-\omega b$ as $A$. Definitions are:

- F1: $Z=U_m$, $m=1,2,3$.
- F2: $Z=H_mU_m$, where $H_m=\{1+\sum_i b_i\sqrt{p_i}:b_i\in\{0,1\}\}$,
  $m=1,2$. This is genuine additive thickening of the multiplier carrier.
- F3: $Z=\prod_i\{1,\sqrt{p_i},\pi_i,\overline{\pi_i}\}$, $m=1,2,3$.
  The local norm alphabet is $\{1,p_i,1+p_i+\sqrt{p_i}\}$.

These extension-valued letters are different from the rational split/inert
prime-marker code in the old CR obstruction. That obstruction is not
imported without its rationality and prime-label hypotheses.

| Family | $m$ | $n=|A|$ | Distinct engineered pairs | Engineered norm values | Full $|q(A,A)|$ |
|---|---:|---:|---:|---:|---:|
| F1 | 1 | 9 | 3 | 1 | 18 |
| F1 | 2 | 27 | 9 | 1 | 171 |
| F1 | 3 | 81 | 27 | 1 | 1,602 |
| F2 | 1 | 17 | 6 | 2 | 59 |
| F2 | 2 | 105 | 36 | 4 | 2,690 |
| F3 | 1 | 7 | 4 | 3 | 11 |
| F3 | 2 | 29 | 16 | 9 | 163 |
| F3 | 3 | 137 | 64 | 27 | 4,289 |

At F1, $m=3$, the complete nonzero-pair return histogram is

| Number of returning multipliers | 1 | 8 | 12 | 18 | 27 |
|---|---:|---:|---:|---:|---:|
| Ordered pairs | 6,398 | 48 | 72 | 36 | 6 |

The additional zero pair is charged separately. A threshold above one already
leaves at least $6,399$ exceptional pairs, out of $81^2=6,561$. The actual
norm-one output fiber has 162 representatives, but the rest of the support
is not controlled by that rich fiber. At F2, $m=2$, $10,696$ of $11,024$
nonzero pairs return only under the identity. All listed multipliers were
tested on every pair; these are not sampled tails.

### Full construction ledger for F1–F3 and rephasing

| Gain/cost | Bound, status, and remaining obligation |
|---|---|
| Input counts and parameter fibers | Exact finite deduplication; $n$ and word-label counts recorded. In general, $|Z|\le n^2$ and $n\le4|Z|$ for signed completion. No unproved injectivity of word labels is used. Uniform asymptotic lower and upper input rates are unknown. |
| Thinning in both coordinates | No finite input thinning. Coordinate sharing/word fibers are counted before $A^2$; a future stable-core restriction would need its loss charged twice. |
| Field degree and real projection | $[L_m:\mathbb Q]=2^m$ by the proved independent-prime basis lemma; $[L_m(\omega):\mathbb Q]=2^{m+1}$. Only $L_m$ is embedded into the real inputs. Projection to this real embedding is injective. |
| Discriminant/regulator/units | No bounded-discriminant or regulator estimate is assumed. These are fractional norm-one elements, not an uncharged exponential family of integral units. Exact finite coordinate counting does not use a lattice-volume theorem. |
| Denominators and normalization | F1/F2 denominators $D_m$ recorded exactly, F3 denominator one. A common scalar clearing $D$ preserves $|q(A,A)|$ via $q(DA,DA)=D^2q(A,A)$. It does not by itself transfer the $P_0$ experiment. Rephasing denominators must be charged separately. |
| Heights and conjugate distortion | Every conjugate of $u_i$ has complex absolute value one. If $z=a-\omega b$ has absolute value $R$ at such an embedding, $|a|,|b|\le2R/\sqrt3$. F1 has $R=1$; F2 has $R\le1+\sum\sqrt{p_i}$; F3 has $R\le\prod\sqrt{p_i+1+\sqrt{p_i}}$. These bounds control height but supply no lattice-return count. |
| Local moduli/splitting and class population | No CRT saving or uniform residue population is assumed. Denominator divisibility for each tested action is checked exactly. |
| Branches, multiplier ratios, carries | All words are evaluated, all coordinates completed, and every Cartesian pair counted. F1/F2 test the entire explicitly listed $U_m$. F3 has no measured return tail. No digit/carry argument is invoked. |
| Exceptional/uncovered pairs | Exact unengineered counts $n^2-|Z|$ recorded; all their actual outputs counted. The tail certificate additionally charges zero. Selected engineered pairs never replace the full square. |
| Output upper bound | Finite actual support, plus the valid general bound $|N(Z)|+n^2-|Z|$. The latter has a large uncovered term in the tested cases. |
| Rates $a,B,g$, net $2a-g$, fixed exponent | No uniform favorable rates proved. Finite ratios and finite large fibers do not certify an asymptotic exponent. The targets remain OPEN. |

## 6. Reproducibility and completion

New scripts are opt-in modules; they are not added to the default historical
`experiments verify` search. Full runtime, command, finite schedule, code and
input/output hashes are stored with the local run records. Compact results,
the rephasing experiment, final validation, and aggregate budget accounting
are recorded in [run-summary.md](run-summary.md).

No historical archive, canonical manifest, SPEC, STATUS, or preexisting
working-tree change was edited. All cycle files remain uncommitted.
