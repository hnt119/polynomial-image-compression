# Source, claim and verification ledger

21 October 2026 · version 1 · T01 · fixed \(P(x,y)=(x-y)^3+x+y\).

## Authorization and scope

The active task authorized one offline multiscale question: how actual
fiber multiplicity persists under scalar-cell refinement. The lead used
a nonlinear-projection specialist and a separate exact-arithmetic referee.
No internet, installations, rank search, arithmetic tower, complete-frame
catalogue, torsion test or literature/novelty claim was used. TJ-C6 was
read as a frozen boundary, not reopened.

The initial finite budget was six scalar sets of size at most 24. Before
execution the six instances were fixed: AP8/AP12, CP ladder m=2/m=3,
and B={0,1,3} plus rho D, with rho=1/64 and D={0,1,3}/{0,1,3,7}.
No further candidate or parameter values were enumerated. The metric
resolutions 1, 1/16 and 1/256, root [0,16), and five four-way generations
were fixed in the lead's saved script before it ran. Only the four rational
cases received metric and tree censuses; all six received exact full-square
fiber censuses. These experiments are diagnostic, not a proposed witness.

## Claim identities

| ID | Status and precise scope | Proof / evidence | Dependencies and limitations |
|---|---|---|---|
| MC-L0 | PROVED; exact zoom identity and explicit bounds for every real d, rho>0 | README §3; appendix A | Cubic expansion; independently checked; normalization changes coefficients |
| MC-S1 | PROVED; one exact cubic fiber occupies at most eight child squares of every four-way scalar refinement | specialist §MC-S1; README §1 | Global P_x>=1, 1-Lipschitz fiber graph; no nonconcentration premise |
| MC-S2 | PROVED; for every finite real A, low-branch pair count <=s 8^b; stated near-full consequence if s<=N^(2-c) | specialist §MC-S2; README §1 | MC-S1 and finite prefix-tree proof; no bound on locations or balance of branches |
| MC-S3 | PROVED; localized capacity/actual-overlap inequality and local-rich-mass transfer | specialist §MC-S3; README §2; appendix B | MC-S1, capacity min(n_J,3n_I); hypotheses include the exact supports, so not an autonomous expansion estimate |
| MC-S4 | PROVED elementary exponent comparison; MISSING SOURCE for Raz–Zahl application | specialist §MC-S4; README §4 | No Raz–Zahl exponent or inverse conclusion asserted |
| MC-X1 | EXPERIMENTAL, exhaustive and exact for the six fixed squares | experiment-summary.json, referee-counts.json | 533 ordered pairs, independent agreement; no asymptotic inference |
| GS-P4 specialization | PROVED in inspected source, elementary two-level specialization checked here | appendix C; imported GS-P4 §4 | Faithfulness/root exclusions required; no uniform usable scale as digits grow |
| MC-O1 | OPEN proposed collision-rectangle bound in one fixed two-level model | README §6 | Not tested or assumed; sole successor question |
| T01 target | OPEN | This report supplies no full-image power-saving upper bound | All historical scoped failures remain scoped |

The complete proofs, not the agents' agreement, are the evidence for
PROVED. Internal independent audit is not external review. File versions
and SHA-256 identities accompany this note in source-identities.json.

## Located sources and what was actually used

| Source | Use and evidence boundary |
|---|---|
| [TJ-C6 freeze](../2026-10-21-tj-o1-freeze/README.md) | Read for current frozen scope only; no fresh verification of its roles |
| [Prior projection/entropy note](../2026-10-11-transfer-division-entropy/C_entropy.md) | C-NORM and C-BRIDGE inspected; exact-versus-metric limitations retained; no imported missing theorem |
| [Growing-step structure, GS-P4 §4](../2026-09-21-growing-step-cubic/structure-and-reuse.md) | Full faithful coefficient-recovery proof inspected; explicit predecessor of appendix C |
| [Growing-step checkpoint](../2026-09-21-growing-step-cubic/README.md) | Imported AP/lattice failure and N^(4/3) benchmark; asymptotic results not rerun/proved by the finite census |
| [Quadratic projection note](../2026-09-21-sublinear-cubic/reuse-and-projections.md) | Read for overlap of prior scope; no quadratic-field search performed or theorem silently generalized |
| [CP checkpoint](../2026-10-06-changed-collision-pattern/README.md) and [construction](../2026-10-06-changed-collision-pattern/construction.md) | Accepted fixed ladder definitions and failure imported; exact scalar/fiber census freshly checked at m=2,3 |
| [Lead audit source](audit.py) | New six-case wrapper inspected before execution; existing CP routine inspected before import |
| [Independent referee](referee.md) | Geometry, prefix counting, local capacity, exact identities and six-case counts independently checked |
| Setup, project map, migration audit, master handoff, T01 state export, SPEC/STATUS, conflicts and relevant registries | Read for target, source hierarchy, preservation and missing-source discipline; not substitutes for proofs |

