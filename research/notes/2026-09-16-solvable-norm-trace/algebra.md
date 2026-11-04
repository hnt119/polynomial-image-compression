# Algebraic limits of two exact norm–trace reductions

Date: **2026-09-16**. Branch: **shared rational full-rank quadratic research**;
the four fixed track identities are unchanged. Benchmarks are
$q=x^2+xy+y^2$ and the separate $P_0=q+x$ branch.

**Outcome:** the two lemmas below are **PROVED**, by internal derivations
written in this task and independently inspected by the parent agent. They
give exact reductions for specified architectures. They provide no growing
construction and no image lower bound for arbitrary finite real sets.
External novelty has not been assessed.

## Authorization, provenance, and evidence

The current user commissioned investigation of more general solvable
extensions, addition and multiplication, and norm/trace structures toward
general quadratic forms, with an Eisenstein multiplier fallback. This note
covers the bounded algebraic subtask: one higher-degree norm representation
and one exact intermediate-field output architecture. It does not replace
T01's cubic target or T03's selected adaptive-level obligation.

- Network policy: primary-source verification only if needed, at most four
  queries in this subtask. **Actual use: zero network calls.**
- Finite computation budget for this subtask: tiny symbolic arithmetic only;
  no enumerative research runs. **Actual evidence here: written algebraic
  proofs, with no computational premise.** The separately documented parent
  experiments are not used to prove these lemmas.
- Evidence type: internal derivation plus independent parent inspection of
  both complete arguments, including the nonzero-coefficient cases and exact
  same-set transport. This is not external review.
- Version: this dated file, claim IDs **NT-20260916-1** and
  **NT-20260916-2**. The parent research manifest records file/source hashes.

Source history inspected:

1. `local-only/migration/sources/00_MASTER_HANDOFF.md`, §§11–12, records the
   shared direction; it supplies no proof of compression.
2. `local-only/migration/sources/T01_Norm_Trace_Quadratic_Research_Checkpoint.md`,
   10 September 2026, §§2 and 4–7, gives the completed quadratic norm, the
   same-set transfer implication, quantitative field supply, and failed
   specified carrier certificates. The present lemmas use only elementary
   field and polynomial algebra, not its imported arithmetic theorems.
3. `local-only/migration/research_supplement/shared/Phase_C0_Corrected.md`,
   corrected 3 September 2026, Theorem C0.1 and §§5–6, together with
   `local-only/migration/research_supplement/shared/C0_CORRECTION_LOG.md`,
   controls the reported rank-one baseline and its scope. These lemmas do
   not independently recertify that theorem's arithmetic dependencies.
4. `local-only/migration/sources/T03_CURRENT_STATE.md`, 10 September 2026,
   §§5.2–5.4 and §6's quantitative scopes, already records the
   arbitrary-decomposition and variable-prime failures of the specified
   full-input norm-sieve certificate. That obstruction is inherited and is
   not presented as a new result here.
5. [T01 status](../../tracks/01-cubic-digital/STATUS.md),
   [migration conflicts](../../MIGRATION_CONFLICTS.md), and the
   [open-lemma registry](../../OPEN_LEMMAS.md) retain the distinct targets
   and the unresolved full-support obligations.

No proof-bearing source is missing for the two self-contained arguments
below. Other retained migration availability gaps are not used as premises.

## NT-20260916-1 — degree of one norm plus its trace term

**Status: PROVED.** For every finite separable extension $L/F$ of degree
$n>1$, every nonconstant polynomial $\psi\in L[x,y]$ of total degree
$s\ge1$, every $a\in F^\times$, every $\beta\in L$, and every $c\in F$,

$$
\deg\bigl(aN_{L/F}(\psi)+\operatorname{Tr}_{L/F}(\beta\psi)+c\bigr)=ns.
$$

The norm and trace are the product and sum of the conjugate polynomials,
where embeddings act on coefficients and fix $x,y$. In particular, if the
displayed polynomial equals any fixed quadratic polynomial, then $n=2$
and $s=1$.

### Proof

Let $h$ be the degree-$s$ homogeneous part of $\psi$. It is nonzero.
Inside an algebraic closure of $F$, the norm is the product of the $n$
conjugate polynomials. Its degree-$ns$ homogeneous part is

$$
\prod_{\sigma:L\hookrightarrow\overline F\,/F}\sigma(h).
$$

Every $\sigma(h)$ is nonzero because $\sigma$ is an injective field map.
Their product is nonzero because the polynomial ring over $\overline F$
is an integral domain. Thus $\deg N_{L/F}(\psi)=ns$.
The trace term has degree at most $s$, while $ns>s$. It cannot cancel the
norm's leading term; multiplication by $a\ne0$ also preserves that term.
The assertion follows. Since $n>1$ and $s\ge1$ are integers, $ns=2$
forces $n=2,s=1$. $\square$

