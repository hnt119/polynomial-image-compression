# Proof, computation and preservation record

6 October 2026 · T03 · XB-O1 → Cross-Block Fiber Growth · version 1.

## Mathematical audit

The lead independently checked the accepted field, amplitude, projection,
spreading, saturation and source-count arguments. Specialist C independently
derived the field setup and read both final mathematical companions. Specialist
A additionally checked FG-F1's complete-target coverage and constants.
These are internal mathematical reviews, not external peer review or file checks.

| Proof obligation | Exact check and result |
|---|---|
| Field quantifiers | PASS: unique index-two subfield distinguished from the degree-two field over \(\mathbb Q\); \(K^+=F(\sqrt{21})\) and involution explicit |
| Coset distinctness | PASS: a five-position relation cannot be a nonzero seven-slot cyclotomic relation; all zero/opposite-index cases included |
| Norm normalization | PASS: \(N_{K/K^+}(z)=z\bar z=Q(x,y)\); not the absolute field norm to \(\mathbb Q\) |
| Scalar completion | PASS: all three patterns, both signs and eight scales included; both projections give the same real set |
| Input rate | PASS: at most two labels per \(X\); actual \(q^2/2\le n\le48q^2\), hence factor49 |
| Spreading | PASS: all permitted \(F\)-lines, including pure odd line and zero removal; fixed prefactor allowed by the live task |
| Expanded norm support | PASS: all three four-term coefficient vectors, opposite products, 33 frequencies and nonzero source coefficients |
| Cyclotomic cancellation | PASS: every relation constant on a seven-position block; target support saturation forces equality of cyclic arrays |
| Complete target inventory | PASS: every \(A^2\) target counted, not only orbit points; 32 possibilities per angular index and 48 scalar types |
| Source counting | PASS: 528 differences with a coefficient prime to7, exactly \(7q^3\) solutions each; divide by4 for actual ordered pairs |
| Constants and tail | PASS: threshold \(q\ge7392\), population \(n^2/18432\), cap \(48^2 32^4\), all fixed positive \(\varepsilon,\delta\) excluded |
| Relative-norm scope | PASS: at most \(8q/7\) cosets; iteration restricted to \(1\le\ell\le k-1\); no deduplicated-carrier image claim |

Final written proofs are [amplitudes.md](amplitudes.md) and
[fibers.md](fibers.md), with independent details in [audit.md](audit.md).
The only qualifications during review were the permitted prefactor in the
current spreading gate and the available range of iterated norms.
The final mathematical statements passed. Lead editorial corrections clarified
"squared complex absolute values / relative norms", clarified that FG-N1
uses its displayed seventh-root block product rather than an assumed literal
field norm at every label, and closed a display-math delimiter. None changed
a theorem. No new proof search followed the two scoped failures.

## Counter policy and enforcement

The policy was saved before the first mathematical program in
the local run folder's budget.json. Its initial bytes are retained as
budget-initial.json; the current ledger contains measured use.

- One charge per ordered \(Q\)-pair evaluation, norm-action/source membership
  test, projective equality or canonical-key calculation per scalar, or
  independent validation of one such calculation. Cached projective keys
  are still charged per scalar.
- Carrier-generation primitive arithmetic is timed but not separately charged
  as pair evaluations. Aborted runs would count; none occurred.
- Shared cap: 2,000,000 evaluations and 600 process CPU seconds.
  Discovery allowance: 1,600,000 evaluations and 480 seconds.
  Verification reserve: 400,000 evaluations and 120 seconds.
- Only the lead ran mathematical programs. All three specialists used zero
  mathematical evaluations and zero research-program CPU seconds.
- The scout preflighted each full square against the remaining discovery
  budget; counters are checked before charged operations, with a 470-second
  deadline. Validation uses the remaining verification allowance, a
  119-second deadline, and the global CPU check. Summaries persist on errors.

Two fixed sizes, \(k=1,2\), were chosen in advance. No parameter sweep,
larger case, or action-family scan occurred. The relative-norm proposal
failed algebraically and was not scouted. The first design's preliminary
phase choice was the only possible mutation; there was no post-selection repair.

## Exact arithmetic and reproducibility

Run folder, relative to the repository:

    local-only/runs/T03/2026-10-06-fiber-growth/

Mathematical commands actually executed, from the repository root:

    python3 local-only/runs/T03/2026-10-06-fiber-growth/scout.py
    python3 local-only/runs/T03/2026-10-06-fiber-growth/verify_scout.py

Runtime: **Python 3.12.7**, standard library only. No seed, floating-point
clustering, network, download or external API. The existing Field arithmetic
in experiments/modular_lift.py and its tests were inspected before import;
its experiment main was not invoked. The new scripts are local research
companions, not modifications to the repository arithmetic library.
Their exact bytes, the arithmetic dependency, and raw input/output files
are hashed in manifest.json. Reproduction requires this local run folder
as well as the repository; Git alone does not contain ignored local records.

