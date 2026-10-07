"""Only invented values assembled in memory; never real experience or secrets."""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import shutil
import sys
sys.dont_write_bytecode = True
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate_knowledge.py')
v = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = v
SPEC.loader.exec_module(v)
SCHEMA = json.loads((ROOT / 'schema/experience-entry.schema.json').read_text(encoding='utf-8'))


def entry():
    result = {key: '架空の抽象的な検証値' for key in SCHEMA['required']}
    result.update(id='EXP-000001', category='experiments', observation_date='2026-01-01',
                  evidence_type='inference', reproduction_status='not reproduced',
                  confidence='low', knowledge_status='current', related_knowledge_ids=[],
                  safety_review={'status': 'approved', 'independent_review': True,
                                 'data_minimization': True, 'no_identifiers': True,
                                 'no_private_data': True, 'rights_checked': True})
    return result


class SchemaTests(unittest.TestCase):
    def test_valid_invented_entry(self):
        self.assertEqual(v.schema_errors(entry(), SCHEMA), [])

    def test_all_required_fields(self):
        for key in SCHEMA['required']:
            with self.subTest(key=key):
                value = entry()
                del value[key]
                self.assertTrue(v.schema_errors(value, SCHEMA))

    def test_extra_identification_field_rejected(self):
        value = entry()
        value['person'] = '架空'
        self.assertTrue(v.schema_errors(value, SCHEMA))

    def test_review_requires_every_check(self):
        for key in entry()['safety_review']:
            with self.subTest(key=key):
                value = entry()
                value['safety_review'][key] = False
                self.assertTrue(v.schema_errors(value, SCHEMA))

    def test_failure_details_required_and_complete(self):
        value = entry()
        value['category'] = 'failures'
        self.assertTrue(v.schema_errors(value, SCHEMA))
        fields = SCHEMA['properties']['failure_details']['required']
        value['failure_details'] = {key: '架空の検証値' for key in fields}
        self.assertEqual(v.schema_errors(value, SCHEMA), [])
        for key in fields:
            altered = copy.deepcopy(value)
            del altered['failure_details'][key]
            self.assertTrue(v.schema_errors(altered, SCHEMA))

    def test_date_and_history(self):
        value = entry()
        value['knowledge_status'] = 'historical'
        self.assertEqual(v.schema_errors(value, SCHEMA), [])
        for invalid in ['2026-02-30', '20260101', 'unknown']:
            value['observation_date'] = invalid
            self.assertTrue(v.schema_errors(value, SCHEMA))

    def test_bounds_types_enums_and_related_unique(self):
        for key, invalid in [('title', ''), ('title', 'x' * 161), ('confidence', 'certain'),
                             ('related_knowledge_ids', ['EXP-000002', 'EXP-000002']),
                             ('ai_system', 1)]:
            value = entry()
            value[key] = invalid
            self.assertTrue(v.schema_errors(value, SCHEMA))

    def test_unsupported_nested_schema_fails_even_absent(self):
        schema = copy.deepcopy(SCHEMA)
        schema['properties']['model']['unknownKeyword'] = True
        self.assertTrue(v.schema_errors(entry(), schema))

    def test_malformed_schema_constraints_fail_closed(self):
        for key, invalid in [('minLength', -1), ('minLength', True), ('pattern', '['),
                             ('format', 'unknown')]:
            schema = copy.deepcopy(SCHEMA)
            schema['properties']['title'][key] = invalid
            self.assertTrue(v.unsupported_schema(schema))
        for key, invalid in [('additionalProperties', 'false'), ('required', 'title'),
                             ('properties', []), ('type', 'unknown')]:
            schema = copy.deepcopy(SCHEMA)
            schema[key] = invalid
            self.assertTrue(v.unsupported_schema(schema))

    def test_source_safety_and_uri(self):
        value = entry()
        value['sources'] = [{'type': 'official documentation', 'url': 'https://docs.python.org/3/',
                             'source_safety_review': True}]
        self.assertEqual(v.schema_errors(value, SCHEMA), [])
        for url in ['http://docs.python.org/', 'https://docs.python.org/?sensitive=value',
                    'https://docs.python.org:invalid/']:
            value['sources'][0]['url'] = url
            self.assertTrue(v.schema_errors(value, SCHEMA))


