# Offline verification and computation ledger

**16 September 2026, version 1.** This record separates mathematical proof
review, numerical work and file-integrity checks.

## 1. Authorization and exact outcome

The local user attachment commissioned only the frozen HR-N1 assertion for
$Q$, $A_L$, $u,v$ and the $|r|,|s|\le8L$ window. The lead announced the
offline policy and shared limits before the research assignments. Every
agent received the same no-network restriction and a symbolic-only budget.

HN1-1 verifies the exact input count, matrices/inverses, label injectivity,
scalar recovery and nine depth-order types. HN1-2/3 disprove HR-N1 through
a positive-density identity-only class on $L=10m$, $m\ge2$. The full proof
and failure scope are in [the report](README.md).

## 2. What was read and what was proved

- The user attachment, root instructions, setup guide, project map,
  migration audit and existing Git changes were inspected locally.
- The master handoff, T03 state, SPEC/STATUS, conflict and mechanism/failure/
  open-lemma records established historical scope. ZIP members were listed
  before companion headers were inspected. This orientation is not a new
  audit of the adaptive TCRC proofs.
- The preceding high-return report and relevant complete HR-1 and HR-2–HR-4
  arguments were read. Their files remain unchanged. The one-prime
  full-image theorem was not silently applied to the two-prime carrier.
- The lead derived HN1-2/3. One agent independently derived HN1-1; another
  independently checked every step of the proposed no-go, including signs,
  both $7$-depth orderings, the target-coordinate swap, the $f=0$ edge case,
  the prime-power square congruence and the subsequence quantifiers.
- The lead read the completed local-action and independent-audit notes.
  These are internal independent proof inspections. No source hash, finite
  example or agent agreement substitutes for the written arguments.
- The local-action author also independently read the complete final
  HN1-2/3 argument and passed its joint-prime proof and quantifier checks.
  Both reviewers identified a cosmetic TeX error, which the lead corrected.

The existing standalone F25 source gap and separate checkpoint designation
issue are not needed for this proof. No necessary proof dependency is
missing. No external source, theorem locator or novelty claim was introduced.

## 3. Actual research computation budget

| Item | Actual use |
|---|---:|
| Announced global evaluation cap | 2,000,000 |
| Announced research CPU cap | 600 seconds |
| New action–pair or polynomial evaluations | **0** |
| Independent finite numerical oracles | **0** |
| Research reruns | **0** |
| Research-program CPU time | **0 seconds** |
| Exhaustive HR-N1 cases run | **None** |
| Research-program errors | Not applicable: no research program executed |

The optional $L=1,2$ enumeration was conditional on an unresolved mechanism
after the analytic screen. The no-go closed the assertion first, so that
conditional diagnostic was not commissioned for execution. No $L=3$ or
larger carrier was enumerated. The exact inequalities at $m=2$ in the proof
are an induction base case, not a finite carrier experiment.

The generators and inverses were independently checked by symbolic norm
and matrix identities. No finite oracle was needed or executed. There are
therefore no newly measured return histograms, image multiplicities, seeds
or experimental rates to report. The preceding cycle's data are not reused
as evidence for the new theorem.

All files added or modified in this cycle are documentation/provenance.
No reusable experiment module or test changed, so `unittest discover` and
`python3 -m experiments verify` were not rerun. Those programs are local but
would execute mathematical regressions unrelated to this documentation-only
implementation. The commissioned work itself includes new symbolic proof
research; it is not being described as a documentation-only research cycle.

## 4. Offline enforcement and local check requirements

**No network access was attempted by any agent in this cycle.** There were
no web searches, browser calls, external APIs, connectors, downloads, package
installations or remote Git operations. External links encountered in local
documents were treated as provenance strings and never followed. There was
no request to relax the offline boundary.

Both verification scripts were inspected before execution:

- `scripts/check_repository.py` uses only local archive hashes and local
  Markdown destinations. Its `urllib.parse` import parses strings; links
  with a scheme or host are skipped, not fetched.
- `scripts/check_codex_setup.py` uses local manifests, byte/hash comparisons,
  ZIP CRC/member reads and existing files. It performs no extraction,
  research import, pickle deserialization or network operation.
- `git diff --check`, local Git status/diffs and the additional prefix/hash
  checks operate only on this checkout.

The local environment supplies the Python standard library required by
these checks. Commands, runtime version, exit codes, elapsed time and output
are recorded in the ignored file
`local-only/runs/T03/2026-09-16-hr-n1-offline/checks.json`.

Checks used **Python 3.12.7**. All commands below exited successfully.
Elapsed times measure local validation, not mathematical research CPU.

| Command/check | Result | Elapsed wall time |
|---|---|---:|
| `python3 scripts/check_repository.py` | PASS: 39 archived sources; local destinations in 58 Markdown files | 0.082 s |
| `python3 scripts/check_codex_setup.py` | PASS: 42 local reference files, original import identities, 43 T03 manifest members, duplicate states and C4 hashes | 0.095 s |
| `git diff --check` | PASS: no tracked whitespace errors | 0.025 s |
| New-note `git diff --no-index --check /dev/null <file>` checks | PASS: all four new Markdown files, checked separately from tracked diffs | Recorded as per-file pass |
| Protected-file SHA-256 comparison | PASS: all 55 baseline hashes unchanged | File-integrity check |
| Original navigation byte-prefix comparison | PASS: all five original files preserved exactly before their dated appendices | File-integrity check |

The final manifest and amended verification record also receive a local
hash/whitespace check after manifest creation. No unavailable dependency or
network-dependent check blocked completion. These checks verify packaging
and preservation; they are not mathematical experiments or proof substitutes.

## 5. Preservation and file changes

Before navigation edits, the lead saved exact byte copies of all five append
targets and a local copy of the inherited Git diff. It also recorded hashes
for 55 protected prior-report, setup, SPEC and migration files. These local
records are in `local-only/runs/T03/2026-09-16-hr-n1-offline/` and are not
intended for commits.

This cycle creates the fresh note directory
`research/notes/2026-09-16-hr-n1-offline/` and appends dated entries to:

1. `research/CURRENT_PROJECT_MAP.md`;
2. `research/tracks/03-eisenstein-cartesianization/STATUS.md`;
3. `research/MECHANISM_LIBRARY.md`;
4. `research/FAILURE_LIBRARY.md`;
5. `research/OPEN_LEMMAS.md`.

The old OPEN/untested HR-N1 wording remains in its completed report as
historical context; the new dated entries identify the controlling later
proof. RC15/4, the four fixed track polynomials, the original archive,
migration sources, existing SPECs and all preceding reports are preserved.
No staging, commit, push, reset, clean or remote change occurred. All work
remains uncommitted.

The final manifest hashes the new report/proof/verification files and records
the final navigation identities. Private source/baseline identities remain
in the ignored local run directory. The manifest does not claim that hashing
constitutes proof verification.
