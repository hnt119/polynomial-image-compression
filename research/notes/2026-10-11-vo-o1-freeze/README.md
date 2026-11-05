# VO-O1 freeze: the mixed-role junction has no positive real solution

T01 | 11 October 2026 | version 1 | offline proof verification and documentation.

[Readable PDF](../../../output/pdf/2026-10-11-vo-o1-freeze/vo-o1-freeze.pdf) · [Independent referee](referee-audit.md) · [Source and preservation ledger](verification.md)

**PROVED - VO-C6. VO-O1 is resolved negatively.**
The proposed positive real junction has no solution. The lead and an independent mathematical referee accept the supplied contradiction. T01 remains OPEN.

For the fixed polynomial P(x,y) = (x - y)³ + x + y, the preceding checkpoint proposed three frames on outputs 0, α, α + β, with α,β > 0. The lower row of the long frame was to reuse a lower column of the first short frame; its upper row was to reuse the upper row of the second. This note verifies that these signed roles are already incompatible.

## 1. Exact nonexistence statement

There are no real h, k, H, s satisfying the following necessary subsystem. The letters h, k, H are row halfwidths; s is the first short frame's positive column halfwidth. Define

\[
C(w)=8w(1-2w^2),\qquad g(w)=C(w)/4=2w-4w^3.
\]

Here g always means C/4; it is distinct from the polynomial called g(t) in the preceding checkpoint's root calculation.

\[
0<h,k,H<1/\sqrt3,\quad s>0,\quad s^2=1-3h^2,
\]

\[
H=k+g(h)=s+g(k),\qquad g(H)=g(h)+g(k).
\]

## 2. Why the original junction implies this subsystem

A frame F(q,h,s) = {q - h,q + h} × {q - s,q + s}, with positive halfwidths and 3h² + s² = 1, has row outputs 2q ± C(h)/2. Expansion and the conic give the common upper-row value 2q + h³ + 3hs² + h = 2q + 4h - 8h³; replace h by -h for the lower row. Thus the three ordered output edges fix

\[
\alpha=C(h),\quad\beta=C(k),\quad\alpha+\beta=C(H),
\]

\[
q_{01}=\alpha/4,\quad q_{12}=(2\alpha+\beta)/4,\quad q_{02}=(\alpha+\beta)/4.
\]

The exact two signed sharing equations are q_02 - H = q_01 - s and q_02 + H = q_12 + k. Subtracting the displayed centers gives H = s + β/4 = k + α/4. Dividing the output equations by 4 gives the g-equations above.

The other column halfwidths r,S are positive and satisfy 3k² + r² = 3H² + S² = 1; all three row halfwidths therefore lie strictly between 0 and 1/√3. Discarding the remaining endpoint and pair requirements only enlarges the proposed solution set. A contradiction for this subsystem suffices.

## 3. Proof of VO-C6

**Step 1 - the long row halfwidth is less than 1/2.** On 0 < w < 1/√3, one has 1 - 2w² > 1/3, hence g(w) > 0. In particular H - k = g(h) > 0. Also g(H) - g(k) = g(h) = H - k. Expanding and factoring gives

\[
0=g(H)-g(k)-(H-k)=(H-k)\bigl[1-4(H^2+Hk+k^2)\bigr].
\]

We may divide by H - k because it is strictly positive. Since k,H > 0, the two terms Hk + k² are positive. Therefore

\[
H^2+Hk+k^2=\frac14,\qquad H^2<\frac14,\qquad H<\frac12.
\]

**Step 2 - the first short row halfwidth is greater than 1/2.** From H = s + g(k) and g(k) > 0, we obtain 0 < s < H < 1/2. The conic equation then gives

\[
1-3h^2=s^2<\frac14\quad\Longrightarrow\quad h^2>\frac14\quad\Longrightarrow\quad h>\frac12.
\]

**Step 3 - the compatibility equations force the opposite order.** The exact identity, using s² = 1 - 3h², is

\[
(3h-8h^3)^2-s^2=64h^6-48h^4+12h^2-1=(4h^2-1)^3>0.
\]

Both quantities compared by their squares are positive: s > 0, and h < 1/√3 gives 3h - 8h³ = h(3 - 8h²) > h/3 > 0. Hence s < 3h - 8h³. Moreover g(k) = 2k - 4k³ < 2k because k > 0. Consequently

\[
H=s+g(k)<3h-8h^3+2k=2(k+g(h))-h=2H-h.
\]

Subtracting H yields H > h. Steps 1 and 2 instead give H < 1/2 < h. This contradiction proves nonexistence. No equation was squared in a way that introduces a new branch, and no approximation or enumeration is used.

## 4. Strictness and boundary audit

| Potential issue | Exact justification |
| --- | --- |
| Cancelling H - k | H - k = g(h) > 0; the divisor cannot vanish. |
| Obtaining H < 1/2 | Hk + k² > 0, and H > 0. Equality H = 1/2 is impossible. |
| Obtaining h > 1/2 | s < H < 1/2 and s² = 1 - 3h². Equality h = 1/2 is impossible. |
| Comparing squares | s > 0 and 3h - 8h³ > h/3 > 0. The positive sign is proved before comparison. |
| Using g(k) < 2k | The difference 2k - g(k) = 4k³ is strictly positive. |
| Excluded boundaries | Zero row widths and widths 1/√3 are outside the original positive-width frame domain. No closure or limiting-case claim is needed. |

## 5. Exact scope of the freeze

**PROVED.** VO-C6 excludes the necessary subsystem, and therefore the full VO-O1 junction. Unequal gaps α ≠ β, distinct frame slots, membership of the two long columns in the old scalar set, exclusion of the lower long row from the old row set, and two new pairs after deduplication are unused extra restrictions. They cannot repair an empty necessary subsystem.

**IMPORTED, unchanged.** The earlier continuation has N = 4m, Q = 6m - 2, Z = m + 1 and actual image at least N²/16, for m ≥ 2 (VO-C3-C4). These concern the former equal-gap family. They are neither premises nor consequences of the present contradiction, and are not re-audited here.

**OPEN.** The unrestricted T01 target remains OPEN. This proof makes no claim about other endpoint roles; earlier scoped exclusions and frozen torsion/frame results are unchanged. The previous VO-O1 OPEN text remains intact as history, superseded only in its precise signed-role scope. No successor research cycle is authorized or begun.

## 6. Source and verification ledger

**Controlling problem statement:** *A closed output triangle without growing frame reuse*, 11 October 2026, v1, README §6. Its compatibility appendix supplies the frame formula and VO-C3–C4; audit.md and verification.md were inspected for evidence scope.

**Supplied argument:** the complete three-step proof in the current user message, *T01 - Verify and freeze VO-O1 before further research*. No separate proof-note attachment was located in the workspace or supplied text/Markdown attachments; none is claimed read.

**Audit:** lead and independent mathematical referee checked the original signs, reduction, identities, divisor, strict inequalities and boundaries. Verdict: ACCEPTED, no mathematical correction needed. This is internal verification, not external review or a novelty claim.

**Record:** VO-C6 | T01 | 2026-10-11 | v1. Proof §§1-3; audit §4 and referee-audit.md. Source hashes accompany the Markdown. No mathematical program or enumeration was run.
