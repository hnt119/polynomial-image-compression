# T01 three-branch lift: source scope and local arithmetic audit

Date: 2026-09-16. Track T01, fixed polynomial
\(P(x,y)=(x-y)^3+x+y\). This note performs the assigned offline source-scope
audit and supplies the elementary proofs below. No network access, numerical
search, imported program execution, or arithmetic-tower construction occurred.
The scope of source inspection is distinct from independent proof verification.
Inherited working-tree changes were inspected and preserved.

## 1. Located proofs, reported results, and missing files

The setup guide, project map, migration audit, master handoff, T01 state,
separate norm–trace checkpoint, T01 SPEC/STATUS, migration conflicts, and T01
entries in the mechanism/failure/open-lemma libraries were read. The exact
plus-sign cubic remains the target; the norm–trace checkpoint's
\(x^2+xy+y^2+x\) is a separate branch. The user's current instruction authorizes
this new bounded research; historical stops and archived assignments do not
override it.

| ID | Result and status | Source and actual audit in this task |
|---|---|---|
| TB-S1 | **PROVED — inspected complete proof:** continuous-cover obstruction for bounded Borel \(W\subset\mathbb R^m\), \(V>0\): \(N_1(P_{\rm coord}(W,W))>(\sqrt3/\pi)^mV^2\). | `research/history-sources/Concrete_Cubic_Compression_Block_NoGo_Checkpoint.md`, §F.3, equations F.6–F.10; 3 September checkpoint. Proof read line by line; Jacobian/change-of-variables/Cauchy–Schwarz argument checked. |
| TB-S2 | **PROVED — reported in controlling state, full proof unavailable:** regular digital lower bound \(|Z_{b^n}(D_n,D_n)|\ge c_G|D_n|^2\), for fixed base, finite strongly connected right-resolving digit graph, fixed start, all states terminal, growth \(\mu>1\). | `local-only/migration/sources/T01_CURRENT_STATE.md`, §4.3, T01.5, 10 September. Named complete proof `Regular_Digital_Carry_Collapse_Universal_NoGo_Checkpoint.md` is **MISSING SOURCE / PROVENANCE FILE** in the searched supplied tree. The state gives a reconvergent-prefix proof sketch; this is not a substitute for the missing proof. |
| TB-S3 | **PROVED — reported in controlling state, full proof unavailable:** for fixed finite nonempty prime support \(S\), \(\alpha>0\), sufficiently large \(S\)-smooth \(N\), and \(D\subset[0,N)\cap\mathbb Z\) with \(|D|\ge N^\alpha\), \(|Z_N(D,D)|\ge\eta(S,\alpha)|D|^2\). | Same state §4.3, T01.6; explicit constants, fiber estimate and renormalization are reported. Named full digital checkpoint is missing as above. No fresh proof of this theorem is claimed. |
| TB-S4 | **PROVED / FAILED family — reported, full checkpoint unavailable:** precisely specified rich-quadratic-fiber \(A_j=\sigma_1(T_j/(2\sqrt{\zeta_j}))\) has exactly \(|A_j|^2\) plus-cubic outputs. | Same state §4.4, T01.7, with \(\rho_2R\le1/100\), \(M\ge64\), \(X=2\lfloor M/8\rfloor\ge4\sqrt R\), and the explicit largest-fiber definition of \(T_j\). State contains a modular/norm-separation/monotonicity proof sketch. `Cubic_Target_Exact_Elements_and_Candidate_Test.md` is **MISSING SOURCE / PROVENANCE FILE**. |

Both missing checkpoints are already requested by
`output/source-recovery-prompts-2026-09-15/T01_RECOVERY_PROMPT.md`, items 1–3.
Search included ignored migration files and filenames across the supplied
workspace; no substitute full proof was located. The available
`research/history-sources/quadratic_to_cubic_transfer_checkpoint.md` instead
treats \((x-y)^3-3(x+y)\); it cannot fill the plus-cubic proof gap.

For TB-S1, writing
\(J_y(x)=\prod_i(1+3(x_i-y_i)^2)\) gives
\[
V^2\le\operatorname{vol}(P_{\rm coord}(W,y))\int_WJ_y^{-1},
\qquad \int_WJ_y^{-1}<(\pi/\sqrt3)^m.
\]
Every cover of the full image covers this slice. Thus the theorem is a
continuous volume/cover obstruction. It does not lower-bound a sparse finite
real image and does not exclude a finite zero-volume three-branch gadget.

