# Bottom line

- **Mechanisms tested:** cyclotomic trace domains, a full-residue modular gadget, and denominator-adapted rational carriers. Three mechanisms, with no reopening of the frozen cube-root, tensor or moving-pole families.
- **Identity-only pairs cease to be the obstruction.** The cyclotomic carrier has none; the explicit rational action family has only the origin. Nevertheless both have quadratic-size polynomial-threshold bad sets.
- **Typical polynomial returns: FAILED for these real realizations.** In the cyclotomic family almost every pair has exactly two returns. A fixed fraction of the rational carrier has only subpolynomially many returns under any actions. The strong modular tail does not lift to the proposed real carrier.
- **Coordinate overlap holds:** every concrete carrier uses $X=Y$.
- **DC-R1 gives no positive $c$ this cycle.** DC-O1, the quadratic target, ARG/TCRC and RC15/4 remain OPEN; HR-N1 remains DISPROVED.
- **One next obligation:** construct globally compatible real return domains with polynomial overlap multiplicity on almost every pair. The exact obligation appears at the end.

## RETURN-TAIL FAIL

For the explicit growing cyclotomic action family, the chain is

$$\boxed{\text{many global actions}
\xrightarrow{\mathrm{PROVED}}\text{overlapping domains}
\xrightarrow{\mathrm{PROVED}}\text{small identity-only tail}
\xrightarrow[\text{this carrier}]{\mathrm{FAILED}}\text{polynomial returns}
\xrightarrow[\text{DC-R1 hypotheses}]{\mathrm{PROVED}}\text{power saving}.}$$

The non-sign domains overlap on a small set; they do not distribute their
multiplicity across the square. The general real return-tail construction
remains **OPEN**. The last arrow is the already proved sufficient
implication, whose hypotheses are not achieved here.

**Offline return-tail cycle · 21 September 2026 · T03.** Fixed polynomial
$Q(x,y)=x^2+xy+y^2$. No external result, literature search, or novelty
claim. The [preceding correlated checkpoint](../2026-09-21-correlated-dc-o1/README.md)
and its failures remain frozen. The detailed proofs, arithmetic ledgers,
raw distributions and internal review records are companions to this
concise report. No new global compression theorem was sought.

## 1. Structural result: exact domains and a sufficient tail criterion

### Statement

**PROVED — RT-G1–RT-G3.** For $u=a+b\omega$ of norm one,
$\omega=(-1+i\sqrt3)/2$, and $\Omega=A^2$,

$$D_u=\{(x,y)\in A^2:ax+by\in A,
\ -bx+(a-b)y\in A\},$$
$$M_u(D_u\cap D_v)
=\Omega\cap M_u\Omega\cap M_{vu^{-1}}^{-1}\Omega.$$

Off the origin, assume $N=|\Omega\setminus\{0\}|>0$, and put

$$S_1=\sum_u|D_u\setminus\{0\}|,\qquad
S_2=\sum_{u,v}|(D_u\cap D_v)\setminus\{0\}|,$$
$$\mu=S_1/N,\qquad V=S_2-S_1^2/N.$$

For $t<\mu$, with $\zeta=1$ if the origin is present and zero otherwise,

$$B(t)\le\zeta1_{t>1}+\frac{V}{(\mu-t)^2}.$$

Thus $\mu\ge(1+\kappa)n^\varepsilon$ and
$V/(N\mu^2)=O(n^{-\delta})$, for fixed $\kappa>0$ and
$0<\delta\le2$, suffice for the required lower tail. These estimates
remain candidate-specific premises.

### Meaning

Two domain families can overlap heavily on the same small set. Their
mean return count alone does not control the lower tail; the displayed
intersection and variance formulas retain the missing distribution
information. On a sign-closed set, the two actions $\pm1$ already
remove every nonzero identity-only pair.

### Consequence

This supplies the requested structural criterion, with exact stabilizer
handling at zero. It proves no construction by itself and is not a new
image-compression theorem. Proof: [geometry.md](geometry.md).

## 2. Cyclotomic traces: the additional domains coincide

### Statement

**PROVED — CY-1–CY-3.** Let $p\ge11$ be a prime with
$p\equiv2\pmod3$, $\xi=e^{2\pi i/p}$, and

$$U=\{\pm\omega^j\xi^r:j=0,1,2,\ r\in\mathbb Z/p\mathbb Z\},
\qquad A=X=Y=\{v+v^{-1}:v\in U\}.$$

