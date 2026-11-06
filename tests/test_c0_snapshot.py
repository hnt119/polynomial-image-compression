from pathlib import Path
import subprocess
import tempfile
import unittest

from scripts import check_c0_snapshot as snapshot


class C0SnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        temporary = tempfile.TemporaryDirectory()
        cls.addClassCleanup(temporary.cleanup)
        cls.root = Path(temporary.name) / 'fixture'
        subprocess.run(['git', 'clone', '--quiet', '--shared', '--no-checkout',
                        str(snapshot.ROOT), str(cls.root)], check=True)
        # Materialize only the files actually covered by the frozen release.
        manifest = snapshot.historical_blob(cls.root, snapshot.MANIFEST)
        paths = [line.split('  ', 1)[1] for line in manifest.decode().splitlines()]
        subprocess.run(['git', 'restore', '--source', snapshot.RELEASE, '--worktree', '--',
                        str(snapshot.MANIFEST), *paths], cwd=cls.root, check=True)

    def change(self, path, replacement):
        path = self.root / path
        self.addCleanup(path.write_bytes, path.read_bytes())
        if replacement is None:
            path.unlink()
        else:
            path.write_bytes(replacement)

    def test_only_five_live_pages_may_evolve(self):
        for path in snapshot.LIVE_PAGES:
            self.change(path, b'New navigation\n')
        self.assertIn('267 SHA-256 matches', snapshot.check(self.root))
        self.assertTrue(all((self.root / path).read_bytes() == b'New navigation\n'
                            for path in snapshot.LIVE_PAGES))

    def test_live_path_must_still_exist(self):
        self.change('research/OPEN_LEMMAS.md', None)
        with self.assertRaisesRegex(ValueError, 'Missing public snapshot path'):
            snapshot.check(self.root)

    def test_current_evidence_bytes_are_checked(self):
        self.change(snapshot.PACKAGE / 'research_report.pdf', b'wrong proof')
        with self.assertRaisesRegex(ValueError, 'digest mismatch: .*research_report.pdf'):
            snapshot.check(self.root)

    def test_manifest_and_verifier_cannot_be_substituted(self):
        for path in (snapshot.MANIFEST, snapshot.VERIFIER):
            with self.subTest(path=path):
                self.change(path, b'')
                with self.assertRaisesRegex(ValueError, 'Frozen (manifest|verifier) differs'):
                    snapshot.check(self.root)
                self.doCleanups()