class ScanTests(unittest.TestCase):
    def codes(self, text):
        return {finding.code for finding in v.scan_text(text)}

    def test_synthetic_candidate_families(self):
        candidates = [
            ('EMAIL', 'invented' + '@' + 'example.invalid'),
            ('PHONE', '012' + '-' + '345' + '-' + '6789'),
            ('IP_ADDRESS', '.'.join(['192', '0', '2', '1'])),
            ('IP_ADDRESS', ':'.join(['2001', 'db8', '', '1'])),
            ('IP_ADDRESS', ':' * 2 + '1'),
            ('INTERNATIONAL_PHONE', '+' + '12345678901'),
            ('DOMESTIC_PHONE', '090' + '12345678'),
            ('PRIVATE_KEY', '-' * 5 + 'BEGIN ' + 'PRIVATE KEY' + '-' * 5),
            ('API_KEY', 'sk' + '-' + 'A' * 30),
            ('API_KEY', 'AI' + 'za' + 'A' * 35),
            ('API_KEY', 'AK' + 'IA' + 'A' * 16),
            ('ACCESS_TOKEN', 'gh' + 'p_' + 'A' * 36),
            ('ACCESS_TOKEN', 'github' + '_pat_' + 'A' * 30),
            ('ACCESS_TOKEN', 'xox' + 'b-' + 'A' * 30),
            ('DANGEROUS_ASSIGNMENT', 'pass' + 'word = ' + chr(34) + 'invented-value' + chr(34)),
            ('DANGEROUS_ASSIGNMENT', 'sec' + 'ret: ' + chr(39) + 'invented-value' + chr(39)),
            ('UNQUOTED_CREDENTIAL', 'to' + 'ken=synthetic-value'),
            ('BEARER_TOKEN', 'Bear' + 'er ' + 'A' * 20),
            ('JWT', 'ey' + 'J' + 'A' * 12 + '.' + 'A' * 12 + '.' + 'A' * 12),
            ('PERSONAL_URL', 'https://' + 'x' + '.com/' + 'invented-profile'),
            ('PROFILE_URL', 'https://' + 'github' + '.com/' + 'invented-profile'),
        ]
        for code, text in candidates:
            with self.subTest(code=code):
                self.assertIn(code, self.codes(text))

    def test_raw_large_conversation(self):
        text = ('us' + 'er: ' + 'x' * 7000 + '\n') * 12
        self.assertIn('RAW_TRANSCRIPT', self.codes(text))

    def test_versions_dates_and_policy_terms_are_not_candidates(self):
        self.assertEqual(self.codes('2026-10-07 Python 3.14.6 password secret token API key'), set())

    def test_invalid_address_is_not_ip(self):
        self.assertNotIn('IP_ADDRESS', self.codes('.'.join(['999', '999', '999', '999'])))


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'schema').mkdir()
        shutil.copyfile(ROOT / 'schema/experience-entry.schema.json', self.root / 'schema/experience-entry.schema.json')

    def write(self, path, value):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(value, ensure_ascii=False), encoding='utf-8')

    def codes(self):
        return {finding.code for finding in v.validate_repository(self.root)[0]}

    def test_empty_repository_is_explicit(self):
        self.assertEqual(v.validate_repository(self.root), ([], 0))

    def test_valid_entry_and_category_path(self):
        self.write('knowledge/experiments/one.json', entry())
        self.assertEqual(v.validate_repository(self.root), ([], 1))
        self.write('knowledge/tools/two.json', entry())
        self.assertIn('CATEGORY_PATH', self.codes())
        self.assertIn('DUPLICATE_ID', self.codes())

    def test_missing_and_self_related_ids(self):
        for ref in ['EXP-000002', 'EXP-000001']:
            value = entry()
            value['related_knowledge_ids'] = [ref]
            self.write('knowledge/experiments/one.json', value)
            self.assertIn('RELATED_ID', self.codes())

    def test_schema_violation(self):
        self.write('knowledge/experiments/one.json', {})
        self.assertIn('SCHEMA_VIOLATION', self.codes())

    def test_duplicate_json_keys_rejected(self):
        target = self.root / 'knowledge/experiments/one.json'
        target.parent.mkdir(parents=True)
        target.write_text('{"id": "one", "id": "two"}', encoding='utf-8')
        self.assertIn('INVALID_JSON', self.codes())

    def test_scan_includes_code_and_tests(self):
        for path in ['scripts/new.py', 'tests/new.py', 'docs/new.md']:
            self.write(path, 'invented' + '@' + 'example.invalid')
        self.assertIn('EMAIL', self.codes())

    def test_escaped_json_candidate_is_detected(self):
        value = entry()
        value['goal'] = 'invented' + '@' + 'example.invalid'
        target = self.root / 'knowledge/experiments/one.json'
        target.parent.mkdir(parents=True)
        serialized = json.dumps(value).replace('@', '\\u0040')
        target.write_text(serialized, encoding='utf-8')
        self.assertIn('EMAIL', self.codes())

    def test_decoded_json_key_assignment_is_detected(self):
        value = {'pass' + 'word': 'synthetic-value'}
        serialized = json.dumps(value).replace('password', '\\u0070assword')
        (self.root / 'invented.json').write_text(serialized, encoding='utf-8')
        self.assertIn('DANGEROUS_ASSIGNMENT', self.codes())

    def test_structured_giant_dialogue_is_detected(self):
        value = [{'role': 'user', 'content': 'x' * 7000} for _ in range(12)]
        self.write('invented.json', value)
        self.assertIn('RAW_TRANSCRIPT', self.codes())

    def test_cache_directory_is_scanned(self):
        self.write('docs/__pycache__/hidden.json', 'invented' + '@' + 'example.invalid')
        self.assertIn('EMAIL', self.codes())

    def test_forbidden_binary_oversize_and_wrong_entry_format(self):
        (self.root / 'capture.png').write_bytes(b'\x00')
        (self.root / 'huge.txt').write_text('x' * (1048576 + 1), encoding='utf-8')
        self.write('knowledge/experiments/raw.md', 'invented')
        self.assertTrue({'FORBIDDEN_FILE', 'UNREADABLE_OR_BINARY', 'OVERSIZED_FILE', 'KNOWLEDGE_FORMAT'} <= self.codes())

    def test_diagnostics_never_echo_content(self):
        candidate = 'invented' + '@' + 'example.invalid'
        self.write('docs/check.md', candidate)
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            self.assertEqual(v.main([str(self.root)]), 1)
        self.assertNotIn(candidate, capture.getvalue())
        self.assertIn('EMAIL', capture.getvalue())

    def test_schema_definition_failure(self):
        schema = copy.deepcopy(SCHEMA)
        schema['unsupportedKeyword'] = True
        self.write('schema/experience-entry.schema.json', schema)
        self.assertIn('SCHEMA_DEFINITION', self.codes())

    def test_forbidden_environment_file(self):
        (self.root / '.env.local').write_text('invented', encoding='utf-8')
        self.assertIn('FORBIDDEN_FILE', self.codes())

    def test_japanese_document_encoding_and_required_files(self):
        self.assertTrue((ROOT / 'README.md').read_text(encoding='utf-8').startswith('# AIの経験がスゴーイアツマール'))
        required = ['AGENTS.md', 'README.md', 'CONTRIBUTING.md', 'SECURITY.md',
                    'docs/PRIVACY_RULES.md', 'docs/COLLECTION_POLICY.md', 'docs/SOURCE_POLICY.md',
                    'docs/KNOWLEDGE_MODEL.md', 'docs/AGENT_OPERATIONS.md', 'docs/MIGRATION_POLICY.md',
                    'templates/EXPERIENCE_ENTRY.md', '.github/pull_request_template.md',
                    '.github/workflows/knowledge-safety-check.yml']
        self.assertTrue(all((ROOT / path).is_file() for path in required))


if __name__ == '__main__':
    unittest.main()
