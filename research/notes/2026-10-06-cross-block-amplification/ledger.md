# Construction and signed-rate ledger

6 October 2026 · version 1 · T03 · fixed \(Q(x,y)=x^2+xy+y^2\).
This follows [the required construction template](../../templates/CONSTRUCTION_LEDGER.md).
The active user authorized this cycle, its two directions and shared caps.
No historical next task was treated as permission to change the objective.

## Claims, hypotheses and provenance

| ID | Status / exact scope | Controlling proof | Dependencies / audit |
|---|---|---|---|
| AMP-D0 | PROVED implication: complete \(\mu_m\)-orbit union has at most \(\lfloor(3n^2+1)/4\rfloor\) pairs; valid prescribed inventory forces \(n\ge8q\) | audit.md §2 | Inspected DC-M1; lead and independent C |
| AMP-A1 | PROVED: all \(8q\) product amplitude cosets disjoint for \(r\ge0\) | amplitudes.md §1 | Frozen FG-A1 field relation, balanced digits; lead and C |
| AMP-A2 | PROVED: actual \(8q^2\le n\le48q^2\) for \(r\ge1\), seed \(n=17\) | amplitudes.md §2 | AMP-A1 and injective projection on \(\mathbb Q(\xi)\); lead and C |
| AMP-A3 | PROVED: exact encoded norm classes and \(6q2^s\) encoded fibers | amplitudes.md §3 | Product norm expansion and seven-slot relations; lead and C |
| AMP-A4 | PROVED diagnostic: explicit common-switch assembly defect | amplitudes.md §4 | Exact decoding algebra; lead and C; not a norm-inequality theorem |
| AMP-R1 | PROVED: at most four second phases for any fixed pair of independent switches, apart from sign targets | returns.md §4 | Whole quadratic expansion and sign degeneracy; lead and C |
| AMP-R2 | PROVED: \(D\) has at most \(1536q^3 4^r\) actual sources | returns.md §5 | All label representations counted; lead and C |
| AMP-R3 | PROVED obstruction / FAILED certificate: iterated specified returns at most4 outside \(D\cup\Gamma\) | returns.md §6 | Reversible scalar relation, sign/swap invariance; lead and C |
| AMP-G1 | PROVED obstruction / FAILED inventory: phase-sum rule has exactly8 cosets for all \(q\) | identities.md §§2–6 | Completion of square, elementary finite orthogonality; lead and C |

All claims are dated 2026-10-06 on T03/ML-O1. Their files and version hashes
are recorded in state.json and manifest.json. Source labels do not replace
proof: the new written arguments were read and independently checked.
No literature search, external theorem import or novelty assessment occurred.

## Rule 1 — balanced factors

Fix \(I=\{-3,\ldots,3\}\), scales \(1,\ldots,8\) and prime7 first.
Then grow depth \(r\), choose compatible \(\xi_r\), and take
\(c_{h,\mathbf i}=h\prod_\ell(2-\xi_r^{i_\ell7^\ell})\).
There is no thinning, optimization over depths or auxiliary extension.

