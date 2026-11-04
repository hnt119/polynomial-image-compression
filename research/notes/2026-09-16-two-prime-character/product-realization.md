# TP-P1 / TP-R1 / TP-R2 — product returns and exact real realization

**Date/version:** 16 September 2026, version 1. Track T03, the newly
commissioned two-prime character-correlation branch. The fixed polynomial is
\(Q(x,y)=x^2+xy+y^2\). Statements in the product model concern its
coordinatewise evaluation in a finite ring; they are not real-set
compression theorems.

## Identity, provenance and task boundary

- **TP-P1 — PROVED:** exact product returns, trivial stabilizers, a uniform
  return bound, a typical-log-return theorem and quantitative exceptional
  tails for the full product model defined below. This uses the complete
  one-block proof [TP-L1](local-count-proof.md), §§1–5, inspected in this
  subtask. Its histogram, minimum return count, and norm-zero orbit accounting
  were checked against its displayed sign-count argument.
- **TP-R1 — PROVED / scoped FAILED realization:** a group-compatible
  homomorphism from the product multiplier group into real scalar norm-one
  multipliers has at most eighteen image elements. Thus this exact
  realization loses the exponential return gain through repeated scalar
  actions. It does not prohibit nonhomomorphic lifts or unrelated carriers.
- **TP-R2 — PROVED / scoped FAILED realization:** an exact scalar
  factorization of the whole coordinatewise norm map that sends its zero
  output to real zero collapses every input. The zero-preservation and
  whole-square hypotheses are explicit and essential.
- **Evidence and audit:** complete symbolic arguments appear in this file,
  version 1. They were derived and checked by a separate agent during the
  current task. Parent review is recorded separately. These are internal
  proofs and inspections, not external review or novelty claims.
- **Authorization:** the current user's bounded Cartesian norm-symmetry
  cycle. This subtask used local reads and wrote only this new note. It ran
  no mathematical program, oracle or experiment: **zero charged evaluations**.
  It made no network, browser, connector, download, installation or remote
  Git call. The parent's separately controlled exact diagnostic is not a
  premise of any proof here.
- **Inherited tools:** the established norm action and
  [HR-1 return-to-image lemma](../2026-09-16-high-return/return-lemma.md),
  including repeated labels, projection fibers and exceptional outputs.
  No prior unsuccessful carrier or completed report is modified.

## 1. Fixed block and product definitions

Let \(R=\mathbb F_7\times\mathbb F_{19}\), and let
\(\chi_p:\mathbb F_p^\times\to\{1,-1\}\) be the quadratic character.
The fixed scalar carrier is

\[
D=\{(x_7,x_{19})\in R^\times:
             \chi_7(x_7)=\chi_{19}(x_{19})\}.
\tag{1}
\]

There are \(3\cdot9\) choices for each of the two common character signs,
so \(|D|=54\). This is a correlated subset of the two prime coordinates,
not the Cartesian product of two one-prime scalar subsets.

The polynomial \(\omega^2+\omega+1\) has distinct roots \(2,4\) at 7
and \(7,11\) at 19. At either prime, the norm-one group in the split
algebra consists of \((t,t^{-1})\), \(t\in\mathbb F_p^\times\). Thus

\[
G=H_7\times H_{19}\cong C_6\times C_{18},\qquad |G|=108.
\tag{2}
\]

Use the exact action and definition of \(r(z)\), for \(z\in D^2\), in
TP-L1. Here and below, squares of input sets mean all **ordered** pairs.

Fix this one block before the positive integer \(d\) grows. Define

\[
C_d=D^d\subset R^d,\qquad S_d=C_d^2\cong(D^2)^d,
\qquad \Gamma_d=G^d,
\tag{3}
\]
\[
F_d(x,y)=\bigl(Q(x_1,y_1),\ldots,Q(x_d,y_d)\bigr)\in R^d.
\tag{4}
\]

These are finite-algebra inputs and outputs. There is no identification of
\(C_d\) with a subset of \(\mathbb R\). Their exact sizes are
\(|C_d|=54^d\), \(|S_d|=2916^d\), and \(|\Gamma_d|=108^d\).
The product action applies its \(i\)-th multiplier to the \(i\)-th scalar
pair. Norm one holds at every prime in every block, so it preserves the
whole vector (4), not merely one aggregate norm.

