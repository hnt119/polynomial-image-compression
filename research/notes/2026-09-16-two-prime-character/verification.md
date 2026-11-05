# Two-prime character cycle — verification and provenance

**16 September 2026, version 1.** Track T03; fixed polynomial
$Q(x,y)=x^2+xy+y^2$. This record accompanies the
[report](README.md), [one-block proof](local-count-proof.md),
[product and realization proof](product-realization.md), and
[file manifest](manifest.json).

## Authorization and scope

The latest user attachment, **Full-Rank C0 Extension — First Cartesian
Norm-Symmetry Cycle**, authorized one genuinely correlated $7,19$ model,
an exact one-block distribution, product/tail proofs, and a fully charged
scalar-realization audit. The selected model and shared limits were announced
before execution: **2,000,000 charged evaluations; 600 research CPU seconds**.
The network policy was **strictly offline**. No web, browser, connector,
network command, download, installation, remote Git operation or literature
search occurred. Prior closed carriers were not rerun as research cases.

The current attachment supersedes the earlier documentation-only assignment
for this new cycle. It does not reopen HR-N1. The cycle stops at the
homogeneous real realization failure; no difference-set or affine search,
replacement conjecture, or further proof obligation was started.

## Mathematical sources and inspections

- The setup guide, current project map, migration audit, master handoff,
  T03 current state, relevant final checkpoint/companions, T03 SPEC/STATUS,
  migration conflicts, and mechanism/failure/open-lemma entries were read
  for orientation and status. These are distinct from proof evidence.
- The existing [HR-1 proof](../2026-09-16-high-return/return-lemma.md)
  supplies the support implication. This cycle applies its finite-fiber
  argument to a finite-ring observable, with an explicit warning that
  encoding output labels is not a realization as real scalar $Q$.
- The [correlated-CRT checkpoint](../../history-sources/Q_Correlated_CRT_Tensorization_Checkpoint.md),
  §C, Theorem 1, and its sign-cube proof were inspected. Its hypothesis that
  $3$ is nonsquare in every factor holds here. Its scope is a normalized
  local certificate, not an arbitrary real-image lower bound.
- Corrected C0 and its correction log were consulted as local project
  context. No new proof of C0, general norm identity, or literature claim
  is part of this cycle.
- The [HR-N1 final freeze](../2026-09-16-hr-n1-final-freeze/README.md)
  is retained as completed project context, not rerun or repaired.

### Internal proof and code review

| Review | Actual scope and outcome |
|---|---|
| One-block derivation | A separate analyst derived TP-L1 symbolically: split orbits, all character sign counts, norm-zero lines, the complete histogram, and whole modular image. The lead inspected the full argument. PASS. |
| Product/realization derivation | A separate analyst proved the exact product law, trivial stabilizers, moment tails, HR-1 support application, and bounded real action image. The lead inspected the complete written argument, including the additional zero-preserving projection theorem. PASS. |
| Cross-check of TP-L1 | The product analyst independently read TP-L1 and checked the orbit/sign table, isotropic multiplicities, histogram, mean, geometric expression, and 130 outputs. PASS. |
| Pre-execution code audit | Exact modular arithmetic, all-pair coverage, independent split-coordinate oracle, and the planned 653,787 charges were inspected. Output-path distinctness, no-overwrite behavior and final CPU checks were tightened before the first diagnostic run. |
| Final report consistency | Separate read-only review passed all constants, tail bounds, local/real distinctions, verdict and next-obligation scope. Two clarity edits separated ring notation from return notation and identified $2772^d$ explicitly as an upper bound, not an exact exception count. No theorem changed. |

These are internal reviews. They are not external peer review and do not
establish novelty. TP-G1 in the report aliases TP-R1 in the companion.

The reviewed quantifiers fix the block before $d$ grows. All pairs are
ordered, every stabilizer is one including isotropic states, and within-block
correlation is retained. Product independence follows from the exact input
square. All scalar-realization failures state their additional hypotheses.
Unknown real input, denominator, height and number-field costs are not zero.

## Exact diagnostic: one run

Python runtime: **3.12.7**. Source:
[experiments/two_prime_character.py](../../../experiments/two_prime_character.py).
The source was inspected before execution, remained unchanged afterward,
and has SHA-256
`76671503a828cf7bf76cd316266bec8adc4b14ca5c6cdfdea93196a939e1a7e3`.

Actual command from the repository root:

```bash
python3 -m experiments.two_prime_character \
  --output examples/2026-09-16-two-prime-character.json \
  --pairs-output local-only/runs/T03/2026-09-16-two-prime-character/pairs.json
```

For reproduction use new output filenames: the program refuses overwrites.
It uses the Python standard library, deterministic exhaustive loops, and no
seed. The exact diagnostic and independent oracle covered every one of the
2916 pairs and all 108 actions. The oracle matched each returned-pair set
through its canonical hash as well as the counts and norm values.

| Charge | Count |
|---|---:|
| Main norm-one candidates | 17,689 |
| Main polynomial evaluations in the residue ring | 2,916 |
| Main action-pair tests | 314,928 |
| Oracle norm candidates in the two fields | 410 |
| Oracle polynomial evaluations in the residue ring | 2,916 |
| Oracle action-pair tests | 314,928 |
| **Total diagnostic** | **653,787** |

