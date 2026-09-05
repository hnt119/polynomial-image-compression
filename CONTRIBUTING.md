# Contributing

This repository keeps mathematical reasoning and reproducible evidence together.
A useful contribution can be a proof, a correction, a precisely scoped failed
method, a new conjecture, or an exact experiment.

## Mathematical contributions

State the polynomial, domains, quantifiers, parameter dependencies, and intended
conclusion before presenting an argument. Use one explicit status:

- **Proved here:** a complete argument is present, with its dependencies identified.
- **Reported by a source:** give a file and section; say whether its proof was checked.
- **Conditional:** list the additional hypotheses required by the implication.
- **Conjecture / open:** identify the missing mathematical step.
- **Computational evidence:** give the finite range and a reproducible command.
- **Route failed:** state which estimate or construction fails, without asserting
  that the conjecture is false.

For compression claims, account for the full image support. Keep the polynomial
and exponent fixed as the set size grows, preserve the same set in both inputs,
and charge parameterization multiplicities and all counting losses.

## Source corrections

Files listed in [the manifest](research/manifest.json) are immutable snapshots.
Add a dated correction in `research/notes/` with the original filename and section,
the issue, and the replacement argument. Update the source guide and roadmap when
the correction changes their conclusions. Do not alter a snapshot merely to make
an integrity check pass.

## Computational contributions

Use exact integers or rational numbers where possible. Include the input carrier,
modulus, full enumeration range, and output format. Distinguish sampled searches
from exhaustive enumeration. An experiment should address a stated question.

Run:

```bash
python3 -m unittest discover -s tests -v
python3 -m experiments verify
python3 scripts/check_repository.py
```

Commit useful scripts and small reproducible outputs. Keep large searches,
downloaded reference papers, private working files, and generated LaTeX auxiliary
files outside version control. Issue templates are provided for research tasks
and corrections.
