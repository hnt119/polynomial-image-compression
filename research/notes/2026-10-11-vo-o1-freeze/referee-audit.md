# Independent audit of the inline VO-O1 nonexistence proof

T01 · 11 October 2026 · version 1 · offline proof verification only.

**ACCEPTED — PROVED, VO-C6.** The exact signed-role system posed as
VO-O1 in the preceding varying-output-frame report has no admissible
real solution. The complete argument supplied inline by the user was
independently checked by hand against the original role equations. Its
algebra, signs, strict inequalities, and domain restrictions are valid.
This is an internal proof audit, not external review or a numerical test.

The fixed project polynomial is \(P(x,y)=(x-y)^3+x+y\). This proof
resolves one specified frame-junction question; it does not resolve the
unrestricted same-set image-compression target.

## 1. Evidence and authorization boundary

The proof being audited is the complete **inline user-supplied note**.
The lead's source-location check reported that no separate VO-O1 text
attachment or named standalone proof note was located. This audit does
not claim to have read such a file.

The original obligation was inspected at
[README.md §6](../2026-10-11-varying-output-frames/README.md#6-exactly-one-next-lemma).
The relevant frame conventions and earlier role equations were checked
in [compatibility.md](../2026-10-11-varying-output-frames/compatibility.md)
and the frozen [TC-G2 frame identity](../2026-10-11-torsion-compatible-sharing/geometry.md).
The source versions inspected have these hashes:

| Existing source | SHA-256 |
|---|---|
| Varying-output `README.md`, including VO-O1 | `aca44ca8fd26f32389ed96f535d7c5957f7d21a2fd8c32fb07b9867bdf572038` |
| Varying-output `compatibility.md` | `885cfb686b97849391c8337720b15053d7b0357a72fbf972ce393a14381b6658` |
| Torsion/frame `geometry.md` | `713c2372740eb9b3f54dcb4242192b170436b98002f2ceacdfcc075903cb2d58` |

The lead confirmed capture of the existing-file baseline before this
new audit file was created. No earlier artifact, status entry, proof,
or numerical result was edited by this referee. No mathematical program,
enumeration, target-P evaluation, numerical approximation, new
construction, or follow-up research was performed.

## 2. Reduction from the original signed roles

The original labels are \(0,\alpha,\alpha+\beta\), with positive gaps,
and the original definitions are
\[
 C(w)=8w(1-2w^2),\qquad
 \alpha=C(h),\quad\beta=C(k),\quad C(H)=\alpha+\beta.
\]
The three centers are exactly
\[
 q_{01}=\alpha/4,\quad q_{12}=(2\alpha+\beta)/4,
 \quad q_{02}=(\alpha+\beta)/4.
\]
The lower long row is required to be the lower old column, and the
upper long row remains the upper right-hand row:
\[
 q_{02}-H=q_{01}-s,\qquad q_{02}+H=q_{12}+k.
\]
Subtracting the centers, with these signs unchanged, gives
\[
 H=s+\beta/4=k+\alpha/4.
\]
Thus, on defining the function used in the user's note by
\[
 g(w)=C(w)/4=2w-4w^3,
\]
every original solution would satisfy
\[
 H=k+g(h)=s+g(k),\qquad g(H)=g(h)+g(k),                 \tag{1}
\]
\[
 0<h,k,H<1/\sqrt3,\qquad s>0,\qquad s^2=1-3h^2.       \tag{2}
\]
The strict upper bounds in (2) follow from the original conic equations
\(3h^2+s^2=3k^2+r^2=3H^2+S^2=1\) and positivity of s,r,S.
The letter g here denotes \(C/4\), not the different cubic polynomial
called g(t) in the preceding compatibility appendix.

This is a necessary subsystem. It does not impose the original extra
conditions on long-column membership, the lower row being new as a row,
or the number of new ordered pairs. Proving that (1)–(2) are already
inconsistent suffices to exclude the full original system.

## 3. Verification of each step in the supplied contradiction

### The first cancellation is legitimate

For \(0<w<1/\sqrt3\), one has
\(1-2w^2>1/3>0\), so g(w)>0. In particular (1) gives
\[
 H-k=g(h)>0.
\]
The same equations give \(g(H)-g(k)=g(h)=H-k\). Direct factorization is
\[
 g(H)-g(k)=(H-k)\{2-4(H^2+Hk+k^2)\}.
\]
Subtracting H-k and cancelling only the proved positive factor yields
\[
 H^2+Hk+k^2=1/4.                                      \tag{3}
\]
Since H,k>0, the terms Hk+k² are strictly positive. Thus
\(H^2<1/4\), and positivity of H gives
\[
 H<1/2.                                                \tag{4}
\]

### The width h lies strictly on the other side of one half

From \(H=s+g(k)\), and the already proved g(k)>0, it follows that
s<H. Hence 0<s<1/2. Using \(s^2=1-3h^2\),
\[
 1-3h^2<1/4,
\]
so h²>1/4. Since h>0,
\[
 h>1/2.                                                \tag{5}
\]
No branch of a square root is being chosen here without its sign: all
widths are positive in the original statement.

### The comparison after squaring preserves its direction

The displayed identity in the supplied argument expands exactly as
\[
 (3h-8h^3)^2-s^2
 =64h^6-48h^4+12h^2-1
 =(4h^2-1)^3.                                         \tag{6}
\]
Its right side is strictly positive by (5). The two quantities compared
before squaring are also positive: s>0, and the upper bound in (2) gives
\[
 3h-8h^3=h(3-8h^2)>h/3>0.
\]
Therefore (6) does imply the strict, unsquared inequality
\[
 s<3h-8h^3.                                           \tag{7}
\]

### The final strict inequality contradicts the width ordering

Because k>0,
\[
 g(k)=2k-4k^3<2k.
\]
Combining this with (1) and (7),
\[
 \begin{aligned}
 H=s+g(k)
 &<3h-8h^3+2k\\
 &=2\{k+g(h)\}-h\\
 &=2H-h.
 \end{aligned}
\]
The equality on the second line uses g(h)=2h-4h³ exactly. Subtracting
H gives H>h. This is incompatible with (4)–(5), which say
\(H<1/2<h\). The contradiction proves nonexistence. \(\square\)

## 4. Boundary and scope checklist

- No division by h-k, by a possibly zero derivative, or by a square-root
  branch occurs. The only cancelled factor is H-k=g(h)>0.
- All required inequalities are strict consequences of the original
  positive-width domain. Zero widths or zero column halfwidths are
  excluded there; this proof makes no separate boundary classification.
- The hypothesis \(\alpha\ne\beta\) is not needed by the contradiction.
  The necessary subsystem has no solution even if equal gaps are allowed.
  This stronger observation remains within the same fixed signed-role
  assignment; it is not an exclusion of other mixed-role junctions.
- The nondegeneracy exclusions h≠s, k≠r and H≠S, the two old-column
  membership requirements, the new-row requirement, and the two-new-pair
  requirement need not be used. Every solution satisfying them would
  first have to solve the inconsistent subsystem (1)–(2).
- Replacing a minus sign, reversing which old column is identified,
  changing the upper-row role, or moving to a different frame model is
  outside this theorem. No alternative system is investigated here.

## 5. Relation to the earlier results

The prior compatible family and its ledgers
\(N=4m\), \(Q=6m-2\), \(Z=m+1\), together with its actual-image
lower bound \(N^2/16\), are preserved imported results of VO-C1–VO-C4.
They concern the earlier row-to-row junction. They are neither premises
of this contradiction nor consequences of the mixed-role nonexistence
claim. The retained finite evaluations are likewise not used in this
proof and were not rerun.

VO-C6 supplies an accepted proof resolving the exact VO-O1 question.
The unrestricted same-set T01 target remains OPEN. This audit proposes
no construction, successor lemma, entropy program, or new research cycle.

| Claim record | Scope |
|---|---|
| ID / track / polynomial | VO-C6; T01; \((x-y)^3+x+y\) |
| Date / version | 2026-10-11 / 1 |
| Quantifiers | No real h,k,H,s satisfying (1)–(2); therefore no solution to the original VO-O1 signed-role system |
| Source of proof | Complete inline user-supplied argument; no standalone attachment located by the lead's source check |
| Dependencies | Original VO-O1 equations and positive-width frame conventions; elementary identities and inequalities displayed above |
| Evidence type | Complete symbolic proof, independently verified manually in this task |
| Review | Internal independent referee acceptance; not external review |
| Remaining scope limit | No theorem about other role assignments or arbitrary varying-output networks; no asymptotic compression conclusion |