### Exact interpretation and limitations

This rules out replacing the completed quadratic norm by **one** norm from
a higher-degree separable extension of a polynomial parametrization,
with only the displayed trace term available to cancel it. Solvability is
irrelevant to the proof. Iterating norms without additional operations still
amounts to a single norm and has the same degree cost.

This lemma does not cover rational parametrizations, cancellation between
several norms, an outer trace of quadratic norms, or the use of a larger
solvable extension solely as a source of coefficients and carriers. No
claim is made that these other architectures produce a positive rate.

## NT-20260916-2 — exact intermediate-field image rigidity

**Status: PROVED.** Let $F\subset K$ be any characteristic-zero fields.
Fix

$$
P(x,y)=ax^2+bxy+cy^2+dx+ey+r\in F[x,y],
\qquad b\ne0,\quad\Delta=b^2-4ac\ne0.
$$

For every finite $A\subset K$ with $|A|\ge2$ and
$P(A,A)\subset F$, define

$$
u=2a+b,\qquad v=b+2c,\qquad J=vd-ue.
$$

Then the following alternatives hold.

1. If $J\ne0$, necessarily $A\subset F$.
2. If $J=0$, there are $t\in F$, $\delta\in K^\times$, a finite
   $D\subset F$, and $r_0\in F$ such that

   $$
   \delta^2\in F,\qquad A+t=\delta D,\qquad
   P(A,A)=\delta^2q(D,D)+r_0,
   \quad q(x,y)=ax^2+bxy+cy^2.
   $$

   Consequently $|A|=|D|$ and $|P(A,A)|=|q(D,D)|$.

For the research application take $F\subset K\subset\mathbb R$ and fixed
rational coefficients. The assertion holds for every tower level, without
requiring that $K/F$ be finite, Galois, or solvable.

### Proof

Choose distinct $z,z+\delta\in A$. For all $x,y\in A$, the mixed
rectangular difference is

$$
P(x,y)-P(x,z)-P(z,y)+P(z,z)=b(x-z)(y-z)\in F.
$$

First put $x=y=z+\delta$. Since $b\in F^\times$, this gives
$\delta^2\in F$. Next put $y=z+\delta$. Dividing by
$b\delta^2\in F^\times$ shows that $(x-z)/\delta\in F$ for every
$x\in A$. Thus

$$
A=z+\delta D_0,\qquad D_0\subset F,\qquad 0,1\in D_0.
$$

The two differences involving $z+\delta$ and $z$ are

$$
P(z+\delta,z)-P(z,z)=a\delta^2+\delta(uz+d),
$$

$$
P(z,z+\delta)-P(z,z)=c\delta^2+\delta(vz+e).
$$

They imply

$$
\ell_1:=\delta(uz+d)\in F,\qquad
\ell_2:=\delta(vz+e)\in F.
$$

If $J\ne0$, then

$$
v\ell_1-u\ell_2=\delta J\in F,
$$

so $\delta\in F$. At least one of $u,v$ is nonzero: if both vanished,
then $a=c=-b/2$, contrary to $\Delta\ne0$. The corresponding equation
for $\ell_1$ or $\ell_2$ therefore gives $z\in F$. It follows that
$A\subset F$, proving the first alternative.

Suppose now $J=0$. Since $(u,v)\ne(0,0)$, there is a unique $t\in F$
with $d=ut$ and $e=vt$. To check the possible zero coefficient explicitly:
if $u\ne0$ take $t=d/u$ and use $vd=ue$; if $u=0$, then $v\ne0$,
$vd=0$ gives $d=0$, and take $t=e/v$. Hence

$$
P(x,y)=q(x+t,y+t)+r_0,
\qquad r_0=r-(a+b+c)t^2\in F.
$$

Set $B=A+t$ and $z'=z+t$. Then $q(B,B)\subset F$ and
$B=z'+\delta D_0$. Apply the preceding row and column differences to
$q$ and this translated set. As $q$ has no linear terms, they give

$$
\delta uz'\in F,\qquad \delta vz'\in F.
$$

One of $u,v$ is nonzero, so $\delta z'\in F$. Division by
$\delta^2\in F^\times$ gives $z'/\delta\in F$. Therefore

$$
D=z'/\delta+D_0\subset F,\qquad B=\delta D.
$$

