# Three-branch cycle: verification and handoff

Date: 2026-09-16. This file records this cycle's work, not inherited work.
No network or external publication occurred. The research enumeration ran
once, within the predeclared 1,000-gadget / two-composition budget.

## Mathematical audit

The lead independently checked the symbolic companion's six proofs: analytic
rigidity, reversed input identity obstruction, rational factorization via
the rational function field and pole/degree arguments, generic-seed
injectivity and full count, translation example, and finite adaptive packet
bound. The genericity hypothesis and restriction to within-packet savings
are essential and retained. Claim IDs were made unique as TB-A1–A6.

The lead also checked the source companion's elementary 3-adic induction,
correlated-subset density inequality, and linear tensor obstruction. The
continuous-cover proof was read in the located original checkpoint. The
unavailable full digital and rich-fiber proofs were not independently
recertified. Arithmetic tower PDFs and the cited external primary papers
were not used for a new construction.

The progression tail theorem TB-P1 was derived by the lead and independently
checked by the symbolic agent. The exact 22-value gadget was checked by the
lead both as a nine-block union and as seven disjoint surviving difference
slices, alongside the agent's Fraction computation and independent test
oracle. These are internal audits, not external review or novelty checks.

## Computation and recorded correction

Command: `python3 -m experiments.three_branch_lift`.
Runtime: CPython 3.12.7, approximately 0.625 seconds for the bounded run.
Exact `fractions.Fraction` arithmetic; no randomness, network, or dependencies.
980 attempts, 423 legal gadgets, 557 rejected systems, 79 finite normalized
gains, and two composition checks. Complete local data and run metadata are
under `local-only/runs/T01/2026-09-16-three-branch-lift/`.

The script was inspected before execution. An initial provisional hand count
of 22 for the **integer** six-point comparison gadget was wrong; the exact
run returned 24 and the first targeted test failed on that expectation. The
table and expectation were corrected. The **step-1/3** six-point gadget has
22 outputs, independently certified. This was a correction to a test's hand
count, not a change to the computational algorithm. The execution history
is preserved in local `verification.json`; `provenance.json`'s empty errors
array refers only to the successful enumeration itself.

After the run, the script's docstring phrase “18 outputs” was corrected to
“18 enlarged input values”; there was no computational change or rerun.

| Artifact/version | SHA-256 |
|---|---|
| Code used for the bounded run | `f424e8a8ea4404c093f6fee5a2ae6f7f105be066ba8be059d0c943a47e4f601c` |
| Current code after docstring correction | `63dd434f094b3380a0a93fed5e58636d7684c86db17a788e3f5be078edabb1a6` |
| Exact grid input serialization | `1dd284e857c991ee419581d4f0c01f960580cb313fa77a235e17226606c41a4a` |
| Complete raw gadget data | `faf09047e157936db23fecac2e8124855699e9584b7eadba8ece302efc8b4da4` |
| Portable example/count record | `1a1e0f31dcb9b4d22c4011f28a09aee9198ebe636c3d78c3655f9b9abc36904e` |
| Final targeted test source | `edbd9902882f5b4e47003b448f274e28fa65636df732a17986fbbbbeda0044d8` |

The six targeted tests pass, including a separately specified 22-value support
and block-membership oracle, all 511 possible nonempty block-intersection
selections for the comparison gadget, and rejection of overlapping inputs.
No larger research grid was launched during validation.

## Repository checks and changes

- `python3 -m unittest discover -s tests -v`: **PASS, 48 tests**.
- `python3 -m experiments verify`: **PASS, 159 finite baseline checks**.
- `python3 scripts/check_codex_setup.py`: **PASS, 42 references and 43 T03
  archive manifest members**, plus original import/duplicate/C4 identities.
- `python3 scripts/check_repository.py`: **PASS, 39 archived sources and
  links in 68 Markdown files**. The first lead check, before this verification
  file existed, correctly reported its temporary missing link; the completed
  report passes. An earlier subagent check observed transient missing links
  in concurrently produced two-prime-character work; this task did not edit
  that work, and those failures are absent in the final check.
- `git diff --check`: **PASS**. Tracked diffs and new files were inspected
  separately; no inherited change was reverted or claimed as new work.
- Stored raw/portable JSON and current code/test SHA-256 values: **verified**
  against the preserved provenance records without rerunning the search.

The existing 39-file archive and four SPECs remain unchanged. This cycle
adds its report, two proof companions, this verification record, one exact
experiment module, its tests, portable counts, and ignored raw data. Dated
T01 status/project-map addenda only point to the new result and preserve the
OPEN ultimate target. Earlier modified files and untracked research work
remain inherited, including concurrent work in other branches. No reset,
clean, staging, commit, push, or remote change was performed. Everything
from this cycle remains uncommitted.

These checks establish packaging and the stated finite regressions. They
do not prove the asymptotic T01 objective; the analytic proofs and their
limited scopes are in the report and companions.