## 2. TP-P1: exact product and stabilizer statements

**Theorem TP-P1(a) — PROVED.** For every \(d\ge1\) and every
\(s=(z_1,\ldots,z_d)\in S_d\), the set of legal return labels is exactly

\[
\mathcal R_d(s)=\prod_{i=1}^d\mathcal R_1(z_i).
\]

Consequently

\[
R_d(s)=\prod_{i=1}^d r(z_i),
\tag{5}
\]

and all the returned states counted in (5) are distinct. Every stabilizer
on \(S_d\) is trivial.

**Proof.** Membership in \(C_d^2\) is equivalent to membership in \(D^2\)
at every block. The allowed group is the full product \(G^d\). Hence a
tuple of multipliers is legal precisely when each component is legal,
proving the Cartesian equality and (5).

At one prime the split coordinates of an input are
\((x-\alpha y,x-\beta y)\), with \(\alpha\ne\beta\). At least one is
nonzero: otherwise \((\alpha-\beta)y=0\), whereas the scalar coordinate
\(y\) is nonzero. If \((t,t^{-1})\) fixes this state, any nonzero split
coordinate forces \(t=1\). This includes isotropic norm-zero states;
their other split coordinate can be zero without creating a stabilizer.
Both prime stabilizers, and then all block stabilizers, are therefore
trivial. \(\square\)

This product theorem assumes exactly (3). Extra global restrictions on
multiplier tuples, coupling between different blocks, or a scalar
realization are additional hypotheses; they cannot be inserted while
retaining (5) without proof.

### Uniform and typical returns

TP-L1 proves the complete one-block histogram

\[
(h_8,h_{10},h_{12},h_{18},h_{24},h_{26},h_{30},h_{54})
=(216,270,216,108,648,702,540,216).
\tag{6}
\]

In particular every block has \(r\ge8\). Equation (5) gives the uniform
statement

\[
R_d(s)\ge8^d\qquad(s\in S_d).
\tag{7}
\]

The exceptional set for the threshold \(e^{d\log8}\) is empty. This is
stronger than an exponentially small exceptional set at that threshold.
The elementary simultaneous-negation symmetry alone gives only \(2^d\)
returns; the stronger eight-per-block bound uses the correlated orbit
counts in TP-L1.

For the typical value, define \(p_k=h_k/2916\) and

\[
\mu=\sum_k p_k\log k
=\frac53\log2+\frac79\log3+\frac5{18}\log5
+\frac{13}{54}\log13>0.
\tag{8}
\]

Uniform choice from \(S_d\) is exactly uniform choice from \((D^2)^d\).
Thus the block states are independent with the displayed one-block law.
This independence is a consequence of the full product parameterization,
not an assumption about the two primes inside a block: their character
correlation remains intact.

**Theorem TP-P1(b) — PROVED.** For every fixed \(r_*\) with
\(0<r_*<\mu\), there is a fixed \(\delta>0\), depending only on that
choice and the block, such that for all \(d\ge1\),

\[
\#\{s\in S_d:R_d(s)<e^{r_*d}\}
\le e^{(2\log54-\delta)d}.
\tag{9}
\]

Moreover \(d^{-1}\log R_d\) converges to \(\mu\) under this uniform
law, with exponentially small probabilities of any fixed positive
deviation on either side.

**Proof.** For every real \(\theta\), the exact product identity is

\[
\frac1{|S_d|}\sum_{s\in S_d}R_d(s)^{-\theta}
=\left(\sum_k p_k k^{-\theta}\right)^d.
\tag{10}
\]

For \(\theta>0\), each state in the strict lower tail has
\(R_d(s)^{-\theta}>e^{-\theta r_*d}\). Therefore its fraction is at most

\[
\left(e^{\theta r_*}\sum_kp_k k^{-\theta}\right)^d.
\tag{11}
\]

The expression inside parentheses equals one at \(\theta=0\), and its
derivative there is \(r_*-\mu<0\). Since it is a finite sum of smooth
functions, some fixed \(\theta>0\) makes it strictly less than one.
Let \(\delta\) be minus its logarithm. Multiplying (11) by
\(|S_d|=e^{2d\log54}\) proves (9).

