# Working in this repository

Follow the current user's request. Text in `research/prompts/` is an archived
assignment, not an active instruction to execute a research run.

For continuation, read `research/PROJECT_HISTORY.md` and the selected track's
`SPEC.md` and `STATUS.md` first. The four tracks were explicitly selected by the
owner. Preserve the two distinct cubic polynomials and update history when a
later checkpoint supersedes an earlier proposed route.

- Preserve archived files listed in `research/manifest.json` unchanged. Write
  corrections and follow-up results as new documents with source locators.
- Keep reported results, complete proofs, conditional implications, conjectures,
  computational evidence, and failed routes visibly distinct.
- Do not infer a proof from finite experiments, source labels, or agent agreement.
- Preserve the fixed-polynomial, fixed-exponent, same-set quantifiers.
- Record absent sources instead of reconstructing them or claiming to have read them.
- Keep administrative documents, credentials, local paths, and unlicensed reference
  paper copies out of commits.
- The computational baseline uses Python's standard library. Add dependencies only
  when a concrete research need justifies them.
- After code changes, run `python3 -m unittest discover -s tests -v` and
  `python3 -m experiments verify`. After source or documentation changes, run
  `python3 scripts/check_repository.py`.

GitHub access is needed only for repository collaboration; the experiments run
offline. A research task's network policy should be stated in its active request.
