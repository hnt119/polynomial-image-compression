#!/usr/bin/env python3
"""Run the frozen C0/T03 verifier while allowing five live navigation pages to evolve."""
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
RELEASE = 'c689ab52ca3bb9e3221bd09ae9a083a3111e39df'
PACKAGE = Path('research/exports/2026-11-05-evidence')
MANIFEST = PACKAGE / 'checksums.sha256'
VERIFIER = PACKAGE / 'verify_snapshot.py'
LIVE_PAGES = frozenset(map(Path, (
    'README.md',
    'research/CURRENT_PROJECT_MAP.md',
    'research/OPEN_LEMMAS.md',
    'research/PROJECT_HISTORY.md',
    'research/tracks/03-eisenstein-cartesianization/STATUS.md',
)))


def historical_blob(root, path):
    result = subprocess.run(['git', 'cat-file', 'blob', f'{RELEASE}:{path.as_posix()}'],
                            cwd=root, capture_output=True)
    if result.returncode:
        raise ValueError(f'Missing {RELEASE}:{path}. Fetch the release history '
                         '(in GitHub Actions use actions/checkout with fetch-depth: 0).')
    return result.stdout


def check(root=ROOT):
    root = root.resolve()
    manifest = historical_blob(root, MANIFEST)
    if (root / MANIFEST).read_bytes() != manifest:
        raise ValueError(f'Frozen manifest differs from {RELEASE}: {MANIFEST}')
    verifier = historical_blob(root, VERIFIER)
    if (root / VERIFIER).read_bytes() != verifier:
        raise ValueError(f'Frozen verifier differs from {RELEASE}: {VERIFIER}')

    with tempfile.TemporaryDirectory() as directory:
        snapshot = Path(directory)
        (snapshot / PACKAGE).mkdir(parents=True)
        (snapshot / MANIFEST).write_bytes(manifest)
        for line in manifest.decode().splitlines():
            path = Path(line.split('  ', 1)[1])
            current = root / path
            if not current.is_file() or not current.resolve().is_relative_to(root):
                raise ValueError(f'Missing public snapshot path in current checkout: {path}')
            if path in LIVE_PAGES:
                data = historical_blob(root, path)
            elif path == VERIFIER:
                data = verifier
            else:
                data = current.read_bytes()
            target = snapshot / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        result = subprocess.run([sys.executable, str(snapshot / VERIFIER)], cwd=snapshot,
                                capture_output=True, text=True)
        if result.returncode:
            raise ValueError(result.stderr.strip() or 'Frozen C0/T03 verifier failed.')
        return result.stdout.strip()


if __name__ == '__main__':
    try:
        print(check())
        print(f'{len(LIVE_PAGES)} live navigation paths present, snapshot bytes read at {RELEASE}.')
    except (ValueError, OSError) as exc:
        sys.exit(str(exc))