Then $|U|=6p$, $n=|A|=3p+1$, and $0\notin A$.
Identify pairs with $z=x-\omega y$ and define

$$E=\{(x,y)\in A^2:x-\omega y\in(1+2\omega)U\}.$$

Its size is exactly $6p$, and the **entire actual domains** are

$$\boxed{D_1=D_{-1}=A^2,\qquad D_u=E\quad(u\in U\setminus\{\pm1\}).}$$

Consequently

$$\boxed{R(p)=2+(6p-2)1_E(p),\qquad I=\varnothing.}$$

For every fixed $\varepsilon>0$, eventually
$B_\varepsilon\ge n^2-6p$. For $0<\varepsilon\le1$ this is equality;
if $\varepsilon>1$, eventually every pair is bad.

### Meaning

All $6p$ actions are genuine whole-scalar norm isometries, and each pair
returns at least twice. However, every extra domain is the same linear-size
set. There is no spread of the rich-return population over the square.

### Consequence

**FAILED actual return-tail witness**, with the full selected action group
analyzed. The proof uses sparse cyclotomic coefficient equality, not a
formal tensor count. It does not rule out other infinite-order norm actions
or establish an image lower bound for this algebraic carrier.
Proof and complete exact distribution:
[cyclotomic-domains.md](cyclotomic-domains.md).

## 3. Full residue signatures: a modular tail with a failed real lift

### Statement

**PROVED — MG-1–MG-4, with the real lift FAILED.** Work over
$R_k=\mathbb Z/7^k\mathbb Z$, with scalar alphabet all of $R_k$ and
$n=7^k$. The two compatible roots $\lambda,\mu$ of $T^2+T+1$ give
split coordinates

$$s=x-\lambda y,\qquad t=x-\mu y,\qquad Q=st.$$

The $6\cdot7^{k-1}$ distinct norm-one actions are
$(s,t)\mapsto(hs,h^{-1}t)$ for $h\in R_k^\times$. Their composition
law is exact in this ring. At minimum valuation $m<k$ the distinct-target
count is $6\cdot7^{k-1-m}$ and the stabilizer has size $7^m$.
Zero has one target. For $0<\varepsilon<1$,

$$B_\varepsilon^{\rm mod}\le(49/36)n^{2\varepsilon}.$$

In particular the modular exponents $\varepsilon=1/2$, $\delta=1$
are proved, and every nonzero diagonal residue has nontrivial choices.

For the real sign-closed lift with the six actual unit actions, the
identity-only set is again exactly the origin. The centered integer lift $A=\{-(n-1)/2,\ldots,(n-1)/2\}$ fails:
for $b=(n-1)/2$, reducing the action $\omega(b,b)=(b,-2b)$ into the
interval gives $(b,1)$, but

$$Q(b,1)-Q(b,b)=-n(b-1)\ne0.$$

The retained HR-4A/B integer-fiber bound moreover proves
$B_\varepsilon^{\rm real}=n^2$ eventually for every fixed
$\varepsilon>0$, under any actual norm-preserving actions on this lift.

### Meaning

The full residue signature genuinely removes the former diagonal locking
and has a proved local-to-global tail. Its norm identity is modular.
The representative map introduces an integer carry in the norm and does
not preserve real polynomial values.

### Consequence

This is **not** a real DC-O1 witness. A composition-preserving rational
lift also has at most six distinct actions, since finite-order rational
Eisenstein norm-one elements are exactly the six units. No integer
interval experiment or broad prime search was rerun. Complete local
return table, valuation histogram and lift audit:
[modular-gadget.md](modular-gadget.md).

## 4. Rational denominator states: small identity-only set, quadratic bad tail

### Statement

**PROVED — RT-D1–RT-D3.** Let $H=12L$, $L\ge10{,}000$, and

$$A_H=X_H=Y_H=\{a/b:|a|\le H,\ 1\le b\le H,\ \gcd(a,b)=1\}.$$

Then $H^2/288\le n_H\le3H^2$. A concrete action family is the
deduplicated set $U_H=\{\pm\bar\beta/\beta:0\ne\beta=m+k\omega,
\ |m|,|k|\le H\}$. Its identity-only set is exactly the origin.

There is nevertheless a set $\mathcal B_H$ with

$$|\mathcal B_H|\ge n_H^2/400{,}000$$

on which **every possible** selected action family has at most
$n_H^{o(1)}$ returns, uniformly. Hence for every fixed $\varepsilon>0$,
eventually $B_\varepsilon\ge n_H^2/400{,}000$.

