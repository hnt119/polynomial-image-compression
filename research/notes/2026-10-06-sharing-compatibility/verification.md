# Verification of the sharing compatibility cycle

T01, 2026-10-06. This cycle is commissioned research on one fixed
directed-triangle network for P(x,y)=(x-y)³+x+y. No internet, package
installation, literature assessment, arithmetic tower or unrelated carrier
search was used.

## Source authority and preservation

The controlling predecessor is the 2026-09-30
[elliptic report](../2026-09-30-elliptic-geometry/README.md). Its accepted
global elliptic obstructions and their scopes remain imported results.
This cycle does not claim to have independently re-audited those global
proofs. Its coordinate templates and the signs needed for mixed sharing
were checked directly. The relevant genus companion was read.

The older GS-A4 argument in
[progression-laboratory.md §4](../2026-09-21-growing-step-cubic/progression-laboratory.md)
was read in full. SH-C3 imports that fixed-spacing theorem, independently
checks its hypotheses at r=1/√3, and displays the specialization and exact
outside-band count. It does not reopen the old progression search.

The setup guide, current map, migration audit, master handoff, T01 current
state, its separate quadratic checkpoint, SPEC/STATUS, conflict register,
and relevant mechanism/failure/open records were consulted for scope.
The absent historical originals listed in MC-06 remain unavailable and
are not dependencies. No title or summary was substituted for an
unavailable proof.

Historical archive, migration, SPEC and earlier report bytes were not
edited. Five dated registry additions are recorded with original-prefix
hashes. The working tree was already dirty at task start; inherited and
unrelated changes were preserved. This task did not stage, commit, push,
reset, clean or change remotes.

## Mathematical checks performed

Three subagents handled geometry, construction and exact computation/audit.
The lead inspected the complete new proofs, not only their summaries.

| Claim | Evidence and exact scope | Checks performed and remaining boundary |
|---|---|---|
| SH-G1 | geometry.md §1, all real z,h, one fixed directed triangle | Geometry author, lead and audit agent checked each sharing sign, u+v+w=0, elimination and converse without division |
| SH-G2 | geometry.md §2, every ordered real output triple | Direct comparison system and positive determinant checked, including zero differences. No complex uniqueness or general network classification asserted |
| SH-G3 | geometry.md §3, fixed r>0 with r²=1/3 and h=2r | Seed, translation, full real component and Jacobian checked. Global uniqueness is based on SH-G2, not merely a positive Jacobian |
| SH-C1 | construction.md §2, every nonempty finite real T | Lead and audit agent checked N bounds, exact Z=N, oriented-edge injection and Q≤2N−3. Certificate lower bound is not actual-support lower bound |
| SH-C2 | construction.md §3, every integer m≥1 | Exact scalar/pair/label/output counts, boundary m=1, duplicate labels and absence of a fixed common anchor for m≥4 checked |
| SH-C3 | construction.md §4, consecutive strip only | Imported GS-A4 independently inspected; fixed spacing, exact support union, singleton band and N²−O(N^(3/2)) consequence checked |
| SH-X1 | exact-audit.md and new code/data | Eight predeclared finite sets, exact complete Cartesian enumeration; finite evidence is EXPERIMENTAL |
| SH-O1 | README.md final section | OPEN question about actual support for arbitrary T in this same family, with no truth, novelty or equivalence claim |

The geometry specialist also reviewed the final report and ledger. Its
one correction, explicitly requiring nonempty assemblies for Q≤2N−3,
was applied. The audit agent separately read both proof appendices and
GS-A4 and recorded its challenges in exact-audit.md. This is internal
proof review, not external review or a literature claim.

The new proof files carry date/version 2026-10-06 v1. The final local
manifest records their SHA-256 identifiers, sources and dependency locators.
Substantive claim scopes and unresolved gaps are in their precise statements.

## Computation release and exact budget

The compatibility equations were derived and confirmed before computation.
The geometry file was saved and the new scout and test source were read
before the lead released the single run.

Command:
python3 -m experiments.sharing_compatibility --compatibility-proof research/notes/2026-10-06-sharing-compatibility/geometry.md

The run used Python 3.12.7 and standard-library rational coefficients of
r=1/√3. It enumerated m=1,2,3,4,8,16,32,64 exactly and exhaustively on
each actual scalar square. No random seed, floating-point equality,
numerical root search or omitted cross-pair was used.

Actual run: 8 instances, 6,022 P evaluations and 3,140 charged exact checks.
The new unit tests add two visits to already declared small instances,
25 P evaluations and 53 geometric/accounting checks. Total current-family
cost is 10 instance visits, 6,047 P evaluations and 3,193 checks, below the
announced ceilings 12 / 50,000 / 10,000. Hand proof algebra and inherited
finite regression checks are separately described; no additional family
was evaluated.

All code, test, input, proof-at-release and portable-output hashes are in
exact-audit.md and the run provenance:
local-only/runs/T01/2026-10-06-sharing-compatibility/experiment-provenance.json.
The portable data retains hashes of all eight raw files, each containing
complete scalar, label, pair and output-fiber records. The writer refuses
overwrites. Neither the scout nor its tests were run by a second agent.

## Validation

The lead ran python3 -m unittest discover -s tests -v once: 94 tests passed,
including the four new tests. It ran python3 -m experiments verify once:
all 159 existing fixed finite checks passed. These tests do not establish
the asymptotic mathematical statements.

Post-assembly documentation, local-reference integrity, whitespace and
artifact-hash results are recorded below and in the local validation file.
The six Markdown report/appendix files, new scout/test/data and five
registry additions are this cycle's deliverables. Long calculations are
kept outside the concise main report.

The unrestricted T01 target remains OPEN. The prescribed fixed-gap
triangle architecture has the proved coverage obstruction; the strip
also has an actual-image obstruction. The sole next question concerns
arbitrary finite translate sets within the same family.

Final validation results: python3 scripts/check_repository.py passed
39 archived source files and links in 161 Markdown files;
python3 scripts/check_codex_setup.py passed 50 local references and
43 T03 manifest members; git diff --check passed. The five original
registry prefixes, code and test files, released geometry proof, portable
data and all eight raw result hashes were verified without rerunning
research. No unrelated documentation failure remained at this check.
