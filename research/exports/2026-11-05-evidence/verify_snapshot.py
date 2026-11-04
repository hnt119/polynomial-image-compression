#!/usr/bin/env python3
"""Check the distributed release from any working directory. No network or research code."""
import csv
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parents[2]


def read_json(name):
    return json.loads((here / name).read_bytes())


def main():
    paths = {}
    for line in (here / 'checksums.sha256').read_text().splitlines():
        digest, rel = line.split('  ', 1)
        path = (root / rel).resolve()
        if rel in paths or not path.is_relative_to(root) or not re.fullmatch(r'[a-f0-9]{64}', digest):
            raise ValueError('invalid digest entry: ' + rel)
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('digest mismatch: ' + rel)
        paths[rel] = digest

    claims = read_json('evidence_register.json')['claims']
    with (here / 'evidence_register.csv').open(newline='') as f:
        csv_rows = list(csv.DictReader(f))
    ids = {r['claim_id'] for r in claims}
    if len(claims) != len(ids) or len(claims) != len(csv_rows):
        raise ValueError('duplicate or absent claim')
    source_paths = set()
    for j, c in zip(claims, csv_rows):
        if set(j) != set(c): raise ValueError('CSV schema differs')
        for key, val in j.items():
            if (json.loads(c[key]) if isinstance(val, list) else c[key]) != val:
                raise ValueError('CSV differs: '+j['claim_id']+' '+key)
        if set(j['dependencies']) - ids: raise ValueError('unresolved dependency')
        for s in [j['source_file'], j['historical_audit'], *j['supporting_code_data']]:
            if s and '/' in s:
                source_paths.add(s)
                if s not in paths or not (root / s).is_file(): raise ValueError('missing public evidence: '+s)

    state = read_json('state.json')
    for group in [*state['objectives'], *state['current_milestones']]:
        if set(group.get('claims', [])) - ids: raise ValueError('state references unknown claim')
        if group.get('source') and not (root / group['source']).is_file(): raise ValueError(group['source'])
    for item in state['corrections_and_availability']:
        for s in item['sources']:
            if not (root / s).is_file(): raise ValueError(s)

    with zipfile.ZipFile(here / 'professor_brief.docx') as z:
        if z.testzip(): raise ValueError('corrupted Word document')
        doc = ET.fromstring(z.read('word/document.xml'))
        nm = len(doc.findall('.//{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath'))
        if not nm: raise ValueError('no native Word equations')
    print(f'{len(paths)} SHA-256 matches; {len(ids)} equivalent CSV/JSON claims; '
          f'{len(source_paths)} distinct claim-source paths; {nm} editable Word equations.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
        sys.exit(str(exc))
