# Cross-block returns and full-fiber obstructions

6 October 2026 · T03 · strictly offline · final bounded-cycle report.

**PROVED:** explicit mixed-parity multipliers produce returns missed by
the previous cyclic action group. **FAILED IN STATED SCOPE:** enlarging
the action family cannot rescue either tested dyadic carrier. Both now
have proved quadratic actual-image size. The unrestricted target for
\(Q(x,y)=x^2+xy+y^2\) remains **OPEN**.

## What the old obstruction restricted

**Statement — PROVED, inherited.** In the
[previous composition proof](../2026-09-30-multiscale-packing/composition.md),
§4 used \(u=\zeta_m^j\) to conclude \(\sigma(u)=(-1)^j u\).
Because \(\sigma\) fixes \(\omega\), both coefficients of
\(u=a+b\omega\) lie in the same eigenspace of \(\sigma\).
The four-line lemma in §5 explicitly assumes that same coefficient
restriction, even when it allows non-torsion actions.

**Meaning.** A fractional norm-one multiplier with mixed coefficient
parities is outside that proof. The old selected-return bounds alone
did not imply an actual-image lower bound.

**Consequence.** This cycle studies full polynomial fibers first. The
stronger conclusions below are new proofs, not reinterpretations of the
30 September checkpoint. That checkpoint remains unchanged.

## Explicit cross-block identities

**Statement — PROVED, XB-A1–A3.** For \(p=(x,y)\ne0\), put
\(z=x-\omega y\). The explicit multiplier
\[
u_p=-\omega\frac{\bar z}{z}
=\frac{y-\omega x}{x-\omega y},\qquad N(u_p)=1,
\]
sends \((x,y)\) to \((y,x)\). On nonzero opposite-parity sources,
\(u_p\notin\mu_m\). On the mixed carrier, put \(t=\gamma_0\) and
\(b=c_Js_1\), with \(J\subseteq\{1,\ldots,d-1\}\) and
\(c_J=\prod_{\ell\in J}(1+\gamma_\ell)\). A single multiplier gives
\[
v_t=\omega\frac{t-\omega}{1-\omega t},\qquad
M_{v_t}(b,tb)=(b,-(1+t)b).
\]
Both target coordinates belong to the same mixed carrier: \(tb=c_Js_2\)
and \((1+t)b\) is in its other amplitude block.

**Meaning.** There are genuine new cross-block targets. The swap completes
the first carrier's obstructed fibers from two to four returns. The fixed
Vieta multiplier has a certified source domain on one real line, hence
at most \(n-1\) nonzero sources. Formal product addresses are deduplicated.

**Consequence.** This is a constant improvement, not a positive return
exponent. The finite deduplicated action family and exact source domains
are specified in [actions](actions.md); incidental returns are controlled
by the full-fiber theorems below, not by certificate-domain counts.

## Full fibers decide both finalists

Let \(d\ge1\), \(m=6\cdot2^d\), \(\theta=2\pi/m\),
\(S_d=\{-2\sin(r\theta):0\le r<m\}\), and
\(\gamma_\ell=2\cos(2^\ell\theta)\). The unchanged carriers are
\[
A_d^{(0)}=\bigcup_{J\subseteq\{0,\ldots,d-1\}}
\left(\prod_{\ell\in J}\gamma_\ell\right)S_d,
\quad
A_d^{(1)}=\bigcup_{J\subseteq\{0,\ldots,d-1\}}
\left(\prod_{\ell\in J}(1+\gamma_\ell)\right)S_d.
\]
In each row below \(n\) denotes that carrier's actual cardinality.

| Carrier | PROVED full-fiber population | PROVED actual-image lower bound |
|---|---|---|
| Cosine products, XB-F1 | At least \(4(n-1)^2/9\) pairs have full fiber exactly4 | \((n-1)^2/9\) |
| Mixed products, XB-F2 | At least \((n-1)^2/2-4(n-1)\) pairs have full fiber at most48 | \((n-1)^2/96-(n-1)/12\) |

