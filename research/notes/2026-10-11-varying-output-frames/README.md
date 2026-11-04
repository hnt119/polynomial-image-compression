# A closed output triangle without growing frame reuse

T01 · 11 October 2026 · version 1 · offline research.
Fixed polynomial: P(x,y)=(x-y)^3+x+y; both coordinates use the same real set.

## Verdict

**PROVED:** one output-first, three-output junction closes inside its existing scalar pool. Its long-edge frame adds two genuinely new cross-block pairs and no scalar. But the prescribed overlapping-junction continuation has
\[
N=4m,\qquad Q=6m-2,\qquad Z=m+1,
\qquad |P(A_m,A_m)|\ge N^2/16 \quad(m\ge2).
\]
It is therefore **FAILED as a power-saving candidate**, and is stopped. Selected fibers have at most six pairs and at most two distinct rows per output. This does not improve the earlier N^(4/3) prescribed-pair benchmark.

The failure is not just a bad choice of equal output gaps: keeping this junction's two specified outer-row identifications forces those gaps to be equal. The obstruction is scoped to this role pattern. **The unrestricted varying-output problem and T01 remain OPEN.** MS-C1 and the frozen fixed-output results are unchanged.

Throughout, \(E\) is the union of actual ordered row–column pairs in the specified frames and \(A\) is their scalar-coordinate union. We count \(N=|A|\), \(Q=|E|\), \(Z=|P(E)|\), and \(B=N^2-Q\), after deduplication. Each uncovered pair costs at most one further output, so \(|P(A,A)|\le Z+B\).

## 1. Output-first rule and simultaneous compatibility

**PROVED — VO-C1. Meaning.** The three frames must agree at actual scalar endpoints; solving their width equations separately is insufficient.

**Statement.** Before choosing scalars, prescribe outputs \(-\Delta,0,\Delta\), \(\Delta>0\), and frames on all three output edges. Write
\[
C(x)=8x(1-2x^2),\quad \delta=\Delta/4,
\quad C(h)=\Delta,\quad C(H)=2\Delta,
\]
\[
s^2=1-3h^2,\quad S^2=1-3H^2,
\quad h,s,H,S>0,\quad h\ne s,\ H\ne S.
\]
The short-frame centers are \(-\delta,+\delta\); the long-frame center is zero. The selected gluing rule identifies each long-frame row with the outside row of the corresponding short frame:
\[
-H=-\delta-h,\qquad H=\delta+h.
\tag{1}
\]
Thus this candidate requires **simultaneously**
\[
H=3h-4h^3,\qquad C(H)=2C(h),
\]
not just three individually valid frames.

**Proof.** Existence of the long edge forces \(\Delta\le8/(3\sqrt6)\). The short gap then has a unique admissible width \(h<1/6\), using the frozen width function within its stated domain. Substituting (1), with \(t=h^2\), gives
\[
(2t-1)(64t^3-112t^2+52t-1)=0.
\tag{2}
\]
There is exactly one admissible root, with \(1/50<t<1/49\). The factor \(2t-1\) is inadmissible. The other positive long-edge width is real but fails (1); it is not silently discarded. Complete branch and sign arguments are in [the compatibility appendix](compatibility.md).

**Scope.** The output pattern and endpoint roles were fixed before solving (2). The resulting algebraic gap is forced by that system; outputs are not labels assigned after arbitrary scalar choices.

## 2. Worked junction: the extra frame costs no new scalar

**PROVED — VO-C2. Meaning.** Two otherwise disjoint short frames interact through a frame closing entirely inside their union.

Put
\[
h=\sqrt t>0,\quad \rho=2-4t,\quad\delta=h\rho,
\quad H=h(\rho+1),\quad S=h(\rho+3),\quad s=h(2\rho+3),
\]
and \(p=h(\rho-1)\), \(v=3H\). The scalar union is
\[
A=\{\pm p,\pm H,\pm S,\pm v\},\qquad 0<p<H<S<v.
\]

