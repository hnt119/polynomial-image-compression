import csv
import hashlib
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

from scripts import check_quadratic_v6_references as refs


class ReferenceAuditTests(unittest.TestCase):
    def make_repo(self, target='proof.md', cross_link='#ref5'):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name).resolve()
        package = root / refs.PACKAGE
        package.mkdir(parents=True)
        source = package / 'proof.md'
        source.write_text('Original proof witness\n')
        sha = hashlib.sha256(source.read_bytes()).hexdigest()
        with (root / refs.PROVENANCE).open('w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('path', 'origin', 'selection', 'origin_sha256', 'public_sha256'))
            writer.writerow((refs.PACKAGE+'/proof.md', 'proof.md', 'entire original file', sha, sha))
        (root / refs.INDEX).write_text(''.join(f'## {key}\n\n[Proof]({target})\n\n' for key in refs.PROJECT_KEYS)
                                       + f'[Related]({cross_link})\n')
        for args in (['init', '-q'], ['add', 'research'], ['-c', 'user.name=Fixture', '-c',
                'user.email=fixture@example.invalid', 'commit', '-qm', 'Original evidence']):
            subprocess.run(['git', *args], cwd=root, check=True)
        pin = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
        original_pin = patch.object(refs, 'SUPPORT_REVISION', pin)
        original_pin.start()
        self.addCleanup(original_pin.stop)
        content = []
        for key in refs.ALL_KEYS:
            line = '\\bibitem{'+key+'}\n'
            if key in refs.PROJECT_KEYS:
                line += '\\href{'+refs.PREFIX+pin+'/'+refs.INDEX+'#'+key+'}{evidence}\n'
            content.append(line)
        bib = package / 'bibliography-github.tex'
        bib.write_text(''.join(content))
        return root, bib, pin

    def test_full_revision_and_current_checkout(self):
        root, _, pin = self.make_repo()
        self.assertEqual(refs.check(root), ((13, 1), {pin: (13, 1)}))

    def test_selected_bibliography_is_checked_independently(self):
        root, published, _ = self.make_repo()
        editor = root / 'editor.tex'
        editor.write_text(published.read_text().replace('#ref14}', '#ref15}'))
        with self.assertRaisesRegex(ValueError, 'Wrong commit pin, index path or anchor: ref14'):
            refs.check(root, bibliography='editor.tex')
        refs.check(root)

    def test_later_file_cannot_fill_a_historical_gap(self):
        root, _, _ = self.make_repo(target='later.md')
        (root / refs.PACKAGE / 'later.md').write_text('Present only in this checkout')
        with self.assertRaisesRegex(ValueError, 'Missing historical blob'):
            refs.check(root)

    def test_wrong_but_existing_anchor_or_short_pin(self):
        root, bib, pin = self.make_repo()
        valid = bib.read_text()
        for bad in (valid.replace('#ref5}', '#ref6}'), valid.replace(pin, pin[:8])):
            with self.subTest(bad=bad[:60]):
                bib.write_text(bad)
                with self.assertRaisesRegex(ValueError, 'Wrong commit pin, index path or anchor: ref5'):
                    refs.check(root)

    def test_missing_relative_anchor(self):
        root, _, _ = self.make_repo(cross_link='#ref99')
        with self.assertRaisesRegex(ValueError, 'Unresolved anchor'):
            refs.check(root)

    def test_changed_working_provenance_copy(self):
        root, _, _ = self.make_repo()
        (root / refs.PACKAGE / 'proof.md').write_text('different')
        with self.assertRaisesRegex(ValueError, 'Public digest mismatch'):
            refs.check(root)

    def test_reference_heading_needs_its_own_source(self):
        root, _, _ = self.make_repo()
        index = root / refs.INDEX
        index.write_text(index.read_text().replace('## ref9\n\n[Proof](proof.md)',
                                                   '## ref9\n\n[Neighbor](#ref10)'))
        with self.assertRaisesRegex(ValueError, 'Missing source file link under ref9'):
            refs.check(root)

    def test_nonempty_provenance_cannot_discard_an_original(self):
        root, _, _ = self.make_repo()
        manifest = root / refs.PROVENANCE
        manifest.write_text(manifest.read_text().replace('/proof.md,proof.md', '/other.md,other.md'))
        with self.assertRaisesRegex(ValueError, 'Missing or changed source-support provenance row'):
            refs.check(root)