**Statement — PROVED.** The bounds hold at every depth. Together with
the trivial upper bound \(n^2\), they imply \(|Q(A_d^{(i)},A_d^{(i)})|
=\Theta(n^2)\) for both families. The input bounds are
\(3\cdot2^d+1\le |A_d^{(0)}|\le3\cdot4^d+1\) and
\(6\cdot2^d+1\le |A_d^{(1)}|\le3\cdot4^d+1\). No limit \(\lambda\)
is assumed or proved.

**Meaning.** For the first carrier, conjugation separates \(xy\) from
\(x^2+y^2\), fixing the full fiber to the two orders and simultaneous
signs. For the second, a target on two different subfield lines must
satisfy two nonproportional positive quadratic equations, hence has at
most four solutions per ordered line pair. There are twelve such line
pairs. Same-line targets are excluded outside two explicit output lines;
at most \(4(n-1)\) independent source pairs land on those exceptional
output lines. See the complete [full-fiber proofs and audit](audit.md)
and [six-block calculation](composition.md).

**Consequence — FAILED IN STATED SCOPE.** For either carrier, every choice
of norm-one actions, including arbitrary fractional algebraic actions,
has a quadratic-sized set below \(n^\varepsilon\) for every fixed
\(\varepsilon>0\) eventually. No fixed \(\varepsilon,\delta>0\)
satisfy the requested tail, and no fixed \(c>0\) works for these carriers.
There is no rectangular intermediate set, so \(\eta\) is inapplicable.
The general real quadratic target, DC-O1, ML-O1, ARG/TCRC and RC15/4 remain
**OPEN**; HR-N1 remains **DISPROVED**.

## Budget and completion

Both finalists failed through complete full-fiber proofs, so the stop rule
was met before any scout. One action mechanism, two unchanged carrier
finalists, three specialists, zero mutations, zero mathematical program
runs. Used **0 of2,000,000 charged evaluations** and **0 of600 CPU seconds**;
20% was reserved for verification. These are program-accounting figures,
not model-token or credit usage.

The [ledger](ledger.md), [verification record](verification.md),
[machine state](state.json) and [hash manifest](manifest.json) contain
the arithmetic audit, sources, exact counter policy and checks. Historical
sources remain intact; handoffs are dated additions; nothing is committed.

## One next obligation

**XB-O1 / OPEN — projective spreading within the prescribed ML-O1 model.**
For \(m_k=6\cdot7^{k-1}\), \(t_k=8\cdot7^{k-1}\), let
\(K_k=\mathbb Q(\zeta_{m_k})\), \(K_k^+=K_k\cap\mathbb R\).
Construct explicit nonzero \(c_{k,j}\in K_k\), \(1\le j\le t_k\),
with disjoint cosets \(c_{k,j}\mu_{m_k}\), whose same-set coordinate
completion \(A_k\) satisfies \(n_k=|A_k|\to\infty\) and, for some fixed
\(\kappa>0\),
\[
\max_{\substack{F\subset K_k^+\,;\,[K_k^+:F]=2\\
\alpha\in(K_k^+)^\times}}
\bigl|(A_k\setminus\{0\})\cap\alpha F\bigr|
\le n_k^{1-\kappa}
\quad(k\ge2).
\]
Here the completion is precisely the union of both real coordinate
projections of \(\bigcup_j c_{k,j}\mu_{m_k}\) under
\(\phi^{-1}(z)=(x,y)\), \(z=x-\omega y\). This is one concrete
amplitude-and-scalar-count obligation; no candidate for it was searched
after the stop rule. It targets the bounded-line concentration exposed by
the proofs. It is not asserted necessary for every solution, equivalent
to ML-O1, or sufficient for power saving; cross-block full-fiber growth
would still require proof. No replacement positive conjecture is adopted.
