# VO-O1 source, status and verification ledger

T01 | 11 October 2026 | version 1 | offline proof verification and documentation.

## Verdict and claim record

**PROVED - VO-C6; VO-O1 resolved negatively in its exact signed-role scope.**
The lead and an independent mathematical referee verified the complete
user-supplied argument manually. There is no mathematical correction to
the supplied proof. This is an internal independent audit, not external
review, a numerical certificate or a novelty claim.

| Record | Exact scope |
| --- | --- |
| Track / polynomial | T01; P(x,y)=(x-y)^3+x+y; the fixed same-set real target remains OPEN |
| Quantifiers | No real h,k,H,s with 0<h,k,H<1/√3, s>0, s²=1-3h², H=k+g(h)=s+g(k), g(H)=g(h)+g(k), where g(w)=2w-4w³ |
| Consequence | The full original VO-O1 system in the preceding checkpoint §6 has no solution, since every solution implies this necessary subsystem |
| Proof source | Complete three-step argument supplied inline in the current user message, titled “T01 - Verify and freeze VO-O1 before further research” |
| Formal proof locator | [Freeze note](README.md), §§1-3; sign audit §4; version 1, 2026-10-11 |
| Independent audit | [Referee audit](referee-audit.md), §§2-4; version 1, 2026-10-11; ACCEPTED |
| Dependencies | Original signed center/width equations and original positive-width frame domain; displayed elementary polynomial identities and real inequalities |
| Audit performed | Both reviewers checked the reduction, the nonzero cancelled factor, both square-comparison signs, every strict inequality and the boundary exclusions |
| Unused restrictions | Unequal gaps, slot nondegeneracy, membership of the new columns, exclusion from the old row set and deduplicated new-pair count |
| Retained scope limit | T01 remains OPEN; this proof makes no claim about other endpoint roles or frame models, and asserts no boundary classification. Earlier scoped exclusions remain unchanged. |
| Historical supersession | Only the prior VO-O1 OPEN obligation is resolved. Its original wording and all previous proof/data bytes remain preserved. |

The existence of a complete proof, not the agreement of reviewers by
itself, supports the PROVED label. There is no conditional external theorem
or unavailable arithmetic result in this elementary argument.

## Sources read and availability

| Source | What was used; what was not claimed |
| --- | --- |
| [Varying-output checkpoint](../2026-10-11-varying-output-frames/README.md), §6 and §§3-4; v1, 2026-10-11 | Original VO-O1 signs, domains, centers and extra endpoint/pair restrictions checked against the new reduction. Earlier continuation counts/image bound imported separately. |
| [Compatibility appendix](../2026-10-11-varying-output-frames/compatibility.md), VO-C1 and VO-C3-C4; v1, 2026-10-11 | Frame conventions and exact old claim locators inspected. No new audit of the old continuation or irrational-spacing theorem is claimed. |
| [Prior finite audit](../2026-10-11-varying-output-frames/audit.md), §1, and [prior ledger](../2026-10-11-varying-output-frames/verification.md) | Read for evidence and status scope. The old numerical results and evaluator are preserved; neither is rerun. |
| [TC geometry](../2026-10-11-torsion-compatible-sharing/geometry.md), TC-G2; v2, 2026-10-11 | Referee inspected the accepted frame identity. No renewed fixed-output, torsion or genus-four investigation. |
| Current user message | Its complete inline proof is the argument verified here. No independent file identity is invented for a conversational source. |
| Separate attached VO-O1 proof note | No attachment path was supplied with this message; no matching standalone text/Markdown note was located in the supplied attachments or workspace. This availability gap is identified, and no such file is claimed read or reconstructed. The inline argument suffices for the requested verification. |

[Source identities](source-identities.json) give exact hashes and sizes for
the five existing research files above. Source identity is distinct from
proof verification. Repository setup, migration/state, SPEC, STATUS,
mechanism/failure and open-lemma records were consulted for orientation
and preservation; obsolete prompts were not treated as assignments.

**Imported, not re-proved here:** VO-C3-C4 give N=4m, Q=6m-2, Z=m+1
and |P(A_m,A_m)|≥N²/16 for the prior family, m≥2. They are neither
assumptions nor consequences of VO-C6. MS-C1, the fixed-output width bound
and genus-four completion remain frozen in their prior scopes. T01 OPEN.

## Production and preservation

The Markdown note and three-page PDF share one document-content source.
ReportLab, the existing DejaVu fonts and bundled Poppler were used offline.
No package installation, internet, mathematical enumeration, target-P
evaluation or research-program execution occurred. The rendering helper
and raw page images are under
`local-only/runs/T01/2026-10-11-vo-o1-freeze/`; it is document-production
code and does not evaluate the mathematical claim.

Automatic layout checks rejected drafts with an overfull third page.
Table spacing and source-ledger wording were shortened, without changing
the proof. The final PDF has
three A4 pages. The lead rendered and visually inspected every final page:
all equations, signs, superscripts, Greek letters, table cells, headings
and footers are readable, with no clipped text or missing glyphs. The final
content stays at least 67.8 points above the page bottom.

The initial preservation baseline covers 388 existing files, including
inherited modified/untracked work. This task appends dated updates only to
the current map, mechanism library, failure library, open-lemma index and
T01 STATUS. It edits no historical proof. All five identified source files
and all seven files in the preceding varying-output checkpoint are
hash-preserved; the prior T01 STATUS is an exact prefix of its updated file.

The workspace changed concurrently during this task: six existing files in
the separate balanced-full-fibers note, T03 STATUS, and earlier content of
the four shared indexes differ from the initial baseline. These changes
were not made by this task and are retained. Accordingly this freeze does
not claim a globally unchanged baseline or unchanged prefixes for those
four shared indexes. Its dated additions are identified separately from
the concurrent differences. Source identities, preservation output, PDF
text/layout checks and artifact hashes accompany the production record.

Completion commands and their results are recorded below after validation.
These checks establish source/document integrity, not the theorem. No
stage, commit, push, remote change or next research cycle is performed.

- `python3 scripts/check_repository.py`: passed; 39 archived source files
  and links in 225 Markdown files verified at completion.
- `python3 scripts/check_codex_setup.py`: passed; 50 local reference files,
  43 T03 manifest members, original identities, duplicate states and C4
  hashes verified. This checker executes no research code.
- `git diff --check`: passed. The new note files were checked separately
  for whitespace, since they are untracked.
- PDF validation: three pages, nonempty extracted text, no replacement
  characters, page bounds passed; every final rendered page inspected.
- Preservation: all five identified research sources and all seven prior
  varying-output artifacts match their recorded hashes. The new T01 STATUS
  retains its former content as an exact prefix. Concurrent unrelated
  changes are itemized separately in the local preservation record.

No research code was changed and no mathematical experiment or old finite
regression was rerun. The only executed helper builds and checks documents.
