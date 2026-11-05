# Verification, sources, and construction ledger

T01 | 2026-10-20 | version 1 | \(P(x,y)=(x-y)^3+x+y\).

## Scope and provenance

The active user commissioned one offline tetrahedral constructive test,
with a lead, a compatibility/construction specialist, and an independent
exact-arithmetic referee. The three roles were performed by `/root`,
`/root/finite_gadgets`, and `/root/symbolic_obstruction`, respectively.
They worked on the same four registered systems.

The main report and proof appendix are new mathematical work. Historical
VO results are imported with their exact scope; inspecting a prior status
record is not described as rerunning its proof or experiment.

| Source | Sections used | What was done |
|---|---|---|
| `../2026-10-11-varying-output-frames/README.md` | Main conclusions and VO-O1 | Read for the prior candidate and frozen boundary |
| `../2026-10-11-varying-output-frames/compatibility.md` | VO-C1 frame formula; branch restrictions | Read; frame expansion independently checked in TJ-C1 |
| `../2026-10-11-vo-o1-freeze/README.md` | Statement, signed reduction, proof and scope | Read; confirmed that VO-C6 is already formally frozen |
| `../2026-10-11-vo-o1-freeze/referee-audit.md` and `verification.md` | Internal audit and evidence status | Availability and accepted status inspected; prior audit not presented as a fresh rerun |
| T01 current-state export, master handoff, SPEC, STATUS and current map | Target, chronology and preservation rules | Orientation; they do not replace the newer VO proof records |
| `../../templates/CONSTRUCTION_LEDGER.md` | Required count and cost fields | Applied below to a candidate with no admissible base case |

The necessary VO checkpoint and freeze companions are available. The
preceding freeze records that no separate original VO-O1 proof-note
attachment was located; this task does not claim to have read that
unavailable attachment. Its argument is available in the frozen note,
and is not a premise of the new contradictions. No outside theorem or
literature claim is needed.

Source identities are recorded in [source-identities.json](source-identities.json).
Repository paths in this ledger are relative to this note unless otherwise
specified.

## Claim register

All entries are dated 2026-10-20, version 1, on the retained T01 cubic branch.
“PROVED” below means a complete local proof, independently checked internally.
It does not mean external review.

| ID / status | Quantifiers and hypotheses | Proof locator / dependencies | Audit and remaining scope |
|---|---|---|---|
| TJ-C1 / PROVED | Every hypothetical real realization in the four-case catalogue; \(a,b>0\), positive conic widths and matching reflected branches | `compatibility.md` §1; direct cubic expansion and differentiation | Signs, all branches, \(u<1/6,D>2,H<1/2\) checked by all three roles |
| TJ-C2 / PROVED | Neither sign admits pattern A, \(H=r,S=e+p\) | Appendix §2; TJ-C1 and elementary maximum/square comparison | Both signs and all admissible \(p,w,H\) branches; no other closing pattern classified |
| TJ-C3 / PROVED | Neither sign admits pattern B; already impossible under \(S=w\) | Appendix §3; TJ-C1 and explicit derivative factorization | Both signs; no need for B's other role equation |
| TJ-C4 / PROVED | No admissible solution in any of the four registered systems | Appendix §4; TJ-C2–C3 | Exact finite feasibility obstruction, not unrestricted tetrahedral nonexistence |
| TJ-C5 / PROVED | Any actual finite frame union, after deduplication | Main report §3; counting uncovered pairs and edge incidences | Capacity bounds only; no actual \(N,Q,Z,B\) assigned to failed systems |
| TJ-O1 / OPEN | One explicitly changed column-role system, plus two new pairs and a third old-output row | Main report §4; complete untested statement | No existence, obstruction, finite test, or extension claimed |

The unchanged imported continuation has \(N=4m,Q=6m-2,Z=m+1\) and
actual image at least \(N^2/16\) (VO-C3–C4). Those are neither consequences
nor dependencies of TJ-C2–C4. VO-C6 is a separate signed triangular
nonexistence theorem. The fixed-output frame, marked-shift and other
historical proofs were not reopened.

