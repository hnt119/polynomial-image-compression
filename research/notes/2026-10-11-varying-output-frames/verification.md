# Claim, cost and preservation ledger

T01 · 11 October 2026 · version 1. Fixed polynomial
P(x,y)=(x-y)^3+x+y, with one finite real set in both coordinates.

## Authorization, sources and evidence

This cycle is the user's commissioned offline varying-output-frame task.
The lead, compatibility/construction specialist and independent referee
worked on one output-first triangle. No internet, installation, rank/CM
search, arithmetic tower, new torsion test or global elliptic-factorization
search was used. The mathematical budget was declared before evaluation:
at most six justified instances and 5,000 explicit exact predicates plus
target-polynomial evaluations combined. After the symbolic obstruction,
only m=2,3,4 of the same family were released as finite diagnostics.

The polynomial identities, branch restrictions and continuation counts
were derived before the evaluator ran. The lead inspected the complete
proof and code, and the referee independently checked the proof. This is
internal review, not external review. The new proof is distinguished from
the accepted results imported below. No novelty claim is made.

| Source, date and locator | Use and evidence in this cycle |
| --- | --- |
| [Frozen torsion/frame checkpoint](../2026-10-11-torsion-frame-freeze/README.md), main report and source/status ledger; 2026-10-11 | Read for the controlling boundary: MS-C1 PROVED, TC-O1 resolved, T01 OPEN. No new audit of the marked-point arithmetic or genus-four proof. |
| [TC geometry](../2026-10-11-torsion-compatible-sharing/geometry.md), TC-G2; 2026-10-11 | Inspected the frame identity, admissible real-width domain and fixed-output width bound. Our use of its elementary width function is explicitly reproduced in VO-C1–C2. Other frozen theorems are not reopened. |
| [CP construction](../2026-10-06-changed-collision-pattern/construction.md), CP-C1, §2; 2026-10-06 | Read the simultaneous two-row conic identity and output formula. The frame identity is imported; the new three-frame gluing is proved here. |
| [Progression laboratory](../2026-09-21-growing-step-cubic/progression-laboratory.md), GS-A4, §4; 2026-09-21 | Read the exact irrational-squared-spacing injectivity clause and reproduce its proof for our subgrid. No general theorem for unions of progressions is assumed. |
| [Structure and reuse](../2026-09-21-growing-step-cubic/structure-and-reuse.md), GS-P3, §3; 2026-09-21 | Imported N^(4/3) prescribed-pair benchmark for comparison; no rerun of its experiment or claim that it solves T01. |

The setup, current project map, migration audit/conflicts, master handoff,
T01 current-state export, SPEC and STATUS were consulted for chronology
and source locations. The separate quadratic branch is not substituted
for this cubic target. All required sources for this cycle were located;
historical migration gaps are not dependencies. A guessed filename that
did not exist was replaced by the actual linked source, not reconstructed.

[Source identities](source-identities.json) retain the exact sizes and
SHA-256 hashes of the seven research source files listed or linked above.

## New claim records

All following records are T01 / varying-output conic-frame networks,
P(x,y)=(x-y)^3+x+y, dated 2026-10-11, version 1. Exact file versions are
identified by the retained artifact hashes. “PROVED” means the complete
identified argument was inspected and independently checked internally.

| ID / status | Quantifiers and hypotheses | Proof / dependencies / audit | Retained gap or limitation |
| --- | --- | --- | --- |
| VO-C1 / PROVED | Three outputs −Δ,0,Δ with Δ>0; all admissible positive real widths; the two specified outside-row identifications | README §1; compatibility VO-C1–C2. TC-G2 frame identity, explicit branch analysis and elimination; lead and referee checked. | Other signed endpoint roles are outside scope. |
| VO-C2 / PROVED | Unique positive root t in (1/50,1/49); the three displayed frames | README §2; compatibility VO-C2. VO-C1, positive-root identities and exact deduplication; lead and referee checked. | N=8,Q=10,Z=3 is a finite junction, not asymptotic progress. |
| VO-C3 / PROVED | Every integer m≥2, fixed t and Δ selected before m; consecutive output rule jΔ and its specified short/long frames | README §3; compatibility VO-C3. VO-C2, cubic irreducibility and coefficient comparison; lead and referee checked. | Q=6m−2, Z=m+1, B=16m²−6m+2; growing reuse fails. |
| VO-C4 / PROVED; candidate FAILED | Every m≥2 for exactly A_m; and every additional admissible frame whose scalar slots all lie in A_m | README §4; compatibility VO-C4 for the subgrid. VO-C3, GS-A4 irrational clause, elementary interval count; lead and referee checked. | Actual image ≥N²/16; frame-only closure ≤20N pairs. No obstruction to arbitrary real sets. |
| VO-C5 / PROVED | Positive adjacent gaps α,β and widths h,k,H, with the same two outside-row identities and long gap α+β | README §4; compatibility VO-C5. Exact elimination, checked independently. | Forces α=β in this role pattern only. |
| VO-X1 / EXPERIMENTAL | Exhaustive entire squares for the three predeclared instances m=2,3,4 | audit.md and exact-results.json; two exact P formulas, no floating-point equality; referee executed, lead reviewed. | Finite counts do not establish a uniform full-fiber formula. |
| VO-O1 / OPEN | The single mixed row/column junction specified in README §6, with unequal gaps and all real/nondegeneracy conditions | A precise next finite obligation; role equations inspected for faithful scope only. | Existence is not tested or proved; even a witness would not establish growth. |