Homogeneity of $q$ now gives the claimed equality of full images. Both
the input affine map and the output affine map are injective, so they
preserve the stated cardinalities. Every ordered pair is covered, with
no exceptional pairs or multiplicity loss. $\square$

### The two benchmarks

For $q=x^2+xy+y^2$, $u=v=3$ and $J=0$. Therefore

$$
q(A,A)\subset F
\quad\Longrightarrow\quad
A=\delta D,\ D\subset F,\ \delta^2\in F,
\quad |q(A,A)|=|q(D,D)|.
$$

For $P_0=q+x$, $J=3\ne0$. Therefore

$$
|A|\ge2,\quad P_0(A,A)\subset F
\quad\Longrightarrow\quad A\subset F.
$$

Thus forcing the **entire** benchmark image into an intermediate field
does not yield a construction supported on genuinely higher extension
coordinates. In the homogeneous case, $F(A)\subseteq F(\delta)$ has
degree at most two over $F$. In the $P_0$ case, $F(A)=F$.
For example, with $F=\mathbb Q$ and a cubic field $K$, the homogeneous
alternative also forces $A\subset\mathbb Q$: a degree-two intermediate
field is impossible because extension degrees multiply.

### Exact scope

The hypothesis $b\ne0$ is essential to this argument. It does not cover
$x^2+y^2$, where unrelated square roots can have all pair outputs in $F$.
The lemma also does not cover an output support spanning $K$, a union of
several subfield cosets, restrictions holding on selected pairs only, or
arbitrary trace parametrizations. These cases remain outside its conclusion.

## Quantitative ledger: no construction is supplied

These lemmas are reductions of architectures, not serious construction
candidates. Their exact accounting is nevertheless recorded to prevent
an ambient degree from being mistaken for an input or output gain.

| Gain or cost | Bound and status |
|---|---|
| Input count before any restriction | Unspecified. No ambient carrier is constructed. |
| Actual input count | **PROVED:** in the homogeneous/common-center alternative, $|A|=|D|$ exactly; in the other alternative $A\subset F$. |
| Input thinning in both coordinates | No thinning in the proved transport. If an ambient carrier is thinned to enforce $P(A,A)\subset F$, its unknown loss must still be charged twice. |
| Parameter and real-projection fibers | **PROVED:** the input map has one-point fibers. If $K\subset\mathbb R$ is specified through a real field embedding, that embedding is injective. |
| Full ordered-pair output support | **PROVED:** exact image equality, not merely containment on selected pairs. |
| Additional support saving from $K/F$ | Zero for these exact reductions: both cardinalities reduce to the base-field problem. This does not assert that the base-field problem has zero saving. |
| Field degree | **PROVED:** relevant input field is at most quadratic over $F$, and equals $F$ for $P_0$. Additional ambient degree is unused. |
| Discriminant, regulator, units | Inapplicable to the algebraic identities. No quantitative arithmetic carrier is supplied; any later construction must count these costs. |
| Local moduli and splitting | Inapplicable: no residue sieve is used. The earlier full-input sieve obstruction remains inherited source history. |
| Heights, denominators, normalization | Exact affine transport preserves cardinalities without a height hypothesis. Heights of $D$ or $\delta$ are uncontrolled and cannot be assigned zero cost in a subsequent arithmetic counting argument. |
| Archimedean radii and distortion | No radius or packing estimate is asserted; these costs remain to be proved for any later carrier. |
| Branches, ratios, carries | One exact transport and no digit model. No additional branch or ratio count is used. |
| Exceptional or uncovered pairs | Zero in the stated lemmas: all pairs in $A^2$ satisfy the premise and are transported. |
| Actual growing input/output rates | Unspecified. Neither lemma provides $a>0$, an output rate, or a positive $\delta=2a-c+s$. |
| Certified fixed exponent | None. The quadratic construction targets remain **OPEN**. |

More explicitly, suppose a separate construction over base fields of degrees
$m_j$ already supplied bounds with input rates $a,B$ and output rate $g$.
Writing those same sets inside larger fields of degree $d_j=h m_j$, for
fixed $h$, merely replaces these rates by $a/h,B/h,g/h$. The ratio
$(2a-g)/B$ is unchanged. If $h=h_j$ grows, a positive lower input rate per
ambient degree need not remain positive. The exact cardinality equalities
above hold in either case, so an unused extension supplies no extra saving.

## Disposition

**PROVED:** NT-20260916-1 and NT-20260916-2 in the exact scopes stated.
**OPEN:** a growing same-set carrier with a complete support bound and a
strictly positive net rate for either benchmark. The proofs do not establish
such a carrier and do not refute the benchmark targets. No historical
archive, SPEC, or prior claim status is rewritten by this note.