For the upper tail above \(\mu+\eta\), \(\eta>0\), apply the same
argument to \(R_d^{\theta}\). The derivative at zero of
\(e^{-\theta(\mu+\eta)}\sum_kp_k k^{\theta}\) is \(-\eta\).
The lower-tail argument also applies at \(\mu-\eta\); if this threshold
is nonpositive, the lower tail is empty because \(R_d\ge1\).
Thus both fixed deviations have exponentially small probability.
\(\square\)

This is an analytic all-depth theorem. Approximate logarithms printed by
the separate finite diagnostic are not used in (8)–(11).

## 3. Applying HR-1 inside the finite product model

Put \(a=\log54\). Input rates in actual block depth are exactly
\(\log|C_d|=ad\), with no thinning or projection loss **inside this
model**. The same fiber-counting implication in HR-1 applies to the
finite-valued function (4); its proof uses only finite fibers and distinct
returned states, not the nature of the codomain.

Uniform bound (7), with no exceptions or duplicate states, gives

\[
|F_d(S_d)|\le\frac{54^{2d}}{8^d}.
\tag{12}
\]

Thus the uniform finite-model certificate has positive gap \(\log8\)
against \(2a\). The pointwise reciprocal form of HR-1 gives the stronger
bound

\[
|F_d(S_d)|\le\sum_{s\in S_d}\frac1{R_d(s)}
=\left(\sum_k\frac{h_k}{k}\right)^d=154^d.
\tag{13}
\]

The equality is the product identity, and the last integer follows
directly from (6). In fact TP-L1 supplies the exact image:

\[
F_d(S_d)=Q(D,D)^d,\qquad |F_d(S_d)|=130^d.
\tag{14}
\]

For each selected vector of output values, choose one local pair
representing each coordinate and concatenate its two input vectors. This
proves both inclusions needed for the image equality in (14).

These are coordinatewise **finite-ring** image statements. They do not
give \(|Q(A,A)|\) for any subset \(A\subset\mathbb R\). No real
exponent \(c>0\) is extracted from (12)–(14).

For completeness, the explicit reciprocal moment in (10) is
\(\sum_kp_k/k=77/1458\). Therefore any fixed
\(r_*<\log(1458/77)\) yields (9) with the explicit choice
\(\delta=\log(1458/77)-r_*\), by taking \(\theta=1\) in (11).
The general moment argument also covers every \(r_*<\mu\).

## 4. TP-R1: finite exponent bounds all compatible scalar actions

Let

\[
\mathcal U_{\mathbb R}
=\{\alpha+\beta\omega:\alpha,\beta\in\mathbb R,
                         N(\alpha+\beta\omega)=1\},
\]

where \(\omega\) now has its usual nonreal complex value. This is the
group of actual real scalar norm-preserving multipliers, embedded in
\(\mathbb C^\times\). It acts on real scalar pairs by the established
Eisenstein coordinate action.

**Theorem TP-R1 — PROVED.** For every \(d\ge1\), any group homomorphism

\[
\phi_d:\Gamma_d\longrightarrow\mathcal U_{\mathbb R}
\tag{15}
\]

has image of size at most 18. Suppose in addition that a parameter-to-scalar
pair map \(\pi_d:S_d\to A_d^2\) is compatible with every legal local
return, in the precise sense

\[
\pi_d(T_gs)=T_{\phi_d(g)}\pi_d(s)
\qquad\bigl(s\in S_d,\ g\in\mathcal R_d(s)\bigr).
\tag{16}
\]

Then at most 18 distinct scalar pairs are returned from any \(s\).
If \(\nu_d(s)\) denotes the largest number of returning labels that
produce a single scalar pair, then

\[
\nu_d(s)\ge\left\lceil\frac{R_d(s)}{18}\right\rceil,
\qquad
\frac{R_d(s)}{\nu_d(s)}\le18.
\tag{17}
\]

If \(h_d\) is the largest fiber of \(\pi_d\), it also satisfies
\(h_d\ge R_d(s)/18\) for every \(s\). For a coordinatewise common
projection \(\pi_d=f_d\times f_d\), its maximum scalar-input fiber is
therefore at least \(\sqrt{R_d(s)/18}\).