| Gain/cost | Exact charge | Consequence |
|---|---|---|
| Input labels and actual cosets | \(8q\) disjoint cosets, \(48q^2\) encoded complex points | No label collisions before projection |
| Actual scalar count | \(8q^2\le n\le48q^2\) | \(a=B=2\log7\) per depth; factor49 |
| Input thinning in both coordinates | None | All ordered pairs remain in scope |
| Projection fibers | Lower count uses \(X\) injective on \(8q^2\) points; upper count allows every other collision | No global scalar injectivity is assumed |
| Encoded norm gain | \(8\cdot4^r\) outputs on \(\Gamma\), fibers \(6q2^s\) | Restricted to \(\Gamma\), never an all-image bound |
| Encoded source mass | \(48q^2=\Theta(n)\) | Leaves \(\Theta(n^2)\) pairs for another membership argument |
| Independent branch cost | At most \(4^r\) switch pairs per amplitude pair | Fully charged against \(6q\) second-phase choices |
| Cross-block eligibility | At most4 phases per fixed choices, or at most2 in the sign-degenerate case | Whole quadratic equality, not assumed equality of formal labels |
| Certified rich-source mass | At most \(1536q^3 4^r+48q^2\) | Fraction \(24(4/7)^r+3/(4q^2)\to0\) |
| Low-certificate population | At least \(n^2/2\) for \(r\ge8\), certified multiplicity at most4 | Every fixed positive certificate tail fails |
| Actual full-fiber bad population | UNKNOWN | Certified upper counts are not full-fiber upper counts |
| Origin and stabilizers | Encoded points nonzero; norm multipliers free there; origin has one actual target | Repeated labels never count as targets |
| Field degree | \([K:\mathbb Q]=12\cdot7^{r-1}\) for \(r\ge1\) | Grows with depth; no fixed-field estimate applied |
| Local relation / carries | Seven-slot relations; supports at most2 per block for amplitudes and3 for their norms | Proved by balanced digits, used only for the displayed inventory/norm classification |
| Scalar denominators | \(3A\subset\mathcal O_{K^+}\) | Fixed decode; no denominator strata omitted |
| Switch denominators | Explicit nonzero \(P_S\); every conjugate lies in modulus range \([1,3^{\lvert S\rvert}]\) | Membership proved only through exact cancellation in admitted products |
| Archimedean / coefficient growth | Amplitude conjugates at most \(8\cdot3^r\), scalar conjugates at most \(16\cdot3^r/\sqrt3\) | Charged growth, not converted into an unproved volume saving |
| Discriminant, regulator, class number, ideal index | Not evaluated; no estimate using these is invoked | Not assigned zero in a proposed positive arithmetic rate |
| Norm-one distortion | Modulus1 in every embedding of the cyclotomic field | Does not imply scalar membership on arbitrary sources |
| Entire output rate | Only the trivial upper exponent \(4\log7\) is supplied | Actual exponent remains OPEN |
| Signed rate from supplied full-support bound | \(2a-4\log7=0\) | No positive \(c\); not a lower bound on the actual image |
| Required \(\varepsilon,\delta\) | Unproved for full fibers; impossible for the defined certificate | No borrowed spreading exponent or collision-energy inference |

Uniformity: all constants are independent of \(r\); the \(O(1)\) errors in
\(\log n\) follow from fixed prefactors. The potential rich-certificate
set is \(O(n^{2-\alpha})\) for
\(\alpha=\log(7/4)/(2\log7)>0\). This exponent describes the **small rich
set**, the opposite of the desired small bad set. It is not a successful
exception exponent.

## Rule 2 — quadratic phase sums

Fix the same prime and scales, and take
\(c_{h,j}=h\sum_{a\bmod q}\xi^{a^2+ja}\).
The exact phase identity collapses all \(j\) for each \(h\).

| Gain/cost | Exact accounting |
|---|---|
| Required versus actual cosets | \(8q\) required; exactly8 present |
| Paired labels | \(48q^2\) formal labels, \(48q\) actual points; exactlyq labels per point |
| Actual input | \(3q\le n\le48q\); native-depth factor7 |
| Scalar thinning | None inferred from the pair-label loss |
| Certified targets | \(6q\) distinct cyclic targets on exactly \(48q\) encoded sources |
| Missing membership domain | At least \(n^2-48q\) pairs; their actual full fibers are unknown |
| Action duplicates | Quadratic shift labels can coincide; all lie in the existing cyclic group |
| Integrality / denominators | Integral amplitude sums; \(3A\) integral after decoding |
| Heights | Amplitude conjugates at most \(8\sqrt q\), scalar conjugates at most \(16\sqrt q/\sqrt3\) |
| Field, discriminant, regulator and local factors | Same field degree; no discriminant, regulator, ideal-count or density estimate is used |
| Rates | Encoded gain cannot repair inventory or coverage; full-image rate OPEN, no positive signed gap proved |

## Disposition

Two proposals, two finalists, zero mutations. The first is a valid new
carrier whose specific amplification certificate fails; it is **not**
proved to have quadratic image. The second fails the required inventory;
its deduplicated image is also unresolved. Neither supplies a surviving
near-full amplification mechanism. No replacement proxy or rigidity task
is substituted for the power-saving objective. T03, ML-O1, DC-O1,
ARG/TCRC and RC15/4 remain OPEN; all frozen failures keep their prior scope.
