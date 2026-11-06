"""Verify the editor file against the frozen release and both reviewed fragments."""
import re
import unittest
from pathlib import Path

from scripts import check_quadratic_v6_references as refs


class EditorPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        exports = Path(__file__).resolve().parents[1] / 'research' / 'exports'
        cls.audit = exports / '2026-11-05-report-audit'
        cls.published = (exports / '2026-11-05-report-references' / 'bibliography-github.tex').read_bytes()
        cls.editor = (cls.audit / 'integration' / 'bibliography-v6-editor.tex').read_bytes()

    def test_only_the_reviewed_ref14_replaces_published_bytes(self):
        prefix, entries = self.published.split(br'\bibitem{ref14}')
        _, suffix = entries.split(br'\bibitem{ref15}')
        ref14 = (self.audit / 'quadratic' / 'ref14-editor.tex').read_bytes().rstrip(b'\n')
        self.assertEqual(self.editor, prefix + ref14 + b'\n\n' + br'\bibitem{ref15}' + suffix)
        self.assertIn(b'Section 7, (RC15/4)', ref14)

    def test_reviewed_locators_and_source_revision(self):
        bib = self.editor.decode()
        ref15 = bib.split(r'\bibitem{ref15}')[1].split(r'\bibitem{ref16}')[0]
        self.assertIn('Sections 1--5', ref15)
        ref17 = bib.split(r'\bibitem{ref17}')[1].split('\n%', 1)[0].strip()
        cubic = (self.audit / 'cubic' / 'citation-snippets.tex').read_text()
        self.assertEqual(ref17, cubic.split(r'\bibitem{ref17}')[1].strip())
        self.assertIn('Its complete standalone proof was unavailable for this revision.', ref17)
        links = [url for url in re.findall(r'\\href\{([^}]+)\}', bib) if url.startswith(refs.PREFIX)]
        self.assertEqual(links, [f'{refs.PREFIX}{refs.SUPPORT_REVISION}/{refs.INDEX}#{key}'
                                 for key in refs.PROJECT_KEYS])