TB-S2/TB-S3 concern growing normalized rational sets with their stated fixed
prime support and entropy. Merely writing three affine branches is not enough
to invoke them: one must establish the precise denominator model, positive
entropy, and fixed prime support. Stage dependence alone does not escape
TB-S3. Algebraic irrational coordinates, growing prime support, zero entropy,
or failure to lie in the normalized interval are outside that theorem as
stated; none is positive evidence for compression. TB-S4 only rejects its
specified carrier and scaling. No generic radical-branch impossibility is
reported.

## 2. TB-L1 — exact prime-power permutation and normalized local obstruction

**PROVED internally here.** For every \(k,d\ge1\), let
\(R_k=\mathbb Z/3^k\mathbb Z\), and use \(P\) coordinatewise on \(R_k^d\).
For every nonempty \(E\subset R_k^d\),
\[
|P_{\rm coord}(E,E)|\ge|E|,
\qquad
\frac{3^{kd}|P_{\rm coord}(E,E)|}{|E|^2}
\ge\frac{3^{kd}}{|E|}\ge1.\tag{L1}
\]
Equality in the last bound is possible only for the full input ring; for
that input the image is the full ring and the normalized ratio is exactly 1.

**Proof.** Modulo 3, \(P(x,y)=-x\) as a function. Fix \(y\), and suppose
\(x\mapsto P(x,y)\) is bijective modulo \(3^k\). For \(t\in\{0,1,2\}\),
\[
P(x+3^kt,y)\equiv P(x,y)+3^kt\bigl(3(x-y)^2+1\bigr)
\pmod {3^{k+1}}.
\]
The parenthesized factor is 1 modulo 3, so exactly one lift of each solution
maps to any specified lifted output. Induction proves that this map is a
permutation of \(R_k\) for every \(y\). Fix one vector \(y_0\in E\); applying
the coordinate permutations to \(E\) is injective and has image contained in
\(P_{\rm coord}(E,E)\). This proves (L1), including for correlated \(E\).
The full-ring support is also immediate from \(P(x,x)=2x\).

Writing the input density as \(\alpha=|E|/3^{kd}\) and output density as
\(q=|P_{\rm coord}(E,E)|/3^{kd}\), equation (L1) reads
\(q/\alpha^2\ge1/\alpha\ge1\). Hence any certificate whose only local gain
is output-residue density and whose input restriction pays density twice
cannot acquire a favorable local factor at 3, at any precision, even with
correlated residue restrictions. This says nothing about a nonuniform global
carrier exploiting exact equality within its lifts. It is not a lower bound
for every real cubic image.

The mod-3 nine input types still have precisely three output types and each
output has three preimages. A fiber count and a sparse output support are
different quantities. After complete splitting, full output support has
density \(1^d=1\), hence zero local logarithmic sparsity gain.

The formula \(P(x,y)=-x\) is a function identity on \(\mathbb F_3\), not on
every characteristic-3 extension: there one has
\(P(x,y)=x^3-y^3+x+y\), and generally \(z^3\ne z\). The diagonal still
proves full-field support in every finite characteristic-3 extension. The
permutation argument above is specifically for powers of 3 with residue
field \(\mathbb F_3\); no claim for arbitrary ramification or residue degree
is inferred.

## 3. TB-L2 — direct coordinate tensorization has no scalar algebra embedding

**PROVED internally here; limited scope.** Let \(d>1\). There is no injective
ring map from the direct-product algebra \(\mathbb Q^d\) into a real field:
the nonzero idempotents \(e_i,e_j\), \(i\ne j\), satisfy \(e_ie_j=0\), while
a field has no zero divisors. Therefore the formal coordinatewise gadget
in a product algebra does not become a scalar real gadget by an injective
algebra embedding.

A slightly more precise version concerns linear encodings. If a real-linear
map \(T:\mathbb R^d\to\mathbb R\) intertwines the cubic on **all** pairs,
\[
P(Tx,Ty)=T(P_{\rm coord}(x,y)),
\]
then with \(y=0\) it preserves coordinatewise cubes. Write
\(a_i=T(e_i)\). Testing \(e_i\) gives \(a_i^3=a_i\); testing
\(e_i+t e_j\) for every real \(t\) and comparing the coefficient of \(t\)
gives \(3a_i^2a_j=0\). Thus at most one \(a_i\) is nonzero, and \(T\) is
either zero or a signed coordinate projection. It is not injective for
\(d>1\). This does **not** exclude a finite nonlinear encoding whose
particular identities are checked directly, nor a number-field construction
using constrained conjugates and a separately proved support bound.