Research CPU: **0.691836 seconds**; wall time: **0.6989277499960735 seconds**.
The two component norms in the oracle form one residue-ring polynomial
evaluation. Group-membership and action queries are separately charged.
Approximate logarithms/geometric means are presentation only; all equalities,
returned sets, integer histograms, and rational statistics use exact arithmetic.

Results: [public summary](../../../examples/2026-09-16-two-prime-character.json).
The local `pairs.json` retains all per-pair values, counts, stabilizers and
returned-set hashes. No product dimension was enumerated: its all-depth
statements are proved analytically.

## Required fixed regression checks and shared budget

All relevant existing modules and tests were inspected before execution.
The standard commands were executed using an inspected local `runpy` guard:

```bash
python3 -m unittest discover -s tests -v
python3 -m experiments verify
```

The guard retains equivalent module arguments, output and timing, and
conservatively charges **every Python function call in `experiments/` or
`tests/`**, including helpers and generator resumptions. This deliberately
overcounts mathematical queries. It enforces the same shared caps and is
stored with logs in `local-only/runs/T03/2026-09-16-two-prime-character/`.
The fixed regression suite does not expand the authorized carrier search.

| Execution | Result | Additional charges | CPU seconds |
|---|---|---:|---:|
| First regression wrapper | Import-path failure; no mathematical test ran | 6 | 0.048576 |
| Corrected unit wrapper | **42 tests PASS** | 57,178 | 2.007706 |
| Finite baseline verification | **159 checks PASS** | 25,386 | 0.859286 |
| **Regression subtotal** | Failure retained and charged | **82,570** | **2.915568** |
| **Entire research/validation total** | Under both shared limits | **736,357** | **3.607404** |

The first wrapper omitted the repository from `sys.path`; adding it fixed
the wrapper without changing mathematical source or tests. Its six import
attempts and CPU time are included, and the first wrapper copy and error log
are retained. The exact new diagnostic itself ran once without failure.
No further mathematical rerun was performed for documentation.

## Files and preservation

This cycle adds the new note directory, one standalone experiment module,
and one exact example JSON. Only after the mathematical work was complete,
dated navigation/status records were appended to the current project map,
T03 STATUS, and the failure, mechanism and open-lemma libraries. These
records retain HR-N1 as closed and T03/ARG/TCRC/RC15/4 as OPEN.

The checkout was already dirty. Its initial nine tracked-file diffs contained
957 insertions and 58 deletions; those are inherited work, not this cycle's
changes. A local baseline preserves 90 source hashes, exact original bytes
of the five append targets, and the initial tracked diff. Historical
mathematical reports, SPECs, imported archives, canonical registries, existing
experiments and tests were not edited. No staging, commit, reset, cleanup,
push or remote change was requested or performed.

Repository/reference checks and baseline comparisons are documented in the
final validation section below. They check links, byte integrity and
formatting; they are not mathematical proof audits.

## Final validation

| Check actually performed | Result |
|---|---|
| `python3 scripts/check_repository.py`, initial completed-artifact check | PASS: 39 archived source files and local links in 66 Markdown files |
| Same command, intermediate recheck after metadata completion | Temporarily FAILED on an unrelated missing `verification.md` link in `research/notes/2026-09-16-three-branch-lift/README.md`. This separate report was present before this cycle; it was left untouched. |
| Same command, after observing that the separate file had appeared | PASS: 39 archived sources and local links in 68 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 42 local references, original import identities, 43 T03 manifest members, duplicate states and C4 hashes; no research code executed |
| `git diff --check` | PASS |
| Separate `git diff --no-index --check /dev/null FILE` on seven new files | PASS; covers untracked artifacts absent from the ordinary diff |
| Protected-file hashes | PASS: all 90 baseline identities unchanged |
| Append-target original-byte prefixes | PASS: all five preserved |
| Other inherited tracked diff blocks | PASS: all eight unchanged; only the authorized T03 STATUS append changes the ninth |
| Exact-run source identity | PASS: matches the source hash recorded above |
| Final report review | PASS: constants, scope, verdict and sole next obligation; clarity edits recorded above |

The separate verification file appeared without edits by this cycle, so a
new repository check was justified and passed. The temporary failure is
retained as chronology. No mathematical failure or broken link in this
cycle's report was reported. No historical content was reconstructed to
repair the separate report.

The local `preservation.json` records these byte-comparison counts. The
manifest separately identifies the finished proof/report/code/output files,
dependencies, our original state-file prefixes and exact appended sections,
and retained raw records by SHA-256.
Its own digest is not recursively included. Metadata/formatting checks do
not call the research programs and do not alter the research charge totals.

An unrelated T01 appendix appeared between the original project-map prefix
and this cycle's appendix during finalization. Whole-file and combined-prefix
comparisons correctly detected that change. The original baseline prefix and
our exact appended section remain byte-identical; concatenating those two
recovers the previously recorded snapshot hash. The manifest records these
pieces separately. This does not claim the shared navigation files are
immutable or attribute other additions to this cycle. Earlier inherited-diff
comparisons describe their stated preservation checkpoint.

The final state remains uncommitted. The check counts and proof reviews are
reported separately: repository checks do not prove the mathematical claims,
and the one-block experiment does not substitute for the all-depth proofs.
