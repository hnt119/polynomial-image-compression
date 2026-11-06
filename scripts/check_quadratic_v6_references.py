#!/usr/bin/env python3
"""Verify the v6 bibliography, reference index and published source copies offline."""
import argparse
import csv
import hashlib
import io
import posixpath
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = 'research/exports/2026-11-05-report-references'
PUBLISHED_BIBLIOGRAPHY = PACKAGE + '/bibliography-github.tex'
INDEX = PACKAGE + '/README.md'
PROVENANCE = PACKAGE + '/source-provenance.csv'
SUPPORT_REVISION = 'bd1f2d663262821575eebdfa559b7c25f76b46ab'
PREFIX = 'https://github.com/hnt119/polynomial-image-compression/blob/'
ALL_KEYS = [f'ref{i}' for i in range(1, 18)] + ['refErdos', 'refSST', 'refPohoata', 'refLiu']
PROJECT_KEYS = ALL_KEYS[4:17]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_git(root, revision, path):
    result = subprocess.run(['git', 'cat-file', 'blob', f'{revision}:{path}'], cwd=root,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    require(result.returncode == 0, f'Missing historical blob {revision}:{path}. Use a full-history checkout.')
    return result.stdout


def read_local(root, path):
    file = (root / path).resolve()
    require(file.is_relative_to(root) and file.is_file(), f'Missing local file: {path}')
    return file.read_bytes()


def repository_path(base, link):
    decoded = unquote(link)
    require(not decoded.startswith('/') and '\\' not in decoded, f'Invalid relative path: {link}')
    path = posixpath.normpath(posixpath.join(base, decoded))
    require(path != '..' and not path.startswith('../'), f'Link leaves repository: {link}')
    return path


def check_index(read):
    index = read(INDEX).decode()
    headings = re.findall(r'^## (ref\d+)\s*$', index, re.M)
    require(headings == PROJECT_KEYS, 'Missing, duplicated or reordered reference headings')
    link_pattern = r'\[[^\]\n]+\]\(([^)\s]+)\)'
    for section in re.split(r'(?m)^## ', index)[1:]:
        heading, _, body = section.partition('\n')
        if heading in PROJECT_KEYS:
            require(any(urlsplit(link).path for link in re.findall(link_pattern, body)),
                    f'Missing source file link under {heading}')
    links = re.findall(link_pattern, index)
    count = 0
    for link in links:
        url = urlsplit(link)
        require(not url.scheme and not url.netloc and not url.query, f'Expected a repository link: {link}')
        target = repository_path(PACKAGE, url.path) if url.path else INDEX
        data = read(target) if target != INDEX else index.encode()
        if url.fragment:
            # The shipped index uses literal ref headings. Reject any unsupported anchor syntax.
            require(re.fullmatch(r'ref\d+', url.fragment) and
                    re.search(r'^## '+re.escape(url.fragment)+r'\s*$', data.decode(), re.M),
                    f'Unresolved anchor: {link}')
        count += bool(url.path)
    return count


def check_provenance(read, original_records):
    records = list(csv.DictReader(io.StringIO(read(PROVENANCE).decode())))
    require(records and len({r['path'] for r in records}) == len(records), 'Empty or duplicate provenance')
    indexed = {row['path']: row for row in records}
    for original in original_records:
        require(indexed.get(original['path']) == original,
                f'Missing or changed source-support provenance row: {original["path"]}')
    for row in records:
        path = repository_path('', row['path'])
        require(path == row['path'] and row['selection'] and row['origin'], f'Invalid provenance: {path}')
        require(re.fullmatch(r'[0-9a-f]{64}', row['origin_sha256']), f'Invalid original digest: {path}')
        require(hashlib.sha256(read(path)).hexdigest() == row['public_sha256'], f'Public digest mismatch: {path}')
        if row['selection'] == 'entire original file':
            require(row['origin_sha256'] == row['public_sha256'], f'Full original digest mismatch: {path}')
    return len(records)


def check(root=ROOT, bibliography=PUBLISHED_BIBLIOGRAPHY):
    root = root.resolve()
    bib = read_local(root, bibliography).decode()
    entries = re.split(r'(?m)^\\bibitem\{([^}]+)\}', bib)
    require(entries[1::2] == ALL_KEYS, 'Wrong bibliography keys or order')
    revisions = set()
    for key, body in zip(entries[1::2], entries[2::2]):
        urls = [u for u in re.findall(r'\\href\{([^}]+)\}', body) if u.startswith(PREFIX)]
        if key not in PROJECT_KEYS:
            require(not urls, f'Unexpected project citation: {key}')
            continue
        require(len(urls) == 1, f'Expected one project citation: {key}')
        match = re.fullmatch(re.escape(PREFIX)+r'([0-9a-f]{40})/'+re.escape(INDEX+'#'+key), urls[0])
        require(match, f'Wrong commit pin, index path or anchor: {key}')
        revisions.add(match[1])
    # This immutable inventory defines the required source copies, including the one excerpt.
    original_records = list(csv.DictReader(io.StringIO(read_git(root, SUPPORT_REVISION, PROVENANCE).decode())))
    historical = {}
    for revision in sorted(revisions):
        typ = subprocess.run(['git', 'cat-file', '-t', revision], cwd=root, capture_output=True)
        require(typ.stdout.strip() == b'commit', f'Missing commit {revision}. Use a full-history checkout.')
        def read(path):
            return read_git(root, revision, path)
        historical[revision] = (check_index(read), check_provenance(read, original_records))
    def read(path):
        return read_local(root, path)
    return (check_index(read), check_provenance(read, original_records)), historical


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bibliography', default=PUBLISHED_BIBLIOGRAPHY,
                        help='repository-relative TeX file (default: the published bibliography)')
    args = parser.parse_args()
    try:
        current, historical = check(bibliography=args.bibliography)
    except (OSError, ValueError, KeyError) as error:
        raise SystemExit(str(error))
    print(f'{args.bibliography}: 21 bibliography keys, 13 pinned citations. (Index file links, provenance records)')
    print('Working checkout:', current)
    for pin, counts in historical.items():
        print(pin, counts)