The scout constructs the exact cyclotomic coefficient vectors of \(3A\).
Since \(Q(3x,3y)=9Q(x,y)\) and \(3\in F^\times\), scaling preserves
all scalar, image, fiber and projective-class counts. Values are reduced
modulo the exact cyclotomic polynomial; coefficient equality is exact.
Both \(A^2\) squares were exhaustively evaluated. Projective keys are
\(a/\sigma(a)\), with rational polynomial inversion and exact caching.

The independent validator rebuilt the entire output distribution using
\((x-\omega y)(x-\omega^2y)\) on representatives of
\((x,y),(y,x),(-x,-y),(-y,-x)\), weighted by the actual orbit sizes.
This covers all ordered pairs. It compared the full sorted distribution
hash, not only the image cardinality or histogram. It separately regrouped
every nonzero scalar through \(a\sigma(b)=b\sigma(a)\), without inversion.
Both cases and both projective methods passed.

These oracles use the same inspected field-reduction layer, so they are
independent norm/projective computations, not independent implementations
of all algebraic-number arithmetic. At \(k=1\), rational scalar arithmetic
was checked separately. None of these finite checks is a premise of FG-F1.

### Counters

| Category | Charged evaluations |
|---|---:|
| Discovery: full ordered \(Q\)-pairs | 1,050,914 |
| Discovery: new projective keys | 64 |
| Discovery: cached projective keys | 960 |
| **Discovery subtotal** | **1,051,938** |
| Verification: amplitude norms | 64 |
| Verification: initial complex-norm oracle | 1,313 |
| Verification: rational seed oracle | 289 |
| Verification: projective ratio oracle | 64 |
| Verification: full symmetry-orbit norm reconstruction | 263,250 |
| Verification: projective cross products | 18,952 |
| **Verification subtotal** | **283,932** |
| **Shared total** | **1,335,870** |

Scout CPU: 25.657741 seconds. Reserved validator CPU: 10.076273 seconds.
The authoritative combined measurement is **35.734223 seconds**; the
microsecond difference from adding rounded stage fields is final accounting
overhead. Timers cover mathematical work from budget initialization, including
carrier construction and all validation; interpreter startup/imports and
file-only metadata before the timers are not measured. Total evaluations
leave 664,130 unused, including 116,068 unused
verification evaluations. The cycle stopped by proof, not budget exhaustion.
Program usage is not model-token, credit, or total wall-time usage.

The complete pair-weighted fiber and projective histograms are in data.json.
The raw case files save exact \(3A\) and the field moduli. Output values are
reproducible from those inputs; the stored full-distribution hashes detect
any disagreement in both values and multiplicities.

## Source and worktree preservation

Orientation covered Git status/diffs, setup, map and migration audit,
master handoff, T03 current state, SPEC/STATUS, migration conflicts,
the latest cross-block and linked proofs, mechanism/failure/open-lemma entries,
and the construction ledger template. Unrelated historical experiments and
proofs were not rerun. No unavailable source was reconstructed.

The worktree already had modified tracked files and extensive untracked work.
A baseline of 304 preexisting nonignored files, inherited diff and inherited
status are saved in the run folder. Earlier checkpoints, SPECs, code, tests,
canonical manifests and private source copies are preserved. Five global
handoffs receive only dated suffixes, with exact pre-append byte copies.
The new report manifest excludes itself. During this task, a separate T01
variable-gap cycle appended its own status and four shared handoffs. Their
original prefixes match the baseline, and those concurrent additions were
retained before our suffixes. They are not work or mathematical claims of
this T03 cycle.

Repository/hash/formatting checks below are administrative validation, not
mathematical experiments. They do not substitute for the proof audits.
No repository library or test code changed, and unrelated historical regression
experiments were not rerun; the new local scouts received the full reserved
validation described above. Nothing is staged, committed, pushed, reset or cleaned.

## Repository verification results

| Command or check | Result |
|---|---|
| python3 scripts/check_repository.py | PASS: 39 archived sources and local links in 178 Markdown files |
| python3 scripts/check_codex_setup.py | PASS: 50 local references, original import identities, 43 T03 members, duplicate states and C4 hashes |
| git diff --check | PASS |
| New Markdown whitespace, tables and math delimiters | PASS |
| Initial 304-file baseline | All original bytes preserved; 298 whole files unchanged, remaining files preserve their original prefixes |
| Five task handoff appends | PASS: exact pre-append bytes plus exact recorded suffixes |
| Concurrent T01 additions | Preserved: four shared handoffs and T01 STATUS; separately identified, not attributed to this task |
| Companion/source/run hashes | Verified against saved bytes; final manifest excludes itself |

The initial packaging checks caught an as-yet unwritten manifest link and
an unescaped table delimiter; both were corrected before the passing check.
The first preservation assertion also detected concurrent T01 additions;
prefix hashes established their exact scope without modifying them.
These were packaging issues, not mathematical scout or proof failures.
No code, archive or historical-source repair was needed. All work remains
uncommitted.