**Proof.** Every element of \(G\) has order dividing 18, by (2), and the
same is true in every direct power \(\Gamma_d\). A homomorphism must
therefore satisfy \(\phi_d(g)^{18}=1\). The nonzero polynomial
\(X^{18}-1\) has at most eighteen roots in \(\mathbb C\), proving the
image bound. This argument permits arbitrary real coefficients; passing
to a larger number field with a real scalar embedding cannot alter it.

Compatibility (16) places every projected return among the images of the
single pair \(\pi_d(s)\) under these at most eighteen scalar actions.
The local return labels yield \(R_d(s)\) distinct parameter states by
TP-P1(a). Pigeonholing their projections proves (17) and the maximum-fiber
bound. If the pair map is \(f_d\times f_d\), its maximum pair fiber is
the square of the maximum individual-input fiber, proving the last
assertion. If the projected pair is zero, all scalar multipliers fix it;
there is then at most one distinct return, an even stronger loss.
\(\square\)

### Exact failed scope and rate charge

For any unbounded sequence of real scalar carrier sizes, a return count
bounded by 18 has exponent zero. HR-1 cannot turn the exponential local
label count into a real positive return exponent under (15)–(16): its
repeated-action correction is at least the exponential loss in (17).
This is a **PROVED obstruction to this compatible scalar realization**.

It is not legitimate to use the local \(54^d\) input count as the real
input count without proving the projection cardinality. Nor does a large
maximum projection fiber alone establish an upper bound on the number of
distinct real inputs. The direct distinct-return bound of eighteen is
sufficient for the stated certificate obstruction, regardless of that
unknown input size.

This theorem requires a genuine homomorphism (15) and compatibility (16).
A choice of characteristic-zero lifts whose products agree only modulo
primes need not satisfy either condition. The theorem makes no universal
claim about such lifts, other return actions, or unrelated constructions.
For them, exact real norm preservation, legal scalar returns, carries,
denominators and projection costs remain to be proved; unknown costs are
not zero. No such replacement construction is proposed here.

## 5. TP-R2: zero-preserving norm factorization collapses all inputs

This is a separate obstruction, with different explicit hypotheses.
It must not be confused with stabilizers of the nonzero local states.

**Theorem TP-R2 — PROVED.** Suppose there are maps

\[
f_d:C_d\to\mathbb R,\qquad
\Psi_d:Q(D,D)^d\to\mathbb R,
\]

such that \(\Psi_d(0)=0\) and

\[
Q(f_d(x),f_d(y))=\Psi_d(F_d(x,y))
\qquad\text{for every }(x,y)\in C_d^2.
\tag{18}
\]

Then \(f_d\) is identically zero.

**Proof.** The two split roots at each prime are squares: they have order
three, and \(3\) divides both \((7-1)/2\) and \((19-1)/2\).
Hence the four root-ratio choices

\[
\rho\in\{2,4\}\times\{7,11\}
\]

have character \((+,+)\) and lie in \(D\). This set \(D\) is a
multiplicative subgroup of \(R^\times\), since it is the kernel of
\((a,b)\mapsto\chi_7(a)\chi_{19}(b)\). For every \(y\in C_d\),
choose any of the four ratios at each block and set \(x_i=\rho_i y_i\).
Then \(x\in C_d\), and every coordinate norm equals
\(y_i^2(\rho_i^2+\rho_i+1)=0\). Thus \(F_d(x,y)=0\).

Equation (18) gives \(Q(f_d(x),f_d(y))=0\). Over \(\mathbb R\),
\(Q(a,b)=(a+b/2)^2+3b^2/4\) vanishes only when \(a=b=0\).
In particular \(f_d(y)=0\). Since every \(y\) has such a partner,
the whole input set collapses. \(\square\)

The exact count is \(54^d4^d=216^d\) ordered zero-norm pairs, as also
follows from TP-L1. Their relative frequency is

\[
\frac{216^d}{2916^d}=\left(\frac2{27}\right)^d.
\tag{19}
\]

