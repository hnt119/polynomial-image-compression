# Local Codex setup

**Publication update · 5 November 2026.** This is the historical local migration record. The [existing GitHub repository and release process](publishing.md) supersede its no-remote description for new checkouts. The private migration bundle is still not distributed. The [evidence index](../research/EVIDENCE_INDEX.md) covers the later native results.

Prepared 2026-09-14; mathematical research cutoff remains 2026-09-10.
Open **this repository directory** (`polynomial-image-compression`) as a local
project in Codex. The parent folder is a ChatGPT mirror, not the Git root.
This is a complete local copy with existing Git history and uncommitted migration
work. No commit, push, fetch, or new proof search was performed. The selected
source checkout had no remote; none has been added here.

Codex loads the root [AGENTS.md](../AGENTS.md) as project instructions. Start a
new task from this root after instruction changes, following
[official instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
No model override, API key, plugin, startup research command, or global setting
is needed. These files do not automatically add a sidebar project entry;
opening/adding this folder in Codex is the UI step.

## First session

1. Inspect Git status and diff before editing; inherited changes are intentional.
2. Read [the map](../research/CURRENT_PROJECT_MAP.md),
   [setup audit](../research/CODEX_MIGRATION_AUDIT.md), and
   [preserved migration issues](../research/MIGRATION_CONFLICTS.md).
3. Read the master, chosen state export, and checkpoints at the map's paths.
4. State whether the task is documentation, proof audit, authorized research,
   or reproduction of specified finite evidence. Preserve that boundary.
5. Run checks appropriate to the changes and report their scope.

From the repository root, using Python 3.10 or later:

```bash
git status --short --branch
git diff --stat
python3 scripts/check_repository.py
python3 scripts/check_codex_setup.py
```

For code changes, also run the existing finite regressions:

```bash
python3 -m unittest discover -s tests -v
python3 -m experiments verify
git diff --check
```

No package installation is needed. These checks do not run imported T02–T04
research programs or certify their mathematics.

## References and local transfer

`local-only/migration/` contains 50 hash-registered source files: the original
42 setup references plus eight recovery documents received on 20 September.
The recovery intake also has a local README explaining that only the addenda
and Markdown manifests were received, not the larger source packages those
documents describe. Original source paths and historical links remain
unchanged. The portable relative-path inventory is
[CODEX_SOURCE_MANIFEST.json](../research/CODEX_SOURCE_MANIFEST.json). The old
39-file archive and manifest remain separate and unchanged.

The local-only folder is ignored by Git; it includes restricted-distribution
reference PDFs and a manifest with private source paths. A plain Git clone
does **not** include these files. For an authorized local transfer, copy
`local-only/migration/` alongside the checkout and run the setup checker.
Do not auto-download missing sources, silently substitute versions, or commit
the private bundle. Missing sources must be reported before dependent work.

The repository checker validates the distributed archive and current links,
excluding ignored private/scratch/environment directories. The local setup
checker separately validates reference hashes, original import identities,
and T03 ZIP members. These are packaging checks, not proof audits.

`local-only/setup-audit/` holds source-checkout identity, baseline hashes, and
patches separating inherited migration changes from this setup. It is local
setup evidence. Future mathematical changes belong in dated claim records.
