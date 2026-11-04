# TJ-O1 source, audit and freeze ledger

21 October 2026 · version 1 · T01 · offline verification only.

## Claim record

- **ID/status:** TJ-C6, PROVED; TJ-O1, PROVED IMPOSSIBLE in its stated scope.
- **Polynomial/branch:** \(P(x,y)=(x-y)^3+x+y\), retained T01 cubic.
- **Quantifiers:** no positive real tuple satisfies equations (1)–(2) and
  the domains in [the proof note](README.md), for any \(a,b>0\).
- **Hypotheses:** symmetric gaps \((a,b,a)\), retained reflected frame
  branches, negative-sign opposite-edge roles, positive conics, and
  \(H=r,\ S=e+q\). Extra distinct-slot and pair-count requirements are unused.
- **Proof:** README, “Complete contradiction,” steps 1–5; source identities
  and versions are recorded in [source-identities.json](source-identities.json).
- **Dependency:** the common-bound derivation of TJ-C1, rechecked here for
  applicability to the changed closing columns. TJ-C2–C4 are preserved
  contextual exclusions, not substitutes for the new proof.
- **Evidence:** complete exact argument supplied by the user and checked
  manually by the lead and two independent checking agents. No finite
  experiment, external theorem, or novelty claim.
- **Remaining gaps:** none for TJ-O1 in this scope. Other roles and the
  unrestricted fixed-polynomial target remain OPEN.

## Sources read and available

| Source | Use |
|---|---|
| [Accepted checkpoint](../2026-10-20-tetrahedral-junction/README.md), especially §4 | Exact historical TJ-O1 statement, left unchanged |
| [Catalogue](../2026-10-20-tetrahedral-junction/catalogue.md) | Sign conventions, centers, branches and original roles |
| [Compatibility proof](../2026-10-20-tetrahedral-junction/compatibility.md), TJ-C1–C4 | Read; common bounds and their unchanged hypotheses checked explicitly |
| Current user message, “T01 — Verify and freeze TJ-O1” | Complete five-step proposed contradiction, independently verified |
| Setup/map/audit, master handoff, T01 state export, SPEC/STATUS, migration conflicts and relevant registries | Target identity, source hierarchy and preservation rules |

All mathematical sources needed for this verification are available.
The supplied proof is inline in the current request; no separate attachment
is required or claimed read. Older arithmetic, torsion and finite-count
programs were not reopened or rerun.

## Independent checks

The algebraic referee (`/root/symbolic_obstruction`) and separate proof checker
(`/root/finite_gadgets`) each received the same verification assignment and
returned an independent first verdict before their conclusions were combined.
Their records are [algebraic-referee.md](algebraic-referee.md) and
[proof-check.md](proof-check.md).

Both accepted every step without mathematical correction. The algebraic
referee checked the exact factorization of \(C(x)-2\); the proof checker
independently justified the branch inference using the shape of \(C\).
The lead checked the full reduction and the two strict inequalities.
The algebraic referee subsequently read and accepted the saved main proof
note in full for transcription and scope.

This is internal independent verification, not external review. Agreement
is accompanied by the complete written proof and does not replace it.

## Scope and computation boundary

The budget for construction searches, role sweeps and numerical experiments
was **zero**. None was run. Polynomial identities and signs were checked
exactly by hand. Repository validation and file hashing are document checks,
not research enumeration. No packages, network access, or code changes were
needed. No new obligation or research cycle was adopted.

There is no surviving seed, so there are no actual \(N,Q,Z,B\) or image
counts to report. This conclusion is not an image lower bound or an
asymptotic obstruction for the general T01 target.

## Preservation and validation

The initial checkout was `main` with nine inherited modified tracked files
and existing untracked research artifacts. Before editing, a 418-file
baseline with byte lengths and SHA-256 hashes was saved in
`local-only/runs/T01/2026-10-21-tj-o1-freeze/`, together with the initial
tracked diff. That directory is ignored and contains only local audit data.

The original tetrahedral report, catalogue, proofs, audit records and
source manifest are preserved. The old TJ-O1 OPEN statements remain
verbatim. This task adds its freeze note and two independent checking
records, plus dated appendices to T01 STATUS, the current project map,
and the mechanism, failure and open-lemma registries.

Final validation:

| Check | Result |
|---|---|
| `python3 scripts/check_repository.py` | PASS: 39 archived sources and local links in 252 Markdown files |
| `python3 scripts/check_codex_setup.py` | PASS: 50 references, original import identities, 43 T03 manifest members, duplicate states and C4 hashes; no research code executed |
| `git diff --check` and new-note whitespace scan | PASS |
| Source/proof SHA-256 check | PASS: all six source and proof identities |
| Preservation of baseline contents | PASS: 411 files unchanged; seven modified files retain their exact original byte prefixes; no original-content violation |
| Independent proof checks | Both ACCEPTED; algebraic referee also accepted the saved main note |

Concurrent T03 work added `research/notes/2026-10-21-relative-unit-population/`
and dated appendices to project history, T03 STATUS and three shared
registries. The first preservation check flagged the two additional changed
files outside this task's five-file append list. Inspection confirmed that
these too preserved their entire original byte prefixes. The initial audit
and the resolved preservation report are both retained in the local run
directory. Those concurrent additions were neither authored nor mathematically
reviewed here, and were left intact.

No executable code changed, so no unit-test or experiment suite was run.
The document checks above do not certify the general T01 target.
Nothing was staged, committed, pushed, reset or cleaned. This verification
and freeze is complete; no next construction cycle is initiated.
