# Source and status ledger: torsion/frame freeze

T01 · 11 October 2026 · TF-D1 · version 1 · documentation only.

The fixed polynomial is P(x,y)=(x-y)^3+x+y. This document introduces no new mathematical claim. All required companions for this freeze are available. Historical migration gaps identified in MC-06 are not dependencies here and have not been reconstructed.

## Frozen status and proof scope

| Claim | Status | Quantifier/hypotheses and identified evidence | This task |
| --- | --- | --- | --- |
| TC-G1 | PROVED in the supplied system | Every real fixed c=z-w≠0: three-slot sharing model on E_c; TC geometry, TC-G1 | Editorial fidelity check |
| TC-G2 | PROVED in the supplied system | Fixed ordered real z>w; nondegenerate two-row conic frames: at most two widths/four marked points; TC geometry, TC-G2 | Reproduced scope and proof |
| TC-G4 | PROVED in the supplied system | Every real c≠0; general one-row completion cover genus 4; every characteristic-zero degree-e elliptic isogeny pullback genus 1+3e; TC geometry, TC-G4 | Kept separate from TC-G2 |
| TC-G5 | PROVED in the supplied system | Exact positive-root, same-center different-width attachment: N=6,Q=8,Z=2,B=28; TC geometry, TC-G5 | Exact constants/signs retained |
| TC-X1 | EXPERIMENTAL, exact and exhaustive in finite scope | The specified six-scalar square has full image 30, two size-4 fibers and 28 singleton fibers; TC exact audit §4 and retained JSON | Imported, no rerun; not promoted to an asymptotic theorem |
| MS-C1 | PROVED in the supplied system | For the one exact positive-Y marked difference T=R2-R1, [n]T≠O for every positive integer n; MS arithmetic §§1-5 | Frozen with original complete proof and saved internal audit |
| TC-O1 | RESOLVED by MS-C1 | Former OPEN text in TC README/geometry/provenance is historical for this one point | Supersession explicit; historical files unchanged |
| T01 | OPEN | Arbitrarily large finite real same-set squares with fixed positive exponent saving for P | No construction, new obligation or proof search |

Dependencies for MS-C1 are the exact TC-G5 constants, elliptic group law, the displayed square-class and local embedding arguments, and the supplied EG-C2 formal-logarithm lemma. The prior independent referee audit is internal evidence, not external review. No novelty claim or literature search is made.

## Exact source identities

Links are relative to this ledger. Hashes identify the versions actually used and retained. “Read” means source inspection for faithful documentation, not fresh independent mathematical verification.

### TC README

[research/notes/2026-10-11-torsion-compatible-sharing/README.md](../2026-10-11-torsion-compatible-sharing/README.md)

v1; 2026-10-11. Read for exposition and chronology; old TC-O1 OPEN is superseded.

SHA-256: `8e46e775a258cdf079598a5a9e1877ee18b32267e1ff204845f0ad73b3d46e34`.

### TC geometry

[research/notes/2026-10-11-torsion-compatible-sharing/geometry.md](../2026-10-11-torsion-compatible-sharing/geometry.md)

v2; 2026-10-11. TC-G1, TC-G2, TC-G4, TC-G5 proof text inspected for source fidelity; no new proof audit.

SHA-256: `713c2372740eb9b3f54dcb4242192b170436b98002f2ceacdfcc075903cb2d58`.

### TC exact audit

[research/notes/2026-10-11-torsion-compatible-sharing/exact-audit.md](../2026-10-11-torsion-compatible-sharing/exact-audit.md)

v1; 2026-10-11. TC-X1 finite full-square counts imported as EXPERIMENTAL, exact and exhaustive in its finite scope.

SHA-256: `93b98a91c922eead2bac3022758e92fd304c021d899f3c305dd85059058be842`.

### TC provenance

[research/notes/2026-10-11-torsion-compatible-sharing/verification.md](../2026-10-11-torsion-compatible-sharing/verification.md)

v1; 2026-10-11. Historical audit scopes and provenance read; historical tests not rerun.

