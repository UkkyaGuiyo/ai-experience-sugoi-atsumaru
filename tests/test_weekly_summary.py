"""Execute the actual inline summary with in-memory proposals, never stored fixtures."""
import os
from pathlib import Path
import tempfile
import textwrap
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / '.github/workflows/knowledge-safety-check.yml').read_text(encoding='utf-8')
CODE = textwrap.dedent(WORKFLOW.split("python -B - <<'PY'\n", 1)[1].rsplit('          PY', 1)[0])


class SummaryTests(unittest.TestCase):
    def render(self, documents, scan='success'):
        proposals = []
        for name, body in documents:
            proposal = Mock()
            proposal.as_posix.return_value = name
            proposal.read_text.return_value = body
            proposals.append(proposal)
        roots = {'docs/proposals': Mock(), 'knowledge': Mock()}
        roots['docs/proposals'].rglob.return_value = proposals
        roots['knowledge'].rglob.return_value = []
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / 'summary.md'
            with patch.dict(os.environ, {'TEST_RESULT': 'success', 'SCAN_RESULT': scan,
                                         'GITHUB_STEP_SUMMARY': str(report)}), \
                    patch('pathlib.Path', side_effect=lambda name: roots[name]) as paths:
                exec(compile(CODE, '<workflow-summary>', 'exec'), {})
            return report.read_text(encoding='utf-8'), paths

    def test_empty_is_noop_with_usage_notice(self):
        summary, _ = self.render([])
        self.assertIn('successful no-op', summary)
        self.assertIn('startup still consumes', summary)
        self.assertIn('Pending documents: 0', summary)

    def test_unreviewed_and_unknown_stay_pending(self):
        for header in ['', 'Review status: PENDING_REVIEW', 'Review status: UNKNOWN',
                       'Review status: REVIEWED\nReview status: PENDING_REVIEW',
                       '## Example\nReview status: REVIEWED']:
            with self.subTest(header=header):
                summary, _ = self.render([('docs/proposals/check.md', '# Proposal\n' + header)])
                self.assertIn('<code>docs/proposals/check.md</code> | PENDING_REVIEW', summary)

    def test_explicit_dispositions_are_excluded(self):
        for state in ['REVIEWED', 'REJECTED', 'FORMALIZED']:
            with self.subTest(state=state):
                summary, _ = self.render([('docs/proposals/done.md',
                                          '# Proposal\nReview status: ' + state + '\n## Details')])
                self.assertIn('Pending documents: 0', summary)
                self.assertNotIn('<code>docs/proposals/done.md', summary)

    def test_markup_is_escaped_and_private_filename_withheld(self):
        summary, _ = self.render([('docs/proposals/a<test>|.md', '# Proposal')])
        self.assertIn('a&lt;test&gt;&#124;.md', summary)
        self.assertNotIn('a<test>', summary)
        for name in ['someone' + chr(64) + 'example.org.md', 'line\nbreak.md']:
            summary, _ = self.render([('docs/proposals/' + name, '# Proposal')])
            self.assertIn('filename withheld', summary)
            self.assertNotIn(name, summary)

    def test_failed_scan_never_reads_queue(self):
        summary, paths = self.render([('docs/proposals/check.md', 'UNREAD_BODY')], 'failure')
        paths.assert_not_called()
        self.assertIn('Queue withheld', summary)
        self.assertNotIn('UNREAD_BODY', summary)


if __name__ == '__main__':
    unittest.main()
