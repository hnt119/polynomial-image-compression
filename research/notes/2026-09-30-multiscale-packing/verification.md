# Verification and reproducibility record

## Mathematical audit performed

This record covers the 2026-09-30 offline multiscale-packing cycle only.
The lead read and independently reconstructed the new arguments; the
specialized internal auditor independently checked them. This is more than
a documentation-integrity check, but is not external peer review.

| Claim | Lead check and evidence | Scope |
|---|---|---|
| MP-L1 local seed | Substituted the multiplier matrix, checked both denominator congruences and all five norm classes; reconstructed return histogram {2:6,4:4,6:6} | Sixteen ordered pairs, no asymptotic extrapolation |
| MP-L2 local seed | Reconstructed rational/radical norm tables, the 48 mixed pairs, three common positive norm shells and twelve irrational outputs; checked total121, histogram, means and full image24 | Exact hand classification, no numerical tests |
| MP-L3 coordinate reuse | Checked sine doubling and both decoded scalar projections; checked sine equality fibers and union counts | Actual values, not injective formal addresses |
| MS-C1 | Verified the involution fixes omega, including depth-one sign of i; matrix entries have common parity; opposite scalar parities exclude every nonmonomial action; the only monomial actions are ±1 | Entire selected cyclic group, all nonzero opposite-parity sources |
| MS-C1 pair count | Reconstructed B union gamma0 B; actual parity counts between max(b0,b1) and b0+b1 imply ratio at most2 and ordered count at least4(n−1)^2/9 | Allows all same-parity projection collisions |
| MS-C2 | Verified four distinct F-lines using gamma0²≠1; their exact nonzero populations are b0,b1,b0,b1; at least half the ordered nonzero square is F-independent | The specified mixed-amplitude carrier |
| MS-C2 action count | For independent x,y the first-coordinate map F²→K is an isomorphism; each target line has a one-dimensional coefficient preimage; the norm equation has at most2 solutions per line per parity | Bound16 counts actual actions, hence distinct targets; no actual-image bound |
| Signed rate | Used n→infinity and fixed epsilon before depth; compared a constant fraction of n² with n^(2−delta) for each fixed delta>0 | No unsupported exact lambda or almost-everywhere rho formula |
| Inherited fixed-field gate | Checked the stated affine recursion satisfies the frozen theorem's fixed-field, denominator and all-conjugate-height assumptions | An application of T03 current state §6.3, not a new global ideal theorem |

### Corrections incorporated before acceptance

1. The fixed-field affine preselection uses \(M^{d+1}\) to clear the seed
   as well as the maps; \(M^d\) would require an integral seed.
2. That gate is an application of an inherited theorem, not a new finalist.
3. At depth one the involution sends \(i\) to \(-i\); sine parity shifts
   accordingly. Eigenpurity, the population count and the obstruction remain.
4. The architect's initial orbit-decoding transcription had the wrong first
   coordinate shift. The correct identity is
   \(\phi^{-1}(\sqrt3\zeta^r)=(s_{r-m/3},s_r)\),
   \(s_r=-2\sin(r\theta)\), with first coordinate
   \(\sqrt3\cos(r\theta)+\sin(r\theta)\). The local proof already used
   this sign. The independent auditor found the error and the lead verified
   the correction; equal projection sets and both theorems are unchanged.
5. Rates are bounds: exact \(\lambda\) is unproved, and the bounded-return
   population rules out near-full \(\rho>1\), without establishing one
   common return asymptotic for almost all sources.

## Budget and execution provenance

| Item | Used | Authorized cap |
|---|---:|---:|
| New research program executions | 0 | Stop at failed theoretical gates |
| Charged exact program evaluations | 0 | 2,000,000 |
| Research-program CPU seconds | 0 | 600 |
| Local gadgets | 2 | 3 |
| Serious scalar definitions | 2 | 2 |
| Related follow-up mutations | 1 | At most1 per construction |
| Specialized subagents | 3 | 4 |

The lead retained the exact-scout role; no candidate survived the analytic
gate for program scouting. Symbolic proof work and hand table derivation
are not measured CPU runs. No research command, runtime, seed or executable
hash exists for this cycle because none was executed. Documentation/hash
scripts and repository checks are recorded separately below. No research
budget was spent rerunning frozen experiments, and no unused budget was
spent after the stop rule.

## Sources and file preservation

Read the setup/map/migration records, master handoff, relevant current T03
state and frozen modular-lift checkpoint, T03 SPEC/STATUS, migration conflicts,
mechanism/failure/open-lemma entries, construction template and the exact
DC-R1 source. Historical source files, SPECs, imported programs, canonical
archive manifests and prior checkpoint files were not edited.

The initial worktree was already dirty. A 270-file initial hash snapshot,
inherited status and inherited patch are preserved locally under
`local-only/runs/T03/2026-09-30-multiscale-packing/`.
Before this task appended its handoffs, four shared index files and the T01
STATUS had changed from that snapshot through concurrent T01 work. Those
changes were retained. Complete byte copies of each of this task's five
pre-append handoff files and exact appended suffixes are preserved there.
The preservation check compares this task's changes to those immediate
pre-append copies, rather than attributing concurrent changes to this cycle.

New report companions are indexed by `manifest.json`; it hashes all companion
files except itself. The checks log resides in the ignored local run folder.
No code, tests or examples were added. No stage, commit, push, reset, clean,
remote change, network call or literature search was performed.

## Repository checks

| Command/check | Result |
|---|---|
| `python3 scripts/check_repository.py` | PASS: 39 archived files; local links in155 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 50 local reference files, original import identities,43 T03 manifest members, duplicate states and C4 hashes |
| `git diff --check` | PASS |
| New report Markdown table/whitespace check | PASS after correcting raw cardinality bars inside table cells |
| Five handoff prefix/suffix comparisons | PASS: exact immediate pre-append bytes retained |
| Initial270-file baseline comparison | No unexpected changed files beyond five recorded handoffs and concurrent T01 STATUS |
| New companion manifest | SHA256/byte counts checked; manifest excludes itself |

These validate documentation and local source identity, not additional
mathematical theorems. The custom formatting check initially caught one
remaining raw absolute-value bar in a Markdown table; it was corrected
without mathematical change and the check repeated. All new proof files
were read separately because ordinary `git diff` omits untracked content.
No code changed, so unit tests and the experiment regression suite were
not rerun. All work remains uncommitted; inherited modifications are retained.