| Frame | Rows | Columns | Row outputs, lower then upper |
| --- | --- | --- | --- |
| Left short | \(-H,-p\) | \(-v,S\) | \(-\Delta,0\) |
| Right short | \(p,H\) | \(-S,v\) | \(0,\Delta\) |
| Long | \(-H,H\) | \(-S,S\) | \(-\Delta,\Delta\) |

**Proof.** Equation (2) gives both conic identities and \(s=2H+h\), \(S=H+2h\). The first two scalar blocks are disjoint. The long frame repeats \((-H,S)\) and \((H,-S)\), while adding exactly \((-H,-S)\) and \((H,S)\). Thus
\[
N=8,\quad Q=10,\quad Z=3,\quad B=54,\quad |P(A,A)|\le57.
\]
The selected fiber sizes are \(3,4,3\); the outside outputs still have only one row each. **Scope:** this is finite compatibility, not asymptotic progress.

## 3. The prescribed extension and its full ledger

**PROVED — VO-C3. Meaning.** Repeat the same local rule on overlapping output triples, then deduplicate every scalar and pair.

**Statement.** For each integer \(m\ge2\), prescribe labels \(z_j=j\Delta\), \(0\le j\le m\). Take short frames
\[
F((2j+1)\delta,h,s),\quad 0\le j<m,
\]
and the closing long frames
\[
F(2(j+1)\delta,H,S),\quad 0\le j<m-1.
\]
The latter join output labels \(j\Delta\) and \((j+2)\Delta\).

**Proof.** The short-frame scalar blocks have the four forms
\[
h((2j+1)\rho\pm1),\quad
h((2j+3)\rho+3),\quad h((2j-1)\rho-3).
\]
The number \(u=4t\) satisfies the irreducible cubic
\(u^3-7u^2+13u-1=0\): its only possible rational roots are \(\pm1\), and neither is a root. Hence \(\rho\) is irrational. Equality of two displayed scalars forces equality of their integer coefficients of \(1,\rho\), proving \(N=4m\). Each long frame lies in two neighboring short blocks and adds exactly two new pairs. Every prescribed output occurs, proving the ledger:

| Quantity | Exact value |
| --- | --- |
| Scalars \(N\) | \(4m\) |
| Distinct controlled pairs \(Q\) | \(6m-2\) |
| Controlled outputs \(Z\) | \(m+1\) |
| Uncovered pairs \(B=N^2-Q\) | \(16m^2-6m+2\) |
| Safe entire-image bound \(Z+B\) | \(16m^2-5m+3\) |
| Endpoint reuse \(2Q/N\) | \(3-1/m\) |
| Selected fiber average \(Q/Z\) | \(6-8/(m+1)\) |
| Coverage \(Q/N^2\) | \((6m-2)/(16m^2)\) |

**Scope.** Both reuse averages stay bounded and coverage tends to zero. This is a proved failed continuation, not a translated-ladder construction offered as progress. No larger instance or alternative carrier is pursued after its obstruction is established.

## 4. Why this continuation cannot be repaired inside its pool

**PROVED — VO-C4. Meaning.** The full square already contains a positive-density injective subgrid.

One of the four scalar progressions has \(m=N/4\) points and step \(D=2\delta\), with
\[
D^2=48t^2-36t+1\notin\mathbb Q.
\]
For \(x=a+Di,y=a+Dj\),
\[
(P(x,y)-2a)/D=D^2(i-j)^3+i+j.
\]
Equal outputs force equal differences and sums because \(D^2\) is irrational, hence identical ordered pairs. Therefore \(|P(A_m,A_m)|\ge m^2=N^2/16\). This imports the precise irrational-spacing clause of GS-A4 and reproduces its elementary proof here.

Moreover any pair in any admissible frame with widths \(u,v>0\), \(3u^2+v^2=1\), obeys \(|x-y|\le u+v\le2/\sqrt3\), by Cauchy–Schwarz. The root interval gives \(D^2=48t^2-36t+1>685/2401>1/4\). Hence an interval of length \(4/\sqrt3\) contains at most five points of each of the four scalar progressions. For each first coordinate, there are therefore at most twenty possible second coordinates. Adding **all** complete frames available inside this same pool still controls at most \(20N\) pairs. No extra-frame enumeration is needed.