The same conclusion already follows from the finite grid
\(C^d\), \(C=\{0,1,2,3,4,5\}\): suppose
\(T(u)=\sum_iw_iu_i\) and the intertwining identity holds for every
\(u,v\in C^d\). Setting \(v=0\) makes
\[
\left(\sum_iw_iu_i\right)^3-\sum_iw_iu_i^3=0
\quad\text{for every }u\in C^d.
\]
The left side has degree at most 3 in each variable. Successive univariate
root counting on the six distinct coordinate values shows it is identically
zero. Its coefficients give \(w_i^3=w_i\) and
\(3w_i^2w_j=0\) for \(i\ne j\). Thus at most one weight is nonzero,
equal to \(1\) or \(-1\), and \(T\) cannot inject \(C^d\) when \(d>1\).
This is a direct finite-grid obstruction to a linear encoding preserving
every coordinatewise gadget output; it assumes the displayed exact output
transport and excludes no other encoding architecture.

A real field embedding \(K\hookrightarrow\mathbb R\) is injective and
preserves the scalar polynomial. However, the Minkowski coordinates of an
element of \(K\) cannot be assigned independently as a full product algebra.
An arbitrary linear/basis encoding of a Cartesian product introduces mixed
cubic terms. Any proposed amplification must prove its precise carrier
realization and charge those terms and multiplicities; formal coordinate
counts alone do not suffice.

## 4. Arithmetic source boundary

**EXTERNAL RESULT — supplied source, recorded, not independently audited
here:** `local-only/migration/research_supplement/shared/03-unit-distance-proof.pdf`,
Proposition 3.8, is the formal tower source identified by the existing T01
checkpoint. Its recorded data are a totally real unramified pro-3 tower,
fixed root discriminant, and finitely many prescribed completely split
rational primes. These supply degree and arithmetic coordinates; they do
not supply cubic support compression. This note did not reopen or verify
the PDF proof.

`local-only/migration/sources/T01_Norm_Trace_Quadratic_Research_Checkpoint.md`,
§4, records prior survey descriptions of Hajir–Maire–Ramakrishna Proposition
1.9 and Hamza–Maire Theorem A. Those papers' full texts were not found in the
supplied migration bundle. Any needed primary theorem beyond the supplied
description, or a favorable quantitative splitting/discriminant constant,
must therefore be marked **MISSING SOURCE / PROVENANCE FILE**. Their URLs
are bibliographic locators, not evidence that those papers were read here.
No theorem statement is reconstructed from a title and no numerical constant
is assumed.

Existing failure scopes relevant to a later ledger are T01 current-state
§§6.1–6.3 (cube residues, scaled coefficients and uniform lifts), §6.5 (exact
carries), §6.7 (scalar trace labels and denominator containers), and §6.8
(literal \(GP\) cross-pair coverage). In particular the recorded optimistic
mod-9 scaled certificate has factor \(7R/3>1\); that is a certificate failure,
not an actual-image lower bound. The exact polynomial and input scaling must
match before importing it.

TB-L1 supplies no positive local gain to amplify. TB-L2 blocks only literal
universal coordinate encodings. Neither decides whether a specific surviving
finite characteristic-zero branch gadget could later have a different,
fully charged arithmetic realization. That question must wait for the
finite-gadget verdict and a ledger with positive \(2a-b\).

## 5. Provenance and verification

Claims TB-L1/TB-L2 quantify over the displayed rings, dimensions, subsets or
linear maps, use only elementary algebra, and have complete proofs in §§2–3
of this 2026-09-16 note. They are **PROVED internally**, with no external
novelty assertion. Their unresolved gaps are deliberately outside their
stated scopes: real scalar carrier realization and full-image amplification.

Source hashes read from original bytes in this task:

```text
T01_CURRENT_STATE.md
2095cb7b4a5f7d848dea1356956ad36f5303e4037b13b2efe7fa32b0c08f2624
T01_Norm_Trace_Quadratic_Research_Checkpoint.md
a9de1edb1ebc43465de7e12cd2e815e8647b4199a0c303afff2e4a8815abc0db
Concrete_Cubic_Compression_Block_NoGo_Checkpoint.md
413dcc5aa06ddc03129d76a68360dc1737a0a7d156d70e27a510a4699d5bbc62
Cubic_Difference_Sum_Research_Checkpoint.md
1a5ecffb8366cd4ef2a0447d16bc183c7c8cde646428db5bc6163959d1e95b92
T01_RECOVERY_PROMPT.md
5da52a0b1f7a1e900e48089a9995b8a2b2e38166b5787d297254ceed6b2ad2fa
```

Read-only shell operations were Git status/diff summaries, file inventory,
text searches/reads, and Python-standard-library SHA-256 of the listed
sources. Hashing is file identification, not proof verification. No original
archive, source, SPEC, or status file was changed. This note is the only file
created by the source-scope subtask; repository checks are coordinated by the
lead report task.