## Construction ledger

| Required item | Disposition in this task |
|---|---|
| Parameter order | Fix symmetric output rule, opposite signs and two closing patterns before solving; catalogue unchanged thereafter |
| Input set and real projection | Would be the union of actual scalar slots in the endpoint table; the simultaneous real locus is empty |
| Lower and upper input counts | No constructed \(N\); \(N\le18\) is a hypothetical slot ceiling, not an attained count |
| Parameter/projection multiplicity | No parameter point survives; no asymptotic projection estimate claimed |
| Input thinning, both coordinates | No thinning scheme or surviving base set; no saving credited |
| Normalization and denominators | Translation gives \(z_0=0\); exact centers divide outputs by four; no scaling |
| Width branches | All positive admissible branches retained, subject to explicitly matching branches on reflected edges |
| Pair and output counts | No actual \(Q,Z,B\). General tetrahedral ceilings \(Q\le24,Z=4\), at most three selected rows and six selected pairs per output |
| Entire image and exceptional pairs | General bound \( |P(A,A)|\le Z+(N^2-Q)\); no numerical substitution without an actual set |
| Field degree, discriminant, regulator, units, local moduli and splitting | Inapplicable: no arithmetic construction or extension-field transport |
| Heights, archimedean distortion, carries, cover losses | No asymptotic construction, encoding, or growth stage; no zero-cost asymptotic estimate claimed |
| Attachment and growing parameter | No admissible base tetrahedron; attachment stage not reached |
| Final exponent and comparison | No new rate; no improvement over the earlier \(N^{4/3}\) selected-pair benchmark |
| Full-square and injective-subgrid audit | Not applicable without a real seed; not reported as passed |

## Budget and exactness

The predeclared finite budget was four role assignments and, only if exact
seeds survived, at most 5,000 target-polynomial evaluations and checked
predicates combined. Four analytic cases were resolved. No seed survived,
so the finite computational stage was not activated: **zero enumerated
parameter trials, zero executable target-polynomial evaluations, and zero
enumerated predicates**.

The proofs use exact identities and inequalities, with positivity checked
before comparing squares. No floating-point equality, bounded numerical
scout, installation, network use, external theorem, or novelty assessment
was used. File hashes and repository validators are documentation checks,
not mathematical enumeration.

## Repository and preservation checks

The initial checkout was `main`, with nine inherited modified tracked
files and many inherited untracked artifacts. They were not reset or
staged. A baseline of 402 nonignored existing files and the initial tracked
diff was saved in the ignored local run directory:

`local-only/runs/T01/2026-10-20-tetrahedral-junction/`.

This task adds only its new note package and dated appendices to the T01
STATUS, current project map, mechanism library, failure library and open
lemma register. Earlier result text and original proof/experiment files
are preserved. No executable mathematical code was added or modified.

Final validation:

| Check | Result |
|---|---|
| `python3 scripts/check_repository.py` | PASS: 39 archived source files and local links in 241 Markdown files verified |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local references, original import identities, 43 T03 manifest members, duplicate states and C4 hashes verified; no research code executed |
| `git diff --check` | PASS |
| New Markdown whitespace scan | PASS |
| Source/proof SHA-256 verification | PASS: all 16 recorded source identities agree |
| Baseline preservation audit | PASS: 397 of 402 pre-existing files unchanged; the other five retain their exact original byte prefixes and contain only dated appendices |
| Independent mathematical referee | ACCEPTED: TJ-C1–C5, saved complete proof and main report; no mathematical or scope correction |

The first repository-link check found the not-yet-written
`source-identities.json`; after generating that manifest, the check passed.
This was a document assembly issue, not a mathematical failure.

Four new files in `research/notes/2026-10-20-mixed-signature/` appeared during
the preservation audit from concurrent work outside this task. They were
not authored, changed, or mathematically reviewed here. They are not part
of this delivery. The local preservation audit records them separately.

No unit-test or experiment suite was run: this task added proof documents
and status appendices, not executable code. The repository checks above
do not certify the research target. All work remains uncommitted; no
stage, commit, push, reset, or remote change was performed.