SHA-256: `6728ae03399afe54511e438d50e2e736ff172a8cea7b6b3932370c6052d4466e`.

### TC retained data

[research/notes/2026-10-11-torsion-compatible-sharing/exact-results.json](../2026-10-11-torsion-compatible-sharing/exact-results.json)

retained exact output; 2026-10-11. Available and hash-preserved; not re-evaluated or independently recounted in this freeze.

SHA-256: `17069d583d612d7f949b191e39164124a872c46ceb5f42ef6593d4aa3fbc3cc4`.

### TC evaluator

[research/notes/2026-10-11-torsion-compatible-sharing/exact_audit.py](../2026-10-11-torsion-compatible-sharing/exact_audit.py)

retained source; 2026-10-11. Availability/hash check only; not executed or freshly code-audited.

SHA-256: `cc8347ebe0b74ae867c4ef35c676328b4ab233b38255bd525b26ddc326e3f819`.

### MS README

[research/notes/2026-10-11-marked-shift-certificate/README.md](../2026-10-11-marked-shift-certificate/README.md)

v1; 2026-10-11. Controls current MS-C1 PROVED and TC-O1 resolved status.

SHA-256: `c7d6ab1d04aad9910cf0c9dfa364335ae3acfc9d5912e2013ab70f616fb181ed`.

### MS arithmetic

[research/notes/2026-10-11-marked-shift-certificate/arithmetic.md](../2026-10-11-marked-shift-certificate/arithmetic.md)

v1; 2026-10-11. Complete exact proof reproduced editorially; field, signs and hypotheses retained.

SHA-256: `dfe7a75294130008d7ad4da909f693454dabd4adb13bcf70aa0fd26af0e4697d`.

### MS referee

[research/notes/2026-10-11-marked-shift-certificate/referee-audit.md](../2026-10-11-marked-shift-certificate/referee-audit.md)

v1; 2026-10-11. Records prior independent internal audit; not external review or a new audit in this freeze.

SHA-256: `70dcfaf7744c3863b99e6f5759cd4fe5424efb5b454fb5d4816a0874f2c461cb`.

### MS provenance

[research/notes/2026-10-11-marked-shift-certificate/verification.md](../2026-10-11-marked-shift-certificate/verification.md)

v1; 2026-10-11. Prior proof and preservation evidence read.

SHA-256: `55eda9c89fd875000fc9d29812b442eb3cfd98e2c9a2127ecbd9e8e3e77e479c`.

### EG local lemma

[research/notes/2026-09-30-elliptic-geometry/complex-extensions.md](../2026-09-30-elliptic-geometry/complex-extensions.md)

EG-C2; 2026-09-30. Necessary earlier local criterion; proof also reproduced in MS arithmetic §5.

SHA-256: `ecf894b30c3a0da77e4bccca37734a78ad0434682c9c72f7cb59f27d5da4c03d`.

## Notation and provenance safeguards

- The same-second-coordinate model is Y²=X³−48X−128−432c²; the inverse uses X+4.
- All finite-attachment radicals a=√2, H=√((3+a)/14), W=√(4a−3) are positive in the original real embedding. L=Q(a,H,W) has degree eight. The Q23 embedding is of F=Q(a,H), not an asserted embedding of W into Q23.
- The cover coordinate is displayed as W_cov only to distinguish it from that fixed W. This is the variable called W in TC-G4; its equation remains W_cov²=4−3u².
- The source’s field K in the arithmetic appendix is denoted L consistently in this package; it is the same exact joint coordinate field. The letter r replaces the first scalar slot A in cover formulas to avoid confusion with the whole finite set A. The symbols and signs of R1,R2,T are unchanged.
- The exact full-image audit remains finite evidence. Neither its two large fibers nor the infinite-order point provides a growing compatible frame family.
- Two assistants reviewed draft source fidelity and mathematical exposition only. This freeze performs no new proof audit, torsion computation, finite-square evaluation, construction search or package installation.
