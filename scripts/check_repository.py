#!/usr/bin/env python3
"""Check archive integrity and local Markdown destinations; no network calls."""

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check(root):
    errors = []
    manifest = json.loads((root / "research/manifest.json").read_text())
    for record in manifest["files"]:
        path = root / record["path"]
        if not path.is_file():
            errors.append(f"Missing archived source: {record['path']}")
            continue
        data = path.read_bytes()
        if len(data) != record["bytes"]:
            errors.append(f"Archived source size changed: {record['path']}")
        if hashlib.sha256(data).hexdigest() != record["sha256"]:
            errors.append(f"Archived source hash changed: {record['path']}")

    # Historical source links retain their original environment and must not be
    # rewritten just to satisfy navigation checks. Their bytes are checked above.
    archived = {root / record["path"] for record in manifest["files"]}
    markdown_files = [p for p in root.rglob("*.md") if ".git" not in p.parts and p not in archived]
    for path in markdown_files:
        # Ignore fenced examples; this deliberately checks destinations, not anchors.
        content = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
        for match in re.finditer(r"\[[^\]\n]*\]\((<[^>]+>|[^)\n]+)\)", content):
            raw = match.group(1).strip()
            target = raw[1:-1] if raw.startswith("<") else raw.split(' "', 1)[0]
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination = path.parent / unquote(parts.path)
            if not destination.exists():
                errors.append(f"Broken local link in {path.relative_to(root)}: {target}")
    registry_path = root / "research/tracks/registry.json"
    if registry_path.exists():
        registry = json.loads(registry_path.read_text())
        tracks = registry["tracks"]
        if len(tracks) != 4 or len({track["id"] for track in tracks}) != 4:
            errors.append("Expected the owner's four distinct research tracks")
        for track in tracks:
            for filename in ("SPEC.md", "STATUS.md"):
                path = registry_path.parent / track["directory"] / filename
                if not path.is_file():
                    errors.append(f"Missing {track['id']} track record: {filename}")
    return errors, len(manifest["files"]), len(markdown_files)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    errors, sources, documents = check(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        sys.exit(1)
    print(f"Verified {sources} archived source files and local links in {documents} Markdown files.")