**PROVED — VO-C5. Meaning.** Changing just the two adjacent output gaps does not escape this chosen endpoint pattern. For gaps \(\alpha=C(h)>0\), \(\beta=C(k)>0\), the same outer-row identifications require
\[
H=h+\beta/4=k+\alpha/4,\qquad C(H)=\alpha+\beta.
\]
They imply \(h=k\), hence \(\alpha=\beta\). If \(h\ne k\), put \(p=h+k\), \(r=hk\). The equations give \(r=p^2-1/4\), \(H=4p^3\), and \(4H^3=p\), forcing \(p=1/2,r=0\), contrary to positive widths. The [appendix](compatibility.md) records the elimination.

**Scope.** The image lower bound and additional-frame bound concern this scalar family; the unequal-gap restriction concerns exactly the two row identities. None is a universal obstruction to varying-output networks.

## 5. Exact finite audit

**EXPERIMENTAL — VO-X1:** the independent referee evaluated only the predeclared cases \(m=2,3,4\), in one fixed exact field, after the compatibility equations and the asymptotic stop were proved. Two exact formulas agreed on all 464 ordered pairs. The run used 928 polynomial evaluations and 602 explicit predicates, totaling 1,530 of the declared 5,000-check budget; no rerun or larger search followed.

| \(m\) | \(N\) | \(Q\) | \(Z\) | \(B\) | Safe \(Z+B\) | Actual full image |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 8 | 10 | 3 | 54 | 57 | 53 |
| 3 | 12 | 16 | 4 | 128 | 132 | 122 |
| 4 | 16 | 22 | 5 | 234 | 239 | 223 |

In these cases no additional pair of the full square enters a selected output fiber. The full squares respectively have 46, 110 and 206 singleton fibers. These are finite checks, not a proposed asymptotic formula. Complete histograms and raw data are in [the exact audit](audit.md).

## 6. Exactly one next lemma

**OPEN — VO-O1, one mixed-role junction.** Keep three output labels \(0<\alpha<\alpha+\beta\), but change exactly the lower long-row identification to an old **column**. Decide whether there is a nondegenerate real solution with \(\alpha\ne\beta\) to
\[
\alpha=C(h),\quad\beta=C(k),\quad C(H)=\alpha+\beta,
\qquad H=s+\beta/4=k+\alpha/4,
\]
\[
3h^2+s^2=3k^2+r^2=3H^2+S^2=1,
\qquad h,s,k,r,H,S>0,\qquad h\ne s,\quad k\ne r,\quad H\ne S.
\]
Set \(q_{01}=\alpha/4\), \(q_{12}=(2\alpha+\beta)/4\), \(q_{02}=(\alpha+\beta)/4\). Require both \(q_{02}\pm S\) to belong to the scalar union of \(F(q_{01},h,s)\) and \(F(q_{12},k,r)\); require \(q_{02}-H=q_{01}-s\) to be outside the old row set \(\{q_{01}\pm h,q_{12}\pm k\}\). The upper long row remains \(q_{02}+H=q_{12}+k\). Define the actual ordered-pair sets
\[
E_{01}=\{q_{01}\pm h\}\times\{q_{01}\pm s\},\qquad
E_{12}=\{q_{12}\pm k\}\times\{q_{12}\pm r\},\qquad
E_{02}=\{q_{02}\pm H\}\times\{q_{02}\pm S\}.
\]
Require \(\lvert E_{02}\setminus(E_{01}\cup E_{12})\rvert\ge2\), so new pairs are counted after actual deduplication relative to both short frames.

This is a specific finite compatibility question, motivated by VO-C5. It is not claimed sufficient for growth or compression and is not searched in this cycle.

[Compatibility proofs](compatibility.md) · [Exact arithmetic audit](audit.md) · [Claim, cost and preservation ledger](verification.md).
