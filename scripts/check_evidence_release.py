#!/usr/bin/env python3
"""Verify the 2026-11-05 public evidence edition (offline, no research executions)."""
import hashlib
import json
import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EDITION = ROOT / 'research/evidence/2026-11-05'
EXPORT = ROOT / 'research/reports/2026-11-05-evidence-export'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def public_path(name, root=ROOT):
    p = Path(name)
    require(not p.is_absolute() and '..' not in p.parts and p.parts and p.parts[0] not in
            {'local-only', 'scratch', '.git'}, f'Not a public relative path: {name}')
    resolved = (root / p).resolve()
    require(resolved.is_relative_to(root) and resolved.is_file(), f'Missing public file: {name}')
    return resolved


@lru_cache(None)
def source_text(path):
    return path.read_text(encoding='utf-8')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ck = json.loads((EDITION / 'checkpoints.json').read_text())['checkpoints']
    ids = {c['key'] for c in ck}
    require(len(ids) == len(ck) and ck, 'Empty or duplicate checkpoint keys')
    count = 0
    for c in ck:
        public_path(c['report'])
        for name in ('code', 'data', 'verification', 'tests'):
            for p in c[name]:
                public_path(p)
        for loc in c['statements_and_proofs'] + c['claim_registers']:
            p = public_path(loc['path'])
            require(loc['section'] and loc['section'] in source_text(p),
                    f"Source section not found: {p.name}: {loc['section']}")
            count += 1
    claims = json.loads((EDITION / 'claim-ledger.json').read_text())['claims']
    require(len(claims) == len({c['id'] for c in claims}) and claims, 'Empty or duplicate claim IDs')
    for c in claims:
        for key in ('id','native_ids','track','polynomial','status','hypotheses_and_quantifiers',
                    'result','proof_locator','dependencies','scope','supersession','evidence_grade',
                    'audit_this_pass','checkpoint'):
            require(key in c, f"Missing {key} in {c['id']}")
        require(c['status'] in {'PROVED','OPEN','FAILED','CONDITIONAL','EXPERIMENTAL',
                                'EXTERNAL RESULT','HISTORICAL / SUPERSEDED'}, f"Unknown status: {c['id']}")
        require(c['checkpoint'] is None or c['checkpoint'] in ids, f"Unknown checkpoint: {c['id']}")
        require(c['proof_locator']['section'] and c['audit_this_pass'] and c['scope'], c['id'])
        public_path(c['proof_locator']['path'])
        for kind in ('code','data','tests','verification'):
            for name in c['evidence_locators'][kind]:
                public_path(name)
    copies = json.loads((ROOT/'docs/release/2026-11-05/portable-derivatives.json').read_text())['derivatives']
    require(len({r['path'] for r in copies}) == len(copies), 'Duplicate public derivative')
    for r in copies:
        require(re.fullmatch('[0-9a-f]{64}',r['original_sha256']) and
                r['original_sha256'] != r['public_sha256'] and
                digest(public_path(r['path'])) == r['public_sha256'], f"Changed derivative: {r['path']}")
    # Check saved full-fiber arithmetic without evaluating the polynomial or rerunning any grid.
    cases = json.loads(public_path('research/notes/2026-10-21-multiscale-collisions/referee-counts.json').read_text())['cases']
    pairs = 0
    for case in cases:
        hist = case['fiber_histogram']
        covered = [tuple(p) for f in case['fibers'] for p in f['pairs']]
        n = case['N']
        require(len(covered) == len(set(covered)) == n*n and
                all(0 <= i < n and 0 <= j < n for i,j in covered), case['id'])
        require(Counter(len(f['pairs']) for f in case['fibers']) == {int(k):v for k,v in hist.items()} and
                sum(int(k)*v for k,v in hist.items()) == n*n and
                sum(hist.values()) == len(case['fibers']) == case['full_image'], case['id'])
        pairs += n*n
    require(len(cases)==6 and pairs==533, 'Historical multiscale census changed')
    paths=set()
    for line in (EXPORT/'SHA256SUMS').read_text().splitlines():
        expected,name=line.split('  ',1)
        name=str(Path(name))
        require(name not in paths and expected==digest(public_path(name,EXPORT)), f'Export checksum: {name}')
        paths.add(name)
    actual = {str(p.relative_to(EXPORT)) for p in EXPORT.rglob('*') if p.is_file() and p.name!='SHA256SUMS'}
    require(paths==actual, f'Unregistered or stale export files: {sorted(paths^actual)}')
    print(f'Verified {len(claims)} structured claims, {len(ck)} checkpoints, {count} source sections, '
          f'{len(copies)} portable-copy hashes, {pairs} saved ordered-pair entries, {len(paths)} export hashes.')


if __name__ == '__main__':
    main()