If all of these pairs are permitted as exceptions to (18), the collapse
argument no longer applies. Their pair count would have to be charged as
\(e^{(2\log54-\log(27/2))d}\); it is exponentially sparse. Thus TP-R2
alone does not rule out a realization allowed to discard these pairs or
one with \(\Psi_d(0)\ne0\). TP-R1 has its separate group-compatible
hypotheses and does not rely on zero-norm outputs.

## 6. Fully charged product and realization ledger

All rates here use actual block depth \(d\). Input/cardinality statements
are labeled by their ambient system.

| Gain or cost | Exact accounting | Status |
|---|---|---|
| Formal input lower and upper count | Exactly \(54^d\); \(a=B=\log54\) | PROVED |
| Carrier restriction at the two primes | \(D\) has 54 of the 108 units of \(R\); the two-coordinate restriction is already charged by the exact \(2916^d\) pair count | PROVED |
| Same-set and all-pair coverage | Exactly \((D^d)^2\); no rich subset replaces that square | PROVED |
| Within-block correlation | Equality of characters is imposed for each scalar; TP-L1 counts the resulting joint return condition | PROVED |
| Between-block structure | Full Cartesian carrier and full product group; no extra global constraint | PROVED, hypotheses of TP-P1 |
| Local stabilizers and labels | All stabilizers trivial, including isotropic pairs; no repeated parameter states | PROVED |
| Uniform local return rate | At least \(8^d\), rate \(\log8\), with no exceptional pairs | PROVED finite model |
| Typical local return rate | \(\mu\) in (8), with exponential tails (9) | PROVED finite model |
| Formal image support | HR-1 gives \(154^d\); the exact vector image is \(130^d\) | PROVED finite model |
| Formal signed gap | Reciprocal certificate: \(2\log54-\log154>0\); exact modular image: \(2\log54-\log130>0\) | PROVED finite model only |
| Real projection count | No real scalar carrier with count \(54^d\) is supplied. Its cardinality cannot be inferred from formal states | OPEN outside the failed realizations |
| Compatible-action duplicate loss | At most 18 realized scalar actions; \(\nu_d(s)\ge R_d(s)/18\). Corrected return rate is zero | FAILED realization under TP-R1 |
| Projection fibers | Maximum pair fiber at least \(R_d(s)/18\), if compatibility is demanded. This is not silently assigned multiplicity one | PROVED |
| Zero-preserving full norm factorization | Entire input projection is zero under (18); no growing real set remains | FAILED realization under TP-R2 |
| Zero-norm exception alternative | \(216^d\) pairs if all such pairs are omitted; this defeats TP-R2's premise and must be paid separately | PROVED exact exception count |
| Field degree, discriminant and regulator | No characteristic-zero tower or lattice estimate is constructed or assumed. TP-R1's exponent bound holds even with arbitrary real multiplier coefficients | No favorable cost assumed |
| Moduli, denominators, heights and carries | The finite model has fixed local moduli; a scalar lift has no proved denominator/height/carry ledger. Such costs are unresolved outside TP-R1/TP-R2 | OPEN, not zero |
| Local sparsity and residue packing | No local density is multiplied by an unproved global volume; no packing theorem supplies a real support bound here | Not invoked |
| Real positive signed rate | None survives the exact compatible action: exponential labels collapse to a constant number of scalar returns | FAILED for TP-R1 architecture |
| Difference-set or affine transfer | Not investigated because no homogeneous real carrier survives these realization gates | Outside the authorized next stage |

## 7. Disposition and evidence limits

The product construction has genuine positive return entropy in its finite
algebra. Exact tensorization and its exceptional tails are proved, not
inferred from several product sizes or a large arithmetic mean.

Its direct group-compatible realization as real scalar norm-one actions
fails by TP-R1; its exact zero-preserving full norm factorization fails by
TP-R2. The appropriate scope is **LOCAL GO / GLOBAL FAIL for these
specified exact realizations**. This does not claim that all ways of using
two-prime correlation fail. No real power-saving construction, additive
difference-set exponent or affine \(Q+x\) transfer is established.

This note adopts no replacement conjecture and starts no additional carrier
search. The sole retained next obligation is the existing T03-O4/RC15/4,
stated precisely in the parent report §10; it was not pursued here.