**MISSING SOURCE:** local Raz–Zahl arXiv:2108.07311, Theorem 1.18 and the
energy-dispersion input. Searches covered project notes and ignored local
sources; attachment filenames and MD/TXT/JSON/TEX contents; and identifying
filenames in Downloads/Documents/Desktop. No matching theorem text was
located. This is not a claim to have searched every binary document on
the computer. The supplied theorem's hypotheses, constants, exponent and
applicability remain unavailable. No abstract was used to reconstruct them.
The earlier entropy note also records unavailable external inputs; they
remain unavailable here. No Bourgain-type theorem is a dependency.

## Exact experiment provenance and independent checking

The lead executed the saved six-case audit once, after reading it. The
rational cases use fractions and two polynomial formulas. For CP the
inspected accepted routine uses rational t-coefficient triples and two
formulas. The referee implemented independent integer companion-operator
arithmetic in U=4t, without executing the imported routine. Its source,
runtime, invocation and hashes are embedded in referee-counts.json.

- Lead evaluations: 1,066, including both full-square formulas.
- Independent referee evaluations: 533; 39 explicit accounting predicates.
- Candidate-audit total: 1,599 evaluations over exactly six sets.
- Comparison: every one of 533 ordered-pair outputs agrees after exact
  conversion of input ordering and CP output basis, not merely histograms.
- All pair masses, exact scalar counts and output supports are deduplicated.
- Covering numbers are separate exact greedy interval covers, not output
  bins or collision multiplicities; numerical floating-point equality is unused.
- The source, fixed parameters, interpreter version, runtime and code hashes
  are recorded in experiment-summary.json and the raw local audit.

Raw lead data and the preservation baseline reside at
`local-only/runs/T01/2026-10-21-multiscale-collisions/`.
Portable summaries and the independent full-fiber oracle are in this note
folder. The copied audit.py has exactly the executed script's bytes and
writes only to that new raw-run path; existing output files are not overwritten.

## Preservation and repository checks

The initial branch was main with nine inherited modified tracked files and
many pre-existing untracked research artifacts. Before this task's report
edits, a 416-file hash/length baseline and the existing tracked diff were
saved. The task adds its own note folder and dated appendices to T01 STATUS,
the project map, mechanism registry and open-lemma registry. Earlier proofs
and historical OPEN records are preserved. No staging or commit is authorized.

The required repository regression commands are validation, separate from
the six-set discovery budget. They execute existing fixed tests; they are
not an enlargement or rerun of this mathematical search.

| Check | Result |
|---|---|
| Local setup/reference checker | PASS: 50 local reference identities, 43 T03 manifest members and listed migration checks |
| Existing unit suite | PASS: 100 tests |
| Existing finite benchmark verifier | PASS: 159 checks; finite regressions, not proof of a target |
| Repository source/link check | PASS: 39 archived sources and links in 263 Markdown files; initial missing-ledger link resolved by completing this file |
| Whitespace and source hashes | PASS: tracked diff, new-note whitespace, 15 saved source/artifact identities, and byte-identical executed audit copy |
| Baseline preservation | PASS: 412 unchanged files; the four stated status files retain their original bytes as prefixes; no violation |

The independent referee subsequently read the saved main report and algebra
appendix and accepted their proofs, constants and scope. Its record includes
the checked document hashes. The six exact histograms were independently
computed; its final metric/tree-table check compared saved data rather than
recomputing those observables. No MC-O1 work was performed.

All changes remain uncommitted. The current task did not modify existing
code, historical proof content, archive manifests or prior raw outputs.
