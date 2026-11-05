#!/usr/bin/env python3
"""Verify local migration packaging without executing research code."""

import hashlib
import json
from pathlib import Path
import sys
import zipfile


def verify_record(root, record, errors):
    """Check an immutable file, refusing absolute or escaping manifest paths."""
    relative = Path(record["path"])
    path = root / relative
    if relative.is_absolute() or ".." in relative.parts or not path.resolve().is_relative_to(root.resolve()):
        errors.append(f"Unsafe manifest path: {relative}")
        return
    if not path.is_file():
        errors.append(f"Missing source: {relative}")
        return
    data = path.read_bytes()
    if len(data) != record["bytes"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
        errors.append(f"Source identity mismatch: {relative}")


def check(root):
    errors = []
    manifest = json.loads((root / "research/CODEX_SOURCE_MANIFEST.json").read_text())
    refs = root / "local-only/migration"
    if manifest["root"] != "local-only/migration":
        return ["Unexpected local reference root"], 0, 0
    for record in manifest["files"]:
        verify_record(refs, record, errors)
    if errors:
        return errors, len(manifest["files"]), 0

    supplement = refs / "research_supplement"
    imported = json.loads((supplement / "IMPORT_MANIFEST.json").read_text())
    for record in imported["imports"]:
        verify_record(supplement, {**record, "path": record["destination"]}, errors)
    for record in imported["existing_synced_references"]:
        verify_record(refs, {**record, "path": record["workspace_path"]}, errors)

    archive_path = supplement / "T03/T03_RESEARCH_RECORD_20260910.zip"
    with zipfile.ZipFile(archive_path) as archive:
        bad_member = archive.testzip()
        if bad_member:
            errors.append(f"T03 ZIP CRC failure: {bad_member}")
        records = json.loads(archive.read("MANIFEST.json"))
        for record in records:
            data = archive.read(record["path"])
            if len(data) != record["bytes"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
                errors.append(f"T03 member identity mismatch: {record['path']}")
        for record in imported["t03_archive_verification"]["existing_sources_also_preserved_inside_original_archive"]:
            if archive.read(record["archive_member"]) != (refs / record["existing_workspace_path"]).read_bytes():
                errors.append(f"T03 duplicate state mismatch: {record['archive_member']}")

    for name, digest in imported["c4_hashes_matched_to_current_state"].items():
        data = (supplement / "T02/phase_c4" / name).read_bytes()
        if hashlib.sha256(data).hexdigest() != digest:
            errors.append(f"C4 recorded identity mismatch: {name}")
    for name in ("AGENTS.md", "docs/CODEX_SETUP.md", "research/CURRENT_PROJECT_MAP.md",
                 "research/CODEX_MIGRATION_AUDIT.md", "research/templates/CONSTRUCTION_LEDGER.md"):
        if not (root / name).is_file():
            errors.append(f"Missing setup entry point: {name}")
    if len((root / "AGENTS.md").read_bytes()) >= 32768:
        errors.append("Root instructions reach the default 32 KiB project-document limit")
    return errors, len(manifest["files"]), len(records)


if __name__ == "__main__":
    try:
        errors, files, members = check(Path(__file__).resolve().parents[1])
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        print(f"Local setup verification failed: {error}", file=sys.stderr)
        sys.exit(1)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        sys.exit(1)
    print(f"Verified {files} local reference files, original import identities, "
          f"{members} T03 manifest members, duplicate states and C4 hashes. "
          "No research code executed.")