The exact denominator mechanism is: for reduced sources with coprime
$b,d>H/2$, put $K=bd$ and
$N=a^2d^2+abcd+c^2b^2$. An equal-norm target must have denominator
least common multiple in $\{K,2K,3K\}$, and its full fiber is bounded by

$$6\sum_{t=1}^3\tau(tK)^2\tau(t^2N)=H^{o(1)}.$$

### Meaning

Allowing many denominator states supplies two sign returns at every
nonzero source but does not supply a polynomial tail. A fixed fraction
of pairs has large coprime denominators, leaving too few denominator
allocations for equal-norm targets.

### Consequence

**FAILED all-action return-tail witness for this rational-height family.**
The complete fiber proof also independently gives
$|Q(A_H,A_H)|\ge n_H^{2-\rho}$ for every $\rho>0$, eventually along
$H=12L$. This image conclusion is proved for this family; it is not
inferred merely from a failed return certificate and says nothing against
the general real target. Proof: [denominator-domains.md](denominator-domains.md).

## 5. Exact finite scouting

**EXPERIMENTAL — exhaustive exact cyclotomic arithmetic.** The two
predetermined cases test every source and every selected action after the
scalar identity and domain theorem were independently reviewed. The
threshold is $n^{1/4}$. Geometric means alone are rounded for display.

| $n$ | $\lvert X\triangle Y\rvert$ | $\lvert U\rvert$ | Identity-only pairs | Median $R$ | Geometric mean $R$ | Maximum $R$ | $B_{1/4}$ | Full $\lvert Q(A,A)\rvert$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 34 | 0 | 66 | **0** | 2 | 2.441896 | 66 | 1090 | 290 |
| 52 | 0 | 102 | **0** | 2 | 2.319759 | 102 | 2602 | 677 |

Full return, stabilizer and image-fiber histograms, individual domain sizes
and exact mean expressions are in the
[frozen summary](../../../examples/2026-09-21-return-tail.json).
The modular gadget has an analytic exact table in its companion; it is
not reported as a real experiment. The rational carrier is rejected by
its uniform theorem before any finite search. No failed family was
expanded after these fixed checks.

## 6. Rate and failure ledger

| Mechanism | Inputs and overlap | Return / bad-tail accounting | Exact disposition |
|---|---|---|---|
| Cyclotomic traces | $n=3p+1$, $X=Y$ | $R=2$ on $n^2-6p$ pairs; no identity-only pairs | Actual selected-action tail FAILED |
| Full residue gadget | $n=7^k$, $X=Y$ in the finite ring | Modular $\varepsilon\in(0,1)$ and $\delta=2-2\varepsilon$ | Modular tail PROVED; canonical real lift FAILED |
| Rational height carrier | $n=\Theta(H^2)$, $X=Y$ | Only zero identity-only; at least $n^2/400{,}000$ pairs below every fixed polynomial threshold | All-action tail FAILED; family-specific image lower bound separately PROVED |

The cyclotomic elements are algebraic integers and the selected actions
are roots of unity; their degree grows and all embeddings/coordinate
identifications are justified in the companion. No discriminant,
regulator or lattice-volume saving is assumed. The modular model charges
its representative-map failure explicitly. Rational scalar denominators
vary, but the target least-common-multiple classes and their divisor
multiplicities are all counted. Every zero, stabilizer, branch and missing
pair is retained in these ledgers.

The [verification record](verification.md) separates internal proof audits,
exact research computation and repository checks. Source identities,
commands, budgets and inherited edits are recorded there. Historical
checkpoints are preserved, with dated handoff addenda only; nothing is
committed. No external result or novelty claim is made.

## 7. One next mathematical obligation

**OPEN — real correlated return-tail witness.** Construct explicit
$X_d,Y_d,U_d$ with $n_d=|X_d\cup Y_d|\to\infty$,
$|X_d\triangle Y_d|=O(n_d^{1-\eta})$, and $n_d^\varepsilon$ distinct
genuine real norm-preserving returns into $X_d\times Y_d$ outside
$O(n_d^{2-\delta})$ pairs, for fixed $\varepsilon,\eta,\delta>0$.
The domain multiplicity must be distributed over almost every pair, not
only eliminate identity-only states. The established DC-R1 then gives
any strict $c<\min(\varepsilon,2\eta,\delta)$; no alternative global
compression theorem or barred carrier search is adopted here.
