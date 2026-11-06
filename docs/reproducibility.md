# Reproducing the finite experiments

Use Python 3.10 or later from the repository root. No third-party packages are
required. Successful experiment subcommands produce JSON, and all counting is
exact. Help, unit tests, and repository checks produce human-readable text.

```bash
python3 -m experiments --help
python3 -m experiments verify
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

## Polynomial identifiers

| Identifier | Fixed polynomial |
| --- | --- |
| `baseline` | $(x-y)^2+x+y$ |
| `quadratic` | $(x+2y)^2+3x-y$ |
| `quartic` | $(x+2y)^4+3x-y$ |
| `mixed-cubic` | $xy(x+y)$ |
| `eisenstein` | $x^2+xy+y^2$ |

## Local images

```bash
python3 -m experiments local-images --polynomial all --primes 2 3 5 7 --q 1
python3 -m experiments local-images --polynomial all --primes 5 7 --q 35
```

For a fixed prime $p$, the program evaluates all $p^2$ ordered pairs in
$\mathbb F_p^2$ and records the distinct outputs. Composite moduli are rejected:
these commands describe prime fields, not prime-power extensions or residue rings.

For a degree-$m$ polynomial, `--q Q` selects the integral deformation

$$F_Q(x,y)=Q^mP(x/Q,y/Q).$$

For the baseline and quadratic, this multiplies the linear part by $Q$; for the
quartic, by $Q^3$. For the two homogeneous polynomials it leaves the polynomial
unchanged. `--q 1` therefore evaluates the original polynomial.

At an odd prime dividing $Q$, the baseline and quadratic deformations have
$(p+1)/2$ outputs. The quartic deformation has
$1+(p-1)/\gcd(4,p-1)$ outputs. These identities motivate checks in the verification
suite; the suite itself certifies only its explicitly listed finite inputs.

The output reports the exact density $|\mathrm{image}|/p$ as a
numerator/denominator object. The
finite-field image of an original polynomial can be full even when its deformation
has a smaller image. A deformation alone does not establish the required
split-prime field supply or an asymptotic real-set bound.

## Same-set carriers and collision energy

```bash
python3 -m experiments carriers --polynomial mixed-cubic --carrier geometric --size 8 --base 3
python3 -m experiments carriers --polynomial eisenstein --carrier arithmetic --size 20
```

The command constructs a finite integer set $A$ and evaluates **every** ordered
pair in $A\times A$. Use `carriers --help` to inspect the available carrier
parameters and their defaults. The output includes the carrier, image count,
normalized support ratio $|F_Q(A,A)|/|A|^2$, and collision energy

$$
E_P(A)=\sum_{z\in P(A,A)}r(z)^2,
\qquad
r(z)=|\{(a,b)\in A^2:P(a,b)=z\}|.
$$

For nonempty $A$, Cauchy–Schwarz gives

$$|P(A,A)|\ge\frac{|A|^4}{E_P(A)}.$$

With `--size 0`, support and energy are zero and both ratios are `null` because
they are undefined. The reported fraction for nonempty inputs is a **lower
bound**, not an upper-bound certificate.
Small favorable finite cases, or a failure to find them, do not settle the
existential asymptotic question.

For $P(x,y)=xy(x+y)$ and $A=\{3^0,\ldots,3^7\}$, the expected image size is
$8\cdot9/2=36$ and the expected energy is $2\cdot8^2-8=120$. This is a useful
adversarial regression example, since symmetry creates collisions but the image
still has quadratic order in $|A|$.

## Saved examples and checks

[examples/README.md](../examples/README.md) records the commands for the committed
JSON snapshots. They can be regenerated without a network connection. The test
suite includes independently stated finite expectations, input validation, exact
deformation identities, and command-line behavior.

The GitHub workflow runs these checks on Python 3.10, 3.12, and 3.13. A successful
workflow certifies the implementation and archive checks at that commit; it does
not certify the research conjectures.

The repository does not currently implement growing number-field towers,
unit/regulator enumeration, a general symbolic proof assistant, or exhaustive
search over correlated residue subsets. Those require separately specified
research tasks and source inputs.


## 2026-11-05 evidence release

A public checkout can run all three standard checks above with the Python standard library. In addition, run `python3 scripts/check_evidence_release.py` from the repository root to validate the dated claim and checkpoint locators, publication-copy hashes, and typeset export inventory. See the [release record](release/2026-11-05/README.md) for the measured results. The release check is archival verification, not a test of an asymptotic claim.

The [ledger](../research/EVIDENCE_INDEX.md) identifies portable JSON evidence and full proof text separately from finite research scripts. Historical run commands describe their original budgets and inputs; they need not be run to read or verify this export. The original source check `python3 scripts/check_codex_setup.py` is **local-bundle only**: a public clone deliberately lacks its 50 restricted reference inputs. Do not infer a missing proof from a passing public check or recreate withheld files from filenames.

The [LaTeX export](../research/reports/2026-11-05-evidence-export/README.md) has its own build instructions and bibliography. The committed PDFs are provided for reading without a TeX installation. Auxiliary TeX and page-inspection files are not publication artifacts.

## Checking frozen releases from a current checkout

Use a full Git clone. From its root run:

~~~sh
python3 scripts/check_evidence_release.py
python3 scripts/check_c0_snapshot.py
python3 scripts/check_quadratic_v6_references.py
python3 scripts/check_quadratic_v6_references.py --bibliography research/exports/2026-11-05-report-audit/integration/bibliography-v6-editor.tex
~~~

The first check validates the four-track ledger, proof locators, finite outputs and report files. The second runs the original 5 November C0/T03 verifier in a temporary tree. The frozen manifest includes five subsequently updated navigation documents: the root README, current project map, project history, open-lemma registry and T03 status. Their historical bytes come from release `c689ab52ca3bb9e3221bd09ae9a083a3111e39df`. All five paths must still exist, and the verifier checks the other 262 listed files against the distributed bytes. The manifest and original verifier must themselves match the published Git objects. To run the legacy verifier directly on its original tree, use a separate checkout of that revision. The last two commands resolve the historical citations and source objects for each bibliography. See the [academic PDF route inventory](release/2026-11-07/report-citations.md) for the separate public link checks.

**Typesetting.** In a disposable copy of the four-track export directory run `sh build.sh` with pdfLaTeX and BibTeX installed. The [source and toolchain notes](../research/reports/2026-11-05-evidence-export/README.md) describe the two outputs. For the quadratic report and brief, follow the [C0/T03 build recipe](../research/exports/2026-11-05-evidence/README.md) in a disposable copy of the repository. Compare frozen hashes before rebuilding. These procedures compile documents. The finite verifier above checks stated examples; the proof packages address unbounded input sizes.
