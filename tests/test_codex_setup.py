"""Regression checks for source identity and private historical-link isolation."""

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from scripts.check_codex_setup import verify_record
from scripts.check_repository import check


class LocalSourceIntegrityTests(unittest.TestCase):
    def test_content_mutation_is_rejected_even_at_same_size(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "source.md"
            path.write_bytes(b"original")
            record = {"path": "source.md", "bytes": 8,
                      "sha256": hashlib.sha256(b"original").hexdigest()}
            errors = []
            verify_record(root, record, errors)
            self.assertEqual(errors, [])
            path.write_bytes(b"changed!")
            verify_record(root, record, errors)
            self.assertTrue(any("identity mismatch" in error for error in errors))

    def test_missing_and_escaping_paths_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, expected in (("absent.md", "Missing source"),
                                   ("../outside.md", "Unsafe manifest path"),
                                   (str(root / "absolute.md"), "Unsafe manifest path")):
                with self.subTest(name=name):
                    errors = []
                    verify_record(root, {"path": name, "bytes": 0, "sha256": ""}, errors)
                    self.assertTrue(any(expected in error for error in errors))

    def test_private_links_are_skipped_but_public_links_are_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "research").mkdir()
            (root / "research/manifest.json").write_text(json.dumps({"files": []}))
            (root / "local-only").mkdir()
            (root / "local-only/history.md").write_text("[old](missing-old-source.md)")
            self.assertEqual(check(root)[0], [])
            (root / "README.md").write_text("[current](missing-current-source.md)")
            errors = check(root)[0]
            self.assertEqual(len(errors), 1)
            self.assertIn("missing-current-source.md", errors[0])


if __name__ == "__main__":
    unittest.main()