No earlier PROVED statement is changed. The new failure is confined to
this candidate. T01 remains OPEN; MS-C1 and the torsion/frame freeze retain
their recorded status and original proof files.

## Construction ledger

This instantiates `research/templates/CONSTRUCTION_LEDGER.md` for the
failed candidate rather than suppressing its complement cost.

**Selection order.** Choose the output triangle and the two endpoint roles;
solve its simultaneous system for the unique t; fix h=√t, ρ=2−4t,
δ=hρ and Δ=4δ. Only then let the integer m≥2 grow. All square roots
are positive in the selected real embedding. Every frame has positive,
unequal row/column widths, and all controlled ordered pairs belong to
the one actual scalar union A_m.

| Gain or cost | Bound and justification | Status |
| --- | --- | --- |
| Input count, lower and upper | N=4m exactly: four disjoint progressions by irrationality of ρ | PROVED |
| Thinning in both coordinates | None: the target and audit use the complete A_m². The selected-pair restriction is charged below, not treated as input density one. | PROVED |
| Parameter/scalar multiplicity | Each of the 4m short scalar slots is distinct; long slots are old scalars. Two duplicate ordered pairs per long frame are removed. | PROVED |
| Real projection and degree | A_m lies in the fixed real field Q(h), h²=t, of degree at most six; no varying-field projection is used. The evaluator works with coefficients in the degree-three field Q(4t) after dividing scalars and outputs by the nonzero h. | PROVED |
| Splitting, local residues and population | Inapplicable: no congruence, local-to-global lifting or residue selection | Not used |
| Discriminant, regulator and units | Fixed field throughout; no field-asymptotic argument or unit construction. No estimate involving these invariants is invoked. | Not used |
| Heights, denominators and moduli | Fixed algebraic coefficients; integer progression coefficients have size O(m). No height-based point count, modular reduction or denominator clearance is used for counting. | PROVED scope |
| Archimedean size/distortion | h,ρ,D fixed positive; A_m has diameter O(m). Exact scalar equality, not proximity, defines reuse. | PROVED |
| Branches and covers | All admissible short/long width branches for the chosen role were handled; no parameter branch is dropped as an uncharged exception. No cover, state or carry encoding. | PROVED |
| Local pairs vs new cross pairs | 4m short-frame pairs plus exactly 2(m−1) genuinely new cross-block pairs | PROVED |
| Outputs and selected fibers | Z=m+1, average Q/Z=6−8/(m+1), at most two rows and six selected pairs per output | PROVED |
| Uncovered-pair charge | B=16m²−6m+2, charged one potential new output per uncovered ordered pair | PROVED |
| Entire-image upper bound | Z+B=16m²−5m+3 | PROVED |
| Actual-image lower bound | N²/16 via an injective m×m subgrid | PROVED |
| Rate and comparison | Q=Θ(N), coverage Θ(1/N), below the inherited Θ(N^(4/3)) selected-pair benchmark. Both actual image and safe upper bound have exponent 2. | PROVED |
| Net exponent | Set depth d=log m: log N=d+O(1), log safe bound=2d+O(1). Thus a=B_input=1 and net delta=2−2=0; no positive certified c_P. The actual lower bound excludes one for this family. | PROVED |

No growth is inferred from the finite seed. Adding all frames already
available in this pool cannot improve Q beyond O(N); changing only the
adjacent output gaps cannot preserve the same two row roles. These two
separate statements explain the stop and motivate precisely VO-O1.

## Finite budget, integrity and completion checks

The exact command, interpreter version, evaluator/proof/result hashes,
operation counts and all finite full-square fiber histograms are in
[audit.md](audit.md). The initial scalar root interval is part of the
proof, not a floating-point numerical input. There is no random seed:
the finite audit is exhaustive over three specified squares.

Existing archive sources and historical proof/data files are preserved.
Only dated addenda are appended to the five current index/status files;
the original bytes remain an exact prefix. The initial 372-file baseline,
final preservation check, artifact manifest and validation log are retained
under `local-only/runs/T01/2026-10-11-varying-output-frames/`.

Repository and setup validation results are recorded at completion below.
These checks test documentation/setup integrity, not the research target.
The workspace already contained unrelated modified and untracked files;
they are not attributed to this task. No stage, commit, push or remote
change is made.

All required completion commands passed:

- `python3 scripts/check_repository.py`: 39 archived files and local links
  in 216 Markdown files verified.
- `python3 scripts/check_codex_setup.py`: 50 local reference files, 43 T03
  manifest members, original identities, duplicate states and C4 hashes
  verified; no research program executed by that checker.
- `python3 -m unittest discover -s tests -v`: 100 existing tests passed.
- `python3 -m experiments verify`: every existing finite regression passed.
- `git diff --check`: no whitespace errors in tracked diffs.

The last two Python suites are the repository-mandated existing regression
checks because a portable copy of the evaluator is included. They do not
run this new evaluator, enlarge its three-instance research budget, or
authorize another mathematical scout. Their logs are saved separately
from the one released VO-X1 run. The new source/data files are inspected
separately because ordinary tracked diffs do not include untracked files.

The completed baseline comparison found 367 of 372 pre-existing files
byte-identical. The remaining five are exactly the current project map,
mechanism library, failure library, open-lemma index and T01 STATUS;
each retains its entire former content as a hash-verified prefix, followed
by this dated cycle's addendum. There are no missing files or unexpected
changes. The seven new report/proof/audit/source/data files in this note
directory are this cycle's new artifacts; the source identity ledger is
included in that count. New-file whitespace checks are clean.
