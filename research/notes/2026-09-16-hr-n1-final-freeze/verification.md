# HR-N1 final freeze — audit and local verification record

**16 September 2026, version 1.** Scope: final proof audit, documentation,
and research handoff. This is not a new constructive research cycle.

## 1. Mathematical and documentary inspection

The lead inspected the completed HN1-1 local-action proof, HN1-2 dominant-gap
argument, HN1-3 counting and quantified contradiction, written independent
audit, completed verification record, and HR-1 support implication. The final
report restates these proofs and does not strengthen their parameter range
or conclusion.

A delegated proof reader inspected the completed arguments and the final
report independently. The checklist included signed exponents, denominator
clearing, integrality, field/norm conventions, simultaneous prime constraints,
the prime-power factor allocation, the explicit constant and quantifier order.
The reader found no mathematical gap and passed the final A–O report.

A separate source reader checked the T03 state and latest archive companions
for the exact RC15/4 hypotheses, ARG/TCRC statuses and existing next obligation.
The reader also checked final-report §§C, H, J and L. This was a documentary
source-fidelity check, not a new audit of all adaptive-family proofs.

The controlling sources establish a direct HR-1 implication for the rational
carrier's own image. A transfer from that carrier to the actual adaptive
root sets is **UNKNOWN FROM CURRENT RECORD**. The report states that limit
explicitly; it does not invent the missing bridge.

## 2. Corrections made to this freeze draft

- Replaced a dangling TeX backslash in the quantified statement with spacing.
- Replaced raw absolute-value bars in two Markdown table cells with
  `\lvert` and `\rvert`.
- Clarified that the pairs have *return count* one, and made integer exponent
  labels explicit in the finite-window definition.
- Clarified that the displayed root component belongs to the **comparison
  lift**, without identifying its parameter with the actual optimizer.
- Displayed the unchanged ultimate target's quantifiers and the finiteness
  of RC15/4's uniform constant explicitly.

These are presentation/definition clarifications. They do not change HN1-1,
HN1-2, HN1-3, the constant 1/200, the range L=10m with m>=2, or the scope
of the all-integer-power obstruction. No historical proof file was edited.

The two internal reviews from the **completed research cycle** are recorded
separately in final-report §L: one has a standalone audit text; the second
is reported in the completed verification record. This freeze's additional
checks are not substituted for, or described as external peer review of,
those records. The second review's detailed separate transcript is not
present in the completed file set; no such document is invented.

## 3. Computation and offline boundary

| Item | Actual freeze usage |
|---|---:|
| Charged mathematical evaluations | 0 |
| Research-program CPU seconds | 0 |
| Carrier enumerations, finite oracles, research reruns | 0 |
| Network attempts | 0 |

The completed cycle also used zero charged evaluations and zero
research-program CPU seconds. Its analytic obstruction made the conditional
enumeration unnecessary. No new experimental claim is made here.

Only local files, Git inspection, local tools and Python's standard library
were used. There was no web/browser/connector/API call, remote Git operation,
download, installation or literature search. Archive members were listed
before reading; no archive program, pickle or mathematical certificate was
executed or deserialized.

## 4. Local check requirements and actual results

Both checker scripts were inspected before execution:

- `scripts/check_repository.py` checks local archived hashes and Markdown
  destinations. `urllib.parse` parses links as strings; external URLs are
  skipped without network access.
- `scripts/check_codex_setup.py` checks local manifests, hashes, ZIP members,
  duplicate states and C4 identities, without running research code.

No experiment/test code changed. The mathematical regression programs
`unittest discover` and `python3 -m experiments verify` were not run, since
this freeze only changes documentation/state records. Packaging checks are
not treated as mathematical proof evidence.

**Actual final-freeze checks: PASS, using Python 3.12.7.**

| Command or check | Result | Elapsed wall time |
|---|---|---:|
| `python3 scripts/check_repository.py` | 39 archived sources; local destinations in 60 Markdown files | 0.091 s |
| `python3 scripts/check_codex_setup.py` | 42 local reference files, original import identities, 43 T03 archive members, duplicate states and C4 hashes | 0.146 s |
| `git diff --check` | No tracked whitespace errors | 0.037 s |
| New-file `git diff --no-index --check /dev/null <file>` checks | All four final-freeze files pass | Per-file pass recorded |
| Baseline SHA-256 comparisons | All 71 protected files unchanged | Local file check |
| Navigation byte-prefix comparison | All five original files preserved before the new appendices | Local file check |
| Inherited tracked-diff comparison | All eight other tracked diff blocks unchanged; T03 STATUS has only its new appendix | Local file check |
| Report structure / machine state | A–O present in order; separate YAML file equals the final report block exactly | Local text check |
| Markdown table structure | Consistent cell counts in both new Markdown files | Local text check |

These are validation wall times, not research-program CPU usage. All three
listed commands returned exit code zero. New-file whitespace checks accept
Git's ordinary no-index difference exit code only when no whitespace errors
are emitted. The final manifest records the completed file identities; a
final identity/whitespace check includes this amended record and manifest.
No dependency or network limitation blocked validation. Detailed command
outputs and timings are preserved in the ignored local `checks.json`.

## 5. Preservation and final file scope

Before editing, a local baseline saved SHA-256 identities for 71 existing
note, migration and SPEC files, exact copies of the five navigation targets,
and the complete inherited tracked diff. The private baseline and raw check
outputs are under
`local-only/runs/T03/2026-09-16-hr-n1-final-freeze/`.

New files are confined to this dated final-freeze directory:

- `README.md`: self-contained final report, sections A–O;
- `final-state.yaml`: exact copy of the report's final YAML block;
- `verification.md`: this audit/check record;
- `manifest.json`: final report/source identities and validation summary.

Only dated appendices are added to the project map, T03 STATUS, failure
library, open-lemma registry and mechanism library. Their original byte
prefixes are retained. All completed reports, historical sources, SPECs,
archives and canonical manifests remain unchanged. Historical navigation
hashes in older manifests remain historical snapshots; they are not rewritten
to conceal the new appendices.

No file was staged or committed. There was no reset, clean, push or remote
change. Inherited work remains uncommitted alongside the freeze files.
